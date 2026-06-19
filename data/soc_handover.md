# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-19 |
| **Generated At** | 2026-06-19T21:13:47Z |
| **Shift Time** | 21:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **70** |
| False Positives Filtered | **8** (10.3%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **13** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **7** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `ubuntu` | 2 |
| `345gs5662d34` | 2 |
| `support` | 2 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `1234` | 1 |
| `Root123123` | 1 |
| `will` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `admin` | `1234` | 1 |
| `root` | `Root123123` | 1 |
| `will` | `will` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root123123` | `180.184.52.206` | 2026-06-19T18:57:32 |
| `root` | `!Q2w3e4r5t6y` | `87.106.44.172` | 2026-06-19T19:24:15 |
| `root` | `3245gs5662d34` | `87.106.44.172` | 2026-06-19T19:24:19 |
| `root` | `Root123-` | `202.51.214.99` | 2026-06-19T20:24:53 |
| `root` | `3245gs5662d34` | `202.51.214.99` | 2026-06-19T20:24:56 |
| `root` | `admin` | `192.42.116.56` | 2026-06-19T20:52:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **78** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 13 |
| OpenSSH | 3 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 9 | 5 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 2 | 2 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 9 | 5 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `180.184.52.206`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `87.106.44.172`, `202.51.214.99`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **23** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS398705` | Censys, Inc. | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS8560` | IONOS SE | 1 | HIGH |
| `AS9694` | Seokyung Cable Television Co.. Ltd. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-965811be6aa4

| Field | Detail |
|---|---|
| **Source IP** | `180.184.52[.]206` |
| **First Seen** | 2026-06-19 18:57 |
| **Last Seen** | 2026-06-19 19:02 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 18:57:31` | `cowrie.session.connect` |
| `2026-06-19 18:57:31` | `cowrie.client.version` |
| `2026-06-19 18:57:31` | `cowrie.client.kex` |
| `2026-06-19 18:57:32` | `cowrie.login.success` |
| `2026-06-19 18:57:33` | `cowrie.session.params` |
| `2026-06-19 18:57:33` | `cowrie.command.input` |
| `2026-06-19 18:57:33` | `cowrie.command.failed` |
| `2026-06-19 18:57:33` | `cowrie.log.closed` |
| `2026-06-19 18:57:33` | `cowrie.session.params` |
| `2026-06-19 18:57:33` | `cowrie.command.input` |
| `2026-06-19 18:57:33` | `cowrie.session.file_download` |
| `2026-06-19 18:57:33` | `cowrie.log.closed` |
| `2026-06-19 18:57:51` | `cowrie.session.params` |
| `2026-06-19 18:57:51` | `cowrie.command.input` |
| `2026-06-19 19:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.52[.]206` to AbuseIPDB if not already reported
- [ ] Block `180.184.52[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea3f55a8477

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-06-19 19:24 |
| **Last Seen** | 2026-06-19 19:24 |
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
| `2026-06-19 19:24:14` | `cowrie.session.connect` |
| `2026-06-19 19:24:14` | `cowrie.client.version` |
| `2026-06-19 19:24:14` | `cowrie.client.kex` |
| `2026-06-19 19:24:15` | `cowrie.login.success` |
| `2026-06-19 19:24:15` | `cowrie.session.params` |
| `2026-06-19 19:24:15` | `cowrie.command.input` |
| `2026-06-19 19:24:15` | `cowrie.command.failed` |
| `2026-06-19 19:24:15` | `cowrie.log.closed` |
| `2026-06-19 19:24:16` | `cowrie.session.params` |
| `2026-06-19 19:24:16` | `cowrie.command.input` |
| `2026-06-19 19:24:16` | `cowrie.session.file_download` |
| `2026-06-19 19:24:16` | `cowrie.log.closed` |
| `2026-06-19 19:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfdce8d812b1

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-06-19 19:24 |
| **Last Seen** | 2026-06-19 19:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 19:24:18` | `cowrie.session.connect` |
| `2026-06-19 19:24:18` | `cowrie.client.version` |
| `2026-06-19 19:24:18` | `cowrie.client.kex` |
| `2026-06-19 19:24:19` | `cowrie.login.success` |
| `2026-06-19 19:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1294c2d0cf

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]99` |
| **First Seen** | 2026-06-19 20:24 |
| **Last Seen** | 2026-06-19 20:24 |
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
| `2026-06-19 20:24:53` | `cowrie.session.connect` |
| `2026-06-19 20:24:53` | `cowrie.client.version` |
| `2026-06-19 20:24:53` | `cowrie.client.kex` |
| `2026-06-19 20:24:53` | `cowrie.login.success` |
| `2026-06-19 20:24:53` | `cowrie.session.params` |
| `2026-06-19 20:24:53` | `cowrie.command.input` |
| `2026-06-19 20:24:53` | `cowrie.command.failed` |
| `2026-06-19 20:24:54` | `cowrie.log.closed` |
| `2026-06-19 20:24:54` | `cowrie.session.params` |
| `2026-06-19 20:24:54` | `cowrie.command.input` |
| `2026-06-19 20:24:54` | `cowrie.session.file_download` |
| `2026-06-19 20:24:54` | `cowrie.log.closed` |
| `2026-06-19 20:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]99` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ab7dbef7dc

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]99` |
| **First Seen** | 2026-06-19 20:24 |
| **Last Seen** | 2026-06-19 20:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 20:24:55` | `cowrie.session.connect` |
| `2026-06-19 20:24:55` | `cowrie.client.version` |
| `2026-06-19 20:24:55` | `cowrie.client.kex` |
| `2026-06-19 20:24:56` | `cowrie.login.success` |
| `2026-06-19 20:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]99` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a8424b484b

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]56` |
| **First Seen** | 2026-06-19 20:52 |
| **Last Seen** | 2026-06-19 20:53 |
| **Session Duration** | 25s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 20:52:54` | `cowrie.session.connect` |
| `2026-06-19 20:52:54` | `cowrie.client.version` |
| `2026-06-19 20:52:54` | `cowrie.client.kex` |
| `2026-06-19 20:52:56` | `cowrie.client.fingerprint` |
| `2026-06-19 20:52:56` | `cowrie.login.failed` |
| `2026-06-19 20:52:56` | `cowrie.login.success` |
| `2026-06-19 20:53:18` | `cowrie.direct-tcpip.request` |
| `2026-06-19 20:53:18` | `cowrie.direct-tcpip.ja4` |
| `2026-06-19 20:53:18` | `cowrie.direct-tcpip.data` |
| `2026-06-19 20:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]56` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.241[.]3` | **14** | 2026-06-19 18:13 | 2026-06-19 20:51 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `175.170.144[.]19` | **13** | 2026-06-19 19:32 | 2026-06-19 19:55 | 22m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `216.144.229[.]11` | **13** | 2026-06-19 18:10 | 2026-06-19 20:24 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `175.170.144[.]17` | **8** | 2026-06-19 20:03 | 2026-06-19 20:13 | 16m | 0 | `T1592` | 🟢 LOW |
| `157.15.78[.]122` | **2** | 2026-06-19 18:14 | 2026-06-19 18:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.52[.]206` | **2** | 2026-06-19 18:57 | 2026-06-19 18:59 | 4m | 0 | `T1592` | 🟢 LOW |
| `115.160.15[.]55` | 1 | 2026-06-19 18:09 | 2026-06-19 18:09 | 14s | 0 | `T1592` | 🟢 LOW |
| `117.205.2[.]250` | 1 | 2026-06-19 19:53 | 2026-06-19 19:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.28.201[.]217` | 1 | 2026-06-19 18:40 | 2026-06-19 18:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.189.226[.]81` | 1 | 2026-06-19 21:05 | 2026-06-19 21:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.106.80[.]16` | 1 | 2026-06-19 18:01 | 2026-06-19 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.42.113[.]10` | 1 | 2026-06-19 18:40 | 2026-06-19 18:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.193.240[.]246` | 1 | 2026-06-19 19:06 | 2026-06-19 19:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.221.50[.]123` | 1 | 2026-06-19 20:27 | 2026-06-19 20:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.51.214[.]99` | 1 | 2026-06-19 20:24 | 2026-06-19 20:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.124.177[.]148` | 1 | 2026-06-19 19:03 | 2026-06-19 19:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.222.178[.]0` | 1 | 2026-06-19 20:33 | 2026-06-19 20:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `87.106.44[.]172` | 1 | 2026-06-19 19:24 | 2026-06-19 19:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `134.209.241[.]3` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `175.170.144[.]19` | CN | CHINA UNICOM Liaoning province network | **100** ⚠️ | 27 |
| `157.15.78[.]122` | ID | PT Box Net Media | **100** ⚠️ | 2 |
| `117.205.2[.]250` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 22 |
| `115.160.15[.]55` | KR | Seokyung Cable Television Co.. Ltd. | **100** ⚠️ | 2 |
| `120.28.201[.]217` | PH | GBB VISAYAS | **100** ⚠️ | 13 |
| `222.124.177[.]148` | ID | PT. TELEKOMUNIKASI INDONESIA | **100** ⚠️ | 50 |
| `190.221.50[.]123` | AR | AGUAS RIOJANAS S.A.P.E.M | **100** ⚠️ | 50 |
| `192.42.116[.]56` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `202.51.214[.]99` | ID | PT Kreasi Sejahtera Teknologi | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (10.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 18 recon entry/entries in table (6 group(s) consolidating 52 session(s)).

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
_Report time: 2026-06-19T21:13:47Z_
