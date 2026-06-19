# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-19 |
| **Generated At** | 2026-06-19T18:02:36Z |
| **Shift Time** | 18:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **121** |
| Confirmed Threats | **117** |
| False Positives Filtered | **4** (3.3%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **13** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **115** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **11** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `admin` | 3 |
| `345gs5662d34` | 2 |
| `test` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `test2010` | 1 |
| `qwerty` | 1 |
| `123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `test` | `test2010` | 1 |
| `user` | `qwerty` | 1 |
| `guest` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qq@2026` | `46.39.254.221` | 2026-06-19T16:58:36 |
| `root` | `3245gs5662d34` | `46.39.254.221` | 2026-06-19T16:58:43 |
| `root` | `password321` | `87.117.32.22` | 2026-06-19T17:26:13 |
| `root` | `1234567` | `91.219.196.17` | 2026-06-19T17:36:29 |
| `root` | `p@ssw0Rd` | `165.154.200.214` | 2026-06-19T17:50:34 |
| `root` | `3245gs5662d34` | `165.154.200.214` | 2026-06-19T17:50:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **121** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Nmap scanner | 15 |
| libssh | 14 |
| OpenSSH | 8 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 11 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 8 | 8 |
| `03a80b21afa8...` | Modern SSH client | 3 | 3 |
| `e788c657d1a2...` | Mirai/variant | 2 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Nmap scanner | 13 | 1 | — |
| `f555226df196...` | libssh | 11 | 4 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 8 | 8 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 3 | Modern SSH client |
| `e788c657d1a2...` | Nmap scanner | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `4c20a8895324...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.200.214`, `46.39.254.221`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **28** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS153283` | Softcrop It | 1 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS12389` | PJSC Rostelecom | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS54994` | Meteverse Limited. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-45df9bd1ca63

| Field | Detail |
|---|---|
| **Source IP** | `46.39.254[.]221` |
| **First Seen** | 2026-06-19 16:58 |
| **Last Seen** | 2026-06-19 16:58 |
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
| `2026-06-19 16:58:34` | `cowrie.session.connect` |
| `2026-06-19 16:58:34` | `cowrie.client.version` |
| `2026-06-19 16:58:35` | `cowrie.client.kex` |
| `2026-06-19 16:58:36` | `cowrie.login.success` |
| `2026-06-19 16:58:37` | `cowrie.session.params` |
| `2026-06-19 16:58:37` | `cowrie.command.input` |
| `2026-06-19 16:58:37` | `cowrie.command.failed` |
| `2026-06-19 16:58:37` | `cowrie.log.closed` |
| `2026-06-19 16:58:38` | `cowrie.session.params` |
| `2026-06-19 16:58:38` | `cowrie.command.input` |
| `2026-06-19 16:58:39` | `cowrie.session.file_download` |
| `2026-06-19 16:58:39` | `cowrie.log.closed` |
| `2026-06-19 16:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.39.254[.]221` to AbuseIPDB if not already reported
- [ ] Block `46.39.254[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d271ecd12b1

| Field | Detail |
|---|---|
| **Source IP** | `46.39.254[.]221` |
| **First Seen** | 2026-06-19 16:58 |
| **Last Seen** | 2026-06-19 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 16:58:41` | `cowrie.session.connect` |
| `2026-06-19 16:58:41` | `cowrie.client.version` |
| `2026-06-19 16:58:42` | `cowrie.client.kex` |
| `2026-06-19 16:58:43` | `cowrie.login.success` |
| `2026-06-19 16:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.39.254[.]221` to AbuseIPDB if not already reported
- [ ] Block `46.39.254[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0cdb4a66659

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-06-19 17:26 |
| **Last Seen** | 2026-06-19 17:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 17:26:11` | `cowrie.session.connect` |
| `2026-06-19 17:26:12` | `cowrie.client.version` |
| `2026-06-19 17:26:12` | `cowrie.client.kex` |
| `2026-06-19 17:26:13` | `cowrie.login.success` |
| `2026-06-19 17:26:13` | `cowrie.direct-tcpip.request` |
| `2026-06-19 17:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea84a8d1d81

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-06-19 17:36 |
| **Last Seen** | 2026-06-19 17:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 17:36:27` | `cowrie.session.connect` |
| `2026-06-19 17:36:28` | `cowrie.client.version` |
| `2026-06-19 17:36:28` | `cowrie.client.kex` |
| `2026-06-19 17:36:29` | `cowrie.login.success` |
| `2026-06-19 17:36:29` | `cowrie.direct-tcpip.request` |
| `2026-06-19 17:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f2060912f4

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]214` |
| **First Seen** | 2026-06-19 17:50 |
| **Last Seen** | 2026-06-19 17:50 |
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
| `2026-06-19 17:50:34` | `cowrie.session.connect` |
| `2026-06-19 17:50:34` | `cowrie.client.version` |
| `2026-06-19 17:50:34` | `cowrie.client.kex` |
| `2026-06-19 17:50:34` | `cowrie.login.success` |
| `2026-06-19 17:50:35` | `cowrie.session.params` |
| `2026-06-19 17:50:35` | `cowrie.command.input` |
| `2026-06-19 17:50:35` | `cowrie.command.failed` |
| `2026-06-19 17:50:35` | `cowrie.log.closed` |
| `2026-06-19 17:50:35` | `cowrie.session.params` |
| `2026-06-19 17:50:35` | `cowrie.command.input` |
| `2026-06-19 17:50:35` | `cowrie.session.file_download` |
| `2026-06-19 17:50:35` | `cowrie.log.closed` |
| `2026-06-19 17:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]214` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d934f758de5e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]214` |
| **First Seen** | 2026-06-19 17:50 |
| **Last Seen** | 2026-06-19 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 17:50:36` | `cowrie.session.connect` |
| `2026-06-19 17:50:36` | `cowrie.client.version` |
| `2026-06-19 17:50:37` | `cowrie.client.kex` |
| `2026-06-19 17:50:37` | `cowrie.login.success` |
| `2026-06-19 17:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]214` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.180.69[.]136` | **29** | 2026-06-19 15:28 | 2026-06-19 17:48 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `216.144.229[.]11` | **24** | 2026-06-19 15:34 | 2026-06-19 17:57 | 13m | 0 | `T1592` | 🟠 MEDIUM |
| `134.209.241[.]3` | **17** | 2026-06-19 15:29 | 2026-06-19 17:54 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `150.107.36[.]236` | **16** | 2026-06-19 17:02 | 2026-06-19 17:02 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `165.154.200[.]214` | **4** | 2026-06-19 17:42 | 2026-06-19 17:50 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `52.15.76[.]227` | **3** | 2026-06-19 16:29 | 2026-06-19 16:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.147.248[.]44` | 1 | 2026-06-19 16:38 | 2026-06-19 16:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.37[.]197` | 1 | 2026-06-19 17:39 | 2026-06-19 17:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.179[.]68` | 1 | 2026-06-19 17:35 | 2026-06-19 17:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-06-19 15:37 | 2026-06-19 15:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `129.146.47[.]44` | 1 | 2026-06-19 16:45 | 2026-06-19 16:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `151.40.78[.]76` | 1 | 2026-06-19 15:37 | 2026-06-19 15:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `174.35.25[.]178` | 1 | 2026-06-19 17:40 | 2026-06-19 17:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.139[.]130` | 1 | 2026-06-19 17:47 | 2026-06-19 17:48 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.106.80[.]16` | 1 | 2026-06-19 17:59 | 2026-06-19 17:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]95` | 1 | 2026-06-19 16:16 | 2026-06-19 16:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.82.111[.]224` | 1 | 2026-06-19 17:38 | 2026-06-19 17:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.86.136[.]221` | 1 | 2026-06-19 17:07 | 2026-06-19 17:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `200.159.14[.]187` | 1 | 2026-06-19 16:26 | 2026-06-19 16:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.39.254[.]221` | 1 | 2026-06-19 16:58 | 2026-06-19 16:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]13` | 1 | 2026-06-19 17:08 | 2026-06-19 17:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-06-19 17:12 | 2026-06-19 17:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `63.47.149[.]59` | 1 | 2026-06-19 15:27 | 2026-06-19 15:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]191` | 1 | 2026-06-19 17:37 | 2026-06-19 17:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `216.144.229[.]11` | US | HostPapa | **100** ⚠️ | 6 |
| `107.180.69[.]136` | US | GoDaddy.com, LLC | **100** ⚠️ | 10 |
| `129.146.47[.]44` | US | Oracle Corporation | **100** ⚠️ | 4 |
| `103.147.248[.]44` | IN | Softcrop It | **100** ⚠️ | 50 |
| `63.47.149[.]59` | US | Verizon Business | **100** ⚠️ | 50 |
| `91.219.196[.]17` | RU | Private Enterprise Tron Vitaliy Vladimirovich | **100** ⚠️ | 50 |
| `134.209.241[.]3` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `165.154.200[.]214` | SG | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 9 |
| `115.190.179[.]68` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 37 |
| `200.159.14[.]187` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 39 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 121 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (3.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 24 recon entry/entries in table (6 group(s) consolidating 93 session(s)).

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
_Report time: 2026-06-19T18:02:36Z_
