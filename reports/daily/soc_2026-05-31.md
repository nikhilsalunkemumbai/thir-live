# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-31 |
| **Generated At** | 2026-05-31T17:11:03Z |
| **Shift Time** | 17:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **205** |
| Confirmed Threats | **196** |
| False Positives Filtered | **9** (4.4%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **10** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **184** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **45** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **14** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 10 |
| `deploy` | 1 |
| `simon` | 1 |
| `prueba` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `` | 2 |
| `abc123` | 1 |
| `simon123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `` | 2 |
| `deploy` | `abc123` | 1 |
| `simon` | `simon123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zh123456.` | `34.135.200.178` | 2026-05-31T16:15:53 |
| `root` | `3245gs5662d34` | `34.135.200.178` | 2026-05-31T16:15:59 |
| `root` | `p@s5w0rd` | `34.135.200.178` | 2026-05-31T16:17:26 |
| `root` | `6yhn^YHN` | `34.135.200.178` | 2026-05-31T16:18:54 |
| `root` | `Aa654321` | `101.126.54.95` | 2026-05-31T16:19:24 |
| `root` | `3245gs5662d34` | `101.126.54.95` | 2026-05-31T16:19:29 |
| `root` | `L@y3rh0st2024` | `101.126.54.95` | 2026-05-31T16:20:05 |
| `root` | `v` | `101.126.54.95` | 2026-05-31T16:20:47 |
| `root` | `Qwer!1234` | `34.135.200.178` | 2026-05-31T16:23:13 |
| `root` | `Yh@123456` | `14.103.114.244` | 2026-05-31T16:24:01 |
| `root` | `1234@qwer` | `34.135.200.178` | 2026-05-31T16:27:24 |
| `root` | `a.123456` | `34.135.200.178` | 2026-05-31T16:28:50 |
| `root` | `Abcd.2025` | `34.135.200.178` | 2026-05-31T16:34:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **205** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 62 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 37 | 3 |
| `03a80b21afa8...` | Modern SSH client | 15 | 4 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 37 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 15 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 10 | 3 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:2I9GKqAqcPs4"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.114.244`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.126.54.95`, `34.135.200.178`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **21** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c698440d6d1d

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:15 |
| **Last Seen** | 2026-05-31 16:15 |
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
| `2026-05-31 16:15:52` | `cowrie.session.connect` |
| `2026-05-31 16:15:52` | `cowrie.client.version` |
| `2026-05-31 16:15:52` | `cowrie.client.kex` |
| `2026-05-31 16:15:53` | `cowrie.login.success` |
| `2026-05-31 16:15:54` | `cowrie.session.params` |
| `2026-05-31 16:15:54` | `cowrie.command.input` |
| `2026-05-31 16:15:54` | `cowrie.command.failed` |
| `2026-05-31 16:15:54` | `cowrie.log.closed` |
| `2026-05-31 16:15:55` | `cowrie.session.params` |
| `2026-05-31 16:15:55` | `cowrie.command.input` |
| `2026-05-31 16:15:55` | `cowrie.session.file_download` |
| `2026-05-31 16:15:55` | `cowrie.log.closed` |
| `2026-05-31 16:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b03b5cbce7

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:15 |
| **Last Seen** | 2026-05-31 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:15:58` | `cowrie.session.connect` |
| `2026-05-31 16:15:58` | `cowrie.client.version` |
| `2026-05-31 16:15:58` | `cowrie.client.kex` |
| `2026-05-31 16:15:59` | `cowrie.login.success` |
| `2026-05-31 16:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ddd948ffd9

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:17 |
| **Last Seen** | 2026-05-31 16:17 |
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
| `2026-05-31 16:17:25` | `cowrie.session.connect` |
| `2026-05-31 16:17:25` | `cowrie.client.version` |
| `2026-05-31 16:17:25` | `cowrie.client.kex` |
| `2026-05-31 16:17:26` | `cowrie.login.success` |
| `2026-05-31 16:17:26` | `cowrie.session.params` |
| `2026-05-31 16:17:26` | `cowrie.command.input` |
| `2026-05-31 16:17:26` | `cowrie.command.failed` |
| `2026-05-31 16:17:27` | `cowrie.log.closed` |
| `2026-05-31 16:17:27` | `cowrie.session.params` |
| `2026-05-31 16:17:27` | `cowrie.command.input` |
| `2026-05-31 16:17:27` | `cowrie.session.file_download` |
| `2026-05-31 16:17:27` | `cowrie.log.closed` |
| `2026-05-31 16:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0387f74f383b

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:17 |
| **Last Seen** | 2026-05-31 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:17:30` | `cowrie.session.connect` |
| `2026-05-31 16:17:30` | `cowrie.client.version` |
| `2026-05-31 16:17:30` | `cowrie.client.kex` |
| `2026-05-31 16:17:31` | `cowrie.login.success` |
| `2026-05-31 16:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd907905aec2

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:18 |
| **Last Seen** | 2026-05-31 16:19 |
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
| `2026-05-31 16:18:53` | `cowrie.session.connect` |
| `2026-05-31 16:18:53` | `cowrie.client.version` |
| `2026-05-31 16:18:53` | `cowrie.client.kex` |
| `2026-05-31 16:18:54` | `cowrie.login.success` |
| `2026-05-31 16:18:55` | `cowrie.session.params` |
| `2026-05-31 16:18:55` | `cowrie.command.input` |
| `2026-05-31 16:18:55` | `cowrie.command.failed` |
| `2026-05-31 16:18:55` | `cowrie.log.closed` |
| `2026-05-31 16:18:55` | `cowrie.session.params` |
| `2026-05-31 16:18:55` | `cowrie.command.input` |
| `2026-05-31 16:18:56` | `cowrie.session.file_download` |
| `2026-05-31 16:18:56` | `cowrie.log.closed` |
| `2026-05-31 16:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc3c9633873

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:18 |
| **Last Seen** | 2026-05-31 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:18:58` | `cowrie.session.connect` |
| `2026-05-31 16:18:58` | `cowrie.client.version` |
| `2026-05-31 16:18:59` | `cowrie.client.kex` |
| `2026-05-31 16:19:00` | `cowrie.login.success` |
| `2026-05-31 16:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8478e88be76

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-05-31 16:19 |
| **Last Seen** | 2026-05-31 16:19 |
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
| `2026-05-31 16:19:23` | `cowrie.session.connect` |
| `2026-05-31 16:19:23` | `cowrie.client.version` |
| `2026-05-31 16:19:24` | `cowrie.client.kex` |
| `2026-05-31 16:19:24` | `cowrie.login.success` |
| `2026-05-31 16:19:25` | `cowrie.session.params` |
| `2026-05-31 16:19:25` | `cowrie.command.input` |
| `2026-05-31 16:19:25` | `cowrie.command.failed` |
| `2026-05-31 16:19:25` | `cowrie.log.closed` |
| `2026-05-31 16:19:25` | `cowrie.session.params` |
| `2026-05-31 16:19:25` | `cowrie.command.input` |
| `2026-05-31 16:19:25` | `cowrie.session.file_download` |
| `2026-05-31 16:19:25` | `cowrie.log.closed` |
| `2026-05-31 16:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c9ddecbdd5

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-05-31 16:19 |
| **Last Seen** | 2026-05-31 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:19:27` | `cowrie.session.connect` |
| `2026-05-31 16:19:27` | `cowrie.client.version` |
| `2026-05-31 16:19:28` | `cowrie.client.kex` |
| `2026-05-31 16:19:29` | `cowrie.login.success` |
| `2026-05-31 16:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5a0ce68121

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-05-31 16:20 |
| **Last Seen** | 2026-05-31 16:20 |
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
| `2026-05-31 16:20:04` | `cowrie.session.connect` |
| `2026-05-31 16:20:04` | `cowrie.client.version` |
| `2026-05-31 16:20:04` | `cowrie.client.kex` |
| `2026-05-31 16:20:05` | `cowrie.login.success` |
| `2026-05-31 16:20:05` | `cowrie.session.params` |
| `2026-05-31 16:20:05` | `cowrie.command.input` |
| `2026-05-31 16:20:05` | `cowrie.command.failed` |
| `2026-05-31 16:20:06` | `cowrie.log.closed` |
| `2026-05-31 16:20:06` | `cowrie.session.params` |
| `2026-05-31 16:20:06` | `cowrie.command.input` |
| `2026-05-31 16:20:06` | `cowrie.session.file_download` |
| `2026-05-31 16:20:06` | `cowrie.log.closed` |
| `2026-05-31 16:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe696828184

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-05-31 16:20 |
| **Last Seen** | 2026-05-31 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:20:10` | `cowrie.session.connect` |
| `2026-05-31 16:20:10` | `cowrie.client.version` |
| `2026-05-31 16:20:10` | `cowrie.client.kex` |
| `2026-05-31 16:20:11` | `cowrie.login.success` |
| `2026-05-31 16:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0677ecd0bdbc

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-05-31 16:20 |
| **Last Seen** | 2026-05-31 16:20 |
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
| `2026-05-31 16:20:46` | `cowrie.session.connect` |
| `2026-05-31 16:20:46` | `cowrie.client.version` |
| `2026-05-31 16:20:46` | `cowrie.client.kex` |
| `2026-05-31 16:20:47` | `cowrie.login.success` |
| `2026-05-31 16:20:48` | `cowrie.session.params` |
| `2026-05-31 16:20:48` | `cowrie.command.input` |
| `2026-05-31 16:20:48` | `cowrie.command.failed` |
| `2026-05-31 16:20:48` | `cowrie.log.closed` |
| `2026-05-31 16:20:48` | `cowrie.session.params` |
| `2026-05-31 16:20:48` | `cowrie.command.input` |
| `2026-05-31 16:20:48` | `cowrie.session.file_download` |
| `2026-05-31 16:20:48` | `cowrie.log.closed` |
| `2026-05-31 16:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc790636ef46

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-05-31 16:20 |
| **Last Seen** | 2026-05-31 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:20:53` | `cowrie.session.connect` |
| `2026-05-31 16:20:53` | `cowrie.client.version` |
| `2026-05-31 16:20:53` | `cowrie.client.kex` |
| `2026-05-31 16:20:53` | `cowrie.login.success` |
| `2026-05-31 16:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2df9553f1f

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:23 |
| **Last Seen** | 2026-05-31 16:23 |
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
| `2026-05-31 16:23:11` | `cowrie.session.connect` |
| `2026-05-31 16:23:11` | `cowrie.client.version` |
| `2026-05-31 16:23:12` | `cowrie.client.kex` |
| `2026-05-31 16:23:13` | `cowrie.login.success` |
| `2026-05-31 16:23:13` | `cowrie.session.params` |
| `2026-05-31 16:23:13` | `cowrie.command.input` |
| `2026-05-31 16:23:13` | `cowrie.command.failed` |
| `2026-05-31 16:23:14` | `cowrie.log.closed` |
| `2026-05-31 16:23:14` | `cowrie.session.params` |
| `2026-05-31 16:23:14` | `cowrie.command.input` |
| `2026-05-31 16:23:14` | `cowrie.session.file_download` |
| `2026-05-31 16:23:14` | `cowrie.log.closed` |
| `2026-05-31 16:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342bf5175fcd

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:23 |
| **Last Seen** | 2026-05-31 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:23:17` | `cowrie.session.connect` |
| `2026-05-31 16:23:17` | `cowrie.client.version` |
| `2026-05-31 16:23:17` | `cowrie.client.kex` |
| `2026-05-31 16:23:18` | `cowrie.login.success` |
| `2026-05-31 16:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99842bdd4248

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-05-31 16:23 |
| **Last Seen** | 2026-05-31 16:24 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2I9GKqAqcPs4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:23:59` | `cowrie.session.connect` |
| `2026-05-31 16:23:59` | `cowrie.client.version` |
| `2026-05-31 16:24:00` | `cowrie.client.kex` |
| `2026-05-31 16:24:01` | `cowrie.login.success` |
| `2026-05-31 16:24:01` | `cowrie.session.params` |
| `2026-05-31 16:24:01` | `cowrie.command.input` |
| `2026-05-31 16:24:01` | `cowrie.command.failed` |
| `2026-05-31 16:24:01` | `cowrie.log.closed` |
| `2026-05-31 16:24:01` | `cowrie.session.params` |
| `2026-05-31 16:24:01` | `cowrie.command.input` |
| `2026-05-31 16:24:02` | `cowrie.session.file_download` |
| `2026-05-31 16:24:02` | `cowrie.log.closed` |
| `2026-05-31 16:24:18` | `cowrie.session.params` |
| `2026-05-31 16:24:18` | `cowrie.command.input` |
| `2026-05-31 16:24:19` | `cowrie.log.closed` |
| `2026-05-31 16:24:20` | `cowrie.session.params` |
| `2026-05-31 16:24:20` | `cowrie.command.input` |
| `2026-05-31 16:24:20` | `cowrie.log.closed` |
| `2026-05-31 16:24:20` | `cowrie.session.params` |
| `2026-05-31 16:24:20` | `cowrie.command.input` |
| `2026-05-31 16:24:21` | `cowrie.session.file_download` |
| `2026-05-31 16:24:21` | `cowrie.log.closed` |
| `2026-05-31 16:24:21` | `cowrie.session.params` |
| `2026-05-31 16:24:21` | `cowrie.command.input` |
| `2026-05-31 16:24:21` | `cowrie.log.closed` |
| `2026-05-31 16:24:22` | `cowrie.session.params` |
| `2026-05-31 16:24:22` | `cowrie.command.input` |
| `2026-05-31 16:24:22` | `cowrie.log.closed` |
| `2026-05-31 16:24:22` | `cowrie.session.params` |
| `2026-05-31 16:24:22` | `cowrie.command.input` |
| `2026-05-31 16:24:22` | `cowrie.command.input` |
| `2026-05-31 16:24:23` | `cowrie.log.closed` |
| `2026-05-31 16:24:23` | `cowrie.session.params` |
| `2026-05-31 16:24:23` | `cowrie.command.input` |
| `2026-05-31 16:24:24` | `cowrie.log.closed` |
| `2026-05-31 16:24:24` | `cowrie.session.params` |
| `2026-05-31 16:24:24` | `cowrie.command.input` |
| `2026-05-31 16:24:25` | `cowrie.log.closed` |
| `2026-05-31 16:24:25` | `cowrie.session.params` |
| `2026-05-31 16:24:25` | `cowrie.command.input` |
| `2026-05-31 16:24:26` | `cowrie.log.closed` |
| `2026-05-31 16:24:26` | `cowrie.session.params` |
| `2026-05-31 16:24:26` | `cowrie.command.input` |
| `2026-05-31 16:24:26` | `cowrie.log.closed` |
| `2026-05-31 16:24:27` | `cowrie.session.params` |
| `2026-05-31 16:24:27` | `cowrie.command.input` |
| `2026-05-31 16:24:27` | `cowrie.log.closed` |
| `2026-05-31 16:24:27` | `cowrie.session.params` |
| `2026-05-31 16:24:27` | `cowrie.command.input` |
| `2026-05-31 16:24:27` | `cowrie.log.closed` |
| `2026-05-31 16:24:27` | `cowrie.session.params` |
| `2026-05-31 16:24:27` | `cowrie.command.input` |
| `2026-05-31 16:24:28` | `cowrie.log.closed` |
| `2026-05-31 16:24:28` | `cowrie.session.params` |
| `2026-05-31 16:24:28` | `cowrie.command.input` |
| `2026-05-31 16:24:29` | `cowrie.log.closed` |
| `2026-05-31 16:24:29` | `cowrie.session.params` |
| `2026-05-31 16:24:29` | `cowrie.command.input` |
| `2026-05-31 16:24:29` | `cowrie.log.closed` |
| `2026-05-31 16:24:29` | `cowrie.session.params` |
| `2026-05-31 16:24:29` | `cowrie.command.input` |
| `2026-05-31 16:24:29` | `cowrie.log.closed` |
| `2026-05-31 16:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-175784cc2b61

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:27 |
| **Last Seen** | 2026-05-31 16:27 |
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
| `2026-05-31 16:27:23` | `cowrie.session.connect` |
| `2026-05-31 16:27:23` | `cowrie.client.version` |
| `2026-05-31 16:27:23` | `cowrie.client.kex` |
| `2026-05-31 16:27:24` | `cowrie.login.success` |
| `2026-05-31 16:27:25` | `cowrie.session.params` |
| `2026-05-31 16:27:25` | `cowrie.command.input` |
| `2026-05-31 16:27:25` | `cowrie.command.failed` |
| `2026-05-31 16:27:25` | `cowrie.log.closed` |
| `2026-05-31 16:27:26` | `cowrie.session.params` |
| `2026-05-31 16:27:26` | `cowrie.command.input` |
| `2026-05-31 16:27:26` | `cowrie.session.file_download` |
| `2026-05-31 16:27:26` | `cowrie.log.closed` |
| `2026-05-31 16:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3042fcfa293

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:27 |
| **Last Seen** | 2026-05-31 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:27:29` | `cowrie.session.connect` |
| `2026-05-31 16:27:29` | `cowrie.client.version` |
| `2026-05-31 16:27:29` | `cowrie.client.kex` |
| `2026-05-31 16:27:30` | `cowrie.login.success` |
| `2026-05-31 16:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb005fed410

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:28 |
| **Last Seen** | 2026-05-31 16:28 |
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
| `2026-05-31 16:28:49` | `cowrie.session.connect` |
| `2026-05-31 16:28:49` | `cowrie.client.version` |
| `2026-05-31 16:28:49` | `cowrie.client.kex` |
| `2026-05-31 16:28:50` | `cowrie.login.success` |
| `2026-05-31 16:28:51` | `cowrie.session.params` |
| `2026-05-31 16:28:51` | `cowrie.command.input` |
| `2026-05-31 16:28:51` | `cowrie.command.failed` |
| `2026-05-31 16:28:51` | `cowrie.log.closed` |
| `2026-05-31 16:28:52` | `cowrie.session.params` |
| `2026-05-31 16:28:52` | `cowrie.command.input` |
| `2026-05-31 16:28:52` | `cowrie.session.file_download` |
| `2026-05-31 16:28:52` | `cowrie.log.closed` |
| `2026-05-31 16:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f723542b181c

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:28 |
| **Last Seen** | 2026-05-31 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:28:55` | `cowrie.session.connect` |
| `2026-05-31 16:28:55` | `cowrie.client.version` |
| `2026-05-31 16:28:55` | `cowrie.client.kex` |
| `2026-05-31 16:28:56` | `cowrie.login.success` |
| `2026-05-31 16:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7bc5fd537b

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:34 |
| **Last Seen** | 2026-05-31 16:34 |
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
| `2026-05-31 16:34:42` | `cowrie.session.connect` |
| `2026-05-31 16:34:42` | `cowrie.client.version` |
| `2026-05-31 16:34:42` | `cowrie.client.kex` |
| `2026-05-31 16:34:43` | `cowrie.login.success` |
| `2026-05-31 16:34:44` | `cowrie.session.params` |
| `2026-05-31 16:34:44` | `cowrie.command.input` |
| `2026-05-31 16:34:44` | `cowrie.command.failed` |
| `2026-05-31 16:34:44` | `cowrie.log.closed` |
| `2026-05-31 16:34:44` | `cowrie.session.params` |
| `2026-05-31 16:34:44` | `cowrie.command.input` |
| `2026-05-31 16:34:45` | `cowrie.session.file_download` |
| `2026-05-31 16:34:45` | `cowrie.log.closed` |
| `2026-05-31 16:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e31fd8fd60

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-31 16:34 |
| **Last Seen** | 2026-05-31 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 16:34:48` | `cowrie.session.connect` |
| `2026-05-31 16:34:48` | `cowrie.client.version` |
| `2026-05-31 16:34:48` | `cowrie.client.kex` |
| `2026-05-31 16:34:49` | `cowrie.login.success` |
| `2026-05-31 16:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `187.108.193[.]54` | **59** | 2026-05-31 15:21 | 2026-05-31 17:09 | 36m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.125[.]12` | **25** | 2026-05-31 16:57 | 2026-05-31 17:03 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `159.203.20[.]239` | **24** | 2026-05-31 15:34 | 2026-05-31 17:06 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `34.135.200[.]178` | **15** | 2026-05-31 16:06 | 2026-05-31 16:34 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.114[.]244` | **14** | 2026-05-31 16:08 | 2026-05-31 16:38 | 18m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.54[.]95` | **12** | 2026-05-31 16:13 | 2026-05-31 16:24 | 14m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `110.166.87[.]119` | **6** | 2026-05-31 16:48 | 2026-05-31 17:02 | 6m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.76.38[.]124` | **3** | 2026-05-31 17:08 | 2026-05-31 17:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]38` | **3** | 2026-05-31 16:56 | 2026-05-31 16:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | **2** | 2026-05-31 15:43 | 2026-05-31 15:50 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.163.16[.]228` | **2** | 2026-05-31 16:47 | 2026-05-31 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.227.75[.]197` | 1 | 2026-05-31 16:07 | 2026-05-31 16:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-31 15:50 | 2026-05-31 15:50 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.122[.]187` | 1 | 2026-05-31 16:53 | 2026-05-31 16:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.46[.]139` | 1 | 2026-05-31 15:45 | 2026-05-31 15:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.52[.]206` | 1 | 2026-05-31 16:51 | 2026-05-31 16:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-05-31 16:14 | 2026-05-31 16:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.235[.]157` | 1 | 2026-05-31 16:18 | 2026-05-31 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `199.223.115[.]56` | 1 | 2026-05-31 15:45 | 2026-05-31 15:46 | 30s | 0 | `T1592` | 🟢 LOW |
| `203.189.195[.]8` | 1 | 2026-05-31 16:54 | 2026-05-31 16:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `206.189.25[.]100` | 1 | 2026-05-31 16:51 | 2026-05-31 16:53 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `180.76.235[.]157` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 7 |
| `187.108.193[.]54` | BR | EVEO S.A. | **100** ⚠️ | 10 |
| `66.132.172[.]38` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `14.103.46[.]139` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `199.223.115[.]56` | US | InMotion Hosting, Inc. | **100** ⚠️ | 0 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `223.123.125[.]12` | PK | CMPak Limited | **100** ⚠️ | 4 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 205 cases |
| Tool 34  | Credential Extractor        | ✅ 45 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (4.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 21 recon entry/entries in table (11 group(s) consolidating 165 session(s)).

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
_Report time: 2026-05-31T17:11:03Z_
