# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-30 |
| **Generated At** | 2026-04-30T22:56:20Z |
| **Shift Time** | 22:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1023** |
| Confirmed Threats | **212** |
| False Positives Filtered | **811** (79.3%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **14** |
| High Severity Cases | **133** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **890** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **148** |
| Unique Credential Pairs | **145** |
| Unique Usernames | **9** |
| Unique Passwords | **145** |
| Successful Auth Pairs | **133** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 135 |
| `admin` | 3 |
| `test` | 2 |
| `user` | 2 |
| `ts3` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `t3st` | 2 |
| `123456` | 2 |
| `123456789` | 2 |
| `ubuntu` | 1 |
| `fuc` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `t3st` | 2 |
| `root` | `123456` | 2 |
| `ts3` | `123456789` | 2 |
| `root` | `ubuntu` | 1 |
| `root` | `fuc` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `202.165.15.88` | 2026-04-30T21:06:06 |
| `root` | `fuc` | `111.61.104.0` | 2026-04-30T22:01:17 |
| `root` | `glock` | `111.61.104.0` | 2026-04-30T22:01:17 |
| `root` | `frisette` | `111.61.104.0` | 2026-04-30T22:01:19 |
| `root` | `George` | `111.61.104.0` | 2026-04-30T22:01:19 |
| `root` | `fuckhead` | `111.61.104.0` | 2026-04-30T22:01:20 |
| `root` | `facebook1` | `111.61.104.0` | 2026-04-30T22:01:20 |
| `root` | `fabrizio` | `111.61.104.0` | 2026-04-30T22:01:22 |
| `root` | `freefall` | `111.61.104.0` | 2026-04-30T22:01:22 |
| `root` | `electronique` | `111.61.104.0` | 2026-04-30T22:01:38 |
| `root` | `extra` | `111.61.104.0` | 2026-04-30T22:01:38 |
| `root` | `edgar` | `111.61.104.0` | 2026-04-30T22:01:40 |
| `root` | `elcamino` | `111.61.104.0` | 2026-04-30T22:01:40 |
| `root` | `diaper` | `111.61.104.0` | 2026-04-30T22:01:41 |
| `root` | `doucette` | `111.61.104.0` | 2026-04-30T22:01:42 |
| `root` | `datsun` | `111.61.104.0` | 2026-04-30T22:01:43 |
| `root` | `carpente` | `111.61.104.0` | 2026-04-30T22:01:59 |
| `root` | `doc` | `111.61.104.0` | 2026-04-30T22:02:00 |
| `root` | `carman` | `111.61.104.0` | 2026-04-30T22:02:01 |
| `root` | `djoudjou` | `111.61.104.0` | 2026-04-30T22:02:01 |
| `root` | `boytoy` | `111.61.104.0` | 2026-04-30T22:02:02 |
| `root` | `dingdong1` | `111.61.104.0` | 2026-04-30T22:02:03 |
| `root` | `boiler` | `111.61.104.0` | 2026-04-30T22:02:04 |
| `root` | `diakite` | `111.61.104.0` | 2026-04-30T22:02:04 |
| `root` | `bluesman` | `111.61.104.0` | 2026-04-30T22:02:12 |
| `root` | `bluebell` | `111.61.104.0` | 2026-04-30T22:02:14 |
| `root` | `bitchy` | `111.61.104.0` | 2026-04-30T22:02:15 |
| `root` | `bigpimp` | `111.61.104.0` | 2026-04-30T22:02:17 |
| `root` | `Baseball` | `111.61.104.0` | 2026-04-30T22:02:18 |
| `root` | `astral` | `111.61.104.0` | 2026-04-30T22:02:20 |
| `root` | `coq` | `111.61.104.0` | 2026-04-30T22:02:20 |
| `root` | `armstron` | `111.61.104.0` | 2026-04-30T22:02:21 |
| `root` | `clubiste` | `111.61.104.0` | 2026-04-30T22:02:22 |
| `root` | `999666` | `111.61.104.0` | 2026-04-30T22:02:23 |
| `root` | `cl` | `111.61.104.0` | 2026-04-30T22:02:24 |
| `root` | `3x7PxR` | `111.61.104.0` | 2026-04-30T22:02:25 |
| `root` | `chaumont` | `111.61.104.0` | 2026-04-30T22:02:40 |
| `root` | `30041987` | `111.61.104.0` | 2026-04-30T22:02:41 |
| `root` | `chanteuse` | `111.61.104.0` | 2026-04-30T22:02:42 |
| `root` | `27081990` | `111.61.104.0` | 2026-04-30T22:02:43 |
| `root` | `carrie` | `111.61.104.0` | 2026-04-30T22:02:44 |
| `root` | `26031988` | `111.61.104.0` | 2026-04-30T22:02:44 |
| `root` | `carlito1` | `111.61.104.0` | 2026-04-30T22:02:46 |
| `root` | `25091987` | `111.61.104.0` | 2026-04-30T22:02:46 |
| `root` | `brasco` | `111.61.104.0` | 2026-04-30T22:02:47 |
| `root` | `25041988` | `111.61.104.0` | 2026-04-30T22:02:47 |
| `root` | `bigman` | `111.61.104.0` | 2026-04-30T22:03:04 |
| `root` | `22041988` | `111.61.104.0` | 2026-04-30T22:03:04 |
| `root` | `azerty3` | `111.61.104.0` | 2026-04-30T22:03:05 |
| `root` | `22031984` | `111.61.104.0` | 2026-04-30T22:03:05 |
| `root` | `aza` | `111.61.104.0` | 2026-04-30T22:03:07 |
| `root` | `21051988` | `111.61.104.0` | 2026-04-30T22:03:07 |
| `root` | `17011987` | `111.61.104.0` | 2026-04-30T22:03:15 |
| `root` | `12345qw` | `111.61.104.0` | 2026-04-30T22:03:18 |
| `root` | `123456ru` | `111.61.104.0` | 2026-04-30T22:03:19 |
| `root` | `1124` | `111.61.104.0` | 2026-04-30T22:03:21 |
| `root` | `10041986` | `111.61.104.0` | 2026-04-30T22:03:22 |
| `root` | `07091990` | `111.61.104.0` | 2026-04-30T22:03:24 |
| `root` | `automne` | `111.61.104.0` | 2026-04-30T22:03:24 |
| `root` | `02051981` | `111.61.104.0` | 2026-04-30T22:03:25 |
| `root` | `angeles` | `111.61.104.0` | 2026-04-30T22:03:25 |
| `root` | `01031985` | `111.61.104.0` | 2026-04-30T22:03:27 |
| `root` | `alex13` | `111.61.104.0` | 2026-04-30T22:03:27 |
| `root` | `01021990` | `111.61.104.0` | 2026-04-30T22:03:28 |
| `root` | `Sabrina` | `111.61.104.0` | 2026-04-30T22:03:28 |
| `root` | `yfnfkb` | `111.61.104.0` | 2026-04-30T22:03:30 |
| `root` | `SAYANG1` | `111.61.104.0` | 2026-04-30T22:03:30 |
| `root` | `yeah` | `111.61.104.0` | 2026-04-30T22:03:38 |
| `root` | `NIKITA` | `111.61.104.0` | 2026-04-30T22:03:38 |
| `root` | `WP2003WP` | `111.61.104.0` | 2026-04-30T22:03:40 |
| `root` | `Monique` | `111.61.104.0` | 2026-04-30T22:03:40 |
| `root` | `vitamin` | `111.61.104.0` | 2026-04-30T22:03:41 |
| `root` | `JUNPYO` | `111.61.104.0` | 2026-04-30T22:03:42 |
| `root` | `villa` | `111.61.104.0` | 2026-04-30T22:03:42 |
| `root` | `Charlene` | `111.61.104.0` | 2026-04-30T22:03:43 |
| `root` | `trinitro` | `111.61.104.0` | 2026-04-30T22:03:44 |
| `root` | `AURORE` | `111.61.104.0` | 2026-04-30T22:03:45 |
| `root` | `tigge` | `111.61.104.0` | 2026-04-30T22:03:45 |
| `root` | `8520` | `111.61.104.0` | 2026-04-30T22:03:46 |
| `root` | `thewho` | `111.61.104.0` | 2026-04-30T22:03:47 |
| `root` | `848484` | `111.61.104.0` | 2026-04-30T22:03:48 |
| `root` | `66666666661` | `111.61.104.0` | 2026-04-30T22:03:49 |
| `root` | `4454708` | `111.61.104.0` | 2026-04-30T22:03:58 |
| `root` | `301290` | `111.61.104.0` | 2026-04-30T22:03:59 |
| `root` | `301286` | `111.61.104.0` | 2026-04-30T22:04:01 |
| `root` | `300686` | `111.61.104.0` | 2026-04-30T22:04:02 |
| `root` | `3006` | `111.61.104.0` | 2026-04-30T22:04:03 |
| `root` | `swinging` | `111.61.104.0` | 2026-04-30T22:04:04 |
| `root` | `300488` | `111.61.104.0` | 2026-04-30T22:04:05 |
| `root` | `smoke1` | `111.61.104.0` | 2026-04-30T22:04:06 |
| `root` | `271088` | `111.61.104.0` | 2026-04-30T22:04:07 |
| `root` | `sluggo` | `111.61.104.0` | 2026-04-30T22:04:07 |
| `root` | `260287` | `111.61.104.0` | 2026-04-30T22:04:08 |
| `root` | `sleep` | `111.61.104.0` | 2026-04-30T22:04:09 |
| `root` | `252` | `111.61.104.0` | 2026-04-30T22:04:10 |
| `root` | `shamus` | `111.61.104.0` | 2026-04-30T22:04:10 |
| `root` | `250987` | `111.61.104.0` | 2026-04-30T22:04:11 |
| `root` | `250285` | `111.61.104.0` | 2026-04-30T22:04:20 |
| `root` | `241282` | `111.61.104.0` | 2026-04-30T22:04:21 |
| `root` | `241089` | `111.61.104.0` | 2026-04-30T22:04:23 |
| `root` | `241085` | `111.61.104.0` | 2026-04-30T22:04:24 |
| `root` | `240589` | `111.61.104.0` | 2026-04-30T22:04:26 |
| `root` | `sevens` | `111.61.104.0` | 2026-04-30T22:04:27 |
| `root` | `240489` | `111.61.104.0` | 2026-04-30T22:04:27 |
| `root` | `rober` | `111.61.104.0` | 2026-04-30T22:04:28 |
| `root` | `rfvfcenhf` | `111.61.104.0` | 2026-04-30T22:04:30 |
| `root` | `231280` | `111.61.104.0` | 2026-04-30T22:04:30 |
| `root` | `231185` | `111.61.104.0` | 2026-04-30T22:04:31 |
| `root` | `230783` | `111.61.104.0` | 2026-04-30T22:04:33 |
| `root` | `redhat` | `111.61.104.0` | 2026-04-30T22:04:38 |
| `root` | `qazws` | `111.61.104.0` | 2026-04-30T22:04:40 |
| `root` | `pufunga7782` | `111.61.104.0` | 2026-04-30T22:04:41 |
| `root` | `220785` | `111.61.104.0` | 2026-04-30T22:04:42 |
| `root` | `priest` | `111.61.104.0` | 2026-04-30T22:04:43 |
| `root` | `210990` | `111.61.104.0` | 2026-04-30T22:04:43 |
| `root` | `pizdec` | `111.61.104.0` | 2026-04-30T22:04:44 |
| `root` | `210583` | `111.61.104.0` | 2026-04-30T22:04:45 |
| `root` | `pebble` | `111.61.104.0` | 2026-04-30T22:04:46 |
| `root` | `201282` | `111.61.104.0` | 2026-04-30T22:04:46 |
| `root` | `201183` | `111.61.104.0` | 2026-04-30T22:04:47 |
| `root` | `200586` | `111.61.104.0` | 2026-04-30T22:04:49 |
| `root` | `palmtree` | `111.61.104.0` | 2026-04-30T22:04:50 |
| `root` | `1919` | `111.61.104.0` | 2026-04-30T22:04:50 |
| `root` | `oxygen` | `111.61.104.0` | 2026-04-30T22:04:52 |
| `root` | `190687` | `111.61.104.0` | 2026-04-30T22:04:52 |
| `root` | `1906` | `111.61.104.0` | 2026-04-30T22:05:08 |
| `root` | `mahler` | `111.61.104.0` | 2026-04-30T22:05:09 |
| `root` | `19` | `111.61.104.0` | 2026-04-30T22:05:10 |
| `root` | `1811` | `111.61.104.0` | 2026-04-30T22:05:11 |
| `root` | `korova` | `111.61.104.0` | 2026-04-30T22:05:11 |
| `root` | `180585` | `111.61.104.0` | 2026-04-30T22:05:12 |
| `root` | `kokomo` | `111.61.104.0` | 2026-04-30T22:05:13 |
| `root` | `180391` | `111.61.104.0` | 2026-04-30T22:05:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1023** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 135 |
| libssh | 62 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `01ca35584ad5...` | Modern SSH client | 134 | 1 |
| `af8223ac9914...` | libssh-based | 47 | 2 |
| `03a80b21afa8...` | Modern SSH client | 3 | 3 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `01ca35584ad5...` | Go SSH scanner | 134 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 47 | 2 | libssh-based |
| `95420f9d932d...` | libssh | 12 | 3 | — |
| `03a80b21afa8...` | libssh | 3 | 3 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **24** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |
| `AS20473` | The Constant Company, LLC | 2 | LOW |
| `AS134762` | CHINANET Liaoning province Dalian MAN network | 1 | HIGH |
| `AS135987` | Reload Company Limited | 1 | LOW |
| `AS273068` | DIAZ TORO JAVIER ANDRES (ECUARED PCTRONIC) | 1 | LOW |
| `AS58563` | CHINANET Hubei province network | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (133)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6e33afaae1c8

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]88` |
| **First Seen** | 2026-04-30 21:06 |
| **Last Seen** | 2026-04-30 21:11 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 21:06:06` | `cowrie.session.connect` |
| `2026-04-30 21:06:06` | `cowrie.client.version` |
| `2026-04-30 21:06:06` | `cowrie.client.kex` |
| `2026-04-30 21:06:06` | `cowrie.login.success` |
| `2026-04-30 21:11:06` | `cowrie.session.file_upload` |
| `2026-04-30 21:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]88` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e46c8e387cc

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:17` | `cowrie.session.connect` |
| `2026-04-30 22:01:17` | `cowrie.client.version` |
| `2026-04-30 22:01:17` | `cowrie.client.kex` |
| `2026-04-30 22:01:17` | `cowrie.login.success` |
| `2026-04-30 22:01:18` | `cowrie.session.params` |
| `2026-04-30 22:01:18` | `cowrie.command.input` |
| `2026-04-30 22:01:18` | `cowrie.log.closed` |
| `2026-04-30 22:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e04440fc93

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:17` | `cowrie.session.connect` |
| `2026-04-30 22:01:17` | `cowrie.client.version` |
| `2026-04-30 22:01:17` | `cowrie.client.kex` |
| `2026-04-30 22:01:17` | `cowrie.login.success` |
| `2026-04-30 22:01:18` | `cowrie.session.params` |
| `2026-04-30 22:01:18` | `cowrie.command.input` |
| `2026-04-30 22:01:18` | `cowrie.log.closed` |
| `2026-04-30 22:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0459db72b336

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:18` | `cowrie.session.connect` |
| `2026-04-30 22:01:18` | `cowrie.client.version` |
| `2026-04-30 22:01:18` | `cowrie.client.kex` |
| `2026-04-30 22:01:19` | `cowrie.login.success` |
| `2026-04-30 22:01:19` | `cowrie.session.params` |
| `2026-04-30 22:01:19` | `cowrie.command.input` |
| `2026-04-30 22:01:19` | `cowrie.log.closed` |
| `2026-04-30 22:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7777e3f82aa

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:18` | `cowrie.session.connect` |
| `2026-04-30 22:01:18` | `cowrie.client.version` |
| `2026-04-30 22:01:18` | `cowrie.client.kex` |
| `2026-04-30 22:01:19` | `cowrie.login.success` |
| `2026-04-30 22:01:19` | `cowrie.session.params` |
| `2026-04-30 22:01:19` | `cowrie.command.input` |
| `2026-04-30 22:01:19` | `cowrie.log.closed` |
| `2026-04-30 22:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb47b2b56b3

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:20` | `cowrie.session.connect` |
| `2026-04-30 22:01:20` | `cowrie.client.version` |
| `2026-04-30 22:01:20` | `cowrie.client.kex` |
| `2026-04-30 22:01:20` | `cowrie.login.success` |
| `2026-04-30 22:01:21` | `cowrie.session.params` |
| `2026-04-30 22:01:21` | `cowrie.command.input` |
| `2026-04-30 22:01:21` | `cowrie.log.closed` |
| `2026-04-30 22:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9778a9158325

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:20` | `cowrie.session.connect` |
| `2026-04-30 22:01:20` | `cowrie.client.version` |
| `2026-04-30 22:01:20` | `cowrie.client.kex` |
| `2026-04-30 22:01:20` | `cowrie.login.success` |
| `2026-04-30 22:01:21` | `cowrie.session.params` |
| `2026-04-30 22:01:21` | `cowrie.command.input` |
| `2026-04-30 22:01:21` | `cowrie.log.closed` |
| `2026-04-30 22:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95feb68d9611

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:21` | `cowrie.session.connect` |
| `2026-04-30 22:01:21` | `cowrie.client.version` |
| `2026-04-30 22:01:21` | `cowrie.client.kex` |
| `2026-04-30 22:01:22` | `cowrie.login.success` |
| `2026-04-30 22:01:22` | `cowrie.session.params` |
| `2026-04-30 22:01:22` | `cowrie.command.input` |
| `2026-04-30 22:01:23` | `cowrie.log.closed` |
| `2026-04-30 22:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbed138d887a

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:21` | `cowrie.session.connect` |
| `2026-04-30 22:01:21` | `cowrie.client.version` |
| `2026-04-30 22:01:21` | `cowrie.client.kex` |
| `2026-04-30 22:01:22` | `cowrie.login.success` |
| `2026-04-30 22:01:22` | `cowrie.session.params` |
| `2026-04-30 22:01:22` | `cowrie.command.input` |
| `2026-04-30 22:01:22` | `cowrie.log.closed` |
| `2026-04-30 22:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de354a8ac59f

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:38` | `cowrie.session.connect` |
| `2026-04-30 22:01:38` | `cowrie.client.version` |
| `2026-04-30 22:01:38` | `cowrie.client.kex` |
| `2026-04-30 22:01:38` | `cowrie.login.success` |
| `2026-04-30 22:01:39` | `cowrie.session.params` |
| `2026-04-30 22:01:39` | `cowrie.command.input` |
| `2026-04-30 22:01:39` | `cowrie.log.closed` |
| `2026-04-30 22:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79bb250d169f

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:38` | `cowrie.session.connect` |
| `2026-04-30 22:01:38` | `cowrie.client.version` |
| `2026-04-30 22:01:38` | `cowrie.client.kex` |
| `2026-04-30 22:01:38` | `cowrie.login.success` |
| `2026-04-30 22:01:39` | `cowrie.session.params` |
| `2026-04-30 22:01:39` | `cowrie.command.input` |
| `2026-04-30 22:01:39` | `cowrie.log.closed` |
| `2026-04-30 22:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d767a7103c8

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:39` | `cowrie.session.connect` |
| `2026-04-30 22:01:39` | `cowrie.client.version` |
| `2026-04-30 22:01:39` | `cowrie.client.kex` |
| `2026-04-30 22:01:40` | `cowrie.login.success` |
| `2026-04-30 22:01:40` | `cowrie.session.params` |
| `2026-04-30 22:01:40` | `cowrie.command.input` |
| `2026-04-30 22:01:40` | `cowrie.log.closed` |
| `2026-04-30 22:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d68591300a6

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:39` | `cowrie.session.connect` |
| `2026-04-30 22:01:39` | `cowrie.client.version` |
| `2026-04-30 22:01:39` | `cowrie.client.kex` |
| `2026-04-30 22:01:40` | `cowrie.login.success` |
| `2026-04-30 22:01:40` | `cowrie.session.params` |
| `2026-04-30 22:01:40` | `cowrie.command.input` |
| `2026-04-30 22:01:40` | `cowrie.log.closed` |
| `2026-04-30 22:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e580fa98b7b7

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:41` | `cowrie.session.connect` |
| `2026-04-30 22:01:41` | `cowrie.client.version` |
| `2026-04-30 22:01:41` | `cowrie.client.kex` |
| `2026-04-30 22:01:41` | `cowrie.login.success` |
| `2026-04-30 22:01:42` | `cowrie.session.params` |
| `2026-04-30 22:01:42` | `cowrie.command.input` |
| `2026-04-30 22:01:42` | `cowrie.log.closed` |
| `2026-04-30 22:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1349a3d8c00

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:41` | `cowrie.session.connect` |
| `2026-04-30 22:01:41` | `cowrie.client.version` |
| `2026-04-30 22:01:42` | `cowrie.client.kex` |
| `2026-04-30 22:01:42` | `cowrie.login.success` |
| `2026-04-30 22:01:42` | `cowrie.session.params` |
| `2026-04-30 22:01:42` | `cowrie.command.input` |
| `2026-04-30 22:01:43` | `cowrie.log.closed` |
| `2026-04-30 22:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64a73956ac0

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:42` | `cowrie.session.connect` |
| `2026-04-30 22:01:42` | `cowrie.client.version` |
| `2026-04-30 22:01:42` | `cowrie.client.kex` |
| `2026-04-30 22:01:43` | `cowrie.login.success` |
| `2026-04-30 22:01:43` | `cowrie.session.params` |
| `2026-04-30 22:01:43` | `cowrie.command.input` |
| `2026-04-30 22:01:43` | `cowrie.log.closed` |
| `2026-04-30 22:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c55aa11e272

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:59` | `cowrie.session.connect` |
| `2026-04-30 22:01:59` | `cowrie.client.version` |
| `2026-04-30 22:01:59` | `cowrie.client.kex` |
| `2026-04-30 22:01:59` | `cowrie.login.success` |
| `2026-04-30 22:02:00` | `cowrie.session.params` |
| `2026-04-30 22:02:00` | `cowrie.command.input` |
| `2026-04-30 22:02:00` | `cowrie.log.closed` |
| `2026-04-30 22:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1964ac1997c1

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:01 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:01:59` | `cowrie.session.connect` |
| `2026-04-30 22:01:59` | `cowrie.client.version` |
| `2026-04-30 22:01:59` | `cowrie.client.kex` |
| `2026-04-30 22:02:00` | `cowrie.login.success` |
| `2026-04-30 22:02:00` | `cowrie.session.params` |
| `2026-04-30 22:02:00` | `cowrie.command.input` |
| `2026-04-30 22:02:00` | `cowrie.log.closed` |
| `2026-04-30 22:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae8161bb4d65

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:00` | `cowrie.session.connect` |
| `2026-04-30 22:02:00` | `cowrie.client.version` |
| `2026-04-30 22:02:00` | `cowrie.client.kex` |
| `2026-04-30 22:02:01` | `cowrie.login.success` |
| `2026-04-30 22:02:01` | `cowrie.session.params` |
| `2026-04-30 22:02:01` | `cowrie.command.input` |
| `2026-04-30 22:02:01` | `cowrie.log.closed` |
| `2026-04-30 22:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfc2648eb69

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:00` | `cowrie.session.connect` |
| `2026-04-30 22:02:00` | `cowrie.client.version` |
| `2026-04-30 22:02:00` | `cowrie.client.kex` |
| `2026-04-30 22:02:01` | `cowrie.login.success` |
| `2026-04-30 22:02:01` | `cowrie.session.params` |
| `2026-04-30 22:02:01` | `cowrie.command.input` |
| `2026-04-30 22:02:02` | `cowrie.log.closed` |
| `2026-04-30 22:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f1ff2b1c7f

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:02` | `cowrie.session.connect` |
| `2026-04-30 22:02:02` | `cowrie.client.version` |
| `2026-04-30 22:02:02` | `cowrie.client.kex` |
| `2026-04-30 22:02:02` | `cowrie.login.success` |
| `2026-04-30 22:02:03` | `cowrie.session.params` |
| `2026-04-30 22:02:03` | `cowrie.command.input` |
| `2026-04-30 22:02:03` | `cowrie.log.closed` |
| `2026-04-30 22:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e81e06c2c8

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:02` | `cowrie.session.connect` |
| `2026-04-30 22:02:02` | `cowrie.client.version` |
| `2026-04-30 22:02:02` | `cowrie.client.kex` |
| `2026-04-30 22:02:03` | `cowrie.login.success` |
| `2026-04-30 22:02:03` | `cowrie.session.params` |
| `2026-04-30 22:02:03` | `cowrie.command.input` |
| `2026-04-30 22:02:03` | `cowrie.log.closed` |
| `2026-04-30 22:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27866582ff6e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:03` | `cowrie.session.connect` |
| `2026-04-30 22:02:03` | `cowrie.client.version` |
| `2026-04-30 22:02:03` | `cowrie.client.kex` |
| `2026-04-30 22:02:04` | `cowrie.login.success` |
| `2026-04-30 22:02:04` | `cowrie.session.params` |
| `2026-04-30 22:02:04` | `cowrie.command.input` |
| `2026-04-30 22:02:04` | `cowrie.log.closed` |
| `2026-04-30 22:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d71fb6b9fe

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:03` | `cowrie.session.connect` |
| `2026-04-30 22:02:03` | `cowrie.client.version` |
| `2026-04-30 22:02:04` | `cowrie.client.kex` |
| `2026-04-30 22:02:04` | `cowrie.login.success` |
| `2026-04-30 22:02:04` | `cowrie.session.params` |
| `2026-04-30 22:02:04` | `cowrie.command.input` |
| `2026-04-30 22:02:05` | `cowrie.log.closed` |
| `2026-04-30 22:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96827e5b27d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:12` | `cowrie.session.connect` |
| `2026-04-30 22:02:12` | `cowrie.client.version` |
| `2026-04-30 22:02:12` | `cowrie.client.kex` |
| `2026-04-30 22:02:12` | `cowrie.login.success` |
| `2026-04-30 22:02:13` | `cowrie.session.params` |
| `2026-04-30 22:02:13` | `cowrie.command.input` |
| `2026-04-30 22:02:13` | `cowrie.log.closed` |
| `2026-04-30 22:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49847538f13

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:13` | `cowrie.session.connect` |
| `2026-04-30 22:02:13` | `cowrie.client.version` |
| `2026-04-30 22:02:13` | `cowrie.client.kex` |
| `2026-04-30 22:02:14` | `cowrie.login.success` |
| `2026-04-30 22:02:14` | `cowrie.session.params` |
| `2026-04-30 22:02:14` | `cowrie.command.input` |
| `2026-04-30 22:02:14` | `cowrie.log.closed` |
| `2026-04-30 22:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5567c5976102

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:14` | `cowrie.session.connect` |
| `2026-04-30 22:02:14` | `cowrie.client.version` |
| `2026-04-30 22:02:15` | `cowrie.client.kex` |
| `2026-04-30 22:02:15` | `cowrie.login.success` |
| `2026-04-30 22:02:16` | `cowrie.session.params` |
| `2026-04-30 22:02:16` | `cowrie.command.input` |
| `2026-04-30 22:02:16` | `cowrie.log.closed` |
| `2026-04-30 22:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a948035d85

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:16` | `cowrie.session.connect` |
| `2026-04-30 22:02:16` | `cowrie.client.version` |
| `2026-04-30 22:02:16` | `cowrie.client.kex` |
| `2026-04-30 22:02:17` | `cowrie.login.success` |
| `2026-04-30 22:02:17` | `cowrie.session.params` |
| `2026-04-30 22:02:17` | `cowrie.command.input` |
| `2026-04-30 22:02:17` | `cowrie.log.closed` |
| `2026-04-30 22:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f439eb003e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:17` | `cowrie.session.connect` |
| `2026-04-30 22:02:17` | `cowrie.client.version` |
| `2026-04-30 22:02:18` | `cowrie.client.kex` |
| `2026-04-30 22:02:18` | `cowrie.login.success` |
| `2026-04-30 22:02:18` | `cowrie.session.params` |
| `2026-04-30 22:02:18` | `cowrie.command.input` |
| `2026-04-30 22:02:19` | `cowrie.log.closed` |
| `2026-04-30 22:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a147c7a25830

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:19` | `cowrie.session.connect` |
| `2026-04-30 22:02:19` | `cowrie.client.version` |
| `2026-04-30 22:02:19` | `cowrie.client.kex` |
| `2026-04-30 22:02:20` | `cowrie.login.success` |
| `2026-04-30 22:02:20` | `cowrie.session.params` |
| `2026-04-30 22:02:20` | `cowrie.command.input` |
| `2026-04-30 22:02:20` | `cowrie.log.closed` |
| `2026-04-30 22:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f6a76dcb133

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:20` | `cowrie.session.connect` |
| `2026-04-30 22:02:20` | `cowrie.client.version` |
| `2026-04-30 22:02:20` | `cowrie.client.kex` |
| `2026-04-30 22:02:20` | `cowrie.login.success` |
| `2026-04-30 22:02:21` | `cowrie.session.params` |
| `2026-04-30 22:02:21` | `cowrie.command.input` |
| `2026-04-30 22:02:21` | `cowrie.log.closed` |
| `2026-04-30 22:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52fa338380d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:20` | `cowrie.session.connect` |
| `2026-04-30 22:02:20` | `cowrie.client.version` |
| `2026-04-30 22:02:20` | `cowrie.client.kex` |
| `2026-04-30 22:02:21` | `cowrie.login.success` |
| `2026-04-30 22:02:21` | `cowrie.session.params` |
| `2026-04-30 22:02:21` | `cowrie.command.input` |
| `2026-04-30 22:02:22` | `cowrie.log.closed` |
| `2026-04-30 22:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0b3caf039e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:21` | `cowrie.session.connect` |
| `2026-04-30 22:02:21` | `cowrie.client.version` |
| `2026-04-30 22:02:21` | `cowrie.client.kex` |
| `2026-04-30 22:02:22` | `cowrie.login.success` |
| `2026-04-30 22:02:22` | `cowrie.session.params` |
| `2026-04-30 22:02:22` | `cowrie.command.input` |
| `2026-04-30 22:02:22` | `cowrie.log.closed` |
| `2026-04-30 22:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b31aaa0744

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:23` | `cowrie.session.connect` |
| `2026-04-30 22:02:23` | `cowrie.client.version` |
| `2026-04-30 22:02:23` | `cowrie.client.kex` |
| `2026-04-30 22:02:24` | `cowrie.login.success` |
| `2026-04-30 22:02:24` | `cowrie.session.params` |
| `2026-04-30 22:02:24` | `cowrie.command.input` |
| `2026-04-30 22:02:24` | `cowrie.log.closed` |
| `2026-04-30 22:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69d811f8fbef

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:23` | `cowrie.session.connect` |
| `2026-04-30 22:02:23` | `cowrie.client.version` |
| `2026-04-30 22:02:23` | `cowrie.client.kex` |
| `2026-04-30 22:02:23` | `cowrie.login.success` |
| `2026-04-30 22:02:24` | `cowrie.session.params` |
| `2026-04-30 22:02:24` | `cowrie.command.input` |
| `2026-04-30 22:02:24` | `cowrie.log.closed` |
| `2026-04-30 22:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8462e42caa

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:24` | `cowrie.session.connect` |
| `2026-04-30 22:02:24` | `cowrie.client.version` |
| `2026-04-30 22:02:24` | `cowrie.client.kex` |
| `2026-04-30 22:02:25` | `cowrie.login.success` |
| `2026-04-30 22:02:25` | `cowrie.session.params` |
| `2026-04-30 22:02:25` | `cowrie.command.input` |
| `2026-04-30 22:02:26` | `cowrie.log.closed` |
| `2026-04-30 22:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13bf19f49253

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:40` | `cowrie.session.connect` |
| `2026-04-30 22:02:40` | `cowrie.client.version` |
| `2026-04-30 22:02:40` | `cowrie.client.kex` |
| `2026-04-30 22:02:40` | `cowrie.login.success` |
| `2026-04-30 22:02:41` | `cowrie.session.params` |
| `2026-04-30 22:02:41` | `cowrie.command.input` |
| `2026-04-30 22:02:41` | `cowrie.log.closed` |
| `2026-04-30 22:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf17a59c438

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:41` | `cowrie.session.connect` |
| `2026-04-30 22:02:41` | `cowrie.client.version` |
| `2026-04-30 22:02:41` | `cowrie.client.kex` |
| `2026-04-30 22:02:41` | `cowrie.login.success` |
| `2026-04-30 22:02:42` | `cowrie.session.params` |
| `2026-04-30 22:02:42` | `cowrie.command.input` |
| `2026-04-30 22:02:42` | `cowrie.log.closed` |
| `2026-04-30 22:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5de122473d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:41` | `cowrie.session.connect` |
| `2026-04-30 22:02:41` | `cowrie.client.version` |
| `2026-04-30 22:02:41` | `cowrie.client.kex` |
| `2026-04-30 22:02:42` | `cowrie.login.success` |
| `2026-04-30 22:02:42` | `cowrie.session.params` |
| `2026-04-30 22:02:42` | `cowrie.command.input` |
| `2026-04-30 22:02:42` | `cowrie.log.closed` |
| `2026-04-30 22:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd33a6771c65

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:42` | `cowrie.session.connect` |
| `2026-04-30 22:02:42` | `cowrie.client.version` |
| `2026-04-30 22:02:42` | `cowrie.client.kex` |
| `2026-04-30 22:02:43` | `cowrie.login.success` |
| `2026-04-30 22:02:43` | `cowrie.session.params` |
| `2026-04-30 22:02:43` | `cowrie.command.input` |
| `2026-04-30 22:02:44` | `cowrie.log.closed` |
| `2026-04-30 22:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec10312c721b

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:44` | `cowrie.session.connect` |
| `2026-04-30 22:02:44` | `cowrie.client.version` |
| `2026-04-30 22:02:44` | `cowrie.client.kex` |
| `2026-04-30 22:02:44` | `cowrie.login.success` |
| `2026-04-30 22:02:45` | `cowrie.session.params` |
| `2026-04-30 22:02:45` | `cowrie.command.input` |
| `2026-04-30 22:02:45` | `cowrie.log.closed` |
| `2026-04-30 22:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d34b67f05f

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:44` | `cowrie.session.connect` |
| `2026-04-30 22:02:44` | `cowrie.client.version` |
| `2026-04-30 22:02:44` | `cowrie.client.kex` |
| `2026-04-30 22:02:44` | `cowrie.login.success` |
| `2026-04-30 22:02:45` | `cowrie.session.params` |
| `2026-04-30 22:02:45` | `cowrie.command.input` |
| `2026-04-30 22:02:45` | `cowrie.log.closed` |
| `2026-04-30 22:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f037ea6a942

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:45` | `cowrie.session.connect` |
| `2026-04-30 22:02:45` | `cowrie.client.version` |
| `2026-04-30 22:02:45` | `cowrie.client.kex` |
| `2026-04-30 22:02:46` | `cowrie.login.success` |
| `2026-04-30 22:02:46` | `cowrie.session.params` |
| `2026-04-30 22:02:46` | `cowrie.command.input` |
| `2026-04-30 22:02:46` | `cowrie.log.closed` |
| `2026-04-30 22:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257d825eb582

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:45` | `cowrie.session.connect` |
| `2026-04-30 22:02:45` | `cowrie.client.version` |
| `2026-04-30 22:02:45` | `cowrie.client.kex` |
| `2026-04-30 22:02:46` | `cowrie.login.success` |
| `2026-04-30 22:02:46` | `cowrie.session.params` |
| `2026-04-30 22:02:46` | `cowrie.command.input` |
| `2026-04-30 22:02:46` | `cowrie.log.closed` |
| `2026-04-30 22:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0144f5ad22af

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:46` | `cowrie.session.connect` |
| `2026-04-30 22:02:46` | `cowrie.client.version` |
| `2026-04-30 22:02:47` | `cowrie.client.kex` |
| `2026-04-30 22:02:47` | `cowrie.login.success` |
| `2026-04-30 22:02:48` | `cowrie.session.params` |
| `2026-04-30 22:02:48` | `cowrie.command.input` |
| `2026-04-30 22:02:48` | `cowrie.log.closed` |
| `2026-04-30 22:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f14951476773

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:02 |
| **Last Seen** | 2026-04-30 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:02:47` | `cowrie.session.connect` |
| `2026-04-30 22:02:47` | `cowrie.client.version` |
| `2026-04-30 22:02:47` | `cowrie.client.kex` |
| `2026-04-30 22:02:47` | `cowrie.login.success` |
| `2026-04-30 22:02:48` | `cowrie.session.params` |
| `2026-04-30 22:02:48` | `cowrie.command.input` |
| `2026-04-30 22:02:48` | `cowrie.log.closed` |
| `2026-04-30 22:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739f86da0be4

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:03` | `cowrie.session.connect` |
| `2026-04-30 22:03:03` | `cowrie.client.version` |
| `2026-04-30 22:03:03` | `cowrie.client.kex` |
| `2026-04-30 22:03:04` | `cowrie.login.success` |
| `2026-04-30 22:03:04` | `cowrie.session.params` |
| `2026-04-30 22:03:04` | `cowrie.command.input` |
| `2026-04-30 22:03:04` | `cowrie.log.closed` |
| `2026-04-30 22:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a1ff8fc7f58

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:03` | `cowrie.session.connect` |
| `2026-04-30 22:03:03` | `cowrie.client.version` |
| `2026-04-30 22:03:03` | `cowrie.client.kex` |
| `2026-04-30 22:03:04` | `cowrie.login.success` |
| `2026-04-30 22:03:04` | `cowrie.session.params` |
| `2026-04-30 22:03:04` | `cowrie.command.input` |
| `2026-04-30 22:03:05` | `cowrie.log.closed` |
| `2026-04-30 22:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5439f26494d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:04` | `cowrie.session.connect` |
| `2026-04-30 22:03:04` | `cowrie.client.version` |
| `2026-04-30 22:03:05` | `cowrie.client.kex` |
| `2026-04-30 22:03:05` | `cowrie.login.success` |
| `2026-04-30 22:03:06` | `cowrie.session.params` |
| `2026-04-30 22:03:06` | `cowrie.command.input` |
| `2026-04-30 22:03:06` | `cowrie.log.closed` |
| `2026-04-30 22:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-426345783618

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:05` | `cowrie.session.connect` |
| `2026-04-30 22:03:05` | `cowrie.client.version` |
| `2026-04-30 22:03:05` | `cowrie.client.kex` |
| `2026-04-30 22:03:05` | `cowrie.login.success` |
| `2026-04-30 22:03:06` | `cowrie.session.params` |
| `2026-04-30 22:03:06` | `cowrie.command.input` |
| `2026-04-30 22:03:06` | `cowrie.log.closed` |
| `2026-04-30 22:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c31ab8f6cad

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:06` | `cowrie.session.connect` |
| `2026-04-30 22:03:06` | `cowrie.client.version` |
| `2026-04-30 22:03:06` | `cowrie.client.kex` |
| `2026-04-30 22:03:07` | `cowrie.login.success` |
| `2026-04-30 22:03:07` | `cowrie.session.params` |
| `2026-04-30 22:03:07` | `cowrie.command.input` |
| `2026-04-30 22:03:07` | `cowrie.log.closed` |
| `2026-04-30 22:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93109b79f675

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:06` | `cowrie.session.connect` |
| `2026-04-30 22:03:06` | `cowrie.client.version` |
| `2026-04-30 22:03:06` | `cowrie.client.kex` |
| `2026-04-30 22:03:07` | `cowrie.login.success` |
| `2026-04-30 22:03:07` | `cowrie.session.params` |
| `2026-04-30 22:03:07` | `cowrie.command.input` |
| `2026-04-30 22:03:07` | `cowrie.log.closed` |
| `2026-04-30 22:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a937284fac

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:15` | `cowrie.session.connect` |
| `2026-04-30 22:03:15` | `cowrie.client.version` |
| `2026-04-30 22:03:15` | `cowrie.client.kex` |
| `2026-04-30 22:03:15` | `cowrie.login.success` |
| `2026-04-30 22:03:16` | `cowrie.session.params` |
| `2026-04-30 22:03:16` | `cowrie.command.input` |
| `2026-04-30 22:03:16` | `cowrie.log.closed` |
| `2026-04-30 22:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1170a9db4c33

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:17` | `cowrie.session.connect` |
| `2026-04-30 22:03:17` | `cowrie.client.version` |
| `2026-04-30 22:03:17` | `cowrie.client.kex` |
| `2026-04-30 22:03:18` | `cowrie.login.success` |
| `2026-04-30 22:03:18` | `cowrie.session.params` |
| `2026-04-30 22:03:18` | `cowrie.command.input` |
| `2026-04-30 22:03:19` | `cowrie.log.closed` |
| `2026-04-30 22:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca25898ff7a

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:19` | `cowrie.session.connect` |
| `2026-04-30 22:03:19` | `cowrie.client.version` |
| `2026-04-30 22:03:19` | `cowrie.client.kex` |
| `2026-04-30 22:03:19` | `cowrie.login.success` |
| `2026-04-30 22:03:20` | `cowrie.session.params` |
| `2026-04-30 22:03:20` | `cowrie.command.input` |
| `2026-04-30 22:03:20` | `cowrie.log.closed` |
| `2026-04-30 22:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912329086e33

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:20` | `cowrie.session.connect` |
| `2026-04-30 22:03:20` | `cowrie.client.version` |
| `2026-04-30 22:03:20` | `cowrie.client.kex` |
| `2026-04-30 22:03:21` | `cowrie.login.success` |
| `2026-04-30 22:03:21` | `cowrie.session.params` |
| `2026-04-30 22:03:21` | `cowrie.command.input` |
| `2026-04-30 22:03:22` | `cowrie.log.closed` |
| `2026-04-30 22:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6117e675df4b

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:22` | `cowrie.session.connect` |
| `2026-04-30 22:03:22` | `cowrie.client.version` |
| `2026-04-30 22:03:22` | `cowrie.client.kex` |
| `2026-04-30 22:03:22` | `cowrie.login.success` |
| `2026-04-30 22:03:23` | `cowrie.session.params` |
| `2026-04-30 22:03:23` | `cowrie.command.input` |
| `2026-04-30 22:03:23` | `cowrie.log.closed` |
| `2026-04-30 22:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813e3faa348e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:23` | `cowrie.session.connect` |
| `2026-04-30 22:03:23` | `cowrie.client.version` |
| `2026-04-30 22:03:23` | `cowrie.client.kex` |
| `2026-04-30 22:03:24` | `cowrie.login.success` |
| `2026-04-30 22:03:24` | `cowrie.session.params` |
| `2026-04-30 22:03:24` | `cowrie.command.input` |
| `2026-04-30 22:03:24` | `cowrie.log.closed` |
| `2026-04-30 22:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbaef959bc63

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:23` | `cowrie.session.connect` |
| `2026-04-30 22:03:23` | `cowrie.client.version` |
| `2026-04-30 22:03:24` | `cowrie.client.kex` |
| `2026-04-30 22:03:24` | `cowrie.login.success` |
| `2026-04-30 22:03:24` | `cowrie.session.params` |
| `2026-04-30 22:03:24` | `cowrie.command.input` |
| `2026-04-30 22:03:25` | `cowrie.log.closed` |
| `2026-04-30 22:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb129940660e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:25` | `cowrie.session.connect` |
| `2026-04-30 22:03:25` | `cowrie.client.version` |
| `2026-04-30 22:03:25` | `cowrie.client.kex` |
| `2026-04-30 22:03:25` | `cowrie.login.success` |
| `2026-04-30 22:03:26` | `cowrie.session.params` |
| `2026-04-30 22:03:26` | `cowrie.command.input` |
| `2026-04-30 22:03:26` | `cowrie.log.closed` |
| `2026-04-30 22:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a6312600583

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:25` | `cowrie.session.connect` |
| `2026-04-30 22:03:25` | `cowrie.client.version` |
| `2026-04-30 22:03:25` | `cowrie.client.kex` |
| `2026-04-30 22:03:25` | `cowrie.login.success` |
| `2026-04-30 22:03:26` | `cowrie.session.params` |
| `2026-04-30 22:03:26` | `cowrie.command.input` |
| `2026-04-30 22:03:26` | `cowrie.log.closed` |
| `2026-04-30 22:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6607d90c4342

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:26` | `cowrie.session.connect` |
| `2026-04-30 22:03:26` | `cowrie.client.version` |
| `2026-04-30 22:03:26` | `cowrie.client.kex` |
| `2026-04-30 22:03:27` | `cowrie.login.success` |
| `2026-04-30 22:03:27` | `cowrie.session.params` |
| `2026-04-30 22:03:27` | `cowrie.command.input` |
| `2026-04-30 22:03:27` | `cowrie.log.closed` |
| `2026-04-30 22:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e63c2f3dded

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:26` | `cowrie.session.connect` |
| `2026-04-30 22:03:26` | `cowrie.client.version` |
| `2026-04-30 22:03:26` | `cowrie.client.kex` |
| `2026-04-30 22:03:27` | `cowrie.login.success` |
| `2026-04-30 22:03:27` | `cowrie.session.params` |
| `2026-04-30 22:03:27` | `cowrie.command.input` |
| `2026-04-30 22:03:27` | `cowrie.log.closed` |
| `2026-04-30 22:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1c3ebd5073

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:27` | `cowrie.session.connect` |
| `2026-04-30 22:03:27` | `cowrie.client.version` |
| `2026-04-30 22:03:28` | `cowrie.client.kex` |
| `2026-04-30 22:03:28` | `cowrie.login.success` |
| `2026-04-30 22:03:29` | `cowrie.session.params` |
| `2026-04-30 22:03:29` | `cowrie.command.input` |
| `2026-04-30 22:03:29` | `cowrie.log.closed` |
| `2026-04-30 22:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0168b23837b

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:28` | `cowrie.session.connect` |
| `2026-04-30 22:03:28` | `cowrie.client.version` |
| `2026-04-30 22:03:28` | `cowrie.client.kex` |
| `2026-04-30 22:03:28` | `cowrie.login.success` |
| `2026-04-30 22:03:29` | `cowrie.session.params` |
| `2026-04-30 22:03:29` | `cowrie.command.input` |
| `2026-04-30 22:03:29` | `cowrie.log.closed` |
| `2026-04-30 22:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10680d4295d9

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:29` | `cowrie.session.connect` |
| `2026-04-30 22:03:29` | `cowrie.client.version` |
| `2026-04-30 22:03:29` | `cowrie.client.kex` |
| `2026-04-30 22:03:30` | `cowrie.login.success` |
| `2026-04-30 22:03:30` | `cowrie.session.params` |
| `2026-04-30 22:03:30` | `cowrie.command.input` |
| `2026-04-30 22:03:30` | `cowrie.log.closed` |
| `2026-04-30 22:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a067f948e4c

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:29` | `cowrie.session.connect` |
| `2026-04-30 22:03:29` | `cowrie.client.version` |
| `2026-04-30 22:03:29` | `cowrie.client.kex` |
| `2026-04-30 22:03:30` | `cowrie.login.success` |
| `2026-04-30 22:03:30` | `cowrie.session.params` |
| `2026-04-30 22:03:30` | `cowrie.command.input` |
| `2026-04-30 22:03:30` | `cowrie.log.closed` |
| `2026-04-30 22:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e20fdadc06

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:38` | `cowrie.session.connect` |
| `2026-04-30 22:03:38` | `cowrie.client.version` |
| `2026-04-30 22:03:38` | `cowrie.client.kex` |
| `2026-04-30 22:03:38` | `cowrie.login.success` |
| `2026-04-30 22:03:39` | `cowrie.session.params` |
| `2026-04-30 22:03:39` | `cowrie.command.input` |
| `2026-04-30 22:03:39` | `cowrie.log.closed` |
| `2026-04-30 22:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbd31068aa9

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:38` | `cowrie.session.connect` |
| `2026-04-30 22:03:38` | `cowrie.client.version` |
| `2026-04-30 22:03:38` | `cowrie.client.kex` |
| `2026-04-30 22:03:38` | `cowrie.login.success` |
| `2026-04-30 22:03:39` | `cowrie.session.params` |
| `2026-04-30 22:03:39` | `cowrie.command.input` |
| `2026-04-30 22:03:39` | `cowrie.log.closed` |
| `2026-04-30 22:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a61cb86b53a

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:39` | `cowrie.session.connect` |
| `2026-04-30 22:03:39` | `cowrie.client.version` |
| `2026-04-30 22:03:39` | `cowrie.client.kex` |
| `2026-04-30 22:03:40` | `cowrie.login.success` |
| `2026-04-30 22:03:40` | `cowrie.session.params` |
| `2026-04-30 22:03:40` | `cowrie.command.input` |
| `2026-04-30 22:03:40` | `cowrie.log.closed` |
| `2026-04-30 22:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03224caf411e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:39` | `cowrie.session.connect` |
| `2026-04-30 22:03:39` | `cowrie.client.version` |
| `2026-04-30 22:03:40` | `cowrie.client.kex` |
| `2026-04-30 22:03:40` | `cowrie.login.success` |
| `2026-04-30 22:03:41` | `cowrie.session.params` |
| `2026-04-30 22:03:41` | `cowrie.command.input` |
| `2026-04-30 22:03:41` | `cowrie.log.closed` |
| `2026-04-30 22:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4506f62565f7

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:40` | `cowrie.session.connect` |
| `2026-04-30 22:03:40` | `cowrie.client.version` |
| `2026-04-30 22:03:41` | `cowrie.client.kex` |
| `2026-04-30 22:03:41` | `cowrie.login.success` |
| `2026-04-30 22:03:41` | `cowrie.session.params` |
| `2026-04-30 22:03:41` | `cowrie.command.input` |
| `2026-04-30 22:03:42` | `cowrie.log.closed` |
| `2026-04-30 22:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf70e087cf6

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:41` | `cowrie.session.connect` |
| `2026-04-30 22:03:41` | `cowrie.client.version` |
| `2026-04-30 22:03:41` | `cowrie.client.kex` |
| `2026-04-30 22:03:42` | `cowrie.login.success` |
| `2026-04-30 22:03:42` | `cowrie.session.params` |
| `2026-04-30 22:03:42` | `cowrie.command.input` |
| `2026-04-30 22:03:42` | `cowrie.log.closed` |
| `2026-04-30 22:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aeb68cd01e4

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:42` | `cowrie.session.connect` |
| `2026-04-30 22:03:42` | `cowrie.client.version` |
| `2026-04-30 22:03:42` | `cowrie.client.kex` |
| `2026-04-30 22:03:42` | `cowrie.login.success` |
| `2026-04-30 22:03:43` | `cowrie.session.params` |
| `2026-04-30 22:03:43` | `cowrie.command.input` |
| `2026-04-30 22:03:43` | `cowrie.log.closed` |
| `2026-04-30 22:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c483b620743

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:42` | `cowrie.session.connect` |
| `2026-04-30 22:03:42` | `cowrie.client.version` |
| `2026-04-30 22:03:43` | `cowrie.client.kex` |
| `2026-04-30 22:03:43` | `cowrie.login.success` |
| `2026-04-30 22:03:44` | `cowrie.session.params` |
| `2026-04-30 22:03:44` | `cowrie.command.input` |
| `2026-04-30 22:03:44` | `cowrie.log.closed` |
| `2026-04-30 22:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f884264f87f6

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:43` | `cowrie.session.connect` |
| `2026-04-30 22:03:43` | `cowrie.client.version` |
| `2026-04-30 22:03:43` | `cowrie.client.kex` |
| `2026-04-30 22:03:44` | `cowrie.login.success` |
| `2026-04-30 22:03:44` | `cowrie.session.params` |
| `2026-04-30 22:03:44` | `cowrie.command.input` |
| `2026-04-30 22:03:44` | `cowrie.log.closed` |
| `2026-04-30 22:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510cddb9a9fb

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:44` | `cowrie.session.connect` |
| `2026-04-30 22:03:44` | `cowrie.client.version` |
| `2026-04-30 22:03:44` | `cowrie.client.kex` |
| `2026-04-30 22:03:45` | `cowrie.login.success` |
| `2026-04-30 22:03:45` | `cowrie.session.params` |
| `2026-04-30 22:03:45` | `cowrie.command.input` |
| `2026-04-30 22:03:45` | `cowrie.log.closed` |
| `2026-04-30 22:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d417afc6088

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:45` | `cowrie.session.connect` |
| `2026-04-30 22:03:45` | `cowrie.client.version` |
| `2026-04-30 22:03:45` | `cowrie.client.kex` |
| `2026-04-30 22:03:45` | `cowrie.login.success` |
| `2026-04-30 22:03:46` | `cowrie.session.params` |
| `2026-04-30 22:03:46` | `cowrie.command.input` |
| `2026-04-30 22:03:46` | `cowrie.log.closed` |
| `2026-04-30 22:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f887db15d7

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:45` | `cowrie.session.connect` |
| `2026-04-30 22:03:45` | `cowrie.client.version` |
| `2026-04-30 22:03:45` | `cowrie.client.kex` |
| `2026-04-30 22:03:46` | `cowrie.login.success` |
| `2026-04-30 22:03:47` | `cowrie.session.params` |
| `2026-04-30 22:03:47` | `cowrie.command.input` |
| `2026-04-30 22:03:47` | `cowrie.log.closed` |
| `2026-04-30 22:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18704fbf177d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:46` | `cowrie.session.connect` |
| `2026-04-30 22:03:46` | `cowrie.client.version` |
| `2026-04-30 22:03:46` | `cowrie.client.kex` |
| `2026-04-30 22:03:47` | `cowrie.login.success` |
| `2026-04-30 22:03:47` | `cowrie.session.params` |
| `2026-04-30 22:03:47` | `cowrie.command.input` |
| `2026-04-30 22:03:47` | `cowrie.log.closed` |
| `2026-04-30 22:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d208976e145

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:47` | `cowrie.session.connect` |
| `2026-04-30 22:03:47` | `cowrie.client.version` |
| `2026-04-30 22:03:47` | `cowrie.client.kex` |
| `2026-04-30 22:03:48` | `cowrie.login.success` |
| `2026-04-30 22:03:48` | `cowrie.session.params` |
| `2026-04-30 22:03:48` | `cowrie.command.input` |
| `2026-04-30 22:03:48` | `cowrie.log.closed` |
| `2026-04-30 22:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3b2cb52900

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:48` | `cowrie.session.connect` |
| `2026-04-30 22:03:48` | `cowrie.client.version` |
| `2026-04-30 22:03:48` | `cowrie.client.kex` |
| `2026-04-30 22:03:49` | `cowrie.login.success` |
| `2026-04-30 22:03:49` | `cowrie.session.params` |
| `2026-04-30 22:03:49` | `cowrie.command.input` |
| `2026-04-30 22:03:50` | `cowrie.log.closed` |
| `2026-04-30 22:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35c8c8425122

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:57` | `cowrie.session.connect` |
| `2026-04-30 22:03:57` | `cowrie.client.version` |
| `2026-04-30 22:03:57` | `cowrie.client.kex` |
| `2026-04-30 22:03:58` | `cowrie.login.success` |
| `2026-04-30 22:03:58` | `cowrie.session.params` |
| `2026-04-30 22:03:58` | `cowrie.command.input` |
| `2026-04-30 22:03:58` | `cowrie.log.closed` |
| `2026-04-30 22:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8a8003e3534

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:03 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:03:58` | `cowrie.session.connect` |
| `2026-04-30 22:03:58` | `cowrie.client.version` |
| `2026-04-30 22:03:59` | `cowrie.client.kex` |
| `2026-04-30 22:03:59` | `cowrie.login.success` |
| `2026-04-30 22:04:00` | `cowrie.session.params` |
| `2026-04-30 22:04:00` | `cowrie.command.input` |
| `2026-04-30 22:04:00` | `cowrie.log.closed` |
| `2026-04-30 22:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39880deed412

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:00` | `cowrie.session.connect` |
| `2026-04-30 22:04:00` | `cowrie.client.version` |
| `2026-04-30 22:04:00` | `cowrie.client.kex` |
| `2026-04-30 22:04:01` | `cowrie.login.success` |
| `2026-04-30 22:04:01` | `cowrie.session.params` |
| `2026-04-30 22:04:01` | `cowrie.command.input` |
| `2026-04-30 22:04:01` | `cowrie.log.closed` |
| `2026-04-30 22:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60ac01804f0

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:01` | `cowrie.session.connect` |
| `2026-04-30 22:04:01` | `cowrie.client.version` |
| `2026-04-30 22:04:01` | `cowrie.client.kex` |
| `2026-04-30 22:04:02` | `cowrie.login.success` |
| `2026-04-30 22:04:02` | `cowrie.session.params` |
| `2026-04-30 22:04:02` | `cowrie.command.input` |
| `2026-04-30 22:04:03` | `cowrie.log.closed` |
| `2026-04-30 22:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c54f300d160

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:03` | `cowrie.session.connect` |
| `2026-04-30 22:04:03` | `cowrie.client.version` |
| `2026-04-30 22:04:03` | `cowrie.client.kex` |
| `2026-04-30 22:04:03` | `cowrie.login.success` |
| `2026-04-30 22:04:04` | `cowrie.session.params` |
| `2026-04-30 22:04:04` | `cowrie.command.input` |
| `2026-04-30 22:04:04` | `cowrie.log.closed` |
| `2026-04-30 22:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7a42ffaf15

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:03` | `cowrie.session.connect` |
| `2026-04-30 22:04:03` | `cowrie.client.version` |
| `2026-04-30 22:04:04` | `cowrie.client.kex` |
| `2026-04-30 22:04:04` | `cowrie.login.success` |
| `2026-04-30 22:04:05` | `cowrie.session.params` |
| `2026-04-30 22:04:05` | `cowrie.command.input` |
| `2026-04-30 22:04:05` | `cowrie.log.closed` |
| `2026-04-30 22:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5a193ded42

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:05` | `cowrie.session.connect` |
| `2026-04-30 22:04:05` | `cowrie.client.version` |
| `2026-04-30 22:04:05` | `cowrie.client.kex` |
| `2026-04-30 22:04:05` | `cowrie.login.success` |
| `2026-04-30 22:04:06` | `cowrie.session.params` |
| `2026-04-30 22:04:06` | `cowrie.command.input` |
| `2026-04-30 22:04:06` | `cowrie.log.closed` |
| `2026-04-30 22:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa34a6b0f21

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:05` | `cowrie.session.connect` |
| `2026-04-30 22:04:05` | `cowrie.client.version` |
| `2026-04-30 22:04:05` | `cowrie.client.kex` |
| `2026-04-30 22:04:06` | `cowrie.login.success` |
| `2026-04-30 22:04:06` | `cowrie.session.params` |
| `2026-04-30 22:04:06` | `cowrie.command.input` |
| `2026-04-30 22:04:06` | `cowrie.log.closed` |
| `2026-04-30 22:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5a13f78786

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:06` | `cowrie.session.connect` |
| `2026-04-30 22:04:06` | `cowrie.client.version` |
| `2026-04-30 22:04:06` | `cowrie.client.kex` |
| `2026-04-30 22:04:07` | `cowrie.login.success` |
| `2026-04-30 22:04:07` | `cowrie.session.params` |
| `2026-04-30 22:04:07` | `cowrie.command.input` |
| `2026-04-30 22:04:07` | `cowrie.log.closed` |
| `2026-04-30 22:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834193246b5b

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:06` | `cowrie.session.connect` |
| `2026-04-30 22:04:06` | `cowrie.client.version` |
| `2026-04-30 22:04:07` | `cowrie.client.kex` |
| `2026-04-30 22:04:07` | `cowrie.login.success` |
| `2026-04-30 22:04:07` | `cowrie.session.params` |
| `2026-04-30 22:04:07` | `cowrie.command.input` |
| `2026-04-30 22:04:08` | `cowrie.log.closed` |
| `2026-04-30 22:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de19752972d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:07` | `cowrie.session.connect` |
| `2026-04-30 22:04:07` | `cowrie.client.version` |
| `2026-04-30 22:04:08` | `cowrie.client.kex` |
| `2026-04-30 22:04:08` | `cowrie.login.success` |
| `2026-04-30 22:04:09` | `cowrie.session.params` |
| `2026-04-30 22:04:09` | `cowrie.command.input` |
| `2026-04-30 22:04:09` | `cowrie.log.closed` |
| `2026-04-30 22:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f209238172c0

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:08` | `cowrie.session.connect` |
| `2026-04-30 22:04:08` | `cowrie.client.version` |
| `2026-04-30 22:04:08` | `cowrie.client.kex` |
| `2026-04-30 22:04:09` | `cowrie.login.success` |
| `2026-04-30 22:04:09` | `cowrie.session.params` |
| `2026-04-30 22:04:09` | `cowrie.command.input` |
| `2026-04-30 22:04:09` | `cowrie.log.closed` |
| `2026-04-30 22:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c3f619df61

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:09` | `cowrie.session.connect` |
| `2026-04-30 22:04:09` | `cowrie.client.version` |
| `2026-04-30 22:04:09` | `cowrie.client.kex` |
| `2026-04-30 22:04:10` | `cowrie.login.success` |
| `2026-04-30 22:04:10` | `cowrie.session.params` |
| `2026-04-30 22:04:10` | `cowrie.command.input` |
| `2026-04-30 22:04:10` | `cowrie.log.closed` |
| `2026-04-30 22:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34d441adadf

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:09` | `cowrie.session.connect` |
| `2026-04-30 22:04:09` | `cowrie.client.version` |
| `2026-04-30 22:04:10` | `cowrie.client.kex` |
| `2026-04-30 22:04:10` | `cowrie.login.success` |
| `2026-04-30 22:04:11` | `cowrie.session.params` |
| `2026-04-30 22:04:11` | `cowrie.command.input` |
| `2026-04-30 22:04:11` | `cowrie.log.closed` |
| `2026-04-30 22:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6427c750547

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:11` | `cowrie.session.connect` |
| `2026-04-30 22:04:11` | `cowrie.client.version` |
| `2026-04-30 22:04:11` | `cowrie.client.kex` |
| `2026-04-30 22:04:11` | `cowrie.login.success` |
| `2026-04-30 22:04:12` | `cowrie.session.params` |
| `2026-04-30 22:04:12` | `cowrie.command.input` |
| `2026-04-30 22:04:12` | `cowrie.log.closed` |
| `2026-04-30 22:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671f0fd768bc

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:19` | `cowrie.session.connect` |
| `2026-04-30 22:04:19` | `cowrie.client.version` |
| `2026-04-30 22:04:19` | `cowrie.client.kex` |
| `2026-04-30 22:04:20` | `cowrie.login.success` |
| `2026-04-30 22:04:20` | `cowrie.session.params` |
| `2026-04-30 22:04:20` | `cowrie.command.input` |
| `2026-04-30 22:04:21` | `cowrie.log.closed` |
| `2026-04-30 22:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62b25414501

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:21` | `cowrie.session.connect` |
| `2026-04-30 22:04:21` | `cowrie.client.version` |
| `2026-04-30 22:04:21` | `cowrie.client.kex` |
| `2026-04-30 22:04:21` | `cowrie.login.success` |
| `2026-04-30 22:04:22` | `cowrie.session.params` |
| `2026-04-30 22:04:22` | `cowrie.command.input` |
| `2026-04-30 22:04:22` | `cowrie.log.closed` |
| `2026-04-30 22:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2bd1f65b43e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:22` | `cowrie.session.connect` |
| `2026-04-30 22:04:22` | `cowrie.client.version` |
| `2026-04-30 22:04:22` | `cowrie.client.kex` |
| `2026-04-30 22:04:23` | `cowrie.login.success` |
| `2026-04-30 22:04:23` | `cowrie.session.params` |
| `2026-04-30 22:04:23` | `cowrie.command.input` |
| `2026-04-30 22:04:23` | `cowrie.log.closed` |
| `2026-04-30 22:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475d085d9266

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:24` | `cowrie.session.connect` |
| `2026-04-30 22:04:24` | `cowrie.client.version` |
| `2026-04-30 22:04:24` | `cowrie.client.kex` |
| `2026-04-30 22:04:24` | `cowrie.login.success` |
| `2026-04-30 22:04:25` | `cowrie.session.params` |
| `2026-04-30 22:04:25` | `cowrie.command.input` |
| `2026-04-30 22:04:25` | `cowrie.log.closed` |
| `2026-04-30 22:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed11bd43632e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:25` | `cowrie.session.connect` |
| `2026-04-30 22:04:25` | `cowrie.client.version` |
| `2026-04-30 22:04:25` | `cowrie.client.kex` |
| `2026-04-30 22:04:26` | `cowrie.login.success` |
| `2026-04-30 22:04:26` | `cowrie.session.params` |
| `2026-04-30 22:04:26` | `cowrie.command.input` |
| `2026-04-30 22:04:26` | `cowrie.log.closed` |
| `2026-04-30 22:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e7ffc2d5143

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:26` | `cowrie.session.connect` |
| `2026-04-30 22:04:26` | `cowrie.client.version` |
| `2026-04-30 22:04:26` | `cowrie.client.kex` |
| `2026-04-30 22:04:27` | `cowrie.login.success` |
| `2026-04-30 22:04:27` | `cowrie.session.params` |
| `2026-04-30 22:04:27` | `cowrie.command.input` |
| `2026-04-30 22:04:27` | `cowrie.log.closed` |
| `2026-04-30 22:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d551c54fd167

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:27` | `cowrie.session.connect` |
| `2026-04-30 22:04:27` | `cowrie.client.version` |
| `2026-04-30 22:04:27` | `cowrie.client.kex` |
| `2026-04-30 22:04:27` | `cowrie.login.success` |
| `2026-04-30 22:04:28` | `cowrie.session.params` |
| `2026-04-30 22:04:28` | `cowrie.command.input` |
| `2026-04-30 22:04:28` | `cowrie.log.closed` |
| `2026-04-30 22:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c0558a7aad5

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:27` | `cowrie.session.connect` |
| `2026-04-30 22:04:27` | `cowrie.client.version` |
| `2026-04-30 22:04:28` | `cowrie.client.kex` |
| `2026-04-30 22:04:28` | `cowrie.login.success` |
| `2026-04-30 22:04:28` | `cowrie.session.params` |
| `2026-04-30 22:04:28` | `cowrie.command.input` |
| `2026-04-30 22:04:29` | `cowrie.log.closed` |
| `2026-04-30 22:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df0bbd4962c

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:29` | `cowrie.session.connect` |
| `2026-04-30 22:04:29` | `cowrie.client.version` |
| `2026-04-30 22:04:29` | `cowrie.client.kex` |
| `2026-04-30 22:04:30` | `cowrie.login.success` |
| `2026-04-30 22:04:30` | `cowrie.session.params` |
| `2026-04-30 22:04:30` | `cowrie.command.input` |
| `2026-04-30 22:04:30` | `cowrie.log.closed` |
| `2026-04-30 22:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3048b8a11da9

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:29` | `cowrie.session.connect` |
| `2026-04-30 22:04:29` | `cowrie.client.version` |
| `2026-04-30 22:04:29` | `cowrie.client.kex` |
| `2026-04-30 22:04:30` | `cowrie.login.success` |
| `2026-04-30 22:04:30` | `cowrie.session.params` |
| `2026-04-30 22:04:30` | `cowrie.command.input` |
| `2026-04-30 22:04:30` | `cowrie.log.closed` |
| `2026-04-30 22:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2216842817b

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:30` | `cowrie.session.connect` |
| `2026-04-30 22:04:30` | `cowrie.client.version` |
| `2026-04-30 22:04:31` | `cowrie.client.kex` |
| `2026-04-30 22:04:31` | `cowrie.login.success` |
| `2026-04-30 22:04:32` | `cowrie.session.params` |
| `2026-04-30 22:04:32` | `cowrie.command.input` |
| `2026-04-30 22:04:32` | `cowrie.log.closed` |
| `2026-04-30 22:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2fabc0be6d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:32` | `cowrie.session.connect` |
| `2026-04-30 22:04:32` | `cowrie.client.version` |
| `2026-04-30 22:04:32` | `cowrie.client.kex` |
| `2026-04-30 22:04:33` | `cowrie.login.success` |
| `2026-04-30 22:04:33` | `cowrie.session.params` |
| `2026-04-30 22:04:33` | `cowrie.command.input` |
| `2026-04-30 22:04:33` | `cowrie.log.closed` |
| `2026-04-30 22:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a40adb45134

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:37` | `cowrie.session.connect` |
| `2026-04-30 22:04:37` | `cowrie.client.version` |
| `2026-04-30 22:04:38` | `cowrie.client.kex` |
| `2026-04-30 22:04:38` | `cowrie.login.success` |
| `2026-04-30 22:04:39` | `cowrie.session.params` |
| `2026-04-30 22:04:39` | `cowrie.command.input` |
| `2026-04-30 22:04:39` | `cowrie.log.closed` |
| `2026-04-30 22:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f903f7eaa42

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:39` | `cowrie.session.connect` |
| `2026-04-30 22:04:39` | `cowrie.client.version` |
| `2026-04-30 22:04:39` | `cowrie.client.kex` |
| `2026-04-30 22:04:40` | `cowrie.login.success` |
| `2026-04-30 22:04:40` | `cowrie.session.params` |
| `2026-04-30 22:04:40` | `cowrie.command.input` |
| `2026-04-30 22:04:40` | `cowrie.log.closed` |
| `2026-04-30 22:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9580dba11a8d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:40` | `cowrie.session.connect` |
| `2026-04-30 22:04:40` | `cowrie.client.version` |
| `2026-04-30 22:04:41` | `cowrie.client.kex` |
| `2026-04-30 22:04:41` | `cowrie.login.success` |
| `2026-04-30 22:04:42` | `cowrie.session.params` |
| `2026-04-30 22:04:42` | `cowrie.command.input` |
| `2026-04-30 22:04:42` | `cowrie.log.closed` |
| `2026-04-30 22:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c5fef22cbf

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:41` | `cowrie.session.connect` |
| `2026-04-30 22:04:41` | `cowrie.client.version` |
| `2026-04-30 22:04:41` | `cowrie.client.kex` |
| `2026-04-30 22:04:42` | `cowrie.login.success` |
| `2026-04-30 22:04:42` | `cowrie.session.params` |
| `2026-04-30 22:04:42` | `cowrie.command.input` |
| `2026-04-30 22:04:42` | `cowrie.log.closed` |
| `2026-04-30 22:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b8679ec8b5

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:42` | `cowrie.session.connect` |
| `2026-04-30 22:04:42` | `cowrie.client.version` |
| `2026-04-30 22:04:42` | `cowrie.client.kex` |
| `2026-04-30 22:04:43` | `cowrie.login.success` |
| `2026-04-30 22:04:43` | `cowrie.session.params` |
| `2026-04-30 22:04:43` | `cowrie.command.input` |
| `2026-04-30 22:04:43` | `cowrie.log.closed` |
| `2026-04-30 22:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0fa49d0ba3

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:42` | `cowrie.session.connect` |
| `2026-04-30 22:04:42` | `cowrie.client.version` |
| `2026-04-30 22:04:43` | `cowrie.client.kex` |
| `2026-04-30 22:04:43` | `cowrie.login.success` |
| `2026-04-30 22:04:43` | `cowrie.session.params` |
| `2026-04-30 22:04:43` | `cowrie.command.input` |
| `2026-04-30 22:04:44` | `cowrie.log.closed` |
| `2026-04-30 22:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b0ab712211

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:43` | `cowrie.session.connect` |
| `2026-04-30 22:04:43` | `cowrie.client.version` |
| `2026-04-30 22:04:43` | `cowrie.client.kex` |
| `2026-04-30 22:04:44` | `cowrie.login.success` |
| `2026-04-30 22:04:44` | `cowrie.session.params` |
| `2026-04-30 22:04:44` | `cowrie.command.input` |
| `2026-04-30 22:04:45` | `cowrie.log.closed` |
| `2026-04-30 22:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c478169adc2a

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:44` | `cowrie.session.connect` |
| `2026-04-30 22:04:44` | `cowrie.client.version` |
| `2026-04-30 22:04:44` | `cowrie.client.kex` |
| `2026-04-30 22:04:45` | `cowrie.login.success` |
| `2026-04-30 22:04:45` | `cowrie.session.params` |
| `2026-04-30 22:04:45` | `cowrie.command.input` |
| `2026-04-30 22:04:45` | `cowrie.log.closed` |
| `2026-04-30 22:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb0fa499759

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:45` | `cowrie.session.connect` |
| `2026-04-30 22:04:45` | `cowrie.client.version` |
| `2026-04-30 22:04:45` | `cowrie.client.kex` |
| `2026-04-30 22:04:46` | `cowrie.login.success` |
| `2026-04-30 22:04:46` | `cowrie.session.params` |
| `2026-04-30 22:04:46` | `cowrie.command.input` |
| `2026-04-30 22:04:46` | `cowrie.log.closed` |
| `2026-04-30 22:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6b625684c4

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:45` | `cowrie.session.connect` |
| `2026-04-30 22:04:45` | `cowrie.client.version` |
| `2026-04-30 22:04:45` | `cowrie.client.kex` |
| `2026-04-30 22:04:46` | `cowrie.login.success` |
| `2026-04-30 22:04:46` | `cowrie.session.params` |
| `2026-04-30 22:04:46` | `cowrie.command.input` |
| `2026-04-30 22:04:47` | `cowrie.log.closed` |
| `2026-04-30 22:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5ce2ae1bfd

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:47` | `cowrie.session.connect` |
| `2026-04-30 22:04:47` | `cowrie.client.version` |
| `2026-04-30 22:04:47` | `cowrie.client.kex` |
| `2026-04-30 22:04:47` | `cowrie.login.success` |
| `2026-04-30 22:04:48` | `cowrie.session.params` |
| `2026-04-30 22:04:48` | `cowrie.command.input` |
| `2026-04-30 22:04:48` | `cowrie.log.closed` |
| `2026-04-30 22:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbcb7e153f2b

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:48` | `cowrie.session.connect` |
| `2026-04-30 22:04:48` | `cowrie.client.version` |
| `2026-04-30 22:04:48` | `cowrie.client.kex` |
| `2026-04-30 22:04:49` | `cowrie.login.success` |
| `2026-04-30 22:04:49` | `cowrie.session.params` |
| `2026-04-30 22:04:49` | `cowrie.command.input` |
| `2026-04-30 22:04:49` | `cowrie.log.closed` |
| `2026-04-30 22:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285821a54bdc

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:49` | `cowrie.session.connect` |
| `2026-04-30 22:04:49` | `cowrie.client.version` |
| `2026-04-30 22:04:50` | `cowrie.client.kex` |
| `2026-04-30 22:04:50` | `cowrie.login.success` |
| `2026-04-30 22:04:51` | `cowrie.session.params` |
| `2026-04-30 22:04:51` | `cowrie.command.input` |
| `2026-04-30 22:04:51` | `cowrie.log.closed` |
| `2026-04-30 22:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ca116e09e2

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:50` | `cowrie.session.connect` |
| `2026-04-30 22:04:50` | `cowrie.client.version` |
| `2026-04-30 22:04:50` | `cowrie.client.kex` |
| `2026-04-30 22:04:50` | `cowrie.login.success` |
| `2026-04-30 22:04:51` | `cowrie.session.params` |
| `2026-04-30 22:04:51` | `cowrie.command.input` |
| `2026-04-30 22:04:51` | `cowrie.log.closed` |
| `2026-04-30 22:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65a15b5ad15

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:51` | `cowrie.session.connect` |
| `2026-04-30 22:04:51` | `cowrie.client.version` |
| `2026-04-30 22:04:51` | `cowrie.client.kex` |
| `2026-04-30 22:04:52` | `cowrie.login.success` |
| `2026-04-30 22:04:52` | `cowrie.session.params` |
| `2026-04-30 22:04:52` | `cowrie.command.input` |
| `2026-04-30 22:04:52` | `cowrie.log.closed` |
| `2026-04-30 22:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0bf6e76ee4

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:04 |
| **Last Seen** | 2026-04-30 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:04:51` | `cowrie.session.connect` |
| `2026-04-30 22:04:51` | `cowrie.client.version` |
| `2026-04-30 22:04:51` | `cowrie.client.kex` |
| `2026-04-30 22:04:52` | `cowrie.login.success` |
| `2026-04-30 22:04:52` | `cowrie.session.params` |
| `2026-04-30 22:04:52` | `cowrie.command.input` |
| `2026-04-30 22:04:52` | `cowrie.log.closed` |
| `2026-04-30 22:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ea47ad0a89

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:07` | `cowrie.session.connect` |
| `2026-04-30 22:05:07` | `cowrie.client.version` |
| `2026-04-30 22:05:08` | `cowrie.client.kex` |
| `2026-04-30 22:05:08` | `cowrie.login.success` |
| `2026-04-30 22:05:09` | `cowrie.session.params` |
| `2026-04-30 22:05:09` | `cowrie.command.input` |
| `2026-04-30 22:05:09` | `cowrie.log.closed` |
| `2026-04-30 22:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3957188275ee

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:08` | `cowrie.session.connect` |
| `2026-04-30 22:05:08` | `cowrie.client.version` |
| `2026-04-30 22:05:08` | `cowrie.client.kex` |
| `2026-04-30 22:05:09` | `cowrie.login.success` |
| `2026-04-30 22:05:09` | `cowrie.session.params` |
| `2026-04-30 22:05:09` | `cowrie.command.input` |
| `2026-04-30 22:05:10` | `cowrie.log.closed` |
| `2026-04-30 22:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93076572b18e

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:09` | `cowrie.session.connect` |
| `2026-04-30 22:05:09` | `cowrie.client.version` |
| `2026-04-30 22:05:09` | `cowrie.client.kex` |
| `2026-04-30 22:05:10` | `cowrie.login.success` |
| `2026-04-30 22:05:10` | `cowrie.session.params` |
| `2026-04-30 22:05:10` | `cowrie.command.input` |
| `2026-04-30 22:05:10` | `cowrie.log.closed` |
| `2026-04-30 22:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97d52e8a701

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:10` | `cowrie.session.connect` |
| `2026-04-30 22:05:10` | `cowrie.client.version` |
| `2026-04-30 22:05:11` | `cowrie.client.kex` |
| `2026-04-30 22:05:11` | `cowrie.login.success` |
| `2026-04-30 22:05:11` | `cowrie.session.params` |
| `2026-04-30 22:05:11` | `cowrie.command.input` |
| `2026-04-30 22:05:12` | `cowrie.log.closed` |
| `2026-04-30 22:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cd476442b2

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:11` | `cowrie.session.connect` |
| `2026-04-30 22:05:11` | `cowrie.client.version` |
| `2026-04-30 22:05:11` | `cowrie.client.kex` |
| `2026-04-30 22:05:11` | `cowrie.login.success` |
| `2026-04-30 22:05:12` | `cowrie.session.params` |
| `2026-04-30 22:05:12` | `cowrie.command.input` |
| `2026-04-30 22:05:12` | `cowrie.log.closed` |
| `2026-04-30 22:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec5f9ec2d3d

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:12` | `cowrie.session.connect` |
| `2026-04-30 22:05:12` | `cowrie.client.version` |
| `2026-04-30 22:05:12` | `cowrie.client.kex` |
| `2026-04-30 22:05:12` | `cowrie.login.success` |
| `2026-04-30 22:05:13` | `cowrie.session.params` |
| `2026-04-30 22:05:13` | `cowrie.command.input` |
| `2026-04-30 22:05:13` | `cowrie.log.closed` |
| `2026-04-30 22:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6ffa40e878

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:12` | `cowrie.session.connect` |
| `2026-04-30 22:05:12` | `cowrie.client.version` |
| `2026-04-30 22:05:12` | `cowrie.client.kex` |
| `2026-04-30 22:05:13` | `cowrie.login.success` |
| `2026-04-30 22:05:13` | `cowrie.session.params` |
| `2026-04-30 22:05:13` | `cowrie.command.input` |
| `2026-04-30 22:05:13` | `cowrie.log.closed` |
| `2026-04-30 22:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea74156d449

