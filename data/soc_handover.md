# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-23 |
| **Generated At** | 2026-06-23T11:21:59Z |
| **Shift Time** | 11:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **149** |
| Confirmed Threats | **119** |
| False Positives Filtered | **30** (20.1%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **13** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **138** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **37** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **19** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 5 |
| `default` | 2 |
| `support` | 2 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `p@ssw0rd` | 2 |
| `qwerty1234` | 1 |
| `root2009` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `ahmed` | `p@ssw0rd` | 2 |
| `default` | `qwerty1234` | 1 |
| `root` | `root2009` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root2009` | `149.54.15.162` | 2026-06-23T09:12:00 |
| `root` | `Pass.123` | `203.66.168.131` | 2026-06-23T10:32:19 |
| `root` | `3245gs5662d34` | `203.66.168.131` | 2026-06-23T10:32:25 |
| `root` | `Smoker666` | `181.115.147.5` | 2026-06-23T11:08:04 |
| `root` | `3245gs5662d34` | `181.115.147.5` | 2026-06-23T11:08:12 |
| `root` | `Alibaba123` | `103.181.142.22` | 2026-06-23T11:17:59 |
| `root` | `3245gs5662d34` | `103.181.142.22` | 2026-06-23T11:18:04 |
| `root` | `Comtom@2024` | `103.181.142.22` | 2026-06-23T11:18:53 |
| `root` | `Cn123456` | `103.181.142.22` | 2026-06-23T11:19:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **149** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 33 |
| OpenSSH | 8 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 32 | 7 |
| `acaa53e0a7d7...` | Mirai/variant | 8 | 8 |
| `8c95e28f1643...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 32 | 7 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 8 | 8 | Mirai/variant |
| `8c95e28f1643...` | libssh | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.181.142.22`, `203.66.168.131`, `181.115.147.5`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **28** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS33582` | Digicel St.Lucia Ltd | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b8a7f6386f85

| Field | Detail |
|---|---|
| **Source IP** | `149.54.15[.]162` |
| **First Seen** | 2026-06-23 09:11 |
| **Last Seen** | 2026-06-23 09:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 09:11:58` | `cowrie.session.connect` |
| `2026-06-23 09:11:59` | `cowrie.client.version` |
| `2026-06-23 09:11:59` | `cowrie.client.kex` |
| `2026-06-23 09:12:00` | `cowrie.login.success` |
| `2026-06-23 09:12:01` | `cowrie.direct-tcpip.request` |
| `2026-06-23 09:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.54.15[.]162` to AbuseIPDB if not already reported
- [ ] Block `149.54.15[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ad56dfcfbb

| Field | Detail |
|---|---|
| **Source IP** | `203.66.168[.]131` |
| **First Seen** | 2026-06-23 10:32 |
| **Last Seen** | 2026-06-23 10:32 |
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
| `2026-06-23 10:32:18` | `cowrie.session.connect` |
| `2026-06-23 10:32:18` | `cowrie.client.version` |
| `2026-06-23 10:32:18` | `cowrie.client.kex` |
| `2026-06-23 10:32:19` | `cowrie.login.success` |
| `2026-06-23 10:32:20` | `cowrie.session.params` |
| `2026-06-23 10:32:20` | `cowrie.command.input` |
| `2026-06-23 10:32:20` | `cowrie.command.failed` |
| `2026-06-23 10:32:20` | `cowrie.log.closed` |
| `2026-06-23 10:32:21` | `cowrie.session.params` |
| `2026-06-23 10:32:21` | `cowrie.command.input` |
| `2026-06-23 10:32:21` | `cowrie.session.file_download` |
| `2026-06-23 10:32:21` | `cowrie.log.closed` |
| `2026-06-23 10:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.66.168[.]131` to AbuseIPDB if not already reported
- [ ] Block `203.66.168[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe0ecadb11e

| Field | Detail |
|---|---|
| **Source IP** | `203.66.168[.]131` |
| **First Seen** | 2026-06-23 10:32 |
| **Last Seen** | 2026-06-23 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 10:32:24` | `cowrie.session.connect` |
| `2026-06-23 10:32:24` | `cowrie.client.version` |
| `2026-06-23 10:32:24` | `cowrie.client.kex` |
| `2026-06-23 10:32:25` | `cowrie.login.success` |
| `2026-06-23 10:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.66.168[.]131` to AbuseIPDB if not already reported
- [ ] Block `203.66.168[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e3bd163985

| Field | Detail |
|---|---|
| **Source IP** | `181.115.147[.]5` |
| **First Seen** | 2026-06-23 11:08 |
| **Last Seen** | 2026-06-23 11:08 |
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
| `2026-06-23 11:08:02` | `cowrie.session.connect` |
| `2026-06-23 11:08:02` | `cowrie.client.version` |
| `2026-06-23 11:08:03` | `cowrie.client.kex` |
| `2026-06-23 11:08:04` | `cowrie.login.success` |
| `2026-06-23 11:08:05` | `cowrie.session.params` |
| `2026-06-23 11:08:05` | `cowrie.command.input` |
| `2026-06-23 11:08:05` | `cowrie.command.failed` |
| `2026-06-23 11:08:06` | `cowrie.log.closed` |
| `2026-06-23 11:08:06` | `cowrie.session.params` |
| `2026-06-23 11:08:06` | `cowrie.command.input` |
| `2026-06-23 11:08:06` | `cowrie.session.file_download` |
| `2026-06-23 11:08:06` | `cowrie.log.closed` |
| `2026-06-23 11:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.115.147[.]5` to AbuseIPDB if not already reported
- [ ] Block `181.115.147[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-376c61dca8f8

| Field | Detail |
|---|---|
| **Source IP** | `181.115.147[.]5` |
| **First Seen** | 2026-06-23 11:08 |
| **Last Seen** | 2026-06-23 11:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:08:10` | `cowrie.session.connect` |
| `2026-06-23 11:08:10` | `cowrie.client.version` |
| `2026-06-23 11:08:10` | `cowrie.client.kex` |
| `2026-06-23 11:08:12` | `cowrie.login.success` |
| `2026-06-23 11:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.115.147[.]5` to AbuseIPDB if not already reported
- [ ] Block `181.115.147[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199c03f3a0e8

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:17 |
| **Last Seen** | 2026-06-23 11:18 |
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
| `2026-06-23 11:17:58` | `cowrie.session.connect` |
| `2026-06-23 11:17:58` | `cowrie.client.version` |
| `2026-06-23 11:17:58` | `cowrie.client.kex` |
| `2026-06-23 11:17:59` | `cowrie.login.success` |
| `2026-06-23 11:17:59` | `cowrie.session.params` |
| `2026-06-23 11:17:59` | `cowrie.command.input` |
| `2026-06-23 11:17:59` | `cowrie.command.failed` |
| `2026-06-23 11:18:00` | `cowrie.log.closed` |
| `2026-06-23 11:18:00` | `cowrie.session.params` |
| `2026-06-23 11:18:00` | `cowrie.command.input` |
| `2026-06-23 11:18:00` | `cowrie.session.file_download` |
| `2026-06-23 11:18:00` | `cowrie.log.closed` |
| `2026-06-23 11:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9816a2350b

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:18 |
| **Last Seen** | 2026-06-23 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:18:03` | `cowrie.session.connect` |
| `2026-06-23 11:18:03` | `cowrie.client.version` |
| `2026-06-23 11:18:03` | `cowrie.client.kex` |
| `2026-06-23 11:18:04` | `cowrie.login.success` |
| `2026-06-23 11:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2925a72e43

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:18 |
| **Last Seen** | 2026-06-23 11:18 |
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
| `2026-06-23 11:18:52` | `cowrie.session.connect` |
| `2026-06-23 11:18:52` | `cowrie.client.version` |
| `2026-06-23 11:18:52` | `cowrie.client.kex` |
| `2026-06-23 11:18:53` | `cowrie.login.success` |
| `2026-06-23 11:18:53` | `cowrie.session.params` |
| `2026-06-23 11:18:53` | `cowrie.command.input` |
| `2026-06-23 11:18:53` | `cowrie.command.failed` |
| `2026-06-23 11:18:53` | `cowrie.log.closed` |
| `2026-06-23 11:18:54` | `cowrie.session.params` |
| `2026-06-23 11:18:54` | `cowrie.command.input` |
| `2026-06-23 11:18:54` | `cowrie.session.file_download` |
| `2026-06-23 11:18:54` | `cowrie.log.closed` |
| `2026-06-23 11:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811a545596f6

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:18 |
| **Last Seen** | 2026-06-23 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:18:56` | `cowrie.session.connect` |
| `2026-06-23 11:18:56` | `cowrie.client.version` |
| `2026-06-23 11:18:56` | `cowrie.client.kex` |
| `2026-06-23 11:18:57` | `cowrie.login.success` |
| `2026-06-23 11:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaefced3ac57

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:19 |
| **Last Seen** | 2026-06-23 11:19 |
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
| `2026-06-23 11:19:22` | `cowrie.session.connect` |
| `2026-06-23 11:19:22` | `cowrie.client.version` |
| `2026-06-23 11:19:22` | `cowrie.client.kex` |
| `2026-06-23 11:19:23` | `cowrie.login.success` |
| `2026-06-23 11:19:24` | `cowrie.session.params` |
| `2026-06-23 11:19:24` | `cowrie.command.input` |
| `2026-06-23 11:19:24` | `cowrie.command.failed` |
| `2026-06-23 11:19:24` | `cowrie.log.closed` |
| `2026-06-23 11:19:24` | `cowrie.session.params` |
| `2026-06-23 11:19:24` | `cowrie.command.input` |
| `2026-06-23 11:19:25` | `cowrie.session.file_download` |
| `2026-06-23 11:19:25` | `cowrie.log.closed` |
| `2026-06-23 11:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8c5c534d1e

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:19 |
| **Last Seen** | 2026-06-23 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:19:27` | `cowrie.session.connect` |
| `2026-06-23 11:19:27` | `cowrie.client.version` |
| `2026-06-23 11:19:27` | `cowrie.client.kex` |
| `2026-06-23 11:19:28` | `cowrie.login.success` |
| `2026-06-23 11:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `135.148.33[.]168` | **58** | 2026-06-23 07:52 | 2026-06-23 11:17 | 42m | 0 | `T1592` | 🟠 MEDIUM |
| `203.66.168[.]131` | **8** | 2026-06-23 10:30 | 2026-06-23 10:49 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `103.181.142[.]22` | **7** | 2026-06-23 10:57 | 2026-06-23 11:20 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `46.32.228[.]2` | **6** | 2026-06-23 08:42 | 2026-06-23 09:40 | 5m | 0 | `T1592` | 🟢 LOW |
| `202.165.29[.]123` | **3** | 2026-06-23 11:00 | 2026-06-23 11:09 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `206.81.2[.]201` | **3** | 2026-06-23 09:53 | 2026-06-23 10:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-06-23 08:03 | 2026-06-23 08:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-06-23 11:11 | 2026-06-23 11:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.235.192[.]214` | 1 | 2026-06-23 11:05 | 2026-06-23 11:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.13.5[.]26` | 1 | 2026-06-23 10:44 | 2026-06-23 10:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.191.83[.]250` | 1 | 2026-06-23 09:22 | 2026-06-23 09:24 | 93s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-06-23 08:38 | 2026-06-23 08:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.66.28[.]132` | 1 | 2026-06-23 11:02 | 2026-06-23 11:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.12.182[.]123` | 1 | 2026-06-23 08:46 | 2026-06-23 08:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.206.1[.]60` | 1 | 2026-06-23 11:10 | 2026-06-23 11:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.227[.]77` | 1 | 2026-06-23 10:41 | 2026-06-23 10:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.114.66[.]105` | 1 | 2026-06-23 09:45 | 2026-06-23 09:45 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.115.147[.]5` | 1 | 2026-06-23 11:08 | 2026-06-23 11:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.134.25[.]203` | 1 | 2026-06-23 10:11 | 2026-06-23 10:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.199.172[.]66` | 1 | 2026-06-23 10:15 | 2026-06-23 10:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.112.46[.]78` | 1 | 2026-06-23 10:32 | 2026-06-23 10:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `36.212.31[.]122` | 1 | 2026-06-23 08:04 | 2026-06-23 08:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `4.227.177[.]11` | 1 | 2026-06-23 10:59 | 2026-06-23 10:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]146` | 1 | 2026-06-23 09:46 | 2026-06-23 09:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]252` | 1 | 2026-06-23 08:46 | 2026-06-23 08:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.145.163[.]164` | 1 | 2026-06-23 08:17 | 2026-06-23 08:18 | 89s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]197` | 1 | 2026-06-23 09:01 | 2026-06-23 09:01 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/73** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/73 ✅ |
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
| `46.32.228[.]2` | GB | Heart Internet Ltd | **100** ⚠️ | 2 |
| `49.124.152[.]252` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 40 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `181.114.66[.]105` | BO | Comteco Ltda | **100** ⚠️ | 6 |
| `4.227.177[.]11` | US | Microsoft Corporation | **100** ⚠️ | 27 |
| `181.115.147[.]5` | BO | Entel S.A. - EntelNet | **100** ⚠️ | 50 |
| `154.12.182[.]123` | HK | DMIT Cloud Services | **100** ⚠️ | 9 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 9 |
| `1.235.192[.]214` | KR | SK Broadband Co Ltd | **100** ⚠️ | 37 |
| `179.185.227[.]77` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 45 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 25 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 149 cases |
| Tool 34  | Credential Extractor        | ✅ 37 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (20.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 27 recon entry/entries in table (8 group(s) consolidating 89 session(s)).

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
_Report time: 2026-06-23T11:21:59Z_
