# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T20:33:56Z |
| **Shift Time** | 20:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **47** |
| False Positives Filtered | **29** (38.2%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **15** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **69** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **24** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **15** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `admin` | 2 |
| `345gs5662d34` | 2 |
| `Support` | 1 |
| `Root` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 3 |
| `techsupport` | 2 |
| `345gs5662d34` | 2 |
| `abcd1234` | 1 |
| `444444` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 3 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `Support` | `techsupport` | 1 |
| `Root` | `abcd1234` | 1 |
| `admin` | `444444` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `192.42.116.94` | 2026-04-02T19:35:43 |
| `root` | `uU123456` | `120.48.175.69` | 2026-04-02T19:39:46 |
| `root` | `3245gs5662d34` | `120.48.175.69` | 2026-04-02T19:40:04 |
| `root` | `123123abc` | `50.225.176.238` | 2026-04-02T20:28:51 |
| `root` | `3245gs5662d34` | `50.225.176.238` | 2026-04-02T20:28:56 |
| `root` | `Pa55word.1` | `101.36.108.125` | 2026-04-02T20:31:08 |
| `root` | `3245gs5662d34` | `101.36.108.125` | 2026-04-02T20:31:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **76** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 15 |
| libssh | 12 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |
| `03a80b21afa8...` | Modern SSH client | 12 | 5 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |
| `03a80b21afa8...` | libssh | 12 | 5 | Modern SSH client |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.36.108.125`, `50.225.176.238`, `120.48.175.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **25** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS215125` | Church of Cyberology | 1 | HIGH |
| `AS10796` | Charter Communications Inc | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |
| `AS11290` | Cogeco Connexion inc | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-43703d8593d1

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]94` |
| **First Seen** | 2026-04-02 19:35 |
| **Last Seen** | 2026-04-02 19:36 |
| **Session Duration** | 20s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 19:35:39` | `cowrie.session.connect` |
| `2026-04-02 19:35:39` | `cowrie.client.version` |
| `2026-04-02 19:35:39` | `cowrie.client.kex` |
| `2026-04-02 19:35:43` | `cowrie.client.fingerprint` |
| `2026-04-02 19:35:43` | `cowrie.login.failed` |
| `2026-04-02 19:35:43` | `cowrie.login.success` |
| `2026-04-02 19:35:58` | `cowrie.direct-tcpip.request` |
| `2026-04-02 19:35:59` | `cowrie.direct-tcpip.ja4` |
| `2026-04-02 19:35:59` | `cowrie.direct-tcpip.data` |
| `2026-04-02 19:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]94` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f7e7dcf5fb

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]69` |
| **First Seen** | 2026-04-02 19:39 |
| **Last Seen** | 2026-04-02 19:40 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 19:39:44` | `cowrie.session.connect` |
| `2026-04-02 19:39:44` | `cowrie.client.version` |
| `2026-04-02 19:39:44` | `cowrie.client.kex` |
| `2026-04-02 19:39:46` | `cowrie.login.success` |
| `2026-04-02 19:39:47` | `cowrie.session.params` |
| `2026-04-02 19:39:47` | `cowrie.command.input` |
| `2026-04-02 19:39:47` | `cowrie.command.failed` |
| `2026-04-02 19:39:48` | `cowrie.log.closed` |
| `2026-04-02 19:39:49` | `cowrie.session.params` |
| `2026-04-02 19:39:49` | `cowrie.command.input` |
| `2026-04-02 19:39:50` | `cowrie.session.file_download` |
| `2026-04-02 19:39:50` | `cowrie.log.closed` |
| `2026-04-02 19:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]69` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62814476257f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]69` |
| **First Seen** | 2026-04-02 19:40 |
| **Last Seen** | 2026-04-02 19:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 19:40:00` | `cowrie.session.connect` |
| `2026-04-02 19:40:00` | `cowrie.client.version` |
| `2026-04-02 19:40:01` | `cowrie.client.kex` |
| `2026-04-02 19:40:04` | `cowrie.login.success` |
| `2026-04-02 19:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]69` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b8bb7cdc67

| Field | Detail |
|---|---|
| **Source IP** | `50.225.176[.]238` |
| **First Seen** | 2026-04-02 20:28 |
| **Last Seen** | 2026-04-02 20:28 |
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
| `2026-04-02 20:28:50` | `cowrie.session.connect` |
| `2026-04-02 20:28:50` | `cowrie.client.version` |
| `2026-04-02 20:28:50` | `cowrie.client.kex` |
| `2026-04-02 20:28:51` | `cowrie.login.success` |
| `2026-04-02 20:28:52` | `cowrie.session.params` |
| `2026-04-02 20:28:52` | `cowrie.command.input` |
| `2026-04-02 20:28:52` | `cowrie.command.failed` |
| `2026-04-02 20:28:52` | `cowrie.log.closed` |
| `2026-04-02 20:28:52` | `cowrie.session.params` |
| `2026-04-02 20:28:52` | `cowrie.command.input` |
| `2026-04-02 20:28:53` | `cowrie.session.file_download` |
| `2026-04-02 20:28:53` | `cowrie.log.closed` |
| `2026-04-02 20:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.225.176[.]238` to AbuseIPDB if not already reported
- [ ] Block `50.225.176[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3c640a88d5

| Field | Detail |
|---|---|
| **Source IP** | `50.225.176[.]238` |
| **First Seen** | 2026-04-02 20:28 |
| **Last Seen** | 2026-04-02 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 20:28:55` | `cowrie.session.connect` |
| `2026-04-02 20:28:55` | `cowrie.client.version` |
| `2026-04-02 20:28:56` | `cowrie.client.kex` |
| `2026-04-02 20:28:56` | `cowrie.login.success` |
| `2026-04-02 20:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.225.176[.]238` to AbuseIPDB if not already reported
- [ ] Block `50.225.176[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30aa687a9736

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]125` |
| **First Seen** | 2026-04-02 20:31 |
| **Last Seen** | 2026-04-02 20:31 |
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
| `2026-04-02 20:31:07` | `cowrie.session.connect` |
| `2026-04-02 20:31:07` | `cowrie.client.version` |
| `2026-04-02 20:31:07` | `cowrie.client.kex` |
| `2026-04-02 20:31:08` | `cowrie.login.success` |
| `2026-04-02 20:31:08` | `cowrie.session.params` |
| `2026-04-02 20:31:08` | `cowrie.command.input` |
| `2026-04-02 20:31:08` | `cowrie.command.failed` |
| `2026-04-02 20:31:08` | `cowrie.log.closed` |
| `2026-04-02 20:31:08` | `cowrie.session.params` |
| `2026-04-02 20:31:08` | `cowrie.command.input` |
| `2026-04-02 20:31:08` | `cowrie.session.file_download` |
| `2026-04-02 20:31:08` | `cowrie.log.closed` |
| `2026-04-02 20:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-686e33e783c6

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]125` |
| **First Seen** | 2026-04-02 20:31 |
| **Last Seen** | 2026-04-02 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 20:31:10` | `cowrie.session.connect` |
| `2026-04-02 20:31:10` | `cowrie.client.version` |
| `2026-04-02 20:31:10` | `cowrie.client.kex` |
| `2026-04-02 20:31:11` | `cowrie.login.success` |
| `2026-04-02 20:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `110.37.55[.]23` | **18** | 2026-04-02 19:28 | 2026-04-02 19:32 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.122[.]90` | **2** | 2026-04-02 19:35 | 2026-04-02 19:44 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.36.108[.]125` | 1 | 2026-04-02 20:31 | 2026-04-02 20:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.219.33[.]118` | 1 | 2026-04-02 19:39 | 2026-04-02 19:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.171.127[.]190` | 1 | 2026-04-02 19:19 | 2026-04-02 19:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.175[.]69` | 1 | 2026-04-02 19:39 | 2026-04-02 19:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.206[.]119` | 1 | 2026-04-02 18:59 | 2026-04-02 18:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `151.48.206[.]71` | 1 | 2026-04-02 19:20 | 2026-04-02 19:21 | 14s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-04-02 19:08 | 2026-04-02 19:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.94.236[.]211` | 1 | 2026-04-02 18:53 | 2026-04-02 18:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-04-02 18:58 | 2026-04-02 19:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]79` | 1 | 2026-04-02 19:26 | 2026-04-02 19:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.47[.]32` | 1 | 2026-04-02 19:44 | 2026-04-02 19:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.2.228[.]48` | 1 | 2026-04-02 20:03 | 2026-04-02 20:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.179.80[.]12` | 1 | 2026-04-02 19:53 | 2026-04-02 19:53 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.189.253[.]198` | 1 | 2026-04-02 20:13 | 2026-04-02 20:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.75.185[.]101` | 1 | 2026-04-02 19:14 | 2026-04-02 19:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.93.154[.]207` | 1 | 2026-04-02 20:21 | 2026-04-02 20:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.225.176[.]238` | 1 | 2026-04-02 20:28 | 2026-04-02 20:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.145.181[.]7` | 1 | 2026-04-02 19:58 | 2026-04-02 19:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.64.153[.]64` | 1 | 2026-04-02 18:54 | 2026-04-02 18:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.102.148[.]242` | 1 | 2026-04-02 19:33 | 2026-04-02 19:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `24.75.185[.]101` | CA | Cogeco Connexion inc | **100** ⚠️ | 9 |
| `151.48.206[.]71` | IT | WIND Telecomunicazioni S.p.A | **100** ⚠️ | 0 |
| `186.179.80[.]12` | CL | TELEFÓNICA CHILE S.A. (MAYORISTAS) | **100** ⚠️ | 42 |
| `192.42.116[.]94` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `61.145.181[.]7` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 50 |
| `109.219.33[.]118` | FR | Orange S.A. | **100** ⚠️ | 11 |
| `36.93.154[.]207` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 47 |
| `120.48.175[.]69` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `156.238.86[.]2` | PK | SB Link Network Private Limited | **100** ⚠️ | 42 |
| `220.189.253[.]198` | CN | Zhejiang Hangwan Automobile SPAREPARTS ENTERPRISE CO.,LTD | **100** ⚠️ | 28 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 24 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (38.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 22 recon entry/entries in table (2 group(s) consolidating 20 session(s)).

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
_Report time: 2026-04-02T20:33:56Z_