| Field | Detail |
|---|---|
| **Source IP** | `111.61.104[.]0` |
| **First Seen** | 2026-04-30 22:05 |
| **Last Seen** | 2026-04-30 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x6F\x6B"` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 22:05:13` | `cowrie.session.connect` |
| `2026-04-30 22:05:13` | `cowrie.client.version` |
| `2026-04-30 22:05:13` | `cowrie.client.kex` |
| `2026-04-30 22:05:14` | `cowrie.login.success` |
| `2026-04-30 22:05:14` | `cowrie.session.params` |
| `2026-04-30 22:05:14` | `cowrie.command.input` |
| `2026-04-30 22:05:14` | `cowrie.log.closed` |
| `2026-04-30 22:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.61.104[.]0` to AbuseIPDB if not already reported
- [ ] Block `111.61.104[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.78[.]222` | **29** | 2026-04-30 22:02 | 2026-04-30 22:43 | 42m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `222.71.205[.]34` | **26** | 2026-04-30 22:00 | 2026-04-30 22:44 | 42m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.1.106[.]74` | **8** | 2026-04-30 22:54 | 2026-04-30 22:56 | 1m | 0 | `T1592` | 🟢 LOW |
| `183.7.13[.]169` | **4** | 2026-04-30 21:10 | 2026-04-30 21:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `179.130.170[.]172` | **3** | 2026-04-30 22:05 | 2026-04-30 22:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]134` | **3** | 2026-04-30 22:41 | 2026-04-30 22:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.160.130[.]8` | 1 | 2026-04-30 22:43 | 2026-04-30 22:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `106.13.56[.]137` | 1 | 2026-04-30 22:38 | 2026-04-30 22:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.159[.]237` | 1 | 2026-04-30 22:03 | 2026-04-30 22:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.120.156[.]87` | 1 | 2026-04-30 21:25 | 2026-04-30 21:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `43.226.40[.]202` | 1 | 2026-04-30 22:41 | 2026-04-30 22:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]223` | 1 | 2026-04-30 22:02 | 2026-04-30 22:02 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
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
| `183.7.13[.]169` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `179.130.170[.]172` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 7 |
| `87.236.176[.]223` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `202.165.15[.]88` | MY | TM ONE Cloud Alpha Edge | **100** ⚠️ | 23 |
| `66.132.172[.]134` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `103.160.130[.]8` | AU | ARCTEL | **100** ⚠️ | 7 |
| `106.13.56[.]137` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 19 |
| `119.96.159[.]237` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `120.48.78[.]222` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 3 |
| `43.226.40[.]202` | CN | Shenzhen Qianhai bird cloud computing Co. Ltd. | **100** ⚠️ | 49 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 197 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 133 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (811 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 10 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 40 |
| AbuseIPDB score 17 below threshold 25 | 165 |
| AbuseIPDB score 3 below threshold 25 | 24 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 577 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1023 cases |
| Tool 34  | Credential Extractor        | ✅ 148 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 811 filtered (79.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 133 priority case(s) shown individually · 12 recon entry/entries in table (6 group(s) consolidating 73 session(s)).

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
_Report time: 2026-04-30T22:56:20Z_
