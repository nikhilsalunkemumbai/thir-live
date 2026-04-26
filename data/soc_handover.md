# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-26 |
| **Generated At** | 2026-04-26T22:43:58Z |
| **Shift Time** | 22:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **153** |
| Confirmed Threats | **75** |
| False Positives Filtered | **78** (51.0%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **13** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **141** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **4** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 4 |
| `admin` | 2 |
| `service` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 4 |
| `P@5sword123` | 1 |
| `service` | 1 |
| `1111` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `P@5sword123` | 1 |
| `service` | `service` | 1 |
| `admin` | `1111` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@5sword123` | `103.63.25.203` | 2026-04-26T21:12:06 |
| `root` | `3245gs5662d34` | `103.63.25.203` | 2026-04-26T21:12:10 |
| `root` | `dreambox` | `82.102.74.238` | 2026-04-26T21:24:33 |
| `root` | `Google12$` | `118.71.20.172` | 2026-04-26T21:35:31 |
| `root` | `3245gs5662d34` | `118.71.20.172` | 2026-04-26T21:35:34 |
| `root` | `miaw11` | `182.253.79.194` | 2026-04-26T21:36:40 |
| `root` | `3245gs5662d34` | `182.253.79.194` | 2026-04-26T21:36:45 |
| `root` | `qaz22` | `119.246.15.94` | 2026-04-26T21:41:43 |
| `root` | `3245gs5662d34` | `119.246.15.94` | 2026-04-26T21:41:48 |
| `root` | `Pa$$word123` | `218.78.59.30` | 2026-04-26T21:42:50 |
| `root` | `3245gs5662d34` | `218.78.59.30` | 2026-04-26T21:43:01 |
| `root` | `------fuck------` | `183.92.151.73` | 2026-04-26T21:55:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **153** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 22 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 15 | 7 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 15 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox WODPD
```
Source IPs: `82.102.74.238`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `119.246.15.94`, `103.63.25.203`, `218.78.59.30`, `118.71.20.172`, `182.253.79.194`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **23** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS21565` | Horry Telephone Cooperative, Inc. | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS16229` | Primetel PLC | 1 | LOW |
| `AS263791` | REFSA TELECOMUNICACIONES | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0a5474e718ca

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-26 21:12 |
| **Last Seen** | 2026-04-26 21:12 |
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
| `2026-04-26 21:12:05` | `cowrie.session.connect` |
| `2026-04-26 21:12:05` | `cowrie.client.version` |
| `2026-04-26 21:12:05` | `cowrie.client.kex` |
| `2026-04-26 21:12:06` | `cowrie.login.success` |
| `2026-04-26 21:12:06` | `cowrie.session.params` |
| `2026-04-26 21:12:06` | `cowrie.command.input` |
| `2026-04-26 21:12:06` | `cowrie.command.failed` |
| `2026-04-26 21:12:06` | `cowrie.log.closed` |
| `2026-04-26 21:12:07` | `cowrie.session.params` |
| `2026-04-26 21:12:07` | `cowrie.command.input` |
| `2026-04-26 21:12:07` | `cowrie.session.file_download` |
| `2026-04-26 21:12:07` | `cowrie.log.closed` |
| `2026-04-26 21:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8467241f44e

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]203` |
| **First Seen** | 2026-04-26 21:12 |
| **Last Seen** | 2026-04-26 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 21:12:09` | `cowrie.session.connect` |
| `2026-04-26 21:12:09` | `cowrie.client.version` |
| `2026-04-26 21:12:09` | `cowrie.client.kex` |
| `2026-04-26 21:12:10` | `cowrie.login.success` |
| `2026-04-26 21:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3208bd9a7d

| Field | Detail |
|---|---|
| **Source IP** | `82.102.74[.]238` |
| **First Seen** | 2026-04-26 21:24 |
| **Last Seen** | 2026-04-26 21:26 |
| **Session Duration** | 103s |
| **Login Attempts** | 3 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox WODPD` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 21:24:31` | `cowrie.session.connect` |
| `2026-04-26 21:24:31` | `cowrie.telnet.option` |
| `2026-04-26 21:24:32` | `cowrie.login.failed` |
| `2026-04-26 21:24:32` | `cowrie.telnet.option` |
| `2026-04-26 21:24:32` | `cowrie.login.failed` |
| `2026-04-26 21:24:32` | `cowrie.telnet.option` |
| `2026-04-26 21:24:33` | `cowrie.login.success` |
| `2026-04-26 21:24:33` | `cowrie.session.params` |
| `2026-04-26 21:24:33` | `cowrie.command.input` |
| `2026-04-26 21:24:33` | `cowrie.command.input` |
| `2026-04-26 21:24:33` | `cowrie.command.failed` |
| `2026-04-26 21:24:33` | `cowrie.command.input` |
| `2026-04-26 21:24:33` | `cowrie.command.failed` |
| `2026-04-26 21:24:33` | `cowrie.command.input` |
| `2026-04-26 21:24:33` | `cowrie.command.input` |
| `2026-04-26 21:24:33` | `cowrie.command.input` |
| `2026-04-26 21:24:33` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.failed` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:34` | `cowrie.command.input` |
| `2026-04-26 21:24:35` | `cowrie.command.input` |
| `2026-04-26 21:24:35` | `cowrie.command.input` |
| `2026-04-26 21:24:35` | `cowrie.command.input` |
| `2026-04-26 21:24:35` | `cowrie.command.input` |
| `2026-04-26 21:24:35` | `cowrie.command.input` |
| `2026-04-26 21:24:35` | `cowrie.command.failed` |
| `2026-04-26 21:26:15` | `cowrie.log.closed` |
| `2026-04-26 21:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.74[.]238` to AbuseIPDB if not already reported
- [ ] Block `82.102.74[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ecefd380cc6

| Field | Detail |
|---|---|
| **Source IP** | `118.71.20[.]172` |
| **First Seen** | 2026-04-26 21:35 |
| **Last Seen** | 2026-04-26 21:35 |
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
| `2026-04-26 21:35:30` | `cowrie.session.connect` |
| `2026-04-26 21:35:30` | `cowrie.client.version` |
| `2026-04-26 21:35:30` | `cowrie.client.kex` |
| `2026-04-26 21:35:31` | `cowrie.login.success` |
| `2026-04-26 21:35:31` | `cowrie.session.params` |
| `2026-04-26 21:35:31` | `cowrie.command.input` |
| `2026-04-26 21:35:31` | `cowrie.command.failed` |
| `2026-04-26 21:35:31` | `cowrie.log.closed` |
| `2026-04-26 21:35:31` | `cowrie.session.params` |
| `2026-04-26 21:35:31` | `cowrie.command.input` |
| `2026-04-26 21:35:31` | `cowrie.session.file_download` |
| `2026-04-26 21:35:31` | `cowrie.log.closed` |
| `2026-04-26 21:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.71.20[.]172` to AbuseIPDB if not already reported
- [ ] Block `118.71.20[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528bc47a1907

| Field | Detail |
|---|---|
| **Source IP** | `118.71.20[.]172` |
| **First Seen** | 2026-04-26 21:35 |
| **Last Seen** | 2026-04-26 21:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 21:35:33` | `cowrie.session.connect` |
| `2026-04-26 21:35:33` | `cowrie.client.version` |
| `2026-04-26 21:35:33` | `cowrie.client.kex` |
| `2026-04-26 21:35:34` | `cowrie.login.success` |
| `2026-04-26 21:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.71.20[.]172` to AbuseIPDB if not already reported
- [ ] Block `118.71.20[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4f003387cb

| Field | Detail |
|---|---|
| **Source IP** | `182.253.79[.]194` |
| **First Seen** | 2026-04-26 21:36 |
| **Last Seen** | 2026-04-26 21:36 |
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
| `2026-04-26 21:36:39` | `cowrie.session.connect` |
| `2026-04-26 21:36:39` | `cowrie.client.version` |
| `2026-04-26 21:36:39` | `cowrie.client.kex` |
| `2026-04-26 21:36:40` | `cowrie.login.success` |
| `2026-04-26 21:36:40` | `cowrie.session.params` |
| `2026-04-26 21:36:40` | `cowrie.command.input` |
| `2026-04-26 21:36:40` | `cowrie.command.failed` |
| `2026-04-26 21:36:40` | `cowrie.log.closed` |
| `2026-04-26 21:36:41` | `cowrie.session.params` |
| `2026-04-26 21:36:41` | `cowrie.command.input` |
| `2026-04-26 21:36:41` | `cowrie.session.file_download` |
| `2026-04-26 21:36:41` | `cowrie.log.closed` |
| `2026-04-26 21:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.79[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.253.79[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed30dd465c15

| Field | Detail |
|---|---|
| **Source IP** | `182.253.79[.]194` |
| **First Seen** | 2026-04-26 21:36 |
| **Last Seen** | 2026-04-26 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 21:36:44` | `cowrie.session.connect` |
| `2026-04-26 21:36:44` | `cowrie.client.version` |
| `2026-04-26 21:36:44` | `cowrie.client.kex` |
| `2026-04-26 21:36:45` | `cowrie.login.success` |
| `2026-04-26 21:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.79[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.253.79[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09e70a5ca42

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-04-26 21:41 |
| **Last Seen** | 2026-04-26 21:41 |
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
| `2026-04-26 21:41:43` | `cowrie.session.connect` |
| `2026-04-26 21:41:43` | `cowrie.client.version` |
| `2026-04-26 21:41:43` | `cowrie.client.kex` |
| `2026-04-26 21:41:43` | `cowrie.login.success` |
| `2026-04-26 21:41:44` | `cowrie.session.params` |
| `2026-04-26 21:41:44` | `cowrie.command.input` |
| `2026-04-26 21:41:44` | `cowrie.command.failed` |
| `2026-04-26 21:41:44` | `cowrie.log.closed` |
| `2026-04-26 21:41:44` | `cowrie.session.params` |
| `2026-04-26 21:41:44` | `cowrie.command.input` |
| `2026-04-26 21:41:44` | `cowrie.session.file_download` |
| `2026-04-26 21:41:44` | `cowrie.log.closed` |
| `2026-04-26 21:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b1df48d37b

| Field | Detail |
|---|---|
| **Source IP** | `119.246.15[.]94` |
| **First Seen** | 2026-04-26 21:41 |
| **Last Seen** | 2026-04-26 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 21:41:47` | `cowrie.session.connect` |
| `2026-04-26 21:41:47` | `cowrie.client.version` |
| `2026-04-26 21:41:47` | `cowrie.client.kex` |
| `2026-04-26 21:41:48` | `cowrie.login.success` |
| `2026-04-26 21:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.246.15[.]94` to AbuseIPDB if not already reported
- [ ] Block `119.246.15[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9848006bb849

| Field | Detail |
|---|---|
| **Source IP** | `218.78.59[.]30` |
| **First Seen** | 2026-04-26 21:42 |
| **Last Seen** | 2026-04-26 21:43 |
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
| `2026-04-26 21:42:50` | `cowrie.session.connect` |
| `2026-04-26 21:42:50` | `cowrie.client.version` |
| `2026-04-26 21:42:50` | `cowrie.client.kex` |
| `2026-04-26 21:42:50` | `cowrie.login.success` |
| `2026-04-26 21:42:51` | `cowrie.session.params` |
| `2026-04-26 21:42:51` | `cowrie.command.input` |
| `2026-04-26 21:42:51` | `cowrie.command.failed` |
| `2026-04-26 21:42:51` | `cowrie.log.closed` |
| `2026-04-26 21:42:52` | `cowrie.session.params` |
| `2026-04-26 21:42:52` | `cowrie.command.input` |
| `2026-04-26 21:42:52` | `cowrie.session.file_download` |
| `2026-04-26 21:42:52` | `cowrie.log.closed` |
| `2026-04-26 21:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.59[.]30` to AbuseIPDB if not already reported
- [ ] Block `218.78.59[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-574ae2faa196

| Field | Detail |
|---|---|
| **Source IP** | `218.78.59[.]30` |
| **First Seen** | 2026-04-26 21:43 |
| **Last Seen** | 2026-04-26 21:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 21:43:00` | `cowrie.session.connect` |
| `2026-04-26 21:43:00` | `cowrie.client.version` |
| `2026-04-26 21:43:00` | `cowrie.client.kex` |
| `2026-04-26 21:43:01` | `cowrie.login.success` |
| `2026-04-26 21:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.59[.]30` to AbuseIPDB if not already reported
- [ ] Block `218.78.59[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c1bc2933e1

| Field | Detail |
|---|---|
| **Source IP** | `183.92.151[.]73` |
| **First Seen** | 2026-04-26 21:55 |
| **Last Seen** | 2026-04-26 21:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 21:55:26` | `cowrie.session.connect` |
| `2026-04-26 21:55:26` | `cowrie.client.version` |
| `2026-04-26 21:55:26` | `cowrie.client.kex` |
| `2026-04-26 21:55:27` | `cowrie.login.success` |
| `2026-04-26 21:55:27` | `cowrie.session.params` |
| `2026-04-26 21:55:27` | `cowrie.command.input` |
| `2026-04-26 21:55:27` | `cowrie.log.closed` |
| `2026-04-26 21:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.92.151[.]73` to AbuseIPDB if not already reported
- [ ] Block `183.92.151[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `195.96.143[.]69` | **23** | 2026-04-26 20:57 | 2026-04-26 21:15 | 46m | 0 | `T1592` | 🟠 MEDIUM |
| `203.101.186[.]91` | **18** | 2026-04-26 21:54 | 2026-04-26 21:58 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `138.121.113[.]28` | **4** | 2026-04-26 21:01 | 2026-04-26 21:09 | 8m | 0 | `T1592` | 🟢 LOW |
| `128.203.202[.]236` | **2** | 2026-04-26 21:51 | 2026-04-26 21:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.118.224[.]96` | **2** | 2026-04-26 22:16 | 2026-04-26 22:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.194[.]210` | 1 | 2026-04-26 21:51 | 2026-04-26 21:52 | 62s | 1 | `T1110.001` | 🟢 LOW |
| `103.63.25[.]203` | 1 | 2026-04-26 21:12 | 2026-04-26 21:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.71.20[.]172` | 1 | 2026-04-26 21:35 | 2026-04-26 21:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.167.206[.]194` | 1 | 2026-04-26 22:10 | 2026-04-26 22:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.246.15[.]94` | 1 | 2026-04-26 21:41 | 2026-04-26 21:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]190` | 1 | 2026-04-26 22:12 | 2026-04-26 22:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]204` | 1 | 2026-04-26 21:38 | 2026-04-26 21:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.104.143[.]176` | 1 | 2026-04-26 21:37 | 2026-04-26 21:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.253.79[.]194` | 1 | 2026-04-26 21:36 | 2026-04-26 21:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.44.12[.]249` | 1 | 2026-04-26 21:45 | 2026-04-26 21:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.92.151[.]73` | 1 | 2026-04-26 21:55 | 2026-04-26 21:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.78.59[.]30` | 1 | 2026-04-26 21:42 | 2026-04-26 21:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.165.123[.]15` | 1 | 2026-04-26 22:14 | 2026-04-26 22:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `67.212.63[.]48` | 1 | 2026-04-26 22:23 | 2026-04-26 22:23 | 3s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `118.71.20[.]172` | VN | FPT Telecom | **100** ⚠️ | 1 |
| `128.203.202[.]236` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `101.96.194[.]210` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `14.103.118[.]190` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `183.92.151[.]73` | CN | China Unicom Hubei Province Network | **100** ⚠️ | 3 |
| `182.253.79[.]194` | ID | ANEKA_RUPA_TERA | **100** ⚠️ | 50 |
| `182.44.12[.]249` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 2 |
| `20.118.224[.]96` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `138.121.113[.]28` | AR | REFSA TELECOMUNICACIONES | **100** ⚠️ | 12 |
| `14.103.127[.]204` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (78 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 32 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 27 |
| AbuseIPDB score 18 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 153 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 78 filtered (51.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 19 recon entry/entries in table (5 group(s) consolidating 49 session(s)).

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
_Report time: 2026-04-26T22:43:58Z_
