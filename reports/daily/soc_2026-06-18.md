# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-18 |
| **Generated At** | 2026-06-18T18:28:39Z |
| **Shift Time** | 18:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **168** |
| Confirmed Threats | **147** |
| False Positives Filtered | **21** (12.5%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **14** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **161** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **33** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **25** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `345gs5662d34` | 3 |
| `young` | 1 |
| `eko` | 1 |
| `arp` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 8 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `young123` | 1 |
| `eko123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `young` | `young123` | 1 |
| `eko` | `eko123` | 1 |
| `arp` | `arp` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin1!!` | `171.25.158.74` | 2026-06-18T15:44:35 |
| `root` | `3245gs5662d34` | `171.25.158.74` | 2026-06-18T15:44:39 |
| `root` | `root123@` | `101.126.82.218` | 2026-06-18T15:47:05 |
| `root` | `3245gs5662d34` | `101.126.82.218` | 2026-06-18T15:47:10 |
| `root` | `123456Zz` | `20.245.71.147` | 2026-06-18T16:42:10 |
| `root` | `3245gs5662d34` | `20.245.71.147` | 2026-06-18T16:42:15 |
| `root` | `ubuntu` | `165.154.177.119` | 2026-06-18T17:15:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **168** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 29 |
| OpenSSH | 5 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 25 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 5 | 5 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 25 | 5 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 5 | 5 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
Source IPs: `101.126.82.218`, `20.245.71.147`, `171.25.158.74`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **24** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS131386` | Long Van System Solution JSC | 1 | HIGH |
| `AS20207` | Gigared S.A. | 1 | HIGH |
| `AS15802` | Emirates Integrated Telecommunications Company PJSC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0e6ccc5fac70

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-06-18 15:44 |
| **Last Seen** | 2026-06-18 15:44 |
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
| `2026-06-18 15:44:34` | `cowrie.session.connect` |
| `2026-06-18 15:44:34` | `cowrie.client.version` |
| `2026-06-18 15:44:34` | `cowrie.client.kex` |
| `2026-06-18 15:44:35` | `cowrie.login.success` |
| `2026-06-18 15:44:35` | `cowrie.session.params` |
| `2026-06-18 15:44:35` | `cowrie.command.input` |
| `2026-06-18 15:44:35` | `cowrie.command.failed` |
| `2026-06-18 15:44:36` | `cowrie.log.closed` |
| `2026-06-18 15:44:36` | `cowrie.session.params` |
| `2026-06-18 15:44:36` | `cowrie.command.input` |
| `2026-06-18 15:44:36` | `cowrie.session.file_download` |
| `2026-06-18 15:44:36` | `cowrie.log.closed` |
| `2026-06-18 15:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4ce397b460

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-06-18 15:44 |
| **Last Seen** | 2026-06-18 15:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 15:44:38` | `cowrie.session.connect` |
| `2026-06-18 15:44:38` | `cowrie.client.version` |
| `2026-06-18 15:44:39` | `cowrie.client.kex` |
| `2026-06-18 15:44:39` | `cowrie.login.success` |
| `2026-06-18 15:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc2b6176dbfc

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-06-18 15:47 |
| **Last Seen** | 2026-06-18 15:47 |
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
| `2026-06-18 15:47:04` | `cowrie.session.connect` |
| `2026-06-18 15:47:04` | `cowrie.client.version` |
| `2026-06-18 15:47:04` | `cowrie.client.kex` |
| `2026-06-18 15:47:05` | `cowrie.login.success` |
| `2026-06-18 15:47:06` | `cowrie.session.params` |
| `2026-06-18 15:47:06` | `cowrie.command.input` |
| `2026-06-18 15:47:06` | `cowrie.command.failed` |
| `2026-06-18 15:47:06` | `cowrie.log.closed` |
| `2026-06-18 15:47:06` | `cowrie.session.params` |
| `2026-06-18 15:47:06` | `cowrie.command.input` |
| `2026-06-18 15:47:06` | `cowrie.session.file_download` |
| `2026-06-18 15:47:06` | `cowrie.log.closed` |
| `2026-06-18 15:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f6cfedfba5

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-06-18 15:47 |
| **Last Seen** | 2026-06-18 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 15:47:09` | `cowrie.session.connect` |
| `2026-06-18 15:47:09` | `cowrie.client.version` |
| `2026-06-18 15:47:09` | `cowrie.client.kex` |
| `2026-06-18 15:47:10` | `cowrie.login.success` |
| `2026-06-18 15:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9caae9ad22

| Field | Detail |
|---|---|
| **Source IP** | `20.245.71[.]147` |
| **First Seen** | 2026-06-18 16:42 |
| **Last Seen** | 2026-06-18 16:42 |
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
| `2026-06-18 16:42:08` | `cowrie.session.connect` |
| `2026-06-18 16:42:08` | `cowrie.client.version` |
| `2026-06-18 16:42:09` | `cowrie.client.kex` |
| `2026-06-18 16:42:10` | `cowrie.login.success` |
| `2026-06-18 16:42:10` | `cowrie.session.params` |
| `2026-06-18 16:42:10` | `cowrie.command.input` |
| `2026-06-18 16:42:10` | `cowrie.command.failed` |
| `2026-06-18 16:42:11` | `cowrie.log.closed` |
| `2026-06-18 16:42:11` | `cowrie.session.params` |
| `2026-06-18 16:42:11` | `cowrie.command.input` |
| `2026-06-18 16:42:11` | `cowrie.session.file_download` |
| `2026-06-18 16:42:11` | `cowrie.log.closed` |
| `2026-06-18 16:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.245.71[.]147` to AbuseIPDB if not already reported
- [ ] Block `20.245.71[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19367e2f61dc

| Field | Detail |
|---|---|
| **Source IP** | `20.245.71[.]147` |
| **First Seen** | 2026-06-18 16:42 |
| **Last Seen** | 2026-06-18 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 16:42:14` | `cowrie.session.connect` |
| `2026-06-18 16:42:14` | `cowrie.client.version` |
| `2026-06-18 16:42:14` | `cowrie.client.kex` |
| `2026-06-18 16:42:15` | `cowrie.login.success` |
| `2026-06-18 16:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.245.71[.]147` to AbuseIPDB if not already reported
- [ ] Block `20.245.71[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef4def38cfc1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.177[.]119` |
| **First Seen** | 2026-06-18 17:15 |
| **Last Seen** | 2026-06-18 17:16 |
| **Session Duration** | 95s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 17:15:17` | `cowrie.session.connect` |
| `2026-06-18 17:15:17` | `cowrie.client.version` |
| `2026-06-18 17:15:17` | `cowrie.client.kex` |
| `2026-06-18 17:15:18` | `cowrie.login.success` |
| `2026-06-18 17:16:52` | `cowrie.session.file_upload` |
| `2026-06-18 17:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.177[.]119` to AbuseIPDB if not already reported
- [ ] Block `165.154.177[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.122.23[.]93` | **109** | 2026-06-18 15:32 | 2026-06-18 18:27 | 101m | 0 | `T1592` | 🟠 MEDIUM |
| `157.230.150[.]187` | **4** | 2026-06-18 17:49 | 2026-06-18 17:50 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]186` | **4** | 2026-06-18 15:51 | 2026-06-18 15:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.221.180[.]165` | **3** | 2026-06-18 16:35 | 2026-06-18 16:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.200.25[.]198` | **2** | 2026-06-18 16:44 | 2026-06-18 16:46 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `173.249.210[.]17` | **2** | 2026-06-18 17:06 | 2026-06-18 17:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.82[.]218` | 1 | 2026-06-18 15:47 | 2026-06-18 15:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.227.152[.]171` | 1 | 2026-06-18 17:08 | 2026-06-18 17:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.166.253[.]226` | 1 | 2026-06-18 18:23 | 2026-06-18 18:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.113[.]212` | 1 | 2026-06-18 15:46 | 2026-06-18 15:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.25.158[.]74` | 1 | 2026-06-18 15:44 | 2026-06-18 15:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.221[.]224` | 1 | 2026-06-18 18:27 | 2026-06-18 18:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.57.233[.]133` | 1 | 2026-06-18 16:00 | 2026-06-18 16:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.245.71[.]147` | 1 | 2026-06-18 16:42 | 2026-06-18 16:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.154.80[.]51` | 1 | 2026-06-18 17:48 | 2026-06-18 17:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.111[.]118` | 1 | 2026-06-18 15:32 | 2026-06-18 15:32 | 7s | 0 | `T1592` | 🟢 LOW |
| `37.60.141[.]90` | 1 | 2026-06-18 16:10 | 2026-06-18 16:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.32.226[.]231` | 1 | 2026-06-18 17:37 | 2026-06-18 17:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `87.106.35[.]227` | 1 | 2026-06-18 16:31 | 2026-06-18 16:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.244.93[.]27` | 1 | 2026-06-18 16:32 | 2026-06-18 16:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.183.59[.]33` | 1 | 2026-06-18 17:23 | 2026-06-18 17:25 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.205.250[.]78` | 1 | 2026-06-18 17:53 | 2026-06-18 17:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `134.122.23[.]93` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `157.230.150[.]187` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `94.183.59[.]33` | IR | Aria Shatel PJSC | **100** ⚠️ | 4 |
| `18.221.180[.]165` | US | Amazon Technologies Inc. | **100** ⚠️ | 35 |
| `173.249.210[.]17` | US | tzulo, inc. | **100** ⚠️ | 1 |
| `37.60.141[.]90` | NL | ColocaTel Datacenter | **100** ⚠️ | 7 |
| `27.123.111[.]118` | IN | Bharti Airtel Limited | **100** ⚠️ | 50 |
| `87.244.93[.]27` | JE | Jersey Telecom Rapid Service | **100** ⚠️ | 2 |
| `87.106.35[.]227` | GB | IONOS SE | **100** ⚠️ | 50 |
| `45.32.226[.]231` | US | Vultr Holdings, LLC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 35 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 168 cases |
| Tool 34  | Credential Extractor        | ✅ 33 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (12.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 22 recon entry/entries in table (6 group(s) consolidating 124 session(s)).

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
_Report time: 2026-06-18T18:28:39Z_
